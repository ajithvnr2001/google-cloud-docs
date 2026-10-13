---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/oauth-clients/credentials/create/
title: gcloud alpha iam oauth-clients credentials create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:56.108224+00:00
---

# gcloud alpha iam oauth-clients credentials create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/oauth-clients/credentials/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha iam oauth-clients credentials create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha iam oauth-clients credentials create - create an OAuth client credential 
SYNOPSIS
    

`gcloud alpha iam oauth-clients credentials create` (`CREDENTIAL` : `--location`=`LOCATION` `--oauth-client`=`OAUTH_CLIENT`) [`--disabled`] [`--display-name`=`DISPLAY_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new OAuth client credential. 
EXAMPLES
     To create a disabled OAuth client credential with ID ``my-oauth-client-credential`` in the default project, run: 
    
    
    gcloud alpha iam oauth-clients credentials create my-oauth-client-credential --location="global" --oauth-client="my-oauth-client" --display-name="My OAuth client credential" --disabled

POSITIONAL ARGUMENTS
    

Oauth client credential resource - The OAuth client credential to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `credential` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CREDENTIAL`
     ID of the oauth client credential or fully qualified identifier for the oauth client credential. 

To set the `credential` attribute: 

  * provide the argument `credential` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location name. 

To set the `location` attribute: 

  * provide the argument `credential` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--oauth-client`=`OAUTH_CLIENT`
     ID to use for the OAuth client, which becomes the final component of the resource name. This value should be 4-32 characters, and may contain the characters [a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may not be specified. To set the `oauth-client` attribute: 

  * provide the argument `credential` on the command line with a fully specified name; 
  * provide the argument `--oauth-client` on the command line. 


FLAGS
    

`--disabled`
     Disables the OAuth client credential. You cannot use a disabled OAuth client credential for OAuth. Include `--no-disabled` to enable a disabled OAuth client credential. 
`--display-name`=`DISPLAY_NAME`
     A display name for the OAuth client credential. Cannot exceed 32 characters. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud iam oauth-clients credentials create](https://docs.cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
