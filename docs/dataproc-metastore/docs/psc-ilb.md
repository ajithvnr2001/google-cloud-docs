---
url: https://docs.cloud.google.com/dataproc-metastore/docs/psc-ilb/
title: Private Service Connect with Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:38.606851+00:00
---

# Private Service Connect with Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/psc-ilb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Private Service Connect with Dataproc Metastore Stay organized with collections  Save and categorize content based on your preferences. 

With Private Service Connect, you can create a Dataproc Metastore service that doesn't use [VPC peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). This page explains what [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) is and how to use it as an alternative networking option for Dataproc Metastore.

## How Dataproc Metastore works with VPC

Dataproc Metastore protects its metadata access by only exposing private IP endpoints. It also restricts connectivity to VMs in your VPC network by using VPC peering.

Dataproc Metastore requires the following configurations per region for each VPC network:

  * 1 [peering quota](https://docs.cloud.google.com/vpc/docs/quota)
  * `/17` and `/20` [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) blocks



As a result, setting up VPC peering and IP address reservations can be difficult on crowded VPC networks. Similarly, a VPC network may not have enough peering quota to accommodate additional peering requests. Both of these limitations can prevent you from creating new Dataproc Metastore services.

To circumvent these issues, you can use Dataproc Metastore with Private Service Connect.

## How Dataproc Metastore works with Private Service Connect

Private Service Connect provides a private connection to Dataproc Metastore metadata across VPC networks.

To use Private Service Connect with Dataproc Metastore, the following configurations are required:

  * A single address reservation in the subnetwork.
  * A forwarding rule targeting the service attachment that exposes the Dataproc Metastore endpoint. The address reservation and forwarding rule are created as a part of the Dataproc Metastore service create call.



### Considerations

  * Dataproc Metastore services that use Private Service Connect only support access from VPC networks of the subnetworks specified during the service creation.

  * Dataproc Metastore reserves addresses and creates forwarding rules in each of the specified subnetworks. Each subnetwork has a Thrift endpoint URI that you can use to access the Dataproc Metastore metadata endpoint from.




### Limitations

  * Dataproc Metastore services that use the gRPC endpoints protocol don't support Private Service Connect.
  * Reverse connectivity is not supported with Private Service Connect. This means you can't use a Kerberos configuration with Private Service Connect.
  * You can't dynamically add or remove subnets from a Dataproc Metastore service that is configured with Private Service Connect. Instead, you must recreate a service if you'd like to add or remove subnets.
  * You can't update a Dataproc Metastore service that uses Private Service Connect to use VPC or the other way around.



## Create a Dataproc Metastore service with Private Service Connect

The following instructions demonstrate how to configure Private Service Connect during service creation.

### Console

  1. In the Google Cloud console, open the Dataproc Metastore page:

[Go to Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. At the top of the **Dataproc Metastore** page, click **Create**.

The **Create service** page opens.

  3. Configure your service as needed.

  4. Under **Network configuration** , click **Make services accessible in multiple VPC subnetworks**.

  5. Select the **Subnetworks**. You can specify up to 5 subnetworks.

  6. Click **Done**.

  7. Click **Submit**.




Verify the service's network configuration:

  1. In the Google Cloud console, open the Dataproc Metastore page:

[Go to Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. On the **Dataproc Metastore** page, click the service name of the service you would like to view.

The **Service detail** page for that service opens.

  3. Under the **Configuration** tab, verify that the details show multiple VPC subnetwork URIs.




### gcloud

  1. Run the following `gcloud metastore services create` command to create a service with Private Service Connect:
         
         gcloud metastore services create SERVICE \
            --location=LOCATION \
            --consumer-subnetworks="projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET1, projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET2"
         

or
         
         gcloud metastore services create SERVICE \
            --location=LOCATION \
            --network-config-from-file=NETWORK_CONFIG_FROM_FILE
         

  2. Verify that the creation was successful.




### REST

Follow the API instructions to [create a service](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/create) by using the API Explorer.

In the `create` request parameters, use the `Network Config` field to configure Private Service Connect. You can specify 1 to 5 subnetworks.
    
    
         "network_config": {
           "consumers": [
               {"subnetwork": "projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET1"},
               {"subnetwork": "projects/PROJECT_ID/regions/LOCATION/subnetworks/SUBNET2"}
           ]
         }
       

## What's next

  * [VPC Network Peering overview](https://docs.cloud.google.com/vpc/docs/vpc-peering)
  * [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect)
  * [Service networking](https://docs.cloud.google.com/dataproc-metastore/docs/networking)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
