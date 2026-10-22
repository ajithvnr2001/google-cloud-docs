---
url: https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/defining-environments-in-connectors/
title: Define environments in SOAR connectors \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:57.603801+00:00
---

# Define environments in SOAR connectors  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/defining-environments-in-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Define environments in SOAR connectors

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

You can set up connectors in various ways, as each connector has its own configuration. Here are some ways you can define connectors: 

  * **Set a static environment:** define the environment in the **Environment** field in the specific connector on the Google Security Operations platform. 
  * **Extract environment dynamically** : define the environment in the **Environment Field Name** field. The environment is extracted from that field. 
  * **Extract environment dynamically + regular expression pattern** : define the option in the **Environment Regex Pattern** field and the environment is extracted from that field by the regular expression pattern. **Note:** Not all connectors support this option. 
  * **Use third-party multi-tenant mechanism** : Define the environment in the **Environment** field using the third-party tenant name. Some integrations have a built-in, multi-tenant mechanism with a checkbox that lets you set the **Environment** field by the third-party tenant name. 



In some cases, the extracted environment field value is different from the Google SecOps environment. For example, the **Environment** field is `altostrat.com`, while the Google SecOps environment is called _altostrat_.

## Define alias names

To define an alias name, follow these steps:

  1. Go to **SOAR Settings > Organization > Environments**.
  2. Click  add  **Add Environment** to match the name in the integration with the name of the environment in the Google SecOps platform. 



## Troubleshooting

If after the entire process, the connector has no environment or an empty environment (`""`), the default overrides the empty result. If the connector contains values that define an uncreated environment, then alerts are ingested in the database and playbooks start to run. As soon as the new environment is created, the cases and playbooks are displayed in the platform.

To stop alerts related to non-existent environments from being ingested into the database, you can contact [ Google SecOps Support](https://console.cloud.google.com/) and request they make the change in the database configuration. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
