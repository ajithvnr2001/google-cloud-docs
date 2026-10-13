---
url: https://docs.cloud.google.com/nodejs/docs/reference/recommender/latest/
title: Recommender API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:10.790836+00:00
---

# Recommender API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/recommender/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Recommender API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  7.3.0  7.1.0  7.0.1  6.1.1  5.0.6  4.2.5 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/recommender.svg)](https://www.npmjs.org/package/@google-cloud/recommender)

Recommender API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/CHANGELOG.md).

  * [Recommender API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/recommender/latest)



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
  3. [Enable the Recommender API API](https://console.cloud.google.com/flows/enableapi?apiid=recommender.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/recommender
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
get insight | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.get_insight.js)  
get insight type config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.get_insight_type_config.js)  
get recommendation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.get_recommendation.js)  
get recommender config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.get_recommender_config.js)  
list insights | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.list_insights.js)  
list recommendations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.list_recommendations.js)  
mark insight accepted | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.mark_insight_accepted.js)  
mark recommendation claimed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.mark_recommendation_claimed.js)  
mark recommendation dismissed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.mark_recommendation_dismissed.js)  
mark recommendation failed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.mark_recommendation_failed.js)  
mark recommendation succeeded | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.mark_recommendation_succeeded.js)  
update insight type config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.update_insight_type_config.js)  
update recommender config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1/recommender.update_recommender_config.js)  
get insight | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.get_insight.js)  
get insight type config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.get_insight_type_config.js)  
get recommendation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.get_recommendation.js)  
get recommender config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.get_recommender_config.js)  
list insight types | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.list_insight_types.js)  
list insights | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.list_insights.js)  
list recommendations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.list_recommendations.js)  
list recommenders | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.list_recommenders.js)  
mark insight accepted | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.mark_insight_accepted.js)  
mark recommendation claimed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.mark_recommendation_claimed.js)  
mark recommendation failed | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.mark_recommendation_failed.js)  
mark recommendation succeeded | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.mark_recommendation_succeeded.js)  
update insight type config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.update_insight_type_config.js)  
update recommender config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-recommender/samples/generated/v1beta1/recommender.update_recommender_config.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/recommender@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
