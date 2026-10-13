---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Client/
title: Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:38.285253+00:00
---

# Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Network Security V1 API class Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.

Client for the NetworkSecurity service.

Network Security API provides resources to configure authentication and authorization policies. Refer to per API resource documentation for more information.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the NetworkSecurity Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Client-Configuration "Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all NetworkSecurity clients
    ::Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the NetworkSecurity Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Client#Google__Cloud__NetworkSecurity__V1__NetworkSecurity__Client_configure_class_ "Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Client-Configuration "Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Client-Configuration)) 



### #create_authorization_policy
    
    
    def create_authorization_policy(request, options = nil) -> ::Gapic::Operation
    def create_authorization_policy(parent: nil, authorization_policy_id: nil, authorization_policy: nil) -> ::Gapic::Operation

Creates a new AuthorizationPolicy in a given project and location.

**Overloads**
    
    
    def create_authorization_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_authorization_policy` via a request object, either of type [CreateAuthorizationPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateAuthorizationPolicyRequest "Google::Cloud::NetworkSecurity::V1::CreateAuthorizationPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::CreateAuthorizationPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateAuthorizationPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_authorization_policy(parent: nil, authorization_policy_id: nil, authorization_policy: nil) -> ::Gapic::Operation

Pass arguments to `create_authorization_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource of the AuthorizationPolicy. Must be in the format `projects/{project}/locations/{location}`. 
  * **authorization_policy_id** (::String) — Required. Short name of the AuthorizationPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "authz_policy". 
  * **authorization_policy** ([::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthorizationPolicy), ::Hash) — Required. AuthorizationPolicy resource to be created. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::CreateAuthorizationPolicyRequest.new
    
    # Call the create_authorization_policy method.
    result = client.create_authorization_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_authz_policy
    
    
    def create_authz_policy(request, options = nil) -> ::Gapic::Operation
    def create_authz_policy(parent: nil, authz_policy_id: nil, authz_policy: nil, request_id: nil) -> ::Gapic::Operation

Creates a new AuthzPolicy in a given project and location.

**Overloads**
    
    
    def create_authz_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_authz_policy` via a request object, either of type [CreateAuthzPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateAuthzPolicyRequest "Google::Cloud::NetworkSecurity::V1::CreateAuthzPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::CreateAuthzPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateAuthzPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_authz_policy(parent: nil, authz_policy_id: nil, authz_policy: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_authz_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource of the `AuthzPolicy` resource. Must be in the format `projects/{project}/locations/{location}`. 
  * **authz_policy_id** (::String) — Required. User-provided ID of the `AuthzPolicy` resource to be created. 
  * **authz_policy** ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy), ::Hash) — Required. `AuthzPolicy` resource to be created. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server can ignore the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::CreateAuthzPolicyRequest.new
    
    # Call the create_authz_policy method.
    result = client.create_authz_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_backend_authentication_config
    
    
    def create_backend_authentication_config(request, options = nil) -> ::Gapic::Operation
    def create_backend_authentication_config(parent: nil, backend_authentication_config_id: nil, backend_authentication_config: nil) -> ::Gapic::Operation

Creates a new BackendAuthenticationConfig in a given project and location.

**Overloads**
    
    
    def create_backend_authentication_config(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_backend_authentication_config` via a request object, either of type [CreateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateBackendAuthenticationConfigRequest "Google::Cloud::NetworkSecurity::V1::CreateBackendAuthenticationConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::CreateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateBackendAuthenticationConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_backend_authentication_config(parent: nil, backend_authentication_config_id: nil, backend_authentication_config: nil) -> ::Gapic::Operation

Pass arguments to `create_backend_authentication_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource of the BackendAuthenticationConfig. Must be in the format `projects/*/locations/{location}`. 
  * **backend_authentication_config_id** (::String) — Required. Short name of the BackendAuthenticationConfig resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "backend-auth-config". 
  * **backend_authentication_config** ([::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-BackendAuthenticationConfig), ::Hash) — Required. BackendAuthenticationConfig resource to be created. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::CreateBackendAuthenticationConfigRequest.new
    
    # Call the create_backend_authentication_config method.
    result = client.create_backend_authentication_config request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_client_tls_policy
    
    
    def create_client_tls_policy(request, options = nil) -> ::Gapic::Operation
    def create_client_tls_policy(parent: nil, client_tls_policy_id: nil, client_tls_policy: nil) -> ::Gapic::Operation

Creates a new ClientTlsPolicy in a given project and location.

**Overloads**
    
    
    def create_client_tls_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_client_tls_policy` via a request object, either of type [CreateClientTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateClientTlsPolicyRequest "Google::Cloud::NetworkSecurity::V1::CreateClientTlsPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::CreateClientTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateClientTlsPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_client_tls_policy(parent: nil, client_tls_policy_id: nil, client_tls_policy: nil) -> ::Gapic::Operation

Pass arguments to `create_client_tls_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource of the ClientTlsPolicy. Must be in the format `projects/*/locations/{location}`. 
  * **client_tls_policy_id** (::String) — Required. Short name of the ClientTlsPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "client_mtls_policy". 
  * **client_tls_policy** ([::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ClientTlsPolicy), ::Hash) — Required. ClientTlsPolicy resource to be created. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::CreateClientTlsPolicyRequest.new
    
    # Call the create_client_tls_policy method.
    result = client.create_client_tls_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_gateway_security_policy
    
    
    def create_gateway_security_policy(request, options = nil) -> ::Gapic::Operation
    def create_gateway_security_policy(parent: nil, gateway_security_policy_id: nil, gateway_security_policy: nil) -> ::Gapic::Operation

Creates a new GatewaySecurityPolicy in a given project and location.

**Overloads**
    
    
    def create_gateway_security_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_gateway_security_policy` via a request object, either of type [CreateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateGatewaySecurityPolicyRequest "Google::Cloud::NetworkSecurity::V1::CreateGatewaySecurityPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::CreateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateGatewaySecurityPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_gateway_security_policy(parent: nil, gateway_security_policy_id: nil, gateway_security_policy: nil) -> ::Gapic::Operation

Pass arguments to `create_gateway_security_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource of the GatewaySecurityPolicy. Must be in the format `projects/{project}/locations/{location}`. 
  * **gateway_security_policy_id** (::String) — Required. Short name of the GatewaySecurityPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "gateway_security_policy1". 
  * **gateway_security_policy** ([::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GatewaySecurityPolicy), ::Hash) — Required. GatewaySecurityPolicy resource to be created. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::CreateGatewaySecurityPolicyRequest.new
    
    # Call the create_gateway_security_policy method.
    result = client.create_gateway_security_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_gateway_security_policy_rule
    
    
    def create_gateway_security_policy_rule(request, options = nil) -> ::Gapic::Operation
    def create_gateway_security_policy_rule(parent: nil, gateway_security_policy_rule: nil, gateway_security_policy_rule_id: nil) -> ::Gapic::Operation

Creates a new GatewaySecurityPolicy in a given project and location.

**Overloads**
    
    
    def create_gateway_security_policy_rule(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_gateway_security_policy_rule` via a request object, either of type [CreateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateGatewaySecurityPolicyRuleRequest "Google::Cloud::NetworkSecurity::V1::CreateGatewaySecurityPolicyRuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::CreateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateGatewaySecurityPolicyRuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_gateway_security_policy_rule(parent: nil, gateway_security_policy_rule: nil, gateway_security_policy_rule_id: nil) -> ::Gapic::Operation

Pass arguments to `create_gateway_security_policy_rule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent where this rule will be created. Format : projects/{project}/location/{location}/gatewaySecurityPolicies/* 
  * **gateway_security_policy_rule** ([::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GatewaySecurityPolicyRule), ::Hash) — Required. The rule to be created. 
  * **gateway_security_policy_rule_id** (::String) — The ID to use for the rule, which will become the final component of the rule's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::CreateGatewaySecurityPolicyRuleRequest.new
    
    # Call the create_gateway_security_policy_rule method.
    result = client.create_gateway_security_policy_rule request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_server_tls_policy
    
    
    def create_server_tls_policy(request, options = nil) -> ::Gapic::Operation
    def create_server_tls_policy(parent: nil, server_tls_policy_id: nil, server_tls_policy: nil) -> ::Gapic::Operation

Creates a new ServerTlsPolicy in a given project and location.

**Overloads**
    
    
    def create_server_tls_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_server_tls_policy` via a request object, either of type [CreateServerTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateServerTlsPolicyRequest "Google::Cloud::NetworkSecurity::V1::CreateServerTlsPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::CreateServerTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateServerTlsPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_server_tls_policy(parent: nil, server_tls_policy_id: nil, server_tls_policy: nil) -> ::Gapic::Operation

Pass arguments to `create_server_tls_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource of the ServerTlsPolicy. Must be in the format `projects/*/locations/{location}`. 
  * **server_tls_policy_id** (::String) — Required. Short name of the ServerTlsPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "server_mtls_policy". 
  * **server_tls_policy** ([::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ServerTlsPolicy), ::Hash) — Required. ServerTlsPolicy resource to be created. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::CreateServerTlsPolicyRequest.new
    
    # Call the create_server_tls_policy method.
    result = client.create_server_tls_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_tls_inspection_policy
    
    
    def create_tls_inspection_policy(request, options = nil) -> ::Gapic::Operation
    def create_tls_inspection_policy(parent: nil, tls_inspection_policy_id: nil, tls_inspection_policy: nil) -> ::Gapic::Operation

Creates a new TlsInspectionPolicy in a given project and location.

**Overloads**
    
    
    def create_tls_inspection_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_tls_inspection_policy` via a request object, either of type [CreateTlsInspectionPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateTlsInspectionPolicyRequest "Google::Cloud::NetworkSecurity::V1::CreateTlsInspectionPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::CreateTlsInspectionPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateTlsInspectionPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_tls_inspection_policy(parent: nil, tls_inspection_policy_id: nil, tls_inspection_policy: nil) -> ::Gapic::Operation

Pass arguments to `create_tls_inspection_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource of the TlsInspectionPolicy. Must be in the format `projects/{project}/locations/{location}`. 
  * **tls_inspection_policy_id** (::String) — Required. Short name of the TlsInspectionPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "tls_inspection_policy1". 
  * **tls_inspection_policy** ([::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-TlsInspectionPolicy), ::Hash) — Required. TlsInspectionPolicy resource to be created. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::CreateTlsInspectionPolicyRequest.new
    
    # Call the create_tls_inspection_policy method.
    result = client.create_tls_inspection_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_url_list
    
    
    def create_url_list(request, options = nil) -> ::Gapic::Operation
    def create_url_list(parent: nil, url_list_id: nil, url_list: nil) -> ::Gapic::Operation

Creates a new UrlList in a given project and location.

**Overloads**
    
    
    def create_url_list(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_url_list` via a request object, either of type [CreateUrlListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateUrlListRequest "Google::Cloud::NetworkSecurity::V1::CreateUrlListRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::CreateUrlListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-CreateUrlListRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_url_list(parent: nil, url_list_id: nil, url_list: nil) -> ::Gapic::Operation

Pass arguments to `create_url_list` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource of the UrlList. Must be in the format `projects/*/locations/{location}`. 
  * **url_list_id** (::String) — Required. Short name of the UrlList resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "url_list". 
  * **url_list** ([::Google::Cloud::NetworkSecurity::V1::UrlList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UrlList), ::Hash) — Required. UrlList resource to be created. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::CreateUrlListRequest.new
    
    # Call the create_url_list method.
    result = client.create_url_list request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_authorization_policy
    
    
    def delete_authorization_policy(request, options = nil) -> ::Gapic::Operation
    def delete_authorization_policy(name: nil) -> ::Gapic::Operation

Deletes a single AuthorizationPolicy.

**Overloads**
    
    
    def delete_authorization_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_authorization_policy` via a request object, either of type [DeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteAuthorizationPolicyRequest "Google::Cloud::NetworkSecurity::V1::DeleteAuthorizationPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::DeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteAuthorizationPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_authorization_policy(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_authorization_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the AuthorizationPolicy to delete. Must be in the format `projects/{project}/locations/{location}/authorizationPolicies/*`. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::DeleteAuthorizationPolicyRequest.new
    
    # Call the delete_authorization_policy method.
    result = client.delete_authorization_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_authz_policy
    
    
    def delete_authz_policy(request, options = nil) -> ::Gapic::Operation
    def delete_authz_policy(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single AuthzPolicy.

**Overloads**
    
    
    def delete_authz_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_authz_policy` via a request object, either of type [DeleteAuthzPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteAuthzPolicyRequest "Google::Cloud::NetworkSecurity::V1::DeleteAuthzPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::DeleteAuthzPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteAuthzPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_authz_policy(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_authz_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the `AuthzPolicy` resource to delete. Must be in the format `projects/{project}/locations/{location}/authzPolicies/{authz_policy}`. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server can ignore the request if it has already been completed. The server guarantees that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::DeleteAuthzPolicyRequest.new
    
    # Call the delete_authz_policy method.
    result = client.delete_authz_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_backend_authentication_config
    
    
    def delete_backend_authentication_config(request, options = nil) -> ::Gapic::Operation
    def delete_backend_authentication_config(name: nil, etag: nil) -> ::Gapic::Operation

Deletes a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Overloads**
    
    
    def delete_backend_authentication_config(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_backend_authentication_config` via a request object, either of type [DeleteBackendAuthenticationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteBackendAuthenticationConfigRequest "Google::Cloud::NetworkSecurity::V1::DeleteBackendAuthenticationConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::DeleteBackendAuthenticationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteBackendAuthenticationConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_backend_authentication_config(name: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_backend_authentication_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. A name of the BackendAuthenticationConfig to delete. Must be in the format `projects/*/locations/{location}/backendAuthenticationConfigs/*`. 
  * **etag** (::String) — Optional. Etag of the resource. If this is provided, it must match the server's etag. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::DeleteBackendAuthenticationConfigRequest.new
    
    # Call the delete_backend_authentication_config method.
    result = client.delete_backend_authentication_config request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_client_tls_policy
    
    
    def delete_client_tls_policy(request, options = nil) -> ::Gapic::Operation
    def delete_client_tls_policy(name: nil) -> ::Gapic::Operation

Deletes a single ClientTlsPolicy.

**Overloads**
    
    
    def delete_client_tls_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_client_tls_policy` via a request object, either of type [DeleteClientTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteClientTlsPolicyRequest "Google::Cloud::NetworkSecurity::V1::DeleteClientTlsPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::DeleteClientTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteClientTlsPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_client_tls_policy(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_client_tls_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the ClientTlsPolicy to delete. Must be in the format `projects/*/locations/{location}/clientTlsPolicies/*`. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::DeleteClientTlsPolicyRequest.new
    
    # Call the delete_client_tls_policy method.
    result = client.delete_client_tls_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_gateway_security_policy
    
    
    def delete_gateway_security_policy(request, options = nil) -> ::Gapic::Operation
    def delete_gateway_security_policy(name: nil) -> ::Gapic::Operation

Deletes a single GatewaySecurityPolicy.

**Overloads**
    
    
    def delete_gateway_security_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_gateway_security_policy` via a request object, either of type [DeleteGatewaySecurityPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteGatewaySecurityPolicyRequest "Google::Cloud::NetworkSecurity::V1::DeleteGatewaySecurityPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::DeleteGatewaySecurityPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteGatewaySecurityPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_gateway_security_policy(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_gateway_security_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the GatewaySecurityPolicy to delete. Must be in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/*`. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::DeleteGatewaySecurityPolicyRequest.new
    
    # Call the delete_gateway_security_policy method.
    result = client.delete_gateway_security_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_gateway_security_policy_rule
    
    
    def delete_gateway_security_policy_rule(request, options = nil) -> ::Gapic::Operation
    def delete_gateway_security_policy_rule(name: nil) -> ::Gapic::Operation

Deletes a single GatewaySecurityPolicyRule.

**Overloads**
    
    
    def delete_gateway_security_policy_rule(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_gateway_security_policy_rule` via a request object, either of type [DeleteGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteGatewaySecurityPolicyRuleRequest "Google::Cloud::NetworkSecurity::V1::DeleteGatewaySecurityPolicyRuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::DeleteGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteGatewaySecurityPolicyRuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_gateway_security_policy_rule(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_gateway_security_policy_rule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the GatewaySecurityPolicyRule to delete. Must be in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy}/rules/*`. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::DeleteGatewaySecurityPolicyRuleRequest.new
    
    # Call the delete_gateway_security_policy_rule method.
    result = client.delete_gateway_security_policy_rule request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_server_tls_policy
    
    
    def delete_server_tls_policy(request, options = nil) -> ::Gapic::Operation
    def delete_server_tls_policy(name: nil) -> ::Gapic::Operation

Deletes a single ServerTlsPolicy.

**Overloads**
    
    
    def delete_server_tls_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_server_tls_policy` via a request object, either of type [DeleteServerTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteServerTlsPolicyRequest "Google::Cloud::NetworkSecurity::V1::DeleteServerTlsPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::DeleteServerTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteServerTlsPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_server_tls_policy(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_server_tls_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the ServerTlsPolicy to delete. Must be in the format `projects/*/locations/{location}/serverTlsPolicies/*`. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::DeleteServerTlsPolicyRequest.new
    
    # Call the delete_server_tls_policy method.
    result = client.delete_server_tls_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_tls_inspection_policy
    
    
    def delete_tls_inspection_policy(request, options = nil) -> ::Gapic::Operation
    def delete_tls_inspection_policy(name: nil, force: nil) -> ::Gapic::Operation

Deletes a single TlsInspectionPolicy.

**Overloads**
    
    
    def delete_tls_inspection_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_tls_inspection_policy` via a request object, either of type [DeleteTlsInspectionPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteTlsInspectionPolicyRequest "Google::Cloud::NetworkSecurity::V1::DeleteTlsInspectionPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::DeleteTlsInspectionPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteTlsInspectionPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_tls_inspection_policy(name: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_tls_inspection_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. A name of the TlsInspectionPolicy to delete. Must be in the format `projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy}`. 
  * **force** (::Boolean) — If set to true, any rules for this TlsInspectionPolicy will also be deleted. (Otherwise, the request will only work if the TlsInspectionPolicy has no rules.) 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::DeleteTlsInspectionPolicyRequest.new
    
    # Call the delete_tls_inspection_policy method.
    result = client.delete_tls_inspection_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_url_list
    
    
    def delete_url_list(request, options = nil) -> ::Gapic::Operation
    def delete_url_list(name: nil) -> ::Gapic::Operation

Deletes a single UrlList.

**Overloads**
    
    
    def delete_url_list(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_url_list` via a request object, either of type [DeleteUrlListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteUrlListRequest "Google::Cloud::NetworkSecurity::V1::DeleteUrlListRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::DeleteUrlListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-DeleteUrlListRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_url_list(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_url_list` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the UrlList to delete. Must be in the format `projects/*/locations/{location}/urlLists/*`. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::DeleteUrlListRequest.new
    
    # Call the delete_url_list method.
    result = client.delete_url_list request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_authorization_policy
    
    
    def get_authorization_policy(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy
    def get_authorization_policy(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy

Gets details of a single AuthorizationPolicy.

**Overloads**
    
    
    def get_authorization_policy(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy

Pass arguments to `get_authorization_policy` via a request object, either of type [GetAuthorizationPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetAuthorizationPolicyRequest "Google::Cloud::NetworkSecurity::V1::GetAuthorizationPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::GetAuthorizationPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetAuthorizationPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_authorization_policy(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy

Pass arguments to `get_authorization_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the AuthorizationPolicy to get. Must be in the format `projects/{project}/locations/{location}/authorizationPolicies/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthorizationPolicy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthorizationPolicy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::GetAuthorizationPolicyRequest.new
    
    # Call the get_authorization_policy method.
    result = client.get_authorization_policy request
    
    # The returned object is of type Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy.
    p result

### #get_authz_policy
    
    
    def get_authz_policy(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy
    def get_authz_policy(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy

Gets details of a single AuthzPolicy.

**Overloads**
    
    
    def get_authz_policy(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy

Pass arguments to `get_authz_policy` via a request object, either of type [GetAuthzPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetAuthzPolicyRequest "Google::Cloud::NetworkSecurity::V1::GetAuthzPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::GetAuthzPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetAuthzPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_authz_policy(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy

Pass arguments to `get_authz_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the `AuthzPolicy` resource to get. Must be in the format `projects/{project}/locations/{location}/authzPolicies/{authz_policy}`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::GetAuthzPolicyRequest.new
    
    # Call the get_authz_policy method.
    result = client.get_authz_policy request
    
    # The returned object is of type Google::Cloud::NetworkSecurity::V1::AuthzPolicy.
    p result

### #get_backend_authentication_config
    
    
    def get_backend_authentication_config(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig
    def get_backend_authentication_config(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig

Gets details of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Overloads**
    
    
    def get_backend_authentication_config(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig

Pass arguments to `get_backend_authentication_config` via a request object, either of type [GetBackendAuthenticationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetBackendAuthenticationConfigRequest "Google::Cloud::NetworkSecurity::V1::GetBackendAuthenticationConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::GetBackendAuthenticationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetBackendAuthenticationConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_backend_authentication_config(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig

Pass arguments to `get_backend_authentication_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the BackendAuthenticationConfig to get. Must be in the format `projects/*/locations/{location}/backendAuthenticationConfigs/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-BackendAuthenticationConfig)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-BackendAuthenticationConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::GetBackendAuthenticationConfigRequest.new
    
    # Call the get_backend_authentication_config method.
    result = client.get_backend_authentication_config request
    
    # The returned object is of type Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig.
    p result

### #get_client_tls_policy
    
    
    def get_client_tls_policy(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy
    def get_client_tls_policy(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy

Gets details of a single ClientTlsPolicy.

**Overloads**
    
    
    def get_client_tls_policy(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy

Pass arguments to `get_client_tls_policy` via a request object, either of type [GetClientTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetClientTlsPolicyRequest "Google::Cloud::NetworkSecurity::V1::GetClientTlsPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::GetClientTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetClientTlsPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_client_tls_policy(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy

Pass arguments to `get_client_tls_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the ClientTlsPolicy to get. Must be in the format `projects/*/locations/{location}/clientTlsPolicies/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ClientTlsPolicy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ClientTlsPolicy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::GetClientTlsPolicyRequest.new
    
    # Call the get_client_tls_policy method.
    result = client.get_client_tls_policy request
    
    # The returned object is of type Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy.
    p result

### #get_gateway_security_policy
    
    
    def get_gateway_security_policy(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy
    def get_gateway_security_policy(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy

Gets details of a single GatewaySecurityPolicy.

**Overloads**
    
    
    def get_gateway_security_policy(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy

Pass arguments to `get_gateway_security_policy` via a request object, either of type [GetGatewaySecurityPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetGatewaySecurityPolicyRequest "Google::Cloud::NetworkSecurity::V1::GetGatewaySecurityPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::GetGatewaySecurityPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetGatewaySecurityPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_gateway_security_policy(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy

Pass arguments to `get_gateway_security_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the GatewaySecurityPolicy to get. Must be in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GatewaySecurityPolicy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GatewaySecurityPolicy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::GetGatewaySecurityPolicyRequest.new
    
    # Call the get_gateway_security_policy method.
    result = client.get_gateway_security_policy request
    
    # The returned object is of type Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy.
    p result

### #get_gateway_security_policy_rule
    
    
    def get_gateway_security_policy_rule(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule
    def get_gateway_security_policy_rule(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule

Gets details of a single GatewaySecurityPolicyRule.

**Overloads**
    
    
    def get_gateway_security_policy_rule(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule

Pass arguments to `get_gateway_security_policy_rule` via a request object, either of type [GetGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetGatewaySecurityPolicyRuleRequest "Google::Cloud::NetworkSecurity::V1::GetGatewaySecurityPolicyRuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::GetGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetGatewaySecurityPolicyRuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_gateway_security_policy_rule(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule

Pass arguments to `get_gateway_security_policy_rule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the GatewaySecurityPolicyRule to retrieve. Format: projects/{project}/location/{location}/gatewaySecurityPolicies/_/rules/_



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GatewaySecurityPolicyRule)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GatewaySecurityPolicyRule)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::GetGatewaySecurityPolicyRuleRequest.new
    
    # Call the get_gateway_security_policy_rule method.
    result = client.get_gateway_security_policy_rule request
    
    # The returned object is of type Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule.
    p result

### #get_server_tls_policy
    
    
    def get_server_tls_policy(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy
    def get_server_tls_policy(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy

Gets details of a single ServerTlsPolicy.

**Overloads**
    
    
    def get_server_tls_policy(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy

Pass arguments to `get_server_tls_policy` via a request object, either of type [GetServerTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetServerTlsPolicyRequest "Google::Cloud::NetworkSecurity::V1::GetServerTlsPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::GetServerTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetServerTlsPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_server_tls_policy(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy

Pass arguments to `get_server_tls_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the ServerTlsPolicy to get. Must be in the format `projects/*/locations/{location}/serverTlsPolicies/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ServerTlsPolicy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ServerTlsPolicy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::GetServerTlsPolicyRequest.new
    
    # Call the get_server_tls_policy method.
    result = client.get_server_tls_policy request
    
    # The returned object is of type Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy.
    p result

### #get_tls_inspection_policy
    
    
    def get_tls_inspection_policy(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy
    def get_tls_inspection_policy(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy

Gets details of a single TlsInspectionPolicy.

**Overloads**
    
    
    def get_tls_inspection_policy(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy

Pass arguments to `get_tls_inspection_policy` via a request object, either of type [GetTlsInspectionPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetTlsInspectionPolicyRequest "Google::Cloud::NetworkSecurity::V1::GetTlsInspectionPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::GetTlsInspectionPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetTlsInspectionPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_tls_inspection_policy(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy

Pass arguments to `get_tls_inspection_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the TlsInspectionPolicy to get. Must be in the format `projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy}`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-TlsInspectionPolicy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-TlsInspectionPolicy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::GetTlsInspectionPolicyRequest.new
    
    # Call the get_tls_inspection_policy method.
    result = client.get_tls_inspection_policy request
    
    # The returned object is of type Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy.
    p result

### #get_url_list
    
    
    def get_url_list(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::UrlList
    def get_url_list(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::UrlList

Gets details of a single UrlList.

**Overloads**
    
    
    def get_url_list(request, options = nil) -> ::Google::Cloud::NetworkSecurity::V1::UrlList

Pass arguments to `get_url_list` via a request object, either of type [GetUrlListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetUrlListRequest "Google::Cloud::NetworkSecurity::V1::GetUrlListRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::GetUrlListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GetUrlListRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_url_list(name: nil) -> ::Google::Cloud::NetworkSecurity::V1::UrlList

Pass arguments to `get_url_list` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. A name of the UrlList to get. Must be in the format `projects/*/locations/{location}/urlLists/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkSecurity::V1::UrlList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UrlList)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::UrlList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UrlList)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::GetUrlListRequest.new
    
    # Call the get_url_list method.
    result = client.get_url_list request
    
    # The returned object is of type Google::Cloud::NetworkSecurity::V1::UrlList.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new NetworkSecurity client object.

**Yields**

  * (config) — Configure the NetworkSecurity client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new do |config|
      config.timeout = 10.0
    end

### #list_authorization_policies
    
    
    def list_authorization_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy>
    def list_authorization_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy>

Lists AuthorizationPolicies in a given project and location.

**Overloads**
    
    
    def list_authorization_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy>

Pass arguments to `list_authorization_policies` via a request object, either of type [ListAuthorizationPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListAuthorizationPoliciesRequest "Google::Cloud::NetworkSecurity::V1::ListAuthorizationPoliciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::ListAuthorizationPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListAuthorizationPoliciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_authorization_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy>

Pass arguments to `list_authorization_policies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location from which the AuthorizationPolicies should be listed, specified in the format `projects/{project}/locations/{location}`. 
  * **page_size** (::Integer) — Maximum number of AuthorizationPolicies to return per call. 
  * **page_token** (::String) — The value returned by the last `ListAuthorizationPoliciesResponse` Indicates that this is a continuation of a prior `ListAuthorizationPolicies` call, and that the system should return the next page of data. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthorizationPolicy)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthorizationPolicy)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::ListAuthorizationPoliciesRequest.new
    
    # Call the list_authorization_policies method.
    result = client.list_authorization_policies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy.
      p item
    end

### #list_authz_policies
    
    
    def list_authz_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy>
    def list_authz_policies(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy>

Lists AuthzPolicies in a given project and location.

**Overloads**
    
    
    def list_authz_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy>

Pass arguments to `list_authz_policies` via a request object, either of type [ListAuthzPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListAuthzPoliciesRequest "Google::Cloud::NetworkSecurity::V1::ListAuthzPoliciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::ListAuthzPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListAuthzPoliciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_authz_policies(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy>

Pass arguments to `list_authz_policies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location from which the `AuthzPolicy` resources are listed, specified in the following format: `projects/{project}/locations/{location}`. 
  * **page_size** (::Integer) — Optional. Requested page size. The server might return fewer items than requested. If unspecified, the server picks an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results that the server returns. 
  * **filter** (::String) — Optional. Filtering results. 
  * **order_by** (::String) — Optional. Hint for how to order the results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::ListAuthzPoliciesRequest.new
    
    # Call the list_authz_policies method.
    result = client.list_authz_policies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy.
      p item
    end

### #list_backend_authentication_configs
    
    
    def list_backend_authentication_configs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig>
    def list_backend_authentication_configs(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig>

Lists BackendAuthenticationConfigs in a given project and location.

**Overloads**
    
    
    def list_backend_authentication_configs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig>

Pass arguments to `list_backend_authentication_configs` via a request object, either of type [ListBackendAuthenticationConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListBackendAuthenticationConfigsRequest "Google::Cloud::NetworkSecurity::V1::ListBackendAuthenticationConfigsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::ListBackendAuthenticationConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListBackendAuthenticationConfigsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_backend_authentication_configs(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig>

Pass arguments to `list_backend_authentication_configs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location from which the BackendAuthenticationConfigs should be listed, specified in the format `projects/*/locations/{location}`. 
  * **page_size** (::Integer) — Maximum number of BackendAuthenticationConfigs to return per call. 
  * **page_token** (::String) — The value returned by the last `ListBackendAuthenticationConfigsResponse` Indicates that this is a continuation of a prior `ListBackendAuthenticationConfigs` call, and that the system should return the next page of data. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-BackendAuthenticationConfig)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-BackendAuthenticationConfig)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::ListBackendAuthenticationConfigsRequest.new
    
    # Call the list_backend_authentication_configs method.
    result = client.list_backend_authentication_configs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig.
      p item
    end

### #list_client_tls_policies
    
    
    def list_client_tls_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy>
    def list_client_tls_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy>

Lists ClientTlsPolicies in a given project and location.

**Overloads**
    
    
    def list_client_tls_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy>

Pass arguments to `list_client_tls_policies` via a request object, either of type [ListClientTlsPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListClientTlsPoliciesRequest "Google::Cloud::NetworkSecurity::V1::ListClientTlsPoliciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::ListClientTlsPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListClientTlsPoliciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_client_tls_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy>

Pass arguments to `list_client_tls_policies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location from which the ClientTlsPolicies should be listed, specified in the format `projects/*/locations/{location}`. 
  * **page_size** (::Integer) — Maximum number of ClientTlsPolicies to return per call. 
  * **page_token** (::String) — The value returned by the last `ListClientTlsPoliciesResponse` Indicates that this is a continuation of a prior `ListClientTlsPolicies` call, and that the system should return the next page of data. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ClientTlsPolicy)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ClientTlsPolicy)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::ListClientTlsPoliciesRequest.new
    
    # Call the list_client_tls_policies method.
    result = client.list_client_tls_policies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy.
      p item
    end

### #list_gateway_security_policies
    
    
    def list_gateway_security_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy>
    def list_gateway_security_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy>

Lists GatewaySecurityPolicies in a given project and location.

**Overloads**
    
    
    def list_gateway_security_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy>

Pass arguments to `list_gateway_security_policies` via a request object, either of type [ListGatewaySecurityPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListGatewaySecurityPoliciesRequest "Google::Cloud::NetworkSecurity::V1::ListGatewaySecurityPoliciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::ListGatewaySecurityPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListGatewaySecurityPoliciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_gateway_security_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy>

Pass arguments to `list_gateway_security_policies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location from which the GatewaySecurityPolicies should be listed, specified in the format `projects/{project}/locations/{location}`. 
  * **page_size** (::Integer) — Maximum number of GatewaySecurityPolicies to return per call. 
  * **page_token** (::String) — The value returned by the last 'ListGatewaySecurityPoliciesResponse' Indicates that this is a continuation of a prior 'ListGatewaySecurityPolicies' call, and that the system should return the next page of data. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GatewaySecurityPolicy)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GatewaySecurityPolicy)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::ListGatewaySecurityPoliciesRequest.new
    
    # Call the list_gateway_security_policies method.
    result = client.list_gateway_security_policies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy.
      p item
    end

### #list_gateway_security_policy_rules
    
    
    def list_gateway_security_policy_rules(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule>
    def list_gateway_security_policy_rules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule>

Lists GatewaySecurityPolicyRules in a given project and location.

**Overloads**
    
    
    def list_gateway_security_policy_rules(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule>

Pass arguments to `list_gateway_security_policy_rules` via a request object, either of type [ListGatewaySecurityPolicyRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListGatewaySecurityPolicyRulesRequest "Google::Cloud::NetworkSecurity::V1::ListGatewaySecurityPolicyRulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::ListGatewaySecurityPolicyRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListGatewaySecurityPolicyRulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_gateway_security_policy_rules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule>

Pass arguments to `list_gateway_security_policy_rules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project, location and GatewaySecurityPolicy from which the GatewaySecurityPolicyRules should be listed, specified in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy}`. 
  * **page_size** (::Integer) — Maximum number of GatewaySecurityPolicyRules to return per call. 
  * **page_token** (::String) — The value returned by the last 'ListGatewaySecurityPolicyRulesResponse' Indicates that this is a continuation of a prior 'ListGatewaySecurityPolicyRules' call, and that the system should return the next page of data. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GatewaySecurityPolicyRule)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GatewaySecurityPolicyRule)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::ListGatewaySecurityPolicyRulesRequest.new
    
    # Call the list_gateway_security_policy_rules method.
    result = client.list_gateway_security_policy_rules request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule.
      p item
    end

### #list_server_tls_policies
    
    
    def list_server_tls_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy>
    def list_server_tls_policies(parent: nil, page_size: nil, page_token: nil, return_partial_success: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy>

Lists ServerTlsPolicies in a given project and location.

**Overloads**
    
    
    def list_server_tls_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy>

Pass arguments to `list_server_tls_policies` via a request object, either of type [ListServerTlsPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListServerTlsPoliciesRequest "Google::Cloud::NetworkSecurity::V1::ListServerTlsPoliciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::ListServerTlsPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListServerTlsPoliciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_server_tls_policies(parent: nil, page_size: nil, page_token: nil, return_partial_success: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy>

Pass arguments to `list_server_tls_policies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location from which the ServerTlsPolicies should be listed, specified in the format `projects/*/locations/{location}`. 
  * **page_size** (::Integer) — Maximum number of ServerTlsPolicies to return per call. 
  * **page_token** (::String) — The value returned by the last `ListServerTlsPoliciesResponse` Indicates that this is a continuation of a prior `ListServerTlsPolicies` call, and that the system should return the next page of data. 
  * **return_partial_success** (::Boolean) — Optional. Setting this field to `true` will opt the request into returning the resources that are reachable, and into including the names of those that were unreachable in the [ListServerTlsPoliciesResponse.unreachable] field. This can only be `true` when reading across collections e.g. when `parent` is set to `"projects/example/locations/-"`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ServerTlsPolicy)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ServerTlsPolicy)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::ListServerTlsPoliciesRequest.new
    
    # Call the list_server_tls_policies method.
    result = client.list_server_tls_policies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy.
      p item
    end

### #list_tls_inspection_policies
    
    
    def list_tls_inspection_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy>
    def list_tls_inspection_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy>

Lists TlsInspectionPolicies in a given project and location.

**Overloads**
    
    
    def list_tls_inspection_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy>

Pass arguments to `list_tls_inspection_policies` via a request object, either of type [ListTlsInspectionPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListTlsInspectionPoliciesRequest "Google::Cloud::NetworkSecurity::V1::ListTlsInspectionPoliciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::ListTlsInspectionPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListTlsInspectionPoliciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_tls_inspection_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy>

Pass arguments to `list_tls_inspection_policies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location from which the TlsInspectionPolicies should be listed, specified in the format `projects/{project}/locations/{location}`. 
  * **page_size** (::Integer) — Maximum number of TlsInspectionPolicies to return per call. 
  * **page_token** (::String) — The value returned by the last 'ListTlsInspectionPoliciesResponse' Indicates that this is a continuation of a prior 'ListTlsInspectionPolicies' call, and that the system should return the next page of data. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-TlsInspectionPolicy)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-TlsInspectionPolicy)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::ListTlsInspectionPoliciesRequest.new
    
    # Call the list_tls_inspection_policies method.
    result = client.list_tls_inspection_policies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy.
      p item
    end

### #list_url_lists
    
    
    def list_url_lists(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::UrlList>
    def list_url_lists(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::UrlList>

Lists UrlLists in a given project and location.

**Overloads**
    
    
    def list_url_lists(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::UrlList>

Pass arguments to `list_url_lists` via a request object, either of type [ListUrlListsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListUrlListsRequest "Google::Cloud::NetworkSecurity::V1::ListUrlListsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::ListUrlListsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ListUrlListsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_url_lists(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkSecurity::V1::UrlList>

Pass arguments to `list_url_lists` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location from which the UrlLists should be listed, specified in the format `projects/{project}/locations/{location}`. 
  * **page_size** (::Integer) — Maximum number of UrlLists to return per call. 
  * **page_token** (::String) — The value returned by the last `ListUrlListsResponse` Indicates that this is a continuation of a prior `ListUrlLists` call, and that the system should return the next page of data. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::UrlList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UrlList)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkSecurity::V1::UrlList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UrlList)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::ListUrlListsRequest.new
    
    # Call the list_url_lists method.
    result = client.list_url_lists request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkSecurity::V1::UrlList.
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
    
    
    def operations_client() -> ::Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-NetworkSecurity-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_authorization_policy
    
    
    def update_authorization_policy(request, options = nil) -> ::Gapic::Operation
    def update_authorization_policy(update_mask: nil, authorization_policy: nil) -> ::Gapic::Operation

Updates the parameters of a single AuthorizationPolicy.

**Overloads**
    
    
    def update_authorization_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_authorization_policy` via a request object, either of type [UpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateAuthorizationPolicyRequest "Google::Cloud::NetworkSecurity::V1::UpdateAuthorizationPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::UpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateAuthorizationPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_authorization_policy(update_mask: nil, authorization_policy: nil) -> ::Gapic::Operation

Pass arguments to `update_authorization_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the AuthorizationPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **authorization_policy** ([::Google::Cloud::NetworkSecurity::V1::AuthorizationPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthorizationPolicy), ::Hash) — Required. Updated AuthorizationPolicy resource. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::UpdateAuthorizationPolicyRequest.new
    
    # Call the update_authorization_policy method.
    result = client.update_authorization_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_authz_policy
    
    
    def update_authz_policy(request, options = nil) -> ::Gapic::Operation
    def update_authz_policy(update_mask: nil, authz_policy: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single AuthzPolicy.

**Overloads**
    
    
    def update_authz_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_authz_policy` via a request object, either of type [UpdateAuthzPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateAuthzPolicyRequest "Google::Cloud::NetworkSecurity::V1::UpdateAuthzPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::UpdateAuthzPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateAuthzPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_authz_policy(update_mask: nil, authz_policy: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_authz_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Used to specify the fields to be overwritten in the `AuthzPolicy` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not specify a mask, then all fields are overwritten. 
  * **authz_policy** ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy), ::Hash) — Required. `AuthzPolicy` resource being updated. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server can ignore the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::UpdateAuthzPolicyRequest.new
    
    # Call the update_authz_policy method.
    result = client.update_authz_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_backend_authentication_config
    
    
    def update_backend_authentication_config(request, options = nil) -> ::Gapic::Operation
    def update_backend_authentication_config(update_mask: nil, backend_authentication_config: nil) -> ::Gapic::Operation

Updates the parameters of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Overloads**
    
    
    def update_backend_authentication_config(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_backend_authentication_config` via a request object, either of type [UpdateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateBackendAuthenticationConfigRequest "Google::Cloud::NetworkSecurity::V1::UpdateBackendAuthenticationConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::UpdateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateBackendAuthenticationConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_backend_authentication_config(update_mask: nil, backend_authentication_config: nil) -> ::Gapic::Operation

Pass arguments to `update_backend_authentication_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the BackendAuthenticationConfig resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **backend_authentication_config** ([::Google::Cloud::NetworkSecurity::V1::BackendAuthenticationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-BackendAuthenticationConfig), ::Hash) — Required. Updated BackendAuthenticationConfig resource. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::UpdateBackendAuthenticationConfigRequest.new
    
    # Call the update_backend_authentication_config method.
    result = client.update_backend_authentication_config request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_client_tls_policy
    
    
    def update_client_tls_policy(request, options = nil) -> ::Gapic::Operation
    def update_client_tls_policy(update_mask: nil, client_tls_policy: nil) -> ::Gapic::Operation

Updates the parameters of a single ClientTlsPolicy.

**Overloads**
    
    
    def update_client_tls_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_client_tls_policy` via a request object, either of type [UpdateClientTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateClientTlsPolicyRequest "Google::Cloud::NetworkSecurity::V1::UpdateClientTlsPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::UpdateClientTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateClientTlsPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_client_tls_policy(update_mask: nil, client_tls_policy: nil) -> ::Gapic::Operation

Pass arguments to `update_client_tls_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the ClientTlsPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **client_tls_policy** ([::Google::Cloud::NetworkSecurity::V1::ClientTlsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ClientTlsPolicy), ::Hash) — Required. Updated ClientTlsPolicy resource. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::UpdateClientTlsPolicyRequest.new
    
    # Call the update_client_tls_policy method.
    result = client.update_client_tls_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_gateway_security_policy
    
    
    def update_gateway_security_policy(request, options = nil) -> ::Gapic::Operation
    def update_gateway_security_policy(update_mask: nil, gateway_security_policy: nil) -> ::Gapic::Operation

Updates the parameters of a single GatewaySecurityPolicy.

**Overloads**
    
    
    def update_gateway_security_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_gateway_security_policy` via a request object, either of type [UpdateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateGatewaySecurityPolicyRequest "Google::Cloud::NetworkSecurity::V1::UpdateGatewaySecurityPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::UpdateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateGatewaySecurityPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_gateway_security_policy(update_mask: nil, gateway_security_policy: nil) -> ::Gapic::Operation

Pass arguments to `update_gateway_security_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the GatewaySecurityPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **gateway_security_policy** ([::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GatewaySecurityPolicy), ::Hash) — Required. Updated GatewaySecurityPolicy resource. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::UpdateGatewaySecurityPolicyRequest.new
    
    # Call the update_gateway_security_policy method.
    result = client.update_gateway_security_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_gateway_security_policy_rule
    
    
    def update_gateway_security_policy_rule(request, options = nil) -> ::Gapic::Operation
    def update_gateway_security_policy_rule(update_mask: nil, gateway_security_policy_rule: nil) -> ::Gapic::Operation

Updates the parameters of a single GatewaySecurityPolicyRule.

**Overloads**
    
    
    def update_gateway_security_policy_rule(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_gateway_security_policy_rule` via a request object, either of type [UpdateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateGatewaySecurityPolicyRuleRequest "Google::Cloud::NetworkSecurity::V1::UpdateGatewaySecurityPolicyRuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::UpdateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateGatewaySecurityPolicyRuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_gateway_security_policy_rule(update_mask: nil, gateway_security_policy_rule: nil) -> ::Gapic::Operation

Pass arguments to `update_gateway_security_policy_rule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the GatewaySecurityPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **gateway_security_policy_rule** ([::Google::Cloud::NetworkSecurity::V1::GatewaySecurityPolicyRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-GatewaySecurityPolicyRule), ::Hash) — Required. Updated GatewaySecurityPolicyRule resource. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::UpdateGatewaySecurityPolicyRuleRequest.new
    
    # Call the update_gateway_security_policy_rule method.
    result = client.update_gateway_security_policy_rule request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_server_tls_policy
    
    
    def update_server_tls_policy(request, options = nil) -> ::Gapic::Operation
    def update_server_tls_policy(update_mask: nil, server_tls_policy: nil) -> ::Gapic::Operation

Updates the parameters of a single ServerTlsPolicy.

**Overloads**
    
    
    def update_server_tls_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_server_tls_policy` via a request object, either of type [UpdateServerTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateServerTlsPolicyRequest "Google::Cloud::NetworkSecurity::V1::UpdateServerTlsPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::UpdateServerTlsPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateServerTlsPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_server_tls_policy(update_mask: nil, server_tls_policy: nil) -> ::Gapic::Operation

Pass arguments to `update_server_tls_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the ServerTlsPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **server_tls_policy** ([::Google::Cloud::NetworkSecurity::V1::ServerTlsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-ServerTlsPolicy), ::Hash) — Required. Updated ServerTlsPolicy resource. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::UpdateServerTlsPolicyRequest.new
    
    # Call the update_server_tls_policy method.
    result = client.update_server_tls_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_tls_inspection_policy
    
    
    def update_tls_inspection_policy(request, options = nil) -> ::Gapic::Operation
    def update_tls_inspection_policy(update_mask: nil, tls_inspection_policy: nil) -> ::Gapic::Operation

Updates the parameters of a single TlsInspectionPolicy.

**Overloads**
    
    
    def update_tls_inspection_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_tls_inspection_policy` via a request object, either of type [UpdateTlsInspectionPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateTlsInspectionPolicyRequest "Google::Cloud::NetworkSecurity::V1::UpdateTlsInspectionPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::UpdateTlsInspectionPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateTlsInspectionPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_tls_inspection_policy(update_mask: nil, tls_inspection_policy: nil) -> ::Gapic::Operation

Pass arguments to `update_tls_inspection_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the TlsInspectionPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **tls_inspection_policy** ([::Google::Cloud::NetworkSecurity::V1::TlsInspectionPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-TlsInspectionPolicy), ::Hash) — Required. Updated TlsInspectionPolicy resource. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::UpdateTlsInspectionPolicyRequest.new
    
    # Call the update_tls_inspection_policy method.
    result = client.update_tls_inspection_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_url_list
    
    
    def update_url_list(request, options = nil) -> ::Gapic::Operation
    def update_url_list(update_mask: nil, url_list: nil) -> ::Gapic::Operation

Updates the parameters of a single UrlList.

**Overloads**
    
    
    def update_url_list(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_url_list` via a request object, either of type [UpdateUrlListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateUrlListRequest "Google::Cloud::NetworkSecurity::V1::UpdateUrlListRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkSecurity::V1::UpdateUrlListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateUrlListRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_url_list(update_mask: nil, url_list: nil) -> ::Gapic::Operation

Pass arguments to `update_url_list` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the UrlList resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **url_list** ([::Google::Cloud::NetworkSecurity::V1::UrlList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UrlList), ::Hash) — Required. Updated UrlList resource. 



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
    
    
    require "google/cloud/network_security/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkSecurity::V1::NetworkSecurity::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkSecurity::V1::UpdateUrlListRequest.new
    
    # Call the update_url_list method.
    result = client.update_url_list request
    
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

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
