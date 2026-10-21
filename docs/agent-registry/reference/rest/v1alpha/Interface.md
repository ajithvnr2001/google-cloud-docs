---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Interface/
title: Interface \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:46.660831+00:00
---

# Interface  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Interface/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  Interface Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ProtocolBinding



Represents the connection details for an Agent or MCP Server.

JSON representation  
---  
      
    
    {
      "url": string,
      "protocolBinding": enum ([ProtocolBinding](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Interface#ProtocolBinding))
    }  
  
Fields  
---  
`url` |  `string` Required. The destination URL.  
`protocolBinding` |  `enum (`[ProtocolBinding](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Interface#ProtocolBinding)`)` Required. The protocol binding of the interface.  
  
## ProtocolBinding

The protocol binding of the interface.

Enums  
---  
`PROTOCOL_BINDING_UNSPECIFIED` | Unspecified transport protocol.  
`JSONRPC` | JSON-RPC specification.  
`GRPC` | gRPC specification.  
`HTTP_JSON` | HTTP+JSON specification.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
