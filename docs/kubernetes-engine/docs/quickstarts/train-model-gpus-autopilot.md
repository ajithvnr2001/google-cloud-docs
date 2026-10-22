---
url: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-autopilot/
title: Quickstart: Train a model with GPUs on GKE Autopilot mode \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:13.502950+00:00
---

# Quickstart: Train a model with GPUs on GKE Autopilot mode  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-autopilot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Train a model with GPUs on GKE Autopilot mode

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This quickstart shows you how to deploy a training model with GPUs in Google Kubernetes Engine (GKE) and store the predictions in Cloud Storage. This document is intended for GKE administrators who have existing Autopilot mode clusters and want to run GPU workloads for the first time.

You can also run these workloads on Standard clusters if you create separate GPU node pools in your clusters. For instructions, see [Train a model with GPUs on GKE Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-standard).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the GKE and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,storage.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the GKE and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,storage.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 




## Clone the sample repository

In Cloud Shell, run the following command:
    
    
    git clone https://github.com/GoogleCloudPlatform/ai-on-gke && \
    cd ai-on-gke/tutorials-and-examples/gpu-examples/training-single-gpu
    

## Create a cluster

  1. In the Google Cloud console, go to the **Create an Autopilot cluster** page:

[Go to Create an Autopilot cluster](https://console.cloud.google.com/kubernetes/auto/add)

  2. In the **Name** field, enter `gke-gpu-cluster`.

  3. In the **Region** list, select `us-central1`.

  4. Click **Create**.




## Create a Cloud Storage bucket

  1. In the Google Cloud console, go to the **Create a bucket** page:

[Go to Create a bucket](https://console.cloud.google.com/storage/create-bucket)

  2. In the **Get started** section, enter a globally unique name for your bucket:
         
         PROJECT_ID-gke-gpu-bucket
         

Replace `PROJECT_ID` with your Google Cloud project ID.

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
  2. Create an IAM allow policy that lets the ServiceAccount access the bucket.



### Create a Kubernetes ServiceAccount in your cluster

In Cloud Shell, do the following:

  1. Connect to your cluster:
         
         gcloud container clusters get-credentials gke-gpu-cluster \
             --location=us-central1
         

  2. Create a Kubernetes namespace:
         
         kubectl create namespace gke-gpu-namespace
         

  3. Create a Kubernetes ServiceAccount in the namespace:
         
         kubectl create serviceaccount gpu-k8s-sa --namespace=gke-gpu-namespace
         




### Create an IAM allow policy on the bucket

Grant the Storage Object Admin (`roles/storage.objectAdmin`) role on the bucket to the Kubernetes ServiceAccount:
    
    
    gcloud storage buckets add-iam-policy-binding gs://PROJECT_ID-gke-gpu-bucket \
        --member=principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/gke-gpu-namespace/sa/gpu-k8s-sa \
        --role=roles/storage.objectAdmin \
        --condition=None
    

Replace `PROJECT_NUMBER` with your Google Cloud project number.

## Verify that Pods can access the Cloud Storage bucket

  1. In Cloud Shell, create the following environment variables:
         
         export K8S_SA_NAME=gpu-k8s-sa
         export BUCKET_NAME=PROJECT_ID-gke-gpu-bucket
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Create a Pod that has a [TensorFlow](https://www.tensorflow.org/) container:
         
         envsubst < src/gke-config/standard-tensorflow-bash.yaml | kubectl --namespace=gke-gpu-namespace apply -f -
         

This command inserts the environment variables that you created into the corresponding references in the manifest. You can also open the manifest in a text editor and replace `$K8S_SA_NAME` and `$BUCKET_NAME` with the corresponding values.

  3. Create a sample file in the bucket:
         
         touch sample-file
         gcloud storage cp sample-file gs://PROJECT_ID-gke-gpu-bucket
         

  4. Wait for your Pod to become ready:
         
         kubectl wait --for=condition=Ready pod/test-tensorflow-pod -n=gke-gpu-namespace --timeout=180s
         

When the Pod is ready, the output is the following:
         
         pod/test-tensorflow-pod condition met
         

If the command times out, GKE might still be creating new nodes to run the Pods. Run the command again and wait for the Pod to become ready.

  5. Open a shell in the TensorFlow container:
         
         kubectl -n gke-gpu-namespace exec --stdin --tty test-tensorflow-pod --container tensorflow -- /bin/bash
         

  6. Try to read the sample file that you created:
         
         ls /data
         

The output shows the sample file.

  7. Check the logs to identify the GPU attached to the Pod:
         
         python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
         

The output shows the GPU attached to the Pod, similar to the following:
         
         ...
         PhysicalDevice(name='/physical_device:GPU:0',device_type='GPU')
         

  8. Exit the container:
         
         exit
         

  9. Delete the sample Pod:
         
         kubectl delete -f src/gke-config/standard-tensorflow-bash.yaml \
             --namespace=gke-gpu-namespace
         


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
         
         envsubst < src/gke-config/standard-tf-mnist-train.yaml | kubectl -n gke-gpu-namespace apply -f -
         

This command replaces the environment variables that you created into the corresponding references in the manifest. You can also open the manifest in a text editor and replace `$K8S_SA_NAME` and `$BUCKET_NAME` with the corresponding values.

  5. Wait until the Job has the `Completed` status:
         
         kubectl wait -n gke-gpu-namespace --for=condition=Complete job/mnist-training-job --timeout=180s
         

When the Job is ready, the output is similar to the following:
         
         job.batch/mnist-training-job condition met
         

If the command times out, GKE might still be creating new nodes to run the Pods. Run the command again and wait for the Job to become ready.

  6. Check the logs from the TensorFlow container:
         
         kubectl logs -f jobs/mnist-training-job -c tensorflow -n gke-gpu-namespace
         

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
         
         kubectl -n gke-gpu-namespace delete -f src/gke-config/standard-tf-mnist-train.yaml
         




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
         
         envsubst < src/gke-config/standard-tf-mnist-batch-predict.yaml | kubectl -n gke-gpu-namespace apply -f -
         

This command replaces the environment variables that you created into the corresponding references in the manifest. You can also open the manifest in a text editor and replace `$K8S_SA_NAME` and `$BUCKET_NAME` with the corresponding values.

  4. Wait until the Job has the `Completed` status:
         
         kubectl wait -n gke-gpu-namespace --for=condition=Complete job/mnist-batch-prediction-job --timeout=180s
         

The output is similar to the following:
         
         job.batch/mnist-batch-prediction-job condition met
         

  5. Check the logs from the TensorFlow container:
         
         kubectl logs -f jobs/mnist-batch-prediction-job -c tensorflow -n gke-gpu-namespace
         

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
         
         kubectl -n gke-gpu-namespace delete -f src/gke-config/standard-tf-mnist-batch-predict.yaml
         kubectl delete namespace gke-gpu-namespace
         

  2. Delete the Cloud Storage bucket:

     1. Go to the **Buckets** page:

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Select the checkbox for `PROJECT_ID-gke-gpu-bucket`.

     3. Click delete **Delete**.

     4. To confirm deletion, type `DELETE` and click **Delete**.

  3. Delete the Google Cloud service account:

     1. Go to the **Service accounts** page:

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select your project.

     3. Select the checkbox for `gke-gpu-sa@PROJECT_ID.iam.gserviceaccount.com`.

     4. Click delete **Delete**.

     5. To confirm deletion, click **Delete**.




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

  3. Delete the Google Cloud service account:

     1. Go to the **Service accounts** page:

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select your project.

     3. Select the checkbox for `gke-gpu-sa@PROJECT_ID.iam.gserviceaccount.com`.

     4. Click delete **Delete**.

     5. To confirm deletion, click **Delete**.




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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
