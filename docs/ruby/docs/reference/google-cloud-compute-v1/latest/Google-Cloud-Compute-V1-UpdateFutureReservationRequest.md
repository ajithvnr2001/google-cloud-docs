---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-UpdateFutureReservationRequest/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::UpdateFutureReservationRequest (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:30.041034+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::UpdateFutureReservationRequest (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-UpdateFutureReservationRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::UpdateFutureReservationRequest (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::UpdateFutureReservationRequest.

A request message for FutureReservations.Update. See the method description for details.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #future_reservation
    
    
    def future_reservation() -> ::String

**Returns**

  * (::String) — Name of the reservation to update. Name should conform to RFC1035. 



### #future_reservation=
    
    
    def future_reservation=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the reservation to update. Name should conform to RFC1035. 



**Returns**

  * (::String) — Name of the reservation to update. Name should conform to RFC1035. 



### #future_reservation_resource
    
    
    def future_reservation_resource() -> ::Google::Cloud::Compute::V1::FutureReservation

**Returns**

  * ([::Google::Cloud::Compute::V1::FutureReservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FutureReservation)) — The body resource for this request 



### #future_reservation_resource=
    
    
    def future_reservation_resource=(value) -> ::Google::Cloud::Compute::V1::FutureReservation

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::FutureReservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FutureReservation)) — The body resource for this request 



**Returns**

  * ([::Google::Cloud::Compute::V1::FutureReservation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FutureReservation)) — The body resource for this request 



### #project
    
    
    def project() -> ::String

**Returns**

  * (::String) — Project ID for this request. 



### #project=
    
    
    def project=(value) -> ::String

**Parameter**

  * **value** (::String) — Project ID for this request. 



**Returns**

  * (::String) — Project ID for this request. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #update_mask
    
    
    def update_mask() -> ::String

**Returns**

  * (::String) — update_mask indicates fields to be updated as part of this request. 



### #update_mask=
    
    
    def update_mask=(value) -> ::String

**Parameter**

  * **value** (::String) — update_mask indicates fields to be updated as part of this request. 



**Returns**

  * (::String) — update_mask indicates fields to be updated as part of this request. 



### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — Name of the zone for this request. Name should conform to RFC1035. 



### #zone=
    
    
    def zone=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the zone for this request. Name should conform to RFC1035. 



**Returns**

  * (::String) — Name of the zone for this request. Name should conform to RFC1035. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
