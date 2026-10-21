---
url: https://docs.cloud.google.com/armor/docs/user-ip-overview/
title: User IP addresses \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:36:50.026098+00:00
---

# User IP addresses  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/user-ip-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  User IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Armor security policy rules that filter based on an IP address typically use the caller's client IP. When your services are behind an intermediary, such as a third-party content delivery network (CDN), the client IP in the `origin.ip` field is the IP address of the last intermediary, not the original client.

The user IP feature lets you configure an alternate field, `origin.user_ip`, to resolve from a header that the upstream provider populates. You can then use the `origin.user_ip` field in your security policy rules to specify the IP address used in those features. You can configure the `userIpRequestHeaders[]` option in the security policy's `advancedOptionsConfig` field when using `origin.user_ip`.

## How user IP addresses work

You configure Cloud Armor to extract the end user's IP address from a specific request header. This value populates the `origin.user_ip` field, which you can then use in your security policy rules.

If the headers specified in `userIpRequestHeaders[]` don't exist, or if their values are not valid IP addresses, then Cloud Armor falls back to the client IP address (`origin.ip`) instead. The following example shows a direct comparison for the default case.
    
    
    origin.ip != origin.user_ip
    

The following examples show how to use `origin.user_ip` in the rules language, with Google Threat Intelligence, and in address groups.

### `inIpRange`
    
    
    inIpRange(origin.user_ip, '9.9.9.0/24')
    

For more information about using `inIpRange` with `origin.user_ip`, see [Attributes](https://docs.cloud.google.com/armor/docs/rules-language-reference#attributes).

### Google Threat Intelligence
    
    
    evaluateThreatIntelligence('iplist-known-malicious-ips', origin.user_ip)
    

For more information, see [Apply Google Threat Intelligence](https://docs.cloud.google.com/armor/docs/threat-intelligence).

### Address groups
    
    
    evaluateAddressGroup('example-address-group', origin.user_ip)
    

For more information, see [Configure address groups](https://docs.cloud.google.com/armor/docs/address-groups-using).

### Organization-scoped address groups
    
    
    evaluateOrganizationAddressGroup('example-org-address-group', origin.user_ip)
    

For more information, see [Use organization-scoped address groups](https://docs.cloud.google.com/armor/docs/address-groups-using#use-org-scoped).

## Best practices

Because `origin.user_ip` resolves from a request header, which an untrusted client can manipulate, you must validate that traffic originates from a trusted upstream source.

To validate the upstream source, create a security policy with at least two rules. The first rule, with a higher priority, checks that the immediate client IP (`origin.ip`) belongs to your trusted upstream provider. The second rule, with a lower priority, applies your intended logic using the `origin.user_ip` field.

For example, you can create a policy with the following two rules:

  * Rule 1: `evaluateThreatIntelligence('iplist-public-clouds', origin.ip)`
  * Rule 2: `inIpRange(origin.user_ip, '9.9.9.0/24')`



## What's next

  * [Configure custom rules language attributes](https://docs.cloud.google.com/armor/docs/rules-language-reference)
  * [Apply Google Threat Intelligence](https://docs.cloud.google.com/armor/docs/threat-intelligence)
  * [Configure address groups](https://docs.cloud.google.com/armor/docs/address-groups-using)
  * [Use organization-scoped address groups](https://docs.cloud.google.com/armor/docs/address-groups-using#use-org-scoped)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
