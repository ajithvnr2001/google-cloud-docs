---
url: https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool/
title: Overview of CA pools \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:44.990166+00:00
---

# Overview of CA pools  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Overview of CA pools

A certificate authority (CA) pool is a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy. CA pools provide the ability to rotate trust chains without any outage or downtime for their payloads.

A CA pool is empty when you create it. For information about adding a CA to a CA pool, see [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca).

The CA pool maintains a list of trusted CA certificates. You must install these trusted CA certificates with the certificate requester.

## Properties of CAs in a CA pool

The following table lists the features that must be same, can be different, and must be different for all CAs in a CA pool.

Must be same for all CAs in a CA pool | Can be different for all CAs in a CA pool | Must be different for all CAs in a CA pool  
---|---|---  
  
  * Certificate issuance policies
  * IAM conditions
  * Tier
  * Location
  * Publishing options. For example, whether to publish a CRL.

| 

  * Algorithms and sizes of signing keys
  * CA subjects and SANs
  * Expiration date and validity period
  * Labels
  * Customer-managed Cloud Storage bucket used for CRL and AIA.
  * Customer-managed CA keys
  * CA certificate extensions

| 

  * CA name

  
  
## Achieve higher QPS

Certificate Authority Service enforces [limits on the number of requests](https://docs.cloud.google.com/certificate-authority-service/quotas) you can send. For example, the usage limit for the [createCertificate](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates/create) request for a DevOps CA is 25 [QPS](https://wikipedia.org/wiki/Queries_per_second).

To increase your total effective QPS, you must have multiple CAs in a CA pool. A CA pool increases the total effective QPS by distributing the incoming certificate requests across all CAs in the `ENABLED` [state](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states). However, you can still [request certificates from a particular CA in the CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates#issue-certificate-specific-ca).

You can use the following formula to calculate the maximum allowed QPS for a CA pool:

`Total effective QPS = min(100, number of CAs in the CA pool x QPS per CA)`

For example, if the effective QPS for a CA is 25 QPS and if you create 4 CAs in a CA pool, then the total effective QPS of the CA pool is 100 QPS.

For more information about achieving a higher total effective QPS, see [Increase certificate creation throughput using a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/higher-qps).

## Manage CA rotation

A CA pool can have CAs that are in different [states](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states). A CA pool load-balances certificate issuance for workloads across the enabled CAs in a CA pool.

The CA pool abstracts the specific CAs within it that issue certificates. When a CA expires, the total effective QPS of the CA pool gets reduced. For example, if a CA pool has 4 enabled CAs, the total effective QPS for that CA pool is 100 QPS. But if one CA in the CA pool expires, the total effective QPS gets reduced to 75 QPS. To ensure that the total effective QPS of the CA pool remains unaffected when a CA expires, you must create a new CA before the existing CA expires.

For more information, see [Managing CA rotation](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-rotation).

For information about requesting an increase in quota, see [Requesting a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## What's next

  * Learn how to [work with quotas](https://docs.cloud.google.com/docs/quotas/overview).
  * Learn how to [create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).
  * Learn how to [update and delete a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/operations-ca-pool).
  * Learn how to [create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca).
  * Learn how to [request a certificate](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
