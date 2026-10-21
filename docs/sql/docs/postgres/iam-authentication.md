---
url: https://docs.cloud.google.com/sql/docs/postgres/iam-authentication/
title: IAM authentication \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:30.575367+00:00
---

# IAM authentication  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/iam-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  IAM authentication Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/iam-authentication "View this page for the SQL Server database engine")

Google Cloud offers Identity and Access Management (IAM), which lets you give access to specific Google Cloud resources and prevent unwanted access to other resources. This page describes how Cloud SQL is integrated with IAM and how you can use IAM for managing access to Cloud SQL resources and for database authentication. For a detailed description of Google Cloud IAM, see [IAM documentation](https://docs.cloud.google.com/iam/docs).

Cloud SQL provides a set of [predefined roles](https://docs.cloud.google.com/sql/docs/postgres/iam-roles) designed to help you control access to your Cloud SQL resources. You can also create your own [custom roles](https://docs.cloud.google.com/sql/docs/postgres/iam-roles#custom-roles), if the predefined roles don't provide the sets of permissions you need. In addition, the legacy basic roles (Editor, Viewer, and Owner) are also still available to you, although they don't provide the same fine-grained control as the Cloud SQL roles. In particular, the basic roles provide access to resources across Google Cloud, rather than just for Cloud SQL. For more information about basic Google Cloud roles, see [Basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).

You can set an IAM policy at any level in the [resource hierarchy](https://docs.cloud.google.com/iam/docs/overview#resource-hierarchy): the organization level, the folder level, or the project level. Resources inherit the policies of all of their parent resources.

## IAM references for Cloud SQL

  * [Required permissions for common tasks in the Google Cloud console](https://docs.cloud.google.com/sql/docs/postgres/iam-permissions#permissions-console)
  * [Required permissions for `gcloud sql` commands](https://docs.cloud.google.com/sql/docs/postgres/iam-permissions#permissions-gcloud)
  * [Required permissions for Cloud SQL Admin API methods](https://docs.cloud.google.com/sql/docs/postgres/iam-permissions#api-methods)
  * [Predefined Cloud SQL IAM roles](https://docs.cloud.google.com/sql/docs/postgres/iam-roles#roles)
  * [Permissions and their roles](https://docs.cloud.google.com/sql/docs/postgres/iam-roles#permissions-roles)
  * [Custom roles](https://docs.cloud.google.com/sql/docs/postgres/iam-roles#custom-roles)



## IAM authentication concepts

When using IAM authentication, permission to access a resource (a Cloud SQL instance) isn't granted _directly_ to the end user. Instead, permissions are grouped into _roles_ , and roles are granted to _principals_. For more information, see the [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

Administrators who have users log in through IAM database authentication can use IAM authentication to centrally manage access control to their instances using IAM policies.

IAM policies involve the following entities:

  * **Principals**. In Cloud SQL, you can use several types of principals: a _user account_ , a _service account_ (for applications), or a _group_. For more information, see [Concepts related to identity](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity).
  * **Roles**. A role is a collection of permissions. You can grant roles to principals to provide them with the privileges required to accomplish specific tasks. For example, with IAM database authentication, a principal requires the `cloudsql.instances.login` permission to log in to an instance, which is included in the **Cloud SQL Instance User** role. To get the permission, you bind the user, service account, or group to the predefined Cloud SQL role or a custom role that includes the permission. For more information about IAM roles, see [Roles](https://docs.cloud.google.com/iam/docs/overview#roles).
  * **Resource**. The resources that principals access are Cloud SQL instances. By default, IAM policy bindings are applied at the project-level, such that principals receive role permissions for all Cloud SQL instances in the project.



## IAM database authentication

Database authentication is the process of verifying the identity of a user who is attempting to access databases. In Cloud SQL, you can use the following types of database authentication for database users:

  * The database's [built-in authentication](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication) uses a username and password to authenticate a database user.
  * IAM database authentication uses IAM to authenticate a user by using an access token. **Note:** If you're using [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), you can use Workforce Identity Federation database authentication to connect to your instances. For more information, see [Workforce Identity Federation authentication](https://docs.cloud.google.com/sql/docs/postgres/workforce-authentication).

## Compare database authentication options

The following table compares different database authentication methods for Cloud SQL.

**Feature** | **Built-in database authentication** | **IAM database authentication (individual)** | **IAM group authentication**  
---|---|---|---  
**Authentication method** | Password | Temporary authentication token | Temporary authentication token  
**Network traffic encryption** | SSL not required | SSL required | SSL required  
**User management** | Manual | Centralized through IAM | Centralized through IAM and Cloud Identity groups  
  
## IAM group authentication

IAM group authentication lets you manage Cloud SQL users at a group level. An example of a group includes a [Cloud Identity group](https://docs.cloud.google.com/identity/docs/groups). This feature simplifies database user management. You can manage the Cloud SQL IAM role or permissions for multiple accounts at once instead of having to update each user or service account individually. You can also grant and revoke the database privileges for a Cloud Identity group. Any new accounts that you add to the Cloud Identity group inherit the privileges of that group.

With IAM group authentication, you can do the following:

    * Add a user to a group and have the user inherit their IAM roles and database privileges automatically.
    * Remove a user from a group to remove their login access and database privileges from Cloud SQL databases.
    * Grant login or database privileges to a group a single time instead of having to grant the same privileges multiple times to different users.
    * Remove login permissions or access to a database object for a group all at once.

Even though IAM roles and permissions are assigned at the group level, users and service accounts use their individual IAM accounts and credentials and not a shared group account to log in. Cloud SQL creates a database account on the instance for that user or service account after their first login.

Individual login and database activity for each user or service account appears in audit logs. For auditing purposes, you get the benefit of viewing which account performed which action in your database.

For more information about working with Cloud Identity groups, see the [Overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview).

When you add a user or service account to a group, the following changes in Cloud SQL occur:

    * If you have already given IAM login permissions to the group, then the user or service account gains the ability to log in to the Cloud SQL instance because the user or service account belongs to the group.
    * The user automatically inherits any [database privileges](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#grant-db-priv-to-group) that have been granted to the group.
**Note:** If you're adding an account that already has access to the instance through individual IAM authentication, first [remove that IAM user or service account from the instance](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#remove-user). Then add the user or service account to the group.

When you remove a user or service account from the group, the following changes in Cloud SQL occur:

    * The user loses any database privileges that were previously inherited by being a member of the group.
    * The user might still be able login if they receive IAM login permissions for the Cloud SQL instance through other group memberships. However, the user won't have database privileges from their former group membership upon logging in.
**Note:** Group membership changes take time to propagate. After a user has been removed from a group, it can take some time to revoke their inherited group database privileges.

### IAM group authentication best practices

    * When you revoke the login permission (`cloudsql.instances.login`) for an IAM group in Cloud Identity, make sure that you also delete the group from the Cloud SQL instance.
    * When you delete a group from a Cloud Identity, make sure that you also delete that group from the Cloud SQL instance.
    * Use groups to configure role-based access control in your database. Always provide the least required privileges to the group.
    * Don't grant IAM group authentication roles to built-in users. For example, if you have a built-in user, `user-a` and create an IAM group authentication user, `user-b@example.com`, then don't grant the `user-b@example.com` role to `user-a`.

### IAM group authentication restrictions

    * When using IAM group authentication, if you have a Cloud SQL instance with read replicas, then you must log in to the primary instance first before logging in to the read replica instance. After your first login to the primary instance, the group user information is replicated to the read replicas. For subsequent logins, you can log in directly to the read replica.
    * You can add a maximum of 200 IAM groups to an instance.
    * You can't add individual IAM user or service accounts that belong to a group on the same instance. In other words, you can't add an account with the type `CLOUD_IAM_USER` or `CLOUD_IAM_SERVICE_ACCOUNT` if an identical account with type `CLOUD_IAM_GROUP_USER` or `CLOUD_IAM_GROUP_SERVICE_ACCOUNT` already exists.
    * If an individual account already exists on an instance with the type `CLOUD_IAM_USER` or `CLOUD_IAM_SERVICE_ACCOUNT`, then the account can't be used for IAM group authentication. These user types don't inherit IAM roles and database privileges from a group. 

To fix this issue and use the account with IAM group authentication, remove the individual IAM user or service account.

For more information, see [An existing IAM user or service account isn't inheriting the database privileges granted to their group](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#user-not-inherit-priv).
    * Changes to Cloud Identity group membership, such as the addition of an account, take about 15 minutes to propagate. This is in addition to the [time required for IAM changes](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Automatic versus manual IAM database authentication

Cloud SQL for PostgreSQL has two options for IAM database authentication: automatic and manual.

### Automatic IAM database authentication

_Automatic IAM database authentication_ lets you hand off requesting and managing access tokens to an intermediary [Cloud SQL connector](https://docs.cloud.google.com/sql/docs/postgres/connect-overview), such as the Cloud SQL Auth Proxy or one of the Cloud SQL Language Connectors. With automatic IAM database authentication, users need to pass only the IAM database username in a connection request from the client. The connector submits the access token information for the password attribute on behalf of the client.

Automatic IAM database authentication requires the use of a Cloud SQL connector and is supported by the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy), the [Go connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#go), the [Java connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#java), and the [Python connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#python).

For the most secure and reliable experience, we recommend you use automatic IAM database authentication. IAM database authentication uses OAuth 2.0 access tokens, which are short-lived and valid for only one hour. Cloud SQL connectors are able to request and refresh these tokens, ensuring that long-lived processes or applications that rely on connection pooling can have stable connections. Automatic IAM database authentication is strongly recommended over manual authentication.

For more information, see [Log in with automatic IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-logins#log-in-with-automatic).

### Manual IAM database authentication

_Manual IAM database authentication_ requires the IAM principal to explicitly pass the access token for the password attribute in the client connection request. Principals must first log in to Google Cloud and explicitly request the access token from IAM.

Using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), you can explicitly request an [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) token with the Cloud SQL Admin API scope that is used to log in to the database. When you log in as a database user with IAM database authentication, you use your email address as the username and the access token as the password. You can use this method with either a direct connection to the database or with a Cloud SQL connector.

**Warning:** OAuth 2.0 access tokens are short lived and are only valid for one hour. Any new connections or logins created after this time fail. For this reason, we recommend that you use automatic IAM database authentication for long-lived processes or applications that rely on connection pooling. 

Logging in with IAM database authentication can only be performed over an SSL connection.

For more information, see [Logging in with manual IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-logins#logging-in-as-a-user).

### Context-aware access and IAM database authentication

If you're using [context-aware access](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto) in your IAM configuration, then you can't use a Cloud SQL connector such as the Cloud SQL Auth Proxy or one of the Cloud SQL Language Connectors with IAM database authentication. Attempts to login either manually or automatically with IAM authentication will fail. Connect directly to the instance instead.

## User and service account administration

To provide users and service accounts access to databases on an instance using IAM database authentication, you need to add them to the instance or add them to a group that has access to the instance. For more information, see [Add a user or service account that uses IAM](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user).

If you use the Google Cloud console to add users or service accounts, Cloud SQL asks you to add the "Cloud SQL User" role to the user. This role is required for users to log in to the instance.

If you add users using `gcloud` or the API, you need to grant login privileges manually. Use the PostgreSQL [GRANT](https://www.postgresql.org/docs/current/static/sql-grant.html) command to [grant database privileges](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#grant-db-privileges). 

## Instance configuration for Cloud SQL IAM database authentication

You can enable IAM database authentication on an instance using the `cloudsql.iam_authentication` flag. Once you enable this flag, the instance enables logins from accounts that are configured for IAM database authentication. This flag is enabled by default if you create the instances using the Google Cloud console.

This flag is required for IAM group authentication and IAM database authentication.

**Note:** If a Cloud SQL instance already has an IAM user (`CLOUD_IAM_USER`) or service account (`CLOUD_IAM_SERVICE_ACCOUNT`) and you want to switch the account to use IAM group authentication (`CLOUD_IAM_GROUP_USER` or `CLOUD_IAM_GROUP_SERVICE_ACCOUNT`), then you must [remove the existing IAM user or service account](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#remove-user) from the instance first.

Setting the flag does not prevent existing, non-IAM users from using their usernames and passwords to log in. However, if you disable this flag on the instance, any user that you previously added using IAM database authentication loses access to the instance. For more information, see [Configuring instances for IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/create-edit-iam-instances).

### Cloud SQL IAM database authentication for different instance scenarios

**Read replicas** | IAM database authentication is not enabled in a read replica automatically, even when it is enabled on the primary instance. After you create a read replica, you need to add IAM database authentication. For more information, see [Configure read replica logins for IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica#configure_iam_replicas).   
---|---  
**Restored instances** | If an instance was previously backed up and later restored to the same or a different instance in the same project, the current user login authorizations apply. If you restore a backup to a new instance in another project, you need to set up the user authorizations for the new instance. For more information, see [Add a user or service account that uses IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user).   
**Point-in-time restored instances** | If you perform a point-in-time restore within the same project, the current user login authorizations apply for the target instance. If you point-in-time restore an instance to a different project, you need to set up the user authorizations for the new instance. For more information, see [Add a user or service account that uses IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user).   
  
## About IAM Conditions

IAM Conditions lets you grant roles based on a variety of attributes. For example, you can allow access only at certain dates and times or grant access only to Cloud SQL resources with certain names.

For more information about IAM Conditions, see the [Overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) page. You can also learn more about [Using IAM Conditions](https://docs.cloud.google.com/sql/docs/postgres/iam-conditions) with Cloud SQL, including examples.

## Work with Cloud Audit Logs

To keep records of data access, including logins, you can use audit logs. [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit#data-access) is turned off, by default. You need to turn on [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access) for login tracking. Using audit logging for this purpose incurs costs for data logging. For more information, see [Audit Logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging#audited_operations), [Configuring Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) and [Pricing for logging data](https://docs.cloud.google.com/logging#pricing).

## Performance on shared-core instances

Shared-core machine types (such as `db-f1-micro` and `db-g1-small`) rely on [CPU bursting](https://docs.cloud.google.com/compute/docs/general-purpose-machines#cpu-bursting) to handle short spikes in activity. IAM database authentication is more computationally intensive than built-in password authentication. Thus, when a shared-core instance is no longer bursting or is experiencing high CPU utilization, connections using IAM database authentication might experience high latency or timeouts.

To ensure optimal connection performance and reliability:

    * **Implement persistent connection pooling** : Configure client-side connection pools (such as HikariCP for Java, SQLAlchemy connection pools for Python, or `database/sql` pools for Go), enable [managed connection pooling](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling), or use the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy).
    * **Increase client connection timeouts** : If your application must establish new connections during periods of high CPU activity, then configure a higher connection timeout (for example, 10 to 15 seconds) in your database driver or client configuration.
    * **Upgrade to dedicated-core instances** : [Edit your instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance) to use a dedicated-core [machine type](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#machine-type-2ndgen). Dedicated-core machines provide unthrottled CPU allocations that ensure faster and more consistent connection times.

## Restrictions

    1. The login for an IAM database authentication user account must be all lowercase. For example, `example-user@example.com`. `Example-User@example.com` is not allowed.
    2. For security, logins using IAM database authentication are only available on an SSL connection. Unencrypted connections are rejected.
    3. There is a per-minute login quota for each instance, which includes both successful and unsuccessful logins. When the quota is exceeded, logins are temporarily unavailable. We recommend that you avoid frequent logins and restrict logins using [authorized networks](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks). The quota for authorization of logins is 12,000 per minute, per instance. 

## What's next

    * Learn how to [configure instances for IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/create-edit-iam-instances).
    * Learn how to [add a user or service account that uses IAM database authentication to your database](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user).
    * Learn how to [log in to a Cloud SQL database with IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-logins).
    * Learn how to [view login information in audit logs](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#viewing-login-audit-logs).
    * Learn about [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
