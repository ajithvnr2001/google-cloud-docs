---
url: https://docs.cloud.google.com/dataproc-metastore/docs/use-managed-migration/
title: Use managed migration with a Dataproc Metastore service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:36.246910+00:00
---

# Use managed migration with a Dataproc Metastore service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/use-managed-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Use managed migration with a Dataproc Metastore service Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to start and manage a Dataproc Metastore managed migration.

You can configure a migration using the Dataproc Metastore APIs.

## Before you begin

  * Understand how a [managed migration works](https://docs.cloud.google.com/dataproc-metastore/docs/about-managed-migration).
  * [Set up the managed migration prerequisites](https://docs.cloud.google.com/dataproc-metastore/docs/managed-migration-prerequisites).



## Start migration

When you run a _start migration_ , Dataproc Metastore connects to Cloud SQL and uses Cloud SQL as its backend database. During this process, Dataproc Metastore runs a pipeline that copies data from Cloud SQL to its own database (Spanner).

Dataproc Metastore continues to use Cloud SQL as its backend and replicates data until the _complete migration_ process is called.

Before you start a migration, make sure you have set up the [managed migration prerequisites](https://docs.cloud.google.com/dataproc-metastore/docs/managed-migration-prerequisites).

### Start migration considerations

  * A Dataproc Metastore service can only run a single migration at a time.

  * A migration remains active until you complete the migration process. There isn't a deadline to complete your migration, for example, the migration can take 1 day, 30 days, or a year.

  * Scheduled backups are not restricted during a migration. However, the backup might be incomplete. To avoid any issues, disable any scheduled backups while the migration is in progress.




A start migration triggers the following state changes:

  * Dataproc Metastore moves to the `MIGRATING` state.
  * The migration execution state moves to `RUNNING`.
  * The migration execution phase moves to `REPLICATION`.




### Console

**Get started**

  1. In the Google Cloud console, open the **Dataproc Metastore** page:

[Go to Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. On the **Dataproc Metastore** page, click the name of the service you want to migrate to.

The **Service detail** page opens.

  3. At the top of the page, click **Migrate Data**.

The **Create migration** page opens to the **Connectivity** tab and displays the **Cloud SQL database configuration for Dataproc Metastore** configuration settings.




**Cloud SQL database configuration for DPMS**

  1. In the **Instance connection name** , enter the instance connection name of the Cloud SQL database, in the following format: `project_id:region:instance_name`.

  2. In the **IP address** field, enter the IP address required to connect to the Cloud SQL instance.

  3. In the **Port** field, enter **3306**.

  4. In the **Hive database name** enter the name of the database being used as the backend of self-managed Hive Metastore.

  5. In the **Username** field, enter the username that you use to connect Cloud SQL to the Hive Metastore.

  6. In the **Password** field, enter the password that you use to connect Cloud SQL to the Hive Metastore.




**SOCKS5 Proxy service**

  1. In the **Proxy Subnet** field, enter a subnet of [Regular type](https://docs.cloud.google.com/vpc/docs/subnets#purpose). The subnetwork should be present in the Cloud SQL VPC network. This subnet is used to deploy the intermediate SOCKS5 proxy service

  2. In the **Nat Subnet** field, enter a subnet of [Private Service Connect type](https://docs.cloud.google.com/vpc/docs/subnets#purpose). This subnetwork should be present in the Cloud SQL VPC network and is used to publish the [SOCKS5 proxy service using private service connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#add-subnet-psc).

  3. Click **Continue**.

The **Change Data Capture (CDC)** tab opens and displays the **Cloud SQL database configuration for Datastream** configuration settings.




**Cloud SQL database configuration for data stream**

  1. In the **Username** field, enter the username that you use to login to the Cloud SQL CDC used by Datastream.

  2. In the **Password** field, enter the password that you use to login to the Cloud SQL CDC used by Datastream.

  3. In the **VPC network** field, enter the network in the same VPC network as the Cloud SQL instance used by Datastream to establish a private connection to the CDC.

  4. In the **Subnet IP range** field, enter a subnet IP range of at least `/29`. Datastream uses this IP to establish peering to the VPC network.

  5. In the **Reverse proxy subnet** field, enter the subnetwork you created in the same VPC network as the Cloud SQL. Datastream uses this subnetwork. The subnetwork is used to host a [reverse proxy connection](https://docs.cloud.google.com/datastream/docs/private-connectivity#reverse-proxy) for the Datastream CDC. The subnet must be configured in the same region as the Dataproc Metastore service.




**GCS configuration**

  1. For the **Bucket ID** , select the Cloud Storage path to store CDC data during the migration.

  2. In the **Root path** field, enter the root path inside the Cloud Storage bucket. The stream event data is written to this path.

  3. Click **Create**.




### REST
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type:application/json" \
      -X POST -d \
      '{
        "migration_execution": {
          "cloud_sql_migration_config": {
            "cloud_sql_connection_config": {
              "instance_connection_name": INSTANCE_CONNECTION_NAME,
              "hive_database_name": "HIVE_DATABASE_NAME",
              "ip_address": "IP_ADDRESS",
              "port": 3306,
              "username": "CONNECTION_USERNAME",
              "password": "CONNECTION_PASSWORD",
              "proxy_subnet": "PROXY_SUBNET",
              "nat_subnet": "NAT_SUBNET"
            },
            "cdc_config": {
              "username": "CDC_USENAME",
              "password": "CDC_PASSWORD",
              "vpc_network": "VPC_NETWORK",
              "subnet_ip_range": "SUBNET_IP_RANGE",
              "reverse_proxy_subnet": "REVERSE_PROXY_SUBNET_ID",
              "bucket": "BUCKET_NAME",
              "root_path": "ROOT_PATH",
            }
          }
        }
    }' \
      https://metastore.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/SERVICE:startMigration
    

Replace the following:

  * `SERVICE`: the name or ID of your Dataproc Metastore service.
  * `PROJECT_ID`: the project ID of the Google Cloud project your Dataproc Metastore service resides in.
  * `LOCATION`: the Google Cloud region in which your Dataproc Metastore service resides.



**Cloud SQL Migration configuration**

  * `INSTANCE_CONNECTION_NAME`: the instance connection name for the Cloud SQL database, in the following format: `PROJECT_ID/LOCATION/CLOUDSQL_INSTANCE_ID`.
  * `HIVE_DATABASE_NAME`: the name of the self managed Hive database connected to Cloud SQL.
  * `IP_ADDRESS`: the IP address required to connect to the Cloud SQL instance.
  * `CONNECTION_USERNAME`: the username that you use to connect Cloud SQL to the Hive Metastore.
  * `CONNECTION_PASSWORD` the password that you use to connect Cloud SQL to the Hive Metastore
  * `PROXY_SUBNET`: the subnetwork used in the Cloud SQL VPC network. This subnetwork hosts an [intermediate proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-multiple-vpcs#intermediate-proxy) to provide connectivity across transitive networks.
  * `NAT_SUBNET`: a [Private Service Connect subnet](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#add-subnet-psc) that provides a connection from the Dataproc Metastore service to access to the intermediate proxy. The subnet size should have a prefix length of at [least /29](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#psc-subnets) and in the [IPv4 range](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).



**CDC configuration**

  * `CDC_USERNAME`: the username that the Datastream service uses to login into Cloud SQL.
  * `CDC_PASSWORD`: the password that the Datastream service uses to login into Cloud SQL.
  * `VPC_NETWORK`: a network in the same VPC network as the Cloud SQL instance used by Datastream to establish a private connection to the CDC.
  * `SUBNET_IP_RANGE`: A subnet IP range of at least /29 used by Datastream to establish peering to the VPC network.
  * `REVERSE_PROXY_SUBNET_ID`: a subnetwork in the same VPC network as the Cloud SQL instance used by Datastream. The subnetwork is used to host a [reverse proxy connection](https://docs.cloud.google.com/datastream/docs/private-connectivity#reverse-proxy) for the Datastream CDC. The subnet must be configured in the same region as the Dataproc Metastore service.
  * `BUCKET_NAME`: the Cloud Storage path to store CDC data during the migration.
  * `ROOT_PATH`: the root path inside the Cloud Storage bucket. The stream event data is written to this path.



## Complete migration

When you complete a migration, Dataproc Metastore connects to Spanner and starts to use Spanner as its backend database.

A complete migration triggers the following state changes:

  * Dataproc Metastore moves back to the `ACTIVE` state.
  * The migration execution state moves to `SUCCEEDED`.




### Console

  1. In the Google Cloud console, open the [**Dataproc Metastore**](https://console.cloud.google.com/dataproc/metastore/services) page.

  2. At the top of the page, click **Migrate Data**.

The **Migrate Data** page opens and displays your completed managed migrations.




### REST
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type:application/json" \
      -X POST -d '' \
       https://metastore.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/SERVICE:completeMigration
    

Replace the following:

  * `SERVICE`: the name or ID of your Dataproc Metastore service.
  * `PROJECT_ID`: the project ID of the Google Cloud project your Dataproc Metastore service resides in.
  * `LOCATION`: the Google Cloud region in which your Dataproc Metastore service resides.



## Cancel migration

When you cancel a migration, Dataproc Metastore reverts any changes and starts using the Spanner database type as its backend database. Any data that was transferred during the migration is deleted.

A cancel migration triggers the following state changes:

  * Dataproc Metastore moves back to the `ACTIVE` state.
  * The migration execution state moves to `CANCELLED`.




### Console

  1. In the Google Cloud console, open the [**Dataproc Metastore**](https://console.cloud.google.com/dataproc/metastore/services) page.

  2. At the top of the page, click **Migrate Data**.

The **Migrate Data** page opens and displays your canceled managed migrations.




### REST
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type:application/json" \
      -X POST -d '' \
        https://metastore.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/SERVICE:cancelMigration
    

Replace the following:

  * `SERVICE_NAME`: the name or ID of your Dataproc Metastore service.
  * `PROJECT_ID`: the project ID of the Google Cloud project your Dataproc Metastore service resides in.
  * `LOCATION`: the Google Cloud region in which your Dataproc Metastore service resides.



## Get migration details

Get details about a single managed migration.

### Console

  1. In the Google Cloud console, open the [**Dataproc Metastore**](https://console.cloud.google.com/dataproc/metastore/services) page.

  2. At the top of the page, click **Migrate Data**.

The **Migrate Data** page opens and displays your managed migrations.

To get more migration details, click the name of a managed migration.




### REST
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -X GET \
       https://metastore.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/SERVICE/migrationExecutions/MIGRATION_ID
    

Replace the following:

  * `SERVICE`: the name or ID of your Dataproc Metastore service.
  * `PROJECT_ID`: the project ID of the Google Cloud project your Dataproc Metastore service resides in.
  * `LOCATION`: the Google Cloud region in which your Dataproc Metastore service resides.
  * `MIGRATION_ID`: the name or ID of your Dataproc Metastore migration.



## List migrations

List managed migrations.

### Console

  1. In the Google Cloud console, open the [**Dataproc Metastore**](https://console.cloud.google.com/dataproc/metastore/services) page.

  2. At the top of the page, click **Migrate Data**.

The **Migrate Data** page opens and displays your managed migrations.

  3. Verify that the command listed the migrations.




### REST
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -X GET \
       https://metastore.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/SERVICE/migrationExecutions/MIGRATION_ID
    

Replace the following:

  * `SERVICE`: the name or ID of your Dataproc Metastore service.
  * `PROJECT_ID`: the project ID of the Google Cloud project your Dataproc Metastore service resides in.
  * `LOCATION`: the Google Cloud region in which your Dataproc Metastore service resides.



## Delete migrations

Delete managed migrations.

### Console

  1. In the Google Cloud console, open the [**Dataproc Metastore**](https://console.cloud.google.com/dataproc/metastore/services) page.

  2. At the top of the page, click **Migrate Data**.

The **Migrate Data** page opens and displays your managed migrations.

  3. Select the migration and click **Delete**.




### REST
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       -X DELETE \
        https://metastore.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/SERVICE/migrationExecutions/MIGRATION_ID
    

Replace the following:

  * `SERVICE`: the name or ID of your Dataproc Metastore service.
  * `PROJECT_ID`: the project ID of the Google Cloud project your Dataproc Metastore service resides in.
  * `LOCATION`: the Google Cloud region in which your Dataproc Metastore service resides.
  * `MIGRATION_ID`: the name or ID of the Dataproc Metastore migration.



## What's next

  * [Import metadata into a service](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata)
  * [Attach a Managed Service for Apache Spark cluster or self-managed cluster](https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
