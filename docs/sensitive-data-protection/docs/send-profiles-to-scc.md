---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc/
title: Publish data profiles to Security Command Center \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:06.546563+00:00
---

# Publish data profiles to Security Command Center  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Publish data profiles to Security Command Center Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a high-level overview of the actions that you must take if you want data profiles to generate findings in [Security Command Center](https://docs.cloud.google.com/security-command-center/docs). This page also provides example queries that you can use to find the generated findings.

## About data profiles

You can configure Sensitive Data Protection to automatically generate profiles about data across an organization, folder, or project. [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) contain metrics and metadata about your data and help you determine where [sensitive and high-risk data](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation) reside. Sensitive Data Protection reports these metrics at various levels of detail. For information about the types of data you can profile, see [Supported resources](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#supported-resources). 

## Benefits of publishing data profiles to Security Command Center

This feature offers the following benefits in Security Command Center:

  * You can use Sensitive Data Protection findings to identify and remediate vulnerabilities and misconfigurations in your resources that can expose sensitive data to the public or to malicious actors.

  * You can use Sensitive Data Protection findings to add context to the triage process and prioritize threats that target resources containing sensitive data.

  * You can configure the [attack path simulation feature](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn) to automatically prioritize resources according to the sensitivity of the data that the resources contain. For more information, see [Set resource priority values automatically by data sensitivity](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity).




## Generated Security Command Center findings

When you configure the discovery service to publish data profiles to Security Command Center, each table data profile or file store data profile generates the following Security Command Center findings.

### Vulnerability findings from the discovery service

The Sensitive Data Protection discovery service helps you determine whether you are storing highly sensitive data that is not protected.

Category | Summary  
---|---  
  
#### `Public sensitive data`

Category name in the API: `PUBLIC_SENSITIVE_DATA` |  **Finding description** : The specified resource has [ high-sensitivity data](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#sensitivity-level) that can be accessed by anyone on the internet. **Note:** Sensitive Data Protection might produce a data access audit log entry when analyzing (_profiling_) a tuning job within a Cloud Storage bucket. The action is performed by an internal Sensitive Data Protection service account. **Supported assets** :

  * `aiplatform.googleapis.com/Dataset`
  * `aiplatform.googleapis.com/TuningJob`
  * `bigquery.googleapis.com/Dataset`
  * `bigquery.googleapis.com/Table`
  * `sqladmin.googleapis.com/Instance`
  * `storage.googleapis.com/Bucket`
  * Amazon S3 bucket
  * Azure Blob Storage container

**Remediation** : For Google Cloud data, remove `allUsers` and `allAuthenticatedUsers` from the data asset's IAM policy. For Amazon S3 data, configure block public access settings or update the object's ACL to deny public read access. For more information, see [ Configuring block public access settings for your S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-block-public-access-bucket.html) and [Configuring ACLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/managing-acls.html) in the AWS documentation. For Azure Blob Storage data, remove public access to the container and the blobs. For more information, see [Overview: Remediating anonymous read access for blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-overview) in the Azure documentation. **Compliance standards** : Not mapped  
  
#### `Secrets in environment variables`

Category name in the API: `SECRETS_IN_ENVIRONMENT_VARIABLES` |  **Finding description** : There are [ secrets](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets)—such as passwords, authentication tokens, and Google Cloud credentials—in environment variables. To enable this detector, see [ Report secrets in environment variables to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/secrets-discovery) in the Sensitive Data Protection documentation. **Supported assets** : 

  * [ `cloudfunctions.googleapis.com/CloudFunction` ](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions)
  * [ `run.googleapis.com/Revision` ](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services.revisions)

**Remediation** : For Cloud Run functions environment variables, remove the secret from the environment variable and [store it in Secret Manager](https://docs.cloud.google.com/functions/docs/configuring/secrets) instead. For Cloud Run service revision environment variables, move all traffic off of the revision, and then delete the revision. **Compliance standards** :

  * **CIS GCP Foundation 1.3** : 1.18
  * **CIS GCP Foundation 2.0** : 1.18

  
  
#### `Secrets in storage`

Category name in the API: `SECRETS_IN_STORAGE` |  **Finding description** : There are [ secrets](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets)—such as passwords, authentication tokens, and cloud credentials—in the specified resource. **Supported assets** :

  * `aiplatform.googleapis.com/Dataset`
  * `aiplatform.googleapis.com/TuningJob`
  * `bigquery.googleapis.com/Dataset`
  * `bigquery.googleapis.com/Table`
  * `sqladmin.googleapis.com/Instance`
  * `storage.googleapis.com/Bucket`
  * Amazon S3 bucket
  * Azure Blob Storage container

**Remediation** :

  1. For Google Cloud data, use Sensitive Data Protection to [ run a deep inspection scan of the specified resource](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage) to identify all affected resources. For Cloud SQL data, export that data to a CSV or AVRO file in a Cloud Storage bucket and run a deep inspection scan of the bucket. For data from other cloud providers, manually inspect the specified bucket or container.
  2. Remove the detected secrets.
  3. Consider resetting the credentials.
  4. For Google Cloud data, consider storing the detected secrets in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) instead. 

**Compliance standards** : Not mapped  
  
### Misconfiguration findings from the discovery service

The Sensitive Data Protection discovery service helps you determine whether you have misconfigurations that might expose sensitive data.

Category | Summary  
---|---  
  
#### `Sensitive data CMEK disabled`

Category name in the API: `SENSITIVE_DATA_CMEK_DISABLED` |  **Finding description** : The specified resource has [ high-sensitivity or moderate-sensitivity data](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#sensitivity-level) and the resource isn't using a customer-managed encryption key (CMEK). **Supported assets** :

  * `aiplatform.googleapis.com/Dataset`
  * `bigquery.googleapis.com/Dataset`
  * `bigquery.googleapis.com/Table`
  * `sqladmin.googleapis.com/Instance`
  * `storage.googleapis.com/Bucket`
  * Amazon S3 bucket
  * Azure Blob Storage container

**Remediation** :

  * For BigQuery data, [use CMEK on the table or dataset](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption).
  * For Cloud SQL data, see the CMEK documentation for [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/cmek) or [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/cmek).
  * For Cloud Storage data, [use CMEK on the bucket](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys).

**Compliance standards** : Not mapped  
  
### Observation findings from the discovery service

The Sensitive Data Protection discovery service helps you determine whether your data contains specific infoTypes and where they reside in your organization, folders, and projects. It generates the following observation finding categories in Security Command Center: 

Category | Summary  
---|---  
  
#### `Data sensitivity`

Category name in the API: `DATA_SENSITIVITY` |  **Finding description** : An indication of the sensitivity level of the data in a particular data asset. Data is sensitive if it contains PII or other elements that might require additional control or management. The severity of the finding is the [sensitivity level that Sensitive Data Protection calculated](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#sensitivity-level) when generating the data profile.  
  
#### `Data risk`

Category name in the API: `DATA_RISK` |  **Finding description** : The risk associated with the data in its current state. When calculating data risk, Sensitive Data Protection considers the sensitivity level of the data in the data asset and the presence of access controls to protect that data. The severity of the finding is the [data risk level that Sensitive Data Protection calculated](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#data-risk) when generating the data profile.  
  
## Finding generation latency

Depending on the size of your organization, Sensitive Data Protection findings can start appearing in Security Command Center within a few minutes after you enable sensitive data discovery. For larger organizations or organizations with specific configurations that affect finding generation, it can take up to 12 hours before initial findings appear in Security Command Center.

Subsequently, Sensitive Data Protection generates findings in Security Command Center within a few minutes after the discovery service scans your resources.

## Send data profiles to Security Command Center

The following is a high-level workflow for publishing data profiles to Security Command Center.

  1. [Check the activation type of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#check-scc-activation-level). You might have a default organization-level discovery subscription, [depending on your Security Command Center service tier](https://docs.cloud.google.com/sensitive-data-protection/pricing#discovery-scc).

  2. If Security Command Center isn't activated, then [activate it](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview).

  3. Confirm that Security Command Center is configured to accept findings from Sensitive Data Protection; that is, **Sensitive Data Protection** is enabled in Security Command Center as an integrated service. For more information, see [Add a Google Cloud integrated service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#gcp-configure-other-services) in the Security Command Center documentation.

  4. Enable discovery by creating a discovery scan configuration for each data source that you want to scan. In your scan configuration, make sure that you keep the **Publish to Security Command Center** option enabled.

If you have an existing discovery scan configuration that doesn't publish data profiles to Security Command Center, see Enable publishing to Security Command Center in an existing configuration on this page.




## Enable discovery with default settings in an organization

To enable discovery, you create a discovery configuration for each [data source](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#supported-resources) that you want to scan. You can [edit the configurations](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#edit-config) after creating them. To customize settings in the process of creating a configuration, see [Create a scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#create) instead.

To enable discovery with default settings at the organization level, follow these steps:

  1. In the Google Cloud console, go to the Sensitive Data Protection **Enable discovery** page.

[Go to Enable discovery](https://console.cloud.google.com/security/sensitive-data-protection;p=3/landing;source=CSCC_ONBOARDING_SUBTASK/dataProfiles/dashboard)

  2. Verify that you are viewing the organization that you activated Security Command Center on.

  3. In the **Enable discovery** pane, in the **Service agent container** field, set the project to be used as a [service agent container](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container). Within this project, the system creates a service agent and automatically grants the required discovery roles to it.

     * To automatically create a project to use as your service agent container, follow these steps:

       1. Click **Create**.
       2. Specify the name, billing account, and parent organization of the new project. Optionally, edit the project ID.
       3. Click **Create**.

It can take a few minutes for the roles to be granted to the new project's service agent.

     * To select a project that you previously used for discovery operations, click the **Service agent container** field and select the project.

  4. To review the default settings, click the expand_more expand icon.

  5. In the **Enable discovery** section, for each discovery type that you want to enable, click **Enable**. Enabling a discovery type does the following:

     * **BigQuery** : Creates a discovery configuration for profiling BigQuery tables across the organization. Sensitive Data Protection starts profiling your BigQuery data and sends the profiles to Security Command Center.
     * **Cloud SQL** : Creates a discovery configuration for profiling Cloud SQL tables across the organization. Sensitive Data Protection starts creating default connections for each of your Cloud SQL instances. This process can take a few hours. When the default connections are ready, you must give Sensitive Data Protection access to your Cloud SQL instances by updating each connection with the proper database user credentials.
     * **Secrets/credentials vulnerabilities** : Creates a discovery configuration for detecting and reporting unencrypted secrets in Cloud Run environment variables. Sensitive Data Protection starts scanning your environment variables.
     * **Cloud Storage** : Creates a discovery configuration for profiling Cloud Storage buckets across the organization. Sensitive Data Protection starts profiling your Cloud Storage data and sends the profiles to Security Command Center.
     * **Vertex AI datasets** : Creates a discovery configuration for profiling Vertex AI datasets across the organization. Sensitive Data Protection starts profiling your Vertex AI datasets and sends the profiles to Security Command Center.
     * **Amazon S3** : Creates a discovery configuration for profiling all Amazon S3 data that your AWS connector has access to.

**Note:** This feature requires Security Command Center Enterprise. You must first [create an AWS connector](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws) that has the AWS permissions needed for Sensitive Data Protection discovery.
     * **Azure Blob Storage** : Creates a discovery configuration for profiling all Azure Blob Storage data that your Azure connector has access to.

**Note:** This feature requires Security Command Center Enterprise. You must first [create an Azure connector](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure) that has the Azure permissions needed for Sensitive Data Protection discovery.
  6. To view the newly created discovery configurations, click **Go to discovery configuration**.

If you enabled Cloud SQL discovery, the discovery configuration is created in paused mode with errors indicating the absence of credentials. See [Manage connections for use with discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-connections) to grant the required IAM roles to your service agent and to provide database user credentials for each Cloud SQL instance.

  7. Close the pane.




## Enable publishing to Security Command Center in an existing configuration

If you have an existing discovery scan configuration that is not set to publish discovery results to Security Command Center, follow these steps:

  1. [Open the scan configuration for editing](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#edit-config).

  2. In the **Actions** section, enable **Publish to Security Command Center**.

  3. Click **Save**.




## Query for Security Command Center findings related to data profiles

The following are example queries that you can use to find relevant `Data sensitivity` and `Data risk` findings in Security Command Center. You can enter these queries in the **Query editor** field. For more information about the query editor, see [Edit a findings query in the Security Command Center dashboard](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console).

### List all `Data sensitivity` and `Data risk` findings for a particular BigQuery table

This query is useful, for example, if Security Command Center detects an event where a BigQuery table was saved to a different project. In this case, an [`Exfiltration: BigQuery Data Exfiltration`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/big-query-exfil) finding is generated, and it contains the full display name of the table that was exfiltrated. You can search for any `Data sensitivity` and `Data risk` findings related to the table. View the calculated sensitivity and data risk levels for the table and plan your response accordingly.
    
    
    state="ACTIVE"
    AND NOT mute="MUTED"
    AND category="DATA_RISK" OR category="DATA_SENSITIVITY"
    AND resource.display_name="PROJECT_ID:DATASET_ID.TABLE_ID"
    

Replace the following:

  * PROJECT_ID: the ID of the project that contains the BigQuery table
  * DATASET_ID: the dataset ID of the table
  * TABLE_ID: the ID of the table



### List all `Data sensitivity` and `Data risk` findings for a particular Cloud SQL instance

This query is useful, for example, if Security Command Center detects an event where live Cloud SQL instance data was exported to a Cloud Storage bucket outside of the organization. In this case, an [`Exfiltration: Cloud SQL Data Exfiltration`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloudsql-exfil-export) finding is generated, and it contains the full resource name of the instance that was exfiltrated. You can search for any `Data sensitivity` and `Data risk` findings related to the instance. View the calculated sensitivity and data risk levels for the instance and plan your response accordingly.
    
    
    state="ACTIVE"
    AND NOT mute="MUTED"
    AND category="DATA_RISK" OR category="DATA_SENSITIVITY"
    AND resource.name:"INSTANCE_NAME"
    

Replace the following:

  * INSTANCE_NAME: a portion of the name of the Cloud SQL instance



### List all `Data risk` and `Data sensitivity` findings with a `High` severity level
    
    
    state="ACTIVE"
    AND NOT mute="MUTED"
    AND category="DATA_RISK" OR category="DATA_SENSITIVITY"
    AND severity="HIGH"
    

## What's next

  * Learn about how to [Set resource priority values automatically by data sensitivity](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity) in Security Command Center.
  * Learn how to [report the presence of secrets in environment variables to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/secrets-discovery). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
