---
url: https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control/
title: Dataproc Metastore: Access control with IAM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:39:59.205856+00:00
---

# Dataproc Metastore: Access control with IAM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Dataproc Metastore: Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

By default, all Google Cloud projects come with a single user, the original project creator. No other users have access to the project, and therefore, access to Dataproc Metastore resources, until a user is added as a project member or is bound to a specific resource.

This page explains the ways you can add new users to your project and how to set access control for your Dataproc Metastore resources.

## What is IAM?

Google Cloud offers [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam), which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. IAM lets you adopt the [security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources.

IAM also lets you control who (identity) has what (roles) permission to which resources by setting IAM policies. IAM policies grant specific roles to a project member, giving the identity certain permissions. For example, for a given resource, such as a project, you can assign the `roles/metastore.admin` role to a Google Account and that account can control Dataproc Metastore resources in the project, but cannot manage other resources. You can also use IAM to manage the basic roles granted to project team members.

## Access control options for users

To give users the ability to create and manage your Dataproc Metastore resources, you can add users as _team members_ to your project or to specific resources and grant them permissions using IAM _roles_.

A team member can be an individual user with a valid Google Account, a Google Group, a service account, or a Google Workspace domain. When you add a team member to a project or to a resource, you specify which roles to grant them. IAM provides three types of roles: [predefined roles](https://docs.cloud.google.com/iam/docs/overview#roles), [basic roles](https://docs.cloud.google.com/iam/docs/overview#roles), and [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

To see a list of capabilities of each Dataproc Metastore role and API methods that a specific role grants permission to, review [Dataproc Metastore IAM roles](https://docs.cloud.google.com/dataproc-metastore/docs/iam-roles).

For other member types, such as service accounts and groups, refer to the [Policy binding reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#binding).

## Service accounts

When you call Dataproc Metastore APIs to perform actions in a project where your service is located, Dataproc Metastore performs these actions on your behalf by using a Service Agent service account that has the permissions required to perform the actions.

The following service accounts have the permissions required to perform Dataproc Metastore actions in the project where your service is located:

  * `service-CUSTOMER_PROJECT_NUMBER@gcp-sa-metastore.iam.gserviceaccount.com`.

**Note:** You may need to grant the [`storage.objectAdmin`](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) role to this service account for your Dataproc Metastore service to have access to its Hive metastore warehouse directory, if a non-default warehouse directory is provided. For more information, see [Hive Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore).



## IAM policies for resources

You can grant access to Dataproc Metastore resources by attaching IAM policies directly to those resources, such as a Dataproc Metastore service. An IAM policy lets you manage IAM roles on those resources instead of, or in addition to, managing roles at the project level. This gives you flexibility to apply the principle of least privilege, which is to grant access only to the specific resources that collaborators need to do their work.

Resources also inherit the policies of their parent resources. If you set a policy at the project level, it's inherited by all its child resources. The effective policy for a resource is the union of the policy set at that resource and the policy inherited from higher up in the hierarchy. For more information, read about the [IAM policy hierarchy](https://docs.cloud.google.com/iam/docs/overview#policy_hierarchy).

You can get and set IAM policies using the Google Cloud console, the IAM API, or the Google Cloud CLI.

  * For the Google Cloud console, see [Access control via the Google Cloud console](https://docs.cloud.google.com/iam/docs/grant-role-console).
  * For the API, see [Access control via the API](https://docs.cloud.google.com/iam/docs/reference/rest).
  * For the Google Cloud CLI, see [Access control via the Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/iam).



## What's next

  * Learn how to grant [fine-grained access to metadata when using gRPC](https://docs.cloud.google.com/dataproc-metastore/docs/grpc-endpoints)
  * Learn more about [IAM roles](https://docs.cloud.google.com/dataproc-metastore/docs/iam-roles).
  * Learn more about [IAM permissions](https://docs.cloud.google.com/dataproc-metastore/docs/iam-permissions).
  * Learn how to set [policies at a project level](https://docs.cloud.google.com/iam/docs/managing-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
