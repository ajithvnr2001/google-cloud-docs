---
url: https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/
title: Notebooks API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:19.580961+00:00
---

# Notebooks API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Notebooks API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  2.1.4  1.3.1  1.2.0  1.1.7 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/notebooks.svg)](https://www.npmjs.org/package/@google-cloud/notebooks)

Notebooks API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/CHANGELOG.md).

  * [Notebooks API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/notebooks/latest)



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
  3. [Enable the Notebooks API API](https://console.cloud.google.com/flows/enableapi?apiid=notebooks.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/notebooks
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create runtime | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.create_runtime.js)  
delete runtime | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.delete_runtime.js)  
diagnose runtime | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.diagnose_runtime.js)  
get runtime | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.get_runtime.js)  
list runtimes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.list_runtimes.js)  
refresh runtime token internal | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.refresh_runtime_token_internal.js)  
report runtime event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.report_runtime_event.js)  
reset runtime | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.reset_runtime.js)  
start runtime | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.start_runtime.js)  
stop runtime | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.stop_runtime.js)  
switch runtime | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.switch_runtime.js)  
update runtime | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.update_runtime.js)  
upgrade runtime | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/managed_notebook_service.upgrade_runtime.js)  
create environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.create_environment.js)  
create execution | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.create_execution.js)  
create instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.create_instance.js)  
create schedule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.create_schedule.js)  
delete environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.delete_environment.js)  
delete execution | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.delete_execution.js)  
delete instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.delete_instance.js)  
delete schedule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.delete_schedule.js)  
diagnose instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.diagnose_instance.js)  
get environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.get_environment.js)  
get execution | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.get_execution.js)  
get instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.get_instance.js)  
get instance health | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.get_instance_health.js)  
get schedule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.get_schedule.js)  
is instance upgradeable | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.is_instance_upgradeable.js)  
list environments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.list_environments.js)  
list executions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.list_executions.js)  
list instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.list_instances.js)  
list schedules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.list_schedules.js)  
register instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.register_instance.js)  
report instance info | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.report_instance_info.js)  
reset instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.reset_instance.js)  
rollback instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.rollback_instance.js)  
set instance accelerator | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.set_instance_accelerator.js)  
set instance labels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.set_instance_labels.js)  
set instance machine type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.set_instance_machine_type.js)  
start instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.start_instance.js)  
stop instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.stop_instance.js)  
trigger schedule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.trigger_schedule.js)  
update instance config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.update_instance_config.js)  
update instance metadata items | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.update_instance_metadata_items.js)  
update shielded instance config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.update_shielded_instance_config.js)  
upgrade instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.upgrade_instance.js)  
upgrade instance internal | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1/notebook_service.upgrade_instance_internal.js)  
create environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.create_environment.js)  
create instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.create_instance.js)  
delete environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.delete_environment.js)  
delete instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.delete_instance.js)  
get environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.get_environment.js)  
get instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.get_instance.js)  
is instance upgradeable | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.is_instance_upgradeable.js)  
list environments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.list_environments.js)  
list instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.list_instances.js)  
register instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.register_instance.js)  
report instance info | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.report_instance_info.js)  
reset instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.reset_instance.js)  
set instance accelerator | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.set_instance_accelerator.js)  
set instance labels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.set_instance_labels.js)  
set instance machine type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.set_instance_machine_type.js)  
start instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.start_instance.js)  
stop instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.stop_instance.js)  
upgrade instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.upgrade_instance.js)  
upgrade instance internal | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v1beta1/notebook_service.upgrade_instance_internal.js)  
check instance upgradability | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v2/notebook_service.check_instance_upgradability.js)  
create instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v2/notebook_service.create_instance.js)  
delete instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v2/notebook_service.delete_instance.js)  
diagnose instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v2/notebook_service.diagnose_instance.js)  
get instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v2/notebook_service.get_instance.js)  
list instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v2/notebook_service.list_instances.js)  
reset instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v2/notebook_service.reset_instance.js)  
rollback instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v2/notebook_service.rollback_instance.js)  
start instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v2/notebook_service.start_instance.js)  
stop instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v2/notebook_service.stop_instance.js)  
update instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v2/notebook_service.update_instance.js)  
upgrade instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-notebooks/samples/generated/v2/notebook_service.upgrade_instance.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/notebooks@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
