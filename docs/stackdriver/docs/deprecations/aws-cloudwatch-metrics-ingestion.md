---
url: https://docs.cloud.google.com/stackdriver/docs/deprecations/aws-cloudwatch-metrics-ingestion/
title: AWS CloudWatch metrics in Connector projects \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:18.772048+00:00
---

# AWS CloudWatch metrics in Connector projects  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/deprecations/aws-cloudwatch-metrics-ingestion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  AWS CloudWatch metrics in Connector projects Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring is ending support for AWS CloudWatch metrics in Connector projects. This is a breaking change.

  * As of August 21, 2023, you can't create new AWS Connector projects.
  * [AWS Cloudwatch metrics](https://docs.cloud.google.com/monitoring/api/metrics_aws) collected by using existing AWS Connector projects were supported until August 21, 2024.



Collection of Amazon EC2 logs by using the legacy Logging agent isn't affected by this deprecation.

## Replacement: Prometheus CloudWatch exporter

If you are collecting [AWS CloudWatch metrics](https://docs.cloud.google.com/monitoring/api/metrics_aws) by using an AWS Connector project, then you must migrate to the replacement solution, which uses the Ops Agent running on a Compute Engine VM to collect metrics from the Prometheus CloudWatch exporter.

The [Prometheus CloudWatch exporter](https://github.com/prometheus/cloudwatch_exporter) is an open source Prometheus exporter that can collect AWS CloudWatch metrics from the CloudWatch API for AWS services and send them to Cloud Monitoring.

  * The Prometheus CloudWatch exporter provides the same functionality as the current solution, supporting from metrics from the same AWS services.
  * The Prometheus CloudWatch exporter provides the following data-collection improvements over the current solution: 
    * Collection of additional metrics from the AWS services currently supported.
    * Ability to to collect metrics from additional AWS services, beyond those supported by the current solution. For more information about the available AWS CloudWatch metrics, see the [AWS CloudWatch service documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html).
  * You can achieve up to an **8x cost savings** for the same AWS CloudWatch metrics over the current solution. The replacement solution uses Google Cloud Managed Service for Prometheus metrics instead of Cloud Monitoring metrics. For more information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).



## Migration

We recommend that you begin migrating AWS metric collection to the Prometheus CloudWatch exporter as soon as possible. If you don't migrate to the Prometheus CloudWatch exporter, then you will stop receiving new data from your AWS Cloudwatch metrics on August 21, 2024.

Moving to the Prometheus CloudWatch exporter is a breaking change that affects any chart, dashboard, or alerting policy that monitors AWS CloudWatch metrics. **You will need to rebuild these charts, dashboards, and alerting policies.**

If you no longer want to collect AWS metrics, then we recommend shutting down your current collection.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
