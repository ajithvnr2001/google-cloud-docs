---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SecuritySettings/
title: SecuritySettings \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:01:14.709529+00:00
---

# SecuritySettings  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SecuritySettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  SecuritySettings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EndpointControlPolicy
    * JSON representation
  * EndpointControlPolicy.EnforcementScope



Project/Location level security settings for CES.

JSON representation  
---  
      
    
    {
      "name": string,
      "endpointControlPolicy": {
        object ([EndpointControlPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SecuritySettings#EndpointControlPolicy))
      },
      "createTime": string,
      "updateTime": string,
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the security settings. Format: `projects/{project}/locations/{location}/securitySettings`  
`endpointControlPolicy` |  `object (`[EndpointControlPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SecuritySettings#EndpointControlPolicy)`)` Optional. Endpoint control related settings.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time of the security settings.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of the security settings.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. Etag of the security settings.  
  
## EndpointControlPolicy

Defines project/location level endpoint control policy.

JSON representation  
---  
      
    
    {
      "enforcementScope": enum ([EndpointControlPolicy.EnforcementScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SecuritySettings#EndpointControlPolicy.EnforcementScope)),
      "allowedOrigins": [
        string
      ]
    }  
  
Fields  
---  
`enforcementScope` |  `enum (`[EndpointControlPolicy.EnforcementScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SecuritySettings#EndpointControlPolicy.EnforcementScope)`)` Optional. The scope in which this policy's allowedOrigins list is enforced.  
`allowedOrigins[]` |  `string` Optional. The allowed HTTP(s) origins that tools in the App are able to directly call. The enforcement depends on the value of enforcementScope and the VPC-SC status of the project. If a port number is not provided, all ports will be allowed. Otherwise, the port number must match exactly. For example, "https://example.com" will match "https://example.com:443" and any other port. "https://example.com:443" will only match "https://example.com:443".  
  
## EndpointControlPolicy.EnforcementScope

Defines the scope in which this policy's allowedOrigins list is enforced.

Enums  
---  
`ENFORCEMENT_SCOPE_UNSPECIFIED` | Unspecified. This policy will be treated as VPCSC_ONLY.  
`VPCSC_ONLY` | This policy applies only when VPC-SC is active.  
`ALWAYS` | This policy ALWAYS applies, regardless of VPC-SC status.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
