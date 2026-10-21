---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/sql-integrations/describe/
title: gcloud alpha active-directory domains sql-integrations describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:19.781425+00:00
---

# gcloud alpha active-directory domains sql-integrations describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/sql-integrations/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha active-directory domains sql-integrations describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha active-directory domains sql-integrations describe - describe a Cloud SQL integration against a Managed Microsoft AD domain 
SYNOPSIS
    

`gcloud alpha active-directory domains sql-integrations describe` (`SQL_INTEGRATION` : `--domain`=`DOMAIN`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Describe a Cloud SQL integration against a Managed Microsoft AD domain. 

Displays all details of a Cloud SQL integration given a valid integration ID. 

EXAMPLES
     To describe a Cloud SQL integration with the ID `my-integration` under the managed AD domain `my-domain`, run: 
    
    
    gcloud alpha active-directory domains sql-integrations describe my-integration --domain=my-domain --project=my-project

POSITIONAL ARGUMENTS
    

SQL integration resource - Arguments and flags that specify the SQL integration you want to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `sql_integration` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SQL_INTEGRATION`
     ID of the SQL integration or fully qualified identifier for the SQL integration. 

To set the `sql_integration` attribute: 

  * provide the argument `sql_integration` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--domain`=`DOMAIN`
     The fully-qualified domain name of the Microsoft Active Directory domain. 

To set the `domain` attribute: 

  * provide the argument `sql_integration` on the command line with a fully specified name; 
  * provide the argument `--domain` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedidentities/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-microsoft-ad/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta active-directory domains sql-integrations describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/sql-integrations/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
