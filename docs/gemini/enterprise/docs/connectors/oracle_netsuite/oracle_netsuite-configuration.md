---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/oracle_netsuite/oracle_netsuite-configuration/
title: Oracle NetSuite configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:59.624672+00:00
---

# Oracle NetSuite configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/oracle_netsuite/oracle_netsuite-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Oracle NetSuite configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how to set up and configure a third-party application before creating the Oracle NetSuite data store.

## Create OAuth app

  1. Sign in to your Oracle NetSuite account.

  2. Create or select an integration application in your Oracle NetSuite account.

  3. In the application page, copy the **Account ID** , **Client ID** , and **Client secret** , and store them securely for later use.




## Set redirect URL and scopes

After creating the OAuth app, configure its redirect URL and scopes:

  1. In the application page, enter the redirect URL: `https://vertexaisearch.cloud.google.com/oauth-redirect`.

  2. Ensure the following scope is enabled for your integration:

Scope | Purpose  
---|---  
mcp | Allows the app to access Oracle NetSuite MCP tools and resources.  
  3. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
