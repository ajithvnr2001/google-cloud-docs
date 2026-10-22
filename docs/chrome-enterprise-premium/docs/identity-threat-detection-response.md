---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/identity-threat-detection-response/
title: Identity Threat Detection and Response with Context-Aware Access overview \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:00.254170+00:00
---

# Identity Threat Detection and Response with Context-Aware Access overview  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/identity-threat-detection-response/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)



Send feedback 

#  Identity Threat Detection and Response with Context-Aware Access overview Stay organized with collections  Save and categorize content based on your preferences. 

**Private Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Identity Threat Detection and Response (ITDR) with Context-Aware Access provides a dynamic layer of security that continuously assesses the user activity based risk associated with an identity's access attempt using signals from [Security Command Center Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules), such as [Excessive Permission Denied Actions](https://docs.cloud.google.com/security-command-center/docs/findings/threats/excessive-failed-attempt) and [Access from Anonymizing Proxy](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-ip-google-proxy-intel). Those signals are categorized into five user activity risk types that you can configure in the Console and APIs Access Policy.

## User Activity risk types

The following are the user activity risk types that you can add to your access policy:

  * **Suspicious actions** : Potentially malicious actions, such as removing or reducing security restrictions.

  * **Identity reputation** : Changes to account settings or state, such as changing group memberships or becoming active (non-dormant).

  * **Malicious source** : Activity from a suspicious source, such as an IP address associated with bad actors.

  * **Repeat actions** : Excessive failed access attempts, such as Identity and Access Management (IAM) denials.

  * **Atypical location** : Access from unusual locations, such as from a new geographic area.




## What's next

  * [Configure user activity in a Console and APIs Access Policy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/configure-console-and-apis-risk-policy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
