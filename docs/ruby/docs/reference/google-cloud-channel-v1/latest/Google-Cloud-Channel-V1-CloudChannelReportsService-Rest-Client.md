---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:24.318328+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client.

REST client for the CloudChannelReportsService service.

CloudChannelReportsService lets Google Cloud resellers and distributors retrieve and combine a variety of data in Cloud Channel for multiple products (Google Cloud, Google Voice, and Google Workspace.)

Deprecated: This service is being deprecated. Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Channel::V1::CloudChannelReportsService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the CloudChannelReportsService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client-Configuration "Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all CloudChannelReportsService clients
    ::Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the CloudChannelReportsService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client#Google__Cloud__Channel__V1__CloudChannelReportsService__Rest__Client_configure_class_ "Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client-Configuration "Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client-Configuration)) 



### #fetch_report_results
    
    
    def fetch_report_results(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Channel::V1::Row>
    def fetch_report_results(report_job: nil, page_size: nil, page_token: nil, partition_keys: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Channel::V1::Row>

Retrieves data generated by [CloudChannelReportsService.RunReportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client#Google__Cloud__Channel__V1__CloudChannelReportsService__Rest__Client_run_report_job_instance_ "Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client#run_report_job \(method\)").

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

**Overloads**
    
    
    def fetch_report_results(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Channel::V1::Row>

Pass arguments to `fetch_report_results` via a request object, either of type [FetchReportResultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-FetchReportResultsRequest "Google::Cloud::Channel::V1::FetchReportResultsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::FetchReportResultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-FetchReportResultsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def fetch_report_results(report_job: nil, page_size: nil, page_token: nil, partition_keys: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Channel::V1::Row>

Pass arguments to `fetch_report_results` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **report_job** (::String) — Required. The report job created by [CloudChannelReportsService.RunReportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client#Google__Cloud__Channel__V1__CloudChannelReportsService__Rest__Client_run_report_job_instance_ "Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client#run_report_job \(method\)"). Report_job uses the format: accounts/{account_id}/reportJobs/{report_job_id} 
  * **page_size** (::Integer) — Optional. Requested page size of the report. The server may return fewer results than requested. If you don't specify a page size, the server uses a sensible default (may change over time).

The maximum value is 30,000; the server will change larger values to 30,000. 

  * **page_token** (::String) — Optional. A token that specifies a page of results beyond the first page. Obtained through [FetchReportResultsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-FetchReportResultsResponse#Google__Cloud__Channel__V1__FetchReportResultsResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::FetchReportResultsResponse#next_page_token \(method\)") of the previous [CloudChannelReportsService.FetchReportResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client#Google__Cloud__Channel__V1__CloudChannelReportsService__Rest__Client_fetch_report_results_instance_ "Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client#fetch_report_results \(method\)") call. 
  * **partition_keys** (::Array<::String>) — Optional. List of keys specifying which report partitions to return. If empty, returns all partitions. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Channel::V1::Row](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Row)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Channel::V1::Row](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Row)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::FetchReportResultsRequest.new
    
    # Call the fetch_report_results method.
    result = client.fetch_report_results request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::Row.
      p item
    end

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new CloudChannelReportsService REST client object.

**Yields**

  * (config) — Configure the CloudChannelReportsService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_reports
    
    
    def list_reports(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Channel::V1::Report>
    def list_reports(parent: nil, page_size: nil, page_token: nil, language_code: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Channel::V1::Report>

Lists the reports that RunReportJob can run. These reports include an ID, a description, and the list of columns that will be in the result.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

**Overloads**
    
    
    def list_reports(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Channel::V1::Report>

Pass arguments to `list_reports` via a request object, either of type [ListReportsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListReportsRequest "Google::Cloud::Channel::V1::ListReportsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::ListReportsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListReportsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_reports(parent: nil, page_size: nil, page_token: nil, language_code: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Channel::V1::Report>

Pass arguments to `list_reports` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the partner account to list available reports for. Parent uses the format: accounts/{account_id} 
  * **page_size** (::Integer) — Optional. Requested page size of the report. The server might return fewer results than requested. If unspecified, returns 20 reports. The maximum value is 100. 
  * **page_token** (::String) — Optional. A token that specifies a page of results beyond the first page. Obtained through [ListReportsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ListReportsResponse#Google__Cloud__Channel__V1__ListReportsResponse_next_page_token_instance_ "Google::Cloud::Channel::V1::ListReportsResponse#next_page_token \(method\)") of the previous [CloudChannelReportsService.ListReports](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client#Google__Cloud__Channel__V1__CloudChannelReportsService__Rest__Client_list_reports_instance_ "Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client#list_reports \(method\)") call. 
  * **language_code** (::String) — Optional. The BCP-47 language code, such as "en-US". If specified, the response is localized to the corresponding language code if the original data sources support it. Default is "en-US". 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Channel::V1::Report](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Report)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Channel::V1::Report](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Report)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::ListReportsRequest.new
    
    # Call the list_reports method.
    result = client.list_reports request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Channel::V1::Report.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Operations)) 



### #run_report_job
    
    
    def run_report_job(request, options = nil) -> ::Gapic::Operation
    def run_report_job(name: nil, date_range: nil, filter: nil, language_code: nil) -> ::Gapic::Operation

Begins generation of data for a given report. The report identifier is a UID (for example, `613bf59q`).

Possible error codes:

  * PERMISSION_DENIED: The user doesn't have access to this report.
  * INVALID_ARGUMENT: Required request parameters are missing or invalid.
  * NOT_FOUND: The report identifier was not found.
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support.



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of [OperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-OperationMetadata "Google::Cloud::Channel::V1::OperationMetadata \(class\)").

To get the results of report generation, call [CloudChannelReportsService.FetchReportResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelReportsService-Rest-Client#Google__Cloud__Channel__V1__CloudChannelReportsService__Rest__Client_fetch_report_results_instance_ "Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client#fetch_report_results \(method\)") with the [RunReportJobResponse.report_job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RunReportJobResponse#Google__Cloud__Channel__V1__RunReportJobResponse_report_job_instance_ "Google::Cloud::Channel::V1::RunReportJobResponse#report_job \(method\)").

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

**Overloads**
    
    
    def run_report_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `run_report_job` via a request object, either of type [RunReportJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RunReportJobRequest "Google::Cloud::Channel::V1::RunReportJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Channel::V1::RunReportJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-RunReportJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def run_report_job(name: nil, date_range: nil, filter: nil, language_code: nil) -> ::Gapic::Operation

Pass arguments to `run_report_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The report's resource name. Specifies the account and report used to generate report data. The report_id identifier is a UID (for example, `613bf59q`). Name uses the format: accounts/{account_id}/reports/{report_id} 
  * **date_range** ([::Google::Cloud::Channel::V1::DateRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-DateRange), ::Hash) — Optional. The range of usage or invoice dates to include in the result. 
  * **filter** (::String) — Optional. A structured string that defines conditions on dimension columns to restrict the report output.

Filters support logical operators (AND, OR, NOT) and conditional operators (=, !=, <, >, <=, and >=) using `column_id` as keys.

For example: `(customer:"accounts/C123abc/customers/S456def" OR customer:"accounts/C123abc/customers/S789ghi") AND invoice_start_date.year >= 2022`

  * **language_code** (::String) — Optional. The BCP-47 language code, such as "en-US". If specified, the response is localized to the corresponding language code if the original data sources support it. Default is "en-US". 



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
    
    
    require "google/cloud/channel/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Channel::V1::CloudChannelReportsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Channel::V1::RunReportJobRequest.new
    
    # Call the run_report_job method.
    result = client.run_report_job request
    
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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
