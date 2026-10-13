---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Client/
title: Cloud Vision V1 API - Class Google::Cloud::Vision::V1::ImageAnnotator::Client (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:51.041675+00:00
---

# Cloud Vision V1 API - Class Google::Cloud::Vision::V1::ImageAnnotator::Client (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Vision V1 API - Class Google::Cloud::Vision::V1::ImageAnnotator::Client (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.1  1.1.0  1.0.1  0.15.0  0.14.0  0.13.2  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4 

Reference documentation and code samples for the Cloud Vision V1 API class Google::Cloud::Vision::V1::ImageAnnotator::Client.

Client for the ImageAnnotator service.

Service that performs Google Cloud Vision API detection tasks over client images, such as face, landmark, logo, label, and text detection. The ImageAnnotator service returns detected entities from the images.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Vision::V1::ImageAnnotator::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ImageAnnotator Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Client-Configuration "Google::Cloud::Vision::V1::ImageAnnotator::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ImageAnnotator clients
    ::Google::Cloud::Vision::V1::ImageAnnotator::Client.configure do |config|
      config.timeout = 10.0
    end

### #async_batch_annotate_files
    
    
    def async_batch_annotate_files(request, options = nil) -> ::Gapic::Operation
    def async_batch_annotate_files(requests: nil, parent: nil, labels: nil) -> ::Gapic::Operation

Run asynchronous image detection and annotation for a list of generic files, such as PDF files, which may contain multiple pages and multiple images per page. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `OperationMetadata` (metadata). `Operation.response` contains `AsyncBatchAnnotateFilesResponse` (results).

**Overloads**
    
    
    def async_batch_annotate_files(request, options = nil) -> ::Gapic::Operation

Pass arguments to `async_batch_annotate_files` via a request object, either of type [AsyncBatchAnnotateFilesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-AsyncBatchAnnotateFilesRequest "Google::Cloud::Vision::V1::AsyncBatchAnnotateFilesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Vision::V1::AsyncBatchAnnotateFilesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-AsyncBatchAnnotateFilesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def async_batch_annotate_files(requests: nil, parent: nil, labels: nil) -> ::Gapic::Operation

Pass arguments to `async_batch_annotate_files` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **requests** (::Array<[::Google::Cloud::Vision::V1::AsyncAnnotateFileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-AsyncAnnotateFileRequest), ::Hash>) — Required. Individual async file annotation requests for this batch. 
  * **parent** (::String) — Optional. Target project and location to make a call.

Format: `projects/{project-id}/locations/{location-id}`.

If no parent is specified, a region will be chosen automatically.

Supported location-ids: `us`: USA country only, `asia`: East asia areas, like Japan, Taiwan, `eu`: The European Union.

Example: `projects/project-A/locations/eu`. 

  * **labels** (::Hash{::String => ::String}) — Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. 




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
    
    
    require "google/cloud/vision/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Vision::V1::AsyncBatchAnnotateFilesRequest.new
    
    # Call the async_batch_annotate_files method.
    result = client.async_batch_annotate_files request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #async_batch_annotate_images
    
    
    def async_batch_annotate_images(request, options = nil) -> ::Gapic::Operation
    def async_batch_annotate_images(requests: nil, output_config: nil, parent: nil, labels: nil) -> ::Gapic::Operation

Run asynchronous image detection and annotation for a list of images.

Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `OperationMetadata` (metadata). `Operation.response` contains `AsyncBatchAnnotateImagesResponse` (results).

This service will write image annotation outputs to json files in customer GCS bucket, each json file containing BatchAnnotateImagesResponse proto.

**Overloads**
    
    
    def async_batch_annotate_images(request, options = nil) -> ::Gapic::Operation

Pass arguments to `async_batch_annotate_images` via a request object, either of type [AsyncBatchAnnotateImagesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-AsyncBatchAnnotateImagesRequest "Google::Cloud::Vision::V1::AsyncBatchAnnotateImagesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Vision::V1::AsyncBatchAnnotateImagesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-AsyncBatchAnnotateImagesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def async_batch_annotate_images(requests: nil, output_config: nil, parent: nil, labels: nil) -> ::Gapic::Operation

Pass arguments to `async_batch_annotate_images` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **requests** (::Array<[::Google::Cloud::Vision::V1::AnnotateImageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-AnnotateImageRequest), ::Hash>) — Required. Individual image annotation requests for this batch. 
  * **output_config** ([::Google::Cloud::Vision::V1::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-OutputConfig), ::Hash) — Required. The desired output location and metadata (e.g. format). 
  * **parent** (::String) — Optional. Target project and location to make a call.

Format: `projects/{project-id}/locations/{location-id}`.

If no parent is specified, a region will be chosen automatically.

Supported location-ids: `us`: USA country only, `asia`: East asia areas, like Japan, Taiwan, `eu`: The European Union.

Example: `projects/project-A/locations/eu`. 

  * **labels** (::Hash{::String => ::String}) — Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. 




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
    
    
    require "google/cloud/vision/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Vision::V1::AsyncBatchAnnotateImagesRequest.new
    
    # Call the async_batch_annotate_images method.
    result = client.async_batch_annotate_images request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #batch_annotate_files
    
    
    def batch_annotate_files(request, options = nil) -> ::Google::Cloud::Vision::V1::BatchAnnotateFilesResponse
    def batch_annotate_files(requests: nil, parent: nil, labels: nil) -> ::Google::Cloud::Vision::V1::BatchAnnotateFilesResponse

Service that performs image detection and annotation for a batch of files. Now only "application/pdf", "image/tiff" and "image/gif" are supported.

This service will extract at most 5 (customers can specify which 5 in AnnotateFileRequest.pages) frames (gif) or pages (pdf or tiff) from each file provided and perform detection and annotation for each image extracted.

**Overloads**
    
    
    def batch_annotate_files(request, options = nil) -> ::Google::Cloud::Vision::V1::BatchAnnotateFilesResponse

Pass arguments to `batch_annotate_files` via a request object, either of type [BatchAnnotateFilesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateFilesRequest "Google::Cloud::Vision::V1::BatchAnnotateFilesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Vision::V1::BatchAnnotateFilesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateFilesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def batch_annotate_files(requests: nil, parent: nil, labels: nil) -> ::Google::Cloud::Vision::V1::BatchAnnotateFilesResponse

Pass arguments to `batch_annotate_files` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **requests** (::Array<[::Google::Cloud::Vision::V1::AnnotateFileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-AnnotateFileRequest), ::Hash>) — Required. The list of file annotation requests. Right now we support only one AnnotateFileRequest in BatchAnnotateFilesRequest. 
  * **parent** (::String) — Optional. Target project and location to make a call.

Format: `projects/{project-id}/locations/{location-id}`.

If no parent is specified, a region will be chosen automatically.

Supported location-ids: `us`: USA country only, `asia`: East asia areas, like Japan, Taiwan, `eu`: The European Union.

Example: `projects/project-A/locations/eu`. 

  * **labels** (::Hash{::String => ::String}) — Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Vision::V1::BatchAnnotateFilesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateFilesResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Vision::V1::BatchAnnotateFilesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateFilesResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/vision/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Vision::V1::BatchAnnotateFilesRequest.new
    
    # Call the batch_annotate_files method.
    result = client.batch_annotate_files request
    
    # The returned object is of type Google::Cloud::Vision::V1::BatchAnnotateFilesResponse.
    p result

### #batch_annotate_images
    
    
    def batch_annotate_images(request, options = nil) -> ::Google::Cloud::Vision::V1::BatchAnnotateImagesResponse
    def batch_annotate_images(requests: nil, parent: nil, labels: nil) -> ::Google::Cloud::Vision::V1::BatchAnnotateImagesResponse

Run image detection and annotation for a batch of images.

**Overloads**
    
    
    def batch_annotate_images(request, options = nil) -> ::Google::Cloud::Vision::V1::BatchAnnotateImagesResponse

Pass arguments to `batch_annotate_images` via a request object, either of type [BatchAnnotateImagesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesRequest "Google::Cloud::Vision::V1::BatchAnnotateImagesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Vision::V1::BatchAnnotateImagesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def batch_annotate_images(requests: nil, parent: nil, labels: nil) -> ::Google::Cloud::Vision::V1::BatchAnnotateImagesResponse

Pass arguments to `batch_annotate_images` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **requests** (::Array<[::Google::Cloud::Vision::V1::AnnotateImageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-AnnotateImageRequest), ::Hash>) — Required. Individual image annotation requests for this batch. 
  * **parent** (::String) — Optional. Target project and location to make a call.

Format: `projects/{project-id}/locations/{location-id}`.

If no parent is specified, a region will be chosen automatically.

Supported location-ids: `us`: USA country only, `asia`: East asia areas, like Japan, Taiwan, `eu`: The European Union.

Example: `projects/project-A/locations/eu`. 

  * **labels** (::Hash{::String => ::String}) — Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/vision/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Vision::V1::BatchAnnotateImagesRequest.new
    
    # Call the batch_annotate_images method.
    result = client.batch_annotate_images request
    
    # The returned object is of type Google::Cloud::Vision::V1::BatchAnnotateImagesResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ImageAnnotator Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Client#Google__Cloud__Vision__V1__ImageAnnotator__Client_configure_class_ "Google::Cloud::Vision::V1::ImageAnnotator::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Client-Configuration "Google::Cloud::Vision::V1::ImageAnnotator::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Client-Configuration)) 



### #crop_hints_detection
    
    
    def crop_hints_detection(images: [], image: nil, max_results: 10, options: nil, async: false, mime_type: nil, batch_size: 10, destination: nil, image_context: nil, &block) { |result, operation| ... } -> Google::Cloud::Vision::V1::BatchAnnotateImagesResponse, Gapic::Operation

Detect features of type CROP_HINTS.

**Parameters**

  * **images** (Array<String>, Array<File>) _(defaults to: [])_ — An array containing files, file paths, io objects, image urls, or Google Cloud Storage urls. Can be used with or instead of image. 
  * **image** (File, String) _(defaults to: nil)_ — A file, file path, io object, url pointing to an image, or Google Cloud Storage url. Can be used with or instead of images. 
  * **max_results** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. 
  * **options** (Gapic::CallOptions) _(defaults to: nil)_ — Optional. Overrides the default settings for this call, e.g, timeout, retries, etc. 
  * **async** (Boolean) _(defaults to: false)_ — Optional. Defaults to `false`. If `false`, performs the request synchronously, returning a `BatchAnnotateImagesResponse`. If `true`, performs the request asynchronously, returning a `Gapic::Operation`. 
  * **mime_type** (String) _(defaults to: nil)_ — Required only if async is `true`. 
  * **batch_size** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. When async is `true`, this specifies the number of input files per output json. 
  * **destination** (String) _(defaults to: nil)_ — A Google Cloud Storage location for storing the output. Required only if async is `true`. 
  * **image_context** (Hash) _(defaults to: nil)_ — Optional. Image context and/or feature-specific parameters. 



**Yields**

  * (result, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **result** ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse), Gapic::Operation) 
  * **operation** (GRPC::ActiveCall::Operation) 



**Returns**

  * ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) — if async is `false`. 
  * (Gapic::Operation) — if async is `true`. 



**Raises**

  * (Google::Cloud::Error) — if the RPC is aborted. 



**Example**
    
    
    require "google/cloud/vision/v1"
    
    image_annotator_client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    response = image_annotator_client.crop_hints_detection image: "path/to/image.png"
    response.responses.each do |res|
      puts res
    end

### #document_text_detection
    
    
    def document_text_detection(images: [], image: nil, max_results: 10, options: nil, async: false, mime_type: nil, batch_size: 10, destination: nil, image_context: nil, &block) { |result, operation| ... } -> Google::Cloud::Vision::V1::BatchAnnotateImagesResponse, Gapic::Operation

Detect features of type DOCUMENT_TEXT_DETECTION.

**Parameters**

  * **images** (Array<String>, Array<File>) _(defaults to: [])_ — An array containing files, file paths, io objects, image urls, or Google Cloud Storage urls. Can be used with or instead of image. 
  * **image** (File, String) _(defaults to: nil)_ — A file, file path, io object, url pointing to an image, or Google Cloud Storage url. Can be used with or instead of images. 
  * **max_results** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. 
  * **options** (Gapic::CallOptions) _(defaults to: nil)_ — Optional. Overrides the default settings for this call, e.g, timeout, retries, etc. 
  * **async** (Boolean) _(defaults to: false)_ — Optional. Defaults to `false`. If `false`, performs the request synchronously, returning a `BatchAnnotateImagesResponse`. If `true`, performs the request asynchronously, returning a `Gapic::Operation`. 
  * **mime_type** (String) _(defaults to: nil)_ — Required only if async is `true`. 
  * **batch_size** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. When async is `true`, this specifies the number of input files per output json. 
  * **destination** (String) _(defaults to: nil)_ — A Google Cloud Storage location for storing the output. Required only if async is `true`. 
  * **image_context** (Hash) _(defaults to: nil)_ — Optional. Image context and/or feature-specific parameters. 



**Yields**

  * (result, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **result** ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse), Gapic::Operation) 
  * **operation** (GRPC::ActiveCall::Operation) 



**Returns**

  * ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) — if async is `false`. 
  * (Gapic::Operation) — if async is `true`. 



**Raises**

  * (Google::Cloud::Error) — if the RPC is aborted. 



**Example**
    
    
    require "google/cloud/vision/v1"
    
    image_annotator_client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    response = image_annotator_client.document_text_detection image: "path/to/image.png"
    response.responses.each do |res|
      puts res
    end

### #face_detection
    
    
    def face_detection(images: [], image: nil, max_results: 10, options: nil, async: false, mime_type: nil, batch_size: 10, destination: nil, image_context: nil, &block) { |result, operation| ... } -> Google::Cloud::Vision::V1::BatchAnnotateImagesResponse, Gapic::Operation

Detect features of type FACE_DETECTION.

**Parameters**

  * **images** (Array<String>, Array<File>) _(defaults to: [])_ — An array containing files, file paths, io objects, image urls, or Google Cloud Storage urls. Can be used with or instead of image. 
  * **image** (File, String) _(defaults to: nil)_ — A file, file path, io object, url pointing to an image, or Google Cloud Storage url. Can be used with or instead of images. 
  * **max_results** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. 
  * **options** (Gapic::CallOptions) _(defaults to: nil)_ — Optional. Overrides the default settings for this call, e.g, timeout, retries, etc. 
  * **async** (Boolean) _(defaults to: false)_ — Optional. Defaults to `false`. If `false`, performs the request synchronously, returning a `BatchAnnotateImagesResponse`. If `true`, performs the request asynchronously, returning a `Gapic::Operation`. 
  * **mime_type** (String) _(defaults to: nil)_ — Required only if async is `true`. 
  * **batch_size** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. When async is `true`, this specifies the number of input files per output json. 
  * **destination** (String) _(defaults to: nil)_ — A Google Cloud Storage location for storing the output. Required only if async is `true`. 
  * **image_context** (Hash) _(defaults to: nil)_ — Optional. Image context and/or feature-specific parameters. 



**Yields**

  * (result, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **result** ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse), Gapic::Operation) 
  * **operation** (GRPC::ActiveCall::Operation) 



**Returns**

  * ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) — if async is `false`. 
  * (Gapic::Operation) — if async is `true`. 



**Raises**

  * (Google::Cloud::Error) — if the RPC is aborted. 



**Example**
    
    
    require "google/cloud/vision/v1"
    
    image_annotator_client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    response = image_annotator_client.face_detection image: "path/to/image.png"
    response.responses.each do |res|
      puts res
    end

### #image_properties_detection
    
    
    def image_properties_detection(images: [], image: nil, max_results: 10, options: nil, async: false, mime_type: nil, batch_size: 10, destination: nil, image_context: nil, &block) { |result, operation| ... } -> Google::Cloud::Vision::V1::BatchAnnotateImagesResponse, Gapic::Operation

Detect features of type IMAGE_PROPERTIES.

**Parameters**

  * **images** (Array<String>, Array<File>) _(defaults to: [])_ — An array containing files, file paths, io objects, image urls, or Google Cloud Storage urls. Can be used with or instead of image. 
  * **image** (File, String) _(defaults to: nil)_ — A file, file path, io object, url pointing to an image, or Google Cloud Storage url. Can be used with or instead of images. 
  * **max_results** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. 
  * **options** (Gapic::CallOptions) _(defaults to: nil)_ — Optional. Overrides the default settings for this call, e.g, timeout, retries, etc. 
  * **async** (Boolean) _(defaults to: false)_ — Optional. Defaults to `false`. If `false`, performs the request synchronously, returning a `BatchAnnotateImagesResponse`. If `true`, performs the request asynchronously, returning a `Gapic::Operation`. 
  * **mime_type** (String) _(defaults to: nil)_ — Required only if async is `true`. 
  * **batch_size** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. When async is `true`, this specifies the number of input files per output json. 
  * **destination** (String) _(defaults to: nil)_ — A Google Cloud Storage location for storing the output. Required only if async is `true`. 
  * **image_context** (Hash) _(defaults to: nil)_ — Optional. Image context and/or feature-specific parameters. 



**Yields**

  * (result, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **result** ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse), Gapic::Operation) 
  * **operation** (GRPC::ActiveCall::Operation) 



**Returns**

  * ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) — if async is `false`. 
  * (Gapic::Operation) — if async is `true`. 



**Raises**

  * (Google::Cloud::Error) — if the RPC is aborted. 



**Example**
    
    
    require "google/cloud/vision/v1"
    
    image_annotator_client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    response = image_annotator_client.image_properties_detection image: "path/to/image.png"
    response.responses.each do |res|
      puts res
    end

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ImageAnnotator client object.

**Yields**

  * (config) — Configure the ImageAnnotator client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Vision::V1::ImageAnnotator::Client.new do |config|
      config.timeout = 10.0
    end

### #label_detection
    
    
    def label_detection(images: [], image: nil, max_results: 10, options: nil, async: false, mime_type: nil, batch_size: 10, destination: nil, image_context: nil, &block) { |result, operation| ... } -> Google::Cloud::Vision::V1::BatchAnnotateImagesResponse, Gapic::Operation

Detect features of type LABEL_DETECTION.

**Parameters**

  * **images** (Array<String>, Array<File>) _(defaults to: [])_ — An array containing files, file paths, io objects, image urls, or Google Cloud Storage urls. Can be used with or instead of image. 
  * **image** (File, String) _(defaults to: nil)_ — A file, file path, io object, url pointing to an image, or Google Cloud Storage url. Can be used with or instead of images. 
  * **max_results** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. 
  * **options** (Gapic::CallOptions) _(defaults to: nil)_ — Optional. Overrides the default settings for this call, e.g, timeout, retries, etc. 
  * **async** (Boolean) _(defaults to: false)_ — Optional. Defaults to `false`. If `false`, performs the request synchronously, returning a `BatchAnnotateImagesResponse`. If `true`, performs the request asynchronously, returning a `Gapic::Operation`. 
  * **mime_type** (String) _(defaults to: nil)_ — Required only if async is `true`. 
  * **batch_size** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. When async is `true`, this specifies the number of input files per output json. 
  * **destination** (String) _(defaults to: nil)_ — A Google Cloud Storage location for storing the output. Required only if async is `true`. 
  * **image_context** (Hash) _(defaults to: nil)_ — Optional. Image context and/or feature-specific parameters. 



**Yields**

  * (result, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **result** ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse), Gapic::Operation) 
  * **operation** (GRPC::ActiveCall::Operation) 



**Returns**

  * ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) — if async is `false`. 
  * (Gapic::Operation) — if async is `true`. 



**Raises**

  * (Google::Cloud::Error) — if the RPC is aborted. 



**Example**
    
    
    require "google/cloud/vision/v1"
    
    image_annotator_client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    response = image_annotator_client.label_detection image: "path/to/image.png"
    response.responses.each do |res|
      puts res
    end

### #landmark_detection
    
    
    def landmark_detection(images: [], image: nil, max_results: 10, options: nil, async: false, mime_type: nil, batch_size: 10, destination: nil, image_context: nil, &block) { |result, operation| ... } -> Google::Cloud::Vision::V1::BatchAnnotateImagesResponse, Gapic::Operation

Detect features of type LANDMARK_DETECTION.

**Parameters**

  * **images** (Array<String>, Array<File>) _(defaults to: [])_ — An array containing files, file paths, io objects, image urls, or Google Cloud Storage urls. Can be used with or instead of image. 
  * **image** (File, String) _(defaults to: nil)_ — A file, file path, io object, url pointing to an image, or Google Cloud Storage url. Can be used with or instead of images. 
  * **max_results** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. 
  * **options** (Gapic::CallOptions) _(defaults to: nil)_ — Optional. Overrides the default settings for this call, e.g, timeout, retries, etc. 
  * **async** (Boolean) _(defaults to: false)_ — Optional. Defaults to `false`. If `false`, performs the request synchronously, returning a `BatchAnnotateImagesResponse`. If `true`, performs the request asynchronously, returning a `Gapic::Operation`. 
  * **mime_type** (String) _(defaults to: nil)_ — Required only if async is `true`. 
  * **batch_size** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. When async is `true`, this specifies the number of input files per output json. 
  * **destination** (String) _(defaults to: nil)_ — A Google Cloud Storage location for storing the output. Required only if async is `true`. 
  * **image_context** (Hash) _(defaults to: nil)_ — Optional. Image context and/or feature-specific parameters. 



**Yields**

  * (result, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **result** ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse), Gapic::Operation) 
  * **operation** (GRPC::ActiveCall::Operation) 



**Returns**

  * ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) — if async is `false`. 
  * (Gapic::Operation) — if async is `true`. 



**Raises**

  * (Google::Cloud::Error) — if the RPC is aborted. 



**Example**
    
    
    require "google/cloud/vision/v1"
    
    image_annotator_client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    response = image_annotator_client.landmark_detection image: "path/to/image.png"
    response.responses.each do |res|
      puts res
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #logo_detection
    
    
    def logo_detection(images: [], image: nil, max_results: 10, options: nil, async: false, mime_type: nil, batch_size: 10, destination: nil, image_context: nil, &block) { |result, operation| ... } -> Google::Cloud::Vision::V1::BatchAnnotateImagesResponse, Gapic::Operation

Detect features of type LOGO_DETECTION.

**Parameters**

  * **images** (Array<String>, Array<File>) _(defaults to: [])_ — An array containing files, file paths, io objects, image urls, or Google Cloud Storage urls. Can be used with or instead of image. 
  * **image** (File, String) _(defaults to: nil)_ — A file, file path, io object, url pointing to an image, or Google Cloud Storage url. Can be used with or instead of images. 
  * **max_results** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. 
  * **options** (Gapic::CallOptions) _(defaults to: nil)_ — Optional. Overrides the default settings for this call, e.g, timeout, retries, etc. 
  * **async** (Boolean) _(defaults to: false)_ — Optional. Defaults to `false`. If `false`, performs the request synchronously, returning a `BatchAnnotateImagesResponse`. If `true`, performs the request asynchronously, returning a `Gapic::Operation`. 
  * **mime_type** (String) _(defaults to: nil)_ — Required only if async is `true`. 
  * **batch_size** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. When async is `true`, this specifies the number of input files per output json. 
  * **destination** (String) _(defaults to: nil)_ — A Google Cloud Storage location for storing the output. Required only if async is `true`. 
  * **image_context** (Hash) _(defaults to: nil)_ — Optional. Image context and/or feature-specific parameters. 



**Yields**

  * (result, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **result** ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse), Gapic::Operation) 
  * **operation** (GRPC::ActiveCall::Operation) 



**Returns**

  * ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) — if async is `false`. 
  * (Gapic::Operation) — if async is `true`. 



**Raises**

  * (Google::Cloud::Error) — if the RPC is aborted. 



**Example**
    
    
    require "google/cloud/vision/v1"
    
    image_annotator_client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    response = image_annotator_client.logo_detection image: "path/to/image.png"
    response.responses.each do |res|
      puts res
    end

### #object_localization_detection
    
    
    def object_localization_detection(images: [], image: nil, max_results: 10, options: nil, async: false, mime_type: nil, batch_size: 10, destination: nil, image_context: nil, &block) { |result, operation| ... } -> Google::Cloud::Vision::V1::BatchAnnotateImagesResponse, Gapic::Operation

Detect features of type OBJECT_LOCALIZATION.

**Parameters**

  * **images** (Array<String>, Array<File>) _(defaults to: [])_ — An array containing files, file paths, io objects, image urls, or Google Cloud Storage urls. Can be used with or instead of image. 
  * **image** (File, String) _(defaults to: nil)_ — A file, file path, io object, url pointing to an image, or Google Cloud Storage url. Can be used with or instead of images. 
  * **max_results** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. 
  * **options** (Gapic::CallOptions) _(defaults to: nil)_ — Optional. Overrides the default settings for this call, e.g, timeout, retries, etc. 
  * **async** (Boolean) _(defaults to: false)_ — Optional. Defaults to `false`. If `false`, performs the request synchronously, returning a `BatchAnnotateImagesResponse`. If `true`, performs the request asynchronously, returning a `Gapic::Operation`. 
  * **mime_type** (String) _(defaults to: nil)_ — Required only if async is `true`. 
  * **batch_size** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. When async is `true`, this specifies the number of input files per output json. 
  * **destination** (String) _(defaults to: nil)_ — A Google Cloud Storage location for storing the output. Required only if async is `true`. 
  * **image_context** (Hash) _(defaults to: nil)_ — Optional. Image context and/or feature-specific parameters. 



**Yields**

  * (result, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **result** ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse), Gapic::Operation) 
  * **operation** (GRPC::ActiveCall::Operation) 



**Returns**

  * ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) — if async is `false`. 
  * (Gapic::Operation) — if async is `true`. 



**Raises**

  * (Google::Cloud::Error) — if the RPC is aborted. 



**Example**
    
    
    require "google/cloud/vision/v1"
    
    image_annotator_client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    response = image_annotator_client.object_localization_detection image: "path/to/image.png"
    response.responses.each do |res|
      puts res
    end

### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::Vision::V1::ImageAnnotator::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Vision::V1::ImageAnnotator::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotator-Operations)) 



### #product_search_detection
    
    
    def product_search_detection(images: [], image: nil, max_results: 10, options: nil, async: false, mime_type: nil, batch_size: 10, destination: nil, image_context: nil, &block) { |result, operation| ... } -> Google::Cloud::Vision::V1::BatchAnnotateImagesResponse, Gapic::Operation

Detect features of type PRODUCT_SEARCH.

**Parameters**

  * **images** (Array<String>, Array<File>) _(defaults to: [])_ — An array containing files, file paths, io objects, image urls, or Google Cloud Storage urls. Can be used with or instead of image. 
  * **image** (File, String) _(defaults to: nil)_ — A file, file path, io object, url pointing to an image, or Google Cloud Storage url. Can be used with or instead of images. 
  * **max_results** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. 
  * **options** (Gapic::CallOptions) _(defaults to: nil)_ — Optional. Overrides the default settings for this call, e.g, timeout, retries, etc. 
  * **async** (Boolean) _(defaults to: false)_ — Optional. Defaults to `false`. If `false`, performs the request synchronously, returning a `BatchAnnotateImagesResponse`. If `true`, performs the request asynchronously, returning a `Gapic::Operation`. 
  * **mime_type** (String) _(defaults to: nil)_ — Required only if async is `true`. 
  * **batch_size** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. When async is `true`, this specifies the number of input files per output json. 
  * **destination** (String) _(defaults to: nil)_ — A Google Cloud Storage location for storing the output. Required only if async is `true`. 
  * **image_context** (Hash) _(defaults to: nil)_ — Optional. Image context and/or feature-specific parameters. 



**Yields**

  * (result, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **result** ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse), Gapic::Operation) 
  * **operation** (GRPC::ActiveCall::Operation) 



**Returns**

  * ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) — if async is `false`. 
  * (Gapic::Operation) — if async is `true`. 



**Raises**

  * (Google::Cloud::Error) — if the RPC is aborted. 



**Example**
    
    
    require "google/cloud/vision/v1"
    
    image_annotator_client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    response = image_annotator_client.product_search_detection image: "path/to/image.png"
    response.responses.each do |res|
      puts res
    end

### #safe_search_detection
    
    
    def safe_search_detection(images: [], image: nil, max_results: 10, options: nil, async: false, mime_type: nil, batch_size: 10, destination: nil, image_context: nil, &block) { |result, operation| ... } -> Google::Cloud::Vision::V1::BatchAnnotateImagesResponse, Gapic::Operation

Detect features of type SAFE_SEARCH_DETECTION.

**Parameters**

  * **images** (Array<String>, Array<File>) _(defaults to: [])_ — An array containing files, file paths, io objects, image urls, or Google Cloud Storage urls. Can be used with or instead of image. 
  * **image** (File, String) _(defaults to: nil)_ — A file, file path, io object, url pointing to an image, or Google Cloud Storage url. Can be used with or instead of images. 
  * **max_results** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. 
  * **options** (Gapic::CallOptions) _(defaults to: nil)_ — Optional. Overrides the default settings for this call, e.g, timeout, retries, etc. 
  * **async** (Boolean) _(defaults to: false)_ — Optional. Defaults to `false`. If `false`, performs the request synchronously, returning a `BatchAnnotateImagesResponse`. If `true`, performs the request asynchronously, returning a `Gapic::Operation`. 
  * **mime_type** (String) _(defaults to: nil)_ — Required only if async is `true`. 
  * **batch_size** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. When async is `true`, this specifies the number of input files per output json. 
  * **destination** (String) _(defaults to: nil)_ — A Google Cloud Storage location for storing the output. Required only if async is `true`. 
  * **image_context** (Hash) _(defaults to: nil)_ — Optional. Image context and/or feature-specific parameters. 



**Yields**

  * (result, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **result** ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse), Gapic::Operation) 
  * **operation** (GRPC::ActiveCall::Operation) 



**Returns**

  * ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) — if async is `false`. 
  * (Gapic::Operation) — if async is `true`. 



**Raises**

  * (Google::Cloud::Error) — if the RPC is aborted. 



**Example**
    
    
    require "google/cloud/vision/v1"
    
    image_annotator_client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    response = image_annotator_client.safe_search_detection image: "path/to/image.png"
    response.responses.each do |res|
      puts res
    end

### #text_detection
    
    
    def text_detection(images: [], image: nil, max_results: 10, options: nil, async: false, mime_type: nil, batch_size: 10, destination: nil, image_context: nil, &block) { |result, operation| ... } -> Google::Cloud::Vision::V1::BatchAnnotateImagesResponse, Gapic::Operation

Detect features of type TEXT_DETECTION.

**Parameters**

  * **images** (Array<String>, Array<File>) _(defaults to: [])_ — An array containing files, file paths, io objects, image urls, or Google Cloud Storage urls. Can be used with or instead of image. 
  * **image** (File, String) _(defaults to: nil)_ — A file, file path, io object, url pointing to an image, or Google Cloud Storage url. Can be used with or instead of images. 
  * **max_results** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. 
  * **options** (Gapic::CallOptions) _(defaults to: nil)_ — Optional. Overrides the default settings for this call, e.g, timeout, retries, etc. 
  * **async** (Boolean) _(defaults to: false)_ — Optional. Defaults to `false`. If `false`, performs the request synchronously, returning a `BatchAnnotateImagesResponse`. If `true`, performs the request asynchronously, returning a `Gapic::Operation`. 
  * **mime_type** (String) _(defaults to: nil)_ — Required only if async is `true`. 
  * **batch_size** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. When async is `true`, this specifies the number of input files per output json. 
  * **destination** (String) _(defaults to: nil)_ — A Google Cloud Storage location for storing the output. Required only if async is `true`. 
  * **image_context** (Hash) _(defaults to: nil)_ — Optional. Image context and/or feature-specific parameters. 



**Yields**

  * (result, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **result** ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse), Gapic::Operation) 
  * **operation** (GRPC::ActiveCall::Operation) 



**Returns**

  * ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) — if async is `false`. 
  * (Gapic::Operation) — if async is `true`. 



**Raises**

  * (Google::Cloud::Error) — if the RPC is aborted. 



**Example**
    
    
    require "google/cloud/vision/v1"
    
    image_annotator_client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    response = image_annotator_client.text_detection image: "path/to/image.png"
    response.responses.each do |res|
      puts res
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #web_detection
    
    
    def web_detection(images: [], image: nil, max_results: 10, options: nil, async: false, mime_type: nil, batch_size: 10, destination: nil, image_context: nil, &block) { |result, operation| ... } -> Google::Cloud::Vision::V1::BatchAnnotateImagesResponse, Gapic::Operation

Detect features of type WEB_DETECTION.

**Parameters**

  * **images** (Array<String>, Array<File>) _(defaults to: [])_ — An array containing files, file paths, io objects, image urls, or Google Cloud Storage urls. Can be used with or instead of image. 
  * **image** (File, String) _(defaults to: nil)_ — A file, file path, io object, url pointing to an image, or Google Cloud Storage url. Can be used with or instead of images. 
  * **max_results** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. 
  * **options** (Gapic::CallOptions) _(defaults to: nil)_ — Optional. Overrides the default settings for this call, e.g, timeout, retries, etc. 
  * **async** (Boolean) _(defaults to: false)_ — Optional. Defaults to `false`. If `false`, performs the request synchronously, returning a `BatchAnnotateImagesResponse`. If `true`, performs the request asynchronously, returning a `Gapic::Operation`. 
  * **mime_type** (String) _(defaults to: nil)_ — Required only if async is `true`. 
  * **batch_size** (Integer) _(defaults to: 10)_ — Optional. Defaults to 10. When async is `true`, this specifies the number of input files per output json. 
  * **destination** (String) _(defaults to: nil)_ — A Google Cloud Storage location for storing the output. Required only if async is `true`. 
  * **image_context** (Hash) _(defaults to: nil)_ — Optional. Image context and/or feature-specific parameters. 



**Yields**

  * (result, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **result** ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse), Gapic::Operation) 
  * **operation** (GRPC::ActiveCall::Operation) 



**Returns**

  * ([Google::Cloud::Vision::V1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-BatchAnnotateImagesResponse)) — if async is `false`. 
  * (Gapic::Operation) — if async is `true`. 



**Raises**

  * (Google::Cloud::Error) — if the RPC is aborted. 



**Example**
    
    
    require "google/cloud/vision/v1"
    
    image_annotator_client = Google::Cloud::Vision::V1::ImageAnnotator::Client.new
    
    response = image_annotator_client.web_detection image: "path/to/image.png"
    response.responses.each do |res|
      puts res
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
