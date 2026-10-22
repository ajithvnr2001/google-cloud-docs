---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-policy-proxyendpoint-or-targetendpoint-flow/
title: Attaching a policy to a ProxyEndpoint or TargetEndpoint Flow \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:54.618818+00:00
---

# Attaching a policy to a ProxyEndpoint or TargetEndpoint Flow  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-policy-proxyendpoint-or-targetendpoint-flow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Attaching a policy to a ProxyEndpoint or TargetEndpoint Flow Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Policies are not executed until they are attached to a Flow. You can create a Policy attachment by naming a Policy in a Step configuration.

The choice of attachment point is critical to the behavior of your API proxy. For example, if you attach the Quota policy to a response Flow, then the Quota would be enforced _after_ the request message was sent to the backend service. That would defeat the purpose of applying a Quota policy! Therefore, you need to attach the Quota policy as a processing Step on the request Flow.

The format of a policy attachment is:
    
    
    <Step>
        <Name>{policy_name}</Name>
    </Step>

For example:
    
    
    <Step>
        <Name>QuotaPolicy</Name>
    </Step>

**Note:** The `{policy_name}` variable must be the same as the `name` attribute in the policy (stored under /policies) that you want to attach. The names must match exactly, as name matching is case-sensitive.

A policy is attached to a Flow by adding the Step configuration to the appropriate request or response Flow element in a ProxyEndpoint or TargetEndpoint configuration.

You can attach a policy to a request or response Flow. Request and response Flows are further subdivided in to PreFlow and PostFlow.

The following example demonstrates the minimal ProxyEndpoint configuration, with no policy attachments. It simply defines the (inbound) HTTPProxyConnection and a RouteRule.
    
    
    <ProxyEndpoint name="default">
        <HTTPProxyConnection>
            <BasePath>/weather</BasePath>
            <VirtualHost>default</VirtualHost>
        </HTTPProxyConnection>
        <RouteRule name="default">
            <TargetEndpoint>default</TargetEndpoint>
        </RouteRule>
    </ProxyEndpoint>

You must modify this configuration so that the ProxyEndpoint enforces a Quota policy (as a processing Step) before the API proxy performs any other processing. If a developer has exceeded a Quota, you don't want to waste any computational resources on additional requests.

To enforce this configuration, you attach a processing Step to the request PreFlow as follows:
    
    
    <ProxyEndpoint name="default">
      <PreFlow>
        <Request>
          <Step><Name>QuotaPolicy</Name></Step>
        </Request>
      </PreFlow>
      <HTTPProxyConnection> 
        <BasePath>/weather</BasePath> 
        <VirtualHost>default</VirtualHost> 
      </HTTPProxyConnection> 
      <RouteRule name="default"> 
        <TargetEndpoint>default</TargetEndpoint> 
      </RouteRule> 
    </ProxyEndpoint>

Sometimes, you might want a policy to execute after some other initial processing on the ProxyEndpoint. For example, you want to check Quota in the PreFlow, then perform another set of processing after Quota is checked, such as converting the request from JSON to XML. To do so, attach a policy to the PostFlow request path. The following is a sample request PostFlow attachment. This policy would execute on the request message after all of the policies in the PreFlow (and any conditional flows) execute.
    
    
    <PostFlow>
      <Request>
        <Step><Name>JSONtoXMLPolicy</Name></Step>
      </Request>
    </PostFlow>

The following is a sample response PostFlow attachment. This policy would execute on the response message. (The ProxyEndpoint response PostFlow is the final processing phase before the response is returned to the requesting client app.)
    
    
    <PostFlow>
      <Response>
        <Step><Name>XMLtoJSONPolicy</Name></Step>
      </Response>
    </PostFlow>

**Tip:** You can also define conditional Flows that execute _between_ the PreFlow and PostFlow phases. This is covered in the next topic, [Flow variables and conditions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
