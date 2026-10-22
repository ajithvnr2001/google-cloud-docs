---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-routes/
title: Understanding routes \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:13.702906+00:00
---

# Understanding routes  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Understanding routes Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

A route determines the path of a request from the `ProxyEndpoint` to the `TargetEndpoint`. Included in the route is the URL used to access the API `ProxyEndpoint` and the URL of the backend service defined by the `TargetEndpoint`.

**Note:** This video was recorded with a previous version of the Apigee UI; however, the concepts are still valid. 

Watch this video for an introduction to routes, describing the relationship between the `ProxyEndpoint` and the `TargetEndpoint`.

## Determining the URL of the API proxy endpoint

The following image shows a request coming in to the `ProxyEndpoint` from an app, and that request being directed to the backend service: 

![An HTTP client request goes through an API proxy on Apigee to the HTTP service, and then
    the response goes through the API proxy back to the client.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ApigeeProxyRoute.png)

After you create an API proxy on Apigee, the default URL that an app uses to access the proxy has the following form:
    
    
    **https://www.example.com/shopping/cart/addItem**
            |_____________| |___________| |_____|
                   |             |           |
                hostname      basepath     resource
    

Where:

  * The hostname is either a domain that you have added to DNS or an IP address.
  * The base path and resource-path are defined when you create the API proxy.



When a request comes in to Apigee, Apigee parses the URL to direct the request to the correct `ProxyEndpoint`. For example, the following URL is used to access an API proxy:
    
    
    http://example.com/v1/weather/forecastrss

If you examine the `ProxyEndpoint` definition for the API proxy in the figure above, you can see how this URL is parsed:

  1. The domain portion of the URL, `http://example.com`, corresponds to a host name defined on an environment group. The proxy was deployed to one or more environments within that environment group. For more information, see [About environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview).
  2. The second part of the URL, `/v1/weather`, is determined by the `<BasePath>` element in the `ProxyEndpoint`. You defined the base path when you created the proxy. The base path must be unique to the API proxy for the environment so that two API proxies in the same environment do not have the same base path.
  3. The third part of the URL, `/forecastrss`, is a resource defined by the API proxy with the corresponding conditional flow defined by the `<Flows>` element.

**Note:** This video was recorded with a previous version of the Apigee UI; however, the concepts are still valid. 

**Video:** Watch a short video to learn more about API proxy endpoints.

## Determining the URL of the target endpoint

The `<RouteRule>` element in a `ProxyEndpoint` definition determines the target of the API proxy, and is evaluated after all policies in the PreFlow, Conditional Flows, and PostFlow of the `ProxyEndpoint` request are processed.

A `ProxyEndpoint` can define the target as:

  * A direct URL to a backend service.
  * A single `TargetEndpoint` definition.
  * Multiple `TargetEndpoint`s where the API proxy delegates the request to a target endpoint based on a condition.
  * Null route or target, meaning the request is not forwarded to a target. Instead, all of the processing of the request, and the generation of the response, occurs on Apigee.

**Note:** This video was recorded with a previous version of the Apigee UI; however, the concepts are still valid. 

**Video:** Watch a short video to learn more about target endpoints.

### Direct URL

A `ProxyEndpoint` can directly invoke a backend service, bypassing any named `TargetEndpoint` configuration. For example, the following `<RouteRule>` always makes an HTTP call to `http://example.com/myAPI:`
    
    
    <RouteRule name="default">
      <URL>http://example.com/myAPI</URL>
    </RouteRule>

However, because there is no `TargetEndpoint`, you can only add policies to the flows defined by the `ProxyEndpoint`.

### Single target

In a single target definition, the `ProxyEndpoint` references a single `TargetEndpoint` definition by name, as shown in the figure above:
    
    
    <RouteRule name="default">
      <TargetEndpoint>default</TargetEndpoint>
    </RouteRule>

All requests to this API proxy are directed to the same `TargetEndpoint` definition. The `<URL>` tag in the `TargetEndpoint` determines the location of the backend service. in the figure above, the target URL is `http://weather.yahooapis.com`.

### Conditional targets

The `<RouteRule>` tag lets you direct a request to a target based on a condition. You can use flow variables, query parameters, HTTP headers, message content, or contextual information such time of day and locale to determine the target endpoint. For example, you might include a geographical area, such as US and UK, in a request URL. You can then route a request to a target endpoint based on the region.

The following route rule evaluates an HTTP header in a request. If the HTTP header `routeTo` has the value `TargetEndpoint1`, then the request is forwarded to the `TargetEndpoint` named `TargetEndpoint1`. If not, then the request is forwarded to `TargetEndpoint2`.
    
    
    <RouteRule name="MyRoute">
      <Condition>request.header.routeTo = "TargetEndpoint1"</Condition>
      <TargetEndpoint>TargetEndpoint1</TargetEndpoint>
    </RouteRule>
    <RouteRule name="default">
      <TargetEndpoint>TargetEndpoint2</TargetEndpoint>
    </RouteRule>

If you have multiple route rules, create one as the _default_ , that is, as a route rule with no condition. Ensure that the default route rule is defined last in the list of conditional routes because rules are evaluated top-down in the `ProxyEndpoint`.

See also [Conditional routes](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint-conditionalroutes) and [Conditions reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference). **Note:** **Order is important** : 

If you have more than one `RouteRule` in a `ProxyEndpoint`, their order in the XML configuration is important. The first `RouteRule` to _match_ gets executed. (`RouteRule` with no condition always match.)

In the previous example, if the unconditional _default_ `RouteRule` came first, it would be executed even if the condition of the `MyRoute` rule would have matched. So list your conditional `RouteRule` before an unconditional `RouteRule`.

**Note:** This video was recorded with a previous version of the Apigee UI; however, the concepts are still valid. 

**Video:** Watch a short video to learn how to route to a target endpoint using conditional targets.

### Null route

A null route supports scenarios in which the request message does not need to be forwarded to a `TargetEndpoint`. This is useful when the `ProxyEndpoint` performs all of the necessary processing, for example by using JavaScript to call an external service.

The following example defines a null route:
    
    
    <RouteRule name="GoNowhere"/>

## Learn more

  * [API proxy configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference)
  * [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference)
  * [Load balancing across backend servers](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
