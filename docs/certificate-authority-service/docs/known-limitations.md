---
url: https://docs.cloud.google.com/certificate-authority-service/docs/known-limitations/
title: Known limitations \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:09.114664+00:00
---

# Known limitations  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/known-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Resources ](https://docs.cloud.google.com/certificate-authority-service/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Known limitations

This page documents the known limitations of Certificate Authority Service.

## Revocation support

Certificate revocation is only supported through Certificate Revocation Lists (CRLs). Online Certificate Status Protocol (OCSP) isn't supported by CA Service, but you can implement and run a delegated OCSP responder.

For more information on implementing an OCSP responder, see [OCSP support](https://docs.cloud.google.com/certificate-authority-service/docs/ocsp-support).

## Client-generated keys

The Google Cloud CLI and Google Cloud console surfaces support automatically generating an asymmetric key-pair when issuing certificates for added convenience. Keys generated using Google Cloud CLI are limited to RSA-2048, while keys generated using Google Cloud console support a wider selection of algorithms.

## Certificate subject

CA Service only supports the following attribute types in the subject of a certificate:

  * Common Name (CN)
  * Country Code (C)
  * Organization (O)
  * Organizational Unit (OU)
  * Locality (L)
  * Province (ST)
  * Street Address
  * Postal Code



This limitation applies to the subject field in both CA certificates and end-entity certificates. Each of these attribute types is limited to only one value.

For more information, see the [Subject](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/Subject) message in the REST API documentation.

## What's next

  * Read answers to the [frequently asked questions](https://docs.cloud.google.com/certificate-authority-service/docs/faqs).
  * Learn how to [troubleshoot common issues encountered in CA Service](https://docs.cloud.google.com/certificate-authority-service/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
