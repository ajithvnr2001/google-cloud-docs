---
url: https://docs.cloud.google.com/alloydb/docs/connect-public-ip/
title: Connect using public IP \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:53.616145+00:00
---

# Connect using public IP  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/connect-public-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Connect using public IP Stay organized with collections  Save and categorize content based on your preferences. 

To connect to your AlloyDB for PostgreSQL instance from outside your Virtual Private Cloud (VPC) network—or to allow your instance to connect to external resources—you can enable public IP connectivity. AlloyDB supports both inbound and outbound public IP connections:

  * **Inbound public IP** : Assigns a public IPv4 address to your AlloyDB instance so external clients can connect to it. You can optionally restrict direct connections to specific external IP addresses or CIDR ranges, called _authorized external networks_. Authorized external networks aren't required when you connect by using the AlloyDB Language Connectors or the AlloyDB Auth Proxy, and you can't specify a private network as an authorized external network.
  * **Outbound public IP** : Assigns two static outbound public IP addresses to a primary or secondary instance so your database can initiate connections to external sources, such as during a database migration.



## Create an AlloyDB instance

To create an instance with public IP, do the following:

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page, go to **Instances in your cluster** , and click **Create primary instance**.

  4. Configure your primary instance:

     1. In the **Instance ID** field, enter an ID for your primary instance.
     2. Under **Zonal availability** , select one of the following options: 
        1. To create a highly available production instance with automated failover, select **Multiple zones (Highly available)**.
        2. To create a basic instance that does not need to be highly available, select **Single zone**.
     3. Select a machine type.
     4. Under **Connectivity** , select **Enable Public IP** to support inbound connections.
     5. Optional: To add outbound connectivity, under **Outbound Public IP Addresses** , select **Enable Outbound Public IP**.
     6. Optional: To configure SSL or connector requirements on the instance, expand **Advanced configuration options** , then do the following: 
        1. By default, AlloyDB instances require all connections to use SSL encryption. To allow non-SSL connections, clear the **Only allow SSL connections** checkbox.
        2. To require that all database connections to the instance use the AlloyDB Auth Proxy or the secure connector libraries provided by Google, select **Enforce mTLS via AlloyDB connectors**.
     7. Optional: To restrict direct connections to specific IP addresses, add a comma-separated list of CIDR ranges:

        1. Under **Authorized external networks** , enter a comma-separated list of CIDR ranges. For each CIDR range, enter a CIDR block, such as `64.233.160.0/16`. To minimize the potential attack surface, keep the list of addresses as small as possible.

You can also click **Use my IP** to let AlloyDB populate the IPv4 address of the client machine from which you're accessing Google Cloud.

**Note:** **Use my IP** isn't available for clients that use IPv6 addresses.
     8. Click **Create instance**.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

For more information about creating other instance types, see [Create a read pool instance](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create) and [Create a secondary instance](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#secondary-cluster-instance).

Use the [`gcloud alloydb instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/create) command to create an instance.
    
    
    gcloud alloydb instances create INSTANCE_ID \
        --instance-type=PRIMARY \
        --cpu-count=CPU_COUNT \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --database-flags=password.enforce_complexity=on \
        --assign-inbound-public-ip=ASSIGN_IPV4
    

Replace the following:

  * `INSTANCE_ID`: the ID of the instance you are creating. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `CPU_COUNT`: the number of vCPUs you want for the instance. Valid values include the following: 
    * `2`: 2 vCPUs, 16 GB RAM
    * `4`: 4 vCPUs, 32 GB RAM
    * `8`: 8 vCPUs, 64 GB RAM
    * `16`: 16 vCPUs, 128 GB RAM
    * `32`: 32 vCPUs, 256 GB RAM
    * `64`: 64 vCPUs, 512 GB RAM
    * `96`: 96 vCPUs, 768 GB RAM
    * `128`: 128 vCPUs, 864 GB RAM
  * `REGION_ID`: the region where you want the instance placed.
  * `CLUSTER_ID`: the ID of the cluster you created earlier.



#### Optional: Add authorized external networks

To restrict direct connections to specific IP addresses, add a comma-separated list of CIDR ranges:
    
    
    gcloud alloydb instances create INSTANCE_ID \
        --instance-type=PRIMARY \
        --cpu-count=CPU_COUNT \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --database-flags=password.enforce_complexity=on \
        --assign-inbound-public-ip=ASSIGN_IPV4 \
        --authorized-external-networks=CIDR_RANGE1,CIDR_RANGE2,...
    

Replace the following:

  * `CIDR_RANGE`: a comma-separated list of CIDR blocks, such as `64.233.160.0/16`. To minimize the potential attack surface, keep the list of addresses as small as possible.



#### Optional: Add outbound connectivity

Add the `--outbound-public-ip` flag to enable outbound public IP addresses. You can only enable outbound public IP for primary and secondary instances.
    
    
    gcloud alloydb instances create INSTANCE_ID \
        --instance-type=PRIMARY \
        --cpu-count=CPU_COUNT \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --database-flags=password.enforce_complexity=on \
        --assign-inbound-public-ip=ASSIGN_IPV4 \
        --outbound-public-ip
    

## Enable public IP on an instance

To enable inbound connectivity using public IP, do the following:

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page that opens, go to the **Instances in your cluster** section, and locate your primary instance.

  4. Click more_vert **Instance actions** > **Edit**.

  5. Under **Connectivity** , select the **Enable Public IP** checkbox to support inbound connections.

  6. Optional: To restrict direct connections to specific IP addresses, under **Authorized external networks** , enter a comma-separated list of CIDR ranges.

For each CIDR range, enter a CIDR block, such as `64.233.160.0/16`. To minimize the potential attack surface, keep the list of addresses as small as possible.

  7. Click **Update instance** to save your changes.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to enable public IP on your instance.
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --database-flags=password.enforce_complexity=on \
        --assign-inbound-public-ip=ASSIGN_IPV4
    

Replace the following:

  * `INSTANCE_ID`: the ID of the instance that you are updating.
  * `CLUSTER_ID`: the ID of the cluster that contains the instance.
  * `REGION_ID`: the region where the cluster is located.



#### Optional: Add authorized external networks

To restrict direct connections to specific IP addresses, add a comma-separated list of CIDR ranges:
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --database-flags=password.enforce_complexity=on \
        --assign-inbound-public-ip=ASSIGN_IPV4 \
        --authorized-external-networks=CIDR_RANGE1,CIDR_RANGE2,...
    

Replace the following:

  * `CIDR_RANGE`: a comma-separated list of CIDR blocks, such as `64.233.160.0/16`. To minimize the potential attack surface, keep the list of addresses as small as possible.



## Disable public IP on an instance

When you disable public IP on your instance, AlloyDB removes the public IP address from your instance and clears the authorized networks list. Any inbound connections to your instance fail. Authorized external networks can only be used with public IP.

To disable public IP, do the following:

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page that opens, go to the **Instances in your cluster** section, and locate your primary instance.

  4. Click more_vert **Instance actions** > **Edit**.

  5. Under **Connectivity** , clear the **Enable Public IP** checkbox to stop inbound connections.

  6. Optional: Under **Authorized external networks** , delete the comma-separated CIDR ranges.

  7. Click **Update instance** to save your changes.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to disable public IP on your instance.
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --assign-inbound-public-ip=NO_PUBLIC_IP
    

Replace the following:

  * `INSTANCE_ID`: the ID of the instance that you are updating.
  * `CLUSTER_ID`: the ID of the cluster that contains the instance.
  * `REGION_ID`: the region where the cluster is located.



## Update the authorized external networks for an instance

You can update the list of authorized external networks on your instance at any time. Public IP must be enabled on your instance when updating the authorized external networks list.

Authorized external networks can't be added or removed individually, and the networks list is overridden each time the update list command is run. To update authorized external networks on your instance, you must provide a comma-separated list of all authorized external networks each time you want to add or remove a network. Each authorized external network must be in CIDR format.

**Note:** To limit the number and size of authorized networks, you can enforce a custom organization policy. For more information, see [Supported custom constraints and operations](https://docs.cloud.google.com/alloydb/docs/alloydb-custom-constraints#supported-custom-constraints-operations).

To update the list of authorized external networks on your instance, do the following:

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page that opens, go to the **Instances in your cluster** section, and locate your primary instance.

  4. Click more_vert **Instance actions** > **Edit**.

  5. Under **Authorized external networks** , enter a comma-separated list of CIDR ranges. For each CIDR range, enter a CIDR block, such as `64.233.160.0/16`. To minimize the potential attack surface, keep the list of addresses as small as possible.

  6. Click **Update instance** to save your changes.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to update the authorized external networks on your instance.
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --authorized-external-networks=CIDR_RANGE1,CIDR_RANGE2,...
    

Replace the following:

  * `INSTANCE_ID`: the ID of the instance that you are updating.
  * `CLUSTER_ID`: the ID of the cluster that contains the instance.
  * `REGION_ID`: the region where the cluster is located.
  * `CIDR_RANGE`: a comma-separated list of CIDR blocks, such as `64.233.160.0/16`. To minimize the potential attack surface, keep the list of addresses as small as possible.



## Add outbound connectivity to an instance

You can enable outbound public IP to establish a connection from your AlloyDB instance to external sources. AlloyDB generates two outbound public IP addresses that remain consistent until you disable outbound connectivity on your instance. You can only enable outbound public IP for primary and secondary instances.

To enable outbound public IP, do the following:

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page that opens, go to the **Instances in your cluster** section, and locate your primary instance.

  4. Click more_vert **Instance actions** > **Edit**.

  5. Under **Outbound Public IP Connectivity** , select the **Enable Outbound Public IP** checkbox to support outbound connections.

  6. Click **Update instance** to save your changes.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to enable outbound public IP on your instance.
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --outbound-public-ip
    

Replace the following:

  * `INSTANCE_ID`: the ID of the instance that you are adding outbound connectivity for.
  * `CLUSTER_ID`: the ID of the cluster that you are adding outbound connectivity for.
  * `REGION_ID`: the region where your cluster is located.



## View connectivity details for an instance

View the list of authorized external networks on your instance at any time and the assigned public IP address using the [`gcloud alloydb instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/describe) command. You can also view outbound public IP addresses, if you have enabled outbound connectivity on your instance.

To view the connectivity details, do the following:

###  Console 

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. Go to the **Connectivity** page, where you can view information about your public IP configuration, including **Public IP Connectivity** and **Outbound Public IP**.

To view your public IP information, you can also choose an instance from **Instances in your cluster** and then click **View connectivity configuration**.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).
    
    
    gcloud alloydb instances describe INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID
    

Replace the following:

  * `INSTANCE_ID`: the ID of the instance that you are viewing.
  * `CLUSTER_ID`: the ID of the cluster that contains the instance.
  * `REGION_ID`: the region where the cluster is located.



## What's next

  * [Connection overview](https://docs.cloud.google.com/alloydb/docs/connection-overview)
  * [Organization policies and custom constraints](https://docs.cloud.google.com/alloydb/docs/org-policy)
  * [Connect using the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect)
  * [Connect using AlloyDB Language Connectors](https://docs.cloud.google.com/alloydb/docs/language-connectors-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
