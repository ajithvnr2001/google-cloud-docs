---
url: https://docs.cloud.google.com/functions/1stgendocs/concepts/nodejs-runtime/
title: The Node.js Runtime \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:27.659989+00:00
---

# The Node.js Runtime  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/concepts/nodejs-runtime/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# The Node.js Runtime

Your Cloud Run function runs in an environment consisting of an operating system version plus add-on packages, language support, and the Functions Framework library that supports and invokes your function. This environment is identified by the language version, and is known as the runtime.

For information about runtimes in general, and to learn which Ubuntu version each Node.js runtime uses, see the [Cloud Run functions execution environment](https://docs.cloud.google.com/static/functions/1stgendocs/concepts/execution-environment#node.js).

To start building and deploying Cloud Run functions with Node.js, see the [Quickstart](https://docs.cloud.google.com/functions/1stgendocs/create-deploy-gcloud-1st-gen).

To build and test your functions on your local system, see [Run Functions with Functions Framework](https://docs.cloud.google.com/functions/1stgendocs/running/function-frameworks).

## Select the runtime

Cloud Run functions supports several versions of Node.js, listed on the [Runtime support](https://docs.cloud.google.com/static/functions/1stgendocs/runtime-support#node.js) page. You can select the preferred Node.js runtime for your function during deployment. See [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy#basics) for details on deploying from the Google Cloud CLI.

## Execution environment

The execution environment includes the runtime, the operating system, packages, and a library that invokes your function.

Node.js 18 and newer versions use an execution environment based on Ubuntu 22.04. Versions earlier than Node.js 18 are based on Ubuntu 18.04. See [Cloud Run functions execution environment](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment#runtimes) for more information.

The library that invokes your function is the [Node.js Functions Framework](https://docs.cloud.google.com/functions/1stgendocs/functions-framework).

## Source code structure

In order for Cloud Run functions to find your function's definition, each runtime has certain structuring requirements for your source code. See [Writing Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/writing#structuring_source_code) for more information.

## Specify dependencies

You can specify dependencies for your functions by listing them in a `package.json` file. For more information, see [Specifying dependencies in Node.js](https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-nodejs).

## NPM build script

By default, the Node.js runtime executes `npm run build` if a `build` script is detected in `package.json`. If you require additional control over your build steps before starting your application, you can provide a [custom build step](https://docs.cloud.google.com/docs/buildpacks/nodejs#executing_custom_build_steps_during_deployment) by adding a `gcp-build` script to your `package.json` file.

You can prevent your build from running the `npm run build` script by either:

  * Adding a `gcp-build` script with an empty value in your `package.json` file: `"gcp-build":""`.

  * Setting the build environment variable `GOOGLE_NODE_RUN_SCRIPTS` to the empty string to prevent all scripts from running.




## Asynchronous function completion

When working with asynchronous tasks that involve callbacks or `Promise` objects, you must explicitly inform the runtime that your function has finished executing these tasks. You can do this in several different ways, as shown in the following samples. The key is that your code must wait for the asynchronous task or `Promise` to complete before returning; otherwise the asynchronous component of your function may be terminated before it completes.

### Event-driven functions

**Implicit return**
    
    
      exports.implicitlyReturning = async (event, context) => {
        return await asyncFunctionThatReturnsAPromise();
      };
    

**Explicit return**
    
    
      exports.explicitlyReturning = function (event, context) {
        return asyncFunctionThatReturnsAPromise();
      };
    

### HTTP functions

###  Node.js 
    
    
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

**Warning:** failure to properly signal your function's termination may cause your function to either terminate early, or keep running until its timeout is reached. See the [Troubleshooting guide](https://docs.cloud.google.com/functions/docs/troubleshooting#unexpected-stops) for more information.

## Use middleware to handle HTTP requests

Node.js HTTP Cloud Run functions provide `request` and `response` objects that are compatible with [ExpressJS](https://expressjs.com/en/4x/api.html) to make consuming HTTP requests simple. Cloud Run functions automatically reads the request body, so you will always receive the body of a request independent of the media type. This means that HTTP requests should be considered to have been fully read by the time your code is executed. The nesting of ExpressJS apps should be used with this caveat—specifically, middleware that expects the body of a request to be unread might not behave as expected.

## Use ES Modules

ECMAScript modules (ES modules or ESM) are a TC39 standard, unflagged feature in Node version 14+ for loading JavaScript modules. Unlike CommonJS, ESM provides an asynchronous API for loading modules. It also provides a popular syntax improvement with `import` and `export` statements that can be used within a Cloud Run function (instead of `require` statements).

To use ESM within a Cloud Run function, you must declare `"type": "module"` within your `package.json`.
    
    
    {
      ...
      "type": "module",
      ...
    }
    

Then you can use `import` and `export` statements.

**Note:** Learn more about using [ES modules](https://github.com/GoogleCloudPlatform/functions-framework-nodejs/blob/main/docs/esm/README.md).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
