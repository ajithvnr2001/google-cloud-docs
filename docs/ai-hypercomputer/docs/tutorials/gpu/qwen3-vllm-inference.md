---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/qwen3-vllm-inference/
title: Use vLLM on GKE to run inference with Qwen3 \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:32.386588+00:00
---

# Use vLLM on GKE to run inference with Qwen3  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/qwen3-vllm-inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Use vLLM on GKE to run inference with Qwen3 Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This tutorial shows you how to deploy and serve a [Qwen3](https://huggingface.co/Qwen/models) large language model (LLM) with the [vLLM serving framework](https://github.com/vllm-project/vllm). You deploy the model on a single [A4 virtual machine](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) (VM) instance on Google Kubernetes Engine (GKE).

**Important:** To complete this tutorial, you must have reserved the capacity to create an A4 VM. To learn more about your options for reserving capacity in AI Hypercomputer for a future date and time, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

This tutorial is intended for machine learning (ML) engineers, platform administrators and operators, and for data and AI specialists who are interested in using Kubernetes container orchestration capabilities to handle inference workloads.

## Objectives

  1. Access Qwen3 by using Hugging Face.

  2. Prepare your environment.

  3. Create a GKE cluster in Autopilot mode.

  4. Create a Cloud Storage bucket.

  5. Create a Kubernetes secret for Hugging Face credentials.

  6. Configure Workload Identity Federation for Cloud Storage.

  7. Populate the Cloud Storage bucket with the Qwen3 model.

  8. Deploy a vLLM container to your GKE.

  9. Interact with Qwen3 by using curl.

  10. Clean up.




## Costs

This tutorial uses billable components of Google Cloud, including: 

  * [ GKE pricing](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [ GPU pricing](https://cloud.google.com/compute/gpus-pricing)



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



## Access Qwen3 by using Hugging Face

To use Hugging Face to access Qwen3, follow these steps:

  1. [Sign in to Hugging Face](https://huggingface.co/Qwen/models)
  2. [Create a Hugging Face `read` access token](https://huggingface.co/docs/hub/security-tokens#how-to-manage-user-access-tokens). Click **Your Profile > Settings > Access Tokens > +Create new token**.
  3. Specify a name of your choice for the token and then select a role. The minimum role permission level that you can select for this tutorial is **Read**.
  4. Select **Create token**.
  5. Copy and save the generated token to your clipboard. You use it later in this tutorial.



## Prepare your environment

To prepare your environment, set the default environment variables:
    
    
    export PROJECT_ID="YOUR_PROJECT_ID"
    export RESERVATION_NAME="YOUR_RESERVATION_NAME"
    export REGION="YOUR_REGION"
    export CLUSTER_NAME="YOUR_CLUSTER_NAME"
    export GCS_BUCKET_NAME="YOUR_GCS_BUCKET"
    export HUGGING_FACE_TOKEN="YOUR_HF_TOKEN"
    export NETWORK="YOUR_NETWORK_NAME"
    export SUBNETWORK="YOUR_SUBNETWORK_NAME"
    
    gcloud config set project "${PROJECT_ID}"
    gcloud config set billing/quota_project "${PROJECT_ID}"

Replace the following:

  * `YOUR_PROJECT_ID`: the ID of the Google Cloud project where you want to create the GKE cluster.

  * `YOUR_RESERVATION_NAME`: the name of the reservation that you want to use to create your GKE cluster. Based on the project in which the reservation exists, specify one of the following values:

    * The reservation exists in your project: `RESERVATION_NAME`

    * The reservation exists in a different project, and your project can use the reservation: `projects/RESERVATION_PROJECT_ID/reservations/RESERVATION_NAME`

  * `YOUR_REGION`: the region where you want to create your GKE cluster. You can only create the cluster in the region where your reservation exists.

  * `YOUR_CLUSTER_NAME`: the name of the GKE cluster to create.

  * `YOUR_BUCKET_NAME`: the name of the regional Cloud Storage bucket to create.

  * `YOUR_HF_TOKEN`: the Hugging Face access token that you created in the previous section.

  * `YOUR_NETWORK_NAME`: the network that the GKE cluster uses. Specify one of the following values:

    * If you created a custom network, then specify the name of your network.

    * Otherwise, specify `default`.

  * `YOUR_SUBNETWORK_NAME`: the subnetwork that the GKE cluster uses. Specify one of the following values:

    * If you created a custom subnetwork, then specify the name of your subnetwork. You can only specify a subnetwork that exists in the same region as the reservation.

    * Otherwise, specify `default`.




## Create a GKE cluster in Autopilot mode

To create a GKE cluster in Autopilot mode, run the following command:
    
    
    gcloud container clusters create-auto "$CLUSTER_NAME" \
        --project="$PROJECT_ID" \
        --region="$REGION" \
        --release-channel=rapid \
        --network="$NETWORK" \
        --subnetwork="$SUBNETWORK"

Creating the GKE cluster might take some time to complete. To verify that Google Cloud has finished creating your cluster, go to [Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview) on the Google Cloud console. 

## Create a Cloud Storage bucket

To create a regional Cloud Storage bucket to store your model, run the following command:
    
    
    gcloud storage buckets create gs://$GCS_BUCKET_NAME \
        --project=$PROJECT_ID \
        --location=$REGION

## Create a Kubernetes secret for Hugging Face credentials

To create a Kubernetes secret for Hugging Face credentials, follow these steps:

  1. Configure `kubectl` to communicate with your GKE cluster:
         
         gcloud container clusters get-credentials "$CLUSTER_NAME" \
             --location="$REGION" \
             --project="$PROJECT_ID"

  2. Create a Kubernetes secret to store your Hugging Face token:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_token="${HUGGING_FACE_TOKEN}" \
             --dry-run=client -o yaml | kubectl apply -f -




## Configure Workload Identity Federation for Cloud Storage

To allow GKE to securely access the Cloud Storage bucket, set up GKE Workload Identity Federation:
    
    
    gcloud iam service-accounts create qwen-gcs-sa \
        --project=$PROJECT_ID
    
    gcloud storage buckets add-iam-policy-binding gs://$GCS_BUCKET_NAME \
        --member="serviceAccount:qwen-gcs-sa@$PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/storage.objectAdmin"
    
    kubectl create serviceaccount qwen-ksa \
        --namespace=default
    
    gcloud iam service-accounts add-iam-policy-binding qwen-gcs-sa@$PROJECT_ID.iam.gserviceaccount.com \
        --project=$PROJECT_ID \
        --role=roles/iam.workloadIdentityUser \
        --member="serviceAccount:$PROJECT_ID.svc.id.goog[default/qwen-ksa]"
    
    kubectl annotate serviceaccount qwen-ksa \
        --namespace=default \
        iam.gke.io/gcp-service-account="qwen-gcs-sa@$PROJECT_ID.iam.gserviceaccount.com"

## Populate the Cloud Storage bucket with the Qwen3 model weights

To populate your Cloud Storage bucket with the Qwen3 model weights, run a Kubernetes Job that uses the Cloud Storage FUSE CSI driver to mount your bucket as a volume. The job downloads the model from Hugging Face if it does not already exist in the bucket.

  1. Create a file named `qwen3-model-loader.yaml` with the following content:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: qwen3-model-loader
         spec:
           template:
             metadata:
               annotations:
                 gke-gcsfuse/volumes: "true"
                 gke-gcsfuse/cpu-limit: "0"
                 gke-gcsfuse/memory-limit: "0"
                 gke-gcsfuse/ephemeral-storage-limit: "0"
             spec:
               serviceAccountName: qwen-ksa
               restartPolicy: OnFailure
               containers:
               - name: downloader
                 image: python:3.11-slim
                 resources:
                   requests:
                     cpu: "4"
                     memory: "16Gi"
                     ephemeral-storage: "100Gi"
                   limits:
                     cpu: "4"
                     memory: "16Gi"
                     ephemeral-storage: "100Gi"
                 command: ["/bin/sh", "-c"]
                 args:
                 - |
                   pip install huggingface_hub
                   python3 -c '
                   import os
                   from huggingface_hub import snapshot_download
                   model_id = "Qwen/Qwen3-235B-A22B-Instruct-2507"
                   local_dir = "/data/Qwen/Qwen3-235B-A22B-Instruct-2507"
                   config_path = os.path.join(local_dir, "config.json")
                   if os.path.exists(config_path):
                       print(f"Model already exists at {local_dir}. Skipping download.")
                   else:
                       print(f"Downloading model {model_id} to {local_dir}...")
                       snapshot_download(
                           repo_id=model_id,
                           local_dir=local_dir,
                           local_dir_use_symlinks=False,
                           token=os.environ.get("HUGGING_FACE_HUB_TOKEN")
                       )
                       print("Download completed successfully!")
                   '
                 env:
                 - name: HUGGING_FACE_HUB_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_token
                 volumeMounts:
                 - name: gcs-fuse-volume
                   mountPath: /data
               volumes:
               - name: gcs-fuse-volume
                 csi:
                   driver: gcsfuse.csi.storage.gke.io
                   volumeAttributes:
                     bucketName: $GCS_BUCKET_NAME
                     mountOptions: "implicit-dirs"

  2. Apply the `qwen3-model-loader.yaml` manifest to initialize the download job:
         
         envsubst < qwen3-model-loader.yaml | kubectl apply -f -

  3. To verify that the job is running, stream the download job logs:
         
         kubectl logs -f job/qwen3-model-loader -c downloader
         

  4. Wait for the model download job to complete:
         
         kubectl wait \
             --for=condition=Complete \
             --timeout=1800s job/qwen3-model-loader

  5. To delete the job, run the following command:
         
         kubectl delete job qwen3-model-loader --ignore-not-found




## Deploy a vLLM container to your GKE cluster

To deploy the vLLM container to serve the Qwen3 model by using Kubernetes Deployments, do the following:

  1. Create a `qwen3-235b-deploy.yaml` file with your chosen vLLM deployment:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: vllm-qwen3-deployment
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: qwen3-server
           template:
             metadata:
               labels:
                 app: qwen3-server
                 ai.gke.io/model: Qwen3-235B-A22B-Instruct-2507
                 ai.gke.io/inference-server: vllm
                 examples.ai.gke.io/source: user-guide
             spec:
               serviceAccountName: qwen-ksa
               containers:
               - name: qwen-inference-server
                 image: us-docker.pkg.dev/vertex-ai/vertex-vision-model-garden-dockers/pytorch-vllm-serve:20250801_0916_RC01
                 resources:
                   requests:
                     cpu: "10"
                     memory: "1000Gi"
                     ephemeral-storage: "500Gi"
                     nvidia.com/gpu: "8"
                   limits:
                     cpu: "10"
                     memory: "1000Gi"
                     ephemeral-storage: "500Gi"
                     nvidia.com/gpu: "8"
                 command: ["python3", "-m", "vllm.entrypoints.openai.api_server"]
                 args:
                 - --model=$(MODEL_ID)
                 - --load-format=runai_streamer
                 - --model-loader-extra-config={"distributed":true}
                 - --tensor-parallel-size=8
                 - --host=0.0.0.0
                 - --port=8000
                 - --max-model-len=8192
                 - --max-num-seqs=4
                 - --dtype=bfloat16
                 env:
                 - name: MODEL_ID
                   value: "gs://$GCS_BUCKET_NAME/Qwen/Qwen3-235B-A22B-Instruct-2507"
                 - name: HUGGING_FACE_HUB_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_token
                 volumeMounts:
                 - mountPath: /dev/shm
                   name: dshm
                 livenessProbe:
                   httpGet:
                     path: /health
                     port: 8000
                   initialDelaySeconds: 200
                   periodSeconds: 10
                 readinessProbe:
                   httpGet:
                     path: /health
                     port: 8000
                   initialDelaySeconds: 200
                   periodSeconds: 5
               volumes:
               - name: dshm
                 emptyDir:
                   medium: Memory
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-b200
                 cloud.google.com/reservation-name: $RESERVATION_NAME
                 cloud.google.com/reservation-affinity: "specific"
                 cloud.google.com/gke-gpu-driver-version: latest
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: qwen3-service
         spec:
           selector:
             app: qwen3-server
           type: ClusterIP
           ports:
             - protocol: TCP
               port: 8000
               targetPort: 8000
         ---
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: vllm-qwen3-monitoring
         spec:
           selector:
             matchLabels:
               app: qwen3-server
           endpoints:
           - port: 8000
             path: /metrics
             interval: 30s

  2. Apply the `qwen3-235b-deploy.yaml` file to your GKE cluster:
         
         envsubst < qwen3-235b-deploy.yaml | kubectl apply -f -

Because the container uses Run:ai Model Streamer to stream model weights directly from Cloud Storage, the startup time is significantly accelerated.
  3. To see the completion status, run the following command:
         
         kubectl wait \
             --for=condition=Available \
             --timeout=1800s deployment/vllm-qwen3-deployment

The `--timeout=600s` flag allows the command to monitor the deployment for up to 10 minutes.



## Interact with Qwen3 by using curl

To verify the Qwen3 model that you deployed, do the following:

  1. Set up port forwarding to Qwen3:
         
         kubectl port-forward service/qwen3-service 8000:8000

  2. Open a new terminal window. You can then chat with your model by using `curl`:
         
         curl http://127.0.0.1:8000/v1/chat/completions \
         -X POST \
         -H "Content-Type: application/json" \
         -d '{
           "model": "Qwen/Qwen3-235B-A22B-Instruct-2507",
           "messages": [
             {
               "role": "user",
               "content": "Describe a GPU in one short sentence?"
             }
           ],
           "stream": false
         }' | jq .

  3. The output is similar to the following:
         
         {
           "id": "chatcmpl-a926ddf7ef2745ca832bda096e867764",
           "object": "chat.completion",
           "created": 1755023619,
           "model": "Qwen/Qwen3-235B-A22B-Instruct-2507",
           "choices": [
             {
               "index": 0,
               "message": {
                 "role": "assistant",
                 "content": "A GPU is a specialized electronic circuit designed to rapidly process and render graphics and perform parallel computations.",
                 "refusal": null,
                 "annotations": null,
                 "audio": null,
                 "function_call": null,
                 "tool_calls": [],
                 "reasoning_content": null
               },
               "logprobs": null,
               "finish_reason": "stop",
               "stop_reason": null
             }
           ],
           "service_tier": null,
           "system_fingerprint": null,
           "usage": {
             "prompt_tokens": 16,
             "total_tokens": 36,
             "completion_tokens": 20,
             "prompt_tokens_details": null
           },
           "prompt_logprobs": null,
           "kv_transfer_params": null
         }
         




## Observe model performance

If you want to observe your model's performance, then you can use the vLLM dashboard integration in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). This dashboard helps you view critical performance metrics for your model like token throughput, network latency, and error rates. For information, see [vLLM](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/vllm) in the Monitoring documentation.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

To avoid incurring charges to your Cloud Billing account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources.

### Delete the resources

To delete the tutorial resources, run the following commands:
    
    
    envsubst < qwen3-235b-deploy.yaml | kubectl delete -f -
    envsubst < qwen3-model-loader.yaml | kubectl delete -f -
    kubectl delete secret hf-secret
    kubectl delete serviceaccount qwen-ksa
    
    gcloud iam service-accounts delete qwen-gcs-sa@$PROJECT_ID.iam.gserviceaccount.com \
        --project=$PROJECT_ID --quiet
    
    gcloud storage rm --recursive gs://$GCS_BUCKET_NAME

### Delete your GKE cluster

To delete your GKE cluster, run the following command:
    
    
    gcloud container clusters delete "$CLUSTER_NAME" \
        --region="$REGION" \
        --project="$PROJECT_ID" \
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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
