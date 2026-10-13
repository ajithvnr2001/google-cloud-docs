---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-UpdateFolderRequest/
title: Dataform V1 API - Class Google::Cloud::Dataform::V1::UpdateFolderRequest (v1.3.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:43.262690+00:00
---

# Dataform V1 API - Class Google::Cloud::Dataform::V1::UpdateFolderRequest (v1.3.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-UpdateFolderRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataform V1 API - Class Google::Cloud::Dataform::V1::UpdateFolderRequest (v1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataform V1 API class Google::Cloud::Dataform::V1::UpdateFolderRequest.

`UpdateFolder` request message.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #folder
    
    
    def folder() -> ::Google::Cloud::Dataform::V1::Folder

**Returns**

  * ([::Google::Cloud::Dataform::V1::Folder](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-Folder)) — Required. The updated Folder. 



### #folder=
    
    
    def folder=(value) -> ::Google::Cloud::Dataform::V1::Folder

**Parameter**

  * **value** ([::Google::Cloud::Dataform::V1::Folder](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-Folder)) — Required. The updated Folder. 



**Returns**

  * ([::Google::Cloud::Dataform::V1::Folder](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-Folder)) — Required. The updated Folder. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Protobuf-FieldMask)) — Optional. Specifies the fields to be updated in the Folder. If left unset, all fields that can be updated, will be updated. A few fields cannot be updated and will be ignored if specified in the update_mask (e.g. parent_name, team_folder_name). 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Protobuf-FieldMask)) — Optional. Specifies the fields to be updated in the Folder. If left unset, all fields that can be updated, will be updated. A few fields cannot be updated and will be ignored if specified in the update_mask (e.g. parent_name, team_folder_name). 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Protobuf-FieldMask)) — Optional. Specifies the fields to be updated in the Folder. If left unset, all fields that can be updated, will be updated. A few fields cannot be updated and will be ignored if specified in the update_mask (e.g. parent_name, team_folder_name). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
