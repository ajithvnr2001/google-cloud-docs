---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy/
title: SanitizeUserPrompt policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:24.560525+00:00
---

# SanitizeUserPrompt policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  SanitizeUserPrompt policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** This policy is supported on Apigee, and on Apigee hybrid **version 1.15.1 and later**.

The SanitizeUserPrompt policy protects AI applications from harmful content by sanitizing user prompts sent to generative AI models. The policy uses [Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) to evaluate user prompts for harmful content, enabling native protection for AI workloads using Apigee. Model Armor is a Google Cloud service offering AI security and safety measures to mitigate the risks associated with large language models (LLMs).

This policy works in conjunction with the [SanitizeModelResponse policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy).

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

**Note:** If you have configured a forward proxy for your environment, the outbound calls this policy makes to Model Armor are routed through the proxy. No policy-level configuration is required. This is applicable for Apigee and Apigee Hybrid 1.16.10 and later, and 1.17.0 and later. For more information, see [Configure forward proxying](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#forward-proxying) (Apigee) or [Configure forward proxying for API proxies](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/forward-proxy) (Apigee Hybrid).

## Before you begin

Before you use the SanitizeUserPrompt policy, complete the following tasks:

  * Create a Model Armor template. Complete this step before you create a SanitizeUserPrompt policy.
  * Set the API endpoint for the Model Armor service.
  * Create a SanitizeModelResponse policy. Complete this task before you deploy the SanitizeUserPrompt policy.



### Required roles

To get the permissions that you need to apply and use the SanitizeUserPrompt policy, ask your administrator to grant you the following IAM roles on the service account you use to deploy Apigee proxies: 

  * [Model Armor User ](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) (`roles/modelarmor.user`)
  * [Model Armor Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.viewer) (`roles/modelarmor.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

Enable the Model Armor API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=modelarmor.googleapis.com)

## `<SanitizeUserPrompt>` element

Defines a SanitizeUserPrompt policy.

**Default Value** | See **Default Policy** tab, below  
---|---  
**Required?** | Required  
**Type** | Complex object  
**Parent Element** |  N/A   
**Child Elements** |  [`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#displayname)  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#ignoreunresolvedvariables)  
[`<TemplateName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#templatename)  
[`<UserPromptSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#userpromptsource)  
  
  
The [`<SanitizeUserPrompt>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#name) element uses the following syntax:

### Syntax
    
    
    <SanitizeUserPrompt async="false" continueOnError="false" enabled="true" name="sanitize-text">
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <DisplayName>Sanitize-Text-sample</DisplayName>
      <ModelArmor>
        <TemplateName>projects/{project}/locations/{location}/templates/{template-name}</TemplateName>
      </ModelArmor>
      <UserPromptSource>{jsonPath('$.contents[-1].parts[-1].text',request.content,true)}</UserPromptSource>
      <FunctionResponseSource>{jsonPath('$.contents[-1].parts[-1].functionResponse.response',request.content,true)}</FunctionResponseSource>
    </SanitizeUserPrompt>

### Default Policy

The following example shows the default settings when you add a SanitizeUserPrompt policy to your request flow in the Apigee UI:
    
    
    <SanitizeUserPrompt async="false" continueOnError="false" enabled="true" name="sanitize-text">
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <DisplayName>Sanitize-Text-sample</DisplayName>
      <ModelArmor>
        <TemplateName>projects/{project}/locations/{location}/templates/{template-name}</TemplateName>
      </ModelArmor>
      <UserPromptSource>{jsonPath('$.contents[-1].parts[-1].text',request.content,true)}</UserPromptSource>
      <FunctionResponseSource>{jsonPath('$.contents[-1].parts[-1].functionResponse.response',request.content,true)}</FunctionResponseSource>
    </SanitizeUserPrompt>

When you insert a new SanitizeUserPrompt policy using the Apigee UI, the template contains stubs for all possible operations. See below for information on required elements.

This element has the following attributes that are common to all policies:

**Attribute** | **Default** | **Required?** | **Description**  
---|---|---|---  
`name` | N/A | **Required** |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name.  
`continueOnError` | false | Optional | Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also: 

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

  
`enabled` | true | Optional | Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow.  
`async` not_interested | false | Deprecated | This attribute is deprecated.  
  
The following table provides a high level description of the child elements of [`<SanitizeUserPrompt>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#name): 

Child Element | Required? | Description  
---|---|---  
[`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#displayname) | Optional | The name of the policy.   
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#ignoreunresolvedvariables) | Optional | Specifies whether processing stops if the variable used for the template name or Model Armor payload is unresolved.  
[`<ModelArmor>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#modelarmor) | Required | Contains the required information for specifying the Model Armor template.  
[`<UserPromptSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#userpromptsource) | Optional | The location of the payload for the user prompt text to be extracted. Only string text values are supported. This field supports Apigee message template syntax, including the use of [ variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#use-curly-braces-to-denote-variables) or [JSON Path functions.](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#json-path-function) For example: 
    
    
    {jsonpath('$.input.prompt.text',request.content,false)}  
  
`<FunctionResponseSource>` | Optional | The location of the function/tool response data to extract. Used as a fallback when `<UserPromptSource>` returns empty on function calling turns. Default: `{jsonPath('$.contents[-1].parts[-1].functionResponse.response',request.content,true)}`  
  
## Example

This section provides an example using the [`<SanitizeUserPrompt>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#name).

This example uses all default values for model detection and prompt extraction:
    
    
    <SanitizeUserPrompt async="false" continueOnError="false" enabled="true" name="sanitize-text">
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <DisplayName>Sanitize-Text-sample</DisplayName>
      <ModelArmor>
        <TemplateName>projects/{project}/locations/{location}/templates/{template-name}</TemplateName>
      </ModelArmor>
    </SanitizeUserPrompt>

## Child element reference

This section describes the child elements of [`<SanitizeUserPrompt>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#name).

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

### <IgnoreUnresolvedVariables>

Determines whether processing stops when a variable is unresolved. Set to `true` to ignore unresolved variables and continue processing.

**Default Value** | False  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<SanitizeUserPrompt>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#name)  
**Child Elements** |  None   
  
### `<ModelArmor>`

Contains the required information for specifying the Model Armor template.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | String  
**Parent Element** |   
**Child Elements** |  [`<TemplateName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#templatename)  
  
The `<ModelArmor>` element uses the following syntax:

### Syntax
    
    
    <ModelArmor>
      <TemplateName>projects/{project}/locations/{location}/templates/{template-name}</TemplateName>
    </ModelArmor>

### Example

This example uses Apigee flow variables to populate the required information.
    
    
    <ModelArmor>
      <TemplateName>projects/**{ organization.name}**/locations/**{ system.region.name}**/templates/**{ id}**</TemplateName>
    </ModelArmor>

The following table provides a high-level description of the child elements of [`<ModelArmor>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#modelarmor).

Child Element | Required? | Description  
---|---|---  
`<TemplateName>` | Required | String The Model Armor template used to sanitize the user prompt. This value can be templated using the following Apigee flow variables: 
    
    
    projects/{organization.name}/locations/{system.region.name}/templates/{id}  
  
### `<UserPromptSource>`

The location of the payload for the user prompt text to be extracted. This field supports Apigee message template syntax, including the use of [ variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#use-curly-braces-to-denote-variables) or [JSON Path functions](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#json-path-function). For example: 
    
    
    {jsonpath('$.input.prompt.text',request.content,false)}

**Default Value** | {jsonPath('$.contents[-1].parts[-1].text',request.content,true)}  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<SanitizeUserPrompt>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#name)  
**Child Elements** |  None   
  
### <FunctionResponseSource>

The location of the function or tool response data to extract from the request. This element is used as a fallback when `<UserPromptSource>` returns empty, which occurs on function calling turns where the last content entry contains a function response instead of text. Function response data must be sanitized because it contains untrusted external data from APIs and databases.

This field supports message template syntax, including JSON Path functions.

**Default Value** | {jsonPath('$.contents[-1].parts[-1].functionResponse.response',request.content,true)}  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<SanitizeUserPrompt>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#name)  
**Child Elements** |  None   
  
## Flow variables

Flow variables configure dynamic runtime behavior for policies and flows, based on HTTP headers or message content, or the context available in the Flow. For more information about flow variables, see [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

This policy provides the following set of _read-only_ flow variables during execution. You can use these flow variables with the [DataCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy) to create custom analytics reports. For more information, see [Collecting customer data with the Data Capture policy](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture).

Variable name | Description  
---|---  
`SanitizeUserPrompt.POLICY_NAME.templateUsed` | Specifies which model armor template is used. For example: `projects/myproject/locations/us-west1/templates/mytemplate`  
`SanitizeUserPrompt.POLICY_NAME.userPrompt` | Specifies the prompt content used for the call to Model Armor to sanitize the content.  
`SanitizeUserPrompt.POLICY_NAME.modelResponse` | Specifies the LLM response content used for the call to Model Armor to sanitize the content.  
`SanitizeUserPrompt.POLICY_NAME.responseFromModelArmor` | Specifies the json response from Model Armor.  
`SanitizeUserPrompt.POLICY_NAME.filterMatchState` | Specifies whether the filter matched. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeUserPrompt.POLICY_NAME.invocationResult` | A field indicating the outcome of the invocation, irrespective of match status. It can have the following: 

  * SUCCESS: All filters executed successfully.
  * PARTIAL: Some filters were skipped or failed execution.
  * FAILURE: All filters were skipped or failed execution.

  
`SanitizeUserPrompt.POLICY_NAME.raiFilterResult.executionState` | Rai filter execution result. Valid values include `EXECUTION_SUCCESS` and `EXECUTION_SKIPPED`.  
`SanitizeUserPrompt.POLICY_NAME.raiFilterResult.matchState` | Rai filter match state. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeUserPrompt.POLICY_NAME.sdpFilterResult.inspectResult.executionState` | Sdp filter inspect result execution state. Valid values include `EXECUTION_SUCCESS` and `EXECUTION_SKIPPED`.  
`SanitizeUserPrompt.POLICY_NAME.sdpFilterResult.inspectResult.matchState` | Sdp filter inspect result match state. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeUserPrompt.POLICY_NAME.sdpFilterResult.deidentifyResult.executionState` | Sdp filter de identify result execution state. Valid values include `EXECUTION_SUCCESS` and `EXECUTION_SKIPPED`.  
`SanitizeUserPrompt.POLICY_NAME.sdpFilterResult.deidentifyResult.matchState` | Sdp filter de identify result match state. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeUserPrompt.POLICY_NAME.piAndJailbreakFilterResult.executionState` | Prompt injection and Jailbreak filter results execution state. Valid values include `EXECUTION_SUCCESS` and `EXECUTION_SKIPPED`.  
`SanitizeUserPrompt.POLICY_NAME.piAndJailbreakFilterResult.matchState` | Prompt injection and Jailbreak filter results match state. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeUserPrompt.POLICY_NAME.csamFilterFilterResult.executionState` | CSAM filter execution state. Valid values include `EXECUTION_SUCCESS` and `EXECUTION_SKIPPED`.  
`SanitizeUserPrompt.POLICY_NAME.csamFilterFilterResult.matchState` | CSAM filter match state. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeUserPrompt.POLICY_NAME.maliciousUriFilterResult.executionState` | Malicious URI filter execution state. Valid values include `EXECUTION_SUCCESS` and `EXECUTION_SKIPPED`.  
`SanitizeUserPrompt.POLICY_NAME.maliciousUriFilterResult.matchState` | Malicious URI filter match state. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeUserPrompt.POLICY_NAME.sanitizationMetadata.errorCode` | Custom overridden Error code if present in Model Armor response.  
`SanitizeUserPrompt.POLICY_NAME.sanitizationMetadata.errorMessage` | Custom overridden Error code if present in Model Armor response.  
`SanitizeUserPrompt.POLICY_NAME.csamFilterMatched` | Boolean value indicating whether the CSAM filter matched.  
`SanitizeUserPrompt.POLICY_NAME.maliciousURIs` | Appended list of malicious URIs detected by the malicious URI filter.  
`SanitizeUserPrompt.POLICY_NAME.maliciousURIsDetected` | Boolean value indicating whether the malicious URI filter matched.  
`SanitizeUserPrompt.POLICY_NAME.matchesFound` | Boolean value indicating whether any of the filters matched.  
`SanitizeUserPrompt.POLICY_NAME.promptInjectionDetected` | Boolean value indicating whether the prompt injection filter matched.  
`SanitizeUserPrompt.POLICY_NAME.promptInjectionConfidence` | Confidence level of prompt injection detection.  
`SanitizeUserPrompt.POLICY_NAME.raiMatchesFound` | Boolean value indicating whether the RAI filter matched.  
`SanitizeUserPrompt.POLICY_NAME.requestSentToModelArmor` | Boolean value indicating whether a request was sent to Model Armor.  
`SanitizeUserPrompt.POLICY_NAME.sanitizeOperation` | Specifies the operation performed by the policy. Valid values include `SANITIZE_USER_PROMPT` and `SANITIZE_MODEL_RESPONSE`.  
  
## Error reference

This section describes the fault codes and error messages that Apigee returns and the fault variables that Apigee sets for the SanitizeUserPrompt policy. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause  
---|---|---  
`steps.sanitize.user.prompt.response.FilterMatched` | `400` | This error occurs if the user prompt does not pass the Model Armor template check.  
`steps.sanitize.user.prompt.SanitizationResponseParsingFailed` | `500` | This error occurs if the Model Armor response cannot be parsed.  
`steps.sanitize.user.prompt.FailedToExtractUserPrompt` | `500` | This error occurs if the automatic user prompt extraction for the default value failed.  
`steps.sanitize.user.prompt.InternalError` | `500` | This error occurs if there is an internal server error.  
`steps.sanitize.modelarmor.ModelArmorTemplateNameExtractionFailed` | `500` | This error occurs if the template name cannot be resolved.  
`steps.sanitize.modelarmor.AuthenticationFailure` | `500` | This error occurs if the service account does not have permission to call the Model Armor API.  
`steps.sanitize.modelarmor.ModelArmorAPIFailed` | `500` | This error occurs if the Model Armor API throws an error.  
`steps.sanitize.modelarmor.ModelArmorCalloutError` | `500` | This error occurs if the Model Armor API call fails.  
`steps.sanitize.modelarmor.ServiceUnavailable` | `500` | This error occurs if the Model Armor service is unavailable.  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

Error name | Cause  
---|---  
`The ModelArmor/TemplateName element is required.` | Occurs if the <TemplateName> element in <ModelArmor> is not present.  
`The TemplateName element value is required.` | Occurs if the <TemplateName> value is empty.  
  
### Fault variables

This policy sets these variables when it triggers an error at runtime. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="FAULT_NAME"` | FAULT_NAME is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name Matches "UnresolvedVariable"`  
`SanitizeUserPrompt.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `SanitizeUserPrompt.sanitize-prompt.failed = true`  
  
### Example error response

**Note:** For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.
    
    
    {
      "fault": {
        "faultstring": "SanitizeUserPrompt[sanitize-prompt]: unable to resolve variable [variable_name]",
        "detail": {
          "errorcode": "steps.sanitizeuserprompt.UnresolvedVariable"
        }
      }
    }

### Example fault rule
    
    
    <FaultRule name="SanitizeUserPrompt Faults">
        <Step>
            <Name>SUP-CustomSetVariableErrorResponse</Name>
            <Condition>(fault.name = "SetVariableFailed")</Condition>
        </Step>
        <Condition>(sanitizeuserprompt.failed = true)</Condition>
    </FaultRule>

### Model Armor template error code and error messages

The Model Armor template supports overriding error codes and error messages thrown by the SanitizeUserPrompt policy's API requests. If the user sets the overrides, then the Model Armor error codes and error messages populate the flow variables.

For example, a response with Model Armor error codes and messages could look like the following: 
    
    
    {
      "sanitizationResult": {
        "filterMatchState": "MATCH_FOUND",
        "filterResults": {...},
        "sanitizationMetadata": {
          "errorCode": "890",
          "errorMessage": "get out"
          },
        "invocationResult": "SUCCESS"
      }
    }

## Schemas

Each policy type is defined by an XML schema (`.xsd`). For reference, [policy schemas](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) are available on GitHub.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
