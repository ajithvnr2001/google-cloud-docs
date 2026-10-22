---
url: https://docs.cloud.google.com/healthcare-api/docs/concepts/consent/
title: Consent and privacy overview \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:13.224665+00:00
---

# Consent and privacy overview  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/concepts/consent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Consent and privacy overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Consent Management API and how to use it to manage user consent and privacy.

The Consent Management API is a component of your consent and privacy architecture and provides scalable and secure management of your user's consent and data privacy. The Consent Management API stores the consent information you receive from users, keeps track of what data is permitted for each use case, and helps your application utilize data only as directed by your users.

## Consent Management API information flow

The flow of consent and privacy information within the Consent Management API is as follows:

  1. Your application presents privacy options to a user, then creates or revises a consent record within the Consent Management API to represent that user's decision.
  2. As your application writes data to its various data stores, your application registers the location and characteristics of that data with your Consent Management API instance.
  3. When an application needs to determine whether data is consented for a particular use case, it makes a request to the Consent Management API with the requested data and the proposed use.
  4. The Consent Management API compares the requested data and proposed use to the stored consents and returns a positive response if a valid consent exists. A negative response is returned if a valid consent doesn't exist.



The following diagram shows the Consent Management API information flow:

![consent data flow](https://docs.cloud.google.com/static/healthcare-api/images/consent_architecture.svg)

For more information on how consent data is organized within the Consent Management API, see [Consent Management API data model](https://docs.cloud.google.com/healthcare-api/docs/concepts/consent-model).

## Policy decision point

The Consent Management API acts as the policy decision point within your consent and privacy architecture as follows:

  1. Stores the consent policies granted by your applications' users.
  2. Accepts data access queries made by authorized client applications.
  3. Evaluates access queries against the stored consent policies.
  4. Makes access determinations to enforce consent policies for client applications.



## Policy enforcement

The Consent Management API supports policy enforcement within your consent and privacy architecture as follows:

  1. Processes access determination queries made by applications or policy enforcement points.
  2. Evaluates if a resource can be accessed for a specified purpose.
  3. Determines all the resources that can be accessed for a specified purpose.
  4. Links resources to attributes and consent policies so enforcement points only need to specify request attributes and an optional resource name.
  5. Returns access determinations using the current consent state, even as consents are added, updated, or revoked.



You can implement more than one policy enforcement pattern using the Consent Management API within your consent and privacy architecture. The following list shows examples of policy enforcement patterns:

  * **Enforcement by trusted applications**. Applications that have verified a user's identity and qualifications can forward the relevant properties to the Consent Management API. This allows users to submit or update consents and allows applications, with verified qualifications, to access only the consented information for their use case.
  * **Enforcement by customer middleware**. Applications that require the verification of a user's identity and qualifications can use the Consent Management API to determine whether access is allowed for a given request.
  * **Enforcement by resource servers**. Resource servers can use a user's identity to retrieve qualifications from other applications, if necessary, and then call the Consent Management API to determine access before fulfilling requests.



## Policy representation

Consent policies within the Consent Management API are composed of a set of resource attribute values that define what data that policy applies to and an authorization rule that defines the conditions under which that policy is valid.

When multiple values are specified for a single resource attribute, the policy applies to data matching any of those values. When multiple resource attributes appear in a policy, each of those resource attributes must match for the policy to apply.

Authorization rules use a [constrained variation](https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-creating#creating_a_consent) of the Common Expression Language (CEL) to flexibly describe the relationships between request attributes values that permit access to the relevant data. For more information on CEL, see [Common Expression Language](https://github.com/google/cel-spec/blob/master/doc/intro.md).

Consent resources can contain multiple consent policies that could represent a positive response to consent questions presented to a user. Consent policies could also be used to represent entire consent forms or organizational and administrative decisions.

The following diagram shows how policies are represented in the Consent Management API:

![consent policies](https://docs.cloud.google.com/static/healthcare-api/images/consent_policies.svg)

This diagram shows how to construct simple consent policies using resource and request attributes. More complex policies can be constructed by combining two or more policies.

## Consent records

The Consent Management API stores the following types of consent records:

  * **Consent artifacts** : store the documents that were accepted or signed by the user. These records can contain PDFs or images of the screens shown to the user during the consent process. They can also be used to store signatures, timestamps, and other important information that document the consent process.
  * **Consent resources** : describe the consent that was given by the user in terms of the configured consent attributes. The Consent Management API evaluates these records to determine whether data is consented for a use case. Consent resources contain the granted consent and the consent status. These records can also be linked to the corresponding consent artifacts.



For more information on consent records, see [Creating and updating user consents](https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-creating).

## Data management

The Consent Management API can manage data stored in your own schemas on Google Cloud, on-premises, or with another cloud provider as long as the data can be described using a string. The Consent Management API uses user data mappings to track the managed data without that data needing to be stored within the service itself.

Each user data mapping contains a data ID, a user ID, and a set of resource attribute values. The data ID is a string that uniquely identifies the data represented by the user data mapping. The user ID is an opaque identifier that links that data to a user. The resource attribute values describe the characteristics of the data using a vocabulary defined by the attribute definition resources.

The following are common storage locations for consent-managed data:

  * FHIR stores
  * BigQuery
  * Cloud Storage



For more information on creating user data mappings, see [Registering user data](https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-registering-user-data).

## Access determination

Access determination requests are made by applications that need to know if the proposed use is permitted to access a specific data element, all data elements associated with a user, or whole data stores. The Consent Management API determines if a request is permitted by evaluating whether or not there is a valid consent that grants permission for the specified data and proposed use. The Consent Management API performs this evaluation as follows:

  1. The Consent Management API receives an access determination request with request attribute values for the proposed use and either a target resource or a range of target resources described by user IDs or resource attribute values.
  2. If a range of target resources is specified, the Consent Management API determines the resources that match the range. For example, if you define a range of resource attribute values, all resources within this range are used in the access determination request. 
  3. Consents for all matched resources are identified.
  4. The proposed use is evaluated against the authorization rules of the relevant consents.
  5. If any of the authorization rules permit this combination of request attribute values, a positive access determination is returned for each resource evaluated.



By default, access determination is only made on active consents. Consents in the draft state can be included in the access determination by specifying them directly in the access determination request. Consents that are expired, revoked, or in the rejected state are ignored in all access determination requests.

For more information on making access determination requests, see [Making access determinations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-access-determination).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
