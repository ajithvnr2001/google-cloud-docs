---
url: https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec/
title: Custom access level specification \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:52:20.951203+00:00
---

# Custom access level specification  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/access-context-manager/docs/apis)



Send feedback 

#  Custom access level specification Stay organized with collections  Save and categorize content based on your preferences. 

This page details the objects and attributes that are used to build the [Common Expression Language](https://opensource.google.com/projects/cel) (CEL) expressions for custom access levels. Examples are included.

To learn more about CEL, see the [CEL language definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md).

**Note:** For [CEL macros](https://github.com/google/cel-spec/blob/master/doc/langdef.md#macros), custom access levels only support those documented on this page.

## Objects

Access Context Manager provides four objects that contain access level attributes.

Objects   
---  
`origin` |  Contains attributes that identify the origin of the request.   
`request.auth` |  Contains attributes that identify authentication and authorization aspects of the request.   
`request.time` |  Contains time-based attributes that you can use to restrict access to resources based on the time of day, day of the week, or a specific date range.   
`levels` |  Contains attributes to define dependency on other access levels.   
`device` |  Contains attributes that describe the device the request originated from.   
`api` |  Contains attributes related to the API call itself, distinct from the user, device, or network.   
  
### `origin` attributes

This section lists the attributes supported by the `origin` object.

Attributes   
---  
`ip` |  |  **Type** |  string   
---|---  
**Description** |  The IP address the request originated from. If the IP address cannot be determined, `origin.ip` evaluates to an error. We recommend that you use `inIpRange` to check if the origin IP address is in a specific IP address range instead of doing a string comparison.  **Warning:** Do not compare `origin.ip` with the empty string. The behavior is undefined.  **Example:**
    
    
    inIpRange(origin.ip, ["203.0.113.24"])  
  
`region_code` |  |  **Type** |  string   
---|---  
**Description** |  The [ISO 3166-1 alpha-2 code](https://www.iso.org/obp/ui/#search/code/) for the country or region where the request originated from. If the region code cannot be determined, `origin.region_code` evaluates to an error.  **Warning:** Do not compare `origin.region_code` with the empty string. The behavior is undefined.  **Example:**
    
    
    origin.region_code == "GB"
    origin.region_code in ["US", "FR", "JP"]  
  
### `request.auth` attributes

This section lists the attributes supported by the `request.auth` object.

Attributes   
---  
`principal` |  |  **Type** |  string, list(string)   
---|---  
**Description** |  The unique ID of the user who issued the request.  The value for `request.auth.principal` must be one or more unique user IDs. The UUIDs can be obtained using the [Admin SDK Directory API](https://developers.google.com/admin-sdk/directory/v1/guides/manage-users#get_user).  The value must be in the following format: `https://accounts.google.com/UUID` Where UUID is the UUID of a user.  **Example:**
    
    
    request.auth.principal == "https://accounts.google.com/1134924314572461055"
    request.auth.principal in ["https://accounts.google.com/1134924314572461055", "https://accounts.google.com/3134824314572461115"]  
  
`claims.crd_str.pwd` |  |  **Type** |  boolean   
---|---  
**Description** |  User authenticated with a password.  **Example:**
    
    
    request.auth.claims.crd_str.pwd == true  
  
`claims.crd_str.push` |  |  **Type** |  boolean   
---|---  
**Description** |  User authenticated with a push notification to the mobile device.  **Example:**
    
    
    request.auth.claims.crd_str.push == true  
  
`claims.crd_str.sms` |  |  **Type** |  boolean   
---|---  
**Description** |  User authenticated using a code sent to SMS or via a phone call.  **Example:**
    
    
    request.auth.claims.crd_str.sms == true  
  
`claims.crd_str.swk` |  |  **Type** |  boolean   
---|---  
**Description** |  2SV used a software key, such as a phone, as security key.  **Example:**
    
    
    request.auth.claims.crd_str.swk == true  
  
`claims.crd_str.hwk` |  |  **Type** |  boolean   
---|---  
**Description** |  2SV used a hardware key, such as Google Titan Key.  **Example:**
    
    
    request.auth.claims.crd_str.hwk == true  
  
`claims.crd_str.otp` |  |  **Type** |  boolean   
---|---  
**Description** |  User authenticated with one time password methods (Google Authenticator and Backup Codes).  **Example:**
    
    
    request.auth.claims.crd_str.otp == true  
  
`claims.crd_str.mfa` |  |  **Type** |  boolean   
---|---  
**Description** |  User authenticated with any of the methods in this table except `pwd`.  **Note:** Software keys and passkeys (SWKs) meet multi-factor authentication (MFA) requirements but don't set the MFA claim to `true` because some flows are treated as a single strong factor. To allow passkeys, check for SWK.  **Example:**
    
    
    request.auth.claims.crd_str.mfa == true  
  
`request.auth.oauth.client_id` |  |  **Type** |  OAuthClientID   
---|---  
**Description** |  The client ID of the AI agent to allow or disallow access to MCP tools.  **Example:**
    
    
    request.auth.oauth.client_id == OAuthClientID  
  
**Important:** The MFA and SWK claims are independent. Passkeys might fulfill multi-factor requirements. When a user authenticates with a passkey, SWK might be set to `true`, but MFA might not automatically be set to `true`. 

To ensure your access level correctly handles both MFA and passkeys, use a combined logical expression, like the following: 
    
    
                  request.auth.claims.crd_str.mfa == true || request.auth.claims.crd_str.swk == true
                  
  
For more information about credential strength policy, see [Configuring a credential strength policy](https://docs.cloud.google.com/access-context-manager/docs/create-credential-strength-policy).

### `request.time` attributes

This section lists the attributes supported by the `request.time` object.

Attributes   
---  
`getFullYear()` |  |  **Type** |  string   
---|---  
**Description** |  Retrieves the year (example: 2023).  **Example:** `request.time.getFullYear("America/Los_Angeles") == 2024`  
`getMonth()` |  |  **Type** |  string   
---|---  
**Description** |  Retrieves the month, from 0 (January) to 11 (December).  **Example:** `request.time.getMonth("America/Los_Angeles") == 0` (January)   
`getDate()` |  |  **Type** |  string   
---|---  
**Description** |  Retrieves the day of the month, from 1 to 31.  **Example:** `request.time.getDate("America/Los_Angeles") == 1`  
`getDayOfMonth()` |  |  **Type** |  string   
---|---  
**Description** |  Retrieves the day of the month, from 0 to 30 (0 is the 1st day).  **Example:** `request.time.getDayOfMonth("America/Los_Angeles") == 0` (1st of the month)   
`getDayOfWeek()` |  |  **Type** |  string   
---|---  
**Description** |  Retrieves the day of the week, from 0 (Sunday) to 6 (Saturday).  **Example:** `request.time.getDayOfWeek("America/Los_Angeles") == 1` (Monday)   
`getDayOfYear()` |  |  **Type** |  string   
---|---  
**Description** |  Retrieves the day of the year, from 0 to 365.  **Example:** `request.time.getDayOfYear("America/Los_Angeles") == 0` (Jan 1st)   
`getHours()` |  |  **Type** |  string   
---|---  
**Description** |  Retrieves the hour of the day, from 0 (midnight) to 23 (11 PM).  **Example:** `request.time.getHours("America/Los_Angeles") == 19` (7 PM)   
`getMinutes()` |  |  **Type** |  string   
---|---  
**Description** |  Retrieves the minute of the hour, from 0 to 59.  **Example:** `request.time.getMinutes("America/Los_Angeles") == 30`  
  
### `levels` attribute

This section lists the attributes supported by the `levels` object.

Attributes   
---  
`LEVEL_NAME` |  |  **Type** |  boolean   
---|---  
**Description** |  `levels.LEVEL_NAME` corresponds to the name of an existing access level.  When used, the conditions of the specified access level must also be met in addition to the other requirements of your custom access level.  **Example:**
    
    
    levels.allow_corp_ips

Where `allow_corp_ips` is the name of an access level.   
  
### `device` attribute

This section lists the attributes supported by the `device` object. If no device associated with the identifiers in the request is found, all of the following attributes will evaluate to an error.

Attributes   
---  
`encryption_status` |  |  **Type** |  enum   
---|---  
**Description** |  Describes the encryption status of the device.  **Enum values:**
    
    
    enum DeviceEncryptionStatus {
      // The encryption status of the device is not specified or not known.
      ENCRYPTION_UNSPECIFIED == 0;
      // The device does not support encryption.
      ENCRYPTION_UNSUPPORTED == 1;
      // The device supports encryption, but is currently unencrypted.
      UNENCRYPTED == 2;
      // The device is encrypted.
      ENCRYPTED == 3;
    }

**Example:**
    
    
    device.encryption_status == DeviceEncryptionStatus.ENCRYPTED  
  
`is_admin_approved_device` |  |  **Type** |  boolean   
---|---  
**Description** |  Whether the device has been approved by the domain administrator.  **Example:**
    
    
    device.is_admin_approved_device == true  
  
`is_corp_owned_device` |  |  **Type** |  boolean   
---|---  
**Description** |  Whether the device is owned by the organization.  **Example:**
    
    
    device.is_corp_owned_device == true  
  
`is_secured_with_screenlock` |  |  **Type** |  boolean   
---|---  
**Description** |  Whether the device has its screen lock function enabled.  **Example:**
    
    
    device.is_secured_with_screenlock == true  
  
`os_type` |  |  **Type** |  enum   
---|---  
**Description** |  Identifies which operating system the device is using.  **Enum values:**
    
    
    enum OsType {
      // The operating system of the device is not specified or not known.
      OS_UNSPECIFIED == 0;
      // A desktop Mac operating system.
      DESKTOP_MAC == 1;
      // A desktop Windows operating system.
      DESKTOP_WINDOWS == 2;
      // A desktop Linux operating system.
      DESKTOP_LINUX == 3;
      // An Android operating system.
      ANDROID == 4;
      // An iOS operating system.
      IOS == 5;
      // A desktop ChromeOS operating system.
      DESKTOP_CHROME_OS == 6;
      // A Googlebook operating system.
      GOOGLEBOOK_OS == 8;
    }

**Example:**
    
    
    device.os_type == OsType.DESKTOP_MAC
    device.os_type != OsType.OS_UNSPECIFIED  
  
`vendors` |  |  **Type** |  map<string, Vendor> vendors;   
---|---  
**Description** |  **Preview** This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages).  The `vendors` object is used to access data provided by third-party security and endpoint management vendors. Each vendor may populate three shared top-level attributes: `is_compliant_device`, `is_managed_device`, and `device_health_score`.  Additionally, vendors may provide their own keys and values that are referenced using the `data` attribute. The available keys for the `data` attribute vary from vendor to vendor. Ensure that you are consistent when comparing the key value in your policy expression. For example, if you expect the key value to be a string or boolean, ensure that you compare it with a string or boolean in the policy expression correspondingly. Note that when the value is an integer, you should compare it with a double number in the policy expression.  To reference [device state](https://cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates/patch#path-parameters), use the format `key-acme` where `acme` is the organization's customer ID. You can get the customer ID from the `GET https://www.googleapis.com/admin/directory/v1/customers/my_customer` URL. The ID field in the response contains the customer ID starting with the letter `C`. Use the string after the letter `C`, excluding the letter `C`, for the customer ID.  **Note:** There is no complete list of available vendors and vendor-specific keys.  **Enum values:**
    
    
    // Health score of the device as provided by the vendor (possibly third party).
    enum DeviceHealthScore {
      // The health score for the device is not specified or unknown.
      DEVICE_HEALTH_SCORE_UNSPECIFIED = 0;
      // The health of the device is very poor.
      VERY_POOR = 1;
      // The health of the device is poor.
      POOR = 2;
      // The health of the device is ok.
      NEUTRAL = 3;
      // The health of the device is good.
      GOOD = 4;
      // The health of the device is very good.
      VERY_GOOD = 5;
    }

**Examples:**
    
    
    device.vendors["some_vendor"].is_compliant_device == true
    
    
    device.vendors["some_vendor"].is_managed_device == true
    
    
    device.vendors["some_vendor"].device_health_score == DeviceHealthScore.VERY_GOOD
    
    
    device.vendors["some_vendor"].data["is_device_compromised"] == true
    
    
    device.vendors["some_vendor"].data["some_num"] == 1.0

**Note:** `is_device_compromised` is only an example that represents a key defined by a vendor.   
`android_device_security.verified_boot` |  |  **Type** |  boolean   
---|---  
**Description** |  Whether the [Android verified boot](https://source.android.com/docs/security/features/verifiedboot) status is [`green`](https://source.android.com/docs/security/features/verifiedboot/boot-flow#communicating-verified-boot-state-to-android).  **Example:**
    
    
    device.android_device_security.verified_boot == true  
  
`android_device_security.cts_profile_match` |  |  **Type** |  boolean   
---|---  
**Description** |  Whether device passes [CTS profile compliance](https://developer.android.com/training/safetynet/attestation).  **Example:**
    
    
    device.android_device_security.cts_profile_match == true  
  
`android_device_security.verify_apps_enabled` |  |  **Type** |  boolean   
---|---  
**Description** |  Whether the device has [Google Play Protect](https://developers.google.com/android/play-protect) Verify Apps enabled.  **Example:**
    
    
    device.android_device_security.verify_apps_enabled == true  
  
`android_device_security.has_potentially_harmful_apps` |  |  **Type** |  boolean   
---|---  
**Description** |  Whether [potentially harmful apps](https://developers.google.com/android/play-protect/potentially-harmful-applications) were found on the device.  **Example:**
    
    
    device.android_device_security.has_potentially_harmful_apps == true  
  
`ios_device_security.is_device_jailbroken` |  |  **Type** |  boolean   
---|---  
**Description** |  Whether the iOS device was found to be [jailbroken](https://support.apple.com/guide/iphone/unauthorized-modification-of-ios-iph9385bb26a/ios).  **Example:**
    
    
    device.ios_device_security.is_device_jailbroken == true  
  
`verified_chrome_os` |  |  **Type** |  boolean   
---|---  
**Description** |  Whether the request comes from a device with a [verified Chrome OS](https://support.google.com/chrome/a/answer/7156268).  **Example:**
    
    
    device.verified_chrome_os == true  
  
`chrome.management_state` |  |  **Type** |  string   
---|---  
**Description** |  Is the browser managed, at the browser level or at the profile level, and by the enterprise under the correct domain.  A browser is considered to be managed if the policies are centrally managed and pushed, and that the domain of the managed browser or profile matches the expected domain on the server side.  Following are the available Chrome management states: | State  
---  
`UNMANAGED` | The browser or profile is not managed by any customer.  
`MANAGED_BY_OTHER_DOMAIN` | The browser or profile is managed by some other customer.  
`PROFILE_MANAGED` | The profile is managed by the customer.  
`BROWSER_MANAGED` | The browser is managed by the customer.  
  
**Example:**
    
    
    device.chrome.management_state in
        [
            ChromeManagementState.CHROME_MANAGEMENT_STATE_BROWSER_MANAGED,
            ChromeManagementState.CHROME_MANAGEMENT_STATE_PROFILE_MANAGED,
        ]  
  
`chrome.versionAtLeast` |  |  **Type** |  string   
---|---  
**Description** |  Is the browser above a certain minimum version.  **Example:**
    
    
    device.chrome.versionAtLeast("88.0.4321.44")  
  
`chrome.is_realtime_url_check_enabled` |  |  **Type** |  boolean   
---|---  
**Description** |  Is the real-time URL check connector enabled.  **Example:**
    
    
    device.chrome.is_realtime_url_check_enabled == true | false  
  
`chrome.is_file_upload_analysis_enabled` |  |  **Type** |  boolean   
---|---  
**Description** |  Is the file upload analysis connector enabled.  **Example:**
    
    
    device.chrome.is_file_upload_analysis_enabled == true | false  
  
`chrome.is_file_download_analysis_enabled` |  |  **Type** |  boolean   
---|---  
**Description** |  Is the file download analysis connector enabled.  **Example:**
    
    
    device.chrome.is_file_download_analysis_enabled == true | false  
  
`chrome.is_bulk_data_entry_analysis_enabled` |  |  **Type** |  boolean   
---|---  
**Description** |  Is the bulk text (paste) analysis connector enabled.  **Example:**
    
    
    device.chrome.is_bulk_data_entry_analysis_enabled == true | false  
  
`chrome.is_security_event_analysis_enabled` |  |  **Type** |  boolean   
---|---  
**Description** |  Is the security event reporting connector enabled.  **Example:**
    
    
    device.chrome.is_security_event_analysis_enabled == true | false  
  
`device.certificates.exists` |  |  **Type** |  boolean   
---|---  
**Description** |  A list of enterprise certificates associated with the device. This attribute is used with macros to iterate through the certificates and check their properties, such as validity.  **Example:**
    
    
    // Checks if the device has at least one valid enterprise certificate.
    device.certificates.exists(cert, cert.is_valid == true)  
  
### `api` attributes

This section lists the attributes supported by the `api` object.

Attributes   
---  
`mcp.is_mcp` |  |  **Type** |  boolean   
---|---  
**Description** |  Indicates whether the API call is being made by an MCP service.  **Example:**
    
    
    api.mcp.is_mcp == true  
  
`mcp.tool.is_read_only` |  |  **Type** |  boolean   
---|---  
**Description** |  Indicates whether the MCP tool invocation is in read-only mode.  **Example:**
    
    
    api.mcp.tool.is_read_only == true  
  
## Functions

Access Context Manager provides the following functions for use in the CEL expressions for custom access levels.

Functions   
---  
`inIpRange(address, [SUBNETS])` |  |  **Type** |  (string, list(string)) -> boolean   
---|---  
**Description** |  Checks whether an IP address belongs to one of the given subnets.  **Warning:** Do not use this function to check if the origin IP address is in a specific private IP subnet. Private IP addresses within Google are subject to change.  **Example:**
    
    
    inIpRange(origin.ip, ["192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24"])  
  
`device.versionAtLeast(minVersion)` |  |  **Type** |  DeviceType.(string) -> boolean   
---|---  
**Description** |  Checks whether the device operating system is at least a given version. We recommend that you use this function with the `device.os_type` attribute.  **Example:**
    
    
    device.versionAtLeast("10.0") == true  
  
`certificateBindingState(origin, device)` |  |  **Type** |  (Peer, DeviceType) -> integer   
---|---  
**Description** |  Checks if the client certificate associated with the origin matches the device and reports the state.  The state returned by the function can be one of the following: 

  * `CertificateBindingState.CERT_MATCHES_EXISTING_DEVICE`
  * `CertificateBindingState.CERT_NOT_MATCHING_EXISTING_DEVICE`
  * `CertificateBindingState.CERT_STATE_UNKNOWN`

**Example:**
    
    
    certificateBindingState(origin, device) == CertificateBindingState.CERT_MATCHES_EXISTING_DEVICE  
  
`startsWith()` |  |  **Type** |  string.(string) -> bool   
---|---  
**Description** |  Tests whether the string operand starts with the prefix argument.  **Example:**
    
    
    "Sample string".startsWith("Sample")  
  
`endsWith()` |  |  **Type** |  string.(string) -> bool   
---|---  
**Description** |  Tests whether the string operand ends with the suffix argument.  **Example:**
    
    
    "Sample string".endsWith("string")  
  
`origin.clientCertFingerprint()` |  |  **Type** |  Origin.() -> string   
---|---  
**Description** |  Returns the fingerprint of the certificate associated with the origin. You can use this in macros to test device certificates.  **Example:**
    
    
    // Checks if the enterprise certificate associated with the origin matches the device.
    device.certificates.exists(cert, cert.is_valid && cert.cert_fingerprint == origin.clientCertFingerprint())  
  
`originatesFromProjects(origin, [PROJECT_LIST])` |  |  **Type** |  (Origin, list(string)) -> boolean   
---|---  
**Description** |  Checks whether the request originates from a specific Google Cloud project or its associated tenant projects.  **Constraints:** Only project numbers are supported (for example, `"projects/1234567890"`). Alphanumeric project IDs are not permitted.  **Example:** To allow requests only from project `projects/1234567890` or `projects/9876543210`: 
    
    
    originatesFromProjects(origin, ["projects/1234567890", "projects/9876543210"])  
  
## Macros for CEL expressions

You can use the following macros in the CEL expressions for custom access levels:

Macro | Description  
---|---  
`has(e.f)` | Tests whether a field is available. See [Field Selection](https://github.com/google/cel-spec/blob/master/doc/langdef.md#field-selection) for more details. Example:  `has({"key": "value"}.key)` `has(device.vendors.some_vendor)`  
`e.all(x, p)` | Tests whether a predicate holds for all elements of a list `e` or keys of a map `e`. Here `x` is an identifier to be used in `p` which binds to the element or key. The `all()` macro combines per-element predicate results with the `and` (&&) operator, so if any predicate evaluates to false, the macro evaluates to false, ignoring any errors from other predicates. Example: This returns false because not all elements are greater than 1:   
`[1,2,3].all(x, x > 1)`  
`e.exists(x, p)` | Like the `all()` macro, but combines the predicate results with the `or` (||) operator. Example: This returns true because there is at least one element in the list greater than 1:   
`[1,2,3].exists(x, x > 1)` Checks if the enterprise certificate associated with the device matches the issuer:   
`device.certificates.exists(cert, cert.is_valid && cert.issuer == "EMAILADDRESS=test_inter1@beyondcorp.in, CN=inter_1, OU=BCEDemo_1, O=BCEDemo, L=NCR, ST=UP, C=IN")`  
`e.exists_one(x, p)` | Like the `exists()` macro, but evaluates to true only if the predicate of exactly one element or key evaluates to true, and the rest to false. Any other combination of boolean results evaluates to false, and any predicate error causes the macro to raise an error. Example:  This returns false because more than one element is greater than 1:   
`[1,2,3].exists_one(x, x > 1)`  
  
## Example CEL expressions

This section includes examples of CEL expressions used to create custom access levels.

### Example 1
    
    
    device.encryption_status == DeviceEncryptionStatus.ENCRYPTED && (origin.region_code in ["US"] || device.is_admin_approved_device)

This example represents an access level that requires the following conditions be met in order to allow a request:

  * The device that the request originated from is encrypted.

  * One or more of the following is true:

    * The request originated in the United States.

    * The device that the request originated from is approved by the domain administrator.




### Example 2
    
    
    (device.os_type == OsType.DESKTOP_WINDOWS && device.is_corp_owned_device) || (device.os_type == OsType.DESKTOP_MAC && device.is_admin_approved_device && device.versionAtLeast("10.11.0"))

This example represents an access level that requires the following conditions be met in order to allow a request:

  * One of the following is true:

    * The device that the request originated from uses a desktop Windows operating system and is owned by your organization.

    * The device that the request originated from uses a desktop Mac operating system, is approved by the domain administrator, and is using at least MacOS 10.11.




### Example 3
    
    
    (certificateBindingState(origin, device) == CertificateBindingState.CERT_MATCHES_EXISTING_DEVICE)

This example represents an access level that requires the following condition be met in order to allow a request:

  * The `certificateBindingState` extension function determines that the certificate presented at request time matches one of the device certificates that was registered when the device was enrolled in [endpoint verification](https://support.google.com/a/answer/9007320).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
