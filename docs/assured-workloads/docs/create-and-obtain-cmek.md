---
url: https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek/
title: Create and obtaining a CMEK key \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:24.610766+00:00
---

# Create and obtaining a CMEK key  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/create-and-obtain-cmek/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and obtaining a CMEK key

If you use customer-managed encryption keys (CMEK) to encrypt your Assured Workloads resources, this page shows you how to create and obtain those keys. Learn more about [Assured Workloads encryption options](https://docs.cloud.google.com/assured-workloads/docs/key-management).

## Before you begin

  1. Choose an encryption strategy.

**Note:** Review [Data encryption and encryption keys](https://docs.cloud.google.com/assured-workloads/docs/key-management), to determine your encryption strategy.
  2. [Create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/key-management) for a control package that supports your requirements.

  3. Select the project ID for the project that contains your Assured Workloads CMEK keys. If you chose IL4 or CJIS as a control package, then, by default, this project is created for you.


**Note:** When accessing a project within an Assured Workloads folder, you must acknowledge the Regulatory Intercept, which generates an audit log when accessing a regulated resource.

## Create the key

**Note:** If you have already created a CMEK, you can skip key creation and go directly to Obtain your CMEK key resource ID.

To create the CMEK key, do the following:

  1. In the Google Cloud console, go to the **Key management** page:

[Go to Key management](https://console.cloud.google.com/security/kms)

  2. Select the Assured Workloads CMEK project. By default, this project ID starts with `cmek-`.

  3. Click your key ring.

  4. Click **Create Key**.

  5. From the **What type of key do you want to create?** list, select **Generated key**.

  6. In **Key name** enter the key name.

  7. From the **Protection level** list, select **Software**.

  8. From the **Purpose** list, select **Symmetric encryption/decryption**.

  9. From the **Rotation period** list, select **90 days**.

  10. Optional: To add a label, do the following:

     1. Click **Add a label.**
     2. Enter a key in the **Key** text field.
     3. Enter a value in the **Value** text field.
  11. Click **Create.**




## Obtain your CMEK key resource ID

**Note:** You might need to contact your security administrator or Assured Workloads administrator to obtain the key resource ID.

  1. In Google Cloud console, in the **Project Selector** , select the project ID for the project that contains your CMEK keys. By default, if Assured Workloads creates this project, it prepends the project ID `cmek-`.
  2. In **Security** , go to the **Key management** page:

[Go to Key management](https://console.cloud.google.com/security/kms)

  3. Under **Key rings** , click the key ring name.

  4. In **Key ring details** , in the **Keys** tab, click the name of the key.

  5. Click the _more_vert_**More** icon to the right of the key name.

  6. Click **Copy Resource Name**.

The resource string is formatted as follows:
         
         projects/SECURITY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
         




## What's next

  * Learn about [supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management).
  * Learn about [data encryption and encryption keys](https://docs.cloud.google.com/assured-workloads/docs/encryption-keys).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
