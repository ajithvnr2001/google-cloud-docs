---
url: https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/
title: Storage Control API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:15.879882+00:00
---

# Storage Control API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Storage Control API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.1.1 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/storage-control.svg)](https://www.npmjs.org/package/@google-cloud/storage-control)

Storage Control API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/CHANGELOG.md).

  * [Storage Control API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/storage-control/latest)
  * [Storage Control API Documentation](https://cloud.google.com/storage/docs/overview)



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
  3. [Enable the Storage Control API API](https://console.cloud.google.com/flows/enableapi?apiid=storage.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/storage-control
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
storage | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/snippet_metadata_google.storage.control.v2.json)  
storage | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/snippet_metadata_google.storage.v2.json)  
create bucket | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage.create_bucket.js)  
delete bucket | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage.delete_bucket.js)  
get bucket | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage.get_bucket.js)  
list buckets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage.list_buckets.js)  
lock bucket retention policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage.lock_bucket_retention_policy.js)  
update bucket | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage.update_bucket.js)  
create anywhere cache | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.create_anywhere_cache.js)  
create folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.create_folder.js)  
create managed folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.create_managed_folder.js)  
delete folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.delete_folder.js)  
delete folder recursive | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.delete_folder_recursive.js)  
delete managed folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.delete_managed_folder.js)  
disable anywhere cache | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.disable_anywhere_cache.js)  
get anywhere cache | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.get_anywhere_cache.js)  
get folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.get_folder.js)  
get folder intelligence config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.get_folder_intelligence_config.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.get_iam_policy.js)  
get managed folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.get_managed_folder.js)  
get organization intelligence config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.get_organization_intelligence_config.js)  
get project intelligence config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.get_project_intelligence_config.js)  
get storage layout | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.get_storage_layout.js)  
list anywhere caches | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.list_anywhere_caches.js)  
list folders | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.list_folders.js)  
list managed folders | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.list_managed_folders.js)  
pause anywhere cache | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.pause_anywhere_cache.js)  
rename folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.rename_folder.js)  
resume anywhere cache | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.resume_anywhere_cache.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.test_iam_permissions.js)  
update anywhere cache | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.update_anywhere_cache.js)  
update folder intelligence config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.update_folder_intelligence_config.js)  
update organization intelligence config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.update_organization_intelligence_config.js)  
update project intelligence config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/samples/generated/v2/storage_control.update_project_intelligence_config.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/storage-control@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/CONTRIBUTING.md).

Please note that this `README.md` and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template.

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-storage-control/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-26 UTC."],[],[]] 
