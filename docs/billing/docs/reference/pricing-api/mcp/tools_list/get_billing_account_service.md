---
url: https://docs.cloud.google.com/billing/docs/reference/pricing-api/mcp/tools_list/get_billing_account_service/
title: MCP Tools Reference: cloudbilling.googleapis.com \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:23.381742+00:00
---

# MCP Tools Reference: cloudbilling.googleapis.com  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/reference/pricing-api/mcp/tools_list/get_billing_account_service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  MCP Tools Reference: cloudbilling.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_billing_account_service`

Gets a billing account service visible to a billing account.

The following code sample shows how to use `curl` to call the `get_billing_account_service` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://cloudbilling.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_billing_account_service",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `GetBillingAccountService`.

### GetBillingAccountServiceRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the `billing account service` to retrieve. Format: billingAccounts/{billing_account}/services/{service}  
  
## Output Schema

Encapsulates a Google Cloud service visible to a `billing account`.

### BillingAccountService

JSON representation  
---  
      
    
    {
      "name": string,
      "serviceId": string,
      "displayName": string
    }  
  
Fields  
---  
`name` |  `string` Resource name for the `BillingAccountService`. Example: "billingAccounts/012345-567890-ABCDEF/services/DA34-426B-A397".  
`serviceId` |  `string` Identifier for the service. It is the string after the collection identifier "services/". Example: "DA34-426B-A397".  
`displayName` |  `string` Description of the `BillingAccountService`. Example: "BigQuery", "Compute Engine".  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
