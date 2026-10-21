---
url: https://docs.cloud.google.com/chronicle/docs/detection/gti-byol/
title: Integrate BYOL Threat Intelligence \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:12:00.325831+00:00
---

# Integrate BYOL Threat Intelligence  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/gti-byol/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate BYOL Threat Intelligence

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Integrate your licensed Google Threat Intelligence (GTI) data directly into Google SecOps using the Bring Your Own License (BYOL) integration. Ingest threat lists, IoC streams, and adversary context to enhance your threat detection and hunting capabilities.

The Google Threat Intelligence BYOL integration ingests your threat intelligence data into Google SecOps and normalizes it into Unified Data Model (UDM) format. Google SecOps correlates this threat telemetry with your security events, immediately improving your threat hunting and detection.

### Availability

This integration is available to **Google SecOps Standard** and **Enterprise** customers who have an active Google Threat Intelligence license.

  * **Standard and Enterprise:** This integration provides a customer-deployed pipeline to bring Google Threat Intelligence data into your Google SecOps environment. You can use this data for custom hunting or to enable prebuilt curated detection rules.
  * **Enterprise+:** Enterprise+ customers already benefit from [Applied Threat Intelligence (ATI)](https://docs.cloud.google.com/chronicle/docs/detection/applied-threat-intel-overview), a fully managed, built-in pipeline that automatically curates and applies Google's threat intelligence. While this BYOL integration is compatible with Enterprise+, the ATI service is the recommended solution.



## Key capabilities

  * **Unified data ingestion:** Ingests GTI threat lists (categorized IoCs) and IoC stream data, providing near real-time updates for file hashes, IPs, URLs, and domains.
  * **UDM normalization:** Automatically parses data into the [Unified Data Model (UDM)](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview) under the log type `GCP_THREATINTEL`, making it instantly searchable and ready for correlation rules.
  * **Adversary context:** Ingests associations for malware, threat actors, campaigns, and reports, including MITRE ATT&CK mappings.
  * **Pre-built dashboards:** Includes out-of-the-box [dashboards](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards) for visualizing threat lists, adversary intelligence, and [IoC streams](https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page).
  * **Curated detection rules:** Leverage prebuilt Google SecOps Curated Rules to automatically evaluate your security telemetry against ingested Google Threat Intelligence Indicators of Compromise (IoCs).



## Prerequisites

Before you set up the integration, ensure you have the following:

  * A valid and active Google Threat Intelligence license (BYOL), to access the GTI API.
  * Access to a Google Cloud project to deploy the necessary resources (Cloud Run functions, Cloud Scheduler, Secret Manager).
  * Access to your Google SecOps instance.



## Deployment

This integration is a customer-deployed solution that uses Google Cloud resources to fetch data from the GTI API and stream it to Google SecOps.

Follow the instructions and user guide to run the deployment scripts and configure the Google Threat Intelligence integration. For details, see the official GitHub repository readme file: [Google Threat Intelligence ingestion scripts on GitHub](https://github.com/chronicle/ingestion-scripts/tree/main/google_threat_intelligence)

Once deployed, the BYOL ingestion process is triggered by a Cloud Scheduler job, which activates a Cloud Function to securely fetch API credentials from Secret Manager. The function then queries the external GTI API for the latest threat data, streams it to the Chronicle API, and a default parser transforms (normalizes) the raw data into UDM entities.

## Detect threats with Curated Rules

Once the integration is deployed and data is normalized under the `GCP_THREATINTEL` log type, you can enable prebuilt detection rules specifically designed for this integration.

To use these rules:

  1. In Google SecOps, navigate to **Curated Detections**.
  2. Locate the Google Threat Intelligence (BYOL) rule set under the **Third-party vendor alerts** category.
  3. Enable the rule set to start generating detections based on matches between your telemetry and the ingested Google Threat Intelligence IoCs, such as malicious IPs, domains, or file hashes.



## Dashboards

Google Threat Intelligence gives you the visibility needed to understand and anticipate threat actor tactics and protect your organization against emerging threats. Use the following dashboards to visualize the ingested data:

  * **Threat lists dashboard** : Focuses on detection and blocking, showing IoC counts by severity and entity type.
  * **Adversary intelligence dashboard** : Focuses on context and lets you drill down into malware families, threat actors, and campaigns.
  * **Google Threat Intelligence dashboard** : Provides a real-time overview of the IoC stream, including severity distribution and geographical breakdown.



## Unified workflow: SIEM and SOAR

The BYOL integration combines SIEM's detection and hunting capabilities with [SOAR's Google Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-threat-intelligence) features in a closed-loop security workflow.

SIEM helps you _find_ threats, and SOAR lets you _respond_ to them. The following scenarios illustrate how these capabilities work together:

  1. **Enriched investigation (SIEM to SOAR):**
     * **Action:** An analyst identifies a suspicious domain in Google SecOps SIEM using the ingested GTI data.
     * **Response:** They trigger a SOAR search action to query GTI for deep context on that domain (for example, associated threat actors, passive DNS) without leaving the investigation flow.
  2. **Advanced artifact analysis (SIEM to SOAR):**
     * **Action:** During an investigation in Google SecOps SIEM, an analyst encounters a suspicious file hash or URL that lacks definitive reputation data.
     * **Response:** Using the SOAR integration, the analyst triggers an action to _privately submit_ the URL or file to Google Threat Intelligence for advanced analysis. This performs deep scanning and sandbox detonations to determine maliciousness, while keeping the submission private and not sharing it with the broader community immediately.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
