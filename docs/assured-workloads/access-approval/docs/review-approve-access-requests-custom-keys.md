---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/review-approve-access-requests-custom-keys/
title: Review and approve access requests using a custom signing key \u00a0|\u00a0 Access Approval \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:50.855776+00:00
---

# Review and approve access requests using a custom signing key  |  Access Approval  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/review-approve-access-requests-custom-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Approval ](https://docs.cloud.google.com/assured-workloads/access-approval/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

## (Optional) Configure Access Approval with a custom signing key

This document shows how to set up Access Approval using the Google Cloud console to add an optional custom signing key for Access Approval requests.

## Before you begin

  * Ensure that Access Approval is already enabled. For more information, see [Enabling Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/review-approve-access-requests-google-keys). 



### Configure a custom signing key (Optional)

Access Approval uses a signing key to verify the integrity of the Access Approval request. By default, a Google-owned and managed key is used.

If you have Cloud EKM enabled, you can choose an externally-managed signing key. For information about using external keys, see [Cloud EKM overview](https://docs.cloud.google.com/kms/docs/ekm#overview).

You can also choose to create a Cloud KMS signing key with an algorithm of your choice. For more information, see [Creating asymmetric keys](https://docs.cloud.google.com/kms/docs/creating-asymmetric-keys).

To use a custom signing key, follow the instructions in this section.

**Get the email address of the service account**

The email address for the service account is of the following form:
    
    
      service-PROJECT_NUMBER@gcp-sa-accessapproval.iam.gserviceaccount.com
    

Replace PROJECT_NUMBER with the project number.

For example, the email address is `service-p123456789@gcp-sa-accessapproval.iam.gserviceaccount.com` for a service account in a project whose project number is `123456789`.

To use your signing key, do the following:

  1. On the **Access Approval** page in the Google Cloud console, select **Use a Cloud KMS signing key (advanced)**.

  2. Add the crypto key version resource ID.

The crypto key version resource ID must have the following form:
         
         projects/PROJECT_ID/locations/LOCATION/keyRings/KEYRING_ID/cryptoKeys/CRYPTOKEY_ID/cryptoKeyVersions/KEY_ID
         

For more information, see [Getting a Cloud KMS resource ID](https://docs.cloud.google.com/kms/docs/getting-resource-ids).

  3. To save your settings, click **Save**.

To use a custom signing key, you must grant the [Cloud KMS CryptoKey Signer/Verifier](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) (`roles/cloudkms.signerVerifier`) IAM role to the Access Approval service account for your project.

If the Access Approval service account doesn't have the permissions to sign with the key you provided, you can grant the required permissions by clicking **Grant**. After granting the permissions, click **Save**. 




## Clean up

To remove your optional custom signing key:

  1. On the Access Approval page in the Google Cloud console, open settings.
  2. Under Advanced Settings, select the default (Google) signing key option.



## What's next

  * Learn about the [anatomy of an access request](https://docs.cloud.google.com/assured-workloads/access-approval/docs/approval-request-details).
  * Learn how to [approve Access Approval requests](https://docs.cloud.google.com/assured-workloads/access-approval/docs/approve-requests).
  * Learn how to [view historical Access Approval requests](https://docs.cloud.google.com/assured-workloads/access-approval/docs/view-historical-requests).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
