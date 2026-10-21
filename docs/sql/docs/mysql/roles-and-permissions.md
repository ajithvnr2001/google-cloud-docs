---
url: https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions/
title: Roles and permissions \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:40.757740+00:00
---

# Roles and permissions  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/roles-and-permissions "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/roles-and-permissions "View this page for the SQL Server database engine")

This page provides information about Identity and Access Management (IAM) roles and permissions and how they're used with Cloud SQL instances.

## Introduction

This page focuses on aspects of IAM that are relevant specifically to Cloud SQL. For a detailed discussion of IAM and its features generally, see [Identity and Access Management](https://docs.cloud.google.com/iam). In particular, see the [Managing IAM Policies](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) section. IAM lets you control who has access to the _resources_ in your Google Cloud project. The set of access rules you apply to a resource is called an IAM _policy_. An IAM policy applied to your project defines the actions that users can take on all resources within your project.

_Members_ are the "who" of IAM. Members can be individual users, groups, domains, or even the public as a whole. Members are assigned _roles_ , which grant members the ability to perform actions in Cloud SQL as well as Google Cloud more generally. Each role is a collection of one or more _permissions_. Permissions are the basic units of IAM: each permission lets you perform a certain action. See [IAM roles in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/iam-roles) and [IAM permissions in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/iam-permissions) for complete lists of all the roles and permissions available in Cloud SQL.

When you use an account to connect to a Cloud SQL instance, the account must have the **Cloud SQL > Client** role (`roles/cloudsql.client`), which includes the [permissions](https://docs.cloud.google.com/sql/docs/mysql/iam-permissions) required for connecting.

You can add roles to an account in the Console on the [**IAM & Admin > IAM** ](https://console.developers.google.com/iam-admin/iam) page, and see which permissions belong to which roles on the [**IAM & Admin > Roles**](https://console.developers.google.com/iam-admin/roles) page.

Cloud SQL uses service accounts for authentication between Cloud SQL and other Google Cloud products. Service accounts provide `credentials` in JSON format, which you download from the Console and use for authentication in various scenarios.

For example: connecting from an application running in a [docker container](https://docs.cloud.google.com/sql/docs/mysql/connect-docker#connect-client). 

## Cloud SQL roles and permissions with Cloud SQL Auth Proxy

If you are connecting to a Cloud SQL instance from a Compute Engine instance using [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#create-service-account), you can use the default Compute Engine service account associated with the Compute Engine instance.

As with all accounts connecting to a Cloud SQL instance, the service account must have the **Cloud SQL > Client** role.

## Cloud SQL roles and permissions with serverless options

Google Cloud [serverless options](https://docs.cloud.google.com/serverless) include [App Engine](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine) and [Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run). 

Use a service account to authorize access from these options. The service account authorizes access to all Cloud SQL in a specific project. When you create an application or a Cloud Run functions, this service creates this account for you. You can find the account on the [**IAM & Admin > IAM** ](https://console.developers.google.com/iam-admin/iam) page, with the appropriate suffix: 

Serverless option | Service account suffix  
---|---  
App Engine | @gae-api-prod.google.com.iam.gserviceaccount.com  
Cloud Run functions | @appspot.gserviceaccount.com  
Cloud Run | compute@developer.gserviceaccount.com  
As with all accounts connecting to a Cloud SQL instance, the service account must have the **Cloud SQL > Client** role. 

## Cloud SQL roles and permissions with Cloud Storage

**Note:** To export data, the account that initiates the export must be assigned the **Cloud SQL Editor** (`roles/cloudsql.editor`) predefined role, or a custom role that includes the `cloudsql.instances.export` permission. 

The import and export features in Cloud SQL work together. Exports write to Cloud Storage and imports read from there. For this reason, the service account you use for these operations needs both read and write permissions to Cloud Storage: 

  * To import data to, and export data from, Cloud Storage, the Cloud SQL instance's service account must have the `storage.objectAdmin` IAM role set in the project. You can find the instance's service account name in the Google Cloud console on your instance's **Overview** page.
  * You can use the `[gcloud storage buckets add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)` command to grant this [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the service account for the bucket. 
  * For help with setting IAM roles and permissions, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). 
  * For more information, see [IAM](https://docs.cloud.google.com/storage/docs/access-control/iam) for Cloud Storage. 



## Cloud SQL roles and permissions with IAM group authentication

When you use IAM group authentication, you create groups. You can then use the groups to manage access and database privileges to your Cloud SQL instances.

The following table lists the roles that are required to manage IAM group authentication. 

**Action** | **Roles**  
---|---  
Create, view, and manage groups. | ` roles/resourcemanager.organizationViewer `  
View the IAM group membership change log. | ` roles/logging.viewer `  
Grant, view, and set IAM permissions at the project level. | ` roles/resourcemanager.projectIamAdmin `  
Grant, view, and set IAM permissions at the folder level. | ` roles/resourcemanager.folderIamAdmin `  
  
The administrator can grant [Cloud SQL roles](https://docs.cloud.google.com/sql/docs/mysql/iam-roles) or give individual [Cloud SQL permissions](https://docs.cloud.google.com/sql/docs/mysql/iam-permissions) to each group. The members of each group inherit roles and permissions. 

## Cloud SQL roles and permissions for Knowledge Catalog integration

To provide access to Cloud SQL metadata on Knowledge Catalog, you can grant a user the `roles/cloudsql.schemaViewer` role or add the `cloudsql.schemas.view` permission to a custom role.

For more information, see [Manage Cloud SQL resources with Knowledge Catalog](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration).

## Permission to access private Cloud SQL instances

When another Google Cloud service, such as BigQuery, needs to communicate with your Cloud SQL instance to access data and make queries against this data over a private connection, the service uses an [internal path](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#private-path) instead of the private IP addresses inside of the Virtual Private Cloud (VPC). Traffic can't be controlled or restricted with any VPC-level configurations, firewall rules, route policies, or cutting of the peering.

Instead, Cloud SQL offers a configuration flag on your instance to control whether to turn this internal path on or off for other Google Cloud services accessing your database.

### Control and revoke the permission

When another Google Cloud service, such as BigQuery, tries to access your private Cloud SQL instance, it must provide a legitimate identity with the `[cloudsql.instances.connect](https://docs.cloud.google.com/iam/docs/permissions-reference)` IAM permission.

Typically, there are two ways that a service can achieve this:

  1. Forwarding the user's credentials. A service can forward the user's IAM identity to Cloud SQL to evaluate the permission to access an instance. In this scenario, the user must have sufficient IAM permissions so that Cloud SQL can make a successful connection.
  2. Using a service account. A service, such as BigQuery, can use a pre-configured service account to connect to a Cloud SQL instance. In this case, the service account must have sufficient IAM permissions.

For example, for the federated connection between BigQuery and Cloud SQL, a service account named `service-{PROJECT_NUMBER}@gcp-sa-bigqueryconnection.iam.gserviceaccount.com` is created when the BigQuery connection API is activated. This service account has two Cloud SQL permissions: `[cloudsql.instances.connect](https://docs.cloud.google.com/iam/docs/permissions-reference)` and `[cloudsql.instances.get](https://docs.cloud.google.com/iam/docs/permissions-reference)`. BigQuery uses these permissions to access a private Cloud SQL instance through an [internal path](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#private-path).




To control the permission for who can use this internal path, you can grant and revoke the IAM permissions to and from the user's IAM identity that the Google Cloud service, such as BigQuery, uses to connect to your Cloud SQL instance. For more information about granting and revoking permissions within BigQuery, see [Setting up access to Cloud SQL](https://docs.cloud.google.com/bigquery/docs/cloud-sql-federated-queries#access-sql).

## Cloud SQL roles and permissions with other scenarios

Cloud SQL interacts with other Google Cloud products and tools. These interactions also require specific roles and permissions which can vary between scenarios. Cloud SQL documentation provides detailed information about these requirements for each case below: 

  * [Connecting to Cloud SQL from external applications](https://docs.cloud.google.com/sql/docs/mysql/connect-overview).

  * [ Using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek).
  * [ IAM Roles for Administering VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control).
  * To connect to a Cloud SQL instance from an application running in Google Kubernetes Engine, you will need to create a [ Secret](https://docs.cloud.google.com/sql/docs/mysql/connect-kubernetes-engine#secrets) for a [ service account's](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#create-service-account) JSON key file.




## Use IAM with projects

The following sections show how to complete basic IAM tasks on projects.

To complete the following tasks, you must have the `resourcemanager.projects.getIamPolicy` and `resourcemanager.projects.setIamPolicy` IAM permissions.

### Add a member to a project-level policy

For a list of roles associated with Cloud SQL, see [IAM Roles](https://docs.cloud.google.com/sql/docs/mysql/iam-roles).

### Console

  1. Go to the [IAM & Admin](https://console.cloud.google.com/iam-admin) page in the Google Cloud console
  2. In the project drop-down menu on the top bar, select the project to which you want to add a member.
  3. Click **Add**. The **Add members, roles to project** dialog appears.
  4. In the **New members** field, specify the name of the entity to which you are granting access.
  5. In the **Select a role** drop down, grant the appropriate role to the member. Roles that affect Cloud SQL resources are found in the **Project** and **Cloud SQL** submenus.
  6. Click **Save**.



### gcloud

To add a project-level IAM policy, use [`gcloud beta projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/projects/add-iam-policy-binding).

### View the IAM policy for a project

### Console

  1. Go to the [IAM & Admin](https://console.cloud.google.com/iam-admin) page in the Google Cloud console
  2. In the project drop-down menu on the top bar, select the project whose policy you want to view.
  3. There are two ways to view permissions for the project: 
     * View by **Members** : View the **Role** column associated with individual members to see which roles each member has.
     * View by **Roles** : Use the drop-down associated with individual roles to see which members have the role.



### gcloud

To view the IAM policy of a project, use [`gcloud beta projects get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/projects/get-iam-policy).

### Remove a member from a project-level policy

### Console

  1. Go to the [IAM & Admin](https://console.cloud.google.com/iam-admin) page in the Google Cloud console
  2. In the project drop-down menu on the top bar, select the project from which you want to remove a member.
  3. Make sure you are viewing permissions by **Members** , and select the members you want to remove.
  4. Click **Remove**.
  5. In the overlay window that appears, click **Confirm**.



### gcloud

To remove a project-level IAM policy, use [`gcloud beta projects remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/projects/remove-iam-policy-binding).

**Important:** It typically takes about a minute for revoking access to take effect. In some cases it may take longer. If you remove a user's access, this change is immediately reflected in the metadata; however, the user may still have access to the object for a short period of time.

## Best practices

IAM, like any other administrative settings, requires active management to be effective. Before you make a resource accessible to other users, be sure you know what roles you want each of those people to play. Over time, changes in project management, usage patterns, and organizational ownership may require you to modify IAM settings on projects, especially if you manage Cloud SQL in a large organization or for a large group of users. As you evaluate and plan your access control settings, keep the following best practices in mind:

  * **Use the principle of least privilege when granting access.** The [_principle of least privilege_](https://en.wikipedia.org/wiki/Principle_of_least_privilege) is a security guideline for granting access to your resources. When you grant access based on the principle of least privilege, you give a user only the access they need to accomplish their assigned task.

  * **Avoid granting roles with`setIamPolicy` permission to people you do not know.** Granting `setIamPolicy` permission allows a user to change permissions and take control of data. You should use roles with `setIamPolicy` permission only when you want to delegate administrative control over objects and buckets.

  * **Be sure you delegate administrative control of your resources.** You should be sure that your resources can still be managed by other team members should an individual with administrative access leave the group. Two common ways to achieve this are the following:

    * Assign the **Cloud SQL Admin** role for your project to a group instead of an individual.
    * Assign the **Cloud SQL Admin** role for your project to at least two individuals.



## What's next

  * Learn more about [Controlling access](https://docs.cloud.google.com/sql/docs/mysql/instance-access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
