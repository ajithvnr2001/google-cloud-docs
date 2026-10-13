---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig/
title: ProxyProtocolConfig \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:14.284772+00:00
---

# ProxyProtocolConfig  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Reference ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference)



Send feedback 

#  ProxyProtocolConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ContextualHeaders
    * JSON representation
  * DelegatedUserInfo
    * JSON representation
  * OutputType
  * DelegatedGroupInfo
    * JSON representation
  * DelegatedDeviceInfo
    * JSON representation
  * DelegatedDispatchInfo
    * JSON representation
  * GatewayIdentity



The configuration for the proxy.

JSON representation  
---  
      
    
    {
      "allowedClientHeaders": [
        string
      ],
      "contextualHeaders": {
        object ([ContextualHeaders](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#ContextualHeaders))
      },
      "metadataHeaders": {
        string: string,
        ...
      },
      "gatewayIdentity": enum ([GatewayIdentity](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#GatewayIdentity)),
      "clientIp": boolean
    }  
  
Fields  
---  
`allowedClientHeaders[]` |  `string` Optional. List of the allowed client header names.  
`contextualHeaders` |  `object (`[ContextualHeaders](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#ContextualHeaders)`)` Optional. Configuration for the contextual headers.  
`metadataHeaders` |  `map (key: string, value: string)` Optional. Custom resource specific headers along with the values. The names should conform to RFC 9110:

> Field names can contain alphanumeric characters, hyphens, and periods, can contain only ASCII-printable characters and tabs, and must start with a letter.  
  
`gatewayIdentity` |  `enum (`[GatewayIdentity](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#GatewayIdentity)`)` Optional. The security gateway identity configuration.  
`clientIp` |  `boolean` Optional. Client IP configuration. The client IP address is included if true.  
  
## ContextualHeaders

Contextual headers configuration.

JSON representation  
---  
      
    
    {
      "userInfo": {
        object ([DelegatedUserInfo](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#DelegatedUserInfo))
      },
      "groupInfo": {
        object ([DelegatedGroupInfo](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#DelegatedGroupInfo))
      },
      "deviceInfo": {
        object ([DelegatedDeviceInfo](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#DelegatedDeviceInfo))
      },
      "dispatchInfo": {
        object ([DelegatedDispatchInfo](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#DelegatedDispatchInfo))
      },
      "outputType": enum ([OutputType](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#OutputType))
    }  
  
Fields  
---  
`userInfo` |  `object (`[DelegatedUserInfo](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#DelegatedUserInfo)`)` Optional. User details.  
`groupInfo` |  `object (`[DelegatedGroupInfo](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#DelegatedGroupInfo)`)` Optional. Group details.  
`deviceInfo` |  `object (`[DelegatedDeviceInfo](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#DelegatedDeviceInfo)`)` Optional. The device information configuration.  
`dispatchInfo` |  `object (`[DelegatedDispatchInfo](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#DelegatedDispatchInfo)`)` Optional. The dispatch information configuration.  
`outputType` |  `enum (`[OutputType](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#OutputType)`)` Optional. Default output type for all enabled headers.  
  
## DelegatedUserInfo

The configuration information for the delegated user.

JSON representation  
---  
      
    
    {
      "outputType": enum ([OutputType](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#OutputType))
    }  
  
Fields  
---  
`outputType` |  `enum (`[OutputType](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#OutputType)`)` Optional. The delegated user's information.  
  
## OutputType

The output type of the headers.

Enums  
---  
`OUTPUT_TYPE_UNSPECIFIED` | The unspecified output type.  
`PROTOBUF` | Protobuf output type.  
`JSON` | JSON output type.  
`NONE` | Explicitly disable header output.  
  
## DelegatedGroupInfo

The delegated group configuration details.

JSON representation  
---  
      
    
    {
      "outputType": enum ([OutputType](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#OutputType))
    }  
  
Fields  
---  
`outputType` |  `enum (`[OutputType](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#OutputType)`)` Optional. The output type of the delegated group information.  
  
## DelegatedDeviceInfo

The delegated device information configuration.

JSON representation  
---  
      
    
    {
      "outputType": enum ([OutputType](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#OutputType))
    }  
  
Fields  
---  
`outputType` |  `enum (`[OutputType](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#OutputType)`)` Optional. The output type details for the delegated device.  
  
## DelegatedDispatchInfo

The delegated dispatch information configuration.

JSON representation  
---  
      
    
    {
      "outputType": enum ([OutputType](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#OutputType))
    }  
  
Fields  
---  
`outputType` |  `enum (`[OutputType](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig#OutputType)`)` Optional. The output type details for the delegated dispatch information.  
  
## GatewayIdentity

The security gateway identity type.

Enums  
---  
`GATEWAY_IDENTITY_UNSPECIFIED` | Unspecified gateway identity.  
`RESOURCE_NAME` | Resource name for gateway identity, in the format: projects/{projectId}/locations/{locationId}/securityGateways/{securityGatewayId}  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-23 UTC."],[],[]] 
