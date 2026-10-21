---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-config/
title: gcloud beta app migrate-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:58.867066+00:00
---

# gcloud beta app migrate-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app migrate-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app migrate-config - convert configuration files from one format to another 
SYNOPSIS
    

`gcloud beta app migrate-config` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Automated one-time migration tooling for helping with transition of configuration from one state to another. Currently exclusively provides commands for converting datastore-indexes.xml, queue.xml, cron.xml and dispatch.xml to their yaml counterparts. 
EXAMPLES
     To convert a cron.xml to cron.yaml, run: 
    
    
    [gcloud beta app migrate-config cron-xml-to-yaml](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-config/cron-xml-to-yaml) my/app/WEB-INF/cron.xml

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[cron-xml-to-yaml](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-config/cron-xml-to-yaml)`
     `(BETA)` Translates a cron.xml into cron.yaml. 
`[datastore-indexes-xml-to-yaml](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-config/datastore-indexes-xml-to-yaml)`
     `(BETA)` Translates a datastore-indexes.xml into index.yaml. 
`[dispatch-xml-to-yaml](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-config/dispatch-xml-to-yaml)`
     `(BETA)` Translates a dispatch.xml into dispatch.yaml. 
`[queue-xml-to-yaml](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-config/queue-xml-to-yaml)`
     `(BETA)` Translates a queue.xml into queue.yaml. 
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
