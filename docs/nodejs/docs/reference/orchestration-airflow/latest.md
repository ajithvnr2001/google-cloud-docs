---
url: https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/
title: Cloud Composer API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:20.071634+00:00
---

# Cloud Composer API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/orchestration-airflow/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Composer API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.2.0  4.0.1  3.6.0  3.2.0  2.4.0  2.3.2  2.1.2  1.0.0 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/orchestration-airflow.svg)](https://www.npmjs.org/package/@google-cloud/orchestration-airflow)

Cloud Composer API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/CHANGELOG.md).

  * [Cloud Composer API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/service/latest)



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
  3. [Enable the Cloud Composer API API](https://console.cloud.google.com/flows/enableapi?apiid=composer.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/orchestration-airflow
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
check upgrade | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.check_upgrade.js)  
create environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.create_environment.js)  
create user workloads config map | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.create_user_workloads_config_map.js)  
create user workloads secret | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.create_user_workloads_secret.js)  
database failover | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.database_failover.js)  
delete environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.delete_environment.js)  
delete user workloads config map | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.delete_user_workloads_config_map.js)  
delete user workloads secret | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.delete_user_workloads_secret.js)  
execute airflow command | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.execute_airflow_command.js)  
fetch database properties | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.fetch_database_properties.js)  
get environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.get_environment.js)  
get user workloads config map | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.get_user_workloads_config_map.js)  
get user workloads secret | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.get_user_workloads_secret.js)  
list environments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.list_environments.js)  
list user workloads config maps | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.list_user_workloads_config_maps.js)  
list user workloads secrets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.list_user_workloads_secrets.js)  
list workloads | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.list_workloads.js)  
load snapshot | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.load_snapshot.js)  
poll airflow command | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.poll_airflow_command.js)  
save snapshot | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.save_snapshot.js)  
stop airflow command | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.stop_airflow_command.js)  
update environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.update_environment.js)  
update user workloads config map | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.update_user_workloads_config_map.js)  
update user workloads secret | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/environments.update_user_workloads_secret.js)  
list image versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1/image_versions.list_image_versions.js)  
check upgrade | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.check_upgrade.js)  
create environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.create_environment.js)  
create user workloads config map | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.create_user_workloads_config_map.js)  
create user workloads secret | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.create_user_workloads_secret.js)  
database failover | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.database_failover.js)  
delete environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.delete_environment.js)  
delete user workloads config map | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.delete_user_workloads_config_map.js)  
delete user workloads secret | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.delete_user_workloads_secret.js)  
execute airflow command | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.execute_airflow_command.js)  
fetch database properties | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.fetch_database_properties.js)  
get environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.get_environment.js)  
get user workloads config map | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.get_user_workloads_config_map.js)  
get user workloads secret | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.get_user_workloads_secret.js)  
list environments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.list_environments.js)  
list user workloads config maps | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.list_user_workloads_config_maps.js)  
list user workloads secrets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.list_user_workloads_secrets.js)  
list workloads | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.list_workloads.js)  
load snapshot | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.load_snapshot.js)  
poll airflow command | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.poll_airflow_command.js)  
restart web server | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.restart_web_server.js)  
save snapshot | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.save_snapshot.js)  
stop airflow command | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.stop_airflow_command.js)  
update environment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.update_environment.js)  
update user workloads config map | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.update_user_workloads_config_map.js)  
update user workloads secret | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/environments.update_user_workloads_secret.js)  
list image versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-orchestration-airflow-service/samples/generated/v1beta1/image_versions.list_image_versions.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/orchestration-airflow@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
