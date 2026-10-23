---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/sourcegraph/sourcegraph-configuration/
title: Sourcegraph configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:10.114110+00:00
---

# Sourcegraph configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/sourcegraph/sourcegraph-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Sourcegraph configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how to set up and configure a third-party application before creating the Sourcegraph data store.

## Create OAuth app

  1. Sign in to your Sourcegraph account or site administration page.

  2. Navigate to your user account settings or site administration page to manage OAuth applications (client applications).

  3. Create a new OAuth client application.

  4. In the creation dialog, enter an application name (for example, `Gemini Enterprise Connector`).

  5. After you create the application, copy the **Client ID** and store it securely for later use when creating the data store.




## Set redirect URL and scopes

When creating or configuring the OAuth application, configure its redirect URL and scopes:

  1. Open the OAuth application configuration page in Sourcegraph.

  2. In the **Redirect URL** (or callback URL) field, enter `https://vertexaisearch.cloud.google.com/oauth-redirect`.

  3. Select and enable the following scopes:

Scope | Purpose  
---|---  
openid | Allows the app to authenticate the user using OpenID Connect.  
profile | Allows the app to view basic profile information of the authenticated user.  
email | Allows the app to view the email address of the authenticated user.  
offline_access | Grants a refresh token so the app can access Sourcegraph when the user is not actively logged in.  
mcp | Allows the app to connect using Model Context Protocol (MCP) to interact with Sourcegraph search and tools.  
  4. Save the configuration changes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
