---
url: https://docs.cloud.google.com/apigee/docs/api-platform/cache/optimize-performance-using-cache/
title: General purpose caching \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:21.626965+00:00
---

# General purpose caching  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/cache/optimize-performance-using-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  General purpose caching Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

You can use policies to store data in a general purpose cache for faster retrieval. Using the following policies, your proxy can store and retrieve cached data at runtime:

  * [Populate Cache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy) to add data to the cache.
  * [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy) to access cached data.
  * [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy) to flush the cache.

**Note:** This topic describes general purpose caching. For information about response caching, see [Response Cache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy), a reference with examples on the Response Cache policy.

These policies are designed for general caching of data used by your proxies.

The sample code in this topic is based on the [Outbound OAuth sample proxy](https://github.com/apigee/api-platform-samples/tree/master/sample-proxies/outbound-oauth) on GitHub. This sample uses the cache policy to store an OAuth access token for re-use across multiple outbound calls.

In the following example, an OAuth access token is written to the cache using a PopulateCache policy. The OAuth token is retrieved for subsequent requests by a LookupCache policy. Once the access token expires, JavaScript is used to retrieve a new access token, which is in turn cached by the PopulateCache policy.

## Populate the cache

Use the PopulateCache policy to write data to the cache. This example writes an OAuth access token to the cache. For policy reference information, see [Populate Cache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy).

**Note:** Cache keys are limited to a size of 2 KB. 
    
    
    <PopulateCache name="token-cache">
        <!-- The cache to write to. -->
        <CacheResource>mycache</CacheResource>
        <!-- The source of the data, a variable containing the value. -->
        <Source>twitter-translate.apiAccessToken</Source>
        <!-- An enumeration representing a prefix for namespace scope. -->
        <Scope>Exclusive</Scope>
        <!-- A unique pointer (a flow variable value) to the data. Use this later to retrieve it. -->
        <CacheKey>
            <KeyFragment>apiAccessToken</KeyFragment>
            <KeyFragment ref="request.queryparam.client_id"></KeyFragment>
        </CacheKey>
        <!-- Entries placed into the cache with this policy will expire after 600 seconds. -->
        <ExpirySettings>
            <TimeoutInSec>600</TimeoutInSec>
        </ExpirySettings>
    </PopulateCache>

Variables can be populated by policies or by code. The `Source` variable in this example is populated by the following JavaScript call: `context.setVariable('twitter-translate.apiAccessToken', getAccessToken());`

For more on cache keys, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys).

## Lookup cached data

You can retrieve cached values with the LookupCache policy. The following LookupCache policy reads a value from `mycache` and writes the value to the variable `twitter-translate.apiAccessToken`. For policy reference information, see [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy).
    
    
    <LookupCache name="token-cache">
        <!-- The cache to read from. -->
        <CacheResource>mycache</CacheResource>
        <!-- Where to assign the retrieved value - here, a variable. -->
        <AssignTo>twitter-translate.apiAccessToken</AssignTo>
        <!-- An enumeration representing a prefix for namespace scope. -->
        <Scope>Exclusive</Scope>
        <!-- The unique pointer (a flow variable value) that was used to store the data in the cache. -->
    
        <CacheKey>
            <KeyFragment>apiAccessToken</KeyFragment>
            <KeyFragment ref="request.queryparam.client_id"></KeyFragment>
        </CacheKey>
    </LookupCache>

## Invalidate the cache

The cache can be invalidated explicitly by specifying an HTTP header. When a request that contains the specified HTTP header is received, the cache will be flushed. For policy reference information, see [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy).
    
    
    <InvalidateCache name="InvalidateMyCache">
        <!-- The cache to invalidate. -->
        <CacheResource>test-cache</CacheResource>
        <!-- An enumeration representing a prefix for namespace scope. -->
        <Scope>Exclusive</Scope>
        <!-- Fragments constructing the unique pointer used when 
            the data was put into the cache. -->
        <CacheKey>
            <KeyFragment>apiAccessToken</KeyFragment>
            <KeyFragment ref="request.queryparam.client_id" />
        </CacheKey>
        <PurgeChildEntries>true</PurgeChildEntries>
    </InvalidateCache>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
