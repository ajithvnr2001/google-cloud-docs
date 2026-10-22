---
url: https://docs.cloud.google.com/armor/docs/best-practices/
title: Best practices for Cloud Armor \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:32.065934+00:00
---

# Best practices for Cloud Armor  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Best practices for Cloud Armor Stay organized with collections  Save and categorize content based on your preferences. 

You can optimize and tune your Google Cloud Armor deployments to help to protect your services against denial-of-service (DoS) and web attacks. This document describes best practices to help you enhance your application's security posture, improve performance, and take a more efficient approach to threat protection by using Google's global infrastructure and security systems.

Cloud Armor integrates with Google Cloud load balancers. When you deploy Cloud Armor, you create security policies that consist of pre-configured and custom rules. You then attach these policies to the backend services of your load balancers to help protect the backend services.

To learn about best practices for centrally managing Cloud Armor policies across your organization and allowing for project-specific rules, see [Managing Cloud Armor using custom constraints](https://docs.cloud.google.com/armor/docs/custom-constraints).

## Security policy and rule creation

The following sections contain best practices and recommendations for new security policies and rules.

### Provide rule descriptions

Use rule descriptions to provide additional context about why each rule was created and the intended function of the rule. The **description** field is limited to 64 characters, so references to configuration management databases or other repositories are the most efficient way to capture context.

### Consider priority spacing

When you initially configure rules, leave an interval of at least 10 between each rule priority value. For example, the first two rules in a security policy could have priorities 20 and 30. This lets you insert more rules when you need them. In addition, we recommend that you group similar rules into blocks, leaving larger intervals between groups.

### Use preview mode

Security policy rules, including Open Web Application Security Project (OWASP) signatures, can have unpredictable effects on your application. Use [preview mode](https://docs.cloud.google.com/armor/docs/security-policy-overview#preview_mode), to evaluate whether the introduction of a rule will have a negative impact on production traffic.

### Enable Google Cloud Armor Adaptive Protection

[Enable Adaptive Protection](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview#configure-alert-tuning) for additional protection of your applications. Adaptive Protection monitors traffic and (as necessary) recommends new rules for your security policies. In addition, we recommend that you put an [alerting policy](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview#monitor-alert-log) in place to ensure that the right people are alerted about potential attacks. Adaptive Protection is best suited for volumetric protection. Attacks that are not volumetric might not trigger Adaptive Protection. 

### Enable JSON parsing

If your application sends JSON content in the request body, ensure that you enable JSON parsing. If you don't enable JSON parsing, Cloud Armor does not parse the JSON content of request bodies for preconfigured WAF rules, and the results can be noisy and generate false positives. For additional information, see [JSON parsing](https://docs.cloud.google.com/armor/docs/content-parsing#enable-json-parsing).

### Test your logic

A rule is triggered when its match condition evaluates to true; for example, the match condition `origin.region_code == 'AU'` evaluates to true if the region code of the request is `AU`. If a higher priority rule evaluates to true, then the action in a lower priority rule is ignored.

**Note:** The rule with a lower numeric priority represents a higher evaluation priority. For more information, see [Rule evaluation order](https://docs.cloud.google.com/armor/docs/security-policy-overview#eval-order).

In the following example, imagine that you want to create a security policy to block users from the `AU` region, except for traffic within the IP address range `10.10.10.0/24`. Consider the following security policy with two rules:
    
    
    Rule1
    expr: inIpRange(origin.ip, '10.10.10.0/24')
    action: allow
    priority: 1
    Rule2
    expr: origin.region_code == 'AU'
    action: deny(403)
    priority: 2
    

In this example, `Rule1` allows traffic that originates from the IP address range `10.10.10.0/24`. Because `Rule1` is the higher-priority rule, such traffic is allowed before it is evaluated against `Rule2`, meaning that Cloud Armor does not evaluate it against `Rule2` (or any other remaining rules).

To achieve a similar exception within a single rule, you can combine match conditions using logical operators. It is important to note that this approach differs from the two-rule example in how subsequent rules are evaluated. For example, the following expression uses a single rule that denies `AU` traffic unless it is from the specific IP range `10.10.10.0/24`:
    
    
    expr: origin.region_code == 'AU' && !inIpRange(origin.ip, '10.10.10.0/24')
    action: deny(403)
    priority: 1
    

This condition only evaluates to true (and triggers a deny action) if both the region is `AU` and the IP address is _not_ within the `10.10.10.0/24` range.

**Note:** The two-rule example uses an allow rule that bypasses subsequent rules for matching traffic. In contrast, traffic not matching this single deny rule (including traffic from `10.10.10.0/24`) continues to be evaluated against any lower-priority rules in the policy.

When you create Cloud Armor policies, test the logic of your rules to ensure that you achieve the intended behavior. To do so, we recommend that you generate synthetic traffic to understand which rules are blocking traffic, and verify that your results are consistent with your rule design decisions. If you're unsure of how a request might flow through the system, use preview mode to see which rule matches the request.

### Identify the client IP addresses of your scanners

Your security scanners can be located inside or outside of Google. If you want an outside and unfiltered assessment of your application, you can explicitly allow traffic based on IP address (or other token) prior to evaluating it against any other rules.

### Group and sort rules in your security policy

Your applications might serve different subsets of your customers. In the following example, you want to deny traffic from certain geographical areas or IP ranges, and therefore you configure the first rule in your policy to deny such traffic. Additionally, you want to explicitly allow some traffic into the application without the security policy processing it. For this example, we recommend the following structure of rule priority, from greatest-priority to least-priority:

  1. Explicit deny rules (ASN, region, IP ranges)
  2. Trusted explicit allow rules (scanners, trusted systems - use with extreme caution)
  3. Security rules (OWASP, custom rules)
  4. Explicit allow rules (ASN, presence of header value, IP range)
  5. Default deny rules



### Use reCAPTCHA for bot management

Cloud Armor integrates with Google's reCAPTCHA for bot detection at the Web Application Firewall (WAF) layer. In this integration, reCAPTCHA generates reCAPTCHA tokens, and Cloud Armor performs the token assessment process instead of reCAPTCHA. This reduces origin load, potentially reducing your costs, and puts security controls closer to the end user than your backends. For more information, see the [bot management overview](https://docs.cloud.google.com/armor/docs/bot-management). 

### Set rate limiting thresholds

Rate limiting is a a flexible and valuable capability to help prevent abuse and mitigate high volume threats like credential stuffing or layer 7 (L7) distributed denial-of-service (DDoS) attacks. When you deploy rate limiting for the first time, it is important to choose a threshold that makes sense for your application. We recommend that you start with enforcement in preview mode. As you analyze and understand the traffic profile, you can adjust the rate limiting parameters. In addition, it is important to consider the priority that you assign to the rate limiting rule. Traffic might be explicitly allowed or denied by a higher priority rule before it is evaluated against the rate limiting rule.

## Rule tuning

Web applications might allow requests that appear to be attacks, and they might allow, or even require, that users send requests that match the signatures in preconfigured WAF rules. It is critical that you validate your Cloud Armor rules against your application and address any findings that might not be relevant for your application prior to promoting the rule by disabling preview mode on a production application. The following sections contain best practices and recommendations for tuning the preconfigured WAF rules.

### Choose your preconfigured WAF rule sensitivity level

When you implement any of the preconfigured WAF rules, you can choose an appropriate sensitivity level based on your security requirements and timelines. We recommend that you begin with a sensitivity level of 1 for most applications that must meet your organization's security requirements. Rules configured for sensitivity 1 use high fidelity signatures and reduce potential noise from the rule. Signatures associated with higher sensitivities might detect and prevent a larger set of exploit attempts, at the expense of potential noise for some protected applications. However, workloads subject to more strict security requirements might prefer the highest sensitivity level. For these use-cases, there might be a great amount of noise or irrelevant findings, which you must address using tuning before the security policy goes into production.

### Enable verbose logging

If you require additional information about which request attributes and payloads are triggering a particular WAF rule, enable [verbose logging](https://docs.cloud.google.com/armor/docs/verbose-logging). Verbose logging provides details from requests that trigger particular rules, including a snippet of the offending portion of the request, which is helpful for troubleshooting and tuning Cloud Armor. Because verbose logging can cause end-user request content to be logged in Cloud Logging, there is a chance that you accumulate end-user PII in your logs. As a result, we don't recommend running production workloads with verbose logging enabled for long periods of time.

### Use stable or canary rules

Both Cloud Armor preconfigured WAF rules and managed rules offer _stable_ and _canary_ versions.

  * For preconfigured rules, updates from the OWASP Core Rule Set (CRS) are first released to the canary version, and then promoted to the stable version.
  * For managed rules, automated signature updates are first released to the canary version, and then promoted to the stable version (or expedited for zero-day rules).



When you use automatic updates, we recommend that you maintain canary rules in preview mode with a higher priority and keep stable rules in enforced mode with a lower priority. This approach helps you preview and validate rule changes using logs before they affect production traffic. For instructions on configuring this setup, see [Evaluate new rules with canary preview mode](https://docs.cloud.google.com/armor/docs/set-up-managed-rules#apply-canary-and-stable).

## Logging and monitoring

The following sections contain best practices and recommendations for configuring logging and monitoring.

### Use the Security Command Center

Cloud Armor integrates automatically with the Security Command Center. Cloud Armor exports different findings to the Security Command Center:

  * Allowed Traffic Spike
  * Increasing Deny Ratio



Make sure that your web security personnel examine these findings. 

### Choose a Cloud Logging sampling rate

Cloud Armor per-request logs use the global external Application Load Balancer or the classic Application Load Balancer's logging infrastructure. As a result, Cloud Armor log generation is subject to the log sampling rate configured on the load balancer. We recommend keeping the sampling rate to 1 when you are actively tuning and implementing Cloud Armor. After you finish tuning and implementing Cloud Armor, we recommend that you keep full request logging turned on; however, you might prefer to down-sample to a lower rate. Both the global external Application Load Balancer and the classic Application Load Balancer don't enable logs by default, so it is important that you enable logging manually.

Note: Adaptive Protection logs are exposed in the Google Cloud console under the `network_security_policy` resource, not under the global external Application Load Balancer or the classic Application Load Balancer. 

### Use the Cloud Monitoring dashboard

Having a clear view of what is happening in your Cloud Armor configuration is essential. To make this easier, you can use the [security dashboard](https://docs.cloud.google.com/armor/docs/monitoring#viewing_the_monitoring_dashboard). Additionally, you can export Cloud Armor logs directly from Logging to your own platform. If you are using Adaptive Protection, it is important to have an escalation path for any Adaptive Protection alerts that are triggered. 

## General management

The following contain additional best practices and recommendations for configuring Cloud Armor.

### Set up Identity and Access Management access control

In accordance with general Google Cloud IAM best practices, ensure that the right people have access to Cloud Armor. The Compute Security Admin role is required to configure, modify, update, and delete Cloud Armor security policies. Additionally, the Compute Network Admin role or `compute.backendServices.setSecurityPolicy` permission is required to attach a Cloud Armor security policy to a backend service.

### Minimize the number of policies

A Cloud Armor policy can be reused across multiple backend services. We recommend that you have a consistent set of reusable security policies.

### Use Terraform

To ensure that configurations can be rolled back, as well as reproduced across projects, we recommend using Terraform. Cloud Armor has full [Terraform integration](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_security_policy) for GA features.

### Configure Cloud Armor with Google Kubernetes Engine

If you are using Google Kubernetes Engine (GKE), you must configure Cloud Armor and other ingress features through `BackendConfig` parameters. We recommend that you avoid manually configuring a global external Application Load Balancer or a classic Application Load Balancer to serve as an ingress point. For more information about configuring Cloud Armor with GKE, see [Configuring ingress features](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-features#cloud_armor).

After you configure a Cloud Armor security policy, you can also use [Kubernetes Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_cloud_armor) to enable it with GKE. Make sure that you [create a Cloud Armor backend security policy](https://docs.cloud.google.com/armor/docs/configure-security-policies) prior to referencing the policy in your `GCPBackendPolicy` policy resource. If you are enabling a regional Gateway, then you must create a _regional_ Cloud Armor backend security policy.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
