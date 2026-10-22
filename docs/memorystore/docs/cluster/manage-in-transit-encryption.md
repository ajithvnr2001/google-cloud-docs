---
url: https://docs.cloud.google.com/memorystore/docs/cluster/manage-in-transit-encryption/
title: Secure your data by using a per-instance Certificate Authority (CA) \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:46.908720+00:00
---

# Secure your data by using a per-instance Certificate Authority (CA)  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/manage-in-transit-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Secure your data by using a per-instance Certificate Authority (CA) Stay organized with collections  Save and categorize content based on your preferences. 

You can encrypt all data that moves between your client applications and Memorystore for Redis Cluster securely. This is _in-transit encryption_. By using in-transit encryption, all Redis traffic is encrypted through the [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security) protocol. This ensures that all data that moves between your applications and Memorystore for Redis Cluster remains confidential and untampered.

When in-transit encryption is enabled, Redis clients communicate exclusively across a secure connection. Redis clients that aren't configured for TLS are blocked. If you choose to use in-transit encryption, then you're responsible for ensuring that your Redis client can use the TLS protocol.

Clusters that use in-transit encryption have Certificate Authorities (CAs). You use the CAs to authenticate the certificates of the machines in your clusters.

One CA mode that you can use is a per-instance CA. Memorystore for Redis Cluster provisions each cluster with its own, unique CA infrastructure. To access a cluster securely, you must configure your client application to trust this CA hierarchy. This involves downloading and installing CA certificates on each client that accesses the cluster.

**Important** : CAs are valid for ten years from the date that they're created. New CAs are available for you to download and install on your clients that connect to the cluster about five years before the current CAs expire. Existing CAs are valid until their expiration dates. After the CAs expire, you can uninstall them from your clients.

For clusters that have replicas, replicated data is encrypted fully at the network level, based on Google Cloud encryption standards. Also, Memorystore for Redis Cluster supports the TLS protocol, versions 1.2 and later.

## Create a cluster that uses a per-instance CA

**Important** : Before you create a cluster, you must have a service connection policy established for your network. For more information, see [Networking](https://docs.cloud.google.com/memorystore/docs/cluster/networking). 

Also, when you use a per-instance CA for this cluster, you can't change the CA mode or deactivate in-transit encryption.

### Console

Follow the steps at [Create instances](https://docs.cloud.google.com/memorystore/docs/cluster/create-manage-instances).

### gcloud

To create a cluster that uses a per-instance CA, use the [`gcloud redis clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/create) command.
    
    
    gcloud redis clusters create CLUSTER_ID \
    --region=REGION_ID \
    --network=NETWORK \
    --replica-count=REPLICA_COUNT \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT \
    --transit-encryption-mode=server-authentication \
    --server-ca-mode=google-managed-per-instance-ca
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster that you're creating. The cluster ID must be 1 to 63 characters, and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter, and end with a lowercase letter or number.

  * REGION_ID: the region where you want the cluster to be located.

  * NETWORK: the network that you use to create the cluster. It must use this format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID that you use must match the network ID that the service connection policy uses. Otherwise, you can't create the cluster.

  * REPLICA_COUNT: the number of replicas (per shard). Accepted values are `0`-`5`.

  * NODE_TYPE: the [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) for the cluster.

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  * SHARD_COUNT: the number of shards in the cluster. The shard count determines the total memory capacity for storing cluster data. For more information about cluster specifications, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).




The `server-ca-mode` parameter represents the CA mode for the cluster. For a per-instance CA, `google-managed-per-instance-ca` is the value for the parameter. If you don't use this parameter, then the default CA mode is per-instance.

For example:
    
    
    gcloud redis clusters create my-cluster \
    --region=us-central1 \
    --network=projects/my-network-project/global/networks/default \
    --replica-count=1 \
    --node-type=redis-highmem-medium \
    --shard-count=3 \
    --transit-encryption-mode=server-authentication \
    --server-ca-mode=google-managed-per-instance-ca
    

## Download the CAs

If you enable in-transit encryption for a cluster, then when you use the `get-cluster-certificate-authority` command, the certificates of the CAs appear.
    
    
    gcloud redis clusters get-cluster-certificate-authority CLUSTER_ID
    

Replace CLUSTER_ID with the ID of the cluster.

The response body includes certificates for all applicable CAs.

## Install CA certificates on the client

You must install the CA certificates on the client that connects to the cluster. Depending on the type of client, the CA certificate installation might vary.

To install a CA certificate on a Compute Engine Linux VM, do the following:

  1. Use SSH to connect to a Compute Engine Linux client.

  2. In the client, use the following command to create a `server_ca.pem` file:
         
         sudo vim /tmp/server_ca.pem
         

  3. Download the CAs and paste them into the `server_ca.pem` file.

You must format the text of the CAs correctly. The `server_ca.pem` file might appear, as follows:
         
         -----BEGIN CERTIFICATE-----
         MIIDnTCCAoWgAwIBAgIBADANBgkqhkiG9w0BAQsFADCBhTEtMCsGA1UELhMkNzYx
         NTc4OGMtMTI2Yi00Nzk0LWI2MWMtY2YxOWE2Y2Y1ZjNiMTEwLwYDVQQDEyhHb29n
         bGUgQ2xvdWQgTWVtb3J5c3RvcmUgUmVkaXMgU2VydmVyIENBMRQwEgYDVQQKEwtH
         b29nbGUsIEluYzELMAkGA1UEBhMCVVMwHhcNMjAwOTE3MjEzNDE1WhcNMzAwOTE1
         MjEzNTE1WjCBhTEtMCsGA1UELhMkNzYxNTc4OGMtMTI2Yi00Nzk0LWI2MWMtY2Yx
         OWE2Y2Y1ZjNiMTEwLwYDVQQDEyhHb29nbGUgQ2xvdWQgTWVtb3J5c3RvcmUgUmVk
         aXMgU2VydmVyIENBMRQwEgYDVQQKEwtHb29nbGUsIEluYzELMAkGA1UEBhMCVVMw
         ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCyDKmDHZm6tzMhNtKOnp8H
         8+zTv1qA6OkBToVqCjKTTMGO18ovNtAAMjbGvclLuJNLbA2WTTWVttHen6Cn82h0
         3gG9HMk9AwK1cVT7gW072h++TRsYddIRlwnSweRWL8jUX+PNt7CjFqH+sma/Hb1m
         CktHdBOa897JiYHrMVNTcpS8SFwwz05yHUTEVGlHdkvlaJXfHLe6keCMABLyjaMh
         1Jl4gZI2WqLMV680pJusK6FI6q/NmqENFc9ywMEg395lHTK9w9e014WIXg0q7sU3
         84ChVVS2yYOMEUWeov4Qx6XeVfA4ss5t7OCqsMQkvslkE90mJZcVvhBj3QvTH9Rz
         AgMBAAGjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwDQYJKoZIhvcNAQELBQADggEB
         AJkn+MDE4V10DZn4uEc0s0Mg4FEMC1fDewmDYwSNnxRlzfEi+wAX2AaqrJ4m4Qa7
         xIyuSYxArEOY6QeyJyw7/06dom8aAv4aO2p8hE04Ih6QwaTMFIlT2Jf6TidVd3eT
         wfjwFJVoJ+dgxsaCv2uMFZWee5aRHmKzj9LhqPwpWnTs9Q/qmOheUNoe2/1i8yvn
         662M7RZMR7fZH6ETsdz5w1nPXXiRqJ7K0EGKoPNjMlYK3/U1X3sazI4tpMNgTdxG
         rnNh9Sd9REMBmDCPj9dUI9k4hQX4yQZp96fnLT6cet22OPajEKnpzyqJs1s4iX/g
         lEtWs4V/YBhKA56CW6ASZS8=
         -----END CERTIFICATE-----
         -----BEGIN CERTIFICATE-----
         MIIDnTCCAoWgAwIBAgIBADANBgkqhkiG9w0BAQsFADCBhTEtMCsGA1UELhMkYjg4
         ZTUzYTMtODdmNC00N2VhLWJjN2MtYTdhMzM4NmIwZmU4MTEwLwYDVQQDEyhHb29n
         bGUgQ2xvdWQgTWVtb3J5c3RvcmUgUmVkaXMgU2VydmVyIENBMRQwEgYDVQQKEwtH
         b29nbGUsIEluYzELMAkGA1UEBhMCVVMwHhcNMjAwOTE4MjEzMTI3WhcNMzAwOTE2
         MjEzMjI3WjCBhTEtMCsGA1UELhMkYjg4ZTUzYTMtODdmNC00N2VhLWJjN2MtYTdh
         MzM4NmIwZmU4MTEwLwYDVQQDEyhHb29nbGUgQ2xvdWQgTWVtb3J5c3RvcmUgUmVk
         aXMgU2VydmVyIENBMRQwEgYDVQQKEwtHb29nbGUsIEluYzELMAkGA1UEBhMCVVMw
         ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDEO4Zs/So5DA6wtftkAElD
         8BVREob4gby2mGBYAtd3JJQKFC+zIqCf2DhrWihrCeXhsdsZqJUF16E3MsCCWS2T
         UWt6T37zObU2fzKmb7X+TSw1tunIUcIXwWzoMhqdGrIvfI9guMbF+KssQIjDMs9M
         G/hY6cY1NB5THOxXqcxzYrwSKB1EE160EDz4RgKAYQhw7AyVOBBAbWqA5pTEDuUy
         qpsz+NFpKYTwaeTpzil0xIl0JJS3DOd4G7ZnMG2wFT2j3wt+P0SkAPuOWgmX82iO
         gGmKoaCh3KcICie/rZRTfsRPjMm+yswRQRDeLB5eoMmH+gbUInVZU0qOJ/7gOYEb
         AgMBAAGjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwDQYJKoZIhvcNAQELBQADggEB
         AF4xlEbwLUK5VjoKlJBtKXLYrYcW+AbQLhZQFP8exE8bOW7p39h+5J0nl3ItPxu6
         97BCt1P5TFisba8pBxaExiDsYmjKQrhtizMkzl5h9hGksOgoLlAqaaxfA97+Q9Tq
         5gaYChESur/159Z3jiM47obKoZmHfgSgr//7tjII7yZxUGhOjIVffv/fEa4aixqM
         0yH1V1s8hWHZeui2VFrHmTxY20IH9ktyedjSUgnFXzsEH6sbR18p0wBZqyrrtURs
         DaUIeoOHfHgEJM8k/wphSJI0V6pMC6nax2JhexLTRiUsiGTLRDe3VtsdWqS2DLa9
         9DmrfdF0eFrfWw3VRNLwwXg=
         -----END CERTIFICATE-----
         

Your file, as seen in the previous example, should use the following guidelines:

     * Copy the entire CA, including the `-----BEGIN CERTIFICATE-----` and   
`-----END CERTIFICATE-----` lines.

     * Make sure that the text of the CAs is completely left justified. Verify that no spaces appear in front of any line of the CAs.

     * Add each CA on a new line. Verify that no blank lines exist between CAs.




## Configure the client for in-transit encryption

The client that you use to connect to the cluster must either support TLS or use a third-party sidecar to enable TLS.

If your client supports TLS, then configure it to point to the cluster's IP address, port 6379, and the file containing the CA. You can see an example of how to connect to a [cluster](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance#connect_to_an_in_transit_encryption_enabled_instance) that has in-transit encryption enabled.

## Manage the CA rotation

We recommend that you install all downloadable CA certificates on the clients that access the cluster.

Installing the latest CA certificates periodically ensures that you have the necessary certificates when Memorystore for Redis Cluster rotates the CAs. During this rotation, both the existing CAs and new CAs are active.

## Code sample to connect to a cluster that uses in-transit encryption

To view a code sample on how to set up a client library to connect to a cluster that uses in-transit encryption, see [In-transit encryption client library code sample](https://docs.cloud.google.com/memorystore/docs/cluster/client-library-connection#in-transit_encryption_client_library_code_sample).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
