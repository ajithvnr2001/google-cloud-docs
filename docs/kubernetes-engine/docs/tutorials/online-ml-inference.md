---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/online-ml-inference/
title: Serve a model with a single GPU in GKE \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:57:38.868039+00:00
---

# Serve a model with a single GPU in GKE  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/online-ml-inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Serve a model with a single GPU in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to deploy and serve a large language model (LLM) using GPUs on Google Kubernetes Engine (GKE) with [NVIDIA Triton Inference Server](https://developer.nvidia.com/triton-inference-server) and [TensorFlow Serving](https://www.tensorflow.org/tfx/guide/serving) This provides a foundation for understanding and exploring practical LLM deployment for inference in a managed Kubernetes environment. You deploy a pre-built container to a GKE cluster with a single [L4 Tensor Core GPU](https://www.nvidia.com/en-us/data-center/l4/) and you prepare the GKE infrastructure to do online inference.

This tutorial is intended for Machine learning (ML) engineers, Platform admins and operators, and for Data and AI specialists who want to host a pre-trained machine learning (ML) model on a GKE cluster. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following:

  * [Current GPU version availability](https://docs.cloud.google.com/compute/docs/gpus)
  * [GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)



## Objectives

  1. Create a GKE Autopilot or Standard cluster.
  2. Configure a Cloud Storage bucket, where the pre-trained model lives.
  3. Deploy the online inference framework you select.
  4. Make a test request to the deployed service.

**Note:** This tutorial is a foundation for online serving. Additional elements like Load Balancers should be considered depending on the use case.

## Costs

This tutorial uses the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * Cloud Storage
  * L4 GPU accelerators
  * Egress traffic



Use the [Pricing Calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.

When you finish this tutorial, you can avoid continued billing by deleting the resources you created. For more information, see Clean up.

## Before you begin

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, click **Create project** to begin creating a new Google Cloud project.

**Roles required to create a project**

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the GKE API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  5. In the Google Cloud console, on the project selector page, click **Create project** to begin creating a new Google Cloud project.

**Roles required to create a project**

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)




### Set defaults for the Google Cloud CLI

  1. In the Google Cloud console, start a Cloud Shell instance:   
[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Download the source code for this sample app:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         cd kubernetes-engine-samples/ai-ml/gke-online-serving-single-gpu
         

  3. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         gcloud config set compute/region COMPUTE_REGION
         

Replace the following values:

     * PROJECT_ID: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * COMPUTE_REGION: the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) that supports the accelerator type you want to use, for example, `us-central1` for L4 GPU.
  4. In Cloud Shell, create the following environment variables:
         
         export PROJECT_ID=$(gcloud config get project)
         export REGION=$(gcloud config get compute/region)
         export K8S_SA_NAME=gpu-k8s-sa
         export GSBUCKET=$PROJECT_ID-gke-bucket
         export MODEL_NAME=mnist
         export CLUSTER_NAME=online-serving-cluster
         




## Create a GKE cluster

You can serve models on a single GPU in a GKE Autopilot or Standard cluster. We recommend that you use a Autopilot cluster for a fully managed Kubernetes experience. With GKE Autopilot the resources scale automatically based on the model requests.

To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot 

Run the following command to create a GKE Autopilot cluster:
    
    
      gcloud container clusters create-auto ${CLUSTER_NAME} \
          --location=${REGION} \
          --project=${PROJECT_ID} \
          --release-channel=rapid
    

**Note:** This step can take up to five minutes to complete.

GKE creates an Autopilot cluster with CPU and GPU nodes as requested by the deployed workloads.

### Standard

  1. Run the following command to create a GKE Standard cluster:
         
         gcloud container clusters create ${CLUSTER_NAME} \
             --project=${PROJECT_ID}  \
             --location=${REGION}  \
             --workload-pool=${PROJECT_ID}.svc.id.goog \
             --addons GcsFuseCsiDriver \
             --release-channel=rapid \
             --num-nodes=1
         

The cluster creation might take several minutes.

  2. Run the following command to create the node pool:
         
         gcloud container node-pools create gpupool \
             --accelerator type=nvidia-l4,count=1,gpu-driver-version=latest \
             --project=${PROJECT_ID} \
             --location=${REGION} \
             --node-locations=${REGION}-a \
             --cluster=${CLUSTER_NAME} \
             --machine-type=g2-standard-8 \
             --num-nodes=1
         

GKE creates a single node pool containing one L4 GPU for each node.




## Create a Cloud Storage bucket

Create a Cloud Storage bucket to store the pre-trained model that will be served.

In Cloud Shell, run the following:
    
    
    gcloud storage buckets create gs://$GSBUCKET --uniform-bucket-level-access
    

## Configure your cluster to access the bucket using Workload Identity Federation for GKE

To let your cluster access the Cloud Storage bucket, you do the following:

  1. Create a Kubernetes ServiceAccount in your cluster.
  2. Grant IAM roles to the Kubernetes ServiceAccount.



### Create a Kubernetes ServiceAccount in your cluster

In Cloud Shell, do the following:

  1. Create a Kubernetes namespace:
         
         kubectl create namespace gke-ai-namespace
         

  2. Create a Kubernetes ServiceAccount in the namespace:
         
         kubectl create serviceaccount gpu-k8s-sa --namespace=gke-ai-namespace
         




### Grant IAM roles to the Kubernetes ServiceAccount

In Cloud Shell, grant the Storage Object Admin (`roles/storage.objectAdmin`) and Storage Insights Collector Service (`roles/storage.insightsCollectorService`) roles to the Kubernetes ServiceAccount:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/gke-ai-namespace/sa/gpu-k8s-sa" \
        --role=roles/storage.objectAdmin \
        --condition=None
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/gke-ai-namespace/sa/gpu-k8s-sa" \
        --role=roles/storage.insightsCollectorService \
        --condition=None
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `PROJECT_NUMBER`: your Google Cloud project number.



## Deploy the online inference server

Each online inference framework expects to find the pre-trained ML model in a specific format. The following section shows how to deploy the inference server depending on the framework you want to use:

### Triton

  1. In Cloud Shell, copy the pre-trained ML model into the Cloud Storage bucket:
         
         gcloud storage cp src/triton-model-repository gs://$GSBUCKET --recursive
         

  2. Deploy the framework by using a Deployment. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster.:
         
         envsubst < src/gke-config/deployment-triton.yaml | kubectl --namespace=gke-ai-namespace apply -f -
         

  3. Validate that GKE deployed the framework:
         
         kubectl get deployments --namespace=gke-ai-namespace
         

When the framework is ready, the output is similar to the following:
         
         NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
         triton-deployment    1/1     1            1           5m29s
         

  4. Deploy the Services to access the Deployment:
         
         kubectl apply --namespace=gke-ai-namespace -f src/gke-config/service-triton.yaml
         

  5. Check the external IP is assigned:
         
         kubectl get services --namespace=gke-ai-namespace
         

The output is similar to the following:
         
         NAME            TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                                        AGE
         kubernetes      ClusterIP      34.118.224.1     <none>          443/TCP                                        60m
         triton-server   LoadBalancer   34.118.227.176   35.239.54.228   8000:30866/TCP,8001:31035/TCP,8002:30516/TCP   5m14s
         

Take note of the IP address for the `triton-server` in the **EXTERNAL-IP** column.

  6. Check that the service and the deployment are working correctly:
         
         curl -v EXTERNAL_IP:8000/v2/health/ready
         

The output is similar to the following:
         
         ...
         < HTTP/1.1 200 OK
         < Content-Length: 0
         < Content-Type: text/plain
         ...
         




### TF Serving

  1. In Cloud Shell, copy the pre-trained ML model into the Cloud Storage bucket:
         
         gcloud storage cp src/tfserve-model-repository gs://$GSBUCKET --recursive
         

  2. Deploy the framework by using a Deployment. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster.:
         
         envsubst < src/gke-config/deployment-tfserve.yaml | kubectl --namespace=gke-ai-namespace apply -f -
         

  3. Validate that GKE deployed the framework:
         
         kubectl get deployments --namespace=gke-ai-namespace
         

When the framework is ready, the output is similar to the following:
         
         NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
         tfserve-deployment   1/1     1            1           5m29s
         

  4. Deploy the Services to access the Deployment:
         
         kubectl apply --namespace=gke-ai-namespace -f src/gke-config/service-tfserve.yaml
         

  5. Check the external IP is assigned:
         
         kubectl get services --namespace=gke-ai-namespace
         

The output is similar to the following:
         
         NAME            TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                                        AGE
         kubernetes      ClusterIP      34.118.224.1     <none>          443/TCP                                        60m
         tfserve-server  LoadBalancer   34.118.227.176   35.239.54.228   8500:30003/TCP,8000:32194/TCP                  5m14s
         

Take note of the IP address for the `tfserve-server` in the **EXTERNAL-IP** column.

  6. Check that the Service and the Deployment are working correctly:
         
         curl -v EXTERNAL_IP:8000/v1/models/mnist
         

Replace the `EXTERNAL_IP` with your external IP address.

The output is similar to the following:
         
         ...
         < HTTP/1.1 200 OK
         < Content-Type: application/json
         < Date: Thu, 12 Oct 2023 19:01:19 GMT
         < Content-Length: 154
         <
         {
           "model_version_status": [
                 {
                 "version": "1",
                 "state": "AVAILABLE",
                 "status": {
                   "error_code": "OK",
                   "error_message": ""
                 }
               }
             ]
         }
         




## Serve the model

### Triton

  1. Create a Python virtual environment in Cloud Shell.
         
         python -m venv ./mnist_client
         source ./mnist_client/bin/activate
         

  2. Install the required Python packages.
         
         pip install -r src/client/triton-requirements.txt
         

  3. Test Triton inference server by loading an image:
         
         cd src/client
         python triton_mnist_client.py -i EXTERNAL_IP -m mnist -p ./images/TEST_IMAGE.png
         

Replace the following:

     * `EXTERNAL_IP`: Your external IP address.
     * `TEST_IMAGE`: The name of the file that corresponds to the image you want to test. You can use the images stored in `src/client/images`.

Depending on which image you use, the output is similar to the following:
    
    Calling Triton HTTP Service      ->      Prediction result: 7
    


**Note:** You can write clients that run inference against the Triton Inference server. To learn more, see [NVIDIA examples and libraries](https://github.com/triton-inference-server/client).

### TF Serving

  1. Create a Python virtual environment in Cloud Shell.
         
         python -m venv ./mnist_client
         source ./mnist_client/bin/activate
         

  2. Install the required Python packages.
         
         pip install -r src/client/tfserve-requirements.txt
         

  3. Test TensorFlow Serving with a few images.
         
         cd src/client
         python tfserve_mnist_client.py -i EXTERNAL_IP -m mnist -p ./images/TEST_IMAGE.png
         




Replace the following:

  * `EXTERNAL_IP`: Your external IP address.
  * `TEST_IMAGE`: A value from `0` to `9`. You can use the images stored in `src/client/images`.



Depending on which image you use, you will get an output similar to this:
    
    
      Calling TensorFlow Serve HTTP Service    ->      Prediction result: 5
    

**Note:** You can write clients that run inference against the TensorFlow server. To learn more, see [TensorFlow API](https://www.tensorflow.org/tfx/serving/api_rest).

**Success:** You've successfully deployed an online serving framework for a pre-trained ML model.

## Observe model performance

### Triton

To observe the model performance, you can use the Triton dashboard integration in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). With this dashboard, you can view critical performance metrics like token throughput, request latency, and error rates.

To use the Triton dashboard, you must enable [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), which collects the metrics from Triton, in your GKE cluster. Triton exposes metrics in Prometheus format by default; you do not need to install an additional exporter.

You can then view the metrics by using the Triton dashboard. For information about using Google Cloud Managed Service for Prometheus to collect metrics from your model, see the [Triton](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/nvidia-triton) observability guidance in the Cloud Monitoring documentation.

### TF Serving

To observe the model performance, you can use the TF Serving dashboard integration in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). With this dashboard, you can view critical performance metrics like token throughput, request latency, and error rates.

To use the TF Serving dashboard, you must enable [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), which collects the metrics from TF Serving, in your GKE cluster.

You can then view the metrics by using the TF Serving dashboard. For information about using Google Cloud Managed Service for Prometheus to collect metrics from your model, see the [TF Serving](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/tf-serving) observability guidance in the Cloud Monitoring documentation.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources that you created in this guide, do one of the following:

  * **Keep the GKE cluster:** Delete the Kubernetes resources in the cluster and the Google Cloud resources
  * **Keep the Google Cloud project:** Delete the GKE cluster and the Google Cloud resources
  * **Delete the project**



### Delete the Kubernetes resources in the cluster and the Google Cloud resources

  1. Delete the Kubernetes namespace and the workloads that you deployed:



### Triton
    
    
    kubectl -n gke-ai-namespace delete -f src/gke-config/service-triton.yaml
    kubectl -n gke-ai-namespace delete -f src/gke-config/deployment-triton.yaml
    kubectl delete namespace gke-ai-namespace
    

### TF Serving
    
    
    kubectl -n gke-ai-namespace delete -f src/gke-config/service-tfserve.yaml
    kubectl -n gke-ai-namespace delete -f src/gke-config/deployment-tfserve.yaml
    kubectl delete namespace gke-ai-namespace
    

  1. Delete the Cloud Storage bucket:

     1. Go to the **Buckets** page:

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Select the checkbox for `PROJECT_ID-gke-bucket`.

     3. Click delete **Delete**.

     4. To confirm deletion, type `DELETE` and click **Delete**.




### Delete the GKE cluster and the Google Cloud resources

  1. Delete the GKE cluster:

     1. Go to the **Clusters** page:

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

     2. Select the checkbox for `online-serving-cluster`.

     3. Click delete **Delete**.

     4. To confirm deletion, type `online-serving-cluster` and click **Delete**.

  2. Delete the Cloud Storage bucket:

     1. Go to the **Buckets** page:

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Select the checkbox for `PROJECT_ID-gke-bucket`.

     3. Click delete **Delete**.

     4. To confirm deletion, type `DELETE` and click **Delete**.




### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * [Serve an LLM with multiple GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multiple-gpu)
  * [Serve Gemma using TPUs on GKE with JetStream](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-tpu-jetstream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
