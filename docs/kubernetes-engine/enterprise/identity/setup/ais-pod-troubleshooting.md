---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ais-pod-troubleshooting/
title: Debug authentication issues by using Pod logs \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:53.134686+00:00
---

# Debug authentication issues by using Pod logs  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ais-pod-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Debug authentication issues by using Pod logs Stay organized with collections  Save and categorize content based on your preferences. 

Cluster administrators and developers can debug problems and monitor cluster activity by using the logs of the system Pods that handle authentication from third-party providers. This document applies only to [supported cluster types](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity#supported_cluster_types) that are registered to a fleet.

Based on the severity of the problem, logs are classified using the following severity levels:

  * **INFO[I]** : An operational event with high-level details of the actions taken by the application during the processing of requests (such as startup and housekeeping messages). The logs also contain information about expected events that could result in problems. Examples include authentication and workflow checks.
  * **WARNING[W]** : An unexpected event that may indicate an underlying problem. Examples include provider-specific authentication issues.
  * **ERROR[E]** : An unexpected problematic event that requires a cluster administrator to fix the issue. Examples include missing configuration, token exchange failure, and authentication issues.



The following is an example of a typical pod log message:

`I0926 09:00:00.000000 12345 foo.cc:10] Skipping Kubernetes Webhook adapter startup since it is not configured.`

where,

  * The prefix `I` represents the INFO severity level, appended with the log date `0926`.
  * The time follows, with microseconds, in the machine's local timezone.
  * `12345` is a thread ID number.
  * `foo.cc:10` is the source code location where the log description appears (the bracket `[` and space are fixed delimiters before the message).

**Note:** You can suppress the prefix globally using the `--nolog_prefix` flag or for a single message the `.NoPrefix()` mutator method.

To learn more about logging and cluster administration, see [Cluster administration](https://kubernetes.io/docs/concepts/cluster-administration/logging/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
