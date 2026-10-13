---
url: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/
title: Kubernetes Engine API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:35.429018+00:00
---

# Kubernetes Engine API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Kubernetes Engine API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.1.0  6.8.0  6.7.0  6.1.0  5.19.0  5.17.0  5.15.1  5.14.0  5.10.0  5.9.0  5.8.0  5.6.0  5.5.0  5.4.1  5.1.0  4.11.0  4.10.0  4.9.0  4.7.1  4.4.0  4.3.0  4.2.0  4.1.3  3.0.0  2.6.0  2.5.0  2.4.4  2.3.2 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/container.svg)](https://www.npmjs.org/package/@google-cloud/container)

Kubernetes Engine API client for Node.js

> Node.js idiomatic client for [Kubernetes Engine][product-docs] cluster management.

[Kubernetes Engine](https://cloud.google.com/kubernetes-engine/docs/) is used for building and managing container based applications, powered by the open source Kubernetes technology.

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/CHANGELOG.md).

  * [Kubernetes Engine API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/container/latest)



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
  3. [Enable the Kubernetes Engine API API](https://console.cloud.google.com/flows/enableapi?apiid=container.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/container
    

## Relationship to Kubernetes

`@google-cloud/container` provides a high level API for creating and managing [Google Kubernetes Engine](https://cloud.google.com/gke) clusters on Google Cloud.

To run commands against the clusters created, you will need to use the [Kubernetes API](https://kubernetes.io/docs/reference/using-api/api-overview/) (and the associated kubectl command-line interface).

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
cancel operation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.cancel_operation.js)  
check autopilot compatibility | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.check_autopilot_compatibility.js)  
complete i p rotation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.complete_i_p_rotation.js)  
complete node pool upgrade | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.complete_node_pool_upgrade.js)  
create cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.create_cluster.js)  
create node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.create_node_pool.js)  
delete cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.delete_cluster.js)  
delete node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.delete_node_pool.js)  
fetch cluster upgrade info | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.fetch_cluster_upgrade_info.js)  
fetch node pool upgrade info | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.fetch_node_pool_upgrade_info.js)  
get cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.get_cluster.js)  
get j s o n web keys | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.get_j_s_o_n_web_keys.js)  
get node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.get_node_pool.js)  
get operation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.get_operation.js)  
get server config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.get_server_config.js)  
list clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.list_clusters.js)  
list node pools | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.list_node_pools.js)  
list operations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.list_operations.js)  
list usable subnetworks | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.list_usable_subnetworks.js)  
rollback node pool upgrade | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.rollback_node_pool_upgrade.js)  
set addons config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.set_addons_config.js)  
set labels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.set_labels.js)  
set legacy abac | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.set_legacy_abac.js)  
set locations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.set_locations.js)  
set logging service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.set_logging_service.js)  
set maintenance policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.set_maintenance_policy.js)  
set master auth | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.set_master_auth.js)  
set monitoring service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.set_monitoring_service.js)  
set network policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.set_network_policy.js)  
set node pool autoscaling | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.set_node_pool_autoscaling.js)  
set node pool management | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.set_node_pool_management.js)  
set node pool size | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.set_node_pool_size.js)  
start i p rotation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.start_i_p_rotation.js)  
update cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.update_cluster.js)  
update master | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.update_master.js)  
update node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1/cluster_manager.update_node_pool.js)  
cancel operation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.cancel_operation.js)  
check autopilot compatibility | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.check_autopilot_compatibility.js)  
complete control plane upgrade | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.complete_control_plane_upgrade.js)  
complete i p rotation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.complete_i_p_rotation.js)  
complete node pool upgrade | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.complete_node_pool_upgrade.js)  
create cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.create_cluster.js)  
create node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.create_node_pool.js)  
delete cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.delete_cluster.js)  
delete node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.delete_node_pool.js)  
fetch cluster upgrade info | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.fetch_cluster_upgrade_info.js)  
fetch node pool upgrade info | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.fetch_node_pool_upgrade_info.js)  
get cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.get_cluster.js)  
get j s o n web keys | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.get_j_s_o_n_web_keys.js)  
get node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.get_node_pool.js)  
get operation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.get_operation.js)  
get server config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.get_server_config.js)  
list clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.list_clusters.js)  
list locations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.list_locations.js)  
list node pools | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.list_node_pools.js)  
list operations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.list_operations.js)  
list usable subnetworks | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.list_usable_subnetworks.js)  
rollback node pool upgrade | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.rollback_node_pool_upgrade.js)  
set addons config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.set_addons_config.js)  
set labels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.set_labels.js)  
set legacy abac | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.set_legacy_abac.js)  
set locations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.set_locations.js)  
set logging service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.set_logging_service.js)  
set maintenance policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.set_maintenance_policy.js)  
set master auth | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.set_master_auth.js)  
set monitoring service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.set_monitoring_service.js)  
set network policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.set_network_policy.js)  
set node pool autoscaling | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.set_node_pool_autoscaling.js)  
set node pool management | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.set_node_pool_management.js)  
set node pool size | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.set_node_pool_size.js)  
start i p rotation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.start_i_p_rotation.js)  
update cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.update_cluster.js)  
update master | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.update_master.js)  
update node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-container/samples/generated/v1beta1/cluster_manager.update_node_pool.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/container@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
