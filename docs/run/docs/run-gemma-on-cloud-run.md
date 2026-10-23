---
url: https://docs.cloud.google.com/run/docs/run-gemma-on-cloud-run/
title: Run agents with Gemma 4 models on Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:56:56.982271+00:00
---

# Run agents with Gemma 4 models on Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/run-gemma-on-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Run agents with Gemma 4 models on Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to deploy [Gemma 4 open models](https://ai.google.dev/gemma/docs/core) on Cloud Run using a prebuilt container with [vLLM](https://docs.vllm.ai/) inference library, and provides guidance on using the deployed Cloud Run service with AI agents built using [Agent Development Kit](https://google.github.io/adk-docs/).

Gemma 4 is the Google's most efficient open-weight model family, delivering strong reasoning and agentic capabilities.

Long context, multimodality, reasoning and tool calling allow Gemma 4 handle complex logic, multi-step planning, coding, and agentic workflows.

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

  6. [Set up your Cloud Run development environment](https://docs.cloud.google.com/run/docs/setup) in your Google Cloud project.
  7. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  8. Ensure you have the following IAM roles granted to your account: 
     * [Cloud Run Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
     * [Project IAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)

#### Learn how to grant the roles

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

  9. By default, new projects are automatically granted 3,000 milliGPU quota upon initial deployment. If you need additional quota, request `Total Nvidia RTX Pro 6000 GPU allocation, in milli GPU, without zonal redundancy, per project per region` quota under Cloud Run Admin API in the [Quotas and system limits page](https://g.co/cloudrun/gpu-quota).
  10. Review the [Cloud Run pricing](https://cloud.google.com/run/pricing) page. To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).



## Deploy a Gemma 4 model with a vLLM container

Gemma 4 offers advanced agentic capabilities, including reasoning, function calling, code generation, and structured output.

Agent Development Kit (ADK) helps you build fully-functional AI agents with Gemma 4.

Use [vLLM](https://docs.vllm.ai/) to serve Gemma as an OpenAI API endpoint. vLLM provides fast and efficient serving for generative models at scale, featuring state-of-the-art serving throughput, efficient memory management with [PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html), continuous batching of incoming requests, quantization support, and optimized CUDA kernels.

**Note:** Gemma 4 26B and 31B require more [advanced Cloud Run and vLLM configuration with Direct VPC Egress and Run:ai Model Streamer](https://codelabs.developers.google.com/codelabs/cloud-run/cloud-run-gpu-rtx-pro-6000-gemma4-vllm).

To deploy Gemma models on Cloud Run, use the following gcloud CLI command with the recommended settings:
    
    
    CONTAINER_ARGS=(
        "serve"
        "MODEL_NAME"
        "--enable-chunked-prefill"
        "--enable-prefix-caching"
        "--generation-config=auto"
        "--enable-auto-tool-choice"
        "--tool-call-parser=gemma4"
        "--reasoning-parser=gemma4"
        "--dtype=bfloat16"
        "--max-num-seqs=64"
        "--gpu-memory-utilization=0.95"
        "--tensor-parallel-size=1"
        "--port=8080"
        "--host=0.0.0.0"
    )
    gcloud beta run deploy SERVICE_NAME \
        --image "us-docker.pkg.dev/vertex-ai/vertex-vision-model-garden-dockers/pytorch-vllm-serve:gemma4" \
        --project PROJECT \
        --region REGION \
        --execution-environment gen2 \
        --no-allow-unauthenticated \
        --cpu 20 \
        --memory 80Gi \
        --gpu 1 \
        --gpu-type nvidia-rtx-pro-6000 \
        --no-gpu-zonal-redundancy \
        --no-cpu-throttling \
        --max-instances 3 \
        --concurrency 64 \
        --timeout 600 \
        --startup-probe tcpSocket.port=8080,initialDelaySeconds=240,failureThreshold=1,timeoutSeconds=240,periodSeconds=240 \
        --command "vllm" \
        --args=$(IFS=','; echo "${CONTAINER_ARGS[*]}")

Replace:

  * `SERVICE_NAME` with a unique name for the Cloud Run service.
  * `PROJECT` with your Google Cloud Project Id.
  * `REGION` with a Google Cloud region where `nvidia-rtx-pro-6000` GPUs are supported for Cloud Run, such as `us-central1`. For a full list of supported regions for GPU-enabled deployments, see [GPU configuration](https://docs.cloud.google.com/run/docs/configuring/services/gpu#supported-regions).

  * `MODEL_NAME` with the full name of a Gemma 4 variant.

    * Gemma 4 2B: `google/gemma-4-E2B-it`
    * Gemma 4 4B: `google/gemma-4-E4B-it`



The other settings are as follows:

Option | Description  
---|---  
[`--concurrency`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--concurrency) | The [maximum number of requests](https://docs.cloud.google.com/run/docs/configuring/concurrency) that can be processed simultaneously by a given instance, such as `8`. See Set concurrency for optimal performance for recommendations on optimal request latency.  
[`--cpu`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--cpu) | The amount of [allocated CPU](https://docs.cloud.google.com/run/docs/configuring/services/cpu) for your service, such as `20`.  
[`--set-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--set-env-vars) | The [environment variables](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables) set for your service. For example, `HF_TOKEN="..."`  
[`--gpu`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--gpu) | The [GPU value](https://docs.cloud.google.com/run/docs/configuring/services/gpu) for your service, such as `1`.  
[`--gpu-type`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--gpu-type) | The [type of GPU](https://docs.cloud.google.com/run/docs/configuring/services/gpu#gpu-type) to use for your service, such as `nvidia-rtx-pro-6000`.  
[`--max-instances`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--max-instances) | The [maximum number of container instances](https://docs.cloud.google.com/run/docs/configuring/max-instances) for your service, such as `1`.  
[`--memory`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--memory) | The amount of [allocated memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) for your service, such as `80Gi`.  
[`--no-invoker-iam-check`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--\[no-\]invoker-iam-check) | Disable invoker IAM checks. See [Secure Cloud Run services tutorial](https://docs.cloud.google.com/run/docs/tutorials/secure-services) for recommendations on how to better secure your app.  
[`--no-cpu-throttling`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--\[no-\]cpu-throttling) | This setting disables CPU throttling when the container is not actively serving requests.  
[`--timeout`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--timeout) | The [time within which a response must be returned](https://docs.cloud.google.com/run/docs/configuring/request-timeout), such as `600` seconds.  
[`--startup-probe`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--startup-probe) | Comma separated settings for [startup probe](https://docs.cloud.google.com/run/docs/reference/rest/v1/Container#Probe) in the form KEY=VALUE. See [Cloud Run Startup Probe](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--startup-probe) for details. With model sizes of Gemma 4, if you are not using [Direct VPC Egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc), it's recommended to set your startup probe timeout to at least 240 seconds.  
  
If you need to modify the default settings or add more customized settings to your Cloud Run service, see [Configure services](https://docs.cloud.google.com/run/docs/configuring).

After completion of the deployed service, a success message is displayed along with the [Cloud Run endpoint URL](https://docs.cloud.google.com/run/docs/triggering/https-request#url) ending with `run.app`.

## Test the deployed Gemma service with curl

Now that you have deployed the Gemma service, you can send requests to it. However, if you send a request directly, Cloud Run responds with `HTTP 401 Unauthorized`. This is intentional, because an LLM inference API is intended for other services to call, such as a front-end application. For more information on service-to-service authentication on Cloud Run, refer to [Authenticating service-to-service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service).

To send requests to the Gemma service, add a header with a valid OIDC token to the requests, for example using the Cloud Run [developer proxy](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/proxy):

  1. Start the proxy, and when prompted to install the `cloud-run-proxy` component, choose `Y`:
         
         gcloud run services proxy SERVICE_NAME \
           --project PROJECT \
           --region REGION \
           --port=9090

  2. Run the following command to send a request in a separate terminal tab, leaving the proxy running. The proxy runs on `localhost:9090`. Specify the Gemma model you previously used:
         
         curl http://localhost:9090/v1/chat/completions \
           -H "Content-Type: application/json" \
           -d '{
             "model": "MODEL_NAME",
             "messages": [{"role": "user", "content": "Why is the sky blue?"}],
             "chat_template_kwargs": {
                  "enable_thinking": true
              },
              "skip_special_tokens": false
           }'

This command should provide an output similar to this:
         
         {
          "id": "chatcmpl-9cf1ab1450487047",
          "object": "chat.completion",
          "created": 1774904187,
          "model": "google/gemma-4-E2B-it",
          "choices": [
            {
              "index": 0,
              "message": {
                "role": "assistant",
                "content": "The short answer is a phenomenon called **Rayleigh scattering**...",
                "function_call": null,
                "tool_calls": [],
                "reasoning": "*   Question: \"Why is the sky blue?\"\n..."
              },
              "finish_reason": "stop",
              "stop_reason": 106
            }
          ],
          "usage": {
            "prompt_tokens": 21,
            "total_tokens": 877,
            "completion_tokens": 856
          }
         }
         

**Success:** You deployed a GPU-enabled Cloud Run service with Gemma 4 and sent an inference request to it.



## Set concurrency for optimal performance

This section provides context on the recommended concurrency settings. For optimal _request latency_ , ensure the `--concurrency` setting is equal to vLLM's `--max-num-seqs` command line argument.

  * `--max-num-seqs` determines how many sequences (requests) are available per each vLLM instance to handle inference concurrently.
  * `--concurrency` determines how many requests Cloud Run sends to a vLLM instance at the same time.



If `--concurrency` exceeds `--max-num-seqs`, Cloud Run can send more requests to a vLLM instance than it has available request slots for. This leads to request queuing within vLLM, increasing request latency for the queued requests. It also leads to less responsive auto scaling, as the queued requests don't trigger Cloud Run to scale out and start new instances.

To completely avoid request queuing on the vLLM instance, you should set `--concurrency` to match `--max-num-seqs`.

It's important to note that increasing `--max-num-seqs` also makes parallel requests take longer, and requires more GPU memory for the KV cache.

#### Optimize utilization

For optimal _GPU utilization_ , increase `--concurrency`, keeping it within twice the value of `--max-num-seqs`. While this leads to request queuing in vLLM, it can help improve utilization: vLLM instances can immediately process requests from their queue, and the queues help absorb traffic spikes.

## Build AI agents with Agent Development Kit using Gemma 4

After you have deployed your Cloud Run service, you can use Cloud Run endpoint with Gemma 4 to create AI agents with the [Agent Development Kit](https://google.github.io/adk-docs/).

Before you use the Agent Development Kit, ensure that incoming requests pass the appropriate identity token. To learn more about using IAM authentication and Cloud Run, see [Authenticating service-to-service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service#use_the_authentication_libraries).

The following example shows how to use the Agent Development Kit in Python with IAM authentication:
    
    
    import subprocess
    from google.adk.models.lite_llm import LiteLlm
    from google.adk.agents import Agent
    
    # Get the identity token using gcloud
    id_token = subprocess.run(
        ["gcloud", "auth", "print-identity-token"],
        capture_output=True, text=True
    ).stdout.strip()
    
    gemma_model = LiteLlm(
        model=f'openai/MODEL_NAME',
        base_url='https://YOUR_CLOUD_RUN_SERVICE_URL/v1',
        extra_body={
            "chat_template_kwargs": {
                "enable_thinking": True
            },
            "skip_special_tokens": False
        },
        extra_headers={
            "Authorization": f"Bearer {id_token}",
        },
    )
    
    root_agent = Agent(
        model=gemma_model,
        name='assistant',
        instruction="You are a helpful assistant",
    )
    

## Clean up

Delete the following Google Cloud resources created:

  * [Cloud Run service](https://docs.cloud.google.com/run/docs/managing/services#delete)



## What's next

  * For larger models and faster startup time with [Run:ai Model Streamer](https://docs.vllm.ai/en/stable/models/extensions/runai_model_streamer/), use codelab [Run inference of Gemma 4 model on Cloud Run with RTX 6000 Pro GPU with vLLM](https://codelabs.developers.google.com/codelabs/cloud-run/cloud-run-gpu-rtx-pro-6000-gemma4-vllm)
  * [Configure GPU](https://docs.cloud.google.com/run/docs/configuring/services/gpu)
  * [Best practices: AI inference on Cloud Run with GPUs](https://docs.cloud.google.com/run/docs/configuring/services/gpu-best-practices)
  * [Run Gemma 4 models with various AI runtime frameworks](https://ai.google.dev/gemma/docs/run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
