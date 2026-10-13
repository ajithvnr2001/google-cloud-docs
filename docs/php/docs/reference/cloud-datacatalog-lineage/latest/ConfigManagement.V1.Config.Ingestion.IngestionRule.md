---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datacatalog-lineage/latest/ConfigManagement.V1.Config.Ingestion.IngestionRule
title: Google Cloud Data Catalog Lineage V1 Client - Class IngestionRule (1.5.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:04.719088+00:00
---

# Google Cloud Data Catalog Lineage V1 Client - Class IngestionRule (1.5.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datacatalog-lineage/latest/ConfigManagement.V1.Config.Ingestion.IngestionRule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Data Catalog Lineage V1 Client - Class IngestionRule (1.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.3 (latest)  1.4.0  1.3.0  1.2.3  1.1.1  1.0.3  0.5.5  0.4.0  0.3.1  0.2.1  0.1.3 

Reference documentation and code samples for the Google Cloud Data Catalog Lineage V1 Client class IngestionRule.

Ingestion rule for Data Lineage ingestion.

Generated from protobuf message `google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule`

## Namespace

Google \ Cloud \ DataCatalog \ Lineage \ ConfigManagement \ V1 \ Config \ Ingestion

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ integration_selector` |  `[IngestionRule\IntegrationSelector](https://docs.cloud.google.com/php/docs/reference/cloud-datacatalog-lineage/latest/ConfigManagement.V1.Config.Ingestion.IngestionRule.IntegrationSelector)`   
Required. Integration selector of the rule. The rule is only applied to the Integration selected by the selector.  
`↳ lineage_enablement` |  `[IngestionRule\LineageEnablement](https://docs.cloud.google.com/php/docs/reference/cloud-datacatalog-lineage/latest/ConfigManagement.V1.Config.Ingestion.IngestionRule.LineageEnablement)`   
Required. Lineage enablement configuration. Defines configurations for the ingestion of lineage for the resource and its children. If unspecified, the ingestion will be enabled only if it was configured in the resource's parent.  
  
### getIntegrationSelector

Required. Integration selector of the rule. The rule is only applied to the Integration selected by the selector.

**Returns**  
---  
**Type** | **Description**  
`[IngestionRule\IntegrationSelector](https://docs.cloud.google.com/php/docs/reference/cloud-datacatalog-lineage/latest/ConfigManagement.V1.Config.Ingestion.IngestionRule.IntegrationSelector)|null` |   
  
### hasIntegrationSelector

### clearIntegrationSelector

### setIntegrationSelector

Required. Integration selector of the rule. The rule is only applied to the Integration selected by the selector.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[IngestionRule\IntegrationSelector](https://docs.cloud.google.com/php/docs/reference/cloud-datacatalog-lineage/latest/ConfigManagement.V1.Config.Ingestion.IngestionRule.IntegrationSelector)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLineageEnablement

Required. Lineage enablement configuration. Defines configurations for the ingestion of lineage for the resource and its children. If unspecified, the ingestion will be enabled only if it was configured in the resource's parent.

**Returns**  
---  
**Type** | **Description**  
`[IngestionRule\LineageEnablement](https://docs.cloud.google.com/php/docs/reference/cloud-datacatalog-lineage/latest/ConfigManagement.V1.Config.Ingestion.IngestionRule.LineageEnablement)|null` |   
  
### hasLineageEnablement

### clearLineageEnablement

### setLineageEnablement

Required. Lineage enablement configuration. Defines configurations for the ingestion of lineage for the resource and its children. If unspecified, the ingestion will be enabled only if it was configured in the resource's parent.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[IngestionRule\LineageEnablement](https://docs.cloud.google.com/php/docs/reference/cloud-datacatalog-lineage/latest/ConfigManagement.V1.Config.Ingestion.IngestionRule.LineageEnablement)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
