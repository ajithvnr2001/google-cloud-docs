---
url: https://docs.cloud.google.com/memorystore/docs/cluster/use-customer-managed-ca/
title: Secure your data by using a customer-managed Certificate Authority (CA) \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:11.306208+00:00
---

# Secure your data by using a customer-managed Certificate Authority (CA)  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/use-customer-managed-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Secure your data by using a customer-managed Certificate Authority (CA) Stay organized with collections  Save and categorize content based on your preferences. 

You can encrypt all data that moves between your client applications and Memorystore for Redis Cluster securely. This is _in-transit encryption_. By using in-transit encryption, all Redis traffic is encrypted through the [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security) protocol. This ensures that all data that moves between your applications and Memorystore for Redis Cluster remains confidential and untampered.

When in-transit encryption is enabled, Redis clients communicate exclusively across a secure connection. Redis clients that aren't configured for TLS are blocked. If you choose to use in-transit encryption, then you're responsible for ensuring that your Redis client can use the TLS protocol.

Clusters that use in-transit encryption have Certificate Authorities (CAs). You use the CAs to authenticate the certificates of the machines in your clusters.

One CA mode that you can use is a customer-managed CA. You can use customer-managed CAs for your clusters in Memorystore for Redis Cluster. If you need to manage your own CAs for compliance reasons, then you can use this CA mode. As part of using this mode, you must set up your own CA pool that's hosted on [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs).

Before you can configure a cluster to use customer-managed CAs, you must create a CA pool in the same region as your cluster and at least one CA in that pool using the CA Service. The CA can be a [root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca) or a [subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca). You also can create a subordinate CA in the CA Service and then chain the subordinate CA to an external root CA.

When you create your cluster, you specify the CA pool. As part of this configuration, the project-specific Memorystore for Redis Cluster service account has permissions to use the CA pool. The service account requests a CA from the pool and Memorystore for Redis Cluster uses that CA to sign the server certificate for the cluster.

**Important:** For clusters that have replicas, replicated data is encrypted fully at the network level, based on Google Cloud encryption standards. Also, Memorystore for Redis Cluster supports the TLS protocol, versions 1.2 and later.

## Before you begin

Before you use the customer-managed CA mode, make sure that you meet the following requirements.

### Required roles

To get the permissions that you need to create a CA pool and CA, have your administrator grant you the CA Service Operation Manager (`roles/privateca.caManager`) IAM role on CA Service.

You might also get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Workflow to use a customer-managed CA

To use a customer-managed CA, the workflow is as follows:

  1. Create a CA pool. Before you can configure a cluster to use a customer-managed CA, you must create a CA pool in CA Service. This pool must be in the same region as your cluster.
  2. Create a CA in the CA pool. After you create the CA pool, you must use CA Service to create at least one CA in the pool.
  3. Delegate permission to the Memorystore for Redis Cluster service account to issue server certificates with CAs from the CA pool that you create.
  4. Create a cluster to use the customer-managed CA.



## Create a CA pool

You can create a CA pool in CA Service in the same project where you plan to create your clusters in Memorystore for Redis Cluster, or you can create the CA pool in a different project. However, if you create the CA pool in a different project, then VPC Service Controls might block you from creating any clusters, depending on your organization policies. To fix the issue, make sure that the project that hosts the CA pool and CA, and the project that hosts Memorystore for Redis Cluster belong to the same service perimeter. For more information, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) and [Manage service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters).

To create a CA pool, follow the instructions in [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool). You can accept the default values for the CA pool, with the following required configuration settings:

  * Create the CA pool in the _same region_ where you plan to create your cluster. For a list of regions that Memorystore for Redis Cluster supports, see [Memorystore for Redis Cluster locations](https://docs.cloud.google.com/memorystore/docs/cluster/locations). 
  * Allow configuration-based certificate requests.
  * Allow DNS names in subject alternative names (SAN). When you configure the identity constraints of the CA pool, don't set any restrictions on the format for the DNS names that might conflict with what Memorystore for Redis Cluster might add to the SAN.



## Create a CA in the CA pool

Create at least one CA in the CA pool that you created.

You can create a root CA or a subordinate CA.

To create a root CA, follow the instructions in [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca). You can accept the default values for the CA, but make sure that you create the CA in the **Enabled** state.

When you configure the **CA key size and algorithm** , you can select any key size and algorithm.

If you create a subordinate CA, then you need to create and configure your root CA first.

  * To create a subordinate CA in CA Service, follow the instructions in [Create a subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca).

  * To create a subordinate CA from an external root CA, follow the instructions in [Create a subordinate CA from an external CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-sub-ca-from-external-ca).




## Provide the service account with access to the CA pool

To make sure that your Memorystore for Redis Cluster service account has permissions to request and sign certificates for your clusters, grant the `roles/privateca.certificateRequester` role to the service account for the CA pool that you created.

This service account has the following format:  
`service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com`. Replace PROJECT_NUMBER with the project number of your Google Cloud project.

### gcloud

To grant the service account access to the CA pool, use the [`gcloud privateca pools add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/add-iam-policy-binding) command.
    
    
    gcloud privateca pools add-iam-policy-binding CA_POOL_ID \
    --project=PROJECT_ID \
    --location=REGION_ID \
    --member serviceAccount:SERVICE_ACCOUNT_NAME \
    --role=roles/privateca.certificateRequester
    

Make the following replacements:

  * CA_POOL_ID: the ID of the CA pool that you created.
  * PROJECT_ID: the ID of the Google Cloud project where you want to create your clusters.
  * REGION_ID: the region where the CA pool is located.
  * SERVICE_ACCOUNT_NAME: the name of the Memorystore for Redis Cluster service account. The project number for this service account is the same as the project number that's associated with the PROJECT_ID.



## Create a cluster that uses a customer-managed CA

**Important:** When you use a customer-managed CA for a cluster, you can't change the CA mode. Also, you can't deactivate in-transit encryption for clusters that you create in this way.

### Console

Follow the steps at [Create instances](https://docs.cloud.google.com/memorystore/docs/cluster/create-manage-instances).

### gcloud

To create a cluster that uses a customer-managed CA, use the [`gcloud redis clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/create) command.
    
    
    gcloud redis clusters create CLUSTER_ID \
    --region=REGION_ID \
    --network=NETWORK \
    --replica-count=REPLICA_COUNT \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT \
    --transit-encryption-mode=server-authentication \
    --server-ca-mode=customer-managed-cas-ca \
    --server-ca-pool="projects/CA_POOL_PROJECT_ID/locations/REGION_ID/caPools/CA_POOL_ID"
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster that you're creating. The cluster ID must be 1 to 63 characters, and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter, and end with a lowercase letter or number.

  * REGION_ID: the region where you want the cluster to be located. You must create your cluster in the same region as the CA pool that you created.

  * NETWORK: the network that you use to create the cluster. It must use this format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID that you use must match the network ID that the service connection policy uses. Otherwise, you can't create the cluster.

  * REPLICA_COUNT: the number of replicas (per shard). Accepted values are `0`-`5`.

  * NODE_TYPE: the node type. Accepted values are:

    * `redis-shared-core-nano`
    * `redis-standard-small`
    * `redis-highmem-medium`
    * `redis-highmem-xlarge`
**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type. For more information about these node types, see [Choose a node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type).
  * SHARD_COUNT: the number of shards in the cluster. The shard count determines the total memory capacity for storing cluster data. For more information about cluster specifications, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

  * CA_POOL_PROJECT_ID: the ID of the CA pool that you created.

  * REGION_ID: the region where the CA pool is located. The cluster that you're creating and the CA pool must be located in the same region.

  * CA_POOL_ID: the ID of the CA pool that you created.




The `server-ca-mode` parameter represents the CA mode for the cluster. For a customer-managed CA, `customer-managed-cas-ca` is the value for the parameter. If you don't use this parameter, then the default CA mode is per-instance.

For example:
    
    
    gcloud redis clusters create my-cluster \
    --region=us-central1 \
    --network=projects/my-network-project/global/networks/default \
    --replica-count=1 \
    --node-type=redis-highmem-medium \
    --shard-count=3 \
    --transit-encryption-mode=server-authentication \
    --server-ca-mode=customer-managed-cas-ca \
    --server-ca-pool="projects/my-CA-pool-project/locations/us-central1/caPools/my-CA-pool"
    

## Rotate the cluster's server certificates

In addition to Memorystore for Redis Cluster conducting a weekly server-side certificate rotation, you can rotate the certificates on-demand.

### gcloud

To rotate the server certificates for all machines in a cluster, use the [`gcloud redis clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/update) command.
    
    
    gcloud redis clusters update CLUSTER_ID \
    --region=REGION_ID \
    --rotate-server-certificate
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster that contains machines for which you want to rotate the server certificates
  * REGION_ID: the region where the cluster is located



For example:
    
    
    gcloud redis clusters update my-cluster \
    --region=us-central1 \
    --rotate-server-certificate
    

## Limitations

The following limitations apply when using customer-managed CAs with Memorystore for Redis Cluster:

  * After you configure a customer-managed CA for a cluster, you can't modify the configuration. For example, you can't change the ID of the CA pool for the cluster.
  * Don't delete the customer-managed CA pool or revoke the service account permissions that are associated with the CA. If you do, then the server certificates can't be rotated and will expire. As a result, your client applications will be unable to connect to the cluster.



## Troubleshoot

This section lists error messages that you might receive when you use customer-managed CAs and includes tips to troubleshoot these messages.

Error message | Cause | Troubleshoot  
---|---|---  
`FAILED_PRECONDITION: GetClusterCertificateAuthority not supported for customer-managed CAs` | If you use a customer-managed CA, then you can't use Memorystore for Redis Cluster to retrieve the CA certificates. | To [get the CA certificates](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/get-ca-certs) for a customer-managed CA, you must use the CA Service.  
`Server certificate rotation can only be triggered for customer-managed CAs.` | You're attempting to rotate server certificates for a cluster, but the cluster's CA mode is per-instance or shared. | You can't rotate server certificates unless the mode that you use for a cluster is customer-managed.  
`Invalid format for server CA pool: {CA pool resource}. Expected projects/{project}/locations/{location}/caPools/{caPool}.` | The CA pool that you're using to create the cluster has an invalid format. | For the CA pool, use this format:  
projects/CA_POOL_PROJECT_ID/locations/REGION_ID/ caPools/CA_POOL_ID  
`The instance/cluster's server CA pool must be in the same region as the instance/cluster. CA Pool region: {CA pool region}, Instance/cluster region: {cluster region}.` | You're attempting to create a cluster that's located in a different region from the CA pool. | Make sure that the cluster you're creating and your CA pool are in the same region.  
`Request is prohibited by organization's policy for CA Pool {CA pool ID}.` | The Google Cloud project that hosts the CA pool and the project that hosts the cluster aren't in the same [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters). | [Configure VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters) so that the projects belong to the same service perimeter.  
`Permission privateca.certificates.create denied on {CA pool ID}. Make sure that you granted the roles/privateca.certificateRequester role to the service account {P4SA email}.` | The Memorystore for Redis Cluster service account doesn't have the `roles/privateca.certificateRequester` role for the CA pool. As a result, Memorystore for Redis Cluster can't generate server certificates. | Grant the `roles/privateca.certificateRequester` role to the service account. For more information, see Provide the service account with access to the CA pool.  
`Resource {CA pool ID} not found.` | Memorystore for Redis Cluster can't find the CA pool that you specified when you attempted to create the cluster. | Check the project ID, location, and name of the CA pool.  
`There are no enabled CAs in the CaPool {CA pool ID}. Please ensure that there is at least one enabled Certificate Authority to issue a certificate.` | There are no CAs enabled in the CA pool. Memorystore for Redis Cluster can't generate server certificates for the cluster. | Make sure that you create at least one CA in the CA pool, and that the CA is in the **Enabled** state.  
`Quota exhausted for CA Service. Check quotas for the project hosting the CA Pool: {CA pool ID}.` | You exceeded the quota for the CA Service in the Google Cloud project that hosts the CA pool. Memorystore for Redis Cluster can't perform operations that require this service. | Check the quota for the CA Service in your project. For more information, see [Quotas and limits](https://docs.cloud.google.com/certificate-authority-service/quotas).  
`server_ca_pool must be provided when server_ca_mode is SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA.` | You're attempting to create a cluster that uses the customer-managed CA mode. However, you didn't provide information about the CA pool. | Specify the project ID, location, and name of the CA pool.  
`server_ca_pool must not be provided when server_ca_mode is not SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA.` | You're attempting to create a cluster that uses the per-instance or shared CA mode. These CA modes don't use the `server_ca_pool` parameter. | You can't use this parameter unless the CA mode is customer-managed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
