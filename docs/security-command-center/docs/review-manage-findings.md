---
url: https://docs.cloud.google.com/security-command-center/docs/review-manage-findings/
title: Review and manage findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:18.041444+00:00
---

# Review and manage findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/review-manage-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Review and manage findings Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to work with Security Command Center _findings_. A finding is a record that Security Command Center services create when they detect a security issue. Findings are listed in the **Findings** page. You can click a finding to see its details and full JSON format.

Some of the actions that you can perform on the **Findings** page include the following:

  * Query findings.
  * Inspect findings.
  * Mute findings.
  * Add security marks to findings.



For information about working with findings programmatically, see [Security Command Center client libraries](https://docs.cloud.google.com/security-command-center/docs/reference/libraries).

**Note** : The **Findings** page doesn't show threat detections and alerts created by [curated detections](https://docs.cloud.google.com/security-command-center/docs/investigate-threat-findings). To view these detections and alerts in the Security Operations console, go to **SIEM Dashboards**. For more information about this console page, see [Security Operations console](https://docs.cloud.google.com/security-command-center/docs/scce-consoles-overview#secops-console). 

## Obtain the required permissions

This section lists the IAM roles that you need to work with findings in the console.

### Google Cloud console IAM roles

To work with findings in the Google Cloud console, you need the following IAM roles.

Make sure that you have the following role or roles on the organization: 

  * **Security Center Findings Viewer** (`roles/securitycenter.findingsViewer`) 
  * **Security Center Findings Editor** (`roles/securitycenter.findingsEditor`) 



#### Check for the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
  2. Select the organization. 
  3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

  4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 



#### Grant the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
  2. Select the organization. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

  5. Click **Select a role** , then search for the role. 
  6. To grant additional roles, click add **Add another role** and add each additional role. 
  7. Click **Save**. 



For more information about Security Command Center roles and permissions, see [IAM for organization-level activations](https://docs.cloud.google.com/security-command-center/docs/access-control-org).

## View findings

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled for your organization, you must access the page using the jurisdictional console. For more information, see [Use the console with data residency enabled](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#console-jconsole).

  2. Select your Google Cloud organization, folder, or project.

The findings displayed are associated with resources in the organization, folder, or project that you select. For example, selecting a project shows only findings that are associated with that project, whereas selecting a folder with multiple projects shows findings for all projects in the folder.

  3. To update the list of findings in the **Findings query results** , click autorenew**Refresh findings**.




## Adjust the time range to view more findings

You can adjust the time range that is used for your queries. The default time range is `Last 7 days`.

The time range is based on the value of the `eventTime` attribute of the findings, which reflects the time at which the finding record was last updated. For information about changes that update the event time, see [Overview of the finding lifecycle](https://docs.cloud.google.com/security-command-center/docs/finding-lifecycle-overview).

On the **Findings** page in the Google Cloud console, set the **Time range** field.

## Finding availability

A finding usually becomes available for you to query in Security Command Center less than a minute after the service that generates the finding stores it in the Security Command Center findings database. For more detailed information about what happens after you activate Security Command Center, see [When to expect findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview).

Depending on your Security Command Center tier, findings remain available for you to list or query for specific periods of time. For more information about Security Command Center data retention, see [Data retention](https://docs.cloud.google.com/security-command-center/docs/concepts-data-security-overview#data_retention).

## Find and view specific findings

By default, the **Findings** page displays all active findings that are not muted and that are either new or updated over the last seven days. To display inactive or muted findings, select **Inactive** or **Muted** in the **Quick filters** panel.

### Use predefined filter views

To display a specific category of findings, click the following predefined filter views that return a specific category of findings:

  * Standard-legacy tier: **All Findings** , **Vulnerabilities** , and **Identity**
  * Standard tier: **All Findings** , **Vulnerabilities** , **Identity** , **Data** , and **Threats**
  * Premium tier: **All Findings** , **Vulnerabilities** , **Identity** , **Data** , and **Threats**
  * Enterprise tier: **All Findings** , **Vulnerabilities** , **Identity** , **Threats** , and **Data**



The view applies, and runs, the predefined query.

In Security Command Center Enterprise, click **Showing all** to filter results by cloud provider: Google Cloud, Amazon Web Services (AWS), or Microsoft Azure. For information about setting up a connection to other cloud providers, see the following:

  * [Connect to AWS for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws)
  * [Connect to Microsoft Azure for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure)



### Use the query editor

This section describes the different ways you can customize the findings query in the Google Cloud console to filter for specific findings.

The following example is the default findings query:
    
    
    state="ACTIVE"
    AND NOT mute="MUTED"
    AND launch_state="LAUNCH_STATE_DEPRECATED"

For information about findings with the `launch_state` field set to `LAUNCH_STATE_DEPRECATED`, see [Standard tier enhanced and automatically activated for some customers](https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy#sha-gcse-migration).

You can see the current findings query in the **Query editor** panel. You can edit the query directly or select predefined filters to build the query. For more information, click the tab for your service tier.

On the **Findings** page in the Google Cloud console, you can do the following:

  * In the **Quick filters** panel, select one or more predefined attribute filters to add them to a query. Use the **Quick filters** panel for commonly used, high-level filter options.
  * In the **Add filter** menu of the **Query editor** panel, select one or more of the predefined attribute filters to add them to a query. Use the **Add filter** menu for more granular and advanced filters that are based on lower-level finding attributes. For more information, see [Edit a findings query in the console](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console).
  * Edit the findings query directly in the **Query editor** panel.
  * In the detail view of a finding, from the drop-down menu for a particular attribute, select a predefined filter for that attribute to add it to a query.



## View the details of a finding

To learn more about a finding, open the detailed view of the finding by clicking the finding name in the **Category** column in the findings query results.

In the detail view, you can find information that is critical for understanding a finding, investigating a threat, or addressing a vulnerability.

The detail view for findings includes the following tabs that you can select to learn more about a finding and take action:

  * The **Summary** tab, which is the default view, highlights key information and attributes about the finding.
  * The **Source properties** tab, where you can see the attributes of the `sourceProperties` object of the finding JSON.
  * The **JSON** tab, where you can see the full JSON format of the finding.



You can take certain actions on the finding in the detail view, as well as find links to additional information that is related to the finding.

### Learn about the finding in the detail view

The detail view of a finding highlights important information about the finding that you can use to understand and address the underlying security issue.

#### Information on the **Summary** tab

The **Summary** tab provides information about the finding in the following sections:

What was detected (or Overview)
    

Details about the finding that was detected, such as the following:

  * The finding severity
  * The finding state, `ACTIVE` or `INACTIVE`
  * Any key fields that are related to the specific finding


Vulnerability
    

Information from the CVE record that corresponds to the vulnerability, if any. The **Vulnerability** section includes information from the CVE record, such as:

  * CVE ID
  * CVE score
  * Impact
  * Exploitation activity


Attack exposure
    

The [attack exposure score](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_exposure_scores) and the time at which the score was last calculated. Clicking the score opens a visual depiction of the affected high-value resources and the associated attack path.

Affected resource
    

Details about the resource that is associated with the finding, including the following information:

  * The full name of the affected resource
  * The cloud service provider of the resource
  * The technical and security contacts


Case information
    

Details about the case that is associated with the finding, including the following information.

  * The full resource name of the external system that is associated with the finding
  * The group assigned to the case
  * The case ID, which links to the case in the Security Operations console
  * The status of the case
  * The update time in the external case management system
  * The committed deadline for closing the case


Security marks
    

Any [security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings) that apply to this finding.

Next steps
    

Guidance on what you can do to remediate the issue detected. Only certain services, such as [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors), provide next steps.

Related links
    

Links to key sources of security information outside of Security Command Center. Only certain services, such as [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), provide related links.

Detection service
    

Details about the service, or _source_ , that detected the finding.

#### Information on the **Source properties** tab

For some findings, the details panel includes a **Source properties** tab that highlights certain properties from the `sourceProperties` object of the finding JSON.

Source properties differ for each finding and for each service that runs on Security Command Center. There's no assurance that source properties are standardized across all services. For this reason, we strongly discourage consuming source properties programmatically. If you want a source property to be standardized across all services, let us know by sending your feedback.

#### Information on the **JSON** tab

The **JSON** tab contains the complete JSON structure of the finding, which can be useful when you're investigating a finding or looking up attributes that you can use in your findings queries.

To copy the JSON object to your clipboard, click content_copy **Copy**.

The JSON structure of a finding contains the following objects:

  * `findings`: The finding's attributes. These attributes are standardized across all built-in and integrated services (also known as _security sources_). For more information, see [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#resource:-finding).
  * `resource`: The attributes of the affected resource. For more information, see [`Resource`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/ListFindingsResponse#resource).
  * `sourceProperties`: The service-specific properties of the finding.



You can also use the [`ListFindings` API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings) to list findings and get their JSON definitions.

### Some findings are missing information

Because Security Command Center aggregates findings from multiple Google Cloud services, third-party integrations, and custom modules, the information that is included in a finding can vary. You might see findings where standard fields are blank or marked as `Unspecified`. 

The following list identifies common fields and explains why they might be missing: 

  * **Project ID:** findings are attached to the resource hierarchy level where the security issue was detected. If an issue is detected at the organization or folder level (for example, an organization-level Identity and Access Management (IAM) policy violation), then the finding is tied directly to that organization or folder and has no associated project ID. 
  * **Severity:** the service that detects the issue determines the finding's severity. If a third-party security source or a custom module generates a finding but doesn't assign a severity level, then Security Command Center displays the severity as `Unspecified`. 
  * **Resource type:** Security Command Center identifies the resource type by correlating the finding's resource name with Cloud Asset Inventory. If the resource isn't supported by Cloud Asset Inventory, or if a third-party provider supplies an unrecognized resource name, then the resource type can't be resolved and remains blank. 
  * **Cloud service provider:** indicates whether the affected resource is in Google Cloud, Amazon Web Services (AWS), or Microsoft Azure. This field might remain blank for findings that are generated by deprecated Security Health Analytics detectors (`LAUNCH_STATE_DEPRECATED`), custom sources, or third-party integrations that don't specify an environment. 



### View findings for resources registered with an application

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Do the following to filter and display findings related to a resource that is registered to an [App Hub application](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#apphub-integration).

  * Use the **Select app** menu to select an application. This appends the query with a term to display only findings related to that application.

  * In the **Quick filters** panel, select one or more applications in the **App ID** section.




When you select a finding, the **Finding detail** panel displays the information about the application that the resource is registered to.

### Take action on a finding from the detail view

You can take a variety of actions on a finding from the finding's detail view, such as mute the finding. If you are viewing the finding's detail view in the Google Cloud console, you can also add attributes from the finding to the current findings query.

#### Mute a finding in the detail view

From the detail view of a finding, you can mute or unmute the finding. You can also create a rule that mutes all future findings like the current finding.

For complete instructions for muting a finding or creating a mute rule, see [Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

#### Add attribute filters to a query from the detail view

In the Google Cloud console, in the detail view of a finding, you can add filters for the displayed attributes to the current findings query.

To add attribute filters to a query from the detail view:

  * On the **Findings** page, click the finding to view its details.
  * In the detail view of the finding, find the attribute that you want to filter on.
  * Next to the attribute, open the drop-down menu.
  * Select a predefined filter for the attribute. The filter is added to the findings query on the **Findings** page.



#### View or copy attribute API names in the detail view of a finding

Most finding attributes that are displayed in the Google Cloud console have a corresponding name that is used in the Security Command Center API.

  1. On the **Findings** page, click the finding to view its details.

  2. In the detail view of the finding, you can find and copy the corresponding API name of each attribute that is displayed.

The equivalent API name for each attribute is listed in the same row as the attribute. All API names are in the last column. For example, for the **State** attribute, the equivalent API name is `state`.




#### Share the detail view of a finding

To share the detail view of a finding, you can copy the URL of the detail view page for sharing with others.

For information about how to copy the URL of the detail view of a finding, click the tab for the console that you are using.

  1. On the **Findings** page, click the finding to view its details.
  2. Click **Take action > Copy link**.

**Note:** When sharing a link to a finding, consider the recipient's IAM roles. If they don't have an IAM role that provides the proper permissions, they can't view the finding. For more information on Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control).

#### Send feedback about the finding to Google Cloud

For information about how to send feedback about a finding, click the tab for your service tier.

  1. On the **Findings** page, click the finding to view its details.
  2. Click **Take action > Send feedback**.
  3. Enter a description of your feedback.
  4. To include a screenshot, click **Capture screenshot**.
  5. Click **Send**.



#### Display details of other findings in the findings query results

To see the details of the findings that precede or follow the finding that you are viewing, use the navigate_next next or navigate_before previous button to go to the next or previous finding, without having to go back to the **Findings** page.

**Note:** The order of findings displayed when you click these buttons depends on the order of findings in the findings query results.

## Add security marks to findings

A _security mark_ is a custom key-value label that you can use to annotate a finding, associate a finding with other findings that share the same security mark, and query findings.

For instructions to set security marks on findings, see [Annotate findings with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings). To set security marks on assets, see [Annotate assets with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-assets).

## Mute findings in the console

You can mute and unmute findings from the following views:

  * Findings query results on the **Findings** page
  * Detail view of a finding



You can mute individual findings or create mute rules that mute current _and_ future findings based on filters you define.

Muted findings are hidden and silenced, but you can still view them by adding the `mute="MUTED"` filter to your findings query. Muted findings continue to be logged for audit and compliance purposes.

For detailed instructions on how to mute and unmute findings, see [Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

## Change the state of a finding

A finding can have one of two states: `Active` or `Inactive`.

A state of `Active` means that the security issue that is identified by the finding persists in your environment as a potential threat or vulnerability.

A state of `Inactive` means that the security issue has been addressed.

You might want to change the state of a finding for a variety of reasons, such as to change the state of a finding to `Inactive` as soon as it is addressed, so you don't have to wait for the next scan to change the state for you.

For information about how to change the state of a finding, click the tab for your service tier.

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Findings query results** panel, select the finding
  4. In the action bar of the **Findings query results** panel, click **Change active state**.
  5. In the **Change active state** menu, select either **Active** or **Inactive**.



## Customize the Findings page

To control screen space, you can customize some of the elements that appear on the findings query results.

### Hide or display columns in the findings query results

In the findings query results, you can hide any column except for **Category**.

**Note** : Some findings might not populate all columns, such as **Project ID** , **Severity** , **Resource type** , or **Resource cloud provider**. For more information, see Why some findings are missing information. 

The following are examples of columns that are available:

  * **Category** : The name of the finding type.
  * **Severity** : The severity of the finding. For more information about finding severity levels, see [Severity classifications for findings](https://docs.cloud.google.com/security-command-center/docs/finding-severity-classifications).
  * **App stage** : The stage in the application lifecycle where the finding was detected, such as **Design** or **Operate**.
  * **App criticality** : The business criticality of the application that is associated with the finding.
  * **App name** : The name of the application registered in App Hub.
  * **App environment** : The environment of the application, such as **Production** or **Staging**.
  * **Toxic combination score** : An [attack exposure score](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_exposure_scores) on a `Toxic combination` class finding.
  * **Attack exposure score** : The [attack exposure score](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_exposure_scores) of the finding.
  * **Event time** : Either when the finding was first detected or when it was last updated. Finding retention periods are calculated from this timestamp. For information about changes that update the event time, see [Overview of the finding lifecycle](https://docs.cloud.google.com/security-command-center/docs/finding-lifecycle-overview).
  * **Create time** : When the finding was first created in Security Command Center. Because the underlying security event might occur before the scan and ingestion, **Event time** can be earlier than **Create time**.
  * **Finding class** : The class of the finding, such as `THREAT`, `VULNERABILITY`, and `MISCONFIGURATION`.
  * **Resource display name** : The display name of the resource in which the finding was detected.
  * **Resource full name** : The full name of the resource in which the finding was detected.
  * **Resource cloud provider** : The cloud service provider on which the resource is hosted.
  * **Resource path** : The path to the resource in which the finding was detected.
  * **Resource type** : The type of resource in which the finding was detected.
  * **Security marks** : Any security marks that are added to the finding.



For information about how to hide or display the columns in the findings query results, click the tab for your service tier.

  1. On the right of the **Findings query results** action bar, click _view_column_ **Columns**.
  2. Select the columns that you want to display.
  3. Clear the selections for columns that you want to hide.
  4. Click **Apply** to apply the changes to the **Findings query results** panel.



Column selections are preserved the next time you view the **Findings** page, even if you change projects or organizations. To clear all custom column selections, click **Clear column selections**.

### Hide or display Findings page panels

To increase your screen space for editing queries or viewing findings, you can hide or display panels. For more information, click the tab for your service tier.

You can hide or display the following panels:

  * **Quick filters** panel
  * **Query editor** panel



To hide a panel, click the **Toggle panel** icon, _first_page_ or _first_page_.

To display the panel, click the icon again.

## What's next

  * Learn about [detection services](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources).
  * Learn how to [use security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings).
  * Learn how to [configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center).
  * Learn how to [form a findings filter using the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
