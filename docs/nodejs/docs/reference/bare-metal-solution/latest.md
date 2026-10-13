---
url: https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/
title: Bare Metal Solution API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:25.659339+00:00
---

# Bare Metal Solution API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Bare Metal Solution API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.1.0  0.3.2  0.2.2 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/bare-metal-solution.svg)](https://www.npmjs.org/package/@google-cloud/bare-metal-solution)

Bare Metal Solution API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/CHANGELOG.md).

  * [Bare Metal Solution API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/baremetalsolution/latest)



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
  3. [Enable the Bare Metal Solution API API](https://console.cloud.google.com/flows/enableapi?apiid=baremetalsolution.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/bare-metal-solution
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create nfs share | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.create_nfs_share.js)  
create provisioning config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.create_provisioning_config.js)  
create s s h key | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.create_s_s_h_key.js)  
create volume snapshot | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.create_volume_snapshot.js)  
delete nfs share | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.delete_nfs_share.js)  
delete s s h key | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.delete_s_s_h_key.js)  
delete volume snapshot | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.delete_volume_snapshot.js)  
detach lun | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.detach_lun.js)  
disable interactive serial console | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.disable_interactive_serial_console.js)  
enable interactive serial console | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.enable_interactive_serial_console.js)  
evict lun | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.evict_lun.js)  
evict volume | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.evict_volume.js)  
get instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.get_instance.js)  
get lun | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.get_lun.js)  
get network | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.get_network.js)  
get nfs share | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.get_nfs_share.js)  
get provisioning config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.get_provisioning_config.js)  
get volume | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.get_volume.js)  
get volume snapshot | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.get_volume_snapshot.js)  
list instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.list_instances.js)  
list luns | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.list_luns.js)  
list network usage | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.list_network_usage.js)  
list networks | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.list_networks.js)  
list nfs shares | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.list_nfs_shares.js)  
list o s images | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.list_o_s_images.js)  
list provisioning quotas | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.list_provisioning_quotas.js)  
list s s h keys | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.list_s_s_h_keys.js)  
list volume snapshots | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.list_volume_snapshots.js)  
list volumes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.list_volumes.js)  
rename instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.rename_instance.js)  
rename network | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.rename_network.js)  
rename nfs share | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.rename_nfs_share.js)  
rename volume | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.rename_volume.js)  
reset instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.reset_instance.js)  
resize volume | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.resize_volume.js)  
restore volume snapshot | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.restore_volume_snapshot.js)  
start instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.start_instance.js)  
stop instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.stop_instance.js)  
submit provisioning config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.submit_provisioning_config.js)  
update instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.update_instance.js)  
update network | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.update_network.js)  
update nfs share | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.update_nfs_share.js)  
update provisioning config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.update_provisioning_config.js)  
update volume | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-baremetalsolution/samples/generated/v2/bare_metal_solution.update_volume.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/bare-metal-solution@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
