---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/data-residency/
title: Data residency \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:01.220571+00:00
---

# Data residency  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/data-residency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Data residency Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about data residency with AML AI. _Data residency_ describes where your data is stored at rest. To help comply with your internal and external data residency requirements, AML AI gives you the ability to control where data is stored.

Each [Instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances) resource is created with a region specified. The artifacts created underneath the parent are constrained to that region location.

## AML AI and data residency

  * Customer Data is stored at rest and machine learning processing is performed in the specified region.
  * This includes Customer Data associated with AML AI resources, such as datasets, engine configs, models, and includes copies of inputs and outputs, generated ML features, model hyperparameters, model weights, and prediction results.
  * See the [Service Specific Terms](https://cloud.google.com/terms/service-terms) for the definition of Customer Data, which may not include resource identifiers, attributes, or other data labels.



## Organizational constraints

Organizational constraints (`constraints/gcp.resourceLocations`) can control the region in which Google Cloud resources can be created. AML AI obeys these regional constraints at resource creation time. For more information, see [restricting resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) and [resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services#aml-ai).

## Location resource

![Location resource parent object](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/rest-vs-data.svg)

AML AI has a [Location](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations#Location) resource as a parent object of all other resources in AML AI. All child AML AI resources are associated with only one Location resource, which ensures data residency within the associated Google Cloud region.

## Input and output data

An AML AI instance requires all input and output data to be specified in the same region and project. This prevents data from being accidentally moved between Google Cloud regions.

## What's next

For more information about Google's data residency commitment, read [the data residency terms](https://cloud.google.com/terms/data-residency).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
