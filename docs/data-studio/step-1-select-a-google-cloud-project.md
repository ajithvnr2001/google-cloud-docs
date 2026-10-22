---
url: https://docs.cloud.google.com/data-studio/step-1-select-a-google-cloud-project/
title: Step 1: Select a Google Cloud project \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:36.198916+00:00
---

# Step 1: Select a Google Cloud project  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/step-1-select-a-google-cloud-project/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Step 1: Select a Google Cloud project Stay organized with collections  Save and categorize content based on your preferences. 

Every Data Studio Pro subscription is associated with a Google Cloud project that hosts their Data Studio Pro content. Google Cloud projects form the basis for creating, enabling, and using all Google Cloud services, including managing APIs, enabling billing, adding and removing collaborators, and managing permissions for Google Cloud resources.

When setting up a Data Studio Pro subscription, you can select an existing Google Cloud project to host your Data Studio Pro content, or you can create a new one. During this step of subscription setup, you can also configure [data residency](https://docs.cloud.google.com/data-studio/data-residency), [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/data-studio/cmek), and [customer-managed storage](https://docs.cloud.google.com/data-studio/cms) for your Data Studio Pro content. If you're setting up a subscription from the Google Cloud console, first make sure that your selected Google Cloud project meets the requirements that are described on this page, and then proceed to [Step 2: Add people to the subscription](https://docs.cloud.google.com/data-studio/step-2-add-people-to-the-subscription).

**Tip:** We recommend that you select or create a new Google Cloud project that is dedicated to Data Studio Pro. This makes it easier to restrict access to the project and helps prevent accidental deletion of your Data Studio Pro content. The project's account information is used to provide Data Studio Pro services and for billing, so having a dedicated project makes it simpler to know how much you're spending on Data Studio Pro.**Important:** Once you've created a Pro subscription, you can't change its project. Instead, you can create a new subscription based on a different project, add licenses and users, move any content to the new project, then cancel the old subscription.

## Project requirements

The project that you choose to host your Data Studio Pro content must meet the following requirements:

  * The project must be owned by your organization.
  * The project must be linked to a billing account. [Learn how to set up a Google Cloud billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account).

  * You must have the Looker Studio Pro Manager Identity and Access Management role on the project. Project owners already have the same underlying permissions as those who are assigned to this role. For custom role configurations and granular permissions, see [Data Studio Pro roles and permissions](https://docs.cloud.google.com/data-studio/about-pro-roles-and-permissions).

  * The project must not already be in use for a Pro subscription.

  * You must belong to the same organization that owns the Google Cloud project that is used for the subscription.




Learn more about [identifying projects](https://www.google.com/url?q=https://cloud.google.com/resource-manager/docs/creating-managing-projects%23identifying_projects&sa=D&source=docs&ust=1695591374190751&usg=AOvVaw00_znkDjy7FDOmC5xVGnH7).

**Important:** Because Data Studio Pro projects have a [Google Cloud lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) placed on them, your assets are protected from accidental deletion. However, if you intentionally delete the project, ALL assets in that project are permanently deleted.

## Select an existing Google Cloud project

To select an existing Google Cloud project, follow these steps:

  1. In the **Get Data Studio Pro** dialog, click **Select project**.
  2. Click **Google Cloud project** and select a project. Data Studio will validate that this project meets the project requirements for Data Studio Pro.
  3. Click **Next**.



## Create a new Google Cloud project

If you're subscribing to Data Studio Pro from within Data Studio, you can create a new project directly from this step. To create a project, in addition to those listed previously you'll need to meet the following requirements:

  * You must accept the Google Cloud Platform Agreement.
  * You must have the [Projects Creator](https://cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectCreator) IAM role or a custom role that grants you the `resourcemanager.projects.create` permission.
  * You must provide a new project ID (one that hasn't been used before).
  * The project ID that you provide must meet naming conventions.
  * You must provide a valid billing account.



[Learn more about creating a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

To create a new project, follow these steps:

  1. In the **Get Data Studio Pro** dialog, click **Create new project**.
  2. Enter a project ID for your new project, following the required naming conventions that are described on the [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin) documentation page. Don't include sensitive information such as personally identifiable information (PII) or security data in your project ID.
  3. Click **Choose a billing account** and select a valid [billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project) for your Google Cloud project.
  4. Click **Create**.



## Use Data Studio Pro with multiple Google Cloud projects

If you want to use Data Studio Pro across multiple projects, you can do so by [adding a separate subscription for each project](https://docs.cloud.google.com/data-studio/link-pro-to-different-projects-within-your-organization).

For example, to use one project for your Sales team and a different project for your Marketing team, you'd create one subscription that is linked to your sales project and a second subscription that is linked to your marketing project.

## Next steps

If your organization uses [Looker](https://docs.cloud.google.com/looker) and your [Looker instance is eligible](https://docs.cloud.google.com/data-studio/pro-subscription-overview#complimentary-licenses-for-looker-users), you can receive complimentary Data Studio Pro licenses. After you set up a Google Cloud project for your subscription, you can link that project to your Looker instance and redeem the complimentary licenses. Select your Looker instance type for instructions on how to redeem these licenses:

  * [Looker (original)](https://docs.cloud.google.com/looker/docs/admin-panel-platform-dsp)
  * [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-dsp)



## Related resources

  * [Step 2: Add people to the subscription](https://docs.cloud.google.com/data-studio/step-2-add-people-to-the-subscription)
  * [Start a new Pro subscription](https://docs.cloud.google.com/data-studio/start-a-new-pro-subscription)
  * [About Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro)
  * [Edit a Data Studio Pro subscription](https://docs.cloud.google.com/data-studio/edit-a-pro-subscription)
  * [Organize and manage Data Studio Pro content](https://docs.cloud.google.com/data-studio/about-pro-content)
  * [Cancel a Data Studio Pro subscription](https://docs.cloud.google.com/data-studio/cancel-a-pro-subscription)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
