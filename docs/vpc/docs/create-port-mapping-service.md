---
url: https://docs.cloud.google.com/vpc/docs/create-port-mapping-service/
title: Create port mapping services \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:11.503790+00:00
---

# Create port mapping services  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-port-mapping-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create port mapping services

This page describes how service producers can publish services that use Private Service Connect port mapping.

Private Service Connect port mapping lets consumer clients privately communicate with specific service ports on specific producer VMs through a single [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints).

## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your project.
  * You must [create VMs](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) for each of the network endpoints that you want to attach to the port mapping NEG. The VMs must all be in the same region.
  * Read [About published services](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services).
  * Read [About Private Service Connect port mapping](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-port-mapping).



### Required roles

To get the permissions that you need to prepare to publish a service with Private Service Connect port mapping, ask your administrator to grant you the following IAM roles on the producer project: 

  * [Compute Load Balancer Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create and publish a port mapping service

Port mapping services have similar configurations to internal passthrough Network Load Balancers, but traffic is not load balanced. To create and publish a port mapping service, do the following:

  * Create a port mapping NEG
  * Add network endpoints to the port mapping NEG
  * Create a port mapping service
  * Publish the port mapping service



### Create a port mapping NEG

A [port mapping network NEG](https://docs.cloud.google.com/load-balancing/docs/negs#port-mapping-neg) is a regional NEG with the network endpoint type of `GCE_VM_IP_PORTMAP`. It's not possible to change a port mapping NEG's type after it is created.

When you create a port mapping NEG, you choose a subnet. Network endpoints that you associate with the port mapping NEG must have a primary network interface in this subnet.

###  Console 

  1. In the Google Cloud console, go to the **Network Endpoint Groups** page.

[Go to Network Endpoint Groups](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Click **Create network endpoint group**.

  3. Enter a **Name**.

  4. Click **Network endpoint group type** , and then select **Port mapping NEG (Regional)**.

  5. Select a **Region**.

  6. Select a **Network**.

  7. Select a **Subnetwork**.

  8. Click **Create**.




###  gcloud 

Use the [`network-endpoints-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/create).
    
    
    gcloud compute network-endpoint-groups create NEG \
        --region=REGION \
        --network=NETWORK \
        --subnet=SUBNET \
        --network-endpoint-type=GCE_VM_IP_PORTMAP
    

Replace the following:

  * `NEG`: the name of the port mapping NEG
  * `REGION`: the region of the port mapping NEG
  * `NETWORK`: the VPC network of the port mapping NEG
  * `SUBNET`: the subnet of the port mapping NEG



###  API 

Send a `POST` request to the [`regionNetworkEndpointGroups.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkEndpointGroups
    {
      "name": "NEG",
      "networkEndpointType": "GCE_VM_IP_PORTMAP",
      "network": "projects/PROJECT_ID/global/networks/NETWORK",
      "subnetwork": "projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET"
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the port mapping NEG
  * `REGION`: the region of the port mapping NEG
  * `NEG`: the name of the port mapping NEG
  * `NETWORK`: the VPC network of the port mapping NEG
  * `SUBNET`: the subnet of the port mapping NEG



### Add network endpoints to the port mapping NEG

Create one or more network endpoints with port mappings and attach them to the port mapping NEG.

Network endpoints for port mapping NEGs are zonal and must fulfill the following requirements:

  * Each network endpoint refers to a Compute Engine VM that has a primary network interface in the same subnet as the port mapping NEG.
  * Each network endpoint refers to a unique client destination port.
  * Each network endpoint must refer to a unique combination of service port and VM.




###  Console 

  1. In the Google Cloud console, go to the **Network Endpoint Groups** page.

[Go to Network Endpoint Groups](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Click the name of the port mapping NEG that you want to update.

  3. Click **Add network endpoints**.

  4. Click **VM instance** , and then select a VM.

  5. Click **VM port 1** , and then enter a service port.

  6. Click **Client port 1** , and then enter a client destination port.

  7. For each additional network endpoint that you want to add, click **Add network endpoint** , and then enter the network endpoint details.

  8. Click **Create**.




###  gcloud 

Use the [`network-endpoint-groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update). Include an `--add-endpoint` flag for each network endpoint that you want to attach.
    
    
    gcloud compute network-endpoint-groups update NEG \
        --region=REGION \
        --add-endpoint=client-destination-port=CLIENT_DESTINATION_PORT_1,instance=projects/PROJECT_ID/zones/ZONE_1/instances/VM_1_NAME,port=VM_1_PORT \
        --add-endpoint=client-destination-port=CLIENT_DESTINATION_PORT_2,instance=projects/PROJECT_ID/zones/ZONE_2/instances/VM_2_NAME,port=VM_2_PORT
    

Replace the following:

  * `NEG`: the name of the port mapping NEG
  * `REGION`: the region of the port mapping NEG
  * `CLIENT_DESTINATION_PORT_1`: the client destination port of the first network endpoint
  * `PROJECT_ID`: the project ID of the producer project
  * `ZONE_1`: the zone of the first network endpoint
  * `VM_1_NAME`: the name of the destination VM for the first network endpoint
  * `VM_1_PORT`: the service port of the first network endpoint
  * `CLIENT_DESTINATION_PORT_2`: the client destination port of the second network endpoint
  * `ZONE_2`: the zone of the second network endpoint
  * `VM_2_NAME`: the name of the destination VM for the second network endpoint
  * `VM_2_PORT`: the service port of the second network endpoint



###  API 

Send a `POST` request to the [`regionNetworkEndpointGroups.attachNetworkEndpoints` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/attachNetworkEndpoints).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkEndpointGroups/NEG/attachNetworkEndpoints
    {
      "networkEndpoints": [
        {
          "clientDestinationPort":CLIENT_DESTINATION_PORT_1,
          "instance": "projects/PROJECT_ID/zones/ZONE_1/instances/VM_1_NAME",
          "port": SERVICE_PORT_1
        },
        {
          "clientDestinationPort": CLIENT_DESTINATION_PORT_2,
          "instance": "projects/PROJECT_ID/zones/ZONE_2/instances/VM_2_NAME",
          "port": SERVICE_PORT_2
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the producer project
  * `REGION`: the region of the port mapping NEG
  * `NEG`: the name of the port mapping NEG
  * `CLIENT_DESTINATION_PORT_1`: the client destination port of the first network endpoint
  * `ZONE_1`: the zone of the first network endpoint
  * `VM_1_NAME`: the name of the destination VM for the first network endpoint
  * `SERVICE_PORT_1`: the service port of the first network endpoint
  * `CLIENT_DESTINATION_PORT_2`: the client destination port of the second network endpoint
  * `ZONE_2`: the zone of the second network endpoint
  * `VM_2_NAME`: the name of the destination VM for the second network endpoint
  * `SERVICE_PORT_2`: the service port of the second network endpoint



### Create a port mapping service

To create a port mapping service, complete the following steps.

You can't change the port mapping NEG that is associated with a backend service after you add the NEG. However, you can [update the port mapping NEG's network endpoints](https://docs.cloud.google.com/vpc/docs/update-port-mapping-service#update).

You can't update the connection of a forwarding rule after it is created. If you need to connect to a different backend service, [delete the forwarding rule](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/delete), and then create a new one.

###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Internal** and click **Next**.
  6. Click **Configure**.



**Basic configuration**

  1. Enter a **Load balancer name**.
  2. Select a **Region**.
  3. Select a **Network**.



**Backend configuration**

  1. For **Backend type** , select **Port mapping network endpoint group**.
  2. Select a **Port mapping network endpoint group**.



**Frontend configuration**

  1. Click **Frontend configuration**.
  2. Optional: Enter a **Name**.
  3. Optional: Enter a **Description**.
  4. Select a **Protocol**.
  5. Select a **Subnetwork**.
  6. Click **Done**.
  7. Click **Create**.



###  gcloud 

  1. To create a backend service, use the [`backend-services create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create).
         
         gcloud compute backend-services create SERVICE \
             --load-balancing-scheme=internal \
             --region=REGION \
             --network=NETWORK
         

Replace the following:

     * `SERVICE`: the name of the backend service
     * `REGION`: the region of the backend service
     * `NETWORK`: the producer VPC network of the backend service
  2. To add your port mapping NEG to the backend service, use the [`backend-services add-backend` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend).

You can't add multiple port mapping NEGs to a single backend service.
         
         gcloud compute backend-services add-backend SERVICE \
             --network-endpoint-group=NEG \
             --network-endpoint-group-region=REGION
         

Replace `NEG` with the name of the port mapping NEG.

  3. To create a forwarding rule for your port mapping service, use the [`forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create).

The forwarding rule must be configured to forward traffic for all client destination ports.
         
         gcloud compute forwarding-rules create RULE \
             --load-balancing-scheme=INTERNAL \
             --ip-protocol=PROTOCOL \
             --network=NETWORK \
             --subnet=SUBNET \
             --address=IP_ADDRESS \
             --ports=ALL \
             --region=REGION \
             --backend-service=SERVICE
         

Replace the following:

     * `RULE`: the name of the forwarding rule
     * `PROTOCOL`: the protocol of the forwarding rule, which can be either `TCP` or `UDP`
     * `SUBNET`: the producer subnet, which must be the same subnet that's associated with the port mapping NEG
     * `IP_ADDRESS`: the IP address of the forwarding rule, which must come from the IP address range of the producer subnet



###  API 

  1. To create a backend service, send a `POST` request to the [`regionBackendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/backendServices
         {
           "name": "SERVICE",
           "loadBalancingScheme": "INTERNAL",
           "network": "projects/PROJECT_ID/global/networks/NETWORK"
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the backend service's project
     * `REGION`: the region of the backend service
     * `SERVICE`: the name of the backend service
     * `NETWORK`: the producer VPC network
  2. To add your port mapping NEG to the backend service, send a `PATCH` request to the [`regionBackendServices.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/patch).

You can't add multiple port mapping NEGs to a single backend service.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/backendServices/SERVICE
         {
           "backends": [
             {
               "group": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkEndpointGroups/NEG"
             }
           ]
         }
         

Replace `NEG` with the name of your port mapping NEG.

  3. To create a forwarding rule for your port mapping service, send a `POST` request to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert).

The forwarding rule must be configured to forward traffic for all client destination ports.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/forwardingRules
         {
           "name": "RULE",
           "loadBalancingScheme": "INTERNAL",
           "IPProtocol": "PROTOCOL",
           "network": "projects/PROJECT_ID/global/networks/NETWORK",
           "subnetwork": "projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET",
           "IPAddress": "IP_ADDRESS",
           "allPorts": true,
           "backendService": "projects/PROJECT_ID/regions/REGION/backendServices/SERVICE"
         }
         

Replace the following:

     * `RULE`: the name of the forwarding rule
     * `PROTOCOL`: the protocol of the forwarding rule, which can be either `TCP` or `UDP`
     * `SUBNET`: the producer subnet, which must be the same subnet that's associated with the port mapping NEG
     * `IP_ADDRESS`: the IP address of the forwarding rule, which must come from the IP address range of the producer subnet



### Publish the port mapping service

To make your port mapping service available to consumers, [publish the service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service) by creating a service attachment. When you create the service attachment, specify the forwarding rule that is associated with your port mapping service.

## What's next

  * [Update a port mapping service](https://docs.cloud.google.com/vpc/docs/update-port-mapping-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
