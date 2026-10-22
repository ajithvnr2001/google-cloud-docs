---
url: https://docs.cloud.google.com/data-studio/consolidate-multiple-pro-subscriptions/
title: Consolidate multiple Data Studio Pro subscriptions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:30.926868+00:00
---

# Consolidate multiple Data Studio Pro subscriptions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/consolidate-multiple-pro-subscriptions/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Consolidate multiple Data Studio Pro subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document is intended for Cloud Identity and Google Workspace administrators who want to centralize management of Data Studio Pro under a single Google Cloud project.

For example, say that several departments in your organization have subscribed to Data Studio Pro, and each department manages its content within their own Google Cloud projects. Managing Data Studio Pro with a single subscription and a single project can make it easier to manage billing and access controls.

To consolidate multiple subscriptions and projects, follow these steps:

  * Prevent users from creating new Data Studio Pro departmental subscriptions
  * Find Data Studio Pro projects in your organization
  * Choose a single Data Studio Pro project to use
  * Add users and licenses to the chosen Data Studio Pro project
  * Move existing content into the chosen Data Studio Pro project
  * Make the chosen project the default project
  * Remove users and licenses from other projects



## Prevent users from creating new Data Studio Pro departmental subscriptions

You can prevent users from creating Pro subscriptions by using an [IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-overview#centralize-admin-privileges). To set up a deny policy, complete the following tasks:

  1. Select or create a Google Group that contains the users who will manage Data Studio Pro. For example: `lsp-managers@example.com`.
  2. Create a deny policy that denies the `datastudio.googleapis.com/pro.manage` permission to everyone except the example Google Group. Following is an example deny policy that uses the `lsp-managers@example.com` Google Group:
         
         {
         
         "deniedPrincipals": [
         
         "principalSet://goog/public:all"
         
         ],
         
         "exceptionPrincipals": [
         
         "principalSet://goog/group/lsp-managers@example.com"
         
         ],
         
         "deniedPermissions": [
         
         "datastudio.googleapis.com/pro.manage"
         
         ]
         
         }
         

  3. Attach the deny policy to your organization.




Learn how to [set up an IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-overview#centralize-admin-privileges) for your organization.

## Find Data Studio Pro projects in your organization

You can locate the Cloud projects that are in use for Data Studio Pro by using the Data Studio Pro user interface or by using [Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports) in the Google Cloud console.

### Use the Data Studio Pro user interface

To locate the Cloud projects that are in use for Data Studio Pro, follow these steps in the Data Studio Pro user interface:

  1. Grant yourself an organization-level IAM role, such as the `lookerstudio.proManager` role, that includes the `lookerstudio.pro.manage` permission.
  2. [Sign in to Data Studio Pro](https://datastudio.google.com/).
  3. To view the list of Pro subscriptions in your organization, in the left navigation, click **Pro Subscriptions**.



### Use Cloud Billing reports to find linking projects

If you don't have access to the Data Studio Pro user interface (for example, if you're a Billing Administrator), you can identify the Cloud projects that are linked to Data Studio Pro subscriptions by using [Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports) in the Google Cloud console.

To view these charges, open the [Cloud Billing reports](https://console.cloud.google.com/billing) page in the Google Cloud console, then configure the report filters as follows:

  * Group the report by **Project**.
  * Filter **Services** to **Data Studio**.
  * Filter **SKUs** to the SKUs that contain `Data Studio Pro`.



The report displays costs broken down by project. The projects showing charges for the `Data Studio Pro` SKU are the linking projects for your Data Studio Pro subscriptions.

For generic instructions on using reports, see [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports).

  * **Data Studio Pro subscription fees:** These charges are associated with the linking project and appear under SKUs that are specifically named for the Pro subscription (for example, `Data Studio Pro`).
  * **Query usage costs:** Charges that are incurred from Data Studio querying data sources (such as BigQuery) are billed to the project that contain the data or the project that's configured as the billing project in the Data Studio data source settings. These costs appear under the respective service's SKUs (for example, BigQuery analysis SKUs).



## Choose a single Data Studio Pro project to use

Choose one of the existing Data Studio Pro projects to use as the single project for your organization. You might choose the project with the most content or the one with the most licenses. Alternatively, you might create a new project to be the chosen Data Studio Pro project.

## Add users and licenses to the chosen Data Studio Pro project

Use the Data Studio Pro user interface or the Google Cloud console to add your existing users and licenses to the chosen Data Studio Pro project. You'll need to repeat this process for each subscription in your organization if you want to maintain those licenses.

Learn more about [managing Data Studio Pro subscriptions](https://docs.cloud.google.com/data-studio/edit-a-pro-subscription).

## Move existing content into the chosen Data Studio Pro project

To consolidate existing content from the original projects, move that content into the chosen project using the Data Studio UI. See [add and remove team workspace assets](https://docs.cloud.google.com/data-studio/manage-team-workspace-assets) for more information.

## Make the chosen project the default project

Setting a default Data Studio Pro project ensures that users can only create content in an organization-managed location. Follow the directions in [Set a default Data Studio Pro project](https://docs.cloud.google.com/data-studio/set-a-default-google-cloud-project-for-pro) and select your chosen Data Studio Pro project to be the default project.

## Remove users and licenses from other projects

Finally, [remove the users and licenses](https://docs.cloud.google.com/data-studio/edit-a-pro-subscription) from the original Data Studio Pro projects.

**Warning:** Don't skip this step. If an individual user belongs to multiple subscriptions, you will be charged for a license for each subscription that user is in.

Additionally, unless your organization sets up a deny policy as described previously, users will still be able to create new Pro subscriptions and create Pro content in any project that they have a license on.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
