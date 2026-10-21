---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/get_certificate_authority/
title: MCP Tools Reference: memorystore.googleapis.com \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:04:49.425033+00:00
---

# MCP Tools Reference: memorystore.googleapis.com  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/get_certificate_authority/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  MCP Tools Reference: memorystore.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_certificate_authority`

Get the certificate authority for a Memorystore for Valkey instance.

The following sample demonstrate how to use `curl` to invoke the `get_certificate_authority` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://memorystore.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_certificate_authority",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for `GetCertificateAuthority`.

### GetCertificateAuthorityRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the certificate authority. Format: projects/{project}/locations/{location}/instances/{instance}/certificateAuthority  
  
## Output Schema

A certificate authority for an instance.

### CertificateAuthority

JSON representation  
---  
      
    
    {
      "name": string,
    
      // Union field server_ca can be only one of the following:
      "managedServerCa": {
        object ([ManagedCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/get_certificate_authority#Output.Schema.ManagedCertificateAuthority))
      }
      // End of list of possible types for union field server_ca.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique name of the certificate authority. Format: projects/{project}/locations/{location}/instances/{instance}  
Union field `server_ca`. Information about the server certificate authority. `server_ca` can be only one of the following:  
`managedServerCa` |  `object (`[ManagedCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/get_certificate_authority#Output.Schema.ManagedCertificateAuthority)`)` A managed server certificate authority.  
  
### ManagedCertificateAuthority

JSON representation  
---  
      
    
    {
      "caCerts": [
        {
          object ([CertChain](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/get_certificate_authority#Output.Schema.CertChain))
        }
      ]
    }  
  
Fields  
---  
`caCerts[]` |  `object (`[CertChain](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/get_certificate_authority#Output.Schema.CertChain)`)` PEM encoded CA certificate chains for managed server authentication.  
  
### CertChain

JSON representation  
---  
      
    
    {
      "certificates": [
        string
      ]
    }  
  
Fields  
---  
`certificates[]` |  `string` The certificates that form the CA chain in order of leaf to root.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
