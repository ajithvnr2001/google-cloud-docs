---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-BigQueryDestination/
title: Capacity Planner V1BETA API - Class Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination (v0.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:25.223211+00:00
---

# Capacity Planner V1BETA API - Class Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination (v0.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-BigQueryDestination/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Capacity Planner V1BETA API - Class Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination (v0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Capacity Planner V1BETA API class Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination.

A BigQuery destination for exporting assets to.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_disposition
    
    
    def create_disposition() -> ::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::CreateDisposition

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::CreateDisposition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-BigQueryDestination-CreateDisposition)) — Optional. Specifies the action that occurs if the destination table does not exist 



### #create_disposition=
    
    
    def create_disposition=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::CreateDisposition

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::CreateDisposition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-BigQueryDestination-CreateDisposition)) — Optional. Specifies the action that occurs if the destination table does not exist 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::CreateDisposition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-BigQueryDestination-CreateDisposition)) — Optional. Specifies the action that occurs if the destination table does not exist 



### #dataset
    
    
    def dataset() -> ::String

**Returns**

  * (::String) — Required. The BigQuery dataset in format "projects/{projectId}/datasets/{datasetId}", to which the snapshot result should be exported. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error. 



### #dataset=
    
    
    def dataset=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The BigQuery dataset in format "projects/{projectId}/datasets/{datasetId}", to which the snapshot result should be exported. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error. 



**Returns**

  * (::String) — Required. The BigQuery dataset in format "projects/{projectId}/datasets/{datasetId}", to which the snapshot result should be exported. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error. 



### #gcs_location
    
    
    def gcs_location() -> ::String

**Returns**

  * (::String) — Optional. Specifies the Cloud Storage location. Users can choose to provide a location for Cloud Storage bucket to store the exported data. (as it is possible that some locations are restricted via org policy for that project) Temporary Cloud Storage bucket creation is an interim step for BigQuery upload. If no value is provided, the default location used will be 'US'. 



### #gcs_location=
    
    
    def gcs_location=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Specifies the Cloud Storage location. Users can choose to provide a location for Cloud Storage bucket to store the exported data. (as it is possible that some locations are restricted via org policy for that project) Temporary Cloud Storage bucket creation is an interim step for BigQuery upload. If no value is provided, the default location used will be 'US'. 



**Returns**

  * (::String) — Optional. Specifies the Cloud Storage location. Users can choose to provide a location for Cloud Storage bucket to store the exported data. (as it is possible that some locations are restricted via org policy for that project) Temporary Cloud Storage bucket creation is an interim step for BigQuery upload. If no value is provided, the default location used will be 'US'. 



### #partition_key
    
    
    def partition_key() -> ::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::PartitionKey

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::PartitionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-BigQueryDestination-PartitionKey)) — Optional. The partition key for BigQuery partitioned table. 



### #partition_key=
    
    
    def partition_key=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::PartitionKey

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::PartitionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-BigQueryDestination-PartitionKey)) — Optional. The partition key for BigQuery partitioned table. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::PartitionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-BigQueryDestination-PartitionKey)) — Optional. The partition key for BigQuery partitioned table. 



### #table
    
    
    def table() -> ::String

**Returns**

  * (::String) — Required. The BigQuery table to which the snapshot result should be written. 



### #table=
    
    
    def table=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The BigQuery table to which the snapshot result should be written. 



**Returns**

  * (::String) — Required. The BigQuery table to which the snapshot result should be written. 



### #write_disposition
    
    
    def write_disposition() -> ::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::WriteDisposition

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::WriteDisposition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-BigQueryDestination-WriteDisposition)) — Optional. Specifies the action that occurs if the destination table or partition already exists. 



### #write_disposition=
    
    
    def write_disposition=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::WriteDisposition

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::WriteDisposition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-BigQueryDestination-WriteDisposition)) — Optional. Specifies the action that occurs if the destination table or partition already exists. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::BigQueryDestination::WriteDisposition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-BigQueryDestination-WriteDisposition)) — Optional. Specifies the action that occurs if the destination table or partition already exists. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
