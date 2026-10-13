---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditManager::Client (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:46.002829+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditManager::Client (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditManager::Client (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::AuditManager::Client.

Client for the AuditManager service.

Service describing handlers for resources

## Inherits

  * Object 



## Includes

  * [Google::Cloud::AuditManager::V1::AuditManager::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the AuditManager Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client-Configuration "Google::Cloud::AuditManager::V1::AuditManager::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all AuditManager clients
    ::Google::Cloud::AuditManager::V1::AuditManager::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the AuditManager Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client#Google__Cloud__AuditManager__V1__AuditManager__Client_configure_class_ "Google::Cloud::AuditManager::V1::AuditManager::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client-Configuration "Google::Cloud::AuditManager::V1::AuditManager::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client-Configuration)) 



### #create_audit_schedule
    
    
    def create_audit_schedule(request, options = nil) -> ::Google::Cloud::AuditManager::V1::AuditSchedule
    def create_audit_schedule(parent: nil, audit_schedule: nil, audit_schedule_id: nil, validate_only: nil) -> ::Google::Cloud::AuditManager::V1::AuditSchedule

Creates a new audit schedule in a given project and location.

**Overloads**
    
    
    def create_audit_schedule(request, options = nil) -> ::Google::Cloud::AuditManager::V1::AuditSchedule

Pass arguments to `create_audit_schedule` via a request object, either of type [CreateAuditScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-CreateAuditScheduleRequest "Google::Cloud::AuditManager::V1::CreateAuditScheduleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AuditManager::V1::CreateAuditScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-CreateAuditScheduleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_audit_schedule(parent: nil, audit_schedule: nil, audit_schedule_id: nil, validate_only: nil) -> ::Google::Cloud::AuditManager::V1::AuditSchedule

Pass arguments to `create_audit_schedule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Project or folder that this audit schedule is for, in one of the following formats:

    * `projects/{project}/locations/{location}`
    * `folders/{folder}/locations/{location}`
  * **audit_schedule** ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule), ::Hash) — Required. Audit schedule to create. 
  * **audit_schedule_id** (::String) — Required. ID to use for the audit schedule, which becomes the final component of the audit schedule's resource name. 
  * **validate_only** (::Boolean) — 

Optional. If `true`, only validates the request and does not create the audit schedule. This executes standard request validation (such as schema, framework existence, scope, and IAM checks) and skips the apply phase.

Use this field for the following purposes:

    * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
    * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
    * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without consuming resource quotas.



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/audit_manager/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AuditManager::V1::CreateAuditScheduleRequest.new
    
    # Call the create_audit_schedule method.
    result = client.create_audit_schedule request
    
    # The returned object is of type Google::Cloud::AuditManager::V1::AuditSchedule.
    p result

### #enroll_resource
    
    
    def enroll_resource(request, options = nil) -> ::Google::Cloud::AuditManager::V1::Enrollment
    def enroll_resource(scope: nil, destinations: nil, validate_only: nil) -> ::Google::Cloud::AuditManager::V1::Enrollment

Adds your project, folder, or organization to Audit Manager. This method creates the Audit Manager service agent in your workload and grants required permissions to the service agent. If you make this request on a workload that's already enrolled, then this method overrides the existing set of destinations.

**Overloads**
    
    
    def enroll_resource(request, options = nil) -> ::Google::Cloud::AuditManager::V1::Enrollment

Pass arguments to `enroll_resource` via a request object, either of type [EnrollResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-EnrollResourceRequest "Google::Cloud::AuditManager::V1::EnrollResourceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AuditManager::V1::EnrollResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-EnrollResourceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def enroll_resource(scope: nil, destinations: nil, validate_only: nil) -> ::Google::Cloud::AuditManager::V1::Enrollment

Pass arguments to `enroll_resource` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **scope** (::String) — 

Required. Organization, folder, or project to enroll in Audit Manager, in one of the following formats:

    * `projects/{project}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `organizations/{organization}/locations/{location}`
  * **destinations** (::Array<[::Google::Cloud::AuditManager::V1::EnrollResourceRequest::EligibleDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-EnrollResourceRequest-EligibleDestination), ::Hash>) — Required. Cloud Storage buckets that you can upload your audit reports to during the audit process.

When you enroll an organization or folder, you can choose a Cloud Storage bucket from any project in the organization or folder. If you run an audit at the project level using the service agent at the organization or folder level, all the buckets that are associated with the service agent are available. 

  * **validate_only** (::Boolean) — 

Optional. If `true`, only validates the request and does not enroll the resource. This executes standard request validation (such as schema, IAM, and destination checks) and skips the apply phase.

Use this field for the following purposes:

    * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
    * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
    * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without consuming resource quotas.



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AuditManager::V1::Enrollment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-Enrollment)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::Enrollment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-Enrollment)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/audit_manager/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AuditManager::V1::EnrollResourceRequest.new
    
    # Call the enroll_resource method.
    result = client.enroll_resource request
    
    # The returned object is of type Google::Cloud::AuditManager::V1::Enrollment.
    p result

### #generate_audit_report
    
    
    def generate_audit_report(request, options = nil) -> ::Gapic::Operation
    def generate_audit_report(gcs_uri: nil, scope: nil, compliance_standard: nil, report_format: nil, compliance_framework: nil, validate_only: nil) -> ::Gapic::Operation

Registers audit report generation requests. This method returns the operation identifier that you can use to track the report generation progress.

**Overloads**
    
    
    def generate_audit_report(request, options = nil) -> ::Gapic::Operation

Pass arguments to `generate_audit_report` via a request object, either of type [GenerateAuditReportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditReportRequest "Google::Cloud::AuditManager::V1::GenerateAuditReportRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AuditManager::V1::GenerateAuditReportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditReportRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def generate_audit_report(gcs_uri: nil, scope: nil, compliance_standard: nil, report_format: nil, compliance_framework: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `generate_audit_report` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **gcs_uri** (::String) — URL for the Cloud Storage bucket where the report and evidence is uploaded. You must select a bucket that was provided during the enrollment process. 
  * **scope** (::String) — 

Required. Organization, folder, or project that the audit applies to, in one of the following formats:

    * `projects/{project}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `organizations/{organization}/locations/{location}`
  * **compliance_standard** (::String) — Optional. Deprecated. Compliance standard for the audit report.

Use the `compliance_framework` field instead. 

  * **report_format** ([::Google::Cloud::AuditManager::V1::GenerateAuditReportRequest::AuditReportFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditReportRequest-AuditReportFormat)) — Required. Format for the audit report. 
  * **compliance_framework** (::String) — Required. The framework that's used for the audit report. For example, `NIST_800_53`. 
  * **validate_only** (::Boolean) — 

Optional. If `true`, only validates the request and does not generate the audit report. This executes standard request validation (such as schema, framework existence, scope, and IAM checks) and skips the apply phase.

Use this field for the following purposes:

    * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
    * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
    * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without triggering expensive Long-Running Operations (LROs) or consuming resource quotas.



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
    
    
    require "google/cloud/audit_manager/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AuditManager::V1::GenerateAuditReportRequest.new
    
    # Call the generate_audit_report method.
    result = client.generate_audit_report request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #generate_audit_scope_report
    
    
    def generate_audit_scope_report(request, options = nil) -> ::Google::Cloud::AuditManager::V1::AuditScopeReport
    def generate_audit_scope_report(scope: nil, compliance_standard: nil, report_format: nil, compliance_framework: nil, validate_only: nil) -> ::Google::Cloud::AuditManager::V1::AuditScopeReport

Generates an audit scope report for the given standard.

The report includes the following:

  * The technical attributes and constraints that Audit Manager uses to verify your compliance with a framework.
  * A list of Google Cloud services and resources that are within the scope of the framework.



**Overloads**
    
    
    def generate_audit_scope_report(request, options = nil) -> ::Google::Cloud::AuditManager::V1::AuditScopeReport

Pass arguments to `generate_audit_scope_report` via a request object, either of type [GenerateAuditScopeReportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditScopeReportRequest "Google::Cloud::AuditManager::V1::GenerateAuditScopeReportRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AuditManager::V1::GenerateAuditScopeReportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditScopeReportRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def generate_audit_scope_report(scope: nil, compliance_standard: nil, report_format: nil, compliance_framework: nil, validate_only: nil) -> ::Google::Cloud::AuditManager::V1::AuditScopeReport

Pass arguments to `generate_audit_scope_report` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **scope** (::String) — 

Required. Project or folder that the audit scope report is generated for, in one of the following formats:

    * `projects/{project}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `organizations/{organization}/locations/{location}`
  * **compliance_standard** (::String) — Optional. Deprecated. The standard (industry or regulatory requirements) that the audit scope report is run against.

Use the `compliance_framework` field instead. 

  * **report_format** ([::Google::Cloud::AuditManager::V1::GenerateAuditScopeReportRequest::AuditScopeReportFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditScopeReportRequest-AuditScopeReportFormat)) — Required. Format for the audit scope report. 
  * **compliance_framework** (::String) — Required. Framework (set of controls) that the audit scope report is generated against. For example, `NIST_800_53`. 
  * **validate_only** (::Boolean) — 

Optional. If `true`, only validates the request and does not generate the audit scope report. This executes standard request validation (such as schema, framework existence, scope, and IAM checks) and skips the apply phase.

Use this field for the following purposes:

    * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
    * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
    * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without consuming resource quotas.



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AuditManager::V1::AuditScopeReport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditScopeReport)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditScopeReport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditScopeReport)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/audit_manager/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AuditManager::V1::GenerateAuditScopeReportRequest.new
    
    # Call the generate_audit_scope_report method.
    result = client.generate_audit_scope_report request
    
    # The returned object is of type Google::Cloud::AuditManager::V1::AuditScopeReport.
    p result

### #get_audit_report
    
    
    def get_audit_report(request, options = nil) -> ::Google::Cloud::AuditManager::V1::AuditReport
    def get_audit_report(name: nil) -> ::Google::Cloud::AuditManager::V1::AuditReport

Gets the full metadata and findings for an audit report.

**Overloads**
    
    
    def get_audit_report(request, options = nil) -> ::Google::Cloud::AuditManager::V1::AuditReport

Pass arguments to `get_audit_report` via a request object, either of type [GetAuditReportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GetAuditReportRequest "Google::Cloud::AuditManager::V1::GetAuditReportRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AuditManager::V1::GetAuditReportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GetAuditReportRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_audit_report(name: nil) -> ::Google::Cloud::AuditManager::V1::AuditReport

Pass arguments to `get_audit_report` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. Name of the audit report, in one of the following formats:

    * `projects/{project}/locations/{location}/auditReports/{audit_report}`
    * `folders/{folder}/locations/{location}/auditReports/{audit_report}`
    * `organizations/{organization}/locations/{location}/auditReports/{audit_report}`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AuditManager::V1::AuditReport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditReport)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditReport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditReport)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/audit_manager/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AuditManager::V1::GetAuditReportRequest.new
    
    # Call the get_audit_report method.
    result = client.get_audit_report request
    
    # The returned object is of type Google::Cloud::AuditManager::V1::AuditReport.
    p result

### #get_audit_schedule
    
    
    def get_audit_schedule(request, options = nil) -> ::Google::Cloud::AuditManager::V1::AuditSchedule
    def get_audit_schedule(name: nil) -> ::Google::Cloud::AuditManager::V1::AuditSchedule

Gets details of a single audit schedule.

**Overloads**
    
    
    def get_audit_schedule(request, options = nil) -> ::Google::Cloud::AuditManager::V1::AuditSchedule

Pass arguments to `get_audit_schedule` via a request object, either of type [GetAuditScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GetAuditScheduleRequest "Google::Cloud::AuditManager::V1::GetAuditScheduleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AuditManager::V1::GetAuditScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GetAuditScheduleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_audit_schedule(name: nil) -> ::Google::Cloud::AuditManager::V1::AuditSchedule

Pass arguments to `get_audit_schedule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. Name of the audit schedule to retrieve, in one of the following formats:

    * `projects/{project}/locations/{location}/auditSchedules/{audit_schedule}`
    * `folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}`
    * `organizations/{organization}/locations/{location}/auditSchedules/{audit_schedule}`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/audit_manager/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AuditManager::V1::GetAuditScheduleRequest.new
    
    # Call the get_audit_schedule method.
    result = client.get_audit_schedule request
    
    # The returned object is of type Google::Cloud::AuditManager::V1::AuditSchedule.
    p result

### #get_resource_enrollment_status
    
    
    def get_resource_enrollment_status(request, options = nil) -> ::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus
    def get_resource_enrollment_status(name: nil) -> ::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus

Gets a resource and its enrollment status.

**Overloads**
    
    
    def get_resource_enrollment_status(request, options = nil) -> ::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus

Pass arguments to `get_resource_enrollment_status` via a request object, either of type [GetResourceEnrollmentStatusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GetResourceEnrollmentStatusRequest "Google::Cloud::AuditManager::V1::GetResourceEnrollmentStatusRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AuditManager::V1::GetResourceEnrollmentStatusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GetResourceEnrollmentStatusRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_resource_enrollment_status(name: nil) -> ::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus

Pass arguments to `get_resource_enrollment_status` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. Name of the resource enrollment status, in one of the following formats:

    * `folders/{folder}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`
    * `projects/{project}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`
    * `organizations/{organization}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ResourceEnrollmentStatus)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ResourceEnrollmentStatus)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/audit_manager/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AuditManager::V1::GetResourceEnrollmentStatusRequest.new
    
    # Call the get_resource_enrollment_status method.
    result = client.get_resource_enrollment_status request
    
    # The returned object is of type Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new AuditManager client object.

**Yields**

  * (config) — Configure the AuditManager client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AuditManager::V1::AuditManager::Client.new do |config|
      config.timeout = 10.0
    end

### #list_audit_reports
    
    
    def list_audit_reports(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::AuditReport>
    def list_audit_reports(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::AuditReport>

Lists the audit reports for the organization, folder, or project that you specify as the parent scope.

**Overloads**
    
    
    def list_audit_reports(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::AuditReport>

Pass arguments to `list_audit_reports` via a request object, either of type [ListAuditReportsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListAuditReportsRequest "Google::Cloud::AuditManager::V1::ListAuditReportsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AuditManager::V1::ListAuditReportsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListAuditReportsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_audit_reports(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::AuditReport>

Pass arguments to `list_audit_reports` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Parent organization, folder, or project to list reports for, in one of the following formats:

    * `projects/{project}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `organizations/{organization}/locations/{location}`
  * **page_size** (::Integer) — Optional. Maximum number of items to return in a single page. The service might return fewer items than this value. If unspecified, the service picks an appropriate default. The maximum value is 100; values above 100 are reduced to 100. 
  * **page_token** (::String) — Optional. A page token, received from a previous call, to retrieve the next page of results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::AuditManager::V1::AuditReport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditReport)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::AuditManager::V1::AuditReport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditReport)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/audit_manager/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AuditManager::V1::ListAuditReportsRequest.new
    
    # Call the list_audit_reports method.
    result = client.list_audit_reports request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AuditManager::V1::AuditReport.
      p item
    end

### #list_audit_schedules
    
    
    def list_audit_schedules(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::AuditSchedule>
    def list_audit_schedules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::AuditSchedule>

Lists audit schedules in a given project and location.

**Overloads**
    
    
    def list_audit_schedules(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::AuditSchedule>

Pass arguments to `list_audit_schedules` via a request object, either of type [ListAuditSchedulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListAuditSchedulesRequest "Google::Cloud::AuditManager::V1::ListAuditSchedulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AuditManager::V1::ListAuditSchedulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListAuditSchedulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_audit_schedules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::AuditSchedule>

Pass arguments to `list_audit_schedules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Parent for the audit schedule, in one of the following formats:

    * `projects/{project}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `organizations/{organization}/locations/{location}`
  * **page_size** (::Integer) — Optional. Maximum number of items to return in a single page. The service might return fewer items than this value. If unspecified, the service picks an appropriate default. The maximum value is 100; values above 100 are reduced to 100. 
  * **page_token** (::String) — Optional. A page token, received from a previous call, to retrieve the next page of results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/audit_manager/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AuditManager::V1::ListAuditSchedulesRequest.new
    
    # Call the list_audit_schedules method.
    result = client.list_audit_schedules request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AuditManager::V1::AuditSchedule.
      p item
    end

### #list_controls
    
    
    def list_controls(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::Control>
    def list_controls(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::Control>

Lists the controls that you must implement to become compliant to a regulatory standard.

**Overloads**
    
    
    def list_controls(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::Control>

Pass arguments to `list_controls` via a request object, either of type [ListControlsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListControlsRequest "Google::Cloud::AuditManager::V1::ListControlsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AuditManager::V1::ListControlsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListControlsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_controls(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::Control>

Pass arguments to `list_controls` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Standard to list controls for, in one of the following formats:

    * `projects/{project}/locations/{location}/standards/{standard}`
    * `folders/{folder}/locations/{location}/standards/{standard}`
    * `organizations/{organization}/locations/{location}/standards/{standard}`
  * **page_size** (::Integer) — Optional. Maximum number of items to return in a single page. The service might return fewer items than this value. If unspecified, the service picks an appropriate default. The maximum value is 100; values above 100 are reduced to 100. 
  * **page_token** (::String) — Optional. A page token, received from a previous call, to retrieve the next page of results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::AuditManager::V1::Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-Control)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::AuditManager::V1::Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-Control)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/audit_manager/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AuditManager::V1::ListControlsRequest.new
    
    # Call the list_controls method.
    result = client.list_controls request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AuditManager::V1::Control.
      p item
    end

### #list_resource_enrollment_statuses
    
    
    def list_resource_enrollment_statuses(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus>
    def list_resource_enrollment_statuses(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus>

Lists all the folders and projects in an organization or folder, along with their enrollments.

**Overloads**
    
    
    def list_resource_enrollment_statuses(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus>

Pass arguments to `list_resource_enrollment_statuses` via a request object, either of type [ListResourceEnrollmentStatusesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListResourceEnrollmentStatusesRequest "Google::Cloud::AuditManager::V1::ListResourceEnrollmentStatusesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AuditManager::V1::ListResourceEnrollmentStatusesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListResourceEnrollmentStatusesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_resource_enrollment_statuses(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus>

Pass arguments to `list_resource_enrollment_statuses` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. Parent organization or folder to list enrollment statuses for, in one of the following formats:

    * `folders/{folder}/locations/{location}`
    * `organizations/{organization}/locations/{location}`
  * **page_size** (::Integer) — Optional. Maximum number of items to return in a single page. The service might return fewer items than this value. If unspecified, the service picks an appropriate default. The maximum value is 100; values above 100 are reduced to 100. 
  * **page_token** (::String) — Optional. A page token, received from a previous call, to retrieve the next page of results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ResourceEnrollmentStatus)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ResourceEnrollmentStatus)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/audit_manager/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AuditManager::V1::ListResourceEnrollmentStatusesRequest.new
    
    # Call the list_resource_enrollment_statuses method.
    result = client.list_resource_enrollment_statuses request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus.
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
    
    
    def operations_client() -> ::Google::Cloud::AuditManager::V1::AuditManager::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditManager::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_audit_schedule
    
    
    def update_audit_schedule(request, options = nil) -> ::Google::Cloud::AuditManager::V1::AuditSchedule
    def update_audit_schedule(audit_schedule: nil, update_mask: nil, validate_only: nil) -> ::Google::Cloud::AuditManager::V1::AuditSchedule

Updates an existing audit schedule.

**Overloads**
    
    
    def update_audit_schedule(request, options = nil) -> ::Google::Cloud::AuditManager::V1::AuditSchedule

Pass arguments to `update_audit_schedule` via a request object, either of type [UpdateAuditScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-UpdateAuditScheduleRequest "Google::Cloud::AuditManager::V1::UpdateAuditScheduleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AuditManager::V1::UpdateAuditScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-UpdateAuditScheduleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_audit_schedule(audit_schedule: nil, update_mask: nil, validate_only: nil) -> ::Google::Cloud::AuditManager::V1::AuditSchedule

Pass arguments to `update_audit_schedule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **audit_schedule** ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule), ::Hash) — Required. Audit schedule to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. List of fields to update. 
  * **validate_only** (::Boolean) — 

Optional. If `true`, only validates the request and does not update the audit schedule. This executes standard request validation (such as schema, framework existence, scope, and IAM checks) and skips the apply phase.

Use this field for the following purposes:

    * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
    * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
    * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without consuming resource quotas.



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/audit_manager/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AuditManager::V1::AuditManager::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AuditManager::V1::UpdateAuditScheduleRequest.new
    
    # Call the update_audit_schedule method.
    result = client.update_audit_schedule request
    
    # The returned object is of type Google::Cloud::AuditManager::V1::AuditSchedule.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
