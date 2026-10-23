---
url: https://docs.cloud.google.com/iap/docs/data-residency/
title: Data residency overview \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:09.662277+00:00
---

# Data residency overview  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/data-residency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Resources ](https://docs.cloud.google.com/iap/docs/resources)



Send feedback 

#  Data residency overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about how [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) meets data residency requirements. _Data residency_ describes where your data is stored and processed. When you data is stored and not being accessed or transferred, it is considered "at rest". When your data is being processed by IAP to provide authentication and authorization, it is considered "in use". IAP only handles data in use.

IAP only supports [region](https://cloud.google.com/about/locations) locations and does not adhere to multi-region or other geographical boundaries for compliance.

## Requirements for Data Residency

Identity-Aware Proxy is enabled on a load balancer, and will support _at most_ the location capabilities of the chosen load balancer. Due to the nature of authentication flows and redirects, IAP cannot offer data residency support for global load balancers. For all other load balancers, IAP will process your data only in the location(s) of the load balancer.

**Warning:** IAP does not support location based on the resource. If a load balancer routes to a resource in a different location, IAP will still process your data in the location of the load balancer.

## When Is Data In Use?

The following data is considered _in use_ by IAP:

  * Request headers, for example `"foo": "bar"
  * URL query parameters, such as "?param=data"

**Warning:** IAP will only enforce data residency for query parameters in the _URL query parameter string_. Any parameters embedded in the path, for example "/param(data)", and the path itself are not enforced.

## How Data Residency Is Enforced

IAP enforces data residency for _in use_ data in _all_ locations, _all_ the time.

### Request Headers

IAP uses request headers, such as `authorization` and `proxy-authorization`, to process requests properly. IAP does not send, route, receive, or redirect any incoming headers to a different location.

### URL Query Parameters

To ensure your data is not lost during authenticating redirects, IAP sets cookies on the browser to temporarily store query parameters until authentication is complete. The cookie is paginated to comply with varying browser cookie size specifications.

`__Secure_GCP_IAP_QUERY_PARAMS_page_<n>`

### Limitations

The number and size limitations of cookies is largely dependent on the specific browser. However, IAP enforces a limit of 16kb for query param size _after_ necessary encoding, or about 12kb plaintext. If this limit is exceeded the query params will be lost in redirects during authentication with no way to retrieve them from IAP.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
