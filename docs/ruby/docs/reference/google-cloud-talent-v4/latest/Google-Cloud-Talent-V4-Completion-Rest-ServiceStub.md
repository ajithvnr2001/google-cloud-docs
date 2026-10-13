---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Rest-ServiceStub/
title: Cloud Talent Solution V4 API - Class Google::Cloud::Talent::V4::Completion::Rest::ServiceStub (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:43.991750+00:00
---

# Cloud Talent Solution V4 API - Class Google::Cloud::Talent::V4::Completion::Rest::ServiceStub (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Talent Solution V4 API - Class Google::Cloud::Talent::V4::Completion::Rest::ServiceStub (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.1  0.9.1  0.8.1  0.7.0  0.6.4 

Reference documentation and code samples for the Cloud Talent Solution V4 API class Google::Cloud::Talent::V4::Completion::Rest::ServiceStub.

REST service stub for the Completion service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #complete_query
    
    
    def complete_query(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Talent::V4::CompleteQueryResponse

Baseline implementation for the complete_query REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Talent::V4::CompleteQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-CompleteQueryRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Talent::V4::CompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-CompleteQueryResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Talent::V4::CompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-CompleteQueryResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



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



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
