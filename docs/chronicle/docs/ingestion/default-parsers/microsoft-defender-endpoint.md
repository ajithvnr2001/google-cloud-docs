---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint/
title: Collect Microsoft Defender for Endpoint logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:17.318396+00:00
---

# Collect Microsoft Defender for Endpoint logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Defender for Endpoint logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can collect Microsoft Defender for Endpoint logs by setting up a Google Security Operations feed and how log fields map to Google SecOps unified data model (UDM) fields.

For more information, see [Data ingestion to Google SecOps](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

A typical deployment consists of Microsoft Defender for Endpoint and the Google SecOps feed configured to send logs to Google SecOps. Your deployment might be different from the typical deployment that is described in this document. The deployment contains the following components:

  * **Microsoft Defender for Endpoint** : The platform that collects logs.

  * **Azure Storage** : The platform that stores logs.

  * **Google SecOps feed** : The Google SecOps feed that fetches logs from Microsoft Defender for Endpoint and writes logs to Google SecOps.

  * **Google SecOps** : The platform that retains and analyzes the logs from Microsoft Defender for Endpoint.




An ingestion label identifies the parser that normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `MICROSOFT_DEFENDER_ENDPOINT` ingestion label.

## Before you begin

Ensure you have the following prerequisites:

  * All systems in the deployment architecture are configured with the UTC time zone.
  * You meet the prerequisites for using Microsoft Defender for Endpoint. For more information, see [Microsoft Defender XDR prerequisites](https://learn.microsoft.com/en-us/defender-xdr/prerequisites?view=o365-worldwide).
  * Configured [Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/mde-planning-guide)
  * A configured storage account in your tenant. To configure the storage account, see Configure Azure Storage account. For a general overview of storage accounts, see [Microsoft Azure storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview).



## Configure Azure Storage account

This section describes how to configure and deploy an Azure Storage account in Microsoft Azure.

### Create storage account

Before you begin, ensure that your resource group has been successfully deployed in your Azure environment.

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **Create**.
  3. Provide the following configuration details under the **Basics** tab:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription.  
**Resource group** | Select the deployed resource group.  
**Storage account name** | Enter a globally unique name between 3 and 24 characters, using lowercase letters and numbers only.  
**Region** | Select the region closest to your users or workloads.  
**Primary service** | Select the primary service, such as Azure Blob Storage or Azure Data Lake Storage Gen2.  
**Performance** | Select **Standard** (recommended for most scenarios) or **Premium** (for low-latency workloads).  
**Redundancy** | Select the replication option based on your availability requirements (for example, **Locally-redundant storage (LRS)**).  
  4. Click **Review + create**.

  5. After validation passes, click **Create** to deploy the Storage Account.


**Note:** Storage Account names must be globally unique across all Azure customers. Choose a name that is meaningful, concise, and follows Azure naming conventions (3–24 lowercase alphanumeric characters).

## Set up Microsoft Defender for Endpoint

  1. Sign in to [security.microsoft.com](https://security.microsoft.com) as a global administrator or security administrator.
  2. In the left pane, click **Settings**.
  3. Select the **Microsoft Defender XDR** tab.
  4. Select **Streaming API** from the general section and click **Add**.
  5. Select **Forward events to Azure Storage**.
  6. Navigate to the storage account of your choice.
  7. Select **Overview > JSON View** and enter the **Resource ID**.
  8. After you enter the resource ID, select all the required data types.
  9. Click **Save**.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the Microsoft Defender for Endpoint feed

  1. Click the **Microsoft Defender** pack.
  2. Locate the **Microsoft Defender for Endpoint** log type.
  3. Specify values in the following fields:

     * **Source Type** : Microsoft Azure Blob Storage V2.
     * **Azure URI** : The URI pointing to an Azure Blob Storage blob or container.
     * **Source deletion option** : whether to delete files or directories after transferring.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * Select **Shared key** or **SAS token**.
     * **Key** : The shared key or SAS token to access Azure resources.
**Caution:** To avoid **HTTP 429 (Too Many Requests)** errors and ingestion delays, don't reuse the same shared key or storage account across multiple feeds.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : Namespace associated with the feed.
     * **Ingestion Labels** : Labels applied to all events from this feed.
  4. Click **Create feed**.


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## Supported Microsoft Defender for Endpoint log types

The Microsoft Defender for Endpoint parser supports the following tables: 

  * AlertEvidence
  * AlertInfo
  * CloudAppEvents
  * DeviceAlertEvents
  * DeviceEvents
  * DeviceFileCertificateInfo
  * DeviceFileEvents
  * DeviceImageLoadEvents
  * DeviceInfo
  * DeviceLogonEvents
  * DeviceNetworkEvents
  * DeviceNetworkInfo
  * DeviceProcessEvents
  * DeviceRegistryEvents
  * DeviceTvmInfoGathering
  * DeviceTvmInfoGatheringKB
  * DeviceTvmSecureConfigurationAssessment
  * DeviceTvmSecureConfigurationAssessmentKB
  * DeviceTvmSoftwareEvidenceBeta
  * DeviceTvmSoftwareInventory
  * DeviceTvmSoftwareVulnerabilities
  * DeviceTvmSoftwareVulnerabilitiesKB
  * EmailAttachmentInfo
  * EmailEvents
  * EmailPostDeliveryEvents
  * EmailUrlInfo
  * IdentityInfo
  * IdentityLogonEvents



## Supported Microsoft Defender for Endpoint log formats

The Microsoft Defender for Endpoint parser supports logs in JSON format.

## Supported Microsoft Defender for Endpoint sample logs

  * JSON:
        
        {
          "time": "2021-07-16T09:57:38.1599837Z",
          "tenantId": "ed236696-8612-40d7-8b49-xxxxxxxxxxx",
          "operationName": "Publish",
          "category": "AdvancedHunting-DeviceInfo",
          "properties": {
            "OSBuild": null,
            "RegistryDeviceTag": null,
            "IsAzureADJoined": null,
            "PublicIP": "198.51.100.0",
            "OSArchitecture": null,
            "OSVersion": null,
            "OSPlatform": null,
            "LoggedOnUsers": "[{\\"UserName\\":\\"bob\\",\\"DomainName\\":\\"DESKTOP-BOB\\",\\"Sid\\":\\"S-1-5-21-1695909852-106810125-1651530144-1001\\"}]",
            "AdditionalFields": "{\\"IsLocalLogon\\":true}",
            "DeviceObjectId": null,
            "DeviceId": "e93c25ad74cc1dd30afeb642696a2559824589e5",
            "MachineGroup": null,
            "Timestamp": "2021-07-16T09:54:41.0662159Z",
            "DeviceName": "desktop-dummy",
            "ReportId": 193010,
            "ClientVersion": "10.7431.19041.746"
          }
        }
        




## Field mapping reference

This section explains how the Google Security Operations parser maps Microsoft Defender for Endpoint fields to Google Security Operations UDM fields. 

### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - Common Fields for UDM Event Model 

The following table lists the common log fields for the `MICROSOFT_DEFENDER_ENDPOINT` log type and their corresponding UDM fields:   
  


Common log field | UDM mapping | Logic  
---|---|---  
`time` | `metadata.collected_timestamp` |   
`category` | `metadata.product_event_type` |   
`` | `metadata.product_name` | The `metadata.product_name` UDM field is set to `Microsoft Defender for Endpoint`.  
`` | `metadata.vendor_name` | The `metadata.vendor_name` UDM field is set to `Microsoft`.  
`Tenant` | `observer.resource_ancestors.name` |   
`tenantId` | `observer.resource_ancestors.product_object_id` |   
`operationName` | `additional.fields[operation_name]` |   
`properties.ActionType` | `security_result.summary` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - Common Fields for UDM Entity Model

The following table lists the common log fields for the `MICROSOFT_DEFENDER_ENDPOINT` log type and their corresponding UDM fields:   
  


Common log field | UDM mapping | Logic  
---|---|---  
`` | `metadata.vendor_name` | The `metadata.vendor_name` UDM field is set to `Microsoft`.  
`` | `metadata.product_name` | The `metadata.product_name` UDM field is set to `Microsoft Defender for Endpoint`.  
`time` | `metadata.collected_timestamp` |   
`tenantId` | `relations.entity.resource.product_object_id` |   
`operationName` | `additional.fields[operation_name]` |   
`category` | `metadata.description` |   
`Tenant` | `relations.entity.resource.name` |   
`` | `relations.entity_type` | The `relations.entity_type` UDM field is set to `RESOURCE`.  
`` | `relations.relationship` | The `relations.relationship` UDM field is set to `MEMBER`.  
`` | `relations.direction` | The `relations.direction` UDM field is set to `UNIDIRECTIONAL`.  
  
### Field mapping reference: DeviceEvents Event Identifier to Event Type

The following table lists the `DeviceEvents` log action types and their corresponding UDM event types. 

Event Identifier | Event Type  
---|---  
`AntivirusDefinitionsUpdated` | `SCAN_HOST`  
`AntivirusDefinitionsUpdateFailed` | `SETTING_MODIFICATION`  
`AntivirusDetection` | `SCAN_HOST`  
`AntivirusDetectionActionType` | `SCAN_HOST`  
`AntivirusEmergencyUpdatesInstalled` | `SETTING_MODIFICATION`  
`AntivirusError` | `SCAN_HOST`  
`AntivirusMalwareActionFailed` | `SCAN_HOST`  
`AntivirusMalwareBlocked` | `SCAN_HOST`  
`AntivirusReport` | `SCAN_HOST`  
`AntivirusScanCancelled` | `SCAN_HOST`  
`AntivirusScanCompleted` | `SCAN_HOST`  
`AntivirusScanFailed` | `SCAN_HOST`  
`AntivirusTroubleshootModeEvent` | `STATUS_UPDATE`  
`AppControlAppInstallationAudited` | `SCAN_HOST`  
`AppControlAppInstallationBlocked` | `SCAN_HOST`  
`AppControlCIScriptAudited` | `SCAN_HOST`  
`AppControlCIScriptBlocked` | `SCAN_HOST`  
`AppControlCodeIntegrityDriverRevoked` | `SCAN_FILE`  
`AppControlCodeIntegrityImageAudited` | `SCAN_FILE`  
`AppControlCodeIntegrityImageRevoked` | `SCAN_FILE`  
`AppControlCodeIntegrityOriginAllowed` | `SCAN_FILE`  
`AppControlCodeIntegrityOriginAudited` | `SCAN_FILE`  
`AppControlCodeIntegrityOriginBlocked` | `SCAN_FILE`  
`AppControlCodeIntegrityPolicyAudited` | `SCAN_FILE`  
`AppControlCodeIntegrityPolicyBlocked` | `SCAN_FILE`  
`AppControlCodeIntegrityPolicyLoaded` | `SCAN_FILE`  
`AppControlCodeIntegritySigningInformation` | `GENERIC_EVENT`  
`AppControlExecutableAudited` | `SCAN_HOST`  
`AppControlExecutableBlocked` | `SCAN_HOST`  
`AppControlPackagedAppAudited` | `SCAN_HOST`  
`AppControlPackagedAppBlocked` | `SCAN_HOST`  
`AppControlPolicyApplied` | `SETTING_MODIFICATION`  
`AppControlScriptAudited` | `SCAN_HOST`  
`AppControlScriptBlocked` | `SCAN_HOST`  
`AppGuardBrowseToUrl` | `NETWORK_UNCATEGORIZED`  
`AppGuardCreateContainer` | `PROCESS_LAUNCH`  
`AppGuardLaunchedWithUrl` | `PROCESS_LAUNCH`  
`AppGuardResumeContainer` | `PROCESS_UNCATEGORIZED`  
`AppGuardStopContainer` | `PROCESS_TERMINATION`  
`AppGuardSuspendContainer` | `PROCESS_UNCATEGORIZED`  
`AppLockerBlockExecutable` | `SCAN_HOST`  
`AppLockerBlockPackagedApp` | `SCAN_HOST`  
`AppLockerBlockPackagedAppInstallation` | `SCAN_HOST`  
`AppLockerBlockScript` | `SCAN_HOST`  
`AsrAbusedSystemToolAudited` | `SCAN_HOST`  
`AsrAbusedSystemToolBlocked` | `SCAN_HOST`  
`AsrAbusedSystemToolWarnBypassed` | `SCAN_HOST`  
`AsrAdobeReaderChildProcessAudited` | `SCAN_HOST`  
`AsrAdobeReaderChildProcessBlocked` | `SCAN_HOST`  
`AsrAdobeReaderChildProcessWarnBypassed` | `SCAN_HOST`  
`AsrExecutableEmailContentAudited` | `SCAN_HOST`  
`AsrExecutableEmailContentBlocked` | `SCAN_HOST`  
`AsrExecutableEmailContentWarnBypassed` | `SCAN_HOST`  
`AsrExecutableOfficeContentAudited` | `SCAN_HOST`  
`AsrExecutableOfficeContentBlocked` | `SCAN_HOST`  
`AsrExecutableOfficeContentWarnBypassed` | `SCAN_HOST`  
`AsrLsassCredentialTheftAudited` | `SCAN_HOST`  
`AsrLsassCredentialTheftBlocked` | `SCAN_HOST`  
`AsrLsassCredentialTheftWarnBypassed` | `SCAN_HOST`  
`AsrObfuscatedScriptAudited` | `SCAN_HOST`  
`AsrObfuscatedScriptBlocked` | `SCAN_HOST`  
`AsrObfuscatedScriptWarnBypassed` | `SCAN_HOST`  
`AsrOfficeChildProcessAudited` | `SCAN_HOST`  
`AsrOfficeChildProcessBlocked` | `SCAN_HOST`  
`AsrOfficeChildProcessWarnBypassed` | `SCAN_HOST`  
`AsrOfficeCommAppChildProcessAudited` | `SCAN_HOST`  
`AsrOfficeCommAppChildProcessBlocked` | `SCAN_HOST`  
`AsrOfficeCommAppChildProcessWarnBypassed` | `SCAN_HOST`  
`AsrOfficeMacroWin32ApiCallsAudited` | `SCAN_HOST`  
`AsrOfficeMacroWin32ApiCallsBlocked` | `SCAN_HOST`  
`AsrOfficeMacroWin32ApiCallsWarnBypassed` | `SCAN_HOST`  
`AsrOfficeProcessInjectionAudited` | `SCAN_HOST`  
`AsrOfficeProcessInjectionBlocked` | `SCAN_HOST`  
`AsrOfficeProcessInjectionWarnBypassed` | `SCAN_HOST`  
`AsrPersistenceThroughWmiAudited` | `SCAN_HOST`  
`AsrPersistenceThroughWmiBlocked` | `SCAN_HOST`  
`AsrPersistenceThroughWmiWarnBypassed` | `SCAN_HOST`  
`AsrPsexecWmiChildProcessAudited` | `SCAN_HOST`  
`AsrPsexecWmiChildProcessBlocked` | `SCAN_HOST`  
`AsrPsexecWmiChildProcessWarnBypassed` | `SCAN_HOST`  
`AsrRansomwareAudited` | `SCAN_HOST`  
`AsrRansomwareBlocked` | `SCAN_HOST`  
`AsrRansomwareWarnBypassed` | `SCAN_HOST`  
`AsrSafeModeRebootAudited` | `SCAN_HOST`  
`AsrSafeModeRebootBlocked` | `SCAN_HOST`  
`AsrSafeModeRebootWarnBypassed` | `SCAN_HOST`  
`AsrScriptExecutableDownloadAudited` | `SCAN_HOST`  
`AsrScriptExecutableDownloadBlocked` | `SCAN_HOST`  
`AsrScriptExecutableDownloadWarnBypassed` | `SCAN_HOST`  
`AsrUntrustedExecutableAudited` | `SCAN_HOST`  
`AsrUntrustedExecutableBlocked` | `SCAN_HOST`  
`AsrUntrustedExecutableWarnBypassed` | `SCAN_HOST`  
`AsrUntrustedUsbProcessAudited` | `SCAN_HOST`  
`AsrUntrustedUsbProcessBlocked` | `SCAN_HOST`  
`AsrUntrustedUsbProcessWarnBypassed` | `SCAN_HOST`  
`AsrVulnerableSignedDriverAudited` | `SCAN_HOST`  
`AsrVulnerableSignedDriverBlocked` | `SCAN_HOST`  
`AsrVulnerableSignedDriverWarnBypassed` | `SCAN_HOST`  
`AsrWebShellOnServerAudited` | `SCAN_HOST`  
`AsrWebShellOnServerBlocked` | `SCAN_HOST`  
`AsrWebShellWarnBypassed` | `SCAN_HOST`  
`AuditPolicyModification` | `SETTING_MODIFICATION`  
`BitLockerAuditCompleted` | `STATUS_UPDATE`  
`BluetoothPolicyTriggered` | `SCAN_HOST`  
`BrowserLaunchedToOpenUrl` | `NETWORK_UNCATEGORIZED`  
`BruteForceActivityDetected` | `USER_LOGIN`  
`ClrUnbackedModuleLoaded` | `PROCESS_MODULE_LOAD`  
`ContainedDeviceConnectionBlocked` | `NETWORK_CONNECTION`  
`ControlFlowGuardViolation` | `SCAN_HOST`  
`ControlledFolderAccessViolationAudited` | `SCAN_FILE`  
`ControlledFolderAccessViolationBlocked` | `SCAN_FILE`  
`CreateRemoteThreadApiCall` | `PROCESS_UNCATEGORIZED`  
`CredentialsBackup` | `SERVICE_START`  
`DeviceBootAttestationInfo` | `GENERIC_EVENT`  
`DirectoryServiceObjectCreated` | `RESOURCE_CREATION`  
`DirectoryServiceObjectModified` | `RESOURCE_WRITTEN`  
`DlpPocPrintJob` | `FILE_UNCATEGORIZED`  
`DnsQueryRequest` | `NETWORK_DNS`  
`DnsQueryResponse` | `NETWORK_DNS`  
`DpapiAccessed` | `PROCESS_UNCATEGORIZED`  
`DriverLoad` | `PROCESS_MODULE_LOAD`  
`ExploitGuardAcgAudited` | `SCAN_HOST`  
`ExploitGuardAcgEnforced` | `SCAN_HOST`  
`ExploitGuardChildProcessAudited` | `SCAN_HOST`  
`ExploitGuardChildProcessBlocked` | `SCAN_HOST`  
`ExploitGuardEafViolationAudited` | `SCAN_HOST`  
`ExploitGuardEafViolationBlocked` | `SCAN_HOST`  
`ExploitGuardIafViolationAudited` | `SCAN_HOST`  
`ExploitGuardIafViolationBlocked` | `SCAN_HOST`  
`ExploitGuardLowIntegrityImageAudited` | `SCAN_HOST`  
`ExploitGuardLowIntegrityImageBlocked` | `SCAN_HOST`  
`ExploitGuardNetworkProtectionAudited` | `SCAN_HOST`  
`ExploitGuardNetworkProtectionBlocked` | `SCAN_HOST`  
`ExploitGuardNonMicrosoftSignedAudited` | `SCAN_HOST`  
`ExploitGuardNonMicrosoftSignedBlocked` | `SCAN_HOST`  
`ExploitGuardRopExploitAudited` | `SCAN_HOST`  
`ExploitGuardRopExploitBlocked` | `SCAN_HOST`  
`ExploitGuardSharedBinaryAudited` | `SCAN_HOST`  
`ExploitGuardSharedBinaryBlocked` | `SCAN_HOST`  
`ExploitGuardWin32SystemCallAudited` | `SCAN_HOST`  
`ExploitGuardWin32SystemCallBlocked` | `SCAN_HOST`  
`FileTimestampModificationEvent` | `FILE_MODIFICATION`  
`FirewallInboundConnectionBlocked` | `NETWORK_CONNECTION`  
`FirewallInboundConnectionToAppBlocked` | `NETWORK_CONNECTION`  
`FirewallOutboundConnectionBlocked` | `NETWORK_CONNECTION`  
`FirewallServiceStopped` | `SERVICE_STOP`  
`GetAsyncKeyStateApiCall` | `PROCESS_UNCATEGORIZED`  
`GetClipboardData` | `PROCESS_UNCATEGORIZED`  
`LdapSearch` | `RESOURCE_READ`  
`LogonRightsSettingEnabled` | `USER_CHANGE_PERMISSIONS`  
`MemoryRemoteProtect` | `PROCESS_UNCATEGORIZED`  
`NamedPipeEvent` | `PROCESS_UNCATEGORIZED`  
`NetworkProtectionUserBypassEvent` | `NETWORK_UNCATEGORIZED`  
`NetworkShareObjectAccessChecked` | `RESOURCE_READ`  
`NetworkShareObjectAdded` | `RESOURCE_CREATION`  
`NetworkShareObjectDeleted` | `RESOURCE_DELETION`  
`NetworkShareObjectModified` | `RESOURCE_WRITTEN`  
`NtAllocateVirtualMemoryApiCall` | `PROCESS_UNCATEGORIZED`  
`NtAllocateVirtualMemoryRemoteApiCall` | `PROCESS_UNCATEGORIZED`  
`NtMapViewOfSectionRemoteApiCall` | `PROCESS_UNCATEGORIZED`  
`NtProtectVirtualMemoryApiCall` | `PROCESS_UNCATEGORIZED`  
`OpenProcessApiCall` | `PROCESS_OPEN`  
`OtherAlertRelatedActivity` | `STATUS_UPDATE`  
`PasswordChangeAttempt` | `USER_CHANGE_PASSWORD`  
`PlistPropertyModified` | `FILE_MODIFICATION`  
`PnpDeviceAllowed` | `SCAN_HOST`  
`PnpDeviceBlocked` | `SCAN_HOST`  
`PnpDeviceConnected` | `DEVICE_CONFIG_UPDATE`  
`PowerShellCommand` | `PROCESS_LAUNCH`  
`PrintJobBlocked` | `SCAN_UNCATEGORIZED`  
`ProcessCreatedUsingWmiQuery` | `PROCESS_LAUNCH`  
`ProcessPrimaryTokenModified` | `PROCESS_UNCATEGORIZED`  
`PTraceDetected` | `PROCESS_UNCATEGORIZED`  
`QueueUserApcRemoteApiCall` | `PROCESS_UNCATEGORIZED`  
`ReadProcessMemoryApiCall` | `PROCESS_UNCATEGORIZED`  
`RemoteDesktopConnection` | `NETWORK_CONNECTION`  
`RemoteWmiOperation` | `PROCESS_UNCATEGORIZED`  
`RemovableStorageFileEvent` | `FILE_UNCATEGORIZED`  
`RemovableStoragePolicyTriggered` | `PROCESS_UNCATEGORIZED`  
`SafeDocFileScan` | `SCAN_FILE`  
`ScheduledTaskCreated` | `SCHEDULED_TASK_CREATION`  
`ScheduledTaskDeleted` | `SCHEDULED_TASK_DELETION`  
`ScheduledTaskDisabled` | `SCHEDULED_TASK_DISABLE`  
`ScheduledTaskEnabled` | `SCHEDULED_TASK_ENABLE`  
`ScheduledTaskUpdated` | `SCHEDULED_TASK_MODIFICATION`  
`ScreenshotTaken` | `GENERIC_EVENT`  
`ScriptContent` | `PROCESS_LAUNCH`  
`SecurityGroupCreated` | `GROUP_CREATION`  
`SecurityGroupDeleted` | `GROUP_DELETION`  
`SecurityLogCleared` | `SYSTEM_AUDIT_LOG_WIPE`  
`SensitiveFileRead` | `FILE_READ`  
`ServiceInstalled` | `SERVICE_CREATION`  
`SetThreadContextRemoteApiCall` | `PROCESS_UNCATEGORIZED`  
`ShellLinkCreateFileEvent` | `FILE_CREATION`  
`SmartScreenAppWarning` | `SCAN_HOST`  
`SmartScreenExploitWarning` | `SCAN_HOST`  
`SmartScreenUrlWarning` | `SCAN_HOST`  
`SmartScreenUserOverride` | `SETTING_MODIFICATION`  
`TamperingAttempt` | `SETTING_MODIFICATION`  
`TvmAxonTelemetryEvent` | `STATUS_UPDATE`  
`UntrustedWifiConnection` | `NETWORK_CONNECTION`  
`UsbDriveDriveLetterChanged` | `DEVICE_CONFIG_UPDATE`  
`UsbDriveMounted` | `DEVICE_CONFIG_UPDATE`  
`UsbDriveUnmounted` | `DEVICE_CONFIG_UPDATE`  
`UserAccountAddedToLocalGroup` | `GROUP_MODIFICATION`  
`UserAccountCreated` | `USER_CREATION`  
`UserAccountDeleted` | `USER_DELETION`  
`UserAccountModified` | `USER_UNCATEGORIZED`  
`UserAccountRemovedFromLocalGroup` | `GROUP_MODIFICATION`  
`WmiBindEventFilterToConsumer` | `PROCESS_UNCATEGORIZED`  
`WriteProcessMemoryApiCall` | `PROCESS_UNCATEGORIZED`  
`WriteToLsassProcessMemory` | `PROCESS_UNCATEGORIZED`  
`AccountCheckedForBlankPassword` | `SCAN_UNCATEGORIZED`  
`AmsiScriptDetection` | `PROCESS_UNCATEGORIZED`  
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceEvents

The following table lists the log fields for the `DeviceEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.Timestamp` | `metadata.event_timestamp` |   
`properties.ActionType` | `metadata.event_type` |   
`properties.ReportId` | `metadata.product_log_id` |   
`properties.LogonId` | `network.session_id` |   
`properties.InitiatingProcessSessionId` | `additional.fields[initiating_process_session_id]` |   
`properties.IsInitiatingProcessRemoteSession` | `additional.fields[is_initiating_process_remote_session]` |   
`properties.InitiatingProcessRemoteSessionIP` | `src.ip` |   
`properties.InitiatingProcessRemoteSessionIP` | `src.asset.ip` |   
`properties.ProcessRemoteSessionIP` | `src.ip` |   
`properties.ProcessRemoteSessionIP` | `src.asset.ip` |   
`properties.CreatedProcessSessionId` | `additional.fields[created_process_session_id]` |   
`properties.IsProcessRemoteSession` | `additional.fields[is_process_remote_session]` |   
`` | `extensions.auth.mechanism` | The `extensions.auth.mechanism` UDM field is set to `MECHANISM_UNSPECIFIED`.  
`properties.InitiatingProcessRemoteSessionDeviceName` | `src.hostname` | If `properties.InitiatingProcessRemoteSessionDeviceName` log field is not empty, then `properties.InitiatingProcessRemoteSessionDeviceName` log field is mapped to `src.hostname` UDM field.  
`properties.InitiatingProcessRemoteSessionDeviceName` | `src.asset.hostname` | If `properties.InitiatingProcessRemoteSessionDeviceName` log field is not empty, then `properties.InitiatingProcessRemoteSessionDeviceName` log field is mapped to `src.asset.hostname` UDM field.  
`properties.ProcessRemoteSessionDeviceName` | `src.hostname` | If `properties.InitiatingProcessRemoteSessionDeviceName` log field is empty, then `properties.ProcessRemoteSessionDeviceName` log field is mapped to `src.hostname` UDM field.  
`properties.ProcessRemoteSessionDeviceName` | `src.asset.hostname` | If `properties.InitiatingProcessRemoteSessionDeviceName` log field is empty, then `properties.ProcessRemoteSessionDeviceName` log field is mapped to `src.asset.hostname` UDM field.  
`properties.ActionType` | `network.application_protocol` | If the `properties.ActionType` log field contains one of the following values, then the `network.application_protocol` UDM field is set to `DNS`:

  * `DnsQueryRequest`
  * `DnsQueryResponse`

  
`properties.ActionType` | `target.resource.resource_type` | If the `properties.ActionType` log field contains one of the following values:

  * `AntivirusDefinitionsUpdateFailed`
  * `AntivirusEmergencyUpdatesInstalled`
  * `AppControlPolicyApplied`
  * `AuditPolicyModification`
  * `FirewallServiceStopped`
  * `SmartScreenUserOverride`
  * `TamperingAttempt`

then the `target.resource.resource_type` UDM field is set to `SETTING`.  
Otherwise, if the `properties.ActionType` log field contains one of the following values:

  * `ScheduledTaskCreated`
  * `ScheduledTaskDeleted`
  * `ScheduledTaskDisabled`
  * `ScheduledTaskEnabled`
  * `ScheduledTaskUpdated`

then the `target.resource.resource_type` UDM field is set to `TASK`.  
Otherwise, if the `properties.ActionType` log field contains one of the following values:

  * `DirectoryServiceObjectCreated`
  * `DirectoryServiceObjectModified`
  * `NetworkShareObjectAccessChecked`
  * `NetworkShareObjectAdded`
  * `NetworkShareObjectDeleted`
  * `NetworkShareObjectModified`

then the `target.resource.resource_type` UDM field is set to `STORAGE_OBJECT`.  
Otherwise, if the `properties.ActionType` log field contains one of the following values:

  * `ExploitGuardNetworkProtectionAudited`
  * `ExploitGuardNetworkProtectionBlocked`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrExecutableEmailContentAudited`
  * `AsrExecutableOfficeContentAudited`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrScriptExecutableDownloadAudited`
  * `AsrUntrustedExecutableAudited`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrWebShellOnServerAudited`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardLowIntegrityImageAudited`
  * `ExploitGuardNonMicrosoftSignedAudited`
  * `ExploitGuardSharedBinaryAudited`
  * `AppControlCIScriptBlocked`
  * `AppControlExecutableBlocked`
  * `AppControlPackagedAppBlocked`
  * `AppControlScriptBlocked`
  * `AppLockerBlockExecutable`
  * `AppLockerBlockPackagedApp`
  * `AppLockerBlockPackagedAppInstallation`
  * `AppLockerBlockScript`
  * `AsrAbusedSystemToolBlocked`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrExecutableEmailContentBlocked`
  * `AsrExecutableOfficeContentBlocked`
  * `AsrLsassCredentialTheftBlocked`
  * `AsrObfuscatedScriptBlocked`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeMacroWin32ApiCallsBlocked`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrPersistenceThroughWmiBlocked`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrRansomwareBlocked`
  * `AsrSafeModeRebootBlocked`
  * `AsrScriptExecutableDownloadBlocked`
  * `AsrUntrustedExecutableBlocked`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrVulnerableSignedDriverBlocked`
  * `AsrWebShellOnServerBlocked`
  * `ControlFlowGuardViolation`
  * `ExploitGuardAcgEnforced`
  * `ExploitGuardChildProcessBlocked`
  * `ExploitGuardEafViolationBlocked`
  * `ExploitGuardIafViolationBlocked`
  * `ExploitGuardLowIntegrityImageBlocked`
  * `ExploitGuardNonMicrosoftSignedBlocked`
  * `ExploitGuardRopExploitBlocked`
  * `ExploitGuardSharedBinaryBlocked`
  * `ExploitGuardWin32SystemCallBlocked`
  * `AppControlAppInstallationBlocked`
  * `AppControlAppInstallationAudited`
  * `AppControlCIScriptAudited`
  * `AppControlExecutableAudited`
  * `AppControlPackagedAppAudited`
  * `AppControlScriptAudited`
  * `AsrAbusedSystemToolAudited`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrLsassCredentialTheftAudited`
  * `AsrObfuscatedScriptAudited`
  * `AsrOfficeMacroWin32ApiCallsAudited`
  * `AsrPersistenceThroughWmiAudited`
  * `AsrRansomwareAudited`
  * `AsrSafeModeRebootAudited`
  * `AsrVulnerableSignedDriverAudited`
  * `ExploitGuardEafViolationAudited`
  * `ExploitGuardIafViolationAudited`
  * `ExploitGuardRopExploitAudited`
  * `ExploitGuardWin32SystemCallAudited`
  * `ExploitGuardAcgAudited`
  * `PnpDeviceAllowed`
  * `PnpDeviceBlocked`
  * `AntivirusDetection`
  * `AntivirusDetectionActionType`
  * `AntivirusMalwareActionFailed`
  * `AntivirusMalwareBlocked`
  * `AntivirusReport`
  * `AntivirusScanCancelled`
  * `AntivirusScanCompleted`
  * `AntivirusScanFailed`
  * `SmartScreenAppWarning`
  * `SmartScreenExploitWarning`
  * `SmartScreenUrlWarning`
  * `AntivirusError`
  * `AntivirusDefinitionsUpdated`
  * `AsrAbusedSystemToolWarnBypassed`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrExecutableEmailContentWarnBypassed`
  * `AsrExecutableOfficeContentWarnBypassed`
  * `AsrLsassCredentialTheftWarnBypassed`
  * `AsrObfuscatedScriptWarnBypassed`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeMacroWin32ApiCallsWarnBypassed`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPersistenceThroughWmiWarnBypassed`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrRansomwareWarnBypassed`
  * `AsrSafeModeRebootWarnBypassed`
  * `AsrScriptExecutableDownloadWarnBypassed`
  * `AsrUntrustedExecutableWarnBypassed`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `AsrVulnerableSignedDriverWarnBypassed`
  * `AsrWebShellWarnBypassed`
  * `BluetoothPolicyTriggered`
  * `PnpDeviceConnected`

then the `target.resource.resource_type` UDM field is set to `DEVICE`.  
`properties.DeviceId` | `principal.asset_id` | If the `properties.ActionType` log field contains one of the following values, then `DeviceID:%{properties.DeviceId}` is mapped to the `target.asset_id` and `target.asset.asset_id` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, `DeviceID:%{properties.DeviceId}` is mapped to the `principal.asset_id` and `principal.asset.asset_id` UDM fields.  
`properties.DeviceId` | `principal.asset.asset_id` | If the `properties.ActionType` log field contains one of the following values, then `DeviceID:%{properties.DeviceId}` is mapped to the `target.asset_id` and `target.asset.asset_id` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, `DeviceID:%{properties.DeviceId}` is mapped to the `principal.asset_id` and `principal.asset.asset_id` UDM fields.  
`properties.DeviceId` | `target.asset_id` | If the `properties.ActionType` log field contains one of the following values, then `DeviceID:%{properties.DeviceId}` is mapped to the `target.asset_id` and `target.asset.asset_id` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, `DeviceID:%{properties.DeviceId}` is mapped to the `principal.asset_id` and `principal.asset.asset_id` UDM fields.  
`properties.DeviceId` | `target.asset.asset_id` | If the `properties.ActionType` log field contains one of the following values, then `DeviceID:%{properties.DeviceId}` is mapped to the `target.asset_id` and `target.asset.asset_id` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, `DeviceID:%{properties.DeviceId}` is mapped to the `principal.asset_id` and `principal.asset.asset_id` UDM fields.  
`properties.InitiatingProcessAccountDomain` | `principal.administrative_domain` | If the `properties.ActionType` log field contains one of the following values and the `properties.InitiatingProcessAccountDomain` log field value is _not_ empty, then the `properties.InitiatingProcessAccountDomain` log field is mapped to the `target.administrative_domain` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, if the `properties.InitiatingProcessAccountDomain` log field value is _not_ empty, then the `properties.InitiatingProcessAccountDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
`properties.InitiatingProcessAccountDomain` | `target.administrative_domain` | If the `properties.ActionType` log field contains one of the following values and the `properties.InitiatingProcessAccountDomain` log field value is _not_ empty, then the `properties.InitiatingProcessAccountDomain` log field is mapped to the `target.administrative_domain` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, if the `properties.InitiatingProcessAccountDomain` log field value is _not_ empty, then the `properties.InitiatingProcessAccountDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
`properties.AccountDomain` | `principal.administrative_domain` | If the `properties.ActionType` log field contains one of the following values:

  * `BruteForceActivityDetected`
  * `LogonRightsSettingEnabled`
  * `PasswordChangeAttempt`
  * `UserAccountCreated`
  * `UserAccountDeleted`
  * `UserAccountModified`

then if the `properties.AccountDomain` log field is _not_ empty, then it is mapped to the `target.administrative_domain` UDM field.  
  
Otherwise, if the `properties.InitiatingProcessAccountDomain` log field is _not_ empty and the `properties.AccountDomain` log field is _not_ empty, then the `properties.AccountDomain` log field is mapped to `additional.fields[AccountDomain]`.  
  
Otherwise, if the `properties.InitiatingProcessAccountDomain` log field is empty and the `properties.AccountDomain` log field is _not_ empty, then the `properties.AccountDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
`properties.AccountDomain` | `target.administrative_domain` | If the `properties.ActionType` log field contains one of the following values:

  * `BruteForceActivityDetected`
  * `LogonRightsSettingEnabled`
  * `PasswordChangeAttempt`
  * `UserAccountCreated`
  * `UserAccountDeleted`
  * `UserAccountModified`

then if the `properties.AccountDomain` log field is _not_ empty, then it is mapped to the `target.administrative_domain` UDM field.  
  
Otherwise, if the `properties.InitiatingProcessAccountDomain` log field is _not_ empty and the `properties.AccountDomain` log field is _not_ empty, then the `properties.AccountDomain` log field is mapped to `additional.fields[AccountDomain]`.  
  
Otherwise, if the `properties.InitiatingProcessAccountDomain` log field is empty and the `properties.AccountDomain` log field is _not_ empty, then the `properties.AccountDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
`properties.DeviceName` | `principal.hostname` | If the `properties.ActionType` log field contains one of the following values, then the `properties.DeviceName` log field is mapped to the `target.hostname` and `target.asset.hostname` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.DeviceName` log field is mapped to the `principal.hostname` and `principal.asset.hostname` UDM fields.  
`properties.DeviceName` | `principal.asset.hostname` | If the `properties.ActionType` log field contains one of the following values, then the `properties.DeviceName` log field is mapped to the `target.hostname` and `target.asset.hostname` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.DeviceName` log field is mapped to the `principal.hostname` and `principal.asset.hostname` UDM fields.  
`properties.DeviceName` | `target.hostname` | If the `properties.ActionType` log field contains one of the following values, then the `properties.DeviceName` log field is mapped to the `target.hostname` and `target.asset.hostname` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.DeviceName` log field is mapped to the `principal.hostname` and `principal.asset.hostname` UDM fields.  
`properties.DeviceName` | `target.asset.hostname` | If the `properties.ActionType` log field contains one of the following values, then the `properties.DeviceName` log field is mapped to the `target.hostname` and `target.asset.hostname` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.DeviceName` log field is mapped to the `principal.hostname` and `principal.asset.hostname` UDM fields.  
`properties.LocalIP` | `principal.ip` | If the `properties.ActionType` log field contains one of the following values, then the `properties.LocalIP` log field is mapped to the `target.ip` and `target.asset.ip` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.LocalIP` log field is mapped to the `principal.ip` and `principal.asset.ip` UDM fields.  
`properties.LocalIP` | `principal.asset.ip` | If the `properties.ActionType` log field contains one of the following values, then the `properties.LocalIP` log field is mapped to the `target.ip` and `target.asset.ip` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.LocalIP` log field is mapped to the `principal.ip` and `principal.asset.ip` UDM fields.  
`properties.LocalIP` | `target.ip` | If the `properties.ActionType` log field contains one of the following values, then the `properties.LocalIP` log field is mapped to the `target.ip` and `target.asset.ip` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.LocalIP` log field is mapped to the `principal.ip` and `principal.asset.ip` UDM fields.  
`properties.LocalIP` | `target.asset.ip` | If the `properties.ActionType` log field contains one of the following values, then the `properties.LocalIP` log field is mapped to the `target.ip` and `target.asset.ip` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.LocalIP` log field is mapped to the `principal.ip` and `principal.asset.ip` UDM fields.  
`properties.FileOriginIP` | `principal.ip` |   
`properties.FileOriginIP` | `principal.asset.ip` |   
`properties.LocalPort` | `principal.port` | If the `properties.ActionType` log field contains one of the following values, then the `properties.LocalPort` log field is mapped to the `target.port` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.LocalPort` log field is mapped to the `principal.port` UDM field.  
`properties.LocalPort` | `target.port` | If the `properties.ActionType` log field contains one of the following values, then the `properties.LocalPort` log field is mapped to the `target.port` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.LocalPort` log field is mapped to the `principal.port` UDM field.  
`properties.InitiatingProcessCommandLine` | `principal.process.command_line` |   
`properties.InitiatingProcessFolderPath` | `principal.process.file.full_path` | If the `properties.InitiatingProcessFolderPath` log field value matches the regular expression pattern the `properties.InitiatingProcessFileName` log field value, then the `properties.InitiatingProcessFolderPath` log field is mapped to the `principal.process.file.full_path` UDM field.  
  
Otherwise, the `principal.process.file.full_path` is set to `%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}`.  
`properties.InitiatingProcessMD5` | `principal.process.file.md5` | If the `properties.InitiatingProcessMD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessMD5` log field is mapped to the `principal.process.file.md5` UDM field.  
`properties.InitiatingProcessFileName` | `principal.process.file.names` |   
`properties.InitiatingProcessSHA1` | `principal.process.file.sha1` | If the `properties.InitiatingProcessSHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessSHA1` log field is mapped to the `principal.process.file.sha1` UDM field.  
`properties.InitiatingProcessSHA256` | `principal.process.file.sha256` | If the `properties.InitiatingProcessSHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.InitiatingProcessSHA256` log field is mapped to the `principal.process.file.sha256` UDM field.  
`properties.InitiatingProcessFileSize` | `principal.process.file.size` |   
`properties.InitiatingProcessParentFileName` | `principal.process.parent_process.file.names` |   
`properties.InitiatingProcessParentId` | `principal.process.parent_process.pid` |   
`properties.InitiatingProcessId` | `principal.process.pid` |   
`properties.FileOriginUrl` | `principal.url` |   
`properties.InitiatingProcessAccountObjectId` | `principal.user.product_object_id` |   
`properties.InitiatingProcessAccountUpn` | `principal.user.user_display_name` |   
`properties.InitiatingProcessAccountName` | `principal.user.userid` |   
`properties.AccountName` | `principal.user.userid` | If the `properties.ActionType` log field contains one of the following values:

  * `BruteForceActivityDetected`
  * `LogonRightsSettingEnabled`
  * `PasswordChangeAttempt`
  * `UserAccountCreated`
  * `UserAccountDeleted`
  * `UserAccountModified`

then if the `properties.AccountName` log field is _not_ empty, then it is mapped to the `target.user.userid` UDM field.  
  
Otherwise, if the `properties.InitiatingProcessAccountName` log field is _not_ empty and the `properties.AccountName` log field is _not_ empty, then the `properties.AccountName` log field is mapped to `additional.fields[AccountName]`.  
  
Otherwise, if the `properties.InitiatingProcessAccountName` log field is empty and the `properties.AccountName` log field is _not_ empty, then the `properties.AccountName` log field is mapped to the `principal.user.userid` UDM field.  
`properties.AccountName` | `target.user.userid` | If the `properties.ActionType` log field contains one of the following values:

  * `BruteForceActivityDetected`
  * `LogonRightsSettingEnabled`
  * `PasswordChangeAttempt`
  * `UserAccountCreated`
  * `UserAccountDeleted`
  * `UserAccountModified`

then if the `properties.AccountName` log field is _not_ empty, then it is mapped to the `target.user.userid` UDM field.  
  
Otherwise, if the `properties.InitiatingProcessAccountName` log field is _not_ empty and the `properties.AccountName` log field is _not_ empty, then the `properties.AccountName` log field is mapped to `additional.fields[AccountName]`.  
  
Otherwise, if the `properties.InitiatingProcessAccountName` log field is empty and the `properties.AccountName` log field is _not_ empty, then the `properties.AccountName` log field is mapped to the `principal.user.userid` UDM field.  
`properties.InitiatingProcessAccountSid` | `principal.user.windows_sid` |   
`properties.AccountSid` | `principal.user.windows_sid` | If the `properties.ActionType` log field contains one of the following values:

  * `BruteForceActivityDetected`
  * `LogonRightsSettingEnabled`
  * `PasswordChangeAttempt`
  * `UserAccountCreated`
  * `UserAccountDeleted`
  * `UserAccountModified`

then if the `properties.AccountSid` log field is _not_ empty, then it is mapped to the `target.user.windows_sid` UDM field.  
  
Otherwise, if the `properties.InitiatingProcessAccountSid` log field is _not_ empty and the `properties.AccountSid` log field is _not_ empty, then the `properties.AccountSid` log field is mapped to `additional.fields[AccountSid]`.  
  
Otherwise, if the `properties.InitiatingProcessAccountSid` log field is empty and the `properties.AccountSid` log field is _not_ empty, then the `properties.AccountSid` log field is mapped to the `principal.user.windows_sid` UDM field.  
`properties.AccountSid` | `target.user.windows_sid` | If the `properties.ActionType` log field contains one of the following values:

  * `BruteForceActivityDetected`
  * `LogonRightsSettingEnabled`
  * `PasswordChangeAttempt`
  * `UserAccountCreated`
  * `UserAccountDeleted`
  * `UserAccountModified`

then if the `properties.AccountSid` log field is _not_ empty, then it is mapped to the `target.user.windows_sid` UDM field.  
  
Otherwise, if the `properties.InitiatingProcessAccountSid` log field is _not_ empty and the `properties.AccountSid` log field is _not_ empty, then the `properties.AccountSid` log field is mapped to `additional.fields[AccountSid]`.  
  
Otherwise, if the `properties.InitiatingProcessAccountSid` log field is empty and the `properties.AccountSid` log field is _not_ empty, then the `properties.AccountSid` log field is mapped to the `principal.user.windows_sid` UDM field.  
`properties.ActionType` | `security_result.action` | If the `properties.ActionType` log field value matches the regular expression pattern `(?i)Allow`, then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, if the `properties.ActionType` log field value matches the regular expression pattern `(?i)Block`, then the `security_result.action` UDM field is set to `BLOCK`.  
  
Otherwise, if the `properties.ActionType` log field value matches the regular expression pattern `(?i)Fail`, then the `security_result.action` UDM field is set to `FAIL`.  
`properties.FolderPath` | `target.file.full_path` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

then if the `properties.FolderPath` log field value matches the regular expression pattern `the `properties.FileName` log field value `, then `properties.FolderPath` log field is mapped to the `target.process.file.full_path` UDM field, otherwise `%{properties.FolderPath}\%{properties.FileName}` is mapped to the `target.process.file.full_path` UDM field.  
Otherwise, if the `properties.FolderPath` log field value matches the regular expression pattern `the `properties.FileName` log field value `, then `properties.FolderPath` log field is mapped to the `target.file.full_path` UDM field, otherwise `%{properties.FolderPath}\%{properties.FileName}` is mapped to the `target.file.full_path` UDM field.  
`properties.FolderPath` | `target.process.file.full_path` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

then if the `properties.FolderPath` log field value matches the regular expression pattern `the `properties.FileName` log field value `, then `properties.FolderPath` log field is mapped to the `target.process.file.full_path` UDM field, otherwise `%{properties.FolderPath}\%{properties.FileName}` is mapped to the `target.process.file.full_path` UDM field.  
Otherwise, if the `properties.FolderPath` log field value matches the regular expression pattern `the `properties.FileName` log field value `, then `properties.FolderPath` log field is mapped to the `target.file.full_path` UDM field, otherwise `%{properties.FolderPath}\%{properties.FileName}` is mapped to the `target.file.full_path` UDM field.  
`properties.MD5` | `target.file.md5` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

and if the `properties.MD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.MD5` log field is mapped to the `target.process.file.md5` UDM field.  
Otherwise, if the `properties.MD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.MD5` log field is mapped to the `target.file.md5` UDM field.  
`properties.MD5` | `target.process.file.md5` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

and if the `properties.MD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.MD5` log field is mapped to the `target.process.file.md5` UDM field.  
Otherwise, if the `properties.MD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.MD5` log field is mapped to the `target.file.md5` UDM field.  
`properties.FileName` | `target.file.names` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

then `properties.FileName` log field is mapped to the `target.process.file.names` UDM field.  
Otherwise, `properties.FileName` log field is mapped to the `target.file.names` UDM field.  
`properties.FileName` | `target.process.file.names` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

then `properties.FileName` log field is mapped to the `target.process.file.names` UDM field.  
Otherwise, `properties.FileName` log field is mapped to the `target.file.names` UDM field.  
`properties.SHA1` | `target.file.sha1` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

and if the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then `properties.SHA1` log field is mapped to the `target.process.file.sha1` UDM field.  
Otherwise, if the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then `properties.SHA1` log field is mapped to the `target.file.sha1` UDM field.  
`properties.SHA1` | `target.process.file.sha1` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

and if the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then `properties.SHA1` log field is mapped to the `target.process.file.sha1` UDM field.  
Otherwise, if the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then `properties.SHA1` log field is mapped to the `target.file.sha1` UDM field.  
`properties.SHA256` | `target.file.sha256` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

and if the `properties.SHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then `properties.SHA256` log field is mapped to the `target.process.file.sha256` UDM field.  
Otherwise, if the `properties.SHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then `properties.SHA256` log field is mapped to the `target.file.sha256` UDM field.  
`properties.SHA256` | `target.process.file.sha256` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

and if the `properties.SHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then `properties.SHA256` log field is mapped to the `target.process.file.sha256` UDM field.  
Otherwise, if the `properties.SHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then `properties.SHA256` log field is mapped to the `target.file.sha256` UDM field.  
`properties.FileSize` | `target.file.size` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

then `properties.FileSize` log field is mapped to the `target.process.file.size` UDM field.  
Otherwise, `properties.FileSize` log field is mapped to the `target.file.size` UDM field.  
`properties.FileSize` | `target.process.file.size` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

then `properties.FileSize` log field is mapped to the `target.process.file.size` UDM field.  
Otherwise, `properties.FileSize` log field is mapped to the `target.file.size` UDM field.  
`properties.RemoteDeviceName` | `principal.hostname` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteDeviceName` log field is mapped to the `principal.hostname` and `principal.asset.hostname` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteDeviceName` log field is mapped to the `target.hostname` and `target.asset.hostname` UDM fields.  
`properties.RemoteDeviceName` | `principal.asset.hostname` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteDeviceName` log field is mapped to the `principal.hostname` and `principal.asset.hostname` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteDeviceName` log field is mapped to the `target.hostname` and `target.asset.hostname` UDM fields.  
`properties.RemoteDeviceName` | `target.hostname` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteDeviceName` log field is mapped to the `principal.hostname` and `principal.asset.hostname` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteDeviceName` log field is mapped to the `target.hostname` and `target.asset.hostname` UDM fields.  
`properties.RemoteDeviceName` | `target.asset.hostname` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteDeviceName` log field is mapped to the `principal.hostname` and `principal.asset.hostname` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteDeviceName` log field is mapped to the `target.hostname` and `target.asset.hostname` UDM fields.  
`properties.RemoteIP` | `principal.ip` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteIP` log field is mapped to the `principal.ip` and `principal.asset.ip` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteIP` log field is mapped to the `target.ip` and `target.asset.ip` UDM fields.  
`properties.RemoteIP` | `principal.asset.ip` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteIP` log field is mapped to the `principal.ip` and `principal.asset.ip` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteIP` log field is mapped to the `target.ip` and `target.asset.ip` UDM fields.  
`properties.RemoteIP` | `target.ip` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteIP` log field is mapped to the `principal.ip` and `principal.asset.ip` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteIP` log field is mapped to the `target.ip` and `target.asset.ip` UDM fields.  
`properties.RemoteIP` | `target.asset.ip` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteIP` log field is mapped to the `principal.ip` and `principal.asset.ip` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteIP` log field is mapped to the `target.ip` and `target.asset.ip` UDM fields.  
`properties.RemotePort` | `principal.port` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemotePort` log field is mapped to the `principal.port` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemotePort` log field is mapped to the `target.port` UDM field.  
`properties.RemotePort` | `target.port` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemotePort` log field is mapped to the `principal.port` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemotePort` log field is mapped to the `target.port` UDM field.  
`properties.ProcessCommandLine` | `target.process.command_line` |   
`properties.ProcessId` | `target.process.pid` |   
`properties.ProcessTokenElevation` | `target.process.token_elevation_type` | If the `properties.ProcessTokenElevation` log field value is equal to `TokenElevationTypeFull`, then the `target.process.token_elevation_type` UDM field is set to `TYPE_1`.  
  
Otherwise, if the `properties.ProcessTokenElevation` log field value is equal to `TokenElevationTypeDefault`, then the `target.process.token_elevation_type` UDM field is set to `TYPE_2`.  
  
Otherwise, if the `properties.ProcessTokenElevation` log field value is equal to `TokenElevationTypeLimited`, then the `target.process.token_elevation_type` UDM field is set to `TYPE_3`.  
`properties.RegistryKey` | `target.registry.registry_key` |   
`properties.RegistryValueData` | `target.registry.registry_value_data` |   
`properties.RegistryValueName` | `target.registry.registry_value_name` |   
`properties.RemoteUrl` | `principal.url` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteUrl` log field is mapped to the `principal.url` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteUrl` log field is mapped to the `target.url` UDM field.  
`properties.RemoteUrl` | `target.url` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteUrl` log field is mapped to the `principal.url` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteUrl` log field is mapped to the `target.url` UDM field.  
`properties.AdditionalFields` | `additional.fields[additional_fields]` |   
`properties.AppGuardContainerId` | `additional.fields[app_guard_container_id]` |   
`properties.InitiatingProcessCreationTime` | `additional.fields[initiating_process_creation_time]` |   
`properties.InitiatingProcessLogonId` | `additional.fields[initiating_process_logon_id]` |   
`properties.InitiatingProcessParentCreationTime` | `additional.fields[initiating_process_parent_creation_time]` |   
`properties.ProcessCreationTime` | `additional.fields[process_creation_time]` |   
`properties.InitiatingProcessVersionInfoCompanyName` | `principal.process.file.exif_info.company` |   
`properties.InitiatingProcessVersionInfoFileDescription` | `principal.process.file.exif_info.file_description` |   
`properties.InitiatingProcessVersionInfoInternalFileName` | `additional.fields[process_version_info_internal_file_name]` |   
`properties.InitiatingProcessVersionInfoOriginalFileName` | `principal.process.file.exif_info.original_file` |   
`properties.InitiatingProcessVersionInfoProductName` | `principal.process.file.exif_info.product` |   
`properties.InitiatingProcessVersionInfoProductVersion` | `additional.fields[process_version_info_product_version]` |   
`properties.ProcessUniqueId` | `additional.fields[ProcessUniqueId]` |   
`properties.InitiatingProcessUniqueId` | `additional.fields[InitiatingProcessUniqueId]` |   
`properties.MachineGroup` | `principal.asset.attribute.labels[MachineGroup]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - AlertEvidence

The following table lists the log fields for the `AlertEvidence` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.Application` | `principal.application` |   
`properties.ResourceType` | `principal.resource.attribute.labels[resource_type]` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `SCAN_HOST`.  
`properties.DeviceId`  
`properties.AdditionalFields.MachineId`  
`properties.AdditionalFields.Host.MachineId`  
`properties.AdditionalFields.ImageFile.Host.MachineId`  
`properties.AdditionalFields.ImageFile.Host.HostMachineId`  
`properties.AdditionalFields.Host.HostMachineId`  
`properties.AdditionalFields.Key.Device.MachineId`  
`properties.AdditionalFields.Key.Device.HostMachineId` | `principal.asset_id` | If the `properties.DeviceId` log field value is _not_ empty then, `DeviceID:properties.DeviceId` is mapped to the `principal.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.MachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.MachineId` is mapped to the `principal.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.Host.MachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.Host.MachineId` is mapped to the `principal.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.ImageFile.Host.MachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.ImageFile.Host.MachineId` is mapped to the `principal.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.ImageFile.Host.HostMachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.ImageFile.Host.HostMachineId` is mapped to the `principal.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.Host.HostMachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.Host.HostMachineId` is mapped to the `principal.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.Key.Device.MachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.Key.Device.MachineId` is mapped to the `principal.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.Key.Device.HostMachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.Key.Device.HostMachineId` is mapped to the `principal.asset_id` UDM field.  
`properties.DeviceId`  
`properties.AdditionalFields.MachineId`  
`properties.AdditionalFields.Host.MachineId`  
`properties.AdditionalFields.ImageFile.Host.MachineId`  
`properties.AdditionalFields.ImageFile.Host.HostMachineId`  
`properties.AdditionalFields.Host.HostMachineId`  
`properties.AdditionalFields.Key.Device.MachineId`  
`properties.AdditionalFields.Key.Device.HostMachineId` | `principal.asset.asset_id` | If the `properties.DeviceId` log field value is _not_ empty then, `DeviceID:properties.DeviceId` is mapped to the `principal.asset.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.MachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.MachineId` is mapped to the `principal.asset.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.Host.MachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.Host.MachineId` is mapped to the `principal.asset.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.ImageFile.Host.MachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.ImageFile.Host.MachineId` is mapped to the `principal.asset.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.ImageFile.Host.HostMachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.ImageFile.Host.HostMachineId` is mapped to the `principal.asset.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.Host.HostMachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.Host.HostMachineId` is mapped to the `principal.asset.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.Key.Device.MachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.Key.Device.MachineId` is mapped to the `principal.asset.asset_id` UDM field.   
Otherwise, if the `properties.AdditionalFields.Key.Device.HostMachineId` log field value is _not_ empty then, `DeviceID:properties.AdditionalFields.Key.Device.HostMachineId` is mapped to the `principal.asset.asset_id` UDM field.  
`properties.DeviceName`  
`properties.AdditionalFields.HostName`  
`properties.AdditionalFields.Host.HostName`  
`properties.AdditionalFields.ImageFile.Host.HostName`  
`properties.AdditionalFields.Key.Device.HostName` | `principal.hostname` | If the `properties.DeviceName` log field value is _not_ empty then, `properties.DeviceName` log field is mapped to the `principal.hostname` UDM field.   
Otherwise, if the `properties.AdditionalFields.HostName` log field value is _not_ empty then, `properties.AdditionalFields.HostName` log field is mapped to the `principal.hostname` UDM field.   
Otherwise, if the `properties.AdditionalFields.ImageFile.Host.HostName` log field value is _not_ empty then, `properties.AdditionalFields.ImageFile.Host.HostName` log field is mapped to the `principal.hostname` UDM field.   
Otherwise, if the `properties.AdditionalFields.Host.HostName` log field value is _not_ empty then, `properties.AdditionalFields.Host.HostName` log field is mapped to the `principal.hostname` UDM field.   
Otherwise, if the `properties.AdditionalFields.Key.Device.HostName` log field value is _not_ empty then, `properties.AdditionalFields.Key.Device.HostName` log field is mapped to the `principal.hostname` UDM field.  
  
`properties.DeviceName`  
`properties.AdditionalFields.HostName`  
`properties.AdditionalFields.Host.HostName`  
`properties.AdditionalFields.ImageFile.Host.HostName`  
`properties.AdditionalFields.Key.Device.HostName` | `principal.asset.hostname` | If the `properties.DeviceName` log field value is _not_ empty then, `properties.DeviceName` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise, if the `properties.AdditionalFields.HostName` log field value is _not_ empty then, `properties.AdditionalFields.HostName` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise, if the `properties.AdditionalFields.ImageFile.Host.HostName` log field value is _not_ empty then, `properties.AdditionalFields.ImageFile.Host.HostName` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise, if the `properties.AdditionalFields.Host.HostName` log field value is _not_ empty then, `properties.AdditionalFields.Host.HostName` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise, if the `properties.AdditionalFields.Key.Device.HostName` log field value is _not_ empty then, `properties.AdditionalFields.Key.Device.HostName` log field is mapped to the `principal.asset.hostname` UDM field.  
  
`properties.LocalIP` | `principal.asset.ip` | If the `properties.LocalIP` log field value is _not_ empty, then the `properties.LocalIP` log field is mapped to the `principal.asset.ip` UDM field.  
`properties.FolderPath` | `target.file.full_path` | If the `properties.FileName` log field value matches the regular expression pattern the `properties.FolderPath`, then the `properties.FolderPath` log field is mapped to the `target.file.full_path` UDM field.  
  
Otherwise, the `properties.FolderPath/properties.FileName` log field is mapped to the `target.file.full_path` UDM field.  
`properties.FileName` | `target.file.names` |   
`properties.SHA1` | `target.file.sha1` | If the `properties.SHA1` log field value matches the regular expression pattern `^the `0-9a-f` log field value+$`, then the `properties.SHA1` log field is mapped to the `target.file.sha1` UDM field.  
`properties.SHA256` | `target.file.sha256` | If the `properties.SHA256` log field value matches the regular expression pattern `^the `a-f0-9`, then 64$`, then the `properties.SHA256` log field is mapped to the `target.file.sha256` UDM field.  
`properties.FileSize` | `target.file.size` |   
`properties.AccountDomain` | `principal.administrative_domain` |   
`properties.RemoteIP` | `target.ip` |   
`properties.AdditionalFields` | `additional.fields[additionalfields]` |   
`properties.ProcessCommandLine` | `target.process.command_line` |   
`properties.RegistryKey` | `target.registry.registry_key` |   
`properties.RegistryValueData` | `target.registry.registry_value_data` |   
`properties.RegistryValueName` | `target.registry.registry_value_name` |   
`properties.CloudPlatform` | `principal.resource.attribute.cloud.environment` | If the `properties.CloudPlatform` log field value matches the regular expression pattern `/(?i)Amazon Web Services/`, then the `principal.resource.attribute.cloud.environment` UDM field is set to `AMAZON_WEB_SERVICES`.  
  
Otherwise, if the `properties.CloudPlatform` log field value matches the regular expression pattern `/(?i)Google Cloud Platform/`, then the `principal.resource.attribute.cloud.environment` UDM field is set to `GOOGLE_CLOUD_PLATFORM`.  
  
Otherwise, if the `properties.CloudPlatform` log field value matches one of the regular expression patterns `/(?i)Azure/` or `/(?i)Azure Arc/`, then the `principal.resource.attribute.cloud.environment` UDM field is set to `MICROSOFT_AZURE`.  
  
Otherwise, the `principal.resource.attribute.cloud.environment` UDM field is set to `UNSPECIFIED_CLOUD_ENVIRONMENT`.  
`properties.SubscriptionId` | `principal.resource.attribute.labels[subscription_id]` |   
`properties.CloudResource` | `principal.resource.name` |   
`properties.ResourceID` | `principal.resource.product_object_id` |   
`` | `principal.resource.resource_type` | The `principal.resource.resource_type` UDM field is set to `CLOUD_PROJECT`.  
`properties.Categories` | `security_result.category_details` |   
`properties.Severity` | `security_result.severity` |   
`properties.Title` | `security_result.threat_name` |   
`properties.ThreatFamily` | `security_result.detection_fields[threat_family]` |   
`properties.RemoteUrl` | `target.url` |   
`properties.EvidenceDirection` | `additional.fields[evidence_direction]` |   
`properties.EvidenceRole` | `additional.fields[evidence_role]` |   
`properties.AccountObjectId` | `additional.fields[account_object_id]` |   
`properties.AccountUpn` | `principal.user.user_display_name` |   
`properties.AccountName` | `principal.user.userid` |   
`properties.AccountSid` | `principal.user.windows_sid` |   
`properties.Timestamp` | `metadata.event_timestamp` |   
`properties.EntityType` | `principal.resource.resource_subtype` |   
`properties.AlertId` | `metadata.product_log_id` |   
`properties.DetectionSource` | `security_result.about.resource.attribute.labels[detection_source]` |   
`properties.ServiceSource` | `security_result.about.resource.attribute.labels[service_source]` |   
`properties.AttackTechniques` | `security_result.attack_details.techniques.name` |   
`properties.ApplicationId` | `additional.fields[application_id]` |   
`properties.EmailSubject` | `network.email.subject` |   
`properties.NetworkMessageId` | `network.email.mail_id` |   
`properties.OAuthApplicationId` | `additional.fields[oauth_application_id]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - AlertInfo

The following table lists the log fields for the `AlertInfo` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.Timestamp` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `GENERIC_EVENT`.  
`properties.AlertId` | `security_result.threat_id` |   
`properties.AttackTechniques` | `security_result.attack_details.techniques.name` |   
`properties.DetectionSource` | `security_result.detection_fields[detection_source]` |   
`properties.ServiceSource` | `principal.application` |   
`properties.Severity` | `security_result.severity` | If the `properties.Severity` log field value matches the regular expression pattern `(?i)(informational)`, then the `security_result.severity` UDM field is set to `INFORMATIONAL`.  
  
Otherwise, if the `properties.Severity` log field value matches the regular expression pattern `(?i)(low)`, then the `security_result.severity` UDM field is set to `LOW`.  
  
Otherwise, if the `properties.Severity` log field value matches the regular expression pattern `(?i)(medium)`, then the `security_result.severity` UDM field is set to `MEDIUM`.  
  
Otherwise, if the `properties.Severity` log field value matches the regular expression pattern `(?i)(high)`, then the `security_result.severity` UDM field is set to `HIGH`.  
`properties.Category` | `security_result.category_details` |   
`properties.Title` | `security_result.threat_name` |   
`properties.Title` | `security_result.rule_name` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceAlertEvents

The following table lists the log fields for the `DeviceAlertEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.Timestamp` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `SCAN_HOST`.  
`properties.ReportId` | `security_result.detection_fields[report_id]` |   
`properties.DeviceId` | `principal.asset_id` | The `principal.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.MachineGroup` | `principal.group.group_display_name` |   
`properties.DeviceName` | `principal.hostname` |   
`properties.AttackTechniques` | `security_result.attack_details.techniques.name` |   
`properties.Category` | `security_result.category_details` |   
`properties.AlertId` | `metadata.product_log_id` |   
`properties.MitreTechniques` | `security_result.detection_fields[mitre_techniques]` |   
`properties.Severity` | `security_result.severity` | If the `properties.Severity` log field value is equal to `High`, then the `security_result.severity` UDM field is set to `HIGH`.  
  
Otherwise, if the `properties.Severity` log field value is equal to `Medium`, then the `security_result.severity` UDM field is set to `MEDIUM`.  
  
Otherwise, if the `properties.Severity` log field value is equal to `Low`, then the `security_result.severity` UDM field is set to `LOW`.  
  
Otherwise, if the `properties.Severity` log field value is equal to `Informational`, then the `security_result.severity` UDM field is set to `INFORMATIONAL`.  
`properties.Title` | `security_result.threat_name` |   
`properties.Title` | `security_result.rule_name` |   
`properties.RemoteIp` | `target.ip` |   
`properties.FileName` | `target.file.names` |   
`properties.SHA1` | `target.file.sha1` | If the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.SHA1` log field is mapped to the `target.file.sha1` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `SHA1` and the `properties.SHA1` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.RemoteUrl` | `target.url` |   
`properties.Table` | `additional.fields[table]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceFileCertificateInfo 

The following table lists the log fields for the `DeviceFileCertificateInfo` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.Timestamp` | `metadata.creation_timestamp` |   
`` | `metadata.entity_type` | The `metadata.entity_type` UDM field is set to `FILE`.  
`properties.ReportId` | `metadata.product_entity_id` |   
`properties.DeviceId` | `entity.asset_id` | The `entity.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.SHA1` | `entity.file.sha1` | If the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.SHA1` log field is mapped to the `entity.file.sha1` UDM field.  
`properties.Issuer` | `entity.file.signature_info.sigcheck.signers.cert_issuer` |   
`properties.Signer` | `entity.file.signature_info.sigcheck.signers.name` |   
`properties.IsSigned` | `entity.file.signature_info.sigcheck.verified` | If the `properties.IsSigned` log field value is equal to `true`, then the `entity.file.signature_info.sigcheck.verified` UDM field is set to `TRUE`.  
  
Otherwise, the `entity.file.signature_info.sigcheck.verified` UDM field is set to `FALSE`.  
`properties.DeviceName` | `entity.asset.hostname` |   
`properties.CertificateCountersignatureTime` | `additional.fields[certificate_countersignature_time]` |   
`properties.CertificateSerialNumber` | `entity.file.signature_info.sigcheck.x509.serial_number` |   
`properties.CertificateCreationTime` | `additional.fields[certification_creation_time]` |   
`properties.CertificateExpirationTime` | `additional.fields[certification_expiration_time]` |   
`properties.CrlDistributionPointUrls` | `additional.fields[crl_distribution_point_urls]` |   
`properties.IsRootSignerMicrosoft` | `additional.fields[is_root_signer_microsoft]` |   
`properties.IsTrusted` | `additional.fields[is_trusted]` |   
`properties.IssuerHash` | `additional.fields[issuer_hash]` |   
`properties.SignatureType` | `additional.fields[signature_type]` |   
`properties.SignerHash` | `additional.fields[signer_hash]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceImageLoadEvents 

The following table lists the log fields for the `DeviceImageLoadEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.InitiatingProcessSessionId` | `additional.fields[initiating_process_session_id]` |   
`properties.IsInitiatingProcessRemoteSession` | `additional.fields[is_initiating_process_remote_session]` |   
`properties.InitiatingProcessRemoteSessionDeviceName` | `src.hostname` |   
`properties.InitiatingProcessRemoteSessionIP` | `src.ip` |   
`properties.Timestamp` | `metadata.event_timestamp` |   
`properties.ActionType` | `metadata.event_type` | If the `properties.ActionType` log field value is equal to `ImageLoaded`, then the `metadata.event_type` UDM field is set to `PROCESS_MODULE_LOAD`.  
`properties.ActionType` | `security_result.action` | If the `properties.ActionType` log field value is equal to `ImageLoaded`, then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, the `security_result.action` UDM field is set to `UNKNOWN_ACTION`.  
`properties.ReportId` | `metadata.product_log_id` |   
`properties.InitiatingProcessAccountDomain` | `principal.administrative_domain` |   
`principal.DeviceId` | `principal.asset_id` | The `principal.asset_id` is set to `DeviceID:%{principal.DeviceId}`.  
`properties.DeviceName` | `principal.hostname` |   
`properties.InitiatingProcessCommandLine` | `principal.process.command_line` |   
`properties.InitiatingProcessFolderPath` | `principal.process.file.full_path` | If the `properties.InitiatingProcessFolderPath` log field value matches the regular expression pattern the `properties.InitiatingProcessFileName` log field value, then the `properties.InitiatingProcessFolderPath` log field is mapped to the `principal.process.file.full_path` UDM field.  
  
Otherwise, the `principal.process.file.full_path` is set to `%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}`.  
`properties.InitiatingProcessMD5` | `principal.process.file.md5` | If the `properties.InitiatingProcessMD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessMD5` log field is mapped to the `principal.process.file.md5` UDM field.  
`properties.InitiatingProcessFileName` | `principal.process.file.names` |   
`properties.InitiatingProcessSHA1` | `principal.process.file.sha1` | If the `properties.InitiatingProcessSHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessSHA1` log field is mapped to the `principal.process.file.sha1` UDM field.  
`properties.InitiatingProcessSHA256` | `principal.process.file.sha256` | If the `properties.InitiatingProcessSHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.InitiatingProcessSHA256` log field is mapped to the `principal.process.file.sha256` UDM field.  
`properties.InitiatingProcessFileSize` | `principal.process.file.size` |   
`properties.InitiatingProcessParentFileName` | `principal.process.parent_process.file.names` |   
`properties.InitiatingProcessParentId` | `principal.process.parent_process.pid` |   
`properties.InitiatingProcessId` | `principal.process.pid` |   
`properties.InitiatingProcessTokenElevation` | `principal.process.token_elevation_type` | If the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeFull`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_1`.  
  
Otherwise, if the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeDefault`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_2`.  
  
Otherwise, if the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeLimited`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_3`.  
`properties.InitiatingProcessAccountObjectId` | `principal.user.product_object_id` |   
`properties.InitiatingProcessAccountUpn` | `principal.user.user_display_name` |   
`properties.InitiatingProcessAccountName` | `principal.user.userid` |   
`properties.InitiatingProcessAccountSid` | `principal.user.windows_sid` |   
`properties.FolderPath` | `target.process.file.full_path` | If the `properties.FolderPath` log field value matches the regular expression pattern the `properties.FileName`, then the `properties.FolderPath` log field is mapped to the `target.process.file.full_path` UDM field.  
  
Otherwise, the `target.process.file.full_path`is set to `%{properties.FolderPath}/%{properties.FileName}`.  
`properties.MD5` | `target.process.file.md5` | If the `properties.MD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.MD5` log field is mapped to the `target.process.file.md5` UDM field.  
`properties.FileName` | `target.process.file.names` |   
`properties.SHA1` | `target.process.file.sha1` | If the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.SHA1` log field is mapped to the `target.process.file.sha1` UDM field.  
`properties.SHA256` | `target.process.file.sha256` | If the `properties.SHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.SHA256` log field is mapped to the `target.process.file.sha256` UDM field.  
`properties.FileSize` | `target.process.file.size` |   
`properties.FolderPath` | `target.file.full_path` | If the `properties.FolderPath` log field value matches the regular expression pattern the `properties.FileName`, then the `properties.FolderPath` log field is mapped to the `target.file.full_path` UDM field.  
  
Otherwise, the `target.file.full_path`is set to `%{properties.FolderPath}/%{properties.FileName}`.  
`properties.MD5` | `target.file.md5` | If the `properties.MD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.MD5` log field is mapped to the `target.process.file.md5` UDM field.  
`properties.FileName` | `target.file.names` |   
`properties.SHA1` | `target.file.sha1` | If the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.SHA1` log field is mapped to the `target.file.sha1` UDM field.  
`properties.SHA256` | `target.file.sha256` | If the `properties.SHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.SHA256` log field is mapped to the `target.file.sha256` UDM field.  
`properties.FileSize` | `target.file.size` |   
`properties.AppGuardContainerId` | `additional.fields[app_guard_container_id]` |   
`properties.InitiatingProcessCreationTime` | `additional.fields[initiating_process_creation_time]` |   
`properties.InitiatingProcessIntegrityLevel` | `additional.fields[initiating_process_integrity_level]` |   
`properties.InitiatingProcessParentCreationTime` | `additional.fields[initiating_process_parent_creation_time]` |   
`properties.InitiatingProcessVersionInfoCompanyName` | `principal.process.file.exif_info.company` |   
`properties.InitiatingProcessVersionInfoFileDescription` | `principal.process.file.exif_info.file_description` |   
`properties.InitiatingProcessVersionInfoInternalFileName` | `additional.fields[initiating_process_version_info_internal_file_name]` |   
`properties.InitiatingProcessVersionInfoOriginalFileName` | `principal.process.file.exif_info.original_file` |   
`properties.InitiatingProcessVersionInfoProductName` | `principal.process.file.exif_info.product` |   
`properties.InitiatingProcessVersionInfoProductVersion` | `additional.fields[initiating_process_version_info_product_version]` |   
`properties.ProcessUniqueId` | `additional.fields[ProcessUniqueId]` |   
`properties.InitiatingProcessUniqueId` | `additional.fields[InitiatingProcessUniqueId]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceFileEvents 

The following table lists the log fields for the `DeviceFileEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.InitiatingProcessSessionId` | `additional.fields[initiating_process_session_id]` |   
`properties.IsInitiatingProcessRemoteSession` | `additional.fields[is_initiating_process_remote_session]` |   
`properties.InitiatingProcessRemoteSessionDeviceName` | `additional.fields[initiating_process_remote_session_device_name]` |   
`properties.InitiatingProcessRemoteSessionIP` | `additional.fields[initiating_process_remote_session_ip]` |   
`properties.Timestamp` | `metadata.event_timestamp` |   
`properties.ActionType` | `metadata.event_type` | If the `properties.ActionType` log field value is equal to `FileCreated`, then the `metadata.event_type` UDM field is set to `FILE_CREATION`.  
  
Otherwise, if the `properties.ActionType` log field value is equal to `FileDeleted`, then the `metadata.event_type` UDM field is set to `FILE_DELETION`.  
  
Otherwise, if the `properties.ActionType` log field value is equal to `FileModified`, then the `metadata.event_type` UDM field is set to `FILE_MODIFICATION`.  
  
Otherwise, if the `properties.ActionType` log field value is equal to `FileRenamed`, then the `metadata.event_type` UDM field is set to `FILE_MOVE`.  
`properties.ActionType` | `security_result.action` | If the `properties.ActionType` log field contains one of the following values:

  * `FileCreated`
  * `FileDeleted`
  * `FileModified`
  * `FileRenamed`

then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, the `security_result.action` UDM field is set to `UNKNOWN_ACTION`.  
`properties.ReportId` | `metadata.product_log_id` |   
`properties.RequestProtocol` | `network.application_protocol` | If the `properties.RequestProtocol` log field value is equal to `SMB`, then the `network.application_protocol` UDM field is set to `SMB`.  
  
Otherwise, if the `properties.RequestProtocol` log field value is equal to `NFS`, then the `network.application_protocol` UDM field is set to `NFS`.  
  
Otherwise, if the `properties.RequestProtocol` log field value is equal to `Local`, then the `network.application_protocol` UDM field is set to `UNKNOWN_APPLICATION_PROTOCOL`.  
`properties.FileOriginReferrerUrl` | `network.http.referral_url` |   
`properties.InitiatingProcessAccountDomain` | `principal.administrative_domain` | If the `properties.InitiatingProcessAccountDomain` log field value is _not_ empty, then the `properties.InitiatingProcessAccountDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
`properties.RequestAccountDomain` | `principal.administrative_domain` | If the `properties.InitiatingProcessAccountDomain` log field value is empty, then the `properties.RequestAccountDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
`properties.DeviceId` | `principal.asset_id` | The `principal.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.DeviceName` | `principal.hostname` |   
`properties.FileOriginIP` | `src.ip` |   
`properties.RequestSourceIP` | `src.ip` |   
`properties.RequestSourcePort` | `src.port` |   
`properties.InitiatingProcessCommandLine` | `principal.process.command_line` |   
`properties.InitiatingProcessFolderPath` | `principal.process.file.full_path` | If the `properties.InitiatingProcessFolderPath` log field value matches the regular expression pattern the `properties.InitiatingProcessFileName` log field value, then the `properties.InitiatingProcessFolderPath` log field is mapped to the `principal.process.file.full_path` UDM field.  
  
Otherwise, the `principal.process.file.full_path` is set to `%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}`.  
`properties.InitiatingProcessMD5` | `principal.process.file.md5` | If the `properties.InitiatingProcessMD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessMD5` log field is mapped to the `principal.process.file.md5` UDM field.  
`properties.InitiatingProcessFileName` | `principal.process.file.names` |   
`properties.InitiatingProcessSHA1` | `principal.process.file.sha1` | If the `properties.InitiatingProcessSHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessSHA1` log field is mapped to the `principal.process.file.sha1` UDM field.  
`properties.InitiatingProcessSHA256` | `principal.process.file.sha256` | If the `properties.InitiatingProcessSHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.InitiatingProcessSHA256` log field is mapped to the `principal.process.file.sha256` UDM field.  
`properties.InitiatingProcessFileSize` | `principal.process.file.size` |   
`properties.InitiatingProcessParentId` | `principal.process.parent_process.pid` |   
`properties.InitiatingProcessParentFileName` | `principal.process.parent_process.file.names` |   
`properties.InitiatingProcessId` | `principal.process.pid` |   
`properties.InitiatingProcessTokenElevation` | `principal.process.token_elevation_type` | If the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeFull`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_1`.  
  
Otherwise, if the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeDefault`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_2`.  
  
Otherwise, if the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeLimited`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_3`.  
`properties.FileOriginUrl` | `src.url` |   
`properties.InitiatingProcessAccountObjectId` | `principal.user.product_object_id` |   
`properties.InitiatingProcessAccountUpn` | `principal.user.user_display_name` |   
`properties.InitiatingProcessAccountName` | `principal.user.userid` | If the `properties.InitiatingProcessAccountName` log field value is _not_ empty, then the `properties.InitiatingProcessAccountName` log field is mapped to the `principal.user.userid` UDM field.  
`properties.RequestAccountName` | `principal.user.userid` | If the `properties.InitiatingProcessAccountName` log field value is empty, then the `properties.RequestAccountName` log field is mapped to the `principal.user.userid` UDM field.  
`properties.InitiatingProcessAccountSid` | `principal.user.windows_sid` | If the `properties.InitiatingProcessAccountSid` log field value is _not_ empty, then the `properties.InitiatingProcessAccountSid` log field is mapped to the `principal.user.windows_sid` UDM field.  
`properties.RequestAccountSid` | `principal.user.windows_sid` | If the `properties.InitiatingProcessAccountSid` log field value is empty, then the `properties.RequestAccountSid` log field is mapped to the `principal.user.windows_sid` UDM field.  
`properties.PreviousFolderPath` | `src.file.full_path` | If the `properties.PreviousFolderPath` log field value matches the regular expression pattern the `properties.PreviousFileName` log field value, then the `properties.PreviousFolderPath` log field is mapped to the `src.file.full_path` UDM field.  
  
Otherwise, `src.file.full_path` set to the `%{properties.PreviousFolderPath}/%{properties.PreviousFileName}`.  
`properties.PreviousFileName` | `src.file.names` |   
`properties.FolderPath` | `target.file.full_path` | If the `properties.FolderPath` log field value matches the regular expression pattern the `properties.FileName` log field value, then the `properties.FolderPath` log field is mapped to the `target.file.full_path` UDM field.  
  
Otherwise, the `target.file.full_path` set to `%{properties.FolderPath}/%{properties.FileName}`.  
`properties.MD5` | `target.file.md5` | If the `properties.MD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.MD5` log field is mapped to the `target.file.md5` UDM field.  
`properties.FileName` | `target.file.names` |   
`properties.SHA1` | `target.file.sha1` | If the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.SHA1` log field is mapped to the `target.file.sha1` UDM field.  
`properties.SHA256` | `target.file.sha256` | If the `properties.SHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.SHA256` log field is mapped to the `target.file.sha256` UDM field.  
`properties.FileSize` | `target.file.size` |   
`properties.SensitivityLabel` | `target.file.tags` |   
`properties.SensitivitySubLabel` | `target.file.tags` |   
`properties.AdditionalFields` | `additional.fields[additional_fields]` |   
`properties.AppGuardContainerId` | `additional.fields[app_guard_container_id]` |   
`properties.InitiatingProcessCreationTime` | `additional.fields[initiating_process_creation_time]` |   
`properties.InitiatingProcessIntegrityLevel` | `additional.fields[initiating_process_integrity_level]` |   
`properties.InitiatingProcessVersionInfoCompanyName` | `principal.process.file.exif_info.company` |   
`properties.InitiatingProcessVersionInfoFileDescription` | `principal.process.file.exif_info.file_description` |   
`properties.InitiatingProcessVersionInfoInternalFileName` | `additional.fields[initiating_process_version_info_internal_file_name]` |   
`properties.InitiatingProcessVersionInfoOriginalFileName` | `principal.process.file.exif_info.original_file` |   
`properties.InitiatingProcessVersionInfoProductName` | `principal.process.file.exif_info.product` |   
`properties.InitiatingProcessVersionInfoProductVersion` | `additional.fields[initiating_process_version_info_product_version]` |   
`properties.InitiatingProcessParentCreationTime` | `additional.fields[initiating_process_parent_creation_time]` |   
`properties.IsAzureInfoProtectionApplied` | `additional.fields[is_azure_info_protection_applied]` |   
`properties.ShareName` | `additional.fields[share_name]` |   
`properties.ProcessUniqueId` | `additional.fields[ProcessUniqueId]` |   
`properties.InitiatingProcessUniqueId` | `additional.fields[InitiatingProcessUniqueId]` |   
`properties.MachineGroup` | `principal.asset.attribute.labels[MachineGroup]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceInfo

The following table lists the log fields for the `DeviceInfo` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.AzureResourceId` | `entity.asset.attribute.labels[azure_resource_id]` |   
`properties.AwsResourceName` | `entity.asset.attribute.labels[aws_resource_name]` |   
`properties.GcpFullResourceName` | `entity.asset.attribute.labels[gcp_full_resource_name]` |   
`properties.HardwareUuid` | `entity.asset.hardware.serial_number` |   
`properties.AzureVmId` | `entity.asset.attribute.labels[azure_vm_id]` |   
`properties.AzureVmSubscriptionId` | `entity.asset.attribute.labels[azure_vm_subscription_id]` |   
`properties.IsTransient` | `entity.asset.attribute.labels[is_transient]` |   
`properties.OsBuildRevision` | `entity.asset.attribute.labels[os_build_revision]` |   
`properties.MitigationStatus` | `entity.asset.attribute.labels[mitigation_status]` |   
`properties.Site` | `entity.asset.location.name` |   
`properties.DiscoverySources` | `entity.asset.attribute.labels[discovery_sources]` |   
`properties.CloudPlatforms` | `entity.asset.attribute.cloud.environment` | If the `properties.CloudPlatforms` log field value matches the regular expression pattern `/(?i)Amazon Web Services/`, then the `entity.asset.attribute.cloud.environment` UDM field is set to `AMAZON_WEB_SERVICES`.  
  
Otherwise, if the `properties.CloudPlatforms` log field value matches the regular expression pattern `/(?i)Google Cloud Platform/`, then the `entity.asset.attribute.cloud.environment` UDM field is set to `GOOGLE_CLOUD_PLATFORM`.  
  
Otherwise, if the `properties.CloudPlatforms` log field value matches one of the regular expression patterns `/(?i)Azure/` or `/(?i)Azure Arc/`, then the `entity.asset.attribute.cloud.environment` UDM field is set to `MICROSOFT_AZURE`.  
`properties.DeviceId` | `entity.asset_id` | The `entity.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.DeviceId` | `entity.asset.asset_id` | The `entity.asset.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.AadDeviceId` | `entity.asset.attribute.labels[aad_device_id]` |   
`properties.AdditionalFields` | `entity.asset.attribute.labels[additional_fields]` |   
`properties.ConnectivityType` | `entity.asset.attribute.labels[connectivity_type]` |   
`properties.DeviceDynamicTags` | `entity.asset.attribute.labels[device_dynamic_tags]` |   
`properties.DeviceManualTags` | `entity.asset.attribute.labels[device_manual_tags]` |   
`properties.DeviceSubtype` | `entity.asset.attribute.labels[device_subtype]` |   
`properties.HostDeviceId` | `entity.asset.attribute.labels[host_device_id]` |   
`properties.IsAzureADJoined` | `entity.asset.attribute.labels[is_azure_ad_joined]` |   
`properties.IsInternetFacing` | `entity.asset.attribute.labels[is_internet_facing]` |   
`properties.JoinType` | `entity.asset.attribute.labels[join_type]` |   
`properties.MergedDeviceIds` | `entity.asset.attribute.labels[merged_device_ids]` |   
`properties.MergedToDeviceId` | `entity.asset.attribute.labels[merged_to_device_id]` |   
`properties.OnboardingStatus` | `entity.asset.attribute.labels[onboarding_status]` |   
`properties.OSArchitecture` | `entity.asset.attribute.labels[os_architecture]` |   
`properties.OSDistribution` | `entity.asset.attribute.labels[os_distribution]` |   
`properties.OSVersionInfo` | `entity.asset.attribute.labels[os_version_info]` |   
`properties.RegistryDeviceTag` | `entity.asset.attribute.labels[registry_divice_tag]` |   
`properties.ReportId` | `entity.asset.attribute.labels[report_id]` |   
`properties.SensorHealthState` | `entity.asset.attribute.labels[sensor_health_state]` |   
`properties.DeviceCategory` | `entity.asset.category` |   
`properties.Vendor` | `entity.asset.hardware.manufacturer` |   
`properties.Model` | `entity.asset.hardware.model` |   
`properties.DeviceName` | `entity.asset.hostname` |   
`properties.PublicIP` | `entity.asset.nat_ip` |   
`properties.OSBuild` | `entity.asset.platform_software.platform_patch_level` |   
`properties.OSPlatform` | `entity.asset.platform_software.platform` | If the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)macos`, then the `entity.asset.platform_software.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)windows`, then the `entity.asset.platform_software.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)linux`, then the `entity.asset.platform_software.platform` UDM field is set to `LINUX`.  
`properties.OSVersion` | `entity.asset.platform_software.platform_version` |   
`properties.ClientVersion` | `entity.asset.software.version` |   
`properties.DeviceType` | `entity.asset.type` | If the `properties.DeviceType` log field value is equal to `NetworkDevice`, then the `entity.asset.type` UDM field is set to `NETWORK_ATTACHED_STORAGE`.  
Otherwise, if the `properties.DeviceType` log field value is equal to `Workstation`, then the `entity.asset.type` UDM field is set to `WORKSTATION`.  
Otherwise, if the `properties.DeviceType` log field value is equal to `Server`, then the `entity.asset.type` UDM field is set to `SERVER`.  
Otherwise, if the `properties.DeviceType` log field value is equal to `Mobile`, then the `entity.asset.type` UDM field is set to `MOBILE`.  
Otherwise, if the `properties.DeviceType` log field value is equal to `Printer`, then the `entity.asset.type` UDM field is set to `PRINTER`.  
Otherwise, the `entity.asset.type` UDM field is set to `ROLE_UNSPECIFIED` and `properties.DeviceType` is mapped to `entity.asset.attribute.labels[device_type]`.  
`properties.MachineGroup` | `entity.group.group_display_name` |   
`properties.ExclusionReason` | `entity.security_result.detection_fields[exclusion_reason]` |   
`properties.ExposureLevel` | `entity.security_result.detection_fields[exposure_level]` |   
`properties.IsExcluded` | `entity.security_result.detection_fields[is_excluded]` |   
`properties.AssetValue` | `entity.security_result.priority` | If the `properties.AssetValue` log field value is equal to `High`, then the `entity.security_result.priority` UDM field is set to `HIGH_PRIORITY`.  
  
Otherwise, if the `properties.AssetValue` log field value is equal to `Medium`, then the `entity.security_result.priority` UDM field is set to `MEDIUM_PRIORITY`.  
  
Otherwise, if the `properties.AssetValue` log field value is equal to `Low`, then the `entity.security_result.priority` UDM field is set to `LOW_PRIORITY`.  
  
Otherwise, the `properties.AssetValue` log field is mapped to the `entity.security_result.detection_fields.asset_value` UDM field.  
`properties.Timestamp` | `metadata.creation_timestamp` |   
`` | `metadata.entity_type` | The `metadata.entity_type` UDM field is set to `ASSET`.  
`properties.DeviceId` | `metadata.product_entity_id` | The `metadata.product_entity_id` is set to `DeviceID:%{properties.DeviceId}`.  
`` | `relations.direction` | The `relations.direction` UDM field is set to `UNIDIRECTIONAL`.  
`` | `relations.entity_type` | The `relations.entity_type` UDM field is set to `USER`.  
`` | `relations.relationship` | The `relations.relationship` UDM field is set to `MEMBER`.  
`properties.LoggedOnUsers.DomainName` | `relations.entity.domain.name` |   
`properties.LoggedOnUsers.UserName` | `relations.entity.user.userid` |   
`properties.LoggedOnUsers.Sid` | `relations.entity.user.windows_sid` |   
`properties.LoggedOnUsers` | `` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - IdentityLogonEvents

The following table lists the log fields for the `IdentityLogonEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.ActionType` | `security_result.action` | If the `properties.ActionType` log field value matches the regular expression pattern `(?i)LogonSuccess`, then the `security_result.action` UDM field is set to `ALLOW`.  
Otherwise, if the `properties.ActionType` log field value matches the regular expression pattern `(?i)LogonBlocked`, then the `security_result.action` UDM field is set to `BLOCK`.  
Otherwise, if the `properties.ActionType` log field value matches the regular expression pattern `(?i)LogonFailed`, then the `security_result.action` UDM field is set to `FAIL`.  
Otherwise, the `security_result.action` UDM field is set to `UNKNOWN_ACTION`.  
`properties.LogonType` | `extensions.auth.mechanism` | If the `properties.LogonType` log field value is equal to `Interactive`, then the `extensions.auth.mechanism` UDM field is set to `INTERACTIVE`.  
Otherwise, if the `properties.LogonType` log field value is equal to `Network`, then the `extensions.auth.mechanism` UDM field is set to `NETWORK`.  
Otherwise, if the `properties.LogonType` log field value is equal to `Batch`, then the `extensions.auth.mechanism` UDM field is set to `BATCH`.  
Otherwise, if the `properties.LogonType` log field value is equal to `Service`, then the `extensions.auth.mechanism` UDM field is set to `SERVICE`.  
Otherwise, if the `properties.LogonType` log field value is equal to `RemoteInteractive`, then the `extensions.auth.mechanism` UDM field is set to `REMOTE_INTERACTIVE`.  
Otherwise, the `extensions.auth.mechanism` UDM field is set to `MECHANISM_UNSPECIFIED` and `properties.LogonType` is mapped to `additional.fields[logon_type]`.  
`properties.Protocol` | `network.ip_protocol` | If the `properties.Protocol` log field value is equal to `Tcp`, then the `network.ip_protocol` UDM field is set to `TCP`.  
  
Otherwise, if the `properties.Protocol` log field value is equal to `Udp`, then the `network.ip_protocol` UDM field is set to `UDP`.  
  
Otherwise, if the `properties.Protocol` log field value is equal to `Icmp`, then the `network.ip_protocol` UDM field is set to `ICMP`.  
  
Otherwise, the `network.ip_protocol` UDM field is set to `UNKNOWN_IP_PROTOCOL` and `properties.Protocol` is mapped to `additional.fields[network_protocol]`.  
`properties.AccountDisplayName` | `principal.user.user_display_name` |   
`properties.Location` | `principal.location.name` |   
`properties.OSPlatform` | `principal.asset.platform_software.platform` | If the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)macos`, then the `principal.asset.platform_software.platform` UDM field is set to `MAC`.  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)windows`, then the `principal.asset.platform_software.platform` UDM field is set to `WINDOWS`.  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)linux`, then the `principal.asset.platform_software.platform` UDM field is set to `LINUX`.  
`properties.OSPlatform` | `principal.asset.platform_software.platform_version` |   
`properties.DeviceType` | `principal.asset.type` | If the `properties.DeviceType` log field value is equal to `NetworkDevice`, then the `principal.asset.type` UDM field is set to `NETWORK_ATTACHED_STORAGE`.  
Otherwise, if the `properties.DeviceType` log field value is equal to `Workstation`, then the `principal.asset.type` UDM field is set to `WORKSTATION`.  
Otherwise, if the `properties.DeviceType` log field value is equal to `Server`, then the `principal.asset.type` UDM field is set to `SERVER`.  
Otherwise, if the `properties.DeviceType` log field value is equal to `Mobile`, then the `principal.asset.type` UDM field is set to `MOBILE`.  
Otherwise, if the `properties.DeviceType` log field value is equal to `Printer`, then the `principal.asset.type` UDM field is set to `PRINTER`.  
Otherwise, the `principal.asset.type` UDM field is set to `ROLE_UNSPECIFIED` and `properties.DeviceType` is mapped to `principal.asset.attribute.labels[device_type]`.  
`properties.ISP` | `network.carrier_name` |   
`properties.DestinationDeviceName` | `intermediary.hostname` |   
`properties.TargetDeviceName` | `target.hostname` |   
`properties.FailureReason` | `security_result.description` |   
`properties.Port` | `principal.port` |   
`properties.DestinationPort` | `intermediary.port` |   
`properties.DestinationIPAddress` | `intermediary.ip` |   
`properties.TargetAccountDisplayName` | `target.user.user_display_name` |   
`properties.Application` | `principal.application` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `USER_LOGIN`.  
`properties.DeviceName` | `principal.hostname` | If the `properties.DeviceName` log field value is _not_ empty, then the `properties.DeviceName` log field is mapped to the `principal.hostname` UDM field.  
`properties.IPAddress` | `principal.ip` | If the `properties.IPAddress` log field value is _not_ empty, then the `properties.IPAddress` log field is mapped to the `principal.asset.ip` UDM field.  
`properties.AccountDomain` | `principal.administrative_domain` |   
`properties.AdditionalFields` | `additional.fields[additionalfields]` |   
`properties.AccountObjectId` | `principal.user.product_object_id` |   
`properties.AccountUpn` | `principal.user.email_addresses` | If the `properties.AccountUpn` log field value matches the regular expression pattern `^.+@.+$` and the `properties.AccountUpn` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.AccountUpn` log field is mapped to the `principal.user.email_addresses` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `AccountUpn` and the `properties.AccountUpn` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.AccountName` | `principal.user.userid` |   
`properties.AccountSid` | `principal.user.windows_sid` |   
`properties.Timestamp` | `metadata.event_timestamp` |   
`properties.ReportId` | `metadata.product_log_id` |   
  
### Field mapping reference: IdentityDirectoryEvents Event Identifier to Event Type

The following table lists the `IdentityDirectoryEvents` log action types and their corresponding UDM event types. 

Event Identifier | Event Type  
---|---  
`Account Constrained Delegation SPNs changed` | `USER_CHANGE_PERMISSIONS`  
`Account Constrained Delegation State changed` | `USER_CHANGE_PERMISSIONS`  
`Account Delegation changed` | `USER_CHANGE_PERMISSIONS`  
`Account Deleted changed` | `USER_DELETION`  
`Account disabled` | `USER_UNCATEGORIZED`  
`Account Disabled changed` | `USER_UNCATEGORIZED`  
`Account Display Name changed` | `USER_UNCATEGORIZED`  
`Account enabled` | `USER_UNCATEGORIZED`  
`Account expired` | `USER_UNCATEGORIZED`  
`Account Expiry Time changed` | `USER_UNCATEGORIZED`  
`Account Name changed` | `USER_UNCATEGORIZED`  
`Account password change failed` | `USER_CHANGE_PASSWORD`  
`Account Password changed` | `USER_CHANGE_PASSWORD`  
`Account Password expired` | `USER_UNCATEGORIZED`  
`Account Password Never Expires changed` | `USER_UNCATEGORIZED`  
`Account Password Not Required changed` | `USER_UNCATEGORIZED`  
`Account Path changed` | `USER_UNCATEGORIZED`  
`Account primary group ID changed` | `GROUP_MODIFICATION`  
`Account Smart Card Required changed` | `USER_UNCATEGORIZED`  
`Account Supported Encryption Types changed` | `USER_UNCATEGORIZED`  
`Account Unlock changed` | `USER_CHANGE_PERMISSIONS`  
`Account Upn Name changed` | `USER_UNCATEGORIZED`  
`Active Directory security group created` | `GROUP_CREATION`  
`ADCS certificate issued` | `RESOURCE_CREATION`  
`ADFS DKM property read` | `RESOURCE_READ`  
`ADFS settings changed` | `SETTING_MODIFICATION`  
`DES encryption restriction changed` | `USER_UNCATEGORIZED`  
`Device Account Created` | `USER_CREATION`  
`Device dNSHostName changed` | `DEVICE_CONFIG_UPDATE`  
`Device Operating System changed` | `DEVICE_CONFIG_UPDATE`  
`Directory Service replication` | `RESOURCE_CREATION`  
`Domain trusts enumerated` | `RESOURCE_READ`  
`Entra Connect password writeback failed` | `USER_CHANGE_PASSWORD`  
`GMSA password read` | `RESOURCE_READ`  
`Group Membership changed` | `GROUP_MODIFICATION`  
`Group Policy display name changed` | `SETTING_MODIFICATION`  
`Group Policy Object created` | `SETTING_CREATION`  
`Group Policy Object deleted` | `SETTING_DELETION`  
`Group Policy settings changed` | `SETTING_MODIFICATION`  
`Kerberos preauthentication flag changed` | `USER_UNCATEGORIZED`  
`Plaintext password allow status changed` | `USER_UNCATEGORIZED`  
`Potential lateral movement path identified` | `STATUS_UPDATE`  
`PowerShell execution` | `PROCESS_LAUNCH`  
`Private Data Retrieval` | `RESOURCE_READ`  
`SAM account name changed` | `USER_UNCATEGORIZED`  
`Security Principal created` | `USER_CREATION`  
`Security Principal deleted changed` | `USER_UNCATEGORIZED`  
`Security Principal Display Name changed` | `USER_UNCATEGORIZED`  
`Security Principal Name changed` | `USER_UNCATEGORIZED`  
`Security Principal Path changed` | `USER_UNCATEGORIZED`  
`Security Principal Sam Name changed` | `USER_UNCATEGORIZED`  
`Sensitive DACL changed` | `RESOURCE_PERMISSIONS_CHANGE`  
`Service creation` | `SERVICE_CREATION`  
`SID-History changed` | `USER_UNCATEGORIZED`  
`SMB session` | `NETWORK_CONNECTION`  
`SmbFileCopy` | `FILE_COPY`  
`Task scheduling` | `SCHEDULED_TASK_CREATION`  
`User Mail changed` | `USER_UNCATEGORIZED`  
`User Manager changed` | `USER_UNCATEGORIZED`  
`User Phone Number changed` | `USER_UNCATEGORIZED`  
`User Title changed` | `USER_UNCATEGORIZED`  
`Wmi execution` | `PROCESS_LAUNCH`  
`User Account Created` | `USER_CREATION`  
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - IdentityDirectoryEvents

The following table lists the log fields for the `IdentityDirectoryEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.Timestamp` | `metadata.event_timestamp` |   
`properties.AccountDisplayName` | `principal.user.user_display_name` |   
`properties.AccountDomain` | `principal.administrative_domain` |   
`properties.AccountName` | `principal.user.userid` |   
`properties.AccountObjectId` | `principal.user.product_object_id` |   
`properties.AccountSid` | `principal.user.windows_sid` |   
`properties.AccountUpn` | `principal.user.email_addresses` | If the `properties.AccountUpn` log field value matches the regular expression pattern `^.+@.+$` and the `properties.AccountUpn` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.AccountUpn` log field is mapped to the `principal.user.email_addresses` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `AccountUpn` and the `properties.AccountUpn` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.DeviceName` | `principal.hostname` |   
`properties.IPAddress` | `principal.ip` |   
`properties.ISP` | `principal.ip_geo_artifact.as_owner` |   
`properties.Location` | `principal.ip_geo_artifact.location.name` |   
`properties.Port` | `principal.port` |   
`properties.TargetAccountDisplayName` | `target.user.user_display_name` |   
`properties.TargetAccountUpn` | `target.user.userid` |   
`properties.TargetDeviceName` | `target.hostname` |   
`properties.DestinationDeviceName` | `intermediary.hostname` |   
`properties.DestinationIPAddress` | `intermediary.ip` |   
`properties.DestinationPort` | `intermediary.port` |   
`properties.Application` | `principal.application` |   
`properties.Protocol` | `additional.fields[Protocol]` |   
`properties.AdditionalFields` | `additional.fields[additional_fields]` |   
`properties.ReportId` | `metadata.product_log_id` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - EntraIdSignInEvents

The following table lists the log fields for the `EntraIdSignInEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.Timestamp` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `USER_LOGIN`.  
`properties.AccountDisplayName` | `target.user.user_display_name` |   
`properties.AccountObjectId` | `target.user.product_object_id` |   
`properties.AccountUpn,properties.AlternateSignInName` | `target.user.userid` | If the `properties.AccountUpn` log field value is _not_ empty, then the `properties.AccountUpn` log field is mapped to the `target.user.userid` UDM field. If the `properties.AlternateSignInName` log field value is _not_ empty, then the `target.user.attribute.labels.key` UDM field is set to `AlternateSignInName` and the `properties.AlternateSignInName` log field is mapped to the `target.user.attribute.labels.value` UDM field.  
  
Otherwise, the `properties.AlternateSignInName` log field is mapped to the `target.user.userid` UDM field.  
`properties.IsExternalUser` | `target.user.attribute.labels[IsExternalUser]` |   
`properties.IsGuestUser` | `target.user.attribute.labels[IsGuestUser]` |   
`properties.LastPasswordChangeTimestamp` | `target.user.last_password_change_time` |   
`properties.Application` | `principal.application` |   
`properties.ApplicationId` | `additional.fields[ApplicationId]` |   
`properties.ClientAppUsed` | `additional.fields[ClientAppUsed]` |   
`properties.IsConfidentialClient` | `principal.asset.attribute.labels[IsConfidentialClient]` |   
`properties.UserAgent` | `network.http.user_agent` |   
`properties.Browser` | `principal.browser.browser_version` |   
`properties.ResourceDisplayName` | `target.resource.name` |   
`properties.ResourceId` | `target.resource.product_object_id` |   
`properties.ResourceTenantId` | `target.resource.attribute.labels[ResourceTenantId]` |   
`properties.DeviceName` | `principal.hostname` |   
`properties.EntraIdDeviceId` | `principal.asset.product_object_id` |   
`properties.IPAddress` | `principal.ip` |   
`properties.DeviceTrustType` | `principal.asset.attribute.labels[DeviceTrustType]` |   
`properties.IsCompliant` | `principal.asset.attribute.labels[IsCompliant]` |   
`properties.IsManaged` | `principal.asset.attribute.labels[IsManaged]` |   
`properties.OSPlatform` | `principal.platform` | If the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)macos`, then the `principal.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)windows`, then the `principal.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)linux`, then the `principal.platform` UDM field is set to `LINUX`.  
`properties.OSPlatform` | `principal.platform_version` |   
`properties.City` | `principal.ip_geo_artifact.location.city` |   
`properties.Country` | `principal.ip_geo_artifact.location.country_or_region` |   
`properties.Latitude` | `principal.ip_geo_artifact.location.region_coordinates.latitude` |   
`properties.Longitude` | `principal.ip_geo_artifact.location.region_coordinates.longitude` |   
`properties.State` | `principal.ip_geo_artifact.location.state` |   
`properties.CorrelationId` | `additional.fields[CorrelationId]` |   
`properties.ReportId` | `metadata.product_log_id` |   
`properties.RequestId` | `additional.fields[RequestId]` |   
`properties.SessionId` | `network.session_id` |   
`properties.ConditionalAccessPolicies` | `security_result.rule_labels[ConditionalAccessPolicies]` |   
`properties.ConditionalAccessStatus` | `security_result.outcomes[ConditionalAccessStatus]` |   
`properties.ErrorCode` | `security_result.outcomes[ErrorCode]` |   
`properties.RiskDetails` | `security_result.detection_fields[RiskDetails]` |   
`properties.RiskLevelAggregated` | `security_result.risk_score` |   
`properties.RiskState` | `security_result.detection_fields[RiskState]` |   
`properties.AuthenticationProcessingDetails` | `additional.fields[AuthenticationProcessingDetails]` |   
`properties.AuthenticationRequirement` | `additional.fields[AuthenticationRequirement]` |   
`properties.EndpointCall` | `additional.fields[EndpointCall]` |   
`properties.LogonType` | `extensions.auth.mechanism` | If the `properties.LogonType` log field value is equal to `Interactive`, then the `extensions.auth.mechanism` UDM field is set to `INTERACTIVE`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `Network`, then the `extensions.auth.mechanism` UDM field is set to `NETWORK`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `Batch`, then the `extensions.auth.mechanism` UDM field is set to `BATCH`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `Service`, then the `extensions.auth.mechanism` UDM field is set to `SERVICE`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `RemoteInteractive`, then the `extensions.auth.mechanism` UDM field is set to `REMOTE_INTERACTIVE`.  
  
Otherwise, the `extensions.auth.mechanism` UDM field is set to `MECHANISM_UNSPECIFIED` and the `additional.fields.key` UDM field is set to `LogonType` and the `properties.LogonType` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.NetworkLocationDetails` | `additional.fields[NetworkLocationDetails]` |   
`properties.TokenIssuerType` | `extensions.auth.auth_details` |   
`properties.TokenIssuerType` | `extensions.auth.type` | If the `properties.TokenIssuerType` log field value contains one of the following values:

  * `0`
  * `1`

then the `extensions.auth.type` UDM field is set to `SSO`.  
  
Otherwise, the `extensions.auth.type` UDM field is set to `AUTHTYPE_UNSPECIFIED`.  
`properties.ErrorCode` | `security_result.action` | If the `properties.ErrorCode` log field value is equal to `0`, then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, the `security_result.action` UDM field is set to `FAIL`.  
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceLogonEvents

The following table lists the log fields for the `DeviceLogonEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.ActionType` | `security_result.action` | If the `properties.ActionType` log field value matches the regular expression pattern `(?i)LogonSuccess`, then the `security_result.action` UDM field is set to `ALLOW`.  
Otherwise, if the `properties.ActionType` log field value matches the regular expression pattern `(?i)LogonFailed` or `(?i)LogonAttempted`, then the `security_result.action` UDM field is set to `FAIL`.  
Otherwise, the `security_result.action` UDM field is set to `UNKNOWN_ACTION`.  
`properties.InitiatingProcessSessionId` | `additional.fields[initiating_process_session_id]` |   
`properties.IsInitiatingProcessRemoteSession` | `additional.fields[is_initiating_process_remote_session]` |   
`properties.InitiatingProcessRemoteSessionDeviceName` | `src.hostname` |   
`properties.InitiatingProcessRemoteSessionIP` | `src.ip` |   
`properties.LogonType` | `extensions.auth.mechanism` | If the `properties.LogonType` log field value is equal to `Interactive`, then the `extensions.auth.mechanism` UDM field is set to `INTERACTIVE`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `Network`, then the `extensions.auth.mechanism` UDM field is set to `NETWORK`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `Batch`, then the `extensions.auth.mechanism` UDM field is set to `BATCH`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `Service`, then the `extensions.auth.mechanism` UDM field is set to `SERVICE`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `CachedInteractive`, then the `extensions.auth.mechanism` UDM field is set to `CACHED_INTERACTIVE`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `CachedRemoteInteractive`, then the `extensions.auth.mechanism` UDM field is set to `CACHED_REMOTE_INTERACTIVE`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `NetworkCleartext`, then the `extensions.auth.mechanism` UDM field is set to `NETWORK_CLEAR_TEXT`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `NewCredentials`, then the `extensions.auth.mechanism` UDM field is set to `NEW_CREDENTIALS`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `Local`, then the `extensions.auth.mechanism` UDM field is set to `LOCAL`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `Unlock`, then the `extensions.auth.mechanism` UDM field is set to `UNLOCK`.  
  
Otherwise, if the `properties.LogonType` log field value is equal to `RemoteInteractive`, then the `extensions.auth.mechanism` UDM field is set to `REMOTE_INTERACTIVE`.  
  
Otherwise, the `extensions.auth.mechanism` UDM field is set to `MECHANISM_UNSPECIFIED`.  
`properties.Timestamp` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `USER_LOGIN`.  
`properties.ReportId` | `metadata.product_log_id` |   
`properties.Protocol` | `network.ip_protocol` | If the `properties.Protocol` log field value is equal to `Tcp`, then the `network.ip_protocol` UDM field is set to `TCP`.  
  
If the `properties.Protocol` log field value is equal to `Udp`, then the `network.ip_protocol` UDM field is set to `UDP`.  
  
If the `properties.Protocol` log field value is equal to `Icmp`, then the `network.ip_protocol` UDM field is set to `ICMP`.  
`properties.LogonId` | `extensions.auth.auth_details` |   
`properties.InitiatingProcessAccountDomain` | `principal.administrative_domain` |   
`properties.DeviceId` | `target.asset_id` | The `target.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.DeviceName` | `target.hostname` |   
`properties.InitiatingProcessCommandLine` | `principal.process.command_line` |   
`properties.InitiatingProcessFolderPath` | `principal.process.file.full_path` | If the `properties.InitiatingProcessFolderPath` log field value matches the regular expression pattern the `properties.InitiatingProcessFileName` log field value, then the `properties.InitiatingProcessFolderPath` log field is mapped to the `principal.process.file.full_path` UDM field.  
  
Otherwise, the `principal.process.file.full_path` is set to `%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}`.  
`properties.InitiatingProcessMD5` | `principal.process.file.md5` | If the `properties.InitiatingProcessMD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessMD5` log field is mapped to the `principal.process.file.md5` UDM field.  
`properties.InitiatingProcessFileName` | `principal.process.file.names` |   
`properties.InitiatingProcessSHA1` | `principal.process.file.sha1` | If the `properties.InitiatingProcessSHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessSHA1` log field is mapped to the `principal.process.file.sha1` UDM field.  
`properties.InitiatingProcessSHA256` | `principal.process.file.sha256` | If the `properties.InitiatingProcessSHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.InitiatingProcessSHA256` log field is mapped to the `principal.process.file.sha256` UDM field.  
`properties.InitiatingProcessFileSize` | `principal.process.file.size` |   
`properties.InitiatingProcessParentFileName` | `principal.process.parent_process.file.names` |   
`properties.InitiatingProcessParentId` | `principal.process.parent_process.pid` |   
`properties.InitiatingProcessId` | `principal.process.pid` |   
`properties.InitiatingProcessTokenElevation` | `principal.process.token_elevation_type` | If the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeFull`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_1`.  
  
Otherwise, if the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeDefault`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_2`.  
  
Otherwise, if the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeLimited`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_3`.  
`properties.InitiatingProcessAccountObjectId` | `principal.user.product_object_id` |   
`properties.InitiatingProcessAccountUpn` | `principal.user.user_display_name` |   
`properties.InitiatingProcessAccountName` | `principal.user.userid` |   
`properties.InitiatingProcessAccountSid` | `principal.user.windows_sid` |   
`properties.FailureReason` | `security_result.description` |   
`properties.AccountDomain` | `target.administrative_domain` |   
`properties.RemoteDeviceName` | `principal.hostname` |   
`properties.RemoteIP` | `principal.ip` |   
`properties.RemotePort` | `principal.port` |   
`properties.IsLocalAdmin` | `target.resource.attribute.labels[is_local_admin]` |   
`properties.AccountName` | `target.user.userid` |   
`properties.AccountSid` | `target.user.windows_sid` |   
`properties.RemoteIPType` | `additional.fields[remote_ip_type]` |   
`properties.AdditionalFields` | `additional.fields[additional_fields]` |   
`properties.AppGuardContainerId` | `additional.fields[app_guard_container_id]` |   
`properties.InitiatingProcessCreationTime` | `additional.fields[initiating_process_creation_time]` |   
`properties.InitiatingProcessIntegrityLevel` | `additional.fields[initiating_process_integrity_level]` |   
`properties.InitiatingProcessVersionInfoCompanyName` | `principal.process.file.exif_info.company` |   
`properties.InitiatingProcessVersionInfoFileDescription` | `principal.process.file.exif_info.file_description` |   
`properties.InitiatingProcessVersionInfoInternalFileName` | `additional.fields[initiating_process_version_info_internal_file_name]` |   
`properties.InitiatingProcessVersionInfoOriginalFileName` | `principal.process.file.exif_info.original_file` |   
`properties.InitiatingProcessVersionInfoProductName` | `principal.process.file.exif_info.product` |   
`properties.InitiatingProcessVersionInfoProductVersion` | `additional.fields[initiating_process_version_info_product_version]` |   
`properties.InitiatingProcessParentCreationTime` | `additional.fields[initiating_process_parent_creation_time]` |   
`properties.ProcessUniqueId` | `additional.fields[ProcessUniqueId]` |   
`properties.InitiatingProcessUniqueId` | `additional.fields[InitiatingProcessUniqueId]` |   
`properties.MachineGroup` | `principal.asset.attribute.labels[MachineGroup]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceNetworkEvents

The following table lists the log fields for the `DeviceNetworkEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.ActionType` | `security_result.action` | If the `properties.ActionType` log field contains one of the following values:

  * `ConnectionAcknowledged`
  * `ConnectionFound`
  * `ConnectionSuccess`
  * `ConnectionSuccessAggregatedReport`
  * `DnsConnectionInspected`
  * `FtpConnectionInspected`
  * `HttpConnectionInspected`
  * `IcmpConnectionInspected`
  * `InboundConnectionAccepted`
  * `InboundInternetScanInspected`
  * `KerberosConnectionInspected`
  * `ListeningConnectionCreated`
  * `NetworkSignatureInspected`
  * `NtlmAuthenticationInspected`
  * `SmtpConnectionInspected`
  * `SshConnectionInspected`
  * `SslConnectionInspected`

then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, if the `properties.ActionType` log field contains one of the following values:

  * `ConnectionFailed`
  * `ConnectionFailedAggregatedReport`

then the `security_result.action` UDM field is set to `FAIL`.  
  
Otherwise, the `security_result.action` UDM field is set to `UNKNOWN_ACTION`.  
`properties.ActionType` | `security_result.summary` |   
`properties.InitiatingProcessSessionId` | `additional.fields[initiating_process_session_id]` |   
`properties.IsInitiatingProcessRemoteSession` | `additional.fields[is_initiating_process_remote_session]` |   
`properties.InitiatingProcessRemoteSessionDeviceName` | `src.hostname` |   
`properties.InitiatingProcessRemoteSessionIP` | `src.ip` |   
`properties.Timestamp` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `NETWORK_CONNECTION`.  
`properties.ReportId` | `metadata.product_log_id` |   
`properties.Protocol` | `network.ip_protocol` | If the `properties.Protocol` log field value is equal to `Tcp`, then the `network.ip_protocol` UDM field is set to `TCP`.  
  
Otherwise, if the `properties.Protocol` log field value is equal to `Udp`, then the `network.ip_protocol` UDM field is set to `UDP`.  
  
Otherwise, if the `properties.Protocol` log field value is equal to `Icmp`, then the `network.ip_protocol` UDM field is set to `ICMP`.  
`properties.InitiatingProcessAccountDomain` | `principal.administrative_domain` |   
`properties.DeviceId` | `principal.asset_id` | The `principal.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.DeviceName` | `principal.hostname` |   
`properties.LocalIP` | `principal.ip` | If the `properties.LocalIP` log field value is _not_ empty, then if the `properties.AdditionalFields.direction` log field value is equal to `In` or the `properties.ActionType` log field value is equal to `InboundConnectionAccepted`, then the `properties.LocalIP` log field is mapped to the `target.ip` and `target.asset.ip` UDM fields.  
  
Otherwise, the `properties.LocalIP` log field is mapped to the `principal.ip` and `principal.asset.ip` UDM fields.  
`properties.LocalPort` | `principal.port` |   
`properties.InitiatingProcessCommandLine` | `principal.process.command_line` |   
`properties.InitiatingProcessFolderPath` | `principal.process.file.full_path` | If the `properties.InitiatingProcessFolderPath` log field value matches the regular expression pattern the `properties.InitiatingProcessFileName` log field value, then the `properties.InitiatingProcessFolderPath` log field is mapped to the `principal.process.file.full_path` UDM field.  
  
Otherwise, the `principal.process.file.full_path` is set to `%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}`.  
`properties.InitiatingProcessMD5` | `principal.process.file.md5` | If the `properties.InitiatingProcessMD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessMD5` log field is mapped to the `principal.process.file.md5` UDM field.  
`properties.InitiatingProcessFileName` | `principal.process.file.names` |   
`properties.InitiatingProcessSHA1` | `principal.process.file.sha1` | If the `properties.InitiatingProcessSHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessSHA1` log field is mapped to the `principal.process.file.sha1` UDM field.  
`properties.InitiatingProcessSHA256` | `principal.process.file.sha256` | If the `properties.InitiatingProcessSHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.InitiatingProcessSHA256` log field is mapped to the `principal.process.file.sha256` UDM field.  
`properties.InitiatingProcessFileSize` | `principal.process.file.size` |   
`properties.InitiatingProcessParentFileName` | `principal.process.parent_process.file.names` |   
`properties.InitiatingProcessParentId` | `principal.process.parent_process.pid` |   
`properties.InitiatingProcessId` | `principal.process.pid` |   
`properties.InitiatingProcessTokenElevation` | `principal.process.token_elevation_type` | If the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeFull`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_1`.  
  
Otherwise, if the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeDefault`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_2`.  
  
Otherwise, if the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeLimited`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_3`.  
`properties.InitiatingProcessAccountObjectId` | `principal.user.product_object_id` |   
`properties.InitiatingProcessAccountUpn` | `principal.user.user_display_name` |   
`properties.InitiatingProcessAccountName` | `principal.user.userid` |   
`properties.InitiatingProcessAccountSid` | `principal.user.windows_sid` |   
`properties.RemoteIP` | `target.ip` | If the `properties.RemoteIP` log field value is _not_ empty, then if the `properties.AdditionalFields.direction` log field value is equal to `In` or the `properties.ActionType` log field value is equal to `InboundConnectionAccepted`, then the `properties.RemoteIP` log field is mapped to the `principal.ip` and `principal.asset.ip` UDM fields.  
  
Otherwise, the `properties.RemoteIP` log field is mapped to the `target.ip` and `target.asset.ip` UDM fields.  
`properties.RemotePort` | `target.port` |   
`properties.RemoteUrl` | `target.url` |   
`properties.LocalIPType` | `additional.fields[LocalIPType]` |   
`properties.RemoteIPType` | `additional.fields[RemoteIPType]` |   
`properties.AdditionalFields` | `additional.fields[additional_fields]` |   
`properties.AppGuardContainerId` | `additional.fields[app_guard_container_id]` |   
`properties.InitiatingProcessCreationTime` | `additional.fields[initiating_process_creation_time]` |   
`properties.InitiatingProcessIntegrityLevel` | `additional.fields[initiating_process_integrity_level]` |   
`properties.InitiatingProcessParentCreationTime` | `additional.fields[initiating_process_parent_creation_time]` |   
`properties.InitiatingProcessVersionInfoCompanyName` | `principal.process.file.exif_info.company` |   
`properties.InitiatingProcessVersionInfoFileDescription` | `principal.process.file.exif_info.file_description` |   
`properties.InitiatingProcessVersionInfoInternalFileName` | `additional.fields[initiating_process_version_info_internal_file_name]` |   
`properties.InitiatingProcessVersionInfoOriginalFileName` | `principal.process.file.exif_info.original_file` |   
`properties.InitiatingProcessVersionInfoProductName` | `principal.process.file.exif_info.product` |   
`properties.InitiatingProcessVersionInfoProductVersion` | `additional.fields[initiating_process_version_info_product_version]` |   
`properties.ProcessUniqueId` | `additional.fields[ProcessUniqueId]` |   
`properties.InitiatingProcessUniqueId` | `additional.fields[InitiatingProcessUniqueId]` |   
`properties.MachineGroup` | `principal.asset.attribute.labels[MachineGroup]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceNetworkInfo

The following table lists the log fields for the `DeviceNetworkInfo` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.NetworkAdapterDnsSuffix` | `entity.asset.attribute.labels[network_adapter_dns_suffix]` |   
`properties.OnboardingStatus` | `entity.asset.attribute.labels[onboarding_status]` |   
`properties.DeviceId` | `entity.asset_id` | The `entity.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.DeviceId` | `entity.asset.asset_id` | The `entity.asset.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.ReportId` | `entity.asset.attribute.labels[report_id]` |   
`properties.ConnectedNetworks` | `entity.asset.attribute.labels[connected_networks]` |   
`properties.MacAddress` | `entity.asset.mac` |   
`properties.NetworkAdapterName` | `entity.asset.attribute.labels[network_adapter_name]` |   
`properties.NetworkAdapterStatus` | `entity.asset.attribute.labels[network_adapter_status]` |   
`properties.NetworkAdapterType` | `entity.asset.attribute.labels[network_adapter_type]` |   
`properties.NetworkAdapterVendor` | `entity.asset.attribute.labels[network_adapter_vendor]` |   
`properties.TunnelType` | `entity.asset.attribute.labels[tunnel_type]` |   
`properties.DefaultGateways` | `entity.asset.attribute.labels[default_gateways]` |   
`properties.DeviceName` | `entity.asset.hostname` |   
`properties.IPAddresses` | `entity.asset.ip` |   
`` | `entity.asset.type` | The `entity.asset.type` UDM field is set to `WORKSTATION`.  
`properties.DnsAddresses` | `entity.domain.last_dns_records.type` | The `entity.domain.last_dns_records.type` UDM field is set to `ip_address`.  
`properties.DnsAddresses` | `entity.domain.last_dns_records.value` | The `properties.DnsAddresses` log field is mapped to the `entity.domain.last_dns_records.value` UDM field.  
`properties.IPv4Dhcp` | `entity.network.dhcp.ciaddr` | If the `properties.IPv4Dhcp` log field value is _not_ empty, then the `properties.IPv4Dhcp` log field is mapped to the `entity.network.dhcp.ciaddr` UDM field.   
  
Otherwise, the `properties.IPv6Dhcp` log field is mapped to the `entity.network.dhcp.ciaddr` UDM field.  
`properties.Timestamp` | `metadata.creation_time` |   
`` | `metadata.entity_type` | The `metadata.entity_type` UDM field is set to `ASSET`.  
`properties.DeviceId` | `metadata.product_entity_id` | The `metadata.product_entity_id` is set to `DeviceID:%{properties.DeviceId}`.  
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceProcessEvents

The following table lists the log fields for the `DeviceProcessEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.InitiatingProcessSessionId` | `additional.fields[initiating_process_session_id]` |   
`properties.IsInitiatingProcessRemoteSession` | `additional.fields[is_initiating_process_remote_session]` |   
`properties.InitiatingProcessRemoteSessionDeviceName` | `src.hostname` | If `properties.InitiatingProcessRemoteSessionDeviceName` log field is not empty, then `properties.InitiatingProcessRemoteSessionDeviceName` log field is mapped to `src.hostname` UDM field.  
`properties.ProcessRemoteSessionDeviceName` | `src.hostname` | If `properties.InitiatingProcessRemoteSessionDeviceName` log field is empty, then `properties.ProcessRemoteSessionDeviceName` log field is mapped to `src.hostname` UDM field.  
`properties.InitiatingProcessRemoteSessionIP` | `src.ip` |   
`properties.ProcessRemoteSessionIP` | `src.ip` |   
`properties.CreatedProcessSessionId` | `additional.fields[created_process_session_id]` |   
`properties.IsProcessRemoteSession` | `additional.fields[is_process_remote_session]` |   
`properties.Timestamp` | `metadata.event_timestamp` |   
`properties.ActionType` | `metadata.event_type` | If the `properties.ActionType` log field value matches the regular expression pattern `(?i)ProcessCreated`, then the `metadata.event_type` UDM field is set to `PROCESS_LAUNCH`.  
  
Otherwise, if the `properties.ActionType` log field value matches the regular expression pattern `(?i)OpenProcess`, then the `metadata.event_type` UDM field is set to `PROCESS_OPEN`.  
`properties.ActionType` | `security_result.action` | If the `properties.ActionType` log field is equal to `ProcessCreated`, then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, the `security_result.action` UDM field is set to `UNKNOWN_ACTION`.  
`properties.ReportId` | `metadata.product_log_id` |   
`properties.LogonId` | `network.session_id` |   
`properties.InitiatingProcessAccountDomain` | `principal.administrative_domain` |   
`properties.DeviceId` | `principal.asset_id` | The `principal.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.DeviceName` | `principal.hostname` |   
`properties.InitiatingProcessCommandLine` | `principal.process.command_line` |   
`properties.InitiatingProcessFolderPath` | `principal.process.file.full_path` | If the `properties.InitiatingProcessFolderPath` log field value matches the regular expression pattern the `properties.InitiatingProcessFileName` log field value, then the `properties.InitiatingProcessFolderPath` log field is mapped to the `principal.process.file.full_path` UDM field.  
  
Otherwise, the `principal.process.file.full_path` is set to `%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}`.  
`properties.InitiatingProcessMD5` | `principal.process.file.md5` | If the `properties.InitiatingProcessMD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessMD5` log field is mapped to the `principal.process.file.md5` UDM field.  
`properties.InitiatingProcessFileName` | `principal.process.file.names` |   
`properties.InitiatingProcessSHA1` | `principal.process.file.sha1` | If the `properties.InitiatingProcessSHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessSHA1` log field is mapped to the `principal.process.file.sha1` UDM field.  
`properties.InitiatingProcessSHA256` | `principal.process.file.sha256` | If the `properties.InitiatingProcessSHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.InitiatingProcessSHA256` log field is mapped to the `principal.process.file.sha256` UDM field.  
`properties.InitiatingProcessSignatureStatus` | `principal.process.file.signature_info.sigcheck.signers.status` |   
`properties.InitiatingProcessFileSize` | `principal.process.file.size` |   
`properties.InitiatingProcessParentId` | `principal.process.parent_process.pid` |   
`properties.InitiatingProcessParentFileName` | `principal.process.parent_process.file.names` |   
`properties.InitiatingProcessId` | `principal.process.pid` |   
`properties.InitiatingProcessTokenElevation` | `principal.process.token_elevation_type` | If the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeFull`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_1`.  
  
Otherwise, if the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeDefault`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_2`.  
  
Otherwise, if the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeLimited`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_3`  
`properties.InitiatingProcessAccountObjectId` | `principal.user.product_object_id` |   
`properties.InitiatingProcessAccountUpn` | `principal.user.user_display_name` |   
`properties.InitiatingProcessAccountName` | `principal.user.userid` |   
`properties.InitiatingProcessAccountSid` | `principal.user.windows_sid` |   
`properties.AccountDomain` | `target.administrative_domain` |   
`properties.FolderPath` | `target.file.full_path` | If the `properties.FolderPath` log field value matches the regular expression pattern the `properties.FileName` log field value, then the `properties.FolderPath` log field is mapped to the `target.file.full_path` UDM field.  
  
Otherwise, the `target.file.full_path` set to `%{properties.FolderPath}/%{properties.FileName}`.  
`properties.MD5` | `target.process.file.md5` | If the `properties.MD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.MD5` log field is mapped to the `target.file.md5` UDM field.  
`properties.FileName` | `target.process.file.names` |   
`properties.SHA1` | `target.process.file.sha1` | If the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.SHA1` log field is mapped to the `target.file.sha1` UDM field.  
`properties.SHA256` | `target.process.file.sha256` | If the `properties.SHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.SHA256` log field is mapped to the `target.file.sha256` UDM field.  
`properties.FileSize` | `target.process.file.size` |   
`properties.ProcessCommandLine` | `target.process.command_line` |   
`properties.ProcessId` | `target.process.pid` |   
`properties.ProcessTokenElevation` | `target.process.token_elevation_type` | If the `properties.ProcessTokenElevation` log field value is equal to `TokenElevationTypeFull`, then the `target.process.token_elevation_type` UDM field is set to `TYPE_1`.  
  
Otherwise, if the `properties.ProcessTokenElevation` log field value is equal to `TokenElevationTypeDefault`, then the `target.process.token_elevation_type` UDM field is set to `TYPE_2`.  
  
Otherwise, if the `properties.ProcessTokenElevation` log field value is equal to `TokenElevationTypeLimited`, then the `target.process.token_elevation_type` UDM field is set to `TYPE_3`.  
`properties.ProcessIntegrityLevel` | `target.resource.attribute.labels[process_integrity_level]` |   
`properties.AccountUpn` | `target.user.user_display_name` |   
`properties.AccountName` | `target.user.userid` |   
`properties.AccountSid` | `target.user.windows_sid` |   
`properties.InitiatingProcessCreationTime` | `additional.fields[initiating_process_creation_time]` |   
`properties.InitiatingProcessParentCreationTime` | `additional.fields[initiating_process_parent_creation_time]` |   
`properties.AccountObjectId` | `additional.fields[account_object_id]` |   
`properties.AdditionalFields` | `additional.fields[additional_fields]` |   
`properties.AppGuardContainerId` | `additional.fields[app_guard_container_id]` |   
`properties.InitiatingProcessIntegrityLevel` | `additional.fields[initiating_process_integrity_level]` |   
`properties.InitiatingProcessLogonId` | `additional.fields[initiating_process_logon_id]` |   
`properties.InitiatingProcessSignerType` | `additional.fields[initiating_process_signer_type]` |   
`properties.InitiatingProcessVersionInfoCompanyName` | `principal.process.file.exif_info.company` |   
`properties.InitiatingProcessVersionInfoFileDescription` | `principal.process.file.exif_info.file_description` |   
`properties.InitiatingProcessVersionInfoInternalFileName` | `additional.fields[initiating_process_version_info_internal_file_name]` |   
`properties.InitiatingProcessVersionInfoOriginalFileName` | `principal.process.file.exif_info.original_file` |   
`properties.InitiatingProcessVersionInfoProductName` | `principal.process.file.exif_info.product` |   
`properties.InitiatingProcessVersionInfoProductVersion` | `additional.fields[initiating_process_version_info_product_version]` |   
`properties.ProcessCreationTime` | `additional.fields[process_creation_time]` |   
`properties.ProcessVersionInfoCompanyName` | `target.process.file.exif_info.company` |   
`properties.ProcessVersionInfoFileDescription` | `target.process.file.exif_info.file_description` |   
`properties.ProcessVersionInfoInternalFileName` | `additional.fields[process_version_info_internal_file_name]` |   
`properties.ProcessVersionInfoOriginalFileName` | `target.process.file.exif_info.original_file` |   
`properties.ProcessVersionInfoProductName` | `target.process.file.exif_info.product` |   
`properties.ProcessVersionInfoProductVersion` | `additional.fields[process_version_info_product_version]` |   
`properties.ProcessUniqueId` | `additional.fields[ProcessUniqueId]` |   
`properties.InitiatingProcessUniqueId` | `additional.fields[InitiatingProcessUniqueId]` |   
`properties.MachineGroup` | `principal.asset.attribute.labels[MachineGroup]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmInfoGathering

The following table lists the log fields for the `DeviceTvmInfoGathering` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.Timestamp` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `SCAN_HOST`.  
`properties.DeviceId` | `principal.asset_id` | The `principal.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.OSPlatform` | `principal.asset.platform_software.platform` | If the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)macos`, then the `principal.asset.platform_software.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)windows`, then the `principal.asset.platform_software.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)linux`, then the `principal.asset.platform_software.platform` UDM field is set to `LINUX`.  
`properties.OSPlatform` | `principal.asset.platform_software.platform_version` |   
`properties.DeviceName` | `principal.hostname` |   
`properties.LastSeenTime` | `principal.asset.last_discover_time` |   
`properties.AdditionalFields` | `additional.fields[additional_fields]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceRegistryEvents 

The following table lists the log fields for the `DeviceRegistryEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.InitiatingProcessSessionId` | `additional.fields[initiating_process_session_id]` |   
`properties.IsInitiatingProcessRemoteSession` | `additional.fields[is_initiating_process_remote_session]` |   
`properties.InitiatingProcessRemoteSessionDeviceName` | `src.hostname` |   
`properties.InitiatingProcessRemoteSessionIP` | `src.ip` |   
`properties.Timestamp` | `metadata.event_timestamp` |   
`properties.ActionType` | `metadata.event_type` | If the `properties.ActionType` log field value matches the regular expression pattern `(?i)RegistryKeyCreated`, then the `metadata.event_type` UDM field is set to `REGISTRY_CREATION`.  
  
Otherwise, if the `properties.ActionType` log field value matches the regular expression pattern `(?i)RegistryKeyDeleted`, then the `metadata.event_type` UDM field is set to `REGISTRY_DELETION`.  
  
Otherwise, if the `properties.ActionType` log field value matches the regular expression pattern `(?i)RegistryKeyRenamed`, then the `metadata.event_type` UDM field is set to `REGISTRY_MODIFICATION`.  
  
Otherwise, if the `properties.ActionType` log field value matches the regular expression pattern `(?i)RegistryValueDeleted`, then the `metadata.event_type` UDM field is set to `REGISTRY_DELETION`.  
  
Otherwise, if the `properties.ActionType` log field value matches the regular expression pattern `(?i)RegistryValueSet`, then the `metadata.event_type` UDM field is set to `REGISTRY_MODIFICATION`.  
  
Otherwise, the `metadata.event_type` UDM field is set to `REGISTRY_UNCATEGORIZED`.  
`properties.ActionType` | `security_result.action` | If the `properties.ActionType` log field contains one of the following values:

  * `RegistryKeyCreated`
  * `RegistryKeyDeleted`
  * `RegistryValueDeleted`
  * `RegistryValueSet`

then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, the `security_result.action` UDM field is set to `UNKNOWN_ACTION`.  
`properties.ReportId` | `metadata.product_log_id` |   
`properties.InitiatingProcessAccountDomain` | `principal.administrative_domain` |   
`properties.DeviceId` | `principal.asset_id` | The `principal.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.DeviceName` | `principal.hostname` |   
`properties.InitiatingProcessCommandLine` | `principal.process.command_line` |   
`properties.InitiatingProcessFolderPath` | `principal.process.file.full_path` | If the `properties.InitiatingProcessFolderPath` log field value matches the regular expression pattern the `properties.InitiatingProcessFileName` log field value, then the `properties.InitiatingProcessFolderPath` log field is mapped to the `principal.process.file.full_path` UDM field.  
  
Otherwise, the `principal.process.file.full_path` is set to `%{properties.InitiatingProcessFolderPath}/%{properties.InitiatingProcessFileName}`.  
`properties.InitiatingProcessMD5` | `principal.process.file.md5` | If the `properties.InitiatingProcessMD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessMD5` log field is mapped to the `principal.process.file.md5` UDM field.  
`properties.InitiatingProcessFileName` | `principal.process.file.names` |   
`properties.InitiatingProcessSHA1` | `principal.process.file.sha1` | If the `properties.InitiatingProcessSHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.InitiatingProcessSHA1` log field is mapped to the `principal.process.file.sha1` UDM field.  
`properties.InitiatingProcessSHA256` | `principal.process.file.sha256` | If the `properties.InitiatingProcessSHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.InitiatingProcessSHA256` log field is mapped to the `principal.process.file.sha256` UDM field.  
`properties.InitiatingProcessFileSize` | `principal.process.file.size` |   
`properties.InitiatingProcessParentFileName` | `principal.process.parent_process.file.names` |   
`properties.InitiatingProcessParentId` | `principal.process.parent_process.pid` |   
`properties.InitiatingProcessId` | `principal.process.pid` |   
`properties.PreviousRegistryValueData` | `src.registry.registry_value_data` |   
`properties.PreviousRegistryKey` | `src.registry.registry_key` |   
`properties.PreviousRegistryValueName` | `src.registry.registry_value_name` |   
`properties.InitiatingProcessAccountObjectId` | `principal.user.attribute.labels[initiating_process_account_object_id]` |   
`properties.InitiatingProcessAccountUpn` | `principal.user.attribute.labels[initiating_process_account_upn]` |   
`properties.InitiatingProcessAccountName` | `principal.user.userid` |   
`properties.InitiatingProcessAccountSid` | `principal.user.windows_sid` |   
`properties.InitiatingProcessTokenElevation` | `principal.process.token_elevation_type` | If the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeFull`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_1`.  
  
Otherwise, if the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeDefault`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_2`.  
  
Otherwise, if the `properties.InitiatingProcessTokenElevation` log field value is equal to `TokenElevationTypeLimited`, then the `principal.process.token_elevation_type` UDM field is set to `TYPE_3`.  
`properties.RegistryValueData` | `target.registry.registry_value_data` |   
`properties.RegistryKey` | `target.registry.registry_key` |   
`properties.RegistryValueName` | `target.registry.registry_value_name` |   
`properties.InitiatingProcessCreationTime` | `additional.fields[initiating_process_creation_time]` |   
`properties.InitiatingProcessIntegrityLevel` | `additional.fields[initiating_process_integrity_level]` |   
`properties.InitiatingProcessParentCreationTime` | `additional.fields[initiating_process_parent_creation_time]` |   
`properties.AppGuardContainerId` | `additional.fields[app_guard_container_id]` |   
`properties.InitiatingProcessVersionInfoCompanyName` | `principal.process.file.exif_info.company` |   
`properties.InitiatingProcessVersionInfoFileDescription` | `principal.process.file.exif_info.file_description` |   
`properties.InitiatingProcessVersionInfoInternalFileName` | `additional.fields[initiating_process_version_info_internal_file_name]` |   
`properties.InitiatingProcessVersionInfoOriginalFileName` | `principal.process.file.exif_info.original_file` |   
`properties.InitiatingProcessVersionInfoProductName` | `principal.process.file.exif_info.product` |   
`properties.InitiatingProcessVersionInfoProductVersion` | `additional.fields[initiating_process_version_info_product_version]` |   
`properties.RegistryValueType` | `additional.fields[registry_value_type]` |   
`properties.ProcessUniqueId` | `additional.fields[ProcessUniqueId]` |   
`properties.InitiatingProcessUniqueId` | `additional.fields[InitiatingProcessUniqueId]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmInfoGatheringKB 

The following table lists the log fields for the `DeviceTvmInfoGatheringKB` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.Description` | `metadata.description` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `GENERIC_EVENT`.  
`properties.IgId` | `metadata.product_log_id` |   
`properties.Categories` | `principal.resource.attribute.labels[categories]` |   
`properties.DataStructure` | `principal.resource.attribute.labels[data_structure]` |   
`properties.FieldName` | `principal.resource.name` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSecureConfigurationAssessment 

The following table lists the log fields for the `DeviceTvmSecureConfigurationAssessment` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.Timestamp` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `SCAN_UNCATEGORIZED`.  
`properties.DeviceId` | `principal.asset_id` | The `principal.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.OSPlatform` | `principal.asset.platform_software.platform` | If the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)macos`, then the `principal.asset.platform_software.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)windows`, then the `principal.asset.platform_software.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)linux`, then the `principal.asset.platform_software.platform` UDM field is set to `LINUX`.  
`properties.DeviceName` | `principal.hostname` |   
`properties.ConfigurationCategory` | `principal.resource.attribute.labels[configuration_category]` |   
`properties.ConfigurationImpact` | `principal.resource.attribute.labels[configuration_impact]` |   
`properties.Context` | `principal.resource.attribute.labels[Context]` | Iterate through log field `properties.Context`:  
  
The `principal.resource.attribute.labels.key` UDM field is set to `Context` and the `properties.Context` log field is mapped to the `principal.resource.attribute.labels.value` UDM field.  
`properties.IsApplicable` | `principal.resource.attribute.labels[is_applicable]` |   
`properties.IsCompliant` | `principal.resource.attribute.labels[is_compliant]` |   
`properties.IsExpectedUserImpact` | `principal.resource.attribute.labels[is_expected_user_impact]` |   
`properties.ConfigurationId` | `principal.resource.product_object_id` |   
`properties.ConfigurationSubcategory` | `principal.resource.resource_subtype` |   
`` | `principal.resource.resource_type` | The `principal.resource.resource_type` UDM field is set to `ACCESS_POLICY`.  
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSecureConfigurationAssessmentKB

The following table lists the log fields for the `DeviceTvmSecureConfigurationAssessmentKB` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `GENERIC_EVENT`.  
`properties.ConfigurationBenchmarks` | `principal.resource.attribute.labels[configuration_benchmarks]` | Iterate for each key, value pair in the `properties.ConfigurationBenchmarks` log field:  
  
The `principal.resource.attribute.labels.key` UDM field is set to `configuration_benchmarks` and the `value` log field is mapped to the `principal.resource.attribute.labels.value` UDM field.  
`properties.ConfigurationCategory` | `principal.resource.attribute.labels[configuration_category]` |   
`properties.ConfigurationDescription` | `principal.resource.attribute.labels[configuration_description]` |   
`properties.ConfigurationImpact` | `principal.resource.attribute.labels[configuration_impact]` |   
`properties.RemediationOptions` | `principal.resource.attribute.labels[remediation_options]` |   
`properties.RiskDescription` | `principal.resource.attribute.labels[risk_description]` |   
`properties.Tags` | `principal.resource.attribute.labels[tags]` |   
`properties.ConfigurationName` | `principal.resource.name` |   
`properties.ConfigurationId` | `principal.resource.product_object_id` |   
`properties.ConfigurationSubcategory` | `principal.resource.resource_subtype` |   
`` | `principal.resource.resource_type` | The `principal.resource.resource_type` UDM field is set to `ACCESS_POLICY`.  
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSoftwareEvidenceBeta 

The following table lists the log fields for the `DeviceTvmSoftwareEvidenceBeta` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `GENERIC_EVENT`.  
`properties.DeviceId` | `principal.asset_id` | The `principal.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.DiskPaths` | `principal.asset.attribute.labels[disk_paths]` | The `properties.DiskPaths` log field is mapped to the `principal.asset.attribute.labels[disk_paths]` UDM field.  
`properties.RegistryPaths` | `principal.asset.attribute.labels[registry_paths]` | The `properties.RegistryPaths` log field is mapped to the `principal.asset.attribute.labels[registry_paths]` UDM field.  
`properties.LastSeenTime` | `principal.asset.last_discover_time` |   
`properties.SoftwareName` | `principal.asset.software.name` |   
`properties.SoftwareVendor` | `principal.asset.software.vendor_name` |   
`properties.SoftwareVersion` | `principal.asset.software.version` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSoftwareInventory 

The following table lists the log fields for the `DeviceTvmSoftwareInventory` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `GENERIC_EVENT`.  
`properties.DeviceId` | `principal.asset_id` | The `principal.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.EndOfSupportDate` | `principal.asset.attribute.labels[end_of_support_date]` |   
`properties.EndOfSupportStatus` | `principal.asset.attribute.labels[end_of_support_status]` |   
`properties.OSArchitecture` | `principal.asset.attribute.labels[os_architecture]` |   
`properties.ProductCodeCpe` | `principal.asset.attribute.labels[product_code_cpe]` |   
`properties.OSPlatform` | `principal.asset.platform_software.platform` | If the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)macos`, then the `principal.asset.platform_software.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)windows`, then the `principal.asset.platform_software.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)linux`, then the `principal.asset.platform_software.platform` UDM field is set to `LINUX`.  
`properties.OSVersion` | `principal.asset.platform_software.platform_version` |   
`properties.SoftwareName` | `principal.asset.software.name` |   
`properties.SoftwareVendor` | `principal.asset.software.vendor_name` |   
`properties.SoftwareVersion` | `principal.asset.software.version` |   
`properties.DeviceName` | `principal.hostname` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSoftwareVulnerabilities

The following table lists the log fields for the `DeviceTvmSoftwareVulnerabilities` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.CveId` | `extensions.vulns.vulnerabilities.cve_id` |   
`properties.VulnerabilitySeverityLevel` | `extensions.vulns.vulnerabilities.severity` | If the `properties.VulnerabilitySeverityLevel` log field value is equal to `High`, then the `extensions.vulns.vulnerabilities.severity` UDM field is set to `HIGH`.  
  
Otherwise, if the `properties.VulnerabilitySeverityLevel` log field value is equal to `Medium`, then the `extensions.vulns.vulnerabilities.severity` UDM field is set to `MEDIUM`.  
  
Otherwise, if the `properties.VulnerabilitySeverityLevel` log field value is equal to `Low`, then the `extensions.vulns.vulnerabilities.severity` UDM field is set to `LOW`.  
  
Otherwise, if the `properties.VulnerabilitySeverityLevel` log field value is equal to `Informational`, then the `extensions.vulns.vulnerabilities.severity` UDM field is set to `INFORMATIONAL`.  
`properties.VulnerabilitySeverityLevel` | `extensions.vulns.vulnerabilities.severity_details` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `SCAN_VULN_HOST`.  
`properties.DeviceId` | `principal.asset_id` | The `principal.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.OSPlatform` | `principal.asset.platform_software.platform` | If the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)macos`, then the `principal.asset.platform_software.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)windows`, then the `principal.asset.platform_software.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)linux`, then the `principal.asset.platform_software.platform` UDM field is set to `LINUX`.  
`properties.OSVersion` | `principal.asset.platform_software.platform_version` |   
`properties.OSArchitecture` | `principal.asset.attribute.labels[OSArchitecture]` |   
`properties.SoftwareName` | `principal.asset.software.name` |   
`properties.SoftwareVendor` | `principal.asset.software.vendor_name` |   
`properties.SoftwareVersion` | `principal.asset.software.version` |   
`properties.DeviceName` | `principal.hostname` |   
`properties.RecommendedSecurityUpdateId` | `security_result.detection_fields[recommended_security_update_id]` |   
`properties.RecommendedSecurityUpdate` | `security_result.detection_fields[recommended_security_update]` |   
`properties.CveTags` | `additional.fields[cve_tags]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSoftwareVulnerabilitiesKB

The following table lists the log fields for the `DeviceTvmSoftwareVulnerabilitiesKB` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `GENERIC_EVENT`.  
`properties.CveId` | `extensions.vulns.vulnerabilities.cve_id` |   
`properties.CvssScore` | `extensions.vulns.vulnerablities.cvss_base_score` |   
`properties.IsExploitAvailable` | `additional.fields[is_exploit_available]` |   
`properties.VulnerabilitySeverityLevel` | `extensions.vulns.vulnerabilities.severity` | If the `properties.VulnerabilitySeverityLevel` log field value is equal to `High`, then the `extensions.vulns.vulnerabilities.severity` UDM field is set to `HIGH`.  
  
Otherwise, if the `properties.VulnerabilitySeverityLevel` log field value is equal to `Medium`, then the `extensions.vulns.vulnerabilities.severity` UDM field is set to `MEDIUM`.  
  
Otherwise, if the `properties.VulnerabilitySeverityLevel` log field value is equal to `Low`, then the `extensions.vulns.vulnerabilities.severity` UDM field is set to `LOW`.  
  
Otherwise, if the `properties.VulnerabilitySeverityLevel` log field value is equal to `Informational`, then the `extensions.vulns.vulnerabilities.severity` UDM field is set to `INFORMATIONAL`.  
  
Otherwise, the `extensions.vulns.vulnerabilities.severity` UDM field is set to `UNKNOWN_SEVERITY`.  
`properties.VulnerabilitySeverityLevel` | `extensions.vulns.vulnerabilities.severity_details` |   
`properties.LastModifiedTime` | `additional.fields[last_modified_time]` |   
`properties.PublishedDate` | `additional.fields[published_date]` |   
`properties.VulnerabilityDescription` | `extensions.vulns.vulnerabilities.cve_description` |   
`properties.AffectedSoftware` | `target.application` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - EmailAttachmentInfo 

The following table lists the log fields for the `EmailAttachmentInfo` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.FileType` | `target.file.mime_type` |   
`properties.FileName` | `target.file.names` |   
`properties.SHA256` | `target.file.sha256` | If the `properties.SHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.SHA256` log field is mapped to the `target.file.sha256` UDM field.  
`properties.FileSize` | `target.file.size` |   
`properties.Timestamp` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `EMAIL_TRANSACTION`.  
`properties.ReportId` | `metadata.product_log_id` |   
`properties.SenderFromAddress` | `network.email.from` | If the `properties.SenderFromAddress` log field value matches the regular expression pattern `^.+@.+$` and the `properties.SenderFromAddress` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.SenderFromAddress` log field is mapped to the `network.email.from` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `SenderFromAddress` and the `properties.SenderFromAddress` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.SenderFromAddress` | `principal.user.email_addresses` | If the `properties.SenderFromAddress` log field value matches the regular expression pattern `^.+@.+$` and the `properties.SenderFromAddress` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.SenderFromAddress` log field is mapped to the `principal.user.email_addresses` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `SenderFromAddress` and the `properties.SenderFromAddress` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.NetworkMessageId` | `network.email.mail_id` |   
`properties.RecipientEmailAddress` | `network.email.to` | If the `properties.RecipientEmailAddress` log field value matches the regular expression pattern `^.+@.+$` and the `properties.RecipientEmailAddress` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.RecipientEmailAddress` log field is mapped to the `network.email.to` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `RecipientEmailAddress` and the `properties.RecipientEmailAddress` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.RecipientEmailAddress` | `target.user.email_addresses` | If the `properties.RecipientEmailAddress` log field value matches the regular expression pattern `^.+@.+$` and the `properties.RecipientEmailAddress` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.RecipientEmailAddress` log field is mapped to the `target.user.email_addresses` UDM field.  
  
Otherwise, the `target.user.attribute.labels.key` UDM field is set to `RecipientEmailAddress` and the `properties.RecipientEmailAddress` log field is mapped to the `target.user.attribute.labels.value` UDM field.  
`properties.SenderObjectId` | `principal.user.product_object_id` |   
`properties.SenderDisplayName` | `principal.user.user_display_name` |   
`properties.ThreatTypes` | `security_result.category` | If the `properties.ThreatTypes` log field value is equal to `Phish`, then the `security_result.category` UDM field is set to `MAIL_PHISHING`.  
  
Otherwise, if the `properties.ThreatTypes` log field value is equal to `Malware`, then the `security_result.category` UDM field is set to `SOFTWARE_MALICIOUS`.  
  
Otherwise, if the `properties.ThreatTypes` log field value is equal to `Spam`, then the `security_result.category` UDM field is set to `MAIL_SPAM`.  
  
Otherwise, the `security_result.category` UDM field is set to `UNKNOWN_CATEGORY`.  
`properties.ThreatTypes` | `security_result.category_details` |   
`properties.DetectionMethods` | `security_result.detection_fields[detection_methods]` |   
`properties.ThreatNames` | `security_result.threat_name` |   
`properties.RecipientObjectId` | `target.user.product_object_id` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - EmailEvents

The following table lists the log fields for the `EmailEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.Timestamp` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `EMAIL_TRANSACTION`.  
`properties.ReportId` | `metadata.product_log_id` |   
`properties.EmailDirection` | `network.direction` | If the `properties.EmailDirection` log field value is equal to `Inbound`, then the `network.direction` UDM field is set to `INBOUND`.  
  
Otherwise, if the `properties.EmailDirection` log field value is equal to `Outbound`, then the `network.direction` UDM field is set to `OUTBOUND`.  
  
Otherwise, the `network.direction` UDM field is set to `UNKNOWN_DIRECTION`, the `additional.fields.key` UDM field is set to `EmailDirection`, and the `properties.EmailDirection` log field value is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.NetworkMessageId` | `network.email.mail_id` |   
`properties.Subject` | `network.email.subject` |   
`properties.DistributionList` | `network.email.to` | If the `properties.RecipientEmailAddress` log field value matches the regular expression pattern `^.+@.+$`, then the `properties.DistributionList` log field is mapped to the `network.email.to` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `DistributionList` and the `properties.DistributionList` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.SenderFromDomain` | `principal.administrative_domain` |   
`properties.SenderIPv4` | `principal.ip` |   
`properties.SenderIPv6` | `principal.ip` |   
`properties.SenderMailFromAddress` | `network.email.reply_to` |   
`properties.SenderFromAddress` | `network.email.from` | If the `properties.SenderFromAddress` log field value matches the regular expression pattern `^.+@.+$` and the `properties.SenderFromAddress` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.SenderFromAddress` log field is mapped to the `network.email.from` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `SenderFromAddress` and the `properties.SenderFromAddress` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.SenderFromAddress` | `principal.user.email_addresses` | If the `properties.SenderFromAddress` log field value matches the regular expression pattern `^.+@.+$` and the `properties.SenderFromAddress` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.SenderFromAddress` log field is mapped to the `principal.user.email_addresses` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `SenderFromAddress` and the `properties.SenderFromAddress` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.SenderMailFromDomain` | `principal.user.attribute.labels[sender_mail_from_domain]` |   
`properties.SenderObjectId` | `principal.user.product_object_id` |   
`properties.SenderDisplayName` | `principal.user.user_display_name` |   
`properties.ThreatTypes` | `security_result.category` | If the `properties.ThreatTypes` log field value is equal to `Phish`, then the `security_result.category` UDM field is set to `MAIL_PHISHING`.  
  
Otherwise, if the `properties.ThreatTypes` log field value is equal to `Malware`, then the `security_result.category` UDM field is set to `SOFTWARE_MALICIOUS`.  
  
Otherwise, if the `properties.ThreatTypes` log field value is equal to `Spam`, then the `security_result.category` UDM field is set to `MAIL_SPAM`.  
  
Otherwise, the `security_result.category` UDM field is set to `UNKNOWN_CATEGORY`.  
`properties.ThreatTypes` | `security_result.category_details` |   
`properties.ConfidenceLevel` | `security_result.confidence_details` |   
`properties.EmailAction` | `security_result.description` |   
`properties.AuthenticationDetails` | `security_result.detection_fields[authentication_details]` |   
`properties.BulkComplaintLevel` | `security_result.detection_fields[bulk_complaint_level]` |   
`properties.DetectionMethods` | `security_result.detection_fields[detection_methods]` |   
`properties.EmailActionPolicyGuid` | `security_result.rule_id` |   
`properties.EmailActionPolicy` | `security_result.rule_name` |   
`properties.ThreatNames` | `security_result.threat_name` |   
`properties.OrgLevelAction` | `security_result.rule_labels[org_level_action]` |   
`properties.OrgLevelPolicy` | `security_result.rule_labels[org_level_policy]` |   
`properties.UserLevelAction` | `security_result.rule_labels[user_level_action]` |   
`properties.UserLevelPolicy` | `security_result.rule_labels[user_level_policy]` |   
`properties.RecipientEmailAddress` | `network.email.to` | If the `properties.RecipientEmailAddress` log field value matches the regular expression pattern `^.+@.+$` and the `properties.RecipientEmailAddress` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.RecipientEmailAddress` log field is mapped to the `network.email.to` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `RecipientEmailAddress` and the `properties.RecipientEmailAddress` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.RecipientEmailAddress` | `target.user.email_addresses` | If the `properties.RecipientEmailAddress` log field value matches the regular expression pattern `^.+@.+$` and the `properties.RecipientEmailAddress` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.RecipientEmailAddress` log field is mapped to the `target.user.email_addresses` UDM field.  
  
Otherwise, the `target.user.attribute.labels.key` UDM field is set to `RecipientEmailAddress` and the `properties.RecipientEmailAddress` log field is mapped to the `target.user.attribute.labels.value` UDM field.  
`properties.RecipientObjectId` | `target.user.product_object_id` |   
`properties.AdditionalFields` | `additional.fields[additional_fields]` |   
`properties.DeliveryAction` | `security_result.action` | If the `properties.DeliveryAction` log field value is equal to `Delivered`, then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, if the `properties.DeliveryAction` log field contains one of the following values:

  * `Junked`
  * `Replaced`

then the `security_result.action` UDM field is set to `ALLOW_WITH_MODIFICATION`.  
  
Otherwise, if the `properties.DeliveryAction` log field value is equal to `Blocked`, then the `security_result.action` UDM field is set to `BLOCK`.  
  
Otherwise, the `security_result.action` UDM field is set to `UNKNOWN_ACTION`.  
`properties.DeliveryAction` | `security_result.action_details` |   
`properties.DeliveryLocation` | `additional.fields[delivery_location]` | The `properties.DeliveryLocation` log field is mapped to the `additional.fields[delivery_location]` UDM field.  
`properties.EmailClusterId` | `additional.fields[email_cluster_id]` |   
`properties.EmailLanguage` | `additional.fields[email_language]` |   
`properties.InternetMessageId` | `additional.fields[internet_message_id]` |   
`properties.LatestDeliveryLocation` | `additional.fields[last_delivery_location]` |   
`properties.UrlCount` | `additional.fields[url_count]` |   
`properties.Connectors` | `additional.fields[connectors]` |   
`properties.AttachmentCount` | `additional.fields[attachment_count]` |   
`properties.LatestDeliveryAction` | `additional.fields[latest_delivery_action]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - EmailPostDeliveryEvents 

The following table lists the log fields for the `EmailPostDeliveryEvents` log type and their corresponding UDM fields: 

Log field | UDM mapping | Logic  
---|---|---  
`properties.Timestamp` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `EMAIL_TRANSACTION`.  
`properties.ReportId` | `security_result.detection_fields[report_id]` |   
`properties.NetworkMessageId` | `network.email.mail_id` |   
`properties.ActionResult` | `security_result.summary` |   
`properties.ThreatTypes` | `security_result.category` | If the `properties.ThreatTypes` log field value is equal to `Phish`, then the `security_result.category` UDM field is set to `MAIL_PHISHING`.  
  
Otherwise, if the `properties.ThreatTypes` log field value is equal to `Malware`, then the `security_result.category` UDM field is set to `SOFTWARE_MALICIOUS`.  
  
Otherwise, if the `properties.ThreatTypes` log field value is equal to `Spam`, then the `security_result.category` UDM field is set to `MAIL_SPAM`.  
  
Otherwise, the `security_result.category` UDM field is set to `UNKNOWN_CATEGORY`.  
`properties.ThreatTypes` | `security_result.category_details` |   
`properties.ActionTrigger` | `security_result.detection_fields[action_trigger]` |   
`properties.DeliveryLocation` | `security_result.detection_fields[delivery_location]` |   
`properties.DetectionMethods` | `security_result.detection_fields[detection_methods]` |   
`properties.Action` | `security_result.action` | If the `properties.Action` log field value is equal to `Moved to quarantine`, then the `security_result.action` UDM field is set to `QUARANTINE`.  
  
Otherwise, if the `properties.Action` log field value is equal to `Added message info only`, then the `security_result.action` UDM field is set to `ALLOW_WITH_MODIFICATION`.  
  
Otherwise, if the `properties.Action` log field value is equal to `Quarantine release`, then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, if the `properties.Action` log field value is equal to `Moved to junk folder`, then the `security_result.action` UDM field is set to `ALLOW_WITH_MODIFICATION`.  
  
Otherwise, if the `properties.Action` log field value is equal to `Reprocessed`, then the `security_result.action` UDM field is set to `CHALLENGE`.  
  
Otherwise, the `security_result.action` UDM field is set to `UNKNOWN_ACTION`.  
`properties.Action` | `security_result.action_details` |   
`properties.ActionType` | `security_result.verdict_info.verdict_type` | If the `properties.ActionType` log field value is equal to `Manual Remediation`, then the `security_result.verdict_info.verdict_type` UDM field is set to `ANALYST_VERDICT`.  
  
Otherwise, if the `properties.ActionType` log field contains one of the following values, then the `security_result.verdict_info.verdict_type` UDM field is set to `PROVIDER_ML_VERDICT`:

  * `Phish ZAP`
  * `Malware ZAP`
  * `Spam ZAP`

Otherwise, the `security_result.verdict_info.verdict_type` UDM field is set to `VERDICT_TYPE_UNSPECIFIED`.  
`properties.RecipientEmailAddress` | `network.email.to` | If the `properties.RecipientEmailAddress` log field value matches the regular expression pattern `^.+@.+$`, then the `properties.RecipientEmailAddress` log field is mapped to the `network.email.to` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `RecipientEmailAddress` and the `properties.RecipientEmailAddress` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.RecipientEmailAddress` | `target.user.email_addresses` | If the `properties.RecipientEmailAddress` log field value matches the regular expression pattern `^.+@.+$` and the `properties.RecipientEmailAddress` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.RecipientEmailAddress` log field is mapped to the `target.user.email_addresses` UDM field.  
  
Otherwise, the `target.user.attribute.labels.key` UDM field is set to `RecipientEmailAddress` and the `properties.RecipientEmailAddress` log field is mapped to the `target.user.attribute.labels.value` UDM field.  
`properties.InternetMessageId` | `additional.fields[internet_message_id]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - EmailUrlInfo

The following table lists the log fields for the `EmailUrlInfo` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.UrlDomain` | `target.hostname` |   
`properties.Url` | `target.url` |   
`properties.Timestamp` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `EMAIL_TRANSACTION`.  
`properties.ReportId` | `metadata.product_log_id` |   
`properties.NetworkMessageId` | `network.email.mail_id` |   
`properties.UrlLocation` | `additional.fields[url_location]` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - IdentityInfo 

The following table lists the log fields for the `IdentityInfo` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.BlastRadius` | `entity.user.attribute.labels[blast_radius]` |   
`properties.CompanyName` | `entity.user.company_name` |   
`properties.CriticalityLevel` | `entity.user.attribute.labels[criticality_level]` |   
`properties.DeletedDateTime` | `entity.user.attribute.labels[deleted_date_time]` |   
`properties.EmployeeId` | `entity.user.employee_id` |   
`properties.GroupMembership` | `entity.user.group_identifiers` |   
`properties.IdentityEnvironment` | `entity.user.attribute.labels[identity_environment]` |   
`properties.OnPremObjectId` | `entity.user.attribute.labels[on_prem_object_id]` |   
`properties.OtherMailAddresses` | `entity.user.email_addresses` | If the `properties.OtherMailAddresses` log field value matches the regular expression pattern `^.+@.+$` and the `properties.OtherMailAddresses` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.OtherMailAddresses` log field is mapped to the `entity.user.email_addresses` UDM field.  
  
Otherwise, the `entity.user.attribute.labels.key` UDM field is set to `OtherMailAddresses` and the `properties.OtherMailAddresses` log field is mapped to the `entity.user.attribute.labels.value` UDM field.  
`properties.PrivilegedEntraPimRoles` | `entity.user.attribute.roles.name` |   
`properties.RiskLevel` | `entity.user.attribute.labels[risk_level]` |   
`properties.RiskLevelDetails` | `entity.user.attribute.labels[risk_level_details]` |   
`properties.RiskStatus` | `entity.user.attribute.labels[risk_status]` |   
`properties.SourceProviders` | `entity.user.attribute.labels[source_providers]` |   
`properties.State` | `entity.user.personal_address.state` |   
`properties.TenantMembershipType` | `entity.user.attribute.labels[tenant_membership_type]` |   
`properties.UserAccountControl` | `entity.user.attribute.labels[user_account_control]` |   
`properties.SourceSystem` | `entity.resource.parent` |   
`properties.AccountDomain` | `entity.administrative_domain` |   
`properties.TenantId` | `entity.resource.product_object_id` |   
`properties.CreatedDateTime` | `entity.user.attribute.creation_time` |   
`properties.AccountUpn` | `entity.user.attribute.labels[account_upn]` |   
`properties.ChangeSource` | `entity.user.attribute.labels[change_source]` |   
`properties.CloudSid` | `entity.user.attribute.labels[cloud_sid]` |   
`properties.ReportId` | `entity.user.attribute.labels[report_id]` |   
`properties.SipProxyAddress` | `entity.user.attribute.labels[sip_proxy_address]` |   
`properties.SourceProvider` | `entity.user.attribute.labels[source_provider]` |   
`properties.Tags` | `entity.user.attribute.labels[tags]` |   
`properties.Type` | `entity.user.account_type` | If the `properties.Type` log field is equal to `User`, then the `entity.user.account_type` UDM field is set to `DOMAIN_ACCOUNT_TYPE`.  
  
Otherwise, if the `properties.Type` log field is equal to `ServiceAccount`, then the `entity.user.account_type` UDM field is set to `SERVICE_ACCOUNT_TYPE`.  
`properties.Type` | `entity.user.attribute.labels[type]` |   
`properties.DistinguishedName` | `entity.user.attribute.labels[distinguished_name]` |   
`properties.Department` | `entity.user.department` |   
`properties.EmailAddress` | `entity.user.email_addresses` | If the `properties.EmailAddress` log field value matches the regular expression pattern `^.+@.+$` and the `properties.EmailAddress` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.EmailAddress` log field is mapped to the `entity.user.email_addresses` UDM field.  
  
Otherwise, the `entity.user.attribute.labels.key` UDM field is set to `EmailAddress` and the `properties.EmailAddress` log field is mapped to the `entity.user.attribute.labels.value` UDM field.  
`properties.GivenName` | `entity.user.first_name` |   
`properties.Surname` | `entity.user.last_name` |   
`properties.Manager` | `entity.user.managers.user_display_name` |   
`properties.City` | `entity.user.personal_address.city` |   
`properties.Country` | `entity.user.personal_address.country_or_region ` |   
`properties.Address` | `entity.user.personal_address.name` |   
`properties.Phone` | `entity.user.phone_numbers` |   
`properties.AccountObjectId` | `entity.user.product_object_id` |   
`properties.AssignedRoles` | `entity.user.role_description` |   
`properties.JobTitle` | `entity.user.title` |   
`properties.IsAccountEnabled` | `entity.user.user_authentication_status` | If the `properties.IsAccountEnabled` log field value is equal to `1` or `true`, then the `entity.user.user_authentication_status` UDM field is set to `ACTIVE`.  
  
Otherwise, the `entity.user.user_authentication_status` UDM field is set to `SUSPENDED`.  
`properties.AccountDisplayName` | `entity.user.user_display_name` |   
`properties.AccountName` | `entity.user.userid` |   
`properties.OnPremSid` | `entity.user.attribute.labels[on_prem_sid]` |   
`properties.Timestamp` | `metadata.creation_time` |   
`` | `metadata.entity_type` | The `metadata.entity_type` UDM field is set to `USER`.  
`properties.AccountObjectId` | `metadata.product_entity_id` |   
  
### Field mapping reference: MICROSOFT DEFENDER ENDPOINT - CloudAppEvents 

The following table lists the log fields for the `CloudAppEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.Timestamp` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `GENERIC_EVENT`.  
`properties.ActionType` | `security_result.action` | If the `properties.ActionType` log field contains one of the following values:

  * `AttachmentAccess`
  * `Create`
  * `MailItemsAccessed`
  * `New-InboxRule`
  * `Send`
  * `Update`

then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, the `security_result.action` UDM field is set to `UNKNOWN_ACTION`.  
`properties.ActionType` | `security_result.summary` |   
`properties.Application` | `additional.fields[application]` |   
`properties.ApplicationId` | `additional.fields[application_id]` |   
`properties.AppInstanceId` | `additional.fields[app_instance_id]` |   
`properties.AccountObjectId` | `principal.user.product_object_id` |   
`properties.AccountId` | `principal.user.userid` |   
`properties.AccountDisplayName` | `principal.user.user_display_name` |   
`properties.IsAdminOperation` | `principal.user.attribute.role.type` | If the `properties.IsAdminOperation` is equal to `true`, then the `principal.user.attribute.role.type` is set to `ADMINISTRATOR`.  
`properties.DeviceType` | `principal.asset.type` | If the `properties.DeviceType` log field value is equal to `NetworkDevice`, then the `principal.asset.type` UDM field is set to `NETWORK_ATTACHED_STORAGE`.  
Otherwise, if the `properties.DeviceType` log field value is equal to `Workstation`, then the `principal.asset.type` UDM field is set to `WORKSTATION`.  
Otherwise, if the `properties.DeviceType` log field value is equal to `Server`, then the `principal.asset.type` UDM field is set to `SERVER`.  
Otherwise, if the `properties.DeviceType` log field value is equal to `Mobile`, then the `principal.asset.type` UDM field is set to `MOBILE`.  
Otherwise, if the `properties.DeviceType` log field value is equal to `Printer`, then the `principal.asset.type` UDM field is set to `PRINTER`.  
Otherwise, the `principal.asset.type` UDM field is set to `ROLE_UNSPECIFIED` and `properties.DeviceType` is mapped to `principal.asset.attribute.labels[device_type]`.  
`properties.OSPlatform` | `principal.asset.platform_software.platform` | If the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)macos`, then the `principal.asset.platform_software.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)windows`, then the `principal.asset.platform_software.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.OSPlatform` log field value matches the regular expression pattern `(?i)linux`, then the `principal.asset.platform_software.platform` UDM field is set to `LINUX`.  
`properties.OSPlatform` | `principal.asset.platform_software.platform_version` |   
`properties.IPAddresses` | `principal.ip` |   
`properties.IsAnonymousProxy` | `additional.fields[IsAnonymousProxy]` |   
`properties.CountryCode` | `principal.ip_geo_artifact.location.country_or_region` |   
`properties.City` | `principal.ip_geo_artifact.location.city` |   
`properties.Isp` | `network.carrier_name` |   
`properties.UserAgent` | `network.http.user_agent` |   
`properties.ActivityType` | `additional.fields[activity_type]` |   
`properties.ActivityObjects` | `additional.fields[activity_objects]` |   
`properties.ObjectName` | `target.resource.name` |   
`properties.ObjectType` | `target.resource.resource_subtype` |   
`properties.ObjectId` | `target.resource.product_object_id` |   
`properties.ReportId` | `metadata.product_log_id` |   
`properties.AccountType` | `principal.asset.attribute.labels[account_type]` | The `properties.AccountType` log field is mapped to the `principal.asset.attribute.labels[account_type]` UDM field.  
`properties.IsExternalUser` | `principal.asset.attribute.labels[is_external_user]` | The `properties.IsExternalUser` log field is mapped to the `principal.asset.attribute.labels[is_external_user]` UDM field.  
`properties.IsImpersonated` | `principal.asset.attribute.labels[is_impersonated]` | The `properties.IsImpersonated` log field is mapped to the `principal.asset.attribute.labels[is_impersonated]` UDM field.  
`properties.IPTags` | `principal.asset.attribute.labels[ip_tags]` | Iterate through log field `properties.IPTags`:  
  
The `principal.asset.attribute.labels.key` UDM field is set to a value generated from the template `ip _tags_ %{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.IPTags` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`properties.IPCategory` | `additional.fields[IPCategory]` |   
`properties.UserAgentTags` | `principal.asset.attribute.labels[user_agent_tags]` | Iterate through log field `properties.UserAgentTags`:  
  
The `principal.asset.attribute.labels.key` UDM field is set to a value generated from the template `user_agent _tags_ %{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.UserAgentTags` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`properties.RawEventData` | `additional.fields[raw_event_data]` | Iterate for each key, value pair of log field `properties.RawEventData`:  
  
The `key` log field is mapped to the `additional.fields.key` UDM field and the `value` log field is mapped to the `additional.fields.value.string _value_` UDM field.  
  
Iterate for each key1, value1 pair of log field `value`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `%{key}%{key1}`, where `%{key}` and `%{key1}` are replaced with the values of the `key` and `key1` log fields, and the `value1` log field is mapped to the `additional.fields.value.string _value_` UDM field.  
  
Iterate for each key2, value2 pair of log field `value1`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `%{key}%{key1}_%{key2}`, where `%{key}`, `%{key1}`, and `%{key2}` are replaced with the values of the `key`, `key1`, and `key2` log fields, and the `value2` log field is mapped to the `additional.fields.value.string _value_` UDM field.  
  
Iterate for each key3, value3 pair of log field `value2`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `%{key}%{key1}_%{key2}_ %{index}_%{key3}`, where `%{key}`, `%{key1}`, `%{key2}`, `%{index}`, and `%{key3}` are replaced with the values of the `key`, `key1`, `key2`, `index`, and `key3` log fields, and the `value3` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields` | `additional.fields[additional_fields]` | Iterate for each key, value pair of log field `properties.AdditionalFields`, then   
`value` log field is mapped to the `additional.fields.key` UDM field.  
`properties.LastSeenForUser` | `principal.user.attribute.labels[last_seen_for_user]` | Iterate for each key, value pair of log field `properties.LastSeenForUser`:  
  
The `key` log field is mapped to the `principal.user.attribute.labels.key` UDM field and the `value` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.UncommonForUser` | `principal.user.attribute.labels[uncommon_for_user]` | Iterate through log field `properties.UncommonForUser`:  
  
The `principal.user.attribute.labels.key` UDM field is set to a value generated from the template `uncommon_for _user_ %{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.UncommonForUser` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.AuditSource` | `additional.fields[audit_source]` |   
`properties.SessionData` | `additional.fields[session_data]` |   
`properties.OAuthAppId` | `additional.fields[oauth_app_id]` |   
  
## AdditionalFields mapping reference

This section explains how the Google Security Operations parser maps nested fields from the `AdditionalFields` raw log field for Microsoft Defender for Endpoint to Google Security Operations UDM fields.

### AdditionalFields mapping reference: MICROSOFT DEFENDER ENDPOINT - AlertEvidence

The following table lists the `AdditionalFields` log fields for the `AlertEvidence` log type and their corresponding UDM fields:   
  


Entity Type | Log field | UDM mapping | Logic  
---|---|---|---  
`CloudLogonRequest` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`CloudLogonRequest` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`CloudLogonRequest` | `properties.AdditionalFields.RequestId` | `additional.fields[RequestId]` |   
`CloudLogonRequest` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`CloudLogonRequest` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.$id` | `additional.fields[Account_$id]` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.AadTenantId` | `target.user.attribute.labels[Account_AadTenantId]` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.AadUserId` | `target.user.attribute.labels[Account_AadUserId]` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.DisplayName` | `target.user.user_display_name` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.IsDomainJoined` | `target.user.attribute.labels[Account_IsDomainJoined]` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.MergeByKey` | `additional.fields[Account_MergeByKey]` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.MergeByKeyHex` | `additional.fields[Account_MergeByKeyHex]` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.Name` | `target.user.userid` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.NTDomain` | `target.administrative_domain` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.Role` | `additional.fields[Account_Role]` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.Sid` | `target.user.windows_sid` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.Type` | `target.user.attribute.labels[Account_Type]` |   
`CloudLogonSession` | `properties.AdditionalFields.Account.UPNSuffix` | `target.user.attribute.labels[Account_UPNSuffix]` |   
`CloudLogonSession` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`CloudLogonSession` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`CloudLogonSession` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`CloudLogonSession` | `properties.AdditionalFields.SessionId` | `network.session_id` |   
`CloudLogonSession` | `properties.AdditionalFields.StartTimeUtc` | `additional.fields[StartTimeUtc]` |   
`CloudLogonSession` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`CloudLogonSession` | `properties.AdditionalFields.UserAgent` | `network.http.user_agent` |   
`RegistryValue` | `properties.AdditionalFields.CreatedTimeUtc` | `additional.fields[CreatedTimeUtc]` |   
`RegistryValue` | `properties.AdditionalFields.DetectionStatus` | `security_result.detection_fields[DetectionStatus]` |   
`RegistryValue` | `properties.AdditionalFields.Host.$id` | `additional.fields[Host_$id]` |   
`RegistryValue` | `properties.AdditionalFields.Host.Asset` | `principal.asset.attribute.labels[Host_Asset]` |   
`RegistryValue` | `properties.AdditionalFields.Host.DetailedRoles` | `principal.asset.attribute.labels[Host_DetailedRoles]` | Iterate through log field `properties.AdditionalFields.Host.DetailedRoles`:  
  
The `principal.asset.attribute.labels.key` UDM field is set to `Host_DetailedRoles` and the `properties.AdditionalFields.Host.DetailedRoles` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.DetectionStatus` | `security_result.detection_fields[Host_DetectionStatus]` |   
`RegistryValue` | `properties.AdditionalFields.Host.DnsDomain` | `principal.administrative_domain` | If the `properties.AccountDomain` log field value is empty, then the `properties.AdditionalFields.Host.DnsDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
  
Otherwise, the `principal.asset.attribute.labels.key` UDM field is set to `Host_DnsDomain` and the `properties.AdditionalFields.Host.DnsDomain` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.EnrichmentType` | `additional.fields[Host_EnrichmentType]` |   
`RegistryValue` | `properties.AdditionalFields.Host.HostMachineId,properties.AdditionalFields.Host.MachineId` | `principal.asset.product_object_id` | If the `properties.AdditionalFields.Host.MachineId` log field value is _not_ empty, then the `properties.AdditionalFields.Host.MachineId` log field is mapped to the `principal.asset.product_object_id` UDM field. If the `properties.AdditionalFields.Host.HostMachineId` log field value is _not_ empty, then the `principal.asset.attribute.labels.key` UDM field is set to `Host_HostMachineId` and the `properties.AdditionalFields.Host.HostMachineId` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
  
Otherwise, the `properties.AdditionalFields.Host.HostMachineId` log field is mapped to the `principal.asset.product_object_id` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.IpInterfaces.$id` | `additional.fields[Host_IpInterfaces_$id]` | Iterate through log field `properties.AdditionalFields.Host.IpInterfaces`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Host_IpInterfaces_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Host.IpInterfaces.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.IpInterfaces.Address` | `principal.ip` | Iterate through log field `properties.AdditionalFields.Host.IpInterfaces`:  
  
The `valid_ipinterface_address` field is extracted from `properties.AdditionalFields.Host.IpInterfaces.Address` log field using the Grok pattern. The `valid_ipinterface_address` log field is mapped to the `principal.ip` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.IpInterfaces.Type` | `additional.fields[Host_IpInterfaces_Type]` | Iterate through log field `properties.AdditionalFields.Host.IpInterfaces`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Host_IpInterfaces_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Host.IpInterfaces.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.IsDomainJoined` | `principal.asset.attribute.labels[Host_IsDomainJoined]` |   
`RegistryValue` | `properties.AdditionalFields.Host.IsIoc` | `security_result.detection_fields[Host_IsIoc]` |   
`RegistryValue` | `properties.AdditionalFields.Host.LastRemediationState` | `security_result.detection_fields[Host_LastRemediationState]` |   
`RegistryValue` | `properties.AdditionalFields.Host.LastVerdict` | `security_result.detection_fields[Host_LastVerdict]` |   
`RegistryValue` | `properties.AdditionalFields.Host.LeadingHost` | `principal.asset.attribute.labels[Host_LeadingHost]` |   
`RegistryValue` | `properties.AdditionalFields.Host.MachineIdType` | `principal.asset.attribute.labels[Host_MachineIdType]` |   
`RegistryValue` | `properties.AdditionalFields.Host.MergeByKey` | `additional.fields[Host_MergeByKey]` |   
`RegistryValue` | `properties.AdditionalFields.Host.MergeByKeyHex` | `additional.fields[Host_MergeByKeyHex]` |   
`RegistryValue` | `properties.AdditionalFields.Host.Metadata.MachineEnrichmentInfo` | `additional.fields[Host_Metadata_MachineEnrichmentInfo]` |   
`RegistryValue` | `properties.AdditionalFields.Host.NetBiosName` | `principal.asset.attribute.labels[Host_NetBiosName]` |   
`RegistryValue` | `properties.AdditionalFields.Host.OSFamily` | `principal.platform` | If the `properties.AdditionalFields.Host.OSFamily` log field value is equal to `Windows`, then the `principal.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.AdditionalFields.Host.OSFamily` log field value is equal to `Mac`, then the `principal.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.AdditionalFields.Host.OSFamily` log field value is equal to `Linux`, then the `principal.platform` UDM field is set to `LINUX`.  
`RegistryValue` | `properties.AdditionalFields.Host.OSVersion` | `principal.platform_version` |   
`RegistryValue` | `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[Host_RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`RegistryValue` | `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[Host_RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Host_RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[Host_RbacScopes_ScopesPerType_Workloads_Mode]` |   
`RegistryValue` | `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[Host_RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Host_RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.RemediationProviders.RemediationDate` | `security_result.detection_fields[Host_RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.Host.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_RemediationProviders_RemediationDate` and the `properties.AdditionalFields.Host.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.RemediationProviders.RemediationState` | `security_result.detection_fields[Host_RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.Host.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_RemediationProviders_RemediationState` and the `properties.AdditionalFields.Host.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.RemediationProviders.Type` | `security_result.detection_fields[Host_RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.Host.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_RemediationProviders_Type` and the `properties.AdditionalFields.Host.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.Role` | `additional.fields[Host_Role]` |   
`RegistryValue` | `properties.AdditionalFields.Host.SuspicionLevel` | `security_result.detection_fields[Host_SuspicionLevel]` |   
`RegistryValue` | `properties.AdditionalFields.Host.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[Host_ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.Host.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.Host.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[Host_ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.Host.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.Host.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Host.Type` | `additional.fields[Host_Type]` |   
`RegistryValue` | `properties.AdditionalFields.IsIoc` | `security_result.detection_fields[IsIoc]` |   
`RegistryValue` | `properties.AdditionalFields.Key.$id` | `additional.fields[Key_$id]` |   
`RegistryValue` | `properties.AdditionalFields.Key.Hive, properties.AdditionalFields.Key.Key` | `target.registry.registry_key` | If the `properties.AdditionalFields.Key.Hive` log field value is _not_ empty and the `properties.RegistryKey` log field value is empty, then the `target.registry.registry_key` UDM field is set to a value generated from the template `%{properties.AdditionalFields.Key.Hive}\%{properties.AdditionalFields.Key.Key}`, where `%{properties.AdditionalFields.Key.Hive}` and `%{properties.AdditionalFields.Key.Key}` are replaced with the values of the `properties.AdditionalFields.Key.Hive` and `properties.AdditionalFields.Key.Key` log fields. The `security_result.detection_fields.key` UDM field is set to `Key_Hive` and the `properties.AdditionalFields.Key.Hive` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Key.Key` | `security_result.detection_fields[Key_Key]` |   
`RegistryValue` | `properties.AdditionalFields.Key.Type` | `additional.fields[Key_Type]` |   
`RegistryValue` | `properties.AdditionalFields.LastRemediationState` | `security_result.detection_fields[LastRemediationState]` |   
`RegistryValue` | `properties.AdditionalFields.LastVerdict` | `security_result.threat_verdict` | If the `properties.AdditionalFields.LastVerdict` log field value is equal to `Suspicious`, then the `security_result.threat_verdict` UDM field is set to `SUSPICIOUS`.  
  
Otherwise, if the `properties.AdditionalFields.LastVerdict` log field value is equal to `Malicious`, then the `security_result.threat_verdict` UDM field is set to `MALICIOUS`.  
`RegistryValue` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`RegistryValue` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`RegistryValue` | `properties.AdditionalFields.Name` | `target.registry.registry_value_name` | If the `properties.RegistryValueName` log field value is empty, then the `properties.AdditionalFields.Name` log field is mapped to the `target.registry.registry_value_name` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `Name` and the `properties.AdditionalFields.Name` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`RegistryValue` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Mode]` |   
`RegistryValue` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.ReferenceId` | `additional.fields[ReferenceId]` |   
`RegistryValue` | `properties.AdditionalFields.RemediationProviders.RemediationDate` | `security_result.detection_fields[RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationDate` and the `properties.AdditionalFields.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.RemediationProviders.RemediationState` | `security_result.detection_fields[RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationState` and the `properties.AdditionalFields.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.RemediationProviders.Type` | `security_result.detection_fields[RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_Type` and the `properties.AdditionalFields.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`RegistryValue` | `properties.AdditionalFields.SuspicionLevel` | `security_result.detection_fields[SuspicionLevel]` |   
`RegistryValue` | `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.Count of ThreatAnalysisSummary` | `security_result.detection_fields[Count_of_ThreatAnalysisSummary]` |   
`RegistryValue` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`RegistryValue` | `properties.AdditionalFields.Value` | `target.registry.registry_value_data` | If the `properties.RegistryValueData` log field value is empty, then the `properties.AdditionalFields.Value` log field is mapped to the `target.registry.registry_value_data` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `Value` and the `properties.AdditionalFields.Value` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`RegistryValue` | `properties.AdditionalFields.ValueType` | `additional.fields[ValueType]` |   
`SecurityGroup` | `properties.AdditionalFields.EdgeRole` | `additional.fields[EdgeRole]` |   
`SecurityGroup` | `properties.AdditionalFields.FriendlyName` | `target.group.group_display_name` |   
`SecurityGroup` | `properties.AdditionalFields.Id` | `additional.fields[Id]` |   
`SecurityGroup` | `properties.AdditionalFields.IsValid` | `additional.fields[IsValid]` |   
`SecurityGroup` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`SecurityGroup` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`SecurityGroup` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`SecurityGroup` | `properties.AdditionalFields.Roles` | `additional.fields[Roles]` | Iterate through log field `properties.AdditionalFields.Roles`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Roles_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Roles` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`SecurityGroup` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`Process` | `properties.AdditionalFields.Account.$id` | `additional.fields[Account_$id]` |   
`Process` | `properties.AdditionalFields.Account.AadUserId` | `target.user.attribute.labels[Account_AadUserId]` |   
`Process` | `properties.AdditionalFields.Account.Asset` | `principal.asset.attribute.labels[Account_Asset]` |   
`Process` | `properties.AdditionalFields.Account.DetectionStatus` | `security_result.detection_fields[Account_DetectionStatus]` |   
`Process` | `properties.AdditionalFields.Account.Host.$ref` | `additional.fields[Account_Host_$ref]` |   
`Process` | `properties.AdditionalFields.Account.IsDomainJoined` | `target.user.attribute.labels[Account_IsDomainJoined]` |   
`Process` | `properties.AdditionalFields.Account.IsIoc` | `security_result.detection_fields[Account_IsIoc]` |   
`Process` | `properties.AdditionalFields.Account.LastRemediationState` | `security_result.detection_fields[Account_LastRemediationState]` |   
`Process` | `properties.AdditionalFields.Account.LastVerdict` | `security_result.detection_fields[Account_LastVerdict]` |   
`Process` | `properties.AdditionalFields.Account.MergeByKey` | `additional.fields[Account_MergeByKey]` |   
`Process` | `properties.AdditionalFields.Account.MergeByKeyHex` | `additional.fields[Account_MergeByKeyHex]` |   
`Process` | `properties.AdditionalFields.Account.Name` | `target.user.userid` |   
`Process` | `properties.AdditionalFields.Account.NTDomain,properties.AdditionalFields.ImageFile.Host.DnsDomain` | `target.administrative_domain` | If the `properties.AdditionalFields.Account.NTDomain` log field value is _not_ empty, then the `properties.AdditionalFields.Account.NTDomain` log field is mapped to the `target.administrative_domain` UDM field and the `additional.fields.key` UDM field is set to `ImageFile_Host_DnsDomain` and the `properties.AdditionalFields.ImageFile.Host.DnsDomain` log field is mapped to the `additional.fields.value.string_value` UDM field.  
  
Otherwise, the `properties.AdditionalFields.ImageFile.Host.DnsDomain` log field is mapped to the `target.administrative_domain` UDM field.  
`Process` | `properties.AdditionalFields.Account.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[Account_RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`Process` | `properties.AdditionalFields.Account.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[Account_RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.Account.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Account_RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Account.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.Account.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[Account_RbacScopes_ScopesPerType_Workloads_Mode]` |   
`Process` | `properties.AdditionalFields.Account.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[Account_RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.Account.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Account_RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Account.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.Account.ReferenceId` | `additional.fields[Account_ReferenceId]` |   
`Process` | `properties.AdditionalFields.Account.RemediationProviders.RemediationDate` | `security_result.detection_fields[Account_RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.Account.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `Account_RemediationProviders_RemediationDate` and the `properties.AdditionalFields.Account.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.Account.RemediationProviders.RemediationState` | `security_result.detection_fields[Account_RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.Account.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `Account_RemediationProviders_RemediationState` and the `properties.AdditionalFields.Account.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.Account.RemediationProviders.Type` | `security_result.detection_fields[Account_RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.Account.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `Account_RemediationProviders_Type` and the `properties.AdditionalFields.Account.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.Account.Role` | `additional.fields[Account_Role]` |   
`Process` | `properties.AdditionalFields.Account.Sid` | `target.user.windows_sid` |   
`Process` | `properties.AdditionalFields.Account.SuspicionLevel` | `security_result.detection_fields[Account_SuspicionLevel]` |   
`Process` | `properties.AdditionalFields.Account.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[Account_ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.Account.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `Account_ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.Account.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.Account.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[Account_ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.Account.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `Account_ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.Account.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.Account.Type` | `target.user.attribute.labels[Account_Type]` |   
`Process` | `properties.AdditionalFields.Account.UPNSuffix` | `target.user.attribute.labels[UPNSuffix]` |   
`Process` | `properties.AdditionalFields.Account.UserPrincipalName` | `target.user.email_addresses` |   
`Process` | `properties.AdditionalFields.CommandLine` | `target.process.command_line` | If the `properties.ProcessCommandLine` log field value is empty, then the `properties.AdditionalFields.CommandLine` log field is mapped to the `target.process.command_line` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `CommandLine` and the `properties.AdditionalFields.CommandLine` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.CreatedTimeUtc` | `additional.fields[CreatedTimeUtc]` |   
`Process` | `properties.AdditionalFields.CreationTimeUtc` | `additional.fields[process_creation_time]` |   
`Process` | `properties.AdditionalFields.DetectionStatus` | `security_result.detection_fields[DetectionStatus]` |   
`Process` | `properties.AdditionalFields.ElevationToken` | `target.process.token_elevation_type` | If the `properties.AdditionalFields.ElevationToken` log field value is equal to `Full`, then the `target.process.token_elevation_type` UDM field is set to `TYPE_1`.  
  
Otherwise, if the `properties.AdditionalFields.ElevationToken` log field value is equal to `Limited`, then the `target.process.token_elevation_type` UDM field is set to `TYPE_3`.  
  
Otherwise, the `target.process.token_elevation_type` UDM field is set to `UNKNOWN`.  
`Process` | `properties.AdditionalFields.Host.$ref` | `additional.fields[Host_$ref]` |   
`Process` | `properties.AdditionalFields.ImageFile.$id` | `additional.fields[ImageFile_$id]` |   
`Process` | `properties.AdditionalFields.ImageFile.CreatedTimeUtc` | `target.process.file.create_time` |   
`Process` | `properties.AdditionalFields.ImageFile.DetectionStatus` | `security_result.detection_fields[ImageFile_DetectionStatus]` |   
`Process` | `properties.AdditionalFields.ImageFile.Directory, properties.AdditionalFields.ImageFile.Name` | `target.process.file.full_path` | If the `properties.AdditionalFields.ImageFile.Directory` log field value matches the regular expression pattern the `properties.AdditionalFields.ImageFile.Name` log field value, then the `properties.AdditionalFields.ImageFile.Directory` log field is mapped to the `target.process.file.full_path` UDM field.  
  
Otherwise, the `target.process.file.full_path` UDM field is set to a value generated from the template `%{properties.AdditionalFields.ImageFile.Directory}\%{properties.AdditionalFields.ImageFile.Name}`, where `%{properties.AdditionalFields.ImageFile.Directory}` and `%{properties.AdditionalFields.ImageFile.Name}` are replaced with the values of the `properties.AdditionalFields.ImageFile.Directory` and `properties.AdditionalFields.ImageFile.Name` log fields.  
`Process` | `properties.AdditionalFields.ImageFile.EnrichmentType` | `additional.fields[ImageFile_EnrichmentType]` |   
`Process` | `properties.AdditionalFields.ImageFile.FileHashes.$id` | `additional.fields[ImageFile_FileHashes_$id]` | Iterate through log field `properties.AdditionalFields.ImageFile.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ImageFile_FileHashes_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ImageFile.FileHashes.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.FileHashes.Algorithm` | `additional.fields[ImageFile_FileHashes_Algorithm]` | Iterate through log field `properties.AdditionalFields.ImageFile.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ImageFile_FileHashes_Algorithm_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ImageFile.FileHashes.Algorithm` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.FileHashes.Type` | `additional.fields[ImageFile_FileHashes_Type]` | Iterate through log field `properties.AdditionalFields.ImageFile.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ImageFile_FileHashes_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ImageFile.FileHashes.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.FileHashes.Value` | `target.process.file.sha1, target.process.file.sha256, target.process.file.md5` | Iterate through log field `properties.AdditionalFields.ImageFile.FileHashes`:  
  
If the `properties.AdditionalFields.ImageFile.FileHashes.Algorithm` log field value is equal to `SHA1` and the `properties.SHA1` log field value is empty and the `target.process.file.sha1` UDM field is empty and the `properties.AdditionalFields.ImageFile.FileHashes.Value` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.AdditionalFields.ImageFile.FileHashes.Value` log field is mapped to the `target.process.file.sha1` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.ImageFile.FileHashes.Algorithm` log field value is equal to `SHA256` and the `properties.SHA256` log field value is empty and the `target.process.file.sha256` UDM field is empty and the `properties.AdditionalFields.ImageFile.FileHashes.Value` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.AdditionalFields.ImageFile.FileHashes.Value` log field is mapped to the `target.process.file.sha256` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.ImageFile.FileHashes.Algorithm` log field value is equal to `MD5` and the `properties.MD5` log field value is empty and the `target.process.file.md5` UDM field is empty and the `properties.AdditionalFields.ImageFile.FileHashes.Value` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.AdditionalFields.ImageFile.FileHashes.Value` log field is mapped to the `target.process.file.md5` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.ImageFile.FileHashes.Value` log field is _not_ mapped to the `target.process.file.sha1`, `target.process.file.sha256`, or `target.process.file.md5` UDM fields, then:  
  
If the `properties.AdditionalFields.ImageFile.FileHashes.Algorithm` log field value is equal to `SHA1`, then the `target.security_result.detection_fields.key` UDM field is set to `ImageFile_FileHashes_SHA1_Value` and the `properties.AdditionalFields.ImageFile.FileHashes.Value` log field is mapped to the `target.security_result.detection_fields.value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.ImageFile.FileHashes.Algorithm` log field value is equal to `SHA256`, then the `target.security_result.detection_fields.key` UDM field is set to `ImageFile_FileHashes_SHA256_Value` and the `properties.AdditionalFields.ImageFile.FileHashes.Value` log field is mapped to the `target.security_result.detection_fields.value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.ImageFile.FileHashes.Algorithm` log field value is equal to `MD5`, then the `target.security_result.detection_fields.key` UDM field is set to `ImageFile_FileHashes_MD5_Value` and the `properties.AdditionalFields.ImageFile.FileHashes.Value` log field is mapped to the `target.security_result.detection_fields.value` UDM field.  
  
Otherwise, the `target.security_result.detection_fields.key` UDM field is set to `ImageFile_FileHashes_Value` and the `properties.AdditionalFields.ImageFile.FileHashes.Value` log field is mapped to the `target.security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.FirstSeen` | `target.process.file.first_seen_time` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.$id` | `additional.fields[ImageFile_Host_$id]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.Asset` | `principal.asset.attribute.labels[ImageFile_Host_Asset]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.DetailedRoles` | `principal.asset.attribute.labels[ImageFile_Host_DetailedRoles]` | Iterate through log field `properties.AdditionalFields.ImageFile.Host.DetailedRoles`:  
  
The `principal.asset.attribute.labels.key` UDM field is set to `ImageFile_Host_DetailedRoles` and the `properties.AdditionalFields.ImageFile.Host.DetailedRoles` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Host.DetectionStatus` | `security_result.detection_fields[ImageFile_Host_DetectionStatus]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.EnrichmentType` | `additional.fields[ImageFile_Host_EnrichmentType]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.IpInterfaces.$id` | `additional.fields[ImageFile_Host_IpInterfaces_$id]` | Iterate through log field `properties.AdditionalFields.ImageFile.Host.IpInterfaces`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ImageFile_Host_IpInterfaces_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ImageFile.Host.IpInterfaces.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Host.IpInterfaces.Address` | `principal.ip` | Iterate through log field `properties.AdditionalFields.ImageFile.Host.IpInterfaces`:  
  
The `valid_imagefile_host_ipinterface_address` field is extracted from `properties.AdditionalFields.ImageFile.Host.IpInterfaces.Address` log field using the Grok pattern. The `valid_imagefile_host_ipinterface_address` log field is mapped to the `principal.ip` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Host.IpInterfaces.Type` | `additional.fields[ImageFile_Host_IpInterfaces_Type]` | Iterate through log field `properties.AdditionalFields.ImageFile.Host.IpInterfaces`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ImageFile_Host_IpInterfaces_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ImageFile.Host.IpInterfaces.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Host.IsDomainJoined` | `principal.asset.attribute.labels[ImageFile_Host_IsDomainJoined]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.IsIoc` | `security_result.detection_fields[ImageFile_Host_IsIoc]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.LastRemediationState` | `security_result.detection_fields[ImageFile_Host_LastRemediationState]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.LastVerdict` | `security_result.detection_fields[ImageFile_Host_LastVerdict]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.LeadingHost` | `principal.asset.attribute.labels[ImageFile_Host_LeadingHost]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.MachineIdType` | `principal.asset.attribute.labels[ImageFile_Host_MachineIdType]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.MergeByKey` | `additional.fields[ImageFile_Host_MergeByKey]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.MergeByKeyHex` | `additional.fields[ImageFile_Host_MergeByKeyHex]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.Metadata.MachineEnrichmentInfo` | `additional.fields[ImageFile_Host_Metadata_MachineEnrichmentInfo]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.NetBiosName` | `principal.asset.attribute.labels[ImageFile_Host_NetBiosName]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.OSFamily` | `principal.platform` | If the `properties.AdditionalFields.ImageFile.Host.OSFamily` log field value is equal to `Windows`, then the `principal.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.AdditionalFields.ImageFile.Host.OSFamily` log field value is equal to `Mac`, then the `principal.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.AdditionalFields.ImageFile.Host.OSFamily` log field value is equal to `Linux`, then the `principal.platform` UDM field is set to `LINUX`.  
`Process` | `properties.AdditionalFields.ImageFile.Host.OSVersion` | `principal.platform_version` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[ImageFile_Host_RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[ImageFile_Host_RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.ImageFile.Host.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ImageFile_Host_RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ImageFile.Host.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Host.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[ImageFile_Host_RbacScopes_ScopesPerType_Workloads_Mode]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[ImageFile_Host_RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.ImageFile.Host.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ImageFile_Host_RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ImageFile.Host.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Host.RemediationProviders.RemediationDate` | `security_result.detection_fields[ImageFile_Host_RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.ImageFile.Host.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `ImageFile_Host_RemediationProviders_RemediationDate` and the `properties.AdditionalFields.ImageFile.Host.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Host.RemediationProviders.RemediationState` | `security_result.detection_fields[ImageFile_Host_RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.ImageFile.Host.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `ImageFile_Host_RemediationProviders_RemediationState` and the `properties.AdditionalFields.ImageFile.Host.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Host.RemediationProviders.Type` | `security_result.detection_fields[ImageFile_Host_RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.ImageFile.Host.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `ImageFile_Host_RemediationProviders_Type` and the `properties.AdditionalFields.ImageFile.Host.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Host.Role` | `additional.fields[ImageFile_Host_Role]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.SuspicionLevel` | `security_result.detection_fields[ImageFile_Host_SuspicionLevel]` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ImageFile_Host_ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ImageFile.Host.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ImageFile_Host_ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ImageFile.Host.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Host.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ImageFile_Host_ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ImageFile.Host.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ImageFile_Host_ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ImageFile.Host.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Host.Type` | `additional.fields[ImageFile_Host_Type]` |   
`Process` | `properties.AdditionalFields.ImageFile.HostUrl.$id` | `additional.fields[ImageFile_HostUrl_$id]` |   
`Process` | `properties.AdditionalFields.ImageFile.HostUrl.Type` | `additional.fields[ImageFile_HostUrl_Type]` |   
`Process` | `properties.AdditionalFields.ImageFile.HostUrl.Url` | `src.url` |   
`Process` | `properties.AdditionalFields.ImageFile.HostUrl.Url` | `additional.fields[ImageFile_HostUrl_Url]` |   
`Process` | `properties.AdditionalFields.ImageFile.IsDownloaded` | `additional.fields[ImageFile_IsDownloaded]` |   
`Process` | `properties.AdditionalFields.ImageFile.IsIoc` | `security_result.detection_fields[ImageFile_IsIoc]` |   
`Process` | `properties.AdditionalFields.ImageFile.IsPe` | `additional.fields[ImageFile_IsPe]` |   
`Process` | `properties.AdditionalFields.ImageFile.KnownPrevalence` | `additional.fields[process_ImageFile_known_prevalence]` |   
`Process` | `properties.AdditionalFields.ImageFile.LastAccessTimeUtc` | `target.process.file.last_access_time` |   
`Process` | `properties.AdditionalFields.ImageFile.LastRemediationState` | `security_result.detection_fields[ImageFile_LastRemediationState]` |   
`Process` | `properties.AdditionalFields.ImageFile.LastVerdict` | `security_result.detection_fields[ImageFile_LastVerdict]` |   
`Process` | `properties.AdditionalFields.ImageFile.LastWriteTimeUtc` | `target.process.file.last_modification_time` |   
`Process` | `properties.AdditionalFields.ImageFile.LsHash` | `additional.fields[ImageFile_LsHash]` |   
`Process` | `properties.AdditionalFields.ImageFile.MergeByKey` | `additional.fields[ImageFile_MergeByKey]` |   
`Process` | `properties.AdditionalFields.ImageFile.MergeByKeyHex` | `additional.fields[ImageFile_MergeByKeyHex]` |   
`Process` | `properties.AdditionalFields.ImageFile.Name` | `target.process.file.names` |   
`Process` | `properties.AdditionalFields.ImageFile.Publisher` | `target.process.file.exif_info.company` |   
`Process` | `properties.AdditionalFields.ImageFile.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[ImageFile_RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`Process` | `properties.AdditionalFields.ImageFile.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[ImageFile_RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.ImageFile.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ImageFile_RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ImageFile.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[ImageFile_RbacScopes_ScopesPerType_Workloads_Mode]` |   
`Process` | `properties.AdditionalFields.ImageFile.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[ImageFile_RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.ImageFile.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ImageFile_RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ImageFile.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.ReferenceId` | `additional.fields[ImageFile_ReferenceId]` |   
`Process` | `properties.AdditionalFields.ImageFile.ReferrerUrl.$id` | `additional.fields[ImageFile_ReferrerUrl_$id]` |   
`Process` | `properties.AdditionalFields.ImageFile.ReferrerUrl.Type` | `additional.fields[ImageFile_ReferrerUrl_Type]` |   
`Process` | `properties.AdditionalFields.ImageFile.ReferrerUrl.Url` | `network.http.referral_url` |   
`Process` | `properties.AdditionalFields.ImageFile.ReferrerUrl.Url` | `additional.fields[ImageFile_ReferrerUrl_Url]` |   
`Process` | `properties.AdditionalFields.ImageFile.RemediationProviders.RemediationDate` | `security_result.detection_fields[ImageFile_RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.ImageFile.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `ImageFile_RemediationProviders_RemediationDate` and the `properties.AdditionalFields.ImageFile.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.RemediationProviders.RemediationState` | `security_result.detection_fields[ImageFile_RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.ImageFile.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `ImageFile_RemediationProviders_RemediationState` and the `properties.AdditionalFields.ImageFile.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.RemediationProviders.Type` | `security_result.detection_fields[ImageFile_RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.ImageFile.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `ImageFile_RemediationProviders_Type` and the `properties.AdditionalFields.ImageFile.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Role` | `additional.fields[ImageFile_Role]` |   
`Process` | `properties.AdditionalFields.ImageFile.SizeInBytes` | `target.process.file.size` | If the `properties.FileSize` log field value is empty, then the `properties.AdditionalFields.ImageFile.SizeInBytes` log field is mapped to the `target.process.file.size` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `SizeInBytes` and the `properties.AdditionalFields.ImageFile.SizeInBytes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.SuspicionLevel` | `security_result.detection_fields[ImageFile_SuspicionLevel]` |   
`Process` | `properties.AdditionalFields.ImageFile.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ImageFile_ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ImageFile.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ImageFile_ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ImageFile.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ImageFile_ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ImageFile.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ImageFile_ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ImageFile.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.ThreatFamilyName` | `security_result.detection_fields[ImageFile_ThreatFamilyName]` |   
`Process` | `properties.AdditionalFields.ImageFile.Type` | `additional.fields[ImageFile_Type]` |   
`Process` | `properties.AdditionalFields.ImageFile.WindowsSecurityZone` | `additional.fields[ImageFile_WindowsSecurityZone]` |   
`Process` | `properties.AdditionalFields.IsIoc` | `security_result.detection_fields[IsIoc]` |   
`Process` | `properties.AdditionalFields.LastRemediationState` | `security_result.detection_fields[LastRemediationState]` |   
`Process` | `properties.AdditionalFields.LastVerdict` | `security_result.threat_verdict` | If the `properties.AdditionalFields.LastVerdict` log field value is equal to `Suspicious`, then the `security_result.threat_verdict` UDM field is set to `SUSPICIOUS`.  
  
Otherwise, if the `properties.AdditionalFields.LastVerdict` log field value is equal to `Malicious`, then the `security_result.threat_verdict` UDM field is set to `MALICIOUS`.  
`Process` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`Process` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`Process` | `properties.AdditionalFields.ParentProcess.$id` | `additional.fields[ParentProcess_$id]` |   
`Process` | `properties.AdditionalFields.ParentProcess.Account.$id` | `additional.fields[ParentProcess_Account_$id]` |   
`Process` | `properties.AdditionalFields.ParentProcess.Account.$ref` | `additional.fields[ParentProcess_Account_$ref]` |   
`Process` | `properties.AdditionalFields.ParentProcess.Account.Asset` | `principal.asset.attribute.labels[ParentProcess_Account_Asset]` |   
`Process` | `properties.AdditionalFields.ParentProcess.Account.Host.$ref` | `additional.fields[ParentProcess_Account_Host_$ref]` |   
`Process` | `properties.AdditionalFields.ParentProcess.Account.IsDomainJoined` | `principal.asset.attribute.labels[ParentProcess_Account_IsDomainJoined]` |   
`Process` | `properties.AdditionalFields.ParentProcess.Account.Name` | `principal.user.userid` | If the `properties.AdditionalFields.ParentProcess.Account.Name` log field value is _not_ empty, then if the `properties.AccountName` log field value is empty, then the `properties.AdditionalFields.ParentProcess.Account.Name` log field is mapped to the `principal.user.userid` UDM field. Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `ParentProcess_Account_Name` and the `properties.AdditionalFields.ParentProcess.Account.Name` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.Account.NTDomain` | `principal.administrative_domain` | If the `properties.AdditionalFields.ParentProcess.Account.NTDomain` log field value is _not_ empty, then if the `properties.AccountDomain` log field value is empty, then the `properties.AdditionalFields.ParentProcess.Account.NTDomain` log field is mapped to the `principal.administrative_domain` UDM field. Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `ParentProcess_Account_Domain` and the `properties.AdditionalFields.ParentProcess.Account.NTDomain` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.Account.Role` | `principal.user.attribute.labels[ParentProcess_Account_Role]` |   
`Process` | `properties.AdditionalFields.ParentProcess.Account.Sid` | `principal.user.windows_sid` | If the `properties.AdditionalFields.ParentProcess.Account.Sid` log field value is _not_ empty, then if the `properties.AccountSid` log field value is empty, then the `properties.AdditionalFields.ParentProcess.Account.Sid` log field is mapped to the `principal.user.windows_sid` UDM field. Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `ParentProcess_Account_Sid` and the `properties.AdditionalFields.ParentProcess.Account.Sid` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.Account.Type` | `principal.user.attribute.labels[ParentProcess_Account_Type]` |   
`Process` | `properties.AdditionalFields.ParentProcess.CommandLine` | `principal.process.command_line` |   
`Process` | `properties.AdditionalFields.ParentProcess.CreatedTimeUtc` | `principal.security_result.detection_fields[ParentProcess_CreatedTimeUtc]` |   
`Process` | `properties.AdditionalFields.ParentProcess.CreationTimeUtc` | `additional.fields[ParentProcess_CreationTimeUtc]` |   
`Process` | `properties.AdditionalFields.ParentProcess.DetectionStatus` | `security_result.detection_fields[ParentProcess_DetectionStatus]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ElevationToken` | `principal.process.parent_process.token_elevation_type` | If the `properties.AdditionalFields.ParentProcess.ElevationToken` log field value is equal to `Full`, then the `principal.process.parent_process.token_elevation_type` UDM field is set to `TYPE_1`.  
  
Otherwise, if the `properties.AdditionalFields.ParentProcess.ElevationToken` log field value is equal to `Limited`, then the `principal.process.parent_process.token_elevation_type` UDM field is set to `TYPE_3`.  
  
Otherwise, the `principal.process.parent_process.token_elevation_type` UDM field is set to `UNKNOWN`.  
`Process` | `properties.AdditionalFields.ParentProcess.Host.$ref` | `additional.fields[ParentProcess_Host_$ref]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.$id` | `additional.fields[ParentProcess_ImageFile_$id]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.CreatedTimeUtc` | `principal.process.file.create_time` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.Directory,properties.AdditionalFields.ParentProcess.ImageFile.Name` | `principal.process.file.full_path` | If the `properties.AdditionalFields.ParentProcess.ImageFile.Directory` log field value matches the regular expression pattern the `properties.AdditionalFields.ParentProcess.ImageFile.Name` log field value, then the `properties.AdditionalFields.ParentProcess.ImageFile.Directory` log field is mapped to the `principal.process.file.full_path` UDM field.  
  
Otherwise, the `principal.process.file.full_path` UDM field is set to a value generated from the template `%{properties.AdditionalFields.ParentProcess.ImageFile.Directory}\%{properties.AdditionalFields.ParentProcess.ImageFile.Name}`, where `%{properties.AdditionalFields.ParentProcess.ImageFile.Directory}` and `%{properties.AdditionalFields.ParentProcess.ImageFile.Name}` are replaced with the values of the `properties.AdditionalFields.ParentProcess.ImageFile.Directory` and `properties.AdditionalFields.ParentProcess.ImageFile.Name` log fields.  
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.$id` | `additional.fields[ParentProcess_ImageFile_FileHashes_$id]` | Iterate through log field `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ParentProcess_ImageFile_FileHashes_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Algorithm` | `additional.fields[ParentProcess_ImageFile_FileHashes_Algorithm]` | Iterate through log field `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ParentProcess_ImageFile_FileHashes_Algorithm_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Algorithm` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Type` | `additional.fields[ParentProcess_ImageFile_FileHashes_Type]` | Iterate through log field `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ParentProcess_ImageFile_FileHashes_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Value` | `principal.process.file.sha1, principal.process.file.sha256, principal.process.file.md5` | Iterate through log field `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes`:  
  
If the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Algorithm` log field value is equal to `SHA1` and the `properties.SHA1` log field value is empty and the `principal.process.file.sha1` UDM field is empty and the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Value` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Value` log field is mapped to the `principal.process.file.sha1` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Algorithm` log field value is equal to `SHA256` and the `properties.SHA256` log field value is empty and the `principal.process.file.sha256` UDM field is empty and the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Value` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Value` log field is mapped to the `principal.process.file.sha256` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Algorithm` log field value is equal to `MD5` and the `properties.MD5` log field value is empty and the `principal.process.file.md5` UDM field is empty and the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Value` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Value` log field is mapped to the `principal.process.file.md5` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Value` log field is _not_ mapped to the `principal.process.file.sha1`, `principal.process.file.sha256`, or `principal.process.file.md5` UDM fields, then:  
  
If the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Algorithm` log field value is equal to `SHA1`, then the `principal.security_result.detection_fields.key` UDM field is set to `ParentProcess_ImageFile_FileHashes_SHA1_Value` and the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Value` log field is mapped to the `principal.security_result.detection_fields.value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Algorithm` log field value is equal to `SHA256`, then the `principal.security_result.detection_fields.key` UDM field is set to `ParentProcess_ImageFile_FileHashes_SHA256_Value` and the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Value` log field is mapped to the `principal.security_result.detection_fields.value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Algorithm` log field value is equal to `MD5`, then the `principal.security_result.detection_fields.key` UDM field is set to `ParentProcess_ImageFile_FileHashes_MD5_Value` and the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Value` log field is mapped to the `principal.security_result.detection_fields.value` UDM field.  
  
Otherwise, the `principal.security_result.detection_fields.key` UDM field is set to `ParentProcess_ImageFile_FileHashes_Value` and the `properties.AdditionalFields.ParentProcess.ImageFile.FileHashes.Value` log field is mapped to the `principal.security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.FirstSeen` | `principal.process.file.first_seen_time` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.Host.$ref` | `additional.fields[ParentProcess_ImageFile_Host_$ref]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.IsPe` | `additional.fields[ParentProcess_ImageFile_IsPe]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.KnownPrevalence` | `additional.fields[ParentProcess_ImageFile_known_prevalence]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.LastAccessTimeUtc` | `principal.process.file.last_access_time` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.LastWriteTimeUtc` | `principal.process.file.last_modification_time` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.LsHash` | `additional.fields[ParentProcess_ImageFile_LsHash]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.Name` | `principal.process.file.names` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.Publisher` | `principal.process.file.exif_info.company` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.SizeInBytes` | `principal.process.file.size` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.Type` | `additional.fields[ParentProcess_ImageFile_Type]` |   
`Process` | `properties.AdditionalFields.ParentProcess.IsIoc` | `security_result.detection_fields[ParentProcess_IsIoc]` |   
`Process` | `properties.AdditionalFields.ParentProcess.LastRemediationState` | `security_result.detection_fields[ParentProcess_LastRemediationState]` |   
`Process` | `properties.AdditionalFields.ParentProcess.LastVerdict` | `security_result.detection_fields[ParentProcess_LastVerdict]` |   
`Process` | `properties.AdditionalFields.ParentProcess.MergeByKey` | `additional.fields[ParentProcess_MergeByKey]` |   
`Process` | `properties.AdditionalFields.ParentProcess.MergeByKeyHex` | `additional.fields[ParentProcess_MergeByKeyHex]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ParentProcess.$id` | `additional.fields[ParentProcess_ParentProcess_$id]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ParentProcess.CreatedTimeUtc` | `additional.fields[ParentProcess_ParentProcess_CreatedTimeUtc]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ParentProcess.CreationTimeUtc` | `additional.fields[ParentProcess_ParentProcess_CreationTimeUtc]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ParentProcess.Host.$ref` | `additional.fields[ParentProcess_ParentProcess_Host_$ref]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ParentProcess.ImageFile.$id` | `additional.fields[ParentProcess_ParentProcess_ImageFile_$id]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ParentProcess.ImageFile.Host.$ref` | `additional.fields[ParentProcess_ParentProcess_ImageFile_Host_$ref]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ParentProcess.ImageFile.Name` | `principal.process.parent_process.file.names` |   
`Process` | `properties.AdditionalFields.ParentProcess.ParentProcess.ImageFile.Type` | `additional.fields[ParentProcess_ParentProcess_ImageFile_Type]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ParentProcess.ProcessId` | `principal.process.parent_process.pid` |   
`Process` | `properties.AdditionalFields.ParentProcess.ParentProcess.Type` | `additional.fields[ParentProcess_ParentProcess_Type]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ProcessId` | `principal.process.pid` |   
`Process` | `properties.AdditionalFields.ParentProcess.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[ParentProcess_RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`Process` | `properties.AdditionalFields.ParentProcess.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[ParentProcess_RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.ParentProcess.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ParentProcess_RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ParentProcess.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[ParentProcess_RbacScopes_ScopesPerType_Workloads_Mode]` |   
`Process` | `properties.AdditionalFields.ParentProcess.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[ParentProcess_RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.ParentProcess.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ParentProcess_RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ParentProcess.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.ReferenceId` | `additional.fields[ParentProcess_ReferenceId]` |   
`Process` | `properties.AdditionalFields.ParentProcess.RemediationProviders.RemediationDate` | `security_result.detection_fields[ParentProcess_RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.ParentProcess.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `ParentProcess_RemediationProviders_RemediationDate` and the `properties.AdditionalFields.ParentProcess.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.RemediationProviders.RemediationState` | `security_result.detection_fields[ParentProcess_RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.ParentProcess.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `ParentProcess_RemediationProviders_RemediationState` and the `properties.AdditionalFields.ParentProcess.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.RemediationProviders.Type` | `security_result.detection_fields[ParentProcess_RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.ParentProcess.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `ParentProcess_RemediationProviders_Type` and the `properties.AdditionalFields.ParentProcess.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.Role` | `principal.security_result.detection_fields[ParentProcess_Role]` |   
`Process` | `properties.AdditionalFields.ParentProcess.SuspicionLevel` | `security_result.detection_fields[ParentProcess_SuspicionLevel]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ParentProcess_ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ParentProcess.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ParentProcess_ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ParentProcess.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ParentProcess_ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ParentProcess.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ParentProcess_ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ParentProcess.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.Type` | `additional.fields[ParentProcess_Type]` |   
`Process` | `properties.AdditionalFields.ProcessId` | `target.process.pid` |   
`Process` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`Process` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Mode]` |   
`Process` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.ReferenceId` | `additional.fields[ReferenceId]` |   
`Process` | `properties.AdditionalFields.RemediationProviders.RemediationDate` | `security_result.detection_fields[RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationDate` and the `properties.AdditionalFields.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.RemediationProviders.RemediationState` | `security_result.detection_fields[RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationState` and the `properties.AdditionalFields.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.RemediationProviders.Type` | `security_result.detection_fields[RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_Type` and the `properties.AdditionalFields.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`Process` | `properties.AdditionalFields.SuspicionLevel` | `security_result.detection_fields[SuspicionLevel]` |   
`Process` | `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.Count of ThreatAnalysisSummary` | `security_result.detection_fields[Count_of_ThreatAnalysisSummary]` |   
`Process` | `properties.AdditionalFields.ThreatFamilyName` | `security_result.detection_fields[ThreatFamilyName]` |   
`Process` | `properties.AdditionalFields.Account.DisplayName` | `target.user.user_display_name` |   
`Process` | `properties.AdditionalFields.Account.DnsDomain` | `target.user.attribute.labels[Account_DnsDomain]` |   
`Process` | `properties.AdditionalFields.FriendlyName` | `security_result.description` |   
`Process` | `properties.AdditionalFields.ImageFile.Host.Metadata.IncriminationTags` | `about.security_result.detection_fields[ImageFile_Host_Metadata_IncriminationTags]` |   
`Process` | `properties.AdditionalFields.ParentProcess.FriendlyName` | `principal.security_result.detection_fields[ParentProcess_FriendlyName]` |   
`Process` | `properties.AdditionalFields.IpInterfaces.Type` | `additional.fields[IpInterfaces_Type]` | Iterate through log field `properties.AdditionalFields.IpInterfaces`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `IpInterfaces_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.IpInterfaces.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.IpInterfaces.$id` | `additional.fields[IpInterfaces_$id]` | Iterate through log field `properties.AdditionalFields.IpInterfaces`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `IpInterfaces_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.IpInterfaces.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Process` | `properties.AdditionalFields.IpInterfaces.Address` | `principal.ip` | Iterate through log field `properties.AdditionalFields.IpInterfaces`:  
  
The `valid_ipinterface_address` field is extracted from `properties.AdditionalFields.IpInterfaces.Address` log field using the Grok pattern. The `valid_ipinterface_address` log field is mapped to the `principal.ip` UDM field.  
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.HostUrl.$id` | `additional.fields[ParentProcess_ImageFile_HostUrl_$id]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.HostUrl.Type` | `additional.fields[ParentProcess_ImageFile_HostUrl_Type]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.HostUrl.Url` | `about.url` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.HostUrl.Url` | `additional.fields[ParentProcess_ImageFile_HostUrl_Url]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.IsDownloaded` | `additional.fields[ParentProcess_ImageFile_IsDownloaded]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.ReferrerUrl.$id` | `additional.fields[ParentProcess_ImageFile_ReferrerUrl_$id]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.ReferrerUrl.Type` | `additional.fields[ParentProcess_ImageFile_ReferrerUrl_Type]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.ReferrerUrl.Url` | `about.network.http.referral_url` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.ReferrerUrl.Url` | `additional.fields[ParentProcess_ImageFile_ReferrerUrl_Url]` |   
`Process` | `properties.AdditionalFields.ParentProcess.ImageFile.WindowsSecurityZone` | `additional.fields[ParentProcess_ImageFile_WindowsSecurityZone]` |   
`Process` | `properties.AdditionalFields.Account.InventoryIdentityId` | `target.user.attribute.labels[Account_InventoryIdentityId]` |   
`Process` | `properties.AdditionalFields.ThreatAnalysisSummary.AnalyzersResult` | `security_result.detection_fields[ThreatAnalysisSummary_AnalyzersResult]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary.AnalyzersResult`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_AnalyzersResult` and the `properties.AdditionalFields.ThreatAnalysisSummary.AnalyzersResult` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.Account.ThreatAnalysisSummary.AnalyzersResult` | `security_result.detection_fields[Account_ThreatAnalysisSummary_AnalyzersResult]` | Iterate through log field `properties.AdditionalFields.Account.ThreatAnalysisSummary`:  
  
Iterate through log field `properties.AdditionalFields.Account.ThreatAnalysisSummary.AnalyzersResult`:  
  
The `security_result.detection_fields.key` UDM field is set to `Account_ThreatAnalysisSummary_AnalyzersResult` and the `properties.AdditionalFields.Account.ThreatAnalysisSummary.AnalyzersResult` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.ImageFile.Host.ThreatAnalysisSummary.AnalyzersResult` | `security_result.detection_fields[ImageFile_Host_ThreatAnalysisSummary_AnalyzersResult]` | Iterate through log field `properties.AdditionalFields.ImageFile.Host.ThreatAnalysisSummary`:  
  
Iterate through log field `properties.AdditionalFields.ImageFile.Host.ThreatAnalysisSummary.AnalyzersResult`:  
  
The `security_result.detection_fields.key` UDM field is set to `ImageFile_Host_ThreatAnalysisSummary_AnalyzersResult` and the `properties.AdditionalFields.ImageFile.Host.ThreatAnalysisSummary.AnalyzersResult` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Process` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`CloudResource` | `properties.AdditionalFields.Asset` | `principal.asset.attribute.labels[Asset]` |   
`CloudResource` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`CloudResource` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`CloudResource` | `properties.AdditionalFields.ResourceId` | `target.resource.product_object_id` |   
`CloudResource` | `properties.AdditionalFields.ResourceName` | `target.resource.name` |   
`CloudResource` | `properties.AdditionalFields.ResourceType` | `target.resource.resource_subtype` |   
`CloudResource` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`CloudResource` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`GenericEntity` | `properties.AdditionalFields.Algorithm` | `security_result.detection_fields[Algorithm]` |   
`GenericEntity` | `properties.AdditionalFields.Asset` | `principal.asset.attribute.labels[Asset]` |   
`GenericEntity` | `properties.AdditionalFields.FriendlyName` | `security_result.description` |   
`GenericEntity` | `properties.AdditionalFields.IsValid` | `additional.fields[IsValid]` |   
`GenericEntity` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`GenericEntity` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`GenericEntity` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`GenericEntity` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`GenericEntity` | `properties.AdditionalFields.Value` | `target.file.sha1, target.file.sha256, target.file.md5` | If the `properties.AdditionalFields.Algorithm` log field value is equal to `SHA1` and the `properties.sha1` log field value is empty, then the `properties.AdditionalFields.Value` log field is mapped to the `target.file.sha1` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.Algorithm` log field value is equal to `SHA256` and the `properties.sha256` log field value is empty, then the `properties.AdditionalFields.Value` log field is mapped to the `target.file.sha256` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.Algorithm` log field value is equal to `MD5` and the `properties.md5` log field value is empty, then the `properties.AdditionalFields.Value` log field is mapped to the `target.file.md5` UDM field.  
  
Otherwise, the `security_result.detection_fields.key` UDM field is set to `Value` and the `properties.AdditionalFields.Value` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Malware` | `properties.AdditionalFields.Asset` | `principal.asset.attribute.labels[Asset]` |   
`Malware` | `properties.AdditionalFields.Category` | `security_result.detection_fields[Category]` |   
`Malware` | `properties.AdditionalFields.Files.$id` | `additional.fields[Files_$id]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Asset` | `target.asset.attribute.labels[Files_Asset]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `target.asset.attribute.labels.key` UDM field is set to `Files_Asset` and the `properties.AdditionalFields.Files.Asset` log field is mapped to the `target.asset.attribute.labels.value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.FileHashes.$id` | `additional.fields[Files_FileHashes_$id]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_$id_%{index1}`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.FileHashes.$ref` | `additional.fields[Files_FileHashes_$ref]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_$ref_%{index1}`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.$ref` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.FileHashes.Algorithm` | `additional.fields[Files_FileHashes_Algorithm]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_Algorithm_%{index1}`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.FileHashes.Asset` | `target.asset.attribute.labels[Files_FileHashes_Asset]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.FileHashes`:  
  
The `target.asset.attribute.labels.key` UDM field is set to `Files_FileHashes_Asset` and the `properties.AdditionalFields.Files.FileHashes.Asset` log field is mapped to the `target.asset.attribute.labels.value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.FileHashes.FriendlyName` | `additional.fields[Files_FileHashes_FriendlyName]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_FriendlyName_%{index1}`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.FriendlyName` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.FileHashes.Role` | `additional.fields[Files_FileHashes_Role]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_Role_%{index1}`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.Role` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.FileHashes.Type` | `additional.fields[Files_FileHashes_Type]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_Type_%{index1}`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.FileHashes.Value` | `target.file.sha1, target.file.sha256, target.file.md5` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.FileHashes`:  
  
If the `index` log field value is equal to `0` and the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field value is equal to `SHA1` and the `target.file.sha1` UDM field is empty and the `properties.AdditionalFields.Files.FileHashes.Value` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `target.file.sha1` UDM field.  
  
Otherwise, if the `index` log field value is equal to `0` and the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field value is equal to `SHA256` and the `target.file.sha256` UDM field is empty and the `properties.AdditionalFields.Files.FileHashes.Value` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `target.file.sha256` UDM field.  
  
Otherwise, if the `index` log field value is equal to `0` and the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field value is equal to `MD5` and the `target.file.md5` UDM field is empty and the `properties.AdditionalFields.Files.FileHashes.Value` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `target.file.md5` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.Files.FileHashes.Value` log field is _not_ mapped to the `target.file.sha1`, `target.file.sha256`, or `target.file.md5` UDM fields, then:  
  
If the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field value is equal to `SHA1`, then the `security_result.detection_fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_%{index1}_SHA1_Value`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `security_result.detection_fields.value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field value is equal to `SHA256`, then the `security_result.detection_fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_%{index1}_SHA256_Value`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `security_result.detection_fields.value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field value is equal to `MD5`, then the `security_result.detection_fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_%{index1}_MD5_Value`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Directory` | `target.file.full_path` | Iterate through log field `properties.AdditionalFields.Files`:  
if the `index` value is equal to `0`, then the `target.file.full_path` UDM field is set to a value generated from the template `%{properties.AdditionalFields.Files.Directory}\\%{properties.AdditionalFields.Files.Name}`, where `%{properties.AdditionalFields.Files.Directory}` and `%{properties.AdditionalFields.Files.Name}` are replaced with the values of the `properties.AdditionalFields.Files.Directory` and `properties.AdditionalFields.Files.Name` log fields.  
  
Otherwise, the `security_result.detection_fields.key` UDM field is set to a value generated from the template `Files_%{index}_Directory_File_Name`, where `%{index}` is replaced with the value of the `index` log field and the `security_result.detection_fields.value` UDM field is set to a value generated from the template `%{properties.AdditionalFields.Files.Directory}\\%{properties.AdditionalFields.Files.Name}`, where `%{properties.AdditionalFields.Files.Directory}` and `%{properties.AdditionalFields.Files.Name}` are replaced with the values of the `properties.AdditionalFields.Files.Directory` and `properties.AdditionalFields.Files.Name` log fields.  
`Malware` | `properties.AdditionalFields.Files.Host.$id` | `additional.fields[Files_Host_$id]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_Host_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.Host.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Host.$ref` | `additional.fields[Files_Host_$ref]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_Host_$ref_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.Host.$ref` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Host.Asset` | `target.asset.attribute.labels[Files_Host_Asset]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `target.asset.attribute.labels.key` UDM field is set to `Files_Host_Asset` and the `properties.AdditionalFields.Files.Host.Asset` log field is mapped to the `target.asset.attribute.labels.value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Host.IsDomainJoined` | `target.asset.attribute.labels[Files_Host_IsDomainJoined]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `target.asset.attribute.labels.key` UDM field is set to `Files_Host_IsDomainJoined` and the `properties.AdditionalFields.Files.Host.IsDomainJoined` log field is mapped to the `target.asset.attribute.labels.value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Host.MachineId` | `target.asset_id` | Iterate through log field `properties.AdditionalFields.Files`:  
if the `index` value is equal to `0`, then the `target.asset_id` UDM field is set to a value generated from the template `DeviceID:%{properties.AdditionalFields.Files.Host.MachineId}`, where `%{properties.AdditionalFields.Files.Host.MachineId}` is replaced with the value of the `properties.AdditionalFields.Files.Host.MachineId` log field.  
  
Otherwise, the `target.asset.attribute.labels.key` UDM field is set to a value generated from the template `Files_%{index}_Host_MachineId`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.Host.MachineId` log field is mapped to the `target.asset.attribute.labels.value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Host.AzureID` | `target.asset.attribute.labels[Files_Host_AzureID]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `target.asset.attribute.labels.key` UDM field is set to `Files_Host_AzureID` and the `properties.AdditionalFields.Files.Host.AzureID` log field is mapped to the `target.asset.attribute.labels.value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Host.MachineIdType` | `target.asset.attribute.labels[Files_Host_MachineIdType]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `target.asset.attribute.labels.key` UDM field is set to `Files_Host_MachineIdType` and the `properties.AdditionalFields.Files.Host.MachineIdType` log field is mapped to the `target.asset.attribute.labels.value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Host.MergeByKey` | `additional.fields[Files_Host_MergeByKey]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_Host_MergeByKey_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.Host.MergeByKey` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Host.MergeByKeyHex` | `additional.fields[Files_Host_MergeByKeyHex]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_Host_MergeByKeyHex_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.Host.MergeByKeyHex` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Host.Role` | `additional.fields[Files_Host_Role]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_Host_Role_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.Host.Role` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Host.Type` | `additional.fields[Files_Host_Type]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_Host_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.Host.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.MergeByKey` | `additional.fields[Files_MergeByKey]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_MergeByKey_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.MergeByKey` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.MergeByKeyHex` | `additional.fields[Files_MergeByKeyHex]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_MergeByKeyHex_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.MergeByKeyHex` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Name` | `target.file.names` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `properties.AdditionalFields.Files.Name` log field is mapped to the `target.file.names` UDM field.  
`Malware` | `properties.AdditionalFields.Count of Files` | `security_result.detection_fields[Count_of_Files]` |   
`Malware` | `properties.AdditionalFields.Files.Role` | `additional.fields[Files_Role]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_Role_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.Role` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.Files.Type` | `additional.fields[Files_Type]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Malware` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`Malware` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`Malware` | `properties.AdditionalFields.Name` | `security_result.detection_fields[Name]` |   
`Malware` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`Malware` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`Ip` | `properties.AdditionalFields.Address` | `principal.ip` | The `valid_address` field is extracted from `properties.AdditionalFields.Address` log field using the Grok pattern. The `valid_address` log field is mapped to the `principal.ip` UDM field.  
`Ip` | `properties.AdditionalFields.Asset` | `principal.asset.attribute.labels[Asset]` |   
`Ip` | `properties.AdditionalFields.DetectionStatus` | `security_result.detection_fields[DetectionStatus]` |   
`Ip` | `properties.AdditionalFields.EntitySources` | `additional.fields[EntitySources]` | Iterate through log field `properties.AdditionalFields.EntitySources`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `EntitySources_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.EntitySources` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Ip` | `properties.AdditionalFields.FirstSeen` | `additional.fields[FirstSeen]` |   
`Ip` | `properties.AdditionalFields.IsIoc` | `security_result.detection_fields[IsIoc]` |   
`Ip` | `properties.AdditionalFields.LastRemediationState` | `security_result.detection_fields[LastRemediationState]` |   
`Ip` | `properties.AdditionalFields.LastVerdict` | `security_result.threat_verdict` | If the `properties.AdditionalFields.LastVerdict` log field value is equal to `Suspicious`, then the `security_result.threat_verdict` UDM field is set to `SUSPICIOUS`.  
  
Otherwise, if the `properties.AdditionalFields.LastVerdict` log field value is equal to `Malicious`, then the `security_result.threat_verdict` UDM field is set to `MALICIOUS`.  
`Ip` | `properties.AdditionalFields.Location.Asn` | `target.artifact.asn` |   
`Ip` | `properties.AdditionalFields.Location.City` | `target.artifact.location.city` |   
`Ip` | `properties.AdditionalFields.Location.CountryCode` | `target.artifact.location.country_or_region` |   
`Ip` | `properties.AdditionalFields.Location.Latitude` | `target.artifact.location.region_coordinates.latitude` |   
`Ip` | `properties.AdditionalFields.Location.Longitude` | `target.artifact.location.region_coordinates.longitude` |   
`Ip` | `properties.AdditionalFields.Location.State` | `target.artifact.location.state` |   
`Ip` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`Ip` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`Ip` | `properties.AdditionalFields.ObservedByDevice.Asset` | `principal.asset.attribute.labels[ObservedByDevice_Asset]` |   
`Ip` | `properties.AdditionalFields.ObservedByDevice.DetailedRoles` | `principal.asset.attribute.labels[ObservedByDevice_DetailedRoles]` | Iterate through log field `properties.AdditionalFields.ObservedByDevice.DetailedRoles`:  
  
The `principal.asset.attribute.labels.key` UDM field is set to `ObservedByDevice_DetailedRoles` and the `properties.AdditionalFields.ObservedByDevice.DetailedRoles` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`Ip` | `properties.AdditionalFields.ObservedByDevice.DnsDomain` | `principal.administrative_domain` | If the `properties.AccountDomain` log field value is empty, then the `properties.AdditionalFields.ObservedByDevice.DnsDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
  
Otherwise, the `principal.asset.attribute.labels.key` UDM field is set to `ObservedByDevice_DnsDomain` and the `properties.AdditionalFields.ObservedByDevice.DnsDomain` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`Ip` | `properties.AdditionalFields.ObservedByDevice.IsDomainJoined` | `principal.asset.attribute.labels[ObservedByDevice_IsDomainJoined]` |   
`Ip` | `properties.AdditionalFields.ObservedByDevice.LeadingHost` | `principal.asset.attribute.labels[ObservedByDevice_LeadingHost]` |   
`Ip` | `properties.AdditionalFields.ObservedByDevice.MachineIdType` | `principal.asset.attribute.labels[ObservedByDevice_MachineIdType]` |   
`Ip` | `properties.AdditionalFields.ObservedByDevice.NetBiosName` | `principal.asset.attribute.labels[ObservedByDevice_NetBiosName]` |   
`Ip` | `properties.AdditionalFields.ObservedByDevice.OSFamily` | `principal.platform` | If the `properties.AdditionalFields.ObservedByDevice.OSFamily` log field value is equal to `Windows`, then the `principal.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.AdditionalFields.ObservedByDevice.OSFamily` log field value is equal to `Mac`, then the `principal.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.AdditionalFields.ObservedByDevice.OSFamily` log field value is equal to `Linux`, then the `principal.platform` UDM field is set to `LINUX`.  
`Ip` | `properties.AdditionalFields.ObservedByDevice.OSVersion` | `principal.platform_version` |   
`Ip` | `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[ObservedByDevice_RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`Ip` | `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[ObservedByDevice_RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ObservedByDevice_RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Ip` | `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[ObservedByDevice_RbacScopes_ScopesPerType_Workloads_Mode]` |   
`Ip` | `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[ObservedByDevice_RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ObservedByDevice_RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Ip` | `properties.AdditionalFields.ObservedByDevice.Role` | `additional.fields[ObservedByDevice_Role]` |   
`Ip` | `properties.AdditionalFields.ObservedByDevice.Type` | `additional.fields[ObservedByDevice_Type]` |   
`Ip` | `properties.AdditionalFields.RbacScopes.ScopesPerType.AppstanceId.Scopes` | `additional.fields[RbacScopes_ScopesPerType_AppstanceId_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.AppstanceId.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_AppstanceId_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.AppstanceId.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Ip` | `properties.AdditionalFields.RbacScopes.ScopesPerType.DiscoveryStreamId.Scopes` | `additional.fields[RbacScopes_ScopesPerType_DiscoveryStreamId_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.DiscoveryStreamId.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_DiscoveryStreamId_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.DiscoveryStreamId.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Ip` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`Ip` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Ip` | `properties.AdditionalFields.RbacScopes.ScopesPerType.RiskCategory.Scopes` | `additional.fields[RbacScopes_ScopesPerType_RiskCategory_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.RiskCategory.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_RiskCategory_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.RiskCategory.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Ip` | `properties.AdditionalFields.RbacScopes.ScopesPerType.UserGroupId.Scopes` | `additional.fields[RbacScopes_ScopesPerType_UserGroupId_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.UserGroupId.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_UserGroupId_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.UserGroupId.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Ip` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Mode]` |   
`Ip` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Ip` | `properties.AdditionalFields.ReferenceId` | `additional.fields[ReferenceId]` |   
`Ip` | `properties.AdditionalFields.RemediationProviders.RemediationDate` | `security_result.detection_fields[RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationDate` and the `properties.AdditionalFields.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Ip` | `properties.AdditionalFields.RemediationProviders.RemediationState` | `security_result.detection_fields[RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationState` and the `properties.AdditionalFields.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Ip` | `properties.AdditionalFields.RemediationProviders.Type` | `security_result.detection_fields[RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_Type` and the `properties.AdditionalFields.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Ip` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`Ip` | `properties.AdditionalFields.Roles` | `additional.fields[Roles]` |   
`Ip` | `properties.AdditionalFields.Source` | `additional.fields[Source]` |   
`Ip` | `properties.AdditionalFields.StartTimeUtc` | `additional.fields[StartTimeUtc]` |   
`Ip` | `properties.AdditionalFields.Stream.Id` | `additional.fields[StreamId]` |   
`Ip` | `properties.AdditionalFields.Stream.Name` | `additional.fields[StreamName]` |   
`Ip` | `properties.AdditionalFields.SuspicionLevel` | `security_result.detection_fields[SuspicionLevel]` |   
`Ip` | `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Ip` | `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Ip` | `properties.AdditionalFields.Count of ThreatAnalysisSummary` | `security_result.detection_fields[Count_of_ThreatAnalysisSummary]` |   
`Ip` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`Ip` | `properties.AdditionalFields.Urn` | `additional.fields[Urn]` |   
`File` | `properties.AdditionalFields.$id` | `additional.fields[$id]` |   
`File` | `properties.AdditionalFields.Asset` | `principal.asset.attribute.labels[Asset]` |   
`File` | `properties.AdditionalFields.CreatedTimeUtc` | `additional.fields[CreatedTimeUtc]` |   
`File` | `properties.AdditionalFields.DetectionStatus` | `security_result.detection_fields[DetectionStatus]` |   
`File` | `properties.AdditionalFields.Directory` | `target.file.full_path` | If the `properties.FolderPath` log field value is empty, then the `properties.AdditionalFields.Directory` log field is mapped to the `target.file.full_path` UDM field.  
  
Otherwise, if the `properties.FolderPath` log field value is _not_ equal to the `properties.AdditionalFields.Directory` log field value, then the `additional.fields.key` UDM field is set to `Directory` and the `properties.AdditionalFields.Directory` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.EnrichmentType` | `additional.fields[EnrichmentType]` |   
`File` | `properties.AdditionalFields.EntitySources` | `additional.fields[EntitySources]` | Iterate through log field `properties.AdditionalFields.EntitySources`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `EntitySources_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.EntitySources` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.FileHashes.$id` | `additional.fields[FileHashes_$id]` | Iterate through log field `properties.AdditionalFields.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `FileHashes_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.FileHashes.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.FileHashes.Algorithm` | `additional.fields[FileHashes_Algorithm]` | Iterate through log field `properties.AdditionalFields.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `FileHashes_Algorithm_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.FileHashes.Algorithm` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.FileHashes.Asset` | `principal.asset.attribute.labels[FileHashes_Asset]` | Iterate through log field `properties.AdditionalFields.FileHashes`:  
  
The `principal.asset.attribute.labels.key` UDM field is set to `FileHashes_Asset` and the `properties.AdditionalFields.FileHashes.Asset` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`File` | `properties.AdditionalFields.FileHashes.FriendlyName` | `additional.fields[FileHashes_FriendlyName]` | Iterate through log field `properties.AdditionalFields.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `FileHashes_FriendlyName_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.FileHashes.FriendlyName` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.FileHashes.Role` | `additional.fields[FileHashes_Role]` | Iterate through log field `properties.AdditionalFields.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `FileHashes_Role_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.FileHashes.Role` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.FileHashes.Type` | `additional.fields[FileHashes_Type]` | Iterate through log field `properties.AdditionalFields.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `FileHashes_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.FileHashes.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.FileHashes.Value` | `target.file.sha1, target.file.sha256, target.file.md5` | Iterate through log field `properties.AdditionalFields.FileHashes`:  
  
If the `properties.AdditionalFields.FileHashes.Algorithm` log field value is equal to `SHA1` and the `properties.SHA1` log field value is empty and the `target.file.sha1` UDM field is empty and the `properties.AdditionalFields.FileHashes.Value` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.AdditionalFields.FileHashes.Value` log field is mapped to the `target.file.sha1` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.FileHashes.Algorithm` log field value is equal to `SHA256` and the `properties.SHA256` log field value is empty and the `target.file.sha256` UDM field is empty and the `properties.AdditionalFields.FileHashes.Value` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.AdditionalFields.FileHashes.Value` log field is mapped to the `target.file.sha256` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.FileHashes.Algorithm` log field value is equal to `MD5` and the `properties.MD5` log field value is empty and the `target.file.md5` UDM field is empty and the `properties.AdditionalFields.FileHashes.Value` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.AdditionalFields.FileHashes.Value` log field is mapped to the `target.file.md5` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.FileHashes.Value` log field is _not_ mapped to the `target.file.sha1`, `target.file.sha256`, or `target.file.md5` UDM fields, then:  
  
If the `properties.AdditionalFields.FileHashes.Algorithm` log field value is equal to `SHA1`, then the `additional.fields.key` UDM field is set to a value generated from the template `FileHashes_SHA1_Value_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.FileHashes.Value` log field is mapped to the `additional.fields.value.string_value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.FileHashes.Algorithm` log field value is equal to `SHA256`, then the `additional.fields.key` UDM field is set to a value generated from the template `FileHashes_SHA256_Value_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.FileHashes.Value` log field is mapped to the `additional.fields.value.string_value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.FileHashes.Algorithm` log field value is equal to `MD5`, then the `additional.fields.key` UDM field is set to a value generated from the template `FileHashes_MD5_Value_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.FileHashes.Value` log field is mapped to the `additional.fields.value.string_value` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to a value generated from the template `FileHashes_Value_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.FileHashes.Value` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.FirstSeen` | `target.file.first_seen_time` |   
`File` | `properties.AdditionalFields.Host.$id` | `additional.fields[Host_$id]` |   
`File` | `properties.AdditionalFields.Host.Asset` | `principal.asset.attribute.labels[Host_Asset]` |   
`File` | `properties.AdditionalFields.Host.AzureID` | `principal.asset.attribute.labels[Host_AzureID]` |   
`File` | `properties.AdditionalFields.Host.DetailedRoles` | `principal.asset.attribute.labels[Host_DetailedRoles]` | Iterate through log field `properties.AdditionalFields.Host.DetailedRoles`:  
  
The `principal.asset.attribute.labels.key` UDM field is set to `Host_DetailedRoles` and the `properties.AdditionalFields.Host.DetailedRoles` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`File` | `properties.AdditionalFields.Host.DetectionStatus` | `security_result.detection_fields[Host_DetectionStatus]` |   
`File` | `properties.AdditionalFields.Host.DnsDomain` | `principal.administrative_domain` | If the `properties.AccountDomain` log field value is empty, then the `properties.AdditionalFields.Host.DnsDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
  
Otherwise, the `principal.asset.attribute.labels.key` UDM field is set to `Host_DnsDomain` and the `properties.AdditionalFields.Host.DnsDomain` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`File` | `properties.AdditionalFields.Host.EnrichmentType` | `additional.fields[Host_EnrichmentType]` |   
`File` | `properties.AdditionalFields.Host.HostMachineId,properties.AdditionalFields.Host.MachineId` | `principal.asset.product_object_id` | If the `properties.AdditionalFields.Host.MachineId` log field value is _not_ empty, then the `properties.AdditionalFields.Host.MachineId` log field is mapped to the `principal.asset.product_object_id` UDM field. If the `properties.AdditionalFields.Host.HostMachineId` log field value is _not_ empty, then the `principal.asset.attribute.labels.key` UDM field is set to `Host_HostMachineId` and the `properties.AdditionalFields.Host.HostMachineId` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
  
Otherwise, the `properties.AdditionalFields.Host.HostMachineId` log field is mapped to the `principal.asset.product_object_id` UDM field.  
`File` | `properties.AdditionalFields.Host.IpInterfaces.$id` | `additional.fields[Host_IpInterfaces_$id]` | Iterate through log field `properties.AdditionalFields.Host.IpInterfaces`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Host_IpInterfaces_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Host.IpInterfaces.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.Host.IpInterfaces.Address` | `principal.ip` | Iterate through log field `properties.AdditionalFields.Host.IpInterfaces`:  
  
The `valid_ipinterface_address` field is extracted from `properties.AdditionalFields.Host.IpInterfaces.Address` log field using the Grok pattern. The `valid_ipinterface_address` log field is mapped to the `principal.ip` UDM field.  
`File` | `properties.AdditionalFields.Host.IpInterfaces.Type` | `additional.fields[Host_IpInterfaces_Type]` | Iterate through log field `properties.AdditionalFields.Host.IpInterfaces`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Host_IpInterfaces_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Host.IpInterfaces.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.Host.IsDomainJoined` | `principal.asset.attribute.labels[Host_IsDomainJoined]` |   
`File` | `properties.AdditionalFields.Host.IsIoc` | `security_result.detection_fields[Host_IsIoc]` |   
`File` | `properties.AdditionalFields.Host.LastRemediationState` | `security_result.detection_fields[Host_LastRemediationState]` |   
`File` | `properties.AdditionalFields.Host.LastVerdict` | `security_result.detection_fields[Host_LastVerdict]` |   
`File` | `properties.AdditionalFields.Host.LeadingHost` | `principal.asset.attribute.labels[Host_LeadingHost]` |   
`File` | `properties.AdditionalFields.Host.MachineIdType` | `principal.asset.attribute.labels[Host_MachineIdType]` |   
`File` | `properties.AdditionalFields.Host.MergeByKey` | `additional.fields[Host_MergeByKey]` |   
`File` | `properties.AdditionalFields.Host.MergeByKeyHex` | `additional.fields[Host_MergeByKeyHex]` |   
`File` | `properties.AdditionalFields.Host.Metadata.MachineEnrichmentInfo` | `additional.fields[Host_Metadata_MachineEnrichmentInfo]` |   
`File` | `properties.AdditionalFields.Host.NetBiosName` | `principal.asset.attribute.labels[Host_NetBiosName]` |   
`File` | `properties.AdditionalFields.Host.OSFamily` | `principal.platform` | If the `properties.AdditionalFields.Host.OSFamily` log field value is equal to `Windows`, then the `principal.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.AdditionalFields.Host.OSFamily` log field value is equal to `Mac`, then the `principal.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.AdditionalFields.Host.OSFamily` log field value is equal to `Linux`, then the `principal.platform` UDM field is set to `LINUX`.  
`File` | `properties.AdditionalFields.Host.OSVersion` | `principal.platform_version` |   
`File` | `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[Host_RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`File` | `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[Host_RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Host_RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[Host_RbacScopes_ScopesPerType_Workloads_Mode]` |   
`File` | `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[Host_RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Host_RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.Host.RemediationProviders.RemediationDate` | `security_result.detection_fields[Host_RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.Host.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_RemediationProviders_RemediationDate` and the `properties.AdditionalFields.Host.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`File` | `properties.AdditionalFields.Host.RemediationProviders.RemediationState` | `security_result.detection_fields[Host_RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.Host.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_RemediationProviders_RemediationState` and the `properties.AdditionalFields.Host.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`File` | `properties.AdditionalFields.Host.RemediationProviders.Type` | `security_result.detection_fields[Host_RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.Host.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_RemediationProviders_Type` and the `properties.AdditionalFields.Host.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`File` | `properties.AdditionalFields.Host.Role` | `additional.fields[Host_Role]` |   
`File` | `properties.AdditionalFields.Host.SuspicionLevel` | `security_result.detection_fields[Host_SuspicionLevel]` |   
`File` | `properties.AdditionalFields.Host.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[Host_ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.Host.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.Host.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`File` | `properties.AdditionalFields.Host.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[Host_ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.Host.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.Host.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`File` | `properties.AdditionalFields.Host.Type` | `additional.fields[Host_Type]` |   
`File` | `properties.AdditionalFields.Host.Metadata.IncriminationTags` | `principal.asset.attribute.labels[Host_Metadata_IncriminationTags]` |   
`File` | `properties.AdditionalFields.Id` | `additional.fields[Id]` |   
`File` | `properties.AdditionalFields.IsIoc` | `security_result.detection_fields[IsIoc]` |   
`File` | `properties.AdditionalFields.IsPe` | `additional.fields[IsPe]` |   
`File` | `properties.AdditionalFields.KnownPrevalence` | `security_result.detection_fields[KnownPrevalence]` |   
`File` | `properties.AdditionalFields.LastAccessTimeUtc` | `security_result.detection_fields[LastAccessTimeUtc]` |   
`File` | `properties.AdditionalFields.LastRemediationState` | `security_result.detection_fields[LastRemediationState]` |   
`File` | `properties.AdditionalFields.LastVerdict` | `security_result.threat_verdict` | If the `properties.AdditionalFields.LastVerdict` log field value is equal to `Suspicious`, then the `security_result.threat_verdict` UDM field is set to `SUSPICIOUS`.  
  
Otherwise, if the `properties.AdditionalFields.LastVerdict` log field value is equal to `Malicious`, then the `security_result.threat_verdict` UDM field is set to `MALICIOUS`.  
`File` | `properties.AdditionalFields.LastWriteTimeUtc` | `security_result.detection_fields[LastWriteTimeUtc]` |   
`File` | `properties.AdditionalFields.LsHash` | `security_result.detection_fields[LsHash]` |   
`File` | `properties.AdditionalFields.MalwareFamily` | `security_result.detection_fields[MalwareFamily]` |   
`File` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`File` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`File` | `properties.AdditionalFields.Name` | `target.file.names` | If the `properties.FileName` log field value is empty, then the `properties.AdditionalFields.Name` log field is mapped to the `target.file.names` UDM field.  
  
Otherwise, if the `properties.FileName` log field value is _not_ equal to the `properties.AdditionalFields.FileName` log field value, then the `additional.fields.key` UDM field is set to `Name` and the `properties.AdditionalFields.Name` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.Publisher` | `target.file.exif_info.company` |   
`File` | `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes` | `additional.fields[RbacScopes_ScopesPerType_AdminUnits_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_AdminUnits_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.RbacScopes.ScopesPerType.AppstanceId.Scopes` | `additional.fields[RbacScopes_ScopesPerType_AppstanceId_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.AppstanceId.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_AppstanceId_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.AppstanceId.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`File` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.RbacScopes.ScopesPerType.RiskCategory.Scopes` | `additional.fields[RbacScopes_ScopesPerType_RiskCategory_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.RiskCategory.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_RiskCategory_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.RiskCategory.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.RbacScopes.ScopesPerType.UserGroupId.Scopes` | `additional.fields[RbacScopes_ScopesPerType_UserGroupId_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.UserGroupId.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_UserGroupId_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.UserGroupId.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Mode]` |   
`File` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`File` | `properties.AdditionalFields.ReferenceId` | `additional.fields[ReferenceId]` |   
`File` | `properties.AdditionalFields.RemediationProviders.RemediationDate` | `security_result.detection_fields[RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationDate` and the `properties.AdditionalFields.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`File` | `properties.AdditionalFields.RemediationProviders.RemediationState` | `security_result.detection_fields[RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationState` and the `properties.AdditionalFields.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`File` | `properties.AdditionalFields.RemediationProviders.Type` | `security_result.detection_fields[RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_Type` and the `properties.AdditionalFields.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`File` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`File` | `properties.AdditionalFields.SizeInBytes` | `target.file.size` | If the `properties.FileSize` log field value is empty, then the `properties.AdditionalFields.SizeInBytes` log field is mapped to the `target.file.size` UDM field.  
`File` | `properties.AdditionalFields.SuspicionLevel` | `security_result.detection_fields[SuspicionLevel]` |   
`File` | `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`File` | `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`File` | `properties.AdditionalFields.Count of ThreatAnalysisSummary` | `security_result.detection_fields[Count_of_ThreatAnalysisSummary]` |   
`File` | `properties.AdditionalFields.ThreatFamilyName` | `security_result.detection_fields[ThreatFamilyName]` |   
`File` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`CloudApplication` | `properties.AdditionalFields.AppId` | `additional.fields[AppId]` |   
`CloudApplication` | `properties.AdditionalFields.EntitySources` | `additional.fields[EntitySources]` | Iterate through log field `properties.AdditionalFields.EntitySources`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `EntitySources_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.EntitySources` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`CloudApplication` | `properties.AdditionalFields.InstanceId` | `additional.fields[InstanceId]` |   
`CloudApplication` | `properties.AdditionalFields.InstanceName` | `additional.fields[InstanceName]` |   
`CloudApplication` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`CloudApplication` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`CloudApplication` | `properties.AdditionalFields.Name` | `principal.application` | If the `properties.Application` log field value is empty, then the `properties.AdditionalFields.Name` log field is mapped to the `principal.application` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `Name` and the `properties.AdditionalFields.Name` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`CloudApplication` | `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes` | `additional.fields[RbacScopes_ScopesPerType_AdminUnits_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_AdminUnits_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`CloudApplication` | `properties.AdditionalFields.RbacScopes.ScopesPerType.AppstanceId.Scopes` | `additional.fields[RbacScopes_ScopesPerType_AppstanceId_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.AppstanceId.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_AppstanceId_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.AppstanceId.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`CloudApplication` | `properties.AdditionalFields.RbacScopes.ScopesPerType.DiscoveryStreamId.Scopes` | `additional.fields[RbacScopes_ScopesPerType_DiscoveryStreamId_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.DiscoveryStreamId.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_DiscoveryStreamId_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.DiscoveryStreamId.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`CloudApplication` | `properties.AdditionalFields.RbacScopes.ScopesPerType.RiskCategory.Scopes` | `additional.fields[RbacScopes_ScopesPerType_RiskCategory_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.RiskCategory.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_RiskCategory_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.RiskCategory.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`CloudApplication` | `properties.AdditionalFields.RbacScopes.ScopesPerType.UserGroupId.Scopes` | `additional.fields[RbacScopes_ScopesPerType_UserGroupId_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.UserGroupId.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_UserGroupId_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.UserGroupId.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`CloudApplication` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`CloudApplication` | `properties.AdditionalFields.Risk` | `additional.fields[Risk]` |   
`CloudApplication` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`CloudApplication` | `properties.AdditionalFields.SaasId` | `additional.fields[SaasId]` |   
`CloudApplication` | `properties.AdditionalFields.Stream.Id` | `additional.fields[StreamId]` |   
`CloudApplication` | `properties.AdditionalFields.Stream.Name` | `additional.fields[StreamName]` |   
`CloudApplication` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`Machine` | `properties.AdditionalFields.Asset` | `principal.asset.attribute.labels[Asset]` |   
`Machine` | `properties.AdditionalFields.AzureID` | `principal.asset.attribute.labels[AzureID]` |   
`Machine` | `properties.AdditionalFields.DetailedRoles` | `principal.asset.attribute.labels[DetailedRoles]` | Iterate through log field `properties.AdditionalFields.DetailedRoles`:  
  
The `principal.asset.attribute.labels.key` UDM field is set to `DetailedRoles` and the `properties.AdditionalFields.DetailedRoles` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`Machine` | `properties.AdditionalFields.DetectionStatus` | `security_result.detection_fields[DetectionStatus]` |   
`Machine` | `properties.AdditionalFields.DnsDomain` | `principal.administrative_domain` | If the `properties.AccountDomain` log field value is empty, then the `properties.AdditionalFields.DnsDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `DnsDomain` and the `properties.AdditionalFields.DnsDomain` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Machine` | `properties.AdditionalFields.EdgeRole` | `additional.fields[EdgeRole]` |   
`Machine` | `properties.AdditionalFields.EnrichmentType` | `additional.fields[EnrichmentType]` |   
`Machine` | `properties.AdditionalFields.Id` | `additional.fields[Id]` |   
`Machine` | `properties.AdditionalFields.IpInterfaces.$id` | `additional.fields[IpInterfaces_$id]` | Iterate through log field `properties.AdditionalFields.IpInterfaces`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `IpInterfaces_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.IpInterfaces.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Machine` | `properties.AdditionalFields.IpInterfaces.Address` | `principal.ip` | Iterate through log field `properties.AdditionalFields.IpInterfaces`:  
  
The `valid_ipinterface_address` field is extracted from `properties.AdditionalFields.IpInterfaces.Address` log field using the Grok pattern. The `valid_ipinterface_address` log field is mapped to the `principal.ip` UDM field.  
`Machine` | `properties.AdditionalFields.IpInterfaces.Type` | `additional.fields[IpInterfaces_Type]` | Iterate through log field `properties.AdditionalFields.IpInterfaces`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `IpInterfaces_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.IpInterfaces.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Machine` | `properties.AdditionalFields.IsDomainJoined` | `principal.asset.attribute.labels[IsDomainJoined]` |   
`Machine` | `properties.AdditionalFields.IsIoc` | `security_result.detection_fields[IsIoc]` |   
`Machine` | `properties.AdditionalFields.LastRemediationState` | `security_result.detection_fields[LastRemediationState]` |   
`Machine` | `properties.AdditionalFields.LastVerdict` | `security_result.threat_verdict` | If the `properties.AdditionalFields.LastVerdict` log field value is equal to `Suspicious`, then the `security_result.threat_verdict` UDM field is set to `SUSPICIOUS`.  
  
Otherwise, if the `properties.AdditionalFields.LastVerdict` log field value is equal to `Malicious`, then the `security_result.threat_verdict` UDM field is set to `MALICIOUS`.  
`Machine` | `properties.AdditionalFields.LeadingHost` | `principal.asset.attribute.labels[LeadingHost]` |   
`Machine` | `properties.AdditionalFields.MachineIdType` | `principal.asset.attribute.labels[MachineIdType]` |   
`Machine` | `properties.AdditionalFields.MDIOriginalEntity` | `security_result.detection_fields[MDIOriginalEntity]` |   
`Machine` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`Machine` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`Machine` | `properties.AdditionalFields.NetBiosName` | `principal.asset.attribute.labels[NetBiosName]` |   
`Machine` | `properties.AdditionalFields.OSFamily` | `principal.platform` | If the `properties.AdditionalFields.OSFamily` log field value matches the regular expression pattern `(?i)(Windows)`, then the `principal.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.AdditionalFields.OSFamily` log field value is equal to `Mac`, then the `principal.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.AdditionalFields.OSFamily` log field value is equal to `Linux`, then the `principal.platform` UDM field is set to `LINUX`.  
`Machine` | `properties.AdditionalFields.OSVersion` | `principal.platform_version` |   
`Machine` | `properties.AdditionalFields.Partial` | `additional.fields[Partial]` |   
`Machine` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`Machine` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Machine` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Mode]` |   
`Machine` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Machine` | `properties.AdditionalFields.RemediationProviders.RemediationDate` | `security_result.detection_fields[RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationDate` and the `properties.AdditionalFields.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Machine` | `properties.AdditionalFields.RemediationProviders.RemediationState` | `security_result.detection_fields[RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationState` and the `properties.AdditionalFields.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Machine` | `properties.AdditionalFields.RemediationProviders.Type` | `security_result.detection_fields[RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_Type` and the `properties.AdditionalFields.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Machine` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`Machine` | `properties.AdditionalFields.Roles` | `additional.fields[Roles]` | Iterate through log field `properties.AdditionalFields.Roles`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Roles_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Roles` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Machine` | `properties.AdditionalFields.ShouldResolveIp` | `additional.fields[ShouldResolveIp]` |   
`Machine` | `properties.AdditionalFields.SuspicionLevel` | `security_result.detection_fields[SuspicionLevel]` |   
`Machine` | `properties.AdditionalFields.Tags.ProviderName` | `security_result.detection_fields[Tags_ProviderName]` | Iterate through log field `properties.AdditionalFields.Tags`:  
  
The `security_result.detection_fields.key` UDM field is set to `Tags_ProviderName` and the `properties.AdditionalFields.Tags.ProviderName` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Machine` | `properties.AdditionalFields.Tags.TagId` | `security_result.detection_fields[Tags_TagId]` | Iterate through log field `properties.AdditionalFields.Tags`:  
  
The `security_result.detection_fields.key` UDM field is set to `Tags_TagId` and the `properties.AdditionalFields.Tags.TagId` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Machine` | `properties.AdditionalFields.Tags.TagName` | `security_result.detection_fields[Tags_TagName]` | Iterate through log field `properties.AdditionalFields.Tags`:  
  
The `security_result.detection_fields.key` UDM field is set to `Tags_TagName` and the `properties.AdditionalFields.Tags.TagName` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Machine` | `properties.AdditionalFields.Tags.TagType` | `security_result.detection_fields[Tags_Type]` | Iterate through log field `properties.AdditionalFields.Tags`:  
  
The `security_result.detection_fields.key` UDM field is set to `Tags_Type` and the `properties.AdditionalFields.Tags.TagType` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Machine` | `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Machine` | `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Machine` | `properties.AdditionalFields.Count of ThreatAnalysisSummary` | `security_result.detection_fields[Count_of_ThreatAnalysisSummary]` |   
`Machine` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`MailCluster` | `properties.AdditionalFields.ClusterBy` | `security_result.detection_fields[ClusterBy]` |   
`MailCluster` | `properties.AdditionalFields.ClusterByValue` | `security_result.detection_fields[ClusterByValue]` |   
`MailCluster` | `properties.AdditionalFields.ClusterGroup` | `security_result.detection_fields[ClusterGroup]` |   
`MailCluster` | `properties.AdditionalFields.ClusterQueryEndTime` | `additional.fields[ClusterQueryEndTime]` |   
`MailCluster` | `properties.AdditionalFields.ClusterQueryStartTime` | `additional.fields[ClusterQueryStartTime]` |   
`MailCluster` | `properties.AdditionalFields.ClusterSourceIdentifier` | `additional.fields[ClusterSourceIdentifier]` |   
`MailCluster` | `properties.AdditionalFields.ClusterSourceType` | `security_result.detection_fields[ClusterSourceType]` |   
`MailCluster` | `properties.AdditionalFields.CountByDeliveryLocation.DeletedFolder` | `security_result.detection_fields[CountByDeliveryLocation_DeletedFolder]` |   
`MailCluster` | `properties.AdditionalFields.CountByDeliveryLocation.External` | `security_result.detection_fields[CountByDeliveryLocation_External]` |   
`MailCluster` | `properties.AdditionalFields.CountByDeliveryLocation.Inbox` | `security_result.detection_fields[CountByDeliveryLocation_Inbox]` |   
`MailCluster` | `properties.AdditionalFields.CountByDeliveryLocation.JunkFolder` | `security_result.detection_fields[CountByDeliveryLocation_JunkFolder]` |   
`MailCluster` | `properties.AdditionalFields.CountByDeliveryLocation.Quarantine` | `security_result.detection_fields[CountByDeliveryLocation_Quarantine]` |   
`MailCluster` | `properties.AdditionalFields.CountByProtectionStatus.Blocked` | `security_result.detection_fields[CountByProtectionStatus_Blocked]` |   
`MailCluster` | `properties.AdditionalFields.CountByProtectionStatus.Delivered` | `security_result.detection_fields[CountByProtectionStatus_Delivered]` |   
`MailCluster` | `properties.AdditionalFields.CountByProtectionStatus.DeliveredAsSpam` | `security_result.detection_fields[CountByProtectionStatus_DeliveredAsSpam]` |   
`MailCluster` | `properties.AdditionalFields.CountByThreatType.HighConfPhish` | `security_result.detection_fields[CountByThreatType_HighConfPhish]` |   
`MailCluster` | `properties.AdditionalFields.CountByThreatType.MaliciousUrl` | `security_result.detection_fields[CountByThreatType_MaliciousUrl]` |   
`MailCluster` | `properties.AdditionalFields.CountByThreatType.Malware` | `security_result.detection_fields[CountByThreatType_Malware]` |   
`MailCluster` | `properties.AdditionalFields.CountByThreatType.Phish` | `security_result.detection_fields[CountByThreatType_Phish]` |   
`MailCluster` | `properties.AdditionalFields.CountByThreatType.Spam` | `security_result.detection_fields[CountByThreatType_Spam]` |   
`MailCluster` | `properties.AdditionalFields.EntitySources` | `additional.fields[EntitySources]` | Iterate through log field `properties.AdditionalFields.EntitySources`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `EntitySources_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.EntitySources` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailCluster` | `properties.AdditionalFields.FirstSeen` | `additional.fields[FirstSeen]` |   
`MailCluster` | `properties.AdditionalFields.IsVolumeAnamoly` | `security_result.detection_fields[IsVolumeAnamoly]` |   
`MailCluster` | `properties.AdditionalFields.LastRemediationState` | `security_result.detection_fields[LastRemediationState]` |   
`MailCluster` | `properties.AdditionalFields.LastVerdict` | `security_result.threat_verdict` | If the `properties.AdditionalFields.LastVerdict` log field value is equal to `Suspicious`, then the `security_result.threat_verdict` UDM field is set to `SUSPICIOUS`.  
  
Otherwise, if the `properties.AdditionalFields.LastVerdict` log field value is equal to `Malicious`, then the `security_result.threat_verdict` UDM field is set to `MALICIOUS`.  
`MailCluster` | `properties.AdditionalFields.MailCount` | `security_result.detection_fields[MailCount]` |   
`MailCluster` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`MailCluster` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`MailCluster` | `properties.AdditionalFields.NetworkMessageIds` | `security_result.detection_fields[NetworkMessageIds]` | Iterate through log field `properties.AdditionalFields.NetworkMessageIds`:  
  
The `security_result.detection_fields.key` UDM field is set to `NetworkMessageIds` and the `properties.AdditionalFields.NetworkMessageIds` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailCluster` | `properties.AdditionalFields.Query` | `security_result.detection_fields[Query]` |   
`MailCluster` | `properties.AdditionalFields.QueryStartTime` | `additional.fields[QueryStartTime]` |   
`MailCluster` | `properties.AdditionalFields.QueryTime` | `additional.fields[QueryTime]` |   
`MailCluster` | `properties.AdditionalFields.RemediationProviders.RemediationDate` | `security_result.detection_fields[RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationDate` and the `properties.AdditionalFields.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailCluster` | `properties.AdditionalFields.RemediationProviders.RemediationState` | `security_result.detection_fields[RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationState` and the `properties.AdditionalFields.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailCluster` | `properties.AdditionalFields.RemediationProviders.Type` | `security_result.detection_fields[RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_Type` and the `properties.AdditionalFields.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailCluster` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`MailCluster` | `properties.AdditionalFields.Source` | `additional.fields[Source]` |   
`MailCluster` | `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailCluster` | `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailCluster` | `properties.AdditionalFields.Count of ThreatAnalysisSummary` | `security_result.detection_fields[Count_of_ThreatAnalysisSummary]` |   
`MailCluster` | `properties.AdditionalFields.ThreatIntelligence.ProviderName` | `security_result.detection_fields[ThreatIntelligence_ProviderName]` | Iterate through log field `properties.AdditionalFields.ThreatIntelligence`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatIntelligence_ProviderName` and the `properties.AdditionalFields.ThreatIntelligence.ProviderName` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailCluster` | `properties.AdditionalFields.ThreatIntelligence.ThreatName` | `security_result.threat_name` | Iterate through log field `properties.AdditionalFields.ThreatIntelligence`:  
  
The `properties.AdditionalFields.ThreatIntelligence.ThreatName` log field is mapped to the `security_result.threat_name` UDM field.  
`MailCluster` | `properties.AdditionalFields.ThreatIntelligence.ThreatType` | `security_result.detection_fields[ThreatIntelligence_ThreatType]` | Iterate through log field `properties.AdditionalFields.ThreatIntelligence`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatIntelligence_ThreatType` and the `properties.AdditionalFields.ThreatIntelligence.ThreatType` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailCluster` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`MailCluster` | `properties.AdditionalFields.Urn` | `additional.fields[Urn]` |   
`Mailbox` | `properties.AdditionalFields.AadId` | `principal.user.attribute.labels[AadId]` |   
`Mailbox` | `properties.AdditionalFields.AccountName` | `principal.user.userid` | If the `properties.AccountName` log field value is empty, then the `properties.AdditionalFields.AccountName` log field is mapped to the `principal.user.userid` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `AccountName` and the `properties.AdditionalFields.AccountName` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.DisplayName` | `principal.user.user_display_name` | If the `properties.AccountUpn` log field value is empty, then the `properties.AdditionalFields.DisplayName` log field is mapped to the `principal.user.user_display_name` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `DisplayName` and the `properties.AdditionalFields.DisplayName` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.DomainName` | `principal.administrative_domain` | If the `properties.AccountDomain` log field value is empty, then the `properties.AdditionalFields.DomainName` log field is mapped to the `principal.administrative_domain` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `DomainName` and the `properties.AdditionalFields.DomainName` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Mailbox` | `properties.AdditionalFields.EndTimeUtc` | `principal.user.attribute.labels[EndTimeUtc]` |   
`Mailbox` | `properties.AdditionalFields.EntitySources` | `additional.fields[EntitySources]` | Iterate through log field `properties.AdditionalFields.EntitySources`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `EntitySources_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.EntitySources` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Mailbox` | `properties.AdditionalFields.FirstSeen` | `additional.fields[FirstSeen]` |   
`Mailbox` | `properties.AdditionalFields.LastRemediationState` | `security_result.detection_fields[LastRemediationState]` |   
`Mailbox` | `properties.AdditionalFields.LastVerdict` | `security_result.threat_verdict` | If the `properties.AdditionalFields.LastVerdict` log field value is equal to `Suspicious`, then the `security_result.threat_verdict` UDM field is set to `SUSPICIOUS`.  
  
Otherwise, if the `properties.AdditionalFields.LastVerdict` log field value is equal to `Malicious`, then the `security_result.threat_verdict` UDM field is set to `MALICIOUS`.  
`Mailbox` | `properties.AdditionalFields.MailboxPrimaryAddress` | `principal.user.email_addresses` | If the `properties.AdditionalFields.MailboxPrimaryAddress` log field value is _not_ empty and the `properties.AdditionalFields.MailboxPrimaryAddress` log field value matches the regular expression pattern `^.+@.+$` and the `properties.AdditionalFields.MailboxPrimaryAddress` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.AdditionalFields.MailboxPrimaryAddress` log field is mapped to the `principal.user.email_addresses` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `MailboxPrimaryAddress` and the `properties.AdditionalFields.MailboxPrimaryAddress` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`Mailbox` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`Mailbox` | `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes` | `additional.fields[RbacScopes_ScopesPerType_AdminUnits_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_AdminUnits_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Mailbox` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Mailbox` | `properties.AdditionalFields.RemediationProviders.RemediationDate` | `security_result.detection_fields[RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationDate` and the `properties.AdditionalFields.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.RemediationProviders.RemediationState` | `security_result.detection_fields[RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationState` and the `properties.AdditionalFields.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.RemediationProviders.Type` | `security_result.detection_fields[RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_Type` and the `properties.AdditionalFields.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.RiskLevel` | `additional.fields[RiskLevel]` |   
`Mailbox` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`Mailbox` | `properties.AdditionalFields.Source` | `additional.fields[Source]` |   
`Mailbox` | `properties.AdditionalFields.SourceEntityId` | `security_result.associations.id` |   
`Mailbox` | `properties.AdditionalFields.SourceEntityType` | `security_result.associations.type` | If the `properties.AdditionalFields.SourceEntityType` log field value is `Malware`, then the `security_result.associations.type` UDM field is set to `MALWARE`.  
  
Otherwise, the `security_result.associations.type` UDM field is set to `ASSOCIATION_TYPE_UNSPECIFIED`.  
`Mailbox` | `properties.AdditionalFields.SourceExtendedProperties` | `additional.fields[SourceExtendedProperties]` |   
`Mailbox` | `properties.AdditionalFields.SourceThreatName` | `security_result.threat_name` |   
`Mailbox` | `properties.AdditionalFields.SourceThreatType` | `security_result.detection_fields[SourceThreatType]` |   
`Mailbox` | `properties.AdditionalFields.StartTimeUtc` | `additional.fields[StartTimeUtc]` |   
`Mailbox` | `properties.AdditionalFields.Tags.ProviderName` | `security_result.detection_fields[Tags_ProviderName]` | Iterate through log field `properties.AdditionalFields.Tags`:  
  
The `security_result.detection_fields.key` UDM field is set to `Tags_ProviderName` and the `properties.AdditionalFields.Tags.ProviderName` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.Tags.TagId` | `security_result.detection_fields[Tags_TagId]` | Iterate through log field `properties.AdditionalFields.Tags`:  
  
The `security_result.detection_fields.key` UDM field is set to `Tags_TagId` and the `properties.AdditionalFields.Tags.TagId` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.Tags.TagName` | `security_result.detection_fields[Tags_TagName]` | Iterate through log field `properties.AdditionalFields.Tags`:  
  
The `security_result.detection_fields.key` UDM field is set to `Tags_TagName` and the `properties.AdditionalFields.Tags.TagName` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.Tags.TagType` | `security_result.detection_fields[Tags_Type]` | Iterate through log field `properties.AdditionalFields.Tags`:  
  
The `security_result.detection_fields.key` UDM field is set to `Tags_Type` and the `properties.AdditionalFields.Tags.TagType` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.Count of ThreatAnalysisSummary` | `security_result.detection_fields[Count_of_ThreatAnalysisSummary]` |   
`Mailbox` | `properties.AdditionalFields.ThreatIntelligence.ProviderName` | `security_result.detection_fields[ThreatIntelligence_ProviderName]` | Iterate through log field `properties.AdditionalFields.ThreatIntelligence`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatIntelligence_ProviderName` and the `properties.AdditionalFields.ThreatIntelligence.ProviderName` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.ThreatIntelligence.ThreatName` | `security_result.threat_name` | Iterate through log field `properties.AdditionalFields.ThreatIntelligence`:  
  
The `properties.AdditionalFields.ThreatIntelligence.ThreatName` log field is mapped to the `security_result.threat_name` UDM field.  
`Mailbox` | `properties.AdditionalFields.ThreatIntelligence.ThreatType` | `security_result.detection_fields[ThreatIntelligence_ThreatType]` | Iterate through log field `properties.AdditionalFields.ThreatIntelligence`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatIntelligence_ThreatType` and the `properties.AdditionalFields.ThreatIntelligence.ThreatType` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`Mailbox` | `properties.AdditionalFields.Upn` | `principal.user.email_addresses` | If the `properties.AdditionalFields.Upn` log field value is _not_ empty and the `properties.AdditionalFields.Upn` log field value matches the regular expression pattern `^.+@.+$` and the `properties.AdditionalFields.Upn` log field value matches the regular expression pattern `^.{0,255}$`, then the `properties.AdditionalFields.Upn` log field is mapped to the `principal.user.email_addresses` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `Upn` and the `properties.AdditionalFields.Upn` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`Mailbox` | `properties.AdditionalFields.Urn` | `additional.fields[Urn]` |   
`Mailbox` | `properties.AdditionalFields.UserSid` | `principal.user.windows_sid` | If the `properties.AccountSid` log field value is empty, then the `properties.AdditionalFields.UserSid` log field is mapped to the `principal.user.windows_sid` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `UserSid` and the `properties.AdditionalFields.UserSid` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`Url` | `properties.AdditionalFields.ClickCount` | `additional.fields[ClickCount]` |   
`Url` | `properties.AdditionalFields.DetectionStatus` | `security_result.detection_fields[DetectionStatus]` |   
`Url` | `properties.AdditionalFields.EmailCount` | `additional.fields[EmailCount]` |   
`Url` | `properties.AdditionalFields.EntitySources` | `additional.fields[EntitySources]` | Iterate through log field `properties.AdditionalFields.EntitySources`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `EntitySources_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.EntitySources` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Url` | `properties.AdditionalFields.FirstSeen` | `additional.fields[FirstSeen]` |   
`Url` | `properties.AdditionalFields.IsIoc` | `security_result.detection_fields[IsIoc]` |   
`Url` | `properties.AdditionalFields.LastRemediationState` | `security_result.detection_fields[LastRemediationState]` |   
`Url` | `properties.AdditionalFields.LastVerdict` | `security_result.threat_verdict` | If the `properties.AdditionalFields.LastVerdict` log field value is equal to `Suspicious`, then the `security_result.threat_verdict` UDM field is set to `SUSPICIOUS`.  
  
Otherwise, if the `properties.AdditionalFields.LastVerdict` log field value is equal to `Malicious`, then the `security_result.threat_verdict` UDM field is set to `MALICIOUS`.  
`Url` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`Url` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`Url` | `properties.AdditionalFields.ObservedByDevice.Asset` | `principal.asset.attribute.labels[ObservedByDevice_Asset]` |   
`Url` | `properties.AdditionalFields.ObservedByDevice.DetailedRoles` | `principal.asset.attribute.labels[ObservedByDevice_DetailedRoles]` | Iterate through log field `properties.AdditionalFields.ObservedByDevice.DetailedRoles`:  
  
The `principal.asset.attribute.labels.key` UDM field is set to `ObservedByDevice_DetailedRoles` and the `properties.AdditionalFields.ObservedByDevice.DetailedRoles` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`Url` | `properties.AdditionalFields.ObservedByDevice.DnsDomain` | `principal.administrative_domain` | If the `properties.AccountDomain` log field value is empty, then the `properties.AdditionalFields.ObservedByDevice.DnsDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
  
Otherwise, the `principal.asset.attribute.labels.key` UDM field is set to `ObservedByDevice_DnsDomain` and the `properties.AdditionalFields.ObservedByDevice.DnsDomain` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`Url` | `properties.AdditionalFields.ObservedByDevice.IsDomainJoined` | `principal.asset.attribute.labels[ObservedByDevice_IsDomainJoined]` |   
`Url` | `properties.AdditionalFields.ObservedByDevice.LeadingHost` | `principal.asset.attribute.labels[ObservedByDevice_LeadingHost]` |   
`Url` | `properties.AdditionalFields.ObservedByDevice.MachineIdType` | `principal.asset.attribute.labels[ObservedByDevice_MachineIdType]` |   
`Url` | `properties.AdditionalFields.ObservedByDevice.NetBiosName` | `principal.asset.attribute.labels[ObservedByDevice_NetBiosName]` |   
`Url` | `properties.AdditionalFields.ObservedByDevice.OSFamily` | `principal.platform` | If the `properties.AdditionalFields.ObservedByDevice.OSFamily` log field value is equal to `Windows`, then the `principal.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.AdditionalFields.ObservedByDevice.OSFamily` log field value is equal to `Mac`, then the `principal.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.AdditionalFields.ObservedByDevice.OSFamily` log field value is equal to `Linux`, then the `principal.platform` UDM field is set to `LINUX`.  
`Url` | `properties.AdditionalFields.ObservedByDevice.OSVersion` | `principal.platform_version` |   
`Url` | `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[ObservedByDevice_RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`Url` | `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[ObservedByDevice_RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ObservedByDevice_RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Url` | `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[ObservedByDevice_RbacScopes_ScopesPerType_Workloads_Mode]` |   
`Url` | `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[ObservedByDevice_RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ObservedByDevice_RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ObservedByDevice.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Url` | `properties.AdditionalFields.ObservedByDevice.Role` | `additional.fields[ObservedByDevice_Role]` |   
`Url` | `properties.AdditionalFields.ObservedByDevice.Type` | `additional.fields[ObservedByDevice_Type]` |   
`Url` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`Url` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Url` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Mode]` |   
`Url` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Url` | `properties.AdditionalFields.ReferenceId` | `additional.fields[ReferenceId]` |   
`Url` | `properties.AdditionalFields.RemediationProviders.RemediationDate` | `security_result.detection_fields[RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationDate` and the `properties.AdditionalFields.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Url` | `properties.AdditionalFields.RemediationProviders.RemediationState` | `security_result.detection_fields[RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationState` and the `properties.AdditionalFields.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Url` | `properties.AdditionalFields.RemediationProviders.Type` | `security_result.detection_fields[RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_Type` and the `properties.AdditionalFields.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Url` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`Url` | `properties.AdditionalFields.Source` | `additional.fields[Source]` |   
`Url` | `properties.AdditionalFields.SuspicionLevel` | `security_result.detection_fields[SuspicionLevel]` |   
`Url` | `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Url` | `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Url` | `properties.AdditionalFields.Count of ThreatAnalysisSummary` | `security_result.detection_fields[Count_of_ThreatAnalysisSummary]` |   
`Url` | `properties.AdditionalFields.ThreatIntelligence.ProviderName` | `security_result.detection_fields[ThreatIntelligence_ProviderName]` | Iterate through log field `properties.AdditionalFields.ThreatIntelligence`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatIntelligence_ProviderName` and the `properties.AdditionalFields.ThreatIntelligence.ProviderName` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Url` | `properties.AdditionalFields.ThreatIntelligence.ThreatName` | `security_result.threat_name` | Iterate through log field `properties.AdditionalFields.ThreatIntelligence`:  
  
The `properties.AdditionalFields.ThreatIntelligence.ThreatName` log field is mapped to the `security_result.threat_name` UDM field.  
`Url` | `properties.AdditionalFields.ThreatIntelligence.ThreatType` | `security_result.detection_fields[ThreatIntelligence_ThreatType]` | Iterate through log field `properties.AdditionalFields.ThreatIntelligence`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatIntelligence_ThreatType` and the `properties.AdditionalFields.ThreatIntelligence.ThreatType` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`Url` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`Url` | `properties.AdditionalFields.Url` | `target.url` | If the `properties.RemoteUrl` log field value is empty, then the `properties.AdditionalFields.Url` log field is mapped to the `target.url` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `Url` and the `properties.AdditionalFields.Url` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`Url` | `properties.AdditionalFields.Urn` | `additional.fields[Urn]` |   
`User` | `properties.AdditionalFields.AadTenantId` | `principal.user.attribute.labels[AadTenantId]` |   
`User` | `properties.AdditionalFields.AadUserId` | `principal.user.attribute.labels[AadUserId]` |   
`User` | `properties.AdditionalFields.Asset` | `principal.asset.attribute.labels[Asset]` |   
`User` | `properties.AdditionalFields.CloudAppAccountId` | `additional.fields[CloudAppAccountId]` |   
`User` | `properties.AdditionalFields.DetectionStatus` | `security_result.detection_fields[DetectionStatus]` |   
`User` | `properties.AdditionalFields.DisplayName` | `principal.user.user_display_name` | If the `properties.AccountUpn` log field value is empty, then the `properties.AdditionalFields.DisplayName` log field is mapped to the `principal.user.user_display_name` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `DisplayName` and the `properties.AdditionalFields.DisplayName` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`User` | `properties.AdditionalFields.EdgeRole` | `additional.fields[EdgeRole]` |   
`User` | `properties.AdditionalFields.EntitySources` | `additional.fields[EntitySources]` | Iterate through log field `properties.AdditionalFields.EntitySources`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `EntitySources_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.EntitySources` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.Host.$id` | `additional.fields[Host_$id]` |   
`User` | `properties.AdditionalFields.Host.Asset` | `principal.asset.attribute.labels[Host_Asset]` |   
`User` | `properties.AdditionalFields.Host.DetailedRoles` | `principal.asset.attribute.labels[Host_DetailedRoles]` | Iterate through log field `properties.AdditionalFields.Host.DetailedRoles`:  
  
The `principal.asset.attribute.labels.key` UDM field is set to `Host_DetailedRoles` and the `properties.AdditionalFields.Host.DetailedRoles` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`User` | `properties.AdditionalFields.Host.DetectionStatus` | `security_result.detection_fields[Host_DetectionStatus]` |   
`User` | `properties.AdditionalFields.Host.DnsDomain,properties.AdditionalFields.NTDomain` | `principal.administrative_domain` | If the `properties.AccountDomain` log field value is empty, then if the `properties.AdditionalFields.Host.DnsDomain` log field value is _not_ empty, then the `properties.AdditionalFields.Host.DnsDomain` log field is mapped to the `principal.administrative_domain` UDM field. If the `properties.AdditionalFields.NTDomain` log field value is _not_ empty, then the `additional.fields.key` UDM field is set to `NTDomain` and the `properties.AdditionalFields.NTDomain` log field is mapped to the `additional.fields.value.string_value` UDM field. Otherwise, the `properties.AdditionalFields.NTDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
  
Otherwise, the `principal.asset.attribute.labels.key` UDM field is set to `Host_DnsDomain` and the `properties.AdditionalFields.Host.DnsDomain` log field is mapped to the `principal.asset.attribute.labels.value` UDM field and the `additional.fields.key` UDM field is set to `NTDomain` and the `properties.AdditionalFields.NTDomain` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.Host.EnrichmentType` | `additional.fields[Host_EnrichmentType]` |   
`User` | `properties.AdditionalFields.Host.HostMachineId,properties.AdditionalFields.Host.MachineId` | `principal.asset.product_object_id` | If the `properties.AdditionalFields.Host.MachineId` log field value is _not_ empty, then the `properties.AdditionalFields.Host.MachineId` log field is mapped to the `principal.asset.product_object_id` UDM field. If the `properties.AdditionalFields.Host.HostMachineId` log field value is _not_ empty, then the `principal.asset.attribute.labels.key` UDM field is set to `Host_HostMachineId` and the `properties.AdditionalFields.Host.HostMachineId` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
  
Otherwise, the `properties.AdditionalFields.Host.HostMachineId` log field is mapped to the `principal.asset.product_object_id` UDM field.  
`User` | `properties.AdditionalFields.Host.IpInterfaces.$id` | `additional.fields[Host_IpInterfaces_$id]` | Iterate through log field `properties.AdditionalFields.Host.IpInterfaces`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Host_IpInterfaces_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Host.IpInterfaces.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.Host.IpInterfaces.Address` | `principal.ip` | Iterate through log field `properties.AdditionalFields.Host.IpInterfaces`:  
  
The `valid_ipinterface_address` field is extracted from `properties.AdditionalFields.Host.IpInterfaces.Address` log field using the Grok pattern. The `valid_ipinterface_address` log field is mapped to the `principal.ip` UDM field.  
`User` | `properties.AdditionalFields.Host.IpInterfaces.Type` | `additional.fields[Host_IpInterfaces_Type]` | Iterate through log field `properties.AdditionalFields.Host.IpInterfaces`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Host_IpInterfaces_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Host.IpInterfaces.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.Host.IsDomainJoined` | `principal.asset.attribute.labels[Host_IsDomainJoined]` |   
`User` | `properties.AdditionalFields.Host.IsIoc` | `security_result.detection_fields[Host_IsIoc]` |   
`User` | `properties.AdditionalFields.Host.LastRemediationState` | `security_result.detection_fields[Host_LastRemediationState]` |   
`User` | `properties.AdditionalFields.Host.LastVerdict` | `security_result.detection_fields[Host_LastVerdict]` |   
`User` | `properties.AdditionalFields.Host.LeadingHost` | `principal.asset.attribute.labels[Host_LeadingHost]` |   
`User` | `properties.AdditionalFields.Host.MachineIdType` | `principal.asset.attribute.labels[Host_MachineIdType]` |   
`User` | `properties.AdditionalFields.Host.MergeByKey` | `additional.fields[Host_MergeByKey]` |   
`User` | `properties.AdditionalFields.Host.MergeByKeyHex` | `additional.fields[Host_MergeByKeyHex]` |   
`User` | `properties.AdditionalFields.Host.Metadata.MachineEnrichmentInfo` | `additional.fields[Host_Metadata_MachineEnrichmentInfo]` |   
`User` | `properties.AdditionalFields.Host.NetBiosName` | `principal.asset.attribute.labels[Host_NetBiosName]` |   
`User` | `properties.AdditionalFields.Host.OSFamily` | `principal.platform` | If the `properties.AdditionalFields.Host.OSFamily` log field value is equal to `Windows`, then the `principal.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.AdditionalFields.Host.OSFamily` log field value is equal to `Mac`, then the `principal.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.AdditionalFields.Host.OSFamily` log field value is equal to `Linux`, then the `principal.platform` UDM field is set to `LINUX`.  
`User` | `properties.AdditionalFields.Host.OSVersion` | `principal.platform_version` |   
`User` | `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[Host_RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`User` | `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[Host_RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Host_RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[Host_RbacScopes_ScopesPerType_Workloads_Mode]` |   
`User` | `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[Host_RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Host_RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Host.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.Host.RemediationProviders.RemediationDate` | `security_result.detection_fields[Host_RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.Host.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_RemediationProviders_RemediationDate` and the `properties.AdditionalFields.Host.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`User` | `properties.AdditionalFields.Host.RemediationProviders.RemediationState` | `security_result.detection_fields[Host_RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.Host.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_RemediationProviders_RemediationState` and the `properties.AdditionalFields.Host.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`User` | `properties.AdditionalFields.Host.RemediationProviders.Type` | `security_result.detection_fields[Host_RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.Host.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_RemediationProviders_Type` and the `properties.AdditionalFields.Host.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`User` | `properties.AdditionalFields.Host.Role` | `additional.fields[Host_Role]` |   
`User` | `properties.AdditionalFields.Host.SuspicionLevel` | `security_result.detection_fields[Host_SuspicionLevel]` |   
`User` | `properties.AdditionalFields.Host.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[Host_ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.Host.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.Host.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`User` | `properties.AdditionalFields.Host.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[Host_ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.Host.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `Host_ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.Host.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`User` | `properties.AdditionalFields.Host.Type` | `additional.fields[Host_Type]` |   
`User` | `properties.AdditionalFields.Id` | `additional.fields[id]` |   
`User` | `properties.AdditionalFields.IsDomainJoined` | `principal.user.attribute.labels[IsDomainJoined]` |   
`User` | `properties.AdditionalFields.IsIoc` | `security_result.detection_fields[IsIoc]` |   
`User` | `properties.AdditionalFields.IsValid` | `additional.fields[IsValid]` |   
`User` | `properties.AdditionalFields.LastRemediationState` | `security_result.detection_fields[LastRemediationState]` |   
`User` | `properties.AdditionalFields.LastVerdict` | `security_result.threat_verdict` | If the `properties.AdditionalFields.LastVerdict` log field value is equal to `Suspicious`, then the `security_result.threat_verdict` UDM field is set to `SUSPICIOUS`.  
  
Otherwise, if the `properties.AdditionalFields.LastVerdict` log field value is equal to `Malicious`, then the `security_result.threat_verdict` UDM field is set to `MALICIOUS`.  
`User` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`User` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`User` | `properties.AdditionalFields.Name` | `principal.user.userid` | If the `properties.AccountName` log field value is empty, then the `properties.AdditionalFields.Name` log field is mapped to the `principal.user.userid` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `Name` and the `properties.AdditionalFields.Name` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`User` | `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes` | `additional.fields[RbacScopes_ScopesPerType_AdminUnits_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_AdminUnits_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.RbacScopes.ScopesPerType.AppstanceId.Scopes` | `additional.fields[RbacScopes_ScopesPerType_AppstanceId_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.AppstanceId.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_AppstanceId_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.AppstanceId.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Mode` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Mode]` |   
`User` | `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` | `additional.fields[RbacScopes_ScopesPerType_MachineGroupIds_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_MachineGroupIds_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.MachineGroupIds.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.RbacScopes.ScopesPerType.RiskCategory.Scopes` | `additional.fields[RbacScopes_ScopesPerType_RiskCategory_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.RiskCategory.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_RiskCategory_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.RiskCategory.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.RbacScopes.ScopesPerType.UserGroupId.Scopes` | `additional.fields[RbacScopes_ScopesPerType_UserGroupId_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.UserGroupId.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_UserGroupId_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.UserGroupId.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Mode` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Mode]` |   
`User` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.ReferenceId` | `additional.fields[ReferenceId]` |   
`User` | `properties.AdditionalFields.RemediationProviders.RemediationDate` | `security_result.detection_fields[RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationDate` and the `properties.AdditionalFields.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`User` | `properties.AdditionalFields.RemediationProviders.RemediationState` | `security_result.detection_fields[RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationState` and the `properties.AdditionalFields.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`User` | `properties.AdditionalFields.RemediationProviders.Type` | `security_result.detection_fields[RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_Type` and the `properties.AdditionalFields.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`User` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`User` | `properties.AdditionalFields.Roles` | `additional.fields[Roles]` | Iterate through log field `properties.AdditionalFields.Roles`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Roles_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Roles` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`User` | `properties.AdditionalFields.Sid` | `additional.fields[Sid]` |   
`User` | `properties.AdditionalFields.SuspicionLevel` | `security_result.detection_fields[SuspicionLevel]` |   
`User` | `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`User` | `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`User` | `properties.AdditionalFields.Count of ThreatAnalysisSummary` | `security_result.detection_fields[Count_of_ThreatAnalysisSummary]` |   
`User` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`User` | `properties.AdditionalFields.UPNSuffix` | `additional.fields[UPNSuffix]` |   
`User` | `properties.AdditionalFields.Count of RemediationProviders` | `security_result.detection_fields[Count_of_RemediationProviders]` |   
`User` | `properties.AdditionalFields.EntityId` | `additional.fields[EntityId]` |   
`User` | `properties.AdditionalFields.InventoryIdentityId` | `additional.fields[InventoryIdentityId]` |   
`User` | `properties.AdditionalFields.UserPrincipalName` | `principal.user.email_addresses` |   
`MailMessage` | `properties.AdditionalFields.AdditionalActionsAndResults` | `security_result.detection_fields[AdditionalActionsAndResults]` | Iterate through log field `properties.AdditionalFields.AdditionalActionsAndResults`:  
  
The `security_result.detection_fields.key` UDM field is set to `AdditionalActionsAndResults` and the `properties.AdditionalFields.AdditionalActionsAndResults` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.AntispamDirection` | `security_result.detection_fields[AntispamDirection]` |   
`MailMessage` | `properties.AdditionalFields.Asset` | `principal.asset.attribute.labels[Asset]` |   
`MailMessage` | `properties.AdditionalFields.AttachmentCount` | `additional.fields[AttachmentCount]` |   
`MailMessage` | `properties.AdditionalFields.AuthDetails.Name` | `security_result.detection_fields[AuthDetails_Name]` | Iterate through log field `properties.AdditionalFields.AuthDetails`:  
  
The `security_result.detection_fields.key` UDM field is set to `AuthDetails_Name` and the `properties.AdditionalFields.AuthDetails.Name` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.AuthDetails.Value` | `security_result.detection_fields[AuthDetails_Value]` | Iterate through log field `properties.AdditionalFields.AuthDetails`:  
  
The `security_result.detection_fields.key` UDM field is set to `AuthDetails_Value` and the `properties.AdditionalFields.AuthDetails.Value` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.CampaignID` | `security_result.detection_fields[CampaignID]` |   
`MailMessage` | `properties.AdditionalFields.Connector` | `security_result.detection_fields[Connector]` |   
`MailMessage` | `properties.AdditionalFields.DeliveryAction` | `additional.fields[DeliveryAction]` |   
`MailMessage` | `properties.AdditionalFields.DeliveryLocation` | `additional.fields[DeliveryLocation]` |   
`MailMessage` | `properties.AdditionalFields.EndTimeUtc` | `security_result.detection_fields[EndTimeUtc]` |   
`MailMessage` | `properties.AdditionalFields.EntitySources` | `additional.fields[EntitySources]` | Iterate through log field `properties.AdditionalFields.EntitySources`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `EntitySources_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.EntitySources` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.$id` | `additional.fields[Files_$id]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.EntitySources` | `about.security_result.detection_fields[Files_EntitySources]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.EntitySources`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_EntitySources` and the `properties.AdditionalFields.Files.EntitySources` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.FileHashes.$id` | `additional.fields[Files_FileHashes_$id]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_FileHashes_$id_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.FileHashes.$id` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.FileHashes.Algorithm` | `additional.fields[Files_FileHashes_Algorithm]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_FileHashes_Algorithm_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.FileHashes.Type` | `additional.fields[Files_FileHashes_Type]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.FileHashes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_FileHashes_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.FileHashes.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.FileHashes.Value` | `about.file.sha1, about.file.sha256, about.file.md5` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.FileHashes`:  
  
If the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field value is equal to `SHA1` and the `about.file.sha1` UDM field is empty and the `properties.AdditionalFields.Files.FileHashes.Value` log field value matches the regular expression pattern `^[a-fA-F0-9]+$`, then the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `about.file.sha1` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field value is equal to `SHA256` and the `about.file.sha256` UDM field is empty and the `properties.AdditionalFields.Files.FileHashes.Value` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `about.file.sha256` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field value is equal to `MD5` and the `about.file.md5` UDM field is empty and the `properties.AdditionalFields.Files.FileHashes.Value` log field value matches the regular expression pattern `^[a-fA-F0-9]+$`, then the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `about.file.md5` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.Files.FileHashes.Value` log field is _not_ mapped to the `about.file.sha1`, `about.file.sha256`, or `about.file.md5` UDM fields, then:  
  
If the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field value is equal to `SHA256`, then the `about.security_result.detection_fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_%{index1}_SHA256_Value`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field value is equal to `SHA1`, then the `about.security_result.detection_fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_%{index1}_SHA1_Value`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.Files.FileHashes.Algorithm` log field value is equal to `MD5`, then the `about.security_result.detection_fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_%{index1}_MD5_Value`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
  
Otherwise, the `about.security_result.detection_fields.key` UDM field is set to a value generated from the template `Files_%{index}_FileHashes_%{index1}_Value`, where `%{index}` and `%{index1}` are replaced with the values of the `index` and `index1` log fields and the `properties.AdditionalFields.Files.FileHashes.Value` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.FirstSeen,properties.AdditionalFields.FirstSeen` | `about.file.first_seen_time` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `properties.AdditionalFields.Files.FirstSeen` log field is mapped to the `about.file.first_seen_time` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.LastRemediationState` | `about.security_result.detection_fields[Files_LastRemediationState]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_LastRemediationState` and the `properties.AdditionalFields.Files.LastRemediationState` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.LastVerdict` | `about.security_result.detection_fields[Files_LastVerdict]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_LastVerdict` and the `properties.AdditionalFields.Files.LastVerdict` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.MalwareFamily` | `about.security_result.detection_fields[Files_MalwareFamily]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_MalwareFamily` and the `properties.AdditionalFields.Files.MalwareFamily` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.MergeByKey` | `additional.fields[Files_MergeByKey]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_MergeByKey_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.MergeByKey` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.MergeByKeyHex` | `additional.fields[Files_MergeByKeyHex]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_MergeByKeyHex_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.MergeByKeyHex` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.Name` | `about.file.names` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `properties.AdditionalFields.Files.Name` log field is mapped to the `about.file.names` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.RemediationProviders.RemediationDate` | `about.security_result.detection_fields[Files_RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.RemediationProviders`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_RemediationProviders_RemediationDate` and the `properties.AdditionalFields.Files.RemediationProviders.RemediationDate` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.RemediationProviders.RemediationState` | `about.security_result.detection_fields[Files_RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.RemediationProviders`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_RemediationProviders_RemediationState` and the `properties.AdditionalFields.Files.RemediationProviders.RemediationState` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.RemediationProviders.Type` | `about.security_result.detection_fields[Files_RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.RemediationProviders`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_RemediationProviders_Type` and the `properties.AdditionalFields.Files.RemediationProviders.Type` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.Role` | `additional.fields[Files_Role]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_Role_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.Role` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.Source` | `about.security_result.detection_fields[Files_Source]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_Source` and the `properties.AdditionalFields.Files.Source` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.ThreatAnalysisSummary.AnalysisDate` | `about.security_result.detection_fields[Files_ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.ThreatAnalysisSummary`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.Files.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.ThreatAnalysisSummary.Verdict` | `about.security_result.detection_fields[Files_ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.ThreatAnalysisSummary`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.Files.ThreatAnalysisSummary.Verdict` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.ThreatIntelligence.ProviderName` | `about.security_result.detection_fields[Files_ThreatIntelligence_ProviderName]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.ThreatIntelligence`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_ThreatIntelligence_ProviderName` and the `properties.AdditionalFields.Files.ThreatIntelligence.ProviderName` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.ThreatIntelligence.ThreatName` | `about.security_result.threat_name` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.ThreatIntelligence`:  
  
The `properties.AdditionalFields.Files.ThreatIntelligence.ThreatName` log field is mapped to the `about.security_result.threat_name` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.ThreatIntelligence.ThreatType` | `about.security_result.detection_fields[Files_ThreatIntelligence_ThreatType]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
Iterate through log field `properties.AdditionalFields.Files.ThreatIntelligence`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_ThreatIntelligence_ThreatType` and the `properties.AdditionalFields.Files.ThreatIntelligence.ThreatType` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.Type` | `additional.fields[Files_Type]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `Files_Type_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.Files.Type` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Files.Urn` | `about.security_result.detection_fields[Files_Urn]` | Iterate through log field `properties.AdditionalFields.Files`:  
  
The `about.security_result.detection_fields.key` UDM field is set to `Files_Urn` and the `properties.AdditionalFields.Files.Urn` log field is mapped to the `about.security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.InternetMessageId` | `additional.fields[InternetMessageId]` |   
`MailMessage` | `properties.AdditionalFields.Language` | `additional.fields[Language]` |   
`MailMessage` | `properties.AdditionalFields.LastRemediationState` | `security_result.detection_fields[LastRemediationState]` |   
`MailMessage` | `properties.AdditionalFields.LastVerdict` | `security_result.threat_verdict` | If the `properties.AdditionalFields.LastVerdict` log field value is equal to `Suspicious`, then the `security_result.threat_verdict` UDM field is set to `SUSPICIOUS`.  
  
Otherwise, if the `properties.AdditionalFields.LastVerdict` log field value is equal to `Malicious`, then the `security_result.threat_verdict` UDM field is set to `MALICIOUS`.  
`MailMessage` | `properties.AdditionalFields.MergeByKey` | `additional.fields[MergeByKey]` |   
`MailMessage` | `properties.AdditionalFields.MergeByKeyHex` | `additional.fields[MergeByKeyHex]` |   
`MailMessage` | `properties.AdditionalFields.NetworkMessageId` | `network.email.mail_id` | If the `properties.NetworkMessageId` log field value is empty, then the `properties.AdditionalFields.NetworkMessageId` log field is mapped to the `network.email.mail_id` UDM field.  
`MailMessage` | `properties.AdditionalFields.OriginalDeliveryLocation` | `additional.fields[OriginalDeliveryLocation]` |   
`MailMessage` | `properties.AdditionalFields.Sender,properties.AdditionalFields.P1Sender,properties.AdditionalFields.P2Sender` | `network.email.from` | If the `properties.AdditionalFields.Sender` log field value is _not_ empty, then the `properties.AdditionalFields.Sender` log field is mapped to the `network.email.from` UDM field. If the `properties.AdditionalFields.P1Sender` log field value is _not_ empty, then the `additional.fields.key` UDM field is set to `P1Sender` and the `properties.AdditionalFields.P1Sender` log field is mapped to the `additional.fields.value.string_value` UDM field. If the `properties.AdditionalFields.P2Sender` log field value is _not_ empty, then the `additional.fields.key` UDM field is set to `P2Sender` and the `properties.AdditionalFields.P2Sender` log field is mapped to the `additional.fields.value.string_value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.P1Sender` log field value is _not_ empty, then the `properties.AdditionalFields.P1Sender` log field is mapped to the `network.email.from` UDM field. If the `properties.AdditionalFields.P2Sender` log field value is _not_ empty, then the `additional.fields.key` UDM field is set to `P2Sender` and the `properties.AdditionalFields.P2Sender` log field is mapped to the `additional.fields.value.string_value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.P2Sender` log field value is _not_ empty, then the `properties.AdditionalFields.P2Sender` log field is mapped to the `network.email.from` UDM field.  
`MailMessage` | `properties.AdditionalFields.P1SenderDomain, properties.AdditionalFields.P2SenderDomain` | `principal.administrative_domain` | If the `properties.AccountDomain` log field value is empty, then if the `properties.AdditionalFields.P1SenderDomain` log field value is _not_ empty, then the `properties.AdditionalFields.P1SenderDomain` log field is mapped to the `principal.administrative_domain` UDM field. If the `properties.AdditionalFields.P2SenderDomain` log field value is _not_ empty, then the `additional.fields.key` UDM field is set to `P2SenderDomain` and the `properties.AdditionalFields.P2SenderDomain` log field is mapped to the `additional.fields.value.string_value` UDM field. Otherwise, the `properties.AdditionalFields.P2SenderDomain` log field is mapped to the `principal.administrative_domain` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `P1SenderDomain` and the `properties.AdditionalFields.P1SenderDomain` log field is mapped to the `additional.fields.value.string_value` UDM field and the `additional.fields.key` UDM field is set to `P2SenderDomain` and the `properties.AdditionalFields.P2SenderDomain` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailMessage` | `properties.AdditionalFields.P2SenderDisplayName` | `principal.user.user_display_name` | If the `properties.AccountUpn` log field value is empty, then the `properties.AdditionalFields.P2SenderDisplayName` log field is mapped to the `principal.user.user_display_name` UDM field.  
`MailMessage` | `properties.AdditionalFields.PhishConfidenceLevel` | `security_result.detection_fields[PhishConfidenceLevel]` |   
`MailMessage` | `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes` | `additional.fields[RbacScopes_ScopesPerType_AdminUnits_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_AdminUnits_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.AdminUnits.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailMessage` | `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` | `additional.fields[RbacScopes_ScopesPerType_Workloads_Scopes]` | Iterate through log field `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `RbacScopes_ScopesPerType_Workloads_Scopes_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.RbacScopes.ScopesPerType.Workloads.Scopes` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`MailMessage` | `properties.AdditionalFields.ReceivedDate` | `additional.fields[ReceivedDate]` |   
`MailMessage` | `properties.AdditionalFields.Recipient` | `network.email.to` |   
`MailMessage` | `properties.AdditionalFields.RemediationProviders.RemediationDate` | `security_result.detection_fields[RemediationProviders_RemediationDate]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationDate` and the `properties.AdditionalFields.RemediationProviders.RemediationDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.RemediationProviders.RemediationState` | `security_result.detection_fields[RemediationProviders_RemediationState]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_RemediationState` and the `properties.AdditionalFields.RemediationProviders.RemediationState` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.RemediationProviders.Type` | `security_result.detection_fields[RemediationProviders_Type]` | Iterate through log field `properties.AdditionalFields.RemediationProviders`:  
  
The `security_result.detection_fields.key` UDM field is set to `RemediationProviders_Type` and the `properties.AdditionalFields.RemediationProviders.Type` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Role` | `additional.fields[Role]` |   
`MailMessage` | `properties.AdditionalFields.SenderIP` | `principal.ip` | The `valid_senderip` field is extracted from `properties.AdditionalFields.SenderIP` log field using the Grok pattern. The `valid_senderip` log field is mapped to the `principal.ip` UDM field.  
`MailMessage` | `properties.AdditionalFields.Source` | `additional.fields[Source]` |   
`MailMessage` | `properties.AdditionalFields.SourceEntityId` | `security_result.associations.id` |   
`MailMessage` | `properties.AdditionalFields.SourceEntityType` | `security_result.associations.type` | If the `properties.AdditionalFields.SourceEntityType` log field value is `Malware`, then the `security_result.associations.type` UDM field is set to `MALWARE`.  
  
Otherwise, the `security_result.associations.type` UDM field is set to `ASSOCIATION_TYPE_UNSPECIFIED`.  
`MailMessage` | `properties.AdditionalFields.SourceExtendedProperties` | `additional.fields[SourceExtendedProperties]` |   
`MailMessage` | `properties.AdditionalFields.SourceThreatName` | `security_result.threat_name` |   
`MailMessage` | `properties.AdditionalFields.SourceThreatType` | `security_result.detection_fields[SourceThreatType]` |   
`MailMessage` | `properties.AdditionalFields.StartTimeUtc` | `additional.fields[StartTimeUtc]` |   
`MailMessage` | `properties.AdditionalFields.Subject` | `network.email.subject` |   
`MailMessage` | `properties.AdditionalFields.SystemOverrides.Details` | `security_result.detection_fields[SystemOverrides_Details]` |   
`MailMessage` | `properties.AdditionalFields.SystemOverrides.FinalOverride` | `security_result.detection_fields[SystemOverrides_FinalOverride]` |   
`MailMessage` | `properties.AdditionalFields.SystemOverrides.Result` | `security_result.detection_fields[SystemOverrides_Result]` |   
`MailMessage` | `properties.AdditionalFields.SystemOverrides.Source` | `security_result.detection_fields[SystemOverrides_Source]` |   
`MailMessage` | `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` | `security_result.detection_fields[ThreatAnalysisSummary_AnalysisDate]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_AnalysisDate` and the `properties.AdditionalFields.ThreatAnalysisSummary.AnalysisDate` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` | `security_result.detection_fields[ThreatAnalysisSummary_Verdict]` | Iterate through log field `properties.AdditionalFields.ThreatAnalysisSummary`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatAnalysisSummary_Verdict` and the `properties.AdditionalFields.ThreatAnalysisSummary.Verdict` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Count of ThreatAnalysisSummary` | `security_result.detection_fields[Count_of_ThreatAnalysisSummary]` |   
`MailMessage` | `properties.AdditionalFields.ThreatDetectionMethods` | `security_result.detection_fields[ThreatDetectionMethods]` | Iterate through log field `properties.AdditionalFields.ThreatDetectionMethods`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatDetectionMethods` and the `properties.AdditionalFields.ThreatDetectionMethods` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.ThreatIntelligence.ProviderName` | `security_result.detection_fields[ThreatIntelligence_ProviderName]` | Iterate through log field `properties.AdditionalFields.ThreatIntelligence`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatIntelligence_ProviderName` and the `properties.AdditionalFields.ThreatIntelligence.ProviderName` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.ThreatIntelligence.ThreatName` | `security_result.threat_name` | Iterate through log field `properties.AdditionalFields.ThreatIntelligence`:  
  
The `properties.AdditionalFields.ThreatIntelligence.ThreatName` log field is mapped to the `security_result.threat_name` UDM field.  
`MailMessage` | `properties.AdditionalFields.ThreatIntelligence.ThreatType` | `security_result.detection_fields[ThreatIntelligence_ThreatType]` | Iterate through log field `properties.AdditionalFields.ThreatIntelligence`:  
  
The `security_result.detection_fields.key` UDM field is set to `ThreatIntelligence_ThreatType` and the `properties.AdditionalFields.ThreatIntelligence.ThreatType` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Threats` | `security_result.detection_fields[Threats]` | Iterate through log field `properties.AdditionalFields.Threats`:  
  
The `security_result.detection_fields.key` UDM field is set to `Threats` and the `properties.AdditionalFields.Threats` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.Type` | `additional.fields[Type]` |   
`MailMessage` | `properties.AdditionalFields.UrlCount` | `additional.fields[UrlCount]` |   
`MailMessage` | `properties.AdditionalFields.Urls` | `security_result.detection_fields[Urls]` | Iterate through log field `properties.AdditionalFields.Urls`:  
  
The `security_result.detection_fields.key` UDM field is set to `Urls` and the `properties.AdditionalFields.Urls` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`MailMessage` | `properties.AdditionalFields.EntityId` | `additional.fields[EntityId]` |   
`MailMessage` | `properties.AdditionalFields.UId` | `additional.fields[UId]` |   
`MailMessage` | `properties.AdditionalFields.Urn` | `additional.fields[Urn]` |   
  
### AdditionalFields mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceEvents

The following table lists the `AdditionalFields` log fields for the `DeviceEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.AdditionalFields.Sha1CatalogHash` | `about.file.sha1` | If the `properties.AdditionalFields.Sha1CatalogHash` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.AdditionalFields.Sha1CatalogHash` log field is mapped to the `about.file.sha1` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `Sha1CatalogHash` and the `properties.AdditionalFields.Sha1CatalogHash` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.Sha256CatalogHash` | `about.file.sha256` | If the `properties.AdditionalFields.Sha256CatalogHash` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.AdditionalFields.Sha256CatalogHash` log field is mapped to the `about.file.sha256` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `Sha256CatalogHash` and the `properties.AdditionalFields.Sha256CatalogHash` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.ClientMachine` | `about.hostname` |   
`properties.AdditionalFields.Command` | `target.process.command_line` | If the `properties.ActionType` log field value is equal to `PowerShellCommand`, then the `properties.AdditionalFields.Command` log field is mapped to the `target.process.command_line` UDM field.  
`properties.AdditionalFields.ProcessName` | `target.process.file.full_path` | If the `properties.ActionType` log field value contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

then if the `properties.FolderPath` log field value is empty, then the `properties.AdditionalFields.ProcessName` log field is mapped to the `target.process.file.full_path` UDM field. Otherwise, the `additional.fields.key` UDM field is set to `ProcessName` and the `properties.AdditionalFields.ProcessName` log field is mapped to the `additional.fields.value.string_value` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `ProcessName` and the `properties.AdditionalFields.ProcessName` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.OriginalFileName` | `target.file.exif_info.original_file` |   
`properties.AdditionalFields.Sha1FlatHash` | `about.file.sha1` |   
`properties.AdditionalFields.Sha256FlatHash` | `about.file.sha256` |   
`properties.AdditionalFields.Accepted` | `additional.fields[Accepted]` |   
`properties.AdditionalFields.ActivityId` | `additional.fields[ActivityId]` |   
`properties.AdditionalFields.AppPackageFamilyName` | `additional.fields[AppPackageFamilyName]` |   
`properties.AdditionalFields.AssemblyId` | `additional.fields[AssemblyId]` |   
`properties.AdditionalFields.AttributeList` | `additional.fields[AttributeList]` | Iterate through log field `properties.AdditionalFields.AttributeList`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `AttributeList_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.AttributeList` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.AuditEnabled` | `additional.fields[AuditEnabled]` |   
`properties.AdditionalFields.AuditPolicyChanges` | `additional.fields[AuditPolicyChanges]` |   
`properties.AdditionalFields.BackgroundCallCount` | `additional.fields[BackgroundCallCount]` |   
`properties.AdditionalFields.BaseAddress` | `additional.fields[BaseAddress]` |   
`properties.AdditionalFields.BluetoothMacAddress` | `additional.fields[BluetoothMacAddress]` |   
`properties.AdditionalFields.BuildId` | `additional.fields[BuildId]` |   
`properties.AdditionalFields.BusType` | `additional.fields[BusType]` |   
`properties.AdditionalFields.CategoryId` | `additional.fields[CategoryId]` |   
`properties.AdditionalFields.ChildCommandLine` | `target.process.command_line` | If the `properties.ProcessCommandLine` log field value is empty, then the `properties.AdditionalFields.ChildCommandLine` log field is mapped to the `target.process.command_line` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `ChildCommandLine` and the `properties.AdditionalFields.ChildCommandLine` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.ClassGuid` | `additional.fields[ClassGuid]` |   
`properties.AdditionalFields.ClassId` | `additional.fields[ClassId]` |   
`properties.AdditionalFields.ClassName` | `additional.fields[ClassName]` |   
`properties.AdditionalFields.Consumer` | `additional.fields[Consumer]` |   
`properties.AdditionalFields.Container` | `additional.fields[Container]` |   
`properties.AdditionalFields.ContainerReason` | `additional.fields[ContainerReason]` |   
`properties.AdditionalFields.CurrentTokenPointer` | `additional.fields[CurrentTokenPointer]` |   
`properties.AdditionalFields.DefenderTrust` | `additional.fields[DefenderTrust]` |   
`properties.AdditionalFields.DesiredAccess` | `additional.fields[DesiredAccess]` |   
`properties.AdditionalFields.DeviceDescription` | `additional.fields[DeviceDescription]` |   
`properties.AdditionalFields.DeviceId` | `principal.asset.product_object_id` |   
`properties.AdditionalFields.DeviceInstanceId` | `additional.fields[DeviceInstanceId]` |   
`properties.AdditionalFields.DeviceUpdated` | `additional.fields[DeviceUpdated]` |   
`properties.AdditionalFields.DistinguishedName` | `additional.fields[DistinguishedName]` |   
`properties.AdditionalFields.Domain` | `additional.fields[Domain]` |   
`properties.AdditionalFields.DriveLetter` | `additional.fields[DriveLetter]` |   
`properties.AdditionalFields.DriverDate` | `additional.fields[DriverDate]` |   
`properties.AdditionalFields.DriverInbox` | `additional.fields[DriverInbox]` |   
`properties.AdditionalFields.DriverName` | `additional.fields[DriverName]` |   
`properties.AdditionalFields.DriverProvider` | `additional.fields[DriverProvider]` |   
`properties.AdditionalFields.DriverSection` | `additional.fields[DriverSection]` |   
`properties.AdditionalFields.DriverVersion` | `additional.fields[DriverVersion]` |   
`properties.AdditionalFields.DSName` | `additional.fields[DSName]` |   
`properties.AdditionalFields.Ess` | `additional.fields[Ess]` |   
`properties.AdditionalFields.EtwActivityId` | `additional.fields[EtwActivityId]` |   
`properties.AdditionalFields.Experience` | `additional.fields[Experience]` |   
`properties.AdditionalFields.FileDescription` | `target.file.exif_info.file_description` |   
`properties.AdditionalFields.FileVersion` | `additional.fields[FileVersion]` |   
`properties.AdditionalFields.Flags` | `additional.fields[Flags]` |   
`properties.AdditionalFields.Fqbn` | `additional.fields[Fqbn]` |   
`properties.AdditionalFields.Hash` | `additional.fields[Hash]` |   
`properties.AdditionalFields.ImageBase` | `additional.fields[ImageBase]` |   
`properties.AdditionalFields.InfoAsJson` | `additional.fields[InfoAsJson]` |   
`properties.AdditionalFields.InitiatingProcess.IntegrityLevel` | `additional.fields[InitiatingProcess_IntegrityLevel]` |   
`properties.AdditionalFields.InitiatingProcess.TokenElevationType` | `additional.fields[InitiatingProcess_TokenElevationType]` |   
`properties.AdditionalFields.IntegrityLevel` | `additional.fields[IntegrityLevel]` |   
`properties.AdditionalFields.InternalName` | `additional.fields[InternalName]` |   
`properties.AdditionalFields.IsAudit` | `additional.fields[IsAudit]` |   
`properties.AdditionalFields.IsExistingConnection` | `additional.fields[IsExistingConnection]` |   
`properties.AdditionalFields.IsOnRemovableMedia` | `additional.fields[IsOnRemovableMedia]` |   
`properties.AdditionalFields.IsRemoteMachine` | `additional.fields[IsRemoteMachine]` |   
`properties.AdditionalFields.IssuerName` | `additional.fields[IssuerName]` |   
`properties.AdditionalFields.IssuerTBSHash` | `additional.fields[IssuerTBSHash]` |   
`properties.AdditionalFields.LoggedOnUsers` | `additional.fields[LoggedOnUsers]` | Iterate through log field `properties.AdditionalFields.LoggedOnUsers`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `LoggedOnUsers_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.LoggedOnUsers` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.ManagedInstallerEnabled` | `additional.fields[ManagedInstallerEnabled]` |   
`properties.AdditionalFields.Manufacturer` | `additional.fields[Manufacturer]` |   
`properties.AdditionalFields.MarkOfTheWeb` | `additional.fields[MarkOfTheWeb]` |   
`properties.AdditionalFields.MasterKeyGUID` | `additional.fields[MasterKeyGUID]` |   
`properties.AdditionalFields.MatchingDeviceId` | `additional.fields[MatchingDeviceId]` |   
`properties.AdditionalFields.ModuleId` | `additional.fields[ModuleId]` |   
`properties.AdditionalFields.ModuleILPathOrName` | `target.file.full_path` | If the `properties.ActionType` log field value is equal to `ClrUnbackedModuleLoaded`, then the `properties.AdditionalFields.ModuleILPathOrName` log field is mapped to the `target.file.full_path` UDM field.  
`properties.AdditionalFields.Name` | `additional.fields[Name]` |   
`properties.AdditionalFields.NotValidAfter` | `additional.fields[NotValidAfter]` |   
`properties.AdditionalFields.NotValidBefore` | `additional.fields[NotValidBefore]` |   
`properties.AdditionalFields.ObjectClass` | `additional.fields[ObjectClass]` |   
`properties.AdditionalFields.ObjectDN` | `additional.fields[ObjectDN]` |   
`properties.AdditionalFields.OperationDetails` | `additional.fields[OperationDetails]` |   
`properties.AdditionalFields.OperationType` | `additional.fields[OperationType]` |   
`properties.AdditionalFields.OriginalTokenPointer` | `additional.fields[OriginalTokenPointer]` |   
`properties.AdditionalFields.OutrankedDrivers` | `additional.fields[OutrankedDrivers]` |   
`properties.AdditionalFields.ParentDeviceInstanceId` | `additional.fields[ParentDeviceInstanceId]` |   
`properties.AdditionalFields.PassesManagedInstaller` | `additional.fields[PassesManagedInstaller]` |   
`properties.AdditionalFields.PassesSmartlocker` | `additional.fields[PassesSmartlocker]` |   
`properties.AdditionalFields.PipeName` | `target.file.full_path` | If the `properties.ActionType` log field value is equal to `NamedPipeEvent`, then the `properties.AdditionalFields.PipeName` log field is mapped to the `target.file.full_path` UDM field.  
`properties.AdditionalFields.PlistProperty` | `additional.fields[PlistProperty]` |   
`properties.AdditionalFields.PolicyBits` | `additional.fields[PolicyBits]` |   
`properties.AdditionalFields.PossibleCause` | `additional.fields[PossibleCause]` |   
`properties.AdditionalFields.PreviousValue` | `additional.fields[PreviousValue]` |   
`properties.AdditionalFields.ProductName` | `additional.fields[ProductName]` |   
`properties.AdditionalFields.ProductRevision` | `additional.fields[ProductRevision]` |   
`properties.AdditionalFields.Profiles` | `additional.fields[Profiles]` |   
`properties.AdditionalFields.ProtectionFlags` | `additional.fields[ProtectionFlags]` |   
`properties.AdditionalFields.ProtectionMask` | `additional.fields[ProtectionMask]` |   
`properties.AdditionalFields.PublisherName` | `additional.fields[PublisherName]` |   
`properties.AdditionalFields.PublisherTBSHash` | `additional.fields[PublisherTBSHash]` |   
`properties.AdditionalFields.RegionSize` | `additional.fields[RegionSize]` |   
`properties.AdditionalFields.RemoteClientsAccess` | `additional.fields[RemoteClientsAccess]` |   
`properties.AdditionalFields.Requested Signing Level` | `additional.fields[Requested Signing Level]` |   
`properties.AdditionalFields.ResponseCategory` | `security_result.detection_fields[ResponseCategory]` |   
`properties.AdditionalFields.ReturnValue` | `security_result.detection_fields[ReturnValue]` |   
`properties.AdditionalFields.SafeLinksMessageId` | `additional.fields[SafeLinksMessageId]` |   
`properties.AdditionalFields.ScopeOfSearch` | `additional.fields[ScopeOfSearch]` |   
`properties.AdditionalFields.SearchFilter` | `additional.fields[SearchFilter]` |   
`properties.AdditionalFields.SerialNumber` | `additional.fields[SerialNumber]` |   
`properties.AdditionalFields.ServiceAccount` | `additional.fields[ServiceAccount]` |   
`properties.AdditionalFields.ServiceStartType` | `additional.fields[ServiceStartType]` |   
`properties.AdditionalFields.ServiceType` | `additional.fields[ServiceType]` |   
`properties.AdditionalFields.ShareName` | `additional.fields[ShareName]` |   
`properties.AdditionalFields.ShellLinkCommandLine` | `target.process.command_line` |   
`properties.AdditionalFields.ShellLinkRunAsAdmin` | `additional.fields[ShellLinkRunAsAdmin]` |   
`properties.AdditionalFields.ShellLinkShowCommand` | `additional.fields[ShellLinkShowCommand]` |   
`properties.AdditionalFields.ShellLinkWorkingDirectory` | `additional.fields[ShellLinkWorkingDirectory]` |   
`properties.AdditionalFields.Signature` | `additional.fields[Signature]` |   
`properties.AdditionalFields.SignatureType` | `additional.fields[SignatureType]` |   
`properties.AdditionalFields.SiSigningScenario` | `additional.fields[SiSigningScenario]` |   
`properties.AdditionalFields.SmartlockerEnabled` | `additional.fields[SmartlockerEnabled]` |   
`properties.AdditionalFields.State` | `additional.fields[State]` |   
`properties.AdditionalFields.Status` | `security_result.detection_fields[Status]` |   
`properties.AdditionalFields.StatusCode` | `security_result.detection_fields[StatusCode]` |   
`properties.AdditionalFields.SubcategoryGuid` | `additional.fields[SubcategoryGuid]` |   
`properties.AdditionalFields.SubcategoryId` | `additional.fields[SubcategoryId]` |   
`properties.AdditionalFields.TamperingAttemptedValue` | `additional.fields[TamperingAttemptedValue]` |   
`properties.AdditionalFields.Target` | `additional.fields[Target]` |   
`properties.AdditionalFields.ThreadId` | `additional.fields[ThreadId]` |   
`properties.AdditionalFields.Timestamp` | `additional.fields[Timestamp]` |   
`properties.AdditionalFields.TokenModificationProperties` | `additional.fields[TokenModificationProperties]` | The `properties.AdditionalFields.TokenModificationProperties` log field is set to a value generated from the template `{"properties.AdditionalFields.TokenModificationProperties":%{properties.AdditionalFields.TokenModificationProperties}}`, where `%{properties.AdditionalFields.TokenModificationProperties}` is replaced with the value of the `properties.AdditionalFields.TokenModificationProperties` log field. The `properties.AdditionalFields.TokenModificationProperties` log field is parsed as JSON.  
  
Iterate for each key, value pair of log field `properties.AdditionalFields.TokenModificationProperties`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `TokenModificationProperties_%{key}`, where `%{key}` is replaced with the value of the `key` log field and the `value of properties.AdditionalFields.TokenModificationProperties` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.TotalBytesCopied` | `additional.fields[TotalBytesCopied]` |   
`properties.AdditionalFields.TotalSignatureCount` | `additional.fields[TotalSignatureCount]` |   
`properties.AdditionalFields.User` | `about.user.user_display_name` |   
`properties.AdditionalFields.UserOverrideKey` | `about.user.attribute.labels[UserOverrideKey]` |   
`properties.AdditionalFields.UserWriteable` | `about.user.attribute.labels[UserWriteable]` |   
`properties.AdditionalFields.USN` | `additional.fields[USN]` |   
`properties.AdditionalFields.Validated Signing Level` | `additional.fields[Validated Signing Level]` |   
`properties.AdditionalFields.ValidatedSigningLevel` | `additional.fields[ValidatedSigningLevel]` |   
`properties.AdditionalFields.Value` | `additional.fields[Value]` |   
`properties.AdditionalFields.VendorIds` | `additional.fields[VendorIds]` | Iterate through log field `properties.AdditionalFields.VendorIds`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `VendorIds_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.VendorIds` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.VerificationError` | `additional.fields[VerificationError]` |   
`properties.AdditionalFields.VerificationResult` | `additional.fields[VerificationResult]` |   
`properties.AdditionalFields.Volume` | `additional.fields[Volume]` |   
`properties.AdditionalFields.WasExecutingWhileDetected` | `security_result.detection_fields[WasExecutingWhileDetected]` |   
`properties.AdditionalFields.direction` | `network.direction` | If the `properties.AdditionalFields.direction` log field value is equal to `In`, then the `network.direction` UDM field is set to `INBOUND`.  
  
Otherwise, if the `properties.AdditionalFields.direction` log field value is equal to `Out`, then the `network.direction` UDM field is set to `OUTBOUND`.  
`properties.AdditionalFields.DnsQueryResult.Result` | `network.dns.answers.data` | Iterate through log field `properties.AdditionalFields.DnsQueryResult`:  
  
The `properties.AdditionalFields.DnsQueryResult.Result` log field value is mapped to the `network.dns.answers.data` UDM field.  
`properties.AdditionalFields.DnsQueryResult.DnsQueryType` | `network.dns.answers.type` | Iterate through log field `properties.AdditionalFields.DnsQueryResult`:  
  
If the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `A`, then the `network.dns.answers.type` UDM field is set to `1`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `NS`, then the `network.dns.answers.type` UDM field is set to `2`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `MD`, then the `network.dns.answers.type` UDM field is set to `3`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `MF`, then the `network.dns.answers.type` UDM field is set to `4`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `CNAME`, then the `network.dns.answers.type` UDM field is set to `5`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `SOA`, then the `network.dns.answers.type` UDM field is set to `6`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `MB`, then the `network.dns.answers.type` UDM field is set to `7`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `MG`, then the `network.dns.answers.type` UDM field is set to `8`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `MR`, then the `network.dns.answers.type` UDM field is set to `9`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `NULL`, then the `network.dns.answers.type` UDM field is set to `10`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `WKS`, then the `network.dns.answers.type` UDM field is set to `11`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `PTR`, then the `network.dns.answers.type` UDM field is set to `12`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `HINFO`, then the `network.dns.answers.type` UDM field is set to `13`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `MINFO`, then the `network.dns.answers.type` UDM field is set to `14`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `MX`, then the `network.dns.answers.type` UDM field is set to `15`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `TXT`, then the `network.dns.answers.type` UDM field is set to `16`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `RP`, then the `network.dns.answers.type` UDM field is set to `17`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `AFSDB`, then the `network.dns.answers.type` UDM field is set to `18`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `X25`, then the `network.dns.answers.type` UDM field is set to `19`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `ISDN`, then the `network.dns.answers.type` UDM field is set to `20`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `RT`, then the `network.dns.answers.type` UDM field is set to `21`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `NSAP`, then the `network.dns.answers.type` UDM field is set to `22`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `NSAP-PTR`, then the `network.dns.answers.type` UDM field is set to `23`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `SIG`, then the `network.dns.answers.type` UDM field is set to `24`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `KEY`, then the `network.dns.answers.type` UDM field is set to `25`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `PX`, then the `network.dns.answers.type` UDM field is set to `26`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `GPOS`, then the `network.dns.answers.type` UDM field is set to `27`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `AAAA`, then the `network.dns.answers.type` UDM field is set to `28`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `LOC`, then the `network.dns.answers.type` UDM field is set to `29`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `NXT`, then the `network.dns.answers.type` UDM field is set to `30`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `EID`, then the `network.dns.answers.type` UDM field is set to `31`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `NIMLOC`, then the `network.dns.answers.type` UDM field is set to `32`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `SRV`, then the `network.dns.answers.type` UDM field is set to `33`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `ATMA`, then the `network.dns.answers.type` UDM field is set to `34`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `NAPTR`, then the `network.dns.answers.type` UDM field is set to `35`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `KX`, then the `network.dns.answers.type` UDM field is set to `36`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `CERT`, then the `network.dns.answers.type` UDM field is set to `37`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `A6`, then the `network.dns.answers.type` UDM field is set to `38`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `DNAME`, then the `network.dns.answers.type` UDM field is set to `39`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `SINK`, then the `network.dns.answers.type` UDM field is set to `40`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `OPT`, then the `network.dns.answers.type` UDM field is set to `41`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `APL`, then the `network.dns.answers.type` UDM field is set to `42`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `DS`, then the `network.dns.answers.type` UDM field is set to `43`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `SSHFP`, then the `network.dns.answers.type` UDM field is set to `44`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `IPSECKEY`, then the `network.dns.answers.type` UDM field is set to `45`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `RRSIG`, then the `network.dns.answers.type` UDM field is set to `46`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `NSEC`, then the `network.dns.answers.type` UDM field is set to `47`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `DNSKEY`, then the `network.dns.answers.type` UDM field is set to `48`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `DHCID`, then the `network.dns.answers.type` UDM field is set to `49`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `NSEC3`, then the `network.dns.answers.type` UDM field is set to `50`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `NSEC3PARAM`, then the `network.dns.answers.type` UDM field is set to `51`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `TLSA`, then the `network.dns.answers.type` UDM field is set to `52`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `SMIMEA`, then the `network.dns.answers.type` UDM field is set to `53`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `UNASSIGNED`, then the `network.dns.answers.type` UDM field is set to `54`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `HIP`, then the `network.dns.answers.type` UDM field is set to `55`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `NINFO`, then the `network.dns.answers.type` UDM field is set to `56`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `RKEY`, then the `network.dns.answers.type` UDM field is set to `57`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `TALINK`, then the `network.dns.answers.type` UDM field is set to `58`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `CDS`, then the `network.dns.answers.type` UDM field is set to `59`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `CDNSKEY`, then the `network.dns.answers.type` UDM field is set to `60`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `OPENPGPKEY`, then the `network.dns.answers.type` UDM field is set to `61`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `CSYNC`, then the `network.dns.answers.type` UDM field is set to `62`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `ZONEMD`, then the `network.dns.answers.type` UDM field is set to `63`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `SVCB`, then the `network.dns.answers.type` UDM field is set to `64`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `HTTPS`, then the `network.dns.answers.type` UDM field is set to `65`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `SPF`, then the `network.dns.answers.type` UDM field is set to `99`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `UINFO`, then the `network.dns.answers.type` UDM field is set to `100`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `UID`, then the `network.dns.answers.type` UDM field is set to `101`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `GID`, then the `network.dns.answers.type` UDM field is set to `102`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `UNSPEC`, then the `network.dns.answers.type` UDM field is set to `103`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `NID`, then the `network.dns.answers.type` UDM field is set to `104`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `L32`, then the `network.dns.answers.type` UDM field is set to `105`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `L64`, then the `network.dns.answers.type` UDM field is set to `106`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `LP`, then the `network.dns.answers.type` UDM field is set to `107`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `EUI48`, then the `network.dns.answers.type` UDM field is set to `108`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `EUI64`, then the `network.dns.answers.type` UDM field is set to `109`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `TKEY`, then the `network.dns.answers.type` UDM field is set to `249`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `TSIG`, then the `network.dns.answers.type` UDM field is set to `250`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `IXFR`, then the `network.dns.answers.type` UDM field is set to `251`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `AXFR`, then the `network.dns.answers.type` UDM field is set to `252`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `MAILB`, then the `network.dns.answers.type` UDM field is set to `253`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `MAILA`, then the `network.dns.answers.type` UDM field is set to `254`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `ALL`, then the `network.dns.answers.type` UDM field is set to `255`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `URI`, then the `network.dns.answers.type` UDM field is set to `256`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `CAA`, then the `network.dns.answers.type` UDM field is set to `257`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `AVC`, then the `network.dns.answers.type` UDM field is set to `258`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `DOA`, then the `network.dns.answers.type` UDM field is set to `259`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `AMTRELAY`, then the `network.dns.answers.type` UDM field is set to `260`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `TA`, then the `network.dns.answers.type` UDM field is set to `32768`.  
  
Otherwise, if the `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is equal to `DLV`, then the `network.dns.answers.type` UDM field is set to `32769`.  
`properties.AdditionalFields.DnsQueryResult.DnsQueryType` | `additional.fields[DnsQueryType]` | Iterate through log field `properties.AdditionalFields.DnsQueryResult`:  
  
The `DnsQueryType_%{index}` value is mapped to the `additional.fields.key` UDM field.  
  
The `properties.AdditionalFields.DnsQueryResult.DnsQueryType` log field value is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.DnsQueryString` | `target.hostname` | If the `properties.DeviceName` log field value is empty and the `properties.RemoteDeviceName` log field value is empty, then the `properties.AdditionalFields.DnsQueryString` log field is mapped to the `target.hostname` UDM field.  
`properties.AdditionalFields.Protocol, properties.AdditionalFields.ProtocolName` | `network.ip_protocol` | If the `properties.Protocol` log field value is empty, then if the `properties.AdditionalFields.Protocol` log field value is _not_ empty, then if the `properties.AdditionalFields.Protocol` log field value matches the regular expression pattern `/(?i)TCP/`, then the `network.ip_protocol` UDM field is set to `TCP`.  
  
Otherwise, if the `properties.AdditionalFields.Protocol` log field value matches the regular expression pattern `/(?i)UDP/`, then the `network.ip_protocol` UDM field is set to `UDP`. The `additional.fields.key` UDM field is set to `ProtocolName` and the `properties.AdditionalFields.ProtocolName` log field is mapped to the `additional.fields.value.string_value` UDM field. Otherwise, if the `properties.AdditionalFields.ProtocolName` log field value matches the regular expression pattern `/(?i)TCP/`, then the `network.ip_protocol` UDM field is set to `TCP`.  
  
Otherwise, if the `properties.AdditionalFields.ProtocolName` log field value matches the regular expression pattern `/(?i)UDP/`, then the `network.ip_protocol` UDM field is set to `UDP`.  
  
Otherwise, the `additional.fields.key` UDM field is set to `Protocol` and the `properties.AdditionalFields.Protocol` log field is mapped to the `additional.fields.value.string_value` UDM field and the `additional.fields.key` UDM field is set to `ProtocolName` and the `properties.AdditionalFields.ProtocolName` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.ClientProcessName` | `principal.process.file.names` | If the `properties.ActionType` log field value contains one of the following values:

  * `DnsQueryResponse`
  * `DnsQueryRequest`

then the `properties.AdditionalFields.ClientProcessName` log field is mapped to the `principal.process.file.names` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `ClientProcessName` and the `properties.AdditionalFields.ClientProcessName` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.ClientProcessId` | `principal.process.pid` | If the `properties.ActionType` log field value contains one of the following values:

  * `DnsQueryResponse`
  * `DnsQueryRequest`

then the `properties.AdditionalFields.ClientProcessId` log field is mapped to the `principal.process.pid` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `ClientProcessId` and the `properties.AdditionalFields.ClientProcessId` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.InitiatingProcessFolderPath, properties.InitiatingProcessFileName` | `intermediary.process.file.full_path` | If the `properties.InitiatingProcessFolderPath` log field value is _not_ empty and the `properties.InitiatingProcessFileName` log field value is _not_ empty, then if the `properties.ActionType` log field value contains one of the following values:

  * `DnsQueryResponse`
  * `DnsQueryRequest`

then if the `properties.InitiatingProcessFolderPath` log field value matches the regular expression pattern the `properties.InitiatingProcessFileName` log field value, then the `properties.InitiatingProcessFolderPath` log field is mapped to the `intermediary.process.file.full_path` UDM field. Otherwise, the `intermediary.process.file.full_path` UDM field is set to a value generated from the template `%{properties.InitiatingProcessFolderPath}\%{properties.InitiatingProcessFileName}`, where `%{properties.InitiatingProcessFolderPath}` and `%{properties.InitiatingProcessFileName}` are replaced with the values of the `properties.InitiatingProcessFolderPath` and `properties.InitiatingProcessFileName` log fields. Otherwise, if the `properties.InitiatingProcessFolderPath` log field value matches the regular expression pattern the `properties.InitiatingProcessFileName` log field value, then the `properties.InitiatingProcessFolderPath` log field is mapped to the `principal.process.file.full_path` UDM field. Otherwise, the `principal.process.file.full_path` UDM field is set to a value generated from the template `%{properties.InitiatingProcessFolderPath}\%{properties.InitiatingProcessFileName}`, where `%{properties.InitiatingProcessFolderPath}` and `%{properties.InitiatingProcessFileName}` are replaced with the values of the `properties.InitiatingProcessFolderPath` and `properties.InitiatingProcessFileName` log fields.  
`properties.AdditionalFields.Action` | `security_result.action_details` |   
`properties.AdditionalFields.TamperingAction` | `security_result.action_details` |   
`properties.AdditionalFields.Description` | `security_result.description` |   
`properties.AdditionalFields.ErrorDescription` | `security_result.description` |   
`properties.AdditionalFields.FriendlyName` | `target.hostname` | If the `properties.RemoteUrl` log field value is empty and the `properties.RemoteDeviceName` log field value is empty and the `properties.DeviceName` log field value is empty and the `properties.AdditionalFields.DnsQueryString` log field value is empty, then the `properties.AdditionalFields.FriendlyName` log field is mapped to the `target.hostname` UDM field.  
`properties.AdditionalFields.Allow` | `security_result.detection_fields[Allow]` |   
`properties.AdditionalFields.DetectionGuid` | `security_result.rule_id` |   
`properties.AdditionalFields.ErrorCode` | `security_result.detection_fields[ErrorCode]` |   
`properties.AdditionalFields.IsConcrete` | `security_result.detection_fields[IsConcrete]` |   
`properties.AdditionalFields.IsPassiveMode` | `security_result.detection_fields[IsPassiveMode]` |   
`properties.AdditionalFields.ReportSource` | `security_result.detection_fields[ReportSource]` |   
`properties.AdditionalFields.ResourceSchema` | `security_result.detection_fields[ResourceSchema]` |   
`properties.AdditionalFields.ScanId` | `security_result.detection_fields[ScanId]` |   
`properties.AdditionalFields.ScanParametersIndex` | `security_result.detection_fields[ScanParametersIndex]` |   
`properties.AdditionalFields.ScanTypeIndex` | `security_result.detection_fields[ScanTypeIndex]` |   
`properties.AdditionalFields.Service` | `security_result.detection_fields[Service]` |   
`properties.AdditionalFields.SignatureName` | `security_result.rule_name` |   
`properties.AdditionalFields.WasRemediated` | `security_result.detection_fields[WasRemediated]` |   
`properties.AdditionalFields.PolicyID` | `security_result.rule_id` |   
`properties.AdditionalFields.RuleId` | `security_result.rule_id` |   
`properties.AdditionalFields.PolicyGuid` | `security_result.rule_labels[PolicyGuid]` |   
`properties.AdditionalFields.PolicyHash` | `security_result.rule_labels[PolicyHash]` |   
`properties.AdditionalFields.PolicyName` | `security_result.rule_name` |   
`properties.AdditionalFields.ThreatName` | `security_result.threat_name` |   
`properties.AdditionalFields.PackageFamilyName` | `target.application` |   
`properties.AdditionalFields.ServiceName` | `target.resource.name` |   
`properties.AdditionalFields.SafeLinksRecipient` | `network.email.to` |   
`properties.AdditionalFields.AuthenticodeHash` | `target.file.authentihash` |   
`properties.AdditionalFields.Signer` | `target.file.signature_info.sigcheck.signers.name` |   
`properties.AdditionalFields.FileSizeInBytes` | `target.file.size` |   
`properties.AdditionalFields.GroupDomainName` | `target.group.attribute.labels[GroupDomainName]` |   
`properties.AdditionalFields.GroupName` | `target.group.group_display_name` |   
`properties.AdditionalFields.GroupSid` | `target.group.windows_sid` |   
`properties.AdditionalFields.Namespace` | `principal.namespace` |   
`properties.AdditionalFields.ScriptContent` | `target.process.command_line` | If the `properties.ProcessCommandLine` log field value is empty, then the `properties.AdditionalFields.ScriptContent` log field is mapped to the `target.process.command_line` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `ScriptContent` and the `properties.AdditionalFields.ScriptContent` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.ProcessId` | `target.process.pid` | If the `properties.ProcessId` log field value is empty, then the `properties.AdditionalFields.ProcessId` log field is mapped to the `target.process.pid` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `ProcessId` and the `properties.AdditionalFields.ProcessId` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.ClrInstanceId` | `additional.fields[ClrInstanceId]` |   
`properties.AdditionalFields.ModuleFlags` | `additional.fields[ModuleFlags]` |   
`properties.AdditionalFields.ModuleNativePathOrName` | `additional.fields[ModuleNativePathOrName]` |   
`properties.AdditionalFields.SubjectUserName` | `additional.fields[SubjectUserName]` |   
`properties.AdditionalFields.TaskContent` | `target.resource.attribute.labels[TaskContent]` |   
`properties.AdditionalFields.TaskName` | `target.resource.name` |   
`properties.AdditionalFields.RelatedContainerId` | `target.resource.product_object_id` |   
`properties.AdditionalFields.FriendlyName,properties.AdditionalFields.DisplayName,properties.AdditionalFields.SafeLinksUrl` | `target.url` | If the `properties.RemoteUrl` log field value is empty, then if the `properties.AdditionalFields.SafeLinksUrl` log field value is _not_ empty, then the `properties.AdditionalFields.SafeLinksUrl` log field is mapped to the `target.url` UDM field and the `additional.fields.key` UDM field is set to `DisplayName` and the `properties.AdditionalFields.DisplayName` log field is mapped to the `additional.fields.value.string_value` UDM field and the `additional.fields.key` UDM field is set to `FriendlyName` and the `properties.AdditionalFields.FriendlyName` log field is mapped to the `additional.fields.value.string_value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.DisplayName` log field value is _not_ empty and the `properties.ActionType` log field value is equal to `ExploitGuardNetworkProtectionBlocked`, then the `url` field is extracted from `properties.AdditionalFields.DisplayName` log field using the Grok pattern. The `url` log field is mapped to the `target.url` UDM field and the `additional.fields.key` UDM field is set to `FriendlyName` and the `properties.AdditionalFields.FriendlyName` log field is mapped to the `additional.fields.value.string_value` UDM field.  
  
Otherwise, if the `properties.AdditionalFields.FriendlyName` log field value is _not_ empty, then the `properties.AdditionalFields.FriendlyName` log field is mapped to the `target.url` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `SafeLinksUrl` and the `properties.AdditionalFields.SafeLinksUrl` log field is mapped to the `additional.fields.value.string_value` UDM field and the `additional.fields.key` UDM field is set to `DisplayName` and the `properties.AdditionalFields.DisplayName` log field is mapped to the `additional.fields.value.string_value` UDM field and the `additional.fields.key` UDM field is set to `FriendlyName` and the `properties.AdditionalFields.FriendlyName` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.HomeDirectory` | `target.user.attribute.labels[HomeDirectory]` |   
`properties.AdditionalFields.HomePath` | `target.user.attribute.labels[HomePath]` |   
`properties.AdditionalFields.NewUacValue` | `target.user.attribute.labels[NewUacValue]` |   
`properties.AdditionalFields.OldUacValue` | `target.user.attribute.labels[OldUacValue]` |   
`properties.AdditionalFields.ProfilePath` | `target.user.attribute.labels[ProfilePath]` |   
`properties.AdditionalFields.SamAccountName` | `target.user.attribute.labels[SamAccountName]` |   
`properties.AdditionalFields.ScriptPath` | `target.user.attribute.labels[ScriptPath]` |   
`properties.AdditionalFields.UserAccountControl` | `target.user.attribute.labels[UserAccountControl]` |   
`properties.AdditionalFields.UserParameters` | `target.user.attribute.labels[UserParameters]` |   
`properties.AdditionalFields.PrimaryGroupId` | `target.user.group_identifiers` |   
`properties.AdditionalFields.PasswordLastSet` | `target.user.last_password_change_time` |   
`properties.AdditionalFields.DisplayName` | `target.user.user_display_name` | If the `properties.ActionType` log field value is equal to `UserAccountModified`, then the `properties.AdditionalFields.DisplayName` log field is mapped to the `target.user.user_display_name` UDM field.  
`properties.AdditionalFields.RegistryKey` | `additional.fields[RegistryKey]` |   
`properties.AdditionalFields.ImageMD5` | `additional.fields[ImageMD5]` |   
`properties.AdditionalFields.ImageName` | `additional.fields[ImageName]` |   
`properties.AdditionalFields.ImageSHA1` | `additional.fields[ImageSHA1]` |   
`properties.AdditionalFields.ImageSHA256` | `additional.fields[ImageSHA256]` |   
`properties.AdditionalFields.UserSid` | `additional.fields[UserSid]` |   
`properties.AdditionalFields.SessionId` | `network.session_id` | If the `properties.LogonId` log field value is empty, then the `properties.AdditionalFields.SessionId` log field is mapped to the `network.session_id` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `SessionId` and the `properties.AdditionalFields.SessionId` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.RelatedContainerId` | `target.resource.resource_type` | If the `properties.AdditionalFields.RelatedContainerId` log field value is _not_ empty, then the `target.resource.resource_type` UDM field is set to `CONTAINER`.  
`properties.AdditionalFields.TaskContent.Actions.Exec.Command, properties.AdditionalFields.TaskContent.Actions.Exec.Arguments` | `target.process.command_line` | If the `properties.ActionType` log field value contains one of the following values:

  * `ScheduledTaskCreated`
  * `ScheduledTaskUpdated`
  * `ScheduledTaskDeleted`

then the `target.process.command_line` UDM field is set to a value formed by concatenating the values of the `properties.AdditionalFields.TaskContent.Actions.Exec.Command` and `properties.AdditionalFields.TaskContent.Actions.Exec.Arguments` log fields.  
  
### AdditionalFields mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmInfoGathering

The following table lists the `AdditionalFields` log fields for the `DeviceTvmInfoGathering` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.AdditionalFields.AvMode` | `additional.fields[AvMode]` |   
`properties.AdditionalFields.AvEngineVersion` | `additional.fields[AvEngineVersion]` |   
`properties.AdditionalFields.AvSignatureVersion` | `additional.fields[AvSignatureVersion]` |   
`properties.AdditionalFields.AvPlatformVersion` | `additional.fields[AvPlatformVersion]` |   
`properties.AdditionalFields.AvScanResults.Quick.ScanStatus` | `additional.fields[AvScanResults_Quick_ScanStatus]` |   
`properties.AdditionalFields.AvScanResults.Quick.ErrorCode` | `additional.fields[AvScanResults_Quick_ErrorCode]` |   
`properties.AdditionalFields.AvScanResults.Quick.Timestamp` | `additional.fields[AvScanResults_Quick_Timestamp]` |   
`properties.AdditionalFields.AvScanResults.Full.ScanStatus` | `additional.fields[AvScanResults_Full_ScanStatus]` |   
`properties.AdditionalFields.AvScanResults.Full.ErrorCode` | `additional.fields[AvScanResults_Full_ErrorCode]` |   
`properties.AdditionalFields.AvScanResults.Full.Timestamp` | `additional.fields[AvScanResults_Full_Timestamp]` |   
`properties.AdditionalFields.AvScanResults.Custom` | `additional.fields[AvScanResults_Custom]` |   
`properties.AdditionalFields.AvModeDataRefreshTime` | `additional.fields[AvModeDataRefreshTime]` |   
`properties.AdditionalFields.CloudProtectionState` | `additional.fields[CloudProtectionState]` |   
`properties.AdditionalFields.SslClient20` | `additional.fields[SslClient20]` |   
`properties.AdditionalFields.SslClient30` | `additional.fields[SslClient30]` |   
`properties.AdditionalFields.SslServer20` | `additional.fields[SslServer20]` |   
`properties.AdditionalFields.SslServer30` | `additional.fields[SslServer30]` |   
`properties.AdditionalFields.TlsClient10` | `additional.fields[TlsClient10]` |   
`properties.AdditionalFields.TlsClient11` | `additional.fields[TlsClient11]` |   
`properties.AdditionalFields.TlsClient12` | `additional.fields[TlsClient12]` |   
`properties.AdditionalFields.TlsServer10` | `additional.fields[TlsServer10]` |   
`properties.AdditionalFields.TlsServer11` | `additional.fields[TlsServer11]` |   
`properties.AdditionalFields.TlsServer12` | `additional.fields[TlsServer12]` |   
`properties.AdditionalFields.SchUseStrongCrypto35` | `additional.fields[SchUseStrongCrypto35]` |   
`properties.AdditionalFields.SchUseStrongCrypto35Wow6432` | `additional.fields[SchUseStrongCrypto35Wow6432]` |   
`properties.AdditionalFields.SchUseStrongCrypto40` | `additional.fields[SchUseStrongCrypto40]` |   
`properties.AdditionalFields.SchUseStrongCrypto40Wow6432` | `additional.fields[SchUseStrongCrypto40Wow6432]` |   
`properties.AdditionalFields.SystemDefaultTlsVersions35` | `additional.fields[SystemDefaultTlsVersions35]` |   
`properties.AdditionalFields.SystemDefaultTlsVersions35Wow6432` | `additional.fields[SystemDefaultTlsVersions35Wow6432]` |   
`properties.AdditionalFields.SystemDefaultTlsVersions40` | `additional.fields[SystemDefaultTlsVersions40]` |   
`properties.AdditionalFields.SystemDefaultTlsVersions40Wow6432` | `additional.fields[SystemDefaultTlsVersions40Wow6432]` |   
`properties.AdditionalFields.Log4j_CVE_2021_44228` | `additional.fields[Log4j_CVE_2021_44228]` |   
`properties.AdditionalFields.LocalCveScannerExecuted` | `additional.fields[LocalCveScannerExecuted]` |   
`properties.AdditionalFields.Log4jLocalScanVulnerable` | `additional.fields[Log4jLocalScanVulnerable]` |   
`properties.AdditionalFields.Log4JEnvironmentVariableMitigation` | `additional.fields[Log4JEnvironmentVariableMitigation]` |   
`properties.AdditionalFields.IsWindowsLtscVersionRunning` | `additional.fields[IsWindowsLtscVersionRunning]` |   
`properties.AdditionalFields.AvEngineUpdateTime` | `additional.fields[AvEngineUpdateTime]` |   
`properties.AdditionalFields.AvSignatureUpdateTime` | `additional.fields[AvSignatureUpdateTime]` |   
`properties.AdditionalFields.AvPlatformUpdateTime` | `additional.fields[AvPlatformUpdateTime]` |   
`properties.AdditionalFields.AvIsSignatureUptoDate` | `additional.fields[AvIsSignatureUptoDate]` |   
`properties.AdditionalFields.AvIsEngineUptodate` | `additional.fields[AvIsEngineUptodate]` |   
`properties.AdditionalFields.AvIsPlatformUptodate` | `additional.fields[AvIsPlatformUptodate]` |   
`properties.AdditionalFields.WdavorHeartbeatEventType` | `additional.fields[WdavorHeartbeatEventType]` |   
`properties.AdditionalFields.AvSignaturePublishTime` | `additional.fields[AvSignaturePublishTime]` |   
`properties.AdditionalFields.AvPlatformPublishTime` | `additional.fields[AvPlatformPublishTime]` |   
`properties.AdditionalFields.AvEnginePublishTime` | `additional.fields[AvEnginePublishTime]` |   
`properties.AdditionalFields.AvSignatureRing` | `additional.fields[AvSignatureRing]` |   
`properties.AdditionalFields.AvPlatformRing` | `additional.fields[AvPlatformRing]` |   
`properties.AdditionalFields.AvEngineRing` | `additional.fields[AvEngineRing]` |   
`properties.AdditionalFields.Spring4Shell_CVE_2022_22965` | `additional.fields[Spring4Shell_CVE_2022_22965]` |   
`properties.AdditionalFields.CVE_2022_30190_Mitigated` | `additional.fields[CVE_2022_30190_Mitigated]` |   
`properties.AdditionalFields.Bootiful_Mind_status` | `additional.fields[Bootiful_Mind_status]` |   
`properties.AdditionalFields.AvSignatureDataRefreshTime` | `additional.fields[AvSignatureDataRefreshTime]` |   
`properties.AdditionalFields.EBPFStatus` | `additional.fields[EBPFStatus]` |   
`properties.AdditionalFields.AsrConfigurationStates.ExecutableEmailContent` | `additional.fields[AsrConfigurationStates_ExecutableEmailContent]` |   
`properties.AdditionalFields.AsrConfigurationStates.OfficeChildProcess` | `additional.fields[AsrConfigurationStates_OfficeChildProcess]` |   
`properties.AdditionalFields.AsrConfigurationStates.ExecutableOfficeContent` | `additional.fields[AsrConfigurationStates_ExecutableOfficeContent]` |   
`properties.AdditionalFields.AsrConfigurationStates.OfficeProcessInjection` | `additional.fields[AsrConfigurationStates_OfficeProcessInjection]` |   
`properties.AdditionalFields.AsrConfigurationStates.ScriptExecutableDownload` | `additional.fields[AsrConfigurationStates_ScriptExecutableDownload]` |   
`properties.AdditionalFields.AsrConfigurationStates.ObfuscatedScript` | `additional.fields[AsrConfigurationStates_ObfuscatedScript]` |   
`properties.AdditionalFields.AsrConfigurationStates.OfficeMacroWin32ApiCalls` | `additional.fields[AsrConfigurationStates_OfficeMacroWin32ApiCalls]` |   
`properties.AdditionalFields.AsrConfigurationStates.UntrustedExecutable` | `additional.fields[AsrConfigurationStates_UntrustedExecutable]` |   
`properties.AdditionalFields.AsrConfigurationStates.Ransomware` | `additional.fields[AsrConfigurationStates_Ransomware]` |   
`properties.AdditionalFields.AsrConfigurationStates.LsassCredentialTheft` | `additional.fields[AsrConfigurationStates_LsassCredentialTheft]` |   
`properties.AdditionalFields.AsrConfigurationStates.PsexecWmiChildProcess` | `additional.fields[AsrConfigurationStates_PsexecWmiChildProcess]` |   
`properties.AdditionalFields.AsrConfigurationStates.UntrustedUsbProcess` | `additional.fields[AsrConfigurationStates_UntrustedUsbProcess]` |   
`properties.AdditionalFields.AsrConfigurationStates.OfficeCommAppChildProcess` | `additional.fields[AsrConfigurationStates_OfficeCommAppChildProcess]` |   
`properties.AdditionalFields.AsrConfigurationStates.AdobeReaderChildProcess` | `additional.fields[AsrConfigurationStates_AdobeReaderChildProcess]` |   
`properties.AdditionalFields.AsrConfigurationStates.PersistenceThroughWmi` | `additional.fields[AsrConfigurationStates_PersistenceThroughWmi]` |   
`properties.AdditionalFields.AsrConfigurationStates.VulnerableSignedDriver` | `additional.fields[AsrConfigurationStates_VulnerableSignedDriver]` |   
`properties.AdditionalFields.AsrConfigurationStates.BlockWebshellCreation` | `additional.fields[AsrConfigurationStates_BlockWebshellCreation]` |   
`properties.AdditionalFields.AsrConfigurationStates.BlockCopiedOrImpersonatedSystemTools` | `additional.fields[AsrConfigurationStates_BlockCopiedOrImpersonatedSystemTools]` |   
`properties.AdditionalFields.AsrConfigurationStates.BlockSafeModeReboot` | `additional.fields[AsrConfigurationStates_BlockSafeModeReboot]` |   
  
### AdditionalFields mapping reference: MICROSOFT DEFENDER ENDPOINT - CloudAppEvents

The following table lists the `AdditionalFields` log fields for the `CloudAppEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.AdditionalFields.IsSatelliteProvider` | `additional.fields[IsSatelliteProvider]` |   
  
### AdditionalFields mapping reference: MICROSOFT DEFENDER ENDPOINT - IdentityLogonEvents

The following table lists the `AdditionalFields` log fields for the `IdentityLogonEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.AdditionalFields.ActionTypeInner` | `additional.fields[ActionTypeInner]` |   
`properties.AdditionalFields.ACTOR.ACCOUNT` | `principal.user.user_display_name` | If the `properties.AccountDisplayName` log field value is empty, then the `properties.AdditionalFields.ACTOR.ACCOUNT` log field is mapped to the `principal.user.user_display_name` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `ACTOR_ACCOUNT` and the `properties.AdditionalFields.ACTOR.ACCOUNT` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.AdditionalFields.ACTOR.ALIAS` | `additional.fields[ACTOR_ALIAS]` |   
`properties.AdditionalFields.ACTOR.DEVICE` | `principal.hostname` | If the `properties.DeviceName` log field value is empty, then the `properties.AdditionalFields.ACTOR.DEVICE` log field is mapped to the `principal.hostname` UDM field.  
  
Otherwise, the `principal.resource.attribute.labels.key` UDM field is set to `ACTOR_DEVICE` and the `properties.AdditionalFields.ACTOR.DEVICE` log field is mapped to the `principal.resource.attribute.labels.value` UDM field.  
`properties.AdditionalFields.SourceAccountName,properties.AdditionalFields.ACTOR.ENTITY_USER` | `principal.user.userid` | If the `properties.AccountName` log field value is empty, then if the `properties.AdditionalFields.SourceAccountName` log field value is _not_ empty, then the `properties.AdditionalFields.SourceAccountName` log field is mapped to the `principal.user.userid` UDM field. If the `properties.AdditionalFields.ACTOR.ENTITY_USER` log field value is _not_ empty, then the `principal.user.attribute.labels.key` UDM field is set to `ACTOR_ENTITY_USER` and the `properties.AdditionalFields.ACTOR.ENTITY_USER` log field is mapped to the `principal.user.attribute.labels.value` UDM field. Otherwise, the `properties.AdditionalFields.ACTOR.ENTITY_USER` log field is mapped to the `principal.user.userid` UDM field.  
  
Otherwise, the `properties.AccountName` log field is mapped to the `principal.user.userid` UDM field. If the `properties.AdditionalFields.SourceAccountName` log field value is _not_ empty, then the `principal.user.attribute.labels.key` UDM field is set to `SourceAccountName` and the `properties.AdditionalFields.SourceAccountName` log field is mapped to the `principal.user.attribute.labels.value` UDM field. If the `properties.AdditionalFields.ACTOR.ENTITY_USER` log field value is _not_ empty, then the `principal.user.attribute.labels.key` UDM field is set to `ACTOR_ENTITY_USER` and the `properties.AdditionalFields.ACTOR.ENTITY_USER` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.AdditionalFields.ARG.CLOUD_SERVICE` | `target.application` |   
`properties.AdditionalFields.AttackTechniques` | `security_result.attack_details.techniques.name` |   
`properties.AdditionalFields.Category` | `security_result.category_details` |   
`properties.AdditionalFields.Count` | `additional.fields[Count]` |   
`properties.AdditionalFields.DestinationComputerObjectGuid` | `intermediary.resource.product_object_id` |   
`properties.AdditionalFields.DestinationComputerOperatingSystem` | `intermediary.asset.platform_software.platform_version` |   
`properties.AdditionalFields.DestinationComputerOperatingSystemType` | `intermediary.asset.platform_software.platform` | If the `properties.AdditionalFields.DestinationComputerOperatingSystemType` log field value matches the regular expression pattern `(?i)windows`, then the `intermediary.asset.platform_software.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.AdditionalFields.DestinationComputerOperatingSystemType` log field value matches the regular expression pattern `(?i)macos`, then the `intermediary.asset.platform_software.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.AdditionalFields.DestinationComputerOperatingSystemType` log field value matches the regular expression pattern `(?i)linux`, then the `intermediary.asset.platform_software.platform` UDM field is set to `LINUX`.  
`properties.AdditionalFields.DestinationComputerOperatingSystemVersion` | `intermediary.asset.software.version` |   
`properties.AdditionalFields.EncryptionType` | `additional.fields[EncryptionType]` |   
`properties.AdditionalFields.FROM.DEVICE` | `src.hostname` |   
`properties.AdditionalFields.IsNtlmV1` | `additional.fields[IsNtlmV1]` |   
`properties.AdditionalFields.IsResourceAccountTrustedForUnconstrainedDelegation` | `additional.fields[IsResourceAccountTrustedForUnconstrainedDelegation]` |   
`properties.AdditionalFields.IsSourceAccountLocalAdminOnResource` | `additional.fields[IsSourceAccountLocalAdminOnResource]` |   
`properties.AdditionalFields.KdcOptions` | `additional.fields[KdcOptions]` |   
`properties.AdditionalFields.KerberosType` | `additional.fields[KerberosType]` |   
`properties.AdditionalFields.Pass-through authentication` | `additional.fields[Pass_through_authentication]` |   
`properties.AdditionalFields.Request ID` | `additional.fields[Request_ID]` |   
`properties.AdditionalFields.RequestTicketHash` | `additional.fields[RequestTicketHash]` |   
`properties.AdditionalFields.ResponseTicketHash` | `additional.fields[ResponseTicketHash]` |   
`properties.AdditionalFields.SourceAccountId` | `principal.user.product_object_id` | If the `properties.AccountObjectId` log field value is empty, then the `properties.AdditionalFields.SourceAccountId` log field is mapped to the `principal.user.product_object_id` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `SourceAccountId` and the `properties.AdditionalFields.SourceAccountId` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.AdditionalFields.SourceAccountLastLogonToSourceComputerTime` | `additional.fields[SourceAccountLastLogonToSourceComputerTime]` |   
`properties.AdditionalFields.SourceAccountSid` | `principal.user.windows_sid` | If the `properties.AccountSid` log field value is empty, then the `properties.AdditionalFields.SourceAccountSid` log field is mapped to the `principal.user.windows_sid` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `SourceAccountSid` and the `properties.AdditionalFields.SourceAccountSid` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.AdditionalFields.SourceComputerId` | `additional.fields[SourceComputerId]` |   
`properties.AdditionalFields.SourceComputerObjectGuid` | `principal.resource.product_object_id` |   
`properties.AdditionalFields.SourceComputerOperatingSystem` | `principal.asset.platform_software.platform_version` | If the `properties.OSPlatform` log field value is empty, then the `properties.AdditionalFields.SourceComputerOperatingSystem` log field is mapped to the `principal.asset.platform_software.platform_version` UDM field.  
  
Otherwise, the `principal.asset.attribute.labels.key` UDM field is set to `SourceComputerOperatingSystem` and the `properties.AdditionalFields.SourceComputerOperatingSystem` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`properties.AdditionalFields.SourceComputerOperatingSystemType` | `principal.asset.platform_software.platform` | If the `properties.OSPlatform` log field value is empty, then if the `properties.AdditionalFields.SourceComputerOperatingSystemType` log field value matches the regular expression pattern `(?i)macos`, then the `principal.asset.platform_software.platform` UDM field is set to `MAC`. Otherwise, if the `properties.AdditionalFields.SourceComputerOperatingSystemType` log field value matches the regular expression pattern `(?i)windows`, then the `principal.asset.platform_software.platform` UDM field is set to `WINDOWS`. Otherwise, if the `properties.AdditionalFields.SourceComputerOperatingSystemType` log field value matches the regular expression pattern `(?i)linux`, then the `principal.asset.platform_software.platform` UDM field is set to `LINUX`.  
  
Otherwise, the `principal.asset.attribute.labels.key` UDM field is set to `SourceComputerOperatingSystemType` and the `properties.AdditionalFields.SourceComputerOperatingSystemType` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`properties.AdditionalFields.SourceComputerOperatingSystemVersion` | `principal.asset.software.version` |   
`properties.AdditionalFields.SourceComputerSid` | `additional.fields[SourceComputerSid]` |   
`properties.AdditionalFields.Spns` | `additional.fields[Spns]` |   
`properties.AdditionalFields.TARGET_OBJECT.DEVICE` | `target.hostname` | If the `properties.TargetDeviceName` log field value is empty, then the `properties.AdditionalFields.TARGET_OBJECT.DEVICE` log field is mapped to the `target.hostname` UDM field.  
  
Otherwise, the `target.resource.attribute.labels.key` UDM field is set to `TARGET_OBJECT_DEVICE` and the `properties.AdditionalFields.TARGET_OBJECT.DEVICE` log field is mapped to the `target.resource.attribute.labels.value` UDM field.  
`properties.AdditionalFields.TargetComputerObjectGuid` | `target.resource.product_object_id` |   
`properties.AdditionalFields.TargetComputerOperatingSystem` | `target.asset.platform_software.platform_version` |   
`properties.AdditionalFields.TargetComputerOperatingSystemType` | `target.asset.platform_software.platform` | If the `properties.AdditionalFields.TargetComputerOperatingSystemType` log field value matches the regular expression pattern `(?i)windows`, then the `target.asset.platform_software.platform` UDM field is set to `WINDOWS`.  
  
Otherwise, if the `properties.AdditionalFields.TargetComputerOperatingSystemType` log field value matches the regular expression pattern `(?i)macos`, then the `target.asset.platform_software.platform` UDM field is set to `MAC`.  
  
Otherwise, if the `properties.AdditionalFields.TargetComputerOperatingSystemType` log field value matches the regular expression pattern `(?i)linux`, then the `target.asset.platform_software.platform` UDM field is set to `LINUX`.  
`properties.AdditionalFields.TargetComputerOperatingSystemVersion` | `target.asset.software.version` |   
`properties.AdditionalFields.TO.DEVICE` | `intermediary.hostname` | If the `properties.DestinationDeviceName` log field value is empty, then the `properties.AdditionalFields.TO.DEVICE` log field is mapped to the `intermediary.hostname` UDM field.  
  
Otherwise, the `intermediary.resource.attribute.labels.key` UDM field is set to `TO_DEVICE` and the `properties.AdditionalFields.TO.DEVICE` log field is mapped to the `intermediary.resource.attribute.labels.value` UDM field.  
  
### AdditionalFields mapping reference: MICROSOFT DEFENDER ENDPOINT - EmailEvents

The following table lists the `AdditionalFields` log fields for the `EmailEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.AdditionalFields.TransportRuleGuid` | `additional.fields[TransportRuleGuid]` |   
`properties.AdditionalFields.UserDetectedLocation` | `additional.fields[UserDetectedLocation]` |   
`properties.AdditionalFields.ImpersonatedDomain` | `additional.fields[ImpersonatedDomain]` |   
  
### AdditionalFields mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceInfo

The following table lists the `AdditionalFields` log fields for the `DeviceInfo` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.AdditionalFields.InternetFacingLastSeen` | `entity.asset.last_discover_time` |   
`properties.AdditionalFields.InternetFacingLocalIp` | `entity.asset.ip` |   
`properties.AdditionalFields.InternetFacingLocalPort` | `entity.port` |   
`properties.AdditionalFields.InternetFacingPublicScannedIp` | `entity.asset.nat_ip` | If the `properties.PublicIP` log field value is empty, then the `properties.AdditionalFields.InternetFacingPublicScannedIp` log field is mapped to the `entity.asset.nat_ip` UDM field.  
  
Otherwise, the `entity.asset.attribute.labels.key` UDM field is set to `InternetFacingPublicScannedIp` and the `properties.AdditionalFields.InternetFacingPublicScannedIp` log field is mapped to the `entity.asset.attribute.labels.value` UDM field.  
`properties.AdditionalFields.InternetFacingPublicScannedPort` | `entity.nat_port` |   
`properties.AdditionalFields.InternetFacingReason` | `entity.asset.attribute.labels[InternetFacingReason]` |   
`properties.AdditionalFields.InternetFacingTransportProtocol` | `entity.network.ip_protocol` | If the `properties.AdditionalFields.InternetFacingTransportProtocol` log field value is equal to `Tcp`, then the `entity.network.ip_protocol` UDM field is set to `TCP`.  
  
Otherwise, if the `properties.AdditionalFields.InternetFacingTransportProtocol` log field value is equal to `Udp`, then the `entity.network.ip_protocol` UDM field is set to `UDP`.  
  
Otherwise, if the `properties.AdditionalFields.InternetFacingTransportProtocol` log field value is equal to `Icmp`, then the `entity.network.ip_protocol` UDM field is set to `ICMP`.  
  
Otherwise, the `entity.network.ip_protocol` UDM field is set to `UNKNOWN_IP_PROTOCOL`.  
  
### AdditionalFields mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceLogonEvents

The following table lists the `AdditionalFields` log fields for the `DeviceLogonEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.AdditionalFields.InitiatingAccountDomain` | `principal.domain.name` |   
`properties.AdditionalFields.InitiatingAccountName,properties.AdditionalFields.InitiatingAccountPosixUserId` | `principal.user.userid` | If the `properties.InitiatingProcessAccountName` log field value is empty, then if the `properties.AdditionalFields.InitiatingAccountName` log field value is _not_ empty, then the `properties.AdditionalFields.InitiatingAccountName` log field is mapped to the `principal.user.userid` UDM field. If the `properties.AdditionalFields.InitiatingAccountPosixUserId` log field value is _not_ empty, then the `principal.user.attribute.labels.key` UDM field is set to `InitiatingAccountPosixUserId` and the `properties.AdditionalFields.InitiatingAccountPosixUserId` log field is mapped to the `principal.user.attribute.labels.value` UDM field. Otherwise, the `properties.AdditionalFields.InitiatingAccountPosixUserId` log field is mapped to the `principal.user.userid` UDM field.  
  
Otherwise, the `properties.InitiatingProcessAccountName` log field is mapped to the `principal.user.userid` UDM field. If the `properties.AdditionalFields.InitiatingAccountName` log field value is _not_ empty, then the `principal.user.attribute.labels.key` UDM field is set to `InitiatingAccountName` and the `properties.AdditionalFields.InitiatingAccountName` log field is mapped to the `principal.user.attribute.labels.value` UDM field. If the `properties.AdditionalFields.InitiatingAccountPosixUserId` log field value is _not_ empty, then the `principal.user.attribute.labels.key` UDM field is set to `InitiatingAccountPosixUserId` and the `properties.AdditionalFields.InitiatingAccountPosixUserId` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.AdditionalFields.InitiatingAccountPosixGroupId` | `principal.group.product_object_id` |   
`properties.AdditionalFields.InitiatingAccountPosixGroupName` | `principal.group.group_display_name` |   
`properties.AdditionalFields.IsLocalLogon` | `additional.fields[isLocalLogon]` |   
`properties.AdditionalFields.PosixPrimaryGroupId` | `about.group.product_object_id` |   
`properties.AdditionalFields.PosixPrimaryGroupName` | `about.group.group_display_name` |   
`properties.AdditionalFields.PosixSecondaryGroups` | `about.group.attribute.labels[PosixSecondaryGroups]` | The `properties.AdditionalFields.PosixSecondaryGroups` log field is set to a value generated from the template `{"properties.AdditionalFields.PosixSecondaryGroups":%{properties.AdditionalFields.PosixSecondaryGroups}}`, where `%{properties.AdditionalFields.PosixSecondaryGroups}` is replaced with the value of the `properties.AdditionalFields.PosixSecondaryGroups` log field. The `properties.AdditionalFields.PosixSecondaryGroups` log field is parsed as JSON.  
  
Iterate for each key, value pair of log field `properties.AdditionalFields.PosixSecondaryGroups`:  
  
The `about.group.attribute.labels.key` UDM field is set to a value generated from the template `PosixSecondaryGroups_%{key}`, where `%{key}` is replaced with the value of the `key` log field and the `value of properties.AdditionalFields.PosixSecondaryGroups` log field is mapped to the `about.group.attribute.labels.value` UDM field.  
`properties.AdditionalFields.PosixUserId` | `about.user.userid` |   
`properties.AdditionalFields.Terminal` | `additional.fields[Terminal]` |   
`properties.AdditionalFields.Upn` | `target.user.user_display_name` |   
  
### AdditionalFields mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceFileEvents

The following table lists the `AdditionalFields` log fields for the `DeviceFileEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.AdditionalFields.FilePosixGroupOwner.Name` | `about.group.group_display_name` |   
`properties.AdditionalFields.FilePosixGroupOwner.PosixGroupId` | `about.group.product_object_id` |   
`properties.AdditionalFields.FilePosixPermissions` | `additional.fields[FilePosixPermissions]` | Iterate through log field `properties.AdditionalFields.FilePosixPermissions`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `FilePosixPermissions_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.FilePosixPermissions` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.FilePosixUserOwner.AadUserUpn` | `about.user.email_addresses` |   
`properties.AdditionalFields.FilePosixUserOwner.DomainName` | `about.user.attribute.labels[FilePosixUserOwner_DomainName]` |   
`properties.AdditionalFields.FilePosixUserOwner.LogonId` | `about.user.attribute.labels[FilePosixUserOwner_LogonId]` |   
`properties.AdditionalFields.FilePosixUserOwner.Name` | `about.user.user_display_name` |   
`properties.AdditionalFields.FilePosixUserOwner.PosixUserId` | `about.user.userid` |   
`properties.AdditionalFields.FilePosixUserOwner.PrimaryPosixGroup.Name` | `about.user.group_identifiers` |   
`properties.AdditionalFields.FilePosixUserOwner.PrimaryPosixGroup.PosixGroupId` | `about.user.groupid` |   
`properties.AdditionalFields.FilePosixUserOwner.Sid` | `about.user.windows_sid` |   
`properties.AdditionalFields.FileStreamName` | `additional.fields[FileStreamName]` |   
`properties.AdditionalFields.FileType` | `target.file.file_type` | If the `properties.AdditionalFields.FileType` log field value is equal to `PortableExecutable`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PE_EXE`.  
  
Otherwise, if the `properties.AdditionalFields.FileType` log field value is equal to `PDF`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PDF`.  
  
Otherwise, if the `properties.AdditionalFields.FileType` log field value is equal to `Zip`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ZIP`.  
  
Otherwise, if the `properties.AdditionalFields.FileType` log field value is equal to `SevenZip`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SEVENZIP`.  
  
Otherwise, if the `properties.AdditionalFields.FileType` log field value is equal to `Rar`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RAR`.  
  
Otherwise, if the `properties.AdditionalFields.FileType` log field value is equal to `MachOExecutable`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MACH_O`.  
  
Otherwise, if the `properties.AdditionalFields.FileType` log field value is equal to `Shebang`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SCRIPT`.  
  
Otherwise, if the `properties.AdditionalFields.FileType` log field value is equal to `Tar`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TAR`.  
  
Otherwise, the `target.file.file_type` UDM field is set to `FILE_TYPE_UNSPECIFIED`.  
`properties.AdditionalFields.InitiatingProcessCurrentWorkingDirectory` | `principal.process.file.full_path` | If the `properties.InitiatingProcessFolderPath` log field value is empty, then the `properties.AdditionalFields.InitiatingProcessCurrentWorkingDirectory` log field is mapped to the `principal.process.file.full_path` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `InitiatingProcessCurrentWorkingDirectory` and the `properties.AdditionalFields.InitiatingProcessCurrentWorkingDirectory` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.InitiatingProcessPosixAttachedTerminal` | `principal.process.tty` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveGroup.Name` | `about.group.group_display_name` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveGroup.PosixGroupId` | `principal.process.egid` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.AadUserUpn` | `about.user.email_addresses` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.DomainName` | `about.user.attribute.labels[InitiatingProcessPosixEffectiveUser_DomainName]` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.LogonId` | `about.user.attribute.labels[InitiatingProcessPosixEffectiveUser_LogonId]` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.Name` | `about.user.user_display_name` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.PosixUserId` | `principal.process.euid` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.PrimaryPosixGroup.Name` | `about.user.group_identifiers` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.PrimaryPosixGroup.PosixGroupId` | `about.user.groupid` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.Sid` | `about.user.windows_sid` |   
`properties.AdditionalFields.InitiatingProcessPosixFilePermissions` | `additional.fields[InitiatingProcessPosixFilePermissions]` | Iterate through log field `properties.AdditionalFields.InitiatingProcessPosixFilePermissions`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `InitiatingProcessPosixFilePermissions_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.InitiatingProcessPosixFilePermissions` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.InitiatingProcessPosixGroupOwner.Name` | `principal.group.group_display_name` |   
`properties.AdditionalFields.InitiatingProcessPosixGroupOwner.PosixGroupId` | `principal.group.product_object_id` |   
`properties.AdditionalFields.InitiatingProcessPosixProcessGroupId` | `principal.process.pgid` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.AadUserUpn` | `principal.user.email_addresses` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.DomainName` | `principal.user.attribute.labels[RealUser_DomainName]` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.LogonId` | `principal.user.attribute.labels[RealUser_LogonId]` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.Name` | `principal.user.user_display_name` | If the `properties.InitiatingProcessAccountUpn` log field value is empty, then the `properties.AdditionalFields.InitiatingProcessPosixRealUser.Name` log field is mapped to the `principal.user.user_display_name` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `InitiatingProcessPosixRealUser_Name` and the `properties.AdditionalFields.InitiatingProcessPosixRealUser.Name` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.AdditionalFields.InitiatingProcessPosixRealUser.PosixUserId` | `principal.process.ruid` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.PrimaryPosixGroup.Name` | `principal.user.group_identifiers` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.PrimaryPosixGroup.PosixGroupId` | `principal.user.groupid` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.Sid` | `principal.user.windows_sid` | If the `properties.InitiatingProcessAccountSid` log field value is empty and the `properties.RequestAccountSid` log field value is empty, then the `properties.AdditionalFields.InitiatingProcessPosixRealUser.Sid` log field is mapped to the `principal.user.windows_sid` UDM field.  
  
Otherwise, the `principal.user.attribute.labels.key` UDM field is set to `InitiatingProcessPosixRealUser_Sid` and the `properties.AdditionalFields.InitiatingProcessPosixRealUser.Sid` log field is mapped to the `principal.user.attribute.labels.value` UDM field.  
`properties.AdditionalFields.InitiatingProcessPosixSessionId` | `network.session_id` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.AadUserUpn` | `about.user.email_addresses` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.DomainName` | `about.user.attribute.labels[InitiatingProcessPosixUserOwner_DomainName]` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.LogonId` | `about.user.attribute.labels[InitiatingProcessPosixUserOwner_LogonId]` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.Name` | `about.user.user_display_name` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.PosixUserId` | `about.user.userid` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.PrimaryPosixGroup.Name` | `about.user.group_identifiers` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.PrimaryPosixGroup.PosixGroupId` | `about.user.groupid` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.Sid` | `about.user.windows_sid` |   
`properties.AdditionalFields.uniqueEventsAggregated` | `additional.fields[uniqueEventsAggregated]` |   
  
### AdditionalFields mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceProcessEvents

The following table lists the `AdditionalFields` log fields for the `DeviceProcessEvents` log type and their corresponding UDM fields:   
  


Log field | UDM mapping | Logic  
---|---|---  
`properties.AdditionalFields.InitiatingProcessCurrentWorkingDirectory` | `additional.fields[InitiatingProcessCurrentWorkingDirectory]` |   
`properties.AdditionalFields.InitiatingProcessPosixAttachedTerminal` | `principal.process.tty` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveGroup.Name` | `additional.fields[InitiatingProcessPosixEffectiveGroup_Name]` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveGroup.PosixGroupId` | `principal.process.egid` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.AadUserUpn` | `additional.fields[InitiatingProcessPosixEffectiveUser_AadUserUpn]` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.DomainName` | `additional.fields[InitiatingProcessPosixEffectiveUser_DomainName]` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.LogonId` | `additional.fields[InitiatingProcessPosixEffectiveUser_LogonId]` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.Name` | `additional.fields[InitiatingProcessPosixEffectiveUser_Name]` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.PosixUserId` | `principal.process.euid` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.PrimaryPosixGroup.Name` | `additional.fields[InitiatingProcessPosixEffectiveUser_PrimaryPosixGroup_Name]` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.PrimaryPosixGroup.PosixGroupId` | `additional.fields[InitiatingProcessPosixEffectiveUser_PrimaryPosixGroup_PosixGroupId]` |   
`properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.Sid` | `additional.fields[InitiatingProcessPosixEffectiveUser_Sid]` |   
`properties.AdditionalFields.InitiatingProcessPosixFilePermissions` | `additional.fields[InitiatingProcessPosixFilePermissions]` | Iterate through log field `properties.AdditionalFields.InitiatingProcessPosixFilePermissions`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `InitiatingProcessPosixFilePermissions_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.InitiatingProcessPosixFilePermissions` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.InitiatingProcessPosixGroupOwner.Name` | `additional.fields[InitiatingProcessPosixGroupOwner_Name]` |   
`properties.AdditionalFields.InitiatingProcessPosixGroupOwner.PosixGroupId` | `additional.fields[InitiatingProcessPosixGroupOwner_PosixGroupId]` |   
`properties.AdditionalFields.InitiatingProcessPosixProcessGroupId` | `principal.process.pgid` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.AadUserUpn` | `additional.fields[InitiatingProcessPosixRealUser_AadUserUpn]` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.DomainName` | `additional.fields[InitiatingProcessPosixRealUser_DomainName]` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.LogonId` | `additional.fields[InitiatingProcessPosixRealUser_LogonId]` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.Name` | `additional.fields[InitiatingProcessPosixRealUser_Name]` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.PosixUserId` | `principal.process.ruid` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.PrimaryPosixGroup.Name` | `additional.fields[InitiatingProcessPosixRealUser_PrimaryPosixGroup_Name]` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.PrimaryPosixGroup.PosixGroupId` | `additional.fields[InitiatingProcessPosixRealUser_PrimaryPosixGroup_PosixGroupId]` |   
`properties.AdditionalFields.InitiatingProcessPosixRealUser.Sid` | `additional.fields[InitiatingProcessPosixRealUser_Sid]` |   
`properties.AdditionalFields.InitiatingProcessPosixSessionId,properties.AdditionalFields.ProcessPosixSessionId` | `network.session_id` | If the `properties.LogonId` log field value is empty, then if the `properties.AdditionalFields.ProcessPosixSessionId` log field value is _not_ empty, then the `properties.AdditionalFields.ProcessPosixSessionId` log field is mapped to the `network.session_id` UDM field. If the `properties.AdditionalFields.InitiatingProcessPosixSessionId` log field value is _not_ empty, then the `additional.fields.key` UDM field is set to `InitiatingProcessPosixSessionId` and the `properties.AdditionalFields.InitiatingProcessPosixSessionId` log field is mapped to the `additional.fields.value.string_value` UDM field. Otherwise, the `properties.AdditionalFields.InitiatingProcessPosixSessionId` log field is mapped to the `network.session_id` UDM field.  
  
Otherwise, the `additional.fields.key` UDM field is set to `InitiatingProcessPosixSessionId` and the `properties.AdditionalFields.InitiatingProcessPosixSessionId` log field is mapped to the `additional.fields.value.string_value` UDM field and the `additional.fields.key` UDM field is set to `ProcessPosixSessionId` and the `properties.AdditionalFields.ProcessPosixSessionId` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.AadUserUpn` | `additional.fields[InitiatingProcessPosixUserOwner_AadUserUpn]` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.DomainName` | `additional.fields[InitiatingProcessPosixUserOwner_DomainName]` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.LogonId` | `additional.fields[InitiatingProcessPosixUserOwner_LogonId]` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.Name` | `additional.fields[InitiatingProcessPosixUserOwner_Name]` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.PosixUserId` | `additional.fields[InitiatingProcessPosixUserOwner_PosixUserId]` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.PrimaryPosixGroup.Name` | `additional.fields[InitiatingProcessPosixUserOwner_PrimaryPosixGroup_Name]` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.PrimaryPosixGroup.PosixGroupId` | `additional.fields[InitiatingProcessPosixUserOwner_PrimaryPosixGroup_PosixGroupId]` |   
`properties.AdditionalFields.InitiatingProcessPosixUserOwner.Sid` | `additional.fields[InitiatingProcessPosixUserOwner_Sid]` |   
`properties.AdditionalFields.ProcessCurrentWorkingDirectory` | `additional.fields[ProcessCurrentWorkingDirectory]` |   
`properties.AdditionalFields.ProcessPosixAttachedTerminal` | `target.process.tty` |   
`properties.AdditionalFields.ProcessPosixEffectiveGroup.Name` | `about.group.group_display_name` |   
`properties.AdditionalFields.ProcessPosixEffectiveGroup.PosixGroupId` | `target.process.egid` |   
`properties.AdditionalFields.ProcessPosixEffectiveUser.AadUserUpn` | `about.user.email_addresses` |   
`properties.AdditionalFields.ProcessPosixEffectiveUser.DomainName` | `about.user.attribute.labels[ProcessPosixEffectiveUser_DomainName]` |   
`properties.AdditionalFields.ProcessPosixEffectiveUser.LogonId` | `about.user.attribute.labels[ProcessPosixEffectiveUser_LogonId]` |   
`properties.AdditionalFields.ProcessPosixEffectiveUser.Name` | `about.user.user_display_name` |   
`properties.AdditionalFields.ProcessPosixEffectiveUser.PosixUserId` | `target.process.euid` |   
`properties.AdditionalFields.ProcessPosixEffectiveUser.PrimaryPosixGroup.Name` | `about.user.group_identifiers` |   
`properties.AdditionalFields.ProcessPosixEffectiveUser.PrimaryPosixGroup.PosixGroupId` | `about.user.groupid` |   
`properties.AdditionalFields.ProcessPosixEffectiveUser.Sid` | `about.user.windows_sid` |   
`properties.AdditionalFields.ProcessPosixFileGroupOwner.Name` | `about.group.group_display_name` |   
`properties.AdditionalFields.ProcessPosixFileGroupOwner.PosixGroupId` | `about.group.product_object_id` |   
`properties.AdditionalFields.ProcessPosixFilePermissions` | `additional.fields[ProcessPosixFilePermissions]` | Iterate through log field `properties.AdditionalFields.ProcessPosixFilePermissions`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `ProcessPosixFilePermissions_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.ProcessPosixFilePermissions` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`properties.AdditionalFields.ProcessPosixFileUserOwner.AadUserUpn` | `about.user.email_addresses` |   
`properties.AdditionalFields.ProcessPosixFileUserOwner.DomainName` | `about.user.attribute.labels[ProcessPosixFileUserOwner_DomainName]` |   
`properties.AdditionalFields.ProcessPosixFileUserOwner.LogonId` | `about.user.attribute.labels[ProcessPosixFileUserOwner_LogonId]` |   
`properties.AdditionalFields.ProcessPosixFileUserOwner.Name` | `about.user.user_display_name` |   
`properties.AdditionalFields.ProcessPosixFileUserOwner.PosixUserId` | `about.user.userid` |   
`properties.AdditionalFields.ProcessPosixFileUserOwner.PrimaryPosixGroup.Name` | `about.user.group_identifiers` |   
`properties.AdditionalFields.ProcessPosixFileUserOwner.PrimaryPosixGroup.PosixGroupId` | `about.user.groupid` |   
`properties.AdditionalFields.ProcessPosixFileUserOwner.Sid` | `about.user.windows_sid` |   
`properties.AdditionalFields.ProcessPosixProcessGroupId` | `target.process.pgid` |   
`properties.AdditionalFields.uniqueEventsAggregated` | `additional.fields[uniqueEventsAggregated]` |   
  
### AdditionalFields mapping reference: MICROSOFT DEFENDER ENDPOINT - DeviceNetworkEvents

The following table lists the `AdditionalFields` log fields for the `DeviceNetworkEvents` log type and their corresponding UDM fields:   
  


ActionType | Log field | UDM mapping | Logic  
---|---|---|---  
`SslConnectionInspected` | `properties.AdditionalFields.direction` | `network.direction` | If the `properties.AdditionalFields.direction` log field value is equal to `In`, then the `network.direction` UDM field is set to `INBOUND`.  
  
Otherwise, if the `properties.AdditionalFields.direction` log field value is equal to `Out`, then the `network.direction` UDM field is set to `OUTBOUND`.  
`SslConnectionInspected` | `properties.AdditionalFields.version` | `network.tls.version` |   
`SslConnectionInspected` | `properties.AdditionalFields.curve` | `network.tls.curve` |   
`SslConnectionInspected` | `properties.AdditionalFields.server_name` | `network.tls.client.server_name` |   
`SslConnectionInspected` | `properties.AdditionalFields.server_name` | `target.hostname` |   
`SslConnectionInspected` | `properties.AdditionalFields.resumed` | `network.tls.resumed` |   
`SslConnectionInspected` | `properties.AdditionalFields.established` | `network.tls.established` |   
`SslConnectionInspected` | `properties.AdditionalFields.subject` | `network.tls.server.certificate.subject` |   
`SslConnectionInspected` | `properties.AdditionalFields.uid` | `additional.fields[uid]` |   
`SslConnectionInspected` | `properties.AdditionalFields.issuer` | `network.tls.server.certificate.issuer` |   
`SslConnectionInspected` | `properties.AdditionalFields.cipher` | `network.tls.cipher` |   
`SslConnectionInspected` | `properties.AdditionalFields.ts` | `additional.fields[ts]` |   
`SslConnectionInspected` | `properties.AdditionalFields.next_protocol` | `network.tls.next_protocol` |   
`SslConnectionInspected` | `properties.AdditionalFields.last_alert` | `additional.fields[last_alert]` |   
`SslConnectionInspected` | `properties.AdditionalFields.client_subject` | `network.tls.client.certificate.subject` |   
`SslConnectionInspected` | `properties.AdditionalFields.client_issuer` | `network.tls.client.certificate.issuer` |   
`SslConnectionInspected` | `properties.AdditionalFields.ja4` | `network.tls.client.ja4` |   
`SslConnectionInspected` | `properties.AdditionalFields.ja4s` | `network.tls.server.ja4s` |   
`SslConnectionInspected` | `properties.AdditionalFields.ja3` | `network.tls.client.ja3` |   
`SslConnectionInspected` | `properties.AdditionalFields.ja3s` | `network.tls.server.ja3s` |   
`DnsConnectionInspected` | `properties.AdditionalFields.direction` | `network.direction` | If the `properties.AdditionalFields.direction` log field value is equal to `In`, then the `network.direction` UDM field is set to `INBOUND`.  
  
Otherwise, if the `properties.AdditionalFields.direction` log field value is equal to `Out`, then the `network.direction` UDM field is set to `OUTBOUND`.  
`DnsConnectionInspected` | `` | `network.application_protocol` | The `network.application_protocol` UDM field is set to `DNS`.  
`DnsConnectionInspected` | `properties.AdditionalFields.trans_id` | `network.dns.id` |   
`DnsConnectionInspected` | `properties.AdditionalFields.rtt` | `network.session_duration` |   
`DnsConnectionInspected` | `properties.AdditionalFields.query` | `target.hostname` |   
`DnsConnectionInspected` | `properties.AdditionalFields.query` | `network.dns.questions.name` |   
`DnsConnectionInspected` | `properties.AdditionalFields.qclass` | `network.dns.questions.class` |   
`DnsConnectionInspected` | `properties.AdditionalFields.qclass_name` | `additional.fields[qclass_name]` |   
`DnsConnectionInspected` | `properties.AdditionalFields.qtype` | `network.dns.questions.type` |   
`DnsConnectionInspected` | `properties.AdditionalFields.qtype_name` | `additional.fields[qtype_name]` |   
`DnsConnectionInspected` | `properties.AdditionalFields.rcode` | `network.dns.response_code` |   
`DnsConnectionInspected` | `properties.AdditionalFields.uid` | `additional.fields[uid]` |   
`DnsConnectionInspected` | `properties.AdditionalFields.rcode_name` | `additional.fields[rcode_name]` |   
`DnsConnectionInspected` | `properties.AdditionalFields.AA` | `network.dns.authoritative` |   
`DnsConnectionInspected` | `properties.AdditionalFields.TC` | `network.dns.truncated` |   
`DnsConnectionInspected` | `properties.AdditionalFields.RD` | `network.dns.recursion_desired` |   
`DnsConnectionInspected` | `properties.AdditionalFields.RA` | `network.dns.recursion_available` |   
`DnsConnectionInspected` | `properties.AdditionalFields.answers` | `network.dns.answers.data` | The `properties.AdditionalFields.answers` log field is set to a value generated from the template `{"properties.AdditionalFields.answers":%{properties.AdditionalFields.answers}}`, where `%{properties.AdditionalFields.answers}` is replaced with the value of the `properties.AdditionalFields.answers` log field. The `properties.AdditionalFields.answers` log field is parsed as JSON. The `properties.AdditionalFields.TTLs` log field is set to a value generated from the template `{"properties.AdditionalFields.TTLs":%{properties.AdditionalFields.TTLs}}`, where `%{properties.AdditionalFields.TTLs}` is replaced with the value of the `properties.AdditionalFields.TTLs` log field. The `properties.AdditionalFields.TTLs` log field is parsed as JSON.  
  
Iterate through log field `properties.AdditionalFields.answers`:  
  
Iterate through log field `properties.AdditionalFields.TTLs`:  
  
If the `index` value is equal to the `index1` log field value, then the `properties.AdditionalFields.answers` log field is mapped to the `network.dns.answers.data` UDM field.  
`DnsConnectionInspected` | `properties.AdditionalFields.TTLs` | `network.dns.answers.ttl` | Iterate through log field `properties.AdditionalFields.answers`:  
  
Iterate through log field `properties.AdditionalFields.TTLs`:  
  
If the `index` value is equal to the `index1` log field value, then the `properties.AdditionalFields.TTLs` log field is mapped to the `network.dns.answers.ttl` UDM field.  
`DnsConnectionInspected` | `properties.AdditionalFields.rejected` | `security_result.action` | If the `properties.AdditionalFields.rejected` log field value is equal to `false`, then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, the `security_result.action` UDM field is set to `BLOCK`.  
`DnsConnectionInspected` | `properties.AdditionalFields.ts` | `additional.fields[ts]` |   
`HttpConnectionInspected` | `properties.AdditionalFields.direction` | `network.direction` | If the `properties.AdditionalFields.direction` log field value is equal to `In`, then the `network.direction` UDM field is set to `INBOUND`.  
  
Otherwise, if the `properties.AdditionalFields.direction` log field value is equal to `Out`, then the `network.direction` UDM field is set to `OUTBOUND`.  
`HttpConnectionInspected` | `properties.AdditionalFields.host` | `target.hostname` |   
`HttpConnectionInspected` | `properties.AdditionalFields.method` | `network.http.method` |   
`HttpConnectionInspected` | `properties.AdditionalFields.request_body_len` | `network.sent_bytes` |   
`HttpConnectionInspected` | `properties.AdditionalFields.response_body_len` | `network.received_bytes` |   
`HttpConnectionInspected` | `properties.AdditionalFields.status_code` | `network.http.response_code` |   
`HttpConnectionInspected` | `properties.AdditionalFields.status_msg` | `security_result.description` |   
`HttpConnectionInspected` | `properties.AdditionalFields.tags` | `additional.fields[tags]` |   
`HttpConnectionInspected` | `properties.AdditionalFields.trans_depth` | `additional.fields[trans_depth]` |   
`HttpConnectionInspected` | `properties.AdditionalFields.uri` | `additional.fields[uri]` |   
`HttpConnectionInspected` | `properties.AdditionalFields.user_agent` | `network.http.user_agent` |   
`HttpConnectionInspected` | `` | `network.application_protocol` | The `network.application_protocol` UDM field is set to `HTTP`.  
`HttpConnectionInspected` | `properties.AdditionalFields.version` | `network.application_protocol_version` |   
`HttpConnectionInspected` | `properties.AdditionalFields.proxied` | `additional.fields[proxied]` |   
`HttpConnectionInspected` | `properties.AdditionalFields.resp_filenames` | `target.file.names` |   
`HttpConnectionInspected` | `properties.AdditionalFields.referrer` | `network.http.referral_url` |   
`HttpConnectionInspected` | `properties.AdditionalFields.username` | `about.user.user_display_name` |   
`HttpConnectionInspected` | `properties.AdditionalFields.info_code` | `security_result.detection_fields[info_code]` |   
`HttpConnectionInspected` | `properties.AdditionalFields.info_msg` | `security_result.detection_fields[info_msg]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.AadUserUpn` | `additional.fields[InitiatingProcessPosixEffectiveUser_AadUserUpn]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.DomainName` | `additional.fields[InitiatingProcessPosixEffectiveUser_DomainName]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.LogonId` | `additional.fields[InitiatingProcessPosixEffectiveUser_LogonId]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.Name` | `additional.fields[InitiatingProcessPosixEffectiveUser_Name]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.PosixUserId` | `principal.process.euid` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.PrimaryPosixGroup.Name` | `additional.fields[InitiatingProcessPosixEffectiveUser_PrimaryPosixGroup_Name]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.PrimaryPosixGroup.PosixGroupId` | `additional.fields[InitiatingProcessPosixEffectiveUser_PrimaryPosixGroup_PosixGroupId]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixEffectiveUser.Sid` | `additional.fields[InitiatingProcessPosixEffectiveUser_Sid]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixEffectiveGroup.Name` | `additional.fields[InitiatingProcessPosixEffectiveGroup_Name]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixEffectiveGroup.PosixGroupId` | `principal.process.egid` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixProcessGroupId` | `principal.process.pgid` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixSessionId` | `additional.fields[InitiatingProcessPosixSessionId]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessCurrentWorkingDirectory` | `additional.fields[InitiatingProcessCurrentWorkingDirectory]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixFilePermissions` | `additional.fields[InitiatingProcessPosixFilePermissions]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixRealUser.AadUserUpn` | `additional.fields[InitiatingProcessPosixRealUser_AadUserUpn]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixRealUser.DomainName` | `additional.fields[InitiatingProcessPosixRealUser_DomainName]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixRealUser.LogonId` | `additional.fields[InitiatingProcessPosixRealUser_LogonId]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixRealUser.Name` | `additional.fields[InitiatingProcessPosixRealUser_Name]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixRealUser.PosixUserId` | `principal.process.ruid` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixRealUser.PrimaryPosixGroup.Name` | `additional.fields[InitiatingProcessPosixRealUser_PrimaryPosixGroup_Name]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixRealUser.PrimaryPosixGroup.PosixGroupId` | `additional.fields[InitiatingProcessPosixRealUser_PrimaryPosixGroup_PosixGroupId]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixRealUser.Sid` | `additional.fields[InitiatingProcessPosixRealUser_Sid]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixUserOwner.AadUserUpn` | `additional.fields[InitiatingProcessPosixUserOwner_AadUserUpn]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixUserOwner.DomainName` | `additional.fields[InitiatingProcessPosixUserOwner_DomainName]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixUserOwner.LogonId` | `additional.fields[InitiatingProcessPosixUserOwner_LogonId]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixUserOwner.Name` | `additional.fields[InitiatingProcessPosixUserOwner_Name]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixUserOwner.PosixUserId` | `additional.fields[InitiatingProcessPosixUserOwner_PosixUserId]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixUserOwner.PrimaryPosixGroup.Name` | `additional.fields[InitiatingProcessPosixUserOwner_PrimaryPosixGroup_Name]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixUserOwner.PrimaryPosixGroup.PosixGroupId` | `additional.fields[InitiatingProcessPosixUserOwner_PrimaryPosixGroup_PosixGroupId]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixUserOwner.Sid` | `additional.fields[InitiatingProcessPosixUserOwner_Sid]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixGroupOwner.Name` | `additional.fields[InitiatingProcessPosixGroupOwner_Name]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixGroupOwner.PosixGroupId` | `additional.fields[InitiatingProcessPosixGroupOwner_PosixGroupId]` |   
`ConnectionRequest/ConnectionFailed/InboundConnectionAccepted/ConnectionSuccess` | `properties.AdditionalFields.InitiatingProcessPosixAttachedTerminal` | `principal.process.tty` |   
`IcmpConnectionInspected` | `properties.AdditionalFields.direction` | `network.direction` | If the `properties.AdditionalFields.direction` log field value is equal to `In`, then the `network.direction` UDM field is set to `INBOUND`.  
  
Otherwise, if the `properties.AdditionalFields.direction` log field value is equal to `Out`, then the `network.direction` UDM field is set to `OUTBOUND`.  
`IcmpConnectionInspected` | `properties.AdditionalFields.conn_state` | `additional.fields[conn_state]` |   
`IcmpConnectionInspected` | `properties.AdditionalFields.duration` | `network.session_duration` |   
`IcmpConnectionInspected` | `properties.AdditionalFields.missed_bytes` | `additional.fields[missed_bytes]` |   
`IcmpConnectionInspected` | `properties.AdditionalFields.orig_bytes` | `network.sent_bytes` |   
`IcmpConnectionInspected` | `properties.AdditionalFields.orig_ip_bytes` | `additional.fields[orig_ip_bytes]` |   
`IcmpConnectionInspected` | `properties.AdditionalFields.orig_pkts` | `network.sent_packets` |   
`IcmpConnectionInspected` | `properties.AdditionalFields.resp_bytes` | `network.received_bytes` |   
`IcmpConnectionInspected` | `properties.AdditionalFields.resp_ip_bytes` | `additional.fields[resp_ip_bytes]` |   
`IcmpConnectionInspected` | `properties.AdditionalFields.resp_pkts` | `network.received_packets` |   
`IcmpConnectionInspected` | `properties.AdditionalFields.uid` | `additional.fields[uid]` |   
`NetworkSignatureInspected` | `properties.AdditionalFields.SignatureName` | `security_result.rule_name` |   
`NetworkSignatureInspected` | `properties.AdditionalFields.SignatureMatchedContent` | `additional.fields[SignatureMatchedContent]` |   
`NetworkSignatureInspected` | `properties.AdditionalFields.SamplePacketContent` | `additional.fields[SamplePacketContent]` | Iterate through log field `properties.AdditionalFields.SamplePacketContent`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `SamplePacketContent_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.SamplePacketContent` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`NtlmAuthenticationInspected` | `properties.AdditionalFields.direction` | `network.direction` | If the `properties.AdditionalFields.direction` log field value is equal to `In`, then the `network.direction` UDM field is set to `INBOUND`.  
  
Otherwise, if the `properties.AdditionalFields.direction` log field value is equal to `Out`, then the `network.direction` UDM field is set to `OUTBOUND`.  
`NtlmAuthenticationInspected` | `properties.AdditionalFields.username` | `target.user.userid` |   
`NtlmAuthenticationInspected` | `properties.AdditionalFields.hostname` | `principal.hostname` | If the `properties.DeviceName` log field value is empty, then the `properties.AdditionalFields.hostname` log field is mapped to the `principal.hostname` UDM field.  
  
Otherwise, the `principal.asset.attribute.labels.key` UDM field is set to `hostname` and the `properties.AdditionalFields.hostname` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`NtlmAuthenticationInspected` | `properties.AdditionalFields.domainname` | `principal.administrative_domain` | If the `properties.InitiatingProcessAccountDomain` log field value is empty, then the `properties.AdditionalFields.domainname` log field is mapped to the `principal.administrative_domain` UDM field.  
  
Otherwise, the `principal.asset.attribute.labels.key` UDM field is set to `domainname` and the `properties.AdditionalFields.domainname` log field is mapped to the `principal.asset.attribute.labels.value` UDM field.  
`NtlmAuthenticationInspected` | `properties.AdditionalFields.server_nb_computer_name` | `target.asset.attribute.labels[server_nb_computer_name]` |   
`NtlmAuthenticationInspected` | `properties.AdditionalFields.server_nb_domain_name` | `target.asset.attribute.labels[server_nb_domain_name]` |   
`NtlmAuthenticationInspected` | `properties.AdditionalFields.server_dns_computer_name` | `target.hostname` |   
`NtlmAuthenticationInspected` | `properties.AdditionalFields.uid` | `additional.fields[uid]` |   
`NtlmAuthenticationInspected` | `properties.AdditionalFields.success` | `security_result.action` | If the `properties.AdditionalFields.success` log field value is equal to `true`, then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, the `security_result.action` UDM field is set to `BLOCK`.  
`NtlmAuthenticationInspected` | `properties.AdditionalFields.server_version` | `additional.fields[server_version]` |   
`NtlmAuthenticationInspected` | `properties.AdditionalFields.ts` | `additional.fields[ts]` |   
`NtlmAuthenticationInspected` | `properties.AdditionalFields.server_dns_domain_name` | `target.administrative_domain` |   
`NtlmAuthenticationInspected` | `properties.AdditionalFields.server_tree_name` | `additional.fields[server_tree_name]` |   
`ConnectionAcknowledged` | `properties.AdditionalFields.Destination Mac` | `target.mac` |   
`ConnectionAcknowledged` | `properties.AdditionalFields.Packet Size` | `network.sent_bytes` |   
`ConnectionAcknowledged` | `properties.AdditionalFields.Source Mac` | `principal.mac` |   
`ConnectionAcknowledged` | `properties.AdditionalFields.Tcp Flags` | `additional.fields[Tcp Flags]` |   
`ConnectionAttempt` | `properties.AdditionalFields.Destination Mac` | `target.mac` |   
`ConnectionAttempt` | `properties.AdditionalFields.Packet Size` | `network.sent_bytes` |   
`ConnectionAttempt` | `properties.AdditionalFields.Source Mac` | `principal.mac` |   
`ConnectionAttempt` | `properties.AdditionalFields.Tcp Flags` | `additional.fields[Tcp Flags]` |   
`SshConnectionInspected` | `properties.AdditionalFields.direction` | `network.direction` | If the `properties.AdditionalFields.direction` log field value is equal to `In`, then the `network.direction` UDM field is set to `INBOUND`.  
  
Otherwise, if the `properties.AdditionalFields.direction` log field value is equal to `Out`, then the `network.direction` UDM field is set to `OUTBOUND`.  
`SshConnectionInspected` | `properties.AdditionalFields.auth_attempts` | `additional.fields[auth_attempts]` |   
`SshConnectionInspected` | `properties.AdditionalFields.auth_success` | `security_result.action` | If the `properties.AdditionalFields.auth_success` log field value is equal to `true`, then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, the `security_result.action` UDM field is set to `BLOCK`.  
`SshConnectionInspected` | `properties.AdditionalFields.client` | `principal.application` |   
`SshConnectionInspected` | `properties.AdditionalFields.host_key` | `additional.fields[host_key]` |   
`SshConnectionInspected` | `properties.AdditionalFields.server` | `target.asset.software.name` |   
`SshConnectionInspected` | `` | `network.application_protocol` | The `network.application_protocol` UDM field is set to `SSH`.  
`SshConnectionInspected` | `properties.AdditionalFields.version` | `network.application_protocol_version` |   
`SshConnectionInspected` | `properties.AdditionalFields.uid` | `additional.fields[uid]` |   
`InboundInternetScanInspected` | `properties.AdditionalFields.PublicScannedPort` | `target.nat_port` |   
`InboundInternetScanInspected` | `properties.AdditionalFields.PublicScannedIp` | `target.nat_ip` |   
`InboundInternetScanInspected` | `` | `network.direction` | The `network.direction` UDM field is set to `INBOUND`.  
`FtpConnectionInspected` | `properties.AdditionalFields.direction` | `network.direction` | If the `properties.AdditionalFields.direction` log field value is equal to `In`, then the `network.direction` UDM field is set to `INBOUND`.  
  
Otherwise, if the `properties.AdditionalFields.direction` log field value is equal to `Out`, then the `network.direction` UDM field is set to `OUTBOUND`.  
`FtpConnectionInspected` | `properties.AdditionalFields.user` | `target.user.userid` |   
`FtpConnectionInspected` | `properties.AdditionalFields.reply_msg` | `additional.fields[reply_msg]` |   
`FtpConnectionInspected` | `properties.AdditionalFields.reply_code` | `additional.fields[reply_code]` |   
`FtpConnectionInspected` | `properties.AdditionalFields.cwd` | `additional.fields[cwd]` |   
`FtpConnectionInspected` | `properties.AdditionalFields.command` | `network.ftp.command` |   
`FtpConnectionInspected` | `properties.AdditionalFields.arg` | `additional.fields[arg]` |   
`FtpConnectionInspected` | `properties.AdditionalFields.mime_type` | `target.file.mime_type` |   
`FtpConnectionInspected` | `properties.AdditionalFields.uid` | `additional.fields[uid]` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.direction` | `network.direction` | If the `properties.AdditionalFields.direction` log field value is equal to `In`, then the `network.direction` UDM field is set to `INBOUND`.  
  
Otherwise, if the `properties.AdditionalFields.direction` log field value is equal to `Out`, then the `network.direction` UDM field is set to `OUTBOUND`.  
`SmtpConnectionInspected` | `` | `network.application_protocol` | The `network.application_protocol` UDM field is set to `SMTP`.  
`SmtpConnectionInspected` | `properties.AdditionalFields.cc` | `network.email.cc` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.date` | `additional.fields[date]` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.from` | `network.email.from` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.fuids` | `additional.fields[fuids]` | Iterate through log field `properties.AdditionalFields.fuids`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `fuids_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.fuids` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`SmtpConnectionInspected` | `properties.AdditionalFields.helo` | `network.smtp.helo` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.last_reply` | `network.smtp.server_response` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.mailfrom` | `network.smtp.mail_from` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.msg_id` | `network.email.mail_id` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.path` | `additional.fields[path]` | Iterate through log field `properties.AdditionalFields.path`:  
  
The `additional.fields.key` UDM field is set to a value generated from the template `path_%{index}`, where `%{index}` is replaced with the value of the `index` log field and the `properties.AdditionalFields.path` log field is mapped to the `additional.fields.value.string_value` UDM field.  
`SmtpConnectionInspected` | `properties.AdditionalFields.rcptto` | `network.smtp.rcpt_to` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.subject` | `network.email.subject` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.tls` | `network.smtp.is_tls` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.to` | `network.email.to` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.trans_depth` | `additional.fields[trans_depth]` |   
`SmtpConnectionInspected` | `properties.AdditionalFields.uid` | `additional.fields[uid]` |   
`KerberosConnectionInspected` | `properties.AdditionalFields.direction` | `network.direction` | If the `properties.AdditionalFields.direction` log field value is equal to `In`, then the `network.direction` UDM field is set to `INBOUND`.  
  
Otherwise, if the `properties.AdditionalFields.direction` log field value is equal to `Out`, then the `network.direction` UDM field is set to `OUTBOUND`.  
`KerberosConnectionInspected` | `properties.AdditionalFields.success` | `security_result.action` | If the `properties.AdditionalFields.success` log field value is equal to `true`, then the `security_result.action` UDM field is set to `ALLOW`.  
  
Otherwise, if the `properties.AdditionalFields.success` log field value is equal to `false`, then the `security_result.action` UDM field is set to `BLOCK`.  
`KerberosConnectionInspected` | `properties.AdditionalFields.ticketHash` | `additional.fields[ticketHash]` |   
`KerberosConnectionInspected` | `properties.AdditionalFields.cipher` | `additional.fields[cipher]` |   
`KerberosConnectionInspected` | `properties.AdditionalFields.requestType` | `additional.fields[requestType]` |   
`KerberosConnectionInspected` | `properties.AdditionalFields.service` | `target.application` |   
`KerberosConnectionInspected` | `properties.AdditionalFields.uid` | `additional.fields[uid]` |   
`KerberosConnectionInspected` | `properties.AdditionalFields.ts` | `additional.fields[ts]` |   
`ConnectionSuccessAggregatedReport` | `properties.AdditionalFields.uniqueEventsAggregated` | `additional.fields[uniqueEventsAggregated]` |   
`ConnectionFailedAggregatedReport` | `properties.AdditionalFields.uniqueEventsAggregated` | `additional.fields[uniqueEventsAggregated]` |   
  
## UDM Mapping Delta

### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT

**Note:** In this delta, "Old UDM Mapping" refers to releases before April 28th, 2026. Versions released after April 28th, 2026 include the following "New UDM Mapping". This version was promoted to be part of the default parser version in June 2026.

The following tables list the delta between the Old UDM Mapping of `Microsoft Defender Endpoint` and the New UDM Mapping of `Microsoft Defender Endpoint`.

### UDM Mapping Delta reference: DeviceEvents Event Identifier to Event Type

The following table lists the delta of `DeviceEvents` log action types and their corresponding UDM event types.

Event Identifier | Old UDM Event Type Mapping | New UDM Event Type Mapping  
---|---|---  
`AntivirusDefinitionsUpdateFailed` | `SCAN_HOST` | `SETTING_MODIFICATION`  
`AntivirusEmergencyUpdatesInstalled` | `SCAN_HOST` | `SETTING_MODIFICATION`  
`AntivirusTroubleshootModeEvent` | `SCAN_HOST` | `STATUS_UPDATE`  
`AppControlCodeIntegrityDriverRevoked` | `SCAN_HOST` | `SCAN_FILE`  
`AppControlCodeIntegrityImageAudited` | `SCAN_HOST` | `SCAN_FILE`  
`AppControlCodeIntegrityImageRevoked` | `SCAN_HOST` | `SCAN_FILE`  
`AppControlCodeIntegrityOriginAllowed` | `SCAN_HOST` | `SCAN_FILE`  
`AppControlCodeIntegrityOriginAudited` | `SCAN_HOST` | `SCAN_FILE`  
`AppControlCodeIntegrityOriginBlocked` | `SCAN_HOST` | `SCAN_FILE`  
`AppControlCodeIntegrityPolicyAudited` | `SCAN_HOST` | `SCAN_FILE`  
`AppControlCodeIntegrityPolicyBlocked` | `SCAN_HOST` | `SCAN_FILE`  
`AppControlCodeIntegrityPolicyLoaded` | `SCAN_HOST` | `SCAN_FILE`  
`AppControlCodeIntegritySigningInformation` | `SCAN_HOST` | `GENERIC_EVENT`  
`AppControlPolicyApplied` | `SCAN_HOST` | `SETTING_MODIFICATION`  
`AppGuardBrowseToUrl` | `SCAN_HOST` | `NETWORK_UNCATEGORIZED`  
`AppGuardCreateContainer` | `SCAN_HOST` | `PROCESS_LAUNCH`  
`AppGuardLaunchedWithUrl` | `SCAN_HOST` | `PROCESS_LAUNCH`  
`AppGuardResumeContainer` | `SCAN_HOST` | `PROCESS_UNCATEGORIZED`  
`AppGuardStopContainer` | `SCAN_HOST` | `PROCESS_TERMINATION`  
`AppGuardSuspendContainer` | `SCAN_HOST` | `PROCESS_UNCATEGORIZED`  
`AppLockerBlockExecutable` | `PROCESS_UNCATEGORIZED` | `SCAN_HOST`  
`AppLockerBlockPackagedApp` | `STATUS_UPDATE` | `SCAN_HOST`  
`AppLockerBlockPackagedAppInstallation` | `STATUS_UPDATE` | `SCAN_HOST`  
`AppLockerBlockScript` | `STATUS_UPDATE` | `SCAN_HOST`  
`AuditPolicyModification` | `SERVICE_MODIFICATION` | `SETTING_MODIFICATION`  
`BitLockerAuditCompleted` | `SERVICE_UNSPECIFIED` | `STATUS_UPDATE`  
`BluetoothPolicyTriggered` | `STATUS_UPDATE` | `SCAN_HOST`  
`ContainedDeviceConnectionBlocked` | `NETWORK_UNCATEGORIZED` | `NETWORK_CONNECTION`  
`ControlFlowGuardViolation` | `STATUS_UPDATE` | `SCAN_HOST`  
`DeviceBootAttestationInfo` | `STATUS_UPDATE` | `GENERIC_EVENT`  
`DirectoryServiceObjectCreated` | `SERVICE_MODIFICATION` | `RESOURCE_CREATION`  
`DirectoryServiceObjectModified` | `SERVICE_MODIFICATION` | `RESOURCE_WRITTEN`  
`DpapiAccessed` | `GENERIC_EVENT` | `PROCESS_UNCATEGORIZED`  
`GetAsyncKeyStateApiCall` | `STATUS_UPDATE` | `PROCESS_UNCATEGORIZED`  
`GetClipboardData` | `STATUS_UPDATE` | `PROCESS_UNCATEGORIZED`  
`LdapSearch` | `STATUS_UPDATE` | `RESOURCE_READ`  
`NetworkShareObjectAccessChecked` | `NETWORK_UNCATEGORIZED` | `RESOURCE_READ`  
`NetworkShareObjectAdded` | `NETWORK_UNCATEGORIZED` | `RESOURCE_CREATION`  
`NetworkShareObjectDeleted` | `NETWORK_UNCATEGORIZED` | `RESOURCE_DELETION`  
`NetworkShareObjectModified` | `NETWORK_UNCATEGORIZED` | `RESOURCE_WRITTEN`  
`PnpDeviceAllowed` | `DEVICE_CONFIG_UPDATE` | `SCAN_HOST`  
`PnpDeviceBlocked` | `STATUS_UPDATE` | `SCAN_HOST`  
`PnpDeviceConnected` | `STATUS_UPDATE` | `DEVICE_CONFIG_UPDATE`  
`PrintJobBlocked` | `STATUS_UPDATE` | `SCAN_UNCATEGORIZED`  
`QueueUserApcRemoteApiCall` | `PROCESS_LAUNCH` | `PROCESS_UNCATEGORIZED`  
`RemoteWmiOperation` | `NETWORK_CONNECTION` | `PROCESS_UNCATEGORIZED`  
`RemovableStoragePolicyTriggered` | `STATUS_UPDATE` | `PROCESS_UNCATEGORIZED`  
`SmartScreenAppWarning` | `SCAN_UNCATEGORIZED` | `SCAN_HOST`  
`SmartScreenExploitWarning` | `SCAN_UNCATEGORIZED` | `SCAN_HOST`  
`SmartScreenUrlWarning` | `SCAN_UNCATEGORIZED` | `SCAN_HOST`  
`SmartScreenUserOverride` | `SCAN_UNCATEGORIZED` | `SETTING_MODIFICATION`  
`WmiBindEventFilterToConsumer` | `STATUS_UPDATE` | `PROCESS_UNCATEGORIZED`  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceEvents

The following table lists the delta of log fields for the `DeviceEvents` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`properties.DeviceId` | `principal.asset_id`  
`principal.asset.asset_id` | If the `properties.ActionType` log field contains one of the following values, then `DeviceID:%{properties.DeviceId}` is mapped to the `target.asset_id` and `target.asset.asset_id` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, `DeviceID:%{properties.DeviceId}` is mapped to the `principal.asset_id` and `principal.asset.asset_id` UDM fields.  
`properties.DeviceName` | `principal.hostname`  
`principal.asset.hostname` | If the `properties.ActionType` log field contains one of the following values, then the `properties.DeviceName` log field is mapped to the `target.hostname` and `target.asset.hostname` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.DeviceName` log field is mapped to the `principal.hostname` and `principal.asset.hostname` UDM fields.  
`properties.LocalIP` | `principal.ip`  
`principal.asset.ip` | If the `properties.ActionType` log field contains one of the following values, then the `properties.LocalIP` log field is mapped to the `target.ip` and `target.asset.ip` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.LocalIP` log field is mapped to the `principal.ip` and `principal.asset.ip` UDM fields.  
`properties.LocalPort` | `principal.port` | If the `properties.ActionType` log field contains one of the following values, then the `properties.LocalPort` log field is mapped to the `target.port` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.LocalPort` log field is mapped to the `principal.port` UDM field.  
`properties.FolderPath` | `target.file.full_path`  
`target.process.file.full_path` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

then if the `properties.FolderPath` log field value matches the regular expression pattern `the `properties.FileName` log field value `, then `properties.FolderPath` log field is mapped to the `target.process.file.full_path` UDM field, else `%{properties.FolderPath}\%{properties.FileName}` is mapped to the `target.process.file.full_path` UDM field.  
Otherwise, if the `properties.FolderPath` log field value matches the regular expression pattern `the `properties.FileName` log field value `, then `properties.FolderPath` log field is mapped to the `target.file.full_path` UDM field, else `%{properties.FolderPath}\%{properties.FileName}` is mapped to the `target.file.full_path` UDM field.  
`properties.MD5` | `target.file.md5`  
`target.process.file.md5` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

and if the `properties.MD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.MD5` log field is mapped to the `target.process.file.md5` UDM field.  
Otherwise, if the `properties.MD5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.MD5` log field is mapped to the `target.file.md5` UDM field.  
`properties.FileName` | `target.file.names`  
`target.process.file.names` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

then `properties.FileName` log field is mapped to the `target.process.file.names` UDM field.  
Otherwise, `properties.FileName` log field is mapped to the `target.file.names` UDM field.  
`properties.SHA1` | `target.file.sha1`  
`target.process.file.sha1` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

and if the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then `properties.SHA1` log field is mapped to the `target.process.file.sha1` UDM field.  
Otherwise, if the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then `properties.SHA1` log field is mapped to the `target.file.sha1` UDM field.  
`properties.SHA256` | `target.file.sha256`  
`target.process.file.sha256` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

and if the `properties.SHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then `properties.SHA256` log field is mapped to the `target.process.file.sha256` UDM field.  
Otherwise, if the `properties.SHA256` log field value matches the regular expression pattern `^[a-f0-9]{64}$`, then `properties.SHA256` log field is mapped to the `target.file.sha256` UDM field.  
`properties.FileSize` | `target.file.size`  
`target.process.file.size` | If the `properties.ActionType` log field contains one of the following values:

  * `AmsiScriptDetection`
  * `AppGuardCreateContainer`
  * `AppGuardLaunchedWithUrl`
  * `AppGuardResumeContainer`
  * `AppGuardStopContainer`
  * `AppGuardSuspendContainer`
  * `ClrUnbackedModuleLoaded`
  * `CreateRemoteThreadApiCall`
  * `DpapiAccessed`
  * `DriverLoad`
  * `GetAsyncKeyStateApiCall`
  * `GetClipboardData`
  * `MemoryRemoteProtect`
  * `NamedPipeEvent`
  * `NtAllocateVirtualMemoryApiCall`
  * `NtAllocateVirtualMemoryRemoteApiCall`
  * `NtMapViewOfSectionRemoteApiCall`
  * `NtProtectVirtualMemoryApiCall`
  * `OpenProcessApiCall`
  * `PowerShellCommand`
  * `ProcessCreatedUsingWmiQuery`
  * `ProcessPrimaryTokenModified`
  * `PTraceDetected`
  * `QueueUserApcRemoteApiCall`
  * `ReadProcessMemoryApiCall`
  * `RemoteWmiOperation`
  * `RemovableStoragePolicyTriggered`
  * `ScriptContent`
  * `SetThreadContextRemoteApiCall`
  * `WmiBindEventFilterToConsumer`
  * `WriteProcessMemoryApiCall`
  * `WriteToLsassProcessMemory`
  * `AsrAdobeReaderChildProcessAudited`
  * `AsrAdobeReaderChildProcessBlocked`
  * `AsrAdobeReaderChildProcessWarnBypassed`
  * `AsrOfficeChildProcessAudited`
  * `AsrOfficeChildProcessBlocked`
  * `AsrOfficeChildProcessWarnBypassed`
  * `AsrOfficeCommAppChildProcessAudited`
  * `AsrOfficeCommAppChildProcessBlocked`
  * `AsrOfficeCommAppChildProcessWarnBypassed`
  * `AsrOfficeProcessInjectionAudited`
  * `AsrOfficeProcessInjectionBlocked`
  * `AsrOfficeProcessInjectionWarnBypassed`
  * `AsrPsexecWmiChildProcessAudited`
  * `AsrPsexecWmiChildProcessBlocked`
  * `AsrPsexecWmiChildProcessWarnBypassed`
  * `AsrUntrustedUsbProcessAudited`
  * `AsrUntrustedUsbProcessBlocked`
  * `AsrUntrustedUsbProcessWarnBypassed`
  * `ExploitGuardChildProcessAudited`
  * `ExploitGuardChildProcessBlocked`

then `properties.FileSize` log field is mapped to the `target.process.file.size` UDM field.  
Otherwise, `properties.FileSize` log field is mapped to the `target.file.size` UDM field.  
`properties.RemoteDeviceName` | `principal.hostname`  
`principal.asset.hostname` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteDeviceName` log field is mapped to the `principal.hostname` and `principal.asset.hostname` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteDeviceName` log field is mapped to the `target.hostname` and `target.asset.hostname` UDM fields.  
`properties.RemoteIP` | `principal.ip`  
`principal.asset.ip` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteIP` log field is mapped to the `principal.ip` and `principal.asset.ip` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteIP` log field is mapped to the `target.ip` and `target.asset.ip` UDM fields.  
`properties.RemotePort` | `principal.port` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemotePort` log field is mapped to the `principal.port` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemotePort` log field is mapped to the `target.port` UDM field.  
`properties.RemoteUrl` | `principal.url` | If the `properties.ActionType` log field contains one of the following values, then the `properties.RemoteUrl` log field is mapped to the `principal.url` UDM field:

  * `RemoteWmiOperation`
  * `ProcessCreatedUsingWmiQuery`

Otherwise, the `properties.RemoteUrl` log field is mapped to the `target.url` UDM field.  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - AlertEvidence

The following table lists the delta of log fields for the `AlertEvidence` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`properties.Application` | `additional.fields[application]` | `principal.application`  
`properties.EvidenceDirection` | `principal.user.attribute.labels[evidence_direction]` | `additional.fields[evidence_direction]`  
`properties.EvidenceRole` | `principal.user.attribute.labels[evidence_role]` | `additional.fields[evidence_role]`  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - AlertInfo

The following table lists the delta of log fields for the `AlertInfo` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`properties.ServiceSource` | `security_result.detection_fields[service_source]` | `principal.application`  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceFileCertificateInfo

The following table lists the delta of log fields for the `DeviceFileCertificateInfo` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`properties.Timestamp` | `metadata.event_timestamp` | `metadata.creation_timestamp`  
`` | The `metadata.event_type` UDM field is set to `STATUS_UPDATE`. | The `metadata.entity_type` UDM field is set to `FILE`.  
`properties.ReportId` | `metadata.product_log_id` | `metadata.product_entity_id`  
`properties.DeviceId` | `principal.asset_id` | The `entity.asset_id` is set to `DeviceID:%{properties.DeviceId}`.  
`properties.SHA1` | `principal.file.sha1` | If the `properties.SHA1` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `properties.SHA1` log field is mapped to the `entity.file.sha1` UDM field.  
`properties.Issuer` | `principal.file.signature_info.sigcheck.signers.cert_issuer` | `entity.file.signature_info.sigcheck.signers.cert_issuer`  
`properties.Signer` | `principal.file.signature_info.sigcheck.signers.name` | `entity.file.signature_info.sigcheck.signers.name`  
`properties.IsSigned` | `principal.file.signature_info.sigcheck.verified` | If the `properties.IsSigned` log field value is equal to `true`, then the `entity.file.signature_info.sigcheck.verified` UDM field is set to `TRUE`.  
Otherwise, the `entity.file.signature_info.sigcheck.verified` UDM field is set to `FALSE`.  
`properties.DeviceName` | `principal.hostname` | `entity.asset.hostname`  
`properties.CertificateSerialNumber` | `additional.fields[certificate_serial_number]` | `entity.file.signature_info.sigcheck.x509.serial_number`  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceFileEvents

The following table lists the delta of log fields for the `DeviceFileEvents` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`properties.FileOriginIP` | `principal.ip` | `src.ip`  
`properties.RequestSourceIP` | `principal.ip` | `src.ip`  
`properties.RequestSourcePort` | `principal.port` | `src.port`  
`properties.FileOriginUrl` | `principal.url` | `src.url`  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceLogonEvents

The following table lists the delta of log fields for the `DeviceLogonEvents` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`properties.LogonId` | `network.session_id` | `extensions.auth.auth_details`  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmInfoGathering

The following table lists the delta of log fields for the `DeviceTvmInfoGathering` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`properties.LastSeenTime` | `security.result.last_discovered_time` | `principal.asset.last_discover_time`  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceRegistryEvents

The following table lists the delta of log fields for the `DeviceRegistryEvents` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`properties.PreviousRegistryValueData` | `principal.registry.registry_value_data` | `src.registry.registry_value_data`  
`properties.PreviousRegistryKey` | `principal.registry.registry_key` | `src.registry.registry_key`  
`properties.PreviousRegistryValueName` | `principal.registry.registry_value_name` | `src.registry.registry_value_name`  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - DeviceTvmSoftwareVulnerabilitiesKB

The following table lists the delta of log fields for the `DeviceTvmSoftwareVulnerabilitiesKB` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`properties.IsExploitAvailable` | `extensions.vulns.vulnerablities.cvss_vector` | `additional.fields[is_exploit_available]`  
`properties.LastModifiedTime` | `extensions.vulns.vulnerabilities.scan_end_time` | `additional.fields[last_modified_time]`  
`properties.PublishedDate` | `extensions.vulns.vulnerabilities.first_found` | `additional.fields[published_date]`  
`properties.AffectedSoftware` | `extensions.vulns.vulnerabilities.description` | `target.application`  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - EmailEvents

The following table lists the delta of log fields for the `EmailEvents` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`properties.SenderMailFromAddress` | `principal.user.attribute.labels[sender_mail_from_address]` | `network.email.reply_to`  
`properties.DeliveryAction` | `additional.fields[delivery_action]` | If the `properties.DeliveryAction` log field is equal to `Delivered`, then the `security_result.action` UDM field is set to `ALLOW`.  
Otherwise, if the `properties.DeliveryAction` log field contains one of the following values:

  * `Junked`
  * `Replaced`

then the `security_result.action` UDM field is set to `ALLOW_WITH_MODIFICATION`.  
Otherwise, if the `properties.DeliveryAction` log field is equal to `Blocked`, then the `security_result.action` UDM field is set to `BLOCK`.  
Otherwise, the `security_result.action` UDM field is set to `UNKNOWN_ACTION`.  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - EmailPostDeliveryEvents

The following table lists the delta of log fields for the `EmailPostDeliveryEvents` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`` | The `metadata.event_type` UDM field is set to `EMAIL_UNCATEGORIZED`. | The `metadata.event_type` UDM field is set to `EMAIL_TRANSACTION`.  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - IdentityInfo

The following table lists the delta of log fields for the `IdentityInfo` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`properties.Type` | `entity.user.attribute.role.name` | If the `properties.Type` log field is equal to `User`, then the `entity.user.account_type` UDM field is set to `DOMAIN_ACCOUNT_TYPE`.  
Otherwise, if the `properties.Type` log field is equal to `ServiceAccount`, then the `entity.user.account_type` UDM field is set to `SERVICE_ACCOUNT_TYPE`.  
`properties.Type` | `entity.user.attribute.role.name` | `entity.user.attribute.labels[type]`  
  
### UDM Mapping Delta reference: MICROSOFT DEFENDER ENDPOINT - IdentityLogonEvents

The following table lists the delta of log fields for the `IdentityLogonEvents` log type and their corresponding UDM fields:

Raw Field | Old UDM Mapping | New UDM Mapping  
---|---|---  
`properties.Application` | `additional.fields[application]` | `principal.application`  
`properties.AccountObjectId` | `additional.fields[account_object_id]` | `principal.user.product_object_id`  
`properties.DestinationDeviceName` | `src.hostname` | `intermediary.hostname`  
`properties.DestinationPort` | `src.port` | `intermediary.port`  
`properties.DestinationIPAddress` | `src.ip` | `intermediary.ip`  
`properties.AccountUpn` | `principal.user.user_display_name` | `principal.user.email_addresses`  
  
## What's next

  * [Data ingestion to Google SecOps](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow)



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-endpoint-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
