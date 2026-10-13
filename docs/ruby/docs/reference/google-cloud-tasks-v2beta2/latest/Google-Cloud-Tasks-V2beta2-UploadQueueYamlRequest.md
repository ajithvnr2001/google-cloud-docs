---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-UploadQueueYamlRequest/
title: Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::UploadQueueYamlRequest (v0.18.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:32.262898+00:00
---

# Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::UploadQueueYamlRequest (v0.18.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-UploadQueueYamlRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::UploadQueueYamlRequest (v0.18.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.2 (latest)  0.18.1  0.17.0  0.16.1  0.15.0  0.14.1  0.13.0  0.12.1  0.11.3  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.5 

Reference documentation and code samples for the Cloud Tasks V2beta2 API class Google::Cloud::Tasks::V2beta2::UploadQueueYamlRequest.

Request message for [UploadQueueYaml](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-CloudTasks-Client#Google__Cloud__Tasks__V2beta2__CloudTasks__Client_upload_queue_yaml_instance_ "Google::Cloud::Tasks::V2beta2::CloudTasks::Client#upload_queue_yaml \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #app_id
    
    
    def app_id() -> ::String

**Returns**

  * (::String) — Required. The App ID is supplied as an HTTP parameter. Unlike internal usage of App ID, it does not include a region prefix. Rather, the App ID represents the Project ID against which to make the request. 



### #app_id=
    
    
    def app_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The App ID is supplied as an HTTP parameter. Unlike internal usage of App ID, it does not include a region prefix. Rather, the App ID represents the Project ID against which to make the request. 



**Returns**

  * (::String) — Required. The App ID is supplied as an HTTP parameter. Unlike internal usage of App ID, it does not include a region prefix. Rather, the App ID represents the Project ID against which to make the request. 



### #http_body
    
    
    def http_body() -> ::Google::Api::HttpBody

**Returns**

  * ([::Google::Api::HttpBody](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Api-HttpBody)) — The http body contains the queue.yaml file which used to update queue lists 



### #http_body=
    
    
    def http_body=(value) -> ::Google::Api::HttpBody

**Parameter**

  * **value** ([::Google::Api::HttpBody](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Api-HttpBody)) — The http body contains the queue.yaml file which used to update queue lists 



**Returns**

  * ([::Google::Api::HttpBody](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Api-HttpBody)) — The http body contains the queue.yaml file which used to update queue lists 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
