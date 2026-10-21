---
url: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-quickstart/
title: Client library quickstart \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:28:25.190352+00:00
---

# Client library quickstart  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/kubernetes-engine/docs/samples)



#  Client library quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Use the Node.js GKE cluster admin client library. 

## Code sample

### Node.js

To authenticate to GKE, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const container = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)');
    
    // Create the Cluster Manager Client
    const client = new container.v1.[ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
    async function quickstart() {
      const zone = 'us-central1-a';
      const projectId = await client.getProjectId();
      const request = {
        projectId: projectId,
        zone: zone,
      };
    
      const [response] = await client.listClusters(request);
      console.log('Clusters: ', response);
    }
    quickstart();

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=container). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
