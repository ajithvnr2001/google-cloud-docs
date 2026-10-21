---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy/
title: PopulateCache policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:37.158445+00:00
---

# PopulateCache policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  PopulateCache policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The PopulateCache policy configures how cached values should be written at runtime.

The Populate Cache policy is designed for writing entries in a short-term general-purpose cache. It's used in conjunction with the [Lookup Cache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy) (for reading cache entries) and the [Invalidate Cache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy) (for invalidating entries).

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

For caching the responses of backend resources, see the [Response Cache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy).

## Element reference

The following lists the elements you can configure on this policy.
    
    
    <PopulateCache async="false" continueOnError="false" enabled="true" name="Populate-Cache-1">
        <DisplayName>Populate Cache 1</DisplayName>
        <Properties/>
        <CacheKey>
            <Prefix/>
            <KeyFragment ref=""/>
        </CacheKey>
        <!-- Omit this element if you're using the included shared cache. -->
        <CacheResource/>
        <Scope>Exclusive</Scope>
        <ExpirySettings>
            <TimeoutInSeconds>300</TimeoutInSeconds>
        </ExpirySettings>
        <Source>flowVar</Source>
    </PopulateCache>

## <PopulateCache> attributes

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
  
## <CacheKey> element

Configures a unique pointer to a piece of data stored in the cache.

Cache keys are limited to a size of 2 KB.
    
    
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

## <CacheResource> element

Specifies the cache where messages should be stored.

Omit this element completely if this policy (and your corresponding LookupCache and InvalidateCache policies) is using the included shared cache.
    
    
    <CacheResource>_cache_to_use_ </CacheResource>

**Default:** |  N/A  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
For more about configuring caches, see [ General purpose caching](https://docs.cloud.google.com/apigee/docs/api-platform/cache/optimize-performance-using-cache).

## <CacheKey>/<KeyFragment> element

Specifies a value that should be included in the cache key. Specify a variable to de-reference with the `ref` attribute, or a fixed value.
    
    
    <KeyFragment ref="_variable_name_ "/>
    <KeyFragment>_literal_string_ </KeyFragment>

**Default:** |  N/A  
---|---  
**Presence:** | zero or more  
**Type:** |  N/A  
  
At runtime, Apigee creates the cache key by prepending the value obtained from the `<Scope>` element or the `<Prefix>` element, to a concatenation of the resolved values of each of the `<KeyFragment>` elements. For more information, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys).

### Attributes

Attribute | Type | Default | Required | Description  
---|---|---|---|---  
ref | string |  | No |  The variable from which to get the value. Should not be used if this element contains a literal value.  
  
## <CacheKey>/<Prefix> element

Specifies a fixed value to use as a cache key prefix.
    
    
    <Prefix>_prefix_string_ </Prefix>

**Default:** |  N/A  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
A `<Prefix>` element overrides any `<Scope>` element.

At runtime, Apigee creates the cache key by prepending the value obtained from the `<Scope>` element or the `<Prefix>` element, to a concatenation of the resolved values of each of the `<KeyFragment>` elements. For more information, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys).

## <ExpirySettings> element

Specifies when a cache entry should expire.
    
    
    <ExpirySettings>
      <!-- use exactly one of the following child elements -->
      <TimeoutInSeconds ref="duration_variable">seconds_until_expiration</TimeoutInSeconds>
      <ExpiryDate ref="date_variable">expiration_date</ExpiryDate>
      <TimeOfDay ref="time_variable">expiration_time</TimeOfDay>
    </ExpirySettings>

**Default:** |  N/A  
---|---  
**Presence:** | Required  
**Type:** |  N/A  
  
### Child elements of `<ExpirySettings>`

Use exactly one child element. The following table provides a description of the child elements of `<ExpirySettings>`:

Child Element | Description  
---|---  
`<TimeoutInSeconds>` |  The number of seconds after which a cache entry should expire. 
    
    
    <ExpirySettings>
      <TimeoutInSeconds ref="_var-containing-duration_ ">_expiry_ </TimeoutInSeconds>
    </ExpirySettings>

This element replaces the now-deprecated `TimeoutInSec` element.  
`<ExpiryDate>` |  Specifies the date on which a cache entry should expire. Specify a string in the form `mm-dd-yyyy`.
    
    
    <ExpirySettings>
      <ExpiryDate ref="_var-containing-date_ ">_expiry_ </ExpiryDate>
    </ExpirySettings>

If the date specified is in the past, the policy will apply the maximum time-to-live to the cached entry. This maximum is 30 days.  
`<TimeOfDay>` |  Specifies the time of day on which a cache entry should expire. Specify a string in the form `HH:mm:ss`, where HH represents the hour on a 24-hour clock, in the UTC time zone. For example, 14:30:00 implies 2:30 in the afternoon.
    
    
    <ExpirySettings>
      <TimeOfDay ref="_var-containing-time_ ">_expiry_ </TimeOfDay>
    </ExpirySettings>

**Notes:**

  * Specify times in the [ Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) (UTC) time zone.
  * Populate Cache time notation follows the international standard date notation defined in International Standard [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

  
  
You should specify only one of the possible child elements. If you specify multiple elements, the order of precedence is:`TimeoutInSeconds`, `ExpiryDate`, `TimeOfDay`.

With each of the above child elements of `<ExpirySettings>`, if you specify the optional `ref` attribute on the child element, the policy will retrieve the expiry value from the named context variable. If the variable is not defined, the policy uses the literal text value of the child element.

## <Scope> element

Enumeration used to construct a prefix for a cache key when a `<Prefix>` element is not provided in the `<CacheKey>` element.
    
    
    <Scope>_scope_enumeration_ </Scope>

**Default:** |  "Exclusive"  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
The `<Scope>` setting determines a cache key that is prepended according to the `<Scope>` value. For example, a cache key would take the following form when scope is set to `Exclusive`:

_orgName__envName__apiProxyName__proxy|TargetName___ [ _serializedCacheKey_ ]

If a `<Prefix>` element is present in `<CacheKey>`, it supersedes a `<Scope>` element value. Valid values include the enumerations below.

You use the `<Scope>` element in conjunction with `<CacheKey>` and `<Prefix>`. For more information, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys).

### Acceptable values

`Global` |  Cache key is shared across all API proxies deployed in the environment. Cache key is prepended in the form _orgName_ __ _envName_ __. If you define a `<CacheKey>` entry with the `<KeyFragment>` apiAccessToken and a `<Global>` scope, each entry is stored as `orgName__envName__apiAccessToken`, followed by the serialized value of the access token. For an API proxy deployed in an environment called 'test' in an organization called 'apifactory', access tokens would be stored under the following cache key: `apifactory__test__apiAccessToken`.  
---|---  
`Application` |  API proxy name is used as the prefix. Cache key is prepended in the form _orgName__envName__apiProxyName_.  
`Proxy` |  ProxyEndpoint configuration is used as the prefix. Cache key is prepended in the form _orgName__envName__apiProxyName__proxyEndpointName_ .  
`Target` |  TargetEndpoint configuration is used as the prefix. Cache key prepended in the form _orgName__envName__apiProxyName__targetEndpointName_ .  
`Exclusive` |  Default. This is the most specific, and therefore presents minimal risk of namespace collisions within a given cache. Prefix is one of two forms:

  * If the policy is attached to the `ProxyEndpoint` flow, prefix is of the form _ApiProxyName_ProxyEndpointName_.
  * If the policy is attached at `TargetEndpoint`, prefix is of the form _ApiProxyName_TargetName_.

Cache key prepended in the form _orgName__envName__apiProxyName__proxyNameITargetName_ For example, the full string might look like this:
    
    
    apifactory__test__weatherapi__default__apiAccessToken

.   
  
## <Source> element

Specifies the variable whose value should be written to the cache.
    
    
    <Source>_source_variable_ </Source>

**Default:** |  N/A  
---|---  
**Presence:** | Required  
**Type:** |  String  
**Notes:**

  * _JSON objects_ are exclusively stored in the [in-memory cache (L1)](https://docs.cloud.google.com/apigee/docs/api-platform/cache/cache-internals#inmemoryandpersistentcachelevels). 
  * If you intend to cache these objects in [persistent chache (L2)](https://docs.cloud.google.com/apigee/docs/api-platform/cache/cache-internals#inmemoryandpersistentcachelevels), we recommend serializing them into a _string_ format. 
  * By following this practice, you can effectively utilize the L2 cache and maximize caching efficiency. 
  * For more information, see [Cache internals](https://docs.cloud.google.com/apigee/docs/api-platform/cache/cache-internals).  




## Usage notes

Use this policy for general purpose caching. At runtime, the `<PopulateCache>` policy writes data from the variable you specified in the `<Source>` element to the cache you specified in the `<CacheResource>` element. You can use the `<CacheKey>`, `<Scope>`, and `<Prefix>` elements to specify a key that you can use from the `<LookupCache>` policy to retrieve the value. Use the `<ExpirySettings>` element to configure when the cached value should expire.

General purpose caching with the PopulateCache policy, [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy), and [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy) uses either a cache you configure or a shared cache that's included by default. In most cases, the underlying shared cache should meet your needs. To use this cache, simply omit the `<CacheResource>` element.

**Cache limits** : [Various cache limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits) apply, such as name and value size, total number of caches, the number of items in a cache, and expiration.

For more about the underlying data store, see [Cache internals](https://docs.cloud.google.com/apigee/docs/api-platform/cache/cache-internals).

### About cache encryption

**Apigee and Apigee hybrid (version 1.4 and later):** Cache and KVM data are always encrypted.

## Error codes

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP Status | Occurs when  
---|---|---  
`policies.populatecache.EntryCannotBeCached` | `500` | An entry cannot be cached. The message object being cached is not an instance of a class that is Serializable.  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information. Error name | Cause | Fix  
---|---|---  
`InvalidCacheResourceReference` | This error occurs if the `<CacheResource>` element in the `PopulateCache` policy is set to a name that does not exist in the environment where the API proxy is being deployed. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/populate-cache-deployment-errors#invalidcacheresourcereference)  
`CacheNotFound` | The cache specified in the `<CacheResource>` element does not exist. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/populate-cache-deployment-errors#cachenotfound)  
  
### Fault variables

These variables are set when this policy triggers an error. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name = "EntryCannotBeCached"`  
`populatecache.policy_name.failed` | policy_name is the user-specified name of the policy that threw the fault. | `populatecache.POP-CACHE-1.failed = true`  
  
### Example error response
    
    
    {
      "fault": {
        "faultstring": "[entry] can not be cached. Only serializable entries are cached.",
        "detail": {
          "errorcode": "steps.populatecache.EntryCannotBeCached"
        }
      }
    }

### Example fault rule
    
    
    <FaultRule name="Populate Cache Fault">
        <Step>
            <Name>AM-EntryCannotBeCached</Name>
            <Condition>(fault.name Matches "EntryCannotBeCached") </Condition>
        </Step>
        <Condition>(populatecache.POP-CACHE-1.failed = true) </Condition>
    </FaultRule>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
