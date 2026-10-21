---
url: https://docs.cloud.google.com/dataform/docs/vpc-service-controls/
title: Configure VPC Service Controls \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:39.611507+00:00
---

# Configure VPC Service Controls  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Configure VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

VPC Service Controls is a Google Cloud feature that lets you set up a perimeter that helps guard against data exfiltration. This guide shows how to use VPC Service Controls with Dataform to help make your services more secure.

VPC Service Controls provides an extra layer of defense for Google Cloud services that is independent of the protection provided by Identity and Access Management (IAM).

To learn more about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Limitations

Dataform supports VPC Service Controls with the following limitations:

  * You must set the [`dataform.restrictGitRemotes` Organization Policy Service](https://docs.cloud.google.com/dataform/docs/restrict-git-remotes).
  * Dataform and BigQuery must be restricted by the same VPC Service Controls service perimeter.
  * To allow users to authenticate with the user credentials for their Google Account when scheduling or manually triggering runs, you must add their user identities to your ingress rules. For more information, see [Updating ingress and egress policies for a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#updating) and [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).



### Security considerations

When you set up a VPC Service Controls perimeter for Dataform, make sure that you review the permissions granted to your custom service accounts to verify that they match your security architecture.

Depending on the permissions that you grant to the custom service account, that service account might have access to BigQuery or Secret Manager data in the project that the service account belongs to, regardless of VPC Service Controls. In such a case, restricting Dataform with a VPC Service Controls perimeter doesn't block communication with BigQuery or Secret Manager.

You should block communication with BigQuery if you don't need to run any workflow invocations originating from your Dataform repositories. For more information about blocking communication with BigQuery, see Block communication with BigQuery.

You should block communication with Secret Manager if none of your Dataform repositories connect to a third-party Git repository. For more information about blocking communication with Secret Manager, see Block communication with Secret Manager.

## Before you begin

Before you configure a VPC Service Controls service perimeter for Dataform, follow the [Restrict remote repositories](https://docs.cloud.google.com/dataform/docs/restrict-git-remotes) guide to set the `dataform.restrictGitRemotes` Organization Policy.

The `dataform.restrictGitRemotes` Organization Policy is required to ensure that VPC Service Controls checks are enforced when using Dataform and that third-party access to Dataform Git repositories is restricted.

### Required roles

To get the permissions that you need to configure a VPC Service Controls service perimeter, ask your administrator to grant you the [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about VPC Service Controls permissions, see [Access control with IAM](https://docs.cloud.google.com/vpc-service-controls/docs/access-control).

## Configure VPC Service Controls

You can restrict Dataform with a VPC Service Controls service perimeter in the following ways:

  * Add Dataform to an existing service perimeter that restricts BigQuery.
  * Create a service perimeter that restricts both Dataform and BigQuery.

**Important:** Dataform and BigQuery must be restricted by the same service perimeter.

To add Dataform to a service perimeter that restricts BigQuery, follow the [Update a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) guide in the VPC Service Controls documentation.

To create a new service perimeter that restricts both Dataform and BigQuery, follow the [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) guide in the VPC Service Controls documentation.

## Optional: Block communication with BigQuery

Custom service accounts use the following permissions and roles to communicate with BigQuery:

  * The`bigquery.jobs.create` permission, granted to the custom service account.
  * The [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) (`roles/iam.serviceAccountTokenCreator`), granted to the default Dataform service agent on the custom service account.



You can block communication between a custom service account and BigQuery in either of the following ways:

  * Revoke all predefined and custom roles granted at the project level to the custom service account that contain the `bigquery.jobs.create` permission. The `bigquery.jobs.create` permission is included in the following predefined [BigQuery IAM roles](https://docs.cloud.google.com/bigquery/docs/access-control):

    * [BigQuery Admin](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.admin) (`roles/bigquery.admin`)
    * [BigQuery Job User](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser) (`roles/bigquery.jobUser`)
    * [BigQuery User](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.user) (`roles/bigquery.user`)
    * [BigQuery Studio Admin](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)
    * [BigQuery Studio User](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.studioUser) (`roles/bigquery.studioUser`)

To revoke roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  * Revoke the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) (`roles/iam.serviceAccountTokenCreator`), granted to the default Dataform service agent on the selected custom service account. To revoke the Service Account Token Creator role, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).




## Optional: Block communication with Secret Manager

Dataform uses the `secretmanager.versions.access` permission to access individual Secret Manager secrets. You give this permission to the default Dataform service agent on a selected Secret Manager secret when you [connect a Dataform repository to a third-party repository](https://docs.cloud.google.com/dataform/docs/connect-repository).

To block communication between Dataform and Secret Manager, you need to revoke access to all secrets from the default Dataform service agent.

To revoke access to a Secret Manager secret from the default Dataform service agent, follow the [Manage access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets) guide in the Secret Manager documentation. You must revoke all predefined and custom roles that contain the `secretmanager.versions.access` permission, granted to the default Dataform service agent on the selected secret.

The `secretmanager.versions.access` permission is included in the following predefined [Secret Manager IAM roles](https://docs.cloud.google.com/secret-manager/docs/access-control):

  * [Secret Manager Admin (`roles/secretmanager.admin`)](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.admin)
  * [Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`)](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.secretAccessor)
  * [Secret Manager Secret Version Manager (`roles/secretmanager.secretVersionManager`)](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.secretVersionManager)



## What's next

  * To learn more about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * To learn more about the Organization Policy, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).
  * To learn more about service accounts in Dataform, see [About Dataform service agents and custom service accounts](https://docs.cloud.google.com/dataform/docs/access-control#about-service-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
