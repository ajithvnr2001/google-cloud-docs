---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/assign-message-runtime-errors/
title: Assign Message runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:26.871096+00:00
---

# Assign Message runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/assign-message-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Assign Message runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/assign-message-runtime-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/assign-message-runtime-errors/).

## UnresolvedVariable

### Error code
    
    
    steps.assignmessage.UnresolvedVariable
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "AssignMessage[policy_name]: unable to resolve variable [variable_name]",
            "detail": {
                "errorcode": "steps.assignmessage.UnresolvedVariable"
            }
        }
    }

### Cause

This error occurs if a variable specified in the [Assign Message policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) is either:

  * out of scope (not available in the specific flow where the policy is being executed) or
  * can't be resolved (is not defined)



For example, this error occurs if the Assign Message policy executes in the request flow, but the `source` attribute in the `<Copy>` element is set to the `response` or `error` variable or any other custom variable that does not exist in the request flow.

### Diagnosis

  1. Identify the Assign Message Policy where the error occurred and the name of the variable that is not available. You can find both of these items in the `faultstring` element of the error response.

For example, in the following `faultstring`, the policy name is `googleBook` and the variable is `var`:
         
         "faultstring": "AssignMessage[googleBook]: unable to resolve variable var"
         

  2. In the failed Assign Message Policy XML, verify that the name of the variable used matches the variable name identified in the fault string (step #1 above). For example, the following policy sets the source attribute in the `<Copy>` element to a variable named `var`, which matches what's in the `faultstring`:
         
         <AssignMessage async="false" continueOnError="false" enabled="true" name="Assign-Message-1">
            <DisplayName>googleBook</DisplayName>
            <Properties />
            <Copy source="var">
               <Headers>
                  <Header name="user-agent" />
               </Headers>
            </Copy>
            <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
            <AssignTo createNew="true" transport="http" type="request">googleBookReq</AssignTo>
         </AssignMessage>
         

  3. Determine if the variable is defined and available in the flow in which the Assign Message policy is being executed.

  4. If the variable is either:

     1. out of scope (not available in the specific flow where the policy is being executed) or
     2. can't be resolved (is not defined)

then that's the cause for the error.

As an example, let's say the Assign Message policy shown above executes in the request flow. Check if the variable `var` is defined in any of the policies that are executed before the Assign Message policy in the request flow. If the variable has not been defined, then you will receive the error code:
    
    steps.assignmessage.UnresolvedVariable
    




### Resolution

Ensure that the variable referenced in the policy exists and is available in the specific flow, where the Assign Message policy is being executed.

To correct the example policy shown above, you can modify the source attribute in the `<Copy>` element to be the request variable or any other custom variable of type message that exists in the request flow.
    
    
    <AssignMessage async="false" continueOnError="false" enabled="true" name="Assign-Message-1">
       <DisplayName>googleBook</DisplayName>
       <Properties />
       <Copy source="request">
          <Headers>
             <Header name="user-agent" />
          </Headers>
       </Copy>
       <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
       <AssignTo createNew="true" transport="http" type="request">googleBookReq</AssignTo>
    </AssignMessage>
    

## VariableOfNonMsgType

### Error code
    
    
    steps.assignmessage.VariableOfNonMsgType
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "AssignMessage[policy_name]: value of variable [variable] is not of type Message",
            "detail": {
                "errorcode": "steps.assignmessage.VariableOfNonMsgType"
            }
        }
    }

### Cause

This error occurs if the `source` attribute in the `<Copy>` element is set to a variable which is not of type [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#messagevariables).

Message type variables represent entire HTTP requests and responses. The built-in flow variables `request`, `response`, and `message` are of type message. To learn more about message variables, see the [Variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#messagevariables).

### Diagnosis

  1. Identify the Assign Message Policy where the error occurred and the name of the variable whose type is incorrect. You can find both of these items in the `faultstring` element of the error response. For example, in the following `faultstring`, the policy name is `GenerateGeocodingRequest` and the variable is `PostalCode`:
         
         "faultstring": "AssignMessage[GenerateGeocodingRequest]: value of variable PostalCode is not of type Message"
         

  2. In the failed Assign Message Policy XML, verify that the name of the variable set in the `<Copy>` element matches the variable name identified in the fault string (step #1 above). For example, the following policy sets a source attribute to a variable named `PostalCode`, which matches what's in the `faultstring`:
         
         <AssignMessage name="GenerateGeocodingRequest">
            <AssignTo createNew="true" type="request">GeocodingRequest</AssignTo>
            <AssignVariable>
               <Name>PostalCode</Name>
               <Ref>request.queryparam.postalcode</Ref>
            </AssignVariable>
            <AssignVariable>
               <Name>Country</Name>
               <Ref>request.queryparam.country</Ref>
            </AssignVariable>
            <Copy source="PostalCode">
               <QueryParams>
                  <QueryParam name="q" />
               </QueryParams>
            </Copy>
         </AssignMessage>
         

  3. Determine if this variable is of type message or not:

     1. Locate the code within the API Proxy bundle, where the variable was defined first.
     2. Once you figure out the policy in which the variable is defined and populated first, you need to determine the type of that variable as follows: 
        1. Check the value of the type attribute (if present).
        2. If the type attribute is not present, then the variable is considered to be a string.
     3. If the variable's type is non-message (such as a string), then that's the cause of the error. You can learn about common variables and their types in the [Variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

For example, look at the PostalCode variable in the above XML. It is assigned the value of the flow variable `request.queryparam.postalcode` in the `<AssignVariable>` element. This value is a string, because there is no type attribute present in the variable assignment.

Now, recall that the PostalCode variable is used in the `<Copy>` element of the Assign Message policy:
    
    <Copy source="PostalCode">
       <QueryParams>
          <QueryParam name="PostalCode" />
       </QueryParams>
    </Copy>
    

Because PostalCode is not of type message (it's a string in this example), you receive the error code:
    
    steps.assignmessage.VariableOfNonMsgType
    




### Resolution

Ensure that the `source` attribute in the `<Copy>` element in the failed Assign Message policy is set to a [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#messagevariables) type flow variable that exists.

To correct the policy, you can modify the `source` attribute in the `<Copy>` element to specify a variable that is of type message. For example, if the Assign Message policy is supposed to execute in the request flow, then you could use the message type variable `request` or any other custom variable of type message.
    
    
    <AssignMessage name="GenerateGeocodingRequest">
       <AssignTo createNew="true" type="request">GeocodingRequest</AssignTo>
       <AssignVariable>
          <Name>PostalCode</Name>
          <Ref>request.queryparam.postalcode</Ref>
       </AssignVariable>
       <AssignVariable>
          <Name>Country</Name>
          <Ref>request.queryparam.country</Ref>
       </AssignVariable>
       <Copy source="request">
          <QueryParams>
             <QueryParam name="PostalCode" />
          </QueryParams>
       </Copy>
    </AssignMessage>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
