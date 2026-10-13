---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/
title: Cloud Dataproc API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:41.067162+00:00
---

# Cloud Dataproc API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Dataproc API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/dataproc.svg)](https://www.npmjs.org/package/@google-cloud/dataproc)

Cloud Dataproc API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/CHANGELOG.md).

  * [Cloud Dataproc API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/dataproc/latest)



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
  3. [Enable the Cloud Dataproc API API](https://console.cloud.google.com/flows/enableapi?apiid=dataproc.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/dataproc
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create autoscaling policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/autoscaling_policy_service.create_autoscaling_policy.js)  
delete autoscaling policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/autoscaling_policy_service.delete_autoscaling_policy.js)  
get autoscaling policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/autoscaling_policy_service.get_autoscaling_policy.js)  
list autoscaling policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/autoscaling_policy_service.list_autoscaling_policies.js)  
update autoscaling policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/autoscaling_policy_service.update_autoscaling_policy.js)  
create batch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/batch_controller.create_batch.js)  
delete batch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/batch_controller.delete_batch.js)  
get batch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/batch_controller.get_batch.js)  
list batches | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/batch_controller.list_batches.js)  
create cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/cluster_controller.create_cluster.js)  
delete cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/cluster_controller.delete_cluster.js)  
diagnose cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/cluster_controller.diagnose_cluster.js)  
get cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/cluster_controller.get_cluster.js)  
list clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/cluster_controller.list_clusters.js)  
start cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/cluster_controller.start_cluster.js)  
stop cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/cluster_controller.stop_cluster.js)  
update cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/cluster_controller.update_cluster.js)  
cancel job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/job_controller.cancel_job.js)  
delete job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/job_controller.delete_job.js)  
get job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/job_controller.get_job.js)  
list jobs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/job_controller.list_jobs.js)  
submit job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/job_controller.submit_job.js)  
submit job as operation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/job_controller.submit_job_as_operation.js)  
update job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/job_controller.update_job.js)  
create node group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/node_group_controller.create_node_group.js)  
get node group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/node_group_controller.get_node_group.js)  
resize node group | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/node_group_controller.resize_node_group.js)  
create session | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/session_controller.create_session.js)  
delete session | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/session_controller.delete_session.js)  
get session | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/session_controller.get_session.js)  
list sessions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/session_controller.list_sessions.js)  
terminate session | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/session_controller.terminate_session.js)  
create session template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/session_template_controller.create_session_template.js)  
delete session template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/session_template_controller.delete_session_template.js)  
get session template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/session_template_controller.get_session_template.js)  
list session templates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/session_template_controller.list_session_templates.js)  
update session template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/session_template_controller.update_session_template.js)  
create workflow template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/workflow_template_service.create_workflow_template.js)  
delete workflow template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/workflow_template_service.delete_workflow_template.js)  
get workflow template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/workflow_template_service.get_workflow_template.js)  
instantiate inline workflow template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/workflow_template_service.instantiate_inline_workflow_template.js)  
instantiate workflow template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/workflow_template_service.instantiate_workflow_template.js)  
list workflow templates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/workflow_template_service.list_workflow_templates.js)  
update workflow template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataproc/samples/generated/v1/workflow_template_service.update_workflow_template.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/dataproc@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
