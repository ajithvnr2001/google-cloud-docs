---
url: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview/
title: Compliance Manager overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:52.145195+00:00
---

# Compliance Manager overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Compliance Manager overview Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

You can use Compliance Manager in Google Cloud to help ensure that your Google Cloud infrastructure, workloads, and data meet the security and regulatory requirements of your organization or project. Compliance Manager lets you do the following:

  * Define and deploy a compliant and secure configuration for your Google Cloud environment.
  * View dashboards that show your environment's alignment with your compliance and security requirements.
  * (Premium and Enterprise tiers only) Audit your cloud environments, including collecting evidence and generating reports.

**Note:** You can enable Compliance Manager for individual projects in your Google Cloud environment, regardless of the parent organization's settings.

Compliance Manager uses software-defined controls that let you assess support for multiple compliance programs and security requirements within a Google Cloud organization or project.

## Compliance Manager components

The following table describes the components of Compliance Manager.

Rule | A technical item within a cloud control that lets you meet a compliance, security, or privacy requirement. Rules can be organization policies, IAM policies, cloud settings, and detection logic based on [Common Expression Language (CEL)](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-write-cel-expressions).   
---|---  
Cloud control | A set of rules and associated metadata that you can use to define the security or compliance intent for your organization or project. Compliance Manager includes a library of built-in cloud controls and lets you create your own. The metadata in a cloud control includes remediation instructions and finding severity. Cloud controls have the following modes:

  * **Detective:** Compliance Manager applies the cloud control to the defined resources for monitoring purposes. Any violations are detected and alerts are generated. No preventive actions are taken automatically. Some cloud controls require that you provide additional information so that they can work. For example, if you want to use a cloud control that checks whether your workloads and resources are running in particular regions, you must specify the permitted regions when you create the cloud control.
  * (Premium and Enterprise tiers only) **Audit:** Compliance Manager uses this cloud control to [ audit your environment](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit) for alignment with your compliance obligations. Compliance Manager uses this control to gather evidence for compliance audits and identify any gaps.

  
Regulatory control | An industry-defined security or regulatory compliance requirement. The relationship mapping between cloud controls and regulatory controls defines how one or more cloud controls satisfy a regulatory control requirement. Consider the following:

  * A single cloud control can map to multiple regulatory controls.
  * A single regulatory control can map to multiple cloud controls.

  
Framework | A collection of cloud controls and regulatory controls that represent security best practices or industry-defined standards such as FedRAMP or NIST. A framework can include a mapping between cloud controls and the regulatory controls. Compliance Manager includes a library of built-in frameworks. You can customize these frameworks or create your own. **Note:** The Standard tier supports only the [Security Essentials](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials) framework. Other built-in frameworks require [Premium or Enterprise](https://docs.cloud.google.com/security-command-center/docs/service-tiers) tiers. For more information, see [Frameworks for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#frameworks-gcp).   
Framework deployment | The binding between a particular framework and an organization, folder, or project when you deploy the framework.   
  
The following diagram shows the components of Compliance Manager.

![Compliance Manager components.](https://docs.cloud.google.com/static/security-command-center/images/compliance-terminology.svg)

## Built-in frameworks

Compliance Manager supports built-in frameworks for Google Cloud. You can deploy these frameworks as-is, or you can customize them to meet your particular needs.

The [Security Essentials](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials) framework is available for all Security Command Center tiers.

The following frameworks are available in the Premium and Enterprise tiers only:

  * [Google Recommended AI Essentials - Gemini Enterprise Agent Platform](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#aipp)
  * [Center for Information Security (CIS) Controls 8.0](https://www.cisecurity.org/controls/v8)
  * [CIS Google Cloud Computing Platform Benchmark v3.0](https://www.cisecurity.org/benchmark/google_cloud_computing_platform/)
  * [CIS Kubernetes Benchmark v1.1.7](https://www.cisecurity.org/benchmark/kubernetes)
  * [Cloud Controls Matrix (CCM) 4](https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4)
  * [Data Security and Privacy Essentials](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-security-framework)
  * [Data Security Framework Template](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#data-security-framework-template)
  * [FedRAMP Low](https://www.fedramp.gov)
  * [International Organization for Standardization (ISO) 27001, 2022](https://www.iso.org/standard/27001)
  * [National Institute of Standards and Technology (NIST) SP 800-53 R5](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_1/home)
  * [NIST AI 600-1 Privacy Controls](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
  * [NIST Cybersecurity Framework (CSF) 1.1](https://www.nist.gov/cyberframework/getting-started-csf-11)
  * [Payment Card Industry Data Security Standard (PCI DSS) 4.0](https://www.pcisecuritystandards.org/document_library)
  * [Qatar National Information Assurance Standard 2.1](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#nias-v2-1)
  * [System and Organization Controls (SOC) 2](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)



## Compliance Manager scan types for detective controls

Compliance Manager scans run in two modes:

  * **Batch scan:** All detective cloud controls are scheduled to run for all enrolled organizations or projects periodically.

For information about the frequency of scans, see Compliance Manager scan latency.

  * **Near-real-time scan:** In the Premium tier only, supported detective cloud controls start scans whenever a change is detected in a resource's configuration.




For a list of cloud controls that don't support near-real-time scans, see [Cloud controls that support batch scanning only](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-batch-scan-support).

### Compliance Manager scan latency for detective controls

The following sections describe the amount of time before findings are generated by the initial scan and the frequency of subsequent scans for detective cloud controls that are deployed in your environment.

**Note:** Batch scan schedules are performance objectives, not service guarantees.

### Initial scan

For the Premium and Enterprise tiers, the initial batch scan starts approximately one hour after activation. The first Compliance Manager scans can take up to 48 hours to complete.

For the Security Command Center Standard tier, batch scans run every 96 hours, which can result in an initial finding latency of 96 hours.

After you deploy a framework, it can take up to 6 hours before findings related to detective cloud controls appear.

You might see some findings in the Google Cloud console while initial scans are taking place but before the onboarding process is complete. Preliminary findings are accurate and actionable, but they are not comprehensive. Starting an audit in the Premium or Enterprise tier within the first 48 hours is not recommended.

### Subsequent scans

After the initial scan, subsequent batch scans run periodically, as follows:

  * For the Premium and Enterprise tiers, batch scans run every 16 hours.
  * For the Standard tier, batch scans run every 38 hours.



With near-real-time scanning, relevant Google Cloud resource configuration changes might result in updated findings. The update might take several minutes, depending on the asset type and the change.

### Latency on monitoring dashboards

Compliance Manager includes [monitoring dashboards](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-monitor-framework) that aggregate data about compliance levels. After a finding appears on the **Findings** dashboard, it can take up to 24 hours for that finding to affect the compliance counts on the monitoring dashboards. In addition, asset changes (such as creation or updates) can take up to 48 hours to appear on the monitoring dashboards.

## Using Compliance Manager with Security Command Center services and features

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

You can enable other Security Command Center services and features and use them in the same organization or project where you enable Compliance Manager. Consider the following:

  * Most Security Health Analytics detectors are also available as cloud controls in Compliance Manager. For more information, see [Mapping of Security Health Analytics detectors to cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls#mapping-sha-cloud-control).

  * Most Security Health Analytics detectors are turned on by default. When you [enable Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-enable#enable-compliance-manager), certain built-in frameworks are automatically applied to your Google Cloud organization. You can deploy additional frameworks with more cloud controls as required.

  * You can [disable Security Health Analytics detectors](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#enable_and_disable_detectors). To disable a cloud control, you must [remove the cloud control from the custom frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#update-custom-framework) that include it or [unassign the deployed built-in framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#remove-resource-assignments).

  * Both Security Health Analytics and Compliance Manager generate findings. However, Security Health Analytics uses the [`securitycenter.googleapis.com` API](https://docs.cloud.google.com/security-command-center/docs/reference/rest) to generate findings, and Compliance Manager uses the [`cloudsecuritycompliance.googleapis.com` API](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest). If you enable Security Health Analytics and Compliance Manager on the same resource, you might generate duplicate findings. Duplicate findings occur when both a Security Health Analytics detector and a Compliance Manager cloud control check for the same configuration (for example, both check whether CMEK is enabled for a particular service.) In the findings dashboard, the duplicate findings display with different provider IDs. To avoid duplicate findings, complete one of the following:

    * If the frameworks that you've deployed include cloud controls that map to all the Security Health Analytics detectors that apply to your environment, [disable Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) for the project or folder.

    * If the frameworks don't include the required Security Health Analytics detectors, [mute the duplicate Security Health Analytics detector findings](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

  * If you deployed a security posture using the security posture service, you might receive duplicate findings when you enable Compliance Manager. Consider deploying a framework that matches your security posture and [delete the posture deployment](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#delete-posture-deployment).

  * Compliance Manager uses the global endpoint, not the endpoint that you might specify when you enable [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) for Security Command Center. However, you can specify the location that you want to audit your environment in. For more information, see [Audit your environment with Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit).




## What's next

  * [Enable Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-enable).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
