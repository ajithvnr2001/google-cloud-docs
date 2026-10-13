---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyViews-Rest-Client/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ImageFamilyViews::Rest::Client (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:39.649774+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ImageFamilyViews::Rest::Client (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyViews-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ImageFamilyViews::Rest::Client (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::ImageFamilyViews::Rest::Client.

REST client for the ImageFamilyViews service.

The ImageFamilyViews API.

This client uses ImageFamilyViews version 2026-09-01.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ImageFamilyViews Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyViews-Rest-Client-Configuration "Google::Cloud::Compute::V1::ImageFamilyViews::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyViews-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyViews-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ImageFamilyViews clients
    ::Google::Cloud::Compute::V1::ImageFamilyViews::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ImageFamilyViews Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyViews-Rest-Client#Google__Cloud__Compute__V1__ImageFamilyViews__Rest__Client_configure_class_ "Google::Cloud::Compute::V1::ImageFamilyViews::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyViews-Rest-Client-Configuration "Google::Cloud::Compute::V1::ImageFamilyViews::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyViews-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyViews-Rest-Client-Configuration)) 



### #get
    
    
    def get(request, options = nil) -> ::Google::Cloud::Compute::V1::ImageFamilyView
    def get(family: nil, project: nil, zone: nil) -> ::Google::Cloud::Compute::V1::ImageFamilyView

Returns the latest image that is part of an image family, is not deprecated and is rolled out in the specified zone.

**Overloads**
    
    
    def get(request, options = nil) -> ::Google::Cloud::Compute::V1::ImageFamilyView

Pass arguments to `get` via a request object, either of type [GetImageFamilyViewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetImageFamilyViewRequest "Google::Cloud::Compute::V1::GetImageFamilyViewRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::GetImageFamilyViewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetImageFamilyViewRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get(family: nil, project: nil, zone: nil) -> ::Google::Cloud::Compute::V1::ImageFamilyView

Pass arguments to `get` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **family** (::String) — Name of the image family to search for. 
  * **project** (::String) — Project ID for this request. 
  * **zone** (::String) — The name of the zone for this request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::ImageFamilyView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyView)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::ImageFamilyView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyView)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::ImageFamilyViews::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::GetImageFamilyViewRequest.new
    
    # Call the get method.
    result = client.get request
    
    # The returned object is of type Google::Cloud::Compute::V1::ImageFamilyView.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ImageFamilyViews REST client object.

**Yields**

  * (config) — Configure the ImageFamilyViews client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyViews-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyViews-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Compute::V1::ImageFamilyViews::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Compute::V1::ImageFamilyViews::Rest::Client.new do |config|
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
