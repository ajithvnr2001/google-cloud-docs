---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-xml-policy/
title: JSONtoXML policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:04.477793+00:00
---

# JSONtoXML policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-xml-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  JSONtoXML policy Stay organized with collections  Save and categorize content based on your preferences. 

[Standard policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The JSONtoXML policy converts messages from the JavaScript Object Notation (JSON) format to extensible markup language (XML), giving you several options for controlling how messages are converted.

The policy is particularly useful if you want to transform messages using XSL. After converting a JSON payload to XML, use the XSL Transform policy with a custom style sheet to perform the transformation you need.

**Note:** The HTTP Content-type header of the source message must be set to `application/json`, otherwise the policy is not enforced, meaning it is skipped during processing.

Assuming that the intent is to convert a JSON-formatted request into an XML-formatted request, the policy would be attached to a request Flow (for example, Request / ProxyEndpoint / PostFlow).

This policy is a _Standard policy_ and can be deployed to any environment type. For information on policy types and availability with each environment type, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

### Samples

For a detailed discussion, see [Converting between XML and JSON with Apigee: what you need to know](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/Converting-between-XML-and-JSON-with-Apigee-what-you-need-to/ta-p/76127). 

### Converting a request
    
    
    <JSONToXML name="jsontoxml">
        <Source>request</Source>
        <OutputVariable>request</OutputVariable>
    </JSONToXML>

This configuration takes JSON-formatted request message as the source, and then creates an XML-formatted message that is populated in the `request` OutputVariable. Apigee automatically uses the content of this variable as the message for next processing step.

* * *

## Element reference

Following are elements and attributes you can configure on this policy.
    
    
    <JSONToXML async="false" continueOnError="false" enabled="true" name="JSON-to-XML-1">
        <DisplayName>JSON to XML 1</DisplayName>
        <Source>request</Source>
        <OutputVariable>request</OutputVariable>
        <Options>
            <OmitXmlDeclaration>false</OmitXmlDeclaration>
            <DefaultNamespaceNodeName>$default</DefaultNamespaceNodeName>
            <NamespaceSeparator>:</NamespaceSeparator>
            <AttributeBlockName>#attrs</AttributeBlockName>
            <AttributePrefix>@</AttributePrefix>
            <ObjectRootElementName>Root</ObjectRootElementName>
            <ArrayRootElementName>Array</ArrayRootElementName>
            <ArrayItemElementName>Item</ArrayItemElementName>
            <Indent>false</Indent>
            <TextNodeName>#text</TextNodeName>
            <NullValue>I_AM_NULL</NullValue>
            <InvalidCharsReplacement>_</InvalidCharsReplacement>
        </Options>
    </JSONToXML>

## <JSONToXML> attributes

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
  
## <Source> element

The variable, request or response, that contains the JSON message that you want to convert to XML.

**Note:** The HTTP Content-type header of the source message must be set to `application/json`, otherwise the policy is not enforced, meaning it is skipped during processing.

If `<Source>` is not defined, then it is treated as message (which resolves to request when the policy is attached to a request flow, or response when the policy is attached to a response flow).

If the source variable cannot be resolved, or resolves to a non-message type, the policy throws an error.
    
    
    <Source>request</Source>

**Default** | request or response, determined by where the policy is added to the API proxy flow  
---|---  
**Presence** | Optional  
**Type** | message  
  
## <OutputVariable> element

Stores the output of the JSON to XML format conversion. This is usually the same value as the source, that is, usually a JSON request is converted to an XML request.

The payload of the JSON message is parsed and converted into XML, and the HTTP Content-type header of the XML-formatted message is set to `text/xml;charset=UTF-8`.

If `OutputVariable` is not specified, the `source` is treated as `OutputVariable`. For example, if the `source` is `request`, then `OutputVariable` defaults to `request`.
    
    
    <OutputVariable>request</OutputVariable>

**Default** | request or response, determined by where the policy is added to the API proxy flow  
---|---  
**Presence** | This element is mandatory when the variable defined in the `<Source>` element is of type string.  
**Type** | message  
  
## <Options>/<OmitXmlDeclaration>

Specifies to omit the XML declaration line from the output. An XML declaration line can optionally appear at the top of an XML document. A typical example looks like this: 
    
    
    <?xml version="1.0" encoding="UTF-8"?>

In some cases it's important to avoid including such a line in the output of this policy. One good example is if you plan to embed the output of this policy as a fragment into a larger XML document. Because the declaration must appear only once in a document, and only at the top of the document, it would be important in that case to suppress the XML declaration line in the XML fragment.

The default value for this option is `false`, which means the policy will include the XML declaration line in the output. The following setting will configure the policy to omit the XML Declaration:
    
    
    <OmitXmlDeclaration>true</OmitXmlDeclaration>

There is no way to shape or affect the contents of the XML declaration line via the configuration of this policy. The policy always generates UTF-8 encoded text, and always uses XML version 1.0, and the declaration line, if it is included, will reflect that.

## <Options>/<NamespaceBlockName>  
<Options>/<DefaultNamespaceNodeName>  
<Options>/<NamespaceSeparator> elements

JSON has no support for namespaces, while XML documents often require them. `NamespaceBlockName` enables you to define a JSON property that serves as the source of a namespace definition in the XML that is produced by the policy. (This means that the source JSON must provide a property that can be mapped into a namespace that is expected by application that consumes the resulting XML.)

For example, the following settings:
    
    
    <NamespaceBlockName>#namespaces</NamespaceBlockName>
    <DefaultNamespaceNodeName>$default</DefaultNamespaceNodeName>
    <NamespaceSeparator>:</NamespaceSeparator>

indicates that a property called `#namespaces` exists in the source JSON that contains at least one namespace designated as the default. For example:
    
    
    {
       "population": {
           "#namespaces": {
               "$default": "http://www.w3.org/1999/people",
               "exp": "http://www.w3.org/1999/explorers"
           },
           "person": "John Smith",
           "exp:person": "Pedro Cabral"
       }
    }

converts to:
    
    
    <population xmlns="http://www.w3.org/1999/people" xmlns:exp="http://www.w3.org/1999/explorers">
      <person>John Smith</person>
      <exp:person>Pedro Cabral</exp:person>
    </population>

## <Options>/<ObjectRootElementName>

<ObjectRootElementName> specifies the root element name when you convert from JSON, which does not have a named root element, to XML.

For example, if the JSON appears as:
    
    
    {
      "abc": "123",
      "efg": "234"
    }

And you set <ObjectRootElementName> as:
    
    
    <ObjectRootElementName>Root</ObjectRootElementName>

The resultant XML appears as:
    
    
    <Root>
       <abc>123</abc>
       <efg>234</efg>
    </Root>

## <Options>/<AttributeBlockName>  
<Options>/<AttributePrefix> elements

`<AttributeBlockName>` enables you to specify when JSON elements are converted into XML attributes (rather than XML elements).

For example, the following setting converts properties inside an object named `#attrs` into XML attributes:
    
    
    <AttributeBlockName>#attrs</AttributeBlockName>

The following JSON object:
    
    
    {
        "person" : {
            "#attrs" : {
                "firstName" : "John",
                "lastName" : "Smith"
            },
            "occupation" : "explorer",
        }
    }

is converted to the following XML structure:
    
    
    <person firstName="John" lastName="Smith">
      <occupation>explorer</occupation>
    </person>

`<AttributePrefix>` converts the property starting with the specified prefix into XML attributes. Where the attribute prefix is set to `@`, for example:
    
    
    <AttributePrefix>@</AttributePrefix>

Converts the following JSON object:
    
    
    {
    "person" : {
       "@firstName" : "John",
       "@lastName" : "Smith"
       "occupation" : "explorer",
    
     }
    }

to the following XML structure:
    
    
    <person firstName="John" lastName="Smith">
      <occupation>explorer</occupation>
    </person>

## <Options>/<ArrayRootElementName>  
<Options>/<ArrayItemElementName> element

Converts a JSON array into a list of XML elements with specified parent and child element names.

For example, the following settings:
    
    
    <ArrayRootElementName>Array</ArrayRootElementName>
    <ArrayItemElementName>Item</ArrayItemElementName>

converts the following JSON array:
    
    
    [
    "John Cabot",
    {
     "explorer": "Pedro Cabral"
    },
    "John Smith"
    ]

into the following XML structure:
    
    
    <Array>
      <Item>John Cabot</Item>
      <Item>
        <explorer>Pedro Cabral</explorer>
      </Item>
      <Item>John Smith</Item>
    </Array>

## <Options>/<Indent>

Specifies to indent the XML output. The default value is `false` meaning do not indent. 

For example, the following setting configures the policy to indent the output:
    
    
    <Indent>true</Indent>

If the JSON input is in the form:
    
    
    {"n": [1, 2, 3] }

Then the output without intdenting is:
    
    
    <Array><n>1</n><n>2</n><n>3</n></Array>

With indenting enabled, the output is:
    
    
      <Array>
        <n>1</n>
        <n>2</n>
        <n>3</n>
      </Array>

## <Options>/<TextNodeName> element

Converts a JSON property into an XML text node with the specified name. For example, the following setting:
    
    
    <TextNodeName>age</TextNodeName>

converts this JSON:
    
    
    {
        "person": {
            "firstName": "John",
            "lastName": "Smith",
            "age": 25
        }
    }

to this XML structure:
    
    
    <person>
      <firstName>John</firstName>25<lastName>Smith</lastName>
    </person>

If `TextNodeName` is not specified, the XML is generated, using the default setting for a text node:
    
    
    <person>
      <firstName>John</firstName>
      <age>25</age>
      <lastName>Smith</lastName>
    </person>

## <Options>/<NullValue> element

Indicates a null value. By default the value is `NULL`.

For example the following setting:
    
    
    <NullValue>I_AM_NULL</NullValue>

Converts the following JSON object: 
    
    
    {"person" : "I_AM_NULL"}

to the following XML element:
    
    
    <person></person>

Where no value (or a value other than `I_AM_NULL`) is specified for the Null value, then the same payload converts to:
    
    
    <person>I_AM_NULL</person>

## <Options>/<InvalidCharsReplacement> element

To assist with handling invalid XML that may cause issues with a parser, this setting replaces any JSON elements that produce invalid XML with the string. For example, the following setting:
    
    
    <InvalidCharsReplacement>_</InvalidCharsReplacement>

Converts this JSON object
    
    
    {
        "First%%%Name": "John"
    }

to this XML structure:
    
    
    <First_Name>John<First_Name>

* * *

## Usage notes

In a typical mediation scenario, a JSON to XML policy on the inbound request flow is often paired with an XMLtoJSON policy on the outbound response flow. By combining policies this way, a JSON API can be exposed for services that natively support only XML.

It is often useful to apply the default (empty) JSON to XML policy and iteratively add configuration elements as required.

For scenarios where APIs are consumed by diverse clients apps which may require either JSON and XML, the format of the response can be dynamically set by configuring JSON to XML and XML to JSON policies to execute conditionally. See [Flow variables and conditions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions) for an implementation of this scenario.

## Schemas

**Sample:** See our [GitHub repository](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) samples for the most recent schemas.

## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [ What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information.Fault code | HTTP status | Cause | Fix  
---|---|---|---  
`steps.jsontoxml.ExecutionFailed` | `500` | The input payload (JSON) is empty or the input (JSON) passed to JSON to XML policy is invalid or malformed. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsontoxml-runtime-errors#executionfailed)  
`steps.jsontoxml.InCompatibleTypes` | `500` | This error occurs if the type of the variable defined in the `<Source>` element and the `<OutputVariable>` element are not the same. It is mandatory that the type of the variables contained within the `<Source>` element and the `<OutputVariable>` element matches. The valid types are `message` and `string`. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsontoxml-runtime-errors#incompatibletypes)  
`steps.jsontoxml.InvalidSourceType` | `500` | This error occurs if the type of the variable used to define the `<Source>` element is invalid. The valid types of variable are `message` and `string`.  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsontoxml-runtime-errors#invalidsourcetype)  
`steps.jsontoxml.OutputVariableIsNotAvailable` | `500` | This error occurs if the variable specified in the `<Source>` element of the JSON to XML Policy is of type string and the `<OutputVariable>` element is not defined. The `<OutputVariable>` element is mandatory when the variable defined in the `<Source>` element is of type string. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsontoxml-runtime-errors#outputvariableisnotavailable)  
`steps.jsontoxml.SourceUnavailable` | `500` |  This error occurs if the [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#messagevariables) variable specified in the `<Source>` element of the JSON to XML policy is either: 

  * Out of scope (not available in the specific flow where the policy is being executed) or
  * Can't be resolved (is not defined)

| [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsontoxml-runtime-errors#sourceunavailable)  
  
### Deployment errors

None.

### Fault variables

These variables are set when a runtime error occurs. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name Matches "SourceUnavailable"`  
`jsontoxml.policy_name.failed` | policy_name is the user-specified name of the policy that threw the fault. | `jsontoxml.JSON-to-XML-1.failed = true`  
  
### Example error response

**Note:** For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.
    
    
    {
      "fault": {
        "faultstring": "JSONToXML[JSON-to-XML-1]: Source xyz is not available",
        "detail": {
          "errorcode": "steps.json2xml.SourceUnavailable"
        }
      }
    }

### Example fault rule
    
    
    <FaultRule name="JSON To XML Faults">
        <Step>
            <Name>AM-SourceUnavailableMessage</Name>
            <Condition>(fault.name Matches "SourceUnavailable") </Condition>
        </Step>
        <Step>
            <Name>AM-BadJSON</Name>
            <Condition>(fault.name = "ExecutionFailed")</Condition>
        </Step>
        <Condition>(jsontoxml.JSON-to-XML-1.failed = true) </Condition>
    </FaultRule>

## Related topics

  * XML to JSON: [XMLtoJSON policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy)
  * XSL transformation: [XSLTransform policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xsl-transform-policy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
