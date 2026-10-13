---
url: https://docs.cloud.google.com/chronicle/docs/reference/mcp/execute_bulk_close_case/
title: MCP Tools Reference: chronicle.googleapis.com \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:57:38.581218+00:00
---

# MCP Tools Reference: chronicle.googleapis.com  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/mcp/execute_bulk_close_case/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  MCP Tools Reference: chronicle.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `execute_bulk_close_case`

Closes one or more cases in bulk. This is the only tool that can change the status of a case to 'CLOSED'.

This tool allows for the efficient closure of multiple cases at once, which is useful for resolving incidents that have been fully investigated or for cleaning up old cases. It can also be used to close a single case.

**Workflow Integration:** \- Used in automated playbooks to close cases after a successful remediation workflow. - Enables SOC managers or senior analysts to perform bulk cleanup of resolved or irrelevant cases from a queue. - Can be integrated into custom scripts for case management tasks, such as automatically closing cases that have been inactive for a certain period.

**Use Cases:** \- A playbook automatically closes a set of related cases after the root cause has been addressed and all associated alerts have been triaged. - An analyst closes a single case after completing their investigation and documenting the findings. - A SOC manager selects multiple resolved cases from a dashboard and closes them in a single action.

Args: project_id (str): Google Cloud project ID (required). The ID of the Google Cloud project associated with the Chronicle instance. customer_id (str): Chronicle customer ID (required). The unique identifier for the Chronicle customer instance. region (str): Chronicle region (e.g., "us", "europe") (required). The geographical region where the Chronicle instance is hosted. cases_ids (list of int): A list of case IDs to be closed (required). Each ID uniquely identifies a case in Chronicle. close_reason (str): The reason for closing the cases (required). Possible values: 'MALICIOUS', 'NOT_MALICIOUS', 'MAINTENANCE', 'INCONCLUSIVE', 'UNKNOWN'. - `MALICIOUS`: The case was closed because malicious activity was confirmed. - `NOT_MALICIOUS`: The case was closed because the activity was determined to be benign. - `MAINTENANCE`: The case was closed due to maintenance or system-related activities. - `INCONCLUSIVE`: The investigation was inconclusive, and a definitive determination could not be made. - `UNKNOWN`: The reason for closure is unknown or not specified. root_cause (str, required): The root cause of the incident that led to the case closure. A detailed explanation of the underlying factor that caused the incident. close_comment (str, required): A comment to be added to each case upon closure. This provides additional context or notes regarding the closure.

Note: The ability to update custom fields via `dynamic_parameters` is intentionally omitted from this bulk operation, as the Google SecOps UI advises that custom fields are not updated during bulk closure and should be updated on a per-case basis.

Returns: An empty response object if the operation is successful. Returns an error message if the operation fails, for example, if one of the cases does not exist or the user does not have permission to close it.

Example Usage: # Close a single case execute_bulk_close_case( project_id='123', region='us', customer_id='abc', cases_ids=[456], close_reason='NOT_MALICIOUS', root_cause='False positive identified', close_comment='Closing due to false positive.' )
    
    
    # Close multiple cases in bulk
            execute_bulk_close_case(
                project_id='123',
                region='us',
                customer_id='abc',
                cases_ids=[101, 102, 103],
                close_reason='MALICIOUS',
                root_cause='Phishing campaign identified and blocked.'
            )
            

Next Steps (using MCP-enabled tools): - Use 'list_cases' with a filter for 'status="CLOSED"' to verify that the cases have been closed. - Use 'get_case' for one of the closed cases to check that the close reason, root cause, and comment have been correctly applied.

The following sample demonstrate how to use `curl` to invoke the `execute_bulk_close_case` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://chronicle.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "execute_bulk_close_case",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for ExecuteBulkCloseCase. Next ID: 9

### ExecuteBulkCloseCaseRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "customerId": string,
      "region": string,
      "casesIds": [
        integer
      ],
      "closeReason": string,
    
      // Union field _root_cause can be only one of the following:
      "rootCause": string
      // End of list of possible types for union field _root_cause.
    
      // Union field _close_comment can be only one of the following:
      "closeComment": string
      // End of list of possible types for union field _close_comment.
    }  
  
Fields  
---  
`projectId` |  `string` Project ID of the customer.  
`customerId` |  `string` Customer ID of the customer.  
`region` |  `string` Region of the customer.  
`casesIds[]` |  `integer` Case IDs to close.  
`closeReason` |  `string` Reason for closing.  
Union field `_root_cause`.`_root_cause` can be only one of the following:  
`rootCause` |  `string` Root cause.  
Union field `_close_comment`.`_close_comment` can be only one of the following:  
`closeComment` |  `string` Close comment.  
  
## Output Schema

Response message for ExecuteBulkCloseCase.

### Tool Annotations

Destructive Hint: ✅ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-15 UTC."],[],[]] 
