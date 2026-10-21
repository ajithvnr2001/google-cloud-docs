---
url: https://docs.cloud.google.com/memorystore/docs/valkey/instance-provisioning-vpc/
title: Instance provisioning on a VPC network \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:17.878517+00:00
---

# Instance provisioning on a VPC network  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/instance-provisioning-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Instance provisioning on a VPC network Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the gcloud CLI commands needed to set up prerequisites, provision an instance, describe an instance, and delete an instance on a standard VPC network. For instructions on performing these tasks on a Shared VPC network, see [Instance provisioning on a Shared VPC network](https://docs.cloud.google.com/memorystore/docs/valkey/instance-provisioning-shared-vpc). In order to accomplish these tasks you should follow the instructions in each section of this page.

For more detailed guidance for these tasks, see the following pages:

  * [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking)
  * [Create instances](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances)
  * [List instances](https://docs.cloud.google.com/memorystore/docs/valkey/list-instances)
  * [Delete instances](https://docs.cloud.google.com/memorystore/docs/valkey/delete-instances)



## Enable APIs

Begin by enabling the APIs in this section. These APIs are needed because Memorystore for Valkey uses Private Service Connect service connectivity automation to automate connectivity for instances. For more information, see [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking).

To enable the APIs, run the following commands:

### gcloud
    
    
    gcloud services enable --project=PROJECT_ID networkconnectivity.googleapis.com
    gcloud services enable --project=PROJECT_ID compute.googleapis.com
    gcloud services enable --project=PROJECT_ID serviceconsumermanagement.googleapis.com
    gcloud services enable --project=PROJECT_ID memorystore.googleapis.com
    

Replace the following:

  * PROJECT_ID is your project ID.



## Create a service connection policy

You must create a [service connection policy](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) for the project, network, and region where you want to provision the Memorystore for Valkey instance. A service connection policy lets you authorize the `gcp-memorystore` service class to create a Private Service Connect connection between producer and consumer VPC networks in the region where the policy is defined, and in the subnet that the policy specifies.

To see the permission needed to create a service connection policy, see [required roles](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#roles).

This quickstart uses the `default` network and `default` subnet. IP addresses for your instance are allocated on this default subnet in the region.

To create the service connection policy, run the following command:

### gcloud
    
    
    gcloud network-connectivity service-connection-policies create POLICY_NAME \
      --network=default \
      --project=PROJECT_ID \
      --region=REGION \
      --service-class=gcp-memorystore \
      --subnets=https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/default
    

Replace the following:

  * POLICY_NAME is your desired policy name.
  * PROJECT_ID is the project ID.
  * REGION is the same region where you want to provision your Memorystore for Valkey instance.



## Validate service connection policy creation

Validate if the policy was created successfully by running the `list` command:

### gcloud
    
    
    gcloud network-connectivity service-connection-policies list --region=REGION --project=PROJECT_ID
    

Replace the following:

  * PROJECT_ID is the project ID.
  * REGION is the region where the service connection policy is defined.



## Create an instance

To create an instance, run the `create` command:

### gcloud
    
    
    gcloud memorystore instances create INSTANCE \
    --project=PROJECT_ID \
    --location=REGION \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT \
    --replica-count=REPLICA_COUNT \
    --endpoints='[{"connections": [{"pscAutoConnection": {"network": "projects/PROJECT_ID/global/networks/NETWORK_ID", "projectId": "PROJECT_ID"}}]}]'
    

Replace the following:

  * INSTANCE is the instance ID.
  * REGION is the region where you want to provision your instance.

  * NODE_TYPE is the [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type) that you want to use for the instance.

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
  * SHARD_COUNT determines the number of shards in your instance. Shard count determines the total memory capacity for storing instance data. To see more details about instance specification, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

  * REPLICA_COUNT is the number of read replicas (per shard). Accepted values are `0`-`5`.

  * PROJECT_ID is the ID of the project where you want to create your instance.

  * NETWORK_ID is the ID of the network you want to use to create your instance.


**Note:** When running the `create` command you must use the same network and same region where the service connection policy is defined.

## Describe the instance

To view instance details, run the `describe` command:

### gcloud
    
    
    gcloud memorystore instances describe INSTANCE \
    --project=PROJECT_ID \
    --location=REGION
    

Replace the following:

  * INSTANCE is the instance ID.
  * PROJECT_ID is the project ID.
  * REGION is the region where your instance is located.



## Delete the instance

To delete an instance, run the `delete` command:

### gcloud
    
    
    gcloud memorystore instances delete INSTANCE \
    --project=PROJECT_ID \
    --location=REGION
    

Replace the following:

  * INSTANCE is the instance ID.
  * PROJECT_ID is the project ID.
  * REGION is the region where your instance is located.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
