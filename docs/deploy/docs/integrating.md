---
url: https://docs.cloud.google.com/deploy/docs/integrating/
title: Integrating Cloud Deploy with other systems \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:46.289490+00:00
---

# Integrating Cloud Deploy with other systems  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/integrating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Integrating Cloud Deploy with other systems Stay organized with collections  Save and categorize content based on your preferences. 

You can integrate Cloud Deploy with some of the other systems you rely on for software delivery. This page describes how to integrate Cloud Deploy with the following:

  * Test tooling
  * Workflow management



See [Integrating with your CI system](https://docs.cloud.google.com/deploy/docs/integrating-ci) to learn how to call Cloud Deploy from your CI pipeline.

## Before you begin

The instructions on this page assume you already meet the following conditions:

  * You have [enabled the applicable APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com&redirect=https://cloud.google.com/deploy/docs/deploy-app-gke&_ga=2.88599711.504283000.1626992575-1788689322.1622287630)

  * You have at least one delivery pipeline [defined](https://docs.cloud.google.com/deploy/docs/config-file) and [registered](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets#register_the_delivery_pipeline_and_targets) with Cloud Deploy.

  * You have at least one [target defined](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions), and your delivery pipeline references that target.

  * You have [set up Pub/Sub notifications](https://docs.cloud.google.com/deploy/docs/subscribe-deploy-notifications) to receive notifications from the following topics:

    * `clouddeploy-operations`
    * `clouddeploy-approvals`



## Integrating with automated testing

You can use Cloud Deploy with Pub/Sub to integrate testing with your delivery pipeline, so you can promote the release automatically, for continuous delivery.

You can also use annotations on a rollout to provide a link to test results. For more information, see [Using labels and annotations with Cloud Deploy](https://docs.cloud.google.com/deploy/docs/labels-annotations).

### Using Pub/Sub to automate promotion

  1. Listen to [Pub/Sub messages](https://docs.cloud.google.com/deploy/docs/subscribe-deploy-notifications) from the `clouddeploy-operations` topic.

The message contains the following attributes:

     * `Action: SUCCEED`
     * `ResourceType: Rollout`
     * `Resource: projects/.../locations/.../deliveryPipelines/.../releases/.../rollouts/...`
  2. When you receive a notification that deployment has succeeded, run your tests on your deployed application.

  3. When your tests succeed, call Cloud Deploy to automatically promote to the next stage:
         
         gcloud deploy releases promote RELEASE_NAME \
         --delivery-pipeline=PIPELINE_NAME \
         --region=REGION \
         --annotations=KEY=VALUE,...
         

where:

     * RELEASE_NAME

is the name of the release. This value is required.

     * PIPELINE_NAME

is the name of the delivery pipeline managing this release. This value is required.

     * REGION

is the region in which the pipeline is running. If you've set the property `deploy/region`, you can omit this flag.

     * KEY=VALUE,...

is a list of one or more key-value string pairs, comma-separated, which can contain information about your test results and other testing information. Here's an example:

`gcloud deploy releases promote --annotations="from_target=test,status=stable"`

Annotations on the rollout are immutable, so if you add a status annotation, you can't later update that status on the same rollout.




### Using annotations to provide access to test results

If you have the URL pointing to where test results can be accessed, you can provide that URL as an annotation on a rollout, using the `--annotations` flag. Here's an example:
    
    
    gcloud deploy releases promote --delivery-pipeline=my-demo-app-1 --region=us-central1 --project=my-demo-app-1-project --release=test-release-001 --annotations="test_results_url=https://example.com/results/my-demo-app-test-results-dev"
    
    

For more information, see [Using labels and annotations with Cloud Deploy](https://docs.cloud.google.com/deploy/docs/labels-annotations).

## Integrating with third-party workflow management

Cloud Deploy publishes operational messages to Pub/Sub. Your workflow management tool can subscribe to these Pub/Sub topics and use them to trigger specific workflows.

### For approvals

The `clouddeploy-approvals` topic notifies your system when an approval is required for a rollout. Your external workflow system can then work its magic to get the approval, then call `gcloud deploy rollouts approve`.

The account that issues the `rollouts approve` command must have the predefined IAM role `roles/clouddeploy.approver`.

To set up an external approval workflow:

  1. [Require approval on the target](https://docs.cloud.google.com/deploy/docs/promote-release#manage_approvals_for_a_delivery_pipeline).

In the definition for that target, include `requireApproval: true`.

  2. To consume the messages, subscribe to the `clouddeploy-approvals` Pub/Sub topic, and set up your workflow management system.

  3. When your workflow management system receives a message from the `clouddeploy-approvals` topic that includes `"Action": "Required"`, it kicks off an approval workflow, configured according to the requirements of your organization.

The message also includes a reference to the rollout to be approved, in the following format:

`Resource: projects/.../locations/.../deliveryPipelines/.../releases/.../rollouts/...`

The output of the approval workflow is an [approval or rejection](https://docs.cloud.google.com/deploy/docs/promote-release#manage_approvals_for_a_delivery_pipeline) of the rollout.

  4. Your workflow management system returns the approval or rejection to Cloud Deploy in the form of the following command:

The command for approval is as follows:
         
         gcloud deploy rollouts approve ROLLOUT \
         --delivery-pipeline=PIPELINE_NAME \
         --region=REGION \
         --release=RELEASE_NAME
         

The command for rejecting the rollout is as follows:
         
         gcloud deploy rollouts reject ROLLOUT \
         --delivery-pipeline=PIPELINE_NAME \
         --region=REGION \
         --release=RELEASE_NAME
         

where:

     * ROLLOUT

is the name of the rollout for which approval was requested.

     * PIPELINE_NAME

is the delivery pipeline managing deployment of your application.

     * RELEASE_NAME

is the name of the release with which this rollout is associated.

     * REGION

is the region in which the delivery pipeline is running.




Here's an example:

`gcloud deploy rollouts approve test-rollout --delivery-pipeline=web-app --release=test-release --region=us-central1`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
