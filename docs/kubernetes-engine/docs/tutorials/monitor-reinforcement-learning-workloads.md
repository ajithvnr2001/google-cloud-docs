---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/monitor-reinforcement-learning-workloads/
title: Monitor reinforcement learning workloads on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:10.415560+00:00
---

# Monitor reinforcement learning workloads on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/monitor-reinforcement-learning-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Monitor reinforcement learning workloads on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to emit, collect, and view key metrics and traces for Python-based reinforcement learning (RL) applications that are running on Google Kubernetes Engine (GKE).

This document shows you how to do the following:

  * Instrument the RL application to emit metrics and traces. The instrumentation used is for metrics and traces that follow the OpenTelemetry format.
  * Collect metrics and traces when the application runs on GKE. Data is collected using Managed OpenTelemetry for GKE ([Preview](https://cloud.google.com/products#product-launch-stages)).
  * View the collected metrics in Cloud Monitoring and traces in Cloud Trace.
  * Identify and understand critical RL metrics based on OpenTelemetry semantic conventions and golden signals. Golden signals are the four key metrics of a service that provide a high-level overview of its health: _Latency_ , _Traffic_ , _Errors_ , and _Saturation_.



## Before you begin

  1. Ensure you have a Python-based RL application that you want to monitor using metrics and trace data.

  2. Ensure you have a Google Cloud project with billing enabled.

  3. You need a GKE cluster running GKE version 1.34.1-gke.2178000 or higher, which are the versions where Managed OpenTelemetry for GKE ([Preview](https://cloud.google.com/products#product-launch-stages)) is available.

  4. Enable the following Google Cloud APIs:

     * `container.googleapis.com` (GKE)
     * `monitoring.googleapis.com` (Monitoring)
     * `cloudtrace.googleapis.com` (Trace)
     * `telemetry.googleapis.com` (OpenTelemetry Telemetry API)

You can enable these APIs using `gcloud`:
    
    gcloud services enable \
        container.googleapis.com \
        monitoring.googleapis.com \
        cloudtrace.googleapis.com \
        telemetry.googleapis.com
    

  5. **Install OpenTelemetry SDK:** In your Python RL application's environment, install the OpenTelemetry SDK and OTLP Exporter:
         
         pip install opentelemetry-sdk \
                     opentelemetry-exporter-otlp-proto-grpc \
                     opentelemetry-api
         

You might also need instrumentation libraries for any frameworks your RL app uses, for example, `opentelemetry-instrumentation-flask`.




## Costs

When you send telemetry data to Google Cloud, you are billed by ingestion volume. Metrics are billed using the Google Cloud Managed Service for Prometheus pricing, logs are billed using the Cloud Logging pricing, and traces are billed using the Cloud Trace pricing.

For information about costs associated with the ingestion of traces, logs, and Google Cloud Managed Service for Prometheus metrics, see [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing).

## Instrument your application with OpenTelemetry

Instrument your Python RL application code so that it can emit OpenTelemetry metrics. To instrument the application, do the following:

  1. Initialize OpenTelemetry by adding the following code to your application:
         
         import os
         import time
         from opentelemetry import metrics, trace
         from opentelemetry.sdk.metrics import MeterProvider
         from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
         from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
         from opentelemetry.sdk.trace import TracerProvider
         from opentelemetry.sdk.trace.export import BatchSpanProcessor
         from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
         from opentelemetry.sdk.resources import Resource
         from opentelemetry.metrics import Counter, Histogram, UpDownCounter
         
         resource = Resource.create({
             "service.name": "rl-training-service",
             "service.namespace": "opentelemetry-demo",
         })
         
         # Initialize Metrics
         reader = PeriodicExportingMetricReader(
             OTLPMetricExporter(
                 endpoint=os.environ.get("OTEL_EXPORTER_OTLP_METRICS_ENDPOINT", "localhost:4317"),
                 insecure=True
             )
         )
         meter_provider = MeterProvider(metric_readers=[reader], resource=resource)
         metrics.set_meter_provider(meter_provider)
         meter = metrics.get_meter("rl-training-meter")
         
         # Initialize Tracing
         trace_provider = TracerProvider(resource=resource)
         trace_processor = BatchSpanProcessor(
             OTLPSpanExporter(
                 endpoint=os.environ.get("OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "localhost:4317"),
                 insecure=True
             )
         )
         trace_provider.add_span_processor(trace_processor)
         trace.set_tracer_provider(trace_provider)
         tracer = trace.get_tracer("rl-training-tracer")
         

  2. Create instruments for each metric and record values that you want emitted by the application. Attach relevant semantic conventions as attributes.

Use the list of semantic conventions and golden signals to help determine which metrics to instrument for your application.

The following is an example of instruments for specific metrics:
         
         # Latency Histograms
         rl_loop_duration = meter.create_histogram(
             name="rl.loop.duration", description="Duration of a single RL loop iteration.", unit="ms"
         )
         rl_sample_duration = meter.create_histogram(
             name="rl.sample.duration", description="Duration of the sampling phase.", unit="ms"
         )
         rl_train_duration = meter.create_histogram(
             name="rl.train.duration", description="Duration of the training phase.", unit="ms"
         )
         # ... create other duration histograms (reward, train, sync, step)
         
         # Throughput Counters
         rl_sample_samples = meter.create_counter(
             name="rl.sample.samples", description="Number of samples generated.", unit="{samples}"
         )
         rl_train_steps = meter.create_counter(
             name="rl.train.steps", description="Number of training steps completed.", unit="{steps}"
         )
         # ... create other counter metrics (rl.sample.episodes, rl.train.tokens)
         
         # Performance/Saturation Gauges (using UpDownCounter)
         rl_reward_mean = meter.create_up_down_counter(
             name="rl.environment.reward.mean", description="Mean reward observed.", unit="1"
         )
         rl_train_loss = meter.create_up_down_counter(
             name="rl.train.loss", description="Current training loss.", unit="1"
         )
         rl_train_mfu = meter.create_up_down_counter(
             name="rl.train.mfu", description="Model Flop Utilization.", unit="1"
         )
         _rl_reward_mean_val, _rl_train_loss_val = 0.0, 0.0
         
         def get_common_attributes(rl_system, rl_run_id, rl_algorithm, rl_env_name, rl_model_name):
             return {
                 "rl.system": rl_system,
                 "rl.run.id": rl_run_id,
                 "rl.algorithm": rl_algorithm,
                 "rl.environment.name": rl_env_name,
                 "rl.model.name": rl_model_name,
             }
         
         # Example Usage within your RL code:
         common_attrs = get_common_attributes("MyPPO", "run-42", "PPO", "Acrobot-v1", "PolicyModelV1")
         
         # Inside the main RL loop:
         with tracer.start_as_current_span("rl_loop_iteration", attributes={**common_attrs, "rl.loop.iteration": 5}) as span:
             loop_start_time = time.perf_counter()
         # --- Sampling Phase ---
         sample_start = time.perf_counter()
         # ... perform sampling ...
         sampled_count = 1024
         rl_sample_samples.add(sampled_count, attributes={**common_attrs, "rl.sample.batch_size": 128})
         rl_sample_duration.record((time.perf_counter() - sample_start) * 1000, attributes=common_attrs)
         
         # --- Training Phase ---
         train_start = time.perf_counter()
         # ... perform training step ...
         rl_train_steps.add(1, attributes={**common_attrs, "rl.loop.iteration": 5})
         current_loss = 0.125
         rl_train_loss.add(current_loss - _rl_train_loss_val, attributes=common_attrs) # Record current loss
         _rl_train_loss_val = current_loss
         rl_train_duration.record((time.perf_counter() - train_start) * 1000, attributes=common_attrs)
         
         # --- Record Mean Reward ---
         current_mean_reward = -5.5
         rl_reward_mean.add(current_mean_reward - _rl_reward_mean_val, attributes=common_attrs)
         _rl_reward_mean_val = current_mean_reward
         
         loop_duration = (time.perf_counter() - loop_start_time) * 1000
         rl_loop_duration.record(loop_duration, attributes={**common_attrs, "rl.loop.iteration": 5})
         
         # Ensure metrics are pushed before application exit in short-lived scripts
         # For long-running services, PeriodicExportingMetricReader handles this.
         # meter_provider.shutdown()
         




Now that you have initialized OpenTelemetry and created instruments for specific metrics, the application emits the specified telemetry data when it runs.

## Enable collection of metrics and trace data in GKE

To collect the telemetry data that the application emits while it runs, you can use Managed OpenTelemetry for GKE ([Preview](https://cloud.google.com/products#product-launch-stages)). This feature collects telemetry data, such as metrics and traces, and sends the data to Google Cloud Observability.

To enable and configure Managed OpenTelemetry for GKE, do the following:

  1. Enable Managed OpenTelemetry for GKE on the cluster where the application runs. To do so, follow the steps in [Enable Managed OpenTelemetry for GKE in a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke#enable-managed-opentelemetry).

  2. Annotate your application Deployment with environment variables to direct the OpenTelemetry SDK to send telemetry data to the managed collector's OTLP endpoint. For a Python-based RL application, you can't use the automatic configuration feature from Managed OpenTelemetry for GKE.

Instead, add the following `env` section to your container specification in your Deployment manifest:
         
         env:
           - name: OTEL_COLLECTOR_NAME
             value: 'opentelemetry-collector'
           - name: OTEL_COLLECTOR_NAMESPACE
             value: 'gke-managed-otel'
           - name: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT
             value: $(OTEL_COLLECTOR_NAME).$(OTEL_COLLECTOR_NAMESPACE).svc.cluster.local:4317
           - name: OTEL_EXPORTER_OTLP_TRACES_ENDPOINT
             value: $(OTEL_COLLECTOR_NAME).$(OTEL_COLLECTOR_NAMESPACE).svc.cluster.local:4317
           - name: OTEL_SERVICE_NAME
             value: 'rl-training-service'
           - name: OTEL_RESOURCE_ATTRIBUTES
             value: service.namespace=opentelemetry-demo
         




Now that the application is instrumented, and the managed collector is enabled and configured, when the application runs on the GKE cluster, metrics and traces are sent to Google Cloud Observability.

You can view this telemetry data in Monitoring and Trace.

## View metrics in Monitoring

Once your RL application is running on GKE with Managed OpenTelemetry enabled, metrics are sent to Monitoring. The metrics are typically available under the `prometheus.googleapis.com/` domain.

To view your custom RL metrics in Monitoring, do the following:

  1. To view the RL metrics in a dashboard, you can do one of the following:

     * In the Google Cloud console, open **Metrics Explorer** in the Google Cloud console:

[Go to the Metrics Explorer page](https://console.cloud.google.com/monitoring/metrics-explorer)

     * Use the [RL workload performance dashboard](https://console.cloud.google.com/monitoring/dashboards/integration/reinforcement-learning.rl-workload-performance).

  2. In the **Metric** field of the dashboard, search for metrics starting with `prometheus.googleapis.com/`. The metrics that are available correspond to the metrics that you instrumented in the application. Examples of these metrics could include:

     * `prometheus.googleapis.com/rl_loop_duration_histogram/`
     * `prometheus.googleapis.com/rl_sample_samples_total/`
     * `prometheus.googleapis.com/rl_environment_reward_mean_total/`
  3. **Filtering and Grouping:** You can use the filters in Metrics Explorer to leverage the semantic conventions you added as attributes. For example, the following specifies the loop duration for a specific run and algorithm:

     * Filter: `metric.label."rl_run_id" == "run-42"`
     * Filter: `metric.label."rl_algorithm" == "PPO"`
     * Group By: `metric.label."rl_environment_name"` to compare performance across environments.



## View traces in Trace

Distributed traces provide a timeline of operations and help you debug the flow of execution within your RL system.

  1. In the Google Cloud console, open **Trace Explorer** in the Google Cloud console:

[Go to the Trace Explorer page](https://console.cloud.google.com/traces/explorer)

  2. You can query and filter traces. Since you set `"service.name": "rl-training-service"` as a resource attribute, you can filter traces by `resource.labels.service_name="rl-training-service"`.

Individual spans within a trace represent different parts of your RL workload. These spans could include calls to external services or different phases of the RL loop, depending on how you instrumented tracing in the application.




## RL semantic conventions and golden signals

This section lists OpenTelemetry metrics that can help you identify issues that occur as the RL application runs on GKE.

Use the information in this section to do the following:

  * Decide which metrics and traces to collect for your application.
  * Decide how to view and use the metrics and trace data collected from your application.



To effectively monitor RL workloads using OpenTelemetry, it's helpful to focus on "golden signals." Golden signals are the four key metrics of a service that provide a high-level overview of its health: _Latency_ , _Traffic_ , _Errors_ , and _Saturation_. By instrumenting your RL application with these metrics, you can quickly understand and debug performance issues.

The following sections have the semantic conventions and metric names categorized by the golden signals they represent in an RL context.

### RL semantic conventions

The follow are attributes on your metrics. These attributes provide context for filtering and analysis in Monitoring.

  * `RL_SYSTEM` = "rl.system": The name of the RL system or framework (for example, "MyCustomRL").
  * `RL_SYSTEM_VERSION` = "rl.system.version": Version of the RL system.
  * `RL_RUN_ID` = "rl.run.id": Unique identifier for a specific training run.
  * `RL_ALGORITHM` = "rl.algorithm": The RL algorithm being used (for example, "PPO", "DQN").
  * `RL_ENVIRONMENT_NAME` = "rl.environment.name": The name of the RL environment (for example, "CartPole-v1").
  * `RL_MODEL_NAME` = "rl.model.name": The name or identifier of the policy/value model.
  * `RL_LOOP` = "rl.loop": Identifier for the main training loop.
  * `RL_LOOP_ITERATION` = "rl.loop.iteration": Current iteration number of the RL loop.
  * `RL_SAMPLE` = "rl.sample": Context for the sampling phase.
  * `RL_SAMPLE_EPISODES` = "rl.sample.episodes": Number of episodes sampled.
  * `RL_SAMPLE_STEPS` = "rl.sample.steps": Number of steps sampled.
  * `RL_SAMPLE_BATCH_SIZE` = "rl.sample.batch_size": Batch size used during sampling.
  * `RL_REWARD` = "rl.reward": Context for reward calculation.
  * `RL_REWARD_BATCH_SIZE` = "rl.reward.batch_size": Batch size for reward calculation.
  * `RL_REWARD_SANDBOX` = "rl.reward.sandbox": Identifier for the reward calculation sandbox.
  * `RL_TRAIN` = "rl.train": Context for the training phase.
  * `RL_TRAIN_STEPS` = "rl.train.steps": Number of training steps.
  * `RL_TRAIN_BATCH_SIZE` = "rl.train.batch_size": Batch size used during training.
  * `RL_TRAIN_TOKENS` = "rl.train.tokens": Number of tokens processed during training.
  * `RL_SYNC` = "rl.sync": Context for synchronization operations.
  * `RL_SYNC_BYTES` = "rl.sync.bytes": Bytes transferred during synchronization.
  * `RL_SYNC_SOURCE` = "rl.sync.source": Source of the synchronization.
  * `RL_SYNC_DESTINATION` = "rl.sync.destination": Destination of the synchronization.



### Golden signals and RL metrics

The following sections lists RL metrics that are related to the four golden signals: _Latency_ , _Traffic_ , _Errors_ , and _Saturation_.

For details about golden signals, see [The Four Golden Signals](https://sre.google/sre-book/monitoring-distributed-systems/#xref_monitoring_golden-signals) in Chapter 6 of the Google Site Reliability Engineering (SRE) book.

#### Latency

How long does it take to complete key operations? High latency can indicate delays when completing key operations. The following metrics can help you identify any latency problems that occur as your RL application runs on GKE.

  * `rl.loop.duration` (Histogram): high loop duration slows down the entire training process. Monitoring this helps identify performance regressions in any part of the RL cycle.
  * `rl.sample.duration` (Histogram): slow sampling directly impacts how quickly new data is generated for training.
  * `rl.reward.duration` (Histogram): reward calculation can be complex; tracking its latency helps optimize this critical step.
  * `rl.train.duration` (Histogram): training time is crucial for iteration speed. Spikes here can point to issues in the training algorithm or hardware.
  * `rl.sync.duration` (Histogram): efficient synchronization is vital in distributed RL. Long sync times can cause stale data and slow down learning.
  * `rl.step.duration` (Histogram): granular latency of individual environment steps.



#### Traffic and throughput

How much work is being done? Low throughput can mean inefficient resource usage. The following metrics can help you identify any issues with traffic or throughput that occur as your RL application runs on GKE.

  * `rl.sample.samples` (Counter): represents the volume of experience data collected. A drop indicates issues in the sampling process.
  * `rl.sample.episodes` (Counter): tracks the number of complete episodes run.
  * `rl.train.steps` (Counter): measures the training progress in terms of optimization steps.
  * `rl.train.tokens` (Counter): tracks the total tokens processed. This metric is relevant for large model RL.
  * `rl.tokens.rate` / `rl.tokens.rate_per_gpu` (Gauge/Rate): Direct measures of training speed and efficiency, especially in token-based models.
  * `rl.samples.rate` / `rl.samples.rate_per_gpu` (Gauge/Rate): Measures how quickly the system is collecting new samples.



#### Errors

Are there any performance or running errors? In RL, "errors" can manifest as unexpected behavior or poor performance. The following metrics can help you identify any errors that occur as your RL application runs on GKE.

  * `rl.environment.reward.mean` (Gauge): while not a traditional error, a _dramatic drop_ in mean reward is a critical signal that something is wrong with the agent or environment interaction. This metric directly reflects learning progress and agent performance.
  * `rl.environment.episode.length.mean` (Gauge): similar to reward, unexpected changes in episode length can signal problems.
  * `rl.train.loss` (Gauge): a sudden _increase_ or erratic behavior in training loss indicates that the model is not learning effectively. Fundamental indicator of training stability and success.



#### Saturation

Is the system overloaded? High saturation can lead to performance degradation. The following metric can help you identify any issues with saturation that occur as your RL application runs on GKE.

  * `rl.train.mfu` (Gauge): model Flop Utilization (MFU). Indicates how effectively compute resources (such as GPUs or TPUs) are being used during training. Low MFU suggests underutilization or bottlenecks.



## What's next

  * Learn more about [Managed OpenTelemetry for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke).
  * [Fine-tune and scale reinforcement learning with verl on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scaling-rl-verl-gke).
  * Learn more about [Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
