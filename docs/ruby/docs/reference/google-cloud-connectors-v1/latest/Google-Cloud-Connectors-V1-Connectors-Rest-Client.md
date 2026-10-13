---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Rest-Client/
title: Connectors V1 API - Class Google::Cloud::Connectors::V1::Connectors::Rest::Client (v1.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:20:11.276220+00:00
---

# Connectors V1 API - Class Google::Cloud::Connectors::V1::Connectors::Rest::Client (v1.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Connectors V1 API - Class Google::Cloud::Connectors::V1::Connectors::Rest::Client (v1.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.1 (latest)  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Connectors V1 API class Google::Cloud::Connectors::V1::Connectors::Rest::Client.

REST client for the Connectors service.

Connectors is the interface for managing Connectors.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Connectors::V1::Connectors::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Connectors Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Rest-Client-Configuration "Google::Cloud::Connectors::V1::Connectors::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Connectors clients
    ::Google::Cloud::Connectors::V1::Connectors::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Connectors Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Rest-Client#Google__Cloud__Connectors__V1__Connectors__Rest__Client_configure_class_ "Google::Cloud::Connectors::V1::Connectors::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Rest-Client-Configuration "Google::Cloud::Connectors::V1::Connectors::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Rest-Client-Configuration)) 



### #create_connection
    
    
    def create_connection(request, options = nil) -> ::Gapic::Operation
    def create_connection(parent: nil, connection_id: nil, connection: nil) -> ::Gapic::Operation

Creates a new Connection in a given project and location.

**Overloads**
    
    
    def create_connection(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_connection` via a request object, either of type [Google::Cloud::Connectors::V1::CreateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-CreateConnectionRequest "Google::Cloud::Connectors::V1::CreateConnectionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::CreateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-CreateConnectionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_connection(parent: nil, connection_id: nil, connection: nil) -> ::Gapic::Operation

Pass arguments to `create_connection` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource of the Connection, of the form: `projects/*/locations/*`
  * **connection_id** (::String) — Required. Identifier to assign to the Connection. Must be unique within scope of the parent resource. 
  * **connection** ([::Google::Cloud::Connectors::V1::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connection), ::Hash) — Required. Connection resource. 



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
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::CreateConnectionRequest.new
    
    # Call the create_connection method.
    result = client.create_connection request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_connection
    
    
    def delete_connection(request, options = nil) -> ::Gapic::Operation
    def delete_connection(name: nil) -> ::Gapic::Operation

Deletes a single Connection.

**Overloads**
    
    
    def delete_connection(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_connection` via a request object, either of type [DeleteConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-DeleteConnectionRequest "Google::Cloud::Connectors::V1::DeleteConnectionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::DeleteConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-DeleteConnectionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_connection(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_connection` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the form: `projects/*/locations/*/connections/*`



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
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::DeleteConnectionRequest.new
    
    # Call the delete_connection method.
    result = client.delete_connection request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_connection
    
    
    def get_connection(request, options = nil) -> ::Google::Cloud::Connectors::V1::Connection
    def get_connection(name: nil, view: nil) -> ::Google::Cloud::Connectors::V1::Connection

Gets details of a single Connection.

**Overloads**
    
    
    def get_connection(request, options = nil) -> ::Google::Cloud::Connectors::V1::Connection

Pass arguments to `get_connection` via a request object, either of type [GetConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetConnectionRequest "Google::Cloud::Connectors::V1::GetConnectionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::GetConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetConnectionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_connection(name: nil, view: nil) -> ::Google::Cloud::Connectors::V1::Connection

Pass arguments to `get_connection` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Resource name of the form: `projects/*/locations/*/connections/*`
  * **view** ([::Google::Cloud::Connectors::V1::ConnectionView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectionView)) — Specifies which fields of the Connection are returned in the response. Defaults to `BASIC` view. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Connectors::V1::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connection)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Connectors::V1::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connection)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::GetConnectionRequest.new
    
    # Call the get_connection method.
    result = client.get_connection request
    
    # The returned object is of type Google::Cloud::Connectors::V1::Connection.
    p result

### #get_connection_schema_metadata
    
    
    def get_connection_schema_metadata(request, options = nil) -> ::Google::Cloud::Connectors::V1::ConnectionSchemaMetadata
    def get_connection_schema_metadata(name: nil) -> ::Google::Cloud::Connectors::V1::ConnectionSchemaMetadata

Gets schema metadata of a connection. SchemaMetadata is a singleton resource for each connection.

**Overloads**
    
    
    def get_connection_schema_metadata(request, options = nil) -> ::Google::Cloud::Connectors::V1::ConnectionSchemaMetadata

Pass arguments to `get_connection_schema_metadata` via a request object, either of type [GetConnectionSchemaMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetConnectionSchemaMetadataRequest "Google::Cloud::Connectors::V1::GetConnectionSchemaMetadataRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::GetConnectionSchemaMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetConnectionSchemaMetadataRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_connection_schema_metadata(name: nil) -> ::Google::Cloud::Connectors::V1::ConnectionSchemaMetadata

Pass arguments to `get_connection_schema_metadata` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Connection name Format: projects/{project}/locations/{location}/connections/{connection}/connectionSchemaMetadata 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Connectors::V1::ConnectionSchemaMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectionSchemaMetadata)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Connectors::V1::ConnectionSchemaMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectionSchemaMetadata)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::GetConnectionSchemaMetadataRequest.new
    
    # Call the get_connection_schema_metadata method.
    result = client.get_connection_schema_metadata request
    
    # The returned object is of type Google::Cloud::Connectors::V1::ConnectionSchemaMetadata.
    p result

### #get_connector
    
    
    def get_connector(request, options = nil) -> ::Google::Cloud::Connectors::V1::Connector
    def get_connector(name: nil) -> ::Google::Cloud::Connectors::V1::Connector

Gets details of a single Connector.

**Overloads**
    
    
    def get_connector(request, options = nil) -> ::Google::Cloud::Connectors::V1::Connector

Pass arguments to `get_connector` via a request object, either of type [GetConnectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetConnectorRequest "Google::Cloud::Connectors::V1::GetConnectorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::GetConnectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetConnectorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_connector(name: nil) -> ::Google::Cloud::Connectors::V1::Connector

Pass arguments to `get_connector` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the form: `projects/*/locations/*/providers/*/connectors/*` Only global location is supported for Connector resource. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Connectors::V1::Connector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connector)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Connectors::V1::Connector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connector)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::GetConnectorRequest.new
    
    # Call the get_connector method.
    result = client.get_connector request
    
    # The returned object is of type Google::Cloud::Connectors::V1::Connector.
    p result

### #get_connector_version
    
    
    def get_connector_version(request, options = nil) -> ::Google::Cloud::Connectors::V1::ConnectorVersion
    def get_connector_version(name: nil, view: nil) -> ::Google::Cloud::Connectors::V1::ConnectorVersion

Gets details of a single connector version.

**Overloads**
    
    
    def get_connector_version(request, options = nil) -> ::Google::Cloud::Connectors::V1::ConnectorVersion

Pass arguments to `get_connector_version` via a request object, either of type [GetConnectorVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetConnectorVersionRequest "Google::Cloud::Connectors::V1::GetConnectorVersionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::GetConnectorVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetConnectorVersionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_connector_version(name: nil, view: nil) -> ::Google::Cloud::Connectors::V1::ConnectorVersion

Pass arguments to `get_connector_version` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Resource name of the form: `projects/*/locations/*/providers/*/connectors/*/versions/*` Only global location is supported for ConnectorVersion resource. 
  * **view** ([::Google::Cloud::Connectors::V1::ConnectorVersionView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectorVersionView)) — Specifies which fields of the ConnectorVersion are returned in the response. Defaults to `CUSTOMER` view. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Connectors::V1::ConnectorVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectorVersion)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Connectors::V1::ConnectorVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectorVersion)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::GetConnectorVersionRequest.new
    
    # Call the get_connector_version method.
    result = client.get_connector_version request
    
    # The returned object is of type Google::Cloud::Connectors::V1::ConnectorVersion.
    p result

### #get_global_settings
    
    
    def get_global_settings(request, options = nil) -> ::Google::Cloud::Connectors::V1::Settings
    def get_global_settings(name: nil) -> ::Google::Cloud::Connectors::V1::Settings

GetGlobalSettings gets settings of a project. GlobalSettings is a singleton resource.

**Overloads**
    
    
    def get_global_settings(request, options = nil) -> ::Google::Cloud::Connectors::V1::Settings

Pass arguments to `get_global_settings` via a request object, either of type [GetGlobalSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetGlobalSettingsRequest "Google::Cloud::Connectors::V1::GetGlobalSettingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::GetGlobalSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetGlobalSettingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_global_settings(name: nil) -> ::Google::Cloud::Connectors::V1::Settings

Pass arguments to `get_global_settings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the Settings. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Connectors::V1::Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Settings)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Connectors::V1::Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Settings)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::GetGlobalSettingsRequest.new
    
    # Call the get_global_settings method.
    result = client.get_global_settings request
    
    # The returned object is of type Google::Cloud::Connectors::V1::Settings.
    p result

### #get_provider
    
    
    def get_provider(request, options = nil) -> ::Google::Cloud::Connectors::V1::Provider
    def get_provider(name: nil) -> ::Google::Cloud::Connectors::V1::Provider

Gets details of a provider.

**Overloads**
    
    
    def get_provider(request, options = nil) -> ::Google::Cloud::Connectors::V1::Provider

Pass arguments to `get_provider` via a request object, either of type [GetProviderRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetProviderRequest "Google::Cloud::Connectors::V1::GetProviderRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::GetProviderRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetProviderRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_provider(name: nil) -> ::Google::Cloud::Connectors::V1::Provider

Pass arguments to `get_provider` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the form: `projects/*/locations/*/providers/*` Only global location is supported for Provider resource. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Connectors::V1::Provider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Provider)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Connectors::V1::Provider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Provider)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::GetProviderRequest.new
    
    # Call the get_provider method.
    result = client.get_provider request
    
    # The returned object is of type Google::Cloud::Connectors::V1::Provider.
    p result

### #get_runtime_config
    
    
    def get_runtime_config(request, options = nil) -> ::Google::Cloud::Connectors::V1::RuntimeConfig
    def get_runtime_config(name: nil) -> ::Google::Cloud::Connectors::V1::RuntimeConfig

Gets the runtimeConfig of a location. RuntimeConfig is a singleton resource for each location.

**Overloads**
    
    
    def get_runtime_config(request, options = nil) -> ::Google::Cloud::Connectors::V1::RuntimeConfig

Pass arguments to `get_runtime_config` via a request object, either of type [GetRuntimeConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetRuntimeConfigRequest "Google::Cloud::Connectors::V1::GetRuntimeConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::GetRuntimeConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-GetRuntimeConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_runtime_config(name: nil) -> ::Google::Cloud::Connectors::V1::RuntimeConfig

Pass arguments to `get_runtime_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the form: `projects/*/locations/*/runtimeConfig`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Connectors::V1::RuntimeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-RuntimeConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Connectors::V1::RuntimeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-RuntimeConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::GetRuntimeConfigRequest.new
    
    # Call the get_runtime_config method.
    result = client.get_runtime_config request
    
    # The returned object is of type Google::Cloud::Connectors::V1::RuntimeConfig.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Connectors REST client object.

**Yields**

  * (config) — Configure the Connectors client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Connectors::V1::Connectors::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_connections
    
    
    def list_connections(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::Connection>
    def list_connections(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, view: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::Connection>

Lists Connections in a given project and location.

**Overloads**
    
    
    def list_connections(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::Connection>

Pass arguments to `list_connections` via a request object, either of type [ListConnectionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListConnectionsRequest "Google::Cloud::Connectors::V1::ListConnectionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::ListConnectionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListConnectionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_connections(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, view: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::Connection>

Pass arguments to `list_connections` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource of the Connection, of the form: `projects/*/locations/*`
  * **page_size** (::Integer) — Page size. 
  * **page_token** (::String) — Page token. 
  * **filter** (::String) — Filter. 
  * **order_by** (::String) — Order by parameters. 
  * **view** ([::Google::Cloud::Connectors::V1::ConnectionView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectionView)) — Specifies which fields of the Connection are returned in the response. Defaults to `BASIC` view. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Connectors::V1::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connection)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Connectors::V1::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connection)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::ListConnectionsRequest.new
    
    # Call the list_connections method.
    result = client.list_connections request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Connectors::V1::Connection.
      p item
    end

### #list_connector_versions
    
    
    def list_connector_versions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::ConnectorVersion>
    def list_connector_versions(parent: nil, page_size: nil, page_token: nil, view: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::ConnectorVersion>

Lists Connector Versions in a given project and location.

**Overloads**
    
    
    def list_connector_versions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::ConnectorVersion>

Pass arguments to `list_connector_versions` via a request object, either of type [ListConnectorVersionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListConnectorVersionsRequest "Google::Cloud::Connectors::V1::ListConnectorVersionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::ListConnectorVersionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListConnectorVersionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_connector_versions(parent: nil, page_size: nil, page_token: nil, view: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::ConnectorVersion>

Pass arguments to `list_connector_versions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource of the connectors, of the form: `projects/*/locations/*/providers/*/connectors/*` Only global location is supported for ConnectorVersion resource. 
  * **page_size** (::Integer) — Page size. 
  * **page_token** (::String) — Page token. 
  * **view** ([::Google::Cloud::Connectors::V1::ConnectorVersionView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectorVersionView)) — Specifies which fields of the ConnectorVersion are returned in the response. Defaults to `BASIC` view. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Connectors::V1::ConnectorVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectorVersion)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Connectors::V1::ConnectorVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectorVersion)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::ListConnectorVersionsRequest.new
    
    # Call the list_connector_versions method.
    result = client.list_connector_versions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Connectors::V1::ConnectorVersion.
      p item
    end

### #list_connectors
    
    
    def list_connectors(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::Connector>
    def list_connectors(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::Connector>

Lists Connectors in a given project and location.

**Overloads**
    
    
    def list_connectors(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::Connector>

Pass arguments to `list_connectors` via a request object, either of type [ListConnectorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListConnectorsRequest "Google::Cloud::Connectors::V1::ListConnectorsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::ListConnectorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListConnectorsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_connectors(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::Connector>

Pass arguments to `list_connectors` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource of the connectors, of the form: `projects/*/locations/*/providers/*` Only global location is supported for Connector resource. 
  * **page_size** (::Integer) — Page size. 
  * **page_token** (::String) — Page token. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Connectors::V1::Connector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connector)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Connectors::V1::Connector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connector)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::ListConnectorsRequest.new
    
    # Call the list_connectors method.
    result = client.list_connectors request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Connectors::V1::Connector.
      p item
    end

### #list_providers
    
    
    def list_providers(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::Provider>
    def list_providers(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::Provider>

Lists Providers in a given project and location.

**Overloads**
    
    
    def list_providers(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::Provider>

Pass arguments to `list_providers` via a request object, either of type [ListProvidersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListProvidersRequest "Google::Cloud::Connectors::V1::ListProvidersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::ListProvidersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListProvidersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_providers(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::Provider>

Pass arguments to `list_providers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource of the API, of the form: `projects/*/locations/*` Only global location is supported for Provider resource. 
  * **page_size** (::Integer) — Page size. 
  * **page_token** (::String) — Page token. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Connectors::V1::Provider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Provider)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Connectors::V1::Provider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Provider)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::ListProvidersRequest.new
    
    # Call the list_providers method.
    result = client.list_providers request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Connectors::V1::Provider.
      p item
    end

### #list_runtime_action_schemas
    
    
    def list_runtime_action_schemas(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::RuntimeActionSchema>
    def list_runtime_action_schemas(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::RuntimeActionSchema>

List schema of a runtime actions filtered by action name.

**Overloads**
    
    
    def list_runtime_action_schemas(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::RuntimeActionSchema>

Pass arguments to `list_runtime_action_schemas` via a request object, either of type [ListRuntimeActionSchemasRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListRuntimeActionSchemasRequest "Google::Cloud::Connectors::V1::ListRuntimeActionSchemasRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::ListRuntimeActionSchemasRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListRuntimeActionSchemasRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_runtime_action_schemas(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::RuntimeActionSchema>

Pass arguments to `list_runtime_action_schemas` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource of RuntimeActionSchema Format: projects/{project}/locations/{location}/connections/{connection} 
  * **page_size** (::Integer) — Page size. 
  * **page_token** (::String) — Page token. 
  * **filter** (::String) — Required. Filter Format: action="{actionId}" Only action field is supported with literal equality operator. Accepted filter example: action="CancelOrder" Wildcards are not supported in the filter currently. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Connectors::V1::RuntimeActionSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-RuntimeActionSchema)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Connectors::V1::RuntimeActionSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-RuntimeActionSchema)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::ListRuntimeActionSchemasRequest.new
    
    # Call the list_runtime_action_schemas method.
    result = client.list_runtime_action_schemas request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Connectors::V1::RuntimeActionSchema.
      p item
    end

### #list_runtime_entity_schemas
    
    
    def list_runtime_entity_schemas(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::RuntimeEntitySchema>
    def list_runtime_entity_schemas(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::RuntimeEntitySchema>

List schema of a runtime entities filtered by entity name.

**Overloads**
    
    
    def list_runtime_entity_schemas(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::RuntimeEntitySchema>

Pass arguments to `list_runtime_entity_schemas` via a request object, either of type [ListRuntimeEntitySchemasRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListRuntimeEntitySchemasRequest "Google::Cloud::Connectors::V1::ListRuntimeEntitySchemasRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::ListRuntimeEntitySchemasRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListRuntimeEntitySchemasRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_runtime_entity_schemas(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Connectors::V1::RuntimeEntitySchema>

Pass arguments to `list_runtime_entity_schemas` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource of RuntimeEntitySchema Format: projects/{project}/locations/{location}/connections/{connection} 
  * **page_size** (::Integer) — Page size. 
  * **page_token** (::String) — Page token. 
  * **filter** (::String) — Required. Filter Format: entity="{entityId}" Only entity field is supported with literal equality operator. Accepted filter example: entity="Order" Wildcards are not supported in the filter currently. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Connectors::V1::RuntimeEntitySchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-RuntimeEntitySchema)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Connectors::V1::RuntimeEntitySchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-RuntimeEntitySchema)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::ListRuntimeEntitySchemasRequest.new
    
    # Call the list_runtime_entity_schemas method.
    result = client.list_runtime_entity_schemas request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Connectors::V1::RuntimeEntitySchema.
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
    
    
    def operations_client() -> ::Google::Cloud::Connectors::V1::Connectors::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Connectors::V1::Connectors::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connectors-Rest-Operations)) 



### #refresh_connection_schema_metadata
    
    
    def refresh_connection_schema_metadata(request, options = nil) -> ::Gapic::Operation
    def refresh_connection_schema_metadata(name: nil) -> ::Gapic::Operation

Refresh runtime schema of a connection.

**Overloads**
    
    
    def refresh_connection_schema_metadata(request, options = nil) -> ::Gapic::Operation

Pass arguments to `refresh_connection_schema_metadata` via a request object, either of type [RefreshConnectionSchemaMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-RefreshConnectionSchemaMetadataRequest "Google::Cloud::Connectors::V1::RefreshConnectionSchemaMetadataRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::RefreshConnectionSchemaMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-RefreshConnectionSchemaMetadataRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def refresh_connection_schema_metadata(name: nil) -> ::Gapic::Operation

Pass arguments to `refresh_connection_schema_metadata` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name. Format: projects/{project}/locations/{location}/connections/{connection}/connectionSchemaMetadata 



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
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::RefreshConnectionSchemaMetadataRequest.new
    
    # Call the refresh_connection_schema_metadata method.
    result = client.refresh_connection_schema_metadata request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_connection
    
    
    def update_connection(request, options = nil) -> ::Gapic::Operation
    def update_connection(connection: nil, update_mask: nil) -> ::Gapic::Operation

Updates the parameters of a single Connection.

**Overloads**
    
    
    def update_connection(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_connection` via a request object, either of type [UpdateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-UpdateConnectionRequest "Google::Cloud::Connectors::V1::UpdateConnectionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Connectors::V1::UpdateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-UpdateConnectionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_connection(connection: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_connection` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **connection** ([::Google::Cloud::Connectors::V1::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connection), ::Hash) — Required. Connection resource. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Protobuf-FieldMask), ::Hash) — 

Required. You can modify only the fields listed below.

To lock/unlock a connection:

    * `lock_config`

To suspend/resume a connection:

    * `suspended`

To update the connection details:

    * `description`
    * `labels`
    * `connector_version`
    * `config_variables`
    * `auth_config`
    * `destination_configs`
    * `node_config`



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
    
    
    require "google/cloud/connectors/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Connectors::V1::Connectors::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Connectors::V1::UpdateConnectionRequest.new
    
    # Call the update_connection method.
    result = client.update_connection request
    
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

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
