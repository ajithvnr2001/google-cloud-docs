---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DlpService-Paths/
title: Cloud Data Loss Prevention (DLP) V2 API - Module Google::Cloud::Dlp::V2::DlpService::Paths (v1.19.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:48.207884+00:00
---

# Cloud Data Loss Prevention (DLP) V2 API - Module Google::Cloud::Dlp::V2::DlpService::Paths (v1.19.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DlpService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Data Loss Prevention (DLP) V2 API - Module Google::Cloud::Dlp::V2::DlpService::Paths (v1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.1  1.17.0  1.16.1  1.15.2  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.2  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1 

Reference documentation and code samples for the Cloud Data Loss Prevention (DLP) V2 API module Google::Cloud::Dlp::V2::DlpService::Paths.

Path helper methods for the DlpService API.

## Extended By

  * [Google::Cloud::Dlp::V2::DlpService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DlpService-Paths)



## Included In

  * [Google::Cloud::Dlp::V2::DlpService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DlpService-Client)
  * [Google::Cloud::Dlp::V2::DlpService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DlpService-Paths)
  * [Google::Cloud::Dlp::V2::DlpService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DlpService-Rest-Client)



## Methods 

### #column_data_profile_path
    
    
    def column_data_profile_path(organization:, location:, column_data_profile:) -> ::String
    def column_data_profile_path(project:, location:, column_data_profile:) -> ::String

Create a fully-qualified ColumnDataProfile resource string.

**Overloads**
    
    
    def column_data_profile_path(organization:, location:, column_data_profile:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/columnDataProfiles/{column_data_profile}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **column_data_profile** (String) 


    
    
    def column_data_profile_path(project:, location:, column_data_profile:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/columnDataProfiles/{column_data_profile}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **column_data_profile** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #connection_path
    
    
    def connection_path(project:, location:, connection:) -> ::String
    def connection_path(organization:, location:, connection:) -> ::String

Create a fully-qualified Connection resource string.

**Overloads**
    
    
    def connection_path(project:, location:, connection:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/connections/{connection}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **connection** (String) 


    
    
    def connection_path(organization:, location:, connection:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/connections/{connection}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **connection** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #content_policy_path
    
    
    def content_policy_path(project:, location:, content_policy:) -> ::String

Create a fully-qualified ContentPolicy resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/contentPolicies/{content_policy}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **content_policy** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #deidentify_template_path
    
    
    def deidentify_template_path(organization:, deidentify_template:) -> ::String
    def deidentify_template_path(project:, deidentify_template:) -> ::String
    def deidentify_template_path(organization:, location:, deidentify_template:) -> ::String
    def deidentify_template_path(project:, location:, deidentify_template:) -> ::String

Create a fully-qualified DeidentifyTemplate resource string.

**Overloads**
    
    
    def deidentify_template_path(organization:, deidentify_template:) -> ::String

The resource will be in the following format:

`organizations/{organization}/deidentifyTemplates/{deidentify_template}`

**Parameters**

  * **organization** (String) 
  * **deidentify_template** (String) 


    
    
    def deidentify_template_path(project:, deidentify_template:) -> ::String

The resource will be in the following format:

`projects/{project}/deidentifyTemplates/{deidentify_template}`

**Parameters**

  * **project** (String) 
  * **deidentify_template** (String) 


    
    
    def deidentify_template_path(organization:, location:, deidentify_template:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **deidentify_template** (String) 


    
    
    def deidentify_template_path(project:, location:, deidentify_template:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **deidentify_template** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #discovery_config_path
    
    
    def discovery_config_path(project:, location:, discovery_config:) -> ::String

Create a fully-qualified DiscoveryConfig resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/discoveryConfigs/{discovery_config}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **discovery_config** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #dlp_job_path
    
    
    def dlp_job_path(project:, dlp_job:) -> ::String
    def dlp_job_path(project:, location:, dlp_job:) -> ::String

Create a fully-qualified DlpJob resource string.

**Overloads**
    
    
    def dlp_job_path(project:, dlp_job:) -> ::String

The resource will be in the following format:

`projects/{project}/dlpJobs/{dlp_job}`

**Parameters**

  * **project** (String) 
  * **dlp_job** (String) 


    
    
    def dlp_job_path(project:, location:, dlp_job:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/dlpJobs/{dlp_job}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **dlp_job** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #file_store_data_profile_path
    
    
    def file_store_data_profile_path(organization:, location:, file_store_data_profile:) -> ::String
    def file_store_data_profile_path(project:, location:, file_store_data_profile:) -> ::String

Create a fully-qualified FileStoreDataProfile resource string.

**Overloads**
    
    
    def file_store_data_profile_path(organization:, location:, file_store_data_profile:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/fileStoreDataProfiles/{file_store_data_profile}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **file_store_data_profile** (String) 


    
    
    def file_store_data_profile_path(project:, location:, file_store_data_profile:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/fileStoreDataProfiles/{file_store_data_profile}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **file_store_data_profile** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #inspect_template_path
    
    
    def inspect_template_path(organization:, inspect_template:) -> ::String
    def inspect_template_path(project:, inspect_template:) -> ::String
    def inspect_template_path(organization:, location:, inspect_template:) -> ::String
    def inspect_template_path(project:, location:, inspect_template:) -> ::String

Create a fully-qualified InspectTemplate resource string.

**Overloads**
    
    
    def inspect_template_path(organization:, inspect_template:) -> ::String

The resource will be in the following format:

`organizations/{organization}/inspectTemplates/{inspect_template}`

**Parameters**

  * **organization** (String) 
  * **inspect_template** (String) 


    
    
    def inspect_template_path(project:, inspect_template:) -> ::String

The resource will be in the following format:

`projects/{project}/inspectTemplates/{inspect_template}`

**Parameters**

  * **project** (String) 
  * **inspect_template** (String) 


    
    
    def inspect_template_path(organization:, location:, inspect_template:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/inspectTemplates/{inspect_template}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **inspect_template** (String) 


    
    
    def inspect_template_path(project:, location:, inspect_template:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/inspectTemplates/{inspect_template}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **inspect_template** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #job_trigger_path
    
    
    def job_trigger_path(project:, job_trigger:) -> ::String
    def job_trigger_path(project:, location:, job_trigger:) -> ::String

Create a fully-qualified JobTrigger resource string.

**Overloads**
    
    
    def job_trigger_path(project:, job_trigger:) -> ::String

The resource will be in the following format:

`projects/{project}/jobTriggers/{job_trigger}`

**Parameters**

  * **project** (String) 
  * **job_trigger** (String) 


    
    
    def job_trigger_path(project:, location:, job_trigger:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/jobTriggers/{job_trigger}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **job_trigger** (String) 



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



### #organization_path
    
    
    def organization_path(organization:) -> ::String

Create a fully-qualified Organization resource string.

The resource will be in the following format:

`organizations/{organization}`

**Parameter**

  * **organization** (String) 



**Returns**

  * (::String) 



### #project_data_profile_path
    
    
    def project_data_profile_path(organization:, location:, project_data_profile:) -> ::String
    def project_data_profile_path(project:, location:, project_data_profile:) -> ::String

Create a fully-qualified ProjectDataProfile resource string.

**Overloads**
    
    
    def project_data_profile_path(organization:, location:, project_data_profile:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/projectDataProfiles/{project_data_profile}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **project_data_profile** (String) 


    
    
    def project_data_profile_path(project:, location:, project_data_profile:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/projectDataProfiles/{project_data_profile}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **project_data_profile** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #project_path
    
    
    def project_path(project:) -> ::String

Create a fully-qualified Project resource string.

The resource will be in the following format:

`projects/{project}`

**Parameter**

  * **project** (String) 



**Returns**

  * (::String) 



### #stored_info_type_path
    
    
    def stored_info_type_path(organization:, stored_info_type:) -> ::String
    def stored_info_type_path(project:, stored_info_type:) -> ::String
    def stored_info_type_path(organization:, location:, stored_info_type:) -> ::String
    def stored_info_type_path(project:, location:, stored_info_type:) -> ::String

Create a fully-qualified StoredInfoType resource string.

**Overloads**
    
    
    def stored_info_type_path(organization:, stored_info_type:) -> ::String

The resource will be in the following format:

`organizations/{organization}/storedInfoTypes/{stored_info_type}`

**Parameters**

  * **organization** (String) 
  * **stored_info_type** (String) 


    
    
    def stored_info_type_path(project:, stored_info_type:) -> ::String

The resource will be in the following format:

`projects/{project}/storedInfoTypes/{stored_info_type}`

**Parameters**

  * **project** (String) 
  * **stored_info_type** (String) 


    
    
    def stored_info_type_path(organization:, location:, stored_info_type:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/storedInfoTypes/{stored_info_type}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **stored_info_type** (String) 


    
    
    def stored_info_type_path(project:, location:, stored_info_type:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/storedInfoTypes/{stored_info_type}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **stored_info_type** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #table_data_profile_path
    
    
    def table_data_profile_path(organization:, location:, table_data_profile:) -> ::String
    def table_data_profile_path(project:, location:, table_data_profile:) -> ::String

Create a fully-qualified TableDataProfile resource string.

**Overloads**
    
    
    def table_data_profile_path(organization:, location:, table_data_profile:) -> ::String

The resource will be in the following format:

`organizations/{organization}/locations/{location}/tableDataProfiles/{table_data_profile}`

**Parameters**

  * **organization** (String) 
  * **location** (String) 
  * **table_data_profile** (String) 


    
    
    def table_data_profile_path(project:, location:, table_data_profile:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/tableDataProfiles/{table_data_profile}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **table_data_profile** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
