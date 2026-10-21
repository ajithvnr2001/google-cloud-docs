---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/update/
title: gcloud compute interconnects macsec update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:20:29.289116+00:00
---

# gcloud compute interconnects macsec update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute interconnects macsec update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute interconnects macsec update - update a Compute Engine interconnect MACsec configuration 
SYNOPSIS
    

`gcloud compute interconnects macsec update` `NAME` [`--enabled`] [`--fail-open`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute interconnects macsec update` is used to update MACsec configuration of interconnect. An interconnect represents a single specific connection between Google and the customer. 

For an example, refer to the `EXAMPLES` section below. 

EXAMPLES
     To enable MACsec on an interconnect, run: 
    
    
    gcloud compute interconnects macsec update example-interconnect --enabled

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect to update. 
FLAGS
    

`--enabled`
     Enable or disable MACsec on this Interconnect. MACsec enablement will fail if the MACsec configuration is not specified. Use --no-enabled to disable it. 
`--fail-open`
     If enabled, the Interconnect will be configured with a should-secure MACsec security policy, that allows the Google router to fallback to cleartext traffic if the MKA session cannot be established. By default, the Interconnect will be configured with a must-secure security policy that drops all traffic if the MKA session cannot be established with your router. Use --no-fail-open to disable it. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute interconnects macsec update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/macsec/update)
    
    
    [gcloud beta compute interconnects macsec update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/macsec/update)
    
    
    [gcloud preview compute interconnects macsec update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/macsec/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
