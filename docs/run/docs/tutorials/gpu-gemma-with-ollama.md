---
url: https://docs.cloud.google.com/run/docs/tutorials/gpu-gemma-with-ollama/
title: Run LLM inference on GPUs with Gemma 4 and Ollama \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:54:16.395471+00:00
---

# Run LLM inference on GPUs with Gemma 4 and Ollama  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/gpu-gemma-with-ollama/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Run LLM inference on GPUs with Gemma 4 and Ollama Stay organized with collections  Save and categorize content based on your preferences. 

## Objectives

Gemma 4 is Google's most efficient open-weight model family, delivering strong reasoning and agentic capabilities. Long context, multimodality, reasoning, and tool calling let Gemma 4 handle complex logic, multi-step planning, coding, and agentic workflows.

This guide shows how to run LLM inference on Cloud Run GPUs with Gemma and Ollama, and has the following objectives:

  * Deploy [Ollama](https://ollama.com/) with the [Gemma 4](https://ai.google.dev/gemma/docs/core) model on a GPU-enabled Cloud Run service.
  * Send prompts to the Ollama service on its private endpoint.



To learn an alternative way for deploy Gemma 4 open models on Cloud Run using a vLLM container, see [Run Gemma 4 models on Cloud Run](https://docs.cloud.google.com/run/docs/run-gemma-on-cloud-run).

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Run](https://cloud.google.com/run)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Run API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com)

  7. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  8. By default, new projects are automatically granted 3,000 milliGPU quota upon initial deployment. If you need additional quota, request `Total Nvidia RTX Pro 6000 GPU allocation, in milli GPU, without zonal redundancy, per project per region` quota under Cloud Run Admin API in the [Quotas and system limits page](https://g.co/cloudrun/gpu-quota).



### Required roles

To get the permissions that you need to complete the tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to complete the tutorial. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

#### Grant the roles

#### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter your user identifier. This is typically the email address that is used to deploy the Cloud Run service.

  5. In the **Select a role** list, select a role. 
  6. To grant additional roles, click add **Add another role** and add each additional role. 
  7. Click **Save**. 



#### gcloud

To grant the required IAM roles to your account on your project:
    
    
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=PRINCIPAL \
             --role=ROLE
         

Replace:

  * PROJECT_NUMBER with your Google Cloud project number.
  * PROJECT_ID with your Google Cloud project ID.
  * PRINCIPAL with the account you are adding the binding for. This is typically the email address that is used to deploy the Cloud Run service.
  * ROLE with the role you are adding to the deployer account.



## Deploy the Ollama service for LLM inference

Deploy the service to Cloud Run:
    
    
    gcloud beta run deploy SERVICE-NAME \
        --image "ollama/ollama:latest" \
        --project PROJECT_ID \
        --region REGION \
        --no-allow-unauthenticated \
        --cpu 20 \
        --memory 80Gi \
        --gpu 1 \
        --gpu-type nvidia-rtx-pro-6000 \
        --no-gpu-zonal-redundancy \
        --max-instances 1 \
        --concurrency 16 \
        --timeout 600 \
        --set-env-vars=OLLAMA_NUM_PARALLEL=16 \
        --set-env-vars=OLLAMA_HOST=0.0.0.0:8080 \
        --set-env-vars=OLLAMA_DEBUG=false \
        --set-env-vars=OLLAMA_KEEP_ALIVE=-1 \
        --startup-probe tcpSocket.port=8080,initialDelaySeconds=240,failureThreshold=1,timeoutSeconds=240,periodSeconds=240 \
        --command "bash" \
        --args="-c,(sleep 15 && ollama pull MODEL_NAME) & ollama serve"

Replace:

  * `SERVICE-NAME` with a unique name for the Cloud Run service.
  * `PROJECT` with your Google Cloud Project Id.
  * `REGION` with a Google Cloud region where `nvidia-rtx-pro-6000` GPUs are supported for Cloud Run, such as `us-central1`. For a full list of supported regions for GPU-enabled deployments, see [GPU configuration](https://docs.cloud.google.com/run/docs/configuring/services/gpu#supported-regions).

  * `MODEL_NAME` with the full name of a Gemma 4 variant.

    * Gemma 4 E2B: `gemma4:e2b`
    * Gemma 4 E4B: `gemma4:e4b`



Gemma 4 26B and 31B require more [advanced Cloud Run and vLLM configuration with Direct VPC Egress and Run:ai Model Streamer](https://codelabs.developers.google.com/codelabs/cloud-run/cloud-run-gpu-rtx-pro-6000-gemma4-vllm).

Note the following important flags in this command:

  * `--concurrency 16` is set to match the value of the environment variable `OLLAMA_NUM_PARALLEL`.
  * `--gpu 1` with `--gpu-type nvidia-rtx-pro-6000` assigns 1 NVIDIA RTX PRO 6000 Blackwell GPU GPU to every Cloud Run instance in the service.
  * `--max-instances 1` specifies the maximum number of instances to scale to. It has to be equal to or lower than your project's NVIDIA RTX Pro 6000 GPU (`Total NVIDIA RTX Pro 6000 GPU allocation, in milli GPU, without zonal redundancy, per project per region`) quota.
  * `--no-allow-unauthenticated` restricts unauthenticated access to the service. By keeping the service private, you can rely on Cloud Run's built-in [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) authentication for service-to-service communication. Refer to [Managing access using IAM](https://docs.cloud.google.com/run/docs/securing/managing-access).
  * `--no-cpu-throttling` is required for enabling GPU.
  * `--no-gpu-zonal-redundancy` sets zonal redundancy options depending on your zonal failover requirements and available quota. See [GPU zonal redundancy options](https://docs.cloud.google.com/run/docs/configuring/services/gpu#zonal-redundancy) for details.



### Concurrency settings for optimal performance

This section provides context on the recommended concurrency settings. For optimal _request latency_ , ensure the `--concurrency` setting is equal to Ollama's `OLLAMA_NUM_PARALLEL` environment variable.

  * `OLLAMA_NUM_PARALLEL` determines how many request slots are available per each model to handle inference requests concurrently.
  * `--concurrency` determines how many requests Cloud Run sends to an Ollama instance at the same time.



If `--concurrency` exceeds `OLLAMA_NUM_PARALLEL`, Cloud Run can send more requests to a model in Ollama than it has available request slots for. This leads to request queuing within Ollama, increasing request latency for the queued requests. It also leads to less responsive auto scaling, as the queued requests don't trigger Cloud Run to scale out and start new instances.

Ollama also supports serving multiple models from one GPU. To avoid request queuing on the Ollama instance, set `--concurrency` to match `OLLAMA_NUM_PARALLEL`.

Increasing `OLLAMA_NUM_PARALLEL` also makes parallel requests take longer.

#### Optimize GPU utilization

For optimal _GPU utilization_ , increase `--concurrency`, keeping it within twice the value of `OLLAMA_NUM_PARALLEL`. While this leads to request queuing in Ollama, it can help improve utilization: Ollama instances can immediately process requests from their queue, and the queues help absorb traffic spikes.

### Test the deployed Ollama service with curl

Now that you have deployed the Ollama service, you can send requests to it. However, if you send a request directly, Cloud Run responds with `HTTP 401 Unauthorized`. This is intentional, because an LLM inference API is intended for other services to call, such as a frontend application. For more information on service-to-service authentication on Cloud Run, refer to [Authenticating service-to-service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service).

To send requests to the Ollama service, add a header with a valid OIDC token to the requests, for example using the Cloud Run [developer proxy](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/proxy):

  1. Start the proxy, and when prompted to install the `cloud-run-proxy` component, choose `Y`:
         
         gcloud run services proxy SERVICE-NAME \
            --project PROJECT_ID \
            --region REGION \
            --port=9090

  2. Send a request to it in a separate terminal tab, leaving the proxy running. Note that the proxy runs on `localhost:9090`:
         
         curl http://localhost:9090/api/generate -d '{
            "model": "MODEL_NAME",
            "prompt": "Why is the sky blue?",
            "stream": false
         }' | jq -r '.response'

This command should provide streaming output similar to this:
         
         This is one of the most beautiful and fundamental questions in physics! The reason the sky appears blue is due to a phenomenon called **Rayleigh Scattering**.
         ...
         

**Success:** You deployed a GPU-enabled Cloud Run service with Gemma 4 on Ollama and sent an inference request to it.



## Clean up

To avoid additional charges to your Google Cloud account, delete all the resources you deployed with this tutorial.

### Delete the project

If you created a new project for this tutorial, delete the project. If you used an existing project and need to keep it without the changes you added in this tutorial, delete resources that you created for the tutorial.

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete tutorial resources

  1. Delete the Cloud Run service you deployed in this tutorial. Cloud Run services don't incur costs until they receive requests.

To delete your Cloud Run service, run the following command:
         
         gcloud run services delete SERVICE-NAME

Replace SERVICE-NAME with the name of your service.

You can also delete Cloud Run services from the [Google Cloud console](https://console.cloud.google.com/run).

  2. Remove the `gcloud` default region configuration you added during tutorial setup:
         
         gcloud config unset run/region
         

  3. Remove the project configuration:
         
         gcloud config unset project
         




## What's next

  * [Configure GPU](https://docs.cloud.google.com/run/docs/configuring/services/gpu)
  * [Best practices: AI inference on Cloud Run with GPUs](https://docs.cloud.google.com/run/docs/configuring/services/gpu-best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
