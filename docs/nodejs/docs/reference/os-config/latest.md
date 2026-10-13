---
url: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/
title: OS Config API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:21.360900+00:00
---

# OS Config API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  OS Config API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  2.2.2  2.1.2  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.6 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/os-config.svg)](https://www.npmjs.org/package/@google-cloud/os-config)

OS Config API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/CHANGELOG.md).

  * [OS Config API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/osconfig/latest)



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
  3. [Enable the OS Config API API](https://console.cloud.google.com/flows/enableapi?apiid=osconfig.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/os-config
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
cancel patch job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_service.cancel_patch_job.js)  
create patch deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_service.create_patch_deployment.js)  
delete patch deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_service.delete_patch_deployment.js)  
execute patch job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_service.execute_patch_job.js)  
get patch deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_service.get_patch_deployment.js)  
get patch job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_service.get_patch_job.js)  
list patch deployments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_service.list_patch_deployments.js)  
list patch job instance details | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_service.list_patch_job_instance_details.js)  
list patch jobs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_service.list_patch_jobs.js)  
pause patch deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_service.pause_patch_deployment.js)  
resume patch deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_service.resume_patch_deployment.js)  
update patch deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_service.update_patch_deployment.js)  
create o s policy assignment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_zonal_service.create_o_s_policy_assignment.js)  
delete o s policy assignment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_zonal_service.delete_o_s_policy_assignment.js)  
get inventory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_zonal_service.get_inventory.js)  
get o s policy assignment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_zonal_service.get_o_s_policy_assignment.js)  
get o s policy assignment report | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_zonal_service.get_o_s_policy_assignment_report.js)  
get vulnerability report | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_zonal_service.get_vulnerability_report.js)  
list inventories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_zonal_service.list_inventories.js)  
list o s policy assignment reports | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_zonal_service.list_o_s_policy_assignment_reports.js)  
list o s policy assignment revisions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_zonal_service.list_o_s_policy_assignment_revisions.js)  
list o s policy assignments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_zonal_service.list_o_s_policy_assignments.js)  
list vulnerability reports | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_zonal_service.list_vulnerability_reports.js)  
update o s policy assignment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1/os_config_zonal_service.update_o_s_policy_assignment.js)  
create o s policy assignment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.create_o_s_policy_assignment.js)  
delete o s policy assignment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.delete_o_s_policy_assignment.js)  
get instance o s policies compliance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.get_instance_o_s_policies_compliance.js)  
get inventory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.get_inventory.js)  
get o s policy assignment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.get_o_s_policy_assignment.js)  
get o s policy assignment report | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.get_o_s_policy_assignment_report.js)  
get vulnerability report | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.get_vulnerability_report.js)  
list instance o s policies compliances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.list_instance_o_s_policies_compliances.js)  
list inventories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.list_inventories.js)  
list o s policy assignment reports | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.list_o_s_policy_assignment_reports.js)  
list o s policy assignment revisions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.list_o_s_policy_assignment_revisions.js)  
list o s policy assignments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.list_o_s_policy_assignments.js)  
list vulnerability reports | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.list_vulnerability_reports.js)  
update o s policy assignment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1alpha/os_config_zonal_service.update_o_s_policy_assignment.js)  
cancel patch job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.cancel_patch_job.js)  
create guest policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.create_guest_policy.js)  
create patch deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.create_patch_deployment.js)  
delete guest policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.delete_guest_policy.js)  
delete patch deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.delete_patch_deployment.js)  
execute patch job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.execute_patch_job.js)  
get guest policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.get_guest_policy.js)  
get patch deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.get_patch_deployment.js)  
get patch job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.get_patch_job.js)  
list guest policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.list_guest_policies.js)  
list patch deployments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.list_patch_deployments.js)  
list patch job instance details | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.list_patch_job_instance_details.js)  
list patch jobs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.list_patch_jobs.js)  
lookup effective guest policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.lookup_effective_guest_policy.js)  
pause patch deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.pause_patch_deployment.js)  
resume patch deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.resume_patch_deployment.js)  
update guest policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.update_guest_policy.js)  
update patch deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-osconfig/samples/generated/v1beta/os_config_service.update_patch_deployment.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/os-config@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
