---
url: https://docs.cloud.google.com/chronicle/docs/administration/datarbac-impact/
title: Data RBAC impact on features overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:12.873519+00:00
---

# Data RBAC impact on features overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/datarbac-impact/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data RBAC impact on features overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

_Data role-based access control_ (_data RBAC_) is a security model that restricts user access to data based on individual user roles within an organization. After data RBAC is configured in an environment, you start seeing filtered data in Google Security Operations features. Data RBAC controls user access according to their assigned scopes and ensures that users can access only authorized information. This page gives an overview of how data RBAC impacts each Google SecOps feature.

To understand how data RBAC works, see [Data RBAC overview](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview).

**Important:** Data RBAC applies only to the SIEM side. Your data may still be visible on the SOAR side; therefore, ensure that appropriate access controls are in place.

## Search

The data returned in search results is based on the user's data access scopes. Users can only see results from data that matches the scopes that are assigned to them. If users have more than one assigned scope, then the search is executed across the combined data of all the authorized scopes. Data belonging to scopes that the user doesn't have access to does not appear in search results.

**Note:** Users or service accounts that need access to global scope data, must have `chronicle.globalDataAccessScopes.permit` permission.

### Cases access

Cases and case history search in SIEM Search don't support Data RBAC scopes. A user with permissions to perform SIEM Search can search for cases and case history across all data scopes.

## Rules

Rules are detection mechanisms that analyze the ingested data and help identify potential security threats. Rules can be categorized as follows:

  * **Scoped rules** : associated with a specific data scope. Scoped rules can only operate on data that falls within that scope's definition. Users with access to a scope can view and manage its rules.

  * **Global rules** : with broader visibility, these rules and can operate on data across all scopes. To maintain security and control, only users with global scope can view and create global rules.




Alert generation is restricted to events that match the rule's scope. If a rule has no assigned scope, it runs in the global scope and applies to all data.

Data RBAC impacts rules in the following ways:

  * **Data RBAC is enabled _before_ assigning scopes to rules:** all existing rules are automatically assigned global scope. Assign scopes to each rule according to your data access control requirement.

  * **Data RBAC is enabled _after_ assigning scopes to rules**: scoped rules operate on ingested data according to their defined scopes, even before data RBAC is enabled. This allows users to see detections that were generated after the scope assignments.




The scope that is associated with a rule determines how [global and scoped users](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#user-roles) can interact with it. The access permissions are summarized in the following table:

Action  | Global user  | Scoped user   
---|---|---  
Can view scoped rules  | Yes  | Yes (only if the rule's scope is within the user's assigned scopes)  For example, a user with scopes A and B can see a rule with scope A, but not a rule with scope C.  
Can view global rules  | Yes  | No   
Can create and update scoped rules  | Yes  | Yes (only if the rule's scope is within the user's assigned scopes)  For example, a user with scopes A and B can create a rule with scope A, but not a rule with scope C.  
Can create and update global rules  | Yes  | No   
  
## Detections

Detections are alerts that signify potential security threats. Detections are triggered by custom rules, which are created by your security team for your Google SecOps environment.

Detections are generated when incoming security data matches the criteria defined in a rule. Before data RBAC is enabled, all users have visibility into all detections, regardless of any scope tagging. After data RBAC is enabled, users can only see detections that originate from rules associated with their assigned scopes.

For example, a security analyst with the finance data scope only sees detections generated by rules assigned to the finance data scope, and doesn't see detections from any other rules.

The actions that a user can take on a detection (for example, marking a detection as resolved) are also limited to the scope in which the detection occurred.

## Curated detections

Detections are triggered by custom rules that are created by your security team whereas curated detections are triggered by rules provided by the Google Cloud Threat Intelligence (GCTI) team. As part of the curated detections, GCTI provides and manages a set of YARA-L rules to help you identify common security threats within your Google SecOps environment. For more information, see [Use curated detections to identify threats](https://docs.cloud.google.com/chronicle/docs/detection/curated-detections).

Curated detections don't support data RBAC. Only users with [global scope](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#user-roles) can access curated detections.

## Impact of data RBAC on first-party cases and alerts

This section summarizes how to configure data RBAC for first-party alerts and cases within Google Security Operations.

Key topics include:

  * **Prerequisites** : Requirements for unified SIEM and SOAR instances, connector compatibility, and the implications of irreversible feature enablement.
  * **Enablement** : Configuration steps for enabling data access enforcement for both existing and new SIEM enforcement scenarios.
  * **Environment mapping** : Instructions for establishing data boundaries by mapping defined SIEM scopes to SOAR environments.
  * **Access evaluation** : Explanations of scope propagation, access logic, and rules governing entity and case grouping.
  * **Lifecycle management** : Guidelines for modifying environment mappings, creating manual cases, handling overflow scenarios, and addressing scope deletions.
  * **Interface monitoring** : How to verify and filter data access scopes within the Case Management UI.



For more information, see [Control access to 1P cases and alerts](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-impact-cases).

## Triage Agent

The Triage Agent is an AI-powered assistant embedded in Google Security Operations. It investigates security alerts to determine whether they are true or false positives and provides a summarized explanation for its assessment.

When data RBAC is enabled, only users with global data access can trigger and view Triage Agent investigations. For more information, see [User roles](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#user-roles).

## Raw logs

With data RBAC enabled, unparsed raw logs are accessible only to users with global scope.

## Data tables

Data tables are multicolumn data constructs that let you input your own data into Google SecOps. They can act as lookup tables with defined columns and the data stored in rows. By assigning scopes to a data table, you can control which users and resources can access and utilize it.

### Access permissions for users in data tables

The scopes that are associated with a data table determine how [global and scoped users](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#user-roles) can interact with it. The access permissions are summarized in the following table:

Action  | Global user  | Scoped user   
---|---|---  
Can create scoped data table  | Yes  | Yes (only with scopes that match or are a subset of their assigned scopes)  
For example, scoped user with scopes A and B can create a data table with scope A or with scopes A and B, but not with scopes A, B, and C.  
Can create unscoped data table  | Yes  | No   
Can update scoped data table  | Yes  | Yes (only with scopes that match or are a subset of their assigned scopes)  
For example, a user with scopes A and B can modify a data table with scope A or with scopes A and B, but not a data table with scopes A, B, and C.  
Can update unscoped data table  | Yes  | No   
Can update scoped data table to unscoped  | Yes  | No   
Can view and use scoped data table  | Yes  | Yes (if there's at least one matching scope between the user and the data table)  
For example, a user with scopes A and B can use a data table with scopes A and B, but not a data table with scopes C and D.  
Can view and use unscoped data table  | Yes  | Yes   
Can run search queries with unscoped data tables  | Yes  | Yes   
Can run search queries with scoped data tables  | Yes  | Yes (if there's at least one matching scope between the user and the data table)  
For example, a user with scope A can run search queries with data tables with scopes A, B, and C, but not with data tables with scopes B and C.  
  
## Reference lists

Reference lists are collections of values that are used for matching and filtering data in UDM Search and detection rules. Assigning scopes to a reference list (scoped list) restricts its access to specific users and resources such as rules and UDM search. A reference list that has no scope assigned is called an unscoped list.

### Access permissions for users in reference lists

The scopes that are associated with a reference list determine how [global and scoped users](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#user-roles) can interact with it. The access permissions are summarized in the following table:

Action  | Global user  | Scoped user   
---|---|---  
Can create scoped list  | Yes  | Yes (with scopes that match their assigned scopes or are a subset of their assigned scopes)  For example, scoped user with scopes A and B can create a reference list with scope A or with scopes A and B, but not with scopes A, B, and C.  
Can create unscoped list  | Yes  | No   
Can update scoped list  | Yes  | Yes (with scopes that match their assigned scopes or are a subset of their assigned scopes)  For example, a user with scopes A and B can modify a reference list with scope A or with scopes A and B, but not a reference list with scopes A, B, and C.  
Can update unscoped list  | Yes  | No   
Can update scoped list to unscoped  | Yes  | No   
Can view and use scoped list  | Yes  | Yes (if there is at least one matching scope between the user and the reference list)  For example, a user with scopes A and B can use a reference list with scopes A and B, but not a reference list with scopes C and D.  
Can view and use unscoped list  | Yes  | Yes   
Can run UDM search and dashboard queries with unscoped reference lists  | Yes  | Yes   
Can run UDM search and dashboard queries with scoped reference lists  | Yes  | Yes (if there is at least one matching scope between the user and the reference list)  For example, a user with scope A can run UDM search queries with reference lists with scopes A, B, and C, but not with reference lists with scopes B and C.  
  
### Access permissions for rules in reference lists

A scoped rule can use a reference list if there is at least one matching scope between the rule and the reference list. For example, a rule with scope A can use a reference list with scopes A, B, and C, but not a reference list with scopes B and C.

A rule with global scope can use any reference list.

## Feeds and forwarders

Data RBAC doesn't directly affect the feed and forwarder execution. However, during their configuration, users can assign the default labels (log type, namespace, or ingestion labels) to the incoming data. Data RBAC is then applied to features using this labeled data.

## Dashboards

Use Dashboards to build visualizations across various data sources. Each dashboard is composed of different charts.

Dashboards fully support data RBAC. This security model filters the information displayed in dashboard widgets based on your assigned scopes.

  * **Data visibility** : Widgets only display results from data that matches your assigned scopes. If a dashboard relies on a YARA-L query, that query only executes against authorized data.
  * **Scope overlap** : If you have multiple scopes, the dashboard displays the combined data from all authorized scopes.
  * **Access control** : While feature RBAC determines who can create or edit a dashboard, data RBAC determines what specific data is visible within the charts and tables.



The specific scope associated with a dashboard determines the level of interaction permitted for [global and scoped users](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#user-roles):

  * **Global users** : Maintain full visibility and management capabilities across all dashboards, regardless of scope.

  * **Scoped users** : Interaction is restricted based on the user's assigned scopes.


**Note:** While Dashboards support data RBAC, looker-based dashboards rely solely on feature-based RBAC.

### Case access

Dashboards with SOAR data, such as Cases, Case history, Playbooks and Alerts, are only visible to global users.

## Applied Threat Intelligence and IOC matches

IOCs and Advanced Threat Intelligence (ATI) data provide critical information about potential security threats within your environment.

ATI curated detections are triggered by rules provided by the ATI team. These rules use Mandiant threat intelligence to proactively identify high-priority threats. For more information, see [Applied Threat Intelligence overview](https://docs.cloud.google.com/chronicle/docs/detection).

IOC matches and ATI data derived from customer logs require global scope for visibility and aren't available to users with restricted scopes.

## User and Entity Behavior Analytics (UEBA)

The Risk Analytics for UEBA category offers prebuilt rule sets to detect potential security threats. These rule sets use machine learning to proactively trigger detections by analyzing user and entity behavior patterns. For more information, see [Overview of Risk Analytics for UEBA category](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-ueba-category).

UEBA does not support data RBAC. Only users with [global scope](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#user-roles) can access the risk analytics for UEBA category.

## Entity details across Google SecOps

The following fields, which describe an asset or a user, appear on multiple pages in Google SecOps, such as the **Entity Context** panel in UDM Search. With data RBAC, the fields are available only to the users with [global scope](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#user-roles).

  * First seen
  * Last seen
  * Prevalence



Scoped users can view the first seen and last seen data of users and assets if the first seen and last seen is calculated from data within the user's assigned scopes.

## What's next

[Configure data RBAC for users](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
