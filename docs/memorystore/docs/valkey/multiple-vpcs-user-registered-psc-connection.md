---
url: https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection/
title: Set up multiple VPC networks using user-registered Private Service Connect connections \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:55:07.267384+00:00
---

# Set up multiple VPC networks using user-registered Private Service Connect connections  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Set up multiple VPC networks using user-registered Private Service Connect connections Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to set up connectivity for multiple Virtual Private Cloud (VPC) networks and a new Memorystore for Valkey instance. To do this, you do the following:

  * Create Private Service Connect endpoints in consumer networks.

  * Target the service attachments for your Memorystore instance.

  * Register the components with the instance.




For instructions on how to set up multiple VPC networking for an instance that already has some [automatically registered Private Service Connect connections](https://docs.cloud.google.com/memorystore/docs/valkey/about-multiple-vpc-networking#psc_connection_types), see [Set up multiple VPC networks for instances provisioned with automatically registered Private Service Connect connections](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-automatically-registered-psc-connection).

For more information about multiple VPC network setups, see [About multiple VPC networking](https://docs.cloud.google.com/memorystore/docs/valkey/about-multiple-vpc-networking).

![Multi vpc networking architecture. It has two customer VPC networks across two projects connected to a Private Service Connect connection, which is connected to the Memorystore service attachment.](https://docs.cloud.google.com/static/memorystore/img/mvc-multi-vpc.png)

## Summary of key steps

This section gives a summary of the key steps in this tutorial for setting up your Private Service Connect connections. First, complete the steps in [Before you begin](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#before_you_begin).

**Note:** The sample commands on this page are [`gcloud CLI`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore) commands. To find instructions and examples of using Terraform to perform these tasks, see the [google_memorystore_instance_desired_user_created_endpoints](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/memorystore_instance_desired_user_created_endpoints) page.

### Key steps

  1. [Step 1: Create an instance](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#step_1_create_an_instance)
  2. [Step 2: Note the service attachment paths](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#step_2_note_the_service_attachment_paths)
  3. [Step 3: Set up and register Private Service Connect connections for your first VPC network](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#step_3_set_up_and_register_psc_connections_for_your_first_vpc_network)
  4. [Step 4: Set up and register Private Service Connect connections for your second VPC network](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#step_4_set_up_and_register_psc_connections_for_your_second_vpc_network)
  5. [Step 5: Set up a client connection](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#step_5_set_up_a_client_connection)



Additionally, you can also:

  * [Delete your Private Service Connect connections](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#delete_your_psc_connections)
  * [Delete your Memorystore for Valkey instance](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#delete_your_memorystore_for_valkey_instance)



## Before you begin

Before you begin, ensure that you have the following IAM roles and Google Cloud resources.

**Important** : To use multiple VPC networking with Memorystore for Valkey, your instance must run a maintenance version of at least `MEMORYSTORE_20251210_02_00`. If your instance runs an older maintenance version, then you must perform a self-service update before you can add or use multiple connections. For more information about updating your instance to a newer maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/self-service-maintenance).

### Required IAM roles

Example resource ID | Resource type  
---|---  
[ `roles/memorystore.admin`](https://docs.cloud.google.com/memorystore/docs/valkey/access-control#predefined_roles) |  Provides full control of a Memorystore for Valkey instance and controls the instance over its lifecycle.   
[ `roles/servicedirectory.editor`](https://docs.cloud.google.com/service-directory/docs/access-control) |  Grants you permission to edit Service Directory resources. This role is needed for creating a Private Service Connect endpoint.   
[ `roles/compute.networkAdmin`](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) |  Grants full control over the VPC network that initiates a connection to a Memorystore instance. You can create and manage IP addresses, firewall rules, and [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints). This role is needed for creating a Private Service Connect endpoint.  
  
If you use Private Service Connect to connect to a Memorystore instance from multiple VPC networks, then each network may have its own administrator.   
  
### Prerequisite resources

You need to create the following resources before you begin this tutorial. We recommend creating the resources with the following IDs and locations, however you can also choose your own IDs and locations. In this tutorial, you will use the following resources to set up two Private Service Connect connections in VPC network 1:

Example resource ID | Resource type | Example full path | Description  
---|---|---|---  
`my-project-1` |  Google Cloud project  |  n/a  |  Your Memorystore instance is located in this project   
`my-network-1` |  VPC network  |  `projects/my-project-1/global/networks/my-network-1` |  In this tutorial, you set up 2 Private Service Connect connections in this network   
`my-subnet-1` |  VPC subnet  |  `projects/my-project-1/regions/us-central1/subnetworks/my-subnet-1 ` |  In this tutorial, you reserve 2 IP addresses in this subnet   
  
In this tutorial, you will use the following resources to create two Private Service Connect connections in VPC network 2:

Example resource ID | Resource type | Example full path | Description  
---|---|---|---  
`my-project-2` |  Google Cloud project  |  n/a  |  For this tutorial, this is the project where you create the second network and second subnetwork. However, the second network and subnet can be in the same project as the first network, if you choose.   
`my-network-2` |  VPC network  |  `projects/my-project-2/global/networks/my-network-2` |  In this tutorial, you create 2 Private Service Connect endpoints in this network   
`my-subnet-2` |  VPC subnet  |  `projects/my-project-2/regions/us-central1/subnetworks/my-subnet-2 ` |  In this tutorial, you reserve 2 IP addresses in this subnet   
  
### Enable APIs

Enable the following APIs needed for managing Compute Engine networking, Memorystore for Valkey, and Private Service Connect resources.

### gcloud

To enable the APIs in both project 1 and project 2, run the following commands:
    
    
    gcloud services enable --project=PROJECT_1_ID compute.googleapis.com
    gcloud services enable --project=PROJECT_2_ID compute.googleapis.com
    gcloud services enable --project=PROJECT_1_ID memorystore.googleapis.com
    gcloud services enable --project=PROJECT_2_ID memorystore.googleapis.com
    gcloud services enable --project=PROJECT_1_ID servicedirectory.googleapis.com
    gcloud services enable --project=PROJECT_2_ID servicedirectory.googleapis.com
    

## Step 1: Create an instance

This guide shows you how to set up connectivity for a Memorystore instance that has no [automatically registered Private Service Connect connections](https://docs.cloud.google.com/memorystore/docs/valkey/about-multiple-vpc-networking#psc_connection_types). It is acceptable to have a service connection policy, but a service connection policy isn't required when following the process for user-registering Private Service Connect connections.

To avoid automatically creating and registering Private Service Connect connections, run the create command without specifying a network, as seen in the following example.

### gcloud

To create an instance without auto-creating any Private Service Connect connections, run the `gcloud memorystore instances create` command, without using the `--network` or `--endpoints` parameter, as follows:
    
    
    gcloud memorystore instances create INSTANCE_ID \
    --location=REGION_ID \
    --project=PROJECT_1_ID \
    --replica-count=REPLICA_COUNT \
    --shard-count=SHARD_COUNT
    

Replace the following:

  * INSTANCE_ID is the ID of the Memorystore for Valkey instance you're creating. Your instance ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.

  * REGION_ID is the region where you want the instance placed.

  * PROJECT_1_ID is the ID of project 1. This is the project where your Memorystore instance is located.

  * REPLICA_COUNT is your chosen number of replicas (per shard). Accepted values are `0`, `1`, and `2`.

  * SHARD_COUNT determines the number of shards in your instance. Shard count determines the total memory capacity for storing instance data. To see more details about instance specification, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).




For example:
    
    
    gcloud memorystore instances create my-instance \
    --location=us-central1 \
    --replica-count=2 \
    --shard-count=8
    

## Step 2: Note the service attachment paths

After creating a Memorystore instance, make a note of the two service attachment URIs for your Memorystore instance. You use these service attachment URIs to set up Private Service Connect connections.

### gcloud

To view summary information about an instance with Private Service Connect enabled, look for the `pscServiceAttachments` field. This field displays the two URIs that point to the service attachments of the instance. To view this information, use the `gcloud memorystore instances describe` command:
    
    
    gcloud memorystore instances describe INSTANCE_ID --project=PROJECT_1_ID --location=REGION_ID
    

Replace the following:

  * INSTANCE_ID is the name of your Memorystore instance.
  * PROJECT_1_ID is the ID of Project 1 that contains the Memorystore instance.
  * REGION_ID is the ID of the region where your instance is located.



The following shows a sample output for this command:
    
    
    gcloud memorystore instances describe my-instance \
    --project=my-project-1 --location=us-central1
    
    ...
    
    pscAttachmentDetails:
    - connectionType: CONNECTION_TYPE_DISCOVERY
      serviceAttachment: projects/1048073346231/regions/us-central1/serviceAttachments/gcp-memorystore-auto-8d7d48ef-3ca3-4d-psc-sa
    - serviceAttachment: projects/1048073346231/regions/us-central1/serviceAttachments/gcp-memorystore-auto-8d7d48ef-3ca3-4d-psc-sa-2
    

## Step 3: Set up and register connections for your first VPC network

This section shows you how to set up the two Private Service Connect connections required for your first VPC network. You must repeat this process for every VPC for which you want to set up connectivity. For example, later in this tutorial you will find these steps repeated again, but for the new connections needed for the second VPC network.

### Create the Private Service Connect endpoints for network 1

This section explains the actions you need to take to create 2 Private Service Connect endpoints in Network 1.

#### Reserve IP addresses for network 1

Next, reserve two IP addresses in network 1.

##### Reserve IP address 1

### gcloud

To reserve IP address 1, run the `gcloud compute addresses create` command:
    
    
    gcloud compute addresses create IP_ADDRESS_1_ID \
    --project=PROJECT_1_ID \
    --addresses=IP_ADDRESS_1 \
    --region=REGION_ID \
    --subnet=projects/PROJECT_1_ID/regions/REGION_ID/subnetworks/SUBNET_1_ID \
    --purpose=GCE_ENDPOINT
    

Replace the following:

  * IP_ADDRESS_1_ID is the ID you give to your IP address.
  * PROJECT_1_ID is the ID of project 1. This is the project where your Memorystore instance is located.
  * IP_ADDRESS_1 is an IP address of your choosing from within the `SUBNET_1_ID` range you reserved as a part of [Prerequisite resources](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#prerequisite_resources).
  * REGION_ID is the region where your Memorystore instance is located.
  * SUBNET_1_ID is the ID of the subnetwork you reserved on network one in project 1 as a part of [Prerequisite resources](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#prerequisite_resources).



For example:
    
    
    gcloud compute addresses create my-ip-address-1 \
    --project=my-project-1 \
    --addresses=10.2.5.9 \
    --region=us-central1 \
    --subnet=projects/my-project-1/regions/us-central1/subnetworks/my-subnet-1 \
    --purpose=GCE_ENDPOINT
    

##### Reserve IP address 2

### gcloud

To reserve IP address 2, run the `gcloud compute addresses create` command:
    
    
    gcloud compute addresses create IP_ADDRESS_2_ID \
    --project=PROJECT_1_ID \
    --addresses=IP_ADDRESS_2 \
    --region=REGION_ID \
    --subnet=projects/PROJECT_1_ID/regions/REGION_ID/subnetworks/SUBNET_1_ID \
    --purpose=GCE_ENDPOINT
    

Replace the following:

  * IP_ADDRESS_2_ID is the ID you give to your IP address.
  * PROJECT_1_ID is the ID of project 1. This is the project where your Memorystore instance is located.
  * IP_ADDRESS_2 is an IP address of your choosing from within the `SUBNET_1_ID` range you reserved as a part of [Prerequisite resources](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#prerequisite_resources).
  * REGION_ID is the region where your Memorystore instance is located.
  * SUBNET_1_ID is the ID of the subnetwork you reserved on network 1 in project 1 as a part of [Prerequisite resources](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#prerequisite_resources).



#### Add forwarding rules for network 1

Next, create forwarding rules that connect the IP addresses to the Memorystore instance's service attachments.

##### Add forwarding rule 1 for IP 1

### gcloud

To add a forwarding rule for IP 1, run the `gcloud compute forwarding-rules create` command:
    
    
    gcloud compute forwarding-rules create FORWARDING_RULE_1_NAME \
    --address=IP_ADDRESS_1_ID \
    --network=projects/PROJECT_1_ID/global/networks/NETWORK_1_ID \
    --region=REGION_ID \
    --target-service-attachment=SERVICE_ATTACHMENT_1 \
    --project=PROJECT_1_ID \
    --allow-psc-global-access
    

Replace the following:

  * FORWARDING_RULE_1_NAME is the name you give to the forwarding rule you are creating.
  * IP_ADDRESS_1_ID is the ID of the IP address you reserved in the [Reserve IP addresses](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#reserve_ip_addresses_for_network_1) section.
  * NETWORK_1_ID is the ID of your first network.
  * REGION_ID is the region where your Memorystore instance is located.
  * SERVICE_ATTACHMENT_1 is the service attachment you noted in [Note the service attachment paths](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#step_2_note_the_service_attachment_paths) listed after the `CONNECTION_TYPE_DISCOVERY` field.
  * PROJECT_1_ID is the ID of project 1. This is the project where your Memorystore instance is located.

By using the optional [\--allow-psc-global-access](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--allow-psc-global-access) parameter, clients from all Memorystore for Valkey supported regions can access this forwarding rule.

For example:
    
    
    gcloud compute forwarding-rules create my-forwarding-rule-1 \
    --address=my-ip-address-1 \
    --network=projects/my-project-1/global/networks/my-network-1 \
    --region=us-central1 \
    --target-service-attachment=projects/1048073346231/regions/us-central1/serviceAttachments/gcp-memorystore-auto-a0583920-edef-42-psc-sa \
    --project=my-project-1 \
    --allow-psc-global-access
    

##### Add forwarding rule 2 for IP 2

### gcloud

To add a forwarding rule for IP 2, run the `gcloud compute forwarding-rules create` command:
    
    
    gcloud compute forwarding-rules create FORWARDING_RULE_2_NAME \
    --address=IP_ADDRESS_2_ID \
    --network=projects/PROJECT_1_ID/global/networks/NETWORK_1_ID \
    --region=REGION_ID \
    --target-service-attachment=SERVICE_ATTACHMENT_2 \
    --project=PROJECT_1_ID \
    --allow-psc-global-access
    

Replace the following:

  * FORWARDING_RULE_2_NAME is the name you give to the forwarding rule you are creating.
  * IP_ADDRESS_2_ID is the ID of the IP address you reserved in the [Reserve IP addresses](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#reserve_ip_addresses_for_network_1) section.
  * NETWORK_1_ID is the ID of your first network.
  * REGION_ID is the region where your Memorystore instance is located.
  * SERVICE_ATTACHMENT_2 is the second service attachment you noted in [Note the service attachment paths](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#step_2_note_the_service_attachment_paths).
  * PROJECT_1_ID is the ID of project 1. This is the project where your Memorystore instance is located.

By using the optional [\--allow-psc-global-access](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--allow-psc-global-access) parameter, clients from all Memorystore for Valkey supported regions can access this forwarding rule.

For example:
    
    
    gcloud compute forwarding-rules create my-forwarding-rule-2 \
    --address=my-ip-address-2 \
    --network=projects/my-project-1/global/networks/my-network-1 \
    --region=us-central1 \
    --target-service-attachment=projects/1048073346231/regions/us-central1/serviceAttachments/gcp-memorystore-auto-a0583920-edef-42-psc-sa-2 \
    --project=my-project-1 \
    --allow-psc-global-access
    

### Register Private Service Connect connections with your Memorystore instance for network 1

This section shows the steps to follow to register Private Service Connect connections with your Memorystore instance. First, you need to get the connection IDs and project IDs of your forwarding rules.

Then, you will enable connectivity by registering the Private Service Connect connection information with your Memorystore instance.

#### Get the forwarding rule connection IDs and project IDs for network 1

Next, get the `pscConnectionId` value for each forwarding rule. Make a note of the values.

##### Get Private Service Connect connection ID 1

### gcloud

To see the `pscConnectionId` value and other forwarding rule summary information, run the `gcloud compute forwarding-rules describe` command:
    
    
    gcloud compute forwarding-rules describe FORWARDING_RULE_1_NAME \
    --project=PROJECT_1_ID \
    --region=REGION_ID
    

Replace the following:

  * FORWARDING_RULE_1_NAME is the name of your first forwarding rule.
  * PROJECT_1_ID is the ID of the Google Cloud project that contains the forwarding rule.



The following example shows a sample output for this command:
    
    
    gcloud compute forwarding-rules describe my-forwarding-rule-1 \
    --project=my-project-1 \
    --region=us-central1
    
    ...
    
    pscConnectionId: '415109836469698'
    

##### Get Private Service Connect connection ID 2

### gcloud

To see the `pscConnectionId` value and other forwarding rule summary information, run the `gcloud compute forwarding-rules describe` command:
    
    
    gcloud compute forwarding-rules describe FORWARDING_RULE_2_NAME \
    --project=PROJECT_1_ID \
    --region=REGION_ID
    

Replace the following:

  * FORWARDING_RULE_2_NAME is the name of your second forwarding rule.
  * PROJECT_1_ID is the ID of the Google Cloud project that contains the forwarding rule.



#### Register connection information for VPC network 1

### gcloud

To register each Private Service Connect connection, you'll provide the Private Service Connect connection ID, IP address, network path, forwarding rule path/URI, and the target service attachment. Do this by running the `gcloud memorystore instances update --add-endpoints` command:
    
    
      gcloud memorystore instances update INSTANCE_ID \
       --location=REGION_ID \
       --project=PROJECT_1_ID \
       --add-endpoints='[{"connections":[{"pscConnection":{"pscConnectionId":"PSC_CONNECTION_1_ID","ipAddress":"IP_ADDRESS_1","network":"projects/PROJECT_1_ID/global/networks/NETWORK_1_ID","forwardingRule":"projects/PROJECT_1_ID/regions/REGION_ID/forwardingRules/FORWARDING_RULE_1_NAME","serviceAttachment":"SERVICE_ATTACHMENT_1"}}, {"pscConnection":{"pscConnectionId":"PSC_CONNECTION_2_ID","ipAddress":"IP_ADDRESS_2","network":"projects/PROJECT_1_ID/global/networks/NETWORK_1_ID","forwardingRule":"projects/PROJECT_1_ID/regions/REGION_ID/forwardingRules/FORWARDING_RULE_2_NAME","serviceAttachment":"SERVICE_ATTACHMENT_2"}}]}]'
      

Replace the following:

  * INSTANCE_ID is the ID of your Memorystore for Valkey instance.
  * REGION_ID is the ID of the region where your Memorystore instance is located.
  * PROJECT_1_ID is the ID of project 1. This is the project where your Memorystore instance is located.
  * PSC_CONNECTION_1_ID is the first Private Service Connect connection ID you noted when [Getting forwarding rule connection IDs](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#get_the_forwarding_rule_connection_ids_and_project_ids_for_network_1).
  * IP_ADDRESS_1 is the address of the first IP address you reserved.
  * NETWORK_1_ID is the ID of Network 1.
  * FORWARDING_RULE_1_NAME is the name of the first forwarding rule you created.
  * SERVICE_ATTACHMENT_1 is your first service attachment that `FORWARDING_RULE_1_NAME` is connected with.
  * PSC_CONNECTION_2_ID is the second Private Service Connect connection ID you noted when [Getting forwarding rule connection IDs](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#get_the_forwarding_rule_connection_ids_and_project_ids_for_network_1).
  * IP_ADDRESS_2 is the address of the second IP address you reserved.
  * FORWARDING_RULE_2_NAME is the name of the second forwarding rule you created.
  * SERVICE_ATTACHMENT_2 is your second service attachment that `FORWARDING_RULE_2_NAME` is connected with.

For example:
        
        gcloud memorystore instances update my-instance \
        --location=us-central-1 \
        --project=my-project-1 \
        --add-endpoints='[{"connections":[{"pscConnection":{"pscConnectionId":"41510983646969883","ipAddress":"10.2.5.9","network":"projects/my-project-1/global/networks/my-network-1","forwardingRule":"projects/my-project-1/regions/us-central1/forwardingRules/my-forwarding-rule-1","serviceAttachment":"projects/1048073346231/regions/us-central1/serviceAttachments/gcp-memorystore-auto-8d7d48ef-3ca3-4d-psc-sa"}}, {"pscConnection":{"pscConnectionId":"41510983646969234","ipAddress":"10.2.5.11","network":"projects/my-project-1/global/networks/my-network-1","forwardingRule":"projects/my-project-1/regions/us-central1/forwardingRules/my-forwarding-rule-2","serviceAttachment":"projects/1048073346231/regions/us-central1/serviceAttachments/gcp-memorystore-auto-8d7d48ef-3ca3-4d-psc-sa-2"}}]}]'
        




## Step 4: Set up and register connections for your second VPC network

This section shows you how to set up the two Private Service Connect connections required for your second VPC network.

### Create the Private Service Connect endpoints for network 2

This section explains the actions you need to take to create 2 Private Service Connect endpoints in Network 2.

#### Reserve IP addresses for network 2

Next, reserve 2 IP addresses in network 2.

##### Reserve IP address 3

### gcloud

To reserve IP address 3, run the `gcloud compute addresses create` command:
    
    
    gcloud compute addresses create IP_ADDRESS_3_ID \
    --project=PROJECT_2_ID \
    --addresses=IP_ADDRESS_3 \
    --region=REGION_ID \
    --subnet=projects/PROJECT_2_ID/regions/REGION_ID/subnetworks/SUBNET_2_ID \
    --purpose=GCE_ENDPOINT
    

Replace the following:

  * IP_ADDRESS_3_ID is the ID you give to your IP address.
  * PROJECT_2_ID is the ID of project 2. This is the project where you create the second VPC network and subnetwork.
  * IP_ADDRESS_3 is an IP address of your choosing from within the `SUBNET_2_ID` range you reserved as a part of [Prerequisite resources](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#prerequisite_resources).
  * REGION_ID is the region where your Memorystore instance is located.
  * SUBNET_2_ID is the ID of the subnetwork you reserved on network 2 in project 2 as a part of [Prerequisite resources](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#prerequisite_resources).



##### Reserve IP address 4

### gcloud

To reserve IP address 4, run the `gcloud compute addresses create` command:
    
    
    gcloud compute addresses create IP_ADDRESS_4_ID \
    --project=PROJECT_2_ID \
    --addresses=IP_ADDRESS_4 \
    --region=REGION_ID \
    --subnet=projects/PROJECT_2_ID/regions/REGION_ID/subnetworks/SUBNET_2_ID \
    --purpose=GCE_ENDPOINT
    

Replace the following:

  * IP_ADDRESS_4_ID is the ID you give to your IP address.
  * PROJECT_2_ID is the ID of project 2. This is the project where you create the second VPC network and subnetwork.
  * IP_ADDRESS_4 is an IP address of your choosing from within the `SUBNET_2_ID` range you reserved as a part of [Prerequisite resources](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#prerequisite_resources).
  * REGION_ID is the region where your Memorystore instance is located.
  * SUBNET_2_ID is the ID of the subnetwork you reserved on network 2 in project 2 as a part of [Prerequisite resources](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#prerequisite_resources).



#### Add forwarding rules for network 2

Next, create forwarding rules that connect the IP addresses to the Memorystore instance's service attachments.

##### Add forwarding rule 3 for IP 3

### gcloud

To add a forwarding rule for IP 3, run the `gcloud compute forwarding-rules create` command:
    
    
    gcloud compute forwarding-rules create FORWARDING_RULE_3_NAME \
    --address=IP_ADDRESS_3_ID \
    --network=projects/PROJECT_2_ID/global/networks/NETWORK_2_ID \
    --region=REGION_ID \
    --target-service-attachment=SERVICE_ATTACHMENT_1 \
    --project=PROJECT_2_ID \
    --allow-psc-global-access
    

Replace the following:

  * FORWARDING_RULE_3_NAME is the name you give to the forwarding rule you are creating.
  * IP_ADDRESS_3_ID is the ID of the IP address you reserved in the [Reserve IP addresses](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#reserve_ip_addresses_for_network_2) section.
  * NETWORK_2_ID is the ID of your second network.
  * REGION_ID is the region where your Memorystore instance is located.
  * SERVICE_ATTACHMENT_1 is the first service attachment you noted in [Note the service attachment paths](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#step_2_note_the_service_attachment_paths).
  * PROJECT_2_ID is your second project.

By using the optional [\--allow-psc-global-access](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--allow-psc-global-access) parameter, clients from all Memorystore for Valkey supported regions can access this forwarding rule.

For example:
    
    
    gcloud compute forwarding-rules create my-forwarding-rule-3 \
    --address=my-ip-address-3 \
    --network=projects/my-project-2/global/networks/my-network-2 \
    --region=us-central1 \
    --target-service-attachment=projects/1048073346231/regions/us-central1/serviceAttachments/gcp-memorystore-auto-a0583920-edef-42-psc-sa \
    --project=my-project-2 \
    --allow-psc-global-access
    

##### Add forwarding rule 4 for IP 4

### gcloud

To add a forwarding rule for IP 4, run the `gcloud compute forwarding-rules create` command:
    
    
    gcloud compute forwarding-rules create FORWARDING_RULE_4_NAME \
    --address=IP_ADDRESS_4_ID \
    --network=projects/PROJECT_2_ID/global/networks/NETWORK_2_ID \
    --region=REGION_ID \
    --target-service-attachment=SERVICE_ATTACHMENT_2 \
    --project=PROJECT_2_ID \
    --allow-psc-global-access
    

Replace the following:

  * FORWARDING_RULE_4_NAME is the name you give to the forwarding rule you are creating.
  * IP_ADDRESS_4_ID is the ID of the IP address you reserved in the [Reserve IP addresses](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#reserve_ip_addresses_for_network_2) section.
  * NETWORK_2_ID is the ID of your second network.
  * REGION_ID is the region where your Memorystore instance is located.
  * SERVICE_ATTACHMENT_2 is the second service attachment you noted in [Note the service attachment paths](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#step_2_note_the_service_attachment_paths).
  * PROJECT_2_ID is your second project.

By using the optional [\--allow-psc-global-access](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--allow-psc-global-access) parameter, clients from all Memorystore for Valkey supported regions can access this forwarding rule.

For example:
    
    
    gcloud compute forwarding-rules create my-forwarding-rule-4 \
    --address=my-ip-address-4 \
    --network=projects/my-project-2/global/networks/my-network-2 \
    --region=us-central1 \
    --target-service-attachment=projects/1048073346231/regions/us-central1/serviceAttachments/gcp-memorystore-auto-a0583920-edef-42-psc-sa-2 \
    --project=my-project-2 \
    --allow-psc-global-access
    

### Register Private Service Connect connections with your Memorystore instance for network 2

This section shows the steps to follow to register Private Service Connect connections with your Memorystore instance. First, you need to get the connection IDs and project IDs of your forwarding rules.

#### Get the forwarding rule connection IDs and project IDs for network 2

Next, get the `pscConnectionId` value for each forwarding rule. Make a note of the values.

##### Get Private Service Connect connection ID 3

### gcloud

To see the `pscConnectionId` value and other forwarding rule summary information, run the `gcloud compute forwarding-rules describe` command:
    
    
    gcloud compute forwarding-rules describe FORWARDING_RULE_3_NAME \
    --project=PROJECT_2_ID \
    --region=REGION_ID
    

Replace the following:

  * FORWARDING_RULE_3_NAME is the name of your third forwarding rule.
  * PROJECT_2_ID is the ID of the Google Cloud project that contains the forwarding rule.



The following example shows a sample output for this command:
    
    
    gcloud compute forwarding-rules describe my-forwarding-rule-3 \
    --project=my-project-2 \
    --region=us-central1
    
    ...
    
    pscConnectionId: '94710983646969729'
    

##### Get Private Service Connect connection ID 4

### gcloud

To see the `pscConnectionId` value and other forwarding rule summary information, run the `gcloud compute forwarding-rules describe` command:
    
    
    gcloud compute forwarding-rules describe FORWARDING_RULE_4_NAME \
    --project=PROJECT_2_ID \
    --region=REGION_ID
    

Replace the following:

  * FORWARDING_RULE_4_NAME is the name of your fourth forwarding rule.
  * PROJECT_2_ID is the ID of the Google Cloud project that contains the forwarding rule.



#### Register Private Service Connect connection information for VPC network 2

### gcloud

To register each Private Service Connect connection, you'll provide the Private Service Connect connection ID, IP address, network path, forwarding rule path/URI, and the target service attachment. Do this by running the `gcloud memorystore instances update --add-endpoints` command:
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --location=REGION_ID \
    --project=PROJECT_1_ID \
    --add-endpoints='[{"connections":[{"pscConnection":{"pscConnectionId":"PSC_CONNECTION_3_ID","ipAddress":"IP_ADDRESS_3","network":"projects/PROJECT_2_ID/global/networks/NETWORK_2_ID","forwardingRule":"projects/PROJECT_2_ID/regions/REGION_ID/forwardingRules/FORWARDING_RULE_3_NAME","serviceAttachment":"SERVICE_ATTACHMENT_1"}}, {"pscConnection":{"pscConnectionId":"PSC_CONNECTION_4_ID","ipAddress":"IP_ADDRESS_4","network":"projects/PROJECT_2_ID/global/networks/NETWORK_2_ID","forwardingRule":"projects/PROJECT_2_ID/regions/REGION_ID/forwardingRules/FORWARDING_RULE_4_NAME","serviceAttachment":"SERVICE_ATTACHMENT_2"}}]}]'
    

Replace the following:

  * INSTANCE_ID is the ID of your Memorystore for Valkey instance.
  * REGION_ID is the ID of the region where your Memorystore instance is located.
  * PROJECT_1_ID is the ID of project 1. This is the project where your Memorystore instance is located.
  * PROJECT_2_ID is the ID of project 2. This is the project where you create the second VPC network and subnetwork.
  * PSC_CONNECTION_3_ID is the Private Service Connect connection 3 you noted when [Getting forwarding rule connection IDs for network 2](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#get_the_forwarding_rule_connection_ids_and_project_ids_for_network_2).
  * IP_ADDRESS_3 is the address of the third IP address you reserved.
  * NETWORK_2_ID is the ID of Network 2.
  * FORWARDING_RULE_3_NAME is the name of the third forwarding rule you created.
  * SERVICE_ATTACHMENT_1 is your first service attachment that `FORWARDING_RULE_3_NAME` is connected with.
  * PSC_CONNECTION_4_ID is the Private Service Connect connection 4 you noted when [Getting forwarding rule connection ID for network 2](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#get_the_forwarding_rule_connection_ids_and_project_ids_for_network_2).
  * IP_ADDRESS_4 is the address of the fourth IP address you reserved.
  * FORWARDING_RULE_4_NAME is the name of the fourth forwarding rule you created.
  * SERVICE_ATTACHMENT_2 is your second service attachment that `FORWARDING_RULE_4_NAME` is connected with.



For example:
    
    
    gcloud memorystore instances my-instance \
    --location=us-central-1 \
    --project=my-project-1 \
    --add-endpoints='[{"connections":[{"pscConnection":{"pscConnectionId":"94710983646969729","ipAddress":"10.142.0.10","network":"projects/my-project-2/global/networks/my-network-2","forwardingRule":"projects/my-project-2/regions/us-central1/forwardingRules/my-forwarding-rule-3","serviceAttachment":"projects/1048073346231/regions/us-central1/serviceAttachments/gcp-memorystore-auto-8d7d48ef-3ca3-4d-psc-sa"}}, {"pscConnection":{"pscConnectionId":"86510983646969993","ipAddress":"10.142.0.12","network":"projects/my-project-2/global/networks/my-network-2","forwardingRule":"projects/my-project-2/regions/us-central1/forwardingRules/my-forwarding-rule-4","serviceAttachment":"projects/1048073346231/regions/us-central1/serviceAttachments/gcp-memorystore-auto-8d7d48ef-3ca3-4d-psc-sa-2"}}]}]'
    

## Step 5: Set up a client connection

This section explains how to configure your client for connectivity for the networks in this guide.

### Make a note of Private Service Connect connection endpoint information

Next, make a note of two IP addresses: one for each network you set up in this tutorial. Each network you set up for Memorystore has a discovery connection endpoint.

### gcloud

To view Private Service Connect connection endpoint information for your networks, run the `gcloud memorystore instances describe` command:
    
    
    gcloud memorystore instances describe INSTANCE_ID \
    --location=REGION_ID \
    --project=PROJECT_1_ID
    

The output contains a list of `Endpoints`. For each `Endpoint`, there are two user-registered Private Service Connect connections.

Make a note of the IP addresses that correspond with the Private Service Connect connections that have the `CONNECTION_TYPE_DISCOVERY` type. For these connections, Memorystore for Valkey adds a `port` field.

For this tutorial, there's one `CONNECTION_TYPE_DISCOVERY` type for each of the two networks that you set up.

For example, here is a piece of sample output from the `gcloud memorystore instances describe` command that contains the IP address you should write down:
    
    
    Endpoints:
    - connections:
      - pscConnection:
          forwardingRule: projects/my-project-1/regions/us-east1/forwardingRules/multivpc-test-auto-network-tls-us-east1-fr1
          ipAddress: 10.x.x.x
          network: projects/my-project-1/global/networks/default
          projectId: my-project-1
          pscConnectionId: '36424170410479572'
          pscConnectionStatus: ACTIVE
          serviceAttachment: projects/606617939844/regions/us-east1/serviceAttachments/gcp-memorystore-auto-187b9c64-0f82-49-psc-sa-2
      - pscConnection:
          connectionType: CONNECTION_TYPE_DISCOVERY
          forwardingRule: projects/my-project-1/regions/us-east1/forwardingRules/multivpc-test-auto-network-tls-us-east1-fr2
          ipAddress: 10.x.x.x
          network: projects/my-project-1/global/networks/default
          port: 6379
          projectId: my-project-1
          pscConnectionId: '36424170410479573'
          pscConnectionStatus: ACTIVE
          serviceAttachment: projects/606617939844/regions/us-east1/serviceAttachments/gcp-memorystore-auto-187b9c64-0f82-49-psc-sa
    

To get the discovery IP address in the endpoints list, look for the `CONNECTION_TYPE_DISCOVERY` connection type.

### Configure your client

Next, configure your client as follows:

  * Configure client connections in network 1 using the discovery IP in network 1. This is the IP address you noted in the previous step. For the example given in this tutorial, the value is `10.2.5.9`.

  * Configure client connections in network 2 using the discovery IP in network 2. This is the IP address you noted in the previous step. For the example given in this tutorial, the value is `10.142.0.10`.




For instructions on connecting to a Memorystore instance, see [Connect from a Compute Engine VM using valkey-cli](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance#connect_from_a_compute_engine_vm_using_valkey_cli).

### Allow ports on your firewall

If you don't allow the correct ports on your firewall, then your instance might encounter connection errors because the firewall might block the ports that Memorystore for Valkey uses.

For all of your instance's Private Service Connect endpoints, you must allow TCP port 6379, as well as TCP ports 11000 through 13047. For more information, see [Troubleshoot issues](https://docs.cloud.google.com/memorystore/docs/valkey/troubleshoot-issues#connection_error_caused_by_firewall_rules).

## Delete your Private Service Connect connections

Before you can [Delete your Memorystore instance](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#delete_your_memorystore_for_valkey_instance), you must delete all Private Service Connect connections associated with the instance. To do this, you must delete the forwarding rules and deregister the endpoints that you set up in this tutorial. This section guides you through deleting all of the forwarding rules first, then deregistering the endpoints. However, if you choose, you can delete forwarding rules and deregister endpoints for one network at a time.

Also, you can optionally delete the reserved IP addresses to release them for future use if you choose.

### Delete forwarding rules

This section gives instructions on deleting the forwarding rules you created previously in this tutorial.

#### Delete forwarding rule 1

### gcloud

To delete a forwarding rule, run the [`gcloud compute forwarding-rules delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/delete) command:
    
    
    gcloud compute forwarding-rules delete FORWARDING_RULE_1_NAME \
    --region=REGION_ID \
    --project=PROJECT_1_ID
    

Replace the following:

  * FORWARDING_RULE_1_NAME is the name of your first forwarding rule.
  * PROJECT_1_ID is the ID of project 1. This is the project where your Memorystore instance is located.



#### Delete forwarding rule 2

### gcloud

To delete a forwarding rule, run the [`gcloud compute forwarding-rules delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/delete) command:
    
    
    gcloud compute forwarding-rules delete FORWARDING_RULE_2_NAME \
    --region=REGION_ID \
    --project=PROJECT_1_ID
    

Replace the following:

  * FORWARDING_RULE_2_NAME is the name of your second forwarding rule.
  * PROJECT_1_ID is the ID of project 1. This is the project where your Memorystore instance is located.



#### Delete forwarding rule 3

### gcloud

To delete a forwarding rule, run the [`gcloud compute forwarding-rules delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/delete) command:
    
    
    gcloud compute forwarding-rules delete FORWARDING_RULE_3_NAME \
    --region=REGION_ID \
    --project=PROJECT_2_ID
    

Replace the following:

  * FORWARDING_RULE_3_NAME is the name of your third forwarding rule.
  * PROJECT_2_ID is the ID of project 2. This is the project where you create the second VPC network and subnetwork.



#### Delete forwarding rule 4

### gcloud

To delete a forwarding rule, run the [`gcloud compute forwarding-rules delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/delete) command:
    
    
    gcloud compute forwarding-rules delete FORWARDING_RULE_4_NAME \
    --region=REGION_ID \
    --project=PROJECT_2_ID
    

Replace the following:

  * FORWARDING_RULE_4_NAME is the name of your fourth forwarding rule.
  * PROJECT_2_ID is the ID of project 2. This is the project where you create the second VPC network and subnetwork.



### Deregister your Private Service Connect endpoints

This section provides instructions for deregistering the Private Service Connect endpoints that you [registered earlier in this tutorial](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#register_psc_connection_information_for_vpc_network_1).

#### Deregister endpoints for VPC networks 1 and 2

### gcloud

To deregister the endpoint information with the Memorystore instance, run the `gcloud memorystore instances update --remove-endpoints` command.
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --location=REGION_ID \
    --project=PROJECT_1_ID \
    --remove-endpoints='[{"connections":[{"pscConnection":{"pscConnectionId":"PSC_CONNECTION_1_ID","ipAddress":"IP_ADDRESS_1","network":"projects/PROJECT_1_ID/global/networks/NETWORK_1_ID","forwardingRule":"projects/PROJECT_1_ID/regions/REGION_ID/forwardingRules/FORWARDING_RULE_1_NAME","serviceAttachment":"SERVICE_ATTACHMENT_1"}}, {"pscConnection":{"pscConnectionId":"PSC_CONNECTION_2_ID","ipAddress":"IP_ADDRESS_2","network":"projects/PROJECT_1_ID/global/networks/NETWORK_1_ID","forwardingRule":"projects/PROJECT_1_ID/regions/REGION_ID/forwardingRules/FORWARDING_RULE_2_NAME","serviceAttachment":"SERVICE_ATTACHMENT_2"}}]}, {"connections":[{"pscConnection":{"pscConnectionId":"PSC_CONNECTION_3_ID","ipAddress":"IP_ADDRESS_3","network":"projects/PROJECT_2_ID/global/networks/NETWORK_2_ID","forwardingRule":"projects/PROJECT_2_ID/regions/REGION_ID/forwardingRules/FORWARDING_RULE_3_NAME","serviceAttachment":"SERVICE_ATTACHMENT_1"}}, {"pscConnection":{"pscConnectionId":"PSC_CONNECTION_4_ID","ipAddress":"IP_ADDRESS_4","network":"projects/PROJECT_2_ID/global/networks/NETWORK_2_ID","forwardingRule":"projects/PROJECT_2_ID/regions/REGION_ID/forwardingRules/FORWARDING_RULE_4_NAME","serviceAttachment":"SERVICE_ATTACHMENT_2"}}]}]'
    

Replace the following:

  * INSTANCE_ID is the ID of the instance for which you are deregistering endpoints.
  * PROJECT_1_ID is the ID of project 1. This is the project where your Memorystore instance is located.
  * REGION_ID is the ID of the region where your Memorystore instance is located.
  * PSC_CONNECTION_1_ID is the first Private Service Connect connection ID you noted when [Getting forwarding rule connection IDs](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#get_the_forwarding_rule_connection_ids_and_project_ids_for_network_1).
  * IP_ADDRESS_1 is the address of the first IP address you reserved.
  * NETWORK_1_ID is the ID of Network 1.
  * FORWARDING_RULE_1_NAME is the name of the first forwarding rule you created.
  * SERVICE_ATTACHMENT_1 is your first service attachment that `FORWARDING_RULE_1_NAME` is connected with.
  * PSC_CONNECTION_2_ID is the second Private Service Connect connection ID you noted when [Getting forwarding rule connection IDs](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#get_the_forwarding_rule_connection_ids_and_project_ids_for_network_1).
  * IP_ADDRESS_2 is the address of the second IP address you reserved.
  * FORWARDING_RULE_2_NAME is the name of the second forwarding rule you created.
  * SERVICE_ATTACHMENT_2 is your second service attachment that `FORWARDING_RULE_2_NAME` is connected with.
  * PROJECT_2_ID is the ID of project 2. This is the project where you create the second VPC network and subnetwork.
  * PSC_CONNECTION_3_ID is the Private Service Connect connection 3 you noted when [Getting forwarding rule connection IDs for network 2](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#get_the_forwarding_rule_connection_ids_and_project_ids_for_network_2).
  * IP_ADDRESS_3 is the address of the third IP address you reserved.
  * NETWORK_2_ID is the ID of Network 2.
  * FORWARDING_RULE_3_NAME is the name of the third forwarding rule you created.
  * SERVICE_ATTACHMENT_1 is your first service attachment that `FORWARDING_RULE_3_NAME` is connected with.
  * PSC_CONNECTION_4_ID is the Private Service Connect connection 4 you noted when [Getting forwarding rule connection ID for network 2](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#get_the_forwarding_rule_connection_ids_and_project_ids_for_network_2).
  * IP_ADDRESS_4 is the address of the fourth IP address you reserved.
  * FORWARDING_RULE_4_NAME is the name of the fourth forwarding rule you created.
  * SERVICE_ATTACHMENT_2 is your second service attachment that `FORWARDING_RULE_4_NAME` is connected with.



The preceding command deregisters all connections created in this tutorial. If you want to only deregister one of the connections, only specify the connection IDs of the connections you want to remove.

## Delete your Memorystore for Valkey instance

Before you can delete your Memorystore instance, you must [Deregister your Private Service Connect endpoints](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#deregister_your_private_service_connect_endpoints).

### gcloud

To delete your Memorystore for Valkey instance, run the `gcloud memorystore instances delete` command:
    
    
    gcloud memorystore instances delete INSTANCE_ID \
    --location=REGION_ID \
    --project=PROJECT_1_ID
    

Replace the following:

  * INSTANCE_ID is the ID of your instance.
  * REGION_ID is the ID of the region where your Memorystore instance is located.
  * PROJECT_1_ID is the ID of project 1. This is the project where your Memorystore instance is located.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
