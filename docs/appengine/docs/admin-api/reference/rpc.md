---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/
title: App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:55:26.276594+00:00
---

# App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  App Engine Admin API Stay organized with collections  Save and categorize content based on your preferences. 

Provisions and manages developers' App Engine applications.

## Service: appengine.googleapis.com

The Service name `appengine.googleapis.com` is needed to create RPC client stubs.

## `[google.appengine.v1.Applications](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Applications)`

Methods  
---  
``[CreateApplication](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Applications.CreateApplication)`` |  Creates an App Engine application for a Google Cloud Platform project.  
``[GetApplication](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Applications.GetApplication)`` |  Gets information about an application.  
``[RepairApplication](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Applications.RepairApplication)`` |  Recreates the required App Engine features for the specified App Engine application, for example a Cloud Storage bucket or App Engine service account.  
``[UpdateApplication](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Applications.UpdateApplication)`` |  Updates the specified Application resource.  
  
## `[google.appengine.v1.AuthorizedCertificates](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificates)`

Methods  
---  
``[CreateAuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificates.CreateAuthorizedCertificate)`` |  Uploads the specified SSL certificate.  
``[DeleteAuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificates.DeleteAuthorizedCertificate)`` |  Deletes the specified SSL certificate.  
``[GetAuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificates.GetAuthorizedCertificate)`` |  Gets the specified SSL certificate.  
``[ListAuthorizedCertificates](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificates.ListAuthorizedCertificates)`` |  Lists all SSL certificates the user is authorized to administer.  
``[UpdateAuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificates.UpdateAuthorizedCertificate)`` |  Updates the specified SSL certificate.  
  
## `[google.appengine.v1.AuthorizedDomains](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedDomains)`

Methods  
---  
``[ListAuthorizedDomains](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedDomains.ListAuthorizedDomains)`` |  Lists all domains the user is authorized to administer.  
  
## `[google.appengine.v1.DomainMappings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainMappings)`

Methods  
---  
``[CreateDomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainMappings.CreateDomainMapping)`` |  Maps a domain to an application.  
``[DeleteDomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainMappings.DeleteDomainMapping)`` |  Deletes the specified domain mapping.  
``[GetDomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainMappings.GetDomainMapping)`` |  Gets the specified domain mapping.  
``[ListDomainMappings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainMappings.ListDomainMappings)`` |  Lists the domain mappings on an application.  
``[UpdateDomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainMappings.UpdateDomainMapping)`` |  Updates the specified domain mapping.  
  
## `[google.appengine.v1.Firewall](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Firewall)`

Methods  
---  
``[BatchUpdateIngressRules](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Firewall.BatchUpdateIngressRules)`` |  Replaces the entire firewall ruleset in one bulk operation.  
``[CreateIngressRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Firewall.CreateIngressRule)`` |  Creates a firewall rule for the application.  
``[DeleteIngressRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Firewall.DeleteIngressRule)`` |  Deletes the specified firewall rule.  
``[GetIngressRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Firewall.GetIngressRule)`` |  Gets the specified firewall rule.  
``[ListIngressRules](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Firewall.ListIngressRules)`` |  Lists the firewall rules of an application.  
``[UpdateIngressRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Firewall.UpdateIngressRule)`` |  Updates the specified firewall rule.  
  
## `[google.appengine.v1.Instances](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instances)`

Methods  
---  
``[DebugInstance](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instances.DebugInstance)`` |  Enables debugging on a VM instance.  
``[DeleteInstance](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instances.DeleteInstance)`` |  Stops a running instance.  
``[GetInstance](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instances.GetInstance)`` |  Gets instance information.  
``[ListInstances](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instances.ListInstances)`` |  Lists the instances of a version.  
  
## `[google.appengine.v1.Services](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Services)`

Methods  
---  
``[DeleteService](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Services.DeleteService)`` |  Deletes the specified service and all enclosed versions.  
``[GetService](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Services.GetService)`` |  Gets the current configuration of the specified service.  
``[ListServices](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Services.ListServices)`` |  Lists all the services in the application.  
``[UpdateService](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Services.UpdateService)`` |  Updates the configuration of the specified service.  
  
## `[google.appengine.v1.Versions](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Versions)`

Methods  
---  
``[CreateVersion](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Versions.CreateVersion)`` |  Deploys code and resource files to a new version.  
``[DeleteVersion](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Versions.DeleteVersion)`` |  Deletes an existing Version resource.  
``[GetVersion](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Versions.GetVersion)`` |  Gets the specified Version resource.  
``[ListVersions](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Versions.ListVersions)`` |  Lists the versions of a service.  
``[UpdateVersion](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Versions.UpdateVersion)`` |  Updates the specified Version resource.  
  
## `[google.appengine.v1beta.Applications](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Applications)`

Methods  
---  
``[CreateApplication](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Applications.CreateApplication)`` |  Creates an App Engine application for a Google Cloud Platform project.  
``[GetApplication](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Applications.GetApplication)`` |  Gets information about an application.  
``[RepairApplication](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Applications.RepairApplication)`` |  Recreates the required App Engine features for the specified App Engine application, for example a Cloud Storage bucket or App Engine service account.  
``[UpdateApplication](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Applications.UpdateApplication)`` |  Updates the specified Application resource.  
  
## `[google.appengine.v1beta.AuthorizedCertificates](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.AuthorizedCertificates)`

Methods  
---  
``[CreateAuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.AuthorizedCertificates.CreateAuthorizedCertificate)`` |  Uploads the specified SSL certificate.  
``[DeleteAuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.AuthorizedCertificates.DeleteAuthorizedCertificate)`` |  Deletes the specified SSL certificate.  
``[GetAuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.AuthorizedCertificates.GetAuthorizedCertificate)`` |  Gets the specified SSL certificate.  
``[ListAuthorizedCertificates](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.AuthorizedCertificates.ListAuthorizedCertificates)`` |  Lists all SSL certificates the user is authorized to administer.  
``[UpdateAuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.AuthorizedCertificates.UpdateAuthorizedCertificate)`` |  Updates the specified SSL certificate.  
  
## `[google.appengine.v1beta.AuthorizedDomains](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.AuthorizedDomains)`

Methods  
---  
``[ListAuthorizedDomains](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.AuthorizedDomains.ListAuthorizedDomains)`` |  Lists all domains the user is authorized to administer.  
  
## `[google.appengine.v1beta.DomainMappings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.DomainMappings)`

Methods  
---  
``[CreateDomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.DomainMappings.CreateDomainMapping)`` |  Maps a domain to an application.  
``[DeleteDomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.DomainMappings.DeleteDomainMapping)`` |  Deletes the specified domain mapping.  
``[GetDomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.DomainMappings.GetDomainMapping)`` |  Gets the specified domain mapping.  
``[ListDomainMappings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.DomainMappings.ListDomainMappings)`` |  Lists the domain mappings on an application.  
``[UpdateDomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.DomainMappings.UpdateDomainMapping)`` |  Updates the specified domain mapping.  
  
## `[google.appengine.v1beta.Firewall](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Firewall)`

Methods  
---  
``[BatchUpdateIngressRules](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Firewall.BatchUpdateIngressRules)`` |  Replaces the entire firewall ruleset in one bulk operation.  
``[CreateIngressRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Firewall.CreateIngressRule)`` |  Creates a firewall rule for the application.  
``[DeleteIngressRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Firewall.DeleteIngressRule)`` |  Deletes the specified firewall rule.  
``[GetIngressRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Firewall.GetIngressRule)`` |  Gets the specified firewall rule.  
``[ListIngressRules](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Firewall.ListIngressRules)`` |  Lists the firewall rules of an application.  
``[UpdateIngressRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Firewall.UpdateIngressRule)`` |  Updates the specified firewall rule.  
  
## `[google.appengine.v1beta.Instances](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Instances)`

Methods  
---  
``[DebugInstance](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Instances.DebugInstance)`` |  Enables debugging on a VM instance.  
``[DeleteInstance](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Instances.DeleteInstance)`` |  Stops a running instance.  
``[GetInstance](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Instances.GetInstance)`` |  Gets instance information.  
``[ListInstances](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Instances.ListInstances)`` |  Lists the instances of a version.  
  
## `[google.appengine.v1beta.Services](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Services)`

Methods  
---  
``[DeleteService](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Services.DeleteService)`` |  Deletes the specified service and all enclosed versions.  
``[GetService](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Services.GetService)`` |  Gets the current configuration of the specified service.  
``[ListServices](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Services.ListServices)`` |  Lists all the services in the application.  
``[UpdateService](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Services.UpdateService)`` |  Updates the configuration of the specified service.  
  
## `[google.appengine.v1beta.Versions](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Versions)`

Methods  
---  
``[CreateVersion](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Versions.CreateVersion)`` |  Deploys code and resource files to a new version.  
``[DeleteVersion](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Versions.DeleteVersion)`` |  Deletes an existing Version resource.  
``[GetVersion](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Versions.GetVersion)`` |  Gets the specified Version resource.  
``[ListVersions](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Versions.ListVersions)`` |  Lists the versions of a service.  
``[UpdateVersion](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1beta#google.appengine.v1beta.Versions.UpdateVersion)`` |  Updates the specified Version resource.  
  
## `[google.cloud.location.Locations](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.cloud.location#google.cloud.location.Locations)`

Methods  
---  
``[GetLocation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.cloud.location#google.cloud.location.Locations.GetLocation)`` |  Gets information about a location.  
``[ListLocations](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.cloud.location#google.cloud.location.Locations.ListLocations)`` |  Lists information about the supported locations for this service.  
  
## `[google.longrunning.Operations](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operations)`

Methods  
---  
``[GetOperation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`` |  Gets the latest state of a long-running operation.  
``[ListOperations](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`` |  Lists operations that match the specified filter in the request.  
``[WaitOperation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operations.WaitOperation)`` |  Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
