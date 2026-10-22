---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/release-notes/
title: Google SecOps Response Integrations release notes \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:25.356990+00:00
---

# Google SecOps Response Integrations release notes  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Support ](https://docs.cloud.google.com/chronicle/docs/secops/release-notes)



Send feedback 

#  Google SecOps Response Integrations release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Google SecOps Response Integrations. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/chronicle-soar-marketplace-release-notes.xml) directly. 

## October 14, 2026

Change

**SentinelOneV2** : Version 52.0

  * Fixed an issue to properly handle merged cases during threat synchronization in the following job:

    * **SentinelOne V2 - Sync Threats Job**



Change

**Microsoft Graph Mail Delegated** : Version 26.0

  * Updated the **Folder Name** parameter to be optional, allowing searches across the entire mailbox when no folder is specified in the following action:

    * **Search Emails**
  * Improved S/MIME processing to support multi-layered encrypted, clear-signed, and opaque-signed messages, and resolved an issue where the **Bypass Signature Verification** parameter didn't bypass verification for malformed or unsupported S/MIME signatures in the following connector:

    * **Microsoft Graph Mail Delegated Connector**



Change

**Okta** : Version 18.0

  * Fixed a pagination issue to retrieve all available roles and user groups in the following actions:

    * **List Roles**

    * **List User Groups**




Change

**Google Threat Intelligence** : Version 21.0

  * Improved issue ingestion to adaptively scan the configured `Max Hours Backwards` time range and skip periods without new issues in the following connector:

    * **Google Threat Intelligence - ASM Issues Connector**
  * Added the **Anonymize Credential** parameter to optionally mask compromised passwords with asterisks in ingested alerts and events in the following connector:

    * **Google Threat Intelligence - DTM Alerts Connector**



Change

**Email Utilities** : Version 17.0

  * Resolved an issue causing entities to not be created when `Create Observed Entities` was configured for specific entity types in the following action:

    * **Parse Case Wall Email**



Change

**Microsoft Graph Mail** : Version 49.0

  * Updated the **Folder Name** parameter to be optional, allowing searches across the entire mailbox when no folder is specified in the following action:

    * **Search Emails**
  * Improved S/MIME processing to support multi-layered encrypted, clear-signed, and opaque-signed messages, and resolved an issue where the **Bypass Signature Verification** parameter didn't bypass verification for malformed or unsupported S/MIME signatures in the following connector:

    * **Microsoft Graph Mail Connector**



Change

**Splunk** : Version 68.0

  * Added the **Alert Start Time Field** parameter to specify a custom field for determining the alert start time in the following connector:

    * **Splunk Query Connector**



Change

**Google Chronicle** : Version 98.0

  * Added the **Use Cache** and **Cache TTL** parameters to enable caching of data table responses in the following actions:

    * **Get Data Tables**

    * **Is Value In Data Table**

    * **Is Value In Data Table Async**

  * Fixed an issue where environment extraction only checked the first event in multi-event alerts in the following connector:

    * **Chronicle Alerts Connector**



## October 07, 2026

Change

**Google Chronicle** : Version 97.0

  * Updated the alert synchronization logic in the following job:

    * **Google Chronicle Sync Job**



Change

**Gitsync** : Version 53.0

  * (REGRESSIVE) **Integration** : Updated to support the latest Chronicle API.

**Important:** Existing users **must** migrate their repository branch and re-export their content after updating. 

For instructions, see [Chronicle API-enabled environment migration](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/gitsync#chronicle-api-enabled-environment-migration).




## September 30, 2026

Feature

**Akeyless Security** : Version 1.0

  * New **Akeyless Security** integration.



Change

**Vertex AI** : Version 9.0

  * **Integration** : Improved API error message parsing.



Change

**Microsoft Graph Mail** : Version 48.0

  * Added support for message timezone in the following action:

    * **Send Thread Reply**



Change

**Cyberint** : Version 8.0

  * Added the **Disable Overflow** parameter to the following connector:

    * **Cyberint - Alerts Connector**



Change

**Illusive Networks** : Version 11.0

  * Fixed the endpoint for retrieving forensic data in the following action:

    * **Run Forensic Scan**



Change

**Microsoft 365 Defender** : Version 33.0

  * Improved the case priority parsing mechanism to support protobuf format on remote agents and updated comment syncing logic to support multi-line closure comments in the following job:

    * **Sync Alerts**



Change

**CrowdStrike Falcon** : Version 83.0

  * Updated comment syncing logic to support multi-line closure comments and sync comments from closed CrowdStrike alerts in the following action:

    * **Sync Alerts**



Change

**Microsoft Graph Mail Delegated** : Version 25.0

  * Added support for message timezone in the following action:

    * **Send Thread Reply**



Change

**Jira** : Version 62.0

  * Improved context properties processing logic in the following action:

    * **Create Issue**



Change

**Google Chronicle** : Version 96.0

  * **Integration** : Removed dummy network socket initialization during multipart response parsing and updated the default API root to point to the Chronicle API.



Change

**SentinelOne Singularity Operations Center** : Version 2.0

  * Updated event processing logic and ontology mapping in the following connector:

    * **SentinelOne Singularity Operations Center - Unified Alerts Connector**



## September 16, 2026

Feature

**CyberArk PAM** : Version 13.0

  * The following new job has been added:

    * **Sync Integration Credentials Job**



Feature

**Siemplify** : Version 113.0

  * The following new action has been added:

    * **Attach Playbook to Case**



Change

**Microsoft 365 Defender** : Version 32.0

  * Improved the rate limit handling and timestamp updating mechanism in the following connector:

    * **Microsoft 365 Defender - Incidents Connector**
  * Added the `Sync Direction` and `Closed Reason Mapping` parameters for configurable sync direction and improved comment payload handling to skip empty and whitespace comments in the following job:

    * **Sync Alerts**



Change

**Microsoft Graph Mail** : Version 47.0

  * Added support for S/MIME digital signing and encryption in the following action:

    * **Send Email**
  * Added support for HTML URL extraction, attachment exclusions, event field exclusions, and S/MIME signature verification bypass in the following connector:

    * **Microsoft Graph Mail Connector**



Change

**Palo Alto Cortex XDR** : Version 33.0

  * Added the `Unzip File` parameter and improved error handling for failed retrievals in the following action:

    * **Download File**



Change

**Microsoft Graph Mail Delegated** : Version 24.0

  * Added support for S/MIME digital signing and encryption in the following action:

    * **Send Email**
  * Added support for HTML URL extraction, attachment exclusions, event field exclusions, and S/MIME signature verification bypass in the following connector:

    * **Microsoft Graph Mail Delegated Connector**



Change

**CrowdStrike Falcon** : Version 82.0

  * Updated the polling logic to prevent host containment flapping in the following actions:

    * **Contain Endpoint**

    * **Lift Contained Endpoint**




Change

**Microsoft Graph Security** : Version 29.0

  * **Integration** : Added support for Microsoft Sovereign / GCC High environments by adding Login API Root and API Root parameters.



## September 09, 2026

Feature

**Google Chronicle** : Version 95.0

  * The following new action has been added:

    * **Is Value In Data Table Async**



Change

**Microsoft 365 Defender** : Version 31.0

  * Updated alert tracking logic, extracted alert object metadata, and improved the pagination and timeout handling mechanism in the following connector:

    * **Microsoft 365 Defender - Incidents Connector**



Change

**Google Chronicle** : Version 95.0

  * **Integration** : Improved OAuth 2.0/JWT authentication logging, validation diagnostics, and error messaging.



Change

**Trend Vision One** : Version 12.0

  * Made the `Description` parameter mandatory in the following actions:

    * **Isolate Endpoint**

    * **Unisolate Endpoint**




## September 04, 2026

Change

**Google Chronicle** : Version 94.0

  * Reverted the execution mode to synchronous in the following action:

    * **Is Value in Data Table**



## September 03, 2026

Feature

**Google Chronicle** : Version 93.0

  * Added the following new action:

    * **Execute UDM Query Async**



Change

**ServiceNow** : Version 72.0

  * Added the ability to authenticate using client credentials without a refresh token to the following connector:

    * **Sync Incidents**



Change

**FireEye ETP** : Version 11.0

  * Updated ontology mapping rules and fixed missing alert details and event data for v2 API issue in the following connector:

    * **FireEye ETP - Email Alerts Connector**



## August 26, 2026

Feature

**FireEye HX** : Version 26.0

  * Added the following new actions: 
    * **Get File**
    * **Check Containment Status**
  * Added the **Agent Id** input parameter to the following actions: 
    * **Contain Host**
    * **Cancel Host Contain**



Feature

**Proofpoint Email Protection** : Version 11.0

  * Added the following new actions: 
    * **Forward Quarantined Email**
    * **Release Quarantined Email**



Feature

**Wiz** : Version 10.0

  * Added the **Authentication URL** parameter to support Gov (FedRAMP) and custom environments.
  * Added the following new job: 
    * **Wiz and Google SecOps Bi-directional Sync Job**



Change

**Microsoft Graph Mail** : Version 46.0

  * Updated parameters and filtering options in the following actions: 
    * **Wait For Email From User**
    * **Search Emails**



Change

**Microsoft Graph Mail Delegated** : Version 23.0

  * Updated parameters and filtering options in the following actions: 
    * **Wait For Email From User**
    * **Search Emails**



Change

**ServiceNow** : Version 71.0

  * Added support for OAuth authentication in the following job: 
    * **Sync Incidents Job**



## August 19, 2026

Feature

**Wiz** : Version 9.0

  * Added the following new job:

    * **Wiz and Google SecOps Bi-directional Sync Job**



Change

**Exchange** : Version 125.0

  * Updated the parsing logic for nested S/MIME email attachments (`.eml`) sent from macOS and Windows in the following connector:

    * **Exchange Mail Connector v2 with Oauth Authentication**



Change

**Microsoft Teams** : Version 39.0

  * Updated error handling in the following job:

    * **Refresh Token Renewal Job**



Change

**Palo Alto Cortex XDR** : Version 32.0

  * Fixed an issue where the job repeatedly logged errors when a case was merged or deleted in Google SecOps in the following job:

    * **Sync Incidents**



Change

**Proofpoint Cloud Threat Response** : Version 5.0

  * Fixed an issue where null, missing, or unmapped priority values in API payloads caused log ingestion errors in the following connector:

    * **Proofpoint Cloud Threat Response - Incidents Connector**



Change

**Pub/Sub** : Version 4.0

  * Added support for `pubsub_message_id` in the **Unique ID Field** parameter in the following connector:

    * **Pub/Sub - Messages Connector**



Change

**Splunk** : Version 67.0

  * Updated the lookback timestamp progression logic when all fetched alerts in a cycle have already been processed in the following connector:

    * **Splunk ES - Notable Events Connector**



Change

**Zscaler** : Version 16.0

  * Fixed an issue where legacy API key and password authentication failed due to URL path normalization issues.



## August 12, 2026

Feature

**CyberArk Credential Provider** : Version 5.0

  * The following new job has been added:

    * **Sync Integration Credentials Job**



Feature

**Microsoft Graph Mail** : Version 45.0

  * The following new actions have been added:

    * **Block Domain**
    * **Block Sender**
    * **Delete Inbox Rules**
    * **List Rules**
    * **Remove Block Domain**
    * **Remove Block Sender**



Feature

**Microsoft Graph Mail Delegated** : Version 22.0

  * The following new actions have been added:

    * **Block Domain**
    * **Block Sender**
    * **Delete Inbox Rules**
    * **List Rules**
    * **Remove Block Domain**
    * **Remove Block Sender**



Change

**Active Directory** : Version 45.0

  * Fixed an issue in the following action where entity properties were incorrectly reset on update:

    * **Enrich Entities**



Change

**AWS WAF** : Version 14.0

  * Updated integration dependencies.



Change

**Cisco Umbrella** : Version 21.0

  * Fixed an issue in the following action where entity attachment failed due to a bytes object serialization error:

    * **Get Domain Security Info**



Change

**CrowdStrike Falcon** : Version 81.0

  * Added the ability to use device IDs as input parameters in the following actions:

    * **Hide Hosts**
    * **Contain Endpoint**
    * **Download File**
    * **Execute Command**
    * **Get Host Information**
    * **Lift Contained Endpoint**
    * **List Host Vulnerabilities**
    * **On-Demand Scan**
    * **Run Script**



Change

**Enrichment**

  * Fixed an issue in the following action where unsupported entity types were selected during enrichment:

    * **Whois**



Change

**GitSync**

  * Fixed an issue in the following action where the **Include Playbook Blocks** parameter was ignored when a folder allowlist was used:

    * **Push Playbook**



Change

**Microsoft 365 Defender** : Version 30.0

  * Added support for GCC High tenants by dynamically constructing API token scopes and adding a configurable **API Root** parameter in the following connector:

    * **Microsoft 365 Defender - Incidents Connector**
  * Improved error handling and alert processing mechanisms in the following job:

    * **Sync Alerts**



Change

**Microsoft Graph Mail** : Version 45.0

  * Fixed an issue in the following action where an unhandled exception occurred when a user mailbox was not found:

    * **Get Mailbox Account Out Of Facility Settings**



Change

**Microsoft Graph Mail Delegated** : Version 22.0

  * Fixed an issue in the following action where an unhandled exception occurred when a user mailbox was not found:

    * **Get Mailbox Account Out Of Facility Settings**



## August 05, 2026

Change

**Microsoft Graph Mail Delegated** : Version 21.0

  * Updated logic for parsing email headers and S/MIME digitally signed emails in the following connector:

    * **Microsoft Graph Mail Delegated Connector**



Change

**ServiceNow** : Version 70.0

  * Fixed verification logic when updating reference fields in the following action:

    * **Update Incident**



Change

**Microsoft Graph Mail** : Version 44.0

  * Updated logic for parsing email headers and S/MIME digitally signed emails in the following connector:

    * **Microsoft Graph Mail Connector**



Change

**Microsoft 365 Defender** : Version 29.0

  * Updated Google SecOps event structure, added support for incident tags and assignee filtering, updated ontology mapping, and optimized evidence handling with limits on maximum evidence items per alert in the following connector:

    * **Microsoft 365 Defender - Incidents Connector**



Change

**Jira** : Version 61.0

  * Added support for customizable status-to-closure mapping, Case-level job scope, custom field variables in Closed Reason Mapping, context value alignment to JIRA_ISSUE_KEY, and automatic fallback retry mechanism in the following job:

    * **Sync Closure Job**



Change

**Google Chronicle** : Version 92.0

  * Updated the action to use new search API in the following action:

    * **Is Value in Data Table**



Change

**CrowdStrike Falcon** : Version 80.0

  * Implemented 500-device safety limit per entity search, updated device sorting by last_seen.desc, and added batch request chunking for device details, login history, and online states in the following action:

    * **Get Host Information**



## July 30, 2026

Change

**Google Chronicle** : Version 91.0

  * Updated Wiz Defend alert naming format in the following connector:

    * **Google Chronicle - Chronicle Alerts Connector**



## July 29, 2026

Change

**Active Directory** : Version 44.0

  * Added optional `Connection Timeout` and `Receive Timeout` parameters to configure network connectivity limits in the following action:

    * **Enrich Entities**



Change

**Anomali ThreatStream** : Version 18.0

  * Updated API output handling in the following action:

    * **Enrich Entities**



Change

**Google Threat Intelligence** : Version 20.0

  * Added support for `CHILDHASH` and `PARENTHASH` entity types in the following action:

    * **Enrich Entities**
  * Added `Entity Type Filter` parameter to allow configuring entity types for notifications in the following connector:

    * **Google Threat Intelligence - Livehunt Connector**



Change

**Microsoft 365 Defender** : Version 28.0

  * Updated case syncing logic in the following action:

    * **Sync Alerts**
  * Updated alert processing logic in the following connector:

    * **Microsoft 365 Defender - Incidents Connector**



Change

**Siemplify** : Version 112.0

  * Added `Update Enabled Connectors Only` filtering option in the following job:

    * **Response Integration & Connector Upgrade Job**



Change

**Vertex AI** : Version 8.0

  * Added support for multi-region endpoints across the integration configuration.



## July 22, 2026

Feature

**Wiz** : Version 14.0

  * Added the following action:

    * **Get Blue Agent Analysis**



Feature

**SentinelOne Singularity Operations Center** : Version 1.0

  * Added **SentinelOne Singularity Operations Center** integration.



Feature

**Proofpoint Email Protection** : Version 10.0

  * Added the following action:

    * **Download Quarantined Email**



Change

**Azure Monitor** : Version 5.0

  * Updated integration documentation links in the integration configuration.



Change

**QRadar** : Version 69.0

  * Updated timestamp filtering to use `last_persisted_time` for tracking modifications in the following connector:

    * **Qradar Offenses Connector**



Change

**Jira** : Version 60.0

  * Added support for the `Created Before` date filter and `Custom JQL` query parameter in the following action:

    * **List Issues**



Change

**Google Chronicle** : Version 90.0

  * Updated handling of Wiz Defend detections and ontology mapping in the following connector:

    * **Chronicle Alerts Connector**



## July 15, 2026

Change

**AWS GuardDuty** : Version 14.0

  * Added support for Google Cloud Web Identity (OIDC) Federation authentication.



Change

**SCC Enterprise** : Version 22.0

  * Refactored integration code to optimize underlying execution performance.



Change

**Google Threat Intelligence** : Version 18.0

  * Added an optional `Active Group` parameter to support multi-tenant organization context routing in the integration configuration and the following connector:

    * **ASM Issues Connector**



Change

**Google Chronicle** : Version 88.0

  * Added `api_root` parameter to alert extensions to expand normalization metadata options in the following connector:

    * **Chronicle Alerts Connector**



Change

**Microsoft Defender ATP** : Version 33.0

  * Updated execution processing logic to improve backend tracking stability in the following action:

    * **Execute Live Response Command**



Change

**ServiceNow** : Version 68.0

  * Updated affected CIs processing logic to handle missing reference keys smoothly in the following job:

    * **Sync Incidents Job**



Change

**CrowdStrike Falcon** : Version 78.0

  * Fixed pagination loop logic to prevent infinite timeouts during high-volume sweeps in the following action:

    * **Get Host Information**



## July 08, 2026

Change

**FileUtilities** : Version 27.0

  * Added support for extracting files from .7z archives in the following action:

    * **Extract Zip Files**



Change

**Google Threat Intelligence** : Version 17.0

  * Fixed widget rendering failures by escaping raw HTML script tags within `extended_response_body` in the following action:

    * **Get ASM Entity Details**



Change

**Google Chronicle** : Version 87.0

  * Improved case and alert synchronization logic by fixing the verification handling of valid external ID values in the following job:

    * **Google Chronicle Sync Job**



## July 01, 2026

Feature

**Proofpoint Email Protection** : Version 8.0

  * The following new actions have been added to support searching and programmatically managing quarantined emails:

    * **Search Quarantined Emails**

    * **Delete Quarantined Email**

    * **Resubmit Quarantined Email**

    * **Move Quarantined Email**




Change

**Proofpoint Email Protection** : Version 8.0

  * Updated backend script implementation to support the new framework for the following actions:

    * **Enrich Entities**

    * **Ping**




## June 25, 2026

Feature

**Palo Alto Cortex XDR** : Version 30.0

  * The following new action has been added:

    * **Download File**



Feature

**CyberArk PAM** : Version 11.0

  * The following new action has been added:

    * **Change Account Password**



Change

**Siemplify** : Version 110.0

  * Updated results processing logic to cleanly escape backslashes in the following action:

    * **Create Gemini Case Summary**



Change

**Secret Manager** : Version 2.0

  * Updated action description in the following action:

    * **Ping**



Change

**CrowdStrike Falcon** : Version 77.0

  * Updated syncing logic to support multiple CrowdStrike alert IDs mapped to a single SecOps alert and improved error handling for alert ID context values in the following connector:

    * **Sync Alerts**



Change

**Azure Active Directory** : Version 29.0

  * Updated error handling for sign-in activity retrieval in the following action:

    * **Enrich User**



Change

**Google Cloud Compute** : Version 19.0

  * Refactored action code in the following actions:

    * **Add IP To Firewall Rule**

    * **Remove external IP addresses**

    * **Execute VM Patch Job**

    * **Update Firewall Rule**




Change

**VirusTotalV3** : Version 41.0

  * Updated Predefined Widgets to fix cached fallback rendering in the following actions:

    * **Enrich Hash**

    * **Enrich IOC**

    * **Enrich IP**

    * **Enrich URL**

    * **Get Domain Details**




Change

**Google Threat Intelligence** : Version 16.0

  * Updated Predefined Widgets to optimize loading performance and aligned layouts to prevent visual shifts in the following actions:

    * **Enrich Entities**

    * **Enrich IOCs**




Change

**EmailV2** : Version 42.0

  * Updated default values for IMAP server address, port, username, and password for the following connector:

    * **Generic IMAP Email Connector**



Change

**FireEye Helix** : Version 20.0

  * Added Trellix IAM OAuth authentication support.



Change

**FireEye ETP** : Version 9.0

  * Added Trellix OAuth support, updated public API endpoints to v2, and removed legacy V1 API support.



## June 17, 2026

Feature

**Secret Manager** : Version 1.0

  * New **Secret Manager** integration.



Change

Source code is now publicly available on [GitHub](https://github.com/chronicle/content-hub) for the following integrations:

  * **AlienVault USM Appliance** : Version 29.0

  * **AlienVaultTI** : Version 15.0

  * **Arcsight** : Version 46.0

  * **Axonius** : Version 8.0

  * **BMC Helix Remedyforce** : Version 18.0

  * **Cisco AMP** : Version 24.0

  * **EasyVista** : Version 8.0

  * **Mandiant** : Version 10.0

  * **Office 365 Management API** : Version 11.0

  * **SCCM** : Version 22.0

  * **SonicWall-Beta** : Version 9.0

  * **Stellar Cyber Starlight** : Version 19.0

  * **Symantec Email Security.Cloud** : Version 6.0

  * **Twilio** : Version 16.0

  * **XForce** : Version 20.0

  * **Zabbix** : Version 17.0




Change

**Google Chronicle** : Version 86.0

  * Fixed an issue where the connector would idle or hang on heartbeats instead of breaking early when `nextPageToken` or `nextPageStartTime` is received, and updated ontology mapping in the following connector:

    * **Chronicle Alerts Connector**



Change

**Palo Alto Cortex XDR** : Version 29.0

  * Updated host name extraction logic in the raw payload in the following connector:

    * **Palo Alto Cortex XDR Connector**



## June 11, 2026

Change

**Siemplify** : Version 109.0

  * Refactored the code in the following action:

    * **Attach Playbook to Alert**



## June 10, 2026

Change

**Azure Security Center** : Version 17.0

  * Announced deprecation notice. Connector will be deprecated on 30th March 2027. Only critical bug fixes will be considered. For more information refer to the documentation of individual connectors in the following connector:

    * **Azure Security Center - Security Alerts Connector**



Change

**Google Chronicle** : Version 85.0

  * Updated partial batch handling and added dynamic batch sizing to prevent timeout loops, refactored logging and added monitoring signals for process health, and pipeline states, and improved detections batch parsing and processing efficiency in the following connector:

    * **Chronicle Alerts Connector**
  * **Integration** : Updated authentication flow mechanism.




Change

**Google Cloud IAM** : Version 20.0

  * Updated Predefined Widgets in the following widgets:

    * **List Roles**

    * **List Service Accounts**




Change

**Microsoft Azure Sentinel** : Version 64.0

  * Announced deprecation notice. Connector will be deprecated on 30th March 2027. Only critical bug fixes will be considered. For more information refer to the documentation of individual connectors in the following connectors:

    * **Microsoft Azure Sentinel Incident Connector v2**

    * **Microsoft Sentinel Incident Tracking Connector**




Change

**Microsoft Defender ATP** : Version 32.0

  * Announced deprecation notice. Connector will be deprecated on 30th March 2027. Only critical bug fixes will be considered. For more information refer to the documentation of individual connectors in the following connectors:

    * **Microsoft Defender ATP Connector**

    * **Microsoft Defender ATP Connector V2**




Change

**Microsoft Graph Mail** : Version 42.0

  * Updated the logic for robust handling of transient upstream API errors and connection issues in the following connector:

    * **Microsoft Graph Mail Connector**



Change

**Microsoft Graph Mail Delegated** : Version 19.0

  * Updated the logic for robust handling of transient upstream API errors and connection issues in the following connector:

    * **Microsoft Graph Mail Delegated Connector**



Change

**Microsoft Graph Security** : Version 27.0

  * Announced deprecation notice. Connector will be deprecated on 30th March 2027. Only critical bug fixes will be considered. For more information refer to the documentation of individual connectors in the following connectors:

    * **Microsoft Graph Office 365 Security and Compliance Connector**

    * **Microsoft Graph Security Connector**




Change

**Protectwise** : Version 7.0

  * Refactored the code in the following action:

    * **Get Pcap**



Change

**Qualys VM** : Version 28.0

  * Fixed AttributeError during parsing of multiple host lists and added fallback hostname matching in the following actions:

    * **List Endpoint Detections**

    * **Enrich Host**




## June 03, 2026

Change

**AlienVault USM Appliance** : Version 28.0

  * Refactored the code for the following action: 
    * **Get PCAP Files For Events**



Change

**ConnectWise** : Version 23.0

  * Refactored the code for the following action: 
    * **Create Alerts Ticket**



Change

**Google Chronicle** : Version 84.0

  * Refactored the code for the following action: 
    * **Get Detection Details**



Change

**Jira** : Version 58.0

  * Refactored the code for the following action: 
    * **Create Alert Issue**



Change

**ServiceDesk Plus** : Version 10.0

  * Refactored the code for the following action: 
    * **Create Alert Request**



Change

**ServiceDesk PlusV3** : Version 10.0

  * Refactored the code for the following action: 
    * **Create Alert Request**



Change

**ServiceNow** : Version 67.0

  * Refactored the code for the following action: 
    * **Create Alert Incident**



Change

**Siemplify** : Version 245.0

  * Refactored internal code execution logic for the platform integration.



Change

**MISP** : Version 275.6

  * Refactored internal code execution logic and optimized core integration components.



Change

**Microsoft Sentinel Incident Tracking Connector** : Version 29.0

  * Added the `Incident Creation Time Filter (days)` advanced parameter and optimized error handling logic.



## May 27, 2026

Feature

New **Cloud Identity** integration

## May 20, 2026

Change

**AlienVault USM Appliance** : Version 27.0

  * Refactored the code for the following action: 
    * **Get PCAP Files For Events**



Change

**Protectwise** : Version 6.0

  * Refactored the code for the following action: 
    * **Get Pcap**



Change

**Service Desk Plus** : Version 9.0

  * Refactored the code for the following action: 
    * **Create Alert Request**



Change

**Service Desk Plus V3** : Version 9.0

  * Refactored the code for the following action: 
    * **Create Alert Request**



Change

**ServiceNow** : Version 66.0

  * Updated the code for the following action: 
    * **Update Incident** : Added support for updating reference fields.



Change

**Google Chronicle** : Version 83.0

  * Added support for filtering alerts by rule type to the following connector: 
    * **Google Chronicle - Chronicle Alerts Connector**



Change

**Tanium** : Version 20.0

  * **Integration** : Added a partner header to all API requests.



## May 13, 2026

Change

**Azure Active Directory** : Version 28.0

  * **Integration** : Updated TIPCommon to 2.3.8.



Change

**ConnectWise** : Version 22.0

  * Refactored the code for the following action: 
    * **Create Alerts Ticket**



Change

**EmailV2** : Version 41.0

  * **Integration** : Updated TIPCommon to 2.3.8 and migrated `EnvironmentCommon` imports to `TIPCommon.envcommon`.



Change

**Google Chronicle** : Version 82.0

  * **Integration** : Improved memory efficiency to prevent OOM crashes when querying large timeframes for **Lookup Similar Alerts**.
  * Updated the code for the following action: 
    * **Get Detection Details**
  * Improved Dynamic List filter validation, logging, and added the `Validate Dynamic List Entries` parameter for the following connector: 
    * **Google Chronicle - Chronicle Alerts Connector**



Change

**Jira** : Version 57.0

  * Refactored the code for the following action: 
    * **Create Alert Issue**



Change

**MITRE ATT &CK**: Version 19.0

  * **Integration** : Updated TIPCommon to 2.3.8.



Change

**ServiceNow** : Version 65.0

  * Refactored the code for the following action: 
    * **Create Alert Incident**



## May 06, 2026

Change

**Tenable.io** : Version 18.0

  * Improved the handling of concurrent requests and API rate limits in the following action:

    * **Enrich Entities**



Change

**SiemplifyUtilities** : Version 30.0

  * Added support for backticks to the following action:

    * **Query Joiner**



Change

**Azure Active Directory** : Version 27.0

  * Updated enrichment logic to ensure `id` is fetched when `Include Last Sign In Details` is enabled in the following action:

    * **Enrich User**



Change

**Palo Alto Next Gen Firewall** : Version 29.0

  * **Integration** : Updated Manager to reuse the API token instead of generating a new one.



## April 29, 2026

Change

**UrlScan.io** : Version 30.0

  * Added `is_risky` handling to the following action:

    * **Url Check**



Change

**Siemplify** : Version 107.0

  * **Integration** : Updated TIPCommon dependency.



Change

**Microsoft Graph Mail** : Version 41.0

  * Updated MSG attachments processing logic in the following connector:

    * **Microsoft Graph Mail Connector**



Change

**Zerofox** : Version 4.0

  * **Integration** : Updated documentation link.



Change

**MISP** : Version 39.0

  * Updated tag retrieval logic in the following actions:

    * **Add Tag to an Attribute**

    * **Add Tag to an Event**

    * **Remove Tag from an Attribute**

    * **Remove Tag from an Event**




Change

**Anomali ThreatStream** : Version 16.0

  * Added `is_risky` handling to the following action:

    * **Enrich Entities**



Change

**Microsoft Graph Mail Delegated** : Version 18.0

  * Updated MSG attachments processing logic in the following connector:

    * **Microsoft Graph Mail Delegated Connector**



Change

**Palo Alto Cortex XDR** : Version 28.0

  * Added the ability to ignore specific artifact types to the following connector:

    * **Palo Alto Cortex XDR Connector**



Change

Source code is now publicly available on [GitHub](https://github.com/chronicle/content-hub) for the following integrations:

  * **Cisco Orbital** : Version 9.0

  * **F5 Big IQ** : Version 8.0

  * **FireEye EX** : Version 14.0

  * **HCL BigFix Inventory** : Version 6.0

  * **Illusive Networks** : Version 8.0

  * **Lastline** : Version 10.0

  * **McAfee ATD** : Version 18.0

  * **McAfee Active Response** : Version 10.0

  * **ObserveIT** : Version 6.0

  * **Outpost24** : Version 9.0

  * **Site24x7** : Version 7.0

  * **Splash** : Version 8.0

  * **Websense** : Version 15.0




## April 22, 2026

Feature

**Netskope** : Version 17.0

  * The following new actions have been added:

    * **Add Entities to URL List**

    * **Deploy URL List Changes**




Change

**Netskope** : Version 17.0

  * Added a new `Use V2 API` parameter to the following actions:

    * **List Clients**

    * **List Quarantined Files**

  * **Integration** : Added support for V2 API endpoints and OAuth 2.0 authentication.




Change

**Qualys VM** : Version 26.0

  * **Integration** : Migrated to the latest Qualys API endpoints.



Change

**SCC Enterprise** : Version 21.0

  * Updated ticket synchronization logic in the following job:

    * **Sync SCC Jira Tickets**



Change

**McAfee Mvision EDR** : Version 12.0

  * **Integration** : Added support for configuring the `Login API Root` as a customizable parameter.



## April 15, 2026

Feature

**SentinelOneV2** : Version 50.0

  * The following new job has been added:

    * **Sync Threats**



Feature

**CrowdStrike Falcon** : Version 76.0

  * The following new job has been added:

    * **Sync Alerts**



Change

**ServiceNow** : Version 64.0

  * Added support for disabling overflow settings and updated ticket processing and environment mapping logic in the following connector:

    * **ServiceNow Connector**



Change

**Zscaler** : Version 14.0

  * Added the ability to provide IOCs using input parameters to the following actions:

    * **Add To Blacklist**

    * **Add To Whitelist**

    * **Remove From Blacklist**

    * **Remove From Whitelist**

  * **Integration** : Added support for OAuth authentication.




Change

**Mandiant Threat Intelligence** : Version 17.0

  * Optimized execution performance and entity processing logic in the following action:

    * **Enrich Entities**



## April 10, 2026

Feature

**Gmail** : Version 9.0

  * A new predefined widget has been added to the following action:

    * **Delete Email**



Feature

**Tanium** : Version 19.0

  * A new predefined widget has been added to the following action:

    * **Create Connection**



Feature

**Cynet** : Version 13.0

  * New predefined widgets have been added to the following actions:

    * **Delete Hash In Hosts**

    * **Kill Hash In Hosts**

    * **Quarantine Hash In Hosts**




Feature

**Area1** : Version 9.0

  * A new predefined widget has been added to the following action:

    * **Search Indicator**



Feature

**Azure Active Directory** : Version 26.0

  * A new predefined widget has been added to the following action:

    * **Is User In a Group**



Feature

**MX ToolBox** : Version 14.0

  * A new predefined widget has been added to the following action:

    * **SPF Lookup**



Feature

**Active Directory** : Version 41.0

  * New predefined widgets have been added to the following actions:

    * **Is User In Group**

    * **List User Groups**




Feature

**Cisco Threat Grid** : Version 18.0

  * New predefined widgets have been added to the following actions:

    * **Get Hash Associated Domains**

    * **Get Hash Associated IPs**




Feature

**Google Chronicle** : Version 81.0

  * The following new action has been added:

    * **Is CIDR In Data Table**



Feature

**Endgame** : Version 15.0

  * New predefined widgets have been added to the following actions:

    * **Collect Autoruns**

    * **Drivers Survey** (Windows only)

    * **Firewall Survey** (Windows only)

    * **Process Survey**

    * **Removable Media Survey** (Windows only)

    * **Software Survey** (Windows only)

    * **User Sessions Survey**




Feature

**AWS Identity and Access Management (IAM)** : Version 10.0

  * A new predefined widget has been added to the following action:

    * **Disable User Access**



Feature

**Carbon Black Response** : Version 39.0

  * A new predefined widget has been added to the following action:

    * **Download Binary**



Feature

**Carbon Black Protection** : Version 13.0

  * A new predefined widget has been added to the following action:

    * **Get Computers By File**



Feature

**McAfee ATD** : Version 17.0

  * A new predefined widget has been added to the following action:

    * **Check Hash**



Feature

**UnshortenMe** : Version 9.0

  * A new predefined widget has been added to the following action:

    * **Unshorten URL**



Feature

**CiscoUmbrella** : Version 19.0

  * A new predefined widget has been added to the following action:

    * **Get Associated Domains**



Feature

**Microsoft Graph Mail** : Version 40.0

  * A new predefined widget has been added to the following action:

    * **Get Mailbox Account Out Of Facility Settings**



Change

**Exabeam Advanced Analytics** : Version 10.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**Check Point SandBlast** : Version 8.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Query**

    * **Upload File**




Change

**Palo Alto AutoFocus** : Version 12.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Hunt Domain**

    * **Hunt File**

    * **Hunt Ip**

    * **Hunt Url**




Change

**XForce** : Version 19.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get Hash Info**

    * **Get IP Info**

    * **Get IP malware**

    * **Get Url Info**




Change

**Trend Micro Apex Central** : Version 7.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Create Entity UDSO**

    * **Create File UDSO**

    * **Enrich Entities**




Change

**BulkWhoIs** : Version 18.0

  * Introduced light theme support for the predefined widget of the following action:

    * **WhoIs Details**



Change

**Any.Run** : Version 12.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Report**



Change

**Siemplify ThreatFuse** : Version 19.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**Google Cloud Policy Intelligence** : Version 7.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Search Service Account Activity**



Change

**MISP** : Version 38.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Get Event Details**

    * **Get Related Events**




Change

**ReversingLabs Titanium** : Version 12.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Malware Details**



Change

**MX ToolBox** : Version 14.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **A Record Lookup**

    * **Blacklist Check**

    * **MX Record Lookup**

    * **Reverse DNS Lookup**




Change

**Google Rapid Response (GRR)** : Version 11.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get Client Details**

    * **List Clients**

    * **List Launched Flows**




Change

**Armis** : Version 15.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**Lastline** : Version 9.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Analysis Results**



Change

**McAfee Mvision EPO** : Version 11.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Endpoint**



Change

**Office 365 Cloud App Security** : Version 26.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get IP related activities**

    * **Get User related activities**




Change

**SSL Labs** : Version 11.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Analyse Entity**



Change

**Qualys VM** : Version 25.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Host**

    * **List Endpoint Detections**




Change

**Exchange** : Version 123.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get Account Out Of Facility Settings**

    * **Send Email And Wait**




Change

**Microsoft Defender ATP** : Version 31.0

  * Added Graph API V2 version support to the following actions:

    * **Get User Related Alerts**

    * **List Alerts**

    * **Ping**

    * **Update Alert**

  * Deprecated the following actions:

    * **Get File Related Alerts**

    * **Get Machine Related Alerts**

  * Added Graph API V2 version support to the following connector:

(REGRESSIVE) The connector must be updated by April 10, 2026.

**Note:** You must update ontology mapping. Alerts created with the new API have a different structure and require additional permissions. We recommend using **Microsoft 365 Defender - Incidents Connector** as a replacement.
    * **Microsoft Defender ATP Connector V2**
  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Execute Live Response Command**

    * **Get File Related Alerts**

    * **Get File Related Machines**

    * **Get Machine Logon Users**

    * **Get Machine Recommendations**

    * **Get Machine Related Alerts**

    * **Get Machine Vulnerabilities**

    * **Get User Related Alerts**




Change

**Cisco AMP** : Version 23.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get Computer Info**

    * **Get Computers By File Hash**

    * **Get Computers By File Name**

    * **Get Computers By Network Activity (Ip)**

    * **Get Computers By Network Activity (URL)**

    * **Isolate Machine**

    * **Unisolate Machine**




Change

**HaveIBeenPwned** : Version 10.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Check Account**



Change

**Symantec Blue Coat ProxySG** : Version 7.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Block Entities**

    * **Enrich Entities**




Change

**Cybereason** : Version 25.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Get Sensor Details**

    * **Is Probe Connected**




Change

**Cofense Triage** : Version 21.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **EnrichURL**

    * **Get Domain Details**

    * **Get Threat Indicator Details**




Change

**Slack** : Version 30.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Send Advanced Message**

    * **Send Message**




Change

**IPVoid** : Version 12.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Ip Reputation**



Change

**RSA NetWitness EDR** : Version 9.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Endpoint**

    * **Get IOC Details**




Change

**Microsoft Intune** : Version 8.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Managed Device**



Change

**Trend Micro DDAN** : Version 6.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Submit File**

    * **Submit File URL**




Change

**Tenable.io** : Version 17.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **List Endpoint Vulnerabilities**




Change

**JoeSandbox** : Version 11.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Search Hash**

    * **Search Url**




Change

**Endgame** : Version 15.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Network Survey**

    * **System Survey**




Change

**ThreatQ** : Version 19.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich CVE**

    * **Enrich Email**

    * **Enrich Hash**

    * **Enrich IP**

    * **Enrich URL**

    * **Get Indicator Details**

    * **Get Malware Details**

    * **Link Entities**

    * **Link Entities To Object**

    * **List Entity Related Objects**

    * **Update Indicator Score**

    * **Update Indicator Status**




Change

**RSA NetWitness Platform** : Version 17.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Endpoint**

    * **Enrich File**

    * **Query NetWitness For Events Around Host**

    * **Query NetWitness For Events Around IP**

    * **Query NetWitness For Events Around User**




Change

**McAfee TIEDXL** : Version 9.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get File Reputation**



Change

**Symantec Endpoint Protection 14** : Version 21.0

  * Introduced light theme support for the predefined widget of the following action:

    * **GetSystemInfo**



Change

**FireEye AX** : Version 9.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Submit URL**



Change

**Splash** : Version 7.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**MalShare** : Version 11.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Hash**



Change

**Elastica CloudSOC** : Version 8.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get User Activities**



Change

**Amazon Macie** : Version 10.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Findings**



Change

**CiscoUmbrella** : Version 19.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get Domain Security Info**

    * **Get Domain Status**

    * **Get Whois**

    * **Is Domain In Cisco Popularity List**




Change

**SCCM** : Version 21.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Get Computer Properties**

    * **Get Login History**




Change

**Web Risk** : Version 4.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Submit Entities**




Change

**DShield** : Version 8.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Ip Info**



Change

**Tenable Security Center** : Version 22.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich IP**

    * **Get Related Assets**

    * **Get Vulnerabilities for IP**




Change

**ServiceNow** : Version 63.0

  * Introduced light theme support for the predefined widget of the following action:

    * **List Records Related To User**



Change

**McAfee EPO** : Version 37.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Compare Server and Agent DAT**

    * **Get Agent Information**

    * **Get Dat Version**

    * **Get Endpoint Events**

    * **Get Events For Hash**

    * **Get Host IPS Status**

    * **Get Host Network IPS Status**

    * **Get Last Communication Time**

    * **Get McAfee Epo Agent Version**

    * **Get System Information**

    * **Get Virus Engine Agent Version**

    * **Run Full Scan**

    * **Update Mcafee Agent**




Change

**RSA NetWitness** : Version 20.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Query NetWitness For Events Around Host**

    * **Query NetWitness For Events Around IP**

    * **Query NetWitness For Events Around User**




Change

**Axonius** : Version 7.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Add Note**

    * **Enrich Entities**




Change

**Automox** : Version 8.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Execute Device Command**

    * **Execute Policy**




Change

**Cylance** : Version 19.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Get Threat**

    * **Get Threat Devices**

    * **Get Threat Download Link**




Change

**Anomali** : Version 15.0

  * Introduced light theme support for the predefined widget of the following action:

    * **GetThreatInfo**



Change

**TruSTAR** : Version 9.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**PhishingInitiative** : Version 12.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Url Status**



Change

**Digital Shadows** : Version 12.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **EnrichCVE**

    * **EnrichHash**

    * **EnrichIP**

    * **EnrichURL**




Change

**iBoss** : Version 14.0

  * Introduced light theme support for the predefined widget of the following action:

    * **URL Lookup**



Change

**Google Cloud IAM** : Version 19.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Get Service Account IAM Policy**

    * **Rotate Service Account Keys**

    * **Set Service Account IAM Policy**




Change

**Sumo Logic Cloud SIEM** : Version 13.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Search Entity Signals**




Change

**Microsoft Teams** : Version 37.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Create Chat**

    * **Send User Message**




Change

**FortiAnalyzer** : Version 12.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**Sophos** : Version 21.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Get Events Log**

    * **Get Services Status**




Change

**Palo Alto Cortex XDR** : Version 27.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Scan Endpoint**




Change

**Cisco Threat Grid** : Version 18.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Submissions**



Change

**Intezer** : Version 14.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Submit Hash**



Change

**Recorded Future** : Version 22.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich CVE**

    * **Enrich Hash**

    * **Enrich Host**

    * **Enrich IP**

    * **Enrich IOC**

    * **Enrich URL**




Change

**Gmail** : Version 9.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Search For Emails**

    * **Wait For Thread Reply**




Change

**Illusive Networks** : Version 7.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Run Forensic Scan**




Change

**VirusTotal** : Version 42.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get Domain Report**

    * **Scan Hash**

    * **Scan IP**

    * **Scan URL**

    * **Upload And Scan Files**




Change

**Anomali ThreatStream** : Version 15.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**ThreatConnect** : Version 17.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**Azure Active Directory** : Version 26.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Host**

    * **Enrich User**

    * **Get Manager Contact Details**

    * **List Users**

    * **List User's Groups Membership**

    * **Revoke User Session**




Change

**Splunk** : Version 65.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Host Events**



Change

**Attivo** : Version 10.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**Cisco ISE** : Version 16.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Add Endpoint To Endpoint Identity Group**



Change

**DeepSight** : Version 11.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Scan Domain**

    * **Scan Email**

    * **Scan File Name**

    * **Scan Hash**

    * **Scan IP**

    * **Scan URL**




Change

**Symantec Email Security Cloud** : Version 5.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Block Entities**



Change

**GSuite** : Version 26.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Get Extension Details**

    * **Get Group Details**

    * **Get Host Browser Details**

    * **List Group Privileges**

    * **List User Privileges**

    * **Revoke User Session**

    * **Search User Activity Events**




Change

**SymantecESCC** : Version 9.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**Google Cloud Compute** : Version 17.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**FireEye HX** : Version 23.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get Host Alert Groups**

    * **Get Host Info**

    * **Get List of File Acquisitions For Host**

    * **Is Contain Malware Alerts**




Change

**Rapid7 InsightVm** : Version 16.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Asset**



Change

**McAfee Mvision EDRV2** : Version 5.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Create Investigation**



Change

**HCL BigFix Inventory** : Version 5.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**SiemplifyUtilities** : Version 29.0

  * Added support for a custom delimiter in the following action:

    * **Query Joiner**



Change

**Nmap** : Version 4.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Scan Entities**



Change

**VMware Carbon Black Enterprise EDR** : Version 10.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Hash**

    * **Get Events Associated With Process by Process Guide**

    * **Process Search**




Change

**Outpost24** : Version 8.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**PassiveTotal** : Version 14.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **WhoIs Address Reputation**

    * **Whois Host Reputation**

    * **WhoIs Scan Address**

    * **WhoIs Scan Domain**




Change

**Carbon Black Defense** : Version 12.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get Device Info**

    * **Get Events**

    * **Get Processes**




Change

**QRadar** : Version 67.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Similar Events Query**

    * **Similar Flows Query**




Change

**SentinelOneV2** : Version 49.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Create Hash Blacklist Record**

    * **Create Hash Exclusion Record**

    * **Get Agent Status**

    * **Get Application List For Endpoint**

    * **Get Events For Endpoint Hours Back**

    * **Get Group Details**

    * **Get Hash Reputation**




Change

**Zscaler** : Version 13.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get Sandbox Report**

    * **Lookup Entity**




Change

**McAfee Mvision EDR** : Version 11.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Endpoint**



Change

**Tanium** : Version 19.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Delete File**

    * **Enrich Entities**

    * **List Endpoint Events**

    * **Quarantine Endpoint**




Change

**VMware Carbon Black Endpoint Standard Live Response** : Version 10.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Create Memdump**

    * **Delete File**

    * **Delete File from Cloud Storage**

    * **Download File**

    * **Execute File**

    * **Kill Process**

    * **List Files**

    * **List Files in Cloud Storage**

    * **List Processes**

    * **Put File**




Change

**VSphere** : Version 12.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Vm By Ip**



Change

**Nozomi Networks** : Version 10.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**Active Directory** : Version 41.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich entities**

    * **Get Manager Contact Details**




Change

**Talos** : Version 20.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get Reputation**

    * **WhoIs**




Change

**Check Point Threat Reputation** : Version 8.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get File Hash Reputation**

    * **Get Host Reputation**

    * **Get IP Reputation**




Change

**Zabbix** : Version 16.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Execute Script**



Change

**FireEye Helix** : Version 19.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Add Entities To a List**



Change

**Malware Domain List** : Version 11.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Check URL**



Change

**AlienVault USM Appliance** : Version 26.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Assets**

    * **Enrich Vulnerabilities**




Change

**Alexa** : Version 9.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get URL Rank**



Change

**AWS GuardDuty** : Version 12.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get a Trusted IP List**

    * **Get Detector Details**

    * **Get Threat Intelligence Set Details**




Change

**HTTP** : Version 15.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get URL Data**



Change

**BlueLiv** : Version 13.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **List Entity Threats**




Change

**Azure AD Identity Protection** : Version 9.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**Carbon Black Response** : Version 39.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Binary**

    * **Enrich Process**

    * **Get System Info**

    * **Hosts By Process**

    * **List Processes**




Change

**Falcon Sandbox** : Version 21.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get Hash Scan Report**

    * **Scan URL**

    * **Submit File**




Change

**CSV** : Version 41.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **CSV Search by Entity**

    * **CSV Search by String**




Change

**URLVoid** : Version 14.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get domain reputation**



Change

**Harmony Mobile** : Version 7.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**Cloudflare** : Version 8.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Add URL To Rule List**



Change

**Carbon Black Protection** : Version 13.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Analyze File**



Change

**Jira** : Version 56.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Search Users**



Change

**Microsoft Graph Mail Delegated** : Version 17.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Mailbox Account Out Of Facility Settings**



Change

**Trend Vision One** : Version 9.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Execute Custom Script**

    * **Isolate Endpoint**

    * **Submit File**

    * **Submit URL**

    * **Unisolate Endpoint**




Change

**Internet Storm Center** : Version 6.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**AlienVaultTI** : Version 14.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enriches Entities**



Change

**Google Threat Intelligence** : Version 14.0

  * Migrated the following connector to new API endpoints:

**Note:** Duplicate notifications may occur temporarily during the transition.
    * **Google Threat Intelligence - Livehunt Connector**



Change

**Shodan** : Version 17.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Get Ip Info**



Change

**Cisco Vulnerability Management** : Version 3.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **List Asset Vulnerabilities**




Change

**ForeScout CounterACT** : Version 6.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**McAfee ESM** : Version 46.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get Similar Events**

    * **Send Entity Query To ESM**




Change

**LogRhythm** : Version 23.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **List Entity Events**




Change

**Mandiant ASM** : Version 13.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Search ASM Entities**



Change

**Ivanti Endpoint Manager** : Version 10.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Enrich Entities**

    * **List Endpoint Vulnerabilities**




Change

**Cuckoo** : Version 14.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Detonate Url**



Change

**IntSights** : Version 27.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Search IOCs**



Change

**Vectra** : Version 13.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Endpoint**



Change

**McAfee ATD** : Version 17.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Submit URL**



Change

**FortinetFortiSIEM** : Version 10.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Entities**



Change

**ThreatCrowd** : Version 9.0

  * Introduced light theme support for the predefined widget of the following action:

    * **EnrichEntities**



Change

**APIVoid** : Version 14.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Get domain reputation**

    * **Get Ip Reputation**

    * **Get Screenshot**

    * **Get URL Reputation**

    * **Verify Email**




Change

**McAfee Mvision EPOV2** : Version 8.0

  * Introduced light theme support for the predefined widget of the following action:

    * **Enrich Endpoint**



Change

**VMRay** : Version 19.0

  * Introduced light theme support for predefined widgets of the following actions:

    * **Scan Hash**

    * **Scan URL**




Change

**Google Chronicle** : Version 81.0

  * Added support for CIDR matching to the following action:

    * **Is Value In Reference List**



## April 01, 2026

Feature

**Microsoft 365 Defender** : Version 26.0

  * The following new job has been added:

    * **Sync Alerts**



Feature

**SentinelOneV2** : Version 48.0

  * The following new job has been added:

    * **Sync Alerts**



Change

**Microsoft Teams** : Version 36.0

  * Optimized user lookup logic for the following actions:

    * **Add Users To Channel**

    * **Create Chat**




Change

**Akamai** : Version 6.0

  * Updated the JSON results of the following actions:

    * **Add Items To Client List**

    * **Remove Items From Client List**




Change

Source code is now publicly available on [GitHub](https://github.com/chronicle/content-hub) for the following integrations:

  * **CyberX** : Version 6.0

  * **JuniperVSRX** : Version 11.0

  * **McAfee NSM** : Version 11.0

  * **Micro Focus ITSMA** : Version 7.0

  * **Portnox** : Version 9.0

  * **ReversingLabs A1000** : Version 10.0

  * **Stealthwatch V6.10** : Version 6.0

  * **Symantec Content Analysis** : Version 7.0




Change

**Azure Active Directory** : Version 25.0

  * Added the ability to fetch last login time information to the following actions:

    * **Enrich User**

    * **Get Manager Contact Details**




## March 25, 2026

Feature

**Azure API** : Version 3.0

  * Added predefined widget to the following action:

    * **Ping**



Feature

**Microsoft Graph Security** : Version 26.0

  * Added predefined widget to the following action:

    * **Get Incident**



Feature

**Google Cloud IAM** : Version 20.0

  * The following new action has been added:

    * **Rotate Service Account Keys**



Feature

**Siemplify** : Version 106.0

  * The following new action has been added:

    * **Search Cases**
  * Added predefined widget to the following action:

    * **Search Cases**



Feature

**Microsoft Defender ATP** : Version 30.0

  * The following new actions have been added:

    * **Get Machine Recommendations**

    * **Get Machine Vulnerabilities**

    * **Get User Related Alerts**




Change

**BitSight** : Version 12.0

  * IIntroduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Company Details**



Change

**RSA NetWitness Platform** : Version 16.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Update Incident**



Change

**CyberArk Credential Provider** : Version 3.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Application Password Value**

    * **Run CLI Application Password SDK Command**




Change

**CrowdStrike Falcon** : Version 75.0

  * Added offline queueing support to the following actions:

    * **Execute Command**

    * **Run Script**




Change

**MobileIron** : Version 6.0

  * **Integration** : The integration's source code is now publicly available on [Github](https://github.com/chronicle/content-hub).



Change

**FireEye HX** : Version 22.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Acknowledge Alert Groups**

    * **Get Indicator**




Change

**Anomali ThreatStream** : Version 14.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Related Associations**

    * **Get Related Entities**




Change

**HashiCorp Vault** : Version 6.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Generate AWS Credentials**

    * **List AWS Roles**

    * **List Key-Value Secret Keys**

    * **Read Key-Value Secret**




Change

**AWS WAF** : Version 11.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Rule Groups**

    * **List Web ACLs**




Change

**Microsoft Graph Security** : Version 26.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Alert**



Change

**JoeSandbox** : Version 10.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Detonate File**



Change

**ThreatQ** : Version 18.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Attribute**

    * **Add Source**

    * **Create Adversary**

    * **Create Event**

    * **Create Indicator**

    * **Create Object**

    * **Link Objects**




Change

**Symantec Endpoint Security Complete Cloud** : Version 8.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Symantec Endpoint Security Complete Cloud**



Change

**EmailV2** : Version 40.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Delete Email**

    * **Forward Email**

    * **Save Email Attachments To Case**

    * **Send Email**

    * **Send Thread Reply**

    * **Wait for Email from User**




Change

**Cofense Triage** : Version 20.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Tags To Report**

    * **Categorize Report**

    * **Download Report Email**

    * **Download Report Preview**

    * **Get Report Reporters**




Change

**CA Service Desk Manager** : Version 26.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Wait For Status Change**



Change

**Microsoft Defender ATP** : Version 30.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Update Alert**



Change

**Akamai** : Version 5.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Activate Client List**

    * **Activate Network List**

    * **Add Items To Network List**

    * **Remove Items From Network List**




Change

**SSH** : Version 20.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Connections**

    * **List iptables Rules**

    * **List Processes**

    * **Run Command**




Change

**Microsoft Azure Sentinel** : Version 62.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Comment to Incident**

    * **Create Alert Rule**

    * **Create Custom Hunting Rule**

    * **Get Alert Rule Details**

    * **Get Custom Hunting Rule Details**

    * **Get Incident Statistic**

    * **Update Alert Rule**

    * **Update Custom Hunting Rule**

    * **Update Incident Details**

    * **Update Incident Details v2**

    * **Update Incident Labels**

    * **Update Incident Labels v2**




Change

**Google Cloud Compute** : Version 16.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add IP To Firewall Rule**

    * **Add Network Tags**

    * **Delete Instance**

    * **Execute VM Patch Job**

    * **Remove IP From Firewall Rule**

    * **Remove Network Tags**

    * **Start Instance**

    * **Stop Instance**

    * **Update Firewall Rule**




Change

**Microsoft Graph Mail Delegated** : Version 16.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Forward Email**

    * **Save Email to the Case**

    * **Send Email**

    * **Send Email HTML**

    * **Send Thread Reply**

    * **Send Vote Email**

    * **Wait For Email From User**

    * **Wait For Vote Email Results**




Change

**Extrahop** : Version 8.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Update Detection**



Change

**Palo Alto Cortex XDR** : Version 26.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Incident Details**

    * **Query**




Change

**Recorded Future** : Version 21.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Alert Details**



Change

**VSphere** : Version 11.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get System Info**



Change

**FireEye CM** : Version 14.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add IOC Feed**

    * **Download Alert Artifacts**




Change

**Tenable.io** : Version 16.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Scan Endpoints**



Change

**Remote Agent Utilities** : Version 7.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Serialize A File**



Change

**FireEye Helix** : Version 18.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Archive Search**

    * **Get Alert Details**

    * **Index Search**




Change

**Okta** : Version 16.0

  * **Integration** : Added support for OAuth authentication.



Change

**Office 365 CloudApp Security** : Version 25.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add IP To IP Address Range**

    * **Create IP Address Range**

    * **Remove IP From IP Address Range**




Change

**Palo Alto Prisma Cloud** : Version 6.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Enrich Assets**



Change

**Google Cloud Armor** : Version 5.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add a Rule to a Security Policy**

    * **Create a Security Policy**

    * **Update a Security Policy**




Change

**Redis** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add To List**

    * **Get List**




Change

**Carbon Black Response** : Version 38.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get FileMod Data For Process**

    * **Get Process Tree Data**




Change

**Microsoft Graph Mail** : Version 39.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Forward Email**

    * **Save Email to the Case**

    * **Send Email**

    * **Send Email HTML**

    * **Send Thread Reply**

    * **Send Vote Email**

    * **Wait For Email From User**

    * **Wait For Vote Email Results**




Change

**NessusScanner** : Version 12.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Scan Templates**



Change

**Atlassian Confluence Server** : Version 5.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Child Pages**

    * **Get Page by ID**

    * **Get Page Comments**

    * **List Pages**




Change

**Slack** : Version 29.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Build Block**

    * **Create Channel**

    * **Get User Details**

    * **Get User Details By Id**

    * **Rename Channel**

    * **Wait For Reply**

    * **Wait For Reply With Webhook**




Change

**McAfee ATD** : Version 16.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Report**

    * **Submit File**




Change

**Symantec ICDX** : Version 9.0

  * **Integration** : The integration's source code is now publicly available on [Github](https://github.com/chronicle/content-hub).



Change

**McAfee NSM** : Version 10.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Alert Info Data**



Change

**Cloudflare** : Version 7.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Firewall Rule**

    * **Create Rule List**

    * **Update Firewall Rule**




Change

**Rapid7 InsightIDR** : Version 12.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Saved Query**

    * **Set Investigation Assignee**

    * **Set Investigation Status**

    * **Update Investigation**




Change

**Exchange Extension Pack** : Version 13.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Domains to Exchange-Siemplify Mail Flow Rules**

    * **Add Senders to Exchange-Siemplify Mail Flow Rule**

    * **Purge Compliance Search Results**

    * **Remove Domains from Exchange-Siemplify Mail Flow Rules**

    * **Remove Senders from Exchange-Siemplify Mail Flow Rules**

    * **Run Compliance Search**




Change

**CSV** : Version 40.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Save Json To CSV**



Change

**Mandiant ASM** : Version 12.0

  * IIntroduced Light Theme compatibility for the predefined widget of the following action:

    * **Update Issue**



Change

**Shodan** : Version 16.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **DNS Resolve**

    * **DNS Reverse**

    * **Get Api Info**




Change

**Google Kubernetes Engine** : Version 9.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Operation Status**

    * **List Clusters**

    * **List Node Pools**

    * **List Operations**

    * **Set Cluster Addons**

    * **Set Cluster Labels**

    * **Set Node Autoscaling**

    * **Set Node Count**

    * **Set Node Pool Management**




Change

**SiemplifyUtilities** : Version 28.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Delete File**

    * **Filter JSON**

    * **Get Deployment URL**

    * **List Operations**

    * **Parse EML to JSON**




Change

**Anomali** : Version 14.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Related Associations**



Change

**Reversinglabs A1000** : Version 9.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Upload File**



Change

**CyberArk PAM** : Version 9.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Account Password Value**



Change

**Jira** : Version 55.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Alert Issue**

    * **Create Issue**

    * **List Issues**

    * **Update Issue**




Change

**Ivanti Endpoint Manager** : Version 9.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Execute Query**

    * **List Column Set Fields**

    * **List Column Sets**

    * **List Delivery Methods**

    * **List Packages**

    * **List Queries**




Change

**Check Point Firewall** : Version 15.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add a SAM Rule**

    * **Remove SAM Rule**

    * **Run Script**




Change

**Any.Run** : Version 11.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **AnalyzeFile**

    * **AnalyzeFileURL**

    * **AnalyzeURL**




Change

**Carbon Black Protection** : Version 12.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get System Info**



Change

**LogRhythm** : Version 22.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Note To Case**

    * **Create Cas**

    * **Download Case Files**

    * **Update Case**




Change

**BMC Remedy ITSM** : Version 12.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Incident**

    * **Create Record**

    * **Wait For Incident Fields Update**

    * **Wait For Record Fields Update**




Change

**AlienVault USM Anywhere** : Version 35.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Alarm Details**



Change

**Zoho Desk** : Version 11.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Comment To Ticket**

    * **Create Ticket**

    * **Update Ticket**




Change

**AWS GuardDuty** : Version 11.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create a Detector**

    * **Create a Trusted IP List**

    * **Create Threat Intelligence Set**

    * **Get all Trusted IP lists**

    * **Get Finding Details**

    * **List Detectors**

    * **List Findings for a Detector**

    * **List Threat Intelligence Sets**




Change

**AWS Elastic Compute Cloud (EC2)** : Version 10.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Instances**

    * **List Security Groups**

    * **Take Snapshot**




Change

**Cybereason** : Version 24.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Malop**

    * **List Malop Processes**

    * **List Reputation Items**




Change

**Rapid7 InsightVm** : Version 15.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Scan Results**

    * **Launch Scan**




Change

**Cisco AMP** : Version 22.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Group**

    * **Get File Lists By Policy**

    * **Get Groups**

    * **Get Policies**




Change

**Trend Micro Cloud App Security** : Version 11.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Enrich Entities**



Change

**CiscoUmbrella** : Version 18.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Malicious Domains**



Change

**Solar Winds Orion** : Version 7.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Enrich Endpoint**

    * **Execute Entity Query**

    * **Execute Query**




Change

**Tenable Security Center** : Version 21.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add IP To IP List Asset**

    * **Create IP List Asset**

    * **Get Report**

    * **Get Scan Results**

    * **Run Asset Scan**




Change

**Gmail** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Forward Email**

    * **Save Email To The Case**

    * **Send Email**

    * **Send Thread Reply**




Change

**FireEye AX** : Version 8.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Appliance Details**



Change

**FortiAnalyzer** : Version 11.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Comment To Alert**

    * **Update Alert**




Change

**WMI** : Version 14.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **GetSystemInfo**



Change

**Google Chat** : Version 7.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Send Advanced Message**

    * **Send Message**




Change

**SentinelOneV2** : Version 47.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Device Control Rule**

    * **Download Threat File**

    * **Enrich Endpoint**

    * **Get System Status**

    * **Update Alert**

    * **Update Device Control Rule**




Change

**Google Translate** : Version 6.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Translate Text**

    * **List Languages**




Change

**Exchange** : Version 122.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Save Mail Attachments To The Case**

    * **Send Mail**

    * **Send Thread Reply**

    * **Send Vote Mail**

    * **Wait for mail from user**

    * **Wait for Vote Mail Results**




Change

**Symantec ATP** : Version 12.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Incident Comments**



Change

**Azure API** : Version 3.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Execute HTTP Request**



Change

**Tanium** : Version 18.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Question**

    * **Download File**

    * **Get Question Results**




Change

**Site24x7** : Version 6.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Generate Refresh Token**



Change

**ConnectWise** : Version 21.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Attachment To Ticket**

    * **Get Ticket**




Change

**Cisco Threat Grid** : Version 17.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Upload Sample**



Change

**Zendesk** : Version 12.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Ticket Details**

    * **Search Tickets**




Change

**Symantec Endpoint Protection 12** : Version 15.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **GetReport**



Change

**ServiceNow** : Version 62.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Comment To Record**

    * **Add Parent Incident**

    * **Create Alert Incident**

    * **Create Incident**

    * **Create Record**

    * **Get Incident**

    * **Get Oauth Token**

    * **Get Record Details**

    * **Update Incident**

    * **Update Record**

    * **Wait For Field Update**

    * **Wait For Status Update**




Change

**Cuckoo** : Version 13.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Detonate File**

    * **Get Report**




Change

**Sophos** : Version 20.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Alert Actions**



Change

**IronPort** : Version 15.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get All Recipients By Sender**

    * **Get All Recipients By Subject**

    * **Get Report**




Change

**Lastline** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Search Analysis History**

    * **Submit File**

    * **Submit URL**




Change

**F5 BIG-IP iControl API** : Version 7.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add IP To Address List**

    * **Add IP To Data Group**

    * **Add Port To Port List**

    * **Create Address List**

    * **Create Data Group**

    * **Create iRule**

    * **Create Port List**

    * **Remove IP From Address List**

    * **Remove IP From Data Group**

    * **Remove Port From Port List**

    * **Update iRule**




Change

**Palo Alto Panorama** : Version 35.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Ips to group**

    * **Block ips in policy**

    * **Block Urls**

    * **Edit Blocked Applications**

    * **Get Blocked Applications**

    * **Remove Ips from group**

    * **Unblock ips in policy**

    * **Unblock Urls**




Change

**Cynet** : Version 12.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Hash Query**

    * **Remediation Status**




Change

**Trend Vision One** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Execute Email**

    * **Update Workbench Alert**




Change

**MalShare** : Version 10.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Upload File**



Change

**Tor** : Version 9.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Is Exit Node**



Change

**Qualys VM** : Version 24.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Download Report**

    * **List Ips**




Change

**BMC Helix Remedyforce** : Version 17.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Record**

    * **Wait For Fields Update**




Change

**AlienVault USM Appliance** : Version 25.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get PCAP Files For Events**



Change

**Service Desk Plus** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Request**

    * **Get Request**

    * **Update Request**




Change

**FireEye NX** : Version 11.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Download Alert Artifacts**



Change

**Intezer** : Version 13.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Alert**

    * **Submit Alert**

    * **Submit File**

    * **Submit Suspicious Email**




Change

**MISP** : Version 37.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Event**

    * **Create File Misp Object**

    * **Create IP-Port Misp Object**

    * **Create network-connection Misp Object**

    * **Create Virustotal-Report Object**

    * **Download File**

    * **Publish Event**

    * **Unpublish Event**

    * **Upload File**




Change

**Palo Alto Next Gen Firewall** : Version 28.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Ips to group**

    * **Block ips in policy**

    * **Block Urls**

    * **Edit Blocked Applications**

    * **Get Blocked Applications**

    * **Remove Ips from group**

    * **Unblock ips in policy**

    * **Unblock Urls**




Change

**Illusive Networks** : Version 6.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Deceptive Items**



Change

**Freshworks Freshservice** : Version 18.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Agent**

    * **Deactivate Agent**

    * **Update Agent**




Change

**Splunk** : Version 64.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Submit Event**



Change

**AlgoSec** : Version 7.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Allow IP**

    * **Block IP**

    * **Wait for Change Request Status Update**




Change

**Salesforce** : Version 17.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Case**

    * **Search Records**




Change

**RSA Archer** : Version 14.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Incident Journal Entry**

    * **Create Incident**

    * **Get Incident Details**

    * **Update Incident**




Change

**QRadar** : Version 66.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **QRadar AQL Search**

    * **QRadar Simple AQL Search**

    * **Update Offense**




Change

**Mimecast** : Version 15.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Create Block Sender Policy**



Change

**Sumo Logic Cloud SIEM** : Version 12.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Tags To Insight**

    * **Add Comment To Insight**

    * **Update Insight**




Change

**ArcSight** : Version 45.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Resources**



Change

**Microsoft Teams** : Version 35.0

  * **Integration** : Updated dependencies.

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Channel**

    * **Create Channel**

    * **Send Chat Message**

    * **Send Message Reply**

    * **Wait For Reply**




Change

**Service Desk Plus V3** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Note**

    * **Add Note And Wait For Reply**

    * **Close Request**

    * **Create Alert Request**

    * **Create Request**

    * **Create Request - Dropdown Lists**

    * **Get Request**

    * **Update Request**

    * **Wait For Field Update**

    * **Wait For Status Update**




Change

**AWS CloudWatch** : Version 9.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Log Group**

    * **Create Log Stream**




Change

**Endgame** : Version 14.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Investigation Details**



Change

**Falcon Sandbox** : Version 20.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Wait For Job and Fetch Report**



Change

**Google Cloud Recommender** : Version 10.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Apply IAM Recommendations**



Change

**HTTP Rest API** : Version 14.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Data**

    * **Post Data**




Change

**Google Threat Intelligence** : Version 13.0

  * Improved loading for predefined widgets of the following actions:

    * **Enrich Entities**

    * **Enrich IOC**

  * Removed the usage of a deprecated API endpoint and the `Retrieve AI Summary` parameter from the following action:

    * **Submit File**



Change

**IntSights** : Version 26.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Download Alert CSV**



## March 18, 2026

Feature

**Microsoft Graph Mail** : Version 37.0

  * A new predefined widget has been added to the following action:

    * **Delete Email**



Feature

**CrowdStrike Falcon** : Version 73.0

  * The following new action has been added:

    * **Hide Hosts**



Feature

**Endgame** : Version 73.0

  * New predefined widgets have been added to following actions:

    * **Get Endpoints**

    * **Get Host Isolation Config**

    * **Hunt File**

    * **Hunt IP**

    * **Hunt Process**

    * **Hunt Registry**

    * **Hunt User**

    * **List Investigations**




Feature

**Microsoft Graph Security** : Version 24.0

  * A new predefined widget has been added to the following action:

    * **List Incidents**



Change

**Azure Security Center** : Version 14.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Regulatory Standards**

    * **List Regulatory Standard Controls**




Change

**Zoho Desk** : Version 9.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Ticket Details**



Change

**Stellar Cyber Starlight** : Version 17.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Advanced Search**

    * **Simple Search**




Change

**Siemplify ThreatFuse** : Version 17.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Related Associations**

    * **Get Related Domains**

    * **Get Related Email Addresses**

    * **Get Related Hashes**

    * **Get Related IPs**

    * **Get Related URLs**

    * **Submit Observables**




Change

**Devo** : Version 10.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Advanced Query**

    * **Simple Query**




Change

**AWS CloudWatch** : Version 7.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Log Groups**

    * **List Log Streams**

    * **Search Log Events**




Change

**ZScaler** : Version 11.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Url Categories**



Change

**Google Workspace** : Version 24.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Members To Group**

    * **Block Extension**

    * **Create Group**

    * **Create OU**

    * **Create User**

    * **Delete Extension**

    * **List Group Members**

    * **List OU Of Account**

    * **List Users**

    * **Update OU**

    * **Update User**




Change

**Azure Active Directory** : Version 23.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Groups**

    * **List Members in the Group**




Change

**Trend Micro Cloud App Security** : Version 9.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Entity Email Search**



Change

**Tanium** : Version 16.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Task Details**

    * **List Connections**




Change

**Intezer** : Version 11.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Detonate File**

    * **Detonate Hash**

    * **Detonate URL**

    * **Get File Report**

    * **Get URL Report**

    * **Index File**




Change

**RSA NetWitness** : Version 18.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Run General Query**



Change

**MongoDB** : Version 8.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Free Query**



Change

**Exchange** : Version 120.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Block Sender by Message ID**

    * **Delete Mail**

    * **Download Attachments**

    * **Extract EML Data**

    * **List Exchange-Siemplify Inbox Rules**

    * **Move Mail To Folder**

    * **Search Mails**

    * **Unblock Sender by Message ID**




Change

**ThreatQ** : Version 16.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Events**

    * **List Related Objects**




Change

**RSA NetWitness Platform** : Version 14.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Run General Query**



Change

**Carbon Black Response** : Version 36.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Binary Free Query**

    * **Process Free Query**




Change

**Symantec Endpoint Protection** : Version 19.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Report And Enrich**

    * **GetReport**

    * **ListEndpoints**

    * **ListGroups**




Change

**AlienVault USM Anywhere** : Version 33.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Events**



Change

**Mandiant Digital Threat Monitoring** : Version 5.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Update Alert**



Change

**FireEye CM** : Version 12.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Download Custom Rules File**

    * **Download Quarantined Email**

    * **List IOC Feeds**

    * **List Quarantined Emails**




Change

**Google Threat Intelligence** : Version 11.0

  * Updated `is_suspicious` and `is_risky` logic handling in the following actions:

    * **Enrich Entities**

    * **Submit File**




Change

**Shodan** : Version 14.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Search**

    * **SearchForExploits**




Change

**Snowflake** : Version 7.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Execute Custom Query**

    * **Execute Simple Query**




Change

**Proofpoint Threat Protection** : Version 2.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Allow List Entries**

    * **Get Block List Entries**




Change

**Vectra** : Version 11.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Triage Rule Details**



Change

**MSSQL** : Version 18.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **RunSQLQuery**



Change

**Rapid7 InsightVm** : Version 13.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Scans**



Change

**ServiceNow** : Version 60.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Attachment**

    * **Download Attachments**

    * **Get Child Incident Details**

    * **Get CMDB Record Details**

    * **Get User Details**

    * **List CMDB Records**

    * **List Record Comments**

    * **Wait For Comments**




Change

**CiscoUmbrella** : Version 16.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Top Domains**



Change

**RSA NetWitness EDR** : Version 7.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add IP To Blacklist**

    * **Add URL To Blacklist**




Change

**Microsoft 365 Defender** : Version 24.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Execute Custom Query**

    * **Execute Entity Query**

    * **Execute Query**




Change

**Easy Vista** : Version 6.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get EasyVista Ticket**



Change

**Sumologic** : Version 18.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Search**



Change

**Symantec Endpoint Security Complete Cloud** : Version 6.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Device Groups**



Change

**Google Rapid Response (GRR)** : Version 9.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Hunt Details**

    * **List Hunts**

    * **Start a Hunt**

    * **Stop a Hunt**




Change

**TruSTAR** : Version 7.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Related IOCs**

    * **Get Related Reports**

    * **List Enclaves**




Change

**FireEye AX** : Version 6.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Submit File**



Change

**McAfee ATD** : Version 14.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Analyzer Profiles**



Change

**Mimecast** : Version 13.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Advanced Archive Search**

    * **Simple Archive Search**




Change

**Microsoft Azure Sentinel** : Version 60.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Alert Rules**

    * **List Custom Hunting Rules**

    * **List Incidents**

    * **Run Custom Hunting Rule Query**

    * **Run KQL Query**




Change

**ElasticSearch** : Version 42.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Advanced ES Search**

    * **DSL Search**

    * **Simple ES Search**




Change

**FireEye HX** : Version 20.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Alert Group Details**

    * **Get Alerts**

    * **Get Alerts in Alert Group**

    * **Get Indicators**




Change

**FortiGate** : Version 18.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Address Groups**

    * **List Policies**




Change

**CBProtection** : Version 10.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Find File**



Change

**BlueLiv** : Version 11.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Add Comment to a Threat**



Change

**MISP** : Version 35.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Attribute**

    * **Add Sighting to an Attribute**

    * **Add Tag to an Attribute**

    * **Add Tag to an Event**

    * **Create Url Misp Object**

    * **Delete an Attribute**

    * **Delete an Event**

    * **List Event Objects**

    * **List Sightings of an Attribute**

    * **Remove Tag from an Attribute**

    * **Remove Tag from an Event**




Change

**Exchange Extension Pack** : Version 11.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Fetch Compliance Search Results**

    * **List Exchange-Siemplify Mail Flow Rules**




Change

**Google Cloud Storage** : Version 13.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Download an Object From a Bucket**

    * **Get a Bucket's Access Control List**

    * **List Bucket Objects**

    * **List Buckets**

    * **Upload an Object To a Bucket**




Change

**Microsoft Graph Mail Delegated** : Version 14.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Delete Email**

    * **Download Attachments from Email**

    * **Extract Data from Attached EML**

    * **Move Email To Folder**

    * **Run Microsoft Search Query**

    * **Search Emails**




Change

**Ivanti Endpoint Manager** : Version 7.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Execute Task**

    * **Scan Endpoints**




Change

**Akamai** : Version 3.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Items To Client List**

    * **Get Client Lists**

    * **Get Network Lists**

    * **Remove Items From Client List**




Change

**CyberArk PAM** : Version 7.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Accounts**



Change

**Nozomi Networks** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Vulnerabilities**

    * **Run a Query**




Change

**iBoss** : Version 12.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Policy Block List Entries**



Change

**FireEye EX** : Version 12.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Download Alert Artifacts**

    * **Download Quarantined Email**

    * **List Quarantined Emails**




Change

**AWS Security Hub** : Version 9.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Insight**

    * **Get Insight Details**




Change

**Mandiant ASM** : Version 10.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get ASM Entity Details**

    * **Search Issues**




Change

**Cisco Orbital** : Version 17.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Execute Query**



Change

**IronScales** : Version 5.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Incident Details**

    * **Get Incident Mitigation Details**

    * **Get Mitigation Impersonation Detail**

    * **Get Mitigations Per Mailbox**




Change

**Google Cloud IAM** : Version 16.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Role**

    * **Create Service Account**

    * **Delete Role**

    * **List Roles**

    * **List Service Accounts**




Change

**Armis** : Version 13.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Alert Connections**



Change

**Attivo** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Critical ThreatPath**

    * **List Service ThreatPaths**

    * **List Vulnerability Hosts**




Change

**Falcon Sandbox** : Version 18.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Analyze File**

    * **Analyze File URL**

    * **Search**




Change

**Tenable.io** : Version 14.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Vulnerability Details**

    * **List Plugin Families**

    * **List Policies**

    * **List Scanners**




Change

**Google Chat** : Version 5.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Spaces**



Change

**IntSights** : Version 24.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Alert Image**



Change

**Jira** : Version 53.0

  * **Integration** : Added support for service account token based authentication.

  * **Integration** : Updated issue object handling.

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Download Attachments**

    * **Get Issues**

    * **List Relation Types**




Change

**Google BigQuery** : Version 16.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Run Custom Query**

    * **Run SQL Query**




Change

**ArcSight** : Version 43.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Activelist Entries**

    * **Get Query Results**

    * **Get Report**

    * **Is Value In Activelist Column**

    * **Search**




Change

**Check Point Firewall** : Version 13.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Download Log Attachment**

    * **List Layers On Site**

    * **List Policies On Site**

    * **Show Logs**




Change

**FortiAnalyzer** : Version 9.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Search Logs**



Change

**Microsoft Defender ATP** : Version 28.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Isolate Machine Task**

    * **Create Run Antivirus Scan Task**

    * **Create Stop And Quarantine File Specific Machine Task**

    * **Create Unisolate Machine Task**

    * **Get Current Task Status**

    * **List Alerts**

    * **List Indicators**

    * **List Machines**

    * **Run Advanced Hunting Query**

    * **Wait Task Status**




Change

**Microsoft Teams** : Version 33.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Chats**

    * **List Teams**

    * **List Users**

    * **Send Message**




Change

**Recorded Future** : Version 19.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Update Alert**



Change

**Active Directory** : Version 39.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Group Members**

    * **Search Active Directory**




Change

**Cofense Triage** : Version 18.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Report Headers**

    * **List Categories**

    * **List Playbooks**

    * **List Reports Related To Threat Indicators**




Change

**ElasticSearchV7** : Version 20.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Advanced ES Search**

    * **DSL Search**

    * **Simple ES Search**




Change

**BMC Remedy ITSM** : Version 10.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Incident Details**

    * **Get Record Details**




Change

**Cloudflare** : Version 5.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add IP To Rule List**

    * **List Firewall Rules**




Change

**OpenSearch** : Version 2.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Advanced OS Search**

    * **DSL Search**

    * **Simple OS Search**




Change

**Microsoft Graph Mail** : Version 37.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Download Attachments from Email**

    * **Extract Data from Attached EML**

    * **Move Email To Folder**

    * **Search Emails**




Change

**F5 BIG-IP Access Policy Manager** : Version 6.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Active Sessions**



Change

**McAfee Mvision EPO** : Version 9.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Endpoints In Group**

    * **List Groups**

    * **List Tags**




Change

**Palo Alto Cortex XDR** : Version 24.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Execute XQL Search**



Change

**XForce** : Version 17.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get IP By Category**



Change

**Okta** : Version 14.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get User**



Change

**Microsoft Intune** : Version 6.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Managed Devices**



Change

**F5 BIG-IP iControl API** : Version 5.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Address Lists**

    * **List Data Groups**

    * **List Port Lists**

    * **List iRules**




Change

**AppSheet** : Version 4.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Record**

    * **Delete Record**

    * **List Tables**

    * **Search Records**

    * **Update Record**




Change

**McAfee ESM** : Version 44.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Send Advanced Query To ESM**

    * **Send Query To ESM**




Change

**Google Cloud Recommender** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Recommendation**

    * **List Recommendations**

    * **Update Recommendation**




Change

**Any.Run** : Version 9.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Search Report History**



Change

**FireEye Helix** : Version 16.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Lists**

    * **Get List Items**




Change

**Area1** : Version 7.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get Recent Indicators**



Change

**ExabeamAdvancedAnalytics** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Comments To Entity**

    * **Create Watchlist**

    * **List Watchlist Items**

    * **List Watchlists**




Change

**Azure Monitor** : Version 2.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Search Logs**



Change

**Rapid7 InsightIDR** : Version 10.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Investigations**

    * **List Saved Queries**

    * **Run Saved Query**




Change

**Amazon Macie** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Custom Data Identifier**

    * **List Findings**




Change

**AWS IAM Access Analyzer** : Version 8.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Scan Resources**



Change

**ProofPoint TAP** : Version 13.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **DecodeURL**

    * **Get Threat Forensics**

    * **GetCampaign**

    * **List Campaigns**

    * **Search Events**




Change

**Splunk** : Version 62.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Execute Entity Query**

    * **SplunkQuery**




Change

**LogPoint** : Version 18.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Execute Entity Query**

    * **Execute Query**

    * **List Repos**




Change

**BitSight** : Version 10.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Company Highlights**

    * **List Company Vulnerabilities**




Change

**WMI** : Version 12.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **ListServices**

    * **ListUsers**

    * **RunQuery**




Change

**AWS Identity and Access Management (IAM)** : Version .0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create a Group**

    * **Create a Policy**

    * **Create a User**

    * **List Groups**

    * **List Policies**

    * **List Users**




Change

**Fortinet FortiSIEM** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Execute Custom Query**

    * **Execute Simple Query**




Change

**Humio** : Version 7.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Execute Custom Search**

    * **Execute Simple Search**




Change

**AlgoSec** : Version 5.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Templates**



Change

**AWS WAF** : Version 9.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create IP Set**

    * **Create Regex Pattern Set**

    * **Create Rule Group**

    * **Create Web ACL**

    * **List IP Sets**

    * **List Regex Pattern Sets**




Change

**CA Service Desk Manager** : Version 24.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Search Tickets**

    * **Sync Ticket History**




Change

**Freshworks Freshservice** : Version 16.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Ticket Time Entry**

    * **Add a Ticket Note**

    * **Add a Ticket Reply**

    * **Create Requester**

    * **Create Ticket**

    * **List Agents**

    * **List Requesters**

    * **List Ticket Conversations**

    * **List Ticket Time Entries**

    * **List Tickets**

    * **Update Requester**

    * **Update Ticket**

    * **Update Ticket Time Entry**




Change

**BMC Helix RemedyForce** : Version 15.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Execute Custom Query**

    * **Execute Simple Query**

    * **Get Record Details**

    * **List Record Types**




Change

**AWS S3** : Version 6.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Download File From Bucket**

    * **Get Bucket Policy**

    * **List Bucket Objects**

    * **List Buckets**

    * **Upload File To Bucket**




Change

**Cybereason** : Version 22.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Execute Custom Investigation Search**

    * **Execute Simple Investigation Search**

    * **List Malop Affected Machines**

    * **List Malop Remediations**

    * **List Processes**

    * **List files**

    * **Remediate Malop**




Change

**SCCM** : Version 19.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Run WQL Query**



Change

**Netskope** : Version 15.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Alerts**

    * **List Clients**

    * **List Events**




Change

**Qradar** : Version .0

  * Optimized the caching fetched offenses logic in the following connectors:

    * **Qradar Correlation Events Connector V2**

    * **Qradar Offenses Connector**

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Rule MITRE Coverage**

    * **List Reference Maps**

    * **List Reference Maps of Sets**

    * **List Reference Sets**

    * **List Reference Tables**

    * **Lookup for a Key in Reference Map**

    * **Lookup for a Key in Reference Map of Sets**

    * **Lookup for a Value in Reference Map**

    * **Lookup for a Value in Reference Map of Sets**

    * **Lookup for a Value in Reference Set**

    * **Lookup for a Value in Reference Tables**




Change

**Google Cloud Compute** : Version 14.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Labels To Instance**

    * **Get Instance IAM Policy**

    * **List Instances**

    * **Remove External IP Addresses**

    * **Set Instance IAM Policy**




Change

**Cylance** : Version 17.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Global List**

    * **Get Threats**




Change

**EmailV2** : Version 38.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Search Email**



Change

**McAfee EPO** : Version 35.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Execute Custom Query**

    * **Execute Entity Query**

    * **Execute Query By ID**

    * **List Queries**

    * **List Tasks**




Change

**ArcSight Logger** : Version 10.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Send Query**



Change

**SonicWall-Beta** : Version 7.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Address Groups**

    * **List URI Groups**

    * **List URI Lists**




Change

**VSphere** : Version 9.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Vms**



Change

**SiemplifyUtilities** : Version 26.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Export Entities as OpenIOC File**

    * **Extract Top From JSON**




Change

**Office 365 CloudApp Security** : Version 23.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Enrich Entities**

    * **List Files**




Change

**Salesforce** : Version 15.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Cases**



Change

**AWS Elastic Compute Cloud (EC2)** : Version 8.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Start Instance**

    * **Stop Instance**

    * **Terminate Instance**




Change

**McAfee Mvision ePO V2** : Version 6.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **List Devices**

    * **List Tags**




Change

**Anomali ThreatStream** : Version 12.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Submit Observables**



Change

**Automox** : Version 6.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Policies**



Change

**Microsoft Graph Security** : Version 24.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Alerts**



Change

**Qualys VM** : Version 22.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Download Vm Scan Results**

    * **Launch VM Scan And Fetch Results**

    * **List Groups**

    * **List Reports**

    * **List Scans**




Change

**Cloud Logging** : Version 4.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Execute Query**



Change

**Cisco ISE** : Version 14.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **List Endpoint Identity Group**



Change

**SentinelOneV2** : Version 45.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Create Path Exclusion Record**

    * **Get Blacklist**

    * **Get Deep Visibility Query Result**

    * **Get Site Agents**

    * **Get Threats**

    * **Initiate Deep Visibility Query**

    * **List Sites**

    * **Mark as Threat**

    * **Mitigate Threat**

    * **Resolve Threat**




Change

**Palo Alto Panorama** : Version 33.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Correlated Traffic Between IPs**

    * **Search logs**




Change

**Cisco AMP** : Version 20.0

  * Introduced Light Theme compatibility for the predefined widget of the following action:

    * **Get File List Items**



Change

**Slack** : Version 27.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Get Channel Or User Conversation History**

    * **List Channels**

    * **List Users**

    * **Send Interactive Message**




Change

**LogRhythm** : Version 20.0

  * Introduced Light Theme compatibility for predefined widgets of the following actions:

    * **Add Alarm To Case**

    * **Attach File To Case**

    * **Get Alarm Details**

    * **List Case Evidence**




## March 12, 2026

Feature

**Microsoft Azure Sentinel** : Version 59.0

  * The following new job has been added:

    * **Sync Incidents V2**



Change

**Microsoft Azure Sentinel** : Version 59.0

  * Deprecated the following job:

    * **Sync Incidents V2**
**Note:** Use the Sync Incidents V2 job for syncing.



## March 11, 2026

Change

**CrowdStrike Falcon** : Version 72.0

  * Updated the handling of `Days To Expire` in the following action:

    * **Upload IOCs**



Change

**Case Federation** : Version 7.0

  * **Integration** : Updated to support self-service configuration.



Change

**ProofPoint TAP** : Version 12.0

  * Updated input handling in the following action:

    * **DecodeURL**



Change

**Microsoft Teams** : Version 32.0

  * Updated reply handling in the following action:

    * **Wait for Reply**



Change

Introduced Light Theme compatibility for predefined widgets in the following integrations:

  * **CrowdStrike Falcon** : Version 72.0

  * **Google Chronicle** : Version 79.0

  * **Google Cloud API** : Version 8.0

  * **Google Cloud Asset Inventory** : Version 13.0

  * **Google Security Command Center** : Version 16.0

  * **Google Threat Intelligence** : Version 10.0

  * **HTTP v2** : Version 13.0

  * **MITRE ATT &CK**: Version 17.0

  * **ScreenshotMachine** : Version 14.0

  * **Siemplify** : Version 104.0

  * **UrlScan.io** : Version 28.0

  * **Vertex AI** : Version 5.0

  * **VirusTotalV3** : Version 38.0

  * **Vmware Carbon Black Cloud** : Version 37.0




## March 03, 2026

Feature

**Siemplify** : Version 103.0

  * The following new job has been added:

    * **Response Integration & Connector Upgrade**



Feature

**Akamai** : Version 2.0

  * The following new action has been added:

    * **Activate Client List**



Change

**Splunk** : Version 61.0

  * Updated input handling in the following action:

    * **Update Notable Events**



Change

**CrowdStrike Falcon** : Version 71.0

  * Added the ability to define an expiration date for IOCs to the following action:

    * **Upload IOCs**
  * Added support for hidden hosts in the following action:

    * **Get Host Information**



Change

**Google Security Command Center** : Version 15.0

  * Updated the processing of mute states in the following action:

    * **List Asset Vulnerabilities**



Change

**AWS GuardDuty** : Version 9.0

  * Updated severity handling in the following connector:

    * **AWS GuardDuty - Findings Connector**



Change

**Microsoft Graph Mail Delegated** : Version 13.0

  * Updated folder handling in the following actions:

    * **Forward Email**

    * **Save Email To Case**

    * **Send Email**

    * **Send Email HTML**

    * **Send Thread Reply**

    * **Send Vote Email**

    * **Wait For Email From User**

    * **Wait For Vote Email Results**

  * Updated folder handling in the following connector:

    * **Microsoft Graph Mail Delegated Connector**



Change

**Google Chronicle** : Version 78.0

  * Updated raw log data processing in the following actions:

    * **Get Detection Details**

    * **Execute UDM Query**




Change

**Microsoft Graph Mail** : Version 36.0

  * Updated folder handling in the following actions:

    * **Forward Email**

    * **Save Email To Case**

    * **Send Email**

    * **Send Email HTML**

    * **Send Thread Reply**

    * **Send Vote Email**

    * **Wait For Email From User**

    * **Wait For Vote Email Results**

  * Updated folder handling in the following connector:

    * **Microsoft Graph Mail Connector**



## February 25, 2026

Feature

**Google Workspace** : Version 23.0

  * The following new action has been added:

    * **Remove Extension**



Change

**Google Chronicle** : Version 77.0

  * **Integration** : Updated the error handling for Workload Identity authentication.



Change

**Microsoft 365 Defender** : Version 23.0

  * Added support for Graph API to the following actions:

    * **Execute Query**

    * **Execute Custom Query**

    * **Execute Entity Query**




## February 18, 2026

Feature

New **Proofpoint Threat Protection** integration

Change

**Cofense Triage** : Version 17.0

  * Optimized the report processing in the following connector:

    * **Cofense Triage - Reports Connector**



Change

**Qualys VM** : Version 21.0

  * **Integration** : Added the ability to configure the `X-Requested-With` header.



Change

**QRadar** : Version 63.0

  * Updated the logic for offense processing in the following connectors:

    * **Qradar Correlation Events Connector V2**

    * **Qradar Offenses Connector**




Change

**Palo Alto Cortex XDR** : Version 23.0

  * Added the ability to provide agents using input parameters in the following actions:

    * **Scan Endpoint**

    * **Isolate Endpoint**

    * **Unisolate Endpoint**




Change

**Google Chronicle** : Version 76.0

  * Restored the previous JSON result structure for empty result sets in the following action:

    * **Execute UDM Query**



Change

**Exchange** : Version 119.0

  * Updated the handling of S/MIME emails sent on MacOS in the following connectors:

    * **Exchange - Mail Connector v2 with OAuth Authentication**

    * **Exchange - Mail Connector v2**




Change

**CrowdStrike Falcon** : Version 70.0

  * Deprecated the following actions:

    * **Add Incident Comment**

    * **Update Incident**

    * **Add Comment to Detection**

    * **Close Detection**

    * **Update Detection**

  * Deprecated the following connectors:

    * **CrowdStrike - Detections Connector**

    * **Crowdstrike - Incidents Connector**




## February 11, 2026

Feature

**CiscoUmbrella** : Version 15.0

  * The following new actions have been added:

    * **Is Domain In Cisco Popularity List**

    * **List Top Domains**




Change

**Tenable.io** : Version 13.0

  * Optimized the asset processing of the following connector:

    * **TenableIO - Vulnerabilities Connector**
  * Updated the entity processing logic of the following actions:

    * **Enrich Entities**

    * **List Endpoint Vulnerabilities**

    * **Scan Endpoints**




Change

**Google Threat Intelligence** : Version 9.0

  * Added the ability to define the data freshness threshold for available hashes to the following action:

    * **Submit File**
  * Added the ability to filter using monitor names to the following connector:

    * **Google Threat Intelligence - DTM Alerts Connector**
  * **Integration** : Updated the connectivity test method to avoid API quota consumption.




Change

**Palo Alto Cortex XDR** : Version 22.0

  * Updated the event processing and dynamic list handling of the following connector:

    * **Palo Alto Cortex XDR Connector**
  * Added the ability to ignore certain types of artifacts to the following connector:

    * **Palo Alto Cortex XDR Connector**



## February 04, 2026

Change

**Azure Security Center** : Version 13.0

  * Updated the configuration (`Connector.def`) of the following connector:

    * **Azure Security Center - Security Alerts Connector**



Change

**Google Chronicle** : Version 75.0

  * Optimized performance for large data tables in the following actions:

    * **Is Value In Data Table**

    * **Remove Rows From Data Table**




Change

**Siemplify** : Version 102.0

  * Refactored the following actions:

    * **Get Case Details**

    * **Wait For Custom Fields**

    * **Set Custom Fields**

    * **Get Similar Cases**

    * **Get Custom Field Values**

    * **Export Case**

  * Updated error handling in the following action:

    * **Assign Case**



Change

**Siemplify ThreatFuse** : Version 16.0

  * Updated the configuration (`Connector.def`) of the following connector::

    * **Siemplify ThreatFuse - Observables Connector**



## January 28, 2026

Feature

**Google Threat Intelligence** : Version 8.0

  * The following new actions have been added:

    * **Add ASM Issue Note**

    * **Add Tag To DTM Alert**




Change

**Azure Active Directory** : Version 22.0

  * Added the ability to fetch MFA information to the following actions:

    * **Enrich User**

    * **Get Manager Contact Details**




Change

**Jira** : Version 52.0

  * Optimized ticket processing workflows in the following job:

    * **Sync Closure Job**



Change

**Proofpoint Cloud Threat Response** : Version 2.0

  * **Integration** : Updated dependencies.



Change

**Salesforce** : Version 14.0

  * **Integration** : Updated the Salesforce SDK to the latest version



Change

**Siemplify** : Version 101.0

  * Added support to set custom fields upon alert closure to the following action:

    * **Close Alert**
  * Added support to set custom fields upon case closure to the following action:

    * **Close Case**



Change

**Google Threat Intelligence** : Version 8.0

  * Added the ability to automatically set the `is_suspicious` flag on entities based on specific GTI score and Engine count thresholds in the following action:

    * **Enrich Entities**
  * Added the ability to flag entities as `is_risky` within the JSON output when GTI scores or Engine counts meet specified criteria to the following action:

    * **Submit File**



Change

**Google Chronicle** : Version 74.0

  * Reverted the JSON result structure for aggregated queries in the following action:

    * **Execute UDM Query**



## January 21, 2026

Feature

**Okta** : Version 13.0

  * The following new action has been added:

    * **Clear Okta User Session**



Feature

New **Azure API** integration

Change

**Netskope** : Version 14.0

  * Refactored the following action:

    * **Ping**



Change

**HTTP v2** : Version 12.0

  * Updated `Expected Response Values` description in the following action:

    * **Execute HTTP Request**



Change

**Microsoft 365 Defender** : Version 22.0

  * Updated the tracking logic for alerts in the following connector:

    * **Microsoft 365 Defender - Incidents Connector**



Change

**QRadar** : Version 62.0

  * Updated the event processing logic of the following connector:

    * **QRadar Correlations Connector V2**



Change

**Google Chronicle** : Version 73.0

  * Updated the processing of queries in the following action:

    * **Execute UDM Query**



Change

**Google Cloud API** : Version 7.0

  * Updated `Expected Response Values` description in the following action:

    * **Execute HTTP Request**



Change

**Azure Active Directory** : Version 21.0

  * Updated the JSON result example of the following action:

    * **List Members in The Group**
  * Added more metadata to the JSON result example of the following action:

    * **List Groups**



## January 14, 2026

Change

**Siemplify** : Version 100.0

  * Updated the following action to include the JSON result in the action output:

    * **Get Custom Field Values**



Change

**Microsoft Graph Mail** : Version 35.0

  * Improved the "mark emails as read" functionality in the following connector:

    * **Microsoft Graph Mail Connector**



Change

**Microsoft Graph Mail Delegated** : Version 12.0

  * Improved the "mark emails as read" functionality in the following connector:

    * **Microsoft Graph Mail Delegated Connector**



Change

**Okta** : Version 12.0

  * Updated the pagination processing mechanismthe in following action:

    * **List Users**



Change

**Slack** : Version 26.0

  * Updated the Base URL construction logic for the following action:

    * **Build Block**



Change

**Azure Active Directory** : Version 20.0

  * Updated the action to include the email ID in the action output and expanded capabilities to return all metadata fields in the following action:

    * **Get Manager Contact Details**
  * **Integration** : Updated the code to handle special characters in identifiers by implementing URL encoding and OData escaping.




## January 07, 2026

Feature

**Palo Alto Cortex XDR** : Version 21.0

  * The following new job has been added:

    * **Sync Incidents**



Feature

**Microsoft Defender ATP** : Version 27.0

  * The following new action has been added:

    * **Execute Live Response Command**



Change

**Google Chronicle** : Version 72.0

  * Added support for curated rules in the following action:

    * **Get Rule Details**
  * Updated rule severity filter logic in the following connector:

    * **Google Chronicle - Chronicle Alerts Connector**



Change

Updated the dependencies of the following integrations:

  * **BMC Helix RemedyForce** : Version 14.0

  * **EmailV2** : Version 37.0

  * **Google Cloud Storage** : Version 12.0

  * **HTTP v2** : Version 11.0

  * **Jira** : Version 51.0

  * **JuniperVSRX** : Version 9.0

  * **McAfee Active Response** : Version 8.0

  * **PassiveTotal** : Version 12.0

  * **Salesforce** : Version 13.0

  * **SCCM** : Version 18.0

  * **SiemplifyUtilities** : Version 25.0

  * **ThreatConnect** : Version 15.0

  * **Websense** : Version 13.0

  * **WMI** : Version 11.0




Change

**SCC Enterprise** : Version 19.0

  * **Integration** : Refactored code to work with the updated API.



Change

Updated the file management logic of the `Download Attachment From Email` action in the following integrations:

  * **Microsoft Graph Mail** : Version 34.0

  * **Microsoft Graph Mail Delegated** : Version 11.0




Change

**Siemplify** : Version 99.0

  * Updated the TIPCommon method in the following action:

    * **Get Case Details**



Change

**Exchange** : Version 118.0

  * Added new parameters (`Event Fields to Exclude` and `Exclude Attachments`) to the following connectors:

    * **Exchange - Mail Connector v2**

    * **Exchange - Mail Connector v2 with OAuth Authentication**




## December 24, 2025

Feature

New **Proofpoint Cloud Threat Response** integration

Feature

New **OpenSearch** integration

Feature

**Siemplify** : Version 98.0

  * The following new action has been added:

    * **Export Case**



Change

**Fortigate** : Version 17.0

  * Expanded the supported log filter in the following connector:

    * **Fortigate - Threat Logs Connector**



Change

**Google Chronicle** : Version 71.0

  * Updated event processing and ontology mapping in the following connector:

    * **Google Chronicle - Chronicle Alerts Connector**
  * Added support for returning raw logs related to UDM events to the following actions:

    * **Get Detection Details**

    * **Execute UDM Search**




## December 17, 2025

Change

**AWS WAF** : Version 8.0

  * **Integration** : Updated the authentication logic.



Change

**Splunk** : Version 60.0

  * Added support for the latest ES version to the following connector:

    * **Splunk Notable Events Connector**



Change

**Siemplify** : Version 97.0

  * Extended the capabilities of the following action:

    * **Assign Case**
  * Added the ability to add multiple tags using a delimiter to the following action:

    * **Case Tag**
  * Added a JSON result to the following action:

    * **Create Entity**



Change

**Netskope** : Version 13.0

  * **Integration** : Updated the dependencies to include the Netscope SDK library.



Change

**Cofense Triage** : Version 16.0

  * Added the ability to disable the overflow mechanism in the following connector:

    * **Cofense Triage - Reports Connector**



## December 10, 2025

Feature

**Google Threat Intelligence** : Version 7.0

  * The following new action has been added:

    * **Private Submit URL**



Change

**MISP** : Version 34.0

  * Refactored the following actions:

    * **Publish Event**

    * **Unpublish Event**

  * Updated the predefined widget of the following action:

    * **Enrich Entities**



Change

**Siemplify** : Version 96.0

  * Refactored the following action:

    * **Resume Alert SLA**



Change

**Tenable.io** : Version 12.0

  * Updated the entity processing mechanism in the following actions:

    * **List Endpoint Vulnerabilities**

    * **Enrich Entities**

    * **Scan Endpoints**




Change

**Google Chronicle** : Version 70.0

  * Updated the error handling of the API limit and input processing of the following action:

    * **Is Value In Data Table**



## December 04, 2025

Change

**Gmail** : Version 6.0

  * **Integration** : Updated the dependency files.



Change

**Cofense Triage** : Version 15.0

  * Improved category based filtering in the following connector:

    * **Cofense Triage - Reports Connector**



Change

**Tenable Security Center** : Version 19.0

  * **Integration** : Added support to authenticate using an Access Key and a Secret Key.



Change

**CSV** : Version 38.0

  * **Integration** : Updated dependencies.



## November 26, 2025

Feature

**Google Chronicle** : Version 69.0

  * The following new actions have been added:

    * **Generate UDM Query**

    * **Add Entry To Watchlist**




Change

**Jira** : Version 50.0

  * Improved handling of comments with additional styling in the following action:

    * **Add Comment**
  * Improved handling of comments with additional styling in the following job:

    * **Sync Comments**



Change

**Urlscan.io** : Version 27.0

  * Added support for the Domain entity in the following action:

    * **Search For Scans**



Change

Updated the dependency files in the following integrations:

  * **Exchange** : Version 117.0

  * **HTTP V2** : Version 10.0




Change

**CSV** : Version 37.0

  * Updated support for nested JSONs in the following action:

    * **Save Json to CSV**



## November 19, 2025

Feature

**Google Threat Intelligence** : Version 6.0

  * The following new action has been added:

    * **Get Related Associations**



Change

**SentinelOneV2** : Version 44.0

  * Updated the mechanism for fetching agent information in the following actions:

    * **Disconnect Agent From Network**

    * **Enrich Endpoint**

    * **Get Agent Status**

    * **Get Application List For Endpoint**

    * **Get Events For Endpoint Hours Back**

    * **Initiate Full Scan**

    * **Move Agents**

    * **Reconnect Agent To The Network**




Change

**Okta** : Version 11.0

  * Updated the pagination processing mechanism in the following actions:

    * **List Users**

    * **Add Group**

    * **Get Group**

    * **List Providers**




Change

**Google Chronicle** : Version 68.0

  * Improved error handling in the following jobs:

    * **Google Chronicle Sync Job**

    * **Google Chronicle Alerts Creator Job**




Change

**Cofense Triage** : Version 14.0

  * Added the ability to filter based on category to the following connector:

    * **Cofense Triage - Reports Connector**



Change

**Splunk** : Version 59.0

  * Refactored the following integration items to use the new API endpoints:

    * **Ping**

    * **Get Host Events**

    * **Splunk Notable Events Connector**

    * **Sync Splunk ES Closed Events**

    * **Sync Splunk ES Comments**




## November 12, 2025

Change

**Google Security Command Center** : Version 14.0

  * Added the ability to ingest Toxic Combinations and Chokepoints in the following connector:

    * **Google Security Command Center - Findings Connector**



Change

Updated the dependency files in the following integrations:

  * **Microsoft Graph Mail** : Version 33.0

  * **Microsoft Graph Mail Delegated** : Version 10.0




Change

The following integrations are now GUS recommended:

  * **CrowdStrike Falcon** : Version 69.0

  * **Wiz** : Version 3.0

  * **Fortigate** : Version 16.0




Change

**Google Chronicle** : Version 67.0

  * Updated curated detections processing logic in the following action:

    * **Get Detection Details**



Change

**Cybereason** : Version 21.0

  * **Integration** : Added ability to provide a CA Certificate file as part of the configuration.



Change

Updated action definitions to meet the new requirements of IDE in the following integrations:

Updated Integrations (45)

  * **Active Directory** : Version 38.0
  * **AlienVault USM Appliance** : Version 22.0
  * **AlienVault USM Anywhere** : Version 32.0
  * **Area1** : Version 6.0
  * **BulkWhoIs** : Version 16.0
  * **CA Service Desk Manager** : Version 23.0
  * **Carbon Black Response** : Version 35.0
  * **Case Federation** : Version 6.0
  * **ConnectWise** : Version 19.0
  * **CSV** : Version 36.0
  * **DeepSight** : Version 9.0
  * **DomainTools** : Version 9.0
  * **Email V2** : Version 36.0
  * **Endgame** : Version 11.0
  * **Exchange** : Version 116.0
  * **F5 Big IQ** : Version 6.0
  * **FileOperation** : Version 12.0
  * **HTTP** : Version 12.0
  * **IntSights** : Version 23.0
  * **Jira** : Version 49.0
  * **JuniperVSRX** : Version 8.0
  * **McAfee EPO** : Version 17.0
  * **McAfee NSM** : Version 8.0
  * **Microsoft Graph Security** : Version 23.0
  * **MSSQL** : Version 17.0
  * **Palo Alto Next Gen Firewall** : Version 26.0
  * **PhishRod** : Version 4.0
  * **RSA NetWitness** : Version 17.0
  * **Runners** : Version 5.0
  * **Salesforce** : Version 12.0
  * **SCC Enterprise** : Version 18.0
  * **ServiceNow** : Version 59.0
  * **Siemplify** : Version 95.0
  * **SSH** : Version 18.0
  * **Symantec Endpoint Protection** : Version 18.0
  * **Symantec Endpoint Protection 12** : Version 13.0
  * **Symantec ICDX** : Version 7.0
  * **Tenable Security Center** : Version 18.0
  * **Twilio** : Version 14.0
  * **VSphere** : Version 8.0
  * **VirusTotal** : Version 40.0
  * **WildFire** : Version 8.0
  * **WMI** : Version 10.0
  * **XForce** : Version 16.0
  * **Zabbix** : Version 14.0
  * **Zendesk** : Version 10.0



Change

**CrowdStrike Falcon** : Version 69.0

  * Refactored the pagination and filtering mechanism in the following actions:

    * **List Uploaded IOCs**

    * **List Hosts**

  * Added support for wildcards to `File Paths to Scan` in the following action:

    * **On-Demand Scan**



Feature

**Siemplify** : Version 95.0

  * The following new action has been added:

    * **Get Case Alerts**



Feature

New **Azure Monitor** integration

## November 05, 2025

Change

**AWS Identity and Access Management** : Version 7.0

  * Refactored the following actions:

    * **Create User**

    * **Create Group**

    * **Create Policy**

    * **List Users**

    * **List Groups**

    * **List Policies**




Feature

**Palo Alto XDR** : Version 20.0

  * The following new action has been added:

    * **Scan Endpoint**



Change

**Microsoft Teams** : Version 31.0

  * **Integration** : Updated the integration's action definitions to meet the new requirements of the IDE.



Change

**Freshworks Freshservice** : Version 15.0

  * Added the ability to provide a department in the integration configuration for the following action:

    * **Create Ticket**



Change

**FortiAnalyzer** : Version 8.0

  * Updated search processing logic in the following action:

    * **Search Logs**



Feature

**SentinelOneV2** : Version 43.0

  * The following new action has been added:

    * **Get Site Agents**



## October 29, 2025

Change

**CrowdStrike Falcon** : Version 68.0

  * Update the following action to check if there is an existing identical running scan for a provided hostname before creating a new one:

    * **On-Demand Scan**



Change

**Microsoft Graph Mail** : Version 32.0

  * Updated the file management logic in the following action:

    * **Download Attachments from Email**



Change

**Exchange** : Version 115.0

  * Updated the file management logic in the following action:

    * **Download Attachments**



Change

**CSV** : Version 35.0

  * Updated file path processing logic in the following connector:

    * **CSV Connector**



Change

**Microsoft Graph Mail Delegated** : Version 9.0

  * Updated the file management logic in the following action:

    * **Download Attachments from Email**



Change

**ZScaler** : Version 10.0

  * Added support for domain entity type in the following actions:

    * **Add to Whitelist**

    * **Lookup Entity**




Change

**Tanium** : Version 15.0

  * (REGRESSIVE) Updated JSON result to return data for multiple columns in the following action:

    * **Get Question Results**



Change

**Palo Alto Cortex XDR** : Version 19.0

  * Updated incident processing logic in the following action:

    * **Get Incident Details**
  * Added new filtering options, the ability to create a SecOps alert for every Palo Alto XDR alert, and the ability to track updates to an incident in the following connector:

    * **Palo Alto Cortex XDR Connector**



## October 22, 2025

Change

**DomainTools** : Version 8.0

  * Extended capabilities in the following action:

    * **Get Domain Risk**
  * Added support for the domain entity type in the following actions:

    * **Get Domain Profile**

    * **Get Domain Risk**

    * **Reverse Domain**




Change

**CSV** : Version 34.0

  * Fixed a bug that caused inconsistent column order for the same JSON input by stabilizing the order based on the keys of the first object in the list in the following action:

    * **Save Json to CSV**



Feature

**SentinelOneV2** : Version 42.0

  * The following new actions have been added:

    * **Create Device Control Rule**

    * **Delete Device Control Rule**

    * **Update Device Control Rule**




Change

**CrowdStrike Falcon** : Version 67.0

  * Fixed a bug where the Contains filter would fail to find hosts when the `Max Hosts To Return` limit was applied in the following action:

    * **List Host**



## October 15, 2025

Feature

**CrowdStrike Falcon** : Version 66.0

  * The following new action has been added:

    * **Get Alert Details**



Change

**ThreatQ** : Version 15.0

  * Updated the API request payload to align with a change in the ThreatQ API in the following actions:

    * **Enrich IP**

    * **Enrich URL**

    * **Enrich Email**

    * **Enrich Hash**

    * **Enrich CVE**




Change

**UrlScan.io** : Version 26.0

  * Added ability to scan domains and IPs in the following action:

    * **URL Check**



Change

Updated dependencies in the following integrations:

  * **Microsoft Teams** : Version 30.0

  * **Microsoft Graph Mail Delegated** : Version 8.0

  * **Exchange** : Version 114.0

  * **Case Federation** : Version 5.0

  * **Azure Security Center** : Version 12.0




Change

**Azure Active Directory** : Version 19.0

  * Improved performance by implementing a direct API filter query for group name searches, which avoids fetching all groups and significantly reduces execution time in large-group environments, in the following action:

    * **List Members in Group**



Change

**CrowdStrike Falcon** : Version 66.0

  * Updated entity processing logic in the following actions:

    * **Contain Endpoint**

    * **Download File**

    * **Execute Command**

    * **Get Host Information**

    * **Lift Contained Endpoint**

    * **List Host Vulnerabilities**

    * **On-Demand Scan**

    * **Run Script**




Change

**Okta** : Version 10.0

  * Updated the pagination processing mechanism in the following actions:

    * **List Users**

    * **Add Group**

    * **Get Group**

    * **List Providers**




Change

**Microsoft Teams** : Version 30.0

  * **Integration** : Fixed an issue with the special characters in the query parameters.



## October 09, 2025

Change

**Microsoft Teams** : Version 29.0

  * Refactored action logic in the following actions:

    * **Get Authorization**

    * **Generate Token**




Change

**Google Chronicle** : Version 66.0

  * Updated processing of reference list rows in the following action:

    * **Get Reference Lists**



Change

**Google Threat Intelligence** : Version 5.0

  * Added ability to filter by issue name in the following connector:

    * **Google Threat Intelligence - ASM Issues Connector**
  * Added ability to filter events in the following connector:

    * **Google Threat Intelligence - DTM Alerts Connector**



Change

**Google Workspace** : Version 22.0

  * Updated the action description to reflect that the action deletes the extension from the blocklist rather than deleting the extension from the organizational unit in the following action:

    * **Delete Extension**



## September 25, 2025

Feature

**Microsoft Azure Sentinel** : Version 57.0

  * The following new job has been added:

    * **Sync Incidents**



Change

**Google Chronicle** : Version 65.0

  * Updated the filtering mechanism of the following action:

    * **Get Data Tables**



Feature

New **Apache Kafka** integration

Change

**Google Workspace** : Version 21.0

  * Expanded capabilities of the following action:

    * **List OU Of Account**
  * Updated processing of the organization unit inside the following actions:

    * **Block Extension**

    * **Delete Extension**

    * **List OU Of Account**




Change

**CrowdStrike Falcon** : Version 64.0

  * Updated timeout handling in the following connector:

    * **Crowdstrike Falcon - Streaming Events Connector**
  * **Integration** : Updated authentication to support multi-tenancy execution.




Change

**Any.Run** : Version 8.0

  * Updated the available privacy settings in the following actions:

    * **Analyze URL**

    * **Analyze File URL**

    * **Analyze File**




Change

**Orca Security** : Version 12.0

  * **Integration** : (REGRESSIVE) Updated to support the latest API version.

Ontology has been updated. Overwrite current ontology mapping to align with the new API alert structure. 




## September 17, 2025

Feature

**Google Threat Intelligence** : Version 4.0

  * The following new action has been added:

    * **Set DTM Alert Analysis**



Feature

**Palo Alto Cortex XDR** : Version 18.0

  * The following new actions have been added:

    * **Add Comment To Incident**

    * **Execute XQL Search**

    * **Get Incident Details**




Feature

**SentinelOneV2** : Version 41.0

  * The following new action has been added:

    * **Update Alert**
  * The following new connector has been added:

    * **SentinelOne - Alert Connector**
  * A new predefined widget has been added to the following action:

    * **Update Alert**



Change

**Microsoft Azure Sentinel** : Version 56.0

  * Updated mapping for the `ScheduledAlert` event types in the following connector:

    * **Microsoft Azure Sentinel Incident Connector v2**



Change

**Jira** : Version 48.0

  * **Integration** : Updated the SDK version.



Change

**Trend Vision One** : Version 6.0

  * Added support for Agent UUID in the following actions:

    * **Enrich Entities**

    * **Execute Custom Script**

    * **Isolate Endpoint**

    * **Unisolate Endpoint**




Change

**Vertex AI** : Version 4.0

  * **Integration** : Increased the default timeout for API requests.



Change

Added the ability to modify the `API Root` and `Login API Root` in the following integrations:

  * **Azure Active Directory** : Version 18.0

  * **Azure AD Identity Protection** : Version 7.0

  * **Microsoft Teams** : Version 28.0




Change

**Splunk** : Version 58.0

  * Updated the alert processing logic in the following connector:

    * **Splunk ES - Notable Events Connector**



Change

**Google Threat Intelligence** : Version 4.0

  * Updated the processing of the threat actor entity in the following action:

    * **Enrich Entities**
  * Updated the predefined widget in the following actions:

(REGRESSIVE) The widget now works with GTI information. To see the changes, the widget must be re-added to the existing views in playbooks.

    * **Enrich Entities**

    * **Enrich IOCs**

  * Added JSON samples to the following action:

    * **Enrich Entities**



## September 03, 2025

Change

**Google Threat Intelligence** : Version 3.0

  * Extended supported filters in the following connector:

    * **Google Threat Intelligence - ASM Issues Connector**



## August 27, 2025

Feature

**Google Workspace** : Version 20.0

  * The following new actions have been added:

    * **Block Extension**

    * **Delete Extension**

    * **Get Extension Details**

    * **Get Host Browser Details**

    * **Search User Activity Events**




Change

**Google Threat Intelligence** : Version 3.0

  * **Integration:** Updated authentication flow.



## August 20, 2025

Change

**Google Chronicle** : Version 64.0

  * Added support for aggregated searches in the following action:

    * **Execute UDM Query**



Change

**Microsoft Graph Mail** : Version 30.0

  * Improved handling of `Case Name Template` in the following connector:

    * **Microsoft Graph Mail - Microsoft Graph Mail Connector**



Change

**CrowdStrike Falcon** : Version 63.0

  * Updated processing of `On-Demand Scan` alerts in the following connector:

    * **Crowdstrike Falcon - Alerts Connector**



Change

**Microsoft Graph Mail Delegated** : Version 6.0

  * Improved handling of `Case Name Template` in the following connector:

    * **Microsoft Graph Mail Delegated - Microsoft Graph Mail Delegated Connector**



## August 13, 2025

Feature

New **CyberArk Credential Provider** integration

Change

**Microsoft Graph Mail** : Version 29.0

  * **Integration** : Updated dependencies.



Change

**Jira** : Version 47.0

  * Updated timestamp processing logic in the following jobs:

    * **Sync Comments**

    * **Sync Closure**

  * Updated logic for processing closed tickets in the following job:

    * **Sync Closure**



## August 04, 2025

Feature

**Google Chronicle** : Version 63.0

  * The following new actions have been added:

    * **Ask Gemini**
    * **Enrich Entities**



Change

**QRadar** : Version 60.0

  * Updated offense processing logic in the following connector:

    * **Qradar - Baseline Offenses Connector**



Change

**Gmail** : Version 5.0

  * **Integration** : Improved error handling.



Change

**Google Chronicle** : Version 63.0

  * The following actions have been deprecated:

    * **Enrich Domain**
    * **Enrich IP**



Change

**Case Federation** : Version 4.0

  * **Integration:** Refactored the code.



Change

**SentinelOneV2** : Version 40.0

  * Added ability to fetch agent information in the following actions:

    * **Disconnect Agent From Network**
    * **Enrich Endpoint**
    * **Get Agent Status**
    * **Get Application List For Endpoint**
    * **Get Events For Endpoint Hours Back**
    * **Initiate Full Scan**
    * **Move Agents**
    * **Reconnect Agent To The Network**



## July 23, 2025

Feature

**Siemplify** : Version 94.0

  * The following new actions have been added:

    * **Get Custom Field Values**

    * **Resume Case SLA**

    * **Pause Case SLA**




Change

**Sophos** : Version 18.0 

Added ability to work with new authentication method in the following action:

  * **Get Events Log**



## July 16, 2025

Feature

**Google Chronicle** : Version 62.0

  * The following new actions have been added:

    * **Remove Rows From Data Table**

    * **Get Data Tables**

    * **Is Value In Data Table**

    * **Add Rows To Data Table**




Change

**Microsoft Azure Sentinel** : Version 55.0

  * Updated logger initialization in the following connector:

    * **Microsoft Azure Sentinel - Incident Connector v2**



Change

**Azure Security Center** : Version 11.0

  * **Integration** : Refactored the integration code to support the updated API.



Change

**MySQL** : Version 5.0

  * Refined query processing in the following action:

    * **Run SQL Query**



Change

**Mandiant Threat Intelligence** : Version 14.0

  * Improved entity processing logic in the following action:

    * **Enrich Entities**



## July 09, 2025

Change

**Siemplify** : Version 93.0

  * Updated action logic in the following actions:

    * **Get Case Details**

    * **Get Similar Cases**




Change

**BMC Remedy ITSM** : Version 9.0

  * Updated input parameter processing in the following action:

    * **Create Incident**



Change

**ServiceNow** : Version 58.0

  * Updated processing of record object in the following connector:

    * **ServiceNow - ServiceNow Connector**



## July 02, 2025

Feature

**Okta** : Version 9.0

  * The following new action has been added:

    * **Send SSF to Okta**



Change

**Vertex AI** : Version 3.0

  * **Integration** : Updated the handling of non-Google models.



Change

**CrowdStrike Falcon** : Version 62.0

  * Updated JSON Result structure in the following action:

    * **List Hosts**



Change

**Google Chronicle** : Version 61.0

  * Updated action processing logic in the following action:

    * **Execute UDM Query**



## June 27, 2025

Change

**Siemplify** : Version 92.0

  * Updated action logic in the following actions:

    * **Get Case Details**

    * **Get Similar Cases**

    * **Update Case Description**




## June 25, 2025

Change

Refactored the code to work with updated API in the following integrations:

  * **Case Federation** : Version 3.0

  * **Siemplify** : Version 91.0




Change

**Siemplify** : Version 91.0

  * Updated Predefined Widget in the following action:

    * **Get Similar Cases**



Change

**Microsoft Azure Sentinel** : Version 54.0

  * Added an ability to not process the alert until Scheduled/NRT alert objects are available from API in the following connectors:

    * **Microsoft Azure Sentinel - Incident Connector v2**

    * **Microsoft Azure Sentinel - Incident Tracking Connector**




Change

**SentinelOneV2** : Version 39.0

  * Updated ontology mapping in the following connector:

    * **SentinelOneV2 - Threats Connector**



## June 18, 2025

Change

**Microsoft Teams** : Version 27.0

  * **Integration** : Refactored the code to work with updated API.



Change

**Google Chronicle** : Version 60.0

  * Updated risk score handling in the following connector:

    * **Google Chronicle - Alerts Connector**



## June 11, 2025

Feature

New **Google Threat Intelligence** integration

Feature

New **Akamai** integration

Change

Refactored the code to work with updated API in the following integrations: 

  * **Exchange** : Version 113.0
  * **ServiceNow** : Version 57.0
  * **Microsoft Graph Mail Delegated** : Version 5.0



Refactored the code in the following integrations: 

  * **Gmail** : Version 4.0
  * **Google Cloud API** : Version 6.0
  * **HTTP v2** : Version 9.0
  * **Microsoft Graph Mail** : Version 28.0
  * **Tor** : Version 7.0



Change

**Darktrace** : Version 18.0

  * Added ability to filter model breaches by priority in the following connector:

    * **Darktrace - Model Breaches Connector**



## June 04, 2025

Change

Refactored the code to work with updated API in the following integrations:

  * **BMC Remedy ITSM** : Version 8.0
  * **Gmail** : Version 3.0
  * **Google Cloud API** : Version 5.0
  * **Microsoft Graph Mail** : Version 27.0
  * **Service Desk Plus V3** : Version 6.0
  * **Vertex AI** : Version 2.0



Change

**Google Chronicle** : Version 59.0

  * Updated the API root to be configurable in IDE in the following connector: 
    * **Google Chronicle - Chronicle Alerts Connector**



Change

**Vertex AI** : Version 2.0

  * Fixed non-Google models that weren't working



Change

**Nmap** : Version 2.0

  * Updated JSON Result structure in the following action: 
    * **Scan Entities**



## May 28, 2025

Feature

New **Nmap** integration

Change

**Sophos** : Version 17.0

  * Updated the logic of entity processing in the following actions: 
    * **Isolate Endpoint**
    * **Unisolate Endpoint**



Change

**Office 365 CloudApp Security** : Version 22.0

  * Updated processing of the input parameters in the following actions:

    * **Bulk Resolve Alert**
    * **Close Alert**
    * **Dismiss Alert**



Change

**Trend Vision One** : Version 5.0

  * Updated the logic for processing alerts in the following connector: 
    * **Trend Vision One - Workbench Alerts**



Change

**Mandiant Threat Intelligence** : Version 13.0

  * Updated entity processing in the following action:

    * **Enrich Entities**



Change

**Microsoft 365 Defender** : Version 21.0

  * Added more transparency around Microsoft Sentinel and Microsoft Defender For Cloud alerts. You can now provide `microsoftSentinel` and `microsoftDefenderForCloud` as the Service Source in the following connector: 
    * **Microsoft 365 Defender - Incidents Connector**



## May 21, 2025

Change

**Palo Alto Cortex XDR** : Version 17.0

  * Updated the supported statuses in the following action:

    * **Update an Incident**



Change

**Microsoft Azure Sentinel** : Version 53.0

  * Updated entity mapping in the following connectors:

    * **Microsoft Azure Sentinel - Incident Connector v2**

    * **Microsoft Azure Sentinel - Incident Tracking Connector**




Change

**Google Chronicle** :Version: 58.0

  * Updated the following action:

    * **Broken Google Chronicle Widget**
  * Expanded the JSON Result with new fields in the following connector:

    * **Google Chronicle** \- Get Rule Details



## May 14, 2025

Feature

**ProofPoint TAP** : Version 11.0

  * The following new actions have been added:

    * **Get Threat Forensics**

    * **Search Events**

    * **List Campaigns**




Change

**Google Chronicle** : Version 57.0

  * Updated the processing of the events in the following connector:

    * **Google Chronicle - Chronicle Alerts Connector**



## May 07, 2025

Feature

**CrowdStrike Falcon** : Version 61.0

  * The following new action has been added:

    * **Search Events**



Feature

New **Cisco Vulnerability Management** integration

Change

**Microsoft Azure Sentinel** : Version 52.0

  * Updated events processing logic in the following connectors:

    * **Microsoft Azure Sentinel - Incident Connector v2**

    * **Microsoft Azure Sentinel - Incident Tracking Connector**




Change

**CrowdStrike Falcon** : Version 61.0

  * Updated input parameter processing in the following action:

    * **On-Demand Scan**
  * Added ability to define Alert Name and Case Name templates in the following connectors:

    * **Crowdstrike Falcon - Detections Connector**

    * **Crowdstrike Falcon - Identity Protection Detections Connector**

    * **Crowdstrike Falcon - Alerts Connector**




Change

**CrowdStrike Falcon** : Version 61.0

  * Updated input parameter processing in the following action:

    * **On-Demand Scan**
  * Added ability to define Alert Name and Case Name templates to the following connectors:

    * **Crowdstrike Falcon - Detections Connector**

    * **Crowdstrike Falcon - Identity Protection Detections Connector**

    * **Crowdstrike Falcon - Alerts Connector**




Change

**Google Chronicle** : Version 56.0

  * Added ignore \r\n characters and skip empty input values when adding in the following actions:

    * **Is Value in Reference List**

    * **Add Value to Reference List**

  * Optimised the processing of the alerts in the following jobs:

    * **Alerts Sync**

    * **Alerts Creator**




**Microsoft Azure Sentinel** : Version 52.0

  * Updated events processing logic in the following connectors:

    * **Microsoft Azure Sentinel - Incident Connector v2**

    * **Microsoft Azure Sentinel - Incident Tracking Connector**




**Microsoft Graph Mail** : Version 26.0

  * Added ability to define `Alert Name Template` in the following connector:

    * **Microsoft Graph Mail - Microsoft Graph Mail Connector**



**Microsoft Graph Mail Delegated** : Version 26.0

  * Added ability to define `Alert Name Template` in the following connector:

    * **Microsoft Graph Mail Delegated - Microsoft Graph Mail Delegated Connector**



Change

**Google Chronicle** : Version 56.0

  * Added ignore \r\n characters and skip empty input values when adding to the following actions:

    * **Is Value in Reference List**

    * **Add Value to Reference List**

  * Optimized the processing of the alerts in the following jobs:

    * **Google Chronicle - Alerts Sync**

    * **Google Chronicle - Alerts Creator**




Change

**Microsoft Graph Mail** : Version 26.0

  * Added ability to define Alert Name Template in the following connector:

    * **Microsoft Graph Mail - Microsoft Graph Mail Connector**



Change

**Microsoft Graph Mail Delegated** : Version 4.0

  * Added ability to define Alert Name Template in the following connector:

    * **Microsoft Graph Mail Delegated - Microsoft Graph Mail Delegated Connector**



## April 30, 2025

Feature

**Mimecast** : Version 12.0

  * The following new action has been added:

    * **Create Block Sender Policy**



Change

**VirusTotalV3** : Version 37.0

  * Updated entity handling of the following actions:

    * **Add Comment To Entity**

    * **Add Vote To Entity**

    * **Enrich URL**

    * **Get Domain Details**

    * **Get Related Domains**

    * **Get Related Hashes**

    * **Get Related IPs**

    * **Get Related URLs**

  * Updated Predefined Widgets in the following actions:

    * **Add Comment To Entity**

    * **Add Vote To Entity**

    * **Enrich URL**

    * **Get Domain Details**

    * **Get Related Domains**

    * **Get Related Hashes**

    * **Get Related IPs**

    * **Get Related URLs**




Change

**HTTP v2** : Version 8.0

  * **Integration** : Refactored the code to work with updated API.



Change

**SentinelOneV2** : Version 38.0

  * The underlying API endpoint of the following action has been **deprecated** and there is no suitable replacement:

    * **Get Hash Reputation**
  * Refactored the code of the following connector:

    * **SentinelOneV2 - Get Events For Endpoint Hours Back**



Change

**Mimecast** : Version 12.0

  * Added ability to ingest attachments and body associated with the held message to the following connector:

    * **Mimecast - Message Tracking Connector**
  * Added ability to filter by queue reason to the following connector:

    * **Mimecast - Message Tracking Connector**



## April 23, 2025

Feature

**ExtraHop** : Version 6.0

  * The following new action has been added:

    * **Update Detection**



Feature

**Zerofox** : Version 2.0

  * The following new action has been added:

    * **Add Evidence To Alert**



Change

**Tanium** : Version 14.0

  * Improved action compatibility with Python 3.11 in the following action:

    * **Download File**



Change

**Siemplify** : Version 90.0

  * Added ability to work with additional timestamp types in the following action:

    * **Permitted Alert Time**
  * Added ability to work with IANA timezone names in the following action:

    * **Permitted Alert Time**



Change

**Microsoft Graph Mail** : Version 25.0

  * Updated event structure for the attached emails in the following connector:

    * **Microsoft Graph Mail - Microsoft Graph Mail Connector**



Change

**SCC Enterprise** : Version 17.0

  * Updated ticket creation workflow in the following action:

    * **Create SCC Enterprise Cloud Posture Ticket Type Jira**



Change

**Microsoft Graph Mail Delegated** : Version 3.0

  * Updated event structure for the attached emails in the following connector:

    * **Microsoft Graph Mail Delegated - Microsoft Graph Mail Delegated Connector**



## April 16, 2025

Change

**Microsoft Graph Security** : Version 22.0

  * **Integration** : Added support for V2 version of the API. 

**Note:** The support needs to be enabled in the connectors and integration. Connector behavior changes on the new API; note filter configuration. New permissions to work with V2 API need to be provided.



Change

**Microsoft Graph Mail** : Version 24.0

  * **Integration** : Added support for working with S/MIME-encrypted emails.

  * Added Connector API throttling improvements to accommodate `Max Emails per Cycle` logic in the following connector:

    * **Microsoft Graph Mail - Microsoft Graph Mail Connector**



Change

**Google Chronicle** : Version 55.0

  * Added ability to ingest composite alerts in the following connector:

    * **Google Chronicle - Alerts Connector**
  * Removed the `Disable Event Splitting` parameter so the connector will always ingest events in the original structure in the following connector and ontology mapping must be updated:

    * **Google Chronicle - Alerts Connector**



Change

**CrowdStrike Falcon** : Version 60.0

  * Added ability to fetch hidden alerts in the following connector:

    * **CrowdStrike - Alerts Connector**



Change

**ServiceNow** : Version 56.0

  * Improved handling of OAuth 2.0 authentication in the following actions:

    * **Create Incident**
    * **Create Alert Incident**



## April 09, 2025

Feature

New **Zerofox** integration.

Change

**VirusTotalV3** : Version 36.0

  * Updated private submission is_risky logic in the following action:

    * **Submit File**



Change

**Web Risk** : Version 2.0

  * Updated entity handling in the following action:

    * **Enrich Entities**



Change

**Siemplify** : Version 89.0

  * Removed the following unsupported job:

    * **Siemplify - ETL Monitor Job**



Change

**VMware Carbon Black Cloud** : Version 36.0

  * Updated the ingestion processing logic in the following connector:

    * **VMware Carbon Black Cloud - Alerts and Events Baseline Connector**



Change

**Exchange** : Version 112.0

  * Added an option to overwrite the URL regex connectors use in the following connectors:

    * **Exchange - Mail Connector v2**
    * **Exchange - Mail Connector v2 with OAuth Authentication**



## April 02, 2025

Change

**Exchange** : Version 111.0

  * Improved encoding handling during email parsing in the following connectors:

    * **Exchange - Mail Connector v2**

    * **Exchange - Mail Connector v2 with Oauth Authentication**




Change

**VMRay** : Version 17.0

  * Updated entity handling in the following action:

    * **Scan URL**



Change

**ServiceNow** : Version 55.0

  * Added support for `Sync Closed Incidents` job to handle created incidents in the following actions:

    * **Create Incident**

    * **Create Alert Incident**

  * Added ability to filter records by assignment group in the following connector:

    * **ServiceNow - ServiceNow Connector**
  * Added ability to sync incidents created during playbook execution in the following job:

    * **Sync Closed Incidents**



Change

**Siemplify** : Version 88.0

  * Removed the following unsupported job from the integration:

    * **Jobs Monitor**



Change

**Google Chronicle** : Version 54.0

  * Updated the following connector to support new SIEM API:

    * **Google Chronicle - Alerts Connector**
  * Updated the following jobs to support new SIEM API:

    * **Sync**

    * **Alerts Creator**

  * Added ability to authenticate via Workload Identity in the following connector:

    * **Google Chronicle - Alerts Connector**
  * Added ability to authenticate via Workload Identity in the following connector in the following jobs:

    * **Sync**

    * **Alerts Creator**




Change

**Microsoft Azure Sentinel** : Version 51.0

  * **Integration** : Updated the integration code to work with Python version 3.11.

**Important:** To ensure compatibility and avoid disruptions, follow the best practices in [Upgrade Python versions](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/upgrade-python-versions).
  * Added an option to create additional SecOps events for all Sentinel Incident's entities in the following connectors:

    * **Microsoft Azure Sentinel - Incident Connector v2**

    * **Microsoft Azure Sentinel - Incident Tracking Connector**

  * Improved tracking of Microsoft Sentinel Incident's entities (if the connector can't fetch events for Sentinel's Scheduled alerts or NRT-based incidents, it will attempt to fetch Incident's entities instead) in the following connectors:

    * **Microsoft Azure Sentinel - Incident Connector v2**

    * **Microsoft Azure Sentinel - Incident Tracking Connector**

  * Improved handling of Microsoft Sentinel incidents IDs in connectors backlog in the following connectors:

    * **Microsoft Azure Sentinel - Incident Connector v2**

    * **Microsoft Azure Sentinel - Incident Tracking Connector**




Change

**Microsoft Graph Mail** : Version 23.0

  * **Integration** : Added support for working with S/MIME-encrypted emails.

  * The code base was refactored in the following connector:

(REGRESSIVE) As part of the refactor, connector's `Tenant (Directory) ID` parameter has been updated to a `Microsoft Entra ID Directory ID`, this will require re-entering connector's configuration parameters after the update.

    * **Microsoft Graph Mail - Microsoft Graph Mail Connector**



Change

**Jira** : Version 46.0

  * Updated the following jobs:

    * **Sync Closure**

    * **Sync Comments**




Change

**CrowdStrike Falcon** : Version 59.0

  * Updated input handling for the following actions:

    * **Update Identity Protection Detection**

    * **Add Identity Protection Detection Comment**




Change

**ExtraHop** : Version 5.0

  * Updated alert processing logic in the following connector:

    * **Extrahop - Detections Connector**



## March 26, 2025

Change

**Microsoft Graph Security** : Version 21.0

  * Updated the handling of alerts in the following connector:

    * **Microsoft Graph Security - Office 365 Security and Compliance Connector**



Change

**Cisco Firepower Management Center** : Version 7.0

  * **Integration** : Added pagination mechanism support.



Change

**Siemplify** : Version 87.0

  * Removed the following unsupported job from the integration:

    * **Connectors Monitor**



Change

**MSSQL** : Version 16.0

  * **Integration** : Integration updates.



Change

**SCC Enterprise** : Version 16.0

  * **Integration** : Added support for regionalized environments.



Change

**Exchange** : Version 110.0

  * **Integration** : Dependencies update.



Change

**Google Chronicle** : Version 53.0

  * Propagate SIEM data access scope in the following connector:

    * **Google Chronicle - Alerts Connector**
  * Updated predefined widget in the following action:

    * **Get Detection Details**



Change

**Cofense Triage** : Version 13.0

  * **Integration** : (REGRESSIVE) Updated alerts and events time mappings.



## March 19, 2025

Change

**Jira** : Version 45.0

  * Added support for integration's sync jobs to handle created issues in the following actions:

    * **Create Issue**

    * **Create Alert Issue Actions**

  * Added support to handle issues created by the `Create Issue` and `Create Alert Issue` actions in the following jobs:

    * **Sync Closure**

    * **Sync Comments Jobs**




Change

**ServiceNow** : Version 54.0

  * Added ability to provide custom fields as JSON objects in the following actions:

    * **Create Incident**

    * **Update Incident**




Change

**Exchange** : Version 109.0

  * **Integration** : Added support for working with S/MIME-encrypted emails.



Change

**Zoho Desk** : Version 8.0

  * Updated the user searching mechanism in the following action:

    * **Create Ticket**



## March 12, 2025

Feature

New **Sysdig Secure** integration

Feature

New **Web Risk** integration

Change

**Mandiant Threat Intelligence** : Version 12.0

  * Updated predefined widgets in the following actions:

    * **Enrich Entities**

    * **Enrich IOCs**

    * **Get Malware Details**




Change

**Varonis Data Security Platform** : Version 5.0

  * **Integration** : Updated dependencies.



Change

**Mandiant** : Version 8.0

  * Updated predefined widgets in the following actions:

    * **Enrich Entities**

    * **Enrich IOCs**

    * **Get Malware Details**




Change

**Mimecast** : Version 11.0

  * (DEPRECATED) No replacement API endpoint in new API in the following action:

    * **Report Message**
  * **Integration** : Migrated integration to work with the latest API version.

  * **Integration** : Added client credentials authentication.




## March 05, 2025

Change

**CrowdStrike Falcon** : Version 58.0

  * Added ability to provide a hostname from the input parameters in the following actions:

    * **On-Demand Scan**

    * **Execute Command**

    * **Run Script**




Change

**Microsoft Azure Sentinel** : Version 50.0

  * Improved the connector logging and the API timeout handling in the following connector:

    * **Microsoft Azure Sentinel - Incident Connector v2**



Change

**Exchange** : Version 108.0

  * **Integration** : Updated the integration.



Change

**Google Chronicle** : Version 52.0

  * Updated severity handling in the following connector:

    * **Google Chronicle - Alerts Connector**
  * **Integration** : Updated the integration dependencies.

  * Error handling improvements in the following job:

    * **Alerts Creator**



Change

**SiemplifyUtilities** : Version 24.0

  * Added ability to disable JSON data escaping in the following action:

    * **Filter JSON**



Change

**VirusTotalV3** : Version 35.0

  * Updated the comment fetching logic in the following action:

    * **Submit File**



## February 26, 2025

Feature

**Siemplify** : Version 86.0

  * The following new actions have been added:

    * **Wait For Custom Fields**

    * **Set Custom Fields**

    * **Create Gemini Case Summary**




Feature

New **Microsoft Graph Mail Delegated** integration

Change

**HTTP v2** : Version 7.0

  * **Integration** : Updated the integration to work without authentication.



Change

**Anomali** : Version 12.0

  * **Integration** : Updated the API authentication.



Change

**Mandiant ASM** : Version 9.0

  * **Integration** : Updated handling of the ASM Project.



## February 24, 2025

Change

**Siemplify** : Version 85.0

  * Updated input handling in the following case:

    * **Close Case**



## February 19, 2025

Change

**Carbon Black Response** : Version 34.0

  * Fixed the issue with data type of the `Version` parameter in the following connector:

    * **Carbon Black Response - Carbon Black Response Connector**



Change

**Netskope** : Version 12.0

  * **Integration** : Integration updated to support latest Netskope API updates

**Note:** The integration needs to be configured with V1 and V2 API Tokens, to support actions that are working with V1 endpoints, and actions that work with newer, V2 endpoints. For more information, see the following Netskope article - https://docs.netskope.com/en/netskope-product-eol-announcements/#eol-for-specific-rest-api-v1-endpoints-1



Change

**Splunk** : Version 57.0

  * **Integration** : Updated Dependencies.



Change

**Microsoft Graph Mail** : Version 22.0

  * Added the ability to control the action's JSON result behavior in the following actions:

    * **Search Emails**

    * **Move Email To Folder**

    * **Delete Email**

    * **Wait For Email From User**

  * **Integration** : Improved localization support and better handling of the internetMessageID filter.

  * **Integration** : Improved integration configuration validation.




Change

**Exchange** : Version 107.0

  * **Integration** : Updated external package dependencies.



## February 12, 2025

Change

**Microsoft 365 Defender** : Version 20.0

  * Added ability to disable alert tracking in the following connector:

    * **Microsoft 365 Defender - Incidents Connector**



Change

**Google Chronicle** : Version 51.0

  * Improved Connector Logs To Notify On Possible Ingestion Delays in the following connector:

    * **Google Chronicle - Alerts Connector**
  * Updated OOTB mapping in the following connector:

New mapping allows you to have "Disable Event Splitting" enabled and still have all entities mapped out.

    * **Google Chronicle - Alerts Connector**



Change

**Snowflake** : Version 6.0

  * **Integration** : Updated integration to use the latest API version.



## February 07, 2025

Change

**Google Chronicle** : Version 50.0

  * Improved events time format conversion handling in the following job:

    * **Google Chronicle - Alerts Creator**



## February 05, 2025

Feature

**Google Workspace** : Version 19.0

  * The following new action has been added:

    * **Revoke User Sessions**



Feature

**Google BigQuery** : Version 15.0

  * The following new action has been added:

    * **Run Custom Query**



Change

**CrowdStrike Falcon** : Version 57.0

  * Updated predefined widgets in the following actions:

    * **Get Host Information**

    * **List Host Vulnerabilities**




Change

**Google BigQuery** : Version 15.0

  * Updated error handling in the following action:

    * **Run SQL Query**



Change

**ServiceNow** : Version 53.0

  * Improved support for updating custom fields in the following action:

    * **Update Incident**



Change

**McAfee ESM** : Version 43.0

  * **Integration** : Added support for the 11.6.13 and later product versions. 

**Note:** Make sure to enable "Use AES Encryption".



Change

**Microsoft Graph Mail** : Version 21.0

  * Improved email processing in the following actions:

    * **Wait For Email From User**

    * **Wait For Vote Email Results**




Change

**QRadar** : Version 59.0

  * Updated the storage of fetched offenses IDs in the following connectors:

    * **Qradar - Correlation Events Connector V2**

    * **Qradar - Offenses Connector**

**Note:** It is recommended to re-create related connectors after the integration update to avoid data inconsistencies.



Change

**VMware Carbon Black Cloud** : Version 35.0

  * Updated predefined widgets in the following actions:

    * **List Host Vulnerabilities**

    * **Enrich Entities**




## January 29, 2025

Feature

New **Vertex AI** integration

Change

**Mandiant Managed Defense** : Version 3.0

  * Added ability to provide padding time and updated error handling for the following connector:

    * **Mandiant Managed Defense - Investigations Connector**



Change

**Splunk** : Version 56.0

  * **Integration** : Updated authentication handling.



Change

**Google Chronicle** : Version 49.0

  * Updated default configuration for event splitting in the following connector:

    * **Google Chronicle - Alerts Connector**
  * **Integration** : Updated actions to support the new SIEM API and the ability to authenticate using the `Workload Identity Email`.

**Note:** JSON results are different on the new SIEM API.
  * Updated predefined widgets in the following actions:

    * **Lookup Similar Alerts**

    * **Get Rule Details**

    * **Execute UDM Query**

    * **Get Detection Details**




## January 22, 2025

Feature

**Siemplify** : Version 83.0

  * The following new action has been added:

    * **Get Case Details**
  * Added a new predefined widget to the following action:

    * **Get Case Details**



Change

**Exchange** : Version 106.0

  * Improved handling of email ingestion in the following connecxtors:

    * **Exchange - Mail Connector v2**

    * **Exchange - Mail Connector v2 With Oauth Authentication**




## January 15, 2025

Change

**Fortigate** : Version 15.0

  * **Integration** : Updated authentication to be aligned with new API best practices.



Change

**Google Kubernetes Engine** : Version 7.0

  * **Integration** : Added ability to provide API Root and location in the integration configuration.



Change

**Freshworks Freshservice** : Version 14.0

  * Added ability to define the workspace in the following action:

    * **List Tickets**
  * Added ability to define the workspace in the following connector:

    * **Freshworks Freshservice - Tickets Connector**



Change

**Orca Security** : Version 11.0

  * Added ability to work with Orca Score in the following connecctor:

    * **Orca Security - Alerts Connector**



Change

**Google Chronicle** : Version 48.0

  * Updated ontology mapping in the following connector:

    * **Google Chronicle - Alerts Connector**



Change

**ThreatConnect** : Version 14.0

  * **Integration** : Updated integration configuration parameters.



Change

**SentinelOneV2** : Version 37.0

  * Fixed IDs file handling and added an ability to disable the overflow mechanism in the following connector:

    * **SentinelOne - Threats Connector**



Change

**Palo Alto Next Gen Firewall** : Version 25.0

  * **Integration** : Authorization method aligned to latest PanOS versions.



## January 09, 2025

Change

**Exchange** : Version 105.0

  * **Integration** : Updated code to work with Python version 3.11. 

**Important:** To ensure compatibility and avoid disruptions, follow the best practices in [Upgrade Python versions](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/upgrade-python-versions).

## January 08, 2025

Change

**Darktrace** : Version 17.0

  * Added the `Padding Time` parameter to the following connector:

    * **Darktrace - Model Breaches Connector**



Change

**CrowdStrike Falcon** : Version 56.0

  * **Integration** : Dependencies update.



Change

**Splunk** :

  * Improved unicode handling for API responses in the following action:

    * **Ping**



Change

**SiemplifyUtilities** : Version 23.0

  * Updated the following action:

    * **Filter JSON**



## January 02, 2025

Change

**Microsoft Azure Sentinel** : Version 49.0

  * Microsoft Azure Sentinel

    * **Integration** : Reverted to Version 46. Now running with Python 3.7.



## December 26, 2024

Change

Updated code to work with Python version 3.11 in the following integrations:

  * **HTTP v2** : Version 6.0

  * **ThreatConnect** : Version 13.0


**Important:** To ensure compatibility and avoid disruptions, follow the best practices in [Upgrade Python versions](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/upgrade-python-versions).

## December 24, 2024

Feature

New **Google Forms** integration

Feature

**Google Cloud Compute** : Version 13.0

  * The following new actions have been added:

    * **Add Network Tags**

    * **Remove Network Tags**

    * **Add IP To Firewall Rule**

    * **Remove IP From Firewall Rule**

    * **Execute VM Patch Job**




Change

**Google Cloud Policy Intelligence** : Version 5.0

  * **Integration** : Added the ability to provide the location for regionalised API execution.



Change

**Google BigQuery** : Version 14.0

  * **Integration** : Added the ability to provide the API Root in the integration configuration.



Change

**Screenshot Machine** : Version 13.0

  * **Integration** : Updated dependencies.



Change

**VMRay** : Version 16.0

  * Updated the logic of the following action:

    * **Upload File And Get Report**



Change

**Splunk** : Version 54.0

  * Refactored the logic of the following action:

    * **Ping**



Change

**Cloud Logging** : Version 3.0

  * **Integration** : Added the ability to provide the API Root in the integration configuration.



Change

**ProofPoint TAP** : Version 10.0

  * **Integration** : Action updates.



Change

**Any.Run** : Version 7.0

  * Due to the changes of the Any.Run API, the following actions have been updated (The `opt_network_heavyevasion` action input parameter was replaced with `opt_kernel_heavyevasion` and the `opt_network_geo` action input parameter value "Fastest" was replaced with "fastest"):

    * **Analyze File**

    * **Analyze File URL**

    * **Analyze URL**




Change

**Google Cloud Compute** : Version 13.0

  * Extended capabilities of the following action:

    * **Update Firewall Rule**
  * **Integration** : Added the ability to provide the API Root in the integration configuration.




Change

**Siemplify** : Version 82.0

  * Updated predefined widget in the following action:

    * **Get Similar Cases**



Change

**CrowdStrike Falcon** : Version 55.0

  * Updated the ontology mapping in the following connector:

    * **Crowdstrike Falcon - Alerts Connector**



## December 19, 2024

Change

Updated code to work with Python version 3.11 in the following integrations: 

  * **Case Federation** : Version 2.0

  * **ElasticSearch** : Version 41.0

  * **ElasticSearchV7** : Version 19.0

  * **Ivanti Endpoint Manager** : Version 6.0

  * **Splunk** : Version 53.0


**Important:** To ensure compatibility and avoid disruptions, follow the best practices in [Upgrade Python versions](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/upgrade-python-versions).

## December 18, 2024

Feature

**SCC Enterprise** : Version 15.0

  * The following new action has been added:

    * **Add SCCE Tags**



Feature

New **PubSub** integration

Change

**Google Cloud Storage** : Veresion 11.0

  * **Integration** : Added ability to provide API Root in the integration configuration.



Change

**Google Alert Center** : Version 9.0

  * Updated severity handling logic in the following connector:

    * **Google Alert Center - Alerts Connector**



Change

**SCC Enterprise** : Version 15.0

  * **Integration** : Code improvements.



Change

**Google Cloud IAM** : Veresion 15.0

  * Updated action parameter descriptions in the following action:

    * **Delete Role**
  * **Integration** : Added ability to provide API Root in the integration configuration.




Change

**Microsoft Graph Mail** : Version 20.0

  * Updated the following action:

    * **Send Vote Email**
  * **Integration** : Added support for selecting whether to fetch the user email address from the `userPrincipalName` or `mail` fields from Microsoft Graph API.




## December 12, 2024

Change

Updated code to work with Python version 3.11 in the following integrations:

  * **Intezer** : Version 10.0

  * **Microsoft Azure Sentinel** : Version 48.0

  * **ServiceNow** : Version 52.0

  * **ZohoDesk** : Version 7.0




## December 11, 2024

Feature

**SCC Enterprise** : Version 14.0

  * The following new action has been added:

    * **Add SCCE Tags**



Change

**Microsoft Defender ATP** : Version 26.0

  * **Integration** : Added support to modify the login API root.



Change

**Rapid7 InsightVM** : Version 12.0

  * Updated pagination handling logic in the following actions:

    * **Enrich Asset**

    * **List Scans**

    * **Launch Scan**

  * Updated pagination handling logic in the following connector:

    * **Rapid7 InsightVM - Vulnerabilities Connector**



Change

**Microsoft 365 Defender** : Version 19.0

  * **Integration** : Added ability to modify the Login API root and Graph API root.



Change

**Google Chronicle** : Version 47.0

  * Improved handling of detections in the following action:

    * **Get Detection Details**
  * Updated alert structure in the following connector:

    * **Google Chronicle - Alerts Connector**



Change

**Palo Alto Panorama** : Version 32.0

  * **Integration** : Improved actions compatibility with Python 3.11.



## December 05, 2024

Change

Updated code to work with Python version 3.11 in the following integrations:

  * **Google Chronicle** : Version 46.0

  * **SCC Enterprise** : Version 13.0


**Important:** To ensure compatibility and avoid disruptions, follow the best practices in [Upgrade Python versions](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/upgrade-python-versions).

## December 04, 2024

Change

**Microsoft Azure Sentinel** : Version 47.0

  * Added an option to create additional SecOps events for all Sentinel Incident's entities in the following connectors: 

    * **Microsoft Azure Sentinel - Incident Connector v2**

    * **Microsoft Azure Sentinel - Incident Tracking Connector**

  * Improved tracking of Microsoft Sentinel Incident's entities in the following connectors (if the connector can't fetch events for Sentinel's Scheduled alerts or NRT-based incidents, it will attempt to fetch Incident's entities instead):

    * **Microsoft Azure Sentinel - Incident Connector v2**

    * **Microsoft Azure Sentinel - Incident Tracking Connector**

  * Improved handling of Microsoft Sentinel incidents IDs in the connector backlog in the following connectors:

    * **Microsoft Azure Sentinel - Incident Connector v2**

    * **Microsoft Azure Sentinel - Incident Tracking Connector**




Change

**Symantec Endpoint Protection 14** : Version 17.0

  * **Integration** : Made integration updates.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
