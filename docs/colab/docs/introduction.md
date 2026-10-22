---
url: https://docs.cloud.google.com/colab/docs/introduction/
title: Introduction to Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:11.095670+00:00
---

# Introduction to Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/introduction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to Colab Enterprise

Colab Enterprise is a collaborative, managed notebook environment with the security and compliance capabilities of Google Cloud.

## Get started

To get started using Colab Enterprise, try any of the following:

  * **Quickstart** : To create your first Colab Enterprise notebook and learn how to run its code on a default runtime, see [Quickstart: Create a Colab Enterprise notebook](https://docs.cloud.google.com/colab/docs/create-console-quickstart).

  * **Notebook gallery** : The notebook gallery is a curated collection of notebooks to help you get started using Colab Enterprise. See the [notebook gallery](https://console.cloud.google.com/agent-platform/colab/notebook-gallery). These notebooks use ready-to-use templates and examples to make it easier to learn new techniques, to understand best practices, and to get projects started quickly. Browse the notebooks by category, or use the search bar to find a notebook that helps you get started.




## Share and collaborate

Colab Enterprise lets you share notebooks (IPYNB files) and collaborate with others. You can share a notebook with a single user, Google group, or Google Workspace domain. You control this access through Identity and Access Management (IAM).

Learn how to [grant access to a notebook](https://docs.cloud.google.com/colab/docs/manage-access-notebook).

## Managed compute

Colab Enterprise lets you work in notebooks without having to manage infrastructure. Colab Enterprise provisions a runtime for you when you need it. If you want to, you can configure runtimes for specific needs, but Colab Enterprise starts them for you and shuts them down when you no longer need them.

## Configurable runtimes

Use the default runtime or configure your own by creating a runtime template. When you create a runtime template, you can choose between any available machine type, add accelerators, and specify your disk space.

By using runtimes that you configured, you can run code on the runtime that meets your needs at the moment. For example, you can test your code with a small dataset by using a runtime with a smaller, cost-effective machine type. Then you can use a runtime with more processing power when you need to run your code with more data.

To learn more, see [Runtimes and runtime templates](https://docs.cloud.google.com/colab/docs/runtimes).

## Integrated with Agent Platform and BigQuery

Colab Enterprise's integrations with Google Cloud services make it easier to use notebooks that interact with those services.

Colab Enterprise is a part of Gemini Enterprise Agent Platform. Colab Enterprise's API methods are a subset of the Agent Platform API. This can save you time when you're managing access to Colab Enterprise resources or when you authenticate and authorize your notebook code to use Agent Platform.

To learn more, see the [API usage overview](https://docs.cloud.google.com/colab/docs/reference).

Colab Enterprise is embedded within the UI of its integrated services. This lets you do work in Agent Platform and BigQuery, and then continue your work in a notebook without leaving their areas of the Google Cloud console. For example, you can create a notebook directly from the BigQuery editor, populated with a sample query to help you get started. To learn more, see BigQuery's [Introduction to notebooks](https://docs.cloud.google.com/bigquery/docs/notebooks-introduction).

## Write and edit code with Gemini assistance

You can use Gemini in Colab Enterprise, which is a product in the [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) portfolio, to help you write and generate code in a Colab Enterprise notebook. Gemini in Colab Enterprise can also help you fix errors in your code. To learn more, see [Write code with Gemini assistance](https://docs.cloud.google.com/colab/docs/use-code-completion).

## Idle shutdown

To help manage costs, Colab Enterprise runtimes shut down when they're inactive for a specific time period. You can change the amount of time or turn this feature off.

For more information, see [Idle shutdown](https://docs.cloud.google.com/colab/docs/idle-shutdown).

## Run code that interacts with Google Cloud services and APIs

By default Colab Enterprise notebooks use your user credentials to authenticate and authorize code that interacts with other Google Cloud services.

This means that the notebook's code has the same level of access to Google Cloud that the user does. This makes it easier to write and run code that interacts with Google Cloud services.

For more information, see [Run code that interacts with Google Cloud](https://docs.cloud.google.com/colab/docs/run-code-adc).

## Schedule notebook runs

You can schedule a notebook to run immediately for one time, or on a recurring schedule. Colab Enterprise stores the results in Cloud Storage for you to review and share with others. For more information, see [Schedule a notebook run](https://docs.cloud.google.com/colab/docs/schedule-notebook-run).

## Use with customer-managed encryption keys (CMEK)

By default, Google Cloud automatically [encrypts data when it is at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) using encryption keys managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use customer-managed encryption keys (CMEK) with your Colab Enterprise runtimes, notebooks, and the Data Science Agent. For more information, see [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/colab/docs/cmek).

## Access Transparency

Colab Enterprise supports Access Transparency. Access Transparency provides you with logs that capture the actions Google personnel take when accessing your content. You can enable Access Transparency for a Google Cloud project, if the project resides in an organization. See [Enabling Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable).

For more information about Access Transparency, see [Overview of Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview).

## Reserve VM resources

Use [Compute Engine reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) to gain a high level of assurance that your Colab Enterprise runtimes have enough virtual machine (VM) resources to run.

Reservations are a Compute Engine feature. They help make sure that you have the resources available to create VMs with the same hardware (memory and vCPUs) and optional resources (GPUs and Local SSD disks) whenever you need them.

For more information, see [Use reservations](https://docs.cloud.google.com/colab/docs/reservations).

## Colab Enterprise is different from Colab

Colab Enterprise is different from [Colaboratory](https://colab.google/), which is still available. Both have specific advantages that can be helpful depending on your needs. See the main differences in the following table:

Component | Colab Enterprise | Colab  
---|---|---  
Storage | Regional storage in Dataform | Google Drive storage, regionalized storage not supported  
Access control | Managed by IAM | Managed through Google Drive sharing functionality  
Security and networking | Google Cloud security and network functionality | Google Drive-based security, with the internet always available  
Support | Google Cloud support | Send feedback or report a bug  
  
## Limitations

Consider the following limitations of Colab Enterprise when planning your project:

  * The file size of imported notebooks is limited to approximately 20 MB. Working with a notebook that is near the size limit can impact performance.



See also [Quotas and limits](https://docs.cloud.google.com/colab/docs/quotas).

## What's next

  * [Create a Colab Enterprise notebook](https://docs.cloud.google.com/colab/docs/create-console-quickstart).

  * Learn more about [runtimes and runtime templates](https://docs.cloud.google.com/colab/docs/runtimes).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
