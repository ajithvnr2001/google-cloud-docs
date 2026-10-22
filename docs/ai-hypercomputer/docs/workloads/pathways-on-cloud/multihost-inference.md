---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference/
title: Perform multihost inference using Pathways \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:11.199915+00:00
---

# Perform multihost inference using Pathways  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Perform multihost inference using Pathways Stay organized with collections  Save and categorize content based on your preferences. 

Multihost inference is a method of running model inference that distributes the model across multiple accelerators hosts. This enables the inference of large models that don't fit on a single host. Pathways can be deployed for both batch and real time multihost inference use cases. 

## Before you begin

Make sure you have:

  * [Created a GKE cluster that uses Trillium chips (v6e-16)](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster).
  * [Installed Kubernetes tools](https://kubernetes.io/docs/tasks/tools/)
  * [Enabled the Google Kubernetes Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api)



## Run Batch inference using JetStream

[JetStream](https://github.com/AI-Hypercomputer/JetStream) is a throughput and memory-optimized engine for large language model (LLM) inference on XLA devices, primarily Tensor Processing Units (TPUs) written in JAX.

You can use a prebuilt JetStream Docker image to run a batch inference workload, as shown in the following YAML. This container is built from the [OSS JetStream project](https://github.com/AI-Hypercomputer/JetStream/tree/main). For more information about MaxText-JetStream flags, see [JetStream MaxText server flags](https://github.com/AI-Hypercomputer/JetStream/blob/main/docs/). The following example uses Trillium chips (`v6e-16`) to load the Llama3.1-405b int8 checkpoint and perform inference over it. This example assumes you already have a GKE cluster with at least one `v6e-16` nodepool inside it.

### Start model server and Pathways

  1. Get credentials to the cluster and add them to your local kubectl context. 
         
         gcloud container clusters get-credentials $CLUSTER \
               --zone=$ZONE \
               --project=$PROJECT \
               && kubectl config set-context --current --namespace=default
             

  2. Deploy LeaderWorkerSet (LWS) API. 
         
         VERSION=v0.4.0
               kubectl apply --server-side -f "https://github.com/kubernetes-sigs/lws/releases/download/${VERSION}/manifests.yaml"
             

  3. Copy and paste the following YAML into a file named `pathways-job.yaml`: This YAML has been optimized for the `v6e-16` slice shape. For more information on how to convert a Meta checkpoint into a JAX compatible checkpoint, follow the checkpoint creation guide in [Creating inference checkpoints](https://gke-ai-labs.dev/docs/tutorials/inference-servers/checkpoints/). As an example, instructions for Llama3.1-405B are provided here [Checkpoint conversion for Llama3.1-405B](https://github.com/ai-on-gke/tutorials-and-examples/tree/main/inference-servers/checkpoints/examples/llama3.1-405b). 
         
         apiVersion: leaderworkerset.x-k8s.io/v1
             kind: LeaderWorkerSet
             metadata:
               name: jetstream-pathways
               annotations:
                 leaderworkerset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
             spec:
               replicas: 1
               leaderWorkerTemplate:
                 leaderTemplate:
                   metadata:
                     labels:
                       app: jetstream-pathways
                   spec:
                     nodeSelector:
                       cloud.google.com/gke-tpu-accelerator: TPU_ACCELERATOR_TYPE # Example: tpu-v6e-slice
                       cloud.google.com/gke-tpu-topology: TPU_TOPOLOGY # Example: 4x4
                     tolerations:
                     - key: "google.com/tpu"
                       operator: "Exists"
                       effect: "NoSchedule"
                     containers:
                     - name: pathways-proxy
                       image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/proxy_server:latest
                       args:
                       - --resource_manager_address=$(LWS_LEADER_ADDRESS):38677
                       - --server_port=38681
                       - --gcs_scratch_location=gs://cloud-pathways-staging/tmp
                       imagePullPolicy: Always
                       ports:
                       - containerPort: 38681
                     - name: pathways-rm
                       env:
                       - name: HOST_ADDRESS
                         value: "$(LWS_LEADER_ADDRESS)"
                       - name: TPU_SKIP_MDS_QUERY
                         value: "true"
                       image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/server:latest
                       args:
                       - --server_port=38677
                       - --gcs_scratch_location=gs://cloud-pathways-staging/tmp
                       - --node_type=resource_manager
                       - --instance_count=1
                       - --instance_type=tpuv6e:TPU_TOPOLOGY # Example: 4x4
                       - --temporary_flags_for_debugging=temporary_flag_for_debugging_worker_expected_tpu_chip_config=megachip_tccontrol
                       imagePullPolicy: Always
                       ports:
                       - containerPort: 38677
                     - name: jax-tpu
                       image: us-docker.pkg.dev/cloud-tpu-images/inference/jetstream-pathways:jax-0.8.0
                       # Optimized settings used to serve Llama3.1-405b.
                       args:
                       - MaxText/configs/v5e/inference/llama3_405b_v5e-64.yml
                       - model_name=llama3.1-405b
                       - load_parameters_path=CHECKPOINT_PATH
                       - max_prefill_predict_length=1024
                       - max_target_length=2048
                       - async_checkpointing=false
                       - steps=1
                       - ici_fsdp_parallelism=1
                       - ici_autoregressive_parallelism=2
                       - ici_tensor_parallelism=8
                       - scan_layers=false
                       - weight_dtype=bfloat16
                       - per_device_batch_size=10
                       - enable_single_controller=true
                       - quantization=int8
                       - quantize_kvcache=true
                       - checkpoint_is_quantized=true
                       - enable_model_warmup=true
                       imagePullPolicy: Always
                       ports:
                       - containerPort: 9000
                       startupProbe:
                         httpGet:
                           path: /healthcheck
                           port: 8000
                           scheme: HTTP
                         periodSeconds: 1
                         initialDelaySeconds: 900
                         failureThreshold: 10000
                       livenessProbe:
                         httpGet:
                           path: /healthcheck
                           port: 8000
                           scheme: HTTP
                         periodSeconds: 60
                         failureThreshold: 10
                       readinessProbe:
                         httpGet:
                           path: /healthcheck
                           port: 8000
                           scheme: HTTP
                         periodSeconds: 60
                         failureThreshold: 10
                     - name: jetstream-http
                       image: us-docker.pkg.dev/cloud-tpu-images/inference/jetstream-http:v0.2.4
                       imagePullPolicy: Always
                       ports:
                       - containerPort: 8000
                 # The size variable defines the number of worker nodes to be created.
                 # It must be equal to the number of hosts + 1 (for the leader node).
                 size: 5
                 workerTemplate:
                   spec:
                     nodeSelector:
                       cloud.google.com/gke-tpu-accelerator: TPU_ACCELERATOR_TYPE # Example: tpu-v6e-slice
                       cloud.google.com/gke-tpu-topology: TPU_TOPOLOGY # Example: 4x4
                     tolerations:
                     - key: "google.com/tpu"
                       operator: "Exists"
                       effect: "NoSchedule"
                     containers:
                     - name: worker
                       args:
                       - --server_port=38679
                       - --resource_manager_address=$(LWS_LEADER_ADDRESS):38677
                       - --gcs_scratch_location=gs://cloud-pathways-staging/tmp
                       image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/server:latest
                       imagePullPolicy: Always
                       ports:
                       - containerPort: 38679
                       resources:
                         limits:
                           google.com/tpu: "4"
             ---
             apiVersion: v1
             kind: Service
             metadata:
               name: jetstream-svc
             spec:
               selector:
                 app: jetstream-pathways
               ports:
               - protocol: TCP
                 name: jetstream-http
                 port: 8000
                 targetPort: 8000
             

Replace the following: 
     * `TPU_ACCELERATOR_TYPE`: The TPU accelerator type. For example, `tpu-v6e-slice`.
     * `TPU_TOPOLOGY`: The TPU topology. For example, `2x4`.
     * `CHECKPOINT_PATH`: The Cloud Storage path to the checkpoint.
Apply this YAML. Wait for the LeaderWorkerSet to be scheduled. Once the set is scheduled, the model server may take some time to restore the checkpoint. For the 405B model, this takes ~7 minutes. 
  4. Look at the Kubernetes logs to see if the JetStream model server is ready: The workload was named `jetstream-pathways` in the previous YAML, and `0` is the head node. 
         
         kubectl logs -f jetstream-pathways-0 -c jax-tpu
               

The output is similar to the following which indicates the JetStream model server is ready to serve requests: 
         
         2025-03-02 02:15:07,682 - JetstreamLogger - INFO - Initializing the driver with 1 prefill engines and 1 generate engines in interleaved mode
             2025-03-02 02:15:07,683 - JetstreamLogger - INFO - Spinning up prefill thread 0.
             2025-03-02 02:15:07,683 - JetstreamLogger - INFO - Spinning up transfer thread 0.
             2025-03-02 02:15:07,684 - JetstreamLogger - INFO - Spinning up generate thread 0.
             2025-03-02 02:15:07,684 - JetstreamLogger - INFO - Spinning up detokenize thread 0.
             2025-03-02 02:15:07,685 - JetstreamLogger - INFO - Driver initialized.
             ...
             ...
             ...
             INFO:     Started server process [7]
             INFO:     Waiting for application startup.
             INFO:     Application startup complete.
             INFO:     Uvicorn running on http://0.0.0.0:9999 (Press CTRL+C to quit)
             




### Connect to the model server

You can access the JetStream Pathways deployment using GKE's ClusterIP service. The ClusterIP service is only reachable from within the cluster. Therefore, to access the service from outside the cluster, you must first establish a port-forwarding session by running the following command:
    
    
    kubectl port-forward pod/${HEAD_POD} 8000:8000

Verify that you can access the JetStream HTTP server by opening a new terminal and running the following command:
    
    
    curl --request POST \
    --header "Content-type: application/json" \
    -s \
    localhost:8000/generate \
    --data \
    '{
        "prompt": "What are the top 5 programming languages",
        "max_tokens": 200
    }'
    

The initial request can take several seconds to complete due to model warmup. The output should be similar to the following:
    
    
    {
        "response": " for web development?\nThe top 5 programming languages for web development are:\n1. **JavaScript**: JavaScript is the most popular language for web development, used by over 90% of websites for client-side scripting. It's also popular for server-side programming with technologies like Node.js.\n2. **HTML/CSS**: HTML (Hypertext Markup Language) and CSS (Cascading Style Sheets) are not programming languages, but are essential for building websites. HTML is used for structuring content, while CSS is used for styling and layout.\n3. **Python**: Python is a popular language for web development, especially with frameworks like Django and Flask. It's known for its simplicity, flexibility, and large community of developers.\n4. **Java**: Java is a popular language for building enterprise-level web applications, especially with frameworks like Spring and Hibernate. It's known for its platform independence, strong security features, and large community of developers.\n5. **PHP**: PHP is a mature language for web"
    }
    

### Disaggregated inference

[Disaggregated serving](https://arxiv.org/html/2401.11181v1) is a technique for running large language models (LLMs) that separates the _prefill_ and _decode_ stages into different processes, potentially on different machines. This allows for better utilization of resources and can lead to improvements in performance and efficiency, especially for large models.

  * **Prefill** : this stage processes the input prompt and generates an intermediate representation (like a key-value cache). It's often compute intensive.
  * **Decode** : this stage generates the output tokens, one by one, using the prefill representation. It is typically memory-bandwidth bound.



By separating these stages, disaggregated serving allows for prefill and decode to run in parallel, improving throughput and latency.

To enable disaggregated serving, modify the following YAML to utilize two `v6e-8` slices: one for prefill and the other for generate. Before proceeding, ensure your GKE cluster has at least two node pools configured with this `v6e-8` topology. For optimal performance, specific XLA flags have been configured.

Create a llama2-70b checkpoint following the same process as llama3.1-405b checkpoint creation, detailed in the previous section.

  1. To launch the JetStream server in disaggregated mode using Pathways, copy and paste the following YAML into a file named `pathways-job.yaml`: 
         
         apiVersion: leaderworkerset.x-k8s.io/v1
         kind: LeaderWorkerSet
         metadata:
           name: jetstream-pathways
           annotations:
             leaderworkerset.sigs.k8s.io/subgroup-exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           replicas: 1
           leaderWorkerTemplate:
             subGroupPolicy:
               subGroupSize: 2
             leaderTemplate:
               metadata:
                 labels:
                   app: jetstream-pathways
               spec:
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: TPU_ACCELERATOR_TYPE # Example: tpu-v6e-slice
                   cloud.google.com/gke-tpu-topology: TPU_TOPOLOGY # Example: 2x4
                 tolerations:
                 - key: "google.com/tpu"
                   operator: "Exists"
                   effect: "NoSchedule"
                 containers:
                 - name: pathways-proxy
                   image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/proxy_server:latest
                   args:
                   - --resource_manager_address=$(LWS_LEADER_ADDRESS):38677
                   - --server_port=38681
                   - --gcs_scratch_location=gs://cloud-pathways-staging/tmp
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 38681
                 - name: pathways-rm
                   env:
                   - name: HOST_ADDRESS
                     value: "$(LWS_LEADER_ADDRESS)"
                   - name: TPU_SKIP_MDS_QUERY
                     value: "true"
                   image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/server:latest
                   args:
                   - --server_port=38677
                   - --gcs_scratch_location=gs://cloud-pathways-staging/tmp
                   - --node_type=resource_manager
                   - --instance_count=2
                   - --instance_type=tpuv6e:TPU_TOPOLOGY # Example: 2x4
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 38677
                 - name: jax-tpu
                   image: us-docker.pkg.dev/cloud-tpu-images/inference/jetstream-pathways:jax-0.8.0
                   # Optimized settings used to serve Llama2-70b.
                   args:
                   - MaxText/configs/base.yml
                   - tokenizer_path=assets/tokenizer.llama2
                   - load_parameters_path=CHECKPOINT_PATH
                   - max_prefill_predict_length=1024
                   - max_target_length=2048
                   - model_name=llama2-70b
                   - ici_fsdp_parallelism=1
                   - ici_autoregressive_parallelism=1
                   - ici_tensor_parallelism=-1
                   - scan_layers=false
                   - weight_dtype=bfloat16
                   - per_device_batch_size=1
                   - checkpoint_is_quantized=true
                   - quantization=int8
                   - quantize_kvcache=true
                   - compute_axis_order=0,2,1,3
                   - ar_cache_axis_order=0,2,1,3
                   - stack_prefill_result_cache=True
                   # Specify disaggregated mode to run Jetstream
                   - inference_server=ExperimentalMaxtextDisaggregatedServer_8
                   - inference_benchmark_test=True
                   - enable_model_warmup=True
                   env:
                   - name: LOG_LEVEL
                     value: "INFO"
                   imagePullPolicy: Always
                   securityContext:
                     capabilities:
                       add: ["SYS_PTRACE", "NET_ADMIN", "SYS_TIME"]
                   ports:
                   - containerPort: 9000
                   startupProbe:
                     httpGet:
                       path: /healthcheck
                       port: 8000
                       scheme: HTTP
                     periodSeconds: 1
                     initialDelaySeconds: 240
                     failureThreshold: 10000
                   livenessProbe:
                     httpGet:
                       path: /healthcheck
                       port: 8000
                       scheme: HTTP
                     periodSeconds: 60
                     failureThreshold: 100
                   readinessProbe:
                     httpGet:
                       path: /healthcheck
                       port: 8000
                       scheme: HTTP
                     periodSeconds: 60
                     failureThreshold: 100
                 - name: jetstream-http
                   image: us-docker.pkg.dev/cloud-tpu-images/inference/jetstream-http:v0.2.4
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 8000
             # The size variable defines the number of worker nodes to be created.
             # It must be equal to the number of hosts + 1 (for the leader node).
             size: 5
             workerTemplate:
               spec:
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: TPU_ACCELERATOR_TYPE # Example: tpu-v6e-slice
                   cloud.google.com/gke-tpu-topology: TPU_TOPOLOGY # Example: 2x4
                 containers:
                 - name: worker
                   args:
                   - --server_port=38679
                   - --resource_manager_address=$(LWS_LEADER_ADDRESS):38677
                   - --gcs_scratch_location=gs://cloud-pathways-staging/tmp
                   image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/server:latest
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 38679
                   resources:
                     limits:
                       google.com/tpu: "4"
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: jetstream-svc
         spec:
           selector:
             app: jetstream-pathways
           ports:
           - protocol: TCP
             name: jetstream-http
             port: 8000
             targetPort: 8000
           

Replace the following: 
     * `TPU_ACCELERATOR_TYPE`: The TPU accelerator type. For example, `tpu-v6e-slice`.
     * `TPU_TOPOLOGY`: The TPU topology. For example, `2x4`.
     * `CHECKPOINT_PATH`: The Cloud Storage path to the checkpoint.
  2. Apply this YAML, the model server will take some time to restore the checkpoint. For the 70B model, this may take ~2 minutes. 
         
         kubectl apply -f pathways-job.yaml
               

  3. Look at the Kubernetes logs to see if the JetStream model server is ready: 
         
         kubectl logs -f jetstream-pathways-0 -c jax-tpu
             

You will see output similar to the following which indicates the JetStream model server is ready to serve requests: 
         
         2025-03-02 02:15:07,682 - JetstreamLogger - INFO - Initializing the driver with 1 prefill engines and 1 generate engines in interleaved mode
             2025-03-02 02:15:07,683 - JetstreamLogger - INFO - Spinning up prefill thread 0.
             2025-03-02 02:15:07,683 - JetstreamLogger - INFO - Spinning up transfer thread 0.
             2025-03-02 02:15:07,684 - JetstreamLogger - INFO - Spinning up generate thread 0.
             2025-03-02 02:15:07,684 - JetstreamLogger - INFO - Spinning up detokenize thread 0.
             2025-03-02 02:15:07,685 - JetstreamLogger - INFO - Driver initialized.
             ...
             ...
             ...
             INFO:     Started server process [7]
             INFO:     Waiting for application startup.
             INFO:     Application startup complete.
             INFO:     Uvicorn running on http://0.0.0.0:9999 (Press CTRL+C to quit)
           




### Connect to the model server

You can access the JetStream Pathways deployment through the GKE's ClusterIP service. The ClusterIP service is only reachable from within the cluster. Therefore, to access the service from outside the cluster, establish a port-forwarding session by running the following command:
    
    
    kubectl port-forward pod/${HEAD_POD} 8000:8000

Verify that you can access the JetStream HTTP server by opening a new terminal and running the following command:
    
    
    curl --request POST \
    --header "Content-type: application/json" \
    -s \
    localhost:8000/generate \
    --data \
    '{
        "prompt": "What are the top 5 programming languages",
        "max_tokens": 200
    }'
    

The initial request can take several seconds to complete due to model warmup. The output should be similar to the following:
    
    
    {
        "response": " used in software development?\nThe top 5 programming languages used in software development are:\n\n1. Java: Java is a popular programming language used for developing enterprise-level applications, Android apps, and web applications. Its platform independence and ability to run on any device that has a Java Virtual Machine (JVM) installed make it a favorite among developers.\n2. Python: Python is a versatile language that is widely used in software development, data analysis, artificial intelligence, and machine learning. Its simplicity, readability, and ease of use make it a popular choice among developers.\n3. JavaScript: JavaScript is a widely used programming language for web development, allowing developers to create interactive client-side functionality for web applications. It is also used for server-side programming, desktop and mobile application development, and game development.\n4. C++: C++ is a high-performance programming language used for developing operating systems, games, and other high-performance applications."
    }
    

## What's next

  * [Batch workloads with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
  * [Pathways interactive mode](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
  * [Porting JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
  * [Troubleshooting Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
