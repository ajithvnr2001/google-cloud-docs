---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-enable-encryption/
title: Enable encryption on standard properties \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:33:25.222024+00:00
---

# Enable encryption on standard properties  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-enable-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Enable encryption on standard properties Stay organized with collections  Save and categorize content based on your preferences. 

Some organizations have requirements to encrypt phone fields in the Salesforce instance. This requires some changes in the CCAI Platform portal to allow searching for these phone numbers. For information about conducting searches for encrypted phone fields, see [Enable exact search queries for encrypted phone fields](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-exact-search-queries).

## Permissions

  * **CC_Agent_App** must be 1.38+ to enable encryption on standard properties.

  * Admin must have **Manage Encryption Keys, Customize Application, View Setup and Configuration, & Manage Certificates** permissions in their role.




## Enable encryption

To enable encryption in the Salesforce platform, follow these steps:

  1. To create a new tenant secret, do the following. This is required to create a deterministic tenant secret.

     1. Go to **Setup > Key Management**.

     2. Click **Generate Tenant Secret**.

  2. Go to **Encryption Settings > Deterministic Encryption**, and click the toggle to the on position.

  3. To create a new **Deterministic Tenant Secret** , do the following:

     1. Go to **Setup > Key Management**.

     2. Go to the **Fields (Deterministic)** tab.

     3. Click **Generate Tenant Secret**.

  4. From **Setup** , in the **Quick Find** field, enter **Encryption Settings** , and then select **Encryption Settings**. Only new data is affected by this setting change. To apply these settings retroactively, see [Synchronize Your Data Encryption with the Background Encryption Service](https://developer.salesforce.com/docs/atlas.en-us.securityImplGuide.meta/securityImplGuide/security_pe_mass_encryption.htm#security_pe_mass_encryption).

  5. Update settings to encrypt phone fields on the contact types.

  6. In the phone field, select **Deterministic**. **Probabilistic** won't work with exact searches. Exact searches are required to search for encrypted phone numbers.

  7. Click **Apply**. An email is generated that contains a summary of the encryption settings. If any fields are invalid an explanation is included.




### Example email

The following is an example email.
    
    
    Encryption is now enabled on one or more fields.
    
    These fields use deterministic encryption:
    Contact: Phone, Home Phone, Other Phone
    
    Salesforce Shield Platform Encryption
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
