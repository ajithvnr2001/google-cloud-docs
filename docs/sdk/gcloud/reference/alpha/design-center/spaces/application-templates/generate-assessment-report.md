---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/generate-assessment-report/
title: gcloud alpha design-center spaces application-templates generate-assessment-report \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:44.160499+00:00
---

# gcloud alpha design-center spaces application-templates generate-assessment-report  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/generate-assessment-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha design-center spaces application-templates generate-assessment-report Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha design-center spaces application-templates generate-assessment-report - generate a best practice assessment report generator for an application template 
SYNOPSIS
    

`gcloud alpha design-center spaces application-templates generate-assessment-report` (`APPLICATION_TEMPLATE` : `--location`=`LOCATION` `--space`=`SPACE`) [`--async`] [`--service-account`=`SERVICE_ACCOUNT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Generate a best practice assessment report generator for an application template. 
EXAMPLES
     To generate an assessment report for the application template `my-template` in space `my-space` and location `us-central1`, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) generate-assessment-report my-template --space=my-space --location=us-central1

To run the assessment using a specific service account, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) generate-assessment-report my-template --space=my-space --location=us-central1 --service-account=my-svc-account@my-project.iam.gserviceaccount.com

POSITIONAL ARGUMENTS
    

Application template resource - The application template to generate an assessment report for IaC. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `APPLICATION_TEMPLATE` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`APPLICATION_TEMPLATE`
     ID of the application_template or fully qualified identifier for the application_template. 

To set the `application_template_id` attribute: 

  * provide the argument `APPLICATION_TEMPLATE` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the application_template. 

To set the `location` attribute: 

  * provide the argument `APPLICATION_TEMPLATE` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--space`=`SPACE`
     The ID of the space. 

To set the `space` attribute: 

  * provide the argument `APPLICATION_TEMPLATE` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--service-account`=`SERVICE_ACCOUNT`
     The full resource name of the service account to use for this assessment report generation operation. 

  * This service account will be used to execute the assessment report generation process. 
  * The caller must have the "iam.serviceAccounts.actAs" permission on this service account. Format: `projects/{PROJECT}/serviceAccounts/{EMAIL_ADDRESS}`


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
