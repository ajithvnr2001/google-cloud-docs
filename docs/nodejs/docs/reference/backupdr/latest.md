---
url: https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/
title: Backup and DR Service API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:26.516336+00:00
---

# Backup and DR Service API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Backup and DR Service API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.12.1 (latest)  0.12.0  0.9.0  0.8.0  0.7.0  0.6.0  0.1.0 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/backupdr.svg)](https://www.npmjs.org/package/@google-cloud/backupdr)

Backup and DR Service API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/CHANGELOG.md).

  * [Backup and DR Service API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/backupdr/latest)
  * [Backup and DR Service API Documentation](https://cloud.google.com/backup-disaster-recovery/docs/reference/rpc)



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
  3. [Enable the Backup and DR Service API API](https://console.cloud.google.com/flows/enableapi?apiid=backupdr.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/backupdr
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create backup plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.create_backup_plan.js)  
create backup plan association | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.create_backup_plan_association.js)  
create backup vault | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.create_backup_vault.js)  
create management server | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.create_management_server.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.delete_backup.js)  
delete backup plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.delete_backup_plan.js)  
delete backup plan association | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.delete_backup_plan_association.js)  
delete backup vault | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.delete_backup_vault.js)  
delete management server | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.delete_management_server.js)  
fetch backup plan associations for resource type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.fetch_backup_plan_associations_for_resource_type.js)  
fetch backups for resource type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.fetch_backups_for_resource_type.js)  
fetch data source references for resource type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.fetch_data_source_references_for_resource_type.js)  
fetch usable backup vaults | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.fetch_usable_backup_vaults.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.get_backup.js)  
get backup plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.get_backup_plan.js)  
get backup plan association | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.get_backup_plan_association.js)  
get backup plan revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.get_backup_plan_revision.js)  
get backup vault | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.get_backup_vault.js)  
get data source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.get_data_source.js)  
get data source reference | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.get_data_source_reference.js)  
get management server | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.get_management_server.js)  
initialize service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.initialize_service.js)  
list backup plan associations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.list_backup_plan_associations.js)  
list backup plan revisions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.list_backup_plan_revisions.js)  
list backup plans | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.list_backup_plans.js)  
list backup vaults | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.list_backup_vaults.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.list_backups.js)  
list data source references | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.list_data_source_references.js)  
list data sources | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.list_data_sources.js)  
list management servers | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.list_management_servers.js)  
restore backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.restore_backup.js)  
trigger backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.trigger_backup.js)  
update backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.update_backup.js)  
update backup plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.update_backup_plan.js)  
update backup plan association | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.update_backup_plan_association.js)  
update backup vault | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.update_backup_vault.js)  
update data source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_d_r.update_data_source.js)  
list resource backup configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-backupdr/samples/generated/v1/backup_dr_protection_summary.list_resource_backup_configs.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/backupdr@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
