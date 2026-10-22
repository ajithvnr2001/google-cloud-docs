---
url: https://docs.cloud.google.com/data-studio/roles-and-permissions/
title: Roles and permissions \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:39.657444+00:00
---

# Roles and permissions  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/roles-and-permissions/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

Access to Data Studio assets (reports and data sources) is based on the Google Cloud Identity and Access Management (IAM) system. With IAM, you manage access to Data Studio assets by assigning users to a predefined _role_. A role is a collection of _permissions_ that allows users to perform certain actions while preventing them from performing other actions.

[Learn more about IAM](https://docs.cloud.google.com/iam/docs/overview).

**Tip:** Roles and permissions don't govern who can actually see the data that is provided by a data source. This is governed by [data credentials](https://docs.cloud.google.com/data-studio/data-credentials).

For assets in team workspaces or folders, sharing capabilities may be restricted by organizational policies. See [Organizational sharing policies](https://docs.cloud.google.com/data-studio/invite-others-to-your-reports#organizational-sharing-policies) for details.

Changes to IAM permissions and roles may cause a propagation latency, and report content may temporarily be visible to users whose access has been removed. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Basic roles

The following basic roles are available to all Data Studio users. Basic roles apply to individual assets. For example, you can grant a user the **Editor** role on a particular report and the **Viewer** role on the data source that is added to that report.

Role  |  General capabilities   
---|---  
**Viewer** | 

  * Can view the report and interact with controls 
  * Can view the data source schema 

  
**Editor** |  All the capabilities of the **Viewer** role, plus the following capabilities: 

  * Can modify the report 
  * Can modify the data source 
  * Can share the report 
  * Can share the data source 

  
**Owner** |  All the capabilities of the **Editor** role, plus the following capabilities: 

  * Can delete the report or data source 
  * Can make someone else the owner of the report or data source 

  
  
See Role details for more granular capabilities.

## Team workspace roles

The following roles are available to users of Data Studio Pro whose organization has a Google Cloud project linked through the Admin console. Team workspace roles are applied at the workspace level and govern access to the assets that are contained in that workspace.

Role  |  General capabilities   
---|---  
**Viewer** | 

  * Can view existing assets in the team workspace 
  * Can view folders in the team workspace 
  * Can view the team workspace Trash 

  
**Contributor** |  All the capabilities of the **Viewer** role, plus the following capabilities: 

  * Can edit existing assets in the team workspace 
  * Can create new assets in the team workspace 
  * Can create new folders in the team workspace 
  * Can move assets to team workspaces and folders in team workspaces 
  * Can view workspace members and roles 
  * Can add editors and viewers directly to an asset inside a workspace 
  * Can restore assets from the Trash 
  * Can move assets from **Sandbox/Owned by me** to a team workspace 

  
**Content manager** |  All the capabilities of the **Contributor** role, plus the following capabilities: 

  * Can add/remove contributors to/from the workspace 
  * Can move assets in a team workspace between folders that are located in the same team workspace 
  * Can rename folders in the team workspace 
  * Can remove assets to the Trash 

  
**Manager** |  All the capabilities of the **Content manager** role, plus the following capabilities: 

  * Can add/remove Contributors and Content managers to/from the workspace 
    * ( **Note** : A workspace must have at least one Manager.) 
  * Can change member access levels for a team workspace 
  * Can move an asset from one folder in a team workspace to a folder in a different team workspace 
  * Can move assets out of a team workspace to **Sandbox/Owned by me**
  * Can permanently delete a folder in a team workspace 
  * Can permanently delete an asset, a folder, or a team workspace 

  
  
## Role details

The following tables show the granular capabilities of each role according to feature area.

**Tip:** To see individual IAM permissions, visit [IAM permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference) and search for `datastudio`. Note that Data Studio does not support custom roles.

### Feature area: Reports

Capability  |  Basic roles  |  Team workspace roles   
---|---|---  
Viewer  |  Editor  |  Owner  |  Viewer  |  Contributor  |  Content manager  |  Manager   
Create the report  |  |  |  ✔  |  |  ✔  |  ✔  |  ✔   
Remove the report (move to Trash)  |  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
Restore from Trash  |  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
Delete the report  |  |  |  ✔  |  |  |  |  ✔   
View the report  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔   
Copy the report  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔   
Download data from the report  |  ✔  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
Modify the report  |  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
Use data from added data sources  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔   
Modify data from added data sources  |  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
Add and remove data sources  |  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
Prevent report copying for viewers  |  |  |  ✔  |  |  ✔  |  ✔  |  ✔   
Prevent report sharing for viewers  |  |  |  ✔  |  |  ✔  |  ✔  |  ✔   
Prevent downloading data for viewers  |  |  |  ✔  |  |  ✔  |  ✔  |  ✔   
Transfer ownership  |  |  |  ✔  |  n/a  |  n/a  |  n/a  |  n/a   
**Note:** The role capabilities listed previously refer specifically to reusable data sources. For [embedded data sources](https://docs.cloud.google.com/data-studio/embedded-data-sources), people with the Editor role on the report can view and modify the data source.

### Feature area: Data sources

Capability  |  Basic roles  |  Team workspace roles   
---|---|---  
Viewer  |  Editor  |  Owner  |  Viewer  |  Contributor  |  Content manager  |  Manager   
Add the data source to reports  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔   
View the data source schema  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔   
Modify the data source  |  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
Copy the data source  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔   
Remove the data source (move to Trash)  |  |  ✔  |  ✔  |  |  |  ✔  |  ✔   
Restore from Trash  |  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
Permanently delete the data source  |  |  |  ✔  |  |  |  |  ✔   
Change data source credentials  |  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
Prevent data source copying  |  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
Transfer ownership  |  |  |  ✔  |  n/a  |  n/a  |  n/a  |  n/a   
  
### Feature area: Sharing

These capabilities apply to both reports and data sources, unless otherwise specified.

Capability  |  Basic roles  |  Team workspace roles   
---|---|---  
Viewer  |  Editor  |  Owner  |  Viewer  |  Contributor  |  Content manager  |  Manager   
Share the asset directly  |  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
Stop sharing the asset directly  |  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
Create and edit schedules on reports  |  |  ✔  |  ✔  |  |  ✔  |  ✔  |  ✔   
**Note:** Viewers can also create and edit schedules if they are granted [scheduling permissions](https://docs.cloud.google.com/data-studio/invite-others-to-your-reports) by an Editor or Owner.

### Feature area: Team workspaces

These capabilities apply only to Data Studio Pro team workspace roles. Basic roles are not applicable. 

Capability  |  Team workspace roles   
---|---  
Viewer  |  Contributor  |  Content manager  |  Manager   
View workspace membership  |  |  ✔  |  ✔  |  ✔   
View workspace assets  |  ✔  |  ✔  |  ✔  |  ✔   
View workspace folders  |  ✔  |  ✔  |  ✔  |  ✔   
Edit workspace and folder assets  |  |  ✔  |  ✔  |  ✔   
Create new workspace assets  |  |  ✔  |  ✔  |  ✔   
Create new workspace folders  |  |  ✔  |  ✔  |  ✔   
View the workspace Trash  |  ✔  |  ✔  |  ✔  |  ✔   
Restore workspace and workspace folder assets from the Trash  |  |  ✔  |  ✔  |  ✔   
Move assets from **Sandbox/Owned by me** to a team workspace or workspace folder  |  |  ✔  |  ✔  |  ✔   
Move assets out of a team workspace or workspace folder to **Sandbox/Owned by me** , to a different team workspace, or to a folder in a different workspace  |  |  |  |  ✔*   
Move assets between a team workspace and its child folders  |  |  |  ✔  |  ✔   
Add members to / remove members from the team workspace  |  |  |  ✔**  |  ✔   
Change member roles for the team workspace  |  |  |  |  ✔   
Permanently delete a workspace folder  |  |  |  |  ✔   
Permanently delete the workspace  |  |  |  |  ✔   
  
* If a Manager is moving an asset from one team workspace to another team workspace, they must have one of the three roles in the target team workspace.

** Content managers can add or remove Contributors.

## Related resources

  * [About team workspaces](https://docs.cloud.google.com/data-studio/about-team-workspaces)
  * [Organize assets with folders in team workspaces](https://docs.cloud.google.com/data-studio/organize-assets-with-folders-in-team-workspaces)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
