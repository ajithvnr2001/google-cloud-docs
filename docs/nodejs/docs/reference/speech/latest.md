---
url: https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/
title: Cloud Speech-to-Text API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:15.279375+00:00
---

# Cloud Speech-to-Text API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Speech-to-Text API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.5.0  7.4.0  6.6.1  6.3.0  6.1.1  6.0.1  5.4.1  5.3.1  5.1.0  5.0.3  4.10.0  4.9.0  4.8.1  4.7.0  4.6.1  4.5.6  4.1.3 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/speech.svg)](https://www.npmjs.org/package/@google-cloud/speech)

Cloud Speech-to-Text API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/CHANGELOG.md).

  * [Cloud Speech-to-Text API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/speech/latest)



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
  3. [Enable the Cloud Speech-to-Text API API](https://console.cloud.google.com/flows/enableapi?apiid=speech.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/speech
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/adaptation.create_custom_class.js)  
create phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/adaptation.create_phrase_set.js)  
delete custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/adaptation.delete_custom_class.js)  
delete phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/adaptation.delete_phrase_set.js)  
get custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/adaptation.get_custom_class.js)  
get phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/adaptation.get_phrase_set.js)  
list custom classes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/adaptation.list_custom_classes.js)  
list phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/adaptation.list_phrase_set.js)  
update custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/adaptation.update_custom_class.js)  
update phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/adaptation.update_phrase_set.js)  
long running recognize | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/speech.long_running_recognize.js)  
recognize | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/speech.recognize.js)  
streaming recognize | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1/speech.streaming_recognize.js)  
create custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/adaptation.create_custom_class.js)  
create phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/adaptation.create_phrase_set.js)  
delete custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/adaptation.delete_custom_class.js)  
delete phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/adaptation.delete_phrase_set.js)  
get custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/adaptation.get_custom_class.js)  
get phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/adaptation.get_phrase_set.js)  
list custom classes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/adaptation.list_custom_classes.js)  
list phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/adaptation.list_phrase_set.js)  
update custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/adaptation.update_custom_class.js)  
update phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/adaptation.update_phrase_set.js)  
long running recognize | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/speech.long_running_recognize.js)  
recognize | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/speech.recognize.js)  
streaming recognize | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v1p1beta1/speech.streaming_recognize.js)  
batch recognize | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.batch_recognize.js)  
create custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.create_custom_class.js)  
create phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.create_phrase_set.js)  
create recognizer | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.create_recognizer.js)  
delete custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.delete_custom_class.js)  
delete phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.delete_phrase_set.js)  
delete recognizer | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.delete_recognizer.js)  
get config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.get_config.js)  
get custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.get_custom_class.js)  
get phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.get_phrase_set.js)  
get recognizer | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.get_recognizer.js)  
list custom classes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.list_custom_classes.js)  
list phrase sets | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.list_phrase_sets.js)  
list recognizers | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.list_recognizers.js)  
recognize | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.recognize.js)  
streaming recognize | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.streaming_recognize.js)  
undelete custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.undelete_custom_class.js)  
undelete phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.undelete_phrase_set.js)  
undelete recognizer | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.undelete_recognizer.js)  
update config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.update_config.js)  
update custom class | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.update_custom_class.js)  
update phrase set | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.update_phrase_set.js)  
update recognizer | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-speech/samples/generated/v2/speech.update_recognizer.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/speech@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
