---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Paths/
title: Audit Manager V1 API - Module Google::Cloud::AuditManager::V1::AuditManager::Paths (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:46.692352+00:00
---

# Audit Manager V1 API - Module Google::Cloud::AuditManager::V1::AuditManager::Paths (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Module Google::Cloud::AuditManager::V1::AuditManager::Paths (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API module Google::Cloud::AuditManager::V1::AuditManager::Paths.

Path helper methods for the AuditManager API.

## Extended By

  * [Google::Cloud::AuditManager::V1::AuditManager::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Paths)



## Included In

  * [Google::Cloud::AuditManager::V1::AuditManager::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client)
  * [Google::Cloud::AuditManager::V1::AuditManager::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Paths)
  * [Google::Cloud::AuditManager::V1::AuditManager::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Rest-Client)



## Methods 

### #audit_report_path
    
    
    def audit_report_path(project:, location:, audit_report:) -> ::String
    def audit_report_path(folder:, location:, audit_report:) -> ::String
    def audit_report_path(organization:, location:, audit_report:) -> ::String

Create a fully-qualified AuditReport resource string.

**Overloads**
    
    
    def audit_report_path(project:, location:, audit_report:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/auditReports/{audit_report}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **audit_report** (String) 


    
    
    def audit_report_path(folder:, location:, audit_report:) -> ::String

The resource will be in the following format:

`folders/{folder}/locations/{location}/auditReports/{audit_report}`

**Parameters**

  * **folder** (String) 
  * **location** (String) 
  * **audit_report** (String) 


    
    
    def audit_report_path(organization:, location:, audit_report:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/auditReports/{audit_report}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **audit_report** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #audit_schedule_path
    
    
    def audit_schedule_path(project:, location:, audit_schedule:) -> ::String
    def audit_schedule_path(folder:, location:, audit_schedule:) -> ::String
    def audit_schedule_path(organization:, location:, audit_schedule:) -> ::String

Create a fully-qualified AuditSchedule resource string.

**Overloads**
    
    
    def audit_schedule_path(project:, location:, audit_schedule:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/auditSchedules/{audit_schedule}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **audit_schedule** (String) 


    
    
    def audit_schedule_path(folder:, location:, audit_schedule:) -> ::String

The resource will be in the following format:

`folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}`

**Parameters**

  * **folder** (String) 
  * **location** (String) 
  * **audit_schedule** (String) 


    
    
    def audit_schedule_path(organization:, location:, audit_schedule:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/auditSchedules/{audit_schedule}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **audit_schedule** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #enrollment_status_scope_path
    
    
    def enrollment_status_scope_path(folder:, location:) -> ::String
    def enrollment_status_scope_path(organization:, location:) -> ::String

Create a fully-qualified EnrollmentStatusScope resource string.

**Overloads**
    
    
    def enrollment_status_scope_path(folder:, location:) -> ::String

The resource will be in the following format:

`folders/{folder}/locations/{location}`

**Parameters**

  * **folder** (String) 
  * **location** (String) 


    
    
    def enrollment_status_scope_path(organization:, location:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #folder_location_path
    
    
    def folder_location_path(folder:, location:) -> ::String

Create a fully-qualified FolderLocation resource string.

The resource will be in the following format:

`folders/{folder}/locations/{location}`

**Parameters**

  * **folder** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #organization_location_path
    
    
    def organization_location_path(organization:, location:) -> ::String

Create a fully-qualified OrganizationLocation resource string.

The resource will be in the following format:

`organizations/{organization}/locations/{location}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #resource_enrollment_status_path
    
    
    def resource_enrollment_status_path(folder:, location:, resource_enrollment_status:) -> ::String
    def resource_enrollment_status_path(project:, location:, resource_enrollment_status:) -> ::String
    def resource_enrollment_status_path(organization:, location:, resource_enrollment_status:) -> ::String

Create a fully-qualified ResourceEnrollmentStatus resource string.

**Overloads**
    
    
    def resource_enrollment_status_path(folder:, location:, resource_enrollment_status:) -> ::String

The resource will be in the following format:

`folders/{folder}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`

**Parameters**

  * **folder** (String) 
  * **location** (String) 
  * **resource_enrollment_status** (String) 


    
    
    def resource_enrollment_status_path(project:, location:, resource_enrollment_status:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **resource_enrollment_status** (String) 


    
    
    def resource_enrollment_status_path(organization:, location:, resource_enrollment_status:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **resource_enrollment_status** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #standard_path
    
    
    def standard_path(project:, location:, standard:) -> ::String
    def standard_path(folder:, location:, standard:) -> ::String
    def standard_path(organization:, location:, standard:) -> ::String

Create a fully-qualified Standard resource string.

**Overloads**
    
    
    def standard_path(project:, location:, standard:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/standards/{standard}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **standard** (String) 


    
    
    def standard_path(folder:, location:, standard:) -> ::String

The resource will be in the following format:

`folders/{folder}/locations/{location}/standards/{standard}`

**Parameters**

  * **folder** (String) 
  * **location** (String) 
  * **standard** (String) 


    
    
    def standard_path(organization:, location:, standard:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/standards/{standard}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **standard** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
