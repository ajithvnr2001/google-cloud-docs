---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-command-reference/
title: Metrics API examples \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:04.677064+00:00
---

# Metrics API examples  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-command-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Metrics API examples Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document provides examples of using the Apigee metrics API based on specific criteria. This is not a comprehensive reference.

For more information, see:

  * [Metrics API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.stats/get)
  * [Analytics metrics, dimensions, and filters reference](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference)
  * [Getting started using the Apigee API](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started)



**Note** : If you are a Pay-as-you-go customer, you must enable the Apigee API Analytics add-on in your eligible environments to use this API. If the Apigee API Analytics add-on is not enabled, you will see an error that you are unable to access this API. For more information, see [ Manage the Apigee API Analytics add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-analytics-add-on).

In the following examples: 

  * `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in the examples, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of the environment variables used, see [ Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).
  * [`apiproxy` ](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#apiproxy) is the internal name (not the display name) of the API proxy.
  * [`developer` ](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#developer) is the unique Apigee-generated developer ID of the form `org_name@@@unique_id`. 
  * [`developer_app` ](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#developer_app) is the Apigee-registered developer app making API calls.
  * [`api_product` ](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#api_product) is the name of the API product containing the API proxies being called. .



## API analytics commands

### Request counts by API proxy

Requests by API proxy
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/$ENV/stats/apiproxy?select=sum(message_count)&timeRange=9/24/2019+00:00~10/25/2019+00:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"
    

### Response time by API proxy

Avg. Total Response Time by API proxy
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/$ENV/stats/apiproxy?select=avg(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"
    

Max Total Response Time by API proxy
    
    
    curl https://apigee.googleapis.com/v1/organizations/$ORG/environments/$ENV/stats/apiproxy?select=max(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Total Response Time by API proxy
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/$ENV/stats/apiproxy?select=min(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg. Target Response Time by API proxy
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/$ENV/stats/apiproxy?select=avg(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Target Response Time by API proxy
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/$ENV/stats/apiproxy?select=max(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Target Response Time by API proxy
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/$ENV/stats/apiproxy?select=min(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Errors by API proxy

Errors by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=sum(is_error)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Request/response size by API

Max Request Size by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=max(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Min Request Size by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=min(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Avg Request Size by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=avg(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Max Response Size by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=max(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Min Response Size by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=min(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Avg Response Size by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=avg(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

### Request/response latency by API

Avg. Response Processing Latency by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=avg(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Max Response Processing Latency by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=max(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Min Response Processing Latency by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=min(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Avg. Request Processing Latency by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=avg(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Max Request Processing Latency by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=max(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Min Request Processing Latency by API
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/apiproxy?select=min(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

## Developer analytics commands

### App/User/Request counts by developer

App count by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=app_count&timeRange=9/24/2014%2000:00~10/25/2014%2000:00&timeUnit=day \
    

End User count by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/<**$ORG** /environments/**$ENV** /stats/developer?select=user_count&timeRange=9/24/2014%2000:00~10/25/2014%2000:00&timeUnit=day \
    

Requests by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=sum(message_count)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

### Response time by developer

Avg. Total Response Time by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=avg(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Max Total Response Time by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=max(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Min Total Response Time by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=min(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Avg. Target Response Time by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=avg(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Max Target Response Time by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=max(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Min Target Response Time by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=min(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

### Errors by developer

Errors by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=sum(is_error)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

### Request/response size by developer

Max Request Size by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=max(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Min Request Size by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=min(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Avg Request Size by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=avg(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Max Response Size by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=max(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Min Response Size by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=min(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Avg Response Size by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=avg(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

### Request/response latency by developer

Avg. Response Processing Latency by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=avg(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Max Response Processing Latency by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=max(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Min Response Processing Latency by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=min(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Avg. Request Processing Latency by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=avg(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Min Request Processing Latency by Developers
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer?select=min(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

## App analytics commands

### User/Request counts by app

User count by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=user_count&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Requests by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=sum(message_count)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

### Response time by app

Avg. Total Response Time by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=avg(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Max Total Response Time by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=max(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Min Total Response Time by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=min(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Avg. Target Response Time by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=avg(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Max Target Response Time by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=max(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

Min Target Response Time by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=min(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
    

### Errors by app

Errors by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=sum(is_error)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Request/response size by app

Max Request Size by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=max(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Request Size by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=min(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg Request Size by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=avg(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Response Size by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=max(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Response Size by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=min(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg Response Size by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=avg(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Request/response latency by app

Avg. Response Processing Latency by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=avg(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Response Processing Latency by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=max(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Response Processing Latency by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=min(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg. Request Processing Latency by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=avg(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Request Processing Latency by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=max(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Request Processing Latency by Apps
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/developer_app?select=min(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

## API product analytics commands

### App/Developer/Request counts by API product

App count by API Products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=app_count&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Developer count by API Products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=developer_count&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Requests by Products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=sum(message_count)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Response time by API product

Avg. Total Response Time API products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=avg(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Total Response Time API products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=max(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Total Response Time API products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=min(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg. Target Response Time API products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=avg(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Target Response Time API products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=max(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Target Response Time API products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=min(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Errors by API product

Errors by API Products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=sum(is_error)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Request/response size by API product

Max Request Size by API Products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=max(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Request Size by API Products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=min(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg Request Size by API Products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=avg(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Response Size by API Products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=max(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

MIn Response Size by API Products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=min(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg Response Size by API Products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=avg(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Request/response latency by API product

Avg. Response Processing Latency by API products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=avg(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Response Processing Latency by API products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=max(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Response Processing Latency by API products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=min(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg. Request Processing Latency by API products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=avg(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Request Processing Latency by API products
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/api_product?select=min(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

## API resource analytics commands 

### Request counts by API resource

Requests by API Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=sum(message_count)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Response time by API resource

Avg. Total Response Time by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=avg(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Total Response Time by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=max(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Total Response Time by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=min(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg. Target Response Time by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=avg(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Target Response Time by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=max(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Target Response Time by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=min(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Errors by API resource

Errors by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=sum(is_error)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Request/response size by API resource

Max Request Size by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=max(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Request Size by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=min(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg Request Size by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=avg(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Response Size by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=max(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Response Size by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=min(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg Response Size by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=avg(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Request/response latency by API resource

Avg. Response Processing Latency by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=avg(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Response Processing Latency by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=max(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Response Processing Latency by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=min(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg. Request Processing Latency by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=avg(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Request Processing Latency by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=max(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Request Processing Latency by API-Resource
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/request_path?select=min(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

## API program-wide analytics commands

### Request counts

Requests over Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats?select=sum(message_count)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Response time

Average Total Response Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=avg(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Total Response Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=max(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Total Response Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=min(total_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Average Target Response Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=avg(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Target Response Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=max(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Target Response Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=min(target_response_time)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Errors

Errors over Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=sum(is_error)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Request/response size

Max Request Size over Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=min(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Request Size over Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=min(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg Request Size over Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=avg(request_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Response Size over Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=min(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Response Size over Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=min(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Avg Response Size over Time
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=avg(response_size)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

### Request/response latency

Avg. Response Processing Latency
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=avg(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Response Processing Latency
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=max(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Response Processing Latency
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=min(response_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Average Request Processing Latency
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=avg(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Max Request Processing Latency
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=max(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Min Request Processing Latency
    
    
    curl https://apigee.googleapis.com/v1/organizations/**$ORG** /environments/**$ENV** /stats/?select=min(request_processing_latency)&timeRange=9/24/2018%2000:00~10/25/2018%2000:00&timeUnit=day \
      -H "Authorization: Bearer $TOKEN"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
