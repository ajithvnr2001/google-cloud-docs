---
url: https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis/
title: Artifact Analysis overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:11.096796+00:00
---

# Artifact Analysis overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Artifact Analysis overview Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Analysis is a family of services that provide software composition analysis, metadata storage and retrieval. Its detection points are built into a number of Google Cloud products such as Artifact Registry and Google Kubernetes Engine (GKE) for quick enablement. The service works with both Google Cloud's first-party products and also lets you store information from third-party sources. The scanning services use a common vulnerability store for matching files against known vulnerabilities.

This service was formerly known as Container Analysis. The new name does not change existing products or APIs, but reflects the product's expanding range of features beyond containers.

![Artifact Analysis in CI/CD](https://docs.cloud.google.com/static/artifact-analysis/images/aa-diagram.png)

**Figure 1.** Diagram that shows Artifact Analysis creating and interacting with metadata across source, build, storage, deployment and runtime environments.

## Registry scanning

This section outlines Artifact Analysis vulnerability scanning features based in Artifact Registry, and lists related Google Cloud products where you can enable complementary capabilities to support your security posture.

### Automatic scanning in Artifact Registry

  * The scanning process is triggered automatically every time you push a new image to Artifact Registry. The vulnerability information is continuously updated when new vulnerabilities are discovered. Artifact Registry includes application language package scanning. To get started, enable [automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/os-overview).



### Centralized risk management with Security Command Center

  * Security Command Center centralizes your cloud security, offering vulnerability scanning, threat detection, posture monitoring, and data management. Security Command Center aggregates vulnerability findings from Artifact Registry scans, allowing you to view container image vulnerabilities within your running workloads, across all projects alongside your other security risks in Security Command Center. You can also export these findings to BigQuery for in-depth analysis and long-term storage. For more information, see [Artifact Registry vulnerability assessment](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#ar-vuln-assessment).



## On-Demand scanning

  * This service is not continual; you must run a command to manually initiate the scan. Scan results are available up to 48 hours after the scan is completed. The vulnerability information is not updated after the scan is finished. You can scan images stored locally, without having to push them to Artifact Registry or GKE runtimes first. To learn more, see [on-demand scanning](https://docs.cloud.google.com/artifact-analysis/docs/os-scanning-on-demand).



## Access metadata

  * Artifact Analysis is a Google Cloud infrastructure component that lets you [store and retrieve structured metadata](https://docs.cloud.google.com/artifact-analysis/docs/metadata-management-overview) for Google Cloud resources. At various phases of your release process, people or automated systems can add metadata that describes the result of an activity. For example, you can add metadata to your image indicating that the image has passed an integration test suite or a vulnerability scan.

  * With Artifact Analysis integrated into your CI/CD pipeline, you can make decisions based on metadata. For example, you can use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) to create deployment policies that only allow deployments for compliant images from trusted registries.

  * Artifact Analysis associates metadata with images through **notes** and **occurrences**. To learn more about these concepts, see the [metadata management page](https://docs.cloud.google.com/artifact-analysis/docs/metadata-management-overview).




To learn about the costs for Artifact Analysis features, see [Artifact Analysis pricing](https://cloud.google.com/artifact-analysis/pricing).

## What's next

  * [Get started with automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/quickstart-scanning-os-automatically).
  * [Get started with On-Demand Scanning](https://docs.cloud.google.com/artifact-analysis/docs/quickstart-scanning-os-manually).
  * Learn more about [scanning concepts](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).
  * Learn more about [supported metadata types](https://docs.cloud.google.com/artifact-analysis/docs/metadata-management-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
