import json
import os

'''
Environment vairables

export JENKINS_SRC_URL=
export JENKINS_SRC_UNAME=
export JENKINS_SRC_PASS=
export JENKINS_DST_URL=
export JENKINS_DST_UNAME=
export JENKINS_DST_PASS

'''

all_jobs = []


def get_jobs(url):
    get_jobs_cmd = "curl -s -k -u " + os.environ["JENKINS_SRC_UNAME"].strip() + ":" + os.environ[
        "JENKINS_SRC_PASS"].strip() + " " + url
    out = os.popen(get_jobs_cmd)
    src_jobs = json.loads(out.read())
    out.close()
    for job in src_jobs['jobs']:
        all_jobs.append(job)
        if job['_class'] == "com.cloudbees.hudson.plugins.folder.Folder":
            get_jobs(job['url'] + "/api/json")


get_jobs(os.environ['JENKINS_SRC_URL'] + "/api/json")

print(len(all_jobs))

for job in all_jobs:

    url = job['url']
    path = url.replace(os.environ['JENKINS_DST_URL'], "")

    if path.startswith('/'):
        path = path[1:]
    if path.endswith('/'):
        path = path[:-1]

    if job['_class'] == "com.cloudbees.hudson.plugins.folder.Folder":
        cmd = "curl -k -X POST -u " + os.environ['JENKINS_DST_UNAME'].strip() + ":" + os.environ[
            'JENKINS_DST_PASS'].strip() + " " + os.environ['JENKINS_DST_URL'] + path + "/createItem?name=" + job[
                  'name'] + "&mode=com.cloudbees.hudson.plugins.folder.Folder -H 'Content-Type: application/json'"
        # os.popen(cmd)
        print(cmd)
    else:
        get_config_cmd = "curl -s -k -u " + os.environ["JENKINS_SRC_UNAME"].strip() + ":" + os.environ[
            "JENKINS_SRC_PASS"].strip() + "  " + url + "config.xml " + " -o config.xml"
        # out = os.popen(get_config_cmd)
        print(get_config_cmd)
        cmd = "curl -k -X POST -u " + os.environ['JENKINS_DST_UNAME'].strip() + ":" + os.environ[
            'JENKINS_DST_PASS'].strip() + " " + os.environ['JENKINS_DST_URL'] + path + "/createItem?name=" + job[
                  'name'] + " --header Content-Type: 'application/xml' -d @config.xml"
        # os.popen(cmd)
        print(cmd)
