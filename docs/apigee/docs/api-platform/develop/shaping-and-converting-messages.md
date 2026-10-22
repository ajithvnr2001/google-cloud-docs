---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/shaping-and-converting-messages/
title: Shaping, accessing, and converting messages \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:43.259013+00:00
---

# Shaping, accessing, and converting messages  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/shaping-and-converting-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Shaping, accessing, and converting messages Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

You can use policies included with Apigee to manipulate the messages flowing through your API proxies. With policies, you can:

  * Convert messages between formats, such as from XML to JSON.
  * Set variable values from message content, and create messages from variable values.
  * Use procedural code, such as JavaScript, Java, and Python, to handle messages and data in more complex ways.



In general, when using these policies, you specify input and output as a flow variables. At run time, Apigee retrieves the input value from a source variable and writes the output value to an output variable.

This topic introduces these capabilities. For more complete and technical information, see the policy references for each.

## Simple handling for XML and JSON

Apigee includes policies that make it easier to convert between XML and JSON, and to transform XML with XSL.

### Converting JSON to XML

The [JSONtoXML policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-xml-policy) takes your JSON input and converts it to XML.

In the following policy example, the policy takes a JSON-formatted message from the `request` variable, then replaces the variable value with an XML-formatted message. The input is specified in the `<Source>` element, while the output is specified in the `<OutputVariable>` element.
    
    
    <JSONToXML name="jsontoxml">
         <Source>request</Source>                     _--- > INPUT_
         <OutputVariable>request</OutputVariable>          _OUTPUT --- >_
    </JSONToXML>

### Converting XML to JSON

The [XMLtoJSON policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy) converts XML input message into JSON.

In the following policy example, the policy takes an XML-formatted message from the `response` variable, then replaces the variable value with a JSON-formatted message. The input is specified in the `<Source>` element, while the output is specified in the `<OutputVariable>` element.
    
    
    <XMLToJSON name="ConvertToJSON">
       <Source>response</Source>                     _--- > INPUT_
       <OutputVariable>response</OutputVariable>          _OUTPUT --- >_
    </XMLToJSON>

### Transforming XML with XSL

You can use the [XSLTransform policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xsl-transform-policy) to transform messages using XSL. For example, after converting a JSON payload to XML, you can use the XSL Transform policy with a style sheet to perform the transformation you need.

In the following policy example, the policy takes an XML-formatted message from the `response` variable, then replaces the variable value with a message formatted by `my_transform.xsl`. The input is specified in the `<Source>` element, while the output is specified in the `<OutputVariable>` element.
    
    
    <XSL name="TransformXML">
      <Source>response</Source>                        _--- > INPUT_
      <ResourceURL>xsl://my_transform.xsl</ResourceURL>       _--TRANSFORMER--_
      <OutputVariable>response</OutputVariable>                            _OUTPUT --- >_
    </XSL>

## Handling variable data

Data handling within a proxy often involves simply working with state data as flow variable values. You can often do this by using a policy that gets or sets variable values. For example, you might want to shape variable values into a message, or extract the contents of a message to set variable values.

Be sure to see references for the following two policies:

  * [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) to create messages from variable values.
  * [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy) to assign variables from message content.



## Creating more complex transformations

For data handling whose complexity is outside the capability of included policies, you can use procedural languages such as JavaScript, Java, or Python.

Generally, this involves writing code in one of these languages, then invoking the code from a policy specific to the language. For more about this, see [Incorporating procedural code](https://docs.cloud.google.com/apigee/docs/api-platform/develop/incorporating-procedural-code-api-proxy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
