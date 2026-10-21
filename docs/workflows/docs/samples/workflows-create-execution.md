---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-create-execution/
title: Create execution \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:21.310015+00:00
---

# Create execution  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-create-execution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Create execution Stay organized with collections  Save and categorize content based on your preferences. 

Creates a workflow execution.

## Code sample

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Node.js API reference documentation](https://googleapis.dev/nodejs/workflows/latest/). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {ExecutionsClient} = require('@google-cloud/workflows');
    const client = new ExecutionsClient();
    
    async function createExecution(projectId, location, name) {
      /**
       * TODO(developer): Uncomment these variables before running the sample.
       */
      // const projectId = 'my-project';
      // const location = 'us-central1';
      // const name = 'my-test-workflow';
    
      const [resp] = await client.createExecution({
        parent: client.workflowPath(projectId, location, name),
      });
      console.info(`name: ${resp.name}`);
    }
    
    createExecution(projectId, location, name).catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Node.js API reference documentation](https://googleapis.dev/nodejs/workflows/latest/). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import {ExecutionsClient} from '@google-cloud/workflows';
    const client: ExecutionsClient = new ExecutionsClient();
    
    async function createExecution(
      projectId: string,
      location: string,
      name: string
    ) {
      /**
       * TODO(developer): Uncomment these variables before running the sample.
       */
      // const projectId = 'my-project';
      // const location = 'us-central1';
      // const name = 'my-test-workflow';
    
      const [resp] = await client.createExecution({
        parent: client.workflowPath(projectId, location, name),
      });
      console.info(`name: ${resp.name}`);
    }
    
    createExecution(projectId, location, name).catch((err: Error) => {
      console.error(err.message);
      process.exitCode = 1;
    });

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
