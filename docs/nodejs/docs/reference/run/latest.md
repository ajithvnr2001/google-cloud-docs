---
url: https://docs.cloud.google.com/nodejs/docs/reference/run/latest/
title: Cloud Run Admin API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:12.519168+00:00
---

# Cloud Run Admin API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/run/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Run Admin API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  3.3.0  3.2.0  2.1.0  1.5.0  1.0.2  0.5.0  0.4.2  0.2.3 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/run.svg)](https://www.npmjs.org/package/@google-cloud/run)

Cloud Run Admin API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/CHANGELOG.md).

  * [Cloud Run Admin API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/run/latest)



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
  3. [Enable the Cloud Run Admin API API](https://console.cloud.google.com/flows/enableapi?apiid=run.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/run
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
submit build | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/builds.submit_build.js)  
cancel execution | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/executions.cancel_execution.js)  
delete execution | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/executions.delete_execution.js)  
get execution | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/executions.get_execution.js)  
list executions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/executions.list_executions.js)  
create instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/instances.create_instance.js)  
delete instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/instances.delete_instance.js)  
get instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/instances.get_instance.js)  
list instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/instances.list_instances.js)  
start instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/instances.start_instance.js)  
stop instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/instances.stop_instance.js)  
create job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/jobs.create_job.js)  
delete job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/jobs.delete_job.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/jobs.get_iam_policy.js)  
get job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/jobs.get_job.js)  
list jobs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/jobs.list_jobs.js)  
run job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/jobs.run_job.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/jobs.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/jobs.test_iam_permissions.js)  
update job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/jobs.update_job.js)  
delete revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/revisions.delete_revision.js)  
get revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/revisions.get_revision.js)  
list revisions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/revisions.list_revisions.js)  
create service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/services.create_service.js)  
delete service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/services.delete_service.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/services.get_iam_policy.js)  
get service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/services.get_service.js)  
list services | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/services.list_services.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/services.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/services.test_iam_permissions.js)  
update service | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/services.update_service.js)  
get task | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/tasks.get_task.js)  
list tasks | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/tasks.list_tasks.js)  
create worker pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/worker_pools.create_worker_pool.js)  
delete worker pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/worker_pools.delete_worker_pool.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/worker_pools.get_iam_policy.js)  
get worker pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/worker_pools.get_worker_pool.js)  
list worker pools | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/worker_pools.list_worker_pools.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/worker_pools.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/worker_pools.test_iam_permissions.js)  
update worker pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-run/samples/generated/v2/worker_pools.update_worker_pool.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/run@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
