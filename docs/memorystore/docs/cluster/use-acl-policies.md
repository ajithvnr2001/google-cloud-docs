---
url: https://docs.cloud.google.com/memorystore/docs/cluster/use-acl-policies/
title: Secure access to your clusters by using ACL policies \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:10.749814+00:00
---

# Secure access to your clusters by using ACL policies  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/use-acl-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Secure access to your clusters by using ACL policies Stay organized with collections  Save and categorize content based on your preferences. 

By using access control list (ACL) policies in Memorystore for Redis Cluster, you can secure access to your clusters. You can enable fine-grained security by restricting user and service access to specific keys, commands, and Pub/Sub channels.

The following are sample use cases for using ACL policies to secure access to clusters:

  * **Provide role-based access control (RBAC)** : create distinct user profiles for different components of your applications. For example, a web frontend can have read-only access, while a background worker service has read-write access. This prevents accidental data leaks or tampering.
  * **Prevent destructive commands** : restrict dangerous commands such as [`FLUSHALL`](https://redis.io/commands/flushall/), [`FLUSHDB`](https://redis.io/commands/flushdb/), or [`CONFIG`](https://redis.io/commands/config/) to high-level administrators only. This protects data integrity from software bugs or manual errors.
  * **Provide multi-tenant application security** : use separate ACL users for different microservices or external partners. This ensures that users of one service can't read or modify keys that another service owns.

Memorystore for Redis Cluster doesn't offer resource-level multi-tenancy. Even though keyspaces are divided, one service might consume a disproportionate amount of memory or CPU.

  * **Perform read-only analytics and monitoring** : assign a dedicated user that can use only [`GET`](https://redis.io/commands/get/) or other read-only commands (for example, [`SCAN`](https://redis.io/commands/scan/) or [`TYPE`](https://redis.io/commands/type/)) to analytics engines or dashboard applications. This prevents accidental writes or data deletion.

  * **Secure database keys** : restrict applications to interact only with keys that match specific patterns (for example, `app1:*`). This provides the logical separation of data within a cluster.

  * **Disable Lua scripts** : use ACL policies to manage [Lua scripting capabilities](https://redis.io/docs/latest/develop/programmability/eval-intro/) for your clusters. Disabling or restricting Lua scripts can be useful for performance tuning, simplifying the functionality of your clusters, or adhering to security guidelines for your organization.


**Important** : If you use [cross-region replication](https://docs.cloud.google.com/memorystore/docs/cluster/about-cross-region-replication) to create secondary clusters from a primary cluster, then you must manage ACL policies for primary and secondary clusters independently. Memorystore for Redis Cluster doesn't propagate ACL policies from primary clusters to secondary clusters.

## Before you begin

Before you begin to use ACL policies, complete the instructions in this section.

### Use the Google Cloud console, Google Cloud CLI, and APIs

To use the Google Cloud console, Google Cloud CLI, and APIs, do the following:

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).  


**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

  
[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)
  2. Make sure that billing is enabled for your project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  3. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI.

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. You need at least gcloud CLI version `440.0.0` to access the Memorystore for Redis Cluster gcloud CLI commands.

  4. Enable the Memorystore for Redis API.   
[Memorystore for Redis](https://console.cloud.google.com/apis/library/redis.googleapis.com)
  5. Enable the Network Connectivity API.   
[Network Connectivity API](https://console.cloud.google.com/apis/library/networkconnectivity.googleapis.com)
  6. Enable the Service Consumer Management API.   
[Service Consumer Management API](https://console.cloud.google.com/apis/library/serviceconsumermanagement.googleapis.com)



### Assign Memorystore for Redis Cluster roles

Make sure that either you or the user account that you're using has the [required permissions](https://docs.cloud.google.com/memorystore/docs/cluster/access-control) for the action that you need to perform.

To perform all ACL policy operations, use the **Redis Admin** (`roles/redis.admin`) and **Redis Editor** (`roles/redis.editor`) roles. To view ACL policies only, use the **Redis Viewer** (`roles/redis.viewer`) role.

### Assign Memorystore for Redis Cluster permissions

In addition to the Redis Admin, Redis Editor, and Redis Viewer roles, to use ACL policies in Memorystore for Redis Cluster, you need the following permissions:

Action | Permission  
---|---  
Create an ACL policy | `redis.aclPolicies.create`  
Assign an ACL policy to a cluster | `redis.clusters.update`  
View information about ACL policies | `redis.aclPolicies.list`  
View information about an ACL policy | `redis.aclPolicies.get`  
View information about ACL policy revisions | `redis.aclPolicyRevisions.list`  
View information about an ACL policy revision | `redis.aclPolicyRevisions.get`  
Modify an ACL policy | `redis.aclPolicies.update`  
Remove an ACL policy from a cluster | `redis.clusters.update`  
Delete an ACL policy | `redis.aclPolicies.delete`  
  
## Create an ACL policy

By creating ACL policies in Memorystore for Redis Cluster, you enhance the security of your clusters by restricting user access to specific keys, commands, and Pub/Sub channels.

You can create an ACL policy by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. In the side navigation panel, click **ACL policies**.

  3. In the **ACL policies** page, click **Create policy**.

  4. In the **Create policy** window, do the following:

     1. In the **Policy name** field, enter a name for the ACL policy. The policy name must contain only lowercase letters, numbers, and hyphens. It must also start with a letter and be unique in its region.

     2. From the **Region** menu, select the region where you want Memorystore for Redis Cluster to create the ACL policy.

**Important** : After you create the ACL policy, you can't change the policy's name or region. Also, you can assign this policy only to clusters that are located in the same region as the policy.

For example, if you select `us-central1` as the region for the policy, then you can assign the policy only to clusters that are also located in the `us-central1` region.

     3. Click **Add rule**.

     4. In the **User ID** field, enter the name of the user to which the ACL policy is to apply.

     5. In the **Access string** field, enter the access string for the policy. The access string is a human-readable rule that defines the specific permissions for the user.

For example, if you want to give the `default` superuser read and write permissions to all ACL keys for the cluster, then populate the **User ID** and **Access string** fields, as follows:

User ID | Access string  
---|---  
`default` | `on ~* &* +@all`  
  
This rule grants the following permissions to the `default` user:

        * `on`: the user is active and enabled for authentication
        * `~*`: the user has read-access and write-access to all possible keys
        * `&*`: the user has access to all Pub/Sub channels
        * `+@all`: the user can run all available commands
**Important** : Unless you include a rule in your ACL policy that restricts or blocks access for the `default` user, this user retains their full access permissions.

For more information about other ACL rules and policies that you can create, see [ACL](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/) in the Redis documentation.

     6. Repeat steps c through e for additional ACL rules that you want to create for the policy.

     7. Click **Create**.




### gcloud

To create an ACL policy, use the [`gcloud redis acl-policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/create) command.
    
    
    gcloud redis acl-policies create ACL_POLICY_NAME \
    --region=REGION \
    --rules=rule="on ~* +@all",username="lucian" \
    --rules=rule="on +get",username="taylor"
    

Make the following replacements:

  * ACL_POLICY_NAME: the name of the ACL policy that you're creating. The policy name must contain only lowercase letters, numbers, and hyphens. It must also start with a letter and be unique in its region.
  * REGION: the region where you want the ACL policy to be located.



This policy uses basic token-based authentication and has rules that perform the following actions:

  * The first rule grants `lucian` the `~* +@all` permission. This permission lets the user access all keys and run all commands.
  * The second rule grants the `get` permission to `taylor`. This permission lets the user retrieve the values associated with keys. It restricts the user's access to read-only data operations, and prevents the user from modifying keys.



To create rules for an ACL policy that uses Identity and Access Management (IAM) authentication, we recommend that you use IAM principals for the usernames (for example, the users' email addresses).
    
    
    gcloud redis acl-policies create ACL_POLICY_NAME \
    --region=REGION \
    --rules=rule="on ~* +@all",username="lucian@example.com" \
    --rules=rule="on +get",username="taylor@example.com"
    

To create a rule for an ACL policy that doesn't use authentication, the user must be the `default` user.
    
    
    gcloud redis acl-policies create ACL_POLICY_NAME \
    --region=REGION \
    --rules=rule="on ~* +@all",username="default"
    

For more information about basic token-based authentication and IAM authentication, see [Secure access to your clusters by using basic token-based authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-basic-auth) and [About IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth).

**Important** : Unless you include a rule in your ACL policy that restricts or blocks access for the `default` user, this user retains their full access permissions.

After you create the ACL policy, you can't change the policy's name or region. Also, you can assign this policy only to clusters that are located in the same region as the policy.

For example, if you specify `us-central1` as the region for the policy, then you can assign the policy only to clusters that are also located in the `us-central1` region.

For more information about other ACL rules and policies that you can create, see [ACL](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/) in the Redis documentation.

## Assign an ACL policy to a cluster

By assigning an ACL policy to a cluster, or by replacing an assigned policy, you enable Memorystore for Redis Cluster to apply the rules of the policy to the cluster. As a result, you restrict user access to specific keys, commands, and Pub/Sub channels.

You can assign an ACL policy to a cluster by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important** : If you want to assign an ACL policy to an existing cluster, then the maintenance version must be `REDISCLUSTER_20260626_00_01` and later. For more information about updating the maintenance version of a cluster, see [ Self-service maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/self-service-maintenance).

If you assign a policy that restricts actions for a user, and the user attempts to perform those actions, then the user receives an error message and the activity appears in the Data Access audit logs. For more information about these logs, see [Monitor access using audit logs](https://docs.cloud.google.com/memorystore/docs/cluster/audit-logs).

If you don't enable either Identity and Access Management (IAM) authentication or basic token-based authentication for a cluster, then any user who connects to the cluster does so as the `default` user. Because of this, any ACL policy that you assign to the cluster must contain rules exclusively for this user. For more information about these authentication types, see [Manage IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth) and [Secure access to your clusters by using basic token-based authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-basic-auth).

### Assign a policy to a new cluster

To create a cluster and assign an ACL policy to the cluster, see [Create instances](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances).

### Assign a policy to an existing cluster

To increase the security of an existing cluster, you can assign an ACL policy to the cluster.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the ID of the cluster to which you want to assign an ACL policy.

  3. On the **Cluster at a glance** page, scroll to the **Security** card.

  4. Next to the **ACL policy** field, click **Edit** (_edit_).

  5. In the **Edit ACL policy** window, do the following:

     1. From the **Policy** menu, select the policy that you want to assign to the cluster.

     2. Click **Update cluster.**




### gcloud

To assign an ACL policy to an existing cluster, use the [`gcloud redis clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/update) command.
    
    
    gcloud redis clusters update CLUSTER_ID \
    --update_mask=acl_policy \
    --acl-policy=ACL_POLICY_NAME \
    --region=REGION
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster to which you're assigning the ACL policy
  * ACL_POLICY_NAME: the name of the ACL policy
  * REGION: the region where the cluster is located



## View information about ACL policies

Viewing information about ACL policies in Memorystore for Redis Cluster helps you to maintain security, ensures the operational stability of your environment, and lets you audit in-memory data. These policies define which users can read or modify particular key patterns, run specific commands, or access specific Pub/Sub channels.

You can view information about ACL policies by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. In the side navigation panel, click **ACL policies**.

In the **ACL policies** page, you can view the following information about each ACL policy:

     * **Policy ID** : the unique ID of the policy
     * **Location** : the region where the policy is located
     * **Created at** : the date and time that the policy was created
     * **Updated at** : the date and time that the policy was last updated
     * **Number of rules** : the total number of rules for the policy
     * **Used by clusters** : the clusters that are assigned to the policy



### gcloud

To view information abut ACL policies, use the [`gcloud redis acl-policies list`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/list) command.
    
    
    gcloud redis acl-policies list
    --region=REGION
    

Replace REGION with the region where the ACL policy is located.

## View information about an ACL policy

By viewing information about an ACL policy in Memorystore for Redis Cluster, you can perform security audits, troubleshoot access errors, and enforce principle-of-least-privilege by verifying user commands, key permissions, and access to Pub/Sub channels. In addition, administrators can view an ACL policy to ensure that your applications have the appropriate access and to detect overly permissive rules.

You can view information about an ACL policy by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). To view this information, use the [`gcloud redis acl-policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/describe) command.
    
    
    gcloud redis acl-policies describe ACL_POLICY_NAME \
    --region=REGION
    

Make the following replacements:

  * ACL_POLICY_NAME: the name of the ACL policy about which you want to view information
  * REGION: the region where the ACL policy is located



## View information about ACL policy revisions

When you create an ACL policy, Memorystore for Redis Cluster creates a version (revision) for the policy. Each time that you modify the policy, Memorystore for Redis Cluster creates a subsequent policy revision.

Because Memorystore for Redis Cluster generates these revisions automatically, you can use them for internal tracking and auditing purposes. In addition, viewing the revisions lets you view the exact contents of the ACL policy at each historical version.

By using ACL policy revisions, you can track which clusters are using which revision of a policy. This helps you to maintain visibility and ensure that clusters are on the correct version during periods of eventual consistency after a policy update.

You can view information about ACL policy revisions by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important** : You can't revert a cluster to an older revision of an ACL policy because Memorystore for Redis Cluster automatically updates clusters to use the latest compatible revisions of their assigned policies. If you need to revert a cluster to a previous configuration, then you must either create a policy with those configuration settings or modify the existing policy to replicate the older revision.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. In the side navigation panel, click **ACL policies**.

  3. In the **ACL policies** page, click the ID of the ACL policy that has revisions you want to view. In the **ACL policy revisions** page, the following information appears:

     * **Revision ID** : the ID of each ACL policy revision
     * **Revision number** : the number of each ACL policy revision
     * **Location** : the region where each ACL policy revision is located
     * **Created on** : the date and time that each ACL policy revision is created
     * **Attached clusters** : the clusters that are assigned to each ACL policy revision
     * **Snapshot** : detailed information about each ACL policy revision



### gcloud

To view information about ACL policy revisions, use the [`gcloud redis acl-policies revisions list`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/revisions/list) command.
    
    
    gcloud redis acl-policies revisions list \
    --acl-policy=ACL_POLICY_NAME \
    --region=REGION
    

Make the following replacements:

  * ACL_POLICY_NAME: the name of the ACL policy that contains revisions about which you want to view information
  * REGION: the region where the ACL policy is located



In the output, make a note of the revision IDs. You need these IDs to view information about specific ACL policy revisions.

## View information about an ACL policy revision

Viewing an ACL policy revision lets you see its rules, metadata, and a list of all attached clusters. You can view information about an ACL policy revision by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. In the side navigation panel, click **ACL policies**.

  3. In the **ACL policies** page, click the ID of the ACL policy that has a revision you want to view.

  4. In the **ACL policy revisions** page, click the **Snapshot** link next to the ACL policy revision that has information you want to view.




### gcloud

To view information about an ACL policy revision, use the [`gcloud redis acl-policies revisions describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/revisions/describe) command.
    
    
    gcloud redis acl-policies revisions describe ACL_POLICY_REVISION_ID \
    --acl-policy=ACL_POLICY_NAME \
    --region=REGION
    

Make the following replacements:

  * ACL_POLICY_REVISION_ID: the ID of the ACL policy revision about which you want to view information. You noted this ID when you viewed information about ACL policy revisions.
  * ACL_POLICY_NAME: the name of the ACL policy that contains the revision.
  * REGION: the region where the ACL policy is located.



## Modify an ACL policy

By modifying an ACL policy in Memorystore for Redis Cluster, you can enhance security, enforce least-privilege access, and manage operational safety. You can modify a policy by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important** : After you create a policy, you can't change the policy's name or region.

### Add a rule to an ACL policy

To increase the security of an ACL policy, add a rule to it.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. In the side navigation panel, click **ACL policies**.

  3. Next to the ACL policy to which you want to add a rule, click **More actions** (_more_vert_), and then select **Edit**.

  4. In the **Edit policy** window, click **Add rule**.

  5. In the **User ID** field, enter the name of the user to which the ACL policy is to apply.

  6. In the **Access string** field, enter the access string for the policy. For more information about access strings for ACL policies, see Create an ACL policy.

  7. Repeat steps 4 through 6 for additional ACL rules that you want to add to the policy.

  8. Click **Save**.




### gcloud

To add a rule to an ACL policy, use the [`gcloud redis acl-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/update) command.
    
    
    gcloud redis acl-policies update ACL_POLICY_NAME \
    --region=REGION \
    --add-rules=rule="on ~list:*",username="lucian"
    

Make the following replacements:

  * ACL_POLICY_NAME: the name of the ACL policy for which you want to add an ACL rule
  * REGION: the region where the ACL policy is located



This rule grants `lucian` access to all keys that begin with `list:`.

### Modify a rule for an ACL policy

Modifying an ACL rule for an ACL policy provides tighter security, improved operational safety, and more granular user access control. For example, you can revoke permissions during an incident response or enable temporary access for debugging purposes.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. In the side navigation panel, click **ACL policies**.

  3. Next to the ACL policy for which you want to modify a rule, click **More actions** (_more_vert_), and then select **Edit**.

  4. In the **Edit policy** window, click **Add rule**.

  5. In the **User ID** and **Access string** fields, modify the user ID or access string for the policy. For more information about access strings for ACL policies, see Create an ACL policy.

  6. Repeat steps 4 and 5 for additional ACL rules that you want to modify for the policy.

  7. Click **Save**.




### Replace the rules of an ACL policy

Similar to modifying a rule for a policy, replacing the rules of a policy provides tighter security, improved operational safety, and more granular user access control.

### gcloud

To replace the rules of an ACL policy, use the [`gcloud redis acl-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/update) command.
    
    
    gcloud redis acl-policies update ACL_POLICY_NAME \
    --region=REGION \
    --rules=rule="on ~c*che",username="lucian"
    

Make the following replacements:

  * ACL_POLICY_NAME: the name of the ACL policy for which you want to replace the ACL rules
  * REGION: the region where the ACL policy is located



The rule that you're replacing for the policy grants `lucian` access to all keys that match the `c*che` pattern. For example: `cache`, `caache`, and `ceche`.

### Remove a rule from an ACL policy

If an ACL rule no longer applies to an ACL policy, then you can remove it.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. In the side navigation panel, click **ACL policies**.

  3. Next to the ACL policy from which you want to remove a rule, click **More actions** (_more_vert_), and then select **Edit**.

  4. In the **Edit policy** window, next to a rule that you want to remove from the policy, click **Delete rule** (_delete_).

  5. Repeat step 4 for additional ACL rules that you want to remove from the policy.

  6. Click **Save**.




### gcloud

To remove a rule from an ACL policy, use the [`gcloud redis acl-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/update) command.
    
    
    gcloud redis acl-policies update ACL_POLICY_NAME \
    --region=REGION \
    --remove-rules=rule="on ~set",username="lucian"
    

Make the following replacements:

  * ACL_POLICY_NAME: the name of the ACL policy from which you want to remove an ACL rule
  * REGION: the region where the ACL policy is located



Removing this rule revokes its associated permissions for `lucian`. To access the cluster, `lucian` must now connect as the `default` user and is subject to that user's permissions.

**Important** : To use the `remove-rules` parameter successfully, you must provide an exact match for both the rule and the user. If you specify only the user, then Memorystore for Redis Cluster doesn't remove the rule that's associated with the user from the ACL policy.

## Remove an ACL policy from a cluster

If an ACL policy no longer applies to a cluster in Memorystore for Redis Cluster, then you can remove it. You can remove a policy by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the ID of the cluster from which you want to remove an ACL policy.

  3. On the **Cluster at a glance** page, scroll to the **Security** card.

  4. Next to the **ACL policy** field, click **Edit** (_edit_).

  5. In the **Edit ACL policy** window, do the following:

     1. From the **Policy** menu, select **No policy**.

     2. Click **Update cluster.**




### gcloud

To remove an ACL policy from a cluster, use the [`gcloud redis clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/update) command.
    
    
    gcloud redis clusters update CLUSTER_ID \
    --acl-policy="" \
    --region=REGION
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster from which you're removing the ACL policy
  * REGION: the region where the cluster is located



The `""` value for the `acl-policy` parameter is an empty string. This indicates that you want to remove the ACL policy from the cluster.

## Delete an ACL policy

If you no longer need an ACL policy, then you can delete it. You can delete a policy by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important** : Before you can delete an ACL policy, you must remove it from all clusters to which it's assigned. To determine which clusters are assigned to a policy, see View information about ACL policies.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. In the side navigation panel, click **ACL policies**.

  3. Next to the ACL policy that you want to delete, click **More actions** (_more_vert_), and then select **Delete**.

If the **Delete** menu item is deactivated, then the policy is assigned to clusters. Before you can delete the policy, you must remove it from each cluster.

  4. In the **Delete policy** window, do the following:

     1. In the text field, enter the name of the policy.

     2. Click **Delete.**




### gcloud

To delete an ACL policy, use the [`gcloud redis acl-policies delete`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/delete) command.
    
    
    gcloud redis acl-policies delete ACL_POLICY_NAME \
    --region=REGION
    

Make the following replacements:

  * ACL_POLICY_NAME: the name of the ACL policy that you want to delete
  * REGION: the region where the ACL policy is located



## Disable Lua scripts

You can use ACL policies to manage Lua scripting capabilities for your clusters. Disabling or restricting Lua scripts can be useful for performance tuning, simplifying the functionality of your clusters, or adhering to security guidelines for your organization.

### Disable scripting commands for users

To disable Lua scripts so that users can't run them, you must use ACL policies and remove the permissions for the scripting commands from the user's ACL rule string.

Redis categorizes commands into groups. Lua scripting falls under the `@scripting` category. The primary commands for which you must remove user permissions are:

  * [`EVAL`](https://redis.io/commands/eval/): run a Lua script that's provided as a string
  * [`EVALSHA`](https://redis.io/commands/evalsha/): run a Lua script that's cached by using the [`SCRIPT LOAD`](https://redis.io/commands/script-load/) command
  * [`SCRIPT`](https://redis.io/commands/script/) : manage the script cache (for example, [`LOAD`](https://redis.io/commands/script-load/), [`FLUSH`](https://redis.io/commands/script-flush/), [`EXISTS`](https://redis.io/commands/script-exists/), and [`KILL`](https://redis.io/commands/script-kill/))

The `SCRIPT` command includes the following subcommands:

    * [`DEBUG`](https://redis.io/commands/script-debug/)
    * [`EXISTS`](https://redis.io/commands/script-exists/)
    * [`FLUSH`](https://redis.io/commands/script-flush/)
    * [`HELP`](https://redis.io/commands/script-help/)
    * [`KILL`](https://redis.io/commands/script-kill/)
    * [`LOAD`](https://redis.io/commands/script-load/)



You can disable either all scripting commands or a specific command for users. To disable scripting commands, use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and prefix the command or category with a minus sign (`-`).

#### Disable all scripting commands for a user

To disable all scripting commands for a user, either create an ACL policy and assign it to a cluster or modify an ACL policy that's assigned to a cluster.

##### Create a policy

To create an ACL policy to disable all scripting commands for a user named `lucian`, use the [`gcloud redis acl-policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/create) command.
    
    
    gcloud redis acl-policies create POLICY_NAME \
    --region=REGION \
    --rules=rule="on ~* +@all -@scripting",username=lucian
    

Make the following replacements:

  * POLICY_NAME: the name of the ACL policy
  * REGION: the region where you want the ACL policy to be located



After you create the policy, you must assign it to a new or existing cluster.

##### Modify a policy

To modify an ACL policy to disable all scripting commands for `lucian`, use the [`gcloud redis acl-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/update) command.
    
    
    gcloud redis acl-policies update POLICY_NAME \
    --region=REGION \
    --rules=rule="on ~* +@all -@scripting",username=lucian
    

Make the following replacements:

  * POLICY_NAME: the name of the ACL policy
  * REGION: the region where the ACL policy is located



If you want to grant only specific permissions that a user needs, then change the `+@all` value. For example, if you want the user to have access to read-only commands only, then change `+@all` to `+@read`. For more information about the user permissions that you can set, see the Redis ACL documentation.

#### Disable a scripting command for a user

You can target specific commands to disable for a user. For example, you can let the user run all scripting commands except for the [`SCRIPT FLUSH`](https://redis.io/commands/script-flush/) command. To disable a scripting command for a user, either create an ACL policy and assign it to a cluster or modify an ACL policy that's assigned to a cluster.

You can disable any scripting command. For the examples in this section, you disable the `SCRIPT FLUSH` command for the user. For a list of scripting commands, see Disable scripting commands for users.

##### Create a policy

To create an ACL policy to disable the `SCRIPT FLUSH` scripting command for `lucian`, use the [`gcloud redis acl-policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/create) command.
    
    
    gcloud redis acl-policies create POLICY_NAME \
    --region=REGION \
    --rules=rule="on ~* -script|flush",username=lucian
    

Make the following replacements:

  * POLICY_NAME: the name of the ACL policy
  * REGION: the region where you want the ACL policy to be located



After you create the policy, you must assign it to a new or existing cluster.

##### Modify a policy

To modify an ACL policy to disable all scripting commands for `lucian`, use the [`gcloud redis acl-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/update) command.
    
    
    gcloud redis acl-policies update POLICY_NAME \
    --region=REGION \
    --rules=rule="on ~* -script|flush",username=lucian
    

Make the following replacements:

  * POLICY_NAME: the name of the ACL policy
  * REGION: the region where the ACL policy is located



If you want to grant only specific permissions that a user needs, then change the `+@all` value. For example, if you want the user to have access to read-only commands only, then change `+@all` to `+@read`. For more information about the user permissions that you can set, see the Redis ACL documentation.

#### Secure the default user

To disable scripting permissions for the `default` superuser, either create an ACL policy and assign it to a cluster or modify an ACL policy that's assigned to a cluster.

**Important** : If your applications rely on internal Redis functions that use Lua scripts, then removing scripting permissions from the `default` user might cause errors in your applications. Therefore, before applying these restrictions in a production environment, we recommend that you validate your application requirements.

##### Create a policy

To create an ACL policy to disable all scripting commands for the `default` user, use the [`gcloud redis acl-policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/create) command.
    
    
    gcloud redis acl-policies create POLICY_NAME \
    --region=REGION \
    --rules=rule="on ~* +@all -@scripting",username=default
    

Make the following replacements:

  * POLICY_NAME: the name of the ACL policy
  * REGION: the region where you want the ACL policy to be located



After you create the policy, you must assign it to a new or existing cluster.

##### Modify a policy

To modify an ACL policy to disable all scripting commands for the `default` user, use the [`gcloud redis acl-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/acl-policies/update) command.
    
    
    gcloud redis acl-policies update POLICY_NAME \
    --region=REGION \
    --rules=rule="on ~* +@all -@scripting",username=default
    

Make the following replacements:

  * POLICY_NAME: the name of the ACL policy
  * REGION: the region where the ACL policy is located



If you want to grant only specific permissions that the `default` user needs, then change the `+@all` value. For example, if you want this user to have access to read-only commands only, then change `+@all` to `+@read`. For more information about the user permissions that you can set, see the Redis ACL documentation.

## Troubleshoot

This section lists error messages that you might receive when you use ACL policies, the reasons for these messages, and tips to troubleshoot the messages.

Error message | Cause | Troubleshoot  
---|---|---  
`username cannot be empty` | You set an empty string or a string containing only whitespaces for a username in an ACL policy. | Use a username that has alphanumeric or special characters. Then, create the ACL policy again.  
`duplicate username found in ACL policy` | You have duplicate usernames in an ACL policy. | Use the error logs to find the duplicate username. Modify the ACL policy creation request to specify exactly one rule for the username. Then, create the ACL policy again.  
`ACL rule token cannot contain token. use either IAM or Basic Auth features to enable authentication` | You can't use password characters (for example, `<`, `>`, `#`, and `!`) or related commands (for example, `nopass`, `resetpass`, and `reset`) in an ACL policy. | Remove all password characters and related commands from the rules of the ACL policy. Then, create the ACL policy again. To set up authentication, enable basic authentication or [IAM-based authentication](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth).  
`passwords not allowed in ACL rules (token starts with char). use either IAM or Basic Auth features to enable authentication` | You can't use password characters (for example, `<`, `>`, `#`, and `!`) or related commands (for example, `nopass`, `resetpass`, and `reset`) in an ACL policy. | Remove all password characters and related commands from the rules of the ACL policy. Then, create the ACL policy again. To set up authentication, enable basic authentication or [IAM-based authentication](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth).  
`invalid ACL rule syntax` | You didn't [format](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/) an access string in one or more of the ACL policy's rules correctly. | Format the access string correctly.  
`ACL policy is in DELETING state and cannot be used` | You're trying to assign an ACL policy to a cluster, but the policy has a `DELETING` status. | Assign a different ACL policy to the cluster.  
`ACL_POLICY_IN_USE: ACL policy is in use by 1 or more clusters ` | You're trying to delete an ACL policy that's assigned to at least one cluster. | Before you can delete an ACL policy, you must remove it from all clusters to which it's assigned. To determine which clusters are assigned to a policy, see View information about ACL policies.  
`fast-failing the workflow as the resource is in DELETING state` | You're trying to modify an ACL policy that has a `DELETING` status. | If an ACL policy has a `DELETING` status, then you can't modify the policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
