---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys/
title: Working with cache keys \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:09.411925+00:00
---

# Working with cache keys  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Working with cache keys Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

When using cache policies, you ensure the uniqueness of cached value keys by configuring cache keys. A cache key, along with other values you can configure, gives you a reliable way to get out the same data that you put in. You use cache keys with the [PopulateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy), [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy), [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy), and [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy). 

Apigee uses the values of configuration elements -- `<Scope>`, `<CacheKey>`/`<Prefix>`, and `<CacheKey>`/`<KeyFragment>` \-- to compose a value for the _cache key_ , which is an identifier that is associated with the value in the cache. Cache key composition works the same way with all of the cache policies. 

With the following cache policy configuration elements, you can create a cache key: 

Cache Configuration Element | Description  
---|---  
`<Scope>` or `<CacheKey>` / `<Prefix>` |  Use either the `<Scope>` or the `<CacheKey>` `<Prefix>` elements to configure a prefix to apply to the final cache key. `<Scope>` enumerates a list of predefined values. The `<CacheKey>` `<Prefix>` element overrides `<Scope>` with a fixed value of your own choosing.   
`<CacheKey>` / `<KeyFragment>` |  Use one or more `<CacheKey>` `<KeyFragment>` elements combined to specify a unique identifier for cache entries. KeyFragment values can be static literals or set from variables.   
  
Apigee composes the cache key of two parts, the prefix part and the composite fragment part, separated by a double-underscore. 

> _PREFIX_PART_ ___FRAGMENT_PART_

The prefix part is determined by the `<Scope>` element, or the `<CacheKey>` `<Prefix>` element if it is present. The fragment part is composed of each of the values from each `<KeyFragment>` element, joined by double-underscores. 

With the [Response Cache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy), you can optionally append this cache key with values from the response Accept header. 

## Using <CacheKey>

The `<CacheKey>` element configures how Apigee will create a unique identifier (a key) for each cache entry it creates. When Apigee retrieves the cached value, it uses the cache key to locate the correct value. In the ResponseCache policy, one configuration defines the key for both caching and retrieval. In the PopulateCache and LookupCache policies, each policy must have identical `<CacheKey>`elements to ensure that a value retrieved from the cache corresponds to a value put there. 

The `<CacheKey>` element can include a single optional `<Prefix>` element as well as one or more `<KeyFragment>` elements. At runtime, Apigee concatenates the values determined from each part two underscores between them to make up the cache key. 

For example, the following configuration creates a value of `myprefix__hello__world` for use in the cache key: 
    
    
    <CacheKey>
        <Prefix>myprefix</Prefix>
        <KeyFragment>hello</KeyFragment>
        <KeyFragment>world</KeyFragment>
    <CacheKey>

You can configure Apigee to use a dynamically composed cache key by referencing the variable in a `<KeyFragment>` element, as shown here: 
    
    
    <KeyFragment ref="_variable_name_ "/>

For example, to make the cache key value incorporate the Content-Type of the request message, you do as follows: 
    
    
    <KeyFragment ref="request.header.Content-Type"/>

Consider the following configuration:
    
    
    <CacheKey>
      <Prefix>system1</Prefix>
      <KeyFragment>apiAccessToken</KeyFragment>
      <KeyFragment ref="request.header.Content-Type" />
      <KeyFragment>bar</KeyFragment>
    </CacheKey>

If the `request.header.Content-Type` variable has the value `application/json`, this will result in a cache key of `system1__apiAccessToken__application/json__bar`. 

You can use platform-defined or custom variables in a `ref` attribute. 

###  Cache keys derived from query parameters 

Using variables such as request.queryparam.<queryparam_name> and request.querystring, you can configure a cache key so that the key includes parts of a request's query string. For example, the following URL uses two query parameters -- param1 and param2 -- that you can use in your cache key: 
    
    
    http://myaccount.apigee.net/mydata?param1=value1&param2=value2

Your `<CacheKey>` element can incorporate these values with a configuration such as the following: 
    
    
    <CacheKey>
        <KeyFragment ref="request.queryparam.param1" />
        <KeyFragment ref="request.queryparam.param2" />
    <CacheKey>

At runtime, the cache key would include the param values concatenated, as in the following: 

_prefix_part_ __value1__value2

Rather than specifying multiple distinct query parameters, an alternative is to use the `request.querystring` variable, which inserts the entire string of parameters literally as part of the cache key. Keep in mind that while this method accounts for all of the parameters, if the order of parameters varies from one request to the next then the key will be different. In other words, `param1=value1&param2=value2` and `param2=value2&param1=value1` don't result in the same cache key value. 

## Using <Scope> and <Prefix>

The `<Scope>` and `<CacheKey>` / `<Prefix>` elements provide a way to organize cached values into a namespace. Apigee prepends a value derived from them to your cache key. The advantage of using a scope or prefix in your cache key is that you can invalidate all the values that share a single prefix, with one call to the [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy). 

The `<Scope>` element is used by default. It is an enumeration whose values range from broad to narrow, with the narrowest as the default. This default value is used unless you specify another value or specify a `<Prefix>` element value. You can override the `<Scope>` value by using a `<CacheKey>` / `<Prefix>` element, and so specify a custom value for namespacing. 

For example, the `<Scope>` value "Global" -- the broadest scope -- represents the organization and environment name. So if your proxy is deployed in an organization called 'mycompany' and an environment named 'prod', the resulting preprended value will be the following: 
    
    
    mycompany__prod__[FRAGMENT_PART]

As described in [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy), the scope can be configured for increasing specificity from Global to Exclusive. An Exclusive scope is the most specific, and therefore represents minimal risk of namespace collisions within a given cache. Each cache entry with an Exclusive scope is prefixed in the following form: 
    
    
    orgName__envName__apiProxyName__deployedRevisionNumber___nameof_(proxyEndpoint|targetEndpoint)__[serializedCacheKey]

Some examples follow. These assume that the 16th revision of your proxy named 'weatherapi' is deployed in an organization called 'mycompany' and an environment named 'prod', and the proxyEndpoint name is 'default', and that the cache policy is attached to a flow in the proxyEndpoint. 

Configuration | Result  
---|---  
      
    
    <Scope>Global</Scope>
    <CacheKey>
      <KeyFragment>hello</KeyFragment>
      <KeyFragment>world</KeyFragment>
    <CacheKey>

| `mycompany__prod__hello__world`.  
      
    
    <Scope>Exclusive</Scope>
    <CacheKey>
        <KeyFragment>hello</KeyFragment>
        <KeyFragment>world</KeyFragment>
    <CacheKey>

| `mycompany__prod__weatherapi__16__default__hello__world`  
      
    
    <Scope>Exclusive</Scope>
    <CacheKey>
        <Prefix>system1</Prefix>
        <KeyFragment>hello</KeyFragment>
        <KeyFragment>world</KeyFragment>
    <CacheKey>

| `system1__hello__world` In this case, the `<Prefix>` element overrides `<Scope>`, which is why the namespace `system1` appears in the result.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
