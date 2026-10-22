---
url: https://docs.cloud.google.com/build/docs/triggers/
title: Cloud Build triggers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:30.449893+00:00
---

# Cloud Build triggers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/triggers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Cloud Build triggers Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Build uses build triggers to enable CI/CD automation. You can configure triggers to listen for incoming events, such as when a new commit is pushed to a repository or when a pull request is initiated, and then automatically execute a build when new events come in. You can also configure triggers to build code on any changes to your source repository or only on changes that match certain criteria.

This page provides an overview of each trigger type and capabilities associated with triggers.

## Repository event triggers

Cloud Build lets you to automatically execute builds on repository events such as pushes or pull requests. You can connect external repositories, such as repositories in GitHub or Bitbucket, to Cloud Build or use code in Cloud Source Repositories for your builds. While you can connect any source repository to Cloud Build, Cloud Build provides specific repository event triggers you can can use to integrate specific source code management systems (SCMs). This section discusses available repository event triggers.

**Caution:** Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

### GitHub triggers

You can create GitHub triggers to automatically execute builds in response to repository events, such as pushes or pull requests. You can view the trigger's build status on GitHub and Google Cloud console. You can also use the [Cloud Build GitHub app](https://github.com/marketplace/google-cloud-build) to connect and build code in GitHub. To learn more, see [Building repositories from GitHub](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-github).

### GitHub Enterprise triggers

You can create triggers for repositories hosted on a GitHub Enterprise instance, including instances hosted in an on-premises environment and not reachable over a public internet connection. GitHub Enterprise triggers can be used to execute builds in response to pushes or pull requests from a GitHub Enterprise instance. To learn more, see [Building repositories from GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-github-enterprise).

### GitLab Enterprise Edition triggers

You can create triggers for repositories hosted on a GitLab Enterprise Edition instance, including instances hosted in a private network. GitLab Enterprise Edition triggers can be used to execute builds in response to commit pushes or pull requests associated with your GitLab Enterprise Edition repository. To learn more, see [Building repositories from GitLab Enterprise Edition](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/build-repos-from-gitlab-enterprise-edition).

### Bitbucket Server triggers

You can create triggers for repositories hosted on a Bitbucket Server instance, including instances hosted in an on-premises environment. You can connect your Bitbucket Server repository to Cloud Build multiple times with multiple host connections. To learn more on how to create triggers to execute builds in response to events, see [Building repositories from Bitbucket Server](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-bitbucket-server).

### Bitbucket Data Center triggers

You can create triggers for repositories hosted on a Bitbucket Data Center instance, including instances hosted in an on-premises environment. Bitbucket Data Center triggers can be used to execute builds in response to events such as commit pushes or pull requests. To learn more, see [Building repositories from Bitbucket Data Center](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-bitbucket-data-center).

### Bitbucket Cloud triggers

You can create triggers for repositories hosted in Bitbucket Cloud. Bitbucket Cloud triggers can be used to execute builds in response to events such as commit pushes or pull requests. To learn more, see [Building repositories from Bitbucket Cloud](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-bitbucket-cloud).

### Secure Source Manager triggers

You can create triggers for repositories hosted in [Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/overview). Secure Source Manager triggers can be used to execute builds in response to events such as commit pushes or pull requests. To learn more, see [Create a triggers file in Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/create-triggers-file).

## Manual triggers

You can create manual triggers to execute builds manually and override defined substitution variable values at invocation time prior to executing a build. You can also configure manual triggers to [run on a schedule](https://docs.cloud.google.com/build/docs/automating-builds/create-scheduled-triggers). To learn more, see [Manually build code in source repositories](https://docs.cloud.google.com/build/docs/automating-builds/create-manual-triggers).

## Pub/Sub triggers

**Note:** Cloud Build Pub/Sub triggers are not supported when VPC Service Controls is used.

You can create Pub/Sub triggers to execute builds in response to any message published over Pub/Sub. For example, you can use Pub/Sub triggers for building in response to image pushes to Artifact Registry. In this case, you can configure your trigger to use filters to execute a build only if the pushed image matches a specific tag, such as `prod`. Additionally, Pub/Sub triggers can be configured to subscribe to any Pub/Sub topic. To learn more, see [Automate builds in response to Pub/Sub events](https://docs.cloud.google.com/build/docs/automating-builds/create-pubsub-triggers).

## Webhook triggers

You can create webhook triggers to execute builds in response to webhooks. Webhook events sent to a custom URL enable you to directly connect external systems and external source code management systems (SCMs), such as Bitbucket.com, Bitbucket Server, or GitLab, to Cloud Build. When creating webhook triggers, you can also define your build configuration inline on your trigger to control which repositories your trigger clones during build time rather than explicitly specifying a source. To learn more, see [Automate builds in response to webhook events](https://docs.cloud.google.com/build/docs/automating-builds/create-webhook-triggers). Additionally, to learn to use webhook triggers to build repositories from specific SCMs, see [Building repositories from Bitbucket Server](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-bitbucket-server), [Building repositories from Bitbucket Cloud](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-bitbucket-cloud), and [Building repositories from GitLab](https://docs.cloud.google.com/build/docs/automating-builds/build-repos-from-gitlab).

## Triggers for Developer Connect-linked repositories

[Developer Connect](https://docs.cloud.google.com/developer-connect/docs/overview) lets you connect external products or non-Google developer tools to Google Cloud using standardized steps and apps. You can configure triggers that build from repositories connected through Developer Connect for the following SCMs:

  * [Bitbucket Cloud](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-cloud?generation=connect)
  * [Bitbucket Data Center](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-data-center?generation=connect)
  * [Bitbucket Server](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server?generation=connect)
  * [GitHub](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github?generation=connect)
  * [GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise?generation=connect)
  * [GitLab](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/build-repos-from-gitlab?generation=connect)
  * [Gitlab Enterprise Edition](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/build-repos-from-gitlab-enterprise-edition?generation=connect)



## Trigger capabilities

Cloud Build triggers provide capabilities that give you fine-grained control over how a build is executed. This section discusses various capabilities associated with triggers.

### Scheduled manual triggers

You can schedule manual triggers to automatically execute builds on a predefined schedule. For example, you may want to configure a scheduled trigger to run a build every Saturday at 6:00 AM. To schedule builds, you can [create a manual trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manual-triggers#creating_manual_triggers) and invoke the trigger using Cloud Scheduler. To learn more, see [Schedule builds](https://docs.cloud.google.com/build/docs/automating-builds/create-scheduled-triggers).

### Filtering events

Cloud Build uses [Common Expression Language](https://github.com/google/cel-spec) (CEL) with the variable, `build`, on fields listed in the [Build](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds) resource to access fields associated with your build event such as your trigger ID, image list, or substitution values. You can use the `filter` string to filter build events in your build config file using any field listed in the [Build](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds) resource. To learn more, see [Use CEL to filter build events](https://docs.cloud.google.com/build/docs/automating-builds/create-pubsub-triggers)

### Substitution variables

You can specify substitution variables in your build configuration file to substitute specific values at build time. For example, you may want to use substitution variables if a value is not known until build time or if you want to re-use an existing build request with different variables. Cloud Build provides default substitutions you can use for builds invoked by triggers, such as variables mapping to your trigger name or repository name. You can also define your own substitution variables. To learn more, see [Substituting variable values](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values).

#### Bash parameter expansions

You can apply bash parameter expansions to substitution variable values. Bash parameter expansions allow you to manipulate strings associated with existing variables. For example, you can use bash parameter expansions to capitalize letters or replace a substring. To learn more, see [Bash parameter expansions](https://docs.cloud.google.com/build/docs/configuring-builds/use-bash-and-bindings-in-substitutions#bash_parameter_expansions).

#### Payload bindings

You can store part of your trigger's event payload as a substitution variable by using payload bindings. Variables associated with a payload are referred to as bindings and are available for builds invoked by both push and pull events. You can use bindings to access additional data related to your build, such as the author of a pull request. To learn more, see [Payload bindings](https://docs.cloud.google.com/build/docs/configuring-builds/use-bash-and-bindings-in-substitutions#payload_bindings).

### Approvals

You can configure triggers to not immediately execute a build, but instead mark a build as pending until approved. If a user with permissions approves a pending build, the build starts. If the approval is denied, the build doesn't start. To learn how to configure triggers that require approval, see [Gate builds on approval](https://docs.cloud.google.com/build/docs/automating-builds/approve-builds).

### Build status notifications

You can configure Cloud Build notifiers to listen to build event updates from Pub/Sub [on the default `cloud-builds` topic or a user-defined topic](https://docs.cloud.google.com/build/docs/configuring-notifications/notifiers#pubsub-topic-config). Notifiers can also filter messages received by the topic and send messages to your connected services. Cloud Build provides and maintains deployable notifier images in the [`cloud-build-notifiers` repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers). You can configure notifications using a Cloud Build notifier, such as [BigQuery](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-bigquery), [HTTP](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-http), [Slack](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-slack), or [SMTP](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-smtp) or [create your own notifier](https://docs.cloud.google.com/build/docs/configuring-notifications/create-notifier).

## What's next

  * Learn how to [create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
