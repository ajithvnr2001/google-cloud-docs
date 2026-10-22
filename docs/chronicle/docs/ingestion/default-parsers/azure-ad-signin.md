---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-signin/
title: Collect Microsoft Entra ID Sign-in (formerly Azure Active Directory) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:10.580363+00:00
---

# Collect Microsoft Entra ID Sign-in (formerly Azure Active Directory) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-signin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Entra ID Sign-in (formerly Azure Active Directory) logs

**Parser Version:** 8.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how to collect Microsoft Entra ID Sign-in (formerly known as Azure Active Directory) logs by setting up a Google Security Operations feed using Microsoft Azure Blob Storage V2.

Microsoft Entra ID is a cloud-based identity and access management service. Sign-in logs capture authentication activities across your organization, including interactive user sign-ins, non-interactive sign-ins, service principal sign-ins, and managed identity sign-ins. These logs are critical for monitoring access patterns, detecting suspicious authentication attempts, and investigating security incidents.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the Azure portal with permissions to: 
    * Create Storage Accounts
    * Configure Diagnostic Settings for Microsoft Entra ID
    * Manage access keys
  * Security Administrator role or higher in Microsoft Entra ID (required to configure Diagnostic Settings)

**Note:** If you restrict access to your Azure resources using an Azure Storage firewall, you must add the IP ranges used by Storage Transfer Service (STS) workers to your list of allowed IPs. See [IP Allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip_allowlisting).



## Configure Azure Storage Account

### Create Storage Account

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Storage account name** | Enter a unique name (for example, `secops-entraid-signin`)  
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
     * **Storage account name** : Your storage account name (for example, `secops-entraid-signin`)
     * **Key 1** or **Key 2** : The shared access key (a 512-bit random string in base-64 encoding)



### Get Blob Service endpoint

  1. In the same Storage Account, select **Endpoints** from the left navigation.
  2. Copy and save the **Blob service** endpoint URL. 
     * Example: `https://secops-entraid-signin.blob.core.windows.net/`



## Configure Microsoft Entra ID Diagnostic Settings

To export Entra ID sign-in logs to the storage account:

  1. In the **Azure portal** , search for **Microsoft Entra ID**.
  2. In the left navigation, go to **Monitoring & health > Diagnostic settings**.
  3. Click **\+ Add diagnostic setting**.
  4. Provide the following configuration details: 
     * **Diagnostic setting name** : Enter a descriptive name (for example, `signin-logs-to-secops`).
     * In the **Logs** section, select the following sign-in log categories: 
       * **SignInLogs** : Interactive user sign-ins
       * **NonInteractiveUserSignInLogs** : Non-interactive user sign-ins
       * **ServicePrincipalSignInLogs** : Service principal and application sign-ins
       * **ManagedIdentitySignInLogs** : Managed identity sign-ins
       * **ADFSSignInLogs** : Sign-in activity for Active Directory Federated Services (AD FS) applications (select only if AD FS is in use)
     * In the **Destination details** section, select the **Archive to a storage account** checkbox.
     * **Subscription** : Select the subscription containing your storage account.
     * **Storage account** : Select the storage account you created earlier (for example, `secops-entraid-signin`).
  5. Click **Save**.

**Note:** It may take up to 72 hours for Entra ID sign-in logs to start appearing in the storage account. Each selected log category will create a separate container with the naming pattern `insights-logs-{category-name}`.



## Configure a feed in Google SecOps to ingest Microsoft Entra ID Sign-in logs

You must create a separate feed for each sign-in log container. The following table shows the mapping between containers and log categories:

Container Name | Log Category  
---|---  
`insights-logs-signinlogs` | Interactive Sign-in Logs  
`insights-logs-noninteractiveusersigninlogs` | Non-interactive Sign-in Logs  
`insights-logs-serviceprincipalsigninlogs` | Service Principal Sign-in Logs  
`insights-logs-managedidentitysigninlogs` | Managed Identity Sign-in Logs  
`insights-logs-adfssigninlogs` | AD FS Sign-in Logs  
  
### Create feed for Interactive Sign-in Logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Entra ID Interactive Sign-in Logs`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Azure AD Sign-In** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the container path:
    
    https://secops-entraid-signin.blob.core.windows.net/insights-logs-signinlogs/
    

Replace `secops-entraid-signin` with your Azure storage account name.

**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers.
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * From the authentication drop-down (defaults to **Access/Shared key**), select the method you want to use and provide the corresponding credential. The exact request schema for each method is documented in the [Feed Management API reference](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#azure_blob_store_v2): 
       * **Access/Shared key** : In the **Key** field, paste a storage account access key (**Key 1** or **Key 2**) captured earlier.
       * **SAS token** : In the **Token** field, paste a shared access signature (SAS) token issued for the container.
       * **Azure V2 Workload Identity Federation** : Enter the Microsoft Entra application **Client ID** and **Tenant ID**. Copy the read-only **Subject ID** that the feed displays and configure it as the subject of a [Microsoft Entra federated credential](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) on the Azure application; then grant that application the **Storage Blob Data Reader** role on the storage account.
**Note:** The **Chronicle service account** shown on the right side of the feed is read-only. It identifies the Google SecOps identity used by the **Access/Shared key** and **SAS token** paths.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




### Create feeds for other sign-in log categories

Repeat the preceding feed creation steps for each additional sign-in log container, using the same settings but with the appropriate Azure URI:

**For Non-interactive Sign-in Logs:**

  * **Feed name** : `Entra ID Non-interactive Sign-in Logs`
  * **Log type** : `Azure AD Sign-In`
  * **Azure URI** : `https://secops-entraid-signin.blob.core.windows.net/insights-logs-noninteractiveusersigninlogs/`



**For Service Principal Sign-in Logs:**

  * **Feed name** : `Entra ID Service Principal Sign-in Logs`
  * **Log type** : `Azure AD Sign-In`
  * **Azure URI** : `https://secops-entraid-signin.blob.core.windows.net/insights-logs-serviceprincipalsigninlogs/`



**For Managed Identity Sign-in Logs:**

  * **Feed name** : `Entra ID Managed Identity Sign-in Logs`
  * **Log type** : `Azure AD Sign-In`
  * **Azure URI** : `https://secops-entraid-signin.blob.core.windows.net/insights-logs-managedidentitysigninlogs/`



**For AD FS Sign-in Logs:**

  * **Feed name** : `Entra ID AD FS Sign-in Logs`
  * **Log type** : `Azure AD Sign-In`
  * **Azure URI** : `https://secops-entraid-signin.blob.core.windows.net/insights-logs-adfssigninlogs/`

**Note:** Only create feeds for the log categories you selected in the Entra ID diagnostic settings. If you did not enable a specific log category, skip creating the corresponding feed.



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
`AuthenticationContextClassReferences_label` | `additional.fields` | Merged  
`AuthenticationProtocol_label` | `additional.fields` | Merged  
`ClientCredentialType_label` | `additional.fields` | Merged  
`TimeGenerated_label` | `additional.fields` | Merged  
`additional_AuthenticationProtocol` | `additional.fields` | Merged  
`additional_AuthenticationRequirement` | `additional.fields` | Merged  
`additional_DurationMs` | `additional.fields` | Merged  
`additional_ResultSignature` | `additional.fields` | Merged  
`additional_TokenIssuerType` | `additional.fields` | Merged  
`additional_resultSignature` | `additional.fields` | Merged  
`additional_resultType` | `additional.fields` | Merged  
`additional_tokenIssuerType` | `additional.fields` | Merged  
`agentSubjectType_label` | `additional.fields` | Merged  
`agentType_label` | `additional.fields` | Merged  
`authconclassref_detail_label` | `additional.fields` | Merged  
`authconclassref_id_label` | `additional.fields` | Merged  
`authenticationDetail_label` | `additional.fields` | Merged  
`authenticationRequirement_label` | `additional.fields` | Merged  
`authentication_Detail_label` | `additional.fields` | Merged  
`clientCredentialType_fields` | `additional.fields` | Merged  
`conditionalAccessAudiences_label` | `additional.fields` | Merged  
`conditionalAccessStatus_fields` | `additional.fields` | Merged  
`conditionalAccessStatus_label` | `additional.fields` | Merged  
`crossTenantAccessType_fields` | `additional.fields` | Merged  
`field_` | `additional.fields` | Merged  
`incomingTokenType_fields` | `additional.fields` | Merged  
`incoming_token_type_label` | `additional.fields` | Merged  
`originalRequestId_label` | `additional.fields` | Merged  
`originalTransferMethod_fields` | `additional.fields` | Merged  
`originalTransferMethod_label` | `additional.fields` | Merged  
`processingTimeInMilliseconds_label` | `additional.fields` | Merged  
`prp_networkType_additional_fields` | `additional.fields` | Merged  
`prp_network_names_additional_fields` | `additional.fields` | Merged  
`resource_label` | `additional.fields` | Merged  
`riskDetail_fields` | `additional.fields` | Merged  
`riskEventTypeV2_label` | `additional.fields` | Merged  
`riskEventType_label` | `additional.fields` | Merged  
`riskLevelAggregated_fields` | `additional.fields` | Merged  
`riskLevelDuringSignIn_fields` | `additional.fields` | Merged  
`riskState_fields` | `additional.fields` | Merged  
`risk_event_types_label` | `additional.fields` | Merged  
`risk_event_types_v2_label` | `additional.fields` | Merged  
`signInEventTypes_label` | `additional.fields` | Merged  
`signInTokenProtectionStatus_fields` | `additional.fields` | Merged  
`sign_In_Token_Protection_Status_fields` | `additional.fields` | Merged  
`status_additional_details_label` | `additional.fields` | Merged  
`has_principal` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`has_target_user` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`Category` | `metadata.description` | Directly mapped  
`CreatedDateTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`createdDateTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`properties.createdDateTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`when` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `USER_LOGIN`, `true` → `STATUS_UPDATE`  
`has_target_user` | `metadata.event_type` | Mapped: `true` → `USER_LOGIN`  
`TenantId` | `metadata.product_deployment_id` | Directly mapped  
`tenantId` | `metadata.product_deployment_id` | Directly mapped  
`operationName` | `metadata.product_event_type` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`prop_id` | `metadata.product_log_id` | Directly mapped  
`operationVersion` | `metadata.product_version` | Directly mapped  
`UserAgent` | `network.http.parsed_user_agent` | Directly mapped  
`properties.userAgent` | `network.http.parsed_user_agent` | Renamed/mapped  
`Status_errorCode` | `network.http.response_code` | Directly mapped  
`status.errorCode` | `network.http.response_code` | Directly mapped  
`Browser` | `network.http.user_agent` | Directly mapped  
`UserAgent` | `network.http.user_agent` | Directly mapped  
`properties.userAgent` | `network.http.user_agent` | Directly mapped  
`CorrelationId` | `network.session_id` | Directly mapped  
`properties.sessionId` | `network.session_id` | Directly mapped  
`appDisplayName` | `principal.application` | Directly mapped  
`hardware` | `principal.asset.hardware` | Merged  
`callerIpAddress` | `principal.asset.ip` | Merged  
`ipAddress` | `principal.asset.ip` | Merged  
`principal_ip` | `principal.asset.ip` | Merged  
`callerIpAddress` | `principal.ip` | Merged  
`ipAddress` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`City` | `principal.location.city` | Directly mapped  
`city` | `principal.location.city` | Directly mapped  
`city_value` | `principal.location.city` | Directly mapped  
`CountryOrRegion` | `principal.location.country_or_region` | Directly mapped  
`countryOrRegion` | `principal.location.country_or_region` | Directly mapped  
`country_or_region_value` | `principal.location.country_or_region` | Directly mapped  
`geoCoordinates_latitude` | `principal.location.region_coordinates.latitude` | Directly mapped  
`geo_latitude` | `principal.location.region_coordinates.latitude` | Directly mapped  
`geo_latitude_value` | `principal.location.region_coordinates.latitude` | Directly mapped  
`geoCoordinates_longitude` | `principal.location.region_coordinates.longitude` | Directly mapped  
`geo_longitude` | `principal.location.region_coordinates.longitude` | Directly mapped  
`geo_longitude_value` | `principal.location.region_coordinates.longitude` | Directly mapped  
`State` | `principal.location.state` | Directly mapped  
`state` | `principal.location.state` | Directly mapped  
`state_value` | `principal.location.state` | Directly mapped  
`OperatingSystem` | `principal.platform` | Mapped: `Win` → `WINDOWS`, `Mac` → `MAC`, `Lin` → `LINUX`  
`DeviceDetail_operatingSystem` | `principal.platform_version` | Directly mapped  
`OperatingSystem` | `principal.platform_version` | Directly mapped  
`ServicePrincipalId_label` | `principal.resource.attribute.labels` | Merged  
`resourceServicePrincipalId_label` | `principal.resource.attribute.labels` | Merged  
`userPrincipalName` | `principal.user.email_addresses` | Merged  
`userDisplayName` | `principal.user.user_display_name` | Directly mapped  
`userId` | `principal.user.userid` | Directly mapped  
`auth_detail_sec` | `security_result` | Merged  
`auth_sec_res` | `security_result` | Merged  
`sec_res` | `security_result` | Merged  
`sr_result` | `security_result` | Merged  
`OperationName` | `security_result.action` | Mapped: `Sign-in activity` → `action`  
`ResultType` | `security_result.action` | Mapped: `0` → `action`  
`action` | `security_result.action` | Merged  
`security_action` | `security_result.action` | Merged  
`Category` | `security_result.category` | Merged  
`OperationName` | `security_result.category` | Mapped: `Sign-in activity` → `Category`  
`category` | `security_result.category_details` | Merged  
`AADTenantId_label` | `security_result.detection_fields` | Merged  
`AppOwnerTenantId_label` | `security_result.detection_fields` | Merged  
`AutonomousSystemNumber_label` | `security_result.detection_fields` | Merged  
`CorrelationId_label` | `security_result.detection_fields` | Merged  
`CrossTenantAccessType_label` | `security_result.detection_fields` | Merged  
`DeviceDetail_browser_label` | `security_result.detection_fields` | Merged  
`IsTenantRestricted_label` | `security_result.detection_fields` | Merged  
`IsThroughGlobalSecureAccess_label` | `security_result.detection_fields` | Merged  
`TokenIssuerType_label` | `security_result.detection_fields` | Merged  
`Type_label` | `security_result.detection_fields` | Merged  
`UniqueTokenIdentifier_label` | `security_result.detection_fields` | Merged  
`_Internal_WorkspaceResourceId_label` | `security_result.detection_fields` | Merged  
`_TimeReceived_label` | `security_result.detection_fields` | Merged  
`alternateSignInName_label` | `security_result.detection_fields` | Merged  
`appId_label` | `security_result.detection_fields` | Merged  
`appid_label` | `security_result.detection_fields` | Merged  
`browser_label` | `security_result.detection_fields` | Merged  
`clientAppUsed_label` | `security_result.detection_fields` | Merged  
`conditionalAccessStatus_label` | `security_result.detection_fields` | Merged  
`correlationId_field` | `security_result.detection_fields` | Merged  
`cribl_source_label` | `security_result.detection_fields` | Merged  
`cribl_topic_name_label` | `security_result.detection_fields` | Merged  
`detail_label` | `security_result.detection_fields` | Merged  
`deviceId_label` | `security_result.detection_fields` | Merged  
`deviceName_label` | `security_result.detection_fields` | Merged  
`displayName_label` | `security_result.detection_fields` | Merged  
`flaggedForReview_label` | `security_result.detection_fields` | Merged  
`home_id_label` | `security_result.detection_fields` | Merged  
`home_tenant_name_label` | `security_result.detection_fields` | Merged  
`id_label` | `security_result.detection_fields` | Merged  
`isCompliant_label` | `security_result.detection_fields` | Merged  
`isInteractive_label` | `security_result.detection_fields` | Merged  
`isManaged_label` | `security_result.detection_fields` | Merged  
`item_id_label` | `security_result.detection_fields` | Merged  
`message` | `security_result.detection_fields` | Mapped: `cribl_pipe` → `cribl_topic_name_label`, `cribl_pipe` → `cribl_source_label`  
`method_label` | `security_result.detection_fields` | Merged  
`networkNames_label` | `security_result.detection_fields` | Merged  
`networkType_label` | `security_result.detection_fields` | Merged  
`network_Names_label` | `security_result.detection_fields` | Merged  
`network_Type_label` | `security_result.detection_fields` | Merged  
`network_type_label` | `security_result.detection_fields` | Merged  
`operationVersion_label` | `security_result.detection_fields` | Merged  
`properties_resourceDisplayName_label` | `security_result.detection_fields` | Merged  
`properties_resourceId_label` | `security_result.detection_fields` | Merged  
`requirement_provider_label` | `security_result.detection_fields` | Merged  
`resourceOwnerTenantId_label` | `security_result.detection_fields` | Merged  
`resourceTenantId_label` | `security_result.detection_fields` | Merged  
`resource_group_field` | `security_result.detection_fields` | Merged  
`riskDetail_label` | `security_result.detection_fields` | Merged  
`riskLevelAggregated_label` | `security_result.detection_fields` | Merged  
`riskLevelDuringSignIn_label` | `security_result.detection_fields` | Merged  
`riskState_label` | `security_result.detection_fields` | Merged  
`sessionId_label` | `security_result.detection_fields` | Merged  
`sessionLifetimePolicies_label` | `security_result.detection_fields` | Merged  
`siginsess_status_code_label` | `security_result.detection_fields` | Merged  
`signInIdentifier_label` | `security_result.detection_fields` | Merged  
`source_system_label` | `security_result.detection_fields` | Merged  
`step_date_label` | `security_result.detection_fields` | Merged  
`step_detail_label` | `security_result.detection_fields` | Merged  
`step_requirement_label` | `security_result.detection_fields` | Merged  
`tokenIssuerName_label` | `security_result.detection_fields` | Merged  
`token_protection_status_details_label` | `security_result.detection_fields` | Merged  
`trustType_label` | `security_result.detection_fields` | Merged  
`RiskLevelDuringSignIn` | `security_result.priority` | Mapped: `medium` → `MEDIUM_PRIORITY`  
`ResultType` | `security_result.rule_id` | Directly mapped  
`OperationName` | `security_result.severity` | Mapped: `Sign-in activity` → `ERROR`  
`level` | `security_result.severity` | Directly mapped  
`level` | `security_result.severity_details` | Directly mapped  
`OperationName` | `security_result.summary` | Mapped: `Sign-in activity` → `Successful login occurred`, `Sign-in activity` → `Failed login...  
`ResultType` | `security_result.summary` | Mapped: `0` → `Successful login occurred`  
`Status_failureReason` | `security_result.summary` | Directly mapped  
`status.failureReason` | `security_result.summary` | Directly mapped  
`AppDisplayName` | `target.application` | Directly mapped  
`properties.appDisplayName` | `target.application` | Directly mapped  
`resourceDisplayName` | `target.application` | Directly mapped  
`AppId_label` | `target.resource.attribute.labels` | Merged  
`identity_label` | `target.resource.attribute.labels` | Merged  
`resourceIdentity_label` | `target.resource.attribute.labels` | Merged  
`resourceId` | `target.resource.name` | Directly mapped  
`ResourceId` | `target.resource.product_object_id` | Directly mapped  
`target_role_name` | `target.user.attribute.roles` | Merged  
`UserPrincipalName` | `target.user.email_addresses` | Mapped: `^.+@.+$` → `UserPrincipalName`  
`properties.userPrincipalName` | `target.user.email_addresses` | Merged  
`UserId` | `target.user.product_object_id` | Directly mapped  
`Identity` | `target.user.user_display_name` | Directly mapped  
`properties.userDisplayName` | `target.user.user_display_name` | Directly mapped  
`UserPrincipalName` | `target.user.userid` | Directly mapped  
`properties.userId` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `network.http.parsed_user_agent` | Constant: `parseduseragent`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `security_result.priority` | Constant: `MEDIUM_PRIORITY`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `security_result.summary` | Constant: `Successful login occurred`  
`properties.userId` | `event.idm.read_only_udm.target.user.product_object_id` | Mapped from changelog  
`properties.appDisplayName` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`resourceDisplayName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`clientAppUsed` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`deviceDetail.deviceId` | `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`deviceDetail.isCompliant` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`deviceDetail.isManaged` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`deviceDetail.trustType` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.deviceDetail.browser` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.deviceDetail.displayName` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`properties.appId` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`properties.userPrincipalName` | `event.idm.read_only_udm.target.user.email_address` | Mapped from changelog  
`properties.userPrincipalName` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`properties.location.countryOrRegion` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`ip_address_from_resource_provider` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`properties.redirectUrl` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`properties.homeTenantName` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`properties.deviceDetail.operatingSystem` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`properties.originalTransferMethod` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`properties.authenticationProtocol` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`properties.federatedCredentialId` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.servicePrincipalCredentialKeyId` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.servicePrincipalCredentialThumbprint` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.sourceAppClientId` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.appServicePrincipalId` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.signInIdentifier` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.alternateSignInName` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.riskLevelDuringSignIn` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.riskEventTypes` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.riskEventTypes_v2` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.authenticationRequirementPolicies` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.sessionLifetimePolicies` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`properties.authenticationStrengths` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`TimeGenerated` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`authenticationRequirement` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RiskEventTypes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Status.errorCode` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`Status.failureReason` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`cribl.cribl_data.cribl_enrichment.topic_name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`cribl.cribl_data.cribl_enrichment.cribl_source` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`AlternateSignInName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`SignInIdentifier` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`DeviceDetail.deviceId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`DeviceDetail.trustType` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`TokenIssuerName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`AADTenantId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`authdetail.authenticationMethod` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`authdetail.authenticationMethodDetail` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`authdetail.authenticationStepDateTime` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`authdetail.authenticationStepRequirement` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`authdetail.authenticationStepResultDetail` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`networklocation.networkType` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`networklocation.networkNames` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`authdetail.succeeded` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`authdetail.succeeded` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`Agent.agentType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AuthenticationContextClassReferences` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AuthenticationProtocol` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AuthenticationRequirement` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ClientCredentialType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`TimeGenerated` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AuthenticationProcessingDetails` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`IsInteractive` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`DeviceDetail.displayName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`OperationVersion` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`AppOwnerTenantId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`CrossTenantAccessType` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`IsTenantRestricted` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`IsThroughGlobalSecureAccess` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`_TimeReceived` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`AuthenticationRequirementPolicies` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`CreatedDateTime` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`apc.displayName` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`apc.id` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`apc.Result` | `event.idm.read_only_udm.security_result.rule_labels` | Mapped from changelog  
`apc.conditionsSatisfied` | `event.idm.read_only_udm.security_result.rule_labels` | Mapped from changelog  
`apc.conditionsNotSatisfied` | `event.idm.read_only_udm.security_result.rule_labels` | Mapped from changelog  
`apc.enforcedGrantControls` | `event.idm.read_only_udm.security_result.rule_labels` | Mapped from changelog  
`apc.enforcedSessionControls` | `event.idm.read_only_udm.security_result.rule_labels` | Mapped from changelog  
`SourceSystem` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`SessionLifetimePolicies` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`SessionId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ResourceTenantId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ResourceOwnerTenantId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`TokenProtectionStatusDetails.signInSessionStatusCode` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`TokenProtectionStatusDetails.signInSessionStatus` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`DeviceDetail.browser` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`DeviceDetail.operatingSystem` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ResourceServicePrincipalId` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`ResourceIdentity` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`Resource` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ProcessingTimeInMilliseconds` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`OriginalTransferMethod` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`OriginalRequestId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Status.additionalDetails` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RiskEventTypes_V2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`IncomingTokenType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LocationDetails.city` | `event.idm.read_only_udm.principal.location.city` | Mapped from changelog  
`LocationDetails.countryOrRegion` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`LocationDetails.state` | `event.idm.read_only_udm.principal.location.state` | Mapped from changelog  
`LocationDetails.geoCoordinates.latitude` | `event.idm.read_only_udm.principal.location.region_coordinates.latitude` | Mapped from changelog  
`LocationDetails.geoCoordinates.longitude` | `event.idm.read_only_udm.principal.location.region_coordinates.longitude` | Mapped from changelog  
`deviceDetail.operatingSystem` | `principal.platform` | Mapped from changelog  
`appId", "clientAppUsed", "conditionalAccessStatus", "deviceDetail.deviceId", "deviceDetail.deviceName", "deviceDetail.browser", "deviceDetail.isCompliant", "deviceDetail.isManaged", and "deviceDetail.trustType` | `security_result.detection_fields` | Mapped from changelog  
`location.countryOrRegion` | `principal.location.country_or_region` | Mapped from changelog  
`location.geoCoordinates.latitude` | `principal.location.region_coordinates.latitude` | Mapped from changelog  
`location.geoCoordinates.longitude` | `principal.location.region_coordinates.longitude` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-signin-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
