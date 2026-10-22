---
url: https://docs.cloud.google.com/healthcare-api/docs/smart-on-fhir/
title: Connect to applications using SMART on FHIR \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:38.866421+00:00
---

# Connect to applications using SMART on FHIR  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/smart-on-fhir/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Connect to applications using SMART on FHIR Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the [SMART (Substitutable Medical Applications, Reusable Technologies) on FHIR v1.1.0](http://hl7.org/fhir/smart-app-launch/2021May/) standard to access data in FHIR stores in the Cloud Healthcare API.

## Overview

SMART on FHIR is a data standard that enables applications to access information in electronic health record (EHR) systems. An application developer can write a single application that connects to any EHR system that has adopted the standard.

For example, if you have patient data stored in a FHIR store in the Cloud Healthcare API, you can develop an application that does the following:

  1. Authenticates to the FHIR store.
  2. Retrieves the patient's data.
  3. Displays the patient's data in a user interface.



SMART on FHIR supports the OpenID and OAuth 2.0 authorization models for authorization and authentication.

### SMART App Launch Framework, scopes, and launch context

The Cloud Healthcare API supports the SMART App Launch Framework, scopes, and launch context as follows:

SMART App Launch Framework
    

The Cloud Healthcare API supports the [Standalone launch sequence](http://hl7.org/fhir/smart-app-launch/2021May/#standalone-launch-sequence) from the [SMART App Launch Framework](http://hl7.org/fhir/smart-app-launch/2021May/).

An app can launch from within an existing EHR system or Patient Portal session, both of which are called an "EHR launch," or as a standalone app.

Scopes
    

Clinical data scopes define read and write permissions for patient-specific and user-level access. The Cloud Healthcare API supports the following data scopes defined at [Scopes for requesting clinical data](http://hl7.org/fhir/smart-app-launch/2021May/scopes-and-launch-context.html#clinical-scope-syntax):

  * `patient`
  * `user`
  * `system`


Launch context
    

Describes the current patient, encounter, or other context that the request is being made in. The Cloud Healthcare API supports the Patient launch context from [Scopes for requesting context data](http://hl7.org/fhir/smart-app-launch/2021May/scopes-and-launch-context.html#scopes-for-requesting-context-data).

## Configure your authorization server for SMART on FHIR

The Cloud Healthcare API provides built-in support for SMART on FHIR access enforcement based on the input SMART authorization scopes and patient context. FHIR store administrators create and configure an authorization server outside the Cloud Healthcare API that grants SMART authorization scopes and patient context.

If a client application obtains an access token representing the granted SMART authorization scopes and patient context, the Cloud Healthcare API doesn't specify which launch workflow the client application needs to use with the external authorization server.

### Set and validate SMART authorization scopes

If you're using SMARTProxy, you can skip this section. SMARTProxy sets and validates SMART authorization scopes automatically.

SMART authorization scopes use the following format:
    
    
    ( 'patient' | 'user' | 'system') '/' ( resourceType | '*' ) '.' ( 'read' | 'write' | '*' )
    

SMART authorization scopes and patient contexts are passed to the Cloud Healthcare API using `X-Authorization-` HTTP headers. The Cloud Healthcare API uses these headers to enforce access control on data in FHIR stores.

Your authorization server grants the SMART authorization scopes and patient context and encodes them in an access token. The proxy then reads the information in the access token and passes it into the FHIR request headers.

If you don't have an authorization server, you can use the Apigee-based interoperability accelerator [HealthAPIx](https://docs.cloud.google.com/apigee/solutions/healthcare-apix) on [Apigee](https://docs.cloud.google.com/apigee/docs).

Use the following SMART on FHIR HTTP headers when making requests from the proxy. The client application doesn't need to set these headers because they're only passed from the proxy to the Cloud Healthcare API.

  * `X-Authorization-Scope`: One or more authorization scopes that use the [standard SMART authorization scope formats](http://hl7.org/fhir/smart-app-launch/2021May/scopes-and-launch-context.html). For example, setting the authorization scope to `user/Observation.read` means that a request can only read an Observation resource. The Cloud Healthcare API enforces this access control.
  * `X-Authorization-Patient`: The patient context of the request. When you set this header, any resource types in the request that are eligible to be in a patient compartment must belong to the [patient compartment](https://www.hl7.org/fhir/compartmentdefinition-patient.html) of the provided patient ID. The Cloud Healthcare API enforces this access control.
  * `X-Authorization-Subject`: An identifier for the end user accessing the SMART on FHIR client application. The Cloud Healthcare API logs the subject in [Audit logs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/audit-logging).
  * `X-Authorization-Issuer`: The SMART access token issuer. The Cloud Healthcare API logs the issuer in [Audit logs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/audit-logging).



### Configure the authorization server access tokens

To emit a JWT token, you must configure an authorization server. The JWT token contains the SMART authorization scopes and, optionally, the patient context. The Cloud Healthcare API doesn't have specific requirements for how the authorization server mints the SMART JWT token. For example, your application might be registered for a subset of scopes, or the application might present a patient selection widget to set the patient context.

If you don't have an authorization server that configures SMART JWT tokens, you can use the Apigee-based interoperability accelerator [HealthAPIx](https://docs.cloud.google.com/apigee/solutions/healthcare-apix) on [Apigee](https://docs.cloud.google.com/apigee/docs) to set up an authentication server that signs JWT tokens.

### Sample access token

The following sample shows an access token encoded in base64:
    
    
    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJpc3MiOiJzbWFydC50b2tlbi5vcmciLCJpYXQiOjE2MTI4ODQwODUsImV4cCI6MTY0NDQyMDA4NSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoiZG9jdG9yLmpvZUBleGFtcGxlLmNvbSIsInNjb3BlIjoidXNlci9QcmFjdGl0aW9uZXIucmVhZCBwYXRpZW50LyouKiIsInBhdGllbnQiOiJwYXRpZW50MTIzIn0.lC0ouNuXNcj7FxQ83NU_MInULWo0wvyiNuaMt2RbFzBOnnMP_IXJdCeNnw3SQzUV
    

After decoding the access token, it contains the following payload:
    
    
    {
      "iss": "smart.token.org",
      "iat": 1612884085,
      "exp": 1644420085,
      "aud": "www.example.com",
      "sub": "doctor.gabriela@example.com",
      "scope": "user/Practitioner.read patient/*.*",
      "patient": "patient123"
    }
    

## Configure SMART on FHIR in the Cloud Healthcare API

This section describes the steps you need to take to start using SMART on FHIR with data in the Cloud Healthcare API.

### Configure SMARTProxy

If you're using your own authorization server instead of SMARTProxy, skip this section and continue to Configure a Google Cloud service account.

[SMARTProxy](https://github.com/GoogleCloudPlatform/smart-on-fhir) is an open source proxy from Google that provides the following features:

  * Allows the Cloud Healthcare API to accept and validate SMART access tokens.
  * Allows the FHIR implementation in the Cloud Healthcare API to include SMART access tokens as part of the API management and permission model.



When you make a request to retrieve data from the Cloud Healthcare API through SMARTProxy, the request follows these steps:

  1. SMARTProxy accepts a request containing a SMART token from a client.
  2. SMARTProxy validates the SMART token through your JWT authorization server.
  3. SMARTProxy reads the scopes and patient context from the SMART token and passes them to the Cloud Healthcare API using four HTTP headers.
  4. The Cloud Healthcare API receives the headers and validates them to enforce access control on the request. The Cloud Healthcare API then returns a response through SMARTProxy to the client.



### Configure a Google Cloud service account

A proxy can only have one Google Cloud service account. If multiple clients use the same proxy, then the clients must use the same service account. Use caution when sharing a service account with multiple clients for the following reasons:

  * To read the FHIR data in the Cloud Healthcare API, the service account has broad read and write permissions.
  * The Cloud Audit Logs [principal email address](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog#AuthenticationInfo.FIELDS.principal_email) is tied to the service account.

For example, if you call the Cloud Healthcare API using your Google Account for authentication, then Cloud Audit Logs logs your email address as the principal email address. When you use a proxy to call the Cloud Healthcare API, the proxy uses its own service account, and the service account's email address is the principal email address, so the original caller is obscured. To save the end user to the metadata of the audit log, pass in the end user's email address in the `sub` field of the JWT token.




### Configure a FHIR store

You don't need to configure the FHIR store holding the FHIR data you're accessing.

## Make SMART on FHIR requests

This section provides an overview of the supported SMART on FHIR methods in the Cloud Healthcare API and how resource access is enforced when you make a SMART on FHIR request.

When making a request, your authorization server is responsible for generating access tokens with the relevant SMART authorization scope and launch context.

### Supported methods

The Cloud Healthcare API supports SMART on FHIR for all [`projects.locations.datasets.fhirStores.fhir`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir) methods except for the following:

  * [`fhir.ConceptMap-search-translate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/ConceptMap-search-translate)
  * [`fhir.ConceptMap-translate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/ConceptMap-translate)
  * [`fhir.Resource-validate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Resource-validate)



### Resource access enforcement

When making a SMART on FHIR request to a FHIR store, access control occurs in the following order:

  1. The Cloud Healthcare API checks the permissions on the Google Cloud service account configured in the proxy. If the service account has the correct IAM permissions on the FHIR store, the request proceeds.
  2. The Cloud Healthcare API verifies whether the SMART token has the appropriate permissions to access each FHIR resource the request asks for.



The patient compartment is critical to the access enforcement logic in the Cloud Healthcare API. SMART on FHIR has a list of FHIR [resource types](https://www.hl7.org/fhir/compartmentdefinition-patient.html) that are eligible to be included in a patient compartment. The resource types also have their own inclusion criteria. In the rest of this section, the eligible resource types are called "patient compartment-eligible resource types." Ineligible resource types are called "patient compartment-ineligible resource types."

SMART on FHIR requests to a FHIR store must meet the following requirements:

  * Provide the `patient`, `user`, or `system` role in the SMART authorization scopes. If you provide the `patient` role, you must provide a patient context. The patient context is a Patient resource [logical ID](https://www.hl7.org/fhir/resource.html#id). The Patient resource must already exist in the FHIR store or exist after the request is made, otherwise the Cloud Healthcare API rejects the request.

  * When creating, reading, updating, or deleting a resource, the `resourceType` and type of operation (`read` or `write`) must match, otherwise the Cloud Healthcare API rejects the request.

  * If you supply a `patient` scope containing patient compartment-ineligible resource types, such as `patient/Practitioner.*`, the scope validation check fails and the Cloud Healthcare API rejects the scope.

  * You can set all resource types with the `user` scope. If a patient context is present with a `user` scope, patient compartment-eligible resource types are restricted to the patient context. The remaining resource types ignore the patient context.

  * The presence of a patient context restricts the patient compartment-eligible resource types to the given patient. For example, an Observation resource must have the `subject` field reference the given Patient resource for the Observation to be accessible. See the patient compartment access types in [Resource CompartmentDefinition - Content](https://www.hl7.org/fhir/compartmentdefinition.html) for a list of which fields on each patient compartment resource type must be referenced to the given Patient for the resource to be considered inside the patient compartment.

  * Requests can contain both `patient` and `user` scopes.

  * Don't use the `system` scope with the patient context, otherwise the request fails.

  * Don't use the `system` scope with the `patient` scope or the `user` scope.

  * If you call a method that accesses multiple resources (for example, the [`fhir.Patient-everything`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Patient-everything), [`fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle), or [`fhir.search`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/search) method), access control applies to each individual resource.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
