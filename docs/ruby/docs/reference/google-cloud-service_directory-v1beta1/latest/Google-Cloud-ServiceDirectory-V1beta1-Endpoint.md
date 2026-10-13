---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Cloud-ServiceDirectory-V1beta1-Endpoint/
title: Service Directory V1beta1 API - Class Google::Cloud::ServiceDirectory::V1beta1::Endpoint (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:16.411096+00:00
---

# Service Directory V1beta1 API - Class Google::Cloud::ServiceDirectory::V1beta1::Endpoint (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Cloud-ServiceDirectory-V1beta1-Endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Directory V1beta1 API - Class Google::Cloud::ServiceDirectory::V1beta1::Endpoint (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.1  0.20.0  0.19.1  0.18.0  0.17.1  0.16.0  0.15.2  0.14.2  0.13.0  0.12.1  0.11.1  0.10.0  0.9.0  0.8.0  0.7.4 

Reference documentation and code samples for the Service Directory V1beta1 API class Google::Cloud::ServiceDirectory::V1beta1::Endpoint.

An individual endpoint that provides a [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Cloud-ServiceDirectory-V1beta1-Service "Google::Cloud::ServiceDirectory::V1beta1::Service \(class\)"). The service must already exist to create an endpoint.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #address
    
    
    def address() -> ::String

**Returns**

  * (::String) — Optional. An IPv4 or IPv6 address. Service Directory rejects bad addresses like:

    * `8.8.8`
    * `8.8.8.8:53`
    * `test:bad:address`
    * `[::1]`
    * `[::1]:8080`

Limited to 45 characters. 




### #address=
    
    
    def address=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An IPv4 or IPv6 address. Service Directory rejects bad addresses like:

    * `8.8.8`
    * `8.8.8.8:53`
    * `test:bad:address`
    * `[::1]`
    * `[::1]:8080`

Limited to 45 characters. 




**Returns**

  * (::String) — Optional. An IPv4 or IPv6 address. Service Directory rejects bad addresses like:

    * `8.8.8`
    * `8.8.8.8:53`
    * `test:bad:address`
    * `[::1]`
    * `[::1]:8080`

Limited to 45 characters. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp when the endpoint was created. 



### #metadata
    
    
    def metadata() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Metadata for the endpoint. This data can be consumed by service clients.

Restrictions:

    * The entire metadata dictionary may contain up to 512 characters, spread accoss all key-value pairs. Metadata that goes beyond this limit are rejected
    * Valid metadata keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/). Metadata that fails to meet these requirements are rejected

Note: This field is equivalent to the `annotations` field in the v1 API. They have the same syntax and read/write to the same location in Service Directory. 




### #metadata=
    
    
    def metadata=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Metadata for the endpoint. This data can be consumed by service clients.

Restrictions:

    * The entire metadata dictionary may contain up to 512 characters, spread accoss all key-value pairs. Metadata that goes beyond this limit are rejected
    * Valid metadata keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/). Metadata that fails to meet these requirements are rejected

Note: This field is equivalent to the `annotations` field in the v1 API. They have the same syntax and read/write to the same location in Service Directory. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Metadata for the endpoint. This data can be consumed by service clients.

Restrictions:

    * The entire metadata dictionary may contain up to 512 characters, spread accoss all key-value pairs. Metadata that goes beyond this limit are rejected
    * Valid metadata keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/). Metadata that fails to meet these requirements are rejected

Note: This field is equivalent to the `annotations` field in the v1 API. They have the same syntax and read/write to the same location in Service Directory. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Immutable. The resource name for the endpoint in the format `projects/*/locations/*/namespaces/*/services/*/endpoints/*`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Immutable. The resource name for the endpoint in the format `projects/*/locations/*/namespaces/*/services/*/endpoints/*`. 



**Returns**

  * (::String) — Immutable. The resource name for the endpoint in the format `projects/*/locations/*/namespaces/*/services/*/endpoints/*`. 



### #network
    
    
    def network() -> ::String

**Returns**

  * (::String) — Immutable. The Google Compute Engine network (VPC) of the endpoint in the format `projects/<project number>/locations/global/networks/*`.

The project must be specified by project number (project id is rejected). Incorrectly formatted networks are rejected, but no other validation is performed on this field (ex. network or project existence, reachability, or permissions). 




### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — Immutable. The Google Compute Engine network (VPC) of the endpoint in the format `projects/<project number>/locations/global/networks/*`.

The project must be specified by project number (project id is rejected). Incorrectly formatted networks are rejected, but no other validation is performed on this field (ex. network or project existence, reachability, or permissions). 




**Returns**

  * (::String) — Immutable. The Google Compute Engine network (VPC) of the endpoint in the format `projects/<project number>/locations/global/networks/*`.

The project must be specified by project number (project id is rejected). Incorrectly formatted networks are rejected, but no other validation is performed on this field (ex. network or project existence, reachability, or permissions). 




### #port
    
    
    def port() -> ::Integer

**Returns**

  * (::Integer) — Optional. Service Directory rejects values outside of `[0, 65535]`. 



### #port=
    
    
    def port=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Service Directory rejects values outside of `[0, 65535]`. 



**Returns**

  * (::Integer) — Optional. Service Directory rejects values outside of `[0, 65535]`. 



### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. A globally unique identifier (in UUID4 format) for this endpoint. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp when the endpoint was last updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
