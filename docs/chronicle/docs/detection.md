---
url: https://docs.cloud.google.com/chronicle/docs/detection/
title: Threat Intelligence overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:47.531670+00:00
---

# Threat Intelligence overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Threat Intelligence overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Google Threat Intelligence provides a comprehensive and proactive approach to identifying, analyzing, and mitigating security threats. It uses Google's vast infrastructure, global telemetry, and advanced analytics to deliver useful insights and improve your organization's security. 

Google Threat Intelligence includes threat detection, analysis of malware and phishing campaigns, real-time threat alerts, and intelligence feeds that integrate seamlessly with security tools such as Security Information and Event Management (SIEM) and Security Orchestration, Automation, and Response (SOAR) platforms.

You can integrate and use Google Threat Intelligence within Google SecOps using the following integration methods:

### Applied Threat Intelligence (ATI)

This fully managed, native pipeline automatically curates and applies Google's threat intelligence.

  * **License** : 
    * Google SecOps Enterprise+
  * **Features** : 
    * Provides advanced automated threat intelligence capabilities.
    * Includes a fully built-in and managed integration that automatically uses the complete spectrum of Google, Mandiant, and VirusTotal intelligence to provide automated context, enrichment, and alerting without manual pipeline configuration.
    * Combines frontline expertise with the breadth of Google's visibility to deliver a unified view of the threat landscape.
    * Lets security teams contextualize alerts, understand threat actor tactics, and use intelligence directly within their workflows.
  * **Integration steps** : See [Applied Threat Intelligence overview](https://docs.cloud.google.com/chronicle/docs/detection/applied-threat-intel-overview).



### Bring your own license (BYOL) Google Threat Intelligence integration

This customer-deployed pipeline ingests licensed Google Threat Intelligence (GTI) data (Threat Lists, IoC Streams, and adversary context) into Google SecOps. This method lets you deploy and manage resources (such as Cloud Run functions, Cloud Scheduler, Secret Manager) in your Google SecOps environment to fetch data from the Chronicle API and stream it to Google SecOps.

  * **License** : 
    * Google SecOps Standard or Enterprise. 
    * An active Google Threat Intelligence license to use the Bring Your Own License (BYOL) integration.
    * The Enterprise+ license includes permissions for the BYOL integration.
  * **Features** : 
    * Lets you use a customer-deployed pipeline to ingest your data into Google SecOps for enhanced detection and threat hunting.
    * Replaces legacy fragmented connectors with a single, unified solution.
  * **Integration steps** : See [BYOL Threat Intelligence integration](https://docs.cloud.google.com/chronicle/docs/detection/gti-byol).



### Integrate your own threat intelligence feeds

This integration method lets you ingest custom or third-party Indicators of Compromise (IoCs) and threat intelligence feeds (such as MISP, STIX/TAXII, commercial threat intelligence providers, or custom CSV and JSON lists) directly into Google SecOps. Google SecOps parses incoming feeds into the Unified Data Model (UDM) Entity Context Graph (ECG) to support automated IoC matching against event telemetry, retrohunting across up to 30 days of data, and custom YARA-L rule detections.

  * **License** : 
    * Available across Google SecOps license tiers.
  * **Features** : 
    * Ingests third-party threat feeds using native Google SecOps feeds (such as Cloud Storage, HTTPS, Amazon S3, STIX/TAXII, and MISP).
    * Normalizes threat indicators and contextual metadata directly into UDM entity records (such as `DOMAIN_NAME`, `IP_ADDRESS`, `FILE`, and `URL`) with interval validity windows.
    * Correlates incoming telemetry against your custom threat intelligence feeds in near-real time and retroactively.
    * Supports threat detection through automatic IoC matching and custom YARA-L correlation rules.
  * **Integration steps** : See [Integrate your own threat intelligence feeds](https://docs.cloud.google.com/chronicle/docs/detection/integrate-threat-intel-feeds).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
