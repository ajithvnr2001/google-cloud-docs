---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/access_from_python/
title: Accessing backend APIs from Python clients \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:30.930663+00:00
---

# Accessing backend APIs from Python clients  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/access_from_python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Accessing backend APIs from Python clients Stay organized with collections  Save and categorize content based on your preferences. 

If you want to access an Cloud Endpoints API from a Python client, you need to use the [Google APIs Python Client Library](https://github.com/google/google-api-python-client). If the API doesn't require any authentication, your client can access the API as shown in the following example code:
    
    
    import pprint
    
    from googleapiclient.discovery import build
    
    
    def main():
      # Build a service object for interacting with the API.
      api_root = 'https://guestbook.appspot.com/_ah/api'
      api = 'guestbook'
      version = 'v0.2'
      discovery_url = '%s/discovery/v1/apis/%s/%s/rest' % (api_root, api, version)
      service = build(api, version, discoveryServiceUrl=discovery_url)
    
      # Fetch all greetings and print them out.
      response = service.greetings().list().execute()
      pprint.pprint(response)
    
      # Fetch a single greeting and print it out.
      response = service.greetings().get(id='9001').execute()
      pprint.pprint(response)
    
    
    if __name__ == '__main__':
      main()

In the example code:

  * `api_root` is the frontend root URL under which your API methods are exposed. Usually, the URL is `https://YOUR_PROJECT_ID.appspot.com/_ah/api` where `YOUR_PROJECT_ID` represents your Google Cloud
  * `api` is the name of the API.
  * `version` is the version of the backend API.



### Accessing an API requiring Authentication

If the backend API requires authentication, you need use both the [Google APIs Python Client Library](https://github.com/google/google-api-python-client) and the [OAuth2.0 Client Library](https://github.com/google/oauth2client).

Your client can get the required authorization and access the API by using code similar to the following:
    
    
    import argparse
    import pprint
    import sys
    
    from googleapiclient import discovery
    import httplib2
    import oauth2client
    from oauth2client import tools
    
    
    CLIENT_ID = 'YOUR_CLIENT_ID'
    CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
    SCOPE = 'https://www.googleapis.com/auth/userinfo.email'
    USER_AGENT = 'my-cmdline-tool/1.0'
    OAUTH_DISPLAY_NAME = 'My Commandline Tool'
    
    
    def main(argv):
      # Parse command line flags used by the oauth2client library.
      parser = argparse.ArgumentParser(
          description='Auth sample',
          formatter_class=argparse.RawDescriptionHelpFormatter,
          parents=[tools.argparser])
      flags = parser.parse_args(argv[1:])
    
      # Acquire and store oauth token.
      storage = oauth2client.file.Storage('guestbook.dat')
      credentials = storage.get()
    
      if credentials is None or credentials.invalid:
        flow = oauth2client.client.OAuth2WebServerFlow(
            client_id=YOUR_CLIENT_ID,
            client_secret=YOUR_CLIENT_SECRET,
            scope=SCOPE,
            user_agent=USER_AGENT,
            oauth_displayname=OAUTH_DISPLAY_NAME)
        credentials = tools.run_flow(flow, storage, flags)
      http = httplib2.Http()
      http = credentials.authorize(http)
    
      # Build a service object for interacting with the API.
      api_root = 'https://guestbook.appspot.com/_ah/api'
      api = 'guestbook'
      version = 'v0.2'
      discovery_url = '%s/discovery/v1/apis/%s/%s/rest' % (api_root, api, version)
      service = discovery.build(
          api, version, discoveryServiceUrl=discovery_url, http=http)
    
      # Fetch all greetings and print them out.
      response = service.greetings().list().execute()
      pprint.pprint(response)
    
      # Fetch a single greeting and print it out.
      response = service.greetings().get(id='9001').execute()
      pprint.pprint(response)
    
    
    if __name__ == '__main__':
      main(sys.argv)

Notice that `SCOPE` must be set as shown. For information about `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET`, see [Creating client IDs](https://docs.cloud.google.com/endpoints/docs/frameworks/python/creating-client-ids).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
