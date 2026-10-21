---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-dynamics-365/
title: Collect Microsoft Dynamics 365 User Activity logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:08:56.758063+00:00
---

# Collect Microsoft Dynamics 365 User Activity logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-dynamics-365/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Dynamics 365 User Activity logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can collect Microsoft Dynamics 365 User Activity logs by setting up a Google SecOps feed using Microsoft Azure Blob Storage V2.

Microsoft Dynamics 365 is a cloud-based business applications platform that combines CRM and ERP capabilities. User activity logs capture actions and events performed by users within Dynamics 365 applications, including entity operations, data access, and administrative activities. Dynamics 365 is built on Microsoft Dataverse, which provides comprehensive audit logging through the Microsoft Purview unified audit log.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Microsoft Azure** portal with permissions to: 
    * Create Storage Accounts
    * Configure Azure Synapse Link for Dataverse
    * Manage access keys
  * A Microsoft 365 subscription that includes Dynamics 365
  * System Administrator security role in the Dynamics 365 environment
  * Global Administrator or Power Platform administrator access to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/)

**Note:** If you restrict access to your Azure resources using an Azure Storage firewall, you must add the IP ranges used by Storage Transfer Service (STS) workers to your list of allowed IPs. See [IP Allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip_allowlisting).



## Enable Dataverse auditing

Before exporting Dynamics 365 user activity logs, you must enable auditing in the Power Platform admin center.

  1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
  2. In the navigation pane, select **Environments**.
  3. Select the environment that contains your Dynamics 365 deployment.
  4. In the command bar, select **Settings**.
  5. Expand **Audit and logs** and select **Audit settings**.
  6. Under **Auditing** , enable the following options: 
     * **Start Auditing** : Activates auditing for the environment.
     * **Log access** : Tracks user sign-ins.
     * **Read logs** : Captures most user activities and events.
  7. Set the **Retention policy** for auditing logs based on your requirements.
  8. Select **Save** to apply the changes.



### Enable table-level auditing

  1. Sign in to [Power Apps](https://make.powerapps.com/) and select the environment.
  2. In the command bar, select **Settings > Advanced settings**.
  3. Go to **Settings > Customizations > Customize the System**.
  4. In the navigation pane, under **Components** , expand **Entities** and select the entity to audit (for example, **Account**).
  5. Scroll down to **Data Services** and enable the **Auditing** checkbox.
  6. Under **Auditing** , enable the following options: 
     * **Single record auditing. Log a record when opened.**
     * **Multiple record auditing. Log all records displayed on an opened page.**
  7. Select **Save** and then select **Publish**.
  8. Repeat steps 4-7 for each table you want to audit.



For more information, see [Microsoft Dataverse and model-driven apps activity logging](https://learn.microsoft.com/en-us/power-platform/admin/enable-use-comprehensive-auditing).

## Configure Azure Storage Account

### Create Storage Account

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Storage account name** | Enter a unique name (for example, `secopsd365logs`)  
**Region** | Select the same region as your Dataverse environment  
**Performance** | Standard (recommended)  
**Redundancy** | GRS (Geo-redundant storage) or LRS (Locally redundant storage)  
  4. Select the **Advanced** tab and enable the **Hierarchical Namespace** option.

**Note:** Hierarchical Namespace is required for Azure Data Lake Storage Gen2, which is used by Azure Synapse Link for Dataverse.
  5. Click **Review + create**.

  6. Review the overview of the account and click **Create**.

  7. Wait for the deployment to complete.




### Get Storage Account credentials

  1. Go to the **Storage Account** you just created.
  2. In the left navigation, select **Access keys** under **Security + networking**.
  3. Click **Show keys**.
  4. Copy and save the following for later use: 
     * **Storage account name** : `secopsd365logs`
     * **Key 1** or **Key 2** : The shared access key (a 512-bit random string in base-64 encoding)



### Get Blob Service endpoint

  1. In the same Storage Account, select **Endpoints** from the left navigation.
  2. Copy and save the **Blob service** endpoint URL. 
     * Example: `https://secopsd365logs.blob.core.windows.net/`



### Grant storage account permissions

Grant permissions to the Power Platform administrator who will configure the Azure Synapse Link:

  1. In the **Storage Account** , select **Access control (IAM)** in the left pane.
  2. Click **\+ Add > Add role assignment**.
  3. Assign the following roles to the Power Platform administrator: 
     * **Storage Blob Data Contributor**
     * **Storage Blob Data Owner**



## Configure Azure Synapse Link for Dataverse

Azure Synapse Link for Dataverse exports the Dataverse audit table to Azure Data Lake Storage Gen2, which is compatible with Azure Blob Storage V2 feeds.

### Create Azure Synapse workspace

  1. In the **Azure portal** , search for **Synapse Analytics**.
  2. Click **\+ Create**.
  3. Provide the following configuration details: 
     * **Subscription** : Select the subscription where you created the storage account.
     * **Resource group** : Select the same resource group as the storage account.
     * **Workspace name** : Enter a unique name (for example, `synapse-d365-secops`).
     * **Region** : Select the same region as your Dataverse environment.
     * **Storage account name** : Select the storage account you created earlier (`secopsd365logs`).
     * **File system name** : Click **Create new** and enter a name (for example, `d365-audit`).
  4. Click **Review + create** and then click **Create**.
  5. Wait for the deployment to complete.



### Create Apache Spark pool

  1. In the **Azure portal** , go to the Synapse workspace you created.
  2. Click **\+ New Apache Spark pool**.
  3. Provide the following configuration details: 
     * **Apache Spark pool name** : Enter a name (for example, `sparkpoold365`).
     * **Number of nodes** : Enter `5`.
  4. Select the **Additional settings** tab and enter `5` for the **Number of minutes idle**.
  5. Click **Review + create** and then click **Create**.



### Connect Dataverse audit table to Synapse workspace

  1. Sign in to [Power Apps](https://make.powerapps.com/) and select the environment containing your Dynamics 365 deployment.
  2. In the left navigation pane, select **Azure Synapse Link**. If the item is not visible, select **More > Discover all** and locate **Azure Synapse Link**.
  3. Click **New link**.
  4. On the **New link** page: 
     * Select the **Connect to your Azure Synapse Analytics workspace** option.
     * **Subscription** : Select the Azure subscription.
     * **Resource group** : Select the resource group containing the Synapse workspace.
     * **Storage account** : Select the storage account (`secopsd365logs`).
     * Select the **Use Spark pool for Delta Lake data conversion job** option.
     * **Spark pool** : Select the Spark pool you created (`sparkpoold365`).
     * **Storage account** : Select the same storage account.
  5. Click **Next**.
  6. Expand the **Advanced** tab and enter `480` minutes in the **Time interval** field.
  7. Under the list of tables, select the **Auditing** and **User** tables.
  8. Click **Save**.

**Note:** The export of the audit table is only supported with Delta Lake profiles. It may take some time for the initial export to complete. After completion, verify the sync status by returning to the **Azure Synapse Link** page and confirming the status is **Active**.



For more information, see [Access audit data with Azure Synapse Link and Power BI](https://learn.microsoft.com/en-us/power-platform/admin/audit-data-azure-synapse-link).

## Configure a feed in Google SecOps to ingest Microsoft Dynamics 365 User Activity logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft Dynamics 365 User Activity`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Microsoft Dynamics 365** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the container path:
    
    https://secopsd365logs.blob.core.windows.net/d365-audit/
    

Replace the following:

     * `secopsd365logs`: Your Azure storage account name.
     * `d365-audit`: The file system (container) name configured in the Synapse workspace.
**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:
     * **Never** : Never deletes any files after transfers.
     * **Delete transferred files** : Deletes files after successful transfer.
     * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Shared key** : Enter the shared key value (access key) you captured from the Storage Account earlier
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Configure Azure Storage firewall (if enabled)

If your Azure Storage Account uses a firewall, you must add Google SecOps IP ranges.

  1. In the **Azure portal** , go to your **Storage Account**.
  2. Select **Networking** under **Security + networking**.
  3. Under **Firewalls and virtual networks** , select **Enabled from selected virtual networks and IP addresses**.
  4. In the **Firewall** section, under **Address range** , click **\+ Add IP range**.
  5. Add each Google SecOps IP range in CIDR notation.

To get the current IP ranges:

     * See [IP Allowlisting documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip_allowlisting)
     * Or retrieve them programmatically using the [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api)
  6. Click **Save**.

**Note:** This feed source uses the Storage Transfer Service (STS) to transfer data from Azure storage to Google SecOps. Before using this feed source, you may need to add the IP ranges used by STS workers to your list of allowed IPs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
BuildNumber | about.labels | Merged about_BuildNumber with key "BuildNumber" and value from BuildNumber if not empty  
RECORD_IDENTIFIER | additional.fields | Merged with labels created from each respective field if not empty  
LastProcessedChange_DateTime | additional.fields |   
DataLakeModified_DateTime | additional.fields |   
Application_Object_Server_node | additional.fields |   
ClientType | additional.fields |   
LogoutDateTime | additional.fields |   
LOGOUTDATETIMETZID | additional.fields |   
TerminatedOk | additional.fields |   
Type | additional.fields |   
Alive | additional.fields |   
PARTITION | additional.fields |   
has_user | metadata.event_type | Set to "GENERIC_EVENT", then "USER_UNCATEGORIZED" if has_user true, else "STATUS_UPDATE" if has_principal true  
has_principal | metadata.event_type |   
RECVERSION | metadata.product_version | Value copied directly if not empty  
SessionId | network.session_id | Value copied directly if not empty  
LOG_SEQUENCE_NUMBER | security_result.detection_fields | Merged LOG_SEQUENCE_NUMBER_label with key "LOG_SEQUENCE_NUMBER" and value from LOG_SEQUENCE_NUMBER if not empty  
UserId | target.user.userid | Value copied directly if not empty  
timestamp | timestamp | Parsed using date match with ISO8601 or RFC 3339 format if not empty  
metadata.product_name | metadata.product_name | Set to "MICROSOFT_DYNAMICS_365"  
metadata.vendor_name | metadata.vendor_name | Set to "MICROSOFT_DYNAMICS_365"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-dynamics-365-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
