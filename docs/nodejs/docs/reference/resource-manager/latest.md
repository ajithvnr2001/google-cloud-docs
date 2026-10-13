---
url: https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/
title: Cloud Resource Manager API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:11.299931+00:00
---

# Cloud Resource Manager API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Resource Manager API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.3.0  6.1.0  4.3.0  4.2.1  4.1.3  3.2.0  3.1.0  3.0.0  2.0.1 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/resource-manager.svg)](https://www.npmjs.org/package/@google-cloud/resource-manager)

Cloud Resource Manager API client for Node.js

> Node.js idiomatic client for [Cloud Resource Manager API][product-docs].

Google Cloud Platform provides container resources such as Organizations and Projects, that allow you to group and hierarchically organize other Cloud Platform resources. This hierarchical organization lets you easily manage common aspects of your resources such as access control and configuration settings. The [Cloud Resource Manager API](https://cloud.google.com/resource-manager/docs/) enables you to programmatically manage these container resources.

### **_IMPORTANT NOTE_**

**Version 2.0.0 renames`@google-cloud/resource` to `@google-cloud/resource-manager` on npm.**

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/CHANGELOG.md).

  * [Cloud Resource Manager API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/resourcemanager/latest)



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
  3. [Enable the Cloud Resource Manager API API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/resource-manager
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/folders.create_folder.js)  
delete folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/folders.delete_folder.js)  
get folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/folders.get_folder.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/folders.get_iam_policy.js)  
list folders | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/folders.list_folders.js)  
move folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/folders.move_folder.js)  
search folders | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/folders.search_folders.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/folders.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/folders.test_iam_permissions.js)  
undelete folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/folders.undelete_folder.js)  
update folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/folders.update_folder.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/organizations.get_iam_policy.js)  
get organization | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/organizations.get_organization.js)  
search organizations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/organizations.search_organizations.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/organizations.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/organizations.test_iam_permissions.js)  
create project | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/projects.create_project.js)  
delete project | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/projects.delete_project.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/projects.get_iam_policy.js)  
get project | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/projects.get_project.js)  
list projects | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/projects.list_projects.js)  
move project | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/projects.move_project.js)  
search projects | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/projects.search_projects.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/projects.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/projects.test_iam_permissions.js)  
undelete project | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/projects.undelete_project.js)  
update project | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/projects.update_project.js)  
create tag binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_bindings.create_tag_binding.js)  
delete tag binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_bindings.delete_tag_binding.js)  
list effective tags | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_bindings.list_effective_tags.js)  
list tag bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_bindings.list_tag_bindings.js)  
create tag hold | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_holds.create_tag_hold.js)  
delete tag hold | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_holds.delete_tag_hold.js)  
list tag holds | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_holds.list_tag_holds.js)  
create tag key | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_keys.create_tag_key.js)  
delete tag key | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_keys.delete_tag_key.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_keys.get_iam_policy.js)  
get namespaced tag key | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_keys.get_namespaced_tag_key.js)  
get tag key | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_keys.get_tag_key.js)  
list tag keys | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_keys.list_tag_keys.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_keys.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_keys.test_iam_permissions.js)  
update tag key | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_keys.update_tag_key.js)  
create tag value | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_values.create_tag_value.js)  
delete tag value | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_values.delete_tag_value.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_values.get_iam_policy.js)  
get namespaced tag value | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_values.get_namespaced_tag_value.js)  
get tag value | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_values.get_tag_value.js)  
list tag values | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_values.list_tag_values.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_values.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_values.test_iam_permissions.js)  
update tag value | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-resourcemanager/samples/generated/v3/tag_values.update_tag_value.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/resource-manager@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
