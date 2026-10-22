---
url: https://docs.cloud.google.com/certificate-authority-service/docs/using-identity-reflection/
title: Identity reflection for federated workloads \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:59.416030+00:00
---

# Identity reflection for federated workloads  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/using-identity-reflection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Identity reflection for federated workloads

You can use Certificate Authority Service with [workload identity pools](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools) and identity reflection to federate a third-party identity and obtain a certificate that attests to this identity.

Identity reflection is a special certificate issuance mode that limits an unprivileged certificate requester to requesting certificates with a _subject alternative name (SAN)_ corresponding to the identity in their credential. For example, an Cloud Service Mesh workload with a federated third-party identity token might be able to request a certificate with a SAN corresponding to its Mesh identity, but cannot request a certificate with any other SAN.

## What's next

  * Learn how to reflect [third-party identities](https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/using-3pi-with-reflection) using IAM workload identity federation.
  * Learn more about [SPIFFE](https://spiffe.io).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
