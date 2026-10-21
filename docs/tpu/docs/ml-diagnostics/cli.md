---
url: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/cli/
title: Get started with the ML Diagnostics CLI \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:02.915795+00:00
---

# Get started with the ML Diagnostics CLI  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get started with the ML Diagnostics CLI

Use the ML Diagnostics Google Cloud CLI to create and manage machine learning runs, deploy [XProf](https://openxla.org/XProf) as a managed instance with a scalable backend, and provide a managed profiling experience on Google Cloud. You can also list all events detected by workload monitoring and get analyzer details for these events through the CLI or API.

There are three categories of ML Diagnostics gcloud CLI commands: `machine-learning-run`, `profiler`, and `monitored-events` commands. Use the `machine-learning-run` commands to create, delete, describe, list, and update machine learning runs. Use the `profiler` commands to list nodes and capture on-demand profiles from the CLI. Use the `monitored-events` commands to list all events detected by workload monitoring, and receive analyzer details for each event.

  * `Machine-learning-run` commands: `Create`, `Delete`, `Describe`, `List`, `Update`.
  * `Monitored-events` commands: `Describe`, `List`
  * Profiler commands: 
    * `profiler-target`: `List`
    * `profiler-session`: `Capture`, `List`



All gcloud CLI commands require a project defined in the environment. To set the project:
    
    
    gcloud config set project PROJECT_ID
    

For more information on the ML Diagnostics gcloud CLI commands, see the [API reference](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics).

## Capture profiles

You can capture XProf profiles of your ML workload with programmatic capture or on-demand capture (manual capture). Programmatic capture involves embedding profiling commands directly into your machine learning code, and explicitly stating when to start and stop recording data. On-demand capture occurs in real-time, where you trigger the profiler while the workload is already actively running.

To enable on-demand profile capture, you need to start the XProf server within your code and call the `profiler.start_server` method. This starts an XProf server on your ML workload that listens for the on-demand capture trigger to start capturing profiles. Use port 9999 for this command: `profiler.start_server(port=9999)`

For both programmatic and on-demand profile capture, specify the location to store the captured profiles. For example: `gs://my-bucket/my-run`. Profiles are stored in directories nested within the location:`gs://my-bucket/my-run/plugins/profile/session1/`. Programmatic profile capture and on-demand capture must not occur during the same time period.

For on-demand profile capture, set up a GKE cluster which installs `connection-operator`. For Programmatic profile capture, set up a GKE cluster which installs `injection-webhook`, using the ML Diagnostics SDK and labeling the workload.

For more information about profiling with JAX, see [Profiling computation](https://docs.jax.dev/en/latest/profiling.html).

## Create machine learning run

Create a machine learning run resource in a specified project and location. The `machine-learning-run create` command deploys XProf as a managed instance in your project. The managed XProf instance is used for viewing all profiles in the project, and is created when the first machine learning run is created in the project.

Use the `machine-learning-run create` command:
    
    
    gcloud alpha mldiagnostics machine-learning-run create
    

There are two ways to create a machine learning run:

  * Register existing captured profiles to the ML Diagnostics platform.
  * Use ML Diagnostics to perform on-demand profile capture by registering an active run. This requires a GKE cluster setup.



### Create ML Run and register existing captured profiles

The following code creates a run and registers existing captured profiles to ML Diagnostics:
    
    
    gcloud alpha mldiagnostics machine-learning-run create RUN_NAME \
      --location LOCATION \
      --run-group GROUP_NAME \
      --gcs-path gs://BUCKET_NAME \
      --display-name DISPLAY_NAME \
      --labels "list_existing_sessions_only"="true"
    

The code example uses the following flags:

Flag | Requirement | Description  
---|---|---  
`machine-learning-run` | Required |  A unique identifier for this specific run. If the name is not unique, the run creation fails with the message: "ML Run already exists".   
`location` | Required | All [Cluster Director locations](https://docs.cloud.google.com/cluster-director/docs/locations) are supported except `us-east5`. This flag can be set by an argument for each command, or with the command: `gcloud config set compute/region`.  
`gcs-path` | Required | The Google Cloud Storage location where all profiles are saved. For example: `gs://my-bucket` or `gs://my-bucket/folder1`. Required only if the SDK is used for profile capture.   
`run-group` | Optional | An identifier that can help group multiple runs belonging to the same experiment. For example, all runs associated with a TPU slice size sweep could belong to the same group.  
`display-name` | Optional |  Display name for the machine learning run. If not provided, it is set to machine learning run ID.   
  
The `--labels list_existing_sessions_only=true` flag is required if you want to view and manage existing collected profiles in ML Diagnostics. The flag does the following:

  1. Creates a machine learning run with state "Completed".
  2. Recursively searches for [xplane.pb](https://pypi.org/project/tensorboard-plugin-profile/) files within the Cloud Storage directory path.
  3. Loads all located profile sessions into the ML Diagnostics database to view in Google Cloud, creates shareable links for the profile sessions, and allows users to manage these profiles with ML Diagnostics platform.



If the `--labels list_existing_sessions_only` flag is set to `true` for a run, you cannot perform on-demand profiling or update the run. You can only view and manage existing profiles.

### Create ML Run to perform on-demand profile capture

The following code creates an `mlrun` in order perform on-demand profile capture:
    
    
    gcloud alpha mldiagnostics machine-learning-run create RUN_NAME \
      --location LOCATION \
      --orchestrator gke \
      --run-group RUN_GROUP \
      --gcs-path gs://BUCKET_NAME \
      --display-name DISPLAY_NAME \
      --gke-cluster-name projects/user/locations/LOCATION/clusters/CLUSTER_NAME \
      --gke-namespace NAMESPACE \
      --gke-workload-name WORKLOAD_NAME \
      --gke-kind GKE_KIND \
      --gke-workload-create-time CREATE_TIME \
      --run-phase RUN_PHASE
    

Along with the flags from the previous example, the code example uses the following additional flags:

Flag | Requirement | Description  
---|---|---  
`orchestrator` | Optional |  The orchestrator used for the run. If not specified, `gke` is used by default. Valid values: `gce`, `gke`, `slurm`.   
`gke-cluster-name` | Required for GKE |  The cluster of the workload. For example: `/projects/<project_id>/locations/<location>/clusters/<cluster_name>`.   
`gke-kind` | Required for GKE |  The kind of the workload. For example: `JobSet`.   
`gke-namespace` | Required for GKE |  The namespace of the workload. For example: `default`.   
`gke-workload-name` | Required for GKE |  The identifier of the workload. For example: `jobset-abcd`.   
`gke-workload-create-time` | Required for GKE |  The creation timestamp for a JobSet in ISO timestamp format. For example: `2026-02-20T06:00:00Z`.   
`run-phase` | Optional |  Phase and state of a run. If not provided, it is `ACTIVE` by default.   
  
## Describe machine learning run

View the details of a machine learning run with the `machine-learning-run describe` command:
    
    
    gcloud alpha mldiagnostics machine-learning-run describe RUN_NAME --FORMAT=FORMAT
    

The following example is a request for run details in JSON:
    
    
    gcloud alpha mldiagnostics machine-learning-run describe my-run-on-demand \
      --format json
    

The output is similar to the following:
    
    
    {
      "artifacts": {
        "gcsPath": "gs://my-bucket"
      },
      "createTime": "2026-02-05T16:25:28.367865234Z",
      "displayName": "mldiagnostics-my-run-on-demand",
      "endTime": "0001-01-01T00:00:00Z",
      "etag": "1f54a7f4-bd25-4f98-a91c-97bfa1c5b7a6",
       "name": "projects/163028815180/locations/us-central1/machineLearningRuns/my-run-on-demand",
      "orchestrator": "GKE",
      "runPhase": "ACTIVE",
      "runSet": "my-run-on-demand-group",
      "tools": [
        {
          "XProf": {}
        }
      ],
      "updateTime": "2026-02-05T16:25:28.367865344Z",
      "workloadDetails": {
        "gke": {
          "cluster": "projects/163028815180/locations/us-central1/clusters/my-cluster",
          "id": "jobset-abcd",
          "kind": "JobSet",
          "namespace": "default"
        }
      }
    }
    

## List machine learning runs

Get a list of machine learning runs within a specified project and location with the `machine-learning-run list` command:
    
    
    gcloud alpha mldiagnostics machine-learning-run list
    

The following example is a request for a list of up to two runs, with outputs of their URI paths:
    
    
    gcloud alpha mldiagnostics machine-learning-run list --limit 2 --uri
    
    
    
    https://hypercomputecluster.googleapis.com/v1alpha/projects/163028815180/locations/us-central1/machineLearningRuns/my-run-on-demand
    https://hypercomputecluster.googleapis.com/v1alpha/projects/163028815180/locations/us-central1/machineLearningRuns/my-run-on-demand-2
    

## Update machine learning runs

Update a machine learning run in a specified project and location. You can update the display name, run phase, orchestrator, and GKE workload details. You cannot change the run ID and location. Update a run with the `machine-learning-run update` command:
    
    
    gcloud alpha mldiagnostics machine-learning-run update
    

Provide all fields that were included in the `create` request. If mandatory fields are not provided during update request, they are overridden by the default values.

The `etag` flag is a mandatory field, and should be the latest ETag (entity tag) value for an ML Run resource. For more information, see [Use entity tags for optimistic concurrency control](https://docs.cloud.google.com/secret-manager/docs/etags). Use the following to find the correct ETAG value:
    
    
    gcloud alpha mldiagnostics machine-learning-run describe RUN_NAME
    

The following is an example of a complete update request:
    
    
    gcloud alpha mldiagnostics machine-learning-run update my-run-on-demand \
      --orchestrator gke \
      --run-group my-run-on-demand-group \
      --gcs-path gs://my-bucket \
      --display-name mldiagnostics-my-run-on-demand-completed \
      --gke-cluster-name projects/user/locations/us-central1/clusters/my-cluster \
      --gke-namespace default \
      --gke-workload-name jobset-abcd \
      --gke-kind JobSet \
      --gke-workload-create-time 2026-02-20T06:06:06Z \
      --run-phase COMPLETED \
      --etag 1f54a7f4-bd25-4f98-a91c-97bfa1c5b7a6
    

## Delete machine learning runs

Delete a machine learning run in a specified project and location with the `machine-learning-run delete` command:
    
    
    gcloud alpha mldiagnostics machine-learning-run delete RUN_NAME
    

Deleting an ML run does not delete any data in Cloud Storage, Cloud Logging, or the GKE workload. Deleting the `mlrun` only deletes metadata related to the run within the ML Diagnostics system.

## Profiler commands

You can use the profiler command group to list all profiles, find GKE nodes of workload where the XProf server is running, and capture on-demand profiles from the CLI.

### List profiler targets

List all profiler targets associated with a machine learning run in a specified project and location:
    
    
    gcloud alpha mldiagnostics profiler-target list --machine-learning-run RUN_NAME
    

This command requires the following:

  * On-demand Xprof is enabled in the workload, which deploys XProf server into all nodes of the workload.
  * GKE cluster is set up for ML Diagnostics, with deployed webhook and operator.
  * Deployed workload on GKE.



The following is an example of a request:
    
    
    gcloud alpha mldiagnostics profiler-target list \
      --machine-learning-run my-run-on-demand
    

The following is an example of the output:
    
    
    ---
    hostname: gke-tpu-1f0789b5-jqx9
    name: projects/163028815180/locations/us-central1/machineLearningRuns/my-run-on-demand/profilerTargets/jobset-abcd-tpu-slice-0-0-tcw2k
    ---
    hostname: gke-tpu-1f0789b5-rxvf
    name: projects/163028815180/locations/us-central1/machineLearningRuns/my-run-on-demand/profilerTargets/jobset-abcd-tpu-slice-0-1-dct59
    

### List profiler sessions

List all profiler sessions associated with a machine learning run in a specified project and location with the following command:
    
    
    gcloud alpha mldiagnostics profiler-session list --machine-learning-run RUN_NAME
    

This profiler command does not require GKE or workload setup. It will list all profile sessions, both programmatic and on-demand. If you only have programmatic profile captures, use this command to list all profile sessions. There is no required GKE setup, GKE workload labeling, or on-demand XProf enablement.

The following is an example of a request:
    
    
    gcloud alpha mldiagnostics profiler-session list \
      --machine-learning-run my-run-on-demand
    

## Capture on-demand profiler sessions

You can capture an on-demand profiler session for a machine learning run on a specified set of nodes that the workload is running on (profiler targets).

This command requires the following:

  * On-demand XProf is enabled in the workload, which deploys XProf server into all nodes of the workload
  * GKE cluster is set up for ML Diagnostics, with deployed webhook and operator
  * Deployed workload on GKE.



The following is an example of a request:
    
    
    gcloud alpha mldiagnostics profiler-session capture \
      profiler-session-on-demand \
      --machine-learning-run RUN_NAME \
      --targets TARGET \
      --duration DURATION
    

The example uses the following flags:

Flag | Requirement | Description  
---|---|---  
`profiler-session-name` | Required |  Name of profiler session to be captured.   
`duration` | Required |  Duration for the profiler session capture. It is of `Duration` type. For example, specify a duration of `1s` for 1 second, `400ms` for 400 milliseconds, and `5m` for 5 minutes.   
`targets` | Required |  IDs of the profiler targets or fully qualified identifiers for the profiler-targets. Must match with a list of targets associated with the run.   
`device-tracer-level` | Optional |  Device tracer level for the session. Accepted values: `device-tracer-level-enabled`, `device-tracer-level-disabled` (default).   
`host-tracer-level` | Optional |  Host tracer level for the session. Accepted values: `host-tracer-level-info` (default), `host-tracer-level-critical`, `host-tracer-level-disabled`, `host-tracer-level-verbose`.   
`python-tracer-level` | Optional |  Python tracer level for the session. Accepted values: `python-tracer-level-disabled` (default), `python-tracer-level-enabled`.   
  
## Monitored-events commands

You can use `monitored-events` commands to list all events detected by workload monitoring and to get analyzer details for each of the events.

### List monitored-events

List all events detected by workload monitoring associated with a machine learning run.

The following is an example of a request:
    
    
    gcloud alpha mldiagnostics monitored-events list \
     --machine-learning-run=my-run-123 \
     --location=us-central1 \
     --project=PROJECT_ID \
     --format=json
    

The following is an example of the output:
    
    
    [
     {
       "displayName": "Performance degradation - 2026-05-01T12:00:00Z",
       "endTime": "2026-05-01T12:10:00Z",
       "name": "projects/PROJECT_ID/locations/us-central1/machineLearningRuns/my-run-123/monitoredEvents/abc-123-def-456",
       "startTime": "2026-05-01T12:00:00Z",
       "type": "PERFORMANCE_DEGRADATION"
     },
     {
       "displayName": "Performance degradation - 2026-06-27T07:35:00Z",
       "endTime": "2026-06-27T08:15:00Z",
       "name": "projects/PROJECT_ID/locations/us-central1/machineLearningRuns/my-run-123/monitoredEvents/abc-789-def-123",
       "startTime": "2026-06-27T07:35:00Z",
       "type": "PERFORMANCE_DEGRADATION"
       }
       // ... other events
    ]
    

### Describe monitored-events

Get analyzer details for each of the events detected by workload monitoring associated with a machine learning run.

The following is an example of a request:
    
    
    gcloud alpha mldiagnostics monitored-events describe abc-123-def-456 \
     --machine-learning-run=my-run-123 \
     --location=us-central1 \
     --project=PROJECT_ID \
     --format=json
    

The following is an example of the output:
    
    
    {
     "analyzerReports": [
       {
         "analyzer": "ICI Link Analyzer",
         "detectionState": "DETECTED",
         "details": "ICI Link issues detected in <instance_ids>: This indicates networking issues on ICI links connected between TPU processors.",
         "recommendedActions": [
           {
             "description": "Contact Google team for further diagnosis. Potential action could be to Outkast affected nodes, but there could be other causes that need further investigation.",
             "documentationUrl": "https://docs.cloud.google.com/tpu/docs/ml-diagnostics/workload-monitoring"
           }
         ]
       }
     ],
     "displayName": "Performance degradation - 2026-05-01T12:00:00Z",
     "endTime": "2026-05-01T12:10:00Z",
     "name": "projects/PROJECT_ID/locations/us-central1/machineLearningRuns/my-run-123/monitoredEvents/abc-123-def-456",
     "startTime": "2026-05-01T12:00:00Z",
     "type": "PERFORMANCE_DEGRADATION"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
