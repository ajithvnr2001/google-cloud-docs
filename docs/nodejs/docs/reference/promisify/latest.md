---
url: https://docs.cloud.google.com/nodejs/docs/reference/promisify/latest/
title: Google Cloud Common Promisify: Node.js Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:10.389971+00:00
---

# Google Cloud Common Promisify: Node.js Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/promisify/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Google Cloud Common Promisify: Node.js Client Stay organized with collections  Save and categorize content based on your preferences. 

5.1.0 (latest)  5.0.0  4.0.0  3.0.1  2.0.4 

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/promisify.svg)](https://www.npmjs.org/package/@google-cloud/promisify)

A simple utility for promisifying functions and classes.

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/nodejs-promisify/blob/main/CHANGELOG.md).

  * [Google Cloud Common Promisify Node.js Client API Reference](https://googleapis.dev/nodejs/promisify/latest)

  * [github.com/googleapis/nodejs-promisify](https://github.com/googleapis/nodejs-promisify)




Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart

    * Installing the client library
    * Using the client library
  * Samples
  * Versioning
  * Contributing
  * License



## Quickstart

### Installing the client library
    
    
    npm install @google-cloud/promisify
    

### Using the client library
    
    
    const {promisify} = require('[@google-cloud/promisify](https://docs.cloud.google.com/nodejs/docs/reference/promisify/latest/overview.html)');
    
    /**
     * This is a very basic example function that accepts a callback.
     */
    function someCallbackFunction(name, callback) {
      if (!name) {
        callback(new Error('Name is required!'));
      } else {
        callback(null, `Well hello there, ${name}!`);
      }
    }
    
    // let's promisify it!
    const somePromiseFunction = promisify(someCallbackFunction);
    
    async function quickstart() {
      // now we can just `await` the function to use it like a promisified method
      const [result] = await somePromiseFunction('nodestronaut');
      console.log(result);
    }
    quickstart();
    

It's unlikely you will need to install this package directly, as it will be installed as a dependency when you install other `@google-cloud` packages.

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/nodejs-promisify/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
Quickstart | [source code](https://github.com/googleapis/nodejs-promisify/blob/main/samples/quickstart.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-promisify&page=editor&open_in_editor=samples/quickstart.js,samples/README.md)  
  
The [Google Cloud Common Promisify Node.js Client API Reference](https://googleapis.dev/nodejs/promisify/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/promisify@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-promisify/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/nodejs-promisify/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
