---
url: https://docs.cloud.google.com/memorystore/docs/redis/access-control/
title: Access control with IAM \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:15:47.116410+00:00
---

# Access control with IAM  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are looking for the Memorystore for Redis Cluster documentation, see [Access control with IAM](https://docs.cloud.google.com/memorystore/docs/cluster/access-control).

This page describes how you can control Memorystore for Redis project access and permissions using Identity and Access Management (IAM).

## Overview

Google Cloud offers IAM, which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. This page describes the Memorystore for Redis IAM roles and permissions. For a detailed description of roles and permissions, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

Memorystore for Redis provides a set of predefined roles designed to help you easily control access to your Redis resources. If the predefined roles do not provide the sets of permissions you need, you can also create your own custom roles. In addition, the older basic roles (Editor, Viewer, and Owner) are also still available to you, although they do not provide the same fine-grained control as the Memorystore for Redis roles. In particular, the basic roles provide access to resources across Google Cloud, rather than just for Memorystore for Redis. For more information about basic roles, see [Basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).

## Permissions and roles

This section summarizes the permissions and roles that Memorystore for Redis supports.

### Predefined roles

Memorystore for Redis provides some predefined roles that you can use to provide finer-grained permissions to principals. The role you grant to a principal controls what actions the principal can take. Principals can be individuals, groups, or [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).

You can grant multiple roles to the same principal, and if you have the permissions to do so, you can change the roles granted to a principal at any time.

The broader roles include the more narrowly defined roles. For example, the Redis Editor role includes all of the permissions of the Redis Viewer role, along with the addition of permissions for the Redis Editor role. Likewise, the Redis Admin role includes all of the permissions of the Redis Editor role, along with its additional permissions.

The basic roles (Owner, Editor, Viewer) provide permissions across Google Cloud. The roles specific to Memorystore for Redis provide only Memorystore for Redis permissions, except for the following Google Cloud permissions, which are needed for general Google Cloud usage:

`resourcemanager.projects.get` `resourcemanager.projects.list`

The following table lists the predefined roles available for Memorystore for Redis, along with their Memorystore for Redis permissions:

Role | Name | Redis permissions | Description  
---|---|---|---  
` roles/owner ` | Owner | ` redis.* ` | Full access and control for all Google Cloud resources; manage user access  
` roles/editor ` | Editor | All` redis `permissions except for` *.getIamPolicy` & `.setIamPolicy` | Read-write access to all Google Cloud and Redis resources (full control except for the ability to modify permissions)  
` roles/viewer ` | Viewer | ` redis.*.get redis.*.list ` | Read-only access to all Memorystore for Redis resources. However, you can't use this permission to view data that's associated with the resources.  
` roles/redis.admin ` | Redis Admin | ` redis.* ` | Full control for all Memorystore for Redis resources.  
` roles/redis.editor ` | Redis Editor | All `redis` permissions except for  
` redis.instances.create redis.instances.delete redis.instances.upgrade redis.instances.import redis.instances.export redis.instances.updateAuth redis.instances.getAuthString redis.operations.delete ` | Manage Memorystore for Redis instances. Can't create or delete instances.  
` roles/redis.viewer ` | Redis Viewer | All `redis` permissions except for  
` redis.instances.create redis.instances.delete redis.instances.update redis.instances.upgrade redis.instances.import redis.instances.export redis.instances.updateAuth redis.instances.getAuthString redis.operations.delete ` | Read-only access to all Memorystore for Redis resources.  
  
### Permissions and their roles

The following table lists each permission that Memorystore for Redis supports and the Memorystore for Redis roles that include it:

Permission | Redis role | Basic role  
---|---|---  
` redis.instances.list ` | Redis Admin  
Redis Editor  
Redis Viewer | Reader  
` redis.instances.get ` | Redis Admin  
Redis Editor  
Redis Viewer | Reader  
` redis.instances.create ` | Redis Admin | Writer  
` redis.instances.update ` | Redis Admin  
Redis Editor | Writer  
` redis.instances.updateAuth ` | Redis Admin | Writer  
` redis.instances.getAuthString ` | Redis Admin | Writer  
` redis.instances.delete ` | Redis Admin | Writer  
`redis.instances.upgrade` |  Redis Admin  | Writer  
`redis.instances.import` |  Redis Admin  | Writer  
`redis.instances.export` |  Redis Admin  | Writer  
` redis.locations.list ` | Redis Admin  
Redis Editor  
Redis Viewer | Reader  
` redis.locations.get   
` | Redis Admin  
Redis Editor  
Redis Viewer | Reader  
` redis.operations.list ` | Redis Admin  
Redis Editor  
Redis Viewer | Reader  
` redis.operations.get ` | Redis Admin  
Redis Editor  
Redis Viewer | Reader  
` redis.operations.delete ` | Redis Admin | Writer  
  
### Custom roles

If the predefined roles do not address your unique business requirements, you can define your own custom roles with permissions that you specify. To support this, IAM offers [custom roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom). When you create custom roles for Memorystore for Redis, make sure that you include both `resourcemanager.projects.get` and `resourcemanager.projects.list`. Otherwise, the Google Cloud console will not function correctly for Memorystore for Redis. For more information, see [Permission dependencies](https://docs.cloud.google.com/iam/docs/roles-overview#custom-roles-permission-dependencies). To learn how to create a custom role, see [Creating a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role).

### Required permissions for common tasks in the Google Cloud console

To enable a user to work with Memorystore for Redis using the Google Cloud console, the user's role must include the `resourcemanager.projects.get` and the `resourcemanager.projects.list` permission.

The following table provides the other permissions required for some common tasks in the Google Cloud console:

Task | Required additional permissions  
---|---  
Display the instance listing page | ` redis.instances.get redis.instances.list `  
Create and edit an instance | ` redis.instances.create redis.instances.get redis.instances.list compute.networks.list `  
Delete an instance | ` redis.instances.delete redis.instances.get redis.instances.list `  
Connect to an instance from Cloud Shell | ` redis.instances.get redis.instances.list redis.instances.update `  
View instance information | ` redis.instances.get monitoring.timeSeries.list `  
Import and export RDB backup files |  ` redis.instances.import  
redis.instances.export `  
Upgrade the Redis version of an instance |  ` redis.instances.upgrade `  
  
### Required permissions for gcloud commands

To enable a user to work with Memorystore for Redis using `gcloud` commands, the user's role must include the `resourcemanager.projects.get` and the `resourcemanager.projects.list` permission.

The following table lists the permissions that the user invoking a `gcloud` command must have for each `gcloud redis` subcommand:

Command | Required permissions  
---|---  
`gcloud redis instances auth` |  ` redis.instances.updateAuth  
redis.instances.getAuthString `  
`gcloud redis instances create` |  ` redis.instances.get redis.instances.create `  
`gcloud redis instances delete` | `redis.instances.delete`  
`gcloud redis instances update` |  ` redis.instances.get redis.instances.update `  
`gcloud redis instances list` | `redis.instances.list  
`  
`gcloud redis instances describe` | `redis.instances.get`  
`gcloud redis instances import` | `redis.instances.import`  
`gcloud redis instances export` | `redis.instances.export`  
`gcloud redis instances upgrade` | `redis.instances.upgrade`  
`gcloud redis operations list` | `redis.operations.list`  
`gcloud redis operations describe` | `redis.operations.get`  
`gcloud redis regions list` | `redis.locations.list`  
`gcloud redis regions describe` | `redis.locations.get`  
`gcloud redis zones list` | `redis.locations.list`  
  
### Required permissions for API methods

The following table lists the permissions that the caller must have to call each method in the Memorystore for Redis API or to perform tasks using Google Cloud tools that use the API (such as the Google Cloud console or the `gcloud`command line tool):

**Note** : To call a method, in addition to the permissions in the following table, you must also have the required scopes. These scopes are described in the method's reference page. For more information, see [Authorize requests](https://docs.cloud.google.com/sql/docs/mysql/admin-api#auth).

All permissions are applied to the project. You can't apply different permissions based on the instance or on other lower-level objects.

Method | Required permissions  
---|---  
`locations.get` | `redis.locations.get`  
`locations.list` | `redis.locations.list`  
`instances.create` | `redis.instances.create`  
`instances.delete` | `redis.instances.delete`  
`instances.get` | `redis.instances.get`  
`instances.list` | `redis.instances.list`  
`instances.patch` | `redis.instances.update`  
`instances.import` | `redis.instances.import`  
`instances.export` | `redis.instances.export`  
`instances.upgrade` | `redis.instances.upgrade`  
`operations.get` | `redis.operations.get`  
`operations.list` | `redis.operations.list`  
  
## The Memorystore for Redis service account

Each Memorystore for Redis instance has a service account that it uses to communicate with other Google Cloud resources.

Sometimes (like when [exporting](https://docs.cloud.google.com/memorystore/docs/redis/access-control#permissions_for_the_service_account), or [using CMEK](https://docs.cloud.google.com/memorystore/docs/redis/cmek#about_service_accounts)) you must grant specific roles or permissions to the service account.

#### Memorystore for Redis service account format

Your instance's service account uses one of two different formats, depending on when it was created.

  * The first format is:

`PROJECT_NUMBER-compute@developer.gserviceaccount.com`

  * The second format is:

`service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com`


**Note:** For the first format, replace PROJECT_NUMBER with the project number of your default Compute Engine service account. For the second format, replace PROJECT_NUMBER with the project number of your Google Cloud project. Also, for more information about which format your instance's service account uses, see [View your instance's service account](https://docs.cloud.google.com/memorystore/docs/redis/access-control#view_your_instances_service_account).

#### Known issues

Sometimes a service account using the `[PROJECT_NUMBER]-compute@developer.gserviceaccount.com` format can conflict with your organization policy. For more information, and steps to resolve this issues, see [Issues with the domain restricted sharing organization policy](https://docs.cloud.google.com/memorystore/docs/redis/troubleshooting#issues_with_the_domain_restricted_sharing_organization_policy).

#### View your instance's service account

To view the service account for your instance, run the following command and make a note of the service account listed under `persistenceIamIdentity`:
    
    
    gcloud redis instances describe [INSTANCE_ID] --region=[REGION]
    

## Redis AUTH permissions

The following table shows the minimum permissions a user needs to complete some basic Memorystore for Redis [AUTH](https://docs.cloud.google.com/memorystore/docs/redis/auth-overview) tasks.

Permissions needed | Create a Memorystore instance with Redis AUTH enabled | Enable / disable AUTH on an existing Redis instance | View the AUTH string | View whether AUTH is enabled / disabled for a Redis instance  
---|---|---|---|---  
`redis.instances.create` |  ✓  |  X  |  X  |  X   
`redis.instances.update` |  X  |  ✓  |  X  |  X   
`redis.instances.get` |  X  |  X  |  X  |  ✓  |  `redis.instances.updateAuth` |  ✓  |  ✓  |  X  |  X   
`redis.instances.getAuthString` |  X  |  X  |  ✓  |  X   
  
## In-transit encryption permissions

The table below shows permissions required for enabling and managing [In-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption) for Memorystore for Redis.

Permissions needed | Create a Memorystore instance with in-transit encryption | Download the Certificate Authority  
---|---|---  
`redis.instances.create` |  ✓  |  X   
`redis.instances.get` |  X  |  ✓   
  
## Maintenance policy permissions

The table below shows permissions required for managing the [Maintenance policy](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy) for Memorystore for Redis.

Permissions needed | Create a Memorystore instance with a maintenance policy enabled | Create or modify maintenance policies on an existing Memorystore instance | View the maintenance policy settings | Reschedule maintenance  
---|---|---|---|---  
`redis.instances.create` |  ✓  |  X  |  X  |  X   
`redis.instances.update` |  X  |  ✓  |  X  |  X   
`redis.instances.get` |  X  |  X  |  ✓  |  X   
`redis.instances.rescheduleMaintenance` |  X  |  X  |  X  |  ✓   
  
## Required permissions for import and export

Using custom roles for importing and exporting requires two separate custom roles. One custom role for the user, and an additional custom role for the Redis instance's service account. The custom role for the service account uses Cloud Storage bucket level permissions.

To find the service account for your instance, see [View your instance's service account](https://docs.cloud.google.com/memorystore/docs/redis/access-control#view_your_instances_service_account)

### Permissions for the service account

Note that you only need to grant storage permissions to the service account at the bucket-level, not the entire project. For instructions, see [Adding a principal to a bucket-level policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).

Once you grant your service account bucket-level permissions, you can ignore the message that says "Memorystore is unable to verify if service account xxxx@xxxx.gserviceaccount.com has the permissions required to import/export. For help verifying or updating permissions, contact your project's administrator. For the required permissions, see import/export permissions documentation." If you apply the permissions listed below to custom roles for the user account and the service account, the import/export will succeed.

Permissions for custom role for service account | Import with gcloud | Export with gcloud | Import with Google Cloud console | Export with Google Cloud console  
---|---|---|---|---  
`storage.buckets.get` | ✓ | ✓ | ✓ | ✓  
`storage.objects.get` | ✓ | X | ✓ | X  
`storage.objects.create` | X | ✓ | X | ✓  
`storage.objects.delete` | X | Optional.   
(Grants permission to overwrite existing RDB file). | X | Optional.   
(Grants permission to overwrite existing RDB file).  
  
### Permissions for the user account

Permissions for custom role for user account | Import with gcloud | Export with gcloud | Import with Google Cloud console | Export with Google Cloud console  
---|---|---|---|---  
`resourcemanager.projects.get` | X | X | ✓ | ✓  
`redis.instances.get` | ✓ | ✓ | ✓ | ✓  
`redis.instances.list` | X | X | X | X  
`redis.instances.import` | ✓ | X | ✓ | X  
`redis.instances.export` | X | ✓ | X | ✓  
`redis.operations.get` | X | ✓ | ✓ | ✓  
`redis.operations.list` | X | X | ✓ | ✓  
`redis.operations.cancel` | ✓ | ✓ | ✓ | ✓  
`storage.buckets.list` | X | X | ✓ | ✓  
`storage.buckets.get` | X | X | ✓ | ✓  
`storage.objects.list` | X | X | ✓ | ✓  
`storage.objects.get` | X | X | ✓ | ✓  
  
## What's next

  * Learn how to [grant and revoke access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs).
  * Learn more about [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
