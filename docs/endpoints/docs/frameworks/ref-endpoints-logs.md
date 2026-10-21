---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs/
title: Endpoints logs \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:15.462354+00:00
---

# Endpoints logs  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  Endpoints logs Stay organized with collections  Save and categorize content based on your preferences. 

When users make requests to your API, [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/frameworks/glossary#extensible_service_proxy) uses Cloud Logging to log information about the requests and responses. This page describes the information logged.

To locate Cloud Endpoints logs on the **Logs Explorer** page:

  1. In the Google Cloud console, go to the **Operations** > **Logging** page:

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

  2. Select **Produced API,` SERVICE_NAME`**, where `SERVICE_NAME` is the name of the Endpoints service. **Note:** You can select **Produced API** from the resource menu only if a recent log message contains the **API** resource type. 

  3. Click the log you want to investigate. The log contains a structured JSON message such as the following:
         
         {
           insertId: "…"
           jsonPayload: {…}
           resource: {
             type: "api"
             labels: {…}
           }
           timestamp: "2017-05-08T15:00:02.804424422Z"
           severity: "INFO"
           logName: "…"
         }
         




The `jsonPayload` object contains all the information reported by ESP. The following table describes its fields:

Field | Description  
---|---  
`url` | URL path of the request.  
`producer_project_id` | Google Cloud project ID that owns the API.  
`api_name` | Name of the API invoked.  
`api_version` | Version of the named API invoked.  
`api_method` | Method of the named API invoked.  
`api_key` | API key used by the calling consumer, if present.  
`http_method` | HTTP method of the request such as `GET` and `POST`.  
`request_size_in_bytes` | Size of request body in bytes.  
`http_response_code` | HTTP status code of the response such as `200`, `404`, and `500`.  
`response_size_in_bytes` | Size of the response body in bytes.  
`request_latency_in_ms` | Time it took to respond to the request in milliseconds, including the time taken by ESP and its backend. Not present for streaming methods.  
`timestamp` | Timestamp for when the request came in.  
`location` | Google Cloud zone that serviced the request.  
`log_message` | Short message about the called method and its status if it is rejected. No API information fields are logged for rejected calls.  
`error_cause` | Error message if the response was an error.  
`labels` | The `labels` section contains information that identifies that source of the log, such as the Google Cloud project ID, the Endpoints service name, the API version number, and the method name.  
  
## What's next

  * [Monitoring your API](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
