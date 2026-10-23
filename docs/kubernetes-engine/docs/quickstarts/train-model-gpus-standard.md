---
url: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-standard/
title: Quickstart: Train a model with GPUs on GKE Standard mode \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:32.247213+00:00
---

# Quickstart: Train a model with GPUs on GKE Standard mode  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-standard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Train a model with GPUs on GKE Standard mode

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This quickstart tutorial shows you how to deploy a training model with GPUs in Google Kubernetes Engine (GKE) and store the predictions in Cloud Storage. This tutorial uses a TensorFlow model and GKE Standard clusters. You can also run these workloads on Autopilot clusters with fewer setup steps. For instructions, see [Train a model with GPUs on GKE Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-autopilot).

This document is intended for GKE administrators who have existing Standard clusters and want to run GPU workloads for the first time.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Kubernetes Engine and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,storage.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Kubernetes Engine and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,storage.googleapis.com)

  10. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 




### Required roles

To get the permissions that you need to train a model on GPUs, ask your administrator to grant you the following IAM roles on your project: 

  * Manage GKE clusters: [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) 
  * Manage Cloud Storage buckets: [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 
  * Grant IAM roles on the project: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Clone the sample repository

In Cloud Shell, run the following command:
    
    
    git clone https://github.com/GoogleCloudPlatform/ai-on-gke/ ai-on-gke
    cd ai-on-gke/tutorials-and-examples/gpu-examples/training-single-gpu
    

## Create a Standard mode cluster and a GPU node pool

Use Cloud Shell to do the following:

  1. Create a Standard cluster that uses [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) and installs the [Cloud Storage FUSE driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver):
         
         gcloud container clusters create gke-gpu-cluster \
             --addons GcsFuseCsiDriver \
             --location=us-central1 \
             --num-nodes=1 \
             --workload-pool=PROJECT_ID.svc.id.goog
         

Replace `PROJECT_ID` with your Google Cloud project ID.

Cluster creation might take several minutes.

  2. Create a GPU node pool:
         
         gcloud container node-pools create gke-gpu-pool-1 \
             --accelerator=type=nvidia-tesla-t4,count=1,gpu-driver-version=default \
             --machine-type=n1-standard-16 --num-nodes=1 \
             --location=us-central1 \
             --cluster=gke-gpu-cluster
         




## Create a Cloud Storage bucket

  1. In the Google Cloud console, go to the **Create a bucket** page:

[Go to Create a bucket](https://console.cloud.google.com/storage/create-bucket)

  2. In the **Name your bucket** field, enter the following name:
         
         PROJECT_ID-gke-gpu-bucket
         

  3. Click **Continue**.

  4. For **Location type** , select **Region**.

  5. In the **Region** list, select `us-central1 (Iowa)` and click **Continue**.

  6. In the **Choose a storage class for your data** section, click **Continue**.

  7. In the **Choose how to control access to objects** section, for **Access control** , select **Uniform**.

  8. Click **Create**.

  9. In the **Public access will be prevented** dialog, ensure that the **Enforce public access prevention on this bucket** checkbox is selected, and click **Confirm**.




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



## Verify that Pods can access the Cloud Storage bucket

  1. In Cloud Shell, create the following environment variables:
         
         export K8S_SA_NAME=gpu-k8s-sa
         export BUCKET_NAME=PROJECT_ID-gke-gpu-bucket
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Create a Pod that has a [TensorFlow](https://www.tensorflow.org/) container:
         
         envsubst < src/gke-config/standard-tensorflow-bash.yaml | kubectl --namespace=gke-ai-namespace apply -f -
         

This command substitutes the environment variables that you created into the corresponding references in the manifest. You can also open the manifest in a text editor and replace `$K8S_SA_NAME` and `$BUCKET_NAME` with the corresponding values.

  3. Create a sample file in the bucket:
         
         touch sample-file
         gcloud storage cp sample-file gs://PROJECT_ID-gke-gpu-bucket
         

  4. Wait for your Pod to become ready:
         
         kubectl wait --for=condition=Ready pod/test-tensorflow-pod -n=gke-ai-namespace --timeout=180s
         

When the Pod is ready, the output is the following:
         
         pod/test-tensorflow-pod condition met
         

  5. Open a shell in the TensorFlow container:
         
         kubectl -n gke-ai-namespace exec --stdin --tty test-tensorflow-pod --container tensorflow -- /bin/bash
         

  6. Try to read the sample file that you created:
         
         ls /data
         

The output shows the sample file.

  7. Check the logs to identify the GPU attached to the Pod:
         
         python3 -m pip install 'tensorflow[and-cuda]'
         python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
         

The output shows the GPU attached to the Pod, similar to the following:
         
         ...
         PhysicalDevice(name='/physical_device:GPU:0',device_type='GPU')
         

  8. Exit the container:
         
         exit
         

  9. Delete the sample Pod:
         
         kubectl delete -f src/gke-config/standard-tensorflow-bash.yaml \
             --namespace=gke-ai-namespace
         


**Success:** At this point, your cluster runs a GPU node pool and can communicate with the Cloud Storage bucket using the Kubernetes ServiceAccount.

## Train and predict using the `MNIST` dataset

In this section, you run a training workload on the `MNIST` example dataset.

  1. Copy the example data to the Cloud Storage bucket:
         
         gcloud storage cp src/tensorflow-mnist-example gs://PROJECT_ID-gke-gpu-bucket/ --recursive
         

  2. Create the following environment variables:
         
         export K8S_SA_NAME=gpu-k8s-sa
         export BUCKET_NAME=PROJECT_ID-gke-gpu-bucket
         

  3. Review the training Job:
         
         # Copyright 2023 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: mnist-training-job
         spec:
           template:
             metadata:
               name: mnist
               annotations:
                 gke-gcsfuse/volumes: "true"
             spec:
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-tesla-t4
               tolerations:
               - key: "nvidia.com/gpu"
                 operator: "Exists"
                 effect: "NoSchedule"
         ** containers:**
               - name: tensorflow
                 image: tensorflow/tensorflow:latest-gpu 
                 command: ["/bin/bash", "-c", "--"]
                 args: ["cd /data/tensorflow-mnist-example; pip install -r requirements.txt; python tensorflow_mnist_train_distributed.py"]
                 resources:
                   limits:
         ** nvidia.com/gpu: 1**
                     cpu: 1
                     memory: 3Gi
                 volumeMounts:
                 - name: gcs-fuse-csi-vol
                   mountPath: /data
                   readOnly: false
               serviceAccountName: $K8S_SA_NAME
               volumes:
               - name: gcs-fuse-csi-vol
                 csi:
                   driver: gcsfuse.csi.storage.gke.io
                   readOnly: false
                   volumeAttributes:
                     bucketName: $BUCKET_NAME
                     mountOptions: "implicit-dirs"
               restartPolicy: "Never"

  4. Deploy the training Job:
         
         envsubst < src/gke-config/standard-tf-mnist-train.yaml | kubectl -n gke-ai-namespace apply -f -
         

This command substitutes the environment variables that you created into the corresponding references in the manifest. You can also open the manifest in a text editor and replace `$K8S_SA_NAME` and `$BUCKET_NAME` with the corresponding values.

  5. Wait until the Job has the `Completed` status:
         
         kubectl wait -n gke-ai-namespace --for=condition=Complete job/mnist-training-job --timeout=180s
         

The output is similar to the following:
         
         job.batch/mnist-training-job condition met
         

  6. Check the logs from the TensorFlow container:
         
         kubectl logs -f jobs/mnist-training-job -c tensorflow -n gke-ai-namespace
         

The output shows the following events occur:

     * Install required Python packages
     * Download the MNIST dataset
     * Train the model using a GPU
     * Save the model
     * Evaluate the model
    
    ...
    Epoch 12/12
    927/938 [============================>.] - ETA: 0s - loss: 0.0188 - accuracy: 0.9954
    Learning rate for epoch 12 is 9.999999747378752e-06
    938/938 [==============================] - 5s 6ms/step - loss: 0.0187 - accuracy: 0.9954 - lr: 1.0000e-05
    157/157 [==============================] - 1s 4ms/step - loss: 0.0424 - accuracy: 0.9861
    Eval loss: 0.04236088693141937, Eval accuracy: 0.9861000180244446
    **Training finished. Model saved**
    

  7. Delete the training workload:
         
         kubectl -n gke-ai-namespace delete -f src/gke-config/standard-tf-mnist-train.yaml
         




## Deploy an inference workload

In this section, you deploy an inference workload that takes a sample dataset as input and returns predictions.

  1. Copy the images for prediction to the bucket:
         
         gcloud storage cp data/mnist_predict gs://PROJECT_ID-gke-gpu-bucket/ --recursive
         

  2. Review the inference workload:
         
         # Copyright 2023 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: mnist-batch-prediction-job
         spec:
           template:
             metadata:
               name: mnist
               annotations:
                 gke-gcsfuse/volumes: "true"
             spec:
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-tesla-t4
               tolerations:
               - key: "nvidia.com/gpu"
                 operator: "Exists"
                 effect: "NoSchedule"
         ** containers:**
               - name: tensorflow
                 image: tensorflow/tensorflow:latest-gpu 
                 command: ["/bin/bash", "-c", "--"]
                 args: ["cd /data/tensorflow-mnist-example; pip install -r requirements.txt; python tensorflow_mnist_batch_predict.py"]
                 resources:
                   limits:
         ** nvidia.com/gpu: 1**
                     cpu: 1
                     memory: 3Gi
                 volumeMounts:
                 - name: gcs-fuse-csi-vol
                   mountPath: /data
                   readOnly: false
               serviceAccountName: $K8S_SA_NAME
               volumes:
               - name: gcs-fuse-csi-vol
                 csi:
                   driver: gcsfuse.csi.storage.gke.io
                   readOnly: false
                   volumeAttributes:
                     bucketName: $BUCKET_NAME
                     mountOptions: "implicit-dirs"
               restartPolicy: "Never"

  3. Deploy the inference workload:
         
         envsubst < src/gke-config/standard-tf-mnist-batch-predict.yaml | kubectl -n gke-ai-namespace apply -f -
         

This command substitutes the environment variables that you created into the corresponding references in the manifest. You can also open the manifest in a text editor and replace `$K8S_SA_NAME` and `$BUCKET_NAME` with the corresponding values.

  4. Wait until the Job has the `Completed` status:
         
         kubectl wait -n gke-ai-namespace --for=condition=Complete job/mnist-batch-prediction-job --timeout=180s
         

The output is similar to the following:
         
         job.batch/mnist-batch-prediction-job condition met
         

  5. Check the logs from the TensorFlow container:
         
         kubectl logs -f jobs/mnist-batch-prediction-job -c tensorflow -n gke-ai-namespace
         

The output is the prediction for each image and the model's confidence in the prediction, similar to the following:
         
         Found 10 files belonging to 1 classes.
         1/1 [==============================] - 2s 2s/step
         The image /data/mnist_predict/0.png is the number 0 with a 100.00 percent confidence.
         The image /data/mnist_predict/1.png is the number 1 with a 99.99 percent confidence.
         The image /data/mnist_predict/2.png is the number 2 with a 100.00 percent confidence.
         The image /data/mnist_predict/3.png is the number 3 with a 99.95 percent confidence.
         The image /data/mnist_predict/4.png is the number 4 with a 100.00 percent confidence.
         The image /data/mnist_predict/5.png is the number 5 with a 100.00 percent confidence.
         The image /data/mnist_predict/6.png is the number 6 with a 99.97 percent confidence.
         The image /data/mnist_predict/7.png is the number 7 with a 100.00 percent confidence.
         The image /data/mnist_predict/8.png is the number 8 with a 100.00 percent confidence.
         The image /data/mnist_predict/9.png is the number 9 with a 99.65 percent confidence.
         


**Success:** You've successfully trained a model and used it to evaluate new data.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources that you created in this guide, do one of the following:

  * **Keep the GKE cluster:** Delete the Kubernetes resources in the cluster and the Google Cloud resources
  * **Keep the Google Cloud project:** Delete the GKE cluster and the Google Cloud resources
  * **Delete the project**



### Delete the Kubernetes resources in the cluster and the Google Cloud resources

  1. Delete the Kubernetes namespace and the workloads that you deployed:
         
         kubectl -n gke-ai-namespace delete -f src/gke-config/standard-tf-mnist-batch-predict.yaml
         kubectl delete namespace gke-ai-namespace
         

  2. Delete the Cloud Storage bucket:

     1. Go to the **Buckets** page:

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Select the checkbox for `PROJECT_ID-gke-gpu-bucket`.

     3. Click delete **Delete**.

     4. To confirm deletion, type `DELETE` and click **Delete**.




### Delete the GKE cluster and the Google Cloud resources

  1. Delete the GKE cluster:

     1. Go to the **Clusters** page:

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

     2. Select the checkbox for `gke-gpu-cluster`.

     3. Click delete **Delete**.

     4. To confirm deletion, type `gke-gpu-cluster` and click **Delete**.

  2. Delete the Cloud Storage bucket:

     1. Go to the **Buckets** page:

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Select the checkbox for `PROJECT_ID-gke-gpu-bucket`.

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

  * [Learn more about using GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
