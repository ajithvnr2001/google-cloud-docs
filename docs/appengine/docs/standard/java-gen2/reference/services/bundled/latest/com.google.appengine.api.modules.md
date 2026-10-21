---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules
title: Package com.google.appengine.api.modules (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:17:03.451261+00:00
---

# Package com.google.appengine.api.modules (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.modules (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Utility functions for working with App Engine services (previously known as modules).

A common pattern of usage is:

// Get a handle of the ModulesService. ModulesService modules = ModulesServiceFactory.getModulesService();

// Lookup the versions associated with the current service/module. for (String version : modules.getVersions(modules.getCurrentModule())) { // Process version. }

See Also: [com.google.appengine.api.modules.ModulesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService)

## Classes 

### [IModulesServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.IModulesServiceFactoryProvider)

Google App Engine's [FactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.FactoryProvider) for [IModulesServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.IModulesServiceFactory).

### [ModulesServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServiceFactory)

Factory by which users get an implementation of the [ModulesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService). See Also: [ModulesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService)

### [ModulesServicePb](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb)

### [ModulesServicePb.GetDefaultVersionRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetDefaultVersionRequest)

### [ModulesServicePb.GetDefaultVersionRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetDefaultVersionRequest.Builder)

### [ModulesServicePb.GetDefaultVersionResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetDefaultVersionResponse)

### [ModulesServicePb.GetDefaultVersionResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetDefaultVersionResponse.Builder)

### [ModulesServicePb.GetHostnameRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetHostnameRequest)

### [ModulesServicePb.GetHostnameRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetHostnameRequest.Builder)

### [ModulesServicePb.GetHostnameResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetHostnameResponse)

### [ModulesServicePb.GetHostnameResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetHostnameResponse.Builder)

### [ModulesServicePb.GetModulesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetModulesRequest)

### [ModulesServicePb.GetModulesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetModulesRequest.Builder)

### [ModulesServicePb.GetModulesResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetModulesResponse)

### [ModulesServicePb.GetModulesResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetModulesResponse.Builder)

### [ModulesServicePb.GetNumInstancesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetNumInstancesRequest)

### [ModulesServicePb.GetNumInstancesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetNumInstancesRequest.Builder)

### [ModulesServicePb.GetNumInstancesResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetNumInstancesResponse)

### [ModulesServicePb.GetNumInstancesResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetNumInstancesResponse.Builder)

### [ModulesServicePb.GetVersionsRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetVersionsRequest)

### [ModulesServicePb.GetVersionsRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetVersionsRequest.Builder)

### [ModulesServicePb.GetVersionsResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetVersionsResponse)

### [ModulesServicePb.GetVersionsResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetVersionsResponse.Builder)

### [ModulesServicePb.ModulesServiceError](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.ModulesServiceError)

### [ModulesServicePb.ModulesServiceError.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.ModulesServiceError.Builder)

### [ModulesServicePb.SetNumInstancesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.SetNumInstancesRequest)

### [ModulesServicePb.SetNumInstancesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.SetNumInstancesRequest.Builder)

### [ModulesServicePb.SetNumInstancesResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.SetNumInstancesResponse)

### [ModulesServicePb.SetNumInstancesResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.SetNumInstancesResponse.Builder)

### [ModulesServicePb.StartModuleRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.StartModuleRequest)

### [ModulesServicePb.StartModuleRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.StartModuleRequest.Builder)

### [ModulesServicePb.StartModuleResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.StartModuleResponse)

### [ModulesServicePb.StartModuleResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.StartModuleResponse.Builder)

### [ModulesServicePb.StopModuleRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.StopModuleRequest)

### [ModulesServicePb.StopModuleRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.StopModuleRequest.Builder)

### [ModulesServicePb.StopModuleResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.StopModuleResponse)

### [ModulesServicePb.StopModuleResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.StopModuleResponse.Builder)

## Interfaces 

### [IModulesServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.IModulesServiceFactory)

Factory interface for use by providers of [ModulesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService) for registration with [com.google.appengine.spi.ServiceFactoryFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceFactoryFactory).

### [ModulesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService)

ModulesService allows the application to fetch information about its own module and version information. Additionally, the service has the ability to start, stop and change the number of instances associated with a module version.

### [ModulesServicePb.GetDefaultVersionRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetDefaultVersionRequestOrBuilder)

### [ModulesServicePb.GetDefaultVersionResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetDefaultVersionResponseOrBuilder)

### [ModulesServicePb.GetHostnameRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetHostnameRequestOrBuilder)

### [ModulesServicePb.GetHostnameResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetHostnameResponseOrBuilder)

### [ModulesServicePb.GetModulesRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetModulesRequestOrBuilder)

### [ModulesServicePb.GetModulesResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetModulesResponseOrBuilder)

### [ModulesServicePb.GetNumInstancesRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetNumInstancesRequestOrBuilder)

### [ModulesServicePb.GetNumInstancesResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetNumInstancesResponseOrBuilder)

### [ModulesServicePb.GetVersionsRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetVersionsRequestOrBuilder)

### [ModulesServicePb.GetVersionsResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.GetVersionsResponseOrBuilder)

### [ModulesServicePb.ModulesServiceErrorOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.ModulesServiceErrorOrBuilder)

### [ModulesServicePb.SetNumInstancesRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.SetNumInstancesRequestOrBuilder)

### [ModulesServicePb.SetNumInstancesResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.SetNumInstancesResponseOrBuilder)

### [ModulesServicePb.StartModuleRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.StartModuleRequestOrBuilder)

### [ModulesServicePb.StartModuleResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.StartModuleResponseOrBuilder)

### [ModulesServicePb.StopModuleRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.StopModuleRequestOrBuilder)

### [ModulesServicePb.StopModuleResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.StopModuleResponseOrBuilder)

## Enums 

### [ModulesServicePb.ModulesServiceError.ErrorCode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesServicePb.ModulesServiceError.ErrorCode)

## Exceptions 

### [ModulesException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesException)

Exception thrown by the [ModulesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.modules.ModulesService).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
