---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/
title: Cloud Firestore: Node.js Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:45.203036+00:00
---

# Cloud Firestore: Node.js Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Firestore: Node.js Client Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/firestore.svg)](https://www.npmjs.com/package/@google-cloud/firestore)

This is the Node.js Server SDK for [Google Cloud Firestore](https://firebase.google.com/docs/firestore/). Google Cloud Firestore is a NoSQL document database built for automatic scaling, high performance, and ease of application development.

This Cloud Firestore Server SDK uses Google’s Cloud Identity and Access Management for authentication and should only be used in trusted environments. Your Cloud Identity credentials allow you bypass all access restrictions and provide read and write access to all data in your Cloud Firestore project.

The Cloud Firestore Server SDKs are designed to manage the full set of data in your Cloud Firestore project and work best with reliable network connectivity. Data operations performed via these SDKs directly access the Cloud Firestore backend and all document reads and writes are optimized for high throughput.

Applications that use Google's Server SDKs should not be used in end-user environments, such as on phones or on publicly hosted websites. If you are developing a Web or Node.js application that accesses Cloud Firestore on behalf of end users, use the firebase Client SDK.

**Note:** This Cloud Firestore Server SDK does not support Firestore databases created in [Datastore mode](https://cloud.google.com/datastore/docs/firestore-or-datastore#in_datastore_mode). To access these databases, use the [Datastore SDK](https://www.npmjs.com/package/@google-cloud/datastore).

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/nodejs-firestore/blob/main/CHANGELOG.md).

  * [Cloud Firestore Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/firestore/latest)
  * [Cloud Firestore Documentation](https://cloud.google.com/firestore)
  * [github.com/googleapis/nodejs-firestore](https://github.com/googleapis/nodejs-firestore)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart
    * Before you begin
    * Installing the client library
    * Using the client library
  * Samples
  * Versioning
  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable the Cloud Firestore API](https://console.cloud.google.com/flows/enableapi?apiid=firestore.googleapis.com).
  3. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation.



### Installing the client library
    
    
    npm install @google-cloud/firestore
    

### Using the client library
    
    
    const {Firestore} = require('[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)');
    
    // Create a new client
    const firestore = new [Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore.html)();
    
    async function quickstart() {
      // Obtain a document reference.
      const document = firestore.doc('posts/intro-to-firestore');
    
      // Enter new data into the document.
      await document.set({
        title: 'Welcome to Firestore',
        body: 'Hello World',
      });
      console.log('Entered new data into the document');
    
      // Update an existing document.
      await document.update({
        body: 'My first Firestore app',
      });
      console.log('Updated an existing document');
    
      // Read the document.
      const doc = await document.get();
      console.log('Read the document');
    
      // Delete the document.
      await document.delete();
      console.log('Deleted the document');
    }
    quickstart();
    

### Using the client library with Pipelines
    
    
    const {Firestore} = require('[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)');
    
    // Require/import Pipelines from '@google-cloud/firestore/pipelines'
    const {field} = require('@google-cloud/firestore/pipelines');
    
    // Create a new client
    const firestore = new [Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore.html)({
      projectId: 'firestore-sdk-nightly',
      databaseId: 'enterprise'
    });
    
    async function pipelinesQuickstart() {
      // Obtain a collection reference.
      const collection = firestore.collection('books');
    
      // Enter new documents into the document.
      await collection.add({
        "title": "Whispers of the Cobalt Sea",
        "price": 12.99,
        "author": "Elara Vance",
        "yearPublished": 2023
      });
      await collection.add({
        "title": "The Antigravity Cat's Guide to Napping",
        "price": 24.50,
        "author": "Mittens the IV",
        "yearPublished": 2026
      });
      console.log('Entered new documents into the collection.');
    
      // Define a Pipeline query that selects books published this century,
      // orders them by price, and computes a discounted price (20% off).
      const pipeline = firestore.pipeline().collection('books')
          .where(field('yearPublished').greaterThanOrEqual(2000))
          .[sort](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline.html)(field('price').ascending())
          .select('title', 'author', field('price').multiply(0.8).as('discountedPrice'));
    
      // Execute the pipeline
      const pipelineSnapshot = await pipeline.execute();
      console.log('Executed the Pipeline.');
    
      console.log('Results:');
      pipelineSnapshot.results.forEach(pipelineResult=> {
        console.log(pipelineResult.data());
      });
    }
    pipelinesQuickstart();
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/nodejs-firestore/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
Limit-to-last-query | [source code](https://github.com/googleapis/nodejs-firestore/blob/main/samples/limit-to-last-query.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-firestore&page=editor&open_in_editor=samples/limit-to-last-query.js,samples/README.md)  
Pipelines-quickstart | [source code](https://github.com/googleapis/nodejs-firestore/blob/main/samples/pipelines-quickstart.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-firestore&page=editor&open_in_editor=samples/pipelines-quickstart.js,samples/README.md)  
Quickstart | [source code](https://github.com/googleapis/nodejs-firestore/blob/main/samples/quickstart.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-firestore&page=editor&open_in_editor=samples/quickstart.js,samples/README.md)  
Solution-counters | [source code](https://github.com/googleapis/nodejs-firestore/blob/main/samples/solution-counters.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-firestore&page=editor&open_in_editor=samples/solution-counters.js,samples/README.md)  
  
The [Cloud Firestore Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/firestore/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/firestore@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-firestore/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/nodejs-firestore/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
