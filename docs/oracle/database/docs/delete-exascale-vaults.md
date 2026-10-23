---
url: https://docs.cloud.google.com/oracle/database/docs/delete-exascale-vaults/
title: Delete Exascale Storage Vaults \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:03.369038+00:00
---

# Delete Exascale Storage Vaults  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/delete-exascale-vaults/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Delete Exascale Storage Vaults Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete an Exascale Storage Vault in Google Cloud.

## Before you begin

Make sure that you have the required Identity and Access Management (IAM) roles and permissions to delete an Exascale Storage Vault:

  * `roles/oracledatabase.exascaleDbStorageVaultAdmin`



For information on how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).

## Delete an Exascale Storage Vault

To delete an Exascale Storage Vault, do the following:

### Console

  1. Go to the **Exadata Database Service > Exascale Infrastructure** page.

[Go to Exascale Infrastructure](https://console.cloud.google.com/oracle/exascale/)

  2. Select the **Exascale Storage Vaults** tab.

  3. For the Exascale Storage Vault that you want to delete, click more_vert **View actions** , and then click **Delete**.

  4. In the **Delete Exascale Storage Vault?** dialog, type the vault name to confirm deletion of your vault.

  5. Click **Confirm**.




###  API 

To delete an Exascale Storage Vault, run the following `curl` command:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exascaleDbStorageVaults/VAULT_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains the Exascale Storage Vault. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of your Exascale Storage Vault.
  * VAULT_ID: the ID of your Exascale Storage Vault.



## What's next

  * Learn more about [Exadata Database Service on Exascale Infrastructure](https://docs.public.content.oci.oraclecloud.com/en-us/iaas/exadb-xs/doc/overview-exadb-xs-service.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
