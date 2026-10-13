---
url: https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/fetch_enrichment_actions/
title: MCP Tools Reference: chronicle.googleapis.com \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:33.527208+00:00
---

# MCP Tools Reference: chronicle.googleapis.com  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/fetch_enrichment_actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  MCP Tools Reference: chronicle.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `fetch_enrichment_actions`

Retrieves a curated list of SOAR integration actions available for enriching a specific SIEM alert. This tool is similar to `list_integrations` and `list_integration_actions`, but it filters specifically for actions that are suitable for enrichment and are enabled for the environment where the alert originated.

For each integration, it provides:

  * **Integration ID and Display Name** : To identify the tool provider (e.g., 'VirusTotal', 'SafeBreach').
  * **Available Actions** : A list of specific enrichment functions (e.g., 'Get IP Report', 'Enrich Host').
  * **Action Parameters** : Detailed information for each parameter, including: `name` and `description`, `type` (e.g., 'String', 'Boolean'), `mandatory` flag, `default_value` and `optional_values_json` for dropdowns.
  * **AI Description** : A detailed, structured description of the action designed for the AI. It typically includes: **General Description** : What the action does and what data it retrieves. **Parameters Description** : A table explaining each parameter's purpose and constraints. **Flow Description** : A step-by-step breakdown of the action's execution logic.
  * **Entity Types** : A list of specific entity types that this action supports (e.g., 'ADDRESS', 'HOSTNAME', 'FILEHASH'). **Crucial** : You should only attempt to run this action on entities that match one of these types.



**Workflow Integration:**

  * Use this tool to discover what enrichment capabilities are available for the current alert.
  * **Critical Step** : Compare the `entity_types` of each available action against the actual entities found in the alert (via `fetch_alert_data`). Only plan to execute actions where there is a match.
  * The `integration` and `display_name` retrieved here are required for `execute_actions`.



**Use Cases:**

  * Discover available threat intelligence tools for enriching IPs or domains found in an alert.
  * Identify EDR actions that can provide host or process details for investigation.
  * Understand what parameters are required for specific enrichment actions.



The following sample demonstrate how to use `curl` to invoke the `fetch_enrichment_actions` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://chronicle.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "fetch_enrichment_actions",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for FetchActions.

### FetchActionsRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "customerId": string,
      "region": string,
      "siemAlertId": string
    }  
  
Fields  
---  
`projectId` |  `string` Required. Google Cloud project ID.  
`customerId` |  `string` Required. Chronicle customer ID.  
`region` |  `string` Required. Chronicle region (e.g., "us", "europe").  
`siemAlertId` |  `string` Required. The unique identifier of the alert in SIEM.  
  
## Output Schema

Response for FetchActions.

### FetchActionsResponse

JSON representation  
---  
      
    
    {
      "parent": string,
      "integrations": [
        {
          object ([AgentIntegrationDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/fetch_enrichment_actions#Output.Schema.AgentIntegrationDetails))
        }
      ]
    }  
  
Fields  
---  
`parent` |  `string` Output only. The parent, which owns the collection of actions.  
`integrations[]` |  `object (`[AgentIntegrationDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/fetch_enrichment_actions#Output.Schema.AgentIntegrationDetails)`)` List of all integrations that can be used to execute actions on the SIEM alert.  
  
### AgentIntegrationDetails

JSON representation  
---  
      
    
    {
      "integration": string,
      "integrationInstance": string,
      "displayName": string,
      "description": string,
      "actions": [
        {
          object ([AgentIntegrationAction](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/fetch_enrichment_actions#Output.Schema.AgentIntegrationAction))
        }
      ]
    }  
  
Fields  
---  
`integration` |  `string` Unique identifier of the integration.  
`integrationInstance` |  `string` Unique identifier of the integration instance.  
`displayName` |  `string` Display name of the integration.  
`description` |  `string` Description of the integration.  
`actions[]` |  `object (`[AgentIntegrationAction](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/fetch_enrichment_actions#Output.Schema.AgentIntegrationAction)`)` List of all actions that can be executed on the SIEM alert using this integration.  
  
### AgentIntegrationAction

JSON representation  
---  
      
    
    {
      "displayName": string,
      "description": string,
      "parameters": [
        {
          object ([AgentActionParameter](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/fetch_enrichment_actions#Output.Schema.AgentActionParameter))
        }
      ],
      "entityTypes": [
        string
      ],
      "shortDescription": string,
      "parametersDescription": string
    }  
  
Fields  
---  
`displayName` |  `string` The name of the action.  
`description` |  `string` The description of the action.  
`parameters[]` |  `object (`[AgentActionParameter](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/fetch_enrichment_actions#Output.Schema.AgentActionParameter)`)` The parameters required for the action.  
`entityTypes[]` |  `string` The entity types that the action supports.  
`shortDescription` |  `string` Output only. The short description of the action.  
`parametersDescription` |  `string` Output only. Description of the parameters for AI use.  
  
### AgentActionParameter

JSON representation  
---  
      
    
    {
      "mandatory": boolean,
      "defaultValue": string,
      "description": string,
      "name": string,
      "value": string,
      "type": string,
      "optionalValuesJson": string
    }  
  
Fields  
---  
`mandatory` |  `boolean` Required. Whether the parameter is mandatory.  
`defaultValue` |  `string` The default value of the parameter.  
`description` |  `string` The description of the parameter.  
`name` |  `string` The name of the parameter.  
`value` |  `string` The value of the parameter.  
`type` |  `string` Required. The type of the parameter.  
`optionalValuesJson` |  `string` The optional values for the parameter in JSON format.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-27 UTC."],[],[]] 
