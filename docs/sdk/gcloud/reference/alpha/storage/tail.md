---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/tail/
title: gcloud alpha storage tail \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:22:59.397519+00:00
---

# gcloud alpha storage tail  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/tail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage tail Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage tail - outputs the last parts (the tail) of an object to stdout 
SYNOPSIS
    

`gcloud alpha storage tail` `URL` [`--additional-headers`=`HEADER`=`VALUE`] [`--bytes`=`BYTES`; default="1000"] [`--follow`] [`--decryption-keys`=[`DECRYPTION_KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The tail command outputs the last B bytes of an object to stdout. It can also be used to monitor real time appends to an appendable object in the RAPID storage. 
EXAMPLES
     The following command outputs the last 1000 bytes of an object: 
    
    
    gcloud alpha storage tail gs://my-bucket/object

The following command outputs the last 100 bytes of an object: 
    
    
    gcloud alpha storage tail gs://my-bucket/object --bytes=100

The following command continuously streams new data as it is appended to the appendable object: 
    
    
    gcloud alpha storage tail gs://my-bucket/appendable-object --follow

POSITIONAL ARGUMENTS
    

`URL`
     The URL of the object to tail. 
FLAGS
    

`--additional-headers`=`HEADER`=`VALUE`
     Includes arbitrary headers in storage API calls. Accepts a comma separated list of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides the default `storage/additional_headers` property value for this command invocation. 
`--bytes`=`BYTES`; default="1000"
     Output the last BYTES bytes of the object, or use +BYTES to output starting with byte BYTES of the object (capped at object size). Default is 1000. 
`--follow`
     Output the last B bytes of the appendable object and continuously streams new bytes appended to the appendable object. 
ENCRYPTION FLAGS
    

`--decryption-keys`=[`DECRYPTION_KEY`,…]
     A comma-separated list of customer-supplied encryption keys (RFC 4648 section 4 base64-encoded AES256 strings) that will be used to decrypt Cloud Storage objects. Data encrypted with a customer-managed encryption key (CMEK) is decrypted automatically, so CMEKs do not need to be listed here. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
