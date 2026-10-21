---
url: https://docs.cloud.google.com/talent-solution/job-search/libs/20161025-jobs-api-python-client-example.txt
title: https://docs.cloud.google.com/talent-solution/job-search/libs/20161025-jobs-api-python-client-example.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:01:47.303674+00:00
---

# https://docs.cloud.google.com/talent-solution/job-search/libs/20161025-jobs-api-python-client-example.txt

> Source: https://docs.cloud.google.com/talent-solution/job-search/libs/20161025-jobs-api-python-client-example.txt

import pprint import sys import json import httplib2 from apiclient.discovery import build_from_document from oauth2client.service_account import ServiceAccountCredentials scopes = ['https://www.googleapis.com/auth/jobs'] credentials = ServiceAccountCredentials.from_json_keyfile_name( 'key.json', scopes) http = httplib2.Http(".cache", disable_ssl_certificate_validation=True) content = open("discovery-doc.json",'r').read() discovery = json.loads(content) service = build_from_document(discovery, 'jobs', 'v2beta1', http=http, credentials=credentials) searchRequest={} request = service.jobs().search(body=searchRequest) pprint.pprint(request) response = request.execute() pprint.pprint(response) 
