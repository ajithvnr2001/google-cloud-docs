---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/stealthwatch/
title: Integrate Cisco Secure Network Analytics with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:26.772678+00:00
---

# Integrate Cisco Secure Network Analytics with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/stealthwatch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Cisco Secure Network Analytics with Google SecOps 

This document explains how to integrate Cisco Secure Network Analytics (formerly Stealthwatch) with Google Security Operations (Google SecOps).

**Important:** Cisco acquired Stealthwatch and rebranded it as _Cisco Secure Network Analytics_. However, the integration for Cisco Secure Network Analytics in the Google SecOps platform uses the name _Stealthwatch_.

## Use cases

The **Cisco Secure Network Analytics** integration can address the following use cases:

  * **Retrieve security events** : Use Google SecOps capabilities to search and retrieve host security events from the Cisco Secure Network Analytics server during incident investigation.

  * **Search for network flow data** : Use Google SecOps capabilities to search for network flows by IP address within a specified timeframe to understand host communication patterns.




## Integration parameters

The **Cisco Secure Network Analytics** integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required.The base URL of the Cisco Secure Network Analytics instance.The default value is `https://x.x.x.x`.  
`Username` | Required.The username used to sign in to Cisco Secure Network Analytics.  
`Password` | Required.The password used to sign in to Cisco Secure Network Analytics.  
`Verify SSL` | Optional.If selected, the integration validates the SSL certificate when connecting to the Cisco Secure Network Analytics server.Disabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to test connectivity to Cisco Secure Network Analytics.

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
`Successfully connected to the Stealthwatch with the provided connection parameters!` | The action succeeded.  
`Error executing action "Ping". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the Ping action: 

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search Events

Use the **Search Events** action to retrieve a host's security events from Cisco Secure Network Analytics for a given timeframe.

This action runs on the following Google SecOps entities:

  * `IP Address`



#### Action inputs

The **Search Events** action requires the following parameters:

Parameter | Description  
---|---  
`Time Frame` | Required.The number of hours, measured backward from the current time, to include in the search window for security events.  
  
#### Action outputs

The **Search Events** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
### Search Flows

Use the **Search Flows** action to retrieve network flow data from Cisco Secure Network Analytics for a given IP address and timeframe.

This action runs on the following Google SecOps entities:

  * `IP Address`



#### Action inputs

The **Search Flows** action requires the following parameters:

Parameter | Description  
---|---  
`Time Frame` | Required.The number of hours, measured backward from the current time, to include in the flow search.  
`Limit` | Required.The maximum number of flow records to retrieve from Cisco Secure Network Analytics.  
  
#### Action outputs

The **Search Flows** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
