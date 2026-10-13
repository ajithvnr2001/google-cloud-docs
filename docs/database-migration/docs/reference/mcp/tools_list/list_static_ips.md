---
url: https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_static_ips/
title: MCP Tools Reference: datamigration \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:25.839043+00:00
---

# MCP Tools Reference: datamigration  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_static_ips/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  MCP Tools Reference: datamigration Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_static_ips`

When you migrate a database into Google Cloud using DMS, Google needs a way to securely connect to your source database to read the data. If you choose the Static-IP connectivity method to connect to your source database, you will need to allow incoming traffic from DMS's specific, trusted IPs. This tool lists the IP addresses (matching the provided resource name) that should be allowlisted by the customer.

  * The resource `name` parameter is in the form `projects/{project name}/locations/{location}`, for example: `projects/my-project/locations/us-central1`.



The following sample demonstrate how to use `curl` to invoke the `list_static_ips` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://datamigration.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_static_ips",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for 'ListStaticIps' request.

### ListStaticIpsRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name for the location for which static IPs should be returned. Must be in the format `projects/*/locations/*`. For example: 'projects/my-project/locations/us-central1'  
  
## Output Schema

Response message for a 'FetchStaticIps' request.

### FetchStaticIpsResponse

JSON representation  
---  
      
    
    {
      "staticIps": [
        string
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`staticIps[]` |  `string` List of static IPs.  
`nextPageToken` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
