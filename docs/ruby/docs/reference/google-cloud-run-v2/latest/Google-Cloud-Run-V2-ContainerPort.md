---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-ContainerPort/
title: Cloud Run V2 API - Class Google::Cloud::Run::V2::ContainerPort (v0.29.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:03.544515+00:00
---

# Cloud Run V2 API - Class Google::Cloud::Run::V2::ContainerPort (v0.29.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-ContainerPort/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Run V2 API - Class Google::Cloud::Run::V2::ContainerPort (v0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.1  0.23.0  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.2  0.12.0  0.11.0  0.10.1  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Run V2 API class Google::Cloud::Run::V2::ContainerPort.

ContainerPort represents a network port in a single container.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #container_port
    
    
    def container_port() -> ::Integer

**Returns**

  * (::Integer) — Port number the container listens on. This must be a valid TCP port number, 0 < container_port < 65536\. 



### #container_port=
    
    
    def container_port=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Port number the container listens on. This must be a valid TCP port number, 0 < container_port < 65536\. 



**Returns**

  * (::Integer) — Port number the container listens on. This must be a valid TCP port number, 0 < container_port < 65536\. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — If specified, used to specify which protocol to use. Allowed values are "http1" and "h2c". 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — If specified, used to specify which protocol to use. Allowed values are "http1" and "h2c". 



**Returns**

  * (::String) — If specified, used to specify which protocol to use. Allowed values are "http1" and "h2c". 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
