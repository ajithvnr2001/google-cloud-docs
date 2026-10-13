---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryConfig/
title: Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::DiscoveryConfig (v1.19.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:39.350368+00:00
---

# Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::DiscoveryConfig (v1.19.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::DiscoveryConfig (v1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.1  1.17.0  1.16.1  1.15.2  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.2  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1 

Reference documentation and code samples for the Cloud Data Loss Prevention (DLP) V2 API class Google::Cloud::Dlp::V2::DiscoveryConfig.

Configuration for discovery to scan resources for profile generation. Only one discovery configuration may exist per organization, folder, or project.

The generated data profiles are retained according to the [data retention policy](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #actions
    
    
    def actions() -> ::Array<::Google::Cloud::Dlp::V2::DataProfileAction>

**Returns**

  * (::Array<[::Google::Cloud::Dlp::V2::DataProfileAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DataProfileAction)>) — Actions to execute at the completion of scanning. 



### #actions=
    
    
    def actions=(value) -> ::Array<::Google::Cloud::Dlp::V2::DataProfileAction>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dlp::V2::DataProfileAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DataProfileAction)>) — Actions to execute at the completion of scanning. 



**Returns**

  * (::Array<[::Google::Cloud::Dlp::V2::DataProfileAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DataProfileAction)>) — Actions to execute at the completion of scanning. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Protobuf-Timestamp)) — Output only. The creation timestamp of a DiscoveryConfig. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Display name (max 100 chars) 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Display name (max 100 chars) 



**Returns**

  * (::String) — Display name (max 100 chars) 



### #errors
    
    
    def errors() -> ::Array<::Google::Cloud::Dlp::V2::Error>

**Returns**

  * (::Array<[::Google::Cloud::Dlp::V2::Error](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-Error)>) — Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared. 



### #inspect_templates
    
    
    def inspect_templates() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Detection logic for profile generation.

Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.

Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.

For more information, see https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency. 




### #inspect_templates=
    
    
    def inspect_templates=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Detection logic for profile generation.

Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.

Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.

For more information, see https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency. 




**Returns**

  * (::Array<::String>) — Detection logic for profile generation.

Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery.

Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.

For more information, see https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency. 




### #last_run_time
    
    
    def last_run_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp of the last time this config was executed. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Unique resource name for the DiscoveryConfig, assigned by the service when the DiscoveryConfig is created, for example `projects/dlp-test-project/locations/global/discoveryConfigs/53234423`. 



### #org_config
    
    
    def org_config() -> ::Google::Cloud::Dlp::V2::DiscoveryConfig::OrgConfig

**Returns**

  * ([::Google::Cloud::Dlp::V2::DiscoveryConfig::OrgConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryConfig-OrgConfig)) — Only set when the parent is an org. 



### #org_config=
    
    
    def org_config=(value) -> ::Google::Cloud::Dlp::V2::DiscoveryConfig::OrgConfig

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::DiscoveryConfig::OrgConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryConfig-OrgConfig)) — Only set when the parent is an org. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::DiscoveryConfig::OrgConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryConfig-OrgConfig)) — Only set when the parent is an org. 



### #other_cloud_starting_location
    
    
    def other_cloud_starting_location() -> ::Google::Cloud::Dlp::V2::OtherCloudDiscoveryStartingLocation

**Returns**

  * ([::Google::Cloud::Dlp::V2::OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-OtherCloudDiscoveryStartingLocation)) — Must be set only when scanning other clouds. 



### #other_cloud_starting_location=
    
    
    def other_cloud_starting_location=(value) -> ::Google::Cloud::Dlp::V2::OtherCloudDiscoveryStartingLocation

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-OtherCloudDiscoveryStartingLocation)) — Must be set only when scanning other clouds. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-OtherCloudDiscoveryStartingLocation)) — Must be set only when scanning other clouds. 



### #processing_location
    
    
    def processing_location() -> ::Google::Cloud::Dlp::V2::ProcessingLocation

**Returns**

  * ([::Google::Cloud::Dlp::V2::ProcessingLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ProcessingLocation)) — Optional. Processing location configuration. Vertex AI dataset scanning will set processing_location.image_fallback_type to MultiRegionProcessing by default. 



### #processing_location=
    
    
    def processing_location=(value) -> ::Google::Cloud::Dlp::V2::ProcessingLocation

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::ProcessingLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ProcessingLocation)) — Optional. Processing location configuration. Vertex AI dataset scanning will set processing_location.image_fallback_type to MultiRegionProcessing by default. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::ProcessingLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ProcessingLocation)) — Optional. Processing location configuration. Vertex AI dataset scanning will set processing_location.image_fallback_type to MultiRegionProcessing by default. 



### #status
    
    
    def status() -> ::Google::Cloud::Dlp::V2::DiscoveryConfig::Status

**Returns**

  * ([::Google::Cloud::Dlp::V2::DiscoveryConfig::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryConfig-Status)) — Required. A status for this configuration. 



### #status=
    
    
    def status=(value) -> ::Google::Cloud::Dlp::V2::DiscoveryConfig::Status

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::DiscoveryConfig::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryConfig-Status)) — Required. A status for this configuration. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::DiscoveryConfig::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryConfig-Status)) — Required. A status for this configuration. 



### #targets
    
    
    def targets() -> ::Array<::Google::Cloud::Dlp::V2::DiscoveryTarget>

**Returns**

  * (::Array<[::Google::Cloud::Dlp::V2::DiscoveryTarget](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryTarget)>) — Target to match against for determining what to scan and how frequently. 



### #targets=
    
    
    def targets=(value) -> ::Array<::Google::Cloud::Dlp::V2::DiscoveryTarget>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dlp::V2::DiscoveryTarget](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryTarget)>) — Target to match against for determining what to scan and how frequently. 



**Returns**

  * (::Array<[::Google::Cloud::Dlp::V2::DiscoveryTarget](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DiscoveryTarget)>) — Target to match against for determining what to scan and how frequently. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Protobuf-Timestamp)) — Output only. The last update timestamp of a DiscoveryConfig. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
