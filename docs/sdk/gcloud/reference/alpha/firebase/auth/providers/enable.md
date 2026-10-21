---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/auth/providers/enable/
title: gcloud alpha firebase auth providers enable \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:13.323037+00:00
---

# gcloud alpha firebase auth providers enable  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/auth/providers/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha firebase auth providers enable Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha firebase auth providers enable - enable and configure Google Sign-In for Firebase Authentication 
SYNOPSIS
    

`gcloud alpha firebase auth providers enable` `--app`=`APP` (`--client-id`=`CLIENT_ID` `--client-secret`=`CLIENT_SECRET` | `--display-name`=`DISPLAY_NAME` `--support-email`=`SUPPORT_EMAIL`) [`--redirect-uris`=[`URI`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Enable and configure Google Sign-In for Firebase Authentication. 
EXAMPLES
     To enable Google Sign-In with a new brand: 
    
    
    gcloud alpha firebase auth providers enable --app=1:123:web:abc --display-name="My App" --support-email=support@example.com

To enable Google Sign-In with an existing OAuth client: 
    
    
    gcloud alpha firebase auth providers enable --app=1:123:web:abc --client-id=CLIENT_ID --client-secret=CLIENT_SECRET

REQUIRED FLAGS
    

`--app`=`APP`
     The Firebase App ID to use. 
OAuth configuration for Google Sign-In. 

Exactly one of these must be specified: 

Client configuration (for using an existing OAuth client): 
`--client-id`=`CLIENT_ID`
     The OAuth client ID (Google provider only, for existing client). 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--client-secret`=`CLIENT_SECRET`
     The OAuth client secret (Google provider only, for existing client). 

This flag argument must be specified if any of the other arguments in this group are specified. 

Brand configuration (for creating a new brand): 
`--display-name`=`DISPLAY_NAME`
     The public display name for the OAuth brand (Google provider only). 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--support-email`=`SUPPORT_EMAIL`
     The customer support email for the OAuth brand (Google provider only). 

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--redirect-uris`=[`URI`,…]
     Authorized redirect URIs (Google provider only). Each URI must be a valid URL starting with `http://` or `https://` (e.g. `https://example.com`). If no scheme is specified, `http://` is prepended. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
