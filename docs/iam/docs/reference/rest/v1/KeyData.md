---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/KeyData/
title: KeyData \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:49.897041+00:00
---

# KeyData  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/KeyData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  KeyData Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * KeyFormat
  * KeySpec



Represents a public key data along with its format.

JSON representation  
---  
      
    
    {
      "format": enum ([KeyFormat](https://docs.cloud.google.com/iam/docs/reference/rest/v1/KeyData#KeyFormat)),
      "notBeforeTime": string,
      "notAfterTime": string,
      "key": string,
      "keySpec": enum ([KeySpec](https://docs.cloud.google.com/iam/docs/reference/rest/v1/KeyData#KeySpec))
    }  
  
Fields  
---  
`format` |  `enum (`[KeyFormat](https://docs.cloud.google.com/iam/docs/reference/rest/v1/KeyData#KeyFormat)`)` Output only. The format of the key.  
`notBeforeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Earliest timestamp when this key is valid. Attempts to use this key before this time will fail. Only present if the key data represents a X.509 certificate.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`notAfterTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Latest timestamp when this key is valid. Attempts to use this key after this time will fail. Only present if the key data represents a X.509 certificate.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`key` |  `string` Output only. The key data. The format of the key is represented by the `[format](https://docs.cloud.google.com/iam/docs/reference/rest/v1/KeyData#FIELDS.format)` field.  
`keySpec` |  `enum (`[KeySpec](https://docs.cloud.google.com/iam/docs/reference/rest/v1/KeyData#KeySpec)`)` Required. The specifications for the key.  
  
## KeyFormat

The supported formats for the public key.

Enums  
---  
`KEY_FORMAT_UNSPECIFIED` | No format has been specified. This is an invalid format and must not be used.  
`RSA_X509_PEM` | A RSA public key wrapped in an X.509v3 certificate ([RFC5280](https://www.ietf.org/rfc/rfc5280.txt)), encoded in base64, and wrapped in [public certificate label](https://datatracker.ietf.org/doc/html/rfc7468#section-5.1).  
  
## KeySpec

Allowed list of specifications for the key.

Enums  
---  
`KEY_SPEC_UNSPECIFIED` | No key specification specified.  
`RSA_2048` | A 2048 bit RSA key.  
`RSA_3072` | A 3072 bit RSA key.  
`RSA_4096` | A 4096 bit RSA key.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-28 UTC."],[],[]] 
