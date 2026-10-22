---
url: https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview/
title: Google Threat Intelligence for firewall policy rules \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:15.029682+00:00
---

# Google Threat Intelligence for firewall policy rules  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Google Threat Intelligence for firewall policy rules Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how firewall policy rules secure your network by allowing or blocking traffic based on Google Threat Intelligence data. Google Threat Intelligence data includes lists of IP addresses based on the following categories:

  * **Tor exit nodes** : [Tor](https://www.torproject.org/about/) is open source software that enables anonymous communication. To exclude users who hide their identity, block the IP addresses of Tor exit nodes (endpoints at which traffic exits the Tor network).
  * **Known malicious IP addresses** : IP addresses that are known to be the origin of web application attacks. To improve your application's security posture, block these IP addresses.
  * **Search engines** : IP addresses that you can allow to enable site indexing.
  * **Public cloud IP address ranges** : this category can be either blocked to avoid malicious automated tools from browsing web applications or allowed if your service uses other public clouds. This category is further divided into the following subcategories: 
    * IP address ranges used by Amazon Web Services
    * IP address ranges used by Microsoft Azure
    * IP address ranges used by Google Cloud
    * IP address ranges used by Google services



The Google Threat Intelligence data lists can include IPv4 addresses, IPv6 addresses, or both. To configure Google Threat Intelligence in your firewall policy rules, use the predefined Google Threat Intelligence list names based on the category that you want to allow or block. These lists are continually updated, protecting services from new threats without additional configuration steps. The valid list names are as follows.

List name | Description  
---|---  
Known malicious IPs  
(`iplist-known-malicious-ips`) | Matches IP addresses known to attack web applications  
Search engine crawlers  
(`iplist-search-engines-crawlers`) | Matches IP addresses of search engine crawlers  
Tor exit nodes  
(`iplist-tor-exit-nodes`) | Matches IP addresses of Tor exit nodes  
Public cloud IPs  
(`iplist-public-clouds`) | Matches IP addresses belonging to public clouds  
Public clouds - AWS  
(`iplist-public-clouds-aws`) | Matches IP address ranges used by Amazon Web Services  
Public clouds - Azure  
(`iplist-public-clouds-azure`) | Matches IP address ranges used by Microsoft Azure  
Public clouds - Google Cloud  
(`iplist-public-clouds-gcp`) | Matches IP address ranges used by customer resources, such as Compute Engine VMs and GKE clusters. These ranges include [customer-assigned IP ranges](https://www.gstatic.com/ipranges/cloud.json) used by all Google Cloud customers and are not restricted to your own project or organization.   
Public clouds - Google services  
(`iplist-public-clouds-google-services`) | Matches IP address ranges used for API and web access to all Google services, including Google Cloud, Google Workspace, Maps, and YouTube. This list covers Google-owned service infrastructure, such as Google Public DNS, and represents the subset of [Google public IP ranges](https://www.gstatic.com/ipranges/goog.json) distinct from the customer-assigned IPs in the Google Cloud list.   
VPN providers  
(`iplist-vpn-providers`) | Matches IP addresses that belong to low-reputation VPN providers  
Anonymous proxies  
(`iplist-anon-proxies`) | Matches IP addresses that belong to open anonymous proxies  
Crypto mining sites  
(`iplist-crypto-miners`) | Matches IP addresses that belong to cryptocurrency mining sites  
  
## Use Google Threat Intelligence with other firewall policy rule filters

To define a firewall policy rule with Google Threat Intelligence, follow these guidelines:

  * For egress rules, specify the destination by using one or more destination Google Threat Intelligence lists.

  * For ingress rules, specify the source by using one or more source Google Threat Intelligence lists.

  * You can configure Google Threat Intelligence lists for hierarchical firewall policies, global network firewall policies, and regional network firewall policies.

  * You can use these lists along with other source or destination rule filter components.

For information about how Google Threat Intelligence lists work with other source filters in the ingress rules, see [Sources for ingress rules in hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-ingress-src) and [Sources for ingress rules in network firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#nfp-ingress-src).

For information about how Google Threat Intelligence lists work with other destination filters in the egress rules, see [Destinations for egress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-dest).

  * [Firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview) is done at the rule level. To make it easier for you to debug and analyze the effect of your firewall rules, don't include multiple Google Threat Intelligence lists in a single firewall rule.

  * You can add multiple Google Threat Intelligence lists to a firewall policy rule. Each list name included in the rule is counted as one attribute regardless of the number of IP addresses or IP address ranges included in that list. For example, if you have included the `iplist-tor-exit-nodes`, `iplist-known-malicious-ips`, and `iplist-search-engines-crawlers` list names in your firewall policy rule, the rule attribute count per firewall policy is increased by three. For more information about the rule attribute count, see [Rule attribute count details](https://docs.cloud.google.com/firewall/docs/quotas#per-firewall-policy-rule-attr-count).




## Creating exceptions to Google Threat Intelligence lists

If you have rules that apply to Google Threat Intelligence lists, you can use the following techniques to create exception rules that are applicable to certain IP addresses within a Google Threat Intelligence list:

  * **Selective allow firewall rule** : suppose you have an ingress or egress firewall rule that denies packets from or to a Google Threat Intelligence list. To allow packets from or to a selected IP address within that Google Threat Intelligence list, create a separate higher-priority ingress or egress allow firewall rule that specifies the exception IP address as a source or destination.

  * **Selective deny firewall rule** : suppose you have an ingress or egress firewall rule that allows packets from or to a Google Threat Intelligence list. To deny packets from or to a selected IP address within that Google Threat Intelligence list, create a higher-priority ingress or egress deny firewall rule that specifies the exception IP address as a source or destination.




## What's next

  * [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details)
  * [Fully qualified domain name objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview)
  * [Address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
