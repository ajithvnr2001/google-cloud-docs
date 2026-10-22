---
url: https://docs.cloud.google.com/carbon-footprint/docs/data-schema/
title: Carbon Footprint export data schema \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:55.297649+00:00
---

# Carbon Footprint export data schema  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/carbon-footprint/docs/data-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Carbon Footprint ](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Carbon Footprint export data schema

After [configuring an export](https://docs.cloud.google.com/carbon-footprint/docs/export), a BigQuery table with the following schema is created: 

Field | Type | Description | Example  
---|---|---|---  
`usage_month` | Date | Month during which this usage occurred. | `2021-10-01`  
`billing_account_id` | String | Cloud Billing account ID used for the carbon footprint export. | `007GD7-15C0E6-BDE6B3`  
`project.id` | String | Google Cloud project identifier associated with the carbon footprint data. If data isn't associated with a project or project was [deleted](https://docs.cloud.google.com/docs/security/deletion), then the `project.id` field is `NULL`. | `my-project`  
`project.number` | String | Google Cloud project number associated with the carbon footprint data. If data isn't associated with a project, then the `project.number` field is an empty string. | `802583874831`  
`service.description` | String | Readable name for the Google Cloud service associated with the carbon footprint data. | Cloud Run  
`service.id` | String | Identifier of the Google Cloud service associated with the carbon footprint data. | `F17B-412E-CB64`  
`location.location` | String | Location of the carbon footprint at the level of a country, region, or zone. | `us-central1-a`  
`location.region` | String | Cloud region for the carbon footprint. | `us-central1`  
`carbon_model_version` | Integer | Version of carbon model that produced this output. This value is updated whenever the model is changed. | `1`  
`carbon_footprint_total_kgCO2e.market_based` | Float | Total carbon footprint for the account, project, service, location, and month in kg of CO2 equivalent. Equivalent to scope 1 + scope 2 market-based + scope 3. | `588.8`  
`carbon_footprint_total_kgCO2e.location_based` | Float | Total carbon footprint for the account, project, service, location, and month in kg of CO2 equivalent. Equivalent to scope 1 + scope 2 location-based + scope 3. | `1587.3`  
`carbon_footprint_kgCO2e.scope1` | Float | Total scope 1 carbon footprint for the account, project, service, location, and month in kg of CO2 equivalent. | `10`  
`carbon_footprint_kgCO2e.scope2.location_based` | Float | Total scope 2 location-based carbon footprint for the account, project, service, location, and month in kg of CO2 equivalent. | `400`  
`carbon_footprint_kgCO2e.scope2.market_based` | Float | Total scope 2 market-based carbon footprint for the account, project, service, location, and month in kg of CO2 equivalent. | `105.8`  
`carbon_footprint_kgCO2e.scope3` | Float | Total scope 3 carbon footprint for the account, project, service, location, and month in kg of CO2 equivalent. | `986.8`  
`carbon_footprint_total_kgCO2e.after_offsets` | Float | `[DEPRECATED]` Total carbon footprint for the account, project, service, location, and month in kg of CO2 equivalent. Equivalent to scope 1 + scope 2 market-based + scope 3 + carbon offsets. **Set to`NULL` because this field is deprecated due to [Google's Strategic shift](https://blog.google/outreach-initiatives/sustainability/our-progress-to-accelerate-carbon-removal-solutions/)** from conventional carbon offsets to a direct focus on carbon removal technologies. | `NULL`  
`carbon_offsets_kgCO2e` | Float | `[DEPRECATED]` Total carbon offsets for the account, project, service, location, and month in kg of CO2 equivalent. **Set to`NULL` because this field is deprecated due to [Google's Strategic shift](https://blog.google/outreach-initiatives/sustainability/our-progress-to-accelerate-carbon-removal-solutions/)** from conventional carbon offsets to a direct focus on carbon removal technologies. | `NULL`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
