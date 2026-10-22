---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy/
title: SetDialogflowResponse policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:24.352373+00:00
---

# SetDialogflowResponse policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  SetDialogflowResponse policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The SetDialogflowResponse policy facilitates the integration of Dialogflow with Apigee. For more information, see [Integrating Apigee with Contact Center AI](https://docs.cloud.google.com/apigee/docs/api-platform/develop/integrating-apigee-contact-center-ai). 

The SetDialogflowResponse policy processes and formats the response data from your backend systems before sending the data as a [WebhookResponse](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#webhook-response) to the [Dialogflow](https://docs.cloud.google.com/dialogflow/cx/docs) agent. A Dialogflow agent requires the WebhookResponse in a specific format, and the SetDialogflowResponse policy builds the response in the required format. The policy constructs a WebhookResponse in the required format for a Dialogflow agent. The WebhookResponse has natural language phrases and other parameters that the Dialogflow agent understands.

If you are a backend service integrator, you need not spend time understanding the format of the Dialoglfow WebhookResponse. The out-of-the-box SetDialogflowResponse policy handles the processing of the response data seamlessly.

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## `<SetDialogflowResponse>`

Defines a SetDialogflowResponse policy.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex object  
**Parent Element** |  N/A   
**Child Elements** |  [`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#dispname)  
[`<Source>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#source)  
[`<DialogflowVersion>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#diagversion)  
[`<NaturalLanguageResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#nlresponse)  
[`<Parameters>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameters)  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#ignoreunresolvvars)  
  
  
The following table provides a high-level description of all the child elements of the `SetDialogflowResponse` element:

Child Element | Required? | Description  
---|---|---  
[`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#dispname) | Optional | A custom name for the policy.  
[`<Source>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#source) | Optional | Specifies the variable to parse.  
[`<DialogflowVersion>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#diagversion) | Optional | Specifies the Dialogflow version.  
[`<NaturalLanguageResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#nlresponse) | Optional | Encapsulates all content required to be sent as as a `WebhookResponse.FulfillmentResponse` object.  
[`<Parameters>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameters) | Optional | Parent element of `<Parameter>`. Defines the set of parameters to be set in the Webhook's response.  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#ignoreunresolvvars) | Optional | Specifies whether processing stops when an unresolved variable is encountered.  
Other child elements  
[`<MergeBehavior>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#mergebehavior) | Optional | Specifies the merge behavior for the response messages.  
[`<Header>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#header) | Optional | Extracts the value of the specified field in the response header.  
[`<JSONPath>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#jsonpath) | Optional | Extracts the value of the specified JSON path.  
[`<Parameter>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameter) | Required | Specifies a parameter to be set in the `sessionInfo.parameters` object of the Webhook's response.  
[`<Phrase>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrase) | Required | Specifies the phrase (text) to be set in the `fulfillmentResponse.messages` object of the Webhook's response.  
[`<Phrases>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrases) | Optional | Parent element of `<Phrase>`. Defines the set of natural language phrases to be set in the Webhook's response.  
[`<Ref>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#ref) | Optional | Extracts the value of the specified reference variable.  
[`<Value>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#value) | Optional | Sets a custom text to the specified parameter.  
  
### Example

The following example shows a sample SetDialogflowResponse policy and the WebhookResponse sent to the Dialogflow agent:

### Syntax
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <SetDialogflowResponse continueOnError="false" enabled="true"
            name="POLICY_NAME">
        <!-- The display name for this policy -->
        <DisplayName>DISPLAY_NAME</DisplayName>
        <!-- The message variable from which the policy extracts the required information -->
        <Source>MESSAGE_VARIABLE</Source>
        <!-- The version of Dialogflow for which this response policy is written up.
             This policy supports only the CX version. This element is optional and
             defaults to CX if unspecified -->
        <DialogflowVersion>DIALOGFLOW_VERSION</DialogflowVersion>
        <!-- A container object to encapsulate all content needed for a natural
             language response to be returned to Dialogflow from the Southbound API -->
        <NaturalLanguageResponse>
            <!-- Defines the merge behavior for existing responses and new responses.
                 Refer here for more details -->
            <MergeBehavior>MERGE_BEHAVIOR</MergeBehavior>
            <!-- An ordered list of natural language phrases to be returned to
                 Dialogflow from the Southbound API -->
            <Phrases>
                <!-- A phrase is a natural language phrase that Dialogflow agents
                     can send back to their caller/chatting customer -->
                <Phrase>
                    <!-- A phrase can be extracted from the response JSON payload of a
                         service callout -->
                    <JSONPath>JSON_PATH</JSONPath>
                </Phrase>
                <Phrase>
                    <!-- A phrase can be extracted from the response headers of a
                         service callout -->
                    <Header name="HEADER_NAME"/>
                </Phrase>
                <Phrase>
                    <!-- A phrase refer to the value of an existing flow variable -->
                    <Ref>EXISTING_FLOW_VARIABLE</Ref>
                </Phrase>
                <Phrase>
                    <!-- A phrase can be static text -->
                    <Value>CUSTOM_TEXT</Value>
                </Phrase>
            </Phrases>
        </NaturalLanguageResponse>
        <!-- A container object defining the parameters to be set as session parameters
             in the Webhook response sent to Dialogflow -->
        <Parameters>
            <!-- Defines a single parameter to be set in sessionInfo.parameters object
                 of the WebhookResponse object. The name of the parameter is defined
                 as an attribute -->
            <Parameter name="PARAMETER_NAME">
                <!-- A parameter's value can be extracted from the response JSON
                     payload of a service callout -->
                <JSONPath>JSON_PATH</JSONPath>
            </Parameter>
            <Parameter name="PARAMETER_NAME">
                <!-- A parameter's value can be extracted from the response headers
                     of a service callout -->
                <Header name="HEADER_NAME"/>
            </Parameter>
            <Parameter name="PARAMETER_NAME">
                <!-- A parameter's value can be refer to the value of an existing flow
                     variable -->
                <Ref>EXISTING_FLOW_VARIABLE</Ref>
            </Parameter>
            <Parameter name="PARAMETER_NAME">
                <!-- A parameter's value can be static text -->
                <Value>CUSTOM_TEXT</Value>
            </Parameter>
        </Parameters>
        <IgnoreUnresolvedVariables>BOOLEAN_VALUE</IgnoreUnresolvedVariables>
    </SetDialogflowResponse>
          

### SetDialogflowResponse policy

The following example shows the `SetDialogflowResponse` policy definition:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <SetDialogflowResponse continueOnError="false" enabled="true"
            name="CCAIDialogflowResponse-InsuranceAgent">
        <DisplayName>Insurance Agent Webhook Response Policy</DisplayName>
        <Source>myMessageVar</Source>
        <DialogflowVersion>CX</DialogflowVersion>
        <NaturalLanguageResponse>
            <MergeBehavior>APPEND</MergeBehavior>
            <Phrases>
                <Phrase>
                    <JSONPath>$.claim.status.text</JSONPath>
                </Phrase>
                <Phrase>
                    <Header name="X-Response-Text"/>
                </Phrase>
                <Phrase>
                    <Ref>myVar</Ref>
                </Phrase>
                <Phrase>
                    <Value>You call is important to us</Value>
                </Phrase>
            </Phrases>
        </NaturalLanguageResponse>
        <Parameters>
            <Parameter name="claimStatus">
                <JSONPath>$.claim.status.value</JSONPath>
            </Parameter>
            <Parameter name="claimAmount">
                <JSONPath>$.claim.amount</JSONPath>
            </Parameter>
            <Parameter name="timeSpent">
                <Header name="X-Time-Spent"/>
            </Parameter>
            <Parameter name="myVar">
                <Ref>dialogflow.my.var</Ref>
            </Parameter>
            <Parameter name="responder">
                <Value>SYSTEM</Value>
            </Parameter>
        </Parameters>
        <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </SetDialogflowResponse>

Go to the next sample to see the Webhook response created by this policy.

### Webhook response

The following example shows a WebhookResponse sent to the Dialogflow agent:
    
    
    {
        "fulfillmentResponse": {
            "mergeBehavior": "APPEND",
            "messages": [{
                "text": {
                    "text": ["Your claim is currently being processed",
                              "Please call back in a couple of days"]
                }
            }]
        },
        "sessionInfo": {
            "parameters": {
                "claimStatus": "PROCESSING",
                "claimAmount": 1000
            }
        }
    }

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

This section describes the child elements of [`<SetDialogflowResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#setdiagresponse). 

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

### `<Source>`

Specifies the variable to be parsed. The value of `<Source>` defaults to `message`. The `message` value is context-sensitive. In a request flow, `message` resolves to the request message. In a response flow, `message` resolves to the response message.

While you often use this policy to extract information from a request or response message, you can use it to extract information from any variable. For example, you can use it to extract information from an entity created by the [AccessEntity policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-entity-policy), from data returned by the [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy), or extract information from an XML or JSON object.  
  
If `<Source>` cannot be resolved, or resolves to a non-message type, the policy fails and you will get a runtime error.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<SetDialogflowResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#setdiagresponse)  
**Child Elements** |  None   
The `<Source>` element uses the following syntax: 

### Syntax
    
    
    <Source>MESSAGE_VARIABLE</Source>

### Example

The following example sets the Source to `myMessageVar`:
    
    
    <Source>myMessageVar</Source>

### `<DialogflowVersion>`

Specifies the Dialogflow version. The SetDialogflowResponse policy supports only the **CX** version. If you do not specify this element in your policy, the version defaults to **CX**.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<SetDialogflowResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#setdiagresponse)  
**Child Elements** |  None   
The `<DialogflowVersion>` element uses the following syntax: 

### Syntax
    
    
    <DialogflowVersion>DIALOGFLOW_VERSION</DialogflowVersion>

### Example

The following example sets the DialogflowVersion to `CX`:
    
    
    <DialogflowVersion>CX</DialogflowVersion>

### `<IgnoreUnresolvedVariables>`

Determines whether processing stops when an unresolved variable is encountered.

**Default Value** | True  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<SetDialogflowResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#setdiagresponse)  
**Child Elements** |  None   
  
Set to `true` to ignore unresolved variables and continue processing; otherwise `false`. The default value is `true`.

Setting `<IgnoreUnresolvedVariables>` to `true` is different from setting the [`<SetDialogflowResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#setdiagresponse)'s `continueOnError` to `true`. If you set `continueOnError` to `true`, Apigee ignores all errors, not only errors in variables.

The `<IgnoreUnresolvedVariables>` element uses the following syntax:

### Syntax
    
    
     <IgnoreUnresolvedVariables>[true|false]</IgnoreUnresolvedVariables>

### Example

The following example sets `<IgnoreUnresolvedVariables>` to `false`:
    
    
           <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>

### `<MergeBehavior>`

Defines the merge behavior for the response messages. You can specify any of the following values: 

  * `APPEND`: Appends the messages to the list of messages waiting to be sent to the user. 
  * `REPLACE`: Replaces the older messages with newer messages in the list of messages waiting to be sent to the user.

If you do not specify the element, the behavior defaults to `APPEND`. **Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<NaturalLanguageResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#nlresponse)  
**Child Elements** |  None   
The `<MergeBehavior>` element uses the following syntax: 

### Syntax
    
    
    <MergeBehavior>BEHAVIOR</MergeBehavior>

### Example

The following example sets the merge behavior to `APPEND`:
    
    
    <MergeBehavior>APPEND</MergeBehavior>

### `<NaturalLanguageResponse>`

Encapsulates all the natural language response that you want to send to the Dialogflow agent.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex Object  
**Parent Element** |  [`<SetDialogflowResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#setdiagresponse)  
**Child Elements** |  [`<MergeBehavior>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#mergebehavior)  
[`<Phrases>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrases)  
  
  
### `<Parameters>`

Defines the set of parameters to be set in the Webhook's response. The name of the parameter is as an attribute of the `<Parameter>` element. 

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex Object  
**Parent Element** |  [`<SetDialogflowResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#setdiagresponse)  
**Child Elements** |  [`<Parameter>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameter)  
  
### `<Parameter>`

Specifies a parameter to be set in the **sessionInfo.parameters** object of the Webhook's response.

You can specify a static text as a parameter value or extract the value from any of the following fields in the response:

  * Response header fields
  * JSON payload
  * Flow variables



You must define a separate `<Parameter>` element for each value that you want to extract.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex Object  
**Parent Element** |  [`<Parameters>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameters)  
**Child Elements** |  [`<Header>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#header)  
[`<JSONPath>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#jsonpath)  
[`<Ref>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#ref)  
[`<Value>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#value)  
  
The `<Parameter>` element has the following attributes: Attribute | Description | Required? | Type  
---|---|---|---  
`name` | The name of the variable to create with this parameter. | Yes | String  
  
The `<Parameter>` element uses the following syntax:

### Syntax
    
    
    <Parameters>
      <Parameter name="PARAMETER_NAME">
      <Header name="HEADER_NAME"/>
    </Parameter>
    <Parameter name="PARAMETER_NAME">
      <JSONPath>JSON_PATH</JSONPath>
    </Parameter>
    <Parameter name="PARAMETER_NAME">
      <Ref>EXISTING_FLOW_VARIABLE</Ref>
    </Parameter>
    <Parameter name="PARAMETER_NAME">
      <Value>CUSTOM_TEXT</Value>
    </Parameter>
    </Parameters>

### Extract Header field value

This example sets the **timeSpent** parameter to the value of the **X-Time-Spent** header field.
    
    
    <Parameter name="timeSpent">
         <Header name="X-Time-Spent"/>
    </Parameter>

### Extract JSON path value

This example sets the **claimAmount** parameter to the value of the **claim.amount** field in the JSON payload.
    
    
    <Parameter name="claimAmount">
       <JSONPath>$.claim.amount</JSONPath>
    </Parameter>

### Extract flow variable value

This example sets the **myVar** parameter to the value of the **dialogflow.my.var** flow variable.
    
    
    <Parameter name="myVar">
       <Ref>dialogflow.my.var</Ref>
    </Parameter>
           

### Set custom text

This example sets the value of the **responder** parameter to **SYSTEM**.
    
    
    <Parameter name="responder">
       <Value>SYSTEM</Value>
    </Parameter>

### `<Phrases>`

Parent element of `<Phrase>`. Defines the ordered list of natural language phrases to be set in the Webhook's response. 

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex Object  
**Parent Element** |  [`<NaturalLanguageResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#nlresponse)  
**Child Elements** |  [`<Phrase>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrase)  
  
### `<Phrase>`

Specifies the phrase (text) to be set in **fulfillmentResponse.messages** object of the Webhook's response.

You can specify a static text as a phrase value or extract the value from any of the following fields in the response:

  * Response header fields
  * JSON payload
  * Flow variables



You must define a separate `<Phrase>` element for each value you want to extract.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex Object  
**Parent Element** |  [`<Phrases>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrases)  
**Child Elements** |  [`<Header>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#header)  
[`<JSONPath>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#jsonpath)  
[`<Ref>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#ref)  
[`<Value>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#value)  
  
  
The `<Phrase>` element uses the following syntax:

### Syntax
    
    
    <Phrases>
      <Phrase>
        <Header name="HEADER_NAME"/>
      </Phrase>
      <Phrase>
        <JSONPath>JSON_PATH</JSONPath>
      </Phrase>
      <Phrase>
        <Ref>EXISTING_FLOW_VARIABLE</Ref>
      </Phrase>
      <Phrase>
        <Value>CUSTOM_TEXT</Value>
      </Phrase>
    </Phrases>

### Extract Header field value

This example sets a natural language text in the response to the value of the `X-Response-Text` header field.
    
    
    <Phrase>
         <Header name="X-Response-Text"/>
    </Phrase>

### Extract JSON path value

This example sets a natural language text in the response to the value of the `claim.status.text` field in the JSON payload.
    
    
    <Phrase>
       <JSONPath>$.claim.status.text</JSONPath>
    </Phrase>

### Extract flow variable value

This example sets a natural language text in the response to the value of the `myVar` flow variable.
    
    
    <Phrase>
       <Ref>myVar</Ref>
    </Phrase>
           

### Set custom text

This example adds the text `You call is important to us` to the natural language text in the response.
    
    
    <Phrase>
       <Value>You call is important to us</Value>
    </Phrase>

### `<Header>`

Extracts the value from the specified field in the response header. You can use the header value either to set a natural language text or a response parameter.

  * To extract the header value as a natural language response, specify the `<Header>` element inside the [`<Phrase>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrase) element.
  * To extract the header value as a response parameter, specify the `<Header>` element inside the [`<Parameter>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameter) element.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<Phrase>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrase)  
[`<Parameter>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameter)  
  
**Child Elements** |  None   
The `<Header>` element uses the following syntax: 

### Syntax
    
    
    <Header name="HEADER_FIELD"/>

### Example 1

The following example gets the value of the `X-Response-Text` header field as a natural language response:
    
    
    <Phrase>
      <Header name="X-Response-Text"/>
    <Phrase/>

### Example 2

The following example gets the value of the `X-Response-Text` header field as a response parameter:
    
    
    <Parameter name="timeSpent">
      <Header name="X-Response-Text"/>
    <Parameter/>

The `timeSpent` flow variable is set to the value of the `X-Response-Text` header field.

The `<Header>` element has the following attributes:

Attribute | Description | Required ? | Type  
---|---|---|---  
name | Specifies the name of the response header from which you extract the value. | Required | String  
  
### `<JSONPath>`

Extracts the value of a JSON path in a JSON payload of the service callout. You can use the value either to set a natural language text or a response parameter.

  * To extract the JSON value as a natural language text, specify the `<JSONPath>` element inside the [`<Phrase>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrase) element.
  * To extract the JSON value as a response parameter, specify the `<JSONPath>` element inside the [`<Parameter>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameter) element.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<Phrase>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrase)  
[`<Parameter>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameter)  
  
**Child Elements** |  None   
The `<JSONPath>` element uses the following syntax: 

### Syntax
    
    
    <JSONPath>JSON_PATH</JSONPath>

### Example 1

The following example gets the value of the `claim.status.text` JSON field as a natural language response:
    
    
    <Phrase>
      <JSONPath>$.claim.status.text</JSONPath>
    <Phrase/>

### Example 2

The following example gets the value of the `claim.amount` JSON field as a response parameter:
    
    
    <Parameter name="claimAmount">
      <JSONPath>$.claim.amount.</JSONPath>
    <Parameter/>

The `claimAmount` flow variable is set to the value of the `{claim.amount}` JSON field.

### `<Ref>`

Extracts the value of an existing flow variable. You can use the value either to set a natural language text or a response parameter.

  * To extract the value of a variable as a natural language text, specify the `<Ref>` element inside the [`<Phrase>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrase) element.
  * To extract the value of a variable as a response parameter, specify the `<Ref>` element inside the [`<Parameter>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameter) element.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<Phrase>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrase)  
[`<Parameter>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameter)  
  
**Child Elements** |  None   
The `<Ref>` element uses the following syntax: 

### Syntax
    
    
    <Ref>EXISTING_FLOW_VARIABLE</Ref>

### Example 1

The following example gets the value of the `myVar` flow variable as a natural language response:
    
    
    <Phrase>
      <Ref>myVar</Ref>
    <Phrase/>

### Example 2

The following example gets the value of the `dialogflow.my.var` flow variable as a response parameter:
    
    
    <Parameter name="customVar">
      <Ref>dialogflow.my.var</Ref>
    <Parameter/>

The `customVar` flow variable is set to the value of the `dialogflow.my.var` variable.

### `<Value>`

Sets a literal value to a natural language text or a response parameter.

  * To set the literal value as a natural language text, specify the `<Value>` element inside the [`<Phrase>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrase) element.
  * To set the literal value as a response parameter, specify the `<Value>` element inside the [`<Parameter>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameter) element.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<Phrase>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#phrase)  
[`<Parameter>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy#parameter)  
  
**Child Elements** |  None   
The `<Value>` element uses the following syntax: 

### Syntax
    
    
    <Value>CUSTOM_TEXT</Value>

### Example 1

The following example sets the literal text `You call is important to us` as a natural language response:
    
    
    <Phrase>
      <Value>You call is important to us</Value>
    <Phrase/>

### Example 2

The following example sets the literal text `SYSTEM` as a response parameter:
    
    
    <Parameter name="responder">
      <Value>SYSTEM</Value>
    <Parameter/>

The `responder` flow variable is set to `SYSTEM`.

## Error codes

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause  
---|---|---  
`steps.setdialogflowresponse.ExecutionFailed` | `500` | This error occurs when the execution of the policy failed because of a generic exception. The fault message has the details of the exception.  
`steps.setdialogflowresponse.InvalidSourceType` | `500` | This error occurs if the variable specified in the <Source> element is not of [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) type.  
`steps.setdialogflowresponse.MalformedInput` | `500` | This error occurs when the JSON provided to this policy is invalid or malformed.  
`steps.setdialogflowresponse.SourceMessageNotAvailable` | `500` | This error occurs if the [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) variable specified in the `Source` element of the policy is either: 

  * Out of scope (not available in the specific flow where the policy is executed)
or 
  * Can't be resolved (is not defined)

  
`steps.setdialogflowresponse.UnresolvedHeader` | `500` | This error occurs if the `Header` element has an invalid header. For example, if the `Header` element has the value `X-Response-Text`, and there is no `X-Response-Text` in the response header, you will get this error.   
`steps.setdialogflowresponse.UnresolvedJSONPath` | `500` | This error occurs if the `JSONPath` element has an invalid path. For example, if the `JSONPath` element has the value `{claim.status.value}`, and there is no `status` object in the JSON payload, you will get this error.  
`steps.setdialogflowresponse.UnresolvedVariable` | `500` |  This error occurs if a variable specified in the SetDialogflowResponse policy is either:

  * Out of scope (not available in the specific flow where the policy is being executed)
or 
  * Can't be resolved (is not defined)

  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

Error name | Cause  
---|---  
`UnsupportedOperation` | This error occurs if you have specified unsupported Dialogflow version in the `DialogflowVersion` element. The SetDialogflowResponse policy supports only the `CX` version.  
  
### Fault variables

Whenever there are execution errors in a policy, Apigee generates error messages. You can view these error messages in the error response. Many a time, system generated error messages might not be relevant in the context of your product. You might want to customize the error messages based on the type of error to make the messages more meaningful. 

To customize the error messages, you can use either fault rules or the RaiseFault policy. For information about differences between fault rules and the RaiseFault policy, see [FaultRules vs. the RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#rulesvraisefault). You must check for conditions using the `Condition` element in both the fault rules and the RaiseFault policy. Apigee provides fault variables unique to each policy and the values of the fault variables are set when a policy triggers runtime errors. By using these variables, you can check for specific error conditions and take appropriate actions. For more information about checking error conditions, see [Building conditions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#buildingconditions).

The following table describes the fault variables specific to this policy.

Variables | Where | Example  
---|---|---  
`fault.name="FAULT_NAME"` | FAULT_NAME is the name of the fault, as listed in the Runtime errors table. The fault name is the last part of the fault code. | `fault.name Matches "UnresolvedVariable"`  
`setdialogflowresponse.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `setdialogflowresponse.My-Set-Dialogflow-Response.failed = true`  
For more information about policy errors, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors). 

## Related topics

Reference implementations of Apigee proxies and shared flows that show the usage of the SetDialogflowResponse policy are available on Apigee GitHub. For more information, see [Conversational AI Reference Implementations](https://github.com/apigee/conversational-ai-reference-implementations). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
