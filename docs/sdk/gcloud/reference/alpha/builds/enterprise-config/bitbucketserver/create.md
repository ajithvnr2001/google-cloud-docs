---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create/
title: gcloud alpha builds enterprise-config bitbucketserver create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:18:10.016339+00:00
---

# gcloud alpha builds enterprise-config bitbucketserver create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha builds enterprise-config bitbucketserver create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha builds enterprise-config bitbucketserver create - create a Bitbucket Server config for use by Cloud Build 
SYNOPSIS
    

`gcloud alpha builds enterprise-config bitbucketserver create` `--admin-access-token-secret-version`=`ADMIN_ACCESS_TOKEN_SECRET_VERSION` `--api-key`=`API_KEY` `--host-uri`=`HOST_URI` `--name`=`NAME` `--read-access-token-secret-version`=`READ_ACCESS_TOKEN_SECRET_VERSION` `--user-name`=`USER_NAME` `--webhook-secret-secret-version`=`WEBHOOK_SECRET_SECRET_VERSION` [`--region`=`REGION`] [`--ssl-ca-file`=`PATH_TO_FILE`] [`--peered-network`=`PEERED_NETWORK` `--peered-network-ip-range`=`PEERED_NETWORK_IP_RANGE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Bitbucket Server config for use by Cloud Build. 
REQUIRED FLAGS
    

`--admin-access-token-secret-version`=`ADMIN_ACCESS_TOKEN_SECRET_VERSION`
     Secret Manager resource containing the admin access token. The secret is specified in resource URL format projects/{secret_project}/secrets/{secret_name}/versions/{secret_version}. 
`--api-key`=`API_KEY`
     The Cloud Build API key that should be associated with this config. 
`--host-uri`=`HOST_URI`
     The host uri of the Bitbucket Server instance. 
`--name`=`NAME`
     The config name of the Bitbucket Server connection. 
`--read-access-token-secret-version`=`READ_ACCESS_TOKEN_SECRET_VERSION`
     Secret Manager resource containing the read access token. The secret is specified in resource URL format projects/{secret_project}/secrets/{secret_name}/versions/{secret_version}. 
`--user-name`=`USER_NAME`
     The Bitbucket Server user name that should be associated with this config. 
`--webhook-secret-secret-version`=`WEBHOOK_SECRET_SECRET_VERSION`
     Secret Manager resource containing the webhook secret. The secret is specified in resource URL format projects/{secret_project}/secrets/{secret_name}/versions/{secret_version}. 
OPTIONAL FLAGS
    

`--region`=`REGION`
     The region of the Cloud Build Service to use. Must be set to a supported region name (e.g. `us-central1`). If unset, `builds/region`, which is the default region to use when working with Cloud Build resources, is used. If builds/region is unset, region is set to `global`. Note: Region must be specified in 2nd gen repo; `global` is not supported. 
`--ssl-ca-file`=`PATH_TO_FILE`
     Path to a local file that contains SSL certificate to use for requests to Bitbucket Server. The certificate should be in PEM format. Use a full or relative path to a local file containing the value of ssl_ca_file. 
`--peered-network`=`PEERED_NETWORK`
     VPC network that should be used when making calls to the Bitbucket Server instance. 

If not specified, calls will be made over the public internet. 

`--peered-network-ip-range`=`PEERED_NETWORK_IP_RANGE`
     IP range within the peered network. This is specified in CIDR notation with a slash and the subnet prefix size. Examples: `192.168.0.0/24` or '/29'. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
