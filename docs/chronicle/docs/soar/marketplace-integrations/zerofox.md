---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/zerofox/
title: Integrate Zerofox with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:11:58.067673+00:00
---

# Integrate Zerofox with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/zerofox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Zerofox with Google SecOps

This document provides guidance on how to integrate Zerofox with Google SecOps.

### Integration Parameters

The Zerofox integration requires the following parameters:

Parameter | Description  
---|---  
API Root | Required. The API root of the Zerofox instance.  
API Token | Required. The Zerofox API token.  
Verify SSL | Required. If selected, the integration validates the SSL certificate when connecting to Zerofox. Selected by default. The default value is `Checked`.  
  
## Actions

For more information about actions, see [Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action).

### Ping

Use the **Ping** action to test the connectivity to Zerofox.

The action doesn't run on any entities. 

#### Action inputs

The **Ping** action doesn't require any parameters.

#### Action Outputs

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

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Zerofox server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Zerofox server! Error is {0}".format(exception.stacktrace)` | The action failed.  
  
#### Script Result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Request Takedown

Use the **Request Takedown** action to request a takedown in Zerofox.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Request Takedown** action requires the following parameters:

Parameter | Description  
---|---  
Alert ID | Required. The ID of the Zerofox Alert.  
  
#### Action outputs

The **Request Takedown** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
#### Output messages

The **Request Takedown** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully requested takedown for alert with ID {alert id}` | The action succeeded.   
`Error executing action "Request Takedown". Reason: {0}''.format(error.Stacktrace)` `Error executing action "Request Takedown". Reason: Alert with ID {alert ID} wasn't found in Zerofox.''` `Error executing action "Request Takedown". Reason: {error}.''` | The action failed.  
  
#### Script Result

The following table describes the values for the script result output when using the **Request Takedown** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Close Alert

Use the **Close Alert** action to close an alert in Zerofox.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Close Alert** action requires the following parameters:

Parameter | Description  
---|---  
Alert ID | Required. The ID of the Zerofox Alert.  
  
#### Action Outputs

The **Close Alert** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
#### Script Result

The following table describes the values for the script result output when using the **Close Alert** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
##### Output messages

The **Close Alert** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully closed alert with ID {alert id}` | The action succeeded.  
`Error executing action "Close Alert". Reason: {0}''.format(error.Stacktrace)` `Error executing action "Close Alert". Reason: Alert with ID {alert ID} wasn't found in Zerofox.''` `Error executing action "Close Alert". Reason: {error}` | The action failed.  
  
### Add Note To Alert

Use the **Add Note To Alert** action to add a note to an alert in Zerofox.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Add Note To Alert** action requires the following parameters:

Parameter | Description  
---|---  
Alert ID | Required. The ID of the Zerofox Alert.  
Note | Required. The note for the alert.  
  
#### Action outputs

The **Add Note To Alert** action provides the following outputs:

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

The **Add Note To Alert** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added a note to alert with ID {alert id}` | The action succeeded.  
`Error executing action "Add Note To Alert". Reason: {0}''.format(error.Stacktrace)` `Error executing action "Add Note To Alert". Reason: Alert with ID {alert ID} wasn't found in Zerofox.''` `Error executing action "Add Note To Alert". Reason: {error}` | The action failed.  
  
#### Script Result

The following table describes the values for the script result output when using the **Add Note To Alert** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Add Evidence To Alert

Use the **Add Evidence To Alert** action to add evidence to an alert in Zerofox.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Add Evidence To Alert** action requires the following parameters:

Parameter | Description  
---|---  
Alert ID | Required. The ID of the Zerofox Alert.  
Filepath | Required. The absolute path for the evidence submitted to the alert.  
  
#### Action outputs

The **Add Evidence To Alert** action provides the following outputs:

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

The **Add Evidence To Alert** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added evidence to the alert with ID {alert id}` | The action succeeded.  
`Error executing action "Add Evidence To Alert". Reason: {0}''.format(error.Stacktrace)` `Error executing action "Add Evidence To Alert". Reason: Alert with ID {alert ID} wasn't found in Zerofox.''` `Error executing action "Add Evidence To Alert". Reason: {error}` | The action failed.  
  
#### Script Result

The following table describes the values for the script result output when using the **Add Evidence To Alert** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
