---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-inference/
title: Serve LLMs on GKE with a cost-optimized and high-availability GPU provisioning strategy \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:12:06.161900+00:00
---

# Serve LLMs on GKE with a cost-optimized and high-availability GPU provisioning strategy  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Serve LLMs on GKE with a cost-optimized and high-availability GPU provisioning strategy Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide shows you how to optimize costs for LLM-serving workloads on GKE. This tutorial uses a combination of Flex-start VMs, Spot VMs, and ComputeClasses for cost-effective inference.

This guide uses [Mixtral 8x7b](https://mistral.ai/news/mixtral-of-experts/) as an example LLM you can deploy.

This guide is intended for Machine learning (ML) engineers, Platform admins and operators, and for Data and AI specialists who are interested in using Kubernetes container orchestration capabilities for serving LLMs. For more information about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

## Flex-start pricing

Flex-start is recommended if your workload requires dynamically provisioned resources as needed, for up to seven days with short-term reservations, no complex quota management, and cost-effective access. Flex-start is powered by Dynamic Workload Scheduler and is billed using [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing):

  * Can receive a discount (up to 53%) for vCPUs, GPUs, TPUs, and any attached Local SSD disks.
  * You pay as you go (PAYG).



## Background

This section describes the available features that you can use to obtain computing resources, which include GPUs or TPUs, based on the requirements of your AI/ML workloads. These features help you implement strategies to maximize the flexibility, efficiency, and availability of your compute capacity.

### GPUs

Graphical processing units (GPUs) let you accelerate specific workloads such as machine learning and data processing. GKE offers nodes that are equipped with these powerful GPUs to optimize the performance of machine learning and data processing tasks. GKE provides a range of machine type options for node configuration, including machine types with NVIDIA H100, A100, and L4 GPUs.

For more information, see [About GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus).

### Flex-start

Flex-start, powered by [Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler), is a GPU consumption option where GKE persists your GPU request and automatically provisions Flex-start VMs when capacity becomes available. Consider using flex-start for workloads that need GPU capacity for a limited time, up to seven days, and don't have a fixed start date. For more information, see [flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).

### Spot VMs

You can use GPUs with [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms) if your workloads can tolerate frequent node disruptions. Using Spot VMs or flex-start reduce the price of running GPUs. Using Spot VMs combined with flex-start provides a fallback option when Spot VMs capacity is unavailable.

For more information, see [Using Spot VMs with GPU node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#spot-vms-gpus).

### ComputeClasses

You can request GPUs by using ComputeClasses. ComputeClasses let you define a hierarchy of node configurations for GKE to prioritize during node scaling decisions, so that workloads run on your selected hardware. For more information, see [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

## Before you begin

  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 



  * Ensure that you have a GKE Autopilot or Standard cluster that runs version 1.32.2-gke.1652000 or later. Your cluster must [enable node auto-provisioning and configure GPU limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#use_accelerators_for_new_auto-provisioned_node_pools) .
  * Create a [Hugging Face](https://huggingface.co/) account, if you don't already have one.
  * Ensure your project has sufficient preemptible quota for NVIDIA L4 GPUs. For more information, see [Preemptible quotas](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas).



## Get access to the model

**Note:** You must sign the consent agreement to use Mixtral 8x7b in the [Hugging Face repository](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1).

If you don't already have one, generate a new [Hugging Face token](https://huggingface.co/docs/hub/security-tokens):

  1. Click **Your Profile > Settings > Access Tokens**.
  2. Select **New Token**.
  3. Specify a name of your choice and a role of at least `Read`.
  4. Select **Generate a token**.



## Create a ComputeClass

In this section, you create a custom ComputeClass. ComputeClasses define the types and relationships between multiple compute resources used by your workload.

  1. In the Google Cloud console, launch a Cloud Shell session by clicking ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** in the [Google Cloud console](http://console.cloud.google.com). A session opens in the bottom pane of the Google Cloud console.
  2. Create a `dws-flex-start.yaml` manifest file:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: dws-model-inference-class
         spec:
           priorities:
             - machineType: g2-standard-24
               spot: true
             - machineType: g2-standard-24
               flexStart:
                 enabled: true
                 nodeRecycling:
                   leadTimeSeconds: 3600
           nodePoolAutoCreation:
             enabled: true
         

  3. Apply the `dws-flex-start.yaml` manifest:
         
         kubectl apply -f dws-flex-start.yaml
         




GKE deploys `g2-standard-24` machines with L4 accelerators. GKE uses [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) to prioritize Spot VMs first, and Flex-start VMs second.

## Deploy the LLM workload

  1. Create a Kubernetes Secret that contains the Hugging Face token by using the following command:
         
         kubectl create secret generic model-inference-secret \
             --from-literal=HUGGING_FACE_TOKEN=HUGGING_FACE_TOKEN \
             --dry-run=client -o yaml | kubectl apply -f -
         

Replace the `HUGGING_FACE_TOKEN` with your Hugging Face access token.

  2. Create a file named `mixtral-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: inference-mixtral-ccc
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: llm
           template:
             metadata:
               labels:
                 app: llm
             spec:
               nodeSelector:
                 cloud.google.com/compute-class: dws-model-inference-class
               containers:
               - name: llm
                 image: us-docker.pkg.dev/deeplearning-platform-release/gcr.io/huggingface-text-generation-inference-cu124.2-3.ubuntu2204.py311
                 resources:
                   requests:
                     cpu: "5"
                     memory: "40Gi"
                     nvidia.com/gpu: "2"
                   limits:
                     cpu: "5"
                     memory: "40Gi"
                     nvidia.com/gpu: "2"
                 env:
                 - name: MODEL_ID
                   value: mistralai/Mixtral-8x7B-Instruct-v0.1
                 - name: NUM_SHARD
                   value: "2"
                 - name: PORT
                   value: "8080"
                 - name: QUANTIZE
                   value: bitsandbytes-nf4
                 - name: HUGGING_FACE_HUB_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: model-inference-secret
                       key: HUGGING_FACE_TOKEN
                 volumeMounts:
                   - mountPath: /dev/shm
                     name: dshm
                   - mountPath: /tmp
                     name: ephemeral-volume
               volumes:
                 - name: dshm
                   emptyDir:
                       medium: Memory
                 - name: ephemeral-volume
                   ephemeral:
                     volumeClaimTemplate:
                       metadata:
                         labels:
                           type: ephemeral
                       spec:
                         accessModes: ["ReadWriteOnce"]
                         storageClassName: "premium-rwo"
                         resources:
                           requests:
                             storage: 100Gi
         

In this manifest, the `mountPath` field is set to `/tmp`, because it's the path where the `HF_HOME` environment variable in the Deep Learning Container (DLC) for Text Generation Inference (TGI) is set to, instead of the default `/data` path that's set within the TGI default image. The downloaded model will be stored in this directory.

  3. Deploy the model:
         
         kubectl apply -f  mixtral-deployment.yaml
         

GKE schedules a new Pod to deploy, which triggers the node pool autoscaler to add a second node before it deploys the second replica of the model.

  4. Verify the status of the model:
         
         watch kubectl get deploy inference-mixtral-ccc
         

If the model was deployed successfully, the output is similar to the following:
         
         NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
         inference-mixtral-ccc  1/1     1            1           10m
         

To exit the watch, press `CTRL + C`.

  5. Wait for the container to download and start serving the model:
         
         watch "kubectl logs $(kubectl get pods -l app=llm -o custom-columns=:metadata.name --no-headers) | tail"
         

To exit the watch, press `CTRL + C`.

**Note:** If you see HTTP `403 Forbidden` status codes instead of download logs, you may have to go to the [Mixtral 8x7b repository](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) on Hugging Face and sign the consent agreement.
  6. View the node pools that GKE provisioned:
         
         kubectl get nodes -L cloud.google.com/gke-nodepool
         

The output is similar to the following:
         
         NAME                                                  STATUS   ROLES    AGE   VERSION               GKE-NODEPOOL
           gke-flex-na-nap-g2-standard--0723b782-fg7v   Ready    <none>   10m   v1.32.3-gke.1152000   nap-g2-standard-24-spot-gpu2-1gbdlbxz
           gke-flex-nap-zo-default-pool-09f6fe53-fzm8   Ready    <none>   32m   v1.32.3-gke.1152000   default-pool
           gke-flex-nap-zo-default-pool-09f6fe53-lv2v   Ready    <none>   32m   v1.32.3-gke.1152000   default-pool
           gke-flex-nap-zo-default-pool-09f6fe53-pq6m   Ready    <none>   32m   v1.32.3-gke.1152000   default-pool
         

The name of the created node pool indicates the type of machine. In this case, GKE provisioned Spot VMs.

  7. Expose the model:
         
         kubectl expose deployment/inference-mixtral-ccc --port 8080 --name=llm-service
         

**Success:** You've successfully served an LLM by using a combination of Flex-start VMs, Spot VMs, and ComputeClasses to optimize GPU provisioning and cost. You can now interact with the model.



### Interact with the model using `curl`

This section shows how you can perform a basic inference test to verify your deployed model.

  1. Set up port forwarding to the model:
         
         kubectl port-forward service/llm-service 8080:8080
         

The output is similar to the following:
         
         Forwarding from 127.0.0.1:8080 -> 8080
         

  2. In a new terminal session, chat with your model by using `curl`:
         
         curl http://localhost:8080/v1/completions \
         -X POST \
         -H "Content-Type: application/json" \
         -d '{
             "model": "mixtral-8x7b-instruct-gptq",
             "prompt": "<s>[INST]Who was the first president of the United States?[/INST]",
             "max_tokens": 40}'
         

The output looks similar to the following:
         
         George Washington was a Founding Father and the first president of the United States, serving from 1789 to 1797.
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, either delete the project that contains the resources, or keep the project and delete the individual resources.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resource

  1. Delete the Kubernetes resources that you created from this guide:
         
         kubectl delete deployment inference-mixtral-ccc
         kubectl delete service llm-service
         kubectl delete computeclass dws-model-inference-class
         kubectl delete secret model-inference-secret
         

  2. Delete the cluster:
         
         gcloud container clusters delete CLUSTER_NAME
         




## What's next

  * Learn more how to [Train a small workload with flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training).
  * Learn more about [GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
