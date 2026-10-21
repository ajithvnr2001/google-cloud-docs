---
url: https://docs.cloud.google.com/certificate-authority-service/docs/trust-model/
title: Trust model \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:57:13.935451+00:00
---

# Trust model  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/trust-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Trust model

## Background

In a typical Web Public Key Infrastructure (PKI), millions of clients across the world trust a set of independent certificate authorities (CAs) to assert identities (such as domain names) in certificates. As part of their responsibilities, CAs commit to only issuing certificates when they have independently validated the identity in that certificate. For example, a CA typically needs to verify that somebody requesting a certificate for the domain name `example.com` actually controls the said domain before they issue a certificate to them. Since those CAs can issue certificates for millions of customers where they might not have an existing direct relationship, they are limited to asserting identities that are publicly verifiable. Those CAs are limited to certain well-defined verification processes that are consistently applied across the Web PKI.

Unlike Web PKI, a private PKI often involves a smaller CA hierarchy, which is directly managed by an organization. A private PKI sends certificates only to clients that inherently trust the organization to have the appropriate controls (for example, machines owned by that organization). Since the CA admins often have their own ways of validating identities for which they issue certificates (for example, issuing certificates to their own employees), they aren't limited by the same requirements as for Web PKI. This flexibility is one of the main advantages of private PKI over Web PKI. A private PKI enables new use-cases such as securing internal websites with short domain names without requiring unique ownership of those names, or encoding alternative identities formats (such as [SPIFFE IDs](https://spiffe.io/docs/latest/spiffe/concepts/#spiffe-id)) into a certificate.

Certificate Authority Service aims to simplify the process of managing private PKI by allowing you to easily create and manage CAs. As such, CA Service does not define how identities in certificates must be validated. However, CA Service provides a robust set of policy controls that allows fine-grained configuration of CA pools. For more information, see [Policy controls](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls).

## What's next

  * Learn more about [policy controls](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls).
  * Learn how to [configure IAM policies](https://docs.cloud.google.com/certificate-authority-service/docs/configuring-iam).
  * Learn how to [use an issuance policy](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
