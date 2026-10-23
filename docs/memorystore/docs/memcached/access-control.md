---
url: https://docs.cloud.google.com/memorystore/docs/memcached/access-control/
title: Access control with IAM \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:54.367702+00:00
---

# Access control with IAM  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/access-control/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can control project access and permissions for Memorystore for Memcached using Identity and Access Management (IAM).

## Overview

IAM lets you control access to specific Google Cloud resources at a granular level, and also prevents unwanted access to those resources. For a detailed description of roles and permissions, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

Memorystore for Memcached provides a set of predefined roles designed to help you easily control access to your Memcached resources. If the predefined roles do not provide the sets of permissions you need, you can also create custom roles. In addition, the older basic roles (Editor, Viewer, and Owner) are still available to you, although they do not provide the same fine-grained control as the Memorystore for Memcached roles. Specifically, the basic roles provide access to resources across Google Cloud, rather than just for Memorystore for Memcached. For more information about basic roles, see [Basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).

## Permissions and roles

This section summarizes the permissions and roles that Memorystore for Memcached supports.

### Predefined roles

Memorystore for Memcached provides predefined roles that you can use to provide finer-grained permissions to principals. The role you grant to a principal controls what actions the principal can take. Principals can be individuals, groups, or [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).

You can grant multiple roles to the same principal, and can change the roles at any time.

The broader roles are more narrowly defined. For example, the Memcached Editor role includes all of the permissions of the Memcached Viewer role, along with the addition of permissions for the Memcached Editor role. Likewise, the Memcached Admin role includes all of the permissions of the Memcached Editor role, along with its additional permissions.

The basic roles (Owner, Editor, Viewer) provide permissions across Google Cloud. The roles specific to Memorystore for Memcached provide only Memorystore for Memcached permissions, except for the following Google Cloud permissions, which are needed for general Google Cloud usage:

`resourcemanager.projects.get` `resourcemanager.projects.list`

The following table lists the predefined roles available for Memorystore for Memcached, along with their Memorystore for Memcached permissions:

Role | Name | Memcached permissions | Description  
---|---|---|---  
` roles/owner ` | Owner | ` memcache.* ` | Full access and control for all Google Cloud resources; manage user access  
` roles/editor ` | Editor | All` memcache `permissions except for` *.getIamPolicy` & `.setIamPolicy` | Read-write access to all Google Cloud and Memcached resources (full control except for the ability to modify permissions)  
` roles/viewer ` | Viewer | ` memcache.*.get memcache.*.list ` | Read-only access to all Google Cloud resources, including Memcached resources  
` roles/memcache.admin ` | Memcached Admin | ` memcache.* ` | Full control for all Memorystore for Memcached resources.  
` roles/memcache.editor ` | Memcached Editor | All `memcache` permissions except for  
` memcache.instances.create memcache.instances.delete memcache.instances.applySoftwareUpdate memcache.instances.upgrade ` | Manage Memorystore for Memcached instances. Can't create or delete instances.  
` roles/memcache.viewer ` | Memcached Viewer | All `memcache` permissions except for  
` memcache.instances.create memcache.instances.delete memcache.instances.update memcache.operations.delete memcache.instances.applyParameters memcache.instances.updateParameters memcache.instances.applySoftwareUpdate memcache.instances.upgrade ` | Read-only access to all Memorystore for Memcached resources.  
  
### Permissions and their roles

The following table lists the permissions that Memorystore for Memcached supports, and the Memorystore for Memcached roles that include it:

Permission | Memcached role | Basic role  
---|---|---  
` memcache.instances.list ` | Memcached Admin  
Memcached Editor  
Memcached Viewer | Reader  
` memcache.instances.get ` | Memcached Admin  
Memcached Editor  
Memcached Viewer | Reader  
` memcache.instances.create ` | Memcached Admin | Writer  
` memcache.instances.update ` | Memcached Admin  
Memcached Editor | Writer  
` memcache.instances.delete ` | Memcached Admin | Writer  
`memcache.instances.applyParameters` | Memcached Admin  
Memcached Editor | Writer  
`memcache.instances.updateParameters` | Memcached Admin  
Memcached Editor | Writer  
`memcache.instances.applySoftwareUpdate` | Memcached Admin  
Memcached Editor | Writer  
`memcache.instances.upgrade` | Memcached Admin | Writer  
` memcache.locations.list ` | Memcached Admin  
Memcached Editor  
Memcached Viewer | Reader  
` memcache.locations.get   
` | Memcached Admin  
Memcached Editor  
Memcached Viewer | Reader  
` memcache.operations.list ` | Memcached Admin  
Memcached Editor  
Memcached Viewer | Reader  
` memcache.operations.get ` | Memcached Admin  
Memcached Editor  
Memcached Viewer | Reader  
` memcache.operations.delete ` | Memcached Admin  
Memcached Editor | Writer  
  
### Custom roles

If the predefined roles do not address your unique business requirements, you can define your own [custom roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom) with permissions that you specify. When you create custom roles for Memorystore for Memcached, make sure that you include both `resourcemanager.projects.get` and `resourcemanager.projects.list`. For more information, see [Permission dependencies](https://docs.cloud.google.com/iam/docs/roles-overview#custom-role-permission-dependencies).

### Required permissions for common tasks in the Google Cloud console

To enable a user to work with Memorystore for Memcached using the Google Cloud console, the user's role must include the `resourcemanager.projects.get` and the `resourcemanager.projects.list` permission.

The following table provides the other permissions required for some common tasks in the Google Cloud console:

Task | Required additional permissions  
---|---  
Display the instance listing page | ` memcache.instances.get memcache.instances.list `  
Creating and editing an instance | ` memcache.instances.create memcache.instances.get memcache.instances.list memcache.instances.update memcache.instances.applyParameters memcache.instances.updateParameters memcache.instances.applySoftwareUpdate compute.networks.list `  
Deleting an instance | ` memcache.instances.delete memcache.instances.get memcache.instances.list `  
Connecting to an instance from the Cloud Shell | ` memcache.instances.get memcache.instances.list memcache.instances.update `  
Upgrading the Memcached version of an instance | ` memcache.instances.upgrade `  
Viewing instance information | ` memcache.instances.get monitoring.timeSeries.list `  
  
### Required permissions for gcloud commands

To enable a user to work with Memorystore for Memcached using `gcloud` commands, the user's role must include the `resourcemanager.projects.get` and the `resourcemanager.projects.list` permission.

The following table lists the permissions that the user invoking a `gcloud` command must have for each `gcloud memcache` subcommand:

Command | Required permissions  
---|---  
`gcloud memcache instances create` |  ` memcache.instances.get memcache.instances.create `  
`gcloud memcache instances delete` | `memcache.instances.delete`  
`gcloud memcache instances update` |  ` memcache.instances.get memcache.instances.update memcache.instances.updateParameters `  
`gcloud memcache instances upgrade` |  ` memcache.instances.upgrade `  
`gcloud memcache instances list` | `memcache.instances.list  
`  
`gcloud memcache instances describe` | `memcache.instances.get`  
`gcloud memcache instances apply-parameters` | `memcache.instances.applyParameters`  
`gcloud beta memcache instances apply-software-update` | `memcache.instances.applySoftwareUpdate`  
`gcloud memcache operations list` | `memcache.operations.list`  
`gcloud memcache operations describe` | `memcache.operations.get`  
`gcloud memcache regions list` | `memcache.locations.list`  
`gcloud memcache regions describe` | `memcache.locations.get`  
`gcloud memcache zones list` | `memcache.locations.list`  
  
### Required permissions for API methods

The following table lists the permissions that the user must have to call each method in the Memorystore for Memcached API or to perform tasks using Google Cloud tools that use the API (such as the Google Cloud console or the `gcloud`command line tool):

**Note** : To call a method, in addition to the permissions in the following table, you must also have the required scopes. These scopes are described in the method's reference page. For more information, see [Authorize requests](https://docs.cloud.google.com/sql/docs/mysql/admin-api#auth).

All permissions are applied to the project. You can't apply different permissions based on the instance or on other lower-level objects.

Method | Required permissions  
---|---  
`locations.get` | `memcache.locations.get`  
`locations.list` | `memcache.locations.list`  
`instances.create` | `memcache.instances.create`  
`instances.delete` | `memcache.instances.delete`  
`instances.get` | `memcache.instances.get`  
`instances.upgrade` | `memcache.instances.upgrade`  
`instances.list` | `memcache.instances.list`  
`instances.patch` | `memcache.instances.update`  
`instances.updateParameters` | `memcache.instances.updateParameters`  
`instances.applyParameters` | `memcache.instances.applyParameters`  
`instances.applySoftwareUpdate` | `memcache.instances.applySoftwareUpdate`  
`operations.get` | `memcache.operations.get`  
`operations.list` | `memcache.operations.list`  
  
## Maintenance policy permissions

The table below shows permissions required for managing the [Maintenance policy](https://docs.cloud.google.com/memorystore/docs/memcached/maintenance-policy) for Memorystore for Memcached.

Permissions needed | Create a Memorystore instance with a maintenance policy enabled | Create or modify maintenance policies on an existing Memorystore instance | Viewing the maintenance policy settings | Rescheduling maintenance  
---|---|---|---|---  
`memcache.instances.create` |  ✓  |  X  |  X  |  X   
`memcache.instances.update` |  X  |  ✓  |  X  |  X   
`memcache.instances.get` |  X  |  X  |  ✓  |  X   
`memcache.instances.rescheduleMaintenance` |  X  |  X  |  X  |  ✓   
  
## What's next

  * [Monitor your Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/monitoring-instances).
  * View [audit logs](https://docs.cloud.google.com/memorystore/docs/memcached/audit-logging) for your Memcached instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
