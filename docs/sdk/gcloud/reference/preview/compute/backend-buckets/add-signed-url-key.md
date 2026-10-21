---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/backend-buckets/add-signed-url-key/
title: gcloud preview compute backend-buckets add-signed-url-key \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:38.683801+00:00
---

# gcloud preview compute backend-buckets add-signed-url-key  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/backend-buckets/add-signed-url-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute backend-buckets add-signed-url-key Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute backend-buckets add-signed-url-key - add Cloud CDN Signed URL key to a backend bucket 
SYNOPSIS
    

`gcloud preview compute backend-buckets add-signed-url-key` `BACKEND_BUCKET_NAME` `--key-file`=`LOCAL_FILE_PATH` `--key-name`=`KEY_NAME` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute backend-buckets add-signed-url-key` is used to add a new Cloud CDN Signed URL key to a backend bucket. 

Cloud CDN Signed URLs give you a way to serve responses from the globally distributed CDN cache, even if the request needs to be authorized. 

Signed URLs are a mechanism to temporarily give a client access to a private resource without requiring additional authorization. To achieve this, the full request URL that should be allowed is hashed and cryptographically signed. By using the signed URL you give it, that one request will be considered authorized to receive the requested content. 

Generally, a signed URL can be used by anyone who has it. However, it is usually only intended to be used by the client that was directly given the URL. To mitigate this, they expire at a time chosen by the issuer. To minimize the risk of a signed URL being shared, it is recommended that the signed URL be set to expire as soon as possible. 

A 128-bit secret key is used for signing the URLs. 

POSITIONAL ARGUMENTS
    

`BACKEND_BUCKET_NAME`
     Name of the backend bucket to add CDN signed URL key to. 
REQUIRED FLAGS
    

`--key-file`=`LOCAL_FILE_PATH`
     The file containing the RFC 4648 Section 5 base64url encoded 128-bit secret key for Cloud CDN Signed URL. It is vital that the key is strongly random. One way to generate such a key is with the following command: 
    
    
    head -c 16 /dev/random | base64 | tr +/ -_ > [KEY_FILE_NAME]

`--key-name`=`KEY_NAME`
     Name of the Cloud CDN Signed URL key. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute backend-buckets add-signed-url-key](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/add-signed-url-key)
    
    
    [gcloud alpha compute backend-buckets add-signed-url-key](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/add-signed-url-key)
    
    
    [gcloud beta compute backend-buckets add-signed-url-key](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/backend-buckets/add-signed-url-key)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
