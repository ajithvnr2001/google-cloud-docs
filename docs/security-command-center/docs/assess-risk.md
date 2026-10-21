---
url: https://docs.cloud.google.com/security-command-center/docs/assess-risk/
title: Assess risk using Risk overview dashboards \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:44.052798+00:00
---

# Assess risk using Risk overview dashboards  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/assess-risk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Assess risk using Risk overview dashboards Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

The **Risk** section in the Google Cloud console helps you to manage the highest profile risks in your cloud environment.

The **Overview** page serves as your first contact security dashboard, highlighting the highest priority risks in your cloud environments. You can view multiple domains in **Overview** by selecting one of the following views:

  * All risk
  * Vulnerabilities
  * Identity
  * Data
  * AI security
  * External attack surface
  * Threats



If Security Command Center was recently activated, it might take time for data to appear. For information about the scan frequency of Security Command Center services, see [When to expect findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview). 

## All risk dashboard

The **All risk** dashboard surfaces the following high-priority security risks across your cloud environments:

###  Standard-legacy 

  * **Misconfigurations by date** : shows the number of misconfiguration findings over time.
  * **Top misconfigurations** : summarizes the misconfiguration findings by resource type, category, and project (when viewing data for an organization).
  * **Critical CVEs** : summarizes the CVEs in vulnerability findings identified as having critical impact.



### Standard

  * **Misconfigurations by date** : shows the number of misconfiguration findings over time.
  * **Top misconfigurations** : summarizes the misconfiguration findings by resource type, category, and project (when viewing data for an organization).
  * **Critical CVEs** : summarizes the CVEs in vulnerability findings identified as having critical impact.
  * **Compliance** : summarizes the passing cloud controls in applied Compliance Manager frameworks and the number of active findings.



The **Misconfigurations by date** and **Top misconfigurations** panels include data about Security Health Analytics findings that don't have the `launch_state="LAUNCH_STATE_DEPRECATED"` field-value identifier.

### Premium and Enterprise

  * **Riskiest issues** shows at-a-glance information for your top [issues](https://docs.cloud.google.com/security-command-center/docs/issues-overview), including simplified attack paths, evidence diagrams, or threat findings that are combined together as [Correlated Threats](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview) ([Preview](https://cloud.google.com/products/#product-launch-stages)). This panel isn't available with project-level activations.

  * **Recent Google Cloud threats** that are active in your cloud environments.

  * **High-impact, exploitable vulnerabilities** , prioritized by the resources impacted by them.

  * **Compliance** : The dashboard also displays your progress in **Compliance**. For standards such as NIST, HIPAA, PCI DSS, and CIS, progress is reported as a percentage of how many controls are passing.




In most cases, you can interact with individual high-priority risks for a brief summary, continue on to a more detailed view of each risk, or view all risks of a specific type.

### View application-related information on the All risk dashboard

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

When viewing the **All risk** dashboard for an organization or project, you can also see information about the [application](https://docs.cloud.google.com/application-design-center/docs/application-centric-google-cloud) if the primary resource in the issue or finding is part of an application in App Hub or Application Design Center.

The **Select app** menu lets you display only issues and findings where the primary resource is registered in the application that you selected. If **None** is selected, the dashboard displays issues for all resources, including those that are related to an application and those that aren't related.

In the **Riskiest issues** panel, an issue displays the application name if the primary resource in the issue is defined in an application.

### View issues in the folder or project on the All risk dashboard

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Issues created by security graph rules and Correlated Threats appear in the folder and project level of the **All risk** dashboard.

Toxic combinations and chokepoints created by Risk Engine only appear in the organization level. For more information, see [Issues overview](https://docs.cloud.google.com/security-command-center/docs/issues-overview).

The selected level determines which dashboard panels are displayed. Some panels aren't supported at the folder and project level.

## Vulnerabilities dashboard

The **Vulnerabilities** dashboard gives insights into virtual machines and containers with exploitable vulnerabilities across your cloud environments. The dashboard displays the following information:

  * **Top common vulnerabilities and exploits**. Displays a clickable quadrant heatmap to help you filter vulnerabilities by exploitability and impact. The number of unique resources that are affected and the findings related to those resources are shown in a table after the heatmap. Each unique resource might have more than one finding. You can click a heatmap cell again to reset the heatmap.

  * **Most common critical exploitable vulnerabilities**. A list of highly exploitable vulnerabilities found in your cloud environments, prioritized by the total number of unique resources impacted by them.

Vulnerability findings are grouped in an interactive chart by the exploitability and impact of the corresponding CVE, as assessed by Mandiant. Click a block in the chart to see a list of vulnerabilities by CVE ID that have been detected in your environment.

Expand a CVE section to view its descriptions, which are findings related to the CVE and the resources they affect. Because different findings can affect the same resource, the sum of all resource counts in the expanded description might be greater than the unique resource count in the heading row.

  * **Containers with exploitable vulnerabilities**. A list of containers with exploitable vulnerabilities, where the vulnerability [exploitation activity](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#exploitationactivity) rating is `available`, `confirmed`, or `wide` and the [risk rating](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#Finding.RiskRating) is `critical`, based on the assessment of Google Threat Intelligence. The list is ordered by [attack exposure score](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn), then by the largest number of impacted resources.

  * **Latest compute vulnerabilities with known exploits**. A list of Compute Engine virtual machine instances that have exploitable vulnerabilities with findings that belong to the `OS_VULNERABILITY` or `SOFTWARE_VULNERABILITY` category.

From here, you can check the following:

    * The attack exposure score of the exploit. Click the score to view the attack paths to your exposed [high-value resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#high-value_resources). 
      * How many [configured high-value resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#resource-value-configurations) have been exposed due to the vulnerability that have a [priority](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-manual) of `HIGH`, `MEDIUM`, or `LOW`.
      * The **Exploit release date** , which is when the vulnerability was announced.
      * The **First available date** , which is when an exploit was first observed.
      * The [level of exploitability](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#exploitationactivity) of the vulnerability.



## Data dashboard

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

The **Data** dashboard in the Google Cloud console lets you see how your organization's data aligns with your data security and compliance requirements. For more information, see [Data Security Posture Management overview](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security).

The dashboard displays the following information:

###  Standard 

  * **Data security compliance** summarizes the failing data cloud controls, the number of data security findings, and the top data security findings.
  * **Learn about data security** provides a video and links to more information about how to protect your digital information from unauthorized access, use, disclosure, alteration, or destruction.
  * **Data Map Explorer** shows the geographic locations where your data is stored and lets you filter information about your data by geographic location, how sensitive the data is, the associated project, and which Google Cloud services store the data. The circles on the data map represent the relative count of data resources and data resources with alerts in the region.
  * **Resources** table summarizes findings by resource and includes the display name, resource type, location, number of findings, and project ID that the resource belongs to.



###  Premium and Enterprise 

  * **Top data security findings** lists the number of findings by finding category and severity.
  * **Top data frameworks with open findings** lists frameworks with the most findings.
  * **Data Map Explorer** shows the geographic locations where your data is stored and lets you filter information about your data by geographic location.
  * **Resources** table summarizes findings by resource and includes the display name, resource type, location, number of findings, and project ID that the resource belongs to.
  * **Quick Filters** panel lets you filter data in the **Resources** table.



### View application-related information on the Data dashboard

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

When viewing the **Data** dashboard for an organization, you can view issues related to a specific [App Hub application](https://docs.cloud.google.com/application-design-center/docs/application-centric-google-cloud) if the primary resource in the issue is registered in an application.

The **Select app** menu lets you display only issues where the primary resource is registered in the application that you selected. If **None** is selected, the dashboard displays issues for all resources, including those that are related to an application and those that aren't related.

## AI Security dashboard

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The **AI Security** dashboard provides a high-level view of your AI security posture.

Your Security Command Center service tier determines the features available on the **AI Security** dashboard. For information about features in each service tier, see [AI Protection overview](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview).

The dashboard displays the following sections:

  * **AI Inventory** : use the AI Security dashboard for an organization-wide or project-wide view of your AI systems and assets, categorized into the following tabs: 
    * **Gemini Enterprise & Agent search apps**: monitor discovered AI agents that are cataloged in Agent Registry, which includes Gemini Enterprise apps and agents that are deployed to [Gemini Enterprise Agent Platform Runtime](https://docs.cloud.google.com/agent-builder/agent-engine/overview). Each listed agent has a detailed view page that shows you any findings, change history, Identity and Access Management (IAM) policies, and metadata for that agent. Available for Standard, Premium, and Enterprise (Deprecated) service tiers (limited capabilities in the Standard tier).
    * **MCP servers** : monitor Model Context Protocol (MCP) servers that are cataloged in Agent Registry as resources. To discover MCP servers, you must enable the App Hub API (`apphub.googleapis.com`) in each project that hosts an MCP server. Available for Standard, Premium, and Enterprise (Deprecated) service tiers (limited capabilities in the Standard tier).
    * **Models** : review AI models that are used in your organization or project, including Gemini models and custom-built models. Gemini models are available for Premium and Enterprise (Deprecated) service tiers.
    * **Data sources** : view data source counts, including Gemini, that are used in training or fine-tuning the AI models. If Sensitive Data Protection is enabled, the dashboard shows whether data sources contain sensitive data.
    * **Endpoints** : track the endpoints where your AI models are hosted. Available for Standard, Premium, and Enterprise (Deprecated) service tiers (limited capabilities in the Standard tier).
For each category tab, you can click links to open the associated AI resource on the [AI resources tab](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console#quick-filters-secops-console) of the **Assets** page. 
  * **Riskiest AI Issues** : view top risks in your AI inventory, prioritized by the highest [attack exposure scores](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn). For each issue, you can view attack paths that help you visualize relationships between AI resources in your environment. Each listed issue provides an explanation of the risk, its impact, and step-by-step remediation guidance. Click an issue to view its [issue details](https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate#view). Available for Premium and Enterprise (Deprecated) service tiers.
  * **Recent AI Threats** : review the most recent critical and high threat findings that are associated with your AI resources. These detections cover suspicious activities such as prompt injection, model theft, or unauthorized data access. Available for Premium and Enterprise (Deprecated) service tiers.
  * **Findings** : assess and manage your overall security posture and adherence to security policies. This widget breaks up findings into two categories: 
    * **AI Vulnerabilities & misconfigurations**: track and identify common vulnerabilities and misconfigurations in findings across your AI workloads, such as critical software vulnerabilities (CVEs) in Reasoning Engine container images, package vulnerability findings for notebooks, exposed API keys, insecure model configurations, or over-privileged service accounts. **Note:** Standard tier users can view a limited subset of these findings. 
    * **AI Framework: Google Recommended AI Essentials - Gemini Enterprise Agent Platform** : view the percentage of adherence to Google Recommended AI Essentials best practices, including controls that help improve the security posture of your AI workloads. Available for Premium and Enterprise (Deprecated) service tiers. 
Click a finding to view its [finding details](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#finding-details). 
  * **Gemini models secured with Model Armor** : view the security status of your Gemini models as monitored by Model Armor. This widget shows models that are protected by Model Armor floor settings. It helps you understand how well your models are protected against common AI threats by showing the volume and types of issues filtered out by Model Armor. For more information, see the [Model Armor overview](https://docs.cloud.google.com/model-armor/overview). Available for Premium and Enterprise (Deprecated) service tiers.
  * **Violations** : monitor and manage policy violations across your AI environment. This widget lists recent violations of Model Armor floor settings and templates, and provides tools to investigate and resolve them. Violations are categorized into the following tabs: 
    * **All** : show violations for resources that are protected by Model Armor templates and floor settings.
    * **Gemini Enterprise** : show violations for resources that are protected by Model Armor templates only.
    * **Agent gateways** : show violations for resources that are protected by Model Armor templates only.
    * **Gemini models** : show violations for resources that are protected by Model Armor floor settings only.
    * **MCP servers** : show violations for resources that are protected by Model Armor floor settings only.
An interaction is a single request that is analyzed by Model Armor and one interaction can have multiple violations. If you are using Model Armor templates to protect models, this widget might show violations even if the **Gemini models secured with Model Armor** widget shows that no models are protected by floor settings. **Note:**
    * For agentic workloads, Model Armor can be configured on Agent Gateway to screen prompts and responses to and from agents.
    * If Model Armor isn't configured in your organization or project, or if a template isn't created, the Model Armor widgets in the AI Security dashboard won't show any data. For configuration steps, see [Configure Model Armor](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection#configure-model).



## External Exposure dashboard

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **External Exposure** dashboard helps identify resources that are reachable from the public internet across your cloud environments. The dashboard displays the following information:

  * **What was scanned** : Summarizes active scan metrics, including **Last scan** , **Next scan** , **Successful projects** , **Projects excluded** , **Exposed resources** , and **Exposed public ports**.
  * **External exposure findings** : Displays a table summarizing active findings grouped by finding category and severity.



For a detailed breakdown of finding attributes, active scanners, and scan metrics, see [Detect exposed resources](https://docs.cloud.google.com/security-command-center/docs/detect-external-exposure).

## Identity dashboard

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The **Identity** dashboard shows misconfiguration findings related to principal accounts (_identities_) that are misconfigured or are granted excessive or sensitive permissions.

## Threats dashboard

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The **Threats** dashboard helps you review potentially harmful events in your Google Cloud resources in the past seven days. You can view findings in the following panels:

  * **New threats over time** shows potentially harmful events in your resources over a time period that you specify. The default time period is seven days. Specify the time period to display threats for by using the **Time range** field.

  * **Top Threats** shows the following:

    * **Threats by severity** shows the number of threats in each severity level.
    * **Threats by category** shows the number of findings in each category across all projects.
  * **Threats by project** panel shows the number of findings for each project in your organization.




## What's next

  * Learn how to [Review and manage findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).

  * Learn more about [services that generate findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
