---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-BigQueryExport/
title: Chronicle V1 API - Class Google::Cloud::Chronicle::V1::BigQueryExport (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:01.218306+00:00
---

# Chronicle V1 API - Class Google::Cloud::Chronicle::V1::BigQueryExport (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-BigQueryExport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Chronicle V1 API - Class Google::Cloud::Chronicle::V1::BigQueryExport (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Chronicle V1 API class Google::Cloud::Chronicle::V1::BigQueryExport.

This resource represents the BigQuery export configuration for a Chronicle instance which includes Google Cloud Platform resources like Cloud Storage buckets, BigQuery datasets etc and the export settings for each data source.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #big_query_export_package
    
    
    def big_query_export_package() -> ::Google::Cloud::Chronicle::V1::BigQueryExportPackage

**Returns**

  * ([::Google::Cloud::Chronicle::V1::BigQueryExportPackage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-BigQueryExportPackage)) — Output only. The BigQueryExportPackage entitled for the Chronicle instance. 



### #entity_graph_settings
    
    
    def entity_graph_settings() -> ::Google::Cloud::Chronicle::V1::DataSourceExportSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the Entity Graph data source. 



### #entity_graph_settings=
    
    
    def entity_graph_settings=(value) -> ::Google::Cloud::Chronicle::V1::DataSourceExportSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the Entity Graph data source. 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the Entity Graph data source. 



### #ioc_matches_settings
    
    
    def ioc_matches_settings() -> ::Google::Cloud::Chronicle::V1::DataSourceExportSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the IOC Matches data source. 



### #ioc_matches_settings=
    
    
    def ioc_matches_settings=(value) -> ::Google::Cloud::Chronicle::V1::DataSourceExportSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the IOC Matches data source. 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the IOC Matches data source. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. The resource name of the BigQueryExport. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The resource name of the BigQueryExport. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport 



**Returns**

  * (::String) — Identifier. The resource name of the BigQueryExport. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport 



### #provisioned
    
    
    def provisioned() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Whether the BigQueryExport has been provisioned for the Chronicle instance. 



### #rule_detections_settings
    
    
    def rule_detections_settings() -> ::Google::Cloud::Chronicle::V1::DataSourceExportSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the Rule Detections data source. 



### #rule_detections_settings=
    
    
    def rule_detections_settings=(value) -> ::Google::Cloud::Chronicle::V1::DataSourceExportSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the Rule Detections data source. 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the Rule Detections data source. 



### #udm_events_aggregates_settings
    
    
    def udm_events_aggregates_settings() -> ::Google::Cloud::Chronicle::V1::DataSourceExportSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the UDM Events Aggregates data source. 



### #udm_events_aggregates_settings=
    
    
    def udm_events_aggregates_settings=(value) -> ::Google::Cloud::Chronicle::V1::DataSourceExportSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the UDM Events Aggregates data source. 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the UDM Events Aggregates data source. 



### #udm_events_settings
    
    
    def udm_events_settings() -> ::Google::Cloud::Chronicle::V1::DataSourceExportSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the UDM Events data source. 



### #udm_events_settings=
    
    
    def udm_events_settings=(value) -> ::Google::Cloud::Chronicle::V1::DataSourceExportSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the UDM Events data source. 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::DataSourceExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DataSourceExportSettings)) — Optional. The export settings for the UDM Events data source. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
