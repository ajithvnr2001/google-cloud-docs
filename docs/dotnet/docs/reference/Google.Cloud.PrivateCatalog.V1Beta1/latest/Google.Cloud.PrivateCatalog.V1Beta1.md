---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1
title: Cloud Private Catalog v1beta1 API - Namespace Google.Cloud.PrivateCatalog.V1Beta1 (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:43.671270+00:00
---

# Cloud Private Catalog v1beta1 API - Namespace Google.Cloud.PrivateCatalog.V1Beta1 (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Private Catalog v1beta1 API - Namespace Google.Cloud.PrivateCatalog.V1Beta1 (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/2.0.0-beta05/Google.Cloud.PrivateCatalog.V1Beta1)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/1.0.0-beta02/Google.Cloud.PrivateCatalog.V1Beta1)



## Classes 

### [AssetReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.AssetReference)

Defines the reference of an asset belonging to a product.

### [AssetReference.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.AssetReference.Types)

Container for nested types declared in the AssetReference message type.

### [Catalog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.Catalog)

The readonly representation of a catalog computed with a given resource context.

### [CatalogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.CatalogName)

Resource name for the `Catalog` resource.

### [GcsSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.GcsSource)

Defines how to access Cloud Storage source.

### [GitSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.GitSource)

Defines how to access a Git Source.

### [Inputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.Inputs)

Defines definition of input parameters of asset templates.

### [PrivateCatalog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.PrivateCatalog)

`PrivateCatalog` allows catalog consumers to retrieve `Catalog`, `Product` and `Version` resources under a target resource context.

`Catalog` is computed based on the [Association][]s linked to the target resource and its ancestors. Each association's [google.cloud.privatecatalogproducer.v1beta.Catalog][] is transformed into a `Catalog`. If multiple associations have the same parent [google.cloud.privatecatalogproducer.v1beta.Catalog][], they are de-duplicated into one `Catalog`. Users must have `cloudprivatecatalog.catalogTargets.get` IAM permission on the resource context in order to access catalogs. `Catalog` contains the resource name and a subset of data of the original [google.cloud.privatecatalogproducer.v1beta.Catalog][].

`Product` is child resource of the catalog. A `Product` contains the resource name and a subset of the data of the original [google.cloud.privatecatalogproducer.v1beta.Product][].

`Version` is child resource of the product. A `Version` contains the resource name and a subset of the data of the original [google.cloud.privatecatalogproducer.v1beta.Version][].

### [PrivateCatalog.PrivateCatalogBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.PrivateCatalog.PrivateCatalogBase)

Base class for server-side implementations of PrivateCatalog

### [PrivateCatalog.PrivateCatalogClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.PrivateCatalog.PrivateCatalogClient)

Client for PrivateCatalog

### [PrivateCatalogClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.PrivateCatalogClient)

PrivateCatalog client wrapper, for convenient use.

### [PrivateCatalogClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.PrivateCatalogClientBuilder)

Builder class for [PrivateCatalogClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.PrivateCatalogClient) to provide simple configuration of credentials, endpoint etc.

### [PrivateCatalogClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.PrivateCatalogClientImpl)

PrivateCatalog client wrapper implementation, for convenient use.

### [PrivateCatalogSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.PrivateCatalogSettings)

Settings for [PrivateCatalogClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.PrivateCatalogClient) instances.

### [Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.Product)

The readonly representation of a product computed with a given resource context.

### [ProductName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.ProductName)

Resource name for the `Product` resource.

### [SearchCatalogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchCatalogsRequest)

Request message for [PrivateCatalog.SearchCatalogs][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchCatalogs].

### [SearchCatalogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchCatalogsResponse)

Response message for [PrivateCatalog.SearchCatalogs][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchCatalogs].

### [SearchProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchProductsRequest)

Request message for [PrivateCatalog.SearchProducts][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchProducts].

### [SearchProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchProductsResponse)

Response message for [PrivateCatalog.SearchProducts][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchProducts].

### [SearchVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchVersionsRequest)

Request message for [PrivateCatalog.SearchVersions][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchVersions].

### [SearchVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchVersionsResponse)

Response message for [PrivateCatalog.SearchVersions][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchVersions].

### [Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.Version)

The consumer representation of a version which is a child resource under a `Product` with asset data.

### [VersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.VersionName)

Resource name for the `Version` resource.

## Enums 

### [AssetReference.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.AssetReference.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [AssetReference.Types.AssetValidationState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.AssetReference.Types.AssetValidationState)

Possible validation steates of an asset reference.

### [CatalogName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.CatalogName.ResourceNameType)

The possible contents of [CatalogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.CatalogName).

### [GitSource.RefOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.GitSource.RefOneofCase)

Enum of possible cases for the "ref" oneof.

### [ProductName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.ProductName.ResourceNameType)

The possible contents of [ProductName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.ProductName).

### [VersionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.VersionName.ResourceNameType)

The possible contents of [VersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.VersionName).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
