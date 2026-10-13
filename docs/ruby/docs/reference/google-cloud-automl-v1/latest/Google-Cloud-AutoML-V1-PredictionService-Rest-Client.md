---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Client/
title: Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::PredictionService::Rest::Client (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:11.388293+00:00
---

# Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::PredictionService::Rest::Client (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::PredictionService::Rest::Client (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.8 

Reference documentation and code samples for the Cloud AutoML V1 API class Google::Cloud::AutoML::V1::PredictionService::Rest::Client.

REST client for the PredictionService service.

AutoML Prediction API.

On any input that is documented to expect a string parameter in snake_case or dash-case, either of those cases is accepted.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::AutoML::V1::PredictionService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the PredictionService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Client-Configuration "Google::Cloud::AutoML::V1::PredictionService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all PredictionService clients
    ::Google::Cloud::AutoML::V1::PredictionService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #batch_predict
    
    
    def batch_predict(request, options = nil) -> ::Gapic::Operation
    def batch_predict(name: nil, input_config: nil, output_config: nil, params: nil) -> ::Gapic::Operation

Perform a batch prediction. Unlike the online [Predict](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Client#Google__Cloud__AutoML__V1__PredictionService__Rest__Client_predict_instance_ "Google::Cloud::AutoML::V1::PredictionService::Rest::Client#predict \(method\)"), batch prediction result won't be immediately available in the response. Instead, a long running operation object is returned. User can poll the operation result via GetOperation method. Once the operation is done, [BatchPredictResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BatchPredictResult "Google::Cloud::AutoML::V1::BatchPredictResult \(class\)") is returned in the [response](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_response_instance_ "Google::Longrunning::Operation#response \(method\)") field. Available for following ML scenarios:

  * AutoML Vision Classification
  * AutoML Vision Object Detection
  * AutoML Video Intelligence Classification
  * AutoML Video Intelligence Object Tracking * AutoML Natural Language Classification
  * AutoML Natural Language Entity Extraction
  * AutoML Natural Language Sentiment Analysis
  * AutoML Tables



**Overloads**
    
    
    def batch_predict(request, options = nil) -> ::Gapic::Operation

Pass arguments to `batch_predict` via a request object, either of type [BatchPredictRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BatchPredictRequest "Google::Cloud::AutoML::V1::BatchPredictRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AutoML::V1::BatchPredictRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BatchPredictRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def batch_predict(name: nil, input_config: nil, output_config: nil, params: nil) -> ::Gapic::Operation

Pass arguments to `batch_predict` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the model requested to serve the batch prediction. 
  * **input_config** ([::Google::Cloud::AutoML::V1::BatchPredictInputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BatchPredictInputConfig), ::Hash) — Required. The input configuration for batch prediction. 
  * **output_config** ([::Google::Cloud::AutoML::V1::BatchPredictOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BatchPredictOutputConfig), ::Hash) — Required. The Configuration specifying where output predictions should be written. 
  * **params** (::Hash{::String => ::String}) — Additional domain-specific parameters for the predictions, any string must be up to 25000 characters long.

AutoML Natural Language Classification

`score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for a text snippet, it will only produce results that have at least this confidence score. The default is 0.5.

AutoML Vision Classification

`score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for an image, it will only produce results that have at least this confidence score. The default is 0.5.

AutoML Vision Object Detection

`score_threshold` : (float) When Model detects objects on the image, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5.

`max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per image. The default is 100, the number of bounding boxes returned might be limited by the server. AutoML Video Intelligence Classification

`score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for a video, it will only produce results that have at least this confidence score. The default is 0.5.

`segment_classification` : (boolean) Set to true to request segment-level classification. AutoML Video Intelligence returns labels and their confidence scores for the entire segment of the video that user specified in the request configuration. The default is true.

`shot_classification` : (boolean) Set to true to request shot-level classification. AutoML Video Intelligence determines the boundaries for each camera shot in the entire segment of the video that user specified in the request configuration. AutoML Video Intelligence then returns labels and their confidence scores for each detected shot, along with the start and end time of the shot. The default is false.

WARNING: Model evaluation is not done for this classification type, the quality of it depends on training data, but there are no metrics provided to describe that quality.

`1s_interval_classification` : (boolean) Set to true to request classification for a video at one-second intervals. AutoML Video Intelligence returns labels and their confidence scores for each second of the entire segment of the video that user specified in the request configuration. The default is false.

WARNING: Model evaluation is not done for this classification type, the quality of it depends on training data, but there are no metrics provided to describe that quality.

AutoML Video Intelligence Object Tracking

`score_threshold` : (float) When Model detects objects on video frames, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5.

`max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per image. The default is 100, the number of bounding boxes returned might be limited by the server.

`min_bounding_box_size` : (float) Only bounding boxes with shortest edge at least that long as a relative value of video frame size are returned. Value in 0 to 1 range. Default is 0. 




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
    
    
    require "google/cloud/automl/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AutoML::V1::PredictionService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AutoML::V1::BatchPredictRequest.new
    
    # Call the batch_predict method.
    result = client.batch_predict request
    
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

Configure the PredictionService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Client#Google__Cloud__AutoML__V1__PredictionService__Rest__Client_configure_class_ "Google::Cloud::AutoML::V1::PredictionService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Client-Configuration "Google::Cloud::AutoML::V1::PredictionService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Client-Configuration)) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new PredictionService REST client object.

**Yields**

  * (config) — Configure the PredictionService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AutoML::V1::PredictionService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AutoML::V1::PredictionService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::AutoML::V1::PredictionService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::AutoML::V1::PredictionService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Rest-Operations)) 



### #predict
    
    
    def predict(request, options = nil) -> ::Google::Cloud::AutoML::V1::PredictResponse
    def predict(name: nil, payload: nil, params: nil) -> ::Google::Cloud::AutoML::V1::PredictResponse

Perform an online prediction. The prediction result is directly returned in the response. Available for following ML scenarios, and their expected request payloads:

AutoML Vision Classification

  * An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB.



AutoML Vision Object Detection

  * An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB.



AutoML Natural Language Classification

  * A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in .PDF, .TIF or .TIFF format with size upto 2MB.



AutoML Natural Language Entity Extraction

  * A TextSnippet up to 10,000 characters, UTF-8 NFC encoded or a document in .PDF, .TIF or .TIFF format with size upto 20MB.



AutoML Natural Language Sentiment Analysis

  * A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in .PDF, .TIF or .TIFF format with size upto 2MB.



AutoML Translation

  * A TextSnippet up to 25,000 characters, UTF-8 encoded.



AutoML Tables

  * A row with column values matching the columns of the model, up to 5MB. Not available for FORECASTING `prediction_type`.



**Overloads**
    
    
    def predict(request, options = nil) -> ::Google::Cloud::AutoML::V1::PredictResponse

Pass arguments to `predict` via a request object, either of type [Google::Cloud::AutoML::V1::PredictRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictRequest "Google::Cloud::AutoML::V1::PredictRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AutoML::V1::PredictRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def predict(name: nil, payload: nil, params: nil) -> ::Google::Cloud::AutoML::V1::PredictResponse

Pass arguments to `predict` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the model requested to serve the prediction. 
  * **payload** ([::Google::Cloud::AutoML::V1::ExamplePayload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ExamplePayload), ::Hash) — Required. Payload to perform a prediction on. The payload must match the problem type that the model was trained to solve. 
  * **params** (::Hash{::String => ::String}) — Additional domain-specific parameters, any string must be up to 25000 characters long.

AutoML Vision Classification

`score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for an image, it will only produce results that have at least this confidence score. The default is 0.5.

AutoML Vision Object Detection

`score_threshold` : (float) When Model detects objects on the image, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5.

`max_bounding_box_count` : (int64) The maximum number of bounding boxes returned. The default is 100. The number of returned bounding boxes might be limited by the server.

AutoML Tables

`feature_importance` : (boolean) Whether [feature_importance][google.cloud.automl.v1.TablesModelColumnInfo.feature_importance] is populated in the returned list of [TablesAnnotation][google.cloud.automl.v1.TablesAnnotation] objects. The default is false. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AutoML::V1::PredictResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AutoML::V1::PredictResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/automl/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AutoML::V1::PredictionService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AutoML::V1::PredictRequest.new
    
    # Call the predict method.
    result = client.predict request
    
    # The returned object is of type Google::Cloud::AutoML::V1::PredictResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
