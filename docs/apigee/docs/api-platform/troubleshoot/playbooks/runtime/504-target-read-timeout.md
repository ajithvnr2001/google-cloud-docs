---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/504-target-read-timeout/
title: 504 Gateway timeout - Target read timeout \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:16.049910+00:00
---

# 504 Gateway timeout - Target read timeout  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/504-target-read-timeout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  504 Gateway timeout - Target read timeout Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## Symptom

This issue appears as a `Gateway Timeout` error with HTTP status `504`. 

## Error Message

You may see this error in [API Monitoring](https://docs.cloud.google.com/apigee/docs/api-monitoring/investigate), [Debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace), or other tools. The `TARGET_READ_TIMEOUT` reason indicates that Apigee runtime did not receive a timely response from the target during the execution of a request. 

The default target read timeout value ([io.timeout.millis](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference#targetendpointtransportpropertyspecification)) is 55 seconds. Which means that if after 55 seconds the target doesn't respond, Apigee throws this error: 
    
    
    {"fault":{"faultstring":"Gateway Timeout",
      "detail":{"errorcode":"messaging.adaptors.http.flow.GatewayTimeout",
      "reason":"TARGET_READ_TIMEOUT"}}}

## Possible Causes

Cause | Description | Troubleshooting instructions applicable for  
---|---|---  
Slow target | The target doesn't produce a timely response.  | Apigee X and Apigee hybrid   
TargetServer connectivity issue | There is a general connectivity problem with the target when [`<LoadBalancer>`](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers#configuringatargetendpointtoloadbalanceacrossnamedtargetservers) is configured on the TargetEndpoint.  | Apigee X and Apigee hybrid   
  
## Cause: Slow Target

### Diagnosis

You can diagnose a slow target issue using the Apigee [Debug Tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace): 

  1. Create a [debug session](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#create) for your API proxy. 
  2. In the debug session, send a request and inspect the debug output.



![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/target-timeout-1.png)![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/target-timeout-1.png)

As you can see in the example above, the Target Request exceeded 55 seconds, which is the [default target timeout](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference#targetendpointtransportpropertyspecification) limit. The time limit is configurable, and if you have changed the timeout, then the duration of the Target Request will match the timeout you set. For instance, if your timeout is 10 seconds, then in that scenario a target request will timeout after 10 seconds. Such "slow target" behavior is a clear indication that the target is not responding to a request in time. 

### Resolution

Apigee recommends that you avoid using [slow targets](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend). For example, if normal target latency is 50 ms, and you experience a latency of 55000 ms, you may need to investigate if there is a problem with the target. 

If you must increase the timeout, follow these steps: 

  1. Click on the **Develop** tab in the proxy editor. 
  2. In the navigation pane, select the affected target endpoint. 
  3. In the XML editor, find the `HTTPTargetConnection` XML element:  
  


![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/target-timeout-2.png)![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/target-timeout-2.png)

  4. Add the `io.timeout.millis` property under the `<HTTPTargetConnection>` element and specify the new time limit in milliseconds, for example: 
         
         <HTTPTargetConnection>
           <URL>https://my-very-slow-target.example.com</URL>
           <Properties>
             <Property name="io.timeout.millis">120000</Property>
           </Properties>
         </HTTPTargetConnection>

In the example above the timeout is increased to 120 seconds. Note that 300 seconds is the maximum limit. For further information, see [Endpoints property reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference). 

  5. Save the new revision and deploy the proxy.



If the problem persists, go to Must gather diagnostic information below. 

## Cause: TargetServer connectivity issue

### Diagnosis

Apigee does not reveal the exact cause of a connectivity issue when you configure the `[<LoadBalancer>](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers#configuringatargetendpointtoloadbalanceacrossnamedtargetservers)` endpoint property. You may be able to infer the cause of a connectivity problem, however, from the elapsed time of the Target Request. As a debugging method, you can try to remove the `<LoadBalancer>` element altogether, and try to hit the target directly in the proxy. 

To diagnose the issue, use the [Debug Tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace). 

  1. Create a [debug session](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#create) for your API proxy. 
  2. In the debug session, send a request and inspect the debug output.



![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/target-timeout-3.png)![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/target-timeout-3.png)

In the example above, it took nine seconds for a timeout to occur. Since it is not 55 seconds, you know the cause of the error is not that the timeout limit was exceeded due to a slow target. By default, Apigee retries a connection two additional times if the `<LoadBalancer>` element is used on the TargetEndpoint. Because you know that connection has been attempted three times in total, and the default timeout for a connection error is three seconds ([connect.timeout.millis](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference#targetendpointtransportpropertyspecification)), you can assume that the issue is a connectivity issue. 

### Resolution

If the issue is confirmed to be a connection timeout, see [ VPC Peering 503 Service Unavailable error with TARGET_CONNECT_TIMEOUT](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/vpc-503-target-connect-timeout). 

For other issues, remove the `<LoadBalancer>` element to debug and reveal the exact error code, and check for the code in the [error catalog](https://docs.cloud.google.com/apigee/docs/api-platform/errorcatalog/mp-runtime-errorcatalog). 

## Must Gather Diagnostic Information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Support](https://cloud.google.com/support-hub): 

  1. Project ID and the Apigee organization name 
  2. Proxy name(s) and the environment. 
  3. Time-frame of the issue. 
  4. Frequency of the issue 
  5. Target hostname. 
  6. [Debug session](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#download) with the issue.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
