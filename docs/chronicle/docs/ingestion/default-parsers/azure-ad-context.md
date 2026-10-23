---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-context/
title: Collect Microsoft Entra ID Organizational Context data (formerly Azure Active Directory) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:40.514131+00:00
---

# Collect Microsoft Entra ID Organizational Context data (formerly Azure Active Directory) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Entra ID Organizational Context data (formerly Azure Active Directory) logs

**Parser Version:** 12.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Microsoft Entra ID (formerly Azure Active Directory) organizational context data by setting up a Google Security Operations feed using the Third Party API.

Microsoft Entra ID Organizational Context provides directory information such as users, groups, and devices from your Microsoft Entra ID tenant. This is not event or log data - it is a periodic snapshot of directory state that enriches other log types in Google SecOps with identity context.

**Note:** An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `AZURE_AD_CONTEXT` ingestion label.**Note:** Because this data type retrieves directory snapshots using the Microsoft Graph API (not streaming events), Azure Event Hub and Diagnostic Settings are not applicable for this log type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the **Microsoft Azure** portal
  * One of the following roles for granting administrator consent: 
    * **Global Administrator** \- can grant consent for any permission, for any API
    * **Privileged Role Administrator** \- can grant consent for any permission, for any API

**Caution:** Google SecOps requires allowlisting for log types that ingest from third-party APIs. See Configure IP allowlisting.

## Configure IP allowlisting

You should add the Google SecOps IP ranges in your Microsoft Azure network settings or Conditional Access policies before creating your feed. This matters where the data source enforces IP-based restrictions. If the feed returns a 403 error, verify that allowlisting is enabled there. To restrict access by a narrower range, open a support ticket.

**Note:** The published list is the all-Google `goog.json`, not a Google SecOps egress list and Google SecOps cannot guarantee that a feed originates from a given region.

For more information, see [IP Allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip-allow-lists).

### Get Google SecOps IP ranges

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Note the IP ranges displayed in the feed creation interface.
  4. Alternatively, retrieve IP ranges programmatically using the [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api).



### Configure conditional access for workload identities (if required)

If your organization uses conditional access policies that restrict access by location do the following:

  1. In the **Microsoft Entra admin center** , go to **Protection > Conditional Access > Named locations**.
  2. Click **\+ New location**.
  3. Provide the following configuration details: 
     * **Name** : Enter `Google SecOps IP Ranges`.
     * **Mark as trusted location** : Optional, based on your security policy.
     * **IP ranges** : Add each Google SecOps IP range in CIDR notation.
  4. Click **Create**.
  5. Go to **Conditional Access > Policies**.
  6. For any policies that apply to workload identities, configure an exclusion for the `Google SecOps IP Ranges` named location or the specific service principal.



## Configure Microsoft Entra app registration

### Create app registration

  1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) or [Azure portal](https://portal.azure.com/).
  2. Go to **Identity > Applications > App registrations**.
  3. Click **New registration**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Entra ID Context Integration`).
     * **Supported account types** : Select **Accounts in this organizational directory only (Single tenant)**.
     * **Redirect URI** : Leave blank (not required for service principal authentication).
  5. Click **Register**.
  6. After registration, copy and save the following values: 
     * **Application (client) ID**
     * **Directory (tenant) ID**



### Configure API permissions

The feed reads the user directory through the Microsoft Graph `List users` endpoint, with each user's manager expanded. Grant the application permissions that match the feed options you enable.

  1. In the app registration, go to **API permissions**.
  2. Click **Add a permission**.
  3. Select **Microsoft Graph > Application permissions**.
  4. Search for and select the following permissions: 
     * **User.Read.All** \- Required. Reads the user profiles and the manager relationship that the feed ingests.
     * **Group.Read.All** \- Only if you set **Retrieve groups** to **True** in the feed. Reads the groups returned for each user's membership.
     * **Device.Read.All** \- Only if you set **Retrieve devices** to **True** in the feed. Reads the devices associated with each user.
  5. Click **Add permissions**.
  6. Click **Grant admin consent for Your Organization**.
  7. Verify that the **Status** column shows **Granted for Your Organization** for all permissions.

**Note:** If the **Grant admin consent** button is disabled, make sure you have either the `Global Administrator` or `Privileged Role Administrator` role.Permission | Type | When required  
---|---|---  
**User.Read.All** | Application | Always  
**Group.Read.All** | Application | **Retrieve groups** is **True**  
**Device.Read.All** | Application | **Retrieve devices** is **True**  
**Note:** **Directory.Read.All** is not required. It's a broader permission that covers all three of these permissions. You can grant it instead of the individual permissions if your organization prefers a single permission. However, the feed works with the least-privileged set listed here.**Note:** The current `AZURE_AD_CONTEXT` parser maps user and manager attributes to UDM. Group and device data retrieved with the **Retrieve groups** and **Retrieve devices** options is not mapped to UDM fields.



### Create a client secret

  1. In the app registration, go to **Certificates & secrets**.
  2. Click **New client secret**.
  3. Provide the following configuration details:

     * **Description** : Enter a descriptive name (for example, `Google SecOps Feed`).
     * **Expires** : Select an expiration period.
**Note:** Microsoft recommends setting an expiration value of less than 12 months. The maximum allowed is 24 months.
  4. Click **Add**.

  5. Copy the client secret **Value** immediately.

**Important:** The secret value is displayed only once and cannot be retrieved after leaving this page. If you lose the value, you must create a new client secret.



## Configure a feed in Google SecOps to ingest Microsoft Entra ID organizational context data

To configure the feed, do the following:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Azure AD Organizational Context`).
  5. Select **Third party API** as the **Source type**.
  6. Select **Azure AD Organizational Context** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters as follows:

     * **OAuth Client ID** : Enter the **Application (client) ID** from the app registration.
     * **OAuth Client Secret** : Enter the **client secret value** you copied earlier.
     * **Tenant ID** : Enter the **Directory (tenant) ID** from the app registration in UUID format (for example, `0fc279f9-fe30-41be-97d3-abe1d7681418`).
     * **Retrieve devices** : Select whether to retrieve device information within user context. Set to **True** to include device data.
     * **Retrieve groups** : Select whether to retrieve group membership information within user context. Set to **True** to include group data.
     * **API Full Path** : Microsoft Graph REST API endpoint URL:
           
           graph.microsoft.com/beta
           

**Note:** Don't include the `https://` prefix. The feed adds the protocol automatically. This log type uses the Microsoft Graph **beta** endpoint, not v1.0.
     * **API Authentication Endpoint** : Microsoft Entra ID Authentication Endpoint:
           
           login.microsoftonline.com
           

**Note:** Don't include the `https://` prefix or the `/oauth2/v2.0/token` path. The feed constructs the full authentication URL automatically using your Tenant ID.

**Advanced Options:**

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.


**Note:** After creating the feed, context data will be retrieved periodically. It may take up to 24 hours for the initial directory snapshot to appear in Google SecOps.

## Regional endpoints

For Microsoft Entra ID deployments in sovereign clouds, use the appropriate regional endpoints:

Cloud Environment | API Full Path | API Authentication Endpoint  
---|---|---  
**Global** | `graph.microsoft.com/beta` | `login.microsoftonline.com`  
**US Government L4** | `graph.microsoft.us/beta` | `login.microsoftonline.us`  
**US Government L5 (DOD)** | `dod-graph.microsoft.us/beta` | `login.microsoftonline.us`  
**China (21Vianet)** | `microsoftgraph.chinacloudapi.cn/beta` | `login.chinacloudapi.cn`  
**Note:** Google SecOps documents the API hostname only as an optional override with a commercial default, and doesn't document support for sovereign-cloud hosts. For the Azure Blob Storage and Event Hub feed types it states that sovereign clouds are not supported. Confirm with Support before relying on a sovereign endpoint here.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`extension_wfc_AccountType` | `entity.labels.value` | Directly mapped  
`extension_wfc_AccountingUnitName` | `entity.labels.value` | Directly mapped  
`extension_wfc_execDescription` | `entity.labels.value` | Directly mapped  
`extension_wfc_groupDescription` | `entity.labels.value` | Directly mapped  
`extension_wfc_orgDescription` | `entity.labels.value` | Directly mapped  
`createdDateTime` | `entity.user.attribute.creation_time` | Parsed as `RFC3339`  
`sign_in_type` | `entity.user.attribute.labels.key` | Directly mapped  
`assignedLicense.skuId` | `entity.user.attribute.labels.value` | Directly mapped  
`employeeType` | `entity.user.attribute.labels.value` | Directly mapped  
`empmanager-src.usageLocation` | `entity.user.attribute.labels.value` | Directly mapped  
`externalUserState` | `entity.user.attribute.labels.value` | Directly mapped  
`gopher-manager.onPremisesImmutableId` | `entity.user.attribute.labels.value` | Directly mapped  
`mailNickname` | `entity.user.attribute.labels.value` | Directly mapped  
`onPremisesDistinguishedName` | `entity.user.attribute.labels.value` | Directly mapped  
`onPremisesDomainName` | `entity.user.attribute.labels.value` | Directly mapped  
`onPremisesExtensionAttributes.extensionAttribute4` | `entity.user.attribute.labels.value` | Directly mapped  
`onPremisesImmutableId` | `entity.user.attribute.labels.value` | Directly mapped  
`onPremisesSamAccountName` | `entity.user.attribute.labels.value` | Directly mapped  
`refreshTokensValidFromDateTime` | `entity.user.attribute.labels.value` | Directly mapped  
`token_date_time` | `entity.user.attribute.labels.value` | Directly mapped  
`userPrincipalName` | `entity.user.attribute.labels.value` | Directly mapped  
`user_ou_data` | `entity.user.attribute.labels.value` | Directly mapped  
`userType` | `entity.user.attribute.roles.name` | Directly mapped  
`user_ou_data` | `entity.user.attribute.roles.type` | Mapped: `Admin` → `ADMINISTRATOR`, `Service Accounts` → `SERVICE_ACCOUNT`  
`department` | `entity.user.department` | Merged  
`mail` | `entity.user.email_addresses` | Merged  
`proxyAddress` | `entity.user.email_addresses` | Mapped: `smtp/SMTP` → `proxyAddress`  
`userPrincipalName` | `entity.user.email_addresses` | Merged  
`employeeId` | `entity.user.employee_id` | Renamed/mapped  
`extension_employeeNumber` | `entity.user.employee_id` | Renamed/mapped  
`onPremisesDomainName` | `entity.user.group_identifiers` | Merged  
`proxyAddress` | `entity.user.group_identifiers` | Merged  
`sign_in_type_manager` | `entity.user.managers.attribute.labels.key` | Directly mapped  
`temp` | `entity.user.managers.attribute.labels.key` | Mapped: `true` → `manager accountEnabled`  
`empmanager-src.sbuxCompanyCode` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxCostCenter` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxDirectorySync` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxEmployeeStatus` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxEmployeeType` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxFullName` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxFullNameAKA` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxFullNameAKAAlt` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxFullNameAlt` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxGivenNameAlt` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxGlobalID` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxJobNumber` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxKnownAs` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxKnownAsAlt` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxLocalMarket` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxLocalMarketEmployeeID` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxManagerImmutableID` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxManagerNumber` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxOnTLA` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxOrgAreaID` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxOrgDistrictID` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxOrgDivisionID` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxOrgRegionID` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxOrgShortName` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxOrgStoreID` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxOrgType` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxOrgUnit` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxSnAlt` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.sbuxSourceSystem` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`empmanager-src.userPrincipalName` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`manager_ou_data` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`temp` | `entity.user.managers.attribute.labels.value` | Directly mapped  
`manager_user_type` | `entity.user.managers.attribute.roles.name` | Directly mapped  
`manager_ou_data` | `entity.user.managers.attribute.roles.type` | Mapped: `Users` → `ADMINISTRATOR`, `Service Accounts` → `SERVICE_ACCOUNT`  
`empmanager-src.companyName` | `entity.user.managers.company_name` | Renamed/mapped  
`empmanager-src.department` | `entity.user.managers.department` | Merged  
`empProxyAddress` | `entity.user.managers.email_addresses` | Mapped: `smtp/SMTP` → `empProxyAddress`  
`empmanager-src.mail` | `entity.user.managers.email_addresses` | Merged  
`principal_name` | `entity.user.managers.email_addresses` | Merged  
`empmanager-src.employeeId` | `entity.user.managers.employee_id` | Renamed/mapped  
`empmanager-src.extension_employeeNumber` | `entity.user.managers.employee_id` | Renamed/mapped  
`empmanager-src.givenName` | `entity.user.managers.first_name` | Renamed/mapped  
`empProxyAddress` | `entity.user.managers.group_identifiers` | Merged  
`empmanager-src.surname` | `entity.user.managers.last_name` | Renamed/mapped  
`empmanager-src.city` | `entity.user.managers.personal_address.city` | Renamed/mapped  
`country_n_code` | `entity.user.managers.personal_address.country_or_region` | Directly mapped  
`empmanager-src.streetAddress` | `entity.user.managers.personal_address.name` | Renamed/mapped  
`empmanager-src.state` | `entity.user.managers.personal_address.state` | Renamed/mapped  
`empmanager-src.businessPhones.0` | `entity.user.managers.phone_numbers` | Merged  
`empmanager-src.id` | `entity.user.managers.product_object_id` | Renamed/mapped  
`empmanager-src.jobTitle` | `entity.user.managers.title` | Renamed/mapped  
`empmanager-src.displayName` | `entity.user.managers.user_display_name` | Renamed/mapped  
`empmanager-src.sAMAccountName` | `entity.user.managers.userid` | Renamed/mapped  
`empmanager-src.onPremisesSecurityIdentifier` | `entity.user.managers.windows_sid` | Renamed/mapped  
`country` | `entity.user.personal_address.country_or_region` | Directly mapped  
`usageLocation` | `entity.user.personal_address.country_or_region` | Directly mapped  
`phoneNumber` | `entity.user.phone_numbers` | Merged  
`onPremisesSamAccountName` | `entity.user.userid` | Renamed/mapped  
`sAMAccountName` | `entity.user.userid` | Renamed/mapped  
`gopher-device-item.createdDateTime` | `metadata.event_timestamp` | Parsed as `RFC3339`  
N/A | `entity.labels.key` | Constant: `wfc_AccountType`  
N/A | `entity.user.attribute.labels.key` | Constant: `gopher-manager onPremisesImmutableId`  
N/A | `entity.user.attribute.roles.type` | Constant: `SERVICE_ACCOUNT`  
N/A | `entity.user.managers.attribute.labels.key` | Constant: `manager accountEnabled`  
N/A | `entity.user.managers.attribute.roles.type` | Constant: `SERVICE_ACCOUNT`  
N/A | `entity.user.user_authentication_status` | Constant: `ACTIVE`  
N/A | `metadata.entity_type` | Constant: `USER`  
N/A | `metadata.event_metadata.log_type` | Constant: `AZURE_AD_CONTEXT`  
N/A | `metadata.product_name` | Constant: `Azure Active Directory`  
N/A | `metadata.vendor_name` | Constant: `Microsoft`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-context-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
