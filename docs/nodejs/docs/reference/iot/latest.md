---
url: https://docs.cloud.google.com/nodejs/docs/reference/iot/latest/
title: Cloud IoT API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:13.006528+00:00
---

# Cloud IoT API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/iot/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud IoT API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  6.0.1  5.1.0  4.0.0  3.2.2  3.1.2  2.5.1  2.4.0  2.3.6  2.2.0 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/iot.svg)](https://www.npmjs.org/package/@google-cloud/iot)

Cloud IoT API client for Node.js

> Node.js idiomatic client for [Cloud IoT Core][product-docs].

[Google Cloud Internet of Things (IoT) Core](https://cloud.google.com/iot/docs) is a fully managed service for securely connecting and managing IoT devices, from a few to millions. Ingest data from connected devices and build rich applications that integrate with the other big data services of Google Cloud Platform.

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/CHANGELOG.md).

  * [Cloud IoT API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/iot/latest)



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
  3. [Enable the Cloud IoT API API](https://console.cloud.google.com/flows/enableapi?apiid=cloudiot.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/iot
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
bind device to gateway | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.bind_device_to_gateway.js)  
create device | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.create_device.js)  
create device registry | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.create_device_registry.js)  
delete device | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.delete_device.js)  
delete device registry | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.delete_device_registry.js)  
get device | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.get_device.js)  
get device registry | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.get_device_registry.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.get_iam_policy.js)  
list device config versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.list_device_config_versions.js)  
list device registries | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.list_device_registries.js)  
list device states | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.list_device_states.js)  
list devices | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.list_devices.js)  
modify cloud to device config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.modify_cloud_to_device_config.js)  
send command to device | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.send_command_to_device.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.test_iam_permissions.js)  
unbind device from gateway | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.unbind_device_from_gateway.js)  
update device | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.update_device.js)  
update device registry | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-iot/samples/generated/v1/device_manager.update_device_registry.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/iot@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
