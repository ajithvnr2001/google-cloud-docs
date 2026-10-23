---
url: https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview/
title: Policies and rules \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:34.205183+00:00
---

# Policies and rules  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Policies and rules Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure rules for your outbound web traffic with Secure Web Proxy. You can control which traffic is allowed or denied based on various criteria, ensuring only authorized traffic leaves your network. Secure Web Proxy provides three primary mechanisms for defining these controls: authorization policies, gateway security policies, and service rate limiting policies.

## Use the appropriate policy type

To control the flow of outbound web traffic, you must configure each Secure Web Proxy gateway with either an authorization policy or a gateway security policy. These two policy types are mutually exclusive; you can't attach both types of policies to the same gateway.

However, you can attach a service rate limiting policy to a gateway regardless of whether it uses an authorization policy or a gateway security policy.

Choose between the following two primary security policy types based on your requirements:

  * **Authorization policy** : use this policy type for features such as [custom authorization extensions by using Service Extensions](https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies#delegate) or [frontend mTLS](https://docs.cloud.google.com/secure-web-proxy/docs/use-frontend-mtls-with-swp). Authorization policies provide a flexible framework to secure your outbound traffic. You can use these policies to enable fine-grained controls, including identity-based and content-based policies, and support delegation to external authorization engines by using [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview).

If you want to adopt these features for an existing deployment, then you must migrate your rules for outbound traffic from your gateway security policy to an authorization policy.

**Caution:** Before migrating your rules, you must verify that authorization policies support all your required matching criteria. For example, authorization policies don't support [URL lists](https://docs.cloud.google.com/secure-web-proxy/docs/use-url-list).
  * **Gateway security policy** : use this policy type if you require either standard connection-level filtering based on source identity and destination attributes or URL lists in your policy. Gateway security policies are the foundation to define security rules in Secure Web Proxy. They allow or deny requests based on source identity—such as [service accounts](https://docs.cloud.google.com/secure-web-proxy/docs/use-service-accounts) or [secure tags](https://docs.cloud.google.com/secure-web-proxy/docs/use-tags)—and destination attributes, such as [URL lists](https://docs.cloud.google.com/secure-web-proxy/docs/use-url-list). Gateway security policies don't support using features such as custom authorization extensions or frontend mTLS.




In addition to choosing your primary security policy, you can optionally configure the following type of policy:

  * **Service rate limiting policy** : use this policy type to prioritize traffic, protect external destinations from traffic overloads, and control the costs of outbound web traffic by limiting request counts. You can attach a service rate limiting policy to a gateway regardless of whether it uses an authorization policy or a gateway security policy.



## Authorization policies

[Authorization policies](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview) let you establish identity-based access control checks when processing outbound requests through Secure Web Proxy. You can configure authorization policies ([`AuthzPolicy`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.authzPolicies)) to validate the identity of a source workload or agent that accesses the internet.

**Note:** If you already have a gateway security policy with existing security rules, then you don't need to remove them. Secure Web Proxy ignores these rules when you apply an authorization policy to the instance.

An authorization policy lets you specify conditions to allow, deny, or delegate request authorization based on their source, destination, and other request attributes. Requests that pass these checks are forwarded to the web destination. Requests that fail are rejected with a `403 Forbidden` error.

For Secure Web Proxy, you can attach authorization policies to your gateway resource to define the security perimeter for your outbound traffic and evaluate authorization policy rules in Secure Web Proxy. In addition, you can configure Secure Web Proxy to delegate authorization decisions to an external authorization engine by using Service Extensions ([authorization extensions](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-for-swp)).

For more information about how to configure authorization policies, see [Set up authorization policies for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies).

Authorization policies provide the following benefits over standard gateway security policies:

  * **Consistent policy surface** : use the unified [`AuthzPolicy`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.authzPolicies) API to manage traffic authorization for Secure Web Proxy along with other services such as Application Load Balancer and Cloud Service Mesh (CSM).

  * **Service Extensions support** : use Service Extensions to delegate authorization decisions to your custom logic. You can use authorization extensions to perform request-level authorization (based on headers, identity, and more) and content sanitization (such as sensitive data protection or threat detection).

  * **Identity-centric security** : while still supporting IP-based rules, authorization policies provide a more robust security posture by letting you enforce controls based on identity. You can define your security perimeter by using [service accounts](https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies#service-account), [tags](https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies#tag), or [frontend mutual TLS](https://docs.cloud.google.com/secure-web-proxy/docs/use-frontend-mtls-with-swp). You can also use Service Extensions to delegate authorization decisions to identity-based services like Identity-Aware Proxy.




## Gateway security policies and rules

A [gateway security policy](https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy#gateway-security-policies) is the core security item that defines access controls for all outbound web traffic.

Gateway security policies include the following key features:

  * **Policy control** : a policy contains the gateway security rules that the proxy uses to allow or deny a web request. You can create a single policy and reuse it across multiple Secure Web Proxy instances to keep your security rules consistent and efficient.

  * **Secure by default** : gateway security policies are `deny-all` by default. The proxy blocks every HTTP and HTTPS request until you create a specific rule to permit it. This enforces a zero-trust architecture from the start.

  * **Policy logic** : every policy is built on two core checks: determine the traffic source and verify the allowed destination.


**Note:** For information about the quotas and system limits that apply to Secure Web Proxy policies, see [Quotas and limits](https://docs.cloud.google.com/secure-web-proxy/docs/quotas).

A [gateway security rule](https://docs.cloud.google.com/secure-web-proxy/docs/configure-rules) is an instruction in a gateway security policy that matches and defines the final action: allow or deny.

Your Secure Web Proxy instance evaluates rules based on priority, with the lowest number checked first. The proxy stops and acts on the first rule that matches the request.

  * **Session Matcher** : checks basic information about the network connection as it's being set up. Session Matcher includes the following items:

    * Source identity (service account or secure tag)
    * Destination hostname (the domain name)
    * Destination port
  * **Application Matcher** : inspects the content of the actual web request. It's typically used to ensure granular control and requires TLS inspection to check encrypted traffic. Application Matcher includes the following items:

    * Full URL path
    * Request method—for example, block all `DELETE` actions
    * Specific HTTP headers

**Note:** To analyze request attributes such as HTTP methods or headers, [enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection). When TLS inspection is active, use authorization policies instead of standard gateway rules to get finer control over identity and content controls for decrypted traffic.

## Service rate limiting policies

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Service rate limiting policies help keep your outbound web traffic gateways resilient. Although other traffic management mechanisms prioritize scaling resources, rate limiting throttles resource-intensive clients at the source to maximize gateway availability.

Secure Web Proxy enforces service rate limiting at the end of the request processing path, after all gateway security rules, authorization checks, and service extensions complete successfully. This helps ensure that only authorized and trusted traffic consumes your rate limit budget.

**Note:** Service rate limiting applies only to Layer 7 traffic that matches a Secure Web Proxy rule with an application attribute (`ApplicationMatcher`). The outbound web traffic that matches a rule with only a session attribute (`SessionMatcher`) isn't subject to rate limiting.

For more information about how to set up rate limiting policies, see [Service rate limiting overview](https://docs.cloud.google.com/load-balancing/docs/srl-policy/service-rate-limiting-overview) and [Configure service rate limiting policies](https://docs.cloud.google.com/secure-web-proxy/docs/configure-service-rate-limiting-policies).

## Limitations

When you configure policies in Secure Web Proxy, the following limitations apply:

  * **Gateway security policies** : these policies don't support authorization extensions. Advanced capabilities like using custom logic or delegating authorization decisions to external services are available only through authorization policies.

  * **Authorization policies** : these policies don't support URL lists or regular expression (regex) matching for URL strings.

  * **Service rate limiting policies** : rate limiting applies only to Layer 7 traffic that matches a rule with an application attribute (`ApplicationMatcher`). For outbound web traffic that matches a rule with only a session attribute (`SessionMatcher`), rate limiting isn't applied.




## What's next

  * [Set up authorization policies for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies)
  * [Configure service rate limiting policies](https://docs.cloud.google.com/secure-web-proxy/docs/configure-service-rate-limiting-policies)
  * [Gateway security policies](https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy)
  * [Gateway security rules](https://docs.cloud.google.com/secure-web-proxy/docs/configure-rules)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
