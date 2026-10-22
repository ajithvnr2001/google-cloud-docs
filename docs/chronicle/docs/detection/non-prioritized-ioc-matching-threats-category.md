---
url: https://docs.cloud.google.com/chronicle/docs/detection/non-prioritized-ioc-matching-threats-category/
title: Non-prioritized IoC Matching threats \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:46.701510+00:00
---

# Non-prioritized IoC Matching threats  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/non-prioritized-ioc-matching-threats-category/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Non-prioritized IoC Matching threats

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document outlines the expansion of curated detections through the integration of Google's Indicators of Compromise (IoC) feeds. These rule sets build on curated threat intelligence to identify malicious activities within Google Security Operations environments, specifically focusing on threats identifiable through high-fidelity indicators like IPs, domains, and file hashes.

For Google SecOps Enterprise Plus customers, rule sets in this category are enabled by default. The status is set to **Enabled** for both Precise and Broad rules to support producer and composite detections and populate IOC metadata. However, these rules are not designed to generate noise in your alert queue. Consequently, Alerting is set to **Off** by default. This allows the system to match high-volume curated IoCs from Google's feeds and support deeper correlation without generating alert fatigue.

If you customize these settings, Google recommends keeping Alerting set to **Off** for this category.

The non-prioritized IoC Matching rules category provides comprehensive coverage for threats often missed by standard managed content, including cryptomining, Command and Control (C2) communications, and the use of malicious anonymization services. The [Applied Threat Intelligence curated detections](https://docs.cloud.google.com/chronicle/docs/detection/ati-curated-detections) are Mandiant-based and use prioritization logic for alerts (`Active Breach` or `High` designations), while the non-prioritized IoC Matching category focuses on matching a high volume of curated IoCs from Google's feeds to exclusively identify specific threat activities.

**Note:** These rules are available for **Google SecOps Enterprise Plus** customers only.

## Rule set descriptions

The **Applied Threat Intelligence - Non-prioritized IOC Matching** category includes the following rule sets:

  * Applied Threat Intelligence - Non-prioritized Domain IOC Matching
  * Applied Threat Intelligence - Non-prioritized File IOC Matching
  * Applied Threat Intelligence - Non-prioritized IP IOC Matching
  * Applied Threat Intelligence - Curated Composites



These rule sets contain logic designed to detect direct hits against specific Google IoC feeds. They function as producer rules that tag security-relevant events and populate metadata for deeper correlation, rather than generating direct alerts.

## Understand Non-prioritized IoC Matching identification rules

These rules utilize direct matching against Google's IoC Feeds to tag security-relevant events. They are designed to function as the identification layer of the detection funnel, providing high-confidence indicators of malicious infrastructure or tools.

### Supported Indicators and Log types

The rules rely on Google SecOps Unified Data Model (UDM) records, which normalize various log sources to match against the following feed types:

Indicator Category | Feed Examples | Supported Log Types  
---|---|---  
**Network Infrastructure** | C2 IPs, C2 Egress IPs,, Malicious Proxy/VPN IPs, Tor Exit Nodes | Cloud Audit Logs, Network Proxy Logs, Firewall Logs  
**Host/Endpoint Indicators** | Malicious Linux Binaries, Crypto mining Hashes, RMM Tool Samples | EDR Logs, Process Launch Events  
**Domain Indicators** | C2 Domains, Crypto mining Domains | DNS Logs, Web Proxy Logs  
  
## Modify rules in a rule set

Following the standard Mandiant Hunt configuration, you can adjust how IoC Matching rules operate within your environment:

  * **Broad:** Detects any potentially malicious feed hit. While providing maximum visibility, this may increase detection volume for common indicators like VPN or Proxy IPs. Also, it is advisable not to enable alerting for these broad rules while keeping the detection on.
  * **Precise:** Focuses on the highest-confidence behavioral clusters to minimize noise.



To modify settings, use the Google SecOps rules list to toggle the Status (Enabled/Disabled) and Alerting (On/Off) for each rule.

## Tune alerts from rule sets

Use [rule exclusions](https://docs.cloud.google.com/chronicle/docs/detection/rule-exclusions) to prevent specific authorized internal tools or known-good traffic from triggering ATI-based alerts. This helps you maintain a high signal-to-noise ratio and is particularly useful for excluding authorized use of administrative tools that might otherwise be flagged by RMM tool feeds.

For examples of custom YARA-L rules using IoC feeds, see [IP address matching against indicators of compromise](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples#ioc-ip-matching).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
