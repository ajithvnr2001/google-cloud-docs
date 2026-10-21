---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/users-roles-overview/
title: Users and roles \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:01:32.088668+00:00
---

# Users and roles  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/users-roles-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Users and roles Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

A _user_ represents an authenticated account that can access an organization and the entities within that organization, such as the environments, API proxies, and keystores.

To add a new user to your Apigee organization, you grant access to the user's _account,_ first in the Cloud project and then in the Apigee UI. (This document uses the terms _user_ and _user account_ interchangeably.)

When you add a new user, you typically:

  1. **In the Console** , assign the new user to one or more roles in your Cloud project. This gives the user broad access to all environments in the organization. 

For more information, see [Managing access in the Console](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-access).

  2. **In the Apigee UI** , grant additional user roles in one or more environments in your Apigee organization. Note that environment-scoped user roles do not supersede roles granted at the Google Cloud level; they are additive. 

For more information, see [Manage users in the Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-users).


**Note:** You do not have to assign the same role for a user in the Apigee UI for each environment that you assigned to the user for the Cloud project.

## About roles

The capabilities that you grant to the user account depend on the type of _role_ that you assign to them. A role is a collection of [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions). You cannot grant a permission to the user directly. Instead, you grant them a role. For example, you might assign a developer to the role of `API Admin` so that they can create API proxies, KVM, and shared flows. For someone that will deploy proxies, you might assign them to the role of `Environment Admin`, which grants them the ability to deploy and undeploy API proxy revisions. For details about all Apigee roles, see [Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles).

Additionally, the resources that a user can access based on their role depends on _where_ you assigned the role:

  * **Google Cloud project** \- If you assign a role in the Console (on the Google Cloud project), then the user can access all Apigee resources— _all environments and resources within those environments_ —in that role. This is because the Cloud project is the _parent_ of the Apigee UI in the resource hierarchy; the permissions set on the parent (the Cloud project) are inherited by all children (environments). You can refine this access by specifying user roles on a _per environment_ basis in the Apigee UI. 

Access control in Google Cloud Platform is controlled by Identity and Access Management (IAM). IAM lets you set permissions specifying **who** has **what** kind of access to **which** resources in your project. For more information, see [Concepts related to identity](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity).

Users are a type of _principal_ , a broad term that refers to an identity that can be granted access to resources. Other types of Cloud principals include service accounts, Google groups, and G Suite domains. For more information, see [this overview](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity) of Cloud Identity and Access Management.

  * **Environment access** \- Granting a user role for a specific environment does not supersede roles set at the Google Cloud project level. At the environment level, roles granted to a user are represented as a union with any Cloud roles assigned to the user.



For example, if you define a user as an `API Admin` on the Cloud project, then that user will have access—as an `API Admin`— to all environments in your organization.

### Role recommendations

Apigee recommends that you do the following for each new user account that you add. (When adding _super users_ or administrators, this is not necessary.):

  1. In the Console, add the new user account and select a role that has a minimal set of permissions. For example, set the role of a new user to `API Admin`. See [Managing access in Google Cloud](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-access).
  2. In the Apigee UI's **Environment Access** view, add the user and set any additional user roles for each environment in the organization as described in [Manage users](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-users). Note that environment-scoped roles set in the Apigee UI do not supersede roles set at the Google Cloud level, they are additive.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
  *[KVM]: Key Value Map
