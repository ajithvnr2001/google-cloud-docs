---
url: https://docs.cloud.google.com/vpc/docs/update-port-mapping-service/
title: Update port mapping services \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:37.848420+00:00
---

# Update port mapping services  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/update-port-mapping-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update port mapping services

This page describes how service producers can update Private Service Connect port mapping services.

## Add a network endpoint

You can add network endpoints to a port mapping network endpoint group (NEG) without needing to recreate the NEG.

For information about adding a network endpoint, see [Add networking endpoints to a port mapping NEG](https://docs.cloud.google.com/vpc/docs/create-port-mapping-service#add-endpoints).

## List network endpoints

You can list the network endpoints that are associated with a port mapping NEG.

###  Console 

  1. In the Google Cloud console, go to the **Network Endpoint Groups** page.

[Go to Network Endpoint Groups](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Click the name of your port mapping NEG.




###  gcloud 

Use the [`network-endpoint-groups list-network-endpoints` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/list).
    
    
    gcloud compute network-endpoint-groups list-network-endpoints NEG \
        --region=REGION
    

Replace the following:

  * `NEG`: the name of the port mapping NEG.
  * `REGION`: the region of the port mapping NEG.



###  API 

Send a `POST` request to the [`regionNetworkEndpointGroups.listNetworkEndpoints` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/listNetworkEndpoints).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkEndpointGroups/NEG/listNetworkEndpoints
    

Replace the following:

  * `PROJECT_ID`: the ID of the port mapping NEG's project.
  * `REGION`: the region of the port mapping NEG.
  * `NEG`: the name of the port mapping NEG.



## Update a network endpoint

If you need to update the port mapping or VM that is associated with a network endpoint, you can remove the network endpoint or [delete the VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance#delete_an_instance). When you delete a VM, Google Cloud deletes all network endpoints that are associated with the VM.

After the network endpoint is deleted, add a network endpoint to the port mapping NEG that contains the updated port mapping or VM.

## Remove a network endpoint from a port mapping NEG

You can remove network endpoints from a port mapping NEG without needing to recreate the NEG.

###  Console 

  1. In the Google Cloud console, go to the **Network Endpoint Groups** page.

[Go to Network Endpoint Groups](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Click the name of the port mapping NEG that you want to update.

  3. Select the network endpoint that you want to remove.

  4. Click **Remove endpoint**.




###  gcloud 

Use the [`network-endpoint-groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update).
    
    
    gcloud compute network-endpoint-groups update NEG \
        --region=REGION \
        --remove-endpoint=instance=https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    

Replace the following:

  * `NEG`: the name of the port mapping NEG.
  * `REGION`: the region of the port mapping NEG.
  * `PROJECT_ID`: the ID of the port mapping NEG's project.
  * `ZONE`: the zone of the VM that is associated with the network endpoint to remove.
  * `INSTANCE_NAME`: the name of the instance that is associated with the network endpoint to remove.



###  API 

Send a `POST` request to the [`regionNetworkEndpointGroups.detachNetworkEndpoints` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/detachNetworkEndpoints).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkEndpointGroups/NEG/detachNetworkEndpoints
    {
      "networkEndpoints": [
        {
          "instance": "projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME"
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the port mapping NEG's project.
  * `REGION`: the region of the port mapping NEG.
  * `NEG`: the name of the port mapping NEG.
  * `ZONE`: the zone of the VM that is associated with the network endpoint to remove.
  * `INSTANCE_NAME`: the name of the instance that is associated with the network endpoint to remove.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
