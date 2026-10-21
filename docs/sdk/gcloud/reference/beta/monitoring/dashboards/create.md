---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/dashboards/create/
title: gcloud beta monitoring dashboards create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:09:50.202303+00:00
---

# gcloud beta monitoring dashboards create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/dashboards/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta monitoring dashboards create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta monitoring dashboards create - create a new Cloud Monitoring dashboard 
SYNOPSIS
    

`gcloud beta monitoring dashboards create` (`--config`=`CONFIG` | `--config-from-file`=`PATH_TO_FILE`) [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new Monitoring dashboard. A dashboard can be specified as a JSON/YAML value passed in as a string through the `--config` flag or as a file through the `--config-from-file` flag. Validate a dashboard config without saving by setting the `--validate-only` flag. 

For information about the format of a dashboard: <https://cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards>

EXAMPLES
     To create a dashboard with a YAML config, run: 
    
    
    gcloud beta monitoring dashboards create --config='''
      displayName: New Dashboard
      gridLayout:
        widgets:
        - text:
            content: Hello World
      '''

To validate a dashboard and not save it, run: 
    
    
    gcloud beta monitoring dashboards create --validate-only --config='''
      displayName: New Dashboard
      gridLayout:
        widgets:
        - text:
            content: Hello World
      '''

To create a dashboard with a JSON config, run: 
    
    
    gcloud beta monitoring dashboards create --config='''
      {
        "displayName": "New Dashboard",
        "gridLayout": {
          "widgets": [
            {
              "text": {
                "content": "Hello World",
              }
            }
          ]
        },
      }
      '''

To create a dashboard with a specific dashboard ID, run: 
    
    
    gcloud beta monitoring dashboards create --config='''
      name: projects/MY-PROJECT/dashboards/MY-DASHBOARD
      displayName: New Dashboard
      gridLayout:
        widgets:
        - text:
            content: Hello World
      '''

To create a dashboard within a specific project, run: 
    
    
    gcloud beta monitoring dashboards create --project=MY-PROJECT --config='''
      displayName: New Dashboard
      gridLayout:
        widgets:
        - text:
            content: Hello World
      '''

To create a dashboard with a file, run: 
    
    
    gcloud beta monitoring dashboards create --config-from-file=MY-FILE

Sample contents of MY-FILE: 
    
    
    displayName: New Dashboard
    gridLayout:
      widgets:
      - text:
          content: Hello World

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--config`=`CONFIG`
     Dashboard configuration, in either JSON or YAML format, as a string. 
`--config-from-file`=`PATH_TO_FILE`
     Path to a JSON or YAML file containing the dashboard configuration. Use a full or relative path to a local file containing the value of config. 
OPTIONAL FLAGS
    

`--validate-only`
     When set, validate the dashboard but do not save it. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `monitoring/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/monitoring/api/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud monitoring dashboards create](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/create)
    
    
    [gcloud alpha monitoring dashboards create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/dashboards/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
