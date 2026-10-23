---
url: https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview/
title: Authorization policy overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:25.647663+00:00
---

# Authorization policy overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Authorization policy overview Stay organized with collections  Save and categorize content based on your preferences. 

Authorization policies let you establish both access control checks and content sanitization checks when processing requests or responses through different Google Cloud services such as Application Load Balancers, Agent Gateway, and Secure Web Proxy.

For Agent Gateway and Secure Web Proxy, the authorization policy is attached directly to the gateway resource of these services. For a load balancer, the authorization policy is attached to the load balancer's forwarding rule resource.

**Note:** Although parts of this document focus on authorization policies in relation to Cloud Load Balancing, the authorization policy concepts discussed here apply to all the aforementioned Google Cloud services.

An authorization policy ([`AuthzPolicy`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.authzPolicies)), attached to the forwarding rule of a load balancer, lets you specify conditions that permit, restrict, or delegate the authorization of requests based on their source and intended operations. Requests that pass these checks are routed to the backend service of the load balancer, whereas requests that fail these checks are rejected with an unauthorized response.

You can configure authorization policies on the forwarding rule of all Application Load Balancers with a [load balancing scheme of `EXTERNAL_MANAGED` or `INTERNAL_MANAGED`](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#summary-gclb). The following Application Load Balancers support authorization policies:

  * Global external Application Load Balancers


  * Regional external Application Load Balancers
  * Regional internal Application Load Balancers


  * Cross-region internal Application Load Balancers



## Authorization policy rules

An authorization policy consists of a list of HTTP rules to match against the incoming request.

For an authorization policy with an `ALLOW` or `DENY` action, an HTTP rule (`AuthzRule`) defines the conditions that determine whether traffic is allowed to pass through the load balancer. At least one HTTP rule is required.

For an authorization policy with a `CUSTOM` action, an HTTP rule (`AuthzRule`) defines the conditions that determine whether traffic is delegated to the custom provider for authorization. A custom provider is required while HTTP rules are optional.

A policy match occurs when at least one HTTP rule matches the request or when no HTTP rules are defined in the policy.

An authorization policy HTTP rule consists of the following fields:

  * `from`: specifies the identity of the client that is allowed by the rule. The identity can be derived from a client certificate in a mutual TLS connection, or it can be the ambient identity associated with the client virtual machine (VM) instance, such as from a service account or a secure tag.
  * `to`: specifies the operations allowed by the rule, such as the URLs that can be accessed or the HTTP methods allowed.
  * `when`: specifies additional constraints that must be met. You can use [Common Expression Language (CEL)](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference) expressions to define the constraints.



## Authorization policy actions

When evaluating a request, an authorization policy specifies the action (`AuthzAction`) to be applied on the request. An authorization policy needs to have at least one action, which can be one of the following:

  * `ALLOW`: allows the request to pass through to the backend if the request matches any of the rules specified within an `ALLOW` policy. If `ALLOW` policies exist, but there is no match, the request is denied. In other words, the request is denied if none of the configured authorization policies with an `ALLOW` action match the request. In Cloud Logging, this action is logged as `denied_as_no_allow_policies_matched_request`.

For an `ALLOW` action to be applied, you need at least one HTTP rule.

  * `DENY`: denies the request if the request matches any of the rules specified within a `DENY` policy. If `DENY` policies exist, but there is no match, the request is allowed. In other words, the request is allowed if none of the configured authorization policies with a `DENY` action match the request. In Cloud Logging, this action is logged as `allowed_as_no_deny_policies_matched_request`.

For a `DENY` action to be applied, you need at least one HTTP rule.

  * `CUSTOM`: delegates the authorization decision to a custom authorization provider, such as IAP or service extensions. To learn more, see Delegate authorization decisions.

If there are HTTP rules configured for a `CUSTOM` policy, the request needs to match the HTTP rules to invoke the custom provider. However, if _no HTTP rules_ are defined, then the authorization policy always delegates the authorization decision to a custom authorization provider. To learn more, see the examples in [Authorization policy to delegate authorization decisions](https://docs.cloud.google.com/load-balancing/docs/auth-policy/set-up-auth-policy-app-lb#delegate).




## Authorization policy evaluation order

An authorization policy supports `CUSTOM`, `DENY`, and `ALLOW` policies for access control. When multiple authorization policies are associated with a single resource, the `CUSTOM` policy is evaluated first, then the `DENY` policy, and finally the `ALLOW` policy. The evaluation is determined by the following rules:

  1. If there is a `CUSTOM` policy that matches the request, the `CUSTOM` policy is evaluated using a custom authorization provider. If the custom provider rejects the request, it is denied. `DENY` or `ALLOW` policies aren't evaluated, even if any are configured.

  2. If there are any `DENY` policies that match the request, the request is denied. Any `ALLOW` policies aren't evaluated, even if they are configured.

  3. If no `ALLOW` policies exist, the request is allowed.

  4. If any of the `ALLOW` policies match the request, allow the request.

  5. If `ALLOW` policies exist, but there is no match, the request is denied. In other words, the request is denied by default if none of the configured `AuthzPolicies` with `ALLOW` action match the request.




For regional external Application Load Balancers, regional internal Application Load Balancers, Agent Gateway, and Secure Web Proxy—Google Cloud services that support policy profiles—the authorization policy evaluation order is as follows:

  1. If there is a custom request authorization (`REQUEST_AUTHZ`) policy that matches the request, the `REQUEST_AUTHZ` policy is evaluated using a custom authorization provider. If the custom provider rejects the request, it is denied. `DENY`, `ALLOW`, and `CONTENT_AUTHZ` policies aren't evaluated, even if any are configured.

  2. If there are any `DENY` policies that match the request, the request is denied. `ALLOW` and `CONTENT_AUTHZ` policies aren't evaluated, even if they are configured.

  3. If no `ALLOW` policies exist, the request proceeds to content authorization (`CONTENT_AUTHZ`) evaluation.

  4. If any of the `ALLOW` policies match the request, the request proceeds to `CONTENT_AUTHZ` evaluation.

  5. If `ALLOW` policies exist, but there is no match, the request is denied. `CONTENT_AUTHZ` policies aren't evaluated.

  6. If there is a `CONTENT_AUTHZ` policy that matches the request, it is evaluated last. If the custom provider rejects the request, it is denied.




## Policy profiles in authorization policies

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Policy profiles in authorization policies are supported for the following Google Cloud services:

  * Regional external Application Load Balancers
  * Regional internal Application Load Balancers
  * Agent Gateway
  * Secure Web Proxy



A policy profile ([`PolicyProfile`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1beta1/projects.locations.authzPolicies#policyprofile)) in an authorization policy is of the following types:

  * Request authorization profile (`REQUEST_AUTHZ`): relies on information in HTTP request headers to allow or deny traffic.
  * Content authorization profile (`CONTENT_AUTHZ`): provides content-based security and filtering to block prompt injection attacks, prevent sensitive data leaks, and filter harmful content.



You can configure an authorization policy with either a `REQUEST_AUTHZ` profile or a `CONTENT_AUTHZ` profile, but not both. If a policy profile is not specified, the authorization policy uses the `REQUEST_AUTHZ` profile by default.

### Request authorization profile

Authorization policies using the `REQUEST_AUTHZ` policy profile can evaluate access decisions for incoming traffic either directly or delegate them. You can delegate access decisions to Identity-Aware Proxy or to a custom authorization engine using an authorization extension. The `REQUEST_AUTHZ` policy profile acts on information in the HTTP request headers to allow or deny a request.

An authorization policy with the `REQUEST_AUTHZ` policy profile can have an `ALLOW`, `DENY`, or `CUSTOM` action applied to the request. An action of `ALLOW` or `DENY` means that the access decision is evaluated directly, whereas a `CUSTOM` action means that the access decision is delegated.

When the access decision is delegated, an authorization policy, configured on the forwarding rule of the load balancer, points to a request authorization extension that runs on a callout backend service. For each authorization request, the load balancer forwards the request headers to the authorization extension using Envoy's `ext_proc` or `ext_authz` protocol. Depending on the response from the extension, the load balancer proxy either forwards the request to its backend service or rejects the request.

If a policy profile is not specified, the authorization policy uses the request authorization profile (`REQUEST_AUTHZ`) by default.

### Content authorization profile

Authorization policies using the `CONTENT_AUTHZ` policy profile can be used to perform deep inspection of your application payloads to allow or deny requests or mutate the requests or responses, as necessary. You can delegate access decisions to either Model Armor or your own content sanitization extension.

An authorization policy with the `CONTENT_AUTHZ` policy profile can only have a `CUSTOM` action applied to the request. This means that the request cannot be evaluated directly and needs to be delegated.

An authorization policy, configured on the forwarding rule of the load balancer, points to a content authorization extension. For each authorization request, the load balancer forwards the full request and response content, which includes headers, body, and trailers, using Envoy's `ext_proc` protocol in full duplex streaming mode (`FULL_DUPLEX_STREAMED`), to the content authorization extension. Depending on the response from the extension, the load balancer proxy either forwards the request to its destination or rejects the request. The destination, in the case of a _request_ , is the backend service of the load balancer, and in the case of a _response_ , is the client.

## Delegate authorization decisions

Authorization policies can be evaluated directly or they can be delegated. For complex authorization decisions that can't be expressed using an authorization policy, you can create an authorization policy with a `CUSTOM` action and delegate the authorization decision to a Google-managed service or a user-managed service through Service Extensions.

  * Google-managed service 
    * Model Armor
    * Identity-Aware Proxy
  * User-managed service 
    * a Google Cloud backend service
    * a service accessible by a fully qualified domain name (FQDN) that supports Envoy's `ext_proc` or `ext_authz` protocol



The following table summarizes the different services that an authorization decision can be delegated to through Service Extensions.

Authorization policy | Evaluated directly | Delegated to Service Extensions (authorization extension)  
---|---|---  
Google-managed services | User-managed services  
Model Armor | Identity-Aware Proxy | Google Cloud backend service | FQDN-based service  
`REQUEST_AUTHZ` profile |  |  |  |  |   
`CONTENT_AUTHZ` profile |  |  |  |  |   
  
### Service Extensions

You can use authorization policies to delegate authorization decisions to [Service Extensions, specifically of the type authorization extension](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview). Authorization extensions support callouts to inject custom logic into Google Cloud Application Load Balancers. This capability lets you write your own code to perform various activities on traffic processed by a load balancer such as header rewrites, incremental security, custom logging, and custom user authentication.

With Service Extensions callouts, you instruct the load balancer to forward traffic from within the load-balancing data-processing path using gRPC calls, to a callout service, which can be user-managed or Google-managed. The different callout services are defined in the preceding table. These callout services run the authorization extension and can apply various policies or functions before returning the traffic to the load balancer for further processing. The following diagram shows this process.

[ ![An authorization policy can delegate authorization decisions to
    Service Extensions, specifically of the type
    authorization extension.](https://docs.cloud.google.com/static/load-balancing/images/service-extensions.svg)](https://docs.cloud.google.com/static/load-balancing/images/service-extensions.svg) Authorization policy delegating authorization decision through an authorization extension (click to enlarge).

To delegate authorization decisions to an authorization extension, create an authorization extension (`AuthzExtension`) that runs on a callout service. Then, you can create an authorization policy with a `CUSTOM` action and point it to the authorization extension that you created. The authorization extension can be used to perform both request-level authorization (`REQUEST_AUTHZ`) and content sanitization (`CONTENT_AUTHZ`).

To learn more about how to delegate authorization decision to a user-managed Google Cloud backend service or an FQDN-based service, see [Delegate authorization decision to a user-managed service](https://docs.cloud.google.com/load-balancing/docs/auth-policy/set-up-auth-policy-app-lb#delegate-authorization-user-managed-service).

#### Authorization extensions in the data processing path

When delegating an authorization decision to Service Extensions, specifically of the type [authorization extension](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview), note the following terminology:

  * When a custom authorization policy with a `REQUEST_AUTHZ` policy profile points to an authorization extension (`AuthzExtension`), the authorization extension is referred to as a _request authorization extension_.

  * When an authorization policy with a `CONTENT_AUTHZ` policy profile points to an authorization extension (`AuthzExtension`), the authorization extension is referred to as a _content authorization extension_. 




In the request processing path, a request authorization extension is invoked first, followed by deny and allow policy evaluation, then the content authorization extension, and finally the traffic extension. A content authorization extension can also be invoked in the response processing path. The following diagram shows the sequence in which different extensions are invoked.

**Note:** The request authorization extension is invoked only when the request headers arrive. Request body along with response headers and response body is not visible to the request authorization extension.[ ![A request authorization extension is invoked before a
        content authorization extension](https://docs.cloud.google.com/static/load-balancing/images/request-authz-content-authz.svg)](https://docs.cloud.google.com/static/load-balancing/images/request-authz-content-authz.svg) Request authorization extension invoked before a content authorization extension (click to enlarge).

You can think of different extensions as hooks that get triggered along certain points of the data processing path. To learn more about the different extensions, see [Extensibility points in the load balancing data path](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#extensibility_points_in_the_load_balancing_data_path) in the _Service Extensions_ documentation.

### Model Armor

You can use authorization policies to enable [Model Armor](https://docs.cloud.google.com/model-armor/overview) to apply AI guardrails that prevent generation of harmful content, prevent prompt injection, and prevent data leakage.

To do this, you can create an authorization extension (`AuthzExtension`) that runs on a Model Armor service. Then, you can create an authorization policy with a `CUSTOM` action and a `CONTENT_AUTHZ` profile that points to the authorization extension that you created.

To learn more about how to delegate authorization to Model Armor, see [Delegate authorization decision to Model Armor](https://docs.cloud.google.com/load-balancing/docs/auth-policy/set-up-auth-policy-app-lb#delegate-model-armor).

### Identity-Aware Proxy

You can delegate authorization decisions to Identity-Aware Proxy. IAP verifies user identity and context of the request to determine if a user should be allowed to access an application or a resource.

For global external Application Load Balancers and cross-region internal Application Load Balancers, you cannot delegate the authorization decision to IAP through an authorization extension.

For regional external Application Load Balancers and regional internal Application Load Balancers, you can configure an authorization policy to delegate the authorization decision to IAP through an authorization extension.

To learn more about using IAP as an authorization service, see [Delegate authorization decision to Identity-Aware Proxy](https://docs.cloud.google.com/load-balancing/docs/auth-policy/set-up-auth-policy-app-lb#delegate-iap).

## Authorization policy based on principals

To identify the source of traffic with high granularity, you can configure authorization policies based on identities derived from a client's certificate. This method requires [frontend mTLS](https://docs.cloud.google.com/load-balancing/docs/mtls) to be enabled on the load balancer and uses the following certificate attributes as a [principal selector](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.authzPolicies#principalselector) for identification:

  * Client certificate URI SANs (`CLIENT_CERT_URI_SAN`)
  * Client certificate DNS Name SANs (`CLIENT_CERT_DNS_NAME_SAN`)
  * Client certificate Common Name (`CLIENT_CERT_COMMON_NAME`)



If no principal selector is specified for identification, `CLIENT_CERT_URI_SAN` is used as the default principal selector. This means that the client certificate's URI SANs are evaluated when making authorization decisions.

For principal-based authorization to work, the following conditions must apply:

  * **Frontend mTLS must be enabled**. If frontend mTLS isn't enabled, the client doesn't present a certificate. As a result, any principal-based rules in the authorization policy find no certificate information to evaluate. For example, a rule checking `CLIENT_CERT_URI_SAN` sees an empty value.

  * **There must be a valid client certificate**. Even with mTLS enabled, a client certificate isn't used for authorization if the connection was established with a missing or an invalid certificate. This scenario occurs when the mTLS client validation mode is set to the permissive mode [`ALLOW_INVALID_OR_MISSING_CLIENT_CERT`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies#clientvalidationmode). In this case as well, any principal-based rules in the authorization policy find no certificate information to evaluate. For example, a rule checking `CLIENT_CERT_URI_SAN` sees an empty value.




**Impact of attribute size limits**

Authorization decisions are sensitive to the size of client certificate attributes. A request is _rejected_ if an attribute exceeds its size limit and the policy is configured to validate that specific attribute.

A rejection can occur under the following conditions:

  * The policy validates against `CLIENT_CERT_URI_SAN`, and the certificate's URI SANs exceed the size limit.
  * The policy validates against `CLIENT_CERT_DNS_NAME_SAN`, and the certificate's DNS Name SANs exceed the size limit.
  * The policy validates against `CLIENT_CERT_COMMON_NAME`, and the certificate's Subject (which contains the Common Name) exceeds the size limit.



If a certificate's attribute exceeds its size limit but is _not_ explicitly validated by the policy's principal selector, the request is still evaluated against the configured principal rules. For example, if a policy is configured to validate only the `CLIENT_CERT_DNS_NAME_SAN`, a request from a client with oversized URI SANs is not rejected for that reason. The policy proceeds to evaluate the request based on its DNS Name SANs.

To see an example of an authorization policy based on principals, see [Authorization policy to deny requests](https://docs.cloud.google.com/load-balancing/docs/auth-policy/set-up-auth-policy-app-lb#authorization_policy_to_deny_requests).

## Authorization policy based on service accounts or secure tags

An authorization policy based on [service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview) or [secure tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) is supported for the following load balancers:

  * Regional internal Application Load Balancers
  * Cross-region internal Application Load Balancers

**Note:** Applying authorization policies based on service accounts or tags isn't supported for external Application Load Balancers.

Authorization policies, based on service accounts and secure tags, let you enforce security rules based on who or what is sending the traffic, rather than just the IP address. This results in a shift from IP-based rules to identity-based controls by using service accounts and secure tags to define your security perimeter. For example, you can create an authorization policy to do the following:

  * deny a Compute Engine VM with a specific service account (`my-sa-123@PROJECT_ID.iam.gserviceaccount.com`) to reach the `/api/payments` path.

  * allow Compute Engine VMs with a secure tag (`environment: prod` key-value pair) to reach the `/api/payments` path.




You can apply authorization policies based on service accounts or secure tags attached to various Google Cloud services. Any traffic originating from these Google Cloud services, which are linked to a specific service account or a secure tag, can be either allowed, denied, or delegated for further evaluation.

The following table lists the various Google Cloud services that support the use of service accounts and secure tags.

Google Cloud service | Service account support | Secure tag support  
---|---|---  
[Compute Engine virtual machine (VM)](https://docs.cloud.google.com/compute/docs/overview) |  |   
[Google Kubernetes Engine (GKE) node](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) |  |   
[Google Kubernetes Engine (GKE) container](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) | 1 | 1  
[Direct VPC for Cloud Run](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) |  | 1  
[Serverless VPC Access connector](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors) | 2 | 2  
[Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) | 1 | 1  
[Cloud Interconnect on premises](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) | 1 | 1  
[Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer) | 3 | 3  
[Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/proxy-network-load-balancer) | 3 | 3  
  
1 Not supported by Google Cloud.

2 Source IP address is unique and can be used instead.

3 Service accounts and tags aren't supported when Application Load Balancers and Network Load Balancers serve as sources of traffic in a tiered architecture.

The following table lists the different Virtual Private Cloud (VPC) architectures that support the use of service accounts and tags.

VPC | VPC architecture | Support  
---|---|---  
Within VPC | Cross project (Shared VPC) |   
Within VPC | Cross region |   
Cross VPC | Cross peering link (peer VPC) |   
Cross VPC | Cross Private Service Connect |   
Cross VPC | Cross Network Connectivity Center spokes |   
  
To learn more about setting up an authorization policy that is based on service accounts and tags attached to a Google Cloud resource, see [Authorization policy based on service accounts or tags](https://docs.cloud.google.com/load-balancing/docs/auth-policy/set-up-auth-policy-app-lb#authz-policy-tags-or-sa).

## Quotas

For information about quotas for authorization policies, see [quotas and limits for authorization policies](https://docs.cloud.google.com/load-balancing/docs/quotas#authorization_policy).

## Pricing

For pricing information, see [Network pricing: Cloud Load Balancing](https://cloud.google.com/vpc/network-pricing#cloud-load-balancing).

## What's next

  * [Set up authorization policies for Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/auth-policy/set-up-auth-policy-app-lb)


  * [Configure an authorization extension](https://docs.cloud.google.com/service-extensions/docs/configure-authorization-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
