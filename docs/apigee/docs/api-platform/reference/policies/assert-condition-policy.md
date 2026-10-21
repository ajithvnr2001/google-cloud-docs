---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy/
title: AssertCondition policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:51.849305+00:00
---

# AssertCondition policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  AssertCondition policy Stay organized with collections  Save and categorize content based on your preferences. 

[Standard policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The AssertCondition policy evaluates a conditional statement at runtime in the request or response flows. You can define a condition based on the flow variables, and use this policy to assert the condition. A condition always evaluates to a boolean value, either true or false. For more information about writing a conditional statement, see [Conditions reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference). 

After evaluating the condition, the AssertCondition policy stores the result of the evaluation in the `assertcondition.policy-name.truthValue` flow variable. You can use the resultant flow variable in your subsequent callouts or orchestrated logic. If a condition evaluates to true, the value of the variable is set to `true`, `false` otherwise. If you have defined multiple AssertCondition policies, the `policy-name` in the variable name helps you to uniquely identify the variable. 

This policy is a _Standard policy_ and can be deployed to any environment type. For information on policy types and availability with each environment type, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## `<AssertCondition>`

Defines an `<AssertCondition>` policy. By using this policy, you can evaluate a conditional statement that has one or more conditions joined by a logical operator. For information about all the supported operators in a condition, see [Operators](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference#operators).

The result of a conditional statement is a boolean which can be either a `true` or a `false`. **Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex type  
**Parent Element** |  N/A   
**Child Elements** |  [`<Condition>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy#condition)  
[`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy#displayname)  
  
  
The following table provides a high-level description of the child elements of [`<AssertCondition>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy#assertcondition): 

Child Element | Required? | Description  
---|---|---  
[`<Condition>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy#condition) | Yes | Specifies the condition to evaluate.  
[`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy#displayname) | Optional | A custom name for the policy.  
  
The `<AssertCondition>` element uses the following syntax:

### Syntax
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AssertCondition">
        <!-- Display name for this policy -->
        <DisplayName>DISPLAY_NAME</DisplayName>
        <!-- Assertion's condition where operators are defined -->
        <Condition>CONDITIONAL_STATEMENT</Condition>
    </AssertCondition>

### Example

The following example checks if the `google.dialogflow.my-prefix.claimAmount` variable is greater than 0 and less than 1000.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AssertCondition continueOnError="false" enabled="true"
            name="MyAssertCondition">
        <DisplayName>Assert My Condition</DisplayName>
        <Condition>(google.dialogflow.my-prefix.claimAmount > 0)
                    and
                   (google.dialogflow.my-prefix.claimAmount LesserThan 1000)</Condition>
    </AssertCondition>

In this example:

  * If the value of `google.dialogflow.my-prefix.claimAmount` variable is 500, the condition evaluates to true and hence the `assertcondition.MyAssertCondition.truthValue` variable is set to `true`.
  * However, if the value of the `google.dialogflow.my-prefix.claimAmount` variable is 1200, the `assertcondition.MyAssertCondition.truthValue` variable is set to `false`.



This element has the following attributes that are common to all policies:

**Attribute** | **Default** | **Required?** | **Description**  
---|---|---|---  
`name` | N/A | **Required** |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name.  
`continueOnError` | false | Optional | Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also: 

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

  
`enabled` | true | Optional | Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow.  
`async` not_interested | false | Deprecated | This attribute is deprecated.  
  
## Child element reference

This section describes the child elements of [`<AssertCondition>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy#assertcondition). 

### `<Condition>`

Specifies the condition to evaluate. For more information about writing a conditional statement in Apigee, see [Conditions reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference).

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | String  
**Parent Element** |  [`<AssertCondition>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy#assertcondition)  
**Child Elements** |  None   
  
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

## Error codes

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause  
---|---|---  
`steps.assertcondition.ConditionEvaluationFailed` | `500` | Failed to evaluate the conditional statement. There can be many reasons for this error, including incorrect values in the variables at run time.   
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

Error name | Cause  
---|---  
`InvalidCondition` | The policy was not able to validate the conditional statement. There can be many reasons for this error, including malformed conditions or use of unsupported operators.  
  
### Fault variables

Whenever there are execution errors in a policy, Apigee generates error messages. You can view these error messages in the error response. Many a time, system generated error messages might not be relevant in the context of your product. You might want to customize the error messages based on the type of error to make the messages more meaningful. 

To customize the error messages, you can use either fault rules or the RaiseFault policy. For information about differences between fault rules and the RaiseFault policy, see [FaultRules vs. the RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#rulesvraisefault). You must check for conditions using the `Condition` element in both the fault rules and the RaiseFault policy. Apigee provides fault variables unique to each policy and the values of the fault variables are set when a policy triggers runtime errors. By using these variables, you can check for specific error conditions and take appropriate actions. For more information about checking error conditions, see [Building conditions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#buildingconditions).

The following table describes the fault variables specific to this policy.

Variables | Where | Example  
---|---|---  
`fault.name="FAULT_NAME"` | FAULT_NAME is the name of the fault, as listed in the Runtime errors table. The fault name is the last part of the fault code. | `fault.name Matches "ConditionEvaluationFailed"`  
`AssertCondition.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `AssertCondition.My-AssertCondition.failed = true`  
For more information about policy errors, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
