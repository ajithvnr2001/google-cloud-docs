---
url: https://docs.cloud.google.com/alloydb/docs/knowledge-catalog-integration/
title: Manage your AlloyDB resources using Knowledge Catalog \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:40.797544+00:00
---

# Manage your AlloyDB resources using Knowledge Catalog  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/knowledge-catalog-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Manage your AlloyDB resources using Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Knowledge Catalog integration with AlloyDB is now enabled by default for all new AlloyDB clusters. 

Knowledge Catalog integration is enabled by default for all new AlloyDB clusters, allowing you to search for and manage your AlloyDB for PostgreSQL resources using Knowledge Catalog, a platform that lets you store, manage, and access metadata. This integration helps you discover and understand your AlloyDB metadata, supporting the following use cases:

  * **Analysis:** Understand dependencies and assess suitability for various use cases.
  * **Change Management:** Track and manage metadata changes effectively.
  * **Schema Evolution:** Monitor and plan schema modifications.



Knowledge Catalog automatically retrieves the following metadata from AlloyDB clusters, instances, databases, tables, columns, and views:

  * Name
  * Location (Region)
  * Labels (for clusters and instances)
  * Dataplex Integration Enabled (for clusters)
  * Database Version
  * Machine CPU Count (for instances)
  * Availability Type (for instances)
  * Charset (for databases)
  * Collation (for databases)
  * Owner
  * Description (for table, views, columns, and foreign keys)
  * Type (for clusters, instances, and machines)
  * Columns 
    * Data Type
    * Mode
  * Primary Key
  * Foreign Keys 
    * Referenced Table
    * Column Mappings
  * Creation Time
  * Last modification Time



For more information, see [About metadata management in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview).

**Note:** Knowledge Catalog refers to resources in AlloyDB and in other Google Cloud services as _assets_. In this document, AlloyDB resources—clusters, instances, databases, tables, schemas and views—are called AlloyDB _assets_. Assets also refer to the resources and their Knowledge Catalog metadata.

## Types of metadata discovery

Knowledge Catalog metadata discovery is an automated process that scans connected data sources—such as AlloyDB—to identify data assets like tables, views, and databases. Then, Knowledge Catalog extracts technical metadata from the assets like schemas, descriptions, and locations, into Knowledge Catalog.

This process syncs metadata in near real-time, which keeps the catalog synchronized with source systems. For AlloyDB, cluster and instance metadata is discovered by default. Database, schema, table, and view metadata discovery is enabled by default on new clusters. For clusters created before this default was implemented (February 26, 2026), manually [enable the integration](https://docs.cloud.google.com/alloydb/docs/dataplex-catalog-integration#enable-dataplex-cluster).

### Keyword and natural language search

Knowledge Catalog supports keyword and natural language searches.

  * Keyword search helps you find resources using specific keywords, filters, and a defined syntax. For example, to view all AlloyDB databases, enter `system=AlloyDB AND type=Database`.
  * Natural language search uses AI to understand semantic queries. It helps you find resources using everyday language, eliminating the need for complex syntax. For example, enter a query such as `List all AlloyDB tables related to sales`.



For more information, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax).

### Example: Discovering an AlloyDB database schema

To understand the metadata discovery process, consider the example of an AlloyDB cluster named `user-data-cluster` with Knowledge Catalog integration enabled. Inside this cluster's primary instance, a database named `profiles` exists, which contains a table `customers` (`id`, `email`, `signup_date`) and a view `active_users` (`id`, `email`).

Because AlloyDB syncs in near real-time to Knowledge Catalog, the following resources are available:

  * Clusters
  * Columns
  * Databases
  * Instances
  * Tables
  * Views



After discovery is complete, search for these assets—`customers` table and `active_users`—in the Knowledge Catalog page of the Google Cloud console or by using the API. Then, view their schemas and enrich them with additional business or operational metadata.

## Enrich metadata using aspects

_Aspect types_ are reusable resources that serve as templates for aspects. Aspect types help avoid duplicating work and creating incomplete aspects. Create the necessary aspect types using Knowledge Catalog.

After you create custom aspect types, attach aspects to your AlloyDB assets. Attaching aspects to AlloyDB assets lets you do the following:

  * Add business metadata to the assets.
  * Search for assets by business metadata and other custom metadata.



To learn more about creating aspect types and attaching aspects to AlloyDB, see [Manage aspects and enrich metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata).

## Metadata discovery workflow

By default, cluster and instance resources are ingested and discoverable. To ingest and discover database, schema, table and view resources, follow these steps:

  1. [Enable the Knowledge Catalog integration](https://docs.cloud.google.com/alloydb/docs/dataplex-catalog-integration#enable-dataplex-cluster) for your AlloyDB cluster using the AlloyDB API if it's not already enabled. This is required for clusters created before February 26, 2026.

  2. Search for your AlloyDB assets using the Knowledge Catalog search page in the Google Cloud console. For more information, see [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets).

  3. To add more context to your AlloyDB assets, attach aspects to your assets. _Aspects_ are custom metadata entries that help with data governance and analysis. For example, use an aspect to label a column that contains personally identifiable information (PII). For more information, see [Manage aspects and enrich metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata).

  4. Navigate through your AlloyDB resources following this hierarchy: Cluster > Database > Schema > Table or View > Column. This hierarchy provides a detailed view of your data landscape. For more information, see [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets).




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

You must have specific Identity and Access Management (IAM) roles and permissions to search for and attach entries to AlloyDB assets. For more information, see Required IAM roles and permissions for Knowledge Catalog. 




### Required IAM roles

This section describes the roles and permissions required to search for resources and to access the search results.

#### Required roles for accessing search results

To search for and view AlloyDB metadata in Knowledge Catalog, principals require permissions to view AlloyDB resources, including the `dataplex.projects.search` permission.

To grant principals—such as users, groups, or service accounts—these permissions, assign them the **AlloyDB Viewer** ([`roles/alloydb.viewer`](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions)) IAM role on the project that contains the AlloyDB resources.

Knowledge Catalog operation | AlloyDB resource | Roles or permissions required  
---|---|---  
Search for AlloyDB resources | Cluster | `alloydb.clusters.get`  
Columns | `alloydb.databases.get`  
Instance | `alloydb.instances.get`  
Database | `alloydb.databases.get`  
Tables | `alloydb.databases.get`  
Views | `alloydb.databases.get`  
**Caution:** If you grant the `roles/alloydb.viewer` role at the project level, principals with this role can view the metadata for all AlloyDB instances in the project.

If you don't want to use the predefined **AlloyDB Viewer** role, assign a custom role that includes `alloydb.clusters.get`, `alloydb.instances.get`, and `alloydb.databases.get` permissions.

For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). For more information about AlloyDB IAM roles, see [IAM roles and permissions for AlloyDB](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions).

#### Required roles for searching entries

You must have at least one of the following [IAM roles](https://docs.cloud.google.com/dataplex/docs/iam-roles#predefined-roles) on the project used for search:

  * Dataplex Catalog Admin ([`roles/dataplex.catalogAdmin`](https://docs.cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogAdmin))
  * Dataplex Catalog Editor ([`roles/dataplex.catalogEditor`](https://docs.cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogEditor))
  * Dataplex Catalog Viewer ([`roles/dataplex.catalogViewer`](https://docs.cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogViewer))



Permissions on search results are checked independently of the selected project. For more information, see [Search for data assets with Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets#required-roles).

## Knowledge Catalog integration data freshness

By default, Knowledge Catalog ingests and discovers cluster and instance resources, and their metadata freshness is near real-time.

The Knowledge Catalog integration for database, schema, table, and view resources is enabled by default when you create a new AlloyDB cluster. To prevent this metadata from syncing, [disable the integration](https://docs.cloud.google.com/alloydb/docs/dataplex-catalog-integration#deactivate-integration).

Enabling the integration activates the export of AlloyDB metadata—such as databases, schemas, and tables—to Cloud Storage buckets for periodic sync or to Pub/Sub topics for near real-time sync, making it available to Knowledge Catalog. This feature is only applicable to primary clusters. Secondary clusters used for cross-region replication don't support Knowledge Catalog integration for database, schema, table, and view metadata.

**Note:** Resource-level metadata, such as cluster and instance metadata, is always enabled and can't be disabled.

The metadata freshness for these resources depends on when the cluster was created or restored:

  * **Near real-time:** clusters created or restored on or after April 3, 2026, sync metadata to Knowledge Catalog in near real-time. Updates are available in Knowledge Catalog in up to 5 minutes. The extraction process typically takes a few seconds.

  * **Every few hours:** clusters created or restored between February 26, 2026, and April 3, 2026 refresh metadata in Knowledge Catalog every few hours. Updates are available in Knowledge Catalog in up to 48 hours. The extraction process typically takes a few minutes, but time to completion depends on the CPU size and the table count.


**Note:** To upgrade clusters from every few hours to near real-time synchronization, [contact Google Cloud Support](https://cloud.google.com/support).

## Create AlloyDB with Knowledge Catalog integration disabled

You can control this integration when you create or update a cluster using the Google Cloud CLI or the [AlloyDB API](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters):

### gcloud

Use the `gcloud alloydb clusters create` command to create an AlloyDB cluster. If you omit the `--enable-dataplex-integration` flag, [Knowledge Catalog integration is enabled by default](https://docs.cloud.google.com/alloydb/docs/dataplex-catalog-integration#freshness) for database, schema, table, and view metadata. For a complete list of parameters for this call, see [`gcloud alloydb clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create). For information about cluster settings, see [View cluster and instance settings](https://docs.cloud.google.com/alloydb/docs/cluster-settings?resource=primary).

Don't include sensitive or personally identifiable information in your cluster ID because the cluster ID might be visible in various operational contexts, such as system logs, monitoring dashboards, and support communications. You don't need to include the project ID in the cluster name. The system automatically includes this where appropriate, for example, in the log files.

To disable Knowledge Catalog integration for database, schema, table, and view resources, include the `--no-enable-dataplex-integration` flag:
    
    
    gcloud alloydb clusters create CLUSTER_ID \
        --password=PASSWORD \
        --region=REGION \
        --no-enable-dataplex-integration

Make the following replacements:

  * `CLUSTER_ID`: the ID of the cluster that you create. The cluster ID must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `PASSWORD`: the password that you use for the default `postgres` user.
  * `REGION`: the ID of the cluster's region.



### REST

Use the `POST` method to create an AlloyDB cluster. If you omit the `dataplexConfig` from the request, [Knowledge Catalog integration enables by default](https://docs.cloud.google.com/alloydb/docs/dataplex-catalog-integration#freshness) for database, schema, table, and view metadata. For a complete list of parameters for this call, see [Method: projects.locations.clusters.create](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/create). For information about cluster settings, see [View cluster and instance settings](https://docs.cloud.google.com/alloydb/docs/cluster-settings?resource=primary).

Don't include sensitive or personally identifiable information in your cluster ID because the cluster ID might be visible in various operational contexts, such as system logs, monitoring dashboards, and support communications. You don't need to include the project ID in the cluster name. The system automatically includes this where appropriate, for example, in the log files.

To disable Knowledge Catalog integration for database, schema, table, and view resources, include `"dataplexConfig": { "enabled": false }` in the request body:
    
    
    {
      "databaseVersion": "DATABASE_VERSION",
      "initialUser": {
        "user": "INITIAL_USERNAME",
        "password": "INITIAL_USER_PASSWORD"
      },
      "labels": {
        "test": "alloydb-cluster-full"
      },
      "dataplexConfig" : {
        "enabled" : false
      }
    }

Make the following replacements:

  * `DATABASE_VERSION`: enum string of the database version—for example, `POSTGRES_16`.
  * `INITIAL_USERNAME`: the username that you use for the default postgres user.
  * `INITIAL_USER_PASSWORD`: the password that you use for the default postgres user.



Use the following HTTP method and URL:
    
    
    POST https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters?cluster_id=CLUSTER_ID
    

Make the following replacements:

  * `PROJECT_ID`: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the cluster.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `CLUSTER_ID`: the ID of the cluster that you create. The cluster ID must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.



To send your request, use one of the following options:

#### curl (Linux, macOS, or Cloud Shell)

The following command assumes you signed in to the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you in to the gcloud CLI. Check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
    
    
        curl -X POST \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             -d @request.json \
            "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters?cluster_id=CLUSTER_ID"
          

#### PowerShell (Windows)

The following command assumes you signed in to the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you in to the gcloud CLI. Check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
        -Method POST `
        -Headers $headers `
        -ContentType: "application/json; charset=utf-8" `
        -InFile request.json `
        -Uri "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters?cluster_id=CLUSTER_ID"| Select-Object -Expand Content
    

You receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "alloydb#operation",
      "targetLink": "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/clusters/CLUSTER_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-09-25T22:19:33.735Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "CLUSTER_ID",
      "selfLink": "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }

## Enable the Knowledge Catalog integration for your AlloyDB cluster

To enable the Knowledge Catalog integration on an existing cluster, use one of the following procedures:

### gcloud

To enable the Knowledge Catalog integration on an existing cluster, use the `gcloud alloydb clusters update` command with the `--enable-dataplex-integration` flag.
    
    
    gcloud alloydb clusters update CLUSTER_ID \
        --region=REGION \
        --enable-dataplex-integration

Make the following replacements:

  * `CLUSTER_ID`: the name of the cluster.
  * `REGION`: the ID of the cluster's region.



### REST

To update specific fields of an existing cluster, use the `PATCH` method on the [`projects.locations.clusters resource`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters).

Use the following HTTP method and URL:
    
    
    PATCH https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID?updateMask=dataplexConfig.enabled
    

Make the following replacements:

  * `PROJECT_ID`: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the cluster.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `CLUSTER_ID`: the name of the cluster.



Request JSON body:
    
    
    {
      "dataplexConfig": {
        "enabled": true
      }
    }

To send your request, use one of the following options:

#### curl (Linux, macOS, or Cloud Shell)

The following command assumes you signed in to the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you in to the gcloud CLI. Check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
    
    
        curl -X PATCH \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             -d @request.json \
            "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID?updateMask=dataplexConfig.enabled"
          

#### PowerShell (Windows)

The following command assumes you signed in to the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you in to the gcloud CLI. Check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
        -Method PATCH `
        -Headers $headers `
        -ContentType: "application/json; charset=utf-8" `
        -InFile request.json `
        -Uri "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID?updateMask=dataplexConfig.enabled"| Select-Object -Expand Content
    

You receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "alloydb#operation",
      "targetLink": "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/clusters/CLUSTER_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-09-25T22:19:33.735Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "CLUSTER_ID",
      "selfLink": "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }

## Verify Knowledge Catalog integration on your AlloyDB cluster

To verify that the Knowledge Catalog integration is enabled on an existing cluster, use one of the following procedures:

### gcloud

To verify that the Knowledge Catalog integration is enabled on an existing cluster, use the `gcloud alloydb clusters describe` command.
    
    
    gcloud alloydb clusters describe CLUSTER_ID --region=REGION

Make the following replacements:

  * `CLUSTER_ID`: the cluster ID.
  * `REGION`: the ID of the cluster's region.



The output includes the `dataplexConfig` section in YAML format. If `enabled` is `true`, then Knowledge Catalog integration is enabled:
    
    
    dataplexConfig:
      enabled: true

### REST

To verify that the Knowledge Catalog integration is enabled on an existing cluster, use the `GET` method.

Use the following HTTP method and URL:
    
    
    GET https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID
    

Make the following replacements:

  * `PROJECT_ID`: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the cluster.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `CLUSTER_ID`: the cluster ID.



To send your request, use one of the following options:

#### curl (Linux, macOS, or Cloud Shell)

The following command assumes you signed in to the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you in to the gcloud CLI. Check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID"
          

#### PowerShell (Windows)

The following command assumes you signed in to the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you in to the gcloud CLI. Check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
        -Method GET `
        -Headers $headers `
        -Uri "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID"| Select-Object -Expand Content
    

You receive a JSON response for the entire Cluster proto, which includes the `dataplexConfig` message:
    
    
    {
      "dataplexConfig": {
        "enabled": true
      }
    }

## Deactivate the integration of Knowledge Catalog on your AlloyDB cluster

When you disable integration of Knowledge Catalog on your AlloyDB cluster, only the cluster and instance metadata are available.

### gcloud

Use the `gcloud alloydb clusters update` command with the `--no-enable-dataplex-integration` flag to deactivate the integration.
    
    
    gcloud alloydb clusters update CLUSTER_ID \
        --region=REGION \
        --no-enable-dataplex-integration

Make the following replacements:

  * `CLUSTER_ID`: the ID of the cluster.
  * `REGION`: the ID of the cluster's region.



### REST

Use the following example to deactivate the integration.

Use the following HTTP method and URL:
    
    
    PATCH https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID?updateMask=dataplexConfig.enabled
    

Make the following replacements:

  * `PROJECT_ID`: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the cluster.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `CLUSTER_ID`: the cluster ID.



Request JSON body:
    
    
    {
      "dataplexConfig": {
        "enabled": false
      }
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

The following command assumes you signed in to the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you in to the gcloud CLI. Check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
    
    
    curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d @request.json \
         "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID?updateMask=dataplexConfig.enabled"
          

#### PowerShell (Windows)

The following command assumes you signed in to the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you in to the gcloud CLI. Check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
        -Method PATCH `
        -Headers $headers `
        -ContentType: "application/json; charset=utf-8" `
        -InFile request.json `
        -Uri "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID?updateMask=dataplexConfig.enabled"| Select-Object -Expand Content
    

You receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "alloydb#operation",
      "targetLink": "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/clusters/CLUSTER_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "CLUSTER_ID",
      "selfLink": "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }

## Enrich AlloyDB assets with aspects

_Aspect types_ are reusable resources that serve as templates for aspects. Aspect types help avoid duplicating work and creating incomplete aspects. Create the necessary aspect types using Knowledge Catalog.

After you create custom aspect types, attach aspects to your AlloyDB assets. Attaching aspects to AlloyDB assets provides the following capabilities:

  * Add business metadata to the assets
  * Search for assets by business metadata and other custom metadata



To learn more about creating aspect types and attaching aspects to AlloyDB, see [Manage aspects and enrich metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata).

## Search for AlloyDB assets

Use the Knowledge Catalog search page in the Google Cloud console to search for AlloyDB assets.

  1. Go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. In **Choose search platform** , select **Knowledge Catalog**.

  3. In the **Filters** panel, click **Systems** , and then select **AlloyDB**.

  4. Optional. In **Type aliases** , filter the search results to a specific type of AlloyDB asset by selecting one or more of the following type aliases:

     * Database
     * Database schema
     * Cluster
     * Instance
     * Service
     * Table
     * View
**Note:** Service is a type alias for an AlloyDB instance.



### Use queries to perform keyword search

Use the search field in Knowledge Catalog to perform keyword search queries. For example, enter `system=AlloyDB AND type=Database` to view all AlloyDB databases.

For more information, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax).

To view all AlloyDB assets, enter `system=AlloyDB`.

Then enter specific keywords. For example, to view all AlloyDB databases:
    
    
    system=AlloyDB AND type=Database
    

To view all AlloyDB tables, enter the following query:
    
    
    system=AlloyDB AND type=Table
    

You can also use parentheses and the logical operators `AND` and `OR` for complex expressions. For more information about the expressions you can use in the search field, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax).

You can directly enter search queries for specific AlloyDB assets into the search field. The format of the query string is as follows:
    
    
    type="projects/dataplex-types/locations/global/entryTypes/QUERY_STRING"

Replace the following:

  * `QUERY_STRING`: use the following list to identify a query string based on the type of AlloyDB asset that you want to query:

    * `alloydb-database`
    * `alloydb-cluster`
    * `alloydb-instance`
    * `alloydb-table`
    * `alloydb-schema`
    * `alloydb-view`



An example query might look like the following:
    
    
    type="projects/1234567890/locations/global/entryTypes/alloydb-cluster"
    

## Search by aspect type

Knowledge Catalog includes a few built-in aspect types that help you perform searches.

To search by aspect type, follow these steps:

  1. In the **Aspects** panel, click the **Add more aspect types** menu.
  2. Optional. Select **AlloyDB Access** to filter the results by AlloyDB dialect.
  3. Select one or more of the following aspect types to limit the search results to that type. 
     * AlloyDB Database
     * AlloyDB Cluster
     * AlloyDB Instance
     * AlloyDB View
     * AlloyDB Schema
     * AlloyDB Table
  4. Click **OK**.
  5. In the results table, click the name of the asset to view the metadata for that asset.
  6. Optional: Enhance or view your assets. You can enhance or view your assets in the following ways: 
     * To add a rich text description of the asset, click **Add** in **Overview**.
     * To attach an aspect to the asset, click **Add** in **Aspects**.
     * To view member databases for an instance, click the **Entry List** tab, and then click **Show all children entries in search**. If the **Entry List** tab doesn't appear, then the cluster has no databases.
     * View the full details of the asset in **Entry details**. Click the entry name to drill down to additional entries.



### Natural Language search in AlloyDB

Natural language search uses AI to understand semantic queries. It helps you find resources using everyday language, eliminating the need for complex syntax. For example, enter queries such as `List all AlloyDB tables related to sales`.

For more information, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax).

### Syntax search in AlloyDB

Keyword search helps you find resources using specific keywords, filters, and a defined syntax. For example, enter `system=AlloyDB AND type=Database` to view all AlloyDB databases.

For more information, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax).

### Example workflow - Drill down from cluster to columns

To drill down from cluster to columns, follow these steps:

  1. Go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. For the **Choose search platform** option, select **Knowledge Catalog**.

  3. In the **Filters panel** , select **Systems** and then **AlloyDB**. Alternatively, enter `system=AlloyDB` in the search field.

  4. Select a cluster name.

  5. On the **AlloyDB details** page, click the **Entry list** tab, and then click **Show all children entries in search**. Knowledge Catalog displays the databases in the cluster.

**Note:** If the **Entry list** tab doesn't appear, return to the **Search** page and choose a different cluster.
  6. On the **AlloyDB database details** page, click the **Entry list** tab, and then click **View child entries in search**. Knowledge Catalog displays the tables in the cluster.

  7. Select a table name, and then on the **AlloyDB table details** page, click **Schema** to view the table columns.

  8. Optional: To add an aspect type to a column, click the **Add aspect** button.




## Pricing

There is no charge for storing AlloyDB technical metadata in Knowledge Catalog. Standard Knowledge Catalog pricing applies for API calls and additional business metadata enrichment. For more information, see the [Knowledge Catalog pricing page](https://docs.cloud.google.com/dataplex/pricing).

### Resource usage

Knowledge Catalog periodically extracts metadata from your AlloyDB clusters. This extraction process consumes CPU resources on your cluster. The CPU usage is generally minimal. For example, clusters with smaller machine types (such as `n2-highmem-2-icelake`) that manage large schemas (such as those with 100,000 or more tables) might experience a CPU usage increase of up to 5% during the extraction.

## Limitations

  * The integration supports a maximum of one million tables per database and an average of 150 columns per table. If either of these limits is exceeded, metadata for resources such as databases, schemas, tables, and views is not extracted. Only cluster and instance metadata is available in Knowledge Catalog.
  * When a cluster is first created, the initial synchronization of all metadata to Knowledge Catalog can take up to 48 hours. After the initial sync, subsequent updates are available in near real-time.
  * In case of a high rate of metadata changes (over 100 or more DDL changes per second) on your database, Near real-time metadata synchronization with Knowledge Catalog might pause for up to 30 minutes before resuming.
  * In the event any update is missed due to high rate of metadata changes, networking issues or when the synchronization process is interrupted, they eventually become visible in Knowledge Catalog within 48 hours.
  * When an instance doesn't exist or is not running, it can take 7 days for metadata to be deleted.
  * When a database is renamed, only the database update is available in Knowledge Catalog in near real-time. The underlying mapping of the database and all the respective tables will be updated in Knowledge Catalog within 48 hours.



## What's next

  * [About metadata management in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview)
  * [Knowledge Catalog Identity and Access Management roles](https://docs.cloud.google.com/dataplex/docs/iam-roles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
