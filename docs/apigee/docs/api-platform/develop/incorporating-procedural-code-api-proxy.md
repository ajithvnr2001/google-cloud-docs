---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/incorporating-procedural-code-api-proxy/
title: Incorporating procedural code \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:09.056304+00:00
---

# Incorporating procedural code  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/incorporating-procedural-code-api-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Incorporating procedural code Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

You can add code in procedural languages such as JavaScript, Java, and Python, then call out to that code from other parts of an API proxy. Support for procedural code is designed to make it easier for you to implement complex handling of flow variables, faults, and request and response bodies.

With procedural code, you can:

  * Create or manipulate complex body values, such as request and response values.
  * Rewrite URLs, such as to mask a target endpoint URL.
  * Add other logic not available with included policies.



## How it works

You use a policy specific to the language in order to make calls from a proxy flow to your included code. For each of the supported languages, Apigee includes a separate policy: [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy), [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy), and [PythonScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/python-script-policy).

The following describes, at a high level, one way this works. Be sure to see the policy references for more details.

  1. In a separate file, write the code you're going to use.
  2. In your code, put the result of the code's processing into an Apigee flow variable. 

You'll retrieve the variable value elsewhere in your API proxy. For more about flow variables, see [Managing proxy state with flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables).

  3. Add your file (or JAR) as a resource file to your API proxy. 

For more about resource files, see [Resource files](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files).

  4. Add the policy corresponding to the language you're using. 

Configure the policy to make a call to your code from the desired place in your API proxy's flow.

  5. Use a policy to retrieve the code's value from the flow variable.



## Limitations

The Apigee security model does not permit system calls such as network I/O, filesystem read/writes, current user info, process list, and CPU/memory utilization. Although some such calls may be functional, they are unsupported and liable to be actively disabled at any time. For forward compatibility, you should avoid making such calls in your code.

Other limitations may exist for each supported language, as described in the language's corresponding policy reference.

## Supported languages

### JavaScript

Support for JavaScript includes a full object model for handling variables and values specific to an API proxy. For more, see [JavaScript object model](https://docs.cloud.google.com/apigee/docs/api-platform/reference/javascript-object-model).

For policy reference information and examples, see [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy).

### Java

Use the [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) to make calls to Java code from your proxy's flow. The policy reference topic includes examples.

### Python

Use the [Python Script policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/python-script-policy) to call out to Python code.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
