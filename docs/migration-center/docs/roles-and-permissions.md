---
url: https://docs.cloud.google.com/migration-center/docs/roles-and-permissions/
title: Migration Center IAM roles and permissions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:39.008789+00:00
---

# Migration Center IAM roles and permissions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/roles-and-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Migration Center IAM roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

If you create the Google Cloud project where you want to use Migration Center, you already have all the permissions required to activate Migration Center and manage resources in the product.

When you add a new member to your project, you can use an [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) policy to give that member one or more IAM roles to control the actions that the member can perform in Migration Center.

This page describes the typical roles you might want to assign to your project members and the permissions required to perform various actions.

## Before you begin

  * Read the [IAM documentation](https://docs.cloud.google.com/iam).



## Roles and actions

There are three main categories of actions that you can perform in Migration Center:

  * Activate Migration Center.
  * Manage Migration Center resources.
  * View Migration Center resources.



As a best practice, assign members of your project the roles with the [least amount of privileges](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) required to perform the actions they need to perform.

### Create the Migration Center Additional Role

As a preliminary step before you assign roles to the members of your organization, create a custom role to simplify how you manage permissions. Follow these steps:

  1. In the Google Cloud console, go to **IAM & Admin > Roles**.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  2. Click add **Create role**

  3. In the **Create role** page, fill in the following fields:

     * **Title** : "Migration Center Additional Role"

     * **Description** : "Additional roles needed for Migration Center scenarios"

  4. Click add **Add permissions**.

  5. From the list of permissions, search for the following permissions and select them:

     * `iam.serviceAccountKeys.list`
     * `iam.serviceAccounts.list`
     * `resourcemanager.projects.update`
     * `serviceusage.services.enable`

Then, to add your permissions, click **Add**.

  6. To finish, click **Create**.




### Activate Migration Center

Before you can use Migration Center, you need to [activate it from the Google Cloud console](https://docs.cloud.google.com/migration-center/docs/get-started-with-migration-center#activate-migration-center). This one-time action includes activating the APIs and selecting a region to store your resources.

To get the permissions that you need to activate Migration Center, ask your administrator to grant you the following IAM roles on the project: 

  * Migration Center Admin (`migrationcenter.admin`) 
  * Migration Center Additional Role



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to activate Migration Center. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to activate Migration Center:

  * `migrationcenter.*`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `rma.*`
  * `resourcemanager.projects.update`
  * `serviceusage.services.list`
  * `serviceusage.services.enable`
  * `iam.serviceAccountKeys.list`
  * `iam.serviceAccounts.list`
  * `resourcemanager.projects.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Manage Migration Center resources

Managing Migration Center resources includes actions such as generating a cost estimate, creating a discovery client, and removing assets.

To get the permissions that you need to manage Migration Center resources, ask your administrator to grant you the following IAM roles on the project: 

  * Migration Center Admin (`migrationcenter.admin`) 
  * Migration Center Additional Role
  * Viewer (`viewer`) 
  * Service Account Key Admin (`iam.serviceAccountKeyAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage Migration Center resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage Migration Center resources:

  * `migrationcenter.*`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `rma.*`
  * `serviceusage.services.list`
  * `iam.serviceAccounts.list`
  * `iam.serviceAccountKeys.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### View Migration Center resources

To get the permissions that you need to view Migration Center resources, ask your administrator to grant you the following IAM roles on the project: 

  * Migration Center Viewer (`migrationcenter.viewer`) 
  * Viewer (`viewer`) 
  * Rapid Migration Assessment Viewer (`rma.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view Migration Center resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view Migration Center resources:

  * `migrationcenter.assets.get`
  * `migrationcenter.assets.list`
  * `migrationcenter.groups.get`
  * `migrationcenter.groups.list`
  * `migrationcenter.importJobs.get`
  * `migrationcenter.importJobs.list`
  * `migrationcenter.locations.*`
  * `migrationcenter.operations.get`
  * `migrationcenter.operations.list`
  * `migrationcenter.sources.get`
  * `migrationcenter.sources.list`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `serviceusage.services.list`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `rma.annotations.get`
  * `rma.collectors.get`
  * `rma.collectors.list`
  * `rma.locations.*`
  * `rma.operations.get`
  * `rma.operations.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Roles and permissions

The following tables show the roles and permissions available in Migration Center.

### Migration Center roles and permissions

Role | Permissions  
---|---  
  
#### Migration Center Admin Beta

(`roles/migrationcenter.admin`) Full access to Migration Center all resources.  |  `migrationcenter.*`

  * `migrationcenter.assets.delete`
  * `migrationcenter.assets.get`
  * `migrationcenter.assets.list`
  * `migrationcenter.assets.reportFrames`
  * `migrationcenter.assets.update`
  * `migrationcenter.assetsExportJobs.create`
  * `migrationcenter.assetsExportJobs.delete`
  * `migrationcenter.assetsExportJobs.get`
  * `migrationcenter.assetsExportJobs.list`
  * `migrationcenter.assetsExportJobs.run`
  * `migrationcenter.discoveryClients.create`
  * `migrationcenter.discoveryClients.delete`
  * `migrationcenter.discoveryClients.get`
  * `migrationcenter.discoveryClients.list`
  * `migrationcenter.discoveryClients.sendHeartbeat`
  * `migrationcenter.discoveryClients.update`
  * `migrationcenter.errorFrames.get`
  * `migrationcenter.errorFrames.list`
  * `migrationcenter.groups.create`
  * `migrationcenter.groups.delete`
  * `migrationcenter.groups.get`
  * `migrationcenter.groups.list`
  * `migrationcenter.groups.update`
  * `migrationcenter.importDataFiles.create`
  * `migrationcenter.importDataFiles.delete`
  * `migrationcenter.importDataFiles.get`
  * `migrationcenter.importDataFiles.list`
  * `migrationcenter.importJobs.create`
  * `migrationcenter.importJobs.delete`
  * `migrationcenter.importJobs.get`
  * `migrationcenter.importJobs.list`
  * `migrationcenter.importJobs.update`
  * `migrationcenter.locations.get`
  * `migrationcenter.locations.list`
  * `migrationcenter.operations.cancel`
  * `migrationcenter.operations.delete`
  * `migrationcenter.operations.get`
  * `migrationcenter.operations.list`
  * `migrationcenter.preferenceSets.create`
  * `migrationcenter.preferenceSets.delete`
  * `migrationcenter.preferenceSets.get`
  * `migrationcenter.preferenceSets.list`
  * `migrationcenter.preferenceSets.update`
  * `migrationcenter.relations.get`
  * `migrationcenter.relations.list`
  * `migrationcenter.reportConfigs.create`
  * `migrationcenter.reportConfigs.delete`
  * `migrationcenter.reportConfigs.get`
  * `migrationcenter.reportConfigs.list`
  * `migrationcenter.reports.create`
  * `migrationcenter.reports.delete`
  * `migrationcenter.reports.get`
  * `migrationcenter.reports.list`
  * `migrationcenter.settings.get`
  * `migrationcenter.settings.update`
  * `migrationcenter.sources.create`
  * `migrationcenter.sources.delete`
  * `migrationcenter.sources.get`
  * `migrationcenter.sources.list`
  * `migrationcenter.sources.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `rma.*`

  * `rma.annotations.create`
  * `rma.annotations.get`
  * `rma.collectors.create`
  * `rma.collectors.delete`
  * `rma.collectors.get`
  * `rma.collectors.list`
  * `rma.collectors.update`
  * `rma.locations.get`
  * `rma.locations.list`
  * `rma.operations.cancel`
  * `rma.operations.delete`
  * `rma.operations.get`
  * `rma.operations.list`

`serviceusage.quotas.get`  
  
#### Migration Center Viewer Beta

(`roles/migrationcenter.viewer`) Read-only access to Migration Center all resources.  |  `migrationcenter.assets.get` `migrationcenter.assets.list` `migrationcenter.assetsExportJobs.get` `migrationcenter.assetsExportJobs.list` `migrationcenter.discoveryClients.get` `migrationcenter.discoveryClients.list` `migrationcenter.errorFrames.*`

  * `migrationcenter.errorFrames.get`
  * `migrationcenter.errorFrames.list`

`migrationcenter.groups.get` `migrationcenter.groups.list` `migrationcenter.importDataFiles.get` `migrationcenter.importDataFiles.list` `migrationcenter.importJobs.get` `migrationcenter.importJobs.list` `migrationcenter.locations.*`

  * `migrationcenter.locations.get`
  * `migrationcenter.locations.list`

`migrationcenter.operations.get` `migrationcenter.operations.list` `migrationcenter.preferenceSets.get` `migrationcenter.preferenceSets.list` `migrationcenter.relations.*`

  * `migrationcenter.relations.get`
  * `migrationcenter.relations.list`

`migrationcenter.reportConfigs.get` `migrationcenter.reportConfigs.list` `migrationcenter.reports.get` `migrationcenter.reports.list` `migrationcenter.settings.get` `migrationcenter.sources.get` `migrationcenter.sources.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `rma.annotations.get` `rma.collectors.get` `rma.collectors.list` `rma.locations.*`

  * `rma.locations.get`
  * `rma.locations.list`

`rma.operations.get` `rma.operations.list` `serviceusage.quotas.get`  
  
#### Migration Center Discovery Client Beta

(`roles/migrationcenter.discoveryClient`) Migration Center Discover Client role  |  `migrationcenter.assets.reportFrames` `migrationcenter.discoveryClients.get` `migrationcenter.discoveryClients.sendHeartbeat`  
  
#### Migration Center Discovery Client Registrator Beta

(`roles/migrationcenter.discoveryClientRegistrator`) Registrator of Migration Center Discover Clients  |  `migrationcenter.discoveryClients.create` `migrationcenter.discoveryClients.delete` `migrationcenter.discoveryClients.update` `migrationcenter.operations.get` `migrationcenter.sources.create` `migrationcenter.sources.delete` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Migration Center Service Agent 

(`roles/migrationcenter.serviceAgent`) Gives Migration Center Service Account access to objects storedin object store and Cloud Migration products.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `storage.objects.get` `vmmigration.migratingVms.create`  
  
### Rapid Migration Assessment roles and permissions

Role | Permissions  
---|---  
  
#### Rapid Migration Assessment Admin 

(`roles/rma.admin`) Full access to Rapid Migration Assessment all resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `rma.*`

  * `rma.annotations.create`
  * `rma.annotations.get`
  * `rma.collectors.create`
  * `rma.collectors.delete`
  * `rma.collectors.get`
  * `rma.collectors.list`
  * `rma.collectors.update`
  * `rma.locations.get`
  * `rma.locations.list`
  * `rma.operations.cancel`
  * `rma.operations.delete`
  * `rma.operations.get`
  * `rma.operations.list`

  
  
#### Rapid Migration Assessment Viewer 

(`roles/rma.viewer`) Read-only access to Rapid Migration Assessment all resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `rma.annotations.get` `rma.collectors.get` `rma.collectors.list` `rma.locations.*`

  * `rma.locations.get`
  * `rma.locations.list`

`rma.operations.get` `rma.operations.list`  
  
#### Rapid Migration Assessment Runner 

(`roles/rma.runner`) Update and Read access to Rapid Migration Assessment all resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `rma.annotations.get` `rma.collectors.get` `rma.collectors.list` `rma.collectors.update` `rma.locations.*`

  * `rma.locations.get`
  * `rma.locations.list`

`rma.operations.get` `rma.operations.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### RMA Service Agent 

(`roles/rapidmigrationassessment.serviceAgent`) Gives RMA service account access to MC resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `autoscaling.sites.writeMetrics` `cloudasset.assets.exportResource` `cloudasset.feeds.create` `logging.logEntries.create` `migrationcenter.assets.list` `migrationcenter.assets.reportFrames` `migrationcenter.importJobs.get` `migrationcenter.importJobs.list` `migrationcenter.sources.*`

  * `migrationcenter.sources.create`
  * `migrationcenter.sources.delete`
  * `migrationcenter.sources.get`
  * `migrationcenter.sources.list`
  * `migrationcenter.sources.update`

`monitoring.metricDescriptors.create` `monitoring.metricDescriptors.list` `monitoring.timeSeries.create` `resourcemanager.projects.get`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
