---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy/
title: ResponseCache policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:34.247934+00:00
---

# ResponseCache policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  ResponseCache policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The ResponseCache policy caches data from a backend resource, reducing the number of requests to the resource. As apps make requests to the same URI, you can use this policy to return cached responses instead of forwarding those requests to the backend server. The ResponseCache policy can improve your API's performance through reduced latency and network traffic.

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

You'll likely find ResponseCache most useful when backend data used by your API is updated only periodically. For example, imagine you have an API that exposes weather report data refreshed only every ten minutes. By using ResponseCache to return cached responses between refreshes, you can decrease the number of requests reaching the backend. This also reduces the number of network hops.

For general purpose short-term caching, considering using the [PopulateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy). That policy is used in conjunction with the [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy) (for reading cache entries) and the [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy) (for invalidating entries). 

Watch the following video for an introduction to the Response Cache policy.

**Tip:** For a discussion of antipatterns for the Response Cache policy, see [Introduction to antipatterns](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/intro).**Note:** You are limited to attaching this policy once in the proxy request flow and once in the response flow. You cannot use the ResponseCache policy in a shared flow.  
  
For a video tutorial showing how to use the policy, see [Tutorial: Implementing Response Caching within Edge](https://discuss.google.dev/t/tutorial-implementing-response-caching-within-edge/17526.html). See also Error Codes below. 

### Samples

### 10-minute cache

This sample shows how to have cached responses kept for 10 minutes.

Imagine that you have an API at the following URL:
    
    
    http://{org_name}-test.apigee.net/weather/forecastrss?w=23424778

You're using the query parameter `w` as a cache key. Apigee checks the value of the query parameter `w` whenever a request is received. If a valid (that is, non-expired) response is present in the cache, then the cached response message is returned to the requesting client.

Now imagine that you have a ResponseCache policy configured as follows.
    
    
    <ResponseCache name="ResponseCache">
        <CacheKey>
            <KeyFragment ref="request.queryparam.w" />
        </CacheKey>
        <ExpirySettings>
            <TimeoutInSeconds>600</TimeoutInSeconds>
        </ExpirySettings>
    </ResponseCache>

The first time the API proxy receives a request message for the following URL, the response is cached. On the second request within 10 minutes, a cache lookup occurs -- the cached response is returned to the app with no request forwarded to the backend service.
    
    
    http://{org_name}-test.apigee.net/weather/forecastrss?w=23424778

**Tip:** HTTP headers and query parameters are automatically populated as variables when a request is received. Any HTTP header is available as `request.header.{header_name}`, for example `request.header.user-agent`. Any query parameter is available as `request.queryparam.{queryparam_name}`, for example `request.queryparam.action`.

### Skip cache lookup

The following example shows how to have the cache lookup skipped and have the cache refreshed. See also [ this video](https://discuss.google.dev/t/using-the-responsecache-policy-responsibly-or-dont-cache-post-requests/17540.html) on the use of SkipCacheLookup. 

The optional SkipCacheLookup condition (if configured) is evaluated in the request path. If the condition evaluates to true, then the cache look up is skipped and the cache is refreshed.

A common use of conditional cache refresh is a condition that defines a specific HTTP header that causes the condition to evaluate to true. A scripted client application could be configured to periodically submit a request with the appropriate HTTP header, explicitly causing the response cache to refresh.

For example, imagine a call to an API at the following URL:
    
    
    'http://{org_name}-test.apigee.net/weather/forecastrss?w=23424778' -H "bypass-cache:true"

Now imagine the following ResponseCache policy configured on that proxy. Note that the bypass-cache condition is set to true.
    
    
    <ResponseCache name="ResponseCache">
        <CacheKey>
            <KeyFragment ref="request.queryparam.w" />
        </CacheKey>
        <!-- Explicitly refresh the cached response -->
        <SkipCacheLookup>request.header.bypass-cache = "true"</SkipCacheLookup>
        <ExpirySettings>
            <TimeoutInSeconds>600</TimeoutInSeconds>
        </ExpirySettings>
    </ResponseCache>

For more information about conditions, see [Flow variables and conditions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions).

## Element reference

The element reference describes the elements and attributes of the policy.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResponseCache async="false" continueOnError="false" enabled="true" name="Response-Cache-1">
        <DisplayName>Response Cache 1</DisplayName>
        <Properties/>
        <CacheKey>
            <Prefix/>
            <KeyFragment ref="request.uri" />
        </CacheKey>
        <Scope>Exclusive</Scope>
        <ExpirySettings>
            <ExpiryDate/>
            <TimeOfDay/>
            <TimeoutInSeconds ref="flow.variable.here">300</TimeoutInSeconds>
        </ExpirySettings>
        <CacheResource>cache_to_use</CacheResource>
        <CacheLookupTimeoutInSeconds/>
        <ExcludeErrorResponse/>
        <SkipCacheLookup/>
        <SkipCachePopulation/>
        <UseAcceptHeader/>
        <UseResponseCacheHeaders/>
    </ResponseCache>

## <ResponseCache> attributes
    
    
    <ResponseCache async="false" continueOnError="false" enabled="true" name="Response-Cache-1">

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

**Note:** You can further augment the cache key configured here by using values from response headers. For more information, see Configuring a cache key.
    
    
    <CacheKey>
        <Prefix>_string_ </Prefix>
        <KeyFragment ref="_variable_name_ " />
        <KeyFragment>_literal_string_ </KeyFragment>
    </CacheKey>

**Default:** |  N/A  
---|---  
**Presence:** | Required  
**Type:** |  N/A  
  
`<CacheKey>` constructs the name of each piece of data stored in the cache. The key is often set using a value from entity headers or query params. In those cases, you would have the element's ref attribute specify a variable containing the key value.

At runtime, `<KeyFragment>` values are prepended with either the `<Scope>` element value or `<Prefix>` value. For example, the following results in a cache key of `UserToken__apiAccessToken__`<_value_of_client_id >_:
    
    
    <CacheKey>
        <Prefix>UserToken</Prefix>
        <KeyFragment>apiAccessToken</KeyFragment>
        <KeyFragment ref="request.queryparam.client_id" />
    </CacheKey>

You use the `<CacheKey>` element in conjunction with `<Prefix>` and `<Scope>`. For more information, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys).

## <CacheLookupTimeoutInSeconds> element

Specifies the number of seconds after which an unsuccessful cache lookup will be considered a cache miss. If this occurs, flow resumes along the cache-miss path.
    
    
    <CacheLookupTimeoutInSeconds>30</CacheLookupTimeoutInSeconds>

**Default:** |  30  
---|---  
**Presence:** | Optional  
**Type:** |  Integer  
  
## <CacheResource> element

Specifies the cache where messages should be stored. Omit this element to use the included shared cache. You should specify a `CacheResource` by name if you wish to be able to administratively clear entries contained in the cache. For more on that, see [Caches API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.caches).
    
    
    <CacheResource>_cache_to_use_ </CacheResource>

**Default:** |  N/A  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
## <CacheKey>/<KeyFragment> element

Specifies a value that should be included in the cache key, creating a namespace for matching requests to cached responses.
    
    
    <KeyFragment ref="_variable_name_ "/>
    <KeyFragment>_literal_string_ </KeyFragment>

**Default:** |  N/A  
---|---  
**Presence:** | Optional  
**Type:** |  N/A  
  
This can be a key (a static name that you provide) or a value (a dynamic entry set by referencing a variable). All specified fragments combined (plus the prefix) are concatenated to create the cache key.
    
    
    <KeyFragment>apiAccessToken</KeyFragment>
    <KeyFragment ref="request.queryparam.client_id" />

You use the `<KeyFragment>` element in conjunction with `<Prefix>` and `<Scope>`. For more information, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys).

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
  
Use this value instead of `<Scope>` when you want to specify your own value rather than a `<Scope>` -enumerated value. If defined, `<Prefix>` prepends the cache key value for entries written to the cache. A `<Prefix>` element value overrides a `<Scope>` element value.

You use the `<Prefix>` element in conjunction with `<CacheKey>` and `<Scope>`. For more information, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys).

## <ExcludeErrorResponse> element

This policy can cache HTTP responses with **any** status code. That means both success and error responses can be cached, including 2xx and 3xx status codes.

Set this element to `true` (default) to exclude the error responses. Set it to `false` if you do not want to exclude cache target responses with HTTP error status codes.

**Note:** Status codes from 200 to 205 are still cached when this element is set to `true`; these are the HTTP status codes that Apigee counts as "success" codes, and you cannot exclude them with this element.

For a discussion of Response Cache patterns in which this element is useful, see [Introduction to antipatterns](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/intro).
    
    
    <ExcludeErrorResponse>true</ExcludeErrorResponse>

**Default:** |  true  
---|---  
**Presence:** | Optional  
**Type:** |  Boolean  
  
## <ExpirySettings> element

Specifies when a cache entry should expire. When present, `<TimeoutInSeconds>` overrides both `<TimeOfDay>` and `<ExpiryDate>`.
    
    
    <ExpirySettings>
      <TimeOfDay ref="time_variable">expiration_time</TimeOfDay>
      <TimeoutInSeconds ref="duration_variable">seconds_until_expiration</TimeoutInSeconds>
      <ExpiryDate ref="date_variable">expiration_date</ExpiryDate>
    </ExpirySettings>

**Default:** |  N/A  
---|---  
**Presence:** | Required  
**Type:** |  N/A  
  
## _< ExpirySettings>_/<ExpiryDate> element

Specifies the date on which a cache entry should expire. Use the form `mm-dd-yyyy`. When present, this element's sibling, `<TimeoutInSeconds>`, overrides `<ExpiryDate>`.
    
    
    <ExpirySettings>
        <ExpiryDate ref="{_date_variable_}">_expiration_date_ </ExpiryDate>
    </ExpirySettings>

**Default:** |  N/A  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
### Attributes
    
    
    <ExpiryDate ref="" />

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
ref |  The variable from which to get the value. Should not be used if this element contains a literal value. | N/A | Optional | String  
  
## <ExpirySettings>/<TimeOfDay> element

The time of day at which a cache entry should expire. Use the form `hh:mm:ss` . When present, this element's sibling, `<TimeoutInSeconds>`, overrides `<TimeOfDay>`.

Enter time of day in the format HH:mm:ss, where HH represents the hour on a 24-hour clock. For example, 14:30:00 for 2:30 in the afternoon.

For the time of day, the default locale and time zone will vary depending on where the code is running (which isn't knowable when you configure the policy).
    
    
    <ExpirySettings>
        <TimeOfDay ref="_time_variable_ ">_expiration_time_ </TimeOfDay>
    </ExpirySettings>

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
ref | Variable with the expiration time value. | N/A | Optional | String  
  
  
## <ExpirySettings>/<TimeoutInSec> element

**Note:** Deprecated. Use `TimeoutInSeconds`. If both the `TimeoutInSec` and `TimeoutInSeconds` elements are present, Apigee uses `TimeoutInSeconds`.

The number of seconds after which a cache entry should expire. 

## <ExpirySettings>/<TimeoutInSeconds> element

The number of seconds after which a cache entry should expire. When present, this element overrides its siblings, `<TimeOfDay>` and `<ExpiryDate>`.
    
    
    <ExpirySettings>
        <TimeoutInSeconds ref="_duration_variable_ ">_seconds_until_expiration_ </TimeoutInSeconds>
    </ExpirySettings>

**Note:** Provide a default timeout value to use if the ref does not receive a value from the `duration_variable`.  **Default:** |  N/A  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
### Attributes

Attribute | Description | Default | Presence | Type  
---|---|---|---|---  
ref | Variable with the timeout value. |  N/A  | Optional | String  
  
## <Scope> element

Enumeration used to construct a prefix for a cache key when a `<Prefix>` element is not provided in the `<CacheKey>` element.
    
    
    <Scope>_scope_enumeration_ </Scope>

**Default:** |  "Exclusive"  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
The `<Scope>` setting determines a cache key that is prepended according to the `<Scope>` value. For example, a cache key would take the following form when scope is set to `Exclusive` : _orgName__envName__apiProxyName__proxy|TargetName___ [ _serializedCacheKey_ ].

If a `<Prefix>` element is present in `<CacheKey>`, it supersedes a `<Scope>` element value. Valid values include the enumerations below.

You use the `<Scope>` element in conjunction with `<CacheKey>` and `<Prefix>`. For more information, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys).

### Acceptable values

Scope Value | Description  
---|---  
`Global` |  Cache key is shared across all API proxies deployed in the environment. Cache key is prepended in the form _orgName_ __ _envName_ __. If you define a `<CacheKey>` entry with the `<KeyFragment>` apiAccessToken and a `<Global>` scope, each entry is stored as `orgName__envName__apiAccessToken`, followed by the serialized value of the access token. For an API proxy deployed in an environment called 'test' in an organization called 'apifactory', access tokens would be stored under the following cache key: `apifactory__test__apiAccessToken`.  
`Application` |  API proxy name is used as the prefix. Cache key is prepended in the form _orgName__envName__apiProxyName_.  
`Proxy` |  ProxyEndpoint configuration is used as the prefix. Cache key is prepended in the form _orgName__envName__apiProxyName__proxyEndpointName_ .  
`Target` |  TargetEndpoint configuration is used as the prefix. Cache key prepended in the form _orgName__envName__apiProxyName__targetEndpointName_ .  
`Exclusive` |  Default. This is the most specific, and therefore presents minimal risk of namespace collisions within a given cache. Prefix is one of two forms:

  * If the policy is attached to the `ProxyEndpoint` flow, prefix is of the form _ApiProxyName_ProxyEndpointName_.
  * If the policy is attached at `TargetEndpoint`, prefix is of the form _ApiProxyName_TargetName_.

Cache key prepended in the form _orgName__envName__apiProxyName__proxyNameITargetName_ For example, the full string might look like this:
    
    
    apifactory__test__weatherapi__default__apiAccessToken

.   
  
## <SkipCacheLookup> element

Defines an expression that, if it evaluates to true at runtime, specifies that cache lookup should be skipped and the cache should be refreshed. See also [Using the ResponseCache policy video](https://discuss.google.dev/t/using-the-responsecache-policy-responsibly-or-dont-cache-post-requests/17540.html) on the use of `SkipCacheLookup`.
    
    
    <SkipCacheLookup>_variable_condition_expression_ </SkipCacheLookup>

**Default:** |  N/A  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
From the following example, if the bypass-cache variable is set to true in an incoming header, cache lookup is skipped and the cache is refreshed.
    
    
    <SkipCacheLookup>request.header.bypass-cache = "true"</SkipCacheLookup>

## <SkipCachePopulation> element

Defines an expression that, if it evaluates to true at runtime, specifies that a write to the cache should be skipped. See also [this video](https://discuss.google.dev/t/using-the-responsecache-policy-responsibly-or-dont-cache-post-requests/17540.html) on the use of `SkipCachePopulation`.
    
    
    <SkipCachePopulation>_variable_condition_expression_ </SkipCachePopulation>

**Default:** |  N/A  
---|---  
**Presence:** | Optional  
**Type:** |  String  
  
For example, the following would skip the cache write if the response status code was 400 or higher:
    
    
    <SkipCachePopulation>response.status.code >= 400</SkipCachePopulation>

## <UseAcceptHeader> element

Set to `true` to have a response cache entry's cache key appended with values from response Accept headers.

Apigee uses the `Accept`, `Accept-Encoding`, `Accept-Language` and `Accept-Charset` request headers when calculating the cache key. This approach prevents a client from getting a media type they did not ask for.

For example, consider if two requests come in from the same URL, where the first request accepts gzip and the second does not. The first request will be cached, and the cached entry will (probably) be a gzipped response. The second request will read the cached value and may then return a gzipped entry to a client that is not capable of reading gzip.

See Configuring a cache key for more.
    
    
    <UseAcceptHeader>false</UseAcceptHeader>

**Default:** |  false  
---|---  
**Presence:** | Optional  
**Type:** |  Boolean  
  
## <UseResponseCacheHeaders> element

Set to `true` to have HTTP response headers considered when setting the "time to live" (TTL) of the response in the cache. When this is true, Apigee considers the values of the following response headers, comparing the values with those set by `<ExpirySettings>` when setting time to live:

  * `Cache-Control s-maxage`
  * `Cache-Control max-age`
  * `Expires`



See Setting cache entry expiration for more details.
    
    
    <UseResponseCacheHeaders>false</UseResponseCacheHeaders>

**Default:** |  false  
---|---  
**Presence:** | Optional  
**Type:** |  Boolean  
  
## Usage notes

The maximum size for each cached object is 256 KB. (For detailed information on how Apigee processes cache, see [Cache internals](https://docs.cloud.google.com/apigee/docs/api-platform/cache/cache-internals).) 

Through configuration in the ResponseCache policy, you can have Apigee include HTTP response headers in setting cache entry expiration and cache keys. This section describes you can use the policy with headers to manage cache expiration and cache keys.

For more about how Apigee handles response headers with the ResponseCache policy, see [Support for HTTP response headers](https://docs.cloud.google.com/apigee/docs/api-platform/cache/http-response-caching).

**Note:** For other best practice suggestions related to the ResponseCache policy, see [Best practices for API proxy design and development](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development).

### Setting cache entry expiration

As with the [PopulateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy), you can set a response cache entry's expiration (its time to live) using the `<ExpirySettings>` element. In the ResponseCache policy, you can also have Apigee consider response headers when they're present.

To use response headers, you set the `<UseResponseCacheHeaders>` element value to true. That setting causes Apigee to consider the response headers, compare them with the value set by `<ExpirySettings>`, then use the lowest value between the two. When considering the response headers, Apigee chooses the value available as described in the following:

![Diagram that shows what happens when you set UseResponseCacheHeaders to true.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/responsecache_ttl3.png)

For example, imagine a response is cached with the following values:

  * No `Cache-Control s-maxage` value
  * A `Cache-Control max-age` value of 300
  * An `Expires` date in three days
  * An `<ExpirySettings>` `TimeoutInSeconds` value of 600.



In this case, the `Cache-Control` `max-age` value would be used for the TTL because it is lower than the `<ExpirySettings>` value and because there is no `Cache-Control s-maxage` value (which takes precedence over `max-age`).

### Configuring a cache key

As with general purpose cache policies such as the [PopulateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy), with ResponseCache you use `<CacheKey>` and `<Scope>` elements to configure cache key creation for cache entries. With ResponseCache you can also make cache keys more meaningful by having response Accept headers appended to key values.

For general information about configuring cache keys, see [Working with cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys). For information about using Accept headers, see `<UseAcceptHeader>`.

### About cache encryption

**Apigee and Apigee hybrid (version 1.4 and later):** Cache and KVM data are always encrypted.

## Flow variables

The following predefined Flow variables are populated when a ResponseCache policy is executed. For more information about Flow variables, see [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

Variables | Type | Permission | Description  
---|---|---|---  
`responsecache.{policy_name}.cachename` | String | Read-Only | Returns the cache used in the policy  
`responsecache.{policy_name}.cachekey` | String | Read-Only | Returns the key used  
`responsecache.{policy_name}.cachehit` | Boolean | Read-Only | True if the policy execution is successful  
`responsecache.{policy_name}.invalidentry` | Boolean | Read-Only | True if the cache entry in not valid  
  
## Error codes

This section describes the error messages and flow variables that are set when this policy triggers an error. This information is important to know if you are developing fault rules for a proxy. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Error code prefix

N/A

### Runtime errors

This policy does not throw any runtime errors.

### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information.Error name | Cause | Fix  
---|---|---  
`InvalidTimeout` | If the `<CacheLookupTimeoutInSeconds>` element of the `ResponseCache` policy is set to a negative number, then the deployment of the API proxy fails. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/responsecache-deployment-errors#invalidtimeout)  
`InvalidCacheResourceReference` | This error occurs if the `<CacheResource>` element in a `ResponseCache` policy is set to a name that does not exist in the environment where the API proxy is being deployed. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/responsecache-deployment-errors#invalidcacheresourcereference)  
`ResponseCacheStepAttachmentNotAllowedReq` | This error occurs if the same `ResponseCache` policy is attached to multiple request paths within any flows of an API proxy. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/responsecache-deployment-errors#responsecachestepattachmentnotallowedreq)  
`ResponseCacheStepAttachmentNotAllowedResp` | This error occurs if the same `ResponseCache` policy is attached to multiple response paths within any flows of an API proxy. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/responsecache-deployment-errors#responsecachestepattachmentnotallowedresp)  
`InvalidMessagePatternForErrorCode` | This error occurs if either the `<SkipCacheLookup>` or the `<SkipCachePopulation>` element in a `ResponseCache` policy contains an invalid condition. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/responsecache-deployment-errors#invalidmessagepatternforerrorcode)  
`CacheNotFound` | This error occurs if the specific cache mentioned in the error message has not been created on a specific Message Processor component. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/responsecache-deployment-errors#cachenotfound)  
  
### Fault variables

N/A

### Example error response

N/A

## Schema

Each policy type is defined by an XML schema (`.xsd`). For reference, [policy schemas](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) are available on GitHub.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
