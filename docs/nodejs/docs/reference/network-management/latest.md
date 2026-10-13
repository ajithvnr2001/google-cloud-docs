---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/
title: Network Management API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:19.346207+00:00
---

# Network Management API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Network Management API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.2.0  4.2.0  3.11.0  3.10.0  3.9.0  3.7.0  3.3.0  3.0.0  2.4.2  2.3.1  2.2.0  1.1.2  1.0.2 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/network-management.svg)](https://www.npmjs.org/package/@google-cloud/network-management)

Network Management API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/CHANGELOG.md).

  * [Network Management API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/networkmanagement/latest)



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
  3. [Enable the Network Management API API](https://console.cloud.google.com/flows/enableapi?apiid=networkmanagement.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/network-management
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/organization_vpc_flow_logs_service.create_vpc_flow_logs_config.js)  
delete vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/organization_vpc_flow_logs_service.delete_vpc_flow_logs_config.js)  
get vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/organization_vpc_flow_logs_service.get_vpc_flow_logs_config.js)  
list vpc flow logs configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/organization_vpc_flow_logs_service.list_vpc_flow_logs_configs.js)  
update vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/organization_vpc_flow_logs_service.update_vpc_flow_logs_config.js)  
create connectivity test | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/reachability_service.create_connectivity_test.js)  
delete connectivity test | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/reachability_service.delete_connectivity_test.js)  
get connectivity test | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/reachability_service.get_connectivity_test.js)  
list connectivity tests | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/reachability_service.list_connectivity_tests.js)  
rerun connectivity test | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/reachability_service.rerun_connectivity_test.js)  
update connectivity test | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/reachability_service.update_connectivity_test.js)  
create vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/vpc_flow_logs_service.create_vpc_flow_logs_config.js)  
delete vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/vpc_flow_logs_service.delete_vpc_flow_logs_config.js)  
get vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/vpc_flow_logs_service.get_vpc_flow_logs_config.js)  
list vpc flow logs configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/vpc_flow_logs_service.list_vpc_flow_logs_configs.js)  
query org vpc flow logs configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/vpc_flow_logs_service.query_org_vpc_flow_logs_configs.js)  
show effective flow logs configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/vpc_flow_logs_service.show_effective_flow_logs_configs.js)  
update vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1/vpc_flow_logs_service.update_vpc_flow_logs_config.js)  
create vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/organization_vpc_flow_logs_service.create_vpc_flow_logs_config.js)  
delete vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/organization_vpc_flow_logs_service.delete_vpc_flow_logs_config.js)  
get vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/organization_vpc_flow_logs_service.get_vpc_flow_logs_config.js)  
list vpc flow logs configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/organization_vpc_flow_logs_service.list_vpc_flow_logs_configs.js)  
update vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/organization_vpc_flow_logs_service.update_vpc_flow_logs_config.js)  
create connectivity test | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/reachability_service.create_connectivity_test.js)  
delete connectivity test | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/reachability_service.delete_connectivity_test.js)  
get connectivity test | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/reachability_service.get_connectivity_test.js)  
list connectivity tests | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/reachability_service.list_connectivity_tests.js)  
rerun connectivity test | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/reachability_service.rerun_connectivity_test.js)  
update connectivity test | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/reachability_service.update_connectivity_test.js)  
create vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/vpc_flow_logs_service.create_vpc_flow_logs_config.js)  
delete vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/vpc_flow_logs_service.delete_vpc_flow_logs_config.js)  
get vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/vpc_flow_logs_service.get_vpc_flow_logs_config.js)  
list vpc flow logs configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/vpc_flow_logs_service.list_vpc_flow_logs_configs.js)  
query org vpc flow logs configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/vpc_flow_logs_service.query_org_vpc_flow_logs_configs.js)  
show effective flow logs configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/vpc_flow_logs_service.show_effective_flow_logs_configs.js)  
update vpc flow logs config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-networkmanagement/samples/generated/v1beta1/vpc_flow_logs_service.update_vpc_flow_logs_config.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/network-management@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
