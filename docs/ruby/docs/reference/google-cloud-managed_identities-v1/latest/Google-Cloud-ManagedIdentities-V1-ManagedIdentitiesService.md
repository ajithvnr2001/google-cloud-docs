---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-managed_identities-v1/latest/Google-Cloud-ManagedIdentities-V1-ManagedIdentitiesService/
title: Managed Service for Microsoft Active Directory API V1 API - Module Google::Cloud::ManagedIdentities::V1::ManagedIdentitiesService (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:23.996689+00:00
---

# Managed Service for Microsoft Active Directory API V1 API - Module Google::Cloud::ManagedIdentities::V1::ManagedIdentitiesService (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-managed_identities-v1/latest/Google-Cloud-ManagedIdentities-V1-ManagedIdentitiesService/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Managed Service for Microsoft Active Directory API V1 API - Module Google::Cloud::ManagedIdentities::V1::ManagedIdentitiesService (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.1  0.4.0  0.3.5 

Reference documentation and code samples for the Managed Service for Microsoft Active Directory API V1 API module Google::Cloud::ManagedIdentities::V1::ManagedIdentitiesService.

API Overview

The `managedidentites.googleapis.com` service implements the Google Cloud Managed Identites API for identity services (e.g. Microsoft Active Directory).

The Managed Identities service provides methods to manage (create/read/update/delete) domains, reset managed identities admin password, add/remove domain controllers in GCP regions and add/remove VPC peering.

Data Model

The Managed Identities service exposes the following resources:

  * Locations as global, named as follows: `projects/{project_id}/locations/global`.

  * Domains, named as follows: `/projects/{project_id}/locations/global/domain/{domain_name}`.




The `{domain_name}` refers to fully qualified domain name in the customer project e.g. mydomain.myorganization.com, with the following restrictions:

  * Must contain only lowercase letters, numbers, periods and hyphens.
  * Must start with a letter.
  * Must contain between 2-64 characters.
  * Must end with a number or a letter.
  * Must not start with period.
  * First segement length (mydomain form example above) shouldn't exceed 15 chars.
  * The last segment cannot be fully numeric.
  * Must be unique within the customer project.



## Example

Load this service and instantiate a gRPC client
    
    
    require "google/cloud/managed_identities/v1/managed_identities_service"
    client = ::Google::Cloud::ManagedIdentities::V1::ManagedIdentitiesService::Client.new

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
