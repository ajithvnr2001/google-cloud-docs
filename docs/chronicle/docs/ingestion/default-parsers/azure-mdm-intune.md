---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-mdm-intune/
title: Collect Azure MDM Intune logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:35.092807+00:00
---

# Collect Azure MDM Intune logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-mdm-intune/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Azure MDM Intune logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Microsoft Intune logs to Google Security Operations. You can configure ingestion using three methods: Azure Event Hub (recommended), the Third Party API, or Microsoft Azure Blob Storage V2.

Microsoft Intune is a cloud-based endpoint management solution that manages user access to organizational resources and simplifies app and device management across devices including mobile devices, desktop computers, and virtual endpoints.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the **Microsoft Azure** portal
  * A user with the **Intune Administrator** or **Global Administrator** Microsoft Entra role for the Intune tenant
  * An active Intune license for the tenant



## Method 1: Azure Event Hub (recommended)

This method streams Intune logs through Azure Event Hub with Capture enabled, which writes the data to Azure Blob Storage. Google SecOps then ingests the logs from Blob Storage using the Azure Blob Storage V2 feed type.

**Note:** This method provides lower latency log delivery compared to the Third Party API method.

### Configure Azure Storage Account

#### Create Storage Account

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Storage account name** | Enter a unique name (for example, `secopsintuneeh`)  
**Region** | Select the region closest to your Event Hub namespace  
**Performance** | Standard (recommended)  
**Redundancy** | LRS (Locally redundant storage) or GRS (Geo-redundant storage)  
  4. Click **Review + create**.

  5. Review the overview and click **Create**.

  6. Wait for the deployment to complete.




#### Get Storage Account credentials

  1. Go to the **Storage Account** you created.
  2. In the left navigation, select **Access keys** under **Security + networking**.
  3. Click **Show keys**.
  4. Copy and save the following: 
     * **Storage account name**
     * **Key 1** or **Key 2** : The shared access key.



### Create and Event Hub namespace and an Event Hub

#### Create Event Hub namespace

  1. In the **Azure portal** , search for **Event Hubs**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select the same resource group as your storage account  
**Namespace name** | Enter a unique name (for example, `secops-intune-logs`)  
**Location** | Select the same region as your storage account  
**Pricing tier** | Standard (required for Event Hub Capture)  
**Note:** The **Standard** or **Premium** pricing tier is required for Event Hub Capture. The Basic tier does not support Capture.
  4. Click **Review + create** , then click **Create**.

  5. Wait for the deployment to complete.




#### Create an Event Hub

  1. Go to the Event Hub namespace you created.
  2. Click **\+ Event Hub** at the top.
  3. Provide the following configuration details: 
     * **Name** : Enter a name (for example, `intune-logs`).
     * **Partition count** : 2 (default, increase for higher throughput).
     * **Cleanup policy** : Delete.
     * **Retention time (hrs)** : 24 (minimum, increase if needed for resilience).
  4. Click **Review + create** , then click **Create**.



### Enable an Event Hub Capture

  1. Go to the Event Hub you created (inside the namespace).
  2. In the left navigation, select **Capture**.
  3. Set **Capture** to **On**.
  4. Provide the following configuration details:

Setting | Value  
---|---  
**Time window (minutes)** | 5 (or lower for near-real-time)  
**Size window (MB)** | 300  
**Capture Provider** | Azure Blob Storage  
**Azure Subscription** | Select your subscription  
**Storage Account** | Select the storage account you created  
**Blob Container** | Create or select a container (for example, `intune-capture`)  
**Note:** If no container exists, select **Create container** and enter a name.
  5. Click **Save**.

**Note:** Event Hub Capture writes files in Apache Avro format to the blob container. Google SecOps can parse Avro-formatted Intune logs.



### Configure Intune diagnostic settings

  1. Sign in to the **Microsoft Intune admin center**.
  2. Select **Reports > Diagnostic settings**.
  3. Click **Add diagnostic setting**.
  4. Provide the following configuration details: 
     * **Diagnostic setting name** : Enter a descriptive name (for example, `intune-to-eventhub`).
     * In the **Logs** section, select the following categories: 
       * **OperationalLogs**
       * **DeviceComplianceOrg**
       * **Devices**
     * In the **Destination details** section, select **Stream to an event hub**.
     * **Subscription** : Select the subscription containing your Event Hub namespace.
     * **Event hub namespace** : Select the namespace you created (for example, `secops-intune-logs`).
     * **Event hub name** : Select the Event Hub you created (for example, `intune-logs`).
     * **Event hub policy name** : Select **RootManageSharedAccessKey**.
  5. Click **Save**.

**Note:** Intune Operational Logs are sent immediately to Azure Monitor services. Device Compliance Organizational Logs and IntuneDevices report data is sent once every 24 hours.



### Configure a feed in Google SecOps to ingest Intune logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft Intune - Event Hub`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Microsoft Intune** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the capture container path:
           
           https://<storage-account>.blob.core.windows.net/intune-capture/
           

     * Replace `<storage-account>` with your Azure storage account name.

**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers.
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Shared key** : Enter the shared access key value from the Storage Account.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




### Configure Azure Storage firewall (if enabled)

If your Azure Storage Account uses a firewall, you must add Google SecOps IP ranges.

  1. In the **Azure portal** , go to your **Storage Account**.
  2. Select **Networking** under **Security + networking**.
  3. Under **Firewalls and virtual networks** , select **Enabled from selected virtual networks and IP addresses**.
  4. In the **Firewall** section, under **Address range** , click **\+ Add IP range**.
  5. Add each Google SecOps IP range in CIDR notation. 
     * See [IP Allowlisting documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip-allow-lists).
     * Or retrieve them programmatically using the [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api).
  6. Click **Save**.



## Method 2: Third Party API

This method uses the Microsoft Graph API to retrieve Intune audit and operational logs directly from your Microsoft tenant.

### Configure Microsoft Entra app registration

#### Create app registration

  1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) or [Azure portal](https://portal.azure.com/).
  2. Go to **Identity > Applications > App registrations**.
  3. Click **New registration**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Intune Integration`).
     * **Supported account types** : Select **Accounts in this organizational directory only (Single tenant)**.
     * **Redirect URI** : Leave blank (not required for service principal authentication).
  5. Click **Register**.
  6. After registration, copy and save the following values from the **Overview** page: 
     * **Application (client) ID**
     * **Directory (tenant) ID**



#### Configure API permissions

  1. In the app registration, go to **API permissions**.
  2. Click **Add a permission**.
  3. Select **Microsoft Graph > Application permissions**.
  4. Search for and select the following permissions: 
     * **DeviceManagementApps.Read.All**
     * **DeviceManagementConfiguration.Read.All**
     * **DeviceManagementManagedDevices.Read.All**
     * **DeviceManagementServiceConfig.Read.All**
     * **DeviceManagementRBAC.Read.All**
  5. Click **Add permissions**.
  6. Click **Grant admin consent for [Your Organization]**.
  7. Verify that the **Status** column shows **Granted for [Your Organization]** for all permissions.

**Note:** If the **Grant admin consent** button is disabled, ensure you have **Global Administrator** or **Privileged Role Administrator** role. Cloud Application Administrator role cannot grant consent for Microsoft Graph application permissions.



#### Required API permissions

Permission | Type | Purpose  
---|---|---  
**DeviceManagementApps.Read.All** | Application | Read app management data and audit events  
**DeviceManagementConfiguration.Read.All** | Application | Read device configuration and compliance policies  
**DeviceManagementManagedDevices.Read.All** | Application | Read managed device information  
**DeviceManagementServiceConfig.Read.All** | Application | Read Intune service configuration  
**DeviceManagementRBAC.Read.All** | Application | Read role-based access control settings  
**Note:** Using least-privilege access. Only read permissions are required; write permissions are not needed for log ingestion.

#### Create client secret

  1. In the app registration, go to **Certificates & secrets**.
  2. Click **New client secret**.
  3. Provide the following configuration details:

     * **Description** : Enter a descriptive name (for example, `Google SecOps Feed`).
     * **Expires** : Select an expiration period.
**Note:** Microsoft recommends setting an expiration value of less than 12 months. The maximum allowed is 24 months.
  4. Click **Add**.

  5. Copy the client secret **Value** immediately.

**Important** : The secret value is displayed only once and cannot be retrieved after leaving this page. If you lose the value, you must create a new client secret.




### Configure a feed in Google SecOps to ingest Microsoft Intune logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft Intune Logs`).
  5. Select **Third Party API** as the **Source type**.
  6. Select **Microsoft Intune** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **OAuth Client ID** : Enter the **Application (client) ID** from the app registration (for example, `1234abcd-1234-abcd-1234-abcd1234abcd`).
     * **OAuth Client Secret** : Enter the **client secret value** you copied earlier.
     * **Tenant ID** : Enter the **Directory (tenant) ID** from the app registration in UUID format (for example, `0fc279f9-fe30-41be-97d3-abe1d7681418`).
     * **API Full Path** : Enter the Microsoft Graph REST API endpoint URL. Default value:
           
           graph.microsoft.com/beta/deviceManagement/auditEvents
           

**Note:** Do not include the `https://` prefix. The feed adds the protocol automatically.
     * **API Authentication Endpoint** : Enter the Microsoft Active Directory authentication endpoint. Default value:
           
           login.microsoftonline.com
           

**Note:** Do not include the `https://` prefix or the `/oauth2/v2.0/token` path. The feed constructs the full authentication URL automatically using your Tenant ID.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




After setup, the feed begins to retrieve Intune audit and operational logs from the Microsoft Graph API.

**Note:** After creating the feed, it may take 5-10 minutes before logs start appearing in Google SecOps.

### Regional endpoints

For Microsoft Intune deployments in sovereign clouds, use the appropriate regional endpoints:

Cloud Environment | API Full Path | API Authentication Endpoint  
---|---|---  
**Global** | `graph.microsoft.com/beta/deviceManagement/auditEvents` | `login.microsoftonline.com`  
**US Government L4** | `graph.microsoft.us/beta/deviceManagement/auditEvents` | `login.microsoftonline.us`  
**US Government L5 (DOD)** | `dod-graph.microsoft.us/beta/deviceManagement/auditEvents` | `login.microsoftonline.us`  
**China (21Vianet)** | `microsoftgraph.chinacloudapi.cn/beta/deviceManagement/auditEvents` | `login.chinacloudapi.cn`  
  
## Method 3: Microsoft Azure Blob Storage V2

This method collects Microsoft Intune logs by exporting diagnostic data to an Azure Storage Account and configuring a Google SecOps feed to ingest from Azure Blob Storage.

### Configure Azure Storage Account

#### Create Storage Account

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Storage account name** | Enter a unique name (for example, `intunelogs`)  
**Region** | Select the region (for example, `East US`)  
**Performance** | Standard (recommended)  
**Redundancy** | GRS (Geo-redundant storage) or LRS (Locally redundant storage)  
  4. Click **Review + create**.

  5. Review the overview and click **Create**.

  6. Wait for the deployment to complete.




#### Get Storage Account credentials

  1. Go to the **Storage Account** you created.
  2. In the left navigation, select **Access keys** under **Security + networking**.
  3. Click **Show keys**.
  4. Copy and save the following: 
     * **Storage account name** : The name you provided during creation.
     * **Key 1** or **Key 2** : The shared access key.



#### Get Blob Service endpoint

  1. In the same Storage Account, select **Endpoints** from the left navigation.
  2. Copy and save the **Blob service** endpoint URL. 
     * Example: `https://intunelogs.blob.core.windows.net/`



### Configure Microsoft Intune Diagnostic Settings

  1. Sign in to the **Microsoft Intune admin center**.
  2. Select **Reports > Diagnostic settings**.
  3. Click **Add diagnostic setting**.
  4. Provide the following configuration details: 
     * **Diagnostic setting name** : Enter a descriptive name (for example, `export-to-secops`).
     * In the **Logs** section, select the following categories: 
       * **OperationalLogs**
       * **DeviceComplianceOrg**
       * **Devices**
     * In the **Destination details** section, select the **Archive to a storage account** checkbox.
     * **Subscription** : Select the subscription containing your storage account.
     * **Storage account** : Select the storage account you created earlier.
  5. Click **Save**.

**Note:** Intune Operational Logs are sent immediately to Azure Monitor services. Device Compliance Organizational Logs and IntuneDevices report data is sent once every 24 hours.**Note:** Azure diagnostic settings create containers in the storage account based on the log category. The container names follow the pattern `insights-logs-{categoryname}`.



### Configure a feed in Google SecOps to ingest Microsoft Intune logs from Blob Storage

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft Intune Blob Storage`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Microsoft Intune** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the container path. Create separate feeds for each log category:

     * For Operational Logs:
           
           https://<storage-account>.blob.core.windows.net/insights-logs-operationallogs/
           

     * For Device Compliance Organizational Logs:
           
           https://<storage-account>.blob.core.windows.net/insights-logs-devicecomplianceorg/
           

     * For Devices:
           
           https://<storage-account>.blob.core.windows.net/insights-logs-devices/
           

Replace `<storage-account>` with your Azure storage account name.

**Note:** Include the trailing slash (/) at the end of the URI. Verify the actual container names in your Azure Storage account.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers
       * **Delete transferred files** : Deletes files after successful transfer
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Shared key** : Enter the shared access key value from the Storage Account.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.

  11. Repeat steps 1-10 to create additional feeds for each Intune log category container.




### Configure Azure Storage firewall (if enabled)

If your Azure Storage Account uses a firewall, you must add Google SecOps IP ranges.

  1. In the **Azure portal** , go to your **Storage Account**.
  2. Select **Networking** under **Security + networking**.
  3. Under **Firewalls and virtual networks** , select **Enabled from selected virtual networks and IP addresses**.
  4. In the **Firewall** section, under **Address range** , click **\+ Add IP range**.
  5. Add each Google SecOps IP range in CIDR notation. 
     * See [IP Allowlisting documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip-allow-lists)
     * Or retrieve them programmatically using the [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api)
  6. Click **Save**.

**Note:** This feed source uses the Storage Transfer Service (STS) to transfer data from Azure storage to Google SecOps. Before using this feed source, you must configure the Azure Storage firewall to allow access from the STS IP ranges.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`AADDeviceId_label` | `additional.fields` | Merged  
`AADTenantId_label` | `additional.fields` | Merged  
`ComplianceState_label` | `additional.fields` | Merged  
`DeviceHealthThreatLevel_loc_label` | `additional.fields` | Merged  
`EnrollmentType_label` | `additional.fields` | Merged  
`FailureCategory_label` | `additional.fields` | Merged  
`FailureReason_label` | `additional.fields` | Merged  
`InGracePeriodUntil_label` | `additional.fields` | Merged  
`IntuneAccountId_label` | `additional.fields` | Merged  
`IntuneDeviceId_label` | `additional.fields` | Merged  
`IntuneUserId_label` | `additional.fields` | Merged  
`LastContact_label` | `additional.fields` | Merged  
`ManagementAgents_label` | `additional.fields` | Merged  
`ManagementAgents_loc_label` | `additional.fields` | Merged  
`MessageId_label` | `additional.fields` | Merged  
`Os_label` | `additional.fields` | Merged  
`RetireAfterDatetime_label` | `additional.fields` | Merged  
`ScaleUnit_label` | `additional.fields` | Merged  
`activityOperationType_label` | `additional.fields` | Merged  
`activityResult_label` | `additional.fields` | Merged  
`category_label` | `additional.fields` | Merged  
`componentName_label` | `additional.fields` | Merged  
`correlationId_label` | `additional.fields` | Merged  
`current_perm` | `additional.fields` | Merged  
`displayName_label` | `additional.fields` | Merged  
`id_label` | `additional.fields` | Merged  
`old_label` | `additional.fields` | Merged  
`resultType_label` | `additional.fields` | Merged  
`start_time_utc` | `additional.fields` | Merged  
`temp_label` | `additional.fields` | Merged  
`tenantId_label` | `additional.fields` | Merged  
`properties.Description` | `metadata.description` | Directly mapped  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`when` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`event_type` | `metadata.event_type` | Renamed/mapped  
`activityType` | `metadata.product_event_type` | Directly mapped  
`operationName` | `metadata.product_event_type` | Directly mapped  
`properties.BatchId` | `metadata.product_log_id` | Directly mapped  
`properties.SessionId` | `network.session_id` | Directly mapped  
`actor.applicationDisplayName` | `principal.application` | Directly mapped  
`properties.Actor.Application` | `principal.application` | Directly mapped  
`properties.DeviceId` | `principal.asset.asset_id` | Directly mapped  
`_hardware` | `principal.asset.hardware` | Merged  
`properties.DeviceName` | `principal.asset.hostname` | Directly mapped  
`properties.DeviceId` | `principal.asset_id` | Directly mapped  
`properties.DeviceName` | `principal.hostname` | Directly mapped  
`properties.OS` | `principal.platform` | Directly mapped  
`properties.OSVersion` | `principal.platform_version` | Directly mapped  
`properties.OsVersion` | `principal.platform_version` | Directly mapped  
`actor.applicationId` | `principal.resource.id` | Directly mapped  
`actor_type_label` | `principal.user.attribute.labels` | Merged  
`auditActorType_label` | `principal.user.attribute.labels` | Merged  
`activityOperationType` | `principal.user.attribute.roles` | Mapped: `Create` → `role`  
`activityType` | `principal.user.attribute.roles` | Mapped values (5 total, e.g. `Create Windows Autopilot Deployment Profile. WindowsAutopilotD...  
`role` | `principal.user.attribute.roles` | Merged  
`properties.UserEmail` | `principal.user.email_addresses` | Merged  
`actor.userId` | `principal.user.product_object_id` | Directly mapped  
`properties.UserName` | `principal.user.user_display_name` | Directly mapped  
`actor.userPrincipalName` | `principal.user.userid` | Directly mapped  
`properties.Actor.UPN` | `principal.user.userid` | Directly mapped  
`properties.AlertType` | `security_result.description` | Directly mapped  
`detection_AlertDisplayName` | `security_result.detection_fields` | Merged  
`detection_DeviceDnsDomain` | `security_result.detection_fields` | Merged  
`detection_DeviceHostName` | `security_result.detection_fields` | Merged  
`detection_DeviceNetBiosName` | `security_result.detection_fields` | Merged  
`detection_DeviceOperatingSystem` | `security_result.detection_fields` | Merged  
`detection_OSDescription` | `security_result.detection_fields` | Merged  
`detection_OS_loc` | `security_result.detection_fields` | Merged  
`detection_OperationalLogCategory` | `security_result.detection_fields` | Merged  
`detection_ScenarioName` | `security_result.detection_fields` | Merged  
`detection_UPNSuffix` | `security_result.detection_fields` | Merged  
`detection_UserDisplayName` | `security_result.detection_fields` | Merged  
`detection_application_id` | `security_result.detection_fields` | Merged  
`detection_object_identity` | `security_result.detection_fields` | Merged  
`operationName` | `security_result.detection_fields` | Mapped: `Reprovision CloudPCModel` → `detection_object_identity`, `Reprovision CloudPCModel`...  
`application` | `target.application` | Renamed/mapped  
`deployment_status` | `target.asset.deployment_status` | Renamed/mapped  
`activityType` | `target.asset.software` | Mapped: `Patch DeviceConfiguration` → `software2`, `Patch DeviceConfiguration` → `software3`...  
`software` | `target.asset.software` | Merged  
`software1` | `target.asset.software` | Merged  
`software2` | `target.asset.software` | Merged  
`software3` | `target.asset.software` | Merged  
`software4` | `target.asset.software` | Merged  
`auditResourceType_label` | `target.resource.attribute.labels` | Merged  
`display_name_label` | `target.resource.attribute.labels` | Merged  
`resources.0.resourceId` | `target.resource.id` | Directly mapped  
`resources.0.type` | `target.resource.name` | Directly mapped  
`resource_type` | `target.resource.resource_type` | Renamed/mapped  
`operationName` | `target.user.email_addresses` | Mapped: `Reprovision CloudPCModel` → `upn_identity`  
`upn_identity` | `target.user.email_addresses` | Mapped: `^.+@.+$` → `upn_identity`  
`user_identity` | `target.user.email_addresses` | Mapped: `^.+@.+$` → `user_identity`  
`user_id` | `target.user.userid` | Directly mapped  
`user_identity` | `target.user.userid` | Directly mapped  
N/A | `metadata.product_name` | Constant: `AZURE MDM INTUNE`  
N/A | `metadata.vendor_name` | Constant: `Microsoft`  
N/A | `principal.platform` | Constant: `MAC`  
N/A | `target.cloud.environment` | Constant: `MICROSOFT_AZURE`  
`resources.auditResourceType` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`resultType", "properties.AADDeviceId", "properties.IntuneDeviceId", "properties.IntuneUserId", "properties.MessageId", "properties.ScaleUnit", and "properties.Os` | `additional.fields` | Mapped from changelog  
`properties.EnrollmentType" and "properties.FailureReason` | `additional.fields` | Mapped from changelog  
`properties.OsVersion", "principal.platform_version", and "properties.StartTimeUtc` | `additional.fields` | Mapped from changelog  
`properties.OperationalLogCategory", "properties.ScenarioName", "properties.UserDisplayName", "properties.UPNSuffix", "properties.DeviceOperatingSystem", "AlertDisplayNameproperties.AlertDisplayName, "properties.DeviceDnsDomain", "properties.DeviceNetBiosName", and "properties.DeviceHostName` | `security_result.detection_fields` | Mapped from changelog  
`identity" and "user_id` | `target.user.userid` | Mapped from changelog  
`properties.SerialNumber` | `_hardware.serial_number` | Mapped from changelog  
`tenantId", "properties.IntuneAccountId", "properties.AADTenantId", "properties.LastContact", "properties.DeviceHealthThreatLevel_loc", "properties.ComplianceState", "properties.InGracePeriodUntil", "properties.RetireAfterDatetime", "properties.ManagementAgents", and "properties.ManagementAgents_loc` | `additional.fields` | Mapped from changelog  
`properties.OS_loc" and "properties.OSDescription` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-mdm-intune-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
