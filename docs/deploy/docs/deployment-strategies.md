---
url: https://docs.cloud.google.com/deploy/docs/deployment-strategies/
title: Use a deployment strategy \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:31.260090+00:00
---

# Use a deployment strategy  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deployment-strategies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Use a deployment strategy Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Deploy supports deployment strategies. A deployment strategy is any of several techniques for deploying changes to your application while minimizing impact to users.

## What deployment strategies does Cloud Deploy support?

Cloud Deploy supports the following deployment strategies:

  * [Standard deployment](https://docs.cloud.google.com/deploy/docs/deploying-application)

The standard deployment strategy simply deploys an application to a target runtime or runtimes. The deployment is not performed progressively, and there is no splitting between the old and new versions of your application.

With a standard deployment, you can easily roll back your release, you can verify your deployment, and you can deploy to more than one target at the same time.

  * [Canary deployment](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary)

A canary deployment is a progressive deployment of your application, such that your app is deployed at first to a portion of your infrastructure and can be tested there before being rolled out further. A canary deployment reduces the risk of introducing changes by reducing the number of users likely to be affected by a bug.

For example, with a 50% canary deployment to Cloud Run, half the traffic would be directed to the new revision, with half of it still directed to the old revision. After testing to help ensure stability, you would advance the rollout to 100%. With Cloud Deploy, you can specify any progression of percentages (except partial percentages, like 20.5%).




Both of these deployment strategies support all of the runtime environments that Cloud Deploy supports. Also, all deployment strategies support [rolling back](https://docs.cloud.google.com/deploy/docs/roll-back), [canceling rollouts](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout#cancel_rollout), and deploying to more than one target at the same time ([parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel)).

## Why phases are sometimes skipped

Because a canary runs against an existing version of an application (progressively replacing that version), the canary strategy can't be performed if there's no version deployed yet that Cloud Deploy can recognize.

This means that if you deploy an application for the first time to a given target, and you use a canary deployment strategy, the rollout might skip the canary phase or phases. In this case, after Cloud Deploy skips to the stable phase, and you click **Advance Rollout** to initiate the `stable` phase, the application gets deployed fully to that target, and you can now run a canary against it with your next set of changes. Clicking **Advance Rollout** constitutes an acknowledgement that we've skipped the canary phases that were not applicable for this deployment.

### Use parallel deployment with a deployment strategy

You can use a deployment strategy and still [deploy to more than one target at the same time](https://docs.cloud.google.com/deploy/docs/parallel).

See [Using parallel deployment with a canary deployment strategy](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary#parallel_canary) to find out how to do this with canary.

## What's next

  * Try the quickstart: [Canary deploy an application to a target](https://docs.cloud.google.com/deploy/docs/deploy-app-canary)

  * Learn how to use the [canary deployment strategy](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary)

  * Find out how to [manage the lifecycle of your canary's rollouts](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
