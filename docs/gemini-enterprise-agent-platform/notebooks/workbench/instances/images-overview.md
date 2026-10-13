---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/images-overview/
title: Agent Platform Workbench images \u00a0|\u00a0 Gemini Enterprise Agent Platform Workbench \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:30.969890+00:00
---

# Agent Platform Workbench images  |  Gemini Enterprise Agent Platform Workbench  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/images-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform Workbench ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances)
  * [ Notebooks ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Agent Platform Workbench images

Every Gemini Enterprise Agent Platform Workbench instance runs on an image that Google builds and maintains. The image determines the operating system, the Python version, the preinstalled ML frameworks (such as TensorFlow and PyTorch), the GPU and CUDA stack, and the JupyterLab environment your instance starts with.

Agent Platform Workbench provides two types of mutually exclusive images:

  * **VM images** : Google-built boot images that install the operating system, frameworks, kernels, and JupyterLab directly on the instance host.
  * **Custom containers** : a Google-provided base container image that you can extend with your own packages, kernels, and JupyterLab configuration. Your container runs on a Google-managed host. Use custom containers for reproducible, pre-provisioned environments that you reuse across many instances.



To compare the two image types and choose one, see Choose an image type.

## Choose an image type

Use the following table to choose the type that fits your workflow. For details about the contents, versions, and lifecycle of each image, see [Image versioning and lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/image-versioning).

Option | VM images | Custom containers  
---|---|---  
What it is | A Google-built boot image that installs the operating system, frameworks, kernels, and JupyterLab directly on the instance host. | A Google-provided base container that runs on a Google-managed host.  
Operating system | Debian | Host: Container-Optimized OS (COS), managed by Google  
Container: Ubuntu  
How you customize | Add packages and micromamba environments to a running instance. The image itself is Google-managed and immutable.  | Build a custom container image ahead of time and reuse it across many instances.  
Host access | Full access to the instance host. | The COS host is Google-managed and not modifiable.  
Best for | The default experience; workloads that need host access or custom system processes. | Customized environments that you can deploy at scale.  
How to create | [Create an instance with a specific version](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-specific-version) | [Create an instance with a custom container](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-custom-container)  
  
## Agent Platform Workbench VM images

Agent Platform Workbench VM images are private images, built by Google, that provision the required packages and kernels directly onto the host machine. Agent Platform Workbench supports Debian-based VM images. A VM installs directly on the instance host, so you can interact with the host machine.

To create an instance on a specific VM image version, see [create an instance with a specific image version](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-specific-version).

## Agent Platform Workbench custom containers

A custom container lets you bring a customized image to Agent Platform Workbench instances using a Docker container. Use a custom container to ship custom packages, kernels, and a ready-made JupyterLab environment without building them at instance startup.

You start from a Google-provided base container image, extend it with what you need, and then provision Agent Platform Workbench instances from the container that you build. Google publishes two variants of the base container image:

  * **Standard: supports all Agent Platform Workbench features**. Includes pre-installed data science packages, CUDA libraries, Google Cloud JupyterLab integrations (BigQuery and Managed Service for Apache Spark), common system packages, and micromamba-based kernel management.
  * **Slim** : a minimal base image with JupyterLab, metadata-based JupyterLab configuration, and micromamba-based kernel management. You install any additional packages or extensions.



Your container runs on a Google-managed host, based on Container-Optimized OS (COS), that provides features such as idle shutdown, the proxy agent, and service telemetry. For more information, see [Container-Optimized OS features and benefits](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits).

For the base image URIs, sizes, and supported Python versions, see [Create a custom container](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-custom-container). For constraints, see [Custom container limitations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-custom-container#limitations).

## Pre-installed packages

Agent Platform Workbench images can be configured to include the following:

  * Specific ML frameworks (for example, TensorFlow and PyTorch) and their supporting packages.
  * Python with common data science packages such as numpy, scipy, matplotlib, pandas, nltk, pillow, scikit-image, opencv-python, and scikit-learn, among many others.
  * JupyterLab notebook environments for quick prototyping.
  * NVIDIA packages, including the NVIDIA driver, CUDA, cuDNN, and NCCL, for GPU-enabled instances.



## What's next

  * [Image versioning and lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/image-versioning): See what each image contains, how versions are numbered, and when images are deprecated.
  * [Manage image versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/manage-image-versions): Create an instance on a specific version, upgrade, and roll back.
  * [Image release notes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/release-notes-image): See what changed in each image release.
  * [Support policy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/support-policy): Learn about CVE handling, packages, support windows, and deprecation notice.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
