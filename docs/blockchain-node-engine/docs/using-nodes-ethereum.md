---
url: https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes-ethereum/
title: Using Ethereum blockchain nodes \u00a0|\u00a0 Blockchain Node Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:00.898299+00:00
---

# Using Ethereum blockchain nodes  |  Blockchain Node Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes-ethereum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain Node Engine ](https://docs.cloud.google.com/blockchain-node-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-node-engine/docs/overview)



Send feedback 

#  Using Ethereum blockchain nodes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to call the Ethereum node API. Before you can access the Ethereum blockchain node, you will need to know the API key and node endpoint URL. Follow the [using blockchain nodes](https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes) guide to determine these, if you have not already done so.

## JSON-RPC

This section describes querying an Ethereum blockchain node's JSON-RPC API.

### Example execution client RPC

You can query the execution client ([Geth](https://launchpad.ethereum.org/en/geth) for full nodes or [Erigon](https://launchpad.ethereum.org/en/erigon) for archive nodes) via JSON-RPC. See [Ethereum API specification](https://ethereum.github.io/execution-apis/api-documentation/) for the generic JSON-RPC specification, or the [Geth RPC documentation](https://geth.ethereum.org/docs/interacting-with-geth/rpc) for Geth-specific documentation.

For example, to call the `eth_getBlockByNumber()` method:
    
    
    curl -H POST \
      -H "X-goog-api-key: YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "id":1,
        "jsonrpc":"2.0",
        "method": "eth_getBlockByNumber",
        "params": ["0x1", true]
      }' \
      http://YOUR_NODES_URL
    

Where:

  * `id` is an identifier set by the client--the originator of the request. For example, `1`.
  * `jsonrpc` is the JSON-RPC version. For example, `2.0`.
  * `method` is the name of the method. For example, `eth_getBlockByNumber`.
  * `params` are values to be used with `method`.
  * YOUR_NODES_URL is the address returned in [Get the blockchain node URLs](https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes#get-urls). For example, `json-rpc.ejp4j0b1rdiq06p8lxksd5z25.blockchainnodeengine.com`.
  * YOUR_API_KEY is the key you created in [Create an API key](https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes#create-api-key).



See [JSON-RPC2.0 Specification](https://www.jsonrpc.org/specification) for more information on the format of the Request object.

Here's a sample response to the above command:
    
    
    {
       "id" : 1,
       "jsonrpc" : "2.0",
       "result" : {
          "difficulty" : "0x3ff800000",
          "extraData" : "0x476574682f76312e302e302f6c696e75782f676f312e342e32",
          "gasLimit" : "0x1388",
          "gasUsed" : "0x0",
          "hash" : "0x88e96d4537bea4d9c05d12549907b32561d3bf31f45aae734cdc119f13406cb6",
          "logsBloom": "0x0000000000000000000000000000000000000",
          "miner" : "0x05a56e2d52c817161883f50c441c3228cfe54d9f",
          "mixHash" : "0x969b900de27b6ac6a67742365dd65f55a0526c41fd18e1b16f1a1215c2e66f59",
          "nonce" : "0x539bd4979fef1ec4",
          "number" : "0x1",
          "parentHash" : "0xd4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3",
          "receiptsRoot" : "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
          "sha3Uncles" : "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
          "size" : "0x219",
          "stateRoot" : "0xd67e4d450343046425ae4271474353857ab860dbc0a1dde64b41b5cd3a532bf3",
          "timestamp" : "0x55ba4224",
          "totalDifficulty" : "0x7ff800000",
          "transactions" : [],
          "transactionsRoot" : "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
          "uncles" : []
       }
    }
    

### Beacon node RPC

Blockchain Node Engine also exposes the Ethereum consensus client endpoint. For example to request the state of the validator at slot `1`:
    
    
    curl \
    -H "X-goog-api-key: YOUR_API_KEY" "Content-Type: application/json" \
    'http://beacon.YOUR_NODES_URL/eth/v1/beacon/states/head/validators/1'
    

You may also provide your API key as an HTTP header instead of a query parameter. The following query is equivalent:
    
    
    curl \
    -H "Content-Type: application/json" \
    'http://beacon.YOUR_NODES_URL/eth/v1/beacon/states/head/validators/1?key=YOUR_API_KEY'
    

Further Explained:

  * YOUR_NODES_URL is the address returned in [Get the blockchain node URLs](https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes#get-urls).
  * YOUR_API_KEY is the key you created in [Create an API key](https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes#create-api-key).



Here's a sample response to the above command:
    
    
    {
      "execution_optimistic": false,
      "data": {
        "index": "1",
        "balance": "36835614902",
        "status": "active_ongoing",
        "validator": {
          "pubkey": "0x1234abcd",
          "withdrawal_credentials": "0x1234abcd",
          "effective_balance": "32000000000",
          "slashed": false,
          "activation_eligibility_epoch": "0",
          "activation_epoch": "0",
          "exit_epoch": "18446744073709551615",
          "withdrawable_epoch": "18446744073709551615"
        }
      }
    }
    

## WebSocket

To subscribe to data feeds rather than poll for data, you can use the WebSocket API of the blockchain node's execution client.

**Note:** Clients using WebSockets must be able to handle loss of the connection. It is strongly recommended that clients track the subscriptions they have on a WebSocket connection and automatically resubscribe to those events if the connection is lost.

For example, to subscribe to new chain heads:
    
    
    wscat -c wss://ws.YOUR_NODES_URL?key=YOUR_API_KEY
    Connected (press CTRL+C to quit)
    > {"jsonrpc":"2.0", "id": 1, "method": "eth_subscribe", "params": ["newHeads"]}
    

The execution client will respond with an identifier for the subscription, such as:
    
    
    {"jsonrpc":"2.0","id":1,"result":"0xf47df962ae9ba250ba9e9fb239b6894f"}
    

Thereafter the client will send details of each new chain head block as it occurs. Here's a sample event from the above subscription:
    
    
    {
       "jsonrpc" : "2.0",
       "method" : "eth_subscription",
       "params" : {
          "result" : {
             "baseFeePerGas" : "0x4bdc620b8",
             "difficulty" : "0x0",
             "extraData" : "0x496c6c756d696e61746520446d6f63726174697a6520447374726962757465",
             "gasLimit" : "0x1c9c380",
             "gasUsed" : "0xe24dae",
             "hash" : "0xbde840749c4d9086d17d66079d5f7d3d568ed4572329691e5b4a70f44a551816",
             "logsBloom": "0x0000000000000000000000000000000000000",
             "miner" : "0xb4c9e4617a16be36b92689b9e07e9f64757c1792",
             "mixHash" : "0xf68eb0b3ec50e1543de1cc7f09c7735ba20fa252124511756857078a3ff9a7cf",
             "nonce" : "0x0000000000000000",
             "number" : "0x109e280",
             "parentHash" : "0x54f78faba9fde0d15d7a9d6b80c4569435c7fdc5f1fef3255110373b66ce14de",
             "receiptsRoot" : "0x876bcb5772f8597fee4b063c57b7a51209eb428034efabf4cdf39a46901681b4",
             "sha3Uncles" : "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
             "stateRoot" : "0xfc5daf9608c8f2b9944bcfe0b9182148d85b1a6ad4dc52d3eb522dd02687c7e0",
             "timestamp" : "0x647fd287",
             "transactionsRoot" : "0x0acaef87e4609ea6075d88fdd404b3fbd25d796af9044522beefd3c708d37af8",
             "withdrawalsRoot" : "0x7adfc670253572678769e7d80db8c4c94b5d14d4e014274f39b679fdb5e72d98"
          },
          "subscription" : "0xf47df962ae9ba250ba9e9fb239b6894f"
       }
    }
    

## Metrics

Ethereum nodes provide a number of metrics on the operational state of the node. Typically these would be consumed by a tool such as [Prometheus](https://prometheus.io/) or [Grafana](https://grafana.com/).

**Tip:** Blockchain Node Engine writes metrics into [Cloud Monitoring](https://docs.cloud.google.com/stackdriver) without requiring any additional infrastructure.

To fetch the metrics exposed by a beacon client you can use a command such as:
    
    
    curl https://bc-mc.YOUR_NODES_URL/metrics/prometheus?key=YOUR_API_KEY
    

This produces an output similar to the following:
    
    
    # HELP async_tasks_count Total number of async tasks spawned using spawn
    # TYPE async_tasks_count gauge
    async_tasks_count{async_task_count="addr_broadcast"} 0
    async_tasks_count{async_task_count="beacon_node"} 0
    async_tasks_count{async_task_count="beacon_processor_manager"} 1
    async_tasks_count{async_task_count="beacon_processor_reprocess_queue"} 1
    async_tasks_count{async_task_count="beacon_processor_worker"} 0
    async_tasks_count{async_task_count="discv5"} 4
    async_tasks_count{async_task_count="el_fork_choice_update"} 0
    async_tasks_count{async_task_count="eth1"} 1
    ...
    

There are separate metrics endpoints for the execution client and beacon client. For the execution client these are typically prefixed `ec-mc` and for the beacon client they are typically prefixed `bc-mc` (as in the example above).

**Note:** The path for execution client metrics is `/debug/metrics/prometheus`, for example `https://ec-mc.YOUR_NODES_URL/debug/metrics/prometheus?key=YOUR_API_KEY`

You can read more about metrics from each client software at:

  * [Geth](https://geth.ethereum.org/docs/monitoring/metrics)
  * [Lighthouse](https://lighthouse-book.sigmaprime.io/advanced_metrics.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
