---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/profiler-session/capture/
title: gcloud alpha mldiagnostics profiler-session capture \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:17.308413+00:00
---

# gcloud alpha mldiagnostics profiler-session capture  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/profiler-session/capture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha mldiagnostics profiler-session capture Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha mldiagnostics profiler-session capture - capture profiler sessions 
SYNOPSIS
    

`gcloud alpha mldiagnostics profiler-session capture` `PROFILER_SESSION` `--targets`=[`TARGETS`,…] [`--async`] [`--device-tracer-level`=`DEVICE_TRACER_LEVEL`; default="device-tracer-level-enabled"] [`--duration`=`DURATION`] [`--host-tracer-level`=`HOST_TRACER_LEVEL`; default="host-tracer-level-info"] [`--is-trace-enabled`] [`--kind`=`KIND`; default="on-demand"] [`--location`=`LOCATION`] [`--machine-learning-run`=`MACHINE_LEARNING_RUN`] [`--python-tracer-level`=`PYTHON_TRACER_LEVEL`; default="python-tracer-level-disabled"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Capture a profiler session 
EXAMPLES
     To capture the profiler session, run: 
    
    
    gcloud alpha mldiagnostics profiler-session capture on-demand-session --location=us-central1 --machine-learning-run=my-ml-run --targets mldiag-prod-demo-jobset-tpu-slice-0-0-qmx7s --duration 5000ms
    
    
    Sample output:
      Request issued for: [on-demand-session]
      Waiting for operation [projects/PROJECT_ID/locations/us-central1operations/operation-1770310771938-64a1698b41364-06f905e7-8eab435b] to complete…done.
      createTime: '2026-02-05T16:59:32.307511739Z'
      deviceTracerLevel: DEVICE_TRACER_LEVEL_ENABLED
      duration: 5000s
      etag: d3f59473-ad4c-47f3-b64b-6855575ab622
      hostTracerLevel: HOST_TRACER_LEVEL_INFO
      name: projects/PROJECT_ID/locations/us-central1machineLearningRuns/mldiag-prod-cluster-diagon-jobset-mldiag-prod-demo-jobset-20260205-164642/profilerSessions/on-demand-session
      profilerTargets:
      - projects/PROJECT_ID/locations/us-central1machineLearningRuns/mldiag-prod-cluster-diagon-jobset-mldiag-prod-demo-jobset-20260205-164642/profilerTargets/mldiag-prod-demo-jobset-tpu-slice-0-0-qmx7s
      pythonTracerLevel: PYTHON_TRACER_LEVEL_DISABLED
      storageFolderUri: gs://diagon-prod-data/mldiag-prod-cluster-diagon-jobset-mldiag-prod-demo-jobset-20260205-164642          ```

POSITIONAL ARGUMENTS
    

ProfilerSession resource - Identifier. The name of the profiler session. Format: projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}/profilerSessions/{profiler_session} This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `profiler_session` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `profiler_session` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/region`. 



To set the `machine-learning-run` attribute: 

  * provide the argument `profiler_session` on the command line with a fully specified name; 
  * provide the argument `--machine-learning-run` on the command line. 



This must be specified. 

`PROFILER_SESSION`
     ID of the profilerSession or fully qualified identifier for the profilerSession. 

To set the `profiler_session` attribute: 

  * provide the argument `profiler_session` on the command line. 


REQUIRED FLAGS
    

ProfilerTarget resource - Profiler targets on which profiler session to be started. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--targets` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--targets` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/region`. 



To set the `machine-learning-run` attribute: 

  * provide the argument `--targets` on the command line with a fully specified name; 
  * provide the argument `--machine-learning-run` on the command line. 



This must be specified. 

`--targets`=[`TARGETS`,…]
     IDs of the profilerTargets or fully qualified identifiers for the profilerTargets. 

To set the `profiler-target` attribute: 

  * provide the argument `--targets` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--device-tracer-level`=`DEVICE_TRACER_LEVEL`; default="device-tracer-level-enabled"
     Device tracer level for the session. If the field is not set or unspecified, the default is `DEVICE_TRACER_LEVEL_ENABLED`. `DEVICE_TRACER_LEVEL` must be one of: 

`device-tracer-level-disabled`
     Tracer level is disabled. 
`device-tracer-level-enabled`
     Tracer level is enabled. 
`--duration`=`DURATION`
     Duration for the profiler session. 
`--host-tracer-level`=`HOST_TRACER_LEVEL`; default="host-tracer-level-info"
     Host tracer level for the session. If the field is not set or unspecified, the default is `HOST_TRACER_LEVEL_INFO`. `HOST_TRACER_LEVEL` must be one of: 

`host-tracer-level-critical`
     Tracer level is critical. 
`host-tracer-level-disabled`
     Tracer level is disabled. 
`host-tracer-level-info`
     Tracer level is info. 
`host-tracer-level-verbose`
     Tracer level is verbose. 
`--is-trace-enabled`
     Customer setting to enable trace level details for the session. 
`--kind`=`KIND`; default="on-demand"
     Profiler session kind. `KIND` must be one of: 

`on-demand`
     Profiler session created via Command Line Interface / UI / API on demand request. 
`snapshot`
     Profiler session is created via continuous profiling flow to capture a snapshot. 
`--location`=`LOCATION`
     For resources [profiler_session, targets], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--machine-learning-run`=`MACHINE_LEARNING_RUN`
     For resources [profiler_session, targets], provides fallback value for resource machine-learning-run attribute. When the resource's full URI path is not provided, machine-learning-run will fallback to this flag value. 
`--python-tracer-level`=`PYTHON_TRACER_LEVEL`; default="python-tracer-level-disabled"
     Python tracer level for the session. If the field is not set or unspecified, the default is `PYTHON_TRACER_LEVEL_DISABLED`. `PYTHON_TRACER_LEVEL` must be one of: 

`python-tracer-level-disabled`
     Tracer level is disabled. 
`python-tracer-level-enabled`
     Tracer level is enabled. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `hypercomputecluster/v1alpha` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/cluster-director/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
