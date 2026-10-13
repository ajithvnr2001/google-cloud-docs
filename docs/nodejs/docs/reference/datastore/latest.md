---
url: https://docs.cloud.google.com/nodejs/docs/reference/datastore/latest/
title: Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:41.210993+00:00
---

# Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datastore/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 9.1.0 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/latest/)
  * [ 8.7.0 ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/8.7.0/)
  * [ 8.6.0 ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/8.6.0/)
  * [ 8.5.0 ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/8.5.0/)
  * [ 8.4.0 ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/8.4.0/)
  * [ 8.3.0 ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/8.3.0/)
  * [ 8.2.2 ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/8.2.2/)
  * [ 8.1.0 ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/8.1.0/)
  * [ 8.0.0 ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/8.0.0/)
  * [ 6.6.2 ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/6.6.2/)
  * [ 6.5.0 ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/6.5.0/)
  * [ 6.4.8 ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/6.4.8/)
  * [ 6.3.1 ](https://docs.cloud.google.com/nodejs/docs/reference/datastore/6.3.1/)



# [Google Cloud Datastore: Node.js Client](https://github.com/googleapis/nodejs-datastore)

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/datastore.svg)](https://www.npmjs.org/package/@google-cloud/datastore)

Cloud Datastore Client Library for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/nodejs-datastore/blob/main/CHANGELOG.md).

  * [Google Cloud Datastore Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/datastore/latest)
  * [Google Cloud Datastore Documentation](https://cloud.google.com/datastore/docs)
  * [github.com/googleapis/nodejs-datastore](https://github.com/googleapis/nodejs-datastore)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart
    * Before you begin
    * Installing the client library
    * Using the client library
  * Samples
  * Versioning
  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable the Google Cloud Datastore API](https://console.cloud.google.com/flows/enableapi?apiid=datastore.googleapis.com).
  3. [Set up authentication with a service account](https://cloud.google.com/docs/authentication/getting-started) so you can access the API from your local workstation.



### Installing the client library
    
    
    npm install @google-cloud/datastore
    

### Using the client library
    
    
    // Imports the Google Cloud client library
    const {Datastore} = require('[@google-cloud/datastore](https://docs.cloud.google.com/nodejs/docs/reference/datastore/latest/overview.html)');
    
    // Creates a client
    const datastore = new [Datastore](https://docs.cloud.google.com/nodejs/docs/reference/datastore/latest/datastore/datastore.html)();
    
    async function quickstart() {
      // The kind for the new entity
      const kind = 'Task';
    
      // The name/ID for the new entity
      const name = 'sampletask1';
    
      // The Cloud Datastore key for the new entity
      const taskKey = datastore.key([kind, name]);
    
      // Prepares the new entity
      const task = {
        key: taskKey,
        data: {
          description: 'Buy milk',
        },
      };
    
      // Saves the entity
      await datastore.save(task);
      console.log(`Saved ${task.key.name}: ${task.data.description}`);
    }
    quickstart();
    

### Troubleshooting

#### Emulator returning `DEADLINE_EXCEEDED`, `java.lang.OutOfMemoryError`

_Reference Issue:[#95](https://github.com/googleapis/nodejs-datastore/issues/95)_

When using the emulator, you may experience errors such as "DEADLINE_EXCEEDED" within your application, corresponding to an error in the emulator: "java.lang.OutOfMemoryError". These errors are unique to the emulator environment and will not persist in production.

A workaround is available, provided by [@ohmpatel1997](https://github.com/ohmpatel1997) [here](https://github.com/googleapis/nodejs-datastore/issues/95#issuecomment-554387312).

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/nodejs-datastore/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
Concepts | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/concepts.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/concepts.js,samples/README.md)  
Error | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/error.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/error.js,samples/README.md)  
Export | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/export.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/export.js,samples/README.md)  
Import | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/import.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/import.js,samples/README.md)  
Indexes.get | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/indexes.get.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/indexes.get.js,samples/README.md)  
Indexes.list | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/indexes.list.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/indexes.list.js,samples/README.md)  
Create a union between two filters | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/queryFilterOr.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/queryFilterOr.js,samples/README.md)  
Run query explain (regular query) | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/queryProfileExplain.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/queryProfileExplain.js,samples/README.md)  
Run query explain (aggregate query) | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/queryProfileExplainAggregation.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/queryProfileExplainAggregation.js,samples/README.md)  
Run query explain analyze (regular query) | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/queryProfileExplainAnalyze.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/queryProfileExplainAnalyze.js,samples/README.md)  
Run query explain analyze (aggregate query) | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/queryProfileExplainAnalyzeAggregation.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/queryProfileExplainAnalyzeAggregation.js,samples/README.md)  
Quickstart | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/quickstart.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/quickstart.js,samples/README.md)  
Add Task | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/tasks.add.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/tasks.add.js,samples/README.md)  
Delete Task | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/tasks.delete.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/tasks.delete.js,samples/README.md)  
Legacy Samples | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/tasks.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/tasks.js,samples/README.md)  
List Tasks | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/tasks.list.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/tasks.list.js,samples/README.md)  
Update Task | [source code](https://github.com/googleapis/nodejs-datastore/blob/main/samples/tasks.markdone.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-datastore&page=editor&open_in_editor=samples/tasks.markdone.js,samples/README.md)  
  
The [Google Cloud Datastore Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/datastore/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/datastore@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-datastore/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/nodejs-datastore/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
