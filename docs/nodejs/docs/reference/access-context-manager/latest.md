---
url: https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/
title: Access Context Manager API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:54.145054+00:00
---

# Access Context Manager API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Access Context Manager API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

5.0.1 (latest)  4.1.0  2.3.2  2.2.0  2.1.1  1.0.0  0.2.0 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/access-context-manager.svg)](https://www.npmjs.org/package/@google-cloud/access-context-manager)

Access Context Manager API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/CHANGELOG.md).

  * [Access Context Manager API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/accesscontextmanager/latest)



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
  3. [Enable the Access Context Manager API API](https://console.cloud.google.com/flows/enableapi?apiid=accesscontextmanager.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/access-context-manager
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
commit service perimeters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.commit_service_perimeters.js)  
create access level | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.create_access_level.js)  
create access policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.create_access_policy.js)  
create gcp user access binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.create_gcp_user_access_binding.js)  
create service perimeter | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.create_service_perimeter.js)  
delete access level | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.delete_access_level.js)  
delete access policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.delete_access_policy.js)  
delete gcp user access binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.delete_gcp_user_access_binding.js)  
delete service perimeter | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.delete_service_perimeter.js)  
get access level | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.get_access_level.js)  
get access policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.get_access_policy.js)  
get gcp user access binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.get_gcp_user_access_binding.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.get_iam_policy.js)  
get service perimeter | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.get_service_perimeter.js)  
list access levels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.list_access_levels.js)  
list access policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.list_access_policies.js)  
list gcp user access bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.list_gcp_user_access_bindings.js)  
list service perimeters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.list_service_perimeters.js)  
replace access levels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.replace_access_levels.js)  
replace service perimeters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.replace_service_perimeters.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.test_iam_permissions.js)  
update access level | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.update_access_level.js)  
update access policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.update_access_policy.js)  
update gcp user access binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.update_gcp_user_access_binding.js)  
update service perimeter | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-identity-accesscontextmanager/samples/generated/v1/access_context_manager.update_service_perimeter.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/access-context-manager@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
