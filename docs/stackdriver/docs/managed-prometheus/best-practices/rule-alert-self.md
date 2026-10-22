---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/rule-alert-self/
title: Evaluation of rules and alerts with self-deployed collection \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:53.586367+00:00
---

# Evaluation of rules and alerts with self-deployed collection  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/rule-alert-self/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Evaluation of rules and alerts with self-deployed collection Stay organized with collections  Save and categorize content based on your preferences. 

This document describes a configuration for rule and alert evaluation in a Managed Service for Prometheus deployment that uses [self-deployed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged).

The following diagram illustrates a deployment that uses multiple clusters in two Google Cloud projects and uses both rule and alert evaluation:

![A deployment for rule and alert evaluation that uses self-deployed collection.](https://docs.cloud.google.com/static/stackdriver/images/gmp-bp-rule-eval-unmgd.png)

To set up and use a deployment like the one in the diagram, note the following:

  * Rules are installed within each Managed Service for Prometheus collection server, just as they are when using standard Prometheus. Rule evaluation executes against the data stored locally on each server. Servers are configured to retain data long enough to cover the lookback period of all rules, which is typically no more than 1 hour. Rule results are written to Monarch after evaluation.

  * A Prometheus AlertManager instance is manually deployed in every single cluster. Prometheus servers are configured by [editing the `alertmanager_config` field of the configuration file](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-unmanaged#eval-rules-unmanaged) to send fired alerting rules to their local AlertManager instance. Silences, acknowledgements, and incident management workflows are typically handled in a third-party tool such as PagerDuty.

You can centralize alert management across multiple clusters into a single AlertManager by using a Kubernetes [Endpoints resource](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-unmanaged#eval-rules-unmanaged).

  * One single cluster running inside Google Cloud is designated as the global rule evaluation cluster for a metrics scope. The [standalone rule evaluator](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-unmanaged#eval-rules-unmanaged) is deployed in that cluster and rules are installed using the standard Prometheus rule-file format.

The standalone rule evaluator is configured to use scoping_project_A, which contains Projects 1 and 2. Rules executed against scoping_project_A automatically fan out to Projects 1 and 2. The underlying service account must be given the [Monitoring Viewer](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) permissions for scoping_project_A.

The rule evaluator is configured to send alerts to the local Prometheus Alertmanager by using the [`alertmanager_config` field of the configuration file](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-unmanaged#eval-rules-unmanaged).




Using a self-deployed global rule evaluator may have unexpected effects, depending on whether you preserve or aggregate the `project_id`, `location`, `cluster`, and `namespace` labels in your rules:

  * If your rules preserve the `project_id` label (by using a `by(project_id)` clause), then rule results are written back to Monarch using the original `project_id` value of the underlying time series.

In this scenario, you need to ensure the underlying service account has the [Monitoring Metric Writer](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) permissions for each monitored project in scoping_project_A. If you add a new monitored project to scoping_project_A, then you must also manually add a new permission to the service account.

  * If your rules do not preserve the `project_id` label (by not using a `by(project_id)` clause), then rule results are written back to Monarch using the `project_id` value of the cluster where the global rule evaluator is running.

In this scenario, you do not need to further modify the underlying service account.

  * If your rules preserve the `location` label (by using a `by(location)` clause), then rule results are written back to Monarch using each original Google Cloud region from which the underlying time series originated.

If your rules do not preserve the `location` label, then data is written back to the location of the cluster where the global rule evaluator is running.




We strongly recommend preserving the `cluster` and `namespace` labels in rule evaluation results whenever possible. Otherwise, query performance might decline and you might encounter cardinality limits. Removing both labels is strongly discouraged.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
