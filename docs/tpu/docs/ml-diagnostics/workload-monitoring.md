---
url: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/workload-monitoring/
title: Workload monitoring with ML Diagnostics \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:01.717923+00:00
---

# Workload monitoring with ML Diagnostics  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/workload-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Workload monitoring with ML Diagnostics

Workload Monitoring is a built-in capability within the ML Diagnostics platform for detecting and diagnosing issues affecting AI/ML workloads running on TPUs on Google Cloud. For every GKE job, ML Diagnostics Workload Monitoring automatically creates an ML run and monitors TPU duty cycle across the workload to detect events affecting the workload.

ML Diagnostics Workload Monitoring has the following key features:

  * **Workload-to-node mapping:** Automatically identify the Google Cloud nodes your workload is using. This is available by default for all TPU workloads on GKE.
  * **Status tracking:** Monitor workload statuses for multiple states, including `performance degradation`, `hang`, `orchestrator interruption`, and `termination`.
  * **Metric-based problem detection:** Detect workload problems (performance degradation, hangs, orchestrator interruption, and terminations) by monitoring the Aggregated TPU duty cycle. By default, a 15% drop in duty cycle indicates a performance degradation and triggers analysis. For other events, other indicators are used to detect hangs, orchestrator interruptions and terminations.
  * **Automated diagnosis:** If a problem is detected, automated analyzers run to find potential infrastructure, orchestrator or framework causes. Analyzers include: 
    * Infrastructure: ICI Link, Thermal, TPU throttling, HBM capacity, HBM bandwidth, Host memory utilization, CPU utilization, ToR uplink congestion, ToR NIC link.
    * Orchestrator: GKE Nodepool interruption, GKE slice interruption.
    * Framework: Megascale XLA hang.
  * **Issue localization:** Pinpoint the specific nodes and instances affected by detected issues.
  * **Suggested actions:** Recommended steps for recovery or further investigation, such as restarting a job, removing a potentially faulty node, or collecting XProf profiles.
  * **Event timeline:** Display a timeline of workload events alongside the TPU duty cycle metric to help correlate events with metric time series.
  * **Analysis details:** Detailed reports for analyzers run for each event.
  * **System metrics** : System metrics are recorded automatically at 1-minute intervals for every workload monitoring ML Run. These system metrics provide additional information to correlate with workload events for deeper analysis. System metrics include: 
    * TPU device: duty cycle, tensorcore utilization.
    * Host device: host CPU utilization, host memory utilization.
    * HBM: memory bandwidth utilization, HBM memory total, HBM memory used.
    * Megascale XLA: MXLA DCN transfer latency, MXLA inbound transfer latency, MXLA compute latency, MXLA e2e collective latency, MXLA d2h latency, MXLA h2d latency.



## Prerequisites

To use ML Diagnostics Workload Monitoring, enable the [Cluster Director](https://docs.cloud.google.com/cluster-director/docs/overview) API and add the required IAM permissions. For more information, see [ML Diagnostics prerequisites](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/overview#prerequisites).

## Get started

When you submit your TPU job on GKE, the ML Diagnostics system automatically begins tracking your workload without requiring any manual code instrumentation. Diagnostic information is displayed in the ML Diagnostics Google Cloud console and can be retrieved using the ML Diagnostics CLI or API. Diagnostic information is listed for each Machine Learning Run (ML Run)

Workload monitoring is automatically enabled for GKE versions 1.36.0-gke.4447000 and later. Megascale XLA hang and Megascale XLA metrics are available with LibTPU versions 0.40.0 and later.

## Workload Monitoring and analyzers

ML Diagnostics continuously monitors your workload performance by monitoring TPU duty cycle and how it relates to the underlying infrastructure. By default, a 15% drop in duty cycle indicates a performance degradation and triggers analysis. For other events, other indicators are used to detect hangs, orchestrator interruptions, and terminations.

The workload states are tracked automatically and assigned one of the following values:

  * `running`: The workload is actively executing. This state is not directly displayed in the Google Cloud console.
  * `termination`: The workload terminated and is no longer running. This can be due to an expected orchestrator interruption (which results in a restart), a successful completion, or a failed job.
  * `hang`: Detected by a prolonged period of minimal to no TPU activity without workload completion.
  * `performance degradation`: Triggered by a significant drop in performance metrics like aggregated TPU duty cycle.
  * `Orchestrator interruption`: Detected GKE interruption of the orchestrator. This includes slice interruptions for TPU7x (ironwood), and nodepool interruptions for earlier versions.



For problems detected in the workload, ML Diagnostics triggers a set of analyzers to help diagnose potential problems with the workload at the infrastructure, orchestrator, and framework layers. These analyzers identify infrastructure, orchestrator or framework problems, pinpoint which nodes are affected, and suggest troubleshooting steps.

### ICI Link Analyzer

ICI Link Analyzer detects issues with the Inter-Chip Interconnect (ICI) links that connect TPUs within a slice. This analyzer detects potential ICI networking issues on the links between TPU processors. The analyzer locates the specific nodes on which the problematic workloads are running.

### Thermal Analyzer

Thermal Analyzer monitors and detects TPU nodes that are overheating. Excessive temperatures can negatively affect workload performance. The analyzer identifies the specific nodes experiencing thermal problems, which can be caused by overheating in the tensor cores or High Bandwidth Memory (HBM).

### TPU Throttling Analyzer

TPU Throttling Analyzer detects when TPU chip throttling occurs. This can be due to power, thermal, or other hardware constraints. The analyzer pinpoints the specific nodes where throttling is occurring.

### HBM Capacity Analyzer

HBM Capacity Analyzer monitors the High Bandwidth Memory (HBM) utilization of TPU nodes. This analyzer detects TPU nodes where HBM utilization is either approaching the limit (around 90%) or causing an out-of-memory (OOM) errors. Potential troubleshooting actions include collecting XProf profiling traces for detailed HBM memory usage analysis. You should also consider modifying workload configurations to optimize HBM usage, such as reducing the batch size or adjusting model parameters.

### HBM Bandwidth Analyzer

HBM Bandwidth Analyzer monitors the High Bandwidth Memory (HBM) read and write bandwidth of TPU nodes and instances. This analyzer detects TPU instances where HBM bandwidth is being throttled, which indicates that High Bandwidth Memory (HBM) operations are being restricted. This is likely due to bandwidth limits or hardware issues, like high TPU chip temperature. The analyzer pinpoints the specific instances where throttling is occurring.

### Host Memory Utilization Analyzer

Host Memory Utilization Analyzer monitors the non-evictable host memory utilization of TPU nodes and instances. This analyzer detects TPU instances where non-evictable host memory utilization is running close to its limit, which can degrade performance and increase the risk of Out-of-Memory (OOM) events. This can be caused by excessive prefetching or buffering in the data pipeline, temporary RAM spikes during checkpoint operations, or memory leaks in custom loaders. For GKE workloads, see [GKE best practices](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#identify-workloads) for identifying workloads and configuring appropriate memory requests and limits.

### CPU Utilization Analyzer

CPU Utilization Analyzer monitors the host CPU utilization of TPU nodes and instances. This analyzer detects TPU instances where host CPU utilization is running close to the allocated limit. This can negatively impact application performance, potentially causing slowdowns or unresponsiveness. Potential troubleshooting actions include using Cloud Profiling for detailed CPU usage analysis. For GKE workloads, see [ GKE best practices](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#identify-workloads) for identifying workloads and configuring appropriate memory requests and limits.

### ToR NIC Link Analyzer

This analyzer detects networking issues between Top-of-Rack (ToR) switch and Network Interface Card (NIC) Links. The analyzer locates the specific instances on which the problematic workloads are running.

### ToR Uplink Congestion Analyzer

This analyzer detects issues with Top-of-Rack (ToR) switches experiencing network path congestion. This analyzer indicates high utilization on specific uplink ports. The analyzer locates the specific instances on which the congestion is happening.

### GKE Orchestrator Slice Interruption Analyzer

**Note:** This analyzer is only available for TPU7x (Ironwood).

This analyzer detects slice-level interruption events at the GKE orchestrator layer. When a slice interruption is detected, the analyzer identifies the affected slice and pinpoints the underlying sub-block as the potential root cause of the interruption. This analyzer works at the level of each slice in the workload, so you get slice interruption events for each slice individually.

### GKE Orchestrator Nodepool Interruption Analyzer

**Note:** This analyzer is available for TPU v6e (Trillium) and earlier.

This analyzer detects nodepool interruption events occurring at the GKE orchestrator layer. For TPU generations TPU v6e (Trillium) and before, GKE does not register a unified "Slice" resource. It only registers standard, individual Compute Engine VMs (Nodes) bound together as nodepools.

When a node goes down due to a planned interruption (maintenance, preemption, or host error) or an unplanned failure, GKE automatically applies Taints (like `node.kubernetes.io/unreachable`) and changes the node's condition to `NotReady`. The Nodepool Interruption analyzer uses these indicators to detect orchestrator interruptions.

### Megascale XLA (MXLA) Hang Analyzer

This analyzer detects hangs affecting multi-slice TPU workloads at the MXLA framework layer. Cloud TPU Multi-slice environments are composed of multiple TPU slices that communicate over the Data Center Network (DCN). Multi-slice workloads use Megascale collectives to communicate over DCN. A Megascale hang occurs when a worker has waited on a Megascale communication operation for a set timeout period. In these cases, you receive a Megascale `HANG_DETECTED` message in your Cloud TPU logs.

Megascale typically detects and reports hangs, since it is responsible for communicating over DCN. However, this does not necessarily mean that the error is caused by Megascale. Often, hang detection is a symptom of a problem in another part of the system. For this reason, the Megascale `HANG_DETECTED` message is a catch-all indication that a workload is not progressing properly. This could be caused by third-party software, Google-owned software, or an issue with the hardware itself.

Rather than manually going through user logs, this analyzer is automatically triggered when hangs occur and provides analyzer reports on potential causes of the hang within the ML Diagnostics system. The analyzer identifies the following potential causes:

  1. `BAD_TPU_CHIP`: The MXLA hang was likely caused by a TPU tensorcore issue. The analyzer also reports the specific instances which are showing issues.
  2. `BAD_SC_CHIP`: The MXLA hang was likely caused by a TPU sparsecore issue. The analyzer also reports the specific instances which are showing issues.
  3. `NETWORKING_ISSUE`: The MXLA hang was likely caused by a networking issue in DCN network. The analyzer also reports the specific instances which are showing issues.
  4. `DIFFERENT_MODULE`: The MXLA hang was likely caused by running different HLO modules on different VMs. To identify the cause, inspect the digest printed by the analyzer in the logs.
  5. `FINGERPRINT_MISMATCH`: The MXLA hang was likely caused by inconsistent HLO module compilation across VMs. This is likely a bug in JAX tracing or the XLA compiler. To identify the cause, inspect the digest printed by the analyzer in the logs. Dump your HLO and share the output with the Google XLA compiler team to further debug. For more, see [Dump HLO Computations](https://openxla.org/xla/hlo_dumps).
  6. `DATA_INPUT_STALL`: The MXLA hang was likely caused by data input stall. The analyzer also reports the specific instances which are showing issues.
  7. `ICI_ERROR`: The MXLA hang was likely caused by ICI error. The analyzer also reports the specific instances which are showing issues.
  8. `PROGRAM_NOT_QUEUED`: The MXLA hang was likely caused by some VM not queuing programs to TPU. Check if your application is blocked or crashing, which prevents JAX from queueing the next TPU program (jitted functions).
  9. `LAUNCHES_ORDER_INCONSISTENT`: The MXLA hang was likely caused by an inconsistent launch order across VMs. To identify the cause, inspect the digest printed by the analyzer in the logs.
  10. `UNRECOVERABLE_ERROR`: The MXLA hang was caused by an unrecoverable error. The analyzer also reports the specific instances which are showing issues. Inspect the error log of the instances with unrecoverable error. If the error appears to be specific to the given machine (for example, failure to copy data from TPU to host), then you need to configure your job to avoid those hosts. If the error logs don't indicate this is related to a given machine, then the problem is likely at the application level.
  11. `UNKNOWN`: The MXLA hang was detected but a potential cause is not determined.



## System Metrics

For every workload monitoring ML run, system metrics are automatically collected by Cloud Monitoring at 1-minute intervals. These system metrics provide additional information to correlate with workload events and for deeper analysis alongside the analyzer results. The system metrics include:

  * TPU device metrics: duty cycle (`node/accelerator/duty_cycle`), tensorcore utilization (`node/accelerator/tensorcore_utilization`).
  * Host device metrics: host CPU utilization (`node/cpu/allocatable_utilization`), host memory utilization (`node/memory/allocatable_utilization`).
  * HBM metrics: memory bandwidth utilization (`node/accelerator/memory_bandwidth_utilization`), HBM memory total (`node/accelerator/memory_total`), HBM memory used (`node/accelerator/memory_used`).
  * MXLA metrics for multi-slice workloads: MXLA DCN transfer latency (`container/multislice/network/dcn_transfer_latencies`), MXLA inbound transfer latency (`container/multislice/network/dcn_inbound_transfer_latencies`), MXLA compute latency (`container/multislice/accelerator/compute_latencies`), MXLA e2e collective latency (`container/multislice/network/collective_end_to_end_latencies`), MXLA d2h latency (`container/multislice/accelerator/device_to_host_transfer_latencies`), MXLA h2d latency (`container/multislice/accelerator/host_to_device_transfer_latencies`).



For information on system metrics, see [GKE system metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes).

To log system metrics at finer grain intervals, use the ML Diagnostics SDK and set `log_system_metrics=true`. For a list of system metrics logged at the 10-second interval by the SDK, see [ML Diagnostics (`google-cloud-mldiagnostics`) SDK](https://github.com/AI-Hypercomputer/google-cloud-mldiagnostics) documentation. By default, system metrics collected at the 1-minute interval are automatically pulled into the ML Diagnostics system.

## View Workload Monitoring in Google Cloud console

You can view your runs monitored by ML Diagnostics workload monitoring in the Google Cloud console both under [Cluster Director](https://docs.cloud.google.com/cluster-director/docs/overview) as well as under GKE

To view all your machine learning runs in Cluster Director:

  1. In the Google Cloud console, go to the **Cluster Director** page.
  2. Click the **Run Diagnostics** tab.



[Go to Cluster Director Run Diagnostics](https://console.cloud.google.com/cluster-director/diagnostics)

To view all your machine learning runs in Google Kubernetes Engine:

  1. In the Google Cloud console, go to the **Kubernetes** page.
  2. In the navigation menu, click **AI/ML**.
  3. Click the **Run Diagnostics** tab.



[Go to GKE AI/ML Run Diagnostics](https://console.cloud.google.com/kubernetes/aiml/diagnostics)

The Cluster Director and GKE consoles display the following information:

  * **Run Summaries:** The table contains the name of each run created by Workload Monitoring for a GKE job. Runs are automatically named using the `job-name-timestamp` format.

  * **Run Details (Monitoring Overview):** Select an ML run to see detailed information within the "Monitoring Overview" tab. This tab contains:

    * **Aggregated TPU duty cycle** : A graph of the aggregated TPU duty cycle for your ML run.
    * **Events timeline** : A timeline of all events that have affected the ML run, including performance degradations, hangs, orchestrator interruptions, and terminations.
    * **Events Table:** This table summarizes events that affected the ML run. For each event, it includes: 
      * Event name and event type.
      * Start time and end time of event.
      * Links to details from analyzers.
    * **Event Details:** Select **View details** for an event to see all analyzer results for that event.
    * **System metrics** : A list of system metrics pulled automatically at a 1-minute interval from Cloud Monitoring or logged at a more granular level by ML Diagnostics SDK



## Access Workload Monitoring information through Google Cloud CLI

For every GKE job, Workload Monitoring automatically creates a Machine Learning Run within ML Diagnostics with an ML run name using the `job-name-timestamp` format. You can use ML Diagnostics gcloud CLI commands such as `Describe`, `List`, `Delete`, and `Update` to view all ML runs created in a project, get details of those runs, and delete or update properties of the ML run.

In addition, you can use `monitored-events` Google Cloud CLI commands to list all the events detected by workload monitoring and retrieve analyzer details of each event. For more information, see [Use ML Diagnostics CLI](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/cli).

## Access Workload Monitoring information through the API

You can access the events detected by Workload Monitoring through the "GET" method for the `MonitoredEvent` API.

### List all monitored events

To list all monitored events (`MonitoredEvent`) for a given ML run, use the "GET" method with the `/v1alpha/{parent=projects/*/locations/*/machineLearningRuns/*}/monitoredEvents` endpoint.

The following is an example request:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
    
     "https://hypercomputecluster.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/machineLearningRuns/ML_RUN_ID/monitoredEvents"
    

The output is a `ListMonitoredEventsResponse` object, which is a JSON object that contains a list of `MonitoredEvent` summaries. The summaries provide an overview of event timestamps and details.

The following is an example of a `ListMonitoredEventsResponse` object:
    
    
    {
     "monitoredEvents": [
       {
         "name": "projects/user-project-id/locations/us-central1/machineLearningRuns/my-tpu-job-20260327T073000/monitoredEvents/event-id-456",
         "type": "PERFORMANCE_DEGRADATION",
         "displayName": "Performance degradation - 2026-03-27T07:45:10Z ",
         "startTime": "2026-03-27T07:45:10Z",
         "endTime": "2026-03-27T08:00:00Z",
         "analyzerReports": [
           {
             "analyzer": "TPU Throttling Analyzer",
             "detectionState": "NOT_DETECTED"
           }
           // ... additional analyzer reports
         ]
       },
       {
         "name": "projects/user-project-id/locations/us-central1/machineLearningRuns/my-tpu-job-20260327T073000/monitoredEvents/event-id-123",
         "type": "PERFORMANCE_DEGRADATION",
         "displayName": "Performance degradation - 2026-03-27T07:35:00Z ",
         "startTime": "2026-03-27T07:35:00Z",
         "endTime": "2026-03-27T08:15:00Z",
         "analyzerReports": [
           // ... analyzer reports
         ]
       }
       // ... other events
     ]
    }
    

### Get monitored events

To retrieve details of a specific monitored event (`MonitoredEvent`), Send a "GET" request to the `/v1alpha/{parent=projects/*/locations/*/machineLearningRuns/*}/monitoredEvents/*` endpoint.

The following is an example request:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://hypercomputecluster.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/machineLearningRuns/ML_RUN_ID/monitoredEvents/EVENT_ID"
    

The output is a `MonitoredEvent` object, which is a JSON object that contains information about the specified event. The `analyzer_reports` array within this object contains the detailed findings, status, and suggestions from each analyzer (ICI Link, Thermal, TPU Throttling, HBM Capacity) that was run in response to the detected event.

The following is an example of a `MonitoredEvent` object:
    
    
    {
     "name": "projects/user-project-id/locations/us-central1/machineLearningRuns/my-tpu-job-20260327T073000/monitoredEvents/event-id-456",
     "type": "PERFORMANCE_DEGRADATION",
     "displayName": "Performance degradation - 2026-03-27T07:45:10Z ",
     "startTime": "2026-03-27T07:45:10Z",
     "endTime": "2026-03-27T08:15:00Z",
     "analyzerReports": [
       {
         "analyzer": "ICI Link Analyzer",
         "detectionState": "DETECTED",
         "details": "ICI Link issues detected in <instance_ids>: This indicates networking issues on ICI links connected between TPU processors.",
         "recommendedActions": [
           {
             "description": "Contact Google team for further diagnosis. Potential action could be to Outkast affected nodes, but there could be other causes that need further investigation.",
             "documentationUrl": "https://docs.cloud.google.com/tpu/docs/ml-diagnostics/workload-monitoring"
           }
         ]
       },
       {
         "analyzer": "TPU Throttling analyzer",
         // ... results from TPU Throttling analyzer
       }
       // ... other analyzer reports
     ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
