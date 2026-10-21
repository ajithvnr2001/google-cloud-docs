---
url: https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure/
title: Connect to Microsoft Azure for configuration and resource data collection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:29.702158+00:00
---

# Connect to Microsoft Azure for configuration and resource data collection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Connect to Microsoft Azure for configuration and resource data collection Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

You can connect Security Command Center Enterprise tier to your Microsoft Azure environment to do the following:

  * Enable the detection of findings related to misconfigurations.
  * Identify potential attack paths from the public internet to your high-value Microsoft Azure assets.
  * Map compliance of Microsoft Azure resources with various standards and benchmarks.



The Security Command Center to Microsoft Azure connection creates a single place for your team to manage and remediate misconfigurations in both Google Cloud and Azure.

You configure a trust connection between Security Command Center and Azure, using a [Google Cloud service agent](https://docs.cloud.google.com/iam/docs/service-agents) and a Microsoft Azure [user-assigned managed identity](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities) with access to Azure resources you want to monitor. You manage and control the trust configuration in your Microsoft Azure environment.

You can create one Azure connection for each Google Cloud organization.

Security Command Center uses this connection to periodically collect data about Microsoft Azure resources that you define. This data is handled in the same way as Service Data per the [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). The connector uses API calls to collect Azure asset data. These API calls may incur Microsoft Azure charges.

During a scan, the data collection pipeline depends on the service agent to authenticate to the Microsoft Azure environment using the user-assigned managed identity.

The following diagram shows how trust is established between Security Command Center and Azure.

![Azure and Security Command Center configuration.](https://docs.cloud.google.com/static/security-command-center/images/azure-scc-connection.png)

This document describes how to set up the connection with Microsoft Azure. At a high level, the steps are the following:

  1. Perform the prerequisite steps in Before you begin.

  2. Create the Azure connector and configure which subscriptions and locations to scan. You need the Microsoft Azure [Tenant ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant) to do these steps. This creates the service agent ID.

  3. Configure the Azure environment to create a dedicated user-assigned managed identity with the following roles:

     * [Reader](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview#root-management-group-for-each-directory) in the scope of the Microsoft Azure root management group to read resources, subscriptions, and management group hierarchy.

     * [Key Vault Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/security#key-vault-reader) in the scope of the Microsoft Azure root management group to read metadata about key vaults and related certificates, keys, and secrets.

     * [Storage Blob Data Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-reader) in the scope of the Microsoft Azure root management group to read metadata about resources. Grant this role if you plan to enable **Grant permissions for Sensitive Data Protection discovery** when you configure the Azure connector.

     * [Directory readers](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#directory-readers) in Microsoft Entra ID to read groups and memberships.

     * [Security reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) in Microsoft Entra ID to read authorization policies.

The default display name for the root management group is [`Tenant root group`](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview#important-facts-about-the-root-management-group).

These permissions are needed for Security Command Center to identify management groups, groups with memberships, and role definitions, which are located at a level higher than subscriptions in the resource hierarchy.

You also configure a federated identity credential for the user-assigned managed identity using information about the service agent.

You can either do the steps manually or use Terraform. You need the service agent ID when doing the steps manually.

  4. Complete the configuration of the Azure connector and test the connection. You use information about the user-assigned managed identity to do these steps.




## Data collection types

Depending on your security goals, you can connect Security Command Center to Microsoft Azure to collect different types of data:

  * **Resource and configuration data** : The Azure connector configured on this page collects configuration metadata and resource data to discover misconfigurations, assess your security posture, and identify attack paths.
  * **Log data** : To power the SIEM curated detection capabilities and analyze Microsoft Azure event logs, you configure a separate connection for log ingestion. For more information, see [Connect to Microsoft Azure for log data collection](https://docs.cloud.google.com/security-command-center/docs/connect-secops-azure).



## Before you begin

The following sections describe the prerequisites, decisions, and information needed before you configure the connection between Security Command Center and Microsoft Azure.

### Review Microsoft Azure features

Make sure you are familiar with the following concepts and capabilities in Microsoft Azure:

  * [Managing user-assigned managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities).

  * [Workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) in Azure, [federated credentials](https://learn.microsoft.com/en-us/graph/api/resources/federatedidentitycredentials-overview?view=graph-rest-1.0), and [configuring a federated identity on a user-assigned managed identity](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust-user-assigned-managed-identity).

  * Creating and managing resource groups using the [Microsoft Azure portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal), the [Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli), or [Terraform](https://learn.microsoft.com/en-us/azure/developer/terraform/).

  * Assigning [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) and [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).




### Plan for the data collection

When you plan the data collection strategy, do the following. You need this information when performing the steps in this document.

  * Create or identify the resource group where you will create the user-defined managed identity. You need the resource group name during configuration.

Replace the RESOURCE_GROUP_NAME variable with the resource group name to populate the value in upcoming steps of this document.

  * Identify the resources that you want to collect data for. If you plan to collect data from only specific subscriptions or regions, identify and record these during planning.

You can also configure the Azure connector to discover resources automatically across all subscriptions and regions.




### Set up permissions in Google Cloud

In Google Cloud, to create and manage a connection to the third-party cloud providers, you must be granted the [Cloud Asset Owner (`roles/cloudasset.owner`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.owner) role in the organization. For more information about granting roles, see [Manage Access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Set up permissions in Microsoft Azure

To do the steps in Configure Microsoft Azure manually or Configure Microsoft Azure using Terraform, you must have an Azure identity with at least one resource group created, plus the following permissions to configure IAM policies for Microsoft Azure and Microsoft Entra.

  * `Microsoft.Authorization/roleAssignments/write` permission in scope of the root management group. This is available in either of the following built-in roles: [Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator) or [User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator).

  * The following permissions in the scope of a resource group where the user-assigned managed identity will be created:

    * `Microsoft.ManagedIdentity/userAssignedIdentities/write`
    * `Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentials/write`

These are available in the built-in [Managed Identity Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/identity#managed-identity-contributor) role.

  * The Microsoft Entra permission, `microsoft.directory/roleAssignments/allProperties/allTasks`. This is available in the Microsoft Entra built-in role [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator).




You must have elevated access to set permissions in the scope of the root management group. See [Elevate access to manage all Azure subscriptions and management groups](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin) for the steps to elevate access for a Global Administrator.

## Enable and configure the Security Command Center Azure connector

Do the following to create and configure the Azure connector.

### Initiate the connector configuration

  1. Make sure you have the permissions defined in the section Set up permissions in Google Cloud.

  2. Make sure you have the 36-character Microsoft Azure [Tenant ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant).

  3. Open the **Connectors** tab on the **Settings** page.

[Go to Connectors](https://console.cloud.google.com/security/command-center/config/connectors)

  4. Select the organization where you activated Security Command Center Enterprise.

  5. Click **Add connector** > **Microsoft Azure**.

  6. On the **Configure connector** page, enter the **Azure tenant ID**.

  7. To let Sensitive Data Protection profile your Azure data, keep **Grant permissions for Sensitive Data Protection discovery** selected. This option adds the Storage Blob Data Reader role in the Terraform template for the user-defined managed identity.

**Note:** This option only grants the required permissions to the Azure connector. To profile your Azure data, see [Profile Azure Blob Storage data](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-azure-blob-storage) after creating this connector.



### Specify subscriptions and locations

  1. Select either of the following:

     * **Add subscriptions automatically** : Security Command Center will automatically discover and include subscriptions and management groups. You can optionally exclude subscription IDs from being collected by adding them to the **Exclude Azure subscriptions** field.

     * **Add subscriptions individually** : Security Command Center will not automatically discover subscriptions. You must define at least one subscription using the **Add Azure Subscription** field.

  2. Under the **Select Azure locations to collect data from** section, optionally select one or more Microsoft Azure locations to collect data from. Leave this field empty to collect from all locations. When you select a location from the menu, the deselected locations are excluded.

The recommended settings are **Automatically discover your Azure subscriptions** and use all Microsoft Azure locations.

  3. Click **Next**. The **Connect to Azure** page opens.

From there, you must configure Microsoft Azure before you save or continue on this page. For instructions, see Configure the Microsoft Azure environment.

After you configure Microsoft Azure, follow Complete the Azure connector configuration.




## Configure the Microsoft Azure environment

Complete one of the following sections:

  * Configure Microsoft Azure manually

  * Configure Microsoft Azure using Terraform




### Configure Microsoft Azure manually

The following section describes high-level manual steps to configure the Azure environment that establishes trust between Security Command Center and Microsoft Azure. This procedure is not comprehensive. Each section provides links to Microsoft Azure documentation that explains how to accomplish that task.

#### Prerequisites

  * Make sure you have the permissions defined in the section Set up permissions in Microsoft Azure.

  * Make sure you have the service agent ID, which was generated when you created the Security Command Center Azure connector.




#### Step 1: Create a user-assigned managed identity in a resource group

  1. Follow the steps in [Manage user-assigned managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities) to create the user-assigned managed identity.

When creating the identity, specify the following:

     * **Subscription** : Select the subscription where the identity will be managed.
     * **Resource group** : Specify the resource group name, RESOURCE_GROUP_NAME, where the identity will be managed. You identified this when planning for the data collection.
     * **Region** : Select a region, for example, `East US`.
     * **Name** : Enter a name for the user-assigned managed identity, for example: `gcp-managed-identity`. Replace the variable USER_ASSIGNED_MANAGED_IDENTITY_NAME with the identity name and it will be populated in the steps of this document where it is required.
  2. Record the following information. You will use this in upcoming steps.

     * Client ID: the 36-character value assigned to the identity.
     * Object (principal) ID: the 36-character value assigned to the identity.
     * Identity name: the value you defined for the **Name**.



#### Step 2: Create a federated credential for the user-assigned managed identity

To add a federated credential in the user-assigned managed identity, follow the steps in [Configure a user-assigned managed identity to trust an external identity provider](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust-user-assigned-managed-identity?pivots=identity-wif-mi-methods-azp#configure-a-federated-identity-credential-on-a-user-assigned-managed-identity).

Use the guidance described by the [Other issuer scenario](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust-user-assigned-managed-identity?pivots=identity-wif-mi-methods-azp#configure-a-federated-identity-credential-on-a-user-assigned-managed-identity) and set the following:

  * **Federated credential scenario** : Choose **Other: Configure an identity managed by an external OpenID Connect provider to access Microsoft Azure resources as this application**.
  * **Issuer URL** : Enter `https://accounts.google.com`.
  * **Subject identifier** : Enter the service agent ID generated when you created the Security Command Center Azure connector.
  * **Name** : Enter a name for the federated credential, for example: `gcp-managed-identity-fic`.
  * **Audience** : Enter `https://cloud.google.com`.



#### Step 3: Assign Microsoft Azure built-in roles

Follow the steps in [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) to assign the following [Microsoft Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) to the user-assigned managed identity:

  * Key Vault Reader
  * Reader
  * Storage Blob Data Reader



Grant these roles at the root management group scope.

#### Step 4: Assign the Microsoft Entra ID built-in roles

Follow the steps in [Assign Microsoft Entra roles to users](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal) to assign the following [Microsoft Entra ID built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) to the user-assigned managed identity:

  * Directory Readers
  * Security Reader



After you assign the roles, complete the Azure connector configuration.

### Configure Microsoft Azure using Terraform

The following high-level steps describe how to use Terraform to configure Microsoft Azure. This procedure is not comprehensive. For more detail about using Terraform to provision resources, see [Terraform on Azure documentation](https://learn.microsoft.com/en-us/azure/developer/terraform/).

#### Download Terraform templates

  1. Open the **Connect to Azure** page that you left open when you created the Azure connector.

  2. Click **Download Terraform Templates**. This downloads the `azure_terraform.zip` file containing multiple JSON files.




#### Prepare the Terraform environment

  1. Sign in to Microsoft Azure, and then open Azure Cloud Shell with either Bash or Azure PowerShell.

  2. Configure Terraform according to your organization policies using one of the following instructions:

     * [Configure Terraform in Azure Cloud Shell with Bash](https://learn.microsoft.com/en-us/azure/developer/terraform/get-started-cloud-shell-bash)
     * [Configure Terraform in Azure Cloud Shell with Azure PowerShell](https://learn.microsoft.com/en-us/azure/developer/terraform/get-started-cloud-shell-powershell)
  3. Copy the `azure_terraform.zip` file to your Azure Cloud Shell environment, and then extract the contents. You will see the following files: `main.tf.json`, `outputs.tf.json`, `providers.tf.json`, and `variables.tf.json`.

  4. Create copies of these files in a separate directory:

     1. Create a new directory to test the sample Terraform code and make it the current directory.
     2. In the newly created directory, create copies of the extracted JSON files with the same name as the original file:

        * Create a new file named `main.tf.json`, and then copy and paste the code from the extracted `main.tf.json` file.
        * Create a new file named `providers.tf.json`, and then copy and paste the code from the extracted `providers.tf.json` file.
        * Create a new file named `outputs.tf.json`, and then copy and paste the code from the extracted `outputs.tf.json` file.
        * Create a new file named `variables.tf.json`, and then copy and paste the code from the extracted `variables.tf.json` file.



#### Deploy the execution plan

  1. Run the following command to initialize the Terraform deployment.
         
         terraform init -upgrade
         

  2. Run the following command to create an execution plan.
         
         terraform plan -out main.tfplan -var="resource_group_name=RESOURCE_GROUP_NAME" -var="user_assigned_managed_identity_name=USER_ASSIGNED_MANAGED_IDENTITY_NAME"
         

Replace the following:

     * `RESOURCE_GROUP_NAME`: the name of the Microsoft Azure resource group where the user-assigned managed identity will be created.
     * `USER_ASSIGNED_MANAGED_IDENTITY_NAME`: the name of the user-assigned managed identity to be created. If this is not specified, the default value is `google-cloud-managed-identity`.
  3. Execute the following command to apply the execution plan to the Microsoft Azure infrastructure.
         
         terraform apply main.tfplan
         




After you finish these steps, complete the Azure connector configuration.

## Complete the Azure connector configuration

  1. Make sure you have the following information about the Microsoft Azure user-assigned managed identity:

     * _Client ID_ : the 36-character value assigned to the identity.
     * _Object (principal) ID_ : the 36-character value assigned to the identity.

For information about how to find this information, see [List user-assigned managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities).

  2. Open the **Connect to Azure** page that you left open when you created the Azure connector.

  3. Under the **Azure managed identity details** section, enter the following:

     * **Managed identity client ID** : this is the _Client ID_.
     * **Managed identity object ID** : this is the _Object (principal) ID_.
  4. Click **Continue**.

  5. In the **Test connector** page, click **Test Connector** to verify that Security Command Center can connect to the Microsoft Azure environment.

If the connection is successful, Google Cloud service agent can assume the Microsoft Azure user-assigned managed identity and has the required Microsoft Azure and Microsoft Entra permissions. If the connection isn't successful, see Troubleshooting errors when testing the connection.

  6. Click **Save**. The **Connectors** page appears.




The connector starts scanning and collecting data from the Azure subscriptions and locations that you specified. It might take up to 24 hours for findings to appear.

## Troubleshooting errors when testing the connection

The following section describes errors that may occur when you test the connection between Security Command Center and Microsoft Azure, and how to resolve each.

### AZURE_ENABLED_SUBSCRIPTIONS_NOT_FOUND error

The Azure connector didn't find [enabled subscriptions](https://learn.microsoft.com/en-us/rest/api/resources/subscriptions/list?view=rest-resources-2022-12-01&tabs=HTTP#subscriptionstate) in the tenant identified by the **Azure tenant ID** field. Check for the following:

  * If **Add subscriptions automatically** is selected, check that the tenant includes subscriptions that are in the `Enabled` state and that don't appear in the **Exclude Azure subscriptions** field.
  * If **Add subscriptions individually** is selected, check that the subscriptions you specified have the `Enabled` state.



### AZURE_FAILED_TO_ASSUME_MANAGED_IDENTITY error

The connection is invalid because the Microsoft Azure user-assigned managed identity can't be assumed by the Google Cloud service agent. The following may be possible causes:

  * The user-assigned managed identity specified in the connection does not exist or the configuration is incorrect.
  * The user-assigned managed identity specified in the connection may be missing the federated identity credential required to trust the Google Cloud service agent.



To resolve this issue, do the following:

  * Review the settings when you created the user-assigned managed identity in a resource group to ensure that identity exists and that the configuration is correct.
  * Review the settings defined in the federated identity credential to ensure that the configuration is correct.



### AZURE_MANAGED_IDENTITY_MISSING_REQUIRED_PERMISSION error

The connection is invalid because the Azure user-assigned managed identity is missing a required Microsoft Azure or Microsoft Entra role. The error message includes the missing role.

To resolve this issue, review the settings that you set when you configured the Microsoft Azure built-in roles and Microsoft Entra built-in roles to ensure that the configuration is correct.

### AZURE_MANAGED_IDENTITY_ASSUMPTION_FAILED_AND_MISSING_REQUIRED_PERMISSION error

The connection is invalid because the Microsoft Azure user-assigned managed identity has failed to be assumed by the Google Cloud service agent and, at the same time, is missing some of the required Microsoft Azure or Microsoft Entra roles.

The error message includes details about which scope the user-assigned managed identity failed to assume and which roles are missing.

To resolve this issue, do the following:

  * Review the settings assigned when you created the user-assigned managed identity in a resource group to ensure that the identity in the connection exists and that the settings are correct.
  * Review the settings that you set when you configured the Microsoft Azure built-in roles and Microsoft Entra built-in roles to ensure that the configuration is correct.



## Other troubleshooting tips

The following section describes behaviors and possible steps to address.

### Finding is returned for a deleted Azure resource

After an Azure resource is deleted, it can take up to 40 hours for it to be removed from the Security Command Center asset inventory system. If you choose to resolve a finding by deleting the resource, you may see the finding reported within this time period because the asset has not yet been removed from the Security Command Center asset inventory system.

## Modify an existing Azure connector

You can modify an existing Azure connector to update permissions, add or remove Azure subscriptions, or adjust locations. For instructions, see [Modify the connector for Azure](https://docs.cloud.google.com/security-command-center/docs/modify-scc-to-azure-connector).

## What's next

  * If you are setting up Security Command Center Enterprise for the first time, [configure additional features using the set up guide](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier#monitor-configure-enterprise-tab).
  * You can also do the following:

    * [Review and remediate findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings) from Azure data.
    * [View resources](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console) related to findings in the Security Operations console.
    * View [attack path simulations for Azure resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
