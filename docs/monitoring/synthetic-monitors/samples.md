---
url: https://docs.cloud.google.com/monitoring/synthetic-monitors/samples/
title: Samples for synthetic monitors \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:26.804829+00:00
---

# Samples for synthetic monitors  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/synthetic-monitors/samples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Samples for synthetic monitors Stay organized with collections  Save and categorize content based on your preferences. 

Preconfigured templates and sample code let you build synthetic monitors in Node.js and TypeScript using frameworks such as Puppeteer, Selenium WebDriver, and Mocha. You can use these samples—available in the [`synthetics-sdk-nodejs`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs) GitHub repository—to query URLs, run browser-based user journeys, test API endpoints, or check for broken links.

## Guidelines for using samples and writing custom tests

Before you deploy a sample or write a custom test, review the following requirements:

  * **Update the target URL** : Before you deploy any sample code, update the `url` field to point to your target endpoint. Don't set this field to `https://www.google.com`.
  * **Throw an`Error` on test failure**: If you write custom tests instead of using a template, ensure that your test passes unless an [`Error`](https://nodejs.org/api/errors.html) is thrown. We recommend that you use the [`Assert`](https://nodejs.org/api/assert.html) library so that any failures are attributed to the correct line of code.



## Generic templates

The generic templates are configured to collect trace and log data for outbound HTTP requests. The solution leverages the OpenTelemetry [auto-instrumentation-node](https://www.npmjs.com/package/@opentelemetry/auto-instrumentations-node) module and the [winston logger](https://www.npmjs.com/package/winston). Due to the dependency on open source products, you should expect changes in the structure of trace and log data. Therefore, the collected trace and log data should be used only for debugging purposes.

**Note:** To enable collection of logs and traces, your code must import the `instantiateAutoInstrumentation` package and invoke the `instantiateAutoInstrumentation()` method before it performs any other actions. Also, ensure that your code specifies the `logger` as an asynchronous callback handler.

You can implement your own approach to collect trace and log data for outbound HTTP requests. For an example of a custom approach, see the class [`SyntheticAutoInstrumentation`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/blob/main/packages/synthetics-sdk-api/src/auto_instrumentation.ts#L82).

### Generic Node.js sample

The [`generic-synthetic-nodejs`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/generic-synthetic-nodejs) sample illustrates how to query a URL. This sample contains the same code as the default function displayed by the Google Cloud console. To view the full sample, in the sample's toolbar, select the GitHub logo.
    
    
    const { instantiateAutoInstrumentation, runSyntheticHandler } = require('@google-cloud/synthetics-sdk-api');
    // Run instantiateAutoInstrumentation before any other code runs, to get automatic logs and traces
    instantiateAutoInstrumentation();
    const functions = require('@google-cloud/functions-framework');
    const axios = require('axios');
    const assert = require('node:assert');
    
    functions.http('SyntheticFunction', runSyntheticHandler(async ({logger, executionId}) => {
      /*
       * This function executes the synthetic code for testing purposes.
       * If the code runs without errors, the synthetic test is considered successful.
       * If an error is thrown during execution, the synthetic test is considered failed.
       */
      logger.info('Making an http request using synthetics, with execution id: ' + executionId);
      const url = 'https://www.google.com/'; // URL to send the request to
      return await assert.doesNotReject(axios.get(url));
    }));
    

### TypeScript sample

The [`generic-synthetic-typescript`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/generic-synthetic-typescript) sample illustrates how to query a URL. To view the full sample, in the sample's toolbar, select the GitHub logo.
    
    
    import {runSyntheticHandler, instantiateAutoInstrumentation} from '@google-cloud/synthetics-sdk-api'
    // Run instantiateAutoInstrumentation before any other code runs, to get automatic logs and traces
    instantiateAutoInstrumentation();
    import * as ff from '@google-cloud/functions-framework';
    import axios from 'axios';
    import assert from 'node:assert';
    import {Logger} from 'winston';
    
    ff.http('SyntheticFunction', runSyntheticHandler(async ({logger, executionId}: {logger: Logger, executionId: string|undefined}) => {
      /*
       * This function executes the synthetic code for testing purposes.
       * If the code runs without errors, the synthetic test is considered successful.
       * If an error is thrown during execution, the synthetic test is considered failed.
       */
      logger.info('Making an http request using synthetics, with execution id: ' + executionId);
      const url = 'https://www.google.com/'; // URL to send the request to
      return await assert.doesNotReject(axios.get(url));
    }));
    

### Puppeteer template

If you use [Puppeteer](https://pptr.dev/), then consider starting with the [`generic-puppeteer-nodejs`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/generic-puppeteer-nodejs) sample.

**Note:** The default settings for the allocated memory, CPU, and security might not be sufficient. We recommend that the memory be set to at least 1 GiB.

#### Required Puppeteer setup

To use Puppeteer, ensure that you complete the following steps:

  1. Include `.puppeteerrc.cjs` in the source directory of your Cloud Run function:
         
         const { join } = require('path');
         
         /**
          * @type {import("puppeteer").Configuration}
          */
         module.exports = {
           cacheDirectory: join(__dirname, '.cache', 'puppeteer'),
         };

  2. Add the following script to the `package.json` file of your Cloud Run function:
         
         "scripts": {
              "gcp-build": "node node_modules/puppeteer/install.mjs"
         },
         




#### Puppeteer sample

The [`generic-puppeteer-nodejs`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/generic-puppeteer-nodejs) sample illustrates how to use Puppeteer with your Cloud Run function. To view the full sample, in the sample's toolbar, select the GitHub logo.
    
    
    const { instantiateAutoInstrumentation, runSyntheticHandler } = require('@google-cloud/synthetics-sdk-api');
    // Run instantiateAutoInstrumentation before any other code runs, to get automatic logs and traces
    instantiateAutoInstrumentation();
    const functions = require('@google-cloud/functions-framework');
    const axios = require('axios');
    const assert = require('node:assert');
    const puppeteer = require('puppeteer');
    
    
    functions.http('CustomPuppeteerSynthetic', runSyntheticHandler(async ({logger, executionId}) => {
     /*
      * This function executes the synthetic code for testing purposes.
      * If the code runs without errors, the synthetic test is considered successful.
      * If an error is thrown during execution, the synthetic test is considered failed.
      */
    
     // Launch a headless Chrome browser and open a new page
     const browser = await puppeteer.launch({ headless: 'new', timeout: 0});
     const page = await browser.newPage();
    
     // Navigate to the target URL
     const result = await page.goto('https://www.example.com', {waitUntil: 'load'});
    
     // Confirm successful navigation
     await assert.equal(result.status(), 200);
    
     // Print the page title to the console
     const title = await page.title();
     logger.info(`My Page title: ${title} ` + executionId);
    
     // Close the browser
     await browser.close();
    }));
    

### Selenium WebDriver template

If you use [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/), then consider starting with the [`generic-selenium-nodejs`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/generic-selenium-nodejs) sample. The sample, which is available on GitHub, includes `index.js` and `package.json` files.

**Note:** The default settings for the allocated memory, CPU, and security might not be sufficient. We recommend that the memory be set to at least 1 GiB.

To view the full sample, in the sample's toolbar, select the GitHub logo.
    
    
    const {
      instantiateAutoInstrumentation,
      runSyntheticHandler,
    } = require('@google-cloud/synthetics-sdk-api');
    // Run instantiateAutoInstrumentation before any other code runs, to get automatic logs and traces
    instantiateAutoInstrumentation();
    const functions = require('@google-cloud/functions-framework');
    const assert = require('node:assert');
    
    const { Builder, Browser, By } = require('selenium-webdriver');
    const chrome = require('selenium-webdriver/chrome');
    
    /*
     * This function executes the synthetic code for testing purposes.
     * If the code runs without errors, the synthetic test is considered successful.
     * If an error is thrown during execution, the synthetic test is considered failed.
     */
    functions.http(
      'CustomSeleniumSynthetic',
      runSyntheticHandler(async ({ logger, executionId }) => {
        /*
         * Construct chrome options
         * Note: `setChromeBinaryPath` must be set to '/srv/bin/chromium' when running in
         *   GCF (but will need to be changed if running on local machine).
         */
        const options = new chrome.Options();
        options.setChromeBinaryPath('/srv/bin/chromium');
        options.addArguments('--headless', '--disable-gpu', '--no-sandbox');
    
        // Launch headless chrome webdriver with options
        const driver = await new Builder()
          .forBrowser(Browser.CHROME)
          .setChromeOptions(options)
          .build();
    
        // Navigate to the target URL
        await driver.get('https://example.com');
    
        // Retrieve title and `a` tag of page
        const title = await driver.getTitle();
        const aTag = await driver.findElement(By.css('a')).getText();
    
        // assert title is as expected and print to console
        await assert.equal(title, 'Example Domain');
        logger.info(`My URL title is: ${title} ` + executionId);
    
        await driver.quit();
      })
    );
    

## Mocha template

If you write tests that rely on the [Mocha](https://mochajs.org/) template, then consider whether a sequence of tests should continue or stop when a failure occurs. To stop a sequence of tests after a failure, you must set the [`bail`](https://mochajs.org/#command-line-usage) flag.

For an end-to-end example that includes deploying an API, writing a sample Mocha test suite for the API endpoints, and configuring the synthetic monitor, see the blog [Google Cloud Synthetic Monitoring Tutorial](https://medium.com/google-cloud/google-cloud-synthetic-monitoring-tutorial-ce502f81bb24).

The [`mocha-url-ok`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/mocha-url-ok) sample illustrates how a Cloud Run function can invoke a [Mocha](https://mochajs.org/) test suite, and it provides a sample test suite. To view the full sample, in the sample's toolbar, select the GitHub logo.
    
    
    const functions = require('@google-cloud/functions-framework');
    const GcmSynthetics = require('@google-cloud/synthetics-sdk-mocha');
    
    /*
     * This is the server template that is required to run a synthetic monitor in
     * Google Cloud Functions.
     */
    
    functions.http('SyntheticMochaSuite', GcmSynthetics.runMochaHandler({
      spec: `${__dirname}/mocha_tests.spec.js`
    }));
    
    
    
    /*
     * This is the file may be interacted with to author mocha tests. To interact
     * with other GCP products or services, users should add dependencies to the
     * package.json file, and require those dependencies here A few examples:
     *  - @google-cloud/secret-manager:
     *        https://www.npmjs.com/package/@google-cloud/secret-manager
     *  - @google-cloud/spanner: https://www.npmjs.com/package/@google-cloud/spanner
     *  - Supertest: https://www.npmjs.com/package/supertest
     */
    
    const {expect} = require('chai');
    const fetch = require('node-fetch');
    
    it('pings my website', async () => {
      const url = 'https://google.com/'; // URL to send the request to
      const externalRes = await fetch(url);
      expect(externalRes.ok).to.be.true;
    });
    

## Broken-link template

The [`broken-links-ok`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/broken-links-ok) sample illustrates how to configure a broken-link checker. For this template, you only specify the values of the `options` object. This object specifies the URI to be tested and the parameters of the test.

If you use Puppeteer, then ensure that you complete the Required Puppeteer setup steps.

**Note:** The default settings for the allocated memory, CPU, and security might not be sufficient. We recommend that the memory be set to at least 1 GiB.

To view the full sample, in the sample's toolbar, select the GitHub logo.
    
    
    const functions = require('@google-cloud/functions-framework');
    const GcmSynthetics = require('@google-cloud/synthetics-sdk-broken-links');
    
    const options = {
      origin_uri: "https://example.com",
      // link_limit: 10,
      // query_selector_all: "a", // https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll
      // get_attributes: ['href'], // https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttribute
      // link_order: "FIRST_N", // "FIRST_N" or "RANDOM"
      // link_timeout_millis: 30000, // timeout per link
      // max_retries: 0, // number of retries per link if it failed for any reason
      // wait_for_selector: '', // https://pptr.dev/api/puppeteer.page.waitforselector
      // per_link_options: {},
        /*
        // example:
          per_link_options: {
            'http://fake-link1': { expected_status_code: "STATUS_CLASS_4XX" },
            'http://fake-link2': { expected_status_code: 304 },
            'http://fake-link3': { link_timeout_millis: 10000 },
            'http://fake-link4': {
              expected_status_code: "STATUS_CLASS_3XX",
              link_timeout_millis: 10,
            },
          },
        */
      // total_synthetic_timeout_millis: 60000 // Timeout set for the entire Synthetic Monitor
      // screenshot_options: { capture_condition: 'FAILING', storage_location: '' }
    };
    
    functions.http('BrokenLinkChecker', GcmSynthetics.runBrokenLinksHandler(options));
    

## What's next

  * [Create a synthetic monitor](https://docs.cloud.google.com/monitoring/synthetic-monitors/create)
  * [Create a broken-link checker](https://docs.cloud.google.com/monitoring/synthetic-monitors/broken-links)
  * [Manage synthetic monitors](https://docs.cloud.google.com/monitoring/synthetic-monitors/manage)
  * [Explore synthetic monitor results](https://docs.cloud.google.com/monitoring/synthetic-monitors/explore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
