---
url: https://docs.cloud.google.com/security-command-center/docs/service-tiers/
title: Security Command Center service tiers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:42.184200+00:00
---

# Security Command Center service tiers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/service-tiers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Security Command Center service tiers Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Security Command Center is offered in three service tiers: Standard, Premium, and Enterprise. Each tier determines the features and services that are available to you in Security Command Center. A short description of each service tier follows:

  * **Standard-legacy**. Supports basic security and compliance posture management for Google Cloud only. The Standard-legacy tier might be [migrated to the Standard tier](https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy) in some organizations.
  * **Standard**. Supports basic security and compliance posture management for Google Cloud only. The Standard tier can be activated at the organization level. Best for Google Cloud environments with minimal security requirements.
  * **Premium**. Everything in Standard, plus advanced security and compliance posture management, attack paths, threat detection, and compliance monitoring for Google Cloud only. The Premium tier can be activated at the project or organization level. Premium is offered in two billing modalities:

    * Pay-as-you-go for customers who want flexibility.
    * Subscription for customers with more predictable needs.
  * **Enterprise**. (Deprecated) Complete multi-cloud CNAPP security that helps you to triage and remediate your most critical issues. Includes most of the services that are in Premium. The Enterprise tier can only be activated at the organization level. Best for helping to protect Google Cloud, AWS, and Azure.




The Standard tier is offered at no additional charge, while the Premium and Enterprise tiers have different pricing structures. For more information, see [Security Command Center pricing](https://cloud.google.com/security-command-center/pricing).

For the Google SecOps features supported with the Security Command Center Enterprise tier, see [Google SecOps features in Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/secops-limits).

Service | Service tier  
---|---  
Standard-legacy | Standard | Premium | Enterprise (Deprecated)  
Vulnerability detection   
Vulnerability scanning   
[ Anomaly Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#anomaly_detection).1 Identifies security anomalies for your projects and virtual machine (VM) instances, like potential leaked credentials and cryptocurrency mining. | 2| 2| 2|   
[ Artifact Registry vulnerability assessment](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#ar-vuln-assessment). Automatically write findings to Security Command Center from Artifact Registry scans that detect vulnerable container images deployed to specific assets. | 2| 2| 2|   
[ Sensitive Data Protection discovery](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery).1 Discovers, classifies, and helps protect sensitive data. | 3| | 3|   
[ Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud). Helps you discover critical and high severity software vulnerabilities in your Compute Engine VM instances without installing agents. A limited set of capabilities are available on the Standard tier. | | 4| |   
[ Agent Platform Vulnerability Assessment](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#aevs) ([Preview](https://cloud.google.com/products#product-launch-stages)). Automatically write findings to Security Command Center from Agent Platform Vulnerability Assessment scans of Gemini Enterprise Agent Platform, including vulnerable agentic workloads and plaintext secrets in container images. | | | |   
[ External Exposure](https://docs.cloud.google.com/security-command-center/docs/detect-external-exposure) ([Preview](https://cloud.google.com/products#product-launch-stages)). Automatically discover exposed external assets, trace your complete network path, and help validate real-world exploitability without manual configuration. | | | |   
[ Notebook Security Scanner](https://docs.cloud.google.com/security-command-center/docs/enable-notebook-security-scanner) ([Preview](https://cloud.google.com/products#product-launch-stages)). Detect and resolve vulnerabilities in Python packages that are used in Colab Enterprise notebooks. | | | |   
VM Manager vulnerability reports ([Preview](https://cloud.google.com/products#product-launch-stages)).1 If you [enable VM Manager](https://docs.cloud.google.com/compute/docs/manage-os), it automatically writes findings from its vulnerability reports to Security Command Center. | | | 2|   
[ Vulnerability Assessment for AWS](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-aws-overview). Detects vulnerabilities in AWS resources, including software installed on Amazon EC2 instances and in Elastic Container Registry (ECR) images. | | | |   
[ Security Health Analytics ](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings)  
Managed vulnerability assessment scanning for Google Cloud that can automatically detect the highest severity vulnerabilities and misconfigurations for your Google Cloud assets.Not supported with new Standard tier activations. A subset of capabilities are available in the Standard tier for organizations that were migrated from the Standard-legacy tier.| | 4| |   
[ Compliance monitoring](https://docs.cloud.google.com/security-command-center/docs/compliance-management). Security Health Analytics detectors map to the controls of common security benchmarks like NIST, HIPAA, PCI-DSS, and CIS. | | | |   
[ Custom module support](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview). Create your own custom Security Health Analytics detectors. | | | |   
[ Web Security Scanner ](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)  
[ Custom scans](https://docs.cloud.google.com/security-command-center/docs/how-to-web-security-scanner-custom-scans). Schedule and run custom scans on deployed Compute Engine, Google Kubernetes Engine, or App Engine web applications that have public URLs and IP addresses and aren't behind firewalls. | | | |   
[ Additional OWASP Top Ten detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview#finding_types)| | | |   
[ Managed scans](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview#managed_scans). Scan public web endpoints for vulnerabilities weekly, with scans configured and managed by Security Command Center. | | | |   
Virtual red teaming   
[ Attack Path Simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn). Helps you to identify and prioritize vulnerability and misconfiguration findings by identifying the paths that a potential attacker could take to reach your high-value resources. | | | 2|   
[ Chokepoints](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview). Identifies resources or resource groups where multiple attack paths converge. | | | |   
[ Issues](https://docs.cloud.google.com/security-command-center/docs/issues-overview). Identifies the most important security risks that Security Command Center has found in your cloud environments. Issues are discovered using virtual red teaming, along with rule-based detections that rely on the Security Command Center security graph. | | | 2|   
[ Risk reports](https://docs.cloud.google.com/security-command-center/docs/risk-reports-overview) ([Preview](https://cloud.google.com/products#product-launch-stages)). Risk reports help you understand the results of the attack path simulations that Security Command Center runs. A risk report contains a high-level overview, sample toxic combinations, and associated attack paths. | | | 2|   
[ Toxic combinations](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview). Detects groups of risks that, when they occur together in a particular pattern, create a path to one or more of your high-value resources that a determined attacker could potentially use to reach and compromise those resources. | | | |   
Other vulnerability services   
[ Compute Engine Security risk dashboard findings](https://docs.cloud.google.com/compute/docs/monitor-security-risks-console). View the security risks that affect your Compute Engine resources. | | | |   
[ GKE security posture dashboard findings](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard) ([Preview](https://cloud.google.com/products#product-launch-stages)). View findings about Kubernetes workload security misconfigurations, actionable security bulletins, and vulnerabilities in the container operating system or in language packages. | | | |   
[ Model Armor](https://docs.cloud.google.com/model-armor/overview). Screen LLM prompts and responses for security and safety risks. Model Armor provides a number of tokens per month at no charge to all Google Cloud customers. For more information, see [Pricing](https://docs.cloud.google.com/security-command-center/pricing#possible-indirect-charges-associated-with-model-armor). Model Armor findings are published to Security Command Center on the Premium and Enterprise tiers. | | | |   
[ Mandiant CVE assessments](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#mandiant-cve-assessment) ([Preview](https://cloud.google.com/products#product-launch-stages)). Findings are enriched with [CVE](https://www.cve.org/ResourcesSupport/Glossary) assessments from Mandiant threat intelligence analysts, including the CVE exploitability and potential impact. You can query findings by CVE ID. A limited set of capabilities are available in the Standard tier. | | 4| |   
[ Artifact guard](https://docs.cloud.google.com/security-command-center/docs/artifact-guard-overview) ([Preview](https://cloud.google.com/products#product-launch-stages)). (Deprecated) Artifact guard is a service that helps you prevent the deployment of vulnerable packages throughout the build process. Artifact guard supports three types of policy scopes: [CI/CD platform](https://docs.cloud.google.com/security-command-center/docs/configure-cicd-integration), registry, and runtime. | | | |   
[ Mandiant Attack Surface Management](https://docs.cloud.google.com/security/products/attack-surface-management). Discovers and analyzes your internet assets across environments, while continually monitoring the external ecosystem for exploitable exposures. | | | | 5  
Postures and policies   
[ Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview).1 Implement software supply-chain security measures when you develop and deploy container-based applications. Monitor and limit the deployment of container images. | 2| 2| 2|   
[ Cloud Infrastructure Entitlement Management (CIEM)](https://docs.cloud.google.com/security-command-center/docs/ciem-overview). Identify principal accounts (identities) that are misconfigured, are granted excessive permissions, or are granted sensitive permissions to your cloud resources.| | | | 6  
[ Cyber Insurance Hub](https://docs.cloud.google.com/risk-manager/docs/overview).1 Profile and generate reports for your organization's technical risk posture. | 2| 2| 2|   
[ Infrastructure as code (IaC) validation](https://docs.cloud.google.com/security-command-center/docs/validate-iac). Validate against organization policies and Security Health Analytics detectors. | 2| | 2|   
[ Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview).1 Enables the application and enforcement of programmable policies for your Kubernetes clusters. | 2| 2| 2|   
[ Policy Intelligence](https://docs.cloud.google.com/policy-intelligence/docs/overview). Provides tools that help you understand and manage your access policies to proactively improve your security configuration.  Policy Intelligence provides some features to Google Cloud customers at no charge, such as recommendations for basic roles and a limited number of queries per month. Advanced features are available for Security Command Center Premium and Enterprise users. For details, see [Pricing](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions#pricing). | | | |   
[ AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview). AI Protection helps you manage the security posture of your AI workloads by detecting threats and helping you to mitigate risks to your AI asset inventory. | | 4| |   
[ Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview). Define, deploy, monitor, and audit controls and frameworks that are designed to help you meet the security and compliance obligations for your Google Cloud environment. A limited set of capabilities are available on the Standard tier. | | 4| 7, 8| 8  
[ Data security posture management (DSPM)](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security). (Deprecated) Evaluate, deploy, and audit data security frameworks and cloud controls to govern access and use of sensitive data. A limited set of capabilities are available in the Standard tier. | | 2, 4| 2|   
[ Security posture](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview). Define and deploy a security posture to monitor the security status of your Google Cloud resources. Address posture drift and unauthorized changes to the posture. On the Enterprise tier, you can also [monitor your AWS environment](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview#security-posture-aws). | | | 2|   
Threat detection and response   
[ Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview).1 Protects Google Cloud deployments against threats such as distributed denial-of-service (DDoS) attacks, cross-site scripting (XSS), and SQL injection (SQLi). | 2| 2| 2|   
[ Sensitive Actions Service](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview). Detects when actions are taken in your Google Cloud organization, folders, and projects that could be damaging to your business if they are taken by a malicious actor. | | | |   
[ Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview) ([Preview](https://cloud.google.com/products#product-launch-stages)). Detects runtime attacks on agents that are deployed and managed through Agent Runtime. | | | |   
[ Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview). Detects runtime attacks in Cloud Run containers. | | | |   
[ Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview). Detects runtime attacks in [Container-Optimized OS node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos). | | | |   
[ Correlated Threats](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview) ([Preview](https://cloud.google.com/products#product-launch-stages)). Helps you make more informed decisions about security incidents. This feature combines related threat findings together by using the security graph, helping you to prioritize and respond to active threats. | | | |   
[ Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview). Monitors Cloud Logging and Google Workspace, using threat intelligence, machine learning, and other advanced methods to detect threats such as malware, cryptocurrency mining, and data exfiltration. | | | |   
[ Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview). Detects potentially malicious applications running in VM instances. | | | |   
[ Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview). Integrates with Security Command Center to help you detect, investigate, and respond to threats. Google SecOps includes the following: 

  * [Google SecOps security information and event management (SIEM)](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc). Scan logs and other data for threats across multiple cloud environments, define threat detection rules, and search the accumulated data. 
  * [Google SecOps security orchestration, automation, and response (SOAR)](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc). Manage cases, define response workflows, and search the response data. 

| | | |   
[ Mandiant Threat Defense](https://docs.cloud.google.com/security/products/mandiant-managed-threat-hunting). Rely on Mandiant experts to provide continual threat hunting to expose attacker activity and reduce impact to your business.Mandiant Threat Defense is not activated by default. For more information and pricing details, contact your sales representative or Google Cloud partner.| | | |   
Data management   
Data residency and encryption   
[ Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/security-command-center/docs/cmek). Use Cloud Key Management Service keys that you create to encrypt selected Security Command Center data. By default, Security Command Center data is encrypted at rest with Google-owned and Google-managed encryption keys. | 2| 2| 2|   
[ Data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support). Controls that restrict the storage and processing of Security Command Center findings, mute rules, continuous exports, and BigQuery exports to one of the data residency multi-regions that Security Command Center supports. | 2| 2| 2|   
[ Modify data residency and data encryption](https://docs.cloud.google.com/security-command-center/docs/modify-data-residency-encryption). Change the data residency or data encryption configuration after you activate Security Command Center. | 2| 2| 2|   
Findings export   
BigQuery exports. Export findings from Security Command Center to BigQuery, either as a [one-time bulk export](https://docs.cloud.google.com/security-command-center/docs/bulk-exports-to-big-query) or by enabling [continuous exports](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query). | | | |   
[ Pub/Sub continuous exports](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#continuous_exports)| | | |   
[ Cloud Logging continuous exports](https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging)| | | 2|   
Other features   
[ App Hub integration](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#apphub-integration). Security Command Center integrates with App Hub to let you filter data related to resources registered to a specific application when investigating findings and issues. | | | |   
[ Cloud Hub Security & compliance page](https://docs.cloud.google.com/hub/docs/security) ([Preview](https://cloud.google.com/products#product-launch-stages)). Security Command Center integrates with Cloud Hub to help you quickly identify critical risks. | | | |   
[ Application Design Center integration for Infrastructure as Code (IaC) validation](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#application-security-assessments). View design-time findings for applications registered in App Hub through integration with Application Design Center and Infrastructure as Code (IaC) validation. | | | |   
[ Assured Open Source Software](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc). Take advantage of the security and experience that Google applies to open source software by incorporating the same packages that Google secures and uses into your own developer workflows. | | | 2|   
[ Graph Search](https://docs.cloud.google.com/security-command-center/docs/graph-search) ([Preview](https://cloud.google.com/products#product-launch-stages)). Query the security graph to identify potential security vulnerabilities that you want to monitor in your environment. | | | 2|   
[ Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-overview). Privileged Access Manager helps you control just-in-time, temporary privilege elevation for specific principals and provides audit logs to track who had access to which resources and when. The following features are available with Security Command Center:

  * [ Multi-level and multi-party approvals](https://docs.cloud.google.com/iam/docs/pam-overview#mp-approvals) ([Preview](https://cloud.google.com/products/#product-launch-stages)). Administrators can mandate more than one approval level per entitlement, allowing up to two levels of sequential approvals for each entitlement. 
  * [ Scope customization](https://docs.cloud.google.com/iam/docs/pam-overview#customize-scope) ([Preview](https://cloud.google.com/products/#product-launch-stages)). Requesters can customize the scope of their grant requests to include only the specific roles and resources that they need within the scope of their entitlement. 

| | | 2|   
[ Query assets with SQL in Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/query-assets-with-sql)| | | |   
[ Request more Cloud Asset Inventory quota](https://docs.cloud.google.com/asset-inventory/docs/quota#request-quota)| | | |   
Multicloud support. Connect Security Command Center to other cloud providers to detect threats, vulnerabilities, and misconfigurations. Assess attack exposure scores and attack paths on external cloud high-value resources. Supported cloud providers: AWS, Azure. | | | |   
  
  1. This is a Google Cloud service that integrates with organization-level activations of Security Command Center to provide findings. One or more features of this service might be priced separately from Security Command Center. 
  2. Requires an organization-level activation. 
  3. Not activated by default. For more information and pricing details, contact your sales representative or Google Cloud partner. 
  4. This service or feature provides limited capabilities on the Standard tier. 
  5. If [data residency controls](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) are enabled, then this feature is not supported. 
  6. If [data residency controls](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) are enabled, then this feature is supported only for Google Cloud. 
  7. This feature doesn't support customer-managed encryption keys (CMEK). 
  8. Doesn't support [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
