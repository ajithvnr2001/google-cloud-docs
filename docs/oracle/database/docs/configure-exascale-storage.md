---
url: https://docs.cloud.google.com/oracle/database/docs/configure-exascale-storage/
title: Configure Exascale Storage for Exadata Infrastructure \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:26:11.345046+00:00
---

# Configure Exascale Storage for Exadata Infrastructure  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/configure-exascale-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Configure Exascale Storage for Exadata Infrastructure Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Exascale Storage for Exadata Infrastructures in Google Cloud.

## Before you begin

  * Make sure that you have the required Identity and Access Management (IAM) roles and permissions to configure Exascale Storage:

    * `oracledatabase.cloudExadataInfrastructures.update` permission

For more information about how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## Configure Exascale Storage

To configure Exascale Storage for an Exadata Infrastructure instance, do the following:

### gcloud

Use the `gcloud oracle-database cloud-exadata-infrastructures configure-exascale` command to configure the Exascale Storage.
    
    
    gcloud oracle-database cloud-exadata-infrastructures configure-exascale EXADATA_INFRASTRUCTURE_ID \
    --project=PROJECT_ID \
    --location=REGION \
    --total-storage-size-gb=STORAGE_SIZE \
    --total-vm-storage-size-gb=VM_STORAGE_SIZE
    

Replace the following:

  * EXADATA_INFRASTRUCTURE: the ID of the Exadata Infrastructure.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your Exadata Infrastructure is located.
  * STORAGE_SIZE: the amount of Exascale storage (in GiBs) that you want to allocate from the Exadata Infrastructure.
  * VM_STORAGE_SIZE: the amount of Exascale VM storage (in GiBs) that you want to allocate from the Exadata Infrastructure.



###  API 

To configure the Exascale Storage for an Exadata Infrastructure instance, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/cloudExadataInfrastructures/EXADATA_INFRASTRUCTURE_ID:configureExascale"
    -d \
    '{
      "total_storage_size_gb": "STORAGE_SIZE",
      "total_vm_storage_size_gb": "VM_STORAGE_SIZE"
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your Exadata Infrastructure is located.
  * EXADATA_INFRASTRUCTURE: the ID of the Exadata Infrastructure.
  * STORAGE_SIZE: the amount of Exascale storage (in GiBs) that you want to allocate from the Exadata Infrastructure.
  * VM_STORAGE_SIZE: the amount of Exascale VM storage (in GiBs) that you want to allocate from the Exadata Infrastructure.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
