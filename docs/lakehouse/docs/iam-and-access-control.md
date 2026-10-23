---
url: https://docs.cloud.google.com/lakehouse/docs/iam-and-access-control/
title: Borderless Lakehouse: Access control with IAM \u00a0|\u00a0 BigLake API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:50.220605+00:00
---

# Borderless Lakehouse: Access control with IAM  |  BigLake API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/iam-and-access-control/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ BigLake API ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



#  Borderless Lakehouse: Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Managing access control for _borderless Lakehouse_ requires adding users to a Google Cloud project and assigning appropriate roles. By default, projects grant access only to the original creator. Additional users cannot access resources until they are added as project members or bound to specific resources.

## What is IAM?

Google Cloud offers [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam), which lets you grant more granular access to specific Google Cloud resources and prevents unwanted access to other resources. IAM lets you adopt the [security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources within _Lakehouse_.

IAM also lets you control who (an identity) has what permissions (roles) for which resources by setting IAM policies. IAM policies grant specific roles to a project member, which gives the identity certain permissions. For example, for a given resource, such as a project, you can assign the `roles/biglake.admin` role to a Google Account and that account can control Lakehouse resources in the project, but cannot manage other resources. You can also use IAM to manage the basic roles granted to project team members.

## Access control options for users

To let users create and manage your Lakehouse resources, you can add them as _team members_ to your project or to specific resources and grant them permissions using IAM _roles_.

A team member can be an individual user with a valid Google Account, a Google Group, a service account, or a Google Workspace domain. When you add a team member to a project or to a resource, you specify which roles to grant them. IAM provides three types of roles: [predefined roles](https://docs.cloud.google.com/iam/docs/overview#roles), [basic roles](https://docs.cloud.google.com/iam/docs/overview#roles), and [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

To see a list of the capabilities of each Lakehouse role and the API methods that a specific role grants permission to, see [borderless Lakehouse IAM roles](https://docs.cloud.google.com/lakehouse/docs/iam-roles).

For other member types, such as service accounts and groups, see the [Policy binding reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#binding).

## Service accounts

When you call Lakehouse APIs to perform certain actions in a project where your service is located, Lakehouse performs these actions on your behalf by using a per-catalog [Service Agent service account](https://docs.cloud.google.com/iam/docs/service-agents#biglake-iceberg-rest-catalog-api-service-agent). Examples include accessing Cloud Storage buckets for [credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending) and retrieving secret data from Secret Manager for [cross-cloud data access](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access).

## IAM policies for resources

You can grant access to Lakehouse resources by attaching IAM policies directly to those resources, such as a Lakehouse service. An IAM policy lets you manage IAM roles on those resources instead of, or in addition to, managing roles at the project level. This gives you flexibility to apply the principle of least privilege, which is to grant access only to the specific resources that collaborators need to do their work.

Resources also inherit the policies of their parent resources. If you set a policy at the project level, it's inherited by all its child resources. The effective policy for a resource is the union of the policy set at that resource and the policy inherited from higher up in the hierarchy. For more information, see the [IAM policy hierarchy](https://docs.cloud.google.com/iam/docs/overview#policy_hierarchy).

You can get and set IAM policies using the Google Cloud console, the Identity and Access Management API, or the Google Cloud CLI.

  * For the Google Cloud console, see [Access control with the Google Cloud console](https://docs.cloud.google.com/iam/docs/grant-role-console).
  * For the API, see [Access control via the API](https://docs.cloud.google.com/iam/docs/reference/rest).
  * For the Google Cloud CLI, see [Access control with the Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/iam).



## What's next

  * Learn more about [Lakehouse IAM roles](https://docs.cloud.google.com/lakehouse/docs/iam-roles).
  * Learn how to set [policies at a project level](https://docs.cloud.google.com/iam/docs/managing-policies).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
