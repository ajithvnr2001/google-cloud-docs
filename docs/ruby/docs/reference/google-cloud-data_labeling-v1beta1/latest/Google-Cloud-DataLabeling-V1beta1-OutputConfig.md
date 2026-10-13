---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-OutputConfig/
title: AI Platform Data Labeling Service V1beta1 API - Class Google::Cloud::DataLabeling::V1beta1::OutputConfig (v0.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:41.857911+00:00
---

# AI Platform Data Labeling Service V1beta1 API - Class Google::Cloud::DataLabeling::V1beta1::OutputConfig (v0.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-OutputConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AI Platform Data Labeling Service V1beta1 API - Class Google::Cloud::DataLabeling::V1beta1::OutputConfig (v0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.0 (latest)  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.1  0.9.0  0.8.1  0.7.2  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the AI Platform Data Labeling Service V1beta1 API class Google::Cloud::DataLabeling::V1beta1::OutputConfig.

The configuration of output data.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #gcs_destination
    
    
    def gcs_destination() -> ::Google::Cloud::DataLabeling::V1beta1::GcsDestination

**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::GcsDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-GcsDestination)) — Output to a file in Cloud Storage. Should be used for labeling output other than image segmentation.

Note: The following fields are mutually exclusive: `gcs_destination`, `gcs_folder_destination`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_destination=
    
    
    def gcs_destination=(value) -> ::Google::Cloud::DataLabeling::V1beta1::GcsDestination

**Parameter**

  * **value** ([::Google::Cloud::DataLabeling::V1beta1::GcsDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-GcsDestination)) — Output to a file in Cloud Storage. Should be used for labeling output other than image segmentation.

Note: The following fields are mutually exclusive: `gcs_destination`, `gcs_folder_destination`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::GcsDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-GcsDestination)) — Output to a file in Cloud Storage. Should be used for labeling output other than image segmentation.

Note: The following fields are mutually exclusive: `gcs_destination`, `gcs_folder_destination`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_folder_destination
    
    
    def gcs_folder_destination() -> ::Google::Cloud::DataLabeling::V1beta1::GcsFolderDestination

**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::GcsFolderDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-GcsFolderDestination)) — Output to a folder in Cloud Storage. Should be used for image segmentation labeling output.

Note: The following fields are mutually exclusive: `gcs_folder_destination`, `gcs_destination`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_folder_destination=
    
    
    def gcs_folder_destination=(value) -> ::Google::Cloud::DataLabeling::V1beta1::GcsFolderDestination

**Parameter**

  * **value** ([::Google::Cloud::DataLabeling::V1beta1::GcsFolderDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-GcsFolderDestination)) — Output to a folder in Cloud Storage. Should be used for image segmentation labeling output.

Note: The following fields are mutually exclusive: `gcs_folder_destination`, `gcs_destination`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::GcsFolderDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-GcsFolderDestination)) — Output to a folder in Cloud Storage. Should be used for image segmentation labeling output.

Note: The following fields are mutually exclusive: `gcs_folder_destination`, `gcs_destination`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
