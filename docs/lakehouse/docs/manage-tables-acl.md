---
url: https://docs.cloud.google.com/lakehouse/docs/manage-tables-acl/
title: Manage Apache Iceberg REST catalog endpoint ACLs \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:38.371182+00:00
---

# Manage Apache Iceberg REST catalog endpoint ACLs  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/manage-tables-acl/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Manage Apache Iceberg REST catalog endpoint ACLs Stay organized with collections  Save and categorize content based on your preferences. 

_Borderless Lakehouse_ supports catalog-level, namespace-level, and table-level access control for Apache Iceberg tables in Cloud Storage that use the _Lakehouse runtime catalog_.

The _Lakehouse runtime catalog_ manages the metadata, while Identity and Access Management (IAM) policies define the permissions. You can use the Google Cloud console or the `gcloud` CLI to get and set these IAM policies.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. Install and initialize the Google Cloud SDK.
  4. Verify that you have an existing Apache Iceberg REST catalog endpoint and namespace.
  5. Verify that you have an existing Apache Iceberg table managed by Lakehouse within the specified catalog and namespace.



### Required roles

To get the permissions that you need to manage Access Control Lists (ACLs) for Iceberg catalogs, namespaces, and tables, ask your administrator to grant you the following IAM roles: 

  * All: [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) on for the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## How it works

IAM policies define which principals have specific roles and permissions for a resource. You can manage access to your resources by getting and setting these policies.

### Scope of IAM roles

You can grant IAM roles at different levels of the resource hierarchy:

  * **Project level** : Grants access to all Lakehouse resources in the project.
  * **Catalog level** : Grants access to resources belonging to the specified catalog.
  * **Namespace level** : Grants access to resources belonging to the specified namespace.
  * **Table level** : Grants access to only the specified table.



### Relevant IAM roles

The following list shows some of the common IAM roles that you can apply to Lakehouse resources. For a complete list of available roles and their associated permissions, see [Lakehouse IAM roles](https://docs.cloud.google.com/lakehouse/docs/iam-roles).

  * `roles/biglake.admin`: provides full access to all Lakehouse resources.
  * `roles/biglake.editor`: provides read and write access to all Lakehouse resources.
  * `roles/biglake.viewer`: provides read-only access to all Lakehouse resources.
  * `roles/biglake.metadataViewer`: provides read-only metadata access to all Lakehouse resources.



### Best practices

  * **Least Privilege** : grant only the necessary permissions to users and service accounts.
  * **Use Etags** : always include the `etag` from a recent `get-iam-policy` call in your policy file when using `set-iam-policy` to avoid unintended overwrites.
  * **Audit Logging** : ensure that Cloud Audit Logs are enabled to track changes to IAM policies.
  * **Version Control** : store your policy files in a version control system.



## Apply ACL roles to catalogs

The following section shows you how to apply ACLs to catalogs.

###  gcloud 

### Get the IAM policy

To view the current IAM policy on a Lakehouse Iceberg catalog, use the [`gcloud alpha biglake iceberg catalogs get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/iceberg/catalogs/get-iam-policy) command.

  1. To get the IAM policy, run the following command:
         
         gcloud alpha biglake iceberg catalogs get-iam-policy CATALOG_NAME \
             --project=PROJECT_ID
         

Replace the following:

     * `CATALOG_NAME`: the name of the Apache Iceberg REST catalog endpoint.
     * `PROJECT_ID`: your Google Cloud project ID.
  2. The command outputs the IAM policy in YAML format, which shows the current role bindings and members.




### Set the IAM policy

To update the IAM policy on a Lakehouse Iceberg catalog, use the [`gcloud alpha biglake iceberg catalogs set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/iceberg/catalogs/set-iam-policy) command. This command uses a local JSON or YAML file that contains the policy you want to apply.

  1. Create a local policy file in JSON or YAML format. The policy file must contain the bindings and an `etag`. The `etag` value provides optimistic concurrency control to prevent overwriting changes. To get the current `etag`, run the `get-iam-policy` command first.

The following example shows a policy file named `policy.json`:
         
         {
           "bindings": [
             {
               "role": "roles/biglake.viewer",
               "members": [
                 "user:test-user@example.com"
               ]
             },
             {
               "role": "roles/biglake.editor",
               "members": [
                 "user:someone@example.com"
               ]
             }
           ],
           "etag": "BwYXa9UuR8w=",
           "version": 3
         }
         

  2. To set the IAM policy, run the following command:
         
         gcloud alpha biglake iceberg catalogs set-iam-policy CATALOG_NAME POLICY_FILE \
             --project=PROJECT_ID
         

Replace the following:

     * `CATALOG_NAME`: the name of the Apache Iceberg REST catalog endpoint.
     * `POLICY_FILE`: the path to your local policy file.
     * `PROJECT_ID`: your Google Cloud project ID.



## Apply ACL roles to namespaces

The following section shows you how to apply ACLs to namespaces.

The Google Cloud console does not display or manage inherited IAM policies.

###  Console 

  1. In the Google Cloud console, open the **Lakehouse** page.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Select an existing catalog or create one if you don't have one.

  3. In the **Namespace details** table, select a namespace and expand the menu options (more_vert).

  4. Click **Manage permissions**.

The **Share permissions** dialog appears.

  5. Click **Add principal**.

  6. For the **New Principals** field, enter the principal account that you want to assign roles to.

  7. For **Select a role** , choose a role to assign to the principal account.

  8. Click **Save**.

  9. Click **Close**.




###  gcloud 

### Get the IAM policy

To view the current IAM policy on a Lakehouse Iceberg namespace, use the [`gcloud alpha biglake iceberg namespaces get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/iceberg/namespaces/get-iam-policy) command.

  1. To get the IAM policy, run the following command:
         
         gcloud alpha biglake iceberg namespaces get-iam-policy NAMESPACE_NAME \
             --catalog=CATALOG_NAME \
             --project=PROJECT_ID
         

Replace the following:

     * `NAMESPACE_NAME`: the name of the target namespace within the catalog.
     * `CATALOG_NAME`: the name of the Apache Iceberg REST catalog endpoint.
     * `PROJECT_ID`: your Google Cloud project ID.
  2. The command outputs the IAM policy in YAML format, which shows the current role bindings and members.




### Set the IAM policy

To update the IAM policy on a Lakehouse Iceberg namespace, use the `gcloud alpha biglake iceberg namespaces set-iam-policy` command. This command uses a local JSON or YAML file that contains the policy you want to apply.

  1. Create a local policy file in JSON or YAML format. The policy file must contain the bindings and an `etag`. The `etag` value provides optimistic concurrency control to prevent overwriting changes. To get the current `etag`, run the `get-iam-policy` command first.

The following example shows a policy file named `policy.json`:
         
         {
           "bindings": [
             {
               "role": "roles/biglake.viewer",
               "members": [
                 "user:test-user@example.com"
               ]
             },
             {
               "role": "roles/biglake.editor",
               "members": [
                 "user:someone@example.com"
               ]
             }
           ],
           "etag": "BwYXa9UuR8w=",
           "version": 3
         }
         

  2. To set the IAM policy, run the following command:
         
         gcloud alpha biglake iceberg namespaces set-iam-policy NAMESPACE_NAME POLICY_FILE \
             --catalog=CATALOG_NAME \
             --project=PROJECT_ID
         

Replace the following:

     * `NAMESPACE_NAME`: the name of the target namespace within the catalog.
     * `POLICY_FILE`: the path to your local policy file.
     * `CATALOG_NAME`: the name of the Apache Iceberg REST catalog endpoint.
     * `PROJECT_ID`: your Google Cloud project ID.



## Apply ACL roles to tables

The following section shows you how to apply ACLs to tables.

The Google Cloud console does not display or manage inherited IAM policies.

###  Console 

  1. In the Google Cloud console, open the **Lakehouse** page.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Select an existing catalog or create one if you don't have one.

  3. In the **Namespace details** table, click the name of the namespace that contains your table.

  4. On the **Table details** page, select a table and expand the menu options (more_vert).

  5. Click **Manage permissions**.

The **Share permissions** dialog appears.

  6. Click **Add principal**.

  7. For the **New Principals** field, enter the principal account that you want to assign roles to.

  8. For **Select a role** , choose a role to assign to the principal account.

  9. Click **Save**.

  10. Click **Close**.




###  gcloud 

### Get the IAM policy

To view the current IAM policy on a Lakehouse Iceberg table, use the [`gcloud biglake iceberg tables get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/tables/get-iam-policy) command.

  1. To get the IAM policy, run the following command:
         
         gcloud biglake iceberg tables get-iam-policy TABLE_NAME \
             --catalog=CATALOG_NAME \
             --namespace=NAMESPACE_NAME \
             --project=PROJECT_ID
         

Replace the following:

     * `TABLE_NAME`: the name of the target Apache Iceberg table.
     * `CATALOG_NAME`: the name of the Apache Iceberg REST catalog endpoint.
     * `NAMESPACE_NAME`: the name of the namespace within the catalog.
     * `PROJECT_ID`: your Google Cloud project ID.
  2. The command outputs the IAM policy in YAML format, which shows the current role bindings and members.




### Set the IAM policy

To update the IAM policy on an Apache Iceberg table managed by Lakehouse, use the `gcloud biglake iceberg tables set-iam-policy` command. This command uses a local JSON or YAML file that contains the policy you want to apply.

  1. Create a local policy file in JSON or YAML format. The policy file must contain the bindings and an `etag`. The `etag` value provides optimistic concurrency control to prevent overwriting changes. To get the current `etag`, run the `get-iam-policy` command first.

The following example shows a policy file named `policy.json`:
         
         {
           "bindings": [
             {
               "role": "roles/biglake.viewer",
               "members": [
                 "user:test-user@example.com"
               ]
             },
             {
               "role": "roles/biglake.editor",
               "members": [
                 "user:someone@example.com"
               ]
             }
           ],
           "etag": "BwYXa9UuR8w=",
           "version": 3
         }
         

  2. To set the IAM policy, run the following command:
         
         gcloud biglake iceberg tables set-iam-policy TABLE_NAME POLICY_FILE \
             --catalog=CATALOG_NAME \
             --namespace=NAMESPACE_NAME \
             --project=PROJECT_ID
         

Replace the following:

     * `TABLE_NAME`: the name of the target Apache Iceberg table.
     * `POLICY_FILE`: the path to your local policy file.
     * `CATALOG_NAME`: the name of the Apache Iceberg REST catalog endpoint.
     * `NAMESPACE_NAME`: the name of the namespace within the catalog.
     * `PROJECT_ID`: your Google Cloud project ID.



## What's next

  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs/overview).
  * See the full list of [Lakehouse IAM roles and permissions](https://docs.cloud.google.com/lakehouse/docs/iam-roles).
  * Learn about [Lakehouse concepts](https://docs.cloud.google.com/lakehouse/docs/key-concepts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
