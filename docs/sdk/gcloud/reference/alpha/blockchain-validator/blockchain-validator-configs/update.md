---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update/
title: gcloud alpha blockchain-validator blockchain-validator-configs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:27:04.981288+00:00
---

# gcloud alpha blockchain-validator blockchain-validator-configs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha blockchain-validator blockchain-validator-configs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha blockchain-validator blockchain-validator-configs update - update the configuration of a single blockchain validator 
SYNOPSIS
    

`gcloud alpha blockchain-validator blockchain-validator-configs update` (`BLOCKCHAIN_VALIDATOR_CONFIG` : `--location`=`LOCATION`) [`--async`] [`--blockchain-node-id`=`BLOCKCHAIN_NODE_ID`] [`--request-id`=`REQUEST_ID`] [`--[no-]validation-work-enabled`] [`--clear-ethereum-protocol-details` `--ethereum-protocol-details-graffiti`=`ETHEREUM_PROTOCOL_DETAILS_GRAFFITI`] [`--clear-remote-web3-signer` `--remote-web3-signer-timeout-duration`=`REMOTE_WEB3_SIGNER_TIMEOUT_DURATION` `--remote-web3-signer-web3signer-uri`=`REMOTE_WEB3_SIGNER_WEB3SIGNER_URI`] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` The `gcloud blockchain-validator` command group is deprecated and will be removed in a future release. 

Update the configuration of a single blockchain validator. 

EXAMPLES
     To enable validation work on a previously disabled blockchain validator `my-validator` in the project `my-project` and location `us-central1` run: 

$ [gcloud alpha blockchain-validator blockchain-validator-configs](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs) \
    
    
    update my-validator --location=us-central1 \
    --project=my-project --validation-work-enabled=true

POSITIONAL ARGUMENTS
    

BlockchainValidatorConfig resource - Identifier. The name of the validator. It must have the format `"projects/{project}/locations/{location}/blockchainValidatorConfigs/{validator}"`. `{validator}` must contain only letters (`[A-Za-z]`), numbers (`[0-9]`), dashes (`-`), underscores (```), periods (`.`), tildes (`~`), plus (`+`) or percent signs (`%`). It must be between 3 and 255 characters in length, and it must not start with `"goog"`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `blockchain_validator_config` on the command line with a fully specified name; 
  * provide the argument `\--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BLOCKCHAIN_VALIDATOR_CONFIG``
     ID of the blockchainValidatorConfig or fully qualified identifier for the blockchainValidatorConfig. 

To set the `blockchain_validator_config` attribute: 

  * provide the argument `blockchain_validator_config` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=LOCATION``
     The location id of the blockchainValidatorConfig resource. 

To set the `location` attribute: 

  * provide the argument `blockchain_validator_config` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Arguments for the blockchain node. 
`--blockchain-node-id`=`BLOCKCHAIN_NODE_ID`
     The fully qualified name of the blockchain node which carries out work on behalf of the validator. If not set, the validator must either be operated outside of Blockchain Validator Manager, or it will be offline (no attestations or blocks will be produced). If this node is offline or deleted, the validator will be offline. 
`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

`--[no-]validation-work-enabled`
     True if the blockchain node requests and signs attestations and blocks on behalf of this validator, false if not. This does NOT define whether the blockchain expects work to occur, only whether the blockchain node specified above is carrying out validation tasks. This should be enabled under normal conditions, but may be useful when migrating validators to/from Blockchain Node Engine, where the validator may be paused during the migration. Use `--validation-work-enabled` to enable and `--no-validation-work-enabled` to disable. 
Arguments for the blockchain type details. 
Blockchain validator configuration unique to Ethereum blockchains. 
`--clear-ethereum-protocol-details`
     Set blockchainValidatorConfig.ethereumProtocolDetails back to default value. 
Arguments for the graffiti. 
`--ethereum-protocol-details-graffiti`=`ETHEREUM_PROTOCOL_DETAILS_GRAFFITI`
     Graffiti is a custom string published in blocks proposed by the validator. This can only be written, as the current value cannot be read back from the validator client API. See <https://lighthouse-book.sigmaprime.io/graffiti.html> for an example of how this is used. If not set, the validator client's default is used. If no blockchain node is specified, this has no effect as no validator client is run. 
Arguments for the key source config. 
Configuration to use an external key signing service, such as the service endpoint. The external key signer is expected to be managed entirely by the customer. For reference see <https://docs.web3signer.consensys.net/> for details on Web3Signer and <https://docs.web3signer.consensys.net/reference/api/json-rpc> for the API exposed by the external service. 
`--clear-remote-web3-signer`
     Set blockchainValidatorConfig.remoteWeb3Signer back to default value. 
Arguments for the timeout duration. 
`--remote-web3-signer-timeout-duration`=`REMOTE_WEB3_SIGNER_TIMEOUT_DURATION`
     Timeout for requests to the Web3Signer service. If not set, a default timeout of 12 seconds is used. 
`--remote-web3-signer-web3signer-uri`=`REMOTE_WEB3_SIGNER_WEB3SIGNER_URI`
     URI of the Web3Signer service the validator client connects to, to request signing of attestations, blocks, etc. 
Update labels. 

At most one of these can be specified: 

`--labels`=[`LABELS`,…]
     Set labels to new value. Labels as key value pairs. 

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

Or at least one of these can be specified: 

`--update-labels`=[`UPDATE_LABELS`,…]
     Update labels value or add key value pair. Labels as key value pairs. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --update-labels=string=string

`JSON Example:`
    
    
    --update-labels='{"string": "string"}'

`File Example:`
    
    
    --update-labels=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-labels`
     Clear labels value and set to empty map. 
`--remove-labels`=`REMOVE_LABELS`
     Remove existing value from map labels. Sets `remove_labels` value. `Shorthand Example:`
    
    
    --remove-labels=string,string

`JSON Example:`
    
    
    --remove-labels=["string"]

`File Example:`
    
    
    --remove-labels=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `blockchainvalidatormanager/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/blockchain-node-engine/docs/create-node-ethereum#validator_configuration>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
