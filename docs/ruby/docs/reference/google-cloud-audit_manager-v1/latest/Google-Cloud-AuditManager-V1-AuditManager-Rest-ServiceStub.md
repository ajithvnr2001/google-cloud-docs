---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Rest-ServiceStub/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditManager::Rest::ServiceStub (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:52.843426+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditManager::Rest::ServiceStub (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditManager::Rest::ServiceStub (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::AuditManager::Rest::ServiceStub.

REST service stub for the AuditManager service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_audit_schedule
    
    
    def create_audit_schedule(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AuditManager::V1::AuditSchedule

Baseline implementation for the create_audit_schedule REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AuditManager::V1::CreateAuditScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-CreateAuditScheduleRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #enroll_resource
    
    
    def enroll_resource(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AuditManager::V1::Enrollment

Baseline implementation for the enroll_resource REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AuditManager::V1::EnrollResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-EnrollResourceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AuditManager::V1::Enrollment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-Enrollment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::Enrollment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-Enrollment)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #generate_audit_report
    
    
    def generate_audit_report(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the generate_audit_report REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AuditManager::V1::GenerateAuditReportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditReportRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #generate_audit_scope_report
    
    
    def generate_audit_scope_report(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AuditManager::V1::AuditScopeReport

Baseline implementation for the generate_audit_scope_report REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AuditManager::V1::GenerateAuditScopeReportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditScopeReportRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AuditManager::V1::AuditScopeReport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditScopeReport)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditScopeReport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditScopeReport)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_audit_report
    
    
    def get_audit_report(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AuditManager::V1::AuditReport

Baseline implementation for the get_audit_report REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AuditManager::V1::GetAuditReportRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GetAuditReportRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AuditManager::V1::AuditReport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditReport)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditReport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditReport)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_audit_schedule
    
    
    def get_audit_schedule(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AuditManager::V1::AuditSchedule

Baseline implementation for the get_audit_schedule REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AuditManager::V1::GetAuditScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GetAuditScheduleRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_resource_enrollment_status
    
    
    def get_resource_enrollment_status(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus

Baseline implementation for the get_resource_enrollment_status REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AuditManager::V1::GetResourceEnrollmentStatusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GetResourceEnrollmentStatusRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ResourceEnrollmentStatus)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ResourceEnrollmentStatus)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_audit_reports
    
    
    def list_audit_reports(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AuditManager::V1::ListAuditReportsResponse

Baseline implementation for the list_audit_reports REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AuditManager::V1::ListAuditReportsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListAuditReportsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AuditManager::V1::ListAuditReportsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListAuditReportsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::ListAuditReportsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListAuditReportsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_audit_schedules
    
    
    def list_audit_schedules(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AuditManager::V1::ListAuditSchedulesResponse

Baseline implementation for the list_audit_schedules REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AuditManager::V1::ListAuditSchedulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListAuditSchedulesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AuditManager::V1::ListAuditSchedulesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListAuditSchedulesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::ListAuditSchedulesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListAuditSchedulesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_controls
    
    
    def list_controls(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AuditManager::V1::ListControlsResponse

Baseline implementation for the list_controls REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AuditManager::V1::ListControlsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListControlsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AuditManager::V1::ListControlsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListControlsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::ListControlsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListControlsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_resource_enrollment_statuses
    
    
    def list_resource_enrollment_statuses(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AuditManager::V1::ListResourceEnrollmentStatusesResponse

Baseline implementation for the list_resource_enrollment_statuses REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AuditManager::V1::ListResourceEnrollmentStatusesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListResourceEnrollmentStatusesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AuditManager::V1::ListResourceEnrollmentStatusesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListResourceEnrollmentStatusesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::ListResourceEnrollmentStatusesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListResourceEnrollmentStatusesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_audit_schedule
    
    
    def update_audit_schedule(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::AuditManager::V1::AuditSchedule

Baseline implementation for the update_audit_schedule REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::AuditManager::V1::UpdateAuditScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-UpdateAuditScheduleRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
