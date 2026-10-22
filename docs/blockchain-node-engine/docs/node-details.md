---
url: https://docs.cloud.google.com/blockchain-node-engine/docs/node-details/
title: View blockchain node details \u00a0|\u00a0 Blockchain Node Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:19.160613+00:00
---

# View blockchain node details  |  Blockchain Node Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-node-engine/docs/node-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain Node Engine ](https://docs.cloud.google.com/blockchain-node-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-node-engine/docs/overview)



Send feedback 

#  View blockchain node details Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view details about a Blockchain Node Engine node using the console or an API call.

## Using the console

To view details about a node in the UI:

  1. In the Google Cloud console, go to the **Blockchain Node Engine** page.

[Go to Blockchain Node Engine](https://console.cloud.google.com/blockchain-node-engine)

The [**Nodes**](https://docs.cloud.google.com/blockchain-node-engine/docs/node-list) list page is displayed by default.

  2. Click a node name. The **Node details** page is displayed.




### View node details

The **Node details** page displays detailed information about the selected node.

You can do the following on this page:

  * Open the **APIs & Services Credentials** page.
  * content_copy **Copy** an item to the clipboard.
  * open_in_new **Open** the **Metrics Explorer** page.



[![Blockchain Node Engine Node details user interface](https://docs.cloud.google.com/static/blockchain-node-engine/images/node-details.png)](https://docs.cloud.google.com/static/blockchain-node-engine/images/node-details.png)

Category | Description  
---|---  
Node info | 

  * **Node name:** The name you gave the node in [Create a blockchain node](https://docs.cloud.google.com/blockchain-node-engine/docs/create-node). 
  * **Status:** The node's current state. For example, **Running**. See [ State](https://docs.cloud.google.com/blockchain-node-engine/docs/reference/rest/v1/projects.locations.blockchainNodes#State) for all possible states. 
  * **Block height:** Block height indicates the number of blocks this node has synced. A node's block height should be roughly equal to its peers after initial syncing. To check the most recent block height of the blockchain you can use a block explorer like [Etherscan](https://etherscan.io/) for Ethereum, [PolygonScan](https://polygonscan.com/) for Polygon, and [Solana Explorer](https://explorer.solana.com/) for Solana. 
  * **Blockchain:** The name of the [ blockchain](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#blockchain) and [network](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#network) you selected in [ Create a blockchain node](https://docs.cloud.google.com/blockchain-node-engine/docs/create-node). 
  * **Execution client:** The name of the [execution](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#execution) client you selected in [ Create a blockchain node](https://docs.cloud.google.com/blockchain-node-engine/docs/create-node). 
  * **Consensus client** The name of the [consensus](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#consensus) client you selected in [ Create a blockchain node](https://docs.cloud.google.com/blockchain-node-engine/docs/create-node). 
  * **Type:** The [type](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#node-type) of blockchain node you selected in [ Create a blockchain node](https://docs.cloud.google.com/blockchain-node-engine/docs/create-node). 

  
Endpoints |  Lists the endpoint URLs of your endpoints that were created when you created your blockchain node. The endpoint URL is required to [ use the blockchain node](https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes).   
API keys |  Provides a link to the API keys page for the API key you created in [ Create an API key](https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes#create-api-key). An API key is required to [ use the blockchain node](https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes).   
Location |  The geographical location you selected in [ Create a blockchain node](https://docs.cloud.google.com/blockchain-node-engine/docs/create-node).   
Metrics |  View metrics using the [ Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) regarding the health of the blockchain node.   
  
## Using an API

To list details related to a blockchain node with [ListBlockchainNodes](https://docs.cloud.google.com/blockchain-node-engine/docs/reference/rest/v1/projects.locations.blockchainNodes/list), send the following request:
    
    
    curl \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
    https://blockchainnodeengine.googleapis.com/v1/projects/PROJECT_ID/\
    locations/LOCATION/blockchainNodes/NODE_NAME
    

Where:

  * PROJECT_ID is your Google Cloud project ID. For example, `my-project-id`
  * LOCATION is the [location](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#location) you selected in [Create a blockchain node](https://docs.cloud.google.com/blockchain-node-engine/docs/create-node). For example, `us-central1`.
  * NODE_NAME is the name of the node that you created in [Create a blockchain node](https://docs.cloud.google.com/blockchain-node-engine/docs/create-node). For example, `my-node`.



If the node has been created, you will see a response like the following Ethereum example:
    
    
      {
          "name": "projects/my-project-id/locations/us-central1/blockchainNodes/my-node",
          "createTime": "2023-04-21T19:26:16.293078Z",
          "updateTime": "2023-04-21T19:57:36.769661Z",
          "labels": {
            "my-label-key": "my-label-value"
          },
          "blockchainType": "ETHEREUM",
          "connectionInfo": {
            "ipInfo": {
              "rpcIpv4Address": "203.0.113.1"
            },
            "endpointInfo": {
              "jsonRpcApiEndpoint": "json-rpc.2g7qvv04aisoq4jhnqqgw8zy0.blockchainnodeengine.com",
              "websocketsApiEndpoint": "ws.2g7qvv04aisoq4jhnqqgw8zy0.blockchainnodeengine.com"
            }
          },
          "ethereumDetails": {
            "network": "MAINNET",
            "nodeType": "FULL",
            "executionClient": "GETH",
            "consensusClient": "LIGHTHOUSE",
            "apiEnableAdmin": false,
            "apiEnableDebug": false,
            "additionalEndpoints": {
              "beaconApiEndpoint": "beacon.2g7qvv04aisoq4jhnqqgw8zy0.blockchainnodeengine.com",
              "beaconPrometheusMetricsApiEndpoint": "bc-mc.2g7qvv04aisoq4jhnqqgw8zy0.blockchainnodeengine.com"
            }
          },
          "state": "RUNNING"
      }
    

If you send this command immediately after sending the command to create the node, the value of `state` will be `CREATING`. You can use the URL to set up your infrastructure; however, the node is not usable until the state changes to `RUNNING`.

Make a note of the endpoint URL from the response so you can use it in [Using blockchain nodes](https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes).

## Node states

Node instances will have various states based on the lifecycle of the node.

State | Description  
---|---  
CREATING |  During this state, the node instance is being created and is not usable. While the endpoints are shown, they are not accessible. This stage lasts up to 45 minutes.   
RUNNING |  During this state, the node will be accessible. Note that after initial creation, the node will need to sync with the blockchain. Until syncing is complete, you may get incomplete results from various RPC calls. 
* **Ethereum Full nodes:** ~10 hours to sync. To check sync status, make a call to [eth_syncing](https://docs.cloud.google.com/blockchain-node-engine/docs/troubleshooting#i_dont_know_if_my_node_has_finished_syncing).
* **Ethereum Archive nodes:** ~12 hours to sync. To check sync status, [query the metrics endpoint](https://docs.cloud.google.com/blockchain-node-engine/docs/troubleshooting#i_dont_know_if_my_node_has_finished_syncing).
* **Polygon Full nodes:** ~6 hours to sync. Note that for the first ~1 hour while Heimdall is syncing, API requests will throw `503` errors. It then takes another ~5 hours for Bor to sync. To check sync status, make a call to [eth_syncing](https://docs.cloud.google.com/blockchain-node-engine/docs/troubleshooting#i_dont_know_if_my_node_has_finished_syncing). 
* **Solana Non-voting RPC nodes:** ~1 hour to sync. Note that while syncing, API requests will throw `503` errors.   
DELETING |  During this state, the node is actively being deleted and cannot be used. This can take up to 30 minutes.   
ERROR |  This state indicates that an unexpected error has occurred. Delete the node and try again. If the issue persists, please contact support.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
