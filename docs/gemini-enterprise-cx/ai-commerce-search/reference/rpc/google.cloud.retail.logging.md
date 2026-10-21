---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging
title: Package google.cloud.retail.logging \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:46.483560+00:00
---

# Package google.cloud.retail.logging  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Package google.cloud.retail.logging Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[ErrorContext](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging#google.cloud.retail.logging.ErrorContext)` (message)
  * `[ErrorLog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging#google.cloud.retail.logging.ErrorLog)` (message)
  * `[HttpRequestContext](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging#google.cloud.retail.logging.HttpRequestContext)` (message)
  * `[ImportErrorContext](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging#google.cloud.retail.logging.ImportErrorContext)` (message)
  * `[ServiceContext](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging#google.cloud.retail.logging.ServiceContext)` (message)
  * `[SourceLocation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging#google.cloud.retail.logging.SourceLocation)` (message)



## ErrorContext

A description of the context in which an error occurred.

Fields  
---  
`http_request` |  `[HttpRequestContext](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging#google.cloud.retail.logging.HttpRequestContext)` The HTTP request which was processed when the error was triggered.  
`report_location` |  `[SourceLocation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging#google.cloud.retail.logging.SourceLocation)` The location in the source code where the decision was made to report the error, usually the place where it was logged.  
  
## ErrorLog

An error log which is reported to the Error Reporting system. This proto a superset of google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent.

Fields  
---  
`service_context` |  `[ServiceContext](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging#google.cloud.retail.logging.ServiceContext)` The service context in which this error has occurred.  
`context` |  `[ErrorContext](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging#google.cloud.retail.logging.ErrorContext)` A description of the context in which the error occurred.  
`message` |  `string` A message describing the error.  
`status` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.rpc#google.rpc.Status)` The RPC status associated with the error log.  
`request_payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The API request payload, represented as a protocol buffer.Most API request types are supported. For example:"type.googleapis.com/google.cloud.retail.v2.ProductService.CreateProductRequest" "type.googleapis.com/google.cloud.retail.v2.UserEventService.WriteUserEventRequest"  
`response_payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The API response payload, represented as a protocol buffer.This is used to log some "soft errors", where the response is valid but we consider there are some quality issues like unjoined events.The following API responses are supported and no PII is included: "google.cloud.retail.v2.PredictionService.Predict" "google.cloud.retail.v2.UserEventService.WriteUserEvent" "google.cloud.retail.v2.UserEventService.CollectUserEvent"  
`import_payload` |  `[ImportErrorContext](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.logging#google.cloud.retail.logging.ImportErrorContext)` The error payload that is populated on LRO import APIs.  
  
## HttpRequestContext

HTTP request data that is related to a reported error.

Fields  
---  
`response_status_code` |  `int32` The HTTP response status code for the request.  
  
## ImportErrorContext

The error payload that is populated on LRO import APIs, including "google.cloud.retail.v2.ProductService.ImportProducts" and "google.cloud.retail.v2.EventService.ImportUserEvents".

Fields  
---  
`operation_name` |  `string` The operation resource name of the LRO.  
`gcs_path` |  `string` Cloud Storage file path of the import source. Can be set for batch operation error.  
`line_number` |  `string` Line number of the content in file. Should be empty for permission or batch operation error.  
Union field `line_content`. Detailed content which caused the error. Should be empty for permission or batch operation error. `line_content` can be only one of the following:  
`catalog_item` |  `string` The detailed content which caused the error on importing a catalog item.  
`product` |  `string` The detailed content which caused the error on importing a product.  
`user_event` |  `string` The detailed content which caused the error on importing a user event.  
  
## ServiceContext

Describes a running service that sends errors.

Fields  
---  
`service` |  `string` An identifier of the service. For example, "retail.googleapis.com".  
  
## SourceLocation

Indicates a location in the source code of the service for which errors are reported.

Fields  
---  
`function_name` |  `string` Human-readable name of a function or method. For example, "google.cloud.retail.v2.UserEventService.ImportUserEvents".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
