---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/sign-url/
title: gcloud alpha storage sign-url \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:35:00.025033+00:00
---

# gcloud alpha storage sign-url  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/sign-url/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage sign-url Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage sign-url - generate a URL with embedded authentication that can be used by anyone 
SYNOPSIS
    

`gcloud alpha storage sign-url` `URL` [`URL` …] [`--duration`=`DURATION`, `-d` `DURATION`; default=3600] [`--headers`=[`KEY`=`VALUE`,…]] [`--http-verb`=`HTTP_VERB`, `-m` `HTTP_VERB`; default="GET"] [`--path-style-url`] [`--private-key-file`=`PRIVATE_KEY_FILE`] [`--private-key-password`=`PRIVATE_KEY_PASSWORD`, `-p` `PRIVATE_KEY_PASSWORD`] [`--query-params`=[`KEY`=`VALUE`,…]] [`--region`=`REGION`, `-r` `REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha storage sign-url` will generate a signed URL that embeds authentication data so the URL can be used by someone who does not have a Google account. Use the global ``\--impersonate-service-account`` flag to specify the service account that will be used to sign the specified URL or authenticate with a service account directly. Otherwise, a service account key is required. Please see the [Signed URLs documentation](https://cloud.google.com/storage/docs/access-control/signed-urls) for background about signed URLs. 

Note, `gcloud alpha storage sign-url` does not support operations on sub-directories. For example, unless you have an object named `some-directory/` stored inside the bucket `some-bucket`, the following command returns an error: `gcloud alpha storage sign-url gs://some-bucket/some-directory/`. 

EXAMPLES
     To create a signed url for downloading an object valid for 10 minutes with the credentials of an impersonated service account: 
    
    
    gcloud alpha storage sign-url gs://my-bucket/file.txt --duration=10m --impersonate-service-account=sa@my-project.iam.gserviceaccount.com

To create a signed url that will bill to my-billing-project when already authenticated as a service account: 
    
    
    gcloud alpha storage sign-url gs://my-bucket/file.txt --query-params=userProject=my-billing-project

To create a signed url, valid for one hour, for uploading a plain text file via HTTP PUT: 
    
    
    gcloud alpha storage sign-url gs://my-bucket/file.txt --http-verb=PUT --duration=1h --headers=content-type=text/plain --impersonate-service-account=sa@my-project.iam.gserviceaccount.com

To create a signed URL that initiates a resumable upload for a plain text file using a private key file: 
    
    
    gcloud alpha storage sign-url gs://my-bucket/file.txt --http-verb=POST --headers=x-goog-resumable=start,content-type=text/plain --private-key-file=key.json

POSITIONAL ARGUMENTS
    

`URL` [`URL` …]
     The URLs to be signed. May contain wildcards. 
FLAGS
    

`--duration`=`DURATION`, `-d` `DURATION`; default=3600
     Specifies the duration that the signed url should be valid for, default duration is 1 hour. For example 10s for 10 seconds. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 

The max duration allowed is 12 hours. This limitation exists because the system-managed key used to sign the URL may not remain valid after 12 hours. 

Alternatively, the max duration allowed is 7 days when signing with either the ``\--private-key-file`` flag or an account that authorized with ``gcloud auth activate-service-account``. 

`--headers`=[`KEY`=`VALUE`,…]
     Specifies the headers to be used in the signed request. Possible headers are listed in the XML API's documentation: <https://cloud.google.com/storage/docs/xml-api/reference-headers#headers>
`--http-verb`=`HTTP_VERB`, `-m` `HTTP_VERB`; default="GET"
     Specifies the HTTP verb to be authorized for use with the signed URL, default is GET. When using a signed URL to start a resumable upload session, you will need to specify the ``x-goog-resumable:start`` header in the request or else signature validation will fail. 
`--path-style-url`
     Generate path-style signed URL. 

By default, virtual hosted-style signed URL is generated, except for [domain-named buckets](https://cloud.google.com/storage/docs/domain-name-verification). Use this flag to force the generation of path-style signed URL. Signed URL generated for domain-named buckets is always path-style. Learn more about the two URL styles [here](https://cloud.google.com/storage/docs/request-endpoints#xml-api). 

`--private-key-file`=`PRIVATE_KEY_FILE`
     The service account private key used to generate the cryptographic signature for the generated URL. Must be in PKCS12 or JSON format. If encrypted, will prompt for the passphrase used to protect the private key file (default ``notasecret``). 

Note: Service account keys are a security risk if not managed correctly. Review [best practices for managing service account keys](https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys) before using this option. 

`--private-key-password`=`PRIVATE_KEY_PASSWORD`, `-p` `PRIVATE_KEY_PASSWORD`
     Specifies the PRIVATE_KEY_FILE password instead of prompting. 
`--query-params`=[`KEY`=`VALUE`,…]
     Specifies the query parameters to be used in the signed request. Possible query parameters are listed in the XML API's documentation: <https://cloud.google.com/storage/docs/xml-api/reference-headers#query>
`--region`=`REGION`, `-r` `REGION`
     Specifies the region in which the resources for which you are creating signed URLs are stored. 

Default value is ``auto`` which will cause gcloud alpha storage sign-url to fetch the region for the resource. When auto-detecting the region, the current user's credentials, not the credentials from PRIVATE_KEY_FILE, are used to fetch the bucket's metadata. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud storage sign-url](https://docs.cloud.google.com/sdk/gcloud/reference/storage/sign-url)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
