---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/blue-green-deployments/delete/
title: gcloud beta sql blue-green-deployments delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:07:02.029615+00:00
---

# gcloud beta sql blue-green-deployments delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/blue-green-deployments/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta sql blue-green-deployments delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta sql blue-green-deployments delete - deletes a Cloud SQL blue-green deployment 
SYNOPSIS
    

`gcloud beta sql blue-green-deployments delete` `DEPLOYMENT` [`--async`] [`--delete-old-source`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Deletes a Cloud SQL blue-green deployment. 
EXAMPLES
     To delete a blue-green deployment named `my-deployment` in region `us-central1`: 
    
    
    gcloud beta sql blue-green-deployments delete my-deployment --region=us-central1

To delete a blue-green deployment and delete the old source instance after a successful switchover: 
    
    
    gcloud beta sql blue-green-deployments delete my-deployment --region=us-central1 --delete-old-source

POSITIONAL ARGUMENTS
    

`DEPLOYMENT`
     The ID of the blue-green deployment. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--delete-old-source`
     Delete the old source instance. This flag is only applicable when deleting a deployment after a switchover has been successfully completed. 

If deleting a deployment before switchover or after a failed switchover, the target instance will be deleted by default, and this flag will be ignored. 

`--region`=`REGION`
     Regional location (e.g. asia-east1, us-east1). See the full list of regions at <https://cloud.google.com/sql/docs/instance-locations>. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha sql blue-green-deployments delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/blue-green-deployments/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
