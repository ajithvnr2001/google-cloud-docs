---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Rest-Client/
title: Financial Services V1 API - Class Google::Cloud::FinancialServices::V1::AML::Rest::Client (v1.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:26.367323+00:00
---

# Financial Services V1 API - Class Google::Cloud::FinancialServices::V1::AML::Rest::Client (v1.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Financial Services V1 API - Class Google::Cloud::FinancialServices::V1::AML::Rest::Client (v1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  0.7.0  0.6.1  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Financial Services V1 API class Google::Cloud::FinancialServices::V1::AML::Rest::Client.

REST client for the AML service.

The AML (Anti Money Laundering) service allows users to perform REST operations on aml.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::FinancialServices::V1::AML::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the AML Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Rest-Client-Configuration "Google::Cloud::FinancialServices::V1::AML::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all AML clients
    ::Google::Cloud::FinancialServices::V1::AML::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the AML Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Rest-Client#Google__Cloud__FinancialServices__V1__AML__Rest__Client_configure_class_ "Google::Cloud::FinancialServices::V1::AML::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Rest-Client-Configuration "Google::Cloud::FinancialServices::V1::AML::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Rest-Client-Configuration)) 



### #create_backtest_result
    
    
    def create_backtest_result(request, options = nil) -> ::Gapic::Operation
    def create_backtest_result(parent: nil, backtest_result_id: nil, backtest_result: nil, request_id: nil) -> ::Gapic::Operation

Create a BacktestResult.

**Overloads**
    
    
    def create_backtest_result(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_backtest_result` via a request object, either of type [CreateBacktestResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-CreateBacktestResultRequest "Google::Cloud::FinancialServices::V1::CreateBacktestResultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::CreateBacktestResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-CreateBacktestResultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_backtest_result(parent: nil, backtest_result_id: nil, backtest_result: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_backtest_result` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the BacktestResult is the Instance. 
  * **backtest_result_id** (::String) — Required. The resource id of the BacktestResult 
  * **backtest_result** ([::Google::Cloud::FinancialServices::V1::BacktestResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BacktestResult), ::Hash) — Required. The BacktestResult that will be created. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::CreateBacktestResultRequest.new
    
    # Call the create_backtest_result method.
    result = client.create_backtest_result request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_dataset
    
    
    def create_dataset(request, options = nil) -> ::Gapic::Operation
    def create_dataset(parent: nil, dataset_id: nil, dataset: nil, request_id: nil) -> ::Gapic::Operation

Creates a dataset.

**Overloads**
    
    
    def create_dataset(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_dataset` via a request object, either of type [CreateDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-CreateDatasetRequest "Google::Cloud::FinancialServices::V1::CreateDatasetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::CreateDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-CreateDatasetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_dataset(parent: nil, dataset_id: nil, dataset: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_dataset` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the Dataset is the Instance. 
  * **dataset_id** (::String) — Required. The resource id of the dataset 
  * **dataset** ([::Google::Cloud::FinancialServices::V1::Dataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Dataset), ::Hash) — Required. The dataset that will be created. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::CreateDatasetRequest.new
    
    # Call the create_dataset method.
    result = client.create_dataset request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_engine_config
    
    
    def create_engine_config(request, options = nil) -> ::Gapic::Operation
    def create_engine_config(parent: nil, engine_config_id: nil, engine_config: nil, request_id: nil) -> ::Gapic::Operation

Creates an engine config.

**Overloads**
    
    
    def create_engine_config(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_engine_config` via a request object, either of type [CreateEngineConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-CreateEngineConfigRequest "Google::Cloud::FinancialServices::V1::CreateEngineConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::CreateEngineConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-CreateEngineConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_engine_config(parent: nil, engine_config_id: nil, engine_config: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_engine_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the EngineConfig is the Instance. 
  * **engine_config_id** (::String) — Required. The resource id of the EngineConfig 
  * **engine_config** ([::Google::Cloud::FinancialServices::V1::EngineConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-EngineConfig), ::Hash) — Required. The EngineConfig that will be created. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::CreateEngineConfigRequest.new
    
    # Call the create_engine_config method.
    result = client.create_engine_config request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_instance
    
    
    def create_instance(request, options = nil) -> ::Gapic::Operation
    def create_instance(parent: nil, instance_id: nil, instance: nil, request_id: nil) -> ::Gapic::Operation

Creates an instance.

**Overloads**
    
    
    def create_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_instance` via a request object, either of type [CreateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-CreateInstanceRequest "Google::Cloud::FinancialServices::V1::CreateInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::CreateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-CreateInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_instance(parent: nil, instance_id: nil, instance: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the Instance is the location for that Instance. Every location has exactly one instance. 
  * **instance_id** (::String) — Required. The resource id of the instance. 
  * **instance** ([::Google::Cloud::FinancialServices::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Instance), ::Hash) — Required. The instance that will be created. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::CreateInstanceRequest.new
    
    # Call the create_instance method.
    result = client.create_instance request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_model
    
    
    def create_model(request, options = nil) -> ::Gapic::Operation
    def create_model(parent: nil, model_id: nil, model: nil, request_id: nil) -> ::Gapic::Operation

Creates a model.

**Overloads**
    
    
    def create_model(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_model` via a request object, either of type [CreateModelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-CreateModelRequest "Google::Cloud::FinancialServices::V1::CreateModelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::CreateModelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-CreateModelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_model(parent: nil, model_id: nil, model: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_model` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the Model is the Instance. 
  * **model_id** (::String) — Required. The resource id of the Model 
  * **model** ([::Google::Cloud::FinancialServices::V1::Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Model), ::Hash) — Required. The Model that will be created. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::CreateModelRequest.new
    
    # Call the create_model method.
    result = client.create_model request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_prediction_result
    
    
    def create_prediction_result(request, options = nil) -> ::Gapic::Operation
    def create_prediction_result(parent: nil, prediction_result_id: nil, prediction_result: nil, request_id: nil) -> ::Gapic::Operation

Create a PredictionResult.

**Overloads**
    
    
    def create_prediction_result(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_prediction_result` via a request object, either of type [CreatePredictionResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-CreatePredictionResultRequest "Google::Cloud::FinancialServices::V1::CreatePredictionResultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::CreatePredictionResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-CreatePredictionResultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_prediction_result(parent: nil, prediction_result_id: nil, prediction_result: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_prediction_result` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the PredictionResult is the Instance. 
  * **prediction_result_id** (::String) — Required. The resource id of the PredictionResult 
  * **prediction_result** ([::Google::Cloud::FinancialServices::V1::PredictionResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-PredictionResult), ::Hash) — Required. The PredictionResult that will be created. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::CreatePredictionResultRequest.new
    
    # Call the create_prediction_result method.
    result = client.create_prediction_result request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_backtest_result
    
    
    def delete_backtest_result(request, options = nil) -> ::Gapic::Operation
    def delete_backtest_result(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a BacktestResult.

**Overloads**
    
    
    def delete_backtest_result(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_backtest_result` via a request object, either of type [DeleteBacktestResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-DeleteBacktestResultRequest "Google::Cloud::FinancialServices::V1::DeleteBacktestResultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::DeleteBacktestResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-DeleteBacktestResultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_backtest_result(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_backtest_result` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the BacktestResult. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::DeleteBacktestResultRequest.new
    
    # Call the delete_backtest_result method.
    result = client.delete_backtest_result request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_dataset
    
    
    def delete_dataset(request, options = nil) -> ::Gapic::Operation
    def delete_dataset(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a dataset.

**Overloads**
    
    
    def delete_dataset(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_dataset` via a request object, either of type [DeleteDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-DeleteDatasetRequest "Google::Cloud::FinancialServices::V1::DeleteDatasetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::DeleteDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-DeleteDatasetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_dataset(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_dataset` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the Dataset. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::DeleteDatasetRequest.new
    
    # Call the delete_dataset method.
    result = client.delete_dataset request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_engine_config
    
    
    def delete_engine_config(request, options = nil) -> ::Gapic::Operation
    def delete_engine_config(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes an engine config.

**Overloads**
    
    
    def delete_engine_config(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_engine_config` via a request object, either of type [DeleteEngineConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-DeleteEngineConfigRequest "Google::Cloud::FinancialServices::V1::DeleteEngineConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::DeleteEngineConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-DeleteEngineConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_engine_config(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_engine_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the EngineConfig. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::DeleteEngineConfigRequest.new
    
    # Call the delete_engine_config method.
    result = client.delete_engine_config request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_instance
    
    
    def delete_instance(request, options = nil) -> ::Gapic::Operation
    def delete_instance(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes an instance.

**Overloads**
    
    
    def delete_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_instance` via a request object, either of type [DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-DeleteInstanceRequest "Google::Cloud::FinancialServices::V1::DeleteInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-DeleteInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_instance(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the Instance. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::DeleteInstanceRequest.new
    
    # Call the delete_instance method.
    result = client.delete_instance request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_model
    
    
    def delete_model(request, options = nil) -> ::Gapic::Operation
    def delete_model(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a model.

**Overloads**
    
    
    def delete_model(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_model` via a request object, either of type [DeleteModelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-DeleteModelRequest "Google::Cloud::FinancialServices::V1::DeleteModelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::DeleteModelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-DeleteModelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_model(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_model` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the Model. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::DeleteModelRequest.new
    
    # Call the delete_model method.
    result = client.delete_model request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_prediction_result
    
    
    def delete_prediction_result(request, options = nil) -> ::Gapic::Operation
    def delete_prediction_result(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a PredictionResult.

**Overloads**
    
    
    def delete_prediction_result(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_prediction_result` via a request object, either of type [DeletePredictionResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-DeletePredictionResultRequest "Google::Cloud::FinancialServices::V1::DeletePredictionResultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::DeletePredictionResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-DeletePredictionResultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_prediction_result(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_prediction_result` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the PredictionResult. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::DeletePredictionResultRequest.new
    
    # Call the delete_prediction_result method.
    result = client.delete_prediction_result request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #export_backtest_result_metadata
    
    
    def export_backtest_result_metadata(request, options = nil) -> ::Gapic::Operation
    def export_backtest_result_metadata(backtest_result: nil, structured_metadata_destination: nil) -> ::Gapic::Operation

Export governance information for a BacktestResult resource. For information on the exported fields, see [AML output data model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#backtest-results).

**Overloads**
    
    
    def export_backtest_result_metadata(request, options = nil) -> ::Gapic::Operation

Pass arguments to `export_backtest_result_metadata` via a request object, either of type [ExportBacktestResultMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ExportBacktestResultMetadataRequest "Google::Cloud::FinancialServices::V1::ExportBacktestResultMetadataRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ExportBacktestResultMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ExportBacktestResultMetadataRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def export_backtest_result_metadata(backtest_result: nil, structured_metadata_destination: nil) -> ::Gapic::Operation

Pass arguments to `export_backtest_result_metadata` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **backtest_result** (::String) — Required. The resource name of the BacktestResult. 
  * **structured_metadata_destination** ([::Google::Cloud::FinancialServices::V1::BigQueryDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BigQueryDestination), ::Hash) — Required. BigQuery output where the metadata will be written. 



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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ExportBacktestResultMetadataRequest.new
    
    # Call the export_backtest_result_metadata method.
    result = client.export_backtest_result_metadata request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #export_engine_config_metadata
    
    
    def export_engine_config_metadata(request, options = nil) -> ::Gapic::Operation
    def export_engine_config_metadata(engine_config: nil, structured_metadata_destination: nil) -> ::Gapic::Operation

Export governance information for an EngineConfig resource. For information on the exported fields, see [AML output data model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#engine-config).

**Overloads**
    
    
    def export_engine_config_metadata(request, options = nil) -> ::Gapic::Operation

Pass arguments to `export_engine_config_metadata` via a request object, either of type [ExportEngineConfigMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ExportEngineConfigMetadataRequest "Google::Cloud::FinancialServices::V1::ExportEngineConfigMetadataRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ExportEngineConfigMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ExportEngineConfigMetadataRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def export_engine_config_metadata(engine_config: nil, structured_metadata_destination: nil) -> ::Gapic::Operation

Pass arguments to `export_engine_config_metadata` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **engine_config** (::String) — Required. The resource name of the EngineConfig. 
  * **structured_metadata_destination** ([::Google::Cloud::FinancialServices::V1::BigQueryDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BigQueryDestination), ::Hash) — Required. BigQuery output where the metadata will be written. 



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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ExportEngineConfigMetadataRequest.new
    
    # Call the export_engine_config_metadata method.
    result = client.export_engine_config_metadata request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #export_model_metadata
    
    
    def export_model_metadata(request, options = nil) -> ::Gapic::Operation
    def export_model_metadata(model: nil, structured_metadata_destination: nil) -> ::Gapic::Operation

Export governance information for a Model resource. For information on the exported fields, see [AML output data model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#model).

**Overloads**
    
    
    def export_model_metadata(request, options = nil) -> ::Gapic::Operation

Pass arguments to `export_model_metadata` via a request object, either of type [ExportModelMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ExportModelMetadataRequest "Google::Cloud::FinancialServices::V1::ExportModelMetadataRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ExportModelMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ExportModelMetadataRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def export_model_metadata(model: nil, structured_metadata_destination: nil) -> ::Gapic::Operation

Pass arguments to `export_model_metadata` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **model** (::String) — Required. The resource name of the Model. 
  * **structured_metadata_destination** ([::Google::Cloud::FinancialServices::V1::BigQueryDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BigQueryDestination), ::Hash) — Required. BigQuery output where the metadata will be written. 



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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ExportModelMetadataRequest.new
    
    # Call the export_model_metadata method.
    result = client.export_model_metadata request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #export_prediction_result_metadata
    
    
    def export_prediction_result_metadata(request, options = nil) -> ::Gapic::Operation
    def export_prediction_result_metadata(prediction_result: nil, structured_metadata_destination: nil) -> ::Gapic::Operation

Export governance information for a PredictionResult resource. For information on the exported fields, see [AML output data model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#prediction-results).

**Overloads**
    
    
    def export_prediction_result_metadata(request, options = nil) -> ::Gapic::Operation

Pass arguments to `export_prediction_result_metadata` via a request object, either of type [ExportPredictionResultMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ExportPredictionResultMetadataRequest "Google::Cloud::FinancialServices::V1::ExportPredictionResultMetadataRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ExportPredictionResultMetadataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ExportPredictionResultMetadataRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def export_prediction_result_metadata(prediction_result: nil, structured_metadata_destination: nil) -> ::Gapic::Operation

Pass arguments to `export_prediction_result_metadata` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **prediction_result** (::String) — Required. The resource name of the PredictionResult. 
  * **structured_metadata_destination** ([::Google::Cloud::FinancialServices::V1::BigQueryDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BigQueryDestination), ::Hash) — Required. BigQuery output where the metadata will be written. 



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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ExportPredictionResultMetadataRequest.new
    
    # Call the export_prediction_result_metadata method.
    result = client.export_prediction_result_metadata request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #export_registered_parties
    
    
    def export_registered_parties(request, options = nil) -> ::Gapic::Operation
    def export_registered_parties(name: nil, dataset: nil, line_of_business: nil) -> ::Gapic::Operation

Exports the list of registered parties. See [Create and manage instances](https://cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances#export-registered-parties) for information on the output schema for this method.

**Overloads**
    
    
    def export_registered_parties(request, options = nil) -> ::Gapic::Operation

Pass arguments to `export_registered_parties` via a request object, either of type [ExportRegisteredPartiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ExportRegisteredPartiesRequest "Google::Cloud::FinancialServices::V1::ExportRegisteredPartiesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ExportRegisteredPartiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ExportRegisteredPartiesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def export_registered_parties(name: nil, dataset: nil, line_of_business: nil) -> ::Gapic::Operation

Pass arguments to `export_registered_parties` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The full path to the Instance resource in this API. format: `projects/{project}/locations/{location}/instances/{instance}`
  * **dataset** ([::Google::Cloud::FinancialServices::V1::BigQueryDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BigQueryDestination), ::Hash) — Required. The location to output the RegisteredParties. 
  * **line_of_business** ([::Google::Cloud::FinancialServices::V1::LineOfBusiness](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-LineOfBusiness)) — Required. LineOfBusiness to get RegisteredParties from. 



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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ExportRegisteredPartiesRequest.new
    
    # Call the export_registered_parties method.
    result = client.export_registered_parties request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_backtest_result
    
    
    def get_backtest_result(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::BacktestResult
    def get_backtest_result(name: nil) -> ::Google::Cloud::FinancialServices::V1::BacktestResult

Gets a BacktestResult.

**Overloads**
    
    
    def get_backtest_result(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::BacktestResult

Pass arguments to `get_backtest_result` via a request object, either of type [GetBacktestResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetBacktestResultRequest "Google::Cloud::FinancialServices::V1::GetBacktestResultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::GetBacktestResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetBacktestResultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backtest_result(name: nil) -> ::Google::Cloud::FinancialServices::V1::BacktestResult

Pass arguments to `get_backtest_result` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the BacktestResult 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::FinancialServices::V1::BacktestResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BacktestResult)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::FinancialServices::V1::BacktestResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BacktestResult)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::GetBacktestResultRequest.new
    
    # Call the get_backtest_result method.
    result = client.get_backtest_result request
    
    # The returned object is of type Google::Cloud::FinancialServices::V1::BacktestResult.
    p result

### #get_dataset
    
    
    def get_dataset(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::Dataset
    def get_dataset(name: nil) -> ::Google::Cloud::FinancialServices::V1::Dataset

Gets a dataset.

**Overloads**
    
    
    def get_dataset(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::Dataset

Pass arguments to `get_dataset` via a request object, either of type [GetDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetDatasetRequest "Google::Cloud::FinancialServices::V1::GetDatasetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::GetDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetDatasetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_dataset(name: nil) -> ::Google::Cloud::FinancialServices::V1::Dataset

Pass arguments to `get_dataset` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the Dataset 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::FinancialServices::V1::Dataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Dataset)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::FinancialServices::V1::Dataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Dataset)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::GetDatasetRequest.new
    
    # Call the get_dataset method.
    result = client.get_dataset request
    
    # The returned object is of type Google::Cloud::FinancialServices::V1::Dataset.
    p result

### #get_engine_config
    
    
    def get_engine_config(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::EngineConfig
    def get_engine_config(name: nil) -> ::Google::Cloud::FinancialServices::V1::EngineConfig

Gets an engine config.

**Overloads**
    
    
    def get_engine_config(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::EngineConfig

Pass arguments to `get_engine_config` via a request object, either of type [GetEngineConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetEngineConfigRequest "Google::Cloud::FinancialServices::V1::GetEngineConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::GetEngineConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetEngineConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_engine_config(name: nil) -> ::Google::Cloud::FinancialServices::V1::EngineConfig

Pass arguments to `get_engine_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the EngineConfig 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::FinancialServices::V1::EngineConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-EngineConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::FinancialServices::V1::EngineConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-EngineConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::GetEngineConfigRequest.new
    
    # Call the get_engine_config method.
    result = client.get_engine_config request
    
    # The returned object is of type Google::Cloud::FinancialServices::V1::EngineConfig.
    p result

### #get_engine_version
    
    
    def get_engine_version(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::EngineVersion
    def get_engine_version(name: nil) -> ::Google::Cloud::FinancialServices::V1::EngineVersion

Gets a single EngineVersion.

**Overloads**
    
    
    def get_engine_version(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::EngineVersion

Pass arguments to `get_engine_version` via a request object, either of type [GetEngineVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetEngineVersionRequest "Google::Cloud::FinancialServices::V1::GetEngineVersionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::GetEngineVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetEngineVersionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_engine_version(name: nil) -> ::Google::Cloud::FinancialServices::V1::EngineVersion

Pass arguments to `get_engine_version` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the EngineVersion 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::FinancialServices::V1::EngineVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-EngineVersion)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::FinancialServices::V1::EngineVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-EngineVersion)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::GetEngineVersionRequest.new
    
    # Call the get_engine_version method.
    result = client.get_engine_version request
    
    # The returned object is of type Google::Cloud::FinancialServices::V1::EngineVersion.
    p result

### #get_instance
    
    
    def get_instance(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::Instance
    def get_instance(name: nil) -> ::Google::Cloud::FinancialServices::V1::Instance

Gets an instance.

**Overloads**
    
    
    def get_instance(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::Instance

Pass arguments to `get_instance` via a request object, either of type [GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetInstanceRequest "Google::Cloud::FinancialServices::V1::GetInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_instance(name: nil) -> ::Google::Cloud::FinancialServices::V1::Instance

Pass arguments to `get_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the Instance. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::FinancialServices::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Instance)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::FinancialServices::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Instance)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::GetInstanceRequest.new
    
    # Call the get_instance method.
    result = client.get_instance request
    
    # The returned object is of type Google::Cloud::FinancialServices::V1::Instance.
    p result

### #get_model
    
    
    def get_model(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::Model
    def get_model(name: nil) -> ::Google::Cloud::FinancialServices::V1::Model

Gets a model.

**Overloads**
    
    
    def get_model(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::Model

Pass arguments to `get_model` via a request object, either of type [GetModelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetModelRequest "Google::Cloud::FinancialServices::V1::GetModelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::GetModelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetModelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_model(name: nil) -> ::Google::Cloud::FinancialServices::V1::Model

Pass arguments to `get_model` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the Model 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::FinancialServices::V1::Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Model)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::FinancialServices::V1::Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Model)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::GetModelRequest.new
    
    # Call the get_model method.
    result = client.get_model request
    
    # The returned object is of type Google::Cloud::FinancialServices::V1::Model.
    p result

### #get_prediction_result
    
    
    def get_prediction_result(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::PredictionResult
    def get_prediction_result(name: nil) -> ::Google::Cloud::FinancialServices::V1::PredictionResult

Gets a PredictionResult.

**Overloads**
    
    
    def get_prediction_result(request, options = nil) -> ::Google::Cloud::FinancialServices::V1::PredictionResult

Pass arguments to `get_prediction_result` via a request object, either of type [GetPredictionResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetPredictionResultRequest "Google::Cloud::FinancialServices::V1::GetPredictionResultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::GetPredictionResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-GetPredictionResultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_prediction_result(name: nil) -> ::Google::Cloud::FinancialServices::V1::PredictionResult

Pass arguments to `get_prediction_result` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the PredictionResult 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::FinancialServices::V1::PredictionResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-PredictionResult)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::FinancialServices::V1::PredictionResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-PredictionResult)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::GetPredictionResultRequest.new
    
    # Call the get_prediction_result method.
    result = client.get_prediction_result request
    
    # The returned object is of type Google::Cloud::FinancialServices::V1::PredictionResult.
    p result

### #import_registered_parties
    
    
    def import_registered_parties(request, options = nil) -> ::Gapic::Operation
    def import_registered_parties(name: nil, party_tables: nil, mode: nil, validate_only: nil, line_of_business: nil) -> ::Gapic::Operation

Imports the list of registered parties. See [Create and manage instances](https://cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances#import-registered-parties) for information on the input schema and response for this method.

**Overloads**
    
    
    def import_registered_parties(request, options = nil) -> ::Gapic::Operation

Pass arguments to `import_registered_parties` via a request object, either of type [ImportRegisteredPartiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ImportRegisteredPartiesRequest "Google::Cloud::FinancialServices::V1::ImportRegisteredPartiesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ImportRegisteredPartiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ImportRegisteredPartiesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def import_registered_parties(name: nil, party_tables: nil, mode: nil, validate_only: nil, line_of_business: nil) -> ::Gapic::Operation

Pass arguments to `import_registered_parties` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The full path to the Instance resource in this API. format: `projects/{project}/locations/{location}/instances/{instance}`
  * **party_tables** (::Array<::String>) — Optional. List of BigQuery tables. Union of tables will be taken if there is more than one table. VPC-SC restrictions apply. format: `bq://{project}.{bqDatasetID}.{bqTableID}` Use of `datasets` is preferred over the latter due to its simplicity and the reduced risk of errors `party_tables` and `datasets` must not be provided at the same time 
  * **mode** ([::Google::Cloud::FinancialServices::V1::ImportRegisteredPartiesRequest::UpdateMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ImportRegisteredPartiesRequest-UpdateMode)) — Required. Mode of the request. 
  * **validate_only** (::Boolean) — Optional. If the request will not register the parties, just determine what would happen. 
  * **line_of_business** ([::Google::Cloud::FinancialServices::V1::LineOfBusiness](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-LineOfBusiness)) — Required. LineOfBusiness for the specified registered parties. 



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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ImportRegisteredPartiesRequest.new
    
    # Call the import_registered_parties method.
    result = client.import_registered_parties request
    
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

Create a new AML REST client object.

**Yields**

  * (config) — Configure the AML client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::FinancialServices::V1::AML::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_backtest_results
    
    
    def list_backtest_results(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::BacktestResult>
    def list_backtest_results(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::BacktestResult>

List BacktestResults.

**Overloads**
    
    
    def list_backtest_results(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::BacktestResult>

Pass arguments to `list_backtest_results` via a request object, either of type [ListBacktestResultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListBacktestResultsRequest "Google::Cloud::FinancialServices::V1::ListBacktestResultsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ListBacktestResultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListBacktestResultsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backtest_results(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::BacktestResult>

Pass arguments to `list_backtest_results` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the BacktestResult is the Instance. 
  * **page_size** (::Integer) — The number of resources to be included in the response. The response contains a next_page_token, which can be used to retrieve the next page of resources. 
  * **page_token** (::String) — In case of paginated results, this is the token that was returned in the previous ListBacktestResultsResponse. It should be copied here to retrieve the next page of resources. Empty will give the first page of ListBacktestResultsRequest, and the last page will return an empty page_token. 
  * **filter** (::String) — Specify a filter to narrow search results. 
  * **order_by** (::String) — Specify a field to use for ordering. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::BacktestResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BacktestResult)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::BacktestResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BacktestResult)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ListBacktestResultsRequest.new
    
    # Call the list_backtest_results method.
    result = client.list_backtest_results request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::FinancialServices::V1::BacktestResult.
      p item
    end

### #list_datasets
    
    
    def list_datasets(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::Dataset>
    def list_datasets(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::Dataset>

Lists datasets.

**Overloads**
    
    
    def list_datasets(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::Dataset>

Pass arguments to `list_datasets` via a request object, either of type [ListDatasetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListDatasetsRequest "Google::Cloud::FinancialServices::V1::ListDatasetsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ListDatasetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListDatasetsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_datasets(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::Dataset>

Pass arguments to `list_datasets` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the Dataset is the Instance. 
  * **page_size** (::Integer) — The number of resources to be included in the response. The response contains a next_page_token, which can be used to retrieve the next page of resources. 
  * **page_token** (::String) — In case of paginated results, this is the token that was returned in the previous ListDatasetResponse. It should be copied here to retrieve the next page of resources. Empty will give the first page of ListDatasetRequest, and the last page will return an empty page_token. 
  * **filter** (::String) — Specify a filter to narrow search results. 
  * **order_by** (::String) — Specify a field to use for ordering. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::Dataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Dataset)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::Dataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Dataset)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ListDatasetsRequest.new
    
    # Call the list_datasets method.
    result = client.list_datasets request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::FinancialServices::V1::Dataset.
      p item
    end

### #list_engine_configs
    
    
    def list_engine_configs(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::EngineConfig>
    def list_engine_configs(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::EngineConfig>

Lists engine configs.

**Overloads**
    
    
    def list_engine_configs(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::EngineConfig>

Pass arguments to `list_engine_configs` via a request object, either of type [ListEngineConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListEngineConfigsRequest "Google::Cloud::FinancialServices::V1::ListEngineConfigsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ListEngineConfigsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListEngineConfigsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_engine_configs(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::EngineConfig>

Pass arguments to `list_engine_configs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the EngineConfig is the Instance. 
  * **page_size** (::Integer) — The number of resources to be included in the response. The response contains a next_page_token, which can be used to retrieve the next page of resources. 
  * **page_token** (::String) — In case of paginated results, this is the token that was returned in the previous ListEngineConfigsResponse. It should be copied here to retrieve the next page of resources. Empty will give the first page of ListEngineConfigsRequest, and the last page will return an empty page_token. 
  * **filter** (::String) — Specify a filter to narrow search results. 
  * **order_by** (::String) — Specify a field to use for ordering. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::EngineConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-EngineConfig)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::EngineConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-EngineConfig)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ListEngineConfigsRequest.new
    
    # Call the list_engine_configs method.
    result = client.list_engine_configs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::FinancialServices::V1::EngineConfig.
      p item
    end

### #list_engine_versions
    
    
    def list_engine_versions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::EngineVersion>
    def list_engine_versions(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::EngineVersion>

Lists EngineVersions for given location.

**Overloads**
    
    
    def list_engine_versions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::EngineVersion>

Pass arguments to `list_engine_versions` via a request object, either of type [ListEngineVersionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListEngineVersionsRequest "Google::Cloud::FinancialServices::V1::ListEngineVersionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ListEngineVersionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListEngineVersionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_engine_versions(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::EngineVersion>

Pass arguments to `list_engine_versions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the EngineVersion is the Instance. 
  * **page_size** (::Integer) — Optional. The number of resources to be included in the response. The response contains a next_page_token, which can be used to retrieve the next page of resources. 
  * **page_token** (::String) — Optional. In case of paginated results, this is the token that was returned in the previous ListEngineVersionsResponse. It should be copied here to retrieve the next page of resources. Empty will give the first page of ListEngineVersionsRequest, and the last page will return an empty page_token. 
  * **filter** (::String) — Optional. Specify a filter to narrow search results. If empty or unset will default to "state!=DEPRECATED", to view deprecated versions use "state:*" or any other filter. 
  * **order_by** (::String) — Optional. Specify a field to use for ordering. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::EngineVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-EngineVersion)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::EngineVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-EngineVersion)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ListEngineVersionsRequest.new
    
    # Call the list_engine_versions method.
    result = client.list_engine_versions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::FinancialServices::V1::EngineVersion.
      p item
    end

### #list_instances
    
    
    def list_instances(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::Instance>
    def list_instances(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::Instance>

Lists instances.

**Overloads**
    
    
    def list_instances(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::Instance>

Pass arguments to `list_instances` via a request object, either of type [ListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListInstancesRequest "Google::Cloud::FinancialServices::V1::ListInstancesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListInstancesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_instances(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::Instance>

Pass arguments to `list_instances` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the Instance is the location for that Instance. Every location has exactly one instance. 
  * **page_size** (::Integer) — The number of resources to be included in the response. The response contains a next_page_token, which can be used to retrieve the next page of resources. 
  * **page_token** (::String) — In case of paginated results, this is the token that was returned in the previous ListInstancesResponse. It should be copied here to retrieve the next page of resources. This will be empty for the first instance of ListInstancesRequest. 
  * **filter** (::String) — Specify a filter to narrow search results. 
  * **order_by** (::String) — Specify a field to use for ordering. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Instance)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Instance)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ListInstancesRequest.new
    
    # Call the list_instances method.
    result = client.list_instances request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::FinancialServices::V1::Instance.
      p item
    end

### #list_models
    
    
    def list_models(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::Model>
    def list_models(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::Model>

Lists models.

**Overloads**
    
    
    def list_models(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::Model>

Pass arguments to `list_models` via a request object, either of type [ListModelsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListModelsRequest "Google::Cloud::FinancialServices::V1::ListModelsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ListModelsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListModelsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_models(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::Model>

Pass arguments to `list_models` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the Model is the Instance. 
  * **page_size** (::Integer) — The number of resources to be included in the response. The response contains a next_page_token, which can be used to retrieve the next page of resources. 
  * **page_token** (::String) — In case of paginated results, this is the token that was returned in the previous ListModelsResponse. It should be copied here to retrieve the next page of resources. Empty will give the first page of ListModelsRequest, and the last page will return an empty page_token. 
  * **filter** (::String) — Specify a filter to narrow search results. 
  * **order_by** (::String) — Specify a field to use for ordering. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Model)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Model)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ListModelsRequest.new
    
    # Call the list_models method.
    result = client.list_models request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::FinancialServices::V1::Model.
      p item
    end

### #list_prediction_results
    
    
    def list_prediction_results(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::PredictionResult>
    def list_prediction_results(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::PredictionResult>

List PredictionResults.

**Overloads**
    
    
    def list_prediction_results(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::PredictionResult>

Pass arguments to `list_prediction_results` via a request object, either of type [ListPredictionResultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListPredictionResultsRequest "Google::Cloud::FinancialServices::V1::ListPredictionResultsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::ListPredictionResultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-ListPredictionResultsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_prediction_results(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::FinancialServices::V1::PredictionResult>

Pass arguments to `list_prediction_results` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the PredictionResult is the Instance. 
  * **page_size** (::Integer) — The number of resources to be included in the response. The response contains a next_page_token, which can be used to retrieve the next page of resources. 
  * **page_token** (::String) — In case of paginated results, this is the token that was returned in the previous ListPredictionResultsResponse. It should be copied here to retrieve the next page of resources. Empty will give the first page of ListPredictionResultsRequest, and the last page will return an empty page_token. 
  * **filter** (::String) — Specify a filter to narrow search results. 
  * **order_by** (::String) — Specify a field to use for ordering. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::PredictionResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-PredictionResult)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::FinancialServices::V1::PredictionResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-PredictionResult)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::ListPredictionResultsRequest.new
    
    # Call the list_prediction_results method.
    result = client.list_prediction_results request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::FinancialServices::V1::PredictionResult.
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
    
    
    def operations_client() -> ::Google::Cloud::FinancialServices::V1::AML::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::FinancialServices::V1::AML::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Rest-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_backtest_result
    
    
    def update_backtest_result(request, options = nil) -> ::Gapic::Operation
    def update_backtest_result(update_mask: nil, backtest_result: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single BacktestResult.

**Overloads**
    
    
    def update_backtest_result(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_backtest_result` via a request object, either of type [UpdateBacktestResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-UpdateBacktestResultRequest "Google::Cloud::FinancialServices::V1::UpdateBacktestResultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::UpdateBacktestResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-UpdateBacktestResultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_backtest_result(update_mask: nil, backtest_result: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_backtest_result` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the BacktestResult resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **backtest_result** ([::Google::Cloud::FinancialServices::V1::BacktestResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BacktestResult), ::Hash) — Required. The new value of the BacktestResult fields that will be updated according to the update_mask. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::UpdateBacktestResultRequest.new
    
    # Call the update_backtest_result method.
    result = client.update_backtest_result request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_dataset
    
    
    def update_dataset(request, options = nil) -> ::Gapic::Operation
    def update_dataset(update_mask: nil, dataset: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single Dataset.

**Overloads**
    
    
    def update_dataset(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_dataset` via a request object, either of type [UpdateDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-UpdateDatasetRequest "Google::Cloud::FinancialServices::V1::UpdateDatasetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::UpdateDatasetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-UpdateDatasetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_dataset(update_mask: nil, dataset: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_dataset` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the Dataset resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **dataset** ([::Google::Cloud::FinancialServices::V1::Dataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Dataset), ::Hash) — Required. The new value of the dataset fields that will be updated according to the update_mask. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::UpdateDatasetRequest.new
    
    # Call the update_dataset method.
    result = client.update_dataset request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_engine_config
    
    
    def update_engine_config(request, options = nil) -> ::Gapic::Operation
    def update_engine_config(update_mask: nil, engine_config: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single EngineConfig.

**Overloads**
    
    
    def update_engine_config(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_engine_config` via a request object, either of type [UpdateEngineConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-UpdateEngineConfigRequest "Google::Cloud::FinancialServices::V1::UpdateEngineConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::UpdateEngineConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-UpdateEngineConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_engine_config(update_mask: nil, engine_config: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_engine_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the EngineConfig resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **engine_config** ([::Google::Cloud::FinancialServices::V1::EngineConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-EngineConfig), ::Hash) — Required. The new value of the EngineConfig fields that will be updated according to the update_mask. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::UpdateEngineConfigRequest.new
    
    # Call the update_engine_config method.
    result = client.update_engine_config request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_instance
    
    
    def update_instance(request, options = nil) -> ::Gapic::Operation
    def update_instance(update_mask: nil, instance: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single Instance.

**Overloads**
    
    
    def update_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_instance` via a request object, either of type [UpdateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-UpdateInstanceRequest "Google::Cloud::FinancialServices::V1::UpdateInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::UpdateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-UpdateInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_instance(update_mask: nil, instance: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the Instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **instance** ([::Google::Cloud::FinancialServices::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Instance), ::Hash) — Required. The new value of the instance fields that will be updated according to the update_mask 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::UpdateInstanceRequest.new
    
    # Call the update_instance method.
    result = client.update_instance request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_model
    
    
    def update_model(request, options = nil) -> ::Gapic::Operation
    def update_model(update_mask: nil, model: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single Model.

**Overloads**
    
    
    def update_model(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_model` via a request object, either of type [UpdateModelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-UpdateModelRequest "Google::Cloud::FinancialServices::V1::UpdateModelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::UpdateModelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-UpdateModelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_model(update_mask: nil, model: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_model` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the Model resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **model** ([::Google::Cloud::FinancialServices::V1::Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Model), ::Hash) — Required. The new value of the Model fields that will be updated according to the update_mask. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::UpdateModelRequest.new
    
    # Call the update_model method.
    result = client.update_model request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_prediction_result
    
    
    def update_prediction_result(request, options = nil) -> ::Gapic::Operation
    def update_prediction_result(update_mask: nil, prediction_result: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single PredictionResult.

**Overloads**
    
    
    def update_prediction_result(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_prediction_result` via a request object, either of type [UpdatePredictionResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-UpdatePredictionResultRequest "Google::Cloud::FinancialServices::V1::UpdatePredictionResultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::FinancialServices::V1::UpdatePredictionResultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-UpdatePredictionResultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_prediction_result(update_mask: nil, prediction_result: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_prediction_result` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the fields to be overwritten in the PredictionResult resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **prediction_result** ([::Google::Cloud::FinancialServices::V1::PredictionResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-PredictionResult), ::Hash) — Required. The new value of the PredictionResult fields that will be updated according to the update_mask. 
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
    
    
    require "google/cloud/financial_services/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::FinancialServices::V1::AML::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::FinancialServices::V1::UpdatePredictionResultRequest.new
    
    # Call the update_prediction_result method.
    result = client.update_prediction_result request
    
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

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
