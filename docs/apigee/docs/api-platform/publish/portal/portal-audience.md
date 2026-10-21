---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience/
title: Manage the audiences for your portal (Preview) \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:42:13.275833+00:00
---

# Manage the audiences for your portal (Preview)  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage the audiences for your portal (Preview) Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Preview — Apigee integrated portal**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Enrolling in the Preview release of the audience management feature

To manage audiences, you must enroll in the Preview release of the audience management feature.

To enroll in the audience management feature:

  1. In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click a portal name.

  3. Click **Audiences**.

  4. Click **Enroll**.




## Understanding audiences

Using audiences, you can segment portal users or developer teams to control access to the following resources:

  * Pages in your portal
  * Published API products 



The following figure shows how audiences are used to control access to a set of resources.

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/audiences.png)

As shown in the figure, as an authenticated portal user, User A is able access the resources available through the public API program. In addition, as a member of Team A, User A inherits the entitlements from the Preview Users audience and is able to access the resources available through this restricted API program.

For restricted API programs, the API provider is responsible for advertising the program and processing access requests from portal users.

The following sections describe how to manage audiences and configure audience entitlements, and the audiences that are available by default.

## About the default audiences

The following two audiences are defined, by default.

Audience  | Assignments   
---|---  
Anonymous users  | All users that are not signed in to the portal.  
**Note** : This audience is not displayed in the Apigee UI as an audience.   
Authenticated users  | All users that are registered and signed in to the portal.  
**Note** : You can customize the entitlements for the authenticated users audience, but audience assignment is defined by default.   
  
## Exploring the Audiences page

To access the Audiences page:

  1. Display the list of portals:

In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click the row of the portal for which you want to view audiences.

  3. Click **Audiences**.

  4. Click the **Audiences** tab.




The Audiences page is displayed.

The Audiences page lets you:

  * View details for all audiences, including: 
    * Name
    * Description
    * Total number of team and individual portal user assignments
    * Creation date
  * Add an audience
  * Edit and delete an audience



You can also manage the resource entitlements for an audience when creating resources and [manage the default visibility for specific portal resources](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/default-audience).

## Adding an audience

**Note:** The maximum number of audiences that you can add is **16**.

To add an audience:

  1. Access the Audiences page.
  2. Add an Audience. 
     1. Click **\+ Audience**.
     2. Enter the name and description of the audience.
     3. Click **Save**.
  3. Manage the assignments for an audience.



## Manage the assignments for an audience

When adding or editing an audience, you can manage the developer teams and individual portal users assigned.

To manage the assignments for an audience:

  1. Access the Audiences page.
  2. Click the row of the audience for which you want to manage audience assignments.
  3. To add a team or individual portal user to an audience:

     1. Click edit **Edit**.
     2. Select members in the drop-down list.
     3. Click **Save**.
  4. To delete an audience assignment:

Click delete **Delete**.




## Managing the resource entitlements for an audience

When creating a portal page or publishing an API product, you can restrict access to the resource by assigning one or more audiences. When the visibility of that resource is set to **Selected audiences** , access is limited to the audiences to which the resource is assigned.

For more information, see:

  * [Manage the audience for a page in your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/page-editor#audience)
  * [Manage the audience for an API on your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#audience)



When viewing and editing an audience, you can view the resource entitlements assigned.

## Editing an audience

To edit an audience:

  1. Access the Audiences page.
  2. Click the row of the audience that you want to edit.
  3. Edit the audience details.

     1. Click edit **Edit**.
     2. Edit the name, description, or members.
     3. Click **Save**.
  4. Manage the developer teams and individual portal users assigned to an audience.

  5. In the **Content visibility entitlements** section, view the resource entitlements for an audience. See Manage the resource entitlements for an audience.




## Deleting an audience

To delete an audience:

  1. Access the Audiences page.
  2. Delete the audience.

     1. Click delete **Delete**.
     2. Click **Delete** to confirm the operation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
