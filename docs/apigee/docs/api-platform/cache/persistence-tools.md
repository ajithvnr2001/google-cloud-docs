---
url: https://docs.cloud.google.com/apigee/docs/api-platform/cache/persistence-tools/
title: Caching and persistence overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:35.659031+00:00
---

# Caching and persistence overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/cache/persistence-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Caching and persistence overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee persistence features include caches, key value maps, and property sets. If you are using Apigee hybrid, you can use Kubernetes secrets to persist sensitive data.

Feature | Use  
---|---  
Caches | Using policies for general purpose caching, you can persist any objects your proxy requires across multiple request/response sessions. You can also cache the response of a backend resource with the [ `ResponseCache` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy). Response caching is especially helpful when backend data is updated only periodically. The `ResponseCache` policy can reduce calls to backend data sources.  
Key value maps | Key value maps (KVMs) provide a general runtime store for data that may change periodically. For example: user session data, shopping cart, etc. KVM entries can be encrypted.  
Property sets | Property sets are good for storing configuration data that doesn't change often.  
Kubernetes secrets | (Apigee hybrid only) Use Secrets to store sensitive data such as user credentials.  
  
##  Caching 

Environment-scoped cache resources are created dynamically when a cache policy executes within an API proxy flow. Cache policies include the [PopulateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy), [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy), [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy), and [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy). 

A cached item stays in memory (L1) for one second. You cannot change this configuration. After one second, the cached object is placed in a database (L2) where it is available until the cache expires. For details, see [In-memory persistent cache levels](https://docs.cloud.google.com/apigee/docs/api-platform/cache/cache-internals#inmemoryandpersistentcachelevels). You manage cache details, such as expiry time, through configuration of a cache policy. An Apigee API is provided that allows you to [list and delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest#rest-resource:-v1.organizations.environments.caches) cache resources. 

When using cache policies, you ensure the uniqueness of cached value keys by configuring [cache keys](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/working-cachekeys). A cache key, along with other values you can configure, gives you a reliable way to get out the same data that you put in. Cache size and availability is subject to certain [limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#persistence:-cache,-kvm,-property-sets).

You might want to use a cache to:

  * **Reduce latency and traffic.** Requests are satisfied in a shorter time and with reused representations.
  * **Persist data across transactions.** You can store session data for reuse across HTTP transactions.
  * **Support security.** Scope access to cache entries so they can be accessed only in a particular environment or by a specific API proxy.



### Backend response caching

You can cache the response of a backend resource with the [`ResponseCache` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy).

This is especially helpful when backend data is updated only periodically. The `ResponseCache` policy can reduce calls to backend data sources.

Through the `ResponseCache` policy, you can also have Apigee look at certain HTTP response caching headers and take actions according to header directives. For example, on responses from backend targets, Apigee supports the `Cache-Control` header. This header can be used to control the maximum age of a cached response, among other things. For more information, see [Support for HTTP response headers](https://docs.cloud.google.com/apigee/docs/api-platform/cache/http-response-caching).

### Short-term general purpose caching

Using policies for general purpose caching, you can persist any objects your proxy requires across multiple request/response sessions.

With the [`PopulateCache` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy), [`LookupCache` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy), and [`InvalidateCache` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy), you can populate, retrieve, and flush cached data at runtime.

For example, you might temporarily store:

  * Session IDs for session management.
  * Credentials for outbound calls (such as API keys or OAuth access tokens).
  * Response content that must be paginated for apps.



At runtime, your cache policies copy values between proxy variables and the configured cache you specify. When a value is placed in the cache, it is copied from the variable you specify to the cache. When it is retrieved from the cache, it is copied into the variable for use by your proxy.

For an example with code, see [Example: General purpose caching](https://docs.cloud.google.com/apigee/docs/api-platform/cache/optimize-performance-using-cache).

### Managing cache with the Apigee API

You can list and delete caches using the [caches API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.caches).

## Long-term persistence with key value maps (KVMs)

To indefinitely store structured data either encrypted or unencrypted, you can create and populate key value maps (KVMs) that contain arbitrary key/value pairs. For example, you might store:

  * A map correlating IP addresses to country codes.
  * A list of IP addresses that are allowed/denied access.
  * A map correlating long URLs to shortened URLs.
  * Environment-specific data, such as quota counts and OAuth token expiration times.



KVMs can have one of three scopes: organization, environment, apiproxy. For example, if key/value pairs are to be used for all APIs in an organization, create a KVM at the organization scope; or if only a specific API proxy should have access to keys/values, create the KVM at the apiproxy scope. For more information, see [Working with key value maps](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps).

##  Property sets 

A _property set_ is a custom collection of key/value pairs that store data. API proxies can retrieve this data when they execute.

Typically, you use property sets to store non-expiring data that shouldn't be hard-coded in your API proxy logic, such as configuration data. You can access property set data anywhere in a proxy where you can access [flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables).

A common use case for property sets is to provide values that are associated with one environment or another. For example, you can create an environment-scoped property set with configuration values that are specific to proxies running in your test environment, and another set for your production environment.

For more information, see [Using property sets](https://docs.cloud.google.com/apigee/docs/api-platform/cache/property-sets). 

##  Kubernetes secrets 

(Apigee hybrid only) If you are already using Kubernetes for secret management in a custom vault for sensitive data, you might want to consider using [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/). Just like with KVM data, you can access the Kubernetes secret data in API proxy flow variables. For more information, see [Storing data in a Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/k8s-secrets). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
