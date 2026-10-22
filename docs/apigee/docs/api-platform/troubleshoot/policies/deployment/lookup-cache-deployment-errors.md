---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/lookup-cache-deployment-errors/
title: Lookup Cache policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:45.965990+00:00
---

# Lookup Cache policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/lookup-cache-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Lookup Cache policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/lookup-cache-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/lookup-cache-deployment-errors/).

## InvalidTimeout

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    CacheLookupTimeoutInSeconds value value should be greater than zero.
    

#### Example Error Message
    
    
    Error Saving Revision 2
    CacheLookupTimeoutInSeconds -1 value should be greater than zero.
    

#### Example Error Screenshot

![Error saving revision 2.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/lookupcache-error-1.png)

### Cause

If the `<CacheLookupTimeoutInSeconds>` element of a [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy) is set to a negative number, then the deployment of the API proxy fails.

For example, if the `<CacheLookupTimeoutInSeconds>` element is `-1`, then the deployment of the API proxy fails.

### Diagnosis

  1. Identify the invalid value specified for the `<CacheLookupTimeoutInSeconds>` element in the [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy). You can find this information in the error message. For example, in the following error, the invalid value used for `<CacheLookupTimeoutInSeconds>` element is `-1`:
         
         CacheLookupTimeoutInSeconds -1 value should be greater than zero.
         

  2. Examine all the LookupCache policies in the specific API Proxy where the failure has occurred. There could be one or more LookupCache policies in which the `<CacheLookupTimeoutInSeconds>` element is specified. Identify the LookUpCache policy where the invalid value (identified in step #1 above) is specified for `<CacheLookupTimeoutInSeconds>` element.

For example, the following policy configuration specifies the value of `<CacheLookupTimeoutInSeconds>` of `-1`, which matches the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <LookupCache async="false" continueOnError="false" enabled="true" name="LookupCache-Token">
             <DisplayName>LookupCache-Token</DisplayName>
             <Properties/>
             <CacheKey>
                 <Prefix/>
                 <KeyFragment ref="request.queryparam.client_id"/>
             </CacheKey>
             <CacheLookupTimeoutInSeconds>-1</CacheLookupTimeoutInSeconds>
             <Scope>Exclusive</Scope>
             <ExpirySettings>
                 <TimeoutInSec>3600</TimeoutInSec>
             </ExpirySettings>
             <AssignTo>usertoken</AssignTo>
         </LookupCache>
         

  3. If the `<CacheLookupTimeoutInSeconds>` is specified as a negative integer, then that's the cause of the error.




### Resolution

Ensure that the value for the `<CacheLookupTimeoutInSeconds>` element of the LookupCache policy is always specified as a non-negative integer.

To correct the example LookupCache policy shown above, you could modify the `<CacheLookupTimeoutInSeconds>` element to `30`.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <LookupCache async="false" continueOnError="false" enabled="true" name="LookupCache-Token">
        <DisplayName>LookupCache-Token</DisplayName>
        <Properties/>
        <CacheKey>
            <Prefix/>
            <KeyFragment ref="request.queryparam.client_id"/>
        </CacheKey>
        <CacheResource>tokencache</CacheResource>
        <CacheLookupTimeoutInSeconds>30</CacheLookupTimeoutInSeconds>
        <Scope>Exclusive</Scope>
        <ExpirySettings>
            <TimeoutInSec>3600</TimeoutInSec>
        </ExpirySettings>
        <AssignTo>usertoken</AssignTo>
    </LookupCache>
    

## InvalidCacheResourceReference

### Error Message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Invalid cache resource reference [cache_resource] in Step definition [populate_cache_policy_name]. Context Revision:[revision_number];APIProxy:ResponseCache;Organization:[organization];Environment:[environment]
    

#### Example Error Message
    
    
    Error Deploying Revision 2 to test
    Invalid cache resource reference tokencache in Step definition LookupCache-Token. Context Revision:2;APIProxy:TestCache;Organization:kkalckstein-eval;Environment:test
    

#### Example Error Screenshot

![Error deploying revision 2 to test.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/lookupcache-error-2.png)

### Cause

This error occurs if the `<CacheResource>` element is set to a name which does not exist in the environment where the API proxy is being deployed.

### Diagnosis

  1. Identify the invalid cache used in `<CacheResource>` element of the [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy) and the environment where the error occurred. You can find both of these items in the error message. For example, in the following error, the name of the invalid cache is `tokencache` and the environment name is `test`.
         
         Invalid cache resource reference tokencache in Step definition LookupCache-Token. Context Revision:2;APIProxy:TestCache;Organization:kkalckstein-eval;Environment:test
         

  2. Examine all the LookupCache policies in the specific API Proxy where the failure has occurred. Identify the specific LookupCache policy where the invalid cache (identified in step #1) is specified in `<CacheResource>` element is specified.

For example, the following policy specifies the value of `<CacheResource>` as `tokencache`, which matches the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <LookupCache async="false" continueOnError="false" enabled="true" name="LookupCache-Token">
             <DisplayName>LookupCache-Token</DisplayName>
             <Properties/>
             <CacheKey>
                 <Prefix/>
                 <KeyFragment ref="request.queryparam.client_id"/>
             </CacheKey>
             <CacheResource>tokencache</CacheResource>
             <CacheLookupTimeoutInSeconds/>
             <Scope>Exclusive</Scope>
             <ExpirySettings>
                 <TimeoutInSec>3600</TimeoutInSec>
             </ExpirySettings>
             <AssignTo>usertoken</AssignTo>
         </LookupCache>
         

  3. Verify if the cache (determined in step #1) has been defined in the specific environment (identified in step #1).

In the Apigee UI, navigate to **ADMIN > Environment > test** and check if the cache exists in the **Caches** tab of **Environment Configuration**. If the cache does not exist, then that's the cause of the error.

For example, notice in the screenshot below that the cache named `tokencache` does not exist.

![Environment Configuration Caches tab.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/lookupcache-error-3.png)

Because the cache named `tokencache` is not defined in the `test` environment, you get the error:
         
         Invalid cache resource reference tokencache in Step definition LookupCache-Token. Context Revision:2;APIProxy:TestCache;Organization:kkalckstein-eval;Environment:test
         
         




### Resolution

Ensure that the cache name specified in the `<CacheResource>` element has been created in the environment where you want to deploy the API proxy.

## CacheNotFound

### Error Message

Deployment of the API proxy through either the Apigee UI or API results in an error message like this, and the deployment status of the API Proxy is marked as partially deployed:
    
    
    Error: Cache : cache_resource, not found in organization : organization__environment.
    

### Example Error Message
    
    
    Error Cache : configCache, not found in organization : kkalckstein-eval__test
    

### Cause

This error occurs if the specific cache mentioned in the error message has not been created on a specific Message Processor component.

### Resolution

Contact [Apigee Support](https://apigee.com/about/support/portal) for assistance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
