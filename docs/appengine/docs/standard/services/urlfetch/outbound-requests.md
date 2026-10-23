---
url: https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/outbound-requests/
title: URL Fetch for legacy bundled services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:32.474789+00:00
---

# URL Fetch for legacy bundled services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/outbound-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  URL Fetch for legacy bundled services Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

This page describes how to issue HTTP and HTTPS requests and receive responses using the URL Fetch service.

App Engine uses URL Fetch for all outbound requests in the Python 2 runtime, by default. However, to use URL Fetch for a [supported](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#python) Python runtime, you must explicitly call the `urlfetch` library. When you use the `urlfetch` library, your metadata server calls might fail, leading to issues in token generation for authorization. 

## Requests

You can use the URL Fetch service, or language idiomatic libraries to issue outbound requests.

In Python, you can use the [`urlfetch`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch) library directly, or the `urllib.request` or `requests` libraries to make HTTP requests. 

### Request protocols

An application can fetch a URL using either HTTP or HTTPS. The protocol that should be used is inferred by looking at the protocol in the target URL.

The URL to be fetched can use any port number in the following ranges:

  * `80` \- `90`
  * `440` \- `450`
  * `1024` \- `65535`



If the port is not mentioned in the URL, the port is implied by the protocol. HTTP requests occur on port `80`, and HTTPS requests occur on port `443`.

### Request methods

If you issue requests through the URL Fetch service, you can use any of the following HTTP methods:

  * `GET`
  * `POST`
  * `PUT`
  * `HEAD`
  * `DELETE`
  * `PATCH`



A request can include HTTP headers and, for `POST`, `PUT`, and `PATCH` requests, a payload.

### Request proxying

Note that the URL Fetch service uses an HTTP/1.1 compliant proxy to fetch the result.

To prevent an application from causing an endless recursion of requests, a request handler is not allowed to fetch its own URL. It is still possible to cause an endless recursion with other means, so exercise caution if your application can be made to fetch requests for URLs supplied by the user.

### Request headers

Your application can set HTTP headers for the outgoing request.

For example, when sending an HTTP `POST` request, if a `Content-Type` header is not set explicitly, the header is set to `x-www-form-urlencoded`. This is the content type used by web forms.

For security reasons, the following headers cannot be modified by the application:

  * `Content-Length`
  * `Host`
  * `Vary`
  * `Via`
  * `X-Appengine-Inbound-Appid`
  * `X-Forwarded-For`
  * `X-ProxyUser-IP`



These headers are set to accurate values by App Engine as appropriate. For example, App Engine calculates the `Content-Length` header from the request data and adds it to the request prior to sending.

The following headers indicate the application ID of the requesting app:

  * `User-Agent`. This header can be modified, but App Engine will append an identifier string to allow servers to identify App Engine requests. The appended string has the format `"AppEngine-Google; (+http://code.google.com/appengine; appid: APPID)"`, where `APPID` is your app's identifier.
  * `X-Appengine-Inbound-Appid`. This header cannot be modified, and is added automatically if the request is sent via the URL Fetch service, when the [follow redirects](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/issue-requests#disabling_redirects) parameter is set to `False`.



### Request timeouts

You can set a deadline, or timeout, for a request. By default, the timeout for a request is 10 seconds. 

You can send synchronous requests and asynchronous requests. The following behavior applies to the URL Fetch API:

  * _Synchronous requests_ : The fetch call waits until the remote host returns a result, and then returns control to the application. If the maximum wait time for the fetch call is exceeded, the call raises an exception.
  * _Asynchronous requests_ : The URL Fetch service starts the request, then returns immediately with an object. The application can perform other tasks while the URL is being fetched. When the application needs the results, it calls a method on the object, which waits for the request to finish if necessary, then returns the result. If any URL Fetch requests are pending when the request handler exits, the application server waits for all remaining requests to either return or reach their deadline before returning a response to the user.



## Secure connections and HTTPS

Your application can fetch a URL securely by using HTTPS to connect to secure servers. Request and response data are transmitted over the network in encrypted form.

By default, the URL Fetch proxy validates the host it contacts. This behavior allows the API to detect man-in-the-middle attacks between App Engine and the remote host when using HTTPS.

## Responses

If you use the URL Fetch API, note that the URL Fetch service returns all response data, including the response, code, headers, and body.

By default, if the URL Fetch service receives a response with a redirect code, the service will follow the redirect. The service will follow up to five redirect responses, then return the final resource. You can instruct the URL Fetch service to [not follow redirects](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/issue-requests#disabling_redirects) and instead return a redirect response to the application. **Note:** The URL Fetch API imposes response size limits. If the incoming response exceeds the maximum response size limit, the URL Fetch service raises an exception. See the Quotas and limits section for details. You can instruct the URL Fetch API to truncate the response instead of raising an exception. 

## Use URL Fetch on the development server

When your application is running on the App Engine development server on your computer, calls to the URL Fetch service are handled locally. The development server fetches URLs by contacting remote hosts directly from your computer, using whatever network configuration your computer is using to access the Internet.

When testing the features of your application that fetch URLs, make sure that your computer can access the remote hosts.

## Quotas and limits for URL Fetch

For information about URL Fetch service quotas, see [Quotas](https://docs.cloud.google.com/appengine/docs/quotas#UrlFetch). To see the current quota usage of your application, go to the Quota Details page in the Google Cloud console.

[Go to the Quota Details page](https://console.cloud.google.com/appengine/quotadetails)

In addition, the following limits apply to the use of the URL Fetch service:

Limit | Amount  
---|---  
Request size | 10 megabytes  
Request header size | 16 KB (Note that this limits the maximum length of the URL that can be specified in the header)  
Response size | 32 megabytes  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
