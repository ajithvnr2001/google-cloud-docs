---
url: https://docs.cloud.google.com/chronicle/docs/secops/google-unified-security/
title: Google Unified Security overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:31.397889+00:00
---

# Google Unified Security overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/google-unified-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Unified Security overview 

Google Unified Security is our new AI-powered converged security solution, designed to address the challenges of fragmented data and siloed security tools of which threat actors are increasingly taking advantage. By integrating Google's leading threat intelligence, security operations, cloud security, secure enterprise browsing, and Mandiant expertise, Google Unified Security creates a scalable security solution running on a planet-scale security fabric to secure your organization. Real-time insights from Gemini AI enhances threat detection and streamlines security operations, empowering organizations to shift from reactive to preemptive security and stay two steps ahead of increasingly sophisticated attackers 

The key components of Google Unified Security are: 

  * [Modern Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview): Detect, investigate, and respond to threats at Google speed and scale
  * [Threat intelligence and exposure management](https://gtidocs.virustotal.com/): Know who is targeting you and where you are exposed.
  * [Comprehensive Google Cloud protection and AI security](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview): Reduce cloud risk and secure your cloud and AI workloads, anywhere.
  * [Secure Enterprise browser](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview): Protect your corporate data on any device. 
  * [Incident response and expert assistance](https://cloud.google.com/security/consulting/mandiant-incident-response-services): World class Mandiant incident experts are by your side. 
  * **Agentic AI Triage and Investigation** : Automatic triage and investigation of security alerts.



![GUS diagram](https://docs.cloud.google.com/chronicle/images/gusdiagram.png)

## Five Main Solutions Enabled by GUS

The following solutions harness the power of the Google Unified Security suite of products.

## Strengthening Endpoint Security: Integrated protection with Google Chrome Enterprise Premium & Google SecOps

Chrome Enterprise Premium (CEP) integration with Google SecOps provides critical visibility into threats originating from browser activity to strengthen your endpoint security posture. The browser has become a common point of entry for a wide range of threats, including malware, phishing attacks, credential theft, and data exfiltration. As many business applications are accessed primarily with a browser, it is essential to respond to these threats before attackers can gain access to critical data.

This integration unlocks new security operations workflows, enabling analysts to more effectively manage browser-based risks from Google SecOps.

  * **New curated detections** : specifically designed for Chrome threats and enriched with Safe Browsing and Google Threat Intelligence (GTI), allow for the identification of threats that might be missed by other security controls.
  * **Improved visibility** : Security analysts gain better visibility through dedicated Google SecOps dashboards that provide key insights into Chrome security events and anomalies to facilitate investigation. 
  * **Automated response** :Leveraging native playbook orchestration capabilities, security teams can also automate response actions on Chrome Enterprise, such as blocking malicious URLs, blocking extensions, and even quarantining devices, directly from the Google SecOps platform.
  * **Simplified Onboarding** : With just a few clicks, enable recommended security defaults and a direct integration of Chrome data. 



This centralized approach, enhanced by Google Threat Intelligence enrichment, empowers security teams to achieve faster detection, conduct more informed investigations, and more efficiently remediate web-based threats.

#### Getting Started with Google Chrome and Google SecOps

  * [Configure the Chrome Enterprise Premium Reporting Connector to send data to Google SecOps](https://support.google.com/chrome/a/answer/11375053?sjid=8303965136477425945-NA#zippy=%2Cadd-a-configuration-to-an-existing-provider)
  * [Connect Chrome Enterprise Premium to Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-bce)
  * [Enable Chrome Enterprise Threats Curated Detections](https://docs.cloud.google.com/chronicle/docs/detection/chrome-enterprise-threats-category)



#### Examples

**Investigating Malicious Browser Extensions** A user downloads and installs a malicious browser extension from outside the Chrome Web Store, that once installed, reads their session cookies and posts them to a server on a suspicious domain that was registered within the last week. Using browser extension telemetry a security analyst can determine how many users have installed this extension and take remediation actions to remove it from their devices.

**What browser activities are present on Unmanaged or Bring-Your-Own Devices (BYOD)** An employee working remotely on their personal laptop, accesses company resources through the Chrome browser to work on a project. Chrome Enterprise policies can enforce policies on how the employee can use the data from business applications. Attempts to bypass these policies such as attempting to upload or download files can be monitored to ensure sensitive data isn't stored on the unmanaged device.

**Suspicious user activities occurring within your environment** A security analyst receives an alert that a user has suddenly initiated a large data transfer to an external cloud storage service after several failed login attempts, raising suspicion of a potential account compromise or unauthorized data transfer. By analyzing the user behavior trends, the analyst can validate whether this employee typically only traditionally accesses these files during standard business hours and their account was compromised.

**Measure effectiveness of Data Loss Prevention (DLP) policies** An administrator can measure the effectiveness of DLP rules by reviewing aggregate data to ensure that "block" and "warn" policies applied through Chrome are addressing threats and not preventing legitimate work. 

## Streamline SOC Operations with Security Command Center and Google SecOps

Google Unified Security includes Google Security Command Center Enterprise with the latest AI Protection suite. 

Google SecOps provides Cloud Detection Investigation and Response (CDIR), Case Management, SIEM log searching and investigation, Cloud Asset Inventory collection for Entity Graph Enrichment, and the ability to automate common SOC workflows using the SOAR component of Google SecOps.

With the unified capabilities between Google SecOps and Security Command Center, SOC analysts and Cloud Security engineers have a single converged platform within which to view and respond to incidents and cases related to threats in their Google Cloud, Azure, and AWS platforms. Since both SIEM and SOAR capabilities are front and center within the platform, there's no need anymore to send Cloud log data and related threat events outside of the platform - everything is included under the umbrella heading of Google Unified Security.

In order to enable the full complement of CDIR features, certain logs need to be ingested into Google SecOps, some directly from Google Cloud, and for multi-cloud capability, from AWS and Azure.

#### Getting Started with Security Command Center and Google SecOps

  1. Activate the Enterprise Tier of SCC-E using your existing Google SecOps instance. See [activate enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier)

  2. Validate Security Command Center Detection Services are enabled: See [How to configure Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center)

  3. Connect Security Command Center to AWS to get configuration and resource data that flows through to the Entity Graph: See [Connect Security Command Center to AWS](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws)

  4. Preview - Connect Security Command Center to Azure to get configuration and resource data that flows through to the Entity Graph.

  5. (Optional) Integrate Security Command Center with ticketing systems. See [Integrate ticketing system](https://docs.cloud.google.com/security-command-center/docs/integrate-ticketing-systems)

  6. Map users to the Google SecOps platform. See [Map users](https://docs.cloud.google.com/security-command-center/docs/map-users-in-secops)

  7. Enable the response playbooks. See [Install playbooks](https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update)

  8. Ingest the Google Cloud logs into Google SecOps using direct ingestion: See [Ingest Google Cloud logs](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs)

  9. Set up the Google Cloud Export Filter.

  10. Ingest the AWS logs into Google SecOps: See [Ingest AWS logs](https://docs.cloud.google.com/security-command-center/docs/connect-secops-aws).

  11. Ingest Azure logs into Google SecOps: See [Ingest Azure logs](https://docs.cloud.google.com/security-command-center/docs/connect-secops-azure)

  12. Configure optional services, See [Advanced Configuration](https://docs.cloud.google.com/security-command-center/docs/advanced-configuration-threat-management)

  13. Enable the CDIR Curated Detections. See [Curated Detections](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category)




#### Examples

**CDIR** : An analyst receives a high priority CDIR SCC Enhanced Privilege Escalation alert (one of many driven by [Cloud Threat Curated Detections](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#cloud-rule-sets)) that gets automatically mapped to a Google SecOps case. They see the behavior within the alert corresponds to a service account that is over-privileged, and is allowing an adversary to move laterally through a cloud environment, access new systems, and escalate to higher privileges in order to carry out malicious actions. The analyst can review the behavior and react by adjusting the account permissions or disabling the account.

**SIEM Log Searching and Investigation** : During a CDIR investigation, or on an ad-hoc basis, analysts can use either natural language syntax, Yara-L syntax, or raw log searching to surface information in various logs ingested into Google SecOps related to cloud infrastructure and services. This allows for the verification of potential adversary behavior to rule out false positives or prove a true positive. Common log sources used during these kinds of investigations include (but are not limited to) Google Cloud audit logs, AWS CloudTrail logs and GuardDuty events, and Azure AD activity logs.

**Cloud Asset Inventory Collection** : Once the various connectors between Google SecOps and Security Command Center are established, asset inventory information about multi-cloud environments regularly flows into the Google SecOps Entity Graph. From there, SOC analysts and other users of the system see immediate additional context, driven by this inventory, to speed analysis and help prioritize workflow. For example, an enriched alert concerning an AWS S3 bucket may contain additional information about the bucket such as the region, the owner, and metadata tags surrounding the bucket even if that information wasn't present in the source alert.

## Enable Secure AI Adoption from Creation to Consumption

Google Cloud's AI Protection is a comprehensive set of capabilities integrated directly into Security Command Center Enterprise (SCC-E), designed to help you proactively manage the unique risks associated across the AI lifecycle. By providing a centralized view of your AI assets, risks, and threats alongside your broader cloud security landscape, AI Protection empowers security teams and developers to confidently build and deploy AI solutions.

#### Key Benefits

  * **Enable Safe and Secure AI Adoption** : Security is often cited as a key barrier to AI adoption. AI Protection helps overcome this challenge by providing the tools and insights needed to mitigate risks such as data breaches, misconfigurations, and unsafe model usage. This allows your organization to accelerate its AI transformation with confidence.
  * **Security across the AI lifecycle** : AI Protection offers end-to-end security to protect against potential risks and threats across the AI lifecycle. This includes:

    * **Discovery of your AI Inventory** : AI Protection can thoroughly scan your systems to identify and catalog all existing AI assets, including models, datasets, and associated applications. This provides a clear picture of your AI landscape, enabling better management and control.
    * **Security of your AI Assets** : AI Protection uses our virtual red teaming capabilities to identify potential attack paths across your AI and cloud assets. This includes surfacing toxic combinations that could allow attackers to access high-value AI resources and prioritizing the highest impact and highest risk items.
    * **Detection and Response for AI Threats** : AI Protection actively monitors your AI environment to detect and respond to potential threats. This includes detecting and responding to LLM highjacking, data poisoning or exfiltration, and other forms of AI-targeted cyberattacks. Response and remediation workflows are directly integrated with Google SecOps.
  * **Model and Cloud agnostic Protection with Model Armor** : Model Armor protects against data loss, brand damage, and offensive content by screening generative AI prompts and responses. Model Armor is model-agnostic and supports a broad range of models across various clouds, including Google's models (like Gemini), open-source models (like Llama), and third-party proprietary models (like OpenAI and Anthropic Claude). It guards against prompt injection, jailbreaks, sensitive data leaks, malicious URLs, and offensive content. Model Armor offers flexible deployment options, including a REST API for broad coverage and in-line integration with Vertex AI and other Google Cloud enforcement points for reduced latency and no app changes.

  * **Protect Sensitive Data in AI Workloads** : AI Protection integrates with Google Cloud's Sensitive Data Protection (SDP) service to discover, classify, and redact sensitive data going into and out of AI workloads. Model Armor can prevent the leakage of sensitive data in AI responses.

  * **Centralized Visibility and Response within Security Command Center** : AI Protection is delivered in SCC-E which provides CNAPP capabilities and SIEM/SOAR integration with Google SecOps as part of GUS. This provides a single pane of glass for managing AI risks and responding and remediating threats in context with your overall cloud security. This unified experience streamlines security workflows from risk migration to detection and response, allowing for faster response and remediation times. 




#### Examples

SCC-E customers have immediate access to several key AI Protection capabilities:

  * [Model Armor](https://console.cloud.google.com/projectselector2/security/modelarmor/templates): Protects against prompt injection, data loss, and offensive content,through prompt and response screening.
  * [Sensitive Data Protection (SDP) Discovery](https://console.cloud.google.com/security/sensitive-data-protection/): Identifies sensitive data in your AI datasets.
  * [AI-related Toxic Combinations](https://console.cloud.google.com/security/command-center/findingsv2): Detects potentially harmful combinations of AI assets and configurations.
  * [Posture Management for AI (Vertex AI)](https://console.cloud.google.com/security/command-center/posture): Assesses and manages the security posture of your Vertex AI resources.
  * [Threat Detection for AI (Vertex AI)](https://console.cloud.google.com/projectselector2/security/command-center/threats): Detects and alerts on threats targeting your Vertex AI workloads.
  * **Notebook Security Scanner (Preview)** : Scans your AI notebooks for security vulnerabilities.
  * [Data Security Posture Management (DSPM) for BigQuery & Cloud Storage (Preview)](https://console.cloud.google.com/security/command-center/enterprise/overview/data-security): Helps manage the security posture of your data used in AI.



**Further Resources to get started:**

  * [Model Armor Documentation](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview)
  * [AI Protection Overview Blog Post](https://cloud.google.com/blog/products/identity-security/introducing-ai-protection-security-for-the-ai-era?e=48754805)
  * [Security Command Center Documentation](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview#tiers)
  * [Sensitive Data Protection Documentation](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



## Continuous Security Validation: Stop Reacting, Start Preventing with Google SecOps

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This feature may not be available to all customers in all regions. Private preview features are not manageable in the Public Preview Manager page in the Google SecOps platform. 

Security teams in SOCs are constantly overwhelmed trying to keep up with the ever-changing threat landscape. Manually assessing vulnerabilities is a time-consuming and reactive process. In addition, the cascading of third-party security controls and complex group policy or IAM permissions have created environments ripe for misconfiguration. This creates a gap between an organization's assumed posture and actual posture which ultimately increases risk. Automated, continuous validation delivers actionable data, empowering you to proactively attack and optimize your defenses via easy-to-use integrated workflows. 

#### Key Benefits

  * **Attack Simulation Catalog** informed by Mandiant front-line intelligence
  * **Security Validation Engine** executing the latest attacker techniques, informed by mandiant front-line intel.
  * **Detection Monitors** to proactively identify broken detections on a scheduled basis. 



#### Examples

**Continuous Detection Validation** removes the need to manually test and verify detections work as expected after initial deployment. How it works:

  * Explore the attack catalog by common attacker TTPs or target service.
  * Execute attacks to test Curated Detections and review results.
  * Run attacks on a recurring basis to continuously ensure detection efficacy.
  * Review results & trends on the Monitor dashboard.



**Continuous Emerging Threat Validation** automates the conversion of intelligence reports into executable procedures to validate your real word response. How it works:

  * An emerging threat relevant to your org has been discovered.
  * Your defenses have been updated with curated detections.
  * We execute AI-generated attacks to test detections in your environment.
  * We open cases if any detections fail.
  * Results and AI informed recommendations are provided.



## Future-Proof Your Defenses: Proactive Threat Hunting with Integrated GTI in Google SecOps

Integrating Google Threat Intelligence (GTI) directly within Google SecOps transforms threat detection and response from reactive to proactive through the [Applied Threat Intelligence (ATI)](https://docs.cloud.google.com/chronicle/docs/detection) feature. ATI continuously analyzes your security telemetry against high-fidelity Indicators of Compromise (IOCs) curated by GTI. By applying this frontline intelligence directly within Google SecOps, security teams gain unparalleled visibility and context, ensuring that security events are actively interpreted through the lens of the latest, validated threat intelligence to help you stay ahead of novel and sophisticated attacks. This integration leverages Google SecOps curated detections to evaluate event data against GTI IOCs, automatically generating prioritized alerts (such as [Active Breach or High](https://docs.cloud.google.com/chronicle/docs/detection/ati-prioritization)) to ensure focus on critical threats.

#### Key Benefits

  * **Intelligence-Driven Detection:** Leverage Google SecOps curated detections that evaluate your event data against Mandiant IOCs. Automatically generate alerts when matches are found for IOCs labeled **Active Breach** or **High** , ensuring focus on critical threats.
  * **Enhanced Investigation Context:** Accelerate investigations using the dedicated **[IOC Matches page](https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page)** in Google SecOps. Gain immediate context around suspicious entities (domains, IPs, hashes, URLs) including **GCTI Priority** , **IC-Score** , threat actor/malware **Associations** , and related **Campaigns** , all without pivoting to external tools.
  * **Prioritized Alerts:** Benefit from intelligence-driven alert prioritization based on Mandiant insights (e.g., Active IR, Prevalence, Attribution, Commodity status). Focus response efforts on alerts classified as Active Breach, High, or Medium based on contextualized IOC matches.
  * **Proactive Threat Hunting:** Utilize GTI feeds and insights within Google SecOps search and detection rules (YARA-L) to proactively hunt for emerging threats and specific attacker TTPs within your environment.



#### Integration points between Google Threat Intelligence and Google SecOps

  * [Continuous IOC Matching](https://docs.cloud.google.com/chronicle/docs/investigation/alerts-iocs): Google SecOps automatically ingests and evaluates GTI-curated IOCs against your normalized security data (UDM).
  * [Curated Detections & Prioritization](https://docs.cloud.google.com/chronicle/docs/detection/ati-curated-detections): Pre-built detection rules (available in rule packs like "Applied Threat Intelligence - Curated Prioritization") contextualize IOC matches using event data and Mandiant intelligence features to generate prioritized alerts (Active Breach, High, Medium, Inbound IP Auth).
  * [Native Threat Feeds](https://docs.cloud.google.com/chronicle/docs/detection/ati-fusion-feed): Natively integrated threat intelligence feeds from Mandiant, VirusTotal, SafeBrowsing, and more, enable users to create their own custom detections and scoring methodologies.
  * **Centralized Investigation:** The **IOC Matches** page serves as the central hub for viewing matched IOCs, filtering results (by Type, Priority, Status, Source: Mandiant, etc.), and drilling down into event details, UDM context, threat intelligence rationale, and associations.



#### Getting Started

  * **Enable Curated Detections:** Activate the **Applied Threat Intelligence curated detections** rule packs within Google SecOps to enable alerting and prioritization. 
  * **Explore IOC Matches:** Familiarize yourself with investigating alerts using the **IOC Matches** page. 
  * Learn more about how GCTI Priority is determined by clicking on any event from a prioritized IOC Match in **IOC Matches** pages



#### Examples

  * **Investigating a High Priority Alert:** An analyst investigates an **Active Breach** priority alert on the **IOC Matches** page. They see the matched IOC is a domain associated with a known phishing campaign (visible in Associations/Campaigns) with a high IC-Score. Reviewing the event details confirms outbound traffic from a user workstation. The analyst uses this context to trigger a SOAR playbook to isolate the machine and reset user credentials.
  * **Proactive Hunting & Validation:** Following a Mandiant report on a new malware variant, an analyst uses the provided IOCs (hashes, C2 domains) in Google SecOps SIEM Search. They also check the **IOC Matches** page, filtering by the relevant malware association or campaign name, to confirm if ATI has already detected related activity in their environment.



## Onboarding and Activating Google Unified Security

This portfolio brings together the following Google's leading security solutions:

  * Security Command Center (SCCE)
  * Google SecOps (SecOps Enterprise Plus)
  * Google Threat Intelligence (Enterprise Plus)
  * Chrome Enterprise Browser (Premium)
  * Mandiant Threat Defense



**Getting Started** Embark on your journey to a more secure future with Google Unified Security. Whether you're looking to enhance your existing security posture or build a comprehensive defense from the ground up, we have a solution tailored to your needs. For existing Google Security customers: If you are already leveraging the power of any of the individual product components within our security portfolio, we can seamlessly upgrade you to the complete Google Unified Security package. Experience the enhanced visibility, intelligence, and automation that comes with a fully integrated security ecosystem. Contact your Google Cloud account team to explore your upgrade path and unlock the full potential of Google's unified defense.

**For new customers** If you are not yet utilizing Google's cutting-edge security solutions, we invite you to discover the transformative power of Google Unified Security. Our integrated portfolio offers a holistic approach to protecting your organization in today's complex threat landscape. Reach out to your dedicated Google Cloud sales representative to discuss your specific security challenges and explore how Google Unified Security can provide the comprehensive protection you need. We offer customized solutions and deployment options designed to align with your unique requirements and business objectives. Take the first step towards a more secure and resilient future. Connect with us today to learn how Google Unified Security can empower your security teams and safeguard your organization's most valuable assets.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
