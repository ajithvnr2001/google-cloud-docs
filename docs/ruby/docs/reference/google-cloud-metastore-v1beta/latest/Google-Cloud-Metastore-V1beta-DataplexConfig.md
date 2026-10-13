---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataplexConfig/
title: Dataproc Metastore V1beta API - Class Google::Cloud::Metastore::V1beta::DataplexConfig (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:41.672793+00:00
---

# Dataproc Metastore V1beta API - Class Google::Cloud::Metastore::V1beta::DataplexConfig (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataplexConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataproc Metastore V1beta API - Class Google::Cloud::Metastore::V1beta::DataplexConfig (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.0  0.20.0  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.2  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Dataproc Metastore V1beta API class Google::Cloud::Metastore::V1beta::DataplexConfig.

Specifies how metastore metadata should be integrated with the Dataplex service.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #lake_resources
    
    
    def lake_resources() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Metastore::V1beta::Lake}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Metastore::V1beta::Lake}) — A reference to the Lake resources that this metastore service is attached to. The key is the lake resource name. Example: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`. 



### #lake_resources=
    
    
    def lake_resources=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Metastore::V1beta::Lake}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Metastore::V1beta::Lake}) — A reference to the Lake resources that this metastore service is attached to. The key is the lake resource name. Example: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Metastore::V1beta::Lake}) — A reference to the Lake resources that this metastore service is attached to. The key is the lake resource name. Example: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
