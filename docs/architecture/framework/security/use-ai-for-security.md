---
url: https://docs.cloud.google.com/architecture/framework/security/use-ai-for-security/
title: Use AI for security \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:14.630578+00:00
---

# Use AI for security  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/security/use-ai-for-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Use AI for security Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-02-05 UTC

This principle in the security pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) provides recommendations to use AI to help you improve the security of your cloud workloads.

Because of the increasing number and sophistication of cyber attacks, it's important to take advantage of AI's potential to help improve security. AI can help to reduce the number of threats, reduce the manual effort required by security professionals, and help compensate for the scarcity of experts in the cyber-security domain.

## Principle overview

Use AI capabilities to improve your existing security systems and processes. You can use [Gemini in Security](https://cloud.google.com/security/ai) as well as the intrinsic AI capabilities that are built into Google Cloud services.

These AI capabilities can transform security by providing assistance across every stage of the security lifecycle. For example, you can use AI to do the following:

  * Analyze and explain potentially malicious code without reverse engineering.
  * Reduce repetitive work for cyber-security practitioners.
  * Use natural language to generate queries and interact with security event data.
  * Surface contextual information.
  * Offer recommendations for quick responses.
  * Aid in the remediation of events.
  * Summarize high-priority alerts for misconfigurations and vulnerabilities, highlight potential impacts, and recommend mitigations.



## Levels of security autonomy

AI and automation can help you achieve better security outcomes when you're dealing with ever-evolving cyber-security threats. By using AI for security, you can achieve greater levels of autonomy to detect and prevent threats and improve your overall security posture. Google defines four [levels of autonomy](https://services.google.com/fh/files/misc/google-cloud-product-vision-ai-powered-security.pdf#page=6) when you use AI for security, and they outline the increasing role of AI in assisting and eventually leading security tasks:

  1. **Manual** : Humans run all of the security tasks (prevent, detect, prioritize, and respond) across the entire security lifecycle.
  2. **Assisted** : AI tools, like Gemini, boost human productivity by summarizing information, generating insights, and making recommendations.
  3. **Semi-autonomous** : AI takes primary responsibility for many security tasks and delegates to humans only when required.
  4. **Autonomous** : AI acts as a trusted assistant that drives the security lifecycle based on your organization's goals and preferences, with minimal human intervention.



## Recommendations

The following sections describe the recommendations for using AI for security. The sections also indicate how the recommendations align with Google's Secure AI Framework (SAIF) [core elements](https://developers.google.com/machine-learning/resources/saif) and how they're relevant to the levels of security autonomy.

  * Enhance threat detection and response with AI
  * Simplify security for experts and non-experts
  * Automate time-consuming security tasks with AI
  * Incorporate AI into risk management and governance processes
  * Implement secure development practices for AI systems

**Note:** For more information about Google Cloud's overall vision for using Gemini across our products to accelerate AI for security, see the whitepaper [Google Cloud's Product Vision for AI-Powered Security](https://services.google.com/fh/files/misc/google-cloud-product-vision-ai-powered-security.pdf).

### Enhance threat detection and response with AI

This recommendation is relevant to the following [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

  * Security operations (SecOps)
  * Logging, auditing, and monitoring



AI can analyze large volumes of security data, offer insights into threat actor behavior, and automate the analysis of potentially malicious code. This recommendation is aligned with the following SAIF elements:

  * Extend detection and response to bring AI into your organization's threat universe.
  * Automate defenses to keep pace with existing and new threats.



Depending on your implementation, this recommendation can be relevant to the following levels of autonomy:

  * **Assisted** : AI helps with threat analysis and detection.
  * **Semi-autonomous** : AI takes on more responsibility for the security task.



[Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence), which uses AI to analyze threat actor behavior and malicious code, can help you implement this recommendation.

### Simplify security for experts and non-experts

This recommendation is relevant to the following [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

  * Security operations (SecOps)
  * Cloud governance, risk, and compliance



AI-powered tools can summarize alerts and recommend mitigations, and these capabilities can make security more accessible to a wider range of personnel. This recommendation is aligned with the following SAIF elements:

  * Automate defenses to keep pace with existing and new threats.
  * Harmonize platform-level controls to ensure consistent security across the organization.



Depending on your implementation, this recommendation can be relevant to the following levels of autonomy:

  * **Assisted** : AI helps you to improve the accessibility of security information.
  * **Semi-autonomous** : AI helps to make security practices more effective for all users.



Gemini in [Security Command Center](https://cloud.google.com/security/products/security-command-center) can provide summaries of alerts for misconfigurations and vulnerabilities.

### Automate time-consuming security tasks with AI

This recommendation is relevant to the following [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

  * Infrastructure security
  * Security operations (SecOps)
  * Application security



AI can automate tasks such as analyzing malware, generating security rules, and identifying misconfigurations. These capabilities can help to reduce the workload on security teams and accelerate response times. This recommendation is aligned with the SAIF element about automating defenses to keep pace with existing and new threats.

Depending on your implementation, this recommendation can be relevant to the following levels of autonomy:

  * **Assisted** : AI helps you to automate tasks.
  * **Semi-autonomous** : AI takes primary responsibility for security tasks, and only requests human assistance when needed.



Gemini in [Google SecOps](https://cloud.google.com/security/products/security-operations) can help to automate high-toil tasks by assisting analysts, retrieving relevant context, and making recommendations for next steps.

### Incorporate AI into risk management and governance processes

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance.

You can use AI to build a model inventory and risk profiles. You can also use AI to implement policies for data privacy, cyber risk, and third-party risk. This recommendation is aligned with the SAIF element about contextualizing AI system risks in surrounding business processes.

Depending on your implementation, this recommendation can be relevant to the semi-autonomous level of autonomy. At this level, AI can orchestrate security agents that run processes to achieve your custom security goals.

### Implement secure development practices for AI systems

This recommendation is relevant to the following [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

  * Application security
  * AI and ML security



You can use AI for secure coding, cleaning training data, and validating tools and artifacts. This recommendation is aligned with the SAIF element about expanding strong security foundations to the AI ecosystem.

This recommendation can be relevant to all levels of security autonomy, because a secure AI system needs to be in place before AI can be used effectively for security. The recommendation is most relevant to the assisted level, where security practices are augmented by AI.

To implement this recommendation, follow the [Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev) guidelines for AI artifacts and use validated container images.

[ Previous arrow_back  Use AI securely and responsibly  ](https://docs.cloud.google.com/architecture/framework/security/use-ai-securely-and-responsibly)

[ Next Meet regulatory, compliance, and privacy needs  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-02-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-05 UTC."],[],[]] 
