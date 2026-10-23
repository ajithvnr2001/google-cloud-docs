---
url: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/sdk/
title: Get started with the ML Diagnostics SDK \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:19.963800+00:00
---

# Get started with the ML Diagnostics SDK  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get started with the ML Diagnostics SDK

The ML Diagnostics Python SDK can be integrated with ML workloads to monitor workloads, collect and manage model metrics, configs, and profiles on Google Cloud. Use the SDK for programmatic profiling and to view model metrics. Model metrics are not available if you use [on-demand profiling](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/cli) without the SDK.

This guide shows you how to create machine learning runs, monitor workloads, collect and manage workload metrics and configs, deploy managed [XProf](https://openxla.org/xprof) resources, and enable programmatic and on-demand profile capture.

In order to have workload monitoring, metrics and config collection, and enable profiling, use an SDK version at least as recent as 1.0.6.

For more information on using the ML Diagnostics SDK, see the [google-cloud-mldiagnostics repository](https://github.com/AI-Hypercomputer/google-cloud-mldiagnostics).

## Install ML Diagnostics SDK

Install the `google-cloud-mldiagnostics` [library](https://pypi.org/project/google-cloud-mldiagnostics/#description):
    
    
    pip install google-cloud-mldiagnostics
    

Import the following packages in your ML workload code:
    
    
    from google_cloud_mldiagnostics import machinelearning_run
    from google_cloud_mldiagnostics import metrics
    from google_cloud_mldiagnostics import xprof
    

## Enable Cloud Logging

The SDK uses the standard Python `logging` module to output metrics and config information. To route these logs to Cloud Logging, install and configure the `google-cloud-logging` library. This lets you view SDK logs, logged metrics, and your own application logs within the Google Cloud console.

Install the `google-cloud-logging` library:
    
    
    pip install google-cloud-logging
    

Configure logging in your script by attaching the Cloud Logging handler to the Python root logger. Add the following lines to the beginning of your Python script:
    
    
      import logging
      import google.cloud.logging
    
      # Instantiate a Cloud Logging client
      logging_client = google.cloud.logging.[Client](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html)()
    
      # Attach the Cloud Logging handler to the Python root logger
      logging_client.[setup_logging](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html#google_cloud_logging_v2_client_Client_setup_logging)()
    
      # Standard logging calls will go to Cloud Logging
      logging.info("SDK logs and application logs will appear in Cloud Logging.")
    

## Enable detailed logging

By default, the logging level is set to `INFO`. To receive more detailed logs from the SDK, such as machine learning run details, set the logging level to `DEBUG` after calling `setup_logging()`:
    
    
    import logging
    import google.cloud.logging
    
    logging_client = google.cloud.logging.[Client](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html)()
    logging_client.[setup_logging](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html#google_cloud_logging_v2_client_Client_setup_logging)()
    logging.getLogger().setLevel(logging.DEBUG) # Enable DEBUG level logs
    
    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    

With `DEBUG` enabled, you receive additional SDK diagnostics in Cloud Logging. For example:
    
    
    DEBUG:google_cloud_mldiagnostics.core.global_manager:current run details:
    {'name': 'projects/my-gcp-project/locations/us-central1/mlRuns/my-run-12345',
    'gcs_path': 'gs://my-bucket/profiles', ...}
    

## Create a machine learning run

To use the ML Diagnostics platform, you need to first create a machine learning run. This involves instrumenting your ML workload with the SDK to perform logging, collect metrics, and enable profile tracing.

The following is a basic example that initializes Cloud Logging, creates a machine learning run (`MLRun`), records metrics, and captures a profile:
    
    
    import logging
    import os
    import google.cloud.logging
    from google_cloud_mldiagnostics import machinelearning_run, metrics, xprof, metric_types
    
    # 1. Set up Cloud Logging
    # Make sure to pip install google-cloud-logging
    logging_client = google.cloud.logging.[Client](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html)()
    logging_client.[setup_logging](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html#google_cloud_logging_v2_client_Client_setup_logging)()
    # Optional: Set logging level to DEBUG for more detailed SDK logs
    logging.getLogger().setLevel(logging.DEBUG)
    
    # 2. Define and start machinelearning run
    try:
        run = machinelearning_run(
              name="<run_name>",
              run_group="<run_group>",
              configs={ "epochs": 100, "batch_size": 32 },
              project="<some_project>",
              region="<some_zone>",
              gcs_path="gs://<some_bucket>",
              on_demand_xprof=True,
            )
        logging.info(f"MLRun created: {run.name}")
    
        # 3. Collect metrics during your run
        metrics.record(metric_types.MetricType.LOSS, 0.123, step=1)
        logging.info("Loss metric recorded.")
    
        # 4. Capture profiles programmatically
        with xprof():
            # ... your code to profile here ...
            pass
        logging.info("Profile captured.")
    
    except Exception as e:
        logging.error(f"Error during MLRun: {e}", exc_info=True)
    

The code example uses the following variables:

Variable | Requirement | Description  
---|---|---  
`name` | Required | An identifier for the specific run. The SDK automatically creates a `machine-learning-run-id` to ensure that run names are unique.  
`run_group` | Optional | An identifier that can help group multiple runs belonging to the same experiment. For example, all runs associated with a TPU slice size sweep could belong to the same group.  
`project` | Optional | If not specified, the project is extracted from Google Cloud CLI.  
`region` | Required | All [Cluster Director locations](https://docs.cloud.google.com/cluster-director/docs/locations) are supported except `us-east5`. This flag can be set by an argument for each command, or with the command: `gcloud config set compute/region`.  
`configs` | Optional | Key-value pairs containing configuration parameters for the run. If configs are not defined, default software and system configs appear but the ML workload configs do not.  
`gcs_path` | Conditionally Required | The Google Cloud Storage location where all profiles are saved. For example: `gs://my-bucket` or `gs://my-bucket/folder1`. Required only if the SDK is used for profile capture.   
`on-demand-xprof` | Optional | Starts `xprofz daemon` on port `9999` to enable on-demand profiling. You can enable both on-demand profiling and programmatic profiling in the same code, as long as they don't occur at the same time.  
  
The following configs are automatically collected by the SDK and don't need to be specified within `machinelearning_run`:

  * **Software configs** : Framework, framework version, XLA flags.
  * **System configs** : Device type, number of slices, slice size, number of hosts.



Project and region information is stored as machine learning run metadata. The region used for the machine learning run does not have to match the region used for the workload run.

## Write configs

Many workloads contain too many configs to define directly in the `machinelearning_run` definition. In these cases, you can write configs to your run using JSON or YAML.
    
    
    import yaml
    import json
    
    # Read the YAML file
    with open('config.yaml', 'r') as yaml_file:
      # Parse YAML into a Python dictionary
      yaml_data = yaml.safe_load(yaml_file)
    
    # Define machinelearning run
    machinelearning_run(
      name="RUN_NAME",
      run_group="GROUP_NAME",
      configs=yaml_data,
      project="PROJECT_NAME",
      region="ZONE",
      gcs_path="gs://BUCKET_NAME",
    )
    

## Collect metrics

You can collect model metrics, model performance metrics, and system metrics with the SDK. You can create visualizations of these metrics as average values and with time series charts.

The SDK provides two functions for recording metrics: `metrics.record()` for capturing individual data points, and `metrics.record_metrics()` for recording multiple metrics in a single batch. Both functions write metrics to Cloud Logging, enabling visualization and analysis.

To record a single metric:
    
    
    # Record a metric only with time as the x-axis
    metrics.record(metric_types.MetricType.LOSS, 0.123)
    
    # Record a metric with time and step as the x-axis
    metrics.record(metric_types.MetricType.LOSS, 0.123, step=1)
    

To record multiple metrics:
    
    
    from google_cloud_mldiagnostics import metric_types
    # User codes
    # machinelearning_run should be called
    # ......
    
    for step in range(num_steps):
      if (step + 1) % 10 == 0:
        metrics.record_metrics([
            # Model quality metrics
            {"metric_name": metric_types.MetricType.LEARNING_RATE, "value": step_size},
            {"metric_name": metric_types.MetricType.LOSS, "value": loss},
            {"metric_name": metric_types.MetricType.GRADIENT_NORM, "value": gradient},
            {"metric_name": metric_types.MetricType.TOTAL_WEIGHTS, "value": total_weights},
            # Model performance metrics
            {"metric_name": metric_types.MetricType.STEP_TIME, "value": step_time},
            {"metric_name": metric_types.MetricType.THROUGHPUT, "value": throughput},
            {"metric_name": metric_types.MetricType.LATENCY, "value": latency},
            {"metric_name": metric_types.MetricType.TFLOPS, "value": tflops},
            {"metric_name": metric_types.MetricType.MFU, "value": mfu},
        ], step=step+1)
    

The following system metrics are automatically collected by the SDK from libTPU, `psutil`, and JAX libraries:

  * TPU TensorCore utilization
  * TPU duty cycle
  * HBM utilization
  * Host CPU utilization
  * Host memory utilization



You don't need to manually specify these metrics. These system metrics have _time_ as the default x-axis.

The following predefined metric keys will automatically appear in the Google Cloud console if assigned. These metrics aren't calculated automatically; they are predefined keys that you can assign values to.

  * **Model quality metric keys** : `LEARNING_RATE`, `LOSS`, `GRADIENT_NORM`, `TOTAL_WEIGHTS`.
  * **Model performance metric keys** : `STEP_TIME`, `THROUGHPUT`, `LATENCY`, `MFU`, `TFLOPS`.



The predefined metrics, as well as other user-defined metrics can be recorded with x-axis as `time`, or both `time` and `step`. You can record any custom metric in the workload.

The following example captures a single metric for the workload, which you can view in the **Model Metrics** tab for the specific machine learning run:
    
    
    metrics.record("custom_metrics_1", step_size, step=step + 1)
    

To record multiple metrics in one call, use the `record_metrics` method. For example:
    
    
    metrics.record_metrics([
            # Model quality metrics
            {"metric_name": metric_types.MetricType.LEARNING_RATE, "value": step_size},
            {"metric_name": metric_types.MetricType.LOSS, "value": loss},
            {"metric_name": metric_types.MetricType.GRADIENT_NORM, "value": gradient},
            {"metric_name": metric_types.MetricType.TOTAL_WEIGHTS, "value": total_weights},
            # Model performance metrics
            {"metric_name": metric_types.MetricType.STEP_TIME, "value": step_time},
            {"metric_name": metric_types.MetricType.THROUGHPUT, "value": throughput},
            {"metric_name": metric_types.MetricType.LATENCY, "value": latency},
            {"metric_name": metric_types.MetricType.TFLOPS, "value": tflops},
            {"metric_name": metric_types.MetricType.MFU, "value": mfu},
         # Custom metrics
         {"custom_metrics_1", "value":<value>},
         {"custom_metrics_2", "value":<value>},
         {"avg_mtp_acceptance_rate_percent", "value":<value>},
         {"dpo_reward_accuracy", "value":<value>},
        ], step=step+1)
    

### System metrics

You can automatically collect system metrics at either the default 1-minute interval or a more fine-grained interval.

#### Default interval

Collect system metrics automatically with 1-minute interval from Cloud Monitoring by setting `log_system_metrics=false`. See [Monitor workloads](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/workload-monitoring) for details on system metrics that are automatically collected with this default.

The following is an example of how to receive default system metrics from Cloud Monitoring:
    
    
    machinelearning_run(
          name="my-run-123",
          run_group="my-group",
          project="gcp-project",
          region="us-central1",
          gcs_path="gs://my_bucket_path",
          on_demand_xprof=True,
          log_system_metrics=False
      )
    

#### Fine-grain interval

Collect system metrics automatically with fine-grained interval (10 seconds) by setting `log_system_metrics=true`. With this option, the following system metrics are automatically collected by the SDK from libTPU, `psutil`, and JAX libraries:

  * TPU TensorCore utilization
  * TPU duty cycle
  * HBM utilization
  * Host CPU utilization
  * Host memory utilization



The following is an example of how to collect fine-grain system metrics:
    
    
    machinelearning_run(
          name="my-run-123",
          run_group="my-group",
          project="gcp-project",
          region="us-central1",
          gcs_path="gs://my_bucket_path",
          on_demand_xprof=True,
          log_system_metrics=True
      )
    

These system metrics have _time_ as the default x-axis.

## Capture profiles

You can capture [XProf](https://openxla.org/xprof) profiles of your ML workload with programmatic capture or on-demand capture (manual capture). Programmatic capture involves embedding profiling commands directly into your machine learning code, and explicitly stating when to start and stop recording data. On-demand capture occurs in real-time, where you trigger the profiler while the workload is already actively running.

The SDK commands to capture profiles are framework-agnostic since all framework-level profiling commands are automatically integrated into ML Diagnostics profiling commands. This means that your profiling code is not dependent on the framework you use.

### Programmatic profile capture

Programmatic capture requires you to annotate your model code and specify where you want to capture profiles. Typically, you capture a profile for a few training steps, or profile a specific block of code within your model.

You can perform programmatic profile capture with the ML Diagnostics SDK in the following ways:

  * **API-based collection** : Control profiling with `start()` and `stop()` methods.
  * **Decorator-based collection** : Annotate functions with `@xprof(run)` for automatic profiling.
  * **Context manager** : Use with `xprof()` for scope-based profiling that automatically handles `start()` and `stop()` operations.



You can use the same profile capture code across all frameworks. All the profile sessions are captured in the Cloud Storage bucket defined in the machine learning run.
    
    
    # Support collection via APIs
    prof = xprof()  # Updates metadata and starts xprofz collector
    prof.start()  # Collects traces to bucket
    # ..... Your code execution here
    # ....
    prof.stop()
    
    # Also supports collection via decorators
    @xprof()
    def abc(self):
        # does something
        pass
    
    # Use xprof as a context manager to automatically start and stop collection
    with xprof() as prof:
        # Your training or execution code here
        train_model()
        evaluate_model()
    

### Multi-host (process) profiling

During programmatic profiling, the SDK starts profiling on each host (process) where ML workload code is executing. If the list of nodes is not provided, all hosts are included.
    
    
    # starts profiling on all nodes
    prof = xprof()
    prof.start()
    # ...
    prof.stop()
    

By default, calling the `prof.start()` method without the `session_id` argument on multiple hosts results in separate trace sessions - one for each host. To group traces from different hosts into a single, unified multi-host session in XProf, ensure that the `prof.start()` method is called with the _same_ `session_id` argument on all participating hosts. For example:
    
    
    # Use the same session_id on all hosts to group traces
    prof = xprof()
    prof.start(session_id="profiling_session")
    # ...
    prof.stop()
    

To enable profiling for specific hosts:
    
    
    # starts profiling on node with index 0 and 2
    prof = xprof(process_index_list=[0,2])
    prof.start()
    # ...
    prof.stop()
    

### On-demand profile capture

Use on-demand profile capture when you want to capture profiles in an ad hoc manner, or when programmatic profile capture is not already enabled. On-demand capture is helpful when there are problems with model performance during the run, and you want to capture profiles in those moments to diagnose the issues.

To enable on-demand profile capture, configure the run with on-demand support:
    
    
    # Define machinelearning run
    machinelearning_run(
        name="<run_name>",
        # specify where profiling data is stored
        gcs_path="gs://<bucket>",
        ...
        # enable on demand profiling, starts xprofz daemon on port 9999
        on_demand_xprof=True
    )
    

You can use the same profile capture code across all frameworks. All profile sessions are captured in the Cloud Storage bucket defined in the machine learning run.

For on-demand profiling on GKE, deploy GKE `connection-operator` and `injection-webhook` into the GKE cluster. This ensures that your machine learning run can locate the GKE nodes it is running on, and the on-demand capture drop-down can autopopulate those nodes. For more information, see [Configure GKE cluster](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/gke).

## Package workload for GKE

You can use a Dockerfile to package an application that uses the ML Diagnostics SDK. Install the `google-cloud-logging` package for Cloud Logging integration. For example:
    
    
    # Base image (user's choice, e.g., python:3.10-slim, or a base with ML frameworks)
    FROM python:3.11-slim
    
    # Install base utilities
    RUN pip install --no-cache-dir --upgrade pip
    
    # Install SDK and Logging client
    # psutil is installed as a dependency of google-cloud-mldiagnostics
    RUN pip install --no-cache-dir \
        google-cloud-mldiagnostics \
        google-cloud-logging
    
    # Optional: For JAX/TPU workloads
    # RUN pip install --no-cache-dir "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html &&
    #     pip install --no-cache-dir libtpu xprof
    
    # Add your application code
    COPY ./app /app
    WORKDIR /app
    
    # Run your script
    CMD ["python", "your_train_script.py"]
    

## Deploy workload

After integrating the SDK with your workload, package the workload in an image and create your YAML file with the specified image. For programmatic profiling, label the workload in the YAML file with `managed-mldiagnostics-gke=true`. On-demand profiling does not require this label.

For GKE:
    
    
    kubectl apply -f YAML_FILE_NAME
    

For Compute Engine, connect to the VM using SSH and run the Python code for your workload:
    
    
    source venv/bin/activate
    python3.11 WORKLOAD_FILE_NAME
    

After deploying the workload, find your job name by searching for your workload namespace:
    
    
    kubectl get job -n YOUR_NAMESPACE
    

You can find the run name and link in your `kubectl` logs by passing the job name and namespace. You must specify the workload container (for example: `-c workload`) because the ML Diagnostics sidecar handles its own logging.
    
    
    kubectl logs jobs/s5-tpu-slice-0 -n YOUR_NAMESPACE -c workload
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
