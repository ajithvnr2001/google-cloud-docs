---
url: https://docs.cloud.google.com/memorystore/docs/valkey/use-customer-managed-ca/
title: Secure your data by using a customer-managed Certificate Authority (CA) \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:20.783404+00:00
---

# Secure your data by using a customer-managed Certificate Authority (CA)  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/use-customer-managed-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Secure your data by using a customer-managed Certificate Authority (CA) Stay organized with collections  Save and categorize content based on your preferences. 

You can encrypt all data that moves between your client applications and Memorystore for Valkey securely. This is _in-transit encryption_. By using in-transit encryption, all Valkey traffic is encrypted through the [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security) protocol. This ensures that all data that moves between your applications and Memorystore for Valkey remains confidential and untampered.

When in-transit encryption is enabled, Valkey clients communicate exclusively across a secure connection. Valkey clients that aren't configured for TLS are blocked. If you choose to use in-transit encryption, then you're responsible for ensuring that your Valkey client can use the TLS protocol.

Instances that use in-transit encryption have Certificate Authorities (CAs). You use the CAs to authenticate the certificates of the machines in your instances.

One CA mode that you can use is a customer-managed CA. You can use customer-managed CAs for your Memorystore for Valkey instances. If you need to manage your own CAs for compliance reasons, then you can use this CA mode. As part of using this mode, you must set up your own CA pool that's hosted on [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs).

Before you can configure an instance to use customer-managed CAs, you must create a CA pool in the same region as your instance and at least one CA in that pool using the CA Service. The CA can be a [root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca) or a [subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca). You also can create a subordinate CA in the CA Service and then chain the subordinate CA to an external root CA.

When you create your instance, you specify the CA pool. As part of this configuration, the project-specific Memorystore for Valkey service account has permissions to use the CA pool. The service account requests a CA from the pool and Memorystore for Valkey uses that CA to sign the server certificate for the instance.

**Important:** For instances that have replicas, replicated data is encrypted fully at the network level, based on Google Cloud encryption standards. Also, Memorystore for Valkey supports the TLS protocol, versions 1.2 and later.

## Before you begin

Before you use the customer-managed CA mode, make sure that you meet the following requirements.

### Required roles

To get the permissions that you need to create a CA pool and CA, have your administrator grant you the CA Service Operation Manager (`roles/privateca.caManager`) IAM role on CA Service.

You might also get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Workflow to use a customer-managed CA

To use a customer-managed CA, the workflow is as follows:

  1. Create a CA pool. Before you can configure an instance to use a customer-managed CA, you must create a CA pool in CA Service. This pool must be in the same region as your instance.
  2. Create a CA in the CA pool. After you create the CA pool, you must use CA Service to create at least one CA in the pool.
  3. Delegate permission to the Memorystore for Valkey service account to issue server certificates with CAs from the CA pool that you create.
  4. Create an instance to use the customer-managed CA.



## Create a CA pool

You can create a CA pool in CA Service in the same project where you plan to create your Memorystore for Valkey instances, or you can create the CA pool in a different project. However, if you create the CA pool in a different project, then VPC Service Controls might block you from creating any instances, depending on your organization policies. To fix the issue, make sure that the project that hosts the CA pool and CA, and the project that hosts Memorystore for Valkey belong to the same service perimeter. For more information, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) and [Manage service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters).

To create a CA pool, follow the instructions in [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool). You can accept the default values for the CA pool, with the following required configuration settings:

  * Create the CA pool in the _same region_ where you plan to create your instance. For a list of regions that Memorystore for Valkey supports, see [Memorystore for Valkey locations](https://docs.cloud.google.com/memorystore/docs/valkey/locations). 
  * Allow configuration-based certificate requests.
  * Allow DNS names in subject alternative names (SAN). When you configure the identity constraints of the CA pool, don't set any restrictions on the format for the DNS names that might conflict with what Memorystore for Valkey might add to the SAN.



## Create a CA in the CA pool

Create at least one CA in the CA pool that you created.

You can create a root CA or a subordinate CA.

To create a root CA, follow the instructions in [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca). You can accept the default values for the CA, but make sure that you create the CA in the **Enabled** state.

When you configure the **CA key size and algorithm** , you can select any key size and algorithm.

If you create a subordinate CA, then you need to create and configure your root CA first.

  * To create a subordinate CA in CA Service, follow the instructions in [Create a subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca).

  * To create a subordinate CA from an external root CA, follow the instructions in [Create a subordinate CA from an external CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-sub-ca-from-external-ca).




## Provide the service account with access to the CA pool

To make sure that your Memorystore for Valkey service account has permissions to request and sign certificates for your instances, grant the `roles/privateca.certificateRequester` role to the service account for the CA pool that you created.

This service account has the following format:  
`service-PROJECT_NUMBER@cloud-memorystore.iam.gserviceaccount.com`. Replace PROJECT_NUMBER with the project number of your Google Cloud project.

### gcloud

To grant the service account access to the CA pool, use the [`gcloud privateca pools add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/add-iam-policy-binding) command.
    
    
    gcloud privateca pools add-iam-policy-binding CA_POOL_ID \
    --project=PROJECT_ID \
    --location=REGION_ID \
    --member serviceAccount:SERVICE_ACCOUNT_NAME \
    --role=roles/privateca.certificateRequester
    

Make the following replacements:

  * CA_POOL_ID: the ID of the CA pool that you created.
  * PROJECT_ID: the ID of the Google Cloud project where you want to create your instances.
  * REGION_ID: the region where the CA pool is located.
  * SERVICE_ACCOUNT_NAME: the name of the Memorystore for Valkey service account. The project number for this service account is the same as the project number that's associated with the PROJECT_ID.



## Create an instance that uses a customer-managed CA

**Important:** When you use a customer-managed CA for an instance, you can't change the CA mode. Also, you can't deactivate in-transit encryption for instances that you create in this way.

### Console

Follow the steps at [Create instances](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances).

### gcloud

To create an instance that uses a customer-managed CA, use the [`gcloud memorystore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/create) command.
    
    
    gcloud memorystore instances create INSTANCE_ID \
    --location=REGION_ID \
    --endpoints='[{"connections": [{"pscAutoConnection": {"network": "projects/PROJECT_ID/global/networks/NETWORK_ID", "projectId": "PROJECT_ID"}}]}]' \
    --replica-count=REPLICA_COUNT \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT \
    --engine-version=ENGINE_VERSION \
    --mode=MODE \
    --transit-encryption-mode=server-authentication \
    --server-ca-mode=customer-managed-cas-ca \
    --server-ca-pool="projects/CA_POOL_PROJECT_ID/locations/REGION_ID/caPools/CA_POOL_ID"
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance that you're creating. The instance ID must be 1 to 63 characters, and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter, and end with a lowercase letter or number.

  * REGION_ID: the region where you want the instance to be located. You must create your instance in the same region as the CA pool that you created.

  * PROJECT_ID: the ID of the project where you want to create the instance.

  * NETWORK_ID: the ID of the network that you want to use to create the instance.

  * REPLICA_COUNT: the number of replicas (per shard). Accepted values are `0`-`5`.

  * NODE_TYPE: the node type. Accepted values are:

    * `shared-core-nano`
    * `standard-small`
    * `highmem-medium`
    * `highmem-xlarge`
**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type. For more information about these node types, see [Choose a node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type).
  * SHARD_COUNT: the number of shards in the instance. The shard count determines the total memory capacity for storing instance data. For more information about instance specifications, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

  * ENGINE_VERSION: the version of the instance. Accepted values for this parameter are `VALKEY_7_2`, `VALKEY_8_0`, `VALKEY_9_0`, and `VALKEY_9_1`. If you don't specify a value, then `VALKEY_9_1` is the default value.

**Important:** After you specify a version for the instance, you can't downgrade the instance to an earlier version.
  * MODE: determine if the instance is Cluster Mode Enabled or Cluster Mode Disabled. If this field is omitted, then the instance defaults to Cluster Mode Enabled. For more information, see [Enable and disable cluster mode](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled).

  * CA_POOL_PROJECT_ID: the ID of the CA pool that you created.

  * REGION_ID: the region where the CA pool is located. The instance that you're creating and the CA pool must be located in the same region.

  * CA_POOL_ID: the ID of the CA pool that you created.




The `server-ca-mode` parameter represents the CA mode for the instance. For a customer-managed CA, `customer-managed-cas-ca` is the value for the parameter. If you don't use this parameter, then the default CA mode is per-instance.

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
    --server-ca-mode=customer-managed-cas-ca \
    --server-ca-pool="projects/my-CA-pool-project/locations/us-central1/caPools/my-CA-pool"
    

## Rotate the instance's server certificates

In addition to Memorystore for Valkey conducting a weekly server-side certificate rotation, you can rotate the certificates on-demand.

### gcloud

To rotate the server certificates for all machines in an instance, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command.
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --location=REGION_ID \
    --rotate-server-certificate
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance that contains machines for which you want to rotate the server certificates
  * REGION_ID: the region where the instance is located



For example:
    
    
    gcloud memorystore instances update my-instance \
    --location=us-central1 \
    --rotate-server-certificate
    

## Limitations

The following limitations apply when using customer-managed CAs with Memorystore for Valkey:

  * After you configure a customer-managed CA for an instance, you can't modify the configuration. For example, you can't change the ID of the CA pool for the instance.
  * Don't delete the customer-managed CA pool or revoke the service account permissions that are associated with the CA. If you do, then the server certificates can't be rotated and will expire. As a result, your client applications will be unable to connect to the instance.



## Troubleshoot

This section lists error messages that you might receive when you use customer-managed CAs and includes tips to troubleshoot these messages.

Error message | Cause | Troubleshoot  
---|---|---  
`FAILED_PRECONDITION: GetClusterCertificateAuthority not supported for customer-managed CAs` | If you use a customer-managed CA, then you can't use Memorystore for Valkey to retrieve the CA certificates. | To [get the CA certificates](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/get-ca-certs) for a customer-managed CA, you must use the CA Service.  
`Server certificate rotation can only be triggered for customer-managed CAs.` | You're attempting to rotate server certificates for an instance, but the instance's CA mode is per-instance or shared. | You can't rotate server certificates unless the mode that you use for an instance is customer-managed.  
`Invalid format for server CA pool: {CA pool resource}. Expected projects/{project}/locations/{location}/caPools/{caPool}.` | The CA pool that you're using to create the instance has an invalid format. | For the CA pool, use this format:  
projects/CA_POOL_PROJECT_ID/locations/REGION_ID/ caPools/CA_POOL_ID  
`The instance/cluster's server CA pool must be in the same region as the instance/cluster. CA Pool region: {CA pool region}, Instance/cluster region: {cluster region}.` | You're attempting to create an instance that's located in a different region from the CA pool. | Make sure that the instance you're creating and your CA pool are in the same region.  
`Request is prohibited by organization's policy for CA Pool {CA pool ID}.` | The Google Cloud project that hosts the CA pool and the project that hosts the instance aren't in the same [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters). | [Configure VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters) so that the projects belong to the same service perimeter.  
`Permission privateca.certificates.create denied on {CA pool ID}. Make sure that you granted the roles/privateca.certificateRequester role to the service account {P4SA email}.` | The Memorystore for Valkey service account doesn't have the `roles/privateca.certificateRequester` role for the CA pool. As a result, Memorystore for Valkey can't generate server certificates. | Grant the `roles/privateca.certificateRequester` role to the service account. For more information, see Provide the service account with access to the CA pool.  
`Resource {CA pool ID} not found.` | Memorystore for Valkey can't find the CA pool that you specified when you attempted to create the instance. | Check the project ID, location, and name of the CA pool.  
`There are no enabled CAs in the CaPool {CA pool ID}. Please ensure that there is at least one enabled Certificate Authority to issue a certificate.` | There are no CAs enabled in the CA pool. Memorystore for Valkey can't generate server certificates for the instance. | Make sure that you create at least one CA in the CA pool, and that the CA is in the **Enabled** state.  
`Quota exhausted for CA Service. Check quotas for the project hosting the CA Pool: {CA pool ID}.` | You exceeded the quota for the CA Service in the Google Cloud project that hosts the CA pool. Memorystore for Valkey can't perform operations that require this service. | Check the quota for the CA Service in your project. For more information, see [Quotas and limits](https://docs.cloud.google.com/certificate-authority-service/quotas).  
`server_ca_pool must be provided when server_ca_mode is SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA.` | You're attempting to create an instance that uses the customer-managed CA mode. However, you didn't provide information about the CA pool. | Specify the project ID, location, and name of the CA pool.  
`server_ca_pool must not be provided when server_ca_mode is not SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA.` | You're attempting to create an instance that uses the per-instance or shared CA mode. These CA modes don't use the `server_ca_pool` parameter. | You can't use this parameter unless the CA mode is customer-managed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
