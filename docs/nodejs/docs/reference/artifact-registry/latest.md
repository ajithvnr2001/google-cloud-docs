---
url: https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/
title: Artifact Registry API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:01.430158+00:00
---

# Artifact Registry API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Artifact Registry API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.7.0  4.6.0  4.4.0  4.2.0  3.1.1  2.2.2  2.1.0  2.0.2  1.3.0  1.2.3  1.1.0  1.0.7 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/artifact-registry.svg)](https://www.npmjs.org/package/@google-cloud/artifact-registry)

Artifact Registry API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/CHANGELOG.md).

  * [Artifact Registry API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/artifactregistry/latest)



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
  3. [Enable the Artifact Registry API API](https://console.cloud.google.com/flows/enableapi?apiid=artifactregistry.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/artifact-registry
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
batch delete versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.batch_delete_versions.js)  
create attachment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.create_attachment.js)  
create repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.create_repository.js)  
create rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.create_rule.js)  
create tag | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.create_tag.js)  
delete attachment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.delete_attachment.js)  
delete file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.delete_file.js)  
delete package | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.delete_package.js)  
delete repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.delete_repository.js)  
delete rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.delete_rule.js)  
delete tag | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.delete_tag.js)  
delete version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.delete_version.js)  
export artifact | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.export_artifact.js)  
get attachment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_attachment.js)  
get docker image | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_docker_image.js)  
get file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_file.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_iam_policy.js)  
get maven artifact | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_maven_artifact.js)  
get npm package | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_npm_package.js)  
get package | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_package.js)  
get project settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_project_settings.js)  
get python package | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_python_package.js)  
get repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_repository.js)  
get rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_rule.js)  
get tag | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_tag.js)  
get v p c s c config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_v_p_c_s_c_config.js)  
get version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.get_version.js)  
import apt artifacts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.import_apt_artifacts.js)  
import yum artifacts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.import_yum_artifacts.js)  
list attachments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.list_attachments.js)  
list docker images | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.list_docker_images.js)  
list files | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.list_files.js)  
list maven artifacts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.list_maven_artifacts.js)  
list npm packages | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.list_npm_packages.js)  
list packages | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.list_packages.js)  
list python packages | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.list_python_packages.js)  
list repositories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.list_repositories.js)  
list rules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.list_rules.js)  
list tags | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.list_tags.js)  
list versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.list_versions.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.test_iam_permissions.js)  
update file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.update_file.js)  
update package | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.update_package.js)  
update project settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.update_project_settings.js)  
update repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.update_repository.js)  
update rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.update_rule.js)  
update tag | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.update_tag.js)  
update v p c s c config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.update_v_p_c_s_c_config.js)  
update version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1/artifact_registry.update_version.js)  
create repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.create_repository.js)  
create tag | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.create_tag.js)  
delete package | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.delete_package.js)  
delete repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.delete_repository.js)  
delete tag | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.delete_tag.js)  
delete version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.delete_version.js)  
get file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.get_file.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.get_iam_policy.js)  
get package | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.get_package.js)  
get project settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.get_project_settings.js)  
get repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.get_repository.js)  
get tag | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.get_tag.js)  
get version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.get_version.js)  
import apt artifacts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.import_apt_artifacts.js)  
import yum artifacts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.import_yum_artifacts.js)  
list files | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.list_files.js)  
list packages | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.list_packages.js)  
list repositories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.list_repositories.js)  
list tags | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.list_tags.js)  
list versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.list_versions.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.test_iam_permissions.js)  
update project settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.update_project_settings.js)  
update repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.update_repository.js)  
update tag | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-devtools-artifactregistry/samples/generated/v1beta2/artifact_registry.update_tag.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/artifact-registry@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
