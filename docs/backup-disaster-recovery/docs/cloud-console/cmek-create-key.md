---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/cmek-create-key/
title: Create an encryption key \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:21.941124+00:00
---

# Create an encryption key  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/cmek-create-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Create an encryption key Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to create a customer-managed encryption key using Cloud Key Management Service (Cloud KMS). You can use this key to back up data in other Google Cloud services.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
  2. Ensure that you have the Cloud KMS Admin (`roles/cloudkms.admin`) role or another role that includes the necessary permissions.



## Create a regional encryption key

Create a key in the same location as the resources you intend to back up.

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to the KMS console page](https://console.cloud.google.com/security/kms)

  2. Select an existing key ring or click **Create key ring** to create a new one.

  3. Click **Create key**.

  4. In the **Key name** field, enter a name for your key.

  5. For **Location type** , select **Region** or **Multi-region**.

  6. In the **Location** menu, select the same region as the resources you want to back up with this key.

If the key location and the resource location don't match, operations that use the key fail.

  7. Click **Create**.

  8. After the key is created, select the key from the list.

  9. Copy the **Resource name** for future reference.




The resource name has the following format:

`projects/`PROJECT_ID`/locations/`REGION`/keyRings/`KEY_RING_NAME`/cryptoKeys/`KEY_NAME

## What's next

  * Learn more about [Cloud KMS](https://docs.cloud.google.com/kms/docs/cmek).
  * Learn how to [create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
