---
url: https://docs.cloud.google.com/load-balancing/docs/tutorials/faster-performance-improved-protection/
title: Faster web performance and improved web protection for load balancing \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:43.344191+00:00
---

# Faster web performance and improved web protection for load balancing  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/tutorials/faster-performance-improved-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Faster web performance and improved web protection for load balancing Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial outlines the value of adding Cloud CDN and Google Cloud Armor to an existing external Application Load Balancer deployment. It includes basic instructions for enabling both Cloud CDN and Cloud Armor with an external Application Load Balancer.

**Note:** If you are using Cloud Armor with Cloud CDN, security policies are enforced only for requests for dynamic content, cache misses, or other requests that are destined for your origin server. Security policies do _not_ apply to cache hits, even if the connecting client would otherwise match a rule in the policy.

## Improving web performance with Cloud CDN

Using the external Application Load Balancer already improves web performance by setting up HTTP(S) connections on Google's global edge closer to the requesting client and by negotiating connections using modern protocols such as QUIC, HTTP/2, and [TLS 1.3](https://cloud.google.com/blog/products/networking/tls-1-3-is-now-on-by-default-for-google-cloud-services) to reduce the number of round trips and enhance throughput. Further, by using persistent connections to your origin, Google Cloud reduces the overhead of each client connection. Google's edge locations are connected to our global private backbone network, which allows Google Cloud to optimize routing and reduce latency between the client, Google's edge, and your backends. You can further improve performance and reduce your serving costs by enabling Cloud CDN as part of your external Application Load Balancer deployment.

### What is Cloud CDN?

Cloud CDN (Content Delivery Network) uses Google's globally distributed edge points of presence to cache copies of load balanced content close to your users.

### How Cloud CDN can improve web performance

There are multiple ways that Cloud CDN improves performance.

#### Offloads and scales your backend infrastructure by reducing requests

A request served from the Cloud CDN cache means that the load balancer doesn't need to send the request to backend infrastructure for a static element such as an image, video, JavaScript, or stylesheet. This not only reduces load during normal operation but allows Google edge infrastructure to absorb spikes in requests without increasing the load on your backend serving infrastructure. This ensures backend infrastructure is focused on generating user-specific responses such as dynamic HTML for interactive web experiences.

#### Serves static assets from the edge

Because Google's global edge sends cached requests, the response times to client requests can be reduced. Static elements of your web experience such as images, videos, JavaScript, and stylesheets can be delivered right away without needing to forward the request to the backend systems and wait for a response and data transfer.

#### Reduces your data transfer and backend infrastructure costs

By using Cloud CDN with your external Application Load Balancer, you reduce your backend infrastructure costs due to reduced traffic to the backend. Additionally, you can reduce the number of cycles to deliver static content because it is sent from the Google edge. Cloud CDN traffic is billed at a [lower data transfer cost](https://cloud.google.com/cdn/pricing), further controlling costs.

### Enabling Cloud CDN for your external Application Load Balancer

You can enable Cloud CDN for an existing external Application Load Balancer or when setting up a new load balancer.

#### Enabling Cloud CDN during external Application Load Balancer setup

During backend configuration, select the **Enable Cloud CDN** checkbox. For details, see the [Cloud CDN how-to guides](https://docs.cloud.google.com/cdn/docs/how-to).

#### Enabling Cloud CDN for an existing external Application Load Balancer

In an existing external Application Load Balancer configuration, in the **Load Balancer** details screen, you can click **Edit** edit to modify your load balancer.

Then, in the **Backend Configuration** section, you can select the **Enable Cloud CDN** checkbox. For detailed instructions, including `gcloud` commands, see the [Cloud CDN how-to guides](https://docs.cloud.google.com/cdn/docs/how-to).

## Improving web protection with Cloud Armor

Using the external Application Load Balancer already provides a measure of web protection by setting up HTTP(S) connections on Google's global edge, offloading your backend infrastructure from needing to handle this process. By enabling Cloud Armor as part of your external Application Load Balancer you have increased visibility and control against infrastructure and application attacks.

**Note:** You can use Cloud Armor with Cloud CDN to protect the CDN origin servers. Cloud Armor ensures that the CDN origin server is protected from application attacks, mitigates OWASP Top 10 risks, and enforces Layer 7 filtering policies. Cloud Armor enforces security policies for backend services with Cloud CDN enabled _only_ for cache misses; that is, for requests that miss or bypass the Cloud CDN cache.

### What is Cloud Armor?

Cloud Armor provides DDoS and application layer defense working in conjunction with external Application Load Balancers. It provides visibility into attacks and allows you to deploy pre-configured and custom rules to mitigate attacks against your web applications and services. Like the external Application Load Balancer, Cloud Armor is delivered at the edge of Google's network, helping to defend against infrastructure and application attacks close to their source.

### How Cloud Armor can improve web protection

There are multiple ways that Cloud Armor improves protection.

#### Always-on automatic DDoS protection

Cloud Armor works with the external Application Load Balancer to provide always-on automatic protection from Layer 3 and Layer 4 volumetric and network protocol-based DDoS attacks. Cloud Armor is based on technologies originally developed to defend Google's own web services such as Google Search, Gmail, and Google Maps. For more information, see [Cloud Armor always-on DDoS protection](https://docs.cloud.google.com/armor/docs/cloud-armor-overview#always-on-ddos-protection).

#### Has pre-configured WAF rules to help detect and mitigate common application attacks

Cloud Armor provides a library of pre-configured web application firewall (WAF) rules that help detect and optionally help mitigate common web attacks such as SQL injection, cross-site scripting, and command injection attacks against your web infrastructure.

#### Detects and blocks by geographical source and IP addresses or IP ranges

Cloud Armor leverages Google's Geo-IP database to identify the geographical region of incoming requests destined for your web infrastructure and allows you to block traffic based on two-character country codes. For example, an online commerce site that does not ship outside of a given country can block requests from common sources of attack traffic. Additionally, Cloud Armor allows quick blocking of specific IP addresses or ranges of IP addresses making malicious requests.

#### Provides visibility to monitor and mitigate application layer HTTP(S) attacks

Cloud Armor also provides a custom-rules language that lets you match complex patterns from incoming requests using a wide variety of HTTP(S) semantics. This includes headers, cookies, URLs, query string elements, user agent patterns, and HTTP methods.

### Enabling Cloud Armor for your external Application Load Balancer

Security policies drive Cloud Armor configuration. These policies enable built-in rules and support custom rules for protection. To deploy Cloud Armor, you must create a security policy, add rules, and then attach this policy to one or more external Application Load Balancer backend services. Each rule specifies the parameters to detect in traffic, the action to take if the traffic matches these parameters, and a priority value that determines the position of the rule in the policy hierarchy.

#### Creating a Cloud Armor security policy

At a high level, these are the steps for configuring Cloud Armor security policies to enable rules that allow or deny traffic to external Application Load Balancer.

  1. Create a Cloud Armor security policy in the Network Security - Cloud Armor screen.
  2. Add rules to the policy based on IP lists, custom expressions, or pre-configured WAF rules such as SQL injection or Cross-site scripting.
  3. Attach the Cloud Armor security policy to a backend service of the external Application Load Balancer for which you want to control access.
  4. Update the Cloud Armor security policy as needed.



For the detailed instructions, see the [Cloud Armor how-to guides](https://docs.cloud.google.com/armor/docs/how-to).

## Next steps

  * Learn more about Cloud CDN [capabilities](https://docs.cloud.google.com/cdn/docs/features).
  * Understand Cloud Armor's [security policies in depth](https://docs.cloud.google.com/armor/docs/configure-security-policies).
  * Set up [Monitoring and logging](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring) for an external Application Load Balancer with Cloud CDN.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
