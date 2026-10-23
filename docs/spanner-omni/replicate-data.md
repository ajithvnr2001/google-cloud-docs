---
url: https://docs.cloud.google.com/spanner-omni/replicate-data/
title: Replicate data from Spanner to Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:35.681785+00:00
---

# Replicate data from Spanner to Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/replicate-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Replicate data from Spanner to Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

This document describes patterns, configuration steps, and operational guidance for setting up disaster recovery topologies between managed Spanner on Google Cloud and Spanner Omni in an external environment like AWS or an on-premises data center.

By combining transaction streaming using change streams and dedicated network connectivity through Cross-Cloud Interconnect, you can achieve low recovery point objectives (RPO) and recovery time objectives (RTO) across cloud boundaries.

## Architecture overview

In a cross-cloud disaster recovery topology, Spanner on Google Cloud serves as the primary database, and Spanner Omni serves as a standby deployment or secondary disaster recovery site. You can replicate transactional changes continuously using change streams.

The following table compares database capabilities, roles, and operational boundaries between a primary Spanner deployment and a secondary Spanner Omni deployment on AWS.

Comparison of primary Spanner and secondary Spanner Omni deployments  Capability or dimension | Primary site: Spanner on Google Cloud | Secondary site: Spanner Omni on AWS  
---|---|---  
Deployment model |  Fully managed service on Google Cloud. |  Self-managed software on AWS, such as Amazon Elastic Compute Cloud (Amazon EC2) or Amazon Elastic Kubernetes Service (Amazon EKS).   
Availability SLA |  Up to 99.999% for multi-region configurations and 99.99% for regional configurations. For more information, see the [Spanner SLA](https://cloud.google.com/spanner/sla).  |  Customer-governed; depends on your infrastructure and topology.   
Replication mode |  Synchronous Paxos-based replication across zones and regions. |  Asynchronous, near-real-time change data capture (CDC) using change streams.   
Recovery point objective (RPO) |  Near-zero within the managed instance. |  Sub-second to seconds across cloud boundaries, depending on pipeline throughput and network latency.   
Recovery time objective (RTO) |  Immediate, automated failover across replicas. |  Depends on your DNS and traffic switchover runbook.  
Network transit layer |  [Virtual Private Cloud (VPC) Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).  |  Cross-Cloud Interconnect connected to AWS Direct Connect.   
Backup storage target |  Google-managed Spanner backups, which can be restored only to managed Spanner.  |  Cloud Storage or Amazon Simple Storage Service (Amazon S3), which can be restored only to Spanner Omni.   
  
## Before you begin

Before you configure replication between Spanner and Spanner Omni, ensure that your environment meets these requirements:

  * **Provision matching destination capacity** : Size your destination Spanner Omni deployment to match the CPU, memory, and storage I/O capacity of your primary Spanner instance. Undersizing the deployment can cause replication lag and prevent the standby cluster from handling workloads during a failover. For more information, see [System requirements](https://docs.cloud.google.com/spanner-omni/system-requirements).
  * **Synchronize database schemas and baseline data** : Create the destination database and tables in Spanner Omni using the same SQL dialect, GoogleSQL or PostgreSQL, and schema definitions as your source Spanner database. Because you can't restore a managed Spanner backup into Spanner Omni, export existing data from Spanner to Avro files in Cloud Storage and import them into Spanner Omni. For more information, see [Schema and data model](https://docs.cloud.google.com/spanner/docs/schema-and-data-model), [Develop with Spanner Omni](https://docs.cloud.google.com/spanner-omni/develop), [Export databases from Spanner to Avro](https://docs.cloud.google.com/spanner/docs/export), and [Import and export data](https://docs.cloud.google.com/spanner-omni/import-export-data).
  * **Establish private network connectivity** : Configure private network routing between your Google Cloud VPC network and your external environment so that your replication workers can connect to both Spanner and the Spanner Omni gRPC endpoint. For more information, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product) and Accelerate replication with Cross-Cloud Interconnect.



## Replicate data continuously using change streams

For applications that require cross-cloud business continuity, [Spanner change streams](https://docs.cloud.google.com/spanner/docs/change-streams) output transactional data changes (`INSERT`, `UPDATE`, and `DELETE` operations) in commit-timestamp order. A continuous replication pipeline reads change records from Spanner on Google Cloud and writes them to your Spanner Omni deployment.

Using change streams for cross-cloud replication provides these benefits:

  * **Active-passive standby** : Maintains a warm replica on Spanner Omni that's ready to serve workloads when you initiate a failover.
  * **Selective replication** : You can configure change streams to watch the entire database or restrict them to specific tables and columns to reduce cross-cloud transfer costs.
  * **Dialect parity** : Because Spanner Omni supports the same GoogleSQL and PostgreSQL dialects and schema semantics as Spanner, your application queries run without modification after cutover.



### Step 1: Create a change stream on the source database

Create a change stream on your source Spanner database to track changes on your target tables. For example, run this DDL statement in your Spanner database:
    
    
    CREATE CHANGE STREAM CHANGE_STREAM_NAME
    FOR TABLE_NAMES
    OPTIONS (
      retention_period = '7d',
      value_capture_type = 'NEW_ROW_AND_OLD_VALUES'
    );
    

Replace the following:

  * `CHANGE_STREAM_NAME`: the name of your change stream, for example, `CsToOmniDrStream`.
  * `TABLE_NAMES`: a comma-separated list of tables to track, for example, `Customers, Orders, AccountBalances`, or `ALL` to track all tables in the database.



Setting `retention_period` to `'7d'` retains change stream records for up to seven days, which helps prevent data loss if your replication pipeline experiences extended maintenance or connectivity interruptions. For more information, see [Create and manage change streams](https://docs.cloud.google.com/spanner/docs/change-streams/manage).

### Step 2: Deploy a change data capture pipeline

To stream changes from Spanner to Spanner Omni, deploy a continuous change data capture (CDC) pipeline using Dataflow with Apache Beam, or run custom worker pods on Google Kubernetes Engine (GKE) or Amazon EKS.

A production replication pipeline performs these tasks:

  * **Reads partitions** : Uses the Spanner Change Streams API or the Apache Beam SpannerIO connector to read change records across dynamic change stream partitions. For more information, see [Change stream partitions, records, and queries](https://docs.cloud.google.com/spanner/docs/change-streams/details) and [Process change stream records using Dataflow](https://docs.cloud.google.com/spanner/docs/change-streams/use-dataflow).
  * **Buffers and orders mutations** : Sequences and batches transactions according to their commit timestamps (`commit_timestamp`) per key range or table to maintain transactional consistency and maximize write throughput.
  * **Writes to Spanner Omni** : Connects over gRPC to the private endpoint of the Spanner Omni deployment and applies the batched mutations. If you use the Apache Beam SpannerIO connector with encryption, use Apache Beam 2.69.0 or later for TLS, or 2.75.0 or later for mutual TLS (mTLS). For more information, see [Use Apache Beam and SpannerIO to connect to Spanner Omni](https://docs.cloud.google.com/spanner-omni/beam) and [Authentication and authorization](https://docs.cloud.google.com/spanner-omni/authentication).
  * **Monitors replication lag** : Tracks the difference between the current time and the `commit_timestamp` of processed change records so that you can alert on replication delays.



If you use Dataflow or Apache Beam, you must use the Apache Beam Java SDK because the Python SDK doesn't include a change streams connector. For custom worker pods, this Python example shows how to configure a Spanner Omni client using TLS encryption and apply a batch of change stream mutations to a destination database. For high-volume workloads, queue and batch non-overlapping mutations in commit-timestamp order across parallel worker processes rather than committing one record at a time:
    
    
    from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
    from google.cloud.spanner_v1 import [InstanceType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.InstanceType.html)
    
    # Configure the Spanner Omni target client
    omni_client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)(
        client_options={"api_endpoint": "ENDPOINT"},
        instance_type=[InstanceType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.InstanceType.html).OMNI,
        ca_certificate="PATH_TO_CA_CERT",
    )
    # Spanner Omni uses "default" as the instance ID
    omni_instance = omni_client.[instance](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_instance)("default")
    omni_database = omni_instance.database("DATABASE_ID")
    
    
    def apply_cdc_mutations_to_omni(records):
        """Applies a batch of ordered change stream records to Spanner Omni."""
    
        def write_batch(transaction):
            for record in records:
                table_name = record["tableName"]
                mutation_type = record["mutationType"]  # INSERT, UPDATE, DELETE
                row_data = record.get("columnValues", {})
    
                if mutation_type in ("INSERT", "UPDATE"):
                    transaction.[insert_or_update](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction.html#google_cloud_spanner_v1_transaction_Transaction_insert_or_update)(
                        table=table_name,
                        columns=list(row_data.keys()),
                        values=[list(row_data.values())],
                    )
                elif mutation_type == "DELETE":
                    key_columns = record["keyValues"]
                    transaction.delete(
                        table=table_name,
                        keyset=[spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[KeySet](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.keyset.KeySet.html)(keys=[list(key_columns.values())]),
                    )
    
        omni_database.run_in_transaction(write_batch)
    

Replace the following:

  * `ENDPOINT`: the private gRPC endpoint and port of your Spanner Omni instance, for example, `spanner-omni.internal.example.com:15000`.
  * `PATH_TO_CA_CERT`: the file path to the certificate authority (CA) certificate for your Spanner Omni deployment.
  * `DATABASE_ID`: the ID of your destination Spanner Omni database.



For more information about configuring client connections, see [Use the Python client library to connect to Spanner Omni](https://docs.cloud.google.com/spanner-omni/python).

## Accelerate replication with Cross-Cloud Interconnect

Relying on the public internet or IPsec VPN tunnels between Google Cloud and another cloud provider can introduce network jitter, packet loss, bandwidth limits, and variable replication lag. For production workloads that require a low RPO, use [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) to establish dedicated, high-speed physical connectivity between Google Cloud and your external cloud provider.

The following table compares network characteristics between public internet or IPsec VPN connections and Cross-Cloud Interconnect.

Comparison of network transit options for cross-cloud replication  Network metric | Public internet or IPsec VPN | Cross-Cloud Interconnect  
---|---|---  
Link capacity |  1.25 Gbps to 3 Gbps per tunnel. |  10 Gbps or 100 Gbps dedicated optical bandwidth per link.  
Network latency and jitter |  Variable and unpredictable internet transit paths. |  Deterministic, low-latency private routing.  
Availability SLA |  No end-to-end performance SLA. |  99.9% or 99.99% availability SLA when configured with redundant connections.   
Data transfer encryption |  IPsec overhead and software cryptography limits. |  Line-rate MACsec for Cloud Interconnect (IEEE 802.1AE) encryption. For more information, see [MACsec for Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview).   
Data transfer costs |  Standard internet egress rates. |  Reduced Cloud Interconnect data transfer rates.  
  
### High-level network configuration workflow

To set up Cross-Cloud Interconnect for your replication pipeline, complete these high-level steps:

  1. **Order Cross-Cloud Interconnect connections** : Order primary and redundant Cross-Cloud Interconnect ports in a colocation facility that pairs with your remote cloud provider location. For example, run the [`gcloud compute interconnects create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/create) command:
         
         gcloud compute interconnects create CONNECTION_NAME \
           --interconnect-type=DEDICATED \
           --link-type=CAPACITY \
           --requested-link-count=LINK_COUNT \
           --location=GOOGLE_CLOUD_LOCATION \
           --remote-location=REMOTE_LOCATION \
           --noc-contact-email=CONTACT_EMAIL
         

Replace the following:

     * `CONNECTION_NAME`: the name of your Cross-Cloud Interconnect connection.
     * `CAPACITY`: the link capacity, such as `LINK_TYPE_ETHERNET_10G_LR` or `LINK_TYPE_ETHERNET_100G_LR`.
     * `LINK_COUNT`: the number of links to request.
     * `GOOGLE_CLOUD_LOCATION`: the edge availability domain for the Google Cloud location, for example, `iad-zone1-1`.
     * `REMOTE_LOCATION`: the remote cloud provider location, for example, `aws-us-east-1`.
     * `CONTACT_EMAIL`: your network operations email address.

For more information, see [Choose your locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/choose-locations) and [Order your AWS ports](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/order-aws-ports).

  2. **Configure Cloud Router and BGP peering** : Create VLAN attachments and configure Border Gateway Protocol (BGP) sessions between Cloud Router in your Google Cloud VPC network and the virtual private gateway or direct connect gateway in your remote cloud environment. For more information, see [Cloud Router overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview), [Configure your Google Cloud resources](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources), and [Configure your AWS resources](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-aws).

  3. **Validate route propagation** : Verify that route tables in both networks propagate non-overlapping CIDR blocks so that your CDC pipeline workers and Spanner Omni nodes communicate exclusively over private IP addresses. For more information, see [Verify your connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/test-connections).




For complete setup instructions, see [Connect to Amazon Web Services](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/connectivity-overview) in the Cross-Cloud Interconnect documentation.

## Failover and runbook checklist

When you execute a switchover or failover from Spanner on Google Cloud to Spanner Omni, follow these operational steps:

  1. **Drain in-flight changes** : Stop application writes to the primary Spanner database (if reachable) and verify that your CDC replication pipeline has processed all change stream records up to the latest commit timestamp.
  2. **Redirect application connections** : Update your application configuration profiles, connection strings, or Kubernetes secrets to connect to your Spanner Omni endpoints instead of Spanner on Google Cloud.
  3. **Update DNS and traffic routing** : Switch your DNS records or global load balancer targets to route client traffic to the application tier and load balancers fronting your Spanner Omni deployment.
  4. **Resynchronize after recovery** : After you restore the primary Google Cloud environment, reverse the replication direction before you fail back. You capture changes from Spanner Omni by using a change stream and the [Debezium connector](https://docs.cloud.google.com/spanner-omni/debezium) to publish changes to Apache Kafka, with a consumer that applies them to Spanner. Alternatively, you can export your Spanner Omni database to Avro files in Cloud Storage and import them into Spanner. For more information, see [Import and export data](https://docs.cloud.google.com/spanner-omni/import-export-data) and [Import Spanner Avro files](https://docs.cloud.google.com/spanner/docs/import).



## What's next

  * [Create and manage Spanner Omni backups](https://docs.cloud.google.com/spanner-omni/backups)
  * [Restore a Spanner Omni backup](https://docs.cloud.google.com/spanner-omni/restores)
  * [Import and export data](https://docs.cloud.google.com/spanner-omni/import-export-data)
  * [Use Apache Beam and SpannerIO to connect to Spanner Omni](https://docs.cloud.google.com/spanner-omni/beam)
  * [Use Debezium to connect to Spanner Omni](https://docs.cloud.google.com/spanner-omni/debezium)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
