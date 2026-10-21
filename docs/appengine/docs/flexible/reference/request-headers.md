---
url: https://docs.cloud.google.com/appengine/docs/flexible/reference/request-headers/
title: Request headers \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:02:24.879848+00:00
---

# Request headers  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/reference/request-headers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/flexible/apis)



Send feedback 

#  Request headers Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed#region-id). 

OK

Use this reference page for details about what HTTP headers are supported . To understand how App Engine receives requests and sends responses, see [How Requests Are Handled](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-handled).

## Request headers

An incoming HTTP request includes the HTTP headers sent by the client. For security purposes, some headers are sanitized, amended, or removed by intermediate proxies before they reach the application.

### Headers removed from incoming requests

The following headers are removed from incoming requests if a client sends them:

  * Headers with names that match the `X-Google-*` pattern. This name pattern is reserved for Google.

  * Headers with names that match App Engine-specific headers. Only exact, case-insensitive matches are removed. For example, headers named `X-Appengine-Country` or `X-AppEngine-Country` will be removed but `X-Appengine-Cntry` will not.




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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
