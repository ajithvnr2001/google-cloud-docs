---
url: https://docs.cloud.google.com/chronicle/docs/secops/mssp-multi-tenant-operations/
title: MSSP multi-tenant operations \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:28.078546+00:00
---

# MSSP multi-tenant operations  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/mssp-multi-tenant-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MSSP multi-tenant operations

Supported in:

Google SecOps 

This guide helps managed security service providers (MSSPs), security analysts, and incident responders run simultaneous searches and investigate threats across multiple Google Security Operations customer instances. It explains how to configure federated instance groups, execute cross-tenant Unified Data Model (UDM) search and statistical queries, and pivot to individual managed tenants. By following this method, you eliminate the need to sign in to each tenant individually and centralize visibility across distributed environments. This reduces operational overhead and accelerates cross-tenant threat detection and incident response.

Federated Search is built directly into the existing UDM **Search** page (**Investigation > Search**) rather than a separate navigation page. It connects a designated _managing instance_ to multiple _managed instances_ using your existing Google Cloud Identity and Access Management (IAM) configurations. 

When you sign in to a managing instance with linked subtenants and the required federation IAM role, an **Instances** menu appears on the **Search** page (this menu doesn't appear on standard single-tenant instances). When you select target instances or groups from this menu and initiate a search query, Google verifies your authorization across all targeted instances, distributes the query, and returns a unified view of matching events and aggregated statistics tagged by source instance code.

## Key terminology

The following terms apply to Federated Search and multi-tenant operations:

  * **Managing instance** : The central Google SecOps instance with the required permissions to manage linked instances, organize federation groups, and execute federated searches.
  * **Managed instances** : Connected Google SecOps instances that respond to federation requests initiated from the managing instance.
  * **Instances menu** : The drop-down selector in **Investigation > Search** that lets you choose which linked managed instances or instance groups to include in a federated search. This menu only appears when you sign in to a managing instance that has linked subtenants under **SIEM settings > Linked Instances** and your account has the `chronicle.googleapis.com/federationAdmin` or `chronicle.googleapis.com/federationViewer` role.
  * **Instance code** : The unique identifier assigned to each managed instance (`instance_code`) that tags returned events and aggregated statistical rows in federated search results.
  * **Federation administrator** : The IAM role (`chronicle.googleapis.com/federationAdmin`) required on the managing instance project to create federation groups and perform federated searches.
  * **Federation viewer** : The IAM role (`chronicle.googleapis.com/federationViewer`) that grants read-only access to view federation configurations and run federated searches without creating or deleting groups.
  * **Federated stats** : UDM-based statistical aggregation queries (such as `count` or `sum`) executed across multiple managed instances, where results are implicitly grouped and isolated by `instance_code`.



## Common use cases

The following sections describe how Federated Search addresses multi-tenant data silos and operational overhead across core security workflows.

### Cross-tenant threat hunting across data silos

  * **Objective** : Execute a single YARA-L query across multiple customer or subsidiary instances simultaneously to detect indicators of compromise (IOCs) and internet-wide threats.
  * **Value** : Eliminates the need to sign in to individual tenants, providing centralized visibility across organizational boundaries and regional compliance silos.



### Incident response and triage across instance groups

  * **Objective** : Organize customer tenants with similar threat profiles (for example, financial institutions) into logical instance groups and run targeted searches or statistical aggregations across those groups.
  * **Value** : Reduces investigation time and management overhead by scoping threat hunts to specific customer segments and identifying which tenants require immediate remediation.



### Collaborative sharing of findings with tenant administrators

  * **Objective** : Pivot directly from federated search results in the managing instance to an individual managed tenant's interface and share specific findings with that tenant's local administrator.
  * **Value** : Streamlines handoffs between central MSSP analysts and local customer security teams while preserving tenant-level data isolation.



## Before you begin

Before you configure instance groups or run federated searches, confirm that the following prerequisites are met:

  * **Permissions** : From the Google Cloud project associated with your managing instance, assign one of the following IAM roles to users:

    * `chronicle.googleapis.com/federationAdmin` (federation administrator): Grants full access to all Federated Search features, including creating and deleting instance groups.
    * `chronicle.googleapis.com/federationViewer` (federation viewer): Grants read-only access to view federation configurations and execute federated searches without modifying groups.
    * Users must also have the `chronicle.events.udmSearch` permission to run UDM searches across managed tenants.
  * **Environment check** :

    * **Regional scope** : All participating Google SecOps instances (managing and managed) must reside in the same Google Cloud region.
    * **Organizational hierarchy** : All participating instances must belong to the same Google Cloud organization. Each managed instance must reside in a subfolder of the managing instance's Google Cloud folder (if the managing instance's project isn't part of any Google Cloud folder, it can manage all instances within the same Google Cloud organization).
    * **Access control enforcement** : Federated Search respects the data role-based access control (RBAC) settings configured on each subtenant. Users can only access data permitted by their assigned roles.



### Limitations

Federated Search supports basic YARA-L queries and UDM statistical aggregations and enforces the following functional boundaries:

  * **Unsupported single-tenant search features** :

    * Raw log search (both legacy and RLSv2)
    * Entity Context Graph (ECG) search
    * YARA-L 2.0 query generation with Gemini and Gemini summary
    * UDM lookup
    * Tenants using customer-managed encryption keys (CMEK)
    * Tenant ID filters with **Apply to search and run**
    * The **Manage parser** pivot from the **Event viewer** panel
    * Reference lists and data tables
    * Legacy views for entities and pivoting to legacy views from the **Overview** panel in UDM search
    * **Overview** tab and **Alerts** tab
    * Ordering of results and downloading results as comma-separated values (CSV)
    * Pivoting in the **Events** table
    * API-based federated searches (Federated Search isn't supported in the Chronicle API)
  * **Federated stats restrictions** :

    * **No cross-tenant merging** : You can't aggregate data from multiple tenants into a single global number. Each statistical result remains isolated to its specific tenant (for example, you see 10 rows for 10 tenants, not 1 row representing the sum of all 10).
    * **No support for joins, data tables, or multi-stage queries** : Queries using joins, multi-stage queries, or data tables aren't supported.
    * **Scope** : Federated stats are strictly limited to UDM events. ECG events aren't supported.
    * **Visualization** : The **Visualize** tab (graphs and charts) is disabled. Results are provided in a tabular data format only.



## Configure and manage federated search groups

Within your managing instance, you can view linked tenants and organize them into logical instance groups to manage customers with similar threat profiles. The following sections explain how to view linked instances and manage groups.

### View linked instances

Verify that your managed tenants are linked and visible to the managing instance before creating groups or running searches:

  1. Sign in to your managing Google SecOps instance.
  2. Go to **SIEM settings > Linked Instances**.
  3. Review the table of linked instances, which displays the following details for each tenant:

     * **Name** : Display name of the instance.
     * **ID** : Instance ID.
     * **Code** : Unique identifier code assigned to the instance, which appears in federated search results.
     * **Groups** : Instance groups assigned for management.
**Caution:** Federated search instances automatically appear in the **Linked Instances** list within 5 minutes after you create a new tenant or move an existing tenant into a folder scoped for federation. If a tenant is missing after 5 minutes, verify that it resides in the same Google Cloud region and within a subfolder of the managing instance's Google Cloud folder.



### Create a federated search group

Create logical instance groups (for example, grouping banks and credit unions) to run targeted federated searches across specific customer segments:

  1. Sign in to your managing Google SecOps instance.
  2. Click **SIEM settings > Linked Instances**.
  3. Click **Manage Groups**.
  4. Click **Add**.
  5. In the **Group name** field, enter a descriptive name for the group.
  6. In the **Assign to instances** list, select the managed instances to include in the group.
  7. Click **Save**.

**Note:** You can create a maximum of 100 instance groups per tenant. If the **Add** button is unavailable or saving fails, verify that your account is assigned the `chronicle.googleapis.com/federationAdmin` role on the managing instance project.



## Run a federated search across multiple instances

You can execute YARA-L queries from your managing instance to search events and inspect aggregated UDM statistics across selected tenants. The following sections explain how to run federated queries and analyze results.

### Execute a cross-tenant UDM search

Run a federated search to retrieve matching UDM events across multiple managed instances or instance groups:

  1. Sign in to your managing instance. Make sure that your account has access to the managing instance and all associated managed instances.
  2. In the navigation bar, click **Investigation > Search**.
  3. Click **Instances** (which appears on the **Search** page on managing instances configured for federation) and select the individual instances or instance groups to include in your search.
  4. In the search field, enter a YARA-L query and click **Run Search**.
  5. Configure result limits as needed:

     * The total number of results returned in a federated search is determined by the result set size configured in your [Search settings](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#search_settings) (default is 30,000; configurable between 1 and 1,000,000).
     * You can also configure the `limit` keyword in a search query, which applies to each targeted instance individually:
           
           ip != "" limit:5000
           

If you select 10 instances, this query fetches up to 5,000 events from each instance, returning up to 50,000 events in total.

  6. Monitor query execution in the **Results summary** menu, which displays status indicators (**Running** , **Completed** , or **Failed**) for each targeted instance.

  7. Filter and inspect results by instance code:

     * Each event in the search results includes a **Tenant** (or **instance code**) column identifying the source managed instance.
     * Use the **Tenant filter** in the sidebar or snapshot view to narrow results to a specific tenant.
     * Click any listed event to view the full UDM event and raw log.
**Note:** Each federated query can target a maximum of 150 instances and search a maximum time range of 30 days. Exceeding the organization rate limit of 30 federated search queries per hour returns an `HTTP 409` error. If a query fails with a compilation error, verify that the query doesn't include unsupported single-tenant features such as joins, data tables, or reference lists.



### Analyze federated stats and pivot to managed instances

Run statistical UDM queries (such as `count` or `sum`) across multiple instances to validate threat hypotheses and drill down into specific tenants:

  1. In the navigation bar on your managing instance, click **Investigation > Search** and select your target instances or groups from the **Instances** menu.
  2. Enter a UDM statistical query (using `match` and `outcome` sections) and click **Run Search**.

     * The federated query engine orchestrates the aggregation across all targeted instances and implicitly groups results by `instance_code`.
  3. Review the per-instance aggregated rows in the tabular results view.

  4. To investigate a specific tenant's events in detail, choose one of the following pivot actions:

     * Click **Run UDM query** on any statistical result row to initiate the underlying search directly on the associated managed instance in a new browser tab.
     * In the **Results summary** menu, click open_in_new **Open in new tab** next to an instance row to open a new browser tab showing only that instance's search results.
  5. Click **Done** when you finish reviewing your search results.

**Note:** Aggregations are performed at the instance level and are capped at 60,000 rows. Because cross-tenant merging and the **Visualize** tab are disabled in Federated Search, pivoting to a specific tenant using **Run UDM query** lets you access single-tenant visualizations, CSV export, and deeper event inspection while preserving your original federated results tab.



## Examples and reference information

The following sections provide sample YARA-L queries and multi-tenant investigation examples to streamline cross-tenant threat hunting and incident response.

### Track user login activity across instance groups

A security analyst wants to search for all `USER_LOGIN` events across the **New York** and **California** instance groups:

  1. In the managing instance navigation bar, click **Investigation > Search**.
  2. Click **Instances** and select the **New York** and **California** instance groups.
  3. In the search field, enter the following UDM query:
         
         metadata.event_type = "USER_LOGIN"
         

  4. Click **Run Search**.

  5. View the results in the **Results summary** :

     * Each event includes a **Tenant** column showing the source instance code and all `USER_LOGIN` events found in the selected tenants.
     * Use the **Tenant filter** in the sidebar to narrow the results to a specific tenant within the selected groups.
     * The summary displays the number of `USER_LOGIN` events per tenant in the **New York** and **California** instance groups.



### Investigate a suspicious executable across tenants

An incident responder for a multi-tenant customer wants to investigate an alert for a suspicious executable (`malicious.exe`) on **instance1** :

  1. In **Investigation > Search** on **instance1** , run the following UDM query to validate the results:
         
         metadata.event_type = "FILE_OPEN" AND target.file.full_path = "<var>FILE_PATH</var>/malicious.exe"
         

  2. Once validated, open the managing instance, go to **Investigation > Search**, and select all relevant instances using the **Instances** menu.

  3. Rerun the same query using Federated Search to scan across the selected instances.

  4. The results summary displays the results for all tenant instances. Each event includes an instance code, letting the responder identify where and when `malicious.exe` was accessed across all tenants.




### Identify anomalous login behavior with federated stats

The following example helps identify anomalous login behavior, including logins from unusual geographic locations and logins occurring at atypical times across all federated instances:

  1. In **Investigation > Search** on **instance1** , run the following UDM query to validate the results:
         
         // Filter for successful logins
         metadata.event_type = "USER_LOGIN"
         security_result.action = "ALLOW"
         
         $user = target.user.userid
         $machine = target.hostname
         $ip = principal.ip
         $country = principal.ip_geo_artifact.location.country_or_region
         
         // Match: Group by Machine
         match: $machine
         
         // Check for affected scope: How many unique IPs hit this machine?
         // Check for logins from multiple countries
         // Identify the time window of activity
         outcome:
           $total_logins = count(metadata.id)
           $unique_users = count_distinct($user)
           $unique_source_ips = count_distinct($ip)
           $distinct_countries = count_distinct($country)
           $first_login = min(metadata.event_timestamp.seconds)
           $last_login = max(metadata.event_timestamp.seconds)
         
         // Identify machines with the most unique users
         order: $unique_users desc
         

  2. Once validated, open the managing instance, go to **Investigation > Search**, and select all relevant instances using the **Instances** menu.

  3. Rerun the same query using Federated Search to scan across the selected instances.

  4. The results summary displays the results for all tenant instances. Each row includes an instance code, informing the threat hunter of login anomalies on each instance.

  5. Focus on a specific instance by clicking **Run UDM query** to complete a deeper investigation of suspicious behavior.




### Share findings with a tenant administrator

This example shows how an investigator isolates findings from a cross-tenant search to a single managed tenant before sharing them with that tenant's local administrator. Because federated search results in the managing instance span multiple tenants, you pivot to the specific managed instance (**instance2**) to share only the search query and events relevant to that customer:

  1. In the **Results summary** on your managing instance, locate the matches for **instance2**.
  2. Click open_in_new **Open in new tab** next to **instance2** to open the search results in that tenant's Google SecOps interface in a new browser tab.
  3. From the **instance2** page, confirm that the search results are scoped exclusively to that instance.
  4. Click **Share** or **Save** to perform one of the following actions:

     * Share the search (query and results) with local users who have access to **instance2**.
     * Save the search query in **instance2** for future use or investigation.



## Troubleshooting

The following sections outline architectural limits, expected latency, and self-service fixes for common Federated Search issues.

### Latency, service quotas, and limits

Federated Search enforces the following service quotas and processing limits to maintain performance across multi-tenant environments:

  * **Tenant discovery latency** : Newly created or moved instances automatically appear in the **Linked Instances** list within 5 minutes after being placed in a folder scoped for federation.
  * **Instance limit** : Each federated search query can target a maximum of 150 instances.
  * **Group limit** : You can create a maximum of 100 instance groups per tenant.
  * **Query rate limit** : You can run a maximum of 30 federated search queries per hour per Google Cloud organization. Exceeding this limit returns an `HTTP 409` error.
  * **Query result limit** : A federated search returns a maximum of 1,000,000 rows of results, divided evenly across the total number of Google SecOps tenants targeted by the query.
  * **Federated stats result limit** : Federated stats queries return a maximum of 60,000 rows in tabular format.
  * **Query time range** : Each federated search query can search a maximum time window of 30 days.



### Error remediation

Use the following table to diagnose and resolve common Federated Search issues:

Issue or error code | Description | Actionable fix  
---|---|---  
`HTTP 409` | **Query rate limit exceeded** : The organization has exceeded the maximum of 30 federated search queries per hour. | Wait for the hourly quota window to reset before running additional federated searches, or run targeted queries directly on individual managed instances.  
Missing tenant in **Linked Instances** | **Tenant not visible in federation list** : A newly created or moved instance doesn't appear under **SIEM settings > Linked Instances**. | Wait up to 5 minutes for automatic discovery sync. If the instance remains missing, verify that it resides in the same Google Cloud organization and region and is located in a subfolder of the managing instance's Google Cloud folder.  
Permission denied or unauthorized | **Unable to run federated query or manage groups** : You can't access the managing instance, create groups, or query a managed tenant. | Verify that your account has `chronicle.googleapis.com/federationAdmin` (or `federationViewer`) on the managing project, `chronicle.events.udmSearch` permission, and data RBAC access on each targeted subtenant.  
Query compilation error | **Unsupported query syntax** : Query fails when attempting to use joins, data tables, reference lists, or ECG fields. | Remove joins, data tables, reference lists, and ECG references from the federated query, or pivot to a single-tenant instance using **Run UDM query** to execute advanced single-tenant searches.  
  
### Validation and testing

Before running a complex YARA-L search or statistical query across up to 150 managed instances, validate the query syntax and field mappings on a single instance first:

  1. Go to **Investigation > Search** on a single managed instance (for example, **instance1**) and run your YARA-L query over a short time range.
  2. Confirm that the UDM fields, event types, and statistical outcome variables compile cleanly and return expected results.
  3. After validating the query on a single instance, go to **Investigation > Search** on the managing instance, select your target instance groups in the **Instances** menu, and execute the validated query across all managed tenants.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
