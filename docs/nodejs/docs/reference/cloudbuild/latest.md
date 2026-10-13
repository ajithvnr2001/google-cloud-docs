---
url: https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/
title: Cloud Build API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:33.620186+00:00
---

# Cloud Build API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Build API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.6.0  5.5.0  5.1.0  4.8.0  4.7.0  4.1.1  4.0.0  3.6.0  3.3.0  3.2.0  3.1.2  2.6.0  2.5.0  2.4.0  2.3.2  2.2.7 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/cloudbuild.svg)](https://www.npmjs.org/package/@google-cloud/cloudbuild)

Cloud Build API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/CHANGELOG.md).

  * [Cloud Build API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/cloudbuild/latest)



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
  3. [Enable the Cloud Build API API](https://console.cloud.google.com/flows/enableapi?apiid=cloudbuild.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/cloudbuild
    

### Using TypeScript

`@google-cloud/cloudbuild` provides TypeScript type definitions.

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
approve build | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.approve_build.js)  
cancel build | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.cancel_build.js)  
create build | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.create_build.js)  
create build trigger | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.create_build_trigger.js)  
create worker pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.create_worker_pool.js)  
delete build trigger | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.delete_build_trigger.js)  
delete worker pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.delete_worker_pool.js)  
get build | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.get_build.js)  
get build trigger | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.get_build_trigger.js)  
get default service account | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.get_default_service_account.js)  
get worker pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.get_worker_pool.js)  
list build triggers | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.list_build_triggers.js)  
list builds | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.list_builds.js)  
list worker pools | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.list_worker_pools.js)  
receive trigger webhook | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.receive_trigger_webhook.js)  
retry build | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.retry_build.js)  
run build trigger | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.run_build_trigger.js)  
update build trigger | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.update_build_trigger.js)  
update worker pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v1/cloud_build.update_worker_pool.js)  
batch create repositories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.batch_create_repositories.js)  
create connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.create_connection.js)  
create repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.create_repository.js)  
delete connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.delete_connection.js)  
delete repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.delete_repository.js)  
fetch git refs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.fetch_git_refs.js)  
fetch linkable repositories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.fetch_linkable_repositories.js)  
fetch read token | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.fetch_read_token.js)  
fetch read write token | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.fetch_read_write_token.js)  
get connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.get_connection.js)  
get repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.get_repository.js)  
list connections | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.list_connections.js)  
list repositories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.list_repositories.js)  
update connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-cloudbuild/samples/generated/v2/repository_manager.update_connection.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/cloudbuild@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
