---
url: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/
title: Managed Service for Apache Kafka API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:15.597487+00:00
---

# Managed Service for Apache Kafka API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.6.0  0.3.0  0.2.0  0.1.0 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/managedkafka.svg)](https://www.npmjs.org/package/@google-cloud/managedkafka)

Managed Service for Apache Kafka API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/CHANGELOG.md).

  * [Managed Service for Apache Kafka API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/managedkafka/latest)
  * [Managed Service for Apache Kafka API Documentation](https://cloud.google.com/managed-service-for-apache-kafka/docs)



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
  3. [Enable the Managed Service for Apache Kafka API API](https://console.cloud.google.com/flows/enableapi?apiid=managedkafka.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/managedkafka
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
add acl entry | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.add_acl_entry.js)  
create acl | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.create_acl.js)  
create cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.create_cluster.js)  
create topic | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.create_topic.js)  
delete acl | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.delete_acl.js)  
delete cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.delete_cluster.js)  
delete consumer group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.delete_consumer_group.js)  
delete topic | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.delete_topic.js)  
get acl | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.get_acl.js)  
get cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.get_cluster.js)  
get consumer group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.get_consumer_group.js)  
get topic | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.get_topic.js)  
list acls | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.list_acls.js)  
list clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.list_clusters.js)  
list consumer groups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.list_consumer_groups.js)  
list topics | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.list_topics.js)  
remove acl entry | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.remove_acl_entry.js)  
update acl | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.update_acl.js)  
update cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.update_cluster.js)  
update consumer group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.update_consumer_group.js)  
update topic | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka.update_topic.js)  
create connect cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.create_connect_cluster.js)  
create connector | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.create_connector.js)  
delete connect cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.delete_connect_cluster.js)  
delete connector | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.delete_connector.js)  
get connect cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.get_connect_cluster.js)  
get connector | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.get_connector.js)  
list connect clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.list_connect_clusters.js)  
list connectors | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.list_connectors.js)  
pause connector | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.pause_connector.js)  
restart connector | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.restart_connector.js)  
resume connector | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.resume_connector.js)  
stop connector | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.stop_connector.js)  
update connect cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.update_connect_cluster.js)  
update connector | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka/samples/generated/v1/managed_kafka_connect.update_connector.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/managedkafka@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
