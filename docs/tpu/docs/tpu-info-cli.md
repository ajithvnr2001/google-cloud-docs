---
url: https://docs.cloud.google.com/tpu/docs/tpu-info-cli/
title: Monitor with tpu-info CLI \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:14.767215+00:00
---

# Monitor with tpu-info CLI  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/tpu-info-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor with tpu-info CLI

The `tpu-info` CLI is a tool for detecting Cloud TPU devices and reading runtime metrics from the `libtpu` library, including memory usage and duty cycle. It supports static, one-time snapshots, and live streaming to monitor metrics continuously.

## Installation

Install the latest release using `pip`:
    
    
    pip install tpu-info
    

Alternatively, install `tpu-info` from source:
    
    
    pip install git+https://github.com/google/cloud-accelerator-diagnostics/#subdirectory=tpu_info
    

**Note:** Use the `--help` or `-h` flags to access help information for `tpu-info`.

If you have already installed a version of `tpu-info`, make sure it is compatible with your environment and is not missing any metrics and features. For more information, see Missing features or metrics.

## Access standard LibTPU metrics using the CLI

Use the following command to view the default `tpu-info` metrics with the CLI:
    
    
    tpu-info
    

The output is similar to the following:
    
    
    TPU Chips
    
    | Chip         | Type         | Devices | PID    |
    |--------------|--------------|---------|--------|
    | /dev/vfio/0  | TPU v6e chip | 1       | 1022   |
    | /dev/vfio/1  | TPU v6e chip | 1       | 1022   |
    | /dev/vfio/2  | TPU v6e chip | 1       | 1022   |
    | /dev/vfio/3  | TPU v6e chip | 1       | 1022   |
    
    TPU Runtime Utilization
    
    | Chip   | HBM Usage (GiB)          | Duty cycle |
    |--------|--------------------------|------------|
    | 8      | 17.26 GiB / 31.25 GiB    |    100.00% |
    | 9      |  9.26 GiB / 31.25 GiB    |    100.00% |
    | 12     |  9.26 GiB / 31.25 GiB    |    100.00% |
    | 13     |  9.26 GiB / 31.25 GiB    |    100.00% |
    
    TensorCore Utilization
    
    | Core ID | TensorCore Utilization |
    |---------|------------------------|
    | 0       | 15.17%                 |
    | 1       | 14.62%                 |
    | 2       | 14.68%                 |
    | 3       | 15.14%                 |
    
    TPU Buffer Transfer Latency
    
    | Buffer Size  | P50          | P90          | P95          | P999         |
    |--------------|--------------|--------------|--------------|--------------|
    | 8MB+         | 18264.03 us  | 33263.06 us  | 35990.98 us  | 53997.32 us  |
    
    TPU Inbound Buffer Transfer Latency
    
    | Buffer Size  | P50          | P90          | P95          | P999         |
    |--------------|--------------|--------------|--------------|--------------|
    | 8MB+         | 18316.95 us  | 32857.03 us  | 36501.59 us  | 58854.54 us  |
    
    TPU Host Compute Latency
    
    | Buffer Size  | P50          | P90          | P95          | P999         |
    |--------------|--------------|--------------|--------------|--------------|
    | 8MB+         | 678.33 us    | 2611.93 us   | 5258.30 us   | 11083.23 us  |
    
    TPU gRPC TCP Minimum RTT
    
    | P50      | P90      | P95      | P999     |
    |----------|----------|----------|----------|
    | 35.99 us | 52.15 us | 53.83 us | 55.51 us |
    
    TPU gRPC TCP Delivery Rate
    
    | P50           | P90           | P95           | P999          |
    |---------------|---------------|---------------|---------------|
    | 12305.96 Mbps | 18367.10 Mbps | 24872.11 Mbps | 44841.55 Mbps |
    

## Usage

To view current TPU utilization data, `tpu-info` requires a running TPU workload with a supported ML framework, such as JAX or PyTorch. You can run the `tpu-info` command in your terminal with the following flags.

### Process

Use the `--process` or `-p` flag to display information about the processes running on the TPU.
    
    
    $ tpu-info --process

The output should look similar to the following:
    
    
    TPU Process Info
    
    | Chip        | PID    | Process Name |
    |-------------|--------|--------------|
    | /dev/vfio/0 | 799657 | python3      |
    | /dev/vfio/1 | 799657 | python3      |
    | /dev/vfio/2 | 799657 | python3      |
    | /dev/vfio/3 | 799657 | python3      |
    | /dev/vfio/4 | 799657 | python3      |
    | /dev/vfio/5 | 799657 | python3      |
    | /dev/vfio/6 | 799657 | python3      |
    | /dev/vfio/7 | 799657 | python3      |
    

### Metric

Use the `--metric` flag to display specific metrics. You can specify multiple metrics separated by spaces. Some common supported metrics are:

  * `hbm_usage`
  * `duty_cycle_percent`
  * `tensorcore_utilization`
  * `buffer_transfer_latency`
  * `host_to_device_transfer_latency`
  * `device_to_host_transfer_latency`
  * `collective_e2e_latency`


    
    
    $ tpu-info --metric duty_cycle_percent hbm_usage

The output should look similar to the following:
    
    
    TPU Duty Cycle
    
    | Core ID | Duty Cycle (%) |
    |---------|----------------|
    | 0       | 100.00%        |
    | 1       | 100.00%        |
    | 2       | 100.00%        |
    | 3       | 100.00%        |
    | 4       | 100.00%        |
    | 5       | 100.00%        |
    | 6       | 100.00%        |
    | 7       | 100.00%        |
    
    TPU HBM Usage
    
    | Chip   | HBM Usage (GiB)       |
    |--------|-----------------------|
    | 0      | 29.50 GiB / 31.25 GiB |
    | 1      | 21.50 GiB / 31.25 GiB |
    | 2      | 21.50 GiB / 31.25 GiB |
    | 3      | 21.50 GiB / 31.25 GiB |
    | 4      | 21.50 GiB / 31.25 GiB |
    | 5      | 21.50 GiB / 31.25 GiB |
    | 6      | 21.50 GiB / 31.25 GiB |
    | 7      | 21.50 GiB / 31.25 GiB |
    

### List metrics

Use the `--list_metrics` flag to display all supported metrics that can be requested with the `--metric` flag.
    
    
    $ tpu-info --list_metrics

The output should look similar to the following:
    
    
    ╭─ Supported Metrics ─────────────────────────────────────────────────────────────────────────────╮
    │         grpc_tcp_min_rtt                                                                        │
    │         host_to_device_transfer_latency                                                         │
    │         grpc_tcp_delivery_rate                                                                  │
    │         inbound_buffer_transfer_latency                                                         │
    │         host_compute_latency                                                                    │
    │         buffer_transfer_latency                                                                 │
    │         collective_e2e_latency                                                                  │
    │         device_to_host_transfer_latency                                                         │
    │         hbm_usage                                                                               │
    │         duty_cycle_percent                                                                      │
    │         tensorcore_utilization                                                                  │
    ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
    

### Stream metrics

Streaming mode periodically refreshes and displays up-to-date utilization statistics. To stream the LibTPU metrics, add the `--streaming` flag to the `tpu-info` command. Use the `--rate` flag to control the cadence of streaming in seconds.

Use the following command to stream the default `tpu-info` metrics with the CLI:
    
    
    # Refresh metrics every 2 seconds
    tpu-info --streaming --rate 2
    

The output is similar to the following:
    
    
    Refresh rate: 0.1s
    Last update: 2025-07-24 11:00:59 UTC
    Libtpu version: 0.0.19.dev20250721+nightly
    Accelerator type: v6e
    
    TPU Chips
    
    | Chip         | Type         | Devices | PID    |
    |--------------|--------------|---------|--------|
    | /dev/vfio/0  | TPU v6e chip | 1       | 1022   |
    | /dev/vfio/1  | TPU v6e chip | 1       | 1022   |
    | /dev/vfio/2  | TPU v6e chip | 1       | 1022   |
    | /dev/vfio/3  | TPU v6e chip | 1       | 1022   |
    
    TPU Runtime Utilization
    
    | Chip   | HBM Usage (GiB)          | Duty cycle |
    |--------|--------------------------|------------|
    | 8      | 17.26 GiB / 31.25 GiB    |    100.00% |
    | 9      |  9.26 GiB / 31.25 GiB    |    100.00% |
    | 12     |  9.26 GiB / 31.25 GiB    |    100.00% |
    | 13     |  9.26 GiB / 31.25 GiB    |    100.00% |
    
    TensorCore Utilization
    
    | Core ID | TensorCore Utilization |
    |---------|------------------------|
    | 0       | 15.17%                 |
    | 1       | 14.62%                 |
    | 2       | 14.68%                 |
    | 3       | 15.14%                 |
    
    TPU Buffer Transfer Latency
    
    | Buffer Size  | P50          | P90          | P95          | P999         |
    |--------------|--------------|--------------|--------------|--------------|
    | 8MB+         | 18264.03 us  | 33263.06 us  | 35990.98 us  | 53997.32 us  |
    
    TPU Inbound Buffer Transfer Latency
    
    | Buffer Size  | P50          | P90          | P95          | P999         |
    |--------------|--------------|--------------|--------------|--------------|
    | 8MB+         | 18316.95 us  | 32857.03 us  | 36501.59 us  | 58854.54 us  |
    
    TPU Host Compute Latency
    
    | Buffer Size  | P50          | P90          | P95          | P999         |
    |--------------|--------------|--------------|--------------|--------------|
    | 8MB+         | 678.33 us    | 2611.93 us   | 5258.30 us   | 11083.23 us  |
    
    TPU gRPC TCP Minimum RTT
    
    | P50      | P90      | P95      | P999     |
    |----------|----------|----------|----------|
    | 35.99 us | 52.15 us | 53.83 us | 55.51 us |
    
    TPU gRPC TCP Delivery Rate
    
    | P50           | P90           | P95           | P999          |
    |---------------|---------------|---------------|---------------|
    | 12305.96 Mbps | 18367.10 Mbps | 24872.11 Mbps | 44841.55 Mbps |
    

### TPU-Z metrics

TPU-Z is a telemetry and debugging facility for TPUs. It provides detailed runtime status information for all TPU cores attached to a host. The functionality is provided through the `tpuz` module, which is part of the `libtpu.sdk` module in the `libtpu` Python SDK. The module provides a snapshot of each core's state.

The primary use case for TPU-Z is diagnosing hangs or deadlocks in distributed TPU workloads. You can query the TPU-Z service on hosts to capture the state of every core, comparing the Program Counters, HLO locations, and Run IDs across all cores to identify anomalies.

Use the following command to view TPU-Z metrics using the CLI:
    
    
    tpu-info --metric core_state
    tpu-info --metric sequencer_state
    tpu-info --metric sequencer_state_detailed
    tpu-info --metric queued_program
    

The output should include the `core_state`, `sequencer_state`, `sequencer_state_detailed`, and `queued_programs` tables.

#### Core State Information

The Core State Information (`core_state`) table provides information on the cores of a given chip. TPUs have either one or two cores per chip, depending on the generation.

Field | Description | Example values  
---|---|---  
Chip ID | The ID of the chip that the core belongs to. | `0`  
Global Core ID | The unique ID of the core within the entire TPU system. | `1`  
Core Type | The type of the TPU core. | `"TPU_CORE_TYPE_TENSOR_CORE"`  
`"TPU_CORE_TYPE_SPARSE_CORE"`  
xdb Server Running | Indicates whether the Accelerator Debugger (XDB) server is running on a specific TPU core. | `True`  
  
The output should look similar to the following table:
    
    
    Core Information
    
    | Chip ID | Global Core ID | Core Type                   | xdb Server |
    |---------|----------------|-----------------------------|------------|
    | 0       | 0              | TPU_CORE_TYPE_TENSOR_CORE   | True       |
    | 0       | 1              | TPU_CORE_TYPE_SPARSE_CORE   | True       |
    | 1       | 2              | TPU_CORE_TYPE_SPARSE_CORE   | False      |
    | 1       | 3              | TPU_CORE_TYPE_SPARSE_CORE   | False      |
    | 2       | 4              | TPU_CORE_TYPE_SPARSE_CORE   | True       |
    | 2       | 5              | TPU_CORE_TYPE_SPARSE_CORE   | True       |
    

#### Sequencer State Information

The Sequencer State Information (`sequencer_state`) table provides information about a sequencer state on a core. A sequencer is a control unit within a TPU core responsible for fetching, decoding, and orchestrating the execution of instructions. There can be multiple sequencers for a single core.

Metric | Description | Example values  
---|---|---  
Chip ID | The ID of the chip that the core belongs to. | `0`  
Global Core ID | The unique ID of the core within the entire TPU system. | `1`  
Program Counter | The memory address of the instruction to be executed by the sequencer. | `15390`  
Tracemark | The launch ID of the current or most recent program. This field is absent if not applicable. | `2147483647`  
Program ID | The ID associated with a specific instance of a program being launched for execution on a TPU core. | `3230481660274331500`  
Run ID | The run ID associated with the program. | `1150`  
Sequence Type | The type of sequencer. | `"TPU_SEQUENCER_TYPE_SPARSE_CORE_SEQUENCER"`  
`"TPU_SEQUENCER_TYPE_SPARSE_CORE_TILE_EXECUTE_CORE_SEQUENCER"`  
  
The output should look similar to the following table:
    
    
    Sequencer Info
    
    | Chip ID | Global Core | Program Counter:Tag | Tracemark  | Program ID | Run ID | Sequence Type                 |
    |---------|-------------|---------------------|------------|------------|--------|-------------------------------|
    | 0       | 0           | 760:1               | 2147483647 | -5.75e17   | 1150   | TPU_SEQ_SPARSE_CORE_SEQUENCER |
    | 0       | 1           | 9:0                 | 0          | -1         | -1     | TPU_SEQ_SPARSE_TILE_EXECUTE   |
    | 0       | 1           | 0:0                 | 0          | -1         | -1     | TPU_SEQ_SPARSE_TILE_EXECUTE   |
    | 1       | 2           | 9:0                 | 0          | -1         | -1     | TPU_SEQ_SPARSE_TILE_EXECUTE   |
    | 1       | 3           | 0:0                 | 0          | -1         | -1     | TPU_SEQ_SPARSE_TILE_EXECUTE   |
    | 1       | 3           | 9:0                 | 0          | -1         | -1     | TPU_SEQ_SPARSE_TILE_EXECUTE   |
    | 1       | 3           | 0:0                 | 0          | -1         | -1     | TPU_SEQ_SPARSE_TILE_EXECUTE   |
    | 2       | 4           | 9:0                 | 0          | -1         | -1     | TPU_SEQ_SPARSE_TILE_EXECUTE   |
    | 2       | 4           | 0:0                 | 0          | -1         | -1     | TPU_SEQ_SPARSE_TILE_EXECUTE   |
    | 2       | 4           | 9:0                 | 0          | -1         | -1     | TPU_SEQ_SPARSE_TILE_EXECUTE   |
    | 2       | 5           | 9:0                 | 0          | -1         | -1     | TPU_SEQ_SPARSE_TILE_EXECUTE   |
    | 2       | 5           | 0:0                 | 0          | -1         | -1     | TPU_SEQ_SPARSE_TILE_EXECUTE   |
    
    

#### Sequencer State Information (detailed)

The Sequencer State Information (detailed) (`sequencer_state_detailed`) table provides all the information from the Sequencer State Information (`sequencer_state`) table, along with the following additional metrics:

Metric | Description | Example values  
---|---|---  
HLO Details | Detailed HLO information, if available. | `[]`  
Queued Program Run ID | The Run ID for this queued program. | `81`  
Queued Program Launch ID | The Launch ID for this queued program. | `1394130914`  
Core Error | Contains any error messages for this core. This field is absent if there are no errors. | `"Failed to parse launch id: 0xdcf36153"`  
HLO Location | High-level Optimizer (HLO) location information. | `"no HLO mapping"`  
`"HLO: fusion.11; HLO computation: main.126_spmd"`  
  
The output should look similar to the following table:
    
    
    Sequencer States (Detailed)
    
    | Chip ID | Global Core ID | Program Counter | Tracemark  | Program ID           | Run ID | Sequence Type                            | Core Error                                               | HLO Location   | HLO Details |
    |---------|----------------|-----------------|------------|----------------------|--------|------------------------------------------|----------------------------------------------------------|----------------|-------------|
    | 0       | 0              | 760             | 2147483647 | -5752110712385440928 | 114    | TPU_SEQUENCER_TYPE_TENSOR_CORE_SEQUENCER | Failed to parse launch id: 0xdcf36109                    | no HLO mapping | []          |
    | 0       | 1              | 9               | 0          | -1                   | -1     | TPU_SEQUENCER_TYPE_SPARSE_CORE_SEQUENCER | Compiler metadata or executable fingerprint not found.   | None           | None        |
    | 0       | 1              | 0               | 0          | -1                   | -1     | TPU_SEQUENCER_TYPE_SPARSE_CORE_TILE_EXE… | Compiler metadata or executable fingerprint not found.   | None           | None        |
    | 0       | 1              | 0               | 0          | -1                   | -1     | TPU_SEQUENCER_TYPE_SPARSE_CORE_TILE_EXE… | Compiler metadata or executable fingerprint not found.   | None           | None        |
    | ...     | ...            | ...             | ...        | ...                  | ...    | ...                                      | ...                                                      | ...            | ...         |
    
    

#### Queued programs

The Queued programs (`queued_programs`) table provides the list of programs queued for execution.

Metric | Description | Example values  
---|---|---  
Chip ID | The ID of the chip that the core belongs to. | `0`  
Global Core | The unique ID of the core within the entire TPU system. | `1`  
Program Counter:Tag | The memory address of the instruction to be executed by the sequencer. | `15390`  
Tracemark | The launch ID of the current or most recent program. This field is absent if not applicable. | `2147483647`  
Program ID | The ID associated with a specific instance of a program being launched for execution on a TPU core. | `3230481660274331500`  
Run ID | The run ID associated with the program. | `1150`  
Sequence Type | The type of sequencer. | `"\ufffdU\ufffd4j\u7c6e\ufffd\ufffd{\u0017\ufffd\ufffdHHV\ufffdD\ufffde\uff"`  
      
    
    Queued Programs
    
    | Chip ID | Global Core | Program Counter:Tag | Tracemark | Program ID  | Run ID | Sequence Type                      |
    |---------|-------------|---------------------|-----------|-------------|--------|------------------------------------|
    | 0       | 0           | 10712385440928      | 1220      | -5.75e17    | 1220   | \ufffdU\\...ufffd{\\u0017\\...\\   |
    | 0       | 1           | 31435440272417      | 1530      | -1          | 1530   | \ufff4j\\...\\ufffd{\\u0017\\...\\ |
    | 0       | 1           | 10230672051156      | 1410      | -1          | 1410   | \ufffde\\...\\ufffd{\\u0017\\...\\ |
    | ...     | ...         | ...                 | ...       | ...         | ...    | ...                                |
    
    

## Missing features or metrics

If you are unable to view some features or metrics, the most common cause is an outdated `libtpu` version. The features and metrics within `tpu-info` are included in the `libtpu` releases, and outdated versions might be missing new features and metrics.

To check that the version of `tpu-info` is compatible with your environment, use the `--version` or `-v` flag:
    
    
    $ tpu-info --version

The following output shows an example of a compatible environment:
    
    
    -   tpu-info version: 0.5.1
    -   libtpu version: 0.0.18
    -   accelerator type: v6e
    

The following output shows an example of an incompatible environment:
    
    
    -   tpu-info version: 0.5.1
    -   libtpu version: N/A (incompatible environment)
    -   accelerator type: N/A (incompatible environment)
    

If you are using an outdated version, update to the latest version of `libtpu`:
    
    
    pip install --upgrade libtpu
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
