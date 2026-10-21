---
url: https://docs.cloud.google.com/architecture/framework/perspectives/fsi/security/
title: Financial services perspective: Security, privacy, and compliance \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:18.841784+00:00
---

# Financial services perspective: Security, privacy, and compliance  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/perspectives/fsi/security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Financial services perspective: Security, privacy, and compliance Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-07-28 UTC

This document in the [Google Cloud Well-Architected Framework: Financial services (FS) perspective](https://docs.cloud.google.com/architecture/framework/perspectives/fsi) provides an overview of the principles and recommendations to address the security, privacy, and compliance requirements of financial services (FS) workloads in Google Cloud. The recommendations help you build resilient and compliant infrastructure, safeguard sensitive data, maintain customer trust, navigate the complex landscape of regulatory requirements, and effectively manage cyber threats. The recommendations in this document align with the [security pillar](https://docs.cloud.google.com/architecture/framework/security) of the Well-Architected Framework.

Security in cloud computing is a critical concern for FS organizations, which are highly attractive to cybercriminals due to the vast amounts of sensitive data that they manage, including customer details and financial records. The consequences of a security breach are exceptionally severe, including significant financial losses, long-term reputational damage, and significant regulatory fines. Therefore, FS workloads need stringent security controls.

To help ensure comprehensive security and compliance, you need to understand the [shared responsibilities](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) between you (FS organizations) and Google Cloud. Google Cloud is responsible for securing the underlying infrastructure, including physical security and network security. You are responsible for securing data and applications, configuring access control, and configuring and managing security services. To support you in your security efforts, the [Google Cloud partner ecosystem](https://cloud.google.com/find-a-partner/?specializations=Security%20-%20Services) offers security integration and managed services.

The security recommendations in this document are mapped to the following core principles:

  * Implement security by design
  * Implement zero trust
  * Implement shift-left security
  * Implement preemptive cyber defense
  * Use AI securely and responsibly, and use AI for security
  * Meet regulatory, compliance, and privacy needs
  * Prioritize security initiatives



## Implement security by design

Financial regulations like the [Payment Card Industry Data Security Standard (PCI DSS)](https://www.pcisecuritystandards.org/standards/pci-dss/), the [Gramm-Leach-Bliley Act (GLBA)](https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act) in the United States, and various national financial data protection laws mandate that security is integrated into systems from the outset. The security-by-design principle emphasizes the integration of security throughout the development lifecycle to help ensure that vulnerabilities are minimized from the outset.

To apply the security-by-design principle for your FS workloads in Google Cloud, consider the following recommendations:

  * Ensure that only necessary permissions are granted by applying the principle of least privilege through granular role-based access control (RBAC) in [Identity and Access Management (IAM)](https://cloud.google.com/security/products/iam). The use of RBAC is a key requirement in many financial regulations.
  * Enforce security perimeters around your sensitive services and data within Google Cloud by using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). The security perimeters help to segment and protect sensitive data and resources, and help to prevent data exfiltration and unauthorized access, as required by regulations.
  * Define security configurations as code by using infrastructure as code (IaC) tools like [Terraform](https://docs.cloud.google.com/docs/terraform/terraform-overview). This approach embeds security controls from the initial deployment phase, which helps to ensure consistency and auditability.
  * Scan your application code by integrating [Static Application Security Testing (SAST)](https://en.wikipedia.org/wiki/Static_application_security_testing) into the CI/CD pipeline with [Cloud Build](https://docs.cloud.google.com/build/docs/overview). Establish automated security gates to prevent the deployment of non-compliant code.
  * Provide a unified interface for security insights by using [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview). The use of Security Command Center enables continuous monitoring and early detection of misconfigurations or threats that could lead to regulatory breaches. To meet the requirements of standards such as [ISO 27001](https://docs.cloud.google.com/security-command-center/docs/security-posture-iso-27001-template) and [NIST 800-53](https://docs.cloud.google.com/security-command-center/docs/security-posture-nist-800-53-template), you can use [posture management](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview) templates.
  * Track the reduction in vulnerabilities that are identified in production deployments and the percentage of IaC deployments that adhere to security best practices. You can detect and view vulnerabilities and information about compliance to security standards by using Security Command Center. For more information, see [Vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).



## Implement zero trust

Modern financial regulations increasingly emphasize the need for stringent access controls and continuous verification. These requirements reflect the principle of zero trust, which aims to protect workloads against both internal and external threats and bad actors. The zero-trust principle advocates for continuous verification of every user and device, which eliminates implicit trust and mitigates [lateral movement](https://en.wikipedia.org/wiki/Lateral_movement_\(cybersecurity\)).

To implement zero trust, consider the following recommendations:

  * Enable context-aware access based on user identity, device security, location, and other factors by combining [IAM](https://cloud.google.com/security/products/iam) controls with [Chrome Enterprise Premium](https://cloud.google.com/chrome-enterprise-premium/docs/overview). This approach ensures continuous verification before access to financial data and systems is granted.
  * Provide secure and scalable identity and access management by configuring [Identity Platform](https://cloud.google.com/security/products/identity-platform) (or your external identity provider if you use [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation)). Set up multi-factor authentication (MFA) and other controls that are crucial to implement zero trust and help ensure regulatory compliance.
  * Implement MFA for all user accounts, especially for accounts with access to sensitive data or systems.
  * Support audits and investigations related to regulatory compliance by establishing comprehensive logging and monitoring of user access and network activity.
  * Enable private and secure communication between services within Google Cloud and on-premises environments without exposing the traffic to the public internet by using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).
  * Implement granular identity controls and authorize access at the application level by using [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) rather than relying on network-based security mechanisms like VPN tunnels. This approach helps to reduce lateral movement within the environment.



## Implement shift-left security

Financial regulators encourage proactive security measures. Identifying and addressing vulnerabilities early in the development lifecycle helps to reduce the risk of security incidents and the potential for non-compliance penalties. The principle of shift-left security promotes early security testing and integration, which helps to reduce the cost and complexity of remediation.

To implement shift-left security, consider the following recommendations:

  * Ensure automated security checks early in the development process by integrating security scanning tools, such as container vulnerability scanning and static code analysis, into the CI/CD pipeline with [Cloud Build](https://docs.cloud.google.com/build/docs/overview).

  * Ensure that only secure artifacts are deployed by using [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) to provide a secure and centralized repository for software packages and container images with integrated vulnerability scanning. Use virtual repositories to mitigate [dependency confusion attacks](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies#public-dependencies) by prioritizing your private artifacts over remote repositories.

  * Automatically scan web applications for common vulnerabilities by integrating [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview), which is a part of [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview), into your development pipelines.

  * Implement security checks for the source code, build process, and code provenance by using the [Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev/) framework. Enforce the provenance of the workloads that run in your environments by using solutions such as [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview). Ensure that your workloads use only verified open-source software libraries by using [Assured Open Source](https://docs.cloud.google.com/assured-open-source-software/docs/overview).

  * Track the number of vulnerabilities that are identified and remediated in your development lifecycle, the percentage of code deployments that pass security scans, and the reduction in security incidents caused by software vulnerabilities. Google Cloud provides tools to help with this tracking for different kinds of workloads. For example, for containerized workloads, use the [container scanning feature of Artifact Registry](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).




## Implement preemptive cyber defense

Financial institutions are prime targets for sophisticated cyberattacks. Regulations often require robust threat intelligence and proactive defense mechanisms. Preemptive cyber defense focuses on proactive threat detection and response by using advanced analytics and automation.

Consider the following recommendations:

  * Proactively identify and mitigate potential threats, by using the [threat intelligence](https://cloud.google.com/security/products/threat-intelligence), [incident response](https://cloud.google.com/security/consulting/mandiant-incident-response-services), and [security validation](https://cloud.google.com/security/products/mandiant-security-validation) services of [Mandiant](https://cloud.google.com/security/mandiant).
  * Protect web applications and APIs from web exploits and DDoS attacks at the network edge by using [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview).
  * Aggregate and prioritize security findings and recommendations by using [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview), which enables security teams to proactively address potential risks.
  * Validate preemptive defenses and incident response plans by conducting regular security simulations and penetration testing.
  * Measure the time to detect and respond to security incidents, the effectiveness of DDoS mitigation efforts, and the number of prevented cyberattacks. You can get the required metrics and data from [Google Security Operations SOAR and SIEM dashboards](https://docs.cloud.google.com/chronicle/docs/secops/understand-the-secops-platform#siem-dashboards-and-soar-dashboards).



## Use AI securely and responsibly, and use AI for security

AI and ML are increasingly used for financial services use cases such as fraud detection and algorithmic trading. Regulations require that these technologies be used ethically, transparently, and securely. AI can also help to enhance your security capabilities. Consider the following recommendations for using AI:

  * Develop and deploy ML models in a secure and governed environment by using [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform). Features like model explainability and fairness metrics can help to address responsible-AI concerns.
  * Leverage the security analytics and operations capabilities of [Google Security Operations](https://cloud.google.com/security/products/security-operations), which uses AI and ML to analyze large volumes of security data, detect anomalies, and automate threat response. These capabilities help to enhance your overall security posture and aid in compliance monitoring.
  * Establish clear governance policies for AI and ML development and deployment, including security and ethics-related considerations.
  * Align with the elements of the [Secure AI Framework (SAIF)](https://developers.google.com/machine-learning/resources/saif), which provides a practical approach to address the security and risk concerns of AI systems.
  * Track the accuracy and effectiveness of AI-powered fraud detection systems, the reduction in false positives in security alerts, and the efficiency gains from AI-driven security automation.



## Meet regulatory, compliance, and privacy needs

Financial services are subject to a vast array of regulations, including data residency requirements, specific audit trails, and data protection standards. To ensure that sensitive data is properly identified, protected, and managed, FS organizations need robust data governance policies and data classification schemes. Consider the following recommendations to help you meet regulatory requirements:

  * Set up data boundaries in Google Cloud for sensitive and regulated workloads by using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview). Doing so helps you to meet government and industry-specific compliance requirements such as [FedRAMP](https://www.fedramp.gov/) and [CJIS](https://www.fbi.gov/services/cjis).
  * Identify, classify, and protect sensitive data, including financial information, by implementing [Sensitive Data Protection](https://cloud.google.com/security/products/sensitive-data-protection). Doing so helps you to meet data privacy regulations like [GDPR](https://gdpr-info.eu/) and [CCPA](https://oag.ca.gov/privacy/ccpa).
  * Track details of administrative activities and access to resources by using [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit). These logs are crucial for meeting audit requirements that are stipulated by many financial regulations.
  * When you choose [Google Cloud regions](https://docs.cloud.google.com/compute/docs/regions-zones) for your workloads and data, consider local regulations that are related to data residency. Google Cloud global infrastructure lets you choose regions that can help you to meet your data residency requirements.
  * Manage the keys that are used to encrypt sensitive financial data at rest and in transit by using [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service). Such encryption is a fundamental requirement of many security and privacy regulations.
  * Implement the controls that are necessary to address your regulatory requirements. Validate that the controls work as expected. Get the controls validated again by an external auditor to prove to the regulator that your workloads are compliant with the regulations.



## Prioritize security initiatives

Given the breadth of security requirements, financial institutions must prioritize initiatives that are based on risk assessment and regulatory mandates. We recommend the following phased approach:

  1. **Establish a strong security foundation** : Focus on the core areas of security, including identity and access management, network security, and data protection. This focus helps to build a robust security posture and helps to ensure comprehensive defense against evolving threats.
  2. **Address critical regulations** : Prioritize compliance with key regulations like PCI DSS, GDPR, and relevant national laws. Doing so helps to ensure data protection, mitigates legal risks, and builds trust with customers.
  3. **Implement advanced security** : Gradually adopt advanced security practices like zero trust, AI-driven security solutions, and proactive threat hunting.



[ Previous arrow_back  Operational excellence  ](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/operational-excellence)

[ Next Reliability  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/reliability)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
