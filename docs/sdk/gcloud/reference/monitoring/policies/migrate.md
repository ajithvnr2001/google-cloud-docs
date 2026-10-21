---
url: https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/migrate/
title: gcloud monitoring policies migrate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:33:10.904684+00:00
---

# gcloud monitoring policies migrate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud monitoring policies migrate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud monitoring policies migrate - migrate a Prometheus configuration file to Cloud Monitoring 
SYNOPSIS
    

`gcloud monitoring policies migrate` [`--channels-from-prometheus-alertmanager-yaml`=`PROMETHEUS_ALERT_MANAGER_FILE_PATH` `--policies-from-prometheus-alert-rules-yaml`=[`PROMETHEUS_ALERT_RULE_FILE_PATHS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates new alerting policies and/or notification channels based on provided Prometheus files. The rules YAML file, which holds the alert rules, must be specified as a file through the `--policies-from-prometheus-alert-rules-yaml` flag. 
FLAGS
    

`--channels-from-prometheus-alertmanager-yaml`=`PROMETHEUS_ALERT_MANAGER_FILE_PATH`
     Prometheus alert manager YAML file to be converted to Cloud Monitoring notification channels. Specifying this flag with the \--policies-from-prometheus-alert-rules-yaml flag puts the newly created notification channels into the translated Alert Policies' definition. Use a full or relative path to a local file containing the value of channels_from_prometheus_alertmanager_yaml. 
`--policies-from-prometheus-alert-rules-yaml`=[`PROMETHEUS_ALERT_RULE_FILE_PATHS`,…]
     One or more Prometheus alert rule YAML files (separated by commas if multiple) to be converted to Cloud Alerting Policies. Example: \--policies-from-prometheus-alert-rules-yaml=rules_1.yaml,rules_2.yaml 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha monitoring policies migrate](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/policies/migrate)
    
    
    [gcloud beta monitoring policies migrate](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/policies/migrate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
