---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/
title: Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:28.358041+00:00
---

# Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 6.0.0 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/)
  * [ 5.1.2 ](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/5.1.2/)
  * [ 5.0.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/5.0.0/)
  * [ 4.6.1 ](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/4.6.1/)
  * [ 4.1.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/4.1.0/)
  * [ 4.0.5 ](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/4.0.5/)
  * [ 3.10.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/3.10.0/)
  * [ 3.9.4 ](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/3.9.4/)
  * [ 3.8.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/3.8.0/)
  * [ 3.7.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/3.7.0/)
  * [ 3.6.0 ](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/3.6.0/)
  * [ 3.5.4 ](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/3.5.4/)



# [Cloud Bigtable: Node.js Client](https://github.com/googleapis/nodejs-bigtable)

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/bigtable.svg)](https://www.npmjs.org/package/@google-cloud/bigtable)

Cloud Bigtable Client Library for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/nodejs-bigtable/blob/main/CHANGELOG.md).

  * [Cloud Bigtable Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/bigtable/latest)
  * [Cloud Bigtable Documentation](https://cloud.google.com/bigtable)
  * [github.com/googleapis/nodejs-bigtable](https://github.com/googleapis/nodejs-bigtable)



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
  2. [Enable billing for your project](https://support.google.com/cloud/answer/6293499#enable-billing).
  3. [Enable the Cloud Bigtable API](https://console.cloud.google.com/flows/enableapi?apiid=bigtable.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation.



### Installing the client library
    
    
    npm install @google-cloud/bigtable
    

### Using the client library
    
    
    // Imports the Google Cloud client library
    const {Bigtable} = require('[@google-cloud/bigtable](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/overview.html)');
    
    const bigtable = new [Bigtable](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/bigtable/bigtable.html)();
    
    async function quickstart() {
      // Connect to an existing instance:my-bigtable-instance
      const instance = bigtable.instance(INSTANCE_ID);
    
      // Connect to an existing table:my-table
      const table = instance.table(TABLE_ID);
    
      // Read a row from my-table using a row key
      const [singleRow] = await table.row('r1').get();
    
      // Print the row key and data (column value, labels, timestamp)
      const rowData = JSON.stringify(singleRow.data, null, 4);
      console.log(`Row key: ${singleRow.id}\nData: ${rowData}`);
    }
    quickstart();
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/nodejs-bigtable/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
Delete Snippets | [source code](https://github.com/googleapis/nodejs-bigtable/blob/main/samples/deleteSnippets.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigtable&page=editor&open_in_editor=samples/deleteSnippets.js,samples/README.md)  
Filter Snippets | [source code](https://github.com/googleapis/nodejs-bigtable/blob/main/samples/filterSnippets.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigtable&page=editor&open_in_editor=samples/filterSnippets.js,samples/README.md)  
Instances | [source code](https://github.com/googleapis/nodejs-bigtable/blob/main/samples/instances.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigtable&page=editor&open_in_editor=samples/instances.js,samples/README.md)  
Quickstart | [source code](https://github.com/googleapis/nodejs-bigtable/blob/main/samples/quickstart.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigtable&page=editor&open_in_editor=samples/quickstart.js,samples/README.md)  
Read Snippets | [source code](https://github.com/googleapis/nodejs-bigtable/blob/main/samples/readSnippets.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigtable&page=editor&open_in_editor=samples/readSnippets.js,samples/README.md)  
Tableadmin | [source code](https://github.com/googleapis/nodejs-bigtable/blob/main/samples/tableadmin.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigtable&page=editor&open_in_editor=samples/tableadmin.js,samples/README.md)  
Write Batch | [source code](https://github.com/googleapis/nodejs-bigtable/blob/main/samples/writeBatch.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigtable&page=editor&open_in_editor=samples/writeBatch.js,samples/README.md)  
Write Conditionally | [source code](https://github.com/googleapis/nodejs-bigtable/blob/main/samples/writeConditionally.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigtable&page=editor&open_in_editor=samples/writeConditionally.js,samples/README.md)  
Write Increment | [source code](https://github.com/googleapis/nodejs-bigtable/blob/main/samples/writeIncrement.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigtable&page=editor&open_in_editor=samples/writeIncrement.js,samples/README.md)  
Simple Insert | [source code](https://github.com/googleapis/nodejs-bigtable/blob/main/samples/writeSimple.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-bigtable&page=editor&open_in_editor=samples/writeSimple.js,samples/README.md)  
  
The [Cloud Bigtable Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/bigtable/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/bigtable@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-bigtable/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/nodejs-bigtable/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
