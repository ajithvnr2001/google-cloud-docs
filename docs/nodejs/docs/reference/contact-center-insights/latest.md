---
url: https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/
title: Contact Center AI Insights API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:35.185589+00:00
---

# Contact Center AI Insights API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Contact Center AI Insights API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.0.1  4.1.3  3.9.0  3.8.0  3.7.0  3.6.0  3.3.0  3.1.0  2.7.0  2.6.0  2.4.1  2.3.0  2.1.2  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.2 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/contact-center-insights.svg)](https://www.npmjs.org/package/@google-cloud/contact-center-insights)

Contact Center AI Insights API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/CHANGELOG.md).

  * [Contact Center AI Insights API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/contactcenterinsights/latest)



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
  3. [Enable the Contact Center AI Insights API API](https://console.cloud.google.com/flows/enableapi?apiid=contactcenterinsights.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/contact-center-insights
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
bulk analyze conversations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.bulk_analyze_conversations.js)  
bulk delete conversations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.bulk_delete_conversations.js)  
bulk download feedback labels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.bulk_download_feedback_labels.js)  
bulk upload feedback labels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.bulk_upload_feedback_labels.js)  
calculate issue model stats | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.calculate_issue_model_stats.js)  
calculate stats | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.calculate_stats.js)  
create analysis | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.create_analysis.js)  
create analysis rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.create_analysis_rule.js)  
create conversation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.create_conversation.js)  
create feedback label | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.create_feedback_label.js)  
create issue model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.create_issue_model.js)  
create phrase matcher | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.create_phrase_matcher.js)  
create qa question | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.create_qa_question.js)  
create qa scorecard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.create_qa_scorecard.js)  
create qa scorecard revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.create_qa_scorecard_revision.js)  
create view | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.create_view.js)  
delete analysis | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.delete_analysis.js)  
delete analysis rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.delete_analysis_rule.js)  
delete conversation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.delete_conversation.js)  
delete feedback label | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.delete_feedback_label.js)  
delete issue | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.delete_issue.js)  
delete issue model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.delete_issue_model.js)  
delete phrase matcher | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.delete_phrase_matcher.js)  
delete qa question | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.delete_qa_question.js)  
delete qa scorecard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.delete_qa_scorecard.js)  
delete qa scorecard revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.delete_qa_scorecard_revision.js)  
delete view | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.delete_view.js)  
deploy issue model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.deploy_issue_model.js)  
deploy qa scorecard revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.deploy_qa_scorecard_revision.js)  
export insights data | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.export_insights_data.js)  
export issue model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.export_issue_model.js)  
get analysis | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_analysis.js)  
get analysis rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_analysis_rule.js)  
get conversation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_conversation.js)  
get encryption spec | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_encryption_spec.js)  
get feedback label | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_feedback_label.js)  
get issue | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_issue.js)  
get issue model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_issue_model.js)  
get phrase matcher | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_phrase_matcher.js)  
get qa question | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_qa_question.js)  
get qa scorecard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_qa_scorecard.js)  
get qa scorecard revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_qa_scorecard_revision.js)  
get settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_settings.js)  
get view | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.get_view.js)  
import issue model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.import_issue_model.js)  
ingest conversations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.ingest_conversations.js)  
initialize encryption spec | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.initialize_encryption_spec.js)  
list all feedback labels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.list_all_feedback_labels.js)  
list analyses | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.list_analyses.js)  
list analysis rules | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.list_analysis_rules.js)  
list conversations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.list_conversations.js)  
list feedback labels | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.list_feedback_labels.js)  
list issue models | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.list_issue_models.js)  
list issues | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.list_issues.js)  
list phrase matchers | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.list_phrase_matchers.js)  
list qa questions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.list_qa_questions.js)  
list qa scorecard revisions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.list_qa_scorecard_revisions.js)  
list qa scorecards | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.list_qa_scorecards.js)  
list views | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.list_views.js)  
query metrics | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.query_metrics.js)  
tune qa scorecard revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.tune_qa_scorecard_revision.js)  
undeploy issue model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.undeploy_issue_model.js)  
undeploy qa scorecard revision | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.undeploy_qa_scorecard_revision.js)  
update analysis rule | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.update_analysis_rule.js)  
update conversation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.update_conversation.js)  
update feedback label | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.update_feedback_label.js)  
update issue | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.update_issue.js)  
update issue model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.update_issue_model.js)  
update phrase matcher | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.update_phrase_matcher.js)  
update qa question | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.update_qa_question.js)  
update qa scorecard | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.update_qa_scorecard.js)  
update settings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.update_settings.js)  
update view | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.update_view.js)  
upload conversation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-contactcenterinsights/samples/generated/v1/contact_center_insights.upload_conversation.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/contact-center-insights@legacy-8` installs client libraries for versions compatible with Node.js 8.

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
