---
url: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles/
title: Create a custom role to restrict access to AI developer tools \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:36.810967+00:00
---

# Create a custom role to restrict access to AI developer tools  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Create a custom role to restrict access to AI developer tools Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To use this feature, your project must be linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that receives an active monthly invoice.

Default roles often provide broad access. To restrict access to AI developer tools and better align permissions with your organization's security policies, create custom roles. This guide shows you how to create and assign a custom IAM role for Gemini Enterprise's AI developer tools in the Google Cloud console.

When AI developer tools are enabled, users with a Gemini Enterprise license can access these tools if you grant them the [Gemini Enterprise User](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) (`roles/discoveryengine.agentspaceUser`) role.

## Create a custom IAM role

To create a custom IAM role that restricts access to AI developer tools, follow these instructions:

  1. In the Google Cloud console, go to **IAM & Admin > Roles**.
  2. Click **Create role**.
  3. Enter the role details:

     * **Title:** Give your role a name. For example, Custom Gemini Enterprise User.
     * **ID:** The Google Cloud console automatically generates the ID, but you can edit it.
     * **Role launch stage:** Set this to "General Availability".
  4. Click **Add permissions**.

  5. In the panel, search for and select the [Gemini Enterprise User](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) (`roles/discoveryengine.agentspaceUser`) role.

  6. Remove all permissions starting with `businessaicode.` from the Gemini Enterprise User role to ensure users assigned this custom role can't access the AI developer tools feature.

  7. Click **Create**.




## Add users to the custom role

To add users to the custom role you created, follow these steps:

  1. In the Google Cloud console, go to **IAM & Admin > IAM**.
  2. Click the **Grant access** button at the top of the page.
  3. In the **New principals** field, enter the email addresses of the users or groups you want to add.
  4. Assign the role: 
     * Click **Assign roles** and search for the **Title** of the custom role you created in the previous section.
     * Select the role.
  5. Click **Save**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
