---
url: https://docs.cloud.google.com/secure-web-proxy/docs/troubleshoot-tls-inspection-errors/
title: Troubleshoot TLS inspection errors \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:04.503452+00:00
---

# Troubleshoot TLS inspection errors  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/troubleshoot-tls-inspection-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Troubleshoot TLS inspection errors Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to diagnose and resolve common issues that might occur when you [enable TLS inspection for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).

## TLS inspection is enabled but traffic is blocked

To fix this issue, do the following:

  1. Make sure that you have granted the necessary Identity and Access Management (IAM) permissions to the [service account](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection#create-service-account) in your Google Cloud project so that it can access the Certificate Authority Service.

  2. Verify that you have defined a valid `ApplicationMatcher` by using the [CEL matcher language](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference) to correctly identify the traffic for decryption.

  3. Check that your client devices trust the [certificate authority (CA) pool](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool) your Secure Web Proxy instance uses; without this trust, connections can be terminated with SSL/TLS handshake errors.




## What's next

  * [Secure Web Proxy release notes](https://docs.cloud.google.com/secure-web-proxy/docs/release-notes)
  * [Secure Web Proxy support](https://docs.cloud.google.com/secure-web-proxy/docs/getting-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
