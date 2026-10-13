---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/message-variables/
title: Message flow variable \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:14.909368+00:00
---

# Message flow variable  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/message-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Message flow variable Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Access to the [`message`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) flow variable and its properties depends on the point within the API Proxy Flow in which it is accessed. It is available in all contexts, whereas some objects, such as [`request`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#request) or [`response`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#response) are not.

## Use cases

The principal use case for the [`message`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) flow variable is when your proxy enters the error flow: the [`request`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#request) and [`response`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#response) flow variables are out of scope.

For example, in the error flow, the `response` object is not available. You will not be able to set response headers on the `response` object with the [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy) if you are in the error flow. Instead, you can use one of the following:

  * [`error`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#error)
  * [`message`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message)



Both of these objects are available in the error flow, and can be used to set response headers from within a JavaScript policy or be accessed in other policies that can use flow variables.

You can use the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) to assign values, such as headers, to the **response** object. AssignMessage automatically handles the switch in context from request/response flow to error flow.

Another use case for the [`message`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) variable is to log response data in the PostClientFlow with the [MessageLogging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy). If you use the `message` object, you can seamlessly log response information following both success and error conditions in the proxy.

## Examples

In an error flow, you can set a response header from a [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy) using either [`error`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#error) or [`message`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message). For example:
    
    
    context.setVariable('error.header.FOO-1', 'error_header');

**OR**
    
    
    context.setVariable('message.header.FOO-2', 'message_header');

The following expression, however, will _not_ work:
    
    
    context.setVariable('response.header.FOO-3', 'response_header');

In this case, the [`response`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#response) variable is out of scope in the error flow. (Note that, in a trace, this is visually indicated by variables shown with an equals sign with a slash through it.)

To set response headers for both success and error flows in a single policy, you can use [`message`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) inside a [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy). For example:
    
    
    <faultrules>
      <faultrule name="invalid_key_rule">
        <step>
          <name>SetResponseHeaders</name>
        </step>
        <condition>(fault.name = "InvalidApiKey")</condition>
      </faultrule>
    </faultrules>

In the policy, code like the following sets the error/response header in any flow context:
    
    
    context.setVariable('message.header.FOO-1', 'the header value');

You can reuse this same policy on the normal ProxyResponse flow and it will succeed because `message` is available from all contexts.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
