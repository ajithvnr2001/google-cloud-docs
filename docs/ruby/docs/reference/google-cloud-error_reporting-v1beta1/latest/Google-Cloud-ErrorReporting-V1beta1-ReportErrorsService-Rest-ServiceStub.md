---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ReportErrorsService-Rest-ServiceStub/
title: Error Reporting V1beta1 API - Class Google::Cloud::ErrorReporting::V1beta1::ReportErrorsService::Rest::ServiceStub (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:40.014218+00:00
---

# Error Reporting V1beta1 API - Class Google::Cloud::ErrorReporting::V1beta1::ReportErrorsService::Rest::ServiceStub (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ReportErrorsService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Error Reporting V1beta1 API - Class Google::Cloud::ErrorReporting::V1beta1::ReportErrorsService::Rest::ServiceStub (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.1  0.14.0  0.13.1  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.5 

Reference documentation and code samples for the Error Reporting V1beta1 API class Google::Cloud::ErrorReporting::V1beta1::ReportErrorsService::Rest::ServiceStub.

REST service stub for the ReportErrorsService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #report_error_event
    
    
    def report_error_event(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::ErrorReporting::V1beta1::ReportErrorEventResponse

Baseline implementation for the report_error_event REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::ErrorReporting::V1beta1::ReportErrorEventRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ReportErrorEventRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ErrorReporting::V1beta1::ReportErrorEventResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ReportErrorEventResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ErrorReporting::V1beta1::ReportErrorEventResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting-v1beta1/latest/Google-Cloud-ErrorReporting-V1beta1-ReportErrorEventResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
