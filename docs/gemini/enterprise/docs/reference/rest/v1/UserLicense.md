---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/UserLicense/
title: UserLicense \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:44.052877+00:00
---

# UserLicense  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/UserLicense/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  UserLicense Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * LicenseAssignmentState



User License information assigned by the admin.

JSON representation  
---  
      
    
    {
      "userPrincipal": string,
      "userProfile": string,
      "licenseAssignmentState": enum ([LicenseAssignmentState](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/UserLicense#LicenseAssignmentState)),
      "licenseConfig": string,
      "createTime": string,
      "updateTime": string,
      "lastLoginTime": string
    }  
  
Fields  
---  
`userPrincipal` |  `string` Required. Immutable. The user principal of the User, could be email address or other prinical identifier. This field is immutable. Admin assign licenses based on the user principal.  
`userProfile` |  `string` Optional. The user profile. We user user full name(First name + Last name) as user profile.  
`licenseAssignmentState` |  `enum (`[LicenseAssignmentState](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/UserLicense#LicenseAssignmentState)`)` Output only. License assignment state of the user. If the user is assigned with a license config, the user login will be assigned with the license; If the user's license assignment state is unassigned or unspecified, no license config will be associated to the user;  
`licenseConfig` |  `string` Optional. The full resource name of the Subscription(LicenseConfig) assigned to the user.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. User created timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. User update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastLoginTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. User last logged in time. If the user has not logged in yet, this field will be empty.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## LicenseAssignmentState

License assignment state enumeration.

Enums  
---  
`LICENSE_ASSIGNMENT_STATE_UNSPECIFIED` | Default value.  
`ASSIGNED` | License assigned to the user.  
`UNASSIGNED` | No license assigned to the user. Deprecated, translated to NO_LICENSE.  
`NO_LICENSE` | No license assigned to the user.  
`NO_LICENSE_ATTEMPTED_LOGIN` | User attempted to login but no license assigned to the user. This state is only used for no user first time login attempt but cannot get license assigned. Users already logged in but cannot get license assigned will be assigned NO_LICENSE state(License could be unassigned by admin).  
`BLOCKED` | User is blocked from assigning a license.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-08 UTC."],[],[]] 
