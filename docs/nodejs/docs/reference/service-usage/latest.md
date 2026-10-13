---
url: https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/
title: Service Usage API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:14.633838+00:00
---

# Service Usage API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Service Usage API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.3.0  2.2.2  2.1.2  1.2.1  1.1.4 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/service-usage.svg)](https://www.npmjs.org/package/@google-cloud/service-usage)

Service Usage API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/CHANGELOG.md).

  * [Service Usage API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/serviceusage/latest)



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
  3. [Enable the Service Usage API API](https://console.cloud.google.com/flows/enableapi?apiid=serviceusage.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/service-usage
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
batch enable services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1/service_usage.batch_enable_services.js)  
batch get services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1/service_usage.batch_get_services.js)  
disable service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1/service_usage.disable_service.js)  
enable service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1/service_usage.enable_service.js)  
get service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1/service_usage.get_service.js)  
list services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1/service_usage.list_services.js)  
batch enable services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.batch_enable_services.js)  
create admin override | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.create_admin_override.js)  
create consumer override | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.create_consumer_override.js)  
delete admin override | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.delete_admin_override.js)  
delete consumer override | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.delete_consumer_override.js)  
disable service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.disable_service.js)  
enable service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.enable_service.js)  
generate service identity | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.generate_service_identity.js)  
get consumer quota limit | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.get_consumer_quota_limit.js)  
get consumer quota metric | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.get_consumer_quota_metric.js)  
get service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.get_service.js)  
import admin overrides | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.import_admin_overrides.js)  
import consumer overrides | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.import_consumer_overrides.js)  
list admin overrides | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.list_admin_overrides.js)  
list consumer overrides | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.list_consumer_overrides.js)  
list consumer quota metrics | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.list_consumer_quota_metrics.js)  
list services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.list_services.js)  
update admin override | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.update_admin_override.js)  
update consumer override | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-api-serviceusage/samples/generated/v1beta1/service_usage.update_consumer_override.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/service-usage@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
