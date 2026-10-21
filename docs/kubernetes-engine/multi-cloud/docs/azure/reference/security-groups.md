---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/security-groups/
title: Network security groups \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:53.427576+00:00
---

# Network security groups  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/security-groups/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Network security groups

This page describes and lists the [Azure network security groups (NSGs)](https://docs.microsoft.com/azure/virtual-network/network-security-groups-overview) required by GKE on Azure.

This page is for Networking specialists who want to install, configure, and support network equipment. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Managed NSGs

GKE on Azure manages the NSGs attached to the virtual network interface card (NIC) of each virtual machine (VM) instance. To further control network traffic, you can add additional NSGs to your subnets.

GKE on Azure manages required NSG rules automatically. It adds missing NSG rules and removes rules that are no longer necessary. GKE on Azure also modifies rules based on your Kubernetes Service configuration. For example, when you add a Kubernetes Service of type `LoadBalancer`, GKE on Azure adds the corresponding NSG rules.

## Rule priorities

Azure NSG rule priorities have a range between 100 and 4096. The lower the priority number, the higher the priority.

By design, GKE on Azure manages only NSG rules with a priority of 500 or higher. Therefore, if you need to implement a specific rule or create additional rules, you can use NSGs with a priority between 100 and 499.

Azure processes rules in order, starting with the lowest priority number and proceeding upward. When you create a new rule, always choose rule priorities in the 100 to 499 range to avoid conflict with existing Anthos NSG rules.

## Application security groups

GKE on Azure creates two [application security groups (ASGs)](https://docs.microsoft.com/azure/virtual-network/application-security-groups) that apply to the virtual NICs of control planes and worker nodes. GKE on Azure updates ASGs automatically—for example, when you add a new node pool to a cluster. You can use these ASGs when creating NSG rules.

The Azure Resource Manager (ARM) IDs of the NSG and control plane ASG can be obtained from the output of [`gcloud container azure clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/describe).

For example, to allow SSH connections to the control plane VMs, run the `az network nsg rule create` command to create an NSG that references the control plane ASG:
    
    
    NSG_NAME=$(basename $(gcloud container azure clusters describe \
      CLUSTER_NAME --location=GOOGLE_CLOUD_LOCATION \
      --format 'value(managedResources.networkSecurityGroupId)'))
    
    ASG_CP_NAME=$(basename $(gcloud container azure clusters describe \
      CLUSTER_NAME --location=GOOGLE_CLOUD_LOCATION \
      --format 'value(managedResources.controlPlaneApplicationSecurityGroupId)'))
    
    az network nsg rule create \
      --name AllowSshToControlPlane \
      --nsg-name "${NSG_NAME}" \
      --priority 100 \
      --resource-group "CLUSTER_RESOURCE_GROUP" \
      --access Allow \
      --protocol Tcp \
      --destination-port-ranges 22 \
      --destination-asgs "${ASG_CP_NAME}"
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud location that manages your cluster
  * `CLUSTER_RESOURCE_GROUP`: the name of the Azure resource group that holds your cluster



For more information about creating a new rule, follow the procedure described in [Azure NSG rule creation](https://docs.microsoft.com/cli/azure/network/nsg/rule?view=azure-cli-latest#az_network_nsg_rule_create).

## Default NSG rules

When you set up GKE on Azure, it creates the following NSG rules in your Azure virtual network.

Priority | Ports | Protocol | Source | Destination | Action | Purpose  
---|---|---|---|---|---|---  
1000 | 2380, 2381 | TCP | Control plane NICs | Control plane NICs | Allow | Control plane etcd communication  
1001 | 443, 8132 | TCP | Any | Control plane NICs | Allow | Allow accessing the Kubernetes API  
1002 | 10250 | TCP | Control plane NICs | Node pool NICs | Allow | Control plane to node communications  
1003 | 10250, 10255 | TCP | Node pool NICs | Node pool NICs | Allow | Node-to-node communication  
1004 | 6081 | UDP | Node pool NICs | Node pool NICs | Allow | Node-to-node CNI communication  
1005 | Any | Any | Azure load balancer | Any | Allow | Allow inbound traffic to load balancer  
4096 | Any | Any | Any | Any | Deny | Deny all inbound connections not covered by another rule  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
