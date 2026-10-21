---
url: https://docs.cloud.google.com/media-cdn/quotas/
title: Quotas and limits \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:36:36.745473+00:00
---

# Quotas and limits  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Resources ](https://docs.cloud.google.com/media-cdn/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Media CDN.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Media CDN resources. System limits can't be changed. 

## Quotas

The following quotas apply to Media CDN. If you need a higher quota, contact your Google Cloud sales team and request adjustments. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).

### Configuration

Item | Default quota  
---|---  
Maximum number of `EdgeCacheService` resources per project | 20  
Maximum number of `EdgeCacheOrigin` resources per project | 30  
Maximum number of `EdgeCacheKeyset` resources per project | 10  
  
## System limits

The following limits apply to Media CDN.

### Configuration

Item | Limits | Notes  
---|---|---  
Maximum number of `RouteRules` resources per `EdgeCacheService` | 200 | Each `EdgeCacheService` can define up to 200 `RouteRules` resources.  
Maximum number of `PathMatchers` resources per `EdgeCacheService` | 50 | Each `EdgeCacheService` can define up to 50 `PathMatchers` resources.  
Maximum SSL certificates per service | 5 | Refer to the [per project quota](https://docs.cloud.google.com/load-balancing/docs/quotas#compute-engine-ssl-certificates) for SSL certificates.   
Maximum number of public keys per `EdgeCacheKeyset` | 3 | Multiple keys in a keyset enable key rotation. Remove unused keys over time.   
Maximum number of validation shared keys per `EdgeCacheKeyset` | 3 | Multiple keys in a keyset are designed to enable key rotation: you should remove older and unused keys over time.   
  
### HTTP headers, requests, and status codes

Item | Limits | Notes  
---|---|---  
**Maximum request header size, including request path** | 16 KiB | This limit cannot be increased.  Depending on the underlying protocol, the request connection is either closed without a response code being written, or the request is rejected with an HTTP `431 Request Header Fields Too Long` response.  These requests are logged with a `statusDetails` of `headers_too_long`, if logging is enabled.   
Maximum request body size | 16 KiB | This limit cannot be increased. Requests with a body over this limit are rejected with an HTTP `413 Content Too Large` status code.   
Maximum response header size  | Approximately 128 KiB |  Origin responses with headers that exceed this limit result in an HTTP `502 Bad Gateway` status code being sent to the client. These are logged with a `statusDetails` value of `backend_response_headers_too_long`, if logging is enabled.   
Maximum cacheable object size | 100 GiB |  This is the maximum size of objects at the origin that Media CDN can cache. Larger objects are treated as uncacheable.  This limit can be increased up to 1 TiB. If you need a higher limit, contact your Google support representative.   
Maximum uncacheable response size | 10239 MiB |  This is the maximum number of bytes in a response (including headers) that Media CDN proxies when an object is uncacheable. Uncacheable responses are truncated after they hit the limit.   
Lowercase conversion for headers | Always, for Media CDN | Media CDN follows HTTP/2 conventions for letter case of request and response headers.  Regardless of the protocol used, all headers are converted to lowercase.  For example, `Host` becomes `host`, and `Keep-Alive` becomes `keep-alive`.  The cases of header values aren't changed.   
  
### API request rate limits

If you need a higher rate limit for API requests, you can review the current use and request an increase.

Item | Limits  
---|---  
Invalidations per `EdgeCacheService` | 10 per minute  
All of the calls that aren't in the `networkservices` namespace per project | 1,200 calls per minute  
Read-only: `GetEdgeCache*`, `ListEdgeCache*` per project | 100 per minute  
Read/write: everything in the `networkservices` namespace not marked as read-only per project | 100 per minute  
  
We recommend that update requests, such as `create`, `patch`, and `delete`, are submitted one at a time. While the API queues multiple simultaneous requests, submitting these requests simultaneously can lead to significantly increased latency and longer processing times as the system processes each item serially.

### Client timeouts

Timeout | Maximum duration | Status code | Description  
---|---|---|---  
**Maximum request duration** | 5 minutes | HTTP `408 Request Timeout` | The maximum duration of a single request-response.  
**Header timeout** | 10 seconds | HTTP `408 Request Timeout` | How long the client has to send the full set of request headers.  
  
### Origin timeouts

  * `connectTimeout` and `maxAttemptsTimeout` limit how long Media CDN takes to find a usable response.

Both timeouts include the time that the origin takes to return headers and to determine whether to use a failover or redirect. `connectTimeout` applies independently for each origin attempt, while `maxAttemptsTimeout` includes the time required to connect across all origin attempts, including failovers and redirects. Following a redirect counts as an additional attempt to connect to the origin, and counts toward the `maxAttempts` set for the configured origin.

When Media CDN encounters a nonredirect response, such as from a redirect or failover origin, the `readTimeout` and `responseTimeout` values apply. Redirected origins use the `connectTimeout`, `readTimeout`, and `responseTimeout` values configured for the `EdgeCacheOrigin` that encountered the redirect.

  * `responseTimeout` and `readTimeout` control how long a streamed response can take. After Media CDN determines that it's going to use an upstream response, neither `connectTimeout` nor `maxAttemptsTimeout` matter. At this point, `readTimeout` and `responseTimeout` come into effect.




Media CDN makes at most four origin attempts across all origins, regardless of the `maxAttempts` set by each `EdgeCacheOrigin`. Media CDN uses the `maxAttemptsTimeout` value from the primary `EdgeCacheOrigin`. The per-attempt timeout values (`connectTimeout`, `readTimeout`, and `responseTimeout`) are configured for the `EdgeCacheOrigin` of each attempt.

The following table describes the timeout fields:

Field | Default | Description  
---|---|---  
**connectTimeout** | 5 seconds | The maximum amount of time Media CDN can take from starting the request to the origin until Media CDN determines whether the response is usable. Practically, `connectTimeout` covers the time starting with creating the request, then doing DNS lookups, then doing TLS handshakes, TCP/QUIC connection establishment, through getting the response headers that contain the HTTP status code. The timeout must be a value between 1 second and 15 seconds.  
**maxAttemptsTimeout** | 15 seconds | The maximum time across all connection attempts to the origin, including failover origins, before returning an error to the client. An HTTP `504` status code is returned if the timeout is reached before a response is returned. The timeout must be a value between 1 second and 30 seconds. This setting defines the _total_ duration for _all_ origin connection attempts, including failover origins, in order to cap the total time clients have to wait for content to start streaming. Only the first `maxAttemptsTimeout` value is used, where the _first_ is defined by the origin configured for the given route.  
**readTimeout** | 15 seconds | The maximum duration to wait between reads of a single HTTP response. The `readTimeout` is capped by the `responseTimeout`. All reads of the HTTP response must be completed by the deadline set by the `responseTimeout`. The timeout must be a value between 1 second and 30 seconds. If this timeout is reached before the response is complete, the response is truncated and logged.  
**responseTimeout** | 30 seconds | The maximum duration to allow for a response to complete. The timeout must be a value between 1 second and 120 seconds. The duration is measured from the time that the first body bytes are received. If this timeout is reached before the response is complete, the response is truncated and logged.  
  
## Manage quotas

Media CDN enforces quotas on resource usage for various reasons. For example, quotas protect the community of Google Cloud users by preventing unforeseen spikes in usage. Quotas also help users who are exploring Google Cloud with the [free tier](https://docs.cloud.google.com/free/docs/gcp-free-tier) to stay within their trial. 

All projects start with the same quotas, which you can change by requesting additional quota. Some quotas might increase automatically based on your use of a product.

### Permissions

To view quotas or request quota increases, Identity and Access Management (IAM) principals need one of the following roles. 

Task | Required role  
---|---  
Check quotas for a project | One of the following: 

  * Project [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Project [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * [Quota Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) (`roles/servicemanagement.quotaViewer`)

  
Modify quotas, request additional quota | One of the following: 

  * Project [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Project [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * [Quota Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) (`roles/servicemanagement.quotaAdmin`)
  * A custom role with the `serviceusage.quotas.update` permission

  
  
### Check your quota

### Console

  1. In the Google Cloud console, go to the **Quotas** page. 

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. To search for the quota that you want to update, use the **Filter table**. If you don't know the name of the quota, use the links on this page instead.



### gcloud

Using the Google Cloud CLI, run the following command to check your quotas. Replace `PROJECT_ID` with your own project ID.
    
    
        gcloud compute project-info describe --project PROJECT_ID

To check your used quota in a region, run the following command:
    
    
        gcloud compute regions describe example-region
        

### Errors when exceeding your quota

If you exceed a quota with a `gcloud` command, `gcloud` outputs a `quota exceeded` error message and returns with the exit code `1`.

If you exceed a quota with an API request, Google Cloud returns the following HTTP status code: `413 Request Entity Too Large`. 

### Request additional quota

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

### Resource availability

Each quota represents a maximum number for a particular type of resource that you can create, if that resource is available. It's important to note that quotas _don't_ guarantee resource availability. Even if you have available quota, you can't create a new resource if it is not available.

For example, you might have sufficient quota to create a new regional, external IP address in a given region. However, that is not possible if there are no available external IP addresses in that region. Zonal resource availability can also affect your ability to create a new resource.

Situations where resources are unavailable in an entire region are rare. However, resources within a zone can be depleted from time to time, typically without impact to the service level agreement (SLA) for the type of resource. For more information, review the relevant SLA for the resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
