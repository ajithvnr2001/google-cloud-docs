---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/linear/config/
title: Linear configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:59.978862+00:00
---

# Linear configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/linear/config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Linear configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up authentication before creating a Linear data store for use with Gemini Enterprise. To connect Linear to Gemini Enterprise, you must create a Linear OAuth app.

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

## Create and configure a Linear app

  1. Navigate to the [API](https://linear.app/settings/api) section of the Linear Administration settings.

  2. Click the add icon. Fill in the following fields:

     1. For **Application name** , enter a name for the OAuth app.

     2. For **Developer name** , enter your organization name.

     3. For **Developer URL** , enter a URL for your organization.

     4. For **Description** , enter a description of the OAuth app (for example, Gemini Enterprise integration").

     5. For **Callback URLs** , enter the following URL:
            
            https://vertexaisearch.cloud.google.com/oauth-redirect
            

     6. Select the **Client credentials** checkbox.

  3. Click **Create**.




## Use OAuth app credentials to connect Linear to Gemini Enterprise

After creating a Linear OAuth app, get the OAuth credentials required to set up a Linear data store in Gemini Enterprise.

  1. In the details page for your new app, copy the **Client ID** and **Client secret**.

  2. Create a Linear data store using the client credentials copied in the previous step. For more information about creating a Linear data store, see [Set up a Linear data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/linear/data-store).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
