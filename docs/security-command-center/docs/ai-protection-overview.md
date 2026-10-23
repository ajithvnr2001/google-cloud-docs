---
url: https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview/
title: AI Protection overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:57.977060+00:00
---

# AI Protection overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  AI Protection overview Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

AI Protection helps you manage the security posture of your AI workloads by providing a view of AI security across your Google Cloud environment, and helping you to detect threats and mitigate risks to your AI inventory. This document provides an overview of AI Protection that includes its benefits and several key concepts.

AI Protection is available with organization-level and project-level activations of Security Command Center.

When you activate Security Command Center at the organization level, the **AI Security** dashboard and **AI Security** views in console pages display data that is aggregated from all projects and resources within the organization.

When you activate Security Command Center at the project level, the **AI Security** dashboard and views on console pages display data that is related to resources in the selected project.

## Capabilities of AI Protection

AI Protection helps you manage threats and risks to components in your AI systems. Your service tier determines the available capabilities, which include the following:

  * **Assess your AI asset inventory** : understand your AI systems and assets.
  * **Identify vulnerabilities** (Premium and Enterprise (Deprecated) service tiers): identify software vulnerabilities (CVEs) and plaintext secrets in agentic workloads deployed with Agent Runtime.
  * **Identify risks** (Premium and Enterprise (Deprecated) service tiers): identify risks and their impact on the ecosystem based on Attack Path Simulation and predefined security graph rules, with agents and MCP servers as high-value resources.
  * **Detect over-privileged agents** : detect Agent Runtime agents that are granted excessive permissions.
  * **Manage compliance** : proactively verify that AI assets in your deployments adhere to relevant security standards. The Standard service tier includes baseline security findings with [Security Essentials](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials), while Premium and Enterprise service tiers include advanced framework compliance.
  * **Detect and manage threats** : detect and respond to potential threats to your AI systems and assets in a timely manner.



## Use cases for AI Protection

AI Protection helps organizations enhance their security by identifying and mitigating threats and risks related to AI systems and sensitive data. The following use cases are examples of how AI Protection can be used in different organizations:

  * **Financial services institution: customer financial data**

A large financial services institution uses AI models that process sensitive financial data.

    * **Challenge:** processing highly sensitive financial data with AI models entails several risks, including the risk of data breaches, data exfiltration during training or inference, and vulnerabilities in the underlying AI infrastructure.
    * **Use case:** AI Protection continuously monitors AI workflows for suspicious activity, works to detect unauthorized data access and anomalous model behavior, performs sensitive data classification, and aids in improving your compliance with regulations such as PCI DSS and GDPR.
  * **Healthcare provider: patient privacy and compliance**

A major healthcare provider manages electronic health records and uses AI for diagnostics and treatment planning, dealing with Protected Health Information (PHI).

    * **Challenge:** PHI analyzed by AI models is subject to strict regulations like HIPAA. Risks include accidental PHI exposure through misconfigurations or malicious attacks that target AI systems for patient data.
    * **Use case:** AI Protection identifies and alerts on potential HIPAA violations, detects unauthorized PHI access by models or users, flags vulnerable and potentially misconfigured AI services, and monitors for data leakage.
  * **Manufacturing and robotics company: proprietary intellectual property**

A manufacturing company specializing in advanced robotics and automation relies heavily on AI for optimizing production lines and robotic control, with vital intellectual property (IP) embedded within its AI algorithms and manufacturing data.

    * **Challenge:** proprietary AI algorithms and sensitive operational data are vulnerable to theft from insider threats or external adversaries, potentially leading to competitive disadvantage or operational disruption.
    * **Use case:** AI Protection monitors for unauthorized access to AI models and code repositories, detects attempts to exfiltrate trained models and unusual data access patterns, and flags vulnerabilities in AI development environments to prevent IP theft.



## Detection services in AI Protection

The following section describes rules and detection services that create findings when you enable AI Protection. Both the Security Command Center service tier and activation scope (organization-level or project-level) determine which detection services Security Command Center supports and the findings that are created. Security Command Center automatically enables some detection services, but you must manually configure others. For more information, see [Configure AI Protection](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection).

### AI Discovery service

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

This is a built-in service that uses Cloud Monitoring data to discover AI models and determine whether Model Armor protects models. On the Standard service tier, AI Discovery doesn't support the detection of [Gemini](https://docs.cloud.google.com/gemini/docs/overview) models.

For information about findings that this service creates, see [AI Discovery service findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#aip-ds-findings).

### Compliance Manager frameworks

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

AI Protection uses Compliance Manager frameworks that Security Command Center deploys automatically in [detective mode](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#cm-scan-types).

#### Compliance Manager built-in frameworks

AI Protection includes the following frameworks. When you enable AI Protection, Security Command Center automatically enables these frameworks in your organization or project.

  * [Security Essentials framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials) is available on the Standard, Premium, and Enterprise service tiers.

  * [Google Recommended AI Essentials - Gemini Enterprise Agent Platform](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#aipp) is available on Premium and Enterprise service tiers.




Depending on your service tier, you can configure additional Compliance Manager [frameworks and cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#built-in-frameworks). For more information about Compliance Manager, see [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview).

#### Compliance Manager custom frameworks

You can create custom frameworks by making copies of built-in frameworks available on your service tier.

  * **Customization:** you can add or remove cloud controls in your custom frameworks to match your security policies.
  * **Targeted application:** you can apply custom frameworks to specific organizations, folders, or projects. For example, you can apply specific jurisdictional controls to specific folders to ensure that data remains within a particular geographical region.
  * **Limitation:** you cannot assign AI Protection frameworks to applications.



### Event Threat Detection rules for Gemini Enterprise Agent Platform assets

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Event Threat Detection detects several potential threats involving Gemini Enterprise Agent Platform assets, such as anomalous service account activity, sensitive permission changes, and agentic identity abuse.

Finding categories that apply to AI assets include the following:

  * **Persistence** : New AI API Method
  * **Persistence** : New Geography for AI Service
  * **Privilege Escalation** : Anomalous Impersonation of Service Account for AI Admin Activity
  * **Privilege Escalation** : Anomalous Service Account Impersonator for AI Data Access
  * **Privilege Escalation** : Anomalous Multistep Service Account Delegation for AI Admin Activity
  * **Privilege Escalation** : Anomalous Multistep Service Account Delegation for AI Data Access
  * **Privilege Escalation** : Anomalous Service Account Impersonator for AI Admin Activity
  * **Initial Access** : Dormant Service Account Activity in AI Service
  * **Persistence** : IAM Anomalous Grant to Agentic Identity
  * **Credential Access** : Agentic Identity Credential Used Outside of Google Cloud
  * **Persistence** : Sensitive AI Permission Added to Custom Role
  * **Persistence** : Sensitive Role Granted by AI Agent
  * **Persistence** : Sensitive Role Granted to External AI Agent
  * **Defense Evasion** : Project Level Token Creator Role Granted to AI Agent
  * **Defense Evasion** : Folder Level Token Creator Role Granted to AI Agent
  * **Defense Evasion** : Organization Level Token Creator Role Granted to AI Agent



For a full list of Event Threat Detection findings that apply to AI assets, see [Overview of Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).

### Agent Platform Threat Detection for Agent Runtime

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Agent Platform Threat Detection ([Preview](https://cloud.google.com/products/#product-launch-stages)) provides runtime threat detection for agents deployed to Agent Runtime. It monitors running agents for potential attacks and generates findings in Security Command Center.

Agent Platform Threat Detection generates findings for Agent Runtime, including the following categories:

  * **Command and Control** : Steganography Tool Detected
  * **Credential Access** : Find Google Cloud Credentials
  * **Credential Access** : GPG Key Reconnaissance
  * **Credential Access** : Search Private Keys or Passwords
  * **Defense Evasion** : Base64 ELF File Command Line
  * **Defense Evasion** : Base64 Encoded Python Script Executed
  * **Defense Evasion** : Base64 Encoded Shell Script Executed
  * **Defense Evasion** : Launch Code Compiler Tool In Container
  * **Execution** : Netcat Remote Code Execution in Container
  * **Execution** : Possible Arbitrary Command Execution through CUPS (CVE-2024-47177)
  * **Execution** : Possible Remote Command Execution Detected
  * **Execution** : Program Run with Disallowed HTTP Proxy Env
  * **Execution** : Socat Reverse Shell Detected
  * **Execution** : Suspicious OpenSSL Shared Object Loaded
  * **Exfiltration** : Launch Remote File Copy Tools in Container
  * **Impact** : Detect Malicious Cmdlines
  * **Impact** : Remove Bulk Data from Disk
  * **Impact** : Suspicious crypto mining activity using the Stratum Protocol
  * **Privilege Escalation** : Abuse of Sudo For Privilege Escalation (CVE-2019-14287)
  * **Privilege Escalation** : Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)
  * **Privilege Escalation** : Sudo Potential Privilege Escalation (CVE-2021-3156)
  * **Execution** : Malicious Python executed
  * **Execution** : Container Escape
  * **Execution** : Kubernetes Attack Tool Execution
  * **Execution** : Local Reconnaissance Tool Execution
  * **Impact** : Malicious Script Executed
  * **Impact** : Malicious URL Observed
  * **Execution** : Unexpected Child Shell



Learn more about [Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-platform-threat-detection-overview).

### Agent Platform Vulnerability Assessment

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Agent Platform Vulnerability Assessment ([Preview](https://cloud.google.com/products/#product-launch-stages)) identifies vulnerabilities and plaintext secrets, such as credentials, keys, access tokens, or certificates, in Gemini Enterprise Agent Platform container images.

For more information, see [Agent Platform Vulnerability Assessment](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#aevs) in "Detection Services".

### Notebook Security Scanner

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Notebook Security Scanner ([Preview](https://cloud.google.com/products/#product-launch-stages)) scans Colab Enterprise notebooks to detect vulnerabilities in Python packages.

For information, see [Notebook Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#notebook-security-scanner) in "Detection Services".

### Sensitive Data Protection

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The Sensitive Data Protection discovery service is a fully managed Google Cloud service that helps you discover, classify, and protect your sensitive data. You can use Sensitive Data Protection to determine whether you're storing sensitive or personally identifiable information (PII).

For more information, see [Sensitive Data Protection findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#dlp) in "Detection Services".

### Model Armor

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

After you enable Model Armor and [configure Model Armor](https://docs.cloud.google.com/model-armor/integrations) to integrate with one or more AI-related components, you can investigate Model Armor findings in Security Command Center.

On the Security Command Center Standard service tier, AI Protection doesn't support [Gemini](https://docs.cloud.google.com/gemini/docs/overview) models.

To configure Model Armor, see [Create and manage templates](https://docs.cloud.google.com/model-armor/manage-templates).

### Risk Engine

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Risk Engine is a feature in Security Command Center that assesses the risk exposure of your cloud deployments, assigns attack exposure scores to vulnerability findings and your high-value resources, and diagrams paths that a potential attacker could take to reach your high-value resources.

For more information, see [Risk Engine](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#risk-engine) in "Detection Services".

## Supported resources in AI Protection

AI Protection discovers assets using the following mechanisms:

  * Declarative AI assets: assets that AI lifecycle management tools (such as Gemini Enterprise Agent Platform) track.
  * Inferred AI assets: general-purpose assets (such as compute and storage assets) that process AI data or workloads.
  * Model-as-a-Service (API only): assets that make programmatic calls into first-party or third-party AI models.



This section defines supported AI inventory and assets that AI Protection can help secure.

  * **Gemini Enterprise & Agent search apps**: these are AI systems that can perceive their environment, make decisions, and take actions to achieve specific goals.
  * **Endpoints** : AI application workloads range from internal tools aimed at improving employee productivity to consumer-facing solutions designed to enhance the user experience and drive business. Examples include AI agents, virtual assistants, conversational AI chatbots, and personalized recommendations. AI Protection identifies these as **Agent Platform endpoints** in the **AI resources** tab on the **Assets page**.
  * **Data sources** : supported data sources include BigQuery tables, Cloud Storage, Agent Platform datasets, and Gemini Enterprise datastores.
  * **Models** : AI Protection identifies AI models as foundation AI models, fine-tuned AI models, standard first-party AI models, and custom AI models. Examples include the following: 
    * [Gemini](https://docs.cloud.google.com/gemini/docs/overview) (available on Premium and Enterprise (Deprecated) service tiers)
    * [Llama](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/llama)
    * [translation models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/translate/translate-text)
    * Custom models for specific tasks
  * **AI assets** : AI assets contribute to machine learning operation pipelines and are used by AI workloads. Types of AI assets include the following:
  * **Model Context Protocol (MCP) servers** : AI Protection identifies MCP servers that are cataloged in [Agent Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry). To use this feature, you must [configure App Hub API](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection#configure-app-hub) in each project that hosts an MCP server.



## Impacts from service tier changes

If you downgrade the service tier from Premium or Enterprise to Standard, the downgrade affects your AI Protection capabilities as follows:

  * **Detection services** : Security Command Center disables detection services and Compliance Manager frameworks that the Standard tier doesn't support. For more information, see [Manage service tiers in Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-enable#manage-service-tiers).
  * **Investigative features** : you lose access to advanced investigative features, such as attack path simulations for AI assets, agent vulnerability assessment, and detection of over-privileged agents.
  * **Findings become inactive:** findings created by Compliance Manager frameworks that are not supported on the Standard tier become inactive. For more information, see [Manage service tiers in Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-enable#manage-service-tiers).



If you upgrade back to the Premium or Enterprise tier, Security Command Center restores the advanced features, but doesn't automatically recover any framework deployments that were removed during the downgrade. You must manually redeploy the frameworks.

## What's next

  * [Configure AI Protection](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection)
  * [Review AI security](https://docs.cloud.google.com/security-command-center/docs/review-ai-security)
  * [Assess risk using dashboard data](https://docs.cloud.google.com/security-command-center/docs/assess-risk#ai-protection)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
