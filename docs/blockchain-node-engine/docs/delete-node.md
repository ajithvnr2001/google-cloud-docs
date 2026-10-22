---
url: https://docs.cloud.google.com/blockchain-node-engine/docs/delete-node/
title: Delete a blockchain node \u00a0|\u00a0 Blockchain Node Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:16.909437+00:00
---

# Delete a blockchain node  |  Blockchain Node Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-node-engine/docs/delete-node/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain Node Engine ](https://docs.cloud.google.com/blockchain-node-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-node-engine/docs/overview)



Send feedback 

#  Delete a blockchain node Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete a Blockchain Node Engine node using the console or an API call.

**Note:** While the blockchain node is being deleted, the response to the [ListBlockchainNode](https://docs.cloud.google.com/blockchain-node-engine/docs/reference/rest/v1/projects.locations.blockchainNodes/list) command continues to display the node, but shows its state as **DELETING**.

## Using the console

To delete a node using the console:

  1. In the Google Cloud console, go to the **Blockchain Node Engine** page.

[Go to Blockchain Node Engine](https://console.cloud.google.com/blockchain-node-engine)

The **Nodes** list page is displayed by default.

[![Blockchain Node Engine Nodes list user interface](https://docs.cloud.google.com/static/blockchain-node-engine/images/nodes-list.png)](https://docs.cloud.google.com/static/blockchain-node-engine/images/nodes-list.png)

  2. Click more_vert **More** > delete **Delete** next to the intended node.

  3. Type the node name in the confirmation dialog and then click **Delete node**.




## Using an API

To delete a blockchain node using [DeleteBlockchainNode](https://docs.cloud.google.com/blockchain-node-engine/docs/reference/rest/v1/projects.locations.blockchainNodes/delete), send the following request:
    
    
    curl -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
    https://blockchainnodeengine.googleapis.com/v1/projects/PROJECT_ID/\
    locations/LOCATION/blockchainNodes/NODE_NAME
    

Where:

  * PROJECT_ID is your Google Cloud project ID. For example, `my-project-id`.
  * LOCATION is the [location](https://docs.cloud.google.com/blockchain-node-engine/docs/terms#location) in which your resources are hosted. For example, `us-central1`.
  * NODE_NAME is the name of the node you created in [Create a blockchain node](https://docs.cloud.google.com/blockchain-node-engine/docs/create-node). For example, `my-node`.



Here is a sample response to the above command:
    
    
    {
      "name": "projects/my-project-id/locations/us-central1/operations/
        operation-1669730507366-5ee9c6dc31fc4-ab3b364d-76c83243",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.blockchainnodeengine.v1.
          OperationMetadata",
        "createTime": "2022-11-29T14:01:47.448829624Z",
        "target": "projects/my-project-id/locations/us-central1/blockchainNodes/
          my-node",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
