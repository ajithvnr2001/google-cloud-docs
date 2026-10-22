---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-8b-base/
title: Serve Qwen3-8B-Base with vLLM on TPUs \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:45.524076+00:00
---

# Serve Qwen3-8B-Base with vLLM on TPUs  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-8b-base/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Serve Qwen3-8B-Base with vLLM on TPUs Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to serve the [Qwen/Qwen3-8B-Base model](https://huggingface.co/Qwen/Qwen3-8B-Base) using the [vLLM TPU serving framework](https://github.com/vllm-project/tpu-inference) on a [v6e TPU](https://docs.cloud.google.com/tpu/docs/v6e) VM.

## Objectives

  1. Set up your environment.
  2. Run vLLM with Qwen3-8B-Base.
  3. Send an inference request.
  4. Run a benchmark workload.
  5. Clean up.



## Costs

This tutorial uses billable components of Google Cloud, including: 

  * [ Cloud TPU](https://docs.cloud.google.com/tpu/pricing)
  * [ Compute Engine](https://docs.cloud.google.com/compute/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

## Before you begin

Before going through this tutorial, follow the instructions in the [Set up the Cloud TPU environment](https://docs.cloud.google.com/tpu/docs/setup-gcp-account) page. The instructions guide you through the steps needed to create a Google Cloud project and configure it to use Cloud TPU. You may also use an existing Google Cloud project. If you choose to do so, you can skip the create a Google Cloud project step and start with [Set up your environment to use Cloud TPU](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#set-up-env).

You need a Hugging Face access token to use this tutorial. You can sign up for a free account at [Hugging Face](http://huggingface.co/login). After you have an account, generate an access token:

  1. On the [Welcome to Hugging Face](https://huggingface.co/welcome) page, click your account avatar and select **Access tokens**.
  2. On the **Access tokens** page, click **Create new token**.
  3. Select the **Read** token type and enter a name for your token.
  4. Your access token is displayed. Save the token in a safe place.



## Set up your environment

###  Queued Resources 

Create a Cloud TPU v6e VM using the queued resources API. For Qwen3-8B-Base, we recommend using a v6e-1 TPU.
    
    
    export PROJECT_ID=<PROJECT>
    export TPU_NAME=<TPU_NAME>
    export ZONE=<ZONE>
    export QR_ID=<QR_ID>
    export TPU_TYPE=<TPU_TYPE>

Set the variables:

  * PROJECT \- The name of your project.
  * TPU_NAME \- Name of the TPU VM machine you will create.
  * ZONE \- The cloud zone in which you create the new VM.
  * TPU_TYPE \- The type of TPU VM you create. For example: `v6e-1` or `v6e-4`.
  * QR_ID \- Name of the Queued Resource you create.



Create the Queued Resource request:
    
    
    gcloud alpha compute tpus queued-resources create $QR_ID \
     --node-id $TPU_NAME \
     --project $PROJECT_ID \
     --zone $ZONE \
     --accelerator-type $TPU_TYPE \
     --runtime-version v2-alpha-tpuv6e

Check to make sure your TPU VM is ready.
    
    
    gcloud compute tpus queued-resources describe $QR_ID \
      --project $PROJECT_ID \
      --zone $ZONE

**Tip:** Initially, the status of the queued resource request will be `WAITING_FOR_RESOURCES`. When your TPU VM has been created, the status will change to `ACTIVE`. This can take some time depending on resource availability. If you experience a very long wait time, you might consider trying a different zone. Wait until the status is `ACTIVE` before proceeding.

For example, when the status is `ACTIVE`:
    
    
    name: projects/your-project-id/locations/your-zone/queuedResources/your-queued-resource-id
      state:
      state: ACTIVE
      tpu:
      nodeSpec:
      - node:
          acceleratorType: v6e-1
          bootDisk: {}
          networkConfig:
              enableExternalIps: true
          queuedResource: projects/your-project-number/locations/your-zone/queuedResources/your-queued-resource-id
          runtimeVersion: v2-alpha-tpuv6e
          schedulingConfig: {}
          serviceAccount: {}
          shieldedInstanceConfig: {}
          useTpuVm: true
          nodeId: your-node-id
          parent: projects/your-project-number/locations/your-zone
    

###  Reservation 

Create a Cloud TPU v6e VM using a reservation. For Qwen3-8B-Base, we recommend using a v6e-1 TPU. Start by setting environment variables:
    
    
    export PROJECT_ID="YOUR_PROJECT_ID"
    export TPU_NAME="YOUR_TPU_NAME"
    export ZONE="YOUR_ZONE"
    export TPU_TYPE=v6e-8
    export HF_TOKEN="YOUR_HF_TOKEN"
    export RESERVATION="YOUR_RESERVATION_NAME"

Set the variables:

  * PROJECT \- The name of your project.
  * TPU_NAME \- Name of the TPU VM machine you will create.
  * ZONE \- The cloud zone in which you create the new VM.
  * TPU_TYPE \- The type of TPU VM you create. For example: `v6e-1` or `v6e-4`.
  * RESERVATION \- Name of the reservation with your TPUs.



Create the TPU VM using your reservation:
    
    
    gcloud alpha compute tpus tpu-vm create $TPU_NAME \
        --zone=$ZONE \
        --project $PROJECT_ID \
        --accelerator-type=$TPU_TYPE \
        --version=v2-alpha-tpuv6e \
        --provisioning-model=reservation-bound \
        --reservation=$RESERVATION

Connect to the TPU VM.
    
    
    gcloud compute tpus tpu-vm ssh $TPU_NAME \
      --project $PROJECT_ID \
      --zone $ZONE

## Run vLLM with Qwen3-8B-Base

  1. Set your Hugging Face token and model name variables.
         
         export HF_TOKEN="YOUR_HF_TOKEN"
           export MODEL_NAME="Qwen/Qwen3-8B-Base"
         

  2. Inside the TPU VM, run the vLLM Docker container in detached mode and start the vLLM server. This command uses a shared memory size of 10 GB.
         
         export DOCKER_URI="vllm/vllm-tpu:v0.18.0"
         export CONTAINER_NAME="${USER}-vllm"
         export MAX_MODEL_LEN=4096
         export TP=1 # number of chips
         
         sudo docker run -d --name "${CONTAINER_NAME}" \
             --privileged --net=host \
             -v /dev/shm:/dev/shm \
             --shm-size 10gb \
             -e "HF_HOME=/dev/shm" \
             -e "HF_TOKEN=${HF_TOKEN}" \
             -p 8000:8000 "${DOCKER_URI}" \
                 vllm serve ${MODEL_NAME} \
                     --seed 42 \
                     --gpu-memory-utilization 0.98 \
                     --max-num-batched-tokens 1024 \
                     --max-num-seqs 128 \
                     --tensor-parallel-size $TP \
                     --max-model-len $MAX_MODEL_LEN

  3. Check the server logs to confirm it's running.
         
         sudo docker logs -f "${CONTAINER_NAME}"

When the vLLM server is running you see an output that resembles the following. After the output displays, press `CTRL+C` to return to the terminal.
         
         (APIServer pid=7) INFO:     Started server process [7]
         (APIServer pid=7) INFO:     Waiting for application startup.
         (APIServer pid=7) INFO:     Application startup complete.
         




## Send an inference request

Once the vLLM server is running, you can send requests to the API. For more information, see the [vLLM API reference documentation](https://docs.vllm.ai/en/stable/serving/openai_compatible_server/#api-reference).

  1. Send a test request to the server using `curl`.
         
         sudo docker exec "${CONTAINER_NAME}" \
           curl http://localhost:8000/v1/completions \
             -H "Content-Type: application/json" \
             -d '{
                 "prompt": "The future of AI is",
                 "max_tokens": 200,
                 "temperature": 0
               }'




The response is returned in JSON format.

## Run a benchmark workload

You can run benchmarks against the running server from your second terminal.

  1. Inside the container, install the `datasets` library.
         
         sudo docker exec "${CONTAINER_NAME}" pip install datasets

  2. Inside the container, run the `vllm bench serve` command.
         
         sudo docker exec "${CONTAINER_NAME}" \
             vllm bench serve \
                 --backend vllm \
                 --dataset-name random \
                 --num-prompts 1000 \
                 --seed 100




The benchmark results appear as follows:
    
    
    ============ Serving Benchmark Result ============
    Successful requests:                     1000
    Failed requests:                         0
    Benchmark duration (s):                  73.97
    Total input tokens:                      1024000
    Total generated tokens:                  128000
    Request throughput (req/s):              13.52
    Output token throughput (tok/s):         1730.38
    Peak output token throughput (tok/s):    2522.00
    Peak concurrent requests:                1000.00
    Total Token throughput (tok/s):          15573.42
    ---------------Time to First Token----------------
    Mean TTFT (ms):                          34834.97
    Median TTFT (ms):                        34486.19
    P99 TTFT (ms):                           70234.40
    -----Time per Output Token (excl. 1st token)------
    Mean TPOT (ms):                          47.30
    Median TPOT (ms):                        48.57
    P99 TPOT (ms):                           48.60
    ---------------Inter-token Latency----------------
    Mean ITL (ms):                           47.31
    Median ITL (ms):                         53.49
    P99 ITL (ms):                            54.58
    ==================================================
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

  1. In your terminal, type `exit` to disconnect from the TPU VM.



## Delete your resources

You can delete the project which will delete all resources or you can keep the project and delete the resources.

### Delete your project

To delete your Google Cloud project and all associated resources run:
    
    
        gcloud projects delete $PROJECT_ID
    

### Delete TPU resources

###  Queued Resources 

Delete your Cloud TPU resources. The following command deletes both the queued resource request and the TPU VM using the `--force` parameter.
    
    
    gcloud alpha compute tpus queued-resources delete $QR_ID \
      --project=$PROJECT_ID \
      --zone=$ZONE \
      --force

###  Reservation 

Delete your Cloud TPU VM. Use following command to terminate the VM, releasing the TPUs back to your reservation.
    
    
    gcloud compute tpus tpu-vm delete $TPU_NAME --zone $ZONE --project $PROJECT_ID --quiet

**Note:** You will be still paying for the TPUs, as long as you have your reservation.

## What's next

  * Learn more about [vLLM on Cloud TPU](https://github.com/vllm-project/tpu-inference).
  * Learn more about [Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
