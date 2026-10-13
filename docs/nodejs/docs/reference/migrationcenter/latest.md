---
url: https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/
title: Migration Center API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:18.548823+00:00
---

# Migration Center API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Migration Center API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.0 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/migrationcenter.svg)](https://www.npmjs.org/package/@google-cloud/migrationcenter)

Migration Center API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/CHANGELOG.md).

  * [Migration Center API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/migrationcenter/latest)
  * [Migration Center API Documentation](https://cloud.google.com/migration-center/docs/migration-center-overview)



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
  3. [Enable the Migration Center API API](https://console.cloud.google.com/flows/enableapi?apiid=migrationcenter.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/migrationcenter
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
add assets to group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.add_assets_to_group.js)  
aggregate assets values | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.aggregate_assets_values.js)  
batch delete assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.batch_delete_assets.js)  
batch update assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.batch_update_assets.js)  
create group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.create_group.js)  
create import data file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.create_import_data_file.js)  
create import job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.create_import_job.js)  
create preference set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.create_preference_set.js)  
create report | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.create_report.js)  
create report config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.create_report_config.js)  
create source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.create_source.js)  
delete asset | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.delete_asset.js)  
delete group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.delete_group.js)  
delete import data file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.delete_import_data_file.js)  
delete import job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.delete_import_job.js)  
delete preference set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.delete_preference_set.js)  
delete report | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.delete_report.js)  
delete report config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.delete_report_config.js)  
delete source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.delete_source.js)  
get asset | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.get_asset.js)  
get error frame | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.get_error_frame.js)  
get group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.get_group.js)  
get import data file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.get_import_data_file.js)  
get import job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.get_import_job.js)  
get preference set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.get_preference_set.js)  
get report | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.get_report.js)  
get report config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.get_report_config.js)  
get settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.get_settings.js)  
get source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.get_source.js)  
list assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.list_assets.js)  
list error frames | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.list_error_frames.js)  
list groups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.list_groups.js)  
list import data files | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.list_import_data_files.js)  
list import jobs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.list_import_jobs.js)  
list preference sets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.list_preference_sets.js)  
list report configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.list_report_configs.js)  
list reports | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.list_reports.js)  
list sources | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.list_sources.js)  
remove assets from group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.remove_assets_from_group.js)  
report asset frames | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.report_asset_frames.js)  
run import job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.run_import_job.js)  
update asset | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.update_asset.js)  
update group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.update_group.js)  
update import job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.update_import_job.js)  
update preference set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.update_preference_set.js)  
update settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.update_settings.js)  
update source | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.update_source.js)  
validate import job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-migrationcenter/samples/generated/v1/migration_center.validate_import_job.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/migrationcenter@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
