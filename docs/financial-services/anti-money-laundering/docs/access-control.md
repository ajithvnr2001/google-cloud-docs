---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/access-control/
title: IAM permissions \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:56.444888+00:00
---

# IAM permissions  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

AML AI uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) for access control.

You can configure access control for the Financial Services API at the project level. For example, you can grant access for developers to list and get all datasets within a project.

For a detailed description of IAM and its features, see the [IAM documentation](https://docs.cloud.google.com/iam/docs). In particular, see the section on [managing IAM policies](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Every AML AI method requires the caller to have the necessary permissions. For more information, see Permissions and Roles.

## Permissions

This section lists AML AI operations and their related permissions implemented by IAM.

### Required permissions

The following tables list the IAM permissions that are associated with AML AI.

`projects.locations` method name | Required permissions  
---|---  
`projects.locations.get` | `financialservices.locations.get` on the specific Google Cloud project  
`projects.locations.list` | `financialservices.locations.list` on the specific Google Cloud project  
**Note:** The following method names are shortened in each table; each method's full name begins with `projects.locations`.`instances` method name | Required permissions  
---|---  
`instances.create` | `financialservices.v1instances.create` on the parent location, which is a specific Google Cloud project and data location combination  
`instances.delete` | `financialservices.v1instances.delete` on the instance resource  
`instances.get` | `financialservices.v1instances.get` on the instance resource  
`instances.list` | `financialservices.v1instances.list` on the parent location, which is a specific Google Cloud project and data location combination  
`instances.patch` | `financialservices.v1instances.update` on the instance resource  
`instances.importRegisteredParties` | `financialservices.v1instances.importRegisteredParties` on the instance resource  
`instances.exportRegisteredParties` | `financialservices.v1instances.exportRegisteredParties` on the instance resource  
`instances.engineConfigs` method name | Required permissions  
---|---  
`instances.engineConfigs.create` | `financialservices.v1engineconfigs.create` on the parent instance  
`instances.engineConfigs.delete` | `financialservices.v1engineconfigs.delete` on the engine config resource  
`instances.engineConfigs.get` | `financialservices.v1engineconfigs.get` on the engine config resource  
`instances.engineConfigs.list` | `financialservices.v1engineconfigs.list` on the parent instance  
`instances.engineConfigs.patch` | `financialservices.v1engineconfigs.update` on the engine config resource  
`instances.engineConfigs.exportMetadata` | `financialservices.v1engineconfigs.exportMetadata` on the engine config resource  
`instances.engineVersions` method name | Required permissions   
---|---  
`instances.engineVersions.get` | `financialservices.v1engineversions.get` on the engine version resource  
`instances.engineVersions.list` | `financialservices.v1engineversions.list` on the parent instance  
`instances.datasets` method name | Required permissions  
---|---  
`instances.datasets.create` | `financialservices.v1datasets.create` on the parent instance  
`instances.datasets.delete` | `financialservices.v1datasets.delete` on the dataset resource  
`instances.datasets.get` | `financialservices.v1datasets.get` on the dataset resource  
`instances.datasets.list` | `financialservices.v1datasets.list` on the parent instance  
`instances.datasets.patch` | `financialservices.v1datasets.update` on the dataset resource  
`instances.models` method name | Required permissions  
---|---  
`instances.models.copy` | `financialservices.v1models.copyFrom` on the source model resource and `financialservices.v1models.copyTo` on the parent instance  
`instances.models.create` | `financialservices.v1models.create` on the parent instance  
`instances.models.delete` | `financialservices.v1models.delete` on the model resource  
`instances.models.get` | `financialservices.v1models.get` on the model resource  
`instances.models.list` | `financialservices.v1models.list` on the parent instance  
`instances.models.patch` | `financialservices.v1models.update` on the model resource  
`instances.models.exportMetadata` | `financialservices.v1models.exportMetadata` on the model resource  
`instances.backtestResults` method name | Required permissions  
---|---  
`instances.backtestResults.create` | `financialservices.v1backtests.create` on the parent instance  
`instances.backtestResults.delete` | `financialservices.v1backtests.delete` on the backtest result resource  
`instances.backtestResults.get` | `financialservices.v1backtests.get` on the backtest result resource  
`instances.backtestResults.list` | `financialservices.v1backtests.list` on the parent instance  
`instances.backtestResults.patch` | `financialservices.v1backtests.update` on the backtest result resource  
`instances.backtestResults.exportMetadata` | `financialservices.v1backtests.exportMetadata` on the backtest result resource  
`instances.predictionResults` method name | Required permissions  
---|---  
`instances.predictionResults.create` | `financialservices.v1predictions.create` on the parent instance  
`instances.predictionResults.delete` | `financialservices.v1predictions.delete` on the prediction result resource  
`instances.predictionResults.get` | `financialservices.v1predictions.get` on the prediction result resource  
`instances.predictionResults.list` | `financialservices.v1predictions.list` on the parent instance  
`instances.predictionResults.patch` | `financialservices.v1predictions.update` on the prediction result resource  
`instances.predictionResults.exportMetadata` | `financialservices.v1predictions.exportMetadata` on the prediction result resource  
  
The following methods are inherited from `google.longrunning.Operations`.

`operations` method name | Required permissions  
---|---  
`operations.cancel` | `financialservices.operations.cancel` on the specific Google Cloud project  
`operations.delete` | `financialservices.operations.delete` on the specific Google Cloud project  
`operations.get` | `financialservices.operations.get` on the specific Google Cloud project  
`operations.list` | `financialservices.operations.list` on the specific Google Cloud project  
  
## Roles

The following table lists the AML AI IAM roles, including the permissions associated with each role:

IAM role | Permissions  
---|---  
  
#### Financial Services Viewer 

(`roles/financialservices.viewer`) View access to all Financial Services API resources.  |  `financialservices.locations.*`

  * `financialservices.locations.get`
  * `financialservices.locations.list`

`financialservices.operations.get` `financialservices.operations.list` `financialservices.v1backtests.exportMetadata` `financialservices.v1backtests.get` `financialservices.v1backtests.list` `financialservices.v1datasets.get` `financialservices.v1datasets.list` `financialservices.v1engineconfigs.exportMetadata` `financialservices.v1engineconfigs.get` `financialservices.v1engineconfigs.list` `financialservices.v1engineversions.*`

  * `financialservices.v1engineversions.get`
  * `financialservices.v1engineversions.list`

`financialservices.v1instances.exportRegisteredParties` `financialservices.v1instances.get` `financialservices.v1instances.list` `financialservices.v1instances.listEffectiveTags` `financialservices.v1instances.listTagBindings` `financialservices.v1models.copyFrom` `financialservices.v1models.exportMetadata` `financialservices.v1models.get` `financialservices.v1models.list` `financialservices.v1predictions.exportMetadata` `financialservices.v1predictions.get` `financialservices.v1predictions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Financial Services Admin 

(`roles/financialservices.admin`) Full access to all Financial Services API resources.  |  `financialservices.*`

  * `financialservices.locations.get`
  * `financialservices.locations.list`
  * `financialservices.operations.cancel`
  * `financialservices.operations.delete`
  * `financialservices.operations.get`
  * `financialservices.operations.list`
  * `financialservices.v1backtests.create`
  * `financialservices.v1backtests.delete`
  * `financialservices.v1backtests.exportMetadata`
  * `financialservices.v1backtests.get`
  * `financialservices.v1backtests.list`
  * `financialservices.v1backtests.update`
  * `financialservices.v1datasets.create`
  * `financialservices.v1datasets.delete`
  * `financialservices.v1datasets.get`
  * `financialservices.v1datasets.list`
  * `financialservices.v1datasets.update`
  * `financialservices.v1engineconfigs.create`
  * `financialservices.v1engineconfigs.delete`
  * `financialservices.v1engineconfigs.exportMetadata`
  * `financialservices.v1engineconfigs.get`
  * `financialservices.v1engineconfigs.list`
  * `financialservices.v1engineconfigs.update`
  * `financialservices.v1engineversions.get`
  * `financialservices.v1engineversions.list`
  * `financialservices.v1instances.create`
  * `financialservices.v1instances.createTagBinding`
  * `financialservices.v1instances.delete`
  * `financialservices.v1instances.deleteTagBinding`
  * `financialservices.v1instances.exportRegisteredParties`
  * `financialservices.v1instances.get`
  * `financialservices.v1instances.importRegisteredParties`
  * `financialservices.v1instances.list`
  * `financialservices.v1instances.listEffectiveTags`
  * `financialservices.v1instances.listTagBindings`
  * `financialservices.v1instances.update`
  * `financialservices.v1models.copyFrom`
  * `financialservices.v1models.copyTo`
  * `financialservices.v1models.create`
  * `financialservices.v1models.delete`
  * `financialservices.v1models.exportMetadata`
  * `financialservices.v1models.get`
  * `financialservices.v1models.list`
  * `financialservices.v1models.update`
  * `financialservices.v1predictions.create`
  * `financialservices.v1predictions.delete`
  * `financialservices.v1predictions.exportMetadata`
  * `financialservices.v1predictions.get`
  * `financialservices.v1predictions.list`
  * `financialservices.v1predictions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
For more information about roles, see [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Custom roles

If the predefined IAM roles for AML AI don't meet your needs, you can define custom roles. Custom roles enable you to choose a specific set of permissions, create your own role with those permissions, and grant the role to users in your organization. For more information, see [Understanding IAM custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
