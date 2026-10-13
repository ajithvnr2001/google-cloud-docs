---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Client/
title: Telco Automation V1 API - Class Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client (v2.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:39.423750+00:00
---

# Telco Automation V1 API - Class Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client (v2.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Telco Automation V1 API - Class Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client (v2.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.5.1 (latest)  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.2  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Telco Automation V1 API class Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.

REST client for the TelcoAutomation service.

TelcoAutomation Service manages the control plane cluster a.k.a. Orchestration Cluster (GKE cluster with config controller) of TNA. It also exposes blueprint APIs which manages the lifecycle of blueprints that control the infrastructure setup (e.g GDCE clusters) and deployment of network functions.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the TelcoAutomation Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Client-Configuration "Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all TelcoAutomation clients
    ::Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #apply_deployment
    
    
    def apply_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment
    def apply_deployment(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Applies the deployment's YAML files to the parent orchestration cluster.

**Overloads**
    
    
    def apply_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Pass arguments to `apply_deployment` via a request object, either of type [ApplyDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ApplyDeploymentRequest "Google::Cloud::TelcoAutomation::V1::ApplyDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ApplyDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ApplyDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def apply_deployment(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Pass arguments to `apply_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the deployment to apply to orchestration cluster. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ApplyDeploymentRequest.new
    
    # Call the apply_deployment method.
    result = client.apply_deployment request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::Deployment.
    p result

### #apply_hydrated_deployment
    
    
    def apply_hydrated_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment
    def apply_hydrated_deployment(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment

Applies a hydrated deployment to a workload cluster.

**Overloads**
    
    
    def apply_hydrated_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment

Pass arguments to `apply_hydrated_deployment` via a request object, either of type [ApplyHydratedDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ApplyHydratedDeploymentRequest "Google::Cloud::TelcoAutomation::V1::ApplyHydratedDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ApplyHydratedDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ApplyHydratedDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def apply_hydrated_deployment(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment

Pass arguments to `apply_hydrated_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the hydrated deployment to apply. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::HydratedDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-HydratedDeployment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::HydratedDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-HydratedDeployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ApplyHydratedDeploymentRequest.new
    
    # Call the apply_hydrated_deployment method.
    result = client.apply_hydrated_deployment request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::HydratedDeployment.
    p result

### #approve_blueprint
    
    
    def approve_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint
    def approve_blueprint(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Approves a blueprint and commits a new revision.

**Overloads**
    
    
    def approve_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Pass arguments to `approve_blueprint` via a request object, either of type [ApproveBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ApproveBlueprintRequest "Google::Cloud::TelcoAutomation::V1::ApproveBlueprintRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ApproveBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ApproveBlueprintRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def approve_blueprint(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Pass arguments to `approve_blueprint` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the blueprint to approve. The blueprint must be in Proposed state. A new revision is committed on approval. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ApproveBlueprintRequest.new
    
    # Call the approve_blueprint method.
    result = client.approve_blueprint request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::Blueprint.
    p result

### #compute_deployment_status
    
    
    def compute_deployment_status(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::ComputeDeploymentStatusResponse
    def compute_deployment_status(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::ComputeDeploymentStatusResponse

Returns the requested deployment status.

**Overloads**
    
    
    def compute_deployment_status(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::ComputeDeploymentStatusResponse

Pass arguments to `compute_deployment_status` via a request object, either of type [ComputeDeploymentStatusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ComputeDeploymentStatusRequest "Google::Cloud::TelcoAutomation::V1::ComputeDeploymentStatusRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ComputeDeploymentStatusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ComputeDeploymentStatusRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def compute_deployment_status(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::ComputeDeploymentStatusResponse

Pass arguments to `compute_deployment_status` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the deployment without revisionID. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::ComputeDeploymentStatusResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ComputeDeploymentStatusResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::ComputeDeploymentStatusResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ComputeDeploymentStatusResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ComputeDeploymentStatusRequest.new
    
    # Call the compute_deployment_status method.
    result = client.compute_deployment_status request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::ComputeDeploymentStatusResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the TelcoAutomation Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Client#Google__Cloud__TelcoAutomation__V1__TelcoAutomation__Rest__Client_configure_class_ "Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Client-Configuration "Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Client-Configuration)) 



### #create_blueprint
    
    
    def create_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint
    def create_blueprint(parent: nil, blueprint_id: nil, blueprint: nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Creates a blueprint.

**Overloads**
    
    
    def create_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Pass arguments to `create_blueprint` via a request object, either of type [CreateBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-CreateBlueprintRequest "Google::Cloud::TelcoAutomation::V1::CreateBlueprintRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::CreateBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-CreateBlueprintRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_blueprint(parent: nil, blueprint_id: nil, blueprint: nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Pass arguments to `create_blueprint` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of parent resource. Format should be - "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}". 
  * **blueprint_id** (::String) — Optional. The name of the blueprint. 
  * **blueprint** ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint), ::Hash) — Required. The `Blueprint` to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::CreateBlueprintRequest.new
    
    # Call the create_blueprint method.
    result = client.create_blueprint request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::Blueprint.
    p result

### #create_deployment
    
    
    def create_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment
    def create_deployment(parent: nil, deployment_id: nil, deployment: nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Creates a deployment.

**Overloads**
    
    
    def create_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Pass arguments to `create_deployment` via a request object, either of type [CreateDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-CreateDeploymentRequest "Google::Cloud::TelcoAutomation::V1::CreateDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::CreateDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-CreateDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_deployment(parent: nil, deployment_id: nil, deployment: nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Pass arguments to `create_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of parent resource. Format should be - "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}". 
  * **deployment_id** (::String) — Optional. The name of the deployment. 
  * **deployment** ([::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment), ::Hash) — Required. The `Deployment` to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::CreateDeploymentRequest.new
    
    # Call the create_deployment method.
    result = client.create_deployment request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::Deployment.
    p result

### #create_edge_slm
    
    
    def create_edge_slm(request, options = nil) -> ::Gapic::Operation
    def create_edge_slm(parent: nil, edge_slm_id: nil, edge_slm: nil, request_id: nil) -> ::Gapic::Operation

Creates a new EdgeSlm in a given project and location.

**Overloads**
    
    
    def create_edge_slm(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_edge_slm` via a request object, either of type [CreateEdgeSlmRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-CreateEdgeSlmRequest "Google::Cloud::TelcoAutomation::V1::CreateEdgeSlmRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::CreateEdgeSlmRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-CreateEdgeSlmRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_edge_slm(parent: nil, edge_slm_id: nil, edge_slm: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_edge_slm` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Value for parent. 
  * **edge_slm_id** (::String) — Required. Id of the requesting object If auto-generating Id server-side, remove this field and edge_slm_id from the method_signature of Create RPC 
  * **edge_slm** ([::Google::Cloud::TelcoAutomation::V1::EdgeSlm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-EdgeSlm), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::CreateEdgeSlmRequest.new
    
    # Call the create_edge_slm method.
    result = client.create_edge_slm request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_orchestration_cluster
    
    
    def create_orchestration_cluster(request, options = nil) -> ::Gapic::Operation
    def create_orchestration_cluster(parent: nil, orchestration_cluster_id: nil, orchestration_cluster: nil, request_id: nil) -> ::Gapic::Operation

Creates a new OrchestrationCluster in a given project and location.

**Overloads**
    
    
    def create_orchestration_cluster(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_orchestration_cluster` via a request object, either of type [CreateOrchestrationClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-CreateOrchestrationClusterRequest "Google::Cloud::TelcoAutomation::V1::CreateOrchestrationClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::CreateOrchestrationClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-CreateOrchestrationClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_orchestration_cluster(parent: nil, orchestration_cluster_id: nil, orchestration_cluster: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_orchestration_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Value for parent. 
  * **orchestration_cluster_id** (::String) — Required. Id of the requesting object If auto-generating Id server-side, remove this field and orchestration_cluster_id from the method_signature of Create RPC 
  * **orchestration_cluster** ([::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-OrchestrationCluster), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::CreateOrchestrationClusterRequest.new
    
    # Call the create_orchestration_cluster method.
    result = client.create_orchestration_cluster request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_blueprint
    
    
    def delete_blueprint(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_blueprint(name: nil) -> ::Google::Protobuf::Empty

Deletes a blueprint and all its revisions.

**Overloads**
    
    
    def delete_blueprint(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_blueprint` via a request object, either of type [DeleteBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DeleteBlueprintRequest "Google::Cloud::TelcoAutomation::V1::DeleteBlueprintRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::DeleteBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DeleteBlueprintRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_blueprint(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_blueprint` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of blueprint to delete. Blueprint name should be in the format {blueprint_id}, if {blueprint_id}@{revision_id} is passed then the API throws invalid argument. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::DeleteBlueprintRequest.new
    
    # Call the delete_blueprint method.
    result = client.delete_blueprint request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_edge_slm
    
    
    def delete_edge_slm(request, options = nil) -> ::Gapic::Operation
    def delete_edge_slm(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single EdgeSlm.

**Overloads**
    
    
    def delete_edge_slm(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_edge_slm` via a request object, either of type [DeleteEdgeSlmRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DeleteEdgeSlmRequest "Google::Cloud::TelcoAutomation::V1::DeleteEdgeSlmRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::DeleteEdgeSlmRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DeleteEdgeSlmRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_edge_slm(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_edge_slm` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::DeleteEdgeSlmRequest.new
    
    # Call the delete_edge_slm method.
    result = client.delete_edge_slm request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_orchestration_cluster
    
    
    def delete_orchestration_cluster(request, options = nil) -> ::Gapic::Operation
    def delete_orchestration_cluster(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single OrchestrationCluster.

**Overloads**
    
    
    def delete_orchestration_cluster(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_orchestration_cluster` via a request object, either of type [DeleteOrchestrationClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DeleteOrchestrationClusterRequest "Google::Cloud::TelcoAutomation::V1::DeleteOrchestrationClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::DeleteOrchestrationClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DeleteOrchestrationClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_orchestration_cluster(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_orchestration_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::DeleteOrchestrationClusterRequest.new
    
    # Call the delete_orchestration_cluster method.
    result = client.delete_orchestration_cluster request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #discard_blueprint_changes
    
    
    def discard_blueprint_changes(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::DiscardBlueprintChangesResponse
    def discard_blueprint_changes(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::DiscardBlueprintChangesResponse

Discards the changes in a blueprint and reverts the blueprint to the last approved blueprint revision. No changes take place if a blueprint does not have revisions.

**Overloads**
    
    
    def discard_blueprint_changes(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::DiscardBlueprintChangesResponse

Pass arguments to `discard_blueprint_changes` via a request object, either of type [DiscardBlueprintChangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DiscardBlueprintChangesRequest "Google::Cloud::TelcoAutomation::V1::DiscardBlueprintChangesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::DiscardBlueprintChangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DiscardBlueprintChangesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def discard_blueprint_changes(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::DiscardBlueprintChangesResponse

Pass arguments to `discard_blueprint_changes` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the blueprint of which changes are being discarded. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::DiscardBlueprintChangesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DiscardBlueprintChangesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::DiscardBlueprintChangesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DiscardBlueprintChangesResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::DiscardBlueprintChangesRequest.new
    
    # Call the discard_blueprint_changes method.
    result = client.discard_blueprint_changes request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::DiscardBlueprintChangesResponse.
    p result

### #discard_deployment_changes
    
    
    def discard_deployment_changes(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::DiscardDeploymentChangesResponse
    def discard_deployment_changes(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::DiscardDeploymentChangesResponse

Discards the changes in a deployment and reverts the deployment to the last approved deployment revision. No changes take place if a deployment does not have revisions.

**Overloads**
    
    
    def discard_deployment_changes(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::DiscardDeploymentChangesResponse

Pass arguments to `discard_deployment_changes` via a request object, either of type [DiscardDeploymentChangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DiscardDeploymentChangesRequest "Google::Cloud::TelcoAutomation::V1::DiscardDeploymentChangesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::DiscardDeploymentChangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DiscardDeploymentChangesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def discard_deployment_changes(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::DiscardDeploymentChangesResponse

Pass arguments to `discard_deployment_changes` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the deployment of which changes are being discarded. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::DiscardDeploymentChangesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DiscardDeploymentChangesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::DiscardDeploymentChangesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DiscardDeploymentChangesResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::DiscardDeploymentChangesRequest.new
    
    # Call the discard_deployment_changes method.
    result = client.discard_deployment_changes request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::DiscardDeploymentChangesResponse.
    p result

### #get_blueprint
    
    
    def get_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint
    def get_blueprint(name: nil, view: nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Returns the requested blueprint.

**Overloads**
    
    
    def get_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Pass arguments to `get_blueprint` via a request object, either of type [GetBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-GetBlueprintRequest "Google::Cloud::TelcoAutomation::V1::GetBlueprintRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::GetBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-GetBlueprintRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_blueprint(name: nil, view: nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Pass arguments to `get_blueprint` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the blueprint. Case 1: If the name provided in the request is {blueprint_id}@{revision_id}, then the revision with revision_id will be returned. Case 2: If the name provided in the request is {blueprint}, then the current state of the blueprint is returned. 
  * **view** ([::Google::Cloud::TelcoAutomation::V1::BlueprintView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-BlueprintView)) — Optional. Defines the type of view of the blueprint. When field is not present BLUEPRINT_VIEW_BASIC is considered as default. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::GetBlueprintRequest.new
    
    # Call the get_blueprint method.
    result = client.get_blueprint request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::Blueprint.
    p result

### #get_deployment
    
    
    def get_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment
    def get_deployment(name: nil, view: nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Returns the requested deployment.

**Overloads**
    
    
    def get_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Pass arguments to `get_deployment` via a request object, either of type [GetDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-GetDeploymentRequest "Google::Cloud::TelcoAutomation::V1::GetDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::GetDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-GetDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_deployment(name: nil, view: nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Pass arguments to `get_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the deployment. Case 1: If the name provided in the request is {deployment_id}@{revision_id}, then the revision with revision_id will be returned. Case 2: If the name provided in the request is {deployment}, then the current state of the deployment is returned. 
  * **view** ([::Google::Cloud::TelcoAutomation::V1::DeploymentView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-DeploymentView)) — Optional. Defines the type of view of the deployment. When field is not present VIEW_BASIC is considered as default. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::GetDeploymentRequest.new
    
    # Call the get_deployment method.
    result = client.get_deployment request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::Deployment.
    p result

### #get_edge_slm
    
    
    def get_edge_slm(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::EdgeSlm
    def get_edge_slm(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::EdgeSlm

Gets details of a single EdgeSlm.

**Overloads**
    
    
    def get_edge_slm(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::EdgeSlm

Pass arguments to `get_edge_slm` via a request object, either of type [GetEdgeSlmRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-GetEdgeSlmRequest "Google::Cloud::TelcoAutomation::V1::GetEdgeSlmRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::GetEdgeSlmRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-GetEdgeSlmRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_edge_slm(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::EdgeSlm

Pass arguments to `get_edge_slm` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::EdgeSlm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-EdgeSlm)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::EdgeSlm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-EdgeSlm)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::GetEdgeSlmRequest.new
    
    # Call the get_edge_slm method.
    result = client.get_edge_slm request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::EdgeSlm.
    p result

### #get_hydrated_deployment
    
    
    def get_hydrated_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment
    def get_hydrated_deployment(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment

Returns the requested hydrated deployment.

**Overloads**
    
    
    def get_hydrated_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment

Pass arguments to `get_hydrated_deployment` via a request object, either of type [GetHydratedDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-GetHydratedDeploymentRequest "Google::Cloud::TelcoAutomation::V1::GetHydratedDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::GetHydratedDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-GetHydratedDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_hydrated_deployment(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment

Pass arguments to `get_hydrated_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the hydrated deployment. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::HydratedDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-HydratedDeployment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::HydratedDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-HydratedDeployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::GetHydratedDeploymentRequest.new
    
    # Call the get_hydrated_deployment method.
    result = client.get_hydrated_deployment request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::HydratedDeployment.
    p result

### #get_orchestration_cluster
    
    
    def get_orchestration_cluster(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster
    def get_orchestration_cluster(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster

Gets details of a single OrchestrationCluster.

**Overloads**
    
    
    def get_orchestration_cluster(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster

Pass arguments to `get_orchestration_cluster` via a request object, either of type [GetOrchestrationClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-GetOrchestrationClusterRequest "Google::Cloud::TelcoAutomation::V1::GetOrchestrationClusterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::GetOrchestrationClusterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-GetOrchestrationClusterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_orchestration_cluster(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster

Pass arguments to `get_orchestration_cluster` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-OrchestrationCluster)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-OrchestrationCluster)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::GetOrchestrationClusterRequest.new
    
    # Call the get_orchestration_cluster method.
    result = client.get_orchestration_cluster request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::OrchestrationCluster.
    p result

### #get_public_blueprint
    
    
    def get_public_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::PublicBlueprint
    def get_public_blueprint(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::PublicBlueprint

Returns the requested public blueprint.

**Overloads**
    
    
    def get_public_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::PublicBlueprint

Pass arguments to `get_public_blueprint` via a request object, either of type [GetPublicBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-GetPublicBlueprintRequest "Google::Cloud::TelcoAutomation::V1::GetPublicBlueprintRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::GetPublicBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-GetPublicBlueprintRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_public_blueprint(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::PublicBlueprint

Pass arguments to `get_public_blueprint` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the public blueprint. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::PublicBlueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-PublicBlueprint)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::PublicBlueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-PublicBlueprint)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::GetPublicBlueprintRequest.new
    
    # Call the get_public_blueprint method.
    result = client.get_public_blueprint request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::PublicBlueprint.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new TelcoAutomation REST client object.

**Yields**

  * (config) — Configure the TelcoAutomation client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_blueprint_revisions
    
    
    def list_blueprint_revisions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Blueprint>
    def list_blueprint_revisions(name: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Blueprint>

List blueprint revisions of a given blueprint.

**Overloads**
    
    
    def list_blueprint_revisions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Blueprint>

Pass arguments to `list_blueprint_revisions` via a request object, either of type [ListBlueprintRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListBlueprintRevisionsRequest "Google::Cloud::TelcoAutomation::V1::ListBlueprintRevisionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ListBlueprintRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListBlueprintRevisionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_blueprint_revisions(name: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Blueprint>

Pass arguments to `list_blueprint_revisions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the blueprint to list revisions for. 
  * **page_size** (::Integer) — The maximum number of revisions to return per page. 
  * **page_token** (::String) — The page token, received from a previous ListBlueprintRevisions call It can be provided to retrieve the subsequent page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ListBlueprintRevisionsRequest.new
    
    # Call the list_blueprint_revisions method.
    result = client.list_blueprint_revisions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::TelcoAutomation::V1::Blueprint.
      p item
    end

### #list_blueprints
    
    
    def list_blueprints(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Blueprint>
    def list_blueprints(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Blueprint>

List all blueprints.

**Overloads**
    
    
    def list_blueprints(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Blueprint>

Pass arguments to `list_blueprints` via a request object, either of type [ListBlueprintsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListBlueprintsRequest "Google::Cloud::TelcoAutomation::V1::ListBlueprintsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ListBlueprintsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListBlueprintsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_blueprints(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Blueprint>

Pass arguments to `list_blueprints` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of parent orchestration cluster resource. Format should be - "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}". 
  * **filter** (::String) — Optional. Filtering only supports equality on blueprint state. It should be in the form: "state = DRAFT". `OR` operator can be used to get response for multiple states. e.g. "state = DRAFT OR state = PROPOSED". 
  * **page_size** (::Integer) — Optional. The maximum number of blueprints to return per page. 
  * **page_token** (::String) — Optional. The page token, received from a previous ListBlueprints call. It can be provided to retrieve the subsequent page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ListBlueprintsRequest.new
    
    # Call the list_blueprints method.
    result = client.list_blueprints request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::TelcoAutomation::V1::Blueprint.
      p item
    end

### #list_deployment_revisions
    
    
    def list_deployment_revisions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Deployment>
    def list_deployment_revisions(name: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Deployment>

List deployment revisions of a given deployment.

**Overloads**
    
    
    def list_deployment_revisions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Deployment>

Pass arguments to `list_deployment_revisions` via a request object, either of type [ListDeploymentRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListDeploymentRevisionsRequest "Google::Cloud::TelcoAutomation::V1::ListDeploymentRevisionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ListDeploymentRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListDeploymentRevisionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_deployment_revisions(name: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Deployment>

Pass arguments to `list_deployment_revisions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the deployment to list revisions for. 
  * **page_size** (::Integer) — Optional. The maximum number of revisions to return per page. 
  * **page_token** (::String) — Optional. The page token, received from a previous ListDeploymentRevisions call Provide this to retrieve the subsequent page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ListDeploymentRevisionsRequest.new
    
    # Call the list_deployment_revisions method.
    result = client.list_deployment_revisions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::TelcoAutomation::V1::Deployment.
      p item
    end

### #list_deployments
    
    
    def list_deployments(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Deployment>
    def list_deployments(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Deployment>

List all deployments.

**Overloads**
    
    
    def list_deployments(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Deployment>

Pass arguments to `list_deployments` via a request object, either of type [ListDeploymentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListDeploymentsRequest "Google::Cloud::TelcoAutomation::V1::ListDeploymentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ListDeploymentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListDeploymentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_deployments(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Deployment>

Pass arguments to `list_deployments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of parent orchestration cluster resource. Format should be - "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}". 
  * **filter** (::String) — Optional. Filtering only supports equality on deployment state. It should be in the form: "state = DRAFT". `OR` operator can be used to get response for multiple states. e.g. "state = DRAFT OR state = APPLIED". 
  * **page_size** (::Integer) — Optional. The maximum number of deployments to return per page. 
  * **page_token** (::String) — Optional. The page token, received from a previous ListDeployments call. It can be provided to retrieve the subsequent page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ListDeploymentsRequest.new
    
    # Call the list_deployments method.
    result = client.list_deployments request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::TelcoAutomation::V1::Deployment.
      p item
    end

### #list_edge_slms
    
    
    def list_edge_slms(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::EdgeSlm>
    def list_edge_slms(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::EdgeSlm>

Lists EdgeSlms in a given project and location.

**Overloads**
    
    
    def list_edge_slms(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::EdgeSlm>

Pass arguments to `list_edge_slms` via a request object, either of type [ListEdgeSlmsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListEdgeSlmsRequest "Google::Cloud::TelcoAutomation::V1::ListEdgeSlmsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ListEdgeSlmsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListEdgeSlmsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_edge_slms(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::EdgeSlm>

Pass arguments to `list_edge_slms` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListEdgeSlmsRequest 
  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **filter** (::String) — Filtering results 
  * **order_by** (::String) — Hint for how to order the results 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::EdgeSlm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-EdgeSlm)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::EdgeSlm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-EdgeSlm)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ListEdgeSlmsRequest.new
    
    # Call the list_edge_slms method.
    result = client.list_edge_slms request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::TelcoAutomation::V1::EdgeSlm.
      p item
    end

### #list_hydrated_deployments
    
    
    def list_hydrated_deployments(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::HydratedDeployment>
    def list_hydrated_deployments(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::HydratedDeployment>

List all hydrated deployments present under a deployment.

**Overloads**
    
    
    def list_hydrated_deployments(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::HydratedDeployment>

Pass arguments to `list_hydrated_deployments` via a request object, either of type [ListHydratedDeploymentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListHydratedDeploymentsRequest "Google::Cloud::TelcoAutomation::V1::ListHydratedDeploymentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ListHydratedDeploymentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListHydratedDeploymentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_hydrated_deployments(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::HydratedDeployment>

Pass arguments to `list_hydrated_deployments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The deployment managing the hydrated deployments. 
  * **page_size** (::Integer) — Optional. The maximum number of hydrated deployments to return. The service may return fewer than this value. If unspecified, at most 50 hydrated deployments will be returned. The maximum value is 1000. Values above 1000 will be set to 1000. 
  * **page_token** (::String) — Optional. The page token, received from a previous ListHydratedDeployments call. Provide this to retrieve the subsequent page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::HydratedDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-HydratedDeployment)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::HydratedDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-HydratedDeployment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ListHydratedDeploymentsRequest.new
    
    # Call the list_hydrated_deployments method.
    result = client.list_hydrated_deployments request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment.
      p item
    end

### #list_orchestration_clusters
    
    
    def list_orchestration_clusters(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster>
    def list_orchestration_clusters(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster>

Lists OrchestrationClusters in a given project and location.

**Overloads**
    
    
    def list_orchestration_clusters(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster>

Pass arguments to `list_orchestration_clusters` via a request object, either of type [ListOrchestrationClustersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListOrchestrationClustersRequest "Google::Cloud::TelcoAutomation::V1::ListOrchestrationClustersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ListOrchestrationClustersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListOrchestrationClustersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_orchestration_clusters(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster>

Pass arguments to `list_orchestration_clusters` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListOrchestrationClustersRequest 
  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **filter** (::String) — Filtering results. 
  * **order_by** (::String) — Hint for how to order the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-OrchestrationCluster)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-OrchestrationCluster)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ListOrchestrationClustersRequest.new
    
    # Call the list_orchestration_clusters method.
    result = client.list_orchestration_clusters request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::TelcoAutomation::V1::OrchestrationCluster.
      p item
    end

### #list_public_blueprints
    
    
    def list_public_blueprints(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::PublicBlueprint>
    def list_public_blueprints(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::PublicBlueprint>

Lists the blueprints in TNA's public catalog. Default page size = 20, Max Page Size = 100.

**Overloads**
    
    
    def list_public_blueprints(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::PublicBlueprint>

Pass arguments to `list_public_blueprints` via a request object, either of type [ListPublicBlueprintsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListPublicBlueprintsRequest "Google::Cloud::TelcoAutomation::V1::ListPublicBlueprintsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ListPublicBlueprintsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ListPublicBlueprintsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_public_blueprints(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::PublicBlueprint>

Pass arguments to `list_public_blueprints` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value of public blueprint. Format should be - "projects/{project_id}/locations/{location_name}". 
  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::PublicBlueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-PublicBlueprint)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::PublicBlueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-PublicBlueprint)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ListPublicBlueprintsRequest.new
    
    # Call the list_public_blueprints method.
    result = client.list_public_blueprints request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::TelcoAutomation::V1::PublicBlueprint.
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
    
    
    def operations_client() -> ::Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Operations)) 



### #propose_blueprint
    
    
    def propose_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint
    def propose_blueprint(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Proposes a blueprint for approval of changes.

**Overloads**
    
    
    def propose_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Pass arguments to `propose_blueprint` via a request object, either of type [ProposeBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ProposeBlueprintRequest "Google::Cloud::TelcoAutomation::V1::ProposeBlueprintRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::ProposeBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-ProposeBlueprintRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def propose_blueprint(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Pass arguments to `propose_blueprint` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the blueprint being proposed. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::ProposeBlueprintRequest.new
    
    # Call the propose_blueprint method.
    result = client.propose_blueprint request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::Blueprint.
    p result

### #reject_blueprint
    
    
    def reject_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint
    def reject_blueprint(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Rejects a blueprint revision proposal and flips it back to Draft state.

**Overloads**
    
    
    def reject_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Pass arguments to `reject_blueprint` via a request object, either of type [RejectBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-RejectBlueprintRequest "Google::Cloud::TelcoAutomation::V1::RejectBlueprintRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::RejectBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-RejectBlueprintRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def reject_blueprint(name: nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Pass arguments to `reject_blueprint` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the blueprint being rejected. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::RejectBlueprintRequest.new
    
    # Call the reject_blueprint method.
    result = client.reject_blueprint request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::Blueprint.
    p result

### #remove_deployment
    
    
    def remove_deployment(request, options = nil) -> ::Google::Protobuf::Empty
    def remove_deployment(name: nil) -> ::Google::Protobuf::Empty

Removes the deployment by marking it as DELETING. Post which deployment and it's revisions gets deleted.

**Overloads**
    
    
    def remove_deployment(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `remove_deployment` via a request object, either of type [RemoveDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-RemoveDeploymentRequest "Google::Cloud::TelcoAutomation::V1::RemoveDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::RemoveDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-RemoveDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def remove_deployment(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `remove_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of deployment to initiate delete. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::RemoveDeploymentRequest.new
    
    # Call the remove_deployment method.
    result = client.remove_deployment request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #rollback_deployment
    
    
    def rollback_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment
    def rollback_deployment(name: nil, revision_id: nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Rollback the active deployment to the given past approved deployment revision.

**Overloads**
    
    
    def rollback_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Pass arguments to `rollback_deployment` via a request object, either of type [RollbackDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-RollbackDeploymentRequest "Google::Cloud::TelcoAutomation::V1::RollbackDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::RollbackDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-RollbackDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def rollback_deployment(name: nil, revision_id: nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Pass arguments to `rollback_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the deployment. 
  * **revision_id** (::String) — Required. The revision id of deployment to roll back to. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::RollbackDeploymentRequest.new
    
    # Call the rollback_deployment method.
    result = client.rollback_deployment request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::Deployment.
    p result

### #search_blueprint_revisions
    
    
    def search_blueprint_revisions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Blueprint>
    def search_blueprint_revisions(parent: nil, query: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Blueprint>

Searches across blueprint revisions.

**Overloads**
    
    
    def search_blueprint_revisions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Blueprint>

Pass arguments to `search_blueprint_revisions` via a request object, either of type [SearchBlueprintRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-SearchBlueprintRevisionsRequest "Google::Cloud::TelcoAutomation::V1::SearchBlueprintRevisionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::SearchBlueprintRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-SearchBlueprintRevisionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def search_blueprint_revisions(parent: nil, query: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Blueprint>

Pass arguments to `search_blueprint_revisions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of parent orchestration cluster resource. Format should be - "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}". 
  * **query** (::String) — 

Required. Supported queries:

    1. "" : Lists all revisions across all blueprints.
    2. "latest=true" : Lists latest revisions across all blueprints.
    3. "name={name}" : Lists all revisions of blueprint with name {name}.
    4. "name={name} latest=true": Lists latest revision of blueprint with name {name}
  * **page_size** (::Integer) — Optional. The maximum number of blueprints revisions to return per page. max page size = 100, default page size = 20. 
  * **page_token** (::String) — Optional. The page token, received from a previous search call. It can be provided to retrieve the subsequent page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::SearchBlueprintRevisionsRequest.new
    
    # Call the search_blueprint_revisions method.
    result = client.search_blueprint_revisions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::TelcoAutomation::V1::Blueprint.
      p item
    end

### #search_deployment_revisions
    
    
    def search_deployment_revisions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Deployment>
    def search_deployment_revisions(parent: nil, query: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Deployment>

Searches across deployment revisions.

**Overloads**
    
    
    def search_deployment_revisions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Deployment>

Pass arguments to `search_deployment_revisions` via a request object, either of type [SearchDeploymentRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-SearchDeploymentRevisionsRequest "Google::Cloud::TelcoAutomation::V1::SearchDeploymentRevisionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::SearchDeploymentRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-SearchDeploymentRevisionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def search_deployment_revisions(parent: nil, query: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::TelcoAutomation::V1::Deployment>

Pass arguments to `search_deployment_revisions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of parent orchestration cluster resource. Format should be - "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}". 
  * **query** (::String) — 

Required. Supported queries:

    1. "" : Lists all revisions across all deployments.
    2. "latest=true" : Lists latest revisions across all deployments.
    3. "name={name}" : Lists all revisions of deployment with name {name}.
    4. "name={name} latest=true": Lists latest revision of deployment with name {name}
  * **page_size** (::Integer) — Optional. The maximum number of deployment revisions to return per page. max page size = 100, default page size = 20. 
  * **page_token** (::String) — Optional. The page token, received from a previous search call. It can be provided to retrieve the subsequent page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::SearchDeploymentRevisionsRequest.new
    
    # Call the search_deployment_revisions method.
    result = client.search_deployment_revisions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::TelcoAutomation::V1::Deployment.
      p item
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_blueprint
    
    
    def update_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint
    def update_blueprint(blueprint: nil, update_mask: nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Updates a blueprint.

**Overloads**
    
    
    def update_blueprint(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Pass arguments to `update_blueprint` via a request object, either of type [UpdateBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-UpdateBlueprintRequest "Google::Cloud::TelcoAutomation::V1::UpdateBlueprintRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::UpdateBlueprintRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-UpdateBlueprintRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_blueprint(blueprint: nil, update_mask: nil) -> ::Google::Cloud::TelcoAutomation::V1::Blueprint

Pass arguments to `update_blueprint` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **blueprint** ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint), ::Hash) — Required. The `blueprint` to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Update mask is used to specify the fields to be overwritten in the `blueprint` resource by the update. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::Blueprint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Blueprint)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::UpdateBlueprintRequest.new
    
    # Call the update_blueprint method.
    result = client.update_blueprint request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::Blueprint.
    p result

### #update_deployment
    
    
    def update_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment
    def update_deployment(deployment: nil, update_mask: nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Updates a deployment.

**Overloads**
    
    
    def update_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Pass arguments to `update_deployment` via a request object, either of type [UpdateDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-UpdateDeploymentRequest "Google::Cloud::TelcoAutomation::V1::UpdateDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::UpdateDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-UpdateDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_deployment(deployment: nil, update_mask: nil) -> ::Google::Cloud::TelcoAutomation::V1::Deployment

Pass arguments to `update_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **deployment** ([::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment), ::Hash) — Required. The `deployment` to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Update mask is used to specify the fields to be overwritten in the `deployment` resource by the update. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::Deployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-Deployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::UpdateDeploymentRequest.new
    
    # Call the update_deployment method.
    result = client.update_deployment request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::Deployment.
    p result

### #update_hydrated_deployment
    
    
    def update_hydrated_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment
    def update_hydrated_deployment(hydrated_deployment: nil, update_mask: nil) -> ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment

Updates a hydrated deployment.

**Overloads**
    
    
    def update_hydrated_deployment(request, options = nil) -> ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment

Pass arguments to `update_hydrated_deployment` via a request object, either of type [UpdateHydratedDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-UpdateHydratedDeploymentRequest "Google::Cloud::TelcoAutomation::V1::UpdateHydratedDeploymentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::TelcoAutomation::V1::UpdateHydratedDeploymentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-UpdateHydratedDeploymentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_hydrated_deployment(hydrated_deployment: nil, update_mask: nil) -> ::Google::Cloud::TelcoAutomation::V1::HydratedDeployment

Pass arguments to `update_hydrated_deployment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **hydrated_deployment** ([::Google::Cloud::TelcoAutomation::V1::HydratedDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-HydratedDeployment), ::Hash) — Required. The hydrated deployment to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The list of fields to update. Update mask supports a special value `*` which fully replaces (equivalent to PUT) the resource provided. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::TelcoAutomation::V1::HydratedDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-HydratedDeployment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::TelcoAutomation::V1::HydratedDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-HydratedDeployment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/telco_automation/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::TelcoAutomation::V1::UpdateHydratedDeploymentRequest.new
    
    # Call the update_hydrated_deployment method.
    result = client.update_hydrated_deployment request
    
    # The returned object is of type Google::Cloud::TelcoAutomation::V1::HydratedDeployment.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
