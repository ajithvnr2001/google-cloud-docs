---
url: https://docs.cloud.google.com/dialogflow/docs/support/faq/
title: FAQ \u00a0|\u00a0 Dialogflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:29.021630+00:00
---

# FAQ  |  Dialogflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/docs/support/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Support ](https://docs.cloud.google.com/dialogflow/docs/support)



Send feedback 

#  FAQ Stay organized with collections  Save and categorize content based on your preferences. 

## When using Dialogflow, do I have to purchase or license any third party software or hardware?

No. However, when using a third-party integration, the third party may require purchasing or licensing.

## Can Dialogflow applications be deployed on-premise?

Yes. The Dialogflow service itself cannot be deployed on-premise; however, your on-premise applications can access the Dialogflow cloud service. You can also host a webhook service on-premise, but it must be accessible through a public URL.

## Why does the first request or initial request after a period of inactivity take longer?

Authentication access tokens need to be refreshed when an API client is first used. For Dialogflow ES, see [Session client reuse](https://docs.cloud.google.com/dialogflow/docs/best-practices#session-client-reuse) to minimize the delays. In addition, a cold agent that has not received recent requests, may respond slower than a warm agent that is in active use. You can keep an agent warm by sending traffic to it periodically.

## When using a paid edition, are initial requests available at no charge, before charges start to apply?

Dialogflow CX has a [$0 trial period](https://cloud.google.com/products/conversational-agents/pricing#cx-trial). Once the $0 trial has ended, or if you are using Dialogflow ES, all requests incur charges according to [pricing](https://cloud.google.com/products/conversational-agents/pricing).

## Some features have price brackets for monthly request counts. Is the final charge based only on the total number of requests, or is it possible for multiple brackets to apply as the month goes on?

The final billed rate is based only on the total number of monthly requests for the given feature.

## What happens when quotas are exceeded?

Requests are rejected. See [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview).

## How to set alerts for quotas?

See [Set up quota alerts and monitoring](https://docs.cloud.google.com/docs/quotas/monitor).

## Does Dialogflow allow enforcement and control of user or application authentication and authorization rules?

Yes.

  * For developer-user or application access to the Dialogflow console and API, see information on [Dialogflow ES access control](https://docs.cloud.google.com/dialogflow/es/docs/access-control) and [Dialogflow CX access control](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-control%22).

  * For fulfillment with an application, see authentication information for the [Dialogflow ES webhook service](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook) and [Dialogflow CX webhook service](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook).

  * For end-user access, Dialogflow doesn't authenticate end-users. Your system or third party integration is responsible for the management of end-user authentication, authorization, and credentials.




## Does Dialogflow support standard authentication models to authenticate users?

Yes, OAuth 2.0 is supported. See the details for [authentication](https://docs.cloud.google.com/docs/authentication) and [roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Can security and operational administrative rights be segregated?

Yes. See information on [Dialogflow ES access control](https://docs.cloud.google.com/dialogflow/es/docs/access-control) and [Dialogflow CX access control](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-control).

## Are end-user messages encrypted at rest?

Yes. See [Encryption at rest](https://cloud.google.com/security/encryption/default-encryption).

Data that passes through third party integrations may be handled differently. See the third party's terms of service, privacy policy, and security policy.

## Are end-user messages encrypted in transit?

Yes. See [Encryption in transit](https://cloud.google.com/security/encryption-in-transit/).

Data that passes through third party integrations may be handled differently. See the third party's terms of service, privacy policy, and security policy.

## Can administrators audit end-user conversations?

Yes. You can log all end-user conversations in BigQuery, control where the data is stored, and control data access with IAM.

## Does Dialogflow reinforce internal security practices with rigorous third party external penetration testing?

Yes. Google coordinates external third party penetration testing using qualified and certified penetration testers. See the [Whitepaper](https://cloud.google.com/security/whitepaper).

## How is end-user data stored?

Text conversations sent to Dialogflow are saved to internal systems for storage. However, you can turn off conversation history storage and, optionally, store conversations elsewhere.

For Dialogflow ES, audio conversations are only stored if you opt in to [Data logging and enhanced speech models](https://docs.cloud.google.com/dialogflow/docs/data-logging).

Data that passes through third party integrations may be handled differently. See the third party's terms of service, privacy policy, and security policy.

For more information, see [Security, privacy, and cloud compliance](https://cloud.google.com/security).

## Does Dialogflow contain any backdoor access that can bypass security?

No.

## Does Dialogflow provide audit logs?

Yes. See [Cloud audit logs](https://docs.cloud.google.com/logging/docs/audit).

## What facility is available for producing reports from logging files?

Dialogflow leverages Google's Stackdiver service. Logs can be [exported](https://docs.cloud.google.com/logging/docs/export) for analysis.

## Does any data get stored on mobile devices?

Not by Dialogflow. Mobile developers and third party integrations can choose to store Dialogflow data as needed.

## Can Dialogflow securely handle PII and PCI information?

Dialogflow can be integrated with [Google's Data Loss Prevention API](https://docs.cloud.google.com/sensitive-data-protection/docs) to handle PII, PCI, and sensitive data to inspect, mask, and redact data as needed.

## What Dialogflow ES features have not been implemented for Dialogflow CX?

The following features found in Dialogflow ES are not implemented for Dialogflow CX:

  * [Knowledge connectors](https://docs.cloud.google.com/dialogflow/es/docs/knowledge-connectors)
  * [History](https://docs.cloud.google.com/dialogflow/es/docs/history)
  * [Training data import](https://docs.cloud.google.com/dialogflow/es/docs/training)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
