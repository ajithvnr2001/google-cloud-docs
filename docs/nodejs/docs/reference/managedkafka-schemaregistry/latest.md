---
url: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/
title: Managed Service for Apache Kafka API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:55.308127+00:00
---

# Managed Service for Apache Kafka API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/managedkafka-schemaregistry.svg)](https://www.npmjs.org/package/@google-cloud/managedkafka-schemaregistry)

Managed Service for Apache Kafka API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/CHANGELOG.md).

  * [Managed Service for Apache Kafka API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/schemaregistry/latest)
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


    
    
    npm install @google-cloud/managedkafka-schemaregistry
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
check compatibility | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.check_compatibility.js)  
create schema registry | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.create_schema_registry.js)  
create version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.create_version.js)  
delete schema config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.delete_schema_config.js)  
delete schema mode | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.delete_schema_mode.js)  
delete schema registry | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.delete_schema_registry.js)  
delete subject | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.delete_subject.js)  
delete version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.delete_version.js)  
get context | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.get_context.js)  
get raw schema | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.get_raw_schema.js)  
get raw schema version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.get_raw_schema_version.js)  
get schema | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.get_schema.js)  
get schema config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.get_schema_config.js)  
get schema mode | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.get_schema_mode.js)  
get schema registry | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.get_schema_registry.js)  
get version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.get_version.js)  
list contexts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.list_contexts.js)  
list referenced schemas | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.list_referenced_schemas.js)  
list schema registries | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.list_schema_registries.js)  
list schema types | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.list_schema_types.js)  
list schema versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.list_schema_versions.js)  
list subjects | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.list_subjects.js)  
list subjects by schema id | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.list_subjects_by_schema_id.js)  
list versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.list_versions.js)  
lookup version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.lookup_version.js)  
update schema config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.update_schema_config.js)  
update schema mode | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-managedkafka-schemaregistry/samples/generated/v1/managed_schema_registry.update_schema_mode.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/managedkafka-schemaregistry@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
