---
url: https://docs.cloud.google.com/memorystore/docs/valkey/instance-provisioning-shared-vpc/
title: Instance provisioning on a Shared VPC network \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:17.455737+00:00
---

# Instance provisioning on a Shared VPC network  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/instance-provisioning-shared-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Instance provisioning on a Shared VPC network Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the gcloud CLI commands needed to set up prerequisites, provision an instance in a service project, describe an instance, and delete an instance. In order to accomplish these tasks you should follow the instructions in each section of this page.

For more detailed guidance for these tasks, see the following pages:

  * [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking)
  * [Create instances](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances)
  * [List instances](https://docs.cloud.google.com/memorystore/docs/valkey/list-instances)
  * [Delete instances](https://docs.cloud.google.com/memorystore/docs/valkey/delete-instances)



## Enable APIs

Enable the following APIs needed for configuring a service connection policy, [configuring Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc), and creating a Memorystore for Valkey instance.

### gcloud

  1. Enable the following APIs in the service project:
         
         gcloud services enable --project=SERVICE_PROJECT_ID networkconnectivity.googleapis.com
         gcloud services enable --project=SERVICE_PROJECT_ID serviceconsumermanagement.googleapis.com
         gcloud services enable --project=SERVICE_PROJECT_ID memorystore.googleapis.com
         

Replace the SERVICE_PROJECT_ID with your service project ID.

  2. Enable the following APIs in the host project:
         
         gcloud services enable --project=HOST_PROJECT_ID networkconnectivity.googleapis.com
         

Replace the HOST_PROJECT_ID with the ID of your host project.




## Create a service connection policy

Next, a [service connection policy](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) must be created for the host project of the Shared VPC where the policy is defined, network, region, and the subnet(s) where you want to provision the Memorystore for Valkey instance. Usually this is done by your Network Admin, or you might have the necessary permission run the command if you have the [Required role](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#roles).

This quickstart uses the `default` network and `default` subnet. IP addresses for your instance are allocated on this default subnet in the region.

### gcloud

  1. To create the service connection policy, run the `create` command:
         
         gcloud network-connectivity service-connection-policies create POLICY_NAME \
           --network=default \
           --project=HOST_PROJECT_ID \
           --region=REGION \
           --service-class=gcp-memorystore \
           --subnets=https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/REGION/subnetworks/default
         

Replace the following:

     * POLICY_NAME is your desired policy name.
     * HOST_PROJECT_ID is the host project ID.
     * REGION is the same region where you want to provision your Memorystore for Valkey instance.
  2. To validate if the policy was created successfully, run the `list` command:
         
         gcloud network-connectivity service-connection-policies list \
           --region=REGION \
           --project=HOST_PROJECT_ID
         

Replace the following:

     * HOST_PROJECT_ID is the host project ID.
     * REGION is the region where the service connection policy is defined.



## Create an instance

To create an instance in the service project attached to the Shared VPC, run the following command:

### gcloud
    
    
    gcloud memorystore instances create INSTANCE \
    --project=SERVICE_PROJECT_ID \
    --location=REGION \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT \
    --replica-count=REPLICA_COUNT \
    --endpoints='[{"connections": [{"pscAutoConnection": {"network": "projects/HOST_PROJECT_ID/global/networks/default", "projectId": "SERVICE_PROJECT_ID"}}]}]'
    

Replace the following:

  * INSTANCE is the instance ID.
  * SERVICE_PROJECT_ID is the service project ID.
  * REGION is the region where you want to provision your instance.

  * NODE_TYPE is the [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type) that you want to use for the instance.

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
  * SHARD_COUNT determines the number of shards in your instance. Shard count determines the total memory capacity for storing instance data. To see more details about instance specification, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

  * REPLICA_COUNT is the number of read replicas (per shard). Accepted values are `0`-`5`.

  * HOST_PROJECT_ID is the host project ID.




## Describe the instance

To view instance details, run the following command:

### gcloud
    
    
    gcloud memorystore instances describe INSTANCE \
    --project=SERVICE_PROJECT_ID \
    --location=REGION
    

Replace the following:

  * INSTANCE is the instance ID.
  * SERVICE_PROJECT_ID is the service project ID.
  * REGION is the region where your instance is located.



## Delete the instance

To delete an instance, run the following command:

### gcloud
    
    
    gcloud memorystore instances delete INSTANCE \
    --project=SERVICE_PROJECT_ID \
    --location=REGION
    

Replace the following:

  * INSTANCE is the instance ID.
  * SERVICE_PROJECT_ID is the service project ID.
  * REGION is the region where your instance is located.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
