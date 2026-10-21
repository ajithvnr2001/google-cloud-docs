---
url: https://docs.cloud.google.com/functions/1stgendocs/running/predeploy-test/
title: Test a Cloud Run functions before deployment \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:34.455951+00:00
---

# Test a Cloud Run functions before deployment  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/running/predeploy-test/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Test a Cloud Run functions before deployment

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide shows you how to test a Cloud Run function in Google Cloud console before deploying it. This feature is available for Node.js and Python functions.

## Prepare a function for testing

To prepare a function for testing:

  1. Open the Functions Overview page in the Google Cloud console:

[Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list)

Make sure that the project for which you enabled Cloud Run functions is selected.

  2. Click **Create Function** to create a new Node.js or Python function, or select an existing Node.js or Python function and click **Edit** to edit it.

  3. Click **Next** to advance to the code editing page:

![Screenshot that shows function predeploy testing panel](https://docs.cloud.google.com/static/functions/img/predeploy-testing-panel.png)

  4. Click **Test Function** to start the testing process.

  5. When prompted, click **Start testing** to authorize use of the Cloud Shell Terminal.




## Run the test

When you complete the preceding steps, the triggering event panel opens on the right, confirming that the function is ready to be tested. Click **Run test** :

![Screenshot that shows function predeploy testing panel](https://docs.cloud.google.com/static/functions/img/predeploy-test-fullscreen.png)

This phase of the testing process includes the following components:

  * **Triggering event panel**. The triggering event panel is pre-populated with a payload that matches the event trigger you specified on the configuration page. This is the input to your function.
  * **Cloud Shell output window**. The Cloud Shell output window displays the HTTP status code and any response returned to the caller.
  * **Run test** executes the test.



You can observe the output from the test in the Cloud Shell window:

![Screenshot that shows Cloud Shell output window](https://docs.cloud.google.com/static/functions/img/predeploy-output.png)

**Note:** It can take 1-3 minutes when initializing the testing panel for the first time. Subsequent times should only take a few seconds. If it takes longer than 3 minutes and you don't see any progress indicators, back up your source code, refresh your browser tab, and restart testing from scratch.

## Cloud Shell terminal

You can view logging output by your function in the Cloud Shell terminal at the bottom of your screen. For example, you'll see source code packaging output when you open the testing panel. When you run a test, you'll see your source code changes and execution level output, including `console.log` and errors.

If your test fails, the Cloud Shell terminal displays an error message to help you pinpoint the exact cause, for example:
    
    
    [11:31:47 AM] - Provided module can't be loaded.
    Is there a syntax error in your code?
    Detailed stack trace: /workspace/index.js:11
        : 'World';
        ^
    
    SyntaxError: Unexpected token ':'
        at Object.compileFunction (node:vm:360:18)
        at wrapSafe (node:internal/modules/cjs/loader:1048:15)
        at Module._compile (node:internal/modules/cjs/loader:1083:27)
        at Module._extensions..js (node:internal/modules/cjs/loader:1173:10)
        at Module.load (node:internal/modules/cjs/loader:997:32)
        at Module._load (node:internal/modules/cjs/loader:838:12)
        at Module.require (node:internal/modules/cjs/loader:1021:19)
        at require (node:internal/modules/cjs/helpers:103:18)
        at getUserFunction (/workspace/node_modules/@google-cloud/functions-framework/build/src/loader.js:98:30)
        at async main (/workspace/node_modules/@google-cloud/functions-framework/build/src/main.js:35:32)
    
    [11:31:47 AM] - Could not load the function, shutting down.
    

**Note:** If the server crashes, you will see a message prompting you to check your source code and re-run the test. If that does not fix the problem, back up your source code, refresh your browser tab, and restart testing from scratch.

## Deploy

Once you're finished testing, you can deploy your function in the usual way by clicking **Deploy**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
