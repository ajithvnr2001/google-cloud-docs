---
url: https://docs.cloud.google.com/sap/docs/secops/overview/
title: Secure SAP applications with Google SecOps \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:33.831892+00:00
---

# Secure SAP applications with Google SecOps  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Secure SAP applications with Google SecOps Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Integrate business-critical SAP telemetry into [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) (SecOps) to help secure your enterprise applications. Google SecOps for SAP closes the visibility gap between SAP environments and security operations, enabling your analysts to detect, investigate, and respond to SAP-specific threats alongside the broader IT landscape.

Integrating SAP infrastructure and application logs into your security operations helps you defend business-critical data against unauthorized access, data exfiltration, and fraud without needing deep SAP technical expertise or custom log pipelines.

To successfully deploy and manage this integration, make sure that you're familiar with the following concepts:

  * **Security operations:** Basic understanding of [security information and event management (SIEM)](https://cloud.google.com/discover/what-is-siem) concepts, [log parsing](https://docs.cloud.google.com/chronicle/docs/event-processing/parsing-overview), and [alert management](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-alert).
  * **Google SecOps concepts:** Understanding of [Unified Data Model (UDM)](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview) and [YARA-L](https://docs.cloud.google.com/chronicle/docs/yara-l/getting-started) syntax is helpful but not required for initial setup.



## Target audience

Google SecOps for SAP is designed for the following personas:

  * **SAP Basis administrators:** Configure SAP log extraction and manage the health of the connection to Google SecOps.
  * **SecOps teams and analysts:** Use Google SecOps to monitor SAP-specific threats alongside the rest of the IT landscape.
  * **Chief Information Security Officer (CISO) and compliance teams:** Monitor enterprise security posture and ensure regulatory compliance through unified visibility.



## Key benefits

Integrating your SAP logs into Google SecOps provides the following benefits:

  * **Unified enterprise-wide visibility:** Gain a centralized view for monitoring threats across your entire IT infrastructure, including on-premises, cloud, and SAP RISE environments.
  * **Business-critical protection:** Defend sensitive data, such as financial records, customer information, and intellectual property, by using Google's comprehensive threat intelligence and curated SAP-specific security detections.
  * **Operational efficiency:** Stop building and maintaining complex, custom log pipelines. Use SAP-specific standard parsers to normalize raw SAP data into the UDM without requiring deep SAP technical expertise.
  * **AI-powered insights:** Use [Gemini in Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/gemini-chronicle) to accelerate threat hunting, summarize complex cases, and automate response workflows with natural language prompts.
  * **Expertise without the overhead:** Help your existing SecOps team [detect and respond to SAP threats](https://docs.cloud.google.com/sap/docs/secops/detect-sap-threats) in near real-time using standard security terminology and playbooks.



## Supported log sources

You can use Google SecOps for SAP to help secure your entire SAP landscape, regardless of where your SAP system is hosted or how your landscape is managed.

### Supported environments

You can monitor SAP systems running in the following environments:

  * **SAP RISE:** Managed SAP landscapes on Google Cloud or other cloud platforms.
  * **Self-managed cloud:** SAP systems you manage on Google Cloud or other cloud platforms.
  * **On-premises:** SAP systems running in your local data centers.



### Supported log types

Google SecOps for SAP includes out-of-the-box ingestion and parsing for critical logs across both infrastructure and application layers:

Log category | SAP log sources  
---|---  
**Infrastructure** | SAP HANA Audit, SAP ICM, SAP Gateway, and SAP Web Dispatcher  
**Application** | SAP Security Audit Logs and SAP Change Documents  
  
For information about how these logs are ingested and the extraction mechanisms used for each environment, see [Plan for log ingestion](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion).

## Integration workflow

The following diagram shows how the integration workflow transitions your SAP logs from the source environment into actionable security insights.

![Google SecOps for SAP integration workflow](https://docs.cloud.google.com/sap/docs/images/secops-sap-workflow.svg)

The integration lifecycle is organized into the following stages:

  1. **Log extraction** : Capture logs from your SAP source and route the data to Google SecOps:

     * **Data capture** : Infrastructure and application logs are gathered from your environment using SAP LogServ, the Application Telemetry Collector, or the Bindplane agent.
     * **Data movement** : Captured logs are then securely transferred to Google SecOps through the Bindplane server or feeds.
  2. **Log ingestion and parsing** : Receive and normalize raw SAP logs within Google SecOps using the standard SAP parsers to prepare the logs for analysis:

     * **Data ingestion** : Logs are received directly by Google SecOps or pulled from storage buckets.
     * **Automated parsing** : Google SecOps uses SAP-specific standard parsers to convert complex logs into the structured UDM format.
  3. **Detect and investigate threats** : Transition from data collection to active security operations and analysis:

     * **Threat detection** : Monitor your SAP landscape using out-of-the-box, curated YARA-L rules designed by Google security experts.
     * **Incident response** : Pivot from alerts to action using standard investigative tools to search UDM logs and trigger automated response playbooks.



## Solution components and pricing

To use Google SecOps for SAP, you combine the core security platform, specialized ingestion components, and curated security content.

  * **Google SecOps** : The central SaaS platform that provides SIEM and SOAR capabilities. Google SecOps serves as the ultimate destination for your SAP logs, featuring built-in log types and parsers that transform raw, complex SAP data into actionable security insights. Google SecOps is available in packages and pricing is based on ingestion. For more information, see the [Google SecOps pricing guide](https://cloud.google.com/security/products/security-operations#pricing) and [Understand your Google SecOps billing components](https://docs.cloud.google.com/chronicle/docs/onboard/understand-billing).

  * **Bindplane (Google Edition)** : Acts as the high-performance ingestion pipeline for transporting logs from self-managed SAP systems and from the Application Telemetry Collector. While [Bindplane (Google Edition)](https://bindplane.com/google) is [included at no additional cost](https://docs.bindplane.com/plans-and-pricing) for Google SecOps customers, you're responsible for the infrastructure costs of the host machines.

  * **Application Telemetry Collector** : A specialized, Docker-based log collector used to extract high-value application security logs, such as Security Audit Logs and Change Documents. Google provides the collector image at no cost. You're responsible for the infrastructure costs where the collector is hosted, as well as any associated Google Cloud service costs.

  * **Google Cloud services** : Depending on your ingestion path, you're responsible for the costs of Google Cloud services that you use:

    * **Cloud Storage** : Stores logs from SAP LogServ and hosts dependencies for the Application Telemetry Collector. For information about pricing, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).
    * **Pub/Sub** : Required for SAP RISE environments to provide the notification mechanism for near real-time ingestion. For information about pricing, see [Pub/Sub pricing](https://docs.cloud.google.com/pubsub/pricing).
    * **Secret Manager** : Securely stores SAP service user credentials for the Application Telemetry Collector. For information about pricing, see [Secret Manager pricing](https://docs.cloud.google.com/secret-manager/pricing).
  * **SAP RISE (LogServ)** : Provides streamlined access to infrastructure logs for customers in SAP RISE environments. SAP manages this service, which delivers logs to a storage bucket and uses an event-driven notification mechanism, such as Pub/Sub, to achieve near real-time ingestion with minimal latency. To use LogServ and understand its pricing, contact your SAP account representative.

  * **SAP Content Reference** : An open-source collection of sample YARA-L rules designed to help your team [identify threats within your SAP logs](https://docs.cloud.google.com/sap/docs/secops/detect-sap-threats) using Google's deep security expertise.




## Get support

For issues related to Google SecOps for SAP, [contact Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support). Our team provides assistance or guides you to the right resource to help ensure a timely resolution.

For issues involving SAP systems or the LogServ service, contact SAP support. For issues related to other third-party products, such as Bindplane, contact the appropriate third-party vendor for assistance.

Get technical answers and peer support in the [Google SecOps Community](https://security.googlecloudcommunity.com/google-security-operations-2).

## What's next

  * [Plan for log ingestion](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
