---
url: https://docs.cloud.google.com/memorystore/docs/cluster/use-shared-ca/
title: Secure your data by using a shared Certificate Authority (CA) \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:08.578561+00:00
---

# Secure your data by using a shared Certificate Authority (CA)  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/use-shared-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Secure your data by using a shared Certificate Authority (CA) Stay organized with collections  Save and categorize content based on your preferences. 

You can encrypt all data that moves between your client applications and Memorystore for Redis Cluster securely. This is _in-transit encryption_. By using in-transit encryption, all Redis traffic is encrypted through the [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security) protocol. This ensures that all data that moves between your applications and Memorystore for Redis Cluster remains confidential and untampered.

When in-transit encryption is enabled, Redis clients communicate exclusively across a secure connection. Redis clients that aren't configured for TLS are blocked. If you choose to use in-transit encryption, then you're responsible for ensuring that your Redis client can use the TLS protocol.

Clusters that use in-transit encryption have Certificate Authorities (CAs). You use the CAs to authenticate the certificates of the machines in your clusters.

One CA mode that you can use is a shared CA. A shared CA is a managed, regionalized CA infrastructure. For each region, you can download a single CA certificate bundle. This bundle is valid for all clusters located in a region that you configure to use the shared CA. Using a shared CA reduces the number of certificates that your clients need to manage.

**Important** : Existing CA certificate bundles are valid until their expiration dates. Before these bundles expire, new bundles are available for you to download and install onto your clients that connect to a cluster in Memorystore for Redis Cluster. After the bundles expire, you can uninstall them from your clients.

For clusters that have replicas, replicated data is encrypted fully at the network level, based on Google Cloud encryption standards. Also, Memorystore for Redis Cluster supports the TLS protocol, versions 1.2 and later.

## Create a cluster that uses a shared CA

**Important:** Before you create a cluster, you must have a [service connection policy](https://docs.cloud.google.com/memorystore/docs/cluster/networking) established for your network. When you use a shared CA for this cluster, you can't change the CA mode. Also, you can't deactivate in-transit encryption for clusters that you create in this way.

### Console

Follow the steps at [Create instances](https://docs.cloud.google.com/memorystore/docs/cluster/create-manage-instances).

### gcloud

To create a cluster that uses a shared CA, use the [`gcloud redis clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/create) command.
    
    
    gcloud redis clusters create CLUSTER_ID \
    --region=REGION_ID \
    --network=NETWORK \
    --replica-count=REPLICA_COUNT \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT \
    --transit-encryption-mode=server-authentication \
    --server-ca-mode=google-managed-shared-ca
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster that you're creating. The cluster ID must be 1 to 63 characters, and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter, and end with a lowercase letter or number.

  * REGION_ID: the region where you want the cluster to be located.

  * NETWORK: the network that you use to create the cluster. It must use this format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID that you use must match the network ID that the service connection policy uses. Otherwise, you can't create the cluster.

  * REPLICA_COUNT: the number of replicas (per shard). Accepted values are `0`-`5`.

  * NODE_TYPE: the node type. Accepted values are:

    * `redis-shared-core-nano`
    * `redis-standard-small`
    * `redis-highmem-medium`
    * `redis-highmem-xlarge`
**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type. For more information about these node types, see [Choose a node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type).
  * SHARD_COUNT: the number of shards in the cluster. The shard count determines the total memory capacity for storing cluster data. For more information about cluster specifications, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).




The `server-ca-mode` parameter represents the CA mode for the cluster. For a shared CA, `google-managed-shared-ca` is the value for the parameter. If you don't use this parameter, then the default CA mode is per-instance.

For example:
    
    
    gcloud redis clusters create my-cluster \
    --region=us-central1 \
    --network=projects/my-network-project/global/networks/default \
    --replica-count=1 \
    --node-type=redis-highmem-medium \
    --shard-count=3 \
    --transit-encryption-mode=server-authentication \
    --server-ca-mode=google-managed-shared-ca
    

## Download the CA certificate bundle

To view the CA certificate bundle and install the CA certificates onto your client application, use the `get-shared-regional-certificate-authority` command.
    
    
    gcloud redis clusters get-shared-regional-certificate-authority
    --region=REGION_ID
    

Replace REGION_ID with the region where the cluster is located.

### Download regional CA certificate bundles for a shared CA

You can use the following table to download the regional CA certificate bundles.

**Important:** These certificate bundles don't apply to clusters that use the [per-instance](https://docs.cloud.google.com/memorystore/docs/cluster/manage-in-transit-encryption) or [customer-managed](https://docs.cloud.google.com/memorystore/docs/cluster/use-customer-managed-ca) CA modes.**Region name** | **Location** | **Certificate bundle**  
---|---|---  
Global | All locations | [global.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/global/all_ca_bundle.pem)  
`africa-south1` | Johannesburg | [africa-south1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/africa-south1/ca_bundle.pem)  
`asia-east1` | Taiwan | [asia-east1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/asia-east1/ca_bundle.pem)  
`asia-east2` | Hong Kong | [asia-east2.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/asia-east2/ca_bundle.pem)  
`asia-northeast1` | Tokyo | [asia-northeast1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/asia-northeast1/ca_bundle.pem)  
`asia-northeast2` | Osaka | [asia-northeast2.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/asia-northeast2/ca_bundle.pem)  
`asia-northeast3` | Seoul | [asia-northeast3.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/asia-northeast3/ca_bundle.pem)  
`asia-south1` | Mumbai | [asia-south1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/asia-south1/ca_bundle.pem)  
`asia-south2` | Delhi | [asia-south2.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/asia-south2/ca_bundle.pem)  
`asia-southeast1` | Singapore | [asia-southeast1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/asia-southeast1/ca_bundle.pem)  
`asia-southeast2` | Jakarta | [asia-southeast2.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/asia-southeast2/ca_bundle.pem)  
`australia-southeast1` | Sydney | [australia-southeast1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/australia-southeast1/ca_bundle.pem)  
`australia-southeast2` | Melbourne | [australia-southeast2.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/australia-southeast2/ca_bundle.pem)  
`europe-central2` | Warsaw | [europe-central2.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-central2/ca_bundle.pem)  
`europe-north1` | Finland | [europe-north1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-north1/ca_bundle.pem)  
`europe-north2` | Stockholm | [europe-north2.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-north2/ca_bundle.pem)  
`europe-southwest1` | Madrid | [europe-southwest1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-southwest1/ca_bundle.pem)  
`europe-west1` | Belgium | [europe-west1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-west1/ca_bundle.pem)  
`europe-west2` | London | [europe-west2.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-west2/ca_bundle.pem)  
`europe-west3` | Frankfurt | [europe-west3.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-west3/ca_bundle.pem)  
`europe-west4` | Netherlands | [europe-west4.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-west4/ca_bundle.pem)  
`europe-west6` | Zurich | [europe-west6.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-west6/ca_bundle.pem)  
`europe-west8` | Milan | [europe-west8.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-west8/ca_bundle.pem)  
`europe-west9` | Paris | [europe-west9.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-west9/ca_bundle.pem)  
`europe-west10` | Berlin | [europe-west10.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-west10/ca_bundle.pem)  
`europe-west12` | Turin | [europe-west12.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/europe-west12/ca_bundle.pem)  
`me-central1` | Doha | [me-central1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/me-central1/ca_bundle.pem)  
`me-central2` | Dammam | [me-central2.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/me-central2/ca_bundle.pem)  
`me-west1` | Tel Aviv | [me-west1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/me-west1/ca_bundle.pem)  
`northamerica-northeast1` | Montréal | [northamerica-northeast1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/northamerica-northeast1/ca_bundle.pem)  
`northamerica-northeast2` | Toronto | [northamerica-northeast2.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/northamerica-northeast2/ca_bundle.pem)  
`northamerica-south1` | Mexico | [northamerica-south1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/northamerica-south1/ca_bundle.pem)  
`southamerica-east1` | São Paulo | [southamerica-east1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/southamerica-east1/ca_bundle.pem)  
`southamerica-west1` | Santiago | [southamerica-west1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/southamerica-west1/ca_bundle.pem)  
`us-central1` | Iowa | [us-central1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/us-central1/ca_bundle.pem)  
`us-east1` | South Carolina | [us-east1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/us-east1/ca_bundle.pem)  
`us-east4` | Northern Virginia | [us-east4.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/us-east4/ca_bundle.pem)  
`us-east5` | Columbus | [us-east5.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/us-east5/ca_bundle.pem)  
`us-south1` | Dallas | [us-south1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/us-south1/ca_bundle.pem)  
`us-west1` | Oregon | [us-west1.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/us-west1/ca_bundle.pem)  
`us-west2` | Los Angeles | [us-west2.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/us-west2/ca_bundle.pem)  
`us-west3` | Salt Lake City | [us-west3.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/us-west3/ca_bundle.pem)  
`us-west4` | Las Vegas | [us-west4.pem](https://storage.googleapis.com/redis-cluster-ca-bundles-prod/prod/regions/us-west4/ca_bundle.pem)  
  
## Install the CA certificate bundle on the client

You must install the CA certificate bundle on the client that connects to the cluster. Depending on the type of client, the CA certificate installation might vary.

To install a bundle on a Compute Engine Linux VM, do the following:

  1. Use SSH to connect to a Compute Engine Linux client.

  2. In the client, use the following command to create a `server_ca.pem` file:
         
         sudo vim /tmp/server_ca.pem
         

  3. Download the CA certificate bundle and paste the certificates into the `server_ca.pem` file.

You must format the text of the CAs correctly. The `server_ca.pem` file might appear, as follows:
         
         -----BEGIN CERTIFICATE-----
         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
         yWsYzii85XgHEw==
         -----END CERTIFICATE-----
         -----BEGIN CERTIFICATE-----
         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
         dDU7oqWT1NWpGv4mQ1vAWWtG
         -----END CERTIFICATE-----
         -----BEGIN CERTIFICATE-----
         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
         m5BSICd0
         -----END CERTIFICATE-----
         -----BEGIN CERTIFICATE-----
         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
         +e62i+/psNOyBpZdIRCS
         -----END CERTIFICATE-----
         

To format the text in the file correctly, use the following guidelines:

     * Copy the entire CA certificate bundle, including the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines.

     * Make sure that the text of the certificates is completely left justified. Verify that no spaces appear in front of any line of the certificates.

     * Add each CA certificate on a new line. Verify that no blank lines exist between certificates.




## Configure the client for in-transit encryption

The client that you use to connect to the cluster must either support TLS or use a third-party sidecar to enable TLS.

If your client supports TLS, then configure it to point to the cluster's IP address, port 6379, and the file containing the CA certificate bundle. You can see an example of how to connect to a [cluster](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance#connect_to_an_in_transit_encryption_enabled_instance) that has in-transit encryption enabled.

## Manage the CA rotation

We recommend that you install all downloadable CA certificate bundles on the clients that access the cluster.

Installing the latest CA certificate bundles periodically ensures that you have the necessary CA certificates when Memorystore for Redis Cluster rotates the CAs. During this rotation, both the existing CAs and new CAs are active.

## Code sample to connect to a cluster that uses in-transit encryption

To view a code sample on how to set up a client library to connect to a cluster that uses in-transit encryption, see [In-transit encryption client library code sample](https://docs.cloud.google.com/memorystore/docs/cluster/client-library-connection#in-transit_encryption_client_library_code_sample).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
