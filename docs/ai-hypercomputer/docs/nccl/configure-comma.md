---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/configure-comma/
title: Enable, disable, and configure CoMMA \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:03.217415+00:00
---

# Enable, disable, and configure CoMMA  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/configure-comma/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Enable, disable, and configure CoMMA Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This guide describes how to enable, disable, and manage the Collective Communication Analyzer (CoMMA) library. CoMMA collects NCCL telemetry for Google Cloud services. For more information about CoMMA, see [Collective Communication Analyzer (CoMMA)](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma).

## Enable CoMMA

CoMMA is pre-installed and enabled if you use images that contain the NCCL gIB plugin. For a list of these images, see [Images that have CoMMA enabled](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma#auto-enabled-images).

### Installation options

If you don't use any of these images and want to install CoMMA, use one of the following methods.

Installation method | Supported machine types  
---|---  
**NCCL/gIB image** (Recommended for newer machine types) | A4X Max, A4X, A4 High, and A3 Ultra  
**CoMMA installer image** | A4X, A4 High, and A3 Ultra  
**Build from source** (Required for older machine types) | A3 Mega, A3 High, A3 Edge, A2 Ultra, A2 Standard, and N1 with attached GPUs  
  
### Install CoMMA

To install CoMMA, select one of the following options:

###  NCCL gIB image 

To install CoMMA by using the NCCL gIB image, run the following command.
    
    
    docker run --rm --name nccl-gib-installer
     --volume /usr/local/gib:/var/lib/gib \
     us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/nccl-plugin-gib install \
     --install-nccl
    

###  CoMMA installer image 

You can get CoMMA binaries in a standalone Docker image. You can use the CoMMA Docker image, `us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/comma-installer`, as `initContainers` to install CoMMA binaries into your workload container. The container stores the binaries in the `/artifacts` directory.

To use the CoMMA installer image, complete the following steps:

  1. [Install NCCL 2.23 or later](https://docs.nvidia.com/deeplearning/nccl/install-guide/index.html).

  2. Install CoMMA into your workload by adding the following snippet to your `initContainers`:
         
         - name: profiler-plugin-installer
           image: us-docker.pkg.dev/gce-ai-infra/gpudirect-gib/comma-installer:latest
           imagePullPolicy: Always
           volumeMounts:
           - name: nccl-plugin-volume
             mountPath: /usr/local/nccl-plugin
           command:
             - /bin/sh
             - -c
             - |
               set -ex
               rm -rf /usr/local/nccl-plugin/lib64/libnccl-profiler.so
               cp /artifacts/libnccl_profiler.so /usr/local/nccl-plugin/lib64/libnccl-profiler.so
         
               # GPUViz is a dependency of telemetry insights such as straggler detection
               rm -rf /usr/local/nccl-plugin/lib64/libGPUViz.so
               cp /artifacts/libGPUViz.so /usr/local/nccl-plugin/lib64/
         




The YAML configuration snippet specifies a container for installing CoMMA. The snippet specifies the installer container image, its pull policy, and a volume mount for the plugin. The same volume mount should be mounted to your workload container with `<mount-path>/lib64` added to `LD_LIBRARY_PATH`. The `command` section runs a shell script to remove any existing profiler library. It then copies the new profiler library into the designated plugin directory. The script ensures that the correct version of the profiler plugin is installed and ready for use.

###  Build from source 

To build the CoMMA library from source, install the following software:

  * Rust Programming Language, which the compiler and Cargo require. This could be installed with [rustup](https://rustup.rs/) or system packages
  * `Libclang-dev`, which `bindgen` requires.
  * `CMake` version 3.10 or later



To build from source, complete the following steps:

  1. Clone the repository and its submodules.
         
         git clone --recurse-submodules https://github.com/google/CoMMA

  2. Compile the binaries by using Cargo.
         
         cargo build --release

Cargo saves the binary in `target/release/libnccl_profiler.so`.

  3. Enable NCCL to load the CoMMA libraries by using one of the following methods:

     * Copy the compiled `libnccl_profiler.so` to a directory in your `LD_LIBRARY_PATH`. Rename it to `libnccl-profiler.so` (use a hyphen instead of an underscore).
     * Alternatively, set the `NCCL_PROFILER_PLUGIN` environment variable to specify the path of the `.so` file.



### Verify installation or enablement

To verify that NCCL loads the CoMMA libraries, review the NCCL logs:

  1. Enable NCCL debug logging. Enable logging by setting the `NCCL_DEBUG=INFO` environment variable. You can also specify a more detailed debug level. For more debug options, see the [`NCCL_DEBUG`](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html#nccl-debug) section in the NVIDIA documentation.
  2. Specify the `INIT` subsystem for debugging. Specify `INIT` by setting the `NCCL_DEBUG_SUBSYS=INIT` environment variable. You can also specify other subsystems. For more subsystem options, see the [`NCCL_DEBUG_SUBSYS`](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html#nccl-debug-subsys) section.
  3. Find a line in the NCCL log that is similar to the following: `NCCL INFO PROFILER/Plugin: Plugin name set by env to PATH_TO_PROFILER_PLUGIN`



## Disable CoMMA

**Caution:** For features such as [straggler detection](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor) to function, CoMMA must be enabled to export data to Google Cloud services.

If CoMMA is already installed, prevent it from collecting NCCL telemetry by setting the `NCCL_TELEMETRY_MODE=0` CoMMA environment variable before running your workloads. To set CoMMA environment variables, see Set environment variables.

To re-enable CoMMA after disabling it, follow these steps:

  1. Set the `NCCL_TELEMETRY_MODE` environment variable to a non-zero value; for example, to use the default mode, specify `NCCL_TELEMETRY_MODE=3`.

To review the full list of options, see `NCCL_TELEMETRY_MODE` in the Configuration options table.

  2. Verify that CoMMA is working.




## Configure and view CoMMA NCCL telemetry

If CoMMA is enabled in your environment, you can configure the type of telemetry data that it collects by setting the level of data granularity. This section explains how to set data granularity and the available options.

You can also review the data that CoMMA collects to verify that it aligns with your organization's security policies or to analyze it with your own NCCL telemetry analysis tools. To do so, export the raw data to a local file.

### Set data granularity

CoMMA collects NCCL telemetry at different granularity levels. Configure the granularity level by using environment variables. To set CoMMA environment variables, see Set environment variables.

  * **Default behavior** : By default, CoMMA tracks NCCL operations, including both collective and peer-to-peer, the metadata of those operations, and completion times. It uses the following environment variables: 
    * `NCCL_PROFILER_TRACK_NCCLOP=true`
    * `NCCL_PROFILER_AGGREGATE_STEPS=true`
    * `NCCL_PROFILER_TRACK_INTERPROCESS_PROXYOP=true`
  * To enable more granular levels of data collection, set the following environment variables: 
    * Track completion time for proxy operations by setting `NCCL_PROFILER_TRACK_PROXYOP=true`.
    * Track the time spent on each networking I/O operation by setting `NCCL_PROFILER_TRACK_STEPS=true`. This setting provides the highest level of granularity.



To review the full list of environment variables, see Configuration options.

### Export data to a local file

**Note:** CoMMA primarily collects NCCL telemetry for other features, such as straggler detection. However, you can also view the raw data by completing the steps in this section.

Export the raw data to a local file to view it. To export the data to a local file and view the output, follow the steps:

  1. Set the `NCCL_TELEMETRY_MODE` to either `1` or `4`. To learn about the `NCCL_TELEMETRY_MODE` environment variable, see Configuration options.
  2. Set one of the following export paths:

     * Set `NCCL_PROFILER_LATENCY_FILE=PATH` to export detailed event traces to a local file. Replace `PATH` with a path such as `/tmp/latency-%p.txt`.
     * Set `NCCL_PROFILER_SUMMARY_FILE=PATH` to export aggregated summary statistics. Replace `PATH` with a path such as `/tmp/summary-%p.txt`.

The system replaces `%p` with the process ID.

  3. Review the output. The raw output is a JSON file.




### Configuration options

The following sections summarize all the environment variables that you can configure for CoMMA. They also explain how to set any environment variable.

#### Set CoMMA environment variables

To set a CoMMA environment variable to a non-default value, set environment variables. You can set environment variables on the command-line for the compute instance or add them to a startup script. If you set the environment variables at the command-line, the value only persists per session. To make the environment variables permanent, place them into the `~/.bashrc` file, `~/.profile`, or whichever startup file your operating system uses. For more information, review your operating system's documentation.

You need to set CoMMA environment variables before your workload starts as the workload reads the variables during NCCL initialization. You can set environment variables as follows:
    
    
    export ENVIRONMENT_VARIABLE=VALUE
    

Replace the following:

  * `ENVIRONMENT_VARIABLE`: the environment variable you want to set; for example, `NCCL_TELEMETRY_MODE`.
  * `VALUE`: the value for the environment variable; for example, `0`.



#### CoMMA environment variables

This section lists the environment variables that you can set for CoMMA and their default values.

Name | Description | Default  
---|---|---  
`NCCL_PROFILER_AGGREGATE_STEPS` | Enables (`true`) or disables (`false`) aggregating network chunk operations. | `true`  
`NCCL_PROFILER_GPUVIZ_LIB` | Specifies the path to `libGPUViz.so`, a library that uploads NCCL telemetry to Google Cloud services. This library wraps the [agent communication API](https://github.com/GoogleCloudPlatform/agentcommunication_client). The agent communication API is the interface that agents, such as processes running within your guest operating system, use to initiate secure and reliable connections with Google Cloud services. If you use a NCCL gIB image as an installer or use any of the images that bundle [the NCCL gIB plugin](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma#auto-enabled-images), you don't need to set this environment variable. |   
`NCCL_PROFILER_LATENCY_FILE` | Specifies the path template for the latency trace file. For example, `/tmp/latency-%p.txt`. The system replaces `%p` in the name with the process ID (pid).   
  
To disable file-based export, unset this variable. |   
`NCCL_PROFILER_PLUGIN` | Specifies the path to the profiler plugin binary.  
  
If you don't specify this setting, NCCL looks for `libnccl-profiler.so` in the `LD_LIBRARY_PATH`. |   
`NCCL_PROFILER_SUMMARY_FILE` | Specifies the path for the aggregated summary file. For example, `/tmp/summary-%p.txt`. The system replaces `%p` in the name with the process ID (pid).   
  
To disable file-based export, unset this variable. |   
`NCCL_PROFILER_SUMMARY_INTERVAL` | Specifies the interval for summary reporting. For example, `10s`, `1m`. Supports `d`, `h`, `m`, `s`, `ms`, `us`, `ns` | `1m`  
`NCCL_PROFILER_TRACK_INTERPROCESS_PROXYOP` | Enables (`true`) or disables (`false`) monitoring inter-process NCCL proxy operations. | `true`  
`NCCL_PROFILER_TRACK_NCCLOP` | Enables (`true`) or disables (`false`) tracking and reporting for NCCL operations, including both collective and point-to-point communications. | `true`  
`NCCL_PROFILER_TRACK_PROXYOP` | Enables (`true`) or disables (`false`) proxy operation tracking and reporting. | `false`  
`NCCL_PROFILER_TRACK_STEPS` | Enables (`true`) or disables (`false`) tracking and reporting network chunk operations. | `false`  
`NCCL_PROFILER_HEARTBEAT` | Enables (`true`) or disables (`false`) a periodic heartbeat telemetry reporting mechanism. | `true`  
`NCCL_PROFILER_HEARTBEAT_UPLOAD_INTERVAL` | Specifies the interval for the heartbeat telemetry reporting mechanism. For example, `10s`, `1m`. Supports `d`, `h`, `m`, `s`, `ms`, `us`, `ns` | `10s`  
`NCCL_TELEMETRY_MODE` | Controls the export location of the NCCL telemetry data. The options include the following:  
  
| Value | Description  
---|---  
`0` | Disables NCCL telemetry collection.  
`1` | Exports NCCL telemetry to a local file. With this method, NCCL telemetry is unavailable to Google.  
`3` | Exports NCCL telemetry to Google services.  
`4` | Exports NCCL telemetry to both local file and Google services.  
`3`  
  
## What's next

  * Learn how to [troubleshoot issues with CoMMA](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-comma).
  * Learn how to [detect and resolve stragglers](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance).
  * Learn how to [detect unresponsive workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor#unresponsive-workload-detection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
