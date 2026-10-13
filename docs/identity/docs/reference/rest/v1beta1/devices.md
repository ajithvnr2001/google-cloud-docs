---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/
title: REST Resource: devices \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:46.992443+00:00
---

# REST Resource: devices  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: devices Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Device

A Device within the Cloud Identity Devices API.

Represents a `[Device](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#Device)` known to Google Cloud, independent of the device ownership, type, and whether it is assigned or in use by a user.

Important: Device API scopes require that you use domain-wide delegation to access the API. For more information, see [Set up the Devices API](https://cloud.google.com/identity/docs/how-to/setup-devices).

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "lastSyncTime": string,
      "ownerType": enum ([DeviceOwnership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#DeviceOwnership)),
      "model": string,
      "osVersion": string,
      "deviceType": enum ([DeviceType](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#DeviceType)),
      "serialNumber": string,
      "assetTag": string,
      "imei": string,
      "meid": string,
      "wifiMacAddresses": [
        string
      ],
      "networkOperator": string,
      "manufacturer": string,
      "releaseVersion": string,
      "brand": string,
      "buildNumber": string,
      "kernelVersion": string,
      "basebandVersion": string,
      "enabledDeveloperOptions": boolean,
      "otherAccounts": [
        string
      ],
      "enabledUsbDebugging": boolean,
      "securityPatchTime": string,
      "bootloaderVersion": string,
      "encryptionState": enum ([EncryptionState](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#EncryptionState)),
      "androidSpecificAttributes": {
        object ([AndroidAttributes](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#AndroidAttributes))
      },
      "managementState": enum ([ManagementState](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#ManagementState)),
      "compromisedState": enum ([CompromisedState](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#CompromisedState)),
      "endpointVerificationSpecificAttributes": {
        object ([EndpointVerificationSpecificAttributes](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#EndpointVerificationSpecificAttributes))
      },
      "deviceId": string,
      "unifiedDeviceId": string,
      "hostname": string,
      "clientTypes": [
        enum ([ClientType](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#ClientType))
      ],
      "browserProfiles": [
        {
          object ([BrowserAttributes](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#BrowserAttributes))
        }
      ],
      "windowsSpecificDeviceAttributes": {
        object ([WindowsSpecificDeviceAttributes](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#WindowsSpecificDeviceAttributes))
      },
      "antivirusInfo": [
        {
          object ([AntivirusInfo](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#AntivirusInfo))
        }
      ],
      "osFirewallStatus": enum ([OsFirewallStatus](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#OsFirewallStatus))
    }  
  
Fields  
---  
`name` |  `string` Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: `devices/{deviceId}`, where deviceId is the unique id assigned to the Device.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the Company-Owned device was imported. This field is empty for BYOD devices.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSyncTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Most recent time when device synced with this service.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ownerType` |  `enum (`[DeviceOwnership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#DeviceOwnership)`)` Output only. Whether the device is owned by the company or an individual  
`model` |  `string` Output only. Model name of device. Example: Pixel 3.  
`osVersion` |  `string` Output only. OS version of the device. Example: Android 8.1.0.  
`deviceType` |  `enum (`[DeviceType](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#DeviceType)`)` Output only. Type of device.  
`serialNumber` |  `string` Serial Number of device. Example: HT82V1A01076.  
`assetTag` |  `string` Asset tag of the device.  
`imei` |  `string` Output only. IMEI number of device if GSM device; empty otherwise.  
`meid` |  `string` Output only. MEID number of device if CDMA device; empty otherwise.  
`wifiMacAddresses[]` |  `string` WiFi MAC addresses of device.  
`networkOperator` |  `string` Output only. Mobile or network operator of device, if available.  
`manufacturer` |  `string` Output only. Device manufacturer. Example: Motorola.  
`releaseVersion` |  `string` Output only. OS release version. Example: 6.0.  
`brand` |  `string` Output only. Device brand. Example: Samsung.  
`buildNumber` |  `string` Output only. Build number of the device.  
`kernelVersion` |  `string` Output only. Kernel version of the device.  
`basebandVersion` |  `string` Output only. Baseband version of the device.  
`enabledDeveloperOptions` |  `boolean` Output only. Whether developer options is enabled on device.  
`otherAccounts[]` |  `string` Output only. Domain name for Google accounts on device. Type for other accounts on device. On Android, will only be populated if |ownershipPrivilege| is |PROFILE_OWNER| or |DEVICE_OWNER|. Does not include the account signed in to the device policy app if that account's domain has only one account. Examples: "com.example", "xyz.com".  
`enabledUsbDebugging` |  `boolean` Output only. Whether USB debugging is enabled on device.  
`securityPatchTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. OS security patch update time on device.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`bootloaderVersion` |  `string` Output only. Device bootloader version. Example: 0.6.7.  
`encryptionState` |  `enum (`[EncryptionState](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#EncryptionState)`)` Output only. Device encryption state.  
`androidSpecificAttributes` |  `object (`[AndroidAttributes](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#AndroidAttributes)`)` Output only. Attributes specific to Android devices.  
`managementState` |  `enum (`[ManagementState](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#ManagementState)`)` Output only. Management state of the device  
`compromisedState` |  `enum (`[CompromisedState](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#CompromisedState)`)` Output only. Represents whether the Device is compromised.  
`endpointVerificationSpecificAttributes` |  `object (`[EndpointVerificationSpecificAttributes](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#EndpointVerificationSpecificAttributes)`)` Output only. Attributes specific to [Endpoint Verification](https://cloud.google.com/endpoint-verification/docs/overview) devices.  
`deviceId` |  `string` Unique identifier for the device.  
`unifiedDeviceId` |  `string` Output only. Unified device id of the device.  
`hostname` |  `string` Host name of the device.  
`clientTypes[]` |  `enum (`[ClientType](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#ClientType)`)` List of the clients the device is reporting to.  
`browserProfiles[]` |  `object (`[BrowserAttributes](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#BrowserAttributes)`)` Browser profiles on the device. This is a copy of the BrowserAttributes message defined in EndpointVerificationSpecificAttributes. We are replicating it here since EndpointVerification isn't the only client reporting browser profiles.  
`windowsSpecificDeviceAttributes` |  `object (`[WindowsSpecificDeviceAttributes](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#WindowsSpecificDeviceAttributes)`)` Output only. Attributes specific to Windows devices.  
`antivirusInfo[]` |  `object (`[AntivirusInfo](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#AntivirusInfo)`)` Output only. Anti-virus information for the device.  
`osFirewallStatus` |  `enum (`[OsFirewallStatus](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#OsFirewallStatus)`)` Output only. OS firewall status of the device.  
  
## DeviceOwnership

Possible owners of the device: Company or individual

Enums  
---  
`DEVICE_OWNERSHIP_UNSPECIFIED` | Default value. The value is unused.  
`COMPANY` | Company owns the device.  
`BYOD` | Bring Your Own Device (i.e. individual owns the device)  
  
## DeviceType

Type of device

Enums  
---  
`DEVICE_TYPE_UNSPECIFIED` | Unknown device type  
`ANDROID` | Device is an Android device  
`IOS` | Device is an iOS device  
`GOOGLE_SYNC` | Device is a Google Sync device.  
`WINDOWS` | Device is a Windows device.  
`MAC_OS` | Device is a MacOS device.  
`LINUX` | Device is a Linux device.  
`CHROME_OS` | Device is a ChromeOS device.  
`GOOGLEBOOK` | Device is a Googlebook device.  
  
## EncryptionState

Possible values of encryption state for this device.

Enums  
---  
`ENCRYPTION_STATE_UNSPECIFIED` | Encryption Status is not set.  
`UNSUPPORTED_BY_DEVICE` | Device doesn't support encryption.  
`ENCRYPTED` | Device is encrypted.  
`NOT_ENCRYPTED` | Device is not encrypted.  
  
## AndroidAttributes

Resource representing the Android specific attributes of a Device.

JSON representation  
---  
      
    
    {
      "enabledUnknownSources": boolean,
      "supportsWorkProfile": boolean,
      "ownerProfileAccount": boolean,
      "ownershipPrivilege": enum ([OwnershipPrivilege](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#OwnershipPrivilege)),
      "verifiedBoot": boolean,
      "ctsProfileMatch": boolean,
      "verifyAppsEnabled": boolean,
      "hasPotentiallyHarmfulApps": boolean
    }  
  
Fields  
---  
`enabledUnknownSources` |  `boolean` Whether applications from unknown sources can be installed on device.  
`supportsWorkProfile` |  `boolean` Whether the device supports Android work profiles. If false, this service will not block access to corp data even if an administrator turns on the "Enforce Work Profile" policy.  
`ownerProfileAccount` |  `boolean` Whether this account is on an owner/primary profile. For phones, only true for owner profiles. Android 4+ devices can have secondary or restricted user profiles.  
`ownershipPrivilege` |  `enum (`[OwnershipPrivilege](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#OwnershipPrivilege)`)` Ownership privileges on device.  
`verifiedBoot` |  `boolean` Whether Android verified boot status is GREEN.  
`ctsProfileMatch` |  `boolean` Whether the device passes Android CTS compliance.  
`verifyAppsEnabled` |  `boolean` Whether Google Play Protect Verify Apps is enabled.  
`hasPotentiallyHarmfulApps` |  `boolean` Whether any potentially harmful apps were detected on the device.  
  
## OwnershipPrivilege

Specifies how the device ownership privilege is configured on the device.

Enums  
---  
`OWNERSHIP_PRIVILEGE_UNSPECIFIED` | Ownership privilege is not set.  
`DEVICE_ADMINISTRATOR` | Active device administrator privileges on the device.  
`PROFILE_OWNER` | Profile Owner privileges. The account is in a managed corporate profile.  
`DEVICE_OWNER` | Device Owner privileges on the device.  
  
## ManagementState

Possible management states of a device.

Enums  
---  
`MANAGEMENT_STATE_UNSPECIFIED` | Default value. This value is unused.  
`APPROVED` | Device is approved.  
`BLOCKED` | Device is blocked.  
`PENDING` | Device is pending approval.  
`UNPROVISIONED` | The device is not provisioned. The device will start from this state until some action is taken (i.e. a user starts using the device).  
`WIPING` | Data and settings on the device are being removed.  
`WIPED` | All data and settings on the device are removed.  
  
## CompromisedState

Represents whether the device is compromised

Enums  
---  
`COMPROMISED_STATE_UNSPECIFIED` | Default value.  
`COMPROMISED` | The device is compromised (currently, this means Android device is rooted).  
`UNCOMPROMISED` | The device is safe (currently, this means Android device is unrooted).  
  
## EndpointVerificationSpecificAttributes

Resource representing the [Endpoint Verification-specific attributes](https://cloud.google.com/endpoint-verification/docs/device-information) of a device.

JSON representation  
---  
      
    
    {
      "certificateAttributes": [
        {
          object ([CertificateAttributes](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#CertificateAttributes))
        }
      ],
      "browserAttributes": [
        {
          object ([BrowserAttributes](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#BrowserAttributes))
        }
      ],
      "additionalSignals": {
        object
      }
    }  
  
Fields  
---  
`certificateAttributes[]` |  `object (`[CertificateAttributes](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#CertificateAttributes)`)` Details of certificates.  
`browserAttributes[]` |  `object (`[BrowserAttributes](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#BrowserAttributes)`)` Details of browser profiles reported by Endpoint Verification.  
`additionalSignals` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` [Additional signals](https://cloud.google.com/endpoint-verification/docs/device-information) reported by Endpoint Verification. It includes the following attributes:

  * Non-configurable attributes: hotfixes, av_installed, av_enabled, windows_domain_name, is_os_native_firewall_enabled, and is_secure_boot_enabled.
  * [Configurable attributes](https://cloud.google.com/endpoint-verification/docs/collect-config-attributes): file, folder, and binary attributes; registry entries; and properties in a plist.

  
  
## CertificateAttributes

Stores information about a certificate.

JSON representation  
---  
      
    
    {
      "fingerprint": string,
      "thumbprint": string,
      "validationState": enum ([CertificateValidationState](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#CertificateValidationState)),
      "serialNumber": string,
      "validityStartTime": string,
      "validityExpirationTime": string,
      "issuer": string,
      "subject": string,
      "certificateTemplate": {
        object ([CertificateTemplate](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#CertificateTemplate))
      }
    }  
  
Fields  
---  
`fingerprint` |  `string` The encoded certificate fingerprint.  
`thumbprint` |  `string` The certificate thumbprint.  
`validationState` |  `enum (`[CertificateValidationState](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#CertificateValidationState)`)` Validation state of this certificate.  
`serialNumber` |  `string` Serial number of the certificate, Example: "123456789".  
`validityStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Certificate not valid before this timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`validityExpirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Certificate not valid at or after this timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`issuer` |  `string` The name of the issuer of this certificate.  
`subject` |  `string` The subject name of this certificate.  
`certificateTemplate` |  `object (`[CertificateTemplate](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#CertificateTemplate)`)` The X.509 extension for CertificateTemplate.  
  
## CertificateValidationState

Certificate validation status, which denotes if the certificate chain was validated for this certificate and if this certificate chains up to a trusted root for enterprise certificates.

Enums  
---  
`CERTIFICATE_VALIDATION_STATE_UNSPECIFIED` | Default value.  
`VALIDATION_SUCCESSFUL` | Certificate validation was successful.  
`VALIDATION_FAILED` | Certificate validation failed.  
  
## CertificateTemplate

CertificateTemplate (v3 Extension in X.509).

JSON representation  
---  
      
    
    {
      "id": string,
      "majorVersion": integer,
      "minorVersion": integer
    }  
  
Fields  
---  
`id` |  `string` The template id of the template. Example: "1.3.6.1.4.1.311.21.8.15608621.11768144.5720724.16068415.6889630.81.2472537.7784047".  
`majorVersion` |  `integer` The Major version of the template. Example: 100.  
`minorVersion` |  `integer` The minor version of the template. Example: 12.  
  
## BrowserAttributes

Contains information about browser profiles reported by the clients on the device (e.g. [Endpoint Verification extension](https://chromewebstore.google.com/detail/endpoint-verification/callobklhcbilhphinckomhgkigmfocg?pli=1)).

JSON representation  
---  
      
    
    {
      "lastProfileSyncTime": string,
      "chromeBrowserInfo": {
        object ([BrowserInfo](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#BrowserInfo))
      },
      "chromeProfileId": string
    }  
  
Fields  
---  
`lastProfileSyncTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp in milliseconds since the Unix epoch when the profile/gcm id was last synced.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`chromeBrowserInfo` |  `object (`[BrowserInfo](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#BrowserInfo)`)` Represents the current state of the [Chrome browser attributes](https://cloud.google.com/access-context-manager/docs/browser-attributes) sent by the clients on the device, such as [Endpoint Verification extension](https://chromewebstore.google.com/detail/endpoint-verification/callobklhcbilhphinckomhgkigmfocg?pli=1).  
`chromeProfileId` |  `string` Chrome profile ID that is exposed by the Chrome API. It is unique for each device.  
  
## BrowserInfo

Browser-specific fields reported by clients on the device, such as [Endpoint Verification extension](https://chromewebstore.google.com/detail/endpoint-verification/callobklhcbilhphinckomhgkigmfocg?pli=1).

JSON representation  
---  
      
    
    {
      "policies": [
        {
          object ([ChromePolicy](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#ChromePolicy))
        }
      ],
      "browserVersion": string,
      "browserManagementState": enum ([BrowserManagementState](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#BrowserManagementState)),
      "isFileUploadAnalysisEnabled": boolean,
      "isFileDownloadAnalysisEnabled": boolean,
      "isBulkDataEntryAnalysisEnabled": boolean,
      "isSecurityEventAnalysisEnabled": boolean,
      "isRealtimeUrlCheckEnabled": boolean,
      "safeBrowsingProtectionLevel": enum ([SafeBrowsingLevel](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#SafeBrowsingLevel)),
      "isSiteIsolationEnabled": boolean,
      "isBuiltInDnsClientEnabled": boolean,
      "passwordProtectionWarningTrigger": enum ([PasswordProtectionTrigger](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#PasswordProtectionTrigger)),
      "isChromeRemoteDesktopAppBlocked": boolean,
      "isChromeCleanupEnabled": boolean,
      "isThirdPartyBlockingEnabled": boolean
    }  
  
Fields  
---  
`policies[]` |  `object (`[ChromePolicy](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#ChromePolicy)`)` Output only. Chrome policies information for the browser as can be seen in <chrome://policy>. Full possibilities of policies can be consulted in [Chrome Enterprise Policy List](https://chromeenterprise.google/policies/).  
`browserVersion` |  `string` Version of the request initiating browser. E.g. `91.0.4442.4`.  
`browserManagementState` |  `enum (`[BrowserManagementState](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#BrowserManagementState)`)` Output only. Browser's management state.  
`isFileUploadAnalysisEnabled` |  `boolean` Current state of [file upload analysis](https://chromeenterprise.google/policies/#OnFileAttachedEnterpriseConnector). Set to true if provider list from Chrome is non-empty.  
`isFileDownloadAnalysisEnabled` |  `boolean` Current state of [file download analysis](https://chromeenterprise.google/policies/#OnFileDownloadedEnterpriseConnector). Set to true if provider list from Chrome is non-empty.  
`isBulkDataEntryAnalysisEnabled` |  `boolean` Current state of [bulk data analysis](https://chromeenterprise.google/policies/#OnBulkDataEntryEnterpriseConnector). Set to true if provider list from Chrome is non-empty.  
`isSecurityEventAnalysisEnabled` |  `boolean` Current state of [security event analysis](https://chromeenterprise.google/policies/#OnSecurityEventEnterpriseConnector). Set to true if provider list from Chrome is non-empty.  
`isRealtimeUrlCheckEnabled` |  `boolean` Current state of [real-time URL check](https://chromeenterprise.google/policies/#EnterpriseRealTimeUrlCheckMode). Set to true if provider list from Chrome is non-empty.  
`safeBrowsingProtectionLevel` |  `enum (`[SafeBrowsingLevel](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#SafeBrowsingLevel)`)` Current state of [Safe Browsing protection level](https://chromeenterprise.google/policies/#SafeBrowsingProtectionLevel).  
`isSiteIsolationEnabled` |  `boolean` Current state of [site isolation](https://chromeenterprise.google/policies/?policy=IsolateOrigins).  
`isBuiltInDnsClientEnabled` |  `boolean` Current state of [built-in DNS client](https://chromeenterprise.google/policies/#BuiltInDnsClientEnabled).  
`passwordProtectionWarningTrigger` |  `enum (`[PasswordProtectionTrigger](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#PasswordProtectionTrigger)`)` Current state of [password protection trigger](https://chromeenterprise.google/policies/#PasswordProtectionWarningTrigger).  
`isChromeRemoteDesktopAppBlocked` |  `boolean` Current state of [Chrome Remote Desktop app](https://chromeenterprise.google/policies/#URLBlocklist).  
`isChromeCleanupEnabled  
**(deprecated)**` |  `boolean` This field is deprecated!Deprecated: This field is not used for Chrome version 118 and later. Current state of [Chrome Cleanup](https://chromeenterprise.google/policies/#ChromeCleanupEnabled).  
`isThirdPartyBlockingEnabled` |  `boolean` Current state of [third-party blocking](https://chromeenterprise.google/policies/#ThirdPartyBlockingEnabled).  
  
## BrowserManagementState

Information regarding management state of the profile.

Enums  
---  
`UNSPECIFIED` | Management state is not specified.  
`UNMANAGED` | Browser/Profile is not managed by any customer.  
`MANAGED_BY_OTHER_DOMAIN` | Browser/Profile is managed, but by some other customer.  
`PROFILE_MANAGED` | Profile is managed by customer.  
`BROWSER_MANAGED` | Browser is managed by customer.  
  
## SafeBrowsingLevel

Information regarding the browsing protection level policy of the browser.

Enums  
---  
`SAFE_BROWSING_LEVEL_UNSPECIFIED` | Browser protection level is not specified.  
`DISABLED` | No protection against dangerous websites, downloads, and extensions.  
`STANDARD` | Standard protection against websites, downloads, and extensions that are known to be dangerous.  
`ENHANCED` | Faster, proactive protection against dangerous websites, downloads, and extensions.  
  
## PasswordProtectionTrigger

Information regarding the password protect warning trigger policy of the browser

Enums  
---  
`PASSWORD_PROTECTION_TRIGGER_UNSPECIFIED` | Password protection is not specified.  
`PROTECTION_OFF` | Password reuse is never detected.  
`PASSWORD_REUSE` | Warning is shown when the user reuses their protected password on a non-allowed site.  
`PHISHING_REUSE` | Warning is shown when the user reuses their protected password on a phishing site.  
  
## ChromePolicy

Represents a Chrome policy and its current state.

JSON representation  
---  
      
    
    {
      "name": string,
      "scope": enum ([PolicyScope](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#PolicyScope)),
      "source": enum ([PolicySource](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#PolicySource)),
      "conflicts": [
        {
          object ([PolicyConflict](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#PolicyConflict))
        }
      ],
      "value": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The unique name of the Chrome policy. These names correspond to the policy names listed in [Chrome Enterprise Policy List](https://chromeenterprise.google/policies/)  
`scope` |  `enum (`[PolicyScope](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#PolicyScope)`)` Output only. The scope at which the _applied_ policy value is set (USER or MACHINE).  
`source` |  `enum (`[PolicySource](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#PolicySource)`)` Output only. The source from which the _applied_ policy value originated.  
`conflicts[]` |  `object (`[PolicyConflict](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#PolicyConflict)`)` Output only. A list of other policy values for the same policy name that were not applied due to lower precedence. This field is empty if there were no conflicts.  
`value` |  `string` Output only. The currently applied value of the policy. The format depends on the policy type (e.g., boolean, string, JSON array/object).  
  
## PolicyScope

The scope of a policy, indicating whether it applies at the user or machine level.

Enums  
---  
`SCOPE_UNKNOWN` | Default value. The policy scope is unknown or not specified.  
`USER` | User-level policy. This scope indicates the policy applies to the specific user session or profile. For cloud policies, this is typically the signed-in Chrome profile. On some platforms like Windows, this can also refer to the OS user.  
`MACHINE` | Machine-level policy. This scope indicates the policy applies system-wide to all users on the current machine or device.  
  
## PolicySource

The source of a policy, indicating where its value originates from.

Enums  
---  
`SOURCE_UNKNOWN` | Default value. The policy source is unknown or not specified.  
`ENTERPRISE_DEFAULT` | The policy is provided by Chrome's default settings when running in an enterprise environment.  
`CLOUD` | The policy is managed and pushed from a cloud-based administration console, such as the Google Admin console.  
`ACTIVE_DIRECTORY` | The policy is sourced from Active Directory, primarily for Active Directory-managed ChromeOS devices.  
`DEVICE_LOCAL_ACCOUNT_OVERRIDE_DEPRECATED` | Deprecated: Formerly used when a policy was overridden by ChromeOS for public sessions or kiosk mode.  
`PLATFORM` | The policy is set by OS built-in tool on desktop.  
`PRIORITY_CLOUD_DEPRECATED` | Deprecated: Formerly used for cloud policies with higher priority.  
`MERGED` | The applied policy value is the result of a merge from multiple policy sources.  
`COMMAND_LINE` | The policy is set using a command line argument passed to the Chrome executable, usually intended for development or testing.  
`CLOUD_FROM_ASH` | For ChromeOS, this indicates a policy set by cloud management in the Ash browser and then made available to the Lacros browser.  
`RESTRICTED_MANAGED_GUEST_SESSION_OVERRIDE` | The policy is set by the restricted managed guest session override.  
  
## PolicyConflict

Represents a policy value from a source that was not applied because a higher-priority source took precedence.

JSON representation  
---  
      
    
    {
      "value": string,
      "scope": enum ([PolicyScope](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#PolicyScope)),
      "source": enum ([PolicySource](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#PolicySource))
    }  
  
Fields  
---  
`value` |  `string` Output only. The policy value from this lower-priority source.  
`scope` |  `enum (`[PolicyScope](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#PolicyScope)`)` Output only. The scope at which this lower-priority policy is set (USER or MACHINE).  
`source` |  `enum (`[PolicySource](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#PolicySource)`)` Output only. The source from which this lower-priority policy value originated.  
  
## ClientType

Client type on the device

Enums  
---  
`CLIENT_TYPE_UNSPECIFIED` | Default value  
`DRIVE_FS` | Managed by DriveFS  
`FUNDAMENTAL` | Management type for every secure device  
`ENDPOINT_VERIFICATION` | Managed by Endpoint Verification  
`WINDOWS_ADVANCED` | Managed by Windows  
`GOOGLE_CREDENTIALS_PROVIDER_FOR_WINDOWS` | Managed by Google credential provider for windows  
  
## WindowsSpecificDeviceAttributes

Represents the Windows specific attributes of a Device.

JSON representation  
---  
      
    
    {
      "windowsMachineDomain": string,
      "windowsUserDomain": string,
      "hotfixes": [
        string
      ],
      "secureBootMode": enum ([SecureBootMode](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#SecureBootMode))
    }  
  
Fields  
---  
`windowsMachineDomain` |  `string` Output only. The domain of the machine that the user is logged into. This is different from the windowsUserDomain as the user could be logged into a domain different from the machine domain.  
`windowsUserDomain` |  `string` Output only. The domain of the user account that is logged into the machine.  
`hotfixes[]` |  `string` Output only. The hotfixes installed on the device.  
`secureBootMode` |  `enum (`[SecureBootMode](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#SecureBootMode)`)` Output only. Secure boot mode of the device.  
  
## SecureBootMode

Types of secure boot mode of the device.

Enums  
---  
`SECURE_BOOT_MODE_UNSPECIFIED` | Default value  
`SECURE_BOOT_MODE_UNKNOWN` | Secure boot mode is unknown.  
`SECURE_BOOT_MODE_ENABLED` | Secure boot mode is enabled.  
`SECURE_BOOT_MODE_DISABLED` | Secure boot mode is disabled.  
  
## AntivirusInfo

Resource representing the anti-virus information of a Device.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "productState": enum ([ProductState](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#ProductState)),
      "productGuid": string
    }  
  
Fields  
---  
`displayName` |  `string` Output only. The display name of the anti-virus software.  
`productState` |  `enum (`[ProductState](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices#ProductState)`)` Output only. The state of the anti-virus.  
`productGuid` |  `string` Output only. The GUID of the anti-virus product.  
  
## ProductState

Types of anti-virus product states.

Enums  
---  
`PRODUCT_STATE_UNSPECIFIED` | Default value  
`PRODUCT_STATE_ON` | The anti-virus is on.  
`PRODUCT_STATE_OFF` | The anti-virus is off.  
`PRODUCT_STATE_SNOOZED` | The anti-virus is snoozed.  
`PRODUCT_STATE_EXPIRED` | The anti-virus is expired.  
  
## OsFirewallStatus

Types of OS firewall status of the device.

Enums  
---  
`OS_FIREWALL_STATUS_UNSPECIFIED` | Default value  
`OS_FIREWALL_STATUS_UNKNOWN` | OS firewall status is unknown.  
`OS_FIREWALL_STATUS_ENABLED` | OS firewall is enabled.  
`OS_FIREWALL_STATUS_DISABLED` | OS firewall is disabled.  
  
## Methods  
  
---  
  
### `[cancelWipe](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/cancelWipe)`

|  Cancels an unfinished device wipe.  
  
### `[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/create)`

|  Creates a device.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/delete)`

|  Deletes the specified device.  
  
### `[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/get)`

|  Retrieves the specified device.  
  
### `[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/list)`

|  Lists/Searches devices.  
  
### `[wipe](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/wipe)`

|  Wipes all data on the specified device.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
