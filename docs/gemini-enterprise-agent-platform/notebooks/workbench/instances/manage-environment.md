---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/manage-environment/
title: Manage the conda environment in your Agent Platform Workbench instance \u00a0|\u00a0 Gemini Enterprise Agent Platform Workbench \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:07:32.738623+00:00
---

# Manage the conda environment in your Agent Platform Workbench instance  |  Gemini Enterprise Agent Platform Workbench  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/manage-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform Workbench ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances)
  * [ Notebooks ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage your conda environment

This page describes how to manage a conda environment in your Gemini Enterprise Agent Platform Workbench instance.

## Overview

If you've added a conda environment to your Agent Platform Workbench instance, it appears as a [kernel](https://jupyterlab.readthedocs.io/en/stable/user/documents_kernels.html) in your instance's JupyterLab interface.

You might have added a conda environment to your instance to use a kernel that isn't available in a default Agent Platform Workbench instance. This page describes how to modify and delete that kernel.

## Open JupyterLab

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances?project=)

  2. Next to your Agent Platform Workbench instance's name, click **Open JupyterLab**.

Your Agent Platform Workbench instance opens JupyterLab.




## Modify a conda kernel

Gemini Enterprise Agent Platform Workbench instances come with pre-installed frameworks such as PyTorch and TensorFlow. If you need a different version, you can modify the libraries by using pip in the relevant conda environment.

For example, if you want to upgrade PyTorch:
    
    
    # Check the name of the conda environment for PyTorch
    conda env list
    
    # Activate the environment for PyTorch
    conda activate pytorch
    
    # Display the PyTorch version
    python -c "import torch; print(torch.__version__)"
    
    # Make sure to use pip from the conda environment for PyTorch
    # This should be `/opt/conda/envs/pytorch/bin/pip`
    which pip
    
    # Upgrade PyTorch
    pip install --upgrade torch

## Delete a conda kernel

Some conda packages add default kernels to your environment when the packages are installed. For example, when you install R, conda might also add a `python3` kernel. This can cause a duplication of kernels in your environment. To avoid duplicated kernels, delete the default kernel before you create a new kernel with the same name.
    
    
    rm -rf /opt/conda/envs/CONDA_ENVIRONMENT_NAME/share/jupyter/kernels/python3

## Troubleshoot

To diagnose and resolve issues related to managing a conda environment in your Agent Platform Workbench instance, see [Troubleshooting Agent Platform Workbench](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/troubleshooting-workbench#instances).

## What's next

  * Learn more about [conda](https://docs.conda.io/en/latest/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
