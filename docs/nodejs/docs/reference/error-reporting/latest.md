---
url: https://docs.cloud.google.com/nodejs/docs/reference/error-reporting/latest/
title: Error Reporting: Node.js Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:44.217707+00:00
---

# Error Reporting: Node.js Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/error-reporting/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Error Reporting: Node.js Client Stay organized with collections  Save and categorize content based on your preferences. 

3.0.6 (latest)  3.0.4  2.0.4 

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/error-reporting.svg)](https://www.npmjs.org/package/@google-cloud/error-reporting)

> Node.js idiomatic client for [Error Reporting](https://cloud.google.com/error-reporting).

[Error Reporting](https://cloud.google.com/error-reporting/docs/) aggregates and displays errors produced in your running cloud services.

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/nodejs-error-reporting/blob/main/CHANGELOG.md).

  * [Error Reporting Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/error-reporting/latest)
  * [Error Reporting Documentation](https://cloud.google.com/error-reporting)
  * [github.com/googleapis/nodejs-error-reporting](https://github.com/googleapis/nodejs-error-reporting)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart

    * Before you begin
    * Installing the client library
  * Versioning

  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable the Error Reporting API](https://console.cloud.google.com/flows/enableapi?apiid=clouderrorreporting.googleapis.com).
  3. [Set up authentication with a service account](https://cloud.google.com/docs/authentication/getting-started) so you can access the API from your local workstation.



### Installing the client library
    
    
    npm install @google-cloud/error-reporting
    

This module provides custom Error Reporting support for Node.js applications. [Error Reporting](https://cloud.google.com/error-reporting/) is a feature of Google Cloud Platform that allows in-depth monitoring and viewing of errors reported by applications running in almost any environment.

However, note that [@google-cloud/logging-winston](https://github.com/googleapis/nodejs-logging-winston) and [@google-cloud/logging-bunyan](https://github.com/googleapis/nodejs-logging-bunyan) automatically integrate with the Error Reporting service for Error objects logged at severity `error` or higher, for applications running on Google Cloud Platform.

Thus, if you are already using Winston or Bunyan in your application, and don't need custom error reporting capabilities, you do not need to use the `@google-cloud/error-reporting` library directly to report errors to the Error Reporting Console.

![Error Reporting overview](https://raw.githubusercontent.com/googleapis/nodejs-error-reporting/master/doc/images/errors-overview.png)

# When Errors Are Reported

The `reportMode` configuration option is used to specify when errors are reported to the Error Reporting Console. It can have one of three values:

  * `'production'` (default): Only report errors if the NODE_ENV environment variable is set to "production".
  * `'always'`: Always report errors regardless of the value of NODE_ENV.
  * `'never'`: Never report errors regardless of the value of NODE_ENV.



The `reportMode` configuration option replaces the deprecated `ignoreEnvironmentCheck` configuration option. If both the `reportMode` and `ignoreEnvironmentCheck` options are specified, the `reportMode` configuration option takes precedence.

The `ignoreEnvironmentCheck` option should not be used. However, if it is used, and the `reportMode` option is not specified, it can have the values:

  * `false` (default): Only report errors if the NODE_ENV environment variable is set to "production".
  * `true`: Always report errors regardless of the value of NODE_ENV.



## Setup, Configuration, and Examples

See the documentation for setup instructions, configuration options, and examples: <https://cloud.google.com/error-reporting/docs/setup/nodejs>

Additional code samples can also be found here: <https://github.com/GoogleCloudPlatform/nodejs-docs-samples/tree/main/error-reporting>

The [Error Reporting Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/error-reporting/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/error-reporting@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-error-reporting/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/nodejs-error-reporting/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-07 UTC."],[],[]] 
