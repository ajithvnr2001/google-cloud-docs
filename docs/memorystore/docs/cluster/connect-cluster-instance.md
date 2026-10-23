---
url: https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance/
title: Connect to a Memorystore for Redis Cluster instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:23.369913+00:00
---

# Connect to a Memorystore for Redis Cluster instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Connect to a Memorystore for Redis Cluster instance Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect to a Memorystore for Redis Cluster instance.

## Client support

Memorystore for Redis Cluster does not provide its own client libraries, but rather supports existing third-party client libraries that support the Redis protocol. For more information about the client libraries that Redis supports, see [Supported connection clients](https://redis.io/docs/latest/operate/rs/databases/connect/supported-clients-browsers/).

### Redis-py client best practice

To connect to your Memorystore for Redis Cluster instance using the [redis-py](https://github.com/redis/) Python client, you must add the `skip_full_coverage_check=True` when declaring a Redis Cluster:
    
    
    from rediscluster import RedisCluster
    endpoints = [{"host": "IPADDRESS", "port": "6379"}]
    
    rdb = RedisCluster(
        startup_nodes=endpoints,
        skip_full_coverage_check=True, # Required for Memorystore
        decode_responses = True)
    
    print(rdb.set('PYTHON', 'CLUSTER'))
    print(rdb.get('PYTHON'))
    print(rdb.unlink('PYTHON'))
    

## Allow ports on your firewall

If you don't allow the correct ports on your firewall, then your cluster might encounter connection errors because the firewall might block the ports that Memorystore for Redis Cluster uses.

For all of your cluster's Private Service Connect endpoints, you must allow TCP port 6379, as well as TCP ports 11000 through 13047. For more information, see [Troubleshoot issues](https://docs.cloud.google.com/memorystore/docs/cluster/troubleshoot-issues#connection_error_caused_by_firewall_rules).

## Cross region access

You can access a Memorystore for Redis Cluster instance from a client located in a different region than where the Memorystore instance is located.

## View your cluster's discovery endpoint

Each cluster has a [discovery endpoint](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#discovery_endpoint) to which your client connects. This endpoint is a combination of an IP address and a port number.

You can view the discovery endpoint of a cluster in Memorystore for Redis Cluster by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important:** In addition to the discovery endpoint, each cluster has a [data endpoint](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#data_endpoint). This endpoint is reserved for Memorystore for Redis Cluster to use to connect your client to nodes in the cluster. Therefore, don't connect to this endpoint directly.

### Console

  1. Go to the **Memorystore for Redis Cluster** page in the Google Cloud console.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click your Cluster ID.

  3. In the **Connect to this instance** section, take a note of the IP address and port number next to **Discovery Endpoint**. These two values used together are your cluster's discovery endpoint.




### gcloud

To view your cluster's discovery endpoint, run the `describe` gcloud CLI as explained in the [view instance details](https://docs.cloud.google.com/memorystore/docs/cluster/create-manage-instances#view_instance_details) section.

The output should be similar to the following:
    
    
    authorizationMode: AUTH_MODE_DISABLED
    createTime: '2023-08-04T17:49:07.988918793Z'
    discoveryEndpoints:
    - address: 10.142.0.13
      port: 6379
      pscConfig:
      - network: projects/my-project-364018/global/networks/default
    name: projects/my-project-364018/locations/us-east1/clusters/my-cluster-1
    pscConnections:
    - address: 10.142.0.13
      forwardingRule: https://www.googleapis.com/compute/v1/projects/my-project-364018/regions/us-east1/forwardingRules/sca-auto-fr-5bc46f69-ec80-4c5a-8971-ce267a4d8ddd
      network: projects/my-project-364018/global/networks/default
      projectId: my-project-364018
      pscConnectionId: '25734306048376845'
    - address: 10.142.0.10
      forwardingRule: https://www.googleapis.com/compute/v1/projects/my-project-364018/regions/us-east1/.
      forwardingRules/sca-auto-fr-817b64c5-85ac-48d0-82e3-c6fa99b4e67d
      network: projects/my-project-364018/global/networks/default
      projectId: my-project-364018
      pscConnectionId: '25734306048376842'
    replicaCount: 0
    shardCount: 3
    sizeGb: 39
    state: ACTIVE
    tier: PERFORMANCE
    transitEncryptionMode: TRANSIT_ENCRYPTION_MODE_DISABLED
    uid: cddda5de-d91f-449b-8755-3a665430271a
    

Take a note of the endpoint address and port number listed in the `discovery_endpoints:` section. These two values used together are your cluster's discovery endpoint.

## Connect from a Compute Engine VM using redis-cli

You can connect to the Memorystore for Redis Cluster instance from any Compute Engine VM that uses the Memorystore instance's authorized network.

To connect to the instance:

  1. If you don't already have a Linux Compute Engine VM that uses the authorized network for your Memorystore for Redis Cluster instance, create one and connect to it by following [Quickstart to create a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

  2. Install `redis-cli` version 6.0 or newer on the Compute Engine VM by following the instructions at [Install Redis on Linux](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-linux/).

  3. [View your cluster's discovery endpoint](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance#view_your_clusters_discovery_endpoint) and make a note of it.

  4. Connect to your instance's discovery endpoint by running the following command:
         
         redis-cli -h DISCOVERY_ENDPOINT_ADDRESS -p PORT_NUMBER -c
         

Where:

     * DISCOVERY_ENDPOINT_ADDRESS and PORT_NUMBER are the values you noted in the previous step.
**Note:** The `-c` switch is used to enable the `redis-cli` cluster support mode. If the `-c` switch is not provided, when you try to access keys from a different shard than the one you are connected to, it results in a `MOVED` error. In the cluster support mode the client is automatically reconnected to the address returned in the error response. For more details, see [Using Redis-CLI with a Redis Cluster](https://developer.redis.com/operate/redis-at-scale/scalability/redis-cli-with-redis-cluster/).
  5. Run the `CLUSTER SHARDS` command to view your cluster topology. Take a note of one of the node's IP addresses and port numbers.

  6. Connect to your desired node by running the following command:
         
         redis-cli -h NODE_IP_ADDRESS -p NODE_PORT -c
         

Replace the following:

     * NODE_IP_ADDRESS is the node's IP address you found in the previous step.
     * NODE_PORT is the node's port number you found in the previous step.
  7. Once connected to the node, enter some Redis commands:

Enter:
         
         PING
         

Result:
         
         PONG
         

Enter
         
         SET HELLO WORLD
         

Result:
         
         OK
         

Enter:
         
         GET HELLO
         

Result:
         
         "WORLD"
         

  8. Once you are done testing your connection to the Redis node, you should consider deleting the Compute Engine VM you used to connect to the Redis instance. Doing so helps you avoid incurring charges to your Cloud Billing account.




## Connect to an in-transit encryption enabled instance

This section provides an example of how to connect to a Memorystore for Redis Cluster instance that has in-transit encryption enabled.

  1. If you don't already have a Compute Engine VM that uses the same authorized network as the Redis instance from the previous step, create one and connect to it by following [Quickstart using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

     1. Install `redis-cli` version 6.0 or newer on the Compute Engine VM by following the instructions at [Install Redis on Linux](https://redis.io/docs/getting-started/installation/install-redis-on-linux/).
  2. Check the [Certificate Authority (CA) mode](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption#certificate-authorities) that you're using for your cluster.

     * If the CA mode [per-instance](https://docs.cloud.google.com/memorystore/docs/cluster/manage-in-transit-encryption), then install your cluster's CA certificates by following the instructions at [Install CA certificates on the client](https://docs.cloud.google.com/memorystore/docs/cluster/manage-in-transit-encryption#install-CA-certificates).

     * If the CA mode is [shared](https://docs.cloud.google.com/memorystore/docs/cluster/use-shared-ca), then install your cluster's CA certificate bundle by following the instructions at [Install the CA certificate bundle on the client](https://docs.cloud.google.com/memorystore/docs/cluster/use-shared-ca#install-CA-certificate-bundle).

     * If the CA mode is [customer-managed](https://docs.cloud.google.com/memorystore/docs/cluster/use-customer-managed-ca), then your applications can connect to the cluster without you having to download and install additional CA certificates. Therefore, you can skip this step.

  3. [View your cluster's discovery endpoint](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance#view_your_clusters_discovery_endpoint) and note the endpoint's IP address and port number.

  4. Connect to your instance's discovery endpoint by running the following command:
         
         redis-cli -h DISCOVERY_ENDPOINT_ADDRESS -p PORT_NUMBER -c --tls --cacert /tmp/server_ca.pem
         

Replace the following:

     * DISCOVERY_ENDPOINT_ADDRESS: the discovery endpoint's IP address that you noted in the previous step
     * PORT_NUMBER: the port number that you noted in the previous step

To enable the `redis-cli` cluster support mode, use the `-c` switch. If you don't provide this switch, then when you try to access keys from a different shard than the one to which you're connected, the cluster returns a `MOVED` error. However, if you use the switch, then the client automatically reconnects to the address that's provided in the error response. For more information, see [Redis Scalability: Clustering, Sharding, and Hash Slots](https://developer.redis.com/operate/redis-at-scale/scalability/redis-cli-with-redis-cluster/).

If you enable either Identity and Access Management (IAM) authentication or basic token-based authentication on the cluster, then you must provide authentication credentials alongside the Transport Layer Security (TLS) flags. For example:
    
    redis-cli -h DISCOVERY_ENDPOINT_ADDRESS -p PORT_NUMBER -c --tls --cacert /tmp/server_ca.pem --user USERNAME -a TOKEN
    

Replace the following:

     * USERNAME: the username of the cluster
     * TOKEN: the authentication token

For more information about generating or managing your authentication credentials, see [Manage IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth) and [Secure access to your clusters by using basic token-based authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-basic-auth).

  5. Run the `CLUSTER SHARDS` command to view your cluster topology. Note the IP address and port number of one of the nodes.

  6. Connect to your node by running the following command:
         
         redis-cli -h NODE_IP_ADDRESS -p NODE_PORT -c --tls --cacert /tmp/server_ca.pem
         

Replace the following:

     * NODE_IP_ADDRESS: the node's IP address that you noted in the previous step
     * NODE_PORT: the node's port number that you noted in the previous step

If your cluster uses IAM or basic token-based authentication, then make sure that you include the `--user` and `-a` flags, as you did in the discovery endpoint step.

  7. Once connected to the node, enter some Redis commands:

Enter:
         
         PING
         

Result:
         
         PONG
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
