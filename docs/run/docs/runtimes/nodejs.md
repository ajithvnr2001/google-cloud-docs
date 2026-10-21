---
url: https://docs.cloud.google.com/run/docs/runtimes/nodejs/
title: The Node.js runtime \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:54.660447+00:00
---

# The Node.js runtime  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/runtimes/nodejs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  The Node.js runtime Stay organized with collections  Save and categorize content based on your preferences. 

Your Cloud Run function runs in an environment consisting of an operating system version with add-on packages, language support, and the [Node.js Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-nodejs) library that supports and invokes your function. This environment is identified by the language version, and is known as the runtime ID.

## Function preparation

You can prepare a function directly from the Google Cloud console or write it on your local machine and upload it. To prepare your local machine for Node.js development, see [Set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup).

## Supported Node.js runtimes and base images

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
Node.js 26   
(Preview) | nodejs26 | 
* google-24 (default)
* google-24-full
| 
* [google-24/nodejs26](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/nodejs26)
* [google-24-full/nodejs26](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/nodejs26)
|  |   
Node.js 24 | nodejs24 | 
* google-24 (default)
* google-24-full
| 
* [google-24/nodejs24](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/nodejs24)
* [google-24-full/nodejs24](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/nodejs24)
| 2028-04-30 | 2028-10-31  
Node.js 22 | nodejs22 | 
* google-22 (default)
* google-22-full
| 
* [google-22/nodejs22](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/nodejs22)
* [google-22-full/nodejs22](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/nodejs22)
| 2027-04-30 | 2027-10-31  
Node.js 20 | nodejs20 | 
* google-22 (default)
* google-22-full
| 
* [google-22/nodejs20](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/nodejs20)
* [google-22-full/nodejs20](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/nodejs20)
| 2026-04-30 | 2026-10-30  
Node.js 18 | nodejs18 | 
* google-22 (default)
* google-22-full
| 
* [google-22/nodejs18](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/nodejs18)
* [google-22-full/nodejs18](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/nodejs18)
| 2025-04-30 | 2025-10-30  
Node.js 16 | nodejs16 |  google-18-full  |  [google-18-full/nodejs16](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs16) | 2024-01-30 | 2025-01-30  
Node.js 14 | nodejs14 |  google-18-full  |  [google-18-full/nodejs14](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs14) | 2024-01-30 | 2025-01-30  
Node.js 12 | nodejs12 |  google-18-full  |  [google-18-full/nodejs12](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs14) | 2024-01-30 | 2025-01-30  
Node.js 10 | nodejs10 |  google-18-full  |  [google-18-full/nodejs10](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs10) | 2024-01-30 | 2025-01-30  
Node.js 8 | nodejs8 |  Decommissioned  |  Decommissioned  | 2020-06-05 | Feb 2021  
Node.js 6 | nodejs6 |  Decommissioned  |  Decommissioned  | 2019-04-17 | Aug 2020  
  
## Select your runtime

You can select one of the supported Node.js runtimes for your function during deployment. 

You can select a runtime version using the Google Cloud console, or the gcloud CLI. Click the tab for instructions on using the tool of your choice:

###  gcloud 

Specify the [Node.js base image](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images) for your function using the `--base-image` flag, while deploying your function. For example:
    
    
    gcloud run deploy FUNCTION \
        --source . \
        --function FUNCTION_ENTRYPOINT \
        --base-image nodejs24
    

Replace:

  * FUNCTION with the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

  * FUNCTION_ENTRYPOINT with the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.




For detailed instructions on deploying a function using the gcloud CLI, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#gcloud).

###  Console 

You can select a runtime version when you create or update a Cloud Run function in the Google Cloud console. For detailed instructions on deploying a function, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#deploy-functions).

To select a runtime in the Google Cloud console when you create a function, follow these steps:

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Write a function**.

  3. In the **Runtime** list, select a Node.js runtime version.

  4. Click **Create** , and wait for Cloud Run to create the service using a placeholder revision.

  5. The console will redirect you to the **Source** tab where you can see the source code of your function. Click **Save and redeploy**.




For detailed instructions on updating the runtime version after your function is deployed, see [Re-deploy new source code](https://docs.cloud.google.com/run/docs/deploy-functions#update-code-functions).

## Source code structure

For Cloud Run functions to find your function's definition, your source code must follow a specific structure. See [Write Cloud Run functions](https://docs.cloud.google.com/static/run/docs/write-functions#node.js) for more information.

## Specify dependencies

You can specify dependencies for your functions by listing them in a `package.json` file. For more information, see [Specify dependencies in Node.js](https://docs.cloud.google.com/run/docs/runtimes/nodejs-dependencies).

## NPM build script

By default, the Node.js runtime executes `npm run build` if a `build` script is detected in `package.json`. If you require additional control over your build steps before starting your application, you can provide a [custom build step](https://docs.cloud.google.com/run/docs/building/functions) by adding a `gcp-build` script to your `package.json` file.

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

**Warning:** failure to properly signal your function's termination may cause your function to either terminate early, or keep running until its timeout is reached.

## Use middleware to handle HTTP requests

Node.js HTTP functions provide `request` and `response` objects that are compatible with [ExpressJS](https://expressjs.com/en/4x/api.html) to make consuming HTTP requests simpler. Cloud Run functions automatically reads the request body, so you will always receive the body of a request independent of the media type. This means that HTTP requests should be considered to have been fully read by the time your code is executed. The nesting of ExpressJS apps should be used with this caveat—specifically, middleware that expects the body of a request to be unread might not behave as expected.

## Use ES Modules

ECMAScript modules (ES modules or ESM) are a TC39 standard, unflagged feature in Node version 14+ for loading JavaScript modules. Unlike CommonJS, ESM provides an asynchronous API for loading modules. It also provides a popular syntax improvement with `import` and `export` statements that can be used within a Cloud Run function (instead of `require` statements).

To use ESM within a Cloud Run function, you must declare `"type": "module"` within your `package.json`.
    
    
    {
      ...
      "type": "module",
      ...
    }
    

Then you can use `import` and `export` statements.

Learn more about using [ES modules](https://github.com/GoogleCloudPlatform/functions-framework-nodejs/tree/main/docs/esm).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
