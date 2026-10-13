---
url: https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/
title: GDC Hardware Management API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:47.232797+00:00
---

# GDC Hardware Management API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  GDC Hardware Management API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.12.1 (latest)  0.10.0  0.7.0  0.5.1  0.4.0  0.2.0 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/gdchardwaremanagement.svg)](https://www.npmjs.org/package/@google-cloud/gdchardwaremanagement)

GDC Hardware Management API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/CHANGELOG.md).

  * [GDC Hardware Management API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest)
  * [GDC Hardware Management API Documentation](https://cloud.google.com/distributed-cloud/edge/latest/docs)



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
  3. [Enable the GDC Hardware Management API API](https://console.cloud.google.com/flows/enableapi?apiid=gdchardwaremanagement.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/gdchardwaremanagement
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
cancel order | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.cancel_order.js)  
create comment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.create_comment.js)  
create hardware | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.create_hardware.js)  
create hardware group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.create_hardware_group.js)  
create order | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.create_order.js)  
create site | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.create_site.js)  
create zone | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.create_zone.js)  
delete hardware | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.delete_hardware.js)  
delete hardware group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.delete_hardware_group.js)  
delete order | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.delete_order.js)  
delete site | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.delete_site.js)  
delete zone | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.delete_zone.js)  
get change log entry | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.get_change_log_entry.js)  
get comment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.get_comment.js)  
get hardware | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.get_hardware.js)  
get hardware group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.get_hardware_group.js)  
get order | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.get_order.js)  
get site | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.get_site.js)  
get sku | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.get_sku.js)  
get zone | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.get_zone.js)  
list change log entries | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.list_change_log_entries.js)  
list comments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.list_comments.js)  
list hardware | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.list_hardware.js)  
list hardware groups | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.list_hardware_groups.js)  
list orders | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.list_orders.js)  
list sites | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.list_sites.js)  
list skus | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.list_skus.js)  
list zones | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.list_zones.js)  
record action on comment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.record_action_on_comment.js)  
request order date change | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.request_order_date_change.js)  
signal zone state | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.signal_zone_state.js)  
submit order | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.submit_order.js)  
update hardware | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.update_hardware.js)  
update hardware group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.update_hardware_group.js)  
update order | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.update_order.js)  
update site | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.update_site.js)  
update zone | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gdchardwaremanagement/samples/generated/v1alpha/g_d_c_hardware_management.update_zone.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/gdchardwaremanagement@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
