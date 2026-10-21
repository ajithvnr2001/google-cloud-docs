---
url: https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/RequestLog/
title: RequestLog \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:26:49.633543+00:00
---

# RequestLog  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/RequestLog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)



Send feedback 

#  RequestLog Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SourceReference
    * JSON representation



Complete log information about a single HTTP request to an App Engine application.

JSON representation  
---  
      
    
    {
      "appId": string,
      "moduleId": string,
      "versionId": string,
      "requestId": string,
      "ip": string,
      "startTime": string,
      "endTime": string,
      "latency": string,
      "megaCycles": string,
      "method": string,
      "resource": string,
      "httpVersion": string,
      "status": number,
      "responseSize": string,
      "referrer": string,
      "userAgent": string,
      "nickname": string,
      "urlMapEntry": string,
      "host": string,
      "cost": number,
      "taskQueueName": string,
      "taskName": string,
      "wasLoadingRequest": boolean,
      "pendingTime": string,
      "instanceIndex": number,
      "finished": boolean,
      "first": boolean,
      "instanceId": string,
      "line": [
        {
          object([LogLine](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/LogLine))
        }
      ],
      "appEngineRelease": string,
      "traceId": string,
      "sourceReference": [
        {
          object([SourceReference](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/RequestLog#SourceReference))
        }
      ],
    }  
  
Field name | Type | Description  
---|---|---  
`appId` | `string` | Application that handled this request.  
`moduleId` | `string` | Module of the application that handled this request.  
`versionId` | `string` | Version of the application that handled this request.  
`requestId` | `string` | Globally unique identifier for a request, which is based on the request start time. Request IDs for requests which started later will compare greater as strings than those for requests which started earlier.  
`ip` | `string` | Origin IP address.  
`startTime` | `string` | Time when the request started.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` | `string` | Time when the request finished.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.  
`latency` | `string` | Latency of the request.A duration in seconds with up to nine fractional digits, terminated by '`s`'. Example: `"3.5s"`.  
`megaCycles` | `string` | Number of CPU megacycles used to process request.  
`method` | `string` | Request method. Example: `"GET"`, `"HEAD"`, `"PUT"`, `"POST"`, `"DELETE"`.  
`resource` | `string` | Contains the path and query portion of the URL that was requested. For example, if the URL was "http://example.com/app?name=val", the resource would be "/app?name=val". The fragment identifier, which is identified by the `#` character, is not included.  
`httpVersion` | `string` | HTTP version of request. Example: `"HTTP/1.1"`.  
`status` | `number` | HTTP response status code. Example: 200, 404.  
`responseSize` | `string` | Size in bytes sent back to client by request.  
`referrer` | `string` | Referrer URL of request.  
`userAgent` | `string` | User agent that made the request.  
`nickname` | `string` | The logged-in user who made the request.Most likely, this is the part of the user's email before the `@` sign. The field value is the same for different requests from the same user, but different users can have similar names. This information is also available to the application via the App Engine Users API.This field will be populated starting with App Engine 1.9.21.  
`urlMapEntry` | `string` | File or class that handled the request.  
`host` | `string` | Internet host and port number of the resource being requested.  
`cost` | `number` | An indication of the relative cost of serving this request.  
`taskQueueName` | `string` | Queue name of the request, in the case of an offline request.  
`taskName` | `string` | Task name of the request, in the case of an offline request.  
`wasLoadingRequest` | `boolean` | Whether this was a loading request for the instance.  
`pendingTime` | `string` | Time this request spent in the pending request queue.A duration in seconds with up to nine fractional digits, terminated by '`s`'. Example: `"3.5s"`.  
`instanceIndex` | `number` | If the instance processing this request belongs to a manually scaled module, then this is the 0-based index of the instance. Otherwise, this value is -1.  
`finished` | `boolean` | Whether this request is finished or active.  
`first` | `boolean` | Whether this is the first `RequestLog` entry for this request. If an active request has several `RequestLog` entries written to Stackdriver Logging, then this field will be set for one of them.  
`instanceId` | `string` | An identifier for the instance that handled the request.  
`line[]` | `object(`[LogLine](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/LogLine)`)` | A list of log lines emitted by the application while serving this request.  
`appEngineRelease` | `string` | App Engine release version.  
`traceId` | `string` | Stackdriver Trace identifier for this request.  
`sourceReference[]` | `object(`[SourceReference](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/RequestLog#SourceReference)`)` | Source code for the application that handled this request. There can be more than one source reference per deployed application if source code is distributed among multiple repositories.  
  
## SourceReference

A reference to a particular snapshot of the source tree used to build and deploy an application.

JSON representation  
---  
      
    
    {
      "repository": string,
      "revisionId": string,
    }  
  
Field name | Type | Description  
---|---|---  
`repository` | `string` | Optional. A URI string identifying the repository. Example: "https://github.com/GoogleCloudPlatform/kubernetes.git"  
`revisionId` | `string` | The canonical and persistent identifier of the deployed revision. Example (git): "0035781c50ec7aa23385dc841529ce8a4b70db1b"  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
