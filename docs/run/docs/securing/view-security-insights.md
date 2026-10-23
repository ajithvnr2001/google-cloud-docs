---
url: https://docs.cloud.google.com/run/docs/securing/view-security-insights/
title: View software supply chain security insights \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:52:04.413798+00:00
---

# View software supply chain security insights  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/securing/view-security-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  View software supply chain security insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view the software supply chain security insights for a selected Cloud Run revision, and provides brief details to help you understand what this information reveals about the security posture of the revision.

To learn how you can use Cloud Run with other Google Cloud products and features to improve the security posture of your software supply chain, see [Software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).

## Before you begin

You must enable Container Scanning API for container scanning.

[Enable the Container Scanning API](https://console.cloud.google.com/apis/library/containerscanning.googleapis.com)

## Required permissions

To view security insights, you need the following roles:

  * Artifact Analysis Occurrences Viewer
  * Cloud Run Viewer



## View security insights

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click the service to open the **Service details** page.

  3. Click the **Revision history** tab.

  4. Select the revision you want to view the security insights of.

  5. Click the **Security** tab in the details panel at the right.

  6. Locate the **Software supply chain security insights** section to view the vulnerability rating and other related details. For more information, see Understanding security insights.




## Understanding security insights

The **Security insights** section displays the following information:

  * Supply-chain Levels for Software Artifacts (SLSA) level: Identifies the maturity level of your software build process in accordance with the SLSA specification. You can find more details at the [SLSA ](https://slsa.dev/spec/v1.0/levels) website.
  * Vulnerabilities: An overview of any vulnerabilities found in your artifacts, and the name of the image that Artifact Analysis has scanned. You can click the image name to view vulnerability details.
  * Build details: Details of the build such as the builder and the link to view logs.
  * Build provenance: [Provenance](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-builds#provenance) for the build.



## What's next

  * For higher SLSA levels, consider setting up [continuous deployment](https://docs.cloud.google.com/run/docs/continuous-deployment-with-cloud-build).
  * For an example that deploys a Cloud Run service and leads you through the security insights for that service, see the [software supply chain security quickstart](https://docs.cloud.google.com/software-supply-chain-security/docs/quickstarts/deploy-run-view-security-insights).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
