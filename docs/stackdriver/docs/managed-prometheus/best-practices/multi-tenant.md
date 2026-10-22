---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/multi-tenant/
title: Multi-tenant monitoring and querying \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:54.807039+00:00
---

# Multi-tenant monitoring and querying  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/multi-tenant/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Multi-tenant monitoring and querying Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can give different teams access to different sets of projects. You can establish this kind of multi-tenant monitoring by using [metrics scopes](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/config#metric-scopes) in combination with multiple instances of Grafana and multiple [data source syncers](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#grafana-oauth).

You need to set up only one Grafana instance and one data source syncer for each metrics scope, regardless of how many projects are in the metrics scope or how many Google Cloud regions you use:

  * Queries to Monarch automatically expand to all projects within a metrics scope, unless a `project_id` filter is included.

  * Queries execute across all regions unless a `location` filter is included.




You don't need to change anything on the ingestion side to achieve multi-tenant monitoring.

The following diagram illustrates a configuration for multi-tenant monitoring:

![You can set up Managed Service for Prometheus with a mix of managed and self-deployed collection.](https://docs.cloud.google.com/static/stackdriver/images/gmp-bp-multi-tenant.png)

To set up and use a configuration like the one in the diagram, set up your metrics scopes, Grafana instances, and data source syncers as follows:

  * You want Dev team A to be able to read from and access Projects 1 and 2. To set up this access, you do the following:

    * Put Project 1 and Project 2 into the metrics scope of scoping_project_A.

    * Put a data source syncer in Project 1, and configure it to use scoping_project_A. Give the syncer's service account [Monitoring Viewer](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) permissions for scoping_project_A.

When a user issues queries from the Grafana instance associated with this data source syncer, Monarch expands scoping_project_A into its constituent monitored projects and returns results for both Project 1 and Project 2, across all Google Cloud regions. Because the Grafana instance and data source syncer live within Project 1, only users with access to Project 1 can query scoping_project_A.

  * You want Dev team B to be able to read from and access Projects 3 and 4. To set up this access, you do the following:

    * Put Project 3 and Project 4 into the metrics scope of scoping_project_B.

    * Put a data source syncer in Project 3, and configure it to use scoping_project_B. Give the syncer's service account [Monitoring Viewer](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) permissions for scoping_project_B.

When a user issues queries from the Grafana instance associated with this data source syncer, Monarch expands scoping_project_B into its constituent monitored projects and returns results for both Project 3 and Project 4, across all Google Cloud regions. Because the Grafana instance and data source syncer live within Project 3, only users with access to Project 3 can query scoping_project_B.

  * You want the SRE team to be able to read from and access Projects 1, 2, 3, 4, and 5. To set up this access, you do the following:

    * Put all the projects into the metrics scope of scoping_project_C.

    * Put a data source syncer in Project 5, and configure it to use scoping_project_C. Give the syncer's service account [Monitoring Viewer](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) permissions for scoping_project_C.

When a user issues queries from the Grafana instance associated with this data source syncer, Monarch expands scoping_project_C into its constituent monitored projects and returns results for Projects 1, 2, 3, 4, and 5, across all Google Cloud regions. Because the Grafana instance and data source syncer live within Project 5, only users with access to Project 5 can query scoping_project_C.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
