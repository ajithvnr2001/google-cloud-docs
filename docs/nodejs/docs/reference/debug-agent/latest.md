---
url: https://docs.cloud.google.com/nodejs/docs/reference/debug-agent/latest/
title: Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:42.044513+00:00
---

# Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/debug-agent/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 7.1.1 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/debug-agent/latest/)
  * [ 7.1.0 ](https://docs.cloud.google.com/nodejs/docs/reference/debug-agent/7.1.0/)
  * [ 5.2.8 ](https://docs.cloud.google.com/nodejs/docs/reference/debug-agent/5.2.8/)



# [Cloud Debugger: Node.js Client](https://github.com/googleapis/cloud-debug-nodejs)

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/debug-agent.svg)](https://www.npmjs.org/package/@google-cloud/debug-agent)

> This module provides Cloud Debugger support for Node.js applications. Cloud Debugger is a feature of Google Cloud Platform that lets you debug your applications in production without stopping or pausing your application.

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/cloud-debug-nodejs/blob/main/CHANGELOG.md).

  * [Cloud Debugger Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/debug-agent/latest)
  * [Cloud Debugger Documentation](https://cloud.google.com/debugger)
  * [github.com/googleapis/cloud-debug-nodejs](https://github.com/googleapis/cloud-debug-nodejs)



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
  2. [Enable the Cloud Debugger API](https://console.cloud.google.com/flows/enableapi?apiid=clouddebugger.googleapis.com).
  3. [Set up authentication with a service account](https://cloud.google.com/docs/authentication/getting-started) so you can access the API from your local workstation.



### Installing the client library
    
    
    npm install @google-cloud/debug-agent
    

## Debugger Agent Settings

To customize the behaviour of the automatic debugger agent, specify options when starting the agent. The following code sample shows how to pass in a subset of the available options.
    
    
    require('[@google-cloud/debug-agent](https://docs.cloud.google.com/nodejs/docs/reference/debug-agent/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/debug-agent/latest/overview.html)({
      // .. auth settings ..
    
      // debug agent settings:
      allowExpressions: true,
      serviceContext: {
        service: 'my-service',
        version: 'version-1'
      },
      capture: { maxFrames: 20, maxProperties: 100 }
    });
    

See [the agent configuration](https://github.com/googleapis/cloud-debug-nodejs/blob/master/src/agent/config.ts) for a list of possible configuration options.

## Using the Debugger

Once your application is running, use the [Debug UI](https://console.cloud.google.com/debug) in your Cloud [developer console](https://console.cloud.google.com/) to debug your application. The Debug UI can be found in the 'Operations -> Debug' section in the navigation panel, or by simply searching for 'Debug' in the cloud console.

To take a snapshot with the debugger:

  1. Click in the gutter (line number area) or enter a filename and line number in the snapshot panel
  2. The debugger inserts a momentary breakpoint at the specified location in your code in the running instance of your application.
  3. As soon as that line of code is reached in any of the running instances of your application, the stack traces, local variables, and watch expressions are captured, and your application continues.



**Note:** The directory layout of the code that is being debugged does not have to exactly match the source code specified in the Debug UI. This is because the debug agent resolves a snapshot filename by searching for a file with the longest matching path suffix. If a unique match is found, that file will be used to set the snapshot.

## Firebase Realtime Database backend

The Cloud Debugger API is deprecated and will be turned down in May 2023.

You can use Firebase Realtime Database for data persistence as an alternative.

### Enabling the agent

To enable the agent, add the following at the top of your app's main script or entry point:
    
    
    require('[@google-cloud/debug-agent](https://docs.cloud.google.com/nodejs/docs/reference/debug-agent/latest/overview.html)').[start](https://docs.cloud.google.com/nodejs/docs/reference/debug-agent/latest/overview.html)({
      useFirebase: true,
      firebaseDbUrl: 'https://my-database-url.firebaseio.com',
      firebaseKeyPath: 'path/to/service_account.json',
    });
    

The following params are optional:

  * firebaseDbUrl - https://**PROJECT_ID** -cdbg.firebaseio.com will be used if not provided. where **PROJECT_ID** is your project ID.
  * firebaseKeyPath - Default google application credentials are used if not provided.



### Using the Debugger

Using the Debugger with the Firebase Realtime Database backend requires using the Snapshot Debugger CLI.

See the [full Snapshot Debugger CLI documentation](https://github.com/GoogleCloudPlatform/snapshot-debugger#readme).

## Limitations and Requirements

> Note: There is a known issue where enabling the agent may trigger memory leaks. See [#811](https://github.com/googleapis/cloud-debug-nodejs/issues/811)

  * Privacy issues can be created by setting snapshot conditions that watch expressions evaluated in the context of your application. You may be able to view sensitive user data when viewing the values of variables.
  * The debug agent tries to ensure that all conditions and watchpoints you add are read-only and have no side effects. It catches, and disallows, all expressions that may have static side effects to prevent accidental state change. However, it presently does not catch expressions that have dynamic side-effects. For example, `o.f` looks like a property access, but dynamically, it may end up calling a getter function. We presently do NOT detect such dynamic-side effects.
  * The root directory of your application needs to contain a `package.json` file.



## Samples

Samples are in the [`samples/`](https://github.com/googleapis/cloud-debug-nodejs/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
App | [source code](https://github.com/googleapis/cloud-debug-nodejs/blob/main/samples/app.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/cloud-debug-nodejs&page=editor&open_in_editor=samples/app.js,samples/README.md)  
Snippets | [source code](https://github.com/googleapis/cloud-debug-nodejs/blob/main/samples/snippets.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/cloud-debug-nodejs&page=editor&open_in_editor=samples/snippets.js,samples/README.md)  
  
The [Cloud Debugger Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/debug-agent/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://nodejs.org/en/about/releases/). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/debug-agent@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/cloud-debug-nodejs/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/cloud-debug-nodejs/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
