---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/add-environment/
title: Add a conda environment to a Agent Platform Workbench instance \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:45:12.965738+00:00
---

# Add a conda environment to a Agent Platform Workbench instance  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/add-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Notebooks ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/overview)



Send feedback 

#  Add a conda environment to a Agent Platform Workbench instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to add a conda environment to your Gemini Enterprise Agent Platform Workbench instance.

## Overview

When you add a conda environment to your Agent Platform Workbench instance, it appears as a [kernel](https://jupyterlab.readthedocs.io/en/stable/user/documents_kernels.html) in your instance's JupyterLab interface.

You might add a conda environment to your Agent Platform Workbench instance to use kernels that aren't available in Agent Platform Workbench instances. For example, you can add conda environments for R and Apache Beam. Or you can add conda environments for specific earlier versions of the available frameworks, such as TensorFlow, PyTorch, or Python.

## Before you begin

If you haven't already, [create a Agent Platform Workbench instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-console-quickstart).

## Open JupyterLab

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances?project=)

  2. Next to your Agent Platform Workbench instance's name, click **Open JupyterLab**.

Your Agent Platform Workbench instance opens JupyterLab.




## Add a conda environment

You can add a conda environment by entering commands in your instance's JupyterLab terminal.

  1. In JupyterLab, select **File > New > Terminal**.

  2. In the **Terminal** window, enter the following commands:
         
         # Creates a conda environment.
         conda create -n CONDA_ENVIRONMENT_NAME -y
         conda activate CONDA_ENVIRONMENT_NAME
         
         # Install packages using a pip local to the conda environment.
         conda install pip
         pip install PACKAGE
         pip install ipykernel
         
         # Adds the conda kernel.
         DL_ANACONDA_ENV_HOME="${DL_ANACONDA_HOME}/envs/CONDA_ENVIRONMENT_NAME"
         python -m ipykernel install --prefix "${DL_ANACONDA_ENV_HOME}" --name CONDA_ENVIRONMENT_NAME --display-name KERNEL_DISPLAY_NAME

Replace the following:

     * `CONDA_ENVIRONMENT_NAME`: your choice of name for the environment
     * `PACKAGE`: the package that you want to install
     * `KERNEL_DISPLAY_NAME`: the display name for the tile of the kernel in the JupyterLab interface
  3. A default kernel can be created when installing to a given conda environment. You can remove the default kernel with the following command:
         
         rm -rf "/opt/micromamba/envs/CONDA_ENVIRONMENT_NAME/share/jupyter/kernels/python3

  4. To see your new kernel, do the following:

     1. Refresh the page.

     2. Select **File > New Launcher**.

The kernel is listed among the others in the **Launcher** window.




By default, conda might use pip packages in the system `pip` folder (for example, `/usr/bin/pip`). Running `conda install pip` ensures that the setup uses a pip local to the environment.

## Example installation: R Essentials

The following example installs R Essentials in a conda environment named `r`.
    
    
    conda create -n r
    conda activate r
    conda install -c r r-essentials

## Example installation: pip package

The following example installs pip packages from a `requirements.txt` file.
    
    
    conda create -n myenv
    conda activate myenv
    conda install pip
    pip install -r requirements.txt
    pip install ipykernel
    DL_ANACONDA_ENV_HOME="${DL_ANACONDA_HOME}/envs/myenv"
    python -m ipykernel install --prefix "${DL_ANACONDA_ENV_HOME}" --name myenv --display-name myenv

## Troubleshoot

To diagnose and resolve issues related to adding a conda environment, see [Troubleshooting Agent Platform Workbench](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/troubleshooting-workbench#pip-packages-missing-instances).

## What's next

  * Learn more about [conda](https://docs.conda.io/en/latest/).

  * To modify your conda environment, see [Manage your conda environment](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/manage-environment).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
