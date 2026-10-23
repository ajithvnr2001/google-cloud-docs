---
url: https://docs.cloud.google.com/run/docs/tips/nodejs/
title: Optimize Node.js applications for Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:13.347784+00:00
---

# Optimize Node.js applications for Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tips/nodejs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Optimize Node.js applications for Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes optimizations for Cloud Run services written in JavaScript or TypeScript, running on the Node.js runtime. The information on this page supplements the [general development tips](https://docs.cloud.google.com/run/docs/tips/general), which also apply to Node.js.

## Optimize startup time

By optimizing startup time, you can reduce latency, improve responsiveness, and achieve effective cost optimization. This section describes different ways to optimize startup time.

### Start your app using `node` instead of `npm`

Start your application directly using `node index.js` instead of `npm start`, as `npm` adds extra latency.

To start your application with `node index.js`, follow either of these methods:

  * Use `CMD node index.js` in your Dockerfile, for example:
        
        CMD node index.js
        

  * Set `node index.js` as your entrypoint. Run the following command using the Google Cloud CLI:
        
        gcloud run deploy SERVICE --command "node index.js"
        

For more information and options for configuring entrypoints, see [Configure containers for services](https://docs.cloud.google.com/run/docs/configuring/services/containers#configure-entrypoint-services).




If you use source deployments without a Dockerfile, Cloud Run performs the optimization.

### Bundle your code

A bundler is a build tool that optimizes the layout of your JavaScript source files for faster load times. Some common bundler optimizations include tree shaking, minification, and coalescing of small files. Bundlers significantly reduce the total size of the bundle and reduce the number of file read requests. Common JavaScript bundlers are [esbuild](https://esbuild.github.io/), [webpack](https://webpack.js.org/), and [rollup](https://rollupjs.org/).

### Lazy load dependencies

At startup, Cloud Run streams each file that your code loads from a remote location. Compared to a local file system, using a remote location leads to additional latency each time a file is read. Node.js packages might use many files with indirect dependencies. Instead of importing all dependencies at startup, we recommended that you only load dependencies that are required for your server to start, and lazy load the other dependencies with [dynamic imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import).

For example, instead of using import at the top of your module, such as `import { Storage } from '@google-cloud/storage'`, use `import()` in the function when it requires the imported object, for example:
    
    
    const { Storage } = await import('@google-cloud/storage');
    

To identify modules that load during startup and the time taken by each module to load on your machine, run the following command:
    
    
    node --trace-event-categories node.module_timer --trace-event-file-pattern 'trace-events.log' index.js
    

### Configure timeout

In Node.js version 14 and later, the built-in HTTP server has a [default timeout](https://nodejs.org/api/http.html#serversettimeoutmsecs-callback) of 0 (no timeout). In Node.js versions earlier than 14, the default timeout was 2 minutes. If the request timeout of your Cloud Run service is longer, modify the timeout using `server.setTimeout(msecs)`. You must also modify the timeout for frameworks that are built on the Node.js server, such as [Express](https://expressjs.com/). To achieve an unlimited timeout in Node.js and to rely on Cloud Run's built-in timeout, use `server.setTimeout(0)`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
