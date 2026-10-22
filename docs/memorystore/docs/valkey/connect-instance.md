---
url: https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance/
title: Connect to a Memorystore for Valkey instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:41.287663+00:00
---

# Connect to a Memorystore for Valkey instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Connect to a Memorystore for Valkey instance Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect to a Memorystore for Valkey instance.

## Client support

For examples and guidance on which connecting clients to use, see [Client library code samples](https://docs.cloud.google.com/memorystore/docs/valkey/client-library-code-samples).

## Allow ports on your firewall

If you don't allow the correct ports on your firewall, then your instance might encounter connection errors because the firewall might block the ports that Memorystore for Valkey uses.

For all of your instance's Private Service Connect endpoints, you must allow TCP port 6379, as well as TCP ports 11000 through 13047. For more information, see [Troubleshoot issues](https://docs.cloud.google.com/memorystore/docs/valkey/troubleshoot-issues#connection_error_caused_by_firewall_rules).

## Cross region access

You can access a Memorystore for Valkey instance from a client located in a different region than where the instance is located.

## Connect to a Cluster Mode Enabled instance

This section explains how to connect to a Memorystore for Valkey Cluster Mode Enabled instance.

### View your instance's discovery endpoint

Each Cluster Mode Enabled instance has a [discovery endpoint](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#discovery_endpoint) to which your client connects. This endpoint is a combination of an IP address and a port number.

You can view the discovery endpoint of a Memorystore for Valkey instance by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important:** In addition to the discovery endpoint, each Cluster Mode Enabled instance has a [data endpoint](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#data_endpoint). This endpoint is reserved for Memorystore for Valkey to use to connect your client to nodes in the instance. Therefore, don't connect to this endpoint directly.

### gcloud

To view your instance's discovery endpoint, run the `describe` gcloud CLI as explained in [view instance information](https://docs.cloud.google.com/memorystore/docs/valkey/view-instance-information).

The output should be similar to the following:
    
    
    authorizationMode: AUTH_DISABLED
    createTime: '2024-08-06T22:02:55.224704101Z'
    deletionProtectionEnabled: false
    engineVersion: VALKEY_7_2
    name: projects/myproject/locations/us-central1/instances/my-instance
    nodeConfig:
      sizeGb: 6.5
    nodeType: STANDARD_SMALL
    persistenceConfig:
      mode: DISABLED
    endpoints:
    - connections:
      - pscAutoConnection:
           connectionType: CONNECTION_TYPE_DISCOVERY
           forwardingRule: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/forwardingRules/sca-auto-fr-ec00907a-3ee3-4740-8092-ae832428f8e4
           ipAddress: 10.128.0.58
           network: projects/my-project/global/networks/default
           port: 6379
           projectId: my-project
           pscConnectionId: '38876592440606778'
           serviceAttachment: projects/129109085717/regions/us-east1/serviceAttachments/gcp-memorystore-auto-58e78f71-fdb7-48-psc-sa
        - pscAutoConnection:
           forwardingRule: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/forwardingRules/sca-auto-fr-5ce5518f-1c59-4b46-aa74-799fad70d7b1
           ipAddress: 10.128.0.59
           network: projects/my-project/global/networks/default
           port: 6379
           projectId: my-project
           pscConnectionId: '38876592440606779'
           serviceAttachment: projects/129109085717/regions/us-east1/serviceAttachments/gcp-memorystore-auto-58e78f71-fdb7-48-psc-sa-2
    replicaCount: 2
    shardCount: 5
    state: ACTIVE
    transitEncryptionMode: TRANSIT_ENCRYPTION_DISABLED
    uid: 869f2d09-d20b-46d8-94ba-be83c48ceb54
    updateTime: '2024-08-06T22:18:59.389980051Z'
    zoneDistributionConfig:
      mode: MULTI_ZONE
    

Take a note of the endpoint address and port number listed in the `endpoints:` section for the `connectionType: CONNECTION_TYPE_DISCOVERY` entry. These two values used together are your instance's discovery endpoint.

### Connect from a Compute Engine VM using valkey-cli

You can connect to the Memorystore for Valkey instance from any Compute Engine VM that uses the Memorystore instance's authorized network.

To connect to the instance:

  1. If you don't already have a Linux Compute Engine VM that uses the authorized network for your Memorystore for Valkey instance, create one and connect to it by following [Quickstart to create a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

  2. Install `valkey-cli` on the Compute Engine VM by following the instructions at [Install Valkey](https://valkey.io/topics/installation/).

  3. [View your instance's discovery endpoint](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance#view_your_instances_discovery_endpoint) and make a note of it.

  4. Connect to your instance's discovery endpoint by running the following command:
         
         valkey-cli -h DISCOVERY_ENDPOINT_ADDRESS -p PORT_NUMBER -c
         

Where:

     * DISCOVERY_ENDPOINT_ADDRESS and PORT_NUMBER are the values you noted in the previous step.
**Note:** The `-c` switch is used to enable the `valkey-cli` cluster support mode. If the `-c` switch is not provided, when you try to access keys from a different shard than the one you are connected to, it results in a `MOVED` error. In the cluster support mode the client is automatically reconnected to the address returned in the error response.
  5. Run the `CLUSTER SHARDS` command to view your node topology. Take a note of one of the node's IP addresses and port numbers.

  6. Connect to your desired node by running the following command:
         
         valkey-cli -h NODE_IP_ADDRESS -p NODE_PORT -c
         

Replace the following:

     * NODE_IP_ADDRESS is the node's IP address you found in the previous step.
     * NODE_PORT is the node's port number you found in the previous step.
  7. Once connected to the node, enter some Valkey commands:

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
         

  8. Once you are done testing your connection to the Valkey node, you should consider deleting the Compute Engine VM you used to connect to the Valkey instance. Doing so helps you avoid incurring charges to your Cloud Billing account.




### Connect to an in-transit encryption enabled instance

This section provides an example of how to connect to a Memorystore for Valkey Cluster Mode Enabled instance that has in-transit encryption enabled.

  1. If you don't already have a Compute Engine VM that uses the same authorized network as the Valkey instance from the previous step, create one and connect to it by following [Quickstart using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

     1. Install `valkey-cli` version 6.0 or newer on the Compute Engine VM by following the instructions at [Install Valkey](https://valkey.io/topics/installation/).
  2. Install your instance's certificate authority (CA) certificates on the Linux VM by following the instructions at [Install CA certificates on the client](https://docs.cloud.google.com/memorystore/docs/valkey/manage-in-transit-encryption#install-CA-certificates).

  3. [View your instance's discovery endpoint](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance#view_your_instances_discovery_endpoint) and note the endpoint's IP address and port number.

  4. Connect to your instance's discovery endpoint by running the following command:
         
         valkey-cli -h DISCOVERY_ENDPOINT_ADDRESS -p PORT_NUMBER -c --tls --cacert /tmp/server_ca.pem
         

Replace the following:

     * DISCOVERY_ENDPOINT_ADDRESS: the discovery endpoint's IP address that you noted in the previous step
     * PORT_NUMBER: the port number that you noted in the previous step

To enable the `valkey-cli` support mode, use the `-c` switch. If you don't provide this switch, then when you try to access keys from a different shard than the one to which you're connected, the instance returns a `MOVED` error. However, if you use the switch, then the client automatically reconnects to the address that's provided in the error response.

If you enable either Identity and Access Management (IAM) authentication or basic token-based authentication on the instance, then you must provide authentication credentials alongside the Transport Layer Security (TLS) flags. For example:
    
    valkey-cli -h DISCOVERY_ENDPOINT_ADDRESS -p PORT_NUMBER -c --tls --cacert /tmp/server_ca.pem --user USERNAME -a TOKEN
    

Replace the following:

     * USERNAME: the username of the instance
     * TOKEN: the authentication token

For more information about generating or managing your authentication credentials, see [Manage IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/manage-iam-auth) and [Secure access to your instances by using basic token-based authentication](https://docs.cloud.google.com/memorystore/docs/valkey/manage-basic-auth).

  5. Run the `CLUSTER SHARDS` command to view your node topology. Note the IP address and port number of one of the nodes.

  6. Connect to your node by running the following command:
         
         valkey-cli -h NODE_IP_ADDRESS -p NODE_PORT -c --tls --cacert /tmp/server_ca.pem
         

Replace the following:

     * NODE_IP_ADDRESS: the node's IP address that you noted in the previous step.
     * NODE_PORT: the node's port number that you noted in the previous step.

If your cluster uses IAM or basic token-based authentication, then make sure that you include the `--user` and `-a` flags, as you did in the discovery endpoint step.

  7. After you connect to the node, enter the following Valkey commands:

Enter:
         
         PING
         

Result:
         
         PONG
         




## Connect to a Cluster Mode Disabled instance

This section explains how to connect to a Memorystore for Valkey Cluster Mode Disabled instance.

### View your instance's primary and reader endpoint

To view your instance's [primary and reader endpoint endpoint](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#cluster_mode_disabled_instance), use the following instructions:

### gcloud

To view your instance's primary and reader endpoint endpoint, run the `describe` gcloud CLI, as explained in [view instance information](https://docs.cloud.google.com/memorystore/docs/valkey/view-instance-information).

The output should be similar to the following:
    
    
    authorizationMode: AUTH_DISABLED
    createTime: '2024-08-06T22:02:55.224704101Z'
    deletionProtectionEnabled: false
    engineVersion: VALKEY_7_2
    name: projects/myproject/locations/us-central1/instances/my-instance
    nodeConfig:
      sizeGb: 6.5
    nodeType: STANDARD_SMALL
    persistenceConfig:
      mode: DISABLED
    endpoints:
    - connections:
      - pscAutoConnection:
          connectionType: CONNECTION_TYPE_PRIMARY
          forwardingRule: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/forwardingRules/sca-auto-fr-ec00907a-3ee3-4740-8092-ae832428f8e4
          ipAddress: 10.128.0.124
          network: projects/my-project/global/networks/default
          port: 6379
          projectId: my-project
          pscConnectionId: '38876592440606778'
          serviceAttachment: projects/448055306617/regions/us-central1/serviceAttachments/gcp-memorystore-auto-b3c43536-4a77-40-psc-sa
      - pscAutoConnection:
          connectionType: CONNECTION_TYPE_READER
          forwardingRule: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/forwardingRules/sca-auto-fr-5ce5518f-1c59-4b46-aa74-799fad70d7b1
          ipAddress: 10.128.0.125
          network: projects/my-project/global/networks/default
          port: 6379
          projectId: my-project
          pscConnectionId: '38876592440606779'
          serviceAttachment: projects/448055306617/regions/us-central1/serviceAttachments/gcp-memorystore-auto-b3c43536-4a77-40-psc-sa-2
    replicaCount: 2
    shardCount: 1
    mode: CLUSTER_DISABLED
    state: ACTIVE
    transitEncryptionMode: TRANSIT_ENCRYPTION_DISABLED
    uid: 869f2d09-d20b-46d8-94ba-be83c48ceb54
    updateTime: '2024-08-06T22:18:59.389980051Z'
    zoneDistributionConfig:
      mode: MULTI_ZONE
    

**Primary endpoint:** Take a note of the endpoint address and port number listed under `CONNECTION_TYPE_PRIMARY` in the `endpoints:` section. These two values used together are your instance's primary endpoint.

**Reader endpoint:** Take a note of the endpoint address and port number listed under `CONNECTION_TYPE_READER` in the `endpoints:` section. These two values used together are your instance's reader endpoint.

### Connect from a Compute Engine VM using valkey-cli

You can connect to the Memorystore for Valkey instance from any Compute Engine VM that uses the Memorystore instance's authorized network.

To connect to the instance:

  1. If you don't already have a Linux Compute Engine VM that uses the authorized network for your Memorystore for Valkey instance, create one and connect to it by following [Quickstart to create a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

  2. Install `valkey-cli` on the Compute Engine VM by following the instructions at [Install Valkey](https://valkey.io/topics/installation/).

  3. [View your instance's primary and reader endpoint](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance#view_your_instances_primary_and_reader_endpoint) and make a note of it.

  4. Connect to your instance's primary endpoint by running the following command:
         
         valkey-cli -h PRIMARY_ENDPOINT_ADDRESS -p PORT_NUMBER
         

Where:

     * PRIMARY_ENDPOINT_ADDRESS and PORT_NUMBER are the values you noted in the previous step.
  5. After you connect to the primary node, enter the following Valkey commands:

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
         

  6. Connect to your instance's reader endpoint by running the following command:
         
         valkey-cli -h READER_ENDPOINT_ADDRESS -p PORT_NUMBER
         

Where:

     * READER_ENDPOINT_ADDRESS and PORT_NUMBER are the values you noted in the previous step.
  7. After you connect to the primary node, enter the following Valkey Get commands:

Enter:
         
         PING
         

Result:
         
         PONG
         

Enter:
         
         GET HELLO
         

Result:
         
         "WORLD"
         

  8. After you test your connection to the Valkey node, you should delete the Compute Engine VM you used to connect to the Valkey instance. This helps you avoid incurring charges to your Cloud Billing account.




### Connect to an in-transit encryption enabled instance

This section provides an example of how to connect to a Memorystore for Valkey Cluster Mode Disabled instance that has in-transit encryption enabled.

  1. If you don't already have a Compute Engine VM that uses the same authorized network as the Valkey instance from the previous step, create one and connect to it by following [Quickstart using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

     1. Install `valkey-cli` version 6.0 or newer on the Compute Engine VM by following the instructions at [Install Valkey](https://valkey.io/topics/installation/).
  2. Check the [Certificate Authority (CA) mode](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption#certificate-authorities) that you're using for your instance.

     * If the CA mode [per-instance](https://docs.cloud.google.com/memorystore/docs/valkey/manage-in-transit-encryption), then install your instance's CA certificates by following the instructions at [Install CA certificates on the client](https://docs.cloud.google.com/memorystore/docs/valkey/manage-in-transit-encryption#install-CA-certificates).

     * If the CA mode is [shared](https://docs.cloud.google.com/memorystore/docs/valkey/use-shared-ca), then install your instance's CA certificate bundle by following the instructions at [Install the CA certificate bundle on the client](https://docs.cloud.google.com/memorystore/docs/valkey/use-shared-ca#install-CA-certificate-bundle).

     * If the CA mode is [customer-managed](https://docs.cloud.google.com/memorystore/docs/valkey/use-customer-managed-ca), then your applications can connect to the instance without you having to download and install additional CA certificates. Therefore, you can skip this step.

  3. [View your instance's primary and reader endpoints](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance#view_your_instances_primary_and_reader_endpoint) and note the IP address and port number of each endpoint.

  4. Connect to your instance's primary endpoint by running the following command:
         
         valkey-cli -h PRIMARY_ENDPOINT_ADDRESS -p PORT_NUMBER --tls --cacert /tmp/server_ca.pem
         

Replace the following:

     * PRIMARY_ENDPOINT_ADDRESS: the primary endpoint's IP address that you noted in the previous step
     * PORT_NUMBER: the port number for this endpoint that you noted in the previous step
  5. Connect to your instance's reader endpoint by running the following command:
         
         valkey-cli -h READER_ENDPOINT_ADDRESS -p PORT_NUMBER --tls --cacert /tmp/server_ca.pem
         

Replace the following:

     * READER_ENDPOINT_ADDRESS: the reader endpoint's IP address that you noted
     * PORT_NUMBER: the port number for this endpoint that you noted

If you enable either IAM authentication or basic token-based authentication on the instance, then you must provide authentication credentials alongside the TLS flags for both the primary and reader endpoints.

For example:
    
    valkey-cli -h PRIMARY_ENDPOINT_ADDRESS -p PORT_NUMBER --tls --cacert /tmp/server_ca.pem --user USERNAME -a TOKEN
    

and
    
    valkey-cli -h READER_ENDPOINT_ADDRESS -p PORT_NUMBER -c --tls --cacert /tmp/server_ca.pem --user USERNAME -a TOKEN
    

Replace the following:

     * USERNAME: the username of the instance
     * TOKEN: the authentication token

For more information about generating or managing your authentication credentials, see [Manage IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/manage-iam-auth) and [Secure access to your instances by using basic token-based authentication](https://docs.cloud.google.com/memorystore/docs/valkey/manage-basic-auth).

  6. After you connect to the node, enter some Valkey commands:

Enter:
         
         PING
         

Result:
         
         PONG
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
