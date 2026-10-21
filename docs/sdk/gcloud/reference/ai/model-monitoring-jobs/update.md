---
url: https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update/
title: gcloud ai model-monitoring-jobs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:50.146375+00:00
---

# gcloud ai model-monitoring-jobs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud ai model-monitoring-jobs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud ai model-monitoring-jobs update - update an Vertex AI model deployment monitoring job 
SYNOPSIS
    

`gcloud ai model-monitoring-jobs update` (`MONITORING_JOB` : `--region`=`REGION`) [`--analysis-instance-schema`=`ANALYSIS_INSTANCE_SCHEMA`] [`--[no-]anomaly-cloud-logging`] [`--display-name`=`DISPLAY_NAME`] [`--emails`=[`EMAILS`,…]] [`--log-ttl`=`LOG_TTL`] [`--monitoring-frequency`=`MONITORING_FREQUENCY`] [`--notification-channels`=[`NOTIFICATION_CHANNELS`,…]] [`--prediction-sampling-rate`=`PREDICTION_SAMPLING_RATE`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--monitoring-config-from-file`=`MONITORING_CONFIG_FROM_FILE` | `--feature-attribution-thresholds`=[`KEY`=`VALUE`,…] `--feature-thresholds`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an Vertex AI model deployment monitoring job. 
EXAMPLES
     To update display name of model deployment monitoring job `123` under project `example` in region `us-central1`, run: 
    
    
    gcloud ai model-monitoring-jobs update 123 --display-name=new-name --project=example --region=us-central1

POSITIONAL ARGUMENTS
    

Monitoring job resource - The model deployment monitoring job to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `monitoring_job` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MONITORING_JOB`
     ID of the monitoring_job or fully qualified identifier for the monitoring_job. 

To set the `name` attribute: 

  * provide the argument `monitoring_job` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the monitoring_job. 

To set the `region` attribute: 

  * provide the argument `monitoring_job` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


FLAGS
    

`--analysis-instance-schema`=`ANALYSIS_INSTANCE_SCHEMA`
     YAML schema file uri(Google Cloud Storage) describing the format of a single instance that you want Tensorflow Data Validation (TFDV) to analyze. 
`--[no-]anomaly-cloud-logging`
     If true, anomaly will be sent to Cloud Logging. Use `--anomaly-cloud-logging` to enable and `--no-anomaly-cloud-logging` to disable. 
`--display-name`=`DISPLAY_NAME`
     Display name of the model deployment monitoring job. 
`--emails`=[`EMAILS`,…]
     Comma-separated email address list. e.g. --emails=a@gmail.com,b@gmail.com 
`--log-ttl`=`LOG_TTL`
     TTL of BigQuery tables in user projects which stores logs(Day-based unit). 
`--monitoring-frequency`=`MONITORING_FREQUENCY`
     Monitoring frequency, unit is 1 hour. 
`--notification-channels`=[`NOTIFICATION_CHANNELS`,…]
     Comma-separated notification channel list. e.g. \--notification-channels=projects/fake-project/notificationChannels/123,projects/fake-project/notificationChannels/456 
`--prediction-sampling-rate`=`PREDICTION_SAMPLING_RATE`
     Prediction sampling rate. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud ai model-monitoring-jobs update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud ai model-monitoring-jobs update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
At most one of these can be specified: 

`--monitoring-config-from-file`=`MONITORING_CONFIG_FROM_FILE`
     Path to the model monitoring objective config file. This file should be a YAML document containing a `ModelDeploymentMonitoringJob`(https://cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/projects.locations.modelDeploymentMonitoringJobs#ModelDeploymentMonitoringJob), but only the ModelDeploymentMonitoringObjectiveConfig needs to be configured. 

Note: Only one of --monitoring-config-from-file and other objective config set, like --feature-thresholds, --feature-attribution-thresholds needs to be set. 

Example(YAML): 
    
    
    modelDeploymentMonitoringObjectiveConfigs:
    - deployedModelId: '5251549009234886656'
      objectiveConfig:
        trainingDataset:
          dataFormat: csv
          gcsSource:
            uris:
            - gs://fake-bucket/training_data.csv
          targetField: price
        trainingPredictionSkewDetectionConfig:
          skewThresholds:
            feat1:
              value: 0.9
            feat2:
              value: 0.8
    - deployedModelId: '2945706000021192704'
      objectiveConfig:
        predictionDriftDetectionConfig:
          driftThresholds:
            feat1:
              value: 0.3
            feat2:
              value: 0.4

Or at least one of these can be specified: 

`--feature-attribution-thresholds`=[`KEY`=`VALUE`,…]
     List of feature-attribution score threshold value pairs(Apply for all the deployed models under the endpoint, if you want to specify different thresholds for different deployed model, please use flag --monitoring-config-from-file or call API directly). If only feature name is set, the default threshold value would be 0.3. 

For example: `feature-attribution-thresholds=feat1=0.1,feat2,feat3=0.2`

`--feature-thresholds`=[`KEY`=`VALUE`,…]
     List of feature-threshold value pairs(Apply for all the deployed models under the endpoint, if you want to specify different thresholds for different deployed model, please use flag --monitoring-config-from-file or call API directly). If only feature name is set, the default threshold value would be 0.3. 

For example: `--feature-thresholds=feat1=0.1,feat2,feat3=0.2`

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha ai model-monitoring-jobs update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/update)
    
    
    [gcloud beta ai model-monitoring-jobs update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/model-monitoring-jobs/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
