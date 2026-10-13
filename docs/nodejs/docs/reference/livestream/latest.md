---
url: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/
title: Live Stream API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:14.558198+00:00
---

# Live Stream API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Live Stream API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.0.2  0.5.1  0.4.1  0.3.4  0.1.0 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/livestream.svg)](https://www.npmjs.org/package/@google-cloud/livestream)

Live Stream API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/CHANGELOG.md).

  * [Live Stream API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/livestream/latest)



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
  3. [Enable the Live Stream API API](https://console.cloud.google.com/flows/enableapi?apiid=livestream.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/livestream
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create asset | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.create_asset.js)  
create channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.create_channel.js)  
create clip | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.create_clip.js)  
create dvr session | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.create_dvr_session.js)  
create event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.create_event.js)  
create input | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.create_input.js)  
delete asset | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.delete_asset.js)  
delete channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.delete_channel.js)  
delete clip | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.delete_clip.js)  
delete dvr session | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.delete_dvr_session.js)  
delete event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.delete_event.js)  
delete input | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.delete_input.js)  
get asset | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.get_asset.js)  
get channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.get_channel.js)  
get clip | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.get_clip.js)  
get dvr session | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.get_dvr_session.js)  
get event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.get_event.js)  
get input | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.get_input.js)  
get pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.get_pool.js)  
list assets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.list_assets.js)  
list channels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.list_channels.js)  
list clips | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.list_clips.js)  
list dvr sessions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.list_dvr_sessions.js)  
list events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.list_events.js)  
list inputs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.list_inputs.js)  
preview input | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.preview_input.js)  
start channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.start_channel.js)  
start distribution | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.start_distribution.js)  
stop channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.stop_channel.js)  
stop distribution | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.stop_distribution.js)  
update channel | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.update_channel.js)  
update dvr session | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.update_dvr_session.js)  
update input | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.update_input.js)  
update pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-video-livestream/samples/generated/v1/livestream_service.update_pool.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/livestream@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
