---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/troubleshoot-data-upload-permissions/
title: Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:08.031553+00:00
---

# Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/troubleshoot-data-upload-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

## Provide Access to Destination Bucket

Finish the [Project Setup and Key Download](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide#project-setup-and-key-download) step for the session. The Session ID can be found in the email titled _Action Required: Provide Access for Data Upload - Google Transfer Appliance._

## Provide Access to KMS

  1. **Prerequisite:** Ensure you have the **Cloud KMS Admin** role (`roles/cloudkms.admin`) to provide access to the KMS key.
  2. Find the Session ID in the email titled _Action Required: Provide Access for Data Upload - Google Transfer Appliance._
  3. Find the KMS key in the 'Key resource n̦ame' field on the Appliance Detail page for the given session.
  4. Go to the **Cryptographic Keys** page in Google Cloud console.

[Go to the Cryptographic Keys page](https://console.cloud.google.com/security/kms)

  5. Click the key ring that contains your asymmetric key.

  6. Select the checkbox for the asymmetric key.

  7. In the **Info panel** , click **Add principal**.

     * **Add principals** is displayed.
  8. In the **New principals** field, enter the Transfer Appliance P4SA. It looks like the following example:

`service-PROJECT_NUMBER@gcp-sa-transferappliance.iam.gserviceaccount.com`

In this example, `PROJECT_NUMBER` is the Google Cloud project number that your appliance is under.

  9. In the **Select a role** field, add the **Cloud KMS CryptoKey Public Key Viewer** role.

  10. Click the **Add another role** and add **Cloud KMS CryptoKey Decrypter** role.

  11. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
