---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors/
title: What you need to know about policy errors \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:12.406964+00:00
---

# What you need to know about policy errors  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  What you need to know about policy errors Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This topic describes the structure of policy errors and the kinds of flow variables that are set when a policy error occurs. This information is essential if you're designing and implementing fault handling for your proxies.

This topic assumes you have a general understanding of how fault handling works in Apigee, and that you know what fault rules are. If you need a review, see [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling). The information here will also help you navigate and use the [Policy error reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/error-code-reference).

## About the default policy error response

When a policy throws an error, Apigee immediately enters the error flow and generates an error message. This system-generated message is a JSON object that includes two bits of information: an `errorcode` and a `faultstring`.

**Note:** It's helpful to know that in the parts of an error as shown below are available as flow variables. You can restructure and customize error messages through these variables. The variable `fault.name` is the value of the `errorcode` attribute and `error.message` is the value of the `faultstring` attribute. These variables are discussed in more detail in the following sections of this topic. 

For example:
    
    
    {
       "fault":{
          "detail":{
             "errorcode":"steps.extractvariables.SourceMessageNotAvailable"
          },
          "faultstring":"mymessage message is not available for ExtractVariable: ParseJsonResponse"
       }
    }

Let's quickly deconstruct this error message:

The `errorcode` consists of a `prefix` and an `error name`, as follows: `[prefix].[error_name]`. In the above example "`steps.extractvariables` is the prefix and `SourceMessageNotAvailable` is the error name. The prefix tells you what kind of policy generated the error. In the above example, you can tell that an [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy) generated the error and the error name is `SourceMessageNotAvailable`.

The `faultstring` contains a description of the error. The fault string typically includes clues to help you find the specific problem that caused the error, such as the name of the policy, the name of an unresolved variable, or whatever contributed to the error. For example, in the above error message, `mymessage` happens to be the name of an unresolved message variable referenced in the policy and `ParseJsonResponse` is the name of the policy that triggered the error.

**Note:** In the [Policy error reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/error-code-reference), we use a consistent convention to document policy fault strings. We indicate where place variables occur with a `[]` notation. Here's an example of how we'd document the above error's fault string: 
    
    
    VAR_NAME message is not available for ExtractVariable: POLICY_NAME

## Variables specific to policy errors

When a policy error is triggered, certain error-specific flow variables are populated. These variables are extremely useful in fault handling. As explained in [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling), it's a common practice to trap the system-generated policy errors and perform a subsequent action such as to create a custom error response. For example, for security reasons, you might want to prevent clients from seeing the actual errors and status codes that Apigee returns.

### The `fault.name` variable

When a policy throws an error, it sets the flow variable `fault.name` to the `error_name` part of the errorcode (as described in the previous section). It's very common to evaluate this variable to conditionally execute fault rules. 

Here's an example fault rule that tests for the value of `fault.name`:
    
    
    <faultrule name="VariableOfNonMsgType"></faultrule><FaultRule name="Source Message Not Available Fault">
        <Step>
            <Name>AM-CustomErrorMessage</Name>
            <Condition>(fault.name Matches "SourceMessageNotAvailable") </Condition>
        </Step>
    </FaultRule>

The thing to remember is that when a policy triggers an error, the `fault.name` variable is always set to the error name.

**Note:** When you're developing your fault handling code, just look in the [Policy error reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/error-code-reference) to learn what the error name is for every policy error. It's also a common practice to use [Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview) to examine error responses and the variables that are set.

### The `[prefix].[policy_name].failed` variable

Besides `fault.name`, another variable that developers commonly check is the `[prefix].[policy_name].failed` flag, which is set to either true or false when a policy executes. In fault rules, you'll want to check to see when it's **true** — that is, to check if an error occurred. Here's how to construct a conditional that checks the `[prefix].[policy_name].failed` flag. To correctly check this variable, you need to know two things:

  * The _name_ of the policy you are checking. This is the value of the policy's name attribute, not the display name. This attribute is always included in the policy definition's XML.
  * A _prefix_ that is specific to the type of policy you are checking. (We'll explain how to find the prefix below.)



To illustrate, here's another fault rule example. Notice in the outer condition how the `[prefix].[policy_name].failed` variable name is formed. In this case the prefix is `extractvariables` and the policy name is `ParseJsonResponse`. In this case, the fault rule will only execute if this variable is true. And, here's a tip: because fault rules can contain multiple steps, this pattern is a nice way to organize fault rules into blocks.
    
    
    <faultrule name="VariableOfNonMsgType"></faultrule><FaultRule name="Extract Variable Faults">
        <Step>
            <Name>AM-CustomErrorMessage</Name>
            <Condition>(fault.name Matches "SourceMessageNotAvailable") </Condition>
        </Step>
        <Condition>(extractvariables.ParseJsonResponse.failed = true) </Condition>
    </FaultRule>

**Note:** How do you know what the fault variable's prefix is? You can't necessarily guess it from the contents of the fault string or error code. You have to look it up in the [Policy error reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/error-code-reference) or you can use trace to inspect the flow variables that are created when an error occurs. For example, for the Extract Variables policy, the `[prefix].[policy_name].failed` prefix is `extractvariables`, and that's pretty straightforward. But for the Access Control policy, the prefix is `acl`. So, the point is, you have to check.

### **About the`error` and `message` variables**

The `error` variable is only available in the error flow of a proxy. You can get useful information from the `error` variable, such as the error message, status code, and so on. The formatting pattern for the error variable is the following:
    
    
    error.ERROR_COMPONENT = VALUE

For example:
    
    
    error.message = "request message is not available for ExtractVariable:
      ParseJsonResponse"

and
    
    
    error.status.code = "500"

**Tip:** You can also use this variable to set response headers. This can be extremely useful because in the error flow, the response object is not available. 

The `message` variable is also available in the error flow and can be used for similar purposes as the `error` variable. The message variable is special because it is contextual. In a request flow, it behaves like a request variable, and in a response flow, it can be used to get/set response values.

Refer to [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference) for information on all of the Apigee variables, including `error` and `message`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
