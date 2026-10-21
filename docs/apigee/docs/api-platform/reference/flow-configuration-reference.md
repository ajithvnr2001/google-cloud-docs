---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference/
title: Flow configuration reference \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:25:32.197978+00:00
---

# Flow configuration reference  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Flow configuration reference Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section provides reference information about the XML elements you use to define your API proxy flows.

### More information

  * [Control proxy execution with flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows)
  * [API Proxy Configuration Reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference)



##  Hierarchy & syntax

The following examples show the element hierarchy and syntax of the flow configuration elements:

### Element Hierarchy

The following example shows the hierarchy of the flow configuration elements within the [`<ProxyEndpoint>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint) and [`<TargetEndpoint>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#targetendpoint) elements:
    
    
    <ProxyEndpoint | TargetEndpoint>
        subdirectory_arrow_right[<PreFlow>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#preflow)
              subdirectory_arrow_right[<Request>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#request)
                    subdirectory_arrow_right[<Step>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step)
                        subdirectory_arrow_right[<Condition>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#condition)
                        subdirectory_arrow_right[<Name>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#name)
              subdirectory_arrow_right[<Response>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response)
                    subdirectory_arrow_right[<Step>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step)
                        subdirectory_arrow_right[<Condition>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#condition)
                        subdirectory_arrow_right[<Name>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#name)
              subdirectory_arrow_right[<Description>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description)
        subdirectory_arrow_right[<Flows>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flows)
              subdirectory_arrow_right[<Flow>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flow)
                    subdirectory_arrow_right[<Description>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description)
                    subdirectory_arrow_right[<Condition>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#condition)
                    subdirectory_arrow_right[<Request>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#request)
                          subdirectory_arrow_right[<Step>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step)
                              subdirectory_arrow_rightmore_horiz
                    subdirectory_arrow_right[<Response>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response)
                          subdirectory_arrow_right[<Step>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step)
                              subdirectory_arrow_rightmore_horiz
              subdirectory_arrow_right[<Description>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description)
        subdirectory_arrow_right[<PostFlow>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#postflow)
              subdirectory_arrow_right[<Request>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#request)
                    subdirectory_arrow_right[<Step>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step)
                        subdirectory_arrow_rightmore_horiz
              subdirectory_arrow_right[<Response>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response)
                    subdirectory_arrow_right[<Step>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step)
                        subdirectory_arrow_rightmore_horiz
              subdirectory_arrow_right[<Description>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description)
        subdirectory_arrow_rightEventFlow
              subdirectory_arrow_right[<Response>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response)
                    subdirectory_arrow_right[<Step>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step)
                        subdirectory_arrow_rightmore_horiz
              subdirectory_arrow_right[<Description>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description)
        subdirectory_arrow_right[<PostClientFlow>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#postclientflow) (<ProxyEndpoint> only)
              subdirectory_arrow_right[<Response>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response)
                    subdirectory_arrow_rightmore_horiz
              subdirectory_arrow_right[<Description>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description)
    
        more_horiz  // [Additional configuration elements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference)
    
    </ProxyEndpoint | TargetEndpoint>

### Syntax

The following example shows the syntax for the flow configuration elements. Each of these elements is described in detail in the sections that follow:
    
    
    <!-- ProxyEndpoint flow configuration file -->
    <ProxyEndpoint ... >
      ...
      <PreFlow name="flow_name">
        <Description>flow_description</Description>
        <Request>
          <Step>
            <Condition>property operator "value"</Condition>
            <Name>policy_name</Name>
          </Step>
          ...
        </Request>
        <Response>
          <Step>
            <Condition>property operator "value"</Condition>
            <Name>policy_name</Name>
          </Step>
          ...
        </Response>
      </PreFlow>
      <Flows name="flow_name">
        <Flow name="conditional_flow_name">
          <Description>flow_description</Description>
          <Condition>property operator "value"</Condition>
          <Request>
            <Step>
              <Condition>property operator "value"</Condition>
              <Name>policy_name</Name>
            </Step>
            ...
          </Request>
          <Response>
            <Step>
              <Condition>property operator "value"</Condition>
              <Name>policy_name</Name>
            </Step>
            ...
          </Response>
        </Flow>
      </Flows>
      <PostFlow name="flow_name">
        <Description>flow_description</Description>
        <Request>
          <Step>
            <Condition>property operator "value"</Condition>
            <Name>policy_name</Name>
          </Step>
          ...
        </Request>
        <Response>
          <Step>
            <Condition>property operator "value"</Condition>
            <Name>policy_name</Name>
          </Step>
          ...
        </Response>
      </PostFlow>
      <PostClientFlow name="flow_name">
        <Description>flow_description</Description>
        <Response>
          <Step>
            <Condition>property operator "value"</Condition>
            <Name>policy_name</Name>
          </Step>
          ...
        </Response>
      </PostClientFlow>
      ...
    </ProxyEndpoint>
    
    <!-- TargetEndpoint flow configuration file -->
    <TargetEndpoint ... >
      ...
      <PreFlow name="flow_name">
        <Description>flow_description</Description>
        <Request>
          <Step>
            <Condition>property operator "value"</Condition>
            <Name>policy_name</Name>
          </Step>
          ...
        </Request>
        <Response>
          <Step>
            <Condition>property operator "value"</Condition>
            <Name>policy_name</Name>
          </Step>
          ...
        </Response>
      </PreFlow>
      <Flows name="flow_name">
        <Flow name="conditional_flow_name">
          <Description>flow_description</Description>
          <Condition>property operator "value"</Condition>
          <Request>
            <Step>
              <Condition>property operator "value"</Condition>
              <Name>policy_name</Name>
            </Step>
            ...
          </Request>
          <Response>
            <Step>
              <Condition>property operator "value"</Condition>
              <Name>policy_name</Name>
            </Step>
            ...
          </Response>
        </Flow>
        ...
      </Flows>
      <PostFlow name="flow_name">
        <Description>flow_description</Description>
        <Request>
          <Step>
            <Condition>property operator "value"</Condition>
            <Name>policy_name</Name>
          </Step>
          ...
        </Request>
        <Response>
          <Step>
            <Condition>property operator "value"</Condition>
            <Name>policy_name</Name>
          </Step>
          ...
        </Response>
      </PostFlow>
      ...
    </TargetEndpoint>

You use these elements to define your PreFlow, Conditional Flow, PostFlow, EventFlow, and PostClientFlow execution.

### Other configuration elements

This section does not cover the following elements that are used in proxy configuration:

  * `<APIProxy>`
  * `<DefaultFaultRule>`
  * `<FaultRules>`
  * `<HTTPProxyConnection>`
  * `<ProxyEndpoint>`
  * `<RouteRule>`
  * `<TargetEndpoint>`



These elements, which define the _proxy_ configuration and not the flows, are discussed in the [API Proxy Configuration Reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference).

## `<Condition>`

Defines a statement that is processed at runtime. If the statement evaluates to true, then the step or flow associated with the condition is executed. If the statement evaluates to false, then the step or flow is ignored.

**Type** | String  
---|---  
**Parent Element(s)** |  [`<Flow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flow)  
[`<Step>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step)  
  
**Child Element(s)** |  None   
  
You can apply a condition to a specific step or to an entire flow, depending on whether you put the element in the [`<Flow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flow) or [`<Step>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step) element:
    
    
    // Condition can apply to just **one step** :        // Or to the flow:
    <Flows>                                         <Flows>
      <Flow>                                          <Flow>
        <Step>                                          **< Condition>**
          **< Condition>**                                   <Step>
          <Name>                                          <Name>
          ...                                             ...
        ...                                             ...
      ...                                             ...
    </Flows>                                        </Flows>

If a condition within a `<Step>` evaluates to true, Apigee executes that step. If the condition evaluates to false, Apigee skips the step.

If a condition within a `<Flow>` evaluates to true, Apigee processes all the steps in the flow. If the condition evaluates to false, Apigee skips the entire flow.

### Syntax

The `<Condition>` element uses the following syntax:
    
    
    <Condition>property operator "value"</Condition>

Where:

property
    The flow variable property that you want to use in your condition. For example, the [`request`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#request) flow variable has properties named `path` and `content`. To use them in a condition, you specify the flow_variable[dot]property_name: 
    
    
    request.path
    request.content

For a complete list of flow variables and their properties, see [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

operator
    A construct that defines how your condition is evaluated. Common operators include: 
    
    
    >     greater than           <=    less than or equal to
    <     less than              >=    greater than or equal to
    =     equals                 &&    and
    !=    not equals             ||    or
    
    ~~    JavaRegex
    ~     Matches
    /~    MatchesPath

For a complete list, see [Operators](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference#operators) in the Conditions reference.

"value"
    The value against which the flow variable property is evaluated. This is commonly a basic type such as an integer or string. For example, `200` or `/cat`. The value can include wildcards, such as asterisks and other characters for pattern matching, as described in [Pattern matching with conditionals](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions#patternmatching).

### Example 1

The following example checks if the [`request`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#request) flow variable's `verb` property is `GET`:
    
    
    <!-- api-platform/reference/examples/flow-segments/condition-1.xml -->
    <ProxyEndpoint name="default">
      <PreFlow name="my-preFlows">
        <Description>My first PreFlow</Description>
        <Request>
          <Step>
            <Condition>request.verb = "GET"</Condition>
            <Name>Log-Request-OK</Name>
          </Step>
        </Request>
      </PreFlow>
      ...
    </ProxyEndpoint>

If the request is a `GET`, then this example executes the `Log-Request-OK` policy.

### Example 2

The following example checks for the response code:
    
    
    <!-- api-platform/reference/examples/flow-segments/condition-2.xml -->
    <ProxyEndpoint name="default">
      <PreFlow name="my-preFlows">
        <Description>My first PreFlow</Description>
        <Response>
          <Step>
            <Condition>response.status.code LesserThanOrEquals 300</Condition>
            <Name>Log-Response-OK</Name>
          </Step>
          <Step>
            <Condition>response.status.code GreaterThan 300</Condition>
            <Name>Log-Response-NOT-OK</Name>
          </Step>
        </Response>
      </PreFlow>
      ...
    </ProxyEndpoint>

Depending on the value of the code, a different policy is executed.

#### Attributes

The `<Condition>` element has no attributes.

#### Child Elements

The `<Condition>` element has no child elements.

## `<Description>`

Describes the flow in human-readable terms. Use this element to provide information about the flow to yourself or other developers. The description is not externally visible.

**Type** | String  
---|---  
**Parent Element(s)** |  [`<Flow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flow)  
[`<PreFlow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#preflow)  
[`<PostFlow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#postflow)  
  
**Child Element(s)** |  None   
  
### Syntax

The `<Description>` element uses the following syntax:
    
    
    <Description>flow_description</Description>

### Example

The following example shows a `<Description>` element that specifies the purpose of a flow:
    
    
    <!-- api-platform/reference/examples/flow-segments/description-1.xml -->
    <ProxyEndpoint name="default">
      <Flows name="my-conditional-flows">
        <Flow name="reports">
          <Request>
            <Description>Based on the path suffix, determine which flow to use</Description>
            <Step>
              <Condition>proxy.pathsuffix MatchesPath "/reports"</Condition>
              <Name>XML-to-JSON-1</Name>
            </Step>
            <Step>
              <Condition>proxy.pathsuffix MatchesPath "/forecasts"</Condition>
              <Name>XML-to-JSON-1</Name>
            </Step>
          </Request>
        </Flow>
      </Flows>
      ...
    </ProxyEndpoint>

#### Attributes

The `<Description>` element has no attributes.

#### Child Elements

The `<Description>` element has no child elements.

## `<Flow>`

Defines a custom set of steps that Apigee executes.

**Type** | Complex object  
---|---  
**Parent Element(s)** |  [`<Flows>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flows)  
  
**Child Element(s)** |  [`<Condition>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#condition)  
[`<Description>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description)  
[`<Request>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#request)  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response)  
  
  
You can optionally specify a [`<Condition>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#condition) on a `<Flow>`. In that case, Apigee only executes the steps in the flow if the condition evaluates to true. Otherwise, Apigee skips the entire flow.

A [`<Flows>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flows) element can contain multiple `<Flow>` elements, each with its own condition and steps. When there are multiple `<Flow>` elements, Apigee executes only the first one in which there is no condition or the condition evaluates to true.

You can define a default flow that always executes (if none of the other conditional flows do). Depending on how your API proxy is configured, this can be a useful tool in [protecting against malicious attacks](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows#defaultflow).

### Syntax

The `<Flow>` element uses the following syntax:
    
    
    <Flow name="conditional_flow_name">
      <Description>flow_description</Description>
      <Condition>property operator "value"</Condition>
      <Request>
        <Step>
          <Condition>property operator "value"</Condition>
          <Name>policy_name</Name>
        </Step>
        ...
      </Request>
      <Response>
        <Step>
          <Condition>property operator "value"</Condition>
          <Name>policy_name</Name>
        </Step>
        ...
      </Response>
    </Flow>

All child elements of `<Flow>` are optional.

### Example 1

The following example shows a simple `<Flow>` that always executes the "Log-Message-OK" policy:
    
    
    <!-- api-platform/reference/examples/flow-segments/flow-1.xml -->
    <ProxyEndpoint name="default">
      <Flows name="my-flow">
        <Flow>
          <Request>
            <Step>
              <Name>Log-Message-OK</Name>
            </Step>
          </Request>
        </Flow>
      </Flows>
      ...
    </ProxyEndpoint>

### Example 2

The following example shows a `<Flow>` with multiple steps, each with its own condition:
    
    
    <!-- api-platform/reference/examples/flow-segments/flow-2.xml -->
    <ProxyEndpoint name="default">
      <Flows name="my-conditional-flows">
        <Flow name="reports">
          <Request>
            <Description>Based on the path suffix, determine which flow to use</Description>
            <Step>
              <Condition>proxy.pathsuffix MatchesPath "/reports"</Condition>
              <Name>XML-to-JSON-1</Name>
            </Step>
            <Step>
              <Condition>proxy.pathsuffix MatchesPath "/forecasts"</Condition>
              <Name>Verify-Auth-1</Name>
            </Step>
          </Request>
        </Flow>
      </Flows>
      ...
    </ProxyEndpoint>

### Example 3

The following example shows multiple flows in a Conditional Flow:
    
    
    <!-- api-platform/reference/examples/flow-segments/flows-2.xml -->
    <ProxyEndpoint name="default">
      <Flows>
        <Flow name="my-flow-1">
          <Response>
            <Step>
              <Condition>response.status.code = 200</Condition>
              <Name>Assign-Message-1</Name>
            </Step>
          </Response>
        </Flow>
        <Flow name="my-flow-2">
          <Response>
            <Step>
              <Condition>response.status.code >= 400</Condition>
              <Name>Assign-Message-2</Name>
            </Step>
          </Response>
        </Flow>
        <Flow name="my-flow-3">
          <Response>
            <Step>
              <Condition>response.status.code >= 300</Condition>
              <Name>Assign-Message-3</Name>
            </Step>
          </Response>
        </Flow>
      </Flows>
      ...
    </ProxyEndpoint>

Apigee executes only one flow in a segment; it executes the first flow which does not have a condition, or whose condition resolves to true.

#### Attributes

The following table describes the attributes of the `<Flow>` element:

Attribute | Type | Description  
---|---|---  
`name` | String | **(Required)** A unique ID for the flow. For example, `My-Conditional-Flow-1`. The name cannot contain spaces or other special characters.  
  
#### Child Elements

The following table describes the child elements of `<Flow>`:

Child Element | Type | Description  
---|---|---  
[`<Condition>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#condition) | String | Defines a conditional statement that is processed at runtime. If the statement evaluates to true, then the flow (and all its steps) are executed. If the statement evaluates to false, then the flow (and all its steps) are ignored.  
[`<Description>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description) | String | Provides a brief description of the flow. This description is not externally visible.  
[`<Request>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#request) | Complex object | Specifies steps and conditions for the request segment.  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response) | Complex object | Specifies steps and conditions for the response segment.  
  
## `<Flows>`

Contains zero or more [`<Flow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flow) elements.

**Type** | Complex object  
---|---  
**Parent Element(s)** |  [`<ProxyEndpoint>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint)  
[`<TargetEndpoint>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#targetendpoint)  
  
**Child Element(s)** |  [`<Flow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flow)  
  
  
If there are multiple `<Flow>` elements within `<Flows>`, only one `<Flow>` will execute. This will be the first flow that either doesn't have a [`<Condition>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#condition), or whose condition resolves to true.

You can define a default flow that always executes (if none of the other flows do). Depending on how your API proxy is configured, this can be a useful tool in [protecting against malicious attacks](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows#defaultflow).

### Syntax

The `<Flows>` element uses the following syntax:
    
    
    <Flows name="flow_name">
      <Flow name="conditional_flow_name">
        <Description>flow_description</Description>
        <Condition>property operator "value"</Condition>
        <Request>
          <Step>
            <Condition>property operator "value"</Condition>
            <Name>policy_name</Name>
          </Step>
          ...
        </Request>
        <Response>
          <Step>
            <Condition>property operator "value"</Condition>
            <Name>policy_name</Name>
          </Step>
          ...
        </Response>
      </Flow>
    </Flows>

All child elements of `<Flows>` are optional.

### Example 1

The following example shows a simple `<Flows>` element with a single `<Flow>`:
    
    
    <!-- api-platform/reference/examples/flow-segments/flows-1.xml -->
    <ProxyEndpoint name="default">
      <Flows name="my-conditional-flows">
        <Flow name="reports">
          <Request>
            <Description>Based on the path suffix, determine which flow to use</Description>
            <Step>
              <Condition>proxy.pathsuffix MatchesPath "/reports"</Condition>
              <Name>XML-to-JSON-1</Name>
            </Step>
            <Step>
              <Condition>proxy.pathsuffix MatchesPath "/forecasts"</Condition>
              <Name>Verify-Auth-1</Name>
            </Step>
          </Request>
        </Flow>
      </Flows>
      ...
    </ProxyEndpoint>

Apigee executes one of these policies based on the path suffix that it gathers from the [`proxy`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#proxy) flow variable. If the path suffix matches neither of the conditions, then Apigee does not execute this flow.

### Example 2

The following example shows multiple `<Flow>` elements within `<Flows>`, each with its own [`<Condition>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#condition):
    
    
    <!-- api-platform/reference/examples/flow-segments/flows-2.xml -->
    <ProxyEndpoint name="default">
      <Flows>
        <Flow name="my-flow-1">
          <Response>
            <Step>
              <Condition>response.status.code = 200</Condition>
              <Name>Assign-Message-1</Name>
            </Step>
          </Response>
        </Flow>
        <Flow name="my-flow-2">
          <Response>
            <Step>
              <Condition>response.status.code >= 400</Condition>
              <Name>Assign-Message-2</Name>
            </Step>
          </Response>
        </Flow>
        <Flow name="my-flow-3">
          <Response>
            <Step>
              <Condition>response.status.code >= 300</Condition>
              <Name>Assign-Message-3</Name>
            </Step>
          </Response>
        </Flow>
      </Flows>
      ...
    </ProxyEndpoint>

Apigee executes only the first flow in a segment whose condition evaluates to true. After that, Apigee skips the remaining flows in the segment.

### Example 3

The following example shows a "default" `<Flow>`:
    
    
    <!-- api-platform/reference/examples/flow-segments/flows-3.xml -->
    <ProxyEndpoint name="default">
      <Flows>
        <Flow name="my-conditional-flow-1">
          <Response>
            <Step>
              <Condition>response.status.code = 200</Condition>
              <Name>Assign-Message-1</Name>
            </Step>
          </Response>
        </Flow>
        <Flow name="my-conditional-flow-2">
          <Response>
            <Step>
              <Condition>response.header.someheader = "42"</Condition>
              <Name>Assign-Message-2</Name>
            </Step>
          </Response>
        </Flow>
        <Flow name="my-default-flow">
          <Response>
            <Step>
              <Name>Assign-Message-3</Name>
            </Step>
          </Response>
        </Flow>
      </Flows>
      ...
    </ProxyEndpoint>

Apigee executes only the first flow in a segment whose condition evaluates to true. If no conditional flows execute, then the third flow in this example (with no condition) executes.

A default flow can be a useful tool in [protecting against malicious attacks](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows#defaultflow).

#### Attributes

The `<Flows>` element has no attributes.

#### Child Elements

The `<Flows>` element has the following child elements:

Child Element | Type | Description  
---|---|---  
[`<Flow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flow) | Complex object | A flow that defines one possible set of steps within the Conditional Flow.  
  
## `<Name>`

Specifies the ID of the policy to execute within a [`<Flow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flow).

**Type** | String  
---|---  
**Parent Element(s)** |  [`<Step>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step)  
  
**Child Element(s)** |  None   
  
### Syntax

The `<Name>` element uses the following syntax:
    
    
    <Name>policy_name</Name>

### Example

The following example shows two policies that are added to flows by their name:
    
    
    <!-- api-platform/reference/examples/flow-segments/name-1.xml -->
    <ProxyEndpoint name="default">
      <Flows name="my-conditional-flows">
        <Flow name="reports">
          <Request>
            <Description>Based on the path suffix, determine which flow to use</Description>
            <Step>
              <Condition>proxy.pathsuffix MatchesPath "/reports"</Condition>
              <Name>XML-to-JSON-1</Name>
            </Step>
            <Step>
              <Condition>proxy.pathsuffix MatchesPath "/forecasts"</Condition>
              <Name>Verify-Auth-1</Name>
            </Step>
          </Request>
        </Flow>
      </Flows>
      ...
    </ProxyEndpoint>

#### Attributes

The `<Name>` element has no attributes.

#### Child Elements

The `<Name>` element has no child elements.

## `<PostFlow>`

Defines the steps to take in the PostFlow of the request and response.

**Type** | Complex object  
---|---  
**Parent Element(s)** |  [`<ProxyEndpoint>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint)  
[`<TargetEndpoint>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#targetendpoint)  
  
**Child Element(s)** |  [`<Description>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description)  
[`<Request>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#request)  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response)  
  
  
The `<PostFlow>` element uses the following syntax:

### Syntax
    
    
    <PostFlow name="flow_name">
      <Description>flow_description</Description>
      <Request>
        <Step>
          <Condition>property operator "value"</Condition>
          <Name>policy_name</Name>
        </Step>
        ...
      </Request>
      <Response>
        <Step>
          <Condition>property operator "value"</Condition>
          <Name>policy_name</Name>
        </Step>
        ...
      </Response>
    </PostFlow>

### Example

The following example shows a PostFlow with steps for both the request and response defined:
    
    
    <!-- api-platform/reference/examples/flow-segments/postflow-1.xml -->
    <ProxyEndpoint name="default">
      <PostFlow name="my-postflows">
        <Description>My first PostFlow</Description>
        <Request>
          <Step>
            <Condition>request.verb = "GET"</Condition>
            <Name>Log-Request-OK</Name>
          </Step>
        </Request>
        <Response>
          <Step>
            <Name>Set-Response-Headers</Name>
          </Step>
        </Response>
      </PostFlow>
      ...
    </ProxyEndpoint>

#### Attributes

The following table describes the attributes of the `<PostFlow>` element:

Attribute | Type | Description  
---|---|---  
`name` | String | A unique ID for the flow (unique within the endpoint). For example, `My-PostFlow-1`. The value cannot include spaces or other special characters.  
  
#### Child Elements

The following table describes the child elements of `<PostFlow>`:

Child Element | Type | Description  
---|---|---  
[`<Description>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description) | String | Provides a brief description of the flow.  
[`<Request>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#request) | Complex object | Defines the policies to execute during the request's PostFlow.  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response) | Complex object | Defines the policies to execute during the response's PostFlow.  
  
## <EventFlow>

Defines the steps to take in the `EventFlow`. `EventFlow` is used to support streaming server-sent events. For more information, see [Streaming server-sent events](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events). 

**Type** | Complex object  
---|---  
**Parent Element(s)** |  [`<TargetEndpoint>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#targetendpoint)  
  
**Child Element(s)** |  [`<Description>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description)  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response)  
  
  
The `EventFlow` element uses the following syntax:

### Syntax
    
    
      <EventFlow name="flow_name" content-type="text/event-stream">>
        <Description>flow_description</Description>
        <Response>
          <Step>
            <Name>policy_name</Name>
          </Step>
        </Response>
      </EventFlow>

### Example

The following example shows a EventFlow:
    
    
    <TargetEndpoint name="default">
      <EventFlow name="EF-1" content-type="text/event-stream">
        <Response>
          <Step>
            <Name>Raise-Fault-Cred-Invalid</Name>
            <Condition>fault.name equals "invalid_access_token"</Condition>
          </Step>
        </Response>
      </EventFlow>
      <HTTPTargetConnection>
    </TargetEndpoint></pre>

#### Attributes

The following table describes the attributes of the EventFlow element:

Attribute | Type | Description  
---|---|---  
`name` | String | A unique ID for the flow (unique within the endpoint). For example, `My-EventFlow-1`. The value cannot include spaces or other special characters.  
`content-type` | String | (Required) Must be set to: `content-type="text/event-stream"`  
  
#### Child Elements

The following table describes the child elements of EventFlow:

Child Element | Type | Description  
---|---|---  
[`<Description>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description) | String | Provides a brief description of the flow.  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response) | Complex object | Defines the policies to execute during the response's EventFlow.  
  
## `<PostClientFlow>`

Defines policies in the ProxyEndpoint that execute only after a response has been returned to the client. These policies typically log messages related to the response.

**Type** | Complex object  
---|---  
**Parent Element(s)** |  [`<ProxyEndpoint>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint)  
  
**Child Element(s)** |  [`<Description>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description)  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response)  
  
  
### Syntax

The `<PostClientFlow>` element uses the following syntax:
    
    
    <PostClientFlow name="flow_name">
      <Description>flow_description</Description>
      <Response>
        <Step>
          <Condition>property operator "value"</Condition>
          <Name>policy_name</Name>
        </Step>
        ...
      </Response>
    </PostClientFlow>

All child elements of `<PostClientFlow>` are optional.

### Example

The following example shows a simple PostClientFlow that executes a single policy:
    
    
    <!-- api-platform/reference/examples/flow-segments/postclientflow-1.xml -->
    <ProxyEndpoint name="default">
      <PostClientFlow name="my-postclientflows">
        <Description>My first PostClientFlow. Processed after the response is sent back to the client.</Description>
        <Response>
          <Step>
            <Name>Message-Logging-OK</Name>
          </Step>
        </Response>
      </PostClientFlow>
      ...
    </ProxyEndpoint>

#### Attributes

The following table describes the attributes of the `<PostClientFlow>` element:

Attribute | Type | Description  
---|---|---  
`name` | String | A unique ID for the flow. The name cannot include spaces or other special characters. For example, `My-PostClientFlow-1`.  
  
#### Child Elements

The following table describes the child elements of `<PostClientFlow>`:

Child Element | Type | Description  
---|---|---  
[`<Description>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description) | String | Provides a brief description of the flow.  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response) | Complex object | Defines the policies to execute during the response's PostFlow.  
  
## `<PreFlow>`

Defines the policies to execute in the PreFlow of the request and response.

**Type** | Complex object  
---|---  
**Parent Element(s)** |  [`<ProxyEndpoint>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint)  
[`<TargetEndpoint>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#targetendpoint)  
  
**Child Element(s)** |  [`<Description>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description)  
[`<Request>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#request)  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response)  
  
  
### Syntax

The `<PreFlow>` element uses the following syntax:
    
    
    <PreFlow name="flow_name">
      <Description>flow_description</Description>
      <Request>
        <Step>
          <Condition>property operator "value"</Condition>
          <Name>policy_name</Name>
        </Step>
        ...
      </Request>
      <Response>
        <Step>
          <Condition>property operator "value"</Condition>
          <Name>policy_name</Name>
        </Step>
        ...
      </Response>
    </PreFlow>

All child elements of `<PreFlow>` are optional.

### Example

The following example shows a PreFlow with a request and a response flow defined:
    
    
    <!-- api-platform/reference/examples/flow-segments/preflow-1.xml -->
    <ProxyEndpoint name="default">
      <PreFlow name="my-preFlows">
        <Description>My first PreFlow</Description>
        <Request>
          <Step>
            <Condition>request.verb = "GET"</Condition>
            <Name>Log-Request-OK</Name>
          </Step>
        </Request>
        <Response>
          <Step>
            <Condition>response.status.code LesserThanOrEquals 300</Condition>
            <Name>Log-Response-OK</Name>
          </Step>
          <Step>
            <Condition>response.status.code GreaterThan 300</Condition>
            <Name>Log-Response-NOT-OK</Name>
          </Step>
        </Response>
      </PreFlow>
      ...
    </ProxyEndpoint>

#### Attributes

The following table describes the attributes of the `<PreFlow>` element:

Attribute | Type | Description  
---|---|---  
`name` | String | A unique ID for the flow. The name cannot include spaces or other special characters. For example, `My-PreFlow-1`.  
  
#### Child Elements

The following table describes the child elements of `<PreFlow>`:

Child Element | Type | Description  
---|---|---  
[`<Description>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#description) | String | Provides a brief description of the flow.  
[`<Request>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#request) | Complex object | Defines the policies to execute during the request's PreFlow.  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response) | Complex object | Defines the policies to execute during the response's PreFlow.  
  
## `<Request>`

Defines the policies to execute during the request segment of the flow.

**Type** | Complex object  
---|---  
**Parent Element(s)** |  [`<Flow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flow)  
[`<PreFlow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#preflow)  
[`<PostFlow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#postflow)  
  
**Child Element(s)** |  [`<Step>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step)  
  
  
### Syntax

The `<Request>` element uses the following syntax:
    
    
    <Request>
      <Step>
        <Condition>property operator "value"</Condition>
        <Name>policy_name</Name>
      </Step>
      ...
    </Request>

All child elements of `<Request>` are optional.

### Example

The following example shows flows defined for the request in both the PreFlow and PostFlow:
    
    
    <!-- api-platform/reference/examples/flow-segments/request-1.xml -->
    <ProxyEndpoint name="default">
      <PreFlow name="my-preFlows">
        <Description>My first PreFlow</Description>
        <Request>
          <Step>
            <Condition>request.verb = "GET"</Condition>
            <Name>Log-Request-OK</Name>
          </Step>
        </Request>
      </PreFlow>
      <PostFlow name="my-postflows">
        <Description>My first PostFlow</Description>
        <Request>
          <Step>
            <Condition>request.verb = "GET"</Condition>
            <Name>Log-Request-OK</Name>
          </Step>
        </Request>
      </PostFlow>
      ...
    </ProxyEndpoint>

#### Attributes

The `<Request>` element has no attributes.

#### Child Elements

The following table describes the child elements of `<Request>`:

Child Element | Type | Description  
---|---|---  
[`<Step>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step) | String | Specifies a policy to execute within the request segment. This type of child can appear multiple times.  
  
## `<Response>`

Defines the policies to execute during the response segment of the flow. 

**Type** | Complex object  
---|---  
**Parent Element(s)** |  [`<Flow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flow)  
[`<PreFlow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#preflow)  
[`<PostClientFlow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#postclientflow)  
[`<PostFlow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#postflow)  
  
**Child Element(s)** |  [`<Step>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step)  
  
  
### Syntax

The `<Response>` element uses the following syntax:
    
    
    <Response>
      <Step>
        <Condition>property operator "value"</Condition>
        <Name>policy_name</Name>
      </Step>
      ...
    </Response>

All child elements of `<Response>` are optional.

### Example

The following example shows flows defined for the response, in both the PreFlow and PostFlow:
    
    
    <!-- api-platform/reference/examples/flow-segments/response-1.xml -->
    <ProxyEndpoint name="default">
        <PreFlow name="my-preFlows">
            <Description>My first PreFlow</Description>
            <Response>
                <Step>
                    <Condition>response.status.code LesserThanOrEquals 300</Condition>
                    <Name>Log-Response-OK</Name>
                </Step>
                <Step>
                    <Condition>response.status.code GreaterThan 300</Condition>
                    <Name>Log-Response-NOT-OK</Name>
                </Step>
            </Response>
        </PreFlow>
        <PostFlow name="my-postflows">
            <Description>My first PostFlow</Description>
            <Response>
                <Step>
                    <Name>Set-Response-Headers</Name>
                </Step>
            </Response>
        </PostFlow>
      ...
    </ProxyEndpoint>

#### Attributes

The `<Response>` element has no attributes.

#### Child Elements

The following table describes the child elements of `<Response>`:

Child Element | Type | Description  
---|---|---  
[`<Step>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#step) | String | Specifies a policy to execute within the response segment. This type of child can appear multiple times.  
  
## `<Step>`

Specifies a policy to execute and (optionally) a condition that determines whether to execute that policy.

**Type** | Complex object  
---|---  
**Parent Element(s)** |  [`<Request>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#request)  
[`<Response>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#response)  
  
**Child Element(s)** |  [`<Condition>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#condition)  
[`<Name>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#name)  
  
  
There can be more than one step defined in a [`<Flow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#flow), and the steps are executed in the order in which they are defined in the flow's XML.

Steps without a condition always execute. Steps with a condition execute only if the condition evaluates to true. If the condition evaluates to false, then Apigee skips the step.

### Syntax

The `<Step>` element uses the following syntax:
    
    
    <Step>
      <Condition>property operator "value"</Condition>
      <Name>policy_name</Name>
    </Step>

There can be only one `<Condition>` and one `<Name>` per `<Step>`, but there can be multiple steps in a `<Flow>`.

All child elements of `<Step>` are optional.

### Example 1

The following example shows one step with a condition and one step without a condition:
    
    
    <!-- api-platform/reference/examples/flow-segments/step-1.xml -->
    <ProxyEndpoint name="default">
      <PostFlow name="my-postflows">
          <Description>My first PostFlow</Description>
          <Request>
              <Step>
                  <Condition>request.verb = "GET"</Condition>
                  <Name>Log-Request-OK</Name>
              </Step>
          </Request>
          <Response>
              <Step>
                  <Name>Set-Response-Headers</Name>
              </Step>
          </Response>
      </PostFlow>
      ...
    </ProxyEndpoint>

The step without the condition will execute every time during the request segment. The step with a condition will execute only when the request is a "GET" during the response segment.

### Example 2

The following example shows multiple steps in a single segment:
    
    
    <!-- api-platform/reference/examples/flow-segments/step-2.xml -->
    <ProxyEndpoint name="default">
        <PostFlow name="PostFlow">
            <Response>
                <Step>
                    <Name>Assign-Message-1</Name>
                </Step>
                <Step>
                    <Name>Assign-Message-2</Name>
                </Step>
            </Response>
        </PostFlow>
      ...
    </ProxyEndpoint>

Steps without a condition always execute.

#### Attributes

The `<Step>` element has no attributes.

#### Child Elements

The following table describes the child elements of `<Step>`:

Child Element | Type | Description  
---|---|---  
[`<Condition>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#condition) | String | Defines a conditional statement for the step that is processed at runtime. If the statement evaluates to true, then Apigee executes the step. If the statement evaluates to false, then Apigee skips the step.  
[`<Name>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/flow-configuration-reference#name) | String | Specifies the ID of the policy to execute in the current flow.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
