---
url: https://docs.cloud.google.com/kms/docs/view-key-usage/
title: View key usage \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:35.948553+00:00
---

# View key usage  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/view-key-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  View key usage Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to view the Google Cloud resources within your organization that are protected by your Cloud KMS keys. Key usage tracking is available within organization resources for organizations that use a centralized key management model. If you use a delegated key management model, you can see key usage tracking data scoped to the selected project.

You can view information about the resources that your keys protect at two levels: 

  * **Key usage summary** : Includes the number of protected resources, projects, and unique Google Cloud products that use each key. This level of detail is available to anyone with the **Cloud KMS Viewer** role on the key. The scope of the key usage summary data that you can see depends on your key management model. 
    * **Centralized key management** : If the Cloud KMS service account has the **Cloud KMS Organization Service Agent** role on the organization, then you can see key usage summary data for resources protected by the key even for resources in other projects within the organization.
    * **Delegated key management** : If the Cloud KMS service account doesn't have the **Cloud KMS Organization Service Agent** role on the organization, then you can see key usage summary data for resources in the same project only. If you are viewing only same-project key usage data, the **Usage tracking** dashboard displays a notice that tells you that the scope of the displayed data is limited to the selected project.
  * **Key usage detail** : Lists the resources that are protected by and depend on this key. The scope of the key usage details that you can see depends on your key management model. 
    * **Centralized key management** : If you have the **Cloud KMS Protected Resources Viewer** role on the organization and the Cloud KMS service account has the **Cloud KMS Organization Service Agent** role on the organization, you can see key usage details for resources protected by the key even for resources that are located in other projects.
    * **Delegated key management** : If you have the **Cloud KMS Protected Resources Viewer** role on the project, but not on the organization, you can see key usage details for resources in the same project only. If your permissions limit you to viewing same-project resources, the **Usage tracking** dashboard displays a notice indicating the limited scope of the data.

**Note:** The key usage information described on this page is subject to limitations. Before making any changes based on key usage information, review the Limitations section on this page.

## Before you begin

  * Enable the Cloud KMS Inventory API on the project that you want to view key usage data for. 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=kmsinventory.googleapis.com)




### Required roles

If you use Cloud KMS with a centralized key management model, you need to grant the required permissions to the Cloud KMS service account.

For both centralized key management and delegated key management, user accounts that need to view key usage data must be granted the required permissions.

#### Cloud KMS service account role

If you use a delegated key management model and don't need to see key usage data aggregated across your organization, skip to the User account roles section of this page.

To ensure that your Cloud KMS service account has the necessary permissions to enable key usage tracking at the organization level, ask your administrator to grant your Cloud KMS service account the **Cloud KMS Organization Service Agent** ([`roles/cloudkms.orgServiceAgent`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.orgServiceAgent)) IAM role on your organization.

**Important:** You must grant this role to the Cloud KMS service account, not to your user account. Failure to grant the roles to the correct principal might result in permission errors.

#### User account roles

The **Usage tracking** dashboard displays different information depending on whether your user account has the required roles on the project or on the parent organization. If your organization uses a centralized key management model, grant the following roles on the organization. If your organization uses a delegated key management model, you can grant the required roles on the project to view key usage details scoped to the selected project.

To get the permissions that you need to view key usage information, ask your administrator to grant you the following IAM roles: 

  * To view key usage summaries: [Cloud KMS Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.viewer) (`roles/cloudkms.viewer`) on the key 
  * To view key usage details: [Cloud KMS Protected Resources Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.protectedResourcesViewer) (`roles/cloudkms.protectedResourcesViewer`) on the project or organization 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View key usage information

###  Console 

  1. In the Google Cloud console, go to the **Key inventory** page.

[Go to Key inventory](https://console.cloud.google.com/security/kms/keys)

  2. Optional: To filter the list of keys, enter your search terms in the filter_list **Filter** box and then press enter. For example, you can filter by location, key ring, status, or other properties of the keys.

  3. Click the name of the key for which you want to view usage information.

  4. Click the **Usage tracking** tab.

  5. Optional: To filter the list of protected resources, enter your search terms in the filter_list **Filter** box and then press Enter.




Key usage summary and details are shown for the selected key. If you and the Cloud KMS service account have the required roles at the organization level, you can see key usage details for all resources in the organization that are protected by keys in the selected project. If you have the required roles only at the project level, or if the Cloud KMS service account doesn't have the required role on the organization, then you can see key usage details for all resources in the selected project that are protected by keys in the same project. If you're viewing same-project details, a notice displays on the **Usage tracking** tab that tells you the scope of the displayed data.

###  gcloud 

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

To view the key usage summary, use the [`get-protected-resources-summary`](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.locations.keyRings.cryptoKeys/getProtectedResourcesSummary) method:
    
    
    gcloud kms inventory get-protected-resources-summary \
        --keyname projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME \
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `KEY_NAME`: the name of the key for which you want to view the usage summary.



To view key usage details, use the [`search-protected-resources`](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/organizations.protectedResources/search) method:
    
    
    gcloud kms inventory search-protected-resources \
        --keyname projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME \
        --scope=organizations/ORGANIZATION_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `KEY_NAME`: the name of the key for which you want to view usage details.
  * `ORGANIZATION_ID`: the numerical ID of your organization.



By default, this method returns key usage details for all resources in your organization that are protected by the indicated key. If you have the **Cloud KMS Protected Resources Viewer** role at the project level but not at the organization level, or if the Cloud KMS service account doesn't have the required role on the organization, then the output indicates that the data returned is scoped to the selected project.

###  REST 

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To view the key usage summary, use the [`cryptoKeys.getProtectedResourcesSummary`](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.locations.keyRings.cryptoKeys/getProtectedResourcesSummary) method:
    
    
    curl "https://kmsinventory.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/protectedResourcesSummary"
        --request "GET" \
        --header "x-goog-user-project: CALLING_PROJECT_ID"
        --header "Content-Type: application/json" \
        --header "Authorization: Bearer TOKEN"

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `KEY_NAME`: the name of the key for which you want to view the usage summary.
  * `CALLING_PROJECT_ID`: the ID of the project from which you are calling the Cloud KMS Inventory API.



To view key usage details, use the [`protectedResources.search`](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/organizations.protectedResources/search) method:
    
    
    curl "https://kmsinventory.googleapis.com/v1/organizations/ORGANIZATION_ID/protectedResources:search?crypto_key=projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME"
        --request "GET" \
        --header "x-goog-user-project: CALLING_PROJECT_ID"
        --header "Content-Type: application/json" \
        --header "Authorization: Bearer TOKEN"

Replace the following:

  * `ORGANIZATION_ID`: the numerical ID of your organization.
  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `KEY_NAME`: the name of the key for which you want to view usage details.
  * `CALLING_PROJECT_ID`: the ID of the project from which you are calling the Cloud KMS Inventory API.



By default, this method returns key usage details for all resources in your organization that are protected by the indicated key. If you have the **Cloud KMS Protected Resources Viewer** role at the project level but not at the organization level, or if the Cloud KMS service account doesn't have the required role on the organization, then the output indicates that the data returned is scoped to the selected project.

**Note:** This functionality isn't available in client libraries.

**Note:** Key usage is shown only for the resource types listed in the Limitations section on this page.

### Key usage details

Usage details about the protected resources that are encrypted with the selected key include the following:

  * **Name** : The name of the Google Cloud resource protected by the selected key.
  * **Project** : The name of the project that contains the protected resource.
  * **Crypto key version** : The key version used to encrypt this resource. Some protected resource types don't report the crypto key version.
  * **Cloud product** : The Google Cloud product associated with this resource.
  * **Resource type** : The type of resource protected, for example Bucket (Cloud Storage) or Disk (Compute Engine).
  * **Location** : The Google Cloud region associated with the resource.
  * **Creation date** : The time at which the resource was created.
  * **Labels** : A set of key-value pairs associated with the resource.



## List key versions that protect a resource

If a resource is protected by several key versions, you might not be able to see the full list of key versions in the **Usage tracking** tab.

To list the key versions that protect a resource, use the gcloud CLI to run the following command:
    
    
    gcloud kms inventory search-protected-resources \
      --keyname=KEY_NAME \
      --scope=organizations/ORGANIZATION_ID \
      --filter="name:RESOURCE_NAME" \
      --flatten="cryptoKeyVersions" \
      --format="value(cryptoKeyVersions)"
    

Replace the following:

  * `KEY_NAME`: the name of the key for which you want to list key versions.
  * `ORGANIZATION_ID`: the numerical ID of your organization.
  * `RESOURCE_NAME`: the name of the resource for which you want to list key versions.



### Filter by resource type

You can filter the search results by resource type. For example, you can choose to list only Cloud Storage buckets or only Compute Engine disks. You can specify resource types by name, or use regular expressions to match multiple resource types.

For a list of supported resource types, see Tracked resource types.

###  gcloud 

To filter by resource type, use the `gcloud kms inventory search-protected-resources` command with the `--resource-types` flag:
    
    
    gcloud kms inventory search-protected-resources \
        --keyname=projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME \
        --scope=organizations/ORGANIZATION_ID \
        --resource-types=RESOURCE_TYPES
    

Replace the following:

  * `KEY_NAME`: the name of the key that you want to view usage details for.
  * `ORGANIZATION_ID`: the numerical ID of your organization.
  * `RESOURCE_TYPES`: a comma-separated list of resource types to filter by—for example, `storage.googleapis.com/Bucket` or `storage.googleapis.com/Bucket,compute.googleapis.com/Disk`. You can use regular expressions to match resource types by pattern. For example, `compute.googleapis.com/.*` matches any resource type that begins with `compute.googleapis.com/`.



###  REST 

To filter by resource type, use the `resourceTypes` query parameter.
    
    
    curl "https://kmsinventory.googleapis.com/v1/organizations/ORGANIZATION_ID/protectedResources:search?crypto_key=projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME&resourceTypes=RESOURCE_TYPE" \
        --request "GET" \
        --header "x-goog-user-project: CALLING_PROJECT_ID" \
        --header "Content-Type: application/json" \
        --header "Authorization: Bearer TOKEN"

Replace the following:

  * `ORGANIZATION_ID`: the numerical ID of your organization.
  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `KEY_NAME`: the name of the key that you want to view usage details for.
  * `CALLING_PROJECT_ID`: the ID of the project that you're calling the Cloud KMS Inventory API from.
  * `RESOURCE_TYPE`: the resource type to filter by—for example, `storage.googleapis.com/Bucket`. To filter by more than one resource type, use multiple `resourceTypes` query parameters. You can use regular expressions to match resource types by pattern. For example, `compute.googleapis.com/.*` matches any resource type that begins with `compute.googleapis.com/`.



## Limitations

When using key usage tracking, note the following:

  * Key usage tracking is only available for CMEK key usage. If you're using a key version in your applications inside or outside of Google Cloud, that usage isn't included in the **Usage tracking** tab.
  * By default, key usage tracking information is provided at the organization level, for all trackable resources in the organization that are protected by the selected key. However, if you have the **Cloud KMS Protected Resources Viewer** on the project but not on the organization, key usage tracking is provided at the project level for resources in the selected project that are protected by the selected key. When key usage tracking data is given at the project level, the output indicates that the data is scoped to the selected project.
  * Key usage tracking information can only be shown at the organization level if the Cloud KMS service account has the required **Cloud KMS Organization Service Agent** role on the organization. If the service account doesn't have the required role, key usage data is scoped to the selected project instead.
  * Some CMEK resources aren't tracked. For resource types that aren't listed in Tracked resource types, key usage information might not be included in the key usage details. For example, key usage by Datastream to encrypt `ConnectionProfile` (`datastream.googleapis.com/ConnectionProfile`) resources isn't shown on the **Usage tracking** tab.
  * Data might be delayed. For example, if you create a new protected resource, the protected resource and associated key version aren't immediately added to the **Usage tracking** tab.
  * Cloud Storage key usage data is subject to the following additional limitations: 
    * Key usage data is aggregated from objects to buckets. Object names aren't shown. A bucket will be shown as using a key if the bucket has at least one object using that key.
    * Key usage tracking might not be complete for buckets that contain objects protected with over 4000 unique key versions.
  * Key usage tracking details are for informational purposes only. Conduct your own due diligence using other sources before making changes that could result in outages or loss of data. Don't disable or destroy key versions based only on key usage tracking information.



### Tracked resource types

The following resource types are supported:

Service | Resource  
---|---  
Agent Search | `discoveryengine.googleapis.com/DataStore`  
AlloyDB for PostgreSQL | `alloydb.googleapis.com/Backup`  
AlloyDB for PostgreSQL | `alloydb.googleapis.com/Cluster`  
Apigee | `apigee.googleapis.com/Organization`  
Apigee | `apigee.googleapis.com/Instance`  
Apigee API hub | `apihub.googleapis.com/ApiHubInstance`  
Artifact Registry | `artifactregistry.googleapis.com/Repository`  
Backup and DR Service | `backupdr.googleapis.com/BackupVault`  
Backup and DR Service | `backupdr.googleapis.com/Backup`  
BigQuery | `bigquery.googleapis.com/Dataset`  
BigQuery | `bigquery.googleapis.com/Model`  
BigQuery | `bigquery.googleapis.com/Table`  
BigQuery | `bigquerydatatransfer.googleapis.com/TransferConfig`  
Bigtable | `bigtableadmin.googleapis.com/Backup`  
Bigtable | `bigtableadmin.googleapis.com/Cluster`  
Bigtable | `bigtableadmin.googleapis.com/Table`  
Cloud Data Fusion | `datafusion.googleapis.com/Instance`  
Cloud Healthcare API | `healthcare.googleapis.com/Dataset`  
Cloud Logging | `logging.googleapis.com/LogBucket`  
Cloud Run | `run.googleapis.com/Revision`  
Cloud Run functions | `cloudfunctions.googleapis.com/CloudFunction`  
Cloud Run functions | `cloudfunctions.googleapis.com/Function`  
Cloud SQL | `sqladmin.googleapis.com/BackupRun`  
Cloud SQL | `sqladmin.googleapis.com/Instance`  
Cloud Storage | `storage.googleapis.com/Bucket`  
Cloud Workstations | `workstations.googleapis.com/Workstation`  
Cloud Workstations | `workstations.googleapis.com/WorkstationConfig`  
Compute Engine | `compute.googleapis.com/Disk`  
Compute Engine | `compute.googleapis.com/Image`  
Compute Engine | `compute.googleapis.com/MachineImage`  
Compute Engine | `compute.googleapis.com/Snapshot`  
Database Migration Service | `datamigration.googleapis.com/MigrationJob`  
Database Migration Service | `datamigration.googleapis.com/ConnectionProfile`  
Dataflow | `dataflow.googleapis.com/Job`  
Dataproc Metastore | `metastore.googleapis.com/Service`  
Datastream | `datastream.googleapis.com/Stream`  
Document AI | `documentai.googleapis.com/HumanReviewConfig`  
Document AI | `documentai.googleapis.com/Processor`  
Document AI | `documentai.googleapis.com/ProcessorVersion`  
Filestore | `file.googleapis.com/Instance`  
Filestore | `file.googleapis.com/Backup`  
Firestore | `firestore.googleapis.com/Database`  
Firestore | `datastore.googleapis.com/Database`  
Gemini Enterprise | `discoveryengine.googleapis.com/DataStore`  
Google Cloud Managed Lustre | `lustre.googleapis.com/Instance`  
Google Cloud Observability | `observability.googleapis.com/Bucket`  
Google Kubernetes Engine | `container.googleapis.com/Cluster`  
Looker (Google Cloud core) | `looker.googleapis.com/Instance`  
Managed Service for Apache Airflow | `composer.googleapis.com/Environment`  
Managed Service for Apache Spark | `dataproc.googleapis.com/Cluster`  
Managed Service for Apache Spark | `dataproc.googleapis.com/Batch`  
Memorystore for Redis | `redis.googleapis.com/Instance`  
Migrate to Virtual Machines | `vmmigration.googleapis.com/Source`  
Pub/Sub | `pubsub.googleapis.com/Topic`  
Secret Manager | `secretmanager.googleapis.com/Secret`  
Secret Manager | `secretmanager.googleapis.com/SecretVersion`  
Secure Source Manager | `securesourcemanager.googleapis.com/Instance`  
Spanner | `spanner.googleapis.com/Database`  
Vertex AI | `aiplatform.googleapis.com/Dataset`  
Vertex AI | `aiplatform.googleapis.com/Featurestore`  
Vertex AI | `aiplatform.googleapis.com/Tensorboard`  
Vertex AI | `aiplatform.googleapis.com/BatchPredictionJob`  
Vertex AI | `aiplatform.googleapis.com/CustomJob`  
Vertex AI | `aiplatform.googleapis.com/Endpoint`  
Vertex AI | `aiplatform.googleapis.com/Model`  
Vertex AI | `aiplatform.googleapis.com/TrainingPipeline`  
Vertex AI | `aiplatform.googleapis.com/PipelineJob`  
Vertex AI | `aiplatform.googleapis.com/MetadataStore`  
Vertex AI Workbench instances | `notebooks.googleapis.com/Instance`  
Workflows | `workflows.googleapis.com/Workflow`  



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
