---
url: https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/
title: GKE Hub: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:10.782312+00:00
---

# GKE Hub: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  GKE Hub: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.4.0  6.1.0  6.0.1  5.0.0  4.5.0  4.4.0  4.2.0  3.4.0  3.3.1  3.2.2  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.1  1.1.4 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/gke-hub.svg)](https://www.npmjs.org/package/@google-cloud/gke-hub)

GKE Hub client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/CHANGELOG.md).

  * [GKE Hub Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/gkehub/latest)



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
  3. [Enable the GKE Hub API](https://console.cloud.google.com/flows/enableapi?apiid=gkehub.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/gke-hub
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create feature | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.create_feature.js)  
create fleet | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.create_fleet.js)  
create membership | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.create_membership.js)  
create membership binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.create_membership_binding.js)  
create membership r b a c role binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.create_membership_r_b_a_c_role_binding.js)  
create scope | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.create_scope.js)  
create scope namespace | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.create_scope_namespace.js)  
create scope r b a c role binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.create_scope_r_b_a_c_role_binding.js)  
delete feature | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.delete_feature.js)  
delete fleet | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.delete_fleet.js)  
delete membership | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.delete_membership.js)  
delete membership binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.delete_membership_binding.js)  
delete membership r b a c role binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.delete_membership_r_b_a_c_role_binding.js)  
delete scope | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.delete_scope.js)  
delete scope namespace | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.delete_scope_namespace.js)  
delete scope r b a c role binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.delete_scope_r_b_a_c_role_binding.js)  
generate connect manifest | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.generate_connect_manifest.js)  
generate membership r b a c role binding y a m l | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.generate_membership_r_b_a_c_role_binding_y_a_m_l.js)  
get feature | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.get_feature.js)  
get fleet | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.get_fleet.js)  
get membership | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.get_membership.js)  
get membership binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.get_membership_binding.js)  
get membership r b a c role binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.get_membership_r_b_a_c_role_binding.js)  
get scope | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.get_scope.js)  
get scope namespace | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.get_scope_namespace.js)  
get scope r b a c role binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.get_scope_r_b_a_c_role_binding.js)  
list bound memberships | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.list_bound_memberships.js)  
list features | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.list_features.js)  
list fleets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.list_fleets.js)  
list membership bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.list_membership_bindings.js)  
list membership r b a c role bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.list_membership_r_b_a_c_role_bindings.js)  
list memberships | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.list_memberships.js)  
list permitted scopes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.list_permitted_scopes.js)  
list scope namespaces | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.list_scope_namespaces.js)  
list scope r b a c role bindings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.list_scope_r_b_a_c_role_bindings.js)  
list scopes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.list_scopes.js)  
update feature | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.update_feature.js)  
update fleet | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.update_fleet.js)  
update membership | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.update_membership.js)  
update membership binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.update_membership_binding.js)  
update membership r b a c role binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.update_membership_r_b_a_c_role_binding.js)  
update scope | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.update_scope.js)  
update scope namespace | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.update_scope_namespace.js)  
update scope r b a c role binding | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1/gke_hub.update_scope_r_b_a_c_role_binding.js)  
create feature | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1alpha/gke_hub.create_feature.js)  
delete feature | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1alpha/gke_hub.delete_feature.js)  
get feature | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1alpha/gke_hub.get_feature.js)  
list features | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1alpha/gke_hub.list_features.js)  
update feature | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1alpha/gke_hub.update_feature.js)  
create feature | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta/gke_hub.create_feature.js)  
delete feature | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta/gke_hub.delete_feature.js)  
get feature | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta/gke_hub.get_feature.js)  
list features | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta/gke_hub.list_features.js)  
update feature | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta/gke_hub.update_feature.js)  
create membership | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta1/gke_hub_membership_service.create_membership.js)  
delete membership | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta1/gke_hub_membership_service.delete_membership.js)  
generate connect manifest | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta1/gke_hub_membership_service.generate_connect_manifest.js)  
generate exclusivity manifest | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta1/gke_hub_membership_service.generate_exclusivity_manifest.js)  
get membership | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta1/gke_hub_membership_service.get_membership.js)  
list memberships | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta1/gke_hub_membership_service.list_memberships.js)  
update membership | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta1/gke_hub_membership_service.update_membership.js)  
validate exclusivity | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gkehub/samples/generated/v1beta1/gke_hub_membership_service.validate_exclusivity.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/gke-hub@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
