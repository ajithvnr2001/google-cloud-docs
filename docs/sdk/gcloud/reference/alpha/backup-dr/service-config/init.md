---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/service-config/init/
title: gcloud alpha backup-dr service-config init \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:48:21.304316+00:00
---

# gcloud alpha backup-dr service-config init  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/service-config/init/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha backup-dr service-config init Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha backup-dr service-config init - initialize a Backup and DR Service configuration 
SYNOPSIS
    

`gcloud alpha backup-dr service-config init` `--location`=`LOCATION` `--resource-type`=`RESOURCE_TYPE` [`--no-async`] [`--cloudsql-edition`=`CLOUDSQL_EDITION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Initialize a Backup and DR Service configuration. 
EXAMPLES
     To initialize a new service configuration in location ``MY_LOCATION`` and project ``MY_PROJECT`` for resource type ``MY_RESOURCE_TYPE``, run: 
    
    
    gcloud alpha backup-dr service-config init --project=MY_PROJECT --location=MY_LOCATION --resource-type=MY_RESOURCE_TYPE

REQUIRED FLAGS
    

Location resource - The location for which the service configuration should be created. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line. 


`--resource-type`=`RESOURCE_TYPE`
     The resource type to which the default service configuration will be applied. Examples include, "compute.<UNIVERSE_DOMAIN>.com/Instance" 
OPTIONAL FLAGS
    

`--no-async`
     Wait for the operation in progress to complete. 
`--cloudsql-edition`=`CLOUDSQL_EDITION`
     Cloud SQL Edition: (Required only for Cloud SQL instances, ignored otherwise). The edition of the Cloud SQL instance. Possible values: "ENTERPRISE" - Enterprise edition. "ENTERPRISE_PLUS" - Enterprise Plus edition. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the backupdr/v1 API. The full documentation for this API can be found at: <https://cloud.google.com/backup-disaster-recovery>
BRIEF
     Initializes a Backup and DR Service configuration. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud backup-dr service-config init](https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/service-config/init)
    
    
    [gcloud beta backup-dr service-config init](https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/service-config/init)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
