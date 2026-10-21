---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/create/
title: gcloud alpha design-center spaces create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:51.977634+00:00
---

# gcloud alpha design-center spaces create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha design-center spaces create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha design-center spaces create - create a space 
SYNOPSIS
    

`gcloud alpha design-center spaces create` (`SPACE` : `--location`=`LOCATION`) [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--enable-gcp-shared-templates`] [`--gcs-bucket`=`GCS_BUCKET`] [`--tags`=[`TAGS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a space. 
EXAMPLES
     To create the space `my-space` in project `my-project` and location `us-central1`, run: 
    
    
    gcloud alpha design-center spaces create my-space --project=my-project --location=us-central1

Or run: 
    
    
    gcloud alpha design-center spaces create projects/my-project/locations/us-central1/spaces/my-space

To create the space `my-space` in project `my-project` and location `us-central1` with display name, description, and enable google templates, run: 
    
    
    gcloud alpha design-center spaces create my-space --project=my-project --location=us-central1 --display-name=my-display-name --description=my-description --enable-gcp-shared-templates

POSITIONAL ARGUMENTS
    

Space resource - Identifier. The space name. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
     The location id of the space resource. 

To set the `location` attribute: 

  * provide the argument `space` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--description`=`DESCRIPTION`
     Description for the space. 
`--display-name`=`DISPLAY_NAME`
     Display name for the space. 
Arguments for the enable gcp shared templates. 
`--enable-gcp-shared-templates`
     Flag to enable Google opinionated shared templates. 
`--gcs-bucket`=`GCS_BUCKET`
     An existing Google Cloud Storage bucket that you want to use instead of creating a new bucket during Application Design Center setup. If not provided, a default bucket is created during setup. The bucket must exist in the same project as the space. If the bucket name does not exist in the same project as the space, the request fails with an INVALID_ARGUMENT error. If you do not have access to the bucket, the request fails with a PERMISSION_DENIED error. Format: {$bucket_name} For example, if the Cloud Storage bucket URI is gs:\/\/{$bucket_name}, the format is {$bucket_name}. 
`--tags`=[`TAGS`,…]
     Tags are key/values bound to space resource. Example: `"123/environment": "production" "123/costCenter": "marketing"`. For more information on tag creation and management, see <https://cloud.google.com/resource-manager/docs/tags/tags-overview>. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --tags=string=string

`JSON Example:`
    
    
    --tags='{"string": "string"}'

`File Example:`
    
    
    --tags=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `designcenter/v1alpha` API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud design-center spaces create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
