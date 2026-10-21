---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/app/migrate-to-run/
title: gcloud alpha app migrate-to-run \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:39.008348+00:00
---

# gcloud alpha app migrate-to-run  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/app/migrate-to-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha app migrate-to-run Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha app migrate-to-run - migrate a second-generation App Engine app to Cloud Run 
SYNOPSIS
    

`gcloud alpha app migrate-to-run` [`--appyaml`=`APPYAML`] [`--async`] [`--destination-repository`=`DESTINATION_REPOSITORY`] [`--dry-run`] [`--export-only`=`EXPORT_PATH`] [`--from-image`] [`--from-source`] [`--region`=`REGION`] [`--service`=`SERVICE`] [`--version`=`VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Migrates the second-generation App Engine app to Cloud Run. 
EXAMPLES
     To migrate an App Engine app to Cloud Run: 

through app.yaml 

gcloud app migrate-to-run --appyaml=path/to/app.yaml 

OR 

through service and version 

gcloud app migrate-to-run --service=default --version=v1 

FLAGS
    

`--appyaml`=`APPYAML`
     Path to the app.yaml file for the second generation App Engine version to be migrated. If not provided, the app.yaml present in the current directory is used. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--destination-repository`=`DESTINATION_REPOSITORY`
     The full resource name of the AR repository to export to in the format of projects/*/locations/*/repositories/*. 
`--dry-run`
     If set to true, only validates the configuration. The configuration is not applied. 
`--export-only`=`EXPORT_PATH`
     Export the generated Cloud Run service.yaml to the provided path. Migration stops without deploying the service. 
`--from-image`
     Use image based migration. 
`--from-source`
     Use source based migration. 
`--region`=`REGION`
     Region in which the resource can be found. Alternatively, set the property [run/region]. 
`--service`=`SERVICE`
     Name of the service that is deployed in App Engine. If specified, the configuration of the existing service will be used and app.yaml in the current directory will be ignored. 
`--version`=`VERSION`
     Name of the version that is deployed in App Engine. If specified, the configuration of the existing version will be used and app.yaml in the current directory will be ignored. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta app migrate-to-run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-to-run)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
