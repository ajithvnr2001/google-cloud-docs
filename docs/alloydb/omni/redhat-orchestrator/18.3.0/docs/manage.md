---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/manage/
title: Manage and monitor AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:40.633407+00:00
---

# Manage and monitor AlloyDB Omni  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/manage/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Manage and monitor AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/manage)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/manage)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/manage)

This page describes how to manage AlloyDB Omni user roles, monitor the activity of your AlloyDB Omni server, and update or remove your AlloyDB Omni installation. 

## Manage user roles

AlloyDB Omni uses the following roles:

  * AlloyDB Omni includes a superuser role named `alloydbadmin`, and a non-superuser role named `alloydbmetadata`.

  * The default `postgres` user has a superuser role.

  * All other predefined user roles have no privileges. They are reserved for potential uses in the future.




### Set up an AlloyDB Omni database

We recommend following these steps when setting up an AlloyDB Omni database:

  1. Define or import your databases using the `postgres` user role. In a new installation, this role has superuser privileges.

  2. Create new user roles that have the correct level of access to your application's tables, again using the `postgres` user role.

  3. Configure your application to connect to the database using these new, limited-access roles.




You can create and define as many new user roles as you need. Don't modify or delete any of the user roles that comes with AlloyDB Omni.

For more information, see [Manage AlloyDB Omni users and roles](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/manage-users-roles-permissions).

## Monitor AlloyDB Omni

Monitoring your AlloyDB Omni installation includes fetching and analyzing AlloyDB Omni metrics.

### View system metrics using System Insights

You can monitor real-time and historical infrastructure metrics for your AlloyDB Omni instances using **System Insights** in the AlloyDB Omni web user interface. **System Insights** queries the Prometheus metrics exported by the AlloyDB Omni monitoring agent to display resource utilization charts.

**Note:** **System Insights** isn't supported when deploying AlloyDB Omni using containers because a containerized monitoring agent isn't available for container deployments.

To view system metrics in the web UI, complete the following steps:

  1. [Connect to the web UI](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/connect-web-ui) and select your cluster.
  2. In the navigation menu, click **System Insights**.
  3. Optional: In a multi-node cluster, use the **Filter by: Instances** list to select a specific instance endpoint (for example, `localhost:9187`).
  4. Select a time window (**1 hour** , **6 hours** , **1 day** , or **7 days**) to adjust the observation period across all charts.
  5. Review the system telemetry charts: 
     * **CPU Usage** : Displays the percentage of CPU utilization over time.
     * **Memory Usage** : Displays the percentage of allocated memory in use over time.
     * **Memory Available** : Displays the percentage of free memory available over time.
     * **Memory Limit** : Displays the configured memory quota (in GB) for the instance.
     * **Storage and disk I/O** : Displays six additional charts tracking storage usage, storage limit, number of disk reads, bytes read, number of disk writes, and bytes written.



## Uninstall AlloyDB Omni

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
