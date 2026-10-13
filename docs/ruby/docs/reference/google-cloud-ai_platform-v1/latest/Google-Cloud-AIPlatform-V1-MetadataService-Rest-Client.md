---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:29.419550+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.

REST client for the MetadataService service.

Service for reading and writing metadata entries.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::AIPlatform::V1::MetadataService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the MetadataService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client-Configuration "Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all MetadataService clients
    ::Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #add_context_artifacts_and_executions
    
    
    def add_context_artifacts_and_executions(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::AddContextArtifactsAndExecutionsResponse
    def add_context_artifacts_and_executions(context: nil, artifacts: nil, executions: nil) -> ::Google::Cloud::AIPlatform::V1::AddContextArtifactsAndExecutionsResponse

Adds a set of Artifacts and Executions to a Context. If any of the Artifacts or Executions have already been added to a Context, they are simply skipped.

**Overloads**
    
    
    def add_context_artifacts_and_executions(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::AddContextArtifactsAndExecutionsResponse

Pass arguments to `add_context_artifacts_and_executions` via a request object, either of type [AddContextArtifactsAndExecutionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AddContextArtifactsAndExecutionsRequest "Google::Cloud::AIPlatform::V1::AddContextArtifactsAndExecutionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::AddContextArtifactsAndExecutionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AddContextArtifactsAndExecutionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def add_context_artifacts_and_executions(context: nil, artifacts: nil, executions: nil) -> ::Google::Cloud::AIPlatform::V1::AddContextArtifactsAndExecutionsResponse

Pass arguments to `add_context_artifacts_and_executions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **context** (::String) — Required. The resource name of the Context that the Artifacts and Executions belong to. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`
  * **artifacts** (::Array<::String>) — The resource names of the Artifacts to attribute to the Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`

  * **executions** (::Array<::String>) — The resource names of the Executions to associate with the Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::AddContextArtifactsAndExecutionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AddContextArtifactsAndExecutionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::AddContextArtifactsAndExecutionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AddContextArtifactsAndExecutionsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::AddContextArtifactsAndExecutionsRequest.new
    
    # Call the add_context_artifacts_and_executions method.
    result = client.add_context_artifacts_and_executions request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::AddContextArtifactsAndExecutionsResponse.
    p result

### #add_context_children
    
    
    def add_context_children(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::AddContextChildrenResponse
    def add_context_children(context: nil, child_contexts: nil) -> ::Google::Cloud::AIPlatform::V1::AddContextChildrenResponse

Adds a set of Contexts as children to a parent Context. If any of the child Contexts have already been added to the parent Context, they are simply skipped. If this call would create a cycle or cause any Context to have more than 10 parents, the request will fail with an INVALID_ARGUMENT error.

**Overloads**
    
    
    def add_context_children(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::AddContextChildrenResponse

Pass arguments to `add_context_children` via a request object, either of type [AddContextChildrenRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AddContextChildrenRequest "Google::Cloud::AIPlatform::V1::AddContextChildrenRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::AddContextChildrenRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AddContextChildrenRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def add_context_children(context: nil, child_contexts: nil) -> ::Google::Cloud::AIPlatform::V1::AddContextChildrenResponse

Pass arguments to `add_context_children` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **context** (::String) — Required. The resource name of the parent Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`

  * **child_contexts** (::Array<::String>) — The resource names of the child Contexts. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::AddContextChildrenResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AddContextChildrenResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::AddContextChildrenResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AddContextChildrenResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::AddContextChildrenRequest.new
    
    # Call the add_context_children method.
    result = client.add_context_children request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::AddContextChildrenResponse.
    p result

### #add_execution_events
    
    
    def add_execution_events(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::AddExecutionEventsResponse
    def add_execution_events(execution: nil, events: nil) -> ::Google::Cloud::AIPlatform::V1::AddExecutionEventsResponse

Adds Events to the specified Execution. An Event indicates whether an Artifact was used as an input or output for an Execution. If an Event already exists between the Execution and the Artifact, the Event is skipped.

**Overloads**
    
    
    def add_execution_events(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::AddExecutionEventsResponse

Pass arguments to `add_execution_events` via a request object, either of type [AddExecutionEventsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AddExecutionEventsRequest "Google::Cloud::AIPlatform::V1::AddExecutionEventsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::AddExecutionEventsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AddExecutionEventsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def add_execution_events(execution: nil, events: nil) -> ::Google::Cloud::AIPlatform::V1::AddExecutionEventsResponse

Pass arguments to `add_execution_events` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **execution** (::String) — Required. The resource name of the Execution that the Events connect Artifacts with. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`
  * **events** (::Array<[::Google::Cloud::AIPlatform::V1::Event](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Event), ::Hash>) — The Events to create and add. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::AddExecutionEventsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AddExecutionEventsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::AddExecutionEventsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-AddExecutionEventsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::AddExecutionEventsRequest.new
    
    # Call the add_execution_events method.
    result = client.add_execution_events request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::AddExecutionEventsResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the MetadataService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client#Google__Cloud__AIPlatform__V1__MetadataService__Rest__Client_configure_class_ "Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client-Configuration "Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client-Configuration)) 



### #create_artifact
    
    
    def create_artifact(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Artifact
    def create_artifact(parent: nil, artifact: nil, artifact_id: nil) -> ::Google::Cloud::AIPlatform::V1::Artifact

Creates an Artifact associated with a MetadataStore.

**Overloads**
    
    
    def create_artifact(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Artifact

Pass arguments to `create_artifact` via a request object, either of type [CreateArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateArtifactRequest "Google::Cloud::AIPlatform::V1::CreateArtifactRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CreateArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateArtifactRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_artifact(parent: nil, artifact: nil, artifact_id: nil) -> ::Google::Cloud::AIPlatform::V1::Artifact

Pass arguments to `create_artifact` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the MetadataStore where the Artifact should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
  * **artifact** ([::Google::Cloud::AIPlatform::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact), ::Hash) — Required. The Artifact to create. 
  * **artifact_id** (::String) — The {artifact} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}` If not provided, the Artifact's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/[a-z][0-9]-/`. Must be unique across all Artifacts in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Artifact.) 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CreateArtifactRequest.new
    
    # Call the create_artifact method.
    result = client.create_artifact request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::Artifact.
    p result

### #create_context
    
    
    def create_context(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Context
    def create_context(parent: nil, context: nil, context_id: nil) -> ::Google::Cloud::AIPlatform::V1::Context

Creates a Context associated with a MetadataStore.

**Overloads**
    
    
    def create_context(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Context

Pass arguments to `create_context` via a request object, either of type [CreateContextRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateContextRequest "Google::Cloud::AIPlatform::V1::CreateContextRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CreateContextRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateContextRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_context(parent: nil, context: nil, context_id: nil) -> ::Google::Cloud::AIPlatform::V1::Context

Pass arguments to `create_context` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the MetadataStore where the Context should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
  * **context** ([::Google::Cloud::AIPlatform::V1::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context), ::Hash) — Required. The Context to create. 
  * **context_id** (::String) — The {context} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`. If not provided, the Context's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/[a-z][0-9]-/`. Must be unique across all Contexts in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Context.) 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CreateContextRequest.new
    
    # Call the create_context method.
    result = client.create_context request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::Context.
    p result

### #create_execution
    
    
    def create_execution(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Execution
    def create_execution(parent: nil, execution: nil, execution_id: nil) -> ::Google::Cloud::AIPlatform::V1::Execution

Creates an Execution associated with a MetadataStore.

**Overloads**
    
    
    def create_execution(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Execution

Pass arguments to `create_execution` via a request object, either of type [CreateExecutionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateExecutionRequest "Google::Cloud::AIPlatform::V1::CreateExecutionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CreateExecutionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateExecutionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_execution(parent: nil, execution: nil, execution_id: nil) -> ::Google::Cloud::AIPlatform::V1::Execution

Pass arguments to `create_execution` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the MetadataStore where the Execution should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
  * **execution** ([::Google::Cloud::AIPlatform::V1::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution), ::Hash) — Required. The Execution to create. 
  * **execution_id** (::String) — The {execution} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}` If not provided, the Execution's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/[a-z][0-9]-/`. Must be unique across all Executions in the parent MetadataStore. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting Execution.) 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CreateExecutionRequest.new
    
    # Call the create_execution method.
    result = client.create_execution request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::Execution.
    p result

### #create_metadata_schema
    
    
    def create_metadata_schema(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::MetadataSchema
    def create_metadata_schema(parent: nil, metadata_schema: nil, metadata_schema_id: nil) -> ::Google::Cloud::AIPlatform::V1::MetadataSchema

Creates a MetadataSchema.

**Overloads**
    
    
    def create_metadata_schema(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::MetadataSchema

Pass arguments to `create_metadata_schema` via a request object, either of type [CreateMetadataSchemaRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateMetadataSchemaRequest "Google::Cloud::AIPlatform::V1::CreateMetadataSchemaRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CreateMetadataSchemaRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateMetadataSchemaRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_metadata_schema(parent: nil, metadata_schema: nil, metadata_schema_id: nil) -> ::Google::Cloud::AIPlatform::V1::MetadataSchema

Pass arguments to `create_metadata_schema` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the MetadataStore where the MetadataSchema should be created. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
  * **metadata_schema** ([::Google::Cloud::AIPlatform::V1::MetadataSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataSchema), ::Hash) — Required. The MetadataSchema to create. 
  * **metadata_schema_id** (::String) — The {metadata_schema} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/metadataSchemas/{metadataschema}` If not provided, the MetadataStore's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/[a-z][0-9]-/`. Must be unique across all MetadataSchemas in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting MetadataSchema.) 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::MetadataSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataSchema)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::MetadataSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataSchema)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CreateMetadataSchemaRequest.new
    
    # Call the create_metadata_schema method.
    result = client.create_metadata_schema request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::MetadataSchema.
    p result

### #create_metadata_store
    
    
    def create_metadata_store(request, options = nil) -> ::Gapic::Operation
    def create_metadata_store(parent: nil, metadata_store: nil, metadata_store_id: nil) -> ::Gapic::Operation

Initializes a MetadataStore, including allocation of resources.

**Overloads**
    
    
    def create_metadata_store(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_metadata_store` via a request object, either of type [CreateMetadataStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateMetadataStoreRequest "Google::Cloud::AIPlatform::V1::CreateMetadataStoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CreateMetadataStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateMetadataStoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_metadata_store(parent: nil, metadata_store: nil, metadata_store_id: nil) -> ::Gapic::Operation

Pass arguments to `create_metadata_store` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Location where the MetadataStore should be created. Format: `projects/{project}/locations/{location}/`
  * **metadata_store** ([::Google::Cloud::AIPlatform::V1::MetadataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataStore), ::Hash) — Required. The MetadataStore to create. 
  * **metadata_store_id** (::String) — The {metadatastore} portion of the resource name with the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}` If not provided, the MetadataStore's ID will be a UUID generated by the service. Must be 4-128 characters in length. Valid characters are `/[a-z][0-9]-/`. Must be unique across all MetadataStores in the parent Location. (Otherwise the request will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the caller can't view the preexisting MetadataStore.) 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CreateMetadataStoreRequest.new
    
    # Call the create_metadata_store method.
    result = client.create_metadata_store request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_artifact
    
    
    def delete_artifact(request, options = nil) -> ::Gapic::Operation
    def delete_artifact(name: nil, etag: nil) -> ::Gapic::Operation

Deletes an Artifact.

**Overloads**
    
    
    def delete_artifact(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_artifact` via a request object, either of type [DeleteArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteArtifactRequest "Google::Cloud::AIPlatform::V1::DeleteArtifactRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::DeleteArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteArtifactRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_artifact(name: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_artifact` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the Artifact to delete. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`
  * **etag** (::String) — Optional. The etag of the Artifact to delete. If this is provided, it must match the server's etag. Otherwise, the request will fail with a FAILED_PRECONDITION. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::DeleteArtifactRequest.new
    
    # Call the delete_artifact method.
    result = client.delete_artifact request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_context
    
    
    def delete_context(request, options = nil) -> ::Gapic::Operation
    def delete_context(name: nil, force: nil, etag: nil) -> ::Gapic::Operation

Deletes a stored Context.

**Overloads**
    
    
    def delete_context(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_context` via a request object, either of type [DeleteContextRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteContextRequest "Google::Cloud::AIPlatform::V1::DeleteContextRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::DeleteContextRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteContextRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_context(name: nil, force: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_context` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the Context to delete. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`
  * **force** (::Boolean) — The force deletion semantics is still undefined. Users should not use this field. 
  * **etag** (::String) — Optional. The etag of the Context to delete. If this is provided, it must match the server's etag. Otherwise, the request will fail with a FAILED_PRECONDITION. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::DeleteContextRequest.new
    
    # Call the delete_context method.
    result = client.delete_context request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_execution
    
    
    def delete_execution(request, options = nil) -> ::Gapic::Operation
    def delete_execution(name: nil, etag: nil) -> ::Gapic::Operation

Deletes an Execution.

**Overloads**
    
    
    def delete_execution(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_execution` via a request object, either of type [DeleteExecutionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteExecutionRequest "Google::Cloud::AIPlatform::V1::DeleteExecutionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::DeleteExecutionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteExecutionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_execution(name: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_execution` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the Execution to delete. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`
  * **etag** (::String) — Optional. The etag of the Execution to delete. If this is provided, it must match the server's etag. Otherwise, the request will fail with a FAILED_PRECONDITION. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::DeleteExecutionRequest.new
    
    # Call the delete_execution method.
    result = client.delete_execution request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_metadata_store
    
    
    def delete_metadata_store(request, options = nil) -> ::Gapic::Operation
    def delete_metadata_store(name: nil, force: nil) -> ::Gapic::Operation

Deletes a single MetadataStore and all its child resources (Artifacts, Executions, and Contexts).

**Overloads**
    
    
    def delete_metadata_store(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_metadata_store` via a request object, either of type [DeleteMetadataStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteMetadataStoreRequest "Google::Cloud::AIPlatform::V1::DeleteMetadataStoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::DeleteMetadataStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteMetadataStoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_metadata_store(name: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_metadata_store` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the MetadataStore to delete. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
  * **force** (::Boolean) — Deprecated: Field is no longer supported. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::DeleteMetadataStoreRequest.new
    
    # Call the delete_metadata_store method.
    result = client.delete_metadata_store request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_artifact
    
    
    def get_artifact(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Artifact
    def get_artifact(name: nil) -> ::Google::Cloud::AIPlatform::V1::Artifact

Retrieves a specific Artifact.

**Overloads**
    
    
    def get_artifact(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Artifact

Pass arguments to `get_artifact` via a request object, either of type [GetArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetArtifactRequest "Google::Cloud::AIPlatform::V1::GetArtifactRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetArtifactRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_artifact(name: nil) -> ::Google::Cloud::AIPlatform::V1::Artifact

Pass arguments to `get_artifact` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the Artifact to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetArtifactRequest.new
    
    # Call the get_artifact method.
    result = client.get_artifact request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::Artifact.
    p result

### #get_context
    
    
    def get_context(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Context
    def get_context(name: nil) -> ::Google::Cloud::AIPlatform::V1::Context

Retrieves a specific Context.

**Overloads**
    
    
    def get_context(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Context

Pass arguments to `get_context` via a request object, either of type [GetContextRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetContextRequest "Google::Cloud::AIPlatform::V1::GetContextRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetContextRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetContextRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_context(name: nil) -> ::Google::Cloud::AIPlatform::V1::Context

Pass arguments to `get_context` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the Context to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetContextRequest.new
    
    # Call the get_context method.
    result = client.get_context request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::Context.
    p result

### #get_execution
    
    
    def get_execution(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Execution
    def get_execution(name: nil) -> ::Google::Cloud::AIPlatform::V1::Execution

Retrieves a specific Execution.

**Overloads**
    
    
    def get_execution(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Execution

Pass arguments to `get_execution` via a request object, either of type [GetExecutionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetExecutionRequest "Google::Cloud::AIPlatform::V1::GetExecutionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetExecutionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetExecutionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_execution(name: nil) -> ::Google::Cloud::AIPlatform::V1::Execution

Pass arguments to `get_execution` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the Execution to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetExecutionRequest.new
    
    # Call the get_execution method.
    result = client.get_execution request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::Execution.
    p result

### #get_metadata_schema
    
    
    def get_metadata_schema(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::MetadataSchema
    def get_metadata_schema(name: nil) -> ::Google::Cloud::AIPlatform::V1::MetadataSchema

Retrieves a specific MetadataSchema.

**Overloads**
    
    
    def get_metadata_schema(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::MetadataSchema

Pass arguments to `get_metadata_schema` via a request object, either of type [GetMetadataSchemaRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetMetadataSchemaRequest "Google::Cloud::AIPlatform::V1::GetMetadataSchemaRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetMetadataSchemaRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetMetadataSchemaRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_metadata_schema(name: nil) -> ::Google::Cloud::AIPlatform::V1::MetadataSchema

Pass arguments to `get_metadata_schema` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the MetadataSchema to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/metadataSchemas/{metadataschema}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::MetadataSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataSchema)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::MetadataSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataSchema)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetMetadataSchemaRequest.new
    
    # Call the get_metadata_schema method.
    result = client.get_metadata_schema request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::MetadataSchema.
    p result

### #get_metadata_store
    
    
    def get_metadata_store(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::MetadataStore
    def get_metadata_store(name: nil) -> ::Google::Cloud::AIPlatform::V1::MetadataStore

Retrieves a specific MetadataStore.

**Overloads**
    
    
    def get_metadata_store(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::MetadataStore

Pass arguments to `get_metadata_store` via a request object, either of type [GetMetadataStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetMetadataStoreRequest "Google::Cloud::AIPlatform::V1::GetMetadataStoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetMetadataStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetMetadataStoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_metadata_store(name: nil) -> ::Google::Cloud::AIPlatform::V1::MetadataStore

Pass arguments to `get_metadata_store` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the MetadataStore to retrieve. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::MetadataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataStore)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::MetadataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataStore)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetMetadataStoreRequest.new
    
    # Call the get_metadata_store method.
    result = client.get_metadata_store request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::MetadataStore.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new MetadataService REST client object.

**Yields**

  * (config) — Configure the MetadataService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_artifacts
    
    
    def list_artifacts(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Artifact>
    def list_artifacts(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Artifact>

Lists Artifacts in the MetadataStore.

**Overloads**
    
    
    def list_artifacts(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Artifact>

Pass arguments to `list_artifacts` via a request object, either of type [ListArtifactsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListArtifactsRequest "Google::Cloud::AIPlatform::V1::ListArtifactsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListArtifactsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListArtifactsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_artifacts(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Artifact>

Pass arguments to `list_artifacts` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The MetadataStore whose Artifacts should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
  * **page_size** (::Integer) — The maximum number of Artifacts to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100. 
  * **page_token** (::String) — A page token, received from a previous [MetadataService.ListArtifacts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client#Google__Cloud__AIPlatform__V1__MetadataService__Rest__Client_list_artifacts_instance_ "Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client#list_artifacts \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.) 

  * **filter** (::String) — Filter specifying the boolean condition for the Artifacts to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. The supported set of filters include the following:

    * **Attribute filtering** : For example: `display_name = "test"`. Supported fields include: `name`, `display_name`, `uri`, `state`, `schema_title`, `create_time`, and `update_time`. Time fields, such as `create_time` and `update_time`, require values specified in RFC-3339 format. For example: `create_time = "2020-11-19T11:30:00-04:00"`
    * **Metadata field** : To filter on metadata fields use traversal operation as follows: `metadata.<field_name>.<type_value>`. For example: `metadata.field_1.number_value = 10.0` In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: `metadata."field:1".number_value = 10.0`
    * **Context based filtering** : To filter Artifacts based on the contexts to which they belong, use the function operator with the full resource name `in_context(<context-name>)`. For example: `in_context("projects/<project_number>/locations/<location>/metadataStores/<metadatastore_name>/contexts/<context-id>")`

Each of the above supported filter types can be combined together using logical operators (`AND` & `OR`). Maximum nested expression depth allowed is 5.

For example: `display_name = "test" AND metadata.field1.bool_value = true`. 

  * **order_by** (::String) — How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a " desc" suffix; for example: "foo desc, bar". Subfields are specified with a `.` character, such as foo.bar. see https://google.aip.dev/132#ordering for more details. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListArtifactsRequest.new
    
    # Call the list_artifacts method.
    result = client.list_artifacts request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::Artifact.
      p item
    end

### #list_contexts
    
    
    def list_contexts(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Context>
    def list_contexts(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Context>

Lists Contexts on the MetadataStore.

**Overloads**
    
    
    def list_contexts(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Context>

Pass arguments to `list_contexts` via a request object, either of type [ListContextsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListContextsRequest "Google::Cloud::AIPlatform::V1::ListContextsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListContextsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListContextsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_contexts(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Context>

Pass arguments to `list_contexts` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The MetadataStore whose Contexts should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
  * **page_size** (::Integer) — The maximum number of Contexts to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100. 
  * **page_token** (::String) — A page token, received from a previous [MetadataService.ListContexts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client#Google__Cloud__AIPlatform__V1__MetadataService__Rest__Client_list_contexts_instance_ "Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client#list_contexts \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.) 

  * **filter** (::String) — Filter specifying the boolean condition for the Contexts to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. Following are the supported set of filters:

    * **Attribute filtering** : For example: `display_name = "test"`. Supported fields include: `name`, `display_name`, `schema_title`, `create_time`, and `update_time`. Time fields, such as `create_time` and `update_time`, require values specified in RFC-3339 format. For example: `create_time = "2020-11-19T11:30:00-04:00"`.
    * **Metadata field** : To filter on metadata fields use traversal operation as follows: `metadata.<field_name>.<type_value>`. For example: `metadata.field_1.number_value = 10.0`. In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: `metadata."field:1".number_value = 10.0`
    * **Parent Child filtering** : To filter Contexts based on parent-child relationship use the HAS operator as follows:

` parent_contexts: "projects/<project_number>/locations/<location>/metadataStores/<metadatastore_name>/contexts/<context_id>" child_contexts: "projects/<project_number>/locations/<location>/metadataStores/<metadatastore_name>/contexts/<context_id>" `

Each of the above supported filters can be combined together using logical operators (`AND` & `OR`). Maximum nested expression depth allowed is 5.

For example: `display_name = "test" AND metadata.field1.bool_value = true`. 

  * **order_by** (::String) — How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a " desc" suffix; for example: "foo desc, bar". Subfields are specified with a `.` character, such as foo.bar. see https://google.aip.dev/132#ordering for more details. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListContextsRequest.new
    
    # Call the list_contexts method.
    result = client.list_contexts request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::Context.
      p item
    end

### #list_executions
    
    
    def list_executions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Execution>
    def list_executions(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Execution>

Lists Executions in the MetadataStore.

**Overloads**
    
    
    def list_executions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Execution>

Pass arguments to `list_executions` via a request object, either of type [ListExecutionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListExecutionsRequest "Google::Cloud::AIPlatform::V1::ListExecutionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListExecutionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListExecutionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_executions(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::Execution>

Pass arguments to `list_executions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The MetadataStore whose Executions should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
  * **page_size** (::Integer) — The maximum number of Executions to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100. 
  * **page_token** (::String) — A page token, received from a previous [MetadataService.ListExecutions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client#Google__Cloud__AIPlatform__V1__MetadataService__Rest__Client_list_executions_instance_ "Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client#list_executions \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with an INVALID_ARGUMENT error.) 

  * **filter** (::String) — Filter specifying the boolean condition for the Executions to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. Following are the supported set of filters:

    * **Attribute filtering** : For example: `display_name = "test"`. Supported fields include: `name`, `display_name`, `state`, `schema_title`, `create_time`, and `update_time`. Time fields, such as `create_time` and `update_time`, require values specified in RFC-3339 format. For example: `create_time = "2020-11-19T11:30:00-04:00"`.
    * **Metadata field** : To filter on metadata fields use traversal operation as follows: `metadata.<field_name>.<type_value>` For example: `metadata.field_1.number_value = 10.0` In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: `metadata."field:1".number_value = 10.0`
    * **Context based filtering** : To filter Executions based on the contexts to which they belong use the function operator with the full resource name: `in_context(<context-name>)`. For example: `in_context("projects/<project_number>/locations/<location>/metadataStores/<metadatastore_name>/contexts/<context-id>")`

Each of the above supported filters can be combined together using logical operators (`AND` & `OR`). Maximum nested expression depth allowed is 5.

For example: `display_name = "test" AND metadata.field1.bool_value = true`. 

  * **order_by** (::String) — How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a " desc" suffix; for example: "foo desc, bar". Subfields are specified with a `.` character, such as foo.bar. see https://google.aip.dev/132#ordering for more details. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListExecutionsRequest.new
    
    # Call the list_executions method.
    result = client.list_executions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::Execution.
      p item
    end

### #list_metadata_schemas
    
    
    def list_metadata_schemas(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::MetadataSchema>
    def list_metadata_schemas(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::MetadataSchema>

Lists MetadataSchemas.

**Overloads**
    
    
    def list_metadata_schemas(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::MetadataSchema>

Pass arguments to `list_metadata_schemas` via a request object, either of type [ListMetadataSchemasRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListMetadataSchemasRequest "Google::Cloud::AIPlatform::V1::ListMetadataSchemasRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListMetadataSchemasRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListMetadataSchemasRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_metadata_schemas(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::MetadataSchema>

Pass arguments to `list_metadata_schemas` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The MetadataStore whose MetadataSchemas should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
  * **page_size** (::Integer) — The maximum number of MetadataSchemas to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100. 
  * **page_token** (::String) — A page token, received from a previous [MetadataService.ListMetadataSchemas](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client#Google__Cloud__AIPlatform__V1__MetadataService__Rest__Client_list_metadata_schemas_instance_ "Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client#list_metadata_schemas \(method\)") call. Provide this to retrieve the next page.

When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.) 

  * **filter** (::String) — A query to filter available MetadataSchemas for matching results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::MetadataSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataSchema)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::MetadataSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataSchema)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListMetadataSchemasRequest.new
    
    # Call the list_metadata_schemas method.
    result = client.list_metadata_schemas request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::MetadataSchema.
      p item
    end

### #list_metadata_stores
    
    
    def list_metadata_stores(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::MetadataStore>
    def list_metadata_stores(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::MetadataStore>

Lists MetadataStores for a Location.

**Overloads**
    
    
    def list_metadata_stores(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::MetadataStore>

Pass arguments to `list_metadata_stores` via a request object, either of type [ListMetadataStoresRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListMetadataStoresRequest "Google::Cloud::AIPlatform::V1::ListMetadataStoresRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListMetadataStoresRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListMetadataStoresRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_metadata_stores(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::MetadataStore>

Pass arguments to `list_metadata_stores` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The Location whose MetadataStores should be listed. Format: `projects/{project}/locations/{location}`
  * **page_size** (::Integer) — The maximum number of Metadata Stores to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100. 
  * **page_token** (::String) — A page token, received from a previous [MetadataService.ListMetadataStores](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Client#Google__Cloud__AIPlatform__V1__MetadataService__Rest__Client_list_metadata_stores_instance_ "Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client#list_metadata_stores \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.) 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::MetadataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataStore)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::MetadataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataStore)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListMetadataStoresRequest.new
    
    # Call the list_metadata_stores method.
    result = client.list_metadata_stores request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::MetadataStore.
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



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::AIPlatform::V1::MetadataService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::MetadataService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Rest-Operations)) 



### #purge_artifacts
    
    
    def purge_artifacts(request, options = nil) -> ::Gapic::Operation
    def purge_artifacts(parent: nil, filter: nil, force: nil) -> ::Gapic::Operation

Purges Artifacts.

**Overloads**
    
    
    def purge_artifacts(request, options = nil) -> ::Gapic::Operation

Pass arguments to `purge_artifacts` via a request object, either of type [PurgeArtifactsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PurgeArtifactsRequest "Google::Cloud::AIPlatform::V1::PurgeArtifactsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::PurgeArtifactsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PurgeArtifactsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def purge_artifacts(parent: nil, filter: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `purge_artifacts` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The metadata store to purge Artifacts from. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
  * **filter** (::String) — Required. A required filter matching the Artifacts to be purged. E.g., `update_time <= 2020-11-19T11:30:00-04:00`. 
  * **force** (::Boolean) — Optional. Flag to indicate to actually perform the purge. If `force` is set to false, the method will return a sample of Artifact names that would be deleted. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::PurgeArtifactsRequest.new
    
    # Call the purge_artifacts method.
    result = client.purge_artifacts request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #purge_contexts
    
    
    def purge_contexts(request, options = nil) -> ::Gapic::Operation
    def purge_contexts(parent: nil, filter: nil, force: nil) -> ::Gapic::Operation

Purges Contexts.

**Overloads**
    
    
    def purge_contexts(request, options = nil) -> ::Gapic::Operation

Pass arguments to `purge_contexts` via a request object, either of type [PurgeContextsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PurgeContextsRequest "Google::Cloud::AIPlatform::V1::PurgeContextsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::PurgeContextsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PurgeContextsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def purge_contexts(parent: nil, filter: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `purge_contexts` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The metadata store to purge Contexts from. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
  * **filter** (::String) — Required. A required filter matching the Contexts to be purged. E.g., `update_time <= 2020-11-19T11:30:00-04:00`. 
  * **force** (::Boolean) — Optional. Flag to indicate to actually perform the purge. If `force` is set to false, the method will return a sample of Context names that would be deleted. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::PurgeContextsRequest.new
    
    # Call the purge_contexts method.
    result = client.purge_contexts request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #purge_executions
    
    
    def purge_executions(request, options = nil) -> ::Gapic::Operation
    def purge_executions(parent: nil, filter: nil, force: nil) -> ::Gapic::Operation

Purges Executions.

**Overloads**
    
    
    def purge_executions(request, options = nil) -> ::Gapic::Operation

Pass arguments to `purge_executions` via a request object, either of type [PurgeExecutionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PurgeExecutionsRequest "Google::Cloud::AIPlatform::V1::PurgeExecutionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::PurgeExecutionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PurgeExecutionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def purge_executions(parent: nil, filter: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `purge_executions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The metadata store to purge Executions from. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`
  * **filter** (::String) — Required. A required filter matching the Executions to be purged. E.g., `update_time <= 2020-11-19T11:30:00-04:00`. 
  * **force** (::Boolean) — Optional. Flag to indicate to actually perform the purge. If `force` is set to false, the method will return a sample of Execution names that would be deleted. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::PurgeExecutionsRequest.new
    
    # Call the purge_executions method.
    result = client.purge_executions request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #query_artifact_lineage_subgraph
    
    
    def query_artifact_lineage_subgraph(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::LineageSubgraph
    def query_artifact_lineage_subgraph(artifact: nil, max_hops: nil, filter: nil) -> ::Google::Cloud::AIPlatform::V1::LineageSubgraph

Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph.

**Overloads**
    
    
    def query_artifact_lineage_subgraph(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::LineageSubgraph

Pass arguments to `query_artifact_lineage_subgraph` via a request object, either of type [QueryArtifactLineageSubgraphRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-QueryArtifactLineageSubgraphRequest "Google::Cloud::AIPlatform::V1::QueryArtifactLineageSubgraphRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::QueryArtifactLineageSubgraphRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-QueryArtifactLineageSubgraphRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def query_artifact_lineage_subgraph(artifact: nil, max_hops: nil, filter: nil) -> ::Google::Cloud::AIPlatform::V1::LineageSubgraph

Pass arguments to `query_artifact_lineage_subgraph` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **artifact** (::String) — Required. The resource name of the Artifact whose Lineage needs to be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`

The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000. 

  * **max_hops** (::Integer) — Specifies the size of the lineage graph in terms of number of hops from the specified artifact. Negative Value: INVALID_ARGUMENT error is returned 0: Only input artifact is returned. No value: Transitive closure is performed to return the complete graph. 
  * **filter** (::String) — Filter specifying the boolean condition for the Artifacts to satisfy in order to be part of the Lineage Subgraph. The syntax to define filter query is based on https://google.aip.dev/160. The supported set of filters include the following:

    * **Attribute filtering** : For example: `display_name = "test"` Supported fields include: `name`, `display_name`, `uri`, `state`, `schema_title`, `create_time`, and `update_time`. Time fields, such as `create_time` and `update_time`, require values specified in RFC-3339 format. For example: `create_time = "2020-11-19T11:30:00-04:00"`
    * **Metadata field** : To filter on metadata fields use traversal operation as follows: `metadata.<field_name>.<type_value>`. For example: `metadata.field_1.number_value = 10.0` In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: `metadata."field:1".number_value = 10.0`

Each of the above supported filter types can be combined together using logical operators (`AND` & `OR`). Maximum nested expression depth allowed is 5.

For example: `display_name = "test" AND metadata.field1.bool_value = true`. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::LineageSubgraph](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-LineageSubgraph)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::LineageSubgraph](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-LineageSubgraph)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::QueryArtifactLineageSubgraphRequest.new
    
    # Call the query_artifact_lineage_subgraph method.
    result = client.query_artifact_lineage_subgraph request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::LineageSubgraph.
    p result

### #query_context_lineage_subgraph
    
    
    def query_context_lineage_subgraph(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::LineageSubgraph
    def query_context_lineage_subgraph(context: nil) -> ::Google::Cloud::AIPlatform::V1::LineageSubgraph

Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph.

**Overloads**
    
    
    def query_context_lineage_subgraph(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::LineageSubgraph

Pass arguments to `query_context_lineage_subgraph` via a request object, either of type [QueryContextLineageSubgraphRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-QueryContextLineageSubgraphRequest "Google::Cloud::AIPlatform::V1::QueryContextLineageSubgraphRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::QueryContextLineageSubgraphRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-QueryContextLineageSubgraphRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def query_context_lineage_subgraph(context: nil) -> ::Google::Cloud::AIPlatform::V1::LineageSubgraph

Pass arguments to `query_context_lineage_subgraph` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **context** (::String) — Required. The resource name of the Context whose Artifacts and Executions should be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`

The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::LineageSubgraph](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-LineageSubgraph)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::LineageSubgraph](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-LineageSubgraph)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::QueryContextLineageSubgraphRequest.new
    
    # Call the query_context_lineage_subgraph method.
    result = client.query_context_lineage_subgraph request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::LineageSubgraph.
    p result

### #query_execution_inputs_and_outputs
    
    
    def query_execution_inputs_and_outputs(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::LineageSubgraph
    def query_execution_inputs_and_outputs(execution: nil) -> ::Google::Cloud::AIPlatform::V1::LineageSubgraph

Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events.

**Overloads**
    
    
    def query_execution_inputs_and_outputs(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::LineageSubgraph

Pass arguments to `query_execution_inputs_and_outputs` via a request object, either of type [QueryExecutionInputsAndOutputsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-QueryExecutionInputsAndOutputsRequest "Google::Cloud::AIPlatform::V1::QueryExecutionInputsAndOutputsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::QueryExecutionInputsAndOutputsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-QueryExecutionInputsAndOutputsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def query_execution_inputs_and_outputs(execution: nil) -> ::Google::Cloud::AIPlatform::V1::LineageSubgraph

Pass arguments to `query_execution_inputs_and_outputs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **execution** (::String) — Required. The resource name of the Execution whose input and output Artifacts should be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::LineageSubgraph](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-LineageSubgraph)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::LineageSubgraph](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-LineageSubgraph)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::QueryExecutionInputsAndOutputsRequest.new
    
    # Call the query_execution_inputs_and_outputs method.
    result = client.query_execution_inputs_and_outputs request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::LineageSubgraph.
    p result

### #remove_context_children
    
    
    def remove_context_children(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::RemoveContextChildrenResponse
    def remove_context_children(context: nil, child_contexts: nil) -> ::Google::Cloud::AIPlatform::V1::RemoveContextChildrenResponse

Remove a set of children contexts from a parent Context. If any of the child Contexts were NOT added to the parent Context, they are simply skipped.

**Overloads**
    
    
    def remove_context_children(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::RemoveContextChildrenResponse

Pass arguments to `remove_context_children` via a request object, either of type [RemoveContextChildrenRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-RemoveContextChildrenRequest "Google::Cloud::AIPlatform::V1::RemoveContextChildrenRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::RemoveContextChildrenRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-RemoveContextChildrenRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def remove_context_children(context: nil, child_contexts: nil) -> ::Google::Cloud::AIPlatform::V1::RemoveContextChildrenResponse

Pass arguments to `remove_context_children` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **context** (::String) — Required. The resource name of the parent Context.

Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`

  * **child_contexts** (::Array<::String>) — The resource names of the child Contexts. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::RemoveContextChildrenResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-RemoveContextChildrenResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::RemoveContextChildrenResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-RemoveContextChildrenResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::RemoveContextChildrenRequest.new
    
    # Call the remove_context_children method.
    result = client.remove_context_children request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::RemoveContextChildrenResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_artifact
    
    
    def update_artifact(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Artifact
    def update_artifact(artifact: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::AIPlatform::V1::Artifact

Updates a stored Artifact.

**Overloads**
    
    
    def update_artifact(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Artifact

Pass arguments to `update_artifact` via a request object, either of type [UpdateArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateArtifactRequest "Google::Cloud::AIPlatform::V1::UpdateArtifactRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::UpdateArtifactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateArtifactRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_artifact(artifact: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::AIPlatform::V1::Artifact

Pass arguments to `update_artifact` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **artifact** ([::Google::Cloud::AIPlatform::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact), ::Hash) — Required. The Artifact containing updates. The Artifact's [Artifact.name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact#Google__Cloud__AIPlatform__V1__Artifact_name_instance_ "Google::Cloud::AIPlatform::V1::Artifact#name \(method\)") field is used to identify the Artifact to be updated. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}`
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. A FieldMask indicating which fields should be updated. 
  * **allow_missing** (::Boolean) — If set to true, and the [Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact "Google::Cloud::AIPlatform::V1::Artifact \(class\)") is not found, a new [Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact "Google::Cloud::AIPlatform::V1::Artifact \(class\)") is created. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Artifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Artifact)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::UpdateArtifactRequest.new
    
    # Call the update_artifact method.
    result = client.update_artifact request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::Artifact.
    p result

### #update_context
    
    
    def update_context(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Context
    def update_context(context: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::AIPlatform::V1::Context

Updates a stored Context.

**Overloads**
    
    
    def update_context(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Context

Pass arguments to `update_context` via a request object, either of type [UpdateContextRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateContextRequest "Google::Cloud::AIPlatform::V1::UpdateContextRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::UpdateContextRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateContextRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_context(context: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::AIPlatform::V1::Context

Pass arguments to `update_context` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **context** ([::Google::Cloud::AIPlatform::V1::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context), ::Hash) — Required. The Context containing updates. The Context's [Context.name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context#Google__Cloud__AIPlatform__V1__Context_name_instance_ "Google::Cloud::AIPlatform::V1::Context#name \(method\)") field is used to identify the Context to be updated. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. A FieldMask indicating which fields should be updated. 
  * **allow_missing** (::Boolean) — If set to true, and the [Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context "Google::Cloud::AIPlatform::V1::Context \(class\)") is not found, a new [Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context "Google::Cloud::AIPlatform::V1::Context \(class\)") is created. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Context)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::UpdateContextRequest.new
    
    # Call the update_context method.
    result = client.update_context request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::Context.
    p result

### #update_execution
    
    
    def update_execution(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Execution
    def update_execution(execution: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::AIPlatform::V1::Execution

Updates a stored Execution.

**Overloads**
    
    
    def update_execution(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::Execution

Pass arguments to `update_execution` via a request object, either of type [UpdateExecutionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateExecutionRequest "Google::Cloud::AIPlatform::V1::UpdateExecutionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::UpdateExecutionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateExecutionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_execution(execution: nil, update_mask: nil, allow_missing: nil) -> ::Google::Cloud::AIPlatform::V1::Execution

Pass arguments to `update_execution` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **execution** ([::Google::Cloud::AIPlatform::V1::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution), ::Hash) — Required. The Execution containing updates. The Execution's [Execution.name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution#Google__Cloud__AIPlatform__V1__Execution_name_instance_ "Google::Cloud::AIPlatform::V1::Execution#name \(method\)") field is used to identify the Execution to be updated. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. A FieldMask indicating which fields should be updated. 
  * **allow_missing** (::Boolean) — If set to true, and the [Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution "Google::Cloud::AIPlatform::V1::Execution \(class\)") is not found, a new [Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution "Google::Cloud::AIPlatform::V1::Execution \(class\)") is created. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Execution)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::MetadataService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::UpdateExecutionRequest.new
    
    # Call the update_execution method.
    result = client.update_execution request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::Execution.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
