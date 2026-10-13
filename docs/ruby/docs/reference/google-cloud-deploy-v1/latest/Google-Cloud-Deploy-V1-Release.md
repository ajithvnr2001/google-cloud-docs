---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Release/
title: Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::Release (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:20.149111+00:00
---

# Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::Release (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Release/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::Release (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.1  2.0.2  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.0  1.0.0  0.20.0  0.19.1  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Google Cloud Deploy V1 API class Google::Cloud::Deploy::V1::Release.

A `Release` resource in the Cloud Deploy API.

A `Release` defines a specific Skaffold configuration instance that can be deployed.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #abandoned
    
    
    def abandoned() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Indicates whether this is an abandoned release. 



### #annotations
    
    
    def annotations() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. 



### #annotations=
    
    
    def annotations=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. 



### #build_artifacts
    
    
    def build_artifacts() -> ::Array<::Google::Cloud::Deploy::V1::BuildArtifact>

**Returns**

  * (::Array<[::Google::Cloud::Deploy::V1::BuildArtifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-BuildArtifact)>) — Optional. List of artifacts to pass through to Skaffold command. 



### #build_artifacts=
    
    
    def build_artifacts=(value) -> ::Array<::Google::Cloud::Deploy::V1::BuildArtifact>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Deploy::V1::BuildArtifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-BuildArtifact)>) — Optional. List of artifacts to pass through to Skaffold command. 



**Returns**

  * (::Array<[::Google::Cloud::Deploy::V1::BuildArtifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-BuildArtifact)>) — Optional. List of artifacts to pass through to Skaffold command. 



### #condition
    
    
    def condition() -> ::Google::Cloud::Deploy::V1::Release::ReleaseCondition

**Returns**

  * ([::Google::Cloud::Deploy::V1::Release::ReleaseCondition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Release-ReleaseCondition)) — Output only. Information around the state of the Release. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time at which the `Release` was created. 



### #custom_target_type_snapshots
    
    
    def custom_target_type_snapshots() -> ::Array<::Google::Cloud::Deploy::V1::CustomTargetType>

**Returns**

  * (::Array<[::Google::Cloud::Deploy::V1::CustomTargetType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-CustomTargetType)>) — Output only. Snapshot of the custom target types referenced by the targets taken at release creation time. 



### #delivery_pipeline_snapshot
    
    
    def delivery_pipeline_snapshot() -> ::Google::Cloud::Deploy::V1::DeliveryPipeline

**Returns**

  * ([::Google::Cloud::Deploy::V1::DeliveryPipeline](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-DeliveryPipeline)) — Output only. Snapshot of the parent pipeline taken at release creation time. 



### #deploy_parameters
    
    
    def deploy_parameters() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. The deploy parameters to use for all targets in this release. 



### #deploy_parameters=
    
    
    def deploy_parameters=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. The deploy parameters to use for all targets in this release. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. The deploy parameters to use for all targets in this release. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Description of the `Release`. Max length is 255 characters. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Description of the `Release`. Max length is 255 characters. 



**Returns**

  * (::String) — Optional. Description of the `Release`. Max length is 255 characters. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 



**Returns**

  * (::String) — This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
    * All characters must use UTF-8 encoding, and international characters are allowed.
    * Keys must start with a lowercase letter or international character.
    * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes. 




### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
    * All characters must use UTF-8 encoding, and international characters are allowed.
    * Keys must start with a lowercase letter or international character.
    * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
    * All characters must use UTF-8 encoding, and international characters are allowed.
    * Keys must start with a lowercase letter or international character.
    * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. Name of the `Release`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}`. The `release` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. Name of the `Release`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}`. The `release` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`



**Returns**

  * (::String) — Identifier. Name of the `Release`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}`. The `release` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`



### #render_end_time
    
    
    def render_end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time at which the render completed. 



### #render_start_time
    
    
    def render_start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time at which the render began. 



### #render_state
    
    
    def render_state() -> ::Google::Cloud::Deploy::V1::Release::RenderState

**Returns**

  * ([::Google::Cloud::Deploy::V1::Release::RenderState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Release-RenderState)) — Output only. Current state of the render operation. 



### #skaffold_config_path
    
    
    def skaffold_config_path() -> ::String

**Returns**

  * (::String) — Optional. Filepath of the Skaffold config inside of the config URI. 



### #skaffold_config_path=
    
    
    def skaffold_config_path=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Filepath of the Skaffold config inside of the config URI. 



**Returns**

  * (::String) — Optional. Filepath of the Skaffold config inside of the config URI. 



### #skaffold_config_uri
    
    
    def skaffold_config_uri() -> ::String

**Returns**

  * (::String) — Optional. Cloud Storage URI of tar.gz archive containing Skaffold configuration. 



### #skaffold_config_uri=
    
    
    def skaffold_config_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Cloud Storage URI of tar.gz archive containing Skaffold configuration. 



**Returns**

  * (::String) — Optional. Cloud Storage URI of tar.gz archive containing Skaffold configuration. 



### #skaffold_version
    
    
    def skaffold_version() -> ::String

**Returns**

  * (::String) — Optional. The Skaffold version to use when operating on this release, such as "1.20.0". Not all versions are valid; Cloud Deploy supports a specific set of versions.

If unset, the most recent supported Skaffold version will be used. 




### #skaffold_version=
    
    
    def skaffold_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The Skaffold version to use when operating on this release, such as "1.20.0". Not all versions are valid; Cloud Deploy supports a specific set of versions.

If unset, the most recent supported Skaffold version will be used. 




**Returns**

  * (::String) — Optional. The Skaffold version to use when operating on this release, such as "1.20.0". Not all versions are valid; Cloud Deploy supports a specific set of versions.

If unset, the most recent supported Skaffold version will be used. 




### #target_artifacts
    
    
    def target_artifacts() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Deploy::V1::TargetArtifact}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Deploy::V1::TargetArtifact}) — Output only. Map from target ID to the target artifacts created during the render operation. 



### #target_renders
    
    
    def target_renders() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Deploy::V1::Release::TargetRender}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Deploy::V1::Release::TargetRender}) — Output only. Map from target ID to details of the render operation for that target. 



### #target_snapshots
    
    
    def target_snapshots() -> ::Array<::Google::Cloud::Deploy::V1::Target>

**Returns**

  * (::Array<[::Google::Cloud::Deploy::V1::Target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Target)>) — Output only. Snapshot of the targets taken at release creation time. 



### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. Unique identifier of the `Release`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
