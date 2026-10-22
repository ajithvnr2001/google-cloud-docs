---
url: https://docs.cloud.google.com/chronicle/docs/soar/ingest/webhooks/setting-up-a-webhook/
title: Set up a SOAR webhook \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:37.337126+00:00
---

# Set up a SOAR webhook  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/ingest/webhooks/setting-up-a-webhook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up a SOAR webhook

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

Webhooks are a lightweight solution for ingesting alerts from your organization into the Google Security Operations SOAR platform.

Webhook-ingested alerts appear in the platform with the same information as alerts ingested using connectors.

Google recommends using either a connector or a webhook from the same source, but not both, to avoid creating duplicate cases.

Webhooks are best for scenarios that require basic mapping logic, while connectors are better for advanced and flexible mapping.

## Set up a webhook to ingest alerts

To set up a webhook to ingest alerts, follow these steps:

  1. Go to **SOAR Settings > Ingestion > Webhooks**.
  2. Click add **Add incoming webhook**.
  3. Enter a name for the new webhook, and choose an environment.
  4. Click **Save**. After saving, the new webhook appears on the main page.
  5. Copy the webhook URL and note it for later use. You need to enter it in the source platform as the webhook destination.

**Note:** The webhook URL appears after you save. Copy this URL immediately, as it's no longer visible once you leave the page. You need this URL to configure the webhook destination in the source platform. If you save without copying the URL, click  cached  **Generate new URL** to create a new one.

## Map data

After you upload a JSON sample, you can use the **Data mapping** section to map fields from your source JSON to the appropriate fields in Google Security Operations SOAR. The system processes your raw JSON, and you use the user interface (UI) to establish the mappings.

  1. In the **Data mapping** section, click **Upload JSON sample**. Provide a representative sample of the JSON payload your webhook sends.
  2. Map the Google Security Operations fields with the corresponding fields in your JSON sample. For example, to map the mandatory `StartTime` field, you might select a timestamp field from your JSON, such as `Detections.Last.Update`.
  3. Use the Expression Builder to refine the data. For example, you can use the **Date format** function to convert your timestamp into the required Unix epoch milliseconds format. For more information, see [Use the Expression Builder](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-expression-builder).
  4. Click **Run** in the Expression Builder to test the mapping and see the result. A green checkmark indicates a successful mapping.
  5. Your webhook JSON payload must contain the required fields for case creation and alert ingestion. For details, see Understanding the webhook JSON schema.
  6. After you map all the necessary fields, click **Save** , and then enable the webhook.



### Understanding mapping target fields

When mapping your JSON data, you are mapping to standardized fields within Google Security Operations SOAR. These fields are organized into categories to help you normalize and structure the incoming data. The available fields in the Data mapping UI are based on the internal system ontology. The main categories include:

  * **Entity fields:** Use these fields for data points from which the system can automatically extract and model entities, such as IP addresses, domain names, file hashes, and usernames. Mapping to these fields enriches the alert and improves correlation and pivoting.
  * **Generic event fields:** Use these for general event metadata, such as timestamps (`StartTime`, `EndTime`), event descriptions or messages, and other common event attributes.
  * **Technical and device metadata:** Use these fields for technical details about the event source, such as the reporting device's vendor and product (`DeviceVendor`, `DeviceProduct`), event severity, and other similar technical attributes.



Explore the available fields within the Data mapping tool in the Google Security Operations SOAR UI to find the most appropriate target field for each piece of data in your JSON payload.

## Understanding the webhook JSON schema

To make sure your alerts are ingested and processed correctly by Google Security Operations SOAR, your webhook JSON payload must follow a specific structure. The following tables detail the main fields expected in the JSON payload.

### Main case and alert fields

These fields represent the top-level properties of the alert or case being created. 

Field | Type | Recommended format | Mandatory | Description | Example  
---|---|---|---|---|---  
`TicketId` | String | UUID | Yes | 

  * An internal globally unique identifier (GUID) for a case within the SOAR platform.
  * The requirement for `TicketId`'s uniqueness is conditional and depends on `DisplayId`: 
    * If a unique `DisplayId` is provided, the `TicketId` does not need to be unique.
    * If `DisplayId` is not provided, the `TicketId` must be unique.
  * The `TicketId` often has the same value as the `DisplayId`.

| `"f7167971-f641-432f-a06f-ebca3caaa9dd"`  
`SourceSystemName` | String | Text | Yes | The name of the external system (for example, SIEM or an endpoint detection and response (EDR) system) that sent the original alerts to SOAR. | `"Splunk"`  
`Name` | String | Text | Yes | The title or name of the Case, often taken from the source alert type or summary. | `"Suspicious Login Attempt"`  
`DeviceVendor` | String | Text | Yes | The vendor of the device or product that generated the alert. This can also be mapped from the event data. | `"Palo Alto Networks"`  
`RuleGenerator` | String | Text | Yes | The name of the rule in the source system (for example, a SIEM correlation rule) that generated the alert. | `"Brute Force Attempt Detected"`  
`StartTime` | String or integer | Epoch milliseconds (UTC) or ISO8601 string (for example, "2026-04-09T14:30:00Z") | Yes | The start time of the earliest event in the case. **If providing an integer, it must be in Unix epoch milliseconds.** | `1670000000000` or `"2026-04-09T14:30:00Z"`  
`Environment` | String | Text | No | The name of the SOAR environment this alert belongs to. This must match an environment defined in your SOAR settings. | `"Default Environment"`  
`Description` | String | Text | No | A brief description of the case or alert. | `"Failed login followed by success from new IP"`  
`DisplayId` | String | UUID or String | No | 

  * An identifier used for display purposes within the SOAR UI.
  * This field is the primary key the system checks to detect duplicate alerts.
  * An alert is rejected as a duplicate if the `DisplayId` is not unique. This uniqueness check on `DisplayId` takes precedence over `TicketId`.
  * The `DisplayId` often has the same value as the `TicketId`.

| `"f7167971-f641-432f-a06f-ebca3caaa9dd"`  
`Reason` | String | Text | No | The reason the alert was created or triggered. | `"Unusual file access patterns detected."`  
`DeviceProduct` | String | Text | No | The product name from the vendor that generated the alert. This can also be mapped from the event data. | `"Cortex XDR"`  
`EndTime` | String or integer | Epoch milliseconds (UTC) or ISO8601 string (for example, "2026-04-09T14:30:00Z") | No | The end time of the latest event in the case. **If providing an integer, it must be in Unix epoch milliseconds.** | `1670000060000` or `"2026-04-09T14:31:00Z"`  
`Priority` | Integer | 0-100 | No | The priority level of the case. Defaults to 40 if not provided. (0-19: Informative, 20-39: Low, 40-59: Medium, 60-79: High, 80-100: Critical) | `80`  
`EventsList` | Array | Array of JSON objects | No | An array containing one or more raw event objects as received from the source. See Sending raw event data. | `[ { ... }, { ... } ]`  
`EventProduct` | String | Text | No | Product that created the events. | `"Cortex XDR"`  
`EventName` | String | Text | No | The title or name of the event, often taken from the source alert type or summary. | `"Suspicious Login Attempt"`  
  
### Sending raw event data - the `EventsList` array

You should send the raw JSON payload representing the events as they come from the source system within the `EventsList` array. This object is one element in the `EventsList` array. You then map fields such as `source_ip` and `timestamp` using the Data mapping UI.

#### Example event object in the `EventsList` array
    
    
    {
      "event_id": "9a8b7c-1234-5678",
      "timestamp": "2026-07-01T07:29:50Z",
      "signature": "UserLoginFailed",
      "severity": "Medium",
      "user_name": "administrator",
      "source_ip": "192.168.1.50",
      "destination_ip": "10.0.0.10",
      "domain": "CORP",
      "status": "Failure",
      "Reason": "Wrong Password",
      "EventProduct": "Acme Firewall",
      "EventName": "Failed Login Attempt"
    }
    

### Key considerations and best practices

  * **Timestamps:** Use Unix epoch milliseconds for all `StartTime` and `EndTime` fields at the top level (as an integer). Within the event data, provide timestamps as they are from the source; you convert them in the Data mapping UI.
  * **Mandatory fields:** Make sure all fields marked as "Yes" in the Mandatory column are present in your JSON payload.
  * **`EventsList` array:** This array is crucial. Even if the alert represents a single event, it must be wrapped in the `EventsList` array.
  * **Data mapping UI:** Use the Data mapping tool in the **Webhook configuration** UI to map fields from your raw JSON to the appropriate Google Security Operations SOAR fields.
  * **Uniqueness:** `DisplayId` must be unique for each new alert to avoid de-duplication. `TicketId` must be unique if `DisplayId` is not provided.
  * **Response status:** An `HTTP 200 OK` response from the Webhooks Ingest endpoint confirms that the payload was received, but it does not guarantee that an alert will be created. Alert creation can fail during downstream processing due to payload structure or filtering rules. You can track downstream processing status using the [Collect SOAR platform logs](https://docs.cloud.google.com/chronicle/docs/secops/collect-secops-soar-logs#etl_log_labels) functionality.
  * **Testing:** Use the **Upload JSON sample** and the **Testing** tabs within the **Webhook configuration** page in SOAR to validate your payload structure and mappings.

**Note on event timestamp display:** When ingesting event data using webhooks, the display of timestamp fields within the alert details list can vary. The platform attempts to format fields that appear to be time-related, assuming the value is provided in epoch milliseconds. If a timestamp field (often one containing "time" in its name, such as `@timestamp`) is sent in a format other than epoch milliseconds (for example, `MM/DD/YYYY HH:MM:SS` or `YYYY-MM-DDTHH:MM:SSz`), the list view might not display the time as expected. This is because the system attempts to interpret it as milliseconds since epoch. You can view the original, raw value as sent in the webhook by double-clicking the timestamp field in the event list. For the most consistent display results across the platform, configure the source system to send time values in epoch milliseconds where possible, or make sure conversion is correct in the Data mapping UI. 

## Test the webhook

In the **Testing** tab, you can test the end-to-end functionality of the webhook and view detailed error descriptions.

  1. In the **Testing** tab, copy the webhook URL.
  2. Upload a JSON file with the relevant data.
  3. Click **Run**. The results display together with the output.



### Configure the CrowdStrike platform

This use case takes you through the steps in CrowdStrike for the webhook to start ingesting alerts into the Google SecOps platform.

  1. In the CrowdStrike Falcon dashboard, go to the [Falcon store](https://falcon.crowdstrike.com/store-v2/) and install the Webhooks add-on.
  2. Configure the webhook with the name and the webhook URL that you copied from the Google SecOps platform, and then click **Save**.
  3. Go to the **Workflows** section.
  4. Click **Create a workflow**.
  5. Select a trigger, such as **New detection** , and click **Next**.
  6. Select **Add action**.
  7. In the **Customize action** section, select **Notifications** from the **Action type** menu, and select **Call webhook** from the **Action** menu.
  8. Select the name you added in the initial step and all necessary fields, and then click **Finish**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
