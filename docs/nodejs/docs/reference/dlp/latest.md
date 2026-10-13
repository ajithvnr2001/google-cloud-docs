---
url: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/
title: Sensitive Data Protection (DLP): Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:43.230776+00:00
---

# Sensitive Data Protection (DLP): Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Sensitive Data Protection (DLP): Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  7.0.1  6.6.0  6.2.0  6.1.0  5.13.0  5.11.0  5.10.0  5.7.0  5.5.0  5.3.0  5.0.0  4.4.2  4.2.0  4.1.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.8 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/dlp.svg)](https://www.npmjs.org/package/@google-cloud/dlp)

Sensitive Data Protection (DLP) client for Node.js

The [Data Loss Prevention API](https://cloud.google.com/dlp/docs/) provides programmatic access to a powerful detection engine for personally identifiable information and other privacy-sensitive data in unstructured data streams.

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/CHANGELOG.md).

  * [Sensitive Data Protection (DLP) Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/dlp/latest)



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
  3. [Enable the Sensitive Data Protection (DLP) API](https://console.cloud.google.com/flows/enableapi?apiid=dlp.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/dlp
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
activate job trigger | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.activate_job_trigger.js)  
cancel dlp job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.cancel_dlp_job.js)  
create connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.create_connection.js)  
create deidentify template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.create_deidentify_template.js)  
create discovery config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.create_discovery_config.js)  
create dlp job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.create_dlp_job.js)  
create inspect template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.create_inspect_template.js)  
create job trigger | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.create_job_trigger.js)  
create stored info type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.create_stored_info_type.js)  
deidentify content | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.deidentify_content.js)  
delete connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.delete_connection.js)  
delete deidentify template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.delete_deidentify_template.js)  
delete discovery config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.delete_discovery_config.js)  
delete dlp job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.delete_dlp_job.js)  
delete file store data profile | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.delete_file_store_data_profile.js)  
delete inspect template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.delete_inspect_template.js)  
delete job trigger | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.delete_job_trigger.js)  
delete stored info type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.delete_stored_info_type.js)  
delete table data profile | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.delete_table_data_profile.js)  
finish dlp job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.finish_dlp_job.js)  
get column data profile | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.get_column_data_profile.js)  
get connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.get_connection.js)  
get deidentify template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.get_deidentify_template.js)  
get discovery config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.get_discovery_config.js)  
get dlp job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.get_dlp_job.js)  
get file store data profile | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.get_file_store_data_profile.js)  
get inspect template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.get_inspect_template.js)  
get job trigger | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.get_job_trigger.js)  
get project data profile | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.get_project_data_profile.js)  
get stored info type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.get_stored_info_type.js)  
get table data profile | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.get_table_data_profile.js)  
hybrid inspect dlp job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.hybrid_inspect_dlp_job.js)  
hybrid inspect job trigger | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.hybrid_inspect_job_trigger.js)  
inspect content | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.inspect_content.js)  
list column data profiles | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.list_column_data_profiles.js)  
list connections | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.list_connections.js)  
list deidentify templates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.list_deidentify_templates.js)  
list discovery configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.list_discovery_configs.js)  
list dlp jobs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.list_dlp_jobs.js)  
list file store data profiles | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.list_file_store_data_profiles.js)  
list info types | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.list_info_types.js)  
list inspect templates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.list_inspect_templates.js)  
list job triggers | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.list_job_triggers.js)  
list project data profiles | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.list_project_data_profiles.js)  
list stored info types | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.list_stored_info_types.js)  
list table data profiles | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.list_table_data_profiles.js)  
redact image | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.redact_image.js)  
reidentify content | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.reidentify_content.js)  
search connections | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.search_connections.js)  
update connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.update_connection.js)  
update deidentify template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.update_deidentify_template.js)  
update discovery config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.update_discovery_config.js)  
update inspect template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.update_inspect_template.js)  
update job trigger | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.update_job_trigger.js)  
update stored info type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-privacy-dlp/samples/generated/v2/dlp_service.update_stored_info_type.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/dlp@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
