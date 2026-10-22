---
url: https://docs.cloud.google.com/endpoint-verification/docs/device-information/
title: Device attributes collected by Endpoint Verification \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:26.272779+00:00
---

# Device attributes collected by Endpoint Verification  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/device-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Guides ](https://docs.cloud.google.com/endpoint-verification/docs/overview)



Send feedback 

#  Device attributes collected by Endpoint Verification Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the details of device attributes that are collected by Endpoint Verification from the devices accessing your organization's resources. Endpoint Verification collects device attributes, device identity attributes, configurable device attributes and Chrome browser attributes.

**Note:** You can also use [Chrome Enterprise Premium and third-party client integrations](https://docs.cloud.google.com/chrome-enterprise-premium/docs/integration-docs) to collect device attributes from third-party clients, such as Tanium, CrowdStrike, and Microsoft Intune.

## Device attributes

The following table describes the attributes that are collected by Endpoint Verification that you can use to create access levels.

**Note:** The value `bce` in `device.clients[]` represents Chrome Enterprise Premium (formerly BeyondCorp Enterprise).**Attribute name** | **Description** | **Supported OS** | **Example of using the attribute in the[CEL](https://github.com/google/cel-spec) expressions**  
---|---|---|---  
`is_secured_with_screenlock` | A boolean value that indicates whether the screen lock function is enabled on a device.  | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.is_secured_with_screenlock == true`  
`encryption_status` | The encryption status of a device. Possible values:

  * `ENCRYPTION_UNSPECIFIED = 0` indicates that the encryption status of the device is not specified or not known.
  * `ENCRYPTION_UNSUPPORTED = 1` indicates that the device does not support encryption.
  * `ENCRYPTION_UNENCRYPTED = 2` indicates that the device supports encryption, but is not encrypted.
  * `ENCRYPTED = 3` indicates that the device is encrypted.

| 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.encryption_status == DeviceEncryptionStatus.ENCRYPTED`  
`os_type` | The operating system running on a device. Possible values:

  * `OS_UNSPECIFIED = 0` indicates that the operating system of the device is not specified or not known.
  * `DESKTOP_MAC = 1`
  * `DESKTOP_WINDOWS = 2`
  * `DESKTOP_LINUX = 3`
  * `DESKTOP_CHROME_OS = 6`

| 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.os_type == OsType.DESKTOP_MAC`  
`os_version` | The version of the operating system running on a device. | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| 

  * `device.os_version == "MacOS 13.4.0"`
  * `device.os_version == "ChromeOs 14541.0.0"`
  * `device.os_version == "Windows 10.0.19045"`
  * `device.os_version == "Linux rodete"`

**Note:** Operating system names are case-sensitive.   
`verified_chrome_os` | A boolean value that indicates whether the request comes from a device with a [verified ChromeOS](https://support.google.com/chrome/a/answer/7156268).  |  ChromeOS (only for enterprise-enrolled devices)  | `device.verified_chrome_os == true`  
`model` | The model of a device. | 

  * macOS
  * Windows
  * Linux

| `device.model == "MacBookPro16,1"`  
`is_managed_browser_profile` | A boolean value that indicates whether the Chrome content area account associated with a device matches its Chrome profile account.  | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.is_managed_browser_profile == true`  
`certificates` | Attributes of the certificates associated with a device. For example, [Enterprise certificates](https://docs.cloud.google.com/access-context-manager/docs/enterprise-certificates).  | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.certificates.exists(cert, cert.is_valid && cert.root_ca_fingerprint == "SOME_ROOT_CA_FINGERPRINT")`  
`windows_domain_name` | The domain name of a Windows machine. | Windows | `device.clients["bce"].data["windows_domain_name"] == "GOOGLE"`  
`is_os_native_firewall_enabled` | A boolean value that indicates whether the operating system's built-in firewall is enabled on a device.  | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.clients["bce"].data["is_os_native_firewall_enabled"] == true`  
`is_secure_boot_enabled` | A boolean value that indicates whether the secure boot option is enabled on a device.  | Windows | `device.clients["bce"].data["is_secure_boot_enabled"] == true`  
`av_installed` | A list of antivirus software products that are installed on a device. **Note:** Requires the [Endpoint Verification native helper](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-third-party-tools). | Windows | `device.clients["bce"].data["av_installed"].exists(x, x == "mcafee") == true`  
`av_enabled` | A list of antivirus software products that are installed and enabled on a device. **Note:** Requires the [Endpoint Verification native helper](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-third-party-tools). | Windows | `device.clients["bce"].data["av_enabled"].exists(x, x == "mcafee") == true`  
`hotfixes` | A list of hotfixes that are applied on Windows systems. **Note:** Requires the [Endpoint Verification native helper](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-third-party-tools). | Windows | `device.clients["bce"].data["hotfixes"].exists(x, x == "KB0001") == true`  
  
## Device identity attributes

The following table describes the attributes that are collected by Endpoint Verification that you can use to identify devices. These attributes cannot be used for creating access levels.

**Attribute name** | **Description** | **Supported OS**  
---|---|---  
Serial number | The serial number of the device. | 

  * macOS
  * ChromeOS (only for enterprise-enrolled devices)
  * Windows
  * Linux

  
Hostname | The hostname of the device. | 

  * macOS
  * Windows
  * Linux

  
Device ID | The unique identification number associated with the device. | 

  * macOS
  * Windows
  * Linux

  
Wifi MAC Address | The MAC address of the device. | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

  
  
## Configurable device attributes

Endpoint Verification provides an option to collect granular device attributes called **configurable device attributes** , such as metadata attributes of files, folders, and binaries; registry entries; and properties in a plist. You can use these device configuration attributes to create access levels.

This option is not enabled by default. To collect these granular configurable device attributes, [configure Endpoint Verification settings](https://docs.cloud.google.com/endpoint-verification/docs/collect-config-attributes).

**Note:** The [Endpoint Verification native helper](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-third-party-tools) runs in the user space, as the signed-in user. It can only detect files, folders, and processes that are visible and accessible to the current user. 

The following table describes the file, folder, and binary attributes.

**Note:** `config_name` is the name of the configuration that you specified when configuring the Endpoint Verification settings.**Attribute name** | **Description** | **Supported OS** | **Example of using the attribute in the[CEL](https://github.com/google/cel-spec) expressions**  
---|---|---|---  
`presence` | Indicates the presence of a file, folder, or binary. Possible values:

  * `VALUE_UNKNOWN = 0` indicates that the presence is not known due to a failure that occurred before the assessment. 
  * `VALUE_INACCESSIBLE = 1` indicates that the organization does not have access to the signal's resource.
  * `VALUE_NOT_FOUND = 2` indicates that the resource was not found.
  * `VALUE_FOUND = 3` indicates that the resource was found.

| 

  * macOS
  * Windows
  * Linux

| `device.clients["bce"].data["file_config"]["config_name"]["presence"] == PresenceValue.VALUE_FOUND`  
`is_running` | Indicates if a binary is running. It is always false for a file or folder.  | 

  * macOS
  * Windows
  * Linux

| `device.clients["bce"].data["file_config"]["config_name"]["is_running"] == true`  
`sha256_hash` | Provides SHA-256 hash of a file or binary. It is always an empty string for a folder. **Note:** String comparisons are case-sensitive.  | 

  * macOS
  * Windows
  * Linux

| `device.clients["bce"].data["file_config"]["config_name"]["sha256_hash"] == ""`  
`public_key_sha256` | Provides a list of SHA-256 hash values of the public keys that are used to sign the executable. It is always an empty string for a file or a folder. **Note:** String comparisons are case-sensitive.  | 

  * macOS
  * Windows

| `device.clients["bce"].data["file_config"]["config_name"]["public_key_sha256"].exists(x, x == "")`  
`product_name` | The product name of the executable. It is always an empty string for a file or folder. **Note:** String comparisons are case-sensitive.  | 

  * macOS
  * Windows

| `device.clients["bce"].data["file_config"]["config_name"]["product_name"] == "some value"`  
`version` | The product version of the executable. It is always an empty string for a file or folder.  **Note:** String comparisons are case-sensitive.  | 

  * macOS
  * Windows

| `device.clients["bce"].data["file_config"]["config_name"]["version"] == "some value"`  
  
The following table describes the attributes based on the registry entries and properties of a plist.

**Note:** `config_name` is the name of the configuration that you specified when configuring the Endpoint Verification settings.**Attribute name** | **Description** | **Supported OS** | **Example of using the attribute in the[CEL](https://github.com/google/cel-spec) expressions**  
---|---|---|---  
`presence` | Indicates the presence of a registry or plist entry. Possible values:

  * `VALUE_UNKNOWN = 0` indicates that the presence is not known due to a failure that occurred before the assessment. 
  * `VALUE_INACCESSIBLE = 1` indicates that the organization does not have access to the signal's resource.
  * `VALUE_NOT_FOUND = 2` indicates that the resource was not found.
  * `VALUE_FOUND = 3` indicates that the resource was found.

| 

  * macOS
  * Windows

| 

  * `device.clients["bce"].data["registry_config"]["config_name"]["presence"] == PresenceValue.VALUE_FOUND`
  * `device.clients["bce"].data["plist_config"]["config_name"]["presence"] == PresenceValue.VALUE_FOUND`

  
`value` | Provides the data that is stored in the registry or plist. Possible values:

  * macOS: `NSString` or `NSNumber`
  * Windows: `REG_SZ`, `REG_DWORD`, or `REG_QWORD`

The strings are limited to 1024 bytes. **Note:** String comparisons are case-sensitive.  | 

  * macOS
  * Windows

| 

  * `device.clients["bce"].data["registry_config"]["config_name"]["value"] == <"string value"|boolean|double|int>`
  * `device.clients["bce"].data["plist_config"]["config_name"]["value"] == <"string value"|boolean|double|int>`

  
  
## Chrome browser attributes

The Chrome browser is Chrome Enterprise Premium's zero trust endpoint platform, empowering and protecting work-from-anywhere enterprises. Integrated natively with the Chrome browser, Chrome Enterprise Premium offers centralized security policy management, agentless endpoint protection, and integrated zero trust access.

The Chrome Enterprise Premium offers the following endpoint security capabilities::

  * Data protection: Prevent leaking of sensitive data (for example, personally-identifiable information) in files transferred and in content uploaded by the browser.
  * Threat protection: Protect against malware transfers using reputation, signatures, and cloud sandboxing.
  * Enterprise analytics: Provide analysis and investigation for security events such as malware transfer, phishing site visit, credential thefts, or sensitive data transfer.



To ensure that users are accessing resources from secure environments, you can set zero trust policies that ensure the user's browser environment has these threat and data protection capabilities turned on.

IMPORTANT: The Chrome attributes are only effective for browser-based traffic; the attributes have no effect when the requests aren't coming from a browser, such as requests from gcloud CLI or Google Cloud SDKs

The following table describes the Google Chrome browser attributes that are collected by Endpoint Verification that you can use to create access levels:

**Attribute name** | **Description** | **Supported OS** | **Example of using the attribute in the[CEL](https://github.com/google/cel-spec) expressions**  
---|---|---|---  
`versionAtLeast(min_version)` | The minimum version of the Chrome browser. | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.chrome.versionAtLeast("88.0.4321.44")`  
`management_state` | The management state of the browser for a device. A browser is considered to be managed if it is enrolled to [Chrome browser cloud management](https://support.google.com/chrome/a/answer/9116814). Possible values:

  * `CHROME_MANAGEMENT_STATE_UNSPECIFIED = 0` indicates that the management state of the device is not specified or not known.
  * `CHROME_MANAGEMENT_STATE_UNMANAGED = 1` indicates that the browser or the profile is not managed by any organization. 
  * `CHROME_MANAGEMENT_STATE_MANAGED_BY_OTHER_DOMAIN = 2` indicates that the browser is managed, but by some other organization.
  * `CHROME_MANAGEMENT_STATE_PROFILE_MANAGED = 3` indicates that the browser is not managed and the profile is managed by an organization.
  * `CHROME_MANAGEMENT_STATE_BROWSER_MANAGED = 4` indicates that the browser and profile are managed by an organization.

| 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.chrome.management_state == ChromeManagementState.CHROME_MANAGEMENT_STATE_MANAGED_BY_OTHER_DOMAIN`  
`is_file_upload_analysis_enabled` | A boolean value that indicates whether the [file upload analysis connector](https://chromeenterprise.google/policies/#OnFileAttachedEnterpriseConnector) is enabled on a device. | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.chrome.is_file_upload_analysis_enabled == true | false`  
`is_file_download_analysis_enabled` | A boolean value that indicates whether the [file download analysis connector](https://chromeenterprise.google/policies/#OnFileDownloadedEnterpriseConnector) is enabled on a device. | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.chrome.is_file_download_analysis_enabled == true | false`  
`is_bulk_data_entry_analysis_enabled` | A boolean value that indicates whether the [bulk text (paste) analysis connector](https://chromeenterprise.google/policies/#OnBulkDataEntryEnterpriseConnector) is enabled on a device. | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.chrome.is_bulk_data_entry_analysis_enabled == true | false`  
`is_security_event_analysis_enabled` | A boolean value that indicates whether the [security event reporting connector](https://chromeenterprise.google/policies/#OnSecurityEventEnterpriseConnector) is enabled on a device. | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.chrome.is_security_event_analysis_enabled == true | false`  
`is_realtime_url_check_enabled` | A boolean value that indicates whether the [real-time URL check connector](https://chromeenterprise.google/policies/#EnterpriseRealTimeUrlCheckMode) is enabled on a device. | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.chrome.is_realtime_url_check_enabled == true | false` | `safe_browsing_protection_level` | The [browsing protection level policy](https://chromeenterprise.google/policies/#SafeBrowsingProtectionLevel) of the browser. Possible values:

  * `SAFE_BROWSING_LEVEL_UNSPECIFIED = 0` indicates that the browser protection level policy is not set for the device.
  * `SAFE_BROWSING_LEVEL_DISABLED = 1` indicates that the browser protection level policy is disabled for the device, and the device is not protected against dangerous websites, downloads, and extensions.
  * `SAFE_BROWSING_LEVEL_STANDARD = 2` indicates that the device is protected against websites, downloads, and extensions that are known to be dangerous. 
  * `SAFE_BROWSING_LEVEL_ENHANCED = 3`
indicates that the device has proactive protection against dangerous websites, downloads, and extensions. 
| 

  * Mac
  * ChromeOS
  * Windows
  * Linux

| `device.chrome.safe_browsing_protection_level == SafeBrowsingLevel.SAFE_BROWSING_LEVEL_STANDARD`  
`is_site_isolation_enabled` | A boolean value that indicates whether the [site isolation](https://chromeenterprise.google/policies/?policy=IsolateOrigins) is enabled for every site.  | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.chrome.is_site_isolation_enabled == true` | `is_built_in_dns_client_enabled` | A boolean value that indicates whether [Chrome's built-in DNS client](https://chromeenterprise.google/policies/#BuiltInDnsClientEnabled) communicates with the DNS server.  | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.chrome.is_built_in_dns_client_enabled == true`  
`password_protection_warning_trigger` | The [password protect warning trigger policy](https://chromeenterprise.google/policies/#PasswordProtectionWarningTrigger) of the browser. Possible values: 

  * `PASSWORD_PROTECTION_TRIGGER_UNSPECIFIED = 0` indicates that the password protect warning trigger policy is not set.
  * `PASSWORD_PROTECTION_TRIGGER_PROTECTION_OFF = 1` indicates that the password reuse is never detected.
  * `PASSWORD_PROTECTION_TRIGGER_PASSWORD_REUSE = 2` indicates that a warning is displayed when the end user reuses their protected password on a site that is not allowed. 
  * `PASSWORD_PROTECTION_TRIGGER_PHISHING_REUSE = 3` indicates that a warning is displayed when the end user reuses their protected password on a phishing site. 

| 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.chrome.password_protection_warning_trigger == PasswordProtectionTrigger.PASSWORD_PROTECTION_TRIGGER_PASSWORD_REUSE` | `is_chrome_remote_desktop_app_blocked` | A boolean value that indicates whether the [Chrome remote desktop remote application](https://chromeenterprise.google/policies/#URLBlocklist) is blocked.  | 

  * macOS
  * ChromeOS
  * Windows
  * Linux

| `device.chrome.is_chrome_remote_desktop_app_blocked == true`  
`is_chrome_cleanup_enabled` | A boolean value that indicates whether the [Chrome Cleanup tool](https://chromeenterprise.google/policies/#ChromeCleanupEnabled) is enabled.  | Windows | `device.chrome.is_chrome_cleanup_enabled == true` | `is_third_party_blocking_enabled` | A boolean value that indicates whether the [third party software injection blocking](https://chromeenterprise.google/policies/#ThirdPartyBlockingEnabled) is enabled. **Note:** This attribute is supported only on Chrome from version 65 to version 135. This attribute is deprecated for Chrome version later than version 135.  | Windows | `device.chrome.is_third_party_blocking_enabled == true`  
  
The following table contains examples of policies that you can set:

Example Policy | Expression  
---|---  
Only allow access when the user is coming from a fully managed Chrome browser and not just a managed Chrome profile. After authentication through a fully managed Chrome browser, the user may also use the Google Cloud CLI to access the resources.  | `device.chrome.management_state == ChromeManagementState.CHROME_MANAGEMENT_STATE_BROWSER_MANAGED`  
Only allow access to resources if download content analysis is enabled so administrators can ensure that sensitive content download can be detected. | `device.chrome.is_file_download_analysis_enabled == true`  
Only allow access to content if the browser has threat and data protection capabilities enabled. | `device.chrome.is_file_download_analysis_enabled == true && device.chrome.is_file_upload_analysis_enabled == true && device.chrome.is_realtime_url_check_enabled == true `  
Only allow access to content if security event reporting is enabled. | `device.chrome.is_security_event_analysis_enabled == true`  
  
## What's next

  * [Set up Endpoint Verification on your devices](https://docs.cloud.google.com/endpoint-verification/docs/quickstart)

  * [Deploy Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-admin-console)

  * [Enable collection of configurable device attributes](https://docs.cloud.google.com/endpoint-verification/docs/collect-config-attributes)

  * [Create device-based access levels](https://docs.cloud.google.com/endpoint-verification/docs/creating-device-access-level)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
