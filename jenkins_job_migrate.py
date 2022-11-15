import os
import sys
import json
import requests

'''
Environment vairables

export JENKINS_SRC_URL=
export JENKINS_SRC_UNAME=
export JENKINS_SRC_PASS=
export JENKINS_DST_URL=
export JENKINS_DST_UNAME=
export JENKINS_DST_PASS

'''

all_jobs=[]

def get_jobs(url):
  get_jobs_cmd = "curl -s -k -u " + os.environ["JENKINS_SRC_UNAME"].strip() + ":" + os.environ["JENKINS_SRC_UNAME"].strip() + " " + url
  out = os.popen(get_jobs_cmd)
  src_jobs = json.loads(out.read())
  out.close()
  for job in src_jobs['jobs']:
     all_jobs.append(job)
     if job['_class'] = "com.cloudbees.hudson.plugins.folder.Folder":
        get_jobs(job['url'] + "/api/json")

get_jobs(os.environ['JENKINS_SRC_URL']) + "/api/json")
