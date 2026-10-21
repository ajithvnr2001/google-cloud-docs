---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/update-key/
title: gcloud compute interconnects macsec update-key \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:44:22.460787+00:00
---

# gcloud compute interconnects macsec update-key  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/update-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute interconnects macsec update-key Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute interconnects macsec update-key - update pre-shared key in a Compute Engine interconnect MACsec configuration 
SYNOPSIS
    

`gcloud compute interconnects macsec update-key` `NAME` `--key-name`=`KEY_NAME` [`--start-time`=`START_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute interconnects macsec update-key` is used to update a pre-shared key in MACsec configuration of interconnect. 

For an example, refer to the `EXAMPLES` section below. 

EXAMPLES
     To update a pre-shared key in MACsec configuration, run: 
    
    
    gcloud compute interconnects macsec update-key example-interconnect --key-name=default-key --start-time=2021-02-01T12:12:12Z

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect to update. 
REQUIRED FLAGS
    

`--key-name`=`KEY_NAME`
     A name of pre-shared key being added to MACsec configuration of the interconnect. The name must be 1-63 characters long, and comply with RFC1035. 
OPTIONAL FLAGS
    

`--start-time`=`START_TIME`
     A RFC3339 timestamp on or after which the key is valid. startTime can be in the future. If the keychain has a single key, --start-time can be omitted. If the keychain has multiple keys, --start-time is mandatory for each key. The start times of two consecutive keys must be at least 6 hours apart. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute interconnects macsec update-key](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/macsec/update-key)
    
    
    [gcloud beta compute interconnects macsec update-key](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/macsec/update-key)
    
    
    [gcloud preview compute interconnects macsec update-key](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/macsec/update-key)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
