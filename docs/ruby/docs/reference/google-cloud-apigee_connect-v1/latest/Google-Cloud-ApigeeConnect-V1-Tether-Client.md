---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Tether-Client/
title: Apigee Connect V1 API - Class Google::Cloud::ApigeeConnect::V1::Tether::Client (v1.7.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:33.038665+00:00
---

# Apigee Connect V1 API - Class Google::Cloud::ApigeeConnect::V1::Tether::Client (v1.7.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Tether-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Apigee Connect V1 API - Class Google::Cloud::ApigeeConnect::V1::Tether::Client (v1.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.2 (latest)  1.7.1  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Apigee Connect V1 API class Google::Cloud::ApigeeConnect::V1::Tether::Client.

Client for the Tether service.

Tether provides a way for the control plane to send HTTP API requests to services in data planes that runs in a remote datacenter without requiring customers to open firewalls on their runtime plane.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Tether Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Tether-Client-Configuration "Google::Cloud::ApigeeConnect::V1::Tether::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Tether-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Tether-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Tether clients
    ::Google::Cloud::ApigeeConnect::V1::Tether::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Tether Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Tether-Client#Google__Cloud__ApigeeConnect__V1__Tether__Client_configure_class_ "Google::Cloud::ApigeeConnect::V1::Tether::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Tether-Client-Configuration "Google::Cloud::ApigeeConnect::V1::Tether::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Tether-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Tether-Client-Configuration)) 



### #egress
    
    
    def egress(request, options = nil) { |response, operation| ... } -> ::Enumerable<::Google::Cloud::ApigeeConnect::V1::EgressRequest>

Egress streams egress requests and responses. Logically, this is not actually a streaming request, but uses streaming as a mechanism to flip the client-server relationship of gRPC so that the server can act as a client. The listener, the RPC server, accepts connections from the dialer, the RPC client. The listener streams http requests and the dialer streams http responses.

**Parameters**

  * **request** (::Gapic::StreamInput, ::Enumerable<[::Google::Cloud::ApigeeConnect::V1::EgressResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-EgressResponse), ::Hash>) — An enumerable of [EgressResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-EgressResponse "Google::Cloud::ApigeeConnect::V1::EgressResponse \(class\)") instances. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Enumerable<[::Google::Cloud::ApigeeConnect::V1::EgressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-EgressRequest)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Enumerable<[::Google::Cloud::ApigeeConnect::V1::EgressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-EgressRequest)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_connect/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeConnect::V1::Tether::Client.new
    
    # Create an input stream.
    input = Gapic::StreamInput.new
    
    # Call the egress method to start streaming.
    output = client.egress input
    
    # Send requests on the stream. For each request object, set fields by
    # passing keyword arguments. Be sure to close the stream when done.
    input << Google::Cloud::ApigeeConnect::V1::EgressResponse.new
    input << Google::Cloud::ApigeeConnect::V1::EgressResponse.new
    input.close
    
    # The returned object is a streamed enumerable yielding elements of type
    # ::Google::Cloud::ApigeeConnect::V1::EgressRequest
    output.each do |current_response|
      p current_response
    end

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Tether client object.

**Yields**

  * (config) — Configure the Tether client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Tether-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Tether-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::ApigeeConnect::V1::Tether::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::ApigeeConnect::V1::Tether::Client.new do |config|
      config.timeout = 10.0
    end

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
