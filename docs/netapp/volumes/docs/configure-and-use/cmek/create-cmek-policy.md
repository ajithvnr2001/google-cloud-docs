---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/create-cmek-policy/
title: Create a CMEK policy \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:26.289168+00:00
---

# Create a CMEK policy  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/create-cmek-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a CMEK policy Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to create a customer-managed encryption key (CMEK) policy.

## Create a CMEK policy

Use the following instructions to create a CMEK policy using the Google Cloud console or Google Cloud CLI:

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Select **CMEK policies**.

  3. Under **Create a CMEK policy** , click **Create**.

  4. Enter a unique name in the **name** field for the CMEK policy.

  5. Optional: Add a description in the **description** field.

  6. Select a region from the **region** field for the policy.

  7. Select a Cloud KMS key from the following options:

     * Choose from the Cloud KMS keys from your project that appear in the drop-down menu.

     * Select **Switch project** if you want to look for a Cloud KMS key in a different project. You need `roles/cloudkms.viewer` in the selected project to be able to browse keys.

     * Select **Enter key manually** if you want to enter a key manually. This is helpful if you don't have permissions to look up the key you intend to use.

  8. Optional: Add a label in the **labels** field.

  9. Click **Create**.




Your CMEK policy appears on the CMEK policies page. The status of the policy has an exclamation exclamation mark. The exclamation mark indicates that this policy needs verification before it's usable. For more information, see [Verify key access](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/verify-key-access).

### gcloud

Use the following instructions to create a CMEK policy using the Google Cloud CLI.

  1. Run the `kms-configs` command with the following parameters:
         
         gcloud netapp kms-configs create CONFIG_NAME \
          --project=PROJECT_ID \
          --location=LOCATION \
          --kms-project=KEY_RING_PROJECT \
          --kms-location=KEY_RING_LOCATION \
          --kms-keyring=KEY_RING \
          --kms-key=KEY_NAME




Replace the following information:

  * `CONFIG_NAME`: the name of the config to be created. This name must be unique per region.

  * `PROJECT_ID`: the name of the project you want to create the CMEK policy in.

  * `LOCATION`: the region of the config to be created in. Google Cloud NetApp Volumes only supports one config per region.

  * `KEY_RING_PROJECT`: the project ID of the project hosting the KMS key ring.

  * `KEY_RING_LOCATION`: the location of the KMS key ring.

  * `KEY_RING`: the name of the KMS key ring.

  * `KEY_NAME`: the name of the KMS key.




For more options, see [Google Cloud SDK documentation for Cloud Key Management Service](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/kms-configs).

## What's next

[Verify key access](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/verify-key-access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
