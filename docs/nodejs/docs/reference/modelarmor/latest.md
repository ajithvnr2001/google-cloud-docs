---
url: https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/
title: Model Armor API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:17.723026+00:00
---

# Model Armor API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Model Armor API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/modelarmor.svg)](https://www.npmjs.org/package/@google-cloud/modelarmor)

Model Armor API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/CHANGELOG.md).

  * [Model Armor API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/modelarmor/latest)
  * [Model Armor API Documentation](https://cloud.google.com/security-command-center/docs/model-armor-overview)



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
  3. [Enable the Model Armor API API](https://console.cloud.google.com/flows/enableapi?apiid=modelarmor.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/modelarmor
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1/model_armor.create_template.js)  
delete template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1/model_armor.delete_template.js)  
get floor setting | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1/model_armor.get_floor_setting.js)  
get template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1/model_armor.get_template.js)  
list templates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1/model_armor.list_templates.js)  
sanitize model response | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1/model_armor.sanitize_model_response.js)  
sanitize user prompt | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1/model_armor.sanitize_user_prompt.js)  
update floor setting | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1/model_armor.update_floor_setting.js)  
update template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1/model_armor.update_template.js)  
create template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1beta/model_armor.create_template.js)  
delete template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1beta/model_armor.delete_template.js)  
get floor setting | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1beta/model_armor.get_floor_setting.js)  
get template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1beta/model_armor.get_template.js)  
list templates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1beta/model_armor.list_templates.js)  
sanitize model response | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1beta/model_armor.sanitize_model_response.js)  
sanitize user prompt | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1beta/model_armor.sanitize_user_prompt.js)  
stream sanitize model response | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1beta/model_armor.stream_sanitize_model_response.js)  
stream sanitize user prompt | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1beta/model_armor.stream_sanitize_user_prompt.js)  
update floor setting | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1beta/model_armor.update_floor_setting.js)  
update template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-modelarmor/samples/generated/v1beta/model_armor.update_template.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/modelarmor@legacy-8` installs client libraries for versions compatible with Node.js 8.

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

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
