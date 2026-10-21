---
url: https://docs.cloud.google.com/memorystore/docs/cluster/create-instances/
title: Create instances \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:08.342008+00:00
---

# Create instances  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/create-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Create instances Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for creating Memorystore for Redis Cluster instances.

## Before you begin

Complete the before you begin instructions:

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)
  2. Make sure that billing is enabled for your project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  3. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI.

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. You need at least gcloud CLI version `440.0.0` to access the Memorystore for Redis Cluster gcloud CLI commands.

  4. Enable the Memorystore for Redis API   
[Memorystore for Redis](https://console.cloud.google.com/apis/library/redis.googleapis.com)
  5. Enable the Network Connectivity API   
[Network Connectivity API](https://console.cloud.google.com/apis/library/networkconnectivity.googleapis.com)
  6. Enable the Service Consumer Management API   
[Service Consumer Management API](https://console.cloud.google.com/apis/library/serviceconsumermanagement.googleapis.com)



### Other prerequisites

  * You must have one of these [IAM roles](https://docs.cloud.google.com/memorystore/docs/cluster/access-control) in the Google Cloud project you're using: 
    * `roles/redis.admin` (the Memorystore Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)



## Set up networking

Read the [Networking](https://docs.cloud.google.com/memorystore/docs/cluster/networking) page to determine if you need to set up a service connection policy.

If a service connection policy hasn't been created for the network with which you will create the Redis cluster, follow the [Networking](https://docs.cloud.google.com/memorystore/docs/cluster/networking) guidance to create it.

## Create an instance

**Important** : Before you follow the steps in this procedure, complete the steps in the Before you begin and Set up networking sections.

If you create a cluster with replicas, and a single zone of the region where you want the cluster to be created is unavailable, then Memorystore for Redis Cluster creates the cluster in the available zones of the region. This zonal allocation is temporary. After the unavailable zone becomes available, Memorystore for Redis Cluster redistributes the nodes of the cluster so that they're evenly distributed among the zones.

If you create a cluster without replicas and a single zone is unavailable, then Memorystore for Redis Cluster fails to create the cluster.

**Tip:** If you plan on using private networking, then you can deploy both the private networking setup of your choice and the Memorystore for Redis Cluster instance along with clients such as Compute Engine VMs by using Terraform. For more information, see [ Simplified Cloud Networking Configuration Solutions](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions). 

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click **Create cluster**.

  3. In the **Name your cluster instance** section, enter an ID for the cluster. The Cluster ID must use only lowercase letters, numbers, and hyphens. It must also start with a letter and be unique in its region.

  4. From the **Region** menu, select a region for your cluster.

  5. In the **Zonal availability** section, select the **Multi-zone** option because you want to create a [multi-zone](https://docs.cloud.google.com/memorystore/docs/cluster/single-zone-instances) cluster.

  6. In the **Node Type** section, select a [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type).

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  7. In the **Cluster size** section, enter the number of shards for your cluster. The shard count determines the total memory capacity for storing cluster data. For more information about cluster specifications, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

  8. If you want to create a cluster with replicas, then in the **Replicas** section, select the number of replicas (per shard). You can select 0-5 replicas. The default value is 1 replica.

  9. In the **Set up connection** section, select the network that your applications can use to connect to this cluster. For more information about private networking for Memorystore for Redis Cluster, see [Networking overview](https://docs.cloud.google.com/memorystore/docs/cluster/networking).

  10. If you want to increase the security of your cluster, then in the **Security** section, do one of the following:

     * If you want to enable [IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth), then select the **IAM Auth** option. Memorystore for Redis Cluster uses IAM authentication to restrict access to the cluster.

     * If you want to enable [basic token-based authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-basic-auth), then select the **Token Auth** option. Memorystore for Redis Cluster restricts access to the cluster by having clients use their authentication tokens to verify their identities within your applications.

     * If you don't want to enable IAM authentication or basic token-based authentication, then select the **Disabled** option.

If you select the **IAM Auth** or **Token Auth** options, then Memorystore for Redis Cluster selects the **Enable In-Transit Encryption (TLS)** checkbox automatically, and the **Certificate authority management** section is displayed. Memorystore for Redis Cluster [encrypts](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption) your credentials so that they're confidential when they're transmitted from the cluster to the application.

  11. In the **Certificate authority management** section, select the **Per-instance CA** , **Customer-managed CA** , or **Shared CA** option. These options represent the [Certificate Authority (CA) modes](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption#certificate-authorities) for your cluster. The CA mode determines which CA hierarchy is used to issue the digital certificates for the cluster.

If you select the **Customer-managed CA** option, then you must add a CA pool. A CA pool is a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy. A CA pool makes CA rotation management easier and lets you achieve higher total effective queries per second (QPS).

To add a CA pool, do one of the following:

     1. To add a CA pool from another Google Cloud project, select the **Add CA from another project** checkbox, and then enter the [resource ID](https://docs.cloud.google.com/memorystore/docs/cluster/use-customer-managed-ca#create-CA-pool) for the pool in the text field.

     2. To add a CA pool that's located in the same Google Cloud project as the project that you're using to create the cluster, select the pool from the **CA pool** menu.

  12. In the **Encryption** section, select one of the following options:

     * **Google-managed encryption key** : you want Google to use a key to encrypt the data in the cluster. This is _Google default encryption_.
     * **Cloud KMS key** : you want to manage the encryption of your data by using customer-managed encryption keys (CMEKs) in [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services, such as Memorystore for Redis Cluster.

If you select this option, then do the following:

       1. From the **Key management type** menu, select **Cloud KMS**.
       2. From the **Select a Cloud KMS** key menu, select a CMEK.
  13. To assign an ACL policy to the cluster, select a policy from the **Policy** menu in the **ACL policy** section.

**Important** : If the ACL policy that you want to assign doesn't appear, then verify that the policy and the cluster are in the same region. You can assign ACL policies only to clusters that are located in the same region as the policy. For example, if you create an ACL policy in the `us-central1` region, then you can assign it only to clusters that are also in `us-central1`. Also, after you create an ACL policy, you can't change its region.
  14. In the **Data persistence strategy** section, specify how you want Memorystore for Redis Cluster to persist the data in your cluster. Acceptable values are **No persistence** , [**Append Only File (AOF)** persistence](https://docs.cloud.google.com/memorystore/docs/cluster/about-aof-persistence), and [**Redis Database (RDB)** persistence](https://docs.cloud.google.com/memorystore/docs/cluster/about-rdb-persistence).

  15. If you want to enable [automated backups](https://docs.cloud.google.com/memorystore/docs/cluster/backups#automated_and_on-demand_backups) for your cluster, then do the following:

     1. Select the **Automated daily backups** checkbox.
     2. In the **Days to retain backups** field, enter the number of days that you want Memorystore for Redis Cluster to keep backups before they're deleted automatically. You can specify from `1` to `365` days. The default value is `35` days.
     3. From the **Time window** menu, select a time for the daily backup.
  16. In the **Maintenance** section, select one of the following options:

     * **Default** : Memorystore for Redis Cluster updates your cluster routinely to ensure that the service is reliable, performant, secure, and up-to-date.
     * **Custom** : you want to customize the maintenance schedule for your cluster to align with your application's needs and to minimize disruptions. If you select this option, then specify the day that you want maintenance to occur and the hour when you want the maintenance window to start.
  17. Click **Create cluster**.




### gcloud

To create a Memorystore for Redis Cluster instance, run the `create` command:
    
    
    gcloud redis clusters create INSTANCE_ID \
    --region=REGION_ID \
    --network=NETWORK \
    --replica-count=REPLICA_COUNT \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT \
    --acl-policy=ACL_POLICY_NAME
    

Replace the following:

  * INSTANCE_ID is the ID of the Memorystore for Redis Cluster instance you're creating. Your instance ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.

  * REGION_ID is the region where you want the instance placed.


**Note:** You can only create instances in the [supported regions](https://docs.cloud.google.com/memorystore/docs/cluster/locations) for Memorystore for Redis Cluster. Not all of the regions currently supported by Memorystore for Redis are available for Memorystore for Redis Cluster. The `gcloud redis regions list` commands shows supported regions for Memorystore for Redis, not Memorystore for Redis Cluster.

  * NETWORK is the network used to create your instance. It must use the format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID used here must match the network ID used by the service connection policy. Otherwise, the `create` operation fails.

  * REPLICA_COUNT is the number of replicas (per shard). Accepted values are `0`-`5`.

  * NODE_TYPE is the [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) that you want to use for the cluster.

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  * SHARD_COUNT determines the number of shards in your instance. Shard count determines the total memory capacity for storing cluster data. To see more details about cluster specification, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

  * ACL_POLICY_NAME is the name of the access control list (ACL) policy that you're assigning to the cluster that you're creating. By using ACL policies, you can secure access to the cluster. You can enable fine-grained security by restricting user and service access to specific keys, commands, and Pub/Sub channels. For more information, see [Secure access to your clusters by using ACL policies](https://docs.cloud.google.com/memorystore/docs/cluster/use-acl-policies).

**Important** : You can assign ACL policies only to clusters that are located in the same region as the policy. For example, if you create an ACL policy in the `us-central1` region, then you can assign it only to clusters that are also in `us-central1`. Also, after you create an ACL policy, you can't change its region.



For example:
    
    
    gcloud alpha redis clusters create my-instance \
    --region=us-central1 \
    --network=projects/my-project-335118/global/networks/default \
    --replica-count=2 \
    --node-type=redis-highmem-medium \
    --shard-count=8 \
    --acl-policy=my-acl-policy
    

By default, [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption) is disabled, and the authorized network is `default`.

## Create a single-zone instance

This section provides instructions on creating a [Single-zone instance](https://docs.cloud.google.com/memorystore/docs/cluster/single-zone-instances).

**Important:** Before following these steps, complete the steps in the [Before you begin](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances#before-you-begin) and [Set up networking](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances#set-up-networking) sections.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click **Create cluster**.

  3. In the **Name your cluster instance** section, enter an ID for the cluster. The Cluster ID must use only lowercase letters, numbers, and hyphens. It must also start with a letter and be unique in its region.

  4. From the **Region** menu, select a region for your cluster.

  5. In the **Zonal availability** section, do the following:

     1. Select the **Single zone** option.

     2. From the **Zone** menu, select the zone where you want Memorystore for Redis Cluster to create the cluster.

  6. In the **Node Type** section, select a [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type).

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  7. In the **Cluster size** section, enter the number of shards for your cluster. The shard count determines the total memory capacity for storing cluster data. For more information about cluster specifications, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

  8. If you want to create a cluster with replicas, then in the **Replicas** section, select the number of replicas (per shard). You can select 0-5 replicas. The default value is 1 replica.

  9. In the **Set up connection** section, select the network that your applications can use to connect to this cluster. For more information about private networking for Memorystore for Redis Cluster, see [Networking overview](https://docs.cloud.google.com/memorystore/docs/cluster/networking).

  10. If you want to increase the security of your cluster, then in the **Security** section, do one of the following:

     * If you want to enable [IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth), then select the **IAM Auth** option. Memorystore for Redis Cluster uses IAM authentication to restrict access to the cluster.

     * If you want to enable [basic token-based authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-basic-auth), then select the **Token Auth** option. Memorystore for Redis Cluster restricts access to the cluster by having clients use their authentication tokens to verify their identities within your applications.

     * If you don't want to enable IAM authentication or basic token-based authentication, then select the **Disabled** option.

If you select the **IAM Auth** or **Token Auth** options, then Memorystore for Redis Cluster selects the **Enable In-Transit Encryption (TLS)** checkbox automatically, and the **Certificate authority management** section is displayed. Memorystore for Redis Cluster [encrypts](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption) your credentials so that they're confidential when they're transmitted from the cluster to the application.

  11. In the **Certificate authority management** section, select the **Per-instance CA** , **Customer-managed CA** , or **Shared CA** option. These options represent the [Certificate Authority (CA) modes](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption#certificate-authorities) for your cluster. The CA mode determines which CA hierarchy is used to issue the digital certificates for the cluster.

If you select the **Customer-managed CA** option, then you must add a CA pool. A CA pool is a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy. A CA pool makes CA rotation management easier and lets you achieve higher total effective queries per second (QPS).

To add a CA pool, do one of the following:

     1. To add a CA pool from another Google Cloud project, select the **Add CA from another project** checkbox, and then enter the [resource ID](https://docs.cloud.google.com/memorystore/docs/cluster/use-customer-managed-ca#create-CA-pool) for the pool in the text field.

     2. To add a CA pool that's located in the same Google Cloud project as the project that you're using to create the cluster, select the pool from the **CA pool** menu.

  12. In the **Encryption** section, select one of the following options:

     * **Google-managed encryption key** : you want Google to use a key to encrypt the data in the cluster. This is _Google default encryption_.
     * **Cloud KMS key** : you want to manage the encryption of your data by using customer-managed encryption keys (CMEKs) in [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services, such as Memorystore for Redis Cluster.

If you select this option, then do the following:

       1. From the **Key management type** menu, select **Cloud KMS**.
       2. From the **Select a Cloud KMS** key menu, select a CMEK.
  13. To assign an ACL policy to the cluster, select a policy from the **Policy** menu in the **ACL policy** section.

**Important** : If the ACL policy that you want to assign doesn't appear, then verify that the policy and the cluster are in the same region. You can assign ACL policies only to clusters that are located in the same region as the policy. For example, if you create an ACL policy in the `us-central1` region, then you can assign it only to clusters that are also in `us-central1`. Also, after you create an ACL policy, you can't change its region.
  14. In the **Data persistence strategy** section, specify how you want Memorystore for Redis Cluster to persist the data in your cluster. Acceptable values are **No persistence** , [**Append Only File (AOF)** persistence](https://docs.cloud.google.com/memorystore/docs/cluster/about-aof-persistence), and [**Redis Database (RDB)** persistence](https://docs.cloud.google.com/memorystore/docs/cluster/about-rdb-persistence).

  15. If you want to enable [automated backups](https://docs.cloud.google.com/memorystore/docs/cluster/backups#automated_and_on-demand_backups) for your cluster, then do the following:

     1. Select the **Automated daily backups** checkbox.
     2. In the **Days to retain backups** field, enter the number of days that you want Memorystore for Redis Cluster to keep backups before they're deleted automatically. You can specify from `1` to `365` days. The default value is `35` days.
     3. From the **Time window** menu, select a time for the daily backup.
  16. In the **Maintenance** section, select one of the following options:

     * **Default** : Memorystore for Redis Cluster updates your cluster routinely to ensure that the service is reliable, performant, secure, and up-to-date.
     * **Custom** : you want to customize the maintenance schedule for your cluster to align with your application's needs and to minimize disruptions. If you select this option, then specify the day that you want maintenance to occur and the hour when you want the maintenance window to start.
  17. Click **Create cluster**.




### gcloud

To create a single-zone instance, run the `create` command:
    
    
    gcloud redis clusters create INSTANCE_ID \
    --region=REGION_ID \
    --network=NETWORK \
    --replica-count=REPLICA_COUNT \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT \
    --zone-distribution-mode=ZONE_DISTRIBUTION_MODE \
    --zone=ZONE \
    --acl-policy=ACL_POLICY_NAME
    

Replace the following:

  * INSTANCE_ID is the ID of the Memorystore for Redis Cluster instance you're creating. Your instance ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.

  * REGION_ID is the region where you want the instance placed.

  * NETWORK is the network used to create your instance. It must use the format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID used here must match the network ID used by the service connection policy. Otherwise, the `create` operation fails.

  * REPLICA_COUNT is the number of replicas (per shard). Accepted values are `0`-`5`.

  * NODE_TYPE is the [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) that you want to use for the cluster.

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  * SHARD_COUNT determines the number of shards in your instance. Shard count determines the total memory capacity for storing cluster data. For more information about cluster specification, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

  * ZONE_DISTRIBUTION_MODE is the mode that lets you choose between provisioning a single-zone instance or a multi-zone instance. The default is multi-zone. Accepted values are `single-zone`, and `multi-zone`.

  * ZONE is the zone where you want to provision your nodes. This flag is applicable only if you set `--zone-distribution-mode` to `single-zone`.

  * ACL_POLICY_NAME is the name of the access control list (ACL) policy that you're assigning to the cluster that you're creating. By using ACL policies, you can secure access to the cluster. You can enable fine-grained security by restricting user and service access to specific keys, commands, and Pub/Sub channels. For more information, see [Secure access to your clusters by using ACL policies](https://docs.cloud.google.com/memorystore/docs/cluster/use-acl-policies).

**Important** : You can assign ACL policies only to clusters that are located in the same region as the policy. For example, if you create an ACL policy in the `us-central1` region, then you can assign it only to clusters that are also in `us-central1`. Also, after you create an ACL policy, you can't change its region.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
