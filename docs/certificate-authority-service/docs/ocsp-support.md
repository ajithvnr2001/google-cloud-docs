---
url: https://docs.cloud.google.com/certificate-authority-service/docs/ocsp-support/
title: Implement a delegated OCSP responder \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:37.321311+00:00
---

# Implement a delegated OCSP responder  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/ocsp-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Implement a delegated OCSP responder

This page contains a sample provided for demonstration purposes. Google does not officially support this sample. We recommend that you carefully evaluate any solution before deploying it in your production environment. 

This document provides information about the Online Certificate Status Protocol (OCSP) responder that you can use to check the revocation status of certificates issued using Certificate Authority Service. For more information about the tool, see [OCSP responder for CA Service](https://github.com/googlecloudplatform/gcp-ca-service-ocsp).

## What is Online Certificate Status Protocol (OCSP)?

[OCSP](https://wikipedia.org/wiki/Online_Certificate_Status_Protocol) is a protocol for obtaining the revocation status for an X.509 certificate. When a user requests information about the validity of a certificate, a request is sent to an OCSP responder. The OCSP responder checks the status of the certificate with a trusted certificate authority (CA) and sends back an OCSP response.

## Why use a delegated OCSP responder?

Tracking certificate revocation status using OCSP can have many benefits. These include quicker response time and smaller requirement for network bandwidth, as compared to Certificate Revocation Lists (CRLs), which can get quite large.

## How does the OCSP responder work?

The OCSP responder pre-generates an OCSP response for each certificate that a particular CA issues. The pre-generated responses are saved as individual files in a Cloud Storage bucket.

You can deploy a Cloud Run service that regenerates these files on-demand or on a schedule. The Cloud Run service is essentially the _frontend_ for the OCSP server.

You can use [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) to forward requests to Cloud Run and cache OCSP responses. For more information, see [Setting up Cloud CDN with Cloud Run](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-serverless).

For instructions about configuring an OCSP responder with CA Service, see the [README: OCSP responder for CA Service](https://github.com/GoogleCloudPlatform/gcp-ca-service-ocsp/blob/master/README.md).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
