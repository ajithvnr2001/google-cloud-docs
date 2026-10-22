---
url: https://docs.cloud.google.com/healthcare-api/docs/concepts/consent-model/
title: Consent Management API data model \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:29.588032+00:00
---

# Consent Management API data model  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/concepts/consent-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Consent Management API data model Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how information is organized within the Consent Management API and explains how various resource fields can be used.

## Overview

The Consent Management API manages data related to consent and privacy across the following areas:

  * **Configuration information**. Consent store settings and data related to the configuration of your consent store, including expiration time and policy building blocks, such as consent attribute definitions.
  * **Consent records**. Data related to the permissions granted by your users, including consents and any linked consent artifacts.
  * **Managed resources**. User data mappings and data related to the resources being managed by the Consent Management API. User data mappings are stored within the Consent Management API while the managed resources are stored outside the Consent Management API.



## Data model

The Consent Management API uses the following data model:

![consent model](https://docs.cloud.google.com/static/healthcare-api/images/consent_model.svg)

## Configuration information

Consent data is stored in a consent store. You can create one or more consent stores that are configured and operated independently. Your consent store configuration choices determine what other Consent Management API resources you can create and how those resources behave.

Depending on your use case, you might require more than one consent store. You can then organize your consent stores by configuring them with key-value labels.

You can configure a default expiration period that applies to consents created within the store. For example, you could set the store expiration period to one year so that new consents created in the store would expire one year after creation. If a consent is created with its own expiration period, that expiration period is used instead of the store's default expiration period. For more information on consent stores and their configuration, see [Creating and updating user consents](https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-creating).

Creating attribute definitions is another way to configure the behavior of your consent store. Attribute definition resources specify what attributes and attribute values are permitted in the consent store. The collection of attribute definitions in your consent store defines the consent and privacy concepts that your consent store can process.

Each attribute is classified as either a resource attribute or a request attribute. Resource attributes are attributes that describe the data that your consent store manages. Resource attributes are used to create user data mappings, to construct consent policies, and to constrain the scope of access determination requests to specific types of data.

Request attributes are attributes that describe how the data in your consent store can be used. Request attributes are necessary to construct the authorization rules of consent policies and are required to describe the proposed use during access determination requests. For more information on attribute definitions, see [Configuring consent policies using attributes](https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-policies).

## Consent records

You can create consent resources and consent artifact resources when recording a user's consent in the Consent Management API. Consent resources record the specific conditions for which a consent is valid and allow the Consent Management API to fulfill access determination requests. Consent artifact resources record the conditions for which the user granted the consent and provide documentation of the granting of consent.

### Consent resources

Consent resources contain one or more policies that describe the granted consent in terms of the attributes and attribute values configured within the consent store.

Consent resources are specific to a user and a `userID` is specified for each consent resource. The `userID` is an identifier that indicates who the consent belongs to. The same identifier is used when creating user data mappings.

Consent policies use resource attributes to describe what data a consent applies to and authorization rules to define which uses of that data are permitted. Authorization rules are expressed using request attributes and the [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). You can construct policies from any of the attribute values defined in your consent store's attribute definitions.

For more information on policies, see [Policy enforcement](https://docs.cloud.google.com/healthcare-api/docs/concepts/consent#policy_enforcement).

Consent resources can have one of the following states:

  * **Active** : the consent has been granted by the user and will be evaluated during most access determination methods. You can change active consents to revoked if the user needs to revoke the consent.
  * **Revoked** : the consent has been revoked by the user and this resource will be ignored during all access determinations.
  * **Draft** : the consent has not yet been granted by the user but can be evaluated in access determinations, under certain conditions. You can change draft consents to active if the user grants consent. The draft resource can be changeed to rejected if the user declines the consent.
  * **Rejected** : the consent has not been granted and will be ignored during all access determinations.



You can also define an expiration for consents as an absolute date or as a time duration. Consents that do not have an expiration inherit the store's default expiration duration. If the consent store's default expiration is not configured and you do not define a consent's expiration, then that consent will not expire.

### Consent artifacts

Consent artifact resources record the documentation to support the policies described by consent resources. This documentation can include the following:

  * Timestamps
  * Signatures of the user, guardian, or witness
  * Images or screen captures that document the user's consent experience
  * eConsent documentation such as a signed PDF or other evidence of consent
  * Additional metadata, such as names, dates, or contact information



Consent resources are linked to consent artifact resources when the consent resource is created. You can include information that can be used to identify a user within a consent artifact resource. To limit access to this information, you can configure permissions just for consent artifacts. For more information on consent permissions, see [Access control](https://docs.cloud.google.com/healthcare-api/docs/access-control#consent_store_methods).

## Managed resources

The Consent Management API manages access for resources stored in various locations, either on Google Cloud, on-premises, or with another cloud provider. Information about the resources being managed is contained within user data mappings, which allows the Consent Management API to make access determinations without requiring access to the managed resources themselves.

User data mappings use the `dataID` field to uniquely identify the resources being managed. The managed resources can be located anywhere that can be described using a string.

The `userID` field is an identifier that represents the user to which the managed resource is associated. This is the same identifier that is used when creating consent and consent artifact resources.

The set of resource attribute values contained within a user data mapping describes the resource represented by that user data mapping. The permitted resource attribute values are defined by the consent store's attribute definitions.

For more information on creating and managing user data mappings, see [Registering user data](https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-registering-user-data).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
