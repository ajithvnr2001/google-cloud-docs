---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/msdefender-atp/
title: Collect Microsoft Windows Defender ATP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:47.657480+00:00
---

# Collect Microsoft Windows Defender ATP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/msdefender-atp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Windows Defender ATP logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Microsoft Windows Defender ATP logs to Google Security Operations using an Azure Storage Account. This parser handles logs from Windows Defender ATP in SYSLOG, XML, and JSON formats. It normalizes the diverse fields from these formats into a unified structure, extracting key information like event details, user data, process information, network activity, and security results, and mapping them to the UDM. The parser also performs conditional logic based on `EventID` and `ActionType` to categorize events and enrich the UDM with specific details relevant to each event type.

## Before you begin

  * Ensure that you have a Google SecOps instance.
  * Ensure that you have an active Azure subscription.
  * Ensure that you have a Global Administrator or Microsoft Defender Advanced Threat Hunting role.
  * Sign in to your Azure tenant, go to **Subscriptions > Your subscription > Resource providers > Register to Microsoft.Insights**.



## Configure Azure storage account

  1. In the Azure console, search for Storage accounts.
  2. Click **Create**.
  3. Specify values for the following input parameters: 
     * **Subscription** : select the subscription.
     * **Resource Group** : select the resource group.
     * **Region** : select the region.
     * **Performance** : select the performance (Standard recommended).
     * **Redundancy** : select the redundancy (GRS or LRS recommended).
     * **Storage account name** : enter a name for the new storage account.
  4. Click **Review + create**.
  5. Review the overview of the account and click **Create**.
  6. From the **Storage Account Overview** page, select submenu **Access keys** in **Security + networking**.
  7. Click **Show** next to **key1** or **key2**
  8. Click **Copy to clipboard** to copy the key.
  9. Save the key in a secure location for later use.
  10. From the **Storage Account Overview** page, select submenu **Endpoints** in **Settings**.
  11. Click **Copy to clipboard** to copy the **Blob service** endpoint URL; for example, `https://<storageaccountname>.blob.core.windows.net`.
  12. Save the endpoint URL in a secure location for later use.



## Configure Windows Defender Advanced Threat Hunting log Export

  1. Sign in to **security.microsoft.com** as a global administrator or security administrator.
  2. Go to **Settings > Microsoft Defender XDR**.
  3. Select **Streaming API**. 
  4. Click **Add**.
  5. Select **Forward events to Azure Storage**.
  6. Go to the previously created storage account.
  7. Copy the **Resource ID** and enter it in the **Storage account Resource ID**.
  8. Select all **Events Types**.
  9. Click **Save**.



## Configure a feed in Google SecOps to ingest the Windows Defender Advanced Threat Hunting logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add new**.
  3. In the **Feed name** field, enter a name for the feed; for example, `Defender ATP Logs`.
  4. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  5. Select **Windows Defender ATP** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters:

     * **Azure URI** : the blob endpoint URL. 
       * `ENDPOINT_URL/BLOB_NAME`
         * Replace the following:
         * `ENDPOINT_URL`: the blob endpoint URL (`https://<storageaccountname>.blob.core.windows.net`).
         * `BLOB_NAME`: the name of the blob; such as, `<logname>-logs`.
     * **Source deletion options** : select the deletion option according to your preference.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.

     * **Shared key** : the access key to the Azure Blob Storage.

**Caution:** To avoid **HTTP 429 (Too Many Requests)** errors and ingestion delays, don't reuse the same shared key or storage account across multiple feeds.
     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : the label to be applied to the events from this feed.
  8. Click **Next**.

  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`AccountName` | `target.user.userid` | Populated when `properties.AccountName` is present and `properties.InitiatingProcessAccountName` is blank.  
`AccountSid` | `target.user.windows_sid` | Populated when `properties.AccountSid` is present.  
`AccountType` | `principal.user.attribute.labels` | Key: `AccountType`, Value: `properties.AccountType`  
`Action` | `security_result.action_details` | The value of `properties.Action`.  
`Action` | `security_result.action` | If `properties.Action` contains `quarantine`, the value is `QUARANTINE`.  
`Action Name` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1117.  
`AdditionalFields` | `about.labels`, `principal.resource.attribute.labels` | Key: `AdditionalFields`, Value: `properties.AdditionalFields` (or `AdditionalFields` if parsed as JSON). Individual key-value pairs from `properties.AdditionalFields` (or `AdditionalFields2` if parsed as JSON) are also added as labels.  
`AdditionalFields.ClientMachine` | `principal.resource.attribute.labels` | Key: `ClientMachine`, Value: `_AdditionalFields.ClientMachine`  
`AdditionalFields.Command` | `target.process.command_line` | Used when `ActionType` is `PowerShellCommand`.  
`AdditionalFields.Count` | `read_only_udm.additional.fields` | Key: `Count`, Value: `properties.AdditionalFields.Count`  
`AdditionalFields.DesiredAccess` | `principal.resource.attribute.labels` | Key: `DesiredAccess`, Value: `_AdditionalFields.DesiredAccess`  
`AdditionalFields.DnsQueryString` | `network.dns.questions.name` | Used when `ActionType` is `DnsQueryResponse`.  
`AdditionalFields.DnsQueryResult` | `network.dns.answers` | Parsed within a loop to extract DNS answers. `Result` becomes `name` and `DnsQueryType` is mapped to the numeric `type`.  
`AdditionalFields.Experience` | `security_result.threat_name` | Used when `properties.ActionType` contains `SmartScreen`.  
`AdditionalFields.FileOperation` | `principal.resource.attribute.labels` | Key: `FileOperation`, Value: `_AdditionalFields.FileOperation`  
`AdditionalFields.InitiatingProcess` | `principal.resource.attribute.labels` | Key: `InitiatingProcess`, Value: `_AdditionalFields.InitiatingProcess`  
`AdditionalFields.IsAudit` | `principal.resource.attribute.labels` | Key: `IsAudit`, Value: `_AdditionalFields.IsAudit`  
`AdditionalFields.IsLocalLogon` | `extensions.auth.mechanism` | If value is `true`, sets `auth_mechanism` to `LOCAL`. If `false`, sets to `REMOTE`.  
`AdditionalFields.IsRemoteMachine` | `principal.resource.attribute.labels` | Key: `IsRemoteMachine`, Value: `_AdditionalFields.IsRemoteMachine`  
`AdditionalFields.NamedPipeEnd` | `principal.resource.attribute.labels` | Key: `NamedPipeEnd`, Value: `_AdditionalFields.NamedPipeEnd`  
`AdditionalFields.PipeName` | `principal.resource.attribute.labels` | Key: `PipeName`, Value: `_AdditionalFields.PipeName`  
`AdditionalFields.RemoteClientsAccess` | `principal.resource.attribute.labels` | Key: `RemoteClientsAccess`, Value: `_AdditionalFields.RemoteClientsAccess`  
`AdditionalFields.SessionId` | `principal.resource.attribute.labels` | Key: `SessionId`, Value: `_AdditionalFields.SessionId`  
`AdditionalFields.SignatureName` | `security_result.rule_id` | Used when `properties.ActionType` is `AntivirusDetection`.  
`AdditionalFields.TaskName` | `target.resource.name` | Used when `properties.ActionType` contains `Scheduled`.  
`AdditionalFields.ThreatName` | `security_result.threat_name` | Used when `properties.ActionType` is `AntivirusDetection`.  
`AdditionalFields.ThreadId` | `principal.resource.attribute.labels` | Key: `ThreadId`, Value: `_AdditionalFields.ThreadId`  
`AdditionalFields.TokenModificationProperties` | `principal.resource.attribute.labels` | Key: `TokenModificationProperties`, Value: `_AdditionalFields.TokenModificationProperties`  
`AdditionalFields.TotalBytesCopied` | `principal.resource.attribute.labels` | Key: `TotalBytesCopied`, Value: `_AdditionalFields.TotalBytesCopied`  
`AdditionalFields.WasExecutingWhileDetected` | `about.labels`, `principal.resource.attribute.labels` | Key: `WasExecutingWhileDetected`, Value: `_AdditionalFields.WasExecutingWhileDetected`  
`AdditionalFields.WasRemediated` | `security_result.action` | If value is `true`, sets `sr_action` to `BLOCK`. If `false`, sets to `ALLOW`.  
`AppGuardContainerId` `ApplicationId` | `read_only_udm.additional.fields` | Key: `ApplicationId`, Value: `properties.ApplicationId`  
`category` | `metadata.product_name` | The value of `category`.  
`category` | `metadata.product_event_type` | The value of `category` with `AdvancedHunting-` removed.  
`City` | `principal.location.city` | The value of `properties.City`.  
`ClientIP` | `principal.ip`, `principal.asset.ip` | The value of `properties.RawEventData.ClientIP` if it is a valid IP address.  
`ClientIPAddress` | `principal.ip`, `principal.asset.ip` | The value of `properties.RawEventData.ClientIPAddress` if it is a valid IP address.  
`ClientInfoString` | `read_only_udm.additional.fields` | Key: `ClientInfoString`, Value: `properties.RawEventData.ClientInfoString`  
`ClientProcessName` | `read_only_udm.additional.fields` | Key: `ClientProcessName`, Value: `properties.RawEventData.ClientProcessName`  
`ClientRequestId` | `read_only_udm.additional.fields` | Key: `ClientRequestId`, Value: `properties.RawEventData.ClientRequestId`  
`ClientVersion` | `read_only_udm.additional.fields` | Key: `ClientVersion`, Value: `properties.RawEventData.ClientVersion`  
`ConnectedNetworks` | `entity.asset.network_domain` | The `Name` field within `ConnectedNetworks` if present.  
`CountryCode` | `principal.location.country_or_region` | The value of `properties.CountryCode`.  
`CreationTime` | `read_only_udm.additional.fields` | Key: `CreationTime`, Value: `properties.RawEventData.CreationTime`  
`Current Engine Version` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2000.  
`Current Signature Version` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2000.  
`DeliveryAction` | `read_only_udm.additional.fields` | Key: `DeliveryAction`, Value: `properties.DeliveryAction`  
`DeliveryAction` | `security_result.action` | If `properties.DeliveryAction` contains `Blocked`, the value is `BLOCK`.  
`DeliveryLocation` | `read_only_udm.additional.fields` | Key: `DeliveryLocation`, Value: `properties.DeliveryLocation`  
`DestinationLocationType` | `read_only_udm.additional.fields` | Key: `DestinationLocationType`, Value: `properties.RawEventData.DestinationLocationType`  
`DetectionMethods` | `security_result.rule_name`, `security_result.detection_fields` | The value of `properties.DetectionMethods` with quotes removed becomes both `rule_name` and `detection_fields` (key: `Detection Method`).  
`Detection User` | `principal.user.userid` | Used when `EventID` is 1116 or 1117.  
`DeviceCategory` | `entity.asset.category` | The value of `properties.DeviceCategory`.  
`DeviceId` | `principal.asset_id` | `WINDOWS_DEFENDER:` \+ `DeviceId` when parsing syslog/JSON or XML. `DeviceId:` \+ `properties.DeviceId` when parsing JSON.  
`DeviceName` | `principal.hostname`, `principal.asset.hostname` | `DeviceName` when parsing syslog/JSON or XML. `properties.DeviceName` when parsing JSON. `properties.RawEventData.DeviceName` if present.  
`DeviceType` | `read_only_udm.additional.fields` | Key: `DeviceType`, Value: `properties.DeviceType`  
`Domain` | `principal.administrative_domain` | Used when parsing syslog/JSON or XML.  
`Dynamic Signature Compilation Timestamp` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2010 or 2011.  
`Dynamic Signature Type` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2010 or 2011.  
`Dynamic Signature Version` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2010 or 2011.  
`EmailClusterId` | `read_only_udm.additional.fields` | Key: `EmailClusterId`, Value: `properties.EmailClusterId`  
`EmailDirection` | `network.direction` | If value is `Inbound`, sets to `INBOUND`. If `Outbound`, sets to `OUTBOUND`. Otherwise, sets to `UNKNOWN_DIRECTION`.  
`EmailLanguage` | `read_only_udm.additional.fields` | Key: `EmailLanguage`, Value: `properties.EmailLanguage`  
`Engine Version` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1011.  
`EnforcementMode` | `read_only_udm.additional.fields` | Key: `EnforcementMode`, Value: `properties.EnforcementMode`  
`Error Code` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1117 or 2001.  
`Error Description` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1117 or 2001.  
`EventID` | `metadata.product_event_type` | Part of the `metadata.product_event_type` when parsing syslog/JSON or XML.  
`EventTime` | `metadata.event_timestamp` | Parsed to generate the `metadata.event_timestamp`.  
`ExchangeLocations` | `security_result.category_details` | The value of `properties.RawEventData.ExchangeLocations`.  
`ExternalAccess` | `read_only_udm.additional.fields` | Key: `ExternalAccess`, Value: `properties.RawEventData.ExternalAccess`  
`FailureReason` | `security_result.description` | The value of `properties.FailureReason` when `ActionType` is `LogonFailed`.  
`FileExtension` | `read_only_udm.additional.fields` | Key: `FileExtension`, Value: `properties.RawEventData.FileExtension`  
`FileName` | `about.file.full_path` | The value of `properties.FileName` when `category` contains `EmailAttachmentInfo`. Otherwise, `target.process.file.full_path`.  
`FileSize` | `target.process.file.size` | The value of `properties.FileSize` converted to an unsigned integer.  
`FileSize` | `about.file.size` | The value of `properties.FileSize` converted to an unsigned integer when `category` contains `EmailAttachmentInfo`.  
`FileSize` | `principal.process.file.size` | The value of `properties.RawEventData.FileSize` converted to an unsigned integer.  
`FileType` | `about.file.mime_type` | The value of `properties.FileType` when `category` contains `EmailAttachmentInfo`. Otherwise, `target.process.file.mime_type`.  
`FileType` | `read_only_udm.additional.fields` | Key: `FileType`, Value: `properties.RawEventData.FileType` if not empty or `Unknown`.  
`FolderPath` | `target.file.full_path` | The value of `properties.FolderPath`.  
`FolderPath` | `target.process.file.full_path` | The value of `FolderPath` when `ActionType` is `CreateRemoteThreadApiCall`, `ExploitGuardNonMicrosoftSignedBlocked`, `DriverLoad`, `FileRenamed`, `OpenProcessApiCall`, `ReadProcessMemoryApiCall`, `ImageLoaded`, or `properties.ActionType` is `FileCreatedOnNetworkShare`.  
`Hidden` | `read_only_udm.additional.fields` | Key: `Hidden`, Value: `properties.RawEventData.Hidden`  
`Hostname` | `principal.hostname`, `principal.asset.hostname` | Used when parsing syslog/JSON or XML.  
`IPAddresses` | `entity.asset.ip` | The `IPAddress` field within each object in the `IPAddresses` array, excluding IPv6 link-local, IPv4 APIPA, IPv6 loopback, IPv6 multicast, and loopback addresses.  
`IPAddress` | `principal.ip`, `principal.asset.ip` | The value of `properties.IPAddress` if it is a valid IP address.  
`IPCategory` | `read_only_udm.additional.fields` | Key: `IPCategory`, Value: `properties.IPCategory`  
`IPTags` | `read_only_udm.additional.fields` | Key: `IPTags`, Value: `properties.IPTags`  
`ISP` | `read_only_udm.additional.fields` | Key: `ISP`, Value: `properties.ISP`  
`InitiatingProcessAccountName` | `principal.user.userid` | Populated when present and `properties.AccountName` is blank, or when both are present.  
`InitiatingProcessAccountSid` | `principal.user.windows_sid` | Populated when present and `properties.AccountSid` is blank, or when both are present.  
`InitiatingProcessAccountUpn` | `principal.user.email_addresses` | The value of `properties.InitiatingProcessAccountUpn`.  
`InitiatingProcessCommandLine` | `principal.process.command_line` | The value of `properties.InitiatingProcessCommandLine` with quotes removed.  
`InitiatingProcessFileName` | `principal.process.file.full_path` | The value of `properties.InitiatingProcessFileName`.  
`InitiatingProcessFileSize` | `principal.process.file.size` | The value of `properties.InitiatingProcessFileSize` converted to an unsigned integer.  
`InitiatingProcessFolderPath` | `principal.process.file.full_path` | The value of `properties.InitiatingProcessFolderPath`.  
`InitiatingProcessId` | `principal.process.pid` | The value of `properties.InitiatingProcessId` converted to a string.  
`InitiatingProcessIntegrityLevel` | `about.labels`, `principal.resource.attribute.labels` | Key: `InitiatingProcessIntegrityLevel`, Value: `properties.InitiatingProcessIntegrityLevel`  
`InitiatingProcessMD5` | `principal.process.file.md5` | The value of `properties.InitiatingProcessMD5`.  
`InitiatingProcessParentFileName` | `principal.process.parent_process.file.full_path` | The value of `properties.InitiatingProcessParentFileName`.  
`InitiatingProcessParentId` | `principal.process.parent_process.pid` | The value of `properties.InitiatingProcessParentId` converted to a string.  
`InitiatingProcessSHA1` | `principal.process.file.sha1` | The value of `properties.InitiatingProcessSHA1`.  
`InitiatingProcessSHA256` | `principal.process.file.sha256` | The value of `properties.InitiatingProcessSHA256`.  
`InitiatingProcessSignatureStatus` | `read_only_udm.additional.fields` | Key: `InitiatingProcessSignatureStatus`, Value: `properties.InitiatingProcessSignatureStatus`  
`InitiatingProcessSignerType` | `read_only_udm.additional.fields` | Key: `InitiatingProcessSignerType`, Value: `properties.InitiatingProcessSignerType`  
`InitiatingProcessTokenElevation` | `about.labels`, `principal.resource.attribute.labels` | Key: `InitiatingProcessTokenElevation`, Value: `properties.InitiatingProcessTokenElevation`  
`InitiatingProcessVersionInfoCompanyName` | `principal.user.company_name` | The value of `properties.InitiatingProcessVersionInfoCompanyName`.  
`InitiatingProcessVersionInfoFileDescription` | `principal.resource.attribute.labels` | Key: `File Description`, Value: `properties.InitiatingProcessVersionInfoFileDescription`  
`InitiatingProcessVersionInfoInternalFileName` | `principal.resource.attribute.labels` | Key: `File Name`, Value: `properties.InitiatingProcessVersionInfoInternalFileName`  
`InitiatingProcessVersionInfoOriginalFileName` | `principal.resource.attribute.labels` | Key: `Original File Name`, Value: `properties.InitiatingProcessVersionInfoOriginalFileName`  
`InitiatingProcessVersionInfoProductName` | `read_only_udm.additional.fields` | Key: `InitiatingProcessVersionInfoProductName`, Value: `properties.InitiatingProcessVersionInfoProductName`  
`InitiatingProcessVersionInfoProductVersion` | `metadata.product_version` | The value of `properties.InitiatingProcessVersionInfoProductVersion`.  
`InternetMessageId` | `read_only_udm.additional.fields` | Key: `InternetMessageId`, Value: `properties.InternetMessageId` with angle brackets removed.  
`IsAdminOperation` | `read_only_udm.additional.fields` | Key: `IsAdminOperation`, Value: `properties.IsAdminOperation`  
`IsAnonymousProxy` | `read_only_udm.additional.fields` | Key: `IsAnonymousProxy`, Value: `properties.IsAnonymousProxy`  
`IsExternalUser` | `read_only_udm.additional.fields` | Key: `IsExternalUser`, Value: `properties.IsExternalUser`  
`IsImpersonated` | `read_only_udm.additional.fields` | Key: `IsImpersonated`, Value: `properties.IsImpersonated`  
`IsLocalAdmin` | `about.labels`, `principal.resource.attribute.labels` | Key: `IsLocalAdmin`, Value: `true` or `false` depending on the boolean value of `properties.IsLocalAdmin`.  
`LoggedOnUsers` | `target.user.userid`, `entity.relations.entity.user.userid` | The `UserName` field within each object in the `LoggedOnUsers` array is added as a `target.user.userid` and a related user entity. The `Sid` field is added as `entity.relations.entity.user.windows_sid`.  
`LocalIP` | `principal.ip`, `principal.asset.ip` | The value of `LocalIP` when parsing JSON.  
`LocalPort` | `principal.port` | The value of `LocalPort` converted to an integer when parsing JSON.  
`LogonType` | `extensions.auth.mechanism` | Mapped to a UDM authentication mechanism based on the value.  
`LogonType` | `read_only_udm.additional.fields` | Key: `LogonType`, Value: `properties.RawEventData.LogonType`  
`LogonUserSid` | `read_only_udm.additional.fields` | Key: `LogonUserSid`, Value: `properties.RawEventData.LogonUserSid`  
`MacAddress` | `entity.asset.mac` | The value of `MacAddress` or `properties.MacAddress` formatted as a colon-separated string.  
`MailboxGuid` | `read_only_udm.additional.fields` | Key: `MailboxGuid`, Value: `properties.RawEventData.MailboxGuid`  
`MailboxOwnerMasterAccountSid` | `read_only_udm.additional.fields` | Key: `MailboxOwnerMasterAccountSid`, Value: `properties.RawEventData.MailboxOwnerMasterAccountSid`  
`MailboxOwnerSid` | `read_only_udm.additional.fields` | Key: `MailboxOwnerSid`, Value: `properties.RawEventData.MailboxOwnerSid`  
`MailboxOwnerUPN` | `read_only_udm.additional.fields` | Key: `MailboxOwnerUPN`, Value: `properties.RawEventData.MailboxOwnerUPN`  
`MD5` | `target.process.file.md5` | The value of `properties.MD5`.  
`Message` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1000, 1001, 1002, 1013, 1116, 1117, 2000, 2001, 2002, 2010, 2011, or 5007.  
`NetworkAdapterType` | `metadata.product_event_type` | The value of `NetworkAdapterType` when parsing JSON.  
`NetworkMessageId` | `network.email.mail_id` | The value of `properties.NetworkMessageId`.  
`New Value` | `security_result.description` | Part of the `security_result.description` when `EventID` is 5007.  
`Object Name` | `read_only_udm.additional.fields` | Key: `ObjectName`, Value: `properties.ObjectName`  
`Object Type` | `read_only_udm.additional.fields` | Key: `ObjectType`, Value: `properties.ObjectType`  
`ObjectId` | `read_only_udm.additional.fields` | Key: `ObjectId`, Value: `properties.ObjectId` or `properties.RawEventData.ObjectId`.  
`Old Value` | `security_result.description` | Part of the `security_result.description` when `EventID` is 5007.  
`Operation` | `read_only_udm.additional.fields` | Key: `Operation`, Value: `properties.RawEventData.Operation`  
`operationName` | `read_only_udm.additional.fields` | Key: `OperationName`, Value: `operationName`  
`OrganizationId` | `read_only_udm.additional.fields` | Key: `OrganizationId`, Value: `properties.RawEventData.OrganizationId`  
`OrganizationName` | `read_only_udm.additional.fields` | Key: `OrganizationName`, Value: `properties.RawEventData.OrganizationName`  
`OriginatingServer` | `read_only_udm.additional.fields` | Key: `OriginatingServer`, Value: `properties.RawEventData.OriginatingServer`  
`OSPlatform` | `asset.platform_software.platform` | If value contains `macos`, sets `platform` to `MAC`. If `windows`, sets to `WINDOWS`. If `nix`, sets to `LINUX`.  
`OSVersion` | `asset.platform_software.platform_version` | The value of `properties.OSVersion`.  
`Path` | `target.file.full_path` | Used when `EventID` is 1011 or 1116.  
`Persistence Limit Type` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2010 or 2011.  
`Persistence Limit Value` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2010 or 2011.  
`Persistence Path` | `target.file.full_path` | Used when `EventID` is 2010 or 2011.  
`Previous Engine Version` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2000, 2001, or 2002.  
`PreviousRegistryKey` | `target.registry.registry_key` | The value of `properties.PreviousRegistryKey`.  
`PreviousRegistryValueData` | `target.resource.attribute.labels` | Key: `PreviousRegistryValueData`, Value: `properties.PreviousRegistryValueData`  
`PreviousRegistryValueName` | `target.resource.attribute.labels` | Key: `PreviousRegistryValueName`, Value: `properties.PreviousRegistryValueName`  
`Previous security intelligence Version` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2001.  
`Previous Signature Version` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2000.  
`ProcessCommandLine` | `target.process.command_line` | The value of `properties.ProcessCommandLine`.  
`ProcessID` | `principal.process.pid` | Used when parsing syslog/JSON or XML.  
`ProcessId` | `target.process.pid` | The value of `properties.ProcessId` converted to a string.  
`Process Name` | `target.process.pid` | Used when `EventID` is 1116 or 1117.  
`Product Version` | `metadata.product_version` | Used when parsing syslog/JSON or XML.  
`Protocol` | `network.ip_protocol` | If value contains `Tcp`, sets to `TCP`. If `Udp`, sets to `UDP`. If `Icmp`, sets to `ICMP`.  
`ProviderGuid` | `principal.resource.id` | Used when parsing syslog/JSON or XML.  
`PublicIP` | `principal.ip`, `principal.asset.ip` | The value of `properties.PublicIP`.  
`RawEventData.Application` | `principal.application` | The value of `properties.RawEventData.Application`.  
`RawEventData.ClientIP` | `principal.ip`, `principal.asset.ip` | The value of `properties.RawEventData.ClientIP` if it is a valid IP address.  
`RawEventData.ClientIPAddress` | `principal.ip`, `principal.asset.ip` | The value of `properties.RawEventData.ClientIPAddress` if it is a valid IP address.  
`RawEventData.ClientInfoString` | `read_only_udm.additional.fields` | Key: `ClientInfoString`, Value: `properties.RawEventData.ClientInfoString`  
`RawEventData.ClientProcessName` | `read_only_udm.additional.fields` | Key: `ClientProcessName`, Value: `properties.RawEventData.ClientProcessName`  
`RawEventData.ClientRequestId` | `read_only_udm.additional.fields` | Key: `ClientRequestId`, Value: `properties.RawEventData.ClientRequestId`  
`RawEventData.ClientVersion` | `read_only_udm.additional.fields` | Key: `ClientVersion`, Value: `properties.RawEventData.ClientVersion`  
`RawEventData.CreationTime` | `read_only_udm.additional.fields` | Key: `CreationTime`, Value: `properties.RawEventData.CreationTime`  
`RawEventData.DeviceName` | `principal.hostname`, `principal.asset.hostname` | The value of `properties.RawEventData.DeviceName`.  
`RawEventData.DestinationLocationType` | `read_only_udm.additional.fields` | Key: `DestinationLocationType`, Value: `properties.RawEventData.DestinationLocationType`  
`RawEventData.ExchangeLocations` | `security_result.category_details` | The value of `properties.RawEventData.ExchangeLocations`.  
`RawEventData.ExternalAccess` | `read_only_udm.additional.fields` | Key: `ExternalAccess`, Value: `properties.RawEventData.ExternalAccess`  
`RawEventData.FileExtension` | `read_only_udm.additional.fields` | Key: `FileExtension`, Value: `properties.RawEventData.FileExtension`  
`RawEventData.FileSize` | `target.process.file.size` | The value of `properties.RawEventData.FileSize` converted to an unsigned integer.  
`RawEventData.FileType` | `read_only_udm.additional.fields` | Key: `FileType`, Value: `properties.RawEventData.FileType` if not empty or `Unknown`.  
`RawEventData.Hidden` | `read_only_udm.additional.fields` | Key: `Hidden`, Value: `properties.RawEventData.Hidden`  
`RawEventData.Id` | `read_only_udm.additional.fields` | Key: `RawEventDataId`, Value: `properties.RawEventData.Id`  
`RawEventData.Item.Id` | `item_idm.read_only_udm.additional.fields` | Key: `RawEventDataItemId`, Value: `properties.RawEventData.item.id`  
`RawEventData.LogonType` | `read_only_udm.additional.fields` | Key: `LogonType`, Value: `properties.RawEventData.LogonType`  
`RawEventData.LogonUserSid` | `read_only_udm.additional.fields` | Key: `LogonUserSid`, Value: `properties.RawEventData.LogonUserSid`  
`RawEventData.MailboxGuid` | `read_only_udm.additional.fields` | Key: `MailboxGuid`, Value: `properties.RawEventData.MailboxGuid`  
`RawEventData.MailboxOwnerMasterAccountSid` | `read_only_udm.additional.fields` | Key: `MailboxOwnerMasterAccountSid`, Value: `properties.RawEventData.MailboxOwnerMasterAccountSid`  
`RawEventData.MailboxOwnerSid` | `read_only_udm.additional.fields` | Key: `MailboxOwnerSid`, Value: `properties.RawEventData.MailboxOwnerSid`  
`RawEventData.MailboxOwnerUPN` | `read_only_udm.additional.fields` | Key: `MailboxOwnerUPN`, Value: `properties.RawEventData.MailboxOwnerUPN`  
`RawEventData.MDATPDeviceId` | `read_only_udm.additional.fields` | Key: `MDATPDeviceId`, Value: `properties.RawEventData.MDATPDeviceId`  
`RawEventData.ObjectId` | `read_only_udm.additional.fields` | Key: `ObjectId`, Value: `properties.RawEventData.ObjectId`  
`RawEventData.Operation` | `read_only_udm.additional.fields` | Key: `Operation`, Value: `properties.RawEventData.Operation`  
`RawEventData.OrganizationId` | `read_only_udm.additional.fields` | Key: `OrganizationId`, Value: `properties.RawEventData.OrganizationId`  
`RawEventData.OrganizationName` | `read_only_udm.additional.fields` | Key: `OrganizationName`, Value: `properties.RawEventData.OrganizationName`  
`RawEventData.OriginatingServer` | `read_only_udm.additional.fields` | Key: `OriginatingServer`, Value: `properties.RawEventData.OriginatingServer`  
`RawEventData.ParentFolder.Id` | `read_only_udm.additional.fields` | Key: `RawEventDataParentFolderId`, Value: `properties.RawEventData.ParentFolder.Id`  
`RawEventData.Pid` | `target.process.pid` | The value of `properties.RawEventData.Pid` converted to a string.  
`RawEventData.Query` | `read_only_udm.additional.fields` | Key: `Query`, Value: `properties.RawEventData.Query`  
`RawEventData.RecordType` | `network.dns.questions.type` | The value of `properties.RawEventData.RecordType` converted to an unsigned integer.  
`RawEventData.ResultStatus` | `read_only_udm.additional.fields` | Key: `ResultStatus`, Value: `properties.RawEventData.ResultStatus`  
`RawEventData.Scope` | `read_only_udm.additional.fields` | Key: `Scope`, Value: `properties.RawEventData.Scope`  
`RawEventData.SessionId` | `network.session_id` | The value of `properties.RawEventData.SessionId`.  
`RawEventData.Sha1` | `target.process.file.sha1` | The value of `properties.RawEventData.Sha1`.  
`RawEventData.Sha256` | `target.process.file.sha256` | The value of `properties.RawEventData.Sha256`.  
`RawEventData.TargetDomain` | `target.hostname`, `target.asset.hostname` | The value of `properties.RawEventData.TargetDomain`.  
`RawEventData.TargetFilePath` | `target.file.full_path` | The value of `properties.RawEventData.TargetFilePath`.  
`RawEventData.UserId` | `principal.user.email_addresses` | The value of `properties.RawEventData.UserId` if it is an email address.  
`RawEventData.UserKey` | `read_only_udm.additional.fields` | Key: `UserKey`, Value: `properties.RawEventData.UserKey`  
`RawEventData.UserType` | `read_only_udm.additional.fields` | Key: `UserType`, Value: `properties.RawEventData.UserType`  
`RawEventData.Version` | `read_only_udm.additional.fields` | Key: `Version`, Value: `properties.RawEventData.Version`  
`RawEventData.Workload` | `read_only_udm.additional.fields` | Key: `Workload`, Value: `properties.RawEventData.Workload`  
`RecipientEmailAddress` | `network.email.to`, `target.user.email_addresses` | The value of `properties.RecipientEmailAddress`.  
`RecipientObjectId` | `target.user.product_object_id` | The value of `properties.RecipientObjectId`.  
`RegistryKey` | `target.registry.registry_key` | The value of `properties.RegistryKey`.  
`RegistryValueData` | `target.registry.registry_value_data` | The value of `properties.RegistryValueData`.  
`RegistryValueName` | `target.registry.registry_value_name` | The value of `properties.RegistryValueName`.  
`Remediation User` | `intermediary.user.userid` | Used when `EventID` is 1117.  
`RemoteDeviceName` | `target.hostname`, `target.asset.hostname` | The value of `properties.RemoteDeviceName`.  
`RemoteIP` | `target.ip`, `target.asset.ip` | The value of `properties.RemoteIP` if not empty, `-`, or `null`.  
`RemoteIPType` | `about.labels`, `principal.resource.attribute.labels` | Key: `RemoteIPType`, Value: `properties.RemoteIPType`  
`RemotePort` | `target.port` | The value of `properties.RemotePort` converted to an integer.  
`RemoteUrl` | `target.url` | The value of `properties.RemoteUrl`. If it contains a hostname, the hostname is extracted and mapped to `target.hostname` and `target.asset.hostname`.  
`Removal Reason Value` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2011.  
`ReportId` | `metadata.product_log_id` | The value of `properties.ReportId` converted to a string.  
`Scan ID` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1000, 1001, or 1002.  
`Scan Parameters` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1000, 1001, or 1002.  
`Scan Resources` | `target.file.full_path` | Used when `EventID` is 1000.  
`Scan Time Hours` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1001.  
`Scan Time Minutes` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1001.  
`Scan Time Seconds` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1001.  
`Scan Type` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1000, 1001, or 1002.  
`Security intelligence Type` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2001.  
`Security intelligence Version` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1011.  
`SenderDisplayName` | `principal.user.user_display_name` | The value of `properties.SenderDisplayName`.  
`SenderFromAddress` | `network.email.from`, `principal.user.email_addresses` | The value of `properties.SenderFromAddress`.  
`SenderFromDomain` | `principal.administrative_domain` | The value of `properties.SenderFromDomain`.  
`SenderIPv4` | `principal.ip`, `principal.asset.ip` | The value of `properties.SenderIPv4`.  
`SenderIPv6` | `principal.ip`, `principal.asset.ip` | The value of `properties.SenderIPv6`.  
`SenderMailFromAddress` | `principal.user.attribute.labels` | Key: `SenderMailFromAddress`, Value: `properties.SenderMailFromAddress`  
`SenderMailFromDomain` | `principal.user.attribute.labels` | Key: `SenderMailFromDomain`, Value: `properties.SenderMailFromDomain`  
`SenderObjectId` | `principal.user.product_object_id` | The value of `properties.SenderObjectId`.  
`Severity Name` | `security_result.severity` | If value is `Low`, sets to `LOW`. If `Moderate`, sets to `MEDIUM`. If `High` or `Severe`, sets to `HIGH`.  
`Severity` | `security_result.severity` | If value contains `informational`, sets to `INFORMATIONAL`. If `low`, sets to `LOW`. If `medium`, sets to `MEDIUM`. If `high`, sets to `HIGH`. Otherwise, sets to `UNKNOWN_SEVERITY`.  
`Severity` | `security_result.severity_details` | The value of `properties.Severity`.  
`SHA1` | `target.process.file.sha1` | The value of `properties.SHA1`.  
`SHA256` | `target.process.file.sha256` | The value of `properties.SHA256`.  
`SHA256` | `about.file.sha256` | The value of `properties.SHA256` when `category` contains `EmailAttachmentInfo`.  
`Signature Type` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2000 or 2010.  
`SourceModuleName` | `target.resource.name` | Used when `EventID` is 2008.  
`Source Path` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2001.  
`Subject` | `network.email.subject` | The value of `properties.Subject`.  
`Tenant` | `read_only_udm.additional.fields` | Key: `Tenant`, Value: `Tenant`  
`tenantId` | `observer.cloud.project.id`, `target.resource_ancestors.product_object_id` | The value of `tenantId` or `properties.tenantId`.  
`Threat ID` | `security_result.threat_name` | Part of the `security_result.threat_name` when `EventID` is 1011 or 1116.  
`ThreatNames` | `security_result.threat_name` | The value of `properties.ThreatNames`.  
`Threat Types` | `security_result.category` | If value is `Phish`, sets `security_result_category` to `MAIL_PHISHING`. Otherwise, sets to `UNKNOWN_CATEGORY`.  
`Timestamp` | `security_result.description` | Part of the `security_result.description` when `EventID` is 1013.  
`Timestamp` | `metadata.event_timestamp` | Parsed to generate the `metadata.event_timestamp`.  
`Timestamp` | `entity.asset.system_last_update_time` | The value of `properties.Timestamp` when `category` is `AdvancedHunting-DeviceNetworkInfo`.  
`Title` | `security_result.threat_name` | The value of `properties.Title`.  
`Update Source` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2001.  
`Update State` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2001.  
`Update Type` | `security_result.description` | Part of the `security_result.description` when `EventID` is 2000 or 2001.  
`UserAgent` | `network.http.user_agent` | The value of `properties.UserAgent`.  
`UserAgentTags` | `additional.fields` | Each element in the `properties.UserAgentTags` array is added as a label with key `UserAgentTags`.  
`Url` | `target.url` | The value of `properties.Url`.  
`UrlCount` | `read_only_udm.additional.fields` | Key: `UrlCount`, Value: `properties.UrlCount`  
`UrlDomain` | `target.hostname`, `target.asset.hostname` | The value of `properties.UrlDomain`.  
`UrlLocation` | `read_only_udm.additional.fields` | Key: `UrlLocation`, Value: `properties.UrlLocation`  
`User` | `target.user.userid` | Used when `EventID` is 1000, 1001, 1002, 1011, 1013, 2000, 2002, or when `Message` contains `\tUser:`.  
`UserID` | `principal.user.userid` | Used when `EventID` is 2010 or 2011.  
(Parser Logic) | `metadata.event_type` | Set to `GENERIC_EVENT` initially, then overwritten based on other fields and logic. Common values include `NETWORK_CONNECTION`, `PROCESS_LAUNCH`, `FILE_CREATION`, `FILE_MODIFICATION`, `USER_LOGIN`, `SCAN_HOST`, `SCAN_PROCESS`, `SYSTEM_AUDIT_LOG_WIPE`, `SETTING_MODIFICATION`, `FILE_DELETION`, `PROCESS_MODULE_LOAD`, `PROCESS_UNCATEGORIZED`, `STATUS_UPDATE`, `PROCESS_OPEN`, `NETWORK_DNS`, `FILE_MOVE`, `REGISTRY_CREATION`, `REGISTRY_DELETION`, `REGISTRY_MODIFICATION`, `SCHEDULED_TASK_CREATION`, `SCHEDULED_TASK_DELETION`, `SCHEDULED_TASK_MODIFICATION`, `SCAN_NETWORK`, `USER_UNCATEGORIZED`.  
(Parser Logic) | `metadata.vendor_name` | Set to `Microsoft`.  
(Parser Logic) | `metadata.product_name` | Set to `Windows Defender ATP` initially, then potentially overwritten by the `category` field.  
(Parser Logic) | `metadata.product_event_type` | Set to `GENERIC_EVENT` initially, then overwritten based on other fields and logic.  
(Parser Logic) | `metadata.product_version` | Set based on `Product Version` or `properties.InitiatingProcessVersionInfoProductVersion`.  
(Parser Logic) | `metadata.log_type` | Set to `WINDOWS_DEFENDER_ATP`.  
(Parser Logic) | `principal.resource.type` | Set to `PROVIDER` when parsing syslog/JSON or XML.  
(Parser Logic) | `target.resource_ancestors` | Contains a single ancestor with `product_object_id` set to the `tenantId`.  
(Parser Logic) | `security_result.summary` | Set based on `EventID`, `properties.ActionType`, or `properties.Title` and `properties.Category`.  
(Parser Logic) | `security_result.description` | Constructed from various fields depending on the `EventID` or `properties.ActionType`.  
(Parser Logic) | `security_result.action` | Set to `ALLOW` initially, then potentially overwritten based on `AdditionalFields.WasRemediated`, `ActionType`, or `Action Name`.  
(Parser Logic) | `security_result.severity` | Set based on `Severity Name` or `properties.Severity`.  
(Parser Logic) | `security_result.category` | Set based on `Threat Types`.  
(Parser Logic) | `network.direction` | Set based on `RemoteIP`, `LocalIP`, or `EmailDirection`.  
(Parser Logic) | `network.ip_protocol` | Set to `TCP` when `metadata.event_type` is `NETWORK_CONNECTION`.  
(Parser Logic) | `network.session_id` | Set based on `properties.RawEventData.SessionId`.  
(Parser Logic) | `network.http.user_agent` | Set based on `properties.UserAgent`.  
(Parser Logic) | `network.email.mail_id` | Set based on `properties.NetworkMessageId`.  
(Parser Logic) | `network.email.subject` | Set based on `properties.Subject`.  
(Parser Logic) | `network.email.from` | Set based on `properties.SenderFromAddress`.  
(Parser Logic) | `network.email.to` | Set based on `properties.RecipientEmailAddress`.  
(Parser Logic) | `network.dns.questions.name` | Set based on `AdditionalFields.DnsQueryString`.  
(Parser Logic) | `network.dns.questions.type` | Set based on `properties.RawEventData.RecordType`.  
(Parser Logic) | `network.dns.answers` | Constructed from `AdditionalFields.DnsQueryResult`.  
(Parser Logic) | `extensions.auth.type` | Set to `MACHINE` when `ActionType` is `LogonAttempted` or `LogonSuccess`.  
(Parser Logic) | `extensions.auth.mechanism` | Set based on `LogonType` or `AdditionalFields.IsLocalLogon`.  
(Parser Logic) | `extensions.auth.auth_details` | Set based on `properties.AuthenticationDetails`.  
(Parser Logic) | `entity.asset.asset_id` | Constructed using `WINDOWS:` \+ `DeviceId` or `properties.DeviceId`.  
(Parser Logic) | `entity.asset.product_object_id` | Set to `DeviceId` or `properties.DeviceId`.  
(Parser Logic) | `entity.asset.network_domain` | Extracted from `ConnectedNetworks`.  
(Parser Logic) | `entity.asset.ip` | Set based on `IPAddresses`, `_ipaddress`, `PublicIP`, or `LocalIP`.  
(Parser Logic) | `entity.asset.mac` | Set based on `MacAddress` or `properties.MacAddress`.  
(Parser Logic) | `entity.asset.hostname` | Set based on `DeviceName` or `properties.DeviceName`.  
(Parser Logic) | `entity.asset.platform_software.platform` | Set based on `OSPlatform`.  
(Parser Logic) | `entity.asset.platform_software.platform_version` | Set based on `OSVersion`.  
(Parser Logic) | `entity.asset.category` | Set based on `DeviceCategory`.  
(Parser Logic) | `entity.asset.type` | Set to `WORKSTATION` for device and network info events.  
(Parser Logic) | `entity.asset.system_last_update_time` | Set based on `properties.Timestamp` for network info events.  
(Parser Logic) | `entity.relations` | Constructed from `LoggedOnUsers`.  
(Parser Logic) | `entity.metadata.entity_type` | Set to `ASSET` for device, network, and asset events.  
(Parser Logic) | `about.labels` | Contains labels for various fields that don't fit directly into the UDM schema.  
(Parser Logic) | `principal.user.attribute.labels` | Contains labels for various user-related fields.  
(Parser Logic) | `principal.resource.attribute.labels` | Contains labels for various resource-related fields.  
(Parser Logic) | `target.resource.resource_type` | Set to `TASK` for scheduled task events and `SETTING` for setting modification events.  
(Parser Logic) | `target.resource.name` | Set based on `SourceModuleName`, `AdditionalFields.TaskName`, or `_taskname`.  
(Parser Logic) | `target.resource.product_object_id` | Set based on `properties.ReportId`.  
(Parser Logic) | `target.resource_ancestors` | Set based on `tenantId`.  
(Parser Logic) | `target.registry.registry_key` | Set based on `RegistryKey`, `PreviousRegistryKey`, or `properties.RegistryKey`.  
(Parser Logic) | `target.registry.registry_value_name` | Set based on `RegistryValueName` or `properties.RegistryValueName`.  
(Parser Logic) | `target.registry.registry_value_data` | Set based on `RegistryValueData` or `properties.RegistryValueData`.  
(Parser Logic) | `intermediary.user.userid` | Set based on `Remediation User`.  
(Parser Logic) | `metadata.collected_timestamp` | Set to the event timestamp for asset and network info events.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
