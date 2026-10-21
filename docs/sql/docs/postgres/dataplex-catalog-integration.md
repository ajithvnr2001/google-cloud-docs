---
url: https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration/
title: Manage your Cloud SQL resources using Knowledge Catalog \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:29.741415+00:00
---

# Manage your Cloud SQL resources using Knowledge Catalog  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Manage your Cloud SQL resources using Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/dataplex-catalog-integration "View this page for the SQL Server database engine")

This page explains how you can search for and manage your Cloud SQL resources by using Knowledge Catalog.

Knowledge Catalog is a platform for storing, managing, and accessing your metadata. Knowledge Catalog retrieves the following metadata from Cloud SQL instances, databases, tables, columns, and views automatically:

  * Name
  * Location (region)
  * Creation date and last modification date
  * Schema (for tables and views)
  * Description
  * Primary key and foreign key constraints



Knowledge Catalog retrieves metadata only from Cloud SQL primary instances and not from read replicas or external server replicas.

You can use Knowledge Catalog to discover and understand your Cloud SQL metadata. Use Knowledge Catalog to aid with the following activities:

  * Data discovery
  * Classification
  * Analysis, including dependencies and suitability for a use case
  * Change management
  * Data movement (pipelines)
  * Schema evolution



With Knowledge Catalog, you curate metadata by attaching aspects to Cloud SQL metadata entries. Each aspect can have multiple metadata fields and can be based on a predefined or custom aspect type.

For example, you might attach the following aspect to a column that contains a Social Security number, which is personally identifiable information (PII):
    
    
      pii:true
      pii_type:SSN
    

For more information about Knowledge Catalog, see [About metadata management in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview).

**Note:** Knowledge Catalog refers to the resources in Cloud SQL and in other Google Cloud services as _assets_. In this page, we refer to Cloud SQL resources—instances, databases, tables, and views—as Cloud SQL assets. We also use the term _assets_ to refer to both the resources and Knowledge Catalog metadata for the resources.

## Knowledge Catalog integration data freshness

The expected freshness of your instance metadata in Knowledge Catalog depends on the creation date of the instance, its database version, and its network architecture.

### Near real-time

Integration with Knowledge Catalog is enabled by default when the instance is created if the instance meets **all** of the following criteria:

  1. **Creation time:** On or after April 18, 2026

**Note:** A small subset of instances created between March 19, 2026 and April 18, 2026 also belong in this category. To confirm whether an instance created during this period belongs in this category, see Verify Knowledge Catalog integration on your Cloud SQL instance. 
  2. **Version:** Cloud SQL for PostgreSQL version 14.0 or later
  3. **Network architecture:** [New network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture#overview)



For existing instances created before April 18, 2026 that meet the version and new network architecture criteria, enabling Knowledge Catalog integration using Enable the integration of Knowledge Catalog on an existing Cloud SQL instance enables integration in near real-time. If such an instance already has Knowledge Catalog integration enabled in once a day, you can deactivate the integration and then re-enable it to move from once a day to near real-time.

If your instance doesn't meet the criteria for near real-time integration, see Once a day.

Instances that are integrated in near real-time contain a timestamp table to track creation and update times for your assets. The timestamp table is in the `cloudsqladmin` database. When your instance has a DDL or schema change, the integration queries the timestamp table to identify recently changed assets, and then loads the latest schema updates to Knowledge Catalog in near real-time. In rare instances, for example when there is network instability, Knowledge Catalog might miss an update. While this is rare, any changes that have been missed become eventually consistent, usually within 24 hours. For more information about scenarios that can cause missed changes, see Limitations on this page.

When you view queries that have been run in an instance, you will see queries that support the Knowledge Catalog integration. You can identify these queries by the `--Dataplex` comment that they include. To view queries for an instance, see [View active queries](https://docs.cloud.google.com/sql/docs/postgres/monitor-active-queries#view-active-queries).

You can deactivate the integration and re-enable it later using the instructions in Update the instance.

### Once a day

Integration with Knowledge Catalog can be enabled for instances that meet **any** of the following criteria:

  1. **Creation time:** Before April 18, 2026
  2. **Version:** Cloud SQL for PostgreSQL version earlier than 14.0
  3. **Network architecture:** [Old network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture#overview)



After you enable integration with Knowledge Catalog, metadata for instances that meet any of these criteria is usually refreshed in Knowledge Catalog around once a day.

If your instance was created after April 18, 2026, then integration with Knowledge Catalog is enabled by default. For instances created prior to April 18, 2026, you can Enable the integration of Knowledge Catalog on an existing Cloud SQL instance  .

If an existing instance created before April 18, 2026 meets the version and new network architecture criteria in Near real-time, enabling Knowledge Catalog integration (or deactivating the integration and re-enabling it if already integrated in once a day) configures the instance for near real-time updates instead.

You can deactivate the integration and re-enable it later using the instructions in Update the instance.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Dataplex API for the project. 

[Enable the Dataplex API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

  7. Check permissions.

You need certain Identity and Access Management (IAM) roles and permissions to search for and attach entries to Cloud SQL assets. For details, see Required IAM roles and permissions for Knowledge Catalog. 




### Required IAM roles and permissions for Knowledge Catalog

Cloud SQL uses the `cloudsql.schemas.view` permission to provide access to the metadata on Knowledge Catalog.

To provide this permission, create a custom role that includes this permission, or use one of predefined roles that has this permission.

For more information, see [Predefined Cloud SQL IAM roles](https://docs.cloud.google.com/sql/docs/postgres/iam-roles).

**Caution:** The `cloudsql.schemas.view` permission must be granted at the project level. Users with this permission can view the metadata for all Cloud SQL instances in the project.

## Create an instance with Knowledge Catalog integration enabled

New instances are integrated with Knowledge Catalog by default. To create a new instance with Knowledge Catalog integration enabled, you just have to create a new instance. To create an instance with Knowledge Catalog integrated in near real-time, your new instance must meet **all** of the following criteria:

  1. **Creation time:** On or after April 18, 2026

**Note:** A small subset of instances created between March 19, 2026 and April 18, 2026 also belong in this category. To confirm whether an instance created during this period belongs in this category, see Verify Knowledge Catalog integration on your Cloud SQL instance. 
  2. **Version:** Cloud SQL for PostgreSQL version 14.0 or later
  3. **Network architecture:** [New network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture#overview)



If you want to enable near real-time Knowledge Catalog for a new instance with an earlier database version or the old network architecture, then you can clone the instance or restore from a backup to a new instance. 

### gcloud

#### Create the instance

To create a Cloud SQL instance, use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command.
    
    
    gcloud sql instances create INSTANCE_NAME \
      --database-version=DATABASE_VERSION \
      --tier=MACHINE_TYPE \
      --region=REGION_NAME

Make the following replacements:

  * INSTANCE_NAME: the name of the instance
  * DATABASE_VERSION: the database version for the instance (for example, `POSTGRES_14` ). For a complete list of available strings, see [SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/SqlDatabaseVersion)
  * MACHINE_TYPE: the machine type for the instance
  * REGION_NAME: the region name for the instance



This example is Linux-based.

### REST v1

#### Create the instance

Use this example to create an instance with the integration enabled. For a complete list of parameters that are available for this call, see the [instances.insert](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/insert) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance
  * REGION_NAME: the region name for the instance
  * DATABASE_VERSION: enum string of the database version (for example, `POSTGRES_13`). For a complete list of available strings, see [SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/SqlDatabaseVersion).
  * PASSWORD: the password for the `root` user
  * MACHINE_TYPE: enum string of the machine (tier) type, as: `db-custom-[CPUS]-[MEMORY_MBS]`
  * EDITION_TYPE: your Cloud SQL edition



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_NAME",
      "region": "REGION_NAME",
      "databaseVersion": "DATABASE_VERSION",
      "rootPassword": "PASSWORD",
      "settings": {
        "tier": "MACHINE_TYPE",
        "edition": "EDITION_TYPE",
        "enableDataplexIntegration": true
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-09-25T22:19:33.735Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

#### Create the instance

Use this example to create an instance with the integration enabled. For a complete list of parameters that are available for this call, see the [instances.insert](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/insert) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance
  * REGION_NAME: the region name for the instance
  * DATABASE_VERSION: enum string of the database version (for example, `POSTGRES_13`). For a complete list of available strings, see [SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/SqlDatabaseVersion).
  * PASSWORD: the password for the `root` user
  * MACHINE_TYPE: enum string of the machine (tier) type, as: `db-custom-[CPUS]-[MEMORY_MBS]`
  * EDITION_TYPE: your Cloud SQL edition



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_NAME",
      "region": "REGION_NAME",
      "databaseVersion": "DATABASE_VERSION",
      "rootPassword": "PASSWORD",
      "settings": {
        "tier": "MACHINE_TYPE",
        "edition": "EDITION_TYPE",
        "enableDataplexIntegration": true
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-09-25T22:19:33.735Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Enable the integration of Knowledge Catalog on an existing Cloud SQL instance

You can follow the update instructions in this section to enable Knowledge Catalog integration on an existing instance created before April 18, 2026. 

When you enable Knowledge Catalog integration on an existing instance: 

  * For instances that meet **any** of the following criteria, enabling Knowledge Catalog integration enables **once a day** updates:

    * **Version:** Cloud SQL for PostgreSQL version earlier than 14.0
    * **Network architecture:** [Old network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture#overview)
  * For instances that meet **all** of the following criteria, enabling Knowledge Catalog integration enables **near real-time** updates:

    * **Version:** Cloud SQL for PostgreSQL version 14.0 or later
    * **Network architecture:** [New network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture#overview)
**Important:** As a known issue, when you enable Knowledge Catalog integration on a Cloud SQL instance created before April 18, 2026, the integration is defaulting to **once a day** instead of **near real-time**.  
  
**Workaround:** To update your instance to use the near real-time integration, do the following:  
1\. Enable the integration.  
2\. After the update finishes, explicitly deactivate the integration.  
3\. Enable the integration a second time. 

After enabling integration in near real-time, new DDL and schema changes appear within 10 minutes while existing resources on the instance are populated within 24 hours.




To enable or re-enable the integration of Knowledge Catalog on an existing Cloud SQL instance, use one of the following procedures.

### gcloud

#### Update the instance

To enable the integration for an existing instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command.
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --enable-dataplex-integration

If you need to enable and update all the Cloud SQL instances in your project, then you can run a script similar to the following:
    
    
    gcloud sql instances list --format="(NAME)" \
    | tail -n +2 | xargs -t -I %
    gcloud sql instances patch % --enable-dataplex-integration

This example is Linux-based.

### REST v1

#### Update the instance

Use this example to update an existing instance. For a complete list of parameters that are available for this call, see the [instances.patch](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/patch) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "settings":
      {
        "enableDataplexIntegration": true
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

#### Update the instance

Use this example to update an existing instance. For a complete list of parameters that are available for this call, see the [instances.patch](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/patch) page.

Use this example to update an existing instance. For a complete list of parameters that are available for this call, see the instances.patch page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "settings":
      {
        "enableDataplexIntegration": true
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Verify Knowledge Catalog integration on your Cloud SQL instance

To verify that the Knowledge Catalog integration is enabled on your instance, use one of the following procedures.

### gcloud

To verify that the Knowledge Catalog integration is enabled on an existing instance, use the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command.
    
    
    gcloud sql instances describe INSTANCE_NAME

Replace INSTANCE_NAME with the name of the instance. In the output, look for the configuration setting `enableDataplexIntegration` set to `true`.

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
    "settings":
      {
      "enableDataplexIntegration": true
      }
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
    "settings":
      {
      "enableDataplexIntegration": true
      }
    }
    

## Deactivate the integration of Knowledge Catalog on your Cloud SQL instance

To deactivate the integration of Knowledge Catalog on your Cloud SQL instance, use one of the following procedures. Disabling Knowledge Catalog integration on an instance that is integrated in near real-time takes up to 10 minutes. 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In the **Customize your instance** section, expand the **Show configuration options** menu.
  5. In the **Flags and parameters** section, clear the **Enable Knowledge Catalog integration** checkbox.

  6. Click **Save**.



### gcloud

To deactivate the integration for an existing instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command.
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --no-enable-dataplex-integration

If you need to deactivate the integration and update all the Cloud SQL instances in your project, then you can run a script similar to the following:
    
    
    gcloud sql instances list --format="(NAME)" \
    | tail -n +2 | xargs -t -I %
    gcloud sql instances patch % --no-enable-dataplex-integration

This example is Linux-based.

### REST v1

Use this example to deactivate the integration.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "settings":
      {
        "enableDataplexIntegration": false
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Use this example to deactivate the integration.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "settings":
      {
        "enableDataplexIntegration": false
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Enrich Cloud SQL assets with aspects

Aspect types are reusable resources that you can use as templates for aspects. Aspect types help you avoid duplication of work and incomplete aspects. You can use Knowledge Catalog to create the aspect types that you need.

After you create custom aspect types, you can attach aspects to your Cloud SQL assets. Attaching aspects to Cloud SQL assets lets you do the following:

  * Add business metadata to the assets
  * Search for assets by business metadata and other custom metadata



To learn more about creating aspect types and attaching aspects to Cloud SQL, see [Manage aspects and enrich metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata).

## Search for Cloud SQL assets

Use the Knowledge Catalog search page in the Google Cloud console to search for Cloud SQL assets.

  1. Go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. In **Choose search platform** , select **Knowledge Catalog**.

  3. In the **Filters** panel, click **Systems** , and then select **Cloud SQL**.

  4. Optional. In **Type aliases** , you can filter the search results to a specific type of Cloud SQL asset by the selecting one or more of the following type alias:

     * **Database**
     * **Database schema**
     * **Service**
     * **Table**
     * **View**
**Note:** **Service** is a type alias for a Cloud SQL instance.



### Use queries to perform search

You can also use the search field in Knowledge Catalog to perform search queries. To view all Cloud SQL assets, enter `system=Cloud_SQL`.

Then you can enter specific keywords. For example, to view all Cloud SQL databases:
    
    
    system=Cloud_SQL AND type=Database
    

To view all Cloud SQL tables, enter the following query:
    
    
    system=Cloud_SQL AND type=Table
    

You can also use parentheses and the logical operators `AND` and `OR` for complex expressions. To learn more about the expressions that you can use in the search field, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax).

You can directly enter search queries for specific Cloud SQL assets into the search field. The format of the query string is as follows:
    
    
    type="projects/dataplex-types/locations/global/entryTypes/QUERY_STRING"

Replace QUERY_STRING with a query string based on the Cloud SQL engine and type of asset that you want to query. Use the following table to identify the appropriate query string.

Cloud SQL engine | Query strings  
---|---  
**Cloud SQL for MySQL** | 

  * `cloudsql-mysql-database`
  * `cloudsql-mysql-instance`
  * `cloudsql-mysql-table`
  * `cloudsql-mysql-view`

**Note** : Schema is not supported for MySQL.   
**Cloud SQL for PostgreSQL** | 

  * `cloudsql-postgresql-database`
  * `cloudsql-postgresql-instance`
  * `cloudsql-postgresql-table`
  * `cloudsql-postgresql-schema`
  * `cloudsql-postgresql-view`

  
**Cloud SQL for SQL Server** | 

  * `cloudsql-sqlserver-database`
  * `cloudsql-sqlserver-instance`
  * `cloudsql-sqlserver-table`
  * `cloudsql-sqlserver-schema`
  * `cloudsql-sqlserver-view`

  
  
An example query might look like the following:
    
    
    type="projects/dataplex-types/locations/global/entryTypes/cloudsql-postgresql-instance"
    

## Filter Cloud SQL assets by Cloud SQL dialect

By default, Knowledge Catalog displays all Cloud SQL assets. To filter the assets for Cloud SQL for MySQL, Cloud SQL for PostgreSQL, or SQL Server only, then perform the following steps.

  1. In the **Aspects** panel, click the **Add more aspect types** menu.

  2. Select **SQL Access**.

  3. Click **OK**.

  4. Click the  playlist_add  edit aspect button. In the **SQL Access** page, do the following:

     * In the **Dialect** field, select **PostgreSQL** to filter for Cloud SQL for PostgreSQL assets.
  5. Optional. Select the **Version** field, and enter a specific version of Cloud SQL for PostgreSQL. 
  6. Click **Apply**. Knowledge Catalog displays only Cloud SQL for PostgreSQL assets.




## Search by aspect type

Knowledge Catalog includes a few built-in aspect types that you can use to perform searches.

  1. In the **Aspects** panel, click the **Add more aspect types** menu.

  2. Optional. Select **SQL Access** to filter the results by Cloud SQL dialect. For more information, see the previous procedure, Filter Cloud SQL assets by Cloud SQL dialect.

  3. Select one or more of the following aspect types to limit the search results to that type.

     * **Cloud SQL Database**
     * **Cloud SQL Instance**
     * **Cloud SQL View**
     * **Cloud SQL Schema**
     * **Cloud SQL Table**
  4. Click **OK**.

  5. In the results table, click the name of the asset to view the metadata for that asset.

  6. Optional: Enhance or view your assets. You can do any of the following:

     * In **Overview** , click **Add** to add a rich text description of the asset.
     * In **Aspects** , click **Add** to attach an aspect to the asset.
     * For an instance, to view member databases, click the **Entry List** tab, and then click **Show all children entries in search**. If the **Entry List** tab doesn't appear, then the instance has no databases.
     * In **Entry details** , view the full details of the asset. Click the entry name to drill down to additional entries.



### Example workflow - Drill down from instance to columns

In this example workflow, you start by searching for a Cloud SQL instance, then view a member database, then view a table in that database, and then view the columns in the table.

  1. Go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. For the **Choose search platform** option, select **Knowledge Catalog**.

  3. In the **Filters panel** , select **Systems** and then **Cloud SQL**. Alternatively, enter `system=Cloud_SQL` in the search field.

  4. Select an instance name.

  5. On the **Cloud SQL details** page, click the **Entry list** tab, and then click **Show all children entries in search**. Knowledge Catalog displays the databases in the instance.

**Note:** If there is no **Entry list** tab, then return to the **Search** page and choose a different instance.
  6. On the **Cloud SQL database details** page, click the **Entry list** tab, and then click **View child entries in search**. Knowledge Catalog displays the tables in the database.

  7. Select a table name, and then on the **Cloud SQL table details** page, click **Schema** to view the table columns.

  8. Optional: To add an aspect type to a column, click the **Add aspect** button.




This workflow demonstrates drilling down from an instance to a table. You can go directly to a list of tables by entering `system=Cloud_SQL AND type=Table` in the search field.

## Pricing

There is no charge for storing Cloud SQL technical metadata in Knowledge Catalog. Standard Knowledge Catalog pricing applies for API calls and additional business metadata enrichment. For more information, see the [Knowledge Catalog pricing page](https://cloud.google.com/dataplex/pricing).

## Resource usage

While the Knowledge Catalog integration is enabled, Knowledge Catalog extracts data from your instances periodically. The extraction process requires a certain amount of CPU usage. Instances that are integrated with Knowledge Catalog in near real-time generally have a minimal impact on CPU usage. For instances that are integrated with Knowledge Catalog in once a day, the CPU usage can be greater. This is especially noticeable for instances with smaller machine types—for example, machines that have shared cores and larger schemas (10,000 or more tables), which can use up to 40% of their CPU during the extraction process. 

## Limitations

This section lists limitations with using Cloud SQL and Knowledge Catalog.

  * For instances created before April 18, 2026, Knowledge Catalog integration with Cloud SQL is turned off for any instance that restricts access to resources due to resource enrollment in [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

  * After you enable Knowledge Catalog on an instance, it can take between 2 to 48 hours for your Cloud SQL resources to appear in Knowledge Catalog as assets, depending on the machine size, version, and type of Cloud SQL engine that you are using. This limitation doesn't apply when your instance updates in near real-time as described in  Near real-time.


The following limitations only apply when your instance updates in near real-time as described in Near real-time: 

  * When a database is renamed, only the database update is available in Knowledge Catalog in near real-time. The underlying mapping of the database and all the respective tables will be eventually consistent in Knowledge Catalog.
  * An instance might drop messages, which can cause the data in Knowledge Catalog to become only eventually consistent. If messages are dropped, the missed updates become visible in Knowledge Catalog eventually. The cases where an instance might drop messages include the following: 
    * Instances that are experiencing a high rate of DDLs in a short span of time.
    * Instances that are clones of an existing instance.
    * Instances that are restored from backup.
    * Instances that are running out of memory.
    * Instances that are restarting or restarting their databases.
    * Instances that are experiencing network issues or a synchronization process interruption with Knowledge Catalog. 



## What's next

  * [About metadata management in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview)
  * [Knowledge Catalog Identity and Access Management roles](https://docs.cloud.google.com/dataplex/docs/iam-roles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
