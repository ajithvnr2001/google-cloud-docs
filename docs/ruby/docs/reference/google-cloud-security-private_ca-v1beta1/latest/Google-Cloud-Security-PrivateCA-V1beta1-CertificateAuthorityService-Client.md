---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client/
title: Certificate Authority Service V1beta1 API - Class Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client (v0.18.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:32.396285+00:00
---

# Certificate Authority Service V1beta1 API - Class Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client (v0.18.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Certificate Authority Service V1beta1 API - Class Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client (v0.18.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.1 (latest)  0.18.0  0.17.1  0.16.0  0.15.1  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the Certificate Authority Service V1beta1 API class Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.

Client for the CertificateAuthorityService service.

[Certificate Authority Service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client \(class\)") manages private certificate authorities and issued certificates.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the CertificateAuthorityService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client-Configuration "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all CertificateAuthorityService clients
    ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.configure do |config|
      config.timeout = 10.0
    end

### #activate_certificate_authority
    
    
    def activate_certificate_authority(request, options = nil) -> ::Gapic::Operation
    def activate_certificate_authority(name: nil, pem_ca_certificate: nil, subordinate_config: nil, request_id: nil) -> ::Gapic::Operation

Activate a [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") that is in state [PENDING_ACTIVATION](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority-State#Google__Cloud__Security__PrivateCA__V1beta1__CertificateAuthority__State__PENDING_ACTIVATION "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority::State::PENDING_ACTIVATION \(constant\)") and is of type [SUBORDINATE](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority-Type#Google__Cloud__Security__PrivateCA__V1beta1__CertificateAuthority__Type__SUBORDINATE "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority::Type::SUBORDINATE \(constant\)"). After the parent Certificate Authority signs a certificate signing request from [FetchCertificateAuthorityCsr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client#Google__Cloud__Security__PrivateCA__V1beta1__CertificateAuthorityService__Client_fetch_certificate_authority_csr_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client#fetch_certificate_authority_csr \(method\)"), this method can complete the activation process.

**Overloads**
    
    
    def activate_certificate_authority(request, options = nil) -> ::Gapic::Operation

Pass arguments to `activate_certificate_authority` via a request object, either of type [ActivateCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ActivateCertificateAuthorityRequest "Google::Cloud::Security::PrivateCA::V1beta1::ActivateCertificateAuthorityRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::ActivateCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ActivateCertificateAuthorityRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def activate_certificate_authority(name: nil, pem_ca_certificate: nil, subordinate_config: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `activate_certificate_authority` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name for this [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") in the format `projects/*/locations/*/certificateAuthorities/*`. 
  * **pem_ca_certificate** (::String) — Required. The signed CA certificate issued from [FetchCertificateAuthorityCsrResponse.pem_csr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-FetchCertificateAuthorityCsrResponse#Google__Cloud__Security__PrivateCA__V1beta1__FetchCertificateAuthorityCsrResponse_pem_csr_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::FetchCertificateAuthorityCsrResponse#pem_csr \(method\)"). 
  * **subordinate_config** ([::Google::Cloud::Security::PrivateCA::V1beta1::SubordinateConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-SubordinateConfig), ::Hash) — Required. Must include information about the issuer of 'pem_ca_certificate', and any further issuers until the self-signed CA. 
  * **request_id** (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

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
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::ActivateCertificateAuthorityRequest.new
    
    # Call the activate_certificate_authority method.
    result = client.activate_certificate_authority request
    
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

Configure the CertificateAuthorityService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client#Google__Cloud__Security__PrivateCA__V1beta1__CertificateAuthorityService__Client_configure_class_ "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client-Configuration "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client-Configuration)) 



### #create_certificate
    
    
    def create_certificate(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate
    def create_certificate(parent: nil, certificate_id: nil, certificate: nil, request_id: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate

Create a new [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)") in a given Project, Location from a particular [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)").

**Overloads**
    
    
    def create_certificate(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate

Pass arguments to `create_certificate` via a request object, either of type [Google::Cloud::Security::PrivateCA::V1beta1::CreateCertificateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CreateCertificateRequest "Google::Cloud::Security::PrivateCA::V1beta1::CreateCertificateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::CreateCertificateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CreateCertificateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_certificate(parent: nil, certificate_id: nil, certificate: nil, request_id: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate

Pass arguments to `create_certificate` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the location and [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") associated with the [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)"), in the format `projects/*/locations/*/certificateAuthorities/*`. 
  * **certificate_id** (::String) — Optional. It must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`. This field is required when using a [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") in the Enterprise [CertificateAuthority.Tier](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority-Tier "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority::Tier \(module\)"), but is optional and its value is ignored otherwise. 
  * **certificate** ([::Google::Cloud::Security::PrivateCA::V1beta1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate), ::Hash) — Required. A [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)") with initial field values. 
  * **request_id** (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Security::PrivateCA::V1beta1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Security::PrivateCA::V1beta1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::CreateCertificateRequest.new
    
    # Call the create_certificate method.
    result = client.create_certificate request
    
    # The returned object is of type Google::Cloud::Security::PrivateCA::V1beta1::Certificate.
    p result

### #create_certificate_authority
    
    
    def create_certificate_authority(request, options = nil) -> ::Gapic::Operation
    def create_certificate_authority(parent: nil, certificate_authority_id: nil, certificate_authority: nil, request_id: nil) -> ::Gapic::Operation

Create a new [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") in a given Project and Location.

**Overloads**
    
    
    def create_certificate_authority(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_certificate_authority` via a request object, either of type [Google::Cloud::Security::PrivateCA::V1beta1::CreateCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CreateCertificateAuthorityRequest "Google::Cloud::Security::PrivateCA::V1beta1::CreateCertificateAuthorityRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::CreateCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CreateCertificateAuthorityRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_certificate_authority(parent: nil, certificate_authority_id: nil, certificate_authority: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_certificate_authority` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the location associated with the [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)"), in the format `projects/*/locations/*`. 
  * **certificate_authority_id** (::String) — Required. It must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`
  * **certificate_authority** ([::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority), ::Hash) — Required. A [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") with initial field values. 
  * **request_id** (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

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
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::CreateCertificateAuthorityRequest.new
    
    # Call the create_certificate_authority method.
    result = client.create_certificate_authority request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #disable_certificate_authority
    
    
    def disable_certificate_authority(request, options = nil) -> ::Gapic::Operation
    def disable_certificate_authority(name: nil, request_id: nil) -> ::Gapic::Operation

Disable a [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)").

**Overloads**
    
    
    def disable_certificate_authority(request, options = nil) -> ::Gapic::Operation

Pass arguments to `disable_certificate_authority` via a request object, either of type [DisableCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-DisableCertificateAuthorityRequest "Google::Cloud::Security::PrivateCA::V1beta1::DisableCertificateAuthorityRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::DisableCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-DisableCertificateAuthorityRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def disable_certificate_authority(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `disable_certificate_authority` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name for this [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") in the format `projects/*/locations/*/certificateAuthorities/*`. 
  * **request_id** (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

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
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::DisableCertificateAuthorityRequest.new
    
    # Call the disable_certificate_authority method.
    result = client.disable_certificate_authority request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #enable_certificate_authority
    
    
    def enable_certificate_authority(request, options = nil) -> ::Gapic::Operation
    def enable_certificate_authority(name: nil, request_id: nil) -> ::Gapic::Operation

Enable a [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)").

**Overloads**
    
    
    def enable_certificate_authority(request, options = nil) -> ::Gapic::Operation

Pass arguments to `enable_certificate_authority` via a request object, either of type [EnableCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-EnableCertificateAuthorityRequest "Google::Cloud::Security::PrivateCA::V1beta1::EnableCertificateAuthorityRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::EnableCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-EnableCertificateAuthorityRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def enable_certificate_authority(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `enable_certificate_authority` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name for this [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") in the format `projects/*/locations/*/certificateAuthorities/*`. 
  * **request_id** (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

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
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::EnableCertificateAuthorityRequest.new
    
    # Call the enable_certificate_authority method.
    result = client.enable_certificate_authority request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #fetch_certificate_authority_csr
    
    
    def fetch_certificate_authority_csr(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::FetchCertificateAuthorityCsrResponse
    def fetch_certificate_authority_csr(name: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::FetchCertificateAuthorityCsrResponse

Fetch a certificate signing request (CSR) from a [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") that is in state [PENDING_ACTIVATION](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority-State#Google__Cloud__Security__PrivateCA__V1beta1__CertificateAuthority__State__PENDING_ACTIVATION "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority::State::PENDING_ACTIVATION \(constant\)") and is of type [SUBORDINATE](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority-Type#Google__Cloud__Security__PrivateCA__V1beta1__CertificateAuthority__Type__SUBORDINATE "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority::Type::SUBORDINATE \(constant\)"). The CSR must then be signed by the desired parent Certificate Authority, which could be another [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") resource, or could be an on-prem certificate authority. See also [ActivateCertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client#Google__Cloud__Security__PrivateCA__V1beta1__CertificateAuthorityService__Client_activate_certificate_authority_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client#activate_certificate_authority \(method\)").

**Overloads**
    
    
    def fetch_certificate_authority_csr(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::FetchCertificateAuthorityCsrResponse

Pass arguments to `fetch_certificate_authority_csr` via a request object, either of type [FetchCertificateAuthorityCsrRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-FetchCertificateAuthorityCsrRequest "Google::Cloud::Security::PrivateCA::V1beta1::FetchCertificateAuthorityCsrRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::FetchCertificateAuthorityCsrRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-FetchCertificateAuthorityCsrRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def fetch_certificate_authority_csr(name: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::FetchCertificateAuthorityCsrResponse

Pass arguments to `fetch_certificate_authority_csr` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name for this [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") in the format `projects/*/locations/*/certificateAuthorities/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Security::PrivateCA::V1beta1::FetchCertificateAuthorityCsrResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-FetchCertificateAuthorityCsrResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Security::PrivateCA::V1beta1::FetchCertificateAuthorityCsrResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-FetchCertificateAuthorityCsrResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::FetchCertificateAuthorityCsrRequest.new
    
    # Call the fetch_certificate_authority_csr method.
    result = client.fetch_certificate_authority_csr request
    
    # The returned object is of type Google::Cloud::Security::PrivateCA::V1beta1::FetchCertificateAuthorityCsrResponse.
    p result

### #get_certificate
    
    
    def get_certificate(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate
    def get_certificate(name: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate

Returns a [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)").

**Overloads**
    
    
    def get_certificate(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate

Pass arguments to `get_certificate` via a request object, either of type [GetCertificateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-GetCertificateRequest "Google::Cloud::Security::PrivateCA::V1beta1::GetCertificateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::GetCertificateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-GetCertificateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_certificate(name: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate

Pass arguments to `get_certificate` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate#Google__Cloud__Security__PrivateCA__V1beta1__Certificate_name_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::Certificate#name \(method\)") of the [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)") to get. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Security::PrivateCA::V1beta1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Security::PrivateCA::V1beta1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::GetCertificateRequest.new
    
    # Call the get_certificate method.
    result = client.get_certificate request
    
    # The returned object is of type Google::Cloud::Security::PrivateCA::V1beta1::Certificate.
    p result

### #get_certificate_authority
    
    
    def get_certificate_authority(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority
    def get_certificate_authority(name: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority

Returns a [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)").

**Overloads**
    
    
    def get_certificate_authority(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority

Pass arguments to `get_certificate_authority` via a request object, either of type [GetCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-GetCertificateAuthorityRequest "Google::Cloud::Security::PrivateCA::V1beta1::GetCertificateAuthorityRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::GetCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-GetCertificateAuthorityRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_certificate_authority(name: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority

Pass arguments to `get_certificate_authority` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority#Google__Cloud__Security__PrivateCA__V1beta1__CertificateAuthority_name_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority#name \(method\)") of the [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") to get. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::GetCertificateAuthorityRequest.new
    
    # Call the get_certificate_authority method.
    result = client.get_certificate_authority request
    
    # The returned object is of type Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority.
    p result

### #get_certificate_revocation_list
    
    
    def get_certificate_revocation_list(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList
    def get_certificate_revocation_list(name: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList

Returns a [CertificateRevocationList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList "Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList \(class\)").

**Overloads**
    
    
    def get_certificate_revocation_list(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList

Pass arguments to `get_certificate_revocation_list` via a request object, either of type [GetCertificateRevocationListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-GetCertificateRevocationListRequest "Google::Cloud::Security::PrivateCA::V1beta1::GetCertificateRevocationListRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::GetCertificateRevocationListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-GetCertificateRevocationListRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_certificate_revocation_list(name: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList

Pass arguments to `get_certificate_revocation_list` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList#Google__Cloud__Security__PrivateCA__V1beta1__CertificateRevocationList_name_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList#name \(method\)") of the [CertificateRevocationList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList "Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList \(class\)") to get. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::GetCertificateRevocationListRequest.new
    
    # Call the get_certificate_revocation_list method.
    result = client.get_certificate_revocation_list request
    
    # The returned object is of type Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList.
    p result

### #get_reusable_config
    
    
    def get_reusable_config(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig
    def get_reusable_config(name: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig

Returns a [ReusableConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ReusableConfig "Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig \(class\)").

**Overloads**
    
    
    def get_reusable_config(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig

Pass arguments to `get_reusable_config` via a request object, either of type [GetReusableConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-GetReusableConfigRequest "Google::Cloud::Security::PrivateCA::V1beta1::GetReusableConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::GetReusableConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-GetReusableConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_reusable_config(name: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig

Pass arguments to `get_reusable_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The [name][ReusableConfigs.name] of the [ReusableConfigs][] to get. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ReusableConfig)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ReusableConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::GetReusableConfigRequest.new
    
    # Call the get_reusable_config method.
    result = client.get_reusable_config request
    
    # The returned object is of type Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new CertificateAuthorityService client object.

**Yields**

  * (config) — Configure the CertificateAuthorityService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_certificate_authorities
    
    
    def list_certificate_authorities(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority>
    def list_certificate_authorities(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority>

Lists [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)").

**Overloads**
    
    
    def list_certificate_authorities(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority>

Pass arguments to `list_certificate_authorities` via a request object, either of type [ListCertificateAuthoritiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateAuthoritiesRequest "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateAuthoritiesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_certificate_authorities(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority>

Pass arguments to `list_certificate_authorities` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the location associated with the [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)"), in the format `projects/*/locations/*`. 
  * **page_size** (::Integer) — Optional. Limit on the number of [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") to include in the response. Further [CertificateAuthorities](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") can subsequently be obtained by including the [ListCertificateAuthoritiesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateAuthoritiesResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListCertificateAuthoritiesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesResponse#next_page_token \(method\)") in a subsequent request. If unspecified, the server will pick an appropriate default. 
  * **page_token** (::String) — Optional. Pagination token, returned earlier via [ListCertificateAuthoritiesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateAuthoritiesResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListCertificateAuthoritiesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesResponse#next_page_token \(method\)"). 
  * **filter** (::String) — Optional. Only include resources that match the filter in the response. 
  * **order_by** (::String) — Optional. Specify how the results should be sorted. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateAuthoritiesRequest.new
    
    # Call the list_certificate_authorities method.
    result = client.list_certificate_authorities request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority.
      p item
    end

### #list_certificate_revocation_lists
    
    
    def list_certificate_revocation_lists(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList>
    def list_certificate_revocation_lists(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList>

Lists [CertificateRevocationLists](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList "Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList \(class\)").

**Overloads**
    
    
    def list_certificate_revocation_lists(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList>

Pass arguments to `list_certificate_revocation_lists` via a request object, either of type [ListCertificateRevocationListsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateRevocationListsRequest "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateRevocationListsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateRevocationListsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateRevocationListsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_certificate_revocation_lists(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList>

Pass arguments to `list_certificate_revocation_lists` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the location associated with the [CertificateRevocationLists](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList "Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList \(class\)"), in the format `projects/*/locations/*/certificateauthorities/*`. 
  * **page_size** (::Integer) — Optional. Limit on the number of [CertificateRevocationLists](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList "Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList \(class\)") to include in the response. Further [CertificateRevocationLists](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList "Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList \(class\)") can subsequently be obtained by including the [ListCertificateRevocationListsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateRevocationListsResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListCertificateRevocationListsResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateRevocationListsResponse#next_page_token \(method\)") in a subsequent request. If unspecified, the server will pick an appropriate default. 
  * **page_token** (::String) — Optional. Pagination token, returned earlier via [ListCertificateRevocationListsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificateRevocationListsResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListCertificateRevocationListsResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateRevocationListsResponse#next_page_token \(method\)"). 
  * **filter** (::String) — Optional. Only include resources that match the filter in the response. 
  * **order_by** (::String) — Optional. Specify how the results should be sorted. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::ListCertificateRevocationListsRequest.new
    
    # Call the list_certificate_revocation_lists method.
    result = client.list_certificate_revocation_lists request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList.
      p item
    end

### #list_certificates
    
    
    def list_certificates(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::Certificate>
    def list_certificates(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::Certificate>

Lists [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)").

**Overloads**
    
    
    def list_certificates(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::Certificate>

Pass arguments to `list_certificates` via a request object, either of type [ListCertificatesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificatesRequest "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificatesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::ListCertificatesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificatesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_certificates(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::Certificate>

Pass arguments to `list_certificates` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the location associated with the [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)"), in the format `projects/*/locations/*/certificateauthorities/*`. 
  * **page_size** (::Integer) — Optional. Limit on the number of [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)") to include in the response. Further [Certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)") can subsequently be obtained by including the [ListCertificatesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificatesResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListCertificatesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificatesResponse#next_page_token \(method\)") in a subsequent request. If unspecified, the server will pick an appropriate default. 
  * **page_token** (::String) — Optional. Pagination token, returned earlier via [ListCertificatesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListCertificatesResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListCertificatesResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListCertificatesResponse#next_page_token \(method\)"). 
  * **filter** (::String) — Optional. Only include resources that match the filter in the response. For details on supported filters and syntax, see [Certificates Filtering documentation](https://cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates#filtering_support). 
  * **order_by** (::String) — Optional. Specify how the results should be sorted. For details on supported fields and syntax, see [Certificates Sorting documentation](https://cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates#sorting_support). 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Security::PrivateCA::V1beta1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Security::PrivateCA::V1beta1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::ListCertificatesRequest.new
    
    # Call the list_certificates method.
    result = client.list_certificates request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate.
      p item
    end

### #list_reusable_configs
    
    
    def list_reusable_configs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig>
    def list_reusable_configs(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig>

Lists [ReusableConfigs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ReusableConfig "Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig \(class\)").

**Overloads**
    
    
    def list_reusable_configs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig>

Pass arguments to `list_reusable_configs` via a request object, either of type [ListReusableConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListReusableConfigsRequest "Google::Cloud::Security::PrivateCA::V1beta1::ListReusableConfigsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::ListReusableConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListReusableConfigsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_reusable_configs(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig>

Pass arguments to `list_reusable_configs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the location associated with the [ReusableConfigs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ReusableConfig "Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig \(class\)"), in the format `projects/*/locations/*`. 
  * **page_size** (::Integer) — Optional. Limit on the number of [ReusableConfigs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ReusableConfig "Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig \(class\)") to include in the response. Further [ReusableConfigs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ReusableConfig "Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig \(class\)") can subsequently be obtained by including the [ListReusableConfigsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListReusableConfigsResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListReusableConfigsResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListReusableConfigsResponse#next_page_token \(method\)") in a subsequent request. If unspecified, the server will pick an appropriate default. 
  * **page_token** (::String) — Optional. Pagination token, returned earlier via [ListReusableConfigsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ListReusableConfigsResponse#Google__Cloud__Security__PrivateCA__V1beta1__ListReusableConfigsResponse_next_page_token_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::ListReusableConfigsResponse#next_page_token \(method\)"). 
  * **filter** (::String) — Optional. Only include resources that match the filter in the response. 
  * **order_by** (::String) — Optional. Specify how the results should be sorted. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ReusableConfig)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ReusableConfig)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::ListReusableConfigsRequest.new
    
    # Call the list_reusable_configs method.
    result = client.list_reusable_configs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Security::PrivateCA::V1beta1::ReusableConfig.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthorityService-Operations)) 



### #restore_certificate_authority
    
    
    def restore_certificate_authority(request, options = nil) -> ::Gapic::Operation
    def restore_certificate_authority(name: nil, request_id: nil) -> ::Gapic::Operation

Restore a [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") that is scheduled for deletion.

**Overloads**
    
    
    def restore_certificate_authority(request, options = nil) -> ::Gapic::Operation

Pass arguments to `restore_certificate_authority` via a request object, either of type [RestoreCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-RestoreCertificateAuthorityRequest "Google::Cloud::Security::PrivateCA::V1beta1::RestoreCertificateAuthorityRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::RestoreCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-RestoreCertificateAuthorityRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def restore_certificate_authority(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `restore_certificate_authority` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name for this [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") in the format `projects/*/locations/*/certificateAuthorities/*`. 
  * **request_id** (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

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
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::RestoreCertificateAuthorityRequest.new
    
    # Call the restore_certificate_authority method.
    result = client.restore_certificate_authority request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #revoke_certificate
    
    
    def revoke_certificate(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate
    def revoke_certificate(name: nil, reason: nil, request_id: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate

Revoke a [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)").

**Overloads**
    
    
    def revoke_certificate(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate

Pass arguments to `revoke_certificate` via a request object, either of type [RevokeCertificateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-RevokeCertificateRequest "Google::Cloud::Security::PrivateCA::V1beta1::RevokeCertificateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::RevokeCertificateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-RevokeCertificateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def revoke_certificate(name: nil, reason: nil, request_id: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate

Pass arguments to `revoke_certificate` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name for this [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)") in the format `projects/*/locations/*/certificateAuthorities/*/certificates/*`. 
  * **reason** ([::Google::Cloud::Security::PrivateCA::V1beta1::RevocationReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-RevocationReason)) — Required. The [RevocationReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-RevocationReason "Google::Cloud::Security::PrivateCA::V1beta1::RevocationReason \(module\)") for revoking this certificate. 
  * **request_id** (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Security::PrivateCA::V1beta1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Security::PrivateCA::V1beta1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::RevokeCertificateRequest.new
    
    # Call the revoke_certificate method.
    result = client.revoke_certificate request
    
    # The returned object is of type Google::Cloud::Security::PrivateCA::V1beta1::Certificate.
    p result

### #schedule_delete_certificate_authority
    
    
    def schedule_delete_certificate_authority(request, options = nil) -> ::Gapic::Operation
    def schedule_delete_certificate_authority(name: nil, request_id: nil) -> ::Gapic::Operation

Schedule a [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") for deletion.

**Overloads**
    
    
    def schedule_delete_certificate_authority(request, options = nil) -> ::Gapic::Operation

Pass arguments to `schedule_delete_certificate_authority` via a request object, either of type [ScheduleDeleteCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ScheduleDeleteCertificateAuthorityRequest "Google::Cloud::Security::PrivateCA::V1beta1::ScheduleDeleteCertificateAuthorityRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::ScheduleDeleteCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-ScheduleDeleteCertificateAuthorityRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def schedule_delete_certificate_authority(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `schedule_delete_certificate_authority` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name for this [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") in the format `projects/*/locations/*/certificateAuthorities/*`. 
  * **request_id** (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

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
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::ScheduleDeleteCertificateAuthorityRequest.new
    
    # Call the schedule_delete_certificate_authority method.
    result = client.schedule_delete_certificate_authority request
    
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



### #update_certificate
    
    
    def update_certificate(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate
    def update_certificate(certificate: nil, update_mask: nil, request_id: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate

Update a [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)"). Currently, the only field you can update is the [labels](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate#Google__Cloud__Security__PrivateCA__V1beta1__Certificate_labels_instance_ "Google::Cloud::Security::PrivateCA::V1beta1::Certificate#labels \(method\)") field.

**Overloads**
    
    
    def update_certificate(request, options = nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate

Pass arguments to `update_certificate` via a request object, either of type [UpdateCertificateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-UpdateCertificateRequest "Google::Cloud::Security::PrivateCA::V1beta1::UpdateCertificateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::UpdateCertificateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-UpdateCertificateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_certificate(certificate: nil, update_mask: nil, request_id: nil) -> ::Google::Cloud::Security::PrivateCA::V1beta1::Certificate

Pass arguments to `update_certificate` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **certificate** ([::Google::Cloud::Security::PrivateCA::V1beta1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate), ::Hash) — Required. [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate "Google::Cloud::Security::PrivateCA::V1beta1::Certificate \(class\)") with updated values. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. A list of fields to be updated in this request. 
  * **request_id** (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Security::PrivateCA::V1beta1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Security::PrivateCA::V1beta1::Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-Certificate)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::UpdateCertificateRequest.new
    
    # Call the update_certificate method.
    result = client.update_certificate request
    
    # The returned object is of type Google::Cloud::Security::PrivateCA::V1beta1::Certificate.
    p result

### #update_certificate_authority
    
    
    def update_certificate_authority(request, options = nil) -> ::Gapic::Operation
    def update_certificate_authority(certificate_authority: nil, update_mask: nil, request_id: nil) -> ::Gapic::Operation

Update a [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)").

**Overloads**
    
    
    def update_certificate_authority(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_certificate_authority` via a request object, either of type [UpdateCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-UpdateCertificateAuthorityRequest "Google::Cloud::Security::PrivateCA::V1beta1::UpdateCertificateAuthorityRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::UpdateCertificateAuthorityRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-UpdateCertificateAuthorityRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_certificate_authority(certificate_authority: nil, update_mask: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_certificate_authority` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **certificate_authority** ([::Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority), ::Hash) — Required. [CertificateAuthority](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateAuthority "Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthority \(class\)") with updated values. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. A list of fields to be updated in this request. 
  * **request_id** (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

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
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::UpdateCertificateAuthorityRequest.new
    
    # Call the update_certificate_authority method.
    result = client.update_certificate_authority request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_certificate_revocation_list
    
    
    def update_certificate_revocation_list(request, options = nil) -> ::Gapic::Operation
    def update_certificate_revocation_list(certificate_revocation_list: nil, update_mask: nil, request_id: nil) -> ::Gapic::Operation

Update a [CertificateRevocationList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList "Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList \(class\)").

**Overloads**
    
    
    def update_certificate_revocation_list(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_certificate_revocation_list` via a request object, either of type [UpdateCertificateRevocationListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-UpdateCertificateRevocationListRequest "Google::Cloud::Security::PrivateCA::V1beta1::UpdateCertificateRevocationListRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Security::PrivateCA::V1beta1::UpdateCertificateRevocationListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-UpdateCertificateRevocationListRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_certificate_revocation_list(certificate_revocation_list: nil, update_mask: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_certificate_revocation_list` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **certificate_revocation_list** ([::Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList), ::Hash) — Required. [CertificateRevocationList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Cloud-Security-PrivateCA-V1beta1-CertificateRevocationList "Google::Cloud::Security::PrivateCA::V1beta1::CertificateRevocationList \(class\)") with updated values. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1beta1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. A list of fields to be updated in this request. 
  * **request_id** (::String) — Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

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
    
    
    require "google/cloud/security/private_ca/v1beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Security::PrivateCA::V1beta1::CertificateAuthorityService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Security::PrivateCA::V1beta1::UpdateCertificateRevocationListRequest.new
    
    # Call the update_certificate_revocation_list method.
    result = client.update_certificate_revocation_list request
    
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
