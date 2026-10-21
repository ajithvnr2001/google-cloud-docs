---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create/
title: gcloud iam oauth-clients create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:15:35.942818+00:00
---

# gcloud iam oauth-clients create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iam oauth-clients create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iam oauth-clients create - create an OAuth client 
SYNOPSIS
    

`gcloud iam oauth-clients create` (`OAUTH_CLIENT` : `--location`=`LOCATION`) `--allowed-grant-types`=[`ALLOWED_GRANT_TYPES`,…] `--allowed-redirect-uris`=[`ALLOWED_REDIRECT_URIS`,…] `--allowed-scopes`=[`ALLOWED_SCOPES`,…] `--client-type`=`CLIENT_TYPE` [`--description`=`DESCRIPTION`] [`--disabled`] [`--display-name`=`DISPLAY_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new OAuth client. 
EXAMPLES
     The following command creates a disabled OAuth client with ID ``my-oauth-client`` in the default project: 
    
    
    gcloud iam oauth-clients create my-oauth-client --location="global" --client-type="confidential-client" --display-name="My oauth client" --description="My oauth client description" --disabled --allowed-grant-types="authorization-code-grant,refresh-token-grant" --allowed-scopes="<https://www.googleapis.com/auth/cloud-platform\>
    ,openid" --allowed-redirect-uris="https://example.com"

POSITIONAL ARGUMENTS
    

Oauth client resource - The OAuth client to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `oauth_client` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`OAUTH_CLIENT`
     ID of the oauth client or fully qualified identifier for the oauth client. 

To set the `oauth_client` attribute: 

  * provide the argument `oauth_client` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location name. 

To set the `location` attribute: 

  * provide the argument `oauth_client` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--allowed-grant-types`=[`ALLOWED_GRANT_TYPES`,…]
     A list of OAuth grant types that are allowed for the OAuth client. 

The following grant types are currently supported: 

  * `authorization-code-grant`


  * `refresh-token-grant`


`--allowed-redirect-uris`=[`ALLOWED_REDIRECT_URIS`,…]
     A list of redirect uris that is allowed for redirecting when the authorization is completed. 
`--allowed-scopes`=[`ALLOWED_SCOPES`,…]
     A list of scopes that the OAuth client is allowed to request during OAuth flows. 

The following scopes are currently supported: 

  * `https://www.googleapis.com/auth/cloud-platform`: View, edit, configure, and delete your Google Cloud data, and view the email address for your Google Account. 


  * `openid`: Associate you with your personal info on Google Cloud. 


  * `email`: The OAuth client can read a federated identity's email address. 


  * `groups`: The OAuth client can read a federated identity's groups. 


`--client-type`=`CLIENT_TYPE`
     The type of OAuth client. `CLIENT_TYPE` must be one of: `confidential-client`, `public-client`. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     A description of the OAuth client. Cannot exceed 256 characters. 
`--disabled`
     Disables the OAuth client. You cannot use a disabled OAuth client for login. Include `--no-disabled` to enable a disabled OAuth client. 
`--display-name`=`DISPLAY_NAME`
     A display name for the OAuth client. Cannot exceed 32 characters. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha iam oauth-clients create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/oauth-clients/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
