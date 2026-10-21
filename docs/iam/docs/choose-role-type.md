---
url: https://docs.cloud.google.com/iam/docs/choose-role-type/
title: Choose which type of role to use \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:07.549972+00:00
---

# Choose which type of role to use  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/choose-role-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Choose which type of role to use Stay organized with collections  Save and categorize content based on your preferences. 

This page offers guidance on which type of role—predefined, custom, or basic—you should use to control access to Google Cloud resources.

The following summarizes our recommendations for choosing which type of role to use:

  * We recommend that you prioritize using predefined roles because they're managed by Google and offer a balance of security and convenience.
  * If you need a role that closely adheres to the principle of least privilege, and you can't find a predefined role that fits your security requirements, use custom roles.
  * Don't use basic roles unless you have no alternative or are using them in a test environment.



## When to use predefined roles

Generally, we recommend that you [use predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles) instead of basic or custom roles. [Predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined) give granular access to specific Google Cloud resources, are maintained by Google, and are updated automatically when new permissions, features, or services are added to Google Cloud.

We recommend prioritizing predefined roles that contain all of the permissions that a user is likely to need for a given use case. Most services provide broad Admin, Editor, and Viewer roles that serve this purpose. For example, the Bigtable Admin role provides administrative permissions to create new instances and access to all table data in a project, and the Bigtable Viewer role provides view-only access to the Bigtable in the Google Cloud console.

However, there are some cases where you might want to use custom or basic roles. The following sections describe these cases.

## When to use custom roles

Unlike predefined roles, custom roles are not maintained by Google. That means when Google Cloud adds new permissions, features, or services, your custom roles won't be updated automatically. For this reason, we recommend granting the most limited [predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles) that meet your needs.

However, it might be appropriate to create and grant custom roles in the following cases:

  * A principal needs a permission, but each predefined role that includes that permission also includes permissions that the principal doesn't need and shouldn't have. 
  * You use [role recommendations](https://docs.cloud.google.com/iam/docs/recommender-overview) to replace overly permissive role grants with more appropriate role grants. In some cases, you might receive a [recommendation to create a custom role](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#custom-roles). 



When using custom roles, be aware of the following limits:

  * Custom roles can contain up to 3,000 permissions.
  * The maximum total size of the title, description, and permission names for a custom role is 64 KB.
  * There are limits to the number of custom roles you can create:

    * You can create up to 300 organization-level custom roles in your organization.
    * You can create up to 300 project-level custom roles in each project in your organization.



## When to use basic roles

Basic roles include thousands of permissions across all Google Cloud services. In production environments, do not grant basic roles unless there is no alternative. Instead, grant the most limited [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meet your needs. 

If you need to replace a basic role, you can use [role recommendations](https://docs.cloud.google.com/iam/docs/recommender-overview) to determine which roles to grant instead. You can also use the [Policy Simulator](https://docs.cloud.google.com/iam/docs/understanding-simulator) to ensure that changing the role won't affect the principal's access.

It might be appropriate to grant basic roles when you want to grant broader permissions for a project. This often happens when you're granting permissions in development or test environments.

## What's next

  * Learn how to [find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).
  * Learn how to [create custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).
  * Learn more about [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
