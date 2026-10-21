---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/invalidate-cache-deployment-errors/
title: Invalidate Cache policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:26.852331+00:00
---

# Invalidate Cache policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/invalidate-cache-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Invalidate Cache policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/invalidate-cache-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/invalidate-cache-deployment-errors/).

## InvalidCacheResourceReference

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Invalid cache resource reference [cache_resource] in Step definition [invalidate_cache_policy_name]. Context Revision:[revision_number];APIProxy:[apiproxy_name];Organization:[organization];Environment:[environment]
    

### Example Error Message
    
    
    Error Deploying Revision 2 to test
    Invalid cache resource reference tokencache in Step definition InvalidateCache-Token. Context Revision:2;APIProxy:TestCache;Organization:kkalckstein-eval;Environment:test
    

### Example Error Screenshot

![Error deploying revision 2 to test.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/invalidatecache-deploy-error-2.png)

### Cause

This error occurs if the `<CacheResource>` element in the InvalidateCache policy is set to a name that does not exist in the environment where the API proxy is being deployed.

### Diagnosis

  1. Identify the [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy) name, the invalid cache used in `<CacheResource>` element of the InvalidateCache policy, and the environment where the error occurred. You can find all these items in the error message. For example, in the following error, the InvalidateCache policy name is `InvalidateCache-Token`, the name of the invalid cache is `tokencache`, and the environment name is `test`.
         
         Invalid cache resource reference tokencache in Step definition InvalidateCache-Token. Context Revision:2;APIProxy:TestCache;Organization:kkalckstein-eval;Environment:test
         

  2. Examine the failed InvalidateCache policy XML and verify if the cache name specified for the `<CacheResource>` element matches with the error message.

In this example, the cache name specified in the `<CacheResource>` element is `tokencache`:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <InvalidateCache async="false" continueOnError="false" enabled="true" name="InvalidateCache-Token">
             <DisplayName>InvalidateCache-Token</DisplayName>
             <Properties/>
             <CacheKey>
                 <Prefix/>
                 <KeyFragment ref=""/>
             </CacheKey>
             <CacheResource>tokencache</CacheResource>
             <Scope>Exclusive</Scope>
             <CacheContext>
                 <APIProxyName/>
                 <ProxyName>default</ProxyName>
                 <TargetName>default</TargetName>
             </CacheContext>
             <PurgeChildEntries>false</PurgeChildEntries>
         </InvalidateCache>
         

  3. Verify if the cache (determined in step #1) has been defined in the specific environment (identified in step #1).

In the Apigee UI, navigate to **ADMIN > Environment > test** and check if the cache exists in the **Caches** tab of **Environment Configuration**. If the cache does not exist, then that's the cause of the error.

For example, notice in the screenshot below that the cache named `tokencache` does not exist.

![Environment Configuration dialog.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/invalidatecache-deploy-error-1.png)

Because the cache named `tokencache` is not defined in the `test` environment, you get the error:
         
         Invalid cache resource reference tokencache in Step definition InvalidateCache-Token. Context Revision:2;APIProxy:TestCache;Organization:kkalckstein-eval;Environment:test
         




### Resolution

Ensure that the cache specified in the `<CacheResource>` element of InvalidateCache policy has been created in the environment where you want to deploy the API proxy.

## CacheNotFound

### Error Message

Deployment of the API proxy through either the Apigee UI or API results in an error message like this, and the deployment status of the API Proxy is marked as partially deployed:
    
    
    Error: Cache : cache_resource, not found in organization : organization__environment.

### Example Error Message
    
    
    Error Cache : configCache, not found in organization : kkalckstein-eval__test
    

### Cause

This error occurs if the specific cache mentioned in the error message has not been created on a specific Message Processor component. A Message Processor is an internal component that processes the flow of API traffic through Apigee.

### Resolution

Contact [Apigee Support](https://apigee.com/about/support/portal) for assistance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
