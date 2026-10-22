---
url: https://docs.cloud.google.com/looker/docs/looker-core-quickstart-public-ip-standard-edition/
title: Quickstart: Create a Looker (Google Cloud core) public secure connection standard edition instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:28.953669+00:00
---

# Quickstart: Create a Looker (Google Cloud core) public secure connection standard edition instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-quickstart-public-ip-standard-edition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Looker (Google Cloud core) public secure connection standard edition instance

Learn how to create a Looker (Google Cloud core) instance that uses default configuration settings. Looker (Google Cloud core) requires approximately 60 minutes to generate a new instance.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=looker--create-instance-public)

* * *

## Before you begin

Before you can create an instance, you need to complete these steps for the Google Cloud project in which you want to create the Looker (Google Cloud core) instance:

  1. [Work with Sales](https://cloud.google.com/contact/form?direct=true&e=13802955) to ensure that your [annual contract](https://cloud.google.com/looker/pricing) is completed and that you have [quota](https://docs.cloud.google.com/docs/quotas/view-manage) allocated in your project.
  2. [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#console).
  3. In the Google Cloud console, on the project selector page, [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) or navigate to an existing one. 

[ Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. [Enable the Looker API](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=looker.googleapis.com)

  5. Ensure that you have been granted the [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) IAM role for the Google Cloud project in which you want to create the Looker (Google Cloud core) instance.



## Create the Looker (Google Cloud core) instance

To create a Looker (Google Cloud core) instance that uses default configuration settings, follow these steps:

  1. Click [Go to Looker (Google Cloud core)](https://console.cloud.google.com/looker) and select the Google Cloud project in which you want to create the Looker (Google Cloud core) instance, if it is not already pre-selected. When you click the button, depending on what Looker instances already exist in this project, you'll see one of the following: 
     * If a Looker (Google Cloud core) instance already exists within this project, the **Instances** page will open. Click **Create Instance** to open the instance creation page.
     * If no Looker (Google Cloud core) instances have been created in this project, the Looker (Google Cloud core) product page will open. Click **Create An Instance** to open the instance creation page.
  2. In the **Instance name** field, provide a name for your Looker (Google Cloud core) instance. The instance name is not associated with the instance's URL. You won't be able to rename the instance after it has been created.
  3. In the **Region** field, select the region that matches your subscription contract, as this is where the [quota for your project](https://docs.cloud.google.com/docs/quotas/view-manage) is allocated. Then click **OK**.
  4. In the **Edition** section, set the instance edition to **Standard**. This edition provides a Looker platform that is best for small organizations or teams with fewer than 50 users. This edition is [billed](https://cloud.google.com/looker/pricing) monthly while the instance is active.

**Tip:** If your project doesn't have quota, you won't be able to select an edition type. [Contact Sales](https://cloud.google.com/contact/form?direct=true&e=13802955) to allocate quota to your project.
  5. Click **Create**. Looker (Google Cloud core) requires approximately 60 minutes to generate a new instance.

  6. Sign in to the new instance by navigating to the instance URL, which can be found on the [**Instances** page](https://docs.cloud.google.com/looker/docs/looker-core-view-console#viewing_instance_information) of the Google Cloud console, and [sign in with Google](https://support.google.com/accounts/answer/12629094?&sjid=8591543582681818450-NC).




## What's next

This Quickstart covered how to create a **Standard** Looker (Google Cloud core) instance that uses a public secure network connection and Google-managed encryption and that requires no deferred or denied maintenance windows and no additional users beyond the default number that is provided for a **Standard** edition.

For more information about creating and configuring an instance, see the Looker (Google Cloud core) documentation:

  * [Create a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create)
  * [Set up a custom domain for a Looker (Google Cloud core) instance that uses public connections](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain)
  * [Configure an IP allowlist for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist)
  * [Prepare a Looker (Google Cloud core) instance for users](https://docs.cloud.google.com/looker/docs/looker-core-instance-setup)
  * [Connect to your database](https://docs.cloud.google.com/looker/docs/looker-core-dialects)
  * [Use the sample LookML project on a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-sample-project)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
