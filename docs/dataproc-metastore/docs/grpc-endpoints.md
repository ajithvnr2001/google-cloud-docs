---
url: https://docs.cloud.google.com/dataproc-metastore/docs/grpc-endpoints/
title: Access gRPC endpoints for Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:39:56.762949+00:00
---

# Access gRPC endpoints for Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/grpc-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Access gRPC endpoints for Dataproc Metastore Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to grant a Google Cloud user account or a service account access to a Dataproc Metastore service that uses the [gRPC endpoint protocol](https://docs.cloud.google.com/dataproc-metastore/docs/about-endpoint-protocols#grpc).

## About granting gRPC metadata roles

When granting an account access to your metadata, consider the following concepts:

  * **The level of access to provide**. The level of access you grant controls how much metadata that an account can access. For example, you can choose to provide access to metadata stored in a specific database, a specific table, or you can provide access to your entire project.
  * **The principal that requires access**. You use IAM principals (identities) to run your jobs. For example, you can run Managed Service for Apache Spark cluster jobs with user accounts or service accounts (typically the [Dataproc VM service account](https://docs.cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity)).

For more information about the accounts you can use with Dataproc Metastore, see [Dataproc service accounts](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#dataproc_service_accounts_2).




Depending on the scope of control required, grant your principal one of the following predefined IAM roles:

  * To grant full access to the metadata resources. Metadata Owner role (`roles/metastore.metadataOwner`)
  * To grant read-write access to metadata: Metadata Editor role (`roles/metastore.metadataEditor`)
  * To grant read access to the metadata: Metadata Viewer role (`roles/metastore.metadataViewer`)



## Before you begin

  * [Enable Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service) in your project.
  * [Create a metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service) that uses the gRPC protocol.
  * Understand [networking requirements](https://docs.cloud.google.com/dataproc-metastore/docs/access-service) specific to your project.

    * **gRPC and Virtual Private Cloud (VPC) requirements**. If you're using gRPC, you don't have to configure a Shared VPC or set any extra network configurations. By default, gRPC endpoints can be reached from any VPC.

However, there's one exception. If your project is using a VPC-SC service perimeter, then gRPC endpoints can only be reached from a VPC belonging to projects in the perimeter. For more information, see [VPC Service Controls with Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/vpc-sc).




### Required Roles

To get the permissions that you need to grant a principal access to Dataproc Metastore metadata, ask your administrator to grant you the following IAM roles on your project, while following the principle of least privilege: 

  * [To grant full control of Dataproc Metastore resources ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)
  * [To grant full control of Dataproc Metastore resources, including updating IAM permissions ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to grant a principal access to Dataproc Metastore metadata. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to grant a principal access to Dataproc Metastore metadata:

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.getIamPolicy`
  * `resourcemanager.projects.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about specific Dataproc Metastore roles and permissions, see [Dataproc Metastore IAM overview](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control). 

## Grant a principal account access to metadata

You can grant a principal account access to metadata at the project level, service level, database level, or table level.

### Grant access at the project level

To grant access to all Dataproc Metastore metadata at the project level, you must grant a metadata role to your principal account.

### gcloud CLI

To grant metadata roles to all Dataproc Metastore services in a specified project, run the following [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=PRINCIPAL \
        --role=METASTORE_ROLE

Replace the following:

  * `PROJECT_ID`: The Google Cloud project ID that you want to grant metadata access to.
  * `PRINCIPAL`: The type and email ID (email address) of the principal. 
    * For user accounts: user:EMAIL_ID
    * For service accounts: serviceAccount:EMAIL_ID
    * For Google Groups: group:EMAIL_ID
    * For other principal types: [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers)
  * `METASTORE_ROLE\`: One of the following roles, depending on the scope of access that you want to grant the principal:`roles/metastore.metadataViewer`,`roles/metastore.metadataEditor`, or`roles/metastore.metadataOwner`.



### Grant access at the service level

To grant access to all Dataproc Metastore metadata at the service level, you must grant a metadata role to your principal account.

### gcloud CLI

To grant metadata roles at the granularity of a single Dataproc Metastore metastore service, run the following [`gcloud metastore services add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/add-iam-policy-binding) command:
    
    
    gcloud metastore services add-iam-policy-binding SERVICE_ID \
      --location=LOCATION \
      --member=PRINCIPAL \
      --role=METASTORE_ROLE

Replace the following:

  * `SERVICE_ID`: The ID or fully qualified identifier for your Dataproc Metastore service.
  * `LOCATION`: The region of the Dataproc Metastore that you're granting access to.
  * `PRINCIPAL`: The type and email ID (email address) of the principal account: 
    * For user accounts: user:EMAIL_ID
    * For service accounts: serviceAccount:EMAIL_ID
    * For Google Groups: group:EMAIL_ID
    * For other principal types: [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers)
  * `METASTORE_ROLE`: One of the following roles, depending on the scope of access that you want to grant the principal: `roles/metastore.metadataViewer`, `roles/metastore.metadataEditor`, or `roles/metastore.metadataOwner`.



### Grant access at the database level

To grant access to all Dataproc Metastore metadata in a specific database, you must add a metadata role to your principal account.

### gcloud CLI

To grant metadata roles at the granularity of a specific database, run the following [`gcloud metastore services databases add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/databases/add-iam-policy-binding) command:
    
    
    gcloud metastore services databases add-iam-policy-binding DATABASE_ID \
      --project=PROJECT \
      --location=LOCATION \
      --service=SERVICE_ID \
      --member=PRINCIPAL \
      --role=METASTORE_ROLE

Replace the following:

  * `DATABASE_ID`: The ID of the database that you're granting metadata access to. You get this ID from your database schema.
  * `PROJECT`: The Google Cloud project ID that contains the Dataproc Metastore service that you're granting metadata access to.
  * `LOCATION`: The region of the Dataproc Metastore service that you're granting metadata access to.
  * `SERVICE_ID`: The ID or fully qualified identifier for your Dataproc Metastore service.
  * `PRINCIPAL`: The type and email ID (email address) of the principal account: 
    * For user accounts: user:EMAIL_ID
    * For service accounts: serviceAccount:EMAIL_ID
    * For Google Groups: group:EMAIL_ID
    * For other principal types: [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers)
  * `METASTORE_ROLE`: One of the following roles, depending on the scope of access that you want to grant the principal: `roles/metastore.metadataViewer`, `roles/metastore.metadataEditor`, or `roles/metastore.metadataOwner`.



### Grant access at the table level

To grant access to all Dataproc Metastore metadata in a specific table, you must grant a metadata role to your principal account.

### gcloud CLI

To grant metadata roles at the granularity of a table, run the following [`gcloud metastore services databases tables add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/databases/tables/add-iam-policy-binding) command:
    
    
    gcloud metastore services databases tables add-iam-policy-binding TABLE_ID \
      --database=DATABASE_ID \
      --project=PROJECT \
      --location=LOCATION \
      --service=SERVICE_ID \
      --member=PRINCIPAL \
      --role=METASTORE_ROLE

Replace the following:

  * `TABLE_ID`: The ID of the table that you're granting access to. You get this ID from your database schema.
  * `DATABASE_ID`: The ID of the database that contains the table that you're granting metadata access to. You get this ID from your database schema.
  * `PROJECT`: The Google Cloud project ID that contains the Dataproc Metastore service that you're granting metadata access to.
  * `LOCATION`: The region of the Dataproc Metastore service that you're granting metadata access to.
  * `SERVICE_ID`: The ID or fully qualified identifier for your Dataproc Metastore service.
  * `PRINCIPAL`: The type and email ID (email address) of the principal account: 
    * For user accounts: user:EMAIL_ID
    * For service accounts: serviceAccount:EMAIL_ID
    * For Google Groups: group:EMAIL_ID
  * `METASTORE_ROLE`: One of the following roles, depending on the scope of access you want to grant the principal: `roles/metastore.metadataViewer`, `roles/metastore.metadataEditor`, or `roles/metastore.metadataOwner`.



## After you grant access to your metadata

After you grant the required roles to your service accounts, you can connect your Dataproc Metastore to a [Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc). Your cluster then uses the Dataproc Metastore service as its Hive Metastore.

## What's next

  * [Attach a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc)
  * [Update and delete Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/manage-service)
  * [Import metadata into Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
