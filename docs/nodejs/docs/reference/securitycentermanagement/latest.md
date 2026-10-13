---
url: https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/
title: Security Command Center Management API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:13.409018+00:00
---

# Security Command Center Management API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Security Command Center Management API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.4.0  0.3.0  0.1.0 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/securitycentermanagement.svg)](https://www.npmjs.org/package/@google-cloud/securitycentermanagement)

Security Command Center Management API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/CHANGELOG.md).

  * [Security Command Center Management API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest)
  * [Security Command Center Management API Documentation](https://cloud.google.com/security-command-center/docs/reference/security-center-management/rest)



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
  3. [Enable the Security Command Center Management API API](https://console.cloud.google.com/flows/enableapi?apiid=securitycentermanagement.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/securitycentermanagement
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create event threat detection custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.create_event_threat_detection_custom_module.js)  
create security health analytics custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.create_security_health_analytics_custom_module.js)  
delete event threat detection custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.delete_event_threat_detection_custom_module.js)  
delete security health analytics custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.delete_security_health_analytics_custom_module.js)  
get effective event threat detection custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.get_effective_event_threat_detection_custom_module.js)  
get effective security health analytics custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.get_effective_security_health_analytics_custom_module.js)  
get event threat detection custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.get_event_threat_detection_custom_module.js)  
get security center service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.get_security_center_service.js)  
get security health analytics custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.get_security_health_analytics_custom_module.js)  
list descendant event threat detection custom modules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.list_descendant_event_threat_detection_custom_modules.js)  
list descendant security health analytics custom modules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.list_descendant_security_health_analytics_custom_modules.js)  
list effective event threat detection custom modules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.list_effective_event_threat_detection_custom_modules.js)  
list effective security health analytics custom modules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.list_effective_security_health_analytics_custom_modules.js)  
list event threat detection custom modules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.list_event_threat_detection_custom_modules.js)  
list security center services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.list_security_center_services.js)  
list security health analytics custom modules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.list_security_health_analytics_custom_modules.js)  
simulate security health analytics custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.simulate_security_health_analytics_custom_module.js)  
update event threat detection custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.update_event_threat_detection_custom_module.js)  
update security center service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.update_security_center_service.js)  
update security health analytics custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.update_security_health_analytics_custom_module.js)  
validate event threat detection custom module | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-securitycentermanagement/samples/generated/v1/security_center_management.validate_event_threat_detection_custom_module.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/securitycentermanagement@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
