---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/monitored-events/describe/
title: gcloud alpha mldiagnostics monitored-events describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:05:32.903592+00:00
---

# gcloud alpha mldiagnostics monitored-events describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/monitored-events/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha mldiagnostics monitored-events describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha mldiagnostics monitored-events describe - display the details of a specific monitored event 
SYNOPSIS
    

`gcloud alpha mldiagnostics monitored-events describe` (`MONITORED_EVENT` : `--location`=`LOCATION` `--machine-learning-run`=`MACHINE_LEARNING_RUN`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Display the details of a specific monitored event. 
EXAMPLES
     To get details of a specific monitored event, run: 
    
    
    gcloud alpha mldiagnostics monitored-events describe abc-123-def-456 --location=us-central1 --machine-learning-run=my-run-123 --format=json
    
    
    Sample output:
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

POSITIONAL ARGUMENTS
    

MonitoredEvent resource - projects/{project}/locations/{location}/machineLearningRuns/{machineLearningRun}/monitoredEvents/{monitoredEvent} The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `monitored_event` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MONITORED_EVENT`
     ID of the monitoredEvent or fully qualified identifier for the monitoredEvent. 

To set the `monitored_event` attribute: 

  * provide the argument `monitored_event` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the monitoredEvent resource. 

To set the `location` attribute: 

  * provide the argument `monitored_event` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/region`. 


`--machine-learning-run`=`MACHINE_LEARNING_RUN`
     The machine learning run id of the monitoredEvent resource. 

To set the `machine-learning-run` attribute: 

  * provide the argument `monitored_event` on the command line with a fully specified name; 
  * provide the argument `--machine-learning-run` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `hypercomputecluster/v1alpha` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/cluster-director/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
