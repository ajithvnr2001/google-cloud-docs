---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects/
title: Add Knowledge Catalog aspects based on insights from data profiles \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:35.793334+00:00
---

# Add Knowledge Catalog aspects based on insights from data profiles  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Add Knowledge Catalog aspects based on insights from data profiles Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to automatically add Knowledge Catalog aspects to your data after Sensitive Data Protection profiles your resources. This page also provides example queries that you can use to find data across your organization and projects with specific aspect values.

This feature is useful if you want to enrich your metadata in Knowledge Catalog with insights gathered from Sensitive Data Protection data profiles. The generated aspects include the following insights:

  * Calculated sensitivity level of the table or dataset
  * Calculated data risk level of the table or dataset
  * Information types ([_infoTypes_](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference)) that were detected in the table or dataset



Insights from Sensitive Data Protection data profiles can help you use Knowledge Catalog to discover sensitive and high-risk data in your organization. Use these insights to help you make informed decisions about how to manage and govern your data.

## About data profiles

You can configure Sensitive Data Protection to automatically generate profiles about data across an organization, folder, or project. [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) contain metrics and metadata about your data and help you determine where [sensitive and high-risk data](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation) reside. Sensitive Data Protection reports these metrics at various levels of detail.

You can send data profiles to other Google Cloud services like Knowledge Catalog, [Pub/Sub](https://docs.cloud.google.com/sensitive-data-protection/docs/dp-receive-pubsub-messages), [Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc), and [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/detection/usecase-dlp-high-risk-user-download) to enrich your data governance, alerting, and security workflows.

## About Knowledge Catalog

[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview) provides a unified inventory of Google Cloud resources.

Knowledge Catalog lets you use _aspects_ to add business and technical metadata to your data to capture context and knowledge about your resources. You can then search and discover data across your organization and enable data governance over your data assets. For more information, see [Aspects](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata#aspects).

## Supported resources

Sensitive Data Protection can automatically attach aspects to Knowledge Catalog entries for the following resources:

  * BigQuery tables
  * Cloud SQL tables

**Note:** You must [enable the integration of Knowledge Catalog on your Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration#enable-dataplex-catalog) for this feature to work.
  * Vertex AI datasets created from BigQuery tables




Knowledge Catalog doesn't ingest Cloud Storage buckets and so this this feature is unavailable when you profile Cloud Storage data.

## How it works

The high-level workflow for automatically creating Knowledge Catalog aspects based on data profiles is as follows:

  1. [Create](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#create) or [edit](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#edit-config) a scan configuration for a supported resource type.

  2. In the **Add actions** step, make sure that the **Send to Dataplex Catalog as aspects** action is enabled.

If you're creating a scan configuration, this action is enabled by default.

If you're editing a scan configuration, then enable this action.




Sensitive Data Protection adds or updates the `Sensitive Data Protection profile` aspect of the [Knowledge Catalog entry](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources#entries) for each supported resource that you profile. You can then search Knowledge Catalog for all data in your organization or project with specific aspect values.

When you enable the **Send to Dataplex Catalog as aspects** action, Sensitive Data Protection applies this action to new and updated profiles only. Existing profiles that aren't updated aren't sent to Knowledge Catalog.

### Top-level fields

The resulting aspect for a profiled table can have the following top-level fields:

Display name | Example value | Description  
---|---|---  
`Sensitivity` | `MODERATE` | The [calculated sensitivity level](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#sensitivity-level) of the table  
`Risk` | `MODERATE` | The [calculated data risk level](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#data-risk) of the table  
`InfoTypes` | 

  * `infoType`: `CREDIT_CARD_NUMBER`
  * `infoType`: `PHONE_NUMBER`
  * `infoType`: `US_SOCIAL_SECURITY_NUMBER`

| A list of all infoTypes found in the table, including [predicted infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#predicted-infotype) and [other infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#other-infoTypes). This field is included if at least one infoType was detected in the table.  
`Column InfoTypes` | 

  * `infoType`: `CREDIT_CARD_NUMBER`
  * `infoType`: `PHONE_NUMBER`

| A list of all [predicted infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#predicted-infotype) found in all columns of the table. This field is included if at least one predicted infoType was detected in the table.  
`Project Profile` | See Project Profile and Organization Profile on this page.  | Included if the resource was profiled through a project-level scan configuration.  
`Organization Profile` | See Project Profile and Organization Profile on this page.  | Included if the resource was profiled through a organization-level or folder-level scan configuration.  
  
If the resource was profiled at both the project level and the organization or folder level, then Sensitive Data Protection aggregates the values of both profiles. The aspect provides a union of the infoTypes detected and uses the highest sensitivity and data risk ratings from both profiles.

For example, suppose that the project-level profile rates the sensitivity of the resource as `MODERATE` and the organization-level profile rates the sensitivity as `LOW`. In this case, the value in the top-level `Sensitivity` field of the aspect is `MODERATE`.

### Project Profile and Organization Profile fields

The resulting `Sensitive Data Protection profile` aspect includes one or both of the following top-level fields, depending on the level at which the resource was profiled:

`Project Profile`
    Included in the aspect if the resource was profiled through a project-level scan configuration
`Organization Profile`
    Included in the aspect if the resource was profiled through an organization-level or folder-level scan configuration

If the resource was profiled at both the project level and the organization or folder level, then the resulting aspect has both the `Project Profile` and `Organization Profile` fields.

Each `Project Profile` or `Organization Profile` field contains nested `Sensitivity` and `Risk` fields with the values that are listed in the data profile. If the data profile has predicted infoTypes and other infoTypes listed, then those are also available as nested `Column InfoTypes` and `InfoTypes` fields. In addition, each `Project Profile` or `Organization Profile` field contains the following nested fields:

`Profile`
    

The full resource name of the data profile. Examples:

  * Project-level profile: `projects/PROJECT_ID/locations/LOCATION/tableDataProfiles/PROFILE_ID`
  * Organization-level or folder-level profile: `organizations/ORGANIZATION_ID/locations/LOCATION/tableDataProfiles/PROFILE_ID`


`Profile Link`
    

A link to the profile in the Google Cloud console. Examples:

  * Project-level profile: `https://console.cloud.google.com/security/sensitive-data-protection/projects/PROJECT_ID/locations/LOCATION/tableDataProfiles/PROFILE_ID`
  * Organization-level or folder-level profile: `https://console.cloud.google.com/security/sensitive-data-protection/organizations/ORGANIZATION_ID/locations/LOCATION/tableDataProfiles/PROFILE_ID`



## Enable the Dataplex API

The Dataplex API must be enabled in each project that contains data that you want to add aspects for. This section describes how to enable the Dataplex API in a single project or in all projects in an organization or folder.

### Enable the Dataplex API in a single project

  1. Select the project in which you want to enable the Dataplex API.

[Go to project selector](https://console.cloud.google.com/projectselector2)

  2. Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)




### Enable the Dataplex API in all projects in an organization or folder

This section provides a script that searches for all projects in an organization or folder and enables the Dataplex API in each of those projects.

To get the permissions that you need to enable the Dataplex API in all projects in an organization or folder, ask your administrator to grant you the following IAM roles: 

  * [Cloud Asset Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.viewer) (`roles/cloudasset.viewer`) on the organization or folder
  * [DLP User ](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.user) (`roles/dlp.user`) on each project in which you want to enable the Dataplex API



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to enable the Dataplex API in all projects in an organization or folder. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to enable the Dataplex API in all projects in an organization or folder:

  * To search for all projects in an organization or folder: `cloudasset.assets.searchAllResources` on the organization or folder 
  * To enable the Dataplex API: `serviceusage.services.use` on each project in which you want to enable the Dataplex API 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To enable the Dataplex API in all projects in an organization or folder, follow these steps:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the following script:
         
         #!/bin/bash
         
         RESOURCE_ID="RESOURCE_ID"
         
         gcloud asset search-all-resources \
             --scope="RESOURCE_TYPE/$RESOURCE_ID" \
             --asset-types="cloudresourcemanager.googleapis.com/Project" \
             --format="value(name)" |
             while read project_name; do
               project_id=$(echo "$project_name" | sed 's|.*/||')
               gcloud services enable "dataplex.googleapis.com" --project="$project_id"
             done
         

Replace the following:

     * `RESOURCE_ID`: the organization number or folder number of the resource that contains the projects
     * `RESOURCE_TYPE`: the type of the resource that contains the projects—`organizations` or `folders`



## Roles and permissions for viewing aspects

To get the permissions that you need to search for aspects associated with your resources, ask your administrator to grant you the following IAM roles on the resources: 

  * [Dataplex Catalog Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)
  * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)
  * [Vertex AI Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.viewer) (`roles/aiplatform.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to search for aspects associated with your resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to search for aspects associated with your resources:

  * View Knowledge Catalog entries: 
    * `dataplex.entries.list`
    * `dataplex.entries.get`
  * View BigQuery datasets and tables: 
    * `bigquery.datasets.get`
    * `bigquery.tables.get`
  * View Vertex AI datasets: `aiplatform.datasets.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information on permissions required to use Knowledge Catalog, see [Knowledge Catalog IAM permissions](https://docs.cloud.google.com/dataplex/docs/iam-permissions).

## Find the generated aspect for a given table data profile

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Select your organization or project.

  3. For **Choose search platform** , select **Knowledge Catalog** as the search mode.

  4. In the **Search** field, enter the following:
         
         name:TABLE_ID
         

Replace `TABLE_ID` with the ID of the table that was profiled.

  5. In the list that appears, click the table name. The details of the BigQuery table appear. Any `Sensitive Data Protection profile` aspects associated with it are shown in the **Optional aspects** section.




For more information about how to search for resources, see [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets).

## Example search queries

This section provides example search queries that you can use in Knowledge Catalog to find data in your organization or project with specific aspect values.

You can find only the data that you have access to. Data access is controlled through IAM permissions. For more information, see Roles and permissions for viewing aspects on this page.

You can enter these example queries in the **Search** field on the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

For information about how to form the queries, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax).

### Find all resources that have the Sensitive Data Protection profile aspect
    
    
    aspect:sensitive-data-protection-profile
    

### Find all resources with a given sensitivity score
    
    
    aspect:sensitive-data-protection-profile.sensitivity=SENSITIVITY_SCORE
    

Replace `SENSITIVITY_SCORE` with `HIGH`, `MODERATE`, `UNKNOWN`, or `LOW`.

For more information, see [Sensitivity and data risk levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

### Find all resources with a given risk score
    
    
    aspect:sensitive-data-protection-profile.risk=DATA_RISK_LEVEL
    

Replace `DATA_RISK_LEVEL` with `HIGH`, `MODERATE`, `UNKNOWN`, or `LOW`.

For more information, see [Sensitivity and data risk levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

### Find all resources that have a project-level profile
    
    
    aspect:sensitive-data-protection-profile.projectProfile
    

### Find all resources that have an organization-level profile
    
    
    aspect:sensitive-data-protection-profile.organizationProfile
    

## Migrate to the Send to Dataplex Catalog as aspects action

To migrate a discovery configuration that is set to use the deprecated **Send to Dataplex as tags** action, follow these steps:

  1. [Edit the discovery configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#edit-config) that is configured to send discovery results to Data Catalog as tags.
  2. Enable **Send to Dataplex Catalog as aspects**.
  3. Click **Save**. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
