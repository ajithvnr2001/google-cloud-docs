---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/overview-of-fine-grained-access-control/
title: Overview \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:15.794735+00:00
---

# Overview  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/overview-of-fine-grained-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can control who has access to what data in Customer Experience Insights. As an administrator, you can grant individual users access to a specific portion of your Customer Experience Insights data, without letting them access all the data. This fine-grained access control is possible when you use authorized views.

Authorized views have full access to all the data, and use a filter expression to restrict which data the user can access. If you grant each individual user access to only one authorized view, a user can only access the portion of data that their authorized view's filter allows.

## Authorized views

Use authorized views to perform the following tasks:

  * Let a manager view and analyze only conversations for agents in their reporting chain.
  * Allow an agent to view only their own conversations.
  * Retrieve conversation data.
  * Perform analysis.
  * Edit feedback labels.



You can't use authorized views to perform the following tasks:

  * Edit or import conversation data.
  * Train topic models.
  * Create score cards.



### View sets

Authorized views are [resources with built-in identities](https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities) and require permissions to access Customer Experience Insights data. You can group them into authorized view sets, which can help organize permissions for authorized views. For example, you can grant a role to all authorized views in an authorized view set instead of individual authorized views using [principal identifiers for sets of resources](https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities#resource-sets).

## Grant fine-grained access

Follow these steps to grant a user fine-grained access:

  1. Create an authorized view set to group the authorized views.
  2. To allow access to Customer Experience Insights data, grant a role on the project to the authorized view.
  3. Create an authorized view to define the data restrictions.
  4. To allow a user to perform actions through the authorized view, grant them a different role on the authorized view.



For example, to allow view access to conversations, you can grant the `contactcenterinsights.conversations.get` permission to the authorized view through the `contactcenterinsights/viewer` role at the project level. You should also grant the corresponding `contactcenterinsights.authorizedConversations.get` permission to the user through the `contactcenterinsights/authorizedViewer` role on the authorized view.

The user only has access based on the combination of the following permissions:

  1. The user has `contactcenterinsights.authorizedConversation.get` on the authorized view.
  2. The authorized view filter doesn't restrict the conversation they're trying to view.
  3. The authorized view has `contactcenterinsights.conversation.get` on the project.



## What's next?

  * [Create and manage authorized views](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-and-manage-authorized-views)
  * [Use authorized views](https://docs.cloud.google.com/gemini-enterprise-cx/insights/use-authorized-views)
  * [Best practices for authorized views](https://docs.cloud.google.com/gemini-enterprise-cx/insights/best-practices-for-fine-grained-access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
