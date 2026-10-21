---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/register-deployed-resources/
title: gcloud alpha design-center spaces register-deployed-resources \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:52.899334+00:00
---

# gcloud alpha design-center spaces register-deployed-resources  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/register-deployed-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha design-center spaces register-deployed-resources Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha design-center spaces register-deployed-resources - register resources with a deployed application in App Hub 
SYNOPSIS
    

`gcloud alpha design-center spaces register-deployed-resources` (`SPACE` : `--location`=`LOCATION`) `--apphub-application`=`APPHUB_APPLICATION` (`--terraform-state`=`TERRAFORM_STATE` | `--tfstate-signed-gcs-uri`=`TFSTATE_SIGNED_GCS_URI`) [`--async`] [`--service-account`=`SERVICE_ACCOUNT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Register deployed resources with an AppHub application in a space. 
EXAMPLES
     To register deployed resources with an AppHub application using the AppHub application URI `my-app` in the space `my-space`, in the project `my-project` and location `us-central1`, run: 
    
    
    gcloud alpha design-center spaces register-deployed-resources my-space --project=my-project --location=us-central1 --apphub-application=`projects/my-project/locations/us-central1/applications/my-app` --terraform-state='{"version":4, "resources": […]}'

To register deployed resources with an AppHub application using a signed GCS URI for the Terraform state file, run: 
    
    
    gcloud alpha design-center spaces register-deployed-resources my-space --project=my-project --location=us-central1 --apphub-application=`projects/my-project/locations/us-central1/applications/my-app` --tfstate-signed-gcs-uri=`[https://storage.googleapis.com/\](https://storage.googleapis.com/\\)
    my-bucket/tfstate.json?x-goog-signature=…`

POSITIONAL ARGUMENTS
    

Space resource - The parent space. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `space` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SPACE`
     ID of the space or fully qualified identifier for the space. 

To set the `space` attribute: 

  * provide the argument `space` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the space. 

To set the `location` attribute: 

  * provide the argument `space` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--apphub-application`=`APPHUB_APPLICATION`
     The name of the AppHub Application. Format: `projects/{project}/locations/{location}/applications/{application}`
Exactly one of these must be specified: 

`--terraform-state`=`TERRAFORM_STATE`
     The Terraform state (tfstate) content as a raw JSON string. Example: '{"version":4, "resources": […]}' 
`--tfstate-signed-gcs-uri`=`TFSTATE_SIGNED_GCS_URI`
     A securely signed Cloud Storage URI pointing to the tfstate file. Example: `https://storage.googleapis.com/my-bucket/tfstate.json?x-goog-signature=…`
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--service-account`=`SERVICE_ACCOUNT`
     The email address of the service account to use for this operation. Format: `projects/{PROJECT}/serviceAccounts/{EMAIL_ADDRESS}`
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the designcenter/v1alpha API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
