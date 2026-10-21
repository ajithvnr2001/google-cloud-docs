---
url: https://docs.cloud.google.com/tpu/docs/tpu-monitoring-library/
title: TPU Monitoring Library \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:21.382323+00:00
---

# TPU Monitoring Library  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/tpu-monitoring-library/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TPU Monitoring Library

Unlock deep insights into your Cloud TPU hardware's performance and behavior with advanced TPU monitoring capabilities, built directly upon the foundational software layer, LibTPU. While LibTPU encompasses drivers, networking libraries, the XLA compiler, and TPU runtime for interacting with TPUs, the focus of this document is the TPU Monitoring Library.

The TPU Monitoring Library provides:

  * Comprehensive observability: Gain access to the telemetry API and metrics suite, which provides detailed insights into the operational performance and specific behaviors of your TPUs.

  * Diagnostic toolkits: Provides an SDK and command-line interface (CLI) designed to enable debugging and in-depth performance analysis of your TPU resources.




These monitoring features are designed to be a top-level, customer-facing solution, providing you with the essential tools to optimize your TPU workloads effectively across frameworks such as JAX and PyTorch ([TorchTPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu)).

The TPU Monitoring Library gives you detailed information on how machine learning workloads are performing on TPU hardware. It's designed to help you understand your TPU utilization, identify bottlenecks, and debug performance issues. It gives you more detailed information than interruption metrics, goodput metrics, and other metrics.

## Get started with the TPU Monitoring Library

Accessing these insights is straightforward. The TPU monitoring functionality is integrated with the LibTPU SDK, so it is included when you install LibTPU or when you install a framework such as JAX or TorchTPU (`torch_tpu`) that uses LibTPU.

### Install LibTPU
    
    
    pip install libtpu
    

### Install a framework

LibTPU updates are coordinated with framework releases. Choose your framework to install a compatible LibTPU version and its monitoring features:

### JAX

When you install the latest JAX release (released monthly), it pins a compatible LibTPU version and its monitoring features:
    
    
    pip install -U "jax[tpu]"
    

### TorchTPU

For PyTorch workloads, [TorchTPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu) (`torch_tpu`) declares `libtpu` as a package dependency and uses the `libtpu` package installed in your environment. When installed, `torch_tpu` automatically registers the `"tpu"` device backend with PyTorch on `import torch` and configures the LibTPU library path:
    
    
    pip install torch_tpu
    

**Note:** If `libtpu` is already installed and meets the minimum version required by `torch_tpu`, `pip` keeps the existing installation. Otherwise, `pip` upgrades `libtpu`. If you set the `TPU_LIBRARY_PATH` environment variable, that LibTPU library is used instead of the one in the `libtpu` package.**Note:** JAX pins a specific `libtpu` version. If you install `torch_tpu` into the same environment as `jax[tpu]` and the pinned version is older than the minimum required by `torch_tpu`, `pip` replaces it with a newer `libtpu`. To keep each framework on its tested `libtpu` version, use separate virtual environments for JAX and for `torch_tpu`.

### Import the library in Python

To start using the TPU Monitoring Library, import the `tpumonitoring` module in your Python code. This API is identical whether your workload uses JAX or PyTorch (`torch_tpu`).
    
    
    from libtpu.sdk import tpumonitoring
    

## List all supported functionality

List all metric names and the functionality they support:
    
    
    from libtpu.sdk import tpumonitoring
    
    tpumonitoring.help()
    """
    libtpu.sdk.tpumonitoring.help():
          List all supported functionality.
    
      libtpu.sdk.tpumonitoring.list_supported_metrics()
          List supported metric names in the list of str format.
    
      libtpu.sdk.tpumonitoring.get_metric(metric_name:str)
          Get metric data with metric name. It represents the snapshot mode.
          The metric data is a object with `description()` and `data()` methods,
          where the `description()` returns a string describe the format of data
          and data unit, `data()` returns the metric data in the list in str format.
    """
    

## Supported metrics

The following code sample shows how to list all supported metric names:
    
    
    from libtpu.sdk import tpumonitoring
    
    tpumonitoring.list_supported_metrics()
    
    ["duty_cycle_pct", "tensorcore_util", "hbm_util", ...]
    

The following table shows commonly used metrics and their definitions. Call `tpumonitoring.list_supported_metrics()` for the complete list of metrics in your `libtpu` version, and call `get_metric(name).description()` to see the format of each metric.

Metric  | Definition  | Metric name for API  | Example values   
---|---|---|---  
Tensor Core Utilization  | Measures the percentage of your TensorCore usage, calculated as the percentage of operations that are part of the TensorCore operations. Sampled 10 microseconds every 1 second. You cannot modify the sampling rate. This metric lets you monitor the efficiency of your workloads on TPU devices.  |  `tensorcore_util` | `['1.11', '2.22', '3.33', '4.44']`   
  
# utilization percentage for accelerator ID 0-3.   
Duty Cycle Percentage  | Percentage of time over the past sample period (every 5 seconds; can be tuned by setting the `LIBTPU_INIT_ARGS` environment variable) during which the accelerator was actively processing (recorded with cycles used to execute HLO programs over the last sampling period). This metric represents how busy a TPU is. The metric is emitted per chip.  |  `duty_cycle_pct` | `['10.00', '20.00', '30.00', '40.00']`   
  
# Duty cycle percentage for accelerator ID 0-3.   
HBM Capacity Total  | This metric reports the total HBM capacity in bytes.  |  `hbm_capacity_total` | `['30000000000', '30000000000', '30000000000', '30000000000']`   
  
# Total HBM capacity in bytes that attached to accelerator ID 0-3.   
HBM Capacity Usage  | This metric reports the usage of HBM capacity in bytes over the past sample period (every 5 seconds; can be tuned by setting the `LIBTPU_INIT_ARGS` environment variable).  |  `hbm_capacity_usage` | `['100', '200', '300', '400']`   
  
# Capacity usage for HBM in bytes that attached to accelerator ID 0-3.   
Buffer transfer latency  | Network transfer latencies for megascale multislice traffic. This visualization lets you understand the overall network performance environment.  |  `buffer_transfer_latency` | `["'8MB+', '2233.25', '2182.02', '3761.93', '19277.01', '53553.6'"]`   
  
# buffer size, mean, p50, p90, p99, p99.9 of network transfer latency distribution.   
Inbound buffer transfer latency | Measures the time it takes to receive data buffers over the network, measured in microseconds. The metric is useful for detecting network performance problems and potential faulty network hardware. | `inbound_buffer_transfer_latency` | `["'8MB+', '4723.59', '4500.22', '6210.11', '7100.45', '8510.99'"]`   
  
# buffer size, mean, p50, p90, p99, p99.9 of inbound DCN network traffic transfer latency distribution.  
Host compute latency | Measures the time it takes to compute a reduction operation in microseconds. The metric is useful for detecting performance issues and potential CPU or memory hardware faults on individual hosts participating in distributed computations. | `host_compute_latency` | `["'8MB+', '2408.17', '2105.40', '3600.22', '4800.15', '15000.80'"]`   
  
# buffer size, mean, p50, p90, p99, p99.9 of host compute latency distribution.  
High Level Operation Execution Time Distribution Metrics  | Provides granular performance insights into the HLO compiled binary execution status, enabling regression detection and model-level debugging.  |  `hlo_execution_timing` | `["'tensor_core-0', '10.00', '10.00', '20.00', '30.00', '40.00'"]`   
  
# The HLO execution time duration distribution for CoreType-CoreID with mean, p50, p90, p95, p999.   
High Level Optimizer queue size  | HLO execution queue size monitoring tracks the number of compiled HLO programs waiting or undergoing execution. This metric reveals execution pipeline congestion, enabling identification of performance bottlenecks in hardware execution, driver overhead, or resource allocation.  |  `hlo_queue_size` | `["tensor_core-0: 1", "tensor_core-1: 2"]`   
  
# Measures queue size for CoreType-CoreID.   
Collective End to End Latency  |  This metric measures the end-to-end collective latency over DCN in microseconds, from the host initiating the operation to all peers receiving the output. It includes host-side data reduction and sending output to the TPU. Results are strings detailing buffer size, type, and mean, p50, p90, p95, and p99.9 latencies.  |  `collective_e2e_latency` |  `["8MB+-ALL_REDUCE, 1000, 2000, 3000, 4000, 5000", …]`   
  
# Transfer size-collective op, mean, p50, p90, p95, p999 of collective end to end latency.   
Round Trip Latency at Transport Layer  |  Distribution of the minimum Round Trip Times (RTT) observed on TCP connections used by gRPC for multislice TPU traffic.  |  `tcp_min_rtt` |  `['27.63, 29.03, 38.52, 41.63, 52.74']`   
  
# Represents the distribution's mean, p50, p90, p95, and p99.9 percentiles in microseconds (µs).   
Throughput at Transport Layer  |  Cumulative distribution of the recent throughput of TCP connections used by gRPC for multislice TPU traffic.  |  `tcp_delivery_rate` |  `['11354.89, 10986.35, 18239.55, 25718.35, 44841.55']`   
  
# Represents the distribution's mean, p50, p90, p95, and p99.9 percentiles in megabits per second (Mbps).   
  
## Read metric data

To read metric data, specify the metric name when you call the `tpumonitoring.get_metric` function. You can insert ad hoc metric checks into low-performance code to identify whether performance issues stem from software or hardware.

The following code sample shows how to read the `duty_cycle` metric:
    
    
    from libtpu.sdk import tpumonitoring
    
    metric = tpumonitoring.get_metric("duty_cycle_pct")
    
    metric.description()
    "The metric provides a list of duty cycle percentages, one for each
    accelerator (from accelerator_0 to accelerator_x). The duty cycle represents
    the percentage of time an accelerator was actively processing during the
    last sample period, indicating TPU utilization."
    
    metric.data()
    ["0.00", "0.00", "0.00", "0.00"]
    
    # accelerator_0-3
    
    

**Note:** Runtime metrics return an empty list until the TPU runtime is initialized in the current process (for example, before your workload runs its first TPU operation). When the runtime is initialized but idle, values are reported as zero.**Note:** `get_metric` doesn't raise an error for an unrecognized metric name; it returns an empty description and an empty list. Use `tpumonitoring.list_supported_metrics()` to confirm a metric name.**Note:** Metric data isn't always in list format. Check the description for a detailed format explanation.

## Use metrics to check TPU utilization

The following examples show how to use metrics from the TPU Monitoring Library to track TPU utilization during training and inference.

**Note:** The placeholder models in these examples are small, so `duty_cycle_pct` might report `0.00`. With a real workload that keeps the TPU busy, the metric reports the percentage of time the TPU was active during the sample period.

### Monitor TPU duty cycle during training

### JAX

**Scenario:** You are running a JAX training script and want to monitor the TPU's `duty_cycle_pct` metric throughout training to confirm your TPUs are effectively utilized. You can log this metric periodically during training to track TPU utilization.

The following code sample shows how to monitor TPU duty cycle during JAX training:
    
    
    import jax
    import jax.numpy as jnp
    from libtpu.sdk import tpumonitoring
    import time
    
    # --- Your JAX model and training setup would go here ---
    # --- Example placeholder model and data (replace with your actual setup) ---
    def simple_model(x):
        return jnp.sum(x)
    
    def loss_fn(params, x, y):
        preds = simple_model(x)
        return jnp.mean((preds - y)**2)
    
    def train_step(params, x, y, optimizer):
        grads = jax.grad(loss_fn)(params, x, y)
        return optimizer.update(grads, params)
    
    key = jax.random.PRNGKey(0)
    params = jnp.array([1.0, 2.0])  # Example params
    optimizer = ...  # Your optimizer (for example, optax.adam)
    data_x = jnp.ones((10, 10))
    data_y = jnp.zeros((10,))
    
    num_epochs = 10
    log_interval_steps = 2  # Log duty cycle every 2 steps
    
    for epoch in range(num_epochs):
        for step in range(5):  # Example steps per epoch
    
            params = train_step(params, data_x, data_y, optimizer)
    
            if (step + 1) % log_interval_steps == 0:
                # --- Integrate TPU Monitoring Library here to get duty_cycle ---
                duty_cycle_metric = tpumonitoring.get_metric("duty_cycle_pct")
                duty_cycle_data = duty_cycle_metric.data()
                print(f"Epoch {epoch+1}, Step {step+1}: TPU Duty Cycle Data:")
                print(f"  Description: {duty_cycle_metric.description()}")
                print(f"  Data: {duty_cycle_data}")
                # --- End TPU Monitoring Library Integration ---
    
            # --- Rest of your training loop logic ---
            time.sleep(0.1)  # Simulate some computation
    
    print("Training complete.")
    

### TorchTPU

**Scenario:** You are running a PyTorch training script with `torch_tpu` and want to monitor the TPU's `duty_cycle_pct` metric throughout training to confirm your TPUs are effectively utilized. Because `torch_tpu` uses LibTPU underneath, you can query `tpumonitoring` directly inside your PyTorch training loop.

The following code sample shows how to monitor TPU duty cycle during PyTorch (`torch_tpu`) training:
    
    
    import time
    import torch
    import torch.nn as nn
    import torch.optim as optim
    from libtpu.sdk import tpumonitoring
    
    # Initialize the TPU device (torch_tpu autoloads on `import torch`)
    device = torch.device("tpu")
    
    # --- Your PyTorch model and training setup would go here ---
    # --- Example placeholder model and data (replace with your actual setup) ---
    class SimpleModel(nn.Module):
        def __init__(self):
            super().__init__()
            self.linear = nn.Linear(10, 1)
    
        def forward(self, x):
            return self.linear(x).squeeze(-1)
    
    model = SimpleModel().to(device)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    data_x = torch.ones((10, 10), device=device)
    data_y = torch.zeros((10,), device=device)
    
    num_epochs = 10
    log_interval_steps = 2  # Log duty cycle every 2 steps
    
    for epoch in range(num_epochs):
        model.train()
        for step in range(5):  # Example steps per epoch
            optimizer.zero_grad()
            preds = model(data_x)
            loss = criterion(preds, data_y)
            loss.backward()
            optimizer.step()
    
            if (step + 1) % log_interval_steps == 0:
                # --- Integrate TPU Monitoring Library here to get duty_cycle ---
                duty_cycle_metric = tpumonitoring.get_metric("duty_cycle_pct")
                duty_cycle_data = duty_cycle_metric.data()
                print(f"Epoch {epoch+1}, Step {step+1}: TPU Duty Cycle Data:")
                print(f"  Description: {duty_cycle_metric.description()}")
                print(f"  Data: {duty_cycle_data}")
                # --- End TPU Monitoring Library Integration ---
    
            # --- Rest of your training loop logic ---
            time.sleep(0.1)  # Simulate some computation
    
    print("Training complete.")
    

### Check HBM utilization before running inference

### JAX

**Scenario:** Before running inference with your JAX model, check the current HBM (High Bandwidth Memory) utilization on the TPU to confirm that you have enough memory available and to get a baseline measurement before inference starts.
    
    
    # The following code sample shows how to check HBM utilization before JAX inference:
    import jax
    import jax.numpy as jnp
    from libtpu.sdk import tpumonitoring
    
    # --- Your JAX model and inference setup would go here ---
    # --- Example placeholder model (replace with your actual model loading/setup) ---
    def simple_model(x):
        return jnp.sum(x)
    
    key = jax.random.PRNGKey(0)
    params = ...  # Load your trained parameters
    
    # Integrate the TPU Monitoring Library to get HBM utilization before inference
    hbm_util_metric = tpumonitoring.get_metric("hbm_util")
    hbm_util_data = hbm_util_metric.data()
    print("HBM Utilization Before Inference:")
    print(f"  Description: {hbm_util_metric.description()}")
    print(f"  Data: {hbm_util_data}")
    # End TPU Monitoring Library Integration
    
    # Your Inference Logic
    input_data = jnp.ones((1, 10))  # Example input
    predictions = simple_model(input_data)
    print("Inference Predictions:", predictions)
    
    print("Inference complete.")
    

### TorchTPU

**Scenario:** Before running inference with your PyTorch model on `torch_tpu`, check the current HBM (High Bandwidth Memory) utilization on the TPU to confirm that you have enough memory available and to get a baseline measurement before inference starts.
    
    
    # The following code sample shows how to check HBM utilization before PyTorch (torch_tpu) inference:
    import torch
    import torch.nn as nn
    from libtpu.sdk import tpumonitoring
    
    device = torch.device("tpu")
    
    # --- Your PyTorch model and inference setup would go here ---
    # --- Example placeholder model (replace with your actual model loading/setup) ---
    class SimpleModel(nn.Module):
        def __init__(self):
            super().__init__()
            self.linear = nn.Linear(10, 1)
    
        def forward(self, x):
            return self.linear(x)
    
    model = SimpleModel().to(device)
    model.eval()
    
    # Integrate the TPU Monitoring Library to get HBM utilization before inference
    hbm_util_metric = tpumonitoring.get_metric("hbm_util")
    hbm_util_data = hbm_util_metric.data()
    print("HBM Utilization Before Inference:")
    print(f"  Description: {hbm_util_metric.description()}")
    print(f"  Data: {hbm_util_data}")
    # End TPU Monitoring Library Integration
    
    # Your Inference Logic
    input_data = torch.ones((1, 10), device=device)  # Example input
    with torch.no_grad():
        predictions = model(input_data)
    print("Inference Predictions:", predictions.cpu())
    
    print("Inference complete.")
    

## Check network metrics

**Scenario:** You are running a multi-host and multislice workload and want to connect to one of the GKE pods or TPUs using SSH to view network metrics while the workload is running. You can also incorporate these commands directly into your multi-host workload.

**Note:** Network metrics such as `tcp_delivery_rate` and `tcp_min_rtt` are populated only when there is multislice (DCN) traffic. On a single-slice workload, they return an empty list.

### JAX
    
    
    import jax
    import jax.numpy as jnp
    from libtpu.sdk import tpumonitoring
    
    # --- Your JAX model and multi-host training setup goes here ---
    metric_name_rate = "tcp_delivery_rate"
    metric_name_rtt = "tcp_min_rtt"
    
    # ==============================================================================
    # Metric 1: TCP Delivery Rate
    # ==============================================================================
    # This metric reflects the delivery rate of the TCP connection (bytes delivered / elapsed time).
    # The output is a list of strings representing delivery rate statistics:
    # [mean, p50, p90, p95, p99.9]
    # Example: ['100.00', '200.00', '300.00', '400.00', '500.00'] (Values in Mbps)
    delivery_rate_metric = tpumonitoring.get_metric(metric_name_rate)
    print("Description:", delivery_rate_metric.description())
    print("Data:", delivery_rate_metric.data())
    
    # ==============================================================================
    # Metric 2: TCP Minimum Round Trip Time (RTT)
    # ==============================================================================
    # This metric reflects the minimum RTT measured between sending a TCP packet
    # and receiving the acknowledgement.
    # The output is a list of strings representing latency statistics:
    # [mean, p50, p90, p95, p99.9]
    # Example: ['100.00', '200.00', '300.00', '400.00', '500.00'] (Values in us - microseconds)
    min_rtt_metric = tpumonitoring.get_metric(metric_name_rtt)
    print("Description:", min_rtt_metric.description())
    print("Data:", min_rtt_metric.data())
    

### TorchTPU
    
    
    import torch
    from libtpu.sdk import tpumonitoring
    
    device = torch.device("tpu")
    
    # --- Your distributed PyTorch (torch_tpu) model and training setup goes here ---
    metric_name_rate = "tcp_delivery_rate"
    metric_name_rtt = "tcp_min_rtt"
    
    # ==============================================================================
    # Metric 1: TCP Delivery Rate
    # ==============================================================================
    delivery_rate_metric = tpumonitoring.get_metric(metric_name_rate)
    print("Description:", delivery_rate_metric.description())
    print("Data:", delivery_rate_metric.data())
    
    # ==============================================================================
    # Metric 2: TCP Minimum Round Trip Time (RTT)
    # ==============================================================================
    min_rtt_metric = tpumonitoring.get_metric(metric_name_rtt)
    print("Description:", min_rtt_metric.description())
    print("Data:", min_rtt_metric.data())
    

## Refresh frequency of TPU metrics

The refresh frequency of TPU metrics is constrained to a minimum of one second. Host metric data is exported at a fixed frequency of 1 Hz. The latency introduced by this export process is negligible. Runtime metrics from LibTPU are not subject to the same frequency constraint. However, for consistency, these metrics are also sampled at 1 Hz or 1 sample per second.

## TPU-Z module

TPU-Z is a telemetry and debugging facility for TPUs. It provides detailed runtime status information for all TPU cores attached to a host. The functionality is provided through the `tpuz` module, which is part of the `libtpu.sdk` module in the `libtpu` Python SDK. The module provides a snapshot of each core's state.

The primary use case for TPU-Z is diagnosing hangs or deadlocks in distributed TPU workloads. You can query the TPU-Z service on hosts to capture the state of every core, comparing the Program Counters, HLO locations, and Run IDs across all cores to identify anomalies.

Use the `get_core_state_summary()` function within the `libtpu.sdk` library to display the TPU-Z metrics:
    
    
    from libtpu import sdk
    
    summary = sdk.tpuz.get_core_state_summary()
    

The output for the TPU-Z metrics is provided as a dictionary. The following is a truncated example for a single core:
    
    
    {
      "host_name": "my-tpu-host-vm",
      "core_states": {
        "1": {
          "core_id": {
            "global_core_id": 1,
            "chip_id": 0,
            "core_on_chip": {
              "type": "TPU_CORE_TYPE_TENSOR_CORE",
              "index": 1
            }
          },
          "sequencer_info": [
            {
              "sequencer_type": "TPU_SEQUENCER_TYPE_TENSOR_CORE_SEQUENCER",
              "sequencer_index": 0,
              "pc": 4490,
              "program_id": 3274167277388825310,
              "run_id": 3
            }
          ],
          "program_fingerprint": "b'\\xbefB\\xc6\\x1eb\\xc1#\\xd0...'",
          "queued_program_info": [],
          "error_message": ""
        }
        // ...
      }
    }
    

To retrieve information about the High-Level Optimizers (HLO) on each core, set the `include_hlo_info` parameter to `True`:
    
    
    summary = sdk.tpuz.get_core_state_summary(include_hlo_info=True)
    

The output includes additional HLO Information:
    
    
    "1": {
        "core_id": {
          "global_core_id": 1,
          "chip_id": 0,
          "core_on_chip": {
            "type": "TPU_CORE_TYPE_TENSOR_CORE",
            "index": 1
          }
        },
        "sequencer_info": [
          {
            "sequencer_type": "TPU_SEQUENCER_TYPE_TENSOR_CORE_SEQUENCER",
            "sequencer_index": 0,
            "pc": 17776,
            "tag": 3,
            "tracemark": 2147483646,
            "program_id": 3230481660274331500,
            "run_id": 81,
            "hlo_location": "HLO: fusion.11; HLO computation: main.126_spmd",
            "hlo_detailed_info": "[{\"details\":\"HloModule fusion.11, entry_computation_layout={(bf16[20>..."
          }
        ],
        "program_fingerprint": "\ufffdU\ufffd4j\u7c6e\ufffd\ufffd{\u0017\ufffd\ufffdHHV\ufffdD\ufffde\uff>",
        "launch_id": 1394130914,
        "queued_program_info": [
          {
            "run_id": 81,
            "launch_id": 1394130914,
            "program_fingerprint": "\ufffdU\ufffd4j\u7c6e\ufffd\ufffd{\u0017\ufffd\ufffdHHV\ufffdD\ufffde>"
          }
        ]
      }
    

### TPU-Z metrics

The `get_core_state_summary` function returns TPU-Z metrics in the form of a dictionary with the following structure.

#### `CurrentCoreStateSummary`

The `CurrentCoreStateSummary` dictionary provides detailed summary of an individual TPU core's state.

**Field** | **Type** | **Description**  
---|---|---  
`core_id` | dictionary | A `TpuCoreIdentifier` dictionary that contains ID information about the TPU core.  
`sequencer_info` | list of dictionaries | A list of `SequencerInfo` dictionaries, describing the state of each sequencer on the core.  
`program_fingerprint` | bytes | The fingerprint of the program executing on this core.  
`launch_id` | integer | The launch ID of the current or most recent program.  
`queued_program_info` | list of dictionaries | A list of `QueuedProgramInfo` dictionaries for programs queued for execution.  
`error_message` | string | Any error messages for this core.  
  
#### `TpuCoreIdentifier`

The `TpuCoreIdentifier` dictionary provides ID information for cores within the TPU system.

**Field** | **Type** | **Description**  
---|---|---  
`global_core_id` | integer | The ID of the core.  
`chip_id` | integer | The ID of the chip that the core belongs to.  
`core_on_chip` | dictionary | A `TpuCoreOnChip` dictionary describing the core's type and its index on the chip.  
  
#### `TpuCoreOnChip`

The `TpuCoreOnChip` dictionary contains information about a core's properties within a specific chip.

**Field** | **Type** | **Description**  
---|---|---  
`type` | string | The type of the TPU core. For example: `TPU_CORE_TYPE_TENSOR_CORE`.  
`index` | integer | The index of the core on the chip.  
  
#### `SequencerInfo`

The `SequencerInfo` dictionary contains information about the state of a single sequencer on a core.

**Field** | **Type** | **Description**  
---|---|---  
`sequencer_type` | string | The type of sequencer. For example: `TPU_SEQUENCER_TYPE_TENSOR_CORE_SEQUENCER`.  
`sequencer_index` | integer | The index of the sequencer (if there are multiple of the same type).  
`pc` | integer | The current Program Counter value.  
`program_id` | integer | The ID associated with a specific instance of a program being launched for execution on a TPU core.  
`run_id` | integer | The Run ID associated with a specific instance of a program's execution on a TPU core.  
`hlo_location` | string | High Level Optimizer location information.  
`hlo_detailed_info` | string | Detailed High Level Optimizer information.  
  
#### `QueuedProgramInfo`

The `QueuedProgramInfo` dictionary contains information about programs queued for execution on a core.

**Field** | **Type** | **Description**  
---|---|---  
`run_id` | integer | The Run ID for the queued program.  
`launch_id` | integer | The Launch ID for the queued program.  
`program_fingerprint` | bytes | The fingerprint of the queued program.  
  
### Use TPU-Z in workloads

You can access TPU-Z metrics in your workloads using either JAX or TorchTPU (`torch_tpu`).

### JAX

You can access TPU-Z metrics in JAX workloads through the `libtpu.sdk` library. The following Python script uses JAX for tensor computation while querying the `libtpu` SDK in a background thread to monitor the state and activity of the underlying TPU hardware.

Include the following Python packages and constants:
    
    
    import jax
    import jax.numpy as jnp
    import time
    import threading
    from functools import partial
    from libtpu import sdk
    
    MONITORING_INTERVAL_SECONDS = 5
    JOB_DURATION_SECONDS = 30
    monitoring_active = True
    

The `monitor_tpu_status` function uses a background thread to continuously show the operational status of the TPU cores while the main application executes a JAX workload.
    
    
    def monitor_tpu_status():
      """Monitors TPU status in a background thread."""
    
      while monitoring_active:
        try:
          summary = sdk.tpuz.get_core_state_summary(include_hlo_info=True)
          if summary and 'core_states' in summary:
            print(summary)
          else:
            print('WARNING: Call returned an empty or invalid summary.')
        except RuntimeError as e:
          print(f'FAIL: Error calling API: {e}')
        except Exception as e:
          print(f'FAIL: Unexpected error in monitor thread: {e}')
    
        for _ in range(MONITORING_INTERVAL_SECONDS * 2):
          if not monitoring_active:
            break
          time.sleep(0.5)
      print('✅ Monitoring thread stopped.')
    

The `transformer_block` function implements a layer of the Transformer architecture.
    
    
    @partial(jax.jit, static_argnames=['num_heads'])
    def transformer_block(params, x, num_heads=32):
      """A simplified but computationally intensive Transformer block."""
      # Multi-head Self-Attention
      qkv = jnp.dot(x, params['qkv_kernel'])
      q, k, v = jnp.array_split(qkv, 3, axis=-1)
    
      # Reshape for multi-head attention
      q = q.reshape(q.shape[0], q.shape[1], num_heads, -1).transpose(0, 2, 1, 3)
      k = k.reshape(k.shape[0], k.shape[1], num_heads, -1).transpose(0, 2, 1, 3)
      v = v.reshape(v.shape[0], v.shape[1], num_heads, -1).transpose(0, 2, 1, 3)
    
      # Scaled dot-product attention
      attention_scores = jnp.einsum('nhqd,nhkd->nhqk', q, k) / jnp.sqrt(q.shape[-1])
      attention_weights = jax.nn.softmax(attention_scores, axis=-1)
      attention_output = jnp.einsum('nhqk,nhvd->nhqd', attention_weights, v)
      attention_output = attention_output.transpose(0, 2, 1, 3).reshape(x.shape)
    
      attention_output = jnp.dot(attention_output, params['o_kernel'])
    
      # Residual connection and Layer Normalization 1
      h1 = x + attention_output
      h1_norm = h1 - jnp.mean(h1, axis=-1, keepdims=True)
      h1_norm = h1_norm / jnp.sqrt(
          jnp.mean(jnp.square(h1_norm), axis=-1, keepdims=True) + 1e-5
      )
    
      # Feed-Forward Network
      ffn_hidden = jax.nn.gelu(jnp.dot(h1_norm, params['ffn1_kernel']))
      ffn_output = jnp.dot(ffn_hidden, params['ffn2_kernel'])
    
      # Residual connection and Layer Normalization 2
      h2 = h1_norm + ffn_output
      h2_norm = h2 - jnp.mean(h2, axis=-1, keepdims=True)
      h2_norm = h2_norm / jnp.sqrt(
          jnp.mean(jnp.square(h2_norm), axis=-1, keepdims=True) + 1e-5
      )
    
      return h2_norm
    

The `main` function sets up the JAX computation, starts the background TPU monitoring thread, and runs the main workload loop.
    
    
    def main():
      num_devices = jax.device_count()
      print(f"Running on {num_devices} devices.")
    
      batch_size = 128 * num_devices
      seq_len = 512
      embed_dim = 1024
      ffn_dim = embed_dim * 4
    
      key = jax.random.PRNGKey(0)
    
      params = {
          'qkv_kernel': jax.random.normal(
              key, (embed_dim, embed_dim * 3), dtype=jnp.bfloat16
          ),
          'o_kernel': jax.random.normal(
              key, (embed_dim, embed_dim), dtype=jnp.bfloat16
          ),
          'ffn1_kernel': jax.random.normal(
              key, (embed_dim, ffn_dim), dtype=jnp.bfloat16
          ),
          'ffn2_kernel': jax.random.normal(
              key, (ffn_dim, embed_dim), dtype=jnp.bfloat16
          ),
      }
      input_data = jax.random.normal(
          key, (batch_size, seq_len, embed_dim), dtype=jnp.bfloat16
      )
      input_data = jax.device_put(input_data)
      monitor_thread = threading.Thread(target=monitor_tpu_status)
      monitor_thread.start()
      print("Starting JAX computation loop...")
      start_time = time.time()
      iterations = 0
      while time.time() - start_time < JOB_DURATION_SECONDS:
        result = transformer_block(params, input_data)
        result.block_until_ready()
        iterations += 1
        print(f'  -> Jax iteration {iterations} complete.', end='\r')
    
      print(f"\nCompleted {iterations} iterations in {JOB_DURATION_SECONDS} seconds.")
    
      global monitoring_active
      monitoring_active = False
      monitor_thread.join()
    
    if __name__ == '__main__':
      main()
    

### TorchTPU

You can access TPU-Z metrics in PyTorch workloads using `torch_tpu` and the `libtpu.sdk` library. The following Python script runs a Transformer block on TPU using `torch_tpu` while querying the `libtpu` SDK in a background thread to monitor the state and activity of the underlying TPU cores.

Include the following Python packages and constants:
    
    
    import time
    import threading
    import torch
    import torch.nn as nn
    from libtpu import sdk
    
    MONITORING_INTERVAL_SECONDS = 5
    JOB_DURATION_SECONDS = 30
    monitoring_active = True
    

The `monitor_tpu_status` function uses a background thread to continuously show the operational status of the TPU cores while the main application executes a PyTorch (`torch_tpu`) workload:
    
    
    def monitor_tpu_status():
      """Monitors TPU status in a background thread."""
    
      while monitoring_active:
        try:
          summary = sdk.tpuz.get_core_state_summary(include_hlo_info=True)
          if summary and 'core_states' in summary:
            print(summary)
          else:
            print('WARNING: Call returned an empty or invalid summary.')
        except RuntimeError as e:
          print(f'FAIL: Error calling API: {e}')
        except Exception as e:
          print(f'FAIL: Unexpected error in monitor thread: {e}')
    
        for _ in range(MONITORING_INTERVAL_SECONDS * 2):
          if not monitoring_active:
            break
          time.sleep(0.5)
      print('✅ Monitoring thread stopped.')
    

The `TransformerBlock` module implements an equivalent Transformer layer in PyTorch:
    
    
    class TransformerBlock(nn.Module):
      """A simplified but computationally intensive Transformer block in PyTorch."""
    
      def __init__(self, embed_dim=1024, num_heads=32, ffn_dim=4096):
        super().__init__()
        self.attn = nn.MultiheadAttention(
            embed_dim=embed_dim, num_heads=num_heads, batch_first=True
        )
        self.norm1 = nn.LayerNorm(embed_dim, eps=1e-5)
        self.ffn = nn.Sequential(
            nn.Linear(embed_dim, ffn_dim),
            nn.GELU(),
            nn.Linear(ffn_dim, embed_dim),
        )
        self.norm2 = nn.LayerNorm(embed_dim, eps=1e-5)
    
      def forward(self, x):
        attn_output, _ = self.attn(x, x, x, need_weights=False)
        h1_norm = self.norm1(x + attn_output)
        ffn_output = self.ffn(h1_norm)
        h2_norm = self.norm2(h1_norm + ffn_output)
        return h2_norm
    

The `main` function initializes the TPU device, starts the background TPU-Z monitoring thread, and runs the PyTorch computation loop:
    
    
    def main():
      device = torch.device("tpu")
      print(f"Running on device: {device}")
    
      batch_size = 128
      seq_len = 512
      embed_dim = 1024
      ffn_dim = embed_dim * 4
    
      model = (
          TransformerBlock(embed_dim=embed_dim, num_heads=32, ffn_dim=ffn_dim)
          .to(dtype=torch.bfloat16, device=device)
          .eval()
      )
      input_data = torch.randn(
          (batch_size, seq_len, embed_dim), dtype=torch.bfloat16, device=device
      )
      monitor_thread = threading.Thread(target=monitor_tpu_status)
      monitor_thread.start()
      print("Starting PyTorch (torch_tpu) computation loop...")
      start_time = time.time()
      iterations = 0
      with torch.no_grad():
        while time.time() - start_time < JOB_DURATION_SECONDS:
          result = model(input_data)
          torch.accelerator.synchronize()
          iterations += 1
          print(f'  -> PyTorch iteration {iterations} complete.', end='\r')
    
      print(f"\nCompleted {iterations} iterations in {JOB_DURATION_SECONDS} seconds.")
    
      global monitoring_active
      monitoring_active = False
      monitor_thread.join()
    
    if __name__ == '__main__':
      main()
    

## Troubleshooting

This section provides troubleshooting information to help you identify and resolve problems you might encounter while using the TPU Monitoring Library.

### Missing features or metrics

If you are unable to view some features or metrics, the most common cause is an outdated `libtpu` version. The TPU Monitoring Library features and metrics are included in the `libtpu` releases, and outdated versions might be missing new features and metrics.

Check the version of `libtpu` that is running in your environment:

Command line:
    
    
    pip show libtpu
    

Python:
    
    
    import libtpu
    
    print(libtpu.__version__)
    

If you are not using the [latest version](https://pypi.org/project/libtpu/) of `libtpu`, use the following command to update the library:
    
    
    pip install --upgrade libtpu
    

### No TPU device or metrics when using TorchTPU

`torch_tpu` loads automatically when you run `import torch`, and it registers the `"tpu"` device only if TPU devices are detected on the host. If `torch.device("tpu")` is unavailable or metric values are all zero, verify that you are running on a TPU VM, that no other process is using the TPUs, and that the `TORCH_DEVICE_BACKEND_AUTOLOAD` environment variable is not set to `0`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
