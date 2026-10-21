---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/deploy/
title: gcloud beta apigee archives deploy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:51:09.877493+00:00
---

# gcloud beta apigee archives deploy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta apigee archives deploy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta apigee archives deploy - deploy an Apigee archive deployment to an environment 
SYNOPSIS
    

`gcloud beta apigee archives deploy` (`--environment`=`ENVIRONMENT` : `--organization`=`ORGANIZATION`) [`--async`] [`--labels`=[`KEY`=`VALUE`,…]] [`--bundle-file`=`BUNDLE_FILE` | `--source`=`SOURCE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Deploy an Apigee archive deployment to an environment. 

`gcloud beta apigee archives deploy` installs an archive deployment in an Apigee environment. 

By default, the archive deployment will be deployed on the remote management plane for the specified Apigee organization. To deploy on a locally running Apigee emulator, use the `--local` flag. 

EXAMPLES
     To deploy the contents of the current working directory as an archive deployment to an environment named ``my-test``, given that the Cloud Platform project has been set in gcloud settings, run: 
    
    
    gcloud beta apigee archives deploy --environment=my-test

To deploy an archive deployment from a local directory other than the current working directory, to an environment named ``my-demo`` in an organization belonging to a Cloud Platform project other than the one set in gcloud settings, named ``my-org``, run: 
    
    
    gcloud beta apigee archives deploy --organization=my-org --environment=my-demo --source=/apigee/dev

To deploy the contents of the current working directory as an archive deployment, with the user-defined labels ``my-label1=foo`` and ``my-label2=bar``, to an environment named ``my-test``, given that the Cloud Platform project has been set in gcloud settings, run: 
    
    
    gcloud beta apigee archives deploy --environment=my-test --labels=my-label1=foo,my-label2=bar

REQUIRED FLAGS
    

Environment resource - Apigee environment in which to deploy the archive deployment. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--environment`=`ENVIRONMENT`
     ID of the environment or fully qualified identifier for the environment. 

To set the `environment` attribute: 

  * provide the argument `--environment` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     Apigee organization containing the environment. If unspecified, the Cloud Platform project's associated organization will be used. 

To set the `organization` attribute: 

  * provide the argument `--environment` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * set the property [project] or provide the argument [--project] on the command line, using a Cloud Platform project with an associated Apigee organization. 


OPTIONAL FLAGS
    

`--async`
     If set, returns immediately and outputs a description of the long running operation that was launched. Else, `gcloud beta apigee archives deploy` will block until the archive deployment has been successfully deployed to the specified environment. 

To monitor the operation once it's been launched, run `gcloud beta apigee operations describe OPERATION_NAME`. 

`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

Source input. 

At most one of these can be specified: 

`--bundle-file`=`BUNDLE_FILE`
     The zip file containing an archive to upload. 
`--source`=`SOURCE`
     The source directory of the archive to upload. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha apigee archives deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/deploy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
