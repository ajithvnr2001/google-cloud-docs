---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/structure-api-proxies/
title: Key points of API proxy development \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:19.809012+00:00
---

# Key points of API proxy development  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/structure-api-proxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Key points of API proxy development Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This topic lists some basic characteristics of API proxies, along with links to more information.

##  APIs are entry points for one application to use the capabilities of another. You implement API proxies to create APIs

In Apigee, you implement API proxies by configuring API proxy logic as a sequence of steps that execute in response to a request from client code. You expose an API proxy to clients by defining endpoints that include a URL with resource paths, an HTTP verb, body requirements, and so on.

Though it's called an API proxy, from the client code's perspective, _it's the API_.

For an overview of API proxies, see [Understanding APIs and API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies).

## You arrange the sequence of API proxy logic using flows

In any application, data flows through the application guided by condition logic. In Apigee, the path of processing is made up of flows. A flow is a sequence of stages (or "steps") that make up an API proxy's processing path. Flows are how Apigee provides places for you to apply logic and behavior at specific places from client to backend resource, then back to client.

For more on flows, see [Controlling how a proxy executes with flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows)

## You access state data through flow variables created by API proxies

An API proxy has access to variables that represent execution state. You can access these variables from the XML that configures your API proxies and policies. You can also access them when you're extending an API proxy with a procedural language, such as Java, JavaScript, or Python.

These variables are held by Apigee. Some exist by default, usually because they're common to what API proxies do (such as because they're part of an HTTP request). You can also create your own variables to satisfy a logic requirement.

For more about variables, see [Managing proxy state with flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables).

## You can have API proxies execute conditionally

Just as in most programming languages, in API proxies you can have code execute conditionally. Conditions are often based on API proxy state, which you can access through flow variables. For example, you can have a condition that checks for the user agent, then processes the request accordingly.

For more on conditional execution, see [Conditions with flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions).

## You implement most logic in an API proxy using policies

Most of the logic you add to an API proxy is packaged as policies. A policy is an Apigee component that encapsulates logic for a functional area, such as security or traffic management. You configure a policy with XML that sets properties for the underlying logic. You arrange policies in a sequence of "steps" within a flow, so that your API proxy executes the logic in the best order for your proxy's goals.

For more about policies, see [What's a policy?](https://docs.cloud.google.com/apigee/docs/api-platform/develop/policy-attachment-and-enforcement).

## You can include reusable sets of functionality

When your API proxy includes logic that will be used from multiple places in your code—such as other API proxies—you can collect that logic for calls from multiple places. For example, you can group security logic in a shared flow that other API proxies call, reducing duplication across API proxies.

For more on shared flows, see [Reusable shared flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows). For more on API proxy chaining, see [Chaining API proxies together](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/connecting-proxies-other-proxies).

## You can debug a proxy with the Debug tool

Apigee includes a [Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview) you can use to examine your API proxy's execution flow when debugging and testing. The tool visually presents each API proxy step that executes for a request. As in a debugger, at each step you can view the list of variable values that make up API proxy state.

For more about debugging with the Debug tool, see [Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview).

## You handle API proxy errors as faults

By configuring a fault handler, you can customize the error returned to an API client. Fault handlers give you control over error messages whether the error originates from your own code or from an included component (such as a policy).

For more, see [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
