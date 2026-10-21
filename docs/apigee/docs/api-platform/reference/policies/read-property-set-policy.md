---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy/
title: ReadPropertySet policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:09:34.871371+00:00
---

# ReadPropertySet policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  ReadPropertySet policy Stay organized with collections  Save and categorize content based on your preferences. 

[Standard policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

The ReadPropertySet policy reads property sets and populates flow variable with the results.

This policy is a _Standard policy_ and can be deployed to any environment type. For information on policy types and availability with each environment type, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## `<ReadPropertySet>` element

Defines a ReadPropertySet policy.

**Default Value** | See **Default Policy** tab, below  
---|---  
**Required?** | Required  
**Type** | Complex object  
**Parent Element** |  N/A   
**Child Elements** |  [`<Read>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#read)  
  
  
The `<ReadPropertySet>` element uses the following syntax:

### Syntax

The `<ReadPropertySet>` element uses the following syntax:
    
    
    <ReadPropertySet name="read-property-set">
      <Read>
        <Name ref="set-ref">property-set-name</Name>
        <Key ref="key-ref">key-name</Key>
        <AssignTo>var1</AssignTo>
        <DefaultValue>default-value</DefaultValue>
      </Read>
      ...
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </ReadPropertySet>

### Default Policy

The following example shows the default settings when you add a ReadPropertySet policy to your flow in the Apigee UI:
    
    
    <ReadPropertySet name="read-property-set">
      <Read>
        <Name ref="set-ref">property-set-name</Name>
        <Key ref="key-ref">key-name</Key>
        <AssignTo>var1</AssignTo>
        <DefaultValue>default-value</DefaultValue>
      </Read>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </ReadPropertySet>

When you insert a new ReadPropertySet policy in the Apigee UI, the template contains stubs for all possible operations. See below for information on required elements.

This element has the following attributes that are common to all policies:

**Attribute** | **Default** | **Required?** | **Description**  
---|---|---|---  
`name` | N/A | **Required** |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name.  
`continueOnError` | false | Optional | Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also: 

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

  
`enabled` | true | Optional | Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow.  
`async` not_interested | false | Deprecated | This attribute is deprecated.  
  
The following table provides a high level description of the child elements of [`<ReadPropertySet>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#readpropertyset):

Child Element | Required? | Description  
---|---|---  
[`<Read>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#read) | Required | Reads and resolves a property set variable and sets it to a specified flow variable.   
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#ignoreunresolvedvariables) | Optional | Determines whether processing stops when a property set is unresolved.  
  
## Example

This section provides an example using [`<ReadPropertySet>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#readpropertyset).

### Example

This example uses [`<ReadPropertySet>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#readpropertyset) to get `propertyset.environment.name.request.headers.api-version` and assign it to `target_url`. If the property set value isn't obtained, `https://httpbin.org/get` is used instead.
    
    
    <ReadPropertySet name="read-property-set">
      <Read>
        <Name ref="set-ref">environment.name</Name>
        <Key ref="key-ref">request.headers.api-version</Key>
        <AssignTo>target_url</AssignTo>
        <DefaultValue>https://httpbin.org/get</DefaultValue>
      </Read>
      <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
    </ReadPropertySet>

## Child element reference

This section describes the child elements of [`<ReadPropertySet>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#readpropertyset).

### `<Read>`

Resolves a property set variable and sets the result in a flow variable.

The `<Read>` element specifes the property set variable to resolve and the flow variable to set that value to. It also includes an optional default value, which is used in the event of an unresolved property set. You can include multiple `<Read>` elements in a single [`<ReadPropertySet>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#readpropertyset) policy.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex type  
**Parent Element** |  [`<ReadPropertySet>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#readpropertyset)  
**Child Elements** |  [`<Name>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#nameelement)  
[`<Key>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#keyelement)  
[`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#assigntoelement)  
[`<DefaultValue>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#defaultvalueelement)  
  
  
The `<Read>` element uses the following syntax:

### Syntax
    
    
    <Read>
      <Name ref="set-ref">property-set-name</Name>
      <Key ref="key-ref">key-name</Key>
      <AssignTo>var1</AssignTo>
      <DefaultValue>default-value</DefaultValue>
    </Read>

### Example

This example uses [`<ReadPropertySet>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#readpropertyset) to get `propertyset.environment.name.request.headers.api-version` and assign it to `target_url`. If the property set value isn't obtained, `https://httpbin.org/get` is used instead.
    
    
    <ReadPropertySet name="read-property-set">
      <Read>
        <Name ref="environment.name">my-property-set-name</Name>
        <Key ref="request.headers.api-version">my-property-set-key</Key>
        <AssignTo>target_url</AssignTo>
        <DefaultValue>https://httpbin.org/get</DefaultValue>
      </Read>
      <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
    </ReadPropertySet>

The following table provides a high-level description of the child elements of [`<Read>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#read).

Child Element | Required? | Description  
---|---|---  
`<Name>` | Required | String  
  
The property set to read from. Provide the `ref`, value, or both. Apigee first tries to resolve the `Name` based on the `ref`, then the value. If neither is resolvable, the [`<DefaultValue>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#defaultvalueelement), if provided, applies.  `<Name>` and `<Key>` combine to `propertyset.{value_resolved_from_Name}.{value_resolved_from_Key}`.   
`<Key>` | Required | String  
  
The key of the property set that is used when resolving the variable. Provide the `ref`, value, or both. Apigee first tries to resolve the `Key` based on the `ref`, then the value. If neither is resolvable, the [`<DefaultValue>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#defaultvalueelement), if provided, applies.  `<Name>` and `<Key>` combine to `propertyset.{value_resolved_from_Name}.{value_resolved_from_Key}`.   
`<AssignTo>` | Required | String  
  
Specifies the flow variable to assign the resolved variable to.  
`<DefaultValue>` | Optional | String  
  
Specifies a default value to use when the variable cannot be resolved.  
  
### <IgnoreUnresolvedVariables>

Determines whether processing stops when a property set is unresolved. Set to `true` to ignore unresolved variables and continue processing.

`IgnoreUnresolvedVariables` is not applicable when [`<DefaultValue>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#defaultvalueelement) is provided.

**Default Value** | False  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<ReadPropertySet>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#readpropertyset)  
**Child Elements** |  None   
  
## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee specific to the `<ReadPropertySet>` policy. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause  
---|---|---  
`steps.readpropertyset.UnresolvedVariable` | `500` |  This error occurs if a variable specified in the ReadPropertySet policy is either:

  * Out of scope (not available in the specific flow where the policy is being executed)
or 
  * Can't be resolved (is not defined).

If [`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#ignoreunresolvedvariables) is false and [`<DefaultValue>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#defaultvalueelement) is not specified, the resolution fails.  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

Error name | Cause  
---|---  
`steps.readpropertyset.EmptyReads` | The policy has no [`<Read>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#read) child elements.  
`steps.readpropertyset.FieldUnset` | This code is returned when any of these are true:  


  * Neither a reference nor name is set for [`<Name>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#nameelement)
  * Neither a reference nor name is set for [`<Key>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#keyelement)
  * No value was provided for [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy#assigntoelement)

  
  
### Fault variables

These variables are set when this policy triggers an error at runtime. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="FAULT_NAME"` | FAULT_NAME is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name Matches "UnresolvedVariable"`  
`readpropertyset.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `readpropertyset.RPS-SetResponse.failed = true`  
  
### Example error response

**Note:** For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.
    
    
      {
        "fault": {
          "faultstring": "ReadPropertySet[RPS-SetResponse]: unable to resolve variable [variable_name]",
          "detail": {
            "errorcode": "steps.readpropertyset.UnresolvedVariable"
          }
        }
      }
      

### Example fault rule
    
    
      <FaultRule name="ReadPropertySet Faults">
          <Step>
              <Name>RPS-CustomSetVariableErrorResponse</Name>
              <Condition>(fault.name = "SetVariableFailed")</Condition>
          </Step>
          <Condition>(readpropertyset.failed = true)</Condition>
      </FaultRule>
      

## Schemas

Each policy type is defined by an XML schema (`.xsd`). For reference, [policy schemas](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) are available on GitHub.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
