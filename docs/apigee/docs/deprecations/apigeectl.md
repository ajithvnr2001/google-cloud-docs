---
url: https://docs.cloud.google.com/apigee/docs/deprecations/apigeectl/
title: apigeectl deprecation \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:14.300632+00:00
---

# apigeectl deprecation  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/deprecations/apigeectl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  apigeectl deprecation Stay organized with collections  Save and categorize content based on your preferences. 

The command line tool used for installation and management of containerized Apigee runtime services, `apigeectl`, is deprecated as of April 17, 2024: 

  * `apigeectl` is not supported for use with Apigee hybrid v1.12.
  * Support for `apigeectl` in Apigee hybrid v1.10 and v1.11 will end in April of 2025.



To prepare for the deprecation of `apigeectl` for _all_ Apigee hybrid versions, take steps to migrate to [Helm](https://helm.sh/) at your earliest convenience. Helm provides native Kubernetes integration, a robust ecosystem of supporting tools, and additional [benefits](https://cloud.google.com/blog/products/api-management/apigee-hybrid-now-uses-helm-charts-for-configuration). Helm support was added in Apigee hybrid v1.11.

Migration to Helm does not require down time. To complete the migration: 

  * Upgrade to Apigee hybrid v1.11, if you have not already done so.
  * Use the [migration tool](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-migration) to migrate Apigee hybrid to Helm from `apigeectl`.



## Shutdown schedule

The following table lists the shutdown schedule for `apigeectl`: 

Date | Event  
---|---  
April 17, 2024 | `apigeectl` command line interface deprecated for Apigee hybrid v1.12.  
April 17, 2024 | Support for `apigeectl` in Apigee hybrid in v1.10 and v1.11 extended for one year.  
April 17, 2025 | Support for `apigeectl` shut down for all Apigee hybrid versions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
