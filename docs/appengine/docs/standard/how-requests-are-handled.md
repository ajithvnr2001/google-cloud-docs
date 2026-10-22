---
url: https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled/
title: How requests are handled \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:28.332131+00:00
---

# How requests are handled  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  How requests are handled Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

This document describes how your App Engine application receives requests and sends responses. For more details, see the [Request Headers and Responses reference](https://docs.cloud.google.com/appengine/docs/standard/reference/request-headers).

If your application uses [services](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine), you can address requests to a specific service or a specific version of that service. For more information about service addressability, see [How Requests are Routed](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed).

## Handling requests

Your application is responsible for starting a webserver and handling requests. You can use any web framework that is available for your development language.

App Engine runs multiple instances of your application, and each instance has its own web server for handling requests. Any request can be routed to any instance, so consecutive requests from the same user are not necessarily sent to the same instance. An instance can handle multiple requests concurrently. The number of instances can be adjusted automatically as traffic changes. You can also change the number of concurrent requests an instance can handle by setting the `max_concurrent_requests` element in your [`app.yaml` file](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#max_concurrent_requests), or [`appengine-web.xml` file](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#automatic_scaling_max_concurrent_requests) file if using the App Engine legacy bundled services.

The following example is a Python script that responds to any HTTP request with the message 'Hello World!'
    
    
    # Copyright 2018 Google LLC
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
    
    from flask import Flask
    
    
    # If `entrypoint` is not defined in app.yaml, App Engine will look for an app
    # called `app` in `main.py`.
    app = Flask(__name__)
    
    
    @app.route("/")
    def hello():
        """Return a friendly HTTP greeting.
    
        Returns:
            A string with the words 'Hello World!'.
        """
        return "Hello World!"
    
    
    if __name__ == "__main__":
        # This is used when running locally only. When deploying to Google App
        # Engine, a webserver process such as Gunicorn will serve the app. You
        # can configure startup instructions by adding `entrypoint` to app.yaml.
        app.run(host="127.0.0.1", port=8080, debug=True)
    

## Quotas and limits

App Engine automatically allocates resources to your application as traffic increases. However, this is bound by the following restrictions:

  * App Engine reserves automatic scaling capacity for applications with low latency, where the application responds to requests in less than one second.

  * Applications that are heavily CPU-bound may also incur some additional latency in order to efficiently share resources with other applications on the same servers. Requests for static files are exempt from these latency limits.




Each incoming request to the application counts toward the **Requests** limit. Data sent in response to a request counts toward the **Outgoing Bandwidth (billable)** limit.

Both HTTP and HTTPS (secure) requests count toward the **Requests** , **Incoming Bandwidth (billable)** , and **Outgoing Bandwidth (billable)** limits. The Google Cloud console [Quota Details page](https://console.cloud.google.com/appengine/quotadetails) also reports **Secure Requests** , **Secure Incoming Bandwidth** , and **Secure Outgoing Bandwidth** as separate values for informational purposes. Only HTTPS requests count toward these values. For more information, see the [Quotas](https://docs.cloud.google.com/appengine/docs/quotas#Requests) page.

The following limits apply specifically to the use of request handlers:

Limit | Amount  
---|---  
Request size | 32 megabytes  
Response size | 32 megabytes  
Request timeout | [Depends on the type of scaling](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed#timeout) your app uses  
Maximum total number of files (app files and static files) | 10,000 total  
1,000 per directory  
Maximum size of an application file | 32 megabytes  
Maximum size of a static file | 32 megabytes  
Maximum total size of all application and static files | First 1 gigabyte is free  
$ 0.026 per gigabyte per month after first 1 gigabyte  
Pending request timeout | 10 seconds  
Maximum size of a single request header field | 8 kilobytes for [second-generation runtimes](https://docs.cloud.google.com/appengine/docs/standard/runtimes) in the standard environment. Requests to these runtimes with header fields exceeding 8 kilobytes will return HTTP 400 errors.  
  
### Request limits

All HTTP/2 requests will be translated into HTTP/1.1 requests when forwarded to the application server.

### Response limits

  * Dynamic responses are limited to 32 MB. If a script handler generates a response larger than this limit, the server sends back an empty response with a 500 Internal Server Error status code. This limitation doesn't apply to responses that serve data from [Cloud Storage](https://docs.cloud.google.com/appengine/docs/standard/using-cloud-storage) or the legacy Blobstore API if it is available in your runtime.

  * The response header limit is 8 KB for [second-generation runtimes](https://docs.cloud.google.com/appengine/docs/standard/runtimes). Response headers that exceed this limit will return HTTP 502 errors, with logs showing `upstream sent too big header while reading response header from upstream`.




## Request headers

An incoming HTTP request includes the HTTP headers sent by the client. For security purposes, some headers are sanitized or amended by intermediate proxies before they reach the application.

For more information, see the [Request headers reference](https://docs.cloud.google.com/appengine/docs/standard/reference/request-headers#request_headers).

## Handling request timeouts

App Engine is optimized for applications with short-lived requests, typically those that take a few hundred milliseconds. An efficient app responds quickly for the majority of requests. An app that doesn't respond quickly, won't scale well with App Engine's infrastructure. To ensure this level of performance, there is a system-imposed maximum [request timeout](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed#timeout) that every app must respond by.

If your app exceeds this deadline, App Engine interrupts the request handler.

## Responses

App Engine calls the handler script with a `Request` and waits for the script to return; all data written to the standard output stream is sent as the HTTP response.

There are size limits that apply to the response you generate, and the response may be modified before it is returned to the client.

For more information, see the [Request responses reference](https://docs.cloud.google.com/appengine/docs/standard/reference/request-headers#request_response).

### Streaming Responses

App Engine doesn't support streaming responses where data is sent in incremental chunks to the client while a request is being processed. All data from your code is collected as described above and sent as a single HTTP response.

## Response compression

For responses that are returned by your code, App Engine compresses data in the response if both of the following conditions are true:

  * The request contains the `Accept-Encoding` header that includes `gzip` as a value.
  * The response contains text-based data such as HTML, CSS, or JavaScript.



For responses that are returned by an App Engine [static file or directory handler](https://docs.cloud.google.com/appengine/docs/standard/serving-static-files#serving_from_your_application), response data is compressed if all of the following conditions are true:

  * The request includes `Accept-Encoding` with `gzip` as one of its values.
  * The client is capable of receiving the response data in a compressed format. The Google Front End (GFE) maintains a list of clients that are known to have problems with compressed responses. These clients won't receive compressed data from static handlers in your app, even if the request headers contain `Accept-Encoding: gzip`.
  * The response contains text-based data such as HTML, CSS, or JavaScript.



Note the following:

  * A client can force text-based content types to be compressed by setting both of the `Accept-Encoding` and `User-Agent` request headers to `gzip`.

  * If a request doesn't specify `gzip` in the `Accept-Encoding` header, App Engine won't compress the response data.

  * The Google Front End caches responses from App Engine static file and directory handlers. Depending on a variety of factors, such as which type of response data is cached first, which `Vary` headers you have specified in the response, and which headers are included in the request, a client could request compressed data but receive uncompressed data, and the other way around. For more information, see Response caching.




## Response caching

The Google Front End, and potentially the user's browser and other intermediate caching proxy servers, will cache your app's responses as instructed by [standard caching headers](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) that you specify in the response. You can specify these response headers either through your framework, directly in your code, or through App Engine [static file and directory handlers](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_element).

In the Google Front End, the cache key is the full URL of the request.

### Caching static content

To ensure that clients always receive updated static content as soon as it is published, we recommend that you serve static content from versioned directories, such as `css/v1/styles.css`. The Google Front End won't validate the cache (check for updated content) until the cache expires. Even after the cache expires, the cache won't be updated until the content at the request URL changes.

The following response headers that you can [set in `app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_http_headers) influence how and when the Google Front End caches content:

  * `Cache-Control` should be set to `public` for the Google Front End to cache content; it may also be cached by the Google Front End unless you specify a `Cache-Control` `private` or `no-store` directive. If you don't set this header in `app.yaml`, App Engine automatically adds it for all responses handled by a static file or directory handler. For more information, see [Headers added or replaced](https://docs.cloud.google.com/appengine/docs/standard/reference/request-headers#headers_added).

  * `Vary`: To enable the cache to return different responses for a URL based on headers that are sent in the request, set one or more of the following values in the `Vary` response header: `Accept`, `Accept-Encoding`, `Origin`, or `X-Origin`

Due to the potential for high cardinality, data won't be cached for other `Vary` values.

For example:

    1. You specify the following response header:

`Vary: Accept-Encoding`

    2. You app receives a request that contains the `Accept-Encoding: gzip` header. App Engine returns a compressed response and the Google Front End caches the gzipped version of the response data. All subsequent requests for this URL that contain the `Accept-Encoding: gzip` header will receive the gzipped data from the cache until the cache becomes invalidated (due to the content changing after the cache expires).

    3. Your app receives a request that doesn't contain the `Accept-Encoding` header. App Engine returns an uncompressed response and Google Frontend caches the uncompressed version of the response data. All subsequent requests for this URL that don't contain the `Accept-Encoding` header receive uncompressed data from the cache until the cache becomes invalidated.

If you don't specify a `Vary` response header, the Google Front End creates a single cache entry for the URL and will use it for all requests regardless of the headers in the request. For example:

    1. You don't specify the `Vary: Accept-Encoding` response header.
    2. A request contains the `Accept-Encoding: gzip` header, and the gzipped version of the response data will be cached.
    3. A second request doesn't contain the `Accept-Encoding: gzip` header. However, because the cache contains a gzipped version of the response data, the response will be gzipped even though the client requested uncompressed data.



The headers in the request also influence caching:

  * If the request contains an `Authorization` header, the content won't be cached by the Google Front End.



### Cache expiration

By default, the caching headers that App Engine static file and directory handlers add to responses instruct clients and web proxies such as the Google Front End to expire the cache after 10 minutes.

After a file is transmitted with a given expiration time, there is generally **no way** to clear it out of web-proxy caches, even if the user clears their own browser cache. Re-deploying a new version of the app will **not** reset any caches. Therefore, if you ever plan to modify a static file, it should have a short (less than one hour) expiration time. In most cases, the default 10-minute expiration time is appropriate.

You can change the default expiration for all static file and directory handlers by specifying the [`default_expiration`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#default_expiration) element in your `app.yaml` file. To set specific expiration times for individiual handlers, specify the [`expiration`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_expiration) element within the handler element in your `app.yaml` file.

The value you specify in the expiration elements time will be used to set the `Cache-Control` and `Expires` HTTP response headers.

## Forcing HTTPS connections

For security reasons, all applications should encourage clients to connect over `https`. To instruct the browser to prefer `https` over `http` for a given page or entire domain, set the `Strict-Transport-Security` header in your responses. For example:
    
    
    Strict-Transport-Security: max-age=31536000; includeSubDomains
    

To set this header for any static content that is served by your app, add the header to your app's [static file and directory handlers](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_http_headers).

To set this header for responses that are generated from your code, use the [`flask-talisman` library](https://github.com/GoogleCloudPlatform/flask-talisman#talisman-http-security-headers-for-flask). 

**Caution:** Clients that have received the header in the past will refuse to connect if `https` becomes non-functional or is disabled for any reason. To learn more, see this [Cheat Sheet on HTTP Strict Transport Security](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html).

## Handling asynchronous background work

Background work is any work that your app performs for a request after you have delivered your HTTP response. Avoid performing background work in your app, and review your code to make sure all asynchronous operations finish before you deliver your response.

For long-running jobs, we recommend using [Cloud Tasks](https://docs.cloud.google.com/tasks). With Cloud Tasks, HTTP requests are long-lived and return a response only after any asynchronous work ends.

**Warning:** Performing asynchronous background work can result in higher billing. App Engine might scale up additional instances due to high CPU load, even if there are no active requests. Users may also experience increased latency because of requests waiting in the pending queue for available instances.

## App Engine pending queue prioritization

During periods of heavy traffic, App Engine might place requests in a pending queue while waiting for an available instance with the following prioritization:

  * App Engine prioritizes other queued requests over pending queued requests from [Task queue](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue). Requests from [App Engine Cloud Tasks](https://docs.cloud.google.com/tasks/docs/creating-appengine-tasks) also share this pending queue priority behavior for compatibility reasons.

  * Within the pending queue, App Engine treats requests from [HTTP target Cloud Tasks](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks) as regular HTTP traffic. The HTTP target requests aren't at a lower priority.

  * When a service receives standard HTTP traffic at high volume while also serving Task queue or Cloud Tasks traffic at much lower volume, there is a disproportionate impact on the latency of the Task queue or the Cloud Tasks traffic. We recommend splitting the traffic types to separate versions or using HTTP target tasks to avoid priority queuing. You should also consider serving latency sensitive requests from Cloud Tasks with a dedicated major version or service.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
