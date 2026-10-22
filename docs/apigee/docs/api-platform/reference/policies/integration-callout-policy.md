---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy/
title: IntegrationCallout policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:33.068831+00:00
---

# IntegrationCallout policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  IntegrationCallout policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

The IntegrationCallout policy lets you run an Application Integration that has an API trigger. However, before running an integration, you must run the [SetIntegrationRequest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-integration-request-policy). The SetIntegrationRequest policy creates a request object and makes the object available to the IntegrationCallout policy as a flow variable. The request object has the integration details such as the API trigger name, integration project ID, integration name, and other details configured in the SetIntegrationRequest policy. The IntegrationCallout policy uses the flow variable of the request object to run the integration. You can configure the IntegrationCallout policy to save the integration run response in a flow variable. 

The IntegrationCallout policy is helpful if you want to run integration in the middle of your proxy flow. Alternately, instead of configuring the IntegrationCallout policy, you can also run an integration by specifying an integration endpoint as your target endpoint. For more information, see [IntegrationEndpoint](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#integrationendpoint).

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

**Note** : You need an authentication token to run the IntegrationCallout policy. However, there is no explicit `Authentication` element in the policy definition. Apigee adds an authentication token to the request under the hood. For the IntegrationCallout policy to successfully authenticate, you must deploy your API proxy with a service account that has the required IAM roles to run an integration. For information about the required roles, see [IAM roles for integrations](https://docs.cloud.google.com/application-integration/docs/predefined-iam-roles-permissions). For more details on deploying an API proxy, see [Deploy on Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview#deploy-on-apigee-x). 

## `<IntegrationCallout>`

Specifies the IntegrationCallout policy.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex type  
**Parent Element** |  N/A   
**Child Elements** |  [`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#displayname)  
[`<AsyncExecution>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#asyncexecution)  
[`<Request>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#request)  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#response)  
  
  
The following table provides a high-level description of the child elements of [`<IntegrationCallout>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#integrationcallout): 

Child Element | Required? | Description  
---|---|---  
[`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#displayname) | Optional | A custom name for the policy.  
[`<AsyncExecution>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#asyncexecution) | Optional | Specifies if the integration must run in synchronous mode or asynchronous mode.  
[`<Request>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#request) | Required | The flow variable having the request object created by the SetIntegrationRequest policy.  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#response) | Optional | The flow variable to save the integration's response.  
  
The `<IntegrationCallout>` element uses the following syntax:

### Syntax
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <IntegrationCallout continueOnError="[true|false]" enabled="[true|false]" name=POLICY_NAME>
      <DisplayName>POLICY_DISPLAY_NAME</DisplayName>
      <AsyncExecution>BOOLEAN_ASYNC_EXECUTION</AsyncExecution>
      <Request clearPayload="[true|false]">REQUEST_FLOW_VARIABLE_NAME</Request>
      <Response>RESPONSE_FLOW_VARIABLE_NAME</Response>
    </IntegrationCallout>

### Example

The following example shows the IntegrationCallout policy definition:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <IntegrationCallout continueOnError="false" enabled="true" name="Integration-Callout">
      <DisplayName>Integration-Callout-1</DisplayName>
      <AsyncExecution>true</AsyncExecution>
      <Request clearPayload="true">my_request_flow_var</Request>
      <Response>my_response_flow_var</Response>
    </IntegrationCallout>

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

This section describes the child elements of [`<IntegrationCallout>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#integrationcallout). 

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

### `<AsyncExecution>`

Specifies the mode to run the integration. You can run the integration either synchronously or asynchronously.

If set to `true`, the integration runs asynchronously. And if set to `false`, the integration runs synchronously.

  * **Asynchronous mode** : When the request to run the integration reaches the endpoint, the endpoint immediately returns the integration execution IDs, but starts the execution of integration at the time specified by the `<ScheduleTime>` element. If you have not set the `<ScheduleTime>` element, the integration is scheduled to run immediately. Even though the integration is scheduled to run immediately, its execution may start after a few seconds. When the integration starts to execute, the following two things happen: 
    * The integration returns the HTTP `200 OK` status code so that the caller can continue processing.
    * The IntegrationCallout policy completes.
Once started, the integration will have a maximum time limit of 50 minutes to complete the execution.
  * **Synchronous mode** : When the request to run the integration reaches the endpoint, the endpoint immediately starts the execution of the integration and waits for the response. The maximum time limit to complete the execution is 2 minutes. After finishing the execution, the endpoint returns a response with the execution IDs and other response data.

**Default Value** | false  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<IntegrationCallout>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#integrationcallout)  
  
**Child Elements** |  None   
  
The `<AsyncExecution>` element uses the following syntax:

#### Syntax
    
    
    <AsyncExecution>BOOLEAN</AsyncExecution>

#### Example

The following example sets asynchronous execution to `true`:
    
    
    <AsyncExecution>true</AsyncExecution>

### `<Request>`

Specifies the flow variable having the request object created by the SetIntegrationRequest policy. The IntegrationCallout policy sends this request object to Application Integration for running the integration.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | String  
**Parent Element** |  [`<IntegrationCallout>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#integrationcallout)  
  
**Child Elements** |  None   
  
The `<Request>` element uses the following syntax:

#### Syntax
    
    
    <Request clearPayload="true">FLOW_VARIABLE_NAME</Request>

#### Example

The following example specifies that the request object is available in the `my_request_flow_var` flow variable:
    
    
    <Request clearPayload="true">my_request_flow_var</Request>

The following table describes the attributes of `<Request>`:

Attribute | Required? | Type | Description  
---|---|---|---  
`clearPayload` | Optional | boolean | Specifies if the request object should be cleared from the memory after sending the request to run the integration.

  * If set to `true`, Apigee clears the request object.
  * If set to `false`, Apigee doesn't clear the request object.

If you don't specify this attribute, the default value is `true` and the request object is cleared from the memory.  
  
### `<Response>`

Specifies the flow variable for saving the integration's response.

If you don't specify this element, the policy saves the response in the `integration.response` flow variable.

**Default Value** | integration.response  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<IntegrationCallout>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy#integrationcallout)  
  
**Child Elements** |  None   
  
The output of the integration can be accessed by `integration.response.content` or `flow_variable.content`. The `<Response>` element uses the following syntax:

#### Syntax
    
    
    <Response>FLOW_VARIABLE_NAME</Response>

#### Example

The following example saves the response of the integration run in the `my_response_flow_var` flow variable:
    
    
    <Response>my_response_flow_var</Response>

## Error codes

This section describes the fault codes, error messages, and the fault variables set by Apigee when this policy triggers an error. This information is essential if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause  
---|---|---  
`entities.UnresolvedVariable` | `500` | This error occurs if Apigee cannot resolve the `integration.project.id` or the `integration.name` variables.  
`steps.integrationcallout.ExecutionFailed` | `500` | This error can occur if the backend target service returns an HTTP error status such as `4xx` or `5xx`. The possible causes include:

  * The service account deployed with the proxy has the incorrect permissions to run the integration.
  * The integration or the API trigger does not exist.
  * Application Integration is not enabled for your Google Cloud project.
  * You have configured the `<ScheduleTime>` element in your SetIntegrationRequest policy and the IntegrationCallout policy has the `AsyncExecution` set to `false`.

  
`steps.integrationcallout.NullRequestVariable` | `500` | This error occurs if the flow variable specified in the `<Request>` is null.  
`steps.integrationcallout.RequestVariableNotMessageType` | `500` | This error occurs when the flow variable specified by the `Request` element is not of [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) type.  
`steps.integrationcallout.RequestVariableNotRequestMessageType` | `500` | This error occurs when the flow variable specified by the `Request` element is not of [Request message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) type.  
`messaging.adaptors.http.filter.GoogleTokenGenerationFailure` | `500` | This error can occur because of an incorrect service account configuration. The possible causes include:

  * The service account deployed with the proxy does not exist in your project.
  * The service account deployed with the proxy is disabled.

  
  
### Fault variables

Whenever there are execution errors in a policy, Apigee generates error messages. You can view these error messages in the error response. Many a time, system generated error messages might not be relevant in the context of your product. You might want to customize the error messages based on the type of error to make the messages more meaningful. 

To customize the error messages, you can use either fault rules or the RaiseFault policy. For information about differences between fault rules and the RaiseFault policy, see [FaultRules vs. the RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#rulesvraisefault). You must check for conditions using the `Condition` element in both the fault rules and the RaiseFault policy. Apigee provides fault variables unique to each policy and the values of the fault variables are set when a policy triggers runtime errors. By using these variables, you can check for specific error conditions and take appropriate actions. For more information about checking error conditions, see [Building conditions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#buildingconditions).

The following table describes the fault variables specific to this policy.

Variables | Where | Example  
---|---|---  
`fault.name` | The `fault.name` can match to any of the faults listed in the Runtime errors table. The fault name is the last part of the fault code. | `fault.name Matches "UnresolvedVariable"`  
`IntegrationCallout.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `IntegrationCallout.integration-callout-1.failed = true`  
For more information about policy errors, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors). 

## Related topics

If you want to learn more about Application Integration feature, see [Application Integration overview](https://docs.cloud.google.com/application-integration/docs/overview)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
