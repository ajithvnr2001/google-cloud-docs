---
url: https://docs.cloud.google.com/build/docs/samples/cloudbuild-list-build-triggers/
title: List build triggers \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:56:19.971064+00:00
---

# List build triggers  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/samples/cloudbuild-list-build-triggers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Samples ](https://docs.cloud.google.com/build/docs/samples)



#  List build triggers Stay organized with collections  Save and categorize content based on your preferences. 

List build triggers with the client libraries.

## Code sample

### Node.js

To authenticate to Cloud Build, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function listBuildTriggers(
      projectId = 'YOUR_PROJECT_ID' // Your Google Cloud Platform project ID
    ) {
      // Imports the Google Cloud client library
      const {CloudBuildClient} = require('[@google-cloud/cloudbuild](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/overview.html)');
    
      // Creates a client
      const cb = new [CloudBuildClient](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/overview.html)();
    
      // What project should we list triggers for?
      const request = {
        projectId,
      };
    
      const [result] = await cb.listBuildTriggers(request);
      console.info(JSON.stringify(result, null, 2));
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudbuild). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
