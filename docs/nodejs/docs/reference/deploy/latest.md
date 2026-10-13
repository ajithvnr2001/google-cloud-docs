---
url: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/
title: Cloud Deploy API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:41.980813+00:00
---

# Cloud Deploy API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Deploy API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.0.1  4.4.0  4.3.0  4.0.0  3.6.0  3.5.0  3.4.0  3.1.0  3.0.0  2.5.0  2.4.1  2.3.1  2.2.2  2.1.1  1.0.0  0.2.0 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/deploy.svg)](https://www.npmjs.org/package/@google-cloud/deploy)

Cloud Deploy API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/CHANGELOG.md).

  * [Cloud Deploy API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/deploy/latest)



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
  3. [Enable the Cloud Deploy API API](https://console.cloud.google.com/flows/enableapi?apiid=clouddeploy.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/deploy
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
abandon release | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.abandon_release.js)  
advance rollout | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.advance_rollout.js)  
approve rollout | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.approve_rollout.js)  
cancel automation run | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.cancel_automation_run.js)  
cancel rollout | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.cancel_rollout.js)  
create automation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.create_automation.js)  
create custom target type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.create_custom_target_type.js)  
create delivery pipeline | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.create_delivery_pipeline.js)  
create deploy policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.create_deploy_policy.js)  
create release | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.create_release.js)  
create rollout | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.create_rollout.js)  
create target | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.create_target.js)  
delete automation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.delete_automation.js)  
delete custom target type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.delete_custom_target_type.js)  
delete delivery pipeline | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.delete_delivery_pipeline.js)  
delete deploy policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.delete_deploy_policy.js)  
delete target | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.delete_target.js)  
get automation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.get_automation.js)  
get automation run | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.get_automation_run.js)  
get config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.get_config.js)  
get custom target type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.get_custom_target_type.js)  
get delivery pipeline | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.get_delivery_pipeline.js)  
get deploy policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.get_deploy_policy.js)  
get job run | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.get_job_run.js)  
get release | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.get_release.js)  
get rollout | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.get_rollout.js)  
get target | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.get_target.js)  
ignore job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.ignore_job.js)  
list automation runs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.list_automation_runs.js)  
list automations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.list_automations.js)  
list custom target types | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.list_custom_target_types.js)  
list delivery pipelines | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.list_delivery_pipelines.js)  
list deploy policies | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.list_deploy_policies.js)  
list job runs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.list_job_runs.js)  
list releases | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.list_releases.js)  
list rollouts | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.list_rollouts.js)  
list targets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.list_targets.js)  
retry job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.retry_job.js)  
rollback target | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.rollback_target.js)  
terminate job run | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.terminate_job_run.js)  
update automation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.update_automation.js)  
update custom target type | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.update_custom_target_type.js)  
update delivery pipeline | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.update_delivery_pipeline.js)  
update deploy policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.update_deploy_policy.js)  
update target | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-deploy/samples/generated/v1/cloud_deploy.update_target.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/deploy@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
