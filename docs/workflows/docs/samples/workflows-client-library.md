---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-client-library/
title: Get started with the Cloud Client Libraries for the Workflows API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:14.239090+00:00
---

# Get started with the Cloud Client Libraries for the Workflows API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-client-library/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Get started with the Cloud Client Libraries for the Workflows API Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates getting started with the Cloud Client Libraries for Workflows.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Workflows client libraries](https://docs.cloud.google.com/workflows/docs/reference/libraries)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/workflows/v1/workflows_client.h"
    #include "google/cloud/location.h"
    #include <iostream>
    
    int main(int argc, char* argv[]) try {
      if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " project-id location-id\n";
        return 1;
      }
    
      auto const location = google::cloud::Location(argv[1], argv[2]);
    
      namespace workflows = ::google::cloud::workflows_v1;
      auto client =
          workflows::WorkflowsClient(workflows::MakeWorkflowsConnection());
    
      for (auto w : client.ListWorkflows(location.FullName())) {
        if (!w) throw std::move(w).status();
        std::cout << w->DebugString() << "\n";
      }
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Node.js API reference documentation](https://googleapis.dev/nodejs/workflows/latest/). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {WorkflowsClient} = require('@google-cloud/workflows');
    const client = new WorkflowsClient();
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project';
    // const location = 'us-central1';
    
    async function listWorkflows(projectId, location) {
      const [workflows] = await client.listWorkflows({
        parent: client.locationPath(projectId, location),
      });
      for (const workflow of workflows) {
        console.info(`name: ${workflow.name}`);
      }
    }
    
    listWorkflows(projectId, location).catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Node.js API reference documentation](https://googleapis.dev/nodejs/workflows/latest/). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import {WorkflowsClient} from '@google-cloud/workflows';
    const client = new WorkflowsClient();
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project';
    // const location = 'us-central1';
    
    async function listWorkflows(projectId: string, location: string) {
      const [workflows] = await client.listWorkflows({
        parent: client.locationPath(projectId, location),
      });
      for (const workflow of workflows) {
        console.info(`name: ${workflow.name}`);
      }
    }
    
    listWorkflows(projectId, location).catch((err: Error) => {
      console.error(err.message);
      process.exitCode = 1;
    });

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
