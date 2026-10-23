---
url: https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version/
title: Perform an in-place major version database upgrade \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:59.824096+00:00
---

# Perform an in-place major version database upgrade  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Perform an in-place major version database upgrade Stay organized with collections  Save and categorize content based on your preferences. 

To upgrade an AlloyDB for PostgreSQL cluster to a higher PostgreSQL major version while preserving your existing instance names, IP addresses, and connection strings, you can plan, validate, and run an in-place major version upgrade. To learn about in-place major version upgrade use cases, workflow stages, and automatic backups, see [Database in-place major version upgrade overview](https://docs.cloud.google.com/alloydb/docs/major-version-upgrade-inplace-overview).

## Plan a major database version upgrade

Use the following steps to plan a major database version upgrade:

  1. Find your current database major version.

###  Console 

     1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

     2. Select a cluster from the list. The **Overview** page appears.

     3. Locate the database major version in the **Version** field.

###  gcloud 

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Run the following command to get the cluster details, including the current major version:
    
    gcloud alloydb clusters describe CLUSTER_ID --region=REGION

Make the following replacements:

     * CLUSTER_ID: the cluster ID
     * REGION: the cluster location or region

###  REST v1beta 

Run the following request to get the cluster details, including the current major version:
    
    GET https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID

Make the following replacements:

     * CLUSTER_ID: the cluster ID
     * PROJECT_ID: the project ID
     * REGION: the cluster location or region

To send your request, use one of the following options:

#### _curl (Linux, macOS, or Cloud Shell)_

The following command assumes that you are signed into the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs/use-cloud-shell-terminal) which automatically signs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             "https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID"
       

#### _PowerShell (Windows)_

The following command assumes that you are signed into the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Run the following command: 
    
    $cred = gcloud auth print-access-token
       $headers = @{ "Authorization" = "Bearer $cred" }
    
       Invoke-WebRequest `
         -Method GET `
         -Headers $headers `
         -Uri "https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID| Select-Object -Expand Content
       

  2. Identify a target database major version from the following table. For a complete list of the database versions that AlloyDB supports, see [Database versions and version policies](https://docs.cloud.google.com/alloydb/docs/db-version-policies).

**Source major version** | **Supported target major version(s)**  
---|---  
POSTGRES_14 | 
     * POSTGRES_15
     * POSTGRES_16
     * POSTGRES_17
     * POSTGRES_18  
POSTGRES_15 | 
     * POSTGRES_16
     * POSTGRES_17
     * POSTGRES_18  
POSTGRES_16 | 
     * POSTGRES_17
     * POSTGRES_18  
POSTGRES_17 | 
     * POSTGRES_18  
  3. Review the features offered in each database major version.

     * [PostgreSQL 18](https://www.postgresql.org/docs/18/release-18.html)
     * [PostgreSQL 17](https://www.postgresql.org/docs/17/release-17.html)
     * [PostgreSQL 16](https://www.postgresql.org/docs/16/release-16.html)
     * [PostgreSQL 15](https://www.postgresql.org/docs/15/release-15.html)
     * [PostgreSQL 14](https://www.postgresql.org/docs/14/static/release-14.html)
  4. Identify any incompatibilities that you need to address. New major versions can introduce incompatible changes that might require you to modify the application code, the schema, or the database settings.

  5. Before you start the major version upgrade on your production cluster, we recommend that you [clone your cluster](https://docs.cloud.google.com/alloydb/docs/backup/restore) and test the major version upgrade on the cloned cluster.

In addition to verifying that the upgrade completes successfully, run tests to ensure that the application behaves as expected on the upgraded cluster.




## Prepare the cluster for a major version upgrade

To connect to the database, use one of the following options:

  * [AlloyDB Studio](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#run)
  * [psql](https://docs.cloud.google.com/alloydb/docs/connect-psql)
  * [Other connection methods](https://docs.cloud.google.com/alloydb/docs/connection-overview)

1\. Drop or promote your cross-region replicas. Database In-place major version upgrades don't support cross-region replicas. For more information, see [Cross-region replication](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication). 

  1. If your AlloyDB cluster is a [logical replication](https://www.postgresql.org/docs/current/logical-replication.html) source, disable downstream subscriptions and drop all logical replication slots. You can re-enable the subscriptions and recreate the logical replication slots after the upgrade. If the AlloyDB instance is only a logical replication target, these steps are not required. To disable subscriptions and drop logical replication slots, follow these steps:

     1. Disable each downstream subscription on the subscriber or downstream replication target. Don't disable the downstream subscriptions on the AlloyDB instance being upgraded:

        * If you're using `pglogical`, run the following command:
              
              SELECT * FROM
              pglogical.alter_subscription_disable(SUBSCRIPTION_NAME, immediate);
              

Replace `SUBSCRIPTION_NAME` in the query with the existing subscription name. If the subscription needs to be disabled immediately, set the value of the `immediate` parameter to `true`. By default, the value is `false` and the subscription is disabled only after the current transaction ends.

For example:
              
              postgres=> SELECT * FROM pglogical.alter_subscription_disable('test_sub',true);
              alter_subscription_disable
              ----------------------------
              t
              (1 row)
              

        * If you're using an extension other than `pglogical`, run the following command:
              
              ALTER SUBSCRIPTION SUBSCRIPTION_NAME DISABLE;
              

     2. Drop all logical replication slots on the AlloyDB primary instance by running the following command:
            
            SELECT pg_drop_replication_slot(REPLICATION_SLOT_NAME) FROM pg_replication_slots WHERE slot_type = 'logical';
            

Replace `REPLICATION_SLOT_NAME` in the query with the name of the replication slot.

  2. Manage your PostgreSQL extensions. For more information, see [Configure database extensions](https://docs.cloud.google.com/alloydb/docs/instance-configure-extensions).

Pre-upgrade checks detect extension incompatibilities and surface those violations in the logs, along with suggested actions. For more information, see [View pre-upgrade check failures](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-database-inplace-major-version-upgrade#pg-upgrade-check-failures).

You might need to do the following:

     1. Drop any extensions that are no longer supported in the target version.
     2. Upgrade PostGIS and the related extensions (`address_standardizer`, `address_standardizer_data_us`, `postgis_raster`, `postgis_sfcgal`, `postgis_tiger_geocoder`, and `postgis_topology`) to a supported version in the target PostgreSQL version. For more information, see [PostGIS extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions#postgis-extensions). The following table lists the minimum supported PostGIS extension versions for each PostgreSQL major version:

**PostgreSQL version** | **PostGIS minimum supported version**  
---|---  
PG14 | 3.1  
PG15 | 3.2  
PG16 | 3.4  
PG17 | 3.5  
PG18 | 3.6  
  
For example, if your PostGIS version is 3.1.x and you want to upgrade from POSTGRES 14 to POSTGRES 16, use the following command to upgrade the PostGIS extension:
            
            ALTER EXTENSION postgis UPDATE TO '3.4.0';
            SELECT PostGIS_Version();
            

  3. Verify that your clusters don't contain orphaned role memberships. In-place major version upgrades don't preserve role memberships where the original grantor no longer exists. If any cluster contains orphaned memberships in the `pg_auth_members` catalog, these role memberships are lost after the upgrade.

To detect orphaned memberships, run the following query:
         
         SELECT roleid::regrole, member::regrole, grantor::regrole
         FROM pg_auth_members
         WHERE grantor::regrole::text ~ '^[0-9]+$';
         

If the query returns any rows, recreate the role memberships before you upgrade the cluster. For each orphaned membership, revoke the privilege and immediately re-grant it. This associates the membership with a current, valid grantor (such as `alloydbadmin`).

Run the following transaction block for each orphaned membership:
         
         BEGIN;
         REVOKE ROLE_NAME FROM MEMBER_NAME;
         GRANT ROLE_NAME TO MEMBER_NAME;
         COMMIT;
         

Replace ROLE_NAME and MEMBER_NAME with the roles from the query results.

  4. Verify that connections are allowed for each database, except for `template0`, by running the following query and checking the `datallowconn` field for each database:
         
         SELECT datname,datallowconn from pg_database;
         

A `t` value in the `datallowconn` field means that the connection is allowed. An `f` value indicates that a connection can't be established. The `template0` database must not allow connections.

To allow connections to a database, run the following command:
         
         ALTER DATABASE DATABASE_NAME WITH ALLOW_CONNECTIONS = true;
         

  5. Verify that `template1` is a template database, by running the following command:
         
         SELECT datname, datistemplate FROM pg_database WHERE datname = 'template1';
         

If `datistemplate` is `f`, set it to `true` by running the following command:
         
         ALTER DATABASE template1 WITH IS_TEMPLATE true;
         




## Upgrade the cluster major version in-place

The database in-place major version upgrade can take between 40 minutes and 48 hours to complete, depending on factors like database size, schema size, and the number of read pool instances in the cluster. The primary instance downtime is typically 20 minutes to one hour, and primarily depends on your database schema.

When you place an in-place major version upgrade request, AlloyDB first performs pre-upgrade checks. If AlloyDB determines that your cluster isn't ready for a major version upgrade, the request fails. For more information, see [Troubleshoot a major version in-place upgrade](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-database-inplace-major-version-upgrade).

To upgrade the major database version in place, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Select a cluster from the list. The **Overview** page appears.

  3. Click **Upgrade** to start the database major version upgrade process.

  4. On the **Choose database version** step, select one of the available database major versions as the target major version.

  5. Click **Continue**.

  6. In the **Upgrade cluster** step, in the **Cluster ID** field, enter the name of the cluster.

  7. Click **Start upgrade**. You are directed to the **Upgrade Status** step, where you can check the upgrade status. For more information, see Monitor the major database version upgrade.




###  gcloud 

Start the in-place major version upgrade by running the following command:
    
    
    gcloud alloydb clusters upgrade CLUSTER_ID --region=REGION --version=DATABASE_VERSION --async

The following is an example command:
    
    
    gcloud alloydb clusters upgrade my-cluster --region=us-central1 --version=POSTGRES_16 --async

###  REST v1beta 

Start the in-place major version upgrade by running the following command:
    
    
    PATCH https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID:upgrade

Request JSON body:
    
    
    {
      "version": "DATABASE_VERSION"
    }

Replace with the enum for the target database major version, which must be later than the current version.

Sample request JSON body:
    
    
    {
    "version": "POSTGRES_16"
    }

* { Terraform } 
    
    
    **Warning :** To keep your Terraform state consistent, update configurations directly in your Terraform files. If you make manual changes using the Google Cloud console, gcloud CLI, or REST API, the following issues can occur:
    
    
    
      
        * API errors
    
      
        * Perpetual diffs
    
      
        * Overwritten changes during terraform apply
    
    
    To upgrade an instance within your database cluster to a PostgreSQL version, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance) and set the `database_version` to a [supported target major version](/alloydb/docs/upgrade-db-inplace-major-version#plan-upgrade).
    
    ```none
    resource "google_alloydb_instance" "default" {
    cluster       = google_alloydb_cluster.default.name
    instance_id   = "alloydb-instance"
    instance_type = "PRIMARY"
    
    machine_config {
      cpu_count = 2
    }
    
    depends_on = [google_service_networking_connection.vpc_connection]
    }
    
    resource "google_alloydb_cluster" "default" {
      cluster_id = "alloydb-cluster"
      location   = "us-central1"
      network_config {
        network = google_compute_network.default.id
      }
      database_version = "POSTGRES_16"
    
      initial_user {
        password = "alloydb-cluster"
      }
    }
    
    data "google_project" "project" {}
    
    resource "google_compute_network" "default" {
      name = "alloydb-network"
    }
    
    resource "google_compute_global_address" "private_ip_alloc" {
      name          =  "alloydb-cluster"
      address_type  = "INTERNAL"
      purpose       = "VPC_PEERING"
      prefix_length = 16
      network       = google_compute_network.default.id
    }
    
    resource "google_service_networking_connection" "vpc_connection" {
      network                 = google_compute_network.default.id
      service                 = "servicenetworking.googleapis.com"
      reserved_peering_ranges = [google_compute_global_address.private_ip_alloc.name]
    }
    ```
    
    To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](/docs/terraform/basic-commands).
    

## Monitor the cluster major version upgrade

After the in-place major database version upgrade starts, you can monitor the upgrade status using the Google Cloud console, the gcloud CLI, or the REST API.

###  Console 

Follow these steps to check the upgrade status in the Google Cloud console:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Select the cluster undergoing the upgrade. The **Overview** page appears.

  3. Open the **Overview** page.

  4. Click **Upgrade Status**. The **Upgrade Status** page appears, where you can check the status of the upgrade.




###  gcloud 

Follow these steps to check the upgrade status in the gcloud CLI:

  1. Get the upgrade operation ID by running the following command. Before you run the command, replace the `CLUSTER_ID` variable with the name of the cluster:
         
         gcloud alloydb operations list --cluster=CLUSTER_ID --region=REGION_ID --filter=metadata.verb:upgrade

The gcloud CLI call used to trigger a major version upgrade. `alloydb beta clusters upgrade`, returns the operation ID as a synchronous response. Alternatively, use the [`gcloud alloydb operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations/list) command with the `--cluster` flag.

The following is an example command:
         
         gcloud alloydb operations list --cluster=my-cluster --region=us-central1 --filter=metadata.verb:upgrade

  2. Monitor the status of the upgrade by running the [`gcloud alloydb operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations/describe) command:
         
         gcloud alloydb operations describe OPERATION_ID
         --region=REGION




###  REST v1beta 

Follow these steps to check the upgrade status in the REST API:

  1. Get the upgrade operation ID.

Use the following `GET` request with the [`operations.list`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.operations/list) method to list all upgrade operations and find the one corresponding to the target cluster:
         
         GET https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION/operations/filter=metadata.verb:upgrade

The REST API call returns the operation ID as a synchronous response.

  2. Monitor the status of the upgrade.

Use a GET request with the [`operations.get`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.operations/get) method:
         
         GET https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID

Make the following replacements:

     * PROJECT_ID: the project ID
     * REGION: the cluster location or region
     * OPERATION_ID: the upgrade operation ID, which was retrieved in the previous step.

The following is an example response when the operation is in progress:
    
    {
    "name": "projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID",
    "metadata": {
    "@type": "type.googleapis.com/google.cloud.alloydb.v1.OperationMetadata",
    "createTime": "2024-09-16T23:17:39.727319438Z",
    "target": "projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID",
    "verb": "upgrade",
    "requestedCancellation": false,
    "apiVersion": "v1",
    "upgradeClusterStatus": {
       "state": "IN_PROGRESS",
       "cancellable": true,
       "stages": [
        {
          "stage": "ALLOYDB_PRECHECK",
          "state": "IN_PROGRESS"
        },
        {
          "stage": "PG_UPGRADE_CHECK",
          "state": "IN_PROGRESS"
        },
        {
          "stage": "PREPARE_FOR_UPGRADE",
          "state": "NOT_STARTED"
        },
        {
          "stage": "PRIMARY_INSTANCE_UPGRADE",
          "state": "NOT_STARTED"
        },
        {
          "stage": "CLEANUP",
          "state": "NOT_STARTED"
        }
       ]
     }
    },
    "done":false
    }
    

The following is a sample response, when the operation is complete:
    
    {
    "operations": [
    {
     "metadata": {
     "@type": "type.googleapis.com/google.cloud.alloydb.v1betaalpha.OperationMetadata",
     "createTime": "2024-09-16T21:52:17.303861317Z",
     "endTime": "2024-09-16T22:29:13.947527949Z",
     "target": "projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID",
     "verb": "upgrade",
     "requestedCancellation": false,
     "apiVersion": "v1beta",
     "upgradeClusterStatus": {
      "state": "SUCCESS",
      "stages": [
        {
          "stage": "ALLOYDB_PRECHECK",
          "state": "SUCCESS"
        },
        {
          "stage": "PG_UPGRADE_CHECK",
          "state": "SUCCESS"
        },
        {
          "stage": "PREPARE_FOR_UPGRADE",
          "state": "SUCCESS"
        },
        {
          "stage": "PRIMARY_INSTANCE_UPGRADE",
          "state": "SUCCESS"
        },
        {
          "stage": "CLEANUP",
          "state": SUCCESS"
        }
       ]
     }
    },
    "response": {
         …
    },
    "name":  "projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID",
    "done": true
    }
    ]
    }
    

For more information about the `response` structure, see Upgrade operation response.




### Upgrade operation response

The `UpgradeCluster` operation response includes the following:

  * `status`: status of the overall upgrade operation. Possible values are `SUCCESS`, `FAILED`, and `PARTIAL_SUCCESS.`
  * `message`: provides a brief summary of the upgrade operation result.
  * `clusterUpgradeDetails`: upgrade details for the clusters being upgraded. This field is an array. AlloyDB only allows a single cluster upgrade, so it includes only one entry. 
    * `name`: fully qualified name of the cluster.
    * `upgradeStatus`: the status of the cluster upgrade. Possible values are `SUCCESS`, `FAILED`, `PARTIAL_SUCCESS`. `PARTIAL_SUCCESS` means that one or more read pool instances can't be upgraded.
    * `clusterType`: the cluster type. AlloyDB only lets you upgrade a single `PRIMARY` cluster. This type must always be `PRIMARY`.
    * `databaseVersion`: the current database version of the cluster.
    * `stageInfo`: information about the core upgrade stages. 
      * `status`: `SUCCESS` or `FAILED`
      * `logs_url`: link to the logs generated by the stage. Empty for stages that don't generate logs.
    * `instanceUpgradeDetails`: upgrade information for all instances in the cluster. 
      * `name`: fully qualified name of the instance
      * `upgradeStatus`: `SUCCESS` or `FAILED`
      * `instanceType`: `PRIMARY` or `READ_POOL`



The following is a sample upgrade operation response:
    
    
    "response": {
      "@type": "type.googleapis.com/google.cloud.alloydb.v1alpha.UpgradeClusterResponse",
      "status": "SUCCESS",
      "message": "Cluster upgraded successfully.",
      "clusterUpgradeDetails": [
        {
          "name": "projects/1234/locations/us-central1/clusters/abc",
          "upgradeStatus": "SUCCESS",
          "clusterType": "PRIMARY",
          "databaseVersion": "POSTGRES_16",
          "stageInfo": [
            {
              "stage": "ALLOYDB_PRECHECK",
              "status": "SUCCESS",
              "logsUrl": "https://console.cloud.google.com/logs/query..."
            },
            {
              "stage": "PG_UPGRADE_CHECK",
              "status": "SUCCESS",
              "logsUrl": "https://console.cloud.google.com/logs/query..."
            },
            {
              "stage": "PRIMARY_INSTANCE_UPGRADE",
              "status": "SUCCESS",
              "logsUrl": "https://console.cloud.google.com/logs/query..."
            },
            {
              "stage": "READ_POOL_INSTANCES_UPGRADE",
              "status": "SUCCESS",
            }
          ],
          "instanceUpgradeDetails": [
            {
              "name": "projects/1234/locations/us-central1/clusters/abc/instances/primary",
              "upgradeStatus": "SUCCESS",
              "instanceType": "PRIMARY",
            },
            {
              "name": "projects/1234/locations/us-central1/clusters/abc/instances/read1",
              "upgradeStatus": "SUCCESS",
              "instanceType": "READ_POOL",
            },
            {
              "name": "projects/1234/locations/us-central1/clusters/abc/instances/read2",
              "upgradeStatus": "SUCCESS",
              "instanceType": "READ_POOL",
            }
          ]
        }
      ]
    }
    

### View AlloyDB upgrade logs

AlloyDB publishes all upgrade logs to the `postgres_upgrade` log name.

To view upgrade related logs, follow these steps:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select `alloydb.googleapis.com/postgres_upgrade` as the log name. This translates to the query `"logName="projects/PROJECT_ID/logs/alloydb.googleapis.com%2Fpostgres_upgrade"`.

  3. Use the following labels to filter the logs: 

**Label** | **Description**  
---|---  
`LOG_TYPE` | Upgrade stage which generated the log. Possible values are `ALLOYDB_PRECHECK`, `PG_UPGRADE_CHECK`, and `PG_UPGRADE`.  
`OPERATION_NAME` | Full operation name for the upgrade operation.  
`FILE_NAME` | Populated only for `pg_upgrade_check` and `pg_upgrade` logs, and corresponds to the log files generated by the `pg_upgrade` utility.  



The following is a sample query that returns AlloyDB pre-check upgrade logs for a given operation:
    
    
    logName="projects/project1234/logs/alloydb.googleapis.com%2Fpostgres_upgrade"
    labels.LOG_TYPE="ALLOYDB_PRECHECK"
    labels.OPERATION_NAME="projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID"
    

For more information about upgrade checks, see [Database in-place major version upgrade overview](https://docs.cloud.google.com/alloydb/docs/major-version-upgrade-inplace-overview).

#### View upgrade logs for a cluster

To view the upgrade logs for a cluster when you don't know the operation ID and the operation has expired, follow these steps:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Query for the AlloyDB pre-check logs for your cluster.
         
         logName="projects/PROJECT_ID/logs/alloydb.googleapis.com%2Fpostgres_upgrade"
         labels.LOG_TYPE="ALLOYDB_PRECHECK"
         resource.labels.cluster_id=CLUSTER_ID
         

  3. Find the `Operation_ID` from the `OPERATION_NAME` log label.

In the following example, `Operation_ID` from `OPERATION_NAME` is `operation-1728225968201-623cff6ed1e02-e34b7191-3cd92013`.
         
         labels.OPERATION_NAME="projects/myproject/locations/us-central1/operations/operation-1728225968201-623cff6ed1e02-e34b7191-3cd92013"
         

  4. Query for all `postgres_upgrade` logs for a specific operation.
         
         logName="projects/production-1/logs/alloydb.googleapis.com%2Fpostgres_upgrade"
         labels.OPERATION_NAME="operation-1728225968201-623cff6ed1e02-e34b7191-3cd92013"
         




## Cancel the database in-place major version upgrade

You can cancel an in-progress major version upgrade operation from the Google Cloud console, the gcloud CLI, or the REST API.

### Find the operation ID

To cancel the major version upgrade operation using the gcloud CLI or the REST API, you need the operation ID. You must specify this ID in the gcloud CLI or REST API command so that AlloyDB knows which operation to cancel.

You can't cancel the upgrade after the primary instance upgrade reaches a certain point.

When you start the in-place major version upgrade, the operation ID is returned in the `name` field of the response. See the Response example.

You can also find the operation ID by making an [`operations.list`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.operations/list) call on the AlloyDB cluster.

### Cancel the upgrade

To cancel a major version upgrade in place, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Select a cluster from the list. The **Overview** page appears.

  3. Click **Upgrade** **status**.

  4. Click **Cancel Upgrade**. If the upgrade isn't cancelable, this button is grayed out.




###  gcloud 

Use the [`gcloud alloydb operations cancel`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations/cancel) command to cancel the operation:
    
    
    gcloud alloydb operations cancel OPERATION_ID

Replace the OPERATION_ID variable with the ID of the operation.

If the `UpgradeClusterStatus` shows `cancellable` as `false` in the output of the [`gcloud alloydb operations cancel`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations/cancel) command, AlloyDB ignores the cancellation request and continues with the upgrade. In this case, the API doesn't throw an error, and it returns an empty response. For more information about the upgrade status, see Monitor the cluster major version upgrade.

###  REST v1beta 

Run the following command:
    
    
    POST https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/operations/OPERATION_ID:cancel
    

Before you use any of the request data, make the following replacements:

  * PROJECT_ID: the project ID.
  * OPERATION_ID: the ID of the import or export operation.



If `cancellable` in `UpgradeClusterStatus` is `false`, you can't cancel the upgrade.

To send your request, use one of the following options:

#### _curl (Linux, macOS, or Cloud Shell)_

The following command assumes that you signed into the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs/use-cloud-shell-terminal) which automatically signs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Run the following command:
    
    
           curl -X POST \
                 -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                 -H "Content-Type: application/json; charset=utf-8" \
                 -d "" \
                "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID:cancel"
      

#### _PowerShell (Windows)_

The following command assumes that you signed into the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Run the following command:
    
    
           $cred = gcloud auth print-access-token
           $headers = @{ "Authorization" = "Bearer $cred" }
    
           Invoke-WebRequest `
             -Method POST `
             -Headers $headers `
             -Uri "https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/operations/OPERATION_ID:cancel"| Select-Object -Expand Content
        

You should receive a JSON response similar to the following:

#### _Response_

This REST API call doesn't return any response.

## Complete the in-place major version upgrade

To complete the major version upgrade, connect to an AlloyDB instance using [AlloyDB Studio](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#run), [psql](https://docs.cloud.google.com/alloydb/docs/connect-psql), or [other connection methods](https://docs.cloud.google.com/alloydb/docs/connection-overview).

If you're using a non-AlloyDB system, consult your system documentation for connection instructions.

After you upgrade your cluster, follow these steps to complete your upgrade:

  1. If you previously disabled `pglogical`, re-enable `pglogical` replication. Enabling `pglogical` replication automatically creates the required replication slot.

     1. Drop the `pglogical` subscription on the destination replica by using the following command:
            
            select pglogical.drop_subscription(subscription_name name);
            

Replace `name` with the name of the existing subscription. For example:
            
            postgres=> select pglogical.drop_subscription(subscription_name:= 'test_sub');
            -[ RECORD 1 ]-----+--
            drop_subscription |1
            

     2. Recreate the `pglogical` subscription on the destination or replica by providing the following connection information to the AlloyDB primary instance:
            
            SELECT pglogical.create_subscription(
              subscription_name :='test_sub',<br>
              provider_dsn := 'host=primary-ip port=5432 dbname=postgres user=replication_user password=replicapassword'
              );
            

     3. Check the status of the subscription by using the following command:
            
            SELECT * FROM pglogical.show_subscription_status('test_sub');
            

     4. Test the replication by performing write transactions and verifying that the changes are visible on the destination.

  2. Manually update your database extensions in your upgraded databases.

Although major version upgrades automatically install the latest extension binaries on your instance's underlying software, they don't automatically update the extension's database catalog. You are responsible for manually updating your extensions to make sure they use the latest supported versions. For instructions, see [Update an extension](https://docs.cloud.google.com/alloydb/docs/instance-configure-extensions#update-extension).

  3. Refresh the database statistics.

After the upgrade completes, run `ANALYZE` on your primary cluster to update the system statistics. Accurate statistics ensure that the PostgreSQL query planner processes queries optimally. Missing statistics can result in inaccurate query plans, which might degrade performance and take up excessive memory.

  4. Run acceptance tests to ensure that the upgraded system performs as expected.

  5. Verify that the upgraded database in-place major version appears on the cluster's **Overview** page in the Google Cloud console.




## Restore to the previous major version

If your upgraded database system doesn't perform as expected, you might need to revert to the pre-upgrade state. You can achieve this by restoring from a pre-upgrade backup –either the one that AlloyDB automatically creates during the upgrade process or an existing pre-upgrade backup– to create a new cluster with the pre-upgrade state.

**Note:** AlloyDB doesn't let you revert or downgrade the same cluster to the pre-upgrade version.

To restore to a pre-upgrade state, follow these steps:

  1. Identify a pre-upgrade backup to restore from. During the upgrade process, AlloyDB automatically creates a pre-upgrade backup with the prefix `pre-upgrade-bkp`. For more information, see [View a list of backups](https://docs.cloud.google.com/alloydb/docs/backup/list).

  2. Initiate a restore from the pre-upgrade backup, which creates a new cluster with the previous PostgreSQL version. For more information, see [Restore a cluster from a stored backup](https://docs.cloud.google.com/alloydb/docs/backup/restore).

  3. Connect your application. Update your application with details about the restored cluster and its read replicas. You can resume serving traffic on the restored cluster.




You can also perform a point-in-time recovery to a pre-upgrade point in time. For more information, see [Use point-in-time recovery (PITR)](https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr).

## Limitations

The following limitations affect in-place major version upgrades for AlloyDB:

\- You can't perform an in-place major version upgrade on a [secondary cluster](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication). \- When you perform a in-place major version upgrade, note that upgrading instances with more than 1,000 databases or 1 million objects (like tables and views) takes a long time, and the upgrade might time out. This limitation is independent of actual data size. \- AlloyDB doesn't support upgrading clusters that use `pg_largeobject_metadata`. If `select count(*) from pg_largeobject_metadata;` is non-zero, then the upgrade fails. \- AlloyDB doesn't preserve role memberships where the original grantor no longer exists. If your database contains these orphaned memberships, resolve them before you upgrade. For more information, see Prepare the cluster. \- The in-place major version upgrade operation might complete before the pre-upgrade backup or before the post-upgrade backups completes, especially when you have a large database with fewer schema objects. \- There might be a short delay between the time when writes start again on the upgraded instance and when the post-upgrade backup is created. This means that post-upgrade backup contents might not match the contents of the database from before the major version upgrade. \- Pre-upgrade backups might still be created when an in-place major version upgrade fails. \- Because automatic upgrade backups are continuous, you can't delete them until they reach the continuous backups and recovery maximum retention. When maximum retention is reached, the backups are garbage collected; alternatively, you can use the gcloud CLI to [manually delete the backups](https://docs.cloud.google.com/alloydb/docs/backup/delete#procedure). For more information, see [Restrictions on deleting backups](https://docs.cloud.google.com/alloydb/docs/backup/delete#restrictions). 

## What's next

  * Learn more about [database in-place major version upgrades](https://docs.cloud.google.com/alloydb/docs/major-version-upgrade-inplace-overview).
  * [Troubleshoot an in-place major version upgrade](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-database-inplace-major-version-upgrade).
  * Learn about [database in-place major version upgrade errors](https://docs.cloud.google.com/alloydb/docs/troubleshoot/database-inplace-major-version-upgrade-errors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
