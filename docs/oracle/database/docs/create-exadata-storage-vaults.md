---
url: https://docs.cloud.google.com/oracle/database/docs/create-exadata-storage-vaults/
title: Create an Exascale Storage Vault for an Exadata Infrastructure \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:05.419432+00:00
---

# Create an Exascale Storage Vault for an Exadata Infrastructure  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/create-exadata-storage-vaults/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Create an Exascale Storage Vault for an Exadata Infrastructure Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create an Exascale Storage Vault in Google Cloud for Exadata Database Service on dedicated infrastructure.

For Exadata Infrastructures, Oracle Database@Google Cloud lets you create and use Exascale Storage Vaults for your Exadata VM Clusters.

Exascale Storage Vault with Exadata Database Service on dedicated infrastructure introduces a next-generation intelligent data architecture for the cloud, combining the strengths of Exadata with the agility of the cloud. Exascale reimagines how compute and storage resources are managed on Exadata platforms by decoupling and simplifying storage management, paving the way for innovative capabilities.

Exascale Storage Vaults let administrators create pools of storage within a single Exadata Infrastructure that can be shared across multiple Exadata VM Clusters. Databases that reside within a storage vault can be cloned across clusters or container databases using a redirect-on-write technique to maximize storage efficiency and minimize the time required to complete a clone operation.

## Before you begin

  * Confirm that you have the required Identity and Access Management (IAM) roles and permissions to create an Exascale Storage Vault:

    * `roles/oracledatabase.exascaleDbStorageVaultAdmin`
    * `roles/oracledatabase.cloudExadataInfrastructureUser`

For information on how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## Create an Exascale Storage Vault

You must create the Exascale Storage Vault in the same project as that of the Exadata Infrastructure.

### gcloud

To create an Exascale Storage Vault, use the `gcloud oracle-database exascale-db-storage-vaults create` command.
    
    
    gcloud oracle-database exascale-db-storage-vaults create VAULT_ID \
    --project=PROJECT_ID \
    --location=REGION \
    --display-name="VAULT_DISPLAY_NAME" \
    --exascale-db-storage-details-total-size-gbs=VAULT_SIZE \
    --exadata-infrastructure=projects/PROJECT_ID/locations/REGION/cloudExadataInfrastructures/EXADATA_INSTANCE_ID \
    --async
    

Replace the following:

  * VAULT_ID: a unique ID for your vault.
  * PROJECT_ID: the ID of your Google Cloud project in which to create the vault.
  * REGION: the region in which to create the vault.
  * VAULT_DISPLAY_NAME: a name for your vault that appears in the Google Cloud console.
  * VAULT_SIZE: the storage capacity of your vault. It can range from 300 GiB to 100000 GiB.

**Note:** The storage capacity for the vault must match or exceed the total storage capacity across the Exadata VM Cluster.
  * For the `--exadata-infrastructure` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains the Exadata Infrastructure.
    * REGION: the region where the Exadata Infrastructure is located.
    * EXADATA_INSTANCE_ID: the ID of the Exadata Infrastructure.



###  API 

To create an Exascale Storage Vault, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exascaleDbStorageVaults/VAULT_ID"
    -d \
    '{
      "display_name": "VAULT_DISPLAY_NAME",
      "gcp_oracle_zone": "GCP_ORACLE_ZONE",
      "name": "projects/PROJECT_ID/locations/REGION/exascaleDbStorageVaults/VAULT_NAME",
      "exadata_infrastructure": "projects/PROJECT_ID/locations/REGION/cloudExadataInfrastructures/EXADATA_INSTANCE_ID"
      "properties": {
        "exascale_db_storage_details": {
          "total_size_gbs": "VAULT_SIZE"
        }
      }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project in which to create the vault.
  * REGION: the region in which to create the vault.
  * VAULT_ID: a unique ID for your vault.
  * VAULT_DISPLAY_NAME: a name for your vault that appears in the Google Cloud console.
  * GCP_ORACLE_ZONE: the GCP Oracle zone for your vault. For the list of available regions and zones, see [Supported regions and zones](https://docs.cloud.google.com/oracle/database/docs/regions-and-zones).
  * VAULT_NAME: a name for your vault.
  * For `exadata_infrastructure` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project which contains the Exadata Infrastructure.
    * REGION: the region where the Exadata Infrastructure is located.
    * EXADATA_INSTANCE_ID: the ID of the Exadata Infrastructure.
  * VAULT_SIZE: the storage capacity of your vault. It can range from 300 GiB to 100000 GiB.

**Note:** The storage capacity for the vault must match or exceed the total storage capacity across the Exadata VM Cluster.



After the Exascale Storage Vault is created, you must configure it for using with your Exadata Infrastructure. For more information, see [Configure Exascale Storage Vault for Exadata Infrastructure](https://docs.cloud.google.com/oracle/database/docs/configure-exascale-storage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
