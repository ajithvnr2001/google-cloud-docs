---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/
title: Dataproc Metastore API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:40.960867+00:00
---

# Dataproc Metastore API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Dataproc Metastore API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.0  4.1.0  3.5.0  3.4.1  3.1.2  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.6 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/dataproc-metastore.svg)](https://www.npmjs.org/package/@google-cloud/dataproc-metastore)

Dataproc Metastore API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/CHANGELOG.md).

  * [Dataproc Metastore API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/metastore/latest)



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
  3. [Enable the Dataproc Metastore API API](https://console.cloud.google.com/flows/enableapi?apiid=metastore.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/dataproc-metastore
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
alter metadata resource location | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.alter_metadata_resource_location.js)  
create backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.create_backup.js)  
create metadata import | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.create_metadata_import.js)  
create service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.create_service.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.delete_backup.js)  
delete service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.delete_service.js)  
export metadata | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.export_metadata.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.get_backup.js)  
get metadata import | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.get_metadata_import.js)  
get service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.get_service.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.list_backups.js)  
list metadata imports | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.list_metadata_imports.js)  
list services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.list_services.js)  
move table to database | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.move_table_to_database.js)  
query metadata | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.query_metadata.js)  
restore service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.restore_service.js)  
update metadata import | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.update_metadata_import.js)  
update service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore.update_service.js)  
create federation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore_federation.create_federation.js)  
delete federation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore_federation.delete_federation.js)  
get federation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore_federation.get_federation.js)  
list federations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore_federation.list_federations.js)  
update federation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1/dataproc_metastore_federation.update_federation.js)  
alter metadata resource location | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.alter_metadata_resource_location.js)  
create backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.create_backup.js)  
create metadata import | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.create_metadata_import.js)  
create service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.create_service.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.delete_backup.js)  
delete service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.delete_service.js)  
export metadata | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.export_metadata.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.get_backup.js)  
get metadata import | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.get_metadata_import.js)  
get service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.get_service.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.list_backups.js)  
list metadata imports | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.list_metadata_imports.js)  
list services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.list_services.js)  
move table to database | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.move_table_to_database.js)  
query metadata | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.query_metadata.js)  
remove iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.remove_iam_policy.js)  
restore service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.restore_service.js)  
update metadata import | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.update_metadata_import.js)  
update service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore.update_service.js)  
create federation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore_federation.create_federation.js)  
delete federation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore_federation.delete_federation.js)  
get federation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore_federation.get_federation.js)  
list federations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore_federation.list_federations.js)  
update federation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1alpha/dataproc_metastore_federation.update_federation.js)  
alter metadata resource location | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.alter_metadata_resource_location.js)  
create backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.create_backup.js)  
create metadata import | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.create_metadata_import.js)  
create service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.create_service.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.delete_backup.js)  
delete service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.delete_service.js)  
export metadata | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.export_metadata.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.get_backup.js)  
get metadata import | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.get_metadata_import.js)  
get service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.get_service.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.list_backups.js)  
list metadata imports | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.list_metadata_imports.js)  
list services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.list_services.js)  
move table to database | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.move_table_to_database.js)  
query metadata | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.query_metadata.js)  
remove iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.remove_iam_policy.js)  
restore service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.restore_service.js)  
update metadata import | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.update_metadata_import.js)  
update service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore.update_service.js)  
create federation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore_federation.create_federation.js)  
delete federation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore_federation.delete_federation.js)  
get federation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore_federation.get_federation.js)  
list federations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore_federation.list_federations.js)  
update federation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-metastore/samples/generated/v1beta/dataproc_metastore_federation.update_federation.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/dataproc-metastore@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
