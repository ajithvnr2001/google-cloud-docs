---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams/
title: Managing developer teams (Preview) \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:19:34.437134+00:00
---

# Managing developer teams (Preview)  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Managing developer teams (Preview) Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Preview — Apigee integrated portal**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Enrolling in the Preview release of the developer teams feature

To manage developer teams, you must enroll in the Preview release of the developer team feature.

To enroll in the team feature:

  1. In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click a portal name.

  3. Click **Audiences**.

  4. Click **Enroll**.




## Understanding teams

Teams allow developers (portal users) to share responsibility for an app with other developers. Apps that are owned by a team are accessible to all members of the team based on their [developer team role](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#roles).

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/teams.png)

As shown in the figure, Developer A is able to access the developer apps that they have created. In addition, as a member of Team A, Developer A shares responsibility for the apps owned by the team. As an Owner, Developer A has full read and write privileges for developer team members, developer team details, and apps.

**Note:** The maximum number of developer teams that a user can be a member of is **64**.

## How do I create a team?

As an API provider, you do not create a team. Portal users create and manage teams on your portal, as described in [Sharing responsibility for an app using developer teams (Preview)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#teams).

You can view team details and membership, assign a team to an audience, and approve or revoke team access to an app, as described in the following sections.

## Exploring the Teams page

The Teams page lists the developer teams created by portal users for a developer program.

To access the developer Teams page:

  1. Display the list of portals:

In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click the row of the portal for which you want to view teams.

  3. Click **Accounts**.

  4. Click the **Teams** tab.




## Viewing developer team details

To view developer team details:

  1. Access the Teams page.
  2. Click the team for which you want to view details.



The Team page is displayed.

The Team details page lists the following details for the team:

  * Team details such as name, description, main point of contact, and date created
  * Team members
  * Apps assigned to the team
  * Audiences to which the team is assigned



From the Teams page, you can perform the following tasks:

  * Assign a team to an audience
  * Approve or revoke team access to an app



## Assigning a team to an audience

After a portal user creates a team on your portal, you may want to assign the team to an audience to enable access to a set of specific resources. For example, you may want to allow access by the team to a set of Preview features.

To assign a team to an audience:

  1. Access the Teams page.
  2. Click the team for which you want to view details.
  3. To assign the team to an audience:

     1. Click edit **Edit**.
     2. Select an audience. **Note:** See [Adding an audience](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience#adding_an_audience) if none are listed.
     3. Click **Save**.
  4. To remove a team from an audience:

     1. Click edit **Edit**.
     2. Clear one or more checkboxes.
     3. Click **Save**.



## Approving or revoking team access to an app

To approve or revoke team access to an app:

  1. Access the Teams page.
  2. Click the team for which you want modify.
  3. Click the **App Name**.
  4. Click edit **Edit**.
  5. In the **App Status** section, select **Approved** or **Revoked**.
  6. Click **Save**.



## Viewing team membership by user

View the team membership for each portal user by viewing the user details, as described in [Viewing user account details](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users#view-user-details).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
