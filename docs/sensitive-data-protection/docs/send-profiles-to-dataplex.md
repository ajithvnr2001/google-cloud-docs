---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-dataplex/
title: Tag tables in Data Catalog based on insights from data profiles \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:35:18.135223+00:00
---

# Tag tables in Data Catalog based on insights from data profiles  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-dataplex/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Tag tables in Data Catalog based on insights from data profiles Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** On or after September 30, 2025, you can no longer send discovery results from Sensitive Data Protection to Data Catalog. Data Catalog is deprecated and will be discontinued on June 1, 2026.

We recommend that you send the discovery results to Knowledge Catalog instead. For more information, see [Add Knowledge Catalog aspects based on insights from data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects). To migrate existing discovery configurations, see [Migrate to the Send to Dataplex Catalog as aspects action](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects#migrate).

Tags and tag templates created for you by Sensitive Data Protection are available in Knowledge Catalog as _aspects_. For steps to transition your Data Catalog content to Knowledge Catalog, see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog) in the Knowledge Catalog documentation.

This page describes how to automatically apply Data Catalog tags to BigQuery tables after Sensitive Data Protection profiles those tables. This page also provides example queries that you can use to find tagged data across your organization and projects.

This feature is useful if you want to enrich your manually curated metadata in Knowledge Catalog with insights gathered from Sensitive Data Protection data profiles. The generated tags include the following insights:

  * Information types ([_infoTypes_](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference)) detected in the columns of the table
  * Calculated sensitivity level of the table
  * Calculated data risk level of the table



Insights from Sensitive Data Protection data profiles can help you use Knowledge Catalog to discover sensitive and high-risk data in your organization. Use these insights to help you make informed decisions about how to manage and govern your data.

If you want to send the results of inspection jobs—not data profiling operations—to Knowledge Catalog, see [Send Sensitive Data Protection inspection results to Data Catalog](https://docs.cloud.google.com/sensitive-data-protection/docs/sending-results-to-dc) instead.

## About data profiles

You can configure Sensitive Data Protection to automatically generate profiles about data across an organization, folder, or project. [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) contain metrics and metadata about your data and help you determine where [sensitive and high-risk data](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation) reside. Sensitive Data Protection reports these metrics at various levels of detail. For information about the types of data you can profile, see [Supported resources](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#supported-resources). 

## About Knowledge Catalog and Data Catalog

[Knowledge Catalog](https://docs.cloud.google.com/dataplex) is a Google Cloud service that unifies distributed data and automates data management and governance for that data. [Data Catalog](https://docs.cloud.google.com/data-catalog/docs/concepts/overview) ([Deprecated](https://docs.cloud.google.com/data-catalog/docs/deprecations)) is a fully managed, scalable metadata management service.

Data Catalog lets you use _tags_ and _tag templates_ to attach business metadata to your data. You can then search and manage all metadata for your organization or project in a unified service. For more information, see [Tags and tag templates](https://docs.cloud.google.com/data-catalog/docs/tags-and-tag-templates).

## How it works

If your discovery scan configuration has the **Send to Dataplex as tags** action enabled, Sensitive Data Protection does the following each time it profiles your data. This action is only applied to new and updated profiles. Existing profiles that aren't updated aren't sent to Knowledge Catalog. 

  1. Creates a [private tag template](https://docs.cloud.google.com/data-catalog/docs/tags-and-tag-templates#private_tags) containing the schema of the tags that will be attached to your BigQuery tables. For information about the name, ID, and location of the tag template, see Tag template details.

Only principals with the proper roles and permissions can view the tag template.

  2. Creates a tag for each BigQuery table that you profile. The tag is based on the newly created tag template.

For example, a resulting tag attached to a table can have the following metadata:

Display name | Value  
---|---  
`Column Insights` | `ccn: CREDIT_CARD_NUMBER`  
`first_name: PERSON_NAME`  
`last_name: PERSON_NAME`  
`ssn: US_SOCIAL_SECURITY_NUMBER`  
`email: EMAIL_ADDRESS`  
`Column Sensitivity` | `ccn: HIGH`  
`first_name: MODERATE`  
`last_name: MODERATE`  
`favorite_animal: LOW`  
`ssn: HIGH`  
`email: MODERATE`  
`id: LOW`  
`Data Risk Level` | `HIGH`  
`Other InfoTypes` | `PHONE_NUMBER`  
`Predicted InfoTypes` | `CREDIT_CARD_NUMBER,US_SOCIAL_SECURITY_NUMBER,EMAIL_ADDRESS,PERSON_NAME`  
`Profile Last Generated` | `DATE at TIME`  
`Sensitive Data Profile` | `organizations/ORGANIZATION_ID/locations/REGION/tableDataProfiles/TABLE_DATA_PROFILE_ID`  
`Sensitivity Score` | `HIGH`  



A table has two tags if it was profiled through both of the following:

  * An organization-level or folder-level scan configuration
  * A project-level scan configuration



After the tables are tagged, you can search Knowledge Catalog for all data in your organization or project with specific tag values.

## Tag template details

The template name, template ID, and the project where the new tag template is stored depend on the resource that the scan configuration pertains to.

  * If the scan configuration is an organization-level or folder-level configuration, the tag template is stored in the [service agent container](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container). The name of the tag template is `Sensitive Data Profile`. Its template ID is `sensitive_data_profile`.
  * If the scan configuration is a project-level configuration, the tag template is stored in the project to be profiled. The name of the tag template is `Sensitive Data Profile (Project)`. Its template ID is `sensitive_data_profile_project`.



## Pricing

For information about how other Google Cloud services may charge you for exporting data profiles, see [Pricing for exporting data profiles](https://cloud.google.com/sensitive-data-protection/pricing#exporting-profiles-pricing).

## Automatically tag BigQuery tables based on data profiles

  1. Create a scan configuration. Alternatively, [edit](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#edit-config) an existing scan configuration.

     * To create a scan configuration at the organization or folder level, see [Profile data in an organization or folder](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder).
     * To create a scan configuration at the project level, see [Profile data in a single project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project).
  2. In the **Add actions** step, make sure **Send to Dataplex as tags** is turned on.

     * If you're creating a scan configuration, this action is enabled by default.
     * If you're editing a scan configuration, you must enable this action.



After the data is profiled and tagged, you can start searching for tagged data in Knowledge Catalog.

## Roles and permissions for viewing tags

Knowledge Catalog search results show you only the data that you have access to. You need the following Identity and Access Management (IAM) roles or permissions to search for the tags that are attached to your BigQuery tables.

Purpose | Predefined role | Relevant permissions  
---|---|---  
View the private tag template | Data Catalog TagTemplate Viewer (`roles/datacatalog.tagTemplateViewer`) | `datacatalog.tagTemplates.getTag`  
View the tags applied to BigQuery tables | BigQuery Metadata Viewer (`roles/bigquery.metadataViewer`) | `bigquery.datasets.get`  
`bigquery.tables.get`  
  
For more information about Knowledge Catalog roles, see [Roles to view public and private tags](https://docs.cloud.google.com/data-catalog/docs/concepts/iam#roles_to_view_public_and_private_tags).

For information about granting a predefined role, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role). If you want to use a custom role instead of a predefined role, make sure that the custom role has the relevant permissions. For more information, see a [Create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating).

## Find the generated tag template

  1. In the Google Cloud console, go to the Knowledge Catalog **Tag Templates** page.

[Go to Tag templates](https://console.cloud.google.com/dataplex/templates)

  2. In the list, find the tag template. For information about the name, ID, and location of the tag template, see Tag template details.

  3. Optional: To find the tag template that was generated by a given discovery scan configuration, enter the following in the **Filter** field:
         
         name:PROJECT_ID.TAG_TEMPLATE_ID
         

Replace the following:

     * PROJECT_ID: the ID of the project that is associated with the scan configuration. If you profiled your data at the organization or folder level, enter the project ID of the service agent container.
     * TAG_TEMPLATE_ID: `sensitive_data_profile` if the scan configuration is for an organization or a folder; `sensitive_data_profile_project` if the scan configuration is for a project. 



## Find the generated tag for a given table data profile

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/search)

  2. In the **Search** field, enter the following:
         
         name:TABLE_ID tag:PROJECT_ID.TAG_TEMPLATE_ID
         

Replace the following:

     * TABLE_ID: the ID of the table that was profiled.
     * PROJECT_ID: the ID of the project that contains the tag template. If you profiled your data at the organization or folder level, enter the project ID of the service agent container.
     * TAG_TEMPLATE_ID: `sensitive_data_profile` if the scan configuration is for an organization or a folder; `sensitive_data_profile_project` if the scan configuration is for a project. 
  3. In the list that appears, click the table ID. The details of the BigQuery table appear along with any `Sensitive Data Profile` or `Sensitive Data Profile (Project)` tags attached to it.

A table has two tags if it was profiled through both of the following:

     * An organization-level or folder-level scan configuration
     * A project-level scan configuration



For information about how to perform a search through the Data Catalog API, see [How to search for data assets](https://docs.cloud.google.com/data-catalog/docs/how-to/search#how_to_search_for_data_assets).

## Example search queries

This section provides example search queries that you can use in Knowledge Catalog to find data in your organization or project with specific tag values.

You can find only the data that you have access to. Data access is controlled through IAM permissions. For more information, see Roles and permissions for viewing tags on this page.

You can enter these queries in the Knowledge Catalog **Search** page in the Google Cloud console.

[Go to Search](https://console.cloud.google.com/dataplex/search)

For information about how to form the queries, see [Data Catalog search syntax](https://docs.cloud.google.com/data-catalog/docs/how-to/search-reference). For information about how to perform a search through the Data Catalog API, see [How to search for data assets](https://docs.cloud.google.com/data-catalog/docs/how-to/search#how_to_search_for_data_assets).

### Find all tables that are tagged using the new tag template
    
    
    tag:PROJECT_ID.TAG_TEMPLATE_ID
    

Replace the following:

  * PROJECT_ID: the ID of the project that contains the tag template. If you profiled your data at the organization or folder level, enter the project ID of the service agent container.
  * TAG_TEMPLATE_ID: `sensitive_data_profile` if the scan configuration is for an organization or a folder; `sensitive_data_profile_project` if the scan configuration is for a project. 



The succeeding examples on this page don't include the project ID, so you might get results associated with various discovery scan configurations. To limit your results to a particular scan configuration, add the project ID to the query as shown in this example.

### Find all tables that were last profiled before a given date
    
    
    tag:TAG_TEMPLATE_ID.profile_last_generated<DATE
    

Replace the following:

  * TAG_TEMPLATE_ID: `sensitive_data_profile` if the scan configuration is for an organization or a folder; `sensitive_data_profile_project` if the scan configuration is for a project. 
  * DATE: a date in the format `YYYY-MM-DD`—for example, `2023-01-15`.



### Find all tables with a given table-level sensitivity score
    
    
    tag:TAG_TEMPLATE_ID.sensitivity_score=SENSITIVITY_SCORE
    

Replace the following:

  * TAG_TEMPLATE_ID: `sensitive_data_profile` if the scan configuration is for an organization or a folder; `sensitive_data_profile_project` if the scan configuration is for a project. 
  * SENSITIVITY_SCORE: one of `HIGH`, `MODERATE`, or `LOW`.



For more information, see [Data risk and sensitivity levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

### Find all tables with a given data risk level
    
    
    tag:TAG_TEMPLATE_ID.data_risk_level=DATA_RISK_LEVEL
    

Replace the following:

  * TAG_TEMPLATE_ID: `sensitive_data_profile` if the scan configuration is for an organization or a folder; `sensitive_data_profile_project` if the scan configuration is for a project. 
  * DATA_RISK_LEVEL: one of `HIGH`, `MODERATE`, or `LOW`.



For more information, see [Data risk and sensitivity levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

### Find all tables that contain a given predicted infoType
    
    
    tag:TAG_TEMPLATE_ID.predicted_info_types:INFOTYPE
    

Replace the following:

  * TAG_TEMPLATE_ID: `sensitive_data_profile` if the scan configuration is for an organization or a folder; `sensitive_data_profile_project` if the scan configuration is for a project. 
  * INFOTYPE: the infoType—for example, `PERSON_NAME`.



For a list of all built-in infoTypes, see [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

For more information, see **Predicted infoType** in the [Metrics reference](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#predicted-infotype).

### Find all tables that partially contain a given infoType
    
    
    tag:TAG_TEMPLATE_ID.other_info_types:INFOTYPE
    

Replace the following:

  * TAG_TEMPLATE_ID: `sensitive_data_profile` if the scan configuration is for an organization or a folder; `sensitive_data_profile_project` if the scan configuration is for a project. 
  * INFOTYPE: the infoType—for example, `PERSON_NAME`.



For a list of all built-in infoTypes, see [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

For more information, see **Other infoTypes** in the [Metrics reference](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#other-infoTypes).

### Find all tables that contain a given column with a given predicted infoType
    
    
    tag:TAG_TEMPLATE_ID.column_insights:COLUMN_NAME:INFOTYPE
    

Replace the following:

  * TAG_TEMPLATE_ID: `sensitive_data_profile` if the scan configuration is for an organization or a folder; `sensitive_data_profile_project` if the scan configuration is for a project. 
  * COLUMN_NAME: the name of the column in the BigQuery table.
  * INFOTYPE: the infoType—for example, `PERSON_NAME`.



For a list of all built-in infoTypes, see [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

For more information, see **Predicted infoType** in the [Metrics reference](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#predicted-infotype).

### Find all tables that contain a given column with a given column-level sensitivity score
    
    
    tag:TAG_TEMPLATE_ID.column_sensitivity:COLUMN_NAME:SENSITIVITY_SCORE
    

Replace the following:

  * TAG_TEMPLATE_ID: `sensitive_data_profile` if the scan configuration is for an organization or a folder; `sensitive_data_profile_project` if the scan configuration is for a project. 
  * COLUMN_NAME: the name of the column in the BigQuery table.
  * SENSITIVITY_SCORE: one of `HIGH`, `MODERATE`, or `LOW`.



For more information, see [Data risk and sensitivity levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

## Truncated tag values

If the column heading data of a BigQuery table exceeds 10 MB, the resulting tag might show `[TRUNCATED]` in the `Column Insights` or `Column Sensitivity` field. In this case, we recommend that you go to Sensitive Data Protection to [review the table data profile](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-data-profiles#view_the_data_profiles) and associated column data profiles.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
