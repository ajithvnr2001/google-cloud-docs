---
url: https://docs.cloud.google.com/armor/docs/release-notes/
title: Cloud Armor release notes \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:17.886887+00:00
---

# Cloud Armor release notes  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Resources ](https://docs.cloud.google.com/armor/docs/resources)



Send feedback 

#  Cloud Armor release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Google Cloud Armor. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/armor-release-notes.xml) directly. 

## October 19, 2026

Security

Security fixes and enhancements to Cloud Armor preconfigured WAF `v33-stable` rulesets. For more information, see [Tuning Google Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning).

The following rulesets have been updated:

  * `sqli-v33-stable`
  * `xss-v33-stable`
  * `lfi-v33-stable`
  * `rfi-v33-stable`
  * `rce-v33-stable`
  * `methodenforcement-v33-stable`
  * `scannerdetection-v33-stable`
  * `protocolattack-v33-stable`
  * `php-v33-stable`
  * `sessionfixation-v33-stable`
  * `java-v33-stable`
  * `nodejs-v33-stable`



Security

Security fixes and enhancements to Cloud Armor preconfigured WAF `stable` rulesets for v3.0. For more information, see [Tuning Google Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning).

The following rulesets have been updated:

  * `sqli-stable`
  * `xss-stable`
  * `lfi-stable`
  * `rfi-stable`
  * `rce-stable`
  * `methodenforcement-stable`
  * `scannerdetection-stable`
  * `protocolattack-stable`
  * `php-stable`
  * `sessionfixation-stable`



## October 14, 2026

Feature

Cloud Armor supports service rate limiting. For more information, see [Cloud Armor and service rate limiting](https://docs.cloud.google.com/armor/docs/integrating-cloud-armor#service-rate-limiting). This feature is available in Preview.

## September 17, 2026

Feature

Cloud Armor managed rulesets protect your backend services and APIs from a wide range of web application threats using threat signatures which are automatically kept up-to-date. For more information, see [Managed rules overview](https://docs.cloud.google.com/armor/docs/managed-rules-overview). This feature is available in Preview.

## August 27, 2026

Security

Cloud Armor supports advanced match conditions to include attributes for inspecting request body content and parameters in Preview. This lets you write custom CEL rules to filter traffic based on raw body content, structured data (JSON, Form Data, GraphQL), and query parameters. For more information, see [Configure custom rules language attributes](https://docs.cloud.google.com/armor/docs/rules-language-reference).

## August 19, 2026

Feature

[Global Front End](https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-overview) is a unified offering that simplifies billing by consolidating pricing across networking products. Cloud Armor is included in the Global Front End Enterprise billing tier. Enabling Global Front End Enterprise in a project enables specific Cloud Armor Enterprise features for your global external Application Load Balancers. For more information, see [Global Front End](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#global-front-end).This feature is available in Preview.

## July 08, 2026

Feature

Cloud Armor preconfigured rules support [ModSecurity Core Rule Set (CRS) 4.22](https://github.com/coreruleset/coreruleset/releases/tag/v4.22.0) as a rule source. For more information, see [Tuning Google Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning). This feature is Generally Available.

## April 06, 2026

Feature

Cloud Armor preconfigured rules support [ModSecurity Core Rule Set (CRS) 4.22](https://github.com/coreruleset/coreruleset/releases/tag/v4.22.0) as a rule source. For more information, see [Tuning Google Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning). This feature is available in Preview.

## March 31, 2026

Feature

Cloud Armor supports a visual **Match Condition Builder** that allows you to create complex expressions in Common Expression Language (CEL) without writing raw code. For more information, see [Use the Match Condition Builder](https://docs.cloud.google.com/armor/docs/manage-security-policies#mcb).

## March 06, 2026

Security

Security fixes and enhancements to Cloud Armor preconfigured WAF `canary` rulesets for v3.0. For more information, see [Tuning Google Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning).

The following rulesets have been updated:

  * `sqli-canary`
  * `xss-canary`
  * `lfi-canary`
  * `rfi-canary`
  * `rce-canary`
  * `methodenforcement-canary`
  * `scannerdetection-canary`
  * `protocolattack-canary`
  * `php-canary`
  * `sessionfixation-canary`



## February 18, 2026

Change

Cloud Armor [preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/waf-rules) support for inspection up to the first 64 kB (either 8 kB, 16 kB, 32 kB, 48 kB, or 64 kB) of the [request body content](https://docs.cloud.google.com/armor/docs/security-policy-overview#request-body) is Generally Available.

## February 13, 2026

Security

Security fixes and enhancements to Cloud Armor preconfigured WAF `v33-canary` rulesets. For more information, see [Tuning Google Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning).

The following rulesets have been updated:

  * `sqli-v33-canary`
  * `xss-v33-canary`
  * `lfi-v33-canary`
  * `rfi-v33-canary`
  * `rce-v33-canary`
  * `methodenforcement-v33-canary`
  * `scannerdetection-v33-canary`
  * `protocolattack-v33-canary`
  * `php-v33-canary`
  * `sessionfixation-v33-canary`
  * `java-v33-canary`
  * `nodejs-v33-canary`



## December 06, 2025

Security

The Cloud Armor `cve-canary` rules include the [`google-mrs-v202512-id000002-rce` signature](https://docs.cloud.google.com/armor/docs/waf-rules#cves_and_other_vulnerabilities) to help detect and mitigate [CVE-2025-55182](https://nvd.nist.gov/vuln/detail/CVE-2025-55182). For more information, see [Cloud Armor preconfigured WAF rules overview](https://docs.cloud.google.com/armor/docs/waf-rules).

## December 03, 2025

Security

The Cloud Armor `cve-canary` rules include the [`google-mrs-v202512-id000001-rce` signature](https://docs.cloud.google.com/armor/docs/waf-rules#cves_and_other_vulnerabilities) to help detect and mitigate [CVE-2025-55182](https://nvd.nist.gov/vuln/detail/CVE-2025-55182). For more information, see [Cloud Armor preconfigured WAF rules overview](https://docs.cloud.google.com/armor/docs/waf-rules).

## October 15, 2025

Feature

Cloud Armor's [Hierarchical security policies](https://docs.cloud.google.com/armor/docs/hierarchical-policies-overview) that facilitate centralized control, enhanced consistency, operational efficiency, and effective delegation of security policy management is Generally Available.

## September 24, 2025

Feature

Cloud Armor supports Autonomous System Numbers (ASNs) in [globally scoped edge security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#expandable-1) for Media CDN edge cache services, and it is Generally Available.

Feature

Cloud Armor supports Network Threat Intelligence (NTI) in [globally scoped edge security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#expandable-1) for Media CDN edge cache services, and it is Generally Available.

## September 16, 2025

Feature

Cloud Armor supports [organization-scoped address groups](https://docs.cloud.google.com/armor/docs/address-groups-overview#organization-scoped-address-group) for security policies, and it is Generally Available.

## August 08, 2025

Feature

Cloud Armor supports Autonomous System Numbers (ASNs) in [globally scoped edge security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#expandable-1) for Media CDN edge cache services in Preview.

## July 23, 2025

Feature

Cloud Armor supports internal service security policies for the [service mesh](https://docs.cloud.google.com/armor/docs/integrating-cloud-armor#service-mesh) to enforce global server-side rate limiting per client in Preview.

## July 08, 2025

Change

Cloud Armor [preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/waf-rules) can now inspect up to the first 64 kB (either 8 kB, 16 kB, 32 kB, 48 kB, or 64 kB) of the [request body content](https://docs.cloud.google.com/armor/docs/security-policy-overview#request-body) in Preview.

## June 27, 2025

Feature

Cloud Armor's [Hierarchical security policies](https://docs.cloud.google.com/armor/docs/hierarchical-policies-overview) facilitate centralized control, enhanced consistency, operational efficiency, and effective delegation of security policy management in Preview.

## June 24, 2025

Feature

Cloud Armor supports [organization-scoped address groups](https://docs.cloud.google.com/armor/docs/address-groups-overview#organization-scoped-address-group) for security policies in Preview.

## June 18, 2025

Feature

Cloud Armor supports Network Threat Intelligence (NTI) in [globally scoped edge security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#expandable-1) for Media CDN edge cache services in Preview.

## June 09, 2025

Change

Cloud Armor supports JA4 rate limiting key, and it is Generally Available. For more information, see [Configure rate limiting](https://docs.cloud.google.com/armor/docs/configure-rate-limiting).

## October 09, 2024

Feature

Cloud Armor support for [IP address groups](https://docs.cloud.google.com/armor/docs/address-groups-overview) is Generally Available.

Feature

Cloud Armor support for regional internal Application Load Balancers is Generally Available. You can use the regional backend security policy type with this load balancer. For more information, see [types of security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types).

## July 17, 2024

Feature

Granular models for Cloud Armor Adaptive Protection are now Generally Available. For more information, see the [Adaptive Protection overview](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview#granular-models).

## June 27, 2024

Feature

Cloud Armor supports [IP address groups](https://docs.cloud.google.com/armor/docs/address-groups-overview) in Preview.

## June 25, 2024

Feature

Cloud Armor support for Layer 7 filtering in [globally scoped edge security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#expandable-1) for Media CDN is now Generally Available.

## May 24, 2024

Feature

Cloud Armor supports Layer 7 filtering in [globally scoped edge security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#expandable-1) for Media CDN in Preview.

## May 20, 2024

Feature

Cloud Armor now supports regional internal Application Load Balancers in public preview. You can use the regional backend security policy type with this load balancer. For more information, see [types of security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types).

## April 03, 2024

Feature

Cloud Armor Enterprise Paygo (formerly Managed Protection Plus Paygo) is now Generally Available. Learn more about [Cloud Armor Enterprise service tiers](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#standard_versus).

Change

The Cloud Armor premium service tier "Cloud Armor Managed Protection Plus" has been renamed to "Cloud Armor Enterprise." This change is being made to reflect the evolution of Cloud Armor's enterprise features. SKU IDs and pricing are unchanged. The name change does not impact the enrollment status of existing projects, or any features that were part of Managed Protection Plus. Learn more about [Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview).

## February 13, 2024

Feature

The following new NTI feeds are now available:

  * `iplist-vpn-providers`
  * `iplist-anon-proxies`
  * `iplist-crypto-miners`



For more information about Network Threat Intelligence, see the [overview](https://docs.cloud.google.com/armor/docs/threat-intelligence).

## January 25, 2024

Feature

The following features are now Generally Available:

  * Parsing of the GraphQL content-type
  * Support for User IP request headers
  * Support for JA3 fingerprints



For more information about parsing GraphQL content, see [Apply parsing on custom Content-Type header values](https://docs.cloud.google.com/armor/docs/rule-tuning#post-parsing). For more information about User IP request headers and JA3, see [Configure custom rules language attributes](https://docs.cloud.google.com/armor/docs/rules-language-reference#attributes).

## December 21, 2023

Feature

Google Cloud Armor integration with reCAPTCHA Enterprise for mobile devices is now in General Availability. See the Cloud Armor [bot management overview](https://docs.cloud.google.com/armor/docs/bot-management#recaptcha-tokens) and the [Overview of reCAPTCHA Enterprise for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha/docs/integration-overview).

## December 11, 2023

Feature

You can now enroll your projects into Managed Protection Plus through a pay-as-you-go option (Preview) instead of subscribing for a one year term. Activating Managed Protection Plus PAYGO gives you access to Cloud Armor premium features such as [Adaptive Protection](https://cloud.google.com/armor/docs/adaptive-protection-overview), [Threat Intelligence](https://docs.cloud.google.com/armor/docs/threat-intelligence), and [Advanced Network DDoS Protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos), without the requirements of annual commitment and with the ability to cancel anytime. Learn more about [what's included](https://docs.cloud.google.com/armor/docs/managed-protection-overview#standard_versus_plus) and [pricing](https://docs.cloud.google.com/armor/pricing).

## December 04, 2023

Feature

DDoS attack visibility is now Generally Available. For more information, see [Access DDoS attack visibility telemetry](https://docs.cloud.google.com/armor/docs/ddos-visibility).

## November 21, 2023

Feature

Network edge security polices (custom rules) are now available to allowlisted users. For more information about network edge policies, see [Types of security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types). In addition, you can learn how to [Configure network edge security policies](https://docs.cloud.google.com/armor/docs/network-edge-policies).

## October 20, 2023

Feature

Cloud Armor for regional HTTP(S) load balancers is now Generally Available. For more information, see the [Security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types).

## August 21, 2023

Feature

Adaptive Protection suggested rules can now be deployed automatically in General Availability. For more information, see [Automatically deploy Adaptive Protection suggested rules](https://docs.cloud.google.com/armor/docs/adaptive-protection-auto-deploy).

## July 17, 2023

Feature

Cloud Armor allows you to filter using custom rules or apply Adaptive Protection based on originating client IP addresses in public preview. If you have an upstream proxy, you can use this feature to evaluate Cloud Armor rules against the original clients' IP addresses, rather than your upstream proxy's IP address. For more information, see the [rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference#attributes).

Feature

Cloud Armor supports parsing of the GraphQL content-type in public preview. For more information, see [POST body content parsing](https://docs.cloud.google.com/armor/docs/security-policy-overview#post-parsing).

## June 20, 2023

Feature

Network edge security polices are now available in public preview to allowlisted users. For more information about network edge policies, see [Types of security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types). In addition, you can learn how to [Configure network edge security policies](https://docs.cloud.google.com/armor/docs/network-edge-policies).

Feature

DDoS attack visibility is now available in public preview. For more information, see [Access DDoS attack visibility telemetry](https://docs.cloud.google.com/armor/docs/ddos-visibility).

## June 12, 2023

Feature

Cloud Armor for regional HTTP(S) load balancers is now available in public preview. For more information, see the [Security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types).

## April 26, 2023

Feature

Google Cloud Armor now supports rate limiting based on multiple keys in General Availability. For more information, see [Apply rate limiting](https://docs.cloud.google.com/armor/docs/rate-limiting-overview#identifying_clients_for_rate_limiting).

## April 12, 2023

Feature

Advanced rule tuning features for preconfigured WAF rules are now Generally Available. For more information about the new tuning features, see [Tune Google Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning).

## March 21, 2023

Feature

[Preview mode](https://docs.cloud.google.com/armor/docs/advanced-network-ddos#use_preview_mode) is now Generally Available for advanced network DDoS protection, allowing you to receive all the logging and telemetry about the detected attack without enforcing the mitigation.

## December 28, 2022

Feature

The rule signature [`942550-sqli`](https://github.com/coreruleset/coreruleset/pull/3055), which covers the vulnerability in which malicious attackers can bypass WAF by appending JSON syntax to SQL injection payloads, is now available. For more information, see the [WAF rules overview](https://docs.cloud.google.com/armor/docs/waf-rules#preconfigured_modsecurity_rules).

## December 16, 2022

Feature

Advanced network DDoS protection is now Generally Available for network load balancers, protocol forwarding, and VMs with public IP addresses. Metering and billing of Managed Protection Plus protected resources and the data processing fee for the endpoint covered by advanced Network DDoS protection will begin on Jan 31, 2023. For more information, see [Configure advanced DDoS protection](https://cloud.google.com/armor/docs/advanced-network-ddos) and the [Cloud armor pricing](https://docs.cloud.google.com/armor/pricing) page.

## November 29, 2022

Feature

Three new rate limiting keys are now Generally Available:

  * HTTP-PATH
  * SNI
  * REGION-CODE



For more information about using rate limiting keys, see the [Rate limiting overview](https://docs.cloud.google.com/armor/docs/rate-limiting-overview).

## October 24, 2022

Feature

Default security policies are now Generally Available. You can configure a default rate-limiting security policy when you use the Google Cloud Console to set up your load balancer. For more information, see the [Rate limiting overview](https://docs.cloud.google.com/armor/docs/rate-limiting-overview#default-policy).

## September 28, 2022

Feature

The rule source for Cloud Armor preconfigured rules now includes [ModSecurity Core Rule Set (CRS) 3.3](https://github.com/coreruleset/coreruleset/releases/tag/v3.3.2) in General Availability. For more information, see [Tuning Google Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning).

## September 21, 2022

Feature

Google Cloud Armor Threat Intelligence (Threat Intel) is generally available. Threat Intelligence lets you secure your traffic by allowing or blocking traffic to your HTTP(S) load balancers based on threat intelligence data. For more information, see [Configuring Threat Intelligence](https://docs.cloud.google.com/armor/docs/threat-intel).

## September 16, 2022

Feature

Advanced rule tuning features for preconfigured WAF rules is now available in public preview. For more information about the new tuning features, see [Tune Google Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning).

Change

The following four libinjection signatures have been added to the `sqli-v33-stable` and `xss-v33-stable` rules:

  * `owasp-crs-v030301-id942100-sqli: SQL Injection Attack Detected via libinjection`
  * `owasp-crs-v030301-id942101-sqli: SQL Injection Attack Detected via libinjection`
  * `owasp-crs-v030301-id941100-xss: XSS Attack Detected via libinjection`
  * `owasp-crs-v030301-id941101-xss: XSS Attack Detected via libinjection`



## September 07, 2022

Feature

Adaptive Protection suggested rules can now be deployed automatically in public preview. For more information, see [Automatically deploy Adaptive Protection suggested rules](https://docs.cloud.google.com/armor/docs/adaptive-protection-auto-deploy).

## August 31, 2022

Feature

The Google Cloud Armor [custom rules language](https://docs.cloud.google.com/armor/docs/rules-language-reference#operations) now supports `URL`, `URL Unicode` and `utf-8` decoding.

## August 16, 2022

Feature

The following two preconfigured WAF rulesets are now available for Google Cloud Armor in public preview:

  * Java attack: `java-v33-stable` and `java-v33-canary`
  * NodeJS attack: `nodejs-v33-stable` and `nodejs-v33-canary`



In addition, the following four libinjection signatures have been added to the `sqli-v33-canary` and `xss-v33-canary` rules:

  * `owasp-crs-v030301-id942100-sqli`: SQL Injection Attack Detected via libinjection
  * `owasp-crs-v030301-id942101-sqli`: SQL Injection Attack Detected via libinjection 
  * `owasp-crs-v030301-id941100-xss`: XSS Attack Detected via libinjection
  * `owasp-crs-v030301-id941101-xss`: XSS Attack Detected via libinjection



## June 30, 2022

Feature

Advanced network DDoS protection is now available for network load balancers, protocol forwarding, and VMs with public IP addresses in public preview. For more information, see [Configure advanced DDoS protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos).

Feature

Google Cloud Armor now supports TCP Proxy load balancers and SSL proxy load balancers in General Availability For more information, see the [security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview).

## June 07, 2022

Feature

Google Cloud Armor Threat Intelligence (Threat Intel) is available in public preview. Threat Intel lets you secure your traffic by allowing or blocking traffic to your HTTP(S) load balancers based on threat intelligence data. For more information, see [Configuring Threat Intelligence](https://docs.cloud.google.com/armor/docs/threat-intel).

## May 25, 2022

Feature

Google Cloud Armor integration with reCAPTCHA Enterprise is now in General Availability. See the Cloud Armor [bot management overview](https://docs.cloud.google.com/armor/docs/bot-management) and the [Overview of reCAPTCHA Enterprise for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha/docs/integration-overview).

## May 16, 2022

Feature

The rule source for Cloud Armor preconfigured rules now includes [ModSecurity Core Rule Set (CRS) 3.3](https://github.com/coreruleset/coreruleset/releases/tag/v3.3.2) in public preview. For more information, see [Tuning Google Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning).

## April 01, 2022

Feature

Google Cloud Armor now supports TCP Proxy load balancers and SSL proxy load balancers in public preview. For more information, see the [security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types).

## February 07, 2022

Feature

[Google Cloud Armor Rate Limiting](https://docs.cloud.google.com/armor/docs/rate-limiting-overview) is now in General Availability.

## September 30, 2021

Feature

[Google Cloud Armor Adaptive Protection](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview) is now in General Availability.

## August 23, 2021

Feature

Google Cloud Armor now has rate-based throttling and ban rules that enable you to limit requests from clients. These rules help you protect your applications from a large volume of requests that flood your instances and block access for legitimate users.

## August 16, 2021

Feature

Google Cloud Armor integration with reCAPTCHA Enterprise is now available in Public Preview. See the Cloud Armor [bot management overview](https://docs.cloud.google.com/armor/docs/bot-management) and the [Overview of reCAPTCHA Enterprise for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha/docs/integration-overview).

## July 15, 2021

Feature

Google Cloud Armor now supports edge security policies in public preview. Edge security policies enable users to configure filtering and access control policies for content that is stored in cache; this includes endpoints like CDN-enabled backend services and storage buckets.

For more information, see the [public docs](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types).

## June 30, 2021

Feature

Google Cloud Armor now supports parsing of the JSON content of POST bodies when preconfigured WAF rules are evaluated. JSON parsing must be enabled on a per-security-policy basis. In addition, you can enable verbose request logging to provide more details about why a particular rule was triggered. These features are Generally Available.

## April 14, 2021

Change

Managed Protection Plus subscribers are also eligible to receive reactive or proactive DDoS response support from Google's DDoS mitigation experts to help triage and mitigate ongoing attacks, as well as DDoS bill protection to provide credits for some bill spikes caused by increased Google Cloud usage as a result being target by a DDoS attack. 

For more information, see the [public docs](https://docs.cloud.google.com/armor/docs/managed-protection-overview#ddos_response_support).

## March 01, 2021

Feature

Google Cloud Armor [Managed Protection Plus Tier](https://docs.cloud.google.com/armor/docs/managed-protection-overview#standard_tier_versus_plus_tier) is in General Availability. Managed Protection Plus Tier offers a monthly subscription that includes all of the features of Standard Tier, and bundles Google Cloud Armor WAF policy, rules, HTTP request usage, and named IP lists.

## February 19, 2021

Feature

[Google Cloud Armor Adaptive Protection](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview) is available in Public Preview. Adaptive Protection builds machine-learning models that help you protect your Google Cloud applications, websites, and services against L7 distributed denial-of-service (DDoS) attacks.

## December 16, 2020

Change

[Google Cloud Armor Managed Protection Plus tier](https://cloud.google.com/armor/docs/managed-protection-overview) is now available in public preview.

## December 15, 2020

Change

[Third-party named IP address lists](https://cloud.google.com/armor/docs/armor-named-ip) are now in general availability. Note that when Google Cloud Armor Managed Protection Plus tier is in general availability, your ability to use third-party named IP address lists will be affected by which Managed Protection tier your projects are in.

Feature

The following new WAF rules have been added in public preview:

  * Method enforcement
  * Scanner detection
  * Protocol attack
  * PHP injection attack
  * Session fixation



## December 03, 2020

Change

The Google Cloud Armor documentation set has been reorganized. Key updates include:

  * Creation of [_Cloud Armor overview_](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) page
  * Creation of [_Integrating with other Google products_](https://docs.cloud.google.com/armor/docs/integrating-cloud-armor) page
  * Creation of [_Security policies for common use cases_](https://docs.cloud.google.com/armor/docs/common-use-cases) page
  * Reorganization of [_Security policy concepts_](https://docs.cloud.google.com/armor/docs/security-policy-overview) page



## August 31, 2020

Change

Pre-configured rules for local file inclusion (LFI), remote file inclusion (RFI), and remote code execution (RCE) are now in General Availability.

Feature

[Google Cloud Armor Managed Protection Plus Tier](https://cloud.google.com/armor/docs/managed-protection-overview) is in Beta. Managed Protection Plus Tier offers a monthly subscription that includes all of the features of Standard Tier, and bundles Google Cloud Armor WAF policy, rules, HTTP request usage, and named IP lists.

## June 23, 2020

Change

[Promotional pricing](https://cloud.google.com/armor/pricing) for Google Cloud Armor is extended to July 31, 2020.

## May 27, 2020

Change

Error correction: Beta flag removed from feature Google Cloud Armor with Cloud CDN. This feature was released with the status General Availability.

## April 15, 2020

Feature

Google Cloud Armor support for CDN origins and hybrid origins is now available in **General Availability**.

## April 13, 2020

Change

Update to rules language syntax. Adds support for the CEL 'has' macro so that Google Cloud Armor check for absence of a header in the 'request.headers' map.

## March 31, 2020

Feature

[Google Cloud Armor](https://docs.cloud.google.com/armor) [integration with Cloud Security Command Center](https://docs.cloud.google.com/armor/docs/cscc-findings) is generally available.

## March 30, 2020

Change

[Google Cloud Armor](https://cloud.google.com/armor/sla) [Service Level Agreement](https://cloud.google.com/armor/sla) is released.

## March 17, 2020

Feature

Custom rules language, pre-configured WAF rules, and geography-based access controls are now in **General Availability**.

## November 22, 2019

Feature

Custom rules language, pre-configured WAF rules, and geography-based access controls are in public Beta.

## October 24, 2019

Feature

Custom rules language, pre-configured WAF rules, and geography-based access controls are in private Beta.

## June 18, 2019

Change

[Google Cloud Armor is now supported with the Standard Tier of Network Service Tiers](https://docs.cloud.google.com/armor/docs).

## December 06, 2018

Feature

[Google Cloud Armor monitoring](https://docs.cloud.google.com/armor/docs) is available in **GA**.

## December 03, 2018

Feature

[Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs) cannot be attached to backend services that are configured to use the HTTP/2 protocol.

Feature

[Google Cloud Armor deny lists and allow lists](https://docs.cloud.google.com/armor/docs) are available in **GA**.

## March 19, 2018

Feature

[Google Cloud Armor allow lists](https://docs.cloud.google.com/armor/docs) are available in **Beta**.

Feature

[Google Cloud Armor deny lists and allow lists](https://docs.cloud.google.com/armor/docs) are available in **Beta**.

## September 27, 2017

Feature

[Google Cloud Armor deny lists and allow lists](https://docs.cloud.google.com/armor/docs) are available in **Private Beta**.

## May 15, 2017

Feature

[Google Cloud Armor deny lists and allow lists](https://docs.cloud.google.com/armor/docs) are available in **Alpha**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
