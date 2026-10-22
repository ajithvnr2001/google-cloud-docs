---
url: https://docs.cloud.google.com/data-studio/best-practices-and-tips-for-using-team-workspaces/
title: Best practices and tips for using team workspaces \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:46.187664+00:00
---

# Best practices and tips for using team workspaces  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/best-practices-and-tips-for-using-team-workspaces/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Best practices and tips for using team workspaces Stay organized with collections  Save and categorize content based on your preferences. 

**Data Studio Pro feature**

The features and functionality described in this page are available to Data Studio Pro users.

[Get Data Studio Pro.](https://docs.cloud.google.com/data-studio/about-pro)

This page describes best practices, tips, and common use cases for working with [team workspaces](https://docs.cloud.google.com/data-studio/about-team-workspaces). The information on this page will help you create and use team workspaces efficiently and confidently and share content only as necessary. This page also provides examples of common naming conventions and scenarios.

## Create team workspaces with a specific purpose or focus

Create and organize your team workspaces with a specific focus or purpose in mind. This can help you achieve the following:

  * Keep team workspaces organized and efficient to maintain.
  * Help users more quickly and conveniently access the information they need.



For example, you could implement the following structure to keep your team workspaces organized and efficient:

  * One team workspace for each cross-functional project that contains shared assets
  * Separate team workspaces for each team or geography, like marketing in APAC, that contain each team's specific assets
  * Separate team workspace for reporting environments, like development, staging, or production reports



For more specific guidance, see the examples in Common use cases for team workspaces.

## Manage membership with Google Groups

Google Groups can help you manage team workspace membership by automatically granting group members access to the team workspaces that the group has access to. This approach has two main advantages:

  * New group members have the same access to reports and data sources as do existing group members.
  * You don't have to manually configure access for each new member.



## Share content selectively

The following tips can help you share the content within team workspaces intentionally.

  * **Give only the necessary permissions to each user.**

When you add people or groups to a team workspace, those people will be able to create, add, and view assets within that team workspace. For people who need to also be able to add and remove team workspace members, give them the Content manager or Manager role as needed.

  * **Share individual assets for limited access.**

If someone needs access to only a certain report or data source within a team workspace, you can share only that asset rather than making them a member of the team workspace.




See [Roles and permissions](https://docs.cloud.google.com/data-studio/roles-and-permissions) for more information about the different team workspace roles in Data Studio.

## Use naming conventions

To help people find team workspaces and to avoid naming conflicts in team workspaces, agree on organization-wide naming conventions. For example:

  * Your company has sales divisions in different regions and you create a team workspace for each sales region. To differentiate the team workspaces, prefix them with the region or an abbreviation of the region.
  * You can indicate status by adding a prefix, such as **[Archive]** , to a project that's no longer active or **[In Progress]** to a project that's active.
  * To distinguish between team workspaces that are shared externally and those that are shared internally, add the prefix **[External]** or **[Internal]**.
  * Use labels to indicate the purpose of the team workspace, such as **[Pre-prod]** for a team workspace that contains pre-production assets and **[Prod]** for a team workspace that contains production assets. Labels can help team members understand the purpose of the workspace and what type of assets each team workspace contains.



## Common use cases for team workspaces

This section includes some examples of how to use the principles outlined in this document to make effective and efficient use of team workspaces.

### Example: Team collaboration

Suppose you want all members of a Marketing team to have a shared space where they can create and access marketing content like reports and data sources. To create this collaborative space for the team, follow these steps:

  1. [Create a team workspace](https://docs.cloud.google.com/data-studio/create-edit-and-delete-team-workspaces) that is dedicated to the Marketing team's assets.
  2. [Add the members](https://docs.cloud.google.com/data-studio/manage-team-workspace-assets) of the Marketing team to that team workspace.
  3. Provide the team members with the Contributor role for the team workspace. This access will allow them to add new content and update existing assets within the team workspace.
  4. Provide leads and others who need to be able to add or remove team workspace members with the Content manager role.



### Example: Environment management (Dev/QA/Prod)

In this example, suppose you have a central data team that creates content to be shared with the entire company. You can leverage team workspaces to structure your Data Studio Pro content across different stages of your development lifecycle, such as Development, QA, and Production.

To allow the team to control how content is shared during the development process and when it's ready for production, follow these steps:

  1. Create a separate team workspace for each environment, with titles like **BI - Dev** , **BI - QA** , and **BI - Prod**. Pre-production content that's developed by the central data team can be stored in the development or QA workspaces.
  2. To promote reports and data sources from one environment to another (for example, Dev to QA), you'll typically copy the asset from the source workspace and paste it into the target workspace. You may also need to reconfigure data sources to point to the appropriate data environment (for example, a development database versus a production database).
  3. Once the content is ready to be shared company-wide, people with the Manager role can move or copy it to the production workspace (**BI - Prod**).



### Example: Ad campaign

Suppose you are working on an ad campaign for a specific client, and you want to manage all client-related content in a single place.

To do this, follow these steps:

  1. Create a team workspace dedicated to the client's ad campaign.
  2. Add people who are working on the ad campaign to the team workspace and assign roles based on the following criteria: 
     * **Contributor role:** Members who need to be able to contribute to the project but who don't need to be able to manage member access
     * **Content manager role or the Manager role:** People who need to be able to manage access, such as the team lead



This will ensure that all relevant information is in one place and that only those who need to see it have access.

### Example: Standard templates

Suppose your company has published reports and metrics for different analyses, like customer support reports, marketing campaign reports, company-wide OKR reports, and project updates.

You can create templates that users can copy and customize to make it easier for people to build their own customized reports. To create a team workspace that is dedicated to standard templates, follow these steps:

  1. Create a team workspace dedicated to the standard templates.
  2. Move the key reports, published reports, or data sources into this workspace.
  3. Add the key people who are responsible for updating and maintaining the templates as Content managers.
  4. Add a company-wide Google Group as a viewer on the reports. This lets everyone in the company view these reports without modifying the template, as well as make use of and customize their copy of the report.



This will ensure everyone has access to the templates and that they don't make any accidental changes.

## Related resources

  * [About team workspaces](https://docs.cloud.google.com/data-studio/about-team-workspaces)
  * [Create, edit, and delete team workspaces](https://docs.cloud.google.com/data-studio/create-edit-and-delete-team-workspaces)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
