---
url: https://docs.cloud.google.com/recaptcha/docs/private-access-tokens/
title: Understand how Fraud Defense uses Private Access Tokens \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:58.048710+00:00
---

# Understand how Fraud Defense uses Private Access Tokens  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/private-access-tokens/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Understand how Fraud Defense uses Private Access Tokens Stay organized with collections  Save and categorize content based on your preferences. 

This document explains what Private Access Tokens (PATs) are and how Google Cloud Fraud Defense uses them.

## What are Private Access Tokens?

Fraud Defense uses a feature on iOS and macOS called PAT to reduce the number of CAPTCHAs that it shows to human users.

A PAT is an opaque token that some iOS and macOS devices generate. The token serves as a privacy-preserving attestation of a device's authenticity and integrity. PATs are an implementation of the Privacy Pass protocol, which is a type of [`WWW-Authenticate`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate) scheme.

## How Fraud Defense uses Private Access Tokens

Fraud Defense uses multiple factors to determine if a request comes from a human or a bot. The ability of a device to produce a PAT is one of these signals. Devices that can't produce a PAT aren't penalized.

The PAT protocol is designed to help preserve privacy. The token doesn't contain personally identifiable information that can be used to identify a specific device or user. Fraud Defense checks that the token is valid to confirm that the request comes from a genuine Apple device.

## The Private Access Token request flow

You might see the 401 error `https://www.google.com/recaptcha/api2/pat` or `https://www.recaptcha.net/recaptcha/api2/pat`. This error is an expected part of the PAT protocol. To determine if a device can produce a PAT, Fraud Defense sends a special header in a response that rejects the initial request. On compatible Apple devices, this header triggers a flow that retries the request with a PAT.

This 401 error doesn't prevent Fraud Defense from working on the page or cause other errors. When you click the checkbox or call `execute`, the reCAPTCHA Enterprise API still generates a valid token.

## What's next

To learn more about how Apple uses Private Access Tokens, see the post [Featuring Private Access Tokens](https://developer.apple.com/news/?id=huqjyh7k) on the Apple Developer blog.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
