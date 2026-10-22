---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mandiant-managed-defense/
title: Mandiant Managed Defense \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:34.114056+00:00
---

# Mandiant Managed Defense  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mandiant-managed-defense/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Mandiant Managed Defense

This document provides guidance to help you configure and integrate Mandiant Managed Defense with Google SecOps.

## Integrate Mandiant Managed Defense with Google SecOps

The integration requires the following parameters:

Parameters | Description  
---|---  
`API Root` | _Required_ The API root of the Mandiant instance. The default value is `https://api.services.mandiant.com`.  
`Client ID` | _Required_ The client ID value of the Mandiant Managed Defense account.  
`Client Secret` | _Required_ The client secret value of the Mandiant Managed Defense account.  
`Verify SSL` | _Required_ If selected, the integration verifies that the SSL certificate for connecting to the Mandiant server is valid. Selected by default.  
  
You can make changes at a later stage, if necessary. After you configure instances, you can use them in playbooks. For more information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

For instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

The integration includes the following actions:

  * Ping



### Ping

Use the **Ping** action to test connectivity to Mandiant Managed Defense.

This action doesn't run on entities.

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

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Mandiant Managed Defense server with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the Mandiant Managed Defense server! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

For more information about how to configure connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Mandiant Managed Defense – Investigations Connector

Use the **Mandiant Managed Defense – Investigations Connector** to retrieve investigation from Mandiant Managed Defense.

The dynamic list works with the `name` parameter.

#### Connector inputs

The **Mandiant Managed Defense – Investigations Connector** requires the following parameters:

Parameters | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored. The default value is `Product Name`.  
`Event Field Name` | _Required_ The field name used to determine the event name (subtype). The default value is `type`.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.The default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` | _Required_ The timeout limit for the Python process running the current script. the default value is 180.  
`API Root` | _Required_ The API root of the Mandiant instance. The default value is `https://api.services.mandiant.com`.  
`Client ID` | _Required_ The client ID value of the Mandiant Managed Defense account.  
`Client Secret` | _Required_ The client secret value of the Mandiant Managed Defense account.  
`Status Filter` | _Optional_ The status filter for the investigations.If you provide no value, the connector ingests the investigations with all status values. Possible values are as follows:

  * `open`
  * `resolved`
  * `disputed`
  * `false-positive`

  
`Max Hours Backwards` | _Required_ The number of hours before the first connector iteration to retrieve the incidents from. This parameter applies only once to the initial connector iteration after you enable the connector for the first time.The default value is 24 hours.  
`Max Investigations To Fetch` | _Required_ The number of investigations to process in a one connector iteration. The default value is 100. The maximum value is 100.  
`Use dynamic list as a blocklist` | _Required_ If selected, the connector uses the dynamic list as a blocklist. Not selected by default.  
`Verify SSL` | _Required_ If selected, Google SecOps verifies that the SSL certificate for the connection to the Mandiant server is valid. Selected by default.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
`Disable Overflow` | _Optional_ Select to disable an event overflow. Not selected by default.  
  
#### Connector rules

The **Mandiant Managed Defense – Investigations Connector** supports proxies.

#### Connector events

The following is an example of a **Mandiant Managed Defense – Investigations Connector** event in Google SecOps:
    
    
    {
       "id": "TYPE-investigation--257e976c-2a2e-5b29-9203-387615b8b670",
       "type": "TYPE-investigation",
       "name": "Privilege escalation - testing 2",
       "description": "\n\n\nMandiant alerted on endpoint activity related to a suspicious `PrivilegeEscalation` event. This event matched the signature **Privilege escalation using token duplication** on the host HOST.\n\nMicrosoft Defender for Endpoint provided the following description for the detection:\n\n```\nA new process was suspiciously created with a duplicated access token for the SYSTEM account. This activity, often referred to as token impersonation, is used to elevate privileges for existing processes or start processes with elevated privileges.\n\n\n```\n\nFor alert details, see the following link in Microsoft Defender for Endpoint:\n\n* https://security.microsoft.com/alerts/ALERT_ID",
       "investigation_status": "open",
       "investigation_form": "case",
       "start_time": "2024-02-23T23:28:10Z",
       "end_time": "",
       "created": "2024-02-23T23:28:10Z",
       "modified": "2024-02-23T23:28:10Z",
       "published": "2024-02-23T23:28:10Z",
       "x_fireeye_com_severity": "medium",
       "x_fireeye_com_priority": "3",
       "assigned_user_email": null,
       "external_references": [
           {
               "source_name": "FaaS Portal",
               "external_id": "ID",
               "url": "https://md.mandiant.com/investigations/ID"
           }
       ]
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
