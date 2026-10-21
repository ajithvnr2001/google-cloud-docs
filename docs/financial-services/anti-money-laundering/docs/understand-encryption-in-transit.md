---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-encryption-in-transit/
title: Understand encryption in transit \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:06.928043+00:00
---

# Understand encryption in transit  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-encryption-in-transit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Understand encryption in transit Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information on how your data is protected while data moves between your site and the cloud provider or between two services in the context of AML AI.

  * Internal Google services, including those used by AML AI, generally use [ALTS](https://docs.cloud.google.com/docs/security/encryption-in-transit/application-layer-transport-security). ALTS is similar in concept to mTLS but has been optimized for Google's data center environments. In some cases, TLS is used.
  * External communications to financialservices.googleapis.com (the AML AI endpoint) uses TLS to the Google Front End (GFE). The GFE ensures that all TLS connections are terminated with correct certificates and that all best practices are followed. Traffic between the GFE and financialservices.googleapis.com is internal and is encrypted with ALTS.
  * Traffic from a VM on Google Cloud to the GFE is encrypted with TLS. By default, this traffic uses external IP addresses but can use internal IP addresses using [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).
  * mTLS can be configured using [BeyondCorp Enterprise](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-resources-with-certificate-based-access). Because a [VPC-SC access level](https://docs.cloud.google.com/chrome-enterprise-premium/docs/create-cba-access-levels) must be configured, see documentation on [VPC-SC in AML AI](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/vpc-service-controls). The mTLS specific endpoint must be used, financialservices.mtls.googleapis.com.



For more details, see [encryption in transit in Google Cloud](https://docs.cloud.google.com/docs/security/encryption-in-transit).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
