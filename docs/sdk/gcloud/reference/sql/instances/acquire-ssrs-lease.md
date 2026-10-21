---
url: https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/acquire-ssrs-lease/
title: gcloud sql instances acquire-ssrs-lease \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:38.696413+00:00
---

# gcloud sql instances acquire-ssrs-lease  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/acquire-ssrs-lease/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud sql instances acquire-ssrs-lease Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud sql instances acquire-ssrs-lease - acquires a SQL Server Reporting Services lease on a Cloud SQL instance 
SYNOPSIS
    

`gcloud sql instances acquire-ssrs-lease` `INSTANCE` `--report-database`=`REPORT_DATABASE` `--service-login`=`SERVICE_LOGIN` `--setup-login`=`SETUP_LOGIN` [`--duration`=`DURATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Acquire a SQL Server Reporting Services lease on a Cloud SQL instance. 
EXAMPLES
     To acquire a SQL Server Reporting Services lease on an instance: 
    
    
    gcloud sql instances acquire-ssrs-lease instance-foo --setup-login=setuplogin --service-login=reportuser --report-database=ReportServer --duration=4h

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
REQUIRED FLAGS
    

`--report-database`=`REPORT_DATABASE`
     Existing or new report database name in the Cloud SQL for SQL Server instance that is used for SSRS setup. 
`--service-login`=`SERVICE_LOGIN`
     Existing login in the Cloud SQL for SQL Server instance that is used as the service login for SSRS setup. 
`--setup-login`=`SETUP_LOGIN`
     Existing login in the Cloud SQL for SQL Server instance that is used as the setup login for SSRS setup. 
OPTIONAL FLAGS
    

`--duration`=`DURATION`
     Time duration, in hours, that the lease will be active to allow SSRS setup. Default lease duration is 5 hours if this flag is not specified. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
