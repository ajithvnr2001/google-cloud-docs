---
url: https://docs.cloud.google.com/armor/docs/adaptive-protection-use-cases/
title: Adaptive Protection use cases \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:59.463429+00:00
---

# Adaptive Protection use cases  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/adaptive-protection-use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Adaptive Protection use cases Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Armor Adaptive Protection automatically detects layer 7 (L7) distributed denial-of-service (DDoS) attacks and abusive traffic patterns. This document describes common use cases for Adaptive Protection, including using machine learning for early detection, applying suggested Web Application Firewall (WAF) rules for mitigation, and customizing models. Understanding these use cases helps you ensure service availability and minimize manual incident response.

### L7 DDoS attack detection and protection

The most common use case for Adaptive Protection is detecting and responding to L7 DDoS attacks such as HTTP GET floods, HTTP POST floods, or other high frequency HTTP activities. L7 DDoS attacks often start relatively slow and grow in intensity over time. By the time humans or automated spike detection mechanisms detect an attack, it is likely to be high in intensity and already having a strong negative impact on the application. Critically, while it is possible to observe the spiking traffic in aggregate, it is much harder to differentiate, in real time, individual requests as malicious or not because they appear as normal, fully formed requests. Similarly, since the attack sources are distributed amongst botnets or other groups of malicious clients ranging in size from thousands to millions, it becomes increasingly difficult to mitigate an ongoing attack by systematically identifying and blocking bad clients based on IP alone. In the case of DDoS, the result is that the attack is successful in making the targeted service unavailable for some or all regular users.

**Note:** Adaptive Protection is intended to detect and alert on high frequency traffic coming from single or distributed sources. Manual or automated malicious activity is not guaranteed to be detected by Adaptive Protection, particularly if the incoming traffic looks just like legitimate traffic at similar volumes.[ ![Illustration of an L7 DDoS attack \(HTTP GET flood\). A successful attack might overwhelm the targeted application and prevent legitimate users from accessing the service.](https://docs.cloud.google.com/static/armor/images/caap-http-flood-attack.svg)](https://docs.cloud.google.com/static/armor/images/caap-http-flood-attack.svg) Illustration of an L7 DDoS attack (HTTP GET flood). A successful attack might overwhelm the targeted application and prevent legitimate users from accessing the service. (click to enlarge)

To rapidly detect and respond to L7 DDoS attacks, the project or security policy owner can enable Adaptive Protection protection on a per-security policy basis in their project. After at least one hour of training and observing normal traffic patterns, Adaptive Protection will be ready to quickly and accurately detect an attack early in its lifecycle and suggest WAF rules to block the ongoing attack while leaving normal users unaffected.

[ ![Adaptive Protection identifies and mitigates an L7 DDoS attack, allowing legitimate users to access the application.](https://docs.cloud.google.com/static/armor/images/caap-detect-protect.svg)](https://docs.cloud.google.com/static/armor/images/caap-detect-protect.svg) Adaptive Protection identifies and mitigates an L7 DDoS attack, allowing legitimate users to access the application. (click to enlarge)

Notifications of potential attacks and the identified signature of the suspect traffic are sent to Logging, where the log message can trigger a custom Alerting Policy, be analyzed and stored, or be sent to a downstream security information and event management (SIEM) or log management solution. Consult the [Logging documentation](https://docs.cloud.google.com/logging/docs) for more information on how to integrate downstream SIEM or log management.

### Attack signature detection and response

It is critical to not only detect and alert on potential attacks early but also be able to act on that alert and respond in time to mitigate the attacks. An enterprise's incident responders have to spend critical minutes and hours investigating, frequently analyzing logs and monitoring systems to gather enough information to develop a response to an ongoing attack. Next, before deploying the mitigation, that plan has to be validated to make sure it won't have an unintended or negative impact on production workloads.

[ ![A common workflow for an enterprise's incident response process.](https://docs.cloud.google.com/static/armor/images/caap-incident-response.svg)](https://docs.cloud.google.com/static/armor/images/caap-incident-response.svg) A common workflow for an enterprise's incident response process. (click to enlarge)

With Adaptive Protection, incident responders have everything they need to quickly analyze and respond to an ongoing L7 DDoS attack the moment they receive the alert. The Adaptive Protection alert includes the signature of the traffic determined to be participating in the potential attack. The contents of the signature will include metadata about the incoming traffic, including the set of malicious HTTP request headers, client geographies, etc. The alert also includes a rule matching the attack signature that can be applied in Google Cloud Armor to immediately block the malicious traffic.

The Adaptive Protection event provides a confidence score and a projected impacted baseline rate associated with the suggested rule to aid in validation. Each component of the signature also has measures for attack likelihood and proportion of attack to enable incident responders to fine tune and narrow or widen the scope of the response.

### Customizing the model and reporting event errors

The Adaptive Protection attack detection models are trained on a dataset, artificially produced to exhibit the characteristics of both the good and the malicious traffic. As a result, it is possible that Adaptive Protection will identify a potential attack that, upon additional investigation, the incident responder or application owner will determine was not an attack. Adaptive Protection is able to learn from the unique context and traffic patterns of each protected application.

[ ![Example signature of a potential attack.](https://docs.cloud.google.com/static/armor/images/caap-identify-respond.svg)](https://docs.cloud.google.com/static/armor/images/caap-identify-respond.svg) Example signature of a potential attack. (click to enlarge)

You can report individual alerts as a false positive to further help Adaptive Protection train and customize the detection models. With false positive reports, Adaptive Protection models will be less likely to alert on traffic with similar characteristics and attributes in the future. Over time, the Adaptive Protection detection models will be more attuned to the specific characteristics of the traffic in each protected security policy. The steps to report false positive events were described in [Monitoring, feedback and reporting event errors](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview#monitor-%0Afeedback-report-errors).

## What's next

  * [Read more about Adaptive Protection](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
