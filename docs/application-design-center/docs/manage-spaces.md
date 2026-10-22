---
url: https://docs.cloud.google.com/application-design-center/docs/manage-spaces/
title: Manage and assign spaces \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:54.723103+00:00
---

# Manage and assign spaces  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/manage-spaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Manage and assign spaces Stay organized with collections  Save and categorize content based on your preferences. 

A space is an isolated area where a team collaborates to create templates and deploy applications. Administrators can assign a space to a development team, where the team can view templates and applications that other space members create.

The templates and applications that users create in a space are only available in that space. An administrator can share templates with other spaces by adding templates to a catalog and sharing that catalog across spaces.

## Before you begin

To perform the tasks in this document, ask your administrator to grant you the necessary roles on the [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder) or [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project), as listed in the following table:

Task | Required roles  
---|---  
Select, view, and manage spaces across regional management boundaries | Application Design Center Admin (`roles/designcenter.admin`)  
Perform initial setup or create new spaces | Application Design Center Admin (`roles/designcenter.admin`)  
Manage space user permissions and assign IAM roles | Application Design Center Admin (`roles/designcenter.admin`)  
  
For more information about roles, see [Access control with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).

Before you manage spaces, do the following:

  * Make sure that you have the [Application Design Center Admin (`roles/designcenter.admin`)](https://docs.cloud.google.com/application-design-center/docs/access-control) IAM role on the [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder) or [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project).

  * Complete the App Design Center [_initial setup_](https://docs.cloud.google.com/application-design-center/docs/setup) to create and name an initial space.




## Select a region

You created the following spaces when you set up App Design Center in your [application management boundary](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-mgmt-boundary):

  * A named _initial space_.
  * A default space in each [region where App Design Center is available](https://docs.cloud.google.com/application-design-center/docs/locations).
  * A space in a global region.



Each supported region in your application management boundary has a single space. You can create templates, components, and application drafts in each space. When application developers deploy these drafts, the application continues to be managed from the originating space, but the underlying Google Cloud resources can be provisioned in any supported region.

To select a region and view its templates, applications, and catalog, do the following:

  1. From the App Design Center navigation menu, click the **Region** list to view [regions where App Design Center is available](https://docs.cloud.google.com/application-design-center/docs/locations).

  2. To open a region and view its space, click the region name.

  3. To view a summary of your spaces across regions, from the **Region** list, select **Manage regions**.

The number of templates and applications in each region is displayed. The table only includes regions that you've previously opened.

  4. To view the resources in another region, in the **Actions** column, click **Switch to this region**.




## Create spaces to share catalogs

You can assign a development team to each space in your [application management boundary](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-mgmt-boundary). However, you can't share a catalog between spaces in the same application management boundary. You can only share a catalog with a destination space that is in the same region as the source space, but located in a different application management boundary.

To set up App Design Center in another application management boundary with its own set of spaces, do the following:

  1. In the Google Cloud console, select an [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder) or project that's not the same as the folder or project where you initially set up App Design Center.

  2. Go to the **App Design Center Overview** page.

[Go to Overview](https://console.cloud.google.com/products/design-center/overview)

  3. Complete the [App Design Center initial setup](https://docs.cloud.google.com/application-design-center/docs/setup) for the new folder or project.

You can now [share a catalog](https://docs.cloud.google.com/application-design-center/docs/manage-catalogs#share-a-catalog-with-a-space) between spaces in distinct application management boundaries.




## Manage space users

Space users can collaborate to create templates and deploy applications. You add each user or group as a principal, and then assign roles to that principal to help them perform their duties. For example, you might assign the Application Design Center Admin (`roles/designcenter.admin`) role to a principal who needs to create and assign spaces, manage catalogs, and design templates.

To manage space user permissions:

  1. In the Google Cloud console, go to the **App Design Center Overview** page.

[Go to Overview](https://console.cloud.google.com/products/design-center/overview)

  2. From the navigation menu, select a space from the **Space** list.

  3. In the **Let your team use ADC** area, click **Manage permissions**.

  4. Click **Add principal** , and do the following:

     1. In the **New principals** field, enter the principals that you want to add to the space.

     2. From the **Select a role** list, click **Other**.

     3. From the **Roles** area, select the role that you want to assign to the selected principals.

For role descriptions, see [Access control with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).

     4. For each additional role that you want to assign to this principal, click **Add another role** and select a role.

     5. Click **Save**.

  5. To assign access for additional users in this space, click **Add principal** and assign the relevant roles.




## What's next

  * Define your own configurations by [designing application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).
  * Share your templates with other spaces by [managing template catalogs](https://docs.cloud.google.com/application-design-center/docs/manage-catalogs). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
