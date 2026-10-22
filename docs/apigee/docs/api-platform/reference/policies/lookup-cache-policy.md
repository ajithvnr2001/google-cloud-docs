---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy/
title: LookupCache policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:43.767827+00:00
---

# LookupCache policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  LookupCache policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The LookupCache policy configures how cached values should be retrieved at runtime.

This policy is intended for use in general purpose short-term caching. It is used in conjunction with the [PopulateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy) (for writing entries) and the [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy) (for invalidating entries).

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

For caching the responses of backend resources, see the [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy).

## Element reference

The following lists the elements you can configure on this policy.
    
    
    <LookupCache async="false" continueOnError="false" enabled="true" name="Lookup-Cache-1">
        <DisplayName>Lookup Cache 1</DisplayName>
        <CacheKey>
            <Prefix/>
            <KeyFragment ref=""/>
        </CacheKey>
        <!-- Omit this element if you're using the included shared cache. -->
        <CacheResource/>
        <CacheLookupTimeoutInSeconds/>
        <Scope>Exclusive</Scope>
        <AssignTo>flowVar</AssignTo>
    </LookupCache>

A shared cache is included by default. To use the shared cache, omit the `<CacheResource>` element in this policy configuration.

For more about the underlying data store, see [Cache internals](https://docs.cloud.google.com/apigee/docs/api-platform/cache/cache-internals). For more about configuring caches, see [General purpose caching](https://docs.cloud.google.com/apigee/docs/api-platform/cache/optimize-performance-using-cache).

## <LookupCache> attributes

The following table describes attributes that are common to all policy parent elements:

Attribute | Description | Default | Presence  
---|---|---|---  
`name` |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name. | N/A | Required  
`continueOnError` |  Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also:

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

| false | Optional  
`enabled` |  Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow. | true | Optional  
`async` |  This attribute is deprecated. | false | Deprecated  
  
## <DisplayName> element

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, natural-language name.
    
    
    <DisplayName>Policy Display Name</DisplayName>

Default |  N/A If you omit this element, the value of the policy's `name` attribute is used.  
---|---  
Presence | Optional  
Type | String  
  
## <AssignTo> element

Specifies the variable where the cache entry is assigned after it has been retrieved from the cache. The variable must be writable. If the cache lookup doesn't retrieve a value, the variable will not be set.
    
    
    <AssignTo>variable_to_receive_cached_value</AssignTo>

**Default:** |  N/A  
---|---  
**Presence:** | Required  
**Type:** |  String  
  
## <CacheKey> element

Configures a unique pointer to a piece of data stored in the cache.
    
    
    <CacheKey>
        <Prefix>_string_ </Prefix>
        <KeyFragment ref="_variable_name_ " />
        <KeyFragment>_literal_string_ </KeyFragment>
    </CacheKey>

**Default:** |  N/A  
---|---  
**Presence:** | Required  
**Type:** |  N/A  
  
`<CacheKey>` constructs the name of each piece of data stored in the cache.

At runtime, `<KeyFragment>` values are prepended with either the `<Scope>` element value or `<Prefix>` value. For example, the following results in a cache key of `UserToken__apiAccessToken__`<_value_of_client_id >_:
    
    
    <CacheKey>
        <Prefix>UserToken</Prefix>
        <KeyFragment>apiAccessToken</KeyFragment>
        <KeyFragment ref="request.queryparam.client_id" />
    </CacheKey>

You use the `<CacheKey>` element in conjunction with `<Prefix>` and `<Scope>`. For more information, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys).

## <CacheLookupTimeoutInSeconds> element

Specifies the number of seconds after which an unsuccessful cache lookup will be considered a cache miss. If this occurs, flow resumes along the cache-miss path.
    
    
    <CacheLookupTimeoutInSeconds>12</CacheLookupTimeoutInSeconds>

**Default:** |  12  
---|---  
**Presence:** | Optional  
**Type:** |  Integer  
  
## <CacheResource> element

Specifies the cache where messages should be stored.

Omit this element completely if this policy (and your corresponding PopulateCache and InvalidateCache policies) is using the included shared cache.
    
    
    <CacheResource>_cache_to_use_ </CacheResource>

**Default:** |  N/A  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
For more about configuring caches, see [General purpose caching](https://docs.cloud.google.com/apigee/docs/api-platform/cache/optimize-performance-using-cache).

## <CacheKey>/<KeyFragment> element

Specifies a value that should be included in the cache key. Specify a variable to de-reference with the `ref` attribute, or a fixed value.
    
    
    <KeyFragment ref="_variable_name_ "/>
    <KeyFragment>_literal_string_ </KeyFragment>

**Default:** |  N/A  
---|---  
**Presence:** | Optional  
**Type:** |  N/A  
  
At runtime, Apigee creates the cache key by prepending the value obtained from the `<Scope>` element or the `<Prefix>` element, to a concatenation of the resolved values of each of the `<KeyFragment>` elements. For more information, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys).

### Attributes

Attribute | Type | Default | Required | Description  
---|---|---|---|---  
ref | string |  | No |  The variable from which to get the value. Should not be used if this element contains a literal value.  
  
## <CacheKey>/<Prefix> element

Specifies a value to use as a cache key prefix.
    
    
    <Prefix>_prefix_string_ </Prefix>

**Default:** |  N/A  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
A `<Prefix>` element overrides any `<Scope>` element.

At runtime, Apigee creates the cache key by prepending the value obtained from the `<Scope>` element or the `<Prefix>` element, to a concatenation of the resolved values of each of the `<KeyFragment>` elements. For more information, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys).

## <Scope> element

Enumeration used to construct a prefix for a cache key when a `<Prefix>` element is not provided in the `<CacheKey>` element.
    
    
    <Scope>_scope_enumeration_ </Scope>

**Default:** |  "Exclusive"  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
The `<Scope>` setting determines a cache key that is prepended according to the `<Scope>` value. For example, a cache key would take the following form when scope is set to `Exclusive` : _orgName__envName____application_ _Name__proxy|TargetName___ [ _serializedCacheKey_ ].

If a `<Prefix>` element is present in `<CacheKey>`, it supersedes a `<Scope>` element value. Valid values include the enumerations below.

For more information, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys).

### Acceptable values

`Global` |  Cache key is shared across all API proxies deployed in the environment. Cache key is prepended in the form _orgName_ __ _envName_ __. If you define a `<CacheKey>` entry with the `<KeyFragment>` apiAccessToken and a `<Global>` scope, each entry is stored as `orgName__envName__apiAccessToken`, followed by the serialized value of the access token. For an API proxy deployed in an environment called 'test' in an organization called 'apifactory', access tokens would be stored under the following cache key: `apifactory__test__apiAccessToken`.  
---|---  
`Application` |  API proxy name is used as the prefix. Cache key is prepended in the form _orgName__envName____application_ _Name_.  
`Proxy` |  ProxyEndpoint configuration is used as the prefix. Cache key is prepended in the form _orgName__envName____application_ _Name__proxyEndpointName_ .  
`Target` |  TargetEndpoint configuration is used as the prefix. Cache key prepended in the form _orgName__envName____application_ _Name__targetEndpointName_ .  
`Exclusive` |  Default. This is the most specific, and therefore presents minimal risk of namespace collisions within a given cache. Prefix is one of two forms:

  * If the policy is attached to the `ProxyEndpoint` flow, prefix is of the form _ApiProxyName_ProxyEndpointName_.
  * If the policy is attached at `TargetEndpoint`, prefix is of the form _ApiProxyName_TargetName_.

Cache key prepended in the form _orgName__envName____application_ _Name__proxyNameITargetName_ For example, the full string might look like this:
    
    
    apifactory__test__weatherapi__default__apiAccessToken

.   
  
## Usage notes

Use this policy for general-purpose caching. At runtime, the LookupCache policy retrieves a value from the cache, assigning the value to the variable you specify with the AssignTo element (if no value is retrieved, the variable will not be set). It looks for the value based on a cache key created through configuration that combines the CacheKey and Scope elements. In other words, to retrieve a particular value added to the cache by a PopulateCache policy, your LookupCache policy must have cache key-related elements configured in the same way as the PopulateCache policy.

General purpose caching with the [PopulateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy), [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy), and [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy) uses either a cache you configure or a shared cache that's included by default. In most cases, the underlying shared cache should meet your needs. To use the default cache, simply omit the `<CacheResource>` element.

For more about configuring caches, see [General purpose caching](https://docs.cloud.google.com/apigee/docs/api-platform/cache/optimize-performance-using-cache). For more about the underlying data store, see [Cache internals](https://docs.cloud.google.com/apigee/docs/api-platform/cache/cache-internals).

## Flow variables

Flow variables can be used to configure dynamic runtime behavior for policies and flows, based on HTTP headers or message content, or the context available in the Flow. For more information about flow variables, see [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

The following predefined Flow variables are available after you customize the behavior of the cache you define in a LookupCache policy.

Variables | Type | Permission | Description  
---|---|---|---  
lookupcache.{policy-name}.cachename | String | Read-Only | Returns the cache name used in the policy.  
lookupcache.{policy-name}.cachekey | String | Read-Only | Returns the key used.  
lookupcache.{policy-name}.cachehit | Boolean | Read-Only | True if the policy found a value for the specified cache key.  
lookupcache.{policy-name}.assignto | String | Read-Only | Returns the variable to which cache is assigned.  
  
## Error codes

This section describes the error messages and flow variables that are set when this policy triggers an error. This information is important to know if you are developing fault rules for a proxy. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Error code prefix

N/A

### Runtime errors

This policy does not throw any runtime errors.

### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information. Error name | Cause | Fix  
---|---|---  
`InvalidCacheResourceReference` | This error occurs if the `<CacheResource>` element is set to a name which does not exist in the environment where the API proxy is being deployed. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/lookup-cache-deployment-errors#invalidcacheresourcereference)  
`InvalidTimeout` | If the `<CacheLookupTimeoutInSeconds>` element is set to a negative number, then the deployment of the API proxy fails. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/lookup-cache-deployment-errors#invalidtimeout)  
`CacheNotFound` | This error occurs if the specific cache mentioned in the error message has not been created on a specific Message Processor component.  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/lookup-cache-deployment-errors#cachenotfound)  
  
### Fault variables

N/A

### Example error response

N/A

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
