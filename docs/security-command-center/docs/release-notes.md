---
url: https://docs.cloud.google.com/security-command-center/docs/release-notes/
title: Security Command Center release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:09:37.016430+00:00
---

# Security Command Center release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Resources ](https://docs.cloud.google.com/security-command-center/docs/resources)



Send feedback 

#  Security Command Center release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Security Command Center. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/scc-release-notes.xml) directly. 

## October 19, 2026

Feature

You can view issues created by Correlated Threats and security graph rules at the folder or project level. On the **Issues** page, you can filter all issues by service type, project number, and folder ID. For more information, see [Issues overview](https://docs.cloud.google.com/security-command-center/docs/issues-overview).

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 15, 2026

Feature

To increase the precision of attack path analysis and provide attack exposure scores that help you prioritize confirmed internet exposures, Risk Engine attack path simulations support the `EXTERNALLY_EXPOSED_VM_INSTANCE` [External Exposure finding category](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#external-exposure-findings) ([Preview](https://cloud.google.com/products/#product-launch-stages)). This finding category identifies Compute Engine or Google Kubernetes Engine (GKE) resources with a direct public IP address that allows host OS access.

For more information, see [Detect exposed resources](https://docs.cloud.google.com/security-command-center/docs/detect-external-exposure), [Risk Engine feature support](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#external-exposure-aes-support), and [Overview of attack exposure scores and attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn).

## October 09, 2026

Feature

Using gcloud CLI, the `securitycenter` REST API, or client libraries, you can configure Pub/Sub and BigQuery continuous export to receive notifications when findings are deleted from Security Command Center due to data retention policies.

For more information, see the following:

  * [Enable finding notifications for Pub/Sub](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications)
  * [Stream findings to BigQuery for analysis](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query)
  * [Enable real-time notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-enable-real-time-notifications)
  * [Creating and managing Notification Configs](https://docs.cloud.google.com/security-command-center/docs/how-to-api-manage-notifications)



## October 06, 2026

Deprecated

Artifact guard with CI/CD integration is deprecated. It will be shut down on October 30, 2026.

## September 29, 2026

Feature

Event Threat Detection integrates with Sensitive Data Protection to enrich findings that affect sensitive resources.

For more information, see [Sensitive data enrichment](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#sdp-enrichment).

## September 28, 2026

Feature

Risk Engine detects and reports reasoning engines that can modify IAM policies and perform lateral movement. These findings are generated as a [toxic combination](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview).

## September 24, 2026

Change

The following Security Command Center finding category names from AI Protection have new names to clarify that AI Protection detects tuned models and to remove the legacy `VERTEX_1P_` prefix:

  * `VERTEX_1P_TUNED_MODEL_DETECTED` changes to `TUNED_MODEL_DETECTED`.
  * `VERTEX_1P_TUNED_MODEL_NOT_PROTECTED_BY_MODEL_ARMOR` changes to `TUNED_MODEL_NOT_PROTECTED_BY_MODEL_ARMOR`.



For more information about AI Protection findings, see [AI Protection overview](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) and [AI Discovery service findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#aip-ds-findings).

## September 16, 2026

Feature

You can use the following MCP server endpoints to enable LLM agents to perform investigative and management tasks in Security Command Center.

  * [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/reference/mcp)
  * [Security Command Center Management](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/mcp)



This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## September 14, 2026

Deprecated

Data Security Posture Management is deprecated. It will be shut down on February 1, 2027. Learn more about the controls and [alternative detection capabilities](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-security-framework).

## August 13, 2026

Feature

[AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) supports data residency in the Kingdom of Saudi Arabia (KSA) for all Security Command Center service tiers.

For more information, see [Planning for data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support).

## August 10, 2026

Feature

The integration of Security Command Center with [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview) for application lifecycle security assessments is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Design-time findings are sent to Security Command Center on demand during deployment. This feature lets you filter findings by App Hub application at the app-enabled folder and project levels.

For more information, see [Application lifecycle security assessments](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#application-security-assessments).

Feature

[Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud) is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

## August 04, 2026

Feature

Security Command Center released new **Malicious Skill** runtime threat detectors for Google Kubernetes Engine (GKE), Cloud Run, and Agent Platform. These detectors identify when a malicious skill (an AI agent capability) is executed or loaded. A malicious skill is any malicious binary that has been tagged as an LLM skill by Google's threat intelligence.

For more information, see the following:

  * [Container Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)
  * [Cloud Run Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview)
  * [Agent Platform overview](https://docs.cloud.google.com/security-command-center/docs/agent-platform-threat-detection-overview)



## August 03, 2026

Feature

The Assured Open Source Software Premium tier supports JavaScript (NPM) packages for Node.js environments.

For more information, see [Download NPM packages using direct repository access](https://docs.cloud.google.com/security-command-center/docs/aoss-download-npm-packages) and [List of supported NPM packages for the Assured Open Source Software premium tier](https://docs.cloud.google.com/security-command-center/docs/aoss-supported-packages-npm-premium).

Feature

For the Security Command Center Standard tier, [AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) is supported for both projects and organizations.

Project-level activations for the Standard tier include access to the [AI security dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#ai-protection), basic inventory view (excluding Gemini models), and baseline security findings.

Some features of AI Protection are only available for the Premium and Enterprise tiers or for organization-level activations. For more information, see [Configure AI Protection](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection).

## July 31, 2026

Feature

Organizations that are enrolled in the data residency Preview program can update their organization's [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) and [data encryption](https://docs.cloud.google.com/security-command-center/docs/cmek) configuration. For more information, see [Modify data residency or data encryption configuration](https://docs.cloud.google.com/security-command-center/docs/modify-data-residency-encryption).

Feature

Agent Platform Vulnerability Assessment ([Preview](https://cloud.google.com/products/#product-launch-stages)) scans for plaintext secrets, such as credentials, access tokens, and API keys, in customer-deployed Gemini Enterprise Agent Platform containers. For more information, see [Agent Platform Vulnerability Assessment](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#aevs).

## July 28, 2026

Feature

Version 1.2.0 of the Google SCC ITSM app and version 1.3.0 of the Google SCC SIR app have been released.

To reflect this update, the ServiceNow integration guide is updated with the following changes:

  * Added support for ServiceNow Yokohama, Zurich, and Australia versions.
  * Added the following features:

    * Mute and unmute findings
    * Create mute rules
    * Create Configuration Item (CI) lookup rules
    * View the action log
  * Updated setup instructions for Java KeyStore certificates.

  * Added additional troubleshooting steps for maximum execution time exceeded errors, data collection issues, and ECC Queue timeout errors.




For more information, see [Sending Security Command Center data to ServiceNow](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-servicenow).

## July 27, 2026

Feature

For the Security Command Center Premium tier, you can enable [AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) at the project level.

Project-level activations include access to the [AI security dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#ai-protection), [AI threat detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview), and [AI vulnerability and misconfiguration findings](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview#review-findings).

Some features of AI Protection are only available for organization-level activations. For more information, see [Configure AI Protection](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection).

Feature

For the Security Command Center Premium tier, you can enable [AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) at the project level.

Project-level activations include access to the [AI security dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#ai-protection), [AI threat detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview), and [AI vulnerability and misconfiguration findings](https://docs.cloud.google.com/security-command-center/docs/review-ai-security#review-findings).

For more information, see [Configure AI Protection](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection).

## July 17, 2026

Announcement

Key insights from Security Command Center are available on the [Security & compliance](https://docs.cloud.google.com/hub/docs/security) page in [Cloud Hub](https://docs.cloud.google.com/hub/docs/overview). This feature is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

## July 13, 2026

Feature

You can integrate Security Command Center with Jira to review findings in your Jira project. For more information, see [Integrate Jira with Security Command Center](https://docs.cloud.google.com/security-command-center/docs/integrate-jira).

## July 09, 2026

Feature

You can modify the [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) and [data encryption](https://docs.cloud.google.com/security-command-center/docs/cmek) configuration on the Premium and Standard tiers after you activate Security Command Center for your organization. For more information, see [Modify data residency or data encryption configuration](https://docs.cloud.google.com/security-command-center/docs/modify-data-residency-encryption).

## June 25, 2026

Change

The Assured Open Source Software premium tier includes an updated list of curated binaries for the Go, Java, and Python languages.

For more information, see [List of supported Java and Python packages for the Assured OSS premium tier](https://docs.cloud.google.com/security-command-center/docs/aoss-supported-packages-premium) and [List of supported Go packages for the Assured OSS premium tier](https://docs.cloud.google.com/security-command-center/docs/aoss-supported-packages-go-premium).

## June 18, 2026

Feature

Security Command Center External Exposure is available in [Preview](https://cloud.google.com/products#product-launch-stages) for the Security Command Center Premium tier. The service helps you manage and reduce your external attack surface through automated asset discovery, Google Cloud network exposure path validation, and active exploitability testing.

For more information, see [Detect exposed resources](https://docs.cloud.google.com/security-command-center/docs/detect-external-exposure).

## June 05, 2026

Feature

[AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) supports data residency in the European Union (EU) for the Security Command Center Premium tier.

For more information, see [Planning for data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support).

Change

The following Security Command Center finding category names from AI Protection have new names that clarify that AI Protection detects Gemini foundation models:

  * `VERTEX_AI_MODEL_DETECTED` changes to `GEMINI_MODEL_DETECTED`.
  * `VERTEX_AI_MODEL_NOT_PROTECTED_BY_MODEL_ARMOR` changes to `GEMINI_MODEL_NOT_PROTECTED_BY_MODEL_ARMOR`.



For more information about AI Protection findings, see [AI Protection overview](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview).

## May 28, 2026

Feature

[Risk Engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features) detects toxic combinations that are related to Managed Service for Apache Spark (formerly known as Dataproc), including Lightning Engine.

Feature

Risk reports are updated to include more content in the **Risk Engine introduction** and the **System attack exposure** pages. For more information about what's included in risk reports, see [Risk reports overview](https://docs.cloud.google.com/security-command-center/docs/risk-reports-overview).

## May 21, 2026

Change

The following [Compliance Manager frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks) were updated:

  * CIS Critical Security Controls v8 (version 8.0)
  * CIS GCP Foundations Benchmark v3.0 (version 7.0)
  * CSA Cloud Controls Matrix v4.0.11 (version 7.0)
  * ISO 27001:2022 (version 9.0)
  * NIST 800-53 Revision 5 (version 9.0)
  * NIST Cybersecurity Framework 1.1 (version 8.0)
  * PCI DSS v4.0.1 (version 6.0)
  * Qatar National Information Assurance Standard v2.1 (version 6.0)
  * SOC 2017 (version 7.0)



Deprecated

The Security Command Center Enterprise service tier is deprecated. It will be shut down on May 21, 2027. By default, your organization will automatically move to the Premium service tier on that date.

Feature

[Artifact guard](https://docs.cloud.google.com/security-command-center/docs/artifact-guard-overview) is available in [Preview](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Enterprise and Premium tiers. Artifact guard is a service that helps you prevent the deployment of vulnerable packages throughout the software development lifecycle.

Feature

[Risk Engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features) detects toxic combinations that are related to Cloud Build resources.

## May 19, 2026

Change

[Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud) supports scanning XFS and NTFS disk partition types.

## May 15, 2026

Change

[Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud) supports scanning GKE clusters that have [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) enabled.

## May 11, 2026

Change

Compliance Manager can be enabled for a single project. For more information, see [Enable Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-enable).

Change

New Standard tier activations at the organization level support the enhanced Standard tier features. New Standard tier activations at the project level continue to support Standard-legacy tier features. For more information, see [Standard tier enhanced and automatically activated for some customers](https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy).

## April 22, 2026

Feature

When Security Command Center is activated at the project level only, you can [enable Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud) on the single project.

Feature

Security Command Center has new predefined rules and controls:

  * Additional [predefined security graph rules](https://docs.cloud.google.com/security-command-center/docs/predefined-security-graph-rules) to support Agent Runtime

  * Additional support in [existing correlated threats rules](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview) for Agent Runtime

  * Additional [runtime detectors in Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-platform-threat-detection-overview#runtime-detectors)

  * Additional [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules) to support AI agents




Feature

Security Command Center findings that are related to AI security risks are available in the **Security** tab of the [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern). The feature helps provide comprehensive visibility into findings, active threats, and attack path simulations. This feature requires Security Command Center Premium or Enterprise.

For more information, see [View security findings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/view-security-findings).

## April 17, 2026

Feature

Through the [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview), Security Command Center helps you perform proactive security assessments ([Preview](https://cloud.google.com/products/#product-launch-stages)) throughout your application development lifecycle. This integration shows both design-time and runtime findings in Security Command Center. For more information, see [Application lifecycle security assessments](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#application-security-assessments).

Feature

[Data Security Posture Management](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security) has new controls in [Preview](https://cloud.google.com/products#product-launch-stages). The controls help you secure Cloud Storage objects and include the following:

  * Govern the minimum retention period for Cloud Storage objects
  * Require Customer-Managed Encryption for Cloud Storage objects
  * Restrict Public Access to Cloud Storage objects



For more information, see [Advanced data governance and security cloud controls](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#advanced-cloud-controls).

## April 16, 2026

Feature

[AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) supports agentic workloads in [Preview](https://cloud.google.com/products#product-launch-stages), including [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) and Model Context Protocol (MCP) servers. This update includes the following:

  * **Agent Platform Vulnerability Assessment** : Identifies software vulnerabilities (CVEs) in agentic workloads that are deployed with Gemini Enterprise Agent Platform. Findings are surfaced for vulnerabilities of HIGH or CRITICAL severity that are detected in your custom dependencies.
  * **Expanded detection and controls** : Includes new threat detection findings and recommended security controls for AI agents and MCP servers.
  * **Enhanced inventory and filtering** : Provides an updated [AI security dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#ai-protection) view and new filtering options for agentic resources in the [console](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console).



## April 15, 2026

Change

When you activate Security Command Center Standard or Premium tier for a project, several [services](https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-a-project#services) are automatically enabled and [service-specific service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-specific) are provisioned with the required IAM roles and permissions.

For more information, see [Activate for a project when Security Command Center is not active in the organization](https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-a-project#project-activation-scc-inactive-in-org).

## April 14, 2026

Feature

[Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview) monitors [Cloud Run worker pools](https://docs.cloud.google.com/run/docs/resource-model#workerpools). For a list of resources that Cloud Run Threat Detection monitors, see [Supported resources](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview#supported-resources).

## April 09, 2026

Announcement

Key insights from Security Command Center are available on the [Security & compliance](https://docs.cloud.google.com/hub/docs/security) page in [Cloud Hub](https://docs.cloud.google.com/hub/docs/overview). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 02, 2026

Feature

Security Command Center [Risk Engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features) supports Managed Service for Apache Spark resources in attack paths and Managed Service for Apache Spark clusters and jobs in high-value resource sets.

## March 31, 2026

Feature

[Risk Engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features) supports [`aiplatform.googleapis.com/ReasoningEngine`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.reasoningEngines) in both [attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn) and [high value resource sets](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#high-value-resource-sets).

## March 27, 2026

Announcement

Risk Engine has launched enhanced heuristics to help identify default high-value resources.

If you are using the default high-value resource set, you might observe changes in the exposure scores of their findings, resources, and issues. For information about these changes, see [Default high-value resource set](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#default-high-value-resource-set).

## March 25, 2026

Change

The following Compliance Manager frameworks were updated:

  * CIS GKE 1.7 (version 3.0)
  * CIS Critical Security Controls v8 (version 6.0)
  * CSA Cloud Controls Matrix v4.0.11 (version 5.0)
  * ISO 27001:2022 (version 7.0)
  * Qutar National Information Assurance Standard v2.1 (version 4.0)
  * NIST 800-53 Revision 5 (version 7.0)
  * NIST Cybersecurity Framework 1.1 (version 6.0)
  * PCI DSS v4.0.1 (version 4.0)
  * Security Essentials (version 12.0)
  * SOC 2017 (version 5.0)



## March 16, 2026

Change

The names of [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) rules pertaining to [AI control plane](https://docs.cloud.google.com/security-command-center/docs/ai-threats#control-plane) have changed.

The [Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview) rule `Privilege Escalation: Fileless Execution in /dev/shm` has been [shut down](https://docs.cloud.google.com/security-command-center/docs/deprecations#detector_shut_downs).

## March 09, 2026

Announcement

In March 2026, Risk Engine will launch enhanced heuristics to more accurately identify [default high-value resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#default-high-value-resource-set).

No action is required. As a result of this enhancement, customers using the default high-value resource set may observe changes in the exposure scores of their findings, resources, and issues. Customers using custom resource value configurations are not affected.

## March 05, 2026

Feature

[AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in the Security Command Center Premium tier at the organization level.

For regional availability, see [Locations for AI Protection](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints#locations-ai-protection).

## February 26, 2026

Feature

Security Command Center lets you filter findings, issues, and compliance information to view only the resources that are [registered to an App Hub application](https://docs.cloud.google.com/app-hub/docs/register-resources). For information, see [Integration with App Hub](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#apphub-integration).

## February 11, 2026

Feature

The [Security Command Center Standard tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers), available at no charge, has a new set of capabilities and is activated automatically for some organizations. For information about these changes, see [Standard tier enhanced and automatically activated for some customers](https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy).

## January 30, 2026

Change

The [prompt injection and jailbreak detection](https://docs.cloud.google.com/model-armor/overview#ma-prompt-injection) filter for the Mumbai (`asia-south1`) and Singapore (`asia-southeast1`) regions is upgraded to improve detection accuracy and reduce the rate of false positives.

## December 16, 2025

Feature

The following [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) detectors have been released to [General Availability](https://cloud.google.com/products#product-launch-stages):

  * `Command and Control: Piped Encoded Code Execution Detected`
  * `Command and Control: Piped Encoded Download`



## December 15, 2025

Feature

You can [configure Model Armor floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings) for Google-managed Model Context Protocol (MCP) servers to define baseline safety and security filters. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

You can also [configure Cloud Logging for sanitization operations](https://docs.cloud.google.com/model-armor/configure-logging#configure-logging-floor-settings). The Model Armor floor settings perform these operations on traffic to and from Google-managed MCP servers and Gemini Enterprise Agent Platform models.

## December 12, 2025

Change

Multiple pages in Security Command Center Standard have been improved:

  * The [Risk overview](https://docs.cloud.google.com/security-command-center/docs/assess-risk) page is enhanced to provide separate views for misconfiguration, vulnerabilities and identity-related findings.
  * The [Findings page](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#edit-finding-query) includes predefined filter views for vulnerabilities and identity findings.
  * The [left navigation](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#features) has been updated.



Feature

[AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) in the Security Command Center Enterprise tier and is available as a [Preview](https://cloud.google.com/products#product-launch-stages) in the Security Command Center Premium tier.

## December 11, 2025

Feature

Security Command Center [Risk Engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features) supports Cloud Build Attack Paths with Cloud Build Resources supported in the high-value resource set.

## December 10, 2025

Feature

You can configure Model Armor to enhance the security of your agentic AI applications that interact with Google Cloud Model Context Protocol (MCP) servers. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For configuration details, see [Model Armor integration with Google Cloud MCP servers](https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration).

## December 05, 2025

Change

Security Command Center [Risk Engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features) uses the [`storage.restrictAuthTypes`](https://docs.cloud.google.com/storage/docs/org-policy-constraints#restrict-auth-types) organization policy constraint to determine whether Cloud Storage buckets are reachable using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## December 04, 2025

Feature

[The monitoring dashboard](https://docs.cloud.google.com/model-armor/monitoring-dashboard) is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

## December 03, 2025

Feature

[Model Armor integration with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/model-armor/model-armor-vertex-integration) is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

## November 20, 2025

Change

The following updates simplify Security Command Center Standard and Premium tier activation for organizations:

  * You need fewer [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier#required-roles) to activate Security Command Center.
  * A variety of [services](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier#premium-services) are automatically enabled during activation. [Service-specific service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-specific) are automatically enabled with the IAM roles and permissions that are required for these services to function.



See the following for detailed information about activating a specific tier:

  * [Activate Security Command Center Standard tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier)
  * [Activate Security Command Center Premium tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier)



## November 17, 2025

Feature

The following [AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) features are available:

  * [AI Security dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#ai-protection): The dashboard has an updated AI Inventory section, which includes an overview of AI agents.
  * [Assets page](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console): You can filter for AI resources, including AI agents that are deployed to Agent Runtime.



AI Protection is available in [Preview](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Enterprise tier.

Feature

[Agent Engine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview), a built-in service of Security Command Center, is available in [Preview](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Enterprise and Premium tiers. This service helps you detect and investigate potential attacks on AI agents that are deployed to [Agent Runtime](https://docs.cloud.google.com/agent-builder/agent-engine/overview) Runtime.

## November 14, 2025

Feature

[Data Security Posture Management (DSPM)](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security) supports the Security Command Center Premium tier at the organization level.

## November 11, 2025

Change

Several features and updates have been made available to Security Command Center in a [federated identity](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services#security-command-center) environment:

  * Exporting findings to a CSV file.
  * Exporting findings to Cloud Storage.



The following features aren't supported by identity federation but are being moved to other sections in the documentation:

  * Sending feedback in Security Command Center
  * Managing Google SecOps settings.



## November 10, 2025

Feature

Model Armor is available in the following regions:

  * `europe-west1` (Belgium)
  * `europe-west2` (London)
  * `europe-west3` (Frankfurt)
  * `asia-south1` (Mumbai)



For more information, see [Locations for the Model Armor API](https://docs.cloud.google.com/model-armor/locations).

Feature

[Data Security Posture Management (DSPM)](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security) has been released to [General Availability](https://cloud.google.com/products#product-launch-stages) for the Security Command Center Enterprise tier.

## November 07, 2025

Feature

You can use customer-managed encryption keys (CMEK) organization policies with Security Command Center. For more information, see [Use CMEK organization policies with Security Command Center](https://docs.cloud.google.com/security-command-center/docs/cmek#org-policies).

Feature

The monitoring and auditing capabilities for [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager/overview) have been released to [General Availability](https://cloud.google.com/products#product-launch-stages).

## November 06, 2025

Feature

Security Command Center [Risk Engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features) supports Cloud Run attack paths for the following high-value resources:

  * `run.googleapis.com/Job`
  * `run.googleapis.com/Service`



## November 03, 2025

Feature

[Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview) supports the Security Command Center Premium tier at the organization level.

## October 30, 2025

Feature

In addition to the Enterprise service tier, [Issues](https://docs.cloud.google.com/security-command-center/docs/issues-overview) are available on the Security Command Center Premium service tier at the organization level. This update includes capabilities such as [Toxic Combinations, Chokepoints](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview), and [Graph Search](https://docs.cloud.google.com/security-command-center/docs/graph-search) ([Preview](https://cloud.google.com/products#product-launch-stages)). The console navigation has been updated to reflect an **Issues** page for Premium tier users.

## October 21, 2025

Change

The release note for Security Command Center and [attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn), published on October 16, 2025, was updated to clarify that [attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn) use Compute Engine and Google Kubernetes Engine OS and software vulnerability _findings_ to detect toxic combinations and chokepoints.

## October 20, 2025

Feature

[Container image vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#ar-vuln-assessment) has been released to [General Availability](https://cloud.google.com/products#product-launch-stages).

## October 17, 2025

Feature

Customers with an organization-level activation of Security Command Center Premium have an organization-level discovery subscription at no charge from Sensitive Data Protection. For more information, see [Sensitive data discovery in Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery#sensitive-data-discovery-scc-premium).

## October 16, 2025

Change

Security Command Center and [attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn) use Compute Engine and Google Kubernetes Engine operating system and software vulnerabilities to detect toxic combinations and chokepoints.

**UPDATE** : [Attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn) analyze OS and software vulnerability findings for Compute Engine and Google Kubernetes Engine resources to detect toxic combinations and chokepoints.

## October 15, 2025

Change

The following features in Compliance Manager are available in [General Availability](https://cloud.google.com/products#product-launch-stages):

  * [Applying and updating built-in frameworks and cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework)
  * Creating, applying, and editing custom frameworks and cloud controls
  * [Support for VPC Service Control perimeters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-configure-vpc-sc)
  * [Audit logging](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit-logging)
  * [Client libraries](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/libraries)
  * [REST APIs](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest)



## October 10, 2025

Feature

[Correlated Threats](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview) is available in [Preview](https://cloud.google.com/products#product-launch-stages). This feature combines related threat findings together by using the security graph, helping you to prioritize and respond to active threats.

## October 09, 2025

Feature

Data Security Posture Management (available in [Preview](https://cloud.google.com/products#product-launch-stages)) lets you deploy frameworks with advanced data security cloud controls to app-enabled folders. For more information, see [Deploy advanced data security cloud controls](https://docs.cloud.google.com/security-command-center/docs/dspm-use-data-security#deploy-advanced-data-security-cloud-controls).

## October 07, 2025

Change

Google Cloud console pages for all Security Command Center tiers have been enhanced.

  * The following changes were made to all service tiers—Standard, Premium, and Enterprise:

    * You can refresh findings in the **Finding query results** panel.
    * The **JSON** tab on the detail pane of the **Findings** page displays the raw findings JSON object, making it compatible with APIs.
    * Autocompletion of a query in the **Findings** page query editor is improved.
    * The **Findings > Quick filters** panel shows default values if there is an error fetching results.
    * The **Findings > Quick filters** panel shows separate **State** and **Mute** filter sections.
  * The following changes were made to the Enterprise service tier:

    * Added support for the **Vulnerabilities** page.
    * Added support for security marks.
    * Added support for the **Threats** dashboard on the **Risk overview** page.
    * The finding detail panel on the **Issues** page is updated. Open the panel using the **View details** button when viewing a toxic combination issue type.
    * Additional query operators and query functions are available.
    * The opt-out banner is no longer available.



## September 27, 2025

Feature

Model Armor limits the maximum input size for files and text to 4 MB, automatically skipping any content that exceeds this threshold.

## September 23, 2025

Change

The upgraded model for the prompt injection and jailbreak detection filter is available in EU multi-region. This model has improved detection rates across several attack vectors, including the following:

  * Do Anything Now prompts
  * System instruction manipulation
  * Unauthorized action execution
  * Sensitive information retrieval



Feature

[Bulk export findings to BigQuery](https://docs.cloud.google.com/security-command-center/docs/bulk-exports-to-big-query) is available in [General Availability](https://cloud.google.com/products#product-launch-stages). Bulk exports are supported for organizations, projects, and folders.

## September 22, 2025

Feature

[Graph search](https://docs.cloud.google.com/security-command-center/docs/graph-search) lets you explore the security graph using custom queries. This product is available in [Preview](https://cloud.google.com/products#product-launch-stages) in the Security Command Center Enterprise tier.

## September 16, 2025

Feature

Model Armor is integrated with Google Agentspace to provide greater insights and enhanced security of your agent interactions by default. For more information, see [Integration with Google Agentspace](https://docs.cloud.google.com/security-command-center/docs/model-armor-agentspace-integration).

## September 15, 2025

Change

The **Findings** page in Security Command Center has been improved.

  * With Security Command Center Premium and Enterprise, the page includes the following predefined filter views that return a specific category of findings.

    * Premium service tier: **All Findings** , **Vulnerabilities** , **Identity** , and **Threats**.
    * Enterprise service tier: **All Findings** , **Vulnerabilities** , **Identity** , **Data** , and **Code**.
  * With Security Command Center Enterprise, the page includes a selector to filter by cloud provider: Google Cloud, Amazon Web Service (AWS), and Microsoft Azure.




For more information, see [Review and manage findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#use_predefined_filter_views).

Feature

[Model Armor integration with Google Kubernetes Engine](https://docs.cloud.google.com/security-command-center/docs/model-armor-gke-integration) is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

## September 12, 2025

Change

Security Command Center has improved the automatic selection of resources when running attack path simulations using the default high-value resource set.

[Risk Engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features) uses heuristics to identify resources used for non-production purposes. To help ensure that you have information about the most important assets, Risk Engine calculates the attack exposure score for all other resources in the default high-value resource set before calculating the attack exposure score for these non-production resources.

To customize the high-value resource set, see [Define and manage your high-value resource set](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set). For information about Risk Engine, see [Attack exposure scores and attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn).

Change

Security Command Center changed how Google Cloud subnets are handled when running [attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn). The result is that attack paths are more accurate in relation to networking. Certain customers with specific Google Cloud subnet configurations, for example, when a VPC connector accesses a subnetwork, may see significant changes to toxic combinations, chokepoints, and attack exposure scores.

## September 11, 2025

Feature

Assured Open Source Software (Assured OSS) now supports Go packages. For more information, see [Download Go packages using direct repository access](https://docs.cloud.google.com/security-command-center/docs/aoss-download-go-packages).

## September 10, 2025

Feature

[Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview) is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

## September 08, 2025

Feature

The Model Armor monitoring dashboard provides a centralized view to track interactions and violations within your projects. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [View the monitoring dashboard](https://docs.cloud.google.com/security-command-center/docs/model-armor-monitoring-dashboard).

Change

Multiple pages in Security Command Center Premium have been improved:

  * The [Risk overview](https://docs.cloud.google.com/security-command-center/docs/assess-risk#threats) page is enhanced to provide a view of threats, vulnerabilities, and misconfigurations.
  * The [Findings page](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#edit-finding-query) includes predefined filter views for vulnerabilities and identity findings.
  * Information previously on the Threats page is available in the [Threats dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#threats) on the Risk overview page.
  * Information previously on the Vulnerabilities page is now available on the [Vulnerabilities dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#vulnerabilities) on the Risk overview page.



## September 02, 2025

Feature

Vulnerability assessment for Google Cloud supports scanning disks configured with customer-managed encryption keys (CMEK) for projects that are outside of VPC Service Controls perimeters. For more information about how to scan disks configured with CMEK, see [Run Vulnerability Scans for CMEK disks](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud#run-cmek-vulns).

## August 27, 2025

Change

Compliance Manager (available in [Preview](https://cloud.google.com/products#product-launch-stages)) now lets you [remove resources from deployed frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#remove-resource-assignments).

## August 20, 2025

Change

[Issues, chokepoints (for Google Cloud), and predefined security graph rules](https://docs.cloud.google.com/security-command-center/docs/issues-overview) have been released to [General Availability](https://cloud.google.com/products#product-launch-stages).

## August 15, 2025

Feature

[AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) helps you manage the security posture of your AI workloads by detecting threats and helping you to mitigate risks to your AI asset inventory. This product is available in [Preview](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Enterprise tier.

## August 14, 2025

Feature

You can use customer-managed encryption keys (CMEKs) to protect data at rest in Security Command Center. This feature is available in General Availability. For more information, see [Enable CMEK for Security Command Center](https://docs.cloud.google.com/security-command-center/docs/cmek).

## August 12, 2025

Feature

[Data Security Posture Management (DSPM)](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security) lets you define, deploy, monitor, and audit data security postures for your Google Cloud environment. This product is available in [Preview](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Enterprise tier.

## August 07, 2025

Feature

The following [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) detectors have been released to [General Availability](https://cloud.google.com/products#product-launch-stages):

  * `Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47177)`
  * `Execution: Socat Reverse Shell Detected`
  * `Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287)`
  * `Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)`
  * `Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)`



Feature

Risk reports generated and downloaded from Security Command Center include a system attack exposure page that shows the organization's exposure risk over time and lists the projects and resources that have the highest risk.

## August 04, 2025

Change

Model Armor supports the `asia-southeast1` location. For information about supported locations, see [Locations for the Model Armor API](https://docs.cloud.google.com/model-armor/locations).

## August 01, 2025

Feature

[Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview) helps ensure that your Google Cloud infrastructure, workloads, and data meet the security and regulatory requirements of your organization. This product is available in [Preview](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Enterprise tier.

## July 29, 2025

Feature

**Model Armor and Gemini Enterprise Agent Platform integration**

Model Armor integrates with Gemini Enterprise Agent Platform, providing a default security configuration for all new prediction endpoints. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Integration with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/security-command-center/docs/model-armor-vertex-integration).

Feature

You can send a bulk export of Security Command Center findings to a BigQuery dataset. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Bulk export findings to BigQuery](https://docs.cloud.google.com/security-command-center/docs/bulk-exports-to-big-query).

Feature

You can use Terraform to manage Model Armor floor settings and templates. This helps reduce manual overhead with Model Armor deployments. For more information, see [Terraform resources for Security Command Center](https://docs.cloud.google.com/security-command-center/docs/terraform#resources).

## July 28, 2025

Change

**Model Armor filter updates**

  * The prompt injection and jailbreak detection filter now supports 10,000 tokens.
  * For the Sensitive Data Protection filter, `SKIP_DETECTION` is returned if the prompt or response exceeds the token limit.
  * For all other filters, if the prompt or response exceeds the token limit, `MATCH_FOUND` is returned if malicious content is found, and `SKIP_DETECTION` is returned if no malicious content is found.



## July 25, 2025

Change

[Cloud Infrastructure Entitlement Management (CIEM)](https://docs.cloud.google.com/security-command-center/docs/ciem-overview) has launched support for log ingestion from Microsoft Azure management groups. This capability lets users set up log ingestion and then consume findings at an Azure management group level, rather than at the subscription level. For more information, see [Configure Microsoft Azure log ingestion for management groups](https://docs.cloud.google.com/security-command-center/docs/connect-secops-azure#mgmt-group). This capability is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Change

A new risk scoring algorithm is launched. As a result, you might see slight changes in [attack exposure scores for resources and findings](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn). The new algorithm better reflects attacker behavior and gives a fairer representation of the relative risk level of your organization. We will monitor the results of this change and might perform further adjustments, if necessary.

## July 24, 2025

Feature

For the Enterprise service tier, Security Command Center offers [data residency support](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) in the European Union, Saudi Arabia, and United States. This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## July 22, 2025

Change

The [Setup guide](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier#monitor-configure-enterprise-tab) in Security Command Center Enterprise, used to monitor the activation progress and configure services, is now in [General Availability](https://cloud.google.com/products#product-launch-stages).

Change

The `Impair Defenses: Two Step Verification Disabled` finding type of Event Threat Detection was renamed to `Persistence: Two Step Verification Disabled`. For a complete list of Event Threat Detection finding types, see [Event Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).

## July 21, 2025

Change

The **Aggregations** panel on the **Findings** page in Security Command Center Enterprise has been enhanced and is now called **Quick Filters**. For information about filtering results on the Findings page, see [Review and manage findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).

## July 17, 2025

Feature

The following [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) detectors for file monitoring are in [Preview](https://cloud.google.com/products#product-launch-stages):

  * `Collection: Pam.d Modification`
  * `Credential Access: Access Sensitive Files on Nodes`
  * `Defense Evasion: Disable or modify Linux audit system`
  * `Defense Evasion: Root Certificate Installed`
  * `Execution: Suspicious Cron Modification`
  * `Persistence: Modify ld.so.preload`



Change

The following Security Command Center Enterprise pages in the Google Cloud console now fully replace equivalent pages that you accessed previously in the Google Security Operations console.

  * [Risk Overview](https://docs.cloud.google.com/security-command-center/docs/assess-risk)
  * [Issues](https://docs.cloud.google.com/security-command-center/docs/issues-overview)
  * [Assets](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console) (previously called Resources)
  * [Findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings)



Left navigation links in the Google SecOps console open the related Google Cloud console page. See the earlier [release announcement](https://docs.cloud.google.com/security-command-center/docs/release-notes#May_08_2025) about these pages.

## July 14, 2025

Change

In the [Google Kubernetes Engine (GKE) security posture dashboard](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#gke-security-posture-dashboard), the software vulnerabilities pane is available in [Preview](https://cloud.google.com/products#product-launch-stages), not General Availability.

## July 11, 2025

Feature

[Notebook Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#notebook-security-scanner) is a built-in package vulnerability detection service of Security Command Center. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Premium or Enterprise tier.

You can enable and use Notebook Security Scanner to detect vulnerabilities in Python packages that are used in Colab Enterprise notebooks (files with the `ipynb` filename extension) and resolve those package vulnerability findings.

## July 10, 2025

Change

In the Google Cloud console, the [Google Kubernetes Engine (GKE) security posture dashboard](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#gke-security-posture-dashboard) shows the top software vulnerabilities that affect your GKE workloads. This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## July 01, 2025

Change

Security Command Center now supports the [detection of Chokepoints](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview) for the following cloud service provider platforms:

  * Amazon Web Services (AWS)
  * Microsoft Azure



Support for Chokepoints with Microsoft Azure and AWS is in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 30, 2025

Feature

You can download risk reports as PDFs. Risk reports help you understand the results of the attack path simulations (virtual red teaming) that Security Command Center runs. This feature is in [Preview](http://cloud.google.com/products#product-launch-stages) and is available for customers on the Enterprise or Premium service tiers. For more information, see [Risk reports overview](https://docs.cloud.google.com/security-command-center/docs/risk-reports-overview).

Feature

The following [Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview) detectors are in [General Availability](https://cloud.google.com/products#product-launch-stages).

  * `Defense Evasion: Unexpected ftrace handler`
  * `Defense Evasion: Unexpected interrupt handler`
  * `Defense Evasion: Unexpected kernel modules`
  * `Defense Evasion: Unexpected kernel read-only data modification`
  * `Defense Evasion: Unexpected kprobe handler`
  * `Defense Evasion: Unexpected processes in runqueue`
  * `Defense Evasion: Unexpected system call handler`



Deprecated

The `Defense Evasion: Unexpected kernel code modification` detector of Virtual Machine Threat Detection is shut down. For more information, see [Detector shutdowns](https://docs.cloud.google.com/security-command-center/docs/deprecations).

## June 27, 2025

Change

The following [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) detectors have been released to [GA](https://cloud.google.com/products#product-launch-stages).

  * `Exfiltration: Cloud SQL Data Exfiltration`
  * `Credential Access: CloudDB Failed login from Anonymizing Proxy IP`
  * `Initial Access: CloudDB Successful login from Anonymizing Proxy IP`



## June 20, 2025

Change

The display name for the following [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules) rules have changed. Please update any artifacts that use these values, such as finding filters, finding queries, or mute rules.

Previous display name | New display name  
---|---  
`Defensive Evasion: Static Pod Created` | `Defense Evasion: Static Pod Created`  
`Data Destruction: Deleted Google Cloud Backup and DR Backup` | `Impact: Deleted Google Cloud Backup and DR Backup`  
`Inhibit System Recovery: Deleted Google Cloud Backup and DR host` | `Impact: Deleted Google Cloud Backup and DR host`  
`Inhibit System Recovery: Deleted Google Cloud Backup and DR plan association` | `Impact: Deleted Google Cloud Backup and DR plan association`  
`Inhibit System Recovery: Deleted Google Cloud Backup and DR Vault` | `Impact: Deleted Google Cloud Backup and DR Vault`  
`Inhibit System Recovery: Google Cloud Backup and DR delete policy` | `Impact: Google Cloud Backup and DR delete policy`  
`Inhibit System Recovery: Google Cloud Backup and DR delete profile` | `Impact: Google Cloud Backup and DR delete profile`  
`Inhibit System Recovery: Google Cloud Backup and DR delete storage pool` | `Impact: Google Cloud Backup and DR delete storage pool`  
`Inhibit System Recovery: Google Cloud Backup and DR delete template` | `Impact: Google Cloud Backup and DR delete template`  
`Data Destruction: Google Cloud Backup and DR expire image` | `Impact: Google Cloud Backup and DR expire image`  
`Data Destruction: Google Cloud Backup and DR remove appliance` | `Impact: Google Cloud Backup and DR remove appliance`  
`Inhibit System Recovery: Google Cloud Backup and DR remove plan` | `Impact: Google Cloud Backup and DR remove plan`  
`Impair Defenses: Strong Authentication Disabled` | `Persistence: Strong Authentication Disabled`  
`Credential Access: External Member Added To Privileged Group` | `Privilege Escalation: External Member Added To Privileged Group`  
`Persistence: Impersonation Role Granted For Dormant Service Account` | `Privilege Escalation: Impersonation Role Granted For Dormant Service Account`  
`Credential Access: Privileged Group Opened To Public` | `Privilege Escalation: Privileged Group Opened To Public`  
`Credential Access: Sensitive Role Granted To Hybrid Group` | `Privilege Escalation: Sensitive Role Granted To Hybrid Group`  
  
Change

Risk Engine includes the `aiplatform.googleapis.com/Model` resource type in the default high-value resource set. For more information, see the [list of default resource types](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#default-high-value-resource-set).

## June 19, 2025

Change

**CVEs with no known exploitation activity are not considered in attack path simulations**

Vulnerability findings in Security Command Center are enriched by Mandiant Threat Intelligence. A CVE with wide exploitation activity is more likely to be used in an attack path compared to a CVE with only anticipated exploitation activity. Vulnerabilities with no known exploitation activity are not considered in attack path simulations. For more information, see [Incorporation of CVE data](https://cloud.google.com/security-command-center/docs/attack-exposure-learn#incorporation_of_cve_data).

Change

The prompt injection and jailbreak detection filter in Model Armor flags more threats across various attack vectors, and offers an improved detection rate for high-confidence malicious prompts. This filter is available in us-east1.

## June 18, 2025

Announcement

The **Set security marks** option in the [new Security Command Center Enterprise Findings and Assets pages](https://docs.cloud.google.com/security-command-center/docs/release-notes#May_08_2025) is temporarily unavailable. You can opt-out of the new Security Command Center Enterprise experience to manage security marks using the Cloud console. Or, you can manage security marks using the [Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-add-manage-security-marks).

## June 13, 2025

Feature

The following [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) detectors for Vertex AI have been released to [Preview](https://cloud.google.com/products#product-launch-stages):

  * `Persistence: New Geography for AI Service`
  * `Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Admin Activity`
  * `Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Data Access`
  * `Privilege Escalation: Anomalous Service Account Impersonator for AI Admin Activity`
  * `Privilege Escalation: Anomalous Service Account Impersonator for AI Data Access`
  * `Privilege Escalation: Anomalous Impersonation of Service Account for AI Admin Activity`
  * `Persistence: New AI API Method`
  * `Initial Access: Dormant Service Account Activity in AI Service`



## June 08, 2025

Feature

**Multi-language support for Model Armor filters**

The Responsible AI and prompt injection and jailbreak detection filters are tested in English, Spanish, French, Italian, Portuguese, German, Chinese (Mandarin), Japanese, and Korean. These filters can work in other languages, but the quality of results might vary.

For more information, see [Languages supported](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview#languages-supported).

Feature

Model Armor supports screening text in the following document types for malicious content.

  * DOCX, DOCM, DOTX, DOTM documents
  * PPTX, PPTM, POTX, POT presentations
  * XLSX, XLSM, XLTX, XLTM spreadsheets



## June 06, 2025

Change

The [Security Risk Overview dashboard for Compute Engine](https://docs.cloud.google.com/compute/docs/monitor-security-risks-console) is in [General Availability](https://cloud.google.com/products#product-launch-stages). In addition, it provides a **Top CVE findings** table that lists the most severe CVEs that affect your Compute Engine instances.

## June 05, 2025

Change

Muted findings are no longer considered in the Security Command Center Risk Engine. As a result, they no longer get [attack exposure scores](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn).

Feature

[Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud) supports scanning on Google Kubernetes Engine (GKE) nodes and containers. This feature has been released to [Preview](https://cloud.google.com/products#product-launch-stages).

## June 04, 2025

Feature

Security Command Center Premium customers can now access toxic combinations, which are in [General Availability](https://cloud.google.com/products#product-launch-stages), and chokepoints, which are in [Preview](https://cloud.google.com/products?e=48754805#product-launch-stages). These are available at the organization level. For more information, see [Toxic combinations and chokepoints overview](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview).

## June 03, 2025

Feature

The following [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) detectors for Google Kubernetes Engine have been released to [General Availability](https://cloud.google.com/products#product-launch-stages):

  * `Credential Access: Find Google Cloud Credentials`
  * `Credential Access: GPG Key Reconnaissance`
  * `Defense Evasion: Base64 ELF File Command Line`
  * `Defense Evasion: Base64 Encoded Python Script Executed`
  * `Defense Evasion: Base64 Encoded Shell Script Executed`
  * `Execution: Fileless Execution in /memfd:`
  * `Execution: Suspicious OpenSSL Shared Object Loaded`
  * `Privilege Escalation: Fileless Execution in /dev/shm`



## May 29, 2025

Change

Domain tagging for [toxic combinations and chokepoints](https://cloud.google.com/security-command-center/docs/toxic-combinations-overview) has been improved to be more precise. The following filters are available for [issues](https://cloud.google.com/security-command-center/docs/issues-overview): 

  * CVE Vulnerabilities
  * Identity
  * Data
  * AI Security



## May 28, 2025

Change

**Model Armor enhancements**

  * Model Armor supports multi-regional endpoints. For more information, see [Locations for the Model Armor API](https://docs.cloud.google.com/model-armor/locations).
  * All Model Armor filters support up to 2,000 tokens.



## May 27, 2025

Change

Enhanced [data residency support](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) in the European Union and United States is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## May 23, 2025

Change

Starting May 26, 2025, the findings retention period for new activations of Security Command Center will change from 13 months to 90 days.

The retention period for findings for existing customers prior to May 26, 2025, remains unchanged.

For more information on retention periods, see [Data retention](https://docs.cloud.google.com/security-command-center/docs/concepts-data-security-overview#data_retention).

## May 22, 2025

Change

The Google Kubernetes Engine (GKE) security posture dashboard shows the top threats, but not the top software vulnerabilities, detected by Security Command Center.

Feature

In the Google Cloud console, the [Google Kubernetes Engine (GKE) security posture dashboard](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#gke-security-posture-dashboard) shows the top threats and software vulnerabilities that affect your GKE workloads. This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## May 15, 2025

Change

The GA release of enhanced data residency support in the European Union and United States is temporarily delayed.

Feature

When you enable Security Command Center for the first time in an organization, and you enable data residency in the European Union or United States, data residency controls are enforced at rest, in use, and in transit. This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages).

For details, see [Planning for data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) and [Security Command Center regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints).

Feature

Risk Engine supports the Artifact Registry service. This support lets Risk Engine consider images that are hosted in Artifact Registry when calculating attack paths. For more information, see [Resources that receive attack exposure scores](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#resources_that_receive_attack_exposure_scores).

To support this change, Risk Engine includes the `artifactregistry.googleapis.com/Repository` resource type in the default high-value resource set. For more information, see the [list of default resource types](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#default-high-value-resource-set).

## May 09, 2025

Feature

A [Security Risk Overview dashboard for Compute Engine](https://docs.cloud.google.com/compute/docs/monitor-security-risks-console) is available in the Google Cloud console. The dashboard, available in [Preview](https://cloud.google.com/products#product-launch-stages), shows the top Security Command Center findings that affect your Compute Engine resources.

## May 08, 2025

Feature

Security Command Center Enterprise uses predefined security graph rules to identify [issues](https://cloud.google.com/security-command-center/docs/issues-overview). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Predefined security graph rules](https://cloud.google.com/security-command-center/docs/predefined-security-graph-rules).

Change

The following Security Command Center Enterprise pages that you previously accessed through the Google Security Operations console are now under Security Command Center in the Google Cloud console:

  * [Risk Overview](https://docs.cloud.google.com/security-command-center/docs/assess-risk)
  * [Issues](https://docs.cloud.google.com/security-command-center/docs/issues-overview)
  * [Assets](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console) (previously called _resources_)
  * [Findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings)



The Security Command Center Enterprise left navigation also includes links to pages in the Google Security Operations console. For information about this navigation and accessing Google Security Operations pages, see [Security Command Center Enterprise console](https://cloud.google.com/security-command-center/docs/scce-consoles-overview).

## May 05, 2025

Feature

Web Security Scanner, a built-in service of Security Command Center, released new detectors. The following detectors, which are available with the [Enterprise and Premium tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) of Security Command Center, detect misconfigurations in web applications:

  * `HSTS_MISCONFIGURATION`
  * `CSP_MISSING`
  * `CSP_MISCONFIGURATION`
  * `COOP_MISSING`
  * `CLICKJACKING_PROTECTION_MISSING`



For more information, see [Web Security Scanner misconfiguration findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#remediate-misconfiguration-findings).

## April 29, 2025

Feature

[Vulnerability Assessment for Google Cloud](https://cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud) has been released to [Preview](https://cloud.google.com/products#product-launch-stages). This feature helps to discover critical and high severity software vulnerabilities in your Compute Engine VM instances without installing agents.

Vulnerability Assessment for Google Cloud is on by default. Customers might see an increase in findings due to vulnerabilities in existing virtual machines that weren't previously detected.

## April 28, 2025

Feature

Security Command Center provides increased support for Microsoft Azure data.

  * Security Command Center can collect [Microsoft Azure resource and configuration data](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure).
  * Risk Engine can discover [toxic combinations](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview), [attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn), and [issues](https://docs.cloud.google.com/security-command-center/docs/issues-overview) in your Microsoft Azure environment.
  * The Sensitive Data Protection discovery service can [profile your Azure Blob Storage](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-azure-blob-storage) data and identify vulnerabilities and misconfigurations that can expose sensitive data.
  * [Cloud Infrastructure Entitlement Management (CIEM)](https://docs.cloud.google.com/security-command-center/docs/ciem-overview) can analyze and generate misconfiguration findings for Azure role-assignments that grant principals excessive privileges beyond what they use. This capability is available in [Preview](https://cloud.google.com/products#product-launch-stages).



Announcement

[Toxic Combinations](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview) for Amazon Web Services (AWS) has been released to [General Availability](https://cloud.google.com/products#product-launch-stages).

## April 21, 2025

Feature

The `Execution: Ingress Nightmare Vulnerability Execution` detector of [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 18, 2025

Feature

The ability of Event Threat Detection to analyze [foundational log sources](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#foundational_log_sources) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## April 17, 2025

Change

The discovery findings that Sensitive Data Protection generates in Security Command Center include recommended next steps. This improvement applies to the finding categories listed in [Publish data profiles to Security Command Center](https://cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc).

## April 09, 2025

Change

[IAM recommender](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#iamrec-source) findings are now available with project-level activations of Security Command Center.

Feature

**Model Armor and GKE integration**

Model Armor now enforces security policies uniformly on generative AI inference traffic using a traffic extension. This applies to all application load balancers, including Google Kubernetes Engine Inference Gateway. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Integration with Google Kubernetes Engine](https://docs.cloud.google.com/security-command-center/docs/model-armor-gke-integration).

## April 07, 2025

Feature

[Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 02, 2025

Change

When activating Security Command Center Enterprise, you can [monitor the provisioning status and progress of initial scans](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier#monitor-configure-enterprise-tab). This capability is in [Preview](https://cloud.google.com/products#product-launch-stages).

## March 21, 2025

Change

**Model Armor filter update**

The [prompt injection and jailbreak detection](https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-prompt-injection) filter in Model Armor is upgraded with increased efficacy and higher model quality scores.

## March 20, 2025

Feature

The **Risk** section of the SecOps console has been updated for Security Command Center Enterprise, introducing the following features in [Preview](https://cloud.google.com/products#product-launch-stages):

  * [**Issues**](https://docs.cloud.google.com/security-command-center/docs/issues-overview) are the most important security risks Security Command Center Enterprise has found in your cloud environments. Sourced from Security Command Center's virtual red teaming and security graph, issues give you all the details you need to understand, triage, and remediate a risk. Explore attack path diagrams, attack exposure scores, exposed resources, related findings, and whether multiple issues exist on a primary resource, all from the one place.
  * **Security graph** is a graph database that has cloud resources like assets, identities, apps, and data assigned to its nodes, while the edges of the graph determine the risk relationship between those resources following detection rules. When a relationship risk is discovered, the security graph generates an issue.
  * [**Chokepoints**](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview) are critical severity issues that focus on common resources or resource groups where multiple attack paths converge. Because of this focus on a common point, resolving a chokepoint can resolve other issues too, like toxic combinations.



The [**Risk Overview** dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk) has also been updated, and a new **Issues** page added to the **Risk** section. You can navigate through different security domains in the Risk section using the tabs near the top of the page, such as **All risk** , **Vulnerabilities** , and **Code**.

## March 18, 2025

Feature

[Cloud Infrastructure Entitlement Management (CIEM)](https://docs.cloud.google.com/security-command-center/docs/ciem-overview) has launched support for the following:

  * Log ingestion from Amazon SQS queues.
  * An alternate `CIEM only` feed to reduce costs.



For more information, see [Configure AWS log ingestion for CIEM](https://docs.cloud.google.com/security-command-center/docs/connect-secops-aws).

This feature is available in [General Availability](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Enterprise tier.

## March 14, 2025

Change

The [Execution: Malicious Python Executed detector](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview#detectors) in Container Threat Detection released to [General Availability](https://cloud.google.com/products#product-launch-stages).

Feature

The following [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) rules for Google Kubernetes Engine have been released to [General Availability](https://cloud.google.com/products#product-launch-stages):

  * `GKE_NODEPORT_SERVICE_CREATED`
  * `GKE_SENSITIVE_NAMESPACE_WORKLOAD_TRIGGERED`
  * `GKE_STATIC_POD_CREATED`
  * `GKE_TOR_PROXY_IP_REQUEST`
  * `GKE_WEBHOOK_CONFIG_CREATED`
  * `YL2_GKE_ANONYMOUS_USERS_GRANTED_ACCESS`
  * `YL2_GKE_APPROVE_CSR_FORBIDDEN`
  * `YL2_GKE_CRB_CLUSTERROLE_AGGREGATION_CONTROLLER`
  * `YL2_GKE_MANUALLY_DELETED_CSR`
  * `YL2_GKE_POD_MASQUERADING`
  * `YL2_GKE_REVERSE_SHELL_POD`
  * `YL2_GKE_SERVICE_ACCOUNT_CREATION_SENSITIVE_NAMESPACE`
  * `YL2_GKE_SUSPICIOUS_CRYPTOMINING_POD`



## March 13, 2025

Feature

Security Command Center has released the [Artifact Registry vulnerability assessment](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#ar-vuln-assessment) detection service, which includes the [`CONTAINER_IMAGE_VULNERABILITY`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ar-vulnerability-assessment-findings) detector. This detector generates vulnerability findings for container images that are stored and scanned in Artifact Registry. The detector generates findings for vulnerable container images deployed to the following assets:

  * Google Kubernetes Engine cluster
  * Cloud Run revision
  * Cloud Run job
  * App Engine



This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages) to all Security Command Center tiers.

## March 10, 2025

Feature

The following detectors have been added to Container Threat Detection.

  * Execution: Program Run with Disallowed HTTP Proxy Env
  * Exfiltration: Launch Remote File Copy Tools in Container



For more information, see [Container Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview#detectors).

## March 06, 2025

Change

The AWS connector has changed to enable additional use cases and requires the collection of AWS organization and organizational unit (OU) data. This change may require you to take additional action. For details about the change, see the [AWS connector changelog](https://docs.cloud.google.com/security-command-center/docs/connector-aws-changelog).

## March 03, 2025

Feature

You can use Virtual Machine Threat Detection to scan your Amazon Elastic Compute Cloud (EC2) VM disks for malware. To enable this feature, see [Enable VM Threat Detection for AWS](https://docs.cloud.google.com/security-command-center/docs/enable-vmtd-aws). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 28, 2025

Feature

[Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), a built-in service of Security Command Center, has released new detectors. The following detectors, which are available in Preview with the Enterprise and Premium tiers of Security Command Center, allow users to manage threats to their Google Cloud Backup and Disaster Recovery assets in Security Command Center:

  * `BACKUP_DELETE_VAULT`
  * `BACKUP_DELETE_VAULT_BACKUP`
  * `BACKUP_DELETE_BACKUP_PLAN_ASSOCIATION`



In addition, we updated the existing `BACKUP_REMOVE_PLAN` detector to support findings on Google Cloud Backup and Disaster Recovery assets that are managed in the Google Cloud console. This detector will dynamically generate finding descriptions based on the finding source.

## February 25, 2025

Feature

You can now use Organization Policy Service custom constraints to provide more granular control over specific fields for some Security Command Center resources. For more information, see [Configure custom organization policies](https://docs.cloud.google.com/security-command-center/docs/org-policy-custom-constraints). This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## February 17, 2025

Change

[Findings from Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc) include the `INFO_TYPES` and `RELATED_RESOURCES` fields when available. These fields appear in the `sourceProperties` field of the finding in Security Command Center. The affected finding categories are `DATA_RISK`, `DATA_SENSITIVITY`, `PUBLIC_SENSITIVE_DATA`, `SECRETS_IN_STORAGE`, and `SENSITIVE_DATA_CMEK_DISABLED`.

## February 14, 2025

Feature

The attack path simulations feature can now [automatically set the resource value of a Vertex AI dataset](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity) based on the sensitivity of the data that the dataset contains. For information about how to enable the automatic assignment of resource values based on data sensitivity, see [Create a resource value configuration](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set#create_a_resource_value_configuration).

## February 13, 2025

Feature

Security Command Center now supports [integration with Snyk](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-snyk-for-scc). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 12, 2025

Feature

[Cloud Infrastructure Entitlement Management (CIEM)](https://docs.cloud.google.com/security-command-center/docs/ciem-overview) has launched support for the following:

  * AWS Managed Microsoft AD and on-premises Active Directory identities. This feature alerts you to potential misconfigurations in your on-premises Active Directory or AWS-managed Active Directory identities.
  * Account-level findings in AWS. This lets you set up AWS audit logs for individual AWS accounts—instead of mandating logs across the entire AWS organization—and helps reduce your total cost of operations for CIEM in Security Command Center Enterprise.



## February 03, 2025

Feature

**Protect your AI applications using Model Armor**

Model Armor is a Google Cloud service that enables you to apply content safety and content security controls to LLM prompts and responses to mitigate risks such as sensitive data leakage, prompt injection, and offensive content. For more information, see [Model Armor overview](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview).

## January 24, 2025

Feature

Risk Engine, which generates attack exposure scores and attack paths for your high-value resources, now supports the `spanner.googleapis.com/Instance` resource type.

For more information, see [Resource types supported in high-value resource sets](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#supported-high-value-resource-types).

## January 17, 2025

Feature

Security Command Center now displays the number of resources scanned for a specific security compliance standard. This information appears as a column in the table on the Compliance detail page of the Google Cloud console for a given compliance standard.

To view the number of resources scanned against a security compliance standard, see [Assess compliance against a specific standard](https://docs.cloud.google.com/security-command-center/docs/compliance-management#assess_compliance_against_a_specific_standard).

## January 16, 2025

Feature

A new **Risk Overview** page is the default view for Security Command Center Enterprise customers. It serves as your first contact security dashboard for the highest priority risks in your cloud environments. From here you can quickly assess toxic combinations, threats, compliance issues, and high impact vulnerabilities.

Change

The **Postures** section in the SecOps console has been renamed to **Risk** , and moved to the top of the navigation for Security Command Center Enterprise customers. You can find the **Vulnerabilities** and **Data Security** dashboards here, along with the **Findings** and **Resources** pages.

## January 13, 2025

Announcement

A new error code, `AWS_ACTIVE_COLLECTOR_ACCOUNTS_NOT_FOUND`, is available in the [AWS connector in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws#aws_active_collector_accounts_not_found). Additional guidance is available to help troubleshoot the ['AWS_FAILED_TO_ASSUME_DELEGATED_ROLE'](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws#aws_failed_to_assume_delegated_role) error.

## December 18, 2024

Change

**Install new version of the Security Command Center Enterprise use case**

The installation and configuration of a new version of the `SCC Enterprise - Cloud Orchestration & Remediation` use case in the Security Operations console is required for the toxic combination functionality of Security Command Center Enterprise. The new use case, identified by date December 18, 2024, introduces updates to security posture findings playbooks and other enhancements to support the management of toxic combination findings and cases in the Security Operations console.

For installation instructions, see [Update Enterprise use case, December 2024](https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update).

Feature

Security Health Analytics now supports new resource types for creating custom modules. For a full list of supported resource types, see [Supported resource types](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview#supported-resource-types).

Feature

[Vulnerability Assessment for AWS](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-aws-overview) now supports scanning container images in Elastic Container Registry (ECR). It can detect operating system misconfigurations and issues with installed packages.

## December 17, 2024

Announcement

For Security Command Center Enterprise customers, the Sensitive Data Protection discovery service is now automatically enabled during the Enterprise activation process. For more information, see [Enable sensitive data discovery in the Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery).

## December 16, 2024

Feature

Security Command Center can now produce [Cloud Infrastructure Entitlement Management (CIEM)](https://docs.cloud.google.com/security-command-center/docs/ciem-overview) misconfiguration findings for federated identities that are connected to your AWS environment through the AWS IAM Identity Center.

Feature

**Detector for Container Threat Detection released to General Availability**

**Container Threat Detection** , a built-in service available in Security Command Center Premium and Enterprise, has launched three new detectors to [General Availability](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages):

  * **Execution: Container Escape** : Detects when a process inside a container tries to break out of its isolation and interact with the host system or other containers.
  * **Execution: Kubernetes Attack Tool Execution** : Detects when a Kubernetes attack tool is run inside a container, indicating a potential attempt to exploit vulnerabilities in the Kubernetes environment.
  * **Execution: Local Reconnaissance Tool Execution** : Detects when a local reconnaissance tool is executed within a container, suggesting that an attacker is gathering information about the container environment, such as network configurations, active processes, or mounted file systems.



For more information, see [Container Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview#detectors).

## December 10, 2024

Deprecated

**AI summaries of attack paths are disabled in Security Command Center**

Effective December 13, 2024, the preview of Gemini AI-generated summaries of Security Command Center attack paths is discontinued. The summaries are no longer available in the Google Cloud console.

For more information, see [Gemini features in Security Command Center](https://cloud.google.com/security-command-center/docs/concepts-security-command-center-overview#ai-features).

## December 09, 2024

Change

When activating the Security Command Center Enterprise tier, you now have the option to connect Security Command Center to an existing Google Security Operations instance or provision a new instance. For more information, see [Activate the Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).

## November 21, 2024

Feature

As of November 13, 2024, Security Command Center can produce [Cloud Entitlement Infrastructure Management (CIEM) findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings) for the following identity and access issues in AWS environments:

  * Users, groups, or assumed IAM roles that are inactive and have one or more permissions.
  * Overly permissive trust policies that are enforced on an AWS IAM role.
  * Identities that can move laterally through impersonation.



Announcement

The Sensitive Data Protection discovery service is now included in Security Command Center Enterprise. To enable discovery, see [Enable sensitive data discovery in the Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery).

The Sensitive Data Protection discovery service remains available to Security Command Center Premium and Standard customers as a [separately priced feature](https://cloud.google.com/sensitive-data-protection/pricing#data_profiling_pricing).

## November 15, 2024

Feature

Manage security postures using the Google Cloud console is generally available.

You can now create, deploy, update, and delete security postures using the Google Cloud console. For more information, see [Manage a security posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture).

## November 14, 2024

Change

The application steps to activate the Security Command Center Enterprise tier have been streamlined. For information, see [Activate the Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier#activate-the-security-command-center-enterprise-tier).

Feature

The `Defense Evasion: Rootkit` detector of Virtual Machine Threat Detection is in [General Availability](https://cloud.google.com/products#product-launch-stages). For more information, see [Virtual Machine Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview).

Feature

You can now view the configurations that determine the resource values of your [high-value resource set](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#high-value-resource-sets). For more information, see [View the configurations that match a high-value resource](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set#view-configs-matching-resource).

## November 11, 2024

Breaking

As of December 9, 2024, if you [activate Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview) within an organization for the first time, then you must use only version 2 of the [Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/rest) in that organization. Earlier versions are not supported.

If you activated Security Command Center at the project level prior to December 9, 2024, then any projects you activate in the same organization will support all available versions of the Security Command Center API.

To migrate to the v2 API from an earlier version, see [Migrate to v2 of the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/migrate-v2-api).

Change

The [Vulnerability management dashboard](https://docs.cloud.google.com/security-command-center/docs/scce-consoles-overview#secops-vulnerability-dashboard) was enhanced to include information about containers with exploitable vulnerabilities. This feature is in Preview.

Announcement

Starting October 24, 2024, the [IAM Recommender](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview) service is enabled by default when activating Security Command Center. You manage the IAM Recommender service under the Security Command Center **Settings** page > **Integrated services** tab. For more information, see [Add integrated Google Cloud services to Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#gcp-configure-other-services).

## November 08, 2024

Feature

To help you detect potentially malicious anomalies in your network, Event Threat Detection now supports the ability to analyze [foundational log sources](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#foundational_log_sources), which produce Bad IP findings without enabling VPC Flow Logs. This feature is in Preview.

  * If you activated Security Command Center Premium or Enterprise in a project or organization _before October 18, 2024_ , then you have access to this feature in that project or organization.
  * If you activated Security Command Center Premium or Enterprise at the project level _before October 18, 2024_ , and you activate additional projects in the same organization, then the additional projects will have access to this feature.
  * If you activated Security Command Center Premium or Enterprise in a project or organization _on or after October 18, 2024_ , and you want to enable this feature, then contact [Google Cloud Customer Care](https://docs.cloud.google.com/support).



## November 07, 2024

Announcement

The v2 [Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/rest) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

To migrate from an earlier version, see [Migrate to v2 of the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/migrate-v2-api).

## October 25, 2024

Deprecated

Event Threat Detection's Outgoing DoS finding has been shut down and is no longer available.

## October 18, 2024

Deprecated

The `VMTD disabled` finding category from Virtual Machine Threat Detection is no longer available. For more information about the finding categories that this built-in service provides, see [Virtual Machine Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview).

## October 16, 2024

Feature

[Toxic combination findings](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview) are generally available. This includes the following updates: 

  * Support for toxic combination findings on AWS resources. This feature is available in Preview.
  * Addition of a new **Toxic Combination Cases TTR and Trend** widget on the Posture overview page of the Google Security Operations console. The widget details the trends for open and closed toxic combination cases for a specific time range.



## October 11, 2024

Feature

**Working with findings and resources in the Security Operations console**

The ability to work with findings and resources using the Security Operations console is now in [General Availability](https://cloud.google.com/products#product-launch-stages). This feature is available only to Security Command Center Enterprise customers. 

The following capabilities were added since the Preview release of this feature:

  * You can [export findings to a CSV file](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#export-csv-secops-console).
  * Additional [query operators in the **Add filters** menu](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console#query-operators-add-filters-menu-secops-console) in the **Query editor** on the **Findings** page are now available.
  * The autocomplete menu suggests possible values when your write queries in the [**Query editor**](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console#edit-findings-query-secops-console). During Preview, the autocomplete menu suggested only filter names and functions.
  * You can [hide or display panels on the **Findings** page](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#collapse-panels-secops-console).
  * Your sort and [column settings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#adjust-columns-secops-console) are retained within the current session.



## October 09, 2024

Change

**Install new version of the Security Command Center Enterprise use case**

The installation and configuration of a new version of the `SCC Enterprise - Cloud Orchestration & Remediation` use case in the Security Operations console is required for the toxic combination functionality of Security Command Center Enterprise. The new use case, identified by date October 9, 2024, introduces a new widget, an updated ingestion logic, and other enhancements to support the management of toxic combination findings and cases in the Security Operations console.

For installation instructions, see [Update Enterprise use case, October 2024](https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update).

## October 08, 2024

Feature

**Vulnerability management dashboard released to Preview**

The new [Vulnerability management dashboard](https://cloud.google.com/security-command-center/docs/scce-consoles-overview#secops-vulnerability-dashboard) lets you investigate CVE vulnerabilities identified in your Google Cloud and AWS environments. 

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 04, 2024

Feature

**Manage security postures using the Google Cloud console**

You can now create, deploy, update, and delete security postures using the Google Cloud console. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Manage a security posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture).

## October 03, 2024

Feature

**GKE Security Posture vulnerability findings now support attack exposure scores**

`GKE runtime OS vulnerability` findings detected by GKE Security Posture in Google Cloud are now scored by attack path simulations. Use these attack exposure scores on vulnerabilities to help secure the resources that are the most valuable to your business and to address the most significant vulnerabilities in your GKE clusters. For more information, see [Attack exposure scores](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_exposure_scores).

## October 01, 2024

Feature

[Data residency for Security Command Center](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is now available in the Kingdom of Saudi Arabia.

## September 25, 2024

Breaking

**YARA rule names that appear in Virtual Machine Threat Detection findings will be renamed**

On or after October 28, 2024, YARA rule names that appear in `Malware: Malicious file on disk (YARA)` findings from Virtual Machine Threat Detection will be renamed. This update will resolve naming inconsistencies in the YARA rules. The new naming convention will contain the prefix, designation, type, name, and iteration of the YARA rule. The following are examples of the new names:

  * `Ext_FE_Hunting_Linux_CYCLOPSBLINK_FEBeta`
  * `M_APT_Controller_REDFLARE_1`
  * `M_Backdoor_REDSONJA_4`
  * `M_Cryptomine_XMRIG_1`



## September 18, 2024

Feature

**Assign high-value resources based on Sensitive Data Protection insights for Amazon S3 buckets**

The attack path simulations feature can now [automatically set the resource value of an Amazon S3 bucket](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity) based on the sensitivity of the data that the bucket contains. 

For information about how to enable the automatic assignment of resource values based on data sensitivity, see [Create a resource value configuration](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set#create_a_resource_value_configuration).

For information about how to configure Sensitive Data Protection to send data sensitivity classifications to Security Command Center, see [Publish data profiles to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc).

## September 11, 2024

Change

**Validate updates to integrations in the Security Command Center Enterprise use case**

Updates to the threat response playbook blocks and use case flows are available in the `SCC Enterprise - Cloud Orchestration & Remediation` use case for Security Command Center Enterprise. To get these changes, upgrade the integrations to the latest versions.

For more information, see [Validate integration versions in the use case](https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update#validate-integrations).

## September 09, 2024

Change

**New configuration options for Vulnerability Assessment for AWS**

When configuring Vulnerability Assessment for AWS, you can customize the scan settings by defining the scan interval, specific regions, specific tags, and specific instance IDs. You can also include SC1 or ST1 instances in the scan. For more information, see [Enable and use Vulnerability Assessment for AWS](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-aws-enable).

## September 04, 2024

Change

**Install new version of the Security Command Center Enterprise use case**

The installation and configuration of a new version of the `SCC Enterprise - Cloud Orchestration & Remediation` use case in the Security Operations console is required for the toxic combination functionality of Security Command Center Enterprise. The new use case, identified by date, September 4, 2024, introduces updated widgets, new playbooks, optimized data synchronization jobs, updated ingestion logic, and other enhancements to support the management of toxic combination findings and cases in the Security Operations console.

For installation instructions, see [Update Enterprise use case, September 2024](https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update).

## August 29, 2024

Feature

**Dynamic mute rules are generally available**

Security Command Center now supports dynamic mute rules, which allow you to mute _future and existing_ findings temporarily until a specified date or indefinitely until a finding no longer matches the configuration. We are adding these rules as an alternative to the original static mute rules that only mute _future_ findings indefinitely.

We recommend using dynamic mute rules exclusively in your mute rule configurations. For instructions on how to migrate your existing mute rules to dynamic mute rules, see [Migrate from static to dynamic mute rules](https://docs.cloud.google.com/security-command-center/docs/dynamic-mute-migrate).

For a comparison of static and dynamic mute rules, see [Types of mute rules](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings#mute-types).

## August 27, 2024

Change

Documentation is available for the [Security Posture REST API](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest).

## August 15, 2024

Change

**Install new version of the Security Command Center Enterprise use case**

The installation and configuration of a new version of the `SCC Enterprise - Cloud Orchestration & Remediation` use case in the Security Operations console is required for the toxic combination functionality of Security Command Center Enterprise. The new use case, identified by the date August 15, 2024, provides updates to the security operations features of the Enterprise tier of Security Command Center.

For installation instructions, see [Update Enterprise use case, August 2024](https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update).

## August 12, 2024

Feature

**EC2 Vulnerability Assessment findings now support attack exposure scores**

`Software vulnerability` findings detected by [EC2 Vulnerability Assessment for Amazon Web Services](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-aws-overview) are now scored with attack path simulations. Use these attack exposure scores on vulnerabilities to proactively secure the resources that are the most valuable to your business. For more information, see [Attack exposure scores](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_exposure_scores).

Feature

**Cloud Infrastructure Entitlement Management (CIEM) is generally available**

CIEM helps you adhere to the principle of least privilege by providing a comprehensive look at the security of your identity and access configuration. It provides insight into details such as what permissions are associated with a given identity, what roles are not optimal (highly permissive), and what steps you can take to remediate potential misconfigurations.

For more information about CIEM, see [Overview of Cloud Infrastructure Entitlement Management](https://docs.cloud.google.com/security-command-center/docs/ciem-overview).

## July 29, 2024

Change

**Preview of curated detections for Microsoft Azure data**

New curated detections in the Cloud Threats category that identify suspicious patterns in Microsoft Azure data are currently available in Preview.

For more information, see [curated detections for Microsoft Azure data](https://docs.cloud.google.com/security-command-center/docs/investigate-threat-findings#curated_detections_for_microsoft_azure_data) in the Security Command Center documentation.

Feature

**Assign high-value resources based on Sensitive Data Protection insights for Cloud Storage**

The attack path simulations feature can now [automatically set the resource value of a Cloud Storage resource](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity) based on the sensitivity of the data that the bucket contains. 

For information about how to enable the automatic assignment of resource values based on data sensitivity, see [Create a resource value configuration](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set#create_a_resource_value_configuration).

For information about how to configure Sensitive Data Protection to send data sensitivity classifications to Security Command Center, see [Publish data profiles to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc).

Change

**Detector for Container Threat Detection released to General Availability**

**Container Threat Detection** , a built-in service available in Security Command Center Premium and Enterprise, has launched a new detector, **Unexpected Child Shell** , in [General Availability](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages).

The detector monitors all process executions and generates a finding if a process that does not normally invoke shells spawns a shell process.

For more information, see [Container Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview#detectors).

## July 01, 2024

Feature

**Working with findings and resources in the Security Operations console**

Security Command Center Enterprise customers can now work with findings and affected resources using the Security Operations console. For example, you can do the following in the Security Operations console:

  * Filter for findings and resources based on different attributes.
  * Fine-tune your queries.
  * View the details of specific findings and resources.
  * View high-value resources and their attack exposure scores.
  * View the changes to a resource.



This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). 

For more information, see the following:

  * [Work with findings in the console](https://docs.cloud.google.com/security-command-center/docs/how-to-work-with-findings-in-the-console)
  * [Inspect resources related to findings](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console)



## June 25, 2024

Announcement

**Introducing the Security Command Center Risk Engine**

Security Command Center introduces _Risk Engine_ as the name of the functionality that provides attack path simulations, attack exposure scores, attack path visualizations, and toxic combination findings.

For more information, see [Assess risk with Risk Engine](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#risk-engine).

Feature

**Toxic combination findings release to Preview**

In the Enterprise tier of Security Command Center, the Risk Engine generates a finding when it detects a toxic combination during attack path simulations. A toxic combination is a group of security issues that, when they occur together in a particular pattern, create a path to one or more of your high-value resources.

The toxic combinations features introduces a new finding class, `Toxic combination`, and adds new fields in the `Finding` object to hold information about toxic combinations.

For more information, see [Overview of toxic combinations](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview).

**UPDATE** : The Preview release of the toxic combination feature is being rolled out to customers in stages. You might not receive toxic combination findings or see the new features in the Security Operations console for up to two weeks.

Change

The release note for the toxic combination feature published on June 25, 2024 was updated to explain the staged release of the feature.

Change

**Install new version of the Security Command Center Enterprise use case**

The installation and configuration of a new version of the `SCC Enterprise - Cloud Orchestration & Remediation` use case in the Security Operations console is required for the toxic combination functionality of Security Command Center Enterprise. The new use case, identified by date, June 25, 2024, introduces new widgets, new playbooks, and other enhancements to support the management of toxic combination findings and cases in the Security Operations console.

For installation instructions, see [Update Enterprise use case, June 2024](https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update).

## June 17, 2024

Breaking

**The Security Command Center Assets page will require new permissions**

On or after July 11, 2024, a new Identity and Access Management (IAM) permission will be required to view the **Assets** page in Google Cloud console. If you use custom roles to control access to Google Cloud resources, you will need to add this new permission to your [custom roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom) before that date to continue using the **Assets** page.

For more information, see [**Assets** page](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#assets_page).

## June 13, 2024

Feature

**Preview of Cloud Infrastructure Entitlement Management capabilities**

Cloud Infrastructure Entitlement Management (CIEM) for Amazon Web Services (AWS) and other identity providers on Google Cloud, such as Entra ID (Azure AD) and Okta, is now in preview.

CIEM helps you adhere to the principle of least privilege by providing a comprehensive look at the security of your identity and access configuration. CIEM provides insight into details such as what permissions are associated with a given identity, what roles are not optimal (highly permissive), and what steps you can take to remediate potential misconfigurations.

For more information, see [Overview of Cloud Infrastructure Entitlement Management](https://docs.cloud.google.com/security-command-center/docs/ciem-overview).

## June 03, 2024

Feature

**Vulnerability Assessment for AWS service released to General Availability**

The Vulnerability Assessment for AWS service, a built-in service of the Enterprise tier of Security Command Center, is released to [General Availability](https://cloud.google.com/products#product-launch-stages).

The Vulnerability Assessment for AWS service creates a disk snapshot to assess Amazon Web Service EC2 machines for software vulnerabilities.

For more information, see [Overview of Vulnerability Assessment for AWS](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-aws-overview).

## May 31, 2024

Feature

**VM Threat Detection's malware detector released to General Availability**

[Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview), a built-in service of Security Command Center, launched the `Malware: Malicious file on disk (YARA)` detector to [GA](https://cloud.google.com/products#product-launch-stages). This detector generates a finding if an executable file in a virtual machine matches known malware signatures.

## May 30, 2024

Feature

**Mute state of findings display in alerts, cases, and tickets**

The mute state of a finding is now reflected in its corresponding alert, case, and tickets in the Security Operations console of Security Command Center Enterprise. Previously, muted findings displayed only their **Active** status. For more information, see Finding status in [Cases overview](https://docs.cloud.google.com/security-command-center/docs/cases-overview#finding_status).

Feature

**Finding severities update in cases automatically**

In the Security Operations console of Security Command Center Enterprise, the severity of each finding is displayed in its corresponding case in the **Finding summary** widget. If the severity of a finding changes, the case is updated automatically. For more information, see [Finding severity versus case priority](https://cloud.google.com/security-command-center/docs/cases-overview#finding_severity_versus_case_priority).

## May 22, 2024

Feature

**New curated detections for existing AWS rule sets**

Enhanced the existing curated detections for AWS rule sets in the Cloud Threats category to add 40 new detections. These new rules, added to existing rule sets, expand the coverage and are designed to identify tactics and techniques commonly employed by malicious actors that use popular open source offensive security tools against AWS resources.

For more information, see [curated detections for AWS rule sets](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#aws-rule-sets) in the Google Security Operations documentation.

## May 14, 2024

Deprecated

**Rapid Vulnerability Detection preview shuts down on July 14, 2024**

The [Preview release](https://cloud.google.com/products#product-launch-stages) of the Rapid Vulnerability Detection service is discontinued and the service will be shut down on July 14, 2024.

No action is required.

On July 14, 2024, the status of any findings produced by the Rapid Vulnerability Detection service will be automatically set to `Inactive` and will be retained for a period defined by the [Security Command Center data retention policy](https://docs.cloud.google.com/security-command-center/docs/concepts-data-security-overview#data_retention).

## May 06, 2024

Feature

**Assign high-value resources based on Sensitive Data Protection insights for Cloud SQL**

The attack path simulations feature can now [automatically set the resource value of a Cloud SQL resource](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity) based on the sensitivity of the data that the instance contains. 

For information about how to enable the automatic assignment of resource values based on data sensitivity, see [Create a resource value configuration](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set#create_a_resource_value_configuration).

For information about how to configure Sensitive Data Protection to send data sensitivity classifications to Security Command Center, see [Publish data profiles to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc).

## May 01, 2024

Deprecated

**AI summaries of finding are disabled in Security Command Center**

Effective May 1, 2024, the preview of Gemini AI-generated summaries of Security Command Center findings is discontinued. The summaries are no longer available in the Google Cloud console.

For more information, see [Gemini features in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview#ai-features).

## April 15, 2024

Deprecated

**Security Health Analytics use of security marks for asset allowlists deprecated**

Starting April 15, 2025, Security Health Analytics will no longer use security marks to allowlist assets for Security Health Analytics detectors.

After that date, you can still apply security marks to assets, but they will no longer affect the way that Security Health Analytics processes assets.

For more information about security marks for assets, see [Add assets to allowlists](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#allowlist-assets).

Deprecated

**Historical snapshots to be disabled in Security Command Center API**

Starting July 15, 2024, Security Command Center will discontinue historical snapshot capabilities in the Security Command Center API, which were used to query for findings at a particular point in time. Specifically, `readTime` and `compareDuration` will be removed from `list` and `group` API calls for findings. Also, `start_time` will be removed from `SetFindingState`, `SetFindingWorkflowState` and `UpdateSecurityMarks`.

For more information about the Security Command Center API, see [Overview](https://docs.cloud.google.com/security-command-center/docs/reference/rest).

Change

**Data retention period to be reduced for Standard tier findings**

For existing Standard tier users, on July 14, 2024, the data retention period for findings will be reduced from 13 months to 35 days. For new users activating the Standard tier after April 15, 2024, the data retention period for findings is 35 days.

The retention period for findings in the Premium tier and Enterprise tier remains 13 months.

For more information, see [Data retention](https://docs.cloud.google.com/security-command-center/docs/concepts-data-security-overview#data_retention).

## April 02, 2024

Feature

**Enterprise tier released to General Availability**

The Enterprise tier, which transforms Security Command Center into a cloud-native application protection platform (CNAPP) that combines cloud security and enterprise security operations with multicloud support, is released to [General Availability](https://cloud.google.com/products#product-launch-stages).

The following features and capabilities of the Enterprise tier are new to Security Command Center:

  * [Multicloud support](https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview#multicloud_support_secure_your_deployments_on_other_cloud_platforms): You can now connect Security Command Center to Amazon Web Services for the following capabilities: 
    * Detect threats and vulnerabilities
    * Assess the risk exposure of your high-value AWS resources
    * Assess compliance with [security standards](https://docs.cloud.google.com/security-command-center/docs/compliance-management#security-standards-supported-on-aws)
  * [A new Security Operations console](https://docs.cloud.google.com/security-command-center/docs/scce-consoles-overview#secops-console) for global security operations tasks
  * [SIEM and SOAR capabilities for security operations](https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview#enterprise_tier_functions_and_services_summary)
    * Security investigation and event management (SIEM) capabilities: 
      * Ingest and normalize logs from Google Cloud, AWS, Security Command Center findings, and resource metadata from multiple sources
      * Detect the most important cloud threats with curated threat detection
      * Search across consolidated SIEM data
    * Security operations and response (SOAR) capabilities: 
      * Manage detections, investigations, and responses with cases
      * Automate response workflows with playbooks
      * Focus on posture and threat findings with dedicated views in the Security Operations console
      * Integrate with IT service management products, such as Jira and ServiceNow, for posture management
      * Search across consolidated SOAR data
  * The following attack exposure scoring features are in General Availability: 
    * [Attack exposure scores now calculated for high-value resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#resources_that_receive_attack_exposure_scores)
    * [Severities of vulnerability findings can vary to align with attack exposure scores](https://docs.cloud.google.com/security-command-center/docs/finding-severity-classifications#variable-severities-by-risk-score)
    * Optional [automated assignment of resource values with Sensitive Data Protection](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity)
  * [Vulnerability and misconfiguration detections](https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview#manage-vulnerabilities)
    * Security Health Analytics includes the following enhancements: 
      * New misconfiguration detectors for AWS resources
      * Detectors are mapped to new security standards
    * You can now manage the remediation of critical and high severity vulnerability and misconfiguration findings using cases that are automatically opened for you.
  * [Threat detection and investigation](https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview#manage-threats)
    * Detect threats in your AWS deployments
    * Investigate and respond to incidents with SIEM-like capabilities across 90 days of cloud logs
    * Manage the investigation of and response to threats by using cases
    * Define response workflows and automated actions in response to threats by using playbooks
  * [Mandiant Attack Surface Management integration](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#mandiant-asm)
    * Mandiant Attack Surface Management scans your external attack surfaces to identify vulnerability and misconfiguration findings
  * [Sensitive Data Protection integration](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#dlp)
    * The **Risk overview** page of Security Command Center in the Google Cloud console now shows data security findings from the Sensitive Data Protection discovery service
    * Findings from Sensitive Data Protection that indicate the sensitivity and data risk levels of your data can inform the automated assignment of resource values for the attack path simulation feature
  * [Gemini artificial intelligence features](https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview#ai-features)
    * Natural language search for threat findings 
    * AI investigation widget for cases
  * [Compliance, security standards](https://docs.cloud.google.com/security-command-center/docs/compliance-management)
    * Support for AWS security standards
  * [Validate infrastructure as code (IaC)](https://docs.cloud.google.com/security-command-center/docs/validate-iac) against organization policies and Security Health Analytics detectors. The IaC validation feature lets you determine whether your new or modified resource definitions violate the existing policies that are applied to your Google Cloud resources.
  * [Integration with Assured Open Source Software](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc) The paid tier of Assured OSS is included with your Enterprise tier license, so that you can enhance your code security by using the open source software packages that Google uses for its own developer workflows.



Breaking

**With the Enterprise tier, severity levels of certain findings are now variable**

In the Enterprise tier of Security Command Center, the default severity level of an active vulnerability or misconfiguration finding can change if the finding's attack exposure score changes. If you are a user of the Premium tier and you upgrade to the Enterprise tier, check any automated or manual procedures that rely on the value of the `severity` property to ensure that they can support a variable severity value.

For more information, see [Severities that vary based on attack exposure score](https://docs.cloud.google.com/security-command-center/docs/finding-severity-classifications#variable-severities-by-risk-score).

## April 01, 2024

Fixed

**The following Security Health Analytics misconfiguration detectors have changed to check for overly restrictive flag values that might prevent error messages from being written to the logs:**

  * `SQL_LOG_ERROR_VERBOSITY`
  * `SQL_LOG_MIN_ERROR_STATEMENT_SEVERITY`



For the flag values that the detectors check for, see:

  * [SQL log error verbosity](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#sql_log_error_verbosity)
  * [SQL log min error statement severity](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#sql_log_min_error_statement_severity)



## March 26, 2024

Feature

**GKE security posture recommendations released to Preview**

Recommendations from [GKE security posture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#scc-integration) are now available as findings in all tiers of Security Command Center as a [Preview](https://cloud.google.com/products#product-launch-stages) release.

GKE security posture publishes [workload configuration auditing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning) results as `Misconfiguration` class findings and [vulnerability assessment](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-workload-vulnerability-scanning#about-container-os-scanning) results as `Vulnerability` class findings in Security Command Center.

For more information, see [GKE security posture dashboard](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#gke-security-posture-dashboard).

## March 21, 2024

Feature

**Security Command Center detectors are now mapped to the following additional compliance frameworks:**

  * CIS Critical Security Controls v8
  * Cloud Controls Matrix v 4
  * HIPAA
  * ISO 27001 (2022)
  * NIST 800-53 (rev 5)
  * NIST Cybersecurity Framework (v 1.0)
  * PCI-DSS 4.0
  * SOC 2 (2017)



## March 20, 2024

Feature

**New misconfiguration detectors for AlloyDB for PostgreSQL clusters released to General Availability.**

Security Health Analytics, a built-in service of Security Command Center, released new detectors to [General Availability](https://cloud.google.com/products#product-launch-stages). The following detectors, which are available only with the [Premium tier](https://docs.cloud.google.com/security-command-center/pricing#premium-tier) of Security Command Center, detect misconfigurations in AlloyDB for PostgreSQL clusters and instances:

  * ALLOYDB_AUTO_BACKUP_DISABLED: Automated backups are not enabled in AlloyDB for PostgreSQL cluster.
  * ALLOYDB_LOG_ERROR_VERBOSITY: Instance database flag `log_error_verbosity` for AlloyDB for PostgreSQL instance is not set to `default` or another less restrictive value.
  * ALLOYDB_LOG_MIN_ERROR_STATEMENT_SEVERITY: Instance database flag `log_min_error_statement` for AlloyDB for PostgreSQL instance is not set to ERROR or lower.
  * ALLOYDB_LOG_MIN_MESSAGES: Instance database flag `log_min_messages` for AlloyDB for PostgreSQL instance is not set to at minimum `warning`.



For more information, see [SQL vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#sql-findings).

## February 29, 2024

Feature

**Security Command Center API v2 released to Preview**

The Security Command Center API v2, which enables data residency control and includes the `/locations/LOCATION` field in resource names, is released to [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see the REST reference [Security Command Center API Overview](https://docs.cloud.google.com/security-command-center/docs/reference/rest).

Feature

**Data residency for Security Command Center release to Preview**

Security Command Center data residency control is released to [Preview](https://cloud.google.com/products#product-launch-stages). Security Command Center supports the following data locations:

  * European Union (`eu`)
  * United States (`us`)
  * Global (`global`)



For more information, see [Data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support).

## February 28, 2024

Feature

**Virtual Machine Threat Detection** , a built-in service of Security Command Center Premium, has launched a new detector, `Defense Evasion: Rootkit`, in [Preview](https://cloud.google.com/products#product-launch-stages).

The detector monitors virtual machines and generates a finding if a combination of signals matching a known kernel-mode rootkit is present.

For more information, see [Virtual Machine Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview).

## February 20, 2024

Deprecated

**Manual control of finding state deprecated for vulnerabilities and misconfigurations**

Starting October 21, 2024, you will no longer be able to manually update the state of vulnerability or misconfiguration findings that are issued by Security Health Analytics or VM Manager. Security Command Center will return an error message on manual attempts to change the values of the state. Security Command Center will also begin preventing the manual creation of findings under the exact same name as a source that is automatically managed by Security Command Center in order to prevent the creation of findings that can never be resolved.

For more information, see [Finding states](https://docs.cloud.google.com/security-command-center/docs/finding-states).

Feature

**Pane on Overview page that supports postures for Vertex AI released to Preview**

A pane on the **Overview** page lets you monitor for vulnerabilities that were found by the Security Health Analytics custom modules that apply to Vertex AI, and lets you view any drift from the Vertex AI organization policies that are defined in a posture.

For more information, see [Monitor posture drift](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#monitor-posture).

## February 14, 2024

Feature

**Support for VPC Service Controls released to[General Availability](https://cloud.google.com/products#product-launch-stages)**

You can now protect Security Command Center using VPC Service Controls perimeters. For more information, see [VPC Service Controls supported products](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_security_command_center).

## February 11, 2024

Breaking

**Exports of compliance reports will require new permissions**

On or after March 15, 2024, a new Identity and Access Management (IAM) permission will be required to export a compliance report from the Google Cloud console. If you use [custom roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom) to control access to Google Cloud resources, you will need to add this new permission to your custom roles before that date to continue exporting compliance reports.

For more information, see [Export a compliance report](https://docs.cloud.google.com/security-command-center/docs/compliance-management#compliance_report_export).

## February 06, 2024

Feature

**High-value resources now include attack exposure scores**

The calculation of attack exposure scores for high-value resources by the Security Command Center Attack Path Simulations feature is released to [Preview](https://cloud.google.com/products#product-launch-stages). Use attack exposure scores on resources to proactively secure the resources that are the most valuable to your business. For more information, see [Attack exposure scores](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_exposure_scores).

Feature

**Mandiant analyst CVE ratings added to vulnerability findings**

The addition of CVE information, including ratings of the vulnerability by Mandiant Threat Intelligence analysts, to the details of Security Command Center vulnerability findings is released to [Preview](https://cloud.google.com/products#product-launch-stages). You can now prioritize vulnerabilities based on the exploitability and impact ratings from Mandiant. For more information, see [Prioritize vulnerability findings to reduce risk](https://docs.cloud.google.com/security-command-center/docs/vulnerabilities-prioritize-remediation#prioritize_vulnerability_findings_to_reduce_risk).

Feature

**New security posture service released to General Availability**

The new security posture service is released to [General Availability](https://cloud.google.com/products#product-launch-stages). This service lets you create and deploy postures so that you can define the policies for your Google Cloud organization and monitor for drift. 

For more information, see [Security posture overview](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview).

Feature

**Attack exposure scores informed by Mandiant Threat Intelligence**

The inclusion of CVE exploitability ratings in the calculation of attack exposure scores for vulnerability findings is released to [Preview](https://cloud.google.com/products#product-launch-stages). The ratings, which are provided by Mandiant Threat Intelligence analysts, enables Security Command Center attack path simulations to provide more accurate scores for prioritizing vulnerability findings. For more information, see [Incorporation of CVE data](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#incorporation_of_cve_data).

Feature

**Prioritize high-value resources automatically by data sensitivity**

The optional integration of the Sensitive Data Protection discovery feature with the Security Command Center attack path simulation feature is released to [Preview](https://cloud.google.com/products#product-launch-stages). If you use Sensitive Data Protection discovery, you can choose to have the priority value of supported high-value resources set automatically based on whether they contain medium-sensitivity or high-sensitivity data. For more information, see [Set resource priority values automatically by data sensitivity](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity).

Feature

**Improvements to compliance standards support now available**

Improvements to the Security Command Center **Compliance** page in the Google Cloud console are released to [General Availability](https://cloud.google.com/products#product-launch-stages). Your state of compliance with all supported standards is now presented more clearly and a new **Compliance details** page makes it easier to see failing controls. For more information, see [Assess and report compliance](https://docs.cloud.google.com/security-command-center/docs/compliance-management).

## January 31, 2024

Feature

[Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview), a built-in service of Security Command Center, launched the `Malware: Malicious file on disk (YARA)` detector to [Preview](https://cloud.google.com/products#product-launch-stages). This detector generates a finding if an executable file in a virtual machine matches known malware signatures.

## January 26, 2024

Feature

**Security Command Center Management API released to General Availability**

The Security Command Center Management API, which provides API support for managing settings and custom modules, is released to [General Availability](https://cloud.google.com/products#product-launch-stages).

For more information, see [Security Center Management API](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest).

## January 24, 2024

Issue

**New Container Threat Detection service account deferred**

The new service account for Container Threat Detection that was included with new activations of Security Command Center after December 7, 2023 was temporarily removed from new activations on Dec 19, 2023 due to issues with older GKE clusters.

If you activated Security Command Center during this time period, all issues have been resolved and there is no impact to your experience.

New activations of Security Command Center will use the service account that was used prior to December 7, 2023 with the Container Threat Detection service until further notice.

For more information about the new service account, see [Required IAM permissions](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#required_permissions).

## January 10, 2024

Fixed

**Issue that caused finding severities to change unexpectedly is resolved**

Between December 11, 2023 and January 10, 2024, an issue might have changed the severities of some findings unexpectedly. As of today, the issue has been fixed for all customers. Any finding severities that were changed have been returned to their original state.

## December 15, 2023

Feature

The custom modules feature for Event Threat Detection is now in [General Availability](https://cloud.google.com/products#product-launch-stages). This feature lets you create custom Event Threat Detection detectors that meet the unique needs of your organization.

In addition, the `Unexpected Cloud API Call` module type is now available. This module type lets you create a custom module that detects when a specified principal calls a specified method against a specified resource.

For more information, see [Overview of custom modules for Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview).

## December 13, 2023

Breaking

**Custom roles will require new permissions for custom modules**

On or after January 22, 2024, new Identity and Access Management (IAM) permissions will be required to work with custom modules for both Event Threat Detection and Security Health Analytics. If you use custom roles to control access to Google Cloud resources, you will need to add these new permissions to your custom roles before that date to continue working with custom modules.

For more information, see the following:

  * [IAM roles for Event Threat Detection custom modules](https://docs.cloud.google.com/security-command-center/docs/use-custom-modules-etd#iam_roles)
  * [IAM roles for Security Health Analytics custom modules](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview#iam_roles)



## December 11, 2023

Change

**New Container Threat Detection service account with new activations**

For activations of Security Command Center after December 7, 2023, Container Threat Detection uses a new service account for Identity and Access Management (IAM) permissions.

During the activation process, new users grant permissions to two service accounts: one for Security Command Center and one for Container Threat Detection. The new service account speeds the first-time enablement of Container Threat Detection.

If you activated Security Command Center prior to December 7, 2023, Container Threat Detection remains unchanged and continues to use its original service account.

For more information, see [Service agent roles](https://docs.cloud.google.com/security-command-center/docs/access-control-org#service-agent).

## December 07, 2023

Feature

**New goal-based query presets for identity and access misconfigurations**

New goal-based query presets on the Security Command Center **Vulnerabilities** page are released to [Preview](https://cloud.google.com/products#product-launch-stages).

The query presets support cloud infrastructure entitlement management (CIEM) by filtering vulnerability finding categories to those that are related to principal accounts that are misconfigured or that have excessive permissions to Google Cloud resources.

For more information, see [Goal-based query presets](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#vulnerability-query-presets).

## December 04, 2023

Feature

**Policy Controller integration released to General Availability**

The integration of Policy Controller for Kubernetes clusters with Security Command Center is released to [General Availability](https://cloud.google.com/products#product-launch-stages). Violation alerts from Policy Controller appear in Security Command Center as misconfiguration findings.

For more information, see [Policy Controller](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#policy_controller).

## November 10, 2023

Feature

**Policy Controller integration now in Preview**

The integration of Policy Controller for Kubernetes clusters with Security Command Center is released to [Preview](https://cloud.google.com/products#product-launch-stages). Violation alerts from Policy Controller now appear in Security Command Center as misconfiguration findings.

For more information, see [Policy Controller](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#policy_controller).

## November 08, 2023

Feature

**Support for VPC Service Controls released to[Preview](https://cloud.google.com/products#product-launch-stages)**

You can now protect Security Command Center using VPC Service Controls perimeters. For more information, see [VPC Service Controls supported products](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_security_command_center).

## October 19, 2023

Feature

**Backup and DR Service threat detectors available in Security Command Center Premium**

Event Threat Detection, a built-in service of Security Command Center, released new rules for the Google Cloud Backup and DR service to [Preview](https://cloud.google.com/products#product-launch-stages). Security Command Center can now detect the following:

  * Backup and DR actions that inhibit system recovery
  * Backup and DR actions that result in data destruction



For more information, see:

  * Backup and DR in [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules)
  * [What is Backup and DR Service?](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



## October 18, 2023

Feature

**Container Threat Detection** , a built-in service of Security Command Center Premium, has launched a new detector, **Unexpected Child Shell** , in [Preview](https://cloud.google.com/products#product-launch-stages).

The detector monitors all process executions and generates a finding if a process that does not normally invoke shells spawns a shell process.

For more information, see [Container Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview#detectors).

## October 09, 2023

Feature

**Cloud IDS threat detections available in Security Command Center**

Threats that are detected by Cloud IDS, a Google Cloud intrusion detection service, are now included in the findings that are issued by the Event Threat Detection service of Security Command Center. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see:

  * Cloud IDS in [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules)
  * [Cloud IDS overview](https://docs.cloud.google.com/intrusion-detection-system/docs/overview)



## September 29, 2023

Feature

**`containsOnly()` function released to [General Availability](https://cloud.google.com/products#product-launch-stages).**

You can now use the `containsOnly()` function to query findings with an array-type attribute or subfield that only contains values that match the specified filter, and no other values.

For more information, see [The `containsOnly` function](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console#containsonly-query-function).

## September 20, 2023

Feature

**Attack path simulations support additional resources**

The attack path simulation feature that generates attack exposure scores and attack paths for your high-value resources now supports the following additional Google Cloud resources:

  * `aiplatform.googleapis.com/Dataset`
  * `aiplatform.googleapis.com/Featurestore`
  * `aiplatform.googleapis.com/MetadataStore`
  * `aiplatform.googleapis.com/Model`
  * `aiplatform.googleapis.com/TrainingPipeline`
  * `container.googleapis.com/Cluster`



For more information, see [Resource types supported in high-value resource sets](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#supported-high-value-resource-types).

## September 19, 2023

Change

**Vulnerabilities per resource type graphic released to[General Availability](https://cloud.google.com/products#product-launch-stages)**

The Security Command Center **Overview** page in the Cloud console now shows a **Vulnerabilities per resource type** graphic, which replaces the **Active vulnerabilities over time by severity** graphic. The **Vulnerabilities per resource type** graphic shows the resources in your organization (for example, Cloud Storage buckets, Compute Engine instances, and firewalls), how many active vulnerabilities exist for each resource, and the severity of those vulnerabilities.

## September 15, 2023

Feature

**Event Threat Detection** , a built-in service of Security Command Center, released a new rule, `Initial Access: Leaked Service Account Key Used`, to [General Availability](https://cloud.google.com/products#product-launch-stages).

For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## September 11, 2023

Feature

Security Command Center now supports CIS Google Cloud Computing Foundations Benchmark v2.0.0.

The support for v2.0.0 includes the following new vulnerability detector:

  * `Load balancer logging disabled`



For more information, see the following:

  * [Detectors and compliance](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#detectors_and_compliance)
  * [CIS Google Cloud Foundation 2.0.0](https://www.cisecurity.org/benchmark/google_cloud_computing_platform)



## August 21, 2023

Feature

**`inIpRange()` function released to [General Availability](https://cloud.google.com/products#product-launch-stages)**

You can now specify a range of IP addresses by using the `inIpRange()` function in query statements to filter findings that contain IPv4 or IPv6 addresses within the specified range.

For more information, see [The inIpRange function](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console#iniprange-function).

## August 16, 2023

Change

**New assets experience released to[General Availability](https://cloud.google.com/products#product-launch-stages)**

The Security Command Center **Assets** page in the Cloud console is now powered by [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview). The new **Assets** page provides expanded asset visibility and includes a new asset query feature.

This release is part of the [planned deprecation of the Security Command Center Assets API](https://docs.cloud.google.com/security-command-center/docs/release-notes#June_28_2023) scheduled for on or after June 20, 2024.

For more information, see [Assets page](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#assets_page).

## August 03, 2023

Feature

AI-generated summaries of the simulated attack paths for Security Command Center findings are released to [Preview](https://cloud.google.com/products#product-launch-stages). When you view the attack path for a finding, you can now read explanations that are generated dynamically by artificial intelligence (AI).

For more information, see [AI-generated summaries](https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview#ai-summaries).

Feature

**Attack exposure scores and attack paths released to General Availability**

The attack path simulation feature that generates attack exposure scores and attack paths for findings that expose your high-value resources is now released to [General Availability](https://cloud.google.com/products#product-launch-stages).

For information about the feature, see [Attack exposure scores and attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn).

## July 31, 2023

Feature

The Security Health Analytics detector `NETWORK_POLICY_DISABLED` now recognizes network policies that are implemented by using GKE Dataplane V2.

For more information, see the following:

  * [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2)
  * [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings)



## July 26, 2023

Feature

The custom modules feature for Event Threat Detection is now in [Preview](https://cloud.google.com/products#product-launch-stages). Custom modules allow you to define custom detectors for Event Threat Detection.

For more information, see [Overview of custom modules for Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview).

## July 14, 2023

Feature

AI-generated summaries of Security Command Center findings are released to [Preview](https://cloud.google.com/products#product-launch-stages). When you view finding details, you can now read explanations that are generated dynamically by artificial intelligence (AI).

For more information, see [AI-generated summaries](https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview#ai-summaries).

## July 13, 2023

Feature

Recommendations from the IAM recommender are now available as findings in Security Command Center in a [Preview](https://cloud.google.com/products#product-launch-stages) release.

The following IAM recommender recommendations are now published as `Vulnerability` class findings in Security Command Center:

  * IAM role has excessive permissions
  * Service agent role replaced with basic role
  * Service agent granted basic role
  * Unused IAM role



For more information, see [Security sources > IAM recommender](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#iamrec-source).

## June 28, 2023

Deprecated

As of June 20, 2023, Security Command Center Asset API endpoints and dependent functionality are deprecated and will be removed from the product for all users on or after June 20, 2024. Use [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview) and its API instead.

After June 20, 2023, the asset functionality is not included with new activations of Security Command Center.

If you activated Security Command Center before June 20, 2023, but have not used the asset functionality in the 90 days prior to June 20, 2023, the asset functionality is removed.

If you activated Security Command Center before June 20, 2023, and have used the asset functionality in the 90 days prior to June 20, 2023, the asset functionality remains available for you until June 20, 2024 or later.

The deprecation applies to the following Security Command Center interfaces:

  * Security Command Center Asset API endpoints
  * Except for `gcloud scc assets update-marks`, which is not deprecated, the `assets` subgroup of the `gcloud scc` CLI command
  * The **Assets** page and related functionality in the Google Cloud Console



## June 22, 2023

Change

Only the [Security Center Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.serviceAgent) (`roles/securitycenter.serviceAgent`) role is required by the Security Command Center service account. Previously, the service account also required the `roles/serviceusage.serviceUsageAdmin` and `roles/cloudfunctions.serviceAgent` roles to work properly.

## June 21, 2023

Feature

Event Threat Detection, a built-in service of Security Command Center, released the following new rules to [General Availability](https://cloud.google.com/products#product-launch-stages).

  * `Initial Access: Dormant Service Account Action`
  * `Privilege Escalation: Dormant Service Account Granted Sensitive Role`
  * `Persistence: Impersonation Role Granted For Dormant Service Account`
  * `Initial Access: Dormant Service Account Key Created`



For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## June 12, 2023

Feature

**New`Finding` attribute: `userAgent`**

The `userAgent` attribute is added to the `Access` object, which is included in the `Finding` object of the Security Command Center API.

The `userAgent` attribute identifies the user agent of the caller that is associated with a Security Command Center finding.

For more information, see the Security Command Center API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## June 08, 2023

Feature

**Usage-based pricing for organization-level activations of Security Command Center**   


You can now use usage-based pricing instead of a fixed-price subscription to activate Security Command Center Premium tier at the organization level. The feature lets you activate Security Command Center at the organization level yourself in the Cloud console. Billing for organization-level activations of Security Command Center is based on the resource consumption in your organization and uses [a usage-based pricing model](https://cloud.google.com/security-command-center/pricing#organization-level-activations). 

For more information, see [Overview of organization-level activation](https://cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation).

Announcement

**Security Command Center Cryptomining Protection Program**

The Security Command Center Cryptomining Protection Program is launched to General Availability. The program offers financial protection up to $1 million USD to cover unauthorized Google Cloud compute expenses that are associated with undetected cryptocurrency mining attacks for Security Command Center Premium customers.

For more information, see [Security Command Center Cryptomining Protection Program](https://cloud.google.com/security-command-center/cryptomining-protection-program).

## June 02, 2023

Change

The Google Cloud console has been updated to change how you open Security Command Center pages. Previously, you selected pages using tabs on the main page. Now you select pages from the slide-out menu on the left side of the console. To show the menu, hold your pointer over the icons on the left side of the console.

For an overview of the pages, see [Using Security Command Center in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center).

## May 17, 2023

Change

With project-level activations of the Security Command Center Premium tier, you can now enable certain Premium-tier threat and vulnerability findings that require organization-level access by activating the Standard tier at the organization level in addition to your project-level activation. These finding categories were previously unsupported with project-level activations.

For more information, see [Premium tier feature support with project-level activations](https://docs.cloud.google.com/security-command-center/docs/activate-scc-project-level-limitations#pla-premium-features).

## May 15, 2023

Announcement

The pricing for project-level activations of Security Command Center has been reduced by lowering the Security Command Center rate for the usage of the following Google Cloud services:

  * Compute Engine
  * GKE-Autopilot
  * App Engine
  * Cloud SQL



For more information, see [Pricing for project-level activations](https://cloud.google.com/security-command-center/pricing#project-level-activations).

## May 04, 2023

Fixed

An issue that affected the display of the counts of controls for certain CIS Google Cloud Platform Benchmark (CIS Benchmark) reports in the Google Cloud console has been fixed.

On March 31, 2023, an update to Security Health Analytics affected the behavior of certain detectors for versions 1.0, 1.1, and 1.2 of the CIS Benchmark reports. The count of controls for CIS Benchmark version 1.3, as well any as CSV exports, were unaffected.

Between March 31, 2023 and May 4, 2023, the following detectors might have been counted and grouped under the incorrect CIS level on the **Compliance** tab of Security Command Center:

  * `API_KEY_EXISTS`
  * `API_KEY_APIS_UNRESTRICTED`
  * `API_KEY_NOT_ROTATED`
  * `FIREWALL_NOT_MONITORED`
  * `ROUTE_NOT_MONITORED`
  * `NETWORK_NOT_MONITORED`
  * `BUCKET_IAM_NOT_MONITORED`
  * `SQL_INSTANCE_NOT_MONITORED`
  * `VPC_FLOW_LOGS_SETTINGS_NOT_RECOMMENDED`
  * `SQL_LOG_STATEMENT`
  * `ACCESS_TRANSPARENCY_DISABLED`



## April 26, 2023

Feature

Event Threat Detection, a built-in service of Security Command Center, launched the following new rules to [Preview](https://cloud.google.com/products#product-launch-stages).

  * `Persistence: Impersonation Role Granted For Dormant Service Account`
  * `Privilege Escalation: Dormant Service Account Granted Sensitive Role`



The `Persistence: Impersonation Role Granted For Dormant Service Account` rule detects events where a principal is granted permissions to impersonate a dormant user-managed service account.

The `Privilege Escalation: Dormant Service Account Granted Sensitive Role` rule detects events where a dormant user-managed service account was granted one or more sensitive IAM roles.

For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## April 13, 2023

Feature

Event Threat Detection, a built-in service of Security Command Center, launched the following new rules to [Preview](https://cloud.google.com/products#product-launch-stages).

  * Defense Evasion: Breakglass Workload Deployment Created
  * Defense Evasion: Breakglass Workload Deployment Updated



These rules detect when the break-glass flag is used to override [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview) controls when deploying or updating workloads. For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## April 12, 2023

Feature

The custom modules feature for Security Health Analytics is now generally available (GA). Custom modules allow you to define custom detectors for Security Health Analytics.

For more information, see [Overview of custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview).

## April 11, 2023

Feature

Event Threat Detection, a built-in service of Security Command Center, launched the following new rules to [General Availability](https://cloud.google.com/products#product-launch-stages).

  * Privilege Escalation: Anomalous Impersonation of Service Account for Admin Activity
  * Privilege Escalation: Anomalous Multistep Service Account Delegation for Admin Activity
  * Privilege Escalation: Anomalous Multistep Service Account Delegation for Data Access
  * Privilege Escalation: Anomalous Service Account Impersonator for Admin Activity
  * Privilege Escalation: Anomalous Service Account Impersonator for Data Access



These rules detect anomalous activities that are taken by someone who is using an impersonated service account to access Google Cloud. For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## April 06, 2023

Deprecated

The legacy version of the **Findings** tab is removed from Security Command Center in the Google Cloud console. You can work with findings in the Google Cloud console only by using the new version of the **Findings** tab.

For more information, see [Work with findings in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-work-with-findings-in-the-dashboard).

## April 03, 2023

Feature

The `moduleName` attribute is added to the `Finding` object of the Security Command Center API.

The `moduleName` attribute, when included in a finding, identifies the full resource name of the specific detection module of the Security Command Center service that generated the finding.

For more information, see the Security Command Center API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## March 31, 2023

Feature

Security Command Center supports CIS Google Cloud Computing Foundations Benchmark v1.3.0.

The following detectors are new for v1.3.0:

  * `Access transparency disabled`
  * `Cloud Asset API disabled`
  * `Dataproc CMEK disabled`
  * `Essential contacts not configured`
  * `Flow logs settings not recommended`



The following detectors have been updated:

  * `Audit logging disabled`



For more information about Security Command Center support for standards and compliance, see the following:

  * [Detectors and compliance](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#detectors_and_compliance)
  * [CIS Google Cloud Computing Platform Benchmarks](https://www.cisecurity.org/benchmark/google_cloud_computing_platform)



## March 23, 2023

Feature

The version 3.0 release of the [Google SCC App for QRadar](https://exchange.xforce.ibmcloud.com/hub/extension/e4644304db756c0113c9c65691bb4704), which lets you send Security Command Center data to QRadar v7.4.1FP2+, is generally available.

This version includes support for multiple Google Cloud organizations, bug fixes, and supportability improvements.

For information about downloading and installing the new application, see [Upgrade the Google SCC app](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-qradar#upgrade_the_google_scc_app).

Feature

The March 20, 2023 release of the [Google Cloud SCC](https://xsoar.pan.dev/marketplace/details/GoogleCloudSCC) content pack for sending Security Command Center data to Cortex XSOAR is generally available.

This version includes support for multiple Google Cloud organizations, bug fixes, and supportability improvements.

For information about downloading and installing the new content pack, see [Upgrade the Google Cloud SCC content pack](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-cortex-xsoar#upgrade_the_scc_content_pack).

Feature

The version 2.0 release of the [Google SCC Add-on For Splunk](https://splunkbase.splunk.com/app/6426) and the [Google SCC App For Splunk](https://splunkbase.splunk.com/app/6425), which let you send Security Command Center data to Splunk, is generally available.

This version includes support for multiple Google Cloud organizations, bug fixes, and supportability improvements.

For information about downloading and installing the new applications, see [Upgrade Google SCC App for Splunk and Google SCC Add-on for Splunk](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-splunk#upgrade_google_scc_app_for_splunk_and_google_scc_add-on_for_splunk).

Feature

The version 3.0 release of the [Google SCC App for ELK](https://storage.googleapis.com/security-center-elastic-stack/GoogleSCCElasticIntegration-Installation.zip), which lets you send Security Command Center data to Elastic Stack, is generally available.

This version includes support for multiple Google Cloud organizations, bug fixes, and supportability improvements.

For information about downloading and installing the new application, see [Upgrade the Docker container](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker#upgrade_the_docker_container).

## March 17, 2023

Feature

The following attributes were added to the `Finding` object of the Security Command Center API.

  * `cloudDlpInspection`
  * `cloudDlpDataProfile`



The `cloudDlpInspection` attribute provides details about the results of a Cloud Data Loss Prevention (Cloud DLP) [inspection job](https://docs.cloud.google.com/dlp/docs/concepts-job-triggers). The `cloudDlpDataProfile` attribute provides the name of a Cloud DLP [data profile](https://docs.cloud.google.com/dlp/docs/data-profiles) that is associated with a finding.

For more information, see the Security Command Center API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

Feature

Event Threat Detection, a built-in service of Security Command Center Premium, has launched the `Initial Access: Excessive Permission Denied Actions` rule to [General Availability](https://cloud.google.com/products#product-launch-stages). This rule detects events where a principal repeatedly triggers _permission denied_ errors across multiple methods and services.

For more information about Event Threat Detection findings, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

Feature

[Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview), a built-in service of Security Command Center, launched the following detectors to [Preview](https://cloud.google.com/products#product-launch-stages).

  * `Defense Evasion: Unexpected kernel code modification`
  * `Defense Evasion: Unexpected kernel read-only data modification`
  * `Defense Evasion: Unexpected ftrace handler`
  * `Defense Evasion: Unexpected interrupt handler`
  * `Defense Evasion: Unexpected kernel modules`
  * `Defense Evasion: Unexpected kprobe handler`
  * `Defense Evasion: Unexpected processes in runqueue`
  * `Defense Evasion: Unexpected system call handler`



These modules analyze runtime Linux kernel integrity to detect common evasion techniques used by malware.

## March 01, 2023

Deprecated

The legacy version of the **Findings** tab in the Security Command Center dashboard in the Cloud console is now deprecated. Similar functionality is currently available in the new version of the **Findings** tab.

After March 31, 2023, the option to use the legacy **Findings** tab will be removed from the dashboard. After that date, you will be able to work with findings in the console only by using the newer, default version of the **Findings** tab.

For more information about working with Security Command Center findings by using the default **Findings** tab, see [Work with findings in the Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-work-with-findings-in-the-dashboard).

## February 07, 2023

Change

[Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), a built-in service of Security Command Center, launched the `Persistence: New API Method` rule to [General Availability](https://cloud.google.com/products#product-launch-stages). This rule detects anomalous usage of Google Cloud services by IAM service accounts. For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## February 06, 2023

Feature

The version 1.0 release of the Google SCC ITSM app and the Google SCC SIR app, which let you send data, such as findings, sources, assets, and audit logs, from Security Command Center to ServiceNow, is generally available. For information about downloading and installing the new applications, see [Sending Security Command Center data to ServiceNow](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-servicenow).

## January 30, 2023

Feature

**Project-level activation of Security Command Center**

The Security Command Center project-level activation feature is generally available. The feature lets you enable Security Command Center for individual Google Cloud projects yourself in the Cloud console. Billing for project-level activations of Security Command Center is based on resource consumption in the project and uses [a pay-as-you-go billing model](https://cloud.google.com/security-command-center/pricing#project-level-activations).

For more information, see [Overview of project-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#project-level-activation-overview).

## January 27, 2023

Feature

The new and improved **Findings** page in the Cloud Console is now generally available and the default view for working with Security Command Center findings. With the redesigned **Findings** page, you can query, filter, and investigate Security Command Center findings faster and more efficiently. For more information, see [Work with findings in the Security Command Center dashboard](https://docs.cloud.google.com/security-command-center/docs/how-to-work-with-findings-in-the-dashboard).

## December 22, 2022

Feature

The `userName` attribute was added to the `Finding` object of the Security Command Center API.

The value of the `userName` attribute depends on the type of the finding and is likely not an IAM principal. For example, this can be a system username if the finding is related to a virtual machine, or it be an application login username.

For more information, see the Security Command Center API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## December 16, 2022

Feature

[Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), a built-in service of Security Command Center, launched the `Initial Access: Dormant Service Account Action` rule to [Preview](https://cloud.google.com/products#product-launch-stages). This rule detects events where a dormant user-managed service account triggered an action. For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## December 15, 2022

Feature

[Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), a built-in service of Security Command Center, launched the following rules to [Preview](https://cloud.google.com/products#product-launch-stages).

  * Privilege Escalation: Anomalous Impersonation of Service Account for Admin Activity
  * Privilege Escalation: Anomalous Multistep Service Account Delegation for Admin Activity
  * Privilege Escalation: Anomalous Multistep Service Account Delegation for Data Access
  * Privilege Escalation: Anomalous Service Account Impersonator for Admin Activity
  * Privilege Escalation: Anomalous Service Account Impersonator for Data Access



These rules detect the unusual impersonation or delegation of a service account, as recorded in either the Admin Activity or Data Access audit logs. For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## December 08, 2022

Feature

Sensitive Actions Service, a built-in service of Security Command Center Premium, is now [generally available](https://cloud.google.com/products#product-launch-stages).

Sensitive Actions Service detects when actions are taken in your Google Cloud organization, folders, and projects that could be damaging to your business if they were to be taken by a malicious actor.

For more information, see [Sensitive Actions Service overview](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview).

Feature

The `Malicious URL Observed` detector of Container Threat Detection, a built-in service of Security Command Center Premium, is now [generally available](https://cloud.google.com/products#product-launch-stages).

The detector checks URLs observed in arguments passed by executables against known phishing and malware URLs to determine if they are malicious.

You can see the full details of the detector's findings only if you upgrade to the refreshed findings display in the Security Command Center dashboard.

For more information, see the following pages:

  * [Container Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)
  * [Findings Workflow Improvements](https://docs.cloud.google.com/security-command-center/docs/findings-summary)



## December 05, 2022

Feature

The `kernelRootkit` attribute was added to the `Finding` object of the Security Command Center API.

The `kernelRootkit` attribute contains information about a kernel rootkit that triggered a finding, including the following:

  * Name of the rootkit, if available.
  * Whether unexpected modifications were made to the kernel's code, read-only data memory, or certain important kernel data structures.



For more information, see the Security Command Center API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## December 02, 2022

Feature

[Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), a built-in service of Security Command Center, launched the `Initial Access: Database Superuser Writes to User Tables` rule to [General Availability](https://cloud.google.com/products#product-launch-stages). This rule detects events where a Cloud SQL superuser (`postgres` for PostgreSQL servers or `root` for MySQL users) writes to non-system tables. For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## November 16, 2022

Feature

Event Threat Detection, a built-in service of Security Command Center Premium, has launched the `Initial Access: Excessive Permission Denied Actions` rule to [Preview](https://cloud.google.com/products#product-launch-stages). This rule detects events where a principal repeatedly triggers _permission denied_ errors across multiple methods and services.

For more information about Event Threat Detection findings, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## November 14, 2022

Feature

The `files` attribute was added to the `Finding` object of the Security Command Center API.

The `files` attribute contains information about each file that triggered a finding, including the name of the file, the full path to the file, and the size of the file. 

For more information, see the Security Command Center API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## November 10, 2022

Feature

Security Command Center added the ability to export findings to a CSV file from the Google Cloud console. For more information, see [Export findings to a CSV file](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#csv).

## November 07, 2022

Feature

Security Command Center released two new error detectors:

  * `KTD blocked by admission controller`
  * `KTD image pull failure`



These detectors report configuration errors that prevent the Container Threat Detection service from functioning properly. 

Remediation guidance is provided for each finding type. For more information, see [Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

## October 21, 2022

Feature

Event Threat Detection, a built-in service of Security Command Center, launched the following rules to [general availability](https://cloud.google.com/products#product-launch-stages) (GA).

  * `Discovery: Can get sensitive Kubernetes object check`
  * `Privilege Escalation: Changes to sensitive Kubernetes RBAC objects`
  * `Privilege Escalation: Create Kubernetes CSR for master cert`
  * `Privilege Escalation: Creation of sensitive Kubernetes bindings`
  * `Privilege Escalation: Get Kubernetes CSR with compromised bootstrap credentials`
  * `Privilege Escalation: Launch of privileged Kubernetes container`



These rules detect scenarios where a potentially malicious actor attempted to query or escalate privileges in Google Kubernetes Engine. For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## October 19, 2022

Feature

Rapid Vulnerability Detection, a built-in service of Security Command Center Premium, is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

Rapid Vulnerability Detection is a zero-configuration network and web application scanner that detects weak credentials, incomplete software installations, and other critical vulnerabilities that have a high likelihood of being exploited.

For more information, see [Rapid Vulnerability Detection conceptual overview](https://docs.cloud.google.com/security-command-center/docs/concepts-rapid-vulnerability-detection-overview).

## October 03, 2022

Feature

**Error notifications in Security Command Center console**

When Security Command Center detects configuration errors that prevent services from detecting threats or vulnerabilities, a pop-up notification appears in the Security Command Center console. The notification includes the number of configuration errors currently detected.

After you fix an error, the error notification is cleared after the next scan for that error type. For information about the scan interval for each error type, see [Error detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors#error_detectors).

## September 30, 2022

Feature

Sensitive Actions Service, a built-in service of Security Command Center Premium, is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

Sensitive Actions Service detects when actions are taken in your Google Cloud organization, folders, and projects that could be damaging to your business if they were to be taken by a malicious actor.

For more information, see [Sensitive Actions Service overview](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview).

Feature

Container Threat Detection, a built-in service of Security Command Center Premium, has launched a new detector, `Malicious URL Observed`, in [Preview](https://cloud.google.com/products#product-launch-stages).

The detector checks URLs observed in arguments passed by executables against known phishing and malware URLs to determine if they are malicious.

Full details for this findings are available in the Security Command Center dashboard only if you upgrade to the refreshed findings display.

For more information, see:

  * [Container Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)
  * [Findings Workflow Improvements](https://docs.cloud.google.com/security-command-center/docs/findings-summary)



## September 28, 2022

Feature

The `parentDisplayName` attribute was added to the `Finding` object of the Security Command Center API.

The `parentDisplayName` attribute provides the display name of the Security Command Center service or _source_ that produced a finding. 

For more information, see the Security Command Center API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## September 02, 2022

Feature

[Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), a built-in service of Security Command Center, launched the `Exfiltration: Cloud SQL Over-Privileged Grant` rule to [General Availability](https://cloud.google.com/products#product-launch-stages). This rule detects events where a Cloud SQL for PostgreSQL user or role was granted all privileges to a database, or to all tables, procedures, or functions in a schema. For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## August 22, 2022

Feature

The following attributes were added to the `Finding` object of the Security Command Center API:

  * `Database` provides information about access to a database that is related to a finding.
  * `serviceAccountKeyName`, `serviceAccountDelegationInfo`, and `principalSubject` attributes were added to the existing `access` attribute. These new attributes provide additional context about the principals that are associated with a finding.
  * `uris`, a new attribute within the `indicator` attribute, lists any malicious URIs that are associated with a finding.



For more information, see the Security Command Center API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## August 08, 2022

Feature

Event Threat Detection, a built-in service of Security Command Center, launched the following rules to [Preview](https://cloud.google.com/products#product-launch-stages).

  * `Discovery: Can get sensitive Kubernetes object check`
  * `Privilege Escalation: Changes to sensitive Kubernetes RBAC objects`
  * `Privilege Escalation: Create Kubernetes CSR for master cert`
  * `Privilege Escalation: Creation of sensitive Kubernetes bindings`
  * `Privilege Escalation: Get Kubernetes CSR with compromised bootstrap credentials`
  * `Privilege Escalation: Launch of privileged Kubernetes container`



These rules detect scenarios where a malicious actor attempted to query for or escalate privileges in Google Kubernetes Engine. For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## July 21, 2022

Feature

The `container` and `kubernetes` attributes were added to the `Finding` object.

The `container` attribute provides information about both Kubernetes and non-Kubernetes containers that are associated with a given finding. The `kubernetes` attribute provides information about Kubernetes resources that are associated with a given finding.

For more information, see the Security Command Center API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## July 18, 2022

Feature

[Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview), a built-in service of Security Command Center Premium, is generally available ([GA](https://cloud.google.com/products?_gl=1*inf9xt*_ga*NzI5Nzk0OTkyLjE2NTUxNDEyODg.*_ga_WH2QY8WWF5*MTY1ODE2MzM2My4xMDguMS4xNjU4MTY0MTczLjA.#product-launch-stages)). VM Threat Detection detects cryptocurrency mining software, which is among the most common types of software installed in compromised cloud environments.

## June 30, 2022

Feature

The `contacts` and `indicator.signatures` attributes were added to the `Finding` object.

  * The `contacts` attribute is a map containing the contacts for the given finding. The key represents the type of contact, and the value contains a list of all contacts of that type.
  * The `indicator.signatures[]` attribute lists matched signatures that indicate that a given process is present in the environment.



For more information, see the API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## May 27, 2022

Feature

The `compliances`, `exfiltration`, and `processes` attributes were added to the `Finding` object.

  * The `compliances` attribute provides details about security standards that are unmet.
  * The `exfiltration` attribute provides details about the sources and targets of an exfiltration attempt.
  * The `processes` attribute provides details about operating system processes relevant to a finding.



For more information, see the API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## May 16, 2022

Feature

Updates were made to the applications that let you send Security Command Center data to to the following SIEM and SOAR platforms:

  * [Cortex XSOAR](https://www.paloaltonetworks.com/cortex/cortex-xsoar)—see [Sending Security Command Center data to Cortex XSOAR](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-cortex-xsoar).
  * [Elastic Stack](https://www.elastic.co/elastic-stack/)—see [Sending Security Command Center data to Elastic Stack](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack) and [Sending Security Command Center data to Elastic Stack using Docker](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker).
  * [IBM QRadar](https://www.ibm.com/qradar)—see [Sending Security Command Center data to IBM QRadar](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-qradar).



In addition, Security Command Center can automatically send findings, assets, audit logs, and security sources to [Splunk](https://www.splunk.com/). For more information, see [Sending Security Command Center data to Splunk](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-splunk).

## April 28, 2022

Feature

Security Command Center error detectors are generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Error detectors report configuration errors that prevent Security Command Center and its services from functioning properly. Remediation guidance is provided for each finding type. For more information, see [Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

Feature

The `connections[]` and `description` attributes were added to the `Finding` object.

  * The `connections[]` attribute contains information about the IP connection associated with the finding. It includes the destination IP address, the destination port, the source IP address, the source port, and the protocol.
  * The `description` attribute provides an explanation of the finding.



For more information, see the API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## April 07, 2022

Feature

The `iamBindings[]` and `nextSteps` attributes were added to the `Finding` object.

  * The `iamBindings[]` attribute provides a list of IAM bindings associated with the finding.
  * The `nextSteps` attribute provides recommended actions you can take to address the finding.



For more information, see the API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## March 29, 2022

Feature

A revamp of the **Findings** workflow is in [Preview](https://cloud.google.com/products#product-launch-stages). This Preview includes improvements in the filtering and querying experience. For a complete summary of improvements, see [Summary: Findings Workflow Improvements](https://docs.cloud.google.com/security-command-center/docs/findings-summary). To opt in to this Preview, see [Upgrade to the Findings Workflow Improvements](https://docs.cloud.google.com/security-command-center/docs/findings-summary#upgrade).

## March 07, 2022

Feature

To support a rich query experience on complex array elements, the `contains()` filter function was introduced. You can use this function in your finding queries to do the following:

  * Exact element matching: Match array elements that contain the exact string, `"example"`.
  * Specific number operations: Match array elements that are greater than or equal to `100`.
  * Complex filtering against array structures: Match array elements that contain property `x` with a corresponding value `y`.



For more information, see [Filtering on array-type fields](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings#array-contains-filtering).

## March 02, 2022

Feature

You can now configure automatic exports of Security Command Center findings to a BigQuery dataset. For more information, see [Export findings to BigQuery for analysis](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query).

Feature

The `vulnerability.cve.upstreamFixAvailable` attribute was added to the `Finding` object. This is a `boolean` field that specifies whether a [Common Vulnerabilities and Exposures](https://cve.mitre.org/) (CVE) fix is available. For more information, see the API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#resource:-finding) object.

## February 24, 2022

Feature

Security Command Center can automatically send findings, assets, and security sources to the following SIEM and SOAR platforms:

  * [Cortex XSOAR](https://www.paloaltonetworks.com/cortex/cortex-xsoar)—see [Sending Security Command Center data to Cortex XSOAR](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-cortex-xsoar).
  * [Elastic Stack](https://www.elastic.co/elastic-stack/)—see [Sending assets and findings to Elastic Stack](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack) and [Exporting assets and findings with Docker and Elastic Stack](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker).
  * [IBM QRadar](https://www.ibm.com/qradar)—see [Sending Security Command Center data to IBM QRadar](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-qradar).



## February 22, 2022

Feature

[MITRE ATT&CK](https://attack.mitre.org/) framework details related to findings are now available as finding attributes for all Security Command Center services. The framework explains [tactics](https://attack.mitre.org/tactics/enterprise/) and [techniques](https://attack.mitre.org/techniques/enterprise/) for attacks against cloud resources, and provides remediation guidance. Although these attributes are available across all built-in and integrated services, only [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) and [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) are populating them at this time. For more information, see the API documentation for the [`Findings`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings) object.

## February 10, 2022

Feature

Access-related details are now available as finding attributes for all Security Command Center services. These attributes relate to an access event associated with a finding. They contain details such as the caller's IP address, which service and method was called, and what region the access event occurred in. Although access-related attributes are available across all built-in and integrated services, they're only populated by [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) at this time. For more information, see the API documentation for the [`Findings`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings) object.

## February 07, 2022

Feature

Security Health Analytics, a built-in service of Security Command Center, released the [`OPEN_GROUP_IAM_MEMBER`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#open_group_iam_member) detector to [General Availability](https://cloud.google.com/products#general-availability).

Fixed

Previously, the following Event Threat Detection rules were made temporarily unavailable because they were generating extraneous findings:

  * `Persistence: New API Method`
  * `Persistence: New Geography`



The underlying issue has been resolved. These rules are now operational. For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## February 02, 2022

Feature

Event Threat Detection, a built-in service of Security Command Center, launched the **Exfiltration: BigQuery Data to Google Drive** rule to [Preview](https://cloud.google.com/products#product-launch-stages). This rule detects events where the protected organization's BigQuery data is saved, through extraction operations, to a Google Drive folder. For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## January 31, 2022

Feature

Web Security Scanner, a built-in service of Security Command Center, released the `CACHEABLE_PASSWORD_INPUT` and `SESSION_ID_LEAK` finding types.

For more information, see [Web Security Scanner findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#web-security-scanner-findings).

Feature

Virtual Machine Threat Detection, a built-in service of Security Command Center Premium, is in [Preview](https://cloud.google.com/products#product-launch-stages). During the Preview, VM Threat Detection detects cryptocurrency mining software, which is among the most common types of software installed in compromised cloud environments.

For more information, see [Virtual Machine Threat Detection conceptual overview](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview).

Feature

Web Security Scanner, a built-in service of Security Command Center, provides detectors for the [OWASP Top 10 2017](https://owasp.org/www-pdf-archive/OWASP_Top_10-2017_%28en%29.pdf.pdf) and [OWASP Top 10 2021](https://owasp.org/Top10/). For more information, see [Detectors and Compliance](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview#detectors_and_compliance).

## January 26, 2022

Feature

Security Command Center supports [CIS Google Cloud Computing Foundations Benchmark v1.2.0](https://www.cisecurity.org/benchmark/google_cloud_computing_platform/) (CIS Google Cloud Foundation 1.2.0).

The following detectors have been added:

  * `BIGQUERY_TABLE_CMEK_DISABLED`
  * `CONFIDENTIAL_COMPUTING_DISABLED`
  * `DNS_LOGGING_DISABLED`
  * `SQL_EXTERNAL_SCRIPTS_ENABLED`
  * `SQL_LOG_DURATION_DISABLED`
  * `SQL_LOG_ERROR_VERBOSITY`
  * `SQL_LOG_EXECUTOR_STATS_ENABLED`
  * `SQL_LOG_HOSTNAME_ENABLED`
  * `SQL_LOG_MIN_ERROR_STATEMENT_SEVERITY`
  * `SQL_LOG_MIN_MESSAGES`
  * `SQL_LOG_PARSER_STATS_ENABLED`
  * `SQL_LOG_PLANNER_STATS_ENABLED`
  * `SQL_LOG_STATEMENT`
  * `SQL_LOG_STATEMENT_STATS_ENABLED`
  * `SQL_REMOTE_ACCESS_ENABLED`
  * `SQL_SKIP_SHOW_DATABASE_DISABLED`
  * `SQL_TRACE_FLAG_3625`
  * `SQL_USER_CONNECTIONS_CONFIGURED`
  * `SQL_USER_OPTIONS_CONFIGURED`



For more information, see [Detectors and compliance](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#detectors_and_compliance).

## January 24, 2022

Feature

Web Security Scanner, a built-in service of Security Command Center, released the `SQL_INJECTION` and `STRUTS_INSECURE_DESERIALIZATION` finding types.

For more information, see [Web Security Scanner findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#web-security-scanner-findings).

## January 10, 2022

Feature

Web Security Scanner, a built-in service of Security Command Center, released the `INSECURE_ALLOW_ORIGIN_ENDS_WITH_VALIDATION`, `INSECURE_ALLOW_ORIGIN_STARTS_WITH_VALIDATION`, and `XXE_REFLECTED_FILE_LEAKAGE` finding types.

For more information, see [Web Security Scanner findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#web-security-scanner-findings).

## December 30, 2021

Feature

Security Health Analytics, a built-in service of Security Command Center, launched the `DATAPROC_IMAGE_OUTDATED` detector to [General Availability](https://cloud.google.com/products#product-launch-stages). This detector finds clusters created with Dataproc image versions that are affected by security vulnerabilities in the Apache Log4j 2 utility ([CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) and [CVE-2021-45046](https://nvd.nist.gov/vuln/detail/CVE-2021-45046)). For more information, see [Dataproc vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#dataproc-findings).

## December 21, 2021

Feature

Event Threat Detection, a built-in service of Security Command Center, launched the **Active Scan: Log4j Vulnerable to RCE** rule to [General Availability](https://cloud.google.com/products#product-launch-stages). This rule detects active Log4j vulnerabilities by identifying DNS queries for unobfuscated domains that were initiated by supported Log4j vulnerability scanners. For more information, see [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules) rules.

## December 16, 2021

Feature

Event Threat Detection, a built-in service of Security Command Center, launched the **Initial Access: Log4j Compromise Attempt** rule to [General Availability](https://cloud.google.com/products#product-launch-stages). This rule detects Java Naming and Directory Interface (JNDI) lookups within headers or URL parameters. These lookups may indicate attempts at Log4Shell exploitation. For more information, see [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules) rules.

## December 13, 2021

Feature

Event Threat Detection, a built-in service of Security Command Center, launched the **Persistence: New API Method** rule to [Preview](https://cloud.google.com/products#product-launch-stages). This rule detects anomalous API behavior by examining Cloud Audit Logs for requests to Google Cloud services that a principal has not seen before. For more information, see [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules) rules.

## December 10, 2021

Feature

Event Threat Detection, a built-in service of Security Command Center, launched the **Evasion: Access from Anonymizing Proxy** rule to [General Availability](https://cloud.google.com/products#product-launch-stages). This rule detects Google Cloud service modifications that originated from anonymous proxy IP addresses, like Tor IP addresses. For more information, see [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules) rules.

## December 07, 2021

Feature

To facilitate the flow of information between Security Command Center and third-party systems, a resource called [`ExternalSystems`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#ExternalSystem) was added under the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings) object. A finding can contain multiple `ExternalSystems` fields. 

The `ExternalSystems` resource can contain any of the following:

  * Third-party SIEM/SOAR fields within Security Command Center
  * External system information
  * External system finding fields



A caller with the **Security Center External Systems Editor** (`roles/securitycenter.externalSystemsEditor`) IAM role can update an `ExternalSystems` object using the [`organizations.sources.findings.externalSystems.patch`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings.externalSystems/patch) API.

Feature

Event Threat Detection, a built-in service of Security Command Center, released the **Exfiltration: BigQuery Data Extraction** rule. This rule is available in [Preview](https://cloud.google.com/products#product-launch-stages). It detects events where an organization's BigQuery data is exported to an externally visible Cloud Storage bucket. For more information, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## November 19, 2021

Feature

Security Command Center has launched Mute Findings in general availability.

Mute Findings is a powerful volume management feature that lets you create filters to automatically hide or suppress current _and_ future findings based on criteria you specify. The feature can save you time from reviewing or responding to security findings for assets that are isolated, fall within acceptable business parameters, or aren't relevant to your organization based on your company's policies.

To learn more, see [Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

## November 17, 2021

Feature

Web Security Scanner, a built-in service of Security Command Center, released the `SERVER_SIDE_REQUEST_FORGERY` finding type in general availability.

For more information, see [Remediating Web Security Scanner findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#remediate-findings).

## October 26, 2021

Issue

An issue that resulted in Security Command Center incorrectly reporting findings for some monitoring vulnerability detectors has been fixed.

Due to changes made on September 20, 2020 in the logging source upon which `FIREWALL_NOT_MONITORED`, `NETWORK_NOT_MONITORED`, `ROUTE_NOT_MONITORED`, and `SQL_INSTANCE_NOT_MONITORED` findings in Security Health Analytics are predicated, the remediation instructions for those findings were inaccurate.

The issue is resolved. Findings are being generated accurately and you are being properly alerted of misconfigurations in your organization. 

If you want to enable monitoring in order to remediate these findings, you will need to update the logs-based metrics for these findings. Updated filters are available in the findings themselves and product documentation:

  * [Vulnerabilities findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings)
  * [Remediating Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings)



If you have questions or need assistance, contact [Google Cloud Support](https://cloud.google.com/support-hub) or [Google Cloud Billing Support](https://docs.cloud.google.com/support/billing).

## October 25, 2021

Feature

The following detectors for unsafe Google Groups changes are generally available ([GA](https://cloud.google.com/products#product-launch-stages)):

  * `Credential Access: Privileged Group Opened To Public`
  * `Credential Access: Sensitive Role Granted To Hybrid Group`
  * `Credential Access: External Member Added To Privileged Group`



For more information, see [Unsafe Google Groups changes](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#unsafe_google_group_changes).

## October 13, 2021

Feature

Event Threat Detection, a built-in service of Security Command Center Premium, launched an integration with Chronicle that lets you perform advanced analysis of threat findings.

The integration lets you seamlessly send findings to Chronicle, a Google Cloud service that you can use to investigate threats and pivot through related actions and events in a unified timeline. Chronicle enriches Event Threat Detection findings, helping you identify indicators of interest and simplify investigations.

To learn more about Chronicle, see [Chronicle overview](https://docs.cloud.google.com/chronicle/docs/overview). For instructions on sending Event Threat Detection findings to Chronicle, see [Investigate findings in Chronicle](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection#investigate_findings).

## October 05, 2021

Feature

Security Health Analytics, a built-in service of Security Command Center, released new detectors in [general availability](https://cloud.google.com/products#general-availability).

The following detectors, available only in Security Command Center's [Premium tier](https://cloud.google.com/security-command-center/pricing#premium-tier), detect vulnerabilities in your Google Kubernetes Engine clusters and expand the number of detectors that support the CIS Google Kubernetes Engine (GKE) Benchmark v1.0.0:

  * [`ALPHA_CLUSTER_ENABLED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#alpha_cluster_enabled): Alpha cluster features are enabled for a GKE cluster. 
  * [`BINARY_AUTHORIZATION_DISABLED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#binary_authorization_disabled): Binary Authorization is disabled on a GKE cluster.
  * [`CLUSTER_SECRETS_ENCRYPTION_DISABLED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#cluster_secrets_encryption_disabled): Application-layer secrets encryption is disabled on a GKE cluster.
  * [`CLUSTER_SHIELDED_NODES_DISABLED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#cluster_shield_nodes_disabled): Shielded GKE nodes are not enabled for a cluster.
  * [`INTEGRITY_MONITORING_DISABLED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#integrity_monitoring_disabled): Integrity monitoring is disabled for a GKE cluster.
  * [`INTRANODE_VISIBILITY_DISABLED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#intranode_visibility_disabled): Intranode visibility is disabled for a GKE cluster.
  * [`NODEPOOL_SECURE_BOOT_DISABLED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#nodepool_secure_boot_disabled): Secure Boot is disabled for a GKE cluster.
  * [`RELEASE_CHANNEL_DISABLED`](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#release_channel_disabled): A GKE cluster is not subscribed to a release channel.



For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings). To learn how to remediate vulnerabilities, see [Remediating Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings)

## September 14, 2021

Feature

Event Threat Detection, a built-in service of Security Command Center Premium, has launched new detectors in [public preview](https://cloud.google.com/products#preview).

The following detectors monitor your Google Workspace and Cloud Audit logs and alert you when external members are added to privileged Google Groups—groups that are granted sensitive IAM roles and permissions:

  * `Credential Access: Privileged Group Joinability Risk`: Detects when Google Groups are changed to be accessible to the general public
  * `Persistence: IAM Anomalous Group Grant`: Detects when sensitive roles are granted to privileged Google Groups with external members
  * `Credential Access: External Member In Privileged Group`: Detects when an external member is added to a privileged Google Group



The following detectors monitor your Admin Activity logs and alert you to suspicious changes in Compute Engine instances:

  * `Persistence: Compute Engine Admin Added SSH Key`: Detects modification of the Compute Engine instance metadata ssh key value on established instances 
  * `Persistence: Compute Engine Admin Added Startup Script`: Detects modification of the Compute Engine instance metadata startup script value on established instances



The `Persistence: IAM Anomalous Grant` detector is enhanced and detects when sensitive roles are granted to users and service accounts.

For more information on Event Threat Detection findings, see [Rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules). To learn how Event Threat Detection monitors changes in Google Groups and defines sensitive roles, see [Unsafe Google Group changes](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#unsafe_google_group_changes).

## September 07, 2021

Feature

VM Manager [vulnerability reports](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management#vulnerability-reports), which are in preview, are now available in Security Command Center Premium. The reports identify vulnerabilities in operating systems installed on Compute Engine virtual machines, including [Common Vulnerabilities and Exposures (CVEs)](https://wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures).

For more information on integrating VM Manager with Security Command Center, see [VM Manager](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#vm_manager).

## August 11, 2021

Feature

Event Threat Detection, a built-in service of Security Command Center Premium, has launched new detectors to protect your Google Workspace domains in general availability. The detectors identify suspicious activities in member accounts and your Admin Console, including leaked passwords, attempted account breaches, settings changes, and possible government-backed attacks. For more information, see [Event Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).

Feature

Container Threat Detection, a built-in service of Security Command Center Premium, has launched a new detector, `Malicious Script Executed`, in general availability. The detector uses natural language processing to evaluate bash scripts and determine if they are malicious. For more information, see [Container Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)

Feature

Security Command Center findings now include two new attributes that provide additional information about the type of finding and the activity that triggered it. The attributes include the following:

  * **Indicator** : displayed as `indicator`. This is an indicator of compromise (IoC), or artifact, observed on a network or in an operating system that, with high confidence, indicates a computer intrusion.
  * **Finding Class** : displayed as `findingClass`. Indicates the type of finding. The following list includes finding classes and their descriptions: 
    * **Threat** : unwanted or malicious activity
    * **Vulnerability** : a potential weakness in software that increases risk to the confidentiality, integrity, and availability of your resources
    * **Misconfiguration** : a potential weakness in a resource's configuration that increases risk
    * **Observation** : a security observation provided for informational purposes



To learn more about findings, see the **Findings** tab in [Using the Security Command Center dashboard](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#findings).

Announcement

Documentation

  * Security Command Center documentation now includes a page that maps resource type formats between Cloud Asset Inventory and Security Command Center. The services use different naming conventions for resource types. For more information, see [Resource type formats in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/resource-types).



## July 19, 2021

Feature

[Security Health Analytics](https://cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings), a built-in service of Security Command Center, has launched a new detector, `DATASET_CMEK_DISABLED`, in general availability. The detector, available to Security Command Center [Premium](https://docs.cloud.google.com/security-command-center/pricing#premium-tier) customers, detects BigQuery datasets that are not encrypted using customer-managed encryption keys (CMEK). For more information, see the `DATASET_SCANNER` table in [Vulnerabilities findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#dataset_cmek_disabled).

Feature

Event Threat Detection, a built-in service of Security Command Center Premium, has launched a public preview of new detectors to protect your Google Workspace domains. The detectors identify suspicious activities in member accounts and your Admin Console, including leaked passwords, attempted account breaches, settings changes, and possible government-backed attacks. For more information, see [Event Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).

## June 07, 2021

Deprecated

Security Command Center Legacy, previously known as Cloud Security Command Center, and Event Threat Detection Legacy have been permanently disabled. 

To continue benefiting from [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview), you must migrate your organizations to Security Command Center's free Standard tier or Premium tier. [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), a built-in service of Security Command Center, is available only in the Premium tier.

For information on upgrading to Security Command Center Standard or Premium, see [Migrate from legacy Security Command Center products](https://docs.cloud.google.com/security-command-center/docs/legacy-products-migration).

## May 24, 2021

Feature

Security Command Center Premium has launched project- and folder-level roles in general availability. The feature lets you grant users Identity and Access Management (IAM) roles for specific folders and projects. You have more granular control over who can access what resources throughout your organization. For more information, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control).

You must be a [Security Command Center Premium](https://cloud.google.com/security-command-center/pricing#premium-tier) customer to use this feature. [Security Command Center Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) continues to support granting roles only at the organization level. To subscribe to Security Command Center Premium, contact your sales representative.

Change

Security Command Center now supports two versions of [CIS Benchmarks for Google Cloud Platform Foundation](https://www.cisecurity.org/benchmark/google_cloud_computing_platform/):

  * CIS Google Cloud Computing Foundations Benchmark v1.1.0 (CIS Google Cloud Foundation 1.1)
  * CIS Google Cloud Computing Foundations Benchmark v1.0.0 (CIS Google Cloud Foundation 1.0) 



For more information about supported compliance standards, see [Detectors and compliance](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#detectors_and_compliance).

Change

Security Health Analytics, a built-in service of Security Command Center, has expanded the number of detectors in the Standard tier. The Standard tier, which is free of charge, now includes the following detectors:

  * `LEGACY_AUTHORIZATION_ENABLED`: Legacy Authorization is enabled on Google Kubernetes Engine (GKE) clusters.
  * `OPEN_CISCOSECURE_WEBSM_PORT`: A firewall is configured to have an open CISCOSECURE_WEBSM port that allows generic access.
  * `OPEN_DIRECTORY_SERVICES_PORT`: A firewall is configured to have an open DIRECTORY_SERVICES port that allows generic access.
  * `OPEN_TELNET_PORT`: A firewall is configured to have an open TELNET port that allows generic access.
  * `PUBLIC_COMPUTE_IMAGE`: A Compute Engine image is publicly accessible.



For a complete list of detectors in the Standard tier, see [Pricing](https://cloud.google.com/security-command-center/pricing#standard-tier). For detailed information about all Security Health Analytics detectors, see [Vulnerabilities findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

## May 05, 2021

Feature

Security Command Center Premium has launched [Continuous Exports for Pub/Sub](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#continuous_exports) in general availability. The feature simplifies the process of creating a [`NotificationConfig`](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications#create-notification-config) and automates the export of new findings to Pub/Sub.

You must be a [Security Command Center Premium](https://cloud.google.com/security-command-center/pricing#premium-tier) customer to use the feature. [Security Command Center Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) continues to support [one-time exports](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#one-time_exports). To subscribe to Security Command Center Premium, contact your sales representative.

Announcement

Security Health Analytics, a built-in service of Security Command Center, has launched a new detector, `PUBSUB_CMEK_DISABLED`, in general availability. The detector, available to [Security Command Center Premium](https://cloud.google.com/security-command-center/pricing#premium-tier) customers, identifies Pub/Sub topics that are not encrypted with customer-managed encryption keys (CMEK). For more information, see the `PUBSUB_SCANNER` table in [Vulnerabilities findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#pubsub-findings).

Change

Event Threat Detection, a built-in service of Security Command Center, has launched a new detector in general availability. `Discovery: Service Account Self-Investigation` detects when a service account credential is used to investigate the roles associated with that same service account. For more information on detectors, see [Event Threat Detection conceptual overview](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

Announcement

Documentation

  * Event Threat Detection and Container Threat Detection documentation now includes examples of JSON output for findings. The examples show the data structure, objects, and properties present in findings. For more information, see the **Example finding formats** sections of [Using Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection#example_finding_formats) and [Using Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#example_finding_formats).

  * Security Command Center documentation now includes guidance on [Optimizing Security Command Center](https://docs.cloud.google.com/security-command-center/docs/quickstart-optimize-security-command-center) and an overview of [Data and infrastructure security](https://docs.cloud.google.com/security-command-center/docs/concepts-data-security-overview).

  * Security Health Analytics documentation now includes instructions for enabling detectors that are not turned on by default. For more information, see [Enabling Security Health Analytics detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#enable_detectors).




## April 07, 2021

Breaking

Security Command Center Legacy, previously known as Cloud Security Command Center, and Event Threat Detection Legacy are being permanently disabled for all customers on June 7, 2021.

If you onboarded to Security Command Center before May 2020, or Event Threat Detection before June 2020, and never upgraded to Security Command Center's Standard tier or Premium tier, you are using a legacy product.

To continue benefiting from [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview) and [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) without an interruption in service, customers using legacy products must migrate their organizations to Security Command Center Standard or Premium. Event Threat Detection, a built-in service of Security Command Center, is available only in the Premium tier.

For details on upgrading legacy products, see [Migrate from legacy Security Command Center products](https://docs.cloud.google.com/security-command-center/docs/legacy-products-migration).

## March 08, 2021

Change

Security Health Analytics, a built-in service of Security Command Center, launched new detectors in general availability:

Detects resources that are not using customer-managed encryption keys (CMEK)

  * `BUCKET_CMEK_DISABLED`
  * `DISK_CMEK_DISABLED`
  * `NODEPOOL_BOOK_CMEK_DISABLED`
  * `SQL_CMEK_DISABLED`



Detects vulnerabilities in Compute Engine instances

  * `DEFAULT_SERVICE_ACCOUNT_USED`
  * `SHIELDED_VM_DISABLED`



Detects publicly accessible Cloud KMS keys

  * `KMS_PUBLIC_KEY`



Detects out-of-region Compute Engine resources

  * `ORG_POLICY_LOCATION_RESTRICTION`



Detects misconfiguration of SQL instances

  * `SQL_CROSS_DB_OWNERSHIP_CHAINING`
  * `SQL_CONTAINED_DATABASE_AUTHENTICATION`
  * `SQL_CROSS_DB_OWNERSHIP_CHAINING`
  * `SQL_LOCAL_INFILE`
  * `SQL_LOG_CHECKPOINTS_DISABLED`
  * `SQL_LOG_CONNECTIONS_DISABLED`
  * `SQL_LOG_DISCONNECTIONS_DISABLED`
  * `SQL_LOG_LOCK_WAITS_DISABLED`
  * `SQL_LOG_MIN_DURATION_STATEMENT_ENABLED`
  * `SQL_LOG_MIN_ERROR_STATEMENT`
  * `SQL_LOG_TEMP_FILES`



For more information on these and other Security Health Analytics detectors, see [Vulnerabilities findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

Change

Event Threat Detection, a built in service of Security Command Center, launched a preview for a new detector.

`Service account self-investigation` detects when a service account is used to investigate roles associated with that same service account. For more information on Event Threat Detection detectors, see [Event Threat Detection conceptual overview](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

Announcement

Documentation

  * Security Health Analytics documentation now includes more detailed information about detectors, including supported assets and scan configurations. For more information, see [Vulnerabilities findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

  * The Security Health Analytics remediation page now includes suggested instructions to resolve all Security Health Analytics findings. For more information, see [Remediating Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings).

  * Event Threat Detection documentation now includes additional details on cloud logs used by the service. For more information, see [Event Threat Detection conceptual overview](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).




## February 05, 2021

Change

Security Command Center's [v1 API](https://docs.cloud.google.com/security-command-center/docs/reference/rest) now includes a `Severity` field for Findings.

The `Severity` field indicates the severity of a finding, as determined by the finding provider, and is included with all findings. The field is managed by finding providers and you are cautioned to not modify its values.

Uses for the field include listing findings of a certain severity level or grouping findings by severity level.

Read [Using the Security Command Center dashboard](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#findings) to learn more about findings and finding severity.

Change

Event Threat Detection, a built-in service of Security Command Center Premium, has launched previews for two new detectors.

`IAM: Anomalous IP geolocation` and `IAM: Anomalous user agent` detect anomalous connections to Google Cloud resources based on location and user agent, respectively.

Read more about available detectors in [Event Threat Detection conceptual overview](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).

Announcement

Documentation

  * New documentation includes guides on [enabling real-time email and chat notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-enable-real-time-notifications) and [investigating and responding to threats](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats).



## December 01, 2020

Announcement

[Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview), a built-in service of Security Command Center Premium, is now in general availability. Read these notes to learn about updates, usability improvements, and new features. See our blog post, [Monitor and secure your containers with new Container Threat Detection](https://cloud.google.com/blog/products/identity-security/container-threat-detection-is-ga), to learn more.

Change

Container Threat Detection now supports Google Kubernetes Engine (GKE) versions on the **Stable** channel. There are currently no plans to add support for GKE version 1.14.

Change

Activation latency for newly created clusters has been improved.

Fixed

A bug that blocked some information from appearing in the the process section of `Added Library Loaded` findings is fixed.

Fixed

A bug that blocked the proper display of the resource name for regional clusters in `Added Library Loaded` findings is fixed.

Announcement

Container Threat Detection documentation includes updated information about compatibility with GKE and Virtual Private Cloud.

Read [Using Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection) for more information.

## October 08, 2020

Feature

Event Threat Detection, a built-in service of Security Command Center Premium, now includes two new detectors to monitor your organization's BigQuery resources. The detectors identify data exfiltration - resources saved outside of your organization or attempts to access protected data.

Read more about available detectors in [Event Threat Detection conceptual overview](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).

Feature

The Security Command Center API now includes a `severity` field for Findings. This feature is available using Security Command Center's [`v1p1beta1` API](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings/list).

## September 08, 2020

Feature

[Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview) Premium is now in general availability ([Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) remains in beta). Read these notes to learn about updates, usability improvements, and new features.

Feature

Improved Summary Dashboard

  * A new set of interactive charts and tables provide a high-level overview of all threats and vulnerabilities.
  * An updated time selector lets you choose preset and customizable time ranges for reviewing findings and creating reports.
  * New page headers provide users with more page-specific context.



Learn more about [Using the Security Command Center dashboard](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center).

Feature

Onboarding and configuration upgrades

  * A streamlined interface lets you manage organization-wide service enablement settings.
  * A dedicated settings page for integrated services has been added to the configuration interface.



Learn more about [Setting up Security Command Center](https://docs.cloud.google.com/security-command-center/docs/quickstart-security-command-center).

Change

Security Health Analytics now supports real-time detections, with [some exceptions](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview#detection_latency). Read more about [Security Health Analytics detectors and findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

Feature

gcloud integration with new, simplified Beta APIs (**Alpha**)

  * The gcloud command line interface can now access configuration functionality through new Beta APIs. The Beta APIs provide stable, programmatic interaction equivalent in functionality to the Security Command Center interface. Learn to use gcloud to [manage Security Command Center settings](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/settings).



Feature

Documentation

  * New documentation includes details on onboarding and enablement in the [Security Command Center latency overview](https://cloud.google.com/security-command-center/docs/concepts-scan-latency-overview) and updates on billing tiers. For more information, read our [Pricing guide](https://docs.cloud.google.com/security-command-center/pricing) and visit product pages.



Feature

Managed Web Security Scans are now available to all Security Command Center Premium users. Learn more about managed scans in our [Overview of Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview).

## August 24, 2020

Feature

Audit logs are now available in Security Command Center as part of Cloud Audit Logs. Learn more about [Security Command Center audit logging](https://docs.cloud.google.com/security-command-center/docs/audit-logging).

## July 27, 2020

Deprecated

Security Command Center v1beta1 API will be disabled on Jan. 31, 2021. All users will be required to migrate to Security Command Center v1 API, which is now in general availability.

  * Update to Google-provided v1 API [client libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained).
  * Move your client libraries and [HTTP/grpc calls](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) to v1 by following instructions in the reference documentation for [service endpoints](https://cloud.google.com/security-command-center/docs/reference/rest#service-endpoint_2) and [SDK configuration](https://cloud.google.com/security-command-center/docs/how-to-programmatic-access).
  * If you call this service using your own libraries, follow the guidance in our [Security Command Center API Overview](https://cloud.google.com/security-command-center/docs/reference/rest#service:-securitycenter.googleapis.com_2) when making API requests.
  * To use `ListFindings` calls in the v1 API, update your response handling to respond to an extra layer of object nesting, as shown below: 
    * v1beta1: `response.getFindings().forEach( x -> ....)`
    * v1: `response.getListFindingsResults().forEach(x -> { x.getFinding(); .... })`



Additional changes to the v1 API are listed below. Learn more about [Using the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to#using-the-security-command-center-api).

Breaking

The finding category of `2SV_NOT_ENFORCED` is being renamed `MFA_NOT_ENFORCED`.

  * **Impact:** Case-sensitive finding notification filters, post-processing, and alerting based on the previous finding category name may fail. 
  * **Recommendation:** Update any post-processing to use the new category name.



Breaking

The `nodePools` finding source property will be removed from the `OVER_PRIVILEGED_SCOPES` findings and replaced with a source property named `VulnerableNodePools`.

  * **Impact:** Finding notification filters, post-processing and alerting based on this finding source property may fail. 
  * **Recommendation:** Modify workflows as necessary to utilize the new `VulnerableNodePools` source property.



Breaking

The `ProjectId` source property from all Security Health Analytics findings will be removed.

  * **Impact:** Finding notification filters, post-processing, and alerting based on the finding source property may fail.
  * **Recommendation:** Update workflows to utilize the project id in the `resource.project_display_name` field of a `ListFindingsResult`.



Breaking

The `SourceRanges` finding source property from findings in OPEN_FIREWALL findings will be replaced with a new `ExternalSourceRanges`, which will contain a subset of the values from the `SourceRanges` property.

  * **Impact:** Finding notification filters, post-processing and alerting based on the finding source property will fail. 
  * **Recommendation:** Modify your workflows as necessary to utilize the new `ExternalSourceRanges` source property.



Breaking

As of Sept. 1, 2020, the `ListFindings` API will no longer support searching on finding properties that are longer than 7,000 characters.

  * **Impact:** Searches on strings that are longer than 7,000 characters will not return expected results. For example, if a partial string match filter has a match at the 7,005th character on a property in a finding, that finding will not be returned because that match is past the 7,000-character threshold. An exception will not be returned.
  * **Recommendation:** Customers can remove filter restrictions (e.g. x : "some-value") that are supposed to match very long properties. The results can then be filtered locally to remove findings whose strings do not match designated criteria. Learn more about [filtering findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings#filtering_findings).



Breaking

The `ExceptionInstructions` source property will be removed from all Security Health Analytics findings.

  * **Impact:** Finding notification filters, post-processing, and alerting based on the finding source property may fail.
  * **In progress:** A new property that will indicate the current state of findings is being developed.



Breaking

The `Allowed` finding source property from `OPEN_FIREWALL` findings will be replaced with changed a new field named `ExternallyAccessibleProtocolsAndPorts`, which will contain a subset of the values from the `Allowed` property.

  * **Impact:** Finding notification filters, post-processing, and alerting based on the finding source property will fail. 
  * **Recommendation:** Modify your workflows as necessary to utilize the new `ExternallyAccessibleProtocolsAndPorts` source property.



Breaking

The `SeverityLevel` finding source property for all Security Health Analytics findings will be removed and replaced with a field named `Severity`, which retains the same values.

  * **Impact:** Finding notification filters, post-processing, and alerting based on the `SeverityLevel` finding source property will no longer be possible.
  * **Recommendation:** Replace the `SeverityLevel` finding source property with the `Severity` finding attribute property to retain existing functionality.



Breaking

As of Jan. 31, 2021, the `UpdateFinding` API will no longer support storing string properties that are longer than 7,000 characters.

  * **Impact:** Calls to `UpdateFinding` that seek to store string properties longer than 7,000 characters will be rejected with an invalid argument error.
  * **Recommendation:** Consider storing string properties longer than 7,000 characters as JSON structs or JSON lists. Learn more about [writing findings](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#Finding).



Breaking

The `AssetSettings` finding source property from `PUBLIC_SQL_INSTANCE`, `SQL_PUBLIC_IP`, `SSL_NOT_ENFORCED`, `AUTO_BACKUP_DISABLED`, `SQL_NO_ROOT_PASSWORD`, `SQL_WEAK_ROOT_PASSWORD` finding types will be removed, as it contains data duplicated from the asset entity.

  * **Impact:** Finding notification filters, post-processing, and alerting based on the finding source property will fail. 
  * **Recommendation:** Replacing the `AssetSettings` finding source property with the `Settings` resource property from the asset underlying the finding will retain existing functionality.



Change

The `CompatibleFeatures` source property in `WEAK_SSL_POLICY` findings will use a list instead of a character-separated string value.

  * **Impact:** Finding notification filters, post-processing, and alerting based on the finding source property will need to be updated to take advantage of the new data type for findings.
  * **Recommendation:** Update workflows to utilize the new data type.



Change

The `OffendingIamRoles` source property in extensions of IAM Scanner Configurations will use structured data instead of a JSON-formatted string.

  * **Impact:** Finding notification filters, post-processing, and alerting based on the finding source property will need to be updated to take advantage of the new data type on findings of the following categories: `ADMIN_SERVICE_ACCOUNT`, `NON_ORG_IAM_MEMBER`, `PRIMITIVE_ROLES_USED`, `OVER_PRIVILEGED_SERVICE_ACCOUNT_USER`, `REDIS_ROLE_USED_ON_ORG`, `SERVICE_ACCOUNT_ROLE_SEPARATION`, `KMS_ROLE_SEPARATION`.
  * **Recommendation:** Update workflows to utilize the new data type.



Change

The `AlertPolicyFailureReasons` source property in specific `Monitoring` findings from Security Health Analytics will use a list instead of a character-separated string value.

  * **Impact:** Finding notification filters, post-processing and alerting based on the finding source property will need to be updated to take advantage of the new data type for findings of the following categories: `AUDIT_CONFIG_NOT_MONITORED`, `BUCKET_IAM_NOT_MONITORED`, `CUSTOM_ROLE_NOT_MONITORED`, `FIREWALL_NOT_MONITORED`, `NETWORK_NOT_MONITORED`, `OWNER_NOT_MONITORED`, `ROUTE_NOT_MONITORED`, `SQL_INSTANCE_NOT_MONITORED`.
  * **Recommendation:** Update workflows to utilize the new data type.



Change

The `QualifiedLogMetricNames` source property in specific `Monitoring` findings from Security Health Analytics will use a list instead of a character-separated string value.

  * **Impact:** Finding notification filters, post-processing and alerting based on the finding source property will need to be updated to take advantage of the new data type for findings of the following categories: `AUDIT_CONFIG_NOT_MONITORED`, `BUCKET_IAM_NOT_MONITORED`, `CUSTOM_ROLE_NOT_MONITORED`, `FIREWALL_NOT_MONITORED`, `NETWORK_NOT_MONITORED`, `OWNER_NOT_MONITORED`, `ROUTE_NOT_MONITORED`, `SQL_INSTANCE_NOT_MONITORED`.
  * **Recommendation:** Update workflows to utilize the new data type.



## May 12, 2020

Feature

The Security Command Center Premium tier includes:

  * Security Health Analytics
  * Web Security Scanner managed scans
  * Event Threat Detection
  * Container Threat Detection



Learn more about the [Security Command Center Premium tier](https://docs.cloud.google.com/security-command-center/docs/concepts-security-command-center-overview).

Feature

Security Command Center Premium and Standard tiers are now available.

Deprecated

The Event Threat Detection API will be deprecated in the coming months. Similar functionality is available in the Security Command Center API settings feature.

Feature

Container Threat Detection currently supports the following Kubernetes Engine versions on the Regular and Rapid [channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels):

  * >= 1.15.9-gke.12
  * >= 1.16.5-gke.2
  * >= 1.17



In a future update, Container Threat Detection will support version 1.14 and the Stable channel.

## April 10, 2020

Feature

Security Health Analytics is now in general availability.

  * Learn about the [vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings) provided by Security Health Analytics.
  * [Get started with Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics).



## March 23, 2020

Feature

The Notifications API is now in general availability. [Get started with the notifications API](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications).

Change

The `eventType` field was removed from `organizations.notificationConfigs.create` in the v1 API. Learn more about [creating a `NotificationConfig`](https://docs.cloud.google.com/security-command-center/docs/how-to-api-manage-notifications#create-config).

## February 14, 2020

Change

Security Command Center roles inherit Web Security Scanner roles as follows:

  * The `securitycenter.adminViewer` role inherits the permissions of the `cloudsecurityscanner.viewer` role.
  * The `securitycenter.adminEditor` role inherits the permissions of the `cloudsecurityscanner.editor` role.



For information about how to view all of the permissions that are associated with a role, see the IAM documentation about [Getting the role metadata](https://docs.cloud.google.com/iam/docs/creating-custom-roles#getting_the_role_metadata).

## February 13, 2020

Feature

The notifications API is now in beta:

  * Send new findings and updated findings notifications to a Pub/Sub topic.
  * Filter notifications by provider source, finding type, category or any other finding fields, properties or security marks.



[Get started with the notifications API](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications).

Change

[Security Command Center tools](https://docs.cloud.google.com/security-command-center/docs/how-to-cloud-scc-tools) will become obsolete in future Security Command Center releases, when their functionalities are added as built-in features. Support is offered on best-effort basis only for all Security Command Center tools.

## November 11, 2019

Change

Cloud SCC now supports full JSON with arrays and JSON objects as potential property types. This includes support for sorting on JSON object sub-fields, and filtering on:

  * Array elements
  * Full JSON objects with partial string match
  * JSON object sub-fields



Learn more about [Filtering and sorting findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings#filtering_findings).

## October 14, 2019

Feature

Security Health Analytics is now in beta and can now be enabled in the Sources Management page of Cloud SCC.

Feature

A new Vulnerabilities tab in Cloud SCC displays a dashboard that summarizes Security Health Analytics findings. This dashboard includes information about CIS benchmarks and recommended remediations.

Change

Security Health Analytics no longer requires separate service account setup or permissions. Instead, it uses the Cloud SCC service account that's created for you during signup.

## August 20, 2019

Change

The following Security Health Analytics finding type names have changed:

Old Name | New Name  
---|---  
`LOGGING_DISABLED` | `CLUSTER_LOGGING_DISABLED`  
`MONITORING_DISABLED` | `CLUSTER_MONITORING_DISABLED`  
`NO_ROOT_PASSWORD` | `SQL_NO_ROOT_PASSWORD`  
`WEAK_ROOT_PASSWORD` | `SQL_WEAK_ROOT_PASSWORD`  
  
## August 05, 2019

Change

findingType string XSS_CALLBACK changed to XSS.

Feature

API updated to v1.

## May 10, 2019

Issue

Using VPC Service Controls currently blocks Cloud SCC asset discovery inside VPC Service perimeters for the following asset types:

  * Compute Engine 
    * Addresses
    * Routes
    * VPN Tunnels
  * Cloud Storage Buckets
  * GKE Clusters



This is expected to be fixed in a future release.

For information about troubleshooting access issues, see [VPC Service Controls Troubleshooting](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting). To work around the access to these assets, see [Granting access from the internet with access levels](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

## April 10, 2019

Feature

Cloud SCC is now in general availability (GA). These release notes include updated items from beta and new items for GA.

Fixed

`gcloud` command-line tool support for Cloud SCC is now available.

Fixed

There are now client libraries available for C#, Go, Java, Node.JS, PHP, Python, and Ruby.

Change

[GroupFindingsResponse](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings/group) now includes `totalSize`.

Change

`ListAssetResult` has changed.

  * [Beta](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta1/organizations.assets/list#ListAssetsResult)
  * [v1](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.assets/list#ListAssetsResult)



Fixed

Previously only active state findings were shown in the UI. You can now also choose to show inactive state findings.

Feature

Assets now include IAM information for organizations, projects, Compute Engine, Cloud Storage, and others where applicable. [IAM Policy information](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.assets/list#IamPolicy) can be searched, filtered, and joined with all other Asset information and Security Marks.

Feature

The Cloud SCC dashboard now enables you to select whether just active state findings are displayed or both active and inactive.

Feature

Additional security partner integrations through [Marketplace](https://console.cloud.google.com/marketplace/details/google-cloud-platform/cloud-security-command-center).

Feature

Native integration with [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-view-vulnerabilities-threats#etd) for log-based threat detection.

Feature

Native integration with [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics) for native managed vulnerability scanning.

Feature

The Cloud SCC dashboard now enables you to set active or inactive state for each finding.

Feature

Native integrations with [Phishing Protection](https://docs.cloud.google.com/security-command-center/docs/how-to-view-vulnerabilities-threats#phishing-protection).

Feature

`ListFindings` and `GroupFindings` now supports comparison between two points in time. For more information, see the [`compareDuration` parameter](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings/list).

Feature

You can now [export Cloud SCC data](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data) as filtered Asset or Findings data to the Cloud Storage bucket and project you select.

Feature

[Hello World example app](https://docs.cloud.google.com/security-command-center/docs/how-to-cloud-scc-tools) is expanded to include Cloud Functions functions for: removing bucket ACLs, deleting firewall rules, and creating a VM snapshot.

Feature

The Cloud SCC dashboard now enables you to perform a time-diff query for a fixed set of time periods.

Feature

New example apps are available for:

  * Integrations with Access Transparency Logs, Audit Logging, and Binary Authorization.
  * Connecting to Splunk.



For more information, see [Installing Cloud SCC tools](https://docs.cloud.google.com/security-command-center/docs/how-to-cloud-scc-tools).

Issue

After you've made an IAM policy change on an asset, the updated policy won't appear in Cloud SCC until it's re-scanned. To see current IAM policy before the daily re-scan, trigger an on-demand re-scan and then wait at least 10 minutes to see the updated IAM policies in Cloud SCC.

Issue

Sorting isn't supported for source properties and security marks on the findings changed page.

Issue

Sorting on Asset ID column on the asset page doesn't work as expected.

Issue

After you've created a new asset, the new asset won't appear in Cloud SCC until it's re-scanned. To see current asset state before the daily re-scan, trigger an on-demand re-scan and then wait at least 5 minutes to see the new asset appear in Cloud SCC.

Issue

Code examples are still in progress for C#, Node.js, PHP, and Ruby.

Issue

Sorting on the following findings page columns doesn't work as expected:

  * `eventTime`
  * `source property`
  * `security mark`
  * `id`
  * `externalUri`



## March 26, 2019

Issue

Web Security Scanner does not yet support applications protected by Cloud Identity-Aware Proxy (Cloud IAP).

Feature

API updated to v1beta.

Change

findingType field changed to string value

The findingType field has changed from an enum to a string in the Beta release of the Web Security Scanner API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
