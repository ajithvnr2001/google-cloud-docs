---
url: https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth/
title: Manage IAM authentication \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:24.436658+00:00
---

# Manage IAM authentication  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Manage IAM authentication Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — IAM group authentication (new clusters only)**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to prepare your AlloyDB for PostgreSQL instance to facilitate database authentication using Identity and Access Management (IAM).

**Note:** IAM group authentication is available in [Preview](https://cloud.google.com/products#product-launch-stages) for new AlloyDB clusters. To enable this feature on an existing cluster, contact your Google Cloud account team.

IAM authentication complements database authentication through [standard PostgreSQL users](https://docs.cloud.google.com/alloydb/docs/database-users/manage-roles), which every AlloyDB cluster supports.

You can authenticate using individual accounts or groups:

  * **Individual accounts** : You add each IAM user or service account to the cluster. You can use IAM or PostgreSQL user roles to authenticate with that cluster.
  * **Groups** : You add an IAM group to the cluster. All members (users and service accounts) of that group inherit the permissions to authenticate. This lets you manage access by managing group membership without adding each member to the cluster individually.



IAM authentication is disabled on AlloyDB instances by default.

To use IAM authentication, complete the following general steps:

  1. Enable IAM individual or group authentication on your instance.
  2. Grant the required roles to the account or group.
  3. Add the account or group to your cluster.
  4. Grant database privileges to the account or group.



## Enable and disable IAM authentication

To enable IAM authentication on an instance, set the database flags.

  * For individual authentication, set [`alloydb.iam_authentication`](https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags#alloydb.iam_authentication) to `on`.
  * For group authentication, set both[`alloydb.iam_authentication`](https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags#alloydb.iam_authentication) and [`alloydb.iam_group_authentication`](https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags#alloydb.iam_group_authentication) to `on`.



To disable IAM authentication, set the flags to `off`.

For more information about setting flags, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

**Caution:** There is a per-minute sign-in quota for each instance, which includes both successful and unsuccessful sign-ins. When the quota is exceeded, sign-ins are temporarily unavailable. We recommend that you avoid frequent sign-ins and restrict sign-ins using authorized networks.

## Grant access to an individual account

To enable IAM access to a new database user, follow these steps:

  1. Update your project's IAM settings to grant AlloyDB database access to the appropriate IAM user or service account.

  2. Create a new database user on your cluster, setting the username as the email address of the IAM user or service account.




To give an IAM account access to other clusters in your project, repeat the last step.

### Update an IAM account with the appropriate role

You can give IAM users or service accounts the ability to authenticate with AlloyDB instances by granting them the following IAM roles:

  * `alloydb.databaseUser`: Lets the user connect to your AlloyDB instance.
  * `serviceusage.serviceUsageConsumer`: Provides the user access to an API that checks permissions.



To do this, follow the instructions on [Grant access to other users](https://docs.cloud.google.com/alloydb/docs/user-grant-access#procedure). In the step where you select a role to grant to the IAM principal, choose `alloydb.databaseUser`.

### Add an IAM user or service account to a cluster

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of the cluster that you want to add a user to.

  3. Click **Users**.

  4. Click **Add user account**.

  5. Select **Cloud IAM**.

  6. In the **Principal** field, enter the IAM principal.

For an IAM user account, provide the full email address of the user account. For example, `dana@example.com`.

For an IAM service account, provide the address of the service account _without_ the `.gserviceaccount.com` suffix. For example, to specify the service account `my-service@my-project.iam.gserviceaccount.com`, you use the value `my-service@my-project.iam`.

**Note:** The shortened service account identifier, which is the email address without the `.gserviceaccount.com` suffix, must not exceed 63 characters. PostgreSQL truncates identifiers longer than 63 characters in the database catalog, which causes IAM authentication to fail. If the shortened address exceeds 63 characters, see the [service account impersonation workaround](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-iam-auth). 
  7. To assign roles other than the default `alloydbsuperuser` to the user, follow these steps:

     1. Enter the name of the role in **Roles**.
     2. To add the role, press `Enter` or `Tab`.
     3. Select **x** for any role that you want to remove for that user.

For more information, see [Predefined roles](https://docs.cloud.google.com/alloydb/docs/database-users/overview#predefined-roles)

  8. Click **Add**.




### gcloud

To create a PostgreSQL database user based on an IAM user or service account, use the [`gcloud alloydb users create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/create) command.
    
    
    gcloud alloydb users create USERNAME \
    --cluster=CLUSTER \
    --region=REGION \
    --type=IAM_BASED

Replace the following variables:

  * `USERNAME`: identifier for the IAM user that you want to add as a new database user.

For an IAM user account, provide the full email address of the user account. For example, `dana@example.com`.

For an IAM service account, provide the address of the service account _without_ the `.gserviceaccount.com` suffix. For example, to specify the service account `my-service@my-project.iam.gserviceaccount.com`, you use the value `my-service@my-project.iam`.

**Note:** The shortened service account identifier, which is the email address without the `.gserviceaccount.com` suffix, must not exceed 63 characters. PostgreSQL truncates identifiers longer than 63 characters in the database catalog, which causes IAM authentication to fail. If the shortened address exceeds 63 characters, see the [service account impersonation workaround](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-iam-auth). 
  * `CLUSTER`: ID of the cluster to create this database user account within.

  * `REGION`: ID of the region where the cluster resides—for example, `us-central1`.




### Grant appropriate database permissions to IAM users

When you add an IAM user to an AlloyDB cluster, the user has no privileges on any databases by default except for the database objects that [PUBLIC](https://www.postgresql.org/docs/17/ddl-priv.html) can access.

If users need additional access, grant more privileges using the [`GRANT` PostgreSQL statement](https://www.postgresql.org/docs/17/sql-grant.html):
    
    
    GRANT SELECT ON TABLE_NAME TO "USERNAME";
    

Replace the following variables:

  * `USERNAME`: email address for the user. You must include double quotes around the address.

  * `TABLE_NAME`: Name of the table that you want to give the user access to.




## Remove an IAM user or service account from a cluster

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of the cluster you want to remove the user from.

  3. Click **Users**.

  4. On the row representing the user you want to remove, click more_vert **Open actions for this user**.

  5. Select **Remove**.

  6. In the **Remove user account?** dialog, click **Remove**.




### gcloud

Use [the `gcloud alloydb users delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/delete).
    
    
    gcloud alloydb users delete USERNAME \
    --cluster=CLUSTER \
    --region=REGION

Replace the following:

  * `USERNAME`: identifier of the IAM user that you want to remove from the cluster.

For an IAM user account, provide the full email address of the user account. For example, `dana@example.com`.

For an IAM service account, provide the address of the service account _without_ the `.gserviceaccount.com` suffix. For example, to specify the service account `my-service@my-project.iam.gserviceaccount.com`, you use the value `my-service@my-project.iam`.

**Note:** The shortened service account identifier, which is the email address without the `.gserviceaccount.com` suffix, must not exceed 63 characters. PostgreSQL truncates identifiers longer than 63 characters in the database catalog, which causes IAM authentication to fail. If the shortened address exceeds 63 characters, see the [service account impersonation workaround](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-iam-auth). 
  * `CLUSTER`: ID of the cluster to remove this user from.

  * `REGION`: ID of the region where the cluster resides. For example, `us-central1`.




## Grant access to an IAM group

To use group authentication ([Preview](https://cloud.google.com/products#product-launch-stages)), you add an IAM group to the AlloyDB cluster.

### Add an IAM group to a cluster

  1. Assign the `alloydb.databaseUser` and `serviceusage.serviceUsageConsumer` roles to the group account. For more information, see Update an IAM account with appropriate role.

A maximum of 200 IAM groups can exist on a cluster at any time. Inactive groups count towards this limit.

IAM group names can be only 63 characters long.

If you have an IAM group with a name that exceeds the length limitation, then you can nest it under a parent group with a valid name. You must add the parent group to the cluster before you can use the nested group.

  2. To create a database user for the group, use the `gcloud alloydb users create` command with the `--type=IAM_GROUP` flag.
         
         gcloud beta alloydb users create GROUP_EMAIL \
         --cluster=CLUSTER \
         --region=REGION \
         --type=IAM_GROUP

**Note:** If you delete an IAM group from IAM and then immediately recreate that group, the group might not be usable right away. IAM group deletion and recreation take time to propagate.



### Add members of a group automatically

When you add an IAM group to a cluster, all members (users and service accounts) of that group inherit the permissions to authenticate. don't need to add the members individually. After a member signs in for the first time, AlloyDB creates an account for them automatically.

### Grant database privileges to an IAM group

You grant database privileges to groups instead of individual users.

Run the `GRANT` statement from the `psql` command line:
    
    
    GRANT SELECT ON TABLE_NAME TO "GROUP_NAME";
    

  * `GROUP_NAME`: The email address of the group. You must use quotes because the string contains special characters.
  * `TABLE_NAME`: The name of the table.



## Delete an IAM group from a cluster

To delete an IAM group from an AlloyDB cluster, revoke the group permissions in the Google Cloud console and delete the corresponding group user from the AlloyDB cluster.

  1. Revoke IAM permissions:

     1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

     2. Find the IAM group from which you want to remove access.

     3. Remove the `roles/alloydb.databaseUser` role and any other AlloyDB-related roles that grant access to the cluster. This action prevents members of the group from authenticating.

  2. Delete the group user from the AlloyDB cluster:

Use the Google Cloud CLI to delete the user representing the IAM group from the AlloyDB cluster. The username is typically the email address of the IAM group.
         
         gcloud alloydb users delete GROUP_EMAIL_ADDRESS \
         --cluster=CLUSTER_ID \
         --region=REGION_ID

Replace the following:

     * `GROUP_EMAIL_ADDRESS`: the full email address of the IAM group—for example, `my-group@example.com`.
     * `CLUSTER_ID`: the ID of your AlloyDB cluster.
     * `REGION_ID`: the region where your AlloyDB cluster is located—for example, `us-central1`.
  3. Optional: Delete the group from Cloud Identity:

**Caution:** Deleting a group is permanent and can't be undone. Members lose access to resources shared with the deleted group, and messages sent to the group's address aren't delivered.

You need appropriate administrator privileges (like Groups Admin) in your Cloud Identity account to delete groups. Group owners can typically only delete groups that they own.

Changes to IAM permissions and group memberships can take time to propagate, potentially 15 minutes or more.

     1. Make sure that you have [appropriate administrator privileges](https://knowledge.workspace.google.com/admin/users/view-role-assignments-and-privileges) like Groups Admin in your Cloud Identity account. Group owners can only delete the groups that they own. For more information, see [Prebuilt administrator roles](https://knowledge.workspace.google.com/admin/users/prebuilt-administrator-roles).

     2. Run the following Cloud Identity gcloud CLI command:
            
            gcloud identity groups delete GROUP_EMAIL_ADDRESS

     3. When you revoke the sign-in permission `alloydb.databaseUser` for an IAM group in Cloud Identity, you must also delete the group from the AlloyDB cluster to make sure that access is completely removed.




## Migrate existing users to IAM group authentication

Existing individual IAM users don't use group authentication. You can migrate them by following these steps:

  1. Add the users to an IAM group.
  2. Add the group to your cluster.
  3. Assign the group the required roles.
  4. Assign database privileges to the group.
  5. Delete the existing individual user from your cluster. Make sure that you transfer ownership if intended.



When the user signs in again, AlloyDB recreates the account as a group user.

## Troubleshoot group authentication

Use the following information to troubleshoot group authentication issues.

### An existing account is not inheriting privileges

If an account isn't inheriting privileges from a group, follow these steps:

  1. List the users.
         
         gcloud alpha alloydb users list --cluster=CLUSTER --region=REGION

  2. If the type is `ALLOYDB_IAM_USER` or `ALLOYDB_IAM_SERVICE_ACCOUNT`, remove the account. It doesn't inherit group privileges.

  3. To recreate the account with the correct group type, sign in again to the instance with the user or service account. Signing in again to the instance re-creates the account with the correct account type of `ALLOYDB_IAM_GROUP_USER` or `ALLOYDB_IAM_GROUP_SERVICE_ACCOUNT`.




## What's next

  * [Connect using an IAM account](https://docs.cloud.google.com/alloydb/docs/connect-iam)
  * [Troubleshoot IAM authentication](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-iam-auth)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
