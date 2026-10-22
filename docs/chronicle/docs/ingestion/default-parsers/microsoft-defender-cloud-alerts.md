---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-cloud-alerts/
title: Collect Microsoft Defender for Cloud alerts \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:06.485269+00:00
---

# Collect Microsoft Defender for Cloud alerts  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-cloud-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Defender for Cloud alerts

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Microsoft Defender for Cloud (formerly Azure Security Center) alerts to Google Security Operations. You can configure ingestion using two supported methods:

  * **Method 1: Azure Event Hub (recommended)** : Defender for Cloud Continuous Export streams alerts directly to an Azure Event Hub, from where Google SecOps ingests them in near real time.
  * **Method 2: Azure Blob Storage V2** : Defender for Cloud Continuous Export delivers alerts to a Log Analytics workspace, a Log Analytics Data Export rule writes them to an Azure Storage Account, and Google SecOps ingests them from the blob container on a polling schedule.



Microsoft Defender for Cloud is a cloud-native application protection platform that provides unified security management and threat protection across Azure, hybrid, and multi-cloud workloads.

**Note:** An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `MICROSOFT_DEFENDER_CLOUD_ALERTS` ingestion label.

## Before you begin

Ensure that you have the following prerequisites:

  * **Common to both methods:**

    * A Google SecOps instance.
    * Privileged access to the **Microsoft Azure** portal with permissions to: 
      * Configure Continuous Export on a Microsoft Defender for Cloud subscription.
    * **Security Admin** or **Owner** role on the Azure subscription containing Microsoft Defender for Cloud.
    * Microsoft Defender for Cloud enabled on the subscription with at least one Defender plan active.
  * **Method 1 additional prerequisites (Azure Event Hub):**

    * Permissions to create Event Hub namespaces and Event Hubs and to manage Event Hub access policies.
    * **Write** permissions on the target Event Hub policy (required by Continuous Export).
  * **Method 2 additional prerequisites (Azure Blob Storage V2):**

    * Permissions to create or manage a Log Analytics workspace and to create Data Export rules on it.
    * Permissions to create an Azure Storage Account with a blob container and to retrieve its access keys.

**Note:** You can create up to 10 Azure Event Hub feeds per Google SecOps instance, including both active and inactive feeds. For details on the canonical Azure Event Hub feed setup, see [Create an Azure Event Hub feed](https://docs.cloud.google.com/chronicle/docs/administration/create-azure-feed).

## Method 1: Azure Event Hub (recommended)

Use this method when you want near-real-time ingestion of Defender for Cloud alerts and you can grant Google SecOps access to an Azure Event Hub.

### Create Event Hub namespace

An Event Hub namespace is a management container for one or more Event Hubs.

  1. In the **Azure portal** , search for **Event Hubs**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select the subscription containing Microsoft Defender for Cloud.  
**Resource group** | Select existing or create new.  
**Namespace name** | Enter a unique name (for example, `secops-defender-ns`).  
**Location** | Select the same region as your Google SecOps instance (deploying in a different region reduces ingestion throughput).  
**Pricing tier** | Standard (recommended for production).  
**Throughput units** | Start with `1`, enable **Auto-inflate** (recommended).  
  4. Click **Review + create**.

  5. Review the overview and click **Create**.

  6. Wait for the deployment to complete (1-2 minutes).

**Note:** One throughput unit (TU) supports up to 1 MB per second of data ingestion (1 MB/s ingress, 2 MB/s egress). If incoming event volume exceeds the capacity of the configured TUs, the Event Hub may crash and logs may be lost before they reach Google SecOps. Enable **Auto-inflate** to automatically scale throughput up as alert volume grows.



### Create Event Hub

  1. After the namespace is deployed, go to the Event Hub namespace.
  2. In the left navigation, select **Event Hubs** under **Entities**.
  3. Click **\+ Event Hub**.
  4. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | Enter a unique name that matches the log type (for example, `defender-cloud-alerts`); avoid leaving the field blank during Defender Continuous Export configuration to prevent the system from creating extra event hubs.  
**Partition count** | `40` (recommended for optimal Google SecOps scaling).  
**Message retention** | `7` days minimum. Set the longest retention you can afford so logs are not deleted before ingestion resumes after a quota throttle.  
**Capture** | Disabled (not needed for direct Event Hub ingestion).  
  5. Click **Create**.

**Note:** **Partition count** of `40` is recommended for Google SecOps feeds. This setting cannot be changed later in the standard and basic tiers.



### Get Event Hub connection string

Google SecOps requires a connection string to authenticate to the Event Hub.

#### Option A: Namespace-level connection string (recommended)

  1. Go to the **Event Hub namespace**.
  2. In the left navigation, select **Shared access policies** under **Settings**.
  3. Click the default policy **RootManageSharedAccessKey**.
  4. Copy the **Connection string-primary key**.
  5. Save this connection string securely.

**Important:** When using a namespace-level connection string, you must **remove the`EntityPath` parameter** before providing it to Google SecOps.

**Example:**
         
         Original: Endpoint=sb://secops-defender-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=abc123==;EntityPath=defender-cloud-alerts
         
         Remove EntityPath: Endpoint=sb://secops-defender-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=abc123==
         




#### Option B: Event Hub-level connection string

  1. Go to the **Event Hub** (not the namespace).
  2. In the left navigation, select **Shared access policies** under **Settings**.
  3. Click **\+ Add** to create a new policy.
  4. Provide the following configuration details: 
     * **Policy name** : enter a descriptive name (for example, `chronicle-listen`).
     * **Permissions** : select **Listen** only (read-only access).
  5. Click **Create**.
  6. Click the newly created policy.
  7. Copy the **Connection string-primary key**.
  8. Save this connection string securely.

**Note:** Event Hub-level connection strings already include the `EntityPath` parameter, so no modification is needed.



### Configure Microsoft Defender for Cloud to stream alerts to Event Hub

Microsoft Defender for Cloud uses the **Continuous Export** feature to stream alerts and recommendations to an Event Hub as they are generated.

  1. Sign in to the **Azure portal**.
  2. Search for and open **Microsoft Defender for Cloud**.
  3. In the Defender for Cloud resource menu, select **Environment settings**.
  4. Select the **subscription** that you want to configure data export for.
  5. In the resource menu under **Settings** , select **Continuous export**.
  6. Select the **Event hub** tab.
  7. Provide the following configuration details: 
     * **Export enabled?** : toggle to the on position.
     * In the **Exported data types** section, select the data types to export. To collect security alerts, select the following checkboxes: 
       * **Security alerts**
       * (Optional) **Security recommendations** , **Secure score** , **Regulatory compliance** , **Attack paths** , and other types as needed
     * For each selected data type, configure filters (for example, export only **Low** , **Medium** , **High** , or all severity levels).
     * In the **Export frequency** section, select the frequency: 
       * **Streaming** : sends alerts as they are generated (recommended for Google SecOps).
       * **Snapshots** : sends a weekly snapshot of the current state (use only for periodic reporting).
     * In the **Export target** section, configure the destination: 
       * **Export target** : select **Event hub**.
       * **Subscription** : select the subscription containing the Event Hub namespace.
       * **Event hub namespace** : select `secops-defender-ns` (or the namespace you created earlier).
       * **Event hub name** : select `defender-cloud-alerts` (or the Event Hub you created earlier). Always select an existing Event Hub; leaving this field blank causes the system to create extra Event Hubs and may exhaust your feed quota.
       * **Event hub policy name** : select **RootManageSharedAccessKey** or a custom policy with **Send** permissions.
  8. Click **Save**.

**Note:** Continuous Export starts streaming new alerts immediately. Existing alerts generated before enabling Continuous Export are not exported retroactively. For historical export, see [Microsoft Defender for Cloud documentation](https://learn.microsoft.com/en-us/azure/defender-for-cloud/continuous-export).



### (Optional) Create dedicated consumer group

By default, Event Hub provides a consumer group named `$Default`. For production environments, it's recommended to create a dedicated consumer group for Google SecOps.

  1. Go to the **Event Hub** (not the namespace).
  2. In the left navigation, select **Consumer groups** under **Entities**.
  3. Click **\+ Consumer group**.
  4. Provide the following configuration details: 
     * **Name** : enter a descriptive name (for example, `chronicle`).
  5. Click **Create**.

**Note:** If you create a dedicated consumer group, you must specify it when creating the feed in Google SecOps. Otherwise, use the default `$Default` consumer group.**Caution:** Don't create additional subscribers on the Google SecOps consumer group, and do not retrieve data programmatically through the Azure portal **Data Explorer** tab while it is in use. Either action may cause data loss because Event Hub consumer-group offsets advance as data is read.



### Configure a feed in Google SecOps to ingest Microsoft Defender for Cloud alerts (Method 1)

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft Defender for Cloud Alerts`).
  5. Select **Microsoft Azure Event Hub** as the **Source type**.
  6. Select **Microsoft Defender For Cloud** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Event Hub Name** : enter the Event Hub name (for example, `defender-cloud-alerts`).
     * **Event Hub Consumer Group** : enter the consumer group name. 
       * Use `$Default` for the default consumer group.
       * If you created a dedicated consumer group, enter its name (for example, `chronicle`).
     * **Event Hub Connection String** : enter the Event Hub connection string you captured earlier.

**If using namespace-level connection string:**

       * Ensure you **removed the`EntityPath` parameter**.

**If using event hub-level connection string:** \- Use the connection string as-is (includes `EntityPath`).

     * **Azure Storage Connection String** (optional): legacy field for Event Hub checkpointing storage; leave blank.

     * **Azure Storage Container Name** (optional): legacy field for Event Hub checkpointing storage; leave blank.

     * **Azure SAS Token** (optional): alternative authentication to the Event Hub when your security policy forbids sharing the **Event Hub Connection String** ; leave blank when you provide the connection string above.

     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : the label to be applied to the events from this feed.

**Note:** Google SecOps manages its own checkpointing for Azure Event Hub feeds. Only the **Event Hub Connection String** (or, in its place, **Azure SAS Token**) is required; the **Azure Storage Connection String** and **Azure Storage Container Name** fields are legacy checkpointing fields that do not affect ingestion and should be left blank in standard deployments.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.

**Note:** After creating the feed, it may take 1-2 minutes before alerts start appearing in Google SecOps.



## Method 2: Azure Blob Storage V2

Use this method when your organization already retains Defender for Cloud alerts in a Log Analytics workspace (for compliance or long-term storage) and you want Google SecOps to ingest the same alerts from an Azure Storage Account. Microsoft Defender for Cloud Continuous Export does not write to a Storage Account directly, so this method relies on the standard Log Analytics **Data Export** feature to land alerts in blob storage, from where Google SecOps reads them.

The end-to-end data path is:

  * Microsoft Defender for Cloud > Continuous Export to a **Log Analytics workspace**
  * Log Analytics workspace > **Data Export** rule writes the `SecurityAlert` table to an **Azure Storage Account** (blob container)
  * Google SecOps **Azure Blob Storage V2** feed polls the blob container and ingests new alerts



### Configure Microsoft Defender for Cloud to stream alerts to a Log Analytics workspace

  1. Sign in to the **Azure portal**.
  2. Search for and open **Microsoft Defender for Cloud**.
  3. In the Defender for Cloud resource menu, select **Environment settings**.
  4. Select the **subscription** that you want to configure data export for.
  5. In the resource menu under **Settings** , select **Continuous export**.
  6. Select the **Log Analytics workspace** tab.
  7. Provide the following configuration details: 
     * **Export enabled?** : toggle to the on position.
     * In the **Exported data types** section, select **Security alerts** (and any other data types you want to capture).
     * For each selected data type, configure severity filters as required.
     * In the **Export frequency** section, select **Streaming** for near-real-time export.
     * In the **Export target** section, configure the destination: 
       * **Export target** : select **Log Analytics workspace**.
       * **Subscription** : select the subscription that contains the workspace.
       * **Log Analytics workspace** : select an existing workspace or create a new one.
  8. Click **Save**.

**Note:** Continuous Export only forwards alerts generated after the configuration is enabled. Existing alerts are not exported retroactively.



### Create an Azure Storage Account and blob container

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select the subscription that contains the Log Analytics workspace.  
**Resource group** | Use the same resource group as the workspace (recommended).  
**Storage account name** | Enter a unique name (for example, `secopsdefenderblob`).  
**Region** | Same region as the Log Analytics workspace (required for Data Export).  
**Performance** | Standard.  
**Redundancy** | LRS (Locally redundant storage) or GRS, per your durability policy.  
  4. Click **Review + create** , then click **Create**.

  5. After deployment, go to the Storage Account.

  6. In the left navigation, select **Containers** under **Data storage**.

  7. Click **\+ Container**.

  8. Provide the following configuration details:

     * **Name** : enter a descriptive name (for example, `defender-cloud-alerts`).
     * **Public access level** : **Private (no anonymous access)**.
  9. Click **Create**.

**Note:** Log Analytics Data Export creates one blob per `SecurityAlert` table row batch, organized by date prefix. Do not delete the container or its lifecycle settings while Google SecOps is reading from it.



### Configure a Log Analytics Data Export rule

  1. In the **Azure portal** , open the Log Analytics workspace you selected as the Continuous Export target.
  2. In the left navigation, select **Data Export** under **Settings**.
  3. Click **\+ New export rule**.
  4. Provide the following configuration details: 
     * **Rule name** : enter a descriptive name (for example, `defender-alerts-to-blob`).
     * **Source** : select the `SecurityAlert` table (the table that Defender for Cloud Continuous Export uses for alerts).
     * **Destination type** : select **Storage account**.
     * **Subscription** : select the subscription that contains the Storage Account.
     * **Storage account** : select the Storage Account that you created above.
  5. Click **Create**.

**Note:** Data Export must run in the same region as the workspace and the Storage Account; cross-region rules are rejected by Azure. For the list of `SecurityAlert` columns that are exported, see [Log Analytics Data Export documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/logs-data-export).



### Get Storage Account credentials

Google SecOps authenticates to the Storage Account with a shared access key.

  1. In the Storage Account, select **Access keys** under **Security + networking**.
  2. Click **Show keys**.
  3. Locate **key1** and copy the following values: 
     * **Storage account name** : the name of the Storage Account you created.
     * **Key** : the 512-bit shared access key (base64 encoded).
  4. Save these values securely.

**Note:** Use the shared access key, not a Shared Access Signature (SAS) token, an Azure AD principal, or a full connection string — the AZURE_BLOBSTORE_V2 feed authenticates only with a shared access key.

### Configure a feed in Google SecOps to ingest Microsoft Defender for Cloud alerts (Method 2)

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft Defender for Cloud Alerts - Blob`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Microsoft Defender For Cloud** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : enter the Blob Service endpoint URL with the container path. Include the trailing slash.
           
           https://<STORAGE_ACCOUNT>.blob.core.windows.net/<CONTAINER>/
           

Replace the following:

       * `<STORAGE_ACCOUNT>`: your Azure storage account name (for example, `secopsdefenderblob`).
       * `<CONTAINER>`: the blob container name where Log Analytics Data Export lands `SecurityAlert` rows (for example, `defender-cloud-alerts`).
     * **Source deletion option** : select the deletion option according to your preference:

       * **Never** : never deletes any files after transfer (recommended for first-time setup and audit retention).
       * **Delete transferred files** : deletes files after successful transfer.
       * **Delete transferred files and empty directories** : deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option that removes files, make sure the shared access key grants delete permissions on the container.
     * **Maximum File Age (Days)** : include files modified within the last number of days (default is `180`).

     * **Shared key** : enter the shared access key value you captured from the Storage Account.

     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : the label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.

**Note:** Google SecOps polls the blob container on a managed schedule. Expect first events to appear within 15 to 30 minutes of the feed becoming active, depending on how quickly Log Analytics Data Export flushes new `SecurityAlert` rows to the Storage Account.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`EndTimeLabel` | `about.labels` | Merged  
`ProcessingEndTimeLabel` | `about.labels` | Merged  
`StartTimeLabel` | `about.labels` | Merged  
`TimeGeneratedLabel` | `about.labels` | Merged  
`extendedLinkCategoryLabel` | `about.labels` | Merged  
`extendedLinkLabel` | `about.labels` | Merged  
`extendedLinkTypeLabel` | `about.labels` | Merged  
`extendedlinkHrefLabel` | `about.labels` | Merged  
`EndTimeLabel` | `about.resource.attribute.labels` | Merged  
`ProcessingEndTimeLabel` | `about.resource.attribute.labels` | Merged  
`StartTimeLabel` | `about.resource.attribute.labels` | Merged  
`TimeGeneratedLabel` | `about.resource.attribute.labels` | Merged  
`extendedLinkCategoryLabel` | `about.resource.attribute.labels` | Merged  
`extendedLinkLabel` | `about.resource.attribute.labels` | Merged  
`extendedLinkTypeLabel` | `about.resource.attribute.labels` | Merged  
`extendedlinkHrefLabel` | `about.resource.attribute.labels` | Merged  
`EndTimeLabel1` | `additional.fields` | Merged  
`IoTHub_ResourceId_label` | `additional.fields` | Merged  
`IoTHub_Type_label` | `additional.fields` | Merged  
`Protocols_label` | `additional.fields` | Merged  
`RemediationSteps_label` | `additional.fields` | Merged  
`Scopes_label` | `additional.fields` | Merged  
`StartTimeLabel1` | `additional.fields` | Merged  
`TimeGeneratedLabel1` | `additional.fields` | Merged  
`account_type` | `additional.fields` | Merged  
`alert_generation_status_label` | `additional.fields` | Merged  
`bacnet_service_label` | `additional.fields` | Merged  
`billed_size_label` | `additional.fields` | Merged  
`category_label` | `additional.fields` | Merged  
`event_data_info` | `additional.fields` | Merged  
`extended_properties_device_id_label` | `additional.fields` | Merged  
`ip_category` | `additional.fields` | Merged  
`is_billable_label` | `additional.fields` | Merged  
`is_learnable_label` | `additional.fields` | Merged  
`item_id_label` | `additional.fields` | Merged  
`key` | `additional.fields` | Mapped: `IpAddress` → `nic_sub_field`  
`key_value` | `additional.fields` | Merged  
`mode_label` | `additional.fields` | Merged  
`nic_field` | `additional.fields` | Merged  
`nic_sub_field` | `additional.fields` | Merged  
`owner_label` | `additional.fields` | Merged  
`processed_by_sentinel_label` | `additional.fields` | Merged  
`protocol_label` | `additional.fields` | Merged  
`provider_name_label` | `additional.fields` | Merged  
`remediation_steps_label` | `additional.fields` | Merged  
`role_label` | `additional.fields` | Merged  
`service_object_type` | `additional.fields` | Merged  
`techniques_label` | `additional.fields` | Merged  
`tenantIdLabel` | `additional.fields` | Merged  
`time_received_label` | `additional.fields` | Merged  
`type_ext_label` | `additional.fields` | Merged  
`type_label` | `additional.fields` | Merged  
`value_label` | `additional.fields` | Merged  
`authentication_type` | `extensions.auth.auth_details` | Directly mapped  
`SensorId` | `intermediary.hostname` | Directly mapped  
`record.TimeGenerated` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`record.properties.Timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`record.time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`record.operationName` | `metadata.product_event_type` | Directly mapped  
`raw_event_id` | `metadata.product_log_id` | Directly mapped  
`record.SystemAlertId` | `metadata.product_log_id` | Directly mapped  
`record.alertId` | `metadata.product_log_id` | Directly mapped  
`record.properties.extendedProperties.alert_Id` | `metadata.product_log_id` | Directly mapped  
`product_name` | `metadata.product_name` | Directly mapped  
`record.properties.productName` | `metadata.product_name` | Directly mapped  
`vendor_name` | `metadata.vendor_name` | Directly mapped  
`record.properties.RawEventData.AffectedItems.0.InternetMessageId` | `network.email.mail_id` | Directly mapped  
`record.properties.RawEventData.Folders.0.FolderItems.0.InternetMessageId` | `network.email.mail_id` | Directly mapped  
`record.properties.RawEventData.Item.InternetMessageId` | `network.email.mail_id` | Directly mapped  
`email_subject` | `network.email.subject` | Merged  
`operation` | `network.email.subject` | Mapped (lookup table)  
`record.properties.UserAgent` | `network.http.user_agent` | Directly mapped  
`user_agent` | `network.http.user_agent` | Directly mapped  
`network_session_id` | `network.session_id` | Directly mapped  
`record.ExtendedProperties.accountSessionId` | `network.session_id` | Directly mapped  
`record.properties.RawEventData.ClientRequestId` | `network.session_id` | Directly mapped  
`record.clientApplication` | `principal.application` | Directly mapped  
`record.properties.extendedProperties.clientApplication` | `principal.application` | Directly mapped  
`SourceDevice` | `principal.asset.hostname` | Directly mapped  
`client_hostname` | `principal.asset.hostname` | Directly mapped  
`compromised_hostname` | `principal.asset.hostname` | Directly mapped  
`SourceDeviceAddress` | `principal.asset.ip` | Mapped: IPv4 regex  
`clientIpAddress` | `principal.asset.ip` | Merged  
`SourceComputerId` | `principal.asset.product_object_id` | Directly mapped  
`SourceDevice` | `principal.hostname` | Directly mapped  
`client_hostname` | `principal.hostname` | Directly mapped  
`compromised_hostname` | `principal.hostname` | Directly mapped  
`SourceDeviceAddress` | `principal.ip` | Mapped: IPv4 regex  
`clientIpAddress` | `principal.ip` | Merged  
`alertLabel` | `principal.labels` | Merged  
`cityLabel` | `principal.location.city` | Directly mapped  
`record.properties.City` | `principal.location.city` | Directly mapped  
`countryLabel` | `principal.location.country_or_region` | Directly mapped  
`record.clientIpLocation` | `principal.location.country_or_region` | Directly mapped  
`record.clientLocation` | `principal.location.country_or_region` | Directly mapped  
`record.properties.clientLocation` | `principal.location.country_or_region` | Directly mapped  
`record.properties.extendedProperties.clientLocation` | `principal.location.country_or_region` | Directly mapped  
`isp` | `principal.location.name` | Directly mapped  
`entity.location.latitude` | `principal.location.region_coordinates.latitude` | Directly mapped  
`entity.location.longitude` | `principal.location.region_coordinates.longitude` | Directly mapped  
`os_platform` | `principal.platform` | Mapped: `iOS` → `MAC`  
`record.ExtendedProperties.suspiciousCommandLine` | `principal.process.command_line` | Directly mapped  
`record.ExtendedProperties.suspiciousProcess` | `principal.process.file.full_path` | Directly mapped  
`record.properties.RawEventData.ClientProcessName` | `principal.process.file.full_path` | Directly mapped  
`record.ExtendedProperties.suspiciousProcessId` | `principal.process.pid` | Directly mapped  
`account_id` | `principal.resource.attribute.labels` | Merged  
`account_object_id` | `principal.resource.attribute.labels` | Merged  
`alertLabel` | `principal.resource.attribute.labels` | Merged  
`alertLabel1` | `principal.resource.attribute.labels` | Merged  
`app_instance_id` | `principal.resource.attribute.labels` | Merged  
`compromisedEntityLabel` | `principal.resource.attribute.labels` | Merged  
`compromisedEntityLabel1` | `principal.resource.attribute.labels` | Merged  
`correlationKeyLabel` | `principal.resource.attribute.labels` | Merged  
`effectiveSubscriptionIdLabel` | `principal.resource.attribute.labels` | Merged  
`object_id` | `principal.resource.attribute.labels` | Merged  
`object_name` | `principal.resource.attribute.labels` | Merged  
`object_type` | `principal.resource.attribute.labels` | Merged  
`potential_causes` | `principal.resource.attribute.labels` | Merged  
`productComponentNameLabel` | `principal.resource.attribute.labels` | Merged  
`sql_instance_name_label` | `principal.resource.attribute.labels` | Merged  
`sql_server_name_label` | `principal.resource.attribute.labels` | Merged  
`supporting_evidence_label` | `principal.resource.attribute.labels` | Merged  
`system_alert_id_label` | `principal.resource.attribute.labels` | Merged  
`zone_interface_label` | `principal.resource.attribute.labels` | Merged  
`record.properties.extendedProperties.resourceType` | `principal.resource.name` | Directly mapped  
`resourceType` | `principal.resource.name` | Directly mapped  
`record.ResourceId` | `principal.resource.product_object_id` | Directly mapped  
`mailbox_owner_upn` | `principal.user.email_addresses` | Merged  
`principal_user_display_name` | `principal.user.user_display_name` | Directly mapped  
`record.ExtendedProperties.userName` | `principal.user.user_display_name` | Directly mapped  
`client_user` | `principal.user.userid` | Directly mapped  
`principal_userid` | `principal.user.userid` | Directly mapped  
`record.properties.RawEventData.LogonUserSid` | `principal.user.windows_sid` | Directly mapped  
`action` | `security_result.action` | Merged  
`operation` | `security_result.action` | Mapped (lookup table)  
`tacticsLabel` | `security_result.attack_details.tactics` | Merged  
`category_details_label` | `security_result.category_details` | Merged  
`threat_category` | `security_result.category_details` | Merged  
`record.Description` | `security_result.description` | Directly mapped  
`record.properties.description` | `security_result.description` | Directly mapped  
`KindLabel` | `security_result.detection_fields` | Merged  
`action_type` | `security_result.detection_fields` | Merged  
`application_id` | `security_result.detection_fields` | Merged  
`device_type` | `security_result.detection_fields` | Merged  
`field` | `security_result.detection_fields` | Merged  
`incidentdetectionfields` | `security_result.detection_fields` | Merged  
`incidentdetectionfields1` | `security_result.detection_fields` | Merged  
`intent_label` | `security_result.detection_fields` | Merged  
`is_admin_operation_label` | `security_result.detection_fields` | Merged  
`is_impersonated_label` | `security_result.detection_fields` | Merged  
`is_new_label` | `security_result.detection_fields` | Merged  
`operation` | `security_result.detection_fields` | Mapped: `MailItemsAccessed` → `field`  
`product_component_name_ext_label` | `security_result.detection_fields` | Merged  
`sourcesystemdetectionfields` | `security_result.detection_fields` | Merged  
`statusdetectionfields` | `security_result.detection_fields` | Merged  
`statusdetectionfields1` | `security_result.detection_fields` | Merged  
`trojan_script_malgent_msr_label` | `security_result.detection_fields` | Merged  
`vendor_original_id_label` | `security_result.detection_fields` | Merged  
`violation_count_label` | `security_result.detection_fields` | Merged  
`report_id` | `security_result.rule_id` | Directly mapped  
`alertDisplayName` | `security_result.rule_name` | Directly mapped  
`record.AlertName` | `security_result.rule_name` | Directly mapped  
`alert_severity` | `security_result.severity` | Directly mapped  
`severity` | `security_result.severity` | Directly mapped  
`alert_severity` | `security_result.severity_details` | Directly mapped  
`record.properties.severity` | `security_result.severity_details` | Directly mapped  
`record.DisplayName` | `security_result.summary` | Directly mapped  
`summary` | `security_result.summary` | Directly mapped  
`record.AlertType` | `security_result.threat_name` | Directly mapped  
`record.properties.alertType` | `security_result.threat_name` | Directly mapped  
`AlertManagementUri` | `security_result.url_back_to_product` | Directly mapped  
`record.properties.RawEventData.Folder.Path` | `src.resource.name` | Directly mapped  
`record.properties.RawEventData.Folder.Id` | `src.resource.product_object_id` | Directly mapped  
`application` | `target.application` | Directly mapped  
`DestinationDevice` | `target.asset.hostname` | Directly mapped  
`record.ExtendedProperties.compromisedHost` | `target.asset.hostname` | Directly mapped  
`DestinationDeviceAddress` | `target.asset.ip` | Mapped: IPv4 regex  
`CompromisedEntityId` | `target.asset.product_object_id` | Directly mapped  
`file_name` | `target.file.names` | Merged  
`operation` | `target.file.names` | Mapped (lookup table)  
`operation` | `target.file.size` | Mapped (lookup table)  
`record.properties.RawEventData.Item.SizeInBytes` | `target.file.size` | Directly mapped  
`DestinationDevice` | `target.hostname` | Directly mapped  
`originating_server` | `target.hostname` | Directly mapped  
`record.ExtendedProperties.compromisedHost` | `target.hostname` | Directly mapped  
`DestinationDeviceAddress` | `target.ip` | Mapped: IPv4 regex  
`target_process_command_line` | `target.process.command_line` | Directly mapped  
`target_process_file` | `target.process.file.full_path` | Directly mapped  
`target_process_id` | `target.process.pid` | Directly mapped  
`workspaceLabel` | `target.resource.attribute.labels` | Merged  
`workspaceResourceGroupLabel` | `target.resource.attribute.labels` | Merged  
`AzureResourceId` | `target.resource.id` | Directly mapped  
`record.properties.RawEventData.DestFolder.Path` | `target.resource.name` | Directly mapped  
`record.properties.RawEventData.Item.ParentFolder.Path` | `target.resource.name` | Directly mapped  
`record._Internal_WorkspaceResourceId` | `target.resource.product_object_id` | Directly mapped  
`record.properties.RawEventData.DestFolder.Id` | `target.resource.product_object_id` | Directly mapped  
`record.properties.RawEventData.Item.Id` | `target.resource.product_object_id` | Directly mapped  
`operation` | `target.user.email_addresses` | Mapped (lookup table)  
`target_user` | `target.user.email_addresses` | Mapped: email regex  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_name` | Constant: `MICROSOFT_DEFENDER_CLOUD_ALERTS`  
N/A | `metadata.vendor_name` | Constant: `MICROSOFT_DEFENDER_CLOUD_ALERTS`  
N/A | `principal.platform` | Constant: `MAC`  
`record.ExtendedProperties.clientIpAddress` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`record.ExtendedProperties.clientPrincipalName` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`record.ExtendedProperties.clientApplication` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`record.ExtendedProperties.Potential causes` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`record.ExtendedProperties.investigationSteps` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`record.ExtendedProperties.alertId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Entity.FriendlyName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Entity.SourceAddress.Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Entity.EntityIds` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Entity.Metadata.IsGraphCenter` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.ExtendedProperties` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Entities.FriendlyName` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`Entities.FileHashes.FriendlyName` | `event.idm.read_only_udm.target.file.sha1` | Mapped from changelog  
`Entities.FileHashes.FriendlyName` | `event.idm.read_only_udm.target.file.md5` | Mapped from changelog  
`Entities.FileHashes.FriendlyName` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`Entities.AzureResourceId` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`Entities.ResourceType` | `event.idm.read_only_udm.target.resource.resource_subtype` | Mapped from changelog  
`Entities.ResourceName` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`Entities.SourceAddress.Location.CountryName` | `event.idm.read_only_udm.location.country_or_region` | Mapped from changelog  
`Entities.SourceAddress.Location.City` | `event.idm.read_only_udm.location.city` | Mapped from changelog  
`Entities.SourceAddress.Location.State` | `event.idm.read_only_udm.location.state` | Mapped from changelog  
`Entities.SourceAddress.Location.Longitude` | `event.idm.read_only_udm.location.region_coordinates.longitude` | Mapped from changelog  
`Entities.SourceAddress.Location.Latitude` | `event.idm.read_only_udm.location.region_coordinates.latitude` | Mapped from changelog  
`Entities.SourceAddress.Location.Asn` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Entities.SourceAddress.Location.Carrier` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Entities.SourceAddress.Location.Organization` | `event.idm.read_only_udm.principal.network.organization_name` | Mapped from changelog  
`RecommendationLink` | `event.idm.read_only_udm.metadata.url_back_to_product` | Mapped from changelog  
`Properties.status.statusChangeDate` | `event.idm.read_only_udm.security_result.last_updated_time` | Mapped from changelog  
`StatusChangeDate` | `event.idm.read_only_udm.target.resource.attribute.last_update_time` | Mapped from changelog  
`Type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`_TimeReceived` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`Properties.additionalData.scanId` | `event.idm.read_only_udm.observer.resource.product_object_id` | Mapped from changelog  
`Properties.additionalData.parentResource` | `event.idm.read_only_udm.target.resource_ancestors.product_object_id` | Mapped from changelog  
`Properties.additionalData.databasePlatform` | `event.idm.read_only_udm.target.resource.resource_subtype` | Mapped from changelog  
`Properties.metadata_data.techniques.0` | `event.idm.read_only_udm.security_result.attack_details.techniques.name` | Mapped from changelog  
`Properties.links.azurePortal` | `event.idm.read_only_udm.security_result.url_back_to_product` | Mapped from changelog  
`Properties.displayName` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`Properties.additionalData.ruleId` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`Properties.additionalData.scanner` | `event.idm.read_only_udm.observer.resource.name` | Mapped from changelog  
`Properties.resourceDetails.id` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`Properties.resourceDetails.resourceName` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`Properties.resourceDetails.resourceProvider` | `event.idm.read_only_udm.target.resource_ancestors.name` | Mapped from changelog  
`FirstEvaluationDate` | `event.idm.read_only_udm.security_result.first_discovered_time` | Mapped from changelog  
`DiscoveredTimeUTC` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`RecommendationDisplayName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Recommendation DisplayName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RecommendationId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Recommendation Id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RecommendationName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Recommendation Name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RecommendationSeverity` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Recommendation Severity` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RecommendationState` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Recommendation State` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RemediationDescription` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Remediation_Description` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SourceSystem` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Source System` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`_ItemId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Item Id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.displayName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Metadata Display Name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.assessmentType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Assessment Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.policyDefinitionId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Policy Definition Id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.description` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Metadata Description` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.remediationDescription` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Remediation Description` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.preview` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Preview` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.severity` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Metadata Severity` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.userImpact` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`User Impact` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.implementationEffort` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Implementation Effort` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.publishDates.public` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Public Publish Date` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.cloudProviders` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Cloud Providers %{index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.managementProvider` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Management Provider` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.securityIssue` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Security Issue` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.recommendationCategory` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Recommendation Category` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`_IsBillable` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Is Billable` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`_BilledSize` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Billed Size` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`IsSnapshot` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Is Snapshot` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ResourceTenantId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Resource Tenant ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.additionalData.hasBaseline` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Has Baseline` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.additionalData.query` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Query` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.additionalData.remediationDescription` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Additional Remediation Description` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.additionalData.remediationQuery` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Remediation Query` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.additionalData.impact` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Impact` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`benchmarks.json_array2.item.reference` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Benchmark Reference` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.status.firstEvaluationDate` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`First Evaluation Date` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.resourceDetails.nativeResourceId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Native Resource ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`benchmarks.json_array2.item.benchmark` | `Benchmark` key to `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.securityCategories` | `Security Categories` key to `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.metadata_data.categories` | `Metadata Categories` key to `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties.additionalData.scanTime` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`scanTime` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`Properties.status.code` | `event.idm.read_only_udm.security_result.outcomes` | Mapped from changelog  
`Status Code` | `event.idm.read_only_udm.security_result.outcomes` | Mapped from changelog  
`Properties.status.cause` | `event.idm.read_only_udm.security_result.outcomes` | Mapped from changelog  
`status_cause` | `event.idm.read_only_udm.security_result.outcomes` | Mapped from changelog  
`Properties.resourceDetails.resourceType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Resource Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.TimeGenerated` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`record.ExtendedProperties.suspiciousProcessId` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`record.ExtendedProperties.suspiciousProcess` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`record.ExtendedProperties.suspiciousCommandLine` | `event.idm.read_only_udm.principal.process.command_line` | Mapped from changelog  
`record.ExtendedProperties.userName` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`record.ExtendedProperties.compromisedHost` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`record.ExtendedProperties.accountSessionId` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`SourceDeviceAddress` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`SourceDeviceAddress` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`DestinationDeviceAddress` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`DestinationDeviceAddress` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`SourceDevice` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`SourceDevice` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`DestinationDevice` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`DestinationDevice` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`SourceComputerId` | `event.idm.read_only_udm.principal.asset.product_object_id` | Mapped from changelog  
`CompromisedEntityId` | `event.idm.read_only_udm.target.asset.product_object_id` | Mapped from changelog  
`SensorId` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`Category` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`AlertManagementUri` | `event.idm.read_only_udm.security_result.url_back_to_product` | Mapped from changelog  
`record.VendorOriginalId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`VendorOriginalId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ProductComponentName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ViolationCount` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`isNew` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`record.ProviderName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ProviderName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`DeviceId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ExtendedProperties_DeviceId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`_TimeReceived` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`BACnet Service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`bacnet_service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Protocol` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`isLearnable` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RemediationSteps` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Techniques` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Alert generation status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ProcessedBySentinel` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.Entities` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Entity: %{key}_%{index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`IoTHub.ResourceId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`IoTHub_ResourceId_%{index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`IoTHub.Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`IoTHub_Type_%{index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Owners` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Owners_%{index}_%{owner_index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Nics` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Nics_%{index}_%{nic_index}_IpAddress_%{sub_key}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Nics_%{index}_%{nic_index}_%{key}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Protocols` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Protocols_%{index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.properties.RawEventData.ClientProcessName` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`record.properties.RawEventData.ClientRequestId` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`record.properties.RawEventData.LogonUserSid` | `event.idm.read_only_udm.principal.user.windows_sid` | Mapped from changelog  
`record.properties.RawEventData.MailboxOwnerUPN` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`record.properties.ISP` | `event.idm.read_only_udm.principal.location.name` | Mapped from changelog  
`record.properties.RawEventData.OriginatingServer` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`record.properties.Application` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`record.properties.ReportId` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`record.properties.IsImpersonated` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`record.properties.IsAdminOperation` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`zone_interface` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`record.properties.extendedProperties.potential causes` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`record.properties.extendedProperties.productComponentName` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`record.properties.extendedProperties.effectiveSubscriptionId` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`record.properties.extendedProperties.sql server name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`record.properties.extendedProperties.sql instance name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`record.properties.supportingEvidence` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`record.properties.systemAlertId` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`record.properties.RawEventData.UserId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`record.properties.RawEventData.Id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-cloud-alerts-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
