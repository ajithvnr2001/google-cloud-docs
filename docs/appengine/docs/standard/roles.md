---
url: https://docs.cloud.google.com/appengine/docs/standard/roles/
title: Roles that grant access to App Engine \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:43.301947+00:00
---

# Roles that grant access to App Engine  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Roles that grant access to App Engine Stay organized with collections  Save and categorize content based on your preferences. 

Roles determine which services and actions are available to a user account or service account. The following types of roles grant access to App Engine:

  * Basic roles which apply to all services and resources in a project, including but not limited App Engine. For example, an account with the Editor role can change App Engine settings as well as Cloud Storage settings.

  * Predefined App Engine roles, which provide granular access to App Engine. Each service in your Google Cloud project provides its own predefined roles. For example, an account that only has the App Engine Deployer role can deploy App Engine apps but cannot view or create objects in Cloud Storage. Such an account would also need a specific [Cloud Storage predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) to create or view objects in Cloud Storage.

  * [Custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), which provide granular access according to a list of permissions you specify.




You can use basic roles when you are working on smaller projects that have less complex needs. For more fine-tuned access controls, use predefined roles.

## Basic roles

Basic roles apply to all services and resources in a project. For example, an account in the Editor role can change App Engine settings as well as Cloud Storage settings.

Role | Google Cloud console permissions | Tools permissions  
---|---|---  
`Owner` | Required to create App Engine applications. All viewer and editor privileges, plus the ability to view deployed source code, invite users, change user roles, and delete an application.  | Required to create App Engine applications. Can also deploy application code and update all configurations.  
`Editor` | View application information and edit application settings.  | Deploy application code, update indexes/queues/crons.  
`Viewer` | View application information.  | Request logs  
  
## Predefined App Engine roles

Role | Permissions  
---|---  
  
#### App Engine Service Admin 

(`roles/appengine.admin`) Full access to App Engine resources.  |  `appengine.*`

  * `appengine.applications.create`
  * `appengine.applications.get`
  * `appengine.applications.listRuntimes`
  * `appengine.applications.update`
  * `appengine.instances.delete`
  * `appengine.instances.enableDebug`
  * `appengine.instances.get`
  * `appengine.instances.list`
  * `appengine.memcache.addKey`
  * `appengine.memcache.flush`
  * `appengine.memcache.get`
  * `appengine.memcache.getKey`
  * `appengine.memcache.list`
  * `appengine.memcache.update`
  * `appengine.operations.get`
  * `appengine.operations.list`
  * `appengine.runtimes.actAsAdmin`
  * `appengine.services.delete`
  * `appengine.services.get`
  * `appengine.services.list`
  * `appengine.services.update`
  * `appengine.versions.create`
  * `appengine.versions.delete`
  * `appengine.versions.exportAppImage`
  * `appengine.versions.get`
  * `appengine.versions.getFileContents`
  * `appengine.versions.list`
  * `appengine.versions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Admin 

(`roles/appengine.appAdmin`) Read/Write/Modify access to all application configuration and settings. To deploy new versions, a principal must have the [Service Account User](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) (`roles/iam.serviceAccountUser`) role on the assigned App Engine [service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts), and the Cloud Build Editor (`roles/cloudbuild.builds.editor`), and Cloud Storage Object Admin (`roles/storage.objectAdmin`) roles on the project. Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.applications.update` `appengine.instances.*`

  * `appengine.instances.delete`
  * `appengine.instances.enableDebug`
  * `appengine.instances.get`
  * `appengine.instances.list`

`appengine.memcache.addKey` `appengine.memcache.flush` `appengine.memcache.get` `appengine.memcache.update` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.runtimes.actAsAdmin` `appengine.services.*`

  * `appengine.services.delete`
  * `appengine.services.get`
  * `appengine.services.list`
  * `appengine.services.update`

`appengine.versions.create` `appengine.versions.delete` `appengine.versions.exportAppImage` `appengine.versions.get` `appengine.versions.list` `appengine.versions.update` `artifactregistry.projectsettings.get` `artifactregistry.repositories.deleteArtifacts` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.tags.get` `recommender.appengineVersionCostInsights.*`

  * `recommender.appengineVersionCostInsights.get`
  * `recommender.appengineVersionCostInsights.list`
  * `recommender.appengineVersionCostInsights.update`

`recommender.appengineVersionCostRecommendations.*`

  * `recommender.appengineVersionCostRecommendations.get`
  * `recommender.appengineVersionCostRecommendations.list`
  * `recommender.appengineVersionCostRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Editor 

(`roles/appengine.editor`) Editor role for App Engine  |  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.applications.update` `appengine.instances.*`

  * `appengine.instances.delete`
  * `appengine.instances.enableDebug`
  * `appengine.instances.get`
  * `appengine.instances.list`

`appengine.memcache.*`

  * `appengine.memcache.addKey`
  * `appengine.memcache.flush`
  * `appengine.memcache.get`
  * `appengine.memcache.getKey`
  * `appengine.memcache.list`
  * `appengine.memcache.update`

`appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.runtimes.actAsAdmin` `appengine.services.*`

  * `appengine.services.delete`
  * `appengine.services.get`
  * `appengine.services.list`
  * `appengine.services.update`

`appengine.versions.create` `appengine.versions.delete` `appengine.versions.exportAppImage` `appengine.versions.get` `appengine.versions.list` `appengine.versions.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Viewer 

(`roles/appengine.viewer`) Viewer role for App Engine  |  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.instances.get` `appengine.instances.list` `appengine.memcache.get` `appengine.memcache.getKey` `appengine.memcache.list` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.runtimes.actAsAdmin` `appengine.services.get` `appengine.services.list` `appengine.versions.get` `appengine.versions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Creator 

(`roles/appengine.appCreator`) Ability to create the App Engine resource for the project.  Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.create` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Viewer 

(`roles/appengine.appViewer`) Read-only access to all application configuration and settings.  Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.instances.get` `appengine.instances.list` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.services.get` `appengine.services.list` `appengine.versions.get` `appengine.versions.list` `artifactregistry.projectsettings.get` `recommender.appengineVersionCostInsights.get` `recommender.appengineVersionCostInsights.list` `recommender.appengineVersionCostRecommendations.get` `recommender.appengineVersionCostRecommendations.list` `recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Code Viewer 

(`roles/appengine.codeViewer`) Read-only access to all application configuration, settings, and deployed source code.  Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.instances.get` `appengine.instances.list` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.services.get` `appengine.services.list` `appengine.versions.get` `appengine.versions.getFileContents` `appengine.versions.list` `artifactregistry.projectsettings.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Managed VM Debug Access 

(`roles/appengine.debugger`) Ability to read or manage v2 instances.  |  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.instances.*`

  * `appengine.instances.delete`
  * `appengine.instances.enableDebug`
  * `appengine.instances.get`
  * `appengine.instances.list`

`appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.services.get` `appengine.services.list` `appengine.versions.get` `appengine.versions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Deployer 

(`roles/appengine.deployer`) Read-only access to all application configuration and settings. To deploy new versions, you must also have the [Service Account User](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) (`roles/iam.serviceAccountUser`) role on the assigned App Engine [service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts), and the Cloud Build Editor (`roles/cloudbuild.builds.editor`), and Cloud Storage Object Admin (`roles/storage.objectAdmin`) roles on the project. Cannot modify existing versions other than deleting versions that are not receiving traffic. Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.instances.get` `appengine.instances.list` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.services.get` `appengine.services.list` `appengine.versions.create` `appengine.versions.delete` `appengine.versions.exportAppImage` `appengine.versions.get` `appengine.versions.list` `artifactregistry.projectsettings.get` `artifactregistry.repositories.deleteArtifacts` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.tags.get` `recommender.appengineVersionCostInsights.*`

  * `recommender.appengineVersionCostInsights.get`
  * `recommender.appengineVersionCostInsights.list`
  * `recommender.appengineVersionCostInsights.update`

`recommender.appengineVersionCostRecommendations.*`

  * `recommender.appengineVersionCostRecommendations.get`
  * `recommender.appengineVersionCostRecommendations.list`
  * `recommender.appengineVersionCostRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Memcache Data Admin 

(`roles/appengine.memcacheDataAdmin`) Can get, set, delete, and flush App Engine Memcache items.  |  `appengine.applications.get` `appengine.memcache.addKey` `appengine.memcache.flush` `appengine.memcache.get` `appengine.memcache.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### App Engine Service Admin 

(`roles/appengine.serviceAdmin`) Read-only access to all application configuration and settings. Write access to module-level and version-level settings. Cannot deploy a new version. Lowest-level resources where you can grant this role:

  * Project 

|  `appengine.applications.get` `appengine.applications.listRuntimes` `appengine.instances.delete` `appengine.instances.get` `appengine.instances.list` `appengine.operations.*`

  * `appengine.operations.get`
  * `appengine.operations.list`

`appengine.services.*`

  * `appengine.services.delete`
  * `appengine.services.get`
  * `appengine.services.list`
  * `appengine.services.update`

`appengine.versions.delete` `appengine.versions.get` `appengine.versions.list` `appengine.versions.update` `artifactregistry.projectsettings.get` `recommender.appengineVersionCostInsights.*`

  * `recommender.appengineVersionCostInsights.get`
  * `recommender.appengineVersionCostInsights.list`
  * `recommender.appengineVersionCostInsights.update`

`recommender.appengineVersionCostRecommendations.*`

  * `recommender.appengineVersionCostRecommendations.get`
  * `recommender.appengineVersionCostRecommendations.list`
  * `recommender.appengineVersionCostRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### App Engine Standard Environment Service Agent 

(`roles/appengine.serviceAgent`) Give App Engine Standard Envirnoment service account access to managed resources. Includes access to service accounts.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `appengine.versions.delete` `appengine.versions.get` `appengine.versions.list` `appengine.versions.update` `artifactregistry.aptartifacts.create` `artifactregistry.dockerimages.*`

  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`

`artifactregistry.files.download` `artifactregistry.files.get` `artifactregistry.files.list` `artifactregistry.kfpartifacts.create` `artifactregistry.locations.*`

  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`

`artifactregistry.mavenartifacts.*`

  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`

`artifactregistry.npmpackages.*`

  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`

`artifactregistry.packages.get` `artifactregistry.packages.list` `artifactregistry.projectsettings.get` `artifactregistry.pythonpackages.*`

  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`

`artifactregistry.repositories.create` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.repositories.uploadArtifacts` `artifactregistry.tags.create` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.tags.update` `artifactregistry.versions.get` `artifactregistry.versions.list` `artifactregistry.yumartifacts.create` `compute.addresses.create` `compute.addresses.createInternal` `compute.addresses.delete` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.list` `compute.globalOperations.get` `compute.networks.get` `compute.regionOperations.get` `compute.subnetworks.get` `compute.subnetworks.use` `compute.zoneOperations.get` `datastore.databases.get` `datastore.entities.create` `datastore.entities.delete` `datastore.entities.get` `datastore.entities.list` `datastore.entities.update` `datastore.namespaces.*`

  * `datastore.namespaces.get`
  * `datastore.namespaces.list`

`datastore.schemas.list` `datastore.statistics.*`

  * `datastore.statistics.get`
  * `datastore.statistics.list`

`iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `iam.serviceAccounts.signBlob` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.buckets.create` `storage.buckets.get`  
The predefined roles for App Engine provide you with finer grained options for access control. 

_These roles only provide access to App Engine._ If your project includes other services, such as Cloud Storage or Cloud SQL, you will need to assign [additional roles](https://docs.cloud.google.com/iam/docs/roles-permissions) to enable access to the other services.

### Comparison of App Engine predefined roles

The following table provides a complete comparison of the capabilities of each predefined App Engine role.

Capability | App Engine Admin | App Engine Service Admin | App Engine Deployer | App Engine Viewer | App Engine Code Viewer  
---|---|---|---|---|---  
List all services, versions and instances | Yes | Yes | Yes | Yes | Yes  
View all application, service, version, and instance settings | Yes | Yes | Yes | Yes | Yes  
View runtime metrics such as resource usage, load information, and error information | Yes | Yes | Yes | Yes | Yes  
View app source code | No | No | No | No | Yes  
Deploy a new version of an app | Yes, if you also grant the Service Account User role | No | Yes, if you also grant the Service Account User role | No | No  
Split or migrate traffic | Yes | Yes | No*** | No | No  
Start and stop a version | Yes | Yes | No | No | No  
Delete a version | Yes | Yes | Yes | No | No  
Delete an entire service | Yes | Yes | No | No | No  
Use SSH to connect to a VM instance in the flexible environment | Yes | No | No | No | No  
Shut down an instance | Yes | No | No | No | No  
Disable and re-enable the App Engine application | Yes | No | No | No | No  
Access handlers that have a login:admin restriction ([first generation](https://docs.cloud.google.com/appengine/docs/standard/runtimes) runtimes only) | Yes | No | No | No | No  
Update dispatch rules | Yes | No | No | No | No  
Update DoS settings | Yes | No | No | No | No  
Update cron schedules | No | No | No | No | No  
Update default cookie expiration | Yes | No | No | No | No  
Update referrers | Yes | No | No | No | No  
Update Email API Authorized Senders | Yes | No | No | No | No  
**Note:** The predefined roles are enforced in the [Google Cloud console](https://console.cloud.google.com/iam-admin/iam), the [Admin API](https://docs.cloud.google.com/appengine/docs/admin-api/access-control), and other tooling that requires access, including the [deployment commands](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#deploying_your_application).

For details about the specific IAM permissions that are granted by each role, see the [Roles](https://docs.cloud.google.com/appengine/docs/admin-api/access-control#roles) section of the Admin API.

## Recommended role for application deployment

For an account that is responsible _only_ for deploying new versions of an app, we recommend that you grant the following roles:

  * App Engine Deployer role (`roles/appengine.deployer`)
  * Service Account User role (`roles/iam.serviceAccountUser`)

The [Service Account User role](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) enables the account to impersonate the default App Engine service account during the deployment process.

  * If the account uses `gcloud` commands to deploy, add these roles as well: 

    * Storage Object Admin (`roles/storage.objectAdmin`)
    * Cloud Build Editor (`roles/cloudbuild.builds.editor`)
  * To access data stored in Datastore, or update indexes, enable the Cloud Datastore Index Admin role (`roles/datastore.indexAdmin`).


**Note:** If you have granted an account the App Engine Admin role, you don't need to grant it the App Engine Deployer role, because the Admin role holds the same relevant permissions as the Deployer role, along with additional administrative privileges. We recommend using the App Engine Deployer role for accounts that are responsible only for deploying new versions.

For details about how to grant the required permissions, see [Creating a user account](https://docs.cloud.google.com/appengine/docs/standard/access-control#user_account).

### Separation of deployment and traffic routing duties

Many organizations prefer to separate the task of deploying an application version from the task of ramping up traffic to the newly created version, and to have these tasks done by different job functions. The App Engine Deployer and App Engine Service Admin roles provide this separation:

  * App Engine Deployer plus Service Account User roles - Accounts are limited to deploying new versions and deleting old versions that are not serving traffic. The account with these roles won't be able to configure traffic to any version nor change application-level settings such as dispatch rules or authentication domain.
  * App Engine Service Admin role - Accounts cannot deploy a new version of an app nor change application-level settings. However, those accounts have privileges to change the properties of existing services and versions, including changing which versions can serve traffic. The App Engine Service Admin role is ideal for an Operations/IT department that handles ramping up traffic to newly deployed versions.



**Note** : Accounts with the App Engine Deployer role can overwrite a version that is serving traffic by deploying a new version with the same name (using the `--version` flag).

### Limitations of the predefined roles

None of the App Engine predefined roles grant access to the following:

  * View and download application logs.
  * View Monitoring charts in the Google Cloud console.
  * Enable and Disable billing.
  * Run security scans in Cloud Security Scanner.
  * Access configuration or data stored in Datastore, Task Queues, Cloud Search or any other Cloud Platform storage product.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
