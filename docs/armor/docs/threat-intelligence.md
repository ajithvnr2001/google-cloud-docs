---
url: https://docs.cloud.google.com/armor/docs/threat-intelligence/
title: Apply Google Threat Intelligence \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:58.213200+00:00
---

# Apply Google Threat Intelligence  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/threat-intelligence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Apply Google Threat Intelligence Stay organized with collections  Save and categorize content based on your preferences. 

Google Threat Intelligence lets Google Cloud Armor Enterprise subscribers secure their traffic by allowing or blocking traffic to their external Application Load Balancers based on several categories of threat intelligence data.

Google Threat Intelligence data is divided into the following categories:

  * **Tor exit nodes** : [Tor](https://www.torproject.org/about/) is open-source software that enables anonymous communication. To exclude users who hide their identity, block the IP addresses of Tor exit nodes (points where traffic exits the Tor network).
  * **Known malicious IP addresses** : IP addresses that need to be blocked to improve your application's security posture because attacks on web applications are known to originate there.
  * **Search engines** : IP addresses that you can allow to enable site indexing.
  * **VPN providers** : IP addresses that are used by low-reputation VPN providers. This category can be blocked to deny attempts to circumnavigate IP address-based rules.
  * **Anonymous proxies** : IP addresses that are used by known anonymous proxies.
  * **Crypto miners** : IP addresses that are used by known cryptocurrency mining websites.
  * **Public cloud IP address ranges** : This category can be either blocked to avoid malicious automated tools from browsing web applications or allowed if your service uses other public clouds.



To use Google Threat Intelligence, you define security policy rules that allow or block traffic based on some or all of these categories by using the `evaluateThreatIntelligence` match expression along with a feed name that represents one of the preceding categories. In addition, you must subscribe to Cloud Armor Enterprise. For more information about Cloud Armor Enterprise, see the [Cloud Armor Enterprise overview](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview).

## Configure Google Threat Intelligence

To use Google Threat Intelligence, you configure security policy rules by using the `evaluateThreatIntelligence('FEED_NAME')` match expression, providing a `FEED_NAME` based on the category that you want to allow or block. Information within each feed is continually updated, protecting services from new threats without additional configuration steps. The valid arguments are as follows.

Feed name | Description  
---|---  
`iplist-tor-exit-nodes` | Matches Tor exit nodes' IP addresses  
`iplist-known-malicious-ips` | Matches IP addresses known to attack web applications  
`iplist-search-engines-crawlers` | Matches IP addresses of search engine crawlers  
`iplist-vpn-providers` | Matches IP address ranges that are used by low-reputation VPN providers  
`iplist-anon-proxies` | Matches IP address ranges that belong to open anonymous proxies  
`iplist-crypto-miners` | Matches IP address ranges that belong to crypto mining sites  
`iplist-cloudflare` | Matches [IPv4](https://www.cloudflare.com/ips-v4) and [IPv6](https://www.cloudflare.com/ips-v6) address ranges of Cloudflare proxy services  
`iplist-fastly` | Matches [IP address ranges of Fastly proxy services](https://api.fastly.com/public-ip-list)  
`iplist-imperva` | Matches [IP address ranges of Imperva proxy services](https://docs.imperva.com/howto/c85245b7)  
`iplist-public-clouds`

  * `iplist-public-clouds-aws`
  * `iplist-public-clouds-azure`
  * `iplist-public-clouds-gcp`

| Matches IP addresses belonging to public clouds

  * Matches IP address ranges used by Amazon Web Services
  * Matches IP address ranges used by Microsoft Azure
  * Matches IP address ranges used by Google Cloud

  
  
You can configure a new security policy rule using the following `gcloud` command, with a FEED_NAME from the previous table and any ACTION like `allow`, `deny`, or `throttle`. For more information about rule actions, see [policy types](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types).
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy=NAME \
        --expression="evaluateThreatIntelligence('FEED_NAME')" \
        --action="ACTION"
    

Replace the following:

  * `NAME`: the name of the security policy that you want to set up
  * `FEED_NAME`: the feed name from the previous table
  * `ACTION`: the action to take for the rule, such as `allow`, `deny`, or `throttle`



### Examples of Google Threat Intelligence expressions

  * You can use Google Threat Intelligence with a user IP address.



The following example command uses the `iplist-tor-exit-nodes` feed name with a caller's User IP address:
    
    
        evaluateThreatIntelligence('iplist-tor-exit-nodes', origin.user_ip)
      

For more information, see [User IP addresses overview](https://docs.cloud.google.com/armor/docs/user-ip-overview).

**Note:** If the second parameter is not provided, it defaults to `origin.ip`.

  * You can prevent Google Threat Intelligence from blocking a specific IP address or IP address range by adding the address to the exclusion list.



The following example command uses the `iplist-known-malicious-ips` feed name:
    
    
        evaluateThreatIntelligence('iplist-known-malicious-ips', ['ADDRESS'])
      

Replace `ADDRESS` with the address or address range that you want to exclude.

  * You can use Google Threat Intelligence with a User IP address. Add an IP address or IP address range to the exclusion list to prevent Google Threat Intelligence from blocking it.



The following example command uses the `iplist-known-malicious-ips` feed name with a User IP address:
    
    
        evaluateThreatIntelligence('iplist-known-malicious-ips', origin.user_ip, ['ADDRESS'])
      

## Use named IP address lists

**Note:** Google Cloud Armor named IP address lists are deprecated. We recommend that you use Google Threat Intelligence feeds instead.

Cloud Armor-named IP address lists let you reference lists of IP addresses and IP ranges that are maintained by third-party providers. You can configure named IP address lists within a security policy. You don't need to manually specify each IP address or IP range individually.

In this document, the terms _IP address_ and _IP address list_ include _IP address ranges_.

Named IP address lists are lists of IP addresses grouped under different names. The name typically refers to the provider. Named IP address lists are not subject to the quota limit on the number of IP addresses per rule.

Named IP address lists are not security policies. You incorporate them into a security policy by referencing them as expressions the same way that you reference a preconfigured rule.

For example, if a third-party provider has an IP address list of `{ip1, ip2, ip3....ip_N_}` under the name `provider-a`, you can create a security rule that allows all IP addresses that are in the `provider-a` list and excludes IP addresses that are not in that list:
    
    
    gcloud beta compute security-policies rules create 1000 \
        --security-policy POLICY_NAME \
        --expression "evaluatePreconfiguredWaf('provider-a')" \
        --action "allow"
    

Replace `POLICY_NAME` with the name of the security policy that you want to set up.

You cannot create your own custom named IP address lists. This feature is available only with respect to named IP address lists that are maintained by third-party providers that partner with Google. If such named IP address lists don't meet your needs, you can create a security policy where the rules allow or deny access to your resources based on the IP address where requests originate from. For more information, see [Create and view Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/configure-security-policies).

To use named IP address lists, you must subscribe to [Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview) and enroll projects in Cloud Armor Enterprise. For more information, see Availability of named IP address lists.

### Allowing traffic only from permitted third-party providers

A typical use case is to create an allowlist containing the IP addresses of a permitted third-party partner to ensure that only traffic coming from this partner can access the load balancer and the backends.

For example, CDN providers need to pull content from origin servers at regular intervals to distribute them to their own caches. A partnership with Google provides a direct connection between CDN providers and the Google network edge. CDN users on Google Cloud can use this direct connection during origin pulls. In this case, the CDN user might want to build a security policy that only allows traffic coming from that particular CDN provider.

In this example, a CDN provider publishes its IP address list `23.235.32.0/20, 43.249.72.0/22, ⋯,`. A CDN user configures a security rule that only allows traffic coming from these IP addresses. As a result, two CDN provider access points are allowed (`23.235.32.10` and `43.249.72.10`) and their traffic is therefore permitted. Traffic from the unauthorized access point `198.51.100.1` is blocked.

[ ![Cloud Armor named IP address.](https://docs.cloud.google.com/static/armor/images/ca-named-ip.svg)](https://docs.cloud.google.com/static/armor/images/ca-named-ip.svg) Cloud Armor named IP address (click to enlarge).

### Simplifying configuration and management by using preconfigured rules

CDN providers often use IP addresses that are well-known and that many CDN users need to use. These lists change over time, as providers add, remove, and update the IP addresses.

Using a named IP address list in a security policy rule simplifies the process of configuring and managing IP addresses because Cloud Armor automatically synchronizes information from CDN providers on a daily basis. This eliminates the time-consuming and error-prone process of maintaining a large IP address list manually.

The following is an example of a preconfigured rule that allows all traffic from a provider:
    
    
    evaluatePreconfiguredWaf('provider-a') => allow traffic
    

### IP address list providers

The IP address list providers in the following table are supported for Cloud Armor. These are CDN providers that have partnered with Google. Their IP address lists are published through individual public URLs.

These partners provide separate lists of IPv4 addresses and IPv6 addresses. Cloud Armor uses the provided URLs to fetch lists, and then converts the lists into named IP address lists. You refer to the lists by the names in the table.

For example, the following code creates a rule in the security policy `POLICY_NAME` with priority 750, incorporating the named IP address list from Cloudflare and allowing access from those IP addresses:
    
    
    gcloud beta compute security-policies rules create 750 \
        --security-policy POLICY_NAME \
        --expression "evaluatePreconfiguredWaf('sourceiplist-cloudflare')" \
        --action "allow"
    

Replace `POLICY_NAME` with the name of the security policy that you want to set up.

Provider | URLs | IP address list name  
---|---|---  
Fastly | `https://api.fastly.com/public-ip-list` | `sourceiplist-fastly`  
Cloudflare |  `https://www.cloudflare.com/ips-v4` `https://www.cloudflare.com/ips-v6` | `sourceiplist-cloudflare`  
Imperva |  `https://my.imperva.com/api/integration/v1/ips` Access to Imperva's list requires a `POST` request. You can use the following command as well: `curl -d "" https://my.imperva.com/api/integration/v1/ips` | `sourceiplist-imperva`  
  
To list the preconfigured named IP address lists, use this gcloud CLI command:
    
    
    gcloud compute security-policies list-preconfigured-expression-sets \
        --filter="id:sourceiplist"
    

The output is similar to the following:
    
    
    EXPRESSION_SET
    sourceiplist-fastly
    sourceiplist-cloudflare
    sourceiplist-imperva
    

### Synchronizing IP address lists

Cloud Armor synchronizes IP address lists with each provider only when it detects changes that are in a valid format. Cloud Armor performs basic syntax validation on the IP addresses in all lists.

### Availability of named IP address lists

[Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-using) is in general availability. The availability of named IP address lists from third parties is as follows:

  1. If you are subscribed to the Cloud Armor Enterprise tier, you are licensed to use named IP address lists in enrolled projects. You can create, update, and delete rules with named IP address lists.
  2. If your Cloud Armor Enterprise tier subscription expires, or you otherwise return to Standard tier, you cannot add or modify rules with named IP address lists, but you can delete existing rules and update rules to remove a named IP list.
  3. For projects that already include rules with named IP address lists and that you did not enroll in Cloud Armor Enterprise, you can continue to use, update, and delete existing rules with named IP address lists. In such projects, you can create new rules that incorporate named IP address lists.



## What's next

  * [Create and view Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/configure-security-policies)
  * [View pricing for Cloud Armor Enterprise tiers](https://cloud.google.com/armor/pricing)
  * [Troubleshoot issues](https://docs.cloud.google.com/armor/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
