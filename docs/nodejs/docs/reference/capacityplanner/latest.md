---
url: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/
title: Capacity Planner API: Node.js Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:28.540571+00:00
---

# Capacity Planner API: Node.js Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Capacity Planner API: Node.js Client Stay organized with collections  Save and categorize content based on your preferences. 

0.4.1 (latest)  0.2.0  0.1.2 

[![release level](https://img.shields.io/badge/release%20level-preview-yellow.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/capacityplanner.svg)](https://www.npmjs.org/package/@google-cloud/capacityplanner)

Capacity Planner API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-capacityplanner/CHANGELOG.md).

  * [Capacity Planner API Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/capacityplanner/latest)
  * [Capacity Planner API Documentation](https://cloud.google.com/capacity-planner/docs)
  * [github.com/googleapis/google-cloud-node/packages/google-cloud-capacityplanner](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-capacityplanner)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart

    * Before you begin
    * Installing the client library
  * Samples

  * Versioning
  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable billing for your project](https://support.google.com/cloud/answer/6293499#enable-billing).
  3. [Enable the Capacity Planner API API](https://console.cloud.google.com/flows/enableapi?apiid=capacityplanner.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation.



### Installing the client library
    
    
    npm install @google-cloud/capacityplanner
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-capacityplanner/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
Capacity_planning_service.get_capacity_plan | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-capacityplanner/samples/generated/v1beta/capacity_planning_service.get_capacity_plan.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-capacityplanner/samples/generated/v1beta/capacity_planning_service.get_capacity_plan.js,packages/google-cloud-capacityplanner/samples/README.md)  
Capacity_planning_service.query_capacity_plan_insights | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-capacityplanner/samples/generated/v1beta/capacity_planning_service.query_capacity_plan_insights.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-capacityplanner/samples/generated/v1beta/capacity_planning_service.query_capacity_plan_insights.js,packages/google-cloud-capacityplanner/samples/README.md)  
Capacity_planning_service.query_capacity_plans | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-capacityplanner/samples/generated/v1beta/capacity_planning_service.query_capacity_plans.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-capacityplanner/samples/generated/v1beta/capacity_planning_service.query_capacity_plans.js,packages/google-cloud-capacityplanner/samples/README.md)  
Usage_service.export_forecasts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-capacityplanner/samples/generated/v1beta/usage_service.export_forecasts.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-capacityplanner/samples/generated/v1beta/usage_service.export_forecasts.js,packages/google-cloud-capacityplanner/samples/README.md)  
Usage_service.export_reservations_usage | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-capacityplanner/samples/generated/v1beta/usage_service.export_reservations_usage.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-capacityplanner/samples/generated/v1beta/usage_service.export_reservations_usage.js,packages/google-cloud-capacityplanner/samples/README.md)  
Usage_service.export_usage_histories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-capacityplanner/samples/generated/v1beta/usage_service.export_usage_histories.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-capacityplanner/samples/generated/v1beta/usage_service.export_usage_histories.js,packages/google-cloud-capacityplanner/samples/README.md)  
Usage_service.query_forecasts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-capacityplanner/samples/generated/v1beta/usage_service.query_forecasts.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-capacityplanner/samples/generated/v1beta/usage_service.query_forecasts.js,packages/google-cloud-capacityplanner/samples/README.md)  
Usage_service.query_reservations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-capacityplanner/samples/generated/v1beta/usage_service.query_reservations.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-capacityplanner/samples/generated/v1beta/usage_service.query_reservations.js,packages/google-cloud-capacityplanner/samples/README.md)  
Usage_service.query_usage_histories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-capacityplanner/samples/generated/v1beta/usage_service.query_usage_histories.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-capacityplanner/samples/generated/v1beta/usage_service.query_usage_histories.js,packages/google-cloud-capacityplanner/samples/README.md)  
  
The [Capacity Planner API Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/capacityplanner/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/capacityplanner@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/google-cloud-node/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/google-cloud-node/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
