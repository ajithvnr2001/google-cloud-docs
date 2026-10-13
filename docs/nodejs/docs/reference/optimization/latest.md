---
url: https://docs.cloud.google.com/nodejs/docs/reference/optimization/latest/
title: Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:20.218056+00:00
---

# Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/optimization/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.2.0 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/optimization/latest/)
  * [ 2.2.2 ](https://docs.cloud.google.com/nodejs/docs/reference/optimization/2.2.2/)
  * [ 2.1.1 ](https://docs.cloud.google.com/nodejs/docs/reference/optimization/2.1.1/)



# [Cloud Optimization AI: Node.js Client](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-optimization)

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/optimization.svg)](https://www.npmjs.org/package/@google-cloud/optimization)

optimization client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-optimization/CHANGELOG.md).

  * [Cloud Optimization AI Node.js Client API Reference](https://googleapis.dev/nodejs/cloudoptimization/latest/)
  * [Cloud Optimization AI Documentation](https://cloud.google.com/optimization/)
  * [github.com/googleapis/google-cloud-node/packages/google-cloud-optimization](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-optimization)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart

    * Before you begin
    * Installing the client library
  * Samples

  * Versioning
  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable billing for your project](https://support.google.com/cloud/answer/6293499#enable-billing).
  3. [Enable the Cloud Optimization AI API](https://console.cloud.google.com/flows/enableapi?apiid=cloudoptimization.googleapis.com).
  4. [Set up authentication with a service account](https://cloud.google.com/docs/authentication/getting-started) so you can access the API from your local workstation.



### Installing the client library
    
    
    npm install @google-cloud/optimization
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-optimization/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
Fleet_routing.batch_optimize_tours | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-optimization/samples/generated/v1/fleet_routing.batch_optimize_tours.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-optimization/samples/generated/v1/fleet_routing.batch_optimize_tours.js,packages/google-cloud-optimization/samples/README.md)  
Fleet_routing.optimize_tours | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-optimization/samples/generated/v1/fleet_routing.optimize_tours.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-optimization/samples/generated/v1/fleet_routing.optimize_tours.js,packages/google-cloud-optimization/samples/README.md)  
Quickstart | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-optimization/samples/quickstart.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-optimization/samples/quickstart.js,packages/google-cloud-optimization/samples/README.md)  
  
The [Cloud Optimization AI Node.js Client API Reference](https://googleapis.dev/nodejs/cloudoptimization/latest/) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/optimization@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/google-cloud-node/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/google-cloud-node/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
