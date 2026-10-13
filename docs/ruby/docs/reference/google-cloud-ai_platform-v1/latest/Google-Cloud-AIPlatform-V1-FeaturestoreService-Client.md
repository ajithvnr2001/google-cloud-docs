---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::FeaturestoreService::Client (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:01.777942+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::FeaturestoreService::Client (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::FeaturestoreService::Client (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.

Client for the FeaturestoreService service.

The service that handles CRUD and List for resources for Featurestore.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::AIPlatform::V1::FeaturestoreService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the FeaturestoreService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client-Configuration "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all FeaturestoreService clients
    ::Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.configure do |config|
      config.timeout = 10.0
    end

### #batch_create_features
    
    
    def batch_create_features(request, options = nil) -> ::Gapic::Operation
    def batch_create_features(parent: nil, requests: nil) -> ::Gapic::Operation

Creates a batch of Features in a given EntityType.

**Overloads**
    
    
    def batch_create_features(request, options = nil) -> ::Gapic::Operation

Pass arguments to `batch_create_features` via a request object, either of type [BatchCreateFeaturesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchCreateFeaturesRequest "Google::Cloud::AIPlatform::V1::BatchCreateFeaturesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::BatchCreateFeaturesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchCreateFeaturesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def batch_create_features(parent: nil, requests: nil) -> ::Gapic::Operation

Pass arguments to `batch_create_features` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`
  * **requests** (::Array<[::Google::Cloud::AIPlatform::V1::CreateFeatureRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateFeatureRequest), ::Hash>) — Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::BatchCreateFeaturesRequest.new
    
    # Call the batch_create_features method.
    result = client.batch_create_features request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #batch_read_feature_values
    
    
    def batch_read_feature_values(request, options = nil) -> ::Gapic::Operation
    def batch_read_feature_values(csv_read_instances: nil, bigquery_read_instances: nil, featurestore: nil, destination: nil, pass_through_fields: nil, entity_type_specs: nil, start_time: nil) -> ::Gapic::Operation

Batch reads Feature values from a Featurestore.

This API enables batch reading Feature values, where each read instance in the batch may read Feature values of entities from one or more EntityTypes. Point-in-time correctness is guaranteed for Feature values of each read instance as of each instance's read timestamp.

**Overloads**
    
    
    def batch_read_feature_values(request, options = nil) -> ::Gapic::Operation

Pass arguments to `batch_read_feature_values` via a request object, either of type [BatchReadFeatureValuesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchReadFeatureValuesRequest "Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchReadFeatureValuesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def batch_read_feature_values(csv_read_instances: nil, bigquery_read_instances: nil, featurestore: nil, destination: nil, pass_through_fields: nil, entity_type_specs: nil, start_time: nil) -> ::Gapic::Operation

Pass arguments to `batch_read_feature_values` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **csv_read_instances** ([::Google::Cloud::AIPlatform::V1::CsvSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CsvSource), ::Hash) — Each read instance consists of exactly one read timestamp and one or more entity IDs identifying entities of the corresponding EntityTypes whose Features are requested.

Each output instance contains Feature values of requested entities concatenated together as of the read time.

An example read instance may be `foo_entity_id, bar_entity_id, 2020-01-01T10:00:00.123Z`.

An example output instance may be `foo_entity_id, bar_entity_id, 2020-01-01T10:00:00.123Z, foo_entity_feature1_value, bar_entity_feature2_value`.

Timestamp in each read instance must be millisecond-aligned.

`csv_read_instances` are read instances stored in a plain-text CSV file. The header should be: [ENTITY_TYPE_ID1], [ENTITY_TYPE_ID2], ..., timestamp

The columns can be in any order.

Values in the timestamp column must use the RFC 3339 format, e.g. `2012-07-30T10:43:17.123Z`.

Note: The following parameters are mutually exclusive: `csv_read_instances`, `bigquery_read_instances`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **bigquery_read_instances** ([::Google::Cloud::AIPlatform::V1::BigQuerySource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BigQuerySource), ::Hash) — Similar to csv_read_instances, but from BigQuery source.

Note: The following parameters are mutually exclusive: `bigquery_read_instances`, `csv_read_instances`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **featurestore** (::String) — Required. The resource name of the Featurestore from which to query Feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`
  * **destination** ([::Google::Cloud::AIPlatform::V1::FeatureValueDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureValueDestination), ::Hash) — Required. Specifies output location and format. 
  * **pass_through_fields** (::Array<[::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest::PassThroughField](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchReadFeatureValuesRequest-PassThroughField), ::Hash>) — When not empty, the specified fields in the *_read_instances source will be joined as-is in the output, in addition to those fields from the Featurestore Entity.

For BigQuery source, the type of the pass-through values will be automatically inferred. For CSV source, the pass-through values will be passed as opaque bytes. 

  * **entity_type_specs** (::Array<[::Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest::EntityTypeSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchReadFeatureValuesRequest-EntityTypeSpec), ::Hash>) — Required. Specifies EntityType grouping Features to read values of and settings. 
  * **start_time** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp), ::Hash) — Optional. Excludes Feature values with feature generation timestamp before this timestamp. If not set, retrieve oldest values kept in Feature Store. Timestamp, if present, must not have higher than millisecond precision. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::BatchReadFeatureValuesRequest.new
    
    # Call the batch_read_feature_values method.
    result = client.batch_read_feature_values request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the FeaturestoreService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_configure_class_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client-Configuration "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client-Configuration)) 



### #create_entity_type
    
    
    def create_entity_type(request, options = nil) -> ::Gapic::Operation
    def create_entity_type(parent: nil, entity_type: nil, entity_type_id: nil) -> ::Gapic::Operation

Creates a new EntityType in a given Featurestore.

**Overloads**
    
    
    def create_entity_type(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_entity_type` via a request object, either of type [CreateEntityTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateEntityTypeRequest "Google::Cloud::AIPlatform::V1::CreateEntityTypeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CreateEntityTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateEntityTypeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_entity_type(parent: nil, entity_type: nil, entity_type_id: nil) -> ::Gapic::Operation

Pass arguments to `create_entity_type` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Featurestore to create EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`
  * **entity_type** ([::Google::Cloud::AIPlatform::V1::EntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EntityType), ::Hash) — The EntityType to create. 
  * **entity_type_id** (::String) — Required. The ID to use for the EntityType, which will become the final component of the EntityType's resource name.

This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number.

The value must be unique within a featurestore. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CreateEntityTypeRequest.new
    
    # Call the create_entity_type method.
    result = client.create_entity_type request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_feature
    
    
    def create_feature(request, options = nil) -> ::Gapic::Operation
    def create_feature(parent: nil, feature: nil, feature_id: nil) -> ::Gapic::Operation

Creates a new Feature in a given EntityType.

**Overloads**
    
    
    def create_feature(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_feature` via a request object, either of type [CreateFeatureRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateFeatureRequest "Google::Cloud::AIPlatform::V1::CreateFeatureRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CreateFeatureRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateFeatureRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_feature(parent: nil, feature: nil, feature_id: nil) -> ::Gapic::Operation

Pass arguments to `create_feature` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`
  * **feature** ([::Google::Cloud::AIPlatform::V1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Feature), ::Hash) — Required. The Feature to create. 
  * **feature_id** (::String) — Required. The ID to use for the Feature, which will become the final component of the Feature's resource name.

This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number.

The value must be unique within an EntityType/FeatureGroup. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CreateFeatureRequest.new
    
    # Call the create_feature method.
    result = client.create_feature request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_featurestore
    
    
    def create_featurestore(request, options = nil) -> ::Gapic::Operation
    def create_featurestore(parent: nil, featurestore: nil, featurestore_id: nil) -> ::Gapic::Operation

Creates a new Featurestore in a given project and location.

**Overloads**
    
    
    def create_featurestore(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_featurestore` via a request object, either of type [CreateFeaturestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateFeaturestoreRequest "Google::Cloud::AIPlatform::V1::CreateFeaturestoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CreateFeaturestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateFeaturestoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_featurestore(parent: nil, featurestore: nil, featurestore_id: nil) -> ::Gapic::Operation

Pass arguments to `create_featurestore` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Location to create Featurestores. Format: `projects/{project}/locations/{location}`
  * **featurestore** ([::Google::Cloud::AIPlatform::V1::Featurestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Featurestore), ::Hash) — Required. The Featurestore to create. 
  * **featurestore_id** (::String) — Required. The ID to use for this Featurestore, which will become the final component of the Featurestore's resource name.

This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number.

The value must be unique within the project and location. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CreateFeaturestoreRequest.new
    
    # Call the create_featurestore method.
    result = client.create_featurestore request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_entity_type
    
    
    def delete_entity_type(request, options = nil) -> ::Gapic::Operation
    def delete_entity_type(name: nil, force: nil) -> ::Gapic::Operation

Deletes a single EntityType. The EntityType must not have any Features or `force` must be set to true for the request to succeed.

**Overloads**
    
    
    def delete_entity_type(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_entity_type` via a request object, either of type [DeleteEntityTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteEntityTypeRequest "Google::Cloud::AIPlatform::V1::DeleteEntityTypeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::DeleteEntityTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteEntityTypeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_entity_type(name: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_entity_type` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the EntityType to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`
  * **force** (::Boolean) — If set to true, any Features for this EntityType will also be deleted. (Otherwise, the request will only work if the EntityType has no Features.) 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::DeleteEntityTypeRequest.new
    
    # Call the delete_entity_type method.
    result = client.delete_entity_type request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_feature
    
    
    def delete_feature(request, options = nil) -> ::Gapic::Operation
    def delete_feature(name: nil) -> ::Gapic::Operation

Deletes a single Feature.

**Overloads**
    
    
    def delete_feature(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_feature` via a request object, either of type [DeleteFeatureRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteFeatureRequest "Google::Cloud::AIPlatform::V1::DeleteFeatureRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::DeleteFeatureRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteFeatureRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_feature(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_feature` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the Features to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::DeleteFeatureRequest.new
    
    # Call the delete_feature method.
    result = client.delete_feature request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_feature_values
    
    
    def delete_feature_values(request, options = nil) -> ::Gapic::Operation
    def delete_feature_values(select_entity: nil, select_time_range_and_feature: nil, entity_type: nil) -> ::Gapic::Operation

Delete Feature values from Featurestore.

The progress of the deletion is tracked by the returned operation. The deleted feature values are guaranteed to be invisible to subsequent read operations after the operation is marked as successfully done.

If a delete feature values operation fails, the feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same delete request again and wait till the new operation returned is marked as successfully done.

**Overloads**
    
    
    def delete_feature_values(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_feature_values` via a request object, either of type [DeleteFeatureValuesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteFeatureValuesRequest "Google::Cloud::AIPlatform::V1::DeleteFeatureValuesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::DeleteFeatureValuesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteFeatureValuesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_feature_values(select_entity: nil, select_time_range_and_feature: nil, entity_type: nil) -> ::Gapic::Operation

Pass arguments to `delete_feature_values` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **select_entity** ([::Google::Cloud::AIPlatform::V1::DeleteFeatureValuesRequest::SelectEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteFeatureValuesRequest-SelectEntity), ::Hash) — Select feature values to be deleted by specifying entities.

Note: The following parameters are mutually exclusive: `select_entity`, `select_time_range_and_feature`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **select_time_range_and_feature** ([::Google::Cloud::AIPlatform::V1::DeleteFeatureValuesRequest::SelectTimeRangeAndFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteFeatureValuesRequest-SelectTimeRangeAndFeature), ::Hash) — Select feature values to be deleted by specifying time range and features.

Note: The following parameters are mutually exclusive: `select_time_range_and_feature`, `select_entity`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **entity_type** (::String) — Required. The resource name of the EntityType grouping the Features for which values are being deleted from. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::DeleteFeatureValuesRequest.new
    
    # Call the delete_feature_values method.
    result = client.delete_feature_values request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_featurestore
    
    
    def delete_featurestore(request, options = nil) -> ::Gapic::Operation
    def delete_featurestore(name: nil, force: nil) -> ::Gapic::Operation

Deletes a single Featurestore. The Featurestore must not contain any EntityTypes or `force` must be set to true for the request to succeed.

**Overloads**
    
    
    def delete_featurestore(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_featurestore` via a request object, either of type [DeleteFeaturestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteFeaturestoreRequest "Google::Cloud::AIPlatform::V1::DeleteFeaturestoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::DeleteFeaturestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteFeaturestoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_featurestore(name: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_featurestore` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the Featurestore to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`
  * **force** (::Boolean) — If set to true, any EntityTypes and Features for this Featurestore will also be deleted. (Otherwise, the request will only work if the Featurestore has no EntityTypes.) 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::DeleteFeaturestoreRequest.new
    
    # Call the delete_featurestore method.
    result = client.delete_featurestore request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #export_feature_values
    
    
    def export_feature_values(request, options = nil) -> ::Gapic::Operation
    def export_feature_values(snapshot_export: nil, full_export: nil, entity_type: nil, destination: nil, feature_selector: nil, settings: nil) -> ::Gapic::Operation

Exports Feature values from all the entities of a target EntityType.

**Overloads**
    
    
    def export_feature_values(request, options = nil) -> ::Gapic::Operation

Pass arguments to `export_feature_values` via a request object, either of type [ExportFeatureValuesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExportFeatureValuesRequest "Google::Cloud::AIPlatform::V1::ExportFeatureValuesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ExportFeatureValuesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExportFeatureValuesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def export_feature_values(snapshot_export: nil, full_export: nil, entity_type: nil, destination: nil, feature_selector: nil, settings: nil) -> ::Gapic::Operation

Pass arguments to `export_feature_values` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **snapshot_export** ([::Google::Cloud::AIPlatform::V1::ExportFeatureValuesRequest::SnapshotExport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExportFeatureValuesRequest-SnapshotExport), ::Hash) — Exports the latest Feature values of all entities of the EntityType within a time range.

Note: The following parameters are mutually exclusive: `snapshot_export`, `full_export`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **full_export** ([::Google::Cloud::AIPlatform::V1::ExportFeatureValuesRequest::FullExport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExportFeatureValuesRequest-FullExport), ::Hash) — Exports all historical values of all entities of the EntityType within a time range

Note: The following parameters are mutually exclusive: `full_export`, `snapshot_export`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **entity_type** (::String) — Required. The resource name of the EntityType from which to export Feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`
  * **destination** ([::Google::Cloud::AIPlatform::V1::FeatureValueDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureValueDestination), ::Hash) — Required. Specifies destination location and format. 
  * **feature_selector** ([::Google::Cloud::AIPlatform::V1::FeatureSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureSelector), ::Hash) — Required. Selects Features to export values of. 
  * **settings** (::Array<[::Google::Cloud::AIPlatform::V1::DestinationFeatureSetting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DestinationFeatureSetting), ::Hash>) — Per-Feature export settings. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ExportFeatureValuesRequest.new
    
    # Call the export_feature_values method.
    result = client.export_feature_values request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_entity_type
    
    
    def get_entity_type(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::EntityType
    def get_entity_type(name: nil) -> ::Google::Cloud::AIPlatform::V1::EntityType

Gets details of a single EntityType.

**Overloads**
    
    
    def get_entity_type(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::EntityType

Pass arguments to `get_entity_type` via a request object, either of type [GetEntityTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetEntityTypeRequest "Google::Cloud::AIPlatform::V1::GetEntityTypeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetEntityTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetEntityTypeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_entity_type(name: nil) -> ::Google::Cloud::AIPlatform::V1::EntityType

Pass arguments to `get_entity_type` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the EntityType resource. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AIPlatform::V1::EntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EntityType)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::EntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EntityType)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetEntityTypeRequest.new
    
    # Call the get_entity_type method.
    result = client.get_entity_type request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::EntityType.
    p result

### #get_feature
    
    
    def get_feature(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Feature
    def get_feature(name: nil) -> ::Google::Cloud::AIPlatform::V1::Feature

Gets details of a single Feature.

**Overloads**
    
    
    def get_feature(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Feature

Pass arguments to `get_feature` via a request object, either of type [GetFeatureRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetFeatureRequest "Google::Cloud::AIPlatform::V1::GetFeatureRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetFeatureRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetFeatureRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_feature(name: nil) -> ::Google::Cloud::AIPlatform::V1::Feature

Pass arguments to `get_feature` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the Feature resource. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AIPlatform::V1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Feature)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Feature)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetFeatureRequest.new
    
    # Call the get_feature method.
    result = client.get_feature request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::Feature.
    p result

### #get_featurestore
    
    
    def get_featurestore(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Featurestore
    def get_featurestore(name: nil) -> ::Google::Cloud::AIPlatform::V1::Featurestore

Gets details of a single Featurestore.

**Overloads**
    
    
    def get_featurestore(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Featurestore

Pass arguments to `get_featurestore` via a request object, either of type [GetFeaturestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetFeaturestoreRequest "Google::Cloud::AIPlatform::V1::GetFeaturestoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetFeaturestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetFeaturestoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_featurestore(name: nil) -> ::Google::Cloud::AIPlatform::V1::Featurestore

Pass arguments to `get_featurestore` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the Featurestore resource. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AIPlatform::V1::Featurestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Featurestore)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Featurestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Featurestore)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetFeaturestoreRequest.new
    
    # Call the get_featurestore method.
    result = client.get_featurestore request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::Featurestore.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Client) 



### #import_feature_values
    
    
    def import_feature_values(request, options = nil) -> ::Gapic::Operation
    def import_feature_values(avro_source: nil, bigquery_source: nil, csv_source: nil, feature_time_field: nil, feature_time: nil, entity_type: nil, entity_id_field: nil, feature_specs: nil, disable_online_serving: nil, worker_count: nil, disable_ingestion_analysis: nil) -> ::Gapic::Operation

Imports Feature values into the Featurestore from a source storage.

The progress of the import is tracked by the returned operation. The imported features are guaranteed to be visible to subsequent read operations after the operation is marked as successfully done.

If an import operation fails, the Feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same import request again and wait till the new operation returned is marked as successfully done.

There are also scenarios where the caller can cause inconsistency.

  * Source data for import contains multiple distinct Feature values for the same entity ID and timestamp.
  * Source is modified during an import. This includes adding, updating, or removing source data and/or metadata. Examples of updating metadata include but are not limited to changing storage location, storage class, or retention policy.
  * Online serving cluster is under-provisioned.



**Overloads**
    
    
    def import_feature_values(request, options = nil) -> ::Gapic::Operation

Pass arguments to `import_feature_values` via a request object, either of type [ImportFeatureValuesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ImportFeatureValuesRequest "Google::Cloud::AIPlatform::V1::ImportFeatureValuesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ImportFeatureValuesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ImportFeatureValuesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def import_feature_values(avro_source: nil, bigquery_source: nil, csv_source: nil, feature_time_field: nil, feature_time: nil, entity_type: nil, entity_id_field: nil, feature_specs: nil, disable_online_serving: nil, worker_count: nil, disable_ingestion_analysis: nil) -> ::Gapic::Operation

Pass arguments to `import_feature_values` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **avro_source** ([::Google::Cloud::AIPlatform::V1::AvroSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AvroSource), ::Hash) — Note: The following parameters are mutually exclusive: `avro_source`, `bigquery_source`, `csv_source`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 
  * **bigquery_source** ([::Google::Cloud::AIPlatform::V1::BigQuerySource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BigQuerySource), ::Hash) — Note: The following parameters are mutually exclusive: `bigquery_source`, `avro_source`, `csv_source`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 
  * **csv_source** ([::Google::Cloud::AIPlatform::V1::CsvSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CsvSource), ::Hash) — Note: The following parameters are mutually exclusive: `csv_source`, `avro_source`, `bigquery_source`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 
  * **feature_time_field** (::String) — Source column that holds the Feature timestamp for all Feature values in each entity.

Note: The following parameters are mutually exclusive: `feature_time_field`, `feature_time`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **feature_time** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp), ::Hash) — Single Feature timestamp for all entities being imported. The timestamp must not have higher than millisecond precision.

Note: The following parameters are mutually exclusive: `feature_time`, `feature_time_field`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **entity_type** (::String) — Required. The resource name of the EntityType grouping the Features for which values are being imported. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}`
  * **entity_id_field** (::String) — Source column that holds entity IDs. If not provided, entity IDs are extracted from the column named entity_id. 
  * **feature_specs** (::Array<[::Google::Cloud::AIPlatform::V1::ImportFeatureValuesRequest::FeatureSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ImportFeatureValuesRequest-FeatureSpec), ::Hash>) — Required. Specifications defining which Feature values to import from the entity. The request fails if no feature_specs are provided, and having multiple feature_specs for one Feature is not allowed. 
  * **disable_online_serving** (::Boolean) — If set, data will not be imported for online serving. This is typically used for backfilling, where Feature generation timestamps are not in the timestamp range needed for online serving. 
  * **worker_count** (::Integer) — Specifies the number of workers that are used to write data to the Featurestore. Consider the online serving capacity that you require to achieve the desired import throughput without interfering with online serving. The value must be positive, and less than or equal to 100. If not set, defaults to using 1 worker. The low count ensures minimal impact on online serving performance. 
  * **disable_ingestion_analysis** (::Boolean) — If true, API doesn't start ingestion analysis pipeline. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ImportFeatureValuesRequest.new
    
    # Call the import_feature_values method.
    result = client.import_feature_values request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new FeaturestoreService client object.

**Yields**

  * (config) — Configure the FeaturestoreService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_entity_types
    
    
    def list_entity_types(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::EntityType>
    def list_entity_types(parent: nil, filter: nil, page_size: nil, page_token: nil, order_by: nil, read_mask: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::EntityType>

Lists EntityTypes in a given Featurestore.

**Overloads**
    
    
    def list_entity_types(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::EntityType>

Pass arguments to `list_entity_types` via a request object, either of type [ListEntityTypesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListEntityTypesRequest "Google::Cloud::AIPlatform::V1::ListEntityTypesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListEntityTypesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListEntityTypesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_entity_types(parent: nil, filter: nil, page_size: nil, page_token: nil, order_by: nil, read_mask: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::EntityType>

Pass arguments to `list_entity_types` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Featurestore to list EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`
  * **filter** (::String) — 

Lists the EntityTypes that match the filter expression. The following filters are supported:

    * `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format.
    * `update_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format.
    * `labels`: Supports key-value equality as well as key presence.

Examples:

    * `create_time > \"2020-01-31T15:30:00.000000Z\" OR update_time > \"2020-01-31T15:30:00.000000Z\"` \--> EntityTypes created or updated after 2020-01-31T15:30:00.000000Z.
    * `labels.active = yes AND labels.env = prod` \--> EntityTypes having both (active: yes) and (env: prod) labels.
    * `labels.env: *` \--> Any EntityType which has a label with 'env' as the key.
  * **page_size** (::Integer) — The maximum number of EntityTypes to return. The service may return fewer than this value. If unspecified, at most 1000 EntityTypes will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000\. 
  * **page_token** (::String) — A page token, received from a previous [FeaturestoreService.ListEntityTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_entity_types_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_entity_types \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [FeaturestoreService.ListEntityTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_entity_types_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_entity_types \(method\)") must match the call that provided the page token. 

  * **order_by** (::String) — 

A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

    * `entity_type_id`
    * `create_time`
    * `update_time`
  * **read_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Mask specifying which fields to read. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::EntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EntityType)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::EntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EntityType)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListEntityTypesRequest.new
    
    # Call the list_entity_types method.
    result = client.list_entity_types request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::EntityType.
      p item
    end

### #list_features
    
    
    def list_features(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Feature>
    def list_features(parent: nil, filter: nil, page_size: nil, page_token: nil, order_by: nil, read_mask: nil, latest_stats_count: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Feature>

Lists Features in a given EntityType.

**Overloads**
    
    
    def list_features(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Feature>

Pass arguments to `list_features` via a request object, either of type [ListFeaturesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListFeaturesRequest "Google::Cloud::AIPlatform::V1::ListFeaturesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListFeaturesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListFeaturesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_features(parent: nil, filter: nil, page_size: nil, page_token: nil, order_by: nil, read_mask: nil, latest_stats_count: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Feature>

Pass arguments to `list_features` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`
  * **filter** (::String) — 

Lists the Features that match the filter expression. The following filters are supported:

    * `value_type`: Supports = and != comparisons.
    * `create_time`: Supports =, !=, <, >, >=, and <= comparisons. Values must be in RFC 3339 format.
    * `update_time`: Supports =, !=, <, >, >=, and <= comparisons. Values must be in RFC 3339 format.
    * `labels`: Supports key-value equality as well as key presence.

Examples:

    * `value_type = DOUBLE` \--> Features whose type is DOUBLE.
    * `create_time > \"2020-01-31T15:30:00.000000Z\" OR update_time > \"2020-01-31T15:30:00.000000Z\"` \--> EntityTypes created or updated after 2020-01-31T15:30:00.000000Z.
    * `labels.active = yes AND labels.env = prod` \--> Features having both (active: yes) and (env: prod) labels.
    * `labels.env: *` \--> Any Feature which has a label with 'env' as the key.
  * **page_size** (::Integer) — The maximum number of Features to return. The service may return fewer than this value. If unspecified, at most 1000 Features will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000\. 
  * **page_token** (::String) — A page token, received from a previous [FeaturestoreService.ListFeatures](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_features_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_features \(method\)") call or [FeatureRegistryService.ListFeatures](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureRegistryService-Client#Google__Cloud__AIPlatform__V1__FeatureRegistryService__Client_list_features_instance_ "Google::Cloud::AIPlatform::V1::FeatureRegistryService::Client#list_features \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [FeaturestoreService.ListFeatures](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_features_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_features \(method\)") or [FeatureRegistryService.ListFeatures](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureRegistryService-Client#Google__Cloud__AIPlatform__V1__FeatureRegistryService__Client_list_features_instance_ "Google::Cloud::AIPlatform::V1::FeatureRegistryService::Client#list_features \(method\)") must match the call that provided the page token. 

  * **order_by** (::String) — 

A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields:

    * `feature_id`
    * `value_type` (Not supported for FeatureRegistry Feature)
    * `create_time`
    * `update_time`
  * **read_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Mask specifying which fields to read. 
  * **latest_stats_count** (::Integer) — Only applicable for Vertex AI Feature Store (Legacy). If set, return the most recent [ListFeaturesRequest.latest_stats_count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListFeaturesRequest#Google__Cloud__AIPlatform__V1__ListFeaturesRequest_latest_stats_count_instance_ "Google::Cloud::AIPlatform::V1::ListFeaturesRequest#latest_stats_count \(method\)") of stats for each Feature in response. Valid value is [0, 10]. If number of stats exists < [ListFeaturesRequest.latest_stats_count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListFeaturesRequest#Google__Cloud__AIPlatform__V1__ListFeaturesRequest_latest_stats_count_instance_ "Google::Cloud::AIPlatform::V1::ListFeaturesRequest#latest_stats_count \(method\)"), return all existing stats. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Feature)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Feature)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListFeaturesRequest.new
    
    # Call the list_features method.
    result = client.list_features request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::Feature.
      p item
    end

### #list_featurestores
    
    
    def list_featurestores(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Featurestore>
    def list_featurestores(parent: nil, filter: nil, page_size: nil, page_token: nil, order_by: nil, read_mask: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Featurestore>

Lists Featurestores in a given project and location.

**Overloads**
    
    
    def list_featurestores(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Featurestore>

Pass arguments to `list_featurestores` via a request object, either of type [ListFeaturestoresRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListFeaturestoresRequest "Google::Cloud::AIPlatform::V1::ListFeaturestoresRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListFeaturestoresRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListFeaturestoresRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_featurestores(parent: nil, filter: nil, page_size: nil, page_token: nil, order_by: nil, read_mask: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Featurestore>

Pass arguments to `list_featurestores` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Location to list Featurestores. Format: `projects/{project}/locations/{location}`
  * **filter** (::String) — 

Lists the featurestores that match the filter expression. The following fields are supported:

    * `create_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
    * `update_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
    * `online_serving_config.fixed_node_count`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons.
    * `labels`: Supports key-value equality and key presence.

Examples:

    * `create_time > "2020-01-01" OR update_time > "2020-01-01"` Featurestores created or updated after 2020-01-01.
    * `labels.env = "prod"` Featurestores with label "env" set to "prod".
  * **page_size** (::Integer) — The maximum number of Featurestores to return. The service may return fewer than this value. If unspecified, at most 100 Featurestores will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100. 
  * **page_token** (::String) — A page token, received from a previous [FeaturestoreService.ListFeaturestores](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_featurestores_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_featurestores \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [FeaturestoreService.ListFeaturestores](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_featurestores_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_featurestores \(method\)") must match the call that provided the page token. 

  * **order_by** (::String) — 

A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported Fields:

    * `create_time`
    * `update_time`
    * `online_serving_config.fixed_node_count`
  * **read_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Mask specifying which fields to read. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::Featurestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Featurestore)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::Featurestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Featurestore)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListFeaturestoresRequest.new
    
    # Call the list_featurestores method.
    result = client.list_featurestores request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::Featurestore.
      p item
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Client) 



### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::AIPlatform::V1::FeaturestoreService::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::FeaturestoreService::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Operations)) 



### #search_features
    
    
    def search_features(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Feature>
    def search_features(location: nil, query: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Feature>

Searches Features matching a query in a given project.

**Overloads**
    
    
    def search_features(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Feature>

Pass arguments to `search_features` via a request object, either of type [SearchFeaturesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SearchFeaturesRequest "Google::Cloud::AIPlatform::V1::SearchFeaturesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::SearchFeaturesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SearchFeaturesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def search_features(location: nil, query: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Feature>

Pass arguments to `search_features` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **location** (::String) — Required. The resource name of the Location to search Features. Format: `projects/{project}/locations/{location}`
  * **query** (::String) — 

Query string that is a conjunction of field-restricted queries and/or field-restricted filters. Field-restricted queries and filters can be combined using `AND` to form a conjunction.

A field query is in the form FIELD:QUERY. This implicitly checks if QUERY exists as a substring within Feature's FIELD. The QUERY and the FIELD are converted to a sequence of words (i.e. tokens) for comparison. This is done by:

    * Removing leading/trailing whitespace and tokenizing the search value. Characters that are not one of alphanumeric `[a-zA-Z0-9]`, underscore `_`, or asterisk `*` are treated as delimiters for tokens. `*` is treated as a wildcard that matches characters within a token.
    * Ignoring case.
    * Prepending an asterisk to the first and appending an asterisk to the last token in QUERY.

A QUERY must be either a singular token or a phrase. A phrase is one or multiple words enclosed in double quotation marks ("). With phrases, the order of the words is important. Words in the phrase must be matching in order and consecutively.

Supported FIELDs for field-restricted queries:

    * `feature_id`
    * `description`
    * `entity_type_id`

Examples:

    * `feature_id: foo` \--> Matches a Feature with ID containing the substring `foo` (eg. `foo`, `foofeature`, `barfoo`).
    * `feature_id: foo*feature` \--> Matches a Feature with ID containing the substring `foo*feature` (eg. `foobarfeature`).
    * `feature_id: foo AND description: bar` \--> Matches a Feature with ID containing the substring `foo` and description containing the substring `bar`.

Besides field queries, the following exact-match filters are supported. The exact-match filters do not support wildcards. Unlike field-restricted queries, exact-match filters are case-sensitive.

    * `feature_id`: Supports = comparisons.
    * `description`: Supports = comparisons. Multi-token filters should be enclosed in quotes.
    * `entity_type_id`: Supports = comparisons.
    * `value_type`: Supports = and != comparisons.
    * `labels`: Supports key-value equality as well as key presence.
    * `featurestore_id`: Supports = comparisons.

Examples:

    * `description = "foo bar"` \--> Any Feature with description exactly equal to `foo bar`
    * `value_type = DOUBLE` \--> Features whose type is DOUBLE.
    * `labels.active = yes AND labels.env = prod` \--> Features having both (active: yes) and (env: prod) labels.
    * `labels.env: *` \--> Any Feature which has a label with `env` as the key.
  * **page_size** (::Integer) — The maximum number of Features to return. The service may return fewer than this value. If unspecified, at most 100 Features will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100\. 
  * **page_token** (::String) — A page token, received from a previous [FeaturestoreService.SearchFeatures](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_search_features_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#search_features \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [FeaturestoreService.SearchFeatures](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_search_features_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#search_features \(method\)"), except `page_size`, must match the call that provided the page token. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Feature)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Feature)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::SearchFeaturesRequest.new
    
    # Call the search_features method.
    result = client.search_features request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::Feature.
      p item
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_entity_type
    
    
    def update_entity_type(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::EntityType
    def update_entity_type(entity_type: nil, update_mask: nil) -> ::Google::Cloud::AIPlatform::V1::EntityType

Updates the parameters of a single EntityType.

**Overloads**
    
    
    def update_entity_type(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::EntityType

Pass arguments to `update_entity_type` via a request object, either of type [UpdateEntityTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateEntityTypeRequest "Google::Cloud::AIPlatform::V1::UpdateEntityTypeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::UpdateEntityTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateEntityTypeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_entity_type(entity_type: nil, update_mask: nil) -> ::Google::Cloud::AIPlatform::V1::EntityType

Pass arguments to `update_entity_type` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **entity_type** ([::Google::Cloud::AIPlatform::V1::EntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EntityType), ::Hash) — Required. The EntityType's `name` field is used to identify the EntityType to be updated. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask), ::Hash) — 

Field mask is used to specify the fields to be overwritten in the EntityType resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields.

Updatable fields:

    * `description`
    * `labels`
    * `monitoring_config.snapshot_analysis.disabled`
    * `monitoring_config.snapshot_analysis.monitoring_interval_days`
    * `monitoring_config.snapshot_analysis.staleness_days`
    * `monitoring_config.import_features_analysis.state`
    * `monitoring_config.import_features_analysis.anomaly_detection_baseline`
    * `monitoring_config.numerical_threshold_config.value`
    * `monitoring_config.categorical_threshold_config.value`
    * `offline_storage_ttl_days`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AIPlatform::V1::EntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EntityType)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::EntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EntityType)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::UpdateEntityTypeRequest.new
    
    # Call the update_entity_type method.
    result = client.update_entity_type request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::EntityType.
    p result

### #update_feature
    
    
    def update_feature(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Feature
    def update_feature(feature: nil, update_mask: nil) -> ::Google::Cloud::AIPlatform::V1::Feature

Updates the parameters of a single Feature.

**Overloads**
    
    
    def update_feature(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Feature

Pass arguments to `update_feature` via a request object, either of type [UpdateFeatureRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateFeatureRequest "Google::Cloud::AIPlatform::V1::UpdateFeatureRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::UpdateFeatureRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateFeatureRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_feature(feature: nil, update_mask: nil) -> ::Google::Cloud::AIPlatform::V1::Feature

Pass arguments to `update_feature` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **feature** ([::Google::Cloud::AIPlatform::V1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Feature), ::Hash) — Required. The Feature's `name` field is used to identify the Feature to be updated. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask), ::Hash) — 

Field mask is used to specify the fields to be overwritten in the Features resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields.

Updatable fields:

    * `description`
    * `labels`
    * `disable_monitoring` (Not supported for FeatureRegistryService Feature)
    * `point_of_contact` (Not supported for FeaturestoreService FeatureStore)



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AIPlatform::V1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Feature)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Feature)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::UpdateFeatureRequest.new
    
    # Call the update_feature method.
    result = client.update_feature request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::Feature.
    p result

### #update_featurestore
    
    
    def update_featurestore(request, options = nil) -> ::Gapic::Operation
    def update_featurestore(featurestore: nil, update_mask: nil) -> ::Gapic::Operation

Updates the parameters of a single Featurestore.

**Overloads**
    
    
    def update_featurestore(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_featurestore` via a request object, either of type [UpdateFeaturestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateFeaturestoreRequest "Google::Cloud::AIPlatform::V1::UpdateFeaturestoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::UpdateFeaturestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateFeaturestoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_featurestore(featurestore: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_featurestore` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **featurestore** ([::Google::Cloud::AIPlatform::V1::Featurestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Featurestore), ::Hash) — Required. The Featurestore's `name` field is used to identify the Featurestore to be updated. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask), ::Hash) — 

Field mask is used to specify the fields to be overwritten in the Featurestore resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields.

Updatable fields:

    * `labels`
    * `online_serving_config.fixed_node_count`
    * `online_serving_config.scaling`
    * `online_storage_ttl_days`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeaturestoreService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::UpdateFeaturestoreRequest.new
    
    # Call the update_featurestore method.
    result = client.update_featurestore request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
