---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/
title: GKE Multi-Cloud API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:10.937952+00:00
---

# GKE Multi-Cloud API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  GKE Multi-Cloud API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.3.0  2.1.0  2.0.1  1.5.0  1.1.0  0.3.2  0.1.4 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/gkemulticloud.svg)](https://www.npmjs.org/package/@google-cloud/gkemulticloud)

GKE Multi-Cloud API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/CHANGELOG.md).

  * [GKE Multi-Cloud API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/gkemulticloud/latest)
  * [GKE Multi-Cloud API Documentation](https://cloud.google.com/kubernetes-engine/multi-cloud/docs)



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
  3. [Enable the GKE Multi-Cloud API API](https://console.cloud.google.com/flows/enableapi?apiid=gkemulticloud.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/gkemulticloud
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create attached cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/attached_clusters.create_attached_cluster.js)  
delete attached cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/attached_clusters.delete_attached_cluster.js)  
generate attached cluster agent token | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/attached_clusters.generate_attached_cluster_agent_token.js)  
generate attached cluster install manifest | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/attached_clusters.generate_attached_cluster_install_manifest.js)  
get attached cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/attached_clusters.get_attached_cluster.js)  
get attached server config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/attached_clusters.get_attached_server_config.js)  
import attached cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/attached_clusters.import_attached_cluster.js)  
list attached clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/attached_clusters.list_attached_clusters.js)  
update attached cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/attached_clusters.update_attached_cluster.js)  
create aws cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.create_aws_cluster.js)  
create aws node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.create_aws_node_pool.js)  
delete aws cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.delete_aws_cluster.js)  
delete aws node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.delete_aws_node_pool.js)  
generate aws access token | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.generate_aws_access_token.js)  
generate aws cluster agent token | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.generate_aws_cluster_agent_token.js)  
get aws cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.get_aws_cluster.js)  
get aws json web keys | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.get_aws_json_web_keys.js)  
get aws node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.get_aws_node_pool.js)  
get aws open id config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.get_aws_open_id_config.js)  
get aws server config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.get_aws_server_config.js)  
list aws clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.list_aws_clusters.js)  
list aws node pools | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.list_aws_node_pools.js)  
rollback aws node pool update | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.rollback_aws_node_pool_update.js)  
update aws cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.update_aws_cluster.js)  
update aws node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/aws_clusters.update_aws_node_pool.js)  
create azure client | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.create_azure_client.js)  
create azure cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.create_azure_cluster.js)  
create azure node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.create_azure_node_pool.js)  
delete azure client | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.delete_azure_client.js)  
delete azure cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.delete_azure_cluster.js)  
delete azure node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.delete_azure_node_pool.js)  
generate azure access token | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.generate_azure_access_token.js)  
generate azure cluster agent token | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.generate_azure_cluster_agent_token.js)  
get azure client | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.get_azure_client.js)  
get azure cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.get_azure_cluster.js)  
get azure json web keys | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.get_azure_json_web_keys.js)  
get azure node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.get_azure_node_pool.js)  
get azure open id config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.get_azure_open_id_config.js)  
get azure server config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.get_azure_server_config.js)  
list azure clients | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.list_azure_clients.js)  
list azure clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.list_azure_clusters.js)  
list azure node pools | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.list_azure_node_pools.js)  
update azure cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.update_azure_cluster.js)  
update azure node pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkemulticloud/samples/generated/v1/azure_clusters.update_azure_node_pool.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/gkemulticloud@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
