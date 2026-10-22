---
url: https://docs.cloud.google.com/functions/docs/samples/functions-concepts-node-termination-http/
title: Node.js: terminate HTTP connection \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:04.460398+00:00
---

# Node.js: terminate HTTP connection  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-concepts-node-termination-http/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Node.js: terminate HTTP connection Stay organized with collections  Save and categorize content based on your preferences. 

Show how to terminate an HTTP connection in Node.js

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [The Node.js Runtime](https://docs.cloud.google.com/functions/1stgendocs/concepts/nodejs-runtime)
  * [The Node.js runtime](https://docs.cloud.google.com/run/docs/runtimes/nodejs)



## Code sample

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // OK: await-ing a Promise before sending an HTTP response
    await Promise.resolve();
    
    // WRONG: HTTP functions should send an
    // HTTP response instead of returning.
    return Promise.resolve();
    
    // HTTP functions should signal termination by returning an HTTP response.
    // This should not be done until all background tasks are complete.
    res.status(200).send();
    
    // WRONG: this may not execute since an
    // HTTP response has already been sent.
    return Promise.resolve();

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
