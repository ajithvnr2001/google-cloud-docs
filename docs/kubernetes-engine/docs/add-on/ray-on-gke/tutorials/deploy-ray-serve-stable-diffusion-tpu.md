---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/tutorials/deploy-ray-serve-stable-diffusion-tpu/
title: Deploy a Ray Serve application with a Stable Diffusion model on Google Kubernetes Engine (GKE) with TPUs \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:17.553877+00:00
---

# Deploy a Ray Serve application with a Stable Diffusion model on Google Kubernetes Engine (GKE) with TPUs  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/tutorials/deploy-ray-serve-stable-diffusion-tpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Deploy a Ray Serve application with a Stable Diffusion model on Google Kubernetes Engine (GKE) with TPUs Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This guide demonstrates how to deploy and serve a Stable Diffusion model on Google Kubernetes Engine (GKE) using TPUs, [Ray Serve](https://docs.ray.io/en/latest/serve/index.html), and the [Ray Operator add-on](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview).

This guide is intended for Generative AI customers, new or existing users of GKE, ML Engineers, MLOps (DevOps) engineers, or platform administrators who are interested in using Kubernetes container orchestration capabilities for serving models using Ray.

## About Ray and Ray Serve

Ray is an open-source scalable compute framework for AI/ML applications. Ray Serve is a model serving library for Ray used for scaling and serving models in a distributed environment. For more information, see [Ray Serve](https://docs.ray.io/en/latest/serve/index.html) in the Ray documentation.

## About TPUs

Tensor Processing Units (TPUs) are specialized hardware accelerators designed to significantly speed up the training and inference of large-scale machine learning models. Using Ray with TPUs lets you seamlessly scale high-performance ML applications. For more information about TPUs, see [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu) in the Cloud TPU documentation.

## About the KubeRay TPU initialization webhook

As part of the Ray Operator add-on, GKE provides validating and mutating [webhooks](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/ray-on-gke/tpu/kuberay-tpu-webhook) that handle TPU Pod scheduling and certain TPU environment variables required by frameworks like [JAX](https://github.com/google/jax) for container initialization. The KubeRay TPU webhook mutates Pods with the `app.kubernetes.io/name: kuberay` label requesting TPUs with the following properties:

  * `TPU_WORKER_ID`: A unique integer for each worker Pod in the TPU slice.
  * `TPU_WORKER_HOSTNAMES`: A list of DNS hostnames for all TPU workers that need to communicate with each other within the slice. This variable is only injected for TPU Pods in a multi-host group.
  * `replicaIndex`: A Pod label that contains a unique identifier for the worker-group replica the Pod belongs to. This is useful for multi-host worker groups, where multiple worker Pods might belong to the same replica, and is used by Ray to enable multi-host autoscaling.
  * `TPU_NAME`: A string representing the GKE TPU PodSlice this Pod belongs to, set to the same value as the `replicaIndex` label.
  * `podAffinity`: Ensures GKE schedules TPU Pods with matching `replicaIndex` labels on the same node pool. This lets GKE scale multi-host TPUs atomically by node pools, rather than single nodes.



## Objectives

  * Create a GKE cluster with a TPU node pool.
  * Deploy a Ray cluster with TPUs.
  * Deploy a [RayService](https://ray-project.github.io/kuberay/reference/api/#rayservice) custom resource.
  * Interact with the Stable Diffusion model server.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing/)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

[Cloud Shell](https://docs.cloud.google.com/shell) is preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/), and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). If you don't use Cloud Shell, install the gcloud CLI.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the GKE API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/container.clusterAdmin, roles/container.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



### Ensure sufficient quota

Ensure that your Google Cloud project has sufficient TPU quota in your Compute Engine region or zone. For more information, see [Ensure sufficient TPU and GKE quotas](https://docs.cloud.google.com/tpu/docs/tpus-in-gke#ensure-quotas) in the Cloud TPU documentation. You might also need to increase your quotas for:

  * Persistent Disk SSD (GB)
  * In-use IP addresses



### Prepare your environment

To prepare your environment, follow these steps:

  1. Launch a Cloud Shell session from the Google Cloud console, by clicking ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** in the [Google Cloud console](https://console.cloud.google.com/). This launches a session in the bottom pane of the Google Cloud console.

  2. Set environment variables:
         
         export PROJECT_ID=PROJECT_ID
         export CLUSTER_NAME=ray-cluster
         export COMPUTE_REGION=us-central2-b
         export CLUSTER_VERSION=CLUSTER_VERSION
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `CLUSTER_VERSION`: the GKE version to use. Must be `1.30.1` or later.
  3. Clone the GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         

  4. Change to the working directory:
         
         cd kubernetes-engine-samples/ai-ml/gke-ray/rayserve/stable-diffusion
         




## Create a cluster with a TPU node pool

Create a [Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode) GKE cluster with a TPU node pool:

  1. Create a Standard mode cluster with the Ray Operator enabled:
         
         gcloud container clusters create ${CLUSTER_NAME} \
             --addons=RayOperator \
             --machine-type=n1-standard-8 \
             --cluster-version=${CLUSTER_VERSION} \
             --location=${COMPUTE_REGION}
         

  2. Create a single-host TPU node pool:
         
         gcloud container node-pools create tpu-pool \
             --location=${COMPUTE_REGION} \
             --cluster=${CLUSTER_NAME} \
             --machine-type=ct4p-hightpu-4t \
             --num-nodes=1
         




To use TPUs with Standard mode, you must select:

  * A Compute Engine location with capacity for TPU accelerators
  * A compatible machine type for the TPU and
  * The physical topology of the TPU PodSlice



## Configure a RayCluster resource with TPUs

Configure your RayCluster manifest to prepare your TPU workload:

### Configure TPU `nodeSelector`

GKE uses Kubernetes [nodeSelectors](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) to ensure that TPU workloads are scheduled on the appropriate TPU topology and accelerator. For more information about selecting TPU nodeSelectors, see [Deploy TPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus).

Update the `ray-cluster.yaml` manifest to schedule your Pod on a v4 TPU podslice with a 2x2x1 topology:
    
    
    nodeSelector:
      cloud.google.com/gke-tpu-accelerator: tpu-v4-podslice
      cloud.google.com/gke-tpu-topology: 2x2x1
    

### Configure a TPU container resource

To use a TPU accelerator, you must specify the number of TPU chips that GKE should allocate to each Pod by configuring the `google.com/tpu`resource `limits` and `requests` in the TPU container field of your RayCluster manifest `workerGroupSpecs`.

Update the `ray-cluster.yaml` manifest with resource limits and requests:
    
    
    resources:
      limits:
        cpu: "1"
        ephemeral-storage: 10Gi
        google.com/tpu: "4"
        memory: "2G"
       requests:
        cpu: "1"
        ephemeral-storage: 10Gi
        google.com/tpu: "4"
        memory: "2G"
    

### Configure worker group `numOfHosts`

KubeRay v1.1.0 adds a `numOfHosts` field to the RayCluster custom resource, which specifies the number of TPU hosts to create per worker group replica. For multi-host worker groups, replicas are treated as PodSlices rather than individual workers, with `numOfHosts` worker nodes being created per replica.

Update the `ray-cluster.yaml` manifest with the following:
    
    
    workerGroupSpecs:
      # Several lines omitted
      numOfHosts: 1 # the number of "hosts" or workers per replica
    

## Create a RayService custom resource

Create a RayService custom resource:

  1. Review the following manifest:
         
         apiVersion: ray.io/v1
         kind: RayService
         metadata:
           name: stable-diffusion-tpu
         spec:
           serveConfigV2: |
             applications:
               - name: stable_diffusion
                 import_path: ai-ml.gke-ray.rayserve.stable-diffusion.stable_diffusion_tpu:deployment
                 runtime_env:
                   working_dir: "https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/archive/refs/heads/main.zip"
                   pip:
                     - diffusers==0.7.2
                     - flax
                     - jax[tpu]==0.4.11
                     - -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
                     - fastapi
           rayClusterConfig:
             rayVersion: '2.9.0'
             headGroupSpec:
               rayStartParams: {}
               template:
                 spec:
                   containers:
                   - name: ray-head
                     image: rayproject/ray-ml:2.9.0-py310
                     ports:
                     - containerPort: 6379
                       name: gcs
                     - containerPort: 8265
                       name: dashboard
                     - containerPort: 10001
                       name: client
                     - containerPort: 8000
                       name: serve
                     resources:
                       limits:
                         cpu: "2"
                         memory: "8G"
                       requests:
                         cpu: "2"
                         memory: "8G"
             workerGroupSpecs:
             - replicas: 1
               minReplicas: 1
               maxReplicas: 10
               numOfHosts: 1
               groupName: tpu-group
               rayStartParams: {}
               template:
                 spec:
                   containers:
                   - name: ray-worker
                     image: rayproject/ray-ml:2.9.0-py310
                     resources:
                       limits:
                         cpu: "100"
                         ephemeral-storage: 20Gi
                         google.com/tpu: "4"
                         memory: 200G
                       requests:
                         cpu: "100"
                         ephemeral-storage: 20Gi
                         google.com/tpu: "4"
                         memory: 200G
                   nodeSelector:
                     cloud.google.com/gke-tpu-accelerator: tpu-v4-podslice
                     cloud.google.com/gke-tpu-topology: 2x2x1

This manifest describes a RayService custom resource that creates a RayCluster resource with 1 head node and a TPU worker group with a 2x2x1 topology, meaning each worker node will have 4 v4 TPU chips.

The TPU node belongs to a single v4 TPU podslice with a 2x2x1 topology. To create a multi-host worker group, replace the `gke-tpu nodeSelector` values, `google.com/tpu` container limits and requests, and `numOfHosts` values with your multi-host configuration. For more information about TPU multi-host topologies, see [System architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm) in the Cloud TPU documentation.

  2. Apply the manifest to your cluster:
         
         kubectl apply -f ray-service-tpu.yaml
         

  3. Verify the RayService resource is running:
         
         kubectl get rayservices
         

The output is similar to the following:
         
         NAME                   SERVICE STATUS   NUM SERVE ENDPOINTS
         stable-diffusion-tpu   Running          2
         

In this output, `Running` in the `SERVICE STATUS` column indicates the RayService resource is ready.




### (Optional) View the Ray Dashboard

You can view your Ray Serve deployment and relevant logs from the Ray Dashboard.

  1. Establish a port-forwarding session to the Ray dashboard from the Ray head service:
         
         kubectl port-forward svc/stable-diffusion-tpu-head-svc 8265:8265
         

  2. In a web browser, go to `http://localhost:8265/`.

  3. Click the **Serve** tab.




## Send prompts to the model server

  1. Establish a port-forwarding session to the Serve endpoint from the Ray head service:
         
         kubectl port-forward svc/stable-diffusion-tpu-serve-svc 8000
         

  2. Open a new Cloud Shell session.

  3. Submit a text-to-image prompt to the Stable Diffusion model server:
         
         python stable_diffusion_tpu_req.py  --save_pictures
         

The results of the stable diffusion inference are saved to a file named `diffusion_results.png`.

![Image generated by Stable Diffusion with 8 sections: a green chair, a man standing outside a house, a robot on the street, a family sitting at a table, a doc walking in a park, a flying dragon, a Japanese-style portrait of bears, and a waterfall.](https://docs.cloud.google.com/static/kubernetes-engine/docs/add-on/ray-on-gke/images/stable-diffusion-generated-image-tpus.png)




## Observe your Ray workloads

To view details for your RayJobs, you can navigate to the **Kubernetes Engine > AI/ML > Jobs** section in Google Cloud console.

[View RayJobs in Google Cloud console](https://console.cloud.google.com/kubernetes/aiml/jobs)

## Clean up

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

To delete the cluster, type:
    
    
    gcloud container clusters delete ${CLUSTER_NAME}
    

## What's next

  * Learn about [Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html).
  * Explore the [KubeRay documentation](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started.html).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
