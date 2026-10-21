---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/datastore/
title: gcloud beta emulators datastore \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:50:26.869751+00:00
---

# gcloud beta emulators datastore  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/datastore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta emulators datastore Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta emulators datastore - manage your local datastore emulator 
SYNOPSIS
    

`gcloud beta emulators datastore` `COMMAND` [`--data-dir`=`DATA_DIR`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This set of commands allows you to start and use a local datastore emulator. 
EXAMPLES
     To start a local datastore emulator, run: 
    
    
    [gcloud beta emulators datastore start](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/datastore/start)

FLAGS
    

`--data-dir`=`DATA_DIR`
     The directory to be used to store/retrieve data/config for an emulator run. The default value is `<USER_CONFIG_DIR>/emulators/datastore`. The value of USER_CONFIG_DIR can be found by running: 
    
    
    [gcloud info](https://docs.cloud.google.com/sdk/gcloud/reference/info) --format='get(config.paths.global_config_dir)'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[env-init](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/datastore/env-init)`
     `(BETA)` Print the commands required to export env variables of a datastore. 
`[env-unset](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/datastore/env-unset)`
     `(BETA)` Print the commands required to unset a datastore emulators env variables. 
`[start](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/datastore/start)`
     `(BETA)` Start a local datastore emulator. 
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha emulators datastore](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/datastore)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
