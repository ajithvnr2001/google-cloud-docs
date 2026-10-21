---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/machine-learning-run/describe/
title: gcloud alpha mldiagnostics machine-learning-run describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:05:32.364860+00:00
---

# gcloud alpha mldiagnostics machine-learning-run describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/machine-learning-run/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha mldiagnostics machine-learning-run describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha mldiagnostics machine-learning-run describe - view the details of a machine learning run 
SYNOPSIS
    

`gcloud alpha mldiagnostics machine-learning-run describe` (`MACHINE_LEARNING_RUN` : `--location`=`LOCATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` View the details of a machine learning run resource. 
EXAMPLES
     To get details of the machine learning run, run: 
    
    
    gcloud alpha mldiagnostics machine-learning-run describe my-run --location=us-central1 --format json
    
    
    Sample output:
      {
        "artifacts": {
          "gcsPath": "gs://diagon-prod-data"
        },
        "createTime": "2026-02-05T16:25:28.367865234Z",
        "displayName": "gcloud-cli-run",
        "endTime": "0001-01-01T00:00:00Z",
        "etag": "1f54a7f4-bd25-4f98-a91c-97bfa1c5b7a6",
        "labels": {
          "on_demand_xprof": "enabled"
        },
        "name": "projects/PROJECT_ID/locations/us-central1/machineLearningRuns/my-run",
        "orchestrator": "GKE",
        "runPhase": "ACTIVE",
        "runSet": "group-gcloud-cli",
        "tools": [
          {
            "xprof": {}
          }
        ],
        "updateTime": "2026-02-05T16:25:28.367865344Z",
        "workloadDetails": {
          "gke": {
            "cluster": "projects/PROJECT_ID/locations/us-central1/clusters/mldiag-prod-cluster",
            "id": "mldiag-prod-demo-jobset",
            "kind": "JobSet",
            "namespace": "diagon"
          }
        }
      }
    `

POSITIONAL ARGUMENTS
    

Machine learning run resource - projects/{project}/locations/{location}/machineLearningRuns/{machineLearningRun} The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `hypercomputecluster/v1alpha` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/cluster-director/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
