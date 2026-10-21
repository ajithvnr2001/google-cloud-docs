---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles/
title: Apigee roles \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:16:45.842995+00:00
---

# Apigee roles  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee roles Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section describes the Apigee-specific roles that you commonly assign to your users. These are not the same roles that you assign to [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).

**Note:** For more information on users and roles in Apigee, see [Users and roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/users-roles-overview). For information on permissions for service accounts, see [ About service account permissions](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview#about-service-account-permissions). 

## Apigee-specific roles

Apigee provides a set of predefined (or _curated_) roles that are Google Cloud IAM roles for Apigee. Among other permissions, these predefined roles allow users to:

  * Get and list Apigee organizations
  * Get and list Apigee environments
  * Get and list Google Cloud projects



### Project-level vs. environment-level roles

In Apigee, you can grant roles at different levels of the resource hierarchy to control the scope of a user's access:

  * **Project-level:** Assigning a role at the Google Cloud project level grants that user permissions across all Apigee organizations and environments within that project.
  * **Environment-level:** Assigning a role at the environment level restricts the user's permissions to a specific environment (e.g., "Prod" but not "Dev"). This is done using the `SetIamPolicy` method on the environment resource.



For example, you can grant a user the **API Reader** role for a specific environment to make them a read-only admin for only that environment.

## Primary Apigee roles

The following table summarizes the main Apigee roles.

**Note:** For a complete list of all Apigee roles and their specific permissions, see [Apigee roles](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee).Role Name | Description  
---|---  
[`Analytics Editor`](https://docs.cloud.google.com/iam/docs/understanding-roles#apigee.analyticsEditor) | Creates and analyzes reports on API proxy traffic for an Apigee organization. Can edit queries and reports.  
[`API Admin` (V2)](https://docs.cloud.google.com/iam/docs/understanding-roles#apigee.apiAdminV2) | A developer that creates and tests API proxies. This role gives full read/write access to API products and apps, as well as API proxies, shared flows, and KVMs. This role replaces the deprecated `API Creator` role.  
[**API Reader** (V2)](https://docs.cloud.google.com/iam/docs/understanding-roles#apigee.apiReaderV2) | Provides read-only access to most Apigee features, including API products, environment groups, environments, KVMs, proxies, shared flows, and more. **Note:** Although API Reader includes permissions such as `apigee.proxyrevisions.deploy` and `apigee.sharedflowrevisions.deploy`, it is _read-only_ and includes only the read-specific aspects of those functions.  
[`Analytics Viewer`](https://docs.cloud.google.com/iam/docs/understanding-roles#apigee.analyticsViewer) | Views analytics data for an organization. This role can get environment stats.  
[`Environment Admin`](https://docs.cloud.google.com/iam/docs/understanding-roles#apigee.environmentAdmin) |  This role gives full read/write access to Apigee environment resources, including flow hooks, keystores, KVMs, shared flows, and target servers. For a full listing of permissions for this role, see [Apigee roles](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee) in the Cloud IAM documentation. **Note:** Deploying an API proxy requires two permissions: 

  * `apigee.deployments.create`: This permission is granted by the Environment Admin role at the environment level.
  * `apigee.proxyrevisions.deploy`: This permission is included in the API Reader role. Because API Reader is an organization-level role, you must grant it in the Google Cloud console at the project level.

  
[`Developer Admin`](https://docs.cloud.google.com/iam/docs/understanding-roles#apigee.developerAdmin) | Manages developer access to apps. This role can read API products and can edit app keys, developer apps, and developers. This role also manages AppGroups.  
[`Org Admin`](https://docs.cloud.google.com/iam/docs/understanding-roles#apigee.admin) | A super user with full access to all Apigee resources in the Apigee organization. This role can access all available actions for all API proxies. This is the only role that can create, delete, or update organizations.  
[`Read Only Admin`](https://docs.cloud.google.com/iam/docs/understanding-roles#apigee.readOnlyAdmin) | An administrator who can run reports and view everything in the Apigee organization without the ability to create or change anything. This role has read access to all Apigee resources within the Apigee organization. Your Google Cloud project's service account is assigned this role during setup and installation.   
  
## View and manage roles

You can view and manage these roles in the IAM **Roles** view within the Google Cloud console.

In the Google Cloud console, go to the **Identify & Access > Roles** page.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

For a complete list of API permissions for each role, see [Apigee roles](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee).

**Note:** If you create a role in the **IAM & Admin > Roles** page, be sure to include the permission `apigee.projectorganizations.get` in the role.

In addition to the Apigee roles, you also apply Google Cloud roles such as Logs Writer and Storage Object Admin to your users.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
