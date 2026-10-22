---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy/
title: ExtractVariables policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:18.698106+00:00
---

# ExtractVariables policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  ExtractVariables policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The ExtractVariables policy extracts content from a request or response and sets the value of a variable to that content. You can extract any part of the message, including headers, URI paths, JSON/XML payloads, form parameters, and query parameters. The policy works by applying a text pattern to the message content and, upon finding a match, sets a variable with the specified message content.

You can also use this policy to extract information from other sources, such as entities created by the [AccessEntity policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-entity-policy), XML objects, or JSON objects.

After extracting the specified message content, you can reference the variable in other policies as part of processing a request and response. For example, you could add the [RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/raise-fault-policy) to return an error if the extracted value is invalid.

**Note about Service Callouts** : You don't need to use this policy to extract variables from Service Callouts. The [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy) has its own request and response variables that you can use directly, for example in an [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy).

When defining the ExtractVariables policy, you can choose:

  * Names of the variables to be set
  * Source of the variables
  * How many variables to extract and set



When executed, the policy applies a text pattern to the content and, upon finding a match, sets the value of the designated variable with the content. Other policies and code can then consume those variables to enable dynamic behavior or to send business data to Apigee API Analytics.

**Warning:** Apigee sets numerous variables automatically during request processing. See [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference). Use the ExtractVariables policy to set additional variables.

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## Samples

These policy code samples illustrate how to extract variables from the following types of artifacts:

### URIs
    
    
    <ExtractVariables name="ExtractVariables-1">
       <DisplayName>Extract a portion of the url path</DisplayName>
       <Source>request</Source>
       <URIPath>
          <Pattern ignoreCase="true">/accounts/{id}</Pattern>
       </URIPath>
       <VariablePrefix>urirequest</VariablePrefix>
       <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </ExtractVariables>

Consider the sample policy code above. The `<URIPath>` element tells the ExtractVariables policy to extract information from the URI path. The `<Pattern>` element specifies the pattern to apply to the URI path. The pattern is treated as a simple template, with the curly braces denoting the varying portion of the URI path.

The name of the variable to be set is determined by the value specified in the `<VariablePrefix>` element, as well as the value enclosed in curly braces {} in the `<Pattern>` element. The two values are joined by an intervening dot, resulting in a variable name of `urirequest.id` for example. If there is no `<VariablePrefix>` element, then the variable name is just the value enclosed in curly braces.

Consider the sample policy code above working with the following incoming request:

`GET http://example.com/svc1/accounts/12797282`

Suppose the basepath for the API Proxy is `/svc1`. When Apigee applies the ExtractVariables policy code above to this incoming request, it sets the variable `urirequest.id` to `12797282`. After Apigee executes the policy, subsequent policies or code in the processing flow can refer to the variable named `urirequest.id` to get the string value `12797282`.

For example, the following [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) embeds the value of that variable into the payload of a new request message:
    
    
    <AssignMessage async="false" continueOnError="false" enabled="true" name="AssignPayload">
      <DisplayName>AssignPayload</DisplayName>
        <Set>
          <Payload contentType="text/xml">
            <IdExtractedFromURI>{urirequest.id}</IdExtractedFromURI>
          </Payload>
        </Set>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <AssignTo createNew="true" transport="http" type="request">newRequest</AssignTo>
    </AssignMessage>

### Query params
    
    
    <ExtractVariables name="ExtractVariables-2">
       <DisplayName>Extract a value from a query parameter</DisplayName>
       <Source>request</Source>
       <QueryParam name="code">
          <Pattern ignoreCase="true">DBN{dbncode}</Pattern>
       </QueryParam>
       <VariablePrefix>queryinfo</VariablePrefix>
       <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </ExtractVariables>

Consider the sample policy code above working with the following incoming request:

`GET http://example.com/accounts/12797282?code=DBN88271`

When Apigee applies the ExtractVariables policy code above to this incoming request, it sets the variable `queryinfo.dbncode` to `88271`. After Apigee executes the policy, subsequent policies or code in the processing flow can refer to the variable named `queryinfo.dbncode` to get the string value `88271`.

You can now access the variable `queryinfo.dbncode` in your proxy. For example, the following [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) copies it to the payload of the request:
    
    
    <AssignMessage async="false" continueOnError="false" enabled="true" name="GetURIPath">
      <DisplayName>GetQP</DisplayName>
      <Set>
       <Payload contentType="text/xml">
        <ExtractQP>{queryinfo.dbncode}</ExtractQP>
       </Payload>
      </Set>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <AssignTo createNew="false" transport="http" type="request"/>
    </AssignMessage>

### Multiple parameters
    
    
    <ExtractVariables name="ExtractVariables-2">
      <DisplayName>Extract a value from a query parameter</DisplayName>
      <Source>request</Source>
      <QueryParam name="w">
        <Pattern ignoreCase="true">{firstWeather}</Pattern>
      </QueryParam>
      <QueryParam name="w.2">
        <Pattern ignoreCase="true">{secondWeather}</Pattern>
      </QueryParam>
      <VariablePrefix>queryinfo</VariablePrefix>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </ExtractVariables>

Suppose your API design allows you to specify multiple query parameters with the same name. You can use an ExtractVariables policy to extract the value of multiple instances of the query parameter. To reference query parameters with the same name in the policy, use indexes where the first instance of the query parameter has no index, the second is at index 2, the third at index 3, and so on.

Consider the sample policy code above working with the following incoming request:

`GET http://example.com/weather?w=Boston&w=Chicago`

When Apigee applies the ExtractVariables policy code above to this incoming request, it sets the variable `queryinfo.firstWeather` to `Boston` and the variable `queryInfo.secondWeather` to `Chicago`. 

You can now access the variable `queryinfo.firstWeather` and `queryinfo.secondWeather` in your proxy. For example, the following [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) copies it to the payload of the request:
    
    
    <AssignMessage async="false" continueOnError="false" enabled="true" name="GetURIPath">
      <DisplayName>GetQP</DisplayName>
      <Set>
        <Payload contentType="text/xml">
          <ExtractQP1>{queryinfo.firstWeather}</ExtractQP1>
          <ExtractQP2>{queryinfo.secondWeather}</ExtractQP2>
        </Payload>
      </Set>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <AssignTo createNew="false" transport="http" type="request"/>
    </AssignMessage>

### Headers
    
    
    <ExtractVariables name='ExtractVariable-OauthToken'>
      <Source>request</Source>
      <Header name="Authorization">
        <Pattern ignoreCase="false">Bearer {oauthtoken}</Pattern>
      </Header>
      <VariablePrefix>clientrequest</VariablePrefix>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </ExtractVariables>

Suppose that your API uses OAuth v2.0 bearer tokens. Consider the sample policy code above working with a request carrying an OAuth v2.0 token that includes a header like this: `Authorization: Bearer TU08xptfFfeM7aS0xHqlxTgEAdAM.`

As the API designer, suppose that you want to use the token value (but not the entire header) as a key in a cache lookup. You could use the ExtractVariables policy code above to extract the token.

When Apigee applies the ExtractVariables policy code above to this header, it sets the variable `clientrequest.oauthtoken` to `TU08xptfFfeM7aS0xHqlxTgEAdAM`.

You can now access the variable `clientrequest.oauthtoken` in your proxy. For example, the following AssignMessage policy copies it to the payload of the request:
    
    
    <AssignMessage async="false" continueOnError="false" enabled="true" name="GetURIPath">
      <DisplayName>GetHeader</DisplayName>
      <Set>
        <Payload contentType="text/xml">
          <ExtractHeader>{clientrequest.oauthtoken}</ExtractHeader>
        </Payload>
      </Set>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <AssignTo createNew="false" transport="http" type="request"/>
    </AssignMessage>

### JSON
    
    
    <ExtractVariables name="ExtractVariables-3">
      <Source>response</Source>
      <JSONPayload>
        <Variable name="latitude" type="float">
          <JSONPath>$.results[0].geometry.location.lat</JSONPath>
        </Variable>
        <Variable name="longitude" type="float">
          <JSONPath>$.results[0].geometry.location.lng</JSONPath>
        </Variable>
      </JSONPayload>
      <VariablePrefix>geocoderesponse</VariablePrefix>
    </ExtractVariables>

Consider the following JSON response payload:
    
    
    {
      "results": [{
        "geometry": {
          "location": {
            "lat": 37.42291810,
            "lng": -122.08542120
          },
          "location_type": "ROOFTOP",
          "viewport": {
            "northeast": {
              "lat": 37.42426708029149,
              "lng": -122.0840722197085
            },
            "southwest": {
              "lat": 37.42156911970850,
              "lng": -122.0867701802915
            }
          }
        }
      }]
    }

When Apigee applies the ExtractVariables policy code above to this JSON message, it sets two variables: `geocoderesponse.latitude` and `geocoderesponse.longitude`. Both variables use the same variable prefix of `geocoderesponse`. The suffix for these variables is specified explicitly by the `<Variable>` element's `name` attribute.

The variable `geocoderesponse.latitude` gets the value `37.42291810`. The variable `geocoderesponse.longitude` gets the value `-122.08542120`.

You can now access the variable `geocoderesponse.latitude` in your proxy. For example, the following AssignMessage policy copies it to a header named `latitude` in the response:
    
    
    <AssignMessage async="false" continueOnError="false" enabled="true" name="GetURIPath">
      <DisplayName>GetJSONVar</DisplayName>
      <Add>
        <Headers>
          <Header name="latitude">{geocoderesponse.latitude}</Header>
        </Headers>
      </Add>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <AssignTo createNew="false" transport="http" type="response"/>
    </AssignMessage>

### XML
    
    
    <ExtractVariables name="ExtractVariables-4">
       <Source>response</Source>
       <XMLPayload>
          <Namespaces>
             <Namespace prefix="dir">urn:43BFF88D-D204-4427-B6BA-140AF393142F</Namespace>
          </Namespaces>
          <Variable name="travelmode" type="string">
             <XPath>/dir:Directions/dir:route/dir:leg/dir:step/@mode</XPath>
          </Variable>
          <Variable name="duration" type="string">
             <XPath>/dir:Directions/dir:route/dir:leg/dir:step/dir:duration/dir:value</XPath>
          </Variable>
          <Variable name="timeunit" type="string">
             <XPath>/dir:Directions/dir:route/dir:leg/dir:step/dir:duration/dir:text</XPath>
          </Variable>
       </XMLPayload>
       <VariablePrefix>directionsresponse</VariablePrefix>
    </ExtractVariables>

Consider the following XML response payload:
    
    
    <Directions xmlns="urn:43BFF88D-D204-4427-B6BA-140AF393142F">
       <status>OK</status>
       <route>
          <summary>I-40 W</summary>
          <leg>
             <step mode="DRIVING">
                <start_location>
                   <lat>41.8507300</lat>
                   <lng>-87.6512600</lng>
                </start_location>
                <end_location>
                   <lat>41.8525800</lat>
                   <lng>-87.6514100</lng>
                </end_location>
                <duration>
                    <value>19</value>
                    <text>minutes</text>
                </duration>
             </step>
          </leg>
       </route>
    </Directions>

When Apigee applies the ExtractVariables policy code above to this XML message, it sets three variables:

  * `directionsresponse.travelmode`: Gets the value `DRIVING`
  * `directionsresponse.duration`: Gets the value `19`
  * `directionsresponse.timeunit`: Gets the value `minutes`



All variables use the same variable prefix of `directionsresponse`. The suffix for these variables is specified explicitly by the `<Variable>` element's `name` attribute.

You can now access the variable `directionresponse.travelmode` in your proxy. For example, the following [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) copies it to a header named `tmode` in the response:
    
    
    <AssignMessage async="false" continueOnError="false" enabled="true" name="GetURIPath">
      <DisplayName>GetXMLVar</DisplayName>
      <Add>
        <Headers>
          <Header name="tmode">{directionsresponse.travelmode}</Header>
        </Headers>
      </Add>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <AssignTo createNew="false" transport="http" type="request"/>
    </AssignMessage>

**Note:** **Setting Content-Type** : When extracting variables from XML messages (including SOAP), the variable extraction works only when `Content-Type` is set in the message header (or SOAP header); for example, `application/xml`.

## Variable Scope

Variables set with the ExtractVariables policy have _global_ scope. That is, after the ExtractVariables policy defines a new variable, you can access that variable from any policy or code in any stage of the flow that executes _after_ the ExtractVariables policy. This includes:

  * **PreFlow:** ProxyEndpoint and TargetEndpoint (Request and Response)
  * **PostFlow:** ProxyEndpoint and TargetEndpoint (Request and Response)
  * **PostClientFlow:** ProxyEndpoint (Response only, using the [MessageLogging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy)>)
  * **Error Flows**

**Tip:** If you do not see the newly extracted variable show up in the [Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview), try removing the `<VariablePrefix>` element if you added it. For more information, refer to this [ExtractVariables not shown in trace](https://discuss.google.dev/t/extractvariables-not-shown-in-trace/276).

## Matching and variable creation

The ExtractVariables policy extracts information from a request or response and writes that information to a variable. For each type of information that you can extract, such as URI path or XML data, you specify the pattern to match and the name of the variable used to hold the extracted information. 

However, the way pattern matching works depends on the source of the extraction. The following sections describe the two basic categories of information that you can extract.

###  Matching URI paths, query parameters, headers, form parameters, and variables

When extracting information from a URI path, query parameters, headers, form parameters, and variables you use the `<Pattern>` tag to specify one or more patterns to match. For example, the following policy example shows a single matching pattern for the URI path:
    
    
    <ExtractVariables name="ExtractVariables-1">
       <Source>request</Source>
       <URIPath>
         ** <Pattern ignoreCase="true">/a/{pathSeg}</Pattern>**
       </URIPath>
       <VariablePrefix>urirequest</VariablePrefix>
       <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </ExtractVariables>

In this example, the `urirequest.pathSeg` variable is set to whatever appears in the proxy.pathsuffix after `/a/`. For example, suppose the base path for your API Proxy is `/basepath/v1` . With an inbound request to `http://myCo.com/basepath/v1/a/b` the variable is set to `b`.

#### Specifying multiple patterns

You can specify multiple patters to match, corresponding to `<Pattern>` tags, where:

  * All patterns are tested for match.
  * If none of the patterns match, the policy does nothing and the variable(s) is not created.
  * If more than one pattern matches, the pattern with longest path segments is used for extraction.
  * If two matched patterns has same longest path segments, then the pattern specified first in the policy is used for extraction.



In the next example, you create a policy that contains three matching patterns for the URI path:
    
    
    <ExtractVariables name="ExtractVariables-1">
      <Source>request</Source>
      <URIPath>
        **< Pattern ignoreCase="true">/a/{pathSeg}</Pattern>
        <Pattern ignoreCase="true">/a/b/{pathSeg}</Pattern>
        <Pattern ignoreCase="true">/a/b/c/{pathSeg}</Pattern>**
      </URIPath>
      <VariablePrefix>urirequest</VariablePrefix>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </ExtractVariables>

Suppose, for an API Proxy with a basepath of `/basepath/v1` , the inbound request URL to the API proxy is of this form:
    
    
    http://myCo.com/basepath/v1/a/b

In this example, the first pattern matches the URI and the `urirequest.pathSeg` variable is set to `b`.

If the request URL is:
    
    
    http://myCo.com/basepath/v1/a/b/c/d

...then the third pattern matches and the `urirequest.pathSeg` variable is set to `d`.

#### Specifying patterns with multiple variables

You can specify multiple variables in the matching pattern. For example, you specify a matching pattern with two variables:
    
    
    <ExtractVariables name="ExtractVariables-1">
      <Source>request</Source>
      <URIPath>
        <Pattern ignoreCase="true">/a/{pathSeg}</Pattern>
        <Pattern ignoreCase="true">/a/b/{pathSeg}</Pattern>
        **< Pattern ignoreCase="true">/a/{pathSeg1}/c/{pathSeg2}</Pattern>**
      </URIPath>
      <VariablePrefix>urirequest</VariablePrefix>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </ExtractVariables>

Again supposing an API Proxy with a base path of `/basepath/v1` , for the inbound request URL:
    
    
    http://myCo.com/basepath/v1/a/b/c/d

...the `urirequest.pathSeg1` variable is set to `b` and the `urirequest.pathSeg2` variable is set to `d`.

#### Matching multiple instances in the pattern

You can also match patterns when there are multiple instances of an item with the same name. For example, you can make a request that contains multiple query parameters or multiple headers with the same name. The following request contains two query parameters named "w":
    
    
    http://myCo.com/basepath/v1/a/b/c/d?w=1&w=2

To reference these query parameters in the ExtractVariables policy, you use indexes, where the first instance of the query parameter has no index, the second is at index 2, the third at index 3, etc. For example, the following policy extracts the value of the second query parameter named "w" in the request:
    
    
    <ExtractVariables name="ExtractVariables-1">
      <Source>request</Source>
      **< QueryParam name="w.2">**
        <Pattern ignoreCase="true">{secondW}</Pattern>
      </QueryParam>
      <VariablePrefix>urirequest</VariablePrefix>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </ExtractVariables>

The `urirequest.secondW` variable is set to "2". If the second query parameter is omitted from the request, then the `urirequest.secondW` variable is empty. Use indexing any time there are multiple items with the same name in the request.

#### Using special characters in the pattern

When matching URI paths, you can use the "*" and "**" wildcard characters in the pattern, where:

  * "*" matches any one segments of the path
  * "**" matches multiple segments of the path



For example, you specify patterns to the `<URIPath>` element as shown below:
    
    
    <URIPath>
      <Pattern ignoreCase="true">/a/*/{id}</Pattern>
      <Pattern ignoreCase="true">/a/**/{id}</Pattern>
    </URIPath>

The first pattern matches requests with pathsuffixes (the portion of the URI path following the basepath) such as "/a/b/c", "/a/foo/bar", etc. The second pattern matches any number of path segments after "/a/", such as "/a/foo/bar/baz/c", as well as "/a/b/c" and "/a/foo/bar".

When specifying patterns to query parameters, headers, and form parameters, the "*"character specifies to match any number of characters. For example, when matching a header, specify the pattern as:
    
    
    *;charset={encoding}

This pattern matches the values "text/xml;charset=UTF-16" and "application/xml;charset=ASCII".

If the value passed to the ExtractVariables policy contains a special character, such as "{", use the "%" character to escape it. The following example escapes the "{" and "}" characters in the pattern because they are used as literal characters in the value of the query parameter:
    
    
    <QueryParam>
      <Pattern ignoreCase="true">%{user%} {name}</Pattern>
    </QueryParam>

In this example, the pattern matches the value "{user} Steve" but not the value "user Steve". 

### Matching JSON and XML

When extracting data from JSON and XML, you specify one or more `<Variable>` tags in the policy. The `<Variable>` tag specifies the name of the destination variable where the extracted information is stored, and the JsonPath (JSON) or XPATH (XML) to the extracted information. 

All `<Variable>` tags in the policy are evaluated, so that you can populate multiple variables from a single policy. If the `<Variable>` tag does not evaluate to a valid field in the JSON or XML, then the corresponding variable is not created. 

The following example shows an ExtractVariables policy that populates two variables from the JSON body of a response:
    
    
    <ExtractVariables name="ExtractVariables-3">
       <Source>response</Source>
       <JSONPayload>
          <Variable name="latitude" type="float">
             <JSONPath>$.results[0].geometry.location.lat</JSONPath>
          </Variable>
          <Variable name="longitude" type="float">
             <JSONPath>$.results[0].geometry.location.lng</JSONPath>
          </Variable>
       </JSONPayload>
       <VariablePrefix>geocoderesponse</VariablePrefix>
    </ExtractVariables>

### Writing to the same variable in multiple places

Take care when choosing the names of variables to set. The policy executes sequentially from the first extraction pattern to the last. If the policy writes a value to the same variable from multiple places, the last write in the policy determines the value of the variable. (This may be what you want.)

For example, you want to extract a token value that can be passed either in a query parameter or in a header, as shown below:
    
    
    <!-- If token only in query param, the query param determines the value.
         If token is found in both the query param and header, header sets value. -->
    <QueryParam name="token">
      <Pattern ignoreCase="true">{tokenValue}</Pattern>
    </QueryParam>
    
    <!-- Overwrite tokenValue even if it was found in query parameter. -->
    <Header name="Token">
      <Pattern ignoreCase="true">{tokenValue}</Pattern>
    </Header>

### Controlling what happens when no match occurs

If the pattern does not match, then the corresponding variable is not created. Therefore, if another policy references the variable, it can cause an error.

One option is to set `<IgnoreUnresolvedVariables>` to true in a policy that references the variable to configure the policy to treat any unresolvable variable as an empty string (null):
    
    
    <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>

## Element reference

The element reference describes the elements and attributes of the ExtractVariables policy.
    
    
    <ExtractVariables async="false" continueOnError="false" enabled="true" name="Extract-Variables-1">
       <DisplayName> 1</DisplayName>
       <Source clearPayload="true|false">request</Source>
       <VariablePrefix>myprefix</VariablePrefix>
       <IgnoreUnresolvedVariables>true|false</IgnoreUnresolvedVariables>
       <URIPath>
          <Pattern ignoreCase="false">/accounts/{id}</Pattern>
       </URIPath>
       <QueryParam name="code">
          <Pattern ignoreCase="true">DBN{dbncode}</Pattern>
       </QueryParam>
       <Header name="Authorization">
          <Pattern ignoreCase="false">Bearer {oauthtoken}</Pattern>
       </Header>
       <FormParam name="greeting">
          <Pattern>hello {user}</Pattern>
       </FormParam>
       <Variable name="request.content">
           <Pattern>hello {user}</Pattern>
       </Variable>
       <JSONPayload>
          <Variable name="name">
             <JSONPath>{example}</JSONPath>
          </Variable>
       </JSONPayload>
       <XMLPayload stopPayloadProcessing="false">
          <Namespaces/>
          <Variable name="name" type="boolean">
             <XPath>/test/example</XPath>
          </Variable>
       </XMLPayload>
    </ExtractVariables>

## <ExtractVariables> attributes
    
    
    <ExtractVariables async="false" continueOnError="false" enabled="true" name="Extract-Variables-1">

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

(Optional) Specifies the variable to be parsed. The value of `<Source>` defaults to `message`. The `message` value is context-sensitive. In a request flow, `message` resolves to the request message. In a response flow, `message` resolves to the response message.

While you often use this policy to extract information from a request or response message, you can use it to extract information from any variable. For example, you can use it to extract information from an entity created by the [AccessEntity policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-entity-policy), from data returned by the [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy), or extract information from an XML or JSON object.  
  
If `<Source>` cannot be resolved, or resolves to a non-message type, the policy will fail to respond.
    
    
    <Source clearPayload="true|false">request</Source>

**Default:** | message  
---|---  
**Presence:** | Optional  
**Type:** | String  
  
### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
`clearPayload` |  Set to **true** if you want to clear the payload specified in `<Source>` after extracting data from it. Use the `<clearPayload>` option only if the source message is not required after ExtractVariables is executed. Setting to **true** frees up the memory used by the message. |  false | Optional | Boolean  
  
## <VariablePrefix> element

(Optional) The complete variable name is created by joining the `<VariablePrefix>`, a dot, and the name you define in {curly braces} in the `<Pattern>` element or `<Variable>` element. For example: `myprefix.id`, `myprefix.dbncode`, or `myprefix.oauthtoken.`
    
    
    <VariablePrefix>myprefix</VariablePrefix>

For example, suppose the value of name is "user".

  * If `<VariablePrefix>` is not specified, the extracted values are assigned to a variable named `user`.
  * If `<VariablePrefix>` is specified as myprefix, the extracted values are assigned to a variable named `myprefix.user`.

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | String  
  
## <IgnoreUnresolvedVariables> element

(Optional) Set to `true` to treat any unresolvable variable as an empty string (null). Set to `false` if you want the policy to throw an error when any referenced variable is unresolvable.
    
    
    <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>

**Default:** | False  
---|---  
**Presence:** | Optional  
**Type:** | Boolean  
  
## <URIPath> element

(Optional, but see the Presence row in the table below for more information.) Extracts a value from the proxy.pathsuffix of a `request` source message. The path applied to the pattern is the proxy.pathsuffix, which does not include the basepath for the API Proxy. If the source message resolves to a message type of `response`, then this element does nothing.
    
    
    <URIPath>
       <Pattern ignoreCase="false">/accounts/{id}</Pattern>
    </URIPath>

It is possible to use multiple `<Pattern>` elements:
    
    
    <URIPath>
       <Pattern ignoreCase="false">/accounts/{id}</Pattern>
       <Pattern ignoreCase="false">/accounts/{id}/transactions/{index}</Pattern>
    </URIPath>

**Default:** | N/A  
---|---  
**Presence:** | Optional. However, you must include at least one of the following: `<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<JSONPayload>`, or `<XMLPayload>.`  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
ignoreCase | Specifies to ignore case when matching the patern. |  false | Optional | Boolean  
  
## <QueryParam> element

(Optional, but see the Presence row in the table below for more information.) Extracts a value from the specified query parameter of a `request` source message. If the source message resolves to a message type of `response`, then this element does nothing.
    
    
    <QueryParam name="code">
       <Pattern ignoreCase="true">DBN{dbncode}</Pattern>
    </QueryParam>

If multiple query parameters have the same name, use indexes to reference the parameters:
    
    
    <QueryParam name="w.2">
       <Pattern ignoreCase="true">{secondW}</Pattern>
    </QueryParam>

**Default:** | N/A  
---|---  
**Presence:** | Optional. However, you must include at least one of the following: `<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<JSONPayload>`, or `<XMLPayload>.`  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
name | Specifies the name of the query parameter. If multiple query parameters have the same name, use indexed referencing, where the first instance of the query parameter has no index, the second is at index 2, the third at index 3, etc.  |  N/A | Required | String  
  
## <Header> element

(Optional, but see the Presence row in the table below for more information.) Extracts a value from the specified HTTP header of the specified `request` or `response` message. If multiple headers have the same name, their values are stored in an array.
    
    
    <!-- The name is the actual header name. -->
    <Header name="Authorization">
    <!-- Provide a name for your new custom variable here. -->
       <Pattern ignoreCase="false">Bearer {oauthtoken}</Pattern>
    </Header>

If multiple headers have the same name, use indexes to reference individual headers in the array:
    
    
    <Header name="myHeader.2">
       <Pattern ignoreCase="true">{secondHeader}</Pattern>
    </Header>

Or the following to list all the headers in the array:
    
    
    <Header name="myHeader.values">
       <Pattern ignoreCase="true">{myHeaders}</Pattern>
    </Header>

**Default:** | N/A  
---|---  
**Presence:** | Optional. However, you must include at least one of the following: `<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<JSONPayload>`, or `<XMLPayload>.`  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
name | Specifies the name of the header from which you extract the value. If multiple headers have the same name, use indexed referencing, where the first instance of the header has no index, the second is at index 2, the third at index 3, etc. Use `.values` to get all headers in the array. |  N/A | Required | String  
  
## <FormParam> element

(Optional, but see the Presence row in the table below for more information.) Extracts a value from the specified form parameter of the specified `request` or `response` message. Form parameters can be extracted only when the `Content-Type` header of the specified message is `application/x-www-form-urlencoded`.
    
    
    <FormParam name="greeting">
        <Pattern>hello {user}</Pattern>
    </FormParam>

**Default:** | N/A  
---|---  
**Presence:** | Optional. However, you must include at least one of the following: `<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<JSONPayload>`, or `<XMLPayload>.`  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
name | The name of the form parameter from which you extract the value. |  N/A | Required | String  
  
## <Variable> element

(Optional, but see the Presence row in the table below for more information.) Specifies the name of a variable from which to extract a value. 
    
    
    <Variable name="myVar">
        <Pattern>hello {user}</Pattern>
    </Variable>

To extract two values from the variable:
    
    
    <Variable name="myVar">
       <Pattern>hello {firstName} {lastName}</Pattern>
    </Variable>

**Default:** | N/A  
---|---  
**Presence:** | Optional. However, you must include at least one of the following: `<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<JSONPayload>`, or `<XMLPayload>.`  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
name | The name of the variable from which to extract the value. |  N/A | Required | String  
  
## <JSONPayload> element

(Optional, but see the Presence row in the table below for more information.) Specifies the JSON-formatted message from which the value of the variable will be extracted. JSON extraction is performed only when message's `Content-Type` header is `application/json`.
    
    
    <JSONPayload>
       <Variable name="name" type="string">
          <JSONPath>{example}</JSONPath>
       </Variable>
    </JSONPayload>

**Default:** | N/A  
---|---  
**Presence:** | Optional. However, you must include at least one of the following: `<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<JSONPayload>`, or `<XMLPayload>.`  
**Type:** | N/A  
  
### <JSONPayload>/<Variable> element

(Required within the JSONPayload element.) Specifies the variable where the extracted value is assigned. You can include multiple `<Variable>` tags in the `<JSONPayload>` element to populate multiple variables.
    
    
    <Variable name="name" type="string">
       <JSONPath>{example}</JSONPath>
    </Variable>

**Default:** | N/A  
---|---  
**Presence:** | Required within the JSONPayload element.   
**Type:** | N/A  
  
#### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
name |  Specifies the name of the variable to which the extracted value will be assigned.  |  name | Required | String  
type | Specifies the data type of the variable value. | N/A | Optional |  String. Select from:

  * string
  * boolean
  * integer
  * long
  * float
  * double
  * nodeset (returns JSON fragment)

  
  
###  <JSONPayload>/<Variable>/<JSONPath> element

(Required within the JSONPayload:Variable element.) Specifies the JSON path used to extract a value from a JSON-formatted message. 

**Note:** The `<JSONPath>` element supports the dynamic string substitution feature called [message templating](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro). 
    
    
    <Variable name="name">
      <JSONPath>$.rss.channel.title</JSONPath>
    </Variable>

**Default:** | N/A  
---|---  
**Presence:** | Required  
**Type:** | String  
  
## <XMLPayload> element

(Optional, but see the Presence row in the table below for more information.) Specifies the XML-formatted message from which the value of the variable will be extracted. XML payloads are extracted only when the `Content-Type` header of the message is `text/xml`, `application/xml`, or `application/*+xml`.
    
    
    <XMLPayload stopPayloadProcessing="false">
      <Namespaces>
        <Namespace prefix="apigee">http://www.apigee.com</Namespace>
        <Namespace prefix="gmail">http://mail.google.com</Namespace>
      </Namespaces>
      <Variable name="name" type="boolean">
        <XPath>/apigee:test/apigee:example</XPath>
      </Variable>
    </XMLPayload>

**Default:** | N/A  
---|---  
**Presence:** | Optional. However, you must include at least one of the following: `<URIPath>`, `<QueryParam>`, `<Header>`, `<FormParam>`, `<JSONPayload>`, or `<XMLPayload>.`  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
`stopPayloadProcessing` |  Set to `true` to stop XPath evaluation after one variable is populated. This means only a single variable is populated by the policy. |  false | Optional | Boolean  
  
### <XMLPayload>/<Namespaces> element

(Optional) Specifies the namespace to be used in the XPath evaluation. If you're using namespaces in your XPath expressions, you must declare the namespaces here, as shown in the following example.
    
    
    <XMLPayload stopPayloadProcessing="false">
      <Namespaces>
         <Namespace prefix="apigee">http://www.apigee.com</Namespace>
         <Namespace prefix="gmail">http://mail.google.com</Namespace>
      </Namespaces>
      <Variable name="legName" type="string">
        <XPath>/apigee:Directions/apigee:route/apigee:leg/apigee:name</XPath>
      </Variable>
    </XMLPayload>

If you are not using namespaces in your XPath expressions, you can omit or comment out the `<Namespaces>` element, as the following example shows:
    
    
    <XMLPayload stopPayloadProcessing="false">
      <!-- <Namespaces/> -->
      <Variable name="legName" type="string">
        <XPath>/Directions/route/leg/name</XPath>
      </Variable>
    </XMLPayload>

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | String  
  
#### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
`prefix` |  The namespace prefix. |  N/A | Required | String  
  
### <XMLPayload>/<Variable> element

(Optional) Specifies variable to which the extracted value will be assigned.
    
    
    <Variable name="name" type="boolean">
       <XPath>/test/example</XPath>
    </Variable>

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | N/A  
  
#### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
name |  Specifies the name of the variable to which the extracted value will be assigned.  |  name | Required | String  
type | Specifies the data type of the variable value. | Boolean | Optional |  String. Select from:

  * string
  * boolean
  * integer
  * long
  * float
  * double
  * nodeset (returns an XML fragment)

  
  
###  <XMLPayload>/<Variable>/<XPath> element

(Required within the XMLPayload:Variable element.) Specifies the XPath defined for the variable. Only XPath 1.0 expressions are supported.

The `<XPath>` element does not support [message templating](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro).
    
    
    <Variable name="name" type="boolean">
       <XPath>/test/example</XPath>
    </Variable>

Example with a namespace. If you use namespaces in your XPath expressions, you must declare the namespaces in the `<XMLPayload><Namespaces>` section of the policy.
    
    
    <Variable name="name" type="boolean">
       <XPath>/foo:test/foo:example</XPath>
    </Variable>

**Default:** | N/A  
---|---  
**Presence:** | Required  
**Type:** | String  
**Note:** Using `parent`, `ancestor`, `following`, and `preceding` in XPath expressions is not supported in Apigee. To get the same matching results, try explicit node name matching or indexing. For example: 

  * `<XPath>/Attributes/Attribute[@Name=’foo_attribute']/Value</XPath>`  
gets the value of `foo_attribute`.
  * `<XPath>/Attributes/Attribute[4]/Value</XPath>`  
gets the value of the 4th attribute.



## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information.

Fault code | HTTP status | Cause | Fix  
---|---|---|---  
`steps.extractvariables.ExecutionFailed` | `500` |  This error occurs when: 

  * The input payload (JSON, XML) is empty.
  * The input (JSON, XML, etc) passed to the policy is invalid or malformed.

| [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/extract-variables-runtime-errors#executionfailed)  
`steps.extractvariables.ImmutableVariable` | `500` | A variable used in the policy is immutable. The policy was unable to set this variable. | N/A  
`steps.extractvariables.InvalidJSONPath` | `500` | This error occurs if an invalid JSON path is used in the `JSONPath` element of the policy. For example, if a JSON payload does not have the object `Name`, but you specify `Name` as the path in the policy, then this error occurs. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/extract-variables-runtime-errors#invalidjsonpath)  
`steps.extractvariables.JsonPathParsingFailure` | `500` | This error occurs when the policy is unable to parse a JSON path and extract data from the flow variable specified in `Source` element. Typically this happens if the flow variable specified in the `Source` element does not exist in the current flow. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/extract-variables-runtime-errors#jsonpathparsingfailure)  
`steps.extractvariables.SetVariableFailed` | `500` | This error occurs if the policy could not set the value to a variable. The error generally happens if you try to assign values to multiple variables whose names start with the same words in a nested dot-separated format. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/extract-variables-runtime-errors#setvariablefailed)  
`steps.extractvariables.SourceMessageNotAvailable` | `500` | This error occurs if the [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#messagevariables) variable specified in the [`Source` element](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy#sourceelement) of the policy is either: 

  * Out of scope (not available in the specific flow where the policy is being executed) or
  * Can't be resolved (is not defined)

| [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/extract-variables-runtime-errors#sourcemessagenotavailable)  
`steps.extractvariables.UnableToCast` | `500` | This error occurs if the policy was unable to cast the extracted value to a variable. Typically this happens if you attempt to set the value of one data type to a variable of another data type.  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/extract-variables-runtime-errors#unabletocast)  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

**Tip:** Need help resolving an error? Click _build_ next to the error's cause description to visit the troubleshooting page. Error name | Cause | Fix  
---|---|---  
`NothingToExtract` | If the policy does not have any of the elements `URIPath`, `QueryParam`, `Header`, `FormParam`, `XMLPayload`, or `JSONPayload`, the deployment of the API Proxy fails, because there's nothing to extract. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/extract-variables-deployment-errors#nothingtoextract)  
`NONEmptyPrefixMappedToEmptyURI` | This error occurs if the policy has a prefix defined in the `Namespace` element under the `XMLPayload` element, but no URI is defined. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/extract-variables-deployment-errors#nonemptyprefixmappedtoemptyuri)  
`DuplicatePrefix` | This error occurs if the policy has the same prefix defined more than once in the `Namespace` element under the `XMLPayload` element. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/extract-variables-deployment-errors#duplicateprefix)  
`NoXPathsToEvaluate` | If the policy does not have the `XPath` element within the `XMLPayload` element, then the deployment of the API proxy fails with this error.  If you want to extract variables from an XML Payload, then an `XPath` child element must be specified. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/extract-variables-deployment-errors#noxpathstoevaluate)  
`EmptyXPathExpression` | If the policy has an empty `XPath` expression within the `XMLPayload` element, then the deployment of the API proxy fails. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/extract-variables-deployment-errors#emptyxpathexpression)  
`NoJSONPathsToEvaluate` | If the policy does not have the `JSONPath` element within the `JSONPayload` element, then the deployment of the API proxy fails with this error. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/extract-variables-deployment-errors#nojsonpathstoevaluate)  
`EmptyJSONPathExpression` | If the policy has an empty `XPath` expression within the `XMLPayload` element, then the deployment of the API proxy fails. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/extract-variables-deployment-errors#emptyjsonpathexpression)  
`MissingName` | If the policy does not have the `name` attribute in any of the policy elements like `QueryParam`, `Header`, `FormParam` or `Variable`, where it is required, then the deployment of the API proxy fails. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/extract-variables-deployment-errors#missingname)  
`PatternWithoutVariable` | If the policy does not have a variable specified within the `Pattern` element, then the deployment of the API proxy fails. The `Pattern` element requires the name of the variable in which extracted data will be stored. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/extract-variables-deployment-errors#patternwithoutvariable)  
`CannotBeConvertedToNodeset` | If the policy has an `XPath` expression where the `Variable` type is defined as [nodeset](https://docs.microsoft.com/en-us/dotnet/standard/data/xml/node-sets-in-transformations), but the expression cannot be converted to nodeset, then the deployment of the API proxy fails. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/extract-variables-deployment-errors#cannotbeconvertedtonodeset)  
`JSONPathCompilationFailed` | The policy could not compile a specified JSON Path. | N/A  
`InstantiationFailed` | The policy could not be instantiated. | N/A  
`XPathCompilationFailed` | If the prefix or the value used in the `XPath` element is not part of any of the declared namespaces in the policy, then the deployment of the API proxy fails. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/extract-variables-deployment-errors#xpathcompilationfailed)  
`InvalidPattern` | If the `Pattern` element definition is invalid in any of the elements like `URIPath`, `QueryParam`, `Header`, `FormParam`, `XMLPayload` or `JSONPayload` within the policy, then the deployment of the API proxy fails. The `Pattern` element is considered invalid if it doesn't include a variable. For more information about pattern matching, see [About matching and variable creation](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy#about-matching-variable-creation). | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/extract-variables-deployment-errors#invalidpattern)  
  
### Fault variables

These variables are set when this policy triggers an error at runtime. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name = "SourceMessageNotAvailable"`  
`extractvariables.policy_name.failed` | policy_name is the user-specified name of the policy that threw the fault. | `extractvariables.EV-ParseJsonResponse.failed = true`  
  
### Example error response

**Note:** For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.
    
    
    {
       "fault":{
          "detail":{
             "errorcode":"steps.extractvariables.SourceMessageNotAvailable"
          },
          "faultstring":"request message is not available for ExtractVariable: EV-ParseJsonResponse"
       }
    }

### Example fault rule
    
    
    <FaultRule name="Extract Variable Faults">
        <Step>
            <Name>AM-CustomErrorMessage</Name>
            <Condition>(fault.name = "SourceMessageNotAvailable") </Condition>
        </Step>
        <Condition>(extractvariables.EM-ParseJsonResponse.failed = true) </Condition>
    </FaultRule>

## Schemas

**Sample:** See our [GitHub repository](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) samples for the most recent schemas.

## Related topics

[Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
