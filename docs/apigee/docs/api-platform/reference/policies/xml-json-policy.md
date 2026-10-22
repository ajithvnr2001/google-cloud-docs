---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy/
title: XMLtoJSON policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:41.561583+00:00
---

# XMLtoJSON policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  XMLtoJSON policy Stay organized with collections  Save and categorize content based on your preferences. 

[Standard policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The XMLtoJSON policy converts messages from the extensible markup language (XML) format to JavaScript Object Notation (JSON), giving you several options for controlling how messages are converted.

Assuming that the intent is to convert an XML-formatted response into a JSON-formatted response, the policy would be attached to a response Flow (for example, Response / ProxyEndpoint / PostFlow).

In a typical mediation scenario, a JSON to XML policy on the inbound request flow is often paired with an XML to JSON policy on the outbound response flow. By combining policies this way, a JSON API can be exposed for backend services that natively support only XML.

For scenarios where APIs are consumed by diverse client apps that may require either JSON or XML, the response format can be dynamically set by configuring JSON to XML and XML to JSON policies to execute conditionally. See [Flow variables and conditions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions) for an implementation of this scenario.

This policy is a _Standard policy_ and can be deployed to any environment type. For information on policy types and availability with each environment type, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

### Samples

For a detailed discussion on converting between JSON and XML, see [this article](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/Converting-between-XML-and-JSON-with-Apigee-what-you-need-to/ta-p/76127).

### Converting a response
    
    
    <XMLToJSON name="ConvertToJSON">
      <Options>
      </Options>
      <OutputVariable>response</OutputVariable>
      <Source>response</Source>
    </XMLToJSON>

This configuration—which is the minimal configuration required to convert XML to JSON—takes an XML-formatted response message as the source, and then creates a JSON-formatted message that is populated in the `response` OutputVariable. Apigee automatically uses the content of this variable as the message for next processing step.

## Element reference

Following are elements and attributes you can configure on this policy.
    
    
    <XMLToJSON async="false" continueOnError="false" enabled="true" name="XML-to-JSON-1">
        <DisplayName>XML to JSON 1</DisplayName>
        <Source>response</Source>
        <OutputVariable>response</OutputVariable>
        <Options>
            <RecognizeNumber>true</RecognizeNumber>
            <RecognizeBoolean>true</RecognizeBoolean>
            <RecognizeNull>true</RecognizeNull>
            <NullValue>NULL</NullValue>
            <NamespaceBlockName>#namespaces</NamespaceBlockName>
            <DefaultNamespaceNodeName>&</DefaultNamespaceNodeName>
            <NamespaceSeparator>***</NamespaceSeparator>
            <TextAlwaysAsProperty>true</TextAlwaysAsProperty>
            <TextNodeName>TEXT</TextNodeName>
            <AttributeBlockName>FOO_BLOCK</AttributeBlockName>
            <AttributePrefix>BAR_</AttributePrefix>
            <OutputPrefix>PREFIX_</OutputPrefix>
            <OutputSuffix>_SUFFIX</OutputSuffix>
            <StripLevels>2</StripLevels>
            <TreatAsArray>
                <Path unwrap="true">teachers/teacher/studentnames/name</Path>
            </TreatAsArray>
        </Options>
        <!-- Use Options or Format, not both -->
        <Format>yahoo</Format>
    </XMLToJSON>

## <XMLtoJSON> attributes
    
    
    <XMLtoJSON async="false" continueOnError="false" enabled="true" name="XML-to-JSON-1">

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

The variable specifying the XML message that you want to convert to JSON.

The HTTP Content-type header of the source message must be set to `application/xml`, otherwise the policy is not enforced.

If `<Source>` is not defined, then it is treated as `message`, which resolves to `request` when the policy is attached to a request flow, or `response` when the policy is attached to a response flow.

If the source variable cannot be resolved, or resolves to a non-message type, the policy throws an error.
    
    
    <Source>response</Source>

Default | The value of the `Source` element  
---|---  
Presence | Optional  
Type | Message  
  
## <OutputVariable> element

Specifies where to store the output of the XML to JSON format conversion. Typically, this element is not included in the policy configuration.

Apigee parses the payload of the XML message specified in `Source`, converts it into JSON, stores the result into the payload of `OutputVariable`, and sets the HTTP Content-type header of the `OutputVariable` message to `application/json`.

If `OutputVariable` is not specified, the value of `Source` is used by default. For example, if the `source` is `response`, then `OutputVariable` defaults to `response`.
    
    
    <OutputVariable>response</OutputVariable>

Default | the message specified in `Source`  
---|---  
Presence | Optional  
Type | Message  
  
## <Options>

Options give you control over the conversion from XML to JSON. Use either the `<Options>` group, which lets you add specific conversion settings, or the `<Format>` element, which lets you reference a template of predefined options. You cannot use both `<Options>` and `<Format>`.

`<Options>` is required if `<Format>` isn't used.

### <RecognizeNumber> element

If true, then number fields in the XML payload retain their original format.
    
    
    <RecognizeNumber>true</RecognizeNumber>

Consider the following XML example:
    
    
    <a>
      <b>100</b>
      <c>value</c>
    </a>

If `RecognizeNumber` is `true`, the policy converts this to:
    
    
    {
        "a": {
            "b": 100,
            "c": "value"
        }
    }

If `RecognizeNumber` is `false`, the policy converts this to:
    
    
    {
      "a": {
        "b": "100",
        "c": "value"
      }
    }

Default | false  
---|---  
Presence | Optional  
Type | Boolean  
  
### <RecognizeBoolean> element

Lets the conversion maintain boolean true/false values rather than turning the values into strings.
    
    
    <RecognizeBoolean>true</RecognizeBoolean>

For the following XML example:
    
    
    <a>
      <b>true</b>
      <c>value</c>
    </a>

If `RecognizeBoolean` is `true`, the policy converts this to:
    
    
    {
        "a": {
            "b": true,
            "c": "value"
        }
    }

If `RecognizeBoolean` is `false`, the policy converts this to:
    
    
    {
        "a": {
            "b": "true",
            "c": "value"
        }
    }

Default | false  
---|---  
Presence | Optional  
Type | Boolean  
  
### <RecognizeNull> element

Lets you convert empty values to null values.
    
    
    <RecognizeNull>true</RecognizeNull>

For the following XML:
    
    
    <a>
      <b></b>
      <c>value</c>
    </a>

If `RecognizeNull` is `true`, and if there is no `NullValue` option, this XML converts to:
    
    
    {
      "a": {
        "b": null,
        "c": "value"
      }
    }

If `RecognizeNull` is `false`, this XML converts to:
    
    
    {
      "a": {
        "b": {},
        "c": "value"
      }
    }

Default | false  
---|---  
Presence | Optional  
Type | Boolean  
  
### <NullValue> element

Indicates the value to which recognized null values in the source message should be converted. By default the value is `null`. This option is effective only if `RecognizeNull` is true.
    
    
    <NullValue>not-present</NullValue>

For the following XML:
    
    
    <a>
      <b></b>
      <c>value</c>
    </a>

If `RecognizeNull` is `true`, and `NullValue` is not specified, this XML converts to:
    
    
    {
      "a": {
        "b": null,
        "c": "value"
      }
    }

If `RecognizeNull` is `true`, and `NullValue` is `not-present`, this XML converts to:
    
    
    {
      "a": {
        "b": "not-present",
        "c": "value"
      }
    }

Default | `null`  
---|---  
Presence | Optional  
Type | String  
  
### Namespace options

By default, this policy omits XML namespaces in the generated JSON. To specify that namespaces in the XML document should be translated into the generated JSON, use these elements together.
    
    
    <NamespaceBlockName>#namespaces</NamespaceBlockName>
    <DefaultNamespaceNodeName>&</DefaultNamespaceNodeName>
    <NamespaceSeparator>***</NamespaceSeparator>

Consider the following XML example:
    
    
    <a xmlns="http://ns.com" xmlns:ns1="http://ns1.com">
      <ns1:b>value</ns1:b>
    </a>

If `NamespaceSeparator` is not specified, the following JSON structure is generated:
    
    
    {
        "a": {
            "b": "value"
        }
    }

If the elements `NamespaceBlockName`, `DefaultNamespaceNodeName`, and `NamespaceSeparator` are specified as `#namespaces`, `&`, and `***`, respectively, then the following JSON structure is generated:
    
    
    {
        "a": {
            "#namespaces": {
                "&": "http://ns.com",
                "ns1": "http://ns1.com"
            },
            "ns1***b": "value"
        }
    }

Default | None. If `<NamespaceBlockName>` is not specified, the policy will generate output JSON that does not refer to any XML namespaces, regardless whether the source message referred to namespaces.  
---|---  
Presence | Optional  
However, if you specify `<NamespaceBlockName>`, you must also specify the other two elements.  
Type | Strings  
  
### Text options

Use these elements together.
    
    
          <TextAlwaysAsProperty>true|false</TextAlwaysAsProperty>
          <TextNodeName>TEXT</TextNodeName>

When the policy encounters an XML element that contains only a single text node as a child, the policy translates the text content of that XML element into a property in the JSON hash.

When the policy encounters an XML element that contains multiple children of [mixed content](https://www.w3.org/TR/2006/REC-xml11-20060816/#sec-element-content), these options allow you to control the output JSON of any child text nodes.

For example, consider this policy configuration:
    
    
    <XMLToJSON name='XMLToJSON-1'>
      <Options>
        <TextAlwaysAsProperty>???</TextAlwaysAsProperty>
        <TextNodeName>#text</TextNodeName>
      </Options>
    </XMLToJSON>

For the given XML inputs, the policy will generate these outputs, depending on whether `TextAlwaysAsProperty` is `true` or `false`:

XML Input | JSON Output  
---|---  
when `TextAlwaysAsProperty` is `false` | when `TextAlwaysAsProperty` is `true`  
      
    
    <a>value1</a>

| 
    
    
    {
      "a": "value1"
    }

| 
    
    
    {
      "a": {
        "#text": "value1"
      }
    }  
      
    
    <a>value1
      <b>value2</b>
    </a>

| 
    
    
    {
      "a": {
        "#text": "value1\n",
        "b": "value2"
      }
    }

| 
    
    
    {
      "a": {
        "#text": "value1\n",
        "b": {
          "#text": "value2"
        }
      }
    }  
  
Default | `<TextAlwaysAsProperty>`: false  
`<TextNodeName>`: (blank string)  
---|---  
Presence | Optional  
Type | `<TextAlwaysAsProperty>`: Boolean  
`<TextNodeName>`: String  
  
### Attribute options

These elements, together, allow you to group attribute values into a JSON block and append prefixes to the attribute names.
    
    
    <AttributeBlockName>FOO_BLOCK</AttributeBlockName>
    <AttributePrefix>BAR_</AttributePrefix>

Consider the following XML example:
    
    
    <a attrib1="value1" attrib2="value2"/>

If both the attributes (`AttributeBlockName` and `AttributePrefix`) are specified as defined in the XML to JSON example, the following JSON structure is generated:
    
    
    {
      "a": {
        "FOO_BLOCK": {
          "BAR_attrib1": "value1",
          "BAR_attrib2": "value2"
        }
      }
    }

If only `AttributeBlockName` is specified, the following JSON structure is generated:
    
    
    {
        "a": {
            "FOO_BLOCK": {
                "attrib1": "value1",
                "attrib2": "value2"
            }
        }
    }

If only `AttributePrefix` is specified, the following JSON structure is generated:
    
    
    {
        "a": {
            "BAR_attrib1": "value1",
            "BAR_attrib2": "value2"
        }
    }

If neither is specified, the following JSON structure is generated:
    
    
    {
        "a": {
            "attrib1": "value1",
            "attrib2": "value2"
        }
    }

Default | none.  
---|---  
Presence | Optional  
Type | String  
  
### <OutputPrefix> and <OutputSuffix> elements

Use these elements together to apply a prefix and/or suffix to the generated JSON.
    
    
    <OutputPrefix>PREFIX_</OutputPrefix>
    <OutputSuffix>_SUFFIX</OutputSuffix>

Consider the following XML example:
    
    
    <a>value</a>

Suppose the policy configuration is as follows:
    
    
    <XMLToJSON name='XMLToJSON-4'>
      <Options>
        <OutputPrefix>{ "result": </OutputPrefix>
        <OutputSuffix>}</OutputSuffix>
      </Options>
    </XMLToJSON>

The following JSON structure is generated:
    
    
    {
      "result": {
        "a": "value"
      }
    }

You may omit either or both of `OutputPrefix` and `OutputSuffix`.

Using these elements, it is possible to generate invalid JSON. For example, using this policy configuration:
    
    
    <XMLToJSON name='XMLToJSON-4'>
      <Options>
        <OutputPrefix>PREFIX_</OutputPrefix>
      </Options>
    </XMLToJSON>

The policy generates the following, which is not valid JSON:
    
    
    PREFIX_{
      "a" : "value"
    }

If the configuration specifies neither `OutputPrefix` nor `OutputSuffix`, the policy generates the following JSON structure:
    
    
    {
      "a": "value"
    }

Default | See samples above.  
---|---  
Presence | Optional  
Type | String  
  
### <StripLevels> element
    
    
    <Options>
        <StripLevels>4</StripLevels>
    </Options>

Sometimes XML payloads, such as SOAP, have many parent levels you don't want to include in the converted JSON. Here's an example SOAP response containing many levels:
    
    
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/Schemata-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
      <soap:Body>
          <GetCityWeatherByZIPResponse xmlns="http://ws.cdyne.com/WeatherWS/">
              <GetCityWeatherByZIPResult>
                  <State>CO</State>
                  <City>Denver</City>
                  <Description>Sunny</Description>
                  <Temperature>62</Temperature>
              </GetCityWeatherByZIPResult>
          </GetCityWeatherByZIPResponse>
      </soap:Body>
    </soap:Envelope>

There are 4 levels before you get to the State, City, Description, and Temperature level. Without using `<StripLevels>`, the converted JSON response would look like this:
    
    
    {
       "Envelope" : {
          "Body" : {
             "GetCityWeatherByZIPResponse" : {
                "GetCityWeatherByZIPResult" : {
                   "State" : "CO",
                   "City" : "Denver",
                   "Description" : "Sunny",
                   "Temperature" : "62"
                }
             }
          }
       }
    }

If you want to strip those first 4 levels in the JSON response, you'd set `<StripLevels>4</StripLevels>`, which would give you the following JSON:
    
    
    {
      "State" : "CO",
      "City" : "Denver",
      "Description" : "Sunny",
      "Temperature" : "62"
    }

You can strip levels away up to the first element that contains multiple children. What does that mean? Let's look at a more complex JSON example:
    
    
    {
       "Envelope" : {
          "Body" : {
             "GetCityForecastByZIPResponse" : {
                "GetCityForecastByZIPResult" : {
                   "ResponseText" : "City Found",
                   "ForecastResult" : {
                      "Forecast" : [
                         {
                            "ProbabilityOfPrecipiation" : {
                               "Nighttime" : "00",
                               "Daytime" : 10
                            }  ...

Level 3 in this example is `GetCityForecastByZIPResponse`, which has only one child. So if you were to use `<StripLevels>3</StripLevels>` (remove the first three levels), the JSON would look like this:
    
    
    {
       "GetCityForecastByZIPResult" : {
          "ResponseText" : "City Found",
          "ForecastResult" : {
             "Forecast" : [
                {
                   "ProbabilityOfPrecipiation" : {
                      "Nighttime" : "00",
                      "Daytime" : 10
                   }  ...

Notice that `GetCityForecastByZIPResult` has multiple children. Since it's the first element containing multiple children, you can strip this last level using `<StripLevels>4</StripLevels>`, which will give you the following JSON:
    
    
    {
       "ResponseText" : "City Found",
       "ForecastResult" : {
          "Forecast" : [
             {
                "ProbabilityOfPrecipiation" : {
                   "Nighttime" : "00",
                   "Daytime" : 10
                }  ...

Because level 4 is the first level containing multiple children, you can't strip any levels lower than this. If you set the strip level to 5, 6, 7, and so on, you'll continue to get the response above.

Default | 0 (no level stripping)  
---|---  
Presence | Optional  
Type | Integer  
  
### <TreatAsArray>/<Path> element
    
    
    <Options>
        <TreatAsArray>
            <Path unwrap="true">teachers/teacher/studentnames/name</Path>
        </TreatAsArray>
    </Options>

This element combination lets you ensure that values from an XML document are always translated to a JSON array. This can be useful when the number of child elements varies for different payloads. Apigee's default behavior is to convert multiple child elements of the same name to a JSON array and single child elements to a JSON primitive. The `TreatAsArray ` option lets you ensure that child elements are always translated to a JSON array.

Using `TreatAsArray` can improve the structure of subsequent code that handles the output, because data from the array is returned the same way every time. For example, evaluating a JSONPath of `$.teachers.teacher.studentnames.name[0]` will return the first name value consistently, whether the original XML contained one, or more than one, `name` element.

Let's take a step back and look at the XML to JSON default behavior, then explore how to control the output using `<TreatAsArray>/<Path>`.

When an XML document contains an element with multiple occurrences (which can happen when the XML schema specifies `maxOccurs='unbounded'` for the element), the XML to JSON policy automatically puts those values in an array. For example, the following XML block
    
    
    <teacher>
        <name>teacherA</name>
        <studentnames>
            <name>student1</name>
            <name>student2</name>
        </studentnames>
    </teacher>

...gets converted into the following JSON automatically with no special policy configuration:
    
    
    {
      "teachers" : {
        "teacher" : {
          "name" : "teacherA",
          "studentnames" : {
            "name" : **[
              "student1",
              "student2"
            ]**
          }
        }
      }
    }

Notice that the two student names are contained in an array.

However, if only one student appears in the XML document, the XML to JSON policy automatically treats the value as a single string, not an array of strings, as shown in the following example:
    
    
    {
      "teachers" : {
        "teacher" : {
          "name" : "teacherA",
          "studentnames" : {
            "name" : **"student1"**
          }
        }
      }
    }

In the previous examples, similar data was converted differently, once to an array, another to a single string. The `<TreatAsArray>/<Path>` element lets you control the output to make sure that the student names are always converted into an array even if there's only one value. You configure this by identifying the Path to the element whose values you want to convert into an array, like so:
    
    
    <Options>
        <TreatAsArray>
            <Path>teachers/teacher/studentnames/name</Path>
        </TreatAsArray>
    </Options>

**Note:** The Path is **not** JSONPath. It's simply the hierarchical path to the element whose values you want to put in an array.

The configuration above would generate the JSON like this:
    
    
    {
      "teachers" : {
        "teacher" : {
          "name" : "teacherA",
          "studentnames" : {
            "name" : **["student1"]**
          }
        }
      }
    }

Notice that student1 is now in an array. Now, regardless of whether there are one or multiple students, you can retrieve them from a JSON array in your code using the following JSONPath: `$.teachers.teacher.studentnames.name[0]`

The `<Path>` element also has an `unwrap` attribute, explained in the next section.

Default | N/A  
---|---  
Presence | Optional  
Type | String  
  
#### Attributes
    
    
    **** <Options>
        <TreatAsArray>
            <Path **unwrap="true"** >teachers/teacher/studentnames/name</Path>
        </TreatAsArray>
    </Options>

Attribute | Description | Presence | Type  
---|---|---|---  
unwrap |  Default: false Removes the element from the JSON output. Use this to streamline or flatten ("unwrap") the JSON, which also shortens the JSONPath needed to retrieve values. For example, instead of `$.teachers.teacher.studentnames.name[*]`, you could flatten the JSON and use `$.teachers.studentnames[*]`. Here's a JSON example:
    
    
    {
      "teachers" : {
          "teacher" : {
              "name" : "teacherA",
              "studentnames" : {
                  "name" : [
                     "student1",
                     "student2"
                  ]}...

In this example, you could argue that the `teacher` element and the studentnames `name` element are unnecessary. So you can remove, or unwrap them. Here's how you'd configure the `<Path>` element to do this:
    
    
    <TreatAsArray>
        <Path unwrap="true">teachers/teacher</Path>
        <Path unwrap="true">teachers/teacher/studentnames/name</Path>
    </TreatAsArray>

The `unwrap` attribute is set to true, and the paths to the elements to unwrap are provided. The JSON output will now look like this:
    
    
    {
      "teachers" : [{
          "name" : "teacherA",
          "studentnames" : ["student1","student2"]
          }]...

Note that because the `<Path>` element is in the `<TreatAsArray>` element, both of the elements in the Path will be treated as arrays in the JSON output. | Optional | Boolean  
  
For more examples and a feature walkthrough, see [ this Google Cloud Community article.](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/Tutorial-the-TreatAsArray-option-in-the-XMLToJSON-policy/ta-p/77314).

## <Format>

Format gives you control over the conversion from XML to JSON. Enter the name of a predefined template that contains a specific combination of Options elements described in this topic. Predefined formats include: `xml.com`, `yahoo`, `google`, `badgerFish`.

Use either the `<Format>` element or the `<Options>` group. You cannot use both `<Format>` and `<Options>`.

Following are the Format definitions of each predefined template.

### xml.com
    
    
    <RecognizeNull>true</RecognizeNull>
    <TextNodeName>#text</TextNodeName>
    <AttributePrefix>@</AttributePrefix>

### yahoo
    
    
    <RecognizeNumber>true</RecognizeNumber>
    <TextNodeName>content</TextNodeName>

### google
    
    
    <TextNodeName>$t</TextNodeName>
    <NamespaceSeparator>$</NamespaceSeparator>
    <TextAlwaysAsProperty>true</TextAlwaysAsProperty>

### badgerFish
    
    
    <TextNodeName>$</TextNodeName>
    <TextAlwaysAsProperty>true</TextAlwaysAsProperty>
    <AttributePrefix>@</AttributePrefix>
    <NamespaceSeparator>:</NamespaceSeparator>
    <NamespaceBlockName>@xmlns</NamespaceBlockName>
    <DefaultNamespaceNodeName>$</DefaultNamespaceNodeName>

Element syntax:
    
    
    <Format>yahoo</Format>

Default | (none)  
---|---  
Valid values | One of the following:  
`xml.com`, `yahoo`, `google`, `badgerFish`  
Presence | Optional, but Required if `<Options>` isn't used.  
Type | String  
  
### Schemas

**Sample:** See our [GitHub repository](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) samples for the most recent schemas.

* * *

## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information.Fault code | HTTP status | Cause | Fix  
---|---|---|---  
`steps.xmltojson.ExecutionFailed` | `ExecutionFailed` | This error occurs when the input payload (XML) is empty or the input XML is invalid or malformed. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/xmltojson-runtime-errors#executionfailed)  
`steps.xmltojson.InCompatibleTypes` | `ExecutionFailed` | This error occurs if the type of the variable defined in the `<Source>` element and the `<OutputVariable>` element are not the same. It is mandatory that the type of the variables contained within the `<Source>` element and the `<OutputVariable>` element matches.  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/xmltojson-runtime-errors#incompatibletypes)  
`steps.xmltojson.InvalidSourceType` | `ExecutionFailed` | This error occurs if the type of the variable used to define the `<Source>` element is invalid.The valid types of variable are message and string. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/xmltojson-runtime-errors#invalidsourcetype)  
`steps.xmltojson.OutputVariableIsNotAvailable` | `ExecutionFailed` | This error occurs if the variable specified in the `<Source>` element of the XML to JSON policy is of type string and the `<OutputVariable>` element is not defined. The `<OutputVariable>` element is mandatory when the variable defined in the `<Source>` element is of type string. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/xmltojson-runtime-errors#outputvariableisnotavailable)  
`steps.xmltojson.SourceUnavailable` | `ExecutionFailed` |  This error occurs if the [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#messagevariables) variable specified in the `<Source>` element of the XML to JSON policy is either: 

  * Out of scope (not available in the specific flow where the policy is being executed) or
  * Can't be resolved (is not defined)

| [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/xmltojson-runtime-errors#sourceunavailable)  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information. Error name | Cause | Fix  
---|---|---  
`EitherOptionOrFormat` |  If one of the elements `<Options>` or `<Format>` is not declared in the XML to JSON Policy, then the deployment of the API proxy fails.  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/xmltojson-deployment-errors#eitheroptionorformat)  
`UnknownFormat` |  If the `<Format>` element within the XML to JSON policy has an unknown format defined, then the deployment of the API proxy fails. Predefined formats include: `xml.com`, `yahoo`, `google`, and `badgerFish`.  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/xmltojson-deployment-errors#unknownformat)  
  
### Fault variables

These variables are set when a runtime error occurs. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name = "SourceUnavailable"`  
`xmltojson.policy_name.failed` | policy_name is the user-specified name of the policy that threw the fault. | `xmltojson.XMLtoJSON-1.failed = true`  
  
### Example error response

**Note:** For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.
    
    
    {
      "fault": {
        "faultstring": "XMLToJSON[XMLtoJSON-1]: Source xyz is not available",
        "detail": {
          "errorcode": "steps.xml2json.SourceUnavailable"
        }
      }
    }

### Example fault rule
    
    
    <faultrule name="VariableOfNonMsgType"></faultrule><FaultRule name="XML to JSON Faults">
        <Step>
            <Name>AM-SourceUnavailableMessage</Name>
            <Condition>(fault.name Matches "SourceUnavailable") </Condition>
        </Step>
        <Step>
            <Name>AM-BadXML</Name>
            <Condition>(fault.name = "ExecutionFailed")</Condition>
        </Step>
        <Condition>(xmltojson.XMLtoJSON-1.failed = true) </Condition>
    </FaultRule>

## Related topics

JSON to XML: [JSONtoXML policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-xml-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
