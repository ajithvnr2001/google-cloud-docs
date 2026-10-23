---
url: https://docs.cloud.google.com/secure-web-proxy/docs/overview/
title: Secure Web Proxy overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:34.418449+00:00
---

# Secure Web Proxy overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Secure Web Proxy overview Stay organized with collections  Save and categorize content based on your preferences. 

Secure Web Proxy helps you secure all outbound web traffic—HTTP and HTTPS—from your organization's internal network. When you configure your clients to explicitly use Secure Web Proxy as a gateway, Secure Web Proxy is a mandatory security checkpoint for any application or service that tries to access a website outside your organization.

## Benefits

Secure Web Proxy provides the following key benefits:

  * **Zero maintenance**. After you set your policies, Secure Web Proxy manages your servers, patching, and scaling to automatically adjust capacity as your traffic grows.

  * **Flexible and reusable rules**. With Secure Web Proxy, security policies are separate from the proxy itself. To help ensure consistent management, administrators create a set of access rules and apply the rules to multiple proxies across different parts of your organization.

  * **Strong default security**. Secure Web Proxy has a default `deny-all` setting that blocks all outbound traffic until you explicitly allow it. Google Cloud automatically handles all software and infrastructure updates, which minimizes the ongoing risk of security vulnerabilities.

  * **Identity-aware access control**. Because Secure Web Proxy checks from _where_ a request is coming (the IP address) and _who_ is making the request (the user or service identity), access is based on the user role and need, not just network location. The identity can be a [service account](https://docs.cloud.google.com/secure-web-proxy/docs/use-service-accounts), a [secure tag](https://docs.cloud.google.com/secure-web-proxy/docs/use-tags), or any identity provided by a client certificate that's verified by using [frontend mTLS](https://docs.cloud.google.com/secure-web-proxy/docs/use-frontend-mtls-with-swp). Secure Web Proxy lets you create highly specific rules, such as "Only members of the Finance team can access this banking website."

  * **Unified traffic logging and auditing**. All web traffic that passes through Secure Web Proxy is centrally logged and audited within Google Cloud. This single, clear source of truth for all outbound access helps you track activity, investigate security incidents, and meet compliance requirements.

  * **Centralized inspection**. Secure Web Proxy consolidates outbound web requests from your cloud workloads and connected offices into a single inspection point for consistent policy enforcement.

  * **Simplified port management**. You can optionally listen on all ports (from `1` to `65535`) when deploying your Secure Web Proxy instance as next hop. This functionality removes the need to enumerate specific ports and is useful for dynamic environments or services that use several ports. For information about the limitations related to using the `all_ports` feature, see [Limitations](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop#limitations).

  * **Distributed tracing**. Built-in integration with [Cloud Trace](https://docs.cloud.google.com/secure-web-proxy/docs/distributed-tracing-overview) and OpenTelemetry lets you trace the entire lifecycle of outbound requests from internal workloads through Secure Web Proxy. By using this feature, you can pinpoint latency bottlenecks and analyze request lifecycles.




## Supported features

Secure Web Proxy supports the following features:

  * **Autoscaling Secure Web Proxy Envoy proxies** : Secure Web Proxy supports automatically adjusting the Envoy proxy pool size and the pool's capacity in a region, which enables consistent performance during high-demand periods at the lowest cost. The autoscaling feature automatically manages capacity adjustments in a region. This means that you don't have to manually monitor and resize your proxy fleet, ensuring better performance with less operational time.

  * **Modular outbound access policies** : Secure Web Proxy manages outbound traffic through the following actions:

    * Identifies source entities by using secure tags, service accounts, IP addresses, or client certificate identities that were cryptographically verified with frontend mutual TLS (mTLS).
    * Filters destination targets by hostnames or URLs when you enable TLS inspection or use unencrypted HTTP.
    * Evaluates request attributes such as methods, headers, or URLs if the traffic is unencrypted HTTP or if TLS inspection is enabled.

This modular nature of policies (sources, destinations, and requests) lets various teams create and manage specific, reusable rule components. A central administrator can define a URL list that multiple proxies can then reference in their distinct policies.

  * **Service rate limiting** : Secure Web Proxy enforces traffic limits on outbound web traffic to prevent resource-intensive clients from exhausting service capacity or generating excessive costs, such as those associated with large language model (LLM) tokens. You can attach service rate limiting policies to gateways that are configured with either gateway security policies or authorization policies. You can use [rate limiting policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#rate-limiting-policies) to prioritize or throttle traffic based on request counts and specific client identities, such as mTLS principals or source IP addresses.

  * **End-to-end encryption** : client-proxy tunnels can transit over TLS. Secure Web Proxy also supports HTTP and HTTPS `CONNECT` for client-initiated, end-to-end TLS connections to the destination server.

This crucial security measure is automatically managed by the service so that traffic is secured without requiring the manual configuration or monitoring of encryption standards.

  * **Cloud Audit Logs and Google Cloud Observability integration** : by using Google Cloud Observability, Cloud Audit Logs records both administrative actions (policy changes) and access requests and metrics (proxy transaction logs) for Secure Web Proxy. This unified, built-in view facilitates security monitoring and compliance reporting.

  * **Global access** : Secure Web Proxy provides the option to enable global access when creating a proxy instance. By using this feature, you can allow clients from any Google Cloud region to connect to the proxy rather than only the clients in a specific local region. This feature enhances infrastructure resilience and supports cross-region use cases, such as customized outbound traffic requirements. For more information, see [Configure global access for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/configure-global-access).




## How Secure Web Proxy works

Secure Web Proxy acts as a mandatory security checkpoint for all web traffic from your organization's network to the internet. Internal workloads must comply with Secure Web Proxy security rules before they can reach the internet.

  1. **Centralized gateway** : your workloads, such as virtual machines (VMs) and containers, are configured to send all outbound web requests to the central Secure Web Proxy instance.

  2. **Policy enforcement** : the proxy inspects the request and applies your security policies to determine whether to allow or deny the connection.

  3. **Secure outbound traffic** : if the request is allowed, then the traffic is securely routed out to the internet by using the Google Cloud infrastructure, typically Cloud NAT. The proxy also uses Cloud DNS to resolve external web addresses.




## Policies and rules

You can configure the following policies and rules in your Secure Web Proxy instance:

  * [Authorization policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies): these policies let you establish identity-based or destination-based access control checks when processing outbound requests through your Secure Web Proxy instance. You can configure authorization policies ([`AuthzPolicy`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.authzPolicies)) to validate the identity of a source workload or agent that accesses the internet.

  * [Gateway security policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#policies-overview): these policies define the overall security standard for a specific gateway. A gateway security policy is the main container for your security instructions.

  * [Gateway security rules](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#policies-overview): within every gateway security policy, you can add one or more gateway security rules. These rules are the individual instructions that allow or deny traffic based on various criteria.

  * [Service rate limiting policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#rate-limiting-policies): these policies let you enforce client-specific and service-wide rate limits on outbound web traffic. You can configure rate limits based on requests per minute, and then associate these limits with specific clients or groups of clients.




## Deployment modes

You can deploy your Secure Web Proxy instance in any one of the following modes:

  * [Explicit proxy routing mode](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart): in this mode, you must explicitly configure your workload environments and clients to point directly to the proxy server. Secure Web Proxy then isolates your clients from the internet. In this way, Secure Web Proxy acts as an intermediary, establishing new TCP connections for the client and ensuring that every connection meets the requirements of the administered security policy.

  * [Private Service Connect service attachment mode](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment): in this mode, you can centralize your web proxy deployments across a complex, multi-VPC architecture.

  * [Next hop mode](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop): in this mode, you can configure your Secure Web Proxy instance to act as a next hop for the routing in your network. In other words, you can configure your network routing to automatically send outbound traffic to your Secure Web Proxy instance. This deployment method reduces your organization's administrative overhead because you don't have to manually configure each source workload or client to use the proxy.




## Limitations

  * **IP versions** : Secure Web Proxy supports only IPv4; IPv6 isn't supported.

  * **HTTP versions** : Secure Web Proxy supports HTTP/0.9, 1.0, 1.1, and 2.0 versions. HTTP/3 isn't supported.

  * **Deployment scope** : You can deploy a Secure Web Proxy instance only in a host project, not in a service project.




## Additional Google Cloud tools to consider

You can integrate Secure Web Proxy with the following Google Cloud tools to enhance the overall security posture of your workloads and applications:

  * Use [frontend mutual TLS](https://docs.cloud.google.com/secure-web-proxy/docs/use-frontend-mtls-with-swp) (mTLS) to enable Secure Web Proxy to configure validated client identities in [authorization policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies) and enforce granular access control for outbound traffic.

  * Use [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/overview) to manage the trust anchors (root certificates) and intermediate CAs required to validate client certificates in frontend mTLS connections to Secure Web Proxy.

  * Implement [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to prevent data exfiltration from Google Cloud services, such as Cloud Storage and BigQuery.

  * Use [Trace](https://docs.cloud.google.com/secure-web-proxy/docs/distributed-tracing-overview) to get distributed tracing data for outbound requests and analyze end-to-end network latency.




## What's next

  * [Policies and rules](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview)
  * [Roles and permissions](https://docs.cloud.google.com/secure-web-proxy/docs/roles-permissions)
  * [Initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
