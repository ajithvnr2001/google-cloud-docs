---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/pubsub/
title: gcloud alpha emulators pubsub \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:41.859675+00:00
---

# gcloud alpha emulators pubsub  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha emulators pubsub Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha emulators pubsub - manage your local pubsub emulator 
SYNOPSIS
    

`gcloud alpha emulators pubsub` `COMMAND` [`--data-dir`=`DATA_DIR`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This set of commands allows you to start and use a local Pub/Sub emulator to produce a local emulation of your production Google Pub/Sub environment. In addition to having Java JRE (of version 7 or higher) installed and an application built with Google Cloud Client libraries, you must have your emulator configured (have it started with environment variables set) for it to run successfully. The underlying commands help to set up this configuration. 

To stop the emulator, press Ctrl+C. 

For a more comprehensive overview of Pub/Sub, see <https://cloud.google.com/pubsub/docs/overview>. For Pub/Sub emulator specific documentation, see <https://cloud.google.com/pubsub/docs/emulator>

EXAMPLES
     To start a local pubsub emulator with the default directory for configuration data, run: 
    
    
    [gcloud alpha emulators pubsub start](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/pubsub/start)

After starting the emulator, if your application and emulator run on the same machine, set environment variables automatically by running: 
    
    
    [gcloud alpha emulators pubsub env-init](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/pubsub/env-init)

If you're running your emulator on a different machine, run the above command and use its resulting output to set the environment variables on the machine that runs your application. This might look like: 
    
    
    export PUBSUB_EMULATOR_HOST=localhost:8538
    export PUBSUB_PROJECT_ID=my-project-id

Your emulator is now ready for use. 

FLAGS
    

`--data-dir`=`DATA_DIR`
     The directory to be used to store/retrieve data/config for an emulator run. The default value is `<USER_CONFIG_DIR>/emulators/pubsub`. The value of USER_CONFIG_DIR can be found by running: 
    
    
    [gcloud info](https://docs.cloud.google.com/sdk/gcloud/reference/info) --format='get(config.paths.global_config_dir)'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[env-init](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/pubsub/env-init)`
     `(ALPHA)` Print the commands required to export pubsub emulator's env variables. 
`[start](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/pubsub/start)`
     `(ALPHA)` Start a local pubsub emulator. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta emulators pubsub](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/pubsub)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
