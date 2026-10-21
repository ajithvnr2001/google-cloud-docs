---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/tpu-multihost-saxml/
title: Serve an LLM using multi-host TPUs on GKE with Saxml \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:15:23.474289+00:00
---

# Serve an LLM using multi-host TPUs on GKE with Saxml  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/tpu-multihost-saxml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Serve an LLM using multi-host TPUs on GKE with Saxml Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Caution:** Saxml on GKE is de-prioritized beginning April 24, 2025. This means the project won't get further updates. Existing Saxml deployments will continue to function as is without disruption. _We strongly suggest_ you migrate to [JetStream](https://github.com/google/JetStream), Google's up to date open source inference framework for high-performance LLM serving on TPUs and GPUs. JetStream offers continuous batching and quantization for better throughput and memory efficiency. For a migration example, see [Serve Gemma using TPUs on GKE with JetStream](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-tpu-jetstream).

This tutorial shows you how to deploy and serve a large language model (LLM) using [multi-host TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host) on Google Kubernetes Engine (GKE) with [Saxml](https://github.com/google/saxml#saxml-aka-sax) for efficient scalable architecture.

### Background

Saxml is an experimental system that serves [Paxml](https://github.com/google/paxml), [JAX](https://github.com/google/jax), and [PyTorch](https://pytorch.org/) frameworks. You can use TPUs to accelerate data processing with these frameworks. To demo the deployment of TPUs in GKE, this tutorial serves the 175B [LmCloudSpmd175B32Test](https://github.com/google/saxml/blob/7caf0870b6f9bacab4d255abe278833d642e7bd5/saxml/server/pax/lm/params/lm_cloud.py#L585C9-L585C9) test model. GKE deploys this test model on two v5e TPU slice node pools with `4x8` topology respectively.

To properly deploy the test model, the TPU topology has been defined based on the size of the model. Given that the N billion 16 bit model approximately requires around 2 times (2xN) GB of memory, the 175B [LmCloudSpmd175B32Test](https://github.com/google/saxml/blob/7caf0870b6f9bacab4d255abe278833d642e7bd5/saxml/server/pax/lm/params/lm_cloud.py#L585C9-L585C9) model requires about 350 GB of memory. The TPU v5e single TPU chip has 16 GB. To support 350 GB, GKE needs 21 v5e TPU chips (350/16= 21). Based on the [mapping of TPU configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus), the proper TPU configuration for this tutorial is:

  * Machine type: `ct5lp-hightpu-4t`
  * Topology: `4x8` (32 number of TPU chips)



Selecting the right TPU topology for serving a model is important when deploying TPUs in GKE. To learn more, see [Plan your TPU configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#plan-tpu).

## Objectives

This tutorial is intended for MLOps or DevOps engineers or platform administrators that want to use GKE orchestration capabilities for serving data models.

This tutorial covers the following steps:

  1. Prepare your environment with a Standard cluster. The cluster has two v5e TPU slice node pools with `4x8` topology.
  2. Deploy Saxml. Saxml needs an administrator server, a group of Pods that work as the model server, a prebuilt HTTP server, and a load balancer.
  3. Use the Saxml to serve the LLM.



The following diagram shows the architecture that the following tutorial implements:

[ ![Architecture of a multi-host TPU on GKE.](https://docs.cloud.google.com/static/kubernetes-engine/images/llm-multi-host.svg)](https://docs.cloud.google.com/static/kubernetes-engine/images/llm-multi-host.svg) **Figure:** Example architecture of a multi-host TPU on GKE. 

## Before you begin

  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  * Make sure that you have the following role or roles on the project: roles/container.admin, roles/iam.serviceAccountAdmin, roles/iam.policyAdmin 

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


  * [Ensure your project has sufficient quota](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-quota) for Cloud TPU in GKE.



## Prepare the environment

  1. In the Google Cloud console, start a Cloud Shell instance:   
[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
           export PROJECT_ID=$(gcloud config get project)
           export CONTROL_PLANE_LOCATION=CONTROL_PLANE_LOCATION
           export BUCKET_NAME=PROJECT_ID-gke-bucket
         

Replace the following values:

     * PROJECT_ID: Your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * CONTROL_PLANE_LOCATION: the Compute Engine [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Select the zone where the [`ct5lp-hightpu-4t` is available](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).

In this command, `BUCKET_NAME` specifies the name of the Google Cloud storage bucket to store Saxml administrator server configurations.




### Create a cluster

Use Cloud Shell to do the following:

  1. Create a Standard cluster that uses [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity):
         
         gcloud container clusters create saxml \
             --location=${CONTROL_PLANE_LOCATION} \
             --workload-pool=${PROJECT_ID}.svc.id.goog \
             --cluster-version=VERSION \
             --num-nodes=4
         

Replace the `VERSION` with the GKE version number. GKE supports TPU v5e in version 1.27.2-gke.2100 and later. For more information, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).

The cluster creation might take several minutes.

  2. Create the first node pool named `tpu1`:
         
         gcloud container node-pools create tpu1 \
             --location=${CONTROL_PLANE_LOCATION} \
             --machine-type=ct5lp-hightpu-4t \
             --tpu-topology=4x8 \
             --num-nodes=8 \
             --cluster=saxml
         

The value for the `--num-nodes` flag is calculated by dividing the TPU topology by the number of TPU chips per TPU slice. In this case: (4 * 8) / 4.

  3. Create the second node pool named `tpu2`:
         
         gcloud container node-pools create tpu2 \
             --location=${CONTROL_PLANE_LOCATION} \
             --machine-type=ct5lp-hightpu-4t \
             --tpu-topology=4x8 \
             --num-nodes=8 \
             --cluster=saxml
         

The value for the `--num-nodes` flag is calculated by dividing the TPU topology by the number of TPU chips per TPU slice. In this case: (4 * 8) / 4.




You have created the following resources:

  * A Standard cluster with four CPU nodes.
  * Two v5e TPU slice node pools with `4x8` topology. Each node pools represent eight TPU slice nodes with 4 TPU chips each.



The 175B model has to be served on a multi-host v5e TPU slice with `4x8` topology slice (32 v5e TPU chips) at minimum.

### Create a Cloud Storage bucket

Create a Cloud Storage bucket to store Saxml administrator server configurations. A running administrator server periodically saves its state and the details of the published models.

In Cloud Shell, run the following:
    
    
    gcloud storage buckets create gs://${BUCKET_NAME}
    

### Configure your workloads access using Workload Identity Federation for GKE

Assign a Kubernetes ServiceAccount to the application and configure that Kubernetes ServiceAccount to act as an IAM service account.

  1. Configure `kubectl` to communicate with your cluster:
         
         gcloud container clusters get-credentials saxml --location=${CONTROL_PLANE_LOCATION}
         

  2. Create a Kubernetes ServiceAccount for your application to use:
         
         kubectl create serviceaccount sax-sa --namespace default
         

  3. Create an IAM service account for your application:
         
         gcloud iam service-accounts create sax-iam-sa
         

  4. Add an [IAM policy binding](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) for your IAM service account to read and write to Cloud Storage:
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID} \
           --member "serviceAccount:sax-iam-sa@${PROJECT_ID}.iam.gserviceaccount.com" \
           --role roles/storage.admin
         

  5. Allow the Kubernetes ServiceAccount to [impersonate the IAM service account](https://docs.cloud.google.com/iam/docs/service-account-overview#impersonation) by adding an IAM policy binding between the two service accounts. This binding allows the Kubernetes ServiceAccount to act as the IAM service account, so that the Kubernetes ServiceAccount can read and write to Cloud Storage.
         
         gcloud iam service-accounts add-iam-policy-binding sax-iam-sa@${PROJECT_ID}.iam.gserviceaccount.com \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:${PROJECT_ID}.svc.id.goog[default/sax-sa]"
         

  6. [Annotate](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) the Kubernetes service account with the email address of the IAM service account. This lets your sample app know which service account to use to access Google Cloud services. So when the app uses any standard Google API Client Libraries to access Google Cloud services, it uses that IAM service account.
         
         kubectl annotate serviceaccount sax-sa \
           iam.gke.io/gcp-service-account=sax-iam-sa@${PROJECT_ID}.iam.gserviceaccount.com
         




## Deploy Saxml

In this section, you deploy the Saxml administrator server and the Saxml model server.

### Deploy the Saxml administrator server

  1. Create the following `sax-admin-server.yaml` manifest:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: sax-admin-server
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: sax-admin-server
           template:
             metadata:
               labels:
                 app: sax-admin-server
             spec:
               hostNetwork: false
               serviceAccountName: sax-sa
               containers:
               - name: sax-admin-server
                 image: us-docker.pkg.dev/cloud-tpu-images/inference/sax-admin-server:v1.1.0
                 securityContext:
                   privileged: true
                 ports:
                 - containerPort: 10000
                 env:
                 - name: GSBUCKET
                   value: BUCKET_NAME

  2. Replace `BUCKET_NAME` with your Cloud Storage created earlier:
         
         perl -pi -e 's|BUCKET_NAME|BUCKET_NAME|g' sax-admin-server.yaml
         

  3. Apply the manifest:
         
         kubectl apply -f sax-admin-server.yaml
         

  4. Verify that the administrator server Pod is up and running:
         
         kubectl get deployment
         

The output is similar to the following:
         
         NAME               READY   UP-TO-DATE   AVAILABLE   AGE
         sax-admin-server   1/1     1            1           52s
         




### Deploy Saxml model server

Workloads running in multi-host TPU slices require a stable network identifier for each Pod to discover peers in the same TPU slice. To define these identifiers, use [IndexedJob](https://kubernetes.io/blog/2021/04/19/introducing-indexed-jobs/), [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#pod-identity) with a headless Service or [JobSet](https://github.com/kubernetes-sigs/jobset) which automatically creates a headless Service for all the Jobs that belong to the JobSet. A Jobset is a workload API that lets you manage a group of Kubernetes Jobs as a unit. The most common use case for a JobSet is distributed training, but you can also use it to run batch workloads.

The following section shows how to manage multiple groups of model server Pods with JobSet.

  1. [Install JobSet](https://jobset.sigs.k8s.io/docs/installation/) v0.2.3 or later.
         
         kubectl apply --server-side -f https://github.com/kubernetes-sigs/jobset/releases/download/JOBSET_VERSION/manifests.yaml
         

Replace the `JOBSET_VERSION` with the JobSet version. For example, `v0.2.3`.

  2. Validate JobSet controller is running in the `jobset-system` namespace:
         
         kubectl get pod -n jobset-system
         

The output is similar to the following:
         
         NAME                                        READY   STATUS    RESTARTS   AGE
         jobset-controller-manager-69449d86bc-hp5r6   2/2     Running   0          2m15s
         

  3. Deploy two model servers in two TPU slice node pools. Save the following `sax-model-server-set` manifest:
         
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: sax-model-server-set
           annotations:
             alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           failurePolicy:
             maxRestarts: 4
           replicatedJobs:
             - name: sax-model-server
               replicas: 2
               template:
                 spec:
                   parallelism: 8
                   completions: 8
                   backoffLimit: 0
                   template:
                     spec:
                       serviceAccountName: sax-sa
                       hostNetwork: true
                       dnsPolicy: ClusterFirstWithHostNet
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                         cloud.google.com/gke-tpu-topology: 4x8
                       containers:
                       - name: sax-model-server
                         image: us-docker.pkg.dev/cloud-tpu-images/inference/sax-model-server:v1.1.0
                         args: ["--port=10001","--sax_cell=/sax/test", "--platform_chip=tpuv5e"]
                         ports:
                         - containerPort: 10001
                         - containerPort: 8471
                         securityContext:
                           privileged: true
                         env:
                         - name: SAX_ROOT
                           value: "gs://BUCKET_NAME/sax-root"
                         - name: MEGASCALE_NUM_SLICES
                           value: ""
                         resources:
                           requests:
                             google.com/tpu: 4
                           limits:
                             google.com/tpu: 4

  4. Replace `BUCKET_NAME` with your Cloud Storage created earlier:
         
         perl -pi -e 's|BUCKET_NAME|BUCKET_NAME|g' sax-model-server-set.yaml
         

In this manifest:

     * `replicas: 2` is the number of Job replicas. Each job represents a model server. Therefore, a group of 8 Pods.
     * `parallelism: 8` and `completions: 8` are equal to the number of nodes in each node pool.
     * `backoffLimit: 0` must be zero to mark the Job as failed if any Pod fails.
     * `ports.containerPort: 8471` is the default port for the VMs communication
     * `name: MEGASCALE_NUM_SLICES` unsets the environment variable because GKE isn't running Multislice training.
  5. Apply the manifest:
         
         kubectl apply -f sax-model-server-set.yaml
         

  6. Verify the status of the Saxml Admin Server and Model Server Pods:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                                              READY   STATUS    RESTARTS   AGE
         sax-admin-server-557c85f488-lnd5d                 1/1     Running   0          35h
         sax-model-server-set-sax-model-server-0-0-nj4sm   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-0-1-sl8w4   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-0-2-hb4rk   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-0-3-qv67g   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-0-4-pzqz6   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-0-5-nm7mz   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-0-6-7br2x   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-0-7-4pw6z   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-1-0-8mlf5   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-1-1-h6z6w   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-1-2-jggtv   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-1-3-9v8kj   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-1-4-6vlb2   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-1-5-h689p   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-1-6-bgv5k   1/1     Running   0          24m
         sax-model-server-set-sax-model-server-1-7-cd6gv   1/1     Running   0          24m
         




In this example, there are 16 model server containers: `sax-model-server-set-sax-model-server-0-0-nj4sm` and `sax-model-server-set-sax-model-server-1-0-8mlf5` are the two primary model servers in each group.

Your Saxml cluster has two model servers deployed on two v5e TPU slice node pools with `4x8` topology respectively.

### Deploy Saxml HTTP Server and load balancer

  1. Use the following prebuilt image HTTP server image. Save the following `sax-http.yaml` manifest:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: sax-http
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: sax-http
           template:
             metadata:
               labels:
                 app: sax-http
             spec:
               hostNetwork: false
               serviceAccountName: sax-sa
               containers:
               - name: sax-http
                 image: us-docker.pkg.dev/cloud-tpu-images/inference/sax-http:v1.0.0
                 ports:
                 - containerPort: 8888
                 env:
                 - name: SAX_ROOT
                   value: "gs://BUCKET_NAME/sax-root"
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: sax-http-lb
         spec:
           selector:
             app: sax-http
           ports:
           - protocol: TCP
             port: 8888
             targetPort: 8888
           type: LoadBalancer

  2. Replace `BUCKET_NAME` with your Cloud Storage created earlier:
         
         perl -pi -e 's|BUCKET_NAME|BUCKET_NAME|g' sax-http.yaml
         

  3. Apply the `sax-http.yaml` manifest:
         
         kubectl apply -f sax-http.yaml
         

**Note:** You can use your own HTTP server built for Saxml. To learn more, see [Inferencing using Saxml and an HTTP Server](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/tools/saxml-on-gke/httpserver).
  4. Wait for the HTTP Server container to finish creating:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                                              READY   STATUS    RESTARTS   AGE
         sax-admin-server-557c85f488-lnd5d                 1/1     Running   0          35h
         sax-http-65d478d987-6q7zd                         1/1     Running   0          24m
         sax-model-server-set-sax-model-server-0-0-nj4sm   1/1     Running   0          24m
         ...
         

  5. Wait for the Service to have an external IP address assigned:
         
         kubectl get svc
         

The output is similar to the following:
         
         NAME           TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
         sax-http-lb    LoadBalancer   10.48.11.80   10.182.0.87   8888:32674/TCP   7m36s
         




## Use Saxml

Load, deploy, and serve the model on the Saxml in the v5e TPU multihost slice:

### Load the model

  1. Retrieve the load balancer IP address for Saxml.
         
         LB_IP=$(kubectl get svc sax-http-lb -o jsonpath='{.status.loadBalancer.ingress[*].ip}')
         PORT="8888"
         

  2. Load the `LmCloudSpmd175B` test model in two v5e TPU slice node pools:
         
         curl --request POST \
         --header "Content-type: application/json" \
         -s ${LB_IP}:${PORT}/publish --data \
         '{
             "model": "/sax/test/spmd",
             "model_path": "saxml.server.pax.lm.params.lm_cloud.LmCloudSpmd175B32Test",
             "checkpoint": "None",
             "replicas": 2
         }'
         

The test model does not have a fine-tuned checkpoint, the weights are randomly generated. The model loading could take up to 10 minutes.

The output is similar to the following:
         
         {
             "model": "/sax/test/spmd",
             "path": "saxml.server.pax.lm.params.lm_cloud.LmCloudSpmd175B32Test",
             "checkpoint": "None",
             "replicas": 2
         }
         

  3. Check the model readiness:
         
         kubectl logs sax-model-server-set-sax-model-server-0-0-nj4sm
         

The output is similar to the following:
         
         ...
         loading completed.
         Successfully loaded model for key: /sax/test/spmd
         

The model is fully loaded.

  4. Get information about the model:
         
         curl --request GET \
         --header "Content-type: application/json" \
         -s ${LB_IP}:${PORT}/listcell --data \
         '{
             "model": "/sax/test/spmd"
         }'
         

The output is similar to the following:
         
         {
         "model": "/sax/test/spmd",
         "model_path": "saxml.server.pax.lm.params.lm_cloud.LmCloudSpmd175B32Test",
         "checkpoint": "None",
         "max_replicas": 2,
         "active_replicas": 2
         }
         




### Serve the model

Serve a prompt request:
    
    
    curl --request POST \
    --header "Content-type: application/json" \
    -s ${LB_IP}:${PORT}/generate --data \
    '{
      "model": "/sax/test/spmd",
      "query": "How many days are in a week?"
    }'
    

The output shows an example of the model response. This response might not be meaningful because the test model has random weights.

**Success:** You have successfully served an LLM using multi-host TPUs on GKE.

### Unpublish the model

Run the following command to unpublish the model:
    
    
    curl --request POST \
    --header "Content-type: application/json" \
    -s ${LB_IP}:${PORT}/unpublish --data \
    '{
        "model": "/sax/test/spmd"
    }'
    

The output is similar to the following:
    
    
    {
      "model": "/sax/test/spmd"
    }
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the deployed resources

  1. Delete the cluster you created for this tutorial:
         
         gcloud container clusters delete saxml --location ${CONTROL_PLANE_LOCATION}
         

  2. Delete the service account:
         
         gcloud iam service-accounts delete sax-iam-sa@${PROJECT_ID}.iam.gserviceaccount.com
         

  3. Delete the Cloud Storage bucket:
         
         gcloud storage rm -r gs://${BUCKET_NAME}
         




## What's next

  * Learn about current TPU versions with the [Cloud TPU system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * Learn more about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
