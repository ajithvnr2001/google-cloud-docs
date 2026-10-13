---
url: https://docs.cloud.google.com/nodejs/docs/reference/connect-datastore/latest/
title: THIS REPOSITORY AND PACKAGE WILL BE DEPRECATED IN JULY 2024 \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:35.072127+00:00
---

# THIS REPOSITORY AND PACKAGE WILL BE DEPRECATED IN JULY 2024  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/connect-datastore/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  THIS REPOSITORY AND PACKAGE WILL BE DEPRECATED IN JULY 2024 Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 7.0.1 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/connect-datastore/latest/)
  * [ 7.0.0 ](https://docs.cloud.google.com/nodejs/docs/reference/connect-datastore/7.0.0/)
  * [ 6.0.1 ](https://docs.cloud.google.com/nodejs/docs/reference/connect-datastore/6.0.1/)
  * [ 5.0.3 ](https://docs.cloud.google.com/nodejs/docs/reference/connect-datastore/5.0.3/)



# Google Cloud Datastore Sessions

[![NPM](https://img.shields.io/npm/v/@google-cloud/connect-datastore.svg?style=flat)](https://www.npmjs.org/package/@google-cloud/connect-datastore)

**@google-cloud/connect-datastore** is a [Google Cloud Datastore](https://cloud.google.com/datastore/docs) session store backed by [@google-cloud/datastore](https://www.npmjs.com/package/@google-cloud/datastore).

**Note:** Cloud Datastore is a persistent, distributed, transactional database. Often, it's more appropriate to choose a different storage solution for sessions such as Memcache or Redis as their designs offer much faster operation in this use case.

## Installation
    
    
    npm install @google-cloud/connect-datastore
    

## Configuration

You must have a Google Cloud project and credentials.

See [gcloud node's documentation](https://cloud.google.com/docs/authentication/getting-started) on setting up authentication.

## Usage Example
    
    
    const {Datastore} = require('[@google-cloud/datastore](https://docs.cloud.google.com/nodejs/docs/reference/datastore/latest/overview.html)');
    const {DatastoreStore} = require('[@google-cloud/connect-datastore](https://docs.cloud.google.com/nodejs/docs/reference/connect-datastore/latest/overview.html)');
    const express = require('express');
    const session = require('express-session');
    
    const app = express();
    
    app.use(session({
      store: new [DatastoreStore](https://docs.cloud.google.com/nodejs/docs/reference/connect-datastore/latest/connect-datastore/datastorestore.html)({
        kind: 'express-sessions',
    
        // Optional: expire the session after this many milliseconds.
        // note: datastore does not automatically delete all expired sessions
        // you may want to run separate cleanup requests to remove expired sessions
        // 0 means do not expire
        expirationMs: 0,
    
        dataset: new Datastore({
    
          // For convenience, @google-cloud/datastore automatically looks for the
          // GCLOUD_PROJECT environment variable. Or you can explicitly pass in a
          // project ID here:
          projectId: process.env.GCLOUD_PROJECT,
    
          // For convenience, @google-cloud/datastore automatically looks for the
          // GOOGLE_APPLICATION_CREDENTIALS environment variable. Or you can
          // explicitly pass in that path to your key file here:
          keyFilename: process.env.GOOGLE_APPLICATION_CREDENTIALS
        })
      }),
      secret: 'my-secret'
    }));
    

## Expiration

If a session is fetched with the delta between the createdAt time and current time greater than expirationMs, the session will not be returned and will instead be destroyed.

Datastore does not support a `ttl`, and tokens are only deleted if a session is fetched. You will likely want to implement logic to occasionally delete expired sessions.

## Contributing

  * See [CONTRIBUTING.md](https://github.com/googleapis/nodejs-datastore-session/blob/master/CONTRIBUTING.md)



## License

  * Apache 2.0 - See [LICENSE](https://github.com/googleapis/nodejs-datastore-session/blob/master/LICENSE)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
