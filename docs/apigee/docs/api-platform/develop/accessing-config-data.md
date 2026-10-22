---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/accessing-config-data/
title: Accessing configuration data \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:16.159983+00:00
---

# Accessing configuration data  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/accessing-config-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Accessing configuration data Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

API proxy developers commonly use one or more Apigee data persistence mechanisms to store configuration data so they can later access it in an API proxy. This topic discusses how to choose the right persistence mechanism depending on your use case. 

##  Persistence mechanisms 

The following table briefly describes the persistence mechanisms available in Apigee: Mechanism | Use  
---|---  
Key value maps | Key value maps (KVMs) provide a general runtime store for data that may change periodically. For example: user session data, shopping cart, etc. KVM entries can be encrypted. See also [Using key value maps](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps).  
Property sets | Property sets are good for storing configuration data that doesn't change often. See also [Using property sets](https://docs.cloud.google.com/apigee/docs/api-platform/cache/property-sets).  
Kubernetes secrets | (Apigee hybrid only) Use Secrets to store sensitive data such as user credentials. See also [Storing data in a Kubernetes Secret](https://docs.cloud.google.com/apigee/docs/hybrid/latest/k8s-secrets).  
  
##  Scope of persistence mechanisms 

Each of the available persistence mechanisms has a specific scope that determines where you can access its stored data. The following table summarizes the available scopes for each persistence mechanism. For more about scopes, see [About persistence scope](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps#scope) and [Property set scopes](https://docs.cloud.google.com/apigee/docs/api-platform/cache/property-sets#scopes). 

| Organization | Environment | API Proxy  
---|---|---|---  
Key Value Maps | Yes | Yes | Yes  
Property sets | No | Yes | Yes  
Kubernetes Secrets | No | Yes | No  
  
##  Deciding which persistence mechanism to use 

This section describes use cases for each persistence mechanism to help you decide which one is best suited for storing configuration data. 

###  When to use Key Value Maps 

You can manage KVMs and their entries using the Apigee UI (for environment-scoped KVMs), the Apigee APIs, or the [ KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy). The policy lets you perform KVM operations at runtime, when the proxy is executing. 

Consider using KVMs when:

  * You have thousands, hundreds of thousands, or millions of key value map entries (any number up to the [documented KVM size limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits)).
  * You have entries that are not known at design time.



For example, use KVM to store user session data when a user logs in and delete it when the user logs out. 

###  When to use property sets 

Consider using property sets when: 

  * The keys and values are known at design time. Property set values cannot be changed by the API proxy when it is running. They are available in the proxy flow as read-only variables.
  * You have a few to few hundred keys (<110 KB in total). Property set keys and values are always stored in memory for quick access. 
  * You want the convenience of allowing administrators to change property sets in an environment without redeploying API proxies.



For example, property sets are good for storing route rules. Route rules are key/value pairs where values are target endpoint URLs. These values typically vary between environments and can be shared by multiple API proxies deployed in an environment. Property sets can also be a good choice for storing public keys and certificates. 

###  When to use Kubernetes Secrets 

This option is only available with Apigee hybrid. It allows an API proxy to access data stored in Kubernetes Secrets. This option is similar to property sets, where stored data is available as message flow variables within the executing proxy. However, the data always remains within the runtime plane; it is never set to the management plane in the Apigee cloud. 

Consider using Kubernetes Secrets when: 

  * You need to store sensitive information that you never want to be stored in the management plane. For example, you might use a Kubernetes Secret to store private keys or credentials required to access external systems. 
  * You need to share stored data with multiple API proxies deployed in the same environment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
