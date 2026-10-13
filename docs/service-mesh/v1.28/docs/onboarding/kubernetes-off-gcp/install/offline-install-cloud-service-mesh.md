---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/offline-install-cloud-service-mesh/
title: Prepare an offline installation of Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:57.487960+00:00
---

# Prepare an offline installation of Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/offline-install-cloud-service-mesh/

You are viewing v1.28 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prepare an offline installation of Cloud Service Mesh

This page explains how to prepare offline installations of Cloud Service Mesh on [supported platforms](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-platforms) other than GKE on Google Cloud.

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview).

When running the `asmcli` tool to [install Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh), it uses a local directory to store configuration and artifacts. By default, a temporary directory is created when executing the tool. However, you can specify a directory using the `--output_dir` option on the command line. If the directory already exists with the necessary configuration and artifacts, they will be reused instead of re-downloading anything.

To perform an offline installation of Cloud Service Mesh, you can generate a configuration package on a machine with Internet access, and then distribute that package to other machines without internet access. Then, use the subcommand `asmcli build-offline-package` to generate configuration packages.

## Before you begin

Before you begin, make sure that you:

  * Review [the prerequisites](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/cloud-service-mesh-prerequisites).
  * Review the information in [Plan the install](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/plan-install).
  * [Install the required tools](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#install_required_tools).
  * [Download `asmcli`](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/install-dependent-tools#download_asmcli).
  * During installation, ensure access to [Google APIs and Services](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid) is possible, or manually enable the required dependencies. Even in offline mode, `asmcli` uses Google Cloud CLI to enable some dependencies if the corresponding flag is passed during installation.



## Offline installation of Cloud Service Mesh

The following outlines how to prepare an offline installation of Cloud Service Mesh:

  1. On the machine with Internet access that you installed Cloud Service Mesh, create a package and then save it to the folder OFFLINE_PKG_DIR_PATH:
         
         ./asmcli build-offline-package \
         --output_dir OFFLINE_PKG_DIR_PATH
         

**Note:** The `offline-package` includes critical hidden files. You must copy all of the files to the offline machine. To avoid missing files, create an archive bundle of the entire `output_dir` and copy it to the offline machine.
  2. Copy the configuration directory and `asmcli` tool to the offline machine.

  3. Follow the normal instructions for [installing Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh). Wherever the instructions specify to run `asmcli install`, ensure that you also pass the `--offline` flag and specify the configuration directory created in the previous steps:
         
         ./asmcli install \
           --output_dir OFFLINE_PKG_DIR_PATH \
           --project_id PROJECT_ID \
           --cluster_location CLUSTER_LOCATION \
           --cluster_name CLUSTER_NAME \
           --offline
         




## What's next?

  * Learn about [setting up a multi-cluster mesh outside of Google Cloud](https://docs.cloud.google.com/service-mesh/v1.28/docs/operate-and-maintain/off-gcp-multi-cluster-setup).

  * [Configure an external IP address on-premises](https://docs.cloud.google.com/service-mesh/v1.28/docs/operate-and-maintain/external-ip-load-balance).

  * [Deploy the Online Boutique sample application](https://docs.cloud.google.com/service-mesh/v1.28/docs/onlineboutique-install-kpt).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
