---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-comma/
title: Troubleshoot CoMMA issues \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:36.602616+00:00
---

# Troubleshoot CoMMA issues  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-comma/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Troubleshoot CoMMA issues Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This page shows you how to resolve common issues that you might encounter when using the Collective Communication Analyzer (CoMMA). CoMMA is a library that collects telemetry data for Google Cloud services. For more information, see [Collective Communication Analyzer (CoMMA)](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma). 

## Troubleshoot CoMMA loading issues

CoMMA might not load correctly. To verify that the binaries load correctly, complete these steps:

  1. Enable NCCL debug logging. To enable logging, set the environment variable `NCCL_DEBUG=INFO`. You might also use a more detailed debug level. For options, see the [`NCCL_DEBUG`](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html#nccl-debug) section in the NVIDIA documentation.
  2. Specify the `INIT` subsystem for debugging. To specify `INIT`, set `NCCL_DEBUG_SUBSYS=INIT`. You might also add other subsystems. For more subsystem options, see the [`NCCL_DEBUG_SUBSYS`](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html#nccl-debug-subsys) section.
  3. Look for a line in the NCCL log that is similar to the following: `NCCL INFO PROFILER/Plugin: Plugin name set by env to PATH_TO_PROFILER_PLUGIN`

If the `NCCL_PROFILER_PLUGIN` environment variable is unset, NCCL might attempt to load the `libnccl-profiler.so` binary from the path specified in the `LD_LIBRARY_PATH` environment variable.




To resolve this issue, consider the following solutions:

  * Verify that the plugin shared library (`libnccl-profiler.so`) is correctly named.

Check that it is located in a directory specified in `LD_LIBRARY_PATH` environment variable. Alternatively, check that the `NCCL_PROFILER_PLUGIN` environment variable points directly to the location of the `libnccl-profiler.so` binary.

  * Check that your NCCL version is `2.23` or later, as the NCCL profiler API requires this version.




## Troubleshoot missing output files

If you configured your environment to send data collected by CoMMA to a local file, but the output file is missing, check the NCCL logs or application logs for messages that are similar to the following:
    
    
    Failed to open file
    Failed to log <telemetry type> to file
    

These errors indicate an underlying file system issue, such as a missing directory or insufficient free space. CoMMA ceases to export telemetry to files after these errors occur.

To resolve this issue, consider these solutions:

  * Check that the `NCCL_PROFILER_LATENCY_FILE` or `NCCL_PROFILER_SUMMARY_FILE` environment variables are set correctly. Provide a valid path and filename template, such as `/tmp/latency-%p.txt`.
  * Check that the process has write permissions to the specified output directory.
  * If you modified the `NCCL_TELEMETRY_MODE` environment variable, check that you set it to a value that enables local file output (for example, `1` or `4`).



## Troubleshoot unexpected data or missing events

CoMMA might capture unexpected data or miss expected events.

To resolve this issue, check that the required [level of granularity is set](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma#set-data-granularity).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
