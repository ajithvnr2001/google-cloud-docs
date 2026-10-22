---
url: https://docs.cloud.google.com/appengine/docs/standard/nodejs/specifying-dependencies/
title: Specifying dependencies \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:21.236796+00:00
---

# Specifying dependencies  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/nodejs/specifying-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
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
    

During deployment, the Node.js runtime [automatically installs](https://docs.cloud.google.com/appengine/docs/standard/nodejs/runtime#dependencies) all `dependencies` declared in your `package.json` file. By default, the `npm install` command is used, however Yarn and Pnpm package managers are also supported:

  * Yarn: If a `yarn.lock` file exists, the `yarn install --production` command is used instead.

  * Pnpm: If a `pnpm-lock.yaml` file exists, the `pnpm install` command is used instead.




Note that you must ensure that the `yarn.lock` or `pnpm-lock.yaml` file is not specified in the `skip_files` section of your `app.yaml` file.

By default, App Engine caches fetched dependencies to reduce build times. To install an uncached version of the dependency, use the command:
    
    
    gcloud app deploy --no-cache
    

Support and limitations for the `package.json` file in the standard environment:

  * You can use any Linux-compatible Node.js package with App Engine, including packages that require native (C) extensions.

  * If the `engines` field is specified in your `package.json`, you must define a [compatible Node.js version](https://docs.cloud.google.com/appengine/docs/standard/nodejs/runtime#nodejs_version).

  * All dependencies that you define under the `devDependencies` field are ignored and do not get installed for your app in App Engine.

  * The `start` script should be lightweight and exclude build steps for the best performance because the script runs each time a new instance of your application is created.




### Private dependencies with Artifact Registry

If your app uses a [private npm module](https://docs.npmjs.com/creating-and-publishing-private-packages), you can use an [Artifact Registry Node.js package repository](https://docs.cloud.google.com/artifact-registry/docs/nodejs/store-nodejs) to host private dependencies. When deploying your app, the build process automatically generates Artifact Registry credentials for the [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) so you won't need to generate additional credentials. To include private dependencies, list the Artifact Registry repository and configure settings for authenticating with the registry in your `.npmrc` file in the app directory. For example:
    
    
    @SCOPE:registry=https://REGION_ID-npm.pkg.dev/PROJECT_ID/REPOSITORY_NAME
    //REGION_ID-npm.pkg.dev/PROJECT_ID/REPOSITORY_NAME:always-auth=true
    

Note that this approach also works for Yarn v1 package manager. If you are using Yarn v2 or higher, list the Artifact Registry repository and configure settings for authenticating with the registry in your `.yarnrc.yml` file in the app directory. For example:
    
    
    npmScopes:
      SCOPE:
        npmRegistryServer: https://REGION_ID-npm.pkg.dev/PROJECT_ID/REPOSITORY_NAME
        npmAlwaysAuth: true
    

Afterwards, include your packages in the `package.json` file. For example:
    
    
    {
      "dependencies": {
        " @SCOPE/my-package": "^1.0.0"
      }
    }
    

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
