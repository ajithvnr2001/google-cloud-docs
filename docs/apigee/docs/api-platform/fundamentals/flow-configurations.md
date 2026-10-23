---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-configurations/
title: Conditional flows \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:18.857839+00:00
---

# Conditional flows  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Conditional flows Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

In a conditional flow, policies are executed only if the flow's condition evaluates to `true` (as opposed to policies attached to the PreFlow or PostFlow, which are always executed). This section describes how to create a conditional flow.

## About conditional flows

During the processing of a request and response, only one conditional flow is executed per segment—the first flow whose condition evaluates to `true`.

You can create conditions that include `||`(OR) and `&&`(AND) operators. However, by default, the `||` operator has higher precedence than the `&&` operator. For example, a condition written as ` A && B || C && D` is evaluated as `A && (B || C) && D`. Make sure to parenthesize the expression if you want to change the precedence when using these operators. 

The following examples illustrate some ways to use conditional flows.

### Example 1

The following ProxyEndpoint definition shows a conditional flow that is executed by the ProxyEndpoint on any `HTTP GET` request to the API proxy:
    
    
    <ProxyEndpoint name="default">
      <PreFlow>
        <Request/>
        <Response/>
      </PreFlow>
    ** <Flows>
        <Flow name="Flow-1">
          <Condition>request.verb="GET"</Condition>
          <Request/>
          <Response/>
        </Flow>
      </Flows>**
      <PostFlow>
        <Request/>
        <Response/>
      </PostFlow>
      ...
    </ProxyEndpoint>

Notice that the condition references the `request.verb` [_flow variable_](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables). A flow variable is named references that hold state information associated with an API transaction processed by Apigee. Apigee defines many state variables that you can reference.

### Example 2

If your service backend provides weather reports and weather forecasts, your API might define two conditional flows that map to those API resources: `/reports` and `/forecasts`. When an API call includes one of those resources in the URL, the condition evaluates to true and the logic attached to the conditional flow is executed.

App developers then access your resources by making requests to a URL in the form:
    
    
    http://myAPIs.myCo.com/weather/reports

or:
    
    
    http://myAPIs.myCo.com/weather/forecasts

In an API proxy, you can define a conditional flow that corresponds to a specific resource:
    
    
    <ProxyEndpoint name="default">
      <PreFlow>
        <Request/>
        <Response/>
      </PreFlow>
    ** <Flows>
        <Flow name="Flow-1">
          <Condition>(proxy.pathsuffix MatchesPath "/reports")</Condition>**
    ** <Request/>
          <Response/>
        </Flow>
        <Flow name="Flow-2">
          <Condition>(proxy.pathsuffix MatchesPath "/forecasts")</Condition>**
    ** <Request/>
          <Response/>
        </Flow>
      </Flows>
    **  <PostFlow>
        <Request/>
        <Response/>
      </PostFlow>
      ...
    </ProxyEndpoint>

In this example, you reference the `proxy.pathsuffix` flow variable, which contains the suffix portion of the URL used to access the API proxy. You can then attach different policies to the conditional flow for each resource.

## Example: Creating a conditional flow

The next example:

  * Creates a conditional flow that executes only when the request message is an HTTP `GET`.
  * Adds a policy to the new flow.



### Adding a conditional flow

To add a conditional flow:

  1. Select the **Develop** tab in the Proxy Editor.
  2. Select **Proxy endpoints > default** in the left-hand pane. 

![Select Proxy endpoints > default in the left-hand pane.](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/proxy-endpoints-default.png)

**Note:** You may need to expand the visual editor in the right-hand pane to see all the elements. To do so, click and drag the divider between the visual editor and the text editor down a little.

  3. Click the **+** button above the **Response** pane. 

![Add conditional flow button](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/add-flow-button.png)

  4. In the **Add conditional flow** dialog, select **Path and verb** , and in the **Path** field, enter the path suffix that you want to be in the request path in order for the conditional flow to execute. See Example 2 above. **Note:** If you don't want to include a path condition, simply enter **/** in the **Path** field, as shown below. This will be matched for any request.

![Add conditional flow button](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/add-conditional-flow-dialog.png)

The conditional flow only executes if the request is a `GET` request (but not for `PUT`, `POST`, etc.).

The new flow, called `Flow-1`, now appears in the **Proxy Endpoint** pane.

![Conditional flow displayed in Proxy endpoints.](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/conditional-flow-proxy-endpoints.png)

  5. The XML code for the new conditional flow is displayed in the text editor.

![Conditional flow displayed in Proxy endpoints.](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/conditional-flow-xml.png)




You can edit the **Condition** element if you wish. See [Adding logic to flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows#addinglogictoflows).

### Attaching a policy to the flow

Now that you have created the conditional flow, you can attach a policy to it. The next example adds a Quota policy, which restricts the number of request messages that an API proxy allows over a period of time, to the flow:

  1. In the left-hand pane, click the **+** button to the right of **Policies**.
  2. In the **Create policy** dialog, click in the **Select policy type** field and scroll down to **Traffic Management** and select **Quota**.
  3. Click **Create** to create the policy.
  4. Click the **+** button next to **Flow-1** in the **Request** pane. 

![Click plus button next to Flow-1 in Request pane.](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/add-policy-conditional-flow.png)

  5. In the **Add policy step** dialog, click in the **Select existing policy** field and select **Quota-1**.
  6. Click **Add**.



The **Request** pane now displays the flow and attached policy, **Quota-1**.

![Request pane showing new flow and Quota policy.](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/request-pane-flow-and-quota-policy.png)

The text editor now displays a step containing the **Quota-1** policy in the **Flow-1** element of the XML:

![Conditional flow and Quota policy displayed in XML](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/quota-policy-xml.png)

With this configuration, the Quota policy will be enforced for `GET` requests. Requests of other types will not contribute to the maximum number of requests in the Quota policy. 

## Next steps

The following topics provide more detail about constructing conditions and using variables:

  * [ Using flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables)
  * [ Conditions with flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
