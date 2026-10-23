---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/manage-cmek-policy/
title: Manage CMEK policies \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:55.780083+00:00
---

# Manage CMEK policies  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/manage-cmek-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage CMEK policies Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions on how to edit or delete a customer-managed encryption key (CMEK) policy.

## Edit a CMEK policy

You can change the labels and description of a CMEK policy, but you cannot specify a different key to be used. To specify a different key, you need to update the CMEK policy, which only works if it isn't already being used by a storage pool.

Use the following instructions to edit a CMEK policy using the Google Cloud console or Google Cloud CLI.

### Console

Use the following instructions to edit a CMEK policy in the Google Cloud console. You can only change a CMEK policy description and its labels.

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Select **CMEK policies**.

  3. Find the CMEK policy you want to edit and click **Show more**.

  4. Select **Edit**.

  5. Optional: Change the description in the **Description** field.

  6. Optional: Add, modify, or delete labels.




### gcloud

Run the following command to edit a CMEK policy in Google Cloud CLI:
    
    
    gcloud netapp kms-configs update CONFIG_NAME \
       --project=PROJECT_ID \
       --location=LOCATION \
       --description=DESCRIPTION \
       --labels=LABELS \

For more options, see [Google Cloud SDK documentation for Cloud Key Management Service](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/kms-configs).

## Delete a CMEK policy

You can delete a CMEK policy if the policy is unused by any storage pools.

### Console

Use the following instructions to delete a CMEK policy using the Google Cloud console:

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Select **CMEK policies**.

  3. Find the CMEK policy you want to delete and click **Show more**.

  4. Select **Delete**.

  5. To confirm your selection, enter a name in the **CMEK policy name** field.

  6. Click **Delete**.




### gcloud

Use the following instructions to delete a CMEK policy using the Google Cloud CLI.

Delete the CMEK policy:
    
    
    gcloud netapp kms-configs delete CONFIG_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \

Replace the following information:

  * `CONFIG_NAME`: the name of the config

  * `PROJECT_ID`: the name of the project the CMEK policy is in

  * `LOCATION`: the region of the config you want to delete




For more options, see [Google Cloud SDK documentation for Cloud Key Management Service](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/kms-configs).

## What's next

[Migrate volumes to CMEK](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/migrate-to-CMEK).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
