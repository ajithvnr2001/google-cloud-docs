---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/log-ingestion-and-parsing/
title: Ingest and parse log data \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:16.485868+00:00
---

# Ingest and parse log data  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/log-ingestion-and-parsing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Ingest and parse log data

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide helps security engineers efficiently ingest and parse log data using Google Security Operations. It explains how to consolidate logs from various sources, including multi-cloud, on-premises, and SaaS environments, normalize them into the Unified Data Model (UDM), and make them available for real-time threat detection and analysis. By following these methods, you can improve visibility across your environments, reduce operational latency, and ensure data is consistently formatted for searching and examination, ultimately enhancing your security posture.

## Common use cases

The following use cases highlight how Google SecOps log ingestion and parsing capabilities can enhance your security operations.

### Consolidate fragmented data

  * **Objective** : Bring logs from all your security tools and environments (multi-cloud, on-premises, SaaS) into a single platform.
  * **Value** : Enables centralized analysis and visibility, breaking down data silos.



### Ensure schema consistency

  * **Objective** : Automatically normalize diverse log formats into the UDM.
  * **Value** : Enables consistent searching and rule application across all data sources. For example, a failed login event from AWS will have the same UDM structure as one from an on-premises Windows server.



### Reduce operational latency

  * **Objective** : Utilize direct ingestion methods for real-time data flow.
  * **Value** : Minimizes the time from event occurrence to detection and response.



## Key terminology

  * [UDM](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview): A standardized schema that Google SecOps uses to normalize log data from various sources. This allows for consistent analysis and threat detection across different log types and vendors.



## Before you begin

  * **Permissions** : Make sure you have the necessary Identity and Access Management (IAM) roles:

    * `roles/chroniclesm.admin`: Typically required at the organization level for multi-project ingestion.
    * `roles/securitycenter.adminEditor`: For configurations using SCC-E. 

For more information, see [Grant a single IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

  * Google SecOps requires [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) (Standard or Premium) for asset metadata ingestion.

  * **Allowlisting** : Set up allowlisting if you use _data feeds_ (pull ingress) or an _Ingestion API_ method (push egress):

    * **V2 feeds (S3_V2, SQS_V2, Azure_Blobstore_V2)** : Require `storage-transfer-service/ipranges.json`. For more information, see [IP allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip-allowlists).
    * **Third-party APIs** : Require `goog.json` and `cloud.json`. For more information, see [IP allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip-allowlists).
    * **Legacy feeds (S3, Azure_Blobstore)** : Require dedicated static pools. For more information, contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support).
    * **Azure Event Hub** : Requires regional IPDB listings. For more information, see [Configure network security (optional) in _Create an Azure Event Hub feed_](https://docs.cloud.google.com/chronicle/docs/administration/create-azure-feed#network-security).
    * **Push ingestion using Ingestion methods in the Chronicle API** : For more information, see [Set up domain allowlisting](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods#allowlist-for-ingest-api).
    * **Push ingestion using the Backstory Ingestion API** : For more information, see [Set up domain allowlisting](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#allowlist-for-ingest-api).



## Configure log ingestion and parsing

  1. Choose the ingestion method based on your log sources. The primary methods are [Direct Ingestion for Google Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs), the [Bindplane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent) for on-premises or pre-processing needs, and [Data Feeds](https://docs.cloud.google.com/chronicle/docs/administration/feed-management) for cloud-to-cloud or API integrations. For more information, see Selecting an ingestion method.
  2. [Apply exclusion filters](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline) to reduce log volume and cost. For example, exclude high-volume, low-value operations.
  3. Use the [Health Hub dashboard](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard) in the Google SecOps console to track ingestion rates, check for errors (`Anomalous Sources`), and identify parser issues.



### Select an ingestion method

  * **Direct ingestion (Google Cloud):** This is the most common ingestion method for Google Cloud telemetry. It uses Cloud Logging filters to forward logs directly to Google SecOps.

    * **Supported types:** Cloud Audit Logs, Cloud DNS, Cloud NAT, Cloud Next Generation Firewall, Cloud IDS, Cloud Load Balancing, and more. For more information, see [Ingest Google Cloud data to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs).
    * **Enablement:**
      * Go to the **Google SecOps Ingestion Settings** in the Google Cloud console.
      * Click the **Sending data to Google Secops** toggle.
      * Configure Logging sinks and filters as needed.
  * **Bindplane agent:** Use Bindplane for on-premises servers (Windows or Linux) or to filter or transform cloud data before it reaches Google SecOps.

    * **Editions:**
      * **Google edition:** All customers receive this edition.
      * **Enterprise edition:** Offers advanced filtering, PII masking, and more.
    * **Architecture:** Can run in _Gateway mode_ , where multiple collectors forward logs to a central Bindplane gateway, simplifying firewall rules and offloading processing.
    * **Enablement:** Install the agent using the shell or PowerShell scripts that the Google SecOps console provides. For more information, see [Use Bindplane with Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent).
  * **Data feeds:** Use Data Feeds for cloud-to-cloud ingestion from object stores or third-party APIs.

    * **Supported sources:** Includes Azure Event Hub, Amazon S3, Azure Blob Storage, Google Cloud Storage, Microsoft 365, CrowdStrike Falcon, and ~50 others. For more information, see [Source Types](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#source-types)
    * **Security:** Google Cloud Secret Manager securely stores credentials for data feeds.
    * **Enablement:** Configure feeds through the Google SecOps console, providing the necessary credentials and source details. For more information, see [Feed management documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management).
  * **Other methods**

    * Direct ingestion of [Google Workspace events](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-workspace-logs).
    * [Chrome Browser Cloud Management telemetry](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chrome-management).
    * Direct API integration (for example, Nozomi) using the [Chronicle API ingestion methods](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods). For information on migrating from the legacy Ingestion API, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

For details on these methods, refer to the specific documentation for each integration.




## Troubleshooting

This section helps you diagnose and resolve common issues with log ingestion and parsing.

### Latency, service quota, and limits

  * **Ingestion delays:** Large files (exceeding 5-10 GB) can cause ingestion delays. Split these files to avoid delays.
  * **Encoding:** Google SecOps only supports UTF-8 encoding for ingested logs.
  * **Google Cloud direct ingestion:** Google SecOps does not support custom Namespace or Label assignment during ingestion.
  * **Data feed log line size:** Google SecOps limits individual log lines within data feeds to 4 MB.
  * **Burst limits:** If ingestion rates exceed tenant burst limits, you might see a **Threshold reached** status. If this happens, refine export filters or contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support) for potential quota increases.
  * **UDM events:** If a batch UDM event exceeds 8.2 MB, all UDM events are dropped. If a single UDM event exceeds 500 KB, the UDM event is dropped.



### Error remediation

Symptom | Potential cause | Fix  
---|---|---  
Missing identity relationships | Context ingestion is desynchronized. | To force a context refresh, disable and then re-enable direct Google Cloud ingestion.  
Threshold reached status | Ingestion rate exceeds tenant burst limits. | Refine export filters to exclude less critical logs. Contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support) to request a quota increase, if necessary.  
Bindplane agent won't connect | Your firewall is blocking required ports or endpoints. | Ensure that firewall rules allow egress to `malachiteingestion-pa.googleapis.com` on port `443`. If you use Gateway Mode, ensure that your firewall allows internal traffic on port `3001` (default).  
Parser errors | The log format changed, or you applied an incorrect parser. | Review logs in [Health Hub](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard). Check if the default parser is appropriate, or if you need a custom parser. Validate that the log format meets parser expectations.  
  
### Validation and testing

  * Use the [Health Hub dashboard](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard) in the Google SecOps console to monitor ingestion rates, check for errors ("Anomalous Sources"), and identify parser issues. Health Hub is the primary tool to validate that data is flowing correctly and that Google SecOps parses it as expected.
  * Use [UDM Search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) in Google SecOps to query for ingested logs and ensure that they are present and Google SecOps normalizes them correctly.



## Support

  * For Bindplane on-premises servers issues, contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support).
  * For Bindplane Cloud issues, contact [Bindplane support](https://bindplane.com/support) directly.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
