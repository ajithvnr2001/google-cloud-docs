---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads/
title: Port JAX workloads to Pathways \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:12.869077+00:00
---

# Port JAX workloads to Pathways  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Port JAX workloads to Pathways Stay organized with collections  Save and categorize content based on your preferences. 

Due to the distributed nature of JAX with Pathways, some operations might not scale well due to communication overheads. While Pathways minimizes these overheads with features like [asynchronous dispatch](https://jax.readthedocs.io/en/latest/async_dispatch.html), there are some things you need to be aware of when you port JAX workloads to Pathways or scale a JAX with Pathways workload to a large number of accelerators.

## Before you begin

Make sure you have:

  * [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment)
  * [Installed Kubernetes tools](https://kubernetes.io/docs/tasks/tools/)
  * [Installed the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install)
  * [Enabled the Google Kubernetes Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api)



## Process index

JAX with Pathways treats all devices across your Pathways cluster as local. This simplifies device management and allows JAX to utilize all available resources. In practice, this means:

  * `jax.process_index()` is always 0 for all devices.
  * `jax.devices()` and `jax.local_devices()` return all TPU devices across the entire job.



## Hardware type and colocation

For best performance, place all Pathways components and the user job in the same Google Cloud cloud zone. Use a large CPU like the IFRT proxy and resource manager. We recommend at least a dedicated `n2-standard-64` which comes with 64 vCPUs and 256 GB memory.

## PathwaysUtils

[Pathways-utils](https://github.com/AI-Hypercomputer/pathways-utils) is a Python-based GitHub repository providing essential utilities and tools that let you streamline the deployment and execution of JAX workloads on the Pathways on Cloud architecture. This package handles the necessary adaptations for the cloud environment, allowing JAX developers to focus on their core machine learning workflows with minimal platform-specific configuration. Specifically, it offers:

  * A "proxy" JAX backend: this custom backend enables your JAX application to use the Pathways infrastructure by setting the `JAX_PLATFORMS=proxy` environment variable.
  * Integrated Profiling Utilities: profiling capabilities that let you understand your application's performance. By using standard JAX profiling APIs like `jax.profiler.start_trace` and `jax.profiler.start_server`, you can profile not only your JAX code but also the underlying Pathways components, providing a holistic view of execution within the cloud environment.
  * Distributed Checkpointing with Orbax: a custom Orbax checkpoint handler that lets you use distributed checkpoints and restore your checkpoints when using the Orbax library within the Pathways environment. This integration aims to work without requiring any changes to your existing Orbax checkpointing code as long as it imports `pathwaysutils`.
  * Elastic Training Primitives: provides foundational elastic training primitives that you can use to build robust and scalable training workflows using Pathways. These primitives allow your training jobs to dynamically adapt to changes in available resources, improving efficiency and resilience in cloud environments.



## Checkpointing

[Orbax](https://github.com/google/orbax) is thoroughly tested with Pathways for distributed checkpointing and restoring with Cloud Storage. When you set the environment variable `ENABLE_PATHWAYS_PERSISTENCE=1` and call `import pathwaysutils; pathwaysutils.initialize()` in your `train.py`, a custom `ArrayHandler` is registered that efficiently handles checkpoint operations through the [IFRT](https://github.com/openxla/xla/blob/main/xla/python/ifrt/README.md) proxy, allowing Pathways workers on accelerators to directly save and restore data.

## Colocated Python

[Colocated Python](https://github.com/jax-ml/jax/blob/main/jax/experimental/colocated_python/api.py) is an open-source JAX API that lets you run user-specified Python code directly on the TPU or GPU hosts, which is more straightforward in multi-controller JAX. This enables more compute-intensive tasks, such as data loading and checkpointing, to avoid data transfer between the client and TPU machines. To configure your Pathways cluster to run colocated python JAX API, follow the instructions in the [colocated Python README](https://github.com/AI-Hypercomputer/pathways-utils/blob/main/pathwaysutils/sidecar/README.md). These instructions explain how to start a colocated Python sidecar alongside your Pathways workers.

## Data loading

During training we repeatedly load batches from a dataset to feed it into the model. Having an efficient, async data loader which shards the batch across hosts is important to avoid starving accelerators of work. When running training with Pathways, the data loader runs on a CPU VM (unlike a TPU VM which is used on multi-controller setups) and dispatches data to TPU VMs. This incurs a higher latency in reading data but that is mitigated partially by reading ahead X number of batches on the CPU host and dispatching the read data asynchronously to the TPUs. This solution is sufficient when running at small to medium scale.

For optimal performance at scale, we strongly recommend co-locating your input data pipeline by using colocated Python to run your data pipeline directly on the accelerators. This eliminates the CPU bottleneck and leverages the TPU's fast interconnects for data transfer.

You can find a reference implementation of migrating a TFDS based input pipeline in the `RemoteIterator` implementation in [multihost_dataloading.py](https://github.com/AI-Hypercomputer/maxtext/blob/main/MaxText/multihost_dataloading.py). This implementation works on both multi-controller JAX and Pathways in a distributed manner using the colocated Python JAX API.

## Jax Versioning

Pathways releases are tightly coupled with JAX versions to ensure compatibility and stability. To avoid potential issues, verify that your Pathways artifacts and your JAX version are aligned. Each Pathways release clearly specifies the compatible JAX versions through a tag of the form `jax-<version>`.

## Compilation Cache

Pathways persistent compilation cache is a feature that allows Pathways servers to store compiled XLA executables in a persistent location, such as Cloud Storage, to avoid redundant compilation. This feature is enabled by default. The location of the cache is passed in as `--gcs_scratch_location` flag to the resource manager and Pathways worker containers. To keep associated storage costs to a minimum, the cache attaches a lifecycle policy to the Cloud Storage location. There is a limit of 50 policies per Cloud Storage bucket. Therefore, we recommend using a common Cloud Storage location across all workloads.

If you omit the `--gcs_scratch_location` flag or leave it empty, Pathways automatically falls back to an in-memory compilation cache. This cache does not persist compiled XLA executables across Pathways deployments.

This cache is similar to the [JAX compilation cache](https://docs.jax.dev/en/latest/persistent_compilation_cache.html) which is disabled by `pathwaysutils.initialize()` for Pathways workloads.

The following Cloud Storage permissions are required for the compilation cache:

  * `storage.buckets.get`: To retrieve bucket metadata.
  * `storage.buckets.update`: Essential for Pathways to set up object lifecycle policies to enforce TTL for cache eviction.
  * `storage.objects.list`: To list existing cache objects within the bucket.
  * `storage.objects.create`: To write new compiled executables to the cache.
  * `storage.objects.get`: To read cached executables from the bucket.



## Profiling

You can use the JAX profiler to generate traces of a JAX program. There are two common ways supported with Pathways:

  * [Programmatic](https://jax.readthedocs.io/en/latest/profiling.html#programmatic-capture)
    * Programmatically capture profiles from your JAX code
  * [Manual](https://jax.readthedocs.io/en/latest/profiling.html#manual-capture)
    * Capturing profiles on demand after starting the profiler server from your JAX code



In both cases, the profiles are written to a Cloud Storage bucket. There will be multiple trace files created in the Cloud Storage bucket potentially under different timestamp folders, for example:

  * Main Python process which invoked the trace (typically your notebook VM): `<jax-client-vm-name>.xplane.pb`
  * Pathways IFRT proxy: `client.<var>PATHWAYS_HEAD_NODE_NAME</var>.xplane.pb`
  * Pathways Resource manager: `server.*<var>PATHWAYS_HEAD_NODE_NAME</var>.xplane.pb`
  * Pathways worker(s): `server.*<tpu-node-name>.xplane.pb`



These trace files can be analyzed with TensorBoard by running the following command. For more information about TensorBoard and all of its profiling tools, see [Optimize TensorFlow performance using the Profiler](https://www.tensorflow.org/guide/profiler).
    
    
    # verify trace files are present
    gsutil ls -l -r gs://BUCKET/PREFIX
    
    # View on tensorboard
    tensorboard --logdir=gs://BUCKET/PREFIX

Replace the following:

  * `BUCKET` : a Cloud Storage bucket to store the trace files
  * `PREFIX`: a path within your Cloud Storage bucket to store the trace files



### Programmatic profile capture

Capture a profile from inside your code. The profiles are saved inside `gs://<bucket>/<prefix>` under a timestamp directory
    
    
    import jax
    import pathwaysutils
    
    pathwaysutils.initialize()
    
    jax.profiler.start_trace("gs://BUCKET/PREFIX")
    
    # Run the operations to be profiled
    key = jax.random.key(0)
    x = jax.random.normal(key, (5000, 5000))
    y = x @ x
    y.block_until_ready()
    
    jax.profiler.stop_trace()

### Manual profile capture

To manually capture profile information, you must start the profiler server from your Python code:
    
    
    import jax
    import pathwaysutils
    
    pathwaysutils.initialize()
    jax.profiler.start_server(jax_profiler_port)
    
    # Your JAX code
    jax.profiler.stop_server() # this is functionally a no-op
    

While the profiler server is running, you can capture a profile and export the data to the target Cloud Storage location:
    
    
    export DURATION_IN_SECS=6
    export OUTPUT_DIR=gs://<var>BUCKET</var>/<var>PREFIX</var>
    
    curl -d "{\"duration_ms\":\"${DURATION_IN_SECS} * 1000 }}\", \"repository_path\":\"${OUTPUT_DIR}\"}" -H "Content-Type: application/json" -X POST http://localhost:<jax_profiler_port>
    

You can find timing information for IFRT proxy client methods like `Compile` and `Execute` within your program's trace. These events, which detail the interactions with the IFRT Proxy gRPC server during compilation and execution, appear on the thread named `GrpcClientSessionUserFuturesWorkQueue`. By examining this thread in your trace, you can gain insights into the performance of these operations.

## XLA Flags

When you use Pathways, you must set the XLA flags in the `pathways-proxy` container.

When you use Cluster Toolkit (the `gcluster job submit` command), set XLA flags by using `--pathways-proxy-args`:
    
    
    --pathways-proxy-args="--xla_flag_1=value1 --xla_flag_2=value2"
    

## HLO Dump

To inspect High Level Optimizer (HLO) inputs that are given to the XLA compiler, you can configure Pathways to dump the HLO to a specified Cloud Storage location by using `--pathways-proxy-args`:
    
    
    --pathways-proxy-args="--xla_dump_to=gs://BUCKET_NAME/HLO_PREFIX/"
    

## What's next

  * [Create a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)
  * [Multihost inference with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference)
  * [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
  * [Pathways interactive mode](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
  * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
  * [Troubleshoot Pathways on cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
