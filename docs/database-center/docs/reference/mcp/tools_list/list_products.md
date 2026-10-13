---
url: https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products/
title: MCP Tools Reference: databasecenter.googleapis.com \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:30.216214+00:00
---

# MCP Tools Reference: databasecenter.googleapis.com  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  MCP Tools Reference: databasecenter.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_products`

Provides a list of all possible database products which can be used to filter database resources.

The following sample demonstrate how to use `curl` to invoke the `list_products` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://databasecenter.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_products",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

QueryProductsRequest is the request to get a list of products.

### QueryProductsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization.The allowed values are:

  * projects/{PROJECT_ID}/locations/{LOCATION} (e.g.,"projects/foo-bar/locations/us-central1")
  * projects/{PROJECT_NUMBER}/locations/{LOCATION} (e.g.,"projects/12345678/locations/us-central1")
  * folders/{FOLDER_NUMBER}/locations/{LOCATION} (e.g.,"folders/1234567/locations/us-central1")
  * organizations/{ORGANIZATION_NUMBER}/locations/{LOCATION} (e.g.,"organizations/123456/locations/us-central1")
  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`pageSize` |  `integer` Optional. If unspecified, at most 50 products will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `ListLocations` call. Provide this to retrieve the subsequent page. All other parameters except page size should match the call that provided the page page token.  
  
## Output Schema

QueryProductsResponse represents the response containing a list of products.

### QueryProductsResponse

JSON representation  
---  
      
    
    {
      "products": [
        {
          object ([Product](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products#Output.Schema.Product))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`products[]` |  `object (`[Product](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products#Output.Schema.Product)`)` List of database products returned.  
`nextPageToken` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
### Product

JSON representation  
---  
      
    
    {
      "type": enum (ProductType),
      "engine": enum (Engine),
      "version": string,
      "minorVersion": string
    }  
  
Fields  
---  
`type` |  `enum (`ProductType`)` Optional. Type of specific database product. It could be CloudSQL, AlloyDB etc..  
`engine` |  `enum (`Engine`)` Optional. The specific engine that the underlying database is running.  
`version` |  `string` Optional. Version of the underlying database engine. Example values: For MySQL, it could be "8.0", "5.7" etc. For Postgres, it could be "14", "15" etc.  
`minorVersion` |  `string` Optional. Minor version of the underlying database engine. Example values: For MySQL, it could be "8.0.35", "5.7.25" etc. For PostgreSQL, it could be "14.4", "15.5" etc.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
