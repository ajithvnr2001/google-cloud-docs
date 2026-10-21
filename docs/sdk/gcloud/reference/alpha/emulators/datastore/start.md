---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/datastore/start/
title: gcloud alpha emulators datastore start \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:32:26.948938+00:00
---

# gcloud alpha emulators datastore start  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/datastore/start/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha emulators datastore start Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha emulators datastore start - start a local datastore emulator 
SYNOPSIS
    

`gcloud alpha emulators datastore start` [`--data-dir`=`DATA_DIR`] [`--host-port`=`HOST_PORT`] [`--no-store-on-disk`] [`--consistency`=`CONSISTENCY`; default=0.9 | `--use-firestore-in-datastore-mode`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command starts a local datastore emulator. 
EXAMPLES
     To start a local datastore emulator, run: 
    
    
    gcloud alpha emulators datastore start --data-dir=DATA-DIR

FLAGS
    

`--data-dir`=`DATA_DIR`
     The directory to be used to store/retrieve data/config for an emulator run. The default value is `<USER_CONFIG_DIR>/emulators/datastore`. The value of USER_CONFIG_DIR can be found by running: 
    
    
    [gcloud info](https://docs.cloud.google.com/sdk/gcloud/reference/info) --format='get(config.paths.global_config_dir)'

`--host-port`=`HOST_PORT`
     The host:port to which the emulator should be bound. Can take the form of a single address (hostname, IPv4, or IPv6) and/or port: 
    
    
    [ADDRESS][:PORT]

In this format you must enclose IPv6 addresses in square brackets: e.g. 
    
    
    [2001:db8:0:0:0:ff00:42:8329]:8080

The default value is localhost:8081. 

`--store-on-disk`
     Whether data should be persisted to disk. Enabled by default, use `--no-store-on-disk` to disable. 
At most one of these can be specified: 

`--consistency`=`CONSISTENCY`; default=0.9
     Fraction of eventually consistent operations that should succeed immediately. Setting to 1.0 can be useful for unit tests, but may mask incorrect assumptions about non-ancestor queries which are eventually consistent. 
`--use-firestore-in-datastore-mode`
     Runs the emulator in Cloud Firestore in Datastore Mode. Reads are always strongly consistent and --consistency flag may not be specified. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta emulators datastore start](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/datastore/start)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
