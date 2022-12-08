import os
import json
import sys

path = sys.argv[1]
create_job_path = sys.argv[2]

if not path:
   print("Path not provided as argument. Format is python create-job.py <jenkins-job-path> <create_job_path>")

if not create_job_path:
   print("Path not provided as argument. Format is python create-job.py <jenkins-job-path> <create_job_path>")

ojcli="java -Djavax.net.ssl.trustStore=mykeystore -Djavax.net.ssl.trustStorePassword=123456 -jar ~/Downloads/jenkins-cli.jar -webSocket -s https://abc-jenkins.xyz.com -auth user:11e3208a90d1127ad45133b0adbed3cb59  "
njcli="java -Djavax.net.ssl.trustStore=mykeystore -Djavax.net.ssl.trustStorePassword=123456 -jar ~/Downloads/jenkins-cli.jar -webSocket -s https://jenkins-abc.xyz.com -auth user:11e54864073a168cb116d4281d2bbed0cc  "

out = os.popen(ojcli + " list-jobs " + path)
jobs = out.read().split('\n')
print(jobs)

for job in jobs:
   get_job = ojcli + " get-job " + path.strip() + "/" + job.strip() + " > job_exports/" + job.strip() + ".xml"
   create_job = njcli + " create-job " + create_job_path.strip() + "/" + job.strip() + " > job_exports/" + job.strip() + ".xml"
   print(get_job)
   print(create_job)
   #os.popen(get_job)
   #os.popen(create_job)
