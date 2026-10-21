---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MigrationWarning/
title: MigrationWarning \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:51.969741+00:00
---

# MigrationWarning  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MigrationWarning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  MigrationWarning Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * WarningCode
  * LocalizedMessage
    * JSON representation
  * Link
    * JSON representation



Represents migration resource warning information that can be used with google.rpc.Status message. MigrationWarning is used to present the user with warning information in migration operations.

JSON representation  
---  
      
    
    {
      "code": enum ([WarningCode](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MigrationWarning#WarningCode)),
      "warningMessage": {
        object ([LocalizedMessage](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MigrationWarning#LocalizedMessage))
      },
      "actionItem": {
        object ([LocalizedMessage](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MigrationWarning#LocalizedMessage))
      },
      "helpLinks": [
        {
          object ([Link](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MigrationWarning#Link))
        }
      ],
      "warningTime": string
    }  
  
Fields  
---  
`code` |  `enum (`[WarningCode](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MigrationWarning#WarningCode)`)` The warning code.  
`warningMessage` |  `object (`[LocalizedMessage](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MigrationWarning#LocalizedMessage)`)` Output only. The localized warning message.  
`actionItem` |  `object (`[LocalizedMessage](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MigrationWarning#LocalizedMessage)`)` Output only. Suggested action for solving the warning.  
`helpLinks[]` |  `object (`[Link](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MigrationWarning#Link)`)` Output only. URL(s) pointing to additional information on handling the current warning.  
`warningTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the warning occurred.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
## WarningCode

Represents possible warning codes.

Enums  
---  
`WARNING_CODE_UNSPECIFIED` | Default value. This value is not used.  
`ADAPTATION_WARNING` | A warning originated from OS Adaptation.  
  
## LocalizedMessage

Provides a localized error message that is safe to return to the user which can be attached to an RPC error.

JSON representation  
---  
      
    
    {
      "locale": string,
      "message": string
    }  
  
Fields  
---  
`locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`message` |  `string` The localized error message in the above locale.  
  
## Link

Describes a URL link.

JSON representation  
---  
      
    
    {
      "description": string,
      "url": string
    }  
  
Fields  
---  
`description` |  `string` Describes what the link offers.  
`url` |  `string` The URL of the link.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
