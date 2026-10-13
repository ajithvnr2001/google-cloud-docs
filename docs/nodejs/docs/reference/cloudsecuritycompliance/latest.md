---
url: https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/
title: Cloud Security Compliance API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:34.293871+00:00
---

# Cloud Security Compliance API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Security Compliance API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/cloudsecuritycompliance.svg)](https://www.npmjs.org/package/@google-cloud/cloudsecuritycompliance)

Cloud Security Compliance API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/CHANGELOG.md).

  * [Cloud Security Compliance API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest)
  * [Cloud Security Compliance API Documentation](https://cloud.google.com/security-command-center/docs/compliance-manager-overview)



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
  3. [Enable the Cloud Security Compliance API API](https://console.cloud.google.com/flows/enableapi?apiid=cloudsecuritycompliance.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/cloudsecuritycompliance
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create framework audit | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/audit.create_framework_audit.js)  
generate framework audit scope report | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/audit.generate_framework_audit_scope_report.js)  
get framework audit | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/audit.get_framework_audit.js)  
list framework audits | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/audit.list_framework_audits.js)  
calculate effective cm enrollment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/cm_enrollment_service.calculate_effective_cm_enrollment.js)  
update cm enrollment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/cm_enrollment_service.update_cm_enrollment.js)  
create cloud control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/config.create_cloud_control.js)  
create framework | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/config.create_framework.js)  
delete cloud control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/config.delete_cloud_control.js)  
delete framework | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/config.delete_framework.js)  
get cloud control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/config.get_cloud_control.js)  
get framework | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/config.get_framework.js)  
list cloud controls | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/config.list_cloud_controls.js)  
list frameworks | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/config.list_frameworks.js)  
update cloud control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/config.update_cloud_control.js)  
update framework | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/config.update_framework.js)  
create framework deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/deployment.create_framework_deployment.js)  
delete framework deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/deployment.delete_framework_deployment.js)  
get cloud control deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/deployment.get_cloud_control_deployment.js)  
get framework deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/deployment.get_framework_deployment.js)  
list cloud control deployments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/deployment.list_cloud_control_deployments.js)  
list framework deployments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/deployment.list_framework_deployments.js)  
aggregate framework compliance report | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/monitoring.aggregate_framework_compliance_report.js)  
fetch framework compliance report | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/monitoring.fetch_framework_compliance_report.js)  
list control compliance summaries | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/monitoring.list_control_compliance_summaries.js)  
list finding summaries | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/monitoring.list_finding_summaries.js)  
list framework compliance summaries | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-cloudsecuritycompliance/samples/generated/v1/monitoring.list_framework_compliance_summaries.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/cloudsecuritycompliance@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
