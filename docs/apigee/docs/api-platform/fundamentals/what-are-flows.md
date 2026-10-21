---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows/
title: Controlling API proxies with flows \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:12.604651+00:00
---

# Controlling API proxies with flows  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Controlling API proxies with flows Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Flows are the basic building blocks of API proxies. Flows enable you to program the behavior of an API by letting you configure the sequence in which policies and code are executed by an API proxy.

Flows are sequential stages along the API request processing path. When you add proxy logic, such as to verify an API key, you add the logic as a step in the sequence specified by a flow. When you define a condition to specify whether and when logic executes, you add the condition to a flow.

The following flow configuration example defines a flow in which the [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) executes _if_ the incoming request path ends with `/` and the request's HTTP verb is `GET`.
    
    
    <Flow name="Get Food Carts">
        <Description>Get Food Carts</Description>
        <Request>
            <Step>
                <Name>Verify-API-Key</Name>
            </Step>
        </Request>
        <Condition>(proxy.pathsuffix MatchesPath "/") and (request.verb = "GET")</Condition>
    </Flow>

The `Verify-API-Key` value in the flow's `<Name>` element serves to include a policy configured elsewhere in the proxy with XML such as the following:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <VerifyAPIKey async="false" continueOnError="false" enabled="true" name="Verify-API-Key">
        <DisplayName>Verify API Key</DisplayName>
        <Properties/>
        <APIKey ref="request.header.x-api-key"/>
    </VerifyAPIKey>

## Designing flow execution sequence

You structure flows so that you can have logic execute in the right sequence along the processing path.

**Note:** See [Build your first API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/get-started) for a simple tutorial on creating a flow. For specifics on configuring flows, see [Configuring flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-configurations).

When deciding where to add logic, you'll first choose whether to add it to a proxy endpoint or target endpoint. An API proxy divides its code between code that interacts with the proxy's client (proxy endpoint) and optional code that interacts with the proxy's backend target, if any (target endpoint).

Both endpoints contain flows, as described here:

Endpoint type | Description | Flows supported  
---|---|---  
ProxyEndpoint | Contains the API proxy flows closest to the client. Provides places for logic to act first on the request from the client, then last on the response to the client. | PreFlow, conditional flows, PostFlow, PostClientFlow  
TargetEndpoint | Contains the API proxy flows closest to the backend resource. Provides places for logic to prepare a request for, then handle the response from, a backend resource.  | PreFlow, conditional flows, PostFlow  
  
You configure flow with XML that specifies what should happen and in what order. The following illustration shows how flows are ordered sequentially within a proxy endpoint and target endpoint:

![Request from HTTP client passing through Proxy Endpoint to the TargetEndpoint on the
  backend to reach the HTTP service. Each request and response panel shows the preflow, conditional
  flows, and post flow. In addition, examples of the proxy endpoint and target endpoint are
  provided.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ProxyToBackendWithFlows_v3.png)

The proxy endpoint and target endpoint each contain flows that you can arrange in the following sequence:

Position | Flow type | Description  
---|---|---  
1 | PreFlow |  Useful when you need to make sure that certain code executes before anything else happens. If the PreFlow is in a target endpoint, it executes after the proxy endpoint's PostFlow.  
2 | Conditional Flow |  The place for conditional logic. Executes after the PreFlow and before the PostFlow. Only one conditional flow is executed per segment--the first flow whose condition evaluates to true. That means you can have one conditional flow executed as part of each of the:

  * ProxyEndpoint's request pipeline
  * TargetEndpoint's request pipeline
  * ProxyEndpoint's response pipeline
  * TargetEndpoint's response pipeline

  
3 | PostFlow |  A good place to need to log data, send a notification that something happened while processing the request, and so on. Executes after conditional flows and PreFlow. If the PostFlow is in a proxy endpoint, and there's a target endpoint, the proxy endpoint PostFlow executes before the target endpoint PreFlow.  
4 | PostClientFlow (proxy flow only) | A flow for logging messages after a response is returned to the client.  
  
### Having code execute first with a PreFlow

A PreFlow is useful when you need to make sure that certain code executes before anything else happens.

In a proxy endpoint, a PreFlow is a great place for code that authenticates a client and limits traffic from clients. In a target endpoint, where it begins preparing to send a request to a backend target, a PreFlow is good for first steps in preparing to send the request.

For example, you usually don't want to service a client that has exceeded its quota. To support these requirements, you put security and quota policies in the PreFlow segment. That way, you don't need to worry about a condition failing to evaluate in a later conditional flow. The policies in this flow will always execute before any other processing takes place.

In the following example, SpikeArrest and Quota policies execute before processing passes to conditional flows.
    
    
    <PreFlow name="MyPreFlow">
        <Request>
            <Step>
                <Name>Spike-Arrest</Name>
            </Step>
            <Step>
                <Name>Quota</Name>
            </Step>
        </Request>
        <Response/>
    </PreFlow>

### Having code execute conditionally with a conditional flow

Between a PreFlow and a PostFlow, you can have flows that execute conditionally. This gives you an opportunity to configure multiple sequences of logic, but have only one execute based on your proxy's state. A conditional flow is optional if you can execute all logic in PreFlow or PostFlow and no conditions are required (in other words, only one path through the endpoint is supported).

Each flow specifies a condition that tests for different state values. This effectively branches execution based on conditions. For example, you might want to convert XML to JSON only when the requesting app is running on a mobile device.

**Note:** In a conditional flow, the condition is evaluated in both the request and response. You cannot have separate conditions for request and response. Only one conditional flow is executed--the first flow whose condition evaluates to true.

Here, quota constraints are enforced only if the request is a `GET` request with a URI pattern of `/issue/**` (`/issue/` with anything in the URI after the last forward slash).
    
    
    <Flow name="MyFlow">
        <Description/>
        <Request>
            <Step>
                <Name>Quota</Name>
            </Step>
        </Request>
        <Response/>
        **< Condition>(proxy.pathsuffix MatchesPath "/issue/**") and (request.verb = "GET")</Condition>**
    </Flow>

You use flow variables to specify conditions. For more about using variables in conditions, see [Conditions with flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions).

For examples of using pattern matching in conditions, see [Pattern matching](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions#patternmatching).

### Having code execute after core logic with a PostFlow

A PostFlow is a great place to perform actions after your endpoint's core logic, and before endpoint processing finishes. A PostFlow executes after conditional flows and PreFlow.

A PostFlow is a good place to log some data, send a notification that something happened, transform the response message format, and so on.

In the following example, an [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) called SetResponseHeaders sets headers of the response message before Apigee sends the response back to the client.
    
    
    <PostFlow>
        <Response>
            <Step>
                <Name>SetResponseHeaders</Name>
            </Step>
        </Response>
     </PostFlow>

###  Having code execute after the client receives your proxy's response with a PostClientFlow

A PostClientFlow can include the following policies only. No other policies can be used in a PostClientFlow:

  * [FlowCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy)*
  * [MessageLogging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy)
  * [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy)



* The FlowCallout policy can only call shared flows which themselves meet the criteria for being in the PostClientFlow (ie, only contain compatible policies).

If you include one, a PostClientFlow would be the last flow to execute, executing after a response is sent to the client.

A PostClientFlow is good for final logging. Also, you can log the start and end timestamps for the response message.

Here's an example of a PostClientFlow with a MessageLogging policy attached.
    
    
      <ProxyEndpoint name="endpoint1">
        ...
        <PostFlow name="PostFlow">
            <Request/>
            <Response/>
        </PostFlow>
        <PostClientFlow>
            <Response>
                <Step>
                    <Name>Message-Logging-1</Name>
                </Step>
            </Response>
        </PostClientFlow>
        ...
      </ProxyEndpoint>
    

For more information, see [API proxy configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference).

## Adding logic to flows

When you add logic to your proxy, you do it by adding policies to your proxy's flows. Just as flows execute in a sequence (PreFlow then Flow then PostFlow, as described in this topic), the contents of a flow execute in a sequence.

**Note:** For more about policies, including how to add them with the console and in code, see [What's a policy?](https://docs.cloud.google.com/apigee/docs/api-platform/develop/policy-attachment-and-enforcement) For details about attaching policies to flows, see [Conditional flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-configurations).

The following example flow configuration references three policies (configured elsewhere in their own XML files). The policy referenced by `Verify-API-Key` executes before the policy referenced by `Assign-Message`; both are followed by the policy represented by `Quota`.
    
    
    <Flow name="Get Food Cart Menus">
      <Description>Get Food Cart Menus</Description>
      <Request>
        <Step>
          <Name>Verify-API-Key</Name>
        </Step>
        <Step>
          <Name>Assign-Message</Name>
        </Step>
        <Step>
          <Name>Quota</Name>
        </Step>
      </Request>
      <Condition>(proxy.pathsuffix MatchesPath "/") and (request.verb = "GET")</Condition>
    </Flow>

**Note:** In the above code the path condition, `(proxy.pathsuffix MatchesPath "/")`, is always true because `"/"` is always matched. So you could just remove it from the **Condition** element and just use the verb condition: 
    
    
        <Condition>request.verb = "GET"</Condition>

## Debugging flows

The [Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview) provides a graphical way to see how the logic in your API proxy executes following a request. The tool illustrates processing between request and response. It doesn't specifically illustrate the separation between PreFlow, conditional flows, and PostFlow.

For more about debugging proxies, see [Using the Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace).

## Handling errors in flows

You can raise faults from various places in an API proxy, including from flows.

The following example is the response stanza from a PreFlow in a target endpoint—in other words, it's the code that executes immediately upon receiving the response from a backend target. In the example, a fault is raised if the response from the target isn't `200` (success).
    
    
    <PreFlow name="PreFlow">
        <Response>
            <Step>
                <Name>RaiseFault</Name>
                <Condition>(response.status.code GreaterThan "200")</Condition>
            </Step>
        </Response>
    </PreFlow>

For more about error handling, see [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
