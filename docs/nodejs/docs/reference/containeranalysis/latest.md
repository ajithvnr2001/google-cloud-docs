---
url: https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/
title: Container Analysis API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:35.613150+00:00
---

# Container Analysis API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Container Analysis API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

7.0.2 (latest)  7.0.1  6.8.0  6.7.0  6.5.0  5.6.0  5.0.1  4.7.0  4.4.2  4.3.0  3.4.0  3.3.0  3.2.0  3.1.8 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/containeranalysis.svg)](https://www.npmjs.org/package/@google-cloud/containeranalysis)

Container Analysis API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/CHANGELOG.md).

  * [Container Analysis API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/containeranalysis/latest)



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
  3. [Enable the Container Analysis API API](https://console.cloud.google.com/flows/enableapi?apiid=containeranalysis.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/containeranalysis
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
export s b o m | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/container_analysis.export_s_b_o_m.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/container_analysis.get_iam_policy.js)  
get vulnerability occurrences summary | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/container_analysis.get_vulnerability_occurrences_summary.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/container_analysis.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/container_analysis.test_iam_permissions.js)  
batch create notes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.batch_create_notes.js)  
batch create occurrences | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.batch_create_occurrences.js)  
create note | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.create_note.js)  
create occurrence | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.create_occurrence.js)  
delete note | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.delete_note.js)  
delete occurrence | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.delete_occurrence.js)  
get note | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.get_note.js)  
get occurrence | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.get_occurrence.js)  
get occurrence note | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.get_occurrence_note.js)  
list note occurrences | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.list_note_occurrences.js)  
list notes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.list_notes.js)  
list occurrences | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.list_occurrences.js)  
update note | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.update_note.js)  
update occurrence | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1/grafeas.update_occurrence.js)  
export s b o m | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/container_analysis_v1_beta1.export_s_b_o_m.js)  
generate packages summary | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/container_analysis_v1_beta1.generate_packages_summary.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/container_analysis_v1_beta1.get_iam_policy.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/container_analysis_v1_beta1.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/container_analysis_v1_beta1.test_iam_permissions.js)  
batch create notes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.batch_create_notes.js)  
batch create occurrences | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.batch_create_occurrences.js)  
create note | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.create_note.js)  
create occurrence | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.create_occurrence.js)  
delete note | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.delete_note.js)  
delete occurrence | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.delete_occurrence.js)  
get note | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.get_note.js)  
get occurrence | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.get_occurrence.js)  
get occurrence note | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.get_occurrence_note.js)  
get vulnerability occurrences summary | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.get_vulnerability_occurrences_summary.js)  
list note occurrences | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.list_note_occurrences.js)  
list notes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.list_notes.js)  
list occurrences | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.list_occurrences.js)  
update note | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.update_note.js)  
update occurrence | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-containeranalysis/samples/generated/v1beta1/grafeas_v1_beta1.update_occurrence.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/containeranalysis@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
