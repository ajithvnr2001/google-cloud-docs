---
url: https://docs.cloud.google.com/memorystore/docs/cluster/access-control/
title: Access control with IAM \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:18.696610+00:00
---

# Access control with IAM  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the Identity and Access Management roles available for Memorystore for Redis Cluster, and the associated permissions for those roles. Memorystore for Redis Cluster and Memorystore for Redis use the same IAM roles. The permissions these roles grant for Memorystore for Redis Cluster are listed on this page. The permissions these roles grant for Memorystore for Redis are listed on the [Memorystore for Redis Access control](https://docs.cloud.google.com/memorystore/docs/redis/access-control) page. Although the permissions are listed separately on both pages, the roles grant permissions for both Memorystore for Redis Cluster and Memorystore for Redis.

Memorystore for Redis Cluster uses a different permissions naming structure than Memorystore for Redis:

  * Memorystore for Redis Cluster instances use `redis.clusters.[PERMISSION]`.
  * Memorystore for Redis instances use `redis.instances.[PERMISSION]`.



To view more information about the Redis Admin role, see [Predefined roles](https://docs.cloud.google.com/memorystore/docs/redis/access-control#predefined_roles).

To learn how to grant the role to a user in your project, see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role).

**Note:** Modifications to IAM settings for Memorystore for Redis Cluster take on the order of minutes to take effect.

## Predefined roles

The following predefined roles are available for Memorystore for Redis Cluster. If you update a role for an [Identity and Access Management principal](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity), the change takes several minutes to [take effect](https://docs.cloud.google.com/iam/docs/access-change-propagation).

Role | Name | Redis permissions | Description  
---|---|---|---  
` roles/owner ` | Owner | ` redis.* ` | Full access and control for all Google Cloud resources; manage user access  
` roles/editor ` | Editor | All `redis` permissions except for` *.getIamPolicy` & `.setIamPolicy` | Read-write access to all Google Cloud and Redis resources (full control except for the ability to modify permissions)  
` roles/viewer ` | Viewer | ` redis.*.get redis.*.list ` | Read-only access to all Memorystore for Redis Cluster resources. However, you can't use this permission to view data that's associated with the resources.  
` roles/redis.admin ` | Redis Admin | ` redis.* ` | Full control for all Memorystore for Redis Cluster resources.  
` roles/redis.editor ` | Redis Editor | All `redis` permissions except for  
` redis.clusters.create redis.clusters.delete redis.clusters.connect ` | Manage Memorystore for Redis Cluster instances. Can't create or delete instances.  
` roles/redis.viewer ` | Redis Viewer | All `redis` permissions except for  
` redis.clusters.create redis.clusters.delete redis.clusters.update redis.clusters.connect redis.operations.delete ` | Read-only access to all Memorystore for Redis Cluster resources.  
` roles/redis.dbConnectionUser ` | Redis Database Connection User | `redis.clusters.connect` | A role that you can assign to users who need to authenticate with IAM authentication.  
  
### Permissions and their roles

The following table lists each permission that Memorystore for Redis Cluster supports and the Memorystore for Redis roles that include it:

Permission | Redis role | Basic role  
---|---|---  
` redis.clusters.list ` | Redis Admin  
Redis Editor  
Redis Viewer | Viewer  
` redis.clusters.get ` | Redis Admin  
Redis Editor  
Redis Viewer | Viewer  
` redis.clusters.create ` | Redis Admin | Owner  
` redis.clusters.update ` | Redis Admin  
Redis Editor | Editor  
` redis.clusters.connect ` | Redis Admin  
Redis Database Connection User | Owner  
` redis.clusters.rescheduleMaintenance ` | Redis Admin | Owner  
  
### Custom roles

If the predefined roles do not address your unique business requirements, you can define your own custom roles with permissions that you specify. To support this, IAM offers [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles). When you create custom roles for Memorystore for Redis Cluster, make sure that you include both `resourcemanager.projects.get` and `resourcemanager.projects.list`. Otherwise, the Google Cloud console will not function correctly for Memorystore for Redis Cluster. For more information, see [Permission dependencies](https://docs.cloud.google.com/iam/docs/understanding-custom-roles#permission_dependencies). To learn how to create a custom role, see [Creating a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role).

## In-transit encryption permissions

The table below shows permissions required for enabling and managing [In-transit encryption](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption) for Memorystore for Redis Cluster.

Permissions needed | Create a Memorystore instance with in-transit encryption | Download the Certificate Authority  
---|---|---  
`redis.clusters.create` |  ✓  |  X   
`redis.clusters.get` |  X  |  ✓   
  
## Network connectivity policy creation role

The permissions described in this section are needed for the Network Admin who is establishing a service connection policy for Memorystore for Redis Cluster, as described in the [Networking](https://docs.cloud.google.com/memorystore/docs/cluster/networking) page.

To establish the policy required for Memorystore cluster creation, the Network Admin must have the `networkconnectivity.googleapis.com/consumerNetworkAdmin` role, which grants the following permissions:

  * networkconnectivity.serviceconnectionpolicies.create
  * networkconnectivity.serviceconnectionpolicies.list
  * networkconnectivity.serviceconnectionpolicies.get
  * networkconnectivity.serviceconnectionpolicies.delete
  * networkconnectivity.serviceconnectionpolicies.update



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
