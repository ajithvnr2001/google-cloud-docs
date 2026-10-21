---
url: https://docs.cloud.google.com/sap/docs/rise-overview/
title: Overview of RISE with SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:45.897024+00:00
---

# Overview of RISE with SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/rise-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Overview of RISE with SAP on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview about the RISE with SAP program on Google Cloud and outlines the architecture for integrating your SAP solutions managed under the RISE program with your on-premise systems and Google Cloud services.

## About RISE with SAP

[RISE with SAP](https://www.sap.com/products/erp/rise.html) is a managed service offering from SAP for hosting ERP systems such as S/4HANA Cloud, Private Edition. It provides a holistic service that includes business process intelligence, the underlying business platform, analytics, and managed cloud infrastructure. The core value of RISE is that SAP maintains responsibility for the holistic service level agreement (SLA), cloud operations, and technical support for the SAP application layer.

According to the terms and conditions specified in [SAP product policies](https://www.sap.com/about/agreements/policies.html), under the RISE with SAP program:

  * The SAP Enterprise Cloud Service team manages the SAP S/4HANA Private Cloud environment on your behalf. This includes the Google Cloud Virtual Private Cloud (VPC), Compute Engine instances, and storage.
  * You or your implementation partner are responsible for: 
    * Managing components including on-premises systems, applications hosted in Google Cloud projects managed by your organization, and third-party SaaS solutions.
    * Establishing connectivity from these components to the Google Cloud projects managed by SAP under the RISE with SAP program.



## Architecture

The following image illustrates integrating a Google Cloud project managed under the RISE with SAP program, with on-premise systems, applications in your Google Cloud projects, Google Cloud services, and third-party SaaS solutions:

![Connect to a Google Cloud project managed under the RISE with SAP program](https://docs.cloud.google.com/static/sap/docs/images/connecting-to-rise-project.png)

As shown in the preceding diagram, connecting your on-premises network with solutions managed under the RISE with SAP program primarily involves the following components:

  * **Customer-managed infrastructure** : On-premises infrastructure that your organization manages. This lets your on-premises users connect with your SAP systems running on Google Cloud.
  * **Secured connectivity to Google Cloud** : Secured network connections to Google Cloud that you establish from your organization's infrastructure, third-party SaaS solutions, or other cloud platforms.
  * **Customer organization** : An intermediary Google Cloud project that your organization manages.
  * **SAP organization** : Google Cloud projects that SAP manages under the RISE with SAP program.



## What's next

  * [Connectivity to RISE with SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/rise-connectivity)
  * [Extensions for RISE with SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/rise-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
