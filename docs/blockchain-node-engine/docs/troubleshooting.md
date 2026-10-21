---
url: https://docs.cloud.google.com/blockchain-node-engine/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Blockchain Node Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:38.433035+00:00
---

# Troubleshooting  |  Blockchain Node Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-node-engine/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain Node Engine ](https://docs.cloud.google.com/blockchain-node-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-node-engine/docs/overview)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page describes some common Blockchain Node Engine errors and how to fix them.

## Could not resolve host

The following error occurs when you try and use the blockchain node while it is still being created:

`Could not resolve host: json-rpc.abc1234.blockchainnodeengine.com`

To resolve this issue, wait for the node to reach a RUNNING state. You can see the status as described in [List blockchain nodes](https://docs.cloud.google.com/blockchain-node-engine/docs/node-list).

## 400 error: Method doesn't allow unregistered callers

The following error occurs when you try and use the blockchain node without an API key:

`400 error: Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`

To resolve this issue, see: [Create an API key](https://docs.cloud.google.com/blockchain-node-engine/docs/using-nodes#create-api-key)

## I don't know if my node has finished syncing

To resolve this issue, do one of the following:

  * **Full nodes:** Make a call to `eth_syncing` and if you get a `false` response, then it is done.
        
        curl -H POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","id":2586,"method":"eth_syncing","params":[]}]}' https://<executionClientJsonRpcEndpoint>?key=<API_KEY>
        
        
        {"jsonrpc":"2.0","id":2586,"result":false}
        

  * **Archive nodes:** Query the metrics endpoint `executionClientPrometheusMetricsApiEndpoint`:
        
        curl -H "Content-Type: application/json" 'http://<executionClientPrometheusMetricsApiEndpoint>/debug/metrics/prometheus?key=<API_KEY>'
        

Look for the `block_hashes` value in the response.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
