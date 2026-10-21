---
url: https://docs.cloud.google.com/service-mesh/docs/service-routing/rate-limiting-overview/
title: Configure rate limiting with Google Cloud Armor \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:38.957978+00:00
---

# Configure rate limiting with Google Cloud Armor  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/service-routing/rate-limiting-overview/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure rate limiting with Google Cloud Armor

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can apply fairshare rate limiting to your Cloud Service Mesh clients, helping you manage fair consumption of your services and prevent malicious or misbehaving clients from overloading your services.

The configuration process requires you to create a Cloud Armor security policy and an endpoint policy. If you aren't familiar with Cloud Armor security policies, we recommend that you read the [Security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview).

## How rate limiting works

Rate limiting restricts the number of requests that your service can receive from clients within a specified time interval in order to improve the availability of your service and fairly share available capacity among clients. The request threshold, interval, and action that Cloud Armor applies to incoming traffic that exceeds the rate limit threshold is user configurable. For Cloud Service Mesh rate limiting, Cloud Armor uses the security policy type `CLOUD_ARMOR_INTERNAL_SERVICE` and security policy rules use the `fairshare` action.

Each Cloud Armor security policy contains one or more rules. Each rule consists of a match condition and an action. When a request meets the match condition, Cloud Armor applies the configured action to the request. When you configure rate limiting, you create a security policy rule with one of the rate limiting actions mentioned previously, and whatever match condition fits your use case (including matching on all incoming requests with the flag `--src-ip-ranges "*"`). Rules within a policy are evaluated in priority order. The rule with the lowest numerical priority has the highest logical priority and is evaluated first. Cloud Armor performs server-side rate limiting, which means that the server enforces the rate limit rather than the client device.

Rate limiting actions have additional fields that you use to fine-tune the rate limit threshold. The following fields are shared among all rate limiting rules:

  * `rate_limit_threshold_count`: the number of requests per user-configured time interval over which Cloud Armor must apply rate limiting.
  * `interval_sec`: the time interval, in seconds, for `rate_limit_threshold_count`.
  * `exceed_action`: the action to perform on requests that exceed the rate limit threshold.
  * `conform_action`: the action to perform on requests that don't exceed the rate limit threshold.



## Rate limiting with Cloud Service Mesh

This section provides a general description of the steps that you need to take to configure rate limiting with Cloud Service Mesh.

First, you create an endpoint policy and make sure that the `EndpointMatcher` selects your Cloud Service Mesh instances to enforce rate limits on inbound traffic. The `EndpointMatcher` uses endpoint labels to identify the instances to which it attaches.

Next, you create a Cloud Armor security policy with the type `CLOUD_ARMOR_INTERNAL_SERVICE`. The only action available for this security policy type is `fairshare`. In this policy, you create a default rule with the `fairshare` action to apply fairshare rate limiting to all traffic that doesn't meet a higher-priority rule. You can add new, higher-priority rules to apply a different rate limit to different kinds of traffic. For example, you can give a specific IP address range a lower or higher rate limit.

Finally, after you finish creating your security policy with one or more rate limiting rules you attach it to the endpoint policy. After you attach the security policy, Cloud Armor applies server-side rate limiting to all incoming traffic that matches with a match condition of a rule and that connects to the service mesh instances that the `EndpointMatcher` selected.

Cloud Service Mesh configures a global rate limit across all instances. This means that the total traffic volume across all server instances is aggregated to determine when to enforce the rate limit. Any client that sends requests to such a service is subject to the same enforcement threshold and policy. This means that when the _aggregate_ traffic rate exceeds the threshold, some requests are dropped.

To configure rate limiting with Cloud Service Mesh, see [Configure Google Cloud Armor rate limiting with Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/rate-limiting-envoy).

## Limitations

When you configure rate limiting with Cloud Armor, consider the following limitations:

  * Cloud Armor [quotas](https://docs.cloud.google.com/armor/quotas) limit the number of custom rules that you can create. We recommend that you check your quota before creating more than 20 custom rules.
  * Each endpoint policy resource must reference a different security policy. You can't attach a security policy to a new endpoint policy if it's already referenced by an existing endpoint policy.
  * Security policies with the `fairshare` action are limited to the `ALL` rate limiting key.
  * When you deploy security policies with the `fairshare` action, Cloud Armor ignores the `preview` field during rule enforcement.
  * You can't configure a Cloud Armor security policy if you're using TCP traffic routing.



In addition, Cloud Armor security policies with the `CLOUD_ARMOR_INTERNAL_SERVICE` type are limited to the following custom expression language (CEL) attributes:

  * `request.headers`
  * `request.method`
  * `request.path`
  * `request.scheme`
  * `request.query`



For more information about CEL attributes, see [Configure custom rules language attributes](https://docs.cloud.google.com/armor/docs/rules-language-reference#attributes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
