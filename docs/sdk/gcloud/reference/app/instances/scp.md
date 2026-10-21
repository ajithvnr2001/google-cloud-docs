---
url: https://docs.cloud.google.com/sdk/gcloud/reference/app/instances/scp/
title: gcloud app instances scp \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:31.778467+00:00
---

# gcloud app instances scp  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/app/instances/scp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud app instances scp Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud app instances scp - SCP from or to the VM of an App Engine Flexible instance 
SYNOPSIS
    

`gcloud app instances scp` [`INSTANCE`:]`SRC` [[`INSTANCE`:]`SRC` …] [`INSTANCE`:]`DEST` [`--compress`] [`--recurse`] [`--service`=`SERVICE`] [`--tunnel-through-iap`] [`--version`=`VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud app instances scp` lets you remotely copy files to or from an App Engine Flexible instance. 

`gcloud app instances scp` resolves the instance's IP address and pre-populates the VM with a public key managed by gcloud. If the gcloud managed key pair does not exist, it is generated the first time an SSH command is run, which may prompt you for a passphrase for the private key encryption. 

All SSH commands require the OpenSSH client suite to be installed on Linux and Mac OS X. On Windows, the Google Cloud CLI comes with a bundled PuTTY suite instead, so it has no external dependencies. 

EXAMPLES
     To copy one file from a remote instance to the local machine, run: 
    
    
    gcloud app instances scp --service=s1 --version=v1 i1:remote_file local_file

To copy several local files to a remote instance, run: 
    
    
    gcloud app instances scp --service=s1 --version=v1 local_1 local_1 i1:remote_dir

To use recursive copy, run: 
    
    
    gcloud app instances scp --service=s1 --version=v1 --recurse local_dir i1:remote_dir

POSITIONAL ARGUMENTS
    

[`INSTANCE`:]`SRC` [[`INSTANCE`:]`SRC` …]
     Specifies the files to copy. 
[`INSTANCE`:]`DEST`
     Specifies a destination for the source files. 
FLAGS
    

`--compress`
     Enable compression. 
`--recurse`
     Upload directories recursively. 
`--service`=`SERVICE`
     The service ID. 
`--tunnel-through-iap`
     Tunnel the ssh connection through Identity-Aware Proxy for TCP forwarding. 

To learn more, see the [IAP for TCP forwarding documentation](https://cloud.google.com/iap/docs/tcp-forwarding-overview). 

`--version`=`VERSION`
     The version ID. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta app instances scp](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/instances/scp)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
