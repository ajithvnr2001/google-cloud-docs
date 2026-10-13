---
url: https://docs.cloud.google.com/nodejs/docs/reference/google-proto-files/latest/
title: Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:10.842381+00:00
---

# Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/google-proto-files/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.2 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/google-proto-files/latest/)
  * [ 3.0.1 ](https://docs.cloud.google.com/nodejs/docs/reference/google-proto-files/3.0.1/)
  * [ 2.5.0 ](https://docs.cloud.google.com/nodejs/docs/reference/google-proto-files/2.5.0/)
  * [ 2.4.1 ](https://docs.cloud.google.com/nodejs/docs/reference/google-proto-files/2.4.1/)



# [Google APIs Proto Files: Node.js Client](https://github.com/googleapis/nodejs-proto-files)

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/google-proto-files.svg)](https://www.npmjs.org/package/google-proto-files)

All of the Google API's protocol buffer files

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/nodejs-proto-files/blob/main/CHANGELOG.md).

  * [Google APIs Proto Files Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/google-proto-files/latest)

  * [github.com/googleapis/nodejs-proto-files](https://github.com/googleapis/nodejs-proto-files)




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
    
    
    npm install google-proto-files
    

### Using the client library
    
    
    const protos = require('[google-proto-files](https://docs.cloud.google.com/nodejs/docs/reference/google-proto-files/latest/overview.html)');
    
    async function quickstart() {
      // Get a directory path by executing as a function
      const files = protos.[getProtoPath](https://docs.cloud.google.com/nodejs/docs/reference/google-proto-files/latest/overview.html)('[logging](https://docs.cloud.google.com/nodejs/docs/reference/google-proto-files/latest/overview.html)', 'v2');
      console.log(files);
      // node_modules/google-proto-files/google/logging/v2
    
      // Get a path to the entry proto file for a specific API version
      console.log(protos.[pubsub](https://docs.cloud.google.com/nodejs/docs/reference/google-proto-files/latest/overview.html).v1);
      // node_modules/google-proto-files/google/pubsub/v1/pubsub.proto
    
      // Load a proto which depends on google common protos.
      const root1 = await protos.[load](https://docs.cloud.google.com/nodejs/docs/reference/google-proto-files/latest/overview.html)('./cloudcats.proto');
      const service1 = root1.lookup('example.MyService');
      console.log(service1);
    
      // Load protos synchronously
      const root2 = protos.[loadSync](https://docs.cloud.google.com/nodejs/docs/reference/google-proto-files/latest/overview.html)('./cloudcats.proto');
      const service2 = root2.lookup('example.MyService');
      console.log(service2);
    }
    quickstart();
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/nodejs-proto-files/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
Quickstart | [source code](https://github.com/googleapis/nodejs-proto-files/blob/main/samples/quickstart.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-proto-files&page=editor&open_in_editor=samples/quickstart.js,samples/README.md)  
  
The [Google APIs Proto Files Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/google-proto-files/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://nodejs.org/en/about/releases/). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install google-proto-files@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-proto-files/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/nodejs-proto-files/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
