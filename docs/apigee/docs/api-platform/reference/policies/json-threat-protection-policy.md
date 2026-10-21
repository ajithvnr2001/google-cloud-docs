---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-threat-protection-policy/
title: JSONThreatProtection policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:34:57.446834+00:00
---

# JSONThreatProtection policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-threat-protection-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  JSONThreatProtection policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

APIs that accept JSON payloads are vulnerable to malicious attacks designed to overwhelm the JSON parser. These attacks might include payloads with excessive array elements, deeply nested structures, or incredibly long strings, which can crash the service or consume excessive memory.

The JSONThreatProtection policy minimizes this risk by screening incoming requests for payloads that violate the defined limits on structures like arrays and strings, effectively protecting your backend services from these denial-of-service or parser attacks.

**Note:** This policy executes only if the `Content-Type` of the request or response header is set to `application/json.`

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## Element reference

The element reference describes the elements and attributes of the JSONThreatProtection policy.
    
    
    <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
       <DisplayName>JSONThreatProtection 1</DisplayName>
       <ArrayElementCount>20</ArrayElementCount>
       <ContainerDepth>10</ContainerDepth>
       <ObjectEntryCount>15</ObjectEntryCount>
       <ObjectEntryNameLength>50</ObjectEntryNameLength>
       <Source>request</Source>
       <StringValueLength>500</StringValueLength>
    </JSONThreatProtection>

## <JSONThreatProtection> attributes
    
    
    <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">

The following table describes attributes that are common to all policy parent elements:

Attribute | Description | Default | Presence  
---|---|---|---  
`name` |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name. | N/A | Required  
`continueOnError` |  Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also:

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

| false | Optional  
`enabled` |  Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow. | true | Optional  
`async` |  This attribute is deprecated. | false | Deprecated  
  
## <DisplayName> element

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, natural-language name.
    
    
    <DisplayName>Policy Display Name</DisplayName>

Default |  N/A If you omit this element, the value of the policy's `name` attribute is used.  
---|---  
Presence | Optional  
Type | String  
  
## <ArrayElementCount> element

Specifies the maximum number of elements allowed in an array.
    
    
    <ArrayElementCount>20</ArrayElementCount>

**Default:** | If you do not specify this element, or if you specify a negative integer, the system does not enforce a limit.  
---|---  
**Presence:** | Optional  
**Type:** | Integer  
  
## <ContainerDepth> element

Specifies the maximum allowed containment depth, where the containers are objects or arrays. For example, an array containing an object which contains an object would result in a containment depth of 3.
    
    
    <ContainerDepth>10</ContainerDepth>

**Default:** | If you do not specify this element, or if you specify a negative integer, the system does not enforce any limit.  
---|---  
**Presence:** | Optional  
**Type:** | Integer  
  
## <ObjectEntryCount> element

Specifies the maximum number of entries allowed in an object.
    
    
    <ObjectEntryCount>15</ObjectEntryCount>

**Default:** | If you do not specify this element, or if you specify a negative integer, the system does not enforce any limit.  
---|---  
**Presence:** | Optional  
**Type:** | Integer  
  
## <ObjectEntryNameLength> element

Specifies the maximum string length allowed for a property name within an object.
    
    
    <ObjectEntryNameLength>50</ObjectEntryNameLength>

**Default:** | If you do not specify this element, or if you specify a negative integer, the system does not enforce a limit.  
---|---  
**Presence:** | Optional  
**Type:** | Integer  
  
## <Source> element

Message to be screened for JSON payload attacks. This is most commonly set to `request`, as you will typically need to validate inbound requests from client apps. When set to `message`, this element will automatically evaluate the request message when attached to the request flow and the response message when attached to the response flow.
    
    
    <Source>request</Source>

**Default:** | request  
---|---  
**Presence:** | Optional  
**Type:** |  String. Valid values: request, response, or message.  
  
## <StringValueLength> element

Specifies the maximum length allowed for a string value.
    
    
    <StringValueLength>500</StringValueLength>

**Default:** | If you do not specify this element, or if you specify a negative integer, the system does not enforce a limit.  
---|---  
**Presence:** | Optional  
**Type:** | Integer  
  
## Error reference

**Note:** This policy executes only if the `Content-Type` of the request or response header is set to `application/json.`

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [ What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [ Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause | Fix  
---|---|---|---  
`steps.jsonthreatprotection.ExecutionFailed` | `500` |  The `JSONThreatProtection` policy can throw many different types of `ExecutionFailed` errors. Most of these errors occur when a specific threshold set in the policy is exceeded. These types of errors include: [object entry name length](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors#exceeded_object_entry_name_length), [object entry count](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors#exceeded_object_entry_count), [array element count](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors#exceeded_array_element_count), [container depth](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors#exceeded_container_depth), [string string value length](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors#exceeded_string_value_length). This error also occurs when the payload contains an [invalid JSON object](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors#not_valid_json_object).  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors#executionfailed)  
`steps.jsonthreatprotection.SourceUnavailable` | `500` |  This error occurs if the [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) variable specified in the `<Source>` element is either: 

  * Out of scope (not available in the specific flow where the policy is being executed)
  * Is not one of the valid values `_request_`, `_response_`, or `_message_`

| [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors#sourceunavailable)  
`steps.jsonthreatprotection.NonMessageVariable` | `500` |  This error occurs if the `<Source>` element is set to a variable which is not of type [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message).  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors#nonmessagevariable)  
  
### Deployment errors

None.

### Fault variables

These variables are set when this policy triggers an error. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name Matches "SourceUnavailable"`  
`jsonattack.policy_name.failed` | policy_name is the user-specified name of the policy that threw the fault. | `jsonattack.JTP-SecureRequest.failed = true`  
  
### Example error response
    
    
    {
      "fault": {
        "faultstring": "JSONThreatProtection[JPT-SecureRequest]: Execution failed. reason: JSONThreatProtection[JTP-SecureRequest]: Exceeded object entry name length at line 2",
        "detail": {
          "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
        }
      }
    }

### Example fault rule
    
    
    <FaultRule name="JSONThreatProtection Policy Faults">
        <Step>
            <Name>AM-CustomErrorResponse</Name>
            <Condition>(fault.name Matches "ExecutionFailed") </Condition>
        </Step>
        <Condition>(jsonattack.JPT-SecureRequest.failed = true) </Condition>
    </FaultRule>
    

## Schemas

**Sample:** See our [GitHub repository](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) samples for the most recent schemas.

## Usage notes

Like XML-based services, APIs that support JavaScript object notation (JSON) are vulnerable to content-level attacks. Simple JSON attacks attempt to use structures that overwhelm JSON parsers to crash a service and induce application-level denial-of-service attacks. All settings are optional and should be tuned to optimize your service requirements against potential vulnerabilities.

## Related topics

[JSONtoXML policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-xml-policy)

[ XMLThreatProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-threat-protection-policy)

[ RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
