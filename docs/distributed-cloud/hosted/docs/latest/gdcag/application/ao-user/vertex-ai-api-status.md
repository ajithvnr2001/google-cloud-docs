---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status/
title: View service status and endpoints \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:09.742705+00:00
---

# View service status and endpoints  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  View service status and endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to check the service status and endpoints for Vertex AI within Google Distributed Cloud (GDC) air-gapped. An endpoint lets you access Vertex AI pre-trained models through their APIs using JupyterLab notebook or the command-line interface. Confirming the service status and endpoints lets you verify new deployments, troubleshoot integration issues, and monitor the operational status of AI features across your applications. 

This page is for application developers within application operator groups responsible for ensuring AI features are operational in applications running in a secure air-gapped environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

Use the following steps to view the service status of Vertex AI APIs and their endpoints:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in). If you can't sign in, see [Connect to an identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/connect-identity).
  2. In the navigation menu, click **Vertex AI** > **Pre-trained APIs**.
  3. On the **Pre-trained APIs** page, you can review the following information:

     * View the status of each pre-trained API on the central panel. The status is either **Enabled** or **Not enabled**. If the status is **Not enabled** , you can enable the corresponding API. For more information, see [Provision GPUs and enable Vertex AI APIs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-enable-pre-trained-apis).

     * If the status of an API is **Enabled** , you can view its endpoint in the service details. To use this endpoint for programmatically interacting with the Vertex AI service, click content_copy **Copy** to copy it to your clipboard.




If the system fails to enable the API, the page displays information to help you troubleshoot the issue.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
