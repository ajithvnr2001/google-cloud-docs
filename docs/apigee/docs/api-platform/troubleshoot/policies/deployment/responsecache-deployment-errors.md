---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/responsecache-deployment-errors/
title: Response Cache policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:53.584709+00:00
---

# Response Cache policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/responsecache-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Response Cache policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/responsecache-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/responsecache-deployment-errors/).

## InvalidTimeout

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    CacheLookupTimeoutInSeconds value value should be greater than zero.
    

#### Example Error Message
    
    
    Error Saving Revision 2
    CacheLookupTimeoutInSeconds -1 value should be greater than zero.
    

#### Example Error Screenshot

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/responsecache-error-3.png)

### Cause

If the `<CacheLookupTimeoutInSeconds>` element of a [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy) is set to a negative number, then the deployment of the API proxy fails.

For example, if the `<CacheLookupTimeoutInSeconds>` is `-1`, then the deployment of the API proxy fails.

### Diagnosis

  1. Identify the invalid value used for the `<CacheLookupTimeoutInSeconds>` element in the ResponseCache policy. You can find this information in the error message. For example, in the following error, the invalid value used for `<CacheLookupTimeoutInSeconds>` element is `-1`:
         
         CacheLookupTimeoutInSeconds -1 value should be greater than zero.
         

  2. Examine all the ResponseCache policies in the specific API Proxy where the failure has occurred. There could be one or more ResponseCache policies in which the `<CacheLookupTimeoutInSeconds>` element is specified.

For example, the following policy configuration sets `<CacheLookupTimeoutInSeconds>` to `-1`, which matches with what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <ResponseCache async="false" continueOnError="false" enabled="true" name="Response-Cache-1">
             <DisplayName>Response Cache-1</DisplayName>
             <Properties/>
             <CacheKey>
                 <Prefix/>
                 <KeyFragment ref="request.uri" type="string"/>
             </CacheKey>
             <Scope>Exclusive</Scope>
             <ExpirySettings>
                 <ExpiryDate/>
                 <TimeOfDay/>
                 <TimeoutInSec ref="">3600</TimeoutInSec>
             </ExpirySettings>
             <CacheLookupTimeoutInSeconds>-1</CacheLookupTimeoutInSeconds>
         </ResponseCache>
         

  3. If the `<CacheLookupTimeoutInSeconds>` is specified as a negative integer, then that's the cause of the error.




### Resolution

Ensure that the value for the `<CacheLookupTimeoutInSeconds>` element of the ResponseCache policy is always specified as a non-negative integer.

To correct the example ResponseCache policy shown above, you could modify the `<CacheLookupTimeoutInSeconds> element` to `30`.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResponseCache async="false" continueOnError="false" enabled="true" name="Response-Cache-1">
        <DisplayName>Response Cache-1</DisplayName>
        <Properties/>
        <CacheKey>
            <Prefix/>
            <KeyFragment ref="request.uri" type="string"/>
        </CacheKey>
        <Scope>Exclusive</Scope>
        <ExpirySettings>
            <ExpiryDate/>
            <TimeOfDay/>
            <TimeoutInSec ref="">3600</TimeoutInSec>
        </ExpirySettings>
        <CacheLookupTimeoutInSeconds>30</CacheLookupTimeoutInSeconds>
    </ResponseCache>
    

## InvalidCacheResourceReference

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Invalid cache resource reference cache_resource in Step definition response_cache_policy_name. Context Revision:revision_number;APIProxy:ResponseCache;Organization:organization;Environment:environment
    

#### Example Error Message
    
    
    Error Deploying Revision 2 to prod
    Invalid cache resource reference itemscache in Step definition ItemsResponseCache. Context Revision:2;APIProxy:StoresInventory;Organization:kkalckstein-eval;Environment:prod
    

#### Example Error Screenshot

![Error deploying revision 2 to prod.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/responsecache-error-4.png)

### Cause

This error occurs if the `<CacheResource>` element in a [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy) is set to a name that does not exist in the environment where the API proxy is being deployed.

### Diagnosis

  1. Identify the invalid cache used in `<CacheResource>` element of the Response Cache policy and the environment where the error occurred. You can find both of these items in the error message. For example, in the following error, the name of the invalid cache is `itemscache` and the environment name is `prod`.
         
         Invalid cache resource reference itemscache in Step definition ItemsResponseCache. Context Revision:2;APIProxy:StoresInventory;Organization:kkalckstein-eval;Environment:prod
         

  2. Examine all the ResponseCache policies in the specific API Proxy where the failure has occurred. Identify the specific ResponseCache policy where the invalid cache (identified in step #1) is specified in `<CacheResource>` element.

For example, the following policy specifies the value of `<CacheResource>` as `itemscache`, which matches with what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <ResponseCache async="false" continueOnError="false" enabled="true" name="ItemsResponseCache">
           <DisplayName>ItemsResponseCache</DisplayName>
           <Properties/>
           <CacheKey>
               <Prefix/>
               <KeyFragment ref="request.uri" type="string"/>
           </CacheKey>
           <CacheResource>itemscache</CacheResource>
           <Scope>Exclusive</Scope>
           <ExpirySettings>
               <ExpiryDate/>
               <TimeOfDay/>
               <TimeoutInSec ref="">3600</TimeoutInSec>
           </ExpirySettings>
           <SkipCacheLookup/>
           <SkipCachePopulation/>
         </ResponseCache>
         

  3. Verify if the cache (determined in step #2) has been defined in the specific environment (identified in step #1).

In the Apigee UI, navigate to **APIs > Environment Configuration** and check if the cache exists in the **Caches** tab in the specific environment. If the cache does not exist, then that's the cause of the error.

For example, notice in the screenshot below that the cache named `itemscache` does not exist.

![Environment Configuration Caches tab.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/responsecache-error-7.png)

Because the cache named `itemscache` is not defined in the `prod` environment, you get the error:
         
         Invalid cache resource reference does_not_exist in Step definition Response-Cache-1. Context Revision:2;APIProxy:ResponseCache;Organization:kkalckstein-eval;Environment:prod
         




### Resolution

Ensure that the cache name specified in the `<CacheResource>` element has been created in the environment where you want to deploy the API proxy.

## ResponseCacheStepAttachmentNotAllowedReq

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Response cache step definition response_cache_policy_name can not be attached more than once in the request path.
    

#### Example Error Message
    
    
    Error Deploying Revision 2 to test
    Response cache step definition Response-Cache-1 can not be attached more than once in the request path.
    

#### Example Error Screenshot

![Error deploying revision 2 to test.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/responsecache-error-6.png)

### Cause

This error occurs if the same [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy) is attached to multiple request paths within any [flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-are-flows) of an API proxy.

For example, if you have the same ResponseCache policy attached in the request Preflow of both the Proxy and Target Endpoints, then this error occurs.

### Diagnosis

  1. Identify the name of the ResponseCache policy that is attached more than once. You can find this information in the error message. For example, in the following error the name of the ResponseCache policy is Response‑Cache‑1.
         
         Error Deploying Revision 2 to test
         Response cache step definition Response-Cache-1 can not be attached more than once in the request path.
         

  2. Examine all the request flows in the Proxy and Target Endpoints of the API Proxy where the error occurred. If the same ResponseCache policy is attached in two or more request flows, then that's the cause of the error.

In the following example the same ResponseCache policy `Response-Cache-1` is configured in the request path of the default proxy endpoint PreFlow, and the default target endpoint PreFlow:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <ProxyEndpoint name="default">
             <Description/>
             <FaultRules/>
             <PreFlow name="PreFlow">
                 <Request>
                     <Step>
                         <Name>Response-Cache-1</Name>
                     </Step>
                 </Request>
             ...
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <TargetEndpoint name="default">
             <Description/>
             <FaultRules/>
             <PreFlow name="PreFlow">
                 <Request/>
                 <Response/>
             </PreFlow>
             <PostFlow name="PostFlow">
                 <Request>
                     <Step>
                         <Name>Response-Cache-1</Name>
                     </Step>
                 </Request>
             ...
         

**Tip:** In the UI, click a flow under **Proxy Endpoint** in the Navigator and a flow under **Target Endpoint**.



### Resolution

Ensure a ResponseCache policy is attached to only one request path across all flows of the API Proxy.

To correct the example shown above, remove the ResponseCache policy `Response-Cache-1` from one of the two request flows.

## ResponseCacheStepAttachmentNotAllowedResp

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Response cache step definition response_cache_policy_name can not be attached more than once in the response path.
    

#### Example Error Message
    
    
    Error Deploying Revision 2 to test
    Response cache step definition Response-Cache-1 can not be attached more than once in the response path.
    

#### Example Error Screenshot

![Error deploying revision 2 to test.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/responsecache-error-5.png)

### Cause

This error occurs if the same [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy) is attached to multiple response paths within any flows of an API proxy.

For example, if you have the same ResponseCache policy attached in the response Preflow of both the Proxy and Target Endpoints, then this error occurs.

### Diagnosis

  1. Identify the name of the ResponseCache policy that is attached more than once. You can find this information in the error message. For example, in the following error the name of the ResponseCache policy is `Response-Cache-1`.
         
         Error Deploying Revision 2 to test
         Response cache step definition Response-Cache-1 can not be attached more than once in the response path.
         

  2. Examine all the request flows in the Proxy and Target Endpoints of the API Proxy where the error occurred. If the same ResponseCache policy is attached in two or more response flows, then that's the cause of the error.

In the following example the same ResponseCache policy `Response-Cache-1` is configured in the response path of the default proxy endpoint PreFlow, and the default target endpoint PreFlow:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <ProxyEndpoint name="default">
             <Description/>
             <FaultRules/>
             <PreFlow name="PreFlow">
                 <Request>
                     <Step>
                         <Name>Response-Cache</Name>
                     </Step>
                 </Request>
                 <Response>
                     <Step>
                         <Name>Response-Cache-1</Name>
                     </Step>
                 </Response>
             </PreFlow>
             ...
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <TargetEndpoint name="default">
             <Description/>
             <FaultRules/>
             <PreFlow name="PreFlow">
                 <Request/>
                 <Response/>
             </PreFlow>
             <PostFlow name="PostFlow">
                 <Request/>
                 <Response>
                     <Step>
                         <Name>Response-Cache-1</Name>
                     </Step>
                 </Response>
             </PostFlow>
             ...
         




### Resolution

Ensure a ResponseCache policy is attached to only one response path across all flows of the API Proxy.

To correct the example shown above, remove the ResponseCache policy `Response-Cache-1` from one of the two response paths.

## InvalidMessagePatternForErrorCode

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with either of these error messages:
    
    
    Error Deploying Revision revision_number to environment
    Invalid message pattern found for error code steps.cache.InvalidSkipCacheLookUpCondition.
    

OR
    
    
    Error Deploying Revision revision_number to environment
    Invalid message pattern found for error code steps.cache.InvalidSkipCachePopulationCondition.
    

#### Example Error Message
    
    
    Error Deploying Revision 2 to prod
    Invalid message pattern found for error code steps.cache.InvalidSkipCacheLookUpCondition.
    

OR
    
    
    Error Deploying Revision 2 to prod
    Invalid message pattern found for error code steps.cache.InvalidSkipCachePopulationCondition.
    

#### Example Error Screenshot

![Error deploying revision 2 to prod - LookUp.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/responsecache-error-2.png)

OR

![Error deploying revision 2 to prod - Population.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/responsecache-error-1.png)

### Cause

This error occurs if either the `<SkipCacheLookup>` or `<SkipCachePopulation>` element in a [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy) contains an invalid condition.

### Diagnosis

  1. Examine all the ResponseCache policies in the API Proxy where the error occurred and check if there are any policies that have conditions specified for `<SkipCacheLookup>` and/or the `<SkipCachePopulation>` elements.

  2. Check if the condition specified for the `<SkipCacheLookup>` and/or the `<SkipCachePopulation>` element is invalid. If yes, then that's the cause of the error.

In the following example, the `<SkipCachePopulation>`element uses the JavaScript operator **===** to check for equal value and equal type which is invalid.
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <ResponseCache async="false" continueOnError="false" enabled="true" name="Response-Cache-1">
             <DisplayName>Response Cache-1</DisplayName>
             <Properties/>
             <CacheKey>
                 <Prefix/>
                 <KeyFragment ref="request.uri" type="string"/>
             </CacheKey>
             <Scope>Exclusive</Scope>
             <ExpirySettings>
                 <ExpiryDate/>
                 <TimeOfDay/>
                 <TimeoutInSec ref="">3600</TimeoutInSec>
             </ExpirySettings>
             <CacheLookupTimeoutInSeconds>2</CacheLookupTimeoutInSeconds>
             <SkipCacheLookup>request.header.bypass-cache === "true"</SkipCacheLookup>
         </ResponseCache>
         

Because the operator `===` is invalid, you get the error:
         
         Invalid message pattern found for error code steps.cache.InvalidSkipCacheLookUpCondition.
         




### Resolution

Ensure the condition specified for the `<SkipCacheLookup>` and/or `<SkipCachePopulation>` elements is always valid.

To correct the example [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy) shown above, you could modify the `<SkipCacheLookup>` to use the `=` operator:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResponseCache async="false" continueOnError="false" enabled="true" name="Response-Cache-1">
        <DisplayName>Response Cache-1</DisplayName>
        <Properties/>
        <CacheKey>
            <Prefix/>
            <KeyFragment ref="request.uri" type="string"/>
        </CacheKey>
        <Scope>Exclusive</Scope>
        <ExpirySettings>
            <ExpiryDate/>
            <TimeOfDay/>
            <TimeoutInSec ref="">3600</TimeoutInSec>
        </ExpirySettings>
        <CacheLookupTimeoutInSeconds>2</CacheLookupTimeoutInSeconds>
        <SkipCacheLookup>request.header.bypass-cache = "true"</SkipCacheLookup>
    </ResponseCache>
    

## CacheNotFound

### Error Message

Deployment of the API proxy through either the Apigee UI or API results in an error message like this, and the deployment status of the API Proxy is marked as partially deployed:
    
    
    Error: Cache : cache_resource, not found in organization : organization__environment.
    

#### Example Error Message
    
    
    Error Cache : Response-Cache-1, not found in organization : kkalckstein-eval__prod
    

### Cause

This error occurs if the specific cache mentioned in the error message has not been created on a specific Message Processor component.

### Resolution

Contact [Apigee Support](https://apigee.com/about/support/portal) for assistance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
