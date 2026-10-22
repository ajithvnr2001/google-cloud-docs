---
url: https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes/
title: Using blockchain nodes \u00a0|\u00a0 Blockchain Node Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:05.049854+00:00
---

# Using blockchain nodes  |  Blockchain Node Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain Node Engine ](https://docs.cloud.google.com/blockchain-node-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-node-engine/docs/overview)



Send feedback 

#  Using blockchain nodes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to get ready to query a Blockchain Node Engine node using an API key for authentication.

Before you can use the blockchain node, you need to:

  * Create an API key
  * Get the node's URLs



## Create an API key

You must use an API key for authentication to query your node.

To generate a key in the Google Cloud console:

  1. In the Google Cloud console, go to the **APIs & Services, Credentials** page.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click **Create credentials**.

  3. Click **API key**.

  4. In the **API key created** dialog, click content_copy **Copy** to copy the key, and then paste it into a temporary file. You will need the API key in Query a blockchain node.




See [Authenticate using API keys](https://cloud.google.com/docs/authentication/api-keys) for more information on API keys.

## Get the blockchain node endpoint URLs

You can get the blockchain node URLs using the console or by sending an API request:

### Using the console

To view details about a node in the UI:

  1. In the Google Cloud console, go to the **Blockchain Node Engine** page.

[Go to Blockchain Node Engine](https://console.cloud.google.com/blockchain-node-engine)

The [**Nodes**](https://docs.cloud.google.com/blockchain-node-engine/docs/node-list) list page is displayed by default.

  2. Click a node name. The [**Node details**](https://docs.cloud.google.com/blockchain-node-engine/docs/node-details) page is displayed.   
Blockchain node URLs are displayed in the **Endpoints** area.




### Using an API

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



The blockchain URLs returned are in the `endpointInfo` and `additionalEndpoints` sections as shown in the following Ethereum example:
    
    
    {
      "name": "projects/my-project-id/locations/us-central1/blockchainNodes/my-node",
      "createTime": "2023-05-05T04:24:12.432769Z",
      "updateTime": "2023-05-05T05:03:02.561240Z",
      "labels": {
        "my-label-key": "my-label-value"
      },
      "blockchainType": "ETHEREUM",
      "connectionInfo": {
        "ipInfo": {
          "rpcIpv4Address": "192.0.2.1"
        },
        "endpointInfo": {
          "jsonRpcApiEndpoint": "json-rpc.ejp4j0b1rdiq06p8lxksd5z25.blockchainnodeengine.com",
          "websocketsApiEndpoint": "ws.ejp4j0b1rdiq06p8lxksd5z25.blockchainnodeengine.com"
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
          "beaconApiEndpoint": "beacon.ejp4j0b1rdiq06p8lxksd5z25.blockchainnodeengine.com",
          "beaconPrometheusMetricsApiEndpoint": "bc-mc.ejp4j0b1rdiq06p8lxksd5z25.blockchainnodeengine.com"
        }
      },
      "state": "RUNNING"
    }
    

See also: [View blockchain node details, Using an API](https://docs.cloud.google.com/blockchain-node-engine/docs/node-details#using-an-api)

## Query a blockchain node

Now that you know your API key and blockchain node endpoint URLs, for usage instructions see the appropriate topic for each blockchain:

  * **Ethereum:** See [Using Ethereum blockchain nodes](https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes-ethereum)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
