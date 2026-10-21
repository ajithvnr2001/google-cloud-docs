---
url: https://docs.cloud.google.com/data-studio/try-pro/
title: Data Studio Pro subscription overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:01:44.147870+00:00
---

# Data Studio Pro subscription overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/try-pro/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Data Studio Pro subscription overview Stay organized with collections  Save and categorize content based on your preferences. 

A Data Studio Pro subscription gives users in your organization all the features of the no-cost version of Data Studio, plus the enhanced enterprise capabilities of Data Studio Pro.

For Data Studio Pro pricing, [visit our Marketing page](https://cloud.google.com/data-studio).

## Data Studio Pro subscription concepts

Subscribing to Data Studio Pro involves the following concepts or elements:

  * Subscription type
  * Licenses
  * Users
  * Google Cloud project
  * Google Cloud billing account
  * Pro Content



### Subscription type

Data Studio Pro is available as a self-service upgrade for Google Workspace or Cloud Identity organizations. A self-service Data Studio Pro subscription supports individual users, as well as teams and departments in your organization. A single organization can have multiple Pro subscriptions, if required.

#### Organization-wide (MAU) subscriptions

Data Studio Pro was originally launched as a "whole organization, monthly active user (MAU)" subscription type. In the MAU subscription type, everyone in the organization can use Data Studio Pro. Billing is based on the number of monthly active users of Data Studio Pro. A monthly active user is any user who views, edits, or otherwise interacts with Data Studio Pro content during a calendar month. MAU subscriptions are available only for large organizations, and they require a [Google Cloud sales specialist](https://cloud.google.com/contact?direct=true) to set them up.

Once a MAU subscription is set up, you must [link the subscription to a Google Cloud project](https://docs.cloud.google.com/data-studio/link-pro-to-a-google-cloud-project-mau-version). 

### Licenses

A self-service Data Studio Pro subscription is based on individual user licenses. You can buy as many Pro licenses as you need and assign them to individual users or to teams of users in your organization. You'll be billed monthly for the number of Pro licenses in the subscription, regardless of whether or not those licenses are used.

#### Complimentary licenses for Looker users

**Important:** Complimentary licenses are not available for the following Looker instances: 

  * Looker (original) instances that are are affiliated with Looker contracts that were signed after **August 1, 2026**.
  * Customer-hosted Looker (original) instances.
  * Looker (Google Cloud core) instances that are created after **August 1, 2026**.



As part of a Data Studio Pro subscription, a number of Data Studio Pro licenses are available at no cost to users of a Looker instance. Eligible Looker customers receive at least 1,000 complimentary licenses, or more if their Looker license count exceeds 1,000. For more information, see [Complimentary Data Studio Pro licenses offer details](https://cloud.google.com/terms/looker-studio/pro/complimentary-license-details).

### Users

Each Data Studio Pro user in the subscription who needs to create, edit, or manage content within Pro workspaces requires one Pro license. You assign licenses by adding specific users or Google Groups to the subscription.

Users who only need to view reports that are created within a Data Studio Pro environment don't require a Pro license. They only need the appropriate sharing permissions for the specific reports or data sources. However, these viewers don't have access to Pro-specific features like team workspaces or enhanced content management.

For more information about how to enable the **Trusted Orgs** feature to add users from other organizations to your Pro subscription, see [Add people to the subscription](https://docs.cloud.google.com/data-studio/step-2-add-people-to-the-subscription#add_users_from_other_organizations).

### Google Cloud project

Every Data Studio Pro subscription is associated with one (and only one) Google Cloud project. When setting up a Data Studio Pro subscription, you can select an existing Google Cloud project, or you can create a new one. To create multiple subscriptions, for example, to support different business units, you'll select or create different projects for each subscription.

### Google Cloud billing account

A Cloud Billing account is used to pay for your Data Studio Pro subscription. The billing account that you select must be linked to the Google Cloud project that you use for Data Studio Pro.

### Data Studio Pro content

Data Studio content consists of the reports and data sources that you create. With a Data Studio Pro subscription, you have two kinds of content: no-cost Data Studio content and Data Studio Pro content. No-cost content is owned by the individual user who created it. Pro content is owned by your organization through a Google Cloud project. This lets you manage your Pro content with project-level permissions and take advantage of other enterprise capabilities, such as team workspaces. [Learn more about Data Studio Pro content](https://docs.cloud.google.com/data-studio/about-pro-content).

## Subscription process overview

Subscribing to Data Studio Pro involves the following steps:

### 1\. Start a new Pro subscription

You can purchase a Data Studio Pro subscription from within Data Studio, from the the Google Cloud console, or from the Google Workspace Admin console. For more information see [Start a new Data Studio Pro subscription](https://docs.cloud.google.com/data-studio/start-a-new-pro-subscription).

### 2\. Select a Google Cloud project to use with Data Studio Pro

Data Studio Pro content lives in a Google Cloud project that is owned and managed by your organization. We recommend that you select or create a new project that is dedicated to Data Studio Pro. This makes it easier to restrict access to the project and helps prevent accidental deletion of your Data Studio Pro content.

### 3\. Add people to your Data Studio Pro subscription

You can assign Data Studio Pro licenses to specific users and to Google Groups. Using Google Groups is a convenient way to provide Data Studio Pro to teams and departments in your organization. For more information see [Add people to the subscription](https://docs.cloud.google.com/data-studio/step-2-add-people-to-the-subscription).

### 4\. Buy additional Data Studio Pro licenses

If your organization is growing, you can buy additional licenses and assign them to new users as needed. You can do this when you first subscribe to Data Studio Pro, and you can [buy more licenses](https://docs.cloud.google.com/data-studio/edit-a-pro-subscription) later.

### 5\. Upgrade Data Studio content to Data Studio Pro

To upgrade your existing no-cost Data Studio content to Pro content, the content must be moved into your Data Studio project. Your users can move their content manually, or an administrator can do it through an automated process. For more information, see [About Data Studio content](https://docs.cloud.google.com/data-studio/about-pro-content).

## Information for Google Cloud Partners

Google Cloud Partners often guide clients in adopting Data Studio Pro. Here's how the process works when dealing with separate organizations:

  * **Who Can Subscribe:** The Data Studio Pro subscription must be initiated by a user account that is part of the **client's** Google Cloud organization. The Google Cloud project selected for the subscription must also belong to the client's organization.

  * **Partner's Role:** A partner cannot directly purchase or initiate a new Data Studio Pro subscription for a project that resides in a client's separate Google Cloud organization.

  * **Billing:** The client's project must be linked to a valid Cloud Billing account. This can be a billing account managed by the partner, such as a reseller sub-billing account, provided it's linked to the client's project.

  * **Granting Partners Access:** Once the client has an active Data Studio Pro subscription, they can allow partner users to utilize Pro licenses. This is achieved by the client's administrator enabling the Trusted Organizations feature and adding the partner's organization ID. This allows the client to assign licenses to users from the partner organization.

  * **Billing Charges:** Note that Data Studio Pro subscription costs accrue to the billing account that's linked to the subscribed project. On a partner's primary billing account, these charges for a client's Pro subscription might appear under "Charges not specific to a project" when you view the sub-billing account, as the subscription is organization-level, not always tied to a single project's resource usage.




## Next step

[Start subscription](https://docs.cloud.google.com/data-studio/start-a-new-pro-subscription)

## Related resources

  * [About Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro)
  * [Edit a Data Studio Pro subscription](https://docs.cloud.google.com/data-studio/edit-a-pro-subscription)
  * [Cancel a Data Studio Pro subscription](https://docs.cloud.google.com/data-studio/cancel-a-pro-subscription)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
