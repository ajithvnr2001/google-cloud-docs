---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/adding-cors-support-api-proxy/
title: Adding CORS support to an API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:42.232493+00:00
---

# Adding CORS support to an API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/adding-cors-support-api-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Adding CORS support to an API proxy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Warning** : The examples provided in this section allow access to your API proxy by any origin and should be secured **before they are used in a production environment**. For example, you might allow the domains that can access the API proxy. 

CORS (Cross-origin resource sharing) is a standard mechanism that allows JavaScript XMLHttpRequest (XHR) calls executed in a web page to interact with resources from non-origin domains. CORS is a commonly implemented solution to the [same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy) that is enforced by all browsers. For example, if you make an XHR call to the Twitter API from JavaScript code executing in your browser, the call will fail. This is because the domain serving the page to your browser is not the same as the domain serving the Twitter API. CORS provides a solution to this problem by allowing servers to _opt-in_ if they wish to provide cross-origin resource sharing. 

**Note:** Most browsers support CORS. See [Cross-Origin Resource Sharing](https://caniuse.com/cors) to view a comprehensive list of supported browsers. For an in-depth description of CORS, see the [Fetch Living Standard](https://fetch.spec.whatwg.org/). 

If you are using a [cache policy](https://docs.cloud.google.com/apigee/docs/api-platform/cache/persistence-tools) on your API proxy, you must ensure that the response of the CORS policy is not cached.

## Typical use case for CORS

The following JQuery code calls a fictitious target service. If executed from within the context of a browser (a web page), the call will fail because of the same-origin policy:
    
    
    <script>
    var url = "http://service.example.com";
    $(document).ready(function(){
      $("button").click(function(){
        $.ajax({
            type:"GET",
            url:url,
            async:true,
            dataType: "json",
               success: function(json) {
                  // Parse the response.
                  // Do other things.
               },
               error: function(xhr, status, err) {
                  // This is where we end up!
                }
        });
      });
    });
    </script>

One solution to this problem is to create an Apigee API proxy that calls the service API on the back end. Remember that Apigee sits between the client (a browser in this case) and the backend API (the service). Because the API proxy executes on the server, not in a browser, it **_is_** able to call the service successfully. Then, all you need to do is attach CORS headers to the TargetEndpoint response. As long as the browser supports CORS, these headers signal to the browser that it's okay to _relax_ its same-origin policy, allowing the cross-origin API call to succeed.

Once the proxy with CORS support is created, you can call the API proxy URL instead of the backend service in your client-side code. For example:
    
    
    <script>
    var url = "http://myorg-test.apigee.net/v1/example";
    $(document).ready(function(){
      $("button").click(function(){
        $.ajax({
            type:"GET",
            url:url,
            async:true,
            dataType: "json",
               success: function(json) {
                  // Parse the response.
                  // Do other things.
               },
               error: function(xhr, status, err) {
                  // This time, we do not end up here!
                }
        });
      });
    });
    </script>

**Note:** In the simplest case, you can return CORS headers to the client and the cross-origin request will work. More complicated cases exist where a _preflight_ request is required. You can read about preflight CORS requests in the [Fetch Living Standard](https://fetch.spec.whatwg.org/), as well as in numerous articles and blogs. See also Handling CORS preflight requests below.

## Attaching the CORS policy to the request PreFlow of the ProxyEndpoint

### Attaching an Add CORS policy to a new API proxy 

You add CORS support to an API proxy by attaching an **Add CORS** policy to the API proxy.

The **Add CORS** policy adds the appropriate headers to the response. Basically, the headers let the browser know which origins it will share its resources with, which methods it accepts, and so on. You can read more about these CORS headers in the [Cross-Origin Resource Sharing W3C Recommendation](https://www.w3.org/TR/cors/).

You should modify the policy, as follows: 

  * Add the `content-type` and `authorization` headers (required to support basic authentication or OAuth2) to the `Access-Control-Allow-Headers` header, as shown in the code excerpt below.
  * For OAuth2 authentication, you may need to take steps to correct [ non-RFC-compliant behavior](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#non-rfc-compliant-behavior).


    
    
    <CORS continueOnError="false" enabled="true" name="add-cors">
        <DisplayName>Add CORS</DisplayName>
        <AllowOrigins>{request.header.origin}</AllowOrigins>
        <AllowMethods>GET, PUT, POST, DELETE</AllowMethods>
        <AllowHeaders>origin, x-requested-with, accept, **content -type, authorization<**/AllowHeaders>
        <ExposeHeaders>*</ExposeHeaders>
        <MaxAge>3628800</MaxAge>
        <AllowCredentials>false</AllowCredentials>
        <GeneratePreflightResponse>true</GeneratePreflightResponse>
        <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </CORS>

### Adding CORS headers to an existing proxy

To add the CORS policy to an existing API proxy: 

  1. In the Google Cloud console, go to the **Apigee > Proxy Development > API Proxies** page.

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select the API proxy to which you want to add the CORS policy. The UI displays the proxy details in the Google Cloud console.
  3. Click the **Develop** tab.
  4. In the navigation pane, click the **+** button in the **Policies** row.
  5. In the **Create policy** dialog, click the **Select policy** field and scroll down to **Security** and select **CORS**.

  6. Enter the details for the policy and click **Create**.

  7. In the navigation pane, click **PreFlow** under **Target Endpoints > default**.
  8. Click the **+** button next to **PreFlow** in the **Request** pane of the Visual Editor. 
  9. In the **Add policy step** dialog, select the **CORS** policy. 
  10. Click **Add** to attach the policy.




## Handling CORS preflight requests

**CORS preflight** refers to sending a request to a server to verify if it supports CORS. Typical preflight responses include which origins the server will accept CORS requests from, a list of HTTP methods that are supported for CORS requests, headers that can be used as part of the resource request, the maximum time preflight response will be cached, and others. If the service does not indicate CORS support or does not wish to accept cross-origin requests from the client's origin, the cross-origin policy of the browser will be enforced and any cross-domain requests made from the client to interact with resources hosted on that server will fail.

Typically, CORS preflight requests are made with the HTTP OPTIONS method. When a server that supports CORS receives an OPTIONS request, it returns a set of CORS headers to the client that indicate its level of CORS support. As a result of this handshake, the client knows what it is allowed to request from the non-origin domain. 

**Note:** If you have a Verify API key policy in the proxy endpoint PreFlow, it is applied to all the incoming requests. If you don't want to apply the policy for CORS preflight requests, add a condition to skip when the method is OPTIONS. For example, use the following API proxy configuration: 
    
    
    <PreFlow name="PreFlow">
        <Request>
            <Step>
                <Name>verify-api-key</Name>
                <Condition>request.verb != "OPTIONS"</Condition>
            </Step>
        </Request>
        <Response/>
    </PreFlow>

For more information on preflight, refer to the [Cross-Origin Resource Sharing W3C Recommendation](https://www.w3.org/TR/cors/). There are in addition numerous blogs and articles on CORS that you can refer to.

Apigee does not include a CORS preflight solution out of the box, but it is possible to implement, as described in this section. The objective is for the proxy to evaluate an OPTIONS request in a conditional flow. The proxy can then send an appropriate response back to the client. 

Let's look at a sample flow, and then discuss the parts that handle the preflight request:  

    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ProxyEndpoint name="default">
        <Description/>
        <Flows>
            **< Flow name="OptionsPreFlight">
                <Request>
                    <Step>
                        <Name>add-cors</Name>
                    </Step>
                </Request>
                <Response/>
            <Condition>request.verb == "OPTIONS" AND request.header.origin != null AND request.header.Access-Control-Request-Method != null</Condition>
            </Flow>**
        </Flows>
    
        <PreFlow name="PreFlow">
            <Request/>
            <Response/>
    
        </PreFlow>
        <HTTPProxyConnection>
            <BasePath>/v1/cnc</BasePath>
            <VirtualHost>default</VirtualHost>
            <VirtualHost>secure</VirtualHost>
        </HTTPProxyConnection>
        **< RouteRule name="NoRoute">
            <Condition>request.verb == "OPTIONS" AND request.header.origin != null AND request.header.Access-Control-Request-Method != null</Condition>
        </RouteRule>**
        <RouteRule name="default">
            <TargetEndpoint>default</TargetEndpoint>
       </RouteRule>
       <PostFlow name="PostFlow">
            <Request/>
            <Response/>
        </PostFlow>
    </ProxyEndpoint>

The key parts of this ProxyEndpoint are as follows:

  * A RouteRule is created to a NULL target with a condition for the OPTIONS request. Note that there is no TargetEndpoint specified. If the OPTIONS request is received and the Origin and Access-Control-Request-Method request headers are not null, the proxy immediately returns the CORS headers in a response to the client (bypassing the actual default "backend" target). For details on flow conditions and RouteRule, see [Conditions with flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions).  

        
        <RouteRule name="NoRoute">
            <Condition>request.verb == "OPTIONS" AND request.header.origin != null AND request.header.Access-Control-Request-Method != null</Condition>
        </RouteRule>

  * An OptionsPreFlight flow is created that adds an Add CORS policy, containing the CORS headers, to the flow if an OPTIONS request is received and the Origin and Access-Control-Request-Method request headers are not null.   

        
        <Flow name="OptionsPreFlight">
                    <Request>
                        <Step>
                            <Name>add-cors</Name>
                        </Step>
                    </Request>
                    <Response/>
                <Condition>request.verb == "OPTIONS" AND request.header.origin != null AND request.header.Access-Control-Request-Method != null</Condition>
         </Flow>


**Note:** RouteRules are evaluated in the order specified in the ProxyEndpoint configuration. You should always have the default (no condition) Route at the end. Otherwise, if at the top, it will always match and never evaluate the other Route possibilities.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
