---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/slurm-custom-images/
title: Build custom Slurm Docker images \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:43:48.593758+00:00
---

# Build custom Slurm Docker images  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/slurm-custom-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Build custom Slurm Docker images Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — Slurm Operator add-on for GKE**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to build custom Docker images for your Slurm clusters on Google Kubernetes Engine (GKE). You can extend the base Slurm images provided by GKE to include additional tools, libraries, or configurations required for your high performance computing (HPC) workloads.

Before reading this document, ensure that you're familiar with the [Slurm Operator add-on for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/concepts/overview).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Prerequisites

This document assumes that you already have a Slurm cluster running on GKE with Slurm Operator add-on for GKE installed. Complete the procedures on the following pages:

  1. Complete the [Quickstart: Deploy a Slurm cluster on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke).
  2. Configure an [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images) repository in your project to store your custom images.



## Slurm base images

GKE provides base Slurm images in the [gcr.io/gke-release/](https://console.cloud.google.com/artifacts/docker/gke-release/us/gcr.io/slinky%2Fslurmd) Artifact Registry repository. GKE updates these images frequently for security and performance. These images come in variants that include the latest Slurm versions and two Linux distributions, Ubuntu and Rocky Linux.

You can customize the following base images:

  * `gcr.io/gke-release/slinky/slurmd`: used for Slurm compute nodes.
  * `gcr.io/gke-release/slinky/login`: used for login nodes.



## Build a custom image

The following example demonstrates how to build a custom Slurm compute image that includes a Python virtual environment with JAX installed. You also build a corresponding login image that mirrors the compute image `PATH` environment variable without actually installing the JAX libraries.

### Select the image version

When you select a base image, ensure that it meets the following conditions:

  * The version matches the Slurm version used by other components in your Slurm cluster.
  * For a specific Slurm version, choose the tag of the newest available image, which includes the latest security updates and bug fixes.



For example, if the default Slurm version in your cluster is 25.11, you should choose a tag that starts with `25.11-`, for example `25.11-ubuntu24.04-gke.6`.

### Create a Dockerfile

  1. Select an Ubuntu-based `slurmd` image tag:

     1. In the Google Cloud console, go to the **Artifact Registry repository** page that includes the `slinky/slurmd` package.

[Go to Artifact Registry repository](https://console.cloud.google.com/artifacts/docker/gke-release/us/gcr.io/slinky%2Fslurmd)

     2. Find an image with a tag that includes `ubuntu` and matches your Slurm version, for example `25.11-ubuntu24.04-gke.6`.

     3. Copy the tag. You use this tag to replace the `VERSION_TAG` placeholder in the following configuration file.

  2. Create a file named `Dockerfile` with the following content:
         
         # --- Target 1: The Worker Node (slurmd) ---
         FROM gcr.io/gke-release/slinky/slurmd:VERSION_TAG AS slurmd-custom
         USER root
         
         # Install minimal requirements for venv
         RUN apt-get update && apt-get install -y --no-install-recommends \
             python3-pip \
             python3-venv \
             && rm -rf /var/lib/apt/lists/*
         
         # Create and populate the virtual environment
         ENV VIRTUAL_ENV=/opt/custom_venv
         RUN python3 -m venv ${VIRTUAL_ENV}
         ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
         
         # Install JAX (CPU version for general compatibility) and dependencies
         RUN pip install --no-cache-dir jax[cpu] numpy
         
         # --- Target 2: The Login Node ---
         FROM gcr.io/gke-release/slinky/login:VERSION_TAG AS login-custom
         USER root
         
         # Mirror the PATH exactly so that the srun command captures it.
         # Note: You don't need to install the JAX libs here,
         # but the binary path must exist for the shell to recognize it.
         ENV VIRTUAL_ENV=/opt/custom_venv
         ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
         
         # Create the directory structure so the PATH is valid on the login node
         RUN mkdir -p ${VIRTUAL_ENV}/bin
         

Replace the `VERSION_TAG` with the Slurm version tag that matches your cluster's default Slurm version.

  3. Build the images by using the `docker build` command:
         
         docker build --target=slurmd-custom \
             -t AR_PATH/slinky/slurmd:CUSTOM_SLURMD_TAG \
             -f Dockerfile .
         docker build --target=login-custom \
             -t AR_PATH/slinky/login:CUSTOM_LOGIN_TAG \
             -f Dockerfile .
         

Replace the following:

     * `AR_PATH`: the path to your Artifact Registry repository, for example `gcr.io/my-project`.
     * `CUSTOM_SLURMD_TAG`: a `slurmd-custom` tag name of your choice.
     * `CUSTOM_LOGIN_TAG`: a `login-custom` tag name of your choice.
  4. Push the custom images to your repository:
         
         docker push AR_PATH/slinky/slurmd:CUSTOM_SLURMD_TAG
         docker push AR_PATH/slinky/login:CUSTOM_LOGIN_TAG
         




## Use the custom images in GKE

**Note:** This section assumes you are using the [Quickstart: Deploy a Slurm cluster on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke) to deploy a Slurm cluster.

To use your custom images, complete the following steps:

  1. As shown in the following example, update the image repository and tag for the `slurmd` nodeset and `login` loginset by modifying the `values.yaml` file:
         
         nodesets:
             slinky:
                 replicas: 1
                 slurmd:
                     image:
                         repository: AR_PATH/slinky/slurmd
                         tag: CUSTOM_SLURMD_TAG
         
         loginsets:
             slinky:
                 enabled: true
                 replicas: 1
                 login:
                     image:
                         repository: AR_PATH/slinky/login
                         tag: CUSTOM_LOGIN_TAG
         

  2. Upgrade the existing deployment:
         
         helm upgrade slurm oci://ghcr.io/slinkyproject/charts/slurm \
             --namespace slurm \
             --version=1.0.2 \
             -f values.yaml
         

  3. Test the new capabilities of your compute node by signing in to the login node and running the following `srun` command:
         
         srun python3 -c "
         import sys
         import jax
         import jax.numpy as jnp
         
         print(f'Python Executable: {sys.executable}')
         print(f'Using JAX backend: {jax.devices()[0].platform}')
         
         key = jax.random.PRNGKey(42)
         x = jax.random.normal(key, (5000, 5000))
         result = jnp.dot(x, x)
         print(f'Matrix multiplication successful. Shape: {result.shape}')
         "
         

The output is similar to the following:
         
         Python Executable: /opt/custom_venv/bin/python3
         Using JAX backend: cpu
         Matrix multiplication successful. Shape: (5000, 5000)
         

This output confirms that Slurm executes the script on worker Pods running your custom image, and the image contains the required Python and JAX capabilities.




## Clean up

To clean up the resources that you used in this tutorial, do the following:

  1. Uninstall the Helm deployment: `sh helm uninstall slurm --namespace slurm`

This command removes all Kubernetes resources deployed by the Helm chart.

  2. Delete the Slurm namespace:
         
         kubectl delete namespace slurm
         

  3. Delete the GKE cluster:
         
         gcloud container clusters delete CLUSTER_NAME
         

Replace `CLUSTER_NAME` with your cluster name.

  4. Delete the custom images from Artifact Registry:
         
         gcloud container images delete AR_PATH/slinky/slurmd:CUSTOM_SLURMD_TAG --force-delete-tags
         gcloud container images delete AR_PATH/slinky/login:CUSTOM_LOGIN_TAG --force-delete-tags
         

  5. Remove the custom images from your local Docker environment:
         
         docker rmi AR_PATH/slinky/slurmd:CUSTOM_SLURMD_TAG
         docker rmi AR_PATH/slinky/login:CUSTOM_LOGIN_TAG
         




## What's next

  * Explore the [Slurm Project on GitHub](https://github.com/SlinkyProject/slurm-operator).
  * Learn how to [enable the Slurm Operator add-on for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/enable-slurm-operator-addon).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
