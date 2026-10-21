---
url: https://docs.cloud.google.com/sql/docs/sqlserver/connect-to-instance-using-write-endpoint/
title: Connect to an instance using a write endpoint \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:15.552985+00:00
---

# Connect to an instance using a write endpoint  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/connect-to-instance-using-write-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Connect to an instance using a write endpoint Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-to-instance-using-write-endpoint "View this page for the PostgreSQL database engine") | SQL Server

## Overview

This page shows you how to use a write endpoint to connect from clients in your Virtual Private Cloud (VPC) network to a Cloud SQL instance using [private services access (PSA)](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access).

A write endpoint is a global domain name service (DNS) name that resolves to the IP address of the current primary instance automatically. In the case of a replica [failover or switchover](https://docs.cloud.google.com/sql/docs/sqlserver/replication/cross-region-replicas) operation, this write endpoint redirects incoming connections to the new primary instance automatically. You can use the write endpoint in a SQL connection string to the Cloud SQL instance instead of using an IP address. By using a write endpoint, you can avoid having to make application connection changes when you perform a replica failover or switchover operation for region outage recovery or disaster recovery drill.

Each eligible Cloud SQL instance has a single built-in write endpoint whose name, creation, and update are managed by Cloud SQL. The following example illustrates its format:
    
    
      primary.103uufa2svq8u.2rb3qdj9tkf4d.global.sql-psa.goog.
      

The write endpoint always ends with the `.global.sql-psa.goog.` suffix. You can't modify the name or format of this write endpoint managed by Cloud SQL.

You can use the write endpoint for all write operations on the primary instance, including inserts, updates, deletes, and DDL changes. You can also use the write endpoint for read operations, such as queries. The private IP address pointed to by the write endpoint is automatically changed by Cloud SQL when you perform a replica failover or switchover operation to promote a replica instance to be the new primary instance.

## Generate the write endpoint

If you create a new Cloud SQL instance, then Cloud SQL automatically creates the write endpoint when the following prerequisites are met:

  * The following APIs must be [enabled](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api#enabling_an_api) in the Google Cloud project where your Cloud SQL instance resides: 
    * [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1)
    * [Cloud DNS API](https://docs.cloud.google.com/dns/docs/reference/rest/v1)

Failure to enable the Cloud DNS API in the project leads to the failure to create the peering DNS zone which will make the DNS names unusable.

Once the peering DNS zone has been successfully created, it is important that it is not modified in any way. Any modifications including delete will render the DNS to be unusable for database connection.

  * The Cloud SQL instance must be [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro).
  * The Cloud SQL instance must be configured to use a private IP with [private service access (PSA) enabled](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#configure_an_instance_to_use_private_ip).
  * The feature requires instances on the new network architecture. In most cases, new instances are created with the new architecture. To verify this, [check the network architecture of your instance](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture#check-single-instance). 



When you upgrade an existing Cloud SQL Enterprise edition instance to an Cloud SQL Enterprise Plus edition instance, Cloud SQL automatically generates the write endpoint if the previously listed prerequisites are met. If your existing instance is in the old network architecture, then you must first [upgrade the instance to the new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture#upgrade-network-architecture\)) to get the write endpoint.

If you already have a Cloud SQL Enterprise Plus edition instance without the write endpoint and you want Cloud SQL to generate a write endpoint automatically, then create a replica that's enabled for [advanced disaster recovery](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery#create-cascadable-dr-replica). 

## View the write endpoint

### gcloud

To find the write endpoint, use the following gcloud CLI command:
    
    
          gcloud sql instances describe INSTANCE_NAME \
          | grep writeEndpoint
        

Make the following replacements:

INSTANCE_NAME: the name of the Cloud SQL instance.

Write endpoints always end with the `.global.sql-psa.goog.` suffix, similar to the following example:
    
    
      primary.103uufa2svq8u.2rb3qdj9tkf4d.global.sql-psa.goog.
      

If you don't see the write endpoint for an eligible instance, then refer to Troubleshooting.

## Connect to a Cloud SQL instance using a write endpoint

### sqlcmd

To connect a `sqlcmd` client to a Cloud SQL instance using the write endpoint, run the following command:
    
    
        sqlcmd -S WRITE_ENDPOINT -U USERNAME -d DATABASE_NAME
      

Make the following replacements:

  * DATABASE_NAME: the name of the database. For example, `main`.
  * USERNAME: the username. For example, `sqlserver`.
  * WRITE_ENDPOINT: the DNS name or write endpoint. This alphanumeric value always ends with the `.global.sql-psa.goog.` suffix. For example, `primary.103uufa2svq8u.2rb3qdj9tkf4d.global.sql-psa.goog.`.



## Connect database clients to instances using the Cloud SQL Auth Proxy or Cloud SQL Language Connectors

When you configure the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy) or one of the [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/sqlserver/language-connectors) using a write endpoint DNS name, the Cloud SQL connector periodically checks for a [switchover](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery#switchover) or [failover](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery#replica-failover) operation. When the Cloud SQL connector detects that the write endpoint DNS name refers to a different instance, it closes all open connections to the old instance. Subsequent connection attempts are directed to the new instance.

**Caution** : Be sure to notify application owners before starting a switchover or failover operation. During the switchover and failover, the connector or Auth Proxy forcibly terminates all open database connections. 

For example, suppose an application is configured to connect using the write endpoint DNS name `primary.103uufa2svq8u.2rb3qdj9tkf4d.global.sql-psa.goog`. Initially, the DNS zone is configured with a record pointing to the primary instance, `my-project:region:instance-a`. The application establishes connections to the `my-project:region:instance-a` Cloud SQL instance.

When the failover or switchover occurs, Cloud SQL updates the DNS record from `my-project:region:instance-a` to the designated [DR replica](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery#designated-dr-replica) instance: `my-project:other-region:instance-b`.

The Cloud SQL connector used by the application detects the change to this DNS record. When the application connects to its database using the write endpoint DNS name `primary.103uufa2svq8u.2rb3qdj9tkf4d.global.sql-psa.goog`, it connects to the `my-project:other-region:instance-b` Cloud SQL instance.

The connector or Auth Proxy automatically closes all existing connections to `my-project:region:instance-a`. This forces any connection pools used by the application to establish new connections. It can also cause database queries in progress to fail.

The Cloud SQL Auth Proxy polls for changes to the DNS name every 30 seconds.

### Update the instance network configuration

If your instance was created before June 30, 2026, then you might need to update the instance's network configuration for Cloud SQL Language Connectors or the Cloud SQL Auth Proxy to be able to use the write endpoint. You only need to run this update task once for each instance. Run the following command:

### [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)
    
    
      # Update the primary instance DNS settings
      gcloud sql instances patch "PRIMARY_NAME" \
          --reconcile-psa-networking
      

Make the following replacements:

  * PRIMARY_NAME: the name of the instance. For example, `my-instance`



### Connect database clients to instances using the Cloud SQL Auth Proxy

To connect to a Cloud SQL instance by its write endpoint and using the Cloud SQL Auth Proxy, first start the proxy using the write endpoint instead of the instance connection name.

### sqlcmd
    
    
      $ cloud-sql-proxy --port PORT WRITE_ENDPOINT --private-ip
      

Then configure the database client to connect to the Cloud SQL Auth Proxy:
    
    
      sqlcmd
        -S 127.0.0.1, PORT -U USERNAME \
        -d DATABASE_NAME
      

Make the following replacements:

  * WRITE_ENDPOINT: the DNS name or write endpoint. This alphanumeric value always ends with the `.global.sql-psa.goog.` suffix. For example, `primary.103uufa2svq8u.2rb3qdj9tkf4d.global.sql-psa.goog.`.
  * PORT: the port number used. For example, `1433`.
  * USERNAME: the username. For example, `sqlserver-user`.
  * DATABASE_NAME: the name of the database. For example, `sqlserver-database`.



### Connect using Cloud SQL Language Connectors

To connect using one of the Cloud SQL Language Connectors, configure your application by following the instructions in the [Connect using Cloud SQL Language Connectors documentation](https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors). Then, modify your database connection to use the write endpoint instead of the instance DNS name.

### Java
    
    
      String jdbcUrl = "jdbc:sqlserver://WRITE_ENDPOINT:1433;"
      "databaseName=DATABASE_NAME;"
        +   "socketFactoryClass=com.google.cloud.sql.sqlserver.SocketFactory;"
        +   "socketFactoryConstructorArg=WRITE_ENDPOINT?ipTypes=PRIVATE;"
        +   "user=USERNAME;"
        +   "password=PASSWORD;"
      

Make the following replacements:

  * WRITE_ENDPOINT: the DNS name or write endpoint. This alphanumeric value always ends with the `.global.sql-psa.goog.` suffix.
  * DATABASE_NAME: the name of the database. For example, `my-database`.
  * USERNAME: the username. For example, `sqlserver-user`.
  * PASSWORD: the database password.

For more information, see the [Java connector documentation](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/blob/main/docs/jdbc.md#using-dns-domain-names-to-identify-instances) on GitHub. 

### Go
    
    
      db, err := sql.Open(
          "cloudsql-sqlserver",
          "sqlserver://USERNAME:PASSWORD@WRITE_ENDPOINT?database=DATABASE_NAME&encrypt=disable",
      )
      

Make the following replacements:

  * WRITE_ENDPOINT: the DNS name or write endpoint. This alphanumeric value always ends with the `.global.sql-psa.goog.` suffix.
  * DATABASE_NAME: the name of the database. For example, `my-database`.
  * USERNAME: the username. For example, `sqlserver-user`.
  * PASSWORD: the database password.

For more information, see the [Go connector documentation](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector/?tab=readme-ov-file#using-dns-domain-names-to-identify-instances) on GitHub. 

### Python
    
    
      Connector = Connector(resolver=DnsResolver)
      engine = sqlalchemy.create_engine(
          "mssql+pytds://",
          creator=lambda: connector.connect(
              "WRITE_ENDPOINT",  # using DNS name
              "pytds",
              user="USERNAME",
              password="PASSWORD",
              db="DATABASE_NAME"
          ),
      )
      

Make the following replacements:

  * WRITE_ENDPOINT: the DNS name or write endpoint. This alphanumeric value always ends with the `.global.sql-psa.goog.` suffix.
  * DATABASE_NAME: the name of the database. For example, `my-database`.
  * USERNAME: the username. For example, `sqlserver-user`.
  * PASSWORD: the database password.

For more information, see the [Python connector documentation](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/?tab=readme-ov-file#using-dns-domain-names-to-identify-instances) on GitHub. 

### Node.js
    
    
      import sql from 'mssql';
      import {Connector} from '@google-cloud/cloud-sql-connector';
    
      const connector = new Connector();
      const clientOpts = await connector.getTediousOptions({
        domainName: 'WRITE_ENDPOINT',
        ipType: 'PRIVATE',
      });
      const pool = new sql.ConnectionPool({
        ...clientOpts,
        user: 'USERNAME',
        password: 'PASSWORD',
        database: 'DATABASE_NAME',
        pool: {
          max: 5,
        }
      });
      Await pool.connect();
      

Make the following replacements:

  * WRITE_ENDPOINT: the DNS name or write endpoint. This alphanumeric value always ends with the `.global.sql-psa.goog.` suffix.
  * DATABASE_NAME: the name of the database. For example, `my-database`.
  * USERNAME: the username. For example, `sqlserver-user`.
  * PASSWORD: the database password.

For more information, see the [Node.js connector documentation](https://github.com/GoogleCloudPlatform/cloud-sql-nodejs-connector/?tab=readme-ov-file#using-dns-domain-names-to-identify-instances) on GitHub. 

## Limitations

  * Write endpoints aren't available for Cloud SQL Enterprise edition instance creations.
  * Write endpoints aren't available for public IP only instances or Private Service Connect only instances.



## Troubleshooting

The following sections describe the architecture of write endpoints and address common troubleshooting issues.

### Architecture of a write endpoint

When you create an eligible instance, a write endpoint is generated by default.

To create a write endpoint, Cloud SQL performs the following setup:

  * Creates a [private DNS zone](https://docs.cloud.google.com/dns/docs/zones/zones-overview#zonal-dns-zones) in the service Cloud SQL producer VPC network
  * Creates a [peering DNS zone](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering_zones) in the customer VPC network
  * Creates a DNS record in the private DNS zone in the service producer network



The following diagram illustrates how this process works:

![Diagram showing how VPC peering supports DNS zone peering between projects.](https://docs.cloud.google.com/static/sql/images/psa-dns-arch.png)**Figure 1.** Diagram showing how VPC peering supports DNS zone peering between a service producer network and a customer network.

### DNS resolutions issues

If DNS resolution isn't working, then check each of the following items:

  1. Make sure all prerequisites are met.
  2. Make sure that the clients where the resolution is expected are located in the same network to which the Cloud SQL instance is attached. To check this, use the `[gcloud compute instances list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list)` command: 
         
         gcloud compute instances list \
            --format="table( name, zone.basename(), networkInterfaces[].network )" \
            --project=PROJECT_NAME

Replace PROJECT_NAME with the project name where the DNS consumer network resides.

  3. Verify that the peering zone exists. To do so, use the `[gcloud dns managed-zones list](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/list)` command: 
         
         gcloud dns managed-zones list \
             --project=PROJECT_NAME

Replace PROJECT_NAME with the project name where the DNS consumer network resides.




### New instance doesn't have a write endpoint

If a newly created instance doesn't contain a write endpoint, then check each of the following items:

  1. Make sure that all prerequisites are completed.
  2. Make sure there isn't a leftover peering DNS zone with the DNS name `sql-psa.goog.`. 

A peering DNS zone is a leftover DNS zone if the network associated with the DNS zone doesn't have a VPC peering with the peer project ID of the peering DNS zone.

If there's a leftover peering DNS zone with the `sql-psa.goog.` suffix, then delete it.

**Caution** : Use extreme caution when you delete the peering DNS zone. If you delete the incorrect DNS zone, then you can cause connectivity loss for all instances attached to the network.

To check for leftover peering DNS zones, use the `[gcloud dns managed-zones list](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/list)` command:
         
         gcloud dns managed-zones list \
            --project=PROJECT_NAME

Replace PROJECT_NAME with the name of the project where the DNS consumer network resides.

If a DNS zone exists with the `sql-psa.goog.` suffix, then delete the DNS zone after double-checking that the peering DNS zone is a leftover DNS zone.

To delete a DNS zone, use the `[gcloud dns managed-zones delete](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/delete)` command:
         
         gcloud dns managed-zones delete ZONE_NAME

Replace ZONE_NAME with the DNS zone name associated with the write endpoints. Values are alphanumeric and use the following format: `cloud-sql-psa-dns-1234567890`.

  3. You can fix a missing write endpoint for an eligible instance by using the `[gcloud sql instances patch](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--reconcile-psa-networking)` command: 
         
         gcloud sql instances patch INSTANCE_NAME --reconcile-psa-networking

Replace INSTANCE_NAME with the name of your Cloud SQL instance.




## What's next

  * Learn more about [Cloud SQL troubleshooting](https://docs.cloud.google.com/sql/docs/sqlserver/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
