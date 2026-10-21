---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy/
title: FlowCallout policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:05:14.419978+00:00
---

# FlowCallout policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  FlowCallout policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Use the FlowCallout policy to call out to a shared flow from either an API proxy or another shared flow.

In a shared flow, you create a sequence of steps that you can reuse at run time from multiple places. These steps are implemented as policies, as within an API proxy. The `FlowCallout` policy gives you a way to invoke the shared flow from API proxies and other shared flows. It works like a function call in a traditional programming language.

  * For example, imagine that you've built a shared flow with security features such as API key verification, OAuth token validation, and regular expression protection. This shared flow represents your convention for a way to check inbound requests. Using the `FlowCallout` policies, you can invoke that shared flow from multiple API proxies. 
  * You can call one shared flow from another by implementing a `FlowCallout` policy from within a shared flow. 



This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

**Note:** For more on shared flows, see [Reusable shared flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows). You can also call a shared flow from outside API proxy code to enforce request pre-processing or response post-processing for all API Proxies deployed in an environment. For more, see [Attaching a shared flow using a flow hook](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-hooks). 

## Samples

### Verify API key in shared flow

In this example a shared flow is used to perform common security-related tasks. Here the shared flow validates an API key. API proxies and other shared flows can use the `FlowCallout` policy to make calls into this shared flow.

The following shared flow definition includes a `Verify-API-Key` policy that executes when the shared flow is called from a `FlowCallout` policy in an API proxy.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <SharedFlow name="default">
        <Step>
            <Name>Verify-API-Key</Name>
        </Step>
    </SharedFlow>

The `VerifyAPIKey` policy within the preceding shared flow retrieves the key value and verifies it.
    
    
    <VerifyAPIKey async="false" continueOnError="false" enabled="true" name="Verify-API-Key">
        <DisplayName>Verify API Key</DisplayName>
        <APIKey ref="request.queryparam.apikey"/>
    </VerifyAPIKey>

The following `FlowCallout` policy, used in an API proxy, calls the preceding shared flow to verify the API key. The `verify-apikey-shared` shared flow bundle (not shown here) configures the shared flow in the way an APIProxy bundle configures a proxy.
    
    
    <FlowCallout async="false" continueOnError="false" enabled="true" name="Auth-Flow-Callout">
        <DisplayName>Auth Flow Callout</DisplayName>
        <SharedFlowBundle>verify-apikey-shared</SharedFlowBundle>
    </FlowCallout>

### Pass parameters to a shared flow

This example illustrates how to pass parameters from a `FlowCallout` policy to a shared flow. Here, a `FlowCallout` policy calls to a shared flow designed to perform common string handling functions. The shared flow includes JavaScript that concatenates its input, lower-cases its input, or both. The `FlowCallout` policy defines parameters that specify the string input, output, and what to do with the input.

  1. The `String-Handler` `FlowCallout` policy calls the shared flow, passing parameters specifying the variable to store the shared flow's output, what shared flow operation to use, and what input to use (here, a string literal, but it could also be a flow variable). The `Parameter` elements specify the names and values of variables to create runtime. The shared flow can retrieve these variables for use in its own code.
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <FlowCallout async="false" continueOnError="false" enabled="true" name="String-Handler">
           <DisplayName>String Handler</DisplayName>
           <Parameters>
             <Parameter name="input">Gladys Kravitz</Parameter>
             <Parameter name="operations">concatenate tolowercase</Parameter>
             <Parameter name="outputVariable">string.handler.output</Parameter>
           </Parameters>
           <SharedFlowBundle>StringHandler</SharedFlowBundle>
         </FlowCallout>

  2. The following `default` shared flow includes a `SharedStringFunctions` JavaScript policy that executes when the shared flow is called from a `FlowCallout` policy.
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <SharedFlow name="default">
           <Step>
             <Name>SharedStringFunctions</Name>
           </Step>
         </SharedFlow>

  3. In the shared flow, the following `SharedStringFunctions` JavaScript policy specifies the `SharedStringFunctions.js` JavaScript file with the code to execute.
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <Javascript async="false" continueOnError="false" enabled="true" timeLimit="200" name="SharedStringFunctions">
           <DisplayName>SharedStringFunctions</DisplayName> <Properties/>
           <ResourceURL>jsc://SharedStringFunctions.js</ResourceURL>
         </Javascript>

  4. The following JavaScript, `SharedStringFunctions.js`, executes from the `SharedStringFunctions` JavaScript policy. This script retrieves values from variables created from `FlowCallout` policy `Parameter` elements.
         
         // Input value from the calling API proxy.
         var handledString = context.getVariable("input");
         // Variable to use for output from this script.
         var outputVariable = context.getVariable("outputVariable");
         // A space-separated list of things to do to the input string.
         // Convert to lower case to handle unintentional capitals in configuration.
         var operation = context.getVariable("operations").toLowerCase();
         
         // If "lowercase" was given as an operation, convert the input to lowercase.
         if (operation.includes("tolowercase")) {
             handledString = handledString.toLowerCase();
         }
         
         // If "concatenate" was given as an operation, concatenate the input.
         if (operation.includes("concatenate")) {
             handledString = handledString.replace(/\s+/g, '');
         }
         // Assign the resulting string to the output variable specified by
         // the calling API proxy.
         context.setVariable(outputVariable, handledString);

  5. Execution flows back from the JavaScript policy, to the shared flow, then to the `FlowCallout` policy in the originating API proxy.



## Element reference

Following are elements and attributes you can configure on this policy:
    
    
    <FlowCallout async="false" continueOnError="false" enabled="true" name="Flow-Callout-1">
        <DisplayName>Custom label used in UI</DisplayName>
        <SharedFlowBundle>thereferencedsharedflowbundle</SharedFlowBundle>
    </FlowCallout>

## <FlowCallout> attributes
    
    
    <FlowCallout async="false" continueOnError="false" enabled="true" name="Flow-Callout-1">

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
  
## <SharedFlowBundle> element

Specifies the name of the shared flow to call. This element's value should be the same as the value of the target `<SharedFlowBundle>` element's name attribute.
    
    
    <SharedFlowBundle/>

In the simplest example, you give the name of the shared flow being called as a value for this element. That is, this element's value must be the same as the shared flow's `name` attribute value.
    
    
    <SharedFlowBundle>Shared-Flow-Name</SharedFlowBundle>

Default | N/A  
---|---  
Presence | Required  
Type | N/A  
  
### Attributes

None.

## <Parameter> element

Specifies a parameter and value (or value source) to pass as a variable into the shared flow called by this policy.

By using a parameter, you can specify a value (or a variable containing a value) that should be passed to the shared flow called by the policy. This is conceptually similar to specifying a parameter in a function call. As with a function parameter, a `FlowCallout` parameter's value can vary based on the context of the shared flow call.

`FlowCallout` parameters are visible only during the shared flow's execution.

### Syntax

You can use this element with any one of the following syntax forms. Note that where you use a literal value, the format of the value you specify will depend on the code that consumes it.
    
    
    <!-- A literal value in an attribute. -->
    <Parameter name="parameter-name" value='parameter-value' />
    <!-- A reference to a variable in an attribute. -->
    <Parameter name="parameter-name" ref='source-variable-name' />
    <!-- A literal value in the element content. -->
    <Parameter name="parameter-name">parameter-value</Parameter>
    <!-- A reference to an attribute in the element content. -->
    <Parameter name="parameter-name">{source-variable-name}</Parameter>

### Example

This `String-Handler` `FlowCallout` policy passing parameters that specify where to store the shared flow's output and what input to use. The `Parameter` elements specify the names and values of variables to create runtime. The shared flow can retrieve these variables for use in its own code.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <FlowCallout async="false" continueOnError="false" enabled="true" name="String-Handler">
      <DisplayName>String Handler</DisplayName>
      <Parameters>
        <Parameter name="input">Gladys Kravitz</Parameter>
        <Parameter name="outputVariable">string.handler.output</Parameter>
      </Parameters>
      <SharedFlowBundle>StringHandler</SharedFlowBundle>
    </FlowCallout>

Default | N/A  
---|---  
Presence | Required  
Type | N/A  
  
### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
`name` | The name of the runtime variable to create with this parameter. | None | Required | String  
`ref` |  The variable that contains the value to use at runtime. Omit this attribute if you're specifying a literal value to use. | None | Optional | String  
`value` | The value to use in the runtime variable created with this parameter. Omit this attribute if you're specifying the name of a variable that should be the value source. | None | Optional | String  
  
## <Parameters> element

Specifies the set of <Parameter> elements to pass as variables into the shared flow called by this policy.

### Syntax
    
    
    <Parameters>
      <Parameter name="parameter-name" value='parameter-value' />
    </Parameters>

Default | N/A  
---|---  
Presence | Optional  
Type | N/A  
  
### Attributes

None.

## Schemas

**Sample:** See our [GitHub repository](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) samples for the most recent schemas.

## Flow variables

Flow variables enable dynamic behavior of policies and flows at runtime, based on HTTP headers, message content, or flow context. For more information about Flow variables, see [Variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

Variable | Description  
---|---  
`apigee.edge.sharedflow.name` |  **Scope** : During the shared flow execution  
**Type** : String  
**Permission** : Read The value of the shared flow's name attribute.  
`apigee.edge.flowhook.name` |  **Scope** : During execution of the shared flow attached to the flow hook.  
**Type** : String  
**Permission** : Read The name of the flow hook.  
  
## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [ What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information. 

Use [API Monitoring](https://docs.cloud.google.com/apigee/docs/api-monitoring) to investigate fault codes and diagnose issues faster.

Fault code | HTTP status | Cause | Fix  
---|---|---|---  
`flow.SharedFlowNotFound` | `500` | Either the shared flow does not exist, or the shared flow exists but is not deployed. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/flowcallout-runtime-errors)  
  
### Deployment errors

N/A

## Related topics

  * Creating shared flows: [ Reusable shared flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows)
  * Executing shared flows across multiple proxies: [ Attaching a shared flow using a flow hook](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-hooks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
