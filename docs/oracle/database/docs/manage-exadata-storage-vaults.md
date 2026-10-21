---
url: https://docs.cloud.google.com/oracle/database/docs/manage-exadata-storage-vaults/
title: Manage Exascale Storage Vaults \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:22:13.437738+00:00
---

# Manage Exascale Storage Vaults  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/manage-exadata-storage-vaults/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Manage Exascale Storage Vaults Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view, list, and delete Exascale Storage Vaults Exascale Storage Vaults on dedicated infrastructure in Google Cloud.

## Before you begin

  * Make sure that you have the required Identity and Access Management (IAM) roles and permissions to perform the tasks described in this page:

    * `roles/oracledatabase.exascaleDbStorageVaultAdmin`
    * `roles/oracledatabase.exascaleDbStorageVaultViewer`

For more information about how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## View Exascale Storage Vault details

To view information about your Exascale Storage Vaults, do the following:

### gcloud

  * **List Exascale Storage Vaults**

Use the `gcloud oracle-database exascale-db-storage-vaults list` command to list vaults.
        
        gcloud oracle-database exascale-db-storage-vaults list \
        --project=PROJECT_ID \
        --location=REGION
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project.
    * REGION: the region where your Exascale Storage Vaults are located.
  * **View Exascale Storage Vault details**

Use the `gcloud oracle-database exascale-db-storage-vaults describe` command to view the details of an Exascale Storage Vault.
        
        gcloud oracle-database exascale-db-storage-vaults describe VAULT_ID \
        --project=PROJECT_ID \
        --location=REGION
        

Replace VAULT_ID with the ID of your Exascale Storage Vault.




###  API 

  * **List Exascale Storage Vaults**
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exascaleDbStorageVaults"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project.
    * REGION: the region where your Exascale Storage Vaults are located.
  * **View Exascale Storage Vault details**
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exascaleDbStorageVaults/VAULT_ID"
        

Replace VAULT_ID with the ID of your Exascale Storage Vault.




## Delete an Exascale Storage Vault

To delete an Exascale Storage Vault, do the following:

### gcloud

Use the `gcloud oracle-database exascale-db-storage-vaults delete` command to delete an Exascale Storage Vault.
    
    
    gcloud oracle-database exascale-db-storage-vaults delete VAULT_ID \
    --project=PROJECT_ID \
    --location=REGION
    

Replace the following:

  * VAULT_ID: the ID of the vault.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your vault is located.



###  API 

To delete an Exascale Storage Vault, run the following `curl` command:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exascaleDbStorageVaults/VAULT_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your Exascale Storage Vault is located.
  * VAULT_ID: the ID of your Exascale Storage Vault.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
