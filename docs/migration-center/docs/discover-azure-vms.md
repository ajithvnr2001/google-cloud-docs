---
url: https://docs.cloud.google.com/migration-center/docs/discover-azure-vms/
title: Discover virtual machine instances on Azure \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:59.317405+00:00
---

# Discover virtual machine instances on Azure  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/discover-azure-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Discover virtual machine instances on Azure Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the steps to run an inventory discovery on your Azure account by using the Migration Center discovery client CLI.

The `mcdc` CLI lets you collect information about your Azure virtual machine (VM) instances. The `mcdc` CLI then sends this information to Migration Center, where you can continue with your assessment.

## Data collected during inventory discovery

The `mcdc` CLI collects the following information from Azure VMs:

  * Instance details (ID, name, type, state)
  * Instance type details (CPU, memory)
  * OS details (type and version)
  * Disk size
  * Network Interfaces (IP and MAC addresses)
  * Tags
  * Instance region
  * Performance metrics (CPU utilization, memory utilization, network I/O, disk I/O)



## Before you begin

  1. Review the [requirements for downloading and running the `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/review-collector-cli-requirements).
  2. Complete the steps to [download the `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/download-collector-cli). Migration Center doesn't support Azure PowerShell; use Azure CLI to run the `mcdc` CLI commands.



## Authenticate to Azure

To allow the `mcdc` CLI to access your Azure environment, you need to configure the access using one of the following methods:

  * Use your existing Azure credentials
  * Create a client secret for the `mcdc` CLI



### Use your existing Azure credentials

To use your existing Azure credentials, run the `mcdc` CLI commands directly from the Azure Cloud Shell. If you run the `mcdc` CLI from the Azure Cloud Shell, you can use your existing credentials without a client secret. In this case, the `mcdc` CLI can access your Azure environment to discover VM instances, as granted by your credentials.

### Create a client secret for the `mcdc` CLI

To allow the `mcdc` CLI access Azure resources, register the `mcdc` CLI as an application in your Azure account and create a client secret.

To create a client secret for the `mcdc` CLI, follow these steps:

  1. In the Azure portal, go to the **App Registration** page, and click **New registration**.
  2. To add new client credentials, click **Add a certificate or secret**.
  3. To add a new client secret, click **\+ New client secret** and enter a description and expiry date for the client secret.
  4. Click **Add**.



Your client secret is now ready to use. Copy the client secret value because you need it later when you run the `mcdc` CLI commands.

#### Create a custom role

To make sure that the `mcdc` CLI has the necessary permissions to access your Azure resources, you need to create a custom role with the required permissions.

To create a custom role, follow these steps:

  1. In the Azure portal, go to the [Subscriptions](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBlade) page and select your Azure subscription.
  2. Copy the **Subscription ID** by clicking it.
  3. Save the following JSON template and replace `SUBSCRIPTION_ID` with the **Subscription ID** you copied in Step 2:
         
         {
           "properties": {
                 "roleName": "Minimum permissions role",
                 "description": "This role contains the bare minimum of Azure IAM permissions",
                 "assignableScopes": [
                       "/subscriptions/SUBSCRIPTION_ID"
                 ],
           "permissions": [
                       {
                       "actions": [
                         "Microsoft.Compute/virtualMachines/read",
                         "Microsoft.Compute/disks/read",
                         "Microsoft.Insights/MetricDefinitions/read",
                         "Microsoft.Insights/Metrics/Read",
                         "Microsoft.Network/networkInterfaces/read"
                       ],
                       "notActions": [],
                       "dataActions": [],
                       "notDataActions": []
                       }
                 ]
           }
           }
           

For more information about the permission details, see [permission details](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/roles-reference#permissions_to_configure_azure_as_a_source).

  4. In the Azure portal, go to the **Access control (IAM)** page.

  5. To add a custom role, click **\+ Add**.

  6. Click **Start from JSON** and then click **Select file** to upload the JSON file you created in Step 3.

  7. To review your inputs click **Review + Create** , and then to create the custom role click **Create**.




#### Assign the custom role to the `mcdc` CLI

After you create the custom role, you need to assign it to the `mcdc` CLI application to grant it the necessary permissions.

To assign a custom role to the `mcdc` CLI, follow these steps:

  1. In the Azure portal, go to the **Access control (IAM)** page.
  2. Click **\+ Add** and then click **Add role assignment**.
  3. In the custom role that you created (Create a custom role), enter `m2vm` and select the role.
  4. Click **Next**.
  5. Click **\+ Select members** and search for the `mcdc` CLI that you registered in Register the `mcdc` CLI and click **Select**.
  6. To review and assign the custom role to your app, click **Review + Assign**.



## Discover VM instances on Azure

To collect inventory information from your Azure VM instances, follow these steps:

  1. In the command line terminal, change to the directory where you downloaded the `mcdc` CLI.

  2. Run the discovery:

### Azure Cloud Shell

To discover VM instances from Azure Cloud Shell by using your existing Azure credentials, run the following command:

### Linux
         
         ./mcdc discover azure --tenant TENANT_ID   
         
          --host-credentials   
         
          [--subscription SUBSCRIPTION_ID]   
         
          [--resource-group RESOURCE_GROUP]
          

### Windows
         
         mcdc.exe discover azure --tenant TENANT_ID   
         
          --host-credentials   
         
          [--subscription SUBSCRIPTION_ID]   
         
          [--resource-group RESOURCE_GROUP]
          

Replace the following:

     * TENANT_ID: the unique identifier for your Azure Active Directory (AAD) tenant.
     * SUBSCRIPTION_ID: the subscription ID that you want to discover. This flag is optional, if omitted all subscriptions in the tenant will be collected.
     * RESOURCE_GROUP: the Azure resource group that contains the VM instances that you want to discover. This flag is optional.

### Client secret

To discover VM instances from any computer with access to your Azure account by using the client secret, run the following command:

### Linux
    
    ./mcdc discover azure --tenant TENANT_ID   
    
     --client CLIENT_ID   
    
     --secret CLIENT_SECRET   
    
     [--subscription SUBSCRIPTION_ID]   
    
     [--resource-group RESOURCE_GROUP]
     

### Windows
    
    mcdc.exe discover azure --tenant TENANT_ID   
    
     --client CLIENT_ID   
    
     --secret CLIENT_SECRET   
    
     [--subscription SUBSCRIPTION_ID]   
    
     [--resource-group RESOURCE_GROUP]
     

Replace the following:

     * TENANT_ID: the unique identifier for your Azure Active Directory (AAD) tenant.
     * CLIENT_ID: the client ID you created in the Register the `mcdc` CLI section.
     * CLIENT_SECRET: the client secret you created in the Register the `mcdc` CLI section.
     * SUBSCRIPTION_ID: the subscription ID that you want to discover. This flag is optional, if omitted all subscriptions in the tenant will be collected.
     * RESOURCE_GROUP: the Azure resource group that contains the VM instances that you want to discover. This flag is optional.




The output should look similar to the following:
    
    
      [+] Collecting Azure VM instances...
      Collecting region eu-west-1
      Collected 73 Azure VM instances
      [✓] Collection completed.
    

After the discovery finishes, to review the collected data, run the `discover ls` command:

### Linux
    
    
    ./mcdc discover ls

### Windows
    
    
    mcdc.exe discover ls

The output should look similar to the following:
    
    
        VM Assets
        PLATFORM VM ID                        NAME              COLLECTED DATA   OS                          IP ADDRESSES
        4f7bd883-b9cd-42e8-a67d-af3ec82b7f29  abc-rhel9.0-arm   AZUREVM          Red Hat Enterprise Linux    192.0.2.1
        b5bcefcc-5565-4e45-a05a-fac055f73f14  def-rhel9.0-arm   AZUREVM          Red Hat Enterprise Linux    192.0.2.2
        sfbcesdc-8865-4e4t-a0sf-f8sfyjf75723  ghi-ol9.3         AZUREVM          Linux/UNIX                  192.0.2.3
    

## What's next

  * Learn how to [run a guest discovery](https://docs.cloud.google.com/migration-center/docs/run-guest-discovery).
  * Learn how to [export collected data to Migration Center](https://docs.cloud.google.com/migration-center/docs/export-collected-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
