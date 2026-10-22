---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/connecting-proxies-other-proxies/
title: Chaining API proxies together \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:42.627615+00:00
---

# Chaining API proxies together  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/connecting-proxies-other-proxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Chaining API proxies together Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

You can specify that one proxy is the target endpoint of another, effectively connecting the two proxies in a proxy chain. Chaining proxies in this way can help you avoid a network hop, and so improve overall performance.

**Note:** Each proxy in the chain is billed as one call, and counts as one call toward [limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits).**Note:** Proxy chaining provides one way to reuse proxies. For another way, in which you develop components that are expressly designed to be reused, be sure to see [Reusable shared flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows).

With proxy chaining, you specify that one proxy is the local target endpoint of the other. Rather than using the `HTTPTargetConnection` element to make a call to the second proxy, you use the `LocalTargetConnection` element.
    
    
    <LocalTargetConnection>
        <APIProxy>myproxy2</APIProxy>
        <ProxyEndpoint>default</ProxyEndpoint>
    </LocalTargetConnection>

You might find proxy chaining useful when you have a proxy that offers some discrete low-level functionality that other proxies will consume. For example, a proxy that exposes create/read/update/delete operations with a backend data store could be the target proxy for multiple other proxies that expose the data to clients.

**Note:** Proxies you want to connect in this way must be in the same organization and environment. When the proxy you're connecting with is outside this scope, consider connecting to it as an external resource using the `HTTPTargetConnection` element (as described in [API proxy configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference)).**Note:** This video was recorded with a previous version of the Apigee UI; however, the concepts are still valid. 

**Video:** Watch a short video to learn more about API proxy chaining.

## How proxy chaining works

Proxy chaining uses a local connection to minimize network overhead when calling one proxy from another. This local connection is more efficient because it bypasses network features such as load balancers, routers, and message processors.

The following illustrates the difference between connecting proxies with `HTTPTargetConnection` and `LocalTargetConnection` (proxy chaining):

![Diagram of proxy-to-proxy call without proxy chaining.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/proxies-unchained.png)

![Diagram of proxy-to-proxy call with proxy chaining.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/proxies-chained.png)

You connect proxies by specifying that one is a local target endpoint of the other. For the configuration in the diagram above (Proxy-to-proxy call with proxy chaining), you would specify that ProxyB (/proxyB) is a local target endpoint of ProxyA (/proxyA). This causes requests arriving at ProxyA to be forwarded to ProxyB.

You can create a local connection between proxies in two ways:

  * By specifying the name of the target proxy and a ProxyEndpoint name
  * By specifying a path to the target proxy endpoint



You connect target proxies within a `TargetEndpoint` configuration, using a `LocalTargetConnection` element, as described below.

**Warning:** When chaining API proxies, take care to avoid infinite loop recursive callouts back into the same API proxy, which could result in system overload.**Note:** If you are using Apigee hybrid v1.14 or newer and your organization is entitled to use the [`Enhanced per-environment proxy limits`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/enhanced-proxy-limits) feature, you must set the [`enhanceProxyLimits`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/config-prop-ref#enhanceproxylimits) property to `true` in your `overrides.yaml` file in order to use proxy chaining. 

## Connecting proxies by proxy name

You can specify the target proxy by name. You might find that this is most useful when you're creating the connection from the start and developing the proxies together. If you don't know the name (or the name might change), consider connecting with the target proxy's endpoint path, as described below.

When you connect to a target proxy by name, you specify the proxy's name and the name of its `ProxyEndpoint`.

The following example specifies a target proxy called `data-manager`, along with the `ProxyEndpoint` name exposed by `data-manager`. For reference information, see [API proxy configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference).

The `<APIProxy>` and `<ProxyEndpoint>` elements support the dynamic string substitution feature called [message templating](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro). **Important:** If you implement proxy chaining using the proxy name, the second proxy will not show results in [Debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview) even when you call Debug for it. Use Proxy chaining by path instead if you need to use Debug on the second proxy. 
    
    
    <TargetEndpoint name="datamanager">
        <PreFlow name="PreFlow">
            <!-- PreFlow policies -->
        </PreFlow>
        <PostFlow name="PostFlow">
            <!-- PostFlow policies -->
        </PostFlow>
        <LocalTargetConnection>
            <APIProxy>data-manager</APIProxy>
            <ProxyEndpoint>default</ProxyEndpoint>
        </LocalTargetConnection>
    </TargetEndpoint>

## Connecting proxies by path

You can specify the target proxy by its endpoint path. You might want to do it this way when you don't know the proxy name, or when the name might change.

If your proxy is simply the consumer of the target proxy—such as when you're not developing both—the path might be the most reliable way to connect. For example, if the proxy you're connecting to is developed and maintained by another team, you might want to connect using a reliable endpoint path.

The following example specifies a target proxy at `/v1/streetcarts/foodcarts/data-manager`, where the host is assumed to be the same as the current proxy. For reference information, see [API proxy configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference).
    
    
    <TargetEndpoint name="datamanager">
        <PreFlow name="PreFlow">
            <!-- PreFlow policies -->
        </PreFlow>
        <PostFlow name="PostFlow">
            <!-- PostFlow policies -->
        </PostFlow>
        <LocalTargetConnection>
            <Path>/v1/streetcarts/foodcarts/data-manager</Path>
        </LocalTargetConnection>
    </TargetEndpoint>

The `<Path>` element under `<LocalTargetConnection>` can be a string, or you can use a [message template](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro) to assign a value dynamically. 

## Connecting proxies using the Apigee UI

You can also connect proxies, either by proxy name or path, using the Apigee UI. In the following example, there are two proxies, ProxyA and ProxyB, and you want ProxyB to be a target endpoint of ProxyA. To connect the proxies by proxy name, do the following steps:

  1. Go to the proxies list. 

In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. In the list of proxies, select **ProxyA**.
  3. Click the **Develop** tab.
  4. In the **Code** pane, replace the `<TargetEndpoint>` section of the XML with the following: 
         
         <TargetEndpoint>
           <LocalTargetConnection>
             <APIProxy>ProxyB</APIProxy>
             <ProxyEndpoint>default</ProxyEndpoint>
           </LocalTargetConnection>
         </TargetEndpoint>

  5. Click **Save**.



## Chained proxies, API products, and security

Proxy chaining is best for cases where both proxies are in the same API product. By default, both are available to clients. Apigee currently doesn't support bundling the second proxy in a separate API product that clients shouldn't have access to.

If your second proxy must be secured against direct client requests, consider adding logic to have your second proxy examine the IP address of the client. In the case of a call made with chaining, the IP address will be local. Your code can validate that it is local before allowing processing to continue. See the [AccessControl policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-control-policy) for one way to do this.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
