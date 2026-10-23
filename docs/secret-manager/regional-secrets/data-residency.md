---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/data-residency/
title: About data residency and regional secrets \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:20.359284+00:00
---

# About data residency and regional secrets  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/data-residency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  About data residency and regional secrets Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of data residency and achieving compliance with data residency regulations using regional secrets.

## Overview of data residency

[Data residency](https://docs.cloud.google.com/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs#control_data_residency) is the concept of keeping data within specific geographical boundaries due to legal, regulatory, or organizational requirements. Data residency isn't just a preference for some businesses; it's a legal and operational necessity. Data residency is essential to comply with regulations like [GDPR](https://docs.cloud.google.com/privacy/gdpr), [HIPAA](https://docs.cloud.google.com/security/compliance/hipaa-compliance), or [PIPEDA](https://docs.cloud.google.com/security/compliance/pipeda-canada), and to mitigate the risk of fines or legal action.

To learn more about data residency in Google Cloud, see the following Identity and Security blog post: [Understanding your options for data residency, operational transparency, and privacy controls on Google Cloud](https://cloud.google.com/blog/products/identity-security/meet-data-residency-requirements-with-google-cloud/).

## Enforce data residency using regional secrets

In Secret Manager, you can enforce data residency by choosing the [regional service](https://docs.cloud.google.com/secret-manager/regional-secrets/global-regionalized-service-comparison) and creating regional secrets that ensure that your sensitive data is stored and processed within a specific location. With regional secrets, your secret data remains within the chosen location at all times, whether it's at rest, in use, or in transit.

Regional secrets work in the following manner:

  * When you create a regional secret, you specify the location where you want it to be stored. The Secret Manager service ensures that the secret data stays within that location's infrastructure.
  * Regional secrets can only be accessed by applications or services running within the same location. This adds an extra layer of security by limiting access to authorized entities within the designated region.
  * Unlike [global secrets](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart), which are often replicated across multiple locations for high availability, regional secrets are not automatically replicated. This ensures strict data residency.



## What's next

  * [Enable the Secret Manager API](https://docs.cloud.google.com/secret-manager/regional-secrets/config-sm-rs)
  * [Create a regional secret](https://docs.cloud.google.com/secret-manager/regional-secrets/create-regional-secret)
  * [Add a regional secret version](https://docs.cloud.google.com/secret-manager/regional-secrets/add-secret-version-rs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
