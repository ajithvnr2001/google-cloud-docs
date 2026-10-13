---
url: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/
title: App Engine Admin API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:00.820484+00:00
---

# App Engine Admin API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  App Engine Admin API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.2.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.6 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/appengine-admin.svg)](https://www.npmjs.org/package/@google-cloud/appengine-admin)

App Engine Admin API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/CHANGELOG.md).

  * [App Engine Admin API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/appengine/latest)



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
  3. [Enable the App Engine Admin API API](https://console.cloud.google.com/flows/enableapi?apiid=appengine.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/appengine-admin
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create application | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/applications.create_application.js)  
get application | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/applications.get_application.js)  
repair application | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/applications.repair_application.js)  
update application | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/applications.update_application.js)  
create authorized certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/authorized_certificates.create_authorized_certificate.js)  
delete authorized certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/authorized_certificates.delete_authorized_certificate.js)  
get authorized certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/authorized_certificates.get_authorized_certificate.js)  
list authorized certificates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/authorized_certificates.list_authorized_certificates.js)  
update authorized certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/authorized_certificates.update_authorized_certificate.js)  
list authorized domains | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/authorized_domains.list_authorized_domains.js)  
create domain mapping | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/domain_mappings.create_domain_mapping.js)  
delete domain mapping | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/domain_mappings.delete_domain_mapping.js)  
get domain mapping | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/domain_mappings.get_domain_mapping.js)  
list domain mappings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/domain_mappings.list_domain_mappings.js)  
update domain mapping | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/domain_mappings.update_domain_mapping.js)  
batch update ingress rules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/firewall.batch_update_ingress_rules.js)  
create ingress rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/firewall.create_ingress_rule.js)  
delete ingress rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/firewall.delete_ingress_rule.js)  
get ingress rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/firewall.get_ingress_rule.js)  
list ingress rules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/firewall.list_ingress_rules.js)  
update ingress rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/firewall.update_ingress_rule.js)  
debug instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/instances.debug_instance.js)  
delete instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/instances.delete_instance.js)  
get instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/instances.get_instance.js)  
list instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/instances.list_instances.js)  
delete service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/services.delete_service.js)  
get service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/services.get_service.js)  
list services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/services.list_services.js)  
update service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/services.update_service.js)  
create version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/versions.create_version.js)  
delete version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/versions.delete_version.js)  
get version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/versions.get_version.js)  
list versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/versions.list_versions.js)  
update version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-appengine/samples/generated/v1/versions.update_version.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/appengine-admin@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
