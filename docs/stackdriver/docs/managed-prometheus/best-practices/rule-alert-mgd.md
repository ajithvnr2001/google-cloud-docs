---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/rule-alert-mgd/
title: Evaluation of rules and alerts with managed collection \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:30.612058+00:00
---

# Evaluation of rules and alerts with managed collection  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/rule-alert-mgd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Evaluation of rules and alerts with managed collection Stay organized with collections  Save and categorize content based on your preferences. 

This document describes a configuration for rule and alert evaluation in a Managed Service for Prometheus deployment that uses [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).

The following diagram illustrates a deployment that uses multiple clusters in two Google Cloud projects and uses both rule and alert evaluation, as well as the optional GlobalRules resource:

![A deployment for rule and alert evaluation that uses managed collection.](https://docs.cloud.google.com/static/stackdriver/images/gmp-bp-rule-eval-mgd.png)

To set up and use a deployment like the one in the diagram, note the following:

  * The [managed rule evaluator](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed) is automatically deployed in any cluster where managed collection is running. These evaluators are configured as follows:

    * Use [Rules](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#rules) resources to run rules on data within a namespace. Rules resources must be applied in every namespace in which you want to execute the rule.

    * Use [ClusterRules](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#clusterrules) resources to run rules on data across a cluster. ClusterRules resources should be applied once per cluster.

  * All rule evaluation executes against the global datastore, Monarch.

    * Rules resources automatically filter rules to the project, location, cluster, and namespace in which they are installed.
    * ClusterRules resources automatically filter rules to the project, location, and cluster in which they are installed.
    * All rule results are written to Monarch after evaluation.
  * A Prometheus AlertManager instance is manually deployed in every single cluster. Managed rule evaluators are configured by [editing the OperatorConfig resource](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed#am-config-managed) to send fired alerting rules to their local AlertManager instance. Silences, acknowledgements, and incident management workflows are typically handled in a third-party tool such as PagerDuty.

You can centralize alert management across multiple clusters into a single AlertManager by using a Kubernetes [Endpoints resource](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed#am-config-managed).




The preceding diagram also shows the optional [GlobalRules](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#globalrules) resource. Use GlobalRules very sparingly, for tasks like calculating global SLOs across projects or for evaluating rules across clusters within a single Google Cloud project. **We strongly recommend using Rules and ClusterRules whenever possible** ; these resources provide superior reliability and are better fits for common Kubernetes deployment mechanisms and tenancy models.

If you use the GlobalRules resource, note the following from the preceding diagram:

  * One single cluster running inside Google Cloud is designated as the global rule-evaluation cluster for a metrics scope. This managed rule evaluator is configured to use scoping_project_A, which contains Projects 1 and 2. Rules executed against scoping_project_A automatically fan out to Projects 1 and 2.

The underlying service account must be given the [Monitoring Viewer](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) permissions for scoping_project_A. For additional information on how to set these fields, see [Multi-project and global rule evaluation](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed#multi-project_and_global_rule_evaluation).

  * As in all other clusters, this rule evaluator is set up with Rules and ClusterRules resources that evaluate rules scoped to a namespace or cluster. These rules are automatically filtered to the _local_ project—Project 1, in this case. Because scoping_project_A contains Project 1, Rules and ClusterRules-configured rules execute only against data from the local project as expected.

  * This cluster also has GlobalRules resources that execute rules against scoping_project_A. GlobalRules are not automatically filtered, and therefore GlobalRules execute exactly as written across all projects, locations, clusters, and namespaces in scoping_project_A.

  * Fired alerting rules will be sent to the self-hosted AlertManager as expected.




Using GlobalRules may have unexpected effects, depending on whether you preserve or aggregate the `project_id`, `location`, `cluster`, and `namespace` labels in your rules:

  * If your GlobalRules rule preserves the `project_id` label (by using a `by(project_id)` clause), then rule results are written back to Monarch using the original `project_id` value of the underlying time series.

In this scenario, you need to ensure the underlying service account has the [Monitoring Metric Writer](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) permissions for each monitored project in scoping_project_A. If you add a new monitored project to scoping_project_A, then you must also manually add a new permission to the service account.

  * If your GlobalRules rule does not preserve the `project_id` label (by not using a `by(project_id)` clause), then rule results are written back to Monarch using the `project_id` value of the cluster where the global rule evaluator is running.

In this scenario, you do not need to further modify the underlying service account.

  * If your GlobalRules preserves the `location` label (by using a `by(location)` clause), then rule results are written back to Monarch using each original Google Cloud region from which the underlying time series originated.

If your GlobalRules does not preserve the `location` label, then data is written back to the location of the cluster where the global rule evaluator is running.




We strongly recommend preserving the `cluster` and `namespace` labels in rule evaluation results unless the purpose of the rule is to aggregate away those labels. Otherwise, query performance might decline and you might encounter cardinality limits. Removing both labels is strongly discouraged.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
