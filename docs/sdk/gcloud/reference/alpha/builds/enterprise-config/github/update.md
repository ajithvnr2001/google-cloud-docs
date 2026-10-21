---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update/
title: gcloud alpha builds enterprise-config github update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:18:10.926213+00:00
---

# gcloud alpha builds enterprise-config github update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha builds enterprise-config github update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha builds enterprise-config github update - update github enterprise config used by Cloud Build 
SYNOPSIS
    

`gcloud alpha builds enterprise-config github update` `CONFIG` [`--app-id`=`APP_ID`] [`--host-uri`=`HOST_URI`] [`--region`=`REGION`] [`--webhook-key`=`WEBHOOK_KEY`] [[`--gcs-bucket`=`GCS_BUCKET` `--gcs-object`=`GCS_OBJECT` : `--generation`=`GENERATION`] | [`--oauth-client-id-name`=`OAUTH_CLIENT_ID_NAME` `--oauth-secret-name`=`OAUTH_SECRET_NAME` `--private-key-name`=`PRIVATE_KEY_NAME` `--webhook-secret-name`=`WEBHOOK_SECRET_NAME` : `--oauth-client-id-version-name`=`OAUTH_CLIENT_ID_VERSION_NAME` `--oauth-secret-version-name`=`OAUTH_SECRET_VERSION_NAME` `--private-key-version-name`=`PRIVATE_KEY_VERSION_NAME` `--webhook-secret-version-name`=`WEBHOOK_SECRET_VERSION_NAME`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update github enterprise config used by Cloud Build. 
POSITIONAL ARGUMENTS
    

`CONFIG`
     The unique identifier of the GitHub Enterprise Config to be updated. 
FLAGS
    

`--app-id`=`APP_ID`
     The app id of the GitHub app that should be associated with this config. 
`--host-uri`=`HOST_URI`
     The host uri of the GitHub Enterprise Server. 
`--region`=`REGION`
     The region of the Cloud Build Service to use. Must be set to a supported region name (e.g. `us-central1`). If unset, `builds/region`, which is the default region to use when working with Cloud Build resources, is used. If builds/region is unset, region is set to `global`. Note: Region must be specified in 2nd gen repo; `global` is not supported. 
`--webhook-key`=`WEBHOOK_KEY`
     The unique identifier that Cloud Build expects to be set as the value for the query field `webhook_key` on incoming webhook requests. 

If this is not set, Cloud Build will generate one on the user's behalf. 

At most one of these can be specified: 

Cloud Storage location of the GitHub App credentials: 
`--gcs-bucket`=`GCS_BUCKET`
     The Cloud Storage bucket containing the credential payload. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--gcs-object`=`GCS_OBJECT`
     The Cloud Storage object containing the credential payload. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--generation`=`GENERATION`
     The object generation to read the credential payload from. 

If this is not set, Cloud Build will read the latest version. 

Secret Manager resources of the GitHub App credentials: 
`--oauth-client-id-name`=`OAUTH_CLIENT_ID_NAME`
     Secret Manager resource containing the oauth client id. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--oauth-secret-name`=`OAUTH_SECRET_NAME`
     Secret Manager resource containing the oauth secret. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--private-key-name`=`PRIVATE_KEY_NAME`
     Secret Manager resource containing the private key. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--webhook-secret-name`=`WEBHOOK_SECRET_NAME`
     Secret Manager resource containing the webhook key. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--oauth-client-id-version-name`=`OAUTH_CLIENT_ID_VERSION_NAME`
     Secret Manager SecretVersion resource containing the oauth client id. 
`--oauth-secret-version-name`=`OAUTH_SECRET_VERSION_NAME`
     Secret Manager SecretVersion resource containing the oauth secret. 
`--private-key-version-name`=`PRIVATE_KEY_VERSION_NAME`
     Secret Manager SecretVersion resource containing the private key. 
`--webhook-secret-version-name`=`WEBHOOK_SECRET_VERSION_NAME`
     Secret Manager SecretVersion resource containing the webhook key. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
