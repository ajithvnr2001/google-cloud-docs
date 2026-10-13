---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secure_source_manager-v1/latest/Google-Cloud-SecureSourceManager-V1-PullRequestComment-Code/
title: Secure Source Manager V1 API - Class Google::Cloud::SecureSourceManager::V1::PullRequestComment::Code (v2.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:46.568762+00:00
---

# Secure Source Manager V1 API - Class Google::Cloud::SecureSourceManager::V1::PullRequestComment::Code (v2.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secure_source_manager-v1/latest/Google-Cloud-SecureSourceManager-V1-PullRequestComment-Code/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secure Source Manager V1 API - Class Google::Cloud::SecureSourceManager::V1::PullRequestComment::Code (v2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.0 (latest)  2.8.1  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.4.0  0.3.0  0.2.2  0.1.0 

Reference documentation and code samples for the Secure Source Manager V1 API class Google::Cloud::SecureSourceManager::V1::PullRequestComment::Code.

The comment on a code line.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #body
    
    
    def body() -> ::String

**Returns**

  * (::String) — Required. The comment body. 



### #body=
    
    
    def body=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The comment body. 



**Returns**

  * (::String) — Required. The comment body. 



### #effective_commit_sha
    
    
    def effective_commit_sha() -> ::String

**Returns**

  * (::String) — Output only. The effective commit sha this code comment is pointing to. 



### #effective_root_comment
    
    
    def effective_root_comment() -> ::String

**Returns**

  * (::String) — Output only. The root comment of the conversation, derived from the reply field. 



### #position
    
    
    def position() -> ::Google::Cloud::SecureSourceManager::V1::PullRequestComment::Position

**Returns**

  * ([::Google::Cloud::SecureSourceManager::V1::PullRequestComment::Position](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secure_source_manager-v1/latest/Google-Cloud-SecureSourceManager-V1-PullRequestComment-Position)) — Optional. The position of the comment. 



### #position=
    
    
    def position=(value) -> ::Google::Cloud::SecureSourceManager::V1::PullRequestComment::Position

**Parameter**

  * **value** ([::Google::Cloud::SecureSourceManager::V1::PullRequestComment::Position](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secure_source_manager-v1/latest/Google-Cloud-SecureSourceManager-V1-PullRequestComment-Position)) — Optional. The position of the comment. 



**Returns**

  * ([::Google::Cloud::SecureSourceManager::V1::PullRequestComment::Position](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secure_source_manager-v1/latest/Google-Cloud-SecureSourceManager-V1-PullRequestComment-Position)) — Optional. The position of the comment. 



### #reply
    
    
    def reply() -> ::String

**Returns**

  * (::String) — Optional. Input only. The PullRequestComment resource name that this comment is replying to. 



### #reply=
    
    
    def reply=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Input only. The PullRequestComment resource name that this comment is replying to. 



**Returns**

  * (::String) — Optional. Input only. The PullRequestComment resource name that this comment is replying to. 



### #resolved
    
    
    def resolved() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Boolean indicator if the comment is resolved. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
