---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma-3-vllm-inference/
title: Use vLLM on GKE to serve Gemma 3 27B inference \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:09.052375+00:00
---

# Use vLLM on GKE to serve Gemma 3 27B inference  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma-3-vllm-inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Use vLLM on GKE to serve Gemma 3 27B inference Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This tutorial shows you how to deploy and serve a [Gemma 3 27B](https://ai.google.dev/gemma/docs/core/model_card_3) large language model (LLM) with the [vLLM serving framework](https://github.com/vllm-project/vllm). You deploy Gemma 3 on a single A4 virtual machine (VM) instance on Google Kubernetes Engine (GKE).

**Important:** To complete this tutorial, you must have reserved the capacity to create an A4 VM. To learn more about your options for reserving capacity in AI Hypercomputer for a future date and time, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

This tutorial is intended for machine learning (ML) engineers, platform administrators and operators, and data and AI specialists who are interested in using Kubernetes container orchestration capabilities to handle inference workloads.

## Objectives

  1. Access Gemma 3 by using Hugging Face.

  2. Prepare your environment.

  3. Create a GKE cluster in Autopilot mode.

  4. Create a Kubernetes secret for Hugging Face credentials.

  5. Deploy a vLLM container to your GKE cluster.

  6. Interact with Gemma 3 by using curl.

  7. Clean up.




## Costs

This tutorial uses billable components of Google Cloud, including: 

  * [ Google Kubernetes Engine pricing](https://docs.cloud.google.com/kubernetes-engine/pricing)
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



## Access Gemma 3 by using Hugging Face

To use Hugging Face to access Gemma 3, do the following:

  1. [Sign in to Hugging Face](https://huggingface.co/google/gemma-3-27b-it)
  2. [Create a Hugging Face `read` access token](https://huggingface.co/docs/hub/security-tokens#how-to-manage-user-access-tokens). Click **Your Profile > Settings > Access tokens > +Create new token**
  3. Copy and save the `read access` token value. You use it later in this tutorial.



## Prepare your environment

To prepare your environment, set the default environment variables:
    
    
    export PROJECT_ID="YOUR_PROJECT_ID"
    export RESERVATION_URL="YOUR_RESERVATION_NAME"
    export REGION="YOUR_REGION"
    export CLUSTER_NAME="YOUR_CLUSTER_NAME"
    export HUGGING_FACE_TOKEN="YOUR_HF_TOKEN"
    export NETWORK="YOUR_NETWORK_NAME"
    export SUBNETWORK="YOUR_SUBNETWORK_NAME"
    
    gcloud config set project "${PROJECT_ID}"
    gcloud config set billing/quota_project "${PROJECT_ID}"

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project where you want to create the GKE cluster.

  * `RESERVATION_URL`: the URL of the reservation that you want to use to create your GKE cluster. Based on the project in which the reservation exists, specify one of the following values:

    * The reservation exists in your project: `RESERVATION_NAME`

    * The reservation exists in a different project, and your project can use the reservation: `projects/RESERVATION_PROJECT_ID/reservations/RESERVATION_NAME`

  * `REGION`: the region where you want to create your GKE cluster. You can only create the cluster in the region where you reservation exists.

  * `CLUSTER_NAME`: the name of the GKE cluster to create.

  * `YOUR_HF_TOKEN`: the Hugging Face access token that you created in the previous section.

  * `NETWORK`: the network that the GKE cluster uses. Specify one of the following values:

    * If you created a custom network, then specify the name of your network.

    * Otherwise, specify `default`.

  * `SUBNETWORK`: the subnetwork that the GKE cluster uses. Specify one of the following values:

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

To create a Kubernetes secret for Hugging Face credentials, follow these steps:

  1. Configure `kubectl` to communicate with your GKE cluster:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --location=$REGION

  2. Create a Kubernetes secret to store your Hugging Face token:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_api_token=${HUGGING_FACE_TOKEN} \
             --dry-run=client -o yaml | kubectl apply -f -




## Deploy a vLLM container to your GKE cluster

To deploy the vLLM container to serve the Gemma 3 27B model by using Kubernetes Deployments, follow these steps:

  1. Create a `vllm-3-27b-it.yaml` file with your chosen vLLM deployment:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: vllm-gemma-deployment
         spec:
           progressDeadlineSeconds: 900
           replicas: 1
           selector:
             matchLabels:
               app: gemma-server
           template:
             metadata:
               labels:
                 app: gemma-server
                 ai.gke.io/model: gemma-3-27b-it
                 ai.gke.io/inference-server: vllm
                 examples.ai.gke.io/source: user-guide
             spec:
               containers:
               - name: inference-server
                 image: us-docker.pkg.dev/vertex-ai/vertex-vision-model-garden-dockers/pytorch-vllm-serve:20250801_0916_RC01
                 resources:
                   requests:
                     cpu: "10"
                     memory: "128Gi"
                     ephemeral-storage: "120Gi"
                     nvidia.com/gpu: "8"
                   limits:
                     cpu: "10"
                     memory: "128Gi"
                     ephemeral-storage: "120Gi"
                     nvidia.com/gpu: "8"
                 command: ["python3", "-m", "vllm.entrypoints.openai.api_server"]
                 args:
                 - --model=$(MODEL_ID)
                 - --tensor-parallel-size=8
                 - --host=0.0.0.0
                 - --port=8000
                 - --max-model-len=4096
                 - --max-num-seqs=4
                 env:
                 - name: MODEL_ID
                   value: google/gemma-3-27b-it
                 - name: HUGGING_FACE_HUB_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_api_token
                 volumeMounts:
                 - mountPath: /dev/shm
                   name: dshm
                 livenessProbe:
                   httpGet:
                     path: /health
                     port: 8000
                   initialDelaySeconds: 720
                   periodSeconds: 10
                 readinessProbe:
                   httpGet:
                     path: /health
                     port: 8000
                   initialDelaySeconds: 720
                   periodSeconds: 5
               volumes:
               - name: dshm
                 emptyDir:
                     medium: Memory
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-b200
                 cloud.google.com/reservation-name: $RESERVATION_URL
                 cloud.google.com/reservation-affinity: "specific"
                 cloud.google.com/gke-gpu-driver-version: latest
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: llm-service
         spec:
           selector:
             app: gemma-server
           type: ClusterIP
           ports:
             - protocol: TCP
               port: 8000
               targetPort: 8000

  2. Apply the `vllm-3-27b-it.yaml` file to your GKE cluster:
         
         envsubst < vllm-3-27b-it.yaml | kubectl apply -f -

During the deployment process, the container must download Gemma 3 from Hugging Face. For this reason, deployment of the container might take up to 30 minutes to complete.

  3. Wait for the deployment to complete:
         
         kubectl wait \
             --for=condition=Available \
             --timeout=1800s deployment/vllm-gemma-deployment




## Interact with Gemma 3 by using curl

To verify your deployed Gemma 3 27B instruction-tuned models, follow these steps:

  1. Set up port forwarding to Gemma 3:
         
         kubectl port-forward service/llm-service 8000:8000

  2. Open a new terminal window. You can then chat with your model by using `curl`:
         
         curl http://127.0.0.1:8000/v1/chat/completions \
         -X POST \
         -H "Content-Type: application/json" \
         -d '{
           "model": "google/gemma-3-27b-it",
           "messages": [
             {
               "role": "user",
               "content": "Why is the sky blue?"
             }
           ]
         }' | jq .

The output is similar to the following:
         
         {
           "id": "chatcmpl-e4a2e624bea849d9b09f838a571c4d9e",
           "object": "chat.completion",
           "created": 1741763029,
           "model": "google/gemma-3-27b-it",
           "choices": [
             {
               "index": 0,
               "message": {
                 "role": "assistant",
                 "reasoning_content": null,
                 "content": "Okay, let's break down why the sky appears blue! It's a fascinating phenomenon rooted in physics, specifically something called **Rayleigh scattering**. Here's the explanation: ...",
                 "tool_calls": []
               },
               "logprobs": null,
               "finish_reason": "stop",
               "stop_reason": 106
             }
           ],
           "usage": {
             "prompt_tokens": 15,
             "total_tokens": 668,
             "completion_tokens": 653,
             "prompt_tokens_details": null
           },
           "prompt_logprobs": null
         }
         




If you want to observe your model's performance, then you can use the vLLM dashboard integration in Cloud Monitoring. This dashboard helps you view critical performance metrics for your model like token throughput, network latency, and error rates. For information, see [vLLM](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/vllm) in the Monitoring documentation.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the resources

  1. To delete the deployment and service defined in the `vllm-3-27b-it.yaml` file and the Kubernetes secret from the GKE cluster, run the following:
         
         envsubst < vllm-3-27b-it.yaml | kubectl delete -f -
         kubectl delete secret hf-secret

  2. To delete your GKE cluster, run the following command:
         
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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
