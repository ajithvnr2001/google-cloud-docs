---
url: https://docs.cloud.google.com/firewall/docs/urlf_best_practices/
title: Best practices for URL filtering service \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:41.226287+00:00
---

# Best practices for URL filtering service  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/urlf_best_practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Best practices for URL filtering service Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices for using URL filtering service with Cloud Next Generation Firewall (Cloud NGFW). Use these recommendations to create effective and maintainable firewall policies that help to prevent unintended filtering actions. This document assumes familiarity with [URL filtering service](https://docs.cloud.google.com/firewall/docs/about-url-filtering) concepts.

## Best practices

The following table lists the best practices for using the URL filtering service:

Topic or use-case | Cloud NGFW feature or rule component | Description  
---|---|---  
Protocol support | [Protocols and ports](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#protocols_and_ports) | Specify the protocol `TCP` and the ports `80` and `443` in a firewall policy rule that enforces URL filtering.  
  
For more information, see Specify destination protocol and ports.  
Firewall rule evaluation | [Firewall rule priority](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#priority) | Place rules that enforce URL filtering at the lowest priorities in a firewall policy.  
  
For more information, see Place URL filtering rules at lowest priorities.  
Traffic segmentation | [Network contexts](https://docs.cloud.google.com/firewall/docs/understand-network-contexts) | Use network contexts to create separate URL filtering firewall policy rules for east-west (non-internet-bound) traffic and internet-bound traffic.  
  
For more information, see Use network contexts to separate traffic.  
Policy exceptions | [Fully qualified domain name (FQDN) objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview) | To create a pinhole exception that allows a specific source to access a website, use a destination FQDN object and a URL filtering security profile in your firewall policy rule.  
  
For more information, see Use FQDNs to add pinhole exceptions.  
Selective inspection | To selectively inspect traffic based on the destination domains, use FQDN objects instead of URL filtering security profiles.  
  
For more information, see Use FQDNs for selective traffic inspection.  
Policy design | To address temporary requirements, avoid creating URL filtering firewall policy rules that use a single resource as a source.  
  
For more information, see Avoid creating rules based on a single resource.  
Protocol support | Use FQDN-based filtering for non-HTTP protocols.  
Policy hierarchy | [Global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies) and [Regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies) | Use URL filtering in global or regional network firewall policies and not in hierarchical firewall policies.  
  
For more information, see Avoid using URL filtering in hierarchical firewall policies.  
Scalability | [URL filtering security profiles](https://docs.cloud.google.com/firewall/docs/about-security-profiles#url-filtering-profile) | To stay within the supported limit for the number of domains in a URL filtering security profile, create separate security profiles that group domains based on a specific criteria.  
  
For more information, see Create separate security profiles for scale.  
  
## Specify destination protocol and ports

Cloud NGFW applies the default `allow` or `deny` action in a URL filtering [security profile](https://docs.cloud.google.com/firewall/docs/about-security-profiles) to non-HTTP and non-HTTPS traffic that matches a firewall policy rule enforcing URL filtering. Specify the protocol `TCP` and the ports `80` and `443` in such a firewall policy rule.

Specifying the protocol and ports in the rule prevents a match with non-HTTP and non-HTTPS traffic, and therefore, prevents the default action from unintentionally allowing or denying this traffic.

## Place URL filtering rules at lowest priorities

To ensure that firewall policy rules that don't use Layer 7 inspection are evaluated first, place rules that enforce URL filtering security profiles at the lowest priorities in a firewall policy. This approach prevents the default action in a URL filtering security profile from accidentally allowing or denying traffic.

For example, to allow any virtual machine (VM) instance to communicate with `www.example.com`, create a URL filtering security profile that allows this URL. And then, add a rule with a low priority, such as `500` that applies a [security profile group](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups) with this security profile.

Priority | Direction | Protocol | Target | Source | Destination | Destination port | Action  
---|---|---|---|---|---|---|---  
150 | Egress | TCP | All | 10.0.0.0/8 | 10.0.0.0/8 | 80, 443 | Allow  
200 | Ingress | TCP | All | Any | 10.0.0.0/8 | 80, 443 | Allow  
300 | Egress | TCP | All | Any | 199.36.153.8/30 | 80, 443 | Allow  
500 | Egress | TCP | All | Any | Any | 80, 443 | Apply a security profile group with URL filtering security profile that allows the URL `www.example.com`  
  
## Use network contexts to separate traffic

The default action of a security profile can allow or deny traffic that doesn't match the defined URL filters. To prevent unintended default actions, use [network contexts](https://docs.cloud.google.com/firewall/docs/understand-network-contexts) to create separate URL filtering firewall policy rules for east-west (non-internet-bound) traffic and internet-bound traffic. Network contexts make the rule match criteria more granular, and therefore, prevent the default action from accidentally allowing or denying traffic.

In the following example, the non-internet network context prevents the rule with the priority of `500` from matching and accidentally allowing or denying internet-bound traffic, which the rule with a priority of `600` manages separately.

Priority | Direction | Network context | Protocol | Target | Source | Destination | Destination port | Action  
---|---|---|---|---|---|---|---|---  
500 | Egress | Non-internet | TCP | All | Any | Any | 80, 443 | Apply a security profile group with URL filtering security profile 1  
600 | Egress | Internet | TCP | All | Any | Any | 80, 443 | Apply a security profile group with URL filtering security profile 2  
  
## Use FQDN objects

Use destination [FQDN](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview) objects along with URL filtering security profiles to avoid accidental traffic matches for the firewall policy rules, and therefore, prevent the security profile's default action from allowing or denying any unintended traffic.

### Use FQDNs to add pinhole exceptions

A pinhole exception in a firewall allows a specific type of traffic to pass through an otherwise closed security perimeter. To create such an exception that allows a specific source to access a website, use a destination FQDN object and a URL filtering security profile in your firewall policy rule.

A pinhole exception rule matches traffic from the source to the FQDN IP before applying URL filtering. Other traffic from the source doesn't match, preventing unrelated traffic from the security profile's default action.

In the following example, the rule matches traffic from the specified IP range to the IP address of `example.com`, then applies URL filtering to the matched traffic.

Priority | Direction | Network context | Protocol | Target | Source | Destination | Destination port | Action  
---|---|---|---|---|---|---|---|---  
100 | Egress | Internet | TCP | All | 192.168.1.0/24 | FQDN = `example.com` | 80, 443 | Apply a security profile group with URL filtering security profile that allows the URL `www.example.com`  
  
### Use FQDNs for selective traffic inspection

To selectively inspect traffic based on the destination domains, use FQDN objects instead of URL filtering security profiles.

URL filtering security profiles don't support selective traffic inspection. If you use URL filtering security profiles for traffic selection, the default action of the profile might unintentionally allow or deny traffic.

For example, to inspect traffic to `example.com` for threats without affecting traffic to `examplepetstore.com`, create separate firewall policy rules with priority `100` and `200`. For each rule, use a destination FQDN object and apply the threat prevention security profile only to the rule with the `example.com` destination. This approach prevents traffic to `examplepetstore.com` from matching the rule with the priority of `100`.

The following table shows the incorrect configuration:

Priority | Direction | Protocol | Target | Source | Destination | Destination port | Action  
---|---|---|---|---|---|---|---  
100 | Egress | TCP | All | Any | Any | 80, 443 | Apply a security profile group with URL filtering security profile 1 that allows the URL `example.com` and a threat prevention security profile that inspects traffic to the URL `example.com`  
200 | Egress | TCP | All | Any | Any | 80, 443 | Apply a security profile group with URL filtering security profile 2 that allows the URL `examplepetstore.com`  
  
The following table shows the correct configuration:

Priority | Direction | Protocol | Target | Source | Destination | Destination port | Action  
---|---|---|---|---|---|---|---  
100 | Egress | TCP | All | Any | FQDN = `example.com` | 80, 443 | Apply a security profile group with threat prevention security profile that inspects traffic to the URL `example.com`  
200 | Egress | TCP | All | Any | FQDN = `examplepetstore.com` | 80, 443 | Apply a security profile group with URL filtering security profile that allows the URL `examplepetstore.com`  
  
### Avoid creating rules based on a single resource

To address temporary requirements, avoid creating firewall policy rules with URL filtering that use a single resource as a source.

If you keep these rules, the default action of a URL filtering security profile might allow or deny unintended traffic. If you don't delete them immediately, these rules can also lead to policy sprawl over time.

In the following example, a rule with a higher priority of `100` matches and allows traffic from `192.168.1.1` to `examplepetstore.com`. This evaluation occurs before the traffic reaches rule with a priority of `101`, which is configured to block that traffic.

Priority | Direction | Network context | Protocol | Target | Source | Destination | Destination port | Action  
---|---|---|---|---|---|---|---|---  
100 | Egress | Internet | TCP | All | 192.168.1.1/32 | Any | 80, 443 | Apply a security profile group with URL filtering security profile 1 that blocks the URL `example.com`  
101 | Egress | Non-internet | TCP | All | 192.168.1.0/24 | Any | 80, 443 | Apply a security profile group with URL filtering security profile 2 that blocks the URL `examplepetstore.com` and allows the URL `example.org`  
  
However, if you need to retain such a rule, use a destination FQDN object. For example, to avoid matching traffic from `192.168.1.1` to `examplepetstore.com`, add the FQDN object `example.com` to the rule with the priority of `100`.

Priority | Direction | Network context | Protocol | Target | Source | Destination | Destination port | Action  
---|---|---|---|---|---|---|---|---  
100 | Egress | Internet | TCP | All | 192.168.1.1/32 | FQDN = `example.com` | 80, 443 | Apply a security profile group with URL filtering security profile 1 that blocks the URL `example.com`  
101 | Egress | Non-internet | TCP | All | 192.168.1.0/24 | Any | 80, 443 | Apply a security profile group with URL filtering security profile 2 that blocks the URL `examplepetstore.com` and allows the URL `example.org`  
  
### Use FQDN-based filtering for non-HTTP protocols

Use FQDN-based filtering for non-HTTP and non-HTTPS protocols, such as RDP or SSH. URL filtering only works with HTTP or HTTPS traffic.

## Avoid using URL filtering in hierarchical firewall policies

To prevent unintended traffic matches, avoid using URL filtering security profiles in the [hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies). Instead, use URL filtering security profiles in the global or regional network firewall policies.

Using a URL filtering security profile in a hierarchical firewall policy rule can cause traffic for a broad set of targets to match that rule. This broad matching can cause the security profile's default action to unintentionally allow or deny traffic.

## Create separate security profiles for scale

To stay within the [supported limit](https://docs.cloud.google.com/firewall/docs/quotas#per-security-profile) for the number of domains or [matcher strings](https://docs.cloud.google.com/firewall/docs/configure-urlf-security-profiles#url-matcher-strings) in a URL filtering security profile, create separate security profiles that group domains based on a specific criteria. For example, group domains based on the traffic type or the location and nature of the destination domain, such as east-west (non-internet-bound) and internet-bound traffic.

This segmentation helps ensure optimal performance and manageability when you use many domains.

For example, create one profile for internal or Google Cloud domains and another for external domains on the public internet. A separate profile for internal domains keeps internal traffic routing and security policies distinct. A separate profile for external domains lets you apply appropriate security measures, such as threat intelligence feeds or stricter egress controls, to external traffic.

## What's next

  * [URL filtering service](https://docs.cloud.google.com/firewall/docs/about-url-filtering)
  * [Create and manage URL filtering security profiles](https://docs.cloud.google.com/firewall/docs/configure-urlf-security-profiles)
  * [Create and manage threat prevention security profiles](https://docs.cloud.google.com/firewall/docs/configure-security-profiles)
  * [Create and manage security profile groups](https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups)
  * [Use global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies)
  * [Use regional network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
