---
url: https://docs.cloud.google.com/memorystore/docs/valkey/manage-in-transit-encryption/
title: Secure your data by using a per-instance Certificate Authority (CA) \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:20.702654+00:00
---

# Secure your data by using a per-instance Certificate Authority (CA)  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/manage-in-transit-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Secure your data by using a per-instance Certificate Authority (CA) Stay organized with collections  Save and categorize content based on your preferences. 

You can encrypt all data that moves between your client applications and Memorystore for Valkey securely. This is _in-transit encryption_. By using in-transit encryption, all Valkey traffic is encrypted through the [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security) protocol. This ensures that all data that moves between your applications and Memorystore for Valkey remains confidential and untampered.

When in-transit encryption is enabled, Valkey clients communicate exclusively across a secure connection. Valkey clients that aren't configured for TLS are blocked. If you choose to use in-transit encryption, then you're responsible for ensuring that your Valkey client can use the TLS protocol.

Instances that use in-transit encryption have Certificate Authorities (CAs). You use the CAs to authenticate the certificates of the machines in your instances.

One CA mode that you can use is a per-instance CA. Memorystore for Valkey provisions each instance with its own, unique CA infrastructure. To access an instance securely, you must configure your client application to trust this CA hierarchy. This involves downloading and installing CA certificates on each client that accesses the instance.

**Important** : CAs are valid for ten years from the date that they're created. New CAs are available for you to download and install on your clients that connect to the instance about five years before the current CAs expire. Existing CAs are valid until their expiration dates. After the CAs expire, you can uninstall them from your clients.

For instances that have replicas, replicated data is encrypted fully at the network level, based on Google Cloud encryption standards. Also, Memorystore for Valkey supports the TLS protocol, versions 1.2 and later.

## Create an instance that uses a per-instance CA

**Important** : Before you create an instance, you must have a service connection policy established for your network. For more information, see [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking). 

Also, when you use a per-instance CA for this instance, you can't change the CA mode or deactivate in-transit encryption.

### Console

Follow the steps at [Create instances](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances).

### gcloud

To create an instance that uses a per-instance CA, use the [`gcloud memorystore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/create) command.
    
    
    gcloud memorystore instances create INSTANCE_ID \
    --location=REGION_ID \
    --endpoints='[{"connections": [{"pscAutoConnection": {"network": "projects/PROJECT_ID/global/networks/NETWORK_ID", "projectId": "PROJECT_ID"}}]}]' \
    --replica-count=REPLICA_COUNT \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT \
    --engine-version=ENGINE_VERSION \
    --mode=MODE \
    --transit-encryption-mode=server-authentication \
    --server-ca-mode=google-managed-per-instance-ca
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance that you're creating. The instance ID must be 1 to 63 characters, and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter, and end with a lowercase letter or number.

  * REGION_ID: the region where you want the instance to be located.

  * PROJECT_ID: the ID of the project where you want to create the instance.

  * NETWORK_ID: the ID of the network that you want to use to create the instance.

  * REPLICA_COUNT: the number of replicas (per shard). Accepted values are `0`-`5`.

  * NODE_TYPE: the [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type) for the instance.

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
  * SHARD_COUNT: the number of shards in the instance. The shard count determines the total memory capacity for storing instance data. For more information about instance specifications, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

  * ENGINE_VERSION: the version of the instance. Accepted values for this parameter are `VALKEY_7_2`, `VALKEY_8_0`, `VALKEY_9_0`, and `VALKEY_9_1`. If you don't specify a value, then `VALKEY_9_1` is the default value.

**Important:** After you specify a version for the instance, you can't downgrade the instance to an earlier version.
  * MODE: determine if the instance is Cluster Mode Enabled or Cluster Mode Disabled. If this field is omitted, then the instance defaults to Cluster Mode Enabled. For more information, see [Enable and disable cluster mode](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled).




The `server-ca-mode` parameter represents the CA mode for the instance. For a per-instance CA, `google-managed-per-instance-ca` is the value for the parameter. If you don't use this parameter, then the default CA mode is per-instance.

For example:
    
    
    gcloud memorystore instances create my-instance \
    --location=us-central1 \
    --endpoints='[{"connections": [{"pscAutoConnection": {"network": "projects/my-project/global/networks/my-network", "projectId": "my-project"}}]}] \
    --replica-count=1 \
    --node-type=highmem-medium \
    --shard-count=3 \
    --engine-version=VALKEY_9_1 \
    --mode=CLUSTER \
    --transit-encryption-mode=server-authentication \
    --server-ca-mode=google-managed-per-instance-ca
    

## Download the CAs

If you enable in-transit encryption for an instance, then when you use the [`get-certificate-authority`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/get-certificate-authority) command, the certificates of the CAs appear.
    
    
    gcloud memorystore instances get-certificate-authority INSTANCE_ID
    

Replace INSTANCE_ID with the ID of the instance.

The response body includes certificates for all applicable CAs.

## Install CA certificates on the client

You must install the CA certificates on the client that connects to the instance. Depending on the type of client, the CA certificate installation might vary.

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
         

To format the text in the file correctly, use the following guidelines:

     * Copy the entire CA, including the `-----BEGIN CERTIFICATE-----` and   
`-----END CERTIFICATE-----` lines.

     * Make sure that the text of the CAs is completely left justified. Verify that no spaces appear in front of any line of the CAs.

     * Add each CA on a new line. Verify that no blank lines exist between CAs.




## Configure the client for in-transit encryption

The client that you use to connect to the instance must either support TLS or use a third-party sidecar to enable TLS.

If your client supports TLS, then configure it to point to the instance's IP address, port 6379, and the file containing the CA. You can see examples of how to connect to a [Cluster Mode Enabled](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance#connect_to_an_in_transit_encryption_enabled_instance) or [Cluster Mode Disabled](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance#connect_to_cluster_disabled_in_transit_encryption_enabled_instance) instance in Memorystore for Valkey that has in-transit encryption enabled.

## Manage the CA rotation

We recommend that you install all downloadable CA certificates on the clients that access the instance.

Installing the latest CA certificates periodically ensures that you have the necessary certificates when Memorystore for Valkey rotates the CAs. During this rotation, both the existing CAs and new CAs are active.

## Code sample to connect to an instance that uses in-transit encryption

To view a code sample on how to set up a client library to connect to an instance that uses in-transit encryption, see [Code sample for both IAM authentication and in-transit encryption](https://docs.cloud.google.com/memorystore/docs/valkey/client-library-code-samples#iam_auth_and_in_transit_encryption).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
