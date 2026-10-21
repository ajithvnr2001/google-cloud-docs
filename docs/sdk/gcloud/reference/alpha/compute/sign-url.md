---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/sign-url/
title: gcloud alpha compute sign-url \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:14:56.744925+00:00
---

# gcloud alpha compute sign-url  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/sign-url/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute sign-url Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute sign-url - sign specified URL for use with Cloud CDN Signed URLs 
SYNOPSIS
    

`gcloud alpha compute sign-url` `URL` `--expires-in`=`EXPIRES_IN` `--key-file`=`LOCAL_FILE_PATH` `--key-name`=`KEY_NAME` [`--validate`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute sign-url` generates a signed URL for the specified URL and optionally validates the response by sending a request to the signed URL. 

Cloud CDN Signed URLs give you a way to serve responses from the globally distributed CDN cache, even if the request needs to be authorized. 

Signed URLs are a mechanism to temporarily give a client access to a private resource without requiring additional authorization. To achieve this, the full request URL that should be allowed is hashed and cryptographically signed. By using the signed URL you give it, that one request will be considered authorized to receive the requested content. 

Generally, a signed URL can be used by anyone who has it. However, it is usually only intended to be used by the client that was directly given the URL. To mitigate this, they expire at a time chosen by the issuer. To minimize the risk of a signed URL being shared, it is recommended that the signed URL be set to expire as soon as possible. 

A 128-bit secret key is used for signing the URLs. 

The URLs to sign have the following restrictions: 

  * The URL scheme must be either HTTP or HTTPS. 
  * The URLs must not contain the query parameters: `Expires`, `KeyName` or `Signature`, since they are used for signing. 
  * The URL must not have a fragment. 


POSITIONAL ARGUMENTS
    

`URL`
     The URL to sign. 
REQUIRED FLAGS
    

`--expires-in`=`EXPIRES_IN`
     The duration for which the signed URL will be valid. For example, specifying `12h` will cause the signed URL to be valid up to 12 hours. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--key-file`=`LOCAL_FILE_PATH`
     The file containing the RFC 4648 Section 5 base64url encoded 128-bit secret key for Cloud CDN Signed URL. It is vital that the key is strongly random. One way to generate such a key is with the following command: 
    
    
    head -c 16 /dev/random | base64 | tr +/ -_ > [KEY_FILE_NAME]

`--key-name`=`KEY_NAME`
     Name of the Cloud CDN Signed URL key. 
OPTIONAL FLAGS
    

`--validate`
     If provided, validates the generated signed URL by sending a HEAD request and prints out the HTTP response code. 

If the signed URL is valid, the result should be the same as the response code sent by the backend. If it isn't, recheck the key name and the contents of the key file, and ensure that expires-in is set to at least several seconds and that the clock on the computer running this command is accurate. 

If not provided, the generated signed URL is not verified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute sign-url](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sign-url)
    
    
    [gcloud beta compute sign-url](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/sign-url)
    
    
    [gcloud preview compute sign-url](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/sign-url)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
