---
url: https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_rule_errors/
title: MCP Tools Reference: chronicle.googleapis.com \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:03.443142+00:00
---

# MCP Tools Reference: chronicle.googleapis.com  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_rule_errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  MCP Tools Reference: chronicle.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_rule_errors`

Lists execution errors for a specific Chronicle SIEM rule.

Helps in troubleshooting rules that might not be generating detections as expected or are failing during execution.

**Agent Responsibilities:** \- Parse the JSON response to extract the list from the `ruleExecutionErrors` key. - Handle the `nextPageToken` for pagination if more results exist.

**Workflow Integration:** \- **Rule Troubleshooting:** If a rule is not producing expected detections or alerts, check for execution errors. - **Rule Development:** After deploying a new or modified rule, check for errors to ensure it's syntactically correct and running properly. - **SIEM Health Monitoring:** Periodically check for rules with high error counts to maintain SIEM operational health.

**Use Cases:** \- Investigate why a specific rule (e.g., "ru_...") has not generated any detections. - Check for errors after modifying and saving a YARA-L rule. - Get details of compilation or runtime errors for a given rule version.

Args: rule_id (str): Unique ID of the rule to list errors for. Examples: "ru_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" (latest version), "ru[_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx@v_12345_67890](mailto:_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx@v_12345_67890)" (specific version), "ru[_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx@-](mailto:_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx@-)" (all versions). project_id (str): Google Cloud project ID (required). customer_id (str): Chronicle customer ID (required). region (str): Chronicle region (e.g., "us", "europe") (required). page_size (Optional[int]): The maximum number of errors to return. Defaults to 1000. page_token (Optional[str]): A page token received from a previous call.

Returns: str: Raw JSON response from the API, containing a list of 'ruleExecutionErrors' and potentially a 'nextPageToken'. The agent must parse this response.

Example Usage: # List errors for the latest version of a rule list_rule_errors( rule_id="ru_12345678-1234-1234-1234-1234567890ab", project_id="my-project", customer_id="my-customer", region="us" )
    
    
    # List errors for a specific rule revision
            list_rule_errors(
                rule_id="ru_12345678-1234-1234-1234-1234567890ab@v_abcdef_123456",
                project_id="my-project",
                customer_id="my-customer",
                region="us",
                page_size=10
            )
    
            # List errors for all revisions of a rule
            list_rule_errors(
                rule_id="ru_12345678-1234-1234-1234-1234567890ab@-",
                project_id="my-project",
                customer_id="my-customer",
                region="us"
            )
            

Next Steps (using MCP-enabled tools): - **Review Rule Code:** If errors are found, retrieve the rule definition using `get_rule` with the specific rule_id and revision. - **Validate Rule Syntax:** Use `validate_rule` to check for syntax issues in the rule text. - **Modify Rule:** Correct the rule based on error messages and update it using `create_rule` (as there's no update function). - **Re-test:** Use `test_rule` to verify the fix.

The following sample demonstrate how to use `curl` to invoke the `list_rule_errors` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://chronicle.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_rule_errors",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for ListRuleExecutionErrors.

### ListRuleExecutionErrorsRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "customerId": string,
      "region": string,
      "ruleId": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`projectId` |  `string` Project ID of the customer.  
`customerId` |  `string` Customer ID of the customer.  
`region` |  `string` Region of the customer.  
`ruleId` |  `string` Rule ID of the rule execution errors to list.  
`pageSize` |  `integer` The maximum number of rule execution errors to return. The service may return fewer than this value. If unspecified, at most 1000 rule execution errors will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000.  
`pageToken` |  `string` A page token, received from a previous `ListRuleExecutionErrors` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListRuleExecutionErrors` must match the call that provided the page token.  
  
## Output Schema

Response message for ListRuleExecutionErrors.

### ListRuleExecutionErrorsResponse

JSON representation  
---  
      
    
    {
      "ruleExecutionErrors": [
        {
          object ([RuleExecutionError](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_rule_errors#Output.Schema.RuleExecutionError))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`ruleExecutionErrors[]` |  `object (`[RuleExecutionError](https://docs.cloud.google.com/chronicle/docs/reference/mcp/list_rule_errors#Output.Schema.RuleExecutionError)`)` List of rule execution errors.  
`nextPageToken` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### RuleExecutionError

JSON representation  
---  
      
    
    {
      "name": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/chronicle/docs/reference/mcp/run_parser#Output.Schema.Status))
      },
      "timeRange": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Interval))
      },
    
      // Union field source can be only one of the following:
      "rule": string,
      "curatedRule": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the rule execution error. Format: projects/{project}/locations/{location}/instances/{instance}/ruleExecutionErrors/{rule_execution_error}  
`error` |  `object (`[Status](https://docs.cloud.google.com/chronicle/docs/reference/mcp/run_parser#Output.Schema.Status)`)` Output only. The error status corresponding with the rule execution error.  
`timeRange` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/mcp/summarize_entity#Output.Schema.Interval)`)` Output only. The event time range that the rule execution error corresponds with.  
Union field `source`. The resource name of the source that generated the rule execution error. `source` can be only one of the following:  
`rule` |  `string` Output only. The resource name of the rule that generated the rule execution error.  
`curatedRule` |  `string` Output only. The resource name of the curated rule that generated the rule execution error.  
  
### Status

JSON representation  
---  
      
    
    {
      "code": integer,
      "message": string,
      "details": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Any

JSON representation  
---  
      
    
    {
      "typeUrl": string,
      "value": string
    }  
  
Fields  
---  
`typeUrl` |  `string` A URL/resource name that uniquely identifies the type of the serialized protocol buffer message. This string must contain at least one "/" character. The last segment of the URL's path must represent the fully qualified name of the type (as in `path/google.protobuf.Duration`). The name should be in a canonical form (e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that they expect it to use in the context of Any. However, for URLs which use the scheme `http`, `https`, or no scheme, one can optionally set up a type server that maps type URLs to message definitions as follows:

  * If no scheme is provided, `https` is assumed.
  * An HTTP GET on the URL must yield a `[google.protobuf.Type](https://protobuf.dev/reference/protobuf/google.protobuf/#type)` value in binary format, or produce an error.
  * Applications are allowed to cache lookup results based on the URL, or have them precompiled into a binary to avoid any lookup. Therefore, binary compatibility needs to be preserved on changes to types. (Use versioned type names to manage breaking changes.)

Note: this functionality is not currently available in the official protobuf release, and it is not used for type URLs beginning with type.googleapis.com. As of May 2023, there are no widely used type server implementations and no plans to implement one.Schemes other than `http`, `https` (or the empty scheme) might be used with implementation specific semantics.  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Must be a valid serialized protocol buffer of the above specified type.A base64-encoded string.  
  
### Interval

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Inclusive start of the interval.If specified, a Timestamp matching this interval will have to be the same or after the start.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Exclusive end of the interval.If specified, a Timestamp matching this interval will have to be before the end.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-15 UTC."],[],[]] 
