---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways/
title: Troubleshoot Pathways on cloud \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:00.443288+00:00
---

# Troubleshoot Pathways on cloud  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Troubleshoot Pathways on cloud Stay organized with collections  Save and categorize content based on your preferences. 

## Before you begin

  * [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment)
  * [Installed Kubernetes tools](https://kubernetes.io/docs/tasks/tools/)
  * [Installed the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install)
  * [Enabled the Google Kubernetes Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api)
  * [Created a Google Kubernetes Engine cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)



This document explains how to troubleshoot your Pathways workloads.

## Viewing logs

You can view logs for your Pathways workloads directly by using the `gcluster job logs` command (pass `--main-only=false` to include worker pod logs):
    
    
    gcluster job logs WORKLOAD_NAME \
        --cluster=CLUSTER \
        --project=PROJECT_ID \
        --location=LOCATION \
        --main-only=false
    

To list all pods for your workload by using `kubectl`, use the Cluster Toolkit workload label:
    
    
    kubectl get pods -l gcluster.google.com/workload=WORKLOAD_NAME
    

To check workload status or list failed jobs, use the `gcluster job list` command:
    
    
    gcluster job list --status Failed \
        --cluster=CLUSTER \
        --project=PROJECT_ID \
        --location=LOCATION
    

**Note:** Status values for the `gcluster job list` command are case-sensitive (`Pending`, `Running`, `Succeeded`, `Failed`, `Suspended`).

Alternatively, in the Cloud Logging [Logs Explorer](https://console.cloud.google.com/logs/query), use the following query adjusted to match your project, region, cluster, and workload:
    
    
    resource.type="k8s_container"
    resource.labels.project_id="PROJECT"
    resource.labels.location="LOCATION"
    resource.labels.cluster_name="CLUSTER"
    resource.labels.namespace_name="default"
    resource.labels.pod_name:"WORKLOAD_NAME"
    

Replace the following:

  * `PROJECT` : your Google Cloud project ID
  * `LOCATION`: the region or zone where you created your GKE cluster
  * `CLUSTER` : the name of your GKE cluster
  * `WORKLOAD_NAME`: the name of your workload when you use Cluster Toolkit or the JobSet name when you use `kubectl`



This query will match multiple Pathways Kubernetes containers with names like `pathways-rm`, `pathways-proxy`, `pathways-worker`. You can narrow down which container is causing a problem by adding a filter on container name like `resource.labels.container_name:"<container_name>"`

## Monitoring

### Health monitoring

You can monitor the health of various Pathways components by looking for entries in the container logs, for example:

`pathways-proxy` is ready to serve new connection requests when the following log is written:
    
    
    kubectl logs ${HEAD_POD_NAME} --container pathways-proxy
    ...
    I1101 04:51:41.967764       1 proxy_server.cc:125] IFRT proxy server started with status OK
    

`pathways-rm` is ready to serve new connection requests when the following log is written:
    
    
    kubectl logs $HEAD_POD_NAME --container pathways-rm
    ...
    I1101 04:50:41.967764       1 server_lib.cc:1473] Pathways Server serving on [::]:29001
    

To verify all TPUs registered to the Pathways Resource Manager are ready, you can look for `***<num slices>/<num slices> Pathways Slices Now Ready ***` in the `pathways-rm` container logs:
    
    
    kubectl logs $HEAD_POD_NAME --container pathways-rm
    ...
    I1101 04:52:41.967764       1 multi_job_allocator.cc:1063] *** 2/2 Pathways Slices Now Ready ***
    

The Pathways client can make connections to the IFRT Proxy server as long as the proxy server is ready even if not all slices are ready. Your job works with virtual slices until the slice becomes ready. Virtual slices allow your code to run when TPUs are unavailable.

`pathways-worker` is ready to serve new connection requests when the following log is written:
    
    
    kubectl logs $WORKER_POD_NAME --container pathways-worker
    ...
    I1101 04:50:41.967764       1 server_lib.cc:1473] Pathways Server serving on [::]:29001
    

### Metrics collection

Pathways can write low level system metrics to Cloud Monitoring for debugging. The metrics include:

  * DCN Transfer Latency
  * Collective Latency
  * Host to Device Transfer Latency
  * Device to Host transfer Latency



You can find the metrics on the Cloud Monitoring dashboard of the Google Cloud project where the GKE cluster is running.

To monitor these metrics in Metrics Explorer:

  1. Navigate to the [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer).
  2. Filter by the name of the metric using the _Select a metric_ field.
  3. Filter by your workload name and time range by selecting _Add Filter_ and filter by _pod_name_.
  4. Choose an appropriate _aggregation type_ based on the metric and the workloads that you're monitoring.



#### DCN transfer latency

This is a Megascale XLA (MXLA) metric that measures the cumulative distribution of network-transfer latencies for multislice traffic. Latency measurement starts when a request for data to be transferred over the DCN is issued and ends when an acknowledgement is received that the transfer of data has completed. To monitor this metric, filter by the `dcn_transfer_latencies` metric name.

#### Collective latency

This is a MXLA metric that measures the cumulative distribution of end to end collective latency for multislice traffic. Latency measurement starts when a request for a collective is issued and ends when an acknowledgement is received that the data transfer has completed. To monitor this metric, filter by the `collective_e2e_latency` metric name.

#### Host to device transfer latency

This is a MXLA metric that measures the cumulative distribution of host to device transfer latencies for multislice traffic. Latency measurement starts when a request for data to be transferred over the DCN is issued and ends when an acknowledgement is received that the data transfer has completed. To monitor this metric, filter by `host_to_device_transfer_latencies` metric name.

#### Device to host transfer latency

This is a MXLA metric that measures the cumulative distribution of device to host transfer latencies for multislice traffic. Latency measurement starts when a request for data to be transferred over the DCN is issued and ends when an acknowledgement is received that the data transfer has completed. To monitor this metric, filter by the `device_to_host_transfer_latencies` metric name.

## Debugging common errors

**Unable to hash accelerator config warnings**

The following messages are only warnings and don't affect the performance of your JAX code.
    
    
    INFO:jax._src.cache_key:get (_hash_accelerator_config): unable to hash accelerator config, falling back to hashing devices + platform: UNIMPLEMENTED: GetTopologyForDevices is not supported for the IFRT proxy client. (type <class 'jaxlib.xla_extension.XlaRuntimeError'>)
    

**Permission`logging.logEntries.create` denied on resource**

If you see the following error, ensure the Compute Engine service account used by Vertex AI Workbench has permissions to write log entries to the Google Cloud logging system.
    
    
    INFO:absl:Created 'ArrayHandler' with primary_host=0, replica-id=0
    WARNING:absl:pathwaysutils: Detected Pathways-on-Cloud backend. Applying changes.
    Failed to submit 1 logs.
    Traceback (most recent call last):
      File "/opt/conda/lib/python3.10/site-packages/google/api_core/grpc_helpers.py", line 65, in error_remapped_callable
        return callable_(**args, **kwargs)
      File "/opt/conda/lib/python3.10/site-packages/grpc/_channel.py", line 1181, in __call__
        return _end_unary_response_blocking(state, call, False, None)
      File "/opt/conda/lib/python3.10/site-packages/google/api_core/grpc_helpers.py", line 1006, in _end_unary_response_blocking
        raise _InactiveRpcError(state) # pytype: disable-not-instantiable
    grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
      status = StatusCode.PERMISSION_DENIED
      details = "Permission 'logging.logEntries.create' denied on resource (or it may not exist)."
      debug_error_string = "UNKNOWN:Error received from peer ipv4:216.239.34.174:443 {created_time:"2024-10-03T20:30:44.820425276+00.00", grpc_status:7, grpc_message:"Permission \'logging.logEntries.create\' denied on resource (or it may not exist)."}"
    >
    

To fix this issue, add the [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) role to the Compute Engine service account.

**Not able to connect to the IFRT proxy server**

If you see this error, your IFRT proxy client is not able to connect to the IFRT proxy server.

  * Ensure your VPC network is configured correctly
  * Ensure your firewall is configured to allow the connection
  * Ensure your Pathways cluster has been provisioned
  * Check for start up error messages



When your first JAX command that sends an IFRT command to the Pathways cluster tries to execute, it will stop responding for about a minute and then display a `RuntimeError` like the following:
    
    
    RuntimeError: Unable to initialize backend 'proxy': UNAVAILABLE: Unable to establish connection to ifrt_proxy server, please check provided address example-workload-proxy-0-0.example-workload.default.svc.example-cluster-domain.:38676'; detailed error: DNS resolution failed (set JAX_PLATFORMS='' to automatically choose an available backend)
    

**There is an existing connection to the Pathways cluster**

A Pathways cluster can only maintain a session with one client at a time. If two separate notebooks attempt to connect to the same Pathways cluster, one will be able to connect and the other will show the following errors.
    
    
    INFO:absl:Created ArrayHandler with primary_host=0, replica_id=0
    WARNING:absl:pathwaysutils: Detected Pathways-on-Cloud backend. Applying changes.
    E0927 21:19:52.919607   37624 rpc_helper.cc:56] Connection to IFRT proxy server was terminated: CANCELLED: Cancelled
    E0927 21:20:03.467547   37719 rpc_helper.cc:56] Connection to IFRT proxy server was terminated: CANCELLED: Cancelled
    E0927 21:20:14.011645   37807 rpc_helper.cc:56] Connection to IFRT proxy server was terminated: CANCELLED: Cancelled
    E0927 21:20:24.557955   37924 rpc_helper.cc:56] Connection to IFRT proxy server was terminated: CANCELLED: Cancelled
    ---------------------------------------------------------------------------
    XlaRuntimeError                           Traceback (most recent call last)
    File /opt/conda/lib/python3.10/site-packages/jax/_src/xla_bridge.py:887, in backends()
        885   continue
    --> 887 backend = _init_backend(platform)
        888 _backends[platform] = backend
    
    File /opt/conda/lib/python3.10/site-packages/jax/_src/xla_bridge.py:973, in _init_backend(platform)
        972 logger.debug("Initializing backend '%s'", platform)
    --> 973 backend = registration.factory()
        974 # TODO: consider raising more descriptive errors directly from backend
        975 # factories instead of returning None.
    
    File /opt/conda/lib/python3.10/site-packages/pathwaysutils/proxy_backend.py:24, in register_backend_factory.<locals>.<lambda>()
         21 def register_backend_factory():
         22   xla_bridge.register_backend_factory(
         23       "proxy",
    ---> 24       lambda: ifrt_proxy.get_client(
         25           jax.config.read("jax_backend_target"),
         26           ifrt_proxy.ClientConnectionOptions(),
         27       ),
         28       priority=-1,
         29   )
    
    XlaRuntimeError: UNAVAILABLE: Unable to establish connection to ifrt_proxy server, please check provided address example-workload-proxy-0-0.example-workload.default.svc.example-cluster-domain.:38676'; detailed error: Connection to IFRT proxy server was terminated: CANCELLED: Cancelled
    
    During handling of the above exception, another exception occurred:
    
    RuntimeError                              Traceback (most recent call last)
    Cell In[2], line 4
          1 import pathwaysutils
          3 import jax
    ----> 4 print(jax.devices())
    
    File /opt/conda/lib/python3.10/site-packages/jax/_src/xla_bridge.py:1085, in devices(backend)
       1060 def devices(
       1061     backend: str | xla_client.Client | None = None
       1062 ) -> list[xla_client.Device]:
       1063   """Returns a list of all devices for a given backend.
       1064
       1065   .. currentmodule:: jaxlib.xla_extension
       (...)
       1083     List of Device subclasses.
       1084   """
    -> 1085   return get_backend(backend).devices()
    
    File /opt/conda/lib/python3.10/site-packages/jax/_src/xla_bridge.py:1019, in get_backend(platform)
       1015 @lru_cache(maxsize=None)  # don't use util.memoize because there is no X64 dependence.
       1016 def get_backend(
       1017     platform: None | str | xla_client.Client = None
       1018 ) -> xla_client.Client:
    -> 1019   return _get_backend_uncached(platform)
    
    File /opt/conda/lib/python3.10/site-packages/jax/_src/xla_bridge.py:998, in _get_backend_uncached(platform)
        994   return platform
        996 platform = (platform or _XLA_BACKEND.value or _PLATFORM_NAME.value or None)
    --> 998 bs = backends()
        999 if platform is not None:
       1000   platform = canonicalize_platform(platform)
    
    File /opt/conda/lib/python3.10/site-packages/jax/_src/xla_bridge.py:903, in backends()
        901       else:
        902         err_msg += " (you may need to uninstall the failing plugin package, or set JAX_PLATFORMS=cpu to skip this backend.)"
    --> 903       raise RuntimeError(err_msg)
        905 assert _default_backend is not None
        906 if not config.jax_platforms.value:
    
    RuntimeError: Unable to initialize backend 'proxy': UNAVAILABLE: Unable to establish connection to ifrt_proxy server, please check provided address 'example-workload-proxy-0-0.example-workload.default.svc.example-cluster-domain.:38676'; detailed error: Connection to IFRT proxy server was terminated: CANCELLED: Cancelled (set JAX_PLATFORMS='' to automatically choose an available backend)
    

Once the original client disconnects, the second client will be able to connect. After an unexpected disconnection, you may need to restart the Pathways cluster to enable other clients to connect.

**LocalProxy.**init**() got an unexpected keyword argument 'unbound_message'**

If you see this error after importing `pathwaysutils`, check if there are outdated versions of Flask or Werkzeug installed in your environment:
    
    
     pip3 list --outdated (replacing pip with pip3 as needed)
    

If Flask or Werkzeug is listed, consider upgrading them with the caveat that doing so may break other packages or dependencies in your project:
    
    
     pip install flask Werkzeug --upgrade ()
    

**Internal error from proxy server**
    
    
    "Internal error from proxy server during Array::IsDeleted(): UNAVAILABLE:Connection to IFRT proxy server was terminated: FAILED_PRECONDITION:
    GrpcClientSession: writes no longer allowed."
    

This error indicates that the IFRT Proxy server has disconnected from the client. This can be fixed by restarting your client. For notebooks, you can restart the notebook kernel and rerun your notebook.

**SIGTERMS and HBM OOM**

A SIGTERM found in the logs associated with a RESOURCE_EXHAUSTED error may indicate an HBM OOM, in this case, you can reduce the amount HBM memory used in your JAX code.

**INVALID_ARGUMENT**
    
    
    "INVALID_ARGUMENT : Permanent error, with a last message of Lifecycle
    matches_prefix cannot specify more than 50 prefixes per config.; Error while
    initializing persistent cache storage Cloud Storage"
    

This error occurs if the Cloud Storage bucket passed in to the `--pathways_gcs_location` flag has reached the maximum lifecycle policy limit. If this occurs, clean up Cloud Storage lifecycle policies that are no longer being used.

**Permanent error**
    
    
    Permanent error, with a last message of The specified bucket does not exist.; Error while initializing persistent cache storage gcs
    

This error is printed on the Resource Manager or Pathways workers when you provide an invalid Cloud Storage location to pathways containers.

**Error response from daemon**
    
    
    Error response from daemon: dockerfile parse error line 16: Unknown flag: exclude
    

This is due to an old version of docker, upgrade your docker version.

**IFRT Proxy client and server failed to agree**
    
    
    IFRT Proxy client and server failed to agree on the protocol version; supported versions: client = [1, 1], server = [3, 14]
    

This indicates that an older version of MaxText is being used, please ensure that you rebuild the latest MaxText image.

## What's next

  * [Create a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)
  * [Multihost inference with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference)
  * [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
  * [Pathways interactive mode](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
  * [Porting JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
