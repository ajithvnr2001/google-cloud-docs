---
url: https://docs.cloud.google.com/media-cdn/docs/configure-request-logging/
title: Configure request logging \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:48.116539+00:00
---

# Configure request logging  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/configure-request-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Configure request logging Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure [request logging](https://docs.cloud.google.com/media-cdn/docs/logging) for Media CDN.

## Enable logs

Logging is disabled by default to minimize the data stored. Logs are routed, filtered, and stored in [Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/overview).

  * Enable logging for a specific Media CDN service:
        
        gcloud edge-cache services update SERVICE_NAME \
           --enable-logging \
           --logging-sample-rate=1.0
        

  * Disable logging:
        
        gcloud edge-cache services update SERVICE_NAME \
           --no-enable-logging
        

  * Get the current state of logging on a service:
        
        gcloud edge-cache services describe SERVICE_NAME
        

The output is similar to the following:
        
        ...
        logConfig:
         enable: true
         sampleRate: 1.0
        ...
        




## Set the log sampling rate

For large volumes of requests, rather than capture a log for every request, you might prefer to sample logs and rely on metrics for proactive monitoring and investigation.

To only ingest and store logs for 10% of your requests, set `logConfig.sampleRate` to `0.1`:
    
    
    gcloud edge-cache services update SERVICE_NAME \
        --enable-logging \
        --logging-sample-rate=0.1
    

Logging must be enabled to change the sampling rate.

The sampling rate, unless otherwise specified, defaults to 0 (0%), which logs every request for the configured service.

## Query logs

To query logs, you can use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) in the Google Cloud console, or you can use the Google Cloud CLI.

To view logs in the Google Cloud console, filter for the Media CDN resource type and (optionally) by project and service name.

The following [logging query](https://docs.cloud.google.com/logging/docs/view/query-library) shows the logs for all of your Media CDN services:
    
    
    resource.type="edgecache.googleapis.com/EdgeCacheRouteRule"
    

To filter for logs associated with a specific `EdgeCacheService` resource and project, extend this query:
    
    
    resource.type="edgecache.googleapis.com/EdgeCacheRouteRule"
    resource.labels.resource_container="projects/12345678"
    resource.labels.service_name="MY_PROJECT"
    

To match on partial names or use regular expressions, see the [Logging query language comparisons](https://docs.cloud.google.com/logging/docs/view/logging-query-language#comparisons).

### Example: Identify cache misses

A request for an object might be a cache miss but might cause a cache fill for the following reasons:

  * A time to live (TTL) that is too short
  * An overly specific cache key
  * Too few requests to stay cached



To identify cache misses, you can filter for logs in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

The following log query shows requests that are cacheable (looked up), but that require a fill from the origin:
    
    
    resource.type="edgecache.googleapis.com/EdgeCacheRouteRule"
    resource.labels.resource_container="projects/12345678"
    resource.labels.service_name="MY_PROJECT"
    jsonPayload.cacheStatus="miss"
    

If you need to filter by a specific URL, filter on the `httpRequest.requestUrl` field:
    
    
    httpRequest.requestUrl = "URL"
    

To filter on part of the URL, such as the path component, use the [`has` operator](https://docs.cloud.google.com/logging/docs/view/logging-query-language#syntax_summary):
    
    
    # `:` is the `has` comparison operator
    
    httpRequest.requestUrl: "/videos/1381381_1080.mp4"
    # You can use `OR` or `AND` to filter on multiple values
    
    httpRequest.requestUrl: ("https://media-test.example.com/" OR "https://canary.example.net")
    

To learn more about Logging's comprehensive syntax for matching and filtering, see [Write advanced queries using the Logging query language](https://docs.cloud.google.com/logging/docs/view/building-queries#queries-by-expression).

## Filter stored logs

To filter logs before storing them—for example, only capturing pertinent fields to reduce the total log volume that you need to store and query—you can configure [exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions), which allow you to define a query (filter) that includes or excludes fields prior to storage.

You can also set up multiple filters—for example, capturing all cache miss requests or all requests for a specific hostname, and only taking a sample of all logs.

## Route logs

Media CDN integrates directly with Cloud Logging, which helps you aggregate and route your logs in the following ways:

  * To storage destinations, such as Cloud Storage and BigQuery

  * To Pub/Sub topics, to which third-party destinations can subscribe to access the logs




For an overview of how logs are routed from Logging, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).

## What's next

  * To understand more about how to set up logs-based metrics to define your own metrics values based on logged requests, see the [Log-based metrics overview](https://docs.cloud.google.com/logging/docs/logs-based-metrics).
  * To learn more about the pricing for Logging, see [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing).
  * To read about how audit logging works and how to enable and configure audit logs for admin activity, see the [Cloud Audit Logs documentation](https://docs.cloud.google.com/logging/docs/audit).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
