---
url: https://docs.cloud.google.com/sdk/gcloud/reference/storage/cat/
title: gcloud storage cat \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:10.632217+00:00
---

# gcloud storage cat  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/storage/cat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud storage cat Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud storage cat - outputs the contents of one or more URLs to stdout 
SYNOPSIS
    

`gcloud storage cat` `URL` [`URL` …] [`--additional-headers`=`HEADER`=`VALUE`] [`--display-url`, `-d`] [`--range`=`RANGE`, `-r` `RANGE`] [`--decryption-keys`=[`DECRYPTION_KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The cat command outputs the contents of one or more URLs to stdout. While the cat command does not compute a checksum, it is otherwise equivalent to doing: 
    
    
    [gcloud storage cp](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) url… -

(The final '-' causes gcloud to stream the output to stdout.) 

EXAMPLES
     The following command writes all text files in a bucket to stdout: 
    
    
    gcloud storage cat gs://bucket/*.txt

The following command outputs a short header describing file.txt, along with its contents: 
    
    
    gcloud storage cat -d gs://my-bucket/file.txt

The following command outputs bytes 256-939 of file.txt: 
    
    
    gcloud storage cat -r 256-939 gs://my-bucket/file.txt

The following command outputs the last 5 bytes of file.txt: 
    
    
    gcloud storage cat -r -5 gs://my-bucket/file.txt

POSITIONAL ARGUMENTS
    

`URL` [`URL` …]
     The url of objects to list. 
FLAGS
    

`--additional-headers`=`HEADER`=`VALUE`
     Includes arbitrary headers in storage API calls. Accepts a comma separated list of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides the default `storage/additional_headers` property value for this command invocation. 
`--display-url`, `-d`
     Prints the header before each object. 
`--range`=`RANGE`, `-r` `RANGE`
     Causes gcloud storage to output just the specified byte range of the object. In a case where "start" = 'x', and "end" = 'y', ranges take the form: `x-y` (e.g., `-r 256-5939`), `x-` (e.g., `-r 256-`), `-y` (e.g., `-r -5`) 

When offsets start at 0, x-y means to return bytes x through y (inclusive), x- means to return bytes x through the end of the object, and -y changes the role of y. If -y is present, then it returns the last y bytes of the object. 

If the bytes are out of range of the object, then nothing is printed 

ENCRYPTION FLAGS
    

`--decryption-keys`=[`DECRYPTION_KEY`,…]
     A comma-separated list of customer-supplied encryption keys (RFC 4648 section 4 base64-encoded AES256 strings) that will be used to decrypt Cloud Storage objects. Data encrypted with a customer-managed encryption key (CMEK) is decrypted automatically, so CMEKs do not need to be listed here. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha storage cat](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/cat)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
