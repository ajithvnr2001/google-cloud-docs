---
url: https://docs.cloud.google.com/blockchain-node-engine/docs/create-node-ethereum/
title: Create an Ethereum blockchain node \u00a0|\u00a0 Blockchain Node Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:05.100747+00:00
---

# Create an Ethereum blockchain node  |  Blockchain Node Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-node-engine/docs/create-node-ethereum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain Node Engine ](https://docs.cloud.google.com/blockchain-node-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-node-engine/docs/overview)



Send feedback 

#  Create an Ethereum blockchain node Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create an Ethereum blockchain node in Blockchain Node Engine using the console or an API call.

**Note:** It takes about 30 minutes to create a blockchain node. You can check the status of the blockchain node as described in [View node details](https://docs.cloud.google.com/blockchain-node-engine/docs/node-details). This does NOT include sync time which can be up to ~1 day.

## Using the console

In the Google Cloud console, go to the **Blockchain Node Engine** page.

[Go to Blockchain Node Engine](https://console.cloud.google.com/blockchain-node-engine)

The [**Nodes**](https://docs.cloud.google.com/blockchain-node-engine/docs/node-list) list page is displayed by default. If no blockchain nodes have been created, you are prompted to create one.

To create a blockchain node:

  1. Click **Create**. The **Create a blockchain node** wizard opens.

![Blockchain Node Engine create node wizard](https://docs.cloud.google.com/static/blockchain-node-engine/images/create-node-wizard.png)

  2. **Configure node info:**

     1. **Name of blockchain node:** Type a name for the [node](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#node). Use lowercase letters (a-z), numbers, and hyphens. For example, `my-node`.
     2. **Blockchain type:** Select the name of the [blockchain](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#blockchain). For example, `ETHEREUM`.
     3. Click **Continue**.
  3. **Configure blockchain info:** Configure blockchain-specific information. For example, to configure an Ethereum node, select the following options. This information cannot be changed later:

     1. **Network:** The name of the [network](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#network). For example `MAINNET`.
     2. **Node type:** The [type](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#node-type) of the blockchain node. For example, `FULL`.
     3. **Execution/Consensus client:** The name of the [execution](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#execution)/[consensus](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#consensus) layer of the [client](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#client) software. For example, `GETH`/`LIGHTHOUSE`. See Supported configurations for supported combinations.
     4. **Enable additional namespaces:** An optional [JSON-RPC namespace](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#json-rpc-namespace) when using the Ethereum Geth execution client. For example, `debug`.
     5. Click **Continue**.
  4. **Configure network info:**

     1. Select the [geographical location](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#location) in which to host your resources. For example, `us-central1`. This information cannot be changed later. See [Supported locations](https://docs.cloud.google.com/blockchain-node-engine/docs/create-node#supported-locations).
     2. **Configure Endpoints:** Creates publicly accessible endpoints.
     3. Click **Continue**.
  5. **Add labels** :

     1. Type a key-value pair. Click **Add item** to add more key-value pairs.
     2. Click **Continue**.
  6. Click **Create**. the blockchain node is created and the [**Nodes**](https://docs.cloud.google.com/blockchain-node-engine/docs/node-list) list is displayed. The **Status** indicates **Creating** until the blockchain node is ready to use, and then the status changes to **Running**.




## Using an API

To create a blockchain node using an API, send a POST request to the API with the blockchain node specification. An example using the `curl` command to send a request to the API follows:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "blockchainType": "BLOCKCHAIN_TYPE",
        "privateServiceConnectEnabled" : false,
        "ethereumDetails": {
          "consensusClient": "CONSENSUS_CLIENT",
          "executionClient": "EXECUTION_CLIENT",
          "apiEnableAdmin": false,
          "apiEnableDebug": false,
          "network": "NETWORK",
          "nodeType": "NODE_TYPE"
        },
        "labels": {
          "LABEL_KEY": "LABEL_VALUE"
        }
      }' \
    https://blockchainnodeengine.googleapis.com/v1/projects/PROJECT_ID/\
    locations/LOCATION/blockchainNodes?blockchain_node_id=NODE_NAME
    

You must replace the variables in this example with actual values as follows:

  * BLOCKCHAIN_TYPE: The name of the [blockchain](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#blockchain). For example, `ETHEREUM`.
  * CONSENSUS_CLIENT: The name of the [consensus](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#consensus) layer of the client software. For example, `LIGHTHOUSE`. See [Supported configurations](https://docs.cloud.google.com/blockchain-node-engine/docs#supported-configurations) for supported combinations.
  * EXECUTION_CLIENT: The name of the [execution](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#execution) layer of the client software. For example, `GETH`. See Supported configurations for supported combinations.
  * `apiEnableAdmin`: An optional [JSON-RPC namespace](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#json-rpc-namespace) when using the Ethereum Geth execution client. Disabled by default. Set to `true` to enable.
  * `apiEnableDebug`: An optional [JSON-RPC namespace](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#json-rpc-namespace) when using the Ethereum Geth execution client. Disabled by default. Set to `true` to enable.
  * NETWORK: The name of the [network](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#network). For example, `MAINNET`.
  * NODE_TYPE: The [type](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#node-type) of the blockchain node. For example, `FULL`.
  * PROJECT_ID: Your Google Cloud project ID. For example, `my-project-id`.
  * LOCATION: The [location](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#location) in which to host your resources. This information cannot be changed later. For example, `us-central1`. See [Supported locations](https://docs.cloud.google.com/blockchain-node-engine/docs/create-node#supported-locations).
  * NODE_NAME: A name you specify for your node. Use lowercase letters (a-z), numbers, and hyphens. For example, `my-node`.
  * `labels`: A key-value pair. In the example, the key is LABEL_KEY, for example `my-label-key` and the value is LABEL_VALUE, for example `my-label-value`.

**Note:** Uppercase letters are not allowed for label names.



Here is a sample response to the earlier command:
    
    
    {
      "name": "projects/my-project-id/locations/us-central1/operations/operation-1683664820863-5fb48c391814a-a546e3e6-ddee30ad",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.blockchainnodeengine.v1.OperationMetadata",
        "createTime": "2023-05-09T20:40:20.979144857Z",
        "target": "projects/my-project-id/locations/us-central1/blockchainNodes/my-node",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

Note that the OPERATION_ID is returned in the earlier example:
    
    
    operation-1683664820863-5fb48c391814a-a546e3e6-ddee30ad
    

You can use this value to [get the status](https://docs.cloud.google.com/blockchain-node-engine/docs/operation-status#get-operation) of the blockchain node creation.

## Validator Configuration

There are additional options available to support customers who are using Blockchain Node Engine beacon clients with a customer-managed validator client.

NOTE: These options are only available using the API.

To create a blockchain node with validator options set, use a `curl` command such as:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "blockchainType": "BLOCKCHAIN_TYPE",
        "ethereumDetails": {
          "consensusClient": "CONSENSUS_CLIENT",
          "executionClient": "EXECUTION_CLIENT",
          "apiEnableAdmin": false,
          "apiEnableDebug": false,
          "network": "NETWORK",
          "nodeType": "NODE_TYPE",
          "validatorConfig": {
            "beaconFeeRecipient": "BEACON_FEE_RECIPIENT",
            "mev_relay_urls": "MEV_RELAY_URL",
          }
        },
      }' \
    https://blockchainnodeengine.googleapis.com/v1/projects/PROJECT_ID/\
    locations/LOCATION/blockchainNodes?blockchain_node_id=NODE_NAME
    

### Beacon Fee Recipient

A default fee recipient can be set on the beacon client, which is used if a fee recipient is not specified by the validator client. While the [Lighthouse documentation](https://lighthouse-book.sigmaprime.io/suggested-fee-recipient.html) refers to this as a suggested fee recipient, as both the execution and beacon clients are trusted, the recipient is always used if specified.

Beacon fee recipients must be Ethereum addresses with the "0x" prefix, for example "0xb469d8b44a3f559a3386af6273ec4a71da88a15a".

### MEV-relay URL

Blockchain nodes come with a managed MEV-boost service included. This enables customers to use an external block builder service or services, take the best block offered by those services, and propose that block.

No specific services are recommended or endorsed, and customers are responsible for verifying the services they select here.

MEV-relay URLs are specified as a comma-separated list of URLs, for example "https://mev1.example.org/,https://mev2.example.org/".

## Supported configurations

Blockchain Node Engine supports a variety of configurations. You can create nodes with any of the following combinations:

nodeType | network | executionClient | consensusClient  
---|---|---|---  
FULL | MAINNET | GETH | LIGHTHOUSE  
FULL | TESTNET_GOERLI_PRATER | GETH | LIGHTHOUSE  
FULL | TESTNET_SEPOLIA | GETH | LIGHTHOUSE  
FULL | TESTNET_HOLESKY | GETH | LIGHTHOUSE  
ARCHIVE | MAINNET | ERIGON | LIGHTHOUSE  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
