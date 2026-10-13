---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create/
title: gcloud alpha blockchain-node-engine nodes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:11.066856+00:00
---

# gcloud alpha blockchain-node-engine nodes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha blockchain-node-engine nodes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha blockchain-node-engine nodes create - create a Blockchain Node Engine node 
SYNOPSIS
    

`gcloud alpha blockchain-node-engine nodes create` (`NODE_NAME` : `--location`=`LOCATION`) [`--async`] [`--blockchain-type`=`BLOCKCHAIN_TYPE`; default="ETHEREUM"] [`--consensus-client`=`CONSENSUS_CLIENT`; default="LIGHTHOUSE"] [`--execution-client`=`EXECUTION_CLIENT`; default="GETH"] [`--network`=`NETWORK`; default="MAINNET"] [`--node-type`=`NODE_TYPE`; default="FULL"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Blockchain Node Engine node with the given name and configurations. 

If run asynchronously with `--async`, exits after printing one operation name that can be used to poll the status of the creation via: 
    
    
    gcloud operations describe

EXAMPLES
     To create a Blockchain Node Engine node with the name `my-node` in location `us-central`, run: 
    
    
    gcloud alpha blockchain-node-engine nodes create my-node --location=us-central1

POSITIONAL ARGUMENTS
    

Node resource - Arguments and flags that specify the Blockchain Node Engine node you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `node_name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NODE_NAME`
     ID of the node or fully qualified identifier for the node. 

To set the `node_name` attribute: 

  * provide the argument `node_name` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the blockchain node resource. To set the `location` attribute: 

  * provide the argument `node_name` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `web3/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--blockchain-type`=`BLOCKCHAIN_TYPE`; default="ETHEREUM"
     Blockchain type the node will connect run on. `BLOCKCHAIN_TYPE` must be (only one value is supported): 

`ethereum`
     Ethereum blockchain. 
`--consensus-client`=`CONSENSUS_CLIENT`; default="LIGHTHOUSE"
     Consensus client for Ethereum nodes. `CONSENSUS_CLIENT` must be (only one value is supported): 

`lighthouse`
     Lighthouse execution client. 
`--execution-client`=`EXECUTION_CLIENT`; default="GETH"
     Execution client for Ethereum nodes. `EXECUTION_CLIENT` must be (only one value is supported): 

`geth`
     Geth execution client. 
`--network`=`NETWORK`; default="MAINNET"
     Blockchain network the node will connect to. `NETWORK` must be one of: 

`goerli`
     Goerli & Prater Ethereum test network. 
`holesky`
     Holesky Ethereum test network. 
`mainnet`
     Primary Ethereum network, often referred to as mainnet. 
`sepolia`
     Sepolia Ethereum test network. 
`--node-type`=`NODE_TYPE`; default="FULL"
     Node type - defines whether the node retains only recent data or an archival history. `NODE_TYPE` must be (only one value is supported): 

`full`
     Node retains full history required for consensus validation, however does not retain archival data beyond that. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `blockchainnodeengine/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/blockchain-node-engine>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
