---
url: https://docs.cloud.google.com/nodejs/docs/reference/apphub/latest/
title: App Hub API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:01.058361+00:00
---

# App Hub API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apphub/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  App Hub API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.1.0 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/apphub.svg)](https://www.npmjs.org/package/@google-cloud/apphub)

App Hub API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/CHANGELOG.md).

  * [App Hub API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/apphub/latest)
  * [App Hub API Documentation](https://cloud.google.com/app-hub/docs/overview)



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
  3. [Enable the App Hub API API](https://console.cloud.google.com/flows/enableapi?apiid=apphub.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/apphub
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create application | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.create_application.js)  
create service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.create_service.js)  
create service project attachment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.create_service_project_attachment.js)  
create workload | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.create_workload.js)  
delete application | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.delete_application.js)  
delete service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.delete_service.js)  
delete service project attachment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.delete_service_project_attachment.js)  
delete workload | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.delete_workload.js)  
detach service project attachment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.detach_service_project_attachment.js)  
get application | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.get_application.js)  
get discovered service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.get_discovered_service.js)  
get discovered workload | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.get_discovered_workload.js)  
get service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.get_service.js)  
get service project attachment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.get_service_project_attachment.js)  
get workload | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.get_workload.js)  
list applications | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.list_applications.js)  
list discovered services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.list_discovered_services.js)  
list discovered workloads | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.list_discovered_workloads.js)  
list service project attachments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.list_service_project_attachments.js)  
list services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.list_services.js)  
list workloads | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.list_workloads.js)  
lookup discovered service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.lookup_discovered_service.js)  
lookup discovered workload | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.lookup_discovered_workload.js)  
lookup service project attachment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.lookup_service_project_attachment.js)  
update application | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.update_application.js)  
update service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.update_service.js)  
update workload | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apphub/samples/generated/v1/app_hub.update_workload.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/apphub@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
