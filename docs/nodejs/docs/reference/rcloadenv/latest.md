---
url: https://docs.cloud.google.com/nodejs/docs/reference/rcloadenv/latest/
title: Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:10.533018+00:00
---

# Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/rcloadenv/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 4.0.0 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/rcloadenv/latest/)
  * [ 3.0.1 ](https://docs.cloud.google.com/nodejs/docs/reference/rcloadenv/3.0.1/)
  * [ 2.1.1 ](https://docs.cloud.google.com/nodejs/docs/reference/rcloadenv/2.1.1/)



# [Google Cloud Runtime Config: Node.js Client](https://github.com/googleapis/nodejs-rcloadenv)

[![release level](https://img.shields.io/badge/release%20level-preview-yellow.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/rcloadenv.svg)](https://www.npmjs.org/package/@google-cloud/rcloadenv)

Node.js implementation of rcloadenv. Wraps execution of a given command and loads variables from the Google Cloud Runtime Config API into that process.

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/nodejs-rcloadenv/blob/main/CHANGELOG.md).

  * [Google Cloud Runtime Config Node.js Client API Reference](https://github.com/googleapis/nodejs-rcloadenv/blob/main/README.md)
  * [Google Cloud Runtime Config Documentation](https://cloud.google.com/deployment-manager/runtime-configurator/)
  * [github.com/googleapis/nodejs-rcloadenv](https://github.com/googleapis/nodejs-rcloadenv)



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
    
    
    npm install @google-cloud/rcloadenv
    

### Using the client library
    
    
    // import the npm module
    const rcloadenv = require('[@google-cloud/rcloadenv](https://docs.cloud.google.com/nodejs/docs/reference/rcloadenv/latest/overview.html)');
    
    async function quickstart() {
      // Just load raw variables from the Runtime Config service:
      const vars = await rcloadenv.[getVariables](https://docs.cloud.google.com/nodejs/docs/reference/rcloadenv/latest/overview.html)('my-config');
      console.log(`${vars.length} variables found!`);
      vars.forEach(console.log);
    
      // Load the variables and apply them to the current environment
      await rcloadenv.[getAndApply](https://docs.cloud.google.com/nodejs/docs/reference/rcloadenv/latest/overview.html)('my-config');
      console.log(process.env.fruit);
    
      // Load the variables and mix them into a provided object
      const newEnv = Object.assign({}, process.env);
      const env = await rcloadenv.[getAndApply](https://docs.cloud.google.com/nodejs/docs/reference/rcloadenv/latest/overview.html)('my-config', newEnv);
      console.log(env.veggie);
    }
    quickstart();
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/nodejs-rcloadenv/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
Quickstart | [source code](https://github.com/googleapis/nodejs-rcloadenv/blob/main/samples/quickstart.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-rcloadenv&page=editor&open_in_editor=samples/quickstart.js,samples/README.md)  
  
The [Google Cloud Runtime Config Node.js Client API Reference](https://github.com/googleapis/nodejs-rcloadenv/blob/main/README.md) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/rcloadenv@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-rcloadenv/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/nodejs-rcloadenv/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
