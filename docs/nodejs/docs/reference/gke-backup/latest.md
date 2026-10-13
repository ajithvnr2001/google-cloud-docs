---
url: https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/
title: Backup for GKE API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:09.817721+00:00
---

# Backup for GKE API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Backup for GKE API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.0  2.0.1  1.3.0  1.0.0  0.3.2  0.2.2 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/gke-backup.svg)](https://www.npmjs.org/package/@google-cloud/gke-backup)

Backup for GKE API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/CHANGELOG.md).

  * [Backup for GKE API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/gkebackup/latest)
  * [Backup for GKE API Documentation](https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



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
  3. [Enable the Backup for GKE API API](https://console.cloud.google.com/flows/enableapi?apiid=gkebackup.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/gke-backup
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.create_backup.js)  
create backup channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.create_backup_channel.js)  
create backup plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.create_backup_plan.js)  
create restore | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.create_restore.js)  
create restore channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.create_restore_channel.js)  
create restore plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.create_restore_plan.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.delete_backup.js)  
delete backup channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.delete_backup_channel.js)  
delete backup plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.delete_backup_plan.js)  
delete restore | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.delete_restore.js)  
delete restore channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.delete_restore_channel.js)  
delete restore plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.delete_restore_plan.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.get_backup.js)  
get backup channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.get_backup_channel.js)  
get backup index download url | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.get_backup_index_download_url.js)  
get backup plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.get_backup_plan.js)  
get backup plan binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.get_backup_plan_binding.js)  
get restore | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.get_restore.js)  
get restore channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.get_restore_channel.js)  
get restore plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.get_restore_plan.js)  
get restore plan binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.get_restore_plan_binding.js)  
get volume backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.get_volume_backup.js)  
get volume restore | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.get_volume_restore.js)  
list backup channels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.list_backup_channels.js)  
list backup plan bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.list_backup_plan_bindings.js)  
list backup plans | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.list_backup_plans.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.list_backups.js)  
list restore channels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.list_restore_channels.js)  
list restore plan bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.list_restore_plan_bindings.js)  
list restore plans | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.list_restore_plans.js)  
list restores | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.list_restores.js)  
list volume backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.list_volume_backups.js)  
list volume restores | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.list_volume_restores.js)  
update backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.update_backup.js)  
update backup channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.update_backup_channel.js)  
update backup plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.update_backup_plan.js)  
update restore | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.update_restore.js)  
update restore channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.update_restore_channel.js)  
update restore plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkebackup/samples/generated/v1/backup_for_g_k_e.update_restore_plan.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/gke-backup@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
