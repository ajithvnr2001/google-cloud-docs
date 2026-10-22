---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-audit/
title: Collect Microsoft Entra ID Directory Audit (formerly Azure Active Directory) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:13.236894+00:00
---

# Collect Microsoft Entra ID Directory Audit (formerly Azure Active Directory) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Entra ID Directory Audit (formerly Azure Active Directory) logs

**Parser Version:** 28.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Microsoft Entra ID (formerly known as Azure Active Directory) directory audit logs by setting up a Google Security Operations feed. You can configure ingestion using two methods: Azure Event Hub (recommended) or the Third Party API.

Entra ID directory audit logs capture changes made within your tenant, including user and group management, application updates, directory role changes, and policy modifications.

**Note:** An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `AZURE_AD_AUDIT` ingestion label.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance.
  * Privileged access to the **Microsoft Azure** portal.
  * **Security Administrator** or **Global Administrator** role in Microsoft Entra ID (required for diagnostic settings).



## Method 1: Azure Event Hub (recommended)

This method streams Entra ID audit logs through Azure Event Hub with Capture enabled, which writes the data to Azure Blob Storage. Google SecOps then ingests the logs from Blob Storage using the Azure Blob Storage V2 feed type.

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
**Storage account name** | Enter a unique name (for example, `secopsauditlogs`)  
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



### Create Event Hub namespace and Event Hub

#### Create Event Hub namespace

  1. In the **Azure portal** , search for **Event Hubs**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select the same resource group as your storage account  
**Namespace name** | Enter a unique name (for example, `secops-entraid-audit`)  
**Location** | Select the same region as your storage account  
**Pricing tier** | Standard (required for Event Hub Capture)  
**Note:** The **Standard** or **Premium** pricing tier is required for Event Hub Capture. The Basic tier does not support Capture.
  4. Click **Review + create** , then click **Create**.

  5. Wait for the deployment to complete.




#### Create Event Hub

  1. Go to the Event Hub namespace you created.
  2. Click **\+ Event Hub** at the top.
  3. Provide the following configuration details: 
     * **Name** : Enter a name (for example, `entraid-audit-logs`).
     * **Partition count** : 2 (default, increase for higher throughput).
     * **Cleanup policy** : Delete.
     * **Retention time (hrs)** : 24 (minimum, increase if needed for resilience).
  4. Click **Review + create** , then click **Create**.



### Enable Event Hub Capture

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
**Blob Container** | Create or select a container (for example, `entraid-audit-capture`)  
**Note:** If no container exists, select **Create container** and enter a name.
  5. Click **Save**.

**Note:** Event Hub Capture writes files in Apache Avro format to the blob container. Google SecOps can parse Avro-formatted Entra ID logs.



### Configure Entra ID diagnostic settings

  1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a **Security Administrator**.
  2. Go to **Entra ID > Monitoring & health > Diagnostic settings**.
  3. Click **Add diagnostic setting**.
  4. Provide the following configuration details: 
     * **Diagnostic setting name** : Enter a descriptive name (for example, `audit-logs-to-eventhub`).
     * In the **Logs** section, select **AuditLogs**.
     * In the **Destination details** section, select **Stream to an event hub**.
     * **Subscription** : Select the subscription containing your Event Hub namespace.
     * **Event hub namespace** : Select the namespace you created (for example, `secops-entraid-audit`).
     * **Event hub name** : Select the Event Hub you created (for example, `entraid-audit-logs`).
     * **Event hub policy name** : Select **RootManageSharedAccessKey**.
  5. Click **Save**.

**Note:** It may take up to 15 minutes for audit logs to start flowing through the Event Hub.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



### Configure a feed in Google SecOps to ingest Entra ID audit logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Entra ID Audit Logs - Event Hub`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Azure AD Directory Audit** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the capture container path:
    
    https://<storage-account>.blob.core.windows.net/entraid-audit-capture/
    

Replace `<storage-account>` with your Azure storage account name.

**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers.
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Shared key** : Enter the shared access key value from the Storage Account.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Create feed**. 




After creating the feed, it may take 5-10 minutes before logs start appearing in Google SecOps.

**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

For more information about Google Security Operations feeds, see [Google Security Operations feeds documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management). For information about requirements for each feed type, see [Feed configuration by type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#feed_configuration_by_type). If you encounter issues when you create feeds, [contact Google Security Operations support](https://docs.cloud.google.com/chronicle/docs/getting-support).

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

This method uses the Microsoft Graph API to retrieve Entra ID directory audit logs directly from your Microsoft tenant.

**Caution:** You must enable allowlisting and add the IP ranges for all log types that ingest data from third-party APIs. See [IP Allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip_allowlisting).

### Configure IP allowlisting

Before creating the feed, you must allowlist Google SecOps IP ranges in your Microsoft Azure network settings or Conditional Access policies.

#### Get Google SecOps IP ranges

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Note the IP ranges displayed in the feed creation interface.
  4. Alternatively, retrieve IP ranges programmatically using the [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api).



#### Configure Conditional Access for workload identities (if required)

If your organization uses Conditional Access policies that restrict access by location:

  1. In the **Microsoft Entra admin center** , go to **Protection > Conditional Access > Named locations**.
  2. Click **\+ New location**.
  3. Provide the following configuration details: 
     * **Name** : Enter `Google SecOps IP Ranges`.
     * **Mark as trusted location** : Optional, based on your security policy.
     * **IP ranges** : Add each Google SecOps IP range in CIDR notation.
  4. Click **Create**.
  5. Go to **Conditional Access > Policies**.
  6. For any policies that apply to workload identities, configure an exclusion for the `Google SecOps IP Ranges` named location or the specific service principal.



### Configure Microsoft Entra app registration

#### Create app registration

  1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) or [Azure portal](https://portal.azure.com/).
  2. Go to **Identity > Applications > App registrations**.
  3. Click **New registration**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Audit Logs Integration`).
     * **Supported account types** : Select **Accounts in this organizational directory only (Single tenant)**.
     * **Redirect URI** : Leave blank (not required for service principal authentication).
  5. Click **Register**.
  6. After registration, copy and save the following values: 
     * **Application (client) ID**
     * **Directory (tenant) ID**



#### Configure API permissions

  1. In the app registration, go to **API permissions**.
  2. Click **Add a permission**.
  3. Select **Microsoft Graph > Application permissions**.
  4. Search for and select the following permissions: 
     * **AuditLog.Read.All** \- Required to read directory audit logs.
     * **Directory.Read.All** \- Required by Microsoft Graph API for audit log access.
  5. Click **Add permissions**.
  6. Click **Grant admin consent for [Your Organization]**.
  7. Verify that the **Status** column shows **Granted for [Your Organization]** for all permissions.

**Note:** If the **Grant admin consent** button is disabled, ensure you have **Global Administrator** or **Privileged Role Administrator** role. Cloud Application Administrator role cannot grant consent for Microsoft Graph application permissions.

Permission | Type | Description  
---|---|---  
**AuditLog.Read.All** | Application | Read all audit log data  
**Directory.Read.All** | Application | Read directory data (required for API access)  
  
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




## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started** ### Configure a feed in Google SecOps to ingest Entra ID audit logs


  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Entra ID Directory Audit Logs`).
  5. Select **Third Party API** as the **Source type**.
  6. Select **Azure AD Directory Audit** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **OAuth Client ID** : Enter the **Application (client) ID** from the app registration.
     * **OAuth Client Secret** : Enter the **client secret value** you copied earlier.
     * **Tenant ID** : Enter the **Directory (tenant) ID** from the app registration in UUID format (for example, `0fc279f9-fe30-41be-97d3-abe1d7681418`).
     * **API Full Path** : Enter the Microsoft Graph REST API endpoint URL:
    
    graph.microsoft.com/v1.0/auditLogs/directoryAudits
    

**Note:** Do not include the `https://` prefix. The feed adds the protocol automatically.
     * **API Authentication Endpoint** : Enter the Microsoft Active Directory authentication endpoint:
    
    login.microsoftonline.com
    

**Note:** Do not include the `https://` prefix or the `/oauth2/v2.0/token` path. The feed constructs the full authentication URL automatically using your Tenant ID.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Create feed**.


**Note:** After creating the feed, it may take 5-10 minutes before logs start appearing in Google SecOps.**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

For more information about Google Security Operations feeds, see [Google Security Operations feeds documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management). For information about requirements for each feed type, see [Feed configuration by type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#feed_configuration_by_type). If you encounter issues when you create feeds, [contact Google Security Operations support](https://docs.cloud.google.com/chronicle/docs/getting-support).

### Regional endpoints

For Microsoft Entra ID deployments in sovereign clouds, use the appropriate regional endpoints:

Cloud Environment | API Full Path | API Authentication Endpoint  
---|---|---  
**Global** | `graph.microsoft.com/v1.0/auditLogs/directoryAudits` | `login.microsoftonline.com`  
**US Government L4** | `graph.microsoft.us/v1.0/auditLogs/directoryAudits` | `login.microsoftonline.us`  
**US Government L5 (DOD)** | `dod-graph.microsoft.us/v1.0/auditLogs/directoryAudits` | `login.microsoftonline.us`  
**China (21Vianet)** | `microsoftgraph.chinacloudapi.cn/v1.0/auditLogs/directoryAudits` | `login.chinacloudapi.cn`  
  
## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`grouptypelabel` | `about.group.attribute.labels` | Merged  
`targetResourceType` | `about.group.attribute.labels` | Mapped: `Group` → `grouptypelabel`  
`target.displayName` | `about.group.group_display_name` | Directly mapped  
`target.id` | `about.group.product_object_id` | Directly mapped  
`resultField` | `about.labels` | Merged  
`target.displayName` | `about.resource.name` | Directly mapped  
`target.id` | `about.resource.product_object_id` | Directly mapped  
`targetResourceType` | `about.resource.resource_subtype` | Directly mapped  
`target.id` | `about.user.product_object_id` | Directly mapped  
`initiatedBy.user.displayName` | `about.user.user_display_name` | Directly mapped  
`policies.displayName` | `about.user.user_display_name` | Directly mapped  
`target.displayName` | `about.user.user_display_name` | Directly mapped  
`policies.id` | `about.user.userid` | Directly mapped  
`userPrincipalName` | `about.user.userid` | Directly mapped  
`AdditionalDetail_label` | `additional.fields` | Merged  
`ReleaseVersion_label` | `additional.fields` | Merged  
`Stamp_label` | `additional.fields` | Merged  
`_field` | `additional.fields` | Merged  
`add_about_field` | `additional.fields` | Merged  
`add_about_label` | `additional.fields` | Merged  
`additional_applicationFilter` | `additional.fields` | Merged  
`additional_applicationFilter_new` | `additional.fields` | Merged  
`additional_builtInControls` | `additional.fields` | Merged  
`additional_builtInControls_new` | `additional.fields` | Merged  
`additional_category` | `additional.fields` | Merged  
`additional_clientAppTypes` | `additional.fields` | Merged  
`additional_clientAppTypes_new` | `additional.fields` | Merged  
`additional_createdDateTime_new` | `additional.fields` | Merged  
`additional_createdDateTime_old` | `additional.fields` | Merged  
`additional_customAuthenticationFactors` | `additional.fields` | Merged  
`additional_customAuthenticationFactors_new` | `additional.fields` | Merged  
`additional_displayName` | `additional.fields` | Merged  
`additional_displayName_new` | `additional.fields` | Merged  
`additional_displayname` | `additional.fields` | Merged  
`additional_excludeApplications` | `additional.fields` | Merged  
`additional_excludeApplications_new` | `additional.fields` | Merged  
`additional_excludeGroups` | `additional.fields` | Merged  
`additional_excludeGroups_new` | `additional.fields` | Merged  
`additional_excludeLocations` | `additional.fields` | Merged  
`additional_excludeLocations_new` | `additional.fields` | Merged  
`additional_excludePlatform` | `additional.fields` | Merged  
`additional_excludePlatforms_new` | `additional.fields` | Merged  
`additional_excludeUsers` | `additional.fields` | Merged  
`additional_excludeUsers_new` | `additional.fields` | Merged  
`additional_fields` | `additional.fields` | Merged  
`additional_id` | `additional.fields` | Merged  
`additional_id_new` | `additional.fields` | Merged  
`additional_includeApplications` | `additional.fields` | Merged  
`additional_includeApplications_new` | `additional.fields` | Merged  
`additional_includeAuthenticationContextClassReferences` | `additional.fields` | Merged  
`additional_includeAuthenticationContextClassReferences_new` | `additional.fields` | Merged  
`additional_includeGroups` | `additional.fields` | Merged  
`additional_includeGroups_new` | `additional.fields` | Merged  
`additional_includeLocations` | `additional.fields` | Merged  
`additional_includeLocations_new` | `additional.fields` | Merged  
`additional_includePlatform` | `additional.fields` | Merged  
`additional_includePlatforms_new` | `additional.fields` | Merged  
`additional_includeRoles` | `additional.fields` | Merged  
`additional_includeRoles_new` | `additional.fields` | Merged  
`additional_includeUserActions` | `additional.fields` | Merged  
`additional_includeUserActions_new` | `additional.fields` | Merged  
`additional_includeUsers` | `additional.fields` | Merged  
`additional_includeUsers_new` | `additional.fields` | Merged  
`additional_includeuserRiskLevel` | `additional.fields` | Merged  
`additional_label` | `additional.fields` | Merged  
`additional_loggedByService` | `additional.fields` | Merged  
`additional_modifiedDateTime_new` | `additional.fields` | Merged  
`additional_modifiedDateTime_old` | `additional.fields` | Merged  
`additional_newValue` | `additional.fields` | Merged  
`additional_oldValue` | `additional.fields` | Merged  
`additional_old_operator` | `additional.fields` | Merged  
`additional_operator` | `additional.fields` | Merged  
`additional_resourceId` | `additional.fields` | Merged  
`additional_servicePrincipalRiskLevels` | `additional.fields` | Merged  
`additional_servicePrincipalRiskLevels_new` | `additional.fields` | Merged  
`additional_signInRiskLevels` | `additional.fields` | Merged  
`additional_signInRiskLevels_new` | `additional.fields` | Merged  
`additional_state` | `additional.fields` | Merged  
`additional_state_new` | `additional.fields` | Merged  
`additional_termsOfUses` | `additional.fields` | Merged  
`additional_termsOfUses_new` | `additional.fields` | Merged  
`additional_userRiskLevels_new` | `additional.fields` | Merged  
`agentSubjectType_label` | `additional.fields` | Merged  
`agentType_label` | `additional.fields` | Merged  
`agent_type_label` | `additional.fields` | Merged  
`aio_label` | `additional.fields` | Merged  
`appDisplayName_label` | `additional.fields` | Merged  
`appId_label` | `additional.fields` | Merged  
`app_owner_tenant_id_label` | `additional.fields` | Merged  
`app_service_principal_id_label` | `additional.fields` | Merged  
`appidacr_label` | `additional.fields` | Merged  
`aud_label` | `additional.fields` | Merged  
`authentication_processing_details_label` | `additional.fields` | Merged  
`authentication_protocol_label` | `additional.fields` | Merged  
`authentication_strengths_label` | `additional.fields` | Merged  
`changed_applicationFilter_label` | `additional.fields` | Merged  
`changed_builtInControls_new` | `additional.fields` | Merged  
`changed_clientAppTypes_label` | `additional.fields` | Merged  
`changed_createdDateTime_label` | `additional.fields` | Merged  
`changed_customAuthenticationFactors_new` | `additional.fields` | Merged  
`changed_displayName_label` | `additional.fields` | Merged  
`changed_excludeApplications_new` | `additional.fields` | Merged  
`changed_excludeGroups_new` | `additional.fields` | Merged  
`changed_excludeLocations_new` | `additional.fields` | Merged  
`changed_excludePlatforms_new` | `additional.fields` | Merged  
`changed_excludeUsers_new` | `additional.fields` | Merged  
`changed_id_label` | `additional.fields` | Merged  
`changed_includeApplications_label` | `additional.fields` | Merged  
`changed_includeAuthenticationContextClassReferences_new` | `additional.fields` | Merged  
`changed_includeGroups_new` | `additional.fields` | Merged  
`changed_includeLocations_label` | `additional.fields` | Merged  
`changed_includePlatforms_new` | `additional.fields` | Merged  
`changed_includeRoles_new` | `additional.fields` | Merged  
`changed_includeUserActions_new` | `additional.fields` | Merged  
`changed_includeUsers_new` | `additional.fields` | Merged  
`changed_modifiedDateTime_label` | `additional.fields` | Merged  
`changed_operator_label` | `additional.fields` | Merged  
`changed_servicePrincipalRiskLevels_new` | `additional.fields` | Merged  
`changed_signInRiskLevels_new` | `additional.fields` | Merged  
`changed_state_label` | `additional.fields` | Merged  
`changed_termsOfUses_new` | `additional.fields` | Merged  
`changed_userRiskLevels_new` | `additional.fields` | Merged  
`claims_tenantid_label` | `additional.fields` | Merged  
`client_credential_type_label` | `additional.fields` | Merged  
`durationMs_label` | `additional.fields` | Merged  
`duration_ms_label` | `additional.fields` | Merged  
`eventCategory_label` | `additional.fields` | Merged  
`event_name_label` | `additional.fields` | Merged  
`exp_label` | `additional.fields` | Merged  
`hierarchy_label` | `additional.fields` | Merged  
`home_tenant_id_label` | `additional.fields` | Merged  
`iat_label` | `additional.fields` | Merged  
`identity_label` | `additional.fields` | Merged  
`idtyp_label` | `additional.fields` | Merged  
`incoming_token_type_label` | `additional.fields` | Merged  
`initiatedBy_label` | `additional.fields` | Merged  
`initiatedBy_type_label` | `additional.fields` | Merged  
`isTenantRestricted_label` | `additional.fields` | Merged  
`isThroughGlobalSecureAccess_label` | `additional.fields` | Merged  
`iss_label` | `additional.fields` | Merged  
`map_field` | `additional.fields` | Merged  
`mfaAuthDetail_label` | `additional.fields` | Merged  
`mfa_auth_method_label` | `additional.fields` | Merged  
`modified_property_displayname` | `additional.fields` | Mapped: `userPrincipalName` → `old_value_label`, `userPrincipalName` → `new_value_label`  
`nameidentifier_label` | `additional.fields` | Merged  
`nbf_label` | `additional.fields` | Merged  
`new_value_label` | `additional.fields` | Merged  
`old_clientAppTypes` | `additional.fields` | Mapped: `new_clientAppTypes` → `changed_clientAppTypes_label`  
`old_createdDateTime` | `additional.fields` | Mapped: `new_createdDateTime` → `changed_createdDateTime_label`  
`old_displayName_value` | `additional.fields` | Mapped: `new_displayName_value` → `changed_displayName_label`  
`old_grantControls` | `additional.fields` | Mapped: `new_grantControls` → `changed_operator_label`  
`old_id_value` | `additional.fields` | Mapped: `new_id_value` → `changed_id_label`  
`old_includeLocations` | `additional.fields` | Mapped: `new_includeLocations` → `changed_includeLocations_label`  
`old_include_applications` | `additional.fields` | Mapped: `new_include_applications` → `changed_includeApplications_label`, `new_include_appli...  
`old_modifiedDateTime` | `additional.fields` | Mapped: `new_modifiedDateTime` → `changed_modifiedDateTime_label`  
`old_state_value` | `additional.fields` | Mapped: `new_state_value` → `changed_state_label`  
`old_value_label` | `additional.fields` | Merged  
`operationType_label` | `additional.fields` | Merged  
`originalRequestId_label` | `additional.fields` | Merged  
`prop_isInteractive_label` | `additional.fields` | Merged  
`prop_log_version_label` | `additional.fields` | Merged  
`prop_processingTimeInMilliseconds_label` | `additional.fields` | Merged  
`prop_signInIdentifierType_label` | `additional.fields` | Merged  
`properties_category_label` | `additional.fields` | Merged  
`properties_correlationId_label` | `additional.fields` | Merged  
`provisioningAction_label` | `additional.fields` | Merged  
`removed_builtInControls_label` | `additional.fields` | Merged  
`removed_customAuthenticationFactors_label` | `additional.fields` | Merged  
`removed_excludeApplications_label` | `additional.fields` | Merged  
`removed_excludeGroups_label` | `additional.fields` | Merged  
`removed_excludeLocations_label` | `additional.fields` | Merged  
`removed_excludeUsers_label` | `additional.fields` | Merged  
`removed_includeAuthenticationContextClassReferences_label` | `additional.fields` | Merged  
`removed_includeGroups_label` | `additional.fields` | Merged  
`removed_includePlatform_label` | `additional.fields` | Merged  
`removed_includeRoles_label` | `additional.fields` | Merged  
`removed_includeUserActions_label` | `additional.fields` | Merged  
`removed_includeUsers_label` | `additional.fields` | Merged  
`removed_includeuserRiskLevel_label` | `additional.fields` | Merged  
`removed_servicePrincipalRiskLevels_label` | `additional.fields` | Merged  
`removed_signInRiskLevels_label` | `additional.fields` | Merged  
`removed_termsOfUses_label` | `additional.fields` | Merged  
`resourceId_label` | `additional.fields` | Merged  
`resource_owner_tenant_id_label` | `additional.fields` | Merged  
`resource_service_principal_id_label` | `additional.fields` | Merged  
`resource_tenant_id_label` | `additional.fields` | Merged  
`result_signature_label` | `additional.fields` | Merged  
`rh_label` | `additional.fields` | Merged  
`riskEventType_label` | `additional.fields` | Merged  
`roleAssignmentId_label` | `additional.fields` | Merged  
`roleAssignmentScope_label` | `additional.fields` | Merged  
`roleDefinitionId_label` | `additional.fields` | Merged  
`serviceRequestId_label` | `additional.fields` | Merged  
`session_id_label` | `additional.fields` | Merged  
`signInEventTypes_label` | `additional.fields` | Merged  
`sign_in_token_protection_status_label` | `additional.fields` | Merged  
`signin_session_status_label` | `additional.fields` | Merged  
`statusCode_label` | `additional.fields` | Merged  
`targetResourceType` | `additional.fields` | Mapped: `"Device", "User", "Directory", "Application", "Group", "ServicePrincipal", "Role"` ...  
`targetResources_agentType_label` | `additional.fields` | Merged  
`tenantId_Label` | `additional.fields` | Merged  
`tenantId_label` | `additional.fields` | Merged  
`tenant_id_label` | `additional.fields` | Merged  
`tokenIssuerType_label` | `additional.fields` | Merged  
`token_protection_type_label` | `additional.fields` | Merged  
`trustType_label` | `additional.fields` | Merged  
`unique_token_identifier_label` | `additional.fields` | Merged  
`uti_label` | `additional.fields` | Merged  
`ver_label` | `additional.fields` | Merged  
`xms_ftd_label` | `additional.fields` | Merged  
`xms_idrel_label` | `additional.fields` | Merged  
`xms_rd_label` | `additional.fields` | Merged  
`xms_tcdt_label` | `additional.fields` | Merged  
`operationName` | `extensions.auth.type` | Mapped: `Sign-in activity` → `SSO`  
`target_userid_present` | `extensions.auth.type` | Mapped: `true` → `MACHINE`  
`logged_by_service` | `intermediary.application` | Directly mapped  
`ActivityDisplayName` | `metadata.description` | Directly mapped  
`record_properties_message` | `metadata.description` | Mapped when `record_properties_message` != ``  
`resultDescription` | `metadata.description` | Directly mapped  
`ActivityDateTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSSSSSZ`  
`TimeGenerated` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSSSSSZ`  
`_TimeReceived` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSSSSSZ`  
`logcollector_timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`properties.activityDateTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`record.time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`time_1` | `metadata.event_timestamp` | Parsed as `UNIX`  
`when` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`activityDisplayName` | `metadata.event_type` | Mapped values (96 total, e.g. `Admin deleted security info` → `USER_DELETION`, `Add applicat...  
`category` | `metadata.event_type` | Mapped values (98 total, e.g. `AdministrativeUnit` → `USER_RESOURCE_CREATION`, `Administrati...  
`eventType` | `metadata.event_type` | Mapped: `USER_UNCATEGORIZED` → `USER_RESOURCE_ACCESS`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_target_hostname` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`  
`has_target_resource` | `metadata.event_type` | Mapped: `true` → `USER_RESOURCE_ACCESS`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`loggedByService` | `metadata.event_type` | Mapped values (31 total, e.g. `Application proxy` → `SERVICE_CREATION`, `Application proxy` ...  
`operationName` | `metadata.event_type` | Mapped: `Sign-in activity` → `USER_LOGIN`  
`principal_ip_present` | `metadata.event_type` | Mapped values (7 total, e.g. `true` → `USER_UNCATEGORIZED`, `true` → `NETWORK_CONNECTION`, `...  
`principal_userid_present` | `metadata.event_type` | Mapped values (6 total, e.g. `false` → `USER_RESOURCE_ACCESS`, `true` → `USER_UNCATEGORIZED`...  
`target_userid_present` | `metadata.event_type` | Mapped: `true` → `USER_CHANGE_PERMISSIONS`, `true` → `USER_CREATION`, `true` → `USER_LOGIN`  
`AADTenantId` | `metadata.product_deployment_id` | Directly mapped  
`OperationName` | `metadata.product_event_type` | Directly mapped  
`activityDisplayName` | `metadata.product_event_type` | Directly mapped  
`operationName` | `metadata.product_event_type` | Directly mapped  
`record_operationName` | `metadata.product_event_type` | Mapped when `record_operationName` != ``  
`Id` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`properties.AuditEventId` | `metadata.product_log_id` | Directly mapped  
`properties_id` | `metadata.product_log_id` | Directly mapped  
`OperationVersion` | `metadata.product_version` | Directly mapped  
`operationVersion` | `metadata.product_version` | Directly mapped  
`kv.value` | `network.http.parsed_user_agent` | Directly mapped  
`properties.userAgent` | `network.http.parsed_user_agent` | Directly mapped  
`kv.value` | `network.http.user_agent` | Directly mapped  
`properties.userAgent` | `network.http.user_agent` | Directly mapped  
`correlationId` | `network.session_id` | Directly mapped  
`record_correlationId` | `network.session_id` | Mapped when `record_correlationId` != ``  
`domain` | `principal.administrative_domain` | Directly mapped  
`InitiatedBy.app.displayName` | `principal.application` | Directly mapped  
`clientAppUsed` | `principal.application` | Directly mapped  
`initiatedBy.app.displayName` | `principal.application` | Directly mapped  
`properties.Actor.ApplicationName` | `principal.application` | Directly mapped  
`properties.servicePrincipal.Name` | `principal.application` | Directly mapped  
`properties.servicePrincipalName` | `principal.application` | Directly mapped  
`properties_initiatedBy_app_displayName` | `principal.application` | Directly mapped  
`properties.deviceDetail.deviceId` | `principal.asset.asset_id` | Directly mapped  
`isCompliant_label` | `principal.asset.attribute.labels` | Merged  
`isManaged_label` | `principal.asset.attribute.labels` | Merged  
`service_principal_id_label` | `principal.asset.attribute.labels` | Merged  
`sourceSystem_label` | `principal.asset.attribute.labels` | Merged  
`hardware` | `principal.asset.hardware` | Merged  
`ip` | `principal.asset.ip` | Merged  
`ip_addr` | `principal.asset.ip` | Merged  
`ip_address` | `principal.asset.ip` | Merged  
`ip_value` | `principal.asset.ip` | Merged  
`principal_ip` | `principal.asset.ip` | Merged  
`properties.sourceSystem.Id` | `principal.asset.product_object_id` | Directly mapped  
`properties.deviceDetail.deviceId` | `principal.asset_id` | Directly mapped  
`principal_hostname` | `principal.hostname` | Directly mapped  
`ip` | `principal.ip` | Merged  
`ip_addr` | `principal.ip` | Merged  
`ip_address` | `principal.ip` | Merged  
`ip_value` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`location.city` | `principal.location.city` | Renamed/mapped  
`prop_loc_city` | `principal.location.city` | Directly mapped  
`location.countryOrRegion` | `principal.location.country_or_region` | Renamed/mapped  
`prop_loc_countryOrRegion` | `principal.location.country_or_region` | Directly mapped  
`record_RoleLocation` | `principal.location.name` | Mapped when `record_RoleLocation` != ``  
`location.geoCoordinates.latitude` | `principal.location.region_latitude` | Renamed/mapped  
`prop_loc_latitude` | `principal.location.region_latitude` | Directly mapped  
`location.geoCoordinates.longitude` | `principal.location.region_longitude` | Renamed/mapped  
`prop_loc_longitude` | `principal.location.region_longitude` | Directly mapped  
`location.state` | `principal.location.state` | Renamed/mapped  
`prop_loc_state` | `principal.location.state` | Directly mapped  
`properties.deviceDetail.operatingSystem` | `principal.platform_version` | Directly mapped  
`Identity_label` | `principal.resource.attribute.labels` | Merged  
`_field` | `principal.resource.attribute.labels` | Merged  
`activityDisplayName` | `principal.resource.attribute.labels` | Mapped: `"Add user", "Update StsRefreshTokenValidFrom Timestamp", "Disable account", "Enable...  
`app_id` | `principal.resource.attribute.labels` | Merged  
`browser_label` | `principal.resource.attribute.labels` | Merged  
`key` | `principal.resource.attribute.labels` | Mapped: `"IsDelegatedAdmin", "Actor_Name", "PartnerTenantId"` → `map_field`, `"resource_grou...  
`map_field` | `principal.resource.attribute.labels` | Merged  
`prop_clientAppType_label` | `principal.resource.attribute.labels` | Merged  
`properties_initiatedBy_app_appId_label` | `principal.resource.attribute.labels` | Merged  
`user_principal_name_label` | `principal.resource.attribute.labels` | Merged  
`Resource` | `principal.resource.name` | Directly mapped  
`ResourceId` | `principal.resource.product_object_id` | Directly mapped  
`properties.Actor.Application` | `principal.resource.product_object_id` | Directly mapped  
`record_identity_evidence_authorization_principalType` | `principal.resource.resource_subtype` | Mapped when `record_identity_evidence_authorization_principalType` != ``  
`Type` | `principal.resource.type` | Mapped: `(?i)AuditLogs` → `AUDIT_LOG`  
`role` | `principal.user.attribute.roles` | Merged  
`role_label` | `principal.user.attribute.roles` | Merged  
`user_role` | `principal.user.attribute.roles` | Merged  
`InitiatedBy.user.userPrincipalName` | `principal.user.email_addresses` | Merged  
`activityDisplayName` | `principal.user.email_addresses` | Mapped: `"Add user", "Update StsRefreshTokenValidFrom Timestamp", "Disable account", "Enable...  
`email` | `principal.user.email_addresses` | Merged  
`initiatedBy.user.userPrincipalName` | `principal.user.email_addresses` | Merged  
`properties.sourceIdentity.details.UserPrincipalName` | `principal.user.email_addresses` | Merged  
`properties_Actor_UPN` | `principal.user.email_addresses` | Merged  
`CorrelationId` | `principal.user.product_object_id` | Directly mapped  
`initiatedBy.app.servicePrincipalId` | `principal.user.product_object_id` | Directly mapped  
`initiatedBy.user.id` | `principal.user.product_object_id` | Directly mapped  
`properties.Actor.ObjectId` | `principal.user.product_object_id` | Directly mapped  
`properties.servicePrincipalId` | `principal.user.product_object_id` | Directly mapped  
`properties.sourceIdentity.Id` | `principal.user.product_object_id` | Directly mapped  
`properties.sourceIdentity.details.id` | `principal.user.product_object_id` | Directly mapped  
`properties_initiatedBy_app_servicePrincipalId` | `principal.user.product_object_id` | Directly mapped  
`InitiatedBy.user.displayName` | `principal.user.user_display_name` | Directly mapped  
`initiatedBy.user.displayName` | `principal.user.user_display_name` | Directly mapped  
`initiatedBy.user.userPrincipalName` | `principal.user.user_display_name` | Directly mapped  
`properties.sourceIdentity.Name` | `principal.user.user_display_name` | Directly mapped  
`properties.sourceIdentity.details.DisplayName` | `principal.user.user_display_name` | Directly mapped  
`user_name` | `principal.user.user_display_name` | Directly mapped  
`InitiatedBy.app.servicePrincipalId` | `principal.user.userid` | Directly mapped  
`InitiatedBy.user.id` | `principal.user.userid` | Directly mapped  
`initiatedBy.app.servicePrincipalName` | `principal.user.userid` | Directly mapped  
`initiatedBy.user.userPrincipalName` | `principal.user.userid` | Directly mapped  
`properties.initiatedBy.Id` | `principal.user.userid` | Directly mapped  
`record_identity_evidence_authorization_principalId` | `principal.user.userid` | Mapped when `record_identity_evidence_authorization_principalId` != ``  
`sec_result` | `security_result` | Merged  
`Result` | `security_result.action` | Mapped: `(?i)success` → `security_result_action_allow`, `(?i)failure` → `security_result_act...  
`action` | `security_result.action` | Merged  
`operationName` | `security_result.action` | Mapped: `Sign-in activity` → `action`  
`result` | `security_result.action` | Mapped: `(?i)success` → `security_result_action_allow`, `(?i)failure` → `security_result_act...  
`resultType` | `security_result.action` | Mapped: `0` → `action`  
`security_result_action` | `security_result.action` | Merged  
`security_result_action_allow` | `security_result.action` | Merged  
`security_result_action_block` | `security_result.action` | Merged  
`operationType` | `security_result.action_details` | Directly mapped  
`resultType` | `security_result.action_details` | Directly mapped  
`Category` | `security_result.category` | Merged  
`operationName` | `security_result.category` | Mapped: `Sign-in activity` → `Category`  
`Category` | `security_result.category_details` | Mapped: `(?i)Device` → `Category`  
`properties_category` | `security_result.category_details` | Merged  
`sec_result_category_details` | `security_result.category_details` | Merged  
`Result` | `security_result.description` | Directly mapped  
`properties.provisioningStatusInfo.errorInformation` | `security_result.description` | Directly mapped  
`properties_status_additionalDetails` | `security_result.description` | Directly mapped  
`resultDescription` | `security_result.description` | Directly mapped  
`resultReason` | `security_result.description` | Directly mapped  
`_field` | `security_result.detection_fields` | Merged  
`auth_app_device_app_version_label` | `security_result.detection_fields` | Merged  
`auth_app_device_client_app_label` | `security_result.detection_fields` | Merged  
`auth_app_device_id_label` | `security_result.detection_fields` | Merged  
`auth_app_device_os_label` | `security_result.detection_fields` | Merged  
`auth_app_policy_adminConfiguration_label` | `security_result.detection_fields` | Merged  
`auth_app_policy_authenticationEvaluation_label` | `security_result.detection_fields` | Merged  
`auth_app_policy_policyName_label` | `security_result.detection_fields` | Merged  
`auth_app_policy_status_label` | `security_result.detection_fields` | Merged  
`auth_detail_label` | `security_result.detection_fields` | Merged  
`auth_id_label` | `security_result.detection_fields` | Merged  
`auth_proc_det_label` | `security_result.detection_fields` | Merged  
`auth_req_label` | `security_result.detection_fields` | Merged  
`caa_label` | `security_result.detection_fields` | Merged  
`detection_authenticationMethod` | `security_result.detection_fields` | Merged  
`detection_authenticationMethodDetail` | `security_result.detection_fields` | Merged  
`detection_authenticationStepDateTime` | `security_result.detection_fields` | Merged  
`detection_authenticationStepRequirement` | `security_result.detection_fields` | Merged  
`detection_authenticationStepResultDetail` | `security_result.detection_fields` | Merged  
`detection_detail` | `security_result.detection_fields` | Merged  
`detection_networkName` | `security_result.detection_fields` | Merged  
`detection_networkType` | `security_result.detection_fields` | Merged  
`detection_requestSequence` | `security_result.detection_fields` | Merged  
`detection_requirementProvider` | `security_result.detection_fields` | Merged  
`detection_statusSequence` | `security_result.detection_fields` | Merged  
`detection_succeeded` | `security_result.detection_fields` | Merged  
`enforcedGrantControls_label` | `security_result.detection_fields` | Merged  
`enforcedSessionControls_label` | `security_result.detection_fields` | Merged  
`key` | `security_result.detection_fields` | Mapped: `"cribl_source", "topic_name", "source_system", "internal_workspace_resource_id"` → ...  
`policy_conditionsNotSatisfied_label` | `security_result.detection_fields` | Merged  
`policy_conditionsSatisfied_label` | `security_result.detection_fields` | Merged  
`policy_displayName_label` | `security_result.detection_fields` | Merged  
`policy_id_label` | `security_result.detection_fields` | Merged  
`policy_result_label` | `security_result.detection_fields` | Merged  
`resultType_label` | `security_result.detection_fields` | Merged  
`riskLevelAggregated_label` | `security_result.detection_fields` | Merged  
`session_lifetime_policy_detail_label` | `security_result.detection_fields` | Merged  
`session_lifetime_policy_expirationRequirement_label` | `security_result.detection_fields` | Merged  
`statusInfo_label` | `security_result.detection_fields` | Merged  
`value_label` | `security_result.detection_fields` | Merged  
`operationName` | `security_result.priority` | Mapped: `Sign-in activity` → `MEDIUM_PRIORITY`  
`riskLevelDuringSignIn` | `security_result.priority` | Mapped: `medium` → `MEDIUM_PRIORITY`  
`resultType` | `security_result.rule_id` | Directly mapped  
`kv.value` | `security_result.rule_name` | Directly mapped  
`Level` | `security_result.severity` | Mapped values (5 total, e.g. `"0", "1", "2"` → `CRITICAL`, `3` → `ERROR`, `4` → `HIGH`)  
`level` | `security_result.severity` | Mapped: `(?i)informational/info` → `INFORMATIONAL`  
`operationName` | `security_result.severity` | Mapped: `Sign-in activity` → `ERROR`  
`Level` | `security_result.severity_details` | Directly mapped  
`level` | `security_result.severity_details` | Directly mapped  
`AADOperationType` | `security_result.summary` | Directly mapped  
`operationName` | `security_result.summary` | Mapped: `Sign-in activity` → `Successful login occurred`, `Sign-in activity` → `Failed login...  
`properties.provisioningStatusInfo.Status` | `security_result.summary` | Directly mapped  
`result` | `security_result.summary` | Directly mapped  
`result1` | `security_result.summary` | Directly mapped  
`resultType` | `security_result.summary` | Mapped: `0` → `Successful login occurred`  
`prop_riskDetail` | `security_result.threat_name` | Directly mapped  
`modified_properties_old_value_label` | `src.resource.attribute.labels` | Merged  
`targetResourceType` | `src.resource.attribute.labels` | Mapped: `"Device", "User", "Directory", "Application", "Group", "ServicePrincipal", "Role"` ...  
`target_domain` | `target.administrative_domain` | Directly mapped  
`appDisplayName` | `target.application` | Directly mapped  
`modifiedProperties.newValue` | `target.asset.asset_id` | Directly mapped  
`targetSystem_ApplicationId_label` | `target.asset.attribute.labels` | Merged  
`targetSystem_ServicePrincipalDisplayName_label` | `target.asset.attribute.labels` | Merged  
`targetSystem_label` | `target.asset.attribute.labels` | Merged  
`target_service_principal_label` | `target.asset.attribute.labels` | Merged  
`kv.value` | `target.asset.hostname` | Directly mapped  
`temp_display_name` | `target.asset.hostname` | Directly mapped  
`properties.targetSystem.Id` | `target.asset.product_object_id` | Directly mapped  
`grouptypelabel` | `target.group.attribute.labels` | Merged  
`index` | `target.group.attribute.labels` | Mapped: `0` → `grouptypelabel`  
`targetResourceType` | `target.group.attribute.labels` | Mapped: `Group` → `grouptypelabel`  
`modifiedProperties.newValue` | `target.group.group_display_name` | Directly mapped  
`target.displayName` | `target.group.group_display_name` | Directly mapped  
`modifiedProperties.newValue` | `target.group.product_object_id` | Directly mapped  
`target.id` | `target.group.product_object_id` | Directly mapped  
`kv.value` | `target.hostname` | Directly mapped  
`temp_display_name` | `target.hostname` | Directly mapped  
`target_ip` | `target.ip` | Merged  
`kv.value` | `target.process.pid` | Directly mapped  
`modified_properties_new_value_label_value` | `target.process.pid` | Directly mapped  
`appId_label` | `target.resource.attribute.labels` | Merged  
`app_id_label` | `target.resource.attribute.labels` | Merged  
`authorization_scope_label` | `target.resource.attribute.labels` | Merged  
`modifiedPropertie_label` | `target.resource.attribute.labels` | Merged  
`modifiedProperty_name_label` | `target.resource.attribute.labels` | Merged  
`modifiedProperty_new_value_label` | `target.resource.attribute.labels` | Merged  
`modifiedProperty_old_value_label` | `target.resource.attribute.labels` | Merged  
`modified_properties_new_value_label` | `target.resource.attribute.labels` | Merged  
`newValue_label` | `target.resource.attribute.labels` | Merged  
`targetResourceType` | `target.resource.attribute.labels` | Mapped: `"Device", "User", "Directory", "Application", "Group", "ServicePrincipal", "Role"` ...  
`target_Name_label` | `target.resource.attribute.labels` | Merged  
`target_resource_display_name_label` | `target.resource.attribute.labels` | Merged  
`target_resource_id_label` | `target.resource.attribute.labels` | Merged  
`type_label` | `target.resource.attribute.labels` | Merged  
`role` | `target.resource.attribute.roles` | Merged  
`targetResourceType` | `target.resource.attribute.roles` | Mapped: `"Device", "User", "Directory", "Application", "Group", "ServicePrincipal", "Role"` ...  
`properties.resourceDisplayName` | `target.resource.name` | Directly mapped  
`resourceDisplayName` | `target.resource.name` | Directly mapped  
`temp_display_name` | `target.resource.name` | Directly mapped  
`id` | `target.resource.product_object_id` | Directly mapped  
`prop_resourceId` | `target.resource.product_object_id` | Directly mapped  
`properties.TargetObjectIds.0` | `target.resource.product_object_id` | Directly mapped  
`targetResourceType` | `target.resource.resource_subtype` | Directly mapped  
`activityDisplayName` | `target.resource.type` | Mapped values (38 total, e.g. `Add agreement` → `SETTING`, `"Delete agreement", "Hard delete...  
`category` | `target.resource.type` | Mapped values (18 total, e.g. `Agreement` → `SETTING`, `ApplicationManagement` → `SETTING`, ...  
`loggedByService` | `target.resource.type` | Mapped: `Core Directory` → `SETTING`  
`principal_ip_present` | `target.resource.type` | Mapped: `true` → `SETTING`  
`type` | `target.resource.type` | Mapped: `Device` → `DEVICE`  
`kv.value` | `target.url` | Directly mapped  
`user_attribute_labels` | `target.user.attribute.labels` | Merged  
`role` | `target.user.attribute.roles` | Merged  
`modifiedProperties.newValue` | `target.user.department` | Merged  
`targetResourceType` | `target.user.department` | Mapped: `"Device", "User", "Directory", "Application", "Group", "ServicePrincipal", "Role"` ...  
`activityDisplayName` | `target.user.email_addresses` | Mapped: `Add member to role outside of PIM (permanent)` → `target.userPrincipalName`  
`kv.value` | `target.user.email_addresses` | Merged  
`modifiedProperties.newValue` | `target.user.email_addresses` | Merged  
`targer_user_principal_name` | `target.user.email_addresses` | Mapped: `(^.*@.*$)` → `target.userPrincipalName`  
`target.userPrincipalName` | `target.user.email_addresses` | Merged  
`targetResourceType` | `target.user.email_addresses` | Mapped: `User` → `target.userPrincipalName`, `"Device", "User", "Directory", "Application", ...  
`target_email` | `target.user.email_addresses` | Merged  
`temp_display_name` | `target.user.email_addresses` | Mapped: `(^.*@.*$)` → `temp_display_name`  
`modifiedProperties.newValue` | `target.user.employee_id` | Directly mapped  
`modifiedProperties.newValue` | `target.user.first_name` | Directly mapped  
`modifiedProperties.newValue` | `target.user.last_name` | Directly mapped  
`modifiedProperties.newValue` | `target.user.office_address.name` | Directly mapped  
`kv.value` | `target.user.phone_numbers` | Merged  
`modifiedProperties.newValue` | `target.user.phone_numbers` | Merged  
`mp.newValue` | `target.user.phone_numbers` | Merged  
`targetResourceType` | `target.user.phone_numbers` | Mapped: `"Device", "User", "Directory", "Application", "Group", "ServicePrincipal", "Role"` ...  
`modifiedProperties.newValue` | `target.user.product_object_id` | Directly mapped  
`properties.targetIdentity.Id` | `target.user.product_object_id` | Directly mapped  
`target.id` | `target.user.product_object_id` | Directly mapped  
`userId` | `target.user.product_object_id` | Directly mapped  
`modifiedProperties.newValue` | `target.user.title` | Directly mapped  
`TargetResource_displayName` | `target.user.user_display_name` | Directly mapped  
`identity` | `target.user.user_display_name` | Directly mapped  
`modifiedProperties.newValue` | `target.user.user_display_name` | Directly mapped  
`mp.newValue` | `target.user.user_display_name` | Directly mapped  
`properties.TargetDisplayNames.0` | `target.user.user_display_name` | Directly mapped  
`properties.targetIdentity.Name` | `target.user.user_display_name` | Directly mapped  
`properties.userDisplayName` | `target.user.user_display_name` | Directly mapped  
`target.displayName` | `target.user.user_display_name` | Directly mapped  
`target_user_name` | `target.user.user_display_name` | Directly mapped  
`userPrincipalName` | `target.user.user_display_name` | Directly mapped  
`TargetResource_id` | `target.user.userid` | Directly mapped  
`identity` | `target.user.userid` | Directly mapped  
`kv.value` | `target.user.userid` | Directly mapped  
`modifiedProperties.newValue` | `target.user.userid` | Directly mapped  
`prop_alternateSignInName` | `target.user.userid` | Directly mapped  
`prop_signInIdentifier` | `target.user.userid` | Directly mapped  
`prop_userPrincipalName` | `target.user.userid` | Directly mapped  
`userPrincipalName` | `target.user.userid` | Directly mapped  
`DATA:target_domain` | `target.userPrincipalName` | Directly mapped  
`DATA:tgt_user_principal_name` | `target.userPrincipalName` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `SSO`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.product_name` | Constant: `Azure AD Directory Audit`  
N/A | `metadata.vendor_name` | Constant: `Microsoft`  
N/A | `network.http.parsed_user_agent` | Constant: `parseduseragent`  
N/A | `principal.resource.type` | Constant: `AUDIT_LOG`  
N/A | `security_result.priority` | Constant: `MEDIUM_PRIORITY`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `security_result.summary` | Constant: `Successful login occurred`  
N/A | `target.resource.type` | Constant: `DEVICE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
