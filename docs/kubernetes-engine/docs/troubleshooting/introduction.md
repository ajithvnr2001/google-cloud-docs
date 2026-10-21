---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction/
title: Introduction to GKE troubleshooting \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:05.796045+00:00
---

# Introduction to GKE troubleshooting  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Introduction to GKE troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Keep your services on Google Kubernetes Engine (GKE) running smoothly by learning how to effectively troubleshoot your issues. Whether you're new to Kubernetes or an experienced user, learn to diagnose and resolve common problems, ranging from application errors like `CrashLoopBackOff` to cluster-wide issues like nodes not joining or Pods failing to schedule. You'll learn to troubleshoot these issues by using key tools like the `kubectl` command-line tool, Cloud Logging, and Cloud Monitoring.

Build your GKE troubleshooting skills with these tools and techniques:

  * [Review Google Cloud service health and incidents](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-service-health) for ongoing reliability incidents that might affect your clusters.

  * Quickly identify potential issues by [assessing cluster and workload health in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-console).

  * View the live status of resources like nodes and Pods by [investigating the cluster's state with the `kubectl` command-line tool](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-kubectl).

  * Find the root cause of failures by [conducting historical analysis with Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-logging).

  * Address issues before they affect users by [performing proactive monitoring with Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-monitoring).

  * [Accelerate diagnosis with Gemini Cloud Assist](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-gemini) by analyzing errors, receiving step-by-step guidance, and automatically investigating issues.

  * Learn how these tools work together by following an [example troubleshooting scenario](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-example) to diagnose and resolve a real-world application failure.

  * Backend logs for certain managed components are retained for a maximum of 30 days. If you need to contact Cloud Customer Care, open a request less than 30 days after you notice an issue.




## Understand core concepts

If you're new to Kubernetes and GKE, understanding core concepts, like cluster architecture and the relationship between Pods and nodes, is essential before you start to troubleshoot. If you want to learn more, see [Start learning about GKE](https://docs.cloud.google.com/kubernetes-engine/docs/learn).

It's also helpful to understand which parts of GKE you're responsible for maintaining and which parts Google Cloud is responsible for maintaining. For more information, see [GKE shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility).

## What's next

  * Read [Review Google Cloud service health and incidents](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-service-health) (the next page in this series).

  * For advice about resolving specific problems, review [GKE's troubleshooting guides](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
