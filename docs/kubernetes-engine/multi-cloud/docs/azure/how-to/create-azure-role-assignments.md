---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-role-assignments/
title: Create Azure role assignments \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:38.609389+00:00
---

# Create Azure role assignments  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-role-assignments/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create Azure role assignments

This page shows how you grant permissions to GKE on Azure so that it can access Azure APIs. You need to perform these steps when setting up a new GKE on Azure cluster or when updating permissions for an existing cluster. These permissions are necessary for GKE on Azure to manage Azure resources on your behalf, such as virtual machines, networking components, and storage.

## Obtain service principal and subscription IDs

To grant permissions to GKE on Azure, you need to obtain your Azure service principal and subscription ID. The Azure service principal and subscription ID are associated with the Azure AD application you created for GKE on Azure. For details, see [Create an Azure Active Directory application](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-ad-application).

A service principal is an identity in Azure Active Directory (AD) that is used to authenticate to Azure and access its resources. An Azure subscription is a logical container that provides you with authorized access to Azure products and services. A subscription ID is a unique identifier associated with your Azure subscription.

To save your service principal and subscription IDs for quick reference, you can store them in shell variables. To create these shell variables, run the following command:
    
    
    APPLICATION_ID=$(az ad app list --all \
        --query "[?displayName=='APPLICATION_NAME'].appId" \
        --output tsv)
    SERVICE_PRINCIPAL_ID=$(az ad sp list --all  --output tsv \
          --query "[?appId=='$APPLICATION_ID'].id")
    SUBSCRIPTION_ID=$(az account show --query "id" --output tsv)
    

Replace `APPLICATION_NAME` with the name of your Azure AD application.

## Create three custom roles

To grant GKE on Azure the permissions to manage your Azure resources, you need to create three custom roles and assign them to the service principal. Only the minimum permissions are added in the following instructions. You can add more permissions if you need to.

You need to create custom roles for the following types of access:

  * **Subscription-level access** : Permissions that apply to the entire Azure subscription, allowing management of all Azure resources within that subscription.
  * **Cluster resource group-level access** : Permissions specific to managing Azure resources within a particular resource group that contains your GKE on Azure clusters.
  * **Virtual network resource group-level access** : Permissions specific to managing Azure resources within a resource group that contains your Azure virtual network resources.



### Create role for subscription-level access

  1. Create a file named `GKEOnAzureAPISubscriptionScopedRole.json`.

  2. Open `GKEOnAzureAPISubscriptionScopedRole.json` in an editor and add the following permissions:
         
         {
         "Name": "GKE on-Azure API Subscription Scoped Role",
         "IsCustom": true,
         "Description": "Allow GKE on-Azure service manage resources in subscription scope.",
         "Actions": [
           "Microsoft.Authorization/roleAssignments/read",
           "Microsoft.Authorization/roleAssignments/write",
           "Microsoft.Authorization/roleAssignments/delete",
           "Microsoft.Authorization/roleDefinitions/read"
         ],
         "NotActions": [],
         "DataActions": [],
         "NotDataActions": [],
         "AssignableScopes": ["/subscriptions/${SUBSCRIPTION_ID}"]
         }
         

  3. Create the new custom role:
         
         az role definition create --role-definition "GKEOnAzureAPISubscriptionScopedRole.json"
         

  4. Assign the role to the service principal using the following command:
         
         az role assignment create --assignee ${SERVICE_PRINCIPAL_ID} --role "GKE on-Azure API Subscription Scoped Role" --scope /subscriptions/${SUBSCRIPTION_ID}
         




### Create role for cluster resource group-level access

  1. Create a file named `GKEOnAzureClusterResourceGroupScopedRole.json`.

  2. Open `GKEOnAzureClusterResourceGroupScopedRole.json` in an editor and add the following permissions:
         
         {
         "Name": "GKE on-Azure API Cluster Resource Group Scoped Role",
         "IsCustom": true,
         "Description": "Allow GKE on-Azure service manage resources in cluster resource group scope.",
         "Actions": [
             "Microsoft.Resources/subscriptions/resourcegroups/read",
             "Microsoft.Authorization/roleDefinitions/write",
             "Microsoft.Authorization/roleDefinitions/delete",
             "Microsoft.ManagedIdentity/userAssignedIdentities/write",
             "Microsoft.ManagedIdentity/userAssignedIdentities/read",
             "Microsoft.ManagedIdentity/userAssignedIdentities/delete",
             "Microsoft.Network/applicationSecurityGroups/write",
             "Microsoft.Network/applicationSecurityGroups/read",
             "Microsoft.Network/applicationSecurityGroups/delete",
             "Microsoft.Network/applicationSecurityGroups/joinIpConfiguration/action",
             "Microsoft.Authorization/roleAssignments/write",
             "Microsoft.Authorization/roleAssignments/read",
             "Microsoft.Authorization/roleAssignments/delete",
             "Microsoft.Network/loadBalancers/write",
             "Microsoft.Network/loadBalancers/read",
             "Microsoft.Network/loadBalancers/delete",
             "Microsoft.Network/loadBalancers/backendAddressPools/join/action",
             "Microsoft.Network/networkSecurityGroups/write",
             "Microsoft.Network/networkSecurityGroups/read",
             "Microsoft.Network/networkSecurityGroups/delete",
             "Microsoft.Network/networkSecurityGroups/join/action",
             "Microsoft.KeyVault/vaults/write",
             "Microsoft.KeyVault/vaults/read",
             "Microsoft.KeyVault/vaults/delete",
             "Microsoft.Compute/disks/read",
             "Microsoft.Compute/disks/write",
             "Microsoft.Compute/disks/delete",
             "Microsoft.Network/networkInterfaces/read",
             "Microsoft.Network/networkInterfaces/write",
             "Microsoft.Network/networkInterfaces/delete",
             "Microsoft.Network/networkInterfaces/join/action",
             "Microsoft.Compute/virtualMachines/read",
             "Microsoft.Compute/virtualMachines/write",
             "Microsoft.Compute/virtualMachines/delete",
             "Microsoft.Compute/virtualMachineScaleSets/write",
             "Microsoft.Compute/virtualMachineScaleSets/read",
             "Microsoft.Compute/virtualMachineScaleSets/delete",
             "Microsoft.ManagedIdentity/userAssignedIdentities/assign/action",
             "Microsoft.Compute/virtualMachines/retrieveBootDiagnosticsData/action",
             "Microsoft.Insights/Metrics/Read"
         ],
         "NotActions": [],
         "DataActions": [
             "Microsoft.KeyVault/vaults/keys/create/action",
             "Microsoft.KeyVault/vaults/keys/delete",
             "Microsoft.KeyVault/vaults/keys/read",
             "Microsoft.KeyVault/vaults/keys/encrypt/action"
         ],
         "NotDataActions": [],
         "AssignableScopes": ["/subscriptions/${SUBSCRIPTION_ID}"]
          }
          ```
         

  3. Create the new custom role:
         
         az role definition create --role-definition "GKEOnAzureClusterResourceGroupScopedRole.json"
         

  4. Assign the role to the service principal using the following command:
         
         az role assignment create --assignee ${SERVICE_PRINCIPAL_ID} --role "GKE on-Azure API Cluster Resource Group Scoped Role" --scope /subscriptions/${SUBSCRIPTION_ID}/resourceGroups/${CLUSTER_RESOURCE_GROUP_ID}
         




### Create role for virtual network resource group-level access

  1. Create a file named `GKEOnAzureAPIVNetResourceGroupScopedRole.json`.

  2. Open `GKEOnAzureAPIVNetResourceGroupScopedRole.json` in an editor and add the following permissions:
         
         {
         "Name": "GKE on-Azure API VNet Resource Group Scoped Role",
         "IsCustom": true,
         "Description": "Allow GKE on-Azure service manage resources in virtual network resource group scope.",
         "Actions": [
             "Microsoft.Network/virtualNetworks/read",
             "Microsoft.Network/virtualNetworks/subnets/read",
             "Microsoft.Network/virtualNetworks/subnets/join/action",
             "Microsoft.Authorization/roleDefinitions/write",
             "Microsoft.Authorization/roleDefinitions/delete"
         ],
         "NotActions": [],
         "DataActions": [],
         "NotDataActions": [],
         "AssignableScopes": ["/subscriptions/${SUBSCRIPTION_ID}"]
         }
         

  3. Create the new custom role:
         
         az role definition create --role-definition "GKEOnAzureAPIVNetResourceGroupScopedRole.json"
         

  4. Assign the role to the service principal using the following command:
         
         az role assignment create --assignee ${SERVICE_PRINCIPAL_ID} --role "GKE on-Azure API Subscription Scoped Role" --scope "/subscriptions/${SUBSCRIPTION_ID}/resourceGroups/VNET_RESOURCE_GROUP_ID"
         




## What's next

  * [Create a client certificate](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-client)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
