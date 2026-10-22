---
url: https://docs.cloud.google.com/blockchain-node-engine/docs/operation-status/
title: Check operation status \u00a0|\u00a0 Blockchain Node Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:33.763731+00:00
---

# Check operation status  |  Blockchain Node Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-node-engine/docs/operation-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain Node Engine ](https://docs.cloud.google.com/blockchain-node-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-node-engine/docs/overview)



Send feedback 

#  Check operation status Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to list all long-running operations and how to view the status of a long-running operation.

To check the status and display any additional error details of a long-running operation, you'll need to get the value for OPERATION_NAME first, and then you can request status.

## ListOperations

To list all long-running operations, send the following request:
    
    
    curl \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://blockchainnodeengine.googleapis.com/v1/projects/PROJECT_ID/\
    locations/LOCATION/operations
    

Where:

  * PROJECT_ID is your Google Cloud project ID. For example, `my-project-id`.
  * LOCATION is the [location](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#location) in which your resources are hosted. For example, `us-central1`.



Here is a sample response to this command:
    
    
    {
      "operations": [
        {
          "name": "projects/my-project-id/locations/us-central1/operations/operation-1683321573175-5faf8d8696fe0-5f1906e4-eb1b6828",
          "metadata": {
            "@type": "type.googleapis.com/google.cloud.blockchainnodeengine.v1.OperationMetadata",
            "createTime": "2023-05-05T21:19:33.245698045Z",
            "endTime": "2023-05-05T21:58:44.520319810Z",
            "target": "projects/my-project-id/locations/us-central1/blockchainNodes/my-new-node-2",
            "verb": "create",
            "requestedCancellation": false,
            "apiVersion": "v1"
          },
          "done": true,
          "response": {
            "@type": "type.googleapis.com/google.cloud.blockchainnodeengine.v1.BlockchainNode",
            "name": "projects/my-project-id/locations/us-central1/blockchainNodes/my-new-node-2",
            "createTime": "2023-05-05T21:19:33.308756Z",
            "updateTime": "2023-05-05T21:58:44.513286Z",
            "labels": {
              "label-key": "label-value"
            },
            "blockchainType": "ETHEREUM",
            "connectionInfo": {
              "ipInfo": {
                "rpcIpv4Address": "203.0.113.1"
              },
              "endpointInfo": {
                "jsonRpcApiEndpoint": "json-rpc.4amkczs2vkh8hjtghcipu7y2t.blockchainnodeengine.com",
                "websocketsApiEndpoint": "ws.4amkczs2vkh8hjtghcipu7y2t.blockchainnodeengine.com"
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
                "beaconApiEndpoint": "beacon.4amkczs2vkh8hjtghcipu7y2t.blockchainnodeengine.com",
                "beaconPrometheusMetricsApiEndpoint": "bc-mc.4amkczs2vkh8hjtghcipu7y2t.blockchainnodeengine.com"
              }
            },
            "state": "RUNNING"
          }
        }
      ]
    }
    

Make a note of the OPERATION_ID, which looks like the following:
    
    
    "name": "projects/my-project-id/locations/us-central1/operations/
        operation-1683321573175-5faf8d8696fe0-5f1906e4-eb1b6828",
    

**Note:** You can also get this information using [ListBlockchainNodes](https://docs.cloud.google.com/blockchain-node-engine/docs/reference/rest/v1/projects.locations.blockchainNodes/list).

## GetOperation

When you send a request and get a response, for example from [CreateBlockchainNode](https://docs.cloud.google.com/blockchain-node-engine/docs/reference/rest/v1/projects.locations.blockchainNodes/create) or [DeleteBlockchainNode](https://docs.cloud.google.com/blockchain-node-engine/docs/reference/rest/v1/projects.locations.blockchainNodes/delete), the response includes the OPERATION_ID:
    
    
      "name": "projects/my-project-id/locations/us-central1/operations/
        operation-1683321573175-5faf8d8696fe0-5f1906e4-eb1b6828",
    

For this example, you'd set OPERATION_NAME to `operation-1683321573175-5faf8d8696fe0-5f1906e4-eb1b6828`.

You can also get the operation name from the results of the [ListOperations](https://docs.cloud.google.com/blockchain-node-engine/docs/reference/rest/v1/projects.locations.operations/list) command.

Once you have the value for OPERATION_NAME, send the following request:
    
    
    curl \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
    https://blockchainnodeengine.googleapis.com/v1/projects/PROJECT_ID/\
    locations/LOCATION/operations/OPERATION_NAME
    

Where:

  * PROJECT_ID is your Google Cloud project ID. For example `my-project-id`.
  * LOCATION is the [location](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#location) in which your resources are hosted. For example, `us-central1`.
  * OPERATION_NAME is a string specifying the operation. For example, `operation-1683321573175-5faf8d8696fe0-5f1906e4-eb1b6828`.



Here is an example response to the above command:
    
    
    {
      "name": "projects/my-project-id/locations/us-central1/operations/operation-1683321573175-5faf8d8696fe0-5f1906e4-eb1b6828",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.blockchainnodeengine.v1.OperationMetadata",
        "createTime": "2023-05-05T21:19:33.245698045Z",
        "endTime": "2023-05-05T21:58:44.520319810Z",
        "target": "projects/my-project-id/locations/us-central1/blockchainNodes/my-new-node-2",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.blockchainnodeengine.v1.BlockchainNode",
        "name": "projects/my-project-id/locations/us-central1/blockchainNodes/my-new-node-2",
        "createTime": "2023-05-05T21:19:33.308756Z",
        "updateTime": "2023-05-05T21:58:44.513286Z",
        "labels": {
          "label-key": "label-value"
        },
        "blockchainType": "ETHEREUM",
        "connectionInfo": {
          "ipInfo": {
            "rpcIpv4Address": "203.0.113.1"
          },
          "endpointInfo": {
            "jsonRpcApiEndpoint": "json-rpc.4amkczs2vkh8hjtghcipu7y2t.blockchainnodeengine.com",
            "websocketsApiEndpoint": "ws.4amkczs2vkh8hjtghcipu7y2t.blockchainnodeengine.com"
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
            "beaconApiEndpoint": "beacon.4amkczs2vkh8hjtghcipu7y2t.blockchainnodeengine.com",
            "beaconPrometheusMetricsApiEndpoint": "bc-mc.4amkczs2vkh8hjtghcipu7y2t.blockchainnodeengine.com"
          }
        },
        "state": "RUNNING"
      }
    }
    

**Note:** You can also get this information using [GetBlockchainNode](https://docs.cloud.google.com/blockchain-node-engine/docs/reference/rest/v1/projects.locations.blockchainNodes/get).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
