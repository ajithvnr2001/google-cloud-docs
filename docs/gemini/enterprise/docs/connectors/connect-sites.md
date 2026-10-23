---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-sites/
title: Connect to Google Sites \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:33.549037+00:00
---

# Connect to Google Sites  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-sites/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Connect to Google Sites Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** You must enable Google Workspace smart features in other Google products to connect Google Sites data to Gemini Enterprise. For information, see [Turn Google Workspace smart features on or off](https://support.google.com/mail/answer/15604322).

To search data from Google Sites, use the following steps to create a connector using the Google Cloud console.

## Before you begin

  * You must be signed into the Google Cloud console with the same account that you use for the Google Workspace instance that you plan to connect. Gemini Enterprise uses your Google Workspace customer ID to connect to Google Sites.

  * To enforce data source access control and secure data in Gemini Enterprise, ensure that you have [configured your identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).



  * If you use security controls, be aware of their limitations related to data in Google Sites, as discussed in the following table:

Security control | Note the following  
---|---  
[Data Residency (DRZ)](https://docs.cloud.google.com/gemini/enterprise/docs/locations) | Gemini Enterprise only guarantees data residency in Google Cloud. For information about data residency and Google Sites, see Google Workspace compliance guidance and documentation, including [Data regions for Google Workspace](https://support.google.com/a/answer/9223653). Also review examples like [Choose the region where data is stored](https://support.google.com/a/topic/7631290) and [ Digital sovereignty](https://workspace.google.com/intl/en_in/security/digital-sovereignty/).   
[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/enterprise/docs/cmek) |  Your keys only encrypt data within Google Cloud. Cloud Key Management Service controls don't apply to data stored in Google Sites.   
[ Access Transparency](https://docs.cloud.google.com/gemini/enterprise/docs/access-transparency) |  Access Transparency logs actions taken by Google personnel on the Google Cloud project. You'll also need to review the Access Transparency logs created by Google Workspace. For more information, see [Access Transparency log events](https://support.google.com/a/answer/9230979) in the Google Workspace Admin Help documentation.   



### Console

To use the console to make Google Sites data searchable, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Go to the **Data Stores** page.

  3. Click **Create Data Store**.

  4. On the **Select a data source** page, select **Google Sites**.

  5. Choose a region for your data connector.

  6. Enter a name for your data connector.

  7. Click **Create**.




## Next steps

  * To attach your data store to an app, create an app and select your data store following the steps in [Create a search app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  * To preview how your search results appear after your app and data store are set up, see [Preview search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).

  * To restrict retrieval to specific Site URLs or exclude them, see [Add filters to a Google Sites data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gsites/add-filters-to-gsites-data-store).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
