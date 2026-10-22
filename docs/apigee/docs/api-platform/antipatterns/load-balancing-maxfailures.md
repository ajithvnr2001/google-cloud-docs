---
url: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/load-balancing-maxfailures/
title: Antipattern: Load Balance with a single target server with MaxFailures set to a non-zero value \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:53.013177+00:00
---

# Antipattern: Load Balance with a single target server with MaxFailures set to a non-zero value  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/load-balancing-maxfailures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Antipattern: Load Balance with a single target server with MaxFailures set to a non-zero value Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/antipatterns/load-balancing-maxfailures) documentation._

The TargetEndpoint configuration defines the way Apigee connects to a backend service or API. It sends the requests and receives the responses to/from the backend service. The backend service can be a HTTP/HTTPS or NodeJS server.

The backend service in the TargetEndpoint can be invoked in one of the following ways:

  * Direct URL to an HTTP or HTTPS server
  * TargetServer configuration



Likewise, the [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy) can be used to make a call to any external service from the API Proxy flow. This policy supports defining HTTP/HTTPS target URLs either directly in the policy itself or using a TargetServer configuration.

## TargetServer configuration

TargetServer configuration decouples the concrete endpoint URLs from TargetEndpoint configurations or in Service Callout policies. A TargetServer is referenced by a name instead of the URL in TargetEndpoint. The TargetServer configuration will have the hostname of the backend service, port number, and other details. 

Here is a sample TargetServer configuration:
    
    
    <TargetServer name="target1">
      <Host>www.mybackendservice.com</Host>
      <Port>80</Port>
      <IsEnabled>true</IsEnabled>
    </TargetServer>

The TargetServer enables you to have different configurations for each environment. A TargetEndpoint/Service Callout policy can be configured with one or more named TargetServers using a LoadBalancer. The built-in support for load balancing enhances the availability of the APIs and failover among configured backend server instances. 

Here is a sample TargetEndpoint configuration using TargetServers:
    
    
    <TargetEndpoint name="default">
        <HTTPTargetConnection>>
          <LoadBalancer>
            <Server name="target1"/>
            <Server name="target2"/>
          </LoadBalancer>
        </HTTPTargetConnection>
    </TargetEndpoint>

## MaxFailures

The `MaxFailures` configuration specifies the maximum number of request failures to the target server after which the target server shall be marked as down and removed from rotation for all subsequent requests. 

An example configuration with `MaxFailures` specified:
    
    
    <TargetEndpoint name="default">
        <HTTPTargetConnection>
          <LoadBalancer>
            <Server name="target1"/>
            <Server name="target2"/>
            <MaxFailures>5</MaxFailures>
          </LoadBalancer>
        </HTTPTargetConnection>
    </TargetEndpoint>

In the above example, if five consecutive requests failed for "target1" then "target1" will be removed from rotation and all subsequent requests will be sent only to target2.

## Antipattern

Having single TargetServer in a `LoadBalancer` configuration of the TargetEndpoint or Service Callout policy with `MaxFailures` set to a non-zero value is not recommended as it can have adverse implications.

Consider the following sample configuration that has a single TargetServer named "target1" with `MaxFailures` set to 5 (non-zero value): 
    
    
    <TargetEndpoint name="default">
      <HTTPTargetConnection>
          <LoadBalancer>
            <Algorithm>RoundRobin</Algorithm>
            <Server name="target1" />
            <MaxFailures>5</MaxFailures>
          </LoadBalancer>
      </HTTPTargetConnection>

If the requests to the TargetServer "target1" fails five times (number specified in `MaxFailures`), the TargetServer is removed from rotation. Since there are no other TargetServers to fail over to, all the subsequent requests to the API Proxy having this configuration will fail with `503 Service Unavailable` error. 

Even if the TargetServer "target1" gets back to its normal state and is capable of sending successful responses, the requests to the API Proxy will continue to return 503 errors. This is because Apigee does not automatically put the TargetServer back in rotation even after the target is up and running again. To address this issue, **_the API Proxy must be redeployed_** for Apigee to put the TargetServer back into rotation.

If the same configuration is used in the Service Callout policy, then the API requests will get 500 Error after the requests to the TargetServer "target1" fails 5 times.

## Impact

Using a single TargetServer in a `LoadBalancer` configuration of TargetEndpoint or Service Callout policy with `MaxFailures` set to a non-zero value causes:

  * API Requests to fail with 503/500 Errors continuously (after the requests fail for MaxFailures number of times) until the API Proxy is redeployed.
  * Longer outage as it is tricky and can take more time to diagnose the cause of this issue (without prior knowledge about this antipattern).



## Best Practice

  1. Have more than one TargetServer in the `LoadBalancer` configuration for higher availability. 
  2. **Always define a Health Monitor** when `MaxFailures` is set to a non-zero value. A target server will be removed from rotation when the number of failures reaches the number specified in `MaxFailures`. Having a HealthMonitor ensures that the TargetServer is put back into rotation as soon as the target server becomes available again, **_meaning there is no need to redeploy the proxy_**.

To ensure that the health check is performed on the same port number that Apigee uses to connect to the target servers, Apigee recommends that you omit the `<Port>` child element under`<TCPMonitor>` unless it is different from TargetServer port. By default `<Port>` is the same as the TargetServer port. 

**Sample configuration with HealthMonitor:**
         
         <TargetEndpoint name="default">
           <HTTPTargetConnection>
             <LoadBalancer>
               <Algorithm>RoundRobin</Algorithm>
               <Server name="target1" />
               <Server name="target2" />
               <MaxFailures>5</MaxFailures>
             </LoadBalancer>
             <Path>/test</Path>
             <HealthMonitor>
               <IsEnabled>true</IsEnabled>
               <IntervalInSec>5</IntervalInSec>
               <TCPMonitor>
                 <ConnectTimeoutInSec>10</ConnectTimeoutInSec>
               </TCPMonitor>
             </HealthMonitor>
           </HTTPTargetConnection>
         </TargetEndpoint>

  3. If there's some constraint such that only one TargetServer and if the HealthMonitor is not used, then don't specify `MaxFailures` in the `LoadBalancer` configuration.

**The default value of MaxFailures is 0.** This means that Apigee always tries to connect to the target for each request and never removes the target server from the rotation.




## Further reading

  * [Load Balancing across Backend Servers](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers)
  * [How to use Target Servers in your API Proxies](https://discuss.google.dev/t/tutorial-how-to-use-target-servers-in-your-api-proxies/17530)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
