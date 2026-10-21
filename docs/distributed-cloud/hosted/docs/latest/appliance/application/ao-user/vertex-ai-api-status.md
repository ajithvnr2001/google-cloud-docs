---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status/
title: View service status and endpoints \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:13.473449+00:00
---

# View service status and endpoints  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  View service status and endpoints Stay organized with collections  Save and categorize content based on your preferences. 

You use pre-trained API endpoints to interact with Vertex AI services programmatically. For example, you need the endpoint when interacting with a pre-trained API from the command-line interface.

Follow these steps to view the status and endpoints of the Optical Character Recognition (OCR), Speech-to-Text, and Vertex AI Translation pre-trained APIs:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in).
  2. In the navigation menu, click **Vertex AI** > **Pre-trained APIs**.
  3. On the **Pre-trained APIs** page, you can review the following information:

     * View the status of each pre-trained API on the central panel. The status is either **Enabled** or **Not enabled**. If the status is **Not enabled** , you can enable the corresponding API. For more information, see [Provision GPUs and enable Vertex AI pre-trained APIs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-enable-pre-trained-apis).

     * If the status of an API is **Enabled** , you can view its endpoint on the central panel. To use this endpoint for programmatically interacting with the Vertex AI service, click content_copy **Copy** to copy it to your clipboard.




If the system fails to enable the API, the page displays information to help you troubleshoot the issue.

**Caution:** GDC air-gapped appliance includes a single NVIDIA A100 80GB GPU. This limits the device to running only _one_ GPU-dependent Vertex AI pre-trained API at a time. If you attempt to enable both Vertex AI Translation and OCR, the second API will fail to enable with an error message indicating insufficient GPU resources. You can, however, run Speech-to-Text alongside either Vertex AI Translation or OCR, as Speech-to-Text only requires CPU resources.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
