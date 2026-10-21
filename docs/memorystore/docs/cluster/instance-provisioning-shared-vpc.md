---
url: https://docs.cloud.google.com/memorystore/docs/cluster/instance-provisioning-shared-vpc/
title: Instance provisioning on a Shared VPC network \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:08.002364+00:00
---

# Instance provisioning on a Shared VPC network  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/instance-provisioning-shared-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Instance provisioning on a Shared VPC network Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the gcloud CLI commands needed to set up prerequisites, provision an instance in a service project, describe an instance, and delete an instance. In order to accomplish these tasks you should follow the instructions in each section of this page.

For more detailed guidance for these tasks, see the following pages:

  * [Networking](https://docs.cloud.google.com/memorystore/docs/cluster/networking)
  * [Create instances](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances)
  * [List instances](https://docs.cloud.google.com/memorystore/docs/cluster/list-instances)
  * [Delete clusters](https://docs.cloud.google.com/memorystore/docs/cluster/delete-instances)



## Enable APIs

Enable the following APIs needed for configuring a service connection policy, [configuring Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc), and creating a Memorystore for Redis Cluster instance.

### gcloud

  1. Enable the following APIs in the service project:
         
         gcloud services enable --project=SERVICE_PROJECT_ID networkconnectivity.googleapis.com
         gcloud services enable --project=SERVICE_PROJECT_ID serviceconsumermanagement.googleapis.com
         gcloud services enable --project=SERVICE_PROJECT_ID redis.googleapis.com
         

Replace the SERVICE_PROJECT_ID with your service project ID.

  2. Enable the following APIs in the host project:
         
         gcloud services enable --project=HOST_PROJECT_ID networkconnectivity.googleapis.com
         

Replace the HOST_PROJECT_ID with the ID of your host project.




## Create a service connection policy

Next, create a [service connection policy](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) for the host project of the Shared VPC network, region, and subnets where you want to provision the Memorystore for Redis Cluster instance. Usually this is done by your network administrator. However, you can also do this if you're assigned to the [required roles](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#roles) to run the command.

This quickstart uses the `default` network and `default` subnet.

### gcloud

  1. To create the service connection policy, run the `create` command:
         
         gcloud network-connectivity service-connection-policies create POLICY_NAME \
           --network=default \
           --project=HOST_PROJECT_ID \
           --region=REGION \
           --service-class=gcp-memorystore-redis \
           --subnets=https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/REGION/subnetworks/default
         

Replace the following:

     * POLICY_NAME is your desired policy name.
     * HOST_PROJECT_ID is the host project ID.
     * REGION is the same region where you want to provision your Memorystore for Redis Cluster instance.
  2. To validate if the policy was created successfully, run the `list` command:
         
         gcloud network-connectivity service-connection-policies list \
           --region=REGION \
           --project=HOST_PROJECT_ID
         

Replace the following:

     * HOST_PROJECT_ID is the host project ID.
     * REGION is the region where the service connection policy is defined.



## Create an instance

To create an instance in the service project that's attached to the Shared VPC network, run the following command:

### gcloud
    
    
    gcloud redis clusters create INSTANCE_ID \
    --project=SERVICE_PROJECT_ID \
    --region=REGION \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT \
    --replica-count=REPLICA_COUNT \
    --network=projects/HOST_PROJECT_ID/global/networks/default
    

Replace the following:

  * INSTANCE_ID is the instance ID.
  * SERVICE_PROJECT_ID is the service project ID.
  * REGION is the region where you want to provision your instance.

  * NODE_TYPE is the [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) that you want to use for the cluster.

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  * SHARD_COUNT determines the number of shards in your instance. Shard count determines the total memory capacity for storing cluster data. To see more details about cluster specification, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

  * REPLICA_COUNT is the number of read replicas (per shard). Accepted values are `0`-`5`.

  * HOST_PROJECT_ID is the host project ID.




## Describe the instance

To view instance details, run the following command:

### gcloud
    
    
    gcloud redis clusters describe INSTANCE_ID \
    --project=SERVICE_PROJECT_ID \
    --region=REGION
    

Replace the following:

  * INSTANCE_ID is the instance ID.
  * SERVICE_PROJECT_ID is the service project ID.
  * REGION is the region where your instance is located.



## Delete the instance

To delete an instance, run the following command:

### gcloud
    
    
    gcloud redis clusters delete INSTANCE_ID \
    --project=SERVICE_PROJECT_ID \
    --region=REGION
    

Replace the following:

  * INSTANCE_ID is the instance ID.
  * SERVICE_PROJECT_ID is the service project ID.
  * REGION is the region where your instance is located.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
