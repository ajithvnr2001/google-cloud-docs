---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplatesService-Client/
title: Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:37.153346+00:00
---

# Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplatesService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API class Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client.

Client for the FlexTemplatesService service.

Provides a service for Flex templates.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the FlexTemplatesService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplatesService-Client-Configuration "Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplatesService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplatesService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all FlexTemplatesService clients
    ::Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the FlexTemplatesService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplatesService-Client#Google__Cloud__Dataflow__V1beta3__FlexTemplatesService__Client_configure_class_ "Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplatesService-Client-Configuration "Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplatesService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplatesService-Client-Configuration)) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new FlexTemplatesService client object.

**Yields**

  * (config) — Configure the FlexTemplatesService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplatesService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplatesService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client.new do |config|
      config.timeout = 10.0
    end

### #launch_flex_template
    
    
    def launch_flex_template(request, options = nil) -> ::Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateResponse
    def launch_flex_template(project_id: nil, launch_parameter: nil, location: nil, validate_only: nil) -> ::Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateResponse

Launch a job with a FlexTemplate.

**Overloads**
    
    
    def launch_flex_template(request, options = nil) -> ::Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateResponse

Pass arguments to `launch_flex_template` via a request object, either of type [LaunchFlexTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-LaunchFlexTemplateRequest "Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-LaunchFlexTemplateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def launch_flex_template(project_id: nil, launch_parameter: nil, location: nil, validate_only: nil) -> ::Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateResponse

Pass arguments to `launch_flex_template` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **project_id** (::String) — Required. The ID of the Cloud Platform project that the job belongs to. 
  * **launch_parameter** ([::Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateParameter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-LaunchFlexTemplateParameter), ::Hash) — Required. Parameter to launch a job form Flex Template. 
  * **location** (::String) — Required. The [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) to which to direct the request. E.g., us-central1, us-west1. 
  * **validate_only** (::Boolean) — If true, the request is validated but not actually executed. Defaults to false. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-LaunchFlexTemplateResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-LaunchFlexTemplateResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataflow/v1beta3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateRequest.new
    
    # Call the launch_flex_template method.
    result = client.launch_flex_template request
    
    # The returned object is of type Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateResponse.
    p result

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
