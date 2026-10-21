---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/update/
title: gcloud preview compute interconnects update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:57.960970+00:00
---

# gcloud preview compute interconnects update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute interconnects update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute interconnects update - update a Compute Engine interconnect 
SYNOPSIS
    

`gcloud preview compute interconnects update` `NAME` [`--admin-enabled`] [`--description`=`DESCRIPTION`] [`--location`=`LOCATION`] [`--noc-contact-email`=`NOC_CONTACT_EMAIL`] [`--requested-link-count`=`REQUESTED_LINK_COUNT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute interconnects update` is used to update interconnects. An interconnect represents a single specific connection between Google and the customer. 
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect to update. 
FLAGS
    

`--admin-enabled`
     Administrative status of the interconnect. When this is enabled, the interconnect is operational and will carry traffic across any functioning linked interconnect attachments. Use --no-admin-enabled to disable it. 
`--description`=`DESCRIPTION`
     An optional, textual description for the interconnect. 
`--location`=`LOCATION`
     The location for the interconnect. The locations can be listed by using the `[gcloud preview compute interconnects locations list](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/locations/list)` command to find the appropriate location to use when creating an interconnect. 
`--noc-contact-email`=`NOC_CONTACT_EMAIL`
     Email address to contact the customer NOC for operations and maintenance notifications regarding this interconnect. 
`--requested-link-count`=`REQUESTED_LINK_COUNT`
     Target number of physical links in the link bundle. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute interconnects update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/update)
    
    
    [gcloud alpha compute interconnects update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/update)
    
    
    [gcloud beta compute interconnects update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
