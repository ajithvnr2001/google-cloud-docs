---
url: https://docs.cloud.google.com/cdn/docs/logging/
title: Logs and metrics for caching \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:52.370072+00:00
---

# Logs and metrics for caching  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Logs and metrics for caching Stay organized with collections  Save and categorize content based on your preferences. 

Each Cloud CDN request is logged in [Cloud Logging](https://docs.cloud.google.com/logging/docs/write-query-log-entries-gcloud). For information about enabling and disabling logging, see the [External Application Load Balancer and Cloud CDN logging and monitoring overview](https://docs.cloud.google.com/cdn/docs/cdn-logging-monitoring).

Logs for Cloud CDN are associated with the external Application Load Balancer that your Cloud CDN backends are attached to. Cloud CDN logs are indexed first by [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) and then by [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts).

To view Cloud CDN logs, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Logs Explorer** page. 

[Go to Logs Explorer](https://console.cloud.google.com/logs?service=network.googleapis.com)

  2. In the **Resource** menu, select **Cloud HTTP Load Balancer**.
  3. View logs as follows: 
     * **View all logs:** select the **Resource** menu, and then select **All forwarding rules**.
     * **View the logs for a forwarding rule:** select the forwarding rule name from the list of forwarding rules.
     * **View the logs for a URL map used by a forwarding rule:** select a forwarding rule, and then select a URL map.



## Request served from the backend

To confirm that a request is served from a Cloud CDN-enabled backend, there are three main fields to look for, as follows:

  * `httpRequest`: When a request is served from a backend, you can see that the cache is filled and you can confirm the request URL. 
    * `cacheFillBytes:` NUMBER_OF_BYTES
    * `cacheLookup: True`
    * `requestURL`: URL
  * `jsonPayload`: From the `statusDetails` field, you can confirm that the response was served by the backend. 
    * `statusDetails: "response_sent_by_backend"`



## Request served from cache

The following log entry shows a cache hit.
    
    
     {
        insertId: "1oek5rg3l3fxj7"
        jsonPayload: {
            @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
            cacheId: "SFO-fbae48ad"
            statusDetails: "response_from_cache"
        }
        httpRequest: {
            requestMethod: "GET"
            requestUrl: "http://LOAD_BALANCER_IP_ADDRESS/static/us/three-cats.jpg"
            requestSize: "577"
            status: 304
            responseSize: "157"
            userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
            remoteIp: "CLIENT_IP_ADDRESS"
            cacheHit: truecacheLookup: true
        }
        resource: {
            type: "http_load_balancer"
            labels: {
                zone: "global"
                url_map_name: "URL_MAP_NAME"
                forwarding_rule_name: "FORWARDING_RULE_NAME"
                target_proxy_name: "TARGET_PROXY_NAME"
                backend_service_name: ""
                project_id: "PROJECT_ID"
            }
        }
        timestamp: "2020-06-08T23:41:30.078651Z"
        severity: "INFO"
        logName: "projects/PROJECT_ID/logs/requests"
        trace: "projects/PROJECT_ID/traces/241d69833e64b3bf83fabac8c873d992"
        receiveTimestamp: "2020-06-08T23:41:30.588272510Z"
        spanId: "7b6537d3672e08e1"
    }
    

## What is logged

In addition to general information contained in most logs, such as severity, project ID, project number, and timestamp, the [external Application Load Balancer and Cloud CDN logs](https://docs.cloud.google.com/cdn/docs/cdn-logging-monitoring#logging) contain the following:

  * The [HttpRequest](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest) log field, which captures the HTTP status code, bytes returned, and whether a cache lookup or cache fill was performed.

  * The `jsonPayload.cacheId` field, which indicates the location and cache instance that the cache response was served from. For example, a cache response served from a cache in Amsterdam would have a cacheId value of `AMS-85e2bd4b`, where `AMS` is the [IATA code](https://en.wikipedia.org/wiki/IATA_airport_code), and `85e2bd4b` is an opaque identifier of the cache instance (because some Cloud CDN locations have multiple discrete caches).

  * The [`statusDetails` and `cacheDetail`](https://docs.cloud.google.com/cdn/docs/cdn-logging-monitoring#what_is_logged) fields of the `jsonPayload`.




You can filter on the following fields to determine the cache hit, miss, or revalidation status of a request served by Cloud CDN:

  * **Cache Hit**

`jsonPayload.statusDetails=("response_from_cache" OR "byte_range_caching")`

or

`httpRequest.cacheHit=true`  
`httpRequest.cacheValidatedWithOriginServer!=true`

  * **Cache Hit Validated With Origin Server**

`jsonPayload.statusDetails="response_from_cache_validated"`

or

`httpRequest.cacheHit=true`  
`httpRequest.cacheValidatedWithOriginServer=true`

  * **Cache Miss**

`jsonPayload.statusDetails="response_sent_by_backend"`

or

`httpRequest.cacheHit!=true`  
`httpRequest.cacheLookup=true`




Alternatively, you can observe the cache status from the client side by configuring a [custom response header](https://docs.cloud.google.com/cdn/docs/caching#custom-headers) with `cdn_cache_status`.

Log fields of type _boolean_ typically only appear if they have a value of `true`. If a boolean field has a value of `false`, that field is omitted from the log.

[UTF-8](https://wikipedia.org/wiki/UTF-8) encoding is enforced for these fields. Characters that are not UTF-8 characters are replaced with question marks.

When Cloud CDN serves a client request by initiating validation requests or byte range requests, it omits the `serverIp` field from the Cloud Logging log entry for the client request. This is because Cloud CDN can send requests to multiple server IP addresses in reaction to a single client request.

Each request initiated by Cloud CDN creates a Cloud Logging log entry. The resulting log entry contains a `parentInsertId` field inside the `jsonPayload`. You can use this field to identify the `insertId` of the log entry for the single client request that prompted Cloud CDN to initiate the validation request or byte range request. Furthermore, the log entry identifies Cloud CDN as the user agent.

## Monitoring for Cloud CDN

Cloud CDN exports monitoring data to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). Monitoring is used to monitor the health of a Cloud CDN deployment.

Cloud Monitoring provides [predefined dashboards](https://docs.cloud.google.com/cdn/docs/logging#predefined-cdn-dashboards) that are enabled by default for a quick insight into system health and performance. Monitoring also offers a set of [custom dashboards](https://docs.cloud.google.com/cdn/docs/logging#custom-cdn-dashboards). The definitions of these custom dashboards are available on GitHub in the [monitoring-dashboard-samples repository](https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples) as JSON files. In the `dashboards/networking` directory, there is a Cloud CDN-specific custom dashboard called `cloud-cdn-monitoring.json`. Upload this custom dashboard to Monitoring by following the instructions in [Installing sample dashboards](https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates).

**Note:** The dashboard doesn't filter on any specific backend; all load-balancing traffic for all backends is included. To filter on a specific backend, you need to add `backend_target_name="example-backend"` to each chart's PromQL query. Additionally, to filter on only backends that have Cloud CDN enabled, include `cache_result!="DISABLED"`.**Note:** To filter your monitoring data for a specific URL map or path rule, add the following filters to each chart's Monitoring Query Language (MQL) query:

  * `filter (resource.url_map_name = 'URL_MAP_NAME')`

  * `filter (resource.matched_url_path_rule = 'PATH_RULE_NAME')`




### Predefined dashboards

Cloud Monitoring offers predefined dashboards for Cloud CDN. These dashboards display key metrics that enable you to monitor traffic distribution and cache effectiveness without manual configuration.

#### View predefined dashboards

Perform the following steps to access the predefined dashboards:

  1. In the Google Cloud console, go to the **Cloud CDN** page.

[Go to Cloud CDN](https://console.cloud.google.com/net-services/cdn)

  2. Click the name of the origin that you want to view the dashboards for.

  3. On the **Origin details** page, click **Monitoring**.

The predefined dashboards appear by default.




#### Metrics on the dashboards

The predefined dashboards provide the following key metrics about your CDN origins:

  * **Client traffic distribution**

A dynamic geographical map displaying the source of client requests. This map provides a visual, global overview of where traffic is originating from. You can adjust the time range filter to analyze traffic distribution patterns over specific periods.

  * **Core metrics**

The following table describes the core metrics displayed on the dashboard.

Metrics | Description  
---|---  
Total requests | The aggregate count of all HTTP/HTTPS requests processed by Cloud CDN, served either from cache or from the origin backend service. The chart shows the request count over time.  
Cache egress | The total volume of data, in bytes, served from the Cloud CDN edge caches. The bar chart shows the egress volume over time.   
Total error ratio | The percentage of all requests that resulted in an error status code `4 _xx_` or `5 _xx_`. This metric is a primary indicator of overall service health.  
4 _xx_ error ratio | The percentage of requests that resulted in a client-side status code. These are 4 _xx_ codes, such as `404 Not Found` or `403 Forbidden`. Such errors indicate issues with the requested content or client permissions.   
5 _xx_ error ratio | The percentage of requests that resulted in a server-side status code. These are 5 _xx_ codes, such as `502 Bad Gateway` or `503 Service Unavailable`. Such errors indicate issues with the backend origin service or the load balancer configuration.  
Cache hit ratio | The ratio, as a percentage, of requests served directly from the Cloud CDN cache versus the total number of requests.  
Total cache fill | The total volume of data, in bytes, retrieved from the origin backend and stored in the Cloud CDN cache.  



### Custom dashboards

Monitoring lets you [create custom dashboards](https://docs.cloud.google.com/cdn/docs/cdn-logging-monitoring#defining_custom_dashboards). Dashboards can use any of the [monitoring metrics](https://docs.cloud.google.com/cdn/docs/cdn-logging-monitoring#monitoring) for external Application Load Balancers. Following are some example PromQL snippets that you can paste into custom Monitoring dashboards.

**Request bytes count broken out by cache result**

This query focuses on backends that have Cloud CDN enabled, which is done by including `cache_result!="DISABLED"`.
    
    
    sum by (cache_result) (
     rate({"loadbalancing.googleapis.com/https/response_bytes_count", monitored_resource="https_lb_rule", cache_result!="DISABLED"}[1m])
    )
    

**Client roundtrip TCP latency at 95% for a specific backend target**

This query includes `backend_target_name="example-backend"`, which narrows down traffic to the backend `example-backend`. A backend can be a Cloud Storage bucket, a Compute Engine VM group, or an external backend.
    
    
    histogram_quantile(
     0.95,
     sum by (proxy_continent, le) (
       rate({"loadbalancing.googleapis.com/https/frontend_tcp_rtt_bucket",
         monitored_resource="https_lb_rule",
         backend_target_name="example-backend"
       }[1m])
     )
    )
    

**Request count broken out by response code class for Cloud CDN-enabled backends**

This query breaks out traffic by response code class (2xx, 3xx, 4xx, 5xx) to help separate client successes, client errors, and server errors.
    
    
    sum by (response_code_class) (
     count_over_time(
      {"loadbalancing.googleapis.com/https/request_count",
         monitored_resource="https_lb_rule",
         cache_result!="DISABLED"
       }[1h]
     )
    )
    

**Request count broken out by country of origin**

This query shows traffic broken out by country of origin, which is determined by using client IP addresses.
    
    
    sum by (client_country) (
     rate({"loadbalancing.googleapis.com/https/request_count", monitored_resource="https_lb_rule"}[1m])
    )
    

## What's next

  * To learn more about logging, including how to export logs to BigQuery, Pub/Sub, or Cloud Storage, and how to configure logs-based metrics for monitoring and alerting, see the [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs).

  * To learn about the fields that are included in the `httpRequest` log entry, see [`HttpRequest`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#httprequest).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
