---
url: https://docs.cloud.google.com/firestore/native/docs/security/iam/
title: Security for server client libraries \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:29.877303+00:00
---

# Security for server client libraries  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/security/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Security for server client libraries

When you use the server client libraries for Firestore, you can manage access to your resources with Identity and Access Management (IAM). IAM lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. This page describes the IAM permissions and roles for Firestore. For a detailed description of IAM, read the [IAM documentation](https://cloud.google.com/iam/docs/).

IAM lets you adopt the [security principle of least privilege](https://wikipedia.org/wiki/Principle_of_least_privilege), so you grant only the necessary access to your resources.

IAM lets you control **who (user)** has **what (role)** permission for **which** resources by setting IAM policies. IAM policies grant one or more roles to a user, giving the user certain permissions. For example, you can grant the `datastore.indexAdmin` role to a user, which allows the user to create, modify, delete, list, or view indexes.

## Permissions and roles

This section summarizes the permissions and roles that Firestore supports.

**Note:** Some Firestore permissions differ from the standard IAM model permissions. For example, in the IAM model, the `datastore.databases.get` permission lets you return a database object while, in Firestore, `datastore.databases.get` lets you begin or roll back a transaction. To retrieve a database object's information, use the `datastore.databases.getMetadata` permission. 

The `datastore.schemas.*` permissions were previously named `datastore.indexes.*`. You can still use `datastore.indexes` as an alias for `datastore.schemas`. 

### Required permissions for API methods

The following table lists the permissions that the caller must have to perform each action:

Method | Required permissions  
---|---  
`projects.databases.documents`  
[`batchGet`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/batchGet) | `datastore.entities.get`  
[`batchWrite`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/batchWrite) update or transform with [exists precondition](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/Precondition) set to `false` | `datastore.entities.create`  
[`batchWrite`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/batchWrite) update or transform with [exists precondition](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/Precondition) set to `true` | `datastore.entities.create`  
[`batchWrite`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/batchWrite) update or transform with no [precondition](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/Precondition) | `datastore.entities.create  
datastore.entities.update`  
[`beginTransaction`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/beginTransaction) | `datastore.databases.get`  
[`commit`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/commit) update or transform with [exists precondition](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/Precondition) set to `false` | `datastore.entities.create`  
[`commit`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/commit) update or transform with [exists precondition](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/Precondition) set to `true` | `datastore.entities.update`  
[`commit`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/commit) update or transform with no [precondition](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/Precondition) | `datastore.entities.create  
datastore.entities.update`  
[`commit`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/commit) delete | `datastore.entities.delete`  
[`createDocument`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/createDocument) | `datastore.entities.create`  
[`delete`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/delete) | `datastore.entities.delete`  
[`get`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/get) | `datastore.entities.get`  
[`list`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/list) | `datastore.entities.get`  
`datastore.entities.list`  
[`listCollectionIds`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/listCollectionIds) | `datastore.entities.list`  
[`partitionQuery`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/partitionQuery) | `datastore.entities.get  
datastore.entities.list`  
[`patch`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/patch) | `datastore.entities.update`  
[`rollback`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/rollback) | `datastore.databases.get`  
[`runAggregationQuery`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/runAggregationQuery) | `datastore.entities.get  
datastore.entities.list`  
[`runQuery`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/runQuery) | `datastore.entities.get  
datastore.entities.list`  
[`executePipeline (RPC)`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/executePipeline)  
  
with any of the following stages:  
\- `collection(...)`  
\- `collection_group(...)`  
\- `database()` |  `datastore.entities.get  
datastore.entities.list`  
[`executePipeline (RPC)`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/executePipeline)  
  
with any of the following stages:  
\- `documents(...)`  
|  `datastore.entities.get`  
[`executePipeline (RPC)`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/executePipeline)  
  
with any of the following stages:  
\- `update(...)`  
|  `datastore.entities.update`  
[`executePipeline (RPC)`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.documents/executePipeline)  
  
with any of the following stages:  
\- `delete(...)`  
|  `datastore.entities.delete`  
[`write (RPC)`](https://docs.cloud.google.com/firestore/native/docs/reference/rpc/google.firestore.v1#write) update or transform with [exists precondition](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/Precondition) set to `false` | `datastore.entities.create`  
[`write (RPC)`](https://docs.cloud.google.com/firestore/native/docs/reference/rpc/google.firestore.v1#write) update or transform with [exists precondition](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/Precondition) set to `true` | `datastore.entities.update`  
[`write (RPC)`](https://docs.cloud.google.com/firestore/native/docs/reference/rpc/google.firestore.v1#write) update or transform with no [precondition](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/Precondition) | `datastore.entities.create  
datastore.entities.update`  
[`write (RPC)`](https://docs.cloud.google.com/firestore/native/docs/reference/rpc/google.firestore.v1#write) delete | `datastore.entities.delete`  
`projects.databases.indexes`  
[`create`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.indexes/create) | `datastore.schemas.create`  
[`delete`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.indexes/delete) | `datastore.schemas.delete`  
[`get`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.indexes/get) | `datastore.schemas.get`  
[`list`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/latest/projects.databases.indexes/list) | `datastore.schemas.list`  
`projects.databases`  
[`create`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/v1/projects.databases/create) |  `datastore.databases.create`  
If your `create` request contains a `tags` value, then the following additional permissions are required:

  * `datastore.databases.createTagBinding`

If you would like to verify whether the tag bindings are set successfully by listing the bindings, then the following additional permissions are required:

  * `datastore.databases.listTagBindings`
  * `datastore.databases.listEffectiveTags`

  
[`delete`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/v1/projects.databases/delete) | `datastore.databases.delete`  
[`get`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/v1/projects.databases/get) | `datastore.databases.getMetadata`  
[`list`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/v1/projects.databases/list) | `datastore.databases.list`  
[`patch`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/v1/projects.databases/patch) | `datastore.databases.update`  
restore | `datastore.backups.restoreDatabase`  
[`clone`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/v1/projects.databases/clone) |  `datastore.databases.clone`  
If your `clone` request contains a `tags` value, then the following additional permissions are required:

  * `datastore.databases.createTagBinding`

If you would like to verify whether the tag bindings are set successfully by listing the bindings, then the following additional permissions are required:

  * `datastore.databases.listTagBindings`
  * `datastore.databases.listEffectiveTags`

  
`projects.locations`  
[`get`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/v1/projects.locations/get) | `datastore.locations.get`  
[`list`](https://docs.cloud.google.com/firestore/native/docs/reference/rest/v1/projects.locations/list) | `datastore.locations.list`  
`projects.databases.backupschedules`  
get | `datastore.backupSchedules.get`  
list | `datastore.backupSchedules.list`  
create | `datastore.backupSchedules.create`  
update | `datastore.backupSchedules.update`  
delete | `datastore.backupSchedules.delete`  
`projects.locations.backups`  
get | `datastore.backups.get`  
list | `datastore.backups.list`  
delete | `datastore.backups.delete`  
  
### Predefined roles

With IAM, every API method in Firestore requires that the account making the API request has the appropriate permissions to use the resource. Permissions are granted by setting policies that grant roles to a user, group, or service account. In addition to the primitive roles, [owner, editor, and viewer](https://cloud.google.com/iam/docs/understanding-roles#primitive_roles), you can grant Firestore roles to the users of your project.

The following table lists the Firestore IAM roles. You can grant multiple roles to a user, group, or service account.

Role | Permissions | Description  
---|---|---  
`roles/datastore.owner` | `appengine.applications.get`  
  
`datastore.*`  
  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
| Full access to Firestore.  
`roles/datastore.user` |  `appengine.applications.get`  
  
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
`resourcemanager.projects.list` | Read/write access to data in a Firestore database. Intended for application developers and service accounts.  
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
  
`datastore.insights.get` | Read access to all Firestore resources.  
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
  
`datastore.operations.list`  
  
`datastore.operations.get`  
  
`resourcemanager.projects.get`  
`resourcemanager.projects.list` | Full access to manage index definitions.  
`roles/datastore.keyVisualizerViewer` | `datastore.databases.getMetadata`  
`datastore.keyVisualizerScans.get`  
`datastore.keyVisualizerScans.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list` | Full access to Key Visualizer scans.  
`roles/datastore.backupSchedulesViewer` |  `datastore.backupSchedules.get`  
`datastore.backupSchedules.list` | Read access to backup schedules in a Firestore database.  
`roles/datastore.backupSchedulesAdmin` |  `datastore.backupSchedules.get`  
`datastore.backupSchedules.list`  
`datastore.backupSchedules.create`  
`datastore.backupSchedules.update`  
`datastore.backupSchedules.delete`  
`datastore.databases.list`  
`datastore.databases.getMetadata` | Full access to backup schedules in a Firestore database.  
`roles/datastore.backupsViewer` |  `datastore.backups.get`  
`datastore.backups.list` | Read access to backup information in a Firestore location.  
`roles/datastore.backupsAdmin` |  `datastore.backups.get`  
`datastore.backups.list`  
`datastore.backups.delete` | Full access to backups in a Firestore location.  
`roles/datastore.restoreAdmin` |  `datastore.backups.get`  
`datastore.backups.list`  
`datastore.backups.restoreDatabase`  
`datastore.databases.list`  
`datastore.databases.create`  
`datastore.databases.getMetadata`  
`datastore.operations.list`  
`datastore.operations.get`  
| Ability to restore a Firestore backup into a new database. This role also gives the ability to create new databases, not necessarily by restoring from a backup.  
`roles/datastore.cloneAdmin` |  `datastore.databases.clone`  
`datastore.databases.list`  
`datastore.databases.create`  
`datastore.databases.getMetadata`  
`datastore.operations.list`  
`datastore.operations.get`  
| Ability to clone a Firestore database into a new database. This role also gives the ability to create new databases, not necessarily by cloning.  
`roles/datastore.statisticsViewer` |  `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
`datastore.databases.getMetadata`  
`datastore.insights.get`  
`datastore.keyVisualizerScans.get`  
`datastore.keyVisualizerScans.list`  
`datastore.statistics.list`  
`datastore.statistics.get`  
| Read access to Insights, Stats, and Key Visualizer scans.  
  
### Custom roles

If the predefined roles don't address your business requirements, you can define your own custom roles with permissions that you specify:

  * [Learn about custom roles.](https://docs.cloud.google.com/iam/docs/understanding-custom-roles)
  * [Create and manage custom roles.](https://cloud.google.com/iam/docs/creating-custom-roles)



#### Required roles to create and manage tags

If any tag is represented in create or restore actions, some roles are required. See [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing) for more details on creating tag key-value pairs before associate them to the database resources.

The following listed permissions are required.

##### View tags

  * `datastore.databases.listTagBindings`
  * `datastore.databases.listEffectiveTags`



##### Manage tags on resources

The following permission is required for the database resource you're attaching the tag value.

  * `datastore.databases.createTagBinding`



### Permissions

The following table lists the permissions that Firestore supports.

Database permission name | Description |   
---|---|---  
`datastore.databases.get` | Begin or rollback a transaction. |   
`datastore.databases.import` | Import entities into a database. |   
`datastore.databases.export` | Export entities from a database. |   
`datastore.databases.bulkDelete` | Bulk delete entities from a database. |   
`datastore.databases.getMetadata` | Read metadata from a database. |   
`datastore.databases.list` | List databases in a project. |   
`datastore.databases.create` | Create a database. |   
`datastore.databases.update` | Update a database. |   
`datastore.databases.delete` | Delete a database. |   
`datastore.databases.clone` | Clone a database. |   
`datastore.databases.createTagBinding` | Create a tag binding for a database. |   
`datastore.databases.deleteTagBinding` | Delete a tag binding for a database. |   
`datastore.databases.listTagBindings` | List all tag bindings for a database. |   
`datastore.databases.listEffectiveTagBindings` | List effective tag bindings for a database. |   
Entity permission name | Description |   
`datastore.entities.create` | Create a document. |   
`datastore.entities.delete` | Delete a document. |   
`datastore.entities.get` | Read a document. |   
`datastore.entities.list` | List the names of documents in a project.  
(`datastore.entities.get` is required to access the document data.) |   
`datastore.entities.update` | Update a document. |   
Index permission name | Description |   
`datastore.schemas.create` | Create an index. |   
`datastore.schemas.delete` | Delete an index. |   
`datastore.schemas.get` | Read metadata from an index. |   
`datastore.schemas.list` | List the indexes in a project. |   
`datastore.schemas.update` | Update an index. |   
Operation permission name | Description |   
`datastore.operations.cancel` | Cancel a long-running operation. |   
`datastore.operations.delete` | Delete a long-running operation. |   
`datastore.operations.get` | Gets the latest state of a long-running operation. |   
`datastore.operations.list` | List long-running operations. |   
Project permission name | Description |   
`resourcemanager.projects.get` | Browse resources in the project. |   
`resourcemanager.projects.list` | List owned projects. |   
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
  
## Role change latency

Firestore caches IAM permissions for 5 minutes, so it takes up to 5 minutes for a role change to become effective.

## Manage Firestore IAM

You can get and set IAM policies using the Google Cloud console, the IAM API, or the `gcloud` command-line tool. See [Granting, Changing, and Revoking Access to Project Members](https://cloud.google.com/iam/docs/granting-changing-revoking-access) for details.

## Configure conditional access permissions

You can use [IAM Conditions](https://cloud.google.com/iam/docs/conditions-overview) to define and enforce conditional access control.

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
    

To learn how to define IAM Conditions for temporary access, see [Configure temporary access](https://cloud.google.com/iam/docs/configuring-temporary-access).

To learn how to configure IAM Conditions for access to one or more databases, see [Configure database access conditions](https://docs.cloud.google.com/firestore/native/docs/manage-databases#configure_database_access_conditions).

## Security rule dependency on IAM

[Firestore Security Rules](https://docs.cloud.google.com/firestore/docs/security/get-started) for mobile/web clients depend on the following service account and IAM binding:

Service account | IAM role  
---|---  
`service-project_number@firebase-rules.iam.gserviceaccount.com` | `roles/firebaserules.system`  
  
Firebase automatically sets up this service account for you. If you remove the `firebaserules.system` role from this service account, your security rules will deny all requests. To restore this IAM binding, use the following [gcloud CLI](https://cloud.google.com/sdk) command:
    
    
    gcloud projects add-iam-policy-binding project_id \
    --member=serviceAccount:service-project_number@firebase-rules.iam.gserviceaccount.com \
    --role=roles/firebaserules.system

To determine your project_id and project_number, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

Use the Google Cloud CLI instead of the Google Cloud console, because the`firebaserules.system` role is hidden in the console by default.

## What's next

  * Learn more about [IAM](https://cloud.google.com/iam/docs/).
  * [Grant IAM roles](https://cloud.google.com/iam/docs/granting-changing-revoking-access).
  * Learn about [authentication](https://cloud.google.com/firestore/docs/authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
