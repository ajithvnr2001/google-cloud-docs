---
url: https://docs.cloud.google.com/datastore/docs/access/iam/
title: Identity and Access Management (IAM) \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:22.557864+00:00
---

# Identity and Access Management (IAM)  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/access/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)



Send feedback 

#  Identity and Access Management (IAM) Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud offers Identity and Access Management (IAM), which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. This page describes the Firestore in Datastore mode IAM roles. For a detailed description of IAM, read the [IAM documentation](https://docs.cloud.google.com/iam/docs).

**Note:** App Engine applications [require IAM permissions to access Datastore mode databases](https://docs.cloud.google.com/datastore/docs/activate#datastore-permissions-for-app-engine).

IAM lets you adopt the [security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources.

IAM lets you control **who (users)** has **what (roles)** permission to **which** resources by setting IAM policies. IAM policies grant specific role(s) to a user, giving the user certain permissions. For example, you can grant the `datastore.indexAdmin` role to a user and the user can create, modify, delete, list, or view indexes.

## Permissions and Roles

This section summarizes the permissions and roles Firestore in Datastore mode supports.

**Note:** Some Datastore mode permissions differ from the standard IAM model permissions. For example, in the IAM model, the `datastore.databases.get` permission lets you return a database object while, in Datastore mode, `datastore.databases.get` lets you begin or roll back a transaction. To retrieve a database object's information, use the `datastore.databases.getMetadata` permission. 

The `datastore.schemas.*` permissions were previously named `datastore.indexes.*`. You can still use `datastore.indexes` as an alias for `datastore.schemas`. 

### Permissions

The following table lists the permissions that Firestore in Datastore mode supports.

Database permission name | Description |   
---|---|---  
`datastore.databases.export` | Export entities from a database. |   
`datastore.databases.bulkDelete` | Bulk delete entities from a database. |   
`datastore.databases.get` | Begin or rollback a transaction.  
Commit with empty mutations. |   
`datastore.databases.import` | Import entities into a database. |   
`datastore.databases.getMetadata` | Read metadata from a database. |   
`datastore.databases.list` | List databases in a project. |   
`datastore.databases.create` | Create a database. |   
`datastore.databases.update` | Update a database. |   
`datastore.databases.delete` | Delete a database. |   
`datastore.databases.clone` | Clone a database. If your `clone` request contains a `tags` value, then the following additional permissions are required:

  * `datastore.databases.createTagBinding`

If you would like to verify whether the tag bindings are set successfully by listing the bindings, then the following additional permissions are required:

  * `datastore.databases.listTagBindings`
  * `datastore.databases.listEffectiveTags`

|   
`datastore.databases.createTagBinding` | Create a tag binding for a database. |   
`datastore.databases.deleteTagBinding` | Delete a tag binding for a database. |   
`datastore.databases.listTagBindings` | List all tag bindings for a database. |   
`datastore.databases.listEffectiveTagBindings` | List effective tag bindings for a database. |   
Entity permission name | Description |   
`datastore.entities.allocateIds` | Allocate IDs for keys with an incomplete key path. |   
`datastore.entities.create` | Create an entity. |   
`datastore.entities.delete` | Delete an entity. |   
`datastore.entities.get` | Read an entity. |   
`datastore.entities.list` | List the keys of entities in a project.  
(`datastore.entities.get` is required to access the entity data.) |   
`datastore.entities.update` | Update an entity. |   
Index permission name | Description |   
`datastore.schemas.create` | Create an index. |   
`datastore.schemas.delete` | Delete an index. |   
`datastore.schemas.get` | Read metadata from an index. |   
`datastore.schemas.list` | List the indexes in a project. |   
`datastore.schemas.update` | Update an index. |   
Namespace permission name | Description |   
`datastore.namespaces.get` | Retrieve metadata from a namespace. |   
`datastore.namespaces.list` | List the namespaces in a project. |   
Operation permission name | Description |   
`datastore.operations.cancel` | Cancel a long-running operation. |   
`datastore.operations.delete` | Delete a long-running operation. |   
`datastore.operations.get` | Gets the latest state of a long-running operation. |   
`datastore.operations.list` | List long-running operations. |   
Project permission name | Description  
`resourcemanager.projects.get` | Browse resources in the project.  
`resourcemanager.projects.list` | List owned projects.  
Statistics permission name | Description |   
`datastore.statistics.get` | Retrieve [statistics](https://docs.cloud.google.com/datastore/docs/concepts/stats) entities. |   
`datastore.statistics.list` | List the keys of [statistics](https://docs.cloud.google.com/datastore/docs/concepts/stats) entities.  
(`datastore.statistics.get` is required to access the statistics entity data.) |   
App Engine permission name | Description |   
`appengine.applications.get` | Read-only access to all App Engine application configuration and settings. |   
Location permission name | Description |   
`datastore.locations.get` | Get details about a database location. Required to create a new database. |   
`datastore.locations.list` | List available database locations. Required to create a new database. |   
Key Visualizer permission name | Description |   
`datastore.keyVisualizerScans.get` | Get details about Key Visualizer scans. |   
`datastore.keyVisualizerScans.list` | List available Key Visualizer scans. |   
Backup Schedule permission name | Description |   
`datastore.backupSchedules.get` | Get details about a backup schedule. |   
`datastore.backupSchedules.list` | List available backup schedules. |   
`datastore.backupSchedules.create` | Create a backup schedule. |   
`datastore.backupSchedules.update` | Update a backup schedule. |   
`datastore.backupSchedules.delete` | Delete a backup schedule. |   
Backup permission name | Description |   
`datastore.backups.get` | Get details about a backup. |   
`datastore.backups.list` | List available backups. |   
`datastore.backups.delete` | Delete a backup. |   
`datastore.backups.restoreDatabase` | Restore a database from a backup. |   
Insights permission name | Description |   
`datastore.insights.get` | Get insights of a resource |   
  
### Predefined roles

With IAM, every Datastore API method requires that the account making the API request has the appropriate permissions to use the resource. Permissions are granted by setting policies that grant roles to a user, group, or service account. In addition to the basic roles, [Owner, Editor, and Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic), you can grant Firestore in Datastore mode roles to the users of your project.

The following table lists the Firestore in Datastore mode IAM roles. You can grant multiple roles to a user, group, or service account.

Role | Permissions | Description  
---|---|---  
`roles/datastore.owner` | `appengine.applications.get`  
`datastore.*`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list` | Full access to the database instance.  
For [Datastore Admin](https://docs.cloud.google.com/datastore/docs/console/datastore-admin-console) access, grant the `appengine.appAdmin` role to the principal.  
`roles/datastore.user` | `appengine.applications.get`  
`datastore.databases.get`  
`datastore.databases.getMetadata`  
`datastore.databases.list`  
`datastore.entities.*`  
`datastore.schemas.list`  
`datastore.namespaces.get`  
`datastore.namespaces.list`  
`datastore.statistics.get`  
`datastore.statistics.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list` | Read/write access to data in a Datastore mode database. Intended for application developers and service accounts.  
`roles/datastore.viewer` | `appengine.applications.get`  
`datastore.databases.get`  
`datastore.databases.getMetadata`  
`datastore.databases.list`  
`datastore.entities.get`  
`datastore.entities.list`  
`datastore.schemas.get`  
`datastore.schemas.list`  
`datastore.namespaces.get`  
`datastore.namespaces.list`  
`datastore.statistics.get`  
`datastore.statistics.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`datastore.insights.get` | Read access to all Datastore mode database resources.  
`roles/datastore.importExportAdmin` | `appengine.applications.get`  
`datastore.databases.export`  
`datastore.databases.getMetadata`  
`datastore.databases.import`  
`datastore.operations.cancel`  
`datastore.operations.get`  
`datastore.operations.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list` | Full access to manage imports and exports.  
`roles/datastore.bulkAdmin` | `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`datastore.databases.getMetadata`  
`datastore.databases.bulkDelete`  
`datastore.operations.cancel`  
`datastore.operations.get`  
`datastore.operations.list` | Full access to manage bulk operations.  
`roles/datastore.indexAdmin` | `appengine.applications.get`  
`datastore.databases.getMetadata`  
`datastore.schemas.*`  
`datastore.operations.get`  
`datastore.operations.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list` | Full access to manage index definitions.  
`roles/datastore.keyVisualizerViewer` | `datastore.databases.getMetadata`  
`datastore.keyVisualizerScans.get`  
`datastore.keyVisualizerScans.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list` | Full access to Key Visualizer scans.  
`roles/datastore.backupSchedulesViewer` |  `datastore.backupSchedules.get`  
`datastore.backupSchedules.list` | Read access to backup schedules in a Datastore mode database.  
`roles/datastore.backupSchedulesAdmin` |  `datastore.backupSchedules.get`  
`datastore.backupSchedules.list`  
`datastore.backupSchedules.create`  
`datastore.backupSchedules.update`  
`datastore.backupSchedules.delete`  
`datastore.databases.list`  
`datastore.databases.getMetadata` | Full access to backup schedules in a Datastore mode database.  
`roles/datastore.backupsViewer` |  `datastore.backups.get`  
`datastore.backups.list` | Read access to backup information in a Datastore mode location.  
`roles/datastore.backupsAdmin` |  `datastore.backups.get`  
`datastore.backups.list`  
`datastore.backups.delete` | Full access to backups in a Datastore mode location.  
`roles/datastore.restoreAdmin` |  `datastore.backups.get`  
`datastore.backups.list`  
`datastore.backups.restoreDatabase`  
`datastore.databases.list`  
`datastore.databases.create`  
`datastore.databases.getMetadata`  
`datastore.operations.list`  
`datastore.operations.get`  
| Ability to restore a Datastore mode backup into a new database. This role also gives the ability to create new databases, not necessarily by restoring from a backup.  
`roles/datastore.cloneAdmin` |  `datastore.databases.clone`  
`datastore.databases.list`  
`datastore.databases.create`  
`datastore.databases.getMetadata`  
`datastore.operations.list`  
`datastore.operations.get`  
| Ability to clone a Datastore mode database into a new database. This role also gives the ability to create new databases, not necessarily by cloning.  
`roles/datastore.statisticsViewer` |  `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`datastore.databases.getMetadata`  
`datastore.insights.get`  
`datastore.keyVisualizerScans.get`  
`datastore.keyVisualizerScans.list`  
`datastore.statistics.list`  
`datastore.statistics.get`  
| Read access to Insights, Stats, and Key Visualizer scans.  
**Warning:** The App Engine [Owner, Editor, and Viewer](https://docs.cloud.google.com/appengine/docs/standard/java/roles#basic_roles) basic roles and the [App Engine Admin](https://docs.cloud.google.com/appengine/docs/java/access-control#predefined_app_engine_roles) predefined role have access to some of the functionality on the [Datastore Admin page](https://docs.cloud.google.com/datastore/docs/console/datastore-admin-console).

### Custom roles

If the predefined roles don't address your business requirements, you can define your own custom roles with permissions that you specify:

  * [Learn about custom roles.](https://docs.cloud.google.com/iam/docs/understanding-custom-roles)
  * [Create and manage custom roles.](https://docs.cloud.google.com/iam/docs/creating-custom-roles)



#### Required roles to create and manage tags

If any tag is represented in create or restore actions, some roles are required. See [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing) for more details on creating tag key-value pairs before associate them to the database resources.

The following listed permissions are required.

##### View tags

  * `datastore.databases.listTagBindings`
  * `datastore.databases.listEffectiveTags`



##### Manage tags on resources

The following permission is required for the database resource you're attaching the tag value.

  * `datastore.databases.createTagBinding`



### Required Permissions for API methods

The following table lists the permissions that the caller must have to call each method:

Method | Required Permission(s)  
---|---  
`[allocateIds](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/allocateIds)` | `datastore.entities.allocateIds`  
`[beginTransaction](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/beginTransaction)` | `datastore.databases.get`  
`[commit](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/commit)` with empty mutations | `datastore.databases.get`  
`[commit](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/commit)` for an insert | `datastore.entities.create`  
`[commit](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/commit)` for an upsert | `datastore.entities.create`  
`datastore.entities.update`  
`[commit](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/commit)` for an update | `datastore.entities.update`  
`[commit](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/commit)` for a delete | `datastore.entities.delete`  
`[commit](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/commit)` for a lookup | `datastore.entities.get`  
  
For a lookup related to metadata or statistics, see Required Permissions for Metadata and Statistics.  
`[commit](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/commit)` for a query | `datastore.entities.list`  
`datastore.entities.get` (if the query is not a [keys-only query](https://docs.cloud.google.com/datastore/docs/concepts/queries#keys-only_queries))  
  
For a query related to metadata or statistics, see Required Permissions for Metadata and Statistics.  
`[lookup](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/lookup)` | `datastore.entities.get`  
  
For a lookup related to metadata or statistics, see Required Permissions for Metadata and Statistics.  
`[rollback](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/rollback)` | `datastore.databases.get`  
`[runQuery](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/runQuery)` | `datastore.entities.list`  
`datastore.entities.get` (if the query is not a [keys-only query](https://docs.cloud.google.com/datastore/docs/concepts/queries#keys-only_queries))  
  
For a query related to metadata or statistics, see Required Permissions for Metadata and Statistics.  
`[runQuery](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/runQuery)` with a [kindless query](https://docs.cloud.google.com/datastore/docs/concepts/queries#kindless_queries) | `datastore.entities.get`  
`datastore.entities.list`  
`datastore.statistics.get`  
`datastore.statistics.list`  
  
### Required Permissions for Metadata and Statistics

The following table lists permissions that the caller must have to call methods on [Metadata](https://docs.cloud.google.com/datastore/docs/concepts/metadataqueries) and [Statistics](https://docs.cloud.google.com/datastore/docs/concepts/stats).

Method | Required Permission(s)  
---|---  
`[lookup](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/lookup)` of entities with kind names matching **__Stat_*__** | `datastore.statistics.get`  
`[runQuery](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/runQuery)` using kinds with names matching **__Stat_*__** | `datastore.statistics.get`  
`datastore.statistics.list`  
`[runQuery](https://docs.cloud.google.com/datastore/reference/rest/v1/projects/runQuery)` using the kind **__namespace__** | `datastore.namespaces.get`  
`datastore.namespaces.list`  
  
### Required roles to create a Datastore mode database instance

To create a new Datastore mode database instance, you require either the [**Owner** role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) or the [ **Datastore Owner** role](https://docs.cloud.google.com/iam/docs/roles-permissions/firestore).

Datastore mode databases requires an active App Engine application. If the project doesn't have an application, Firestore in Datastore mode creates one for you. In that case, you require the `appengine.applications.create` permission from the **Owner** role or from an [IAM custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) containing the permission.

## Role change latency

Firestore in Datastore mode caches IAM permissions for 5 minutes, so it will take up to 5 minutes for a role change to become effective.

## Managing IAM

You can get and set IAM policies using the Google Cloud console, the IAM methods, or the Google Cloud CLI.

  * For the Google Cloud console, see [Access control using the Google Cloud console](https://docs.cloud.google.com/iam/docs/managing-policies#access_control_via_console).
  * For the IAM methods, see [Access control using the API](https://docs.cloud.google.com/iam/docs/managing-policies#access_control_via_api).
  * For the gcloud CLI, see [Access control using the gcloud tool](https://docs.cloud.google.com/iam/docs/managing-policies#access_control_via_the_gcloud_tool).



## Configure conditional access permissions

You can use [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to define and enforce conditional access control.

For example, the following condition assigns a principal the `datastore.user` role up until a specified date:
    
    
    {
      "role": "roles/datastore.user",
      "members": [
        "user:travis@example.com"
      ],
      "condition": {
        "title": "Expires_December_1_2023",
        "description": "Expires on December 1, 2023",
        "expression":
          "request.time < timestamp('2023-12-01T00:00:00.000Z')"
      }
    }
    

To learn how to define IAM Conditions for temporary access, see [Configure temporary access](https://docs.cloud.google.com/iam/docs/configuring-temporary-access).

To learn how to configure IAM Conditions for access to one or more databases, see [Configure database access conditions](https://docs.cloud.google.com/datastore/docs/manage-databases#configure_per-database_access_permissions).

## What's next

  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs).
  * [Grant IAM roles](https://docs.cloud.google.com/iam/docs/managing-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
