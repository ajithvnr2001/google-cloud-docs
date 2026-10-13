---
url: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/
title: Data Labeling API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:39.835956+00:00
---

# Data Labeling API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Data Labeling API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.2.2  3.1.1  2.3.0  2.2.7 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/datalabeling.svg)](https://www.npmjs.org/package/@google-cloud/datalabeling)

Data Labeling API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/CHANGELOG.md).

  * [Data Labeling API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/datalabeling/latest)



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
  3. [Enable the Data Labeling API API](https://console.cloud.google.com/flows/enableapi?apiid=datalabeling.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/datalabeling
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create annotation spec set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.create_annotation_spec_set.js)  
create dataset | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.create_dataset.js)  
create evaluation job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.create_evaluation_job.js)  
create instruction | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.create_instruction.js)  
delete annotated dataset | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.delete_annotated_dataset.js)  
delete annotation spec set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.delete_annotation_spec_set.js)  
delete dataset | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.delete_dataset.js)  
delete evaluation job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.delete_evaluation_job.js)  
delete instruction | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.delete_instruction.js)  
export data | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.export_data.js)  
get annotated dataset | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.get_annotated_dataset.js)  
get annotation spec set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.get_annotation_spec_set.js)  
get data item | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.get_data_item.js)  
get dataset | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.get_dataset.js)  
get evaluation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.get_evaluation.js)  
get evaluation job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.get_evaluation_job.js)  
get example | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.get_example.js)  
get instruction | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.get_instruction.js)  
import data | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.import_data.js)  
label image | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.label_image.js)  
label text | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.label_text.js)  
label video | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.label_video.js)  
list annotated datasets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.list_annotated_datasets.js)  
list annotation spec sets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.list_annotation_spec_sets.js)  
list data items | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.list_data_items.js)  
list datasets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.list_datasets.js)  
list evaluation jobs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.list_evaluation_jobs.js)  
list examples | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.list_examples.js)  
list instructions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.list_instructions.js)  
pause evaluation job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.pause_evaluation_job.js)  
resume evaluation job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.resume_evaluation_job.js)  
search evaluations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.search_evaluations.js)  
search example comparisons | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.search_example_comparisons.js)  
update evaluation job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-datalabeling/samples/generated/v1beta1/data_labeling_service.update_evaluation_job.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/datalabeling@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
