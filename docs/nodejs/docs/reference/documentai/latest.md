---
url: https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/
title: Cloud Document AI API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:44.046164+00:00
---

# Cloud Document AI API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Document AI API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  9.6.0  9.2.0  8.12.0  8.10.0  8.8.0  8.6.0  8.5.0  8.4.0  8.2.0  8.1.2  8.0.0  7.3.1  7.1.0  7.0.1  6.3.0  6.1.0  6.0.0  3.3.0  3.2.1  3.1.0  3.0.2  2.10.0 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/documentai.svg)](https://www.npmjs.org/package/@google-cloud/documentai)

Cloud Document AI API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/CHANGELOG.md).

  * [Cloud Document AI API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/documentai/latest)
  * [Cloud Document AI API Documentation](https://cloud.google.com/document-ai/docs)



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
  2. [Enable billing for your project](https://support.google.com/cloud/answer/6293499#enable-billing).
  3. [Enable the Cloud Document AI API API](https://console.cloud.google.com/flows/enableapi?apiid=documentai.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/documentai
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
batch process documents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.batch_process_documents.js)  
create processor | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.create_processor.js)  
delete processor | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.delete_processor.js)  
delete processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.delete_processor_version.js)  
deploy processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.deploy_processor_version.js)  
disable processor | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.disable_processor.js)  
enable processor | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.enable_processor.js)  
evaluate processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.evaluate_processor_version.js)  
fetch processor types | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.fetch_processor_types.js)  
get evaluation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.get_evaluation.js)  
get processor | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.get_processor.js)  
get processor type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.get_processor_type.js)  
get processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.get_processor_version.js)  
list evaluations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.list_evaluations.js)  
list processor types | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.list_processor_types.js)  
list processor versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.list_processor_versions.js)  
list processors | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.list_processors.js)  
process document | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.process_document.js)  
review document | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.review_document.js)  
set default processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.set_default_processor_version.js)  
train processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.train_processor_version.js)  
undeploy processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1/document_processor_service.undeploy_processor_version.js)  
batch process documents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.batch_process_documents.js)  
create processor | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.create_processor.js)  
delete processor | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.delete_processor.js)  
delete processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.delete_processor_version.js)  
deploy processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.deploy_processor_version.js)  
disable processor | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.disable_processor.js)  
enable processor | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.enable_processor.js)  
evaluate processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.evaluate_processor_version.js)  
fetch processor types | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.fetch_processor_types.js)  
get evaluation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.get_evaluation.js)  
get processor | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.get_processor.js)  
get processor type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.get_processor_type.js)  
get processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.get_processor_version.js)  
import processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.import_processor_version.js)  
list evaluations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.list_evaluations.js)  
list processor types | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.list_processor_types.js)  
list processor versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.list_processor_versions.js)  
list processors | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.list_processors.js)  
process document | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.process_document.js)  
review document | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.review_document.js)  
set default processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.set_default_processor_version.js)  
train processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.train_processor_version.js)  
undeploy processor version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_processor_service.undeploy_processor_version.js)  
batch delete documents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_service.batch_delete_documents.js)  
get dataset schema | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_service.get_dataset_schema.js)  
get document | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_service.get_document.js)  
import documents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_service.import_documents.js)  
list documents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_service.list_documents.js)  
update dataset | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_service.update_dataset.js)  
update dataset schema | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-documentai/samples/generated/v1beta3/document_service.update_dataset_schema.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/documentai@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/google-cloud-node/blob/main/CONTRIBUTING.md).

Please note that this `README.md` and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template.

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/google-cloud-node/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
