---
url: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/odb-networks/odb-subnets/create/
title: gcloud oracle-database odb-networks odb-subnets create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:25.161011+00:00
---

# gcloud oracle-database odb-networks odb-subnets create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/odb-networks/odb-subnets/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud oracle-database odb-networks odb-subnets create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud oracle-database odb-networks odb-subnets create - create a new OdbSubnet 
SYNOPSIS
    

`gcloud oracle-database odb-networks odb-subnets create` (`ODB_SUBNET` : `--location`=`LOCATION` `--odb-network`=`ODB_NETWORK`) `--cidr-range`=`CIDR_RANGE` `--purpose`=`PURPOSE` [`--async`] [`--labels`=[`LABELS`,…]] [`--request-id`=`REQUEST_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new OdbSubnet. 
EXAMPLES
     To create OdbSubnet with id `my-odbsubnet` with cidr-range `10.0.10.0/24` and the purpose of subnet is for client connections `CLIENT_SUBNET` in the location `us-east4` for a given OdbNetwork with id `my-odbnetwork`. run: 
    
    
    gcloud oracle-database odb-networks odb-subnets create my-odbsubnet --odb-network=my-odbnetwork --cidr-range=10.0.10.0/24 --purpose=CLIENT_SUBNET --location=us-east4

POSITIONAL ARGUMENTS
    

OdbSubnet resource - Identifier. The name of the OdbSubnet resource in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet} The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `odb_subnet` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ODB_SUBNET`
     ID of the odbSubnet or fully qualified identifier for the odbSubnet. 

To set the `odb_subnet` attribute: 

  * provide the argument `odb_subnet` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the odbSubnet resource. 

To set the `location` attribute: 

  * provide the argument `odb_subnet` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--odb-network`=`ODB_NETWORK`
     The odbNetwork id of the odbSubnet resource. 

To set the `odb-network` attribute: 

  * provide the argument `odb_subnet` on the command line with a fully specified name; 
  * provide the argument `--odb-network` on the command line. 


REQUIRED FLAGS
    

`--cidr-range`=`CIDR_RANGE`
     The CIDR range of the subnet. 
`--purpose`=`PURPOSE`
     Purpose of the subnet. `PURPOSE` must be one of: 

`backup-subnet`
     Subnet to be used for backup. 
`client-subnet`
     Subnet to be used for client connections. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--labels`=[`LABELS`,…]
     Labels or tags associated with the resource. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

`--request-id`=`REQUEST_ID`
     An optional ID to identify the request. This value is used to identify duplicate requests. If you make a request with the same request ID and the original request is still in progress or completed, the server ignores the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `oracledatabase/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/oracle/database/docs>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
