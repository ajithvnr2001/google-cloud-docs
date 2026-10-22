---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/configuring-the-connector/
title: Configure custom connectors \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:56.235675+00:00
---

# Configure custom connectors  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/configuring-the-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure custom connectors

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

When you configure a new connector, the platform uses the connector script in an integration as a template only. The configured connector is an instance of that connector template. You can add multiple connectors with different configurations using the same code you created for the connector in the IDE.

To configure a connector, follow these steps:

  1. Go to **SOAR Settings > Ingestion > Connectors** to access the connectors module and configure a connector under the relevant environment.  

  2. Click add **Create new Connector**.
  3. In the **Add Connector** dialog, select the connector type from the list.
  4. Optional: Select the **Remote Connector** checkbox.
  5. Click **Create**.
  6. In the **Parameters** section, enter the following connector parameters:
     * **Environment** : Defines which environment this connector connects to. If you don't need to define the environment, select **Default Environment**.
     * **Run Every** : Defines the interval of connector runs.
     * **Product Field Name** : Required by the connector to identify the product that generates the alerts pulled into Google Security Operations. Don't enter the product name here. Instead, enter the event field (a key from your JSON event) instead of the product name. For example: Put `_index` to indicate that `cloudtrail` is the product that generated the alert.
     * **Event Field Name** : Required by the connector to identify the type of the security event pulled into Google SecOps. Don't enter the event name or type here. Enter the event field (a key from your JSON event) instead of the event name or type.  
For example: Enter "`_source.userIdentity.type`" to indicate that `AssumedRole` is the type of the security event.
     * **Event Count Limit** : If you're pulling a correlation alert, indicate the limit of the underlying events Google SecOps should fetch with it. This is required to make a connector run faster (in case the alerts are heavy on redundant events) and reduce the redundancy for security analysts.
  7. The connector is configured under **Default Environment**. Once you fill in all the parameters, click **Save** to save the connector. 



For a full list of parameters for each connector, see [Google SecOps response integrations](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations). 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
