---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-enable-pre-trained-apis/
title: Provision GPUs and enable Vertex AI pre-trained APIs \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:39.391607+00:00
---

# Provision GPUs and enable Vertex AI pre-trained APIs  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-enable-pre-trained-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Provision GPUs and enable Vertex AI pre-trained APIs Stay organized with collections  Save and categorize content based on your preferences. 

Each Vertex AI service requires different computing resources, including graphics processing units (GPUs), as described in [Capacity planning and computing requirements](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-overview#capacity). This page describes how to provision GPU resources to run artificial intelligence (AI) and machine learning (ML) workloads in a GPU environment. This page also walks you through enabling the Vertex AI pre-trained APIs on Google Distributed Cloud (GDC) air-gapped appliance so you can start implementing Vertex AI capabilities.

Most tasks to configure GPU resources and enable or deactivate Vertex AI pre-trained APIs require administrator access. If you lack the necessary permissions, ask your administrator to enable GPUs and the Vertex AI pre-trained APIs on your behalf.

Vertex AI on GDC air-gapped appliance includes three APIs, one for each of its pre-trained models. To learn more about these pre-trained models, see the following documentation:

  * **Optical Character Recognition (OCR)** : [Learn about character recognition features](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ocr).
  * **Speech-to-Text** : [Learn about speech recognition features](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-stt).
  * **Vertex AI Translation** : [Learn about translation features](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-translation).



Use the GDC console to enable, deactivate, and view the endpoints of the Vertex AI pre-trained APIs.

## Before you begin

To get the permissions that you need to enable pre-trained APIs, ask your Organization IAM Admin or Project IAM Admin to grant you the AI Platform Admin (`ai-platform-admin`) role in the project namespace.

For information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ao-permissions). To learn how to grant permissions to a subject, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings).

Follow these steps to provision GPUs before enabling the pre-trained APIs:

  1. [Set up a project to use Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-set-up-project).
  2. Ensure that your project has the adequate ingress communication configured.
  3. [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/deploy-gpu-container-workloads).
  4. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in). If you can't sign in, see [Recover device if identity provider is unavailable](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/recover-idp).



## Enable pre-trained APIs

You can enable the OCR, Speech-to-Text, and Vertex AI Translation pre-trained APIs using the GDC console.

**Caution:** GDC air-gapped appliance includes a single NVIDIA A100 80GB GPU. This limits the device to running only _one_ GPU-dependent Vertex AI pre-trained API at a time. If you attempt to enable both Vertex AI Translation and OCR, the second API will fail to enable with an error message indicating insufficient GPU resources. You can, however, run Speech-to-Text alongside either Vertex AI Translation or OCR, as Speech-to-Text only requires CPU resources.

After meeting the prerequisites, follow these steps to enable the pre-trained APIs:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in).
  2. In the navigation menu, click **Vertex AI** > **Pre-trained APIs**.
  3. On the **Pre-trained APIs** page, click **Enable** on a specific service to enable that API.

**Note:** The GDC console doesn't display the buttons to enable the pre-trained APIs if you don't have the correct permissions.
  4. In the confirmation dialog, click **Enable**. A progress message displays.




The enablement duration varies. It might take between 15 and 45 minutes to finish.

If you want to view the status of the pre-trained APIs, [view the service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status).

**Note:** You can't enable an API while you wait for another API to finish deactivating.

## Deactivate pre-trained APIs

You can deactivate the OCR, Speech-to-Text, and Vertex AI Translation pre-trained APIs using the GDC console.

After meeting the prerequisites, follow these steps to deactivate the pre-trained APIs:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in).
  2. In the navigation menu, click **Vertex AI** > **Pre-trained APIs**.
  3. On the **Pre-trained APIs** page, click **Disable** on a specific service to deactivate that API.

**Note:** The GDC console doesn't display the buttons to deactivate the pre-trained APIs if you don't have the correct permissions.
  4. In the confirmation dialog, enter `disable` in the text field to confirm that you want to take that action. Then, click **Disable**. A progress message displays.




If you want to view the status of the pre-trained APIs, [view the service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status).

**Note:** You can't deactivate an API while you wait for another API to finish enabling.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
