---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Rest-Client/
title: Security Command Center Management V1 API - Class Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:50.410727+00:00
---

# Security Command Center Management V1 API - Class Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Security Command Center Management V1 API - Class Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Security Command Center Management V1 API class Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.

REST client for the SecurityCenterManagement service.

Service describing handlers for resources

## Inherits

  * Object 



## Includes

  * [Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the SecurityCenterManagement Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Rest-Client-Configuration "Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all SecurityCenterManagement clients
    ::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the SecurityCenterManagement Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Rest-Client#Google__Cloud__SecurityCenterManagement__V1__SecurityCenterManagement__Rest__Client_configure_class_ "Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Rest-Client-Configuration "Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Rest-Client-Configuration)) 



### #create_event_threat_detection_custom_module
    
    
    def create_event_threat_detection_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule
    def create_event_threat_detection_custom_module(parent: nil, event_threat_detection_custom_module: nil, validate_only: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule

Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.

**Overloads**
    
    
    def create_event_threat_detection_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule

Pass arguments to `create_event_threat_detection_custom_module` via a request object, either of type [CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-CreateEventThreatDetectionCustomModuleRequest "Google::Cloud::SecurityCenterManagement::V1::CreateEventThreatDetectionCustomModuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-CreateEventThreatDetectionCustomModuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_event_threat_detection_custom_module(parent: nil, event_threat_detection_custom_module: nil, validate_only: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule

Pass arguments to `create_event_threat_detection_custom_module` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Name of parent for the module, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `projects/{project}/locations/{location}`
  * **event_threat_detection_custom_module** ([::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule), ::Hash) — Required. The module to create. The [EventThreatDetectionCustomModule.name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule#Google__Cloud__SecurityCenterManagement__V1__EventThreatDetectionCustomModule_name_instance_ "Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule#name \(method\)") field is ignored; Security Command Center generates the name. 
  * **validate_only** (::Boolean) — Optional. When set to `true`, the request will be validated (including IAM checks), but no module will be created. An `OK` response indicates that the request is valid, while an error response indicates that the request is invalid.

If the request is valid, a subsequent request to create the module could still fail for one of the following reasons:

    * The state of your cloud resources changed; for example, you lost a required IAM permission
    * An error occurred during creation of the module

Defaults to `false`. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::CreateEventThreatDetectionCustomModuleRequest.new
    
    # Call the create_event_threat_detection_custom_module method.
    result = client.create_event_threat_detection_custom_module request
    
    # The returned object is of type Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule.
    p result

### #create_security_health_analytics_custom_module
    
    
    def create_security_health_analytics_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule
    def create_security_health_analytics_custom_module(parent: nil, security_health_analytics_custom_module: nil, validate_only: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule

Creates a resident [SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule "Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule \(class\)") at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default.

**Overloads**
    
    
    def create_security_health_analytics_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule

Pass arguments to `create_security_health_analytics_custom_module` via a request object, either of type [CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-CreateSecurityHealthAnalyticsCustomModuleRequest "Google::Cloud::SecurityCenterManagement::V1::CreateSecurityHealthAnalyticsCustomModuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-CreateSecurityHealthAnalyticsCustomModuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_security_health_analytics_custom_module(parent: nil, security_health_analytics_custom_module: nil, validate_only: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule

Pass arguments to `create_security_health_analytics_custom_module` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Name of the parent organization, folder, or project of the module, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `projects/{project}/locations/{location}`
  * **security_health_analytics_custom_module** ([::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule), ::Hash) — Required. The resource being created. 
  * **validate_only** (::Boolean) — Optional. When set to `true`, the request will be validated (including IAM checks), but no module will be created. An `OK` response indicates that the request is valid, while an error response indicates that the request is invalid.

If the request is valid, a subsequent request to create the module could still fail for one of the following reasons:

    * The state of your cloud resources changed; for example, you lost a required IAM permission
    * An error occurred during creation of the module

Defaults to `false`. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::CreateSecurityHealthAnalyticsCustomModuleRequest.new
    
    # Call the create_security_health_analytics_custom_module method.
    result = client.create_security_health_analytics_custom_module request
    
    # The returned object is of type Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule.
    p result

### #delete_event_threat_detection_custom_module
    
    
    def delete_event_threat_detection_custom_module(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_event_threat_detection_custom_module(name: nil, validate_only: nil) -> ::Google::Protobuf::Empty

Deletes the specified Event Threat Detection custom module and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

**Overloads**
    
    
    def delete_event_threat_detection_custom_module(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_event_threat_detection_custom_module` via a request object, either of type [DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-DeleteEventThreatDetectionCustomModuleRequest "Google::Cloud::SecurityCenterManagement::V1::DeleteEventThreatDetectionCustomModuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-DeleteEventThreatDetectionCustomModuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_event_threat_detection_custom_module(name: nil, validate_only: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_event_threat_detection_custom_module` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — 

Required. The resource name of the Event Threat Detection custom module, in one of the following formats:

    * `organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
    * `folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
    * `projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
  * **validate_only** (::Boolean) — Optional. When set to `true`, the request will be validated (including IAM checks), but no module will be deleted. An `OK` response indicates that the request is valid, while an error response indicates that the request is invalid.

If the request is valid, a subsequent request to delete the module could still fail for one of the following reasons:

    * The state of your cloud resources changed; for example, you lost a required IAM permission
    * An error occurred during creation of the module

Defaults to `false`. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::DeleteEventThreatDetectionCustomModuleRequest.new
    
    # Call the delete_event_threat_detection_custom_module method.
    result = client.delete_event_threat_detection_custom_module request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_security_health_analytics_custom_module
    
    
    def delete_security_health_analytics_custom_module(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_security_health_analytics_custom_module(name: nil, validate_only: nil) -> ::Google::Protobuf::Empty

Deletes the specified [SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule "Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule \(class\)") and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

**Overloads**
    
    
    def delete_security_health_analytics_custom_module(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_security_health_analytics_custom_module` via a request object, either of type [DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-DeleteSecurityHealthAnalyticsCustomModuleRequest "Google::Cloud::SecurityCenterManagement::V1::DeleteSecurityHealthAnalyticsCustomModuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-DeleteSecurityHealthAnalyticsCustomModuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_security_health_analytics_custom_module(name: nil, validate_only: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_security_health_analytics_custom_module` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — 

Required. The resource name of the SHA custom module, in one of the following formats:

    * `organizations/{organization}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}`
    * `folders/{folder}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}`
    * `projects/{project}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}`
  * **validate_only** (::Boolean) — Optional. When set to `true`, the request will be validated (including IAM checks), but no module will be deleted. An `OK` response indicates that the request is valid, while an error response indicates that the request is invalid.

If the request is valid, a subsequent request to delete the module could still fail for one of the following reasons:

    * The state of your cloud resources changed; for example, you lost a required IAM permission
    * An error occurred during deletion of the module

Defaults to `false`. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::DeleteSecurityHealthAnalyticsCustomModuleRequest.new
    
    # Call the delete_security_health_analytics_custom_module method.
    result = client.delete_security_health_analytics_custom_module request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_effective_event_threat_detection_custom_module
    
    
    def get_effective_event_threat_detection_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule
    def get_effective_event_threat_detection_custom_module(name: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule

Gets the effective Event Threat Detection custom module at the given level.

The difference between an [EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EffectiveEventThreatDetectionCustomModule "Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule \(class\)") and an [EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule "Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule \(class\)") is that the fields for an `EffectiveEventThreatDetectionCustomModule` are computed from ancestors if needed. For example, the enablement state for an `EventThreatDetectionCustomModule` can be `ENABLED`, `DISABLED`, or `INHERITED`. In contrast, the enablement state for an `EffectiveEventThreatDetectionCustomModule` is always computed as `ENABLED` or `DISABLED`.

**Overloads**
    
    
    def get_effective_event_threat_detection_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule

Pass arguments to `get_effective_event_threat_detection_custom_module` via a request object, either of type [GetEffectiveEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-GetEffectiveEventThreatDetectionCustomModuleRequest "Google::Cloud::SecurityCenterManagement::V1::GetEffectiveEventThreatDetectionCustomModuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::GetEffectiveEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-GetEffectiveEventThreatDetectionCustomModuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_effective_event_threat_detection_custom_module(name: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule

Pass arguments to `get_effective_event_threat_detection_custom_module` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. The resource name of the Event Threat Detection custom module, in one of the following formats:

    * `organizations/{organization}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}`
    * `folders/{folder}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}`
    * `projects/{project}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EffectiveEventThreatDetectionCustomModule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EffectiveEventThreatDetectionCustomModule)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::GetEffectiveEventThreatDetectionCustomModuleRequest.new
    
    # Call the get_effective_event_threat_detection_custom_module method.
    result = client.get_effective_event_threat_detection_custom_module request
    
    # The returned object is of type Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule.
    p result

### #get_effective_security_health_analytics_custom_module
    
    
    def get_effective_security_health_analytics_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule
    def get_effective_security_health_analytics_custom_module(name: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule

Gets details of a single [EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EffectiveSecurityHealthAnalyticsCustomModule "Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule \(class\)").

**Overloads**
    
    
    def get_effective_security_health_analytics_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule

Pass arguments to `get_effective_security_health_analytics_custom_module` via a request object, either of type [GetEffectiveSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-GetEffectiveSecurityHealthAnalyticsCustomModuleRequest "Google::Cloud::SecurityCenterManagement::V1::GetEffectiveSecurityHealthAnalyticsCustomModuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::GetEffectiveSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-GetEffectiveSecurityHealthAnalyticsCustomModuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_effective_security_health_analytics_custom_module(name: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule

Pass arguments to `get_effective_security_health_analytics_custom_module` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. The full resource name of the custom module, specified in one of the following formats:

    * `organizations/organization/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}`
    * `folders/folder/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}`
    * `projects/project/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EffectiveSecurityHealthAnalyticsCustomModule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EffectiveSecurityHealthAnalyticsCustomModule)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::GetEffectiveSecurityHealthAnalyticsCustomModuleRequest.new
    
    # Call the get_effective_security_health_analytics_custom_module method.
    result = client.get_effective_security_health_analytics_custom_module request
    
    # The returned object is of type Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule.
    p result

### #get_event_threat_detection_custom_module
    
    
    def get_event_threat_detection_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule
    def get_event_threat_detection_custom_module(name: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule

Gets an Event Threat Detection custom module.

**Overloads**
    
    
    def get_event_threat_detection_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule

Pass arguments to `get_event_threat_detection_custom_module` via a request object, either of type [GetEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-GetEventThreatDetectionCustomModuleRequest "Google::Cloud::SecurityCenterManagement::V1::GetEventThreatDetectionCustomModuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::GetEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-GetEventThreatDetectionCustomModuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_event_threat_detection_custom_module(name: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule

Pass arguments to `get_event_threat_detection_custom_module` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. The resource name of the Event Threat Detection custom module, in one of the following formats:

    * `organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
    * `folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
    * `projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::GetEventThreatDetectionCustomModuleRequest.new
    
    # Call the get_event_threat_detection_custom_module method.
    result = client.get_event_threat_detection_custom_module request
    
    # The returned object is of type Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule.
    p result

### #get_security_center_service
    
    
    def get_security_center_service(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService
    def get_security_center_service(name: nil, show_eligible_modules_only: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService

Gets service settings for the specified Security Command Center service.

**Overloads**
    
    
    def get_security_center_service(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService

Pass arguments to `get_security_center_service` via a request object, either of type [GetSecurityCenterServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-GetSecurityCenterServiceRequest "Google::Cloud::SecurityCenterManagement::V1::GetSecurityCenterServiceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::GetSecurityCenterServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-GetSecurityCenterServiceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_security_center_service(name: nil, show_eligible_modules_only: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService

Pass arguments to `get_security_center_service` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — 

Required. The Security Command Center service to retrieve, in one of the following formats:

    * organizations/{organization}/locations/{location}/securityCenterServices/{service}
    * folders/{folder}/locations/{location}/securityCenterServices/{service}
    * projects/{project}/locations/{location}/securityCenterServices/{service}

The following values are valid for `{service}`:

    * `container-threat-detection`
    * `event-threat-detection`
    * `security-health-analytics`
    * `vm-threat-detection`
    * `web-security-scanner`
  * **show_eligible_modules_only** (::Boolean) — Set to `true` to show only modules that are in scope. By default, all modules are shown. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterService)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterService)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::GetSecurityCenterServiceRequest.new
    
    # Call the get_security_center_service method.
    result = client.get_security_center_service request
    
    # The returned object is of type Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService.
    p result

### #get_security_health_analytics_custom_module
    
    
    def get_security_health_analytics_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule
    def get_security_health_analytics_custom_module(name: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule

Retrieves a [SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule "Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule \(class\)").

**Overloads**
    
    
    def get_security_health_analytics_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule

Pass arguments to `get_security_health_analytics_custom_module` via a request object, either of type [GetSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-GetSecurityHealthAnalyticsCustomModuleRequest "Google::Cloud::SecurityCenterManagement::V1::GetSecurityHealthAnalyticsCustomModuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::GetSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-GetSecurityHealthAnalyticsCustomModuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_security_health_analytics_custom_module(name: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule

Pass arguments to `get_security_health_analytics_custom_module` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource, in the format `projects/{project}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::GetSecurityHealthAnalyticsCustomModuleRequest.new
    
    # Call the get_security_health_analytics_custom_module method.
    result = client.get_security_health_analytics_custom_module request
    
    # The returned object is of type Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new SecurityCenterManagement REST client object.

**Yields**

  * (config) — Configure the SecurityCenterManagement client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_descendant_event_threat_detection_custom_modules
    
    
    def list_descendant_event_threat_detection_custom_modules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule>
    def list_descendant_event_threat_detection_custom_modules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule>

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.

**Overloads**
    
    
    def list_descendant_event_threat_detection_custom_modules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule>

Pass arguments to `list_descendant_event_threat_detection_custom_modules` via a request object, either of type [ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListDescendantEventThreatDetectionCustomModulesRequest "Google::Cloud::SecurityCenterManagement::V1::ListDescendantEventThreatDetectionCustomModulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListDescendantEventThreatDetectionCustomModulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_descendant_event_threat_detection_custom_modules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule>

Pass arguments to `list_descendant_event_threat_detection_custom_modules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Name of parent to list custom modules, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `projects/{project}/locations/{location}`
  * **page_size** (::Integer) — Optional. The maximum number of modules to return. The service may return fewer than this value. If unspecified, at most 10 configs will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. A pagination token returned from a previous request. Provide this token to retrieve the next page of results.

When paginating, the rest of the request must match the request that generated the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::ListDescendantEventThreatDetectionCustomModulesRequest.new
    
    # Call the list_descendant_event_threat_detection_custom_modules method.
    result = client.list_descendant_event_threat_detection_custom_modules request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule.
      p item
    end

### #list_descendant_security_health_analytics_custom_modules
    
    
    def list_descendant_security_health_analytics_custom_modules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule>
    def list_descendant_security_health_analytics_custom_modules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule>

Returns a list of all resident [SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule "Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule \(class\)") resources under the given organization, folder, or project and all of its descendants.

**Overloads**
    
    
    def list_descendant_security_health_analytics_custom_modules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule>

Pass arguments to `list_descendant_security_health_analytics_custom_modules` via a request object, either of type [ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListDescendantSecurityHealthAnalyticsCustomModulesRequest "Google::Cloud::SecurityCenterManagement::V1::ListDescendantSecurityHealthAnalyticsCustomModulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListDescendantSecurityHealthAnalyticsCustomModulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_descendant_security_health_analytics_custom_modules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule>

Pass arguments to `list_descendant_security_health_analytics_custom_modules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Name of the parent organization, folder, or project in which to list custom modules, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `projects/{project}/locations/{location}`
  * **page_size** (::Integer) — Optional. The maximum number of results to return in a single response. Default is 10, minimum is 1, maximum is 1000. 
  * **page_token** (::String) — Optional. A pagination token returned from a previous request. Provide this token to retrieve the next page of results.

When paginating, the rest of the request must match the request that generated the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::ListDescendantSecurityHealthAnalyticsCustomModulesRequest.new
    
    # Call the list_descendant_security_health_analytics_custom_modules method.
    result = client.list_descendant_security_health_analytics_custom_modules request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule.
      p item
    end

### #list_effective_event_threat_detection_custom_modules
    
    
    def list_effective_event_threat_detection_custom_modules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule>
    def list_effective_event_threat_detection_custom_modules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule>

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

**Overloads**
    
    
    def list_effective_event_threat_detection_custom_modules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule>

Pass arguments to `list_effective_event_threat_detection_custom_modules` via a request object, either of type [ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListEffectiveEventThreatDetectionCustomModulesRequest "Google::Cloud::SecurityCenterManagement::V1::ListEffectiveEventThreatDetectionCustomModulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListEffectiveEventThreatDetectionCustomModulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_effective_event_threat_detection_custom_modules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule>

Pass arguments to `list_effective_event_threat_detection_custom_modules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Name of parent to list effective custom modules, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `projects/{project}/locations/{location}`
  * **page_size** (::Integer) — Optional. The maximum number of results to return in a single response. Default is 10, minimum is 1, maximum is 1000. 
  * **page_token** (::String) — Optional. A pagination token returned from a previous request. Provide this token to retrieve the next page of results.

When paginating, the rest of the request must match the request that generated the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EffectiveEventThreatDetectionCustomModule)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EffectiveEventThreatDetectionCustomModule)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::ListEffectiveEventThreatDetectionCustomModulesRequest.new
    
    # Call the list_effective_event_threat_detection_custom_modules method.
    result = client.list_effective_event_threat_detection_custom_modules request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::SecurityCenterManagement::V1::EffectiveEventThreatDetectionCustomModule.
      p item
    end

### #list_effective_security_health_analytics_custom_modules
    
    
    def list_effective_security_health_analytics_custom_modules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule>
    def list_effective_security_health_analytics_custom_modules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule>

Returns a list of all [EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EffectiveSecurityHealthAnalyticsCustomModule "Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule \(class\)") resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

**Overloads**
    
    
    def list_effective_security_health_analytics_custom_modules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule>

Pass arguments to `list_effective_security_health_analytics_custom_modules` via a request object, either of type [ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListEffectiveSecurityHealthAnalyticsCustomModulesRequest "Google::Cloud::SecurityCenterManagement::V1::ListEffectiveSecurityHealthAnalyticsCustomModulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListEffectiveSecurityHealthAnalyticsCustomModulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_effective_security_health_analytics_custom_modules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule>

Pass arguments to `list_effective_security_health_analytics_custom_modules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Name of parent to list effective custom modules, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `projects/{project}/locations/{location}`
  * **page_size** (::Integer) — Optional. The maximum number of results to return in a single response. Default is 10, minimum is 1, maximum is 1000. 
  * **page_token** (::String) — Optional. A pagination token returned from a previous request. Provide this token to retrieve the next page of results.

When paginating, the rest of the request must match the request that generated the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EffectiveSecurityHealthAnalyticsCustomModule)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EffectiveSecurityHealthAnalyticsCustomModule)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::ListEffectiveSecurityHealthAnalyticsCustomModulesRequest.new
    
    # Call the list_effective_security_health_analytics_custom_modules method.
    result = client.list_effective_security_health_analytics_custom_modules request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::SecurityCenterManagement::V1::EffectiveSecurityHealthAnalyticsCustomModule.
      p item
    end

### #list_event_threat_detection_custom_modules
    
    
    def list_event_threat_detection_custom_modules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule>
    def list_event_threat_detection_custom_modules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule>

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.

**Overloads**
    
    
    def list_event_threat_detection_custom_modules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule>

Pass arguments to `list_event_threat_detection_custom_modules` via a request object, either of type [ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListEventThreatDetectionCustomModulesRequest "Google::Cloud::SecurityCenterManagement::V1::ListEventThreatDetectionCustomModulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListEventThreatDetectionCustomModulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_event_threat_detection_custom_modules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule>

Pass arguments to `list_event_threat_detection_custom_modules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Name of parent to list custom modules, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `projects/{project}/locations/{location}`
  * **page_size** (::Integer) — Optional. The maximum number of modules to return. The service may return fewer than this value. If unspecified, at most 10 modules will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. A pagination token returned from a previous request. Provide this token to retrieve the next page of results.

When paginating, the rest of the request must match the request that generated the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::ListEventThreatDetectionCustomModulesRequest.new
    
    # Call the list_event_threat_detection_custom_modules method.
    result = client.list_event_threat_detection_custom_modules request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule.
      p item
    end

### #list_security_center_services
    
    
    def list_security_center_services(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService>
    def list_security_center_services(parent: nil, page_size: nil, page_token: nil, show_eligible_modules_only: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService>

Returns a list of all Security Command Center services for the given parent.

**Overloads**
    
    
    def list_security_center_services(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService>

Pass arguments to `list_security_center_services` via a request object, either of type [ListSecurityCenterServicesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListSecurityCenterServicesRequest "Google::Cloud::SecurityCenterManagement::V1::ListSecurityCenterServicesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::ListSecurityCenterServicesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListSecurityCenterServicesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_security_center_services(parent: nil, page_size: nil, page_token: nil, show_eligible_modules_only: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService>

Pass arguments to `list_security_center_services` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. The name of the parent to list Security Command Center services, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `projects/{project}/locations/{location}`
  * **page_size** (::Integer) — Optional. The maximum number of results to return in a single response. Default is 10, minimum is 1, maximum is 1000. 
  * **page_token** (::String) — Optional. A pagination token returned from a previous request. Provide this token to retrieve the next page of results.

When paginating, the rest of the request must match the request that generated the page token. 

  * **show_eligible_modules_only** (::Boolean) — Flag that, when set, is used to filter the module settings that are shown. The default setting is that all modules are shown. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterService)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterService)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::ListSecurityCenterServicesRequest.new
    
    # Call the list_security_center_services method.
    result = client.list_security_center_services request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService.
      p item
    end

### #list_security_health_analytics_custom_modules
    
    
    def list_security_health_analytics_custom_modules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule>
    def list_security_health_analytics_custom_modules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule>

Returns a list of all [SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule "Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule \(class\)") resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

**Overloads**
    
    
    def list_security_health_analytics_custom_modules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule>

Pass arguments to `list_security_health_analytics_custom_modules` via a request object, either of type [ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListSecurityHealthAnalyticsCustomModulesRequest "Google::Cloud::SecurityCenterManagement::V1::ListSecurityHealthAnalyticsCustomModulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListSecurityHealthAnalyticsCustomModulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_security_health_analytics_custom_modules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule>

Pass arguments to `list_security_health_analytics_custom_modules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Name of the parent organization, folder, or project in which to list custom modules, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `projects/{project}/locations/{location}`
  * **page_size** (::Integer) — Optional. The maximum number of results to return in a single response. Default is 10, minimum is 1, maximum is 1000. 
  * **page_token** (::String) — Optional. A pagination token returned from a previous request. Provide this token to retrieve the next page of results.

When paginating, the rest of the request must match the request that generated the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::ListSecurityHealthAnalyticsCustomModulesRequest.new
    
    # Call the list_security_health_analytics_custom_modules method.
    result = client.list_security_health_analytics_custom_modules request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule.
      p item
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Rest::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Rest::Client) 



### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #simulate_security_health_analytics_custom_module
    
    
    def simulate_security_health_analytics_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SimulateSecurityHealthAnalyticsCustomModuleResponse
    def simulate_security_health_analytics_custom_module(parent: nil, custom_config: nil, resource: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SimulateSecurityHealthAnalyticsCustomModuleResponse

Simulates the result of using a [SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule "Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule \(class\)") to check a resource.

**Overloads**
    
    
    def simulate_security_health_analytics_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SimulateSecurityHealthAnalyticsCustomModuleResponse

Pass arguments to `simulate_security_health_analytics_custom_module` via a request object, either of type [Google::Cloud::SecurityCenterManagement::V1::SimulateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SimulateSecurityHealthAnalyticsCustomModuleRequest "Google::Cloud::SecurityCenterManagement::V1::SimulateSecurityHealthAnalyticsCustomModuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::SimulateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SimulateSecurityHealthAnalyticsCustomModuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def simulate_security_health_analytics_custom_module(parent: nil, custom_config: nil, resource: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SimulateSecurityHealthAnalyticsCustomModuleResponse

Pass arguments to `simulate_security_health_analytics_custom_module` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The relative resource name of the organization, project, or folder. For more information about relative resource names, see [AIP-122: Resource names](https://google.aip.dev/122). Example: `organizations/{organization_id}`. 
  * **custom_config** ([::Google::Cloud::SecurityCenterManagement::V1::CustomConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-CustomConfig), ::Hash) — Required. The custom configuration that you need to test. 
  * **resource** ([::Google::Cloud::SecurityCenterManagement::V1::SimulateSecurityHealthAnalyticsCustomModuleRequest::SimulatedResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SimulateSecurityHealthAnalyticsCustomModuleRequest-SimulatedResource), ::Hash) — Required. Resource data to simulate custom module against. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenterManagement::V1::SimulateSecurityHealthAnalyticsCustomModuleResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SimulateSecurityHealthAnalyticsCustomModuleResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenterManagement::V1::SimulateSecurityHealthAnalyticsCustomModuleResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SimulateSecurityHealthAnalyticsCustomModuleResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::SimulateSecurityHealthAnalyticsCustomModuleRequest.new
    
    # Call the simulate_security_health_analytics_custom_module method.
    result = client.simulate_security_health_analytics_custom_module request
    
    # The returned object is of type Google::Cloud::SecurityCenterManagement::V1::SimulateSecurityHealthAnalyticsCustomModuleResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_event_threat_detection_custom_module
    
    
    def update_event_threat_detection_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule
    def update_event_threat_detection_custom_module(update_mask: nil, event_threat_detection_custom_module: nil, validate_only: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule

Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed.

**Overloads**
    
    
    def update_event_threat_detection_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule

Pass arguments to `update_event_threat_detection_custom_module` via a request object, either of type [UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-UpdateEventThreatDetectionCustomModuleRequest "Google::Cloud::SecurityCenterManagement::V1::UpdateEventThreatDetectionCustomModuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-UpdateEventThreatDetectionCustomModuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_event_threat_detection_custom_module(update_mask: nil, event_threat_detection_custom_module: nil, validate_only: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule

Pass arguments to `update_event_threat_detection_custom_module` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The fields to update. If omitted, then all fields are updated. 
  * **event_threat_detection_custom_module** ([::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule), ::Hash) — Required. The module being updated. 
  * **validate_only** (::Boolean) — Optional. When set to `true`, the request will be validated (including IAM checks), but no module will be updated. An `OK` response indicates that the request is valid, while an error response indicates that the request is invalid.

If the request is valid, a subsequent request to update the module could still fail for one of the following reasons:

    * The state of your cloud resources changed; for example, you lost a required IAM permission
    * An error occurred during creation of the module

Defaults to `false`. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-EventThreatDetectionCustomModule)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::UpdateEventThreatDetectionCustomModuleRequest.new
    
    # Call the update_event_threat_detection_custom_module method.
    result = client.update_event_threat_detection_custom_module request
    
    # The returned object is of type Google::Cloud::SecurityCenterManagement::V1::EventThreatDetectionCustomModule.
    p result

### #update_security_center_service
    
    
    def update_security_center_service(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService
    def update_security_center_service(security_center_service: nil, update_mask: nil, validate_only: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService

Updates a Security Command Center service using the given update mask.

**Overloads**
    
    
    def update_security_center_service(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService

Pass arguments to `update_security_center_service` via a request object, either of type [UpdateSecurityCenterServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-UpdateSecurityCenterServiceRequest "Google::Cloud::SecurityCenterManagement::V1::UpdateSecurityCenterServiceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::UpdateSecurityCenterServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-UpdateSecurityCenterServiceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_security_center_service(security_center_service: nil, update_mask: nil, validate_only: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService

Pass arguments to `update_security_center_service` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **security_center_service** ([::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterService), ::Hash) — Required. The updated service. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The fields to update. Accepts the following values:

    * `intended_enablement_state`
    * `modules`

If omitted, then all eligible fields are updated. 

  * **validate_only** (::Boolean) — Optional. When set to `true`, the request will be validated (including IAM checks), but no service will be updated. An `OK` response indicates that the request is valid, while an error response indicates that the request is invalid.

If the request is valid, a subsequent request to update the service could still fail for one of the following reasons:

    * The state of your cloud resources changed; for example, you lost a required IAM permission
    * An error occurred during update of the service

Defaults to `false`. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterService)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterService)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::UpdateSecurityCenterServiceRequest.new
    
    # Call the update_security_center_service method.
    result = client.update_security_center_service request
    
    # The returned object is of type Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService.
    p result

### #update_security_health_analytics_custom_module
    
    
    def update_security_health_analytics_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule
    def update_security_health_analytics_custom_module(update_mask: nil, security_health_analytics_custom_module: nil, validate_only: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule

Updates the [SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule "Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule \(class\)") under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom configuration of a module is supported on resident modules only.

**Overloads**
    
    
    def update_security_health_analytics_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule

Pass arguments to `update_security_health_analytics_custom_module` via a request object, either of type [UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-UpdateSecurityHealthAnalyticsCustomModuleRequest "Google::Cloud::SecurityCenterManagement::V1::UpdateSecurityHealthAnalyticsCustomModuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-UpdateSecurityHealthAnalyticsCustomModuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_security_health_analytics_custom_module(update_mask: nil, security_health_analytics_custom_module: nil, validate_only: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule

Pass arguments to `update_security_health_analytics_custom_module` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The fields to update. The following values are valid:

    * `custom_config`
    * `enablement_state`

If you omit this field or set it to the wildcard value `*`, then all eligible fields are updated. 

  * **security_health_analytics_custom_module** ([::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule), ::Hash) — Required. The resource being updated. 
  * **validate_only** (::Boolean) — Optional. When set to `true`, the request will be validated (including IAM checks), but no module will be updated. An `OK` response indicates that the request is valid, while an error response indicates that the request is invalid.

If the request is valid, a subsequent request to update the module could still fail for one of the following reasons:

    * The state of your cloud resources changed; for example, you lost a required IAM permission
    * An error occurred during creation of the module

Defaults to `false`. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityHealthAnalyticsCustomModule)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::UpdateSecurityHealthAnalyticsCustomModuleRequest.new
    
    # Call the update_security_health_analytics_custom_module method.
    result = client.update_security_health_analytics_custom_module request
    
    # The returned object is of type Google::Cloud::SecurityCenterManagement::V1::SecurityHealthAnalyticsCustomModule.
    p result

### #validate_event_threat_detection_custom_module
    
    
    def validate_event_threat_detection_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::ValidateEventThreatDetectionCustomModuleResponse
    def validate_event_threat_detection_custom_module(parent: nil, raw_text: nil, type: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::ValidateEventThreatDetectionCustomModuleResponse

Validates the given Event Threat Detection custom module.

**Overloads**
    
    
    def validate_event_threat_detection_custom_module(request, options = nil) -> ::Google::Cloud::SecurityCenterManagement::V1::ValidateEventThreatDetectionCustomModuleResponse

Pass arguments to `validate_event_threat_detection_custom_module` via a request object, either of type [ValidateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ValidateEventThreatDetectionCustomModuleRequest "Google::Cloud::SecurityCenterManagement::V1::ValidateEventThreatDetectionCustomModuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::SecurityCenterManagement::V1::ValidateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ValidateEventThreatDetectionCustomModuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def validate_event_threat_detection_custom_module(parent: nil, raw_text: nil, type: nil) -> ::Google::Cloud::SecurityCenterManagement::V1::ValidateEventThreatDetectionCustomModuleResponse

Pass arguments to `validate_event_threat_detection_custom_module` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Resource name of the parent to validate the custom modules under, in one of the following formats:

    * `organizations/{organization}/locations/{location}`
  * **raw_text** (::String) — Required. The raw text of the module's contents. Used to generate error messages. 
  * **type** (::String) — Required. The type of the module. For example, `CONFIGURABLE_BAD_IP`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecurityCenterManagement::V1::ValidateEventThreatDetectionCustomModuleResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ValidateEventThreatDetectionCustomModuleResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecurityCenterManagement::V1::ValidateEventThreatDetectionCustomModuleResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ValidateEventThreatDetectionCustomModuleResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security_center_management/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::SecurityCenterManagement::V1::ValidateEventThreatDetectionCustomModuleRequest.new
    
    # Call the validate_event_threat_detection_custom_module method.
    result = client.validate_event_threat_detection_custom_module request
    
    # The returned object is of type Google::Cloud::SecurityCenterManagement::V1::ValidateEventThreatDetectionCustomModuleResponse.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
