---
url: https://docs.cloud.google.com/apigee/docs/release/notes/apigee-release-notes/
title: Apigee release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:39:12.307800+00:00
---

# Apigee release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/release/notes/apigee-release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Apigee release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents release notes for all Apigee products 2021 and prior.

See [All](https://docs.cloud.google.com/apigee/docs/apigee-release-notes) for current release notes (2022 and later) or select a product area from the menu. For example, [Monetization](https://docs.cloud.google.com/apigee/docs/apigee-monetization-release-notes). 

## **2021**

### December 15, 2021 - UI

On December 15, 2021, we released an updated version of the UI software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205810988** | **Users with the Apigee Integration Approver role were unable to access the UI to approve integrations.**  
This has been fixed. When an integration reaches an [Approval task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/approval-task), an email is sent to the approvers. For approvers with the role Apigee Integration Approver, the email contains a link that opens a pop-up dialog, where the approver can either approve or deny the request.  
---|---|---  
  
### December 15, 2021 - Apigee hybrid v1.6.3

On December 15, 2021, we released an updated version of the Apigee hybrid v1.6.3 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **209097822** | **Fixed and issue where SpikeArrest was not reflecting updated rate.**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **208474799** | **Apigee hybrid 1.6 now supports ASM 1.10.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **208322185** | **Apigee hybrid Cassandra backup and restore can now use either a user-provided custom secret or a generated secret**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **207618262** | **Fixed an issue where SpikeArrest opened too many connections to redis-envoy.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **207400645** | **Allow direct reads from API server to API client when enabled.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205820658** | **Fixed an issue where Apigee X/hybrid Debug could show the authorization header.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205732137** | **Handle Quota correctly when the Operation group is set with empty string params.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205148816** | **Product Level Quota Info now available in Proxy.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **204943895** | **Quota Policy in Shared Flow now working properly.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **204943880** | **Fixed issue where SpikeArrest in Shared Flow did not have context of API Proxy.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **204368970** | **TLS variables are now set by Apigee Runtime.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **204146857** | **Fixed an issue where new environments were not created in Apigee hybrid deployment.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **202299966** | **Added new remote-address-related headers and modified the headers to be RFC compliant.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **189341334** | **Fixed an issue to eliminate the potential for connection leaks for the`watcher` component.**  
  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/upgrade). 

### December 12, 2021 - Apigee X

On December 12, 2021, we released an updated version of the Apigee X software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **N/A** | **Dynamic updates to rate in SpikeArrest may not reflect immediately.**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **N/A** | **If there is more than one SpikeArrest policy in a bundle, 502 errors will occur.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **N/A** | **If ServiceCallout is "fire and forget" (no tag), a race condition can occur if there is another policy that occurs after it.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **N/A** | **SpikeArrest and Quota policies in are now allowed in a shared flow.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **202299966** | **We fixed an issue which was causing the internal headers`X-Apigee*` to escape beyond classification.**  
  
  
#### Security updates

This release includes the following security updates:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | N/A | **Miscellaneous Security updates and fixes.**  
  
---|---|---  
  
### December 9, 2021 - Apigee hybrid v1.5.6

On December 9, 2021, we released an updated version of the Apigee hybrid v1.5.6 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **208322185** | **Apigee hybrid Cassandra backup and restore can now use either a user-provided custom secret or a generated secret.**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **207618262** | **Fixed an issue where SpikeArrest opened too many connections to redis-envoy.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **207400645** | **Allow direct reads from API server to API client when enabled.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205732137** | **Handle Quota correctly when the Operation group is set with empty string params.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205148816** | **Product Level Quota Info now available in Proxy.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **204943895** | **Quota Policy in Shared Flow now working properly.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **204943880** | **Fixed issue where SpikeArrest in Shared Flow did not have context of API Proxy.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **204146857** | **Fixed an issue where new environments were not created in Apigee hybrid deployment.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **202299966** | **Added new remote-address-related headers and modified the headers to be RFC compliant.**  
  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade). 

### December 02,2021 - UI

On December 02,2021, we released an updated version of the UI software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205810988** | **Resolve suspension dialog displayed "user not authorized" message for regions other than US**  
This has been fixed. Location information is now added into the suspension URL from Apigee.  
---|---|---  
  
#### Deprecations

This release includes the following deprecations:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-deprecated.svg) |  **"Apigee Deployer" role deprecated and replaced by "Apigee Environment Admin"**   
The environment role "Apigee Deployer" has been deprecated, and replaced by "Apigee Environment Admin".   
---|---  
  
### November 22, 2021 - Apigee hybrid v1.6.2-hotfix.1

On November 22, 2021, we released an updated version of the Apigee hybrid v1.6.2-hotfix.1 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205820658** | **A security issue was addressed.**  
This hotfix has been superceded by Apigee hybrid v1.6.3.  
---|---|---  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/upgrade). 

### November 22, 2021 - Apigee hybrid v1.5.5-hotfix.1

On November 22, 2021, we released an updated version of the Apigee hybrid v1.5.5-hotfix.1 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205820658** | **A security issue was addressed.**  
This hotfix has been superceded by Apigee hybrid v1.5.6.  
---|---|---  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade). 

### November 11, 2021 - Apigee local development (GA)

On November 11, 2021, we released an updated version of the Apigee local development (GA) software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **General Availability (GA): Apigee local development**  
This is the GA release of local development using Apigee in Visual Studio Code (VS Code). This release enables you to integrate API platform management with the software development lifecycle (SDLC) that you use to develop, test, and deploy applications.During local development, use Apigee in VS Code to develop your API proxies and verify the functionality through unit and manual testing against the Apigee Emulator (local runtime).For more information, see [Overview of local development using Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/overview).  
---|---  
  
### November 10, 2021 - Integrated portal

On November 10, 2021, we released an updated version of the Integrated portal software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **205514395** | **App generating errors on save**  
Fix an issue that was preventing updates to Apps that contained unlisted APIs.  
---|---|---  
  
### November 3, 2021 - Apigee X Monetization

On November 3, 2021, we released an updated version of the Apigee X Monetization software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **DataCapture policy captures monetization variables**  
You can configure the DataCapture policy to capture a transaction's monetization information such as revenue, currency, price multiplier, and status. For more information, see [Monetization variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy#datacollector).  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Prepaid billing**  
Apigee supports the prepaid billing of developers. In prepaid billing, app developers would have paid in advance even before using your API products. The upfront payment made by the developers will be available in the developer's wallet, which can have different currencies. You can track a developer's balance in real-time and block API calls if a developer has insufficient funds.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Revenue sharing with developers**  
The revenue sharing feature enables developers to receive a percentage of the total revenue generated. As an API provider, you can configure **Revenue share** in your [rate plan](https://docs.cloud.google.com/apigee/docs-preview/api-platform/monetization/manage-rate-plans#create) to share a specific percentage of the revenue with your developer partners.   
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Volume banded consumption pricing**  
[Rate plan](https://docs.cloud.google.com/apigee/docs-preview/api-platform/monetization/manage-rate-plans#create) supports the new **Banded** type of consumption based fees. You can configure variable fees for each monetized transaction based on a band. A band refers to an API consumption range, and you can configure a different fee for each band.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Dynamic consumption pricing**  
To calculate the cost of a transaction, you can specify a multiplier ([perUnitPriceMultiplier](https://docs.cloud.google.com/apigee/docs-preview/api-platform/reference/policies/data-capture-policy#mint-var)) value on top of the pre-configured base price in your DataCapture policy.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Criteria for successful transaction**  
You can specify if a transaction must be monetized or not by configuring the [transactionSuccess](https://docs.cloud.google.com/apigee/docs-preview/api-platform/reference/policies/data-capture-policy#mint-var) monetization variable in your DataCapture policy.  
  
#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **199807323** | **A prepaid developer is set as a postpaid developer after updates to the prepaid developer.**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **198549304, 197730687, 196937143, 188370635, 187890034** | **Apigee displays improved error messages during rate plan creation.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **192987085** | **Fixed the**ApiProductNotFound** exception, which occurred when you deleted an API product but the deletion of associated rate plans was pending.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **188407113** | **Invalid value in the ConsumptionPricingType during rate plan creation displayed the 500 status code. Now the status code for an invalid value is 4xx.**  
  
  
#### Deprecations

This release includes the following deprecations:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-deprecated.svg) |  **The rateplans API doesn’t support the**paymentFundingModel** field.**   
  
---|---  
  
### November 3, 2021 - Apigee hybrid v1.6.2

On November 3, 2021, we released an updated version of the Apigee hybrid v1.6.2 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **202309278** | **Monetization: Eliminated a race condition that could make a prepaid developer's balance appear incorrect.**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **200648523** | **Trace Variable, is_request_blocked, was showing incorrect information.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **199807323** | **Updating Developer would reset the Developer billing type attribute**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **199541025** | **Transaction ID is now required to be unique when used with prepaid developer balance credit API.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **198549304, 197730687, 196937143, 188370635, 187890034** | **Error state for conflicting dates is now correct.**  
  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/upgrade). 

### November 3, 2021 - Apigee X

On November 3, 2021, we released an updated version of the Apigee X software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **OAuth JWT access tokens**  
New JWT operations allow the OAuthV2 policy to generate, verify, and refresh access tokens that conform to the [JWT token standard](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-access-token-jwt). See [Using JWT OAuth tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/using-jwt-oauth).  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Cloud Logging**  
New `<CloudLogging>` element in the [MessageLogging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy) lets you log messages to [Cloud Logging](https://cloud.google.com/logging).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **PublishMessage policy**  
The PublishMessage policy lets you publish your API proxy flow information to a Google Cloud [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) topic.

  * **Policy document:** [PublishMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy)

  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **SetDialogflowResponse policy**  
The SetDialogflowResponse policy facilicates easy integration of Apigee with Google's [Dialogflow](https://cloud.devsite.corp.google.com/dialogflow/cx/docs). The SetDialogflowResponse policy lets you process and format the response data from your backend systems before sending the data as a [WebhookResponse](https://cloud.devsite.corp.google.com/dialogflow/cx/docs/concept/webhook#webhook-response) to a Dialogflow agent.

  * **Policy document:** [SetDialogflowResponse policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy)

  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **ParseDialogflowRequest policy**  
The ParseDialogflowRequest policy facilicates easy integration of Apigee with Google's [Dialogflow](https://cloud.devsite.corp.google.com/dialogflow/cx/docs). The ParseDialogflowRequest policy lets you process the WebhookRequest from a Dialogflow agent before sending the request data to your backend systems.

  * **Policy document:** [ParseDialogflowRequest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy)

  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **AssertCondition policy**  
The AssertCondition policy lets you evaluate a conditional statement at runtime in your request or response flows. You can define a condition based on your flow variables, and use this policy to assert the condition.

  * **Policy document:** [AssertCondition policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy)

  
  
### October 28, 2021 - Apigee hybrid v1.6.1

On October 28, 2021, we released an updated version of the Apigee hybrid v1.6.1 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **203462573** | **The StorageClass set in overrides was not honored.**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **202560276** | **AKS - containerd broke`apigee-logger`.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **200918549** | **There was an issue when using forward proxy with the ApigeeConnect agent.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **198036824** | **The`securityContext` was empty when it should have been populated.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **197910247** | **SetDialogflowResponse Policy - JSONPath expressions were not working.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **197711066** | **Cluster upgrade failed due to PDB (PodDisruptionBudget) policy not being met.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **196024622** | **Hybrid images contained keys.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **196024483** | **Hybrid images did not set USER instruction when building the container.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **196024483** | **Hybrid containers were running as root for`apigee-mart-server`, `apigee-synchronizer`, `apigee-runtime` and `apigee-envoy`.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **190679584** | **There was an Incorrect error message on deploying AssertCondition policy with invalid condition.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **180672249** | **FlowCallout succeeded, although SharedFlow had errors in deployment.**  
  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/upgrade). 

### October 27, 2021 - Integrated portal

On October 27, 2021, we released an updated version of the Integrated portal software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **201417419** | **Portal should not throw an error when the user provides an invalid URL**  
An issue was fixed where an invalid URL when importing an Open API Specification file would cause an internal server error.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **196392985** | **Issue loading built-in identity provider pages**  
Fixed issue where built-in identity provider sign-in and account creation pages would in some situations not correctly load.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **193158000** | **From Email In the SMTP settings should be validated**  
The **From Email** field in the SMTP settings is now validated.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **138719777** | **From Email In the SMTP settings should be validated to be the right format**  
The **From Email** field in the SMTP settings is verified to be of the proper email address format.  
  
### October 21, 2021 - Apigee hybrid v1.5.5

On October 21, 2021, we released an updated version of the Apigee hybrid v1.5.5 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **203468593** | **Corrected the`storageclass` property name.**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **203462573** | **The StorageClass set in overrides was not honored.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **202560276** | **AKS -`containerd` broke `apigee-logger`.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **198036824** | **The`securityContext` was empty when it should have been populated.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **197711066** | **Cluster upgrade failed due to PDB (PodDisruptionBudget) policy not being met.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **196024483** | **Hybrid images did not set USER instruction when building the container.**  
  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade). 

### October 13, 2021 - UI

On October 13, 2021, we released an updated version of the UI software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **TraceCapture policy (Preview)**  
The **[Add Policy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui#attaching-a-policy-to-a-flow)** dialog in the Apigee UI now shows the TraceCapture policy.   
If you have [enabled distributed trace](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-distributed-trace) for your Apigee runtime, the TraceCapture policy lets you add additional variables to your Apigee runtime's trace data. For more information, see [TraceCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy).  
---|---  
  
### October 6, 2021 - Connectors (GA)

On October 6, 2021, we released an updated version of the Connectors (GA) software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Support for display names in the Connectors UI**  
Connectors now supports the addition of a `display name`  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Service Account authentication for Connection workloads**  
With this release, Connectors now supports the use of customer Service Accounts as an authentication option for most Connectors workloads.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Support for pagination in**LIST** calls to Entity APIs**  
Connectors now support the option to paginate **LIST** calls to Entity APIs from Application Integration. With the pagination option, Application Integration can now request lists of entities in batches using the **Connector task**.  
  
### October 6, 2021 - Apigee Integration (GA)

On October 6, 2021, we released an updated version of the Apigee Integration (GA) software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Support for regionalization**  
Apigee Integration now supports data plane and runtime regionalization. During the integration creation process, the user can now select the specific region for data and execution to reside. More details are available in [Supported regions](https://docs.cloud.google.com/api-platform/integration/system-limits#supported-regions).  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Support for Connectors**  
With this release, Apigee Integration supports Connectors. Integration customers can now utilize connectors for Cloud SQL (MySQL), BigQuery, Salesforce, and services as a first-class experience. All connectors are regionalized and support a consistent interface for accessing and modifying entities, including auto-complete references and pagination.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Availability of the Apigee Integration API**  
The Apigee Integration API is available. Customers can use the API to manage the entire Integration lifecyle.  
  
### October 05, 2021 - UI

On October 05, 2021, we released an updated version of the UI software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  N/A  | **Fix bug delete dialog does not open**  
Previously, on click of delete dialog, the dialog was not appearing, this fixes it  
---|---|---  
  
### September 23, 2021 - UI

On September 23, 2021, we released an updated version of the UI software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **200700375** | **Fixed API products sorting issue in UI.**  
Previously, sorting was disabled on the API products page. Sorting is now enabled.  
---|---|---  
  
### September 23, 2021 - Apigee hybrid v1.5.4

On September 23, 2021, we released an updated version of the Apigee hybrid v1.5.4 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **196095557** | **Fixed proxy high response times**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **193799009** | **Fixed wrong status code shown on trace with ServiceCallout in PostClientflow**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **193520269** | **Fixed Apigee UI not showing the trace UI**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **181259284** | **Fixed unresolved flow variables`system.region.name` and `system.pod.name`**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **173738907** | **Fixed support resource request/limit in`override.yaml` in `apigee-metrics`**  
  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade). 

### September 23, 2021 - Apigee hybrid v1.4.5

On September 23, 2021, we released an updated version of the Apigee hybrid v1.4.5 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **191339147** | **Updated env-scoped JavaScript resource file fails to update in runtime instance**  
When updating JavaScript resource files, all pods now pick up the new version of the resource file within one minute.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **185849286** | **java.lang.NoClassDefFoundError in Java Callout after upgrading from 1.3.5 to 1.4.2**  
After upgrading from Apigee hybrid v1.3.5 to v1.4.2, a `NoClassDefFoundError` in one of the proxies/shared flows.  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/upgrade). 

### September 22, 2021 - Apigee X

On September 22, 2021, we released an updated version of the Apigee X software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Configurable API Proxies (Preview release)**  
Apigee now supports the use of [Configurable API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/configurable-api-proxies) to quickly create and deploy a lightweight proxy with standard gateway features using industry-standard YAML syntax. For details, see [Create a configurable API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/create-configurable-proxy).  
---|---  
  
### September 13, 2021 - Apigee hybrid v1.6.0

On September 13, 2021, we released an updated version of the Apigee hybrid v1.6.0 software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Support for Google Auth and OpenID Connect tokens**  
Apigee supports using [Google OAuth tokens](https://developers.google.com/identity/protocols/oauth2) or [OpenID Connect tokens](https://developers.google.com/identity/protocols/oauth2/openid-connect) to authenticate API proxy target requests to Google services.Google OAuth tokens can be used to call many kinds of Google services, such as [Cloud Logging](https://cloud.google.com/logging) and [Secret Manager](https://cloud.google.com/secret-manager). OpenId Connect tokens allow you to connect to gRPC-based services, such as [Cloud Run](https://cloud.google.com/run).**Document:** [Using Google authentication](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview)  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **A new`ProxyEndpoint` configuration parameter was added: `request.queryparams.ignore.content.type.charset` This parameter tells the proxy to ignore the `charset` parameter of the `Content-Type` header when processing the request URL.**  
**Document:** [ProxyEndpoint configuration elements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint-proxyendpointconfigurationelements)  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **A list of the Kubernetes resources and custom resources that are used by Apigee installations**  
**Document:** [Kubernetes and custom resources used by Apigee](https://docs.cloud.google.com/apigee/docs/hybrid/kubernetes-resources)  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Apigee provides 64-bit executables for`apigeectl` for Linux, MacOS, and Windows, and no longer provides 32-bit executables.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **The`targetv2/latencies_percentile` metrics are available in this release. The `targetv2/latencies_percentile` are exported to Cloud Monitoring with the Targetv2 monitored resource.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **The Quota limit is increased to 5 yrs.**  
**Document:** [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits)  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **GraphQL policy verification is available with Apigee hybrid 1.6.0.**  
**Document:** [Using GraphQL](https://docs.cloud.google.com/apigee/docs/api-platform/develop/graphql)  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Passthrough is now supported for unsupported content encoding in[streaming mode](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-streaming).**  
  
  
#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **196428068** | **Removed the test directories from the`gcloud` binaries.**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **196095557** | **Fixed High proxy response times.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **188634197** | **Validation for the environment level kvm encryption key has been fixed.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **186417633** | **Cassandra node would restart.**  
An issue with the datastore controller was causing the last cassandra pod to restart in a cluster. For example, if a cluster has three cassandra pods, then apigee-casssndra-default-2 would be periodically restarted  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **182199399** | **Fixed null pointer exception when using target server with client auth enabled.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **174732169** | **Fixed issue with dropping`syslog` messages.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **161491661** | **An issue was fixed where the`client.scheme` flow variable was always set to `http` when an additional gateway was specified as described in [Enable non-SNI and HTTP clients](https://docs.cloud.google.com/apigee/docs/hybrid/latest/enable-non-sni). We now return either `http` or `https` correctly.**  
  
  
#### Additional notes

**Note:** Apigee hybrid 1.6.0 includes the fixes and features in the following releases:

  * Apigee hybrid v1.5.1
  * Apigee hybrid v1.5.2
  * Apigee hybrid v1.5.3
  * Apigee X - July 26, 2021
  * Apigee X - August 30, 2021



#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/upgrade). 

### September 8, 2021 - Connectors (Private Preview)

On September 8, 2021, we released an updated version of the Connectors (Private Preview) software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Support for display names in the Connectors UI**  
This is a Private preview of the connectors feature for Application Integration on Apigee X. With the release of connectors, Application Integration customers can connect to business applications, technologies, and other data sources using the native protocols of each target application. With connectors, both Google Cloud services and third-party business applications are exposed to Application Integration through a transparent, standard interface. Apigee Integration users can quickly connect to a growing pool of applications and systems of record without the need for protocol-specific knowledge or the use of custom code.With this release, the connectors platform is now available within the [Cloud console](https://console.cloud.google.com) under **Apigee > Connectors**. Users with Apigee credentials, Apigee X orgs, and connectors entitlement can use the connectors UI to create new connections for use in Application Integration.Connectors supported in this release:

  * [BigQuery connection](https://docs.cloud.google.com/apigee/docs/api-platform/connectors/configure-bigquery)
  * [Salesforce connection](https://docs.cloud.google.com/apigee/docs/api-platform/connectors/configure-salesforce)
  * [Cloud SQL for MySQL connection](https://docs.cloud.google.com/apigee/docs/api-platform/connectors/configure-mysql)
  * [Cloud SQL for PostgreSQL connection](https://docs.cloud.google.com/apigee/docs/api-platform/connectors/configure-postgresql)
  * [Pub/Sub connection](https://docs.cloud.google.com/apigee/docs/api-platform/connectors/configure-pubsub)

  
---|---  
  
#### Learn more

  * [What are connectors?](https://docs.cloud.google.com/apigee/docs/release/notes/apigee/docs/api-platform/connectors/about-connectors)



### August 30, 2021 - Apigee X

On August 30, 2021, we released an updated version of the Apigee X software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **198213668** | **Fixed issue where the`system.region.name` flow variable was empty. The flow variable is now populated with the runtime pod region.**  
  
---|---|---  
  
### August 23, 2021 - UI

On August 23, 2021, we released an updated version of the UI software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Redesigned API products UI**  
The new UI look and feel for creating and editing API products is being rolled out gradually over time. Not all users will see the UI changes immediately. For more information, see [Managing API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products).  
---|---  
  
### August 20, 2021 - UI

On August 20, 2021, we released an updated version of the UI software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Improved error messages on Apps and API product pages**  
On the Apps and API Products page, we've improved error messages that occur when data cannot be loaded because the Apigee runtime could not be reached.  
---|---  
  
#### Deprecations

This release includes the following deprecations:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-deprecated.svg) |  **Deprecate payment funding model for Monetization rate plans**   
The ability to set the payment funding model using the Apigee UI or API has been deprecated.   
---|---  
  
### August 16, 2021 - Integrated portal

On August 16, 2021, we released an updated version of the Integrated portal software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **196392985** | **Portal sign in and account creation pages not loading correctly**  
Fixed issue where built-in identity provider sign in and account creation pages would not correctly load in some situations.  
---|---|---  
  
### August 10, 2021 - UI

On August 10, 2021, we released an updated version of the UI software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Improve encryption key selection for Apigee X paid org provisioning wizard**  
The Apigee X wizard for paid orgs now lets you select or create encryption keys directly from within the wizard. The change impacts the steps for [creating an organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-org) and a [runtime instance](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-instance).  
---|---  
  
### August 10, 2021 - Integrated portal

On August 10, 2021, we released an updated version of the Integrated portal software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **194145871** | **Team selection to own an app not reflected**  
An issue was fixed where selecting a team to own an app was not reflected in the user interface in the integrated portal.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **192497623** | **Internal server error**  
An issue was fixed where under high load publishing changes to pages or APIs sometimes resulted in an internal server error.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **192338410** | **SSO logins and SAML configurations**  
An issue was fixed where SSO logins and SAML configurations were broken after updating the custom domain.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **191777242** | **Category selector styling**  
A minor issue was fixed with category selector styling.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **187324480** | **Custom domain deployment failing**  
An issue was fixed with custom domain deployment failing in the middle of the process.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **181132931** | **Loading the specs page results in error**  
An issue was fixed where loading the specs page resulted in an error in some cases.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **156001978** | **Security enhancement**  
Added `Cache-Control: private` to several integrated portal resources.  
  
### August 6, 2021 - Apigee hybrid v1.5.3

On August 6, 2021, we released an updated version of the Apigee hybrid v1.5.3 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **195195354** | **DNS error when configuring forward proxy with hybrid 1.5.2.**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **194658442** | **DNS resolution fails when using a use a custom .service domain.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **193799009** | **Wrong status code shown on trace with Service callout in PostClientflow.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **193520269** | **Apigee UI is not showing the trace UI #5G in hybrid v1.5.1.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **191169444** | **When using Google Cloud Monitoring, the Apigee ServiceCallout policy was not displayed in the Metrics explorer.**  
  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade). 

### August 6, 2021 - Apigee X

On August 6, 2021, we released an updated version of the Apigee X software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Google authentication support (Preview release)**  
Apigee now supports using [Google OAuth tokens](https://developers.google.com/identity/protocols/oauth2) or [OpenID Connect tokens](https://developers.google.com/identity/protocols/oauth2/openid-connect) to authenticate with Google services such as [Cloud Logging](https://cloud.google.com/logging) and [Secret Manager](https://cloud.google.com/secret-manager) and custom services running on certain Google Cloud products such as [Cloud Functions](https://cloud.google.com/functions) and [Cloud Run](https://cloud.google.com/run). For details, see [Using Google authentication](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview).  
---|---  
  
### July 28, 2021 - Integrated portal

On July 28, 2021, we released an updated version of the Integrated portal software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **194679083** | **Custom domain dropped for login_failure redirect**  
Fixed issue where a failed login would not correctly redirect to a custom domain when a custom domain is enabled.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **194265224** | **Failed authentication error messages need to be displayed**  
Fixed issue where a failed login would not correctly redirect to a custom domain when a custom domain is enabled.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **194145871** | **App owner doesn't reflect teams**  
Fixed issue where selecting a team to own an app was not reflected in the live portal UI.  
  
### July 27, 2021 - Apigee Integration (Private GA)

On July 27, 2021, we released an updated version of the Apigee Integration (Private GA) software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **New Data Mapping Editor for Data Mapping Task**  
The Data Mapping Editor now includes a new drag-and-drop interface for configuring input and output mappings. Application Integration variables are now listed directly on both sides of the Data Mapping Editor. Users can add mappings by dragging these variables into the corresponding input and output chips. With this release, data mappings are autosaved and can be reordered with drag and drop functionality. New mapping rows are automatically created when the table is filled. A summary of mapped variables can now be referenced at a glance from a panel in the integration editor, without opening the Data Mapping Editor.  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Availability of new Application Integration Tasks**  


  * **For Each Loop** This task enables users to add an integration task that makes repeated calls to a sub-integration from the main integration.
  * **While Loop** This task enables users to add an integration task that makes repeated calls to a sub-integration from the main integration until a specified condition is met.

  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Platform Events supported in Salesforce trigger**  
The Salesforce trigger can now be configured to listen to Salesforce Platform Events, in addition to Change Data Capture. Platform Events are now available for selection as an **Event type** in the Trigger configuration pane.When the event type is set to 'Platform Events' in the trigger, any event in the platform specified will trigger the integration.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Support for additional Data Mapping functions**  
With this release, support for additional Data Mapping functions has been added for a number of variable types. See the data mapping functions table in the [ Data mapping task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/data-mapping-task#supported-data-types) reference for a comprehensive list.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Fine-grained control for IAM permissions**  
With this release, Application Integration supports the ability to grant fine-grained user permission in the UI. For more information on setting IAM roles and permissions, see [Apigee Integration access overview](https://docs.cloud.google.com/apigee/docs/api-platform/integration/integrations-access-permissions).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Regionalization support**  
Application Integration now supports regionalization. All data storage and processing takes place in the same Cloud region (default is US).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Deprovisioning support**  
With this release, upon a customer request to deprovision infrastructure or disable Application Integration, all user content and metadata persisted by Application Integration will be wiped out. Upon the deletion of an Apigee organization bound to a Google Cloud project, all user data is soft deleted. The data can be recovered if the project is restored within 30 days. After 30 days, all user data is permanently deleted.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Application Integration UI**  
Expanded and revised documentation for Application Integration.The Apigee [documentation for Application Integration](https://docs.cloud.google.com/apigee/docs/api-platform/integration/what-is-apigee-integration) includes updated and expanded topics for all new features, as well as: 

  * Monitoring
  * Alerting
  * Application Integration UI updates and improvements

  
  
### July 26, 2021 - Apigee X

On July 26, 2021, we released an updated version of the Apigee X software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Update platform version of[Rhino](https://github.com/mozilla/rhino) (JavaScript engine) to version 1.7.12.**  
  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Update JavaScript policy to use latest supported language level supported by Apigee ([Rhino](https://github.com/mozilla/rhino) 1.7.12)**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **SpikeArrest policy enhancement is now generally available (GA)**  
A new element was added to the SpikeArrest policy: `<UseEffectiveCount>`. This element allows you to choose between distinct spike arrest algorithms.

  * Policy document: [SpikeArrest policy document](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#useeffectivecount).
  * Related document: [Comparing Quota and SpikeArrest policies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/comparing-quota-and-spike-arrest-policies).

  
  
#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **188202481** | **Add missing latency percentile metrics for certain policies.**  
An issue was fixed where latency metrics were not being recorded for certain policies. With this change, all policy latency percentiles will appear in **policyv2/latencies_percentile** metrics as expected.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **183218041** | **The VerifyJWT and VerifyJWS policies have been optimized for faster verification of both valid and invalid tokens.**  
  
  
### July 23, 2021 - Apigee hybrid v1.5.2

On July 23, 2021, we released an updated version of the Apigee hybrid v1.5.2 software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **193902071, 193904144** | ****  
A`create-service-account` script is now available to generate the required runtime service account (SA).  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **192997684** | **In some cases, property sets with environment scope were missing from the runtime pod.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **191745621** | **MART was not able to communicate with`*.googleapis.com` through a forward proxy.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **191339147** | **An updated environment-scoped JavaScript resource file failed to update in a runtime instance.**  
  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade). 

### July 9, 2021 - UI

On July 9, 2021, we released an updated version of the UI software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Add Access Routing to Eval wizard**  
The Apigee X [Eval wizard](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/eval-orgs#access-routing) now includes an Access Routing step. This step lets you choose whether to expose your new cluster to external requests or to keep it private (and only allow requests from within your VPC).  
---|---  
  
### July 9, 2021 - Integrated portal

On July 9, 2021, we released an updated version of the Integrated portal software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **192497623** | **429s and 503s, from bucket storage are being reported as 5XX**  
Fixed issue where under high load publishing changes to Pages or APIs might result in an internal server error.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **192338410** | **Portal SP metadata URL returns 500**  
Resolved issue with broken SSO logins and SAML configuration after updating the custom domain.  
  
#### Security updates

This release includes the following security updates:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | 192335308 | **Miscellaneous security fixes**  
  
---|---|---  
  
### July 2, 2021 - Apigee hybrid v1.5.1

On July 2, 2021, we released an updated version of the Apigee hybrid v1.5.1 software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Reverted the number of buckets resulting in optimization of the proxy-metrics pod's memory utilization.**  
  
---|---  
  
#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **191339147** | **[HYBRID] Updated env-scoped JavaScript resource file fails to update in runtime instance**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **189118133** | **Fix data cleanup logging and insertion logic**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **187532454** | **[Hybrid] Implement Gcloud Config Proxy Settings for Backup and Restore**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **186748502** | **Redis envoy stuck without any state**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **186215334** | **[HYBRID] Cassandra backup doesn't respect httpProxy setting**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **185972246** | **Mitigate failure in Java callout for Envoy integration**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **174732169** | **Dropped syslog messages**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **169257984** | **Hybrid runtime does not load certs from`key_cert` aliases when keystore is used as truststore**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **161491661** | **Hybrid v1.2 - Flow variables are not populated correctly**  
  
  
#### Security updates

This release includes the following security updates:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | 192259560 | **Change default ciphers to support BoringSSL and FIPS**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | 181864314, 183457561 | **Miscellaneous security updates**  
Apigee hybrid v1.5.1 includes miscellaneous security updates for multiple container vulnerabilities.  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade). 

### June 24, 2021 - Integrated portal

On June 24, 2021, we released an updated version of the Integrated portal software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **190747726** | **Performance issues with portal**  
Fixed an issue causing poor performance in SmartDocs when the OpenAPI Specification used schemas that were either very large or used many references.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **185517530** | **List API products alphabetically when viewing apps in the portal**  
When creating or editing an app, API products are now listed alphabetically.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **184544952** | **Spec text wrapping automatically**  
A fix has been implemented to SmartDocs to prevent content from being cut off in certain cases. Smartdocs now wraps text before truncating.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **182687976** | **Duplicate index ID appears on various pages in the portal**  
An incorrectly duplicated CSS selector ID has been removed.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **181903693** | **Broken link in New Account Notification Email default template**  
New account notification emails now contain a link to the users section of the portal administation pages.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **163330599** | **APIx - Oauth Implicit scopes do not render in portal**  
The authorize modal in the live portal now allows scope selection for Oauth2 security schemes.  
  
### June 18, 2021 - Apigee hybrid v1.5.0

On June 18, 2021, we released an updated version of the Apigee hybrid v1.5.0 software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **CORS policy**  
A new CORS policy allows developers to create a new CORS policy to set `Access-Control-Allow-Origin`, `Access-Control-Allow- Headers`, `Access-Control-Max-Age`, and `Access- Control-Allow-Methods`, and to handle CORS preflight requests out of the box.

  * **Policy document:** [ CORS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy)
  * **Updated existing documents:**
    * [Adding support for CORS](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy#addingsecurityandcorssupporttoyourapi-addingsupportforcors)
    * [Framework-style coding](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development#developmentstandards-frameworkstylecoding)
    * [Enabling CORS](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development#apiproxydevelopment-enablingcors)
    * [Configuring your API proxy to support the Try this API panel](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#cors)
    * [Where can you use message templates?](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#where-can-you-use-message-templates)
    * [Adding CORS support to an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/adding-cors-support-api-proxy)

  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **GraphQL support**  
A new GraphQL policy parses GraphQL request/response payloads and outputs Apigee flow variables.

  * **Policy document:** [GraphQL policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/graphql-policy)
  * **How-to document:** [Using GraphQL](https://docs.cloud.google.com/apigee/docs/api-platform/develop/graphql)

New GraphQL operations were added to the API product definition. These operations let you control which GraphQL operations have access API resources and specify quota limits.

  * **API product document:** [GraphQL operations](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#add)

  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **ExternalCallout policy**  
A new ExternalCallout policy allows developers to send [gRPC](https://cloud.google.com/endpoints/docs/grpc/about-grpc) requests to their gRPC server to implement custom behavior that isn't supported by Apigee policies.**Policy document:** [ExternalCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/external-callout-policy)  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Custom Java callout security enhancement**  
A custom Java callout security enhancement lets API developers change the default permissions for a Java callout.**Feature document:** [Adding a custom Java callout security policy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/adding-custom-java-callout-security-policy)  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Apigee hybrid now supports installation on Anthos on bare metal**  


  * **See:** [Apigee hybrid: supported platforms](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms)
  * **Updated existing documents:**
    * [Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-create-cluster#anthos-on-bare-metal)
    * [Step 3: Install ASM](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-asm#anthos-on-bare-metal)

  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Apigee hybrid now supports installation Anthos (attached clusters) on OpenShift**  


  * **See:** [Apigee hybrid: supported platforms](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms)
  * **Updated existing documents:**
    * [Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-create-cluster#openshift)
    * [Step 3: Install ASM](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-asm#openshift)

  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **`create-service-account` tool enhancements**  
The `create-service-account` tool now supports commands to create:

  * Individual service accounts
  * All services accounts
  * A single service account for test environments

**Reference document:** [create-service-account](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/create-service-account)  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **SpikeArrest policy enhancement (Preview release)**  
A new element was added to the SpikeArrest policy: `<UseEffectiveCount>`. This element allows you to choose between distinct spike arrest algorithms.

  * **Policy document:** [SpikeArrest policy document](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#useeffectivecount).
  * **Related document:** [Comparing Quota and SpikeArrest policies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/comparing-quota-and-spike-arrest-policies)

  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **OAuthV2 policy enhancement**  
A new element was added to the OAuthV2 policy: `<RFCCompliantRequestResponseElement>`. This element lets the policy comply to RFC6749 standards and enables related behaviors.**Policy document:** [OAuthV2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#RFCCompliantRequestResponseElement) document.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **The JavaCallout policy now supports Oracle JDK 11 and OpenJDK 11**  
**Policy document:** [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy)  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Custom annotations**  
Added the ability to add annotations, which are key/value maps used to attach metadata to Apigee hybrid Kubernetes pods.**Updated existing documents:**

  * [Custom annotations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/customize-services#custom-annotations)
  * [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/config-prop-ref)

  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Enable Workload Identity**  
Added the ability to enable Workload Identity with Apigee hybrid.**Feature document:** [Enabling Workload Identity with Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/enable-workload-identity)  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Redis in-memory storage**  
`apigeectl` now includes a `--redis` flag to configure the Redis in-memory storage component.**Updated existing document:** [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/cli-reference)  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Updates were made to multiple limits values. New items were added in the Environment and Organization, New Portals, and Debug sections.**  
**Limits document:** [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits)  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **A new section was added to the[Cassandra troubleshooting guide](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/ts-cassandra#create-a-client-container-for-debugging) that explains how to create a client container from which you can access Cassandra debugging utilities.**  
  
  
#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **178079779** | **GKE on-prem hybrid 1.4 trace tool was not showing requests flowing.**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **177936460** | **Reduce resource allocated for authnz container for MART.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **174431114** | **Hybrid upgrade from 1.3.4rc3 to 1.4.0rc2 failed due to connectivity error with the seed node.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **168167050** | **A few hybrid pods were running as root user. This has been changed so that they now all run as non-root user.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **161170762** | **HPA v2beta2 allows scaling on CPU, memory, and custom metrics.**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **143505709** | **Non-ASCII characters were not supported in encryption keys.**  
  
  
#### Security updates

This release includes the following security updates:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | 179529202 | **[CVE-2019-9169](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9169)**  
In the GNU C Library (aka glibc or libc6) through 2.29, proceed_next_node in posix/regexec.c has a heap-based buffer over-read via an attempted case-insensitive regular-expression match.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | 179528920 | **[CVE-2018-6551](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-6551)**  
The malloc implementation in the GNU C Library (aka glibc or libc6), from version 2.24 to 2.26 on powerpc, and only in version 2.26 on i386, did not properly handle malloc calls with arguments close to SIZE_MAX and could return a pointer to a heap region that is smaller than requested, eventually leading to heap corruption.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | 179529260 | **[CVE-2018-6485](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-6485)**  
An integer overflow in the implementation of the posix_memalign in memalign functions in the GNU C Library (aka glibc or libc6) 2.26 and earlier could cause these functions to return a pointer to a heap area that is too small, potentially leading to heap corruption.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | 179529233 | **[CVE-2018-1000001](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000001)**  
In glibc 2.26 and earlier there is confusion in the usage of getcwd() by realpath() which can be used to write before the destination buffer leading to a buffer underflow and potential code execution.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | 173506631 | **[CVE-2019-17195](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17195)**  
Connect2id Nimbus JOSE+JWT before v7.9 can throw various uncaught exceptions while parsing a JWT, which could result in an application crash (potential information disclosure) or a potential authentication bypass.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | 177234739 | **Miscellaneous security updates**  
Apigee hybrid v1.5.0 includes miscellaneous security updates for multiple container vulnerabilities.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | 179272826 | **[CVE-2019-14697](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-14697)**  
musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | 179272826 | **[CVE-2018-1000517](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000517)**  
BusyBox project BusyBox wget version prior to commit 8e2174e9bd836e53c8b9c6e00d1bc6e2a718686e contains a Buffer Overflow vulnerability in Busybox wget that can result in heap buffer overflow. This attack appear to be exploitable via network connectivity. This vulnerability appears to have been fixed in after commit 8e2174e9bd836e53c8b9c6e00d1bc6e2a718686e.  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade). 

### June 9, 2021 - Apigee hybrid v1.4.4 (_deprecated_)

On June 9, 2021, we released an updated version of the Apigee hybrid v1.4.4 (_deprecated_) software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **187532454** | **Implement Gcloud Config Proxy Settings for Backup and Restore**  
Implemented a change in the Cassandra backup and restore scripts that set the proxy settings in `gcloud config` if the `http_proxy` environment variable setting is present.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **186215334** | **Cassandra backup doesn't respect httpProxy setting**  
Added the `http_proxy` and `https_proxy` `env` variables to the Cassandra pods and Cassandra backup job pod when the `httpProxy` setting is configured.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **185849286** | **java.lang.NoClassDefFoundError in Java Callout after upgrading from 1.3.5 to 1.4.2**  
After upgrading from Apigee hybrid v1.3.5 to v1.4.2, a `NoClassDefFoundError` in one of the proxies/shared flows.  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/upgrade). 

### June 07, 2021 - Apigee X

On June 07, 2021, we released an updated version of the Apigee X software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **186766347** | **MP should correctly handle DNS errors and not report them as connection failures**  
  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **185849286** | **Fixes for java.lang.NoClassDefFoundError in Java Callout during proxy deployment**  
  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **169257984** | **Hybrid runtime does not load certs from key_cert aliases when keystore is used as truststore**  
  
  
#### Security updates

This release includes the following security updates:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | 185998748 | **Miscellaneous Security updates and fixes.**  
  
---|---|---  
  
### May 24, 2021 - Apigee public cloud offering

On May 24, 2021, we released an updated version of the Apigee public cloud offering software.

#### Security updates

This release includes the following security updates:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | N/A | **Miscellaneous security updates and fixes**  
This release includes miscellaneous security updates and fixes.  
---|---|---  
  
### May 19, 2021 - UI

On May 19, 2021, we released an updated version of the UI software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Unified UI for provisioning**  
The paid and eval provisioning wizards have been combined into a single UI. For more information, see [Introduction to provisioning](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro).  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Shared VPCs**  
The documentation now includes instructions on provisioning an org with shared VPCs. This information is described in eval and paid org provisioning, using either the command line or the UI/wizard. For more information, see [Introduction to provisioning](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Architectural overviews**  
The documentation now includes sections that discuss components created during the Apigee X provisioning process and routing flows in detail. For more information, see [Architectural overview](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/overview) and [Southbound networking patterns](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Multi-region configurations**  
The documentation now includes instructions on how to [add a new region](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/multi-region) to your org.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Using application and disk keys in command line provisioning**  
The documentation has been updated to include instructions on how to create and use application and disk keys when provisioning on the command line. In addition, the [encryption key doc](https://docs.cloud.google.com/apigee/docs/api-platform/security/encryption-keys) has been refactored.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Wizard updates**  
The documentation now reflects updates to the provisioning wizard.  
  
### May 13, 2021 - UI

On May 13, 2021, we released an updated version of the UI software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Trace tool renamed to Debug tool**  
The Trace tool has been renamed to the [Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview).  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Fault codes added to the Anomaly Events view.**  
The [Anomaly Events](https://docs.cloud.google.com/apigee/docs/aapi-ops/anomaly-detect-ui) view now displays the faultcode-level cause for each anomaly.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Enhancements to provisioning wizard.**  
The [provisioning wizard](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview#about-the-apigee-provisioning-wizard) now has the following enhancements: 

  * The Compute Engine API is now enabled for Apigee evaluation, which avoids potential problems the during the networking step.
  * In the networking step of the provisioning wizard, you can now set up peering using a Shared VPC network if the current project is connected to a Shared VPC host project. **Note:** If the selected network is not peered properly and you don't have permission to update the peering in the host project, the provisioning wizard displays a warning with instructions to set up peering by contacting a Shared VPC Admin of the host project.

  
  
### May 5, 2021 - Apigee Integration (Private Preview)

On May 5, 2021, we released an updated version of the Apigee Integration (Private Preview) software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Apigee Integration (Private Preview release)**  
This is a Private preview of the Application Integration feature for Apigee X. Application Integration extends the Apigee API Management platform to include core integration features—connectors, an integration engine, and data transformation tools. Application Integration offers business organizations of all sizes the tools needed to connect and manage the multitude of software applications required to support business operations in a digital world.With this release, Application Integration is now available within the Apigee UI alongside API Proxies as Integrations. Users with Apigee credentials, Apigee X orgs, and Application Integration entitlement can use the UI to create new integrations and access Integration features.For more information, see [What is Apigee Integration?](https://docs.cloud.google.com/apigee/docs/api-platform/integration/what-is-apigee-integration)  
---|---  
  
### May 3, 2021 - Apigee hybrid v1.4.3

On May 3, 2021, we released an updated version of the Apigee hybrid v1.4.3 software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **[KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy)**  
KVM `private` prefix behavior has been updated. The new behavior is as follows:Use the `private.` attribute with all variables when accessing a KVM with the `GET` command to hide the KVM information in a debug (Trace) session. If the `private.` attribute is not used, the KVM is still encrypted; however, the KVM information will appear decrypted in the debug (Trace) session. An exception is no longer thrown if an encrypted entry is retrieved without the `private.` prefix.Because all KVMs are now encrypted, the **Encrypt** check box has been removed from the **Admin > Environments > Key Value Maps > Add key value map** window.Clear text KVMs are deprecated.  
---|---  
  
#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **185902294** | **Revert the number of bucket increase for proxy/policy/target latency metrics**  
A recent change to the size of latency buckets caused memory problems and has been rolled back to the previous size.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **185508757** | **KVM Read operation failed for encrypted KVM without private prefix.**  
The KVM `private` prefix behavior has been updated in this patch.  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/upgrade). 

### April 27, 2021 - UI

On April 27, 2021, we released an updated version of the UI software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **185176375** | **Enhance the error message shown when Apigee service account does not have permission to use Cloud KMS key**  
A more detailed error message is now displayed when the Apigee service account does not have permission to use a Cloud KMS key provided through the Provisioning UI. The error message now includes buttons to copy the Apigee service account email, open the Cloud KMS UI, and re-check the Apigee service account's permission for the key.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **184888948** | **Restrict peering CIDR ranges based on billing type**  
Peering CIDR ranges are now restriced based on billing type when creating an instance in the Instance Manager.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **182910454** | **Show the anomaly breakdown details in the Anomaly Events dashboard**  
The anomaly breakdown details are now shown in the Anomaly Events dashboard.  
  
### April 26, 2021 - Limited preview: Apigee local development and archive deployment

On April 26, 2021, we released an updated version of the Limited preview: Apigee local development and archive deployment software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Limited preview: Apigee local development and archive deployment**  
**Note:** To enable and use these features, contact [Apigee Sales](https://cloud.google.com/contact/?direct=true&pre_product=).This is a **limited preview release** of local development using Apigee in Visual Studio Code (VS Code) and Apigee archive deployment. This release enables you to integrate API platform management with the software development lifecycle (SDLC) that you use to develop, test, and deploy applications.During **local development** , use Apigee in VS Code to develop your API proxies and verify the functionality through unit and manual testing against the Apigee Emulator (local runtime). During **archive deployment** , deploy to Apigee X for integration testing and release, leveraging an **archive** that contains the complete environment and API proxy configuration.For more information, see [Overview of local development using Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/overview).  
---|---  
  
### April 19, 2021 - Monetization

On April 19, 2021, we released an updated version of the Monetization software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Apigee monetization GA**  
Apigee monetization is now generally available (GA). As an API provider, you need an easy-to-use and flexible way to monetize your APIs so that you can generate revenue for the use of your APIs. Using Apigee monetization, you can add a monetization rate plan to an API product that charges developers or pays them through revenue sharing for the use of your APIs. For more information, see [Overview of Apigee monetization](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview).  
---|---  
  
### April 18, 2021 - UI

On April 18, 2021, we released an updated version of the UI software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Instances UI**  
Apigee added an Instances UI, which lets you create and delete instances. For more information, see [Creating instances](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances).  
---|---  
  
### April 8, 2021 - UI

On April 8, 2021, we released an updated version of the UI software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **182232515** | **Update layout of the Provisioning UI from panel to card-based**  
The layout of the Provisioning UI has been enhanced to be card-based.  
---|---|---  
  
### March 24, 2021 - UI

On March 24, 2021, we released an updated version of the UI software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **182301830  
182301842** | **Add pricing plans to Provisioning wizard**  
On the GCP project selection page of the Provisioning wizard, after entering a GCP project ID if the GCP project is not currently entitled to Apigee the available pricing plans are now listed.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **182234032** | **Add Enable APIs to provisioning flow checklist**  
Enable APIs is now listed as a step in the provisioning flow checklist.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **182216310** | **Add top navigation bar in Provision wizard**  
The top navigation bar is now displayed in the Provisioning wizard.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **169762448** | **Update help/learn more links to point to Apigee X documentation**  
The help and learn more links have been updated to point to the Apigee X documentation (instead of Apigee Edge).  
  
### March 24, 2021 - Analytics/API monitoring

On March 24, 2021, we released an updated version of the Analytics/API monitoring software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Advanced API Operations**  
This is the GA release of Apigee's [Advanced API Operations](https://docs.cloud.google.com/apigee/docs/aapi-ops) (AAPI Ops), which provides tools to help you ensure that your APIs stay up and running as intended. AAPI Ops automatically detects unusual patterns in API traffic—called anomalies—such as spikes in latency or error rate.AAPI Ops enables you to:

  * [Detect anomalies](https://docs.cloud.google.com/apigee/docs/aapi-ops/anomaly-detect-ui) and view them in the Anomaly Events dashboard
  * [Investigate anomalies](https://docs.cloud.google.com/apigee/docs/aapi-ops/anomaly-detect-ui#viewing-anomalies-in-the-api-monitoring-dashboard)
  * [Create anomaly alerts](https://docs.cloud.google.com/apigee/docs/aapi-ops/create-alerts)

  
---|---  
  
### March 18, 2021 - Integrated portal

On March 18, 2021, we released an updated version of the Integrated portal software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **172942224** | **Background shading for page content is inconsistent**  
Fixed inconsistent shading for page content that is not currently in focus and some navigation issues when the Advanced editor panel was displayed on the Themes page.  
---|---|---  
  
### March 10, 2021 - UI

On March 10, 2021, we released an updated version of the UI software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **181046483** | **Trace UI unexpectedly hides the transaction list when hovering on a policy**  
An issue has been fixed that was causing the Trace UI to unexpectedly hide the transaction list when hovering on a policy.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **179579560** | **Loading the API proxy develop page results in a series of error messages (infinite)**  
An issue has been fixed that was causing the API proxy develop page to display a series of messages.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **169252631** | **Remove LDAP policy from UI**  
The LDAP policy is not supported by Apigee X and has been removed from the policy list in the UI.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **161658025** | **SharedFlow deployment failed silently**  
JavaCallout did not validate ClassName allowing SharedFlow deployment to fail silently.  
  
### March 4, 2021 - Integrated portal

On March 4, 2021, we released an updated version of the Integrated portal software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Customizing your domain using a Google load balancer**  
The steps to customize your domain for an integrated portal have been updated to describe how to use a Google load balancer for your incoming client requests. For more information, see [Customizing your domain](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-domain).  
---|---  
  
#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **181238112** | **Change "Entitlements" heading on Audience page for clarity**  
The title of the section that shows entitlements for an audience has changed to Content visibility entitlements.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **180497246** | **Clean up duplicate API doc rows**  
An issue was fixed that was causing duplicate APIs that referenced the same API product to be listed on the APIs page. Attempting to edit these APIs or view them in the integrated portal would throw errors.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **180343973** | **Create API doc returns`4xx` but creates resource**  
When creating an API doc, if there was a problem taking a snapshot of the requested spec, a `4xx` would be returned, but the API would still be created. Now, the API doc creation will fail in this scenario.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **179953039** | **Team members cannot leave teams**  
An issue has been fixed that was preventing team members from removing themselves from a team.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **159256416** | **Bearer authentication HTTP security definition rendering problem in integrated portal**  
When a bearer authentication HTTP security scheme is defined in a spec, the authorize modal now prompts for a Bearer Token in the integrated portal.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **156874569** | **Integrated portal does not render contact section in a spec**  
The integrated portal now renders the contact section of a spec.  
  
### March 2, 2021 - Apigee X

On March 2, 2021, we released an updated version of the Apigee X software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **181765488** | **Property sets do not work when defined at the API proxy level in Apigee X**  
An issue has been fixed with property sets defined at the API proxy level in Apigee X.  
---|---|---  
  
### March 1, 2021 - Apigee hybrid v1.4.2 (_deprecated_)

On March 1, 2021, we released an updated version of the Apigee hybrid v1.4.2 (_deprecated_) software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **180128329** | **Service ports**  
Kubernetes service ports were renamed to follow Istio standards.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **179891322** | **Backup and recovery**  
Backup and recovery of the Cassandra database without Google Cloud was not working in some instances. See [Backup and recovery without Google Cloud](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cassandra-backup-non-gcs).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **179461749** | **Cassandra passwords**  
Non-default Cassandra passwords can now be configured using Kubernetes secrets.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **179332963** | **`create-service-account.sh` tool**  
The `create-service-account.sh` tool will now display an error when asked to create a service account without a role assigned. See [create-service-account](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/create-service-account).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **178829167** | **Synchronizer**  
When synchronizer would go down the error messages indicated apigee-runtime was down.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **178732212** | **Cassandra backup and recovery documentation**  
Documentation for Cassandra backup and recovery has been updated. See [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/backup-recovery).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **177950986** | **Hybrid EKS runtime to Cassandra SSL errors**  
Runtime pod was not able to communicate to cassandra in EKS cluster in some instances. The liveness call timeout was changed from seconds to milliseconds to match what the client expected.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **177681383** | **Watcher timeouts**  
Watcher has added timeouts to handle connection timeouts to Apigee management plane in order to properly handle the stale connections. This eliminates some conditions where apigee-watcher could become stuck.  
  
#### Security updates

This release includes the following security updates:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) | N/A | **This version includes a security update for a vulnerability in fluentd.**  
  
---|---|---  
  
#### Installation

For information on upgrading, see [Upgrading Apigee hybrid to version 1.4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/upgrade). 

### February 26, 2021 - Apigee hybrid v1.3.6 (_deprecated_)

On February 26, 2021, we released an updated version of the Apigee hybrid v1.3.6 (_deprecated_) software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **180128329** | **Kubernetes service port names**  
In Apigee hybrid version 1.3.6, Kubernetes service ports were renamed to follow Istio standards.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **179332963** | **create-service-account.sh tool**  
In Hybrid version 1.3.6 you can now specify a role as a parameter with the create-service-account.sh tool. See [create-service-account](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/create-service-account).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **178732212** | **Cassandra backup and recovery documentation**  
Documentation for Cassandra backup and recovery has been updated. See [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/backup-recovery).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **177681383** | **Watcher timeouts**  
Watcher has added timeouts to handle connection timeouts to Apigee management plane in order to properly handle the stale connections. This eliminates some conditions where apigee-watcher could become stuck.  
  
#### Installation

For upgrade instructions, see [Upgrading Apigee hybrid to version 1.3.6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade). 

### February 18, 2021 - Integrated portal

On February 18, 2021, we released an updated version of the Integrated portal software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **179911854** | **Multiple sets of API documentation associated with the same API product**  
Fixed an issue that would in some circumstances allow more than one set of API documentation to be created for a single API product.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **177991965** | **App name validation inconsistent with guidelines**  
App name validation now follows the same rules as documented in [Naming restrictions for Apigee artifacts](https://docs.cloud.google.com/apigee/docs/api-platform/reference/naming-guidelines).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **174333251** | **Timeouts experienced when viewing or selecting assets**  
Response times are reduced when viewing assets on the Assets page or selecting an image for an API card on the live portal APIs page.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **173010952** | **Downloaded spec unnecessarily quotes strings**  
Clicking **Download spec** when viewing API documentation on the live portal now delivers, for YAML specs, an exact copy of the original spec (previously it was translated to JSON and back to YAML). Note that this only applies to specs downloaded _after_ this release.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **171236872** | **Stop sending portalDefaultDomain cookie for custom domains**  
Going forward, portals with a custom domain will no longer send the `portalDefaultDomain` cookie to consumers' browsers. For existing portals that already have a custom domain enabled, disable and re-enable the custom domain for this change to take effect.**Note** : Users may continue seeing the cookie if it is cached in their browser.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **165795684** | **Viewing spec in live portal issues multiple`GET` requests**  
An issue has been fixed that would sometimes cause more than one `GET`T call to be issued to the spec endpoint when viewing a spec.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **151961459** | **Portal shows key expiry Never on keys with an expiry and keys that are expired**  
The live portal now shows the appropriate expiration date for API keys.  
  
### February 12, 2021 

On February 12, 2021, we announced the following:

#### Deprecations

This release includes the following deprecations:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-deprecated.svg) |  **The`API Creator` and `Deployer` roles were deprecated**   
The `API Admin` role replaces the deprecated `API Creator` role and the `Environment Admin` role replaces the deprecated `Deployer` role.  
---|---  
  
#### Learn more

  * [Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles)



### February 5, 2021 - API Monitoring

On February 5, 2021, we released an updated version of the API Monitoring software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Recent view**  
The new Recent view displays treemaps of API traffic by proxy. A treemap displays traffic data for each proxy as a rectangle, whose size is proportional to the amount of traffic in the proxy. The colors of the rectangle indicate the relative sizes of the following variables:

  * Number of incidents triggered by [alerts](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications).
  * Error rate
  * Maximum latency 50th percentile (median)

See [Using the Recent view](https://docs.cloud.google.com/apigee/docs/api-monitoring/recent).  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Additional channels for sending alert notifications**  
Apigee API Monitoring now supports the following channels for sending alert notifications:

  * Email
  * PagerDuty
  * Slack
  * Webhooks

See [Creating a notification for an alert](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications#creating_a_notfication_for_an_alert).  
  
### February 4, 2021 - Apigee public cloud offering

On February 4, 2021, we released an updated version of the Apigee public cloud offering software.

#### New features

This release includes the following new features:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Eval orgs**  
Added an [](https://apigee.google.com/setup/eval)Apigee eval provisioning wizard for eval orgs.  
---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Integration with CMEK**  
The new integration with [CMEK (Customer Managed Encryption Keys)](https://docs.cloud.google.com/apigee/docs/api-platform/security/encryption-keys) provides disk and database encryption keys.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **VPC Service Control integration**  
Added integration with [VPC Service Controls](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc) that lets you isolate resources and prevent data leaks/exfiltration.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **NAT IP provisioning**  
Added support for [configuring NAT IP provisioning](https://docs.cloud.google.com/apigee/docs/api-platform/security/nat-provisioning).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Reports**  
Added [anomaly detection reports](https://docs.cloud.google.com/apigee/docs/aapi-ops/anomaly-detect-ui).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **VPC-SC with portals**  
Added support for [granting VPC-SC perimeter access to integrated portals](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc#limitations).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **Operations and HTTP verbs**  
Added support for [operations and HTTP verbs](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **API Monitoring**  
Added support for [API monitoring](https://docs.cloud.google.com/apigee/docs/api-monitoring) to Apigee.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-feature.svg) | **SLA and entitlements**  
Updated [Service Level Agreement](https://docs.cloud.google.com/apigee/sla) and [entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements).  
  
#### Bug Fixes

The Apigee public cloud offering includes bug fixes reported during the Beta and pre-release cycles. Because the fixes were part of releases prior to the GA, they are not listed here. Tracking public bug fixes during releases will start with the next release. 

### February 1, 2021 - Apigee hybrid v1.4.1 (_deprecated_)

On February 1, 2021, we released an updated version of the Apigee hybrid v1.4.1 (_deprecated_) software.

#### Bug Fixes

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **178079779** | **UDCA token generator**  
In Apigee hybrid version 1.4.1 UDCA token generator issue with HTTP / HTTPS forward proxy is fixed, allowing file uploading to function correctly.  
---|---|---  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **177788686** | **TLS / DTLS handshake maximum message size**  
In Apigee hybrid version 1.4.1 the TLS / DTLS handshake maximum message size is enforced at 128 kb (131072 bytes).  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **176903129** | **Quota and SpikeArrest status code**  
For installations on Anthos on premises, Apigee hybrid version 1.4.1 supports the Quota and SpikeArrest policies to return `429` as a default HTTP status code when the limit exceeds the quota.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **175881688** | **MART status code**  
When updating developer app status, MART now gives the correct `statuscode:204` response to indicate success.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **175771199** | **Generic DNS service endpoint**  
In Apigee hybrid version 1.4.1 Cassandra uses a generic DNS service endpoint instead of a node-specific DNS service.  
![](https://docs.cloud.google.com/static/apigee/docs/images/pill-fixed.svg) |  **173963014** | **HttpHeader's allowDuplicates and multiValued transport properties**  
Apigee hybrid version 1.4.1 supports `HttpHeader's` `allowDuplicates` and `multiValued` transport properties. HTTP header fields can now be enabled using `allowDuplicates` and `multiValued` for `HTTPProxyConnection` in the format shown below:  
  
#### Security updates

This release includes the following security updates:

![](https://docs.cloud.google.com/static/apigee/docs/images/pill-security.svg) |  | **fluentd vulnerability**  
Includes a security update for a vulnerability in `fluentd`.  
---|---|---  
      
    
    
    <HTTPProxyConnection>
        <Properties>
           <property name = "HTTPHeader.allowDuplicates" value = "Content-Type,Authorization">
           <property name = "HTTPHeader.multiValued" value = "Content-Type,Authorization">
        </Properties>
    </HTTPProxyConnection>
    
    

####  Upgrading 

The steps to upgrade to Apigee hybrid version 1.4.1 depend on the version you are upgrading from as shown below: 

  * [Upgrading from hybrid v1.3.x to hybrid v1.4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/upgrade)
  * [Upgrading from hybrid v1.2.x to hybrid v1.3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade)
  * [Upgrading from hybrid v1.x to hybrid v1.2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade#upgrading-to-version-1.2.0)



### January 25, 2021 - Apigee hybrid v1.3.5 (_deprecated_)

On January 25, 2021, we released Apigee hybrid runtime version 1.3.5.

## Upgrading

The steps to upgrade to Apigee hybrid version 1.3.5 depend on the version you are upgrading from as shown below:

  * [Upgrading from hybrid v1.2.x to hybrid v1.3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade)
  * [Upgrading from hybrid v1.x to hybrid v1.2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade#upgrading-to-version-1.2.0)



## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users. 

Issue ID  | Description   
---|---  
175771199 |  In Apigee hybrid version 1.3.5 Cassandra uses a generic DNS service endpoint instead of a node-specific DNS service.   
177677157 |  Apigee hybrid version 1.3.5 now allows external secrets in the configuration parameters, in the same pattern as the following example: 
    
    
    cassandra:
      auth:
        secret: cassandra-auth  
  
### January 22, 2021 - UI

On Friday, January 22, we will begin releasing a new version of the UI.

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID  |  Component Name  |  Description   
---|---|---  
169439292  |  Apigee UI  |  **Miscellaneous security fixes**  
  
### January 21, 2021 - Integrated portal

On Thursday, January 21, we will begin releasing a new version of the Apigee integrated portal.

## New features and enhancements

The following sections summarize the new features in this release. 

  * General availability (GA) release of the categories feature
  * Beta release of the developer team and audience management features
  * Relocating and reorganizing of developer programs into user account creation and sign-in experience



### General availability (GA) release of the Categories feature

The GA release of the Categories feature is now available. Categories enable portal users to filter the list of APIs by category, title, or description.

![APIs page](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/apis.png)

For more information, see the following sections:

  * [Viewing API reference documentation](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#view-api-doc)
  * [Tagging an API using categories](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#tag)
  * [Managing categories used to discover related APIs](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#manage-categories)



### Beta release of the developer team and audience management features

The beta release of the developer team and audience management features for integrated portals is now available.

**Note:** No SLAs are provided for the beta release of the developer team and audience management features and after you enroll your organization you cannot revert back. Apigee recommends that you limit your use of these beta features in production environments. Beta Feature | Description | More information  
---|---|---  
Developer teams | Allow portal users to share responsibility for an app with other portal users. | 

  * [Sharing responsibility for an app using developer teams (beta)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#teams) (portal users)
  * [Managing developer teams](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams) (API providers)

  
Audience | Segment individuals in order to control access to content. | [Managing the audiences for your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience#manage-audience)  
  
### Relocating and reorganizing of developer programs into user account creation and sign-in experience

Developer programs have been relocated and reorganized into user account and creation and sign-in experience within their associated portals, as described in the following sections:

  * [Configuring the user account creation and sign-in experience](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in)
  * [Configuring the identity provider](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider)
  * [Managing users](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users)
  * [Managing developer teams (beta)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams)



## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users. 

Issue ID | Component Name | Description  
---|---|---  
177910781 | Integrated Portal |  **Cannot modify developer app with spaces in app name** An issue has been fixed that was preventing an app name containing spaces from being modified.  
177635269 | Integrated Portal |  **Upper-case letters in developer email address causing failure in creating apps** Fixed issue with casing in developer email address that was causing issues with app creation.  
177326265 | Integrated Portal |  **Slow portal response times** Fixed issue that was causing slow portal response times.  
151468563 | Integrated Portal |  **Cached old image is served after new image is loaded** An issue has been fixed that was causing a delay before displaying an updated version of an image.  
  
### January 7, 2021 - Integrated portal

On Thursday, January 7, we will begin releasing a new version of the Apigee integrated portal.

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID  |  Component Name  |  Description   
---|---|---  
174721882  |  Integrated Portal  |  **Unable to link to API category from navigation menu** You can now link to an API category from a navigation menu using its full or relative URL.  
171701845  
170957688  |  Integrated Portal  |  **API requests slow to respond, sometimes return`502`** An issue has been fixed that was causing API requests to be slow to respond.  
171208514  |  Integrated Portal  |  **Improve security of`JSESSIONID` cookie** The `JSESSIONID` cookie, which identifies the browser session to the server, now has the flags `HttpOnly` and `Secure` set to `true`. This increases the portal's security against malicious users.  
171208514  |  Integrated Portal  |  **Update configuration to use`HttpOnly` and `Secure` flags on cookies** The `HttpOnly` and `Secure`flags are set to `true` for the `portalRefresh` and `portalSession` cookies. In addition, the `Secure` flag is set to `true` for the `X-Apigee-CSRF` flag. (To ensure proper function, the `HttpOnly` flag is set to `false`, in this case.)  
170897753  |  Integrated Portal  |  **API details page: Audience display issues** Minor formatting improvements have been implemented in the Audience section on the API details page. Specifically:

  * `Anonymous users (anyone can view)` is selected by default when adding an API
  * Options are listed as a single column of radio buttons

  
169596165  |  Integrated Portal  |  **Developer emails should not be case-sensitive for members of developer teams** Developer emails are no longer case-sensitive for members of developer teams.  
163012424  |  Integrated Portal  |  **Organization administrator not able to view developer account information with error "Visibility of PII is restricted by role"** An issue has been fixed that was preventing organization administrators from viewing developer account information.  
153098491  |  Integrated Portal  |  **Nested menu item with no parent breaks portal** Previously, you could publish a header or footer menu that contained a nested item without a parent, but it would prevent the portal from rendering. Now an error is thrown if you attempt to publish a menu with a nested item that does not have a parent.  
138398421  |  Integrated Portal  |  **Changing a portal page URL breaks any assigned audience permissions** Previously, if a page path was modified, then all its associated permissions were lost and the page was invisible to everyone. Now when a page path is modified the associated permissions are maintained.  
  
## **2020**

### December 17, 2020 - Apigee hybrid v1.4.0

On December 17, 2020, Google released Apigee hybrid runtime version 1.4.0.

## Upgrading

The steps to upgrade to Apigee hybrid version 1.4.0 depend on the version you are upgrading from as shown in the following table: 

Current hybrid version | Upgrade to hybrid version | Instructions  
---|---|---  
1.3.x | 1.4 | [Upgrading Apigee hybrid to version 1.4.0](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/upgrade)  
1.2.x | 1.3 | [Upgrading Apigee hybrid to version 1.3.4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade)  
1.x | 1.2 | [Upgrading to version 1.2.0](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade#upgrading-to-version-1.2.0)  
  
## New features and updates

This section describes the new features and enhancements in this release.

###  Supported versions 

See [Apigee hybrid: supported platforms](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms) for a list of software and platform versions Apigee hybrid supports. 

###  New Features 

**Backup and recovery without Google Cloud**

You can now back up your Cassandra database to a compressed file. See [ Backup and recovery without Google Cloud](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cassandra-backup-non-gcs).

**HTTP methods**

Apigee hybrid v1.4 now supports HTTP methods (also called _Verbs_) for API management.

**Dynamic identifier for MapName in KVM Policy**

A `<MapName>` `mapidentifier` is now available in the [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy). See [ <MapName> element](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy#MapName). 

**Support for JMX and Jolokia user Authentication**

Cassandra now supports JMX and Jolokia usernames and passwords, both explicitly and in TLS secrets. See: 

  * [ About Cassandra user authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cassandra-tls#about-cassandra-user-authentication)
  * [ Multi-region deployment on GKE and GKE on-prem: Set up the new region](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/multi-region#set-up-the-new-region)
  * [ Multi-region deployment on AKS: Set up the new region](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/multi-region-aks#set-up-the-new-region)
  * [ Configuration property reference: cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/config-prop-ref#cassandra)



###  Updates 

**KVM Encryption**

Maps created by the [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy) are encrypted by default. 

**Service accounts added to the`create-service-account` tool**

The `create-service-account` tool can now create the following new standard service accounts:

Service Account | IAM Role | Description  
---|---|---  
`apigee-distributed-trace` | Cloud Trace Agent | Allows the hybrid runtime plane to participate in distributed request tracing in a format compatible with systems like [ Google Cloud Trace](https://docs.cloud.google.com/trace) and [Jaeger](https://www.jaegertracing.io/).  
  
See [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/sa-about)

**JSON Support for AccessEntity Policy**

The AccessEntity policy now has an `<OutputFormat>` element that supports JSON. See [ AccessEntity policy: <OutputFormat> element](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-entity-policy#outputformat-element). 

**DataCapture Policy Runtime Design**

The new [DataCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy) replaces the StatisticsCollector policy to manage collection of runtime statistics. 

**Synchronizer data storage in Cassandra**

Synchronizer now stores environment configuration data in the Cassandra database by default. See [ Synchronizer overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/synchronizer-access#synchronizer-overview). 

**Updates to the Cassandra scale-down procedure**

The Cassandra scale-down procedure has been simplified. The Hybrid runtime decommission the nodes and pvcs after you apply the lower node limits. See [ Scaling down Cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cassandra-scaling#scaling-down-cassandra). 

**New`metrics` configuration properties**

`metrics` now has added properties for: 

  * `metrics.aggregator`
  * `metrics.app`
  * `metrics.proxy`
  * `metrics.stackdriverExporter`



See [ Configuration property reference: metrics](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/config-prop-ref#metrics). 

**Image location**

Apigee hybrid images are downloaded from GCR by default now. Apigee continues to maintain the images in Docker Hub. 

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users. 

Issue ID  | Description   
---|---  
172653617 | When a new proxy revision is deployed there can be an interruption to the API traffic.  
169925206 | Readiness probe failed for no reason, disrupting prod traffic.  
171465538 | Sporadic `599` response code with duration of 1ms.  
174235061 | Missing Apigee metrics in Stackdriver.  
172332786 | Double slashes (`//`) in a request could cause the request not to resolve.  
  
### December 15, 2020 - API Monitoring

On December 15, 2020, Apigee API Monitoring was released for general availability (GA).

## New features and enhancements

This section describes the new features and enhancements for API Monitoring in this release.

### Alerts and notifications

One of the main purposes of API Monitoring is to keep you informed of unusual events or patterns, such as spikes in API traffic or latencies. To track events like these, you can now set up alerts, which are triggered when an event occurs. You can also set up notifications, so that an email will be sent to you when an event occurs. See [Alerts and notifications](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications).

### Investigate view

The new API Monitoring Investigate view displays pivot tables of metrics and attributes for all API traffic, to help you compare activity for different metrics. See [Using the investigate view](https://docs.cloud.google.com/apigee/docs/api-monitoring/investigate).

### December 3, 2020 - Apigee hybrid v1.3.4 (_deprecated_)

On December 3, 2020, we released Apigee hybrid runtime version 1.3.4.

## Upgrading

The steps to upgrade to Apigee hybrid version 1.3.4 depend on the version you are upgrading from as shown below:

  * [Upgrading from hybrid v1.2.x to hybrid v1.3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade)
  * [Upgrading from hybrid v1.x to hybrid v1.2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade#upgrading-to-version-1.2.0)



## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users. 

Issue ID  | Description   
---|---  
165910444  | Apigee hybrid now allows you to provide cert details via a Kubernetes secrets instead of using files.  
168861267  | Apigee Hybrid 1.3.2 cassandra could not restore - GKE - Onprem.  
169437878  | Deployment did not progress beyond "Applying routing changes on".  
169769764  | Fixed the httpProxy issue for Logger in Hybrid 1.2 and 1.3.  
170343982  | Added support for http proxy for Cassandra backup.  
170541982  | Node selector is now overridable.  
171498381  | Default resource limits and requests for the metrics component have been increased.   
171520992  | MP liveness probe timeout setting updated to 6 seconds.  
171656955  | Apigee hybrid now supports up to Kubernetes version1.18.  
172362351  | PropertySet can now be defined at the API Proxy level.  
172873530  | Images and resources are now overridable for containers in the metrics deployment.  
173099048  | Fixed access token error in Synchronizer.  
174166751 |  Cassandra vertical scale-up using nodepools now works with Apigee hybrid version 1.3.4.   
  
### November 16, 2020 - Apigee hybrid v1.2.1 (_deprecated_)

On November 16, 2020, we released Apigee hybrid runtime version 1.2.1.

## Upgrading

To upgrade from version 1.1.1 to 1.2.1, you must make changes in your overrides file that are incompatible with version 1.1.1. Making these changes to your overrides file is a prerequisite to performing the upgrade. The new configuration corrects a problem where in some cases API calls were routed to the wrong environment. For details, see [Upgrading Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade).

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID | Component Name | Description  
---|---|---  
171527564 | Runtime |  Fixed HTTP forward proxy settings in logger.   
170343982 | Runtime |  Added HTTP forward proxy support for Cassandra backup.   
  
### November 11, 2020 - Integrated portal

On Wednesday, November 11, we will begin releasing a new version of the Apigee integrated portal.

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID  |  Component Name  |  Description   
---|---|---  
172819569  |  Integrated Portal  |  **Custom script not run by PageNotFoundComponent** Custom scripts can now be run when a `404: Page Not Found` is returned. For example, to redirect the page results.  
  
### November 10, 2020 - UI

On Tuesday, November 10, we will begin releasing a new version of the Apigee UI.

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID  |  Component Name  |  Description   
---|---|---  
155680847  |  Apigee UI  |  **Miscellaneous security fixes**  
  
### November 4, 2020 - Integrated portal

On Wednesday, November 4, we will begin releasing a new version of the Apigee integrated portal.

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID  |  Component Name  |  Description   
---|---|---  
172238684  |  Integrated Portal  |  **App name character validation affects existing apps** App names for the integrated portal now adhere to the following guidelines, as described in [Naming restrictions for Apigee artifacts](https://docs.cloud.google.com/apigee/docs/api-platform/reference/naming-guidelines): Alphanumeric, space, and the following: _ - . # $ %. Must begin with an alpha character.  
  
### November 1, 2020 - Integrated portal

On Sunday, November 1, we will begin releasing a new version of the Apigee integrated portal.

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID  |  Component Name  |  Description   
---|---|---  
172069545  |  Integrated Portal  |  **Fixed latency issues with APIs page** An issue has been fixed that was causing latency issues when viewing the APIs page on an integrated portal.   
  
### October 29, 2020 - Integrated portal

On Thursday, October 29, we will begin releasing a new version of the Apigee integrated portal.

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID  |  Component Name  |  Description   
---|---|---  
170491758  |  Integrated Portal  |  **Stop populating portalEmail cookie** The `portalEmail` cookie is no longer populated or used by the integrated portal.   
156001807  |  Integrated Portal  |  **Miscellaneous security fixes**  
139039098  |  Integrated Portal  |  **Manual approval of developer app is not visible in the portal** When registering an app, if manual approval of API keys is required, the status is shown as **Pending Approval** until the API key is approved. You can configure automatic or manual approval of API keys when [adding an API product](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products).   
  
### October 19, 2020 - Integrated portal

On Monday, October 19, we will begin releasing a new version of the Apigee integrated portal.

## New features and enhancements

This section describes the new features and enhancements in this release.

### Categories used to organize API catalogs (beta)

The beta release of the API categories feature used to organize API catalogs is now available.

As API catalogs grow, it can make it harder for developers to find the APIs they need. Categories are used to tag APIs to enable developers to discover related APIs on the APIs page of the live portal, For more information, see [Managing categories used to discover related APIs (beta)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#manage-categories).

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID  |  Component Name  |  Description   
---|---|---  
159032053  |  Integrated Portal  |  **Unable to remove callback URL requirement from API Doc** An issue has been fixed that was preventing users from disabling the **Require developers to specify a callback URL** configuration option after enabling it for an API.  
155672474  |  Integrated Portal  |  **Error when unnesting portal menu item** An issue has been fixed that was causing an error to be thrown when unnesting a menu item.  
153097790  |  Integrated Portal  |  **Save and Cancel buttons not showing up in advanced theme editor** The Save and Cancel buttons are now visible in the advanced theme editor.  
151774930  |  Integrated Portal  |  **Responses are sorted in alphabetical order breaking the order specified in spec** Object properties are no longer sorted alphabetically. They now match the order in which they are defined in the spec.   
132246663  |  Integrated Portal  |  **Organization administrator cannot access portal page in SAML-enabled organizations** An issue has been fixed that was preventing organization administrators from accessing portal pages in SAML-enabled organizations.   
159871255,  
156000727  |  Integrated Portal  |  **Miscellaneous security fixes**  
  
### September 24, 2020 - Integrated portal

On Thursday, September 24, we will begin releasing a new version of the Apigee integrated portal.

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID  |  Component Name  |  Description   
---|---|---  
168784520  |  Integrated Portal  |  **Error: Unable to load zone** An issue has been fixed that was preventing a subset of developer programs from being loaded.   
168628869  |  Integrated Portal  |  **APIs page: content misaligned when no categories are present** Minor formatting improvements have been made to API cards to improve alignment when no categories are present.   
168241556  |  Integrated Portal  |  **HTTP 404 status code when saving SMTP settings for v1 portals** An issue has been fixed that was causing an `HTTP 404` status error to be thrown when saving SMTP settings in a v1 portal, even though the settings were saved.   
167380810  |  Integrated Portal  |  **Improve UI error for SMTP email send errors** When test emails fail due to misconfigured custom SMTP settings, the message more clearly describes the error and provides better troubleshooting guidance.   
166328984  |  Integrated Portal  |  **Team page fails to load** An issue has been fixed that was impacting the display of the Teams administration page.   
166828723,  
165526496,  
156464449  |  Integrated Portal  |  **Miscellaneous security fixes**  
  
### September 20, 2020 - Apigee hybrid v1.3.3 (_deprecated_)

On September 20, 2020, we released Apigee hybrid runtime version 1.3.3.

## Upgrading

The steps to upgrade to Apigee hybrid version 1.3.3 depend on the version you are upgrading from as shown below:

  * [Upgrading from hybrid v1.2.x to hybrid v1.3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade)
  * [Upgrading from hybrid v1.x to hybrid v1.2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade#upgrading-to-version-1.2.0)



##  Changes introduced in this release 

The **Target latency** metric was removed from from the `apigee.googleapis.com/Proxy` monitored resource. 

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users. 

Issue ID  | Description   
---|---  
167650106  | Unable to use PUT to insert entries into an encrypted KVM when the environment name contained a hyphen (`-`).  
  
### September 10, 2020 - Integrated portal

On Thursday, September 10, we will begin releasing a new version of the Apigee integrated portal.

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID  |  Component Name  |  Description   
---|---|---  
165823319  |  Integrated Portal  |  **Improve mobile experience for APIs page** The APIs page has been updated to improve the mobile experience.   
165798129  |  Integrated Portal  |  **Formatting on develop team membership page** Formatting issues on the developer team membership page has been fixed.   
163759861,162395593,  
161874934, 157120383,  
156464449,156464049  
|  Integrated Portal  |  **Miscellaneous security fixes**  
162079758  |  Integrated Portal  |  **Highlight matching search text in APIs page** Text that matches the Filter string that is searched is now highlighted on the APIs page.   
163174426  |  Integrated Portal  |  **Convert live portal to flex-based layout** Live portal pages now use a flex-based layout.  **Note** : May break custom styles used to modify the high-level layout.  
163073185  |  Integrated Portal  |  **SmartDocs is not using full height at certain screen widths** Fixed a layout issue with SmartDocs that would occur only at certain screen widths.   
161927743  |  Integrated Portal  |  **Consistent spacing on APIs page** The spacing on the APIs page is now consistent.   
136515141  |  Integrated Portal  |  **Beta tag not visible on integrated portal SAML UI** Fixed an intermittent issue that was causing the beta tag to not be visible in the SAML UI.   
  
### September 9, 2020 - API Monitoring (Beta)

On Wednesday, September 9, we will begin releasing a new version of Apigee.

## New features and enhancements

This section describes the new features and enhancements in this release.

### API Monitoring (beta)

The beta release of Apigee API Monitoring is now available. 

API Monitoring enables you to track your APIs to make sure they are up and running correctly. API Monitoring provides immediate insights into API traffic and performance, to help you quickly diagnose and solve issues as they arise. For more information, see [API Monitoring overview](https://docs.cloud.google.com/apigee/docs/api-monitoring). 

### August 27, 2020 - Apigee hybrid v1.3.2 (_deprecated_)

On August 27, 2020, we released Apigee hybrid runtime version 1.3.2.

## Upgrading

The steps to upgrade to Apigee hybrid version 1.3.3 depend on the version you are upgrading from as shown below:

  * [Upgrading from hybrid v1.2.x to hybrid v1.3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade)
  * [Upgrading from hybrid v1.x to hybrid v1.2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade#upgrading-to-version-1.2.0)



## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users. 

Issue ID  | Description   
---|---  
162759110  | Base paths consisting of only "`/`" would fail. Base paths of "`/`" are now supported.  
2668578  | GKE On Prem - WATCHER would fail to connect to apigee.googleapis.com when HTTP_PROXY is configured.  
143659917  | The PopulateCache policy's expiration setting had to be set to an explicit value between 1 and 30.  
  
### August 24, 2020 - Apigee hybrid v1.3.1 (_deprecated_)

On August 24, 2020, we released Apigee hybrid runtime version 1.3.1.

## Upgrading

The steps to upgrade to Apigee hybrid version 1.3.3 depend on the version you are upgrading from as shown below:

  * [Upgrading from hybrid v1.2.x to hybrid v1.3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade)
  * [Upgrading from hybrid v1.x to hybrid v1.2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade#upgrading-to-version-1.2.0)



## New features and updates

This section describes the new features and enhancements in this release.

### New command line tool, `tools/cas_cleanup.sh`

The `tools/cas_cleanup.sh` tool helps clean up and decommission previous Cassandra instances upon completing the upgrade from hybrid version 1.2.0 to version 1.3.1. See [Upgrading Apigee hybrid to version 1.3.1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade). 

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users. 

Issue ID  | Description   
---|---  
162759110  | Base paths consisting of only "`/`" would fail. Base paths of "`/`" are now supported.  
162772922  | Incorrect deployment of fluentd controller caused wrong configuration input to log agent causing it to error out.  
165198951  | GKE On Prem - Synchronizer failing to connect to apigee.googleapis.com when HTTP_PROXY was configured.  
  
### August 5, 2020 - Integrated portal

On Wednesday, August 5, we will begin releasing a new version of the Apigee integrated portal.

### Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID  |  Component Name  |  Description   
---|---|---  
162383847  |  Integrated Portal  |  **Error when activating/deactivating developer account** An issue has been fixed in the UI that was causing an error similar to the following (which could be ignored) when activating/deactivating a developer account:  
`Unable to update user status`  
161985144  |  Integrated Portal  |  **External spec URLs do not support redirects** When importing an OpenAPI Specification using a URL redirects will not be followed.   
161421338  |  Integrated Portal  |  **Duplicate developer programs created and unable to delete** Developer programs that are not in use by an integrated portal will no longer be displayed.   
161354897  |  Integrated Portal  |  **500 error thrown when creating an integrated portal with existing portal name** When creating an integrated portal with the same name as an existing portal, an appropriate error message is provided.   
159946322  |  Integrated Portal  |  **Delete all artifacts when deleting a developer program** When deleting a developer program, all artifacts that are associated with the developer program are also deleted.   
159925336  |  Integrated Portal  |  **APIs page style changes** The following changes have been implemented on the APIs page:

  * The **Filter by title and description** field now appears above API cards and spans the top of the page allowing for better visibility of API cards on small screens and 4 API cards to fit per row on a fully expanded browser window
  * API cards on the APIs page have been made more responsive using CSS Grid Layout

  
159871255  |  Integrated Portal  |  **Miscellaneous security fixes**  
149834093  |  Integrated Portal  |  **Request header`Content-type: application/json` is getting added to GET request** An issue has been fixed that was causing the `Content-type: application/json` to be added to GET requests.   
148792711  |  Integrated Portal  |  **Read access to developer account information should not be available to all users** Read access to developer account information is now controlled by role, and redacted for users that do not have organization adminstrator or portaladmin roles.   
146486866,  
118358600  |  Integrated Portal  |  **OpenAPI Spec with media type of application/json-patch+json does not render in SmartDocs** and  
**SmartDocs does not support formData parameters** The APIs Explorer widget now allows for text input for more request body MIME types, including JSON mime types ending with "+json", "application/xml", "application/x-www-form-urlencoded". The full list of mime types that support text input can be found here: <https://github.com/codemirror/CodeMirror/blob/master/mode/meta.js#L15-L172>  
  
### July 30, 2020 - Apigee hybrid v1.3.0 (_deprecated_)

On July 30, 2020, we released Apigee hybrid runtime version 1.3.0.

## Upgrading

Upgrade to Apigee hybrid v1.3.0 is not supported at this time.

## New features and updates

This section describes the new features and enhancements in this release.

### New installation prerequisites 

#### cert-manager

Apigee hybrid requires **cert-manager v0.14.2** to manage and verify certificates. You can use `kubectl` to install and configure cert-manager directly from _github > jetstack > cert-manager_. See [Download and install cert-manager](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-download-cert-manager-istio#download-and-install-cert-manager). 

#### Anthos Service Mesh

Apigee hybrid uses the Istio distribution provided with Anthos Service Mesh (ASM) version 1.5.x to create and manage the runtime ingress gateway. See [Download and install ASM](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-download-cert-manager-istio#download-and-install-asm). 

### Environment groups

Environment groups allow you to logically group environments together. Environments within each group share the same hostnames. You can group environments by function, by hostname address, by region if you are implementing a multi-region hybrid installation, or by any other metric you choose. 

Environment groups provide the same routing features provided by the `virtualHosts` property in Apigee hybrid version 1.2. 

See [About environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview). 

### New CLI command

The following new command was added to the apigeectl CLI. For more information about each command, see [apigeectl](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference). 

Command  | Description   
---|---  
`encode` | Returns a list of encoded names of all the ApigeeDeployments for the specified organization or the specified environment within the specified organization.   
  
### CLI flag changes

The following new flags were added to the apigeectl CLI. For more information about each command, see [apigeectl](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference). 

Flag  | Status  | Description   
---|---|---  
`--all-envs` | New  | Applies the apigeectl command to all environments under the organization specified in your overrides config file.   
`--env` | New  | Applies the configuration to the specified environment under the organization specified in your overrides config file.   
`--datastore` | New  | Applies the configuration to the datastore scope (Cassandra).   
`--dry-run` | Changed  | Arguments depend on the version of kubectl you are using: 

  * kubectl version 1.7.x or older: `‑‑dry‑run=true`
  * kubectl version 1.8.x or newer: `‑‑dry‑run=client`

  
`--org` | New  | Applies the configuration to the specified organization.   
`--telemetry` | New  | Applies the configuration for telemetry components: apigee-logger and apigee-metrics.   
`-c, --components` | Removed  | Instead, apply changes by env, org, datastore, or telemetry scopes.   
  
### Unique hashed values for organization and environment names

Apigee hybrid now uses a unique hashed value to keep track of organization and environment names. This avoids errors when org and env names are too long to concatenate. You can see the hashed values with the `apigeectl encode` command. For example: 
    
    
    $ ./apigeectl encode --org hybrid-example
    List of ApigeeDeployments are:
      apigee-connect-agent-hybrid-example-6a82f8a
      apigee-mart-hybrid-example-6a82f8a
      apigee-watcher-hybrid-example-6a82f8a
    
    $ ./apigeectl encode --org hybrid-example --env example-env
    List of ApigeeDeployments are:
      apigee-runtime-hybrid-example-example-env-9e87e2d
      apigee-synchronizer-hybrid-example-example-env-9e87e2d
      apigee-udca-hybrid-example-example-env-9e87e2d
    $

See [apigeectl](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference). 

### New axHashSalt configuration property

A new org-level configuration property, axHashSalt, was added. This property lets you specify the name of a Kubernetes secret that contains a hashing salt value used to encrypt [ obfuscated user data](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/obfuscate-userdata-for-analytics) sent to Apigee analytics. For more information, see the [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/config-prop-ref). 

### Added support for mTLS on the Istio ingress

You can configure [mTLS](https://en.wikipedia.org/wiki/Mutual_authentication). on the Istio ingress. For more information, see [Configuring mTLS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/ingress-tls#configuring-mtls). 

### Watcher 

Apigee Watcher pulls virtual hosts related changes for an org from synchronizer and makes necessary changes to configure istio ingress. 

Watcher introduces: 

  * New service account: apigee-watcher 
  * New role: Apigee Runtime Agent 
  * New configuration property: watcher



See [Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-download-install#create-service-accounts) and the [Configuration properties reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/config-prop-ref#watcher). 

### GA of the OASValidation policy

The OASValidation policy is now GA. 

### GA of the WebSockets feature

The WebSockets feature is now GA. See [Using WebSockets](https://docs.cloud.google.com/apigee/docs/api-platform/develop/websocket-config). 

### Apigee Connect enabled by default

Apigee Connect is now GA and is enabled by default for all new Apigee installs. See [Apigee Connect](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/apigee-connect). 

### Metrics enabled by default

Metrics are enabled by default for all new Apigee hybrid installations. See [Configure metrics collection](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/metrics-enable). 

### Changes to the `virtualHosts` configuration property

Use environment groups to configure routing rules. This replaces the virtualHosts:routingRules property. See [Configuring virtual hosts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/base-path-routing) and See [About environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview). 

### Changes to product limits

The following default limits have been changed: 

Limit  | New value   
---|---  
Message logging payload  | 11 MB   
Target connection timeout  | 600 seconds   
  
## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users. 

Issue ID  | Description   
---|---  
153755536  | An issue was fixed where a long environment and/or organization name caused an error. Org and env names are now truncated to prevent this problem from occurring. A 32 character limit is also now enforced for org and env names.   
155913227  | An issue was fixed where the runtime was unable to connect to the UDCA (fluentd) endpoint even though UDCA is healthy.   
155913227  | Unable to connect to UDCA (fluentd) pod   
153755536  | Error received when environment length is long   
  
### July 19, 2020: Apigee Beta release

### April 3, 2020 - Apigee hybrid v1.2.0 (_deprecated_)

On April 3, 2020, we released Apigee hybrid runtime version 1.2.0.

## Upgrading

To upgrade from version 1.1.1 to 1.2.0, you must make changes in your overrides file that are incompatible with version 1.1.1. Making these changes to your overrides file is a prerequisite to performing the upgrade. The new configuration corrects a problem where in some cases API calls were routed to the wrong environment. For details, see [Upgrading Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade).

## New features and updates

Following are the new features and updates in this release.

### A new virtual host configuration was added to specify routing rules

The new `virtualhosts` configuration feature addresses an issue where the order in which base paths were routed to multiple environments was uncertain. For details, see [ Configure virtual hosts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/base-path-routing). (150336519)

### Beta release of the OASValidation policy

The OASValidation (OpenAPI Specification Validation) policy (Beta) enables you to validate an incoming request or response message against an OpenAPI 3.0 Specification (JSON or YAML). For more information, see [OASValidation policy (Beta)](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oas-validation-policy). (144949685)

###  Beta release of WebSocket support 

Apigee hybrid supports WebSocket connections. API proxy clients can now request a protocol upgrade from HTTP to WebSockets. For details, see [Using WebSockets (Beta)](https://docs.cloud.google.com/apigee/docs/api-platform/develop/websocket-config). 

### Accessing policy secret values from Kubernetes secrets

A new feature lets you access values stored in a Kubernetes secret in proxy flow variables. For details, see [Storing data in a Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/k8s-secrets). (133377603)

### Apigee Operators (AO) element replaces ADAC and ADAH

Apigee Operators (AO) Creates and updates low level Kubernetes and Istio resources that are required to deploy and maintain the AD. For example, the controller carries out the release of message processors. Also validates the ApigeeDeployment configuration before persisting it in Kubernetes cluster. AO replaces Apigee Deployment Admissionhook (ADAH) and Apigee Deployment Controller (ADC). See [ao in the Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-ref#ao). (151250559)

### Replace and deprecate certain cluster and project configuration properties

Two new configuration properties were added: `k8sCluster` and `gcp`. These properties replace the following deprecated properties: `k8sClusterName`, `gcpRegion`, and `gcpProjectID`. For details, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-ref). (146299599)

### Persistent Volume expansion for Cassandra on Kubernetes

A process was added to expand the persistent volume used by apigee-cassandra to accommodate the storage needs, without needing to add more nodes just to increase storage. See [Expand Cassandra persistent volumes](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/expand-persistent-volumes). (138167919)

### Support additional sources for certs, encryption keys and SAs

New configuration properties were added that provide greater flexibility in the way you specify TLS certificates, encryption keys, and service account keys. The new properties are listed below:

  * `kmsEncryptionPath`
  * `kmsEncryptionSecret.key`
  * `kmsEncryptionSecret.name`
  * `cassandra.backup.serviceAccountSecretRef`
  * `cassandra.restore.serviceAccountSecretRef`
  * `envs[].cacheEncryptionPath`
  * `envs[].cacheEncryptionSecret.key`
  * `envs[].cacheEncryptionSecret.name`
  * `envs[].kmsEncryptionPath`
  * `envs[].kmsEncryptionSecret.key`
  * `envs[].kmsEncryptionSecret.name`
  * `envs[].serviceAccountSecretRefs.synchronizer`
  * `envs[].serviceAccountSecretRefs.udca`
  * `envs[].sslSecret`
  * `logger.serviceAccountSecretRef`
  * `mart.serviceAccountSecretRef`
  * `mart.sslSecret`
  * `metrics.serviceAccountSecretRef`
  * `synchronizer.serviceAccountSecretRef`
  * `udca.serviceAccountSecretRef`



For more information, see the [Configuration properties reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-ref). (145303466)

### Allow customers to obfuscate data before sending it to analytics

A feature was added that allows you to obfuscate certain analytics data before it is sent to the management plane. For details, see [ Obfuscate user data for analytics](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/obfuscate-userdata-for-analytics). (142578910)

### Expand persistent volumes for statefulsets

A feature was added that allows you expand the persistent volume used by apigee-cassandra to accommodate the storage needs, without adding more compute power. For more information, see [Expand persistent volumes for statefulsets](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/expand-persistent-volumes). (138167919)

### Minimum supported versions of GKE, Anthos, and AKS are upgraded

Apigee hybrid now supports GKE 1.14.x, Anthos 1.2, and AKS 1.14.x. (149578101)

### Support TLS 1.3 for Northbound connections

Two new configuration properties allow you to set the minimum and maximum TLS version for the ingress: `ingress.minTLSProtocolVersion` and `maxTLSProtocolVersion`. Possible values are 1.0, 1.1, 1.2 and 1.3. For more information, see the [Configuration properties reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-ref). (117580780)

### Support forward proxy configuration for hybrid runtime

HTTP forward proxying is now supported for API proxies deployed to an environment. For details, see [Configure forward proxying](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/forward-proxy). (148970527)

### Support multiple hostAliases per environment

A new configuration property, `envs[].hostAliases`, has been added. This property lets you add multiple host aliases to an environment. Use this element instead of `hostAlias`, which has been deprecated. For details, see [Adding multiple host aliases to an environment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/environment-create#adding-multiple-host-aliases-to-an-environment). (150738495)

### Allow templates for property sets

A new element `<PropertySetRef>` was added to the `<AssignVariable>` element of the `<AssignMessage>` policy. `<PropertySetRef>` allows you to create a property set name/key pair dynamically. This feature is only available for API proxies deployed to Apigee hybrid. See [AssignVariable](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#assignvariable). (148612340)

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users.

Issue ID | Component Name | Description  
---|---|---  
147958049 | Runtime |  A timing issue in runtime startup sequencing was addressed that sometimes prevented the synchronizer from starting up properly.   
149867244 | K8S Platform | apigee-cps-setup pod failing in multi-region setup  
150187652 / 149117839 | Runtime | Could not use hyphens in environment names.  
149220463 | MP pod | Previously deployed proxies needed to be re-deployed.  
144321144 | Runtime | Proxies with secure virtual hosts could not be reloaded.  
147685310 | Runtime | Synchronizer initialization failures due to failed GCP token fetch during initialization.  
151115900 | Runtime | Periodic Internal Probe was not happening for HybridMART resulting in false positive results.  
  
### February 14, 2020 - Apigee hybrid v1.1.1 (_deprecated_)

On February 14, 2020, we released Apigee hybrid runtime version 1.1.1.

**NOTE:** The Apigee APIs, Apigee hybrid UI, GCP integrated services, and integrated portal are in [Beta](https://cloud.google.com/products/#product-launch-stages). All other Apigee hybrid components are GA. 

##  Upgrading 

You cannot upgrade from 1.0.0 to 1.1.1, and the new version is not backward compatible with version 1.0.0. If you are starting with version 1.0.0, version 1.1.1 requires a new installation. 

## New features and updates

Following are the new features and enhancements in this release:

###  Support for GKE on-prem and AKS 

You can now install the hybrid runtime on Anthos GKE deployed on-prem (GKE on-prem) and Microsoft® Azure Kubernetes Service (AKS).

Multi-regional deployments are also supported for GKE on-prem and AKS. 

### Proxy variables for hybrid components

You can now provide configuration parameters for an HTTP forward proxy server. When configured, all internet communication for the UDCA, MART, and Synchronizer components pass through the proxy server. For information about the `httpProxy` configuration property, see [httpProxy properties](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/config-prop-ref#httpProxy). (132167490) 

## Bugs fixed

The following bugs are fixed in this release. This list is primarily for users checking to see if their support tickets have been fixed. It's not designed to provide detailed information for all users. 

Issue ID | Component Name | Description  
---|---|---  
144448262 | K8S Platform |  **Discrepancy in UDCA metric`udca_upstream_http_error_count label`**  
147258525 | CPS |  **Turn partitioned hash index on in hybrid**  
144286363 | Trace |  **An issue was fixed where the Debug mask in`env.json` does not mask response data.**  
147191247 | K8S Platform |  **Contract encryption key should not be part of`apigeectl init`**  
146932903 | K8S Platform |  **Remove unwanted ports from the istio ingress**  
146426226 | K8S Platform |  **Ingress logs are not collected**  
143660032 | RMP |  **com.apigee.test.runtime.steps.quota.DefaultQuotaTypeTest fails in hybrid**  
144973407 | RMP |  **There are currently two correlation IDs for one transaction. We should have only one.**  
144321473 | UAP |  **UDCA: remove no health check warning in logging**  
144321491 | RMP |  **CacheConfiguration.warnMaxEntriesLocalHeap() Log statement indicates a performance issue**  
  
### January 27, 2020 - Apigee hybrid v1.1.0 (_deprecated_)

On January 27, 2020, Google released Apigee hybrid runtime version 1.1.0. This section describes new features and changes released in version 1.1.0.

**NOTE:** The Apigee APIs, Apigee hybrid UI, GCP integrated services, and integrated portal are in [Beta](https://cloud.google.com/products/#product-launch-stages). All other Apigee hybrid components are GA. 

##  Upgrading 

You cannot upgrade from 1.0.0 to 1.1.0, and the new version is not backward compatible with version 1.0.0. Version 1.1.0 requires a new installation. 

##  New features and improvements 

###  Apigee Connect (Alpha release) 

Apigee Connect Alpha allows the Apigee hybrid MART service to connect to the management plane without requiring you to expose the MART endpoint. If you use Apigee Connect, you do not need to configure the MART ingress gateway with a host alias and an authorized DNS certificate. For details, please contact your Apigee representative. 

###  Base path routing 

Base path routing allows you to configure and manage how Apigee hybrid routes API proxy calls to specific environments. For details, see [Configure base path routing](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/base-path-routing). 

##  Changes 

The following changes have been made for hybrid runtime version 1.1.0. Some of these changes, as noted, are **not backward incompatible** with version 1.0.0. 

  * The `apigeectl` CLI now installs Istio in the `istio-system` namespace. This is the default namespace for Istio. This change is **backward incompatible** with hybrid version 1.0.0.
  * The `apigeectl` CLI now installs CertManager into the `cert-manager` namespace. This change is **backward incompatible** with hybrid version 1.0.0.
  * The supported version of Istio deployed with Apigee hybrid runtime has been migrated to 1.4.2 because version 1.2.x is no longer supported.



## Bugs fixed

The following issues listed in the Apigee hybrid 1.0.0 release notes have been fixed:

Issue | Description  
---|---  
144886537 | Base path routing is not working in Apigee hybrid v1.0.0. When the overrides is setup to route to different environments with the same hostAlias, the ingress does not route to the environment based on path.   
143774187 | The hybrid UI displays the label "Company" in the Apps view.  
  
### 

### [ 2019 ]  
  
---  
  
### 

### November 20, 2019 - Apigee hybrid v1.0.0 (_deprecated_)

On November 20, 2019, Google released Apigee hybrid runtime version 1.0.0. This section describes bug fixes with version 1.0.0.

**NOTE:** The Apigee APIs, Apigee hybrid UI, GCP integrated services, and integrated portal are in [Beta](https://cloud.google.com/products/#product-launch-stages). All other Apigee hybrid components are GA.

### Bugs fixed

The following issues listed in the Apigee hybrid Beta 2 release notes have been fixed:

Issue | Description  
---|---  
**133444606** | The update developer apps API does not support all documented input fields.  
**133192879** | There is a very high latency when using the API or UI to get your organization's deployment status. This latency can result in an `HTTP 204 (No Content)` or an `HTTP 400 (Bad Request)` response.  
**131111865** | Synchronizer fails when file system gets too full. This is due to the Kubernetes garbage collection process: it is not triggered until it reaches 85% by default. Closed: Not reproducible.  
  
### Unsupported Apigee features

Google does _not_ plan to support the following features in Apigee hybrid: 

  * APIs to: 
    * Manipulate KVM entries
    * Search for or revoke OAuth access tokens (because tokens are hashed)
  * Developer portal development using Drupal 7
  * OAuth v1 or OAuthv1.0a policy
  * ConcurrentRateLimit policy rate limiting policy
  * Trireme (EOL'd on 10/10/2019)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
