---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-hana-audit/
title: Collect SAP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:31.256607+00:00
---

# Collect SAP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-hana-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SAP logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

Google SecOps supports the ingestion and normalization of business-critical telemetry from your SAP landscape. Whether your landscape is managed by SAP (SAP RISE) or self-managed (on-premises or any cloud), you can collect the following logs to monitor for security events:

  * **Infrastructure logs** : Capture events from the operating system and database layers, such as SAP HANA Audit, ICM, and Gateway logs.
  * **Application logs** : Capture security-relevant business events directly from the SAP application layer, such as Security Audit Logs and Change Documents.



To ingest these logs, Google SecOps uses a combination of ingestion mechanisms:

  * **SAP LogServ** : In SAP RISE environments, pulls infrastructure logs from cloud-based storage.
  * **Application Telemetry Collector** : A containerized application that extracts application logs using the Remote Function Call (RFC) protocol.
  * **Bindplane** : A log management platform that provides agents for host log collection and a centralized server for log forwarding and normalization.



For more information about Google SecOps for SAP, see [Secure SAP applications with Google SecOps](https://docs.cloud.google.com/sap/docs/secops/overview).

## Before you begin

Before you start the ingestion process, review the following guides:

  * [Plan for log ingestion](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion): Select an ingestion path and verify technical requirements.

  * [Prepare your environment for log ingestion](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion): Configure Google Cloud resources and SAP systems.




## Log ingestion overview

To ingest SAP logs, first determine the architecture of your SAP environment. The ingestion path depends on whether your environment is managed by SAP (RISE) or self-managed.

### SAP RISE ingestion path

Use this path if your SAP landscape is managed under the SAP RISE program. In an SAP RISE environment, the ingestion path involves the following:

  * **Infrastructure logs** : SAP LogServ writes logs to cloud-based storage. Google SecOps pulls these logs through feeds.

  * **Application logs** : The Application Telemetry Collector extracts logs using the RFC protocol and forwards them through a Bindplane server to Google SecOps.




For more information, see [Set up log ingestion for SAP RISE](https://docs.cloud.google.com/sap/docs/secops/ingest-sap-rise-logs).

### Self-managed ingestion path

Use this path if you manage your own SAP landscape in an on-premises environment or in the cloud. For self-managed environments, the ingestion path involves the following:

  * **Infrastructure logs** : Bindplane agents installed on your SAP hosts tail the log files and forward them through a central Bindplane server to Google SecOps.

  * **Application logs** : A central Application Telemetry Collector connects to your SAP instances to extract logs and forwards them through the Bindplane server to Google SecOps.




For more information, see [Set up log ingestion for self-managed SAP systems](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs).

## Supported log types

The following table lists the SAP log sources that Google SecOps supports and their corresponding log types:

Category | SAP log source | Google SecOps log type  
---|---|---  
**Infrastructure** | SAP ICM Logs | `SAP_ICM`  
SAP Gateway Logs | `SAP_GATEWAY`  
SAP Web Dispatcher Logs | `SAP_WEBDISP`  
SAP HANA Audit Logs | `SAP_HANA_AUDIT`  
**Application** | Change Document Logs | `SAP_CHANGE_DOCUMENT`  
Security Audit Logs | `SAP_SECURITY_AUDIT`  
  
## UDM field mappings

Google SecOps normalizes incoming SAP logs into the Unified Data Model (UDM) so that you can search for data and run detections. For a detailed field-by-field reference of how SAP data maps to UDM fields, see [UDM mapping for SAP logs](https://docs.cloud.google.com/sap/docs/secops/udm-mapping-overview).

## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-hana-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
