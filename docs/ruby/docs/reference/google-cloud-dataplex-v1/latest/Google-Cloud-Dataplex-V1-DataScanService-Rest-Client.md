---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Rest-Client/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::DataScanService::Rest::Client (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:03.115859+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::DataScanService::Rest::Client (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::DataScanService::Rest::Client (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.

REST client for the DataScanService service.

DataScanService manages DataScan resources which can be configured to run various types of data scanning workload and generate enriched metadata (e.g. Data Profile, Data Quality) for the data source.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dataplex::V1::DataScanService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the DataScanService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Rest-Client-Configuration "Google::Cloud::Dataplex::V1::DataScanService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all DataScanService clients
    ::Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #cancel_data_scan_job
    
    
    def cancel_data_scan_job(request, options = nil) -> ::Google::Cloud::Dataplex::V1::CancelDataScanJobResponse
    def cancel_data_scan_job(name: nil) -> ::Google::Cloud::Dataplex::V1::CancelDataScanJobResponse

Cancels a running/pending DataScan job.

**Overloads**
    
    
    def cancel_data_scan_job(request, options = nil) -> ::Google::Cloud::Dataplex::V1::CancelDataScanJobResponse

Pass arguments to `cancel_data_scan_job` via a request object, either of type [CancelDataScanJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CancelDataScanJobRequest "Google::Cloud::Dataplex::V1::CancelDataScanJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::CancelDataScanJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CancelDataScanJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def cancel_data_scan_job(name: nil) -> ::Google::Cloud::Dataplex::V1::CancelDataScanJobResponse

Pass arguments to `cancel_data_scan_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the DataScanJob: `projects/{project_id_or_number}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project_id_or_number` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::CancelDataScanJobResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CancelDataScanJobResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::CancelDataScanJobResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CancelDataScanJobResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::CancelDataScanJobRequest.new
    
    # Call the cancel_data_scan_job method.
    result = client.cancel_data_scan_job request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::CancelDataScanJobResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the DataScanService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Rest-Client#Google__Cloud__Dataplex__V1__DataScanService__Rest__Client_configure_class_ "Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Rest-Client-Configuration "Google::Cloud::Dataplex::V1::DataScanService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Rest-Client-Configuration)) 



### #create_data_scan
    
    
    def create_data_scan(request, options = nil) -> ::Gapic::Operation
    def create_data_scan(parent: nil, data_scan: nil, data_scan_id: nil, validate_only: nil) -> ::Gapic::Operation

Creates a DataScan resource.

**Overloads**
    
    
    def create_data_scan(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_data_scan` via a request object, either of type [CreateDataScanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateDataScanRequest "Google::Cloud::Dataplex::V1::CreateDataScanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::CreateDataScanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateDataScanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_data_scan(parent: nil, data_scan: nil, data_scan_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_data_scan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. 
  * **data_scan** ([::Google::Cloud::Dataplex::V1::DataScan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScan), ::Hash) — Required. DataScan resource. 
  * **data_scan_id** (::String) — 

Optional. DataScan identifier. If not provided, a unique ID will be generated with the prefix "data-scan-".

    * Must contain only lowercase letters, numbers and hyphens.
    * Must start with a letter.
    * Must end with a number or a letter.
    * Must be between 1-63 characters.
    * Must be unique within the customer project / location.
  * **validate_only** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is `false`. 



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
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::CreateDataScanRequest.new
    
    # Call the create_data_scan method.
    result = client.create_data_scan request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_data_scan
    
    
    def delete_data_scan(request, options = nil) -> ::Gapic::Operation
    def delete_data_scan(name: nil, force: nil) -> ::Gapic::Operation

Deletes a DataScan resource.

**Overloads**
    
    
    def delete_data_scan(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_data_scan` via a request object, either of type [Google::Cloud::Dataplex::V1::DeleteDataScanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteDataScanRequest "Google::Cloud::Dataplex::V1::DeleteDataScanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::DeleteDataScanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DeleteDataScanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_data_scan(name: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_data_scan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. 
  * **force** (::Boolean) — Optional. If set to true, any child resources of this data scan will also be deleted. (Otherwise, the request will only work if the data scan has no child resources.) 



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
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::DeleteDataScanRequest.new
    
    # Call the delete_data_scan method.
    result = client.delete_data_scan request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #generate_data_quality_rules
    
    
    def generate_data_quality_rules(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GenerateDataQualityRulesResponse
    def generate_data_quality_rules(name: nil) -> ::Google::Cloud::Dataplex::V1::GenerateDataQualityRulesResponse

Generates recommended data quality rules based on the results of a data profiling scan.

Use the recommendations to build rules for a data quality scan.

**Overloads**
    
    
    def generate_data_quality_rules(request, options = nil) -> ::Google::Cloud::Dataplex::V1::GenerateDataQualityRulesResponse

Pass arguments to `generate_data_quality_rules` via a request object, either of type [GenerateDataQualityRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GenerateDataQualityRulesRequest "Google::Cloud::Dataplex::V1::GenerateDataQualityRulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::GenerateDataQualityRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GenerateDataQualityRulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def generate_data_quality_rules(name: nil) -> ::Google::Cloud::Dataplex::V1::GenerateDataQualityRulesResponse

Pass arguments to `generate_data_quality_rules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. The name must be one of the following:

    * The name of a data scan with at least one successful, completed data profiling job
    * The name of a successful, completed data profiling job (a data scan job where the job type is data profiling)



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::GenerateDataQualityRulesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GenerateDataQualityRulesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::GenerateDataQualityRulesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GenerateDataQualityRulesResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::GenerateDataQualityRulesRequest.new
    
    # Call the generate_data_quality_rules method.
    result = client.generate_data_quality_rules request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::GenerateDataQualityRulesResponse.
    p result

### #get_data_scan
    
    
    def get_data_scan(request, options = nil) -> ::Google::Cloud::Dataplex::V1::DataScan
    def get_data_scan(name: nil, view: nil) -> ::Google::Cloud::Dataplex::V1::DataScan

Gets a DataScan resource.

**Overloads**
    
    
    def get_data_scan(request, options = nil) -> ::Google::Cloud::Dataplex::V1::DataScan

Pass arguments to `get_data_scan` via a request object, either of type [GetDataScanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetDataScanRequest "Google::Cloud::Dataplex::V1::GetDataScanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::GetDataScanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetDataScanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_data_scan(name: nil, view: nil) -> ::Google::Cloud::Dataplex::V1::DataScan

Pass arguments to `get_data_scan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. 
  * **view** ([::Google::Cloud::Dataplex::V1::GetDataScanRequest::DataScanView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetDataScanRequest-DataScanView)) — Optional. Select the DataScan view to return. Defaults to `BASIC`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::DataScan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScan)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::DataScan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScan)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::GetDataScanRequest.new
    
    # Call the get_data_scan method.
    result = client.get_data_scan request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::DataScan.
    p result

### #get_data_scan_job
    
    
    def get_data_scan_job(request, options = nil) -> ::Google::Cloud::Dataplex::V1::DataScanJob
    def get_data_scan_job(name: nil, view: nil) -> ::Google::Cloud::Dataplex::V1::DataScanJob

Gets a DataScanJob resource.

**Overloads**
    
    
    def get_data_scan_job(request, options = nil) -> ::Google::Cloud::Dataplex::V1::DataScanJob

Pass arguments to `get_data_scan_job` via a request object, either of type [GetDataScanJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetDataScanJobRequest "Google::Cloud::Dataplex::V1::GetDataScanJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::GetDataScanJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetDataScanJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_data_scan_job(name: nil, view: nil) -> ::Google::Cloud::Dataplex::V1::DataScanJob

Pass arguments to `get_data_scan_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the DataScanJob: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. 
  * **view** ([::Google::Cloud::Dataplex::V1::GetDataScanJobRequest::DataScanJobView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-GetDataScanJobRequest-DataScanJobView)) — Optional. Select the DataScanJob view to return. Defaults to `BASIC`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::DataScanJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanJob)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::DataScanJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanJob)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::GetDataScanJobRequest.new
    
    # Call the get_data_scan_job method.
    result = client.get_data_scan_job request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::DataScanJob.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new DataScanService REST client object.

**Yields**

  * (config) — Configure the DataScanService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_data_scan_jobs
    
    
    def list_data_scan_jobs(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataScanJob>
    def list_data_scan_jobs(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataScanJob>

Lists DataScanJobs under the given DataScan.

**Overloads**
    
    
    def list_data_scan_jobs(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataScanJob>

Pass arguments to `list_data_scan_jobs` via a request object, either of type [ListDataScanJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListDataScanJobsRequest "Google::Cloud::Dataplex::V1::ListDataScanJobsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::ListDataScanJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListDataScanJobsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_data_scan_jobs(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataScanJob>

Pass arguments to `list_data_scan_jobs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the parent environment: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. 
  * **page_size** (::Integer) — Optional. Maximum number of DataScanJobs to return. The service may return fewer than this value. If unspecified, at most 10 DataScanJobs will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000\. 
  * **page_token** (::String) — Optional. Page token received from a previous `ListDataScanJobs` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataScanJobs` must match the call that provided the page token. 
  * **filter** (::String) — Optional. An expression for filtering the results of the ListDataScanJobs request.

If unspecified, all datascan jobs will be returned. Multiple filters can be applied (with `AND`, `OR` logical operators). Filters are case-sensitive.

Allowed fields are:

    * `start_time`
    * `end_time`

`start_time` and `end_time` expect RFC-3339 formatted strings (e.g. 2018-10-08T18:30:00-07:00).

For instance, 'start_time > 2018-10-08T00:00:00.123456789Z AND end_time < 2018-10-09T00:00:00.123456789Z' limits results to DataScanJobs between specified start and end times. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::DataScanJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanJob)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::DataScanJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanJob)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::ListDataScanJobsRequest.new
    
    # Call the list_data_scan_jobs method.
    result = client.list_data_scan_jobs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dataplex::V1::DataScanJob.
      p item
    end

### #list_data_scans
    
    
    def list_data_scans(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataScan>
    def list_data_scans(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataScan>

Lists DataScans.

**Overloads**
    
    
    def list_data_scans(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataScan>

Pass arguments to `list_data_scans` via a request object, either of type [ListDataScansRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListDataScansRequest "Google::Cloud::Dataplex::V1::ListDataScansRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::ListDataScansRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListDataScansRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_data_scans(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Dataplex::V1::DataScan>

Pass arguments to `list_data_scans` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region. 
  * **page_size** (::Integer) — Optional. Maximum number of dataScans to return. The service may return fewer than this value. If unspecified, at most 500 scans will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. Page token received from a previous `ListDataScans` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataScans` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Filter request. 
  * **order_by** (::String) — Optional. Order by fields (`name` or `create_time`) for the result. If not specified, the ordering is undefined. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::DataScan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScan)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Dataplex::V1::DataScan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScan)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::ListDataScansRequest.new
    
    # Call the list_data_scans method.
    result = client.list_data_scans request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dataplex::V1::DataScan.
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
    
    
    def operations_client() -> ::Google::Cloud::Dataplex::V1::DataScanService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Dataplex::V1::DataScanService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScanService-Rest-Operations)) 



### #run_data_scan
    
    
    def run_data_scan(request, options = nil) -> ::Google::Cloud::Dataplex::V1::RunDataScanResponse
    def run_data_scan(name: nil) -> ::Google::Cloud::Dataplex::V1::RunDataScanResponse

Runs an on-demand execution of a DataScan

**Overloads**
    
    
    def run_data_scan(request, options = nil) -> ::Google::Cloud::Dataplex::V1::RunDataScanResponse

Pass arguments to `run_data_scan` via a request object, either of type [RunDataScanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-RunDataScanRequest "Google::Cloud::Dataplex::V1::RunDataScanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::RunDataScanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-RunDataScanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def run_data_scan(name: nil) -> ::Google::Cloud::Dataplex::V1::RunDataScanResponse

Pass arguments to `run_data_scan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the DataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}`. where `project` refers to a _project_id_ or _project_number_ and `location_id` refers to a Google Cloud region.

Only **OnDemand** data scans are allowed. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataplex::V1::RunDataScanResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-RunDataScanResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::RunDataScanResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-RunDataScanResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::RunDataScanRequest.new
    
    # Call the run_data_scan method.
    result = client.run_data_scan request
    
    # The returned object is of type Google::Cloud::Dataplex::V1::RunDataScanResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_data_scan
    
    
    def update_data_scan(request, options = nil) -> ::Gapic::Operation
    def update_data_scan(data_scan: nil, update_mask: nil, validate_only: nil) -> ::Gapic::Operation

Updates a DataScan resource.

**Overloads**
    
    
    def update_data_scan(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_data_scan` via a request object, either of type [UpdateDataScanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateDataScanRequest "Google::Cloud::Dataplex::V1::UpdateDataScanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataplex::V1::UpdateDataScanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-UpdateDataScanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_data_scan(data_scan: nil, update_mask: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `update_data_scan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **data_scan** ([::Google::Cloud::Dataplex::V1::DataScan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-DataScan), ::Hash) — Required. DataScan resource to be updated.

Only fields specified in `update_mask` are updated. 

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Mask of fields to update. 
  * **validate_only** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is `false`. 



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
    
    
    require "google/cloud/dataplex/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataplex::V1::DataScanService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataplex::V1::UpdateDataScanRequest.new
    
    # Call the update_data_scan method.
    result = client.update_data_scan request
    
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
