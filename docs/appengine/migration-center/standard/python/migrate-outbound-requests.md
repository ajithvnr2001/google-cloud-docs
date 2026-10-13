---
url: https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-outbound-requests/
title: Migrating outbound requests \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:40.663849+00:00
---

# Migrating outbound requests  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-outbound-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrating outbound requests Stay organized with collections  Save and categorize content based on your preferences. 

By default, the Python 2.7 runtime uses the URL Fetch service to handle outbound HTTP(S) requests, even if you use the `urllib`, `urllib2`, or `httplib` Python libraries to issue those requests. URL Fetch does not handle requests from the `requests` library unless you explicitly enable it.

The Python 3 runtime doesn't need an intermediary service to handle outbound requests. If you want to migrate away from using [URL Fetch APIs](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch) but still need similar functionality, you should migrate those requests to use a standard Python library such as the [`requests` library](https://docs.python-requests.org/en/master/).

## Key differences between URL Fetch and standard Python libraries

  * The [size limit](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/outbound-requests) and [quotas](https://docs.cloud.google.com/appengine/docs/standard/quotas#UrlFetch) for requests that are handled by URL Fetch are different from the [size limit](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled#response_limits) and [quotas](https://docs.cloud.google.com/appengine/docs/standard/quotas#Requests) for requests that are **not** handled by URL Fetch.

  * With URL Fetch, when your app sends a request to another App Engine app, URL Fetch adds the `X-Appengine-Inbound-Appid` request header to assert the app's identity. The app that receives the request can use the identity to determine if it should process the request.

This header is only available in requests that are sent from your app if it uses URL Fetch. App Engine removes the header if you or a third-party adds it to a request.

For information about asserting and verifying identity without using URL Fetch, see [Migrating App Identity to OIDC ID Tokens](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-app-identity).

For an example of how to use the request header to verify the calling app's identity when requests are sent between App Engine apps, see the [App Engine to App Engine Request Sample](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/appengine/standard/migration/incoming).

  * You could use URL Fetch to set a [default timeout for all requests](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/issue-requests?tab=python#set_a_request_timeout). Most Python 3 libraries such as `requests` and `urllib` set the default timeout to `None`, so you should update each request your code makes to specify a timeout.




## Overview of the migration process

  1. If your app uses URL Fetch APIs to make requests, update your code to use a standard Python library instead. We recommend that you specify a timeout for each request.

  2. Test your outbound requests in the local development server.

  3. Configure your app to bypass URL Fetch when running in App Engine.

  4. Deploy your app.




## Replacing URL Fetch APIs with a Python library

  1. If you aren't already using a standard Python library to issue outgoing requests, choose a library and add it to your app's dependencies.

For example, to use the [Requests library](https://requests.readthedocs.io/en/master/) create a [`requirements.txt`](https://pip.pypa.io/en/latest/user_guide/#requirements-files) file in the same folder as your `app.yaml` file and add the following line:
         
         requests==2.24.0
         

For compatibility with Python 2, we recommend you pin the `requests` library to version 2.24.0. When you deploy your app, App Engine will download all of the dependencies that are defined in the `requirements.txt` file.

For local development, we recommend that you install dependencies in a virtual environment such as [venv](https://docs.python.org/3/library/venv.html).

  2. Search your code for any use of the `google.appengine.api.urlfetch` module, and update the code to use your Python library.




### Making simple HTTPS requests

The following example shows how to make a standard HTTPS request using the `requests` library: 
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    import logging
    
    from flask import Flask
    
    import requests
    
    
    app = Flask(__name__)
    
    
    @app.route("/")
    def index():
        url = "http://www.google.com/humans.txt"
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    
    
    @app.errorhandler(500)
    def server_error(e):
        logging.exception("An error occurred during a request.")
        return (
            """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(
                e
            ),
            500,
        )
    
    
    if __name__ == "__main__":
        # This is used when running locally.
        app.run(host="127.0.0.1", port=8080, debug=True)
    

### Making asynchronous HTTPS requests

The following example shows how to make an asynchronous HTTPS request using the `requests` library: 
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    import logging
    from time import sleep
    
    from flask import Flask
    from flask import make_response
    from requests_futures.sessions import FuturesSession
    
    
    TIMEOUT = 10  # Wait this many seconds for background calls to finish
    app = Flask(__name__)
    
    
    @app.route("/")  # Fetch and return remote page asynchronously
    def get_async():
        session = FuturesSession()
        url = "http://www.google.com/humans.txt"
    
        rpc = session.get(url)
    
        # ... do other things ...
    
        resp = make_response(rpc.result().text)
        resp.headers["Content-type"] = "text/plain"
        return resp
    
    
    @app.route("/callback")  # Fetch and return remote pages using callback
    def get_callback():
        global response_text
        global counter
    
        response_text = ""
        counter = 0
    
        def cb(resp, *args, **kwargs):
            global response_text
            global counter
    
            if 300 <= resp.status_code < 400:
                return  # ignore intermediate redirection responses
    
            counter += 1
            response_text += "Response number {} is {} bytes from {}\n".format(
                counter, len(resp.text), resp.url
            )
    
        session = FuturesSession()
        urls = [
            "https://google.com/",
            "https://www.google.com/humans.txt",
            "https://www.github.com",
            "https://www.travis-ci.org",
        ]
    
        futures = [session.get(url, hooks={"response": cb}) for url in urls]
    
        # No wait functionality in requests_futures, so check every second to
        # see if all callbacks are done, up to TIMEOUT seconds
        for elapsed_time in range(TIMEOUT + 1):
            all_done = True
            for future in futures:
                if not future.done():
                    all_done = False
                    break
            if all_done:
                break
            sleep(1)
    
        resp = make_response(response_text)
        resp.headers["Content-type"] = "text/plain"
        return resp
    
    
    @app.errorhandler(500)
    def server_error(e):
        logging.exception("An error occurred during a request.")
        return (
            """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(
                e
            ),
            500,
        )
    

## Testing locally

If you updated any of your outbound requests, run your app in the [local development server](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server) and confirm that the requests succeed.

## Bypassing URL Fetch

To stop URL Fetch from handling requests when you deploy your app to App Engine:

  1. In your `app.yaml` file, set the `GAE_USE_SOCKETS_HTTPLIB` environment variable to any value. The value can be any value including an empty string. For example:
         
         env_variables:
           GAE_USE_SOCKETS_HTTPLIB : ''
         

  2. If you enabled URL Fetch to handle requests sent from the `requests` library, you can remove the Requests [`AppEngineAdapter`](https://toolbelt.readthedocs.io/en/latest/adapters.html#appengineadapter) from your app.

For example, remove `requests_toolbelt.adapters.appengine` from your `appengine_config.py` file and `requests_toolbelt.adapters.appengine.monkeypatch()` from your Python files.




Note that even if you bypass URL Fetch as described in the previous steps, your app can still use the URL Fetch API directly.

## Deploying your app

Once you are ready to deploy your app, you should:

  1. [Test the app on App Engine](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#testing-on-app-engine).

View the App Engine Quotas page in the Google Cloud console to confirm that your app isn't making Url Fetch API Calls.

[View URL Fetch API Calls](https://console.cloud.google.com/appengine/quotadetails)

  2. If the app runs without errors, [use traffic splitting](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic) to slowly ramp up traffic for your updated app. Monitor the app closely for any issues before routing more traffic to the updated app.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
