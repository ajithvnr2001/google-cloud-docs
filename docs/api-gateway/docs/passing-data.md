---
url: https://docs.cloud.google.com/api-gateway/docs/passing-data/
title: Pass data to and from the backend service \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:29.675754+00:00
---

# Pass data to and from the backend service  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/passing-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Pass data to and from the backend service

When an API client makes a request to your API deployed on API Gateway, the client can pass any or all of the following information as part of the request:

  * Request headers
  * Query params
  * Form data
  * XML or JSON payloads
  * Request paths



In building its response to the API request, the backend service can return data to the API client, including:

  * Response headers
  * XML or JSON payloads



This document describes how this data is passed to and from the backend service.

## How is request data passed to the backend service?

All data in the request from the API client is passed unchanged to the backend service. It is then up to the backend service to parse the request data as part of handling the request.

## How is response data returned to the API client?

All data received in the response from the backend service is passed unchanged to the API client. It is then up to the API client to process any returned data in the response.

## How is the request URL passed to the backend service?

The URL used to make a request to the backend service is controlled by the [`x-google-backend`](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-extensions#x-google-backend) extension. This section describes the options for configuring the backend service URL.

### Set the backend service address and path in the OpenAPI spec

In the OpenAPI spec that you use to create an API config, you use the `x-google-backend` extension to specify the URL of the backend service. For example, you specify the backend service in the form:

Backend | x-google-backend  
---|---  
Cloud Run functions | 
    
    
    x-google-backend:
      address: https://GCP_REGION-PROJECT_ID.cloudfunctions.net/hello  
  
Cloud Run | One of the following: 

  * x-google-backend:
          address: APP_URL

  * x-google-backend:
          address: DETERMINISTIC_URL


  
App Engine standard environment | 
    
    
    x-google-backend:
      address: https://PROJECT_ID.appspot.com  
  
In these examples:

  * APP_URL specifies the actual URL of your Cloud Run service (the full path of the called API), also referred to as the [non-deterministic URL](https://docs.cloud.google.com/run/docs/triggering/https-request#non_deterministic). For example: `https://hello-abc1def2gh-uc.a.run.app`.
  * DETERMINISTIC_URL is the [deterministic URL](https://docs.cloud.google.com/run/docs/triggering/https-request#deterministic) for your Cloud Run service backend.

**Note** : If you plan to use the [deterministic URL](https://docs.cloud.google.com/run/docs/triggering/https-request#deterministic) to version your Cloud Run service backend, you must specify one of the following: 

  * Open API 2.0: [`jwt_audience`](https://docs.cloud.google.com/api-gateway/docs/oasv2-extensions#jwt_audience_disable_auth) field under `address` in the `x-google-backend` section
  * Open API 3.0: [`jwtAudience`](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions#backend_object) field under `address` in the `x-google-api-management` section

The value of the `jwt_audience` or `jwtAudience` field should be the Cloud Run service hostname. For example, for OpenAPI 2.0: 
    
    
    ...
      x-google-backend:
          address: https://VERSION_TAG---SERVICE_HOSTNAME/PATH
          jwt_audience: https://SERVICE_HOSTNAME
    ...

If the `jwt_audience` or `jwtAudience` field is not present, the field defaults to the value of the `address` field for the JWT audience claim. This can result in an unexpected JWT audience claim for Cloud Run if the revision tag URL is used for `address` and no `jwt_audience` or `jwtAudience` is specified.

In addition, the `path` parameter in the OpenAPI spec specifies the endpoint, or _resource_ , supported by your API. You can specify an absolute path or one that uses [path parameters](https://swagger.io/docs/specification/2-0/describing-parameters/#path-parameters):

Path | Path with parameters  
---|---  
      
    
    paths:
      /hello:

| 
    
    
    paths:
      /hello/{name}:  
  
### Generate the backend service URL from an API request

As API Gateway handles a request from the API client, it takes the request URL sent by the API client and translates it into the URL used to make the request to the backend service. Exactly how this translation occurs depends on which _path translation strategy_ you are using.

The `path_translation` option to the `x-google-backend` extension supports two path translation strategies:

  * `APPEND_PATH_TO_ADDRESS`: The backend service URL is generated by appending the resource path from the client request to the `address` URL of the `x-google-backend` extension.

Most backend services use `APPEND_PATH_TO_ADDRESS` because it means the backend receives the same resource path as specified by the API client.

  * `CONSTANT_ADDRESS`: The backend service URL is constant, as defined by the `address` URL of the `x-google-backend` extension. If the client request contains a resource path, the resource path is added to the backend service URL by using query parameters.

This method is typically used by [Cloud Run functions](https://docs.cloud.google.com/functions/docs).




For example:

  * `APPEND_PATH_TO_ADDRESS`
    * `address`: `https://PROJECT_ID.appspot.com`
    * Without OpenAPI path parameters: 
      * OpenAPI path: `/hello`
      * API client request resource path: `/hello`
      * Backend service request URL: `https://PROJECT_ID.appspot.com/hello`
    * With OpenAPI path parameters: 
      * OpenAPI path: `/hello/{name}`
      * API client request resource path: `/hello/Dave`
      * Backend service request URL: `https://PROJECT_ID.appspot.com/hello/Dave`
  * `CONSTANT_ADDRESS`
    * `address`: `https://GCP_REGION-PROJECT_ID.cloudfunctions.net/hello`
    * Without OpenAPI path parameters 
      * OpenAPI path: `/hello`
      * API client request resource path: `/hello`
      * Backend service request URL: `https://GCP_REGION-PROJECT_ID.cloudfunctions.net/hello`
    * With OpenAPI path parameters 
      * OpenAPI path: `/hello/{name}`
      * API client request resource path: `/hello/Dave`
      * Backend service request URL: `https://GCP_REGION-PROJECT_ID.cloudfunctions.net/hello?name=Dave`



### Set `path_translation`

Set `path_translation` as part of setting `x-google-backend`:
    
    
    x-google-backend:
      address: https://GCP_REGION-PROJECT_ID.cloudfunctions.net/hello
      path_translation: [ APPEND_PATH_TO_ADDRESS | CONSTANT_ADDRESS ]`

The default value of `path_translation` depends on where you set `x-google-backend` in your OpenAPI spec:

  * When `x-google-backend` is used at the top level of the OpenAPI specification, `path_translation` defaults to `APPEND_PATH_TO_ADDRESS`.

  * When `x-google-backend` is used at the operation level of the OpenAPI specification, `path_translation` defaults to `CONSTANT_ADDRESS`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
