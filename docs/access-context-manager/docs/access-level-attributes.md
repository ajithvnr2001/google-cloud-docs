---
url: https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes/
title: Access level attributes \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:01.862056+00:00
---

# Access level attributes  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/access-context-manager/docs/apis)



Send feedback 

#  Access level attributes Stay organized with collections  Save and categorize content based on your preferences. 

Access levels define various attributes that are used to filter requests made to certain resources. The following table lists the attributes supported by access levels and provides additional details about each attribute.

When you create or modify an access level using the `gcloud` command-line tool, you must format the attributes in YAML. This table includes the YAML syntax for each attribute, and the valid values. Links to the REST and RPC reference information for each attribute are also included.

For more information about access levels and YAML, refer to the [example YAML for an access level](https://docs.cloud.google.com/access-context-manager/docs/example-yaml-file).

You can include the following attributes in your access level:

  * IP subnetworks

  * Geographic locations

  * Access level dependencies

  * Principals

  * Device policy




##  Attributes   
  
---  
  
###  **IP subnetworks**

|  |  **Description** |  Checks whether a request is coming from one or more IPv4 and/or IPv6 CIDR blocks that you specify.  When you specify more than one IP subnetwork, the values you enter are combined using an OR operator when the condition is evaluated. The request has to match any one of the values that you specify in order for the condition to evaluate to true.   
---|---  
**YAML** |  `ipSubnetworks`  
**Valid values** |  A list of one or more IPv4 and/or IPv6 CIDR blocks.   
**API reference** | 

  * [ `REST` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#Condition.FIELDS.ip_subnetworks)
  * [ `RPC` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.Condition.FIELDS.repeated.string.google.identity.accesscontextmanager.v1.Condition.ip_subnetworks)

  
  
###  **Geographic locations**

|  |  **Description** |  Checks whether a request originated from a specific geographic location. Geographic locations are identified by the corresponding [ISO 3166-1 alpha-2 codes](https://www.iso.org/obp/ui/#search/code/).  **Caution:** The origin of a request is determined by the geolocation of the IP address that the request originated from. Because of this, the geographic location attribute only works for requests that originate from a public IP address.  Because private IP addresses cannot be geolocated, access levels that require a geographic location will always deny requests from private IP addresses and don't support requests made using Private Google Access.  When you specify more than one geographic location, the values you enter are ORd when the condition is evaluated. Users are granted access if they are in one of the geographic locations that you specify.  **Note:** If a user connects to your resources through a VPN, Access Context Manager determines access based on the derived geographic location of the VPN server's public IP address, rather than the user's actual physical location. Consequently, if the VPN server's IP address maps to an allowed region, the request is permitted, regardless of where the user is physically located. To help improve security in environments with high-security requirements, we recommend supplementing region-based rules with additional signals, such as device compliance.   
---|---  
**YAML** |  `regions`  
**Valid values** |  A list of one or more [ ISO 3166-1 alpha-2 codes](https://www.iso.org/obp/ui/#search/code/).   
**API reference** | 

  * [ `REST` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#Condition.FIELDS.regions)
  * [ `RPC` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.Condition.FIELDS.repeated.string.google.identity.accesscontextmanager.v1.Condition.regions)

  
  
###  **Access level dependencies**

|  |  **Description** |  Checks whether a request meets the criteria of one or more access levels.   
---|---  
**YAML** |  `requiredAccessLevels`  
**Valid values** |  A list of one or more existing access levels formatted as:  `accessPolicies/POLICY-NAME/accessLevels/LEVEL-NAME` Where: 

  * POLICY-NAME is the numeric name of your Organization's access policy. 
  * LEVEL-NAME is the name of the access level that you want to add as a dependency. 

  
**API reference** | 

  * [ `REST` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#Condition.FIELDS.required_access_levels)
  * [ `RPC` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.Condition.FIELDS.repeated.string.google.identity.accesscontextmanager.v1.Condition.required_access_levels)

  
  
###  **Principals**

|  |  **Description** |  Checks whether a request is coming from a specific user or service account.  This attribute can only be included in conditions when creating or modifying an access level using the `gcloud` command-line tool or the Access Context Manager API. If you created an access level using Google Cloud console, either of the methods previously mentioned can be used to add principals to that access level.   
---|---  
**YAML** |  `members`  
**Valid values** |  A list of one or more user or service accounts, formatted as: 

  * `user: EMAIL`
  * `serviceAccount: EMAIL`

Where: 

  * EMAIL is the email that corresponds to the user or service account that you want to include in the access level. 

Groups are not supported.   
**API reference** | 

  * [ `REST` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#Condition.FIELDS.members)
  * [ `RPC` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.Condition.FIELDS.repeated.string.google.identity.accesscontextmanager.v1.Condition.members)

  
  
###  **Device policy**

|  |  **Requirements** |  To use the device policy attributes with mobile devices, [you must configure MDM for your organization](https://docs.cloud.google.com/access-context-manager/docs/use-mobile-devices).  To use the device policy attributes with other devices, [ Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/overview) must be enabled.   
---|---  
**Description** |  A device policy is a  collection of attributes that are used to filter requests based on information about the device where the request originated.  For example, device policy attributes are used in conjunction with [ Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto) to support Context-Aware Access.   
**YAML** |  `devicePolicy`  
**Valid values** |  `devicePolicy` is a list of one or more device policy attributes. The following attributes are supported: 

  * Require screen lock
  * Storage encryption
  * Require administrator approval
  * Require corp owned device
  * OS policy

Only certain device policy attributes can be used with mobile devices. The **Supports mobile devices** row identifies whether an attribute can be used with mobile devices.   
**API reference** | 

  * [ `REST` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#DevicePolicy)
  * [ `RPC` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.DevicePolicy)

  
Device policy attributes   
**Require screen lock**  
|  **Description** |  Checks if a device has screen lock enabled.   
---|---  
**Supports mobile devices** |  Yes   
**YAML** |  `requireScreenlock`  
**Valid values** | 

  * `true`
  * `false`

If omitted, defaults to `false`.   
**API reference** | 

  * [ `REST` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#DevicePolicy.FIELDS.require_screenlock)
  * [ `RPC` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.DevicePolicy.FIELDS.bool.google.identity.accesscontextmanager.v1.DevicePolicy.require_screenlock)

  
**Storage encryption**  
|  **Description** |  Checks whether the device is encrypted, not encrypted, or does not support storage encryption.   
---|---  
**Supports mobile devices** |  Yes  **Important:** For an iOS device to satisfy the the storage encryption attribute, screen lock must be enabled on the device.   
**YAML** |  `allowedEncryptionStatuses`  
**Valid values** |  One or more of the following values: 

  * `ENCRYPTION_UNSUPPORTED`
  * `ENCRYPTED`
  * `UNENCRYPTED`

  
**API reference** | 

  * [ `REST` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/DeviceEncryptionStatus)
  * [ `RPC` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rpc/google.identity.accesscontextmanager.type#google.identity.accesscontextmanager.type.DeviceEncryptionStatus)

  
**Require admin approval**  
|  **Description** |  Checks whether the device has been approved by a an administrator.   
---|---  
**Supports mobile devices** |  Yes   
**YAML** |  `requireAdminApproval`  
**Valid values** | 

  * `true`
  * `false`
If omitted, defaults to `false`.  
  
**API reference** |  None   
**Require corp owned device**  
|  **Description** |  Checks whether the device is owned by your enterprise.   
---|---  
**Supports mobile devices** |  Yes   
**YAML** |  `requireCorpOwned`  
**Valid values** | 

  * `true`
  * `false`
If omitted, defaults to `false`.  
  
**API reference** |  None   
**OS policy**  
|  **Description** |  Checks whether a device is using a specified operating system. Additionally, you can specify a minimum version of an OS that a device must be using.  If you create a ChromeOS policy, you can also specify that it must be a [ verified ChromeOS ](https://support.google.com/chrome/a/answer/7156268).  When you select more than one operating system, the values you select are ORd when the condition is evaluated. Users are granted access if they have one of the operating systems that you specify.   
---|---  
**Supports mobile devices** |  Yes   
**YAML** |  `osConstraints`  
**Valid values** |  `osConstraints` is a list that must include one or more instances of `osType`. `osType` can be paired with an instance of `minimumVersion`, but `minimumVersion` is not required. 

  * `osType` must include a list of one or more of the following values: 
    * `DESKTOP_MAC`
    * `DESKTOP_WINDOWS`
    * `DESKTOP_CHROME_OS`
    * `DESKTOP_LINUX`
    * `IOS`
    * `ANDROID`
    * `GOOGLEBOOK_OS`
  * `minimumVersion` is optional. If used, it must be included with `osType`.  `minimumVersion` must include a minimum version formatted as MAJOR.MINOR.PATCH.  For example: 10.5.301. 
  * If you specify `DESKTOP_CHROME_OS` for `osType`, you can optionally include `requireVerifiedChromeOs`.  Valid values for `requireVerifiedChromeOs` are: 
    * `true`
    * `false`
  * If you specify `IOS` or `ANDROID` for `osType`, you can optionally include any device policy attribute that supports mobile devices. 

  
**API reference** | 

  * [ `REST` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#OsConstraint)
  * [ `RPC` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rpc/google.identity.accesscontextmanager.v1#google.identity.accesscontextmanager.v1.OsConstraint)

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
