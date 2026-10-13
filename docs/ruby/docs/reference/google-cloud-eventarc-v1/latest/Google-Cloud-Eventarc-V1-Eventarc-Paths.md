---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-Eventarc-Paths/
title: Eventarc V1 API - Module Google::Cloud::Eventarc::V1::Eventarc::Paths (v2.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:47.640107+00:00
---

# Eventarc V1 API - Module Google::Cloud::Eventarc::V1::Eventarc::Paths (v2.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-Eventarc-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Eventarc V1 API - Module Google::Cloud::Eventarc::V1::Eventarc::Paths (v2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.1  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.4 

Reference documentation and code samples for the Eventarc V1 API module Google::Cloud::Eventarc::V1::Eventarc::Paths.

Path helper methods for the Eventarc API.

## Extended By

  * [Google::Cloud::Eventarc::V1::Eventarc::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-Eventarc-Paths)



## Included In

  * [Google::Cloud::Eventarc::V1::Eventarc::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-Eventarc-Client)
  * [Google::Cloud::Eventarc::V1::Eventarc::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-Eventarc-Paths)
  * [Google::Cloud::Eventarc::V1::Eventarc::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-Eventarc-Rest-Client)



## Methods 

### #channel_connection_path
    
    
    def channel_connection_path(project:, location:, channel_connection:) -> ::String

Create a fully-qualified ChannelConnection resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/channelConnections/{channel_connection}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **channel_connection** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #channel_path
    
    
    def channel_path(project:, location:, channel:) -> ::String

Create a fully-qualified Channel resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/channels/{channel}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **channel** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #cloud_function_path
    
    
    def cloud_function_path(project:, location:, function:) -> ::String

Create a fully-qualified CloudFunction resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/functions/{function}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **function** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #crypto_key_path
    
    
    def crypto_key_path(project:, location:, key_ring:, crypto_key:) -> ::String

Create a fully-qualified CryptoKey resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **key_ring** (String) 
  * **crypto_key** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #enrollment_path
    
    
    def enrollment_path(project:, location:, enrollment:) -> ::String

Create a fully-qualified Enrollment resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/enrollments/{enrollment}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **enrollment** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #google_api_source_path
    
    
    def google_api_source_path(project:, location:, google_api_source:) -> ::String

Create a fully-qualified GoogleApiSource resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/googleApiSources/{google_api_source}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **google_api_source** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #google_channel_config_path
    
    
    def google_channel_config_path(project:, location:) -> ::String

Create a fully-qualified GoogleChannelConfig resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/googleChannelConfig`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #message_bus_path
    
    
    def message_bus_path(project:, location:, message_bus:) -> ::String

Create a fully-qualified MessageBus resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/messageBuses/{message_bus}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **message_bus** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #network_attachment_path
    
    
    def network_attachment_path(project:, region:, networkattachment:) -> ::String

Create a fully-qualified NetworkAttachment resource string.

The resource will be in the following format:

`projects/{project}/regions/{region}/networkAttachments/{networkattachment}`

**Parameters**

  * **project** (String) 
  * **region** (String) 
  * **networkattachment** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #pipeline_path
    
    
    def pipeline_path(project:, location:, pipeline:) -> ::String

Create a fully-qualified Pipeline resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/pipelines/{pipeline}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **pipeline** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #provider_path
    
    
    def provider_path(project:, location:, provider:) -> ::String

Create a fully-qualified Provider resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/providers/{provider}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **provider** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #service_account_path
    
    
    def service_account_path(project:, service_account:) -> ::String

Create a fully-qualified ServiceAccount resource string.

The resource will be in the following format:

`projects/{project}/serviceAccounts/{service_account}`

**Parameters**

  * **project** (String) 
  * **service_account** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #topic_path
    
    
    def topic_path(project:, topic:) -> ::String

Create a fully-qualified Topic resource string.

The resource will be in the following format:

`projects/{project}/topics/{topic}`

**Parameters**

  * **project** (String) 
  * **topic** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #trigger_path
    
    
    def trigger_path(project:, location:, trigger:) -> ::String

Create a fully-qualified Trigger resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/triggers/{trigger}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **trigger** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #workflow_path
    
    
    def workflow_path(project:, location:, workflow:) -> ::String

Create a fully-qualified Workflow resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/workflows/{workflow}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **workflow** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
