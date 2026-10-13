---
url: https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/
title: Identity and Access Management (IAM) API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:11.633232+00:00
---

# Identity and Access Management (IAM) API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.2.0  0.3.2  0.2.2 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/iam.svg)](https://www.npmjs.org/package/@google-cloud/iam)

Identity and Access Management (IAM) API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/CHANGELOG.md).

  * [Identity and Access Management (IAM) API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/iam/latest)



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
  3. [Enable the Identity and Access Management (IAM) API API](https://console.cloud.google.com/flows/enableapi?apiid=iam.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/iam
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create workload identity pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v1beta/workload_identity_pools.create_workload_identity_pool.js)  
create workload identity pool provider | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v1beta/workload_identity_pools.create_workload_identity_pool_provider.js)  
delete workload identity pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v1beta/workload_identity_pools.delete_workload_identity_pool.js)  
delete workload identity pool provider | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v1beta/workload_identity_pools.delete_workload_identity_pool_provider.js)  
get workload identity pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v1beta/workload_identity_pools.get_workload_identity_pool.js)  
get workload identity pool provider | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v1beta/workload_identity_pools.get_workload_identity_pool_provider.js)  
list workload identity pool providers | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v1beta/workload_identity_pools.list_workload_identity_pool_providers.js)  
list workload identity pools | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v1beta/workload_identity_pools.list_workload_identity_pools.js)  
undelete workload identity pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v1beta/workload_identity_pools.undelete_workload_identity_pool.js)  
undelete workload identity pool provider | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v1beta/workload_identity_pools.undelete_workload_identity_pool_provider.js)  
update workload identity pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v1beta/workload_identity_pools.update_workload_identity_pool.js)  
update workload identity pool provider | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v1beta/workload_identity_pools.update_workload_identity_pool_provider.js)  
create policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v2/policies.create_policy.js)  
delete policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v2/policies.delete_policy.js)  
get policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v2/policies.get_policy.js)  
list policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v2/policies.list_policies.js)  
update policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v2/policies.update_policy.js)  
create policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v2beta/policies.create_policy.js)  
delete policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v2beta/policies.delete_policy.js)  
get policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v2beta/policies.get_policy.js)  
list policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v2beta/policies.list_policies.js)  
update policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v2beta/policies.update_policy.js)  
create policy binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3/policy_bindings.create_policy_binding.js)  
delete policy binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3/policy_bindings.delete_policy_binding.js)  
get policy binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3/policy_bindings.get_policy_binding.js)  
list policy bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3/policy_bindings.list_policy_bindings.js)  
search target policy bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3/policy_bindings.search_target_policy_bindings.js)  
update policy binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3/policy_bindings.update_policy_binding.js)  
create principal access boundary policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3/principal_access_boundary_policies.create_principal_access_boundary_policy.js)  
delete principal access boundary policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3/principal_access_boundary_policies.delete_principal_access_boundary_policy.js)  
get principal access boundary policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3/principal_access_boundary_policies.get_principal_access_boundary_policy.js)  
list principal access boundary policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3/principal_access_boundary_policies.list_principal_access_boundary_policies.js)  
search principal access boundary policy bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3/principal_access_boundary_policies.search_principal_access_boundary_policy_bindings.js)  
update principal access boundary policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3/principal_access_boundary_policies.update_principal_access_boundary_policy.js)  
create access policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/access_policies.create_access_policy.js)  
delete access policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/access_policies.delete_access_policy.js)  
get access policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/access_policies.get_access_policy.js)  
list access policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/access_policies.list_access_policies.js)  
search access policy bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/access_policies.search_access_policy_bindings.js)  
update access policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/access_policies.update_access_policy.js)  
create policy binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/policy_bindings.create_policy_binding.js)  
delete policy binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/policy_bindings.delete_policy_binding.js)  
get policy binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/policy_bindings.get_policy_binding.js)  
list policy bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/policy_bindings.list_policy_bindings.js)  
search target policy bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/policy_bindings.search_target_policy_bindings.js)  
update policy binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/policy_bindings.update_policy_binding.js)  
create principal access boundary policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/principal_access_boundary_policies.create_principal_access_boundary_policy.js)  
delete principal access boundary policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/principal_access_boundary_policies.delete_principal_access_boundary_policy.js)  
get principal access boundary policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/principal_access_boundary_policies.get_principal_access_boundary_policy.js)  
list principal access boundary policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/principal_access_boundary_policies.list_principal_access_boundary_policies.js)  
search principal access boundary policy bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/principal_access_boundary_policies.search_principal_access_boundary_policy_bindings.js)  
update principal access boundary policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-iam/samples/generated/v3beta/principal_access_boundary_policies.update_principal_access_boundary_policy.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/iam@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
