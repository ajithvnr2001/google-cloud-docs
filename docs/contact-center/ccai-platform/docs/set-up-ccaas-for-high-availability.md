---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-ccaas-for-high-availability/
title: Set up CCAI Platform for high availability \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:52.752964+00:00
---

# Set up CCAI Platform for high availability  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-ccaas-for-high-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Set up CCAI Platform for high availability Stay organized with collections  Save and categorize content based on your preferences. 

This document provides strategies and best practices for ensuring high availability (HA) for your contact center operations. Communications Platform as a Service (CPaaS) providers are central to achieving HA.

## CCAI Platform and the role of CPaaS

CCAI Platform provides isolated customer environments that rely on external CPaaS providers to deliver voice and chat services. High availability is achieved by ensuring stable connections to these providers and establishing clear signaling paths to your CCAI Platform instances. Primary partners include the following:

  * **Twilio.** Powers the chat infrastructure and provides call services.
  * **Vonage and Telnyx.** Provide additional call infrastructure.



## Understanding the risks: a case study

A major customer reported that approximately 3% of calls failed to connect. Investigation revealed that the CPaaS provider (Twilio) received a dynamic IP address from its cloud host that was previously flagged for malicious activity. Consequently, the customer's security software (Netskope) blocked the IP, preventing agents from connecting to the media stream. This highlights the risk of selecting individual IP addresses for allowlisting instead of using domain-based rules.

## High availability strategies

To mitigate the risk of outages, implement a layered HA strategy covering network readiness, telephony redundancy, and regional architecture.

### Infrastructure and network readiness

High availability starts with a stable connection to CCAI Platform. You must ensure the following:

  * **Hybrid allowlisting (domain and IP).** To mitigate the risks of rotating dynamic IP addresses, as demonstrated in Understanding the risks: a case study, add CPaaS providers to an allowlist by domain—for example, `*.twilio.com`. Most **Session Border Controllers (SBCs)** don't support domain names and require IP Access Control Lists (ACLs). Therefore, use domain-based rules where possible, and use full IP range allowlists where necessary—for example, `168.86.128.0/18`.
  * **Private Service Connect ([PSC](https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-psc)).** For enhanced security and reliability, use private ingress domains (for example, `.p.ccaiplatform.com`) to route agent traffic directly using the Google Cloud backbone. For more information, see [Create a CCAI Platform instance](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started#create-ccaip-instance).

  * **VDI and VPN support.** If your agents use a Virtual Desktop (VDI), ensure **Browser content redirection** is enabled to maintain audio and connection stability.




### Standard providers versus Bring Your Own Carrier (BYOC)

You have two primary ways to manage your telephony connectivity:

  * **Standard (managed) providers.** CCAI Platform manages the relationship with providers like Twilio or Vonage. Redundancy is handled at the platform level, but you are dependent on the platform's failover timeline.
  * **Bring Your Own Carrier (BYOC).** You can use your own telephony providers. This lets you achieve _carrier redundancy_ —configuring multiple SIP trunks across different carriers so that traffic can be rerouted instantly if one carrier fails.



In the event of a primary provider outage, failing over to a new provider (for example, porting numbers) can take significant time and coordination. Pre-planned redundancy using BYOC provides a robust defense.

## Best practices for high availability

This section contains best practices that can help you improve the availability of your contact center and mitigate risks associated with third-party providers and environmental factors.

### Telephony best practices

  * **E.164 standard.** Ensure that your SBC formats all phone numbers to the E.164 international standard (for example, `+14155551234`). This is critical to correctly preserve the original caller's ANI during call transfers.



### Monitoring and observability

Proactive monitoring is essential for early detection of issues that standard signaling might miss. See the following examples of proactive monitoring:

  * **Integrate status pages.** Monitor public status pages such as `status.twilio.com` or `seti.telnyx.com` (for Telnyx opaque-box testing results).
  * **Cloud monitoring and logging.** Set up custom alerts in your Google Cloud project for spikes in call failure rates or increased latency at the regional level.
  * **CCAI Platform observability toolkit.** Use the open-source [CCaaS Observability Toolkit](https://github.com/GoogleCloudPlatform/ccaas-observability) on GitHub for prebuilt dashboards to monitor CCAI Platform and [virtual agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent).



### Operational alignment and data reporting

Managing multiple instances requires specific operational processes to prevent configuration drift and ensure data visibility. This includes the following:

  * **Configuration alignment.** Manually synchronize all administrative settings (queues, user profiles, and routing rules) across both primary and secondary instances to ensure identical behavior during failover.
  * **Unified data reporting.** Implement an ETL (Extract, Transform, Load) process to aggregate data from all active instances into a centralized tool for a comprehensive view of performance.
  * **Prepare for manual failover.** If a service impact is confirmed using status pages or internal probers, be prepared to manually reroute 100% of traffic to an alternative provider's SIP FQDN.



### Integration robustness

  * **Resilient[call recordings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recording).** Enable the **Skip CRM Account Lookup** setting in your instance to ensure call recordings are successfully uploaded to storage even if CRM ticket creation fails. For more information, see [Skip CRM account and record creation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/skip-crm-account-record-creation).
  * **Environment management.** Configure [Conversation Profiles](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent) to point to a specific **Published Environment ID** rather than the **Draft** environment to ensure predictable behavior for your [virtual agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent).



### Agent environment and workflow

Google recommends doing the following:

  * **Single instance policy.** Enforce a policy where agents have only one instance of the agent adapter (one tab or window) open at a time to prevent socket and connection conflicts.
  * **Browser permissions.** Ensure all agents have **Microphone** and **Notification** permissions enabled in their browser for the CCAI Platform URL.
  * **Standardize configurations.** Maintain a standard, tested version of Google Chrome and monitor for experimental browser flags that might affect WebRTC performance.
  * **Security visibility.** Maintain real-time monitoring of all active internal firewall and security rules (for example, blocklists) to rule out internal causes for connection issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
