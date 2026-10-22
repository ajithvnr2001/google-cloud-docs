---
url: https://docs.cloud.google.com/blockchain-rpc/docs/quickstart/
title: Quickstart: Blockchain RPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:13.595316+00:00
---

# Quickstart: Blockchain RPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-rpc/docs/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain RPC ](https://docs.cloud.google.com/blockchain-rpc/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-rpc/docs/overview)



Send feedback 

#  Quickstart: Blockchain RPC Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Required roles

To get the permissions that you need to view API keys, ask your administrator to grant you the [API Key Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.apiKeysViewer) (`roles/serviceusage.apiKeysViewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Using the RPC endpoint

  1. In the Google Cloud console, go to the Blockchain RPC page.

[Go Blockchain RPC](https://console.cloud.google.com/blockchain/rpc)

  2. From the console, copy the JSON-RPC endpoint that matches the `network` and `location` combination you need. 

![Blockchain RPC quickstart](https://docs.cloud.google.com/static/blockchain-rpc/images/blockchain-rpc-json-rpc.png)

  3. Now you can begin making requests. A full list of all the RPC methods available are listed in the [RPC API](https://docs.cloud.google.com/blockchain-rpc/docs/rpc-api) reference documentation. Our example request calls the `eth_blockNumber` method.



    
    
    curl -X POST -H "Content-Type: application/json" -d '{
      "jsonrpc": "2.0",
      "id": 1,
      "method":
      "eth_blockNumber",
      "params": []}' \
    JSON_RPC_ENDPOINT
    

Where:

  * JSON_RPC_ENDPOINT is an endpoint you copied from the console. This endpoint includes a default API key that has been automatically created. You can manage all of your keys on the [Credentials](https://docs.cloud.google.com/apis/credentials) page.



After executing this curl request, you should see a response like:
    
    
    {"jsonrpc":"2.0","id":1,"result":"0x13acb8d"}
    

## Using WebSocket subscriptions

WebSocket support is also enabled for Blockchain RPC endpoints. This example uses the [wscat](https://github.com/websockets/wscat) open source project.

  1. In the Google Cloud console, go to the Blockchain RPC page.

[Go Blockchain RPC](https://console.cloud.google.com/blockchain/rpc)

  2. From the console, copy the WebSocket endpoint that matches the `network` and `location` combination you need. 

![Blockchain RPC quickstart](https://docs.cloud.google.com/static/blockchain-rpc/images/blockchain-rpc-websocket.png)

  3. Now you can begin making requests.



    
    
    wscat -c WS_ENDPOINT
    

Where:

  * WS_ENDPOINT is a WebSocket endpoint from the console.



Subscribe to new block headers:
    
    
    {"id":1,"jsonrpc":"2.0","method":"eth_subscribe","params":["newHeads"]}
    

You'll start receiving messages for each new block header.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
