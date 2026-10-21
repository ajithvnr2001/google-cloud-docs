---
url: https://docs.cloud.google.com/chronicle/docs/secops/release-notes/
title: Google Security Operations release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:00.122899+00:00
---

# Google Security Operations release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Support ](https://docs.cloud.google.com/chronicle/docs/secops/release-notes)



Send feedback 

#  Google Security Operations release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Google Security Operations. You can periodically check this page for announcements related to new or updated features, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/chronicle-security-operations-release-notes.xml) directly. 

## October 18, 2026

Feature

**Specify whether to reopen closed cases when the grouping is by Source Grouping Identifier**

You can now specify whether Google SecOps reopens closed cases when grouping SOAR alerts by **Source Grouping Identifier**. When the option is enabled and a new alert is received with a source grouping identifier of a case that was previously closed in Google SecOps, then Google SecOps reopens the case. For more information, see [Configure alert grouping](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/alert-grouping-mechanism-admin).

## October 12, 2026

Feature

**Applied Threat Intelligence curated rules now use the GTI_IOC feed**

As a follow-up to the release of the `GTI_IOC` feed and the deprecation of the legacy `MANDIANT_ACTIVE_BREACH_IOC`, `MANDIANT_FUSION_IOC`, and `OPEN_SOURCE_INTEL_IOC` feeds, the Applied Threat Intelligence (ATI) curated detection rules are being updated to match against the `GTI_IOC` feed. You don't need to take any action for curated rules. Updated rules continue to match only on reviewed, stable indicators. If you have custom rules that still reference the legacy feeds, update them to use the `GTI_IOC` feed. For more information, see [Migrate to GTI_IOC](https://docs.cloud.google.com/chronicle/docs/detection/ati-fusion-feed#migrateToGTI).

The update follows the standard Google SecOps rollout schedule. It starts on Monday, October 12, 2026 and rolls out to all regions during the week.

Change

Google SecOps has updated the list of [supported default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers). Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

  * AIX system (`AIX_SYSTEM`)
  * Apache (`APACHE`)
  * AppOmni (`APPOMNI`)
  * Armis Activities (`ARMIS_ACTIVITIES`)
  * Atlassian Cloud Admin Audit (`ATLASSIAN_AUDIT`)
  * Atlassian Bitbucket (`ATLASSIAN_BITBUCKET`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS Inspector (`AWS_INSPECTOR`)
  * AWS RDS (`AWS_RDS`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure AD Organizational Context (`AZURE_AD_CONTEXT`)
  * Azure AD Sign-In (`AZURE_AD_SIGNIN`)
  * Azure App Service (`AZURE_APP_SERVICE`)
  * Azure Firewall (`AZURE_FIREWALL`)
  * Azure Application Gateway (`AZURE_GATEWAY`)
  * Azure Key Vault logging (`AZURE_KEYVAULT_AUDIT`)
  * Bitdefender (`BITDEFENDER`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Box (`BOX`)
  * Zeek JSON (`BRO_JSON`)
  * Check Point Sandblast (`CHECKPOINT_EDR`)
  * Chrome Management (`CHROME_MANAGEMENT`)
  * CipherTrust Manager (`CIPHERTRUST_MANAGER`)
  * Cisco ACS (`CISCO_ACS`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Email Security (`CISCO_EMAIL_SECURITY`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco FireSIGHT Management Center (`CISCO_FIRESIGHT`)
  * Cisco IronPort (`CISCO_IRONPORT`)
  * Cisco Meraki (`CISCO_MERAKI`)
  * Cisco Umbrella Audit (`CISCO_UMBRELLA_AUDIT`)
  * Cisco WLC/WCS (`CISCO_WIRELESS`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Claroty Xdome (`CLAROTY_XDOME`)
  * Claude Compliance Logs (`CLAUDE_COMPLIANCE_LOGS`)
  * Cloudflare Audit (`CLOUDFLARE_AUDIT`)
  * Corelight (`CORELIGHT`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * CrowdStrike Alerts API (`CS_ALERTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CrowdStrike Falcon Stream (`CS_STREAM`)
  * CyberArk (`CYBERARK`)
  * CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
  * Darktrace (`DARKTRACE`)
  * F5 Advanced Firewall Management (`F5_AFM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * F5 VPN (`F5_VPN`)
  * FireEye HX (`FIREEYE_HX`)
  * FireEye NX (`FIREEYE_NX`)
  * Forcepoint DLP (`FORCEPOINT_DLP`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortinet Fortimanager (`FORTINET_FORTIMANAGER`)
  * Fortinet FortiSandbox (`FORTINET_SANDBOX`)
  * Fortinet Switch (`FORTINET_SWITCH`)
  * Fortinet Proxy (`FORTINET_WEBPROXY`)
  * Apigee (`GCP_APIGEE_X`)
  * GCP Cloud Audit (`GCP_CLOUDAUDIT`)
  * Cloud DNS (`GCP_DNS`)
  * Security Command Center Threat (`GCP_SECURITYCENTER_THREAT`)
  * GCP Secure Web Proxy (`GCP_SWP`)
  * VPC Flow Logs (`GCP_VPC_FLOW`)
  * Gemini Code Assist (`GEMINI_CODE_ASSIST`)
  * Gitlab (`GITLAB`)
  * AWS GuardDuty (`GUARDDUTY`)
  * Huawei Switches (`HUAWEI_SWITCH`)
  * IBM AS/400 (`IBM_AS400`)
  * Microsoft IIS (`IIS`)
  * Illumio Core (`ILLUMIO_CORE`)
  * Imperva SecureSphere Management (`IMPERVA_SECURESPHERE`)
  * Infoblox (`INFOBLOX`)
  * Jenkins (`JENKINS`)
  * JFrog Artifactory (`JFROG_ARTIFACTORY`)
  * Journald (`JOURNALD`)
  * Juniper (`JUNIPER_FIREWALL`)
  * Juniper Junos (`JUNIPER_JUNOS`)
  * Kiteworks (`KITEWORKS`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * McAfee IPS (`MCAFEE_IPS`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Defender for Identity (`MICROSOFT_DEFENDER_IDENTITY`)
  * Microsoft Defender for Office 365 (`MICROSOFT_DEFENDER_MAIL`)
  * Microsoft Sentinel (`MICROSOFT_SENTINEL`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * Netskope CASB (`NETSKOPE_CASB`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * Netwrix (`NETWRIX`)
  * NGINX (`NGINX`)
  * Unix system (`NIX_SYSTEM`)
  * Nutanix Prism (`NUTANIX_PRISM`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * Okta User Context (`OKTA_USER_CONTEXT`)
  * Onapsis (`ONAPSIS`)
  * Oracle (`ORACLE_DB`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Palo Alto Prisma Cloud Alert payload (`PAN_PRISMA_CA`)
  * Ping One (`PING_ONE`)
  * Microsoft PowerShell (`POWERSHELL`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Pure Storage (`PURE_STORAGE`)
  * Red Hat OpenShift (`REDHAT_OPENSHIFT`)
  * RSA NetWitness (`RSA_NETWITNESS`)
  * SailPoint IAM (`SAILPOINT_IAM`)
  * Salesforce (`SALESFORCE`)
  * Sangfor Next Generation Firewall (`SANGFOR_NGAF`)
  * Sap Business Technology Platform (`SAP_BTP`)
  * SAP Change Document (`SAP_CHANGE_DOCUMENT`)
  * SecureLink (`SECURELINK`)
  * Sentinelone Alerts (`SENTINELONE_ALERT`)
  * Slack Audit (`SLACK_AUDIT`)
  * Sourcefire (`SOURCEFIRE_IDS`)
  * Squid Web Proxy (`SQUID_WEBPROXY`)
  * STIX Threat Intelligence (`STIX`)
  * Sublime Security (`SUBLIMESECURITY`)
  * Symantec Event export (`SYMANTEC_EVENT_EXPORT`)
  * Synology (`SYNOLOGY`)
  * Sysdig (`SYSDIG`)
  * Tableau (`TABLEAU`)
  * Tanium Stream (`TANIUM_TH`)
  * TCPWave DDI (`TCPWAVE_DDI`)
  * Teleport Access Plane (`TELEPORT_ACCESS_PLANE`)
  * Tenable Security Center (`TENABLE_SC`)
  * Trellix HX Alerts (`TRELLIX_HX_ALERTS`)
  * Trellix HX Audit Events (`TRELLIX_HX_AUDIT`)
  * Trellix HX Event Streamer (`TRELLIX_HX_ES`)
  * TrendMicro Apex Central (`TRENDMICRO_APEX_CENTRAL`)
  * Trend Micro Email Security Advanced (`TRENDMICRO_EMAIL_SECURITY`)
  * Trend Micro Vision One Audit (`TRENDMICRO_VISION_ONE_AUDIT`)
  * Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
  * Trend Micro Vision One Observerd Attack Techniques (`TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES`)
  * Trend Micro Vision One Workbench (`TRENDMICRO_VISION_ONE_WORKBENCH`)
  * Ubiquiti UniFi Switch (`UBIQUITI_SWITCH`)
  * Uptycs EDR (`UPTYCS_EDR`)
  * Upwind (`UPWIND`)
  * Venafi ZTPKI (`VENAFI_ZTPKI`)
  * Veritas NetBackup (`VERITAS_NETBACKUP`)
  * Vmware Avinetworks iWAF (`VMWARE_AVINETWORKS_IWAF`)
  * VMware ESXi (`VMWARE_ESX`)
  * VMware vCenter (`VMWARE_VCENTER`)
  * VMware vRealize Suite (VMware Aria) (`VMWARE_VREALIZE`)
  * Wallix Bastion (`WALLIX_BASTION`)
  * Microsoft AD (`WINDOWS_AD`)
  * Windows Defender AV (`WINDOWS_DEFENDER_AV`)
  * Windows DHCP (`WINDOWS_DHCP`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Sysmon (`WINDOWS_SYSMON`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * wiz.io (`WIZ_IO`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * Zoom Operation Logs (`ZOOM_OPERATION_LOGS`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

  * Amazon Bedrock Model Invocation Logging (`AMAZON_BEDROCK_MODEL_INVOCATION_LOGGING`)
  * AppTrana Web Application Firewall (`AWS_APPTRANA`)
  * Azure Machine Learning (`AZURE_MACHINE_LEARNING`)
  * Bitstamp (`BITSTAMP`)
  * Cloud 9 (`CLOUD9`)
  * Cloudflare Brand Protection (`CLOUDFLARE_BRAND_PROTECTION`)
  * Cloudflare Browser Isolation (`CLOUDFLARE_BROWSER_ISOLATION`)
  * Delinea Cloud Platform (`DELINEA_CLOUD_PLATFORM`)
  * Honeywell Cyber Proactive Defense (`HONEYWELL_CPD`)
  * Huntress EDR (`HUNTRESS_EDR`)
  * IBM Cloud Alert Notification (`IBM_CLOUD_ALERT_NOTIFICATION`)
  * Meter Firewall NIDS (`METER_FIREWALL_NIDS`)
  * OutSystems Cloud (`OUTSYSTEMS_CLOUD`)
  * Staffbase Audit (`STAFFBASE_AUDIT`)
  * Statsig (`STATSIG`)
  * Temporal Cloud Audit Logs (`TEMPORAL_CLOUD_AUDIT_LOGS`)
  * Twilio Segment (`TWILIO_SEGMENT`)



Feature

**[Spotlight Feature] Monitor response and playbook health with the Response Health Hub**

Google SecOps now includes the **Response Health Hub** curated dashboard, a central location for monitoring playbook performance, execution latency, automation effectiveness, and integration health across environments.

Key capabilities include:

  * **Volume and adoption tracking** : Monitor total playbook execution volume, daily trends, completion success rates, and queued playbook backlogs.
  * **Attachment and rerun insights** : Track average and maximum playbooks attached per case or alert, and identify playbooks with high rerun counts.
  * **Execution latency diagnostics** : Compare end-to-end playbook execution time against active action execution time, and drill down into the 30 slowest playbook and action runs.
  * **Playbook and integration health monitoring** : Investigate the latest failed playbook runs, highest failure-rate and terminated playbooks, and integration action error reasons.
  * **Automation effectiveness metrics** : Compare automated versus manual case closure rates and Mean Time to Resolve (MTTR).



For more information, see [Monitor response and playbook health](https://docs.cloud.google.com/chronicle/docs/reports/response-health-monitoring-and-troubleshooting-dashboard).

Announcement

The deadline for the migration of SOAR APIs to the Chronicle API has been extended from November 30, 2026 until March 31, 2027. For more information, refer to [SOAR Migration overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp)

## October 05, 2026

Feature

**[Spotlight Feature] Terraform and client libraries for multiple features using Chronicle API**

Terraform providers and Google Cloud client libraries are now available for several Google SecOps features using Chronicle API including **Feeds, Parsers, Rules, Findings Refinements, Retrohunts, Dashboards, Data Tables, Watchlists, Custom Lists, Environments, Environment Groups, Data Export, SOAR Domains, and SOAR Networks**. For more information, see [Terraform reference](https://docs.cloud.google.com/chronicle/docs/terraform). 

Terraform providers enable programmatic provisioning and management of Google SecOps resources as code, while Client Libraries enable developers to build custom integrations and automate Google SecOps workflows in their preferred programming languages. For more information, see [Client libraries](https://docs.cloud.google.com/chronicle/docs/libraries).

## September 30, 2026

Feature

**Expanded read-only permissions for Chronicle API Restricted Data Access Viewer**

Google SecOps has updated the predefined **Chronicle API Restricted Data Access Viewer** (`roles/chronicle.restrictedDataAccessViewer`) IAM role to include all read-only permissions available in the **Chronicle API Viewer** (`roles/chronicle.viewer`) role, excluding global data access (`chronicle.globalDataAccessScopes.permit`).

With this update, users assigned to `roles/chronicle.restrictedDataAccessViewer` IAM role will have read-only access across Google SecOps features—including SOAR cases and playbooks, investigations, threat collections, findings, security validation, and ingestion resources within their assigned data access scopes.

For more information, see [Configure data RBAC for users](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users).

## September 21, 2026

Feature

**Google Cloud organization ID enrichment for direct ingestion**

Google SecOps now automatically enriches logs ingested through [Google Cloud direct ingestion](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs#option_1_direct_ingestion) with the originating Google Cloud organization ID.

Previously, direct ingestion did not include organization-level identifiers, requiring customers with multiple Google Cloud organizations to configure separate Cloud Logging sinks and feeds to distinguish their log sources. With this update, you can easily identify the source organization for each event, filter UDM searches, scope detection rules, and configure Data RBAC or [Data Processing Pipelines](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline) across multi-organization environments without additional configuration.

In UDM events, the organization ID appears automatically under `metadata.base_labels.ingestion_kv_labels`:

  * `key`: `"gcp_organization_id"`
  * `value`: `"<YOUR_GCP_ORGANIZATION_ID>"`



**Rollout details** : This feature will roll out gradually starting September 21, 2026, through September 28, 2026. No action or configuration change is required.

## September 18, 2026

Feature

**Resizable side panels in the Investigation Management experience**

You can now dynamically resize the **Case preview** and **Alert and detection preview** side panels in the revamped **Investigation Management** experience in Google SecOps. You can adjust the panel width using your mouse or keyboard shortcuts to view detailed telemetry, parsed UDM records, and raw logs without navigating away from your main case queue.

To explore the complete triage workflow, see [Investigation and case management overview](https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/investigation-management-overview).

## September 15, 2026

Feature

**Grok filter match_all option in parser syntax**

The Google SecOps parser syntax is updated to support the `match_all` option within the Grok filter. This allows parsers to extract all non-overlapping pattern occurrences within a field, rather than returning only the first match.

For more information, see [Parser syntax reference](https://docs.cloud.google.com/chronicle/docs/reference/parser-syntax#grok_match_all_option).

## September 14, 2026

Feature

**[Spotlight Feature] GoogleSQL query support in Search**

This feature is in public preview. You can now use GoogleSQL in **Search** to query your security data in Google SecOps, offering a flexible and powerful industry-standard alternative to YARA-L 2.0. GoogleSQL is optimized for broad data exploration, statistical aggregation, and deep-dive ad hoc investigations. You can query telemetry tables including but not limited to UDM events, entity graphs, detection rules, and case management data—using either standard declarative SQL or the linear, sequential Piped SQL syntax.

For more information, see [Get started with GoogleSQL](https://docs.cloud.google.com/chronicle/docs/reference/standard-sql/getting-started-googlesql).

Deprecated

**MANDIANT_ACTIVE_BREACH_IOC`,`MANDIANT_FUSION_IOC`, and`OPEN_SOURCE_INTEL_IOC` feeds are being removed**

The `MANDIANT_ACTIVE_BREACH_IOC`, `MANDIANT_FUSION_IOC`, and `OPEN_SOURCE_INTEL_IOC` feeds are [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) in favor of the `GTI_IOC` feed. After March 18, 2027, we will be removing the `MANDIANT_ACTIVE_BREACH_IOC`, `MANDIANT_FUSION_IOC`, and `OPEN_SOURCE_INTEL_IOC` feeds. For more information on how to migrate, see [Migrate Mandiant legacy feeds to GTI](https://docs.cloud.google.com/chronicle/docs/detection/ati-fusion-feed#migrateToGTI).

## September 11, 2026

Deprecated

**Deprecation of write permissions from the chronicle.readonly OAuth scope**

Effective January 25, 2027, **write** permissions will be removed from the `chronicle.readonly` OAuth scope, restricting it strictly to **read** operations. You can continue using `chronicle.readonly` for read operations. Make sure you update any workflows performing **write** operations to use the `chronicle` OAuth scope.

## September 06, 2026

Feature

**[Spotlight Feature] Case playbooks**

This feature is in preview. Google SecOps now supports case playbooks. You can run playbooks or execute manual actions across an entire case container rather than individual alerts, consolidating response tasks and reducing redundant operations during investigations.

For more information, see [Case playbooks overview](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/case-playbooks).

Feature

**[Spotlight Feature] Reaction triggers**

This feature is in preview. Google SecOps now supports reaction triggers. As post-ingestion triggers, they allow playbooks to automatically fire in response to real-time case or alert updates during active investigations, such as changes to the case assignee, case tags, alert priority, or newly added entities.

For more information, see [Use reaction triggers in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-reaction-triggers-in-playbooks).

## September 03, 2026

Feature

**Self-service Bindplane Enterprise license download**

This feature is currently in Preview for Google Security Operations tenants in the US and EU regions. Google Security Operations Enterprise Plus and Google Unified Security (GUS) customers can now download their **Bindplane Enterprise (Google Edition)** license key directly from the platform console under **SIEM Settings > Collection Agents**.

For more information, see [Bindplane Enterprise (Google Edition)](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#bp-download-license).

## August 31, 2026

Feature

**[Spotlight Feature] Customizable schedules for multi-event rules general availability**

The [customizable schedules for multi-event rules](https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule) feature is now in General Availability (GA).

Customizable schedules give security teams granular control and transparency over how multi-event rules execute in Google SecOps, and provide the following capabilities:

  * **Configure settlement delays:** Set first-run delay offsets (from 1 minute up to 48 hours) to account for log ingestion latency and reduce false negatives.
  * **Leverage automated true-up runs:** Automatically re-evaluate time windows at 4 hours (and optionally 30 hours for full context enrichment) to capture late-arriving logs.
  * **Migrate legacy rules:** Upgrade existing custom multi-event rules to customizable schedules directly from the **Rules Dashboard**.



To manage rule schedules with custom IAM roles, make sure your roles include `chronicle.rules.modifyRules` and `chronicle.ruleDeployments.update`. Predefined IAM roles include these permissions automatically.

For more information, see [Configure customized schedules for rules](https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule) and [Understand rule run scheduling](https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency).

## August 27, 2026

Announcement

**Scheduled maintenance**

SOAR database and infrastructure maintenance is scheduled to take place during the standard maintenance window on Sunday, August 30. During this window, your system will experience a brief period of downtime. You don't need to take any action.

## August 26, 2026

Feature

**[Spotlight Feature] Mandiant Frontline Threats rule packs**

[Curated Detections](https://docs.cloud.google.com/chronicle/docs/detection/curated-detections) has been enhanced with additional Mandiant Frontline Threats detections for Linux, MacOS, and Google Cloud. The following rule packs have been added to the [Content Hub](https://docs.cloud.google.com/chronicle/docs/secops/content_hub):

  * [Mandiant Frontline Threats for Linux](https://docs.cloud.google.com/chronicle/docs/detection/linux-threats-category)
  * [Mandiant Frontline Threats for MacOS](https://docs.cloud.google.com/chronicle/docs/detection/macos-threats-category)
  * [Mandiant Frontline Threats for Google Cloud](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#cloud-rule-sets)



## August 24, 2026

Feature

**Unroll Processor for Data Processing Pipelines**

Google SecOps data processing pipelines now support the **Unroll processor** (event breaking). This processor allows you to split log entries containing arrays or slices of events into multiple individual log events prior to parsing and ingestion.

Key details:

  * **Event Breaking Capability:** Automatically expands log arrays into discrete log events.
  * **Pre-parsing Requirement:** The Unroll processor requires structured data inputs. Raw string payloads must first be parsed using a Transform processor (e.g., `set(body, ParseJSON(body))`) positioned prior to the Unroll processor in the pipeline execution sequence.



For details on configuring data processing pipelines and processors, see [Set up and manage data processing pipelines](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline#configure-processors).

Feature

**[Spotlight Feature] Operations in Emerging Threats Center**

Google SecOps now supports **Operations** in the **Emerging Threats Center** feed to provide rapid visibility into threat activity details involving the targeting of a single organization. Operations complement global Campaigns by providing granular threat intelligence derived from frontline investigations, such as Managed Threat Defense (MTD) engagements. For more information, see [Operations in Emerging Threats](https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats#what_is_an_operation).

Key capabilities include:

  * **Focused threat insights** : Zero in on localized adversary activity and personalized attack vectors specific to individual missions.
  * **Holistic threat mapping** : View Operations alongside global Campaigns to see the full scope of adversary tactics, techniques, and procedures (TTPs).



## August 21, 2026

Feature

**[Spotlight Feature] Relative time filtering in Google SecOps**

This feature is in public preview. Google SecOps has updated how relative time filters calculate data ranges. You can now choose from three distinct, mathematically precise operators: Past, Previous, and Current. This change eliminates ambiguity between rolling windows and calendar-aligned periods, ensuring consistent behavior across all time units (like seconds, minutes, hours, days, weeks, months, years) and aligning SecOps dashboards with Search and other Google tools (such as Looker).

For more information, see the **Relative time range** section of the [Understand search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#relative_time_range) guide.

## August 20, 2026

Feature

**Side-by-side view on the Alerts & Detections tab in Cases**

This feature is in public preview. The **Alerts & Detections** tab in the revamped Investigation Management experience now supports a **Side-by-side view** layout.

You can switch between the default **List view** and the **Side-by-side view** to inspect an alert or detection's detailed metadata, status, priority, creation date, and Gemini investigation insights in an adjacent side pane without navigating away from the main list.

For more information, see [Investigation and case management overview](https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/investigation-management-overview).

## August 18, 2026

Feature

**[Spotlight Feature] Evaluate threat coverage and generate rules with the Detection Engineering Agent**

This feature is in public preview. You can now evaluate and strengthen your Google SecOps security posture against emerging threats using the Detection Engineering Agent. This AI-powered assistant helps you extract threat intelligence and automatically draft YARA-L detection rules, drastically improves time-to-value for custom security automation and accelerating risk mitigation. The agent is accessible using Model Context Protocol (MCP) tools operated by compatible AI clients (such as Google Antigravity or Claude Code). For more information, see [Evaluate threat coverage with the Detection Engineering Agent](https://docs.cloud.google.com/chronicle/docs/secops/agentic-detection-engineering).

Feature

**[Spotlight Feature] Event simulation for detection coverage evaluation**

This feature is in public preview. You can now programmatically deliver realistic threat sequences into the live ingestion pipeline using event simulation. Event simulation provides a full-funnel detection coverage evaluation framework embedded directly within Google SecOps, enabling detection engineering and SOC teams to verify the entire detection lifecycle—from UDM normalization to multi-event correlation and alerting—while preserving production SOC workflows.

As a core capability of the [Detection Engineering Agent (DEA)](https://docs.cloud.google.com/chronicle/docs/secops/agentic-detection-engineering) architecture, event simulation connects Google SecOps MCP tools with AI assistance (such as Gemini) to automate threat intel processing, synthetic telemetry generation, and YARA-L 2.0 rule coverage evaluation.

For more information, see [Use event simulation for detection coverage evaluation](https://docs.cloud.google.com/chronicle/docs/secops/event-simulation).

## August 14, 2026

Feature

**[Spotlight Feature] Monitor your data latency with the Health Hub**

This feature is in public preview. The **Health Hub** now includes two new tables to track the ingestion latency at both the source level and the log-type level. In addition, you can select a specific source or log type to open the **Data Health Deep Dive** page and view detailed information about ingestion latency. For more information, see [Monitor health of data sources](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard).

Key capabilities include:

  * **Improve end-to-end visibility and reduce mean time to debug (MTTD):** Google SecOps calculates latency at both the source level and the log type level to improve end-to-end visibility and help reduce the mean time to debug (MTTD) for delayed logs.
  * **Monitor ingestion latency by source:** View the ingestion latency for each individual data source.
  * **Monitor ingestion latency by log type:** View the ingestion latency for each individual log type.
  * **View detailed information about ingestion latency:** Select a specific source or log type to open the **Data Health Deep Dive** page and view detailed information about ingestion latency.

**Note:** The **Lookback Window** will be fully rolled out next week.

## August 13, 2026

Announcement

**Scheduled Maintenance**

SOAR database and infrastructure maintenance is scheduled to take place during the standard maintenance window on Sunday, August 16. During this window, your system will experience a brief period of downtime. No customer action is required.

## August 12, 2026

Feature

**[Spotlight Feature] Analyze feed activity with Cloud Logging**

This feature is in public preview. To use this feature, your Google SecOps instance must be configured with a Bring Your Own Project (BYOP) Google Cloud project. You can now monitor, debug, and troubleshoot Google SecOps ingestion pipelines and feeds using Cloud Logging. By sending, viewing, and querying ingestion and feed activity logs in the Logs Explorer, you can diagnose log delivery issues, such as, missing, delayed, or failing logs, and decrease the time required to resolve ingestion anomalies.

This visibility into push- and pull-based ingestion mechanisms provides the following capabilities:

  * **Investigate telemetry** : Use Gemini Cloud Assist to investigate logging and metrics telemetry directly from the Google SecOps console.
  * **Debug feeds** : Use the **Debug with logs** option on the **Feed management** page to open **Logs Explorer** pre-filtered for a specific feed.
  * **Filter routed logs** : Configure exclusion filters in the Log Router to exclude specific logs, such as Storage Transfer Service (STS) logs, from being routed to Cloud Logging.



For more information, see [Analyze feed activity with Cloud Logging](https://docs.cloud.google.com/chronicle/docs/ingestion/analyze-feed-activity-with-cloud-logging).

## August 09, 2026

Feature

**Updated rich-text editor**

Upgraded the rich-text editor across Google SecOps, including the Cases Wall, Use Case Upload dialog, Report Template dialog, and Dashboard Editor widget.

Key changes include:

  * **Simplified typography** : Choose font sizes using semantic options (Small, Normal, Large, Huge). Legacy font sizes on existing text are preserved.
  * **Streamlined tables** : You can insert or remove entire tables. Formatting inside table cells is no longer supported.
  * **Toolbar cleanup** : Removed the Cut, Copy, and Paste buttons from the toolbar. Standard OS keyboard shortcuts remain supported.
  * **Visual alignment** : Improved visual consistency between editor content during editing and after submission.



## August 03, 2026

Feature

**[Spotlight Feature] Threat Hunt Agent**

The Threat Hunt Agent is now available in Public Preview for Google SecOps Enterprise Plus customers. Powered by Gemini and grounded in Google Threat Intelligence (GTI), Mandiant frontline expertise, and the MITRE ATT&CK® framework, the Threat Hunt Agent autonomously automates proactive threat hunting across your historical security telemetry. For more information, see [Threat Hunt Agent](https://docs.cloud.google.com/chronicle/docs/detection/threat-hunt-agent).

Key capabilities include:

  * **Autonomous hunt planning:** Generates structured hunting plans tailored to specific threat actors, campaigns, malware families, software toolkits, or MITRE ATT&CK techniques.
  * **Automated case creation and determinations:** Synthesizes findings into summaries, assigns a verdict (Substantial Evidence, Evidence Found, or Threat Not Found), and automatically creates a dedicated case in Case Management.
  * **Automated query translation and execution:** Converts investigative hypotheses into YARA-L 2.0 search queries and executes against historical security telemetry.
  * **AI-driven evidence extraction:** Filters out routine background noise to isolate high-fidelity forensic evidence (hostnames, user accounts, and command lines).



Announcement

The deadline for Stage 2 of the SOAR migration to Google Cloud has been extended from September 30th to November 30th, 2026. For more information, refer to the [SOAR migration guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp).

## July 29, 2026

Change

Google SecOps has updated the list of [supported default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers). Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

  * Airlock Digital Application Allowlisting (`AIRLOCK_DIGITAL`)
  * AIX system (`AIX_SYSTEM`)
  * Akamai DataStream 2 (`AKAMAI_DATASTREAM_2`)
  * Akamai SIEM Connector (`AKAMAI_SIEM_CONNECTOR`)
  * Apache (`APACHE`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * Armis Alerts (`ARMIS_ALERTS`)
  * Aruba Switch (`ARUBA_SWITCH`)
  * Atlassian Cloud Admin Audit (`ATLASSIAN_AUDIT`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * Avaya Aura Experience Portal (`AVAYA_AURA`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS CloudWatch (`AWS_CLOUDWATCH`)
  * AWS Control Tower (`AWS_CONTROL_TOWER`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Organizational Context (`AZURE_AD_CONTEXT`)
  * Azure Application Gateway (`AZURE_GATEWAY`)
  * Azure Key Vault logging (`AZURE_KEYVAULT_AUDIT`)
  * Microsoft Azure Resource (`AZURE_RESOURCE_LOGS`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * BeyondTrust (`BOMGAR`)
  * Cato Networks (`CATO_NETWORKS`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Check Point Harmony (`CHECKPOINT_HARMONY`)
  * Chrome Management (`CHROME_MANAGEMENT`)
  * ChromeOS XDR (`CHROMEOS_XDR`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Email Security (`CISCO_EMAIL_SECURITY`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco FireSIGHT Management Center (`CISCO_FIRESIGHT`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Router (`CISCO_ROUTER`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco UCM (`CISCO_UCM`)
  * Claroty Xdome (`CLAROTY_XDOME`)
  * Claude Compliance Logs (`CLAUDE_COMPLIANCE_LOGS`)
  * HP Aruba (ClearPass) (`CLEARPASS`)
  * Cloudflare (`CLOUDFLARE`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * CrowdStrike Falcon (`CS_EDR`)
  * Darktrace (`DARKTRACE`)
  * EfficientIP DDI (`EFFICIENTIP_DDI`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * Fastly CDN (`FASTLY_CDN`)
  * FireEye eMPS (`FIREEYE_EMPS`)
  * FireEye HX (`FIREEYE_HX`)
  * FireEye NX (`FIREEYE_NX`)
  * Forcepoint Proxy (`FORCEPOINT_WEBPROXY`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortinet FortiClient (`FORTINET_FORTICLIENT`)
  * Fortinet Switch (`FORTINET_SWITCH`)
  * GCP Cloud Audit (`GCP_CLOUDAUDIT`)
  * Security Command Center External Exposure (`GCP_SECURITYCENTER_EXTERNAL_EXPOSURE`)
  * Gitlab (`GITLAB`)
  * Google Threat Intelligence IOC (`GTI_IOC`)
  * AWS GuardDuty (`GUARDDUTY`)
  * Huawei Switches (`HUAWEI_SWITCH`)
  * IBM Security Access Manager (`IBM_SAM`)
  * Microsoft IIS (`IIS`)
  * Illumio Core (`ILLUMIO_CORE`)
  * Imperva SecureSphere Management (`IMPERVA_SECURESPHERE`)
  * Infoblox (`INFOBLOX`)
  * Infoblox DHCP (`INFOBLOX_DHCP`)
  * Jamf pro context (`JAMF_PRO_CONTEXT`)
  * Mobile Endpoint Security (`LOOKOUT_MOBILE_ENDPOINT_SECURITY`)
  * Apple macOS (`MACOS`)
  * McAfee IPS (`MCAFEE_IPS`)
  * Micro Focus iManager (`MICROFOCUS_IMANAGER`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Defender for Office 365 (`MICROSOFT_DEFENDER_MAIL`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft Sentinel (`MICROSOFT_SENTINEL`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * Mimecast URL Logs (`MIMECAST_URL_LOGS`)
  * MISP Threat Intelligence (`MISP_IOC`)
  * NetApp ONTAP (`NETAPP_ONTAP`)
  * Netskope V2 (`NETSKOPE_ALERT_V2`)
  * Unix system (`NIX_SYSTEM`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * Onapsis (`ONAPSIS`)
  * OpenVPN (`OPEN_VPN`)
  * Oracle Fusion (`ORACLE_FUSION`)
  * Ping Identity (`PING`)
  * Proofpoint Sendmail Sentrion (`PROOFPOINT_SENDMAIL_SENTRION`)
  * SailPoint IAM (`SAILPOINT_IAM`)
  * Salesforce (`SALESFORCE`)
  * Sendmail (`SENDMAIL`)
  * Sentinelone Alerts (`SENTINELONE_ALERT`)
  * ServiceNow Audit (`SERVICENOW_AUDIT`)
  * ServiceNow CMDB (`SERVICENOW_CMDB`)
  * ServiceNow Security (`SERVICENOW_SECURITY`)
  * SonicWall (`SONIC_FIREWALL`)
  * STIX Threat Intelligence (`STIX`)
  * Tanium Threat Response (`TANIUM_THREAT_RESPONSE`)
  * Thinkst Canary (`THINKST_CANARY`)
  * ThreatConnect IOC V3 (`THREATCONNECT_IOC_V3`)
  * ThreatLocker Platform (`THREATLOCKER`)
  * Varonis (`VARONIS`)
  * VMware ESXi (`VMWARE_ESX`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * wiz.io (`WIZ_IO`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * Zoom Operation Logs (`ZOOM_OPERATION_LOGS`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

  * Adobe Experience Platform (`ADOBE_EXPERIENCE_PLATFORM`)
  * AudioCodes Session Border Controller (`AUDIOCODES_SBC`)
  * Azure Application Gateway for Containers (`AZURE_GATEWAY_CONTAINERS`)
  * Azure Logic Apps (`AZURE_LOGIC_APPS`)
  * Azure NAT Gateway Flow (`AZURE_NATGW_FLOW`)
  * Broadcom DX NetOps Spectrum (`BROADCOM_DX_NETOPS_SPECTRUM`)
  * Carto Activity (`CARTO_ACTIVITY`)
  * Claude Code Observability (`CLAUDE_CODE_OBSERVABILITY`)
  * Cyble Attack Surface Management (`CYBLE_ASM`)
  * Cyble Brand Intelligence & Protection (`CYBLE_BIP`)
  * Darkweb IQ (`DARKWEB_IQ`)
  * Ellio Threat Intelligence (`ELLIO_THREAT_INTEL`)
  * Exeon NDR (`EXEON_NDR`)
  * Gravitee (`GRAVITEE`)
  * Kaspersky anti targeted attack (`KASPERSKY_ANTI_TARGETED_ATTACK`)
  * Microsoft Copilot Interaction (`MICROSOFT_COPILOT_INTERACTION`)
  * OSTTRA MarkitWire (`OSTTRA_MARKITWIRE`)
  * Proofpoint Adaptive Email Security (`PROOFPOINT_ADAPTIVE_EMAIL_SECURITY`)
  * Secomea GateManager (`SECOMEA_GATEMANAGER`)
  * Trend Micro Vision One Risk Event (`TRENDMICRO_VISION_ONE_RISK_EVENT`)
  * TXOne EdgeIPS (`TXONE_EDGEIPS`)
  * Vectra Respond UX (`VECTRA_RUX`)
  * Zoho CRM (`ZOHO_CRM`)



Feature

**View prebuilt parser version content**

You can now view the prebuilt parser preview version content even if you are using a custom parser for the same log type. Although the prebuilt parser version is inactive, you can still see the content of the new preview version for this parser.

## July 28, 2026

Feature

**[Spotlight Feature] Data RBAC for first-party (1P) cases and alerts**

**Availability** This feature is now available in public preview for all regions.

Google SecOps now supports data role-based access control (Data RBAC) for first-party (1P) SOAR cases and alerts. This feature automatically applies SIEM data access scopes to alerts and cases ingested using the Chronicle connector, ensuring analysts only see data they are authorized to access.

For more information, see the [Release Note entry for July 6th](https://docs.cloud.google.com/chronicle/docs/secops/release-notes#July_06_2026).

## July 26, 2026

Feature

**Customizable schedules for multi-event rules**

[Customizable schedules for multi-event rules](https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule) are available in public preview. You can customize rule execution schedules on the **Rule schedule** tab to specify a first-run delay offset that accounts for data ingestion latency. The system also performs automated background true-up runs to catch late-arriving logs and process metadata enrichment without requiring manual system interventions. This gives you precise control over detection evaluation timing, reduces false negatives without missing detections, and promotes alert accuracy.

To view or modify rule schedules using custom Identity and Access Management (IAM) roles, update your [IAM permissions](https://docs.cloud.google.com/chronicle/docs/reference/feature-rbac-permissions-roles) to include the following:

  * `chronicle.ruleDeployments.update` to update individual rule schedules using the API.
  * `chronicle.rules.modifyRules` to modify rule schedules using the web interface or in batch using the API.



If you use [predefined IAM roles](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#predefined-roles), such as Chronicle API Admin (`roles/chronicle.admin`) or Chronicle API Editor (`roles/chronicle.editor`), these permissions are included automatically.

Feature

**[Spotlight Feature] Investigation and case management experience**

This feature is in public preview. Google SecOps now includes a revamped Investigation Management experience that supports tracking raw UDM events and detections alongside alerts to accommodate new investigation types (such as retrohunt and threat hunt) and higher investigation volumes in cases. You can navigate your case queue using customizable table views, side-drawer previews, and integrated UDM Search workflows. For more information, see [Investigation and case management overview](https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/investigation-management-overview).

This preview is currently supported only for single-SIEM deployments (instances where a single Google SecOps SIEM instance ingests data into SOAR) and does not support federated or MSSP environments.

Additional enhancements include:

  * **Attach SIEM search results to cases:** Manually attach individual UDM events or detections directly from SIEM search results to new or existing cases as core evidence (supporting up to 500 detections and 5,000 UDM events per case). For details, see [Attach SIEM search results to cases](https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/create-case-from-search).
  * **Interactive Events Viewer:** Dive directly into technical evidence from an interactive side panel. Inspect parsed UDM records, review original raw logs, pin key evidence to your case, and build detection exclusions in real time. For details, see [Use the Events Viewer](https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/use-events-viewer).
  * **Configure new default views:** Before enabling the updated Cases experience, set up your default views under **SOAR Settings > Case Data > Views**. Make sure to manually copy over advanced widget configurations (such as **Safe HTML Rendering** or custom conditions) from the **Default Alert View** and **Default Case View** to the **New Default Alert View** and **New Default Case View** to preserve your preferred setups.



## July 20, 2026

Deprecated

**[Spotlight Feature] Deprecation of Google SecOps legacy SIEM APIs**

Google SecOps is [deprecating](https://docs.cloud.google.com/chronicle/docs/deprecations) its legacy SIEM APIs—[Backstory API](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview#backstory_api) (including [Customer Management API](https://docs.cloud.google.com/chronicle/docs/reference/customer-management-api)) and [Ingestion API](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview#ingestion_api)—in favor of the modern [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview#chronicle_api).

**Key dates**

  * **October 26, 2026:** New Google SecOps instances provisioned from this date will no longer support legacy API calls.
  * **July 20, 2027:** All requests to legacy endpoints fail from this date because legacy APIs for all existing instances will be completely turned down. 



This change applies only to custom scripts, integrations, SOAR connectors, or ingestion feeds calling legacy Backstory API or Ingestion API endpoints. Any changes impacting the Google SecOps UI are already addressed and don't call for your action.

**Next steps**

  * Audit API usage to identify any affected components that currently call legacy Backstory API or Ingestion API endpoints, and replace them with Chronicle API endpoints.

  * Validate and test that your updated components work properly.




For more information, see [Migrate from legacy API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

## July 15, 2026

Feature

**[Spotlight Feature] Advanced Filtering in Dashboards**

Advanced Filtering in dashboards is now available in Preview. This feature enhances dashboard capabilities by enabling security analysts to use query variables, also known as tokens, to inject dynamic values, complex regular expressions, or boolean logic directly into YARA-L queries at runtime. 

Key aspects of Advanced Filtering include:

  * **Token Variable Definition:** When creating an advanced filter, you can define a Token Variable. Token variable names must consist only of alphanumeric characters and underscores (`^[a-zA-Z0-9_]+$`) and must be unique within the dashboard.
  * **Filter Value Generation:** Token values can be generated dynamically from YARA-L query results or entered manually as a static list.
  * **Customizable Wrappers:** You can specify prefixes and suffixes to wrap token values, enabling specific logic such as regular expressions.
  * **Multi-Select Support:** The ability to select multiple options for a token can be enabled, with a configurable delimiter (for example, `|`) for combining values in queries.



For more information, see [Advanced filtering](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters#advanced_filtering).

Feature

**Parser extensions for code snippets now support Append/Replace for Repeated Fields**

You can now use append and replace functionality for repeated fields when creating code snippet extensions. Previously, this was only available for no-code extensions. This enhancement provides more granular control over how data is handled in repeated UDM fields, allowing you to either add new values or entirely replace existing ones.

For more information, see [Repeated fields selector](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions#repeated_fields_selector).

## July 13, 2026

Feature

**SOAR migration to Google Cloud validation status**

You can now check if the SOAR migration was successful by going to the **SOAR Settings > License Management** page. After successful completion of Stage 1, it will say **Google.com** after the system version number. After successful completion of Stage 2 of SOAR permissions to IAM roles, it will say both **Google.com** and **CloudIAM Enabled** after the system version number.

For more information on the migration, see the [SOAR migration guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp)

## July 12, 2026

Feature

**Publisher Agent Version 2.7.0**

Publisher Agent Version 2.7.0 is now available for all regions.

This release includes the following updates for the remote agent:

  * **High Availability support:** Adds applicative support for Publisher high availability.
  * **File transfer support:** You can now upload and download files using playbooks and the SDK on agents that have been migrated to the GCOM infrastructure.



## July 06, 2026

Feature

**Data RBAC for first-party (1P) cases and alerts in public preview**

**Availability:** This feature is available **only in the following regions:** europe-central2, asia-northeast1, asia-south1, australia-southeast1, northamerica-northeast2, europe-west3, europe-west6, southamerica-east1, asia-southeast1, me-central1, me-central2, me-west1, europe-west2, europe-west9, europe-west12, asia-southeast2, africa-south1, asia-east1, and asia-northeast3.

Google SecOps now supports data role-based access control (Data RBAC) for first-party (1P) cases and alerts in SOAR. This feature automatically applies SIEM data access scopes to alerts and cases ingested using the Chronicle connector, ensuring analysts only see data they are authorized to access.

**Key highlights**

  * **SIEM-scope-to-SOAR inheritance:** Ingested 1P SIEM alerts carry their assigned data access scopes, which are automatically inherited by their parent SOAR cases.
  * **Dual access enforcement:** To view a case or alert, users must have access to both the assigned SOAR environment and all associated data access scopes. Global users maintain full visibility.
  * **Scope-to-environment mapping:** Administrators can map SIEM data access scopes to SOAR environments (**SOAR settings > Environments**) to manage alert routing and grouping. Alerts without mapped scopes are routed to a fallback environment.
  * **Enhanced UI visibility and filtering:** Assigned data access scopes are visible next to the environment in the **Case header** and the **List cases** table, allowing for easy filtering.
  * **Manual case and grouping logic:** When creating cases manually, analysts can only select from the intersection of their permitted data access scopes and environment mappings.



**Prerequisites and enablement**

  * Requires a unified Google SecOps instance with the **Chronicle connector** using the modern Chronicle API.
  * Administrators can enable this feature under **SIEM settings > Data access** by selecting **Enforce data access in SOAR** (or **Enforce data access** if SIEM data access is not yet active).



For more information, see [Control access to 1P cases and alerts](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-impact-cases).

## July 01, 2026

Announcement

**[Spotlight Feature] Security Tokens**

Security Tokens are now available for metering agentic consumption within Google SecOps. Tokens are consumed by generally available security agents only. These agents are invoked automatically or manually using the web interface, CLI, chat, or Model Context Protocol (MCP). Assistive features, such as standard chat panels and automated summaries, along with preview agents, won't consume Security Tokens.

Security Tokens will start rolling out across all regions starting July 1. For more information, see [Google SecOps Agentic SOC Security Tokens pricing and billing](https://docs.cloud.google.com/chronicle/docs/agentic-soc/security-tokens).

Feature

**[Spotlight Feature] Enhanced security and compliance for the Advanced BigQuery Export feature**

The [Advanced BigQuery Export feature](https://docs.cloud.google.com/chronicle/docs/reports/bigquery-export) is in Preview and is available for Google SecOps Enterprise Plus customers only. 

**Here's what's new:** We're excited to announce significant performance and coverage enhancements to Advanced BigQuery Export for Google SecOps Enterprise Plus customers.

  * **Expanded dataset support** : In addition to UDM events, rule detections, and IoC matches, we now support the export of Entity Graph and Ingestion Metrics.
  * **Enhanced security & compliance**: The offering natively supports [VPC Service Controls (VPC-SC)](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops), [Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops), and Data Residency (DRZ). Furthermore, customer-facing audit logs (Access Transparency) are delivered directly to your Cloud Logging workspace using the Federated Resource Identification Service.
  * **Data integrity and deduplication** : The system now uses Fine-Grained DML merges to update records in place behind the scenes. This ensures that you receive clean, deduplicated data without needing to write complex SQL routines.
  * **Seamless MSSP support (hub and spoke)** : Managed Security Service Providers (MSSPs) can now efficiently manage analytics across multiple customer tenants. This is achieved by programmatically subscribing to customers' linked datasets from a single centralized "Hub" project.
  * **Enum mapping tables** : Advanced BigQuery Export now includes `entity_enum_value_to_name_mapping` and `udm_enum_value_to_name_mapping` tables. These allow you to easily join against your events to translate numerical enum values into human-readable strings.



**Key reminders**

  * **Public preview & feature activation**: This feature is currently in Public Preview, is enabled only upon request, and may require initial configuration in your organization's Google SecOps instance. Contact your Google SecOps representative to confirm feature enablement.
  * **Enterprise Plus only** : This feature is exclusive to the Enterprise Plus tier.
  * **Zero-maintenance** : Your security data remains in a Google-managed project, appearing as a read-only linked dataset directly in your own Google Cloud project. This lets you query the data locally without the overhead of managing the pipeline or paying for storage.
  * **Migration and dual operation** : To support a smooth transition without disruption during the Public Preview, your data will be exported to the new BigQuery tenant project in addition to your existing Google-managed BigQuery project. You'll be notified before the old export pipeline is disabled for your account.



## June 30, 2026

Announcement

**Increased multiple event limits**

Multiple event rule limits have been increased to 200 for Enterprise customers and 400 for Enterprise+ customers.

For more information, see [Package comparison](https://docs.cloud.google.com/chronicle/docs/secops/secops-packages#package_comparison)

Announcement

**[Spotlight Feature] Unified rules interface**

The new rules interface is now available in public preview. The Google SecOps unified rules interface brings custom and curated rule management into a single, cohesive workflow. This optimizes detection engineering with a redesigned dashboard, an advanced rule editor, and expanded API capabilities to streamline rule deployment and troubleshooting.

You can still revert to the legacy experience. At the top right of the screen, click **Switch to the legacy experience**.

For more information about the Unified rules interface, see [Manage unified rules](https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/manage-unified-rules).

## June 28, 2026

Change

Google SecOps has updated the list of [supported default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers). Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

  * AIX system (`AIX_SYSTEM`)
  * Amazon API Gateway (`AWS_API_GATEWAY`)
  * Apache (`APACHE`)
  * Appian Cloud (`APPIAN_CLOUD`)
  * Aruba Switch (`ARUBA_SWITCH`)
  * Atlassian Bitbucket (`ATLASSIAN_BITBUCKET`)
  * Avaya Aura Experience Portal (`AVAYA_AURA`)
  * AWS CloudWatch (`AWS_CLOUDWATCH`)
  * AWS GuardDuty (`GUARDDUTY`)
  * AWS Network Firewall (`AWS_NETWORK_FIREWALL`)
  * AWS RDS (`AWS_RDS`)
  * AWS Security Hub (`AWS_SECURITY_HUB`)
  * AWS VPC Flow (`AWS_VPC_FLOW`)
  * AWS VPC Flow (CSV) (`AWS_VPC_FLOW_CSV`)
  * AWS WAF (`AWS_WAF`)
  * Azure AD (`AZURE_AD`)
  * Barracuda WAF (`BARRACUDA_WAF`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Cato Networks (`CATO_NETWORKS`)
  * Check Point Harmony (`CHECKPOINT_HARMONY`)
  * Chrome Management (`CHROME_MANAGEMENT`)
  * CircleCI (`CIRCLECI`)
  * Cisco ACS (`CISCO_ACS`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Email Security (`CISCO_EMAIL_SECURITY`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco IronPort (`CISCO_IRONPORT`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Meraki (`CISCO_MERAKI`)
  * Cisco Router (`CISCO_ROUTER`)
  * Cisco Secure Access (`CISCO_SECURE_ACCESS`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco Umbrella Audit (`CISCO_UMBRELLA_AUDIT`)
  * Cisco Umbrella Cloud Firewall (`UMBRELLA_FIREWALL`)
  * Cisco Umbrella Web Proxy (`UMBRELLA_WEBPROXY`)
  * Cisco vManage SD-WAN (`CISCO_SDWAN`)
  * Cisco WLC/WCS (`CISCO_WIRELESS`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Claroty Xdome (`CLAROTY_XDOME`)
  * Cloudflare (`CLOUDFLARE`)
  * Corelight (`CORELIGHT`)
  * CrowdStrike Alerts API (`CS_ALERTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CyberArk PTA Privileged Threat Analytics (`CYBERARK_PTA`)
  * Cynet 360 AutoXDR (`CYNET_360_AUTOXDR`)
  * Dell Switch (`DELL_SWITCH`)
  * Elastic Windows Event Log Beats (`ELASTIC_WINLOGBEAT`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * FireEye ETP (`FIREEYE_ETP`)
  * FireEye NX (`FIREEYE_NX`)
  * Forcepoint Proxy (`FORCEPOINT_WEBPROXY`)
  * FortiGate (`FORTINET_FIREWALL`)
  * FortiMail Email Security (`FORTINET_FORTIMAIL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortinet Web Application Firewall (`FORTINET_FORTIWEB`)
  * GitHub (`GITHUB`)
  * Google Cloud Audit (`GCP_CLOUDAUDIT`)
  * Google Cloud DNS (`GCP_DNS`)
  * HAProxy (`HAPROXY`)
  * IBM Tape Storages (`IBM_LTO`)
  * Imperva CEF (`IMPERVA_CEF`)
  * Imperva SecureSphere Management (`IMPERVA_SECURESPHERE`)
  * Infoblox DNS (`INFOBLOX_DNS`)
  * Island Browser logs (`ISLAND_BROWSER`)
  * JumpCloud Directory Insights (`JUMPCLOUD_DIRECTORY_INSIGHTS`)
  * Kemp Load Balancer (`KEMP_LOADBALANCER`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * ManageEngine ADAudit Plus (`ADAUDIT_PLUS`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Defender for Office 365 (`MICROSOFT_DEFENDER_MAIL`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft IIS (`IIS`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * MISP Threat Intelligence (`MISP_IOC`)
  * NetApp ONTAP (`NETAPP_ONTAP`)
  * NetIQ eDirectory (`NETIQ_EDIRECTORY`)
  * Netskope V2 (`NETSKOPE_ALERT_V2`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * NGINX (`NGINX`)
  * Noname API Security (`NONAME_API_SECURITY`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * Oracle (`ORACLE_DB`)
  * Oracle Cloud Infrastructure VCN Flow Logs (`OCI_FLOW`)
  * Oracle NetSuite (`ORACLE_NETSUITE`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Palo Alto Prisma Access (`PAN_CASB`)
  * Palo Alto Prisma Cloud Alert payload (`PAN_PRISMA_CA`)
  * Ping Identity (`PING`)
  * Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
  * RSA (`RSA_AUTH_MANAGER`)
  * Salesforce (`SALESFORCE`)
  * Security Command Center Error (`GCP_SECURITYCENTER_ERROR`)
  * Security Command Center Misconfiguration (`GCP_SECURITYCENTER_MISCONFIGURATION`)
  * Security Command Center Observation (`GCP_SECURITYCENTER_OBSERVATION`)
  * Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
  * Security Command Center Threat (`GCP_SECURITYCENTER_THREAT`)
  * Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
  * Security Command Center Unspecified (`GCP_SECURITYCENTER_UNSPECIFIED`)
  * Security Command Center Vulnerability (`GCP_SECURITYCENTER_VULNERABILITY`)
  * Sendmail (`SENDMAIL`)
  * Sentinelone Activity (`SENTINELONE_ACTIVITY`)
  * ServiceNow CMDB (`SERVICENOW_CMDB`)
  * Sophos Firewall (Next Gen) (`SOPHOS_FIREWALL`)
  * Squid Web Proxy (`SQUID_WEBPROXY`)
  * Symantec EDR (`SYMANTEC_EDR`)
  * Symantec Endpoint Protection (`SEP`)
  * Sysdig (`SYSDIG`)
  * Thinkst Canary (`THINKST_CANARY`)
  * Trellix EDRF Trace Data and Telemetry (`TRELLIX_EDRF`)
  * Trend Micro Vision One Detections (`TRENDMICRO_VISION_ONE_DETECTIONS`)
  * Trend Micro Vision One Workbench (`TRENDMICRO_VISION_ONE_WORKBENCH`)
  * Unix system (`NIX_SYSTEM`)
  * Varonis (`VARONIS`)
  * Veeam (`VEEAM`)
  * VMware vCenter (`VMWARE_VCENTER`)
  * VMWare VSphere (`VMWARE_VSPHERE`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Windows Sysmon (`WINDOWS_SYSMON`)
  * wiz.io (`WIZ_IO`)
  * Workday User Activity (`WORKDAY_USER_ACTIVITY`)
  * Zeek JSON (`BRO_JSON`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * ZScaler NGFW (`ZSCALER_FIREWALL`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

  * Cisco Secure Access Enrollment (`CISCO_SECURE_ACCESS_ENROLLMENT`)
  * Cisco Secure Access Network (`CISCO_SECURE_ACCESS_NETWORK`)
  * CyberArk Certificate Manager SaaS (`CYBERARK_CERTIFICATE_MANAGER_SAAS`)
  * Gemini Enterprise Agent Platform (`GEMINI_ENTERPRISE_AGENT_PLATFORM`)
  * Schneider Electric GeoScada OT (`GEOSCADA_OT`)
  * Model Context Protocol Dev (`MCPDEV`)
  * Model Context Protocol Modify (`MCPMODIFY`)
  * Model Context Protocol View (`MCPVIEW`)
  * NetApp Ransomware Resilience (`NETAPP_RANSOMWARE_RESILIENCE`)
  * Netskope Log Streaming (`NETSKOPE_LOG_STREAMING`)
  * Pylon Audit Logs (`PYLON_LOGS`)
  * Reco AI CSPM (`RECO_CSPM`)
  * Salt Security API Protection Platform (`SALT_SECURITY`)
  * SentinelOne Application (`SENTINELONE_APPLICATION`)
  * Wiz Vulnerabilities (`WIZ_VULNERABILITIES`)



## June 26, 2026

Announcement

**Improved documentation portal navigation**

Finding help is now easier! We've updated the navigation of our documentation portal to be primarily user-centric. Sections have been reorganized and renamed to align with your workflows, providing a logical path through the documentation.

We've also added:

  * A [**Support** tab](https://docs.cloud.google.com/chronicle/docs/secops/release-notes) for technical support, changelogs, and release notes
  * A [**Use cases** tab](https://docs.cloud.google.com/chronicle/docs/use-cases) for persona-driven CUJs and workflows

**Note:** Content-level modifications are not included in this update and are scheduled for subsequent phases.

## June 23, 2026

Feature

**[Spotlight Feature] Ask Gemini Cloud Assist in Feed Management**

Google SecOps now provides Gemini Cloud Assist (GCA) directly within the Feed Management interface. Use the new **Ask Gemini Cloud Assist** button to get help with feed creation, setup, and general troubleshooting questions.

Click **Ask Gemini Cloud Assist** to open the Gemini Cloud Assist panel and ask questions to get guidance on:

  * Configuring and managing data feeds.
  * Understanding ingestion pre-requisites and setup steps for different log sources.
  * Resolving common setup issues.



_Note: Gemini Cloud Assist provides recommendations and answers to your questions, but does not perform configuration changes on your behalf. You must apply any recommended changes manually to your feeds._

For more information, see [Feed management overview](https://docs.cloud.google.com/chronicle/docs/administration/feed-management-overview).

Change

**Ingestion metrics reporting correction**

Google Security Operations has resolved an issue where certain ingestion metrics—which are displayed in both the dashboard and Cloud Monitoring—were under-reported.

Because of this correction, you might notice a one-time apparent spike in your ingestion metrics when the update is enabled for your region (between June 29 and July 10, 2026). The actual log volume ingested remains unchanged.

Historical metrics recorded before this update will not be modified or backfilled. This correction does not affect customer billing.

If you have questions or need assistance, contact Google Security Operations support.

Breaking

**Critical Notice: Upcoming reservation of siemAlertId field**

Effective July 5, 2026, the `siemAlertId` field will be strictly reserved for internal Chronicle SIEM alert IDs.

Starting July 5, the system will automatically overwrite any custom or user-supplied data passed through this field. This change impacts all ingestion methods, including the Ingestion API, webhooks, and both first-party and third-party connectors. If you are currently utilizing a custom field named `siemAlertId` in any of your data ingestion configurations, please migrate to a different field name immediately to prevent data loss.

## June 21, 2026

Announcement

**Scheduled Maintenance**

CloudSQL will undergo a scheduled minor upgrade this Sunday, June 21, 2026.

## June 17, 2026

Change

**Auto-collapse setting for the query editor**

You can now configure the query editor to automatically collapse after you run a search, maximizing the screen space available for viewing your search results. By default, the query editor remains expanded.

For more information, see [Configure query editor behavior](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#CollapsequeryEditor).

## June 16, 2026

Announcement

**New Documentation changelogs**

Google SecOps is now releasing a monthly changelog to capture major documentation updates.

For more information, refer to [Documentation changelog](https://docs.cloud.google.com/chronicle/docs/changelogs/changelogs).

## June 13, 2026

Feature

**Non-prioritized IoC Matching rules Category**

Google SecOps has introduced a new detection category, _Non-prioritized IoC Matching rules_ , as part of the [Curated Detections](https://docs.cloud.google.com/chronicle/docs/detection/curated-detections) feature. These rule sets integrate with Google's Indicators of Compromise (IoC) feeds and build on curated threat intelligence to identify malicious activities within Google SecOps environments, specifically focusing on threats identifiable through high-fidelity indicators like IPs, domains, and file hashes.

This rules category provides comprehensive coverage for threats often missed by standard managed content, including cryptomining, Command and Control (C2) communications, and the use of malicious anonymization services.

For more information, refer to [Non-prioritized IoC Matching rules category overview](https://docs.cloud.google.com/chronicle/docs/detection/non-prioritized-ioc-matching-threats-category).

## June 12, 2026

Feature

**[Spotlight Feature] Search for cases using SIEM Search**

Google SecOps SIEM Search now provides robust capabilities for analyzing cases and case history alongside existing Unified Data Model (UDM) events and entities. This update allows security analysts to seamlessly correlate case details with other security telemetry within a single interface, streamlining workflows and accelerating incident response.

Key Highlights:

  * **Unified Search Experience** : Conduct searches across UDM events, entities, cases, and case history from a single SIEM Search interface.

  * **Correlate SIEM and SOAR Data** : Effortlessly link case details and historical activities with security data, reducing context switching and improving investigation efficiency.




For more information, see [Search cases and case history](https://docs.cloud.google.com/chronicle/docs/investigation/search-and-search-case-history).

Feature

**[Spotlight Feature] Investigate detections in Google SecOps Search**

Google SecOps Search now supports querying, filtering, and analyzing system-generated detections. When searching on events or entities, matching detections will now appear in the **Alerts and Detections** tab, providing a more holistic workflow for threat investigation.

For more details, see [Investigate detections in Search](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-detections-in-search).

Announcement

**Asynchronous Search APIs for large datasets**

Google SecOps now supports asynchronous Search APIs that let you perform long-running queries without blocking your applications. This is ideal for searches that return a large volume of results.

  * **Non-blocking queries** : Initiate searches and receive an operation ID to track progress, so your application remains responsive.
  * **Handle large result sets** : Retrieve up to 1 million results from data sources including Unified Data Model (UDM) events, data tables, and Entity Context Graph (ECG).
  * **Paginated results** : View results efficiently in manageable pages.



For more information, see [Asynchronous Search APIs](https://docs.cloud.google.com/chronicle/docs/investigation/search-lro-api) and [Result limits for data sources](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#resultLimitsDataSources).

## June 09, 2026

Feature

**UDM fields now show the sources of enrichment**

The new Enrichment feature introduces improvements for managing and understanding your data. Each UDM field is now labeled with an icon to indicate its data source: U for unenriched fields and E for enriched fields. Enriched fields contain additional metadata values that indicate the source of the enriched data.

**Note:** The Enrichment feature requires the `chronicle.events.fetchEnrichedEvent` IAM permission. If you're using custom IAM roles, you must add one of the following permissions to your custom policies: `chronicle.googleapis.com/limitedViewer`, `chronicle.googleapis.com/restrictedDataAccessViewer`, or `chronicle.googleapis.com/viewer`.

For more information, see: [Viewing events](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment#viewing_events).

## June 01, 2026

Announcement

The [Manage access to preview features feature](https://docs.cloud.google.com/chronicle/docs/secops/release-notes#May_28_2026) has been rolled back.

## May 31, 2026

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

  * 1Password Audit Events (`ONEPASSWORD_AUDIT_EVENTS`)
  * AIX system (`AIX_SYSTEM`)
  * Apache (`APACHE`)
  * Aruba EdgeConnect SD-WAN (`ARUBA_EDGECONNECT_SDWAN`)
  * Avaya Aura Experience Portal (`AVAYA_AURA`)
  * AWS CloudFront (`AWS_CLOUDFRONT`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS GuardDuty (`GUARDDUTY`)
  * AWS Security Hub (`AWS_SECURITY_HUB`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Organizational Context (`AZURE_AD_CONTEXT`)
  * Azure AD Sign-In (`AZURE_AD_SIGNIN`)
  * Azure SQL (`AZURE_SQL`)
  * Azure Storage Audit (`AZURE_STORAGE_AUDIT`)
  * Barracuda WAF (`BARRACUDA_WAF`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Chrome Management (`CHROME_MANAGEMENT`)
  * Cisco ACS (`CISCO_ACS`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Secure Access (`CISCO_SECURE_ACCESS`)
  * Cisco Secure Workload (`CISCO_SECURE_WORKLOAD`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco Umbrella Audit (`CISCO_UMBRELLA_AUDIT`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Claroty Xdome (`CLAROTY_XDOME`)
  * Claude Compliance Logs (`CLAUDE_COMPLIANCE_LOGS`)
  * Cloudflare (`CLOUDFLARE`)
  * Cloudflare Warp (`CLOUDFLARE_WARP`)
  * Corelight (`CORELIGHT`)
  * CrowdStrike Alerts API (`CS_ALERTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CyberArk (`CYBERARK`)
  * CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
  * Duo Administrator Logs (`DUO_ADMIN`)
  * EfficientIP DDI (`EFFICIENTIP_DDI`)
  * Elastic Audit Beats (`ELASTIC_AUDITBEAT`)
  * Elastic Windows Event Log Beats (`ELASTIC_WINLOGBEAT`)
  * F5 ASM (`F5_ASM`)
  * Forcepoint Proxy (`FORCEPOINT_WEBPROXY`)
  * FortiGate (`FORTINET_FIREWALL`)
  * GitHub (`GITHUB`)
  * Google Cloud Asset Inventory (`GCP_CLOUD_ASSET_INVENTORY`)
  * Google Cloud Audit (`GCP_CLOUDAUDIT`)
  * Google Compute Context (`GCP_COMPUTE_CONTEXT`)
  * Google Threat Intelligence IOC (`GTI_IOC`)
  * GTB Technologies DLP (`GTB_DLP`)
  * HP Aruba (ClearPass) (`CLEARPASS`)
  * IBM Websphere Application Server (`IBM_WEBSPHERE_APP_SERVER`)
  * IBM z/OS (`IBM_ZOS`)
  * Imperva (`IMPERVA_WAF`)
  * Imperva CEF (`IMPERVA_CEF`)
  * Imperva DRA (`IMPERVA_DRA`)
  * Imperva SecureSphere Management (`IMPERVA_SECURESPHERE`)
  * Island Browser logs (`ISLAND_BROWSER`)
  * Juniper (`JUNIPER_FIREWALL`)
  * Juniper Mist (`JUNIPER_MIST`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * LastPass Password Management (`LASTPASS`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft Defender for Office 365 (`MICROSOFT_DEFENDER_MAIL`)
  * Microsoft IIS (`IIS`)
  * Mobileiron (`MOBILEIRON`)
  * Mongo Database (`MONGO_DB`)
  * MySQL (`MYSQL`)
  * Netapp Storagegrid (`NETAPP_STORAGEGRID`)
  * Netskope V2 (`NETSKOPE_ALERT_V2`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * NGFW Enterprise (`GCP_NGFW_ENTERPRISE`)
  * Office 365 (`OFFICE_365`)
  * Office 365 Message Trace (`OFFICE_365_MESSAGETRACE`)
  * Okta Scaleft (`OKTA_SCALEFT`)
  * Oracle (`ORACLE_DB`)
  * Oracle Cloud Infrastructure Audit Logs (`OCI_AUDIT`)
  * Orca Cloud Security Platform (`ORCA`)
  * Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * Red Hat Directory Server LDAP (`REDHAT_DIRECTORY_SERVER`)
  * Red Hat OpenShift (`REDHAT_OPENSHIFT`)
  * Salesforce (`SALESFORCE`)
  * Sangfor Next Generation Firewall (`SANGFOR_NGAF`)
  * Security Command Center Error (`GCP_SECURITYCENTER_ERROR`)
  * Security Command Center Misconfiguration (`GCP_SECURITYCENTER_MISCONFIGURATION`)
  * Security Command Center Observation (`GCP_SECURITYCENTER_OBSERVATION`)
  * Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
  * Security Command Center Threat (`GCP_SECURITYCENTER_THREAT`)
  * Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
  * Security Command Center Unspecified (`GCP_SECURITYCENTER_UNSPECIFIED`)
  * Security Command Center Vulnerability (`GCP_SECURITYCENTER_VULNERABILITY`)
  * SentinelOne Singularity Cloud Funnel (`SENTINELONE_CF`)
  * ServiceNow Security (`SERVICENOW_SECURITY`)
  * Sourcefire (`SOURCEFIRE_IDS`)
  * Suricata EVE (`SURICATA_EVE`)
  * Symantec Endpoint Protection (`SEP`)
  * Sysdig (`SYSDIG`)
  * Trend Micro Deep Security (`TRENDMICRO_DEEP_SECURITY`)
  * Trend Micro Vision One Observerd Attack Techniques (`TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES`)
  * Ubiquiti UniFi Switch (`UBIQUITI_SWITCH`)
  * Unix system (`NIX_SYSTEM`)
  * Upwind (`UPWIND`)
  * VMware ESXi (`VMWARE_ESX`)
  * VMWare VSphere (`VMWARE_VSPHERE`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Wiz.io (`WIZ_IO`)
  * Workday User Activity (`WORKDAY_USER_ACTIVITY`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * Zscaler CASB (`ZSCALER_CASB`)
  * Zscaler DLP (`ZSCALER_DLP`)
  * Zscaler Private Access (`ZSCALER_ZPA`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

  * Azure Software Vulnerabilities (`AZURE_SOFTWARE_VULNERABILITIES`)
  * Caller Verify (`CALLER_VERIFY`)
  * CertSecure Log (`CERTSECURE_LOG`)
  * Cisco MultiCloud Defense Firewall (`CISCO_MULTICLOUD_DEFENSE_FIREWALL`)
  * Cursor (`CURSOR`)
  * Cyfirma (`CYFIRMA_DECYFIR_LOG`)
  * Databahn (`DATABAHN`)
  * Flare Darkweb Alerts (`FLARE_DARKWEB_ALERTS`)
  * Fortinet FortiAppSec Cloud (`FORTINET_FORTIAPPSEC`)
  * Hikvision Network Video Recorders (`HIKVISION_NVR`)
  * IBM B2B Integrator (`IBM_B2B_INTEGRATOR`)
  * IBM InfoSphere Virtual Data Pipeline (`IBM_VDP`)
  * Imperva Account TakeOver (`IMPERVA_ATO`)
  * Imperva Client Side Protection (`IMPERVA_CSP`)
  * Imperva DNS (`IMPERVA_DNS`)
  * Imperva Network Security (`IMPERVA_NETWORK_SECURITY`)
  * Microsoft Defender XDR (`MICROSOFT_DEFENDER_XDR`)
  * Nakivo Backup and Recovery (`NAKIVO_BACKUP`)
  * Netcraft Takedown (`NETCRAFT_TAKEDOWN`)
  * Next Level Performance Amplify (`NXL_AMPLIFY`)
  * Siemens Desigo (`SIEMENS_DESIGO`)



## May 28, 2026

Feature

**[Spotlight Feature] Unified and Upgraded Chronicle API**

[Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest) has been unified with API resources from [legacy SOAR API](https://docs.cloud.google.com/chronicle/docs/soar/reference/working-with-chronicle-soar-apis). Further, we've upgraded the following Chronicle API resources from v1 beta to v1. This upgrade signals API stability and functional completeness, enabling customer and partner adoption for production usage. We recommend that customers and partners use Chronicle API for a more robust, secure, and extensible experience. Learn more about [API Stability](https://google.aip.dev/181).

The following features and resources are included in this update:

**Feature** | **Chronicle API Resources upgraded to v1**  
---|---  
Alerts and ATIs, UEBA  | [Threat Collection](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.threatCollections), [IoC](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.iocs), [CoverageDetail](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.coverageDetails), [EntityRisk](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getRiskConfig)  
Dashboards  | [NativeDashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.nativeDashboards), [DashboardChart](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dashboardCharts), [DashboardQuery](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dashboardQueries), [FeaturedContentNativeDashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.featuredContentNativeDashboards)  
Data Tables  | [DataTable](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataTables), [DataTableRow](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataTables.dataTableRows), [DataTableOperationError](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataTableOperationErrors)  
Ingestion  | [Logs](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.logs), [Feed](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.feeds), [LogTypeSchema](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.feedSourceTypeSchemas.logTypeSchemas), [FeedSourceSchema](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.feedSourceTypeSchemas), [FeedPack](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.feedPacks), [Forwarder](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.forwarders)  
Normalization  | [Logtype](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes), [Parser](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.parsers), [IngestionLogLabel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.ingestionLogLabels)  
Detections  | [FindingsRefinement](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.findingsRefinements), [VerifyRuleText](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/verifyRuleText), [FeaturedContentRule](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.featuredContentRules), [RuleExecutionError](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.ruleExecutionErrors)  
Search & Investigation  | [Event](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.events), [Entity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.entities), [SearchQuery](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries), [SavedColumnSet](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.savedColumnSets)  
Exports  | [BigQueryExportService](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.bigQueryExport)  
Enrichment Controls  | [EnrichmentControl](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.enrichmentControls), [EnrichmentCombination](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getEnrichmentCombination)  
SOAR  | [Case](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases), [CaseAlert](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts), [CaseStageDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseStageDefinitions), [CaseTagDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions), [CaseQueueFilter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters), [CaseCloseDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseCloseDefinitions), [ContextProperty](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.contextProperties), [InvolvedEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts.involvedEntities), [Task](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.tasks), [CaseComment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments), [CaseWallRecord](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords), [ChatMessage](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages), [View](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.views), [VisualFamily](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.ontologyRecords.visualFamilies), [ChatMessages.attachment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages.attachments), [ContentPack](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks), [SocRole](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.socRoles), [EmailTemplate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.emailTemplates), [DynamicParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dynamicParameters), [EntitiesBlocklist](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.entitiesBlocklists), [Environment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environments), [EnvironmentGroup](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.environmentGroups), [Integration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations), [Integrationaction](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.actions), [UserNotification](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.legacySoarUsers.userNotifications), [Integrationactionrevision](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.actions.revisions), [Connector](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors), [ConnectorInstance](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances), [RemoteAgent](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.remoteAgents), [Connectorlog](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.connectorInstances.logs), [Connectorrevision](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.connectors.revisions), [IntegrationInstance](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.integrationInstances), [UniqueEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.uniqueEntities), [Integrationsjob](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.jobs), [JobInstance](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.jobs.jobInstances), [JobInstances.log](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.jobs.jobInstances.logs), [Jobs.revision](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.jobs.revisions), [Integrationmanager](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers), [Integrationmanagerrevision](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.integrations.managers.revisions), [AlertGroupingRule](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules), [Announcement](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.announcements), [Attachment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.legacySoarUsers.attachments), [CustomList](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.customLists), [FormDynamicParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.formDynamicParameters), [MarketplaceIntegration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.marketplaceIntegrations), [ModuleSetting](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.moduleSettings), [SlaDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.slaDefinitions), [NotificationSetting](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.legacySoarUsers/getNotificationSettings), [PropertySchemaDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.propertySchemaDefinitions), [RequestTemplate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.requestTemplates), [SoarDomain](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.soarDomains), [SoarNetwork](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.soarNetworks), [WorkdeskLink](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.legacySoarUsers.workdeskLinks), [SystemNotification](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.systemNotifications), [WorkdeskContact](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.legacySoarUsers.workdeskContacts), [WorkdeskNote](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.legacySoarUsers.workdeskNotes), [LegacySoarUsers.localization](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.legacySoarUsers/getLocalization).   
  
For a full list of updated resources and links to the documentation, please see the [Chronicle API documentation](https://docs.cloud.google.com/chronicle/docs/reference/rest).

Feature

**[Spotlight Feature] Manage access to preview features**

Google SecOps tenant administrators can enable or disable access to public preview features. Previously, all public preview features needed to be enabled through official Support channels.

The new **Public Preview Features** page lists all the public preview features, the status of each feature (on or off)—along with (when available) the expected GA date and a link to a relevant user guide.

**Note:** In [compliance-controlled tenants](https://docs.cloud.google.com/chronicle/docs/onboard#set-up-assured-workloads-folder) (for example, FedRAMP or HIPAA), using the **Public Preview Features** page to turn features on and off isn't available. In these tenants, you must contact Google SecOps support to get public preview features enabled.

For more information, see [Manage access to preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage).

**Note:** It might take one to six days before you see the changes reflected in your region.

## May 27, 2026

Feature

**Standard parser support policy**

Google SecOps introduced a focused support policy for Standard parsers to scale platform stability, predictable performance, and high-quality data normalization. The new policy structures service level objectives (SLOs) and request triaging by customer support tiers (Standard versus Expert/Expert+), and prioritizes core security data through [Important UDM Fields](https://docs.cloud.google.com/chronicle/docs/reference/important-udm-fields). Additionally, the policy outlines a community-driven model where low-usage, longtail prebuilt parsers migrate to a dedicated GitHub repository maintained by partners and the Google SecOps community. 

For more information, see [Standard parser support policy](https://docs.cloud.google.com/chronicle/docs/ingestion/standard-parser-support-policy).

## May 24, 2026

Feature

**[Spotlight Feature] Create and manage calculated fields**

The Calculated Fields feature is now available in Preview. With Calculated Fields, you can dynamically derive new data points within Google Security Operations cases and alerts. By defining logical formulas, you can compute values based on existing system or custom fields. The calculated value is automatically evaluated and stored in a user-selected, pre-existing custom field (labeled **Target Field**) in real time.

For more information, see [Create and manage calculated fields](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/calculated-fields).

Change

**Time range selection for searches**

Google SecOps has now added relative and absolute time range options to define the required time period for retrieving search results.

  * **Relative time range** : Set a search window looking backward from the current time using custom intervals.
  * **Absolute time range** : Define fixed start and end times using calendar presets, exact date and time selections, or event-based timeframes.



For more information, see [Set the date and time range](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#setDateTime).

**Note:** This change follows a phased rollout from **May 12, 2026** , to **May 18, 2026**. Reach out to support if you do not see the new limits applied to your environment after **May 18, 2026**.

## May 18, 2026

Feature

**[Spotlight Feature] Enhanced Data Export API general availability and improvements**

The Data Export API is now GA and introduces significant security and capability improvements. This feature facilitates the bulk export of your security data from Google SecOps to a Google Cloud Storage bucket that you control, and it provides a more secure and scalable data archival experience than the legacy Data Export API feature.

Here's what's new:

  * **Advanced data filtering** : the API now lets you additionally scope export jobs using namespaces and ingestion labels.
  * **Zero-trust security (customer-managed encryption keys)** : full integration with Google Cloud Key Management Service (KMS) ensures that all exported data is encrypted with customer-managed keys.
  * **Identity-aware extraction (RBAC)** : export jobs now inherit the data RBAC scope of users creating an export job, preventing unauthorized data extraction.

**Note:** It might take one to six days before you see the changes reflected in your region. **Important:** You need to update your API settings to call the new `v1` endpoint instead of the `v1alpha` endpoint. For example, to create a new data export job, you need to update the existing endpoint `POST https://chronicle.{region}.rep.googleapis.com/v1alpha/{parent}/dataExports` to the new endpoint `POST https://chronicle.{region}.rep.googleapis.com/v1/{parent}/dataExports`.

For more information, see [Data Export API (enhanced)](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api-enhanced).

Deprecated

The legacy Data Export API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) in favor of the [enhanced Data Export API](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api-enhanced), which provides a more secure and scalable data archival experience. After June 18, 2026, legacy Data Export API won't work.

Deprecated

The [`fetchavailablelogtypes`](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataExports/fetchavailablelogtypes) API endpoint is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) in favor of the [`list` endpoint](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.logTypes/list). After June 18, 2026, the `fetchavailablelogtypes` API endpoint won't work.

Deprecated

The `updateDataExport` endpoint in the enhanced Data Export API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations). The reduction in job queue times using the [enhanced Data Export API](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api-enhanced) has eliminated the need for the update functionality of the `updateDataExport` API endpoint. The `updateDataExport` endpoint was present in v1alpha only; it wasn't present in in v1beta or v1. After June 18, 2026, the `updateDataExport` API endpoint won't work. You can still cancel queued export jobs.

Deprecated

The [`logType`](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataExports#DataExport:%7E:text=05%3A30%22.-,logType,to%20export.%20Format%3A%20projects/%7Bproject%7D/locations/%7Blocation%7D/instances/%7Binstance%7D/logTypes/%7BlogType%7D,-gcsBucket) field in the enhanced Data Export API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) in favor of the new (optional)`includeLogTypes` field, which supports an array of log types for data filtering. If left blank, the export job includes all log types by default. The `logType` field was present in v1alpha only; it wasn't present in in v1beta or v1. After June 18, 2026, the `logType` field is discontinued. 

## May 17, 2026

Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

  * [Collect Arista VeloCloud SD-WAN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/velo-firewall)
  * [Collect Microsoft Defender for Endpoint logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-defender-atp)
  * [Collect PTC Windchill logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/windchill)
  * [Collect Riverbed SteelHead logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/steelhead)
  * [Collect Sangfor Proxy logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sangfor-proxy)
  * [Collect SAP BTP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-btp)
  * [Collect SAP NetWeaver logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-netweaver)
  * [Collect SAP SM20 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-sm20)
  * [Collect SAP SuccessFactors logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-successfactors)
  * [Collect SAP Sybase ASE logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-ase)
  * [Collect Saviynt Enterprise Identity Cloud logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/saviynt-eip)
  * [Collect SecureLink logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/securelink)
  * [Collect Semperis DSP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/semperis-dsp)
  * [Collect Sonrai Security logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sonrai)
  * [Collect SOTI MobiControl logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/soti-mobicontrol)
  * [Collect Splunk Attack Analyzer logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/splunk-attack-analyzer)
  * [Collect SpyCloud logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/spycloud)
  * [Collect Stealthbits Audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stealthbits-audit)
  * [Collect Stealthbits StealthDEFEND logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stealthbits-defend)
  * [Collect STIX Threat Intelligence logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stix)
  * [Collect Swift Alliance Messaging Hub logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/swift-amh)
  * [Collect Symantec Messaging Gateway logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/symantec-mail)
  * [Collect Symantec Security Analytics logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/symantec-sa)
  * [Collect Tableau logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/tableau)
  * [Collect Talon logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/talon)
  * [Collect TCPWave DDI logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi)
  * [Collect Teleport Access Plane logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/teleport-access-plane)
  * [Collect Tenable Audit logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/tenable-audit)
  * [Collect Tenable CSPM logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/tenable-cspm)
  * [Collect Teradata Database logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/teradata-db)
  * [Collect Terraform Enterprise logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/terraform-enterprise)
  * [Collect Tetragon eBPF audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tetragon-ebpf-audit-logs)
  * [Collect ThreatLocker Platform logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatlocker)
  * [Collect ThreatX WAF logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatx-waf)
  * [Collect Tintri logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tintri)
  * [Collect Trend Micro Apex Central logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-apex-central)
  * [Collect uberAgent logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/uberagent)
  * [Collect Ubika WAF logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ubika-waf)
  * [Collect UKG logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ukg)
  * [Collect UPX AntiDDoS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/upx-antiddos)
  * [Collect Verba Recording System logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/verba-rec)
  * [Collect Vercel WAF logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/vercel-waf)
  * [Collect Virtru Email Encryption logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/virtru-email-encryption)
  * [Collect WatchGuard EDR logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/watchguard-edr)
  * [Collect Windows AppLocker logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/windows-applocker)
  * [Collect Windows Defender Antivirus logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/windows-defender-av)
  * [Collect Windows Firewall logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/windows-firewall)
  * [Collect Windows Hyper-V logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/windows-hyperv)
  * [Collect Windows Network Policy Server logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/windows-net-policy-server)



## May 05, 2026

Change

Google SecOps has updated the list of [supported default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers). Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

  * Akeyless Vault Platform (`AKEYLESS_VAULT`)
  * Apache Cassandra (`CASSANDRA`)
  * Aruba (`ARUBA_WIRELESS`)
  * Aruba EdgeConnect SD-WAN (`ARUBA_EDGECONNECT_SDWAN`)
  * Auth0 (`AUTH_ZERO`)
  * AWS Aurora (`AWS_AURORA`)
  * AWS EC2 VPCs (`AWS_EC2_VPCS`)
  * AWS Security Hub (`AWS_SECURITY_HUB`)
  * Azure Firewall (`AZURE_FIREWALL`)
  * Azure Front Door (`AZURE_FRONT_DOOR`)
  * Barracuda CloudGen Firewall (`BARRACUDA_CLOUDGEN_FIREWALL`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Check Point Sandblast (`CHECKPOINT_EDR`)
  * Checkpoint SmartDefense (`CHECKPOINT_SMARTDEFENSE`)
  * Chronicle SOAR Audit (`CHRONICLE_SOAR_AUDIT`)
  * Cisco Application Centric Infrastructure (`CISCO_ACI`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco FireSIGHT Management Center (`CISCO_FIRESIGHT`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Meraki (`CISCO_MERAKI`)
  * Cisco Secure Access (`CISCO_SECURE_ACCESS`)
  * Cisco Secure Workload (`CISCO_SECURE_WORKLOAD`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco Umbrella Audit (`CISCO_UMBRELLA_AUDIT`)
  * Cisco WLC/WCS (`CISCO_WIRELESS`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Claroty Xdome (`CLAROTY_XDOME`)
  * Cloudflare Warp (`CLOUDFLARE_WARP`)
  * CrowdStrike Alerts API (`CS_ALERTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CyberArk (`CYBERARK`)
  * CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
  * EPIC Systems (`EPIC`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP Access Policy Manager (`F5_BIGIP_APM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * F5 Distributed Cloud Services (`F5_DCS`)
  * FireEye eMPS (`FIREEYE_EMPS`)
  * FireEye NX (`FIREEYE_NX`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiEDR (`FORTINET_FORTIEDR`)
  * Fortinet Proxy (`FORTINET_WEBPROXY`)
  * GitHub (`GITHUB`)
  * Google Cloud Audit (`GCP_CLOUDAUDIT`)
  * Google Threat Intelligence IOC (`GTI_IOC`)
  * Guardicore Centra (`GUARDICORE_CENTRA`)
  * HP Aruba (ClearPass) (`CLEARPASS`)
  * Huawei Switches (`HUAWEI_SWITCH`)
  * IBM Websphere Application Server (`IBM_WEBSPHERE_APP_SERVER`)
  * IBM z/OS (`IBM_ZOS`)
  * Imperva SecureSphere Management (`IMPERVA_SECURESPHERE`)
  * Infoblox (`INFOBLOX`)
  * Juniper (`JUNIPER_FIREWALL`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * ManageEngine ADManager Plus (`ADMANAGER_PLUS`)
  * McAfee ePolicy Orchestrator (`MCAFEE_EPO`)
  * McAfee Web Gateway (`MCAFEE_WEBPROXY`)
  * Microsoft Defender For Cloud (`MICROSOFT_DEFENDER_CLOUD_ALERTS`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Defender for Identity (`MICROSOFT_DEFENDER_IDENTITY`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft IIS (`IIS`)
  * Mobileiron (`MOBILEIRON`)
  * Model Armor (`GCP_MODEL_ARMOR`)
  * MySQL (`MYSQL`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * Noname API Security (`NONAME_API_SECURITY`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * Oracle Cloud Infrastructure Audit Logs (`OCI_AUDIT`)
  * Oracle NetSuite (`ORACLE_NETSUITE`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Palo Alto Prisma Access (`PAN_CASB`)
  * Palo Alto Prisma Cloud Alert payload (`PAN_PRISMA_CA`)
  * Ping Identity (`PING`)
  * PostFix Mail (`POSTFIX_MAIL`)
  * Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Proofpoint Threat Response (`PROOFPOINT_TRAP`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * Rapid7 Insight (`RAPID7_INSIGHT`)
  * SAP Hana Audit (`SAP_HANA_AUDIT`)
  * SecureAuth (`SECUREAUTH_SSO`)
  * Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
  * Security Command Center Threat (`GCP_SECURITYCENTER_THREAT`)
  * Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
  * SentinelOne Deep Visibility (`SENTINEL_DV`)
  * SentinelOne Singularity Cloud Funnel (`SENTINELONE_CF`)
  * Silverfort Authentication Platform (`SILVERFORT`)
  * SiteMinder Web Access Management (`CA_SSO_WEB`)
  * SonicWall (`SONIC_FIREWALL`)
  * Squid Web Proxy (`SQUID_WEBPROXY`)
  * STIX Threat Intelligence (`STIX`)
  * Suricata EVE (`SURICATA_EVE`)
  * Sysdig (`SYSDIG`)
  * Tanium Threat Response (`TANIUM_THREAT_RESPONSE`)
  * Thinkst Canary (`THINKST_CANARY`)
  * Trend Micro Apex one (`TRENDMICRO_APEX_ONE`)
  * Unix system (`NIX_SYSTEM`)
  * Vectra XDR (`VECTRA_XDR`)
  * VMware ESXi (`VMWARE_ESX`)
  * Wallix Bastion (`WALLIX_BASTION`)
  * WatchGuard (`WATCHGUARD`)
  * Windows Defender AV (`WINDOWS_DEFENDER_AV`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * wiz.io (`WIZ_IO`)
  * Zscaler Email DLP (`ZSCALER_EMAIL_DLP`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

  * Altiris Logs (`ALTIRIS_LOGS`)
  * Aruba Access Point (`ARUBA_AP`)
  * BloxOne Threat Defense DHCP (`BLOXONE_DHCP`)
  * Checkmarx One (`CHECKMARX_ONE`)
  * Cisco Nexus Dashboard Orchestrator (`CISCO_NDO`)
  * CrowdStrike Cloud Security (`CROWDSTRIKE_CSPM`)
  * F5 F5OS-A Logging (`F5_F5OS_A`)
  * GateWatcher NDR (`GATEWATCHER_NDR`)
  * Hashicorp Terraform (`HASHICORP_TERRAFORM`)
  * Jamf Protect Alerts V2 (`JAMF_PROTECT_V2`)
  * Oracle Cloud Infrastructure Web Application Firewall (`OCI_WAF`)
  * Qualys File Integrity Monitoring (`QUALYS_FIM`)
  * SailPoint IdentityNow (`SAILPOINT_IDENTITYNOW`)
  * ServiceNow Certificate Logs (`SERVICENOW_CERTIFICATE`)
  * ServiceNow User Logs (`SERVICENOW_USER`)
  * ServiceNow User Login History (`SERVICENOW_USER_LOGIN_HISTORY`)
  * SiteGuard Server (`SITEGUARD_SERVER`)
  * Tosi Hub (`TOSI_HUB`)
  * Trellix Network Detection and Response (`TRELLIX_NDR`)



## May 03, 2026

Feature

**Enhanced "Time to respond" options for multi-choice questions**

Google SecOps now provides more granular control over playbook execution when the "time to respond" for a **MultiChoiceQuestion** step is exceeded. When configuring a multi-choice question, you can now choose to proceed with one of the predefined answer branches or to create a dedicated branch to handle this scenario.

For more information, see [Add a multi-choice question flow](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-flows-in-playbooks#multi-choice).

## April 30, 2026

Feature

**VPC Service Controls for Google SecOps general availability**

VPC Service Controls is now GA. This feature helps to create perimeters and protect resources and services data from accidental or targeted action by external or insider entities. This in turn can minimize unwarranted data exfiltration risks from Google Cloud services. For more information, see [Configure VPC Service Controls for Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops) and [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## April 27, 2026

Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

  * [Collect Group-IB Threat Intelligence logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/group-ib)
  * [Collect Microsoft System Center Endpoint Protection (SCEP) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-scep)
  * [Collect Nagios XI logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nagios)
  * [Collect Neo4j Aura logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/neo4j)
  * [Collect Nucleus Security - Nucleus Unified Vulnerability Management logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nucleus-vulnerability)
  * [Collect Nyansa Voyance / VMware Edge Network Intelligence logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nyansa-events)
  * [Collect Okera Dynamic Access Platform (ODAP) audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okera-dap)
  * [Collect Okta Advanced Server Access logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta-scaleft)
  * [Collect Onapsis Platform logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onapsis)
  * [Collect One Identity TPAM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oneidentity-tpam)
  * [Collect Oracle Cloud Infrastructure - Oracle Cloud Guard logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oci-cloudguard)
  * [Collect Cisco Identity Intelligence logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/oort)
  * [Collect Microsoft SharePoint (Office 365) logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/sharepoint)
  * [Collect NetApp Console (formerly BlueXP) audit logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/netapp-bluexp)
  * [Collect Netwrix Auditor logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/netwrix)
  * [Collect Nokia VitalQIP DDI logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/vitalqip)
  * [Collect OpenAI Audit logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/openai-auditlog)
  * [Collect OpenTelemetry Netflow Receiver logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/netflow-otel)
  * [Collect Oracle Fusion Cloud Applications logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/oracle-fusion)
  * [Collect Oracle NetSuite - NetSuite Applications Suite logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/net-suite)
  * [Collect Oracle NetSuite logs](https://clouddocs.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/oracle-netsuite)
  * [Collect Vectra Alerts logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-alerts)
  * [Collect Vectra XDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-xdr)
  * [Collect Windows Event logs (XML format)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/winevtlog-xml)
  * [Collect WinSCP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/winscp)
  * [Collect Workday User Activity logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday-user-activity)
  * [Collect WP Engine logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wpengine)
  * [Collect XAMS by Xiting logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/xiting-xams)
  * [Collect Yubico OTP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/yubico-otp)
  * [Collect Zero Networks logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zero-networks)
  * [Collect Zix Email Encryption logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zix-email-encryption)
  * [Collect Zscaler NSS Feeds for Alerts logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-nss-feeds)
  * [Collect ZyXEL ZyWALL logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zywall)



## April 22, 2026

Deprecated

Support for the legacy Google Security Operations SIEM infrastructure will end on April 30, 2027. After this date, you will no longer have access to your Google SecOps SIEM instance on the legacy infrastructure. You need to self-migrate Google Security Operations SIEM in legacy Infrastructure to Google Cloud to align with industry standards and improve your reliability, privacy, security, compliance, and granular access controls. Follow the [Migration guide](https://docs.cloud.google.com/chronicle/docs/administration/migrate-legacy-siem-infra) and [Community post](https://security.googlecloudcommunity.com/community-blog-42/elevate-your-defense-modernizing-google-secops-for-the-agentic-soc-7087) to begin your transition. 

This migration applies to you **only** if your SIEM instance meets **one of the conditions** below:

  * Not deployed in your Google Cloud Project
  * Not using Google Cloud Authentication (Workforce Identity Federation / Cloud Identity)
  * Not using Google Cloud IAM for Feature Role based access controls.



This migration **does not apply** to you if your SIEM instance meets **all the conditions** below:

  * Is deployed in your Google Cloud project
  * Uses Workforce Identity Federation or Cloud Identity for authentication
  * Uses Google Cloud IAM to manage granular access permissions



## April 15, 2026

Feature

**[Spotlight Feature] Unified and upgraded Chronicle API**

[Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=africa-south1) has been unified with API resources from [legacy SOAR API](https://docs.cloud.google.com/chronicle/docs/soar/reference/working-with-chronicle-soar-apis). In addition, we've upgraded the following Chronicle API resources from alpha to beta. This upgrade signals [API Stability](https://google.aip.dev/181) and functional completeness, enabling customer and partner adoption for production usage. We recommend customers use Chronicle API for a more robust, secure, and extensible experience.

For more information, see [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=africa-south1).

**Feature** | **Chronicle API Resources upgraded to v1 Beta**  
---|---  
Alerts and ATIs, UEBA  | [ThreatCollection](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.threatCollections), [IoC](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocs), [CoverageDetail](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.coverageDetails), [EntityRisk](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/getRiskConfig?rep_location=africa-south1)  
Dashboards  | [NativeDashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.nativeDashboards), [DashboardChart](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dashboardCharts), [DashboardQuery](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dashboardQueries), [FeaturedContentNativeDashboard](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.contentHub.featuredContentNativeDashboards)  
Data Tables  | [DataTable](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables), [DataTableRow](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows), [DataTableOperationError](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTableOperationErrors)  
Ingestion  | [Logs](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.logTypes.logs), [Feed](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.feeds), [LogTypeSchema](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.feedSourceTypeSchemas.logTypeSchemas), [FeedSourceSchema](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.feedSourceTypeSchemas), [FeedPack](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.feedPacks), [Forwarder](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.forwarders), [Collector](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.forwarders.collectors)  
Normalization  | [Logtype](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.logTypes), [Parser](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.logTypes.parsers), [IngestionLogLabel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.ingestionLogLabels)  
Detections  | [FindingsRefinement](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.findingsRefinements), [VerifyRuleText](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/verifyRuleText), [FeaturedContentRule](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.contentHub.featuredContentRules), [RuleExecutionError](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.ruleExecutionErrors)  
Search & Investigation  | [Event](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.events), [Entity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.entities), [SearchQuery](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.users.searchQueries), [SavedColumnSet](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.savedColumnSets)  
Exports  | [BigQueryExportService](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.bigQueryExport)  
Enrichment Controls  | [EnrichmentControl](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.enrichmentControls), [EnrichmentCombination](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/getEnrichmentCombination)  
SOAR  | [Case](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases), [CaseAlert](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.caseAlerts), [CaseStageDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.caseStageDefinitions), [CaseTagDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.caseTagDefinitions), [CaseQueueFilter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.caseQueueFilters), [CaseCloseDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.caseCloseDefinitions), [ConnectorEvent](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.caseAlerts.connectorEvents), [CustomFieldValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.alerts.customFieldValues), [ContextProperty](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.caseAlerts.contextProperties), [InvolvedEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.caseAlerts.involvedEntities), [Task](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.tasks), [Webhook](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.webhooks) [CaseComment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.caseComments), [CaseWallRecord](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.caseWallRecords), [ChatMessage](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.chatMessages), [View](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.views), [VisualFamily](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.ontologyRecords.visualFamilies),  [ChatMessages.attachment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.chatMessages.attachments), [CustomFieldValues](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.customFieldValues), [ContentPack](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.contentHub.contentPacks), [SocRole](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.socRoles), [EmailTemplate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates), [DynamicParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dynamicParameters), [EntitiesBlocklist](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.entitiesBlocklists), [Environment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.environments), [EnvironmentGroup](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.environmentGroups), [Integration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations), [Integrationaction](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.actions), [UserNotification](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.legacySoarUsers.userNotifications), [Integrationactionrevision](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.actions.revisions), [Connector](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.connectors), [ConnectorInstance](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.connectors.connectorInstances), [RemoteAgent](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.remoteAgents), [Connectorlog](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.connectors.connectorInstances.logs), [Connectorrevision](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.connectors.revisions), [IntegrationInstance](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.integrationInstances), [UniqueEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.uniqueEntities), [Integrationsjob](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.jobs), [JobInstance](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.jobs.jobInstances), [JobInstances.log](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.jobs.jobInstances.logs), [Jobs.revision](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.jobs.revisions), [Integrationmanager](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.managers), [Integrationmanagerrevision](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations.managers.revisions), [AlertGroupingRule](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.alertGroupingRules), [Announcement](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.announcements), [Attachment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.legacySoarUsers.attachments), [CustomList](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.customLists), [FormDynamicParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.formDynamicParameters), [LabsExperiment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.labsExperiments), [MarketplaceIntegration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.marketplaceIntegrations), [ModuleSetting](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.moduleSettings), [SlaDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.slaDefinitions), [NotificationSetting](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.legacySoarUsers/getNotificationSettings), [PropertySchemaDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.propertySchemaDefinitions), [RequestTemplate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.requestTemplates), [SoarDomain](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.soarDomains), [SoarNetwork](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.soarNetworks), [WorkdeskLink](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.legacySoarUsers.workdeskLinks), [SystemNotification](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.systemNotifications), [WorkdeskContact](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.legacySoarUsers.workdeskContacts), [WorkdeskNote](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.legacySoarUsers.workdeskNotes), [LegacySoarUsers.localization](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.legacySoarUsers/getLocalization).   
  
## April 08, 2026

Announcement

**Emerging Threats Center general availability**

The **Emerging Threats Center** is now in General Availability (GA) and includes the following new features and enhancements:

  * **Expanded campaign filtering:** Filter the Emerging Threats feed by new categories, including associated malware, tools, and threat actors.
  * **MITRE ATT &CK matrix visualization:** Evaluate your detection rule coverage for specific tactics, techniques, and procedures (TTPs) using the new visualization matrix in the **Associated Rules** panel. You can customize heat map metrics, filter the matrix by rule or alerting status, and view detailed context for specific sub-techniques.
  * **Enhanced Entity context panel:** Investigate an indicator of compromise (IoC) using the **Entity context** panel to view its point-in-time state and related cases.
  * **GTI-associated IoC categories:** Filter GTI-associated IoCs by specific categories, including **Files** , **URLs** , **Domains** , and **IPs**.



For more information, see [Emerging Threats Center overview](https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats) and [Emerging Threats Center detail view](https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats-detailed-view). 

## April 07, 2026

Change

**[Spotlight Feature] Search query editor enhancements**

Google SecOps has enhanced the search query editor to provide intelligent auto-suggestions and improved error handling. The query editor now provides context-aware auto-suggestions for fields, operators, and valid values as you type. The editor also highlights syntax errors with a red squiggly line and displays a tooltip with the specific error description when you hover over it. Additionally, runtime errors now display persistently in the **Results panel** to assist with troubleshooting.

For more information, see [Use auto-suggestions to build queries](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#search_autosuggestions).

**Note:** This change follows a phased rollout from **April 07, 2026** , to **April 10, 2026**. Reach out to support if you do not see the new limits applied to your environment after **April 10, 2026**.

Feature

**[Spotlight Feature] Health Hub**

This feature is currently in Preview. 

The Health Hub is the central location in Google Security Operations for you to monitor the status and health of all configured data sources. The Health Hub provides crucial information on data sources and log types, offering the context needed to diagnose and remediate data pipeline issues.

The Health Hub includes information about the following:

  * Ingestion volumes and ingestion health.
  * Parsing volumes from raw logs to [Unified Data Model (UDM) events](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview).
  * Context and links to interfaces with additional relevant information and functionality.
  * Irregular and failed sources and log types. 



For more information, see [Use the Health Hub](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard).

## April 06, 2026

Change

**Updates to search query limits and error messaging**

Google SecOps has updated search query limits for programmatic and web interface access:

  * Increased Queries Per Hour (QPH) limits of up to 2,000 for APIs and 1,000 for the web interface.
  * New concurrency limits for both simple and complex queries.
  * More descriptive error messages for quota failures in the API and web interface.



For more information, see [Search limits and quotas](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#QPHlimits)

**Note:** This change follows a phased rollout from **April 06, 2026** , to **May 31, 2026**. Contact Support if you don't see the new limits applied to your environment after **May 31, 2026**. **May 31, 2026**. Contact Support if you don't see the new limits applied to your environment after **May 31, 2026**.

Deprecated

**v1 Cloud Storage Feed Types (GCS, S3, SQS, Azure)**

The v1 feed types for `GOOGLE_CLOUD_STORAGE`, `AMAZON_S3`, `AMAZON_SQS`, and `AZURE_BLOBSTORE` are deprecated and will be discontinued on **March 15, 2027**. The new v2 feed types use the Google Cloud Storage Transfer Service (STS) to provide improved performance, scalability, and reliability.

To ensure continued ingestion, transition your feeds before the March 15, 2027 shutdown date:

  * Google SecOps will automatically migrate your feeds using v1 feed types to v2 in waves starting from April 6, 2026. To facilitate this, some feeds may require additional IP allowlist or service account permission updates.



You can also self-migrate by creating new feeds using v2 feed types to substitute your existing feeds using v1 feed types by following the steps documented in our [feed configuration guides](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#source-types) before March 15, 2027.

**Key Dates:**

  * **April 6, 2026:** Transition begins; auto-migration available.
  * **October 1, 2026:** Support for v1 feeds is discontinued.
  * **March 15, 2027:** v1 feeds reach End of Life (EOL) and will stop returning data.



For more information, see [Feature deprecations](https://docs.cloud.google.com/chronicle/docs/deprecations).

## April 04, 2026

Feature

**Playbook Condition and Multi-Choice Question Flows**

The maximum number of branches supported in Playbook **Conditions** and **Multiple Choice Questions** has been increased from 6 to 20. This allows for more complex branching logic within a single step.

For more information, see [Use flows in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-flows-in-playbooks).

## April 03, 2026

Change

Google SecOps has updated the list of [supported default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers). Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

  * Abnormal Security (`ABNORMAL_SECURITY`)
  * Active Countermeasures (`AI_HUNTER`)
  * AIX system (`AIX_SYSTEM`)
  * Apache (`APACHE`)
  * Apache Cassandra (`CASSANDRA`)
  * Aruba (`ARUBA_WIRELESS`)
  * Aruba EdgeConnect SD-WAN (`ARUBA_EDGECONNECT_SDWAN`)
  * Auth0 (`AUTH_ZERO`)
  * AWS Aurora (`AWS_AURORA`)
  * AWS CloudFront (`AWS_CLOUDFRONT`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS CloudWatch (`AWS_CLOUDWATCH`)
  * AWS VPC Flow (`AWS_VPC_FLOW`)
  * AWS WAF (`AWS_WAF`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure Front Door (`AZURE_FRONT_DOOR`)
  * Azure SQL (`AZURE_SQL`)
  * BeyondTrust (`BOMGAR`)
  * BeyondTrust BeyondInsight (`BEYONDTRUST_BEYONDINSIGHT`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Broadcom Support Portal Audit Logs (`BROADCOM_SUPPORT_PORTAL`)
  * Check Point Harmony (`CHECKPOINT_HARMONY`)
  * Chronicle SOAR Audit (`CHRONICLE_SOAR_AUDIT`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Email Security (`CISCO_EMAIL_SECURITY`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Meraki (`CISCO_MERAKI`)
  * Cisco Secure Access (`CISCO_SECURE_ACCESS`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco Umbrella Audit (`CISCO_UMBRELLA_AUDIT`)
  * Cisco Umbrella DNS (`UMBRELLA_DNS`)
  * Cisco WSA (`CISCO_WSA`)
  * Cloud DNS (`GCP_DNS`)
  * Cloud SQL (`GCP_CLOUDSQL`)
  * Cloudflare (`CLOUDFLARE`)
  * Cloudflare Warp (`CLOUDFLARE_WARP`)
  * Code42 Incydr (`CODE42_INCYDR`)
  * CrowdStrike Alerts API (`CS_ALERTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CrowdStrike Falcon Stream (`CS_STREAM`)
  * CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
  * Cybereason EDR (`CYBEREASON_EDR`)
  * CYJAX Threat Intelligence (`CYJAX_THREAT_INTELLIGENCE`)
  * Cyware Threat Intelligence Exchange (`CTIX`)
  * Databricks (`DATABRICKS`)
  * Duo Auth (`DUO_AUTH`)
  * Elastic Defend (`ELASTIC_DEFEND`)
  * ESET AV (`ESET_AV`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP Access Policy Manager (`F5_BIGIP_APM`)
  * FireEye eMPS (`FIREEYE_EMPS`)
  * FireEye ETP (`FIREEYE_ETP`)
  * FireEye NX (`FIREEYE_NX`)
  * Forescout NAC (`FORESCOUT_NAC`)
  * ForgeRock Identity Cloud (`FORGEROCK_IDENTITY_CLOUD`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * GitHub (`GITHUB`)
  * Google Threat Intelligence IOC (`GTI_IOC`)
  * HP Aruba (ClearPass) (`CLEARPASS`)
  * Huawei Switches (`HUAWEI_SWITCH`)
  * IBM DataPower Gateway (`IBM_DATAPOWER`)
  * IBM Safenet (`IBM_SAFENET`)
  * IBM Websphere Application Server (`IBM_WEBSPHERE_APP_SERVER`)
  * Imperva Advanced Bot Protection (`IMPERVA_ABP`)
  * Imperva SecureSphere Management (`IMPERVA_SECURESPHERE`)
  * Juniper (`JUNIPER_FIREWALL`)
  * Kolide Endpoint Security (`KOLIDE`)
  * Kubernetes Audit (`KUBERNETES_AUDIT`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * Maria Database (`MARIA_DB`)
  * McAfee ePolicy Orchestrator (`MCAFEE_EPO`)
  * McAfee Skyhigh CASB (`MCAFEE_SKYHIGH_CASB`)
  * McAfee Web Gateway (`MCAFEE_WEBPROXY`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft Defender For Cloud (`MICROSOFT_DEFENDER_CLOUD_ALERTS`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft IIS (`IIS`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * Mimecast Mail V2 (`MIMECAST_MAIL_V2`)
  * Mobile Endpoint Security (`LOOKOUT_MOBILE_ENDPOINT_SECURITY`)
  * Mobileiron (`MOBILEIRON`)
  * NetApp ONTAP (`NETAPP_ONTAP`)
  * Netskope V2 (`NETSKOPE_ALERT_V2`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * Obsidian (`OBSIDIAN`)
  * Office 365 (`OFFICE_365`)
  * Oort Security Tool (`OORT`)
  * Oracle (`ORACLE_DB`)
  * Orca Cloud Security Platform (`ORCA`)
  * Palo Alto Cortex XDR Events (`PAN_CORTEX_XDR_EVENTS`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Prisma Cloud Alert payload (`PAN_PRISMA_CA`)
  * PostFix Mail (`POSTFIX_MAIL`)
  * Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Proofpoint Threat Response (`PROOFPOINT_TRAP`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * Red Hat OpenShift (`REDHAT_OPENSHIFT`)
  * Salesforce (`SALESFORCE`)
  * SAP Change Document (`SAP_CHANGE_DOCUMENT`)
  * SAP Gateway (`SAP_GATEWAY`)
  * SAP Hana Audit (`SAP_HANA_AUDIT`)
  * SAP Security Audit (`SAP_SECURITY_AUDIT`)
  * Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
  * Security Command Center Sensitive Data Risk (`GCP_SECURITYCENTER_SENSITIVE_DATA_RISK`)
  * Security Command Center Threat (`GCP_SECURITYCENTER_THREAT`)
  * Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
  * Snyk Group level audit Logs (`SNYK_SDLC`)
  * Suricata EVE (`SURICATA_EVE`)
  * Symantec EDR (`SYMANTEC_EDR`)
  * Sysdig (`SYSDIG`)
  * Tenable Active Directory Security (`TENABLE_ADS`)
  * ThreatConnect IOC V3 (`THREATCONNECT_IOC_V3`)
  * Trellix HX Alerts (`TRELLIX_HX_ALERTS`)
  * Trellix HX Audit Events (`TRELLIX_HX_AUDIT`)
  * Trellix HX Event Streamer (`TRELLIX_HX_ES`)
  * Trellix HX Hosts (`TRELLIX_HX_HOSTS`)
  * Trend Micro Vision One Endpoint Vulnerabilities (`TRENDMICRO_VISION_ONE_ENDPOINT_VULNERABILITIES`)
  * Trend Micro Vision One Observerd Attack Techniques (`TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES`)
  * Trend Micro Vision One Workbench (`TRENDMICRO_VISION_ONE_WORKBENCH`)
  * TrendMicro Apex Central (`TRENDMICRO_APEX_CENTRAL`)
  * TXOne Stellar (`TRENDMICRO_STELLAR`)
  * Ubika Waf (`UBIKA_WAF`)
  * Unix system (`NIX_SYSTEM`)
  * Varonis (`VARONIS`)
  * Vmware Avinetworks iWAF (`VMWARE_AVINETWORKS_IWAF`)
  * VMware ESXi (`VMWARE_ESX`)
  * VMware Horizon (`VMWARE_HORIZON`)
  * Wallix Bastion (`WALLIX_BASTION`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * wiz.io (`WIZ_IO`)
  * Zeek JSON (`BRO_JSON`)
  * Zscaler (`ZSCALER_WEBPROXY`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

  * Action1 (`ACTION1`)
  * CDNetworks Cloud Security (`CDNETWORKS_CLOUD_SECURITY`)
  * Claude Compliance Logs (`CLAUDE_COMPLIANCE_LOGS`)
  * Dell RecoverPoint (`DELL_RECOVERPOINT`)
  * IBM Storwize (`IBM_STORWIZE`)
  * LeapXpert Audit Logs (`LEAPXPERT_AUDIT`)
  * Oracle Key Vault Audit Logs (`ORACLE_KEY_VAULT_AUDIT_LOGS`)
  * RSA Cloud (`RSA_CLOUD`)
  * ServiceNow Antivirus Activity (`SERVICENOW_ANTIVIRUS_ACTIVITY`)
  * ServiceNow Attachment (`SERVICENOW_ATTACHMENT`)
  * ServiceNow Email (`SERVICENOW_EMAIL`)
  * Versa Director (`VERSA_DIRECTOR`)
  * ZPE Systems NodeGrid (`ZPE_SYSTEMS_NODEGRID`)



## April 02, 2026

Feature

**Chrome Enterprise Premium Integration general availability**

The Chrome Enterprise Premium integration is now GA. This release includes the following new features and updates:

  * New [Chrome Enterprise Connector](https://support.google.com/chrome/a/answer/16731355?visit_id=639074578268464336-809360017&p=cep_secops&rd=1) which configures recommended data export settings and sends data through Google Cloud to Google Security Operations. Chrome Enterprise Premium customers can export data with additional security context provided by Google Safe Browsing.

  * Updates to the `CHROME_MANAGEMENT` parser documentation in [Collect Chrome Enterprise data](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chrome-management) and [Chrome Enterprise Premium Threats](https://docs.cloud.google.com/chronicle/docs/detection/chrome-enterprise-threats-category).

  * Curated Detections for Chrome Enterprise Premium.

  * Curated Dashboards for Chrome Enterprise Premium.

  * Response actions to [block and remove](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-workspace#block_extension) malicious extensions or to [delete blocked extensions](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-workspace#delete_extension) from the extension policy [ExtensionInstallBlocklist](https://chromeenterprise.google/policies/?policy=ExtensionInstallBlocklist).




## March 31, 2026

Feature

**[Spotlight Feature] Multi-stage queries in YARA-L**

The Multi-stage queries feature is now GA. This feature lets you feed the output of one query stage into the input of another, providing more granular data transformation than a single, monolithic query. You can use multi-stage queries in both Dashboards and Search to build sophisticated detection and visualization logic. No action is required to enable this feature.

For more information, see [create multi-stage queries with YARA-L 2.0](https://docs.cloud.google.com/chronicle/docs/investigation/multi-stage-yaral).

## March 25, 2026

Feature

**[Spotlight Feature] Credential validation for third-party API feed types**

Credential validation is now available for all 49 third-party API connectors. When you create a feed using a third-party API feed type, Google SecOps now automatically validates the provided credentials. 

This ensures that if credentials are incorrect, the following happens:

  * **Immediate feedback** : The web interface displays an error message explaining the configuration failure.
  * **Prevention of broken feeds** : The system blocks the creation of the feed until valid credentials are provided, preventing the creation of broken feeds that fail to ingest data later.



## March 23, 2026

Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

  * [Collect Cisco Umbrella Cloud Firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-firewall)
  * [Collect Cisco Umbrella IP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-ip)
  * [Collect Claroty xDome for Healthcare logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/medigate-iot)
  * [Collect CloudM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudm)
  * [Collect Digital Guardian EDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalguardian-edr)
  * [Collect DNSFilter logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dnsfilter)
  * [Collect Dope Security SWG logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dope-swg)
  * [Collect Druva Backup logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/druva-backup)
  * [Collect EfficientIP DDI logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/efficientip-ddi)
  * [Collect Elastic Defend logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-defend)
  * [Collect Elastic Windows Event Log Beats logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-winlogbeat)
  * [Collect Ergon Informatik Airlock IAM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ergon-informatik-airlock-iam)
  * [Collect ESET Threat Intelligence logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-ioc)
  * [Collect F5 Distributed Cloud Services logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-dcs)
  * [Collect F5 Shape logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-shape)
  * [Collect F5 Silverline logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-silverline)
  * [Collect Falco IDS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/falco-ids)
  * [Collect Fastly CDN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fastly-cdn)
  * [Collect File Scanning Framework logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/file-scanning-framework)
  * [Collect FireEye ETP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-etp)
  * [Collect FireEye HX Audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx-audit)
  * [Collect FireEye NX Audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx-audit)
  * [Collect Fivetran logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fivetran)
  * [Collect Forcepoint Mail Relay logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-mail-relay)
  * [Collect GitGuardian Enterprise logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gitguardian-enterprise)
  * [Collect Google Cloud Looker audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/looker-audit)
  * [Collect Guardicore Centra logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardicore-centra)
  * [Collect HCL BigFix logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hcl-bigfix)
  * [Collect HID DigitalPersona logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hid-digitalpersona)
  * [Collect IBM AS/400 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-as400)
  * [Collect IBM Informix logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/informix)
  * [Collect IBM MaaS360 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-maas360)
  * [Collect IBM Mainframe Storage logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-mainframe-storage)
  * [Collect IBM OpenPages logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-openpages)
  * [Collect IBM Security Access Manager logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sam)
  * [Collect IBM Security Identity Manager logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sim)
  * [Collect iBoss Web Proxy logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iboss-webproxy)
  * [Collect Intel 471 Watcher Alerts logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intel471-watcher-alerts)
  * [Collect Intel Endpoint Management Assistant logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intel-ema)
  * [Collect IONIX Attack Surface Management logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ionix)
  * [Collect Island Enterprise Browser logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/island-browser)
  * [Collect Jamf Protect Telemetry V2 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-telemetry-v2)
  * [Collect Keycloak logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/keycloak)
  * [Collect Kong Gateway logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kong-gateway)
  * [Collect LenelS2 OnGuard logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lenel-onguard)
  * [Collect Lookout Mobile Endpoint Security logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lookout-mobile-endpoint-security)
  * [Collect Lucid audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lucid)
  * [Collect ManageEngine Exchange Reporter Plus logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-reporter-plus)
  * [Collect Mandiant Threat Intelligence Custom IOC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mandiant-custom-ioc)
  * [Collect Menlo Security Isolation Platform (MSIP) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/menlo-security)
  * [Collect Metabase logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/metabase)
  * [Collect Microsoft Defender for Endpoint on iOS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint-ios)
  * [Collect Microsoft Dynamics 365 User Activity logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-dynamics-365)
  * [Collect Microsoft IAS / Network Policy Server (NPS) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-ias)
  * [Collect Microsoft Network Policy Server (NPS) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-nps)
  * [Collect OAuth2 Proxy logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kubernetes-auth-proxy)
  * [Collect Office 365 Message Trace logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365-messagetrace)
  * [Collect Progress MOVEit Transfer logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ipswitch-moveit-transfer)
  * [Collect Netscout Arbor Sightline logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arbor-sightline)
  * [Collect Skyhigh Secure Web Gateway (On-Premises) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-web-protection)
  * [Collect ThreatDown EDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/malwarebytes-edr)
  * [Collect Trellix Endpoint Security (HX) alert logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-alerts)
  * [Collect Trellix Endpoint Security (HX) audit event logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-audit)
  * [Collect Trellix Endpoint Security (HX) host inventory logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-hosts)



## March 20, 2026

Feature

**[Spotlight Feature] View Triage and Investigation Agent (TIN) results in the Case Summary**

The TIN feature is currently in Preview and is part of a gradual rollout. You can now view TIN results and verdict summaries directly within the **Case Summary** view. This integration provides real-time progress updates and automated verdicts for true or false positives without leaving the case.

For more information, see [Use Triage and Investigation Agent (TIN) to investigate alerts](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent#manual_investigations).

Feature

**[Spotlight Feature] Agentic Automation**

The Agentic Automation feature is in Public Preview. You can now use **Agentic Automation** to embed AI Agents directly into your workflows. This feature lets you integrate AI-driven capabilities into your existing playbooks while staying in charge of critical actions by combining agents with deterministic automation steps.

For more information, see [Agentic Automation](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/agentic-automation).

## March 18, 2026

Feature

**[Spotlight Feature] Bindplane features for Google SecOps**

The following Bindplane features that relate to Google SecOps are now in General Availability (GA): Single sign-on with custom claims role mapping, SecOps parser validator and Forwarder migration tool.

Some of the main enhancements include:

  * **Single sign-on with custom claims role mapping** : gives a production-ready way to manage Bindplane access through your identity provider. For more information, see [Single Sign-On (Cloud)](https://docs.bindplane.com/feature-guides/saas-single-sign-on).

  * **SecOps parser validator** : validates that your logs will be parsed correctly by Google SecOps directly from the snapshot view. Get immediate feedback on parsed events or validation errors without waiting for data to appear in Google SecOps. For more information, see [Validate SecOps Parser](https://docs.bindplane.com/feature-guides/pipeline-intelligence#validate-secops-parser).

  * **Forwarder migration tool** : provides production-ready paths to migrate existing forwarder configurations into Bindplane-managed pipelines. For more information, see [Migrate Configurations](https://docs.bindplane.com/feature-guides/pipeline-intelligence#migrate-configurations).




For more information, see [Bindplane](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent)

## March 17, 2026

Announcement

Unified Feature Role-based Access Control (RBAC) is now in General Availability (GA). This enables administrators to manage feature access control for Google SecOps including SOAR by leveraging Google Cloud IAM instead of managing it separately for SIEM and SOAR.

You can enable it by [migrating](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#permissions-iam) the legacy SOAR permission groups and permissions to Google Cloud IAM through a self-service migration available from January 26, 2026. Please check the [documentation](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-permissions-iam) and [video](https://youtu.be/UBfwcgDvc0s) for full instructions.

This update is available to all customers who have completed [Stage 1](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#migration-stage-1-for-google-secops-unified-customers) of the SOAR migration to Google Cloud.

## March 16, 2026

Announcement

Stage 2 of the SOAR migration to Google Cloud deadline has been extended from June 30th to September 30th, 2026. 

## March 12, 2026

Announcement

**Manage parser versions**

The [Manage parser versions](https://docs.cloud.google.com/chronicle/docs/secops/release-notes#October_07_2025) feature is in Public Preview for all customers.

## March 10, 2026

Feature

**[Spotlight Feature] Set up and manage data processing pipelines**

The Data Processing feature is currently in Preview. You can now use the **Data Processing** pipelines to filter, transform, and redact Google SecOps data before ingestion. This feature provides more control over ingested data, letting you reduce costs by filtering out unwanted events, transform data for better compatibility, and protect sensitive information by redacting or masking values before storage. You can configure data processing pipelines using the Bindplane console or the Google SecOps Data Pipeline APIs.

For more information, see [Set up and manage data processing pipelines](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline).

## March 05, 2026

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region. For more information, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

  * Acalvio (`ACALVIO`)
  * AIX system (`AIX_SYSTEM`)
  * Akamai WAF (`AKAMAI_WAF`)
  * Apache (`APACHE`)
  * Apache Cassandra (`CASSANDRA`)
  * Apache Hadoop (`HADOOP`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * Aruba EdgeConnect SD-WAN (`ARUBA_EDGECONNECT_SDWAN`)
  * Attivo Networks (`ATTIVO`)
  * AWS Aurora (`AWS_AURORA`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS CloudWatch (`AWS_CLOUDWATCH`)
  * AWS GuardDuty (`GUARDDUTY`)
  * AWS Network Firewall (`AWS_NETWORK_FIREWALL`)
  * AWS Security Hub (`AWS_SECURITY_HUB`)
  * AWS WAF (`AWS_WAF`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure AD Sign-In (`AZURE_AD_SIGNIN`)
  * Azure Firewall (`AZURE_FIREWALL`)
  * Azure Front Door (`AZURE_FRONT_DOOR`)
  * Barracuda Email (`BARRACUDA_EMAIL`)
  * Barracuda Firewall (`BARRACUDA_FIREWALL`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Check Point Harmony (`CHECKPOINT_HARMONY`)
  * Cisco Application Centric Infrastructure (`CISCO_ACI`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Router (`CISCO_ROUTER`)
  * Cisco Secure Access (`CISCO_SECURE_ACCESS`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco TACACS+ (`CISCO_TACACS`)
  * Cisco UCM (`CISCO_UCM`)
  * Cisco Umbrella Audit (`CISCO_UMBRELLA_AUDIT`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Claroty Continuous Threat Detection (`CLAROTY_CTD`)
  * Claroty Enterprise Management Console (`CLAROTY_EMC`)
  * Claroty Xdome (`CLAROTY_XDOME`)
  * Cloud SQL (`GCP_CLOUDSQL`)
  * Cloudflare (`CLOUDFLARE`)
  * Cloudflare Audit (`CLOUDFLARE_AUDIT`)
  * Cloudflare WAF (`CLOUDFLARE_WAF`)
  * Cloudflare Warp (`CLOUDFLARE_WARP`)
  * Corelight (`CORELIGHT`)
  * CrowdStrike Alerts API (`CS_ALERTS`)
  * CrowdStrike Detection Monitoring (`CS_DETECTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CrowdStrike Falcon Stream (`CS_STREAM`)
  * CyberArk (`CYBERARK`)
  * CyberArk Endpoint Privilege Manager (EPM) (`CYBERARK_EPM`)
  * CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
  * Dell EMC Data Domain (`DELL_EMC_DATA_DOMAIN`)
  * Dell Switch (`DELL_SWITCH`)
  * Duo Auth (`DUO_AUTH`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * F5 Distributed Cloud Services (`F5_DCS`)
  * F5 DNS (`F5_DNS`)
  * FireEye NX (`FIREEYE_NX`)
  * Forcepoint NGFW (`FORCEPOINT_FIREWALL`)
  * Forcepoint Proxy (`FORCEPOINT_WEBPROXY`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Google Cloud (`GCP_SECURITYCENTER_THREAT`)
  * Google Cloud (`GCP_MONITORING_ALERTS`)
  * Google Threat Intelligence IOC (`GTI_IOC`)
  * GreyNoise (`GREYNOISE`)
  * Halcyon Anti Ransomware (`HALCYON`)
  * HP Aruba (ClearPass) (`CLEARPASS`)
  * Huawei Switches (`HUAWEI_SWITCH`)
  * Infoblox DNS (`INFOBLOX_DNS`)
  * Island Browser logs (`ISLAND_BROWSER`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * Linux Sysmon (`LINUX_SYSMON`)
  * ManageEngine ADAudit Plus (`ADAUDIT_PLUS`)
  * Maria Database (`MARIA_DB`)
  * McAfee IPS (`MCAFEE_IPS`)
  * McAfee Web Gateway (`MCAFEE_WEBPROXY`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft Defender For Cloud (`MICROSOFT_DEFENDER_CLOUD_ALERTS`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft IIS (`IIS`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * MISP Threat Intelligence (`MISP_IOC`)
  * Mobileiron (`MOBILEIRON`)
  * MySQL (`MYSQL`)
  * NetApp ONTAP (`NETAPP_ONTAP`)
  * Netskope V2 (`NETSKOPE_ALERT_V2`)
  * NGINX (`NGINX`)
  * Nozomi Networks Scada Guardian (`NOZOMI_GUARDIAN`)
  * Office 365 (`OFFICE_365`)
  * Open Cybersecurity Schema Framework (OCSF) (`OCSF`)
  * Orca Cloud Security Platform (`ORCA`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Palo Alto Prisma Cloud Alert payload (`PAN_PRISMA_CA`)
  * Ping One (`PING_ONE`)
  * PingIdentity Directory Server Logs (`PING_DIRECTORY`)
  * PostFix Mail (`POSTFIX_MAIL`)
  * PostgreSQL (`POSTGRESQL`)
  * Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Proofpoint Threat Response (`PROOFPOINT_TRAP`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * Red Hat OpenShift (`REDHAT_OPENSHIFT`)
  * Rubrik Security Cloud (`RUBRIK_SECURITY_CLOUD`)
  * SailPoint IdentityIQ (`SAILPOINT_IIQ`)
  * Salesforce (`SALESFORCE`)
  * SAP Change Document (`SAP_CHANGE_DOCUMENT`)
  * SAP Gateway (`SAP_GATEWAY`)
  * SAP HANA (`SAP_HANA`)
  * SAP Hana Audit (`SAP_HANA_AUDIT`)
  * SAP Identity and Authentication Data (`SAP_IDENTITY_AND_AUTH_DATA`)
  * SAP Internet Communication Manager (`SAP_ICM`)
  * SAP Security Audit (`SAP_SECURITY_AUDIT`)
  * SAP Webdispatcher (`SAP_WEBDISP`)
  * Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
  * Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
  * Sophos Central (`SOPHOS_CENTRAL`)
  * STIX Threat Intelligence (`STIX`)
  * Stormshield Firewall (`STORMSHIELD_FIREWALL`)
  * Suricata EVE (`SURICATA_EVE`)
  * Symantec Endpoint Protection (`SEP`)
  * Sysdig (`SYSDIG`)
  * Tableau (`TABLEAU`)
  * Teleport Access Plane (`TELEPORT_ACCESS_PLANE`)
  * Trend Micro (`TIPPING_POINT`)
  * Tripwire (`TRIPWIRE_FIM`)
  * TXOne Stellar (`TRENDMICRO_STELLAR`)
  * Ubika Waf (`UBIKA_WAF`)
  * Unix system (`NIX_SYSTEM`)
  * Velo Firewall (`VELO_FIREWALL`)
  * Veritas NetBackup (`VERITAS_NETBACKUP`)
  * Versa Firewall (`VERSA_FIREWALL`)
  * Vmware Avinetworks iWAF (`VMWARE_AVINETWORKS_IWAF`)
  * VMware ESXi (`VMWARE_ESX`)
  * VMware vCenter (`VMWARE_VCENTER`)
  * WatchGuard (`WATCHGUARD`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * wiz.io (`WIZ_IO`)
  * Workday Audit Logs (`WORKDAY_AUDIT`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * ZScaler VPN (`ZSCALER_VPN`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

  * Alibaba Security Center (`ALIBABA_SECURITY_CENTER`)
  * Apache Airflow (`APACHE_AIRFLOW`)
  * Baramundi (`BARAMUNDI`)
  * Bravura Security (`BRAVURA`)
  * Buildkite Audit (`BUILDKITE_AUDIT`)
  * Palo Alto Cortex Xpanse (`CORTEX_XPANSE`)
  * Cyfirma DeCYFIR ServiceNow (`CYFIRMA_DECYFIR`)
  * DATEV (`DATEV`)
  * ELO (`ELO`)
  * Forcepoint Secure Web Gateway (`FORCEPOINT_SWG`)
  * JumpServer PAM (`JUMPSERVER_PAM`)
  * Keep Aware (`KEEP_AWARE`)
  * Lark Suite (`LARK_SUITE`)
  * Macmon (`MACMON`)
  * Mamori Database Activity Monitoring (`MAMORI_DAM`)
  * N8N Security Audit Logs (`N8N_SECURITY_AUDIT_LOGS`)
  * Oracle Cloud Infrastructure LoadBalancer (`OCI_LOADBALANCER`)
  * OpenText Self Service Password Reset (`OPENTEXT_SSPR`)
  * Rackspace (`RACKSPACE`)
  * Secui Bluemax NGF (`SECUI_BLUEMAX_NGF`)
  * Symantec Advanced Threat Protection (`SYMANTEC_ATP`)
  * Tenable Vulnerabilities Management (`TENABLE_VMGNT`)
  * Trellix EDRF Trace Data and Telemetry (`TRELLIX_EDRF`)
  * Trend Micro Vision One Endpoint Vulnerabilities (`TRENDMICRO_VISION_ONE_ENDPOINT_VULNERABILITIES`)
  * Zafran (`ZAFRAN`)



Announcement

**Google Agentic SOC Trial**

There will be a no-cost trial for the Google SecOps Triage Investigative Agent (TIN) from April 1, 2026 to June 30, 2026. TIN is an agentic AI feature for Google SecOps that helps automate security investigations. For more information about the trial, see [Google Agentic SOC Trial details](https://docs.cloud.google.com/chronicle/docs/agentic-soc/trial). For more information about TIN, see [Use Triage and Investigation Agent to investigate alerts](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent).

## March 02, 2026

Deprecated

`Chronicle.soarAnalyst`, `chronicle.soarViewer`, `chronicle.soarEngineer` roles in Cloud IAM are being deprecated and will be fully removed in six months. Although these roles were accessible and can historically be assigned to users in Cloud IAM, they were non-operational. SOAR roles were managed through Permission Groups and with its migration to Cloud IAM as part of the [SOAR Migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#permissions-iam), the preceding roles are being deprecated.

To maintain seamless access and adhere to the principle of least privilege, transition your SOAR users to the following options: 

  * Automatically convert your SOAR Permission Groups to custom roles in IAM through [self-service migration](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#permissions-iam).
  * Pre-defined roles: Utilize the enhanced Google SecOps [pre-defined roles](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#google-security-operations-roles) now available in Cloud IAM.
  * Custom Roles: Create tailored roles with [specific permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#google-security-operations-permissions) to meet your organization's unique security requirements.



Feature

**[Spotlight Feature] New Unified rules interface**

This feature is currently in Preview. Google SecOps has launched a unified rules interface that brings custom and curated rule management into a single, cohesive workflow. This update optimizes detection engineering with a redesigned dashboard, an advanced rule editor, and expanded API capabilities to streamline rule deployment and troubleshooting.

Some of the main enhancements include:

  * **Centralized management:** A unified, single dashboard lets you browse, filter, and manage both custom and curated rules from one location. You can also update configurations for multiple rules simultaneously.

  * **Curated rule transparency:** You can now view the YARA-L text of curated rules, search directly within their logic, and independently toggle individual rule statuses without needing to alter the parent rule pack deployment.

  * **Integrated IDE experience:** The rule editor now features an enhanced IDE experience with inline error highlights, UDM field definitions on hover.




**Expanded API and structured search** :

The Rules API and dashboard have been upgraded to support deeper programmatic access and complex filtering:

  * **Robust search syntax:** Both the UI and API now support AIP-160 compliant structured search. You can filter rules by text, tags, author, and execution state.

  * **Batch modifications:** The `rules.modifyRules` method now supports non-atomic batch updates, letting you change live status, alerting status, tags, and archive status across multiple rules in a single API request.

  * **Advanced resource views:** The `rules.list` method introduces `CONFIG_ONLY` and `TRENDS` views. These views provide expanded deployment information, access to curated rule resources, and larger page sizes (up to 5000 results) for efficient querying.




For more information, see [Manage unified rules](https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/get-started).

## February 25, 2026

Feature

**Added support for Google Cloud VPC Service Controls**

This feature is currently in Preview.

[VPC Service Controls](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops) helps protect against accidental or targeted action by external entities or insider entities, which helps to minimize unwarranted data exfiltration risks from Google Cloud services. You can use VPC Service Controls to create perimeters that protect the resources and data of services that you explicitly specify. For more information, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## February 24, 2026

Feature

**New: cross joins in multi-stage queries**

You can now use cross joins in YARA-L 2.0 multi-stage queries let you compare individual UDM event data against aggregated statistics calculated in previous YARA-L stages. They are supported in:

  * Search
  * Dashboards



For more information, see [Cross joins in multi-stage queries](https://docs.cloud.google.com/chronicle/docs/investigation/multi-stage-yaral#cross-joins).

Feature

**RBAC for ingestion metrics**

Administrators can now use RBAC for ingestion metrics to restrict visibility of system health data, such as ingestion volume, errors, and throughput, based on a user's business scope.

The **Data Ingestion and Health** dashboard now uses Data Access scopes. When a scoped user loads the dashboard, the system automatically filters metrics to show only data that matches their assigned labels: Namespace, Log Type, and Ingestion Source.

For more information, see [Ingestion metrics](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards#ingestion_metrics).

## February 23, 2026

Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

  * [Collect Big Switch BigCloudFabric logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bigswitch-bcf)
  * [Collect BMC AMI Defender logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bmc-ami-defender)
  * [Collect Broadcom Support Portal Audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-support-portal)
  * [Collect CA ACF2 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-acf2)
  * [Collect CA LDAP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-ldap)
  * [Collect ChromeOS XDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chromeos-xdr)
  * [Collect Chronicle SOAR Audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chronicle-soar-audit)
  * [Collect Cisco CTS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-cts)
  * [Collect Cisco FireSIGHT Management Center logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-firesight)
  * [Collect Cisco Vision Dynamic Signage Director logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-stadiumvision)
  * [Collect ClamAV logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/clam-av)
  * [Collect Cofense logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cofense-triage)
  * [Collect Crowdstrike IOC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crowdstrike-ioc)
  * [Collect Custom Application Access logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-application-access)
  * [Collect Custom Security Data Analytics logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-security-data-analytics)
  * [Collect Cyber 2.0 IDS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyber-2-ids)
  * [Collect CyberArk logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark)
  * [Collect Cybereason EDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cybereason-edr)
  * [Collect Dataminr Alerts logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dataminr-alert)
  * [Collect Digital Shadows Indicators logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digital-shadows-ioc)
  * [Collect Mimecast Mail V2 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mimecast-mail-v2)
  * [Collect Okta User Context logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta-user-context)
  * [Collect RH-ISAC IOC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rh-isac-ioc)
  * [Collect ServiceNow CMDB data](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-cmdb)



## February 22, 2026

Change

**Publisher Agent Version 2.6.4** removes support for **Python 3.7** from the remote agent.

## February 20, 2026

Feature

**New capabilities in Feeds page**

The following options have been added to the **Feeds** page:

  * Search 
  * Filtering (using feed attributes)
  * Pagination
  * Last Refreshed Time
  * Feed Metadata Export to CSV



## February 17, 2026

Deprecated

Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see [Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

Change

After March 17, 2026, when you enable Google SecOps, the Google SecOps MCP server is automatically enabled.

## February 12, 2026

Feature

**Advanced Joins in Search**

Google SecOps now supports expanded capabilities for correlating data across multiple sources. These join operations are also supported in multistage queries.

**Joins without a`match` section**: You can now use join operations to correlate and combine data from multiple sources based on common field values without requiring a `match` section (unlike statistical joins). Results are displayed in a Joins table, which you can download as a CSV, or for event-to-event joins, exported to a datatable for further analysis.

For more information, see [Implement joins without a match section](https://docs.cloud.google.com/chronicle/docs/investigation/joins-without-match-section).

**Outer joins** : Search now supports left and right outer joins. Unlike standard inner joins, these operations let you retrieve all records from a primary data source even if no matching entry exists in the secondary source (unmatched fields are returned as `null`). This action lets you correlate data without losing unmatched events.

For more information, see [Correlate data with outer joins](https://docs.cloud.google.com/chronicle/docs/investigation/outer-joins).

## February 09, 2026

Announcement

**Enhanced rule observability: New metadata, visual indicators, and dashboards**

Google Security Operations has introduced updates to how detection and alert data is processed and visualized. These changes help Google SecOps teams distinguish between primary rule runs and _rule replays_ , which provides clarity on detection delays and the impact of late-arriving enrichment data.

  * **Key improvements**

    * **Enhanced metadata** : Detection and alert objects now include specific metadata that identifies whether they were produced during a primary rule run, or as part of a _rule replay_ or retrohunt.
    * **Improved troubleshooting** : This data lets Google SecOps teams definitively answer critical operational questions, such as the cause of perceived detection delays or the specific impact of late-arriving enrichment data on active rules.
    * **Rule replay insights** : Learn more about the distinction between primary runs and replays to manage the re-enrichment of Unified Data Model (UDM) events. For detailed definitions and technical workflows, see [Understand rule replay](https://docs.cloud.google.com/chronicle/docs/detection/rule-replays) and [Understand rule detection delays](https://docs.cloud.google.com/chronicle/docs/detection/detection-delays#re-enrichment-of-udm-events).
    * **New detection dashboard** : To support these backend metadata changes, a new **Detection Health** dashboard is now available. This interface provides a visual representation of rule performance and replay status, letting teams monitor detection health more effectively.
    * **Custom reporting** : There are new fields available in the [Detections schema](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#detections), letting you build custom dashboards.
  * **New metadata and third-party integration** : Detections and alerts now emit specific metadata to help customers track timing and latency. This data is available for integration with third-party systems using the following fields:

    * `detectionTimingDetails`: An enum identifying the run type:
    * `DETECTION_TIMING_DETAILS_REPROCESSING`
    * `DETECTION_TIMING_DETAILS_RETROHUNT`
    * `DETECTION_TIMING_DETAILS_UNSPECIFIED`
    * `latencyMetrics`: Includes timestamps for `oldestIngestionTime`, `newestIngestionTime`, `oldestEventTime`, and `newestEventTime`.
  * **Enhanced platform and visual indicators** :

    * **Alerts and rule details** : A new visual indicator in the **Detection Type** column provides granular details on hover.
    * **Filter facets** : The **Alerts** lister page now includes _detection timing details_ as a filterable facet.
    * **SOAR integration** : In the **Case Overview** , the **Composite Detections** table now carries through the same iconography for a consistent investigation experience.



## February 04, 2026

Feature

**The re.capture_all function is now available**

The new [re.capture_all](https://docs.cloud.google.com/chronicle/docs/yara-l/functions#recapture_all) YARA-L 2.0 function is available in Rules, Search, and Dashboards.

Use the **re.capture_all()** function to extract every non-overlapping match of a regular expression from a string. While the standard [**re.capture**](https://docs.cloud.google.com/chronicle/docs/yara-l/functions#recapture) function stops after the first match it finds, the **re.capture_all()** function continues through the entire string to identify every instance that matches your pattern.

Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

  * [Collect ForgeRock OpenIDM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forgerock-openidm)
  * [Collect Forseti Open Source logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forseti)
  * [Collect Fortinet FortiClient logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-forticlient)
  * [Collect Fortinet FortiDDoS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiddos)
  * [Collect Fortinet FortiEDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiedr)
  * [Collect Fortinet FortiManager logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortimanager)
  * [Collect Fortinet Switch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-switch)
  * [Collect Fortra Powertech SIEM Agent logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortra-powertech-siem-agent)
  * [Collect Google App Engine logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-app-engine)
  * [Collect Google Cloud DNS Threat Detector log](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-dns-atd)s
  * [Collect Google Cloud Monitoring alerting activity logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-monitoring-alerts)
  * [Collect Google Cloud Network Connectivity Center logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-ids)
  * [Collect Google Cloud Secure Web Proxy logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-secure-wp)
  * [Collect Gmail logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gmail-logs)
  * [Collect H3C Comware Platform Switch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/h3c-switch)
  * [Collect HackerOne logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hackerone)
  * [Collect Hillstone Firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hillstone-ngfw)
  * [Collect Hitachi Content Platform logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hitachi-content-platform)
  * [Collect HYPR MFA logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hypr-mfa)
  * [Collect IBM Guardium logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-guardium)



## February 03, 2026

Feature

**Share custom column sets**

Google SecOps now lets you share custom sets of columns in the **Events** table for consistent analysis across teams.

For more details, see [Search for events and alerts](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)

Announcement

**Data RBAC global scope changes for ATI**

To enhance data security, several features related to Indicators of Compromise (IOCs) and Emerging Threats now require global scope data RBAC permissions. Users without global scope will see restricted information in the following areas:

  * **Emerging threats** page: IOC match counts per campaign are no longer visible.

  * **Entity widget overlay** : The **Indicators** table is hidden or appears empty.

  * **Threat details** page: The related entities, IOC matches, and GTI IOC tables are no longer visible.

  * **Entity summary** widget: GTI scores are excluded from the overlay.

  * **IOC details** page: The **Indicator Details** tab doesn't populate.




**API impact** : API calls to `IocService` and `ThreatCollectionService` now require global scope. Direct calls made with the CLI or client libraries fail without this permission.

**Required** : Google SecOps administrators should review user roles and grant global scope to those who require continued access to these threat intelligence features.

**Note:** This change follows a phased rollout throughout the week of February 02, 2026 to February 08, 2026.

Deprecated

**Mute an IoC deprecated**

The Mute an IoC feature is deprecated, and the **IOC details** page no longer displays the **Mute** indicator.

## February 02, 2026

Change

Google SecOps has updated the list of supported default parsers. Updates propagate gradually; changes typically appear in your region within one to four business days. For more information, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

  * A10 Load Balancer (`A10_LOAD_BALANCER`)
  * AIX system (`AIX_SYSTEM`)
  * Akamai Cloud Monitor (`AKAMAI_CLOUD_MONITOR`)
  * AlgoSec Security Management (`ALGOSEC`)
  * Amazon API Gateway (`AWS_API_GATEWAY`)
  * Apache (`APACHE`)
  * Apple macOS (`MACOS`)
  * AppOmni (`APPOMNI`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * Arista Switch (`ARISTA_SWITCH`)
  * Aruba (`ARUBA_WIRELESS`)
  * Aruba Airwave (`ARUBA_AIRWAVE`)
  * Aruba EdgeConnect SD-WAN (`ARUBA_EDGECONNECT_SDWAN`)
  * Aruba Switch (`ARUBA_SWITCH`)
  * Attivo Networks (`ATTIVO`)
  * Auth0 (`AUTH_ZERO`)
  * Automation Anywhere (`AUTOMATION_ANYWHERE`)
  * Avanan Email Security (`AVANAN_EMAIL`)
  * AWS Aurora (`AWS_AURORA`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS CloudWatch (`AWS_CLOUDWATCH`)
  * AWS Elastic Load Balancer (`AWS_ELB`)
  * AWS GuardDuty (`GUARDDUTY`)
  * AWS RDS (`AWS_RDS`)
  * AWS Security Hub (`AWS_SECURITY_HUB`)
  * AWS WAF (`AWS_WAF`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure AD Sign-In (`AZURE_AD_SIGNIN`)
  * Azure Front Door (`AZURE_FRONT_DOOR`)
  * Barracuda Email (`BARRACUDA_EMAIL`)
  * Barracuda WAF (`BARRACUDA_WAF`)
  * BeyondTrust (`BOMGAR`)
  * BeyondTrust BeyondInsight (`BEYONDTRUST_BEYONDINSIGHT`)
  * BeyondTrust Endpoint Privilege Management (`BEYONDTRUST_ENDPOINT`)
  * BeyondTrust Secure Remote Access (`BEYONDTRUST_REMOTE_ACCESS`)
  * BIND (`BIND_DNS`)
  * Bindplane Agent (`BINDPLANE_AGENT`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Box (`BOX`)
  * Carbon Black (`CB_EDR`)
  * Cato Networks (`CATO_NETWORKS`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * CipherTrust Manager (`CIPHERTRUST_MANAGER`)
  * Cisco Application Centric Infrastructure (`CISCO_ACI`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Email Security (`CISCO_EMAIL_SECURITY`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Meraki (`CISCO_MERAKI`)
  * Cisco PIX Firewall (`CISCO_PIX_FIREWALL`)
  * Cisco Router (`CISCO_ROUTER`)
  * Cisco Stealthwatch (`CISCO_STEALTHWATCH`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco Umbrella Audit (`CISCO_UMBRELLA_AUDIT`)
  * Cisco Umbrella DNS (`UMBRELLA_DNS`)
  * Cisco vManage SD-WAN (`CISCO_SDWAN`)
  * Cisco WLC/WCS (`CISCO_WIRELESS`)
  * Cisco WSA (`CISCO_WSA`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Claroty Continuous Threat Detection (`CLAROTY_CTD`)
  * Claroty Xdome (`CLAROTY_XDOME`)
  * Cloud SQL (`GCP_CLOUDSQL`)
  * Cloudflare (`CLOUDFLARE`)
  * Cloudflare Audit (`CLOUDFLARE_AUDIT`)
  * Compute Engine (`GCP_COMPUTE`)
  * Corelight (`CORELIGHT`)
  * CrowdStrike Alerts API (`CS_ALERTS`)
  * CrowdStrike Detection Monitoring (`CS_DETECTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CrowdStrike Falcon Stream (`CS_STREAM`)
  * CyberArk (`CYBERARK`)
  * CyberArk Endpoint Privilege Manager (EPM) (`CYBERARK_EPM`)
  * CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
  * Cyolo Secure Remote Access for OT (`CYOLO_OT`)
  * Darktrace (`DARKTRACE`)
  * Delinea Secret Server (`DELINEA_SECRET_SERVER`)
  * Dell ECS Enterprise Object Storage (`DELL_ECS`)
  * Dell Switch (`DELL_SWITCH`)
  * Duo Auth (`DUO_AUTH`)
  * ExtraHop RevealX (`EXTRAHOP`)
  * Extreme Wireless (`EXTREME_WIRELESS`)
  * F5 Advanced Firewall Management (`F5_AFM`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP Access Policy Manager (`F5_BIGIP_APM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * F5 Distributed Cloud Services (`F5_DCS`)
  * Fastly CDN (`FASTLY_CDN`)
  * FireEye ETP (`FIREEYE_ETP`)
  * FireEye NX (`FIREEYE_NX`)
  * Forcepoint Email Security (`FORCEPOINT_EMAILSECURITY`)
  * Forescout eyeInspect (`FORESCOUT_EYEINSPECT`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortinet Fortimanager (`FORTINET_FORTIMANAGER`)
  * Fortinet Web Application Firewall (`FORTINET_FORTIWEB`)
  * GCP_APP_ENGINE (`GCP_APP_ENGINE`)
  * GCP_MODEL_ARMOR (`GCP_MODEL_ARMOR`)
  * GitHub (`GITHUB`)
  * GitHub Dependabot (`GITHUB_DEPENDABOT`)
  * Google Cloud Audit (`GCP_CLOUDAUDIT`)
  * Google Threat Intelligence (`GCP_THREATINTEL`)
  * H3C Comware Platform Switch (`H3C_SWITCH`)
  * Hashicorp Vault (`HASHICORP`)
  * HP Aruba (ClearPass) (`CLEARPASS`)
  * Huawei Switches (`HUAWEI_SWITCH`)
  * IBM DataPower Gateway (`IBM_DATAPOWER`)
  * IBM DB2 (`DB2_DB`)
  * Illumio Core (`ILLUMIO_CORE`)
  * Imperva (`IMPERVA_WAF`)
  * Imperva DRA (`IMPERVA_DRA`)
  * Island Browser logs (`ISLAND_BROWSER`)
  * Jamf pro context (`JAMF_PRO_CONTEXT`)
  * JumpCloud Directory Insights (`JUMPCLOUD_DIRECTORY_INSIGHTS`)
  * Juniper MX Router (`JUNIPER_MX`)
  * Keycloak (`KEYCLOAK`)
  * KnowBe4 PhishER (`KNOWBE4_PHISHER`)
  * Kolide Endpoint Security (`KOLIDE`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * McAfee DLP (`MCAFEE_DLP`)
  * McAfee ePolicy Orchestrator (`MCAFEE_EPO`)
  * McAfee Web Gateway (`MCAFEE_WEBPROXY`)
  * Microsoft AD FS (`ADFS`)
  * Microsoft Defender For Cloud (`MICROSOFT_DEFENDER_CLOUD_ALERTS`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft IIS (`IIS`)
  * Microsoft Intune (`AZURE_MDM_INTUNE`)
  * Microsoft PowerShell (`POWERSHELL`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * Mimecast Mail V2 (`MIMECAST_MAIL_V2`)
  * MISP Threat Intelligence (`MISP_IOC`)
  * Mobileiron (`MOBILEIRON`)
  * MySQL (`MYSQL`)
  * NetApp ONTAP (`NETAPP_ONTAP`)
  * Netfilter IPtables (`NETFILTER_IPTABLES`)
  * NetIQ Access Manager (`NETIQ_ACCESS_MANAGER`)
  * Netskope V2 (`NETSKOPE_ALERT_V2`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * Network Policy Server (`MICROSOFT_NPS`)
  * NGINX (`NGINX`)
  * Nozomi Networks Scada Guardian (`NOZOMI_GUARDIAN`)
  * Nutanix Prism (`NUTANIX_PRISM`)
  * Obsidian (`OBSIDIAN`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * Onapsis (`ONAPSIS`)
  * One Identity TPAM (`ONEIDENTITY_TPAM`)
  * OneLogin (`ONELOGIN_SSO`)
  * Open Cybersecurity Schema Framework (OCSF) (`OCSF`)
  * Oracle (`ORACLE_DB`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Ping Identity (`PING`)
  * PostFix Mail (`POSTFIX_MAIL`)
  * PostgreSQL (`POSTGRESQL`)
  * Proofpoint CASB (`PROOFPOINT_CASB`)
  * Proofpoint Email Filter (`PROOFPOINT_MAIL_FILTER`)
  * Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Pulse Secure (`PULSE_SECURE_VPN`)
  * QNAP Systems NAS (`QNAP_NAS`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * Recorded Future (`RECORDED_FUTURE_IOC`)
  * Red Hat OpenShift (`REDHAT_OPENSHIFT`)
  * Salesforce (`SALESFORCE`)
  * SAP Sybase Adaptive Server Enterprise Database (`SAP_ASE`)
  * Security Command Center Chokepoint (`GCP_SECURITYCENTER_CHOKEPOINT`)
  * Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
  * Security Command Center Threat (`GCP_SECURITYCENTER_THREAT`)
  * Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
  * ServiceNow Audit (`SERVICENOW_AUDIT`)
  * Snare System Diagnostic Logs (`SNARE_SOLUTIONS`)
  * Snyk Group level audit/issues logs (`SNYK_ISSUES`)
  * Solaris system (`SOLARIS_SYSTEM`)
  * Sophos Central (`SOPHOS_CENTRAL`)
  * STIX Threat Intelligence (`STIX`)
  * Stormshield Firewall (`STORMSHIELD_FIREWALL`)
  * Sublime Security (`SUBLIMESECURITY`)
  * Suricata EVE (`SURICATA_EVE`)
  * Swift Alliance Messaging Hub (`SWIFT_AMH`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Symantec Endpoint Protection (`SEP`)
  * Symantec Messaging Gateway (`SYMANTEC_MAIL`)
  * Tableau (`TABLEAU`)
  * TCPWave DDI (`TCPWAVE_DDI`)
  * TeamViewer (`TEAMVIEWER`)
  * Tenable Active Directory Security (`TENABLE_ADS`)
  * Tenable OT (`TENABLE_OT`)
  * Tenable.io (`TENABLE_IO`)
  * Thinkst Canary (`THINKST_CANARY`)
  * ThreatConnect IOC V3 (`THREATCONNECT_IOC_V3`)
  * Trellix HX Event Streamer (`TRELLIX_HX_ES`)
  * Trend Micro (`TIPPING_POINT`)
  * Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
  * Trend Micro Vision One Workbench (`TRENDMICRO_VISION_ONE_WORKBENCH`)
  * TrendMicro Deep Discovery Inspector (`TRENDMICRO_DDI`)
  * TXOne Stellar (`TRENDMICRO_STELLAR`)
  * Unifi AP (`UNIFI_AP`)
  * Unix system (`NIX_SYSTEM`)
  * Vectra Detect (`VECTRA_DETECT`)
  * Vectra XDR (`VECTRA_XDR`)
  * Veritas NetBackup (`VERITAS_NETBACKUP`)
  * Versa Firewall (`VERSA_FIREWALL`)
  * VMware ESXi (`VMWARE_ESX`)
  * VMware NSX (`VMWARE_NSX`)
  * VMware vCenter (`VMWARE_VCENTER`)
  * WatchGuard (`WATCHGUARD`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Wiz.io (`WIZ_IO`)
  * Workday Audit Logs (`WORKDAY_AUDIT`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * Workspace Alerts (`WORKSPACE_ALERTS`)
  * Zimperium (`ZIMPERIUM`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * Zscaler CASB (`ZSCALER_CASB`)
  * Zscaler DLP (`ZSCALER_DLP`)
  * ZScaler DNS (`ZSCALER_DNS`)
  * Zscaler Internet Access Audit Logs (`ZSCALER_INTERNET_ACCESS`)
  * ZScaler NGFW (`ZSCALER_FIREWALL`)
  * Zscaler Private Access (`ZSCALER_ZPA`)
  * Zscaler Secure Private Access Audit Logs (`ZSCALER_ZPA_AUDIT`)
  * Zscaler Tunnel (`ZSCALER_TUNNEL`)
  * Zywall (`ZYWALL`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

  * Aikido (`AIKIDO`)
  * Akamai API Security (`AKAMAI_API_SECURITY`)
  * Alkira IP Flow (`ALKIRA_IP_FLOW`)
  * Atlassian Guard Detect (`ATLASSIAN_GUARD_DETECT`)
  * BlinkOps (`BLINKOPS`)
  * Canvas LMS (`CANVAS_LMS`)
  * Cisco Secure Email Threat Defense (`CISCO_SECURE_EMAIL_THREAT_DEFENSE`)
  * Cisco StarOS (`CISCO_STAR_OS`)
  * Citadel Identity360 (`CITADEL_IDENTITY360`)
  * Cyware Threat Intelligence Exchange (`CTIX`)
  * Cyberark Identity Audit (`CYBERARK_IDENTITY_AUDIT`)
  * CyCognito ASM (`CYCOGNITO_ASM`)
  * Dell VxRail (`DELL_VXRAIL`)
  * Gene6 FTP Server (`GENE6_FTP`)
  * IBM Copy Services Manager (`IBM_CSM`)
  * LangSmith Audit (`LANGSMITH_AUDIT`)
  * Mellanox Switch (`MELLANOX_SWITCH`)
  * Microsoft Entra ID Protection (`MICROSOFT_ENTRA_ID_PROTECTION`)
  * NSFOCUS Next Generation Intrusion Prevention System (`NSFOCUS_NGIPS`)
  * Perplexity (`PERPLEXITY`)
  * Pleasant Password Server (`PLEASANT_PASSWORD_SERVER`)
  * Prompt Security (`PROMPT_SECURITY`)
  * Qualtrics Audit (`QUALTRICS_AUDIT`)
  * Rancher API Audit Log (`RANCHER_API_AUDIT_LOG`)
  * Rubrik Security Cloud (`RUBRIK_SECURITY_CLOUD`)
  * SAP Business Warehouse (`SAP_BW`)
  * SAP Change Document (`SAP_CHANGE_DOCUMENT`)
  * SAP Gateway (`SAP_GATEWAY`)
  * SAP Hana Audit (`SAP_HANA_AUDIT`)
  * Scale Computing (`SCALE_COMPUTING`)
  * Slack API (`SLACK_API`)
  * Snowplow (`SNOWPLOW`)
  * Sterling Order Management System Data (`STERLING_OMS_DATA`)
  * Strivacity (`STRIVACITY`)
  * Tencent CloudAudit (`TENCENT_CLOUD_AUDIT`)
  * Trellix EX (`TRELLIX_EX`)
  * Unifi System (`UNIFI_SYSTEM`)
  * Windows Bindplane (`WINDOWS_BINDPLANE`)
  * Witness AI Control (`WITNESS_AI_CONTROL`)
  * Zendesk Advanced Data Privacy and Protection (`ZENDESK_ADPP`)



## February 01, 2026

Change

The **Case Federation** feature is no longer dependent on the **Case Federation** integration in the primary platform.

The primary platform sync job is now disabled. Do not attempt to re-enable it.

For more information, see [Set up federated case access for SecOps](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/case-federation-secops).

## January 30, 2026

Announcement

The following v2 connectors, which utilize Google Storage Transfer Service (STS), are now in General Availability:

  * Google Cloud Storage v2
  * Amazon S3 v2
  * Google Cloud Storage (Event Driven)
  * Amazon SQS v2
  * Azure Blobstore v2



## January 29, 2026

Feature

**Rule observability for detections and alerts**

New metadata is now included in all detection and alert objects, indicating if the detection was produced during a primary rule run or through a [rule replay](https://docs.cloud.google.com/chronicle/docs/detection/rule-replays). This information can be used in dashboards and as a filter in the **Alerts** lister page using the field `collection.detection_timing_details`.

## January 25, 2026

Feature

**Structured SOAR Python integration logs**

Python integration logging has been upgraded to a structured format to eliminate visibility gaps and ensure comprehensive diagnostic coverage in Google Cloud. This upgrade changes how Python logs are interpreted in the Google Cloud Logging Explorer. Previously, logs were bundled into a single block per execution. Now, every log line is interpreted as a separate entry, allowing for granular filtering, better searchability, and easier debugging of specific events.

**Recommended Actions:**

  * **Update Log-Based Alerts:** Ensure alerts triggered by string matches are compatible with individual log entries rather than bundled blocks.
  * **Review Automation Scripts:** Test any external scripts or BigQuery exports that parse textPayload against the new granular format.
  * **Verify Dashboards:** Custom monitoring dashboards may show an increase in event counts as executions are no longer bundled.



For more information, see [Collect Google SecOps SOAR logs](https://docs.cloud.google.com/chronicle/docs/secops/collect-secops-soar-logs).

Feature

**Timeline View for Alerts**

Visualize alert patterns over time using the new timeline view in the Alerts section of the Cases Overview tab.

Announcement

**Integration Rollback**

This [Integration Rollback](https://docs.cloud.google.com/chronicle/docs/secops/release-notes#January_18_2026) feature is now in General Availability (GA).

Rollback is not supported for integrations built for Python 2.7 or 3.7. To perform a rollback, a snapshot must have been created during the previous upgrade process. For more information, see [Roll back response integration version](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/version-rollback).

## January 21, 2026

Feature

**Direct ingestion for Google Cloud Model Armor logs**

You can now ingest Google Cloud Model Armor logs (`GCP_MODEL_ARMOR`) directly into Google SecOps. Use an export filter for direct ingestion and access the logs through Google Cloud logging. Model Armor logs provide a unified window into AI-specific threats, such as prompt injection and sensitive data leakage.

For more information, see [Model Armor Documentation to Configure Logging](https://docs.cloud.google.com/model-armor/configure-logging).

Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

  * [Collect Active Countermeasures AI-Hunter logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ai-hunter)
  * [Collect ADVA Fiber Service Platform logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/adva-fsp)
  * [Collect AIX system logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aix-system)
  * [Collect Akamai SIEM Connector logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-siem-connector)
  * [Collect AMD Pensando DSS firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/amd-pensando-dss-firewall)
  * [Collect Azure NSG Flow logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-nfg-flow)
  * [Collect Cloudflare Page Shield logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare-pageshield)
  * [Collect FingerprintJS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fingerprint-js)
  * [Collect FireEye eMPS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-emps)
  * [Collect Forcepoint Email Security logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-emailsecurity)
  * [Collect Forcepoint NGFW logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-ngfw)
  * [Collect Fortinet FortiSASE logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortianalyzer)
  * [Collect IBM DB2 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/db2-db)
  * [Collect ManageEngine ADManager Plus logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/admanager-plus)
  * [Collect Microsoft Azure Resource logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-resource-logs)
  * [Collect Microsoft Intune Context logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-mdm-intune-context)
  * [Collect Ubiquiti Unifi switch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ubiquiti-unifi-switch)
  * [Collect Vectra Detect logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-detect)
  * [Collect Vectra Stream logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-stream)
  * [Collect Voltage SecureMail logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/voltage-sm)
  * [Collect Wallix Bastion logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wallix-bastion)



## January 18, 2026

Feature

**Integration Rollback**

This feature is currently in Preview.

You can now roll back commercial response integrations to their previously installed version. This action reverts all integration content, including standard code and any custom modifications, to the state of the last installed version. For more information, see [Roll back response integration version](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/version-rollback).

## January 16, 2026

Feature

**Perform all-time searches**

You can now run searches over your full retention period by clicking the **Time Picker** on the **Search editor** panel and selecting **All Time**. This functionality is supported for event searches, and results remain limited to a maximum of 1M events.

For more information, see [Search for events and alerts](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search).

## January 15, 2026

Feature

**OneMCP for Google SecOps**

You can use the [Google SecOps remote MCP server](https://docs.cloud.google.com/chronicle/docs/secops/use-google-secops-mcp) to enable LLM agents to perform a range of data-related tasks.

This feature is in Preview.

## January 13, 2026

Announcement

**Auto extraction general availability**

As part of the GA release for the auto extraction feature, customers now need to opt-in and choose which fields to extract. (Full auto extraction is no longer supported.) The _opt-in_ functionality does not impact the extracted fields that are already in use (in saved searches and rules), because those fields have been automatically opted-in as part of the GA migration.

For more information, see [Auto Extraction overview](https://docs.cloud.google.com/chronicle/docs/event-processing/auto-extraction).

Announcement

**Self-service deprovisioning general availability**

The self-service deprovisioning feature is now GA.

For more information, see [Self-service deprovisioning for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/customer-initiated-secops-deprovision).

## January 12, 2026

Feature

**Copy instance metadata**

To enable Google support to test and troubleshoot customer issues, a new option to copy SOAR information and share with Support has been added to the platform. This option, entitled **Copy instance metadata** , can be accessed from the question mark at the top of the platform.

## January 07, 2026

Change

**Expanded capabilities for Gemini in SecOps**

You can now use the Gemini assistant in Google SecOps to answer questions beyond the scope of security or the product. You can integrate the full power of Gemini (for example, general knowledge, coding, and data analysis) without switching tabs or leaving your workflow.

For more information, see [Gemini in Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/gemini-chronicle).

## December 24, 2025

Feature

**ThreatConnect IOC V3 Connector**

Google SecOps now supports the ingestion of Indicators of Compromise (IOCs) from ThreatConnect using the v3 REST API. This updated connector replaces the existing v2-based integration and introduces several enhancements:

  * **Advanced Filtering with TQL** : Use ThreatConnect Query Language (TQL) to perform highly targeted searches based on complex criteria like confidence scores, tags, or specific timeframes.
  * **Efficient Single-Call Data Ingestion** : Ingest complete indicator objects—including attributes, tags, and security labels—in a single API call to reduce overhead and improve performance.
  * **Synchronization Gaps** : Changes in ThreatConnect (for example, ThreatAssessmentScore, confidence, tags) are now replicated into the platform every 30 minutes.



Data ingested through this connector is identified by the new log type `THREATCONNECT_IOC_V3`.

For more information, see [Collect ThreatConnect IOC logs using the v3 API](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc-v3).

Announcement

**Understand your Google SecOps billing components**

A new document is available that helps you understand your Google Security Operations billing components. The document provides information about how to track your usage and the related cost. For more information, see [Understand your Google SecOps billing](https://docs.cloud.google.com/chronicle/docs/onboard/understand-billing).

## December 18, 2025

Announcement

**Understand how to view your billed ingestion volume**

A new document is available that helps you understand your billed ingestion volume. The document provides instructions on how to view and monitor the ingestion volume for the various tenants that you manage. For more information, see [View your billed ingestion volume](https://docs.cloud.google.com/chronicle/docs/ingestion/view-billed-ingestion-volume).

## December 17, 2025

Announcement

The [Change views per alert feature](https://docs.cloud.google.com/chronicle/docs/secops/release-notes#December_07_2025) has been rolled back. 

## December 10, 2025

Announcement

**Learn key differences between SPL and YARA-L 2.0**

A new guide is available to explain the key differences between Splunk Search Processing Language (SPL) and Google Security Operations YARA-L 2.0. The guide provides examples for converting common SPL queries and aims to accelerate the onboarding process for security professionals who transition to YARA-L 2.0. For more information, see [Transition from SPL to YARA-L](https://docs.cloud.google.com/chronicle/docs/yara-l/transition_spl_yaral).

## December 09, 2025

Feature

**Create new reference lists**

You can still create new reference lists.

This feature nullifies certain content in the [release note from August 19, 2025](https://docs.cloud.google.com/chronicle/docs/release-notes#August_19_2025), which specified that from October 2025, you would no longer be able to create new reference lists.

**Note:** Because the reference list functionality is being phased out of the Google SecOps platform (see "Reference lists" in [Feature deprecations](https://docs.cloud.google.com/chronicle/docs/deprecations)), we recommend that you use [data tables](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables) to provide expanded functionality, instead of reference lists.

## December 08, 2025

Feature

**N OF and OR syntax updates**

You can now use the N OF syntax and the `or` operator to write flexible and conditional logic within the `condition` section of your query. These features let you combine multiple conditions, reducing the overall complexity of your query syntax.

For more information, see [Use or in the condition section](https://docs.cloud.google.com/chronicle/docs/yara-l/multievent-or) and [Use N OF syntax with event variables](https://docs.cloud.google.com/chronicle/docs/yara-l/multievent-n-of).

## December 07, 2025

Feature

**Change views per alert**

The **Alert Overview** page now includes a new option to select a specific view for each alert. If several playbooks have run on an alert, and those playbooks have customized views, you can now select and display any of those customized views for that alert.

## December 03, 2025

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

  * 1Password (`ONEPASSWORD`)
  * A10 Load Balancer (`A10_LOAD_BALANCER`)
  * Abnormal Security (`ABNORMAL_SECURITY`)
  * AIX system (`AIX_SYSTEM`)
  * Akamai SIEM Connector (`AKAMAI_SIEM_CONNECTOR`)
  * AlgoSec Security Management (`ALGOSEC`)
  * Amazon API Gateway (`AWS_API_GATEWAY`)
  * Amazon VPC Transit Gateway Flow Logs (`AWS_VPC_TRANSIT_GATEWAY`)
  * Apache (`APACHE`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * Arista Switch (`ARISTA_SWITCH`)
  * Armis Activities (`ARMIS_ACTIVITIES`)
  * Aruba (`ARUBA_WIRELESS`)
  * Aruba Switch (`ARUBA_SWITCH`)
  * Attivo Networks (`ATTIVO`)
  * Auth0 (`AUTH_ZERO`)
  * AWS Aurora (`AWS_AURORA`)
  * AWS CloudFront (`AWS_CLOUDFRONT`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS CloudWatch (`AWS_CLOUDWATCH`)
  * AWS Config (`AWS_CONFIG`)
  * AWS GuardDuty (`GUARDDUTY`)
  * AWS Security Hub (`AWS_SECURITY_HUB`)
  * AWS Session Manager (`AWS_SESSION_MANAGER`)
  * AWS VPC Flow (`AWS_VPC_FLOW`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure AD Organizational Context (`AZURE_AD_CONTEXT`)
  * Azure Firewall (`AZURE_FIREWALL`)
  * Azure Storage Audit (`AZURE_STORAGE_AUDIT`)
  * Barracuda Firewall (`BARRACUDA_FIREWALL`)
  * BeyondTrust (`BOMGAR`)
  * BeyondTrust BeyondInsight (`BEYONDTRUST_BEYONDINSIGHT`)
  * BeyondTrust Secure Remote Access (`BEYONDTRUST_REMOTE_ACCESS`)
  * Bindplane Agent (`BINDPLANE_AGENT`)
  * Bitdefender (`BITDEFENDER`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Cambium Networks (`CAMBIUM_NETWORKS`)
  * Carbon Black (`CB_EDR`)
  * Carbon Black App Control (`CB_APP_CONTROL`)
  * Cequence Bot Defense (`CEQUENCE_BOT_DEFENSE`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Check Point Sandblast (`CHECKPOINT_EDR`)
  * Chrome Management (`CHROME_MANAGEMENT`)
  * CipherTrust Manager (`CIPHERTRUST_MANAGER`)
  * Cisco AMP (`CISCO_AMP`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Email Security (`CISCO_EMAIL_SECURITY`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco Firewall Services Module (`CISCO_FWSM`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco IronPort (`CISCO_IRONPORT`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Meraki (`CISCO_MERAKI`)
  * Cisco Router (`CISCO_ROUTER`)
  * Cisco Secure Access (`CISCO_SECURE_ACCESS`)
  * Cisco Stealthwatch (`CISCO_STEALTHWATCH`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco UCM (`CISCO_UCM`)
  * Cisco Umbrella Audit (`CISCO_UMBRELLA_AUDIT`)
  * Cisco Umbrella Cloud Firewall (`UMBRELLA_FIREWALL`)
  * Cisco Umbrella DNS (`UMBRELLA_DNS`)
  * Cisco Umbrella IP (`UMBRELLA_IP`)
  * Cisco Umbrella SWG DLP (`CISCO_UMBRELLA_SWG_DLP`)
  * Cisco Umbrella Web Proxy (`UMBRELLA_WEBPROXY`)
  * Cisco WSA (`CISCO_WSA`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Claroty Continuous Threat Detection (`CLAROTY_CTD`)
  * Claroty Xdome (`CLAROTY_XDOME`)
  * Cloudflare (`CLOUDFLARE`)
  * Cloudflare Network Analytics (`CLOUDFLARE_NETWORK_ANALYTICS`)
  * Cloudflare WAF (`CLOUDFLARE_WAF`)
  * Cloudflare Warp (`CLOUDFLARE_WARP`)
  * Code42 Incydr (`CODE42_INCYDR`)
  * Corelight (`CORELIGHT`)
  * CoSoSys Protector (`ENDPOINT_PROTECTOR_DLP`)
  * CrowdStrike Alerts API (`CS_ALERTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CrowdStrike Falcon Stream (`CS_STREAM`)
  * Cyber 2.0 IDS (`CYBER_2_IDS`)
  * CyberArk Endpoint Privilege Manager (EPM) (`CYBERARK_EPM`)
  * Cyberark Privilege Cloud (`CYBERARK_PRIVILEGE_CLOUD`)
  * CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
  * Cybereason EDR (`CYBEREASON_EDR`)
  * Cynet 360 AutoXDR (`CYNET_360_AUTOXDR`)
  * Cyolo Secure Remote Access for OT (`CYOLO_OT`)
  * Darktrace (`DARKTRACE`)
  * Delinea Secret Server (`DELINEA_SECRET_SERVER`)
  * Digital Guardian DLP (`DIGITALGUARDIAN_DLP`)
  * Digital Guardian EDR (`DIGITALGUARDIAN_EDR`)
  * DigitalArts i-Filter (`DIGITALARTS_IFILTER`)
  * Dummy LogType (`DUMMY_LOGTYPE`)
  * EfficientIP DDI (`EFFICIENTIP_DDI`)
  * ESET AV (`ESET_AV`)
  * ESET Threat Intelligence (`ESET_IOC`)
  * Extreme Networks Switch (`EXTREME_SWITCH`)
  * F5 Advanced Firewall Management (`F5_AFM`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP Access Policy Manager (`F5_BIGIP_APM`)
  * F5 Silverline (`F5_SILVERLINE`)
  * FireEye ETP (`FIREEYE_ETP`)
  * Fluentd Logs (`FLUENTD`)
  * Forcepoint NGFW (`FORCEPOINT_FIREWALL`)
  * Forcepoint DLP (`FORCEPOINT_DLP`)
  * Forcepoint Proxy (`FORCEPOINT_WEBPROXY`)
  * Forescout NAC (`FORESCOUT_NAC`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortinet FortiEDR (`FORTINET_FORTIEDR`)
  * GCP Abuse Events Logs (`GCP_ABUSE_EVENTS`)
  * GitHub (`GITHUB`)
  * GMV Checker ATM Security (`GMV_CHECKER`)
  * Google Cloud Apigee (`GCP_APIGEE`)
  * Google Cloud Audit (`GCP_CLOUDAUDIT`)
  * Google Cloud Security Center Threat (`GCP_SECURITYCENTER_THREAT`)
  * Google Threat Intelligence IOC (`GTI_IOC`)
  * GTB Technologies DLP (`GTB_DLP`)
  * H3C Comware Platform Switch (`H3C_SWITCH`)
  * Halcyon Anti Ransomware (`HALCYON`)
  * HP Aruba (ClearPass) (`CLEARPASS`)
  * HP Linux (`HP_LINUX`)
  * HP Procurve Switch (`HP_PROCURVE`)
  * IBM AS/400 (`IBM_AS400`)
  * IBM Security Verify Access (`IBM_SVA`)
  * IBM WebSEAL (`IBM_WEBSEAL`)
  * IBM Websphere Application Server (`IBM_WEBSPHERE_APP_SERVER`)
  * IBM z/OS (`IBM_ZOS`)
  * Imperva (`IMPERVA_WAF`)
  * Imperva DRA (`IMPERVA_DRA`)
  * Imperva SecureSphere Management (`IMPERVA_SECURESPHERE`)
  * Infoblox (`INFOBLOX`)
  * Infoblox DHCP (`INFOBLOX_DHCP`)
  * Infoblox DNS (`INFOBLOX_DNS`)
  * ION Spectrum (`ION_SPECTRUM`)
  * Ionix (`IONIX`)
  * Ipswitch MOVEit Transfer (`IPSWITCH_MOVEIT_TRANSFER`)
  * Island Browser logs (`ISLAND_BROWSER`)
  * JAMF Pro (`JAMF_PRO`)
  * Jamf Protect Telemetry V2 (`JAMF_TELEMETRY_V2`)
  * JFrog Artifactory (`JFROG_ARTIFACTORY`)
  * Journald (`JOURNALD`)
  * JumpCloud Directory Insights (`JUMPCLOUD_DIRECTORY_INSIGHTS`)
  * Juniper (`JUNIPER_FIREWALL`)
  * Juniper Junos (`JUNIPER_JUNOS`)
  * Kaspersky AV (`KASPERSKY_AV`)
  * Kaspersky Endpoint (`KASPERSKY_ENDPOINT`)
  * Keycloak (`KEYCLOAK`)
  * Kiteworks (`KITEWORKS`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * Linux Sysmon (`LINUX_SYSMON`)
  * McAfee ePolicy Orchestrator (`MCAFEE_EPO`)
  * Microsoft AD FS (`ADFS`)
  * Microsoft Azure NSG Flow (`AZURE_NSG_FLOW`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Defender for Office 365 (`MICROSOFT_DEFENDER_MAIL`)
  * Microsoft Exchange (`EXCHANGE_MAIL`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft IIS (`IIS`)
  * Microsoft Intune (`AZURE_MDM_INTUNE`)
  * Microsoft PowerShell (`POWERSHELL`)
  * Microsoft Sentinel (`MICROSOFT_SENTINEL`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * Mikrotik Router (`MIKROTIK_ROUTER`)
  * Mimecast Mail V2 (`MIMECAST_MAIL_V2`)
  * MISP Threat Intelligence (`MISP_IOC`)
  * Mobileiron (`MOBILEIRON`)
  * NetApp ONTAP (`NETAPP_ONTAP`)
  * Netscout (`ARBOR_EDGE_DEFENSE`)
  * Netskope CASB (`NETSKOPE_CASB`)
  * Netskope V2 (`NETSKOPE_ALERT_V2`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * Nexus Sonatype (`NEXUS_SONATYPE`)
  * Nozomi Networks Scada Guardian (`NOZOMI_GUARDIAN`)
  * Obsidian (`OBSIDIAN`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * Open Cybersecurity Schema Framework (OCSF) (`OCSF`)
  * Open LDAP (`OPENLDAP`)
  * Opnsense (`OPNSENSE`)
  * Opswat Metadefender (`OPSWAT_METADEFENDER`)
  * Oracle (`ORACLE_DB`)
  * Oracle Cloud Infrastructure Audit Logs (`OCI_AUDIT`)
  * Oracle Cloud Infrastructure VCN Flow Logs (`OCI_FLOW`)
  * Orca Cloud Security Platform (`ORCA`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * Palo Alto Cortex XDR Events (`PAN_CORTEX_XDR_EVENTS`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Palo Alto Prisma Cloud Alert payload (`PAN_PRISMA_CA`)
  * Passwordstate (`PASSWORDSTATE`)
  * Ping Federate (`PING_FEDERATE`)
  * Ping Identity (`PING`)
  * Ping One (`PING_ONE`)
  * PingIdentity Directory Server Logs (`PING_DIRECTORY`)
  * PostFix Mail (`POSTFIX_MAIL`)
  * PostgreSQL (`POSTGRESQL`)
  * Proofpoint Observeit (`OBSERVEIT`)
  * Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Proofpoint Threat Response (`PROOFPOINT_TRAP`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * RSA (`RSA_AUTH_MANAGER`)
  * Ruckus Networks (`RUCKUS_WIRELESS`)
  * SailPoint IAM (`SAILPOINT_IAM`)
  * Salesforce (`SALESFORCE`)
  * Sangfor Next Generation Firewall (`SANGFOR_NGAF`)
  * Security Command Center Chokepoint (`GCP_SECURITYCENTER_CHOKEPOINT`)
  * Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
  * Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
  * Semperis DSP (`SEMPERIS_DSP`)
  * Sentinelone Activity (`SENTINELONE_ACTIVITY`)
  * SentinelOne Deep Visibility (`SENTINEL_DV`)
  * ServiceNow Audit (`SERVICENOW_AUDIT`)
  * Solaris system (`SOLARIS_SYSTEM`)
  * SonicWall (`SONIC_FIREWALL`)
  * Squid Web Proxy (`SQUID_WEBPROXY`)
  * STIX Threat Intelligence (`STIX`)
  * Swift Alliance Messaging Hub (`SWIFT_AMH`)
  * Symantec Endpoint Protection (`SEP`)
  * Tanium Audit (`TANIUM_AUDIT`)
  * Tanium Integrity Monitor (`TANIUM_INTEGRITY_MONITOR`)
  * Tanium Threat Response (`TANIUM_THREAT_RESPONSE`)
  * Teleport Access Plane (`TELEPORT_ACCESS_PLANE`)
  * Tenable Active Directory Security (`TENABLE_ADS`)
  * Tenable OT (`TENABLE_OT`)
  * tenable.io (`TENABLE_IO`)
  * Thales Luna Hardware Security Module (`THALES_LUNA_HSM`)
  * Thales MFA (`THALES_MFA`)
  * Trellix HX Event Streamer (`TRELLIX_HX_ES`)
  * Trend Micro (`TIPPING_POINT`)
  * Trend Micro Apex one (`TRENDMICRO_APEX_ONE`)
  * Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
  * Trend Micro Vision One Audit (`TRENDMICRO_VISION_ONE_AUDIT`)
  * Trend Micro Vision One Detections (`TRENDMICRO_VISION_ONE_DETECTIONS`)
  * Trend Micro Vision One Observerd Attack Techniques (`TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES`)
  * TXOne Stellar (`TRENDMICRO_STELLAR`)
  * Ubika Waf (`UBIKA_WAF`)
  * Unix system (`NIX_SYSTEM`)
  * Upstream Vehicle SOC Alerts (`UPSTREAM_VSOC_ALERTS`)
  * Varonis (`VARONIS`)
  * Vectra Stream (`VECTRA_STREAM`)
  * Venafi ZTPKI (`VENAFI_ZTPKI`)
  * Veritas NetBackup (`VERITAS_NETBACKUP`)
  * Versa Firewall (`VERSA_FIREWALL`)
  * Vmware Avinetworks iWAF (`VMWARE_AVINETWORKS_IWAF`)
  * VMware ESXi (`VMWARE_ESX`)
  * VMware NSX (`VMWARE_NSX`)
  * VMware vCenter (`VMWARE_VCENTER`)
  * WatchGuard (`WATCHGUARD`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Windows Sysmon (`WINDOWS_SYSMON`)
  * wiz.io (`WIZ_IO`)
  * Workday User Activity (`WORKDAY_USER_ACTIVITY`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * Workspace Alerts (`WORKSPACE_ALERTS`)
  * Workspace Users (`WORKSPACE_USERS`)
  * Zendesk CRM (`ZENDESK_CRM`)
  * Zoom Operation Logs (`ZOOM_OPERATION_LOGS`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * ZScaler NGFW (`ZSCALER_FIREWALL`)
  * Zscaler Private Access (`ZSCALER_ZPA`)
  * Zscaler Secure Private Access Audit Logs (`ZSCALER_ZPA_AUDIT`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

  * Absolute Secure Endpoint (`ABSOLUTE_SECURE_ENDPOINT`)
  * Airbus Security Logging (ACD AISD) (`AIRBUS_SECURITY_LOG`)
  * Azure Recovery Services Vaults (`AZURE_RECOVERY_SERVICES_VAULTS`)
  * Boeing Onboard Network System Logging (`BOEING_ONS`)
  * Cisco Firepower Threat Defense (`CISCO_FIREPOWER_THREAT_DEFENSE`)
  * Cisco Security Cloud Control (`CISCO_SECURITY_CLOUD_CONTROL`)
  * Pico Corvilnet Engine (`CORVILNET_ENGINE`)
  * CrowdStrike Falcon Shield (`CROWDSTRIKE_FALCON_SHIELD`)
  * Easy NAC (`EASY_NAC`)
  * FairXchange Horizon (`FAIRXCHANGE_HORIZON`)
  * Google Threat Intelligence (`GCP_THREATINTEL`)
  * HPE Alletra (`HPE_ALLETRA`)
  * Huawei Cloud Trace Service Audit (`HUAWEI_CTS_AUDIT`)
  * Huawei SecMaster (`HUAWEI_SECMASTER`)
  * IBM ILO (`IBM_ILO`)
  * Infisical (`INFISICAL`)
  * JSCAPE SFTP (`JSCAPE_SFTP`)
  * Juniper Edge (`JUNIPER_EDGE`)
  * Kaspersky for Microsoft Office 365 (`KASPERSKY_O365_EVENTS`)
  * Microsoft Defender for Cloud Apps (`MICROSOFT_DEFENDER_CLOUD_APPS`)
  * Oracle Cloud Infrastructure Network Firewall (`OCI_FIREWALL`)
  * Okta Workflows (`OKTA_WORKFLOWS`)
  * Phosphorus (`PHOSPHORUS`)
  * Rapid7 Cloud Security (`RAPID7_CLOUDSEC`)
  * Research and Education Networks Information Sharing and Analysis Center (`REN_ISAC`)
  * Risk Resecurity (`RISK_RESECURITY`)
  * Sangfor Network Detection and Response (`SANGFOR_NDR`)
  * SAP Enterprise Threat Detection (`SAP_ETD`)
  * SAP IAS Context (`SAP_IAS_CONTEXT`)
  * Sectigo SCM (`SECTIGO_SCM`)
  * ServiceNow Node (`SERVICENOW_NODE`)
  * ServiceNow Outbound HTTP (`SERVICENOW_OUTBOUNDHTTP`)
  * ServiceNow System log (`SERVICENOW_SYSLOG`)
  * ServiceNow Transaction (`SERVICENOW_TRANSACTION`)
  * Seti S4 (`SETI_S4`)
  * ThousandEyes (`THOUSAND_EYES`)
  * Transmit Security Mosaic CIAM (`TRANSMIT_MOSAIC_CIAM`)
  * Transmit Security Mosaic Fraud Prevention (`TRANSMIT_MOSAIC_FRAUD_PREVENTION`)
  * Transmit Security Mosaic Identity Verification (`TRANSMIT_MOSAIC_IDENTITY_VERIFICATION`)
  * Transmit Security Mosaic Management (`TRANSMIT_MOSAIC_MANAGEMENT`)
  * Tripwire Security Configuration Management (`TRIPWIRE_SCM`)
  * Valimail (`VALIMAIL`)
  * WSO2 IS AM (`WSO2_IS_AM`)
  * XDR.Net Digital Twin (`XDRNET_DIGITALTWIN`)
  * Zimbra Mail (`ZIMBRA_MAIL`)
  * Zscaler Email DLP (`ZSCALER_EMAIL_DLP`)



## November 13, 2025

Feature

**Raw log search enhancements**

Google SecOps now includes enhancements to raw log search to boost usability, performance, and data analysis:

  * **New filtering options** : Filter raw log results by their parsing status or by one or more log sources.

  * **Optimized results view** : Expand or collapse the Trend over time graph, providing more space for results.

  * **Download raw log results** : Download raw log results to a CSV file. By default, the **Timestamp** , **Type** , and **Raw Log** columns are included. You can select additional columns through **Column Manager**.

  * **Enhanced search visibility** : The search query and applied filters are now displayed on the **Search** page.

  * **New API for raw log search** : Use the **legacySearchRawLogsV2** API to search for raw logs within a specified Google SecOps instance.




For more details, see the following topics:

  * [Filter data in Raw Log Search](https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-raw-log-scan-view)
  * [Search raw logs](https://docs.cloud.google.com/chronicle/docs/investigation/search-raw-logs)
  * [Method: legacy.legacySearchRawLogsV2](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacySearchRawLogsV2)



## November 12, 2025

Feature

**Use the Triage Agent to investigate alerts**

You can now use Triage Agent, an AI-powered investigation assistant, to analyze alerts in Google SecOps. Triage Agent determines if an alert is a true or false positive, provides a summarized explanation for its conclusion, and suggests next steps for further investigation.

You can trigger investigations manually or have them run automatically on supported alert types. Each investigation produces a detailed report that includes the agent's disposition, a summary of its findings, and a timeline of the analysis.

For more details, see [Use Triage Agent to investigate alerts](https://docs.cloud.google.com/chronicle/docs/secops/triage-agent).

Feature

**Enhance threat visibility and detection with Emerging Threats**

The new **Emerging Threats** page provides AI-powered threat intelligence to help you understand how current threat campaigns might affect your organization. Powered by Google Threat Intelligence (GTI) and Gemini models, this page offers a curated view of critical global threats relevant to your environment.

Emerging Threats continuously aligns intelligence from GTI with your organization's telemetry to highlight detection coverage and identify gaps. When it finds a gap, it uses Gemini to automatically draft new detection rules to accelerate your response.

For more details, see [Emerging Threats overview](https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats), [Emerging Threats feed](https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats-feed),and [Emerging Threats detailed view](https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats-detailed-view).

Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

  * [Collect Absolute Secure Endpoint logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/absolute-se)
  * [Collect AIDE (Advanced Intrusion Detection Environment) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aide)
  * [Collect Akamai Enterprise Application Access logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-eaa)
  * [Collect Apache Hadoop logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hadoop)
  * [Collect Armis Vulnerabilities logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-vulnerabilities)
  * [Collect Array Networks SSL VPN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arraynetworks-vpn)
  * [Collect Aruba IPS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-ips)
  * [Collect Atlassian Confluence logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-confluence)
  * [Collect Cisco AMP for Endpoints logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-amp)
  * [Collect Cisco APIC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-apic)
  * [Collect Cisco Application Centric Infrastructure (ACI) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-aci)
  * [Collect Cisco CallManager logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-call-manager)
  * [Collect Cisco CloudLock CASB logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-cloudlock-casb)
  * [Collect Cisco DNA Center Platform logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-dnac)
  * [Collect Cisco eStreamer logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-estreamer)
  * [Collect Cribl Stream logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cribl-stream)
  * [Collect CrowdStrike FileVantage logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-filevantage)
  * [Collect CrowdStrike IDP Services logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-idp)
  * [Collect Cynet 360 AutoXDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cynet-360-autoxdr)
  * [Collect Digital Shadows SearchLight logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digital-shadows-searchlight)
  * [Collect Duo Telephony logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-telephony)
  * [Collect Edgio WAF logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/edgio-waf)
  * [Collect Elastic Auditbeat logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-auditbeat)
  * [Collect Elastic Packet Beats logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-packetbeats)
  * [Collect Elasticsearch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-search)
  * [Collect Entrust nShield HSM audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/entrust-hsm)
  * [Collect Imperva Advanced Bot Protection logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-abp)
  * [Collect Imperva Attack Analytics logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-attack-analytics)
  * [Collect Imperva Audit Trail logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-audit-trail)
  * [Collect Imperva CEF logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-cef)
  * [Collect Imperva Data Risk Analytics (DRA) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-dra)
  * [Collect Imperva Database logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-db)
  * [Collect Imperva FlexProtect logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-flexprotect)
  * [Collect Imperva SecureSphere Management logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-securesphere)
  * [Collect Kiteworks (formally Accellion) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/accellion)
  * [Collect Proofpoint Emerging Threats Pro IOC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/et-pro-ioc)
  * [Collect ServiceNow audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-audit)
  * [Collect Team Cymru Scout Threat Intelligence data](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/team-cymru-scout-threatintel)
  * [Collect URLScan IO logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/urlscan-io)
  * [Collect Uptycs EDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/uptycs-edr)
  * [Collect VanDyke VShell SFTP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vandyke-sftp)
  * [Collect Zendesk CRM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zendesk-crm)
  * [Collect ZeroFox Platform logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zerofox-platform)



## November 10, 2025

Feature

**Nested if**

You can now use `if` statements in both the `outcome` and `events` sections and also within the `then` `else` clauses of another `if` statement. This capability lets you introduce more complicated logic to your query and is supported in Rules, Search, and Dashboards.

For more information, see [Use nested if statements for more complex logic](https://docs.cloud.google.com/chronicle/docs/yara-l/nested-if).

## November 07, 2025

Change

**MITRE ATT &CK coverage dashboard is now available**

The new [MITRE ATT&CK coverage dashboard](https://docs.cloud.google.com/chronicle/docs/detection/mitre-dashboard) lets you measure your security posture against the MITRE ATT&CK framework, helping you:

  * Assess threat coverage
  * Identify gaps
  * Prioritize security efforts



## October 31, 2025

Feature

**Search usability enhancements**

Google SecOps has introduced the following capabilities to improve usability, performance, and customization in search results:

  * **Improved performance for large result sets** : For broad queries, Google SecOps now provides paginated search results. You can select the number of rows to display per page. This pagination applies to the 10,000 results displayed in the table.

  * **Optimized results view** : The search editor now automatically collapses after a query runs, providing more space for results. You can also hide or show the **Charts** and **Aggregations** panels with the **View Options** list.

  * **Customizable column views** : You can now create, save, and share custom sets of columns in the **Events** table for consistent analysis across teams.




For more details, see [Search for events and alerts](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search).

Change

**Custom log type rename**

From now on, all custom log types will be renamed with the custom suffix to prevent confusion with prebuilt log types. The following custom log types already reflect the new naming convention:

  * HUAWEI_SECMASTER_CUSTOM
  * GTI_THREAT_FEED_CUSTOM
  * GTI_IOC_STREAM_CUSTOM
  * ABSOLUTE_SECURE_ENDPOINT_CUSTOM
  * GTI_IOC_CUSTOM
  * IBM_ILO_CUSTOM
  * GCP_THREATINTEL_CUSTOM
  * SAP_ETD_CUSTOM



## October 30, 2025

Feature

**YARA-L functions**

The following new YARA-L functions are now generally available:

  * [strings.ends_with](https://docs.cloud.google.com/chronicle/docs/yara-l/functions#stringsends_with): Takes two strings (value, suffix) and returns true if the suffix is non-empty and at end-of-value.

  * [strings.split](https://docs.cloud.google.com/chronicle/docs/yara-l/functions#stringssplit): Splits string value using a delimiter argument (by default, a comma).

  * [window.range](https://docs.cloud.google.com/chronicle/docs/yara-l/functions#windowrange): Returns the range of the values input values found.




Announcement

**Upgraded Chronicle API ingestion methods from alpha to beta**

We've upgraded the Chronicle API ingestion methods from alpha to beta. This upgrade signals API stability and functional completeness, unblocking customer and partner adoption for production integrations.

For more information, see [Ingestion methods](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods).

## October 29, 2025

Feature

**Improved Support for Chrome Enterprise Premium**

This feature is currently in Preview.

An improved integration for Chrome Enterprise Premium is now available that includes:

  * Streamlined connection to Google SecOps, using recommended security defaults
  * Enhanced log events with Google Safe Browsing context
  * Updated parser and integration documentation: [Collect Google Chrome logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chrome-management)
  * Curated dashboards for Chrome Enterprise Premium
  * Google Workspace SOAR actions to manage Chrome extension blocklist policies ([Block Extension](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-workspace#block_extension) and [Delete Extension](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-workspace#delete_extension))



## October 28, 2025

Feature

**Risk-based alerting with entity-only rules**

With the new `ENTITY_RISK_CHANGE` UDM event type, you can now write YARA-L detection rules that trigger independently of ingested events. This capability lets you focus specifically on changes in an entity's risk score, significantly decreasing the time required for Google Security Operations to detect and alert on shifting entity risk levels.

For more information, see [Risk-based alerting with entity-only rules](https://docs.cloud.google.com/chronicle/docs/detection/risk-based-alerting).

## October 27, 2025

Announcement

**New rules for Chrome Enterprise Premium**

Curated Detections has been enhanced with additional Chrome Enterprise Premium Browser Threat detections. The following rules have been added to the rulepack:

  * Archive Exfiltration Event to Non-Google Websites
  * Google Chrome Navigation Event to Shortened URLs
  * Suspicious Download from Filehosting or Chat Platform in Chrome Management
  * Chrome Suspicious Download Event from Newly Observed Domain in Environment



## October 26, 2025

Feature

**Delete high-load SOAR environments**

You can now easily delete environments with heavy loads directly from the platform.

## October 22, 2025

Change

**Integration of GTI score in Applied Threat Intelligence (ATI)**

Google SecOps now uses Google Threat Intelligence (GTI) score for prioritization in Applied Threat Intelligence (ATI) instead of the IC-score. The GTI score delivers a unified verdict for potential Indicators of Compromise (IoCs) and aggregates a wealth of threat intelligence data.

For details, see [Applied Threat Intelligence priority overview](https://docs.cloud.google.com/chronicle/docs/detection) and [Google Threat Intelligence (GTI) score overview](https://docs.cloud.google.com/chronicle/docs/detection/understand-ic-score).

## October 21, 2025

Announcement

**Premium[Fortinet Firewall parser](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-firewall) now available as Release Candidate**

This enhanced parser is available as a **Release Candidate** for the next 2 months. To opt in and begin testing it, go to **SIEM Settings > Parsers**. We encourage you to try it out and evaluate the improvements before it becomes the default.

## October 15, 2025

Deprecated

The Netskope v1 API feed has been deprecated by Netskope. If you are using the Netskope REST API v1 with Google SecOps, you must switch to the Netskope REST API v2.

## October 08, 2025

Feature

**Multi-stage queries in YARA-L**

This feature is currently in Preview.

Multi-stage queries in YARA-L are now available as a Preview feature. Multi-stage queries in YARA-L let you feed the output of one query stage directly into the input of a subsequent stage. This process gives you greater control over data transformation than single, monolithic query. They are supported in both **Dashboards** and **Search**. Multi-stage queries can contain between 1 and 4 named stages, in addition to a root stage.

For more information, see [Create multi-stage queries in YARA-L](https://docs.cloud.google.com/chronicle/docs/investigation/multi-stage-yaral).

## October 07, 2025

Feature

**Manage parser versions**

This feature is in preview.

You now have granular control over how new pre-built parser versions are deployed within your environment.

This feature lets you manage parser updates by taking the following actions:

  * Opt in or opt out of automatic parser updates.

  * Review and compare the processing logic between different parser versions.

  * Manually update a parser to a newer version.

  * Revert to a previously deployed, stable parser version.




For details, see [Manage prebuilt parser versions](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates#manage-parser-versions).

Announcement

**Azure AD Organizational Context default parser rollback**

The recent update to the pre-built Azure AD Organizational Context (`AZURE_AD_CONTEXT`) parser has been rolled back. This action was necessary to resolve a performance degradation issue that was introduced in the latest parser version. For more information about the exact changes and rollback timeline, see the [change log for the pre-built parser](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates#manage_parser_updates).

## October 06, 2025

Feature

**Advanced BigQuery Export**

This feature is in preview.

This feature is available for Google SecOps Enterprise Plus customers only.

Advanced BigQuery Export automatically provisions and manages essential Google SecOps datasets in a secure, Google-managed BigQuery project. You gain secure, read-only access to this data through a BigQuery linked dataset, which appears directly in your own Google Cloud project. This functionality lets you query your security data as if it were stored locally, but without the overhead of managing the data pipeline or storage.

For details, see [Use Advanced BigQuery Export](https://docs.cloud.google.com/chronicle/docs/reports/bigquery-export).

## October 05, 2025

Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

  * [Collect AlphaSOC alert logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asoc-alert)
  * [Collect AlphaSOC alert logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rippling-activitylogs)
  * [Collect Cisco vManage SD-WAN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-sdwan)
  * [Collect Citrix Analytics logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-analytics)
  * [Collect Citrix Monitor Service logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-ms)
  * [Collect Citrix StoreFront logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-storefront)
  * [Collect Delinea SSO logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-sso)
  * [Collect SailPoint IAM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sailpoint-iam)
  * [Collect Sentry logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentry)
  * [Collect Snipe-IT logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snipe-it)
  * [Collect Sophos AV logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-av)
  * [Collect Sophos Capsule8 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-cap8)
  * [Collect Sophos DHCP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-dhcp)
  * [Collect Sophos Intercept EDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-edr)
  * [Collect Swimlane Platform logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/swimlane)
  * [Collect Symantec WSS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-wss)
  * [Collect Tailscale logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tailscale)
  * [Collect Tanium Asset logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-asset)
  * [Collect Tanium audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-audit)
  * [Collect Tanium Comply logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-comply)
  * [Collect Tanium Discover logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-discover)
  * [Collect Tanium Insight logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-insight)
  * [Collect Tanium Integrity Monitor logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-im)
  * [Collect Tanium Patch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-patch)
  * [Collect Tanium Question logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-question)
  * [Collect Tanium Reveal logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-reveal)
  * [Collect Tanium Stream logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-stream)
  * [Collect Tanium Threat Response logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-tr)
  * [Collect TeamViewer logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/teamviewer)
  * [Collect Tines audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tines)



## October 03, 2025

Change

**Customer-managed encryption key compliance now includes support for data tables**

Google SecOps has expanded its coverage of Customer-Managed Encryption Key (CMEK) compliance to now include support for data tables.

For more information, see [CMEK for Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops).

## September 30, 2025

Feature

**Customize Events table columns in Search**

You can now specify which columns appear in the **Events** table on the **Search** page and in **tables** within your **dashboard widgets**. Use the `select` and `unselect` keywords to define the displayed columns.

For more information, see [Control columns using select and unselect keywords](https://docs.cloud.google.com/chronicle/docs/investigation/select-unselect).

## September 28, 2025

Announcement

**Forwarder component: end-of-life and migration**

The forwarder component is being phased out of the Google SecOps platform and will reach end-of-life (EOL) in January 2027. This impact will change all any data collection pipelines that currently use the forwarder. 

**Action required** : If you're currently using the forwarder component, you must migrate your data collection workflows to an alternative mechanism before April 1, 2027. You'll need to use another data pipeline management application for log ingestion.

We recommend that you migrate to the [Bindplane OpenTelemetry (OTel) collector](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent), which provides a scalable, open-standard solution for log and metric ingestion.

The following are key dates to note:

  * **Apr 1, 2026** : New Google SecOps customers cannot use the forwarder component. 
  * **Jan 1, 2027** : The forwarder is officially EOL. No further patches, including security patches, will be released. 
  * **Apr 1, 2027** : Data is no longer allowed to be ingested from the forwarder component. 



Announcement

Remote Agent, Release 2.5.0 contains the following changes:

Change

**Publisher Connector package size limit enforced**

The maximum allowed size for a Publisher's Connector Package is now limited to 25 MB.

Feature

**Debian support for remote agents**

You can now install a Remote Agent using Debian. This new functionality provides a streamlined deployment workflow—an alternative to existing installation methods. For details, see [Deploy an agent with Debian](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-on-debian).

Announcement

**Update CrowdStrike API permissions before decommission**

CrowdStrike is decommissioning its Detects API on September 30, 2025. This API has been replaced by the Alerts API. To ensure that your data feeds continue without interruption, you may need to update your API permissions.

This change impacts you if your Google SecOps tenant meets both of the following conditions:

  * You use the CrowdStrike Detection Monitoring API connector, which ingests the `CS_DETECTS` log type.
  * The CrowdStrike API client configured for that feed lacks the permissions to read alerts Read.



To prevent disruption to your CrowdStrike data ingestion, you must update your API client permissions before September 30, 2025. Follow the instructions in [Migrate from CrowdStrike Detects API to Alerts API](https://docs.cloud.google.com/chronicle/docs/detection/migrate-detects-api-to-alerts-api) to migrate your configuration to use the Alerts API.

For more details, see [CrowdStrike’s official decommissioning notice](https://supportportal.crowdstrike.com/s/article/Tech-Alert-30-Day-Notice-Planned-Decommission-Announcement-of-the-DetectionSummaryEvent-and-detects-API).

Feature

**Podman support for Remote Agents**

You can now install a Remote Agent using Podman. This new functionality provides a streamlined deployment workflow—a lightweight alternative to existing installation methods. For details, see [Deploy an agent with Podman](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-podman).

Change

**Increased Alert Trimming limit for Remote Agent**

The default setting for Alert Trimming has been increased to 25 MB.

## September 27, 2025

Feature

**Use joins in YARA-L Search queries**

These changes are currently in Preview.

You can now use joins in statistical Search queries that include a `match` section to correlate data from multiple sources. This feature lets you link related sources directly within a single query.

For more information, see [Use joins in Search](https://docs.cloud.google.com/chronicle/docs/investigation/search-joins).

## September 16, 2025

Announcement

**Migrate SOAR to Google Cloud**

We're actively migrating all SOAR customers and partners to their respective Google Cloud projects. This migration unifies your SOAR experience with your existing cloud environment. For more information, see [SOAR migration overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp) and [FAQ](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-faq).

## September 11, 2025

Feature

**SecOps Labs**

This feature is in preview.

You can now configure and run Google SecOps Gemini and other intelligence _experiments_ without disrupting your existing production systems—and benefit from their output. The experiments comply with the Role-Based Access Control (RBAC) configuration of your environment, and they have streamlined configurations with clear actionable results and output.

For details, see [Use Gemini and other experiments in Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-labs).

## September 10, 2025

Feature

**View data retention start date**

You can now view the start date for your account's data retention period. A new, read-only page, **Data Retention** , is available under **SIEM Settings**. This page also shows the start date for your Google SecOps account's data retention period.

For more information, see [View data retention in your Google SecOps account](https://docs.cloud.google.com/chronicle/docs/about/data-retention).

## September 08, 2025

Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

[Collect Akamai Cloud Monitor logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-cloud-monitor)   
[Collect Akamai DataStream 2 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-ds2)   
[Collect Aware audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aware-audit)   
[Collect AWS API Gateway access logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-api-gateway)   
[Collect AWS VPC Transit Gateway flow logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc-tgflow)   
[Collect Bitwarden Enterprise event logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bitwarden-ent-event)   
[Collect Box Collaboration JSON logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/box-collaboration-json)   
[Collect Censys logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/censys)   
[Collect Code42 Incydr core datasets](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/code42-incydr)   
[Collect CSV Custom IOC files](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/csv-custom-ioc)   
[Collect Deep Instinct EDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/deep-ins-edr)   
[Collect DigiCert audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digicert-audit)   
[Collect DomainTools Iris Investigate results](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dt-iris-investigate)   
[Collect Duo administrator logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-admin)   
[Collect Duo authentication logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-auth)   
[Collect Duo entity context logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-entity)   
[Collect Google Cloud Abuse Events logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-abuse-events)   
[Collect Harness IO audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/harness-io-audit)   
[Collect HPE Aruba Networking Central logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hpe-anc)   
[Collect Jamf Pro context logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-pro-context)   
[Collect PingOne Advanced Identity Cloud logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pingone-advanced-identity)   
[Collect Slack audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/slack-audit)   
[Collect Snyk group-level audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snyk-group-audit)   
[Collect Snyk group-level audit and issues logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snyk-group-issues)   
[Collect Venafi Zero Touch PKI logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/venafi-ztpki)   
[Collect Veritas NetBackup logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veritas-netbackup)   
[Collect VMware AirWatch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-airwatch)   
[Collect VMware Avi Load Balancer WAF logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-avilb-waf)   
[Collect VMware Horizon logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-horizon)   
[Collect VMware VeloCloud SD-WAN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-velocloud-sdwan)   
[Collect Zoom operation logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zoom-operations)

## September 07, 2025

Feature

**Use custom fields in the Close Case dialog**

Administrators can now add custom fields to the **Close Case** dialog. This new functionality provides a more streamlined workflow and replaces the **Dynamic Fields** feature.

For more information, see [Use custom fields in the Close Case dialog](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/custom-fields-in-case-closure).

Feature

**Advanced job scheduling**

The job scheduling functionality has been enhanced with advanced options. This functionality provides more precise control and flexible, calendar-like scheduling for your scripts. 

For more information, see [Configure a new job with advanced scheduling](https://docs.cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling).

## September 05, 2025

Change

**Advanced filtering in alerts and search results**

You can now filter alerts and search results by any field in the detection object. This update provides more granular control over your queries, letting you filter by nested fields from events and entities within a detection.

## September 04, 2025

Change

**Improved Okta and Symantec Endpoint Protection parsers**

These changes are currently in Preview.

The Okta and Symantec Endpoint Protection parsers are now more efficient, with increased log-field coverage and more-accurate log-field mappings. These changes include new UDM fields and updated field mappings. We advise you to opt-in and get these new versions.

  * For details on the Okta parser, see [UDM mapping table](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta#udm_mapping_table) and [UDM mapping delta reference](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta#udm_mapping_delta_reference). 

  * For details on the Symantec Endpoint Protection parser, see [Collect Symantec Endpoint Protection logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-endpoint-protection#udm_mapping_table) and [UDM mapping delta reference](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-endpoint-protection#udm-mapping-delta).




Change

**Time zone override for forwarder logs**

Google SecOps now lets you override the default time zone for your logs when you create or configure a forwarder. 

For details, see [Add collector configuration](https://docs.cloud.google.com/chronicle/docs/install/forwarder-management-configurations#add-collectors).

Announcement

**CBN alerts functionality removed from all prebuilt parsers**

As part of deprecating the Configuration Based Normalization (CBN) alerts functionality, all [prebuilt parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates#types_of_parsers) that included the CBN alerts functionality were updated, and the functionality was removed. 

**Note:** For information about how you can migrate CBN alerts to YARA-L detection alerts, see [Migrate CBN alerts to YARA-L detection rule alerts](https://docs.cloud.google.com/chronicle/docs/detection/migrate-cbn-alerts).

## September 03, 2025

Change

**Extended match window for multi-event rules**

You can now configure rules to analyze data over a longer period. The maximum match window for these rules has been extended to 14 days. The run frequency for multi-event rules is automatically set based on the rule's match window:

  * For a window size of 1 to 48 hours, the run frequency is 1 hour.

  * For a window size greater than 48 hours, the run frequency is 24 hours.




## August 29, 2025

Change

**MITRE ATT &CK coverage dashboard is now available**

**This feature is currently in Preview.**

The new [MITRE ATT&CK coverage dashboard](https://docs.cloud.google.com/chronicle/docs/detection/mitre-dashboard) lets you measure your security posture against the MITRE ATT&CK framework, helping you:

  * Assess threat coverage
  * Identify gaps
  * Prioritize security efforts



## August 28, 2025

Change

**Composite detections for MITRE ATT &CK**

The [Curated Detections](https://docs.cloud.google.com/chronicle/docs/detection/use-curated-detections) feature has been enhanced with new [composite rules](https://docs.cloud.google.com/chronicle/docs/detection/composite-rules-category) that define chains of MITRE ATT&CK tactics and techniques.

These powerful new rule packs are now in public preview for customers with a [Google SecOps Enterprise or Enterprise Plus license](https://cloud.google.com/security/products/security-operations).

To learn more, a companion blog post will be published on the [Google Security Cloud Community](https://security.googlecloudcommunity.com/) on September 9, 2025.

## August 27, 2025

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

  * A10 Load Balancer (`A10_LOAD_BALANCER`)
  * AIX system (`AIX_SYSTEM`)
  * Apache (`APACHE`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * Aruba Switch (`ARUBA_SWITCH`)
  * Aruba (`ARUBA_WIRELESS`)
  * Attivo Networks (`ATTIVO`)
  * Auth0 (`AUTH_ZERO`)
  * Amazon VPC Transit Gateway Flow Logs (`AWS_VPC_TRANSIT_GATEWAY`)
  * AWS WAF (`AWS_WAF`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Organizational Context (`AZURE_AD_CONTEXT`)
  * Azure Firewall (`AZURE_FIREWALL`)
  * Azure Front Door (`AZURE_FRONT_DOOR`)
  * Carbon Black App Control (`CB_APP_CONTROL`)
  * None (`CHROME_MANAGEMENT`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco DNA Center Platform (`CISCO_DNAC`)
  * Cisco Email Security (`CISCO_EMAIL_SECURITY`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco IronPort (`CISCO_IRONPORT`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Router (`CISCO_ROUTER`)
  * Cisco vManage SD-WAN (`CISCO_SDWAN`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco Umbrella Audit (`CISCO_UMBRELLA_AUDIT`)
  * Cisco VCS Expressway (`CISCO_VCS`)
  * Cisco WSA (`CISCO_WSA`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Claroty Xdome (`CLAROTY_XDOME`)
  * HP Aruba (ClearPass) (`CLEARPASS`)
  * Cloudflare (`CLOUDFLARE`)
  * Cloudflare WAF (`CLOUDFLARE_WAF`)
  * Corelight (`CORELIGHT`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * CrowdStrike Alerts API (`CS_ALERTS`)
  * CrowdStrike Detection Monitoring (`CS_DETECTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CrowdStrike Falcon Stream (`CS_STREAM`)
  * Cyberark Privilege Cloud (`CYBERARK_PRIVILEGE_CLOUD`)
  * Darktrace (`DARKTRACE`)
  * Datadog (`DATADOG`)
  * Elastic Defend (`ELASTIC_DEFEND`)
  * F5 ASM (`F5_ASM`)
  * F5 Distributed Cloud Services (`F5_DCS`)
  * F5 Silverline (`F5_SILVERLINE`)
  * Fidelis Network (`FIDELIS_NETWORK`)
  * FireEye (`FIREEYE_ALERT`)
  * FireEye NX (`FIREEYE_NX`)
  * Forcepoint DLP (`FORCEPOINT_DLP`)
  * ForgeRock Identity Cloud (`FORGEROCK_IDENTITY_CLOUD`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Cloud SQL (`GCP_CLOUDSQL`)
  * Google Cloud DNS Threat Detector (`GCP_DNS_ATD`)
  * Cloud Load Balancing (`GCP_LOADBALANCING`)
  * None (`GCP_SECURITYCENTER_THREAT`)
  * VPC Flow Logs (`GCP_VPC_FLOW`)
  * AWS GuardDuty (`GUARDDUTY`)
  * IBM-i Operating System (`IBM_I`)
  * Imperva (`IMPERVA_WAF`)
  * Infoblox DHCP (`INFOBLOX_DHCP`)
  * Jamf Protect Telemetry V2 (`JAMF_TELEMETRY_V2`)
  * Kemp Load Balancer (`KEMP_LOADBALANCER`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * ManageEngine AD360 (`MANAGE_ENGINE_AD360`)
  * McAfee ePolicy Orchestrator (`MCAFEE_EPO`)
  * McAfee IPS (`MCAFEE_IPS`)
  * Medigate IoT (`MEDIGATE_IOT`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft Sentinel (`MICROSOFT_SENTINEL`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * Mikrotik Router (`MIKROTIK_ROUTER`)
  * Netskope V2 (`NETSKOPE_ALERT_V2`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * Unix system (`NIX_SYSTEM`)
  * Oracle Cloud Infrastructure VCN Flow Logs (`OCI_FLOW`)
  * Office 365 (`OFFICE_365`)
  * Office 365 Message Trace (`OFFICE_365_MESSAGETRACE`)
  * Okta (`OKTA`)
  * Okta Scaleft (`OKTA_SCALEFT`)
  * Oracle (`ORACLE_DB`)
  * Orca Cloud Security Platform (`ORCA`)
  * Proofpoint Threat Response (`PROOFPOINT_TRAP`)
  * Quest Active Directory (`QUEST_AD`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * Red Hat OpenShift (`REDHAT_OPENSHIFT`)
  * Symantec Endpoint Protection (`SEP`)
  * Silverfort Authentication Platform (`SILVERFORT`)
  * Squid Web Proxy (`SQUID_WEBPROXY`)
  * STIX Threat Intelligence (`STIX`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Sysdig (`SYSDIG`)
  * Tenable Security Center (`TENABLE_SC`)
  * Trend Micro (`TIPPING_POINT`)
  * Trellix HX Event Streamer (`TRELLIX_HX_ES`)
  * Trend Micro Apex one (`TRENDMICRO_APEX_ONE`)
  * Trend Micro Vision One Activity (`TRENDMICRO_VISION_ONE_ACTIVITY`)
  * Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
  * Trend Micro Vision One Workbench (`TRENDMICRO_VISION_ONE_WORKBENCH`)
  * Ubiquiti UniFi Switch (`UBIQUITI_SWITCH`)
  * Cisco Umbrella DNS (`UMBRELLA_DNS`)
  * Cisco Umbrella IP (`UMBRELLA_IP`)
  * Varonis (`VARONIS`)
  * Vectra XDR (`VECTRA_XDR`)
  * VMware vCenter (`VMWARE_VCENTER`)
  * VMware vRealize Suite (VMware Aria) (`VMWARE_VREALIZE`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Zscaler CASB (`ZSCALER_CASB`)
  * ZScaler Deception (`ZSCALER_DECEPTION`)
  * Zscaler DLP (`ZSCALER_DLP`)
  * ZScaler DNS (`ZSCALER_DNS`)
  * ZScaler NGFW (`ZSCALER_FIREWALL`)
  * Zscaler Internet Access Audit Logs (`ZSCALER_INTERNET_ACCESS`)
  * Zscaler Tunnel (`ZSCALER_TUNNEL`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * Zscaler Secure Private Access Audit Logs (`ZSCALER_ZPA_AUDIT`)
  * Zscaler Private Access (`ZSCALER_ZPA`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

  * Alicloud ApsaraDB (`ALICLOUD_APSARADB`)
  * AliCloud Firewall (`ALICLOUD_FIREWALL`)
  * AuthMind (`AUTHMIND`)
  * Microsoft Entra Recommendations (`MS_ENTRA_RECOMMENDATIONS`)
  * Palo Alto Networks Prisma Access (`PAN_PRISMA_ACCESS`)
  * Trellix Malware Analysis (`TRELLIX_AX`)
  * Everfox ULTRA (`ULTRA`)
  * ZScaler NSS VM (`ZSCALER_NSS_VM`)



## August 21, 2025

Feature

[Enhanced curated detections](https://docs.cloud.google.com/chronicle/docs/detection/use-curated-detections) has been enhanced with composite detection content for Mandiant Hunt Cloud Classification, including AWS, GCP, and Azure. This rule pack is available for Mandiant Threat Defense (MTD) customers with a Google Security Operations Enterprise or Enterprise Plus license.

## August 20, 2025

Change

**New rules added to rule pack**

Curated Detections has been enhanced with additional Chrome Enterprise Premium Browser Threat detections. The following rules have been added to the rule pack:

  * Dangerous Download with Matching Hashes by multiple users in Chrome Management

  * GTI High Severity File Download Event in Chrome Management

  * GTI Medium Severity File Download Event in Chrome Management

  * GTI Low Severity File Download Event in Chrome Management

  * Safe-browsing High Severity File Download Event in Chrome Management

  * Multiple Dangerous Download Events by same user in Chrome Management

  * Url Event to Newly Created Domain in Chrome Management




Feature

**Composite detections are now generally available**

The [composite detections](https://docs.cloud.google.com/chronicle/docs/secops/release-notes#April_23_2025) feature is now in General Availability. Composite detections lets you link multiple YARA-L rules to detect complex, multistage threats. This capability enhances detection by correlating alerts that individual rules might not detect.

For more information, see [Overview of composite detections](https://docs.cloud.google.com/chronicle/docs/detection/composite-detections).

## August 19, 2025

Announcement

**Reference lists retiring**

The reference list functionality is being phased out of the Google SecOps platform.

  * **October 2025** : You'll no longer be able to create new reference lists. Instead, use data tables to provide expanded functionality.

  * **Migration period** : All existing reference lists will be automatically migrated to data tables. During this migration period, you can continue to use your existing reference lists without changes.

  * **September 2026** : The legacy reference list functionality will be fully retired from the platform. After that date, all data will be available only through the data table interface.




## August 13, 2025

Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

  * [Collect Anomali ThreatStream IOC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/anomali-threatstream-ioc)
  * [Collect Cisco Application Control Engine (ACE)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ace)
  * [Collect Cisco Firepower NGFW logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-firepower-firewall)
  * [Collect Cisco Firewall Service Module (FWSM)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-fwsm)
  * [Collect Cisco IronPort logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ironport)
  * [Collect Cisco PIX logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-pix-firewall)
  * [Collect Cisco Prime logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-prime)
  * [Collect Cisco Wireless Intrusion Prevention System (WIPS) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wips)
  * [Collect Cisco Wireless LAN Controller (WLC) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless)
  * [Collect Cisco Wireless Security Management (WiSM) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsm)
  * [Collect Cloudian HyperStore logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudian-hs)
  * [Collect CrushFTP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crushftp)
  * [Collect Delinea Distributed Engine logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-de)
  * [Collect Duo User context logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-user)
  * [Collect ExtraHop DNS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extrahop-dns)
  * [Collect ExtraHop RevealX logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extrahop-revealx)
  * [Collect Extreme Networks switch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extreme-switch)
  * [Collect Extreme Networks Wireless logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extreme-wireless)
  * [Collect MuleSoft Anypoint logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mulesoft-anypoint)
  * [Collect Palo Alto Prisma SD-WAN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-sd-wan)
  * [Collect Recorded Future IOC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/recorded-future-ioc)
  * [Collect Veeam logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veeam)
  * [Collect Veridium ID logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veridium-id)
  * [Collect VMware Tanzu logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-tanzu)
  * [Collect VMware vCenter logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vcenter)
  * [Collect VMware vRealize logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vrealize)
  * [Collect VMware vSphere logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vsphere)
  * [Collect VSFTPD logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vsftpd)
  * [Collect VyOS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vyos)
  * [Collect Workday audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday-audit)
  * [Collect Yamaha router logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/yamaha-router)



## August 12, 2025

Change

**Data RBAC self-service enablement**

Data RBAC now includes a self-service option for direct enablement. This makes the initial onboarding process faster and simpler. For details, see [Configure data RBAC for users](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users).

## August 10, 2025

Announcement

**New permissions for Content Hub**

To access all modules in the Content Hub, you must set the correct IAM role permissions.

For full details, see [Google SecOps Content Hub overview](https://docs.cloud.google.com/chronicle/docs/secops/content_hub).

Feature

**Updated permissions for accessing product-centric feeds**

If you have assigned **Custom IAM Roles** , you can now grant access to the product-centric feeds by adding the following permissions to the role:

  * `chronicle.feedPacks.get`
  * `chronicle.feedPacks.list`



To learn more about how to configure feeds using the product-centric feeds UI, see [Configure feeds by product.](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds)

Feature

**Expression Builder enhancements**

The **Expression Builder** has been enhanced with a new set of pre-built filters to help streamline query creation. 

We've improved the information within the platform for all filters, both new and existing. The supporting documentation provides clearer descriptions and practical examples for each transformer, making it easier to understand their purpose and syntax.

For details, see [Use the Expression Builder](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-expression-builder).

Feature

**Remote agent notifications**

Agent notifications will alert you to new remote agent version releases and agent downtime based on your permissions and associated environments. Agent notifications are now enabled by default. You can opt out of these notifications at any time from your user preferences.

For details, see [Agent notifications](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/what-is-a-remote-agent#agent-notifications).

## August 08, 2025

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

  * 1Password (`ONEPASSWORD`)
  * A10 Load Balancer (`A10_LOAD_BALANCER`)
  * AIX system (`AIX_SYSTEM`)
  * Akamai Enterprise Application Access (`AKAMAI_EAA`)
  * Akamai WAF (`AKAMAI_WAF`)
  * Apache (`APACHE`)
  * Aqua Security (`AQUA_SECURITY`)
  * Aruba (`ARUBA_WIRELESS`)
  * Attivo Networks (`ATTIVO`)
  * Auth0 (`AUTH_ZERO`)
  * AWS Config (`AWS_CONFIG`)
  * AWS GuardDuty (`GUARDDUTY`)
  * AWS Lambda Function (`AWS_LAMBDA_FUNCTION`)
  * AWS RDS (`AWS_RDS`)
  * AWS VPC Flow (`AWS_VPC_FLOW`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure AD Sign-In (`AZURE_AD_SIGNIN`)
  * Azure Key Vault logging (`AZURE_KEYVAULT_AUDIT`)
  * Azure VNET Flow (`AZURE_VNET_FLOW`)
  * Barracuda Email (`BARRACUDA_EMAIL`)
  * Barracuda WAF (`BARRACUDA_WAF`)
  * BeyondTrust BeyondInsight (`BEYONDTRUST_BEYONDINSIGHT`)
  * Bitdefender (`BITDEFENDER`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Check Point Sandblast (`CHECKPOINT_EDR`)
  * Chrome Management (`N/A`)
  * Cisco Email Security (`CISCO_EMAIL_SECURITY`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco IronPort (`CISCO_IRONPORT`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Meraki (`CISCO_MERAKI`)
  * Cisco NX-OS (`CISCO_NX_OS`)
  * Cisco Router (`CISCO_ROUTER`)
  * Cisco Stealthwatch (`CISCO_STEALTHWATCH`)
  * Cisco Umbrella SWG DLP (`CISCO_UMBRELLA_SWG_DLP`)
  * Cisco vManage SD-WAN (`CISCO_SDWAN`)
  * Cisco WLC/WCS (`CISCO_WIRELESS`)
  * Cisco WSA (`CISCO_WSA`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Cloud Audit Logs (`N/A`)
  * Cloud DNS (`N/A`)
  * Cloud Load Balancing (`GCP_LOADBALANCING`)
  * Cloudflare (`CLOUDFLARE`)
  * Corelight (`CORELIGHT`)
  * CrowdStrike Alerts API (`CS_ALERTS`)
  * CrowdStrike Detection Monitoring (`CS_DETECTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CrowdStrike Falcon Stream (`CS_STREAM`)
  * CSV Custom IOC (`CSV_CUSTOM_IOC`)
  * CyberArk (`CYBERARK`)
  * Cybereason EDR (`CYBEREASON_EDR`)
  * Darktrace (`DARKTRACE`)
  * EfficientIP DDI (`EFFICIENTIP_DDI`)
  * Elastic Defend (`ELASTIC_DEFEND`)
  * EPIC Systems (`EPIC`)
  * ExtraHop RevealX (`EXTRAHOP`)
  * F5 Advanced Firewall Management (`F5_AFM`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP Access Policy Manager (`F5_BIGIP_APM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * F5 DNS (`F5_DNS`)
  * F5 Silverline (`F5_SILVERLINE`)
  * Fidelis Network (`FIDELIS_NETWORK`)
  * FireEye ETP (`FIREEYE_ETP`)
  * ForgeRock Identity Cloud (`FORGEROCK_IDENTITY_CLOUD`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortinet Proxy (`FORTINET_WEBPROXY`)
  * Fortinet Web Application Firewall (`FORTINET_FORTIWEB`)
  * GitHub (`GITHUB`)
  * Halcyon Anti Ransomware (`HALCYON`)
  * HAProxy (`HAPROXY`)
  * HP Aruba (ClearPass) (`CLEARPASS`)
  * IBM DataPower Gateway (`IBM_DATAPOWER`)
  * Imperva (`IMPERVA_WAF`)
  * Imperva SecureSphere Management (`IMPERVA_SECURESPHERE`)
  * Infoblox DHCP (`INFOBLOX_DHCP`)
  * Jamf pro context (`JAMF_PRO_CONTEXT`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * Lacework Cloud Security (`LACEWORK`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * Linux Sysmon (`LINUX_SYSMON`)
  * McAfee IPS (`MCAFEE_IPS`)
  * Menlo Security (`MENLO_SECURITY`)
  * Microsoft AD (`WINDOWS_AD`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft Defender for Identity (`MICROSOFT_DEFENDER_IDENTITY`)
  * Microsoft IIS (`IIS`)
  * Mimecast (`MIMECAST_MAIL`)
  * Mimecast Mail V2 (`MIMECAST_MAIL_V2`)
  * MISP Threat Intelligence (`MISP_IOC`)
  * NetApp ONTAP (`NETAPP_ONTAP`)
  * Netskope V2 (`NETSKOPE_ALERT_V2`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * NGINX (`NGINX`)
  * One Identity Identity Manager (`ONE_IDENTITY_IDENTITY_MANAGER`)
  * Opnsense (`OPNSENSE`)
  * Orca Cloud Security Platform (`ORCA`)
  * Palo Alto Cortex XDR Events (`PAN_CORTEX_XDR_EVENTS`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Palo Alto Prisma Access (`PAN_CASB`)
  * pfSense (`PFSENSE`)
  * Ping Federate (`PING_FEDERATE`)
  * Proofpoint Observeit (`OBSERVEIT`)
  * Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Qualys VM (`QUALYS_VM`)
  * Remediant SecureONE (`REMEDIANT_SECUREONE`)
  * SAP SM20 (`SAP_SM20`)
  * SecureAuth (`SECUREAUTH_SSO`)
  * SentinelOne EDR (`SENTINEL_EDR`)
  * Silverfort Authentication Platform (`SILVERFORT`)
  * Sophos Central (`SOPHOS_CENTRAL`)
  * Sophos UTM (`SOPHOS_UTM`)
  * Squid Web Proxy (`SQUID_WEBPROXY`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Symantec Web Security Service (`SYMANTEC_WSS`)
  * Tenable Active Directory Security (`TENABLE_ADS`)
  * Tenable Security Center (`TENABLE_SC`)
  * Thinkst Canary (`THINKST_CANARY`)
  * Trellix HX Event Streamer (`TRELLIX_HX_ES`)
  * Trend Micro Apex one (`TRENDMICRO_APEX_ONE`)
  * Trend Micro Cloud one (`TRENDMICRO_CLOUDONE`)
  * Trend Micro Vision One Activity (`TRENDMICRO_VISION_ONE_ACTIVITY`)
  * Trend Micro Vision One Observerd Attack Techniques (`TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES`)
  * Trend Micro Vision One Workbench (`TRENDMICRO_VISION_ONE_WORKBENCH`)
  * Tripwire (`TRIPWIRE_FIM`)
  * Unix system (`NIX_SYSTEM`)
  * VMware Horizon (`VMWARE_HORIZON`)
  * VMware vCenter (`VMWARE_VCENTER`)
  * VMware vRealize Suite (VMware Aria) (`VMWARE_VREALIZE`)
  * WatchGuard (`WATCHGUARD`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Workday Audit Logs (`WORKDAY_AUDIT`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * Workspace Users (`WORKSPACE_USERS`)
  * ZScaler Deception (`ZSCALER_DECEPTION`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

  * Akamai MFA (`AKAMAI_MFA`)
  * Azure Org Context (`AZURE_ORG_CONTEXT`)
  * Cisco Remote Access VPN (`CISCO_RAVPN`)
  * CoreView Audit-log SIEM integration (`COREVIEW`)
  * Fortinet Network Detection and Response (`FORTINET_FORTINDR`)
  * GCP Security Command Center Chokepoint (`GCP_SECURITYCENTER_CHOKEPOINT`)
  * Imperva Cloud WAF (`IMPERVA_CLOUD_WAF`)
  * Lumu Universal SIEM (`LUMU`)
  * Microsoft Azure Databricks (`MICROSOFT_DATABRICKS_WORKSPACES`)
  * Microsoft Insights/Components (`MICROSOFT_INSIGHTS_COMPONENTS`)
  * Microsoft ServiceBus/Namespaces (`MICROSOFT_SERVICEBUS_NAMESPACES`)
  * Microsoft Azure SQL Managed Instances (`MICROSOFT_SQL_MANAGED_INSTANCES`)
  * Moveworks (`MOVEWORKS`)
  * Network Box Unified Threat Management+ (`NETWORKBOX_UTM`)
  * Oracle Cloud Infrastructure Identity Cloud Service (`OCI_IDENTITY_CLOUD_SERVICE`)
  * SAP Commerce Cloud (`SAP_HAC`)
  * Sonatype Lifecycle (`SONATYPE_LIFECYCLE`)
  * TeamViewer Tensor (`TEAMVIEWER_TENSOR`)
  * Torq Audit Logs (`TORQ_AUDIT_LOGS`)
  * Velociraptor - digital forensic & incident response tool (`VELOCIRAPTOR`)
  * Zoom Activity Logs (`ZOOM_ACTIVITY`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## August 05, 2025

Feature

**New YARA-L features**

The following capabilities have been added to YARA-L 2.0 to enhance search precision, data analysis, and investigative workflows:

  * [**Conditions in UDM search and dashboards**](https://docs.cloud.google.com/chronicle/docs/investigation/yara-l-2-0-conditions)

You can now filter aggregates defined in the `outcome` section using the new `condition` clause. This gives you more precise control over your results and supports more targeted investigations.

    * New functionality includes support for `OR` and `n` of `[a, b, c.. z]` expressions.

    * General availability for search and dashboards.

  * [**Deduplicate events in searches and dashboards**](https://docs.cloud.google.com/chronicle/docs/investigation/deduplication-yaral)

The new `dedup` section lets you remove duplicate events after the `match` clause in both standard UDM searches and YARA-L 2.0 queries.

General availability for search and dashboards.

  * [**Use metrics functions in UDM searches**](https://docs.cloud.google.com/chronicle/docs/investigation/yara-l-2-0-metrics-search)

You can now apply `metrics` functions in the `outcome` section of your search to access aggregated historical data directly in your search queries. 

    * Uses the same syntax as `metrics` in rules.
    * General availability for search.
  * [**Increased limits for array and array_distinct**](https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-syntax#aggregations)

The element limit for `array` and `array_distinct` aggregation functions in YARA-L has increased from 25 to 1,000.

    * General availability for search.
  * **Restrict search results using limit**

The `limit` keyword now lets you restrict the number of results returned by a search. Use this to quickly preview data, optimize performance, or focus on a subset of results.

General availability for search and dashboards.

  * [**`earliest`**](https://docs.cloud.google.com/chronicle/docs/investigation/statistics-aggregations-in-udm-search#earliest) and [**`latest`**](https://docs.cloud.google.com/chronicle/docs/investigation/statistics-aggregations-in-udm-search#latest) **timestamps**

New `earliest` and `latest` timestamps let you extract the time range of your data (within microseconds) during aggregation.

General availability for search.

  * **Layer aggregations and analytics across multi-stage queries**

Recent updates to multi-stage queries let you:

    * Layer aggregations and data statistical functions. Calculate baselines, deviations, and trends across multiple stages of data processing.

    * Conduct joins both within and across stages.

Private preview for search and dashboards. Contact your Google SecOps representative to enroll.

  * **Join events, the entity graph, and data tables**

You can now perform Inner joins between events, the entity graph, and data tables. These queries require a `match` clause for these joins and return results as statistics.

Private preview for search and dashboards. Contact your Google SecOps representative to enroll.




## August 04, 2025

Change

**New rules added to rule pack**

Curated detections has been enhanced with additional Chrome Enterprise Premium Browser Threat detections. The following rules have been added to the rule pack:

Malware Transfer Event in Chrome Management

Password Breach Event By Admin User

Phishing Navigation Event Containing Suspicious Parameters In Chrome Management

Chrome Password Event on Newly Observed Domain in Environment

Feature

[Auto Extraction](https://docs.cloud.google.com/chronicle/docs/event-processing/auto-extraction) supports XML formatted logs in addition to JSON formatted logs. This enhancement will be available starting this week.

## August 03, 2025

Feature

**Custom Fields Form widget is now supported in Playbook View**

The **Custom Fields Form** widget is now supported in Playbook View.

Feature

**Automated retries for failed playbook actions**

This feature is in Preview.

Playbook functionality now supports automatic retries for individual actions that encounter temporary issues, such as network outages, API rate limits, or service unavailability. You can define the number of retry attempts and the intervals between retries directly at the step level within playbooks.

For more information on configuring and using action retries, see [Configure action retries in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/retry-actions).

## July 27, 2025

Feature

**Playbook Simulator enhancements for loops**

The Playbook Simulator now supports visualization and debugging of playbooks that contain loops. This lets you clearly see and navigate through each loop iteration within the simulator viewer. 

Additionally, the step display order has been updated to show actions from top to bottom (oldest at the top, newest at the bottom), with automatic scrolling to the most recent activity. 

For more details, see [Loops in the Playbook Simulator](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-loops#loops-in-the-playbook-simulator).

Feature

**Automate tasks with Playbook Loops**

This feature is in Preview.

Playbook functionality has been enhanced to include **Playbook Loops**. This feature update lets playbooks iterate over lists or entities, performing one or more actions for each item. It streamlines automation by eliminating the need for duplicated steps or custom actions when processing multiple items. You can configure Playbook Loops directly within a playbook or inside a playbook block. 

For setup instructions and use case examples , see [Automate tasks with Playbook Loops](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-loops).

## July 22, 2025

Feature

**Silent Host Monitoring**

New configuration options are now available for Silent Host Monitoring. You can now define detection rule-based Silent Host Monitoring in SecOps using UDM fields or labels, configurable within a specified time window. 

For more information, see [Silent host monitoring](https://docs.cloud.google.com/chronicle/docs/ingestion/silent-host-monitoring).

## July 21, 2025

Feature

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

[Collect Apache Tomcat logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tomcat)

[Collect Appian Cloud logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/appian-cloud)

[Collect Archer IRM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/archer-irm)

[Collect ArcSight CEF logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arcsight-cef)

[Collect Area 1 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/area1)

[Collect Aruba EdgeConnect SD-WAN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba)

[Collect Atlassian Cloud Admin Audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-audit)

[Collect Avatier logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/avatier)

[Collect Avigilon Access Control Manager logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/avigilon-access-logs)

[Collect AWS CloudTrail logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-aws-logs-into-chronicle)

[Collect Barracuda CloudGen Firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-cloudgen-firewall)

[Collect Barracuda Web Filter logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-webfilter)

[Collect Broadcom CA PAM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ca-pam)

[Collect Broadcom SSL VA logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ssl-va)

[Collect Cato Networks logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cato-networks)

[Collect Check Point Harmony logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-harmony)

[Collect CipherTrust Manager logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ciphertrust-manager)

[Collect Cisco VCS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-vcs)

[Collect Cisco VPN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-vpn)

[Collect Cisco WSA logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsa)

[Collect CyberArk Privilege Cloud logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-privilege-cloud)

[Collect Digi Modems logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digi-modems)

[Collect F5 DNS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/F5-dns)

[Collect F5 VPN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/F5-vpn)

[Collect Forcepoint CASB logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-casb)

[Collect HPE BladeSystem c7000 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hpe-bladesystem-c7000)

[Collect Skyhigh Security logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/skyhigh-security)

[Collect Trellix IPS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-ips)

## July 07, 2025

Feature

**Dashboards for enhanced visualizations and threat hunting**

You can now use the Google SecOps Dashboards to enhance data visualization, investigations, and threat hunting.

Key capabilities include:

  * SOAR data availability
  * Downloadable reports
  * Custom drilldowns
  * Markdown widgets
  * 51 curated dashboards covering a broad range of security categories and use cases.



For more information, see [Dashboards](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards).

## July 05, 2025

Feature

**Share Case Queue Filters**

You can now share case queue filters with other users. These filters can be saved with specific criteria, such as assignee roles, and shared with individual users, SOC roles, or all users in your organization for quick access.

For more information, see [Apply and save filters](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/apply-and-save-filters).

## July 02, 2025

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

  * 1Password (`ONEPASSWORD`)
  * Apache (`APACHE`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * Aruba Switch (`ARUBA_SWITCH`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS CloudWatch (`AWS_CLOUDWATCH`)
  * AWS GuardDuty (`GUARDDUTY`)
  * AWS Lambda Function (`AWS_LAMBDA_FUNCTION`)
  * AWS S3 Server Access (`AWS_S3_SERVER_ACCESS`)
  * AWS VPC Flow (`AWS_VPC_FLOW`)
  * AWS VPC Flow (CSV) (`AWS_VPC_FLOW_CSV`)
  * Azure AD (`AZURE_AD`)
  * Azure Application Gateway (`AZURE_GATEWAY`)
  * Azure Firewall (`AZURE_FIREWALL`)
  * Azure Storage Audit (`AZURE_STORAGE_AUDIT`)
  * Azure VNET Flow (`AZURE_VNET_FLOW`)
  * BIND (`BIND_DNS`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Brocade Switch (`BROCADE_SWITCH`)
  * Carbon Black (`CB_EDR`)
  * Carbon Black App Control (`CB_APP_CONTROL`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Chronicle SOAR Audit (`CHRONICLE_SOAR_AUDIT`)
  * Cisco Application Centric Infrastructure (`CISCO_ACI`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Email Security (`CISCO_EMAIL_SECURITY`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco IronPort (`CISCO_IRONPORT`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco NX-OS (`CISCO_NX_OS`)
  * Cisco Router (`CISCO_ROUTER`)
  * Cisco Umbrella Web Proxy (`UMBRELLA_WEBPROXY`)
  * Cisco vManage SD-WAN (`CISCO_SDWAN`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Claroty Continuous Threat Detection (`CLAROTY_CTD`)
  * Cloudflare (`CLOUDFLARE`)
  * CrowdStrike Detection Monitoring (`CS_DETECTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * Crowdstrike IOC (`CROWDSTRIKE_IOC`)
  * Custom Security Data Analytics (`CUSTOM_SECURITY_DATA_ANALYTICS`)
  * CyberArk Endpoint Privilege Manager (EPM) (`CYBERARK_EPM`)
  * Cyberark Privilege Cloud (`CYBERARK_PRIVILEGE_CLOUD`)
  * Darktrace (`DARKTRACE`)
  * Datadog (`DATADOG`)
  * Dell Switch (`DELL_SWITCH`)
  * Elastic Defend (`ELASTIC_DEFEND`)
  * ESET AV (`ESET_AV`)
  * ExtraHop RevealX (`EXTRAHOP`)
  * F5 Advanced Firewall Management (`F5_AFM`)
  * F5 ASM (`F5_ASM`)
  * FireEye ETP (`FIREEYE_ETP`)
  * FireEye NX (`FIREEYE_NX`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortinet Web Application Firewall (`FORTINET_FORTIWEB`)
  * GitHub (`GITHUB`)
  * Guardicore Centra (`GUARDICORE_CENTRA`)
  * H3C Comware Platform Switch (`H3C_SWITCH`)
  * IBM Cloud Activity Tracker (`IBM_CLOUD_ACTIVITY_TRACKER`)
  * IBM Security Verify Access (`IBM_SVA`)
  * IBM zSecure Alert (`IBM_ZSECURE_ALERT`)
  * Imperva (`IMPERVA_WAF`)
  * Infoblox (`INFOBLOX`)
  * Infoblox DHCP (`INFOBLOX_DHCP`)
  * KnowBe4 PhishER (`KNOWBE4_PHISHER`)
  * LastPass Password Management (`LASTPASS`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * Microsoft AD (`WINDOWS_AD`)
  * Microsoft AD FS (`ADFS`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft IIS (`IIS`)
  * Netskope V2 (`NETSKOPE_ALERT_V2`)
  * NGINX (`NGINX`)
  * Nozomi Networks Scada Guardian (`NOZOMI_GUARDIAN`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * Openpath (`OPENPATH`)
  * Opnsense (`OPNSENSE`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * Palo Alto Cortex XDR Events (`PAN_CORTEX_XDR_EVENTS`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Palo Alto Prisma Access (`PAN_CASB`)
  * Ping Federate (`PING_FEDERATE`)
  * Ping Identity (`PING`)
  * PostgreSQL (`POSTGRESQL`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Proofpoint Threat Response (`PROOFPOINT_TRAP`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * Red Hat OpenShift (`REDHAT_OPENSHIFT`)
  * Remediant SecureONE (`REMEDIANT_SECUREONE`)
  * Riverbed Steelhead (`STEELHEAD`)
  * SailPoint IAM (`SAILPOINT_IAM`)
  * Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
  * Security Command Center Threat (`N/A`)
  * Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Sysdig (`SYSDIG`)
  * Teradata DB (`TERADATA_DB`)
  * Terraform Enterprise Audit (`TERRAFORM_ENTERPRISE`)
  * Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
  * Tripwire (`TRIPWIRE_FIM`)
  * Vectra Detect (`VECTRA_DETECT`)
  * Vectra Stream (`VECTRA_STREAM`)
  * Versa Firewall (`VERSA_FIREWALL`)
  * VMware AirWatch (`AIRWATCH`)
  * VMware ESXi (`VMWARE_ESX`)
  * Voltage (`VOLTAGE`)
  * WatchGuard (`WATCHGUARD`)
  * Windows DHCP (`WINDOWS_DHCP`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Windows Hyper-V (`WINDOWS_HYPERV`)
  * wiz.io (`WIZ_IO`)
  * Workday (`WORKDAY`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * Zscaler CASB (`ZSCALER_CASB`)
  * ZScaler Deception (`ZSCALER_DECEPTION`)
  * Zscaler DLP (`ZSCALER_DLP`)
  * Zscaler Tunnel (`ZSCALER_TUNNEL`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

  * Akamai Kona Edge Grid (`AKAMAI_KONA_EDGE_GRID`)
  * Azure Compute (`AZURE_COMPUTE`)
  * Bluecat Micetro IP Address Management (`BLUECAT_MICETRO_IPAM`)
  * Cloudera Ranger (`CLOUDERA_RANGER`)
  * Cyberark Identity (`CYBERARK_IDENTITY`)
  * Fortinet FortiDLP (`FORTINET_FORTIDLP`)
  * IBM Cognos Analytics (`IBM_COGNOS`)
  * IBM Planning Analytics (`IBM_PA`)
  * Ironclad (`IRONCLAD`)
  * Ivanti Endpoint Manager Mobile (`IVANTI_ENDPOINT_MANAGER_MOBILE`)
  * Mimecast Mail V2 (`MIMECAST_MAIL_V2`)
  * Minsait Sigefi (`MINSAIT_SIGEFI`)
  * Netskope One Secure SD-WAN (`NETSKOPE_SDWAN`)
  * Proxmox (`PROXMOX`)
  * Radware Bot (`RADWARE_BOT`)
  * ScaleFusion for Windows MDM (`SCALEFUSION`)
  * Titan SFTP Server (`TITAN_SFTP`)
  * ZoomInfo (`ZOOMINFO`)
  * Zscaler Email DLP Insights (`ZSCALER_EMAIL_DLP_INSIGHTS`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## June 30, 2025

Change

[Data tables](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables) are multicolumn constructs that let you input your own data into Google SecOps. You can create or import data tables to your Google SecOps account using the Google SecOps UI, the Data Tables API, or by using YARA-L queries in rules. This feature is now available to all customers.

What's new for this release:

  * Multiple web interface enhancements have been made, including a new default table view for data table management.
  * Support for the `number` data type is now available for data table columns.
  * Support for repeated fields in data table columns.
  * The [Limitations](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables#limitations) section has additional details.



## June 23, 2025

Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

[Collect BeyondTrust BeyondInsight logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyond-trust-beyondinsight)

[Collect BloxOne Threat Defense logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bloxone)

[Collect BlueCat Edge DNS Resolver logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecat-edge)

[Collect Cambium Networks logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cambium-networks)

[Collect Check Point Audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-audit)

[Collect Check Point EDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-edr)

[Collect Check Point SmartDefense logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-smartdefense)

[Collect Commvault logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/commvault)

[Collect Comodo AV logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/comodo-av)

[Collect Cylance PROTECT logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cylance-protect)

[Collect Cyolo OT logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyolo-ot)

[Collect Delinea PAM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-pam)

[Collect Dell CyberSense logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-cybersense)

[Collect Dell EMC Data Domain logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-data-domain)

[Collect Dell EMC Isilon NAS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-isilon-nas)

[Collect Dell EMC PowerStore logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-powerstore)

[Collect Dell OpenManage logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-openmanage)

[Collect Endpoint Protector DLP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/endpoint-protector-dlp)

[Collect ESET AV logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-av)

[Collect ESET EDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-edr)

[Collect F5 AFM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/F5-afm)

[Collect F5 ASM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/F5-asm)

[Collect FileZilla FTP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/filezilla-ftp)

[Collect Forescout NAC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forescout-nac)

[Collect ForgeRock OpenAM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forgerock-openam)

[Collect HAProxy logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/haproxy)

[Collect Kaseya Datto File Protection logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kaseya-datto-file-protection)

[Collect ManageEngine AD360 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-ad360)

[Collect Palo Alto Cortex XDR Events logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cortex-xdr-events)

[Collect Snowflake logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snowflake)

[Collect Trellix DLP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-dlp)

[Collect Trellix ePO logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-epo)

[Collect Trend Micro DDI logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-ddi)

[Collect Trend Micro Email Security logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-security)

[Collect Trend Micro Vision One Activity logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-activity)

[Collect Trend Micro Vision One Audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-audit)

[Collect Trend Micro Vision One Container Vulnerability logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-container-vulnerability)

[Collect Trend Micro Vision One Detections logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-detections)

[Collect Trend Micro Vision One Observed Attack Techniques logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-observed-attack-techniques)

[Collect Trend Micro Vision One Workbench logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-workbench)

## June 19, 2025

Feature

**Content Hub**

This feature is currently in Preview.

The new Content Hub page offers a centralized experience for managing all your Google SecOps content needs. On this page, you can do the following: 

  * Onboard Google SecOps content using content packs for top data sources
  * View and manage native dashboards.
  * Access and configure search queries.
  * View, filter, and review curated detections rule logic.
  * Configure response integrations.
  * Install and run power ups.



For more information, see [Google SecOps Content Hub](https://docs.cloud.google.com/chronicle/docs/secops/content_hub).

Feature

**Product Centric Feed Management**

This feature is currently in Preview.

You can now configure multiple log-type feeds for the same product type on a single page. This new product-led experience simplifies the feed configuration flow and provides additional in-product guidance. For more information, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## June 18, 2025

Feature

You can now remove existing UDM field mappings by using parser extensions in Google SecOps.

For more information, see [Remove UDM field mappings using parser extensions](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions#remove_udm_field_mappings_using_parser_extensions) and [Code snippet - Remove existing mappings](https://docs.cloud.google.com/chronicle/docs/event-processing/parser-extension-examples#code_snippet_remove_existing_mappings)

Feature

New data ingestion and health dashboard widgets are now available. 

  * **Silent host monitoring** : displays hosts that were active in the last 7 days, but haven't reported recently, including a count of days since their last ingestion.
  * **BindPlane agent logging and health** : visualizes logging activity and agent health. Requires Bindplane agent logs to be ingested into Google SecOps.
  * **Throughput in bytes** : shows ingestion volume over time.
  * **Improved log type distribution charts** : updates charts for better readability and usability.



## June 16, 2025

Announcement

The Release Candidate period of the following premium parsers has been extended from the end of May to the week of July 21, 2025:

  * Crowdstrike Detection Monitoring (CS_DETECTS)
  * Crowdstrike Falcon (CS_EDR)
  * Microsoft Defender for Endpoint



We recommend that you opt-in early and make any necessary adjustments before these updates become the default.

## June 08, 2025

Feature

**Playbook Permissions: Support for API Key Roles**

The platform has been updated to extend playbook permissions to also support the SOC Roles associated with API keys, in addition to the user SOC Roles. 

This enhancement affects how integrations using API keys interact with playbooks that have specific permission configurations. For example, GitSync now uses this capability to synchronize playbooks with restricted permissions.

For more information on how playbook permissions work with users and API keys, see[ Playbook permissions](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-permissions). 

For specific instructions on configuring GitSync with restricted playbooks, see[ GitSync - Work with playbook permissions](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/gitsync#work-with-playbook-permissions).

Feature

**Advanced Reports: Case Custom Fields**

Advanced Reports (Looker) has been enhanced to include support for custom fields created for Cases.

This enhancement allows users to leverage organization-specific data captured in custom fields to gain deeper insights and create tailored visualizations within Looker reports. Specific LookML formulas and filtering guidance are now available.

For more information on how to use custom fields in Advanced Reports, see [Use Custom Fields in Advanced Reports](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/adding-custom-fields#use-custom-fields-in-advanced-reports).

## June 04, 2025

Announcement

The following parser documentation is now available:

[Collect Abnormal Security logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/abnormal-security)

[Collect Apache Cassandra logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/apache-cassandra)

[Collect Darktrace logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/darktrace)

[Collect Nix Systems Ubuntu Server (Unix System) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nix-systems-ubuntu)

[Collect 1Password logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword)

[Collect 1Password audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword-audit-events)

[Collect Symantec Endpoint Protection logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-endpoint-protection)

[Collect Symantec VIP Authentication Hub logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-vip-authhub)

[Collect Symantec VIP Enterprise Gateway logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-vip)

[Collect Symantec Web Isolation logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-web-isolation)

[Collect Varonis logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/varonis)

[Collect Oracle DB logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-db)

[Collect Akeyless Vault logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akeyless-vault)

[Collect Attivo Networks BOTsink logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/attivo)

[Collect Avaya Aura logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/avaya-aura)

[Collect BeyondTrust Endpoint Privilege Management logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-epm)

[Collect BeyondTrust Privileged Identity logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-pi)

[Collect Blue Coat ProxySG logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecoat-proxysg)

[Collect Microsoft Exchange logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-exchange)

[Collect MYSQL logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mysql)

[Collect Signal Sciences WAF logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/signal-sciences-waf)

[Collect Symantec CloudSOC CASB logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-cloudsoc-casb)

## June 03, 2025

Fixed

**User interface fixes**

There was an issue with highlighting regular expressions in **Search** and **Rules Editor**. Once you entered a regular expression, all subsequent text on the line would be highlighted as if it was also a regular expression (whether it was or wasn't). This issue has been fixed. Note that both string literals (specified with back ticks) and regular expressions are highlighted in the same color.

There was an issue with uppercase keywords in **Search** and **Rules Editor**. They weren't being highlighted correctly. This issue has been fixed.

## May 29, 2025

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have changed. Each parser is listed by product name and `log_type` value, if applicable. This list now includes both released default parsers and pending parser updates.

  * AIX system (`AIX_SYSTEM`)
  * Akamai WAF (`AKAMAI_WAF`)
  * Apache (`APACHE`)
  * Appian Cloud (`APPIAN_CLOUD`)
  * Auth0 (`AUTH_ZERO`)
  * AWS CloudFront (`AWS_CLOUDFRONT`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS GuardDuty (`GUARDDUTY`)
  * AWS Macie (`AWS_MACIE`)
  * AWS Session Manager (`AWS_SESSION_MANAGER`)
  * AWS VPC Flow (`AWS_VPC_FLOW`)
  * AWS VPC Flow (CSV) (`AWS_VPC_FLOW_CSV`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Organizational Context (`AZURE_AD_CONTEXT`)
  * Azure Firewall (`AZURE_FIREWALL`)
  * Azure Storage Audit (`AZURE_STORAGE_AUDIT`)
  * Barracuda Firewall (`BARRACUDA_FIREWALL`)
  * BeyondTrust BeyondInsight (`BEYONDTRUST_BEYONDINSIGHT`)
  * BIND (`BIND_DNS`)
  * Bitdefender (`BITDEFENDER`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Brocade Switch (`BROCADE_SWITCH`)
  * Carbon Black (`CB_EDR`)
  * CircleCI (`CIRCLECI`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco NX-OS (`CISCO_NX_OS`)
  * Cisco Prime (`CISCO_PRIME`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco Unity Connection (`CISCO_UNITY_CONNECTION`)
  * Cloud Audit Logs (`N/A`)
  * CrowdStrike Alerts API (`CS_ALERTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CyberArk Endpoint Privilege Manager (EPM) (`CYBERARK_EPM`)
  * CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
  * Cylance Protect (`CYLANCE_PROTECT`)
  * Darktrace (`DARKTRACE`)
  * Dell OpenManage (`DELL_OPENMANAGE`)
  * EfficientIP DDI (`EFFICIENTIP_DDI`)
  * Elastic Defend (`ELASTIC_DEFEND`)
  * Elastic Windows Event Log Beats (`ELASTIC_WINLOGBEAT`)
  * ExtraHop RevealX (`EXTRAHOP`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * F5 DNS (`F5_DNS`)
  * Fastly WAF (`FASTLY_WAF`)
  * FireEye HX (`FIREEYE_HX`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortinet FortiAuthenticator (`FORTINET_FORTIAUTHENTICATOR`)
  * Fortinet FortiNAC (`FORTINET_FORTINAC`)
  * Fortinet Web Application Firewall (`FORTINET_FORTIWEB`)
  * GitHub (`GITHUB`)
  * Gitlab (`GITLAB`)
  * HP Aruba (ClearPass) (`CLEARPASS`)
  * Ipswitch SFTP (`IPSWITCH_SFTP`)
  * Juniper (`JUNIPER_FIREWALL`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * ManageEngine ADManager Plus (`ADMANAGER_PLUS`)
  * McAfee ePolicy Orchestrator (`MCAFEE_EPO`)
  * Microsoft AD FS (`ADFS`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Defender for Identity (`MICROSOFT_DEFENDER_IDENTITY`)
  * Microsoft IIS (`IIS`)
  * Microsoft PowerShell (`POWERSHELL`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * Nokia Router (`NOKIA_ROUTER`)
  * Office 365 (`OFFICE_365`)
  * Oracle (`ORACLE_DB`)
  * Palo Alto Cortex XDR Events (`PAN_CORTEX_XDR_EVENTS`)
  * Palo Alto Prisma Access (`PAN_CASB`)
  * Ping Federate (`PING_FEDERATE`)
  * Ping Identity (`PING`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * ServiceNow Audit (`SERVICENOW_AUDIT`)
  * Snare System Diagnostic Logs (`SNARE_SOLUTIONS`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Symantec Security Analytics (`SYMANTEC_SA`)
  * Sysdig (`SYSDIG`)
  * Tanium Question (`TANIUM_QUESTION`)
  * Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
  * Trend Micro Vision One Workbench (`TRENDMICRO_VISION_ONE_WORKBENCH`)
  * TrendMicro Deep Discovery Inspector (`TRENDMICRO_DDI`)
  * VanDyke SFTP (`VANDYKE_SFTP`)
  * Vectra Detect (`VECTRA_DETECT`)
  * Vectra Stream (`VECTRA_STREAM`)
  * Vectra XDR (`VECTRA_XDR`)
  * VMware ESXi (`VMWARE_ESX`)
  * VMWare VSphere (`VMWARE_VSPHERE`)
  * WatchGuard (`WATCHGUARD`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * Zscaler CASB (`ZSCALER_CASB`)
  * Zscaler DLP (`ZSCALER_DLP`)
  * ZScaler DNS (`ZSCALER_DNS`)
  * Zscaler Internet Access Audit Logs (`ZSCALER_INTERNET_ACCESS`)
  * ZScaler NGFW (`ZSCALER_FIREWALL`)
  * Zscaler Private Access (`ZSCALER_ZPA`)
  * Zscaler Secure Private Access Audit Logs (`ZSCALER_ZPA_AUDIT`)
  * Zscaler Tunnel (`ZSCALER_TUNNEL`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, if applicable.

  * Azure App Configuration (`AZURE_APPCONFIGURATION`)
  * Azure App Platform (`AZURE_APPPLATFORM`)
  * Azure ArcData (`AZURE_ARCDATA`)
  * Azure Authorization (`AZURE_AUTHORIZATION`)
  * Azure Change Analysis (`AZURE_CHANGEANALYSIS`)
  * Azure DataFactory (`AZURE_DATAFACTORY`)
  * Doppel (`DOPPEL`)
  * Genian NAC (`GENIAN_NAC`)
  * Penta Security Wapples (`PENTA_WAPPLES`)
  * Redmine (`REDMINE`)
  * S2W Quaxar (`S2W_QUAXAR`)
  * SecurityBridge Dev (`SECURITYBRIDGE_DEV`)
  * TeamT5 ThreatSonar EDR (`TEAMT5_THREATSONAR_EDR`)
  * WorkDay User Sign In (`WORKDAY_USER_SIGNIN`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## May 26, 2025

Feature

**New Storage Transfer Service (STS) based feeds**

This feature is currently in Preview. 

Existing tenants are now able to create new feeds using STS, whereas existing feeds will remain unaffected. Customers will be separately notified about the required steps and timelines for the migration of existing feeds to STS. The following new feeds are available:

  * GOOGLE_CLOUD_STORAGE_V2
  * GOOGLE_CLOUD_STORAGE_EVENT_DRIVEN
  * AMAZON_S3_V2
  * AMAZON_SQS_V2
  * AZURE_BLOBSTORE_V2



The following feed types are replaced by the new STS-based feeds:

  * GOOGLE_CLOUD_STORAGE replaced by GOOGLE_CLOUD_STORAGE_V2
  * AMAZON_S3 replaced by AMAZON_S3_V2
  * AMAZON_SQS replaced by AMAZON_SQS_V2
  * AZURE_BLOBSTORE replaced by AZURE_BLOBSTORE_V2



For more information, see [ Storage Transfer Service and its benefits](https://docs.cloud.google.com/storage-transfer/docs/overview) and [ Configuration by source type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#source-types).

## May 22, 2025

Feature

**Environment load balancing**

The environment load balancing feature offers improved stability and fair resource sharing in multi-tenant environments. It uses a lottery algorithm for resource allocation and lets administrators prioritize SOAR environments via API-based weighting.

For more information, see[ Manage environment load balancing](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/environment-load-balancing).

## May 21, 2025

Announcement

The following parser documentation is now available.

[Collect Apache logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/apache)

[Collect Arista switch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arista-switch)

[Collect Automation Anywhere logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/automation-anywhere)

[Collect Cisco IOS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ios)

[Collect Cisco Router logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-router)

[Collect Cisco Switch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-switch)

[Collect ManageEngine ADAudit Plus logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/me-adaudit-plus)

[Collect Nasuni File Services Platform logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nasuni-fs)

[Collect NetApp SAN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-san)

[Collect Symantec EDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-edr)

[Collect HP ProCurve logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hp-procurve)

[Collect HPE iLO logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hpe-ilo)

[Collect Cisco UCS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ucs)

[Collect Kaspersky AV logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kaspersky-av)

[Collect LimaCharlie EDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/limacharlie-edr)

[Collect McAfee Web Gateway logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-web-gateway)

[Collect Microsoft Defender for Identity logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-for-identity)

[Collect Microsoft LAPS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-laps)

[Collect Nix System Red Hat logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nix-system-red-hat)

[Collect Wiz logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wiz)

## May 20, 2025

Change

**Self-Service Deprovisioning for Google SecOps**

You can now deprovision your Google SecOps tenant and associated data directly. For more information, see [Self-service deprovisioning](https://docs.cloud.google.com/chronicle/docs/onboard/customer-initiated-secops-deprovision).

## May 19, 2025

Announcement

**Simplified provisioning and onboarding**

The process for customer self provisioning and onboarding has been streamlined, significantly reducing the time required to onboard to Google SecOps. 

For more information, see [Onboard a Google SecOps instance](https://docs.cloud.google.com/chronicle/docs/onboard).

## May 15, 2025

Announcement

**Create playbooks with Gemini**

This feature is now in General Availability. For more information, see [Create playbooks with Gemini](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/create-edit-playbook-with-gemini).

## May 14, 2025

Announcement

New premium versions of the following parsers are now available:

  * ZSCALER_WEBPROXY
  * ZSCALER_FIREWALL
  * ZSCALER_DNS
  * ZSCALER_INTERNET_ACCESS
  * ZSCALER_VPN
  * ZSCALER_ZPA
  * ZSCALER_TUNNEL
  * ZSCALER_CASB
  * ZSCALER_DLP
  * ZSCALER_ADMIN_AUDIT



We recommend using the[ documented topology](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration) for each parser.

## May 12, 2025

Change

[YARA-L search with data tables updates](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables)

  * Data tables are now accessible from the **Investigation** menu, instead of **Detection** , in the web interface.
  * Data tables can now be used as a data source in search queries.
  * [Role-based access control (RBAC)](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-data-tables) has been added to manage access to data tables.



Feature

A feature rollout on May 8, 2025, introduced new APIs that may require updated permissions for custom roles to access the detection UI page.

If you encounter access errors, update your permissions, as needed, or select **Revert to Previous Detection Table** on the detection page to revert to the previous UI.

## May 09, 2025

Feature

Google SecOps supports [Self Service creation](https://docs.cloud.google.com/chronicle/docs/event-processing/request-log-type) of custom log types. Self service custom log types let you create custom log types instantly instead of going through SecOps support, allowing quicker data onboarding. This feature will be available as a public preview starting the week of May 12, 2025.

## May 07, 2025

Announcement

We are moving service health updates for Google Cloud Security products from the [Cloud Status Dashboard](https://status.cloud.google.com/) to a [new security-specific status dashboard](https://status.cloud.google.com/security).

This dashboard displays service status and incident history for the following products:

  * Google SecOps
  * Google Threat Intelligence 
  * Mandiant Advantage Threat Intelligence 
  * Mandiant Attack Surface Management 
  * Mandiant Digital Threat Monitoring 
  * Mandiant Hunt 
  * Mandiant Managed Defense 
  * Mandiant Security Validation



## May 05, 2025

Feature

**New Light Theme**

Google SecOps has introduced a new light theme option in the platform. The light theme includes a color palette for visual clarity.

## May 02, 2025

Feature

**Auto extraction of JSON logs**

Google SecOps supports [Auto Extraction](https://docs.cloud.google.com/chronicle/docs/event-processing/auto-extraction) of JSON logs. The auto extraction feature lets you use raw log fields directly in search, detection rules, and [Native Dashboards](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards), with or without a parser. Public preview for this feature begins the week of May 5, 2025.

## April 28, 2025

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so changes may take one-to-four days to appear in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, if applicable. This list now includes both released default parsers and pending parser updates.

  * 1Password Audit Events (`ONEPASSWORD_AUDIT_EVENTS`)
  * AIX system (`AIX_SYSTEM`)
  * Akamai DataStream 2 (`AKAMAI_DATASTREAM_2`)
  * Alveo Risk Data Management (`ALVEO_RDM`)
  * Amazon API Gateway (`AWS_API_GATEWAY`)
  * Apache Tomcat (`TOMCAT`)
  * Appian Cloud (`APPIAN_CLOUD`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * Asset Panda (`ASSET_PANDA`)
  * Aware Audit (`AWARE_AUDIT`)
  * Aware Signals (`AWARE_SIGNALS`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS CloudWatch (`AWS_CLOUDWATCH`)
  * AWS ECS Metrics (`AWS_ECS_METRICS`)
  * AWS Elastic Load Balancer (`AWS_ELB`)
  * AWS GuardDuty (`GUARDDUTY`)
  * AWS Inspector (`AWS_INSPECTOR`)
  * AWS Lambda Function (`AWS_LAMBDA_FUNCTION`)
  * AWS RDS (`AWS_RDS`)
  * AWS Redshift (`AWS_REDSHIFT`)
  * AWS Route 53 DNS (`AWS_ROUTE_53`)
  * AWS Security Hub (`AWS_SECURITY_HUB`)
  * AWS VPC Flow (`AWS_VPC_FLOW`)
  * AWS WAF (`AWS_WAF`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure AD Organizational Context (`AZURE_AD_CONTEXT`)
  * Azure Application Gateway (`AZURE_GATEWAY`)
  * Azure Firewall (`AZURE_FIREWALL`)
  * Azure Key Vault logging (`AZURE_KEYVAULT_AUDIT`)
  * Barracuda CloudGen Firewall (`BARRACUDA_CLOUDGEN_FIREWALL`)
  * Barracuda WAF (`BARRACUDA_WAF`)
  * BeyondTrust BeyondInsight (`BEYONDTRUST_BEYONDINSIGHT`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Broadcom Support Portal Audit Logs (`BROADCOM_SUPPORT_PORTAL`)
  * Cato Networks (`CATO_NETWORKS`)
  * Cequence Bot Defense (`CEQUENCE_BOT_DEFENSE`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * ChromeOS XDR (`CHROMEOS_XDR`)
  * Cisco Email Security (`CISCO_EMAIL_SECURITY`)
  * Cisco EStreamer (`CISCO_ESTREAMER`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco FireSIGHT Management Center (`CISCO_FIRESIGHT`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco IronPort (`CISCO_IRONPORT`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco NX-OS (`CISCO_NX_OS`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco Umbrella Cloud Firewall (`UMBRELLA_FIREWALL`)
  * Cisco vManage SD-WAN (`CISCO_SDWAN`)
  * Cisco VPN (`CISCO_VPN`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Citrix Storefront (`CITRIX_STOREFRONT`)
  * Claroty Xdome (`CLAROTY_XDOME`)
  * Cloud Audit Logs (`N/A`)
  * Cloud Data Loss Prevention (`N/A`)
  * Cloudflare Network Analytics (`CLOUDFLARE_NETWORK_ANALYTICS`)
  * Cloudflare WAF (`CLOUDFLARE_WAF`)
  * Cloudflare Warp (`CLOUDFLARE_WARP`)
  * CommVault (`COMMVAULT`)
  * CrowdStrike Detection Monitoring (`CS_DETECTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CrowdStrike Falcon Stream (`CS_STREAM`)
  * CrowdStrike Identity Protection Services (`CS_IDP`)
  * CrushFTP (`CRUSHFTP`)
  * Custom Application Access Logs (`CUSTOM_APPLICATION_ACCESS`)
  * CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
  * Cybereason EDR (`CYBEREASON_EDR`)
  * Cyolo Secure Remote Access for OT (`CYOLO_OT`)
  * Datadog (`DATADOG`)
  * Delinea Secret Server (`DELINEA_SECRET_SERVER`)
  * Dell CyberSense (`DELL_CYBERSENSE`)
  * Digicert (`DIGICERT`)
  * Edgio WAF (`EDGIO_WAF`)
  * Elastic Packet Beats (`ELASTIC_PACKETBEATS`)
  * F5 ASM (`F5_ASM`)
  * F5 DNS (`F5_DNS`)
  * Forcepoint DLP (`FORCEPOINT_DLP`)
  * Forcepoint NGFW (`FORCEPOINT_FIREWALL`)
  * Forgerock OpenIdM (`FORGEROCK_OPENIDM`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortinet Fortimanager (`FORTINET_FORTIMANAGER`)
  * Fortinet Web Application Firewall (`FORTINET_FORTIWEB`)
  * GitHub (`GITHUB`)
  * Gitlab (`GITLAB`)
  * Harness IO (`HARNESS_IO`)
  * Hashicorp Vault (`HASHICORP`)
  * Hillstone Firewall (`HILLSTONE_NGFW`)
  * Huawei Switches (`HUAWEI_SWITCH`)
  * IBM Guardium (`GUARDIUM`)
  * Imperva Database (`IMPERVA_DB`)
  * Intel Endpoint Management Assistant (`INTEL_EMA`)
  * JAMF Security Cloud (`JAMF_SECURITY_CLOUD`)
  * JFrog Artifactory (`JFROG_ARTIFACTORY`)
  * JumpCloud Directory Insights (`JUMPCLOUD_DIRECTORY_INSIGHTS`)
  * Juniper (`JUNIPER_FIREWALL`)
  * Kaspersky AV (`KASPERSKY_AV`)
  * Kaspersky Endpoint (`KASPERSKY_ENDPOINT`)
  * Kolide Endpoint Security (`KOLIDE`)
  * Kubernetes Audit (`KUBERNETES_AUDIT`)
  * Layer7 SiteMinder (`SITEMINDER_SSO`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * Looker Audit (`LOOKER_AUDIT`)
  * ManageEngine ADAudit Plus (`ADAUDIT_PLUS`)
  * ManageEngine ADManager Plus (`ADMANAGER_PLUS`)
  * McAfee Web Gateway (`MCAFEE_WEBPROXY`)
  * Metabase (`METABASE`)
  * Microsoft AD FS (`ADFS`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft Azure NSG Flow (`AZURE_NSG_FLOW`)
  * Microsoft CyberX (`CYBERX`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Defender for Identity (`MICROSOFT_DEFENDER_IDENTITY`)
  * Microsoft Defender for Office 365 (`MICROSOFT_DEFENDER_MAIL`)
  * Microsoft IIS (`IIS`)
  * Microsoft PowerShell (`POWERSHELL`)
  * Microsoft Sentinel (`MICROSOFT_SENTINEL`)
  * Microsoft System Center Endpoint Protection (`MICROSOFT_SCEP`)
  * Mikrotik Router (`MIKROTIK_ROUTER`)
  * Mimecast (`MIMECAST_MAIL`)
  * MISP Threat Intelligence (`MISP_IOC`)
  * NetIQ eDirectory (`NETIQ_EDIRECTORY`)
  * Netskope V2 (`NETSKOPE_ALERT_V2`)
  * Nozomi Networks Scada Guardian (`NOZOMI_GUARDIAN`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * Okta User Context (`OKTA_USER_CONTEXT`)
  * One Identity Identity Manager (`ONE_IDENTITY_IDENTITY_MANAGER`)
  * Oort Security Tool (`OORT`)
  * Open Cybersecurity Schema Framework (OCSF) (`OCSF`)
  * Open LDAP (`OPENLDAP`)
  * Opnsense (`OPNSENSE`)
  * Ops Genie (`OPS_GENIE`)
  * Oracle (`ORACLE_DB`)
  * Oracle Cloud Guard (`OCI_CLOUDGUARD`)
  * Oracle Cloud Infrastructure Audit Logs (`OCI_AUDIT`)
  * Orca Cloud Security Platform (`ORCA`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Palo Alto Prisma Access (`PAN_CASB`)
  * Palo Alto Prisma Cloud Alert payload (`PAN_PRISMA_CA`)
  * Pharos (`PHAROS`)
  * Privacy-I (`PRIVACY_I`)
  * Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Proofpoint Threat Response (`PROOFPOINT_TRAP`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * ReviveSec (`REVIVESEC`)
  * Rubrik (`RUBRIK`)
  * Salesforce (`SALESFORCE`)
  * Sangfor Proxy (`SANGFOR_PROXY`)
  * Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
  * Security Command Center Threat (`N/A`)
  * Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
  * ServiceNow CMDB (`SERVICENOW_CMDB`)
  * Snare System Diagnostic Logs (`SNARE_SOLUTIONS`)
  * Snipe-IT (`SNIPE_IT`)
  * Snyk Group level audit/issues logs (`SNYK_ISSUES`)
  * SonicWall (`SONIC_FIREWALL`)
  * Sophos Central (`SOPHOS_CENTRAL`)
  * Swimlane Platform (`SWIMLANE`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Symantec Event export (`SYMANTEC_EVENT_EXPORT`)
  * Symantec Web Security Service (`SYMANTEC_WSS`)
  * Tanium Question (`TANIUM_QUESTION`)
  * Tanium Threat Response (`TANIUM_THREAT_RESPONSE`)
  * Teleport Access Plane (`TELEPORT_ACCESS_PLANE`)
  * Tenable Active Directory Security (`TENABLE_ADS`)
  * Tenable CSPM (`TENABLE_CSPM`)
  * tenable.io (`TENABLE_IO`)
  * Terraform Enterprise Audit (`TERRAFORM_ENTERPRISE`)
  * Thinkst Canary (`THINKST_CANARY`)
  * ThreatX WAF (`THREATX_WAF`)
  * Trend Micro Email Security Advanced (`TRENDMICRO_EMAIL_SECURITY`)
  * Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
  * TrendMicro Apex Central (`TRENDMICRO_APEX_CENTRAL`)
  * TXOne Stellar (`TRENDMICRO_STELLAR`)
  * UKG (`UKG`)
  * Unix system (`NIX_SYSTEM`)
  * UPX AntiDDoS (`UPX_ANTIDDOS`)
  * VanDyke SFTP (`VANDYKE_SFTP`)
  * Varonis (`VARONIS`)
  * Vectra Alerts (`VECTRA_ALERTS`)
  * Vectra Stream (`VECTRA_STREAM`)
  * VMware AirWatch (`AIRWATCH`)
  * Vmware Avinetworks iWAF (`VMWARE_AVINETWORKS_IWAF`)
  * VMware ESXi (`VMWARE_ESX`)
  * VMware Horizon (`VMWARE_HORIZON`)
  * Watchguard EDR (`WATCHGUARD_EDR`)
  * Windows Defender AV (`WINDOWS_DEFENDER_AV`)
  * Windows DHCP (`WINDOWS_DHCP`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Windows Sysmon (`WINDOWS_SYSMON`)
  * Workday Audit Logs (`WORKDAY_AUDIT`)
  * Workday User Activity (`WORKDAY_USER_ACTIVITY`)
  * WPEngine (`WPENGINE`)
  * Zimperium (`ZIMPERIUM`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * ZScaler DNS (`ZSCALER_DNS`)
  * Zscaler Internet Access Audit Logs (`ZSCALER_INTERNET_ACCESS`)
  * ZScaler NGFW (`ZSCALER_FIREWALL`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, if applicable.

  * Accenture Synthetic (`ACCENTURE_SYNTHETIC`)
  * Adyen Platform (`ADYEN`)
  * AliCloud ActionTrail (`ALICLOUD_ACTIONTRAIL`)
  * Apache LOG4J Java Application Log (`LOG4J`)
  * AppSmith Audit (`APPSMITH_AUDIT`)
  * Arctic Security Arctic Node (`ARCTIC_NODE`)
  * Arista CorvilNet DANZ Integration (`ARISTA_CORVILNET`)
  * Arista Extensible Operating System (`ARISTA_EOS`)
  * AvePoint EnPower (`AVEPOINT_ENPOWER`)
  * Avigilon Alta Cloud Security (`AVIGILON_ALTA_CLOUD_SECURITY`)
  * Avigilon Ava Security Camera (`AVIGILON_AVA_SECURITY_CAMERA`)
  * AWS Dasha (`AWS_DASHA`)
  * AWS Elastic Kubernetes Service (`AWS_EKS`)
  * Azure Network Security Group Event (`AZURE_NSG_EVENT`)
  * Azure Windows Virtual Desktop Connections Logs (`AZURE_WVD_CONNECTIONS`)
  * Azure Windows Virtual Desktop Management Logs (`AZURE_WVD_MANAGEMENT`)
  * Barracuda Load Balancer ADC (`BARRACUDA_LOAD_BALANCER`)
  * Broadcom Edge Secure Web Gateway (`BROADCOM_EDGE_SWG`)
  * Celonis Audit Logs (`CELONIS`)
  * Chopin PrePay Solutions (`CHOPIN_PPS`)
  * Cisco Duo Authentication Proxy (`DUO_AUTH_PROXY`)
  * Cloudflare CASB Findings (`CLOUDFLARE_CASB_FINDINGS`)
  * Cloudflare Device posture results (`CLOUDFLARE_DEVICE_POSTURE_RESULTS`)
  * Cloudflare DLP Forensic Copies (`CLOUDFLARE_DLP_FORENSIC_COPIES`)
  * Cloudflare DNS Firewall Logs (`CLOUDFLARE_DNS_FIREWALL_LOGS`)
  * Cloudflare DNS logs (`CLOUDFLARE_DNS_LOGS`)
  * Cloudflare Email Security Alerts (`CLOUDFLARE_EMAIL_SECURITY_ALERTS`)
  * Cloudflare Firewall Events (`CLOUDFLARE_FIREWALL_EVENTS`)
  * Cloudflare Gateway DNS (`CLOUDFLARE_GATEWAY_DNS`)
  * Cloudflare Gateway HTTP (`CLOUDFLARE_GATEWAY_HTTP`)
  * Cloudflare Gateway Network (`CLOUDFLARE_GATEWAY_NETWORK`)
  * Cloudflare HTTP requests (`CLOUDFLARE_HTTP_REQUESTS`)
  * Cloudflare Magic IDS Detections (`CLOUDFLARE_MAGIC_IDS_DETECTIONS`)
  * Cloudflare NEL reports (`CLOUDFLARE_NEL_REPORTS`)
  * Cloudflare Sinkhole HTTP Logs (`CLOUDFLARE_SINKHOLE_HTTP_LOGS`)
  * Cloudflare SSH Logs (`CLOUDFLARE_SSH_LOGS`)
  * Cloudflare Workers Trace Events (`CLOUDFLARE_WORKERS_TRACE_EVENTS`)
  * Cloudflare Zero Trust Network Session (`CLOUDFLARE_ZERO_TRUST_NETWORK_SESSION`)
  * CloudWave Honeypot (`CLOUDWAVE_HONEYPOT`)
  * ColorTokens (`COLORTOKENS`)
  * Contrast Security (`CONTRAST_SECURITY`)
  * Conversational Agents and Dialogflow (`CONVERSATIONAL_AGENT`)
  * Corero SmartWall One (`CORERO_SMARTWALL_ONE`)
  * Cytracom Control One (`CYTRACOM_CONTROL_ONE`)
  * Datadog Application Security Management (`DATADOG_ASM`)
  * Express NodeJS (`EXPRESS_NODEJS`)
  * F5 Distributed Cloud WAF (`F5_DCS_WAF`)
  * Figma Developers (`FIGMA`)
  * FIS Trax Payment Factory (`TRAX`)
  * Fortinet FortiDeceptor (`FORTINET_FORTIDECEPTOR`)
  * Fortinet FortiSASE (`FORTINET_FORTISASE`)
  * Gemini Code Assist (`GEMINI_CODE_ASSIST`)
  * Genea Access Control (`GENEA_ACCESS_CONTROL`)
  * Genetec Synergis (`GENETEC_SYNERGIS`)
  * GL TRADE (`GL_TRADE`)
  * HP Inc MFP (`HP_INC_MFP`)
  * HP Tandem (`HP_TANDEM`)
  * Huawei Versatile Routing Platform (`HUAWEI_VRP`)
  * Human Security (`HUMAN_SECURITY`)
  * iManage Threat Manager (`IMANAGE_THREAT_MANAGER`)
  * Indefend DLP (`INDEFEND_DLP`)
  * Invicti (`INVICTI`)
  * Isonline ISL Light (`ISL_LIGHT`)
  * Itential Pronghorn (`ITENTIAL_PRONGHORN`)
  * Jit (`JIT`)
  * Kodem Security (`KODEM_SECURITY`)
  * Konica Minolta YSoft SafeQ (`YSOFT_SAFEQ`)
  * LayerX (`LAYERX`)
  * LinOTP (`LIN_OTP`)
  * Magento Cloud (`MAGENTO_CLOUD`)
  * Mandiant Advantage Security Validation (`MA_SV`)
  * NetApp ONTAP Audit (`NETAPP_ONTAP_AUDIT`)
  * Netscout Arbor Threat Mitigation System (`NETSCOUT_TMS`)
  * Netwrix Privilege Secure (`NETWRIX_PRIVILEGE_SECURE`)
  * NeuVector SUSE (`NEUVECTOR`)
  * Novidea Insurance Management System (`NOVIDEA_CLAIM_HISTORY`)
  * OneTrust (`ONETRUST`)
  * Openpath Context (`OPENPATH_CONTEXT`)
  * Oracle Audit Vault Database Firewall (`ORACLE_AVDF`)
  * Oracle CPQ (`ORACLE_CPQ`)
  * Oracle Exadata Database Machine (`ORACLE_EXADATA`)
  * Palo Alto Prisma Cloud Workload Protection (`PAN_PRISMA_CWP`)
  * Palo Alto Prisma Dig Cloud DSPM (`PAN_PRISMA_DIG_CLOUD_DSPM`)
  * Panorays (`PANORAYS`)
  * Pathlock Identity Security Platform (`PATHLOCK`)
  * Procore (`PROCORE`)
  * ProofPoint Email Protection (`PROOFPOINT_EMAIL_PROTECTION`)
  * Radiantone (`RADIANTONE`)
  * Radware Cloud WAF Service Access (`RADWARE_ACCESS`)
  * Reblaze Web Application Firewall (`REBLAZE_WAF`)
  * Red Access Browsing Security (`RED_ACCESS`)
  * SafeNet Network HSM (`SAFENET_HSM`)
  * Salesforce Marketing Cloud Audit (`SALESFORCE_MARKETING_CLOUD_AUDIT`)
  * Salesforce Shield (`SALESFORCE_SHIELD`)
  * Sangfor IAG (`SANGFOR_IAG`)
  * SAP Leasing (`SAP_LEASING`)
  * SAS Institute (`SAS_INSTITUTE`)
  * Securden (`SECURDEN`)
  * SecurEnvoy SecurAccess (`SECURENVOY_MFA`)
  * Securesoft Sniper IPS (`SECURESOFT_SNIPER_IPS`)
  * Sentra Data Loss Prevention (`SENTRA_DLP`)
  * Shield IoT (`SHIELD_IOT`)
  * Siemens Simatic S7 PLC SNMP (`SIEMENS_S7_PLC_SNMP`)
  * Siemens Simatic S7 PLC SYSLOG (`SIEMENS_S7_PLC_SYSLOG`)
  * Smartsheet User Context (`SMARTSHEET_USER_CONTEXT`)
  * Snowflake Access (`SNOWFLAKE_ACCESS`)
  * SOCRadar Incidents (`SOCRADAR_INCIDENTS`)
  * Strata Maverics Identity Orchestration Platform (`STRATA_MAVERICS`)
  * Stripe Payments (`STRIPE`)
  * Suridata (`SURIDATA`)
  * Teradata Access (`TERADATA_ACCESS`)
  * Thales payShield 10K HSM (`THALES_PS10K_HSM`)
  * Trend Micro TippingPoint Security Management System (`TREND_MICRO_TIPPING_POINT`)
  * Valence Security (`VALENCE`)
  * Vertica Audit (`VERTICA_AUDIT`)
  * Windows NTP (`WINDOWS_NTP`)
  * Winget Autoupdate (`WINGET_AUTOUPDATE`)
  * Wiz Runtime Execution Data (`WIZ_RUNTIME_EXECUTION_DATA`)
  * Workiva Wdesk (`WORKIVA_WDESK`)
  * XL Release (`XLR`)
  * Yugabyte Database (`YUGABYTE_DATABASE`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## April 25, 2025

Feature

Google SecOps now supports native integration with Azure Event Hub through the feed management API or web interface. This enhancement enables real-time log ingestion without requiring Azure blob storage. For more information, see [Create an Azure Event Hub feed](https://docs.cloud.google.com/chronicle/docs/administration/create-azure-feed).

## April 23, 2025

Feature

This feature is currently in Preview. Google SecOps now supports [composite detections](https://docs.cloud.google.com/chronicle/docs/detection/composite-detections). Composite detections lets users link multiple YARA-L rules to detect complex, multistage threats. This capability enhances detection by correlating alerts that individual rules might not detect.

## April 22, 2025

Announcement

The following parser documentation is now available:

[Collect Barracuda Email Security Gateway logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-email)

[Collect Barracuda WAF logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-waf)

[Collect CrowdStrike Falcon logs in CEF](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crowdstrike-cef)

[Collect Juniper NetScreen Firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/juniper-nf)

[Collect Micro Focus NetIQ Access Manager logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netiq-am)

[Collect Symantec DLP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-dlp)

[Collect Aruba ClearPass logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-clearpass)

[Collect Aruba Wireless Controller and Access Point logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-wc)

[Collect BeyondTrust Secure Remote Access logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-sra)

[Collect CyberArk Privileged Threat Analytics logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-pta)

[Collect Fortinet FortiMail logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fm)

[Collect Sophos Central logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-central)

[Collect Sophos XG Firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-xgf)

[Collect AWS EC2 Hosts logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ec2hosts)

[Collect AWS EC2 Instance logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ec2instance)

[Collect AWS IAM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-iam)

[Collect Cisco Stealthwatch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-sna)

[Collect Cisco Umbrella audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ua)

[Collect Cisco Umbrella DNS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-udns)

[Collect Cisco Umbrella Web Proxy logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-uwb)

[Collect CommVault Backup and Recovery logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/commvault-br)

[Collect Forcepoint Proxy logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-webproxy)

[Collect Fortinet FortiAnalyzer logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fana)

[Collect Fortinet FortiAuthenticator logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-faut)

[Collect Fortinet Firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fw)

[Collect Palo Alto Networks Traps logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-traps)

[Collect SecureAuth Identity Platform logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/secureauth-ip)

[Collect Claroty CTD logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/claroty-ctd)

[Collect Claroty xDome logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/claroty-xdome)

[Collect F5 BIG-IP ASM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-asm)

[Collect FireEye HX logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx)

[Collect Microsoft IIS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ms-iis)

[Collect PowerShell logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/powershell)

[Collect Snort logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snort)

[Collect A10 Network Load Balancer logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/a10-lb)

[Collect Alcatel switch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/alcatel-switch)

[Collect AlgoSec Security Management logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/algosec-sm)

[Collect Arbor Edge Defense logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arbor-edge-defense)

[Collect Epic Systems logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/epic-systems)

[Collect Fortra Digital Guardian DLP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortra-dg-dlp)

[Collect MobileIron logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mobileiron)

[Collect Microsoft Windows Defender ATP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/msdefender-atp)

[Collect Nokia Router logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nokia-router)

[Collect Broadcom Symantec SiteMinder Web Access logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/siteminder-wa)

## April 21, 2025

Feature

[Curated Detections](https://docs.cloud.google.com/chronicle/docs/detection/use-curated-detections) has been enhanced with new detection content for [Cloud Threats](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category) to include rule packs covering Office 365 and Okta. These rule packs are in public preview for customers with a Google Security Operations or Enterprise Plus license.

## April 18, 2025

Feature

**Chrome Enterprise Threats Category**

This feature is currently in Preview.

Google SecOps has introduced a new detection category, _Chrome Enterprise Threats_ , as part of the [Curated Detections](https://docs.cloud.google.com/chronicle/docs/detection/curated-detections) feature. This category provides rule sets for extension and browser threats. For more information, see [Overview of Chrome Enterprise Threats Category](https://docs.cloud.google.com/chronicle/docs/detection/chrome-enterprise-threats-category).

## April 17, 2025

Feature

**Entity Context in Search**

This feature enhances security investigations and incident response by letting users search for and view context events related to entities. It incorporates UDM entity context data to provide deeper insights into security incidents.

This feature is currently in Preview.

## April 15, 2025

Announcement

We are releasing updated versions of the following premium parsers:

  * Crowdstrike Detection Monitoring (CS_DETECTS)
  * Crowdstrike Falcon (CS_EDR)
  * Microsoft Defender for Endpoint



These updates include significant improvements to parser mappings. For a detailed list of all mapping changes, contact your Google SecOps representative.

The new versions will remain in an extended Release Candidate period through the end of May 2025. We recommend that you opt-in early and make any necessary adjustments before these updates become the default.

## April 07, 2025

Feature

**Premium parsers**

Specific high-volume parsers are now categorized as **premium**. Google aims to address customer issues related to premium parsers as quickly as possible, typically within a few days. 

For a complete list of different types of parsers and the level of support that Google provides for each, see[ Manage prebuilt and custom parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates).

For a complete list of premium parsers, see [Default parser configuration and ingestion](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration).

## April 06, 2025

Feature

**Create a quick action (Preview)**

Administrators can now predefine quick actions for analysts to execute directly within cases and alerts.

The **Quick Actions** widget can be added to default case and alert views, and customized alert views within playbooks.

For more information, see [Create a quick action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/quick-actions).

Feature

**What's New in Google SecOps**

At the top of your Google SecOps screen, click the question mark and select **What's New** to display the top five new features in the Google SecOps platform.

## April 04, 2025

Feature

**Optimize log management using extractors**

This feature is currently in Preview. 

You can now optimize log management by creating extractors to pull specific fields from high-volume log sources. For more information, see [Work with extractors](https://docs.cloud.google.com/chronicle/docs/event-processing/auto-extraction#extractors).

## April 02, 2025

Feature

**Medium Priority rule set**

Google SecOps has introduced a new rule set, _Medium Priority_ , in Applied Threat Intelligence (ATI). This rule set extends the capabilities of the ATI indicator prioritization model and expands prioritization logic to include commodity malware. For more information, see [Applied Threat Intelligence priority overview](https://docs.cloud.google.com/chronicle/docs/detection/ati-prioritization).

## March 27, 2025

Change

Google SecOps is renaming Applied Threat Intelligence (ATI) rules to improve clarity and better reflect the associated UDM fields with each rule detection.

Currently, multiple underlying ATI rules with the same name can appear in the Google SecOps console, even though the rules apply to different UDM fields.

This change modifies the `rule_name` field in the customer metadata to specify the relevant UDM field for each rule.

For example:

Old rule name: **ATI Active Breach Rule Match for File IoCs (SHA256)**

New rule name: **ATI Active Breach Rule Match for File IoCs (about.file.sha256)**

## March 26, 2025

Announcement

The managed BigQuery resources and API keys associated with the chronicle-tla Google Cloud project will be fully deprecated by April 30, 2025. This applies to non-Enterprise+ customers only.

## March 24, 2025

Change

**Updated retention logic for raw logs and UDM events**

Google SecOps now retains raw logs based on the ingestion timestamp and UDM events based on the UDM event time.

## March 19, 2025

Announcement

The following parser documentation is now available:

[Collect AWS Config logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-config)

[Collect AWS Elastic Load Balancing logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-elb)

[Collect AWS Route 53 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-route53)

[Collect AWS S3 server access logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-s3-sa)

[Collect AWS WAF logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-waf)

[Collect Azure Application Gateway logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-gateway)

[Collect Carbon Black App Control logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/carbon-black-ac)

[Collect Carbon Black EDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/carbon-black-edr)

[Collect Delinea Secret Server logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-ss)

[Collect Radware WAF logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/radware-waf)

[Collect AWS Aurora logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-aurora)

[Collect AWS CloudWatch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudwatch)

[Collect AWS Control Tower logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-control-tower)

[Collect AWS Elastic MapReduce logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-emr)

[Collect AWS Key Management Service logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-kms)

[Collect AWS Macie logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-macie)

[Collect AWS Network Firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-network-firewall)

[Collect AWS Security Hub logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-security-hub)

[Collect AWS Session Manager logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-session-manager)

[Collect Zscaler DLP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-dlp-logs)

[Collect Zscaler Tunnel logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-tunnel-logs)

[Collect Zscaler VPN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-vpn-logs)

[Collect Zscaler ZPA Audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-zpa-audit-logs)

[Collect Zscaler ZPA logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-zpa-logs)

[Collect Zscaler CASB logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-casb)

[Collect Azure AD Sign-In logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-signin)

[Collect Azure API Management logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-api-management)

[Collect Azure APP Service logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-app-service)

[Collect Azure Firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-firewall)

[Collect Azure VPN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-vpn)

[Collect AWS VPN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpn)

[Collect Azure Storage Audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-sa)

[Collect Azure WAF logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-waf)

[Collect Cloud IoT logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-iot)

[Collect Cloud Run logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudrun)

[Collect Cloud Compute logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/compute)

[Collect CrowdStrike Falcon Stream logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crowdstrike-stream)

[Collect SentinelOne Deep Visibility logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinelone-dv)

[Collect Cloud VPC Flow Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-vpc-flow)

[Collect Cloud Compute context logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-compute-context)

[Collect Cloud Intrusion Detection System (Cloud IDS) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-ids)

[Collect Cloud Next Generation Firewall Enterprise logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-ngfw)

[Collect Cloud Storage context logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-storage-context)

[Collect Cloud Identity and Access Management (IAM) Analysis logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iam-analysis)

[Collect Cloud Identity Devices logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-id)

[Collect Cloud Identity Device Users logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-idu)

[Collect Cloud Security Command Center Error logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-scc-error)

[Collect Cloud Security Command Center Observation logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-scc-observation)

[Collect Cloud Security Command Center Posture Violation logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-scc-pv)

[Collect Cloud Security Command Center Toxic Combination logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-scc-tc)

[Collect Cloud Security Command Center Unspecified logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-scc-unspecified)

[Collect Cloud Secure Web Proxy logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-swp)

## March 18, 2025

Feature

**Statistics and aggregations in UDM search using YARA-L 2.0**

You can now run statistical queries on UDM events and group the results for analysis using YARA-L 2.0. You can use the statistical queries to track critical metrics, detect anomalous behavior, and analyze trends over time. For more information on how to run statistical queries on UDM events, see [Statistics and aggregations in UDM search using YARA-L 2.0](https://docs.cloud.google.com/chronicle/docs/investigation/statistics-aggregations-in-udm-search).

## March 16, 2025

Feature

**Remote agent high availability**

This feature is currently in preview. 

Remote agents can now leverage high availability deployment, ensuring increased reliability for remote connectors, actions, and jobs. 

This feature also introduces a new cloud-based remote connector scheduler for improved performance and scalability.

For more information, see [Deploy high availability in remote agents](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-high-availability-for-remote-agents).

Feature

**Remote agent downtime notifications**

Customers using remote agents can now opt in to receive in-app or email notifications when the agent is down.

Feature

**Pause or resume Case SLA**

Users can now pause and resume service level agreement (SLA) timers on cases. 

For more information, see[ Pause and resume a case SLA](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/setting-the-sla#pause-and-resume-a-case-sla).

## March 11, 2025

Feature

Within [Curated Detections](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#cloud-rule-sets), the following rules have been added to the Cloud Hacktool rule pack for Google Cloud data in the "Broad" category. These rules are intended to detect the behavior of common open source hacktools.

  * **Collection: Set GCP Cloud Storage Bucket to Public**
  * **Discovery: Cloud Run Enumeration**
  * **Discovery: CloudFunctions Enumeration of GCP Cloud Functions**
  * **Discovery: CloudKMS Enumeration of GCP Cloud KMS**
  * **Discovery: CloudResourceManager Resource Manager Enumeration**
  * **Discovery: Compute Enumeration**
  * **Discovery: GCP Cloud IAM Enumeration**
  * **Discovery: Secret Manager Cloud Secrets Enumeration**
  * **Discovery: Storage Cloud Storage Enumeration**
  * **Exfiltration: Download Cloud Function Code**
  * **Exfiltration: Export a Compute Image Instance**
  * **Persistence: Generate Signed URL for Modifying Cloud Function Code**
  * **Privilege Escalation: Compute Set Instance or Project Metadata to Enable OS Login**



Feature

URL indicators are now available for matching as part of Applied Threat Intelligence. For more information about Applied Threat Intelligence, see [Applied Threat Intelligence overview](https://docs.cloud.google.com/chronicle/docs/detection).

## March 10, 2025

Change

The following rule has been removed from its associated rule pack in Curated Detections due to high alert volume across the Google SecOps customer base:

  * Serverless Threats 
    * Potential Cryptomining Payload running in Cloud Run Service or Cloud Run Job



## March 09, 2025

Announcement

The **session timeout** duration is being extended from 3 hours to 8 hours. After 8 hours of activity, you are automatically logged out and required to sign in again. To prevent data loss, we recommend that you manually log out in advance if you anticipate being away from the platform for an extended period of time. This feature will be gradually rolled out starting March 17, 2025.

## March 08, 2025

Feature

**Map users in the platform for Google Cloud Identity customers**

Administrators can now provision and map new users into the platform by adding them to groups in bulk using their email addresses. This streamlines user management and access control for organizations using Google Cloud Identity.

For more information, see [Map users with email groups to the platform](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party).

## March 05, 2025

Change

**Gemini documentation summaries**

You can use Gemini to answer questions about Google SecOps based on the documentation. Enter a prompt in the Gemini pane to request information about any aspect of how to use Google SecOps. Gemini generates a summary based on relevant documentation. This feature is in public preview.

For more information, see [Gemini documentation summaries](https://docs.cloud.google.com/chronicle/docs/secops/gemini-docs).

## March 03, 2025

Announcement

The [Custom Fields](https://docs.cloud.google.com/chronicle/docs/secops/release-notes#February_22_2025) feature is now in General Availability.

## February 28, 2025

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have changed. Each parser is listed by product name and `log_type` value, if applicable. This list now includes both released default parsers and pending parser updates.

  * 1Password Audit Events (`ONEPASSWORD_AUDIT_EVENTS`)
  * AIX system (`AIX_SYSTEM`)
  * Akamai DataStream 2 (`AKAMAI_DATASTREAM_2`)
  * Alveo Risk Data Management (`ALVEO_RDM`)
  * Amazon API Gateway (`AWS_API_GATEWAY`)
  * Apache Tomcat (`TOMCAT`)
  * Appian Cloud (`APPIAN_CLOUD`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * Asset Panda (`ASSET_PANDA`)
  * Aware Audit (`AWARE_AUDIT`)
  * Aware Signals (`AWARE_SIGNALS`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS CloudWatch (`AWS_CLOUDWATCH`)
  * AWS ECS Metrics (`AWS_ECS_METRICS`)
  * AWS Elastic Load Balancer (`AWS_ELB`)
  * AWS GuardDuty (`GUARDDUTY`)
  * AWS Inspector (`AWS_INSPECTOR`)
  * AWS Lambda Function (`AWS_LAMBDA_FUNCTION`)
  * AWS RDS (`AWS_RDS`)
  * AWS Redshift (`AWS_REDSHIFT`)
  * AWS Route 53 DNS (`AWS_ROUTE_53`)
  * AWS Security Hub (`AWS_SECURITY_HUB`)
  * AWS VPC Flow (`AWS_VPC_FLOW`)
  * AWS WAF (`AWS_WAF`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure AD Organizational Context (`AZURE_AD_CONTEXT`)
  * Azure Application Gateway (`AZURE_GATEWAY`)
  * Azure Firewall (`AZURE_FIREWALL`)
  * Azure Key Vault logging (`AZURE_KEYVAULT_AUDIT`)
  * Barracuda CloudGen Firewall (`BARRACUDA_CLOUDGEN_FIREWALL`)
  * Barracuda WAF (`BARRACUDA_WAF`)
  * BeyondTrust BeyondInsight (`BEYONDTRUST_BEYONDINSIGHT`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Broadcom Support Portal Audit Logs (`BROADCOM_SUPPORT_PORTAL`)
  * Cato Networks (`CATO_NETWORKS`)
  * Cequence Bot Defense (`CEQUENCE_BOT_DEFENSE`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * ChromeOS XDR (`CHROMEOS_XDR`)
  * Cisco Email Security (`CISCO_EMAIL_SECURITY`)
  * Cisco EStreamer (`CISCO_ESTREAMER`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco FireSIGHT Management Center (`CISCO_FIRESIGHT`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco IronPort (`CISCO_IRONPORT`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco NX-OS (`CISCO_NX_OS`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco Umbrella Cloud Firewall (`UMBRELLA_FIREWALL`)
  * Cisco vManage SD-WAN (`CISCO_SDWAN`)
  * Cisco VPN (`CISCO_VPN`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Citrix Storefront (`CITRIX_STOREFRONT`)
  * Claroty Xdome (`CLAROTY_XDOME`)
  * Cloud Audit Logs (`N/A`)
  * Cloud Data Loss Prevention (`N/A`)
  * Cloudflare Network Analytics (`CLOUDFLARE_NETWORK_ANALYTICS`)
  * Cloudflare WAF (`CLOUDFLARE_WAF`)
  * Cloudflare Warp (`CLOUDFLARE_WARP`)
  * CommVault (`COMMVAULT`)
  * CrowdStrike Detection Monitoring (`CS_DETECTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CrowdStrike Falcon Stream (`CS_STREAM`)
  * Crowdstrike Identity Protection Services (`CS_IDP`)
  * CrushFTP (`CRUSHFTP`)
  * Custom Application Access Logs (`CUSTOM_APPLICATION_ACCESS`)
  * CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
  * Cybereason EDR (`CYBEREASON_EDR`)
  * Cyolo Secure Remote Access for OT (`CYOLO_OT`)
  * Datadog (`DATADOG`)
  * Delinea Secret Server (`DELINEA_SECRET_SERVER`)
  * Dell CyberSense (`DELL_CYBERSENSE`)
  * Digicert (`DIGICERT`)
  * Edgio WAF (`EDGIO_WAF`)
  * Elastic Packet Beats (`ELASTIC_PACKETBEATS`)
  * F5 ASM (`F5_ASM`)
  * F5 DNS (`F5_DNS`)
  * Forcepoint DLP (`FORCEPOINT_DLP`)
  * Forcepoint NGFW (`FORCEPOINT_FIREWALL`)
  * Forgerock OpenIdM (`FORGEROCK_OPENIDM`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortinet Fortimanager (`FORTINET_FORTIMANAGER`)
  * Fortinet Web Application Firewall (`FORTINET_FORTIWEB`)
  * GitHub (`GITHUB`)
  * Gitlab (`GITLAB`)
  * Harness IO (`HARNESS_IO`)
  * Hashicorp Vault (`HASHICORP`)
  * Hillstone Firewall (`HILLSTONE_NGFW`)
  * Huawei Switches (`HUAWEI_SWITCH`)
  * IBM Guardium (`GUARDIUM`)
  * Imperva Database (`IMPERVA_DB`)
  * Intel Endpoint Management Assistant (`INTEL_EMA`)
  * JAMF Security Cloud (`JAMF_SECURITY_CLOUD`)
  * JFrog Artifactory (`JFROG_ARTIFACTORY`)
  * JumpCloud Directory Insights (`JUMPCLOUD_DIRECTORY_INSIGHTS`)
  * Juniper (`JUNIPER_FIREWALL`)
  * Kaspersky AV (`KASPERSKY_AV`)
  * Kaspersky Endpoint (`KASPERSKY_ENDPOINT`)
  * Kolide Endpoint Security (`KOLIDE`)
  * Kubernetes Audit (`KUBERNETES_AUDIT`)
  * Layer7 SiteMinder (`SITEMINDER_SSO`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * Looker Audit (`LOOKER_AUDIT`)
  * ManageEngine ADAudit Plus (`ADAUDIT_PLUS`)
  * ManageEngine ADManager Plus (`ADMANAGER_PLUS`)
  * McAfee Web Gateway (`MCAFEE_WEBPROXY`)
  * Metabase (`METABASE`)
  * Microsoft AD FS (`ADFS`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft Azure NSG Flow (`AZURE_NSG_FLOW`)
  * Microsoft CyberX (`CYBERX`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Defender for Identity (`MICROSOFT_DEFENDER_IDENTITY`)
  * Microsoft Defender for Office 365 (`MICROSOFT_DEFENDER_MAIL`)
  * Microsoft IIS (`IIS`)
  * Microsoft PowerShell (`POWERSHELL`)
  * Microsoft Sentinel (`MICROSOFT_SENTINEL`)
  * Microsoft System Center Endpoint Protection (`MICROSOFT_SCEP`)
  * Mikrotik Router (`MIKROTIK_ROUTER`)
  * Mimecast (`MIMECAST_MAIL`)
  * MISP Threat Intelligence (`MISP_IOC`)
  * NetIQ eDirectory (`NETIQ_EDIRECTORY`)
  * Netskope V2 (`NETSKOPE_ALERT_V2`)
  * Nozomi Networks Scada Guardian (`NOZOMI_GUARDIAN`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * Okta User Context (`OKTA_USER_CONTEXT`)
  * One Identity Identity Manager (`ONE_IDENTITY_IDENTITY_MANAGER`)
  * Oort Security Tool (`OORT`)
  * Open Cybersecurity Schema Framework (OCSF) (`OCSF`)
  * Open LDAP (`OPENLDAP`)
  * Opnsense (`OPNSENSE`)
  * Ops Genie (`OPS_GENIE`)
  * Oracle (`ORACLE_DB`)
  * Oracle Cloud Guard (`OCI_CLOUDGUARD`)
  * Oracle Cloud Infrastructure Audit Logs (`OCI_AUDIT`)
  * Orca Cloud Security Platform (`ORCA`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Palo Alto Prisma Access (`PAN_CASB`)
  * Palo Alto Prisma Cloud Alert payload (`PAN_PRISMA_CA`)
  * Pharos (`PHAROS`)
  * Privacy-I (`PRIVACY_I`)
  * Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Proofpoint Threat Response (`PROOFPOINT_TRAP`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * ReviveSec (`REVIVESEC`)
  * Rubrik (`RUBRIK`)
  * Salesforce (`SALESFORCE`)
  * Sangfor Proxy (`SANGFOR_PROXY`)
  * Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
  * Security Command Center Threat (`N/A`)
  * Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
  * ServiceNow CMDB (`SERVICENOW_CMDB`)
  * Snare System Diagnostic Logs (`SNARE_SOLUTIONS`)
  * Snipe-IT (`SNIPE_IT`)
  * Snyk Group level audit/issues logs (`SNYK_ISSUES`)
  * SonicWall (`SONIC_FIREWALL`)
  * Sophos Central (`SOPHOS_CENTRAL`)
  * Swimlane Platform (`SWIMLANE`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Symantec Event export (`SYMANTEC_EVENT_EXPORT`)
  * Symantec Web Security Service (`SYMANTEC_WSS`)
  * Tanium Question (`TANIUM_QUESTION`)
  * Tanium Threat Response (`TANIUM_THREAT_RESPONSE`)
  * Teleport Access Plane (`TELEPORT_ACCESS_PLANE`)
  * Tenable Active Directory Security (`TENABLE_ADS`)
  * Tenable CSPM (`TENABLE_CSPM`)
  * tenable.io (`TENABLE_IO`)
  * Terraform Enterprise Audit (`TERRAFORM_ENTERPRISE`)
  * Thinkst Canary (`THINKST_CANARY`)
  * ThreatX WAF (`THREATX_WAF`)
  * Trend Micro Email Security Advanced (`TRENDMICRO_EMAIL_SECURITY`)
  * Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
  * TrendMicro Apex Central (`TRENDMICRO_APEX_CENTRAL`)
  * TXOne Stellar (`TRENDMICRO_STELLAR`)
  * UKG (`UKG`)
  * Unix system (`NIX_SYSTEM`)
  * UPX AntiDDoS (`UPX_ANTIDDOS`)
  * VanDyke SFTP (`VANDYKE_SFTP`)
  * Varonis (`VARONIS`)
  * Vectra Alerts (`VECTRA_ALERTS`)
  * Vectra Stream (`VECTRA_STREAM`)
  * VMware AirWatch (`AIRWATCH`)
  * Vmware Avinetworks iWAF (`VMWARE_AVINETWORKS_IWAF`)
  * VMware ESXi (`VMWARE_ESX`)
  * VMware Horizon (`VMWARE_HORIZON`)
  * Watchguard EDR (`WATCHGUARD_EDR`)
  * Windows Defender AV (`WINDOWS_DEFENDER_AV`)
  * Windows DHCP (`WINDOWS_DHCP`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Windows Sysmon (`WINDOWS_SYSMON`)
  * Workday Audit Logs (`WORKDAY_AUDIT`)
  * Workday User Activity (`WORKDAY_USER_ACTIVITY`)
  * WPEngine (`WPENGINE`)
  * Zimperium (`ZIMPERIUM`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * ZScaler DNS (`ZSCALER_DNS`)
  * Zscaler Internet Access Audit Logs (`ZSCALER_INTERNET_ACCESS`)
  * ZScaler NGFW (`ZSCALER_FIREWALL`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, if applicable.

  * Autodesk Cad Cam (`AUTODESK_CAD_CAM`)
  * Azure Risk Events (`AZURE_RISK_EVENTS`)
  * Azure Risky Users (`AZURE_RISKY_USERS`)
  * Azure Service Principal Logins (`AZURE_SERVICE_PRINCIPAL_LOGINS`)
  * Belden Switch (`BELDEN_SWITCH`)
  * Blue Voyant (`BLUE_VOYANT`)
  * Cisco NetFlow (`CISCO_NETFLOW`)
  * Citrix Receiver (`CSG_CITRIX_RX`)
  * Clavistier Firewall (`CLAVISTER_FIREWALL`)
  * ClickHouse (`CLICKHOUSE`)
  * Cloudflare Pageshield (`CLOUDFLARE_PAGESHIELD`)
  * CrowdStrike DLP (`CROWDSTRIKE_DLP`)
  * Crowdstrike Recon (TI) (`CROWDSTRIKE_RECON`)
  * Cynerio Healthcare NDR (`CYNERIO_NDR_H`)
  * Exterro FTK Central (`EXTERRO_FTK_CENTRAL`)
  * Fortra Vulnerability Management (`FORTRA_VM`)
  * GCP Cloud Asset Inventory (`GCP_CLOUD_ASSET_INVENTORY`)
  * Health ISAC (`H_ISAC`)
  * HP Router (`HP_ROUTER`)
  * Huawei Wireless (`HUAWEI_WIRELESS`)
  * IBM Sense (`IBM_SENSE`)
  * IIJ_LanScope (`IIJ_LANSCOPE`)
  * Joblogic (`JOBLOGIC`)
  * OneIdentity Safeguard (`ONEIDENTITY_SAFEGUARD`)
  * OpenText Cordy (`OPENTEXT_CORDY`)
  * Pave (`PAVE`)
  * Proofpoint Identity Threat Platform (`PROOFPOINT_IDENTITY_THREAT_PLATFORM`)
  * Rapid Identity (`RAPID_IDENTITY`)
  * Raven DB (`RAVEN_DB`)
  * SolidServer (`SOLIDSERVER`)
  * Spacelift (`SPACELIFT`)
  * Trend Micro Vision One Activity (`TRENDMICRO_VISION_ONE_ACTIVITY`)
  * Trend Micro Vision One Container Vulnerabilities (`TRENDMICRO_VISION_ONE_CONTAINER_VULNERABILITIES`)
  * Trend Micro Vision One Detections (`TRENDMICRO_VISION_ONE_DETECTIONS`)
  * Vectra XDR (`VECTRA_XDR`)
  * Vicarious VRX Events (`VICARIUS_VRX_EVENTS`)
  * WireGuard VPN Logs (`WIREGUARD_VPN`)
  * Zero Networks (`ZERO_NETWORKS`)
  * Zoho Assist (`ZOHO_ASSIST`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## February 25, 2025

Announcement

The [Custom Fields](https://docs.cloud.google.com/chronicle/docs/secops/release-notes#February_22_2025) feature has been rolled back.

## February 22, 2025

Feature

**New Custom fields for case management**

  * Added support for custom fields that analysts can fill out when working with cases or alerts, such as **report time** or **false positives**. These fields appear as a widget in the Case or Alert overview tab.
  * Custom fields can now be added to playbooks as actions or placeholders.
  * Requires downloading the latest **Siemplify** integration. 



For more information about this new feature, see [Create Custom Fields](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/adding-custom-fields).

## February 20, 2025

Feature

[Data tables](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables)

Data tables are multicolumn data constructs that let you input your own data into Google SecOps. They can act as lookup tables with defined columns and the data stored in rows. You can create or import a data table to your Google SecOps account using the Google SecOps UI, the data tables API, or by using a YARA-L query in rules. This feature is in public preview.

Feature

Enhanced [Cloud Threat Detections](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category) by adding three new rules to the AWS - GuardDuty rule set.

## February 15, 2025

Feature

**This feature is available in Preview.**

**New options to close a case**

New custom field options have been added to the SOAR Settings > Case Data > Close Case page. Once you define these fields, analysts must enter specific types of information when closing a case.

For more information, refer to [Customize the Close Case dialog](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/add-new-case-close-root-cause-admin).

Feature

**Manage user preferences**

The ability to manage platform time zones, date/time settings, and notifications has been relocated to the new **User Preferences** dialog, accessible from your avatar.

In addition, a new accessibility option in the **User Preferences** dialog lets you define how long feedback messages remain on the screen.   
  
For more information, refer to [Configure user preferences](https://docs.cloud.google.com/chronicle/docs/secops/user-preferences).

## February 12, 2025

Announcement

The following parser documentation is now available:

[Collect NGINX logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nginx)

[Collect Proofpoint On-Demand logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-od)

[Collect Qualys asset context logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-ac)

[Collect Qualys Continuous Monitoring logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-cm)

[Collect Qualys Scan logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-scan)

[Collect Qualys Vulnerability Management logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-vm)

[Collect Qualys Virtual Scanner logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-vs)

[Collect ThreatConnect IOC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc)

[Collect Akamai DNS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-dns)

[Collect Aruba switch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-switch)

[Collect Bitdefender logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bitdefender)

[Collect HashiCorp audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hashicorp)

[Collect Microsoft SQL Server logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-microsoft-sql-logs)

[Collect FireEye NX logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-fireeye-nx-logs)

[Collect Illumio Core logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-illumio-core-logs)

[Collect Microsoft Azure Key Vault logging logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-azure-keyvault-audit-logs)

[Collect BeyondTrust Remote Support logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-rs)

[Collect BlueCat DDI logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecat-ddi)

[Collect BMC Helix Discovery logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bmc-helix-discovery)

[Collect Brocade ServerIron logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/brocade-serverIron)

[Collect Check Point firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-fw)

[Collect CyberArk EPM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-epm)

[Collect CyberArk PAM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-pam)

[Collect Dell ECS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-ecs)

[Collect Dell switch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-switch)

[Collect IBM Security Verify Access logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sva)

[Collect McAfee Firewall Enterprise logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-esm)

[Collect NetApp ONTAP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-ontap)

[Collect Trend Micro Apex One logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-apexone)

[Collect Trend Micro Deep Security logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-ds)

[Collect Versa Networks Secure Access Service Edge (SASE) logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/versa-sase)

[Collect VMware Networking and Security Virtualization (NSX) Manager logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-nsx)

[Collect Zscaler Cloud Access Security Broker (CASB) alert logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-casb)

## February 11, 2025

Fixed

The following is a correction to the release note published on [December 22, 2024](https://docs.cloud.google.com/chronicle/docs/release-notes#December_22_2024).

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have changed. Each parser is listed by product name and `log_type` value, if applicable. This list now includes both released default parsers and pending parser updates.

  * Absolute Mobile Device Management (`ABSOLUTE`)
  * Atlassian Cloud Admin Audit (`ATLASSIAN_AUDIT`)
  * AWS VPC Flow (`AWS_VPC_FLOW`)
  * Azure AD (`AZURE_AD`)
  * Azure Application Gateway (`AZURE_GATEWAY`)
  * Azure SQL (`AZURE_SQL`)
  * Azure Storage Audit (`AZURE_STORAGE_AUDIT`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Check Point Harmony (`CHECKPOINT_HARMONY`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco Meraki (`CISCO_MERAKI`)
  * Cisco Router (`CISCO_ROUTER`)
  * Cisco Umbrella SWG DLP (`CISCO_UMBRELLA_SWG_DLP`)
  * Cisco VPN (`CISCO_VPN`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Claroty Continuous Threat Detection (`CLAROTY_CTD`)
  * Cloud Audit Logs (`N/A`)
  * Cloud DNS (`N/A`)
  * Code42 Incydr (`CODE42_INCYDR`)
  * Colinet Trotta GAUS SEGUROS (`CT_GAUS_SEGUROS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * Delinea Distributed Engine (`DELINEA_DISTRIBUTED_ENGINE`)
  * Druva Backup (`DRUVA_BACKUP`)
  * Duo Administrator Logs (`DUO_ADMIN`)
  * Elastic Audit Beats (`ELASTIC_AUDITBEAT`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * Forcepoint NGFW (`FORCEPOINT_FIREWALL`)
  * FortiGate (`FORTINET_FIREWALL`)
  * GitHub (`GITHUB`)
  * Google Cloud Identity Context (`CLOUD_IDENTITY_CONTEXT`)
  * Guardicore Centra (`GUARDICORE_CENTRA`)
  * HPE Aruba Networking Central (`ARUBA_CENTRAL`)
  * Imperva Advanced Bot Protection (`IMPERVA_ABP`)
  * Kubernetes Audit Azure (`KUBERNETES_AUDIT_AZURE`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * Maria Database (`MARIA_DB`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Opnsense (`OPNSENSE`)
  * Oracle NetSuite (`ORACLE_NETSUITE`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Palo Alto Prisma Cloud Alert payload (`PAN_PRISMA_CA`)
  * Ping One (`PING_ONE`)
  * Proofpoint Observeit (`OBSERVEIT`)
  * Proofpoint Threat Response (`PROOFPOINT_TRAP`)
  * QNAP Systems NAS (`QNAP_NAS`)
  * Reserved LogType2 (`RESERVED_LOG_TYPE_2`)
  * Salesforce (`SALESFORCE`)
  * SAP Sybase Adaptive Server Enterprise Database (`SAP_ASE`)
  * Sentinelone Alerts (`SENTINELONE_ALERT`)
  * Snort (`SNORT_IDS`)
  * Solaris system (`SOLARIS_SYSTEM`)
  * Sourcefire (`SOURCEFIRE_IDS`)
  * Suricata IDS (`SURICATA_IDS`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Symantec Event export (`SYMANTEC_EVENT_EXPORT`)
  * Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
  * TrendMicro Apex Central (`TRENDMICRO_APEX_CENTRAL`)
  * Twingate (`TWINGATE`)
  * Wazuh (`WAZUH`)
  * Windows DHCP (`WINDOWS_DHCP`)
  * Windows Event (`WINEVTLOG`)
  * Windows Network Policy Server (`WINDOWS_NET_POLICY_SERVER`)
  * Windows Sysmon (`WINDOWS_SYSMON`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, if applicable.

  * Addigy MDM (`ADDIGY_MDM`)
  * Akamai DataStream 2 (`AKAMAI_DATASTREAM_2`)
  * Anzenna (`ANZENNA`)
  * AWS ECS Metrics (`AWS_ECS_METRICS`)
  * Azure Log Analytics Workspace (`AZURE_LOG_ANALYTICS_WORKSPACE`)
  * Blockdaemon API (`BLOCKDAEMON_API`)
  * Chronicle Feed (`CHRONICLE_FEED`)
  * Claroty xDome Secure Access (`CLAROTY_XDOME_SECURE_ACCESS`)
  * Cloudflare Spectrum (`CLOUDFLARE_SPECTRUM`)
  * Cloudsek Alerts (`CLOUDSEK_ALERTS`)
  * CloudWaves Sensato Nightingale Honeypot (`SENSATO_HONEYPOT`)
  * Docker Hub Activity (`DOCKER_HUB_ACTIVITY`)
  * Fortinet FortiDDoS (`FORTINET_FORTIDDOS`)
  * Honeywell Cyber Insights (`HONEYWELL_CYBERINSIGHTS`)
  * IPFire (`IPFIRE`)
  * Jamf Connect (`JAMF_CONNECT`)
  * KnowBe4 Audit Log (`KNOWBE4`)
  * LogicGate (`LOGICGATE`)
  * ManageEngine NCM (`MANAGEENGINE_NCM`)
  * Microsoft Dotnet Log Files (`MICROSOFT_DOTNET`)
  * Nessus Network Monitor (`NESSUS_NETWORK_MONITOR`)
  * Netography Fusion (`NETOGRAPHY_FUSION`)
  * Netwrix StealthAudit (`NETWRIX_STEALTHAUDIT`)
  * Oomnitza (`OOMNITZA`)
  * Open CTI Platform (`OPENCTI`)
  * Oracle EBS (`ORACLE_EBS`)
  * Oracle Zero Data Loss Recovery Appliance (`ORACLE_ZDLRA`)
  * PhishAlarm (`PHISHALARM`)
  * Savvy Security (`SAVVY_SECURITY`)
  * Symantec Security Analytics (`SYMANTEC_SA`)
  * Venafi ZTPKI (`VENAFI_ZTPKI`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## February 06, 2025

Change

The collector ID representing Google Cloud [direct ingestion](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs) in the Cloud Monitoring metrics and BigQuery has changed from `dddddddd-dddd-dddd-dddd-dddddddddddd` to `aaaa3333-aaaa-3333-aaaa-3333aaaa3333`.

For a complete list of updated collector IDs used for ingestion metrics, see [Use Cloud Monitoring for ingestion notifications](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics).

## February 05, 2025

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have changed. Each parser is listed by product name and `log_type` value, if applicable. This list now includes both released default parsers and pending parser updates.

  * A10 Load Balancer (`A10_LOAD_BALANCER`)
  * Akamai Enterprise Application Access (`AKAMAI_EAA`)
  * Akamai WAF (`AKAMAI_WAF`)
  * Apache (`APACHE`)
  * Apache Tomcat (`TOMCAT`)
  * AppOmni (`APPOMNI`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * Aruba (`ARUBA_WIRELESS`)
  * Aruba Airwave (`ARUBA_AIRWAVE`)
  * Atlassian Cloud Admin Audit (`ATLASSIAN_AUDIT`)
  * Attivo Networks (`ATTIVO`)
  * Auth0 (`AUTH_ZERO`)
  * Avigilon Access Logs (`AVIGILON_ACCESS_LOGS`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS GuardDuty (`GUARDDUTY`)
  * AWS RDS (`AWS_RDS`)
  * AWS Security Hub (`AWS_SECURITY_HUB`)
  * AWS VPC Flow (`AWS_VPC_FLOW`)
  * Azure AD (`AZURE_AD`)
  * Azure Application Gateway (`AZURE_GATEWAY`)
  * Azure Cosmos DB (`AZURE_COSMOS_DB`)
  * Azure Firewall (`AZURE_FIREWALL`)
  * Azure Front Door (`AZURE_FRONT_DOOR`)
  * Bindplane Agent (`BINDPLANE_AGENT`)
  * BloxOne Threat Defense (`BLOXONE`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Cato Networks (`CATO_NETWORKS`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Check Point Harmony (`CHECKPOINT_HARMONY`)
  * CircleCI (`CIRCLECI`)
  * Cisco AMP (`CISCO_AMP`)
  * Cisco Application Centric Infrastructure (`CISCO_ACI`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Email Security (`CISCO_EMAIL_SECURITY`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco NX-OS (`CISCO_NX_OS`)
  * Cisco Umbrella DNS (`UMBRELLA_DNS`)
  * Cisco Umbrella Web Proxy (`UMBRELLA_WEBPROXY`)
  * Cisco vManage SD-WAN (`CISCO_SDWAN`)
  * Cisco VPN (`CISCO_VPN`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Cloudflare (`CLOUDFLARE`)
  * Cloudflare Warp (`CLOUDFLARE_WARP`)
  * CrowdStrike Detection Monitoring (`CS_DETECTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CrowdStrike Falcon Stream (`CS_STREAM`)
  * Crowdstrike Identity Protection Services (`CS_IDP`)
  * Dell CyberSense (`DELL_CYBERSENSE`)
  * Duo Administrator Logs (`DUO_ADMIN`)
  * Elastic Packet Beats (`ELASTIC_PACKETBEATS`)
  * Elastic Windows Event Log Beats (`ELASTIC_WINLOGBEAT`)
  * ExtraHop RevealX (`EXTRAHOP`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * F5 Distributed Cloud Services (`F5_DCS`)
  * Fastly CDN (`FASTLY_CDN`)
  * Forcepoint DLP (`FORCEPOINT_DLP`)
  * Forcepoint Proxy (`FORCEPOINT_WEBPROXY`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortinet FortiClient (`FORTINET_FORTICLIENT`)
  * Fortinet FortiDDoS (`FORTINET_FORTIDDOS`)
  * Fortinet FortiEDR (`FORTINET_FORTIEDR`)
  * Fortinet Proxy (`FORTINET_WEBPROXY`)
  * GitHub (`GITHUB`)
  * Gitlab (`GITLAB`)
  * HP Linux (`HP_LINUX`)
  * IBM Guardium (`GUARDIUM`)
  * Imperva (`IMPERVA_WAF`)
  * Juniper MX Router (`JUNIPER_MX`)
  * Kemp Load Balancer (`KEMP_LOADBALANCER`)
  * Linkshadow NDR (`LINKSHADOW_NDR`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * McAfee Web Gateway (`MCAFEE_WEBPROXY`)
  * McAfee Web Protection (`MCAFEE_WEB_PROTECTION`)
  * Micro Focus iManager (`MICROFOCUS_IMANAGER`)
  * Microsoft Azure NSG Flow (`AZURE_NSG_FLOW`)
  * Microsoft Azure Resource (`AZURE_RESOURCE_LOGS`)
  * Microsoft CyberX (`CYBERX`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Dynamics 365 User Activity (`MICROSOFT_DYNAMICS_365`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft Netlogon (`MICROSOFT_NETLOGON`)
  * Microsoft PowerShell (`POWERSHELL`)
  * Microsoft System Center Endpoint Protection (`MICROSOFT_SCEP`)
  * Mikrotik Router (`MIKROTIK_ROUTER`)
  * Mimecast URL Logs (`MIMECAST_URL_LOGS`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * Okta User Context (`OKTA_USER_CONTEXT`)
  * Open LDAP (`OPENLDAP`)
  * Open Policy Agent (`OPA`)
  * Oracle (`ORACLE_DB`)
  * Oracle Cloud Guard (`OCI_CLOUDGUARD`)
  * Orca Cloud Security Platform (`ORCA`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Networks IoT Security (`PAN_IOT`)
  * Palo Alto Prisma Cloud Alert payload (`PAN_PRISMA_CA`)
  * ProFTPD (`PROFTPD`)
  * Proofpoint Observeit (`OBSERVEIT`)
  * Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
  * ProofPoint Secure Email Relay (`PROOFPOINT_SER`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Proofpoint Threat Response (`PROOFPOINT_TRAP`)
  * RSA SecurID Access Identity Router (`RSA_SECURID`)
  * Rubrik (`RUBRIK`)
  * Salesforce (`SALESFORCE`)
  * Security Command Center Threat (`N/A`)
  * Sentry (`SENTRY`)
  * ServiceNow Audit (`SERVICENOW_AUDIT`)
  * ServiceNow CMDB (`SERVICENOW_CMDB`)
  * Smartsheet (`SMARTSHEET`)
  * Snare System Diagnostic Logs (`SNARE_SOLUTIONS`)
  * Snowflake (`SNOWFLAKE`)
  * Solaris system (`SOLARIS_SYSTEM`)
  * SonicWall (`SONIC_FIREWALL`)
  * Sophos Central (`SOPHOS_CENTRAL`)
  * Sophos UTM (`SOPHOS_UTM`)
  * Sourcefire (`SOURCEFIRE_IDS`)
  * Suricata EVE (`SURICATA_EVE`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Symantec Endpoint Protection (`SEP`)
  * Symantec Event export (`SYMANTEC_EVENT_EXPORT`)
  * Symantec Web Security Service (`SYMANTEC_WSS`)
  * Sysdig (`SYSDIG`)
  * Tableau (`TABLEAU`)
  * Tanium Asset (`TANIUM_ASSET`)
  * Tanium Threat Response (`TANIUM_THREAT_RESPONSE`)
  * tenable.io (`TENABLE_IO`)
  * Trend Micro (`TIPPING_POINT`)
  * Trend Micro Deep Security (`TRENDMICRO_DEEP_SECURITY`)
  * Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
  * TrendMicro Deep Discovery Inspector (`TRENDMICRO_DDI`)
  * UberAgent (`UBERAGENT`)
  * Unix system (`NIX_SYSTEM`)
  * Vectra Detect (`VECTRA_DETECT`)
  * Vectra Stream (`VECTRA_STREAM`)
  * Venafi ZTPKI (`VENAFI_ZTPKI`)
  * Vercel WAF (`VERCEL_WAF`)
  * Virtru Email Encryption (`VIRTRU_EMAIL_ENCRYPTION`)
  * WatchGuard (`WATCHGUARD`)
  * Wazuh (`WAZUH`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Windows Network Policy Server (`WINDOWS_NET_POLICY_SERVER`)
  * Zendesk CRM (`ZENDESK_CRM`)
  * ZeroFox Platform (`ZEROFOX_PLATFORM`)
  * Zimperium (`ZIMPERIUM`)
  * Zoom Operation Logs (`ZOOM_OPERATION_LOGS`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * Zscaler Internet Access Audit Logs (`ZSCALER_INTERNET_ACCESS`)
  * Zscaler Secure Private Access Audit Logs (`ZSCALER_ZPA_AUDIT`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, if applicable.

  * Arcon PAM (`ARCON_PAM`)
  * Azure VNET Flow (`AZURE_VNET_FLOW`)
  * Cameyo Activity Logs (`CAMEYO_ACTIVITY_LOGS`)
  * ChromeOS XDR (`CHROMEOS_XDR`)
  * Cisco Vulnerability Management (`CISCO_VULNERABILITY_MANAGEMENT`)
  * Cloudflare Network Analytics (`CLOUDFLARE_NETWORK_ANALYTICS`)
  * Draytek Router (`DRAYTEK_ROUTER`)
  * FA Solutions (`FA_SOLUTIONS`)
  * Files dot com (`FILES_DOT_COM`)
  * Fortinet ADC (`FORTINET_ADC`)
  * FoxPass Audit Logs (`FOXPASS_AUDIT_LOGS`)
  * Front (`FRONT`)
  * Ghangor DLP (`GHANGOR_DLP`)
  * Hillstone Firewall (`HILLSTONE_NGFW`)
  * Hoxhunt (`HOXHUNT`)
  * Huawei NextGen Firewall (`HUAWEI_FIREWALL`)
  * Huawei Fusion Sphere Hypervisor (`HUAWEI_FUSIONSPHERE`)
  * IBM Security Verify Access (`IBM_SVA`)
  * Indusface WAF (`INDUSFACE_WAF`)
  * Informatica (`INFORMATICA`)
  * Informatica Powercenter (`INFORMATICA_POWERCENTER`)
  * Intel Endpoint Management Assistant (`INTEL_EMA`)
  * Jamf Protect Telemetry V2 (`JAMF_TELEMETRY_V2`)
  * JiranSecurity MailScreen (`JIRANSECURITY_MAILSCREEN`)
  * Juniper SSR Conductor (`JUNIPER_SSR_CONDUCTOR`)
  * Metabase (`METABASE`)
  * Netlify Log Drains (`NETLIFY_LOGDRAINS`)
  * Pingcap TIDB (`PINGCAP_TIDB`)
  * PingOne Advanced Identity Cloud (`PINGONE_AIC`)
  * PingOne Protect (`PINGONE_PROTECT`)
  * Privacy-I (`PRIVACY_I`)
  * ReviveSec (`REVIVESEC`)
  * Sangfor Proxy (`SANGFOR_PROXY`)
  * SoftEther VPN (`SOFTETHER_VPN`)
  * Tehtris EDR (`TEHTRIS_EDR`)
  * TrendMicro Cloud Email Gateway Protection (`TRENDMICRO_CLOUD_EMAIL_GATEWAY_PROTECTION`)
  * VMware VeloCloud SD-WAN (`VELOCLOUD_SDWAN`)
  * Wing Security (`WING_SECURITY`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## January 28, 2025

Feature

**Environment groups**

This feature lets you group environments into logical categories, making it easier to manage your company or your customers as an MSSP.

You can use environment groups for adding users, mapping IdP user groups, creating new playbooks, and applying case filters on the platform.   
For more information about how to create groups of environments, see [Create environment groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/environment-groups).

Change

**Adding individual emails to IdP group mapping page**

Customers who use Cloud Identity Provider can map individual user emails on the IdP group mapping page.

Announcement

**Added instructions on how to add SIEM-only or SOAR-only users to Google SecOps**

For details about how to grant permission to specific users to use only the SIEM features in Google SecOps or only the SOAR features of Google SecOps, see [Add SIEM or SOAR users](https://docs.cloud.google.com/chronicle/docs/secops/enable-soar-access).

## January 26, 2025

Deprecated

**Security Enhancement**   
As of February 10, 2025, concurrent logins to Google SecOps with multiple user accounts using the same browser profile will no longer be supported. Use separate browser profiles or an incognito/private window for each account.

## January 23, 2025

Feature

The following new YARA-L 2.0 functions are available in Rules and Search:

  * arrays.concat
  * arrays.join_string
  * arrays.max
  * arrays.min
  * arrays.size
  * arrays.index_to_int
  * cast.as_bool
  * cast.as_float
  * math.ceil
  * math.floor
  * math.geo_distance
  * math.is_increasing
  * math.pow
  * math.random
  * strings.contains
  * strings.count_substrings
  * strings.extract_domain
  * strings.extract_hostname
  * strings.from_hex
  * strings.ltrim
  * strings.reverse
  * strings.rtrim
  * strings.trim
  * strings.url_decode
  * timestamp.as_unix_seconds
  * timestamp.now



The following new YARA-L 2.0 functions are available in Rules:

  * hash.sha256
  * window.avg
  * window.first
  * window.last
  * window.median
  * window.mode
  * window.stddev
  * window.variance



Details on function signatures and behavior can be found in [YARA-L2.0 Function Syntax Reference Documentation](https://docs.cloud.google.com/chronicle/docs/yara-l/functions#windowvariance).

Change

The Google SecOps team identified that a cloud threat detection rule pack (azure-defender-for-cloud-vm-extensions) was inadvertently made available to all customers. The licensing requirements restrict the availability of this rule pack to only Enterprise and Enterprise+ customers and this has been corrected. 

This change should not remove any prior detections for customers who have enabled this rule pack and do not meet the licensing requirements but the rules themselves will now be unavailable and no new detections will generate.

Deprecated

After July 2025, the **Enterprise Insights** page and the CBN alerts will no longer be available. Use the **Alerts and IOCs** page to view the alerts. We recommend that you [migrate the existing CBN alerts to the YARA-L detection engine](https://docs.cloud.google.com/chronicle/docs/detection/migrate-cbn-alerts).

Change

The prioritization logic of Applied Threat Intelligence (ATI) rule set has been improved to remove alerts from events that have a specified security result action of BLOCKED or QUARANTINED. This change only impacts the IP address indicator types for both High and Active Breach priority. For more information, see [View details about rule sets](https://docs.cloud.google.com/chronicle/docs/detection/curated-detections#enable-configure).

## January 21, 2025

Change

The following rules have been moved from "Precise" to "Broad" in their associated rule packs due to high alert volume across the Google SecOps customer base. 

  * GCP Workspace Data Exfil Drive: 
    * Suspicious Workspace Actions Observed after a Successful Suspicious Login
  * GCP Suspicious Infrastructure Change: 
    * Replacement of Existing Compute Machine Image
    * Replacement of Existing Compute Disk
  * GCP Cloud SQL Ransom: 
    * Base64 Encoded Cloud SQL Command
  * CIDR SCC Persistence: 
    * SCC: Persistence: New API Method
    * SCC: Persistence: IAM Anomalous Grant
    * SCC: Persistence: GCE Admin Added SSH Key
  * CIDR SCC Malware: 
    * SCC: Added Library Loaded
    * SCC: Added Binary Executed
  * CIDR SCC Cloud IDS Low: 
    * SCC: Cloud IDS: Low Threat Finding
  * CIDR SCC Cloud Armor Medium: 
    * SCC: Cloud Armor: Medium - Increasing Deny Ratio
    * SCC: Cloud Armor: Medium - Allowed Traffic Spike
  * Azure Identity: 
    * Azure External User Invitation
  * Azure Defender for Cloud Windows and Linux VM: 
    * Azure Defender for Cloud: Anonymous IP access
  * AWS GuardDuty Discovery: 
    * AWS GuardDuty: Recon:EC2/PortProbeUnprotectedPort



## January 20, 2025

Deprecated

Python 3.7 is being deprecated and will be fully removed on June 1, 2025.

For information on how to update Marketplace integrations to Python 3.11, refer to [Upgrade the Python versions](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/upgrade-python-versions).

## January 19, 2025

Change

The individual parser documents have been put into [one page](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration) with an easy-to-use search bar. This reorganization helps you find all the information you need in one place.

## January 14, 2025

Change

The following rules have been removed from their associated rule packs in Curated Detections due to high alert volume across the Google SecOps customer base:

  * Cloud Threats - CDIR SCC Enhanced Defense Evasion Alerts: 
    * SCC: Modify VPC Service Control with GCE Activity from the Restricted Resource
    * SCC: Modify VPC Service Control with Activity from the Restricted Service
  * Linux Threats - OS Privilege Escalation Tools: 
    * Sensitive File Discovery
    * Last Login Users
    * Whoami Commands
  * Windows Threats - Initial Access: 
    * NetLogon AD System Event
  * Risk Analytics for UEBA - Login to an Application Never Before Seen for a User Group: 
    * First Time User Login Activity to Application for Manager Peer Group
  * Risk Analytics for UEBA - Login from Country Never Before Seen for a User Group: 
    * First Time User Login Activity from Country for Manager Peer Group



The rule "SCC: Unexpected Child Shell" has been moved from the rule pack "Cloud Threats - CDIR SCC Enhanced Malware Alerts" to "Cloud Threats - CDIR SCC Enhanced Execution Alerts"

## January 11, 2025

Change

Playbook names must now be unique across all SOAR environments, as part of updates to support future features. For customers with existing playbooks in different environments that have the same name, there is no need to manually change names. However, the next time you edit one of these playbooks, you will be asked to change the name before you save.

Change

The user must log in to the Google SecOps platform with the exact same IdP group name as entered in the Settings screen.

## January 07, 2025

Announcement

The following parser documentation is now available:

[Collect Microsoft Defender for Endpoint logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-microsoft-defender-endpoint)

[Zscaler parsers overview](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-zscaler-logs)

[Collect Zscaler DNS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-dns-logs)

[Collect Zscaler Firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-firewall-logs)

[Collect Zscaler Internet Access logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-internet-access-logs)

[Collect Zscaler Webproxy logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-zscaler-webproxy-logs)

[Collect Linux auditd and AIX systems logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/auditd)

[Collect CircleCI audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/circleci)

[Collect CloudPassage Halo logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudpassage-halo)

[Collect JFrog Artifactory logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jfrog-artifactory)

[Collect Apple macOS syslog data](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/macos)

[Collect Netskope web proxy logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-wp)

[Collect Onfido logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onfido)

[Collect OPNsense firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/opnsense-fw)

[Collect Rapid7 InsightIDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rapid7-insightidr)

[Collect Sysdig logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sysdig)

[Collect Thinkst Canary logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/thinkst-canary)

[Collect VMware Workspace ONE UEM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-workspaceone-uem)

[Collect Workday HCM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday-hcm)

## December 27, 2024

Change

Google SecOps has added a new rule set to Applied Threat Intelligence (ATI), called Inbound IP Address Authentication, that identifies IP addresses that are authenticating to local infrastructure in an inbound network direction. For more information, see [Applied Threat Intelligence priority overview](https://docs.cloud.google.com/chronicle/docs/detection/ati-prioritization).

## December 23, 2024

Announcement

The following parser documentation is now available:

[Collect CrowdStrike Detection logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-cs-detects)

[Collect Microsoft Azure AD Audit logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-audit)

[Collect Microsoft Azure AD Context logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad-context)

[Ingest Chrome Enterprise Premium data to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-bce)

[Collect Ansible AWX logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ansible-awx)

[Collect Atlassian Bitbucket logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-bitbucket)

[Collect Atlassian Jira logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-jira)

[Collect Auth0 logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/auth-zero)

[Collect Azion firewall logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azion)

[Collect Azure DevOps audit logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-devops)

[Collect GitHub audit logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/github)

[Collect GitLab logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gitlab)

[Collect Microsoft Defender for Cloud alert logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ms-defender-cloud-alerts)

[Collect Microsoft Graph activity logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ms-graph-activity-logs)

[Collect Microsoft Sentinel logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ms-sentinel)

[Collect Twingate VPN logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/twingate)

[Collect Wordpress CMS logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wordpress-cms)

[Collect CrowdStrike IOC logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crowdstrike-ioc)

[Collect Jenkins logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jenkins)

[Collect Wazuh logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wazuh)

[Collect OpenCanary logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/opencanary)

[Collect Synology logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/synology)

[Collect Palo Alto Networks IOC logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-ioc)

[Collect Fastly WAF logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fastly-waf)

[Collect MISP IOC logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/misp)

[Collect ntopng logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ntopng)

[Collect Cloudflare logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare)

[Collect Palo Alto Prisma Cloud alert logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-cloud-alert)

[Collect ServiceNow Security logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-security)

[Collect Akamai WAF logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-waf)

[Collect Aqua Security logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aqua-security)

[Collect Cohesity logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cohesity)

[Collect Datadog logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/datadog)

[Collect Lacework Cloud Security logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lacework)

[Collect Netskope alert logs v1 ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-alert-v1)

[Collect Netskope alert logs v2 ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-alert-v2)

[Collect Nutanix Prism logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nutanix-prism)

[Collect Salesforce logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/salesforce)

[Collect Trend Micro Cloud One logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-cloudone)

[Collect VMware ESXi logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-esxi)

[Collect WatchGuard Fireware logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/watchguard-fireware)

## December 22, 2024

Change

This release note has been updated. Refer to the entry for [February 11, 2025](https://docs.cloud.google.com/chronicle/docs/secops/release-notes#February_11_2025) for the latest information.

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have changed. Each parser is listed by product name and `log_type` value, if applicable. This list now includes both released default parsers and pending parser updates.

  * Absolute Mobile Device Management (`Mobile Device Management`)
  * Atlassian Cloud Admin Audit (`Audit`)
  * AWS VPC Flow (`AWS Specific`)
  * Azure AD (`LDAP`)
  * Azure Application Gateway (`GATEWAY`)
  * Azure SQL (`Database`)
  * Azure Storage Audit (`Storage`)
  * Blue Coat Proxy (`Web Proxy`)
  * Check Point Harmony (`Remote Access Tools`)
  * Cisco ASA (`firewall`)
  * Cisco Firepower NGFW (`Firewall`)
  * Cisco Meraki (`Wireless`)
  * Cisco Router (`Switches, Routers`)
  * Cisco Umbrella SWG DLP (`DLP`)
  * Cisco VPN (`VPN`)
  * Citrix Netscaler (`Load Balancer, Traffic Shaper, ADC`)
  * Claroty Continuous Threat Detection (`IoT`)
  * Cloud Audit Logs (`Google Cloud Specific`)
  * Cloud DNS (`Google Cloud Specific`)
  * Code42 Incydr (`Data loss prevention (DLP)`)
  * Colinet Trotta GAUS SEGUROS (`Alert`)
  * CrowdStrike Falcon (`EDR`)
  * Delinea Distributed Engine (`Application server logs`)
  * Druva Backup (`Security`)
  * Duo Administrator Logs (`Authentication`)
  * Elastic Audit Beats (`ALERTING`)
  * F5 BIGIP LTM (`Load Balancer, Traffic Shaper, ADC`)
  * Forcepoint NGFW (`Network`)
  * FortiGate (`Firewall`)
  * GitHub (`SaaS Application`)
  * Google Cloud Identity Context (`Identity and Access Management`)
  * Guardicore Centra (`Deception Software`)
  * HPE Aruba Networking Central (`Data Security`)
  * Imperva Advanced Bot Protection (`Bot Protection`)
  * Kubernetes Audit Azure (`Log Aggregator`)
  * Linux Auditing System (AuditD) (`OS`)
  * Maria Database (`Database`)
  * Microsoft Defender for Endpoint (`EDR`)
  * Opnsense (`Firewall and Routing Platform`)
  * Oracle NetSuite (`CASB`)
  * Palo Alto Panorama (`Firewall`)
  * Palo Alto Prisma Cloud Alert payload (`Cloud Security`)
  * Ping One (`NA`)
  * Proofpoint Observeit (`Email Server`)
  * Proofpoint Threat Response (`Email Server`)
  * QNAP Systems NAS (`Storage solutions`)
  * Reserved LogType2 (`LDAP`)
  * Salesforce (`SaaS Application`)
  * SAP Sybase Adaptive Server Enterprise Database (`Database`)
  * Sentinelone Alerts (`Endpoint Security`)
  * Snort (`IDS/IPS`)
  * Solaris system (`OS`)
  * Sourcefire (`IDS/IPS`)
  * Suricata IDS (`IDS/IPS`)
  * Symantec DLP (`DLP`)
  * Symantec Event export (`SEP`)
  * Trend Micro Vision One (`AV and endpoint logs`)
  * TrendMicro Apex Central (`Endpoint`)
  * Twingate (`VPN`)
  * Wazuh (`Log Aggregator`)
  * Windows DHCP (`DHCP`)
  * Windows Event (`Endpoint`)
  * Windows Network Policy Server (`Authentication`)
  * Windows Sysmon (`DNS`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, if applicable.

  * Addigy MDM (`ADDIGY_MDM`)
  * Akamai DataStream 2 (`AKAMAI_DATASTREAM_2`)
  * Anzenna (`ANZENNA`)
  * AWS ECS Metrics (`AWS_ECS_METRICS`)
  * Azure Log Analytics Workspace (`AZURE_LOG_ANALYTICS_WORKSPACE`)
  * Blockdaemon API (`BLOCKDAEMON_API`)
  * Chronicle Feed (`CHRONICLE_FEED`)
  * Claroty xDome Secure Access (`CLAROTY_XDOME_SECURE_ACCESS`)
  * Cloudflare Spectrum (`CLOUDFLARE_SPECTRUM`)
  * Cloudsek Alerts (`CLOUDSEK_ALERTS`)
  * CloudWaves Sensato Nightingale Honeypot (`SENSATO_HONEYPOT`)
  * Docker Hub Activity (`DOCKER_HUB_ACTIVITY`)
  * Fortinet FortiDDoS (`FORTINET_FORTIDDOS`)
  * Honeywell Cyber Insights (`HONEYWELL_CYBERINSIGHTS`)
  * IPFire (`IPFIRE`)
  * Jamf Connect (`JAMF_CONNECT`)
  * KnowBe4 Audit Log (`KNOWBE4`)
  * LogicGate (`LOGICGATE`)
  * ManageEngine NCM (`MANAGEENGINE_NCM`)
  * Microsoft Dotnet Log Files (`MICROSOFT_DOTNET`)
  * Nessus Network Monitor (`NESSUS_NETWORK_MONITOR`)
  * Netography Fusion (`NETOGRAPHY_FUSION`)
  * Netwrix StealthAudit (`NETWRIX_STEALTHAUDIT`)
  * Oomnitza (`OOMNITZA`)
  * Open CTI Platform (`OPENCTI`)
  * Oracle EBS (`ORACLE_EBS`)
  * Oracle Zero Data Loss Recovery Appliance (`ORACLE_ZDLRA`)
  * PhishAlarm (`PHISHALARM`)
  * Savvy Security (`SAVVY_SECURITY`)
  * Symantec Security Analytics (`SYMANTEC_SA`)
  * Venafi ZTPKI (`VENAFI_ZTPKI`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## December 17, 2024

Change

**Looker dashboard updates**

The following changes have been made to the Looker dashboards in Google SecOps:

  * All dashboards have been moved to the `ingestion_metrics_connector` explore.

  * The `ingestion_stats`, `ingestion_metric_with_ingestion_stats` and `ingestion_metrics` explores are no longer supported.

  * The `total_entry_number` and `total_size_bytes` fields are defined in the new explore and used to query the log count and log volume for the Google SecOps Ingestion API. For more information, see the [Ingestion metrics field reference for dashboards](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-metrics-explore).

  * The default dashboards for **Context aware detections risk** and **Cloud detection and response overview** have been updated to use a different field for the risk score. It was `rule_detections.outcomes['risk_score']` and is now `rule_detections.risk_score`. This change aligns the risk score in the Google SecOps dashboards to the risk score used in the Google SecOps user interface.

  * The `severity` field in the **Rules and detections** default **Dashboard** has been updated so that it would show the severity for both Curated Detections and custom rules.




## December 09, 2024

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have changed. Each parser is listed by product name and `log_type` value, if applicable. This list now includes both released default parsers and pending parser updates.

  * 1Password Audit Events (`Identity and Access Management`)
  * Advanced Intrusion Detection Environment (`Alert`)
  * Airlock Digital Application Allowlisting (`Application Whitelisting`)
  * Akamai DNS (`DNS`)
  * Amazon VPC Transit Gateway Flow Logs (`Network`)
  * Apache Tomcat (`Web server`)
  * Appian Cloud (`Collaboration log types`)
  * AppOmni (`SAAS Security Application`)
  * Aruba Switch (`Network Infrastructure`)
  * Auth0 (`Authentication log`)
  * AWS Cloudtrail (`Cloud Log Aggregator`)
  * AWS CloudWatch (`Cloud service monitoring`)
  * AWS Elastic Load Balancer (`AWS Specific`)
  * AWS GuardDuty (`IDS/IPS`)
  * AWS Network Firewall (`Firewall`)
  * AWS RDS (`Database`)
  * AWS Route 53 DNS (`AWS Specific`)
  * AWS S3 Server Access (`AWS Specific`)
  * AWS VPC Flow (`AWS Specific`)
  * Azure AD Directory Audit (`Audit`)
  * Azure AD Organizational Context (`LDAP`)
  * Azure API Management (`Schema`)
  * Azure App Service (`SAAS`)
  * Azure Application Gateway (`GATEWAY`)
  * Azure Firewall (`Azure Firewall Application Rule`)
  * Azure Key Vault logging (`Audit`)
  * Azure SQL (`Database`)
  * Barracuda WAF (`Firewall`)
  * Barracuda Web Filter (`Webfilter`)
  * BeyondTrust BeyondInsight (`Privileged Account Activity`)
  * BeyondTrust Endpoint Privilege Management (`Privileged Account Activity`)
  * BIND (`DNS`)
  * BloxOne Threat Defense (`DNS`)
  * Blue Coat Proxy (`Web Proxy`)
  * Cato Networks (`NDR`)
  * Check Point (`Firewall`)
  * Ciena Router logs (`Application server logs`)
  * Cisco ACS (`Authentication`)
  * Cisco APIC (`Software-defined Networking (SDN)`)
  * Cisco Call Manager (`NETWORKING`)
  * Cisco DNA Center Platform (`Network Management and Optimization`)
  * Cisco Email Security (`Email Server`)
  * Cisco EStreamer (`Network Monitoring`)
  * Cisco Firepower NGFW (`Firewall`)
  * Cisco FireSIGHT Management Center (`SaaS Application`)
  * Cisco Internetwork Operating System (`Network Infrastructure`)
  * Cisco ISE (`Identity and Access Management`)
  * Cisco Router (`Switches, Routers`)
  * Cisco Secure Workload (`AV and Endpoint`)
  * Cisco Stealthwatch (`Log Aggregator`)
  * Cisco Switch (`Switches, Routers`)
  * Cisco TACACS+ (`Authentication`)
  * Cisco VPN (`VPN`)
  * Citrix Netscaler (`Load Balancer, Traffic Shaper, ADC`)
  * Claroty Continuous Threat Detection (`IoT`)
  * Cloudflare (`SaaS Application`)
  * Colinet Trotta GAUS SEGUROS (`Alert`)
  * CrowdStrike Detection Monitoring (`EDR`)
  * CrowdStrike Falcon (`EDR`)
  * CrowdStrike Falcon Stream (`Alerts`)
  * CrowdStrike Filevantage (`IT infrastructure`)
  * Cyber 2.0 IDS (`IDS`)
  * Cyberark Privilege Cloud (`Identity & Access Management`)
  * CyberArk Privileged Access Manager (PAM) (`CyberArk Privileged Access Manager`)
  * Cybereason EDR (`EDR`)
  * Darktrace (`NDR`)
  * Dell CyberSense (`Data Security`)
  * Dell EMC PowerStore (`DATA STORAGE`)
  * Druva Backup (`Security`)
  * Duo Administrator Logs (`Authentication`)
  * Duo Auth (`Authentication`)
  * EfficientIP DDI (`Network`)
  * ExtraHop RevealX (`Firewall IDS/IPS`)
  * F5 Advanced Firewall Management (`Firewall`)
  * F5 ASM (`WAF`)
  * F5 BIGIP LTM (`Load Balancer, Traffic Shaper, ADC`)
  * F5 VPN (`VPN`)
  * FingerprintJS (`Vulnerability scanners`)
  * FireEye eMPS (`Email server log types.`)
  * FireEye HX (`EDR`)
  * Forcepoint DLP (`Forcepoint DLP`)
  * Forcepoint NGFW (`Network`)
  * Forcepoint Proxy (`Web Proxy`)
  * Forescout NAC (`NAC`)
  * ForgeRock OpenAM (`Identity and Access Management`)
  * Forgerock OpenIdM (`DATA SECURITY`)
  * FortiGate (`Firewall`)
  * Fortinet FortiAnalyzer (`Fortinet FortiAnalyzer`)
  * Fortinet Switch (`Switches and Routers`)
  * GitHub (`SaaS Application`)
  * Guardicore Centra (`Deception Software`)
  * Hashicorp Vault (`Privileged Account Activity`)
  * HCNET Account Adapter Plus (`DHCP`)
  * IBM MaaS360 (`Security`)
  * IBM Security Access Manager (`WAF`)
  * IBM z/OS (`OS`)
  * Illumio Core (`Policy Management`)
  * Imperva (`WAF`)
  * Imperva Advanced Bot Protection (`Bot Protection`)
  * Imperva Attack Analytics (`WAF`)
  * Ingrian Networks DataSecure Appliance (`System and Audit Logs`)
  * Intel 471 Malware Intelligence (``)
  * ISC DHCP (`DHCP`)
  * Jenkins (`Automation and DevOps`)
  * Journald (`Log Aggregation and SIEM Systems`)
  * Juniper (`Firewall`)
  * Juniper Mist (`Network Management and Optimization software`)
  * Juniper MX Router (`Routers and Switches`)
  * Keeper Enterprise Security (`Security`)
  * Kubernetes Audit Azure (`Log Aggregator`)
  * Lacework Cloud Security (`Cloud Security`)
  * Lenel Onguard Badge Management (`Access Control System`)
  * Linux Auditing System (AuditD) (`OS`)
  * Linux Sysmon (`DNS`)
  * ManageEngine Log360 (`Alert Log`)
  * Maria Database (`Database`)
  * McAfee ePolicy Orchestrator (`Policy Management`)
  * McAfee Web Gateway (`Web Proxy`)
  * Microsoft AD (`LDAP`)
  * Microsoft AD FS (`LDAP`)
  * Microsoft Azure Activity (`Misc Windows Specific`)
  * Microsoft Azure NSG Flow (`Network Flow`)
  * Microsoft Azure Resource (`Log Aggregator`)
  * Microsoft Defender Endpoint for iOS Logs (``)
  * Microsoft Defender for Endpoint (`EDR`)
  * Microsoft PowerShell (`Misc. Windows-specific`)
  * Microsoft SQL Server (`Database`)
  * Microsoft System Center Endpoint Protection (`Malware Detection`)
  * Mikrotik Router (`Router`)
  * Mimecast (`Email Server`)
  * MISP Threat Intelligence (`Cybersecurity`)
  * Mobile Endpoint Security (`Mobile Endpoint Security`)
  * Mobileiron (`ENDPOINT MANAGEMENT`)
  * NetApp BlueXP (`Security`)
  * Nozomi Networks Scada Guardian (`Network Monitoring`)
  * Office 365 (`SaaS Application`)
  * Okta (`Identity and Access Management`)
  * OpenVPN (`Network`)
  * Opnsense (`Firewall and Routing Platform`)
  * Opswat Metadefender (`Threat Protection`)
  * Oracle (`DATABASE`)
  * Oracle Cloud Infrastructure Audit Logs (`Oracle Cloud Infrastructure`)
  * Oracle Fusion (`SaaS Application`)
  * Oracle WebLogic Server (`Web server logs`)
  * Palo Alto Cortex XDR Alerts (`NDR`)
  * Palo Alto Prisma Cloud (`SECURITY PLATFORM`)
  * Palo Alto Prisma Cloud Alert payload (`Cloud Security`)
  * Ping Federate (`Authentication`)
  * Ping Identity (`Authentication`)
  * Ping One (`NA`)
  * PingIdentity Directory Server Logs (`Security`)
  * Precisely Ironstream IBM z/OS (`ZOS`)
  * ProFTPD (`Web Server`)
  * Proofpoint Observeit (`Email Server`)
  * Proofpoint On Demand (`Email Server`)
  * ProofPoint Secure Email Relay (`Email server`)
  * Proofpoint Tap Forensics (`Email Server`)
  * Quest Active Directory (`Authentication log`)
  * Red Hat Directory Server LDAP (`Identity and Access Management`)
  * Remediant SecureONE (`Privileged Account Activity`)
  * Salesforce (`SaaS Application`)
  * SAP Sybase Adaptive Server Enterprise Database (`Database`)
  * Security Command Center Posture Violation (`Google Cloud Specific`)
  * Security Command Center Threat (`Google Cloud Specific`)
  * Security Command Center Toxic Combination (`Google Cloud Specific`)
  * Sentinelone Alerts (`Endpoint Security`)
  * Shibboleth IDP (`Identity and Access Management`)
  * Snare System Diagnostic Logs (`Security`)
  * Snipe-IT (`SaaS Applications`)
  * Snort (`IDS/IPS`)
  * SonicWall (`Firewall`)
  * Squid Web Proxy (`Web Proxy`)
  * STIX Threat Intelligence (`Cybersecurity Threats`)
  * Suricata EVE (`IPS IDS`)
  * Symantec CloudSOC CASB (`CASB`)
  * Symantec DLP (`DLP`)
  * Symantec Endpoint Protection (`AV / Endpoint`)
  * Symantec Event export (`SEP`)
  * Symantec Web Security Service (`Web Proxy`)
  * Sysdig (`Security`)
  * Tailscale (`CASB`)
  * Tanium Threat Response (`Tanium Specific`)
  * TeamViewer (`Remote Support`)
  * Tenable CSPM (`Cloud Security`)
  * Tenable Security Center (`Vulnerability Scanner`)
  * Thales Luna Hardware Security Module (`THALES_LUNA_HSM specific`)
  * Trellix HX Event Streamer (`Cybersecurity`)
  * Trend Micro Deep Security (`AV / Endpoint`)
  * Trend Micro Vision One (`AV and endpoint logs`)
  * Trend Micro Vision One Workbench (`Schema`)
  * TrendMicro Deep Discovery Inspector (`Physical and virtual network`)
  * Tripwire (`DLP`)
  * TXOne Stellar (`AV and Endpoint logs`)
  * UberAgent (`Security`)
  * Unix system (`OS`)
  * UpGuard (`Vulnerability scanners`)
  * Upstream Vehicle SOC Alerts (`Schema`)
  * URLScan IO (`Vulnerability scanners`)
  * Veeam (`Backup software`)
  * VMware AirWatch (`Wireless`)
  * VMware Horizon (`VDI`)
  * VMware vCenter (`Server`)
  * VMWare VSphere (`virtualization`)
  * VPC Flow Logs (`Google Cloud Specific`)
  * Wallix Bastion (`Privileged Account Activity`)
  * WindChill (`Lifecycle Management Software`)
  * Windows Event (`Endpoint`)
  * Windows Event (XML) (`AV / Endpoint`)
  * Windows Sysmon (`DNS`)
  * Workday Audit Logs (`Audit And Compliance`)
  * Workspace Activities (`Google Cloud Specific`)
  * Workspace ChromeOS Devices (`Google Cloud Specific`)
  * Zimperium (`Mobile Device Management`)
  * Zoom Operation Logs (`Operation-Specific`)
  * Zscaler (`Web Proxy`)
  * Zscaler DLP (`Data Loss Prevention`)
  * ZScaler DNS (`DNS`)
  * ZScaler NGFW (`Firewall`)
  * Zscaler NSS Feeds for Alerts (`Alert log types`)
  * Zscaler Private Access (`Security Service Edge`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, if applicable.

  * Arize Cloud (`ARIZE_CLOUD`)
  * Aware Audit (`AWARE_AUDIT`)
  * Aware Signals (`AWARE_SIGNALS`)
  * Azure PostgreSQL (`AZURE_POSTGRESQL`)
  * Cisco Umbrella Firewall (`CISCO_UMBRELLA_FIREWALL`)
  * Cisco Umbrella IPS (`CISCO_UMBRELLA_IPS`)
  * Cisco Umbrella SWG DLP (`CISCO_UMBRELLA_SWG_DLP`)
  * CyberArk Secure Cloud Access (`CYBERARK_SCA`)
  * DBT Cloud (`DBT_CLOUD`)
  * Delinea Distributed Engine (`DELINEA_DISTRIBUTED_ENGINE`)
  * Delinea PBA (`DELINEA_PBA`)
  * Dtex Audit (`DTEX_AUDIT`)
  * Featurespace Aric (`FEATURESPACE_ARIC`)
  * Forcepoint One (`FORCEPOINT_ONE`)
  * Genesys Audit (`GENESYS_AUDIT`)
  * Hex (`HEX`)
  * Linkshadow NDR (`LINKSHADOW_NDR`)
  * Nightfall DLP (`NIGHTFALL`)
  * Palo Alto Cortex IIS (`PAN_CORTEX_XDR_IIS`)
  * Relativity (`RELATIVITY`)
  * Retool (`RETOOL`)
  * Saturn Cloud (`SATURN_CLOUD`)
  * SecurityBridge (`SECURITY_BRIDGE`)
  * TACACS Plus (`TACACS_PLUS`)
  * Transmit Security FlexID (`TRANSMIT_FLEXID`)
  * Unifi Router (`UNIFI_ROUTER`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## November 25, 2024

Feature

Curated Detections has been enhanced with a new detection category, [MacOS Threats](https://docs.cloud.google.com/chronicle/docs/detection/macos-threats-category). The category includes a Mandiant Intel Emerging Threats rulepack.

## November 24, 2024

Feature

**New options for closing a case**

New custom field options have been added to the admin settings close case page. Using these fields, you can ask the analyst to enter different types of information when closing a case. 

For more information, refer to [Customize the Close Case dialog](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/add-new-case-close-root-cause-admin).

## November 09, 2024

Announcement

The following parser documentation is now available. 

[Collect Microsoft Azure AD logs](https://docs.cloud.google.com/chronicle/docs/preview/siem-integrations/azure-ad)

[Collect AWS VPC Flow logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc)

[Collect AWS GuardDuty logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guard-duty)

[Collect Cisco Meraki logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-meraki)

[Collect Cisco Secure Email Gateway logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-email-security)

[Collect Cisco ISE logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ise)

[Collect Cisco Secure ACS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-acs)

[Collect Amazon CloudFront logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudfront-parser)

[Collect AWS RDS logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-rds)

[Collect Cloudflare WAF logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare-waf)

[Collect Forcepoint DLP logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-dlp)

[Collect FortiWeb WAF logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiweb)

[Collect F5 BIG-IP APM logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-apm)

[Collect F5 BIG-IP LTM logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-ltm)

[Collect CrowdStrike EDR logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crowdstrike-edr)

[Collect the General Dynamics Fidelis XPS logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fidelis-network)

[Collect CyberX logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberx)

[Collect Imperva Incapsula Web Application Firewall logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-waf)

[Collect Infoblox logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/infoblox-dns)

[Collect Juniper Junos logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/juniper-junos)

[Collect Microsoft Intune logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-intune)

[Collect Microsoft Graph security API alert logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-graph-alert)

[Collect Kemp Load Balancer logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kemp-load-balancer)

[Collect Mimecast Secure Email Gateway logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mimecast-mail)

[Collect Netgate pfSense logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netgate-pfsense)

[Collect NetScaler logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netscaler)

[Collect Proofpoint TAP alerts logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail)

[Collect Pulse Secure logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pulse-secure-vpn)

[Collect Qualys scan logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-scan)

[Collect RSA Authentication Manager logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rsa-authentication-manager)

[Collect SentinelOne EDR logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinel-edr)

[Collect SonicWall logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-sonicwall)

[Collect Sophos UTM logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-utm)

[Collect Symantec Event Export logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-event-export)

[Collect Tripwire logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tripwire)

[Collect Palo Alto Prisma Cloud logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-cloud)

[Collect Okta logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta)

[Collect Palo Alto Cortex XDR alerts logs ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cortex-xdr)

[Collect CrowdStrike Detection logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-cs-detects)

## October 28, 2024

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have changed. Each parser is listed by product name and `log_type` value, if applicable. This list now includes both released default parsers and pending parser updates.

  * AIX system (`OS`)
  * Apache Tomcat (`Web server`)
  * Apigee (`Google Cloud Specific`)
  * Aqua Security (`IaaS Applications`)
  * Aruba Switch (`Network Infrastructure`)
  * Auth0 (`Authentication log`)
  * AWS Cloudtrail (`Cloud Log Aggregator`)
  * AWS GuardDuty (`IDS/IPS`)
  * AWS RDS (`Database`)
  * AWS Route 53 DNS (`AWS Specific`)
  * AWS VPC Flow (`AWS Specific`)
  * Azure AD (`LDAP`)
  * Azure AD Sign-In (`Misc Windows Specific`)
  * Azure VPN (`VPN`)
  * Blue Coat Proxy (`Web Proxy`)
  * BMC Client Management (`Security`)
  * Checkpoint Audit (`AUDIT`)
  * Chrome Management (`Browser`)
  * Cisco ASA (`firewall`)
  * Cisco Internetwork Operating System (`Network Infrastructure`)
  * Cisco IronPort (`Gateway Security`)
  * Cisco Meraki (`Wireless`)
  * Cisco Router (`Switches, Routers`)
  * Cisco Switch (`Switches, Routers`)
  * Cisco UCM (`Communication Manager`)
  * Cisco Unity Connection (`Administration and Management`)
  * Citrix Netscaler (`Load Balancer, Traffic Shaper, ADC`)
  * Claroty Continuous Threat Detection (`IoT`)
  * Cloud Audit Logs (`Google Cloud Specific`)
  * Cloudflare (`SaaS Application`)
  * CommVault (`Alert System`)
  * CrowdStrike Detection Monitoring (`EDR`)
  * CrowdStrike Falcon (`EDR`)
  * Darktrace (`NDR`)
  * Dell Switch (`Switches, Routers`)
  * Druva Backup (`Security`)
  * Entrust nShield HSM (`Hardware Security Module`)
  * F5 ASM (`WAF`)
  * F5 BIGIP LTM (`Load Balancer, Traffic Shaper, ADC`)
  * Fidelis Network (`NDR`)
  * FireEye (`Alerts`)
  * FireEye HX (`EDR`)
  * FireEye NX (`NDR`)
  * FortiGate (`Firewall`)
  * Fortinet FortiAnalyzer (`Fortinet FortiAnalyzer`)
  * GitGuardian Enterprise (`SaaS Applications`)
  * Guardicore Centra (`Deception Software`)
  * Halcyon Anti Ransomware (`AV and endpoint logs`)
  * Hashicorp Vault (`Privileged Account Activity`)
  * HP Linux (`OS`)
  * IBM Mainframe Storage (`Monitoring`)
  * IBM OpenPages (`Data Security`)
  * IBM Security QRadar SOAR (`Security`)
  * Imperva (`WAF`)
  * Imperva Advanced Bot Protection (`Bot Protection`)
  * Imperva Audit Trail (`IT infrastructure`)
  * Infoblox DHCP (`DHCP`)
  * INTEL471 Watcher Alerts (`Data Security`)
  * Jamf Protect Alerts (`Endpoint Security`)
  * Juniper (`Firewall`)
  * KnowBe4 PhishER (`Email server log types.`)
  * Kubernetes Node (`Kubernetes Container`)
  * Linux Auditing System (AuditD) (`OS`)
  * McAfee ePolicy Orchestrator (`Policy Management`)
  * Microsoft AD (`LDAP`)
  * Microsoft Azure Resource (`Log Aggregator`)
  * Microsoft Defender for Identity (`EDR`)
  * Microsoft Defender for Office 365 (`Email server log types.`)
  * Microsoft Graph Activity Logs (`AUDIT`)
  * Microsoft Netlogon (`Authentication`)
  * Microsoft SQL Server (`Database`)
  * Microsoft System Center Endpoint Protection (`Malware Detection`)
  * Netscope Client (`CASB`)
  * Office 365 (`SaaS Application`)
  * Okta User Context (`Identity and Access Management`)
  * One Identity Identity Manager (`unified identity security`)
  * Opswat Metadefender (`Threat Protection`)
  * Palo Alto Networks Firewall (`Firewall`)
  * Palo Alto Prisma Cloud Alert payload (`Cloud Security`)
  * pfSense (`FIREWALL`)
  * Ping Federate (`Authentication`)
  * Proofpoint Observeit (`Email Server`)
  * ProofPoint Secure Email Relay (`Email server`)
  * Pure Storage (`Data Storage`)
  * Red Hat Directory Server LDAP (`Identity and Access Management`)
  * Salesforce (`SaaS Application`)
  * Salesforce Commerce Cloud (`SaaS Application`)
  * Security Command Center Threat (`Google Cloud Specific`)
  * ServiceNow CMDB (`Policy Management`)
  * Sophos UTM (`Unified Threat Management`)
  * Symantec Endpoint Protection (`AV / Endpoint`)
  * Sysdig (`Security`)
  * Tanium Threat Response (`Tanium Specific`)
  * ThreatX WAF (`WAF`)
  * Thycotic (`Identity and Access Management`)
  * Tines (`Data Security`)
  * Trend Micro (`SMS, UNITY_ONE`)
  * Trend Micro Deep Security (`AV / Endpoint`)
  * Trend Micro Vision One (`AV and endpoint logs`)
  * Twingate (`VPN`)
  * Unix system (`OS`)
  * Velo Firewall (`FIREWALL`)
  * VMware AirWatch (`Wireless`)
  * Windows Defender ATP (`AV / Endpoint`)
  * Windows Event (`Endpoint`)
  * Windows Event (XML) (`AV / Endpoint`)
  * Windows Local Administrator Password Solution (`Local Administrator Password Solution`)
  * Windows Sysmon (`DNS`)
  * Workday Audit Logs (`Audit And Compliance`)
  * Workspace Activities (`Google Cloud Specific`)
  * Workspace Alerts (`Google Cloud Specific`)
  * Zscaler (`Web Proxy`)
  * Zscaler Tunnel (`N/A`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, if applicable.

  * Adobe I/O Runtime (`ADOBE_IO_RUNTIME`)
  * Amazon VPC Transit Gateway Flow Logs (`AWS_VPC_TRANSIT_GATEWAY`)
  * Appsentinels (`APPSENTINELS`)
  * Asset Panda (`ASSET_PANDA`)
  * AstriX (`ASTRIX`)
  * Atlan (`ATLAN`)
  * Azure Container Registry (`AZURE_CONTAINER_REGISTRY`)
  * Backbase Engagement Banking Platform (`BACKBASE`)
  * Barracuda Incident Response (`BARRACUDA_INCIDENTRESPONSE`)
  * Cloudflare Access (`CLOUDFLARE_ACCESS`)
  * Control D DNS (`CONTROL_D`)
  * Digicert (`DIGICERT`)
  * Elastic Defend (`ELASTIC_DEFEND`)
  * FingerprintJS (`FINGERPRINT_JS`)
  * Hashicorp Nomad (`HASHICORP_NOMAD`)
  * IBM NS1 (`IBM_NS1`)
  * Intel 471 Malware Intelligence (`INTEL471_MALWARE_INTEL`)
  * MacStadium (`MACSTADIUM`)
  * N-Able N-Central RMM (`N_ABLE_N_CENTRAL_RMM`)
  * Opentext Exstream (`OPENTEXT_EXSTREAM`)
  * OVHcloud (`OVHCLOUD`)
  * OX Security (`OX_SECURITY`)
  * Pharos (`PHAROS`)
  * ReliaQuest (`RELIAQUEST`)
  * Rublon (`RUBLON`)
  * Snyk Group level audit/issues logs (`SNYK_ISSUES`)
  * SolarWinds Network Performance Monitor (`SOLARWINDS_NPM`)
  * StackHawk (`STACKHAWK`)
  * Tencent Cloud Firewall (`TENCENT_CLOUD_FIREWALL`)
  * Tencent Cloud Waf (`TENCENT_CLOUD_WAF`)
  * Tencent Cloud Workload Protection (`TENCENT_CLOUD_WORKLOAD_PROTECTION`)
  * Trend Micro Server Protect (`TRENDMICRO_SERVER_PROTECT`)
  * UKG (`UKG`)
  * Uptivity (`UPTIVITY`)
  * USBAV Koramis (`USBAV_KORAMIS`)
  * Virtual Network Flow Logs (`VIRTUAL_NETWORK_FLOW_LOGS`)
  * Windows Performance Monitor (`MS_PERFMON`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## October 15, 2024

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have changed. Each parser is listed by product name and `log_type` value, if applicable. This list now includes both released default parsers and pending parser updates.

  * Abnormal Security (`Email Server`)
  * AIX system (`OS`)
  * Akamai DNS (`DNS`)
  * Akamai WAF (`WAF`)
  * Apache (`Security`)
  * Apigee (`Google Cloud Specific`)
  * Apple macOS (`AV / Endpoint`)
  * Archer Integrated Risk Management (`Risk Management Solution`)
  * Area1 Security (`Email server`)
  * Aruba (`Wireless`)
  * Aruba Switch (`Network Infrastructure`)
  * Auth0 (`Authentication log`)
  * AWS CloudFront (`CDN`)
  * AWS Cloudtrail (`Cloud Log Aggregator`)
  * AWS CloudWatch (`Cloud service monitoring`)
  * AWS EMR (`AWS Specific`)
  * AWS VPN (`VPN`)
  * Azure AD (`LDAP`)
  * Azure AD Directory Audit (`Audit`)
  * Azure Firewall (`Azure Firewall Application Rule`)
  * Azure Key Vault logging (`Audit`)
  * Barracuda Firewall (`Firewall`)
  * Barracuda WAF (`Firewall`)
  * BeyondTrust Endpoint Privilege Management (`Privileged Account Activity`)
  * Blue Coat Proxy (`Web Proxy`)
  * BMC Client Management (`Security`)
  * Check Point (`Firewall`)
  * Chrome Management (`Browser`)
  * Cisco IronPort (`Gateway Security`)
  * Cisco ISE (`Identity and Access Management`)
  * Cisco Meraki (`Wireless`)
  * Cisco Router (`Switches, Routers`)
  * Cisco Stealthwatch (`Log Aggregator`)
  * Cisco Switch (`Switches, Routers`)
  * Cisco TACACS+ (`Authentication`)
  * Cisco Umbrella Web Proxy (`Web Proxy`)
  * Cisco WLC/WCS (`Wireless`)
  * Citrix Netscaler (`Load Balancer, Traffic Shaper, ADC`)
  * Claroty Continuous Threat Detection (`IoT`)
  * Cloud Audit Logs (`Google Cloud Specific`)
  * Cloud Data Loss Prevention (`Google Cloud Specific`)
  * Cloud SQL (`Google Cloud Specific`)
  * Cohesity (`Backup Software`)
  * Corelight (`NDR`)
  * CrowdStrike Detection Monitoring (`EDR`)
  * CrowdStrike Falcon (`EDR`)
  * CrushFTP (`Application server`)
  * Darktrace (`NDR`)
  * Delinea Secret Server (`Privileged Account Activity`)
  * Dell EMC Data Domain (`Storage system`)
  * Druva Backup (`Security`)
  * Duo Activity Logs (`Activity`)
  * Duo Administrator Logs (`Authentication`)
  * Elastic Windows Event Log Beats (`Log Aggregator`)
  * Ergon Informatik Airlock IAM (`Application Whitelisting`)
  * F5 BIGIP Access Policy Manager (`Access Policy Manager`)
  * F5 BIGIP LTM (`Load Balancer, Traffic Shaper, ADC`)
  * FireEye HX (`EDR`)
  * FortiGate (`Firewall`)
  * Fortinet FortiAnalyzer (`Fortinet FortiAnalyzer`)
  * Fortinet FortiAuthenticator (`Security`)
  * Fortinet FortiEDR (`EDR`)
  * Fortinet Fortimanager (`Network Management and Optimization software`)
  * GitHub (`SaaS Application`)
  * GMV Checker ATM Security (`ATM Audit`)
  * Guardicore Centra (`Deception Software`)
  * Hashicorp Vault (`Privileged Account Activity`)
  * HP Aruba (ClearPass) (`Identity and Access Management`)
  * IBM Cloud Activity Tracker (`Security Log`)
  * IBM DB2 (`Database`)
  * IBM Mainframe Storage (`Monitoring`)
  * IBM OpenPages (`Data Security`)
  * Imperva (`WAF`)
  * Imperva CEF (`CEF`)
  * Imperva DRA (`Data Security`)
  * Infoblox (`DHCP, DNS`)
  * Infoblox DNS (`DNS`)
  * JAMF Pro (`Mac Endpoint Management System`)
  * Keycloak (`Identity and Access Management`)
  * Lacework Cloud Security (`Cloud Security`)
  * Linux Auditing System (AuditD) (`OS`)
  * Linux DHCP (`DHCP`)
  * ManageEngine Log360 (`Alert Log`)
  * McAfee ePolicy Orchestrator (`Policy Management`)
  * Microsoft AD FS (`LDAP`)
  * Microsoft Azure Activity (`Misc Windows Specific`)
  * Microsoft Azure Resource (`Log Aggregator`)
  * Microsoft Defender For Cloud (`Automation and DevOps Tools`)
  * Microsoft Defender for Endpoint (`EDR`)
  * Microsoft Defender for Identity (`EDR`)
  * Microsoft Graph Activity Logs (`AUDIT`)
  * Microsoft Graph API Alerts (`Gateway to data and intelligence`)
  * Microsoft Intune Context (`Mobile Device Management`)
  * Microsoft SQL Server (`Database`)
  * Mimecast URL Logs (`Email server log types`)
  * MISP Threat Intelligence (`Cybersecurity`)
  * Mobile Endpoint Security (`Mobile Endpoint Security`)
  * NetApp ONTAP (`Rest api`)
  * Netskope V2 (`Cloud Security`)
  * Office 365 (`SaaS Application`)
  * Okta (`Identity and Access Management`)
  * One Identity Identity Manager (`unified identity security`)
  * Opengear Remote Management (`Secure Remote Access`)
  * Oracle (`DATABASE`)
  * Oracle Cloud Infrastructure VCN Flow Logs (`Oracle Cloud Infrastructure`)
  * Palo Alto Networks Firewall (`Firewall`)
  * Palo Alto Panorama (`Firewall`)
  * Palo Alto Prisma Cloud Alert payload (`Cloud Security`)
  * Proofpoint CASB (`CASB`)
  * Proofpoint Email Filter (`Email Server`)
  * Proofpoint On Demand (`Email Server`)
  * Proofpoint Threat Response (`Email Server`)
  * Pulse Secure (`VPN`)
  * Radware Web Application Firewall (`Firewall`)
  * SailPoint IAM (`Identity and Access Management`)
  * Saiwall VPN (`VPN`)
  * Salesforce (`SaaS Application`)
  * Sentinelone Alerts (`Endpoint Security`)
  * SonicWall (`Firewall`)
  * Sophos Central (`AV / Endpoint`)
  * Sophos Firewall (Next Gen) (`Firewall`)
  * Squid Web Proxy (`Web Proxy`)
  * STIX Threat Intelligence (`Cybersecurity Threats`)
  * Suricata EVE (`IPS IDS`)
  * Symantec DLP (`DLP`)
  * Symantec Endpoint Protection (`AV / Endpoint`)
  * Symantec Web Security Service (`Web Proxy`)
  * TINTRI (`Data Security`)
  * Trend Micro Apex one (`Endpoint Security`)
  * TrendMicro Apex Central (`Endpoint`)
  * UberAgent (`Security`)
  * Veeam (`Backup software`)
  * Velo Firewall (`FIREWALL`)
  * VMware AirWatch (`Wireless`)
  * VMware NSX (`Network and Security Virtualization`)
  * VMware vCenter (`Server`)
  * WatchGuard (`Syslog and KV`)
  * Wazuh (`Log Aggregator`)
  * Windows Event (`Endpoint`)
  * Windows Event (XML) (`AV / Endpoint`)
  * Windows Sysmon (`DNS`)
  * Workday User Activity (`N/A`)
  * Workspace Activities (`Google Cloud Specific`)
  * XAMS by Xiting (`Log Aggregator`)
  * ZeroFox Platform (`Database`)
  * Zscaler (`Web Proxy`)
  * Zywall (`Network infrastructure`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, if applicable.

  * Adaptive Shield (`ADAPTIVE_SHIELD`)
  * Agiloft (`AGILOFT`)
  * Airwatch Context (`AIRWATCH_CONTEXT`)
  * Attack IQ (`ATTACK_IQ`)
  * AWS PY Tools (`AWS_PY_TOOLS`)
  * Bindplane Agent (`BINDPLANE_AGENT`)
  * BindPlane Audit Logs (`BINDPLANE`)
  * Bitsight (`BITSIGHT`)
  * Bitvise SFTP (`BITVISE_SFTP`)
  * Ciena Router logs (`CIENA_ROUTER`)
  * Cisco Viptela (`CISCO_VIPTELA`)
  * Colinet Trotta GAUS SEGUROS (`CT_GAUS_SEGUROS`)
  * Conductor One (`CONDUCTOR_ONE`)
  * Crowdstrike Endpoint Security API (`CS_ENDPOINT_SECURITY_API`)
  * Fiserv SecureNow (`SECURE_NOW`)
  * Greenhouse Harvest (`GREENHOUSE_HARVEST`)
  * Harness IO (`HARNESS_IO`)
  * Hashicorp Boundary (`HASHICORP_BOUNDARY`)
  * HP Linux (`HP_LINUX`)
  * IBM Security Guardium Insights (`IBM_INSIGHTS`)
  * Imperva Attack Analytics (`IMPERVA_ATTACK_ANALYTICS`)
  * INTEL471 Watcher Alerts (`INTEL471_WATCHER_ALERTS`)
  * JAMF Security Cloud (`JAMF_SECURITY_CLOUD`)
  * JBoss Web (`JBOSS_WEB`)
  * Kandji Context (`KANDJI_CONTEXT`)
  * Lenels2 Elements Secure (`LENELS2_ELEMENTS_SECURE`)
  * ManageEngine OpUtils (`MANAGE_ENGINE_OPUTILS`)
  * Microsoft Graph Incident (`MICROSOFT_GRAPH_INCIDENT`)
  * Miro (`MIRO`)
  * Open Policy Agent (`OPA`)
  * Oracle Access Manager (`ORACLE_AM`)
  * Oracle Enterprise Manager (`ORACLE_OEM`)
  * Perception Point XRay (`PERCEPTION_POINT_XRAY`)
  * RedSift BrandTrust (`REDSIFT_BRANDTRUST`)
  * Riverbed (`RIVERBED`)
  * SAP Sybase Adaptive Server Enterprise Database (`SAP_ASE`)
  * Sharefile Logs (`SHAREFILE_LOGS`)
  * Smartsheet (`SMARTSHEET`)
  * Statusgator (`STATUSGATOR`)
  * Titan MFT (`TITAN_MFT`)
  * Upwind (`UPWIND`)
  * Vanta Context (`VANTA_CONTEXT`)
  * Varnish Cache (`VARNISH_CACHE`)
  * Vercel WAF (`VERCEL_WAF`)
  * Veriato Cerebral (`VERIATO_CEREBRAL`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## October 06, 2024

Feature

When performing a search on entities in the SOAR search page, you can now focus on more precise results by using the new condition `Equals`, in addition to the default condition `Contains`.

## September 30, 2024

Feature

The case report now includes all information written on the case wall.

Feature

It is now possible to merge cases where the requester is not the assignee both in the platform and through the API endpoint: `api/external/v1/cases-queue/bulk-operations/MergeCases`

## September 16, 2024

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have changed. Each parser is listed by product name and `log_type` value, if applicable. This list now includes both released default parsers and pending parser updates.

  * Abnormal Security (`ABNORMAL_SECURITY`)
  * Akamai DNS (`AKAMAI_DNS`)
  * Amazon API Gateway (`AWS_API_GATEWAY`)
  * Apache (`APACHE`)
  * Apigee (`GCP_APIGEE_X`)
  * Archer Integrated Risk Management (`ARCHER_IRM`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS VPC Flow (`AWS_VPC_FLOW`)
  * AWS VPN (`AWS_VPN`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Audit (`AZURE_AD_AUDIT`)
  * Azure AD Sign-In (`AZURE_AD_SIGNIN`)
  * Azure Storage Audit (`AZURE_STORAGE_AUDIT`)
  * Azure WAF (`AZURE_WAF`)
  * BeyondTrust Privileged Identity (`BEYONDTRUST_PI`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Carbon Black App Control (`CB_APP_CONTROL`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Checkpoint Audit (`CHECKPOINT_AUDIT`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Meraki (`CISCO_MERAKI`)
  * Cisco WSA (`CISCO_WSA`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Cloud Audit Logs (`N/A`)
  * Cloud Data Loss Prevention (`N/A`)
  * Cloud Load Balancing (`GCP_LOADBALANCING`)
  * Cloud SQL (`GCP_CLOUDSQL`)
  * Cloudflare WAF (`CLOUDFLARE_WAF`)
  * Cohesity (`COHESITY`)
  * Corelight (`CORELIGHT`)
  * CrowdStrike Falcon (`CS_EDR`)
  * Cyber 2.0 IDS (`CYBER_2_IDS`)
  * Cyberark Privilege Cloud (`CYBERARK_PRIVILEGE_CLOUD`)
  * CyberArk PTA Privileged Threat Analytics (`CYBERARK_PTA`)
  * Darktrace (`DARKTRACE`)
  * Dell Switch (`DELL_SWITCH`)
  * Duo Administrator Logs (`DUO_ADMIN`)
  * Duo Auth (`DUO_AUTH`)
  * EfficientIP DDI (`EFFICIENTIP_DDI`)
  * Elastic Audit Beats (`ELASTIC_AUDITBEAT`)
  * Elastic Packet Beats (`ELASTIC_PACKETBEATS`)
  * F5 ASM (`F5_ASM`)
  * F5 Shape (`F5_SHAPE`)
  * F5 Silverline (`F5_SILVERLINE`)
  * FireEye (`FIREEYE_ALERT`)
  * FireEye ETP (`FIREEYE_ETP`)
  * FireEye HX (`FIREEYE_HX`)
  * Forcepoint DLP (`FORCEPOINT_DLP`)
  * Forcepoint Email Security (`FORCEPOINT_EMAILSECURITY`)
  * Forcepoint Mail Relay (`FORCEPOINT_MAIL_RELAY`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortinet Fortimanager (`FORTINET_FORTIMANAGER`)
  * GCP_APP_ENGINE (`GCP_APP_ENGINE`)
  * GitHub (`GITHUB`)
  * HP Aruba (ClearPass) (`CLEARPASS`)
  * IBM DS8000 Storage (`IBM_DS8000`)
  * IBM Guardium (`GUARDIUM`)
  * IBM OpenPages (`IBM_OPENPAGES`)
  * Infoblox DNS (`INFOBLOX_DNS`)
  * Jenkins (`JENKINS`)
  * Layer7 SiteMinder (`SITEMINDER_SSO`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * Malwarebytes (`MALWAREBYTES_EDR`)
  * McAfee ePolicy Orchestrator (`MCAFEE_EPO`)
  * Microsoft AD FS (`ADFS`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft Azure Resource (`AZURE_RESOURCE_LOGS`)
  * Microsoft Defender for Office 365 (`MICROSOFT_DEFENDER_MAIL`)
  * Microsoft Exchange (`EXCHANGE_MAIL`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft PowerShell (`POWERSHELL`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * Microsoft System Center Endpoint Protection (`MICROSOFT_SCEP`)
  * Mimecast (`MIMECAST_MAIL`)
  * Nagios Infrastructure Monitoring (`NAGIOS`)
  * Network Policy Server (`MICROSOFT_NPS`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * Okta User Context (`OKTA_USER_CONTEXT`)
  * Oracle (`ORACLE_DB`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Ping Federate (`PING_FEDERATE`)
  * Ping Identity (`PING`)
  * PostgreSQL (`POSTGRESQL`)
  * Precisely Ironstream IBM z/OS (`IRONSTREAM_ZOS`)
  * Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Pulse Secure (`PULSE_SECURE_VPN`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * Rippling Activity Logs (`RIPPLING_ACTIVITYLOGS`)
  * Sap Business Technology Platform (`SAP_BTP`)
  * Security Command Center Threat (`N/A`)
  * Sentinelone Alerts (`SENTINELONE_ALERT`)
  * SentinelOne EDR (`SENTINEL_EDR`)
  * SentinelOne Singularity Cloud Funnel (`SENTINELONE_CF`)
  * Shibboleth IDP (`SHIBBOLETH_IDP`)
  * Snare System Diagnostic Logs (`SNARE_SOLUTIONS`)
  * Snowflake (`SNOWFLAKE`)
  * Sophos AV (`SOPHOS_AV`)
  * Sophos Intercept EDR (`SOPHOS_EDR`)
  * Sourcefire (`SOURCEFIRE_IDS`)
  * Splunk Attack Analyzer (`SPLUNK_ATTACK_ANALYZER`)
  * SpyCloud (`SPYCLOUD`)
  * Squid Web Proxy (`SQUID_WEBPROXY`)
  * Suricata EVE (`SURICATA_EVE`)
  * Symantec Endpoint Protection (`SEP`)
  * Symantec Web Security Service (`SYMANTEC_WSS`)
  * Tenable Audit (`TENABLE_AUDIT`)
  * Thales Vormetric (`VORMETRIC`)
  * Trend Micro Apex one (`TRENDMICRO_APEX_ONE`)
  * Trend Micro Deep Security (`TRENDMICRO_DEEP_SECURITY`)
  * Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
  * TrendMicro Apex Central (`TRENDMICRO_APEX_CENTRAL`)
  * Twingate (`TWINGATE`)
  * Ubika Waf (`UBIKA_WAF`)
  * Unix system (`NIX_SYSTEM`)
  * Vectra Detect (`VECTRA_DETECT`)
  * Vectra Stream (`VECTRA_STREAM`)
  * Wazuh (`WAZUH`)
  * Windows DHCP (`WINDOWS_DHCP`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Windows Local Administrator Password Solution (`MICROSOFT_LAPS`)
  * Windows Sysmon (`WINDOWS_SYSMON`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * Workspace Alerts (`WORKSPACE_ALERTS`)
  * XAMS by Xiting (`XITING_XAMS`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, if applicable.

  * Active Identity HID (`ACTIVE_IDENTITY_HID`)
  * Akamai Event Viewer (`AKAMAI_EVT_VWR`)
  * Autodesk Vault (`AUTODESK_VAULT`)
  * Avaza (`AVAZA`)
  * Avigilon Access Logs (`AVIGILON_ACCESS_LOGS`)
  * Axis Camera (`AXIS_CAMERA`)
  * Axis License Plate Reader (`AXIS_LPR`)
  * Azure Nix System (`AZURE_NIX_SYSTEM`)
  * CallTower Audio Conferencing (`CALLTOWER_AUDIO`)
  * Canon Printers (`CANON_PRINTERS`)
  * Cisco Secure Endpoint (`CISCO_SECURE_ENDPOINT`)
  * Control UP (`CONTROL_UP`)
  * Cradlepoint Router Logs (`CRADLEPOINT`)
  * Crowdstrike Spotlight (`CROWDSTRIKE_SPOTLIGHT`)
  * CrushFTP (`CRUSHFTP`)
  * CrowdStrike Filevantage (`CS_FILEVANTAGE`)
  * Cybersixgill (`CYBERSIXGILL`)
  * Cyolo Secure Remote Access for OT (`CYOLO_OT`)
  * Dell Core Switch (`DELL_EMC_NETWORKING`)
  * DLink Switch (`DLINK_SWITCH`)
  * Elastic Security (`ELASTIC_EDR`)
  * Fireblocks (`FIREBLOCKS`)
  * Forescout eyeInspect (`FORESCOUT_EYEINSPECT`)
  * Fortinet FortiGate IPS (`FORTINET_IPS`)
  * H3C Router (`H3C_ROUTER`)
  * Hackerone (`HACKERONE`)
  * Halo Sensor (`HALO_SENSOR`)
  * Hashcast (`HASHCAST`)
  * Perforce Helix Core (`HELIX_CORE`)
  * Heroku (`HEROKU`)
  * Hillstone NDR (`HILLSTONE_NDR`)
  * HL7 (`HL7`)
  * HoopDev (`HOOPDEV`)
  * Huawei Switches (`HUAWEI_SWITCH`)
  * Identity Security Cloud (`IDENTITY_SECURITY_CLOUD`)
  * Imperva Data Risk Analytics (`IMPERVA_DATA_ANALYTICS`)
  * Imperva DRA (`IMPERVA_DRA`)
  * IM Express (`IM_EXPRESS`)
  * Intezer (`INTEZER`)
  * Jumpcloud IAM (`JUMPCLOUD_IAM`)
  * Maltiverse IOC (`MALTIVERSE_IOC`)
  * ManageEngine Log360 (`MANAGE_ENGINE_LOG360`)
  * McAfee Network Security Platform (`MCAFEE_NSP`)
  * Miro Cloud (`MIRO_CLOUD`)
  * Nokia Home Device Manager (`NOKIA_HDM`)
  * Nortel Secure Router (`NORTEL_SR`)
  * Notion (`NOTION`)
  * One Identity Identity Manager (`ONE_IDENTITY_IDENTITY_MANAGER`)
  * IDnomic Public Key Infrastructure (`OPENTRUST`)
  * Outline Activity Logs (`OUTLINE_ACTIVITY_LOGS`)
  * Prismatic IO (`PRISMATIC_IO`)
  * ProFTPD (`PROFTPD`)
  * Provision Asset Context (`PROVISION_ASSET_CONTEXT`)
  * Ransomcare (`RANSOMCARE`)
  * Rapid7 Insights Threat Command (`RAPID7_INSIGHTS_THREAT_COMMAND`)
  * Saporo (`SAPORO`)
  * SAS Metadata Server log (`SAS_METADATA_SERVER_LOG`)
  * Scylla (`SCYLLA`)
  * Senseon Alerts (`SENSEON_ALERTS`)
  * Sonic Switch (`SONIC_SWITCH`)
  * Symantec Data Center Security (`SYMANTEC_DCS`)
  * Syncplify SFTP 2 Events (`SYNCPLIFY_SFTP`)
  * Team Cymru Scout Threat Intelligence (`TEAM_CYMRU_SCOUT_THREATINTEL`)
  * Tenable CSPM (`TENABLE_CSPM`)
  * Teqtivity Assets (`TEQTIVITY_ASSETS`)
  * Tines (`TINES`)
  * TP Link Network Switches (`TPLINK_SWITCH`)
  * TT D365 (`TT_D365`)
  * TT MSAN DSLAM (`TT_MSAN_DSLAM`)
  * TT Trio Chordiant (`TT_TRIO_CHORDIANT`)
  * Tufin (`TUFIN`)
  * Tufin Secure Track (`TUFIN_SECURE_TRACK`)
  * UberAgent (`UBERAGENT`)
  * Upstream Vehicle SOC Alerts (`UPSTREAM_VSOC_ALERTS`)
  * URLScan IO (`URLSCAN_IO`)
  * Vertiv UPS (`VERTIV_UPS`)
  * Very Good Security (`VERY_GOOD_SECURITY`)
  * Virtual Browser (`VIRTUAL_BROWSER`)
  * VMWare VSphere (`VMWARE_VSPHERE`)
  * Webroot Identity Protection (`WEBROOT_IDENTITY_PROTECTION`)
  * WideField (`WIDEFIELD_SECURITY`)
  * Zscaler Sandbox (`ZSCALER_SANDBOX`)
  * Zywall (`ZYWALL`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## September 06, 2024

Change

Burst limits will be rolling out over the next 90 days. This should not affect customers if sources are properly configured. Review [documentation](https://docs.cloud.google.com/chronicle/docs/preview/limits/limits) for full details.

## August 01, 2024

Change

Customers can now configure direct ingestion of Google Cloud data without using a _1-time Google Security Operations access code_. This feature will be launched over a period of several weeks. For more information, see [Enable direct ingestion from Google Cloud](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs#enable-direct-ingestion).

## July 28, 2024

Feature

Creating a new playbook using prompts is now supported by Gemini. This feature is in public preview. For more information, refer to [Create playbooks with Gemini](https://docs.cloud.google.com/chronicle/docs/secops/gemini-chronicle#playbook-gemini).

## July 25, 2024

Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have changed. Each parser is listed by product name and `log_type` value, if applicable.

  * Airlock Digital Application Allowlisting (`AIRLOCK_DIGITAL`)
  * Akamai SIEM Connector (`AKAMAI_SIEM_CONNECTOR`)
  * Apache (`APACHE`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * Arista Switch (`ARISTA_SWITCH`)
  * Aruba (`ARUBA_WIRELESS`)
  * Aruba EdgeConnect SD-WAN (`ARUBA_EDGECONNECT_SDWAN`)
  * Atlassian Confluence (`ATLASSIAN_CONFLUENCE`)
  * Auth0 (`AUTH_ZERO`)
  * AWS CloudTrail (`AWS_CLOUDTRAIL`)
  * AWS Config (`AWS_CONFIG`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure App Service (`AZURE_APP_SERVICE`)
  * Azure WAF (`AZURE_WAF`)
  * BeyondTrust Endpoint Privilege Management (`BEYONDTRUST_ENDPOINT`)
  * BIND (`BIND_DNS`)
  * BloxOne Threat Defense (`BLOXONE`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Broadcom SSL Visibility Appliance (`BROADCOM_SSL_VA`)
  * Cequence Bot Defense (`CEQUENCE_BOT_DEFENSE`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Checkpoint Audit (`CHECKPOINT_AUDIT`)
  * Checkpoint SmartDefense (`CHECKPOINT_SMARTDEFENSE`)
  * Cimcor | File Integrity Monitoring (`CIMCOR`)
  * CipherTrust Manager (`CIPHERTRUST_MANAGER`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco EStreamer (`CISCO_ESTREAMER`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco FireSIGHT Management Center (`CISCO_FIRESIGHT`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco IronPort (`CISCO_IRONPORT`)
  * Cisco Meraki (`CISCO_MERAKI`)
  * Cisco Router (`CISCO_ROUTER`)
  * Cisco Stealthwatch (`CISCO_STEALTHWATCH`)
  * Cisco VPN (`CISCO_VPN`)
  * Citrix Analytics (`CITRIX_ANALYTICS`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Cloud Audit Logs (`N/A`)
  * Cloud Data Loss Prevention (`N/A`)
  * Cloud Identity Devices (`GCP_CLOUDIDENTITY_DEVICES`)
  * Cloud Load Balancing (`GCP_LOADBALANCING`)
  * Cloud SQL (`GCP_CLOUDSQL`)
  * Cofense (`COFENSE_TRIAGE`)
  * Comforte SecurDPS (`COMFORTE_SECURDPS`)
  * Compute Engine (`GCP_COMPUTE`)
  * Corelight (`CORELIGHT`)
  * Cribl Stream (`CRIBL_STREAM`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CyberArk (`CYBERARK`)
  * DigitalArts i-Filter (`DIGITALARTS_IFILTER`)
  * Duo Auth (`DUO_AUTH`)
  * Duo User Context (`DUO_USER_CONTEXT`)
  * EfficientIP DDI (`EFFICIENTIP_DDI`)
  * Elastic Audit Beats (`ELASTIC_AUDITBEAT`)
  * Elastic Windows Event Log Beats (`ELASTIC_WINLOGBEAT`)
  * Ergon Informatik Airlock IAM (`ERGON_INFORMATIK_AIRLOCK_IAM`)
  * ESET AV (`ESET_AV`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * F5 Shape (`F5_SHAPE`)
  * F5 Silverline (`F5_SILVERLINE`)
  * Fidelis Network (`FIDELIS_NETWORK`)
  * FileZilla (`FILEZILLA_FTP`)
  * Forcepoint Email Security (`FORCEPOINT_EMAILSECURITY`)
  * Forcepoint Proxy (`FORCEPOINT_WEBPROXY`)
  * Forgerock OpenIdM (`FORGEROCK_OPENIDM`)
  * Fortinet FortiAuthenticator (`FORTINET_FORTIAUTHENTICATOR`)
  * Google App Engine (`GCP_APP_ENGINE`)
  * GitHub (`GITHUB`)
  * IBM DataPower Gateway (`IBM_DATAPOWER`)
  * IBM DB2 (`DB2_DB`)
  * IBM Guardium (`GUARDIUM`)
  * IBM Security QRadar SIEM (`IBM_QRADAR`)
  * Imperva Audit Trail (`IMPERVA_AUDIT_TRAIL`)
  * Ingrian Networks DataSecure Appliance (`INGRIAN_NETWORKS_DATASECURE_APPLIANCE`)
  * ION Spectrum (`ION_SPECTRUM`)
  * JAMF Pro (`JAMF_PRO`)
  * Jenkins (`JENKINS`)
  * Juniper Junos (`JUNIPER_JUNOS`)
  * Juniper Mist (`JUNIPER_MIST`)
  * Juniper MX Router (`JUNIPER_MX`)
  * Keeper Enterprise Security (`KEEPER`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * Linux Sysmon (`LINUX_SYSMON`)
  * Lucid (`LUCID`)
  * Maria Database (`MARIA_DB`)
  * Microsoft AD (`WINDOWS_AD`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft CyberX (`CYBERX`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Defender for Identity (`MICROSOFT_DEFENDER_IDENTITY`)
  * Microsoft Exchange (`EXCHANGE_MAIL`)
  * Microsoft Graph Activity Logs (`MICROSOFT_GRAPH_ACTIVITY_LOGS`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft IIS (`IIS`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * Mimecast URL Logs (`MIMECAST_URL_LOGS`)
  * Netapp Storagegrid (`NETAPP_STORAGEGRID`)
  * Netskope (`NETSKOPE_ALERT`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * Network Policy Server (`MICROSOFT_NPS`)
  * Noname API Security (`NONAME_API_SECURITY`)
  * Office 365 (`OFFICE_365`)
  * Office 365 Message Trace (`OFFICE_365_MESSAGETRACE`)
  * Okta (`OKTA`)
  * Okta User Context (`OKTA_USER_CONTEXT`)
  * Open LDAP (`OPENLDAP`)
  * Oracle (`ORACLE_DB`)
  * Oracle Cloud Infrastructure Audit Logs (`OCI_AUDIT`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Palo Alto Prisma Cloud Alert payload (`PAN_PRISMA_CA`)
  * Passwordstate (`PASSWORDSTATE`)
  * Ping Identity (`PING`)
  * Portnix CEF (`PORTNOX_CEF`)
  * PostFix Mail (`POSTFIX_MAIL`)
  * Proofpoint Email Filter (`PROOFPOINT_MAIL_FILTER`)
  * Proofpoint Sendmail Sentrion (`PROOFPOINT_SENDMAIL_SENTRION`)
  * Proofpoint Threat Response (`PROOFPOINT_TRAP`)
  * Quest Change Auditor for EMC (`QUEST_CHANGE_AUDITOR_EMC`)
  * Radware Alteon (`RADWARE_ALTEON`)
  * Radware Web Application Firewall (`RADWARE_FIREWALL`)
  * Red Hat Directory Server LDAP (`REDHAT_DIRECTORY_SERVER`)
  * Riverbed Steelhead (`STEELHEAD`)
  * RSA SecurID Access Identity Router (`RSA_SECURID`)
  * Ruckus Networks (`RUCKUS_WIRELESS`)
  * Salesforce (`SALESFORCE`)
  * SentinelOne EDR (`SENTINEL_EDR`)
  * SentinelOne Singularity Cloud Funnel (`SENTINELONE_CF`)
  * SEPPmail Secure Email (`SEPPMAIL`)
  * ServiceNow CMDB (`SERVICENOW_CMDB`)
  * SiteMinder Web Access Management (`CA_SSO_WEB`)
  * Snare System Diagnostic Logs (`SNARE_SOLUTIONS`)
  * Solarwinds Kiwi Syslog Server (`SOLARWINDS_KSS`)
  * SonicWall (`SONIC_FIREWALL`)
  * Sonrai Enterprise Cloud Security Solution (`SONRAI`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Symantec Endpoint Protection (`SEP`)
  * Symantec VIP Authentication Hub (`SYMANTEC_VIP_AUTHHUB`)
  * Symantec Web Security Service (`SYMANTEC_WSS`)
  * Sysdig (`SYSDIG`)
  * Tableau (`TABLEAU`)
  * Terraform Enterprise Audit (`TERRAFORM_ENTERPRISE`)
  * Thinkst Canary (`THINKST_CANARY`)
  * Thycotic (`THYCOTIC`)
  * Trend Micro (`TIPPING_POINT`)
  * Ubika WAAP (`UBIKA_WAAP`)
  * Ubika Waf (`UBIKA_WAF`)
  * UPX AntiDDoS (`UPX_ANTIDDOS`)
  * Vectra Stream (`VECTRA_STREAM`)
  * Velo Firewall (`VELO_FIREWALL`)
  * VeridiumID by Veridium (`VERIDIUM_ID`)
  * Versa Firewall (`VERSA_FIREWALL`)
  * Virtru Email Encryption (`VIRTRU_EMAIL_ENCRYPTION`)
  * VMware ESXi (`VMWARE_ESX`)
  * VMware NSX (`VMWARE_NSX`)
  * VMware vCenter (`VMWARE_VCENTER`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Windows Local Administrator Password Solution (`MICROSOFT_LAPS`)
  * Workday (`WORKDAY`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * Zscaler CASB (`ZSCALER_CASB`)
  * Zscaler Internet Access Audit Logs (`ZSCALER_INTERNET_ACCESS`)
  * Zscaler Private Access (`ZSCALER_ZPA`)
  * Zscaler Secure Private Access Audit Logs (`ZSCALER_ZPA_AUDIT`)



The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, if applicable.

  * Backstage (`BACKSTAGE`)
  * Bitwarden Password Manager User Context (`BITWARDEN_USER_CONTEXT`)
  * Boomi App (`BOOMI_APP`)
  * ChatGPT Audit Logs (`CHATGPT_AUDIT_LOGS`)
  * Cloudflare Warp (`CLOUDFLARE_WARP`)
  * Coda Io (`CODA_IO`)
  * Fortinet Fortimanager (`FORTINET_FORTIMANAGER`)
  * Fusion Auth (`FUSION_AUTH`)
  * Google Cloud Abuse Events (`GCP_ABUSE_EVENTS`)
  * Google Cloud Monitoring Alerts (`GCP_MONITORING_ALERTS`)
  * Gong (`GONG`)
  * Grafana (`GRAFANA`)
  * IBM Cloud Activity Tracker (`IBM_CLOUD_ACTIVITY_TRACKER`)
  * IBM Cloud System (`IBM_CLOUD_SYSTEM`)
  * Incident Io (`INCIDENT_IO`)
  * Kentik DDoS Detection (`KENTIK_ALERTS`)
  * Lockself Lockpass (`LOCKSELF_LOCKPASS`)
  * Magic Collaboration Studio (`MAGIC_CS`)
  * Metaswitch Perimeta (`METASWITCH_PERIMETA`)
  * Microsoft Defender Endpoint for iOS Logs (`MICROSOFT_DEFENDER_ENDPOINT_IOS`)
  * 9NowAudit (`NINENOW_AUDIT`)
  * Oracle Cloud Guard (`OCI_CLOUDGUARD`)
  * Oort Security Tool (`OORT`)
  * OpsRamp (`OPSRAMP`)
  * Ops Genie (`OPS_GENIE`)
  * People Strong (`PEOPLE_STRONG`)
  * Pingdom (`PINGDOM`)
  * Proofpoint Tap Campaign (`PROOFPOINT_TAP_CAMPAIGN`)
  * Proofpoint Tap Forensics (`PROOFPOINT_TAP_FORENSICS`)
  * Proofpoint Tap People (`PROOFPOINT_TAP_PEOPLE`)
  * Proofpoint Tap Threats (`PROOFPOINT_TAP_THREATS`)
  * Proofpoint Tis IOC (`PROOFPOINT_TIS_IOC`)
  * Push Security (`PUSH_SECURITY`)
  * Recordedfuture Alerts (`RECORDEDFUTURE_ALERTS`)
  * Rippling Activity Logs (`RIPPLING_ACTIVITYLOGS`)
  * Sentry (`SENTRY`)
  * Servertech PDUs (`SERVERTECH_PDUS`)
  * Sprinkledata(DWH) (`SPRINKLEDATA_DWH`)
  * Tenable Audit (`TENABLE_AUDIT`)
  * TINTRI (`TINTRI`)
  * WPass (`WPASS`)
  * WPEngine (`WPENGINE`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

Deprecated

The Google Security Operations alert metadata fields for UDM `idm.is_significant` and `idm.is_alert` have been deprecated. Use [YARA-L detection rule alerts](https://docs.cloud.google.com/chronicle/docs/detection/migrate-cbn-alerts) for alert metadata.

## July 24, 2024

Announcement

The Incident Manager in Google Security Operations will be fully decommissioned on July 22, 2025. Google Cloud will provide full support and maintenance until July 22, 2025 but no new features will be released.

## July 18, 2024

Change

When you migrate an existing Google SecOps instance so that it is [bound to a Google Cloud project](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud#migrate-existing), you can also use auto-generated commands to migrate your existing _feature RBAC_ configuration to IAM permissions and roles. For more information, see [Migrate existing permissions to IAM](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud#migrate-rbac).

## July 17, 2024

Deprecated

On December 31, 2024, the managed BigQuery data lake for export will not be accessible to Google SecOps customers except for customers in the Enterprise Plus Tier. Enterprise Plus Tier customers will retain access until a replacement is available. Other customers can use their own BigQuery instance to export telemetry data, a feature currently in preview. For more information, see [Configure a data export to BigQuery in a self-managed Google Cloud project](https://docs.cloud.google.com/chronicle/docs/preview/cloud-integration/export-to-customer-managed-project).

## July 15, 2024

Deprecated

The third-party API feed `Symantec Event Export` has been discontinued due to the deprecation of Symantec Event Export API. To ingest data, use a Cloud Storage bucket. For more information, see [Add a feed](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#add-new-feed).

## July 13, 2024

Deprecated

Python 2.7 is being deprecated and will be fully removed on October 13, 2024.

For information on how to update Marketplace integrations to Python 3.11, refer to [Upgrade the Python versions](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/upgrade-python-versions).

Announcement

**Support for Python 3.11** : Google SecOps now supports Python 3.11 in all the certified integrations. This feature is in General Availability.

Feature

**IDE Staging mode** : A staging mode has been added to the IDE where you can test certified and custom integrations as well as custom items. The staging mode acts as a sandbox where you can test the new Python 3.11 code or any upgraded integration before pushing to production. For more information, refer to [Test integrations in staging mode](https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/test-integrations-in-staging-mode). This feature is in General Availability.

## June 26, 2024

Feature

You can use the BindPlane agent to collect Windows event logs, query SQL databases, read logs from files, and receive logs using syslog. The agent sends data directly to the Google Security Operations ingestion API or to a Google SecOps forwarder. For more information, see [Use the BindPlane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent).

## June 24, 2024

Change

During the Google Security Operations onboarding steps, you can now specify identity provider groups that include administrators who configure user access to SOAR-related features. For more information, see [Link Google SecOps to Google Cloud services](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud).

Change

You can now configure Cloud Identity or Google Workspace as an identity provider during the Google Security Operations onboarding steps. For more information about onboarding, see [Onboarding or migrating a Google Security Operations instance](https://docs.cloud.google.com/chronicle/docs/onboard).

## June 18, 2024

Feature

Google SecOps now integrates with [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview). 

If you enabled Access Transparency in your organization, Google SecOps writes Access Transparency logs when any Google personnel accesses customer content that supports SIEM features.

For more information, see [enabling Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable) and [viewing Access Transparency logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs#viewing-logs).

Change

`lastAlertStatusChangeTime` is added to the response of the [`GetRule`](https://docs.cloud.google.com/chronicle/docs/reference/detection-engine-api#getrule) Detection Engine API. This indicates when `alertingEnabled` was last updated from `true` to `false` or from `false` to `true`. 

The field is also added to [`RuleDeployment`](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/RuleDeployment) of Chronicle API v1 alpha.

Feature

Google SecOps now supports [data RBAC](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview). This feature enables you to control user access to data within your Google SecOps environment based on their assigned roles.

## June 07, 2024

Change

The syntax for placeholders in UDM saved searches is updated. See [Save a search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#save_a_search) for the new syntax.

## May 30, 2024

Change

The following supported default parsers have changed. Each is listed by product name and `log_type` value, if applicable.

  * Abnormal Security (`ABNORMAL_SECURITY`)
  * Akamai DNS (`AKAMAI_DNS`)
  * Akamai WAF (`AKAMAI_WAF`)
  * Apigee (`GCP_APIGEE_X`)
  * Array Networks SSL VPN (`ARRAYNETWORKS_VPN`)
  * AWS CloudFront (`AWS_CLOUDFRONT`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure AD Sign-In (`AZURE_AD_SIGNIN`)
  * Barracuda Email (`BARRACUDA_EMAIL`)
  * Barracuda Firewall (`BARRACUDA_FIREWALL`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * BMC AMI Defender (`BMC_AMI_DEFENDER`)
  * Carbon Black (`CB_EDR`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Check Point Sandblast (`CHECKPOINT_EDR`)
  * Checkpoint Audit (`CHECKPOINT_AUDIT`)
  * Cisco AMP (`CISCO_AMP`)
  * Cisco EStreamer (`CISCO_ESTREAMER`)
  * Cisco FireSIGHT Management Center (`CISCO_FIRESIGHT`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Router (`CISCO_ROUTER`)
  * Cisco Switch (`CISCO_SWITCH`)
  * Cisco Umbrella DNS (`UMBRELLA_DNS`)
  * Cisco VPN (`CISCO_VPN`)
  * Cisco WLC/WCS (`CISCO_WIRELESS`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Cloud Audit Logs (`N/A`)
  * Cloud SQL (`GCP_CLOUDSQL`)
  * Cloud Storage Context (`N/A`)
  * Cohesity (`COHESITY`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
  * ESET AV (`ESET_AV`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * F5 VPN (`F5_VPN`)
  * Forcepoint DLP (`FORCEPOINT_DLP`)
  * FortiGate (`FORTINET_FIREWALL`)
  * GMAIL Logs (`GMAIL_LOGS`)
  * HID DigitalPersona (`HID_DIGITALPERSONA`)
  * Honeyd (`HONEYD`)
  * HP Aruba (ClearPass) (`CLEARPASS`)
  * IBM AS/400 (`IBM_AS400`)
  * IBM DS8000 Storage (`IBM_DS8000`)
  * IBM Security Verify (`IBM_SECURITY_VERIFY`)
  * Infoblox (`INFOBLOX`)
  * Island Browser logs (`ISLAND_BROWSER`)
  * JAMF CMDB (`JAMF`)
  * JumpCloud Directory Insights (`JUMPCLOUD_DIRECTORY_INSIGHTS`)
  * Juniper Mist (`JUNIPER_MIST`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * ManageEngine ADAudit Plus (`ADAUDIT_PLUS`)
  * Microsoft AD FS (`ADFS`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft Azure Resource (`AZURE_RESOURCE_LOGS`)
  * Microsoft CyberX (`CYBERX`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Graph Activity Logs (`MICROSOFT_GRAPH_ACTIVITY_LOGS`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * Mikrotik Router (`MIKROTIK_ROUTER`)
  * NetDocuments Solutions (`NETDOCUMENTS`)
  * Netwrix (`NETWRIX`)
  * Office 365 (`OFFICE_365`)
  * Office 365 Message Trace (`OFFICE_365_MESSAGETRACE`)
  * Okta (`OKTA`)
  * OneLogin (`ONELOGIN_SSO`)
  * Opengear Remote Management (`OPENGEAR`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * pfSense (`PFSENSE`)
  * PostFix Mail (`POSTFIX_MAIL`)
  * Proofpoint Sendmail Sentrion (`PROOFPOINT_SENDMAIL_SENTRION`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Pulse Secure (`PULSE_SECURE_VPN`)
  * Qumulo FS (`QUMULO_FS`)
  * Rapid7 (`RAPID7_NEXPOSE`)
  * Rapid7 Insight (`RAPID7_INSIGHT`)
  * Rubrik Polaris (`RUBRIK_POLARIS`)
  * SailPoint IAM (`SAILPOINT_IAM`)
  * SAP SuccessFactors (`SAP_SUCCESSFACTORS`)
  * Semperis DSP (`SEMPERIS_DSP`)
  * Sentinelone Alerts (`SENTINELONE_ALERT`)
  * SentinelOne EDR (`SENTINEL_EDR`)
  * Signal Sciences WAF (`SIGNAL_SCIENCES_WAF`)
  * Snare System Diagnostic Logs (`SNARE_SOLUTIONS`)
  * SonicWall (`SONIC_FIREWALL`)
  * Sophos Central (`SOPHOS_CENTRAL`)
  * Sophos UTM (`SOPHOS_UTM`)
  * Spur data feeds (`SPUR_FEEDS`)
  * Suricata EVE (`SURICATA_EVE`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Symantec Endpoint Protection (`SEP`)
  * Symantec VIP Authentication Hub (`SYMANTEC_VIP_AUTHHUB`)
  * Tanium Audit (`TANIUM_AUDIT`)
  * Thinkst Canary (`THINKST_CANARY`)
  * Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
  * Twingate (`TWINGATE`)
  * Unix system (`NIX_SYSTEM`)
  * Vectra Detect (`VECTRA_DETECT`)
  * Veeam (`VEEAM`)
  * Verba Recording System (`VERBA_REC`)
  * VeridiumID by Veridium (`VERIDIUM_ID`)
  * VMware ESXi (`VMWARE_ESX`)
  * Windows Defender ATP (`WINDOWS_DEFENDER_ATP`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Winscp (`WINSCP`)
  * WordPress (`WORDPRESS_CMS`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * Zeek TSV (`BRO_TSV`)
  * Zix Email Encryption (`ZIX_EMAIL_ENCRYPTION`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * ZScaler DNS (`ZSCALER_DNS`)
  * Zscaler Private Access (`ZSCALER_ZPA`)



The following log types, without a default parser, were added. Each is listed by product name and `log_type` value, if applicable.

  * Akamai Log Delivery Service (`AKAMAI_LDS`)
  * AudioCodes Voice DNA (`AUDIOCODES`)
  * Amazon API Gateway (`AWS_API_GATEWAY`)
  * Axway (`AXWAY`)
  * Biztalk (`BIZTALK`)
  * Check Point FDE (`CHECKPOINT_FDE`)
  * Cimcor | File Integrity Monitoring (`CIMCOR`)
  * CS Alerts (`CS_ALERTS`)
  * Custom CSV Log (`CUSTOM_CSV_LOG`)
  * Cyral (`CYRAL`)
  * Druva (`DRUVA`)
  * Entrust DataControl Audit (`ENTR_DATACTRL_AUDIT`)
  * Ergon Informatik Airlock IAM (`ERGON_INFORMATIK_AIRLOCK_IAM`)
  * Eset Protect Platform (`ESET_PROTECT_PLATFORM`)
  * Exim Internet Mailer (`EXIM_INTERNET_MAILER`)
  * FM Systems Workplace Management (`FM_SYSTEMS`)
  * GluWare Network Automation (`GLUWARE_NETWORK_AUTOMATION`)
  * Guidewire Billing Center (`GUIDEWIRE_BILLING_CENTER`)
  * Guidewire Claim Center (`GUIDEWIRE_CLAIM_CENTER`)
  * Guidewire Policy Center (`GUIDEWIRE_POLICY_CENTER`)
  * HAVI Connect (`HAVI_CONNECT`)
  * IBM OpenPages (`IBM_OPENPAGES`)
  * Ingrian Networks DataSecure Appliance (`INGRIAN_NETWORKS_DATASECURE_APPLIANCE`)
  * iSecurity | Security Services and Remediation (`ISECURITY`)
  * iTop (`ITOP`)
  * Microsoft Defender for Office 365 (`MICROSOFT_DEFENDER_MAIL`)
  * Microsoft Graph Risky Users (`MICROSOFT_GRAPH_RISKY_USERS`)
  * NetApp BlueXP (`NETAPP_BLUEXP`)
  * Netgate Firewall (`NETGATE_FIREWALL`)
  * 1KOSMOS | Identity and Authentication (`ONEKOSMOS`)
  * Palo Alto Global Protect SVC (`PAN_GPSVC`)
  * Palo Alto SSLVPN Access (`PAN_SSLVPN_ACCESS`)
  * Palo Alto Telemetry (`PAN_TELEMETRY`)
  * Proofpoint Endpoint Data Loss Prevention (`PROOFPOINT_ENDPOINT_DLP`)
  * SAP ERP (`SAP_ERP`)
  * Ubika WAAP (`UBIKA_WAAP`)
  * Webroot Endpoint Protection (`WEBROOT`)
  * Wolters Kluwer Teammate (`WOLTERS_KLUWER_TEAMMATE`)
  * Xirrus Wireless Controller (`XIRRUS`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## May 22, 2024

Feature

Enhanced the existing [curated detections for AWS rule sets](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#aws-rule-sets) in the Cloud Threats category to add 40 new detections. These new rules, added to existing rule sets, expand the coverage and are designed to identify tactics and techniques commonly employed by malicious actors that use popular open source offensive security tools against AWS resources.

## May 14, 2024

Change

Google SecOps now supports the following functions in Detection Engine rules:

  * fingerprint
  * sample_rate



For more information about these functions, see [YARA-L 2.0 language syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/getting-started).

## May 08, 2024

Change

When Applied Threat Intelligence is enabled, it ingests IOCs curated by Mandiant Threat Intelligence with an IC-Score greater than 80 and generates an alert when a match is found.

## May 06, 2024

Feature

**Gemini for investigation assistance**

Gemini for investigation assistance can now support you with the following:

  * **Search** : Gemini can help you build, edit, and run searches targeted toward relevant events using natural language prompts.
  * **Search summaries** : Gemini can automatically summarize search results after every search and subsequent filter action. Gemini can also answer contextual follow-up questions about the summaries it provides.
  * **Rule generation** : Gemini can create new YARA-L rules from the UDM search queries it generates.
  * **Security questions and threat intelligence analysis** : Gemini can answer general security domain questions and specific threat intelligence questions. Gemini can provide summaries about threat actors, IOCs, and other threat intelligence topics.
  * **Incident remediation** : Based on the event information returned, Gemini can suggest follow-on steps.



For more information, see [Use Gemini to investigate security issues](https://docs.cloud.google.com/chronicle/docs/secops/gemini-chronicle#investigation).

## May 03, 2024

Feature

**Create a new playbook using Gemini (Preview)**

You can now use Gemini to create a fully structured playbook. All you need to do is write a well structured prompt and click **Create**. For more information, see [Create playbook with Gemini](https://docs.cloud.google.com/chronicle/docs/secops/gemini-chronicle#playbook-gemini).

## May 02, 2024

Change

The following supported default parsers have changed. Each is listed by product name and `log_type` value, if applicable.

  * AIX system (`AIX_SYSTEM`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * Arista Switch (`ARISTA_SWITCH`)
  * Aruba (`ARUBA_WIRELESS`)
  * Aruba Switch (`ARUBA_SWITCH`)
  * Attivo Networks (`ATTIVO`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS Control Tower (`AWS_CONTROL_TOWER`)
  * AWS Elastic Load Balancer (`AWS_ELB`)
  * AWS WAF (`AWS_WAF`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure AD Organizational Context (`AZURE_AD_CONTEXT`)
  * Azure Application Gateway (`AZURE_GATEWAY`)
  * Azure Storage Audit (`AZURE_STORAGE_AUDIT`)
  * Azure WAF (`AZURE_WAF`)
  * Barracuda Firewall (`BARRACUDA_FIREWALL`)
  * BeyondTrust Endpoint Privilege Management (`BEYONDTRUST_ENDPOINT`)
  * BigQuery (`N/A`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Brocade Switch (`BROCADE_SWITCH`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * Cisco FireSIGHT Management Center (`CISCO_FIRESIGHT`)
  * Cisco Internetwork Operating System (`CISCO_IOS`)
  * Cisco ISE (`CISCO_ISE`)
  * Cisco Meraki (`CISCO_MERAKI`)
  * Cisco VPN (`CISCO_VPN`)
  * Cisco WLC/WCS (`CISCO_WIRELESS`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Claroty Enterprise Management Console (`CLAROTY_EMC`)
  * Cloud Audit Logs (`N/A`)
  * Cloud Intrusion Detection System (`GCP_IDS`)
  * Corelight (`CORELIGHT`)
  * CrowdStrike Detection Monitoring (`CS_DETECTS`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CyberArk (`CYBERARK`)
  * Cyberark Privilege Cloud (`CYBERARK_PRIVILEGE_CLOUD`)
  * Cybergatekeeper NAC (`CYBERGATEKEEPER_NAC`)
  * Darktrace (`DARKTRACE`)
  * Dell ECS Enterprise Object Storage (`DELL_ECS`)
  * Dell Switch (`DELL_SWITCH`)
  * Elastic Packet Beats (`ELASTIC_PACKETBEATS`)
  * ESET (`ESET_EDR`)
  * ESET AV (`ESET_AV`)
  * F5 Advanced Firewall Management (`F5_AFM`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * FireEye HX (`FIREEYE_HX`)
  * FireEye NX Audit (`FIREEYE_NX_AUDIT`)
  * Firewall Rule Logging (`N/A`)
  * Forcepoint DLP (`FORCEPOINT_DLP`)
  * Forescout NAC (`FORESCOUT_NAC`)
  * Forgerock OpenIdM (`FORGEROCK_OPENIDM`)
  * FortiGate (`FORTINET_FIREWALL`)
  * Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
  * Fortra Powertech SIEM Agent (`FORTRA_POWERTECH_SIEM_AGENT`)
  * Cloud NAT (`N/A`)
  * GCP_SWP (`GCP_SWP`)
  * Gitlab (`GITLAB`)
  * GMAIL Logs (`GMAIL_LOGS`)
  * GMV Checker ATM Security (`GMV_CHECKER`)
  * Guardicore Centra (`GUARDICORE_CENTRA`)
  * HPE BladeSystem C7000 (`HPE_BLADESYSTEM_C7000`)
  * HYPR MFA (`HYPR_MFA`)
  * IBM AS/400 (`IBM_AS400`)
  * IBM DS8000 Storage (`IBM_DS8000`)
  * IBM Guardium (`GUARDIUM`)
  * IBM Tape Storages (`IBM_LTO`)
  * IBM Tivoli (`IBM_TIVOLI`)
  * IBM-i Operating System (`IBM_I`)
  * Illumio Core (`ILLUMIO_CORE`)
  * Imperva (`IMPERVA_WAF`)
  * Imperva Advanced Bot Protection (`IMPERVA_ABP`)
  * Imperva SecureSphere Management (`IMPERVA_SECURESPHERE`)
  * Infoblox (`INFOBLOX`)
  * ION Spectrum (`ION_SPECTRUM`)
  * Ipswitch MOVEit Transfer (`IPSWITCH_MOVEIT_TRANSFER`)
  * Jamf Protect Alerts (`JAMF_PROTECT`)
  * Jamf Protect Telemetry (`JAMF_TELEMETRY`)
  * Juniper Junos (`JUNIPER_JUNOS`)
  * Juniper MX Router (`JUNIPER_MX`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * LastPass Password Management (`LASTPASS`)
  * Linux Auditing System (AuditD) (`AUDITD`)
  * McAfee Enterprise Security Manager (`MCAFEE_ESM`)
  * Medigate IoT (`MEDIGATE_IOT`)
  * Microsoft AD (`WINDOWS_AD`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Defender for Identity (`MICROSOFT_DEFENDER_IDENTITY`)
  * Microsoft Exchange (`EXCHANGE_MAIL`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft IAS Server (`MICROSOFT_IAS`)
  * Microsoft Intune (`AZURE_MDM_INTUNE`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * Mongo Database (`MONGO_DB`)
  * Netscout Arbor Sightline (`ARBOR_SIGHTLINE`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * NGFW Enterprise (`GCP_NGFW_ENTERPRISE`)
  * Office 365 (`OFFICE_365`)
  * Office 365 Message Trace (`OFFICE_365_MESSAGETRACE`)
  * Opengear Remote Management (`OPENGEAR`)
  * Oracle (`ORACLE_DB`)
  * OSQuery (`OSQUERY_EDR`)
  * OSSEC (`OSSEC`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Prisma Cloud (`PAN_PRISMA_CLOUD`)
  * PerimeterX Bot Protection (`PERIMETERX_BOT_PROTECTION`)
  * Phishlabs (`PHISHLABS`)
  * Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
  * Pulse Secure (`PULSE_SECURE_VPN`)
  * Riverbed Steelhead (`STEELHEAD`)
  * RSA SecurID Access Identity Router (`RSA_SECURID`)
  * SAP SM20 (`SAP_SM20`)
  * SAP SuccessFactors (`SAP_SUCCESSFACTORS`)
  * SAP Webdispatcher (`SAP_WEBDISP`)
  * Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
  * Security Command Center Threat (`N/A`)
  * Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
  * Sentinelone Alerts (`SENTINELONE_ALERT`)
  * SentinelOne EDR (`SENTINEL_EDR`)
  * SentinelOne Singularity Cloud Funnel (`SENTINELONE_CF`)
  * Snare System Diagnostic Logs (`SNARE_SOLUTIONS`)
  * Solaris system (`SOLARIS_SYSTEM`)
  * SonicWall (`SONIC_FIREWALL`)
  * Sonicwall Secure Mobile Access (`SONICWALL_SMA`)
  * Splunk Platform (`SPLUNK`)
  * Squid Web Proxy (`SQUID_WEBPROXY`)
  * Suricata EVE (`SURICATA_EVE`)
  * Suricata IDS (`SURICATA_IDS`)
  * Swift Alliance Messaging Hub (`SWIFT_AMH`)
  * Symantec CloudSOC CASB (`SYMANTEC_CASB`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Tenable OT (`TENABLE_OT`)
  * Tetragon Ebpf Audit Logs (`TETRAGON_EBPF_AUDIT_LOGS`)
  * Trellix HX Event Streamer (`TRELLIX_HX_ES`)
  * Trend Micro (`TIPPING_POINT`)
  * Trend Micro Cloud one (`TRENDMICRO_CLOUDONE`)
  * Trend Micro Deep Security (`TRENDMICRO_DEEP_SECURITY`)
  * TrendMicro Apex Central (`TRENDMICRO_APEX_CENTRAL`)
  * TrendMicro Web Proxy (`TRENDMICRO_WEBPROXY`)
  * Unifi AP (`UNIFI_AP`)
  * Unix system (`NIX_SYSTEM`)
  * Vectra Detect (`VECTRA_DETECT`)
  * VeridiumID by Veridium (`VERIDIUM_ID`)
  * VPC Flow Logs (`GCP_VPC_FLOW`)
  * Windows Defender ATP (`WINDOWS_DEFENDER_ATP`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Windows Network Policy Server (`WINDOWS_NET_POLICY_SERVER`)
  * Windows Sysmon (`WINDOWS_SYSMON`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * Workspace Alerts (`WORKSPACE_ALERTS`)
  * Workspace ChromeOS Devices (`WORKSPACE_CHROMEOS`)
  * Workspace Groups (`WORKSPACE_GROUPS`)
  * Workspace Mobile Devices (`WORKSPACE_MOBILE`)
  * Workspace Privileges (`WORKSPACE_PRIVILEGES`)
  * Workspace Users (`WORKSPACE_USERS`)
  * YAMAHA ROUTER RTX1200 (`YAMAHA_ROUTER`)
  * Zeek JSON (`BRO_JSON`)
  * Zimperium (`ZIMPERIUM`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * Zscaler CASB (`ZSCALER_CASB`)
  * ZScaler NGFW (`ZSCALER_FIREWALL`)



The following log types, without a default parser, were added. Each is listed by product name and `log_type` value, if applicable.

  * Adaxes (`ADAXES`)
  * Air Table (`AIR_TABLE`)
  * Alert Enterprise Guardian (`ALERT_GUARDIAN`)
  * Amavis (`AMAVIS`)
  * Atlassian Beacon (`ATLASSIAN_BEACON`)
  * Banner dd (`BANNER_DD`)
  * BetterStack Uptime (`BETTERSTACK_UPTIME`)
  * BloodHound (`BLOODHOUND`)
  * Core Privileged Access Manager (BoKS) (`BOKS`)
  * Cisco Secure Access (`CISCO_SECURE_ACCESS`)
  * Cleafy (`CLEAFY`)
  * Clear Bank Portal Audit (`CLEARBANK_PORTAL`)
  * CloudBees (`CLOUDBEES`)
  * Comforte SecurDPS (`COMFORTE_SECURDPS`)
  * Control Plane (`CONTROL_PLANE`)
  * Corrata (`CORRATA`)
  * Cubist Audit (`CUBIST_AUDIT`)
  * C Zentrix (`C_ZENTRIX`)
  * DefectDojo (`DEFECTDOJO`)
  * Dmarcian (`DMARCIAN`)
  * DocuSign (`DOCUSIGN`)
  * Duo Activity Logs (`DUO_ACTIVITY`)
  * E2 Guardian (`E2_GUARDIAN`)
  * Egress Defend (`EGRESS_DEFEND`)
  * Egress Prevent (`EGRESS_PREVENT`)
  * Emsisoft AntiVirus (`EMSISOFT_ANTIVIRUS`)
  * F5 System Logs (`F5_SYSTEM_LOGS`)
  * Fastly CDN (`FASTLY_CDN`)
  * FireEye CMS (`FIREEYE_CMS`)
  * Forcepoint Mail Relay (`FORCEPOINT_MAIL_RELAY`)
  * Google Ads (`GOOGLE_ADS`)
  * H3C Comware Platform Switch
  * Halcyon Anti Ransomware (`HALCYON`)
  * Halo (`HALO`)
  * HP Poly (`HP_POLY`)
  * Huawei CloudEngine (`HUAWEI_CLOUDENGINE`)
  * Intruder.IO (`INTRUDER_IO`)
  * Ivanti Connect Secure (`IVANTI_CONNECT_SECURE`)
  * Keyfactor (`KEYFACTOR`)
  * Kyverno (`KYVERNO`)
  * LaunchDarkly (`LAUNCH_DARKLY`)
  * LeanIX Enterprise (`LEANIX`)
  * Leanix CMDB (`LEANIX_CMDB`)
  * Lucid (`LUCID`)
  * Lumeta Spectre (`LUMETA`)
  * ManageEngine Asset Explorer (`MANAGE_ENGINE_ASSET_EXPLR`)
  * ManageEngine Endpoint Central (`MANAGE_ENGINE_ENDPT_CNTRL`)
  * Mandiant Digital Threat Monitoring (`MANDIANT_DTM_ALERTS`)
  * Manhattan Warehouse Management System (`MANHATTAN_WMS`)
  * Mend IO (`MEND_IO`)
  * Meta Marketing (`META_MARKETING`)
  * Miasma SecretScanner (`MIASMA_SECRETSCANNER`)
  * Microsoft Ads (`MICROSOFT_ADS`)
  * Microsoft Purview (`MICROSOFT_PURVIEW`)
  * ModSecurity (`MODSECURITY`)
  * Netapp Storagegrid (`NETAPP_STORAGEGRID`)
  * NetBrain (`NETBRAIN`)
  * Netenrich Entity Context (`NETENRICH_ENTITY_CONTEXT`)
  * Netwrix Activity Monitor (`NETWRIX_ACTIVITY_MONITOR`)
  * Netwrix Stealth Intercept (`NETWRIX_STEALTH_INTERCEPT`)
  * Netwrix Threat Manager (`NETWRIX_THREAT_MANAGER`)
  * Nexus Sonatype (`NEXUS_SONATYPE`)
  * Oracle Fusion (`ORACLE_FUSION`)
  * PAGELY (`PAGELY`)
  * Palantir (`PALANTIR`)
  * Proofpoint Meta (`PROOFPOINT_META`)
  * Qumulo FS (`QUMULO_FS`)
  * Radware Alteon (`RADWARE_ALTEON`)
  * SailPoint IdentityIQ (`SAILPOINT_IIQ`)
  * Sentinelone Activity (`SENTINELONE_ACTIVITY`)
  * Siga Level Zero OT Resilience (`SIGA`)
  * Site24x7 (`SITE24X7`)
  * Winevtlog Snare (`SNARE_WINEVTLOG`)
  * Solar System (`SOLAR_SYSTEM`)
  * Stealthbits DLP (`STEALTHBITS_DLP`)
  * Symantec VIP Authentication Hub (`SYMANTEC_VIP_AUTHHUB`)
  * Temenos Journey Manager System Event Publisher (`TEMENOS_MANAGER_SYSTEMEVENT`)
  * Teradata Aster (`TERADATA_ASTER`)
  * Tiktok for Developers (`TIKTOK`)
  * Transmit BindID (`TRANSMIT_BINDID`)
  * Trend Micro Vision One Audit (`TRENDMICRO_VISION_ONE_AUDIT`)
  * Trend Micro Vision One Observerd Attack Techniques (`TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES`)
  * Trend Micro Vision One Workbench (`TRENDMICRO_VISION_ONE_WORKBENCH`)
  * TrueNAS (`TRUENAS`)
  * E-Motional Transparent Screen Lock TSL RFID (`TSL_PRO`)
  * UPX AntiDDoS (`UPX_ANTIDDOS`)
  * Verba Recording System (`VERBA_REC`)
  * Vercara (`VERCARA`)
  * Veza Access Control Platform (`VEZA`)
  * Web Methods Api Gateway (`WEBMETHODS_API_GATEWAY`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## April 26, 2024

Feature

You can now set up feeds to push logs using an HTTPS endpoint by using either the [feed management user interface](https://docs.cloud.google.com/chronicle/docs/administration/feed-management) or the [feed management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api). You can use the following feed management source types to set up ingestion using an HTTPS endpoint:

  * Amazon Data Firehose
  * Google Cloud Pub/Sub
  * Webhooks



You can also generate a secret key and API key to authenticate feeds that use Amazon Data Firehose and webhooks as the feed source type.

Change

The [feed management](https://docs.cloud.google.com/chronicle/docs/administration/feed-management) feature is now enhanced to include the following:

  * **Feed names** : You can assign custom names to new and existing data feeds.
  * **Troubleshooting information** : You can diagnose error feeds by accessing detailed information about the cause of an issue and recommended actions.
  * **Last succeeded time** : Stay informed about the status of a feed, with a timestamp identifying when data was last successfully fetched by each feed.



## April 25, 2024

Announcement

Chronicle Security Operations (Chronicle SecOps) has been rebranded to Google Security Operations (Google SecOps). Both the logo and the platform name have been rebranded as part of this change. This rebranding reflects our commitment to bringing you the best of Google security operations features. There is no change to functionality in the platform.

## April 22, 2024

Deprecated

The ingestion alerting system using Chronicle has been deprecated. This system will no longer be updated, and no alerts will be sent from this system after September 01, 2024. We recommend that you use the Cloud Monitoring integration which provides more flexibility in alert logic, alert workflow, and integration with third-party ticketing systems.

Deprecated

The `ingestion_stats` table in BigQuery is deprecated and will no longer be updated after May 15, 2024. We recommend that you use the Chronicle `ingestion_metrics` table in BigQuery, which provides more accurate ingestion metrics.

## April 15, 2024

Deprecated

The following `labels` fields for UDM nouns are deprecated and these fields will not appear in the search results after November 29, 2024: `about.labels`, `intermediary.labels`, `observer.labels`, `principal.labels`, `src.labels`, `security_result.about.labels`, and `target.labels`. For existing parsers, in addition to these UDM fields, the logs fields are also mapped to key and value `additional.fields` UDM fields. For new parsers, the key and value settings in `additional.fields` UDM fields are used instead of the deprecated `labels` UDM fields. We recommend that you update the existing rules to use the key and value settings in the `additional.fields` UDM fields instead of the deprecated `labels` UDM fields.

## April 03, 2024

Announcement

On or after May 1, 2024, in an effort to improve enrichment quality, the [enrichment process using telemetry events and entities](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment#enrich_entities_merging) will prioritize values set by parsers over values from aliases in unenriched events. If a parser does not set the value, the enrichment process will set the enriched value to using aliases.

Feature

Curated Detections rule packs covering AWS threats are generally available to Chronicle Enterprise and Enterprise Plus customers.

## March 26, 2024

Announcement

[Gemini in Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/gemini-chronicle)

Duet AI in Google Cloud is now Gemini for Google Cloud. See our [blog post](https://blog.google/technology/ai/google-gemini-update-sundar-pichai-2024/) for more information.

## March 25, 2024

Feature

Chronicle Applied Threat Intelligence helps you identify and respond to threats. When enabled, it ingests IOCs curated by Mandiant Threat Intelligence with an IC-Score greater than 80 and generates an error when a match is found. The following are some of the features of Applied Threat Intelligence.

  * **Event-level enrichment** : All telemetry in Chronicle is enriched with Google Threat Intelligence which is a combination of Mandiant and Virus Total, including all threat intelligence associations like campaigns and actors.

  * **Sophisticated indicator matching** : Curated out-of-the-box detections that deliver sophisticated indicator matching using augmented prioritization logic, noise reduction based on customer environment context, and other correlation techniques to maximize signal to noise.

  * **Active breach alerting** : Uses Mandiant's incident response intelligence to alert on potential active breaches delivering on our _no patient 1_ vision. 

  * **Curated behavioral detections for emerging threats** : To protect against newly emerging risks and tactics, techniques, and procedures (TTPs), Applied Threat Intelligence uses real-time insights.

  * **DIY detection engineering and response automation** : Access to Fusion intelligence (formerly known as Mandiant Fusion) for the following.

    * Customer authoring of rules
    * Customer development of response playbooks
  * **Curated views for Investigation and triage Insights** : Applied Threat Intelligence provides curated views that show valuable associations between an indicator and threat actor, threat campaign, or malware, statistics about a threat observed in customer environments. These views are invaluable for all security operations workflows.




For more information about Applied Threat Intelligence, see [Applied Threat Intelligence overview](https://docs.cloud.google.com/chronicle/docs/detection).

This note incorrectly states that an error is generated when an IOC match is found. See the entry for May 8, 2024 for the updated statement.

## March 22, 2024

Feature

Chronicle now supports direct ingestion and parsing of [reCAPTCHA Enterprise logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-gcp-recaptcha-logs) from Google Cloud.

Feature

Chronicle has added a new rule set to [Cloud Threat Detections](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category) , called _Serverless Threats_ , that detects activity associated with potential compromise or abuse of server-less resources in Google Cloud, such as Cloud Run and Cloud Functions.

Change

There is no longer a limit on the number of feeds you can create for the same log type in Feed Management.

## March 20, 2024

Change

**Case filter and URL now in a reciprocal relationship**

In the **Cases** page, the filter and the URL now directly affect each other. Changing the filter changes the URL, and conversely, changing the URL changes the filter. You can take advantage of this feature by setting a filter for cases and putting the newly created URL in an external dashboard. Clicking on this link would then take you directly to the filtered case queue.

Feature

Chronicle has expanded [Cloud Threat Detections](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category) to create a detection when findings from Security Command Center [Event Threat Detections](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), [Cloud Armor](https://docs.cloud.google.com/armor/docs/cscc-findings), [Sensitive Actions Service](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview), and [Custom modules for Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview) are identified. These detections are available through the following rule sets: CDIR SCC Cloud IDS, CDIR SCC Cloud Armor, CDIR SCC Impact, CDIR SCC Enhanced Persistence, CDIR SCC Enhanced Defense Evasion, and CDIR SCC Custom Module.

## March 14, 2024

Change

The following supported default parsers have changed. Each is listed by product name and `log_type` value, if applicable.

  * Akamai WAF (`AKAMAI_WAF`)
  * Alcatel Switch (`ALCATEL_SWITCH`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * Auth0 (`AUTH_ZERO`)
  * AWS Cloudtrail (`AWS_CLOUDTRAIL`)
  * AWS Config (`AWS_CONFIG`)
  * AWS GuardDuty (`GUARDDUTY`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure App Service (`AZURE_APP_SERVICE`)
  * Azure Key Vault logging (`AZURE_KEYVAULT_AUDIT`)
  * BIND (`BIND_DNS`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Box (`BOX`)
  * Chrome Management (`N/A`)
  * Cisco AMP (`CISCO_AMP`)
  * Cisco Umbrella DNS (`UMBRELLA_DNS`)
  * Cisco VPN (`CISCO_VPN`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Cloud Audit Logs (`N/A`)
  * Cloudflare (`CLOUDFLARE`)
  * Cofense (`COFENSE_TRIAGE`)
  * Corelight (`CORELIGHT`)
  * CrowdStrike Falcon (`CS_EDR`)
  * CSV Custom IOC (`CSV_CUSTOM_IOC`)
  * Custom Application Access Logs (`CUSTOM_APPLICATION_ACCESS`)
  * Cybergatekeeper NAC (`CYBERGATEKEEPER_NAC`)
  * Extreme Wireless (`EXTREME_WIRELESS`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * Falco IDS (`FALCO_IDS`)
  * FireEye (`FIREEYE_ALERT`)
  * FireEye ETP (`FIREEYE_ETP`)
  * ForgeRock Identity Cloud (`FORGEROCK_IDENTITY_CLOUD`)
  * FortiGate (`FORTINET_FIREWALL`)
  * GCP_APP_ENGINE (`GCP_APP_ENGINE`)
  * HP Procurve Switch (`HP_PROCURVE`)
  * IAM Context (`N/A`)
  * IBM DB2 (`DB2_DB`)
  * IBM Mainframe Storage (`IBM_MAINFRAME_STORAGE`)
  * IBM Security Access Manager (`IBM_SAM`)
  * Illumio Core (`ILLUMIO_CORE`)
  * Imperva (`IMPERVA_WAF`)
  * Infoblox (`INFOBLOX`)
  * JAMF CMDB (`JAMF`)
  * KerioControl Firewall (`KERIOCONTROL`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft Azure Resource (`AZURE_RESOURCE_LOGS`)
  * Microsoft Defender For Cloud (`MICROSOFT_DEFENDER_CLOUD_ALERTS`)
  * Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
  * Microsoft Exchange (`EXCHANGE_MAIL`)
  * Microsoft Graph Activity Logs (`MICROSOFT_GRAPH_ACTIVITY_LOGS`)
  * Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
  * Microsoft IIS (`IIS`)
  * Microsoft System Center Endpoint Protection (`MICROSOFT_SCEP`)
  * Mobile Endpoint Security (`LOOKOUT_MOBILE_ENDPOINT_SECURITY`)
  * Mongo Database (`MONGO_DB`)
  * Netscout OCI (`NETSCOUT_OCI`)
  * Netskope (`NETSKOPE_ALERT`)
  * Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
  * Network Policy Server (`MICROSOFT_NPS`)
  * Nutanix Prism (`NUTANIX_PRISM`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * OpenCanary (`OPENCANARY`)
  * Ordr IoT (`ORDR_IOT`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Prisma Cloud (`PAN_PRISMA_CLOUD`)
  * PerimeterX Bot Protection (`PERIMETERX_BOT_PROTECTION`)
  * Phishlabs (`PHISHLABS`)
  * Proofpoint Sendmail Sentrion (`PROOFPOINT_SENDMAIL_SENTRION`)
  * Pulse Secure (`PULSE_SECURE_VPN`)
  * RH-ISAC (`RH_ISAC_IOC`)
  * SailPoint IAM (`SAILPOINT_IAM`)
  * Salesforce (`SALESFORCE`)
  * Sap Business Technology Platform (`SAP_BTP`)
  * Security Command Center Threat (`N/A`)
  * Sentinelone Alerts (`SENTINELONE_ALERT`)
  * Shibboleth IDP (`SHIBBOLETH_IDP`)
  * Sourcefire (`SOURCEFIRE_IDS`)
  * Splunk Attack Analyzer (`SPLUNK_ATTACK_ANALYZER`)
  * STIX Threat Intelligence (`STIX`)
  * Symantec CloudSOC CASB (`SYMANTEC_CASB`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Tanium Asset (`TANIUM_ASSET`)
  * Thinkst Canary (`THINKST_CANARY`)
  * Trend Micro Deep Security (`TRENDMICRO_DEEP_SECURITY`)
  * Vectra Detect (`VECTRA_DETECT`)
  * Vectra Stream (`VECTRA_STREAM`)
  * VeridiumID by Veridium (`VERIDIUM_ID`)
  * Wazuh (`WAZUH`)
  * Windows Defender ATP (`WINDOWS_DEFENDER_ATP`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * Windows Local Administrator Password Solution (`MICROSOFT_LAPS`)
  * wiz.io (`WIZ_IO`)
  * Workspace Activities (`WORKSPACE_ACTIVITY`)
  * XAMS by Xiting (`XITING_XAMS`)
  * Zscaler CASB (`ZSCALER_CASB`)
  * Zscaler DLP (`ZSCALER_DLP`)
  * Zscaler Internet Access Audit Logs (`ZSCALER_INTERNET_ACCESS`)



The following log types, without a default parser, were added. Each is listed by product name and `log_type` value, if applicable.

  * Aruba Switch (`ARUBA_SWITCH`)
  * Azure AD Password Protection (`AZURE_AD_PASSWORD_PROTECTION`)
  * Azure Front Door (`AZURE_FRONT_DOOR`)
  * Babelforce (`BABELFORCE`)
  * Cloudaware (`CLOUDAWARE`)
  * Coalition Control API (`COALITION`)
  * Crowdstrike Identity Protection Services (`CS_IDP`)
  * Cymulate (`CYMULATE`)
  * Dell ECS Enterprise Object Storage (`DELL_ECS`)
  * Google Cloud NGFW Enterprise (`GCP_NGFW_ENTERPRISE`)
  * Google Cloud Secure Web Proxy (`GCP_SWP`)
  * HaveIBeenPwned (`HIBP`)
  * HPE BladeSystem C7000 (`HPE_BLADESYSTEM_C7000`)
  * HP OpenView (`HP_OPENVIEW`)
  * IBM DS8000 Storage (`IBM_DS8000`)
  * IBM-i Operating System (`IBM_I`)
  * Multicom Switch (`MULTICOM_SWITCH`)
  * Nextthink Finder (`NEXTTHINK_FINDER`)
  * Palo Alto Cortex XDR Management Audit (`PAN_XDR_MGMT_AUDIT`)
  * PingIdentity Directory Server Logs (`PING_DIRECTORY`)
  * Prisma SD-WAN (`PRISMA_SD_WAN`)
  * Redhat Jboss (`REDHAT_JBOSS`)
  * SafeBreach (`SAFEBREACH`)
  * Scality Ring Audit (`SCALITY_RING_AUDIT`)
  * Sendsafely (`SENDSAFELY`)
  * Solace Pub Sub Cloud (`SOLACE_AUDIT`)
  * Sonicwall Secure Mobile Access (`SONICWALL_SMA`)
  * Sonrai Enterprise Cloud Security Solution (`SONRAI`)
  * Tenemos Journey Manager System Event Publisher (`TENEMOS_MANAGER_SYSTEMEVENT`)
  * TrueFort Platform (`TRUEFORT`)
  * Ubiquiti Accesspoint (`UBIQUITI_ACCESSPOINT`)
  * WithSecure Cloud Protection (`WITHSECURE_CLOUD`)
  * WithSecure Elements Connector (`WITHSECURE_ELEMENTS`)
  * YAMAHA ROUTER RTX1200 (`YAMAHA_ROUTER`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

Feature

[Forwarder troubleshooting guide](https://docs.cloud.google.com/chronicle/docs/install/troubleshoot-forwarder) is now available to help you diagnose and resolve common issues that may arise while using the Chronicle Linux forwarder.

## March 13, 2024

Change

In the Entity Explorer page, **Case Distribution** has been renamed to **Alert Distribution**.

Feature

**Jobs Enhancement**

When updating an integration, the jobs will now be updated automatically. This does not apply to any legacy jobs that were created before October 2023.

The Marketplace integration will clearly identify the legacy jobs that are affected and provide instructions on how to proceed. 

In addition, legacy jobs are now marked as such in the Jobs Scheduler page so that you can take action and resolve issues beforehand.

## February 22, 2024

Deprecated

The following APIs have been deprecated and will be deleted in 6 months.

  * GET `/api/external/v1/connectors/GetConnectorsData`
  * POST `/api/external/v1/connectors/DeleteConnector`
  * POST `/api/external/v1/connectors/AddOrUpdateConnector`
  * POST `/api/external/v1/connectors/UpdateConnectorFromIde`
  * POST `/api/external/v1/connectors/GetConnectorStatus`



For each API above, there are one or more alternative endpoints that you can use as shown below:

Instead of   
GET `/api/external/v1/connectors/GetConnectorsData`  


Use one of the following:

  * `GET /api/external/v1/connectors/template-cards`   
Provides basic information per each accessible connector definition.

  * `POST /api/external/v1/connectors/template`  
Retrieves detailed information regarding a specific connector definition.

  * `GET /api/external/v1/connectors/cards`   
Provides basic information per each accessible connector.

  * `GET /api/external/v1/connectors/{identifier}`   
Retrieves detailed information regarding a specific connector instance.




Instead of   
POST `/api/external/v1/connectors/DeleteConnector`  
Use   
DELETE `/api/external/v1/connectors/{identifier}`

Instead of   
POST `/api/external/v1/connectors/AddOrUpdateConnector`   
Use   
`POST /api/external/v1/connectors`

Instead of   
POST `/api/external/v1/connectors/UpdateConnectorFromIde`  
Use   
POST `/api/external/v1/connectors/update-from-ide`

Instead of   
POST `/api/external/v1/connectors/GetConnectorStatus`   
Use   
GET `/api/external/v1/connectors/{identifier}/statistics`

## February 20, 2024

Feature

Google has added Tokyo (Japan) as a new region for Chronicle customers. Chronicle can now store customer data in this region. This also adds a new regional endpoint for Chronicle APIs at `https://asia-northeast1-backstory.googleapis.com`.

Change

The following supported default parsers have changed. Each is listed by product name and `log_type` value, if applicable.

  * A10 Load Balancer (`A10_LOAD_BALANCER`)
  * Anomali (`ANOMALI_IOC`)
  * Apache (`APACHE`)
  * Arcsight CEF (`ARCSIGHT_CEF`)
  * AWS CloudWatch (`AWS_CLOUDWATCH`)
  * AWS EC2 Hosts (`AWS_EC2_HOSTS`)
  * AWS EC2 Instances (`AWS_EC2_INSTANCES`)
  * AWS EC2 VPCs (`AWS_EC2_VPCS`)
  * Azure AD (`AZURE_AD`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure DevOps Audit (`AZURE_DEVOPS`)
  * Azure Firewall (`AZURE_FIREWALL`)
  * BIND (`BIND_DNS`)
  * BloxOne Threat Defense (`BLOXONE`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Carbon Black (`CB_EDR`)
  * Cato Networks (`CATO_NETWORKS`)
  * CENSYS (`CENSYS`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Chrome Management (`N/A`)
  * Cisco IronPort (`CISCO_IRONPORT`)
  * Cisco Meraki (`CISCO_MERAKI`)
  * Cisco Prime (`CISCO_PRIME`)
  * Cisco Secure Workload (`CISCO_SECURE_WORKLOAD`)
  * Citrix Netscaler (`CITRIX_NETSCALER`)
  * Cloud Audit Logs (`N/A`)
  * Cloud Load Balancing (`GCP_LOADBALANCING`)
  * Cloud Run (`GCP_RUN`)
  * Cloudflare (`CLOUDFLARE`)
  * CommVault Commcell (`COMMVAULT_COMMCELL`)
  * Compute Context (`N/A`)
  * Corelight (`CORELIGHT`)
  * CrowdStrike Detection Monitoring (`CS_DETECTS`)
  * CSV Custom IOC (`CSV_CUSTOM_IOC`)
  * Cybereason EDR (`CYBEREASON_EDR`)
  * Dataminr Alerts (`DATAMINR_ALERT`)
  * Elastic Windows Event Log Beats (`ELASTIC_WINLOGBEAT`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * FireEye ETP (`FIREEYE_ETP`)
  * Forescout NAC (`FORESCOUT_NAC`)
  * ForgeRock OpenAM (`OPENAM`)
  * IBM WebSEAL (`IBM_WEBSEAL`)
  * Imperva (`IMPERVA_WAF`)
  * Imperva Database (`IMPERVA_DB`)
  * Infoblox RPZ (`INFOBLOX_RPZ`)
  * ISC DHCP (`ISC_DHCP`)
  * Juniper (`JUNIPER_FIREWALL`)
  * Linux Sysmon (`LINUX_SYSMON`)
  * LogonBox (`LOGONBOX`)
  * ManageEngine ADAudit Plus (`ADAUDIT_PLUS`)
  * Micro Focus iManager (`MICROFOCUS_IMANAGER`)
  * Microsoft AD (`WINDOWS_AD`)
  * Microsoft ATA (`MICROSOFT_ATA`)
  * Microsoft Azure Activity (`AZURE_ACTIVITY`)
  * Microsoft Defender For Cloud (`MICROSOFT_DEFENDER_CLOUD_ALERTS`)
  * Microsoft Exchange (`EXCHANGE_MAIL`)
  * Microsoft IIS (`IIS`)
  * Netskope (`NETSKOPE_ALERT`)
  * Netskope CASB (`NETSKOPE_CASB`)
  * Ntopng (`NTOPNG`)
  * Office 365 (`OFFICE_365`)
  * OpenCanary (`OPENCANARY`)
  * OpenSSH (`OPENSSH`)
  * OSSEC (`OSSEC`)
  * Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Palo Alto Panorama (`PAN_PANORAMA`)
  * Quest Active Directory (`QUEST_AD`)
  * Recordia (`RECORDIA`)
  * Sangfor Next Generation Firewall (`SANGFOR_NGAF`)
  * SAP SM20 (`SAP_SM20`)
  * Security Command Center Threat (`N/A`)
  * SEPPmail Secure Email (`SEPPMAIL`)
  * ServiceNow CMDB (`SERVICENOW_CMDB`)
  * Snare System Diagnostic Logs (`SNARE_SOLUTIONS`)
  * Solaris system (`SOLARIS_SYSTEM`)
  * STIX Threat Intelligence (`STIX`)
  * Symantec CloudSOC CASB (`SYMANTEC_CASB`)
  * Symantec Web Security Service (`SYMANTEC_WSS`)
  * Trend Micro Deep Security (`TRENDMICRO_DEEP_SECURITY`)
  * Veritas NetBackup (`VERITAS_NETBACKUP`)
  * VMware ESXi (`VMWARE_ESX`)
  * Watchguard EDR (`WATCHGUARD_EDR`)
  * WindChill (`WINDCHILL`)
  * Windows Defender AV (`WINDOWS_DEFENDER_AV`)
  * Windows DNS (`WINDOWS_DNS`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * wiz.io (`WIZ_IO`)
  * Zeek JSON (`BRO_JSON`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * Zscaler CASB (`ZSCALER_CASB`)
  * Zscaler Internet Access Audit Logs (`ZSCALER_INTERNET_ACCESS`)
  * Zscaler Private Access (`ZSCALER_ZPA`)



The following log types, without a default parser, were added. Each is listed by product name and `log_type` value, if applicable.

  * Arista Guardian For Network Identity (`ARISTA_AGNI`)
  * HPE Aruba Networking Central (`ARUBA_CENTRAL`)
  * Blackberry Workspaces (`BLACKBERRY_WORKSPACES`)
  * Barracuda CloudGen Firewall (`BARRACUDA_CLOUDGEN_FIREWALL`)
  * Blackberry Workspaces (`BLACKBERRY_WORKSPACES`)
  * Cisco EStreamer (`CISCO_ESTREAMER`)
  * Cyderes IOC (`CYDERES_IOC`)
  * Dataiku DSS Logging (`DATAIKU_DSS_LOGS`)
  * Edgecore Networks (`EDGECORE_NETWORKS`)
  * Fisglobal Quantum (`FISGLOBAL_QUANTUM`)
  * ForgeRock Identity Cloud (`FORGEROCK_IDENTITY_CLOUD`)
  * Forgerock OpenIdM (`FORGEROCK_OPENIDM`)
  * FS-ISAC IOC (`FS_ISAC_IOC`)
  * Genetec Audit (`GENETEC_AUDIT`)
  * HiBob (`HIBOB`)
  * Imperva Audit Trail (`IMPERVA_AUDIT_TRAIL`)
  * KerioControl Firewall (`KERIOCONTROL`)
  * Looker Audit (`LOOKER_AUDIT`)
  * Mobile Endpoint Security (`LOOKOUT_MOBILE_ENDPOINT_SECURITY`)
  * ManageEngine PAM360 (`MANAGE_ENGINE_PAM360`)
  * Melissa (`MELISSA`)
  * Microsoft CASB Files & Entities (`MICROSOFT_CASB_CONTEXT`)
  * Windows Local Administrator Password Solution (`MICROSOFT_LAPS`)
  * Network Policy Server (`MICROSOFT_NPS`)
  * Power BI Activity Log (`MICROSOFT_POWERBI_ACTIVITY_LOG`)
  * Nxlog Agent (`NXLOG_AGENT`)
  * Nxlog Fim (`NXLOG_FIM`)
  * Opus Codec (`OPUS`)
  * Oracle NetSuite (`ORACLE_NETSUITE`)
  * Pega Automation (`PEGA`)
  * Qualys Knowledgebase (`QUALYS_KNOWLEDGEBASE`)
  * RealiteQ (`REALITEQ`)
  * SAP Webdispatcher (`SAP_WEBDISP`)
  * Serpico (`SERPICO`)
  * Software House Ccure9000 (`SOFTWARE_HOUSE_CCURE9000`)
  * Spirion (`SPIRION`)
  * Spur data feeds (`SPUR_FEEDS`)
  * Swift (`SWIFT`)
  * Technitium DNS (`TECHNITIUM_DNS`)
  * Tetragon Ebpf Audit Logs (`TETRAGON_EBPF_AUDIT_LOGS`)
  * Trend Micro Email Security Advanced (`TRENDMICRO_EMAIL_SECURITY`)
  * Tridium Niagara Framework (`TRIDIUM_NIAGARA_FRAMEWORK`)
  * VeridiumID by Veridium (`VERIDIUM_ID`)
  * Wallarm Webhook Notifications (`WALLARM_NOTIFICATIONS`)
  * Winscp (`WINSCP`)
  * XAMS by Xiting (`XITING_XAMS`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

Feature

Chronicle now supports the `timestamp.get_date()` function. For more information and example usage, see [YARA-L 2.0 language syntax](https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-syntax#timestampget_date).

## February 19, 2024

Announcement

The AI Investigation widget is now available in Europe. For more information, refer to [AI Investigation widget](https://docs.cloud.google.com/chronicle/docs/secops/duet-ai-chronicle#ai-widget).

## February 12, 2024

Feature

[Risk Analytics](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-overview)

Google has introduced Risk Analytics to Chronicle. Risk Analytics looks for patterns of risk across your enterprise, assigning risk scores to all entities and activities. These scores are surfaced in the [Risk Analytics dashboard](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard) which lets you better understand risk in your environment by visualizing entity risk trends. The dashboard helps you to identify unusual behavior and the potential risk that entities pose to your enterprise. You can specify watchlists of entities you suspect of having greater risk. The watchlists let you more easily monitor risk within your environment. 

Risk Analytics also provides both [predefined curated detections](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-ueba-category) and [YARA-L metric functions](https://docs.cloud.google.com/chronicle/docs/detection/metrics-functions) for authoring custom rules.

Risk Analytics is available with Enterprise and Enterprise Plus licenses.

Change

When the data ingestion rate for a tenant reaches a certain threshold, Chronicle controls the rate of ingestion for new data feeds to prevent a source with a high ingestion rate from affecting the ingestion rate of another data source. The ingestion volume and tenant's usage history determine the threshold. If the rate of ingestion does not deviate greatly then there is no effect on the ingestion rate.

Change

Chronicle requires a minimum Transport Layer Security (TLS) version of 1.2 to maintain security compliance. Ingestion routing connections that use lower TLS versions are automatically blocked. Upgrade any custom ingestion mechanisms to adhere to TLS 1.2 or higher.

## February 08, 2024

Announcement

**Email settings: customer configuration change**

In order to help with safe and secure communication, the **Trust Certificate** checkbox is scheduled to be deleted in April 2024 as it will be enabled automatically by default.

Customers who currently do _not_ have this checkbox enabled are advised to carry out the following procedure.

  * In the **Email Settings** > **Customer Configuration** tab, enable the **Trust Certificate** checkbox. 
  * Save the settings. 
  * Click **Test** to ensure the configuration works.
  * Perform an action which will trigger a test email notification. 
  * If errors are shown, follow the instructions in the error message.



Feature

**New audit logs**

The platform now captures audit logs when a playbook folder is deleted.

## January 31, 2024

Feature

The following log types were added to the Chronicle feed management API to create AWS data feeds. These feeds can be used to get context on AWS resources such as EC2 instances and users in identity and access management (IAM). Each is listed by product name and `log_type` value, if applicable.

  * AWS EC2 Hosts (`AWS_EC2_HOSTS`)
  * AWS EC2 Instances (`AWS_EC2_INSTANCES`)
  * AWS EC2 VPCs (`AWS_EC2_VPCS`)
  * AWS Identity and Access Management (`AWS_IAM`)



To view a list of log types that Chronicle supports for third-party APIs, see [Configuration by log type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#api-log-types).

Feature

The Detection Engine added support for event variable joins on `or` expressions and function calls. For examples, see [Event variable join requirements](https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-syntax#event_variable_join_requirements).

## January 24, 2024

Feature

Chronicle has expanded [Cloud Threat Detections](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category) to alert on findings from GCP Security Command Center [Event Threat Detections](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), [Virtual Machine Threat Detections](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview), and [Container Threat Detections](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview). These passthrough detections are available through the following packs: CDIR SCC Enhanced Exfiltration, CDIR SCC Enhanced Defense Evasion, CDIR SCC Enhanced Malware, CDIR SCC Enhanced Persistence, CDIR SCC Enhanced Privilege Escalation, CDIR SCC Credential Access, CDIR SCC Enhanced Discovery, CDIR SCC Brute Force, CDIR SCC Data Destruction, CDIR SCC Inhibit System Recovery, CDIR SCC Execution, CDIR SCC Initial Access, CDIR SCC Impair Defenses.

Change

[Chronicle Curated Detections](https://docs.cloud.google.com/chronicle/docs/detection/curated-detections) has been enhanced with new detection content for [Linux Threats](https://docs.cloud.google.com/chronicle/docs/detection/linux-threats-category). These new rule sets help identify malware and suspicious activity in Linux environments.

## January 17, 2024

Change

The following changes are available in the Unified Data Model.

  * New objects were added: 

    * `DNSRecord`
    * `Favicon`
    * `ThreatVerdict`
    * `PopularityRank`
    * `SSLCertificate`
    * `SSLCertificate.AuthorityKeyId`
    * `SSLCertificate.CertSignature`
    * `SSLCertificate.DSA`
    * `SSLCertificate.EC`
    * `SSLCertificate.Extension`
    * `SSLCertificate.PublicKey`
    * `SSLCertificate.RSA`
    * `SSLCertificate.Subject`
    * `SSLCertificate.Validity`
    * `Tracker`
    * `Url`
    * `SecurityResult.AnalyticsMetadata`
  * A new field was added to `Noun`: `url_metadata`.

  * New fields were added to `SecurityResult`: 

    * `ruleset_category_display_name`
    * `confidence_score`
    * `analytics_metadata`
    * `threat_verdict`
    * `last_discovered_time`
  * New fields were added to `Domain`: 

    * `last_dns_records`
    * `categories`
    * `favicon`
    * `jarm`
    * `last_dns_records`
    * `last_dns_records_time`
    * `last_https_certificate`
    * `last_https_certificate_time`
    * `popularity_ranks`
    * `tags`
    * `whois_time`
  * New fields were added to `File`: `security_result` and `main_icon`.

  * New fields were added to `SecurityResult.Association`: `sponsor_region`, `targeted_regions`, and `tags`.

  * New values were added to `File.FileType`: 

`FILE_TYPE_DWG` | `FILE_TYPE_DXF`  
---|---  
`FILE_TYPE_THREEDS` | `FILE_TYPE_WEBM`  
`FILE_TYPE_MKV` | `FILE_TYPE_ONE_NOTE`  
`FILE_TYPE_OOXML` | `FILE_TYPE_ZST`  
`FILE_TYPE_LZFSE` | `FILE_TYPE_PYTHON_WHL`  
`FILE_TYPE_PYTHON_PKG` | `FILE_TYPE_M4`  
`FILE_TYPE_OBJETIVEC` | `FILE_TYPE_JMOD`  
`FILE_TYPE_MAKEFILE` | `FILE_TYPE_INI`  
`FILE_TYPE_CLJ` | `FILE_TYPE_PDB`  
`FILE_TYPE_SQL` | `FILE_TYPE_NEKO`  
`FILE_TYPE_WER` | `FILE_TYPE_GOLANG`  
`FILE_TYPE_SGML` | `FILE_TYPE_JSON`  
`FILE_TYPE_CSV` | `FILE_TYPE_SQUASHFS`  
`FILE_TYPE_VHD` | `FILE_TYPE_IPS`  
`FILE_TYPE_PEM` | `FILE_TYPE_PGP`  
`FILE_TYPE_CRT` | `FILE_TYPE_PYC`  
  * New values were added to `Metric.Dimension`: 

    * `PRINCIPAL_PROCESS_FILE_PATH`
    * `PRINCIPAL_PROCESS_FILE_HASH`
    * `SECURITY_RESULT_RULE_NAME`
  * A new value was added to `Metric.MetricName`: `ALERT_EVENT_NAME_COUNT`.

  * A new value was added to `SecurityResult.ProductSeverity`: `NONE`. 




For a list of all fields in the Unified Data Model, and their descriptions, see the [Unified Data Model field list](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list).

Change

The following supported default parsers have changed. Each is listed by product name and `log_type` value, if applicable.

  * ADVA Fiber Service Platform (`ADVA_FSP`)
  * Anomali (`ANOMALI_IOC`)
  * Apache (`APACHE`)
  * AWS EMR (`AWS_EMR`)
  * AWS Route 53 DNS (`AWS_ROUTE_53`)
  * AWS WAF (`AWS_WAF`)
  * Azure AD Directory Audit (`AZURE_AD_AUDIT`)
  * Azure Application Gateway (`AZURE_GATEWAY`)
  * BIND (`BIND_DNS`)
  * Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
  * Carbon Black (`CB_EDR`)
  * Check Point (`CHECKPOINT_FIREWALL`)
  * Cisco ASA (`CISCO_ASA_FIREWALL`)
  * Cisco DNA Center Platform (`CISCO_DNAC`)
  * Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
  * CrowdStrike Falcon (`CS_EDR`)
  * Darktrace (`DARKTRACE`)
  * Deep Instinct EDR (`DEEP_INSTINCT_EDR`)
  * Elastic Windows Event Log Beats (`ELASTIC_WINLOGBEAT`)
  * Extreme Networks Switch (`EXTREME_SWITCH`)
  * F5 ASM (`F5_ASM`)
  * F5 BIGIP LTM (`F5_BIGIP_LTM`)
  * Forescout NAC (`FORESCOUT_NAC`)
  * Fortinet FortiClient (`FORTINET_FORTICLIENT`)
  * GitHub (`GITHUB`)
  * GMAIL Logs (`GMAIL_LOGS`)
  * IBM DB2 (`DB2_DB`)
  * IBM Guardium (`GUARDIUM`)
  * Jamf Protect Alerts (`JAMF_PROTECT`)
  * Juniper (`JUNIPER_FIREWALL`)
  * Kubernetes Node (`KUBERNETES_NODE`)
  * Mandiant Custom IOC (`MANDIANT_CUSTOM_IOC`)
  * Mattermost (`MATTERMOST`)
  * Microsoft Exchange (`EXCHANGE_MAIL`)
  * Microsoft IIS (`IIS`)
  * Microsoft SQL Server (`MICROSOFT_SQL`)
  * Nutanix Prism (`NUTANIX_PRISM`)
  * Office 365 (`OFFICE_365`)
  * Okta (`OKTA`)
  * Palo Alto Cortex XDR Events (`PAN_CORTEX_XDR_EVENTS`)
  * Palo Alto Networks Firewall (`PAN_FIREWALL`)
  * Proofpoint Observeit (`OBSERVEIT`)
  * RH-ISAC (`RH_ISAC_IOC`)
  * SAP SAST Suite (`SAP_SAST`)
  * Security Command Center Threat (`N/A`)
  * SentinelOne Singularity Cloud Funnel (`SENTINELONE_CF`)
  * Symantec DLP (`SYMANTEC_DLP`)
  * Talon (`TALON`)
  * Tanium Stream (`TANIUM_TH`)
  * Trend Micro Apex one (`TRENDMICRO_APEX_ONE`)
  * Windows Event (`WINEVTLOG`)
  * Windows Event (XML) (`WINEVTLOG_XML`)
  * wiz.io (`WIZ_IO`)
  * Zscaler (`ZSCALER_WEBPROXY`)
  * Zscaler CASB (`ZSCALER_CASB`)
  * Zscaler Tunnel (`ZSCALER_TUNNEL`)



The following log types, without a default parser, were added. Each is listed by product name and `log_type` value, if applicable.

  * Asimily (`ASIMILY`)
  * Checkpoint Gaia (`CHECKPOINT_GAIA`)
  * Cisco Cyber Vision (`CISCO_CYBER_VISION`)
  * Cisco IronPort (`CISCO_IRONPORT`)
  * Cyber 2.0 IDS (`CYBER_2_IDS`)
  * CypherTrust Manager (`CYPHERTRUST_MANAGER`)
  * Duo Trust Monitor (`DUO_TRUST_MONITOR`)
  * Extreme Wireless (`EXTREME_WIRELESS`)
  * FireEye PX (`FIREEYE_PX`)
  * Harfanglab EDR (`HARFANGLAB_EDR`)
  * ImageNow (`IMAGENOW`)
  * INFINICO NetWyvern Series Appliance (`INFINICO_NETWYVERN`)
  * Quest CA Audit (`QUEST_CA_AUDIT`)
  * Quest Change Auditor for EMC (`QUEST_CHANGE_AUDITOR_EMC`)
  * Quest File Access Audit (`QUEST_FILE_AUDIT`)
  * RadiFlow IDS (`RADIFLOW_IDS`) rigo (`SENTRIGO`)
  * SEPPmail Secure Email (`SEPPMAIL`)
  * SpecterX (`SPECTERX`)
  * ViaControl Server Application (`VIACONTROL`)
  * WindChill (`WINDCHILL`)
  * WS Ftp (`WS_FTP`)



For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## January 16, 2024

Feature

[UDM Search for entity investigation](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search-investigate-entity)

UDM Search now includes a feature that lets you investigate entities (for example, an IP address, user, or asset) in addition to the events and alerts that match the search query terms. UDM Search query conditions can include both UDM fields (for example, `principal.hostname="alice"`) and grouped fields (for example, `hostname="alice"`). When a search query includes a condition that identifies a specific entity, the search results include details about that entity in addition to UDM events that match the entire search query.

## January 04, 2024

Feature

**Additional support for trimming large alerts**

In order to prevent performance issues, when an alert contains over 500 entities, the alert is ingested with the key entities retained and the additional entities are removed. 

This trimming support works in parallel with the current trimming mechanism as defined in [Handle large alerts ](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/handle-large-alerts).

Feature

**New placeholders added**

A new category of placeholders have been added to the SOAR side of the platform which focus on the current state of the session, such as logged-in user and the platform. These can be used in a variety of scenarios. For example, you can use them in an HTML widget to create customized information specifically for logged-in users as opposed to the users assigned to the case. 

A new section called General has been added to the placeholders. It contains the following placeholders

  * HostUrl
  * CurrentUserEmail
  * CurrentUserID
  * CurrentUserFullName
  * CurrentUserRole



Note that the Current User placeholders cannot be used in playbooks or jobs.

## December 13, 2023

Feature

[Duet AI in Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/duet-ai-chronicle)

The following Duet AI features are now available to Chronicle Security Operations customers:

  * You can now use [Duet AI to search your event data using natural language](https://docs.cloud.google.com/chronicle/docs/secops/duet-ai-chronicle#nl-to-udm). Duet AI can translate natural language into Chronicle's unified data model, letting you search your event data without having to know YARA-L to craft custom queries.

  * You can now use the [AI Investigation widget](https://docs.cloud.google.com/chronicle/docs/secops/duet-ai-chronicle#ai-widget) to look at the whole case (alerts, events, and entities). The AI Investigation widget also provides an AI-generated case summary of how much attention the case might require, summarizes the alerts data to better understand the threat, and recommends next steps to be taken for effective remediation. The AI Investigation widget is available in the United States only.




## September 19, 2023

Announcement

Welcome to Chronicle Security Operations (SecOps), a Google Cloud service built as a specialized layer on top of Google's core infrastructure, designed for enterprises to privately retain, analyze, and search petabytes of security and network telemetry. 

The SecOps platform provides instant context about suspicious and malicious activity. It can be used to detect threats, investigate the scope and cause of those threats, and provide remediation using pre-built integrations with enterprise workflow, response, and orchestration platforms. 

The SecOps platform fuses key capabilities of Security Information and Event Management (SIEM), Security Orchestration, Automation, and Response (SOAR) and Threat Intelligence from Google Cloud, VirusTotal, and Mandiant.

The Chronicle SecOps platform enables security analysts to analyze and mitigate a security threat throughout its lifecycle by employing the following capabilities:

**Collection** : Data is ingested into the platform using software forwarders, parsers, connectors, and webhooks.

**Detection** : This data is aggregated, normalized using the Universal Data Model (UDM), and linked to detections and threat intelligence.

**Investigation** : Threats are investigated through case management, search, collaboration, and contextual mapping.

**Response** : Security analysts can respond quickly and provide resolutions using automated playbooks, incident management, and closed-loop feedback.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
