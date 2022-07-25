from elasticsearch import Elasticsearch
import json

client = Elasticsearch(hosts=["localhost"], 
                     port=9200, 
                     http_auth=('elastic', 'elastic'), 
                     ca_certs='http_ca.crt',
                     use_ssl=True, 
                     verify_certs=True)

#es = elasticsearch()


client = Elasticsearch(hosts=["localhost"], 
                     port=9200, 
                     http_auth=('elastic', 'elastic'), 
                     ca_certs='http_ca.crt',
                     use_ssl=True, 
                     verify_certs=True)


from elasticsearch_dsl import connections
client2 = connections.create_connection(hosts=["localhost"],
                     port=9200, 
                     http_auth=('elastic', 'elastic'), 
                     ca_certs='http_ca.crt',
                     use_ssl=True, 
                     verify_certs=True)

from elasticsearch.helpers import bulk

with open('companies.json') as f:
    records = json.load(f)
print(len(records))

resp = bulk(client, records, index = "companies")


# #### Connect to Elasticsearch on your machine

# ### Elasticsearch Queries<br>https://elasticsearch-dsl.readthedocs.io/en/latest/search_dsl.html

# In[ ]:


from elasticsearch_dsl import Search
from pprint import pprint
c
s = Search(using=client2, index="companies").query("match", country="China")  
response = s.execute() # by default you get 10 hits

#print(response)

for hit in response['hits']['hits']:
    pprint(hit['_source'].to_dict())


# #### Get revenue in descending order at the American companies (per description field)

# In[ ]:


s = Search(using=client2, index="companies") \
         .query("match", description="American") \
         .sort({'revenue': {'order': 'desc'}})

response = s.execute() # by default you get 10 hits

for hit in response:
    print(hit.company, hit.revenue)


# #### Search multi match query

# In[ ]:


from elasticsearch_dsl import Q

s = Search(using=client2, index="companies")
q = Q("multi_match", query='Tokyo', fields=['city', 'state'])

response = s.query(q).execute()
for hit in response['hits']['hits']:
    pprint(hit['_source'].to_dict())


# #### Multiple must queries with boolean condition

# In[ ]:


s = Search(using=client2, index="companies")
s.query = Q('bool', must=[Q('match', founded=1976), Q('match', state='California')])
response = s.execute()

for hit in response['hits']['hits']:
    pprint(hit['_source'].to_dict())


# #### Aggregate sum of the number of employees at the USA-based companies

# In[ ]:


s = Search(using=client2, index="companies")
s.query = Q('match', country='USA')
s.aggs.metric('total_revenue', 'sum', field="annual_revenue")
response = s.execute()
response.aggregations.total_revenue.value


# In[ ]:


s = Search(using=client2, index="companies")
#s.query = Q('match', country='China South Korea Japan')
s.aggs.metric('total_revenue', 'sum', field="annual_revenue")
response = s.execute()
response.aggregations.total_revenue.value


# ### Search queries on the bigger Netflix index

# #### Read Netflix JSON strings file

# In[ ]:


json_data = open("webhose_netflix.json").readlines()
newsfeeds = []
for line in json_data:
    newsfeeds.append(json.loads(line))
print(len(newsfeeds))


# In[ ]:


resp = bulk(client, newsfeeds, index = "netflix")


# In[ ]:


from elasticsearch_dsl import Search
from elasticsearch_dsl import Q

s = Search(using=client2, index="netflix").query("match", title="Fashion")   

response = s.execute() # by default you get 10 hits

for hit in response:
    print(hit.title, hit.published)


# In[ ]:


SCROLL_SIZE = 10
response = s[:SCROLL_SIZE].execute()
for hit in response:
    print(hit.title, hit.published)


# #### Run range queries filtered with time range against publish date

# ##### Using datetime package

# In[ ]:


from datetime import datetime
print(datetime.now())


# In[ ]:


TIME_FROM = datetime(2020, 5, 5)
TIME_TO   = datetime(2020, 5, 24)


# In[ ]:


s = Search(using=client, index="netflix") \
        .filter("range", published={'gte': TIME_FROM, 'lte': TIME_TO}) \
        .query("match_phrase", title="Los Angeles")
response = s.execute()
for hit in response:
    print(hit.title, hit.published[:10])


# ### Deleting indices

# In[ ]:


client.indices.delete(index='netflix', ignore=[400, 404])
client.indices.delete(index='companies', ignore=[400, 404])


# In[ ]:




