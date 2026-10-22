---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/troubleshoot/
title: Troubleshoot issues \u00a0|\u00a0 Certificate Manager (2nd gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:32.595591+00:00
---

# Troubleshoot issues  |  Certificate Manager (2nd gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback 

#  Troubleshoot issues Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides troubleshooting steps for common issues that you might encounter with Certificate Manager (2nd gen).

## Certificate not visible in the inventory

This issue occurs when you view your certificate inventory, but a certificate is missing.

To resolve this issue, do the following:

  * If you recently enabled the Certificate Manager API or issued a certificate, certificates can take up to 24 hours to persist in the inventory. Certificate Manager attempts to persist certificates as quickly as possible.
  * Verify that you're viewing the inventory in the same Google Cloud project where the Certificate Authority, Managed Workload Identity pool, or certificate-issuing resource resides. Certificate Manager displays only the relevant certificates for the scope of the Google Cloud project that you're viewing.
  * Certificate Manager displays only certificates from networking resources like load balancers, certificates issued from Certificate Authority Service, and certificates issued from Managed Workload Identity. Certificates issued from other providers or integrations might not appear. To suggest new sources, click the **Send feedback** button on this page.



## Lifecycle management update operations fail

This issue occurs when you attempt to update resources, such as Managed Workload Identity pools or target proxies, using lifecycle management, and the operation fails.

To resolve this issue, do the following:

  * Verify that you have the correct Identity and Access Management permissions to edit the configuration of the target resources.
  * Because some lifecycle management operations can fail intermittently, wait a few minutes and attempt the update operation again.



## Overview metrics don't match the inventory

This issue occurs when you view the certificate overview metrics and notice that they don't match the statistics in the certificate inventory.

To resolve this issue, check the certificate inventory for the most up-to-date view of your certificates. The analytics that evaluate the certificate inventory can lag behind the real-time status by up to 24 hours, which can cause the overview statistics to be temporarily out of date.

## What's next

  * [Audit logging](https://docs.cloud.google.com/certificate-manager/docs/v2/audit-logging)
  * [Monitor resources using Cloud Monitoring](https://docs.cloud.google.com/certificate-manager/docs/v2/cloud-monitoring)
  * [View certificate inventory](https://docs.cloud.google.com/certificate-manager/docs/v2/inventory)
  * [Monitor your certificates](https://docs.cloud.google.com/certificate-manager/docs/v2/monitor)
  * [Compare Certificate Manager versions](https://docs.cloud.google.com/certificate-manager/docs/v2/comparison)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
