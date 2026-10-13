---
url: https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/
title: Apigee Registry API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:57.021399+00:00
---

# Apigee Registry API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Apigee Registry API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

3.0.1 (latest)  1.0.1  0.2.1  0.1.0 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/apigee-registry.svg)](https://www.npmjs.org/package/@google-cloud/apigee-registry)

Apigee Registry API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/CHANGELOG.md).

  * [Apigee Registry API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/apigeeregistry/latest)



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
  3. [Enable the Apigee Registry API API](https://console.cloud.google.com/flows/enableapi?apiid=apigeeregistry.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/apigee-registry
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/provisioning.create_instance.js)  
delete instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/provisioning.delete_instance.js)  
get instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/provisioning.get_instance.js)  
create api | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.create_api.js)  
create api deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.create_api_deployment.js)  
create api spec | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.create_api_spec.js)  
create api version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.create_api_version.js)  
create artifact | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.create_artifact.js)  
delete api | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.delete_api.js)  
delete api deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.delete_api_deployment.js)  
delete api deployment revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.delete_api_deployment_revision.js)  
delete api spec | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.delete_api_spec.js)  
delete api spec revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.delete_api_spec_revision.js)  
delete api version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.delete_api_version.js)  
delete artifact | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.delete_artifact.js)  
get api | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.get_api.js)  
get api deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.get_api_deployment.js)  
get api spec | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.get_api_spec.js)  
get api spec contents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.get_api_spec_contents.js)  
get api version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.get_api_version.js)  
get artifact | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.get_artifact.js)  
get artifact contents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.get_artifact_contents.js)  
list api deployment revisions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.list_api_deployment_revisions.js)  
list api deployments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.list_api_deployments.js)  
list api spec revisions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.list_api_spec_revisions.js)  
list api specs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.list_api_specs.js)  
list api versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.list_api_versions.js)  
list apis | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.list_apis.js)  
list artifacts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.list_artifacts.js)  
replace artifact | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.replace_artifact.js)  
rollback api deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.rollback_api_deployment.js)  
rollback api spec | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.rollback_api_spec.js)  
tag api deployment revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.tag_api_deployment_revision.js)  
tag api spec revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.tag_api_spec_revision.js)  
update api | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.update_api.js)  
update api deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.update_api_deployment.js)  
update api spec | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.update_api_spec.js)  
update api version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-apigeeregistry/samples/generated/v1/registry.update_api_version.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/apigee-registry@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
