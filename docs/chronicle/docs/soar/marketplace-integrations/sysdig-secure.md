---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sysdig-secure/
title: Integrate Sysdig Secure with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:10:58.579732+00:00
---

# Integrate Sysdig Secure with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sysdig-secure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Sysdig Secure with Google SecOps

This document explains how to integrate Sysdig Secure with Google Security Operations (Google SecOps).

## Integration parameters

The Sysdig Secure integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required.The API root of the Sysdig Secure instance. For more information about API root values, see [Sysdig API](https://docs.sysdig.com/en/docs/developer-tools/sysdig-api/#access-next-gen-api-documentation-using-regional-endpoints).   
`API Token` | Required.The Sysdig Secure API token. For more information about how to generate tokens, see [Retrieve the Sysdig API Token](https://docs.sysdig.com/en/retrieve-the-sysdig-api-token).  
`Verify SSL` | Required.If selected, the integration validates the SSL certificate when connecting to the Sysdig Secure server. Selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to test the connectivity to Sysdig Secure.

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
`Successfully connected to the Sysdig Secure server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Sysdig Secure server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Sysdig Secure - Events Connector

Use the **Sysdig Secure - Events Connector** to pull events from Sysdig Secure.

To work with the dynamic list, use the `ruleName` parameter.

#### Connector inputs

The **Sysdig Secure - Events Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required.The name of the field that determines the event name (subtype). The default value is `content_ruleName`.  
`Environment Field Name` | Optional.The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` | Required.The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
`API Root` | Required.The API root of the Sysdig Secure instance. For more information about API root values, see [Sysdig API](https://docs.sysdig.com/en/docs/developer-tools/sysdig-api/#access-next-gen-api-documentation-using-regional-endpoints).   
`API Token` | Required.The Sysdig Secure API token. For more information about how to generate tokens, see [Retrieve the Sysdig API Token](https://docs.sysdig.com/en/retrieve-the-sysdig-api-token).  
`Lowest Severity To Fetch` | Optional.The lowest severity of the alerts to retrieve.If you don't configure this parameter, the connector ingests alerts with all severity levels.The possible values are as follows:

  * `Informational`
  * `Low`
  * `Medium`
  * `High`

  
`Custom Filter Query` | Optional.A query to filter, scope, or group events during ingestion.This parameter has priority over the `Lowest Severity To Fetch` parameter and values that you set in the dynamic list. For more information about how to filter events, see [Filter Secure Events](https://docs.sysdig.com/en/docs/sysdig-secure/threats/activity/events-feed/#filter-secure-events).The example of the input is as follows: `host.hostName = "instance-1"`.  
`Max Hours Backwards` | Required.The number of hours prior to now to retrieve events. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp. The default value is `1`.  
`Max Events To Fetch` | Required.The maximum number of events to process in every connector iteration.The maximum value is `200`.The default value is `100`.  
`Disable Overflow` | Optional.If selected, the connector ignores the Google SecOps overflow mechanism.Not selected by default.  
`Use dynamic list as a blocklist` | Optional.If selected, the connector uses the dynamic list as a blocklist. Not selected by default.  
`Verify SSL` | Optional.If selected, the integration validates the SSL certificate when connecting to the Sysdig Secure server.Not selected by default.  
`Proxy Server Address` | Optional.The address of a proxy server to use.  
`Proxy Username` | Optional.The proxy username to authenticate with.  
`Proxy Password` | Optional.The proxy password to authenticate with.  
  
#### Connector rules

The **Sysdig Secure - Events Connector** supports proxies.

#### Connector events

The example of the **Sysdig Secure - Events Connector** event is as follows:
    
    
    {
       "id": "ID",
       "reference": "0194cd55-6752-823e-990c-380977fa3ce8",
       "cursor": "PTE4MjBjYTI0NjdjZDFjYzkwMzdlZDA0NGVkNjYyNzFh",
       "timestamp": "2025-02-03T19:41:53.874140361Z",
       "customerId": 2002953,
       "originator": "policy",
       "category": "runtime",
       "source": "syscall",
       "rawEventOriginator": "linuxAgent",
       "rawEventCategory": "runtime",
       "sourceDetails": {
           "sourceType": "workload",
           "sourceSubType": "host"
       },
       "engine": "falco",
       "name": "Sysdig Runtime Threat Detection",
       "description": "This policy contains rules which Sysdig considers High Confidence of a security incident. They are tightly coupled to common attacker TTP's. They have been designed to minimize false positives but may still result in some depending on your environment.",
       "severity": 3,
       "agentId": 118055020,
       "machineId": "MACHINE_ID",
       "content": {
           "policyId": 10339481,
           "ruleName": "Find Google Cloud Credentials",
           "internalRuleName": "Find Google Cloud Credentials",
           "ruleType": 6,
           "ruleSubType": 0,
           "ruleTags": [
               "host",
               "container",
               "MITRE",
               "MITRE_TA0006_credential_access",
               "MITRE_TA0007_discovery",
               "MITRE_T1552_unsecured_credentials",
               "MITRE_T1552.004_unsecured_credentials_private_keys",
               "MITRE_T1119_automated_collection",
               "MITRE_T1555_credentials_from_password_stores",
               "MITRE_TA0009_collection",
               "process",
               "gcp",
               "MITRE_T1552.003_unsecured_credentials_bash_history"
           ],
           "output": "OUTPUT",
           "fields": {
               "container.id": "host",
               "container.image.repository": "<NA>",
               "container.image.tag": "<NA>",
               "container.name": "host",
               "evt.args": "ARGS_VALUE",
               "evt.res": "SUCCESS",
               "evt.type": "execve",
               "group.gid": "1010",
               "group.name": "example",
               "proc.aname[2]": "sshd",
               "proc.aname[3]": "sshd",
               "proc.aname[4]": "sshd",
               "proc.cmdline": "grep private_key example_credentials.json",
               "proc.cwd": "/home/example/",
               "proc.exepath": "/usr/bin/grep",
               "proc.hash.sha256": "9a9c5a0c3b5d1d78952252f7bcf4a992ab9ea1081c84861381380a835106b817",
               "proc.name": "grep",
               "proc.pcmdline": "bash",
               "proc.pid": "402495",
               "proc.pid.ts": "1738611713873608827",
               "proc.pname": "bash",
               "proc.ppid": "385443",
               "proc.ppid.ts": "1738599569497780082",
               "proc.sid": "385443",
               "user.loginname": "example",
               "user.loginuid": "1009",
               "user.name": "example",
               "user.uid": "1009"
           },
           "falsePositive": false,
           "matchedOnDefault": false,
           "templateId": 1331,
           "policyType": "falco",
           "AlertId": 1357687,
           "origin": "Sysdig"
       },
       "labels": {
           "agent.tag.role": "datafeeder",
           "cloudProvider.account.id": "ACCOUNT_ID",
           "cloudProvider.name": "gcp",
           "cloudProvider.region": "europe-west3",
           "gcp.compute.availabilityZone": "europe-west3-c",
           "gcp.compute.image": "projects/debian-cloud/global/images/debian-example",
           "gcp.compute.instanceId": "INSTANCE_ID",
           "gcp.compute.instanceName": "example-instance",
           "gcp.compute.machineType": "e2-standard-2",
           "gcp.location": "europe-west3",
           "gcp.projectId": "PROJECT_ID",
           "gcp.projectName": "example-project",
           "host.hostName": "example-instance",
           "host.id": "HOST_ID",
           "orchestrator.type": "none",
           "process.name": "grep private_key example_credentials.json"
       }
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
