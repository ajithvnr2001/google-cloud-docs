---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-vnet/
title: Create an Azure virtual network \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:07:42.228375+00:00
---

# Create an Azure virtual network  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-vnet/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an Azure virtual network

Before you can deploy an Anthos cluster on Azure, you need to create an Azure virtual network (VNet) in which your cluster will run. This page explains how to do that.

However, before creating an Azure VNet, we recommend that you create a new resource group for the VNet that is separate from the resource group you will create later for your GKE on Azure. This separation can help better organize and manage your resources.

To create a new resource group for your Azure VNet, run the following command:
    
    
    az group create --name "VNET_RESOURCE_GROUP_NAME" \
      --location "AZURE_REGION"
    

Replace the following:

  * `VNET_RESOURCE_GROUP_NAME`: the name of the resource group for your GKE on Azure VNet
  * `AZURE_REGION`: a [supported Azure region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions)—for example `westus2`



Now that you have created a resource group for your Azure Vnet, perform the following steps to create a VNet with a default subnet, and attach a NAT gateway to that subnet:

  1. To create a new VNet with a default subnet, run the following command:
         
         az network vnet create \
           --name "VNET_NAME" \
           --location "AZURE_REGION" \
           --resource-group "VNET_RESOURCE_GROUP_NAME" \
           --address-prefixes VNET_ADDRESS_PREFIXES \
           --subnet-name default
         

Replace the following:

     * `VNET_NAME`: the name of your VNet
     * `AZURE_REGION`: the Azure region used previously
     * `VNET_RESOURCE_GROUP_NAME`: the name of the resource group for your VNet that you created at the beginning of this document
     * `VNET_ADDRESS_PREFIXES`: a space-separated list of IP address prefixes in CIDR notation—for example `10.0.0.0/16 172.16.0.0/12`
  2. To create an IP address for a new NAT gateway, attach a NAT gateway to the IP address, and attach the NAT gateway to the default subnet, run the following commands:
         
         az network public-ip create \
           --name "NAT_GATEWAY_NAME-ip" \
           --location "AZURE_REGION" \
           --resource-group "VNET_RESOURCE_GROUP_NAME" \
           --allocation-method Static \
           --sku Standard
         
         az network nat gateway create \
           --name "NAT_GATEWAY_NAME" \
           --location "AZURE_REGION" \
           --resource-group "VNET_RESOURCE_GROUP_NAME" \
           --public-ip-addresses "NAT_GATEWAY_NAME-ip" \
           --idle-timeout 10
         
         az network vnet subnet update \
           --name default \
           --vnet-name "VNET_NAME" \
           --resource-group "VNET_RESOURCE_GROUP_NAME" \
           --nat-gateway "NAT_GATEWAY_NAME"
         

Replace the following:

     * `NAT_GATEWAY_NAME`: the name of the new NAT gateway
     * `VNET_NAME`: the name of your VNet
     * `AZURE_REGION`: the Azure region used previously
     * `VNET_RESOURCE_GROUP_NAME`: the name of the resource group for your VNet that you created at the beginning of this document



## What's next

  * [Create an Azure resource group](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-resource-group)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
