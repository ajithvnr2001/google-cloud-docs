---
url: https://docs.cloud.google.com/memorystore/docs/valkey/create-instances/
title: Create instances \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:43.704848+00:00
---

# Create instances  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/create-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Create instances Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for creating single-zone and multi-zone instances in Memorystore for Valkey.

## Before you begin

Complete the before you begin instructions:

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)
  2. Make sure that billing is enabled for your project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  3. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI.

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. You need at least gcloud CLI version `489.0.0` to access the Memorystore for Valkey gcloud CLI commands.

  4. Enable the Memorystore for Valkey API   
[Memorystore for Valkey](https://console.cloud.google.com/apis/library/memorystore.googleapis.com)
  5. Enable the Network Connectivity API   
[Network Connectivity API](https://console.cloud.google.com/apis/library/networkconnectivity.googleapis.com)
  6. Enable the Service Consumer Management API   
[Service Consumer Management API](https://console.cloud.google.com/apis/library/serviceconsumermanagement.googleapis.com)



### Other prerequisites

  * You must have one of these [IAM roles](https://docs.cloud.google.com/memorystore/docs/valkey/access-control) in the Google Cloud project you're using: 
    * `roles/memorystore.admin` (the Memorystore Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)



## Set up networking

Read the [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking) page to determine if you need to set up a service connection policy.

If a service connection policy hasn't been created for the network with which you will create the Valkey instance, follow the [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking) guidance to create it.

## Create a multi-zone instance

This section provides instructions on creating a [multi-zone instance](https://docs.cloud.google.com/memorystore/docs/valkey/single-zone-instances).

**Important** : Before you follow the steps in this procedure, complete the steps in the Before you begin and Set up networking sections.

If you create an instance with replicas, and a single zone of the region where you want the instance to be created is unavailable, then Memorystore for Valkey creates the instance in the available zones of the region. This zonal allocation is temporary. After the unavailable zone becomes available, Memorystore for Valkey redistributes the nodes of the instance so that they're evenly distributed among the zones.

If you create an instance without replicas and a single zone is unavailable, then Memorystore for Valkey fails to create the instance.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click **Create instance**.

  3. In the **Name your instance** section, enter an ID for the instance. The instance ID must use only lowercase letters, numbers, and hyphens. It must also start with a letter and be unique in its region.

  4. From the **Region** menu, select a region for your instance.

  5. In the **Zonal availability** section, select the **Multi-zone** option because you want to create a [multi-zone](https://docs.cloud.google.com/memorystore/docs/valkey/single-zone-instances) instance.

  6. In the **Cluster Mode** section, specify whether you want a Cluster Mode Enabled or Cluster Mode Disabled instance. For more information about these types of instances, see [Enable and disable cluster mode](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled).

**Note:** After you create a Cluster Mode Enabled or Cluster Mode Disabled instance, you can't change the instance to the other mode. We recommend that you select **Enabled** because this mode has better horizontal scaling characteristics.
  7. In the **Node Type** section, select a [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type).

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
  8. In the **Instance size** section, enter the number of shards for your instance. The shard count determines the total memory capacity for storing instance data. For more information about instance specifications, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

  9. If you want to create an instance with replicas, then in the **Replicas** section, select the number of replicas (per shard). You can select 0-5 replicas. The default value is 1 replica.

  10. In the **Set up connection** section, select the network that your applications can use to connect to this instance. For more information about private networking for Memorystore for Valkey, see [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking).

  11. If you want to increase the security of your instance, then in the **Security** section, do one of the following:

     * If you want to enable [IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth), then select the **IAM Auth** option. Memorystore for Valkey uses IAM authentication to restrict access to the instance.

     * If you want to enable [basic token-based authentication](https://docs.cloud.google.com/memorystore/docs/valkey/manage-basic-auth), then select the **Token Auth** option. Memorystore for Valkey restricts access to the instance by having clients use their authentication tokens to verify their identities within your applications.

     * If you don't want to enable IAM authentication or basic token-based authentication, then select the **Disabled** option.

If you select the **IAM Auth** or **Token Auth** options, then Memorystore for Valkey selects the **Enable In-Transit Encryption (TLS)** checkbox automatically, and the **Certificate authority management** section is displayed. Memorystore for Valkey [encrypts](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption) your credentials so that they're confidential when they're transmitted from the instance to the application.

  12. In the **Certificate authority management** section, select the **Per-instance CA** , **Customer-managed CA** , or **Shared CA** option. These options represent the [Certificate Authority (CA) modes](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption#certificate-authorities) for your instance. The CA mode determines which CA hierarchy is used to issue the digital certificates for the instance.

If you select the **Customer-managed CA** option, then you must add a CA pool. A CA pool is a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy. A CA pool makes CA rotation management easier and lets you achieve higher total effective queries per second (QPS).

To add a CA pool, do one of the following:

     1. To add a CA pool from another Google Cloud project, select the **Add CA from another project** checkbox, and then enter the [resource ID](https://docs.cloud.google.com/memorystore/docs/valkey/use-customer-managed-ca#create-CA-pool) for the pool in the text field.

     2. To add a CA pool that's located in the same Google Cloud project as the project that you're using to create the instance, select the pool from the **CA pool** menu.

  13. In the **Encryption** section, select one of the following options:

     * **Google-managed encryption key** : you want Google to use a key to encrypt the data in the instance. This is _Google default encryption_.
     * **Cloud KMS key** : you want to manage the encryption of your data by using customer-managed encryption keys (CMEKs) in [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services, such as Memorystore for Valkey.

If you select this option, then do the following:

       1. From the **Key management type** menu, select **Cloud KMS**.
       2. From the **Select a Cloud KMS** key menu, select a CMEK.
  14. To assign an ACL policy to the instance, select a policy from the **Policy** menu in the **ACL policy** section.

**Important** : If the ACL policy that you want to assign doesn't appear, then verify that the policy and the instance are in the same region. You can assign ACL policies only to instances that are located in the same region as the policy. For example, if you create an ACL policy in the `us-central1` region, then you can assign it only to instances that are also in `us-central1`. Also, after you create an ACL policy, you can't change its region.
  15. In the **Data persistence strategy** section, specify how you want Memorystore for Valkey to persist the data in your instance. Acceptable values are **No persistence** , [**Append Only File (AOF)** persistence](https://docs.cloud.google.com/memorystore/docs/valkey/about-aof-persistence), and [**Memory Snapshot** persistence](https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence).

  16. If you want to enable [automated backups](https://docs.cloud.google.com/memorystore/docs/valkey/backups#automated-and-on-demand-backups) for your instance, then do the following:

     1. Select the **Automated daily backups** checkbox.
     2. In the **Days to retain backups** field, enter the number of days that you want Memorystore for Valkey to keep backups before they're deleted automatically. You can specify from `1` to `365` days. The default value is `35` days.
     3. From the **Time window** menu, select a time for the daily backup.
  17. In the **Maintenance** section, select one of the following options:

     * **Default** : Memorystore for Valkey updates your instance routinely to ensure that the service is reliable, performant, secure, and up-to-date.
     * **Custom** : you want to customize the maintenance schedule for your instance to align with your application's needs and to minimize disruptions. If you select this option, then specify the day that you want maintenance to occur and the hour when you want the maintenance window to start.
  18. In the **Choose version** section, select your [Valkey version](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions). Available versions are 7.2, 8.0, 9.0, and 9.1. The default version is version 9.1.

**Important:** After you select a version for the instance, you can't downgrade the instance to an earlier version.
  19. Click **Create instance**.




### gcloud

To create a Memorystore for Valkey instance, run the `create` command:
    
    
    gcloud memorystore instances create INSTANCE \
    --location=REGION_ID \
    --endpoints='[{"connections": [{"pscAutoConnection": {"network": "projects/PROJECT_ID/global/networks/NETWORK_ID", "projectId": "PROJECT_ID"}}]}]' \
    --replica-count=REPLICA_COUNT \
    --node-type=NODE_TYPE \
    --engine-version=ENGINE_VERSION \
    --shard-count=SHARD_COUNT \
    --acl-policy=ACL_POLICY_NAME \
    --mode=MODE
    

Replace the following:

  * INSTANCE is the ID of the Memorystore for Valkey instance you're creating. Your instance ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.

  * REGION_ID is the region where you want the instance placed.


**Note:** You can only create instances in the [supported regions](https://docs.cloud.google.com/memorystore/docs/valkey/locations) for Memorystore for Valkey.

  * PROJECT_ID is the ID of the project where you want to create your instance.

  * NETWORK_ID is the ID of the network you want to use to create your instance.

  * REPLICA_COUNT is the number of replicas (per shard). Accepted values are `0`-`5`.

  * NODE_TYPE is the [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type) that you want to use for the instance.

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
  * ENGINE_VERSION is the version of your Memorystore for Valkey instance. Accepted values for this parameter are `VALKEY_7_2`, `VALKEY_8_0`, `VALKEY_9_0`, and `VALKEY_9_1`. If you don't specify a value, then `VALKEY_9_1` is the default value.

**Important:** After you specify a version for the instance, you can't downgrade the instance to an earlier version.
  * SHARD_COUNT determines the number of shards in your instance. The shard count determines the total memory capacity for storing instance data. Cluster Mode Disabled instances only support one shard. For more information, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

  * ACL_POLICY_NAME is the name of the access control list (ACL) policy that you're assigning to the instance that you're creating. By using ACL policies, you can secure access to the instance. You can enable fine-grained security by restricting user and service access to specific keys, commands, and Pub/Sub channels. For more information, see [Secure access to your instances by using ACL policies](https://docs.cloud.google.com/memorystore/docs/valkey/use-acl-policies).

**Important** : You can assign ACL policies only to instances that are located in the same region as the policy. For example, if you create an ACL policy in the `us-central1` region, then you can assign it only to instances that are also in `us-central1`. Also, after you create an ACL policy, you can't change its region.
  * MODE determines whether you're creating a Cluster Mode Enabled or Cluster Mode Disabled instance. If this field is omitted, then the instance defaults to Cluster Mode Enabled. For more information, see [Enable and disable Cluster Mode](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled).

**Note:** After you create a Cluster Mode Enabled or Cluster Mode Disabled instance, you can't change the instance to the other mode. We recommend that you create a Cluster Mode Enabled instance because this type of instance has better scaling characteristics.



For example:

### Cluster Mode Enabled example
    
    
    
    gcloud memorystore instances create my-instance \
    --location=us-central1 \
    --endpoints='[{"connections": [{"pscAutoConnection": {"network": "projects/my-project/global/networks/default", "projectId": "my-project"}}]}]' \
    --replica-count=2 \
    --node-type=highmem-medium \
    --shard-count=8 \
    --acl-policy=my-acl-policy \
    --mode=cluster
    
    

### Cluster Mode Disabled example
    
    
    
    gcloud memorystore instances create my-instance \
    --location=us-central1 \
    --endpoints='[{"connections": [{"pscAutoConnection": {"network": "projects/my-project/global/networks/default", "projectId": "my-project"}}]}]' \
    --shard-count=1 \
    --replica-count=2 \
    --node-type=highmem-medium \
    --acl-policy=my-acl-policy \
    --mode=cluster-disabled
    
    

By default, [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption) is disabled and the authorized network is `default`.

## Create a single-zone instance

This section provides instructions on creating a [single-zone instance](https://docs.cloud.google.com/memorystore/docs/valkey/single-zone-instances).

**Important:** Before following these steps, complete the steps in the [Before you begin](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances#before-you-begin) and [Set up networking](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances#set-up-networking) sections.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click **Create instance**.

  3. In the **Name your instance** section, enter an ID for the instance. The instance ID must use only lowercase letters, numbers, and hyphens. It must also start with a letter and be unique in its region.

  4. From the **Region** menu, select a region for your instance.

  5. In the **Zonal availability** section, do the following:

     1. Select the **Single zone** option.

     2. From the **Zone** menu, select the zone where you want Memorystore for Valkey to create the instance.

  6. In the **Cluster Mode** section, specify whether you want a Cluster Mode Enabled or Cluster Mode Disabled instance. For more information about these types of instances, see [Enable and disable cluster mode](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled).

**Note:** After you create a Cluster Mode Enabled or Cluster Mode Disabled instance, you can't change the instance to the other mode. We recommend that you select **Enabled** because this mode has better horizontal scaling characteristics.
  7. In the **Node Type** section, select a [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type).

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
  8. In the **Instance size** section, enter the number of shards for your instance. The shard count determines the total memory capacity for storing instance data. For more information about instance specifications, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

  9. If you want to create an instance with replicas, then in the **Replicas** section, select the number of replicas (per shard). You can select 0-5 replicas. The default value is 1 replica.

  10. In the **Set up connection** section, select the network that your applications can use to connect to this instance. For more information about private networking for Memorystore for Valkey, see [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking).

  11. If you want to increase the security of your instance, then in the **Security** section, do one of the following:

     * If you want to enable [IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth), then select the **IAM Auth** option. Memorystore for Valkey uses IAM authentication to restrict access to the instance.

     * If you want to enable [basic token-based authentication](https://docs.cloud.google.com/memorystore/docs/valkey/manage-basic-auth), then select the **Token Auth** option. Memorystore for Valkey restricts access to the instance by having clients use their authentication tokens to verify their identities within your applications.

     * If you don't want to enable IAM authentication or basic token-based authentication, then select the **Disabled** option.

If you select the **IAM Auth** or **Token Auth** options, then Memorystore for Valkey selects the **Enable In-Transit Encryption (TLS)** checkbox automatically, and the **Certificate authority management** section is displayed. Memorystore for Valkey [encrypts](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption) your credentials so that they're confidential when they're transmitted from the instance to the application.

  12. In the **Certificate authority management** section, select the **Per-instance CA** , **Customer-managed CA** , or **Shared CA** option. These options represent the [Certificate Authority (CA) modes](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption#certificate-authorities) for your instance. The CA mode determines which CA hierarchy is used to issue the digital certificates for the instance.

If you select the **Customer-managed CA** option, then you must add a CA pool. A CA pool is a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy. A CA pool makes CA rotation management easier and lets you achieve higher total effective queries per second (QPS).

To add a CA pool, do one of the following:

     1. To add a CA pool from another Google Cloud project, select the **Add CA from another project** checkbox, and then enter the [resource ID](https://docs.cloud.google.com/memorystore/docs/valkey/use-customer-managed-ca#create-CA-pool) for the pool in the text field.

     2. To add a CA pool that's located in the same Google Cloud project as the project that you're using to create the instance, select the pool from the **CA pool** menu.

  13. In the **Encryption** section, select one of the following options:

     * **Google-managed encryption key** : you want Google to use a key to encrypt the data in the instance. This is _Google default encryption_.
     * **Cloud KMS key** : you want to manage the encryption of your data by using customer-managed encryption keys (CMEKs) in [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services, such as Memorystore for Valkey.

If you select this option, then do the following:

       1. From the **Key management type** menu, select **Cloud KMS**.
       2. From the **Select a Cloud KMS** key menu, select a CMEK.
  14. To assign an ACL policy to the instance, select a policy from the **Policy** menu in the **ACL policy** section.

**Important** : If the ACL policy that you want to assign doesn't appear, then verify that the policy and the instance are in the same region. You can assign ACL policies only to instances that are located in the same region as the policy. For example, if you create an ACL policy in the `us-central1` region, then you can assign it only to instances that are also in `us-central1`. Also, after you create an ACL policy, you can't change its region.
  15. In the **Data persistence strategy** section, specify how you want Memorystore for Valkey to persist the data in your instance. Acceptable values are **No persistence** , [**Append Only File (AOF)** persistence](https://docs.cloud.google.com/memorystore/docs/valkey/about-aof-persistence), and [**Memory Snapshot** persistence](https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence).

  16. If you want to enable [automated backups](https://docs.cloud.google.com/memorystore/docs/valkey/backups#automated-and-on-demand-backups) for your instance, then do the following:

     1. Select the **Automated daily backups** checkbox.
     2. In the **Days to retain backups** field, enter the number of days that you want Memorystore for Valkey to keep backups before they're deleted automatically. You can specify from `1` to `365` days. The default value is `35` days.
     3. From the **Time window** menu, select a time for the daily backup.
  17. In the **Maintenance** section, select one of the following options:

     * **Default** : Memorystore for Valkey updates your instance routinely to ensure that the service is reliable, performant, secure, and up-to-date.
     * **Custom** : you want to customize the maintenance schedule for your instance to align with your application's needs and to minimize disruptions. If you select this option, then specify the day that you want maintenance to occur and the hour when you want the maintenance window to start.
  18. In the **Choose version** section, select your [Valkey version](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions). Available versions are 7.2, 8.0, 9.0, and 9.1. The default version is version 9.1.

**Important:** After you select a version for the instance, you can't downgrade the instance to an earlier version.
  19. Click **Create instance**.




### gcloud

To create a single-zone instance, run the `create` command:
    
    
    gcloud memorystore instances create INSTANCE \
    --location=REGION_ID \
    --endpoints='[{"connections": [{"pscAutoConnection": {"network": "projects/PROJECT_ID/global/networks/NETWORK_ID", "projectId": "PROJECT_ID"}}]}]' \
    --replica-count=REPLICA_COUNT \
    --node-type=NODE_TYPE \
    --engine-version=ENGINE_VERSION \
    --shard-count=SHARD_COUNT \
    --zone-distribution-config-mode=ZONE_DISTRIBUTION_CONFIG_MODE \
    --zone-distribution-config=ZONE \
    --acl-policy=ACL_POLICY_NAME \
    --mode=MODE
    

Replace the following:

  * INSTANCE is the ID of the Memorystore for Valkey instance you're creating. Your instance ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.

  * REGION_ID is the region where you want the instance placed.

  * PROJECT_ID is the ID of the project where you want to create your instance.

  * NETWORK_ID is the ID of the network you want to use to create your instance.

  * REPLICA_COUNT is the number of replicas (per shard). Accepted values are `0`-`5`.

  * NODE_TYPE is the [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type) that you want to use for the instance.

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
  * ENGINE_VERSION is the version of your Memorystore for Valkey instance. Accepted values for this parameter are `VALKEY_7_2`, `VALKEY_8_0`, `VALKEY_9_0`, and `VALKEY_9_1`. If you don't specify a value, then `VALKEY_9_1` is the default value.

**Important:** After you specify a version for the instance, you can't downgrade the instance to an earlier version.
  * SHARD_COUNT determines the number of shards in your instance. The shard count determines the total memory capacity for storing instance data. If the mode that you select is Cluster Mode Disabled, then you can specify only one shard for your instance. For more information, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

  * ZONE_DISTRIBUTION_CONFIG_MODE is the mode that lets you choose between provisioning a single-zone instance or a multi-zone instance. The default is `multi-zone`. Accepted values are `single-zone`, and `multi-zone`.

  * ZONE is the zone where you want to provision your nodes. This flag is applicable only if you set `--zone-distribution-config-mode` to `single-zone`.

  * ACL_POLICY_NAME is the name of the access control list (ACL) policy that you're assigning to the instance that you're creating. By using ACL policies, you can secure access to the instance. You can enable fine-grained security by restricting user and service access to specific keys, commands, and Pub/Sub channels. For more information, see [Secure access to your instances by using ACL policies](https://docs.cloud.google.com/memorystore/docs/valkey/use-acl-policies).

**Important** : You can assign ACL policies only to instances that are located in the same region as the policy. For example, if you create an ACL policy in the `us-central1` region, then you can assign it only to instances that are also in `us-central1`. Also, after you create an ACL policy, you can't change its region.
  * MODE determines whether you're creating a Cluster Mode Enabled or Cluster Mode Disabled instance. If you omit this field, then the mode defaults to Cluster Mode Enabled. For more information, see [Enable and disable Cluster Mode](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled).

**Note:** After you create a Cluster Mode Enabled or Cluster Mode Disabled instance, you can't change the instance to the other mode. We recommend that you create a Cluster Mode Enabled instance because this type of instance has better scaling characteristics.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
