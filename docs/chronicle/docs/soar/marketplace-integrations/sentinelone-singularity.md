---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sentinelone-singularity/
title: Integrate SentinelOne Singularity Operations Center with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:32.162826+00:00
---

# Integrate SentinelOne Singularity Operations Center with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sentinelone-singularity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate SentinelOne Singularity Operations Center with Google SecOps 

This document explains how to configure and integrate SentinelOne Singularity Operations Center with Google Security Operations.

## Use cases

The **SentinelOne Singularity Operations Center** integration helps you perform the following:

  * **Centralize triage and investigation** : Access unified alerts, assets, indicators, and observables from the SentinelOne Singularity Operations Center to streamline analyst workflows.
  * **Update alert statuses and verdicts** : Programmatically update alert details, assignees, and verdicts directly from Google SecOps.
  * **Add analyst notes** : Synchronize case comments and notes back to SentinelOne Singularity Operations Center alerts.



## Before you begin

To authenticate the connection between Google SecOps and your SentinelOne Singularity Operations Center instance, you must provide a valid API token.

You can generate a personal API token within your SentinelOne management console.

For detailed instructions on generating and managing tokens, go to the [SentinelOne Customer Portal](https://community.sentinelone.com/s/article/000006575).

## Integration parameters

The SentinelOne Singularity Operations Center integration requires the following parameters:

Parameters  
---  
`API Root` | _Required_ API Root for the SentinelOne Singularity Operations Center instance.  
`API Token` | _Required_ API Token for the SentinelOne Singularity Operations Center instance.  
`Verify SSL` | _Required_ If selected, the integration validates the SSL certificate when connecting to SentinelOne Singularity Operations Center. Selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

For more information about actions, see [Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case#run-manual-action).

### Add Alert Comment

Use the **Add Alert Comment** action to add a comment to an alert in SentinelOne Singularity Operations Center.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Alert Comment** action requires the following parameters:

Parameters  
---  
`Alert ID` | _Required_ Specify the ID of the alert that needs to be updated.  
`Comment` | _Required_ Specify the comment for the alert.  
  
#### Action outputs

The **Add Alert Comment** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Add Alert Comment** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### Action output messages

The **Add Alert Comment** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added comment to the alert with ID ALERT_ID in SentinelOne Singularity Operations Center.` | Action succeeded.  
`Error executing action "Add Alert Comment". Reason: ERROR_REASON` | Action failed. Check connection to the server, input parameters, or credentials.  
`Error executing action "Add Alert Comment". Reason: alert with ID ALERT_ID wasn't found in SentinelOne Singularity Operations Center. Please check the spelling.` | Action failed. Check the spelling of the alert ID.  
  
### Ping

Use the **Ping** action to test the connectivity to SentinelOne Singularity Operations Center.

This action doesn't run on Google SecOps entities. 

#### Action inputs

This action has no input parameters.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### Action output messages

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to SentinelOne Singularity Operations Center.` | Action succeeded.  
`Error executing action "Ping". Reason: ERROR_REASON` | Action failed. Check connection to the server, input parameters, or credentials.  
  
### Update Alert

Use the **Update Alert** action to update an alert's status, verdict, or assignee in SentinelOne Singularity Operations Center.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Update Alert** action requires the following parameters:

Parameters  
---  
`Alert ID` | _Required_ Specify the ID of the alert that needs to be updated.  
`Status` | _Optional_ Specify the status for the alert. Possible values: `New`, `In Progress`, `Resolved`.  
`Verdict` | _Optional_ Specify the verdict for the alert. Possible values:

  * `True positive/Malware`
  * `True positive/Unauthorized access`
  * `True positive/Data exfiltration`
  * `True positive/Insider threat`
  * `True positive/Phishing attack`
  * `True positive/Advanced persistent threat`
  * `True positive/Denial of service`
  * `True positive/Ransomware`
  * `True positive/Policy violation`
  * `True positive/Benign but suspicious`
  * `True positive/Benign`
  * `True positive/Undefined`
  * `True positive/Exploitation tools`
  * `True positive/PUA Adware`
  * `False positive/Benign`
  * `False positive/Benign but suspicious`
  * `False positive/System error`
  * `False positive/User error`
  * `False positive/Undefined`

  
`Assignee` | _Optional_ Specify the name of the analyst to whom the alert needs to be assigned. If `Unassign` is provided, the action removes the assignment from the alert.  
  
#### Action outputs

The **Update Alert** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Update Alert** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### Action output messages

The **Update Alert** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated alert with ID ALERT_ID in SentinelOne Singularity Operations Center.` | Action succeeded.  
`Error executing action "Update Alert". Reason: ERROR_REASON` | Action failed. Check connection to the server, input parameters, or credentials.  
`Error executing action "Update Alert". Reason: alert with ID ALERT_ID wasn't found in SentinelOne Singularity Operations Center. Please check the spelling.` | Action failed. Check the spelling of the alert ID.  
  
## Connectors

For more information about connectors, see [Ingest data using connectors](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### SentinelOne Singularity Operations Center - Unified Alerts Connector

Use the **SentinelOne Singularity Operations Center - Unified Alerts Connector** to pull unified alerts from SentinelOne Singularity Operations Center.

#### Connector parameters

Use the following parameters to configure the connector:

Parameters  
---  
`Product Field Name` | _Required_ Enter the source field name in order to retrieve the Product Field name. Default: `Product Name`.  
`Event Field Name` | _Required_ Enter the source field name in order to retrieve the Event Field name. Default: `event_type`.  
`Environment Field Name` | _Optional_ Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
`Environment Regex Pattern` | _Optional_ A regex pattern to run on the value found in the "Environment Field Name" field. Default is `.*` to catch all and return the value unchanged.  
`Script Timeout (Seconds)` | _Required_ Timeout limit in seconds for the Python process running the current script. Default: `180`.  
`API Root` | _Required_ API Root for the SentinelOne Singularity Operations Center instance.  
`API Token` | _Required_ API Token for the SentinelOne Singularity Operations Center instance.  
`Lowest Severity To Fetch` | _Optional_ Lowest severity of the issues to fetch. If nothing is provided, the connector ingests issues with all severities. Possible values: `Critical`, `High`, `Medium`, `Low`, `Info`.  
`Max Hours Backwards` | _Required_ Amount of hours from where to fetch alerts. Default: `1`.  
`Max Alerts To Fetch` | _Required_ How many alerts to process per one connector iteration. Default: `10`.  
`Use dynamic list as a blocklist` | _Required_ If enabled, the dynamic list will be used as a blocklist. Unchecked by default.  
`Disable Overflow` | _Optional_ If enabled, the connector ignores the overflow mechanism. Unchecked by default.  
`Verify SSL` | _Required_ If selected, verifies that the SSL certificate for the connection to the SentinelOne Singularity Operations Center server is valid. Unchecked by default.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
