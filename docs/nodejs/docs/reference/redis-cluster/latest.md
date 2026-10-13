---
url: https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/
title: Google Cloud Memorystore for Redis API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:11.117819+00:00
---

# Google Cloud Memorystore for Redis API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.0  0.12.0  0.11.0  0.8.0  0.7.1  0.6.0  0.5.0  0.1.0 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/redis-cluster.svg)](https://www.npmjs.org/package/@google-cloud/redis-cluster)

Google Cloud Memorystore for Redis API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/CHANGELOG.md).

  * [Google Cloud Memorystore for Redis API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/cluster/latest)
  * [Google Cloud Memorystore for Redis API Documentation](https://cloud.google.com/memorystore/docs/redis)



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
  3. [Enable the Google Cloud Memorystore for Redis API API](https://console.cloud.google.com/flows/enableapi?apiid=redis.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/redis-cluster
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
backup cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.backup_cluster.js)  
create cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.create_cluster.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.delete_backup.js)  
delete cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.delete_cluster.js)  
export backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.export_backup.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.get_backup.js)  
get backup collection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.get_backup_collection.js)  
get cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.get_cluster.js)  
get cluster certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.get_cluster_certificate_authority.js)  
get shared regional certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.get_shared_regional_certificate_authority.js)  
list backup collections | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.list_backup_collections.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.list_backups.js)  
list clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.list_clusters.js)  
reschedule cluster maintenance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.reschedule_cluster_maintenance.js)  
update cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1/cloud_redis_cluster.update_cluster.js)  
backup cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.backup_cluster.js)  
create cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.create_cluster.js)  
delete backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.delete_backup.js)  
delete cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.delete_cluster.js)  
export backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.export_backup.js)  
get backup | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.get_backup.js)  
get backup collection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.get_backup_collection.js)  
get cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.get_cluster.js)  
get cluster certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.get_cluster_certificate_authority.js)  
get shared regional certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.get_shared_regional_certificate_authority.js)  
list backup collections | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.list_backup_collections.js)  
list backups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.list_backups.js)  
list clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.list_clusters.js)  
reschedule cluster maintenance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.reschedule_cluster_maintenance.js)  
update cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-redis-cluster/samples/generated/v1beta1/cloud_redis_cluster.update_cluster.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/redis-cluster@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
