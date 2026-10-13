---
url: https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_connector_event/
title: MCP Tools Reference: chronicle.googleapis.com \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:58.826650+00:00
---

# MCP Tools Reference: chronicle.googleapis.com  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_connector_event/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  MCP Tools Reference: chronicle.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_connector_event`

Retrieves a specific connector event associated with a case alert in Chronicle SIEM.

Provides detailed information about a single connector event, including its raw data.

**Workflow Integration:** \- Used to drill down into a specific connector event from a list of events within a case alert. - Enables other systems to get the current state of a connector event before taking action.

**Use Cases:** \- An analyst clicks on a connector event in the SOAR UI to view its full details. - An automated playbook fetches a connector event to extract specific indicators of compromise (IoCs).

**Important Note:** \- The `connector_event_id`, `case_id`, and `case_alert_id` arguments MUST be the integer IDs of the respective entities. - If you have a non-integer identifier (e.g., a GUID or event identifier), use `list_connector_events` to get the integer IDs first. - Then use `get_connector_event` with the integer IDs.

Args: project_id (str): Google Cloud project ID (required). customer_id (str): Chronicle customer ID (required). region (str): Chronicle region (e.g., "us", "europe") (required). case_id (str): The integer Case ID of the connector event to retrieve. case_alert_id (str): The integer Case Alert ID of the connector event to retrieve. connector_event_id (str): The integer ID of the connector event to retrieve. expand (str, optional): A comma-separated list of fields to expand in the response (e.g., 'event_json_data').

Returns: ConnectorEvent: The full ConnectorEvent object with all its details. Returns an error message if the connector event is not found.

Example Usage: # Get details for a specific connector event using integer IDs get_connector_event(project_id='123', region='us', customer_id='abc', case_id='456', case_alert_id='789', connector_event_id='101112')

Next Steps (using MCP-enabled tools): - Use 'list_connector_events' to see other connector events in the same case alert.

The following sample demonstrate how to use `curl` to invoke the `get_connector_event` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://chronicle.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_connector_event",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for GetConnectorEvent.

### GetConnectorEventRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "customerId": string,
      "region": string,
      "caseId": string,
      "caseAlertId": string,
      "connectorEventId": string,
      "expand": string
    }  
  
Fields  
---  
`projectId` |  `string` Project ID of the customer.  
`customerId` |  `string` Customer ID of the customer.  
`region` |  `string` Region of the customer.  
`caseId` |  `string` Case ID of the case alert.  
`caseAlertId` |  `string` Case alert ID of the case alert.  
`connectorEventId` |  `string` Connector event ID of the connector event.  
`expand` |  `string` Configures expansion of ConnectorEvents in the response. If not specified, ConnectorEvents are returned without any expansion. The expand string is a comma separated list of fields. Supported fields: * `event_json_data`  
  
## Output Schema

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. ConnectorEvent - Chronicle Connector Event. Types of ConnectorEvents: general, case-spesific

### ConnectorEvent

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "alertIdentifier": string,
      "environment": string,
      "eventIdentifier": string,
      "alertGroupIdentifier": string,
      "mappedEventJson": string,
      "eventJsonData": {
        object ([RawEventData](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_connector_event#Output.Schema.RawEventData))
      },
      "caseId": string,
      "id": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the ConnectorEvent. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseAlerts/{case_alert}/connectorEvents/{connector_event}  
`createTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The create_time of the ConnectorEvent.  
`updateTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The update_time of the ConnectorEvent.  
`alertIdentifier` |  `string` Output only. The alert_identifier of the ConnectorEvent.  
`environment` |  `string` Output only. The environment of the ConnectorEvent.  
`eventIdentifier` |  `string` Output only. The event_identifier of the ConnectorEvent.  
`alertGroupIdentifier` |  `string` Output only. The alert_group_identifier of the ConnectorEvent.  
`mappedEventJson` |  `string` Output only. The mapped_event_json of the ConnectorEvent.  
`eventJsonData` |  `object (`[RawEventData](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_connector_event#Output.Schema.RawEventData)`)` Output only. The raw_event of the ConnectorEvent.  
`caseId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The case_id of the ConnectorEvent.  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The id of the ConnectorEvent.  
  
### RawEventData

JSON representation  
---  
      
    
    {
      "rawEvent": string
    }  
  
Fields  
---  
`rawEvent` |  `string` Output only. The raw event of the ConnectorEvent.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-15 UTC."],[],[]] 
