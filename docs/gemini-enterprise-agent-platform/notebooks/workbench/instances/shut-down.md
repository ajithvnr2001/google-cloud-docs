---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/shut-down/
title: Shut down a Agent Platform Workbench instance \u00a0|\u00a0 Gemini Enterprise Agent Platform Workbench \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:27:33.972145+00:00
---

# Shut down a Agent Platform Workbench instance  |  Gemini Enterprise Agent Platform Workbench  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/shut-down/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform Workbench ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances)
  * [ Notebooks ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Shut down a Agent Platform Workbench instance

To stop any processing for a Agent Platform Workbench instance, you can shut down the instance.

You incur costs for running an instance, in addition to other potential costs (see [Pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing#notebooks)). To stop incurring costs for running an instance, shut down the instance. You continue to incur other potential costs.

To shut down a Agent Platform Workbench instance, complete the following steps:

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances?project=)

  2. Select the instance that you want to open.

  3. Click **Open JupyterLab**.

It is important to stop all running processes in case there are operations that need to complete before you shut down your Agent Platform Workbench instance, for example, I/O processes that are writing to disk.

To stop all running processes:

     1. To show all of the processes that are running, select the ![](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/notebooks/workbench/images/icon-running-terminals.png) **Running Terminals and Kernels** tab.

     2. Next to each running process, click **Shutdown all**.

  4. Close the browser tab or window for your Agent Platform Workbench instance.

  5. In the Google Cloud console, return to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances?project=)

  6. Select the instance that you want to shut down, and then click square **Stop**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
