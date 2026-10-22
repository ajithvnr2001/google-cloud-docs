---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/proofpoint-cloud-threat-response/
title: Integrate Proofpoint Cloud Threat Response with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:47.665548+00:00
---

# Integrate Proofpoint Cloud Threat Response with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/proofpoint-cloud-threat-response/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Proofpoint Cloud Threat Response with Google SecOps 

This document explains how to integrate Proofpoint Cloud Threat Response with Google Security Operations.

## Use cases

The **Proofpoint Cloud Threat Response** integration addresses the following security operations use cases:

  * **Automated incident ingestion** : Automatically pull incidents and associated email messages from Proofpoint into Google SecOps to reduce manual monitoring and speed up triage.

  * **Prioritized threat response** : Filter ingested alerts based on specific severity and confidence thresholds to ensure analysts focus on high-impact threats first.

  * **Granular verdict analysis** : Streamline workflows by filtering incidents based on Proofpoint verdicts (such as Threat or Manual Review) and dispositions (such as Malware or Phish).

  * **Custom environment mapping** : Dynamically assign ingested alerts to specific environments using field mapping and regular expression patterns, ensuring proper data segregation and multi-tenancy support.




## Before you begin

Before you configure the integration in the Google SecOps platform, verify that you have the following:

  * **Proofpoint API credentials** : A valid Client ID and Client Secret generated from your Proofpoint Threat Response account. These credentials are required for the integration to authenticate and generate a Bearer token.

  * **API root URL** : The specific endpoint for your Proofpoint Cloud Threat Response instance (the default is `https://threatprotection-api.proofpoint.com`).

  * **Network access** : Ensure that the Google SecOps platform can communicate with the Proofpoint API endpoints over port 443. If your organization uses a proxy, have the proxy server address and credentials available.




## Integration parameters

The **Proofpoint Cloud Threat Response** integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required. The API Root URL of the Proofpoint Cloud Threat Response instance. The default value is `https://threatprotection-api.proofpoint.com`.  
`Client ID` | Required. The Client ID used to authenticate with the Proofpoint Cloud Threat Response instance.  
`Client Secret` | Required. The Client Secret used to authenticate with the Proofpoint Cloud Threat Response instance.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Proofpoint Cloud Threat Response server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to test the connectivity to Proofpoint Cloud Threat Response.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Proofpoint Cloud Threat Response server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Proofpoint Cloud Threat Response server! Error is ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Proofpoint Cloud Threat Response - Incidents Connector

Use the **Proofpoint Cloud Threat Response - Incidents Connector** to retrieve incidents and related message data from Proofpoint Cloud Threat Response and ingest them as alerts into Google SecOps.

**Note:** This connector supports proxy servers and environment aliases. 

For every Proofpoint incident, the connector creates one Google SecOps alert. The primary incident data is ingested as an "Incident" event type, while associated message data is ingested as "Message" event types.

#### Connector inputs

The **Proofpoint Cloud Threat Response - Incidents Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required. The name of the field that determines the event name or subtype. The default value is `product`.  
`Environment Field Name` | Optional. The name of the field that determines the event name (subtype). The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to extract or manipulate the environment value from `Environment Field Name`. The default value is `.*`.  
`Script Timeout (Seconds)` | Required. The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
`API Root` | Required. The API root URL of the Proofpoint Cloud Threat Response instance. The default value is `https://threatprotection-api.proofpoint.com`.  
`Client ID` | Required. The Client ID used to authenticate with the Proofpoint Cloud Threat Response instance.  
`Client Secret` | Required. The Client Secret used to authenticate with the Proofpoint Cloud Threat Response instance.  
`Lowest Severity To Fetch` | Optional. The lowest severity level of incidents to retrieve. For example, selecting `Medium` retrieves both Medium and High severity incidents. The possible values are as follows:

  * `Low`
  * `Medium`
  * `High`

  
`Status Filter` | Optional. A comma-separated list of incident statuses to include in the ingestion. The possible values are `Open` and `Closed`. The default value is `Open`.  
`Lowest Confidence To Fetch` | Optional. The lowest confidence level of incidents to retrieve. For example, selecting `Medium` retrieves both Medium and High confidence incidents. The possible values are as follows:

  * `Low`
  * `Medium`
  * `High`

  
`Disposition Filter` | Optional. A comma-separated list of dispositions to include (for example, `malware, phish, suspicious`).  
`Verdict Filter` | Optional. A comma-separated list of verdicts to include in the ingestion. The possible values are `Failed`, `Low Risk`, `Manual Review`, and `Threat`.  
`Max Hours Backwards` | Required. The number of hours prior to the current time to search for incidents during the first iteration or if the timestamp expires. The default value is `1`.  
`Max Incidents To Fetch` | Required. The maximum number of incidents to process in every connector iteration. The maximum value is `9`. The default value is `9`.  
`Use dynamic list as a blocklist` | Required. If selected, the connector uses the dynamic list (based on Source values) as a blocklist to exclude specific incidents. Disabled by default.  
`Disable Overflow` | Optional. If selected, the connector ignores the Google SecOps overflow mechanism. Disabled by default.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Proofpoint Cloud Threat Response server. Disabled by default.  
`Proxy Server Address` | Optional. The address of the proxy server to use.  
`Proxy Username` | Optional. The proxy username to authenticate with.  
`Proxy Password` | Optional. The proxy password to authenticate with.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
