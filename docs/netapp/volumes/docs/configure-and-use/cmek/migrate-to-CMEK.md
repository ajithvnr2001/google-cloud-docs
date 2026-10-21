---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/migrate-to-CMEK/
title: Migrate volumes to CMEK \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:36.636937+00:00
---

# Migrate volumes to CMEK  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/migrate-to-CMEK/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Migrate volumes to CMEK Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to migrate your volumes to customer-managed encryption key (CMEK).

## Before you begin

Volumes and their container storage pools can migrate from using Google-managed encryption keys to using CMEK.

If you choose to migrate volumes to a CMEK policy, all volumes in the specified region migrate to the CMEK policy. The CMEK policy setting applies to all storage pools in the region.

## Migrate volumes to CMEK

Use the following instructions to migrate volumes to CMEK using the Google Cloud console or Google Cloud CLI.

### Console

Use the following instructions to migrate volumes to CMEK using the Google Cloud console:

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Select **CMEK policies**.

  3. Find the CMEK policy you want to edit and click **Show more**.

  4. Select **Migrate volumes to CMEK**.

  5. Complete the **CMEK policy name** field to confirm migration.

  6. Click **Migrate**.




### gcloud

Use the following instructions to migrate volumes to CMEK using Google Cloud CLI:

Trigger a key migration:
    
    
      gcloud netapp kms-configs encrypt CONFIG_NAME \
        --project=PROJECT_ID \
        --location=LOCATION \

Replace the following information:

  * `CONFIG_NAME`: the name of the config.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the region of the config you want to delete.




For more options, see [Google Cloud SDK documentation for Cloud Key Management Service](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/kms-configs).

## What's next

[Apply a CMEK organization policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/apply-CMEK-organization-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
