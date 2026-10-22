---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/serve-3p-llms/
title: Serve LLMs like DeepSeek-R1 671B or Llama 3.1 405B on bare metal \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:37.954554+00:00
---

# Serve LLMs like DeepSeek-R1 671B or Llama 3.1 405B on bare metal  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/serve-3p-llms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Serve LLMs like DeepSeek-R1 671B or Llama 3.1 405B on bare metal Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This guide shows you how to serve state-of-the-art large language models (LLMs) such as [DeepSeek-R1 671B](https://github.com/deepseek-ai/DeepSeek-R1) or [Llama 3.1 405B](https://github.com/meta-llama/llama) on Distributed Cloud software only for bare metal using graphical processing units (GPUs) across multiple nodes.

This guide demonstrates how to use portable open-source technologies, Kubernetes, [vLLM](https://docs.vllm.ai/en/latest/), and the [LeaderWorkerSet](https://github.com/kubernetes-sigs/lws) (LWS) API to deploy and serve AI/ML workloads on bare metal clusters. Google Distributed Cloud extends GKE for use in an on-premises environment, while providing the advantages of GKE's granular control, scalability, resilience, portability, and cost-effectiveness.

## Background

This section describes the key technologies used in this guide, including the two LLMs used as examples in this guide: DeepSeek-R1 and Llama 3.1 405B.

### DeepSeek-R1

DeepSeek-R1, a 671B parameter large language model by DeepSeek, is designed for logical inference, mathematical reasoning, and real-time problem-solving in various text-based tasks. Google Distributed Cloud handles the computational demands of DeepSeek-R1, supporting its capabilities with scalable resources, distributed computing, and efficient networking.

To learn more, see the [DeepSeek documentation](https://www.deepseek.com/).

### Llama 3.1 405B

Llama 3.1 405B is a large language model by Meta that's designed for a wide range of natural language processing tasks, including text generation, translation, and question answering. Google Distributed Cloud offers the robust infrastructure required to support the distributed training and serving needs of models of this scale.

To learn more, see the [Llama documentation](https://www.llama.com/).

### Google Distributed Cloud managed Kubernetes service

Google Distributed Cloud offers a wide range of services, including Distributed Cloud software only for bare metal, which is well-suited to deploying and managing AI/ML workloads in your own data center. Google Distributed Cloud is a managed Kubernetes service that simplifies deploying, scaling, and managing containerized applications. Google Distributed Cloud provides the necessary infrastructure, including scalable resources, distributed computing, and efficient networking, to handle the computational demands of LLMs.

To learn more about key Kubernetes concepts, see [Start learning about Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes). To learn more about the Google Distributed Cloud and how it helps you scale, automate, and manage Kubernetes, see [Distributed Cloud software only for bare metal overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal).

### GPUs

Graphical processing units (GPUs) let you accelerate specific workloads, such as machine learning and data processing. Google Distributed Cloud supports nodes equipped with these powerful GPUs, allowing you to configure your cluster for optimal performance in machine learning and data processing tasks. Google Distributed Cloud provides a range of machine type options for node configuration, including machine types with NVIDIA H100, L4, and A100 GPUs.

To learn more, see [Install or uninstall the bundled NVIDIA GPU Operator](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#gpu-oper) or [Set up and use NVIDIA GPUs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/gpu-manual-use).

### LeaderWorkerSet (LWS)

[LeaderWorkerSet (LWS)](https://github.com/kubernetes-sigs/lws) is a Kubernetes deployment API that addresses common deployment patterns of AI/ML multi-node inference workloads. Multi-node serving leverages multiple Pods, each potentially running on a different node, to handle the distributed inference workload. LWS enables treating multiple Pods as a group, simplifying the management of distributed model serving.

### vLLM and multi-host serving

When serving computationally intensive LLMs, we recommend using vLLM and running the workloads across GPUs.

vLLM is a highly optimized open source LLM serving framework that can increase serving throughput on GPUs, with features such as the following:

  * Optimized transformer implementation with [PagedAttention](https://huggingface.co/docs/text-generation-inference/en/conceptual/paged_attention)

  * Continuous batching to improve the overall serving throughput

  * Distributed serving on multiple GPUs




With especially computationally intensive LLMs that can't fit into a single GPU node, you can use multiple GPU nodes to serve the model. [vLLM supports running workloads across GPUs with two strategies](https://docs.vllm.ai/en/stable/serving/distributed_serving.html#how-to-decide-the-distributed-inference-strategy):

  * **Tensor parallelism** splits the matrix multiplications in the transformer layer across multiple GPUs. However, this strategy requires a fast network due to the communication needed between the GPUs, making it less suitable for running workloads across nodes.

  * **Pipeline parallelism** splits the model by layer, or vertically. This strategy does not require constant communication between GPUs, making it a better option when running models across nodes.




You can use both strategies in multi-node serving. For example, when using two nodes with eight H100 GPUs each, you can use both strategies:

  * Two-way pipeline parallelism to shard the model across the two nodes

  * Eight-way tensor parallelism to shard the model across the eight GPUs on each node




To learn more, refer to the [vLLM documentation](https://docs.vllm.ai/en/latest/).

## Objectives

  1. Prepare your environment with a Google Distributed Cloud cluster in Autopilot or Standard mode.

  2. Deploy vLLM across multiple nodes in your cluster.

  3. Use vLLM to serve the model through `curl`.




## Before you begin

  * Ensure you have a working [bare metal cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview) with at least one worker node pool that has two worker nodes, [each configured with eight NVIDIA H100 80 GB GPUs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/gpu-manual-use). 


  * Create a [Hugging Face](https://huggingface.co/) account, if you don't already have one.



## Get access to the model

You can use the Llama 3.1 405B or DeepSeek-R1 models.

### DeepSeek-R1

**Note:** You must sign the consent agreement to use DeepSeek-R1 in the [Hugging Face repository](https://huggingface.co/deepseek-ai/DeepSeek-R1)

### Generate an access token

If you don't already have one, generate a new [Hugging Face token](https://huggingface.co/docs/hub/security-tokens):

  1. Click **Your Profile > Settings > Access Tokens**.

  2. Select **New Token**.

  3. Specify a Name of your choice and a Role of at least `Read`.

  4. Select **Generate a token**.




### Llama 3.1 405B

**Note:** You must sign the consent agreement to use Llama 3.1 405B in the [Hugging Face repository](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct)

### Generate an access token

If you don't already have one, generate a new [Hugging Face token](https://huggingface.co/docs/hub/security-tokens):

  1. Click **Your Profile > Settings > Access Tokens**.

  2. Select **New Token**.

  3. Specify a Name of your choice and a Role of at least `Read`.

  4. Select **Generate a token**.




## Prepare the environment

To set up your environment, follow these steps:

  1. Set following parameters on the admin workstation:
         
         gcloud config set project PROJECT_ID
         export PROJECT_ID=$(gcloud config get project)
         export HF_TOKEN=HUGGING_FACE_TOKEN
         export IMAGE_NAME= gcr.io/PROJECT_ID/vllm-multihost/vllm-multihost:latest
         

Replace the following values:

     * `PROJECT_ID`: the project ID associated with your cluster.

     * `HUGGING_FACE_TOKEN`: the hugging face token generated from the preceding Get access to the model section.




## Create a Kubernetes Secret for Hugging Face credentials

Create a Kubernetes Secret that contains the Hugging Face token using the following command:
    
    
    kubectl create secret generic hf-secret \
        --kubeconfig KUBECONFIG \
        --from-literal=hf_api_token=${HF_TOKEN} \
        --dry-run=client -o yaml | kubectl apply -f -
    

Replace `KUBECONFIG` with the path of the kubeconfig file for the cluster on which you intend to host the LLM.

## Install LeaderWorkerSet

To install LWS, run the following command:
    
    
    kubectl apply --server-side \
        --kubeconfig KUBECONFIG \
        -f https://github.com/kubernetes-sigs/lws/releases/latest/download/manifests.yaml
    

Validate that the LeaderWorkerSet controller is running in the `lws-system` namespace, using the following command:
    
    
    kubectl get pod -n lws-system --kubeconfig KUBECONFIG
    

The output is similar to the following:
    
    
    NAME                                      READY   STATUS    RESTARTS   AGE
    lws-controller-manager-5c4ff67cbd-9jsfc   2/2     Running   0          6d23h
    

## Deploy vLLM Model Server

To deploy the vLLM model server, follow these steps:

  1. Create and apply the manifest, depending on LLM you want to deploy.

### DeepSeek-R1

     1. Create a YAML manifest, `vllm-deepseek-r1-A3.yaml`, for the vLLM model server:
            
            apiVersion: leaderworkerset.x-k8s.io/v1
            kind: LeaderWorkerSet
            metadata:
              name: vllm
            spec:
              replicas: 1
              leaderWorkerTemplate:
                size: 2
                restartPolicy: RecreateGroupOnPodRestart
                leaderTemplate:
                  metadata:
                    labels:
                      role: leader
                  spec:
                    nodeSelector:
                      cloud.google.com/gke-accelerator: nvidia-h100-80gb
                    containers:
                      - name: vllm-leader
                        image: vllm/vllm-openai:v0.8.5
                        env:
                          - name: HUGGING_FACE_HUB_TOKEN
                            valueFrom:
                              secretKeyRef:
                                name: hf-secret
                                key: hf_api_token
                        command:
                          - sh
                          - -c
                          - "bash /vllm-workspace/examples/online_serving/multi-node-serving.sh leader --ray_cluster_size=$(LWS_GROUP_SIZE);
                            python3 -m vllm.entrypoints.openai.api_server --port 8080 --model deepseek-ai/DeepSeek-R1 --tensor-parallel-size 8 --pipeline-parallel-size 2 --trust-remote-code --max-model-len 4096"
                        resources:
                          limits:
                            nvidia.com/gpu: "8"
                        ports:
                          - containerPort: 8080
                        readinessProbe:
                          tcpSocket:
                            port: 8080
                          initialDelaySeconds: 15
                          periodSeconds: 10
                        volumeMounts:
                          - mountPath: /dev/shm
                            name: dshm
                    volumes:
                    - name: dshm
                      emptyDir:
                        medium: Memory
                        sizeLimit: 15Gi
                workerTemplate:
                  spec:
                    containers:
                      - name: vllm-worker
                        image: vllm/vllm-openai:v0.8.5
                        command:
                          - sh
                          - -c
                          - "bash /vllm-workspace/examples/online_serving/multi-node-serving.sh worker --ray_address=$(LWS_LEADER_ADDRESS)"
                        resources:
                          limits:
                            nvidia.com/gpu: "8"
                        env:
                          - name: HUGGING_FACE_HUB_TOKEN
                            valueFrom:
                              secretKeyRef:
                                name: hf-secret
                                key: hf_api_token
                        volumeMounts:
                          - mountPath: /dev/shm
                            name: dshm
                    volumes:
                    - name: dshm
                      emptyDir:
                        medium: Memory
                        sizeLimit: 15Gi
            ---
            apiVersion: v1
            kind: Service
            metadata:
              name: vllm-leader
            spec:
              ports:
                - name: http
                  port: 8080
                  protocol: TCP
                  targetPort: 8080
              selector:
                leaderworkerset.sigs.k8s.io/name: vllm
                role: leader
              type: ClusterIP
            

     2. Apply the manifest by running the following command:
            
            kubectl apply -f vllm-deepseek-r1-A3.yaml \
                --kubeconfig KUBECONFIG
            

### Llama 3.1 405B

     1. Create a YAML manifest, `vllm-llama3-405b-A3.yaml`, for the vLLM model server:
            
            apiVersion: leaderworkerset.x-k8s.io/v1
            kind: LeaderWorkerSet
            metadata:
              name: vllm
            spec:
              replicas: 1
              leaderWorkerTemplate:
                size: 2
                restartPolicy: RecreateGroupOnPodRestart
                leaderTemplate:
                  metadata:
                    labels:
                      role: leader
                  spec:
                    nodeSelector:
                      cloud.google.com/gke-accelerator: nvidia-h100-80gb
                    containers:
                      - name: vllm-leader
                        image: vllm/vllm-openai:v0.8.5
                        env:
                          - name: HUGGING_FACE_HUB_TOKEN
                            valueFrom:
                              secretKeyRef:
                                name: hf-secret
                                key: hf_api_token
                        command:
                          - sh
                          - -c
                          - "bash /vllm-workspace/examples/online_serving/multi-node-serving.sh leader --ray_cluster_size=$(LWS_GROUP_SIZE);
                            python3 -m vllm.entrypoints.openai.api_server --port 8080 --model meta-llama/Meta-Llama-3.1-405B-Instruct --tensor-parallel-size 8 --pipeline-parallel-size 2"
                        resources:
                          limits:
                            nvidia.com/gpu: "8"
                        ports:
                          - containerPort: 8080
                        readinessProbe:
                          tcpSocket:
                            port: 8080
                          initialDelaySeconds: 15
                          periodSeconds: 10
                        volumeMounts:
                          - mountPath: /dev/shm
                            name: dshm
                    volumes:
                    - name: dshm
                      emptyDir:
                        medium: Memory
                        sizeLimit: 15Gi
                workerTemplate:
                  spec:
                    containers:
                      - name: vllm-worker
                        image: vllm/vllm-openai:v0.8.5
                        command:
                          - sh
                          - -c
                          - "bash /vllm-workspace/examples/online_serving/multi-node-serving.sh worker --ray_address=$(LWS_LEADER_ADDRESS)"
                        resources:
                          limits:
                            nvidia.com/gpu: "8"
                        env:
                          - name: HUGGING_FACE_HUB_TOKEN
                            valueFrom:
                              secretKeyRef:
                                name: hf-secret
                                key: hf_api_token
                        volumeMounts:
                          - mountPath: /dev/shm
                            name: dshm
                    volumes:
                    - name: dshm
                      emptyDir:
                        medium: Memory
                        sizeLimit: 15Gi
            ---
            apiVersion: v1
            kind: Service
            metadata:
              name: vllm-leader
            spec:
              ports:
                - name: http
                  port: 8080
                  protocol: TCP
                  targetPort: 8080
              selector:
                leaderworkerset.sigs.k8s.io/name: vllm
                role: leader
              type: ClusterIP
            

     2. Apply the manifest by running the following command:
            
            kubectl apply -f vllm-llama3-405b-A3.yaml \
                --kubeconfig KUBECONFIG
            

  2. View the logs from the running model server with the following command:
         
         kubectl logs vllm-0 -c vllm-leader \
             --kubeconfig KUBECONFIG
         

The output should look similar to the following:
         
         INFO 08-09 21:01:34 api_server.py:297] Route: /detokenize, Methods: POST
         INFO 08-09 21:01:34 api_server.py:297] Route: /v1/models, Methods: GET
         INFO 08-09 21:01:34 api_server.py:297] Route: /version, Methods: GET
         INFO 08-09 21:01:34 api_server.py:297] Route: /v1/chat/completions, Methods: POST
         INFO 08-09 21:01:34 api_server.py:297] Route: /v1/completions, Methods: POST
         INFO 08-09 21:01:34 api_server.py:297] Route: /v1/embeddings, Methods: POST
         INFO:     Started server process [7428]
         INFO:     Waiting for application startup.
         INFO:     Application startup complete.
         INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
         




## Serve the model

Set up port forwarding to the model by running the following command:
    
    
    kubectl port-forward svc/vllm-leader 8080:8080 \
        --kubeconfig KUBECONFIG
    

### Interact with the model using curl

To interact with the model using curl, follow these instructions:

### DeepSeek-R1

In a new terminal, send a request to the server:
    
    
    curl http://localhost:8080/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "deepseek-ai/DeepSeek-R1",
        "prompt": "I have four boxes. I put the red box on the bottom and put the blue box on top. Then I put the yellow box on top the blue. Then I take the blue box out and put it on top. And finally I put the green box on the top. Give me the final order of the boxes from bottom to top. Show your reasoning but be brief",
        "max_tokens": 1024,
        "temperature": 0
    }'
    

The output should be similar to the following:
    
    
    {
      "id": "cmpl-f2222b5589d947419f59f6e9fe24c5bd",
      "object": "text_completion",
      "created": 1738269669,
      "model": "deepseek-ai/DeepSeek-R1",
      "choices": [
        {
          "index": 0,
          "text": ".\n\nOkay, let's see. The user has four boxes and is moving them around. Let me try to visualize each step. \n\nFirst, the red box is placed on the bottom. So the stack starts with red. Then the blue box is put on top of red. Now the order is red (bottom), blue. Next, the yellow box is added on top of blue. So now it's red, blue, yellow. \n\nThen the user takes the blue box out. Wait, blue is in the middle. If they remove blue, the stack would be red and yellow. But where do they put the blue box? The instruction says to put it on top. So after removing blue, the stack is red, yellow. Then blue is placed on top, making it red, yellow, blue. \n\nFinally, the green box is added on the top. So the final order should be red (bottom), yellow, blue, green. Let me double-check each step to make sure I didn't mix up any steps. Starting with red, then blue, then yellow. Remove blue from the middle, so yellow is now on top of red. Then place blue on top of that, so red, yellow, blue. Then green on top. Yes, that seems right. The key step is removing the blue box from the middle, which leaves yellow on red, then blue goes back on top, followed by green. So the final order from bottom to top is red, yellow, blue, green.\n\n**Final Answer**\nThe final order from bottom to top is \\boxed{red}, \\boxed{yellow}, \\boxed{blue}, \\boxed{green}.\n</think>\n\n1. Start with the red box at the bottom.\n2. Place the blue box on top of the red box. Order: red (bottom), blue.\n3. Place the yellow box on top of the blue box. Order: red, blue, yellow.\n4. Remove the blue box (from the middle) and place it on top. Order: red, yellow, blue.\n5. Place the green box on top. Final order: red, yellow, blue, green.\n\n\\boxed{red}, \\boxed{yellow}, \\boxed{blue}, \\boxed{green}",
          "logprobs": null,
          "finish_reason": "stop",
          "stop_reason": null,
          "prompt_logprobs": null
        }
      ],
      "usage": {
        "prompt_tokens": 76,
        "total_tokens": 544,
        "completion_tokens": 468,
        "prompt_tokens_details": null
      }
    }
    

### Llama 3.1 405B

In a new terminal, send a request to the server:
    
    
    curl http://localhost:8080/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "meta-llama/Meta-Llama-3.1-405B-Instruct",
        "prompt": "San Francisco is a",
        "max_tokens": 7,
        "temperature": 0
    }'
    

The output should be similar to the following:
    
    
    {"id":"cmpl-0a2310f30ac3454aa7f2c5bb6a292e6c",
    "object":"text_completion","created":1723238375,"model":"meta-llama/Meta-Llama-3.1-405B-Instruct","choices":[{"index":0,"text":" top destination for foodies, with","logprobs":null,"finish_reason":"length","stop_reason":null}],"usage":{"prompt_tokens":5,"total_tokens":12,"completion_tokens":7}}
    

## What's next

  * Learn more about [GPUs in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus).
  * Explore the vLLM [GitHub repository](https://github.com/vllm-project/vllm) and [documentation](https://docs.vllm.ai/en/latest/).
  * Explore the LWS [GitHub repository](https://github.com/kubernetes-sigs/lws)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
