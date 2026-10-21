---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/machine-learning-run/create/
title: gcloud alpha mldiagnostics machine-learning-run create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:45.963623+00:00
---

# gcloud alpha mldiagnostics machine-learning-run create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/machine-learning-run/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha mldiagnostics machine-learning-run create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha mldiagnostics machine-learning-run create - create a machine learning run 
SYNOPSIS
    

`gcloud alpha mldiagnostics machine-learning-run create` (`MACHINE_LEARNING_RUN` : `--location`=`LOCATION`) [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--gcs-path`=`GCS_PATH`] [`--labels`=[`LABELS`,…]] [`--orchestrator`=`ORCHESTRATOR`] [`--run-group`=`RUN_GROUP`] [`--run-phase`=`RUN_PHASE`; default="active"] [`--tools`=[`xprof`=`XPROF`]; default="xprof"] [`--configs-hardware`=[`CONFIGS_HARDWARE`,…] `--configs-software`=[`CONFIGS_SOFTWARE`,…]] [`--workload-targets`=[`display-name`=`DISPLAY-NAME`],[`hostname`=`HOSTNAME`],[`instance-id`=`INSTANCE-ID`],[`zone`=`ZONE`] [`--custom-workload-display-name`=`CUSTOM_WORKLOAD_DISPLAY_NAME` `--custom-workload-id`=`CUSTOM_WORKLOAD_ID` : `--custom-workload-create-time`=`CUSTOM_WORKLOAD_CREATE_TIME`] | `--gke-cluster-name`=`GKE_CLUSTER_NAME` `--gke-kind`=`GKE_KIND` `--gke-namespace`=`GKE_NAMESPACE` `--gke-workload-create-time`=`GKE_WORKLOAD_CREATE_TIME` `--gke-workload-name`=`GKE_WORKLOAD_NAME` | `--slurm-cluster-name`=`SLURM_CLUSTER_NAME` `--slurm-job-id`=`SLURM_JOB_ID` `--slurm-job-name`=`SLURM_JOB_NAME` `--slurm-job-submit-time`=`SLURM_JOB_SUBMIT_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a machine learning run. 
EXAMPLES
     To create the new machine learning run, run: 
    
    
    gcloud alpha mldiagnostics machine-learning-run create gcloud-cli-run-id-01 --orchestrator gke --run-group group-gcloud-cli --tools xprof --gcs-path gs://diagon-prod-data-bucket --display-name gcloud-cli-run --gke-cluster-name projects/PROJECT_ID/locations/us-central1/clusters/mldiag-prod-gke-cluster projects/PROJECT_ID/locations/us-central1/clusters/mldiag-prod-gke-cluster --gke-namespace diagon --gke-workload-name mldiag-prod-demo-jobset --gke-kind JobSet --gke-workload-create-time 2026-02-20T06:00:00Z --labels "created_by"="cli" --run-phase ACTIVE
    
    
    Sample output:
      Create request issued for: [gcloud-cli-run-id-01]
      Waiting for operation [projects/PROJECT_ID/locations/us-central1/operations/operation-1770308728284-64a161ee4640d-38e79884-425e56e2] to complete…done.
      Created machine_learning_run [gcloud-cli-run-id-01].
    
    
    If user want to list all the profiler session capture in Google Cloud Storage bucket (recursively), create a special machine learning run with a special lable `list_existing_sessions_only` as shown below:
    
    
    gcloud alpha mldiagnostics machine-learning-run create gcloud-cli-run-id-02 --run-group group-gcloud-cli --gcs-path gs://diagon-prod-data-bucket/my-parent-directory --display-name gcloud-cli-run-02 --labels "created_by"="cli" --labels "list_existing_sessions_only"="true"
    
    
    This will create a machine learning run in COMPLETED state without any workload
    details. User can navigate to the profiler list page to see all the
    profiler sessions captured under gs://diagon-prod-data-bucket/my-parent-directory (recursively).
    User can visualize any profiler session by passing the link and share it with others.
    No further update is possible for this machine learning run as it is marked as COMPLETED.

POSITIONAL ARGUMENTS
    

Machine learning run resource - Identifier. The name of the Machine Learning run. If not provided, a random UUID will be generated. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `machine_learning_run` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MACHINE_LEARNING_RUN`
     ID of the machine_learning_run or fully qualified identifier for the machine_learning_run. 

To set the `machine_learning_run` attribute: 

  * provide the argument `machine_learning_run` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the machine_learning_run resource. 

To set the `location` attribute: 

  * provide the argument `machine_learning_run` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/region`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     Display name for the run. 
Represents information about the artifacts of the Machine Learning Run. 
`--gcs-path`=`GCS_PATH`
     The Cloud Storage path where the artifacts of the run are stored. Example: `gs://my-bucket/my-run-directory`. 
`--labels`=[`LABELS`,…]
     Any custom labels for this run Example: type:workload, type:simulation etc. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

`--orchestrator`=`ORCHESTRATOR`
     The orchestrator used for the run. `ORCHESTRATOR` must be one of: 

`custom`
     Custom orchestrator with Single/Multiple Compute Engine instances. 
`gke`
     Google Kubernetes Engine orchestrator. 
`slurm`
     Slurm cluster orchestrator. 
`--run-group`=`RUN_GROUP`
     Allows grouping of similar runs. 

  * Helps improve UI rendering performance. 
  * Allows comparing similar runs via fast filters. 


`--run-phase`=`RUN_PHASE`; default="active"
     RunPhase defines the phase of the run. This should be used only if non standard machine learning run needs to be created. If not specified, run phase will be set to active by default. `RUN_PHASE` must be one of: 

`active`
     Run is active. 
`completed`
     Run is completed. 
`failed`
     Run is failed. 
`--tools`=[`xprof`=`XPROF`]; default="xprof"
     List of tools enabled for this run. This is a repeated argument, and each instance configures one tool. If no tools are specified, XProf will be used by default by the service. 

To enable XProf without a specific session ID: `--tools=xprof` To enable XProf with a specific session ID: `--tools=xprof:sessionId=my-session-id` To enable multiple tools, repeat the argument: `--tools=xprof:sessionId=123 --tools=nsys`. 

`xprof`
     Configuration for the XProf tool. 

`sessionId`
     The session ID for XProf. Example: `my-session-id`. 
`Shorthand Example:`
    
    
    --tools=xprof={sessionId=string} --tools=xprof={sessionId=string}

`JSON Example:`
    
    
    --tools='[{"xprof": {"sessionId": "string"}}]'

`File Example:`
    
    
    --tools=path_to_file.(yaml|json)

Configuration for a Machine Learning run. 
`--configs-hardware`=[`CONFIGS_HARDWARE`,…]
     Hardware configs. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --configs-hardware=string=string

`JSON Example:`
    
    
    --configs-hardware='{"string": "string"}'

`File Example:`
    
    
    --configs-hardware=path_to_file.(yaml|json)

`--configs-software`=[`CONFIGS_SOFTWARE`,…]
     Software configs. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --configs-software=string=string

`JSON Example:`
    
    
    --configs-software='{"string": "string"}'

`File Example:`
    
    
    --configs-software=path_to_file.(yaml|json)

Workload details associated for the Machine Learning Run. Workload have different metadata based on the orchestrator like GKE cluster, Slurm cluster, Compute Engine instance etc. 
`--workload-targets`=[`display-name`=`DISPLAY-NAME`],[`hostname`=`HOSTNAME`],[`instance-id`=`INSTANCE-ID`],[`zone`=`ZONE`]
     List of targets/hosts associated with the workload. 

`display-name`
     Display name of the target/host. 
`hostname`
     Hostname of the VM. 
`instance-id`
     Target identifier of the VM. 
`zone`
     Zone of the target, e.g., `us-central1-a`. 
`Shorthand Example:`
    
    
    --workload-targets=display-name=string,hostname=string,instance-id=string,zone=string --workload-targets=display-name=string,hostname=string,instance-id=string,zone=string

`JSON Example:`
    
    
    --workload-targets='[{"display-name": "string", "hostname": "string", "instance-id": "string", "zone": "string"}]'

`File Example:`
    
    
    --workload-targets=path_to_file.(yaml|json)

Arguments for the metadata. 

At most one of these can be specified: 

Workload details for workload running on custom orchestrator. 
`--custom-workload-display-name`=`CUSTOM_WORKLOAD_DISPLAY_NAME`
     The display name of the workload. Example - training-workload 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-workload-id`=`CUSTOM_WORKLOAD_ID`
     The identifier of the workload. Example - "1234567890" 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-workload-create-time`=`CUSTOM_WORKLOAD_CREATE_TIME`
     The create timestamp of the workload. Example - 2026-02-20T06:00:00Z 
Workload details for the GKE orchestrator. 
`--gke-cluster-name`=`GKE_CLUSTER_NAME`
     The cluster of the workload. Example - /projects/<project id>/locations/<location>/clusters/<cluster name>
`--gke-kind`=`GKE_KIND`
     The kind of the workload. Example - JobSet 
`--gke-namespace`=`GKE_NAMESPACE`
     The namespace of the workload. Example - default 
`--gke-workload-create-time`=`GKE_WORKLOAD_CREATE_TIME`
     The create timestamp of the workload. Example - 2026-02-20T06:00:00Z 
`--gke-workload-name`=`GKE_WORKLOAD_NAME`
     The identifier of the workload. Example - jobset-abcd 
Workload details for the Slurm orchestrator. 
`--slurm-cluster-name`=`SLURM_CLUSTER_NAME`
     The cluster of the slurm job. Example - /projects/<project id>/locations/<location>/clusters/<cluster name>
`--slurm-job-id`=`SLURM_JOB_ID`
     The identifier of the slurm job. Example - 1234567890 
`--slurm-job-name`=`SLURM_JOB_NAME`
     The display name of the slurm job (job_name). Example - training-workload 
`--slurm-job-submit-time`=`SLURM_JOB_SUBMIT_TIME`
     The time when the slurm job was submitted. Example - 2026-02-20T06:00:00Z 
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
