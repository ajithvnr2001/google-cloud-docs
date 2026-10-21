---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-exact-search-queries/
title: Enable exact search queries for encrypted phone fields \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:29:50.068735+00:00
---

# Enable exact search queries for encrypted phone fields  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-exact-search-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Enable exact search queries for encrypted phone fields Stay organized with collections  Save and categorize content based on your preferences. 

If you have phone fields encrypted in Salesforce, you need to make an update in the CCAI Platform portal to allow searching for phone numbers in your instance. If you encounter issues with search, verify that encryption is properly configured in the Salesforce tenant. To verify you have encryption configured correctly, see [Enable encryption on standard properties](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-enable-encryption).

## Turn on exact search in Contact Center AI Platform

To turn on exact search, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Under **Account Lookup** , click the **Phone number lookup field is encrypted** checkbox.

  3. Under **Phone Number Format** , select a phone number format. If the phone number format is set to **Automatic** , the phone number lookup fails and and an error is returned.

  4. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
