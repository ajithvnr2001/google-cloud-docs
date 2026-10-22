---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/raise-fault-policy/
title: RaiseFault policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:02.833257+00:00
---

# RaiseFault policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/raise-fault-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  RaiseFault policy Stay organized with collections  Save and categorize content based on your preferences. 

[Standard policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The RaiseFault policy generates a custom message in response to an error condition. Use RaiseFault to define a fault response that is returned to the requesting app when a specific condition arises. A custom fault response can be more useful to app developers and app end users than generic error messages or HTTP response codes.

When executed, the RaiseFault policy transfers control from the current flow to the error flow, which then returns the designated fault response to the requesting client app. When the message flow switches to the error flow, no further policy processing occurs. All remaining processing steps are bypassed, and the fault response is returned directly to the requesting app.

The custom fault response can consist of HTTP headers, query parameters, and a message payload. You can use RaiseFault in a ProxyEndpoint or a TargetEndpoint. Usually, you will attach a [Condition](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference) to the RaiseFault policy. After RaiseFault executes, Apigee will perform normal [fault processing](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling), evaluating fault rules, or if there are no fault rules defined, it terminates processing of the request.

This policy is a _Standard policy_ and can be deployed to any environment type. For information on policy types and availability with each environment type, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

Depending on your use case, you might want to use the RaiseFault policy or the [ AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy).

For general information on handling faults, see [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Samples

### Return FaultResponse

In the most common usage, RaiseFault is used to return a custom fault response to the requesting app. For example, this policy will return a `404` status code with no payload:
    
    
    <RaiseFault name="404">
     <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
     <FaultResponse>
       <Set>
         <StatusCode>404</StatusCode>
       </Set>
     </FaultResponse>
    </RaiseFault>

### Return FaultResponse Payload

A more complex example involves returning a custom fault response payload, along with HTTP headers and an HTTP status code. In the following example the fault response is populated with an XML message containing the HTTP status code received by Apigee from the backend service, and a header containing the type of fault that occurred:
    
    
    <RaiseFault name="ExceptionHandler">
     <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
     <FaultResponse>
       <Set>
         <Payload contentType="text/xml">
           <root>Please contact support@company.com</root>
         </Payload>
         <StatusCode>{response.status.code}</StatusCode>
       </Set>
       <Add>
         <Headers>
           <Header name="FaultHeader">{fault.name}</Header>
         </Headers>
       </Add>
     </FaultResponse>
    </RaiseFault>

For a list of all variables that are available for dynamically populating FaultResponse messages, see [Variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference)

### Handle service callout errors

**Sample:** **Learn by doing!**  
This [ Learn Apigee](https://github.com/apigee/api-platform-samples/tree/master/learn-edge/service-callout-2) example shows you how to check the HTTP code in a ServiceCallout response and throw a custom exception based on the value of the code. The example returns a custom error message when the target service returns a 404 status. Just clone the repository and follow the instructions in that topic. The example illustrates a common pattern for handling service callout errors. .

* * *

## Element reference

The element reference describes the elements and attributes of the RaiseFault policy.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <RaiseFault async="false" continueOnError="false" enabled="true" name="Raise-Fault-1">
        <DisplayName>RaiseFault 1</DisplayName>
        <FaultResponse>
            <AssignVariable>
              <Name/>
              <Value/>
            </AssignVariable>
            <Add>
                <Headers/>
            </Add>
            <Copy source="request">
                <Headers/>
                <StatusCode/>
            </Copy>
            <Remove>
                <Headers/>
            </Remove>
            <Set>
                <Headers/>
                <Payload/>
                <StatusCode/>
            </Set>
        </FaultResponse>
        <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </RaiseFault>

## <RaiseFault> attributes
    
    
    <RaiseFault async="false" continueOnError="false" enabled="true" name="Raise-Fault-1">

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
  
## <IgnoreUnresolvedVariables> element

(Optional) Ignores any unresolved variable error in the Flow. Valid values: true/false. Default `true`.

## <FaultResponse> element

(Optional) Defines the response message returned to the requesting client. FaultResponse uses the same settings as the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy).

### <FaultResponse><AssignVariable> element

Assigns a value to a destination flow variable. If the flow variable does not exist, then `AssignVariable` creates it.

For example, use the following code to set the variable named `myFaultVar` in the RaiseFault policy:
    
    
    <FaultResponse>
      <AssignVariable>
        <Name>myFaultVar</Name>
        <Value>42</Value>
      </AssignVariable>
      ...
    </FaultResponse>

You can then refer to that variable in message templates later in the RaiseFault policy. Also, a policy attached to a FaultRule can then access the variable. For example, the following AssignMessage policy uses the variable set in the RaiseFault to set a Header in the fault response:
    
    
    <AssignMessage enabled="true" name="Assign-Message-1">
      <Add>
        <Headers>
          <Header name="newvar">{myFaultVar}</Header>
        </Headers>
      </Add>
      <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
    </AssignMessage>

`<AssignVariable>` in the RaiseFault policy uses the same syntax as the [`<AssignVariable>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#assignvariable) element in the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy).

###  <FaultResponse><Add>/<Headers> element

Adds HTTP headers to the error message. Note that the empty header `<Add><Headers/></Add>` does not add any header. This example copies the value of the request.user.agent flow variable into the header.

The `<Header>` element supports the dynamic string substitution feature called [message templating](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro).
    
    
    <Add>
        <Headers>
            <Header name="user-agent">{request.user.agent}</Header>
        </Headers>
    </Add>

**Default:** | N/A  
---|---  
Presence: | Optional  
**Type:** | String  
  
### <FaultResponse><Copy> element

Copies information _**from**_ the message specified by the `source` attribute **_to_** the error message.
    
    
        <Copy source="request">
            <Headers/>
            <StatusCode/>
        </Copy>

**Default:** |  N/A  
---|---  
**Presence:** |  Optional  
**Type:** |  String  
  
#### Attributes
    
    
    **** <Copy source="response">

Attribute | Description | Presence | Type  
---|---|---|---  
source |  Specifies the source object of the copy.

  * If source is not specified, it is treated as a simple message. For example, if the policy is in the request flow, then the source defaults to the request object. If the policy is in the response flow, it defaults to the response object. If you omit source, you can use an absolute reference to a flow variable as the source of the copy. For example, specify the value as {request.header.user-agent}.
  * If the source variable cannot be resolved, or resolves to a non-message type, <Copy> fails to respond.

| Optional | String  
  
###  <FaultResponse><Copy>/<Headers> element

Copies the specified HTTP header from the source to the error message. To copy all headers, specify `<Copy><Headers/></Copy>.`
    
    
    <Copy source='request'>
        <Headers>
            <Header name="headerName"/>
        </Headers>
    </Copy>

If there are multiple headers with the same name, use the following syntax:
    
    
    <Copy source='request'>
        <Headers>
          <Header name="h1"/>
          <Header name="h2"/>
          <Header name="h3.2"/>
        </Headers>
    </Copy>

This example copies "h1", "h2", and the second value of "h3". If "h3" has only one value, then it is not copied.

**Default:** |  N/A  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
###  <FaultResponse><Copy>/<StatusCode> element

The HTTP status code to copy from the object specified by the source attribute to the error message.
    
    
    <Copy source='response'>
        <StatusCode>404</StatusCode>
    </Copy>

**Default:** | false  
---|---  
Presence: | Optional  
**Type:** | String  
  
###  <FaultResponse><Remove>/<Headers> element

Removes specified HTTP headers from the error message. To remove all the headers, specify `<Remove><Headers/></Remove>`. This example removes the `user-agent` header from the message.
    
    
    <Remove>
        <Headers>
            <Header name="user-agent"/>
        </Headers>
    </Remove>

If there are multiple headers with the same name, use the following syntax:
    
    
    <Remove>
        <Headers>
          <Header name="h1"/>
          <Header name="h2"/>
          <Header name="h3.2"/>
        </Headers>
    </Remove>

This example removes "h1", "h2", and the second value of "h3". If "h3" has only one value, then it is not removed.

**Default:** | N/A  
---|---  
Presence: | Optional  
**Type:** | String  
  
### <FaultResponse><Set> element

Sets information in the error message.

The sub-elements of `<Set>` support the dynamic string substitution feature called [message templating](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro).
    
    
        <Set>
            <Headers/>
            <Payload> </Payload>
            <StatusCode/>
        </Set>

**Default:** | N/A  
---|---  
Presence: | Optional  
**Type:** | N/A  
  
###  <FaultResponse>/<Set>/<Headers> element

Sets or overwrites HTTP headers in the error message. Note that the empty header `<Set><Headers/></Set>` does not set any header. This example sets the `user-agent` header to the message variable specified with the `<AssignTo>` element.
    
    
    <Set>
        <Headers>
            <Header name="user-agent">{request.header.user-agent}</Header>
        </Headers>
    </Set>

**Default:** | N/A  
---|---  
Presence: | Optional  
**Type:** | String  
  
###  <FaultResponse>/<Set>/<Payload> element

Sets the payload of the error message.
    
    
    <Set>
        <Payload contentType="text/plain">test1234</Payload>
    </Set>

Set a JSON payload:
    
    
    <Set>
        <Payload contentType="application/json">
            {"name":"foo", "type":"bar"}
        </Payload>
    </Set>

In a JSON payload, you can insert variables using the `variablePrefix` and `variableSuffix` attributes with delimiter characters as shown in the following example.
    
    
    <Set>
        <Payload contentType="application/json" variablePrefix="@" variableSuffix="#">
            {"name":"foo", "type":"@variable_name#"}
        </Payload>
    </Set>

or, as of cloud release 16.08.17, you can also curly braces to insert variables:
    
    
    <Set>
        <Payload contentType="application/json">
            {"name":"foo", "type":"{variable_name}"}
        </Payload>
    </Set>

Set a mixed payload in XML:
    
    
    <Set>
        <Payload contentType="text/xml">
            <root>
              <e1>sunday</e1>
              <e2>funday</e2>
              <e3>{var1}</e3>
        </Payload>
    </Set>

**Default:** |   
---|---  
Presence: | Optional  
**Type:** | String  
  
#### Attributes
    
    
    **** <Payload contentType="content_type" variablePrefix="char" variableSuffix="char">

Attribute | Description | Presence | Type  
---|---|---|---  
contentType |  If contentType is specified, its value is assigned to the `Content-Type` header. | Optional | String  
variablePrefix | Optionally specifies the leading delimiter on a flow variable because JSON payloads cannot use the default "{" character. | Optional | Char  
variableSuffix | Optionally specifies the trailing delimiter on a flow variable because JSON payloads cannot use the default "}" character. | Optional | Char  
  
###  <FaultResponse>/<Set>/<StatusCode> element

Sets the status code of the response.
    
    
    <Set source='request'>
        <StatusCode>404</StatusCode>
    </Set>

**Default:** | false  
---|---  
Presence: | Optional  
**Type:** | Boolean  
  
## <ShortFaultReason> element

Specifies to display a short fault reason in the response:
    
    
    <ShortFaultReason>true|false</ShortFaultReason>

By default, the fault reason in the response of the policy is:
    
    
    "fault":{"faultstring":"Raising fault. Fault name : Raise-Fault-1","detail":{"errorcode":"errorCode"}}}

To make the message more readable, you can set the `<ShortFaultReason>` element to true to shorten the `faultstring` to just the policy name:
    
    
    "fault":{"faultstring":"Raise-Fault-1","detail":{"errorcode":"errorCode"}}}

Valid values: true/false(default).

**Default:** | false  
---|---  
Presence: | Optional  
**Type:** | Boolean  
  
## Flow variables

Flow variables enable dynamic behavior of policies and Flows at runtime, based on HTTP headers, message content, or Flow context. The following predefined Flow variables are available after a RaiseFault policy executes. For more information about Flow variables, see [Variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

Variable | Type | Permission | Description  
---|---|---|---  
fault.name | String | Read-Only | When the RaiseFault policy executes, this variable is always set to the string `RaiseFault`.  
fault.type | String | Read-Only | Returns the fault type in the error and if not available, an empty string.  
fault.category | String | Read-Only | Returns the fault category in the error and if not available, an empty string.  
  
## Example use of RaiseFault

The following example uses a Condition to enforce the presence of a `queryparam` with the name `zipcode` on the inbound request. If that `queryparam` is not present, the flow will raise a fault via RaiseFault:
    
    
    <Flow name="flow-1">
      <Request>
        <Step>
            <Name>RF-Error-MissingQueryParam</Name>
            <Condition>request.queryparam.zipcode = null</Condition>
        </Step>
       ...
       </Request>
       ...
       <Condition>(proxy.pathsuffix MatchesPath "/locations") and (request.verb = "GET")</Condition>
    </Flow>

The following illustrates what would be in RaiseFault: 
    
    
    <RaiseFault name='RF-Error-MissingQueryParam'>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <FaultResponse>
        <Set>
          <Payload contentType='application/json'>{
      "error" : {
        "code" : 400.02,
        "message" : "invalid request. Pass a zipcode queryparam."
      }
    }
    </Payload>
          <StatusCode>400</StatusCode>
        </Set>
      </FaultResponse>
    </RaiseFault>

## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [ What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause  
---|---|---  
`steps.raisefault.RaiseFault` | `500` | See fault string.  
  
### Deployment errors

None.

### Fault variables

These variables are set when a runtime error occurs. For more information, see [ What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name = "RaiseFault"`  
`raisefault.policy_name.failed` | policy_name is the user-specified name of the policy that threw the fault. | `raisefault.RF-ThrowError.failed = true`  
  
### Example error response

**Note:** For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.
    
    
    {
       "fault":{
          "detail":{
             "errorcode":"steps.raisefault.RaiseFault"
          },
          "faultstring":"Raising fault. Fault name: [name]"
       }
    }

## Schema

Each policy type is defined by an XML schema (`.xsd`). For reference, [policy schemas](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) are available on GitHub.

## Related topics

See [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
