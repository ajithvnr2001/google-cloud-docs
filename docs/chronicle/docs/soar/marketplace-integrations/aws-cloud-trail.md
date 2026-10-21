---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-cloud-trail/
title: Integrate AWS CloudTrail with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:11:51.866858+00:00
---

# Integrate AWS CloudTrail with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-cloud-trail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate AWS CloudTrail with Google SecOps 

This document explains how to integrate AWS CloudTrail with Google Security Operations (Google SecOps).

## Prerequisites

This integration requires you to configure the read-only access policy. For more information about the policy, see [Granting custom permissions for CloudTrail users](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_id-based-policy-examples.html#grant-custom-permissions-for-cloudtrail-users) on the AWS documentation website.

## Integration inputs

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

To configure the integration, use the following parameters:

Parameters  
---  
`AWS Access Key ID` | Required.AWS Access Key ID to use in integration.  
`AWS Secret Key` | Required.AWS Secret Key to use in integration.  
`AWS Default Region` | Required.AWS default region to use in integration, such as `us-west-2`.  
**Note:** You can make changes at a later stage, if needed. Once configured, the instances can be used in playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

You can run any integration action either automatically in a playbook or manually from the Case View.

### Ping

Test connectivity to AWS CloudTrail.

#### Entities

This action doesn't run on entities.

#### Action inputs

N/A

#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
JSON result | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the AWS CloudTrail server with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the AWS CloudTrail server! Error is ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### AWS CloudTrail - Insights Connector

Pull insights from AWS CloudTrail.

##### Connector inputs

To configure the connector, use the following parameters:

Parameters  
---  
`Product Field Name` | Required.  
`Event Field Name` | Required. The name of the field that determines the event name (subtype). Default value is `CloudTrailEvent_insightDetails_insightType`.   
`Environment Field Name` | Optional. The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` | Required.The timeout limit, in seconds, for the Python process that runs the current script. Default value is 180 seconds.  
`AWS Access Key ID` | Required. AWS Access Key ID to use in integration.  
`AWS Secret Key` | Required. AWS Secret Key to use in integration.  
`AWS Default Region` | Required. AWS default region to use in integration, such as `us-west-2`.   
`Alert Severity` | Required. Severity level of the Google SecOps alerts created based on the insights.Possible values are:

  * Informational
  * Low
  * Medium
  * High
  * Critical

Default value is `Medium`.   
`Fetch Max Hours Backwards` | Optional. The number of hours before the first connector iteration to retrieve the insights. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp. Default value is 1 hour.  
`Max Insights To Fetch` | Optional. Number of incidents to process per one connector iteration. Max value is 50.Default value is 50.  
`Use whitelist as a blacklist` | Required. If selected, the dynamic list is used as a blocklist. Unchecked by default.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the AWS CloudTrail server. Not selected by default.  
`Proxy Server Address` | Optional. Address of the proxy server to use.  
`Proxy Username` | Optional. Proxy username to authenticate with.  
`Proxy Password` | Optional. Proxy password to authenticate with.  
  
#### Connector rules

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
