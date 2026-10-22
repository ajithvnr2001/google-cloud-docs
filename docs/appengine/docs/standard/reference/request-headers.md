---
url: https://docs.cloud.google.com/appengine/docs/standard/reference/request-headers/
title: Request headers and responses \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:07.519697+00:00
---

# Request headers and responses  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/reference/request-headers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Request headers and responses Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

Use this reference page for details about what HTTP headers are supported as well as the request and response limits in App Engine. To understand how App Engine receives requests and sends responses, see [How Requests Are Handled](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled).

## Request headers

An incoming HTTP request includes the HTTP headers sent by the client. For security purposes, some headers are sanitized, amended, or removed by intermediate proxies before they reach the application.

### Headers removed from incoming requests

The following headers are removed from incoming requests if a client sends them:

  * Headers with names that match the `X-Google-*` pattern. This name pattern is reserved for Google.

  * Headers with names that match App Engine-specific headers. Only exact, case-insensitive matches are removed. For example, headers named `X-Appengine-Country` or `X-AppEngine-Country` will be removed but `X-Appengine-Cntry` will not.


In addition, the following headers are removed from incoming requests because they relate to the transfer of the HTTP data between the client and server: 
  * `Accept-Encoding`
  * `Connection`
  * `Keep-Alive`
  * `Proxy-Authorization`
  * `TE`
  * `Trailer`
  * `Transfer-Encoding`



For example, the server may automatically send a gzipped response depending on the value of the `Accept-Encoding` request header. The application itself does not need to know which content encodings the client can accept.

**Note:** Entity headers (headers relating to the request body) are not sanitized or checked, so applications should not rely on them. In particular, the `Content- MD5` request header is sent unmodified to the application, so may not match the MD5 hash of the content. Also, the `Content-Encoding` request header is not checked by the server, so if the client sends a gzipped request body, it will be sent in compressed form to the application. 

### App Engine-specific headers

As a service to the app, App Engine adds the following headers to all requests:

`X-Appengine-Country`
    Country from which the request originated, as an [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. App Engine determines this code from the client's IP address. Note that the country information is not derived from the WHOIS database; it's possible that an IP address with country information in the WHOIS database will not have country information in the `X-Appengine-Country` header. Your application should handle the special country code `ZZ` (unknown country).
`X-Appengine-Region`
    Name of region from which the request originated. This value only makes sense in the context of the country in `X -Appengine-Country`. For example, if the country is "US" and the region is "ca", that "ca" means "California", not Canada. The complete list of valid region values is found in the [ISO-3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) standard.
`X-Appengine-City`
    Name of the city from which the request originated. For example, a request from the city of Mountain View might have the header value `mountain view`. There is no canonical list of valid values for this header. If the city can't be resolved, the header value is set to `?`.
`X-Appengine-CityLatLong`
    Latitude and longitude of the city from which the request originated. This string might look like "37.386051,-122.083851" for a request from Mountain View. If the city can't be resolved, the header value is set to `0.000000,0.000000`.
`X-Cloud-Trace-Context`
    A unique identifier for the request used for [Cloud Trace](https://docs.cloud.google.com/trace) and [Cloud Logging](https://docs.cloud.google.com/logging). There isn't an option to disable this header or choose the sampling rate for tracing since all App Engine standard environment apps are traced automatically.
`X-Forwarded-For: CLIENT_IP,GLOBAL_FORWARDING_RULE_IP`
    

A comma-delimited list of IP addresses through which the client request has been routed. When a request passes through the load balancer, the load balancer appends two IP addresses to the `X-Forwarded-For` header in the following order:

  1. The IP address of the client that connects to the load balancer (CLIENT_IP).
  2. The IP address of the load balancer's forwarding rule (GLOBAL_FORWARDING_RULE_IP).



If an incoming request lacks this header, the load balancer creates and adds the header to the request using the following format:
    
    
        X-Forwarded-For: CLIENT_IP,GLOBAL_FORWARDING_RULE_IP
    

If an incoming request already includes this header (for example, if the client routed through other proxies), the load balancer appends to the header using the following format:
    
    
        X-Forwarded-For: PREVIOUS_ENTRIES,CLIENT_IP,GLOBAL_FORWARDING_RULE_IP
    

In this example, the variables represent the following:

  * CLIENT_IP: the IP address of the client that connected to the load balancer.
  * GLOBAL_FORWARDING_RULE_IP: the IP address of the load balancer's forwarding rule.
  * PREVIOUS_ENTRIES: any preceding IP addresses sent by the client or prior proxies.

**Caution:** The load balancer does not verify any IP addresses that precede `CLIENT_IP,GLOBAL_FORWARDING_RULE_IP` in this header. For more information, see [X-Forwarded-For header](https://docs.cloud.google.com/load-balancing/docs/https#x-forwarded-for_header).
`X-Forwarded-Proto [http | https]`
    

Shows `http` or `https` based on the protocol the client used to connect to your application.

The Google Cloud Load Balancer terminates all `https` connections, and then forwards traffic to App Engine instances over `http`. For example, if a user requests access to your site via `https://PROJECT_ID.REGION_ID.r.appspot.com`, the X- Forwarded-Proto header value is `https`.

In addition, App Engine may set the following headers which are for internal use by App Engine:

  * `X-Appengine-Https`
  * `X-Appengine-User-IP`
  * `X-Appengine-Api-Ticket`
  * `X-Appengine-Request-Log-Id`
  * `X-Appengine-Default-Version-Hostname`
  * `X-Appengine-Timeout-Ms`



App Engine services may add additional request headers:

  * Requests from the Cron Service add the following header:

`X-Appengine-Cron: true`

See [Securing URLs for cron](https://docs.cloud.google.com/appengine/docs/standard/scheduling-jobs-with-cron-yaml) for more details.



  * If you use the legacy bundled services:

    * For `login:admin` or `login:required` handlers specified in `app.yaml` file, App Engine adds the following set of headers:

      * `X-Appengine-User-Email`, with example header: "ange@example.com"
      * `X-Appengine-Auth-Domain`,with example header: "example.com"
      * `X-Appengine-User-ID`, with example header: "100979712376541954724"
      * `X-Appengine-User-Nickname`, with example header: "ange"
      * `X-Appengine-User-Organization`, with example header: "example.com"
      * `X-Appengine-User-Is-Admin`, with example header: "1"
    * [The Task Queue service](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue) adds [additional headers](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-handlers#reading_request_headers) to requests from that provide details about the task in the request, and the queue it is associated with.

    * Requests coming from other App Engine applications will include a header identifying the app making the request, if the requesting app is using the URL Fetch Service:

`X-Appengine-Inbound-Appid`

See the [App Identity documentation](https://docs.cloud.google.com/appengine/docs/standard/services/appidentity) for more details.




## Request responses

This HTTP header documentation only applies to responses to inbound HTTP requests. The response may be modified before it is returned to the client.

### Headers removed

The following headers are ignored and removed from the response:

  * `Connection`
  * `Content-Encoding`*
  * `Content-Length`
  * `Date`
  * `Keep-Alive`
  * `Proxy-Authenticate`
  * `Server`
  * `Trailer`
  * `Transfer-Encoding`
  * `Upgrade`



* May be re-added if the response is compressed by App Engine.

Headers with non-ASCII characters in either the name or value are also removed.

### Headers added or replaced

The following headers are added or replaced in the response:

`Cache-Control`, `Expires` and `Vary`
    

These headers specify caching policy to intermediate web proxies (such as the Google Frontend and Internet Service Providers) and browsers. If your app sets these response headers, they will usually be unmodified unless your app also sets a `Set-Cookie` header, or the response is generated for a user who is signed in using an administrator account.

If your app sets a `Set-Cookie` response header, the `Cache-Control` header will be set to `private` (if it is not already more restrictive) and the `Expires` header will be set to the current date (if it is not already in the past). Generally, this will allow browsers to cache the response, but not intermediate proxy servers. This is for security reasons, since if the response was cached publicly, another user could subsequently request the same resource, and retrieve the first user's cookie.

**Note:** For all runtimes except Java, the development server disables caching by default (for both script and static content), so that if you do not specify caching headers, you will not have cached content while developing your app.

If your app does not set the `Cache-Control` response header, the server may set it to `private` and add a `Vary: Accept-Encoding` header.

For more information about caching, including the list of `Vary` values that the Google Frontend supports, see [Response caching](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled#response_caching).

`Content-Encoding`
    

Depending upon the request headers and response `Content-Type`, the server may automatically compress the response body, as described above. In this case, it adds a `Content-Encoding: gzip` header to indicate that the body is compressed. See the section on response compression for more detail.

`Content-Length` or `Transfer-Encoding`
    

The server always ignores the `Content-Length` header returned by the application. It will either set `Content-Length` to the length of the body (after compression, if compression is applied), or delete `Content-Length`, and use chunked transfer encoding (adding a `Transfer-Encoding: chunked` header). If `Content-Length` is set incorrectly for second-generation runtimes, App Engine returns a 500 response. 

`Date`
    

Set to the current date and time.

`Server`
    Set to `Google Frontend`. The development server sets this to `Development/x`, where _x_ is the version number.

If you access dynamic pages on your site while signed in using an administrator account, App Engine includes per-request statistics in the response headers:

`X-Appengine-Resource-Usage`
    The resources used by the request, including server-side time as a number of milliseconds.

Responses with resource usage statistics will be made uncacheable.

### Response headers set in the application configuration

Custom HTTP Response headers can be set per URL for dynamic and static paths in your application's configuration file. See the `http_headers` sections in the [configuration documentation](https://docs.cloud.google.com/appengine/docs/standard/config/appref#handlers_http_headers) for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
