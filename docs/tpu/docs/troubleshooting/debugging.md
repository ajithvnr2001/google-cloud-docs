---
url: https://docs.cloud.google.com/tpu/docs/troubleshooting/debugging/
title: Debugging Cloud TPU VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:19.240628+00:00
---

# Debugging Cloud TPU VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/troubleshooting/debugging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Debugging Cloud TPU VMs

This document describes how to use the [cloud-tpu-diagnostics](https://pypi.org/project/cloud-tpu-diagnostics/) PyPI package to generate stack traces for processes running in TPU VMs. This package dumps the Python traces when a fault occurs, for example segmentation faults, floating-point exceptions, or illegal operation exceptions. Additionally, it also periodically collects stack traces to help you debug situations when the program is unresponsive.

To use the [cloud-tpu-diagnostics](https://pypi.org/project/cloud-tpu-diagnostics/) PyPI package, you must install it by running `pip install cloud-tpu-diagnostics` on all TPU VMs. You can do this with one `gcloud compute tpus tpu-vm ssh` command. For example:
    
    
      gcloud compute tpus tpu-vm ssh you-tpu-name \
      --zone=your-zone \
      --project=your-project-name \
      --worker=all \
      --command="pip install cloud-tpu-diagnostics"

You must also add the following code to your scripts running on all TPU VMs.
    
    
    from cloud_tpu_diagnostics import diagnostic
    from cloud_tpu_diagnostics.configuration import debug_configuration
    from cloud_tpu_diagnostics.configuration import diagnostic_configuration
    from cloud_tpu_diagnostics.configuration import stack_trace_configuration
    
    stack_trace_config = stack_trace_configuration.StackTraceConfig(
                          collect_stack_trace = True,
                          stack_trace_to_cloud = True)
    debug_config = debug_configuration.DebugConfig(
                    stack_trace_config = stack_trace_config)
    diagnostic_config = diagnostic_configuration.DiagnosticConfig(
                          debug_config = debug_config)
    

By default, stack traces are collected every 10 minutes. You can change the duration between two stack trace collection events to 5 minutes, for example:
    
    
    stack_trace_config = stack_trace_configuration.StackTraceConfig(
                          collect_stack_trace = True,
                          stack_trace_to_cloud = True,
                          stack_trace_interval_seconds = 300)
    

Wrap your main method with `diagnose()` to periodically collect the stack traces:
    
    
    with diagnostic.diagnose(diagnostic_config):
        run_main()
    

This configuration starts collecting stack traces inside the `/tmp/debugging` directory on each TPU VM. There is an agent running on all TPU VMs that uploads the traces from a temporary directory to Cloud Logging.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
