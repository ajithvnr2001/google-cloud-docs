---
url: https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/issue-requests/
title: Issue HTTPS requests \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:37.428015+00:00
---

# Issue HTTPS requests  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/issue-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Issue HTTPS requests Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

This page describes how to issue HTTP(S) requests from your App Engine app using the URL Fetch service for second-generation runtimes.

Before following the instructions on this page, we recommend you use language idiomatic solutions to issue HTTP(S) requests before using the URL Fetch service. The primary use case for using the URL Fetch is when you want to issue HTTP(S) requests to another App Engine app and assert your app's identity on that request.

For details on request size limits and which headers are sent in a URL Fetch request, see [Outbound requests](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/outbound-requests).

## Issue an HTTP request

To use the URL Fetch service to issue outbound HTTP(S) requests, call the `urlfetch` library. 

To issue an outbound HTTP request, use any of the following libraries:

  * For improved code portability, use the Python standard library [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) to issue HTTP requests.
  * Use a third-party library, like [`requests`](https://pypi.org/project/requests/).
  * Explicitly call the `urlfetch` library and use the [`urlfetch.fetch`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/Fetch) method.




### urllib.request

Import the `urllib.request` library:
    
    
    import urllib.request
    

Next, use `urllib.request` to perform the `GET` request:
    
    
    url = 'http://www.google.com/humans.txt'
    try:
        result = urllib.request.urlopen(url)
        self.response.write(result.read())
    except urllib.error.URLError:
        logging.exception('Caught exception fetching url')
    

### urlfetch

The following snippets demonstrate how to perform a basic HTTP `GET` request using `urlfetch`. First, import the `urlfetch` library from the App Engine SDK:
    
    
    from google.appengine.api import urlfetch

Use `urlfetch` to perform the `GET` request:
    
    
    url = 'http://www.google.com/humans.txt'
    try:
        result = urlfetch.fetch(url)
        if result.status_code == 200:
            self.response.write(result.content)
        else:
            self.response.status_code = result.status_code
    except urlfetch.Error:
        logging.exception('Caught exception fetching url')

The following snippet demonstrates how to perform a more advanced request, submitting data from a web form via a HTTP `POST` request using `urlfetch`:
    
    
    try:
        form_data = urllib.urlencode(UrlPostHandler.form_fields)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        result = urlfetch.fetch(
            url='http://localhost:8080/submit_form',
            payload=form_data,
            method=urlfetch.POST,
            headers=headers)
        self.response.write(result.content)
    except urlfetch.Error:
        logging.exception('Caught exception fetching url')

### Set a request timeout

Adjust the default deadline by using the `urlfetch.set_default_fetch_deadline()` function. This function stores the new default deadline on a thread-local variable, so it must be set for each request, for example, in a custom middleware.

### Disable redirects

**Important:** To improve the security of your app, it is recommended that you disable redirects.

If you are using URL Fetch, the underlying URL Fetch service follows up to five redirects by default. These redirects could forward sensitive information, such as authorization headers, to the redirected destination. If your app does not require HTTP redirects, it is recommended that you disable the redirects.

To instruct the URL Fetch service to not follow redirects, set the `fetch` method's [`follow_redirects`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/Fetch) parameter to `False`.

## Issue an HTTPS request

By default, the underlying URL Fetch service validates the certificate of the host it contacts, and rejects requests if the certificate doesn't match. You don't need to explicitly secure your request.

### Disable host certificate validation

To disable automatic host certificate validation in URL Fetch, issue an HTTPS request, and set the `validate_certificate` parameter to `False` when calling the `urlfetch.fetch()` method.

## Issue an asynchronous request

HTTP(S) requests are synchronous by default. To issue an asynchronous request, your application must:

  1. Create a new RPC object using [`urlfetch.create_rpc()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/create_rpc). This object represents your asynchronous call in subsequent method calls.
  2. Call [`urlfetch.make_fetch_call()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/make_fetch_call) to make the request. This method takes your RPC object and the request target's URL as parameters.
  3. Call the RPC object's [`get_result()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch) method. This method returns the result object if the request is successful, and raises an exception if an error occurred during the request.



The following snippets demonstrate how to make a basic asynchronous request from a Python application. First, import the `urlfetch` library from the App Engine SDK:
    
    
    from google.appengine.api import urlfetch

Next, use `urlfetch` to make the asynchronous request:
    
    
    rpc = urlfetch.create_rpc()
    urlfetch.make_fetch_call(rpc, 'http://www.google.com/')
    
    # ... do other things ...
    try:
        result = rpc.get_result()
        if result.status_code == 200:
            text = result.content
            self.response.write(text)
        else:
            self.response.status_int = result.status_code
            self.response.write('URL returned status code {}'.format(
                result.status_code))
    except urlfetch.DownloadError:
        self.response.status_int = 500
        self.response.write('Error fetching URL')

### Set a request timeout

To set a timeout for your request, set the `urlfetch.create_rpc()` method's `deadline` parameter when you create your RPC object.

### Use a callback function

You can define a callback function for your RPC object. The function will be called when your application calls a method on the object—such as `wait()`, `checksuccess()`, or `get_result()`—that causes the object to wait for the request to complete.

To use a callback function to handle the result of your fetch call:

  1. Create a helper function to define the scope of the callback.
  2. Create a handler function to handle the result of your fetch call.
  3. Set your RPC object's `callback` attribute to the helper function.



The following snippet demonstrates how to invoke a callback function:
    
    
    def handle_result(rpc):
        result = rpc.get_result()
        self.response.write(result.content)
        logging.info('Handling RPC in callback: result {}'.format(result))
    
    urls = ['http://www.google.com',
            'http://www.github.com',
            'http://www.travis-ci.org']
    rpcs = []
    for url in urls:
        rpc = urlfetch.create_rpc()
        rpc.callback = functools.partial(handle_result, rpc)
        urlfetch.make_fetch_call(rpc, url)
        rpcs.append(rpc)
    
    # ... do other things ...
    
    # Finish all RPCs, and let callbacks process the results.
    
    for rpc in rpcs:
        rpc.wait()
    
    logging.info('Done waiting for RPCs')

## Issue a request to another App Engine app

When using URL Fetch to issue a request to another App Engine app, your app can assert its identity by adding the header `X-Appengine-Inbound-Appid` to the request.

If you instruct the URL Fetch service to not follow redirects, App Engine will add this header to requests automatically. See Disabling redirects for guidance on disabling redirects.

**Note:** If you are making requests to another App Engine application, use its `REGION_ID.r.appspot.com` domain name rather than a custom domain for your app.

## What's next

Learn about the URL Fetch service, such as the headers that are sent in a URL Fetch request in [Outbound Requests](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/outbound-requests).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
