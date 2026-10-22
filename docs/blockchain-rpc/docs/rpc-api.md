---
url: https://docs.cloud.google.com/blockchain-rpc/docs/rpc-api/
title: Ethereum RPC API \u00a0|\u00a0 Blockchain RPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:25.004978+00:00
---

# Ethereum RPC API  |  Blockchain RPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-rpc/docs/rpc-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain RPC ](https://docs.cloud.google.com/blockchain-rpc/docs)
  * [ Reference ](https://docs.cloud.google.com/blockchain-rpc/docs/rpc-api)



Send feedback 

#  Ethereum RPC API Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Ethereum API Methods

Blockchain RPC offers 100 requests per second per project along with a quota of 1 million requests per day. Some Ethereum methods are resource intensive and therefore count as more than one request. The following table indicates how much each method counts against your quota. For example, the `debug_traceBlockByHash` call has a multiplier of `50` which means that each call counts as 50 requests. The Beacon Node API is not supported.

Note that Ethereum mainnet is backed by clusters of [Erigon](https://erigon.gitbook.io/erigon) archive nodes and Ethereum Holesky testnet is backed by clusters of [Geth](https://geth.ethereum.org/docs/interacting-with-geth/rpc) full nodes. The method support is similar but differs as indicated. Additionally, if a method is not listed below it is not supported. We will be adding support for additional methods in future releases.

Method Calls | Request multiplier | Mainnet | Testnet  
---|---|---|---  
eth_blockNumber | 1 | check | check  
eth_call | 1 | check | check  
eth_chainId | 1 | check | check  
eth_estimateGas | 1 | check | check  
eth_feeHistory | 1 | check | check  
eth_gasPrice | 1 | check | check  
eth_getBalance | 1 | check | check  
eth_getBlockByHash | 1 | check | check  
eth_getBlockByNumber | 1 | check | check  
eth_getBlockReceipts | 1 | check | check  
eth_getBlockTransactionCountByHash | 1 | check | check  
eth_getBlockTransactionCountByNumber | 1 | check | check  
eth_getCode | 10 | check | check  
eth_getLogs | 50 | check | check  
eth_getProof | 50 | check | check  
eth_getStorageAt | 1 | check | check  
eth_getTransactionByBlockHashAndIndex | 1 | check | check  
eth_getTransactionByBlockNumberAndIndex | 1 | check | check  
eth_getTransactionByHash | 1 | check | check  
eth_getTransactionCount | 1 | check | check  
eth_getTransactionReceipt | 1 | check | check  
eth_getUncleByBlockHashAndIndex | 1 | check | check  
eth_getUncleByBlockNumberAndIndex | 1 | check | check  
eth_getUncleCountByBlockHash | 1 | check | check  
eth_getUncleCountByBlockNumber | 1 | check | check  
eth_maxPriorityFeePerGas | 1 | check | check  
eth_subscribe | 1 | check | check  
eth_syncing | 1 | check | check  
eth_unsubscribe | 1 | check | check  
eth_sendRawTransaction | 1 | check | check  
net_listening | 1 | check | check  
net_peerCount | 1 | check | check  
net_version | 1 | check | check  
txpool_inspect | 50 | close | check  
txpool_status | 50 | check | check  
web3_clientVersion | 1 | check | check  
web3_sha3 | 1 | check | check  
trace_block | 50 | check | close  
trace_call | 50 | check | close  
trace_replayBlockTransactions | 100 | check | close  
trace_replayTransaction | 100 | check | close  
trace_transaction | 50 | check | close  
debug_getBadBlocks | 50 | close | check  
debug_storageRangeAt | 50 | check | check  
debug_traceBlock | 50 | check | check  
debug_traceBlockByHash | 50 | check | check  
debug_traceBlockByNumber | 50 | check | check  
debug_traceCall | 50 | close | check  
debug_traceTransaction | 50 | check | check  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
