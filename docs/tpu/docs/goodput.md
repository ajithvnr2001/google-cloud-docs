---
url: https://docs.cloud.google.com/tpu/docs/goodput/
title: Monitor goodput with the ML Goodput Measurement library \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:22.056324+00:00
---

# Monitor goodput with the ML Goodput Measurement library  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/goodput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor goodput with the ML Goodput Measurement library

The ML Goodput Measurement library ([ml-goodput-measurement](https://pypi.org/project/ml-goodput-measurement/)) is a Python package that helps you measure the efficiency of your ML training workloads running on Cloud TPU VMs. The library provides metrics that measure workload goodput, which is the proportion of TPU usage time spent making productive, preserved training progress. Conversely, badput is the proportion of total time spent on non-productive activities like startup overhead, I/O stalls, and disruption recovery.

You can visualize goodput metrics in realtime with [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) dashboards and [TensorBoard](https://www.tensorflow.org/tensorboard), enabling you to pinpoint bottlenecks, optimize resource utilization, and ultimately reduce training costs.

For more information, see the [ML Goodput Measurement GitHub repository](https://github.com/AI-Hypercomputer/ml-goodput-measurement).

## Goodput metrics

The ML Goodput Measurement library provides the following metrics, which are also available to view in Cloud Monitoring and TensorBoard. The metrics in this table must be prefixed with `compute.googleapis.com/workload/`. For example, the full metric name for `goodput_time` is `compute.googleapis.com/workload/goodput_time`.

  * `goodput_time`: The total productive training time in seconds. This can be interpreted as the cumulative goodput.

  * `badput_time`: The total unproductive training time in seconds (startup, stalls, recovery). This can be interpreted as the cumulative badput.

  * `total_elapsed_time`: The total elapsed time (wall-clock duration) of the workload in seconds. The elapsed time is measured from the time the application starts to either the current time or the time of job completion.

  * `interval_goodput`: The goodput rate over a specified time period (for example, the last 24 hours). The metric provides a rolling window for goodput.

  * `interval_badput`: The badput rate over a specified time period. The metric provides a rolling window for badput, and is useful for identifying transient issues like spikes in I/O operations.

  * `disruptions`: The cumulative count of job disruptions. Disruptions are events that cause the training process to stop unexpectedly, requiring a restart. For example, hardware failures and maintenance events.

  * `step_time_deviation`: The amount of unproductive time due to variation in training step times. This is also known as "jitter". The metric measures spike-sensitive stability, which is the deviation of recent "worst-case" steps against a historical baseline in seconds. A step is a single iteration of the training loop.

  * `performance`: The estimated fastest stable step time (baseline) in seconds. The ideal step time is the fastest time a single training step can take under optimal conditions, free from transient noise or jitter.

  * `max_productive_steps`: The highest step count reached that was successfully preserved.




## Installation

Use the following steps to set up the ML Goodput Measurement library with your TPU workloads:

  1. Enable the [Cloud Logging](https://cloud.google.com/logging) API and [ Cloud Monitoring](https://cloud.google.com/monitoring) API.
  2. If deploying on Google Kubernetes Engine (GKE), configure all node pools with the `cloud-platform` access scope.



Install the `ml-goodput-measurement` package on your training host and analysis machine:
    
    
    pip install ml-goodput-measurement
    

## Monitor with the Goodput library

To use the ML Goodput Measurement library, initialize a `GoodputRecorder` instance, instrument your training code by wrapping key sections with the `record_event` context manager, and monitor metrics in realtime with `GoodputMonitor`. The monitor runs a background process to periodically calculate goodput metrics from the recorded events, and uploads them to Cloud Monitoring and TensorBoard for real-time analysis and visualization.

### Initialize the Goodput recorder

Initialize the `GoodputRecorder`, which is the core component of the ML Goodput Measurement library.
    
    
    import datetime
    import jax
    from ml_goodput_measurement import measurement
    
    # Define a unique logger name for this specific run
    logger_name = f'goodput_{config.run_name}'
    
    # Instantiate the recorder
    goodput_recorder = measurement.GoodputRecorder(
        job_name=config.run_name,
        logger_name=logger_name,
        logging_enabled=(jax.process_index() == 0)
    )
    

### Record events

Use the `record_event` context manager to wrap your training code.
    
    
    def train_loop(config):
    
      # 1. Wrap the entire Job (Start/End)
      with goodput_recorder.record_event(measurement.Event.JOB):
    
        # 2. Record Hardware Initialization
        with goodput_recorder.record_event(measurement.Event.ACCELERATOR_INIT):
          # ... perform device mesh setup ...
          initialize_tpu(config)
    
        # 3. Record Training Prep
        with goodput_recorder.record_event(measurement.Event.TRAINING_PREP):
          # ... create checkpoint managers, setup model ...
          model = training_prep(config)
    
        # 4. Main Training Loop
        for step in range(config.steps):
    
          # Record Data Loading
          with goodput_recorder.record_event(measurement.Event.DATA_LOADING):
            batch = get_next_batch()
    
          # Record Step Start (CRITICAL: Pass the step number!)
          with goodput_recorder.record_event(measurement.Event.STEP, step):
            output = train_step(model, batch)
    
          # 5. Record Custom Events (e.g., Evaluation)
          if step % eval_interval == 0:
            with goodput_recorder.record_event(measurement.Event.CUSTOM, "eval_step"):
              run_evaluation()
    

For an example of how training code can be integrated with the Goodput library using MaxText, see [goodput.py](https://github.com/AI-Hypercomputer/maxtext/blob/main/src/maxtext/common/goodput.py).

### Monitor events

Monitor metrics with `GoodputMonitor`, which starts a background process to calculate and upload metrics while the job runs. Wrap the logic in a context manager to ensure that the uploader process starts and stops as intended.

Define a helper context manager to handle configuration and lifecycle management.
    
    
    import contextlib
    from ml_goodput_measurement import monitoring
    
    @contextlib.contextmanager
    def maybe_monitor_goodput(config):
      """Monitor goodput if enabled and on the main process."""
      if not config.monitor_goodput or jax.process_index() != 0:
        yield
        return
    
      goodput_monitor = None
      try:
        # Configure GCPOptions for Cloud Monitoring
        gcp_options = monitoring.GCPOptions(
          enable_gcp_goodput_metrics=config.enable_gcp_goodput_metrics
        )
    
        # Instantiate the monitor
        goodput_monitor = monitoring.GoodputMonitor(
          job_name=config.run_name,
          logger_name=f"goodput_{config.run_name}",
          tensorboard_dir=config.tensorboard_dir,
          upload_interval=config.goodput_upload_interval_seconds,
          monitoring_enabled=True,
          pathway_enabled=config.enable_pathways_goodput,
          include_badput_breakdown=True,
          gcp_options=gcp_options,
        )
    
        # Start the background upload process
        goodput_monitor.start_goodput_uploader()
        print("Started Goodput upload to Tensorboard & GCM in the background!")
        yield
    
      finally:
        # Ensure clean shutdown of the background process
        if goodput_monitor:
          goodput_monitor.stop_goodput_uploader()
          print("Flushed final metrics and safe exited from Goodput monitoring.")
    

To measure rolling window performance, configure the monitor to use `start_rolling_window_goodput_uploader` and `stop_rolling_window_goodput_uploader`.
    
    
    try:
        self._rolling_window_monitor.start_rolling_window_goodput_uploader(
            self.config.rolling_window_size
        )
    finally:
        if self._rolling_window_monitor:
            self._rolling_window_monitor.stop_rolling_window_goodput_uploader()
    

Wrap your main training entry point with the context manager. This ensures that monitoring starts before training begins, and final metrics are cleared when training ends.
    
    
    def main():
      # ... Load configuration ...
    
      # Wrap the entire execution
      with maybe_monitor_goodput(config):
        # Run the training loop (which contains the GoodputRecorder events)
        train_loop(config)
    

### Post-processing and analysis

You can calculate goodput metrics for a completed job from any machine, like a standard CPU VM or your laptop. You don't need to use a TPU for post-processing and analysis.

The following code outputs the total job goodput:
    
    
    from ml_goodput_measurement import goodput
    
    calculator = goodput.GoodputCalculator(
        job_name="my-run-name",
        logger_name="goodput_my-run-name"
    )
    
    goodput, badput, last_step = calculator.get_job_goodput(
        include_badput_breakdown=True
    )
    
    print(f"Goodput: {goodput}%")
    print(f"Badput (Infra Recovery): {badput[goodput.BadputType.INFRASTRUCTURE_RECOVERY_FROM_DISRUPTION]}%")
    

For information on badput types (`BadputType`), see [Badput breakdown details](https://github.com/AI-Hypercomputer/ml-goodput-measurement#badput-breakdown-details).

To specify a specific time window, use `get_job_goodput_interval`:
    
    
    goodput_pct, badput, _, _, _ = calculator.get_job_goodput_interval(
        start_time_utc,
        end_time_utc
    )
    

The start time (`start_time_utc`) and end time (`end_time_utc`) are [datetime](https://docs.python.org/3/library/datetime.html) objects. For more information, see [goodput.py](https://github.com/AI-Hypercomputer/ml-goodput-measurement/blob/main/ml_goodput_measurement/src/goodput.py#L1448).

## Monitor with Goodput dashboards

To help you monitor and visualize your Machine Learning training workloads, Google Cloud offers two sets of Goodput dashboards: the GKE JobSet Goodput dashboard and the Cloud ML Goodput dashboard. Use the GKE JobSet dashboard to diagnose infrastructure or scheduling issues, and the Cloud ML Goodput dashboards to pinpoint bottlenecks within the training code.

### Google Cloud ML Goodput dashboard

The ML Goodput dashboard measures the application-level efficiency of your training script. It provides insights into time spent on productive training, and badput sources like data loading, initialization, or recovering from disruptions.

To view the ML Goodput dashboard dashboard in Cloud Monitoring:

  1. In the Google Cloud console, go to the Cloud Monitoring page.   
[Go to the Monitoring console](https://console.cloud.google.com/monitoring)
  2. In the navigation pane, click **Dashboards**.
  3. In the **Filter search** field, enter "Cloud ML Goodput Dashboard".



The ML Goodput dashboard includes the following metrics (prefixed with `workload/`):

  * `goodput_time`: Cumulative time spent on productive training steps.
  * `badput_time`: Cumulative time spent on non-productive activities, along with the badput source: 
    * `ACCELERATOR_INITIALIZATION`: Time to set up TPUs.
    * `TRAINING_PREP`: Checkpoint loading, model and optimizer creation.
    * `PROGRAM_STARTUP`: JIT compilation, graph tracing.
    * `DATA_LOADING_SYNC`: Time spent blocked on data input.
    * `CHECKPOINT_SAVE`: Time for saving model state.
    * `CHECKPOINT_RESTORE`: Time for restoring model state.
    * `WASTED_PROGRESS`: Productive time lost due to disruptions occurring before a checkpoint.
    * `INFRASTRUCTURE_RECOVERY`: Downtime during job restarts.
    * `CUSTOM_BADPUT_EVENTS`: User-defined synchronous events like evaluations.
  * `step_time_deviation`: Measures the jitter and instability in training step times.
  * `interval_goodput`: Goodput calculated over rolling windows (e.g., last hour).



### GKE JobSet dashboard

The GKE JobSet Goodput dashboard focuses on the efficiency of the orchestration layer, and helps you understand if GKE is scheduling pods quickly and keeping them running.

To view comprehensive information about the health and performance of JobSets, go to the **JobSet monitoring** dashboard in the Google Cloud console:

[Go to JobSet monitoring dashboard](https://console.cloud.google.com/kubernetes/aiml/jobs)

The JobSet monitoring dashboard includes the following metrics:

  * `kubernetes.io/jobset/scheduling_goodput`: The fraction of time that all required resources (pods) for the JobSet are in a ready state and available to do work, relative to the JobSet's creation time. Low values indicate delays in pod scheduling, image pulling, or resource allocation within GKE.

  * `kubernetes.io/jobset/proxy_runtime_goodput`: An estimated fraction of time that the TPUs are actively being used, based on system-level signals like accelerator duty cycle. This provides a high-level view of runtime productivity without application instrumentation.

  * [Node pool metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#metrics): Information about the health, availability, and interruptions affecting the node pools hosting the JobSet. This helps correlate goodput dips with underlying node issues.




For more information on the GKE JobSet dashboard, see [Monitor JobSet goodput](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/tpu-multislice-kueue#jobset-goodput).

## Troubleshooting guide

This section provides troubleshooting information to help you identify and resolve common problems you might encounter while using the ML Goodput Measurement library.

### Missing Cloud Monitoring metrics

If you are missing Cloud Monitoring metrics:

  * **Verify IAM permissions:** The service account attached to your workload must have the `monitoring.timeSeries.create` and `monitoring.metricDescriptors.create` permissions.
  * **Check configuration:** Goodput metrics must be explicitly enabled in your configuration. For example, verify that `enable_gcp_goodput_metrics=True` is passed within your `GCPOptions`.



### Missing general metrics

If you are missing general metrics:

  * **Verify monitor status:** Monitoring must be enabled for your monitor instantiation. Pass `monitoring_enabled=True` to the monitor.



### Corrupted metrics

If your metrics are corrupted or displaying odd values:

  * **Ensure unique run names:** All `run_name` values must be unique for every experiment. Reusing a run name will mix logs from old and new runs.



### Missing logs

If you are missing logs from Cloud Logging:

  * **Enable the Cloud Logging API:** Cloud Logging API must be enabled in your Google Cloud project.
  * **Check recorder settings:** The `logging_enabled=True` flag must be passed to the Goodput Recorder.
  * **Verify the main process:** The primary process (where `jax.process_index() == 0`) must be actively reporting application logs.



### Missing badput checkpoints

If you are missing badput checkpoints:

  * **Verify your checkpointing library:** The Goodput library automatically tracks checkpointing time for Orbax. However, if you are using other libraries (such as PyTorch checkpointing), you must manually wrap your save and restore calls using `record_custom_badput_event_start_time` and `record_custom_badput_event_end_time`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
