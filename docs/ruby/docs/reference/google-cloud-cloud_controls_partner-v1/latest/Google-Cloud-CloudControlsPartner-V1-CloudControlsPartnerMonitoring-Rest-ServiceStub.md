---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerMonitoring-Rest-ServiceStub/
title: Cloud Controls Partner V1 API - Class Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerMonitoring::Rest::ServiceStub (v2.4.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:38:20.049005+00:00
---

# Cloud Controls Partner V1 API - Class Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerMonitoring::Rest::ServiceStub (v2.4.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-CloudControlsPartnerMonitoring-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Controls Partner V1 API - Class Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerMonitoring::Rest::ServiceStub (v2.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.1 (latest)  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.1.1 

Reference documentation and code samples for the Cloud Controls Partner V1 API class Google::Cloud::CloudControlsPartner::V1::CloudControlsPartnerMonitoring::Rest::ServiceStub.

REST service stub for the CloudControlsPartnerMonitoring service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_violation
    
    
    def get_violation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::CloudControlsPartner::V1::Violation

Baseline implementation for the get_violation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::CloudControlsPartner::V1::GetViolationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-GetViolationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::CloudControlsPartner::V1::Violation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Violation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::CloudControlsPartner::V1::Violation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Violation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_violations
    
    
    def list_violations(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::CloudControlsPartner::V1::ListViolationsResponse

Baseline implementation for the list_violations REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::CloudControlsPartner::V1::ListViolationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-ListViolationsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::CloudControlsPartner::V1::ListViolationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-ListViolationsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::CloudControlsPartner::V1::ListViolationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-ListViolationsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



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
