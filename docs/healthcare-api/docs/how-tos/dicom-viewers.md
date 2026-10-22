---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-viewers/
title: Integrating with a DICOM medical viewer \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:40.431132+00:00
---

# Integrating with a DICOM medical viewer  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-viewers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Integrating with a DICOM medical viewer Stay organized with collections  Save and categorize content based on your preferences. 

This page explains concepts and best practices for integrating a third-party medical imaging viewer with the Cloud Healthcare API. The Cloud Healthcare API is integrated with multiple viewers, including the [Open Health Imaging Foundation (OHIF) viewer](https://docs.ohif.org/deployment/google-cloud-healthcare/) and the [Weasis viewer](https://github.com/GoogleCloudPlatform/weasis-chcapi-extension).

## Before you begin

If you haven't stored any DICOM images to use in your viewer, see [Store DICOM data](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#store-dicom) and [Importing and exporting DICOM data using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export) to get started.

## Authorizing and authenticating requests using OAuth 2.0

Google Cloud APIs support the [OAuth 2.0 protocol](https://developers.google.com/identity/protocols/OAuth2) for both authentication and authorization.

A medical viewer needs to handle authentication and authorization to access DICOM data stored in the Cloud Healthcare API. You can grant these permissions in two ways. Each method has its own costs and benefits:

**Using Google Identity Services OAuth 2.0 flow**

  * End users authenticate themselves through the medical viewer to the Cloud Healthcare API.
  * The medical viewer accesses the Cloud Healthcare API on behalf of the end user.
  * Permissions are managed at the level of the user and the user's actions are logged to [Cloud Audit Logs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/audit-logging) with the user's unique identifier.
  * Using the Google Identity Services flow is more complex than using a service account. For example, your application needs to handle callbacks to store the authorization token, which can add unnecessary complexity to a simple application.



**Using a service account**

  * You configure the medical viewer to use its own method of authorization and access control to determine whether an end user can view a given Cloud Healthcare API resource. Using a service account is helpful if you already have a viewer that performs its own user management and authentication checks.
  * Actions performed in the viewer are logged to [Cloud Audit Logs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/audit-logging), but you cannot see logs at the level of individual end users.
  * Authentication using a service account is simpler than using the Google Identity Services flow. For example, there is no need to prompt a user to log in, and therefore there is no need to store an access token.



### Authorizing using Google Identity Services OAuth 2.0 flow

You can authorize a medical viewer to access DICOM data stored in the Cloud Healthcare API on a user's behalf by using the [Google Identity Services OAuth 2.0 flow](https://developers.google.com/identity/oauth2/web/guides/overview). Depending on your application, there are flows available for the following applications:

  * [Web server applications](https://developers.google.com/identity/protocols/OAuth2WebServer)
  * [Mobile and desktop applications](https://developers.google.com/identity/protocols/OAuth2InstalledApp)
  * [JavaScript web applications](https://developers.google.com/identity/oauth2/web/guides/use-token-model)



The following description for the sign-in flow assumes that the user accessing the viewer has [created a DICOM store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom) and [stored DICOM instances in the store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#store-dicom):

  1. A user opens your medical viewer application. The viewer displays a consent window from Google that shows the name of your application and the Google API services that it is requesting permission to access with the user's authorization credentials. The user can then consent or refuse to grant access to your application.
  2. The user is sent to a Google Identity Services page. If the user grants your application the requested access, then your application gains permission to access the user's data.



Do not store refresh tokens in the viewer. The access tokens granted to the viewer by the user should be short-lived and only exchanged when the tokens expire.

Refresh tokens are also unnecessary for the following reasons:

  * The user is always present when using the viewer.
  * Using refresh tokens requires extra work to store the token securely.

**Note:** When configuring the viewer's scopes, the sign-in request should only need to contain the https://www.googleapis.com/auth/cloud-healthcare scope.

### Authorizing using a service account

You can manage authentication and authorization at the level of the medical viewer, rather than at the level of an end user, by using OAuth 2.0 with a [service account](https://developers.google.com/identity/protocols/OAuth2ServiceAccount).

For instructions on how to use a service account to authenticate a medical viewer to the Cloud Healthcare API, see [Authenticating to the API](https://docs.cloud.google.com/healthcare-api/docs/how-tos/authentication).

### Required roles

For the viewer to function properly, a user must have the following [roles](https://docs.cloud.google.com/healthcare-api/docs/access-control#roles):

  * `roles/healthcare.dicomViewer`: for viewing DICOM resources
  * `roles/healthcare.dicomEditor`: for viewing, editing, and creating DICOM resources



In the sign-in flow, it is expected that the user has already configured these roles, and the viewer does not need to do anything else. When using a service account, the roles must be set in the service account. The viewer should return appropriate `PERMISSION_DENIED` errors to users who do not have the required permissions for accessing their DICOM stores.

## Accessing DICOMweb endpoints

After the user authenticates to the viewer, the viewer can make requests to DICOMweb endpoints. Each DICOM store exposes a single DICOMweb endpoint.

When the user is in the viewer, they must specify which projects and DICOM stores they want to access. The simplest process is to ask the user to provide the IDs for the project, dataset, and DICOM store they want to access. However, providing each individual value might take the user a long time.

As an alternative, you can provide a combination of user input and auto-completion in the viewer. For example, you might have the user enter a project ID, and then the viewer would automatically populate a list of the datasets and DICOM stores within that project. Or, you could provide a single input field that automatically populates the projects, datasets, and DICOM stores that the user has access to. The following API methods might be helpful when setting up either of these alternatives:

  * [`projects.list`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/list): Lists projects that are visible to the user and that satisfy a specified filter.
  * [`projects.locations.list`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations/list): Lists information about the supported locations for the Cloud Healthcare API.
  * [`projects.locations.datasets.list`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/list): Lists the Cloud Healthcare API datasets in a project.
  * [`projects.locations.datasets.dicomStores.list`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/list): Lists the DICOM stores in a dataset.



You might also consider pre-populating a list of a user's resources. However, if a user has hundreds or thousands of DICOM stores or datasets, pre-populating and displaying the list might be infeasible.

## Accessing resources in the viewer using DICOMweb

The Cloud Healthcare API supports the [DICOMweb standard](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb). To let users access their data, the viewer must implement the DICOMweb RESTful HTTP methods instead of the legacy [DIMSE](https://dicom.nema.org/dicom/2013/output/chtml/part07/sect_3.10.html) protocols.

There are two main components to any viewer:

  * The worklist provider
  * The image viewer



You can use the DICOMweb standard with both components.

### Viewing the worklist provider

Typically, the first thing a user sees when they open a viewer is a list of all available studies in each DICOM store. The viewer can retrieve these studies using the [Search Transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.6).

See the Cloud Healthcare API [DICOM conformance statement](https://docs.cloud.google.com/healthcare-api/docs/dicom#search_transaction) for specifics on how the Search Transaction is implemented in the Cloud Healthcare API.

### Viewing instances

After the user is in the worklist provider, they will typically select a study for viewing. To render the study, the viewer must access the study's raw pixel bytes and the DICOM metadata. The viewer can retrieve this information using the [Retrieve Transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.4) set of methods. The Retrieve Transaction methods let you retrieve an entire raw DICOM file or the file's raw pixel data. The Retrieve Transaction methods also support transcoding between different transfer syntaxes.

See the Cloud Healthcare API [DICOM conformance statement](https://docs.cloud.google.com/healthcare-api/docs/dicom#search_transaction) for specifics on how the Search and Retrieve Transaction methods are implemented in the Cloud Healthcare API.

To minimize latency, use `transfer-syntax=*` in the Accept request HTTP header. Doing so avoids transcoding on the server side.

### Maximizing network throughput

Sometimes, such as when rendering a CT scan, a viewer might need to download many instances at once to render the image. For best results, fetch each instance in parallel using a high number of concurrent requests (such as 50 or more). The exact number depends on your application and network bandwidth.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
