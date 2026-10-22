---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gpt-oss-vllm-inference/
title: Use vLLM on GKE to run inference with gpt-oss-120b \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:11.679780+00:00
---

# Use vLLM on GKE to run inference with gpt-oss-120b  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gpt-oss-vllm-inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Use vLLM on GKE to run inference with gpt-oss-120b Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This tutorial shows you how to deploy and serve a [`gpt-oss-120b`](https://huggingface.co/openai/gpt-oss-120b) language model by using the [vLLM framework](https://github.com/vllm-project/vllm). You deploy this model on a Google Kubernetes Engine (GKE) autopilot cluster and consume a single [A4 virtual machine](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) (VM) that has 8 B200 GPUs.

**Important:** To complete this tutorial, you must have reserved the capacity to create an A4 VM. To learn more about your options for reserving capacity in AI Hypercomputer for a future date and time, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

This tutorial is intended for machine learning (ML) engineers, platform administrators and operators, and data and AI specialists who are interested in using Kubernetes container orchestration capabilities to handle inference workloads.

## Objectives

  1. Access `gpt-oss-120b` by using Hugging Face.
  2. Prepare your environment.
  3. Create a GKE cluster in Autopilot mode.
  4. Create a Kubernetes secret for Hugging Face credentials.
  5. Create a Cloud Storage bucket.
  6. Download the model to your Cloud Storage bucket.
  7. Deploy a vLLM container to your GKE cluster.
  8. Interact with the [gpt-oss](https://openai.com/index/introducing-gpt-oss/) language model by using curl.
  9. Clean up.



## Costs

This tutorial uses billable components of Google Cloud, including: 

  * [ GKE pricing](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [ Cloud GPUs pricing](https://cloud.google.com/compute/gpus-pricing)



To generate a cost estimate based on your projected usage, use the [Pricing Calculator](https://cloud.google.com/products/calculator).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

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

  7. Enable the required API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

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

  13. Enable the required API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/container.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.
  15. [Sign in to or create a Hugging Face account](https://huggingface.co/login).



## Access gpt-oss by using Hugging Face

To use Hugging Face to access gpt-oss, do the following:

  1. [Sign in to Hugging Face and explore the gpt-oss model](https://huggingface.co/openai/gpt-oss-120b).
  2. [Create a Hugging Face `read` access token](https://huggingface.co/docs/hub/security-tokens#how-to-manage-user-access-tokens).
  3. Copy and save the `read access` token value. You use it later in this tutorial.



## Prepare your environment

To prepare your environment, set the default environment variables:
    
    
    export PROJECT_ID="YOUR_PROJECT_ID"
    export RESERVATION_URL="YOUR_RESERVATION_NAME"
    export REGION="YOUR_REGION"
    export CLUSTER_NAME="YOUR_CLUSTER_NAME"
    export GCS_BUCKET="YOUR_GCS_BUCKET"
    export HUGGING_FACE_TOKEN="YOUR_HF_TOKEN"
    export NETWORK="YOUR_NETWORK_NAME"
    export SUBNETWORK="YOUR_SUBNETWORK_NAME"
    export PROJECT_NUMBER=$(gcloud projects describe "${PROJECT_ID}" --format="value(projectNumber)")
    
    gcloud config set project "${PROJECT_ID}"
    gcloud config set billing/quota_project "${PROJECT_ID}"

Replace the following:

  * `YOUR_PROJECT_ID`: the ID of the Google Cloud project where you want to create the GKE cluster.

  * `YOUR_RESERVATION_NAME`: the URL of the reservation that you want to use to create your GKE cluster. Based on the project in which the reservation exists, specify one of the following values:

    * The reservation exists in your project: `RESERVATION_NAME`

    * The reservation exists in a different project, and your project can use the reservation: `projects/RESERVATION_PROJECT_ID/reservations/RESERVATION_NAME`

  * `YOUR_REGION`: the region where you want to create your GKE cluster. You can only create the cluster in the region where your reservation exists.

  * `YOUR_CLUSTER_NAME`: the name of the GKE cluster to create.

  * `YOUR_GCS_BUCKET`: the name of the Cloud Storage bucket where you download the model.

  * `YOUR_HF_TOKEN`: the Hugging Face access token that you created in the previous section.

  * `YOUR_NETWORK_NAME`: the network that the GKE cluster uses. Specify one of the following values:

    * If you created a custom network, then specify the name of your network.

    * Otherwise, specify `default`.

  * `YOUR_SUBNETWORK_NAME`: the subnetwork that the GKE cluster uses. Specify one of the following values:

    * If you created a custom subnetwork, then specify the name of your subnetwork. You can only specify a subnetwork that exists in the same region as the reservation.

    * Otherwise, specify `default`.




## Create a GKE cluster in Autopilot mode

To create a GKE cluster in Autopilot mode, run the following command:
    
    
    gcloud container clusters create-auto $CLUSTER_NAME \
        --project=$PROJECT_ID \
        --region=$REGION \
        --release-channel=rapid \
        --network=$NETWORK \
        --subnetwork=$SUBNETWORK

Creating the GKE cluster might take some time to complete. To verify that Google Cloud has finished creating your cluster, go to [Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview) on the Google Cloud console.

## Create a Kubernetes secret for Hugging Face credentials

To create a Kubernetes secret for Hugging Face credentials, do the following:

  1. Configure `kubectl` to communicate with your GKE cluster:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --location=$REGION

  2. Create a Kubernetes secret to store your Hugging Face token:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_token=${HUGGING_FACE_TOKEN} \
             --dry-run=client -o yaml | kubectl apply -f -




## Create a Cloud Storage bucket

If you're using an existing Cloud Storage bucket, ensure that the following are true:

  * Your Cloud Storage bucket is in the same region as your GKE cluster.
  * Your service account has the required `write` permissions on the bucket.



To store your model in a new Cloud Storage bucket, complete the following steps:

  1. Run the following command to create a bucket:
         
         gcloud storage buckets create gs://$GCS_BUCKET --location=$REGION --uniform-bucket-level-access

  2. Grant `write` permissions on the Cloud Storage bucket to the default service account.
         
         gcloud storage buckets add-iam-policy-binding gs://$GCS_BUCKET \
             --member="principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$PROJECT_ID.svc.id.goog/subject/ns/default/sa/default" \
             --role="roles/storage.objectAdmin"




## Download the model to your Cloud Storage bucket

To download the model to your Cloud Storage bucket, complete the following steps:

  1. Create a `gpt-download-job.yaml` file:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: gpt-download-job
           namespace: default
         spec:
           template:
             metadata:
               labels:
                 app: gpt-oss-downloader
               annotations:
                 gke-gcsfuse/volumes: "true"
             spec:
               restartPolicy: OnFailure
               containers:
               - name: downloader
                 image: python:3.11-slim
                 resources:
                   requests:
                     cpu: "4"
                     memory: "16Gi"
                   limits:
                     cpu: "4"
                     memory: "16Gi"
                 env:
                 - name: HUGGING_FACE_HUB_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_token
                 - name: HF_HUB_ENABLE_HF_TRANSFER
                   value: "0"
                 - name: HF_HOME
                   value: "/tmp/hf_cache"
                 command: ["/bin/sh", "-c"]
                 args:
                 - |
                   echo "Installing Hugging Face Hub library..."
                   pip install -U "huggingface_hub"
         
                   echo "Beginning model snapshot download to GCS Fuse..."
                   hf download openai/gpt-oss-120b \
                     --token "$HUGGING_FACE_HUB_TOKEN" \
                     --local-dir /mnt/gcs/gpt-oss-120b \
                     --max-workers 1
         
                   DOWNLOAD_STATUS=$?
         
                   if [ $DOWNLOAD_STATUS -eq 0 ]; then
                     echo "Download Complete!"
                   else 
                     echo "ERROR: Model download failed with exit code $DOWNLOAD_STATUS"
                     exit $DOWNLOAD_STATUS
                   fi
         
                 volumeMounts:
                 - mountPath: /mnt/gcs
                   name: gcs-bucket-volume
               volumes:
               - name: gcs-bucket-volume
                 csi:
                   driver: gcsfuse.csi.storage.gke.io
                   volumeAttributes:
                     bucketName: $GCS_BUCKET
                     mountOptions: "implicit-dirs"

  2. To initialize the download job, apply the `gpt-download-job.yaml` manifest.
         
         envsubst '$GCS_BUCKET' < gpt-download-job.yaml | kubectl apply -f -

The job resource downloads the `gpt-oss-120b` model weights from Hugging Face to your Cloud Storage bucket. The download takes around 30 minutes to complete. Once the download finishes, proceed to the next section to launch the model deployment.

  3. To see the completion status, run the following command:
         
         kubectl wait \
             --for=condition=Complete \
             --timeout=7200s job/gpt-download-job

The `--timeout` flag specifies how long the command monitors the job before timing out.

  4. To delete the job, run the following command:
         
         kubectl delete job gpt-download-job




## Deploy a vLLM container to your GKE cluster

After you've downloaded the model to your Cloud Storage bucket, deploy a vLLM container to your GKE cluster:

  1. Create a `vllm-gpt-oss-120b.yaml` file with your chosen vLLM deployment:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: vllm-gpt-oss-deployment
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: gpt-oss
           template:
             metadata:
               labels:
                 app: gpt-oss
                 ai.gke.io/model: gpt-oss-120b
                 ai.gke.io/inference-server: vllm
                 examples.ai.gke.io/source: user-guide
               annotations:
                 gke-gcsfuse/volumes: "true"
             spec:
               containers:
               - name: vllm-inference
                 image: us-docker.pkg.dev/vertex-ai/vertex-vision-model-garden-dockers/pytorch-vllm-serve:20250822_0916_RC01
                 resources:
                   requests:
                     cpu: "10"
                     memory: "128Gi"
                     ephemeral-storage: "240Gi"
                     nvidia.com/gpu: "8"
                   limits:
                     cpu: "10"
                     memory: "128Gi"
                     ephemeral-storage: "240Gi"
                     nvidia.com/gpu: "8"
                 command: ["python3", "-m", "vllm.entrypoints.openai.api_server"]
                 args:
                 - --model=/mnt/gcs/gpt-oss-120b
                 - --tensor-parallel-size=8
                 - --host=0.0.0.0
                 - --port=8000
                 - --max-model-len=8192
                 - --max-num-seqs=4
                 volumeMounts:
                 - mountPath: /dev/shm
                   name: dshm
                 - mountPath: /mnt/gcs
                   name: gcs-bucket-volume
                   readOnly: true
                 livenessProbe:
                   httpGet:
                     path: /health
                     port: 8000
                   initialDelaySeconds: 900
                   periodSeconds: 10
                 readinessProbe:
                   httpGet:
                     path: /health
                     port: 8000
                   initialDelaySeconds: 900
                   periodSeconds: 5
               volumes:
               - name: dshm
                 emptyDir:
                   medium: Memory
               - name: gcs-bucket-volume
                 csi:
                   driver: gcsfuse.csi.storage.gke.io
                   volumeAttributes:
                     bucketName: $GCS_BUCKET
                     mountOptions: "implicit-dirs,file-cache:max-size-mb:-1,file-cache:enable-parallel-downloads:true,file-cache:max-parallel-downloads:32,file-cache:parallel-downloads-per-file:8,file-cache:download-chunk-size-mb:16"
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-b200
                 cloud.google.com/reservation-name: $RESERVATION_URL
                 cloud.google.com/reservation-affinity: "specific"
                 cloud.google.com/gke-gpu-driver-version: latest
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: oss-service
         spec:
           selector:
             app: gpt-oss
           type: ClusterIP
           ports:
           - protocol: TCP
             port: 8000
             targetPort: 8000
         ---
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: vllm-gpt-oss-monitoring
         spec:
           selector:
             matchLabels:
               app: gpt-oss
           endpoints:
           - port: 8000
             path: /metrics
             interval: 30s

  2. Apply the `vllm-gpt-oss-120b.yaml` file to your GKE cluster:
         
         envsubst < vllm-gpt-oss-120b.yaml | kubectl apply -f -

  3. To see the completion status, run the following command:
         
         kubectl wait \
             --for=condition=Available \
             --timeout=7200s deployment/vllm-gpt-oss-deployment

The `--timeout` flag allows the command to monitor the deployment for the specified period of time.



## Interact with the `gpt-oss` model by using curl

To verify the `gpt-oss` model that you deployed, do the following:

  1. Set up port forwarding to the `gpt-oss` model:
         
         kubectl port-forward service/oss-service 8000:8000

  2. Open a new terminal window. You can then chat with your model by using `curl`:
         
         curl http://127.0.0.1:8000/v1/chat/completions \
         -X POST \
         -H "Content-Type: application/json" \
         -d '{
           "model": "openai/gpt-oss-120b",
           "messages": [
             {
               "role": "user",
               "content": "Describe a sailboat in one short sentence?"
             }
           ]
         }' | jq .

  3. The output that you see is similar to the following:
         
         {
           "id": "chatcmpl-2235c39759c040daae23ce2addc40c0a",
           "object": "chat.completion",
           "created": 1756831629,
           "model": "openai/gpt-oss-120b",
           "choices": [
             {
               "index": 0,
               "message": {
                 "role": "assistant",
                 "content": "A sleek vessel gliding on water, its cloth sails billowing like captured wind.",
                 "refusal": null,
                 "annotations": null,
                 "audio": null,
                 "function_call": null,
                 "tool_calls": [],
                 "reasoning_content": "User asks: \"Describe a sailboat in one short sentence?\" We need to produce a short sentence description. Should comply with policy. It's fine. Provide a short sentence."
               },
               "logprobs": null,
               "finish_reason": "stop",
               "stop_reason": null
             }
           ],
           "service_tier": null,
           "system_fingerprint": null,
           "usage": {
             "prompt_tokens": 80,
             "total_tokens": 142,
             "completion_tokens": 62,
             "prompt_tokens_details": null
           },
           "prompt_logprobs": null,
           "kv_transfer_params": null
         }
         




## Observe the performance of the model

To observe your model's performance, you can use the vLLM dashboard integration in Cloud Monitoring. This dashboard helps you view critical performance metrics for your model like token throughput, network latency, and error rates. For information, see [vLLM](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/vllm) in the Monitoring documentation.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the resources

After you're done with the tutorial, delete the resources that you don't need any longer.

  1. To delete the deployment and service defined in the `vllm-gpt-oss-120b.yaml` file and the Kubernetes secret from the GKE cluster, run the following command:
         
         envsubst < vllm-gpt-oss-120b.yaml | kubectl delete -f -
         kubectl delete secret hf-secret

  2. To delete your Cloud Storage bucket, run the following command:
         
         gcloud storage rm --recursive gs://$GCS_BUCKET

  3. To delete your GKE cluster, do the following:
         
         gcloud container clusters delete $CLUSTER_NAME \
             --region=$REGION \
             --quiet




### Delete your project

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

## What's next

  * [Manage AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters)
  * [Learn about recommended storage services for AI and ML workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/storage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
