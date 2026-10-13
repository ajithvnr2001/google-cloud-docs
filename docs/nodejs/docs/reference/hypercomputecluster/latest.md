---
url: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/
title: Cluster Director API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:12.090907+00:00
---

# Cluster Director API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cluster Director API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.2.0  0.1.0 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/hypercomputecluster.svg)](https://www.npmjs.org/package/@google-cloud/hypercomputecluster)

Cluster Director API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/CHANGELOG.md).

  * [Cluster Director API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest)
  * [Cluster Director API Documentation](https://cloud.google.com/cluster-director/docs)



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
  3. [Enable the Cluster Director API API](https://console.cloud.google.com/flows/enableapi?apiid=hypercomputecluster.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/hypercomputecluster
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1/hypercompute_cluster.create_cluster.js)  
delete cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1/hypercompute_cluster.delete_cluster.js)  
get cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1/hypercompute_cluster.get_cluster.js)  
list clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1/hypercompute_cluster.list_clusters.js)  
update cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1/hypercompute_cluster.update_cluster.js)  
create cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/hypercompute_cluster.create_cluster.js)  
delete cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/hypercompute_cluster.delete_cluster.js)  
get cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/hypercompute_cluster.get_cluster.js)  
get node | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/hypercompute_cluster.get_node.js)  
list clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/hypercompute_cluster.list_clusters.js)  
list nodes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/hypercompute_cluster.list_nodes.js)  
update cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/hypercompute_cluster.update_cluster.js)  
create machine learning run | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.create_machine_learning_run.js)  
create monitored event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.create_monitored_event.js)  
create profiler session | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.create_profiler_session.js)  
create profiler target | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.create_profiler_target.js)  
delete machine learning run | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.delete_machine_learning_run.js)  
delete monitored event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.delete_monitored_event.js)  
delete profiler session | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.delete_profiler_session.js)  
delete profiler target | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.delete_profiler_target.js)  
get machine learning run | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.get_machine_learning_run.js)  
get monitored event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.get_monitored_event.js)  
get profile session | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.get_profile_session.js)  
get profiler session | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.get_profiler_session.js)  
get profiler target | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.get_profiler_target.js)  
list machine learning runs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.list_machine_learning_runs.js)  
list monitored events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.list_monitored_events.js)  
list profile sessions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.list_profile_sessions.js)  
list profiler sessions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.list_profiler_sessions.js)  
list profiler targets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.list_profiler_targets.js)  
update machine learning run | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.update_machine_learning_run.js)  
update monitored event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1alpha/machine_learning_runs.update_monitored_event.js)  
create cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1beta/hypercompute_cluster.create_cluster.js)  
delete cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1beta/hypercompute_cluster.delete_cluster.js)  
get cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1beta/hypercompute_cluster.get_cluster.js)  
list clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1beta/hypercompute_cluster.list_clusters.js)  
update cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-hypercomputecluster/samples/generated/v1beta/hypercompute_cluster.update_cluster.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/hypercomputecluster@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
