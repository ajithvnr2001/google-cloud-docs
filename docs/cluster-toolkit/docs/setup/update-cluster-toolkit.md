---
url: https://docs.cloud.google.com/cluster-toolkit/docs/setup/update-cluster-toolkit/
title: Update Cluster Toolkit version \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:08.613336+00:00
---

# Update Cluster Toolkit version  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/setup/update-cluster-toolkit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Update Cluster Toolkit version Stay organized with collections  Save and categorize content based on your preferences. 

To update Cluster Toolkit, you upgrade the [`gcluster` command-line tool](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster). Cluster Toolkit is an open-source software from Google that deploys high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) environments on Google Cloud. Updating Cluster Toolkit helps ensure that you have access to the latest features and bug fixes. Be aware that most updates only require upgrading the tool, but fundamental architectural changes might require you to redeploy your cluster after updating it.

## Overview

To update Cluster Toolkit, you must upgrade the `gcluster` command-line tool. If software or hardware configurations need to be changed, then you also need to re-deploy your cluster.

Before you update the software, consider the following important points:

  * **Immutable fields** : Many aspects of your cluster configuration are immutable after creation. You can't change these fields without re-deploying the cluster.
  * **Backup** : Before making any significant changes or re-deployments, ensure you have proper backups of your data and configurations.



### Update the `gcluster` command-line tool

To update Cluster Toolkit, install the latest version of the command-line tool.

###  Cloud Shell or Linux

To update Cluster Toolkit on Cloud Shell or Linux, download the latest prebuilt binary bundle. For instructions, see [Install the prebuilt bundle](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment#install-bundle).

###  macOS 

To update on macOS, download the latest prebuilt binary bundle. For instructions, see [Install the prebuilt bundle](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment#install-bundle).

###  Windows 

To update on Windows, pull the latest changes from the GitHub repository and rebuild the binary as follows:

  1. Go to the toolkit directory where you originally cloned the repository:
         
         cd cluster-toolkit
         

  2. Pull the updates from the upstream repository:
         
         git pull
         

**Note:** If you have made local changes that conflict with the latest updates, then a prompt with a request to resolve them appears.
  3. Rebuild the `gcluster` command-line tool:
         
         make
         




This command compiles and replaces the previous executable with the updated version. This step is necessary to incorporate new features and bug fixes.

### Redeploy the cluster

For basic changes to a running cluster, like adding or removing a partition or resizing an existing one, you can edit and redeploy the cluster blueprint.

For instructions, see the documentation for your environment:

  * For Compute Engine and Slurm: [Reconfigure a running cluster](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/reconfigure-cluster)
  * For Google Kubernetes Engine: [Reconfigure a GKE cluster](https://docs.cloud.google.com/cluster-toolkit/docs/gke/reconfigure-gke-cluster)



To modify the hardware infrastructure, change immutable properties of the cluster, or if Cluster Toolkit software has a major change, then follow these steps:

  1. Delete the existing cluster.

     1. Remove all compute nodes in the cluster. The process for removing compute nodes depends on your environment:

### Compute Engine and Slurm

For Compute Engine and Slurm environments:

        * See [Manage static compute nodes](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/manage-static-nodes). You can use the following command to gracefully drain and power down nodes:
              
              scontrol update NodeName=NODES_TO_UPDATE State=POWER_DOWN_ASAP

        * Alternatively, you can configure the `cleanup_compute_nodes` setting on the Slurm controller to automatically destroy static compute nodes when the cluster is destroyed. 

### Google Kubernetes Engine

For Google Kubernetes Engine environments:

        * See [Reconfigure a GKE cluster](https://docs.cloud.google.com/cluster-toolkit/docs/gke/reconfigure-gke-cluster) for instructions on managing nodes within a GKE cluster.

     2. Use the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy) to tear down the old deployment:

**Warning** : The destroy command is irreversible. Make sure you can recreate the cluster before running this command.
            
            ./gcluster destroy DEPLOYMENT_FOLDER_NAME --auto-approve
            

  2. Update the cluster blueprint with any needed changes.

  3. Use the [`gcluster create` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-create) to create a new cluster deployment folder based on the updated blueprint, using the `-w` flag to overwrite the previous deployment.
         
         ./gcluster create BLUEPRINT_NAME -w
         

  4. Use the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to deploy the new cluster.
         
         ./gcluster deploy DEPLOYMENT_FOLDER_NAME
         




## What's next

  * [Cluster blueprint overview](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint)
  * [Best practices for running HPC workloads](https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/best-practices)
  * [Deploy an HPC cluster with Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/slurm-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
