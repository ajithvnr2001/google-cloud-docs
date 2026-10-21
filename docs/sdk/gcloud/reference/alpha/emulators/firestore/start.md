---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/firestore/start/
title: gcloud alpha emulators firestore start \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:17:58.347459+00:00
---

# gcloud alpha emulators firestore start  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/firestore/start/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha emulators firestore start Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha emulators firestore start - start a local Firestore emulator 
SYNOPSIS
    

`gcloud alpha emulators firestore start` [`--database-mode`=`DATABASE_MODE`] [`--edition`=`EDITION`; default="standard"] [`--export-on-exit`=`EXPORT_ON_EXIT`] [`--host-port`=`HOST_PORT`] [`--import-data`=`IMPORT_DATA`] [`--index-file`=`INDEX_FILE`] [`--licenses`] [`--require-indexes`] [`--rules`=`RULES`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command starts a local Firestore emulator. 
EXAMPLES
     To start the local Firestore emulator, run: 
    
    
    gcloud alpha emulators firestore start

To bind to a specific host and port, run: 
    
    
    gcloud alpha emulators firestore start --host-port=0.0.0.0:8080

To run the local Firestore emulator with a Firebase Rules set, run: 
    
    
    gcloud alpha emulators firestore start --rules=firestore.rules

To run the local Firestore emulator in Datastore Mode, run: 
    
    
    gcloud alpha emulators firestore start --database-mode=datastore-mode

To import data at the start of the Firestore emulator, run: 
    
    
    gcloud alpha emulators firestore start --import-data=<path/to/file>

To export emulator data upon emulator shutdown, run: 
    
    
    gcloud alpha emulators firestore start --export-on-exit=<path/to/directory>

To run the local Firestore emulator with a specific database edition, run: 
    
    
    gcloud alpha emulators firestore start --edition=edition

FLAGS
    

`--database-mode`=`DATABASE_MODE`
     The database mode to start the Firestore Emulator in. The valid options are: 
    
    
    `firestore-native` (default): start the emulator in Firestore Native
    `datastore-mode`: start the emulator in Datastore Mode

`--edition`=`EDITION`; default="standard"
     The database edition to start the Firestore Emulator in. `EDITION` must be one of: `standard`, `enterprise`. 
`--export-on-exit`=`EXPORT_ON_EXIT`
     Directory path in which emulator data will be saved upon shutdown. Example: `/home/user/myexports/2024-03-26/`
`--host-port`=`HOST_PORT`
     The host:port to which the emulator should be bound. Can take the form of a single address (hostname, IPv4, or IPv6) and/or port: 
    
    
    [ADDRESS][:PORT]

In this format you must enclose IPv6 addresses in square brackets: e.g. 
    
    
    [2001:db8:0:0:0:ff00:42:8329]:8080

The default value is localhost:8080. 

`--import-data`=`IMPORT_DATA`
     File path to the data to be loaded into the emulator upon start up. Example: `/home/user/myexports/sampleExport/sampleExport.overall_export_metadata.`
`--index-file`=`INDEX_FILE`
     File path to the index file to be used by the emulator. Example: `/home/user/firestore.indexes.yaml`

Only supported in Datastore Mode in conjunction with `--require-indexes`. 

`--licenses`
     If set, the emulator will print open-source dependencies and licenses, then exit. 
`--require-indexes`
     If set, the emulator will require composite indexes to be defined in the index file for all queries that require them. 

Only supported in Datastore Mode in conjunction with `--index-file`. 

`--rules`=`RULES`
     If set, all projects will use the security rules in this file. More information on Firebase Rules and the syntax for this file is available at <https://firebase.google.com/docs/rules>. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud emulators firestore start](https://docs.cloud.google.com/sdk/gcloud/reference/emulators/firestore/start)
    
    
    [gcloud beta emulators firestore start](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/firestore/start)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
