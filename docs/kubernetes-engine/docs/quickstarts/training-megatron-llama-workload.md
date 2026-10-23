---
url: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/training-megatron-llama-workload/
title: Train Llama2 with Megatron-LM on A3 Mega virtual machines \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:33.098107+00:00
---

# Train Llama2 with Megatron-LM on A3 Mega virtual machines  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/training-megatron-llama-workload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Train Llama2 with Megatron-LM on A3 Mega virtual machines

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

## Overview

In this quickstart, you learn how to run a container-based, [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) PyTorch workload on [A3 Mega](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms). The code is available on this GitHub repository: [megatron-gke](https://github.com/GoogleCloudPlatform/ai-infra-cluster-provisioning/tree/main/sample_workloads/megatron-gke).

## Before you begin

Take the following steps to enable the Google Kubernetes Engine (GKE) API:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the GKE API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  8. Make sure that you have the following role or roles on the project: roles/container.admin, roles/compute.networkAdmin, roles/iam.serviceAccountUser 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



## Create an A3 Mega cluster

Create a A3 Mega GKE cluster with GPUDirect-TCPXO and multi-networking. For more information, see [Maximize GPU network bandwidth with GPUDirect and multi-networking](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx).

## Set up your environment

  1. Create environment variables for some common parameters
         
         export CLUSTER_NAME=CLUSTER_NAME
         export CONTROL_PLANE_LOCATION=CONTROL_PLANE_LOCATION
         export PROJECT_ID=PROJECT_ID
         

Replace the following:

     * `CLUSTER_NAME`: the name of your A3 Mega GKE cluster that has GPUDirect-TCPXO and multi-networking enabled.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
     * `PROJECT_ID`: your Google Cloud project ID.
  2. Configure the Google Cloud CLI to use your Google Cloud credentials for authentication:
         
         gcloud auth login
         

For more information, see [Authenticate for the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate).

  3. Install `kubectl` and the GKE gcloud CLI plugin:
         
         sudo apt-get install kubectl
         sudo apt-get install google-cloud-cli-gke-gcloud-auth-plugin
         

  4. Fetch credentials for your GKE cluster:
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} \
           --location=${CONTROL_PLANE_LOCATION} \
           --project=${PROJECT_ID}
         

  5. If not already installed, install [Helm](https://helm.sh/):
         
         curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
         chmod 700 get_helm.sh
         ./get_helm.sh && rm get_helm.sh
         sudo chmod +x /usr/local/bin/helm
         




## Use topology-aware scheduler to deploy your Pods

You can use the topology-aware scheduler to deploy your GKE Pods to nodes that have a specified GPU topology.

In the following `kubectl` commands, you will use the files directly from a repository. Alternatively, you can clone the repository locally and the `kubectl` commands can reference the local files instead.

For more information, see [Topology scheduler](https://github.com/GoogleCloudPlatform/container-engine-accelerators/tree/master/gpudirect-tcpxo/topology-scheduler).

  1. Set up the service account:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpxo/topology-scheduler/service-account.yaml
         

  2. Install the topology scheduler scripts in a configmap:
         
         curl -OL  https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpxo/topology-scheduler/schedule-daemon.py
         curl -OL  https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpxo/topology-scheduler/label-nodes-daemon.py
         
         kubectl -n kube-system create configmap topology-scheduler-scripts \
             --from-file=schedule-daemon.py=schedule-daemon.py \
             --from-file=label-nodes-daemon.py=label-nodes-daemon.py
         

  3. Install the topology label daemonset and topology scheduler Pod:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpxo/topology-scheduler/label-nodes-daemon.yaml
         $ kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpxo/topology-scheduler/schedule-daemon.yaml
         

  4. Observe the actions of the topology scheduler:
         
         kubectl -n kube-system logs topology-scheduler-pod
         




## Run the workload

### Build the Dockerfile and push to the Google Cloud Artifact Registry

  1. Create a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) and a [Docker repository](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images). In the `scripts/setup-and-configure-resources.sh script`, replace the bucket and repository names with the ones you created, and then run the script:
         
         bash scripts/setup-and-configure-resources.sh
         

  2. Build and push the `pytorch-megatron:23.11-py3` image to your repository. Ensure the Docker repository name in the `scripts/build-and-push-docker-image.sh` file matches the repository name you used in the `scripts/setup-and-configure-resources.sh` script. You can also edit the Docker image tag name before pushing.
         
         bash scripts/build-and-push-docker-image.sh
         

**Note:** This image is based off of `nvcr.io/nvidia/pytorch:23.11-py3` with minimal changes.



### Launch Megatron-LM Llama2 benchmark

  1. Edit the `helm/values.yaml` file to specify your Cloud Storage bucket and Docker image created in previous sections. For some example configurations, see [sample-configurations](https://github.com/GoogleCloudPlatform/ai-infra-cluster-provisioning/tree/main/sample_workloads/megatron-gke/sample-configurations).

  2. Optional: You can also edit the `selected-configuration.sh` file to specify any changes you made to the default Helm configuration.
         
         helm install HELM_EXPERIMENT_NAME helm/ --values helm/values.yaml
         

Replace `HELM_EXPERIMENT_NAME` with an arbitrary name for your experiment.

**Note:** If you want to run the Helm experiment multiple times, you can either erase the existing experiment using the `helm uninstall` command or you can create a new experiment with a different name.



The experiment writes metrics from the [Nsight Systems profiling tool](https://docs.nvidia.com/nsight-systems/2020.3/profiling/index.html) to the Cloud Storage bucket specified in the `megatron-experiments` directory.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the GKE cluster:

Go to the **Clusters** page:

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  1. Select the checkbox for CLUSTER_NAME.
  2. Click delete **Delete**.
  3. To confirm deletion, type CLUSTER_NAME and click **Delete**.



### Delete the Cloud Storage bucket

Go to the **Buckets** page:

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  1. Select the checkbox for the Cloud Storage bucket you created for this quickstart.

  2. Click delete **Delete**.

  3. To confirm deletion, type `DELETE` and click **Delete**.




## What's next

  * [Learn more about using GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
