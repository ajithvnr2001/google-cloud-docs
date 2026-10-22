---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy/
title: TraceCapture policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:44.779261+00:00
---

# TraceCapture policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  TraceCapture policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The TraceCapture policy lets you add additional variables to your Apigee runtime's trace data. If you have enabled distributed tracing for the Apigee runtime, the runtime, by default, traces a set of pre-defined variables. For more information, see [Default trace variables in tracing report](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-distributed-trace#default-trace-var). However, if you want the Apigee runtime to trace additional flow, policy, or custom variables, use the TraceCapture policy. You can use this policy either in the request or the response flow. In your distributed tracing report, you can view the variables added by TraceCapture policy in the `TraceCaptureExecution` span. 

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## `<TraceCapture>`

Defines the TraceCapture policy.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex type  
**Parent Element** |  N/A   
**Child Elements** |  [`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#displayname)  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#ignoreunresolvedvariables)  
[`<ThrowExceptionOnLimit>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#throwexceptiononlimit)  
[`<Variables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#variables)  
  
  
The `<TraceCapture>` element uses the following syntax:

### Syntax
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <TraceCapture continueOnError="true" enabled="true" name="DistributedTraceCapture-1">
        <DisplayName>POLICY_DISPLAY_NAME</DisplayName>
        <Variables>
            <Variable name="TRACE_VARIABLE_NAME" ref="FLOW_VARIABLE_NAME">DEFAULT_VALUE</Variable>
            <Variable name="TRACE_VARIABLE_NAME" ref="FLOW_VARIABLE_NAME">DEFAULT_VALUE</Variable>
        </Variables>
        <IgnoreUnresolvedVariables>BOOLEAN_VALUE</IgnoreUnresolvedVariables>
        <ThrowExceptionOnLimit>BOOLEAN_VALUE</ThrowExceptionOnLimit>
    </TraceCapture>

### Example

The following example shows the TraceCapture policy definition:
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <TraceCapture continueOnError="true" enabled="true" name="DistributedTraceCapture-1">
        <DisplayName>Distributed-Trace-Capture-Policy-1</DisplayName>
        <Variables>
            <Variable name="trace-variable-1" ref="flow-variable-1">default-val-1</Variable>
            <Variable name="trace-variable-2" ref="flow-variable-2">default-val-2</Variable>
        </Variables>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
        <ThrowExceptionOnLimit>false</ThrowExceptionOnLimit>
    </TraceCapture>

This element has the following attributes that are common to all policies:

**Attribute** | **Default** | **Required?** | **Description**  
---|---|---|---  
`name` | N/A | **Required** |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name.  
`continueOnError` | false | Optional | Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also: 

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

  
`enabled` | true | Optional | Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow.  
`async` not_interested | false | Deprecated | This attribute is deprecated.  
  
The following table provides a high-level description of the child elements of [`<TraceCapture>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#tracecapture): 

Child Element | Required? | Description  
---|---|---  
[`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#displayname) | Optional | Specifies a custom name for the policy.  
[`<Variables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#variables) | Optional | Specifies the list of variables to trace.  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#ignoreunresolvedvariables) | Optional | Specifies whether processing stops when an unresolved variable is encountered.  
[`<ThrowExceptionOnLimit>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#throwexceptiononlimit) | Optional | Specifies whether a variable must be truncated if the size of the variable exceeds the limit of 256 bytes.  
Other child elements  
[`<MergeBehavior>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#mergebehavior) | Optional | Specifies the merge behavior for the response messages.  
  
## Child element reference

This section describes the child elements of [`<TraceCapture>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#tracecapture). 

### `<DisplayName>`

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, more natural-sounding name.

The `<DisplayName>` element is common to all policies.

**Default Value** | N/A  
---|---  
**Required?** | Optional. If you omit `<DisplayName>`, the value of the policy's `name` attribute is used.  
**Type** | String  
**Parent Element** |  <PolicyElement>  
**Child Elements** |  None   
  
The `<DisplayName>` element uses the following syntax:

### Syntax
    
    
    <_PolicyElement_ >
      **< DisplayName>POLICY_DISPLAY_NAME</DisplayName>**
      ...
    </_PolicyElement_ >

### Example
    
    
    <_PolicyElement_ >
      **< DisplayName>My Validation Policy</DisplayName>**
    </_PolicyElement_ >

The `<DisplayName>` element has no attributes or child elements.

### `<Variables>`

Specifies the list of variables to trace.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex type  
**Parent Element** |  [`<TraceCapture>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#tracecapture)  
  
**Child Elements** |  [`<Variable>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#variable)  
  
  
The `<Variables>` element uses the following syntax:

#### Syntax
    
    
    <Variables>
        <Variable name="TRACE_VARIABLE_NAME" ref="FLOW_VARIABLE_NAME">DEFAULT_VALUE</Variable>
        <Variable name="TRACE_VARIABLE_NAME" ref="FLOW_VARIABLE_NAME">DEFAULT_VALUE</Variable>
    </Variables>

#### Example

The following example traces the `flow-variable-1` and `flow-variable-2` flow variables:
    
    
    <Variables>
        <Variable name="trace-variable-1" ref="flow-variable-1">default-val-1</Variable>
        <Variable name="trace-variable-2" ref="flow-variable-2">default-val-2</Variable>
    </Variables>

**Note** : 

  * You cannot trace `private` and `policy.secret` variables.
  * Apigee recommends you to configure a maximum of `15` variables for Cloud Trace and a maximum of `25` variables for Jaeger.



#### `<Variable>`

Specifies the variables to be added in the trace data.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex type  
**Parent Element** |  [`<Variables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#variables)  
  
**Child Elements** |  None   
  
The `<Variable>` element uses the following syntax:

##### Syntax
    
    
    <Variable name="TRACE_VARIABLE_NAME" ref="FLOW_VARIABLE_NAME">DEFAULT_VALUE</Variable>

##### Example

The following example sets the `trace-variable-1` trace variable to the value of the `flow-variable-1` flow variable:
    
    
    <Variable name="trace-variable-1" ref="flow-variable-1">default-val-1</Variable>

If the `flow-variable-1` flow variable is not available, `trace-variable-1` is set to the default value `default-val-1`.

The following table describes the attributes of `<Variable>`:

Attribute | Required? | Type | Description  
---|---|---|---  
`name` | Required | String | A name for referencing the data collected for the specified variable. This name will be visible in your distributed tracing report.   
`ref` | Required | String | The variable for which you are collecting the trace data. This variable can be a flow variable predefined by Apigee or a custom variable in your API proxy.  
**Note** : You can specify an optional default value for a variable. If the variable specified in `ref` is undefined in a request or a response, the trace data will have the default value for the variable. 

### `<IgnoreUnresolvedVariables>`

Determines whether processing stops when an unresolved variable is encountered.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<TraceCapture>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#tracecapture)  
  
**Child Elements** |  None   
  
Set to `true` to ignore unresolved variables and continue processing; otherwise `false`. The default value is `true`.

Setting `<IgnoreUnresolvedVariables>` to `true` is different from setting the [`<TraceCapture>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#tracecapture)'s `continueOnError` to `true`. If you set `continueOnError` to `true`, Apigee ignores all errors, not only errors in variables.

The `<IgnoreUnresolvedVariables>` element uses the following syntax:

### Syntax
    
    
    <IgnoreUnresolvedVariables>BOOLEAN_VALUE</IgnoreUnresolvedVariables>

### Example

The following example sets `<IgnoreUnresolvedVariables>` to `false`:
    
    
    <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>

**Note** : The default value of the element is `false`. 

### `<ThrowExceptionOnLimit>`

Specifies the behavior of the policy when the size of the variable exceeds the limit of 256 bytes.

  * If set to `true`, the policy throws an error if a variable size exceeds the limit.
  * If set to `false`, the policy truncates the variable that exceeds the limit. The variable is truncated to the size of the limit.

**Note** : The default value of the element is `false`. **Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<TraceCapture>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy#tracecapture)  
  
**Child Elements** |  None   
  
The `<ThrowExceptionOnLimit>` element uses the following syntax:

#### Syntax
    
    
    <ThrowExceptionOnLimit>BOOLEAN_VALUE</ThrowExceptionOnLimit>

#### Example

The following example sets the ``<ThrowExceptionOnLimit>`` value to `true`.
    
    
    <ThrowExceptionOnLimit>false</ThrowExceptionOnLimit>

## Error codes

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause  
---|---|---  
`steps.tracecapture.UnresolvedVariable` | `500` |  This error occurs if a variable specified in the TraceCapture policy is either:

  * Out of scope (not available in the specific flow where the policy is being executed)
or 
  * Can't be resolved (is not defined)

  
`steps.tracecapture.VariableValueLimitExceeded` | `500` |  This error occurs if the ``<ThrowExceptionOnLimit>`` element is set to `true` and the size of any variable exceeds 256 bytes.  
  
### Fault variables

Whenever there are execution errors in a policy, Apigee generates error messages. You can view these error messages in the error response. Many a time, system generated error messages might not be relevant in the context of your product. You might want to customize the error messages based on the type of error to make the messages more meaningful. 

To customize the error messages, you can use either fault rules or the RaiseFault policy. For information about differences between fault rules and the RaiseFault policy, see [FaultRules vs. the RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#rulesvraisefault). You must check for conditions using the `Condition` element in both the fault rules and the RaiseFault policy. Apigee provides fault variables unique to each policy and the values of the fault variables are set when a policy triggers runtime errors. By using these variables, you can check for specific error conditions and take appropriate actions. For more information about checking error conditions, see [Building conditions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#buildingconditions).

The following table describes the fault variables specific to this policy.

Variables | Where | Example  
---|---|---  
`fault.name` | The `fault.name` can match to any of the faults listed in the Runtime errors table. The fault name is the last part of the fault code. | `fault.name Matches "UnresolvedVariable"`  
`tracecapture.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `tracecapture.trace-capture-1.failed = true`  
For more information about policy errors, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
