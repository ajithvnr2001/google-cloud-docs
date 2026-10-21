---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy/
title: ParseDialogflowRequest policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:31:11.138070+00:00
---

# ParseDialogflowRequest policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  ParseDialogflowRequest policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The ParseDialogflowRequest policy facilitates the integration of Dialogflow with Apigee. For more information, see [Integrating Apigee with Contact Center AI](https://docs.cloud.google.com/apigee/docs/api-platform/develop/integrating-apigee-contact-center-ai). 

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

The ParseDialogflowRequest policy processes the [WebhookRequest](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#webhook-request) from a [Dialogflow](https://docs.cloud.google.com/dialogflow/cx/docs) agent before sending the request data to your backend systems. The policy extracts data from the WebhookRequest into the flow variables which are available to you for the duration of the entire API call. You can use the variables in your subsequent callouts, lookups, or orchestrated logic. This policy is particularly useful if you want the Dialogflow agent to interact with your legacy backend systems. Before sending the agent's data to the backend systems, you can parse the data and structure it in a way that your backend systems can consume. 

If you are a backend service integrator, you need not spend time understanding the format of the Dialogflow WebhookRequest. The out-of-the-box ParseDialogflowRequest policy handles the processing of the request data seamlessly.

To access your Dialogflow agent's WebhookRequest in Apigee, you have to set the Webhook URL (fulfillment) of the agent to the ProxyEndPoint that you have configured in Apigee. The ProxyEndPoint should be publicly accessible. For more information, see [Webhook service requirements](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#requirements). 

**NOTE** : The ParseDialogflowRequest policy parses only the `fulfillmentInfo.tag`, `sentimentAnalysisResult`, and the `sessionInfo` objects in the Dialogflow Request. 

## `<ParseDialogflowRequest>`

Defines a ParseDialogflowRequest policy.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex object  
**Parent Element** |  N/A   
**Child Elements** |  [`<DialogflowVersion>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy#dfverelement)  
[`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy#displaynameelement)  
[`<VariablePrefix>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy#varprefixelement)  
  
  
The following table provides a high-level description of the child elements specific to the ParseDialogflowRequest policy:

Child Element | Required? | Description  
---|---|---  
[`<VariablePrefix>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy#varprefixelement) | Optional | Specifies a custom prefix for the flow variables.  
[`<DialogflowVersion>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy#dfverelement) | Optional | Specifies the Dialogflow version.  
  
### Example

The following example shows a sample webhook request, the corresponding `ParseDialogflowRequest` policy, and the flow variables generated after applying the policy:

### Syntax
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ParseDialogflowRequest continueOnError="false" enabled="true"
            name="POLICY_NAME">
        <!-- The display name for this policy -->
        <DisplayName>DISPLAY_NAME</DisplayName>
        <!-- The optional prefix to be added to all variables created from the
             Dialogflow Webhook request. Note that all variables created from the
             WebhookRequest object will be within a container named
             "google.dialogflow" -->
        <VariablePrefix>CUSTOM_PREFIX</VariablePrefix>
        <!-- The version of Dialogflow for which this request policy is written up.
             This policy supports only the CX version. This element is optional and
             defaults to CX if unspecified -->
        <DialogflowVersion>DIALOGFLOW_VERSION</DialogflowVersion>
    </ParseDialogflowRequest>

### Webhook request

The following example shows the webhook request (in JSON format) from a Dialogflow agent.
    
    
    {
        "fulfillmentInfo": {
            "tag": "check-claim-status"
        },
        "sessionInfo": {
            "session": "projects/apigee-test/locations/global/agents/ea45003d-3f5c-46ba-ac6b-f4c6dc8db707/sessions/5ea2e8-7c1-cf4-2cf-8e4d89e72",
            "parameters": {
                "claimId": "1234",
                "policyId": "abcd"
            }
        },
        "sentimentAnalysisResult": {
          "score": -0.7,
          "magnitude": 0.7
      }
    }

To view the various fields that you can configure in the request, see [ WebhookRequest](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#webhookrequest).

Go to the next sample to see the ParseDialogflowRequest policy configuration. 

### ParseDialogflowRequest policy
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ParseDialogflowRequest continueOnError="false" enabled="true"
            name="DialogflowRequest-InsuranceAgent">
        <DisplayName>Insurance Agent Webhook Request Policy</DisplayName>
        <VariablePrefix>my-prefix</VariablePrefix>
        <DialogflowVersion>CX</DialogflowVersion>
    </ParseDialogflowRequest>

Go to the next sample to see the flow variables created by the policy.

### Flow variables
    
    
    google.dialogflow.my-prefix.fulfillment.tag = "check-claim-status"
    google.dialogflow.my-prefix.session.id = "5ea2e8-7c1-cf4-2cf-8e4d89e72"
    google.dialogflow.my-prefix.session.project.id = "apigee-test"
    google.dialogflow.my-prefix.session.agent.id = "ea45003d-3f5c-46ba-ac6b-f4c6dc8db707"
    google.dialogflow.my-prefix.session.parameters.claimId = "1234"
    google.dialogflow.my-prefix.session.parameters.policyId = "abcd"
    google.dialogflow.my-prefix.sentimentAnalysisResultScore = -0.7
    google.dialogflow.my-prefix.sentimentAnalysisResultMagnitude = 0.7

All the generated flow variables start with **google.dialogflow** followed by the prefix (**my-prefix**) as specified in the `<VariablePrefix>` element. 

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

This section describes the child elements of [`<ParseDialogflowRequest>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy#parsediagrequest). 

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

### `<VariablePrefix>`

Specifies a custom prefix for the flow variables. The value specified in this element is prefixed to all the variable names generated by the ParseDialogflowRequest policy. By default, all variables generated by the policy are prefixed with `google.dialogflow`. If you have specified the `VariablePrefix` element, your custom prefix is added after `google.dialogflow`. Hence, the variable name starts with `google.dialogflow.CUSTOM_PREFIX`.

If you do not specify the `VariablePrefix` element, the variable name is prefixed only with `google.dialogflow`.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<ParseDialogflowRequest>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy#parsediagrequest)  
**Child Elements** |  None   
The `<VariablePrefix>` element uses the following syntax: 

### Syntax
    
    
    <VariablePrefix>VARIABLE_PREFIX</VariablePrefix>

### Example

The following example sets the VariablePrefix to `my-prefix`:
    
    
    <VariablePrefix>my-custom-prefix</VariablePrefix>

As per this configuration, all variable names start with **google.dialogflow.my-custom-prefix**. 

### `<DialogflowVersion>`

Specifies the Dialogflow version. The ParseDialogflowRequest policy supports only the **CX** version. If you do not specify this element in your policy, the version defaults to **CX**.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  N/A   
**Child Elements** |  None   
The `<DialogflowVersion>` element uses the following syntax: 

### Syntax
    
    
    <DialogflowVersion>DIALOGFLOW_VERSION</DialogflowVersion>

### Example

The following example sets the DialogflowVersion to `CX`:
    
    
    <DialogflowVersion>CX</DialogflowVersion>

## Error codes

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause | Fix  
---|---|---|---  
`steps.parsedialogflowrequest.InvalidSessionInfo` | `500` | This error occurs if there is an invalid sessionInfo.session field in a Dialogflow request. A Webhook can use this field to identify a session. For information about the supported session format, see [Class SessionInfo](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Dialogflow.Cx.V3/api/Google.Cloud.Dialogflow.Cx.V3.SessionInfo.html#Google_Cloud_Dialogflow_Cx_V3_SessionInfo_Session). |   
`steps.parsedialogflowrequest.MalformedInput` | `500` | This error occurs when the JSON provided to this policy is invalid or malformed. |   
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

Error name | Cause | Fix  
---|---|---  
`UnsupportedOperation` | This error occurs if you have specified unsupported Dialogflow version in the `DialogflowVersion` element. The ParseDialogflowRequest policy supports only `CX` version. |   
  
### Fault variables

Whenever there are execution errors in a policy, Apigee generates error messages. You can view these error messages in the error response. Many a time, system generated error messages might not be relevant in the context of your product. You might want to customize the error messages based on the type of error to make the messages more meaningful. 

To customize the error messages, you can use either fault rules or the RaiseFault policy. For information about differences between fault rules and the RaiseFault policy, see [FaultRules vs. the RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#rulesvraisefault). You must check for conditions using the `Condition` element in both the fault rules and the RaiseFault policy. Apigee provides fault variables unique to each policy and the values of the fault variables are set when a policy triggers runtime errors. By using these variables, you can check for specific error conditions and take appropriate actions. For more information about checking error conditions, see [Building conditions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#buildingconditions).

The following table describes the fault variables specific to this policy.

Variables | Where | Example  
---|---|---  
`fault.name="FAULT_NAME"` | FAULT_NAME is the name of the fault, as listed in the Runtime errors table. The fault name is the last part of the fault code. | `fault.name Matches "UnresolvedVariable"`  
`ParseDialogflowRequest.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `ParseDialogflowRequest.My-Parse-Dialogflow-Req.failed = true`  
For more information about policy errors, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors). 

## Related topics

Reference implementations of Apigee proxies and shared flows that show the usage of the ParseDialogflowRequest policy are available on Apigee GitHub. For more information, see [Conversational AI Reference Implementations](https://github.com/apigee/conversational-ai-reference-implementations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
