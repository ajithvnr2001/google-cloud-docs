---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pagerduty/pagerduty-configuration/
title: PagerDuty configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:38:00.261784+00:00
---

# PagerDuty configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pagerduty/pagerduty-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  PagerDuty configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how to set up and configure a third-party application before creating the PagerDuty data store.

## Create OAuth app

  1. Sign in to your PagerDuty account as an Admin or Account Owner.

  2. In the top navigation bar, go to **Integrations**.

  3. Under **Developer Tools** , click **App Registration**.

  4. Click **\+ New App** (or **Create New App**).

  5. Enter an **App Name** and a brief **Description**.

  6. Under **Functionality** , select **OAuth 2.0**.

  7. Click **Next** or proceed to configure the OAuth settings.

  8. Copy the **Client ID** and **Client Secret** immediately, and store them securely for later use. The Client Secret will only be displayed once.




## Set redirect URL and scopes

After creating the OAuth app, configure its redirect URL and scopes:

  1. In the **App Registration** page, click the app that you created in the previous section.

  2. Open the OAuth application page.

  3. Set the redirect URL:

     * In the **Redirect URL** field, enter `https://vertexaisearch.cloud.google.com/oauth-redirect`.
  4. Select the following scopes:

Scope | Purpose  
---|---  
read | Grants read access to PagerDuty resources like incidents, services, and users.  
write | Grants write access to PagerDuty resources, allowing creation and modification of incidents, services, and users.  
  5. Save your changes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
