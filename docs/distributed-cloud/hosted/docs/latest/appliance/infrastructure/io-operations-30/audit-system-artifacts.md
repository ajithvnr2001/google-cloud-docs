---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/audit-system-artifacts/
title: Audit changes to system artifacts \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:59.049358+00:00
---

# Audit changes to system artifacts  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/audit-system-artifacts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Audit changes to system artifacts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to retrieve audit logs for system artifacts in Google Distributed Cloud (GDC) air-gapped appliance.

System artifacts exist in the Artifact Registry of the org infrastructure cluster. All changes and operations performed on the system artifacts are audited. As an Infrastructure Operator (IO), view the audit logs through the Grafana user interface (UI).

## Before you begin

To get the permissions that you need to view audit logs, ask your Security Admin to grant you the following roles for the org infrastructure cluster access:

  * Grafana Viewer (`grafana-viewer`) role.
  * Organization Grafana Viewer (`organization-grafana-viewer`) role.



## Get audit logs for artifacts in the org infrastructure cluster

To retrieve audit logs for system artifacts in the org infrastructure cluster, complete the following steps:

  1. Go to the monitoring instance UI for the org infrastructure cluster.

  2. Click **Explore > audit-logs-loki** and build the query to get audit logs.




![The audit-logs-loki option is selected on the Explore page of the monitoring instance UI for the org infrastructure cluster.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/infrastructure/images/root-admin-cluster-audit-logs.png)

## Find artifacts with Loki queries

You can build Loki queries to find artifacts.

**Note:** Use `service_name="artifactmanagement"` in the query for the audit logs of artifacts.

The following sections contain examples for querying audit logs.

### Query audit logs for all system artifacts

Run the following query to return audit logs for all system artifacts:
    
    
    {cluster="ORG_INFRA_CLUSTER",service_name="artifactmanagement"}
    

Replace CLUSTER_NAME with the cluster name, which will match the pattern `<ORG_NAME>-infra`.

For example:
    
    
    {cluster="<ORG_NAME>-infra", service_name="artifactmanagement"}`
    

### Query audit logs for one specific Artifact Registry

Run the following query to return audit logs for one specific Artifact Registry:
    
    
    {cluster="ORG_INFRA_CLUSTER",service_name="artifactmanagement"} | json resource="resource" | resource=~"^REGISTRY_PREFIX.*"
    

Replace the following:

  * ORG_INFRA_CLUSTER: the org infrastructure cluster name, such as `ORG-INFRA`.
  * REGISTRY_PREFIX: the target Artifact Registry name prefix.



For example:
    
    
    {cluster="ORG-INFRA",service_name="artifactmanagement"} | json resource="resource" | resource=~"^gpc-system-services.*"
    

![On the Explore page of the Grafana UI, the query to return audit logs for one artifact registry is running and displays the resulting audit logs.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/infrastructure/images/audit-logs-one-artifact-repo.png)

**Figure 2.** Examples of audit logs for one specific Artifact Registry listed on the Grafana UI.

In figure 2, the query to return audit logs from the `gpc-system-services` Artifact Registry of the cluster displays its results as a list on the same page.

### Query audit logs for multiple Artifact Registry registries

Run the following query to return audit logs for multiple Artifact Registry registries:
    
    
    {cluster="ORG_INFRA_CLUSTER",service_name="artifactmanagement"}
    | json resource="resource" |
    resource=~"^REGISTRY1_PREFIX.*" or
    resource=~"^REGISTRY2_PREFIX.*"
    

**Note:** The `or` condition specifies additional Artifact Registry registries.

Replace the following:

  * `ORG_INFRA_CLUSTER`: the target cluster name, such as `orgname-infra`.
  * `REGISTRY1_PREFIX`: the first target Artifact Registry name prefix.
  * `REGISTRY2_PREFIX`: the second target Artifact Registry name prefix.



For example:
    
    
    {cluster="org-infra",service_name="artifactmanagement"} | json
    resource="resource" | resource=~"^gpc-system.*" or resource=~"^library/.*"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
