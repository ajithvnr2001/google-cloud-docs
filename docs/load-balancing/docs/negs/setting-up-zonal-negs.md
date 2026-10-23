---
url: https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs/
title: Set up zonal NEGs \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:38.046606+00:00
---

# Set up zonal NEGs  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up zonal NEGs Stay organized with collections  Save and categorize content based on your preferences. 

This document contains instructions for configuring zonal network endpoint groups (NEGs). Before you configure zonal NEGs, read [Network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs).

**Note:** This page describes how to configure a specific load balancer component or feature before or after you've already created a load balancer. Working with specific components is useful for advanced configurations and necessary for some configuration options. Before using the information on this page, know the [type of Google Cloud load balancer](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) that you need.

## Zonal NEGs with `GCE_VM_IP` endpoints

These can be used as backends for backend services in internal passthrough Network Load Balancers and regional external passthrough Network Load Balancers. For details, see [Zonal NEGs overview: Load balancing](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#l4lb-zonal-neg).

For end-to-end examples, see the following:

  * [Set up an internal passthrough Network Load Balancer with zonal NEG backends](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal-zonal-neg)
  * [Set up a regional external passthrough Network Load Balancer with zonal NEG backends](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-zonal-neg)



## Zonal NEGs with `GCE_VM_IP_PORT` endpoints

These can be used as backends for backend services in the following types of load balancers:

  * [External Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
  * [External proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp)
  * [Internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)
    * End-to-end example: [Set up a regional internal proxy Network Load Balancer with zonal NEG backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-zonal).



The primary use case for `GCE_VM_IP_PORT` zonal NEGs is [container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing) so that you can distribute traffic among microservices running in containers on your VMs. Container-native load balancing enables load balancers to target Pods directly and to make load distribution decisions at the Pod-level instead of at the VM-level.

There are two ways to configure container-native load balancing: either use NEGs managed by GKE Ingress, or use standalone NEGs.

For instructions, see:

  * [Container-native load balancing through Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing)
  * [Container-native load balancing through standalone zonal NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg)



## Configuring zonal NEGs

The rest of this page describes how to configure zonal NEGs before or after you've already created a load balancer. Note that some of these actions don't apply to zonal NEGs [created and managed by Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing).

### Create a zonal network endpoint group

###  Console 

To create a zonal network endpoint group:

  1. Go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to the Network Endpoint Groups page](https://console.cloud.google.com/compute/networkendpointgroups/list)  

  2. Click **Create network endpoint group**.
  3. For the **Network endpoint group type** , select **Network endpoint type: Zonal**.
  4. Enter the **Name** of the network endpoint group.
  5. For **Network endpoint type** , select **Network endpoint group (Zonal)**.
  6. Select the **Endpoints type** depending on the type of load balancer you're using.
  7. Select the **Network**.
  8. Select the **Subnetwork**.
  9. Select the **Zone**.
  10. For zonal negs with `GCE_VM_IP_PORT` endpoints only, enter a **Default port**.
  11. Click **Create**.



###  gcloud

#### Create a `GCE_VM_IP_PORT` zonal NEG
    
    
    gcloud compute network-endpoint-groups create NEG_NAME \
        --zone=ZONE \
        --network=NETWORK
        [--subnet=SUBNET]
        [--default-port=DEFAULT_PORT]
    

In this command, the flags are defined as follows:

  * `NEG_NAME` is the name of the new network endpoint group. The name must be unique within the zone.
  * `ZONE` is the name of the zone in which the NEG is created.
  * `NETWORK` is the name of the network in which the NEG is created. If omitted, Google Cloud uses a network named `default`.
  * `SUBNET` is the name of the subnet to which the network endpoints belong. This flag is optional if the network is an auto mode VPC network. If omitted, the NEG resides in the automatically created subnet of the selected zone's region. The flag is required if the network is a custom mode VPC or if you need to specify a manually created subnet.
  * `DEFAULT_PORT` is the default port associated with the NEG. This flag is optional. If omitted, all endpoints must be specified by IP:port. If included, the `port` portion can be omitted from the endpoint specification and the default port is assumed.



#### Create a `GCE_VM_IP` zonal NEG

To create a `GCE_VM_IP` zonal network endpoint group you must specify the `network-endpoint-type` as shown here: [`gcloud compute network-endpoint-groups create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/create)
    
    
    gcloud compute network-endpoint-groups create NEG_NAME \
        --network-endpoint-type=gce-vm-ip \
        --zone=ZONE \
        --network=NETWORK
        --subnet=SUBNET
    

In this command, the flags are defined as follows:

  * `NEG_NAME` is the name of the new network endpoint group. The name must be unique within the zone.
  * `ZONE` is the name of the zone in which the NEG is created.
  * `NETWORK` is the name of the network in which the NEG is created.
  * `SUBNET` is the name of the subnet to which the network endpoints belong.



### Add endpoints to a network endpoint group

###  Console 

To add endpoints to a network endpoint group:

  1. Go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to the Network Endpoint Groups page](https://console.cloud.google.com/compute/networkendpointgroups/list)  

  2. Click the **Name** of the network endpoint group to which you want to add endpoints. You see the **Network endpoint group details** page.
  3. In the **Network endpoints in this group** section, click **Add network endpoint**. You see the **Add network endpoint** page.
  4. Select a **VM instance** to add its internal IP addresses as network endpoints and click **Add**. You see the **Network interface** , zone, subnet, and the internal IP address of the VM interface assigned to the endpoint.
  5. For zonal negs with `GCE_VM_IP_PORT` endpoints only, perform the following steps: 
     1. Enter the **IP address** of the new network endpoint.
     2. Select the **Port type**. 
        * If you select **Default** , the endpoint uses the default port for all endpoints in the network endpoint group.
        * If you select **Custom** , enter the **Port number** for the endpoint to use.
  6. To add more endpoints, click **Add network endpoint** and repeat steps 5 and 6.
  7. After you add all the endpoints that you need, click **Create**.



###  gcloud 

**Add endpoints to a`GCE_VM_IP` zonal NEG**

To add endpoints to a `GCE_VM_IP` zonal NEG, run the [`gcloud compute network-endpoint-groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update). You can add [IPv4 and IPv6 endpoints](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#table_gce_vm_ip_endpoints) to a `GCE_VM_IP` zonal NEG.

Add IPv4 endpoints to the network endpoint group:
    
    
    gcloud compute network-endpoint-groups update NEG_NAME \
        --zone=ZONE \
        --add-endpoint 'instance=INSTANCE_NAME,[ip=IPv4_ADDRESS]' \
        [--add-endpoint ...]
    

Add IPv6 endpoints to the network endpoint group:
    
    
      gcloud compute network-endpoint-groups update NEG_NAME \
          --zone=ZONE \
          --add-endpoint 'instance=INSTANCE_NAME,[ipv6=IPv6_ADDRESS]' \
          [--add-endpoint ...]
    

Replace the following:

  * `NEG_NAME`: the name of the NEG
  * `ZONE`: the name of the zone in which the NEG resides
  * `INSTANCE_NAME`: the name of the VM to which the IP address belongs.
  * `IPv4_ADDRESS`: the primary internal IPv4 address of a network interface
  * `IPv6_ADDRESS`: the first IPv6 address (`/128`) from a `/96` range assigned to a VM network interface



If you omit the IP address, the IP address is selected based on the network interface that is in the NEG's subnet. To learn more about the IP address that is selected, see [Endpoint specifications for `GCE_VM_IP` zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#gce-vm-ip-endpoint-spec).

**Add endpoints to a`GCE_VM_IP_PORT` zonal NEG**

To add endpoints to a `GCE_VM_IP_PORT` zonal NEG, run the [`gcloud compute network-endpoint-groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update). You can add [IPv4, IPv6, and dual-stack endpoints](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#table_gce_vm_ip_port_endpoints) to a `GCE_VM_IP_PORT` zonal NEG.

Add IPv4 endpoints to the network endpoint group:
    
    
      gcloud compute network-endpoint-groups update NEG_NAME \
          --zone=ZONE \
          --add-endpoint 'instance=INSTANCE_NAME,[ip=IPv4_ADDRESS],[port=PORT]' \
          [--add-endpoint ...]
    

Add IPv6 endpoints to the network endpoint group:
    
    
      gcloud compute network-endpoint-groups update NEG_NAME \
          --zone=ZONE \
          --add-endpoint 'instance=INSTANCE_NAME,[ipv6=IPv6_ADDRESS],[port=PORT]' \
          [--add-endpoint ...]
    

Add dual-stack endpoints to the network endpoint group:
    
    
    gcloud compute network-endpoint-groups update NEG_NAME \
        --zone=ZONE \
        --add-endpoint 'instance=INSTANCE_NAME,[ip=IPv4_ADDRESS],[ipv6=IPv6_ADDRESS],[port=PORT]' \
        [--add-endpoint ...]
    

**Note:** The [`--ip-address-selection-policy` field](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create#--ip-address-selection-policy) on the backend service lets you specify a preference for the traffic type that is sent from the backend service to your backends. For more information, see [IP address selection policy](https://docs.cloud.google.com/load-balancing/docs/backend-service#ip-address-selection-policy).

Replace the following:

  * `NEG_NAME`: the name of the NEG
  * `ZONE`: the name of the zone in which the NEG resides
  * `INSTANCE_NAME`: the name of the VM to which the IP address belongs
  * `IPv4_ADDRESS`: the primary internal IPv4 address of a network interface or an internal IPv4 address from the alias IP address range assigned to a VM network interface
  * `IPv6_ADDRESS`: any IPv6 address (`/128`) from a `/96` range assigned to a VM network interface
  * `PORT`: the port of the network endpoint being added. The port is optional if default port is specified in the NEG. This field is not supported for zonal NEGs with `GCE_VM_IP` endpoints.

If you omit the IP address, the IP address is selected based on the network interface that is in the NEG's subnet. To learn more about the IP address that is selected, see [Endpoint specifications for `GCE_VM_IP_PORT` zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#gce-vm-ip-port-endpoint-spec).




In the following example, IPv4 endpoints are added to a `GCE_VM_IP_PORT` zonal NEG:
    
    
    gcloud compute network-endpoint-groups update my-lb-neg \
        --zone=asia-southeast1-a \
        --add-endpoint 'instance=my-vm1,ip=10.1.1.1,port=80'
    

For more details, see [Zonal network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#endpoint-spec).

### Add a zonal NEG to a backend service

###  Console 

To add a network endpoint group to a backend service:

  1. Go to the Load balancing page in the Google Cloud console.   
[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/)
  2. Click the name of the load balancer whose backend service you want to edit.
  3. On the **Load balancer details** page, click **Edit** edit.
  4. On the **Edit load balancer** page, click **Backend configuration**.
  5. On the **Backend configuration** page, click **Edit** edit.
  6. Click **+Add backend**.
  7. Select a **Zonal network endpoint group** and click **Done**.
  8. Click **Update**.



###  gcloud 

To add a NEG to a backend service:
    
    
    gcloud compute backend-services add-backend BACKEND_SERVICE \
         --network-endpoint-group=NETWORK_ENDPOINT_GROUP \
         --network-endpoint-group-zone=ZONE
    

For example, to add a `GCE_VM_IP_PORT` zonal NEG to a backend service:
    
    
    gcloud compute backend-services add-backend my-lb \
       --network-endpoint-group my-lb-neg \
       --network-endpoint-group-zone=asia-southeast1-a \
       --global \
       --balancing-mode=RATE \
       --max-rate-per-endpoint=5
    

### Remove a NEG from a backend service

###  Console 

  1. Go to the Load balancing page in the Google Cloud console.   
[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/)
  2. Click the name of the load balancer whose backend service you want to edit.
  3. On the **Load balancer details** page, click **Edit** edit.
  4. On the **Edit load balancer** page, click **Backend configuration**.
  5. On the **Backend configuration** page, click **Edit** edit for the backend service from which you are removing the NEG.
  6. In the **Backend** section, locate the NEG you want to remove and click the trash can icon for that NEG.
  7. Click **Update**.



###  gcloud 

To remove a NEG from a backend service:
    
    
    gcloud compute backend-services remove-backend BACKEND_SERVICE \
        --network-endpoint-group=NETWORK_ENDPOINT_GROUP \
        --network-endpoint-group-zone=NETWORK_ENDPOINT_GROUP_ZONE
    

For example:
    
    
    gcloud compute backend-services remove-backend my-lb \
        --network-endpoint-group=my-lb-neg \
        --network-endpoint-group-zone=asia-southeast1-a
    

### Remove endpoints from a network endpoint group

When a network endpoint is removed from a load balancing NEG, it triggers connection draining based on the drain parameters specified in the backend service. If multiple backend services refer to the same NEG, the maximum drain interval across all backend services is applied.

###  Console 

To remove endpoints from a network endpoint group:

  1. Go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to the Network Endpoint Groups page](https://console.cloud.google.com/compute/networkendpointgroups/list)  

  2. Click the **Name** of the network endpoint group from which you want to delete endpoints. You see the **Network endpoint group detail** page.
  3. Select the network endpoints you want to delete and click **Remove endpoint**.



###  gcloud 

To remove endpoints from a network endpoint group:
    
    
    gcloud compute network-endpoint-groups update NEG_NAME \
    --zone=ZONE \
    --remove-endpoint 'instance=INSTANCE_NAME,[ip=IP],[port=PORT]' \
    [--remove-endpoint ...]
    

For example, to remove an endpoint from a `GCE_VM_IP_PORT` zonal NEG:
    
    
    gcloud compute network-endpoint-groups update my-lb-neg \
         --remove-endpoint 'instance=my-vm1,ip=10.1.1.1,port=80' \
         --zone=asia-southeast1-a
    

### List network endpoint groups

###  Console 

To view a list of network endpoint groups, go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to the Network Endpoint Groups page](https://console.cloud.google.com/compute/networkendpointgroups/list)  


###  gcloud 

To list network endpoint groups:
    
    
    gcloud compute network-endpoint-groups list
    

### Describe a specific network endpoint group

###  Console 

To get the details of a specific network endpoint group:

  1. Go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to the Network Endpoint Groups page](https://console.cloud.google.com/compute/networkendpointgroups/list)  

  2. Click the name of the network endpoint group whose details you want to see.



###  gcloud 

To get the details of a specific network endpoint group:
    
    
    gcloud compute network-endpoint-groups describe NEG_NAME \
        --zone=ZONE
    

Replace the following:

  * `NEG_NAME`: the name of the network endpoint group
  * `ZONE`: the optional name of the zone where the NEG was created.



For example, the following `gcloud` command lists information about the network endpoint group `my-lb-neg`.
    
    
    gcloud compute network-endpoint-groups describe my-lb-neg \
        --zone=asia-southeast1-a
    

The output of the command is the following:
    
    
        creationTimestamp: '2018-04-09T14:51:34.381-07:00'
        id: '5260475207627726473'
        kind: compute#networkEndpointGroup
        loadBalancer:
          defaultPort: 80
          network: https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/global/networks/default
          zone: https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/asia-southeast1-a
    

### Remove network endpoint groups

A network endpoint group cannot be deleted if it is attached to a backend service. Before you delete a NEG, ensure that it is detached from the backend service.

Deleting a VM immediately causes all network endpoints on the VM to be removed from the NEG, closing all connections. Deleting a NEG after deleting a backend service also removes all endpoints in that NEG without connection draining.

###  Console 

To remove a network endpoint group from a backend service:

  1. Go to the Load balancing page in the Google Cloud console.   
[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/)
  2. Click the name of the load balancer whose backend service you want to edit.
  3. On the **Load balancer details** page, click **Edit** edit.
  4. On the **Edit load balancer** page, click **Backend configuration**.
  5. On the **Backend configuration** page, click **Edit** edit for the backend service from which you are removing the NEG.
  6. In the **Backend** section, locate the NEG you want to remove and click the trash can icon for that NEG.
  7. Click **Update**.



To delete a network endpoint group:

  1. Go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to the Network Endpoint Groups page](https://console.cloud.google.com/compute/networkendpointgroups/list)  

  2. Locate the network endpoint group you want to delete.
  3. Click the trash can icon in that row.



###  gcloud 

To remove a network endpoint group from a backend service:
    
    
    gcloud compute backend-services remove-backend BACKEND_SERVICE \
         --network-endpoint-group=NETWORK_ENDPOINT_GROUP \
         --network-endpoint-group-zone=ZONE
    

To delete a network endpoint group:
    
    
    gcloud compute network-endpoint-groups delete NEG_NAME \
        --zone=ZONE
    

For example:
    
    
    gcloud compute backend-services remove-backend my-neg-backend \
        --network-endpoint-group=my-lb-neg \
        --network-endpoint-group-zone=southeast1-a
    
    
    
    gcloud compute network-endpoint-groups delete my-lb-neg \
        --zone=asia-southeast1-a
    

### List endpoints in a network endpoint group

###  Console 

To view a list of endpoints in a network endpoint group:

  1. Go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to the Network Endpoint Groups page](https://console.cloud.google.com/compute/networkendpointgroups/list)  

  2. Click the **Name** of the network endpoint group from which you want to delete endpoints. You see the **Network endpoint group detail** page, on which the endpoints for the endpoint group are listed.
  3. To filter the endpoints, create key:value pairs in the text field under **Network endpoints in this group**.



###  gcloud 

To list all of the network endpoints in a network endpoint group:
    
    
    gcloud compute network-endpoint-groups list-network-endpoints NEG_NAME \
         --zone=ZONE
    

#### Custom filtering when you list endpoints in a network endpoint group

You can use a custom filter to limit which endpoints in a network endpoint group are listed. Custom filtering is enabled only for the REST API. You cannot use custom filtering from the Google Cloud console or using the `gcloud` command-line interface.

For details, see the documentation for the method [networkEndpointGroups.listNetworkEndpoints](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups/listNetworkEndpoints).

### Health checking network endpoints

Backend services with zonal NEG backends must use a health check whose port specification is either:

  * a fixed (numbered) port (`--port`)
  * configured to use the serving port of the network endpoint (`--use-serving-port`)



The example that follows creates an HTTP health check that uses the serving port of the network endpoint with the `--use-serving-port` flag. Note that the `--use-serving-port` flag is implemented with [`gcloud compute health-checks create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create), but not with `gcloud compute health-checks update`.
    
    
    gcloud compute health-checks create http HTTP_HEALTH_CHECK_NAME
        --use-serving-port
    

You cannot use a legacy health check with a zonal NEG backend. For more information, see [Health Check Concepts](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
