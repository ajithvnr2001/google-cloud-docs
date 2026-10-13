---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-QueryDirectoryContentsRequest/
title: Dataform V1 API - Class Google::Cloud::Dataform::V1::QueryDirectoryContentsRequest (v1.3.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:34.577297+00:00
---

# Dataform V1 API - Class Google::Cloud::Dataform::V1::QueryDirectoryContentsRequest (v1.3.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-QueryDirectoryContentsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataform V1 API - Class Google::Cloud::Dataform::V1::QueryDirectoryContentsRequest (v1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataform V1 API class Google::Cloud::Dataform::V1::QueryDirectoryContentsRequest.

`QueryDirectoryContents` request message.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Maximum number of paths to return. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Maximum number of paths to return. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default. 



**Returns**

  * (::Integer) — Optional. Maximum number of paths to return. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. Page token received from a previous `QueryDirectoryContents` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `QueryDirectoryContents`, with the exception of `page_size`, must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Page token received from a previous `QueryDirectoryContents` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `QueryDirectoryContents`, with the exception of `page_size`, must match the call that provided the page token. 




**Returns**

  * (::String) — Optional. Page token received from a previous `QueryDirectoryContents` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `QueryDirectoryContents`, with the exception of `page_size`, must match the call that provided the page token. 




### #path
    
    
    def path() -> ::String

**Returns**

  * (::String) — Optional. The directory's full path including directory name, relative to the workspace root. If left unset, the workspace root is used. 



### #path=
    
    
    def path=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The directory's full path including directory name, relative to the workspace root. If left unset, the workspace root is used. 



**Returns**

  * (::String) — Optional. The directory's full path including directory name, relative to the workspace root. If left unset, the workspace root is used. 



### #view
    
    
    def view() -> ::Google::Cloud::Dataform::V1::DirectoryContentsView

**Returns**

  * ([::Google::Cloud::Dataform::V1::DirectoryContentsView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-DirectoryContentsView)) — Optional. Specifies the metadata to return for each directory entry. If unspecified, the default is `DIRECTORY_CONTENTS_VIEW_BASIC`. Currently the `DIRECTORY_CONTENTS_VIEW_METADATA` view is not supported by CMEK-protected workspaces. 



### #view=
    
    
    def view=(value) -> ::Google::Cloud::Dataform::V1::DirectoryContentsView

**Parameter**

  * **value** ([::Google::Cloud::Dataform::V1::DirectoryContentsView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-DirectoryContentsView)) — Optional. Specifies the metadata to return for each directory entry. If unspecified, the default is `DIRECTORY_CONTENTS_VIEW_BASIC`. Currently the `DIRECTORY_CONTENTS_VIEW_METADATA` view is not supported by CMEK-protected workspaces. 



**Returns**

  * ([::Google::Cloud::Dataform::V1::DirectoryContentsView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-DirectoryContentsView)) — Optional. Specifies the metadata to return for each directory entry. If unspecified, the default is `DIRECTORY_CONTENTS_VIEW_BASIC`. Currently the `DIRECTORY_CONTENTS_VIEW_METADATA` view is not supported by CMEK-protected workspaces. 



### #workspace
    
    
    def workspace() -> ::String

**Returns**

  * (::String) — Required. The workspace's name. 



### #workspace=
    
    
    def workspace=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The workspace's name. 



**Returns**

  * (::String) — Required. The workspace's name. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
