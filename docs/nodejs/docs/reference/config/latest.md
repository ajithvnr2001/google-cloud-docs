---
url: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/
title: Infrastructure Manager API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:34.885977+00:00
---

# Infrastructure Manager API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Infrastructure Manager API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.14.0  0.12.0  0.7.0  0.5.0  0.2.0  0.1.1 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/config.svg)](https://www.npmjs.org/package/@google-cloud/config)

Infrastructure Manager API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/CHANGELOG.md).

  * [Infrastructure Manager API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/config/latest)
  * [Infrastructure Manager API Documentation](https://cloud.google.com/infrastructure-manager/docs/overview)



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
  3. [Enable the Infrastructure Manager API API](https://console.cloud.google.com/flows/enableapi?apiid=config.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/config
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.create_deployment.js)  
create deployment group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.create_deployment_group.js)  
create preview | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.create_preview.js)  
delete deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.delete_deployment.js)  
delete deployment group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.delete_deployment_group.js)  
delete preview | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.delete_preview.js)  
delete statefile | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.delete_statefile.js)  
deprovision deployment group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.deprovision_deployment_group.js)  
export deployment statefile | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.export_deployment_statefile.js)  
export lock info | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.export_lock_info.js)  
export preview result | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.export_preview_result.js)  
export revision statefile | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.export_revision_statefile.js)  
get auto migration config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.get_auto_migration_config.js)  
get deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.get_deployment.js)  
get deployment group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.get_deployment_group.js)  
get deployment group revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.get_deployment_group_revision.js)  
get preview | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.get_preview.js)  
get resource | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.get_resource.js)  
get resource change | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.get_resource_change.js)  
get resource drift | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.get_resource_drift.js)  
get revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.get_revision.js)  
get terraform version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.get_terraform_version.js)  
import statefile | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.import_statefile.js)  
list deployment group revisions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.list_deployment_group_revisions.js)  
list deployment groups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.list_deployment_groups.js)  
list deployments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.list_deployments.js)  
list previews | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.list_previews.js)  
list resource changes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.list_resource_changes.js)  
list resource drifts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.list_resource_drifts.js)  
list resources | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.list_resources.js)  
list revisions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.list_revisions.js)  
list terraform versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.list_terraform_versions.js)  
lock deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.lock_deployment.js)  
provision deployment group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.provision_deployment_group.js)  
unlock deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.unlock_deployment.js)  
update auto migration config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.update_auto_migration_config.js)  
update deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.update_deployment.js)  
update deployment group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-config/samples/generated/v1/config.update_deployment_group.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/config@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
