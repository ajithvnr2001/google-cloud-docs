---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-PluginInstance/
title: API hub V1 API - Class Google::Cloud::ApiHub::V1::PluginInstance (v1.0.3) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:43.443074+00:00
---

# API hub V1 API - Class Google::Cloud::ApiHub::V1::PluginInstance (v1.0.3)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-PluginInstance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API hub V1 API - Class Google::Cloud::ApiHub::V1::PluginInstance (v1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.2  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the API hub V1 API class Google::Cloud::ApiHub::V1::PluginInstance.

Represents a plugin instance resource in the API Hub. A PluginInstance is a specific instance of a hub plugin with its own configuration, state, and execution details.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #actions
    
    
    def actions() -> ::Array<::Google::Cloud::ApiHub::V1::PluginInstanceAction>

**Returns**

  * (::Array<[::Google::Cloud::ApiHub::V1::PluginInstanceAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-PluginInstanceAction)>) — Required. The action status for the plugin instance. 



### #actions=
    
    
    def actions=(value) -> ::Array<::Google::Cloud::ApiHub::V1::PluginInstanceAction>

**Parameter**

  * **value** (::Array<[::Google::Cloud::ApiHub::V1::PluginInstanceAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-PluginInstanceAction)>) — Required. The action status for the plugin instance. 



**Returns**

  * (::Array<[::Google::Cloud::ApiHub::V1::PluginInstanceAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-PluginInstanceAction)>) — Required. The action status for the plugin instance. 



### #additional_config
    
    
    def additional_config() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::ApiHub::V1::ConfigVariable}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::ApiHub::V1::ConfigVariable}) — Optional. The additional information for this plugin instance corresponding to the additional config template of the plugin. This information will be sent to plugin hosting service on each call to plugin hosted service. The key will be the config_variable_template.display_name to uniquely identify the config variable. 



### #additional_config=
    
    
    def additional_config=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::ApiHub::V1::ConfigVariable}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::ApiHub::V1::ConfigVariable}) — Optional. The additional information for this plugin instance corresponding to the additional config template of the plugin. This information will be sent to plugin hosting service on each call to plugin hosted service. The key will be the config_variable_template.display_name to uniquely identify the config variable. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::ApiHub::V1::ConfigVariable}) — Optional. The additional information for this plugin instance corresponding to the additional config template of the plugin. This information will be sent to plugin hosting service on each call to plugin hosted service. The key will be the config_variable_template.display_name to uniquely identify the config variable. 



### #auth_config
    
    
    def auth_config() -> ::Google::Cloud::ApiHub::V1::AuthConfig

**Returns**

  * ([::Google::Cloud::ApiHub::V1::AuthConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-AuthConfig)) — Optional. The authentication information for this plugin instance. 



### #auth_config=
    
    
    def auth_config=(value) -> ::Google::Cloud::ApiHub::V1::AuthConfig

**Parameter**

  * **value** ([::Google::Cloud::ApiHub::V1::AuthConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-AuthConfig)) — Optional. The authentication information for this plugin instance. 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::AuthConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-AuthConfig)) — Optional. The authentication information for this plugin instance. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp indicating when the plugin instance was created. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Required. The display name for this plugin instance. Max length is 255 characters. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The display name for this plugin instance. Max length is 255 characters. 



**Returns**

  * (::String) — Required. The display name for this plugin instance. Max length is 255 characters. 



### #error_message
    
    
    def error_message() -> ::String

**Returns**

  * (::String) — Output only. Error message describing the failure, if any, during Create, Delete or ApplyConfig operation corresponding to the plugin instance.This field will only be populated if the plugin instance is in the ERROR or FAILED state. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. The unique name of the plugin instance resource. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The unique name of the plugin instance resource. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`



**Returns**

  * (::String) — Identifier. The unique name of the plugin instance resource. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`



### #source_project_id
    
    
    def source_project_id() -> ::String

**Returns**

  * (::String) — Optional. The source project id of the plugin instance. This will be the id of runtime project in case of gcp based plugins and org id in case of non gcp based plugins. This field will be a required field for Google provided on-ramp plugins. 



### #source_project_id=
    
    
    def source_project_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The source project id of the plugin instance. This will be the id of runtime project in case of gcp based plugins and org id in case of non gcp based plugins. This field will be a required field for Google provided on-ramp plugins. 



**Returns**

  * (::String) — Optional. The source project id of the plugin instance. This will be the id of runtime project in case of gcp based plugins and org id in case of non gcp based plugins. This field will be a required field for Google provided on-ramp plugins. 



### #state
    
    
    def state() -> ::Google::Cloud::ApiHub::V1::PluginInstance::State

**Returns**

  * ([::Google::Cloud::ApiHub::V1::PluginInstance::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-PluginInstance-State)) — Output only. The current state of the plugin instance (e.g., enabled, disabled, provisioning). 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp indicating when the plugin instance was last updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
