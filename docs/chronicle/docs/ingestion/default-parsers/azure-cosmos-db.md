---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-cosmos-db/
title: Collect Azure Cosmos DB logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:31.894344+00:00
---

# Collect Azure Cosmos DB logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-cosmos-db/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Azure Cosmos DB logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how to collect Azure Cosmos DB logs by setting up a Google Security Operations feed using Microsoft Azure Blob Storage.

Azure Cosmos DB is a fully managed, globally distributed, multi-model database service designed for low-latency, elastic scalability, and high availability. It supports multiple APIs including NoSQL, MongoDB, Apache Cassandra, Apache Gremlin, and Table. The diagnostic logs capture data plane requests, control plane operations, query runtime statistics, and partition key consumption metrics.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Microsoft Azure** portal with permissions to: 
    * Create Storage Accounts
    * Configure Diagnostic Settings for Azure Cosmos DB
    * Manage access keys
  * An existing Azure Cosmos DB account with appropriate permissions to configure diagnostic settings

**Note:** If you restrict access to your Azure resources using an Azure Storage firewall, you must add the IP ranges used by Storage Transfer Service (STS) workers to your list of allowed IPs. See [IP Allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip_allowlisting).

## Configure an Azure Storage Account

### Create a Storage Account

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Storage account name** | Enter a unique name (for example, `cosmosdbsecops`)  
**Region** | Select the region (for example, `East US`)  
**Performance** | Standard (recommended)  
**Redundancy** | GRS (Geo-redundant storage) or LRS (Locally redundant storage)  
  4. Click **Review + create**.

  5. Review the overview of the account and click **Create**.

  6. Wait for the deployment to complete.




### Get Storage Account credentials

  1. Go to the **Storage Account** you just created.
  2. In the left navigation, select **Access keys** under **Security + networking**.
  3. Click **Show keys**.
  4. Copy and save the following for later use: 
     * **Storage account name** : Your storage account name (for example, `cosmosdbsecops`)
     * **Key 1** or **Key 2** : The shared access key (a 512-bit random string in base-64 encoding)



### Get a Blob Service endpoint

  1. In the same Storage Account, select **Endpoints** from the left navigation.
  2. Copy and save the **Blob service** endpoint URL. 
     * Example: `https://cosmosdbsecops.blob.core.windows.net/`



## Configure Azure Cosmos DB diagnostic settings

  1. In the **Azure portal** , search for **Azure Cosmos DB**.
  2. Select your Azure Cosmos DB account.
  3. In the left navigation, select **Diagnostic settings** under **Monitoring**.
  4. Click **\+ Add diagnostic setting**.
  5. Provide the following configuration details: 
     * **Diagnostic setting name** : Enter a descriptive name (for example, `cosmosdb-to-secops`).
     * In the **Logs** section, select the following categories: 
       * **DataPlaneRequests** : Data plane operation logs including read, write, and delete requests
       * **QueryRuntimeStatistics** : Query text and runtime statistics for executed queries
       * **PartitionKeyStatistics** : Storage consumption statistics for logical partition keys
       * **PartitionKeyRUConsumption** : Request unit consumption per logical partition key
       * **ControlPlaneRequests** : Control plane operations including account modifications, failover policy changes, indexing policy updates, VNet and firewall rule changes, and IAM role assignments
       * **TableApiRequests** : Data plane requests for Table API accounts (if applicable)
       * **MongoRequests** : Data plane requests for MongoDB API accounts (if applicable)
       * **CassandraRequests** : Data plane requests for Cassandra API accounts (if applicable)
       * **GremlinRequests** : Data plane requests for Gremlin API accounts (if applicable)
     * In the **Destination details** section, select the **Archive to a storage account** checkbox.
     * **Subscription** : Select the subscription containing your storage account.
     * **Storage account** : Select the storage account you created (for example, `cosmosdbsecops`).
  6. Click **Save**.

**Note:** Select only the log categories relevant to the APIs you use in your Cosmos DB account. For example, if you use the NoSQL API, select **DataPlaneRequests** , **QueryRuntimeStatistics** , **PartitionKeyStatistics** , **PartitionKeyRUConsumption** , and **ControlPlaneRequests**. After configuration, it may take a few minutes for the first logs to appear in the storage account. Each selected log category creates a separate container with the naming pattern `insights-logs-{category-name}`.



## Understanding the blob container structure

  * After configuration, logs are stored in the following structure:
        
        https://<storage-account>.blob.core.windows.net/
          insights-logs-<log-category>/
            resourceId=/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.DocumentDB/databaseAccounts/<account-name>/
              y=<year>/m=<month>/d=<day>/h=<hour>/m=<minute>/
                PT1H.json
        




**Example containers created by diagnostic settings:**

  * `insights-logs-dataplanerequests`
  * `insights-logs-queryruntimestatistics`
  * `insights-logs-partitionkeystatistics`
  * `insights-logs-partitionkeyruconsumption`
  * `insights-logs-controlplanerequests`



## Configure a feed in Google SecOps to ingest Azure Cosmos DB logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Azure Cosmos DB Logs`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Azure Cosmos DB** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the container path:
           
           https://cosmosdbsecops.blob.core.windows.net/insights-logs-dataplanerequests/
           

Replace the following:

     * `cosmosdbsecops`: Your Azure storage account name.
     * `insights-logs-dataplanerequests`: The blob container name where logs are stored.
**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers.
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Shared key** : Enter the shared key value (access key) you captured from the Storage Account.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Ingesting from multiple containers

If you selected multiple log categories in the diagnostic settings, each category creates a separate blob container. Create a separate feed for each container you want to ingest:

  1. Create a feed for the primary data plane logs (as shown above).
  2. Click **Add New Feed** to create additional feeds.
  3. Use the same storage account credentials but different container paths in the **Azure URI**.



**Example:**

  * Feed 1 (Data Plane Requests): `https://cosmosdbsecops.blob.core.windows.net/insights-logs-dataplanerequests/`
  * Feed 2 (Query Runtime Statistics): `https://cosmosdbsecops.blob.core.windows.net/insights-logs-queryruntimestatistics/`
  * Feed 3 (Control Plane Requests): `https://cosmosdbsecops.blob.core.windows.net/insights-logs-controlplanerequests/`
  * Feed 4 (Partition Key RU Consumption): `https://cosmosdbsecops.blob.core.windows.net/insights-logs-partitionkeyruconsumption/`
  * Feed 5 (Partition Key Statistics): `https://cosmosdbsecops.blob.core.windows.net/insights-logs-partitionkeystatistics/`

**Note:** Select **Azure Cosmos DB** as the **Log type** for all feeds.



## Configure an Azure Storage firewall (if enabled)

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
`activity_id_label` | `additional.fields` | Merged  
`additional_Channel` | `additional.fields` | Merged  
`additional_Event_Origin_Id` | `additional.fields` | Merged  
`additional_Management_Group_Name` | `additional.fields` | Merged  
`additional_Source_System` | `additional.fields` | Merged  
`additional_Task` | `additional.fields` | Merged  
`auth_token_type_label` | `additional.fields` | Merged  
`collection_rid_label` | `additional.fields` | Merged  
`connection_mode_label` | `additional.fields` | Merged  
`key_type_label` | `additional.fields` | Merged  
`number_of_rows_returned_label` | `additional.fields` | Merged  
`operation_name_label` | `additional.fields` | Merged  
`param_value` | `additional.fields` | Mapped: `true` → `parameter_label`  
`parameter_label` | `additional.fields` | Merged  
`partition_id_label` | `additional.fields` | Merged  
`shapesignature_label` | `additional.fields` | Merged  
`signature_label` | `additional.fields` | Merged  
`properties.partialipaddress` | `intermediary.ip` | Merged  
`Activity` | `metadata.description` | Directly mapped  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`TenantId` | `metadata.product_deployment_id` | Directly mapped  
`EventSourceName` | `metadata.product_event_type` | Directly mapped  
`category` | `metadata.product_event_type` | Directly mapped  
`EventID` | `metadata.product_log_id` | Directly mapped  
`properties.statusCode` | `network.http.response_code` | Directly mapped  
`properties.userAgent` | `network.http.user_agent` | Directly mapped  
`properties.useragent` | `network.http.user_agent` | Directly mapped  
`properties.responseLength` | `network.received_bytes` | Directly mapped  
`properties.requestLength` | `network.sent_bytes` | Directly mapped  
`SubjectDomainName` | `principal.administrative_domain` | Directly mapped  
`domain` | `principal.administrative_domain` | Directly mapped  
`SourceComputerId` | `principal.asset.asset_id` | Directly mapped  
`Computer` | `principal.hostname` | Directly mapped  
`properties.clientIpAddress` | `principal.ip` | Merged  
`EventSourceName` | `principal.platform` | Mapped: `(?i)Windows` → `WINDOWS`, `(?i)mac` → `MAC`, `(?i)Linux` → `LINUX`  
`SubjectUserName` | `principal.user.user_display_name` | Directly mapped  
`user_name` | `principal.user.user_display_name` | Directly mapped  
`Account` | `principal.user.userid` | Directly mapped  
`SubjectLogonId` | `principal.user.userid` | Directly mapped  
`SubjectUserSid` | `principal.user.windows_sid` | Directly mapped  
`properties.queryexecutionstatus` | `security_result.summary` | Directly mapped  
`TargetDomainName` | `target.administrative_domain` | Directly mapped  
`target_application` | `target.application` | Renamed/mapped  
`FilePath` | `target.file.full_path` | Directly mapped  
`FileHash` | `target.file.sha256` | Directly mapped  
`properties.region` | `target.location.country_or_region` | Directly mapped  
`CommandLine` | `target.process.command_line` | Directly mapped  
`properties.querytext.query` | `target.process.command_line` | Directly mapped  
`Process` | `target.process.file.full_path` | Directly mapped  
`ParentProcessName` | `target.process.parent_process.file.full_path` | Directly mapped  
`ProcessId` | `target.process.pid` | Directly mapped  
`Token_Elevation_Type` | `target.resource.attribute.labels` | Merged  
`Workspace_Resource_Id` | `target.resource.attribute.labels` | Merged  
`resource_attribute_labels` | `target.resource.attribute.labels` | Renamed/mapped  
`properties.databaseName` | `target.resource.name` | Directly mapped  
`properties.databasename` | `target.resource.name` | Directly mapped  
`_ResourceId` | `target.resource.product_object_id` | Directly mapped  
`resourceId` | `target.resource.product_object_id` | Directly mapped  
`properties.collectionName` | `target.resource.resource_subtype` | Directly mapped  
`properties.collectionname` | `target.resource.resource_subtype` | Directly mapped  
`TargetUserName` | `target.user.user_display_name` | Directly mapped  
`TargetLogonId` | `target.user.userid` | Directly mapped  
`TargetUserSid` | `target.user.windows_sid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `USER_RESOURCE_ACCESS`  
N/A | `metadata.product_name` | Constant: `Azure Cosmos DB`  
N/A | `metadata.vendor_name` | Constant: `Microsoft`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `target.resource.resource_type` | Constant: `DATABASE`  
`_Internal_WorkspaceResourceId", "TokenElevationType` | `target.resource.attribute.labels` | Mapped from changelog  
`Channel", "Task", "SourceSystem", "EventOriginId", "ManagementGroupName` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-cosmos-db-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
