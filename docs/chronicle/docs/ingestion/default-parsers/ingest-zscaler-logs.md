---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-zscaler-logs/
title: Zscaler parsers overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:50:50.852712+00:00
---

# Zscaler parsers overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-zscaler-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Zscaler parsers overview 

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document lists the Zscaler parsers that normalizes Zscaler product logs into Google Security Operations Unified Data Model (UDM) fields. It provides a high level overview of each Zscaler product with its use case scenario.

## Configure ingestion of Zscaler logs

To ingest the Zscaler logs to Google SecOps, click the corresponding ingestion mechanism link from the table and follow the instructions provided with each parser.

**Note:** If Zscaler logs are backlogged or delayed during ingestion to Google SecOps, increase the number of workers and the batch size to 1 MB.

## Zscaler products and description

The following table lists the Zscaler parsers that Google SecOps supports. It also lists the corresponding ingestion label for each parser along with their individual product description. You can click the ingestion mechanism link provided with each parser to view the the detailed steps of ingestion mechanism to be followed. To view the mapping reference documentation of the parser, click the corresponding parser name from the table.

Product Name | Ingestion label | Product Description  
---|---|---  
`[Webproxy](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-webproxy-logs#field-mapping)` | `ZSCALER_WEBPROXY` |  Zscaler Webproxy is an advanced web proxy solution built for the cloud. It inspects all traffic at scale (including TLS/SSL) with connections brokered between users and applications based on identity, context, and business policies. It aims to secure data, eliminate vulnerabilities and stop data loss. It acts as an intermediary between the client and the server, provides secure access to resources and protects the server from malware and other threats.   
  
[Zscaler Webproxy Ingestion Mechanism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-webproxy-logs)  
`[Firewall](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-firewall-logs#field-mapping)` | `ZSCALER_FIREWALL` |  Zscaler Firewall is a cloud-based security solution that secures web and non-web traffic. It enhances connectivity and availability by routing traffic through local internet breakout and eliminates the need for VPNs and redundant security appliances. As a Firewall as a service solution, Zscaler handles updates, upgrades, and patches. This leads to cost savings and reduced complexity. It logs every session to ensure comprehensive visibility and access to necessary information.   
  
[Zscaler Firewall Ingestion Mechanism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-firewall-logs)  
`[Admin Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-internet-access-logs#field-mapping)` | `ZSCALER_INTERNET_ACCESS` |  Zscaler Internet Access records every action performed by admins in the ZIA Admin Portal and the actions occurring through Cloud Service APIs. These logs provide insights that enable you to review alterations made to PAC files or URL filtering policies. It helps in tracking changes made by administrators during login sessions and support compliance demonstrations. It can promptly detect and investigate suspicious activities or unauthorized access to the administrative interface. Thus, it ensures the security and integrity of your network.   
  
[Zscaler Internet Access Ingestion Mechanism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-internet-access-logs)  
`[DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-dns-logs#field-mapping)` | `ZSCALER_DNS` |  Zscaler DNS Security and Control services offer mechanisms to take control of your DNS architecture and response. By proxying the DNS request, you can enforce your organization's DNS policies in the Zscaler Zero Trust Exchange (ZTE). When the DNS request reaches the ZTE, the request is open and inspected. No DNS requests can bypass inspection unless you authorize it, as you can restrict your users to only using DNS servers you specify. Zscaler recommends leveraging the ZTR service as your DNS resolver. ZTR instances exist in each of Zscaler 150+ data centers around the world.   
  
[Zscaler DNS Ingestion Mechanism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-dns-logs)  
`[Tunnel](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-tunnel-logs#field-mapping)` | `ZSCALER_TUNNEL` |  The Zscaler service uses a lightweight, HTTP tunnel called the Zscaler Tunnel (Z-Tunnel) to forward traffic to the ZIA Public Service Edges. When a user connects to the web, Zscaler Client Connector establishes the Z-Tunnel to the closest ZIA Public Service Edge, and forwards the web traffic through the tunnel so that the ZIA Public Service Edge can apply the appropriate security and access policies.   
  
[Zscaler Tunnel Ingestion Mechanism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-tunnel-logs)  
`[CASB](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-casb#field-mapping)` | `ZSCALER_CASB` |  The Zscaler multimode cloud access security broker (CASB) secures cloud data in motion (via proxy) and at rest (via APIs). Administrators configure one automated policy that delivers consistent security across all cloud data channels. With Zscaler CASB as part of the comprehensive Zscaler Zero Trust Exchange™ (with SWG, ZTNA, and more), you can avoid point products, reduce IT complexity, and inspect traffic only. Zscaler CASB secures SaaS like Microsoft 365 and Salesforce as well as IaaS offerings like Amazon S3, preventing risky sharing that leads to sensitive data loss or noncompliance.   
  
[Zscaler CASB Ingestion Mechanism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-casb)  
`[VPN](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-vpn-logs#field-mapping)` | `ZSCALER_VPN` |  Zscaler VPN provides users with the fastest and most secure access to private applications and operational technology (OT) devices, while enabling zero trust connectivity for workloads. By dividing the network into smaller segments to isolate potential threats, Zscaler minimizes security risks and the attack surface. Leveraging artificial intelligence, it enforces policies based on the context of a user's or device's activity, ensuring robust security.   
  
[Zscaler VPN Ingestion Mechanism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-vpn-logs)  
`[ZPA](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-zpa-logs#field-mapping)` | `ZSCALER_ZPA` |  Zscaler Private Access (ZPA) establishes an isolated environment around each application, rendering the network and applications invisible to the internet. By doing so, it eliminates VPN security risks and enables IT teams to streamline operations by removing inbound gateway appliances.   
  
[Zscaler ZPA Ingestion Mechanism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-zpa-logs)  
`[DLP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-dlp-logs#field-mapping)` | `ZSCALER_DLP` |  Zscaler Endpoint Data Loss Prevention (DLP) policy is used to protect the organization from data loss on endpoints. Endpoint DLP policy complements Zscaler DLP policy by extending the monitoring of sensitive data to the activities that end users take on endpoints that includes printing, saving to removable storage, saving to network shares, or uploading to personal Cloud Storage accounts. Zscaler custom and predefined DLP engines can be used to detect sensitive data, allow or block user activities, and notify the organization's auditor when a user's activity on an endpoint triggers an Endpoint DLP rule.   
  
[Zscaler DLP Ingestion Mechanism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-dlp-logs)  
`[ZPA Audit](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-zpa-audit-logs#field-mapping)` | `ZSCALER_ZPA_AUDIT` |  Zscaler Private Access (ZPA) establishes an isolated environment around each application, rendering the network and applications invisible to the internet. By doing so, it eliminates VPN security risks and enables IT teams to streamline operations by removing inbound gateway appliances. Zscaler Private Access (ZPA) includes an audit logging feature that records administrative activities within the ZPA Admin Portal. These audit logs capture details such as administrator sign-in and sign-out attempts, configuration changes, and other actions performed by administrators. This enhances security and compliance by providing a detailed record of administrative operations, facilitating monitoring and troubleshooting within the ZPA environment.   
  
[Zscaler ZPA Audit Ingestion Mechanism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-zpa-audit-logs)  
`[ZSCALER_DECEPTION](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-deception-logs#field-mapping)` | `ZSCALER_DECEPTION` |  Zscaler Deception is a deception-based threat detection platform delivered as part of the Zscaler Zero Trust Exchange. This is an integrated capability that uses decoys/honeypots to detect advanced in-network threats that have bypassed existing defenses. Organizations use Zscaler Deception to detect compromised users, stop lateral movement, and defend against human-operated ransomware, customizable keyboard threats, supply chain attacks, and malicious insiders.   
  
[Zscaler Deception Ingestion Mechanism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-deception-logs)  
`[ZSCALER_EMAIL_DLP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-email-dlp#field-mapping)` | `ZSCALER_EMAIL_DLP` |  Zscaler Email DLP lets you monitor and act on sensitive data in outbound email sent to external domains. You can use Zscaler custom and predefined DLP engines to detect sensitive data and to specify DLP actions (i.e., Allow, Block, and Custom Header Insertion) when an email triggers an outbound email policy rule.   
  
[Zscaler Email DLP Ingestion Mechanism](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-email-dlp)  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
