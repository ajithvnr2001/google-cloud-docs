---
url: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/failover/
title: gcloud oracle-database autonomous-databases failover \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:43:31.056528+00:00
---

# gcloud oracle-database autonomous-databases failover  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/failover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud oracle-database autonomous-databases failover Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud oracle-database autonomous-databases failover - failovers a standby AutonomousDatabase to a new primary 
SYNOPSIS
    

`gcloud oracle-database autonomous-databases failover` `AUTONOMOUS_DATABASE` [`--async`] [`--location`=`LOCATION`] [`--peer-autonomous-database`=`PEER_AUTONOMOUS_DATABASE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Failovers an AutonomousDatabase from a standby database to a new primary. 
EXAMPLES
     To failover an AutonomousDatabase with id `my-instance` in the location `us-east4` with primary database name as 'projects/project-id/locations/us-west3/autonomousDatabases/my-peer-instance' run: 
    
    
    gcloud oracle-database autonomous-databases failover my-instance --location=us-east4 --peer-autonomous-database=projects/project-id/locations/us-west3/autonomousDatabases/my-peer-instance

POSITIONAL ARGUMENTS
    

AutonomousDatabase resource - The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `autonomous_database` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `autonomous_database` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`AUTONOMOUS_DATABASE`
     ID of the autonomousDatabase or fully qualified identifier for the autonomousDatabase. 

To set the `autonomous_database` attribute: 

  * provide the argument `autonomous_database` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--location`=`LOCATION`
     For resources [autonomous_database, peer-autonomous-database], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
AutonomousDatabase resource - The peer database name to fail over to. Required for cross-region standby, and must be omitted for in-region Data Guard. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--peer-autonomous-database` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--peer-autonomous-database` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--peer-autonomous-database`=`PEER_AUTONOMOUS_DATABASE`
     ID of the autonomousDatabase or fully qualified identifier for the autonomousDatabase. 

To set the `autonomous-database` attribute: 

  * provide the argument `--peer-autonomous-database` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `oracledatabase/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/oracle/database/docs>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
