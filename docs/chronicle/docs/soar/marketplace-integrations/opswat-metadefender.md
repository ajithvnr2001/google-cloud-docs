---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/opswat-metadefender/
title: OPSWAT MetaDefender \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:04.604369+00:00
---

# OPSWAT MetaDefender  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/opswat-metadefender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# OPSWAT MetaDefender

This document provides guidance on how to integrate OPSWAT MetaDefender with Google SecOps.

## Before you begin

Before configuring the OPSWAT MetaDefender integration in Google SecOps, obtain an API key from OPSWAT and configure the required network parameters.

### Obtain the API key

To obtain the API key, complete the following steps:

  1. Sign in to your OPSWAT account.

  2. On your dashboard page, copy the API key value under **My API Key** to use it for configuring the OPSWAT MetaDefender integration inputs.




### Configure network parameters

To configure the network parameters required for the OPSWAT MetaDefender integration, refer to the following table:

Function | Default port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | `apikey`  
  
## Integrate OPSWAT MetaDefender with Google SecOps

The integration requires the following parameters:

Parameters | Description  
---|---  
`ApiRoot` | _Required_ The API root of the OPSWAT MetaDefender instance.  
`ApiKey` | _Required_ The API key of the OPSWAT MetaDefender instance.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for connecting to the OPSWAT MetaDefender server is valid. Not selected by default.  
  
For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure instances, you can use them in playbooks. For more information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

The OPSWAT MetaDefender integration contains the following actions:

  * Ping
  * Scan Hash



### Ping

Use the **Ping** action to test connectivity to OPSWAT MetaDefender.

This action runs on all entities.

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
Output messages | Not available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Scan Hash

Use the **Scan Hash** action to scan a hash file in OPSWAT MetaDefender.

This action runs on the Filehash entity.

#### Action inputs

None.

#### Action inputs

The **Ping** action requires the following parameters:

Parameters | Description  
---|---  
`` | _Required_  
`` | _Optional_  
  
#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment | Available  
Insight | Available  
JSON result | Not available  
Output messages | Not available  
Script result | Available  
  
##### Entity enrichment

Entities are marked as **Suspicious** (`True`) if the results of their scan show the `Infected` status. Else, `False`.

##### Insight

Severity  
---  
Warn | A warning insight to inform the enriched hash about its malicious status.  
  
##### Script result

The following table describes the values for the script result output when using the **Scan Hash** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
