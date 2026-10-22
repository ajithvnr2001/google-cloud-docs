---
url: https://docs.cloud.google.com/appengine/docs/flexible/nodejs/specifying-dependencies/
title: Specifying dependencies \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:34.126976+00:00
---

# Specifying dependencies  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/nodejs/specifying-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Specifying dependencies Stay organized with collections  Save and categorize content based on your preferences. 

You specify the dependencies for your Node.js app by declaring them in the `package.json` file.

For example, if you want to specify [Lodash](https://lodash.com/) as a dependency, your `package.json` file might look as follows:
    
    
    {
      "dependencies": {
        "lodash": "^4.0.1"
      }
    }
    

You can use any Linux-compatible Node.js package with App Engine flexible environment, including packages that require native (C) extensions.

During deployment, the Node.js runtime [automatically installs](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/runtime#dependencies) all `dependencies` declared in your `package.json` file. By default, the `npm install` command is used, however Yarn and Pnpm package managers are also supported:

  * Yarn: If a `yarn.lock` file exists, the `yarn install --production` command is used instead.

  * Pnpm: Supported only by Node.js runtimes version 18 and version 20 (preview). If a `pnpm-lock.yaml` file exists, the `pnpm install` command is used instead.




Note that you must ensure that the `yarn.lock` or `pnpm-lock.yaml` file is not specified in the `skip_files` section of your `app.yaml` file.

## Installing a web framework

You'll need to use a web framework to enable your app to serve web requests. You can use any Node.js web framework including the following:

  * [Express.js](http://expressjs.com/)
  * [Hapi.js](http://hapijs.com/)
  * [Loopback.js](http://loopback.io/)
  * [Koa.js](http://koajs.com/)
  * [Kraken.js](http://krakenjs.com/)
  * [Restify.js](http://restify.com/)
  * [Sails.js](http://sailsjs.org/)



To use a particular web framework, such as [Express.js](https://expressjs.com/), add the framework to your `package.json` file:

  * Using [npm](https://www.npmjs.com/):
        
        npm install express

  * Using [yarn](https://yarnpkg.com/):
        
        yarn add express

  * Using [pnpm](https://pnpm.io/):
        
        pnpm add express




For example, the resulting `package.json` file might look as follows:
    
    
    {
      "dependencies": {
        "lodash": "^4.0.1",
        "express": "^4.16.2"
      }
    }
    

## Installing the Cloud Client Libraries

The [Cloud Client Libraries for Node.js](https://docs.cloud.google.com/nodejs/docs/reference) is the idiomatic way for Node.js developers to integrate with Google Cloud services, such as [Firestore in Datastore mode (Datastore)](https://docs.cloud.google.com/datastore/docs/reference/libraries) and [Cloud Storage](https://docs.cloud.google.com/storage/docs/reference/libraries).

To install the Node.js client library for Cloud Storage:

  1. Install the Cloud Client Libraries locally by using a package manager:

     * To use `npm`, run:
           
           npm install @google-cloud/storage

     * To use `yarn`, run:
           
           yarn add @google-cloud/storage

     * To use `pnpm`, run:
           
           pnpm add @google-cloud/storage

  2. Set up authentication. You can configure the Cloud Client Libraries for Node.js to [handle authentication automatically](https://docs.cloud.google.com/docs/authentication/client-libraries).

  3. Use the [Node.js client library for Cloud Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest) reference to implement support for the Cloud Storage service in your app.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
