---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-custom-search/
title: Creating custom FHIR searches \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:31.598463+00:00
---

# Creating custom FHIR searches  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-custom-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Creating custom FHIR searches Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**  
  
This page describes Preview features that are subject to change and may have limited support. Changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see [Pre-GA Offering Terms for Cloud Healthcare API](https://cloud.google.com/healthcare-api/docs/pre-ga-terms#pre-ga_offering_terms_for) and the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

This page describes how to configure a FHIR store to support custom search parameters for fields and extensions that are not covered by the FHIR standard search parameters.

Custom search parameters can be useful in many situations, including the following:

  * You need to search for a field in a FHIR resource, but there isn't a supported search parameter for the field.
  * You need to search in extensions added to the FHIR data model.

**Note:** Custom search parameters are not supported on FHIR stores using the DSTU2 version.

## Overview

By default, [searching for FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search) supports the standard search parameters defined in the [FHIR specification](https://www.hl7.org/fhir/search.html#standard), with some exclusions documented in the [FHIR capability statement](https://www.hl7.org/fhir/capabilitystatement.html) or [FHIR conformance statement](https://docs.cloud.google.com/healthcare-api/docs/fhir).

You can create one or more custom search parameters and configure the FHIR store to support them in queries through the `search` method. Custom search parameters are useful in the following situations:

  * To search in fields not covered by standard search parameters.
  * To search in [extensions](https://www.hl7.org/fhir/extensibility.html) to the FHIR data model.



Many [FHIR implementation guides](http://hl7.org/fhir/profiling.html) define search parameters, which you can use in your searches.

Custom search parameters support the same search behavior, including [advanced FHIR search features](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-advanced-search) as standard search parameters, such as the following:

  * modifiers
  * `_include` and `_revinclude`
  * chained search
  * `_sort`



To enable a custom search for your FHIR store, you must first create one or more [`SearchParameter`](https://www.hl7.org/fhir/searchparameter.html) resources that define the search behavior. `SearchParameter` is a standard FHIR resource type that can be created, updated, or deleted using the same methods as any other resource type. See Create a search parameter resource in the store.

`SearchParameter` resources in a FHIR store do not take effect until configured using the [`configureSearch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores/configureSearch) method. This method enables a list of custom search parameters. Each time it is called, it replaces the previous list of parameters. A long-running operation is triggered for `configureSearch` to reindex all relevant resources within the store according to the new search configuration. All new and updated resources after the method call are indexed according to the new configuration. Any index data for custom search parameters that are no longer in the configuration are removed. For more details on how to use [`configureSearch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores/configureSearch), see Enable the custom search parameter for your FHIR store.

The store's [`CapabilityStatement`](https://www.hl7.org/fhir/capabilitystatement.html), retrieved through the [`fhir.capabilities`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/capabilities) method, lists both standard and custom search parameters. Search parameters for a resource are found in the `rest.resource.searchParam` field.

**Note:** If `configureSearch` is called during an ongoing [import from Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export#importing_fhir_resources), the imported resources may be unsearchable using the newly configured custom search parameters.

## Create a custom FHIR search

### Create a SearchParameter resource in the FHIR store

The following samples show how to create a custom search parameter resource using the [`projects.locations.datasets.fhirStores.fhir.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/create) method. You can also use the [`projects.locations.datasets.fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import) method.

For descriptions of the relevant fields of search parameters, see SearchParameter resource fields.

### curl

The following sample shows a `POST` request using `curl`.
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
            \"resourceType\": \"SearchParameter\",
            \"url\": \"CANONICAL_URL\",
            \"base\": [\"RESOURCE_TYPE\"],
            \"code\": \"SEARCH_PARAMETER_CODE\",
            \"name\": \"SEARCH_PARAMETER_NAME\",
            \"type\": \"SEARCH_PARAMETER_TYPE\",
            \"expression\": \"SEARCH_PARAMETER_EXPRESSION\",
            \"status\": \"active\",
            \"description\": \"SEARCH_PARAMETER_DESCRIPTION\"
        }" \
        "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/SearchParameter"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "resourceType": "SearchParameter",
      "url": "CANONICAL_URL",
      "base": ["RESOURCE_TYPE"],
      "code": "SEARCH_PARAMETER_CODE",
      "name": "SEARCH_PARAMETER_NAME",
      "type": "SEARCH_PARAMETER_TYPE",
      "expression": "SEARCH_PARAMETER_EXPRESSION",
      "status": "active",
      "description": "SEARCH_PARAMETER_DESCRIPTION",
      "meta": {
        "lastUpdated": "LAST_UPDATED",
        "versionId": "VERSION_ID"
      },
    }
    
    

### PowerShell

The following sample shows a `POST` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    $SearchParameter = '{
        "resourceType": "SearchParameter",
        "url": "CANONICAL_URL",
        "base": ["RESOURCE_TYPE"],
        "code": "SEARCH_PARAMETER_CODE",
        "name": "SEARCH_PARAMETER_NAME",
        "type": "SEARCH_PARAMETER_TYPE",
        "expression": "SEARCH_PARAMETER_EXPRESSION",
        "status": "active",
        "description": "SEARCH_PARAMETER_DESCRIPTION"
    }'
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $SearchParameter `
      -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/SearchParameter" | ConvertTo-Json

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "resourceType": "SearchParameter",
      "url": "CANONICAL_URL",
      "base": ["RESOURCE_TYPE"],
      "code": "SEARCH_PARAMETER_CODE",
      "name": "SEARCH_PARAMETER_NAME",
      "type": "SEARCH_PARAMETER_TYPE",
      "expression": "SEARCH_PARAMETER_EXPRESSION",
      "status": "active",
      "description": "SEARCH_PARAMETER_DESCRIPTION",
      "meta": {
        "lastUpdated": "LAST_UPDATED",
        "versionId": "VERSION_ID"
      },
    }
    
    

### Enable the custom search parameter for your FHIR store

To enable one or more custom search parameters for your FHIR store, make a `POST` request to the `[store base URL]:configureSearch` method and specify the canonical URL for each search parameter that you are enabling.

Canonical URLs are specified in either of the following formats:

  * `uri`: Selects the largest `version` available in the store for that URI.
  * `uri|version` Selects a specific version.



For example, if the store contains versions `1.0.0` and `1.0.1` for search parameters with the `http://example.com/search` URI, the canonical URL `http://example.com/search|1.0.0` selects the `1.0.0` version. The canonical URL `http://example.com/search` selects the `1.0.1` version.

The list of URLs provided to this method replaces any previous configuration and removes custom search parameters that were previously in effect. The configuration is cached based on the contents of the `SearchParameter` resources that existed at the time `configureSearch` was called. The configuration will not be updated if the `SearchParameter` resources are updated or deleted until `configureSearch` is called again.

When the `[store base URL]:configureSearch` method call is successful, the return value is the name of a long-running operation to reindex the resources in the store according to the new configuration. You can view the status of the long-running operation using the [`operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method, and you can cancel it using the [`operations.cancel`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/cancel) method. The status contains a counter indicating how many resources have been successfully reindexed.

Searches on the store continue to function normally while the long-running operation runs, except that custom search parameters that are added or changed by this operation return partial results. Canceling the operation is safe, but results in the partial indexing of the custom search parameters. It is important to complete an entire successful reindexing operation before searching with newly added or changed parameters.

**Note:** The Cloud Healthcare API will occasionally be reindexed as part of maintenance or feature updates. If you change your configuration but cancel the reindexing operation, background reindexing process will eventually apply your configuration. Ensure that your custom search configuration is always left in the desired state.

If there are errors, they are displayed in Cloud Logging.

The `configureSearch` method can also be used with the option `"validate_only": true` to validate the specified search parameters without modifying the store configuration and without reindexing any data.

The following samples show how to enable one or more custom search parameters for your FHIR store using the [`projects.locations.datasets.fhirStores.configureSearch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores/configureSearch) method.

### curl

The following sample shows a `POST` request using `curl`.
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
            \"canonicalUrls\": [\"CANONICAL_URL1\",\"CANONICAL_URL2\"],
        }" \
        "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:configureSearch"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

If the long-running operation is still running, the server returns a response with the number of FHIR resources pending reindexing in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1beta1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ConfigureSearch",
        "createTime": "CREATE_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "pending": "PENDING_COUNT"
        }
      }
    }
    

When the LRO finishes, the server returns a response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.fhir.FhirService.configureSearch",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty",
      }
    }
    

If the LRO succeeds, the response contains the number of FHIR resources successfully reindexed and a `google.protobuf.Empty` response type.

### PowerShell

The following sample shows a `POST` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    $configureSearch = '{
      "canonical_urls": [
        "CANONICAL_URL1",
        "CANONICAL_URL2"
      ]
    }'
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $configureSearch `
      -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:configureSearch"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

If the long-running operation is still running, the server returns a response with the number of FHIR resources pending reindexing in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1beta1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ConfigureSearch",
        "createTime": "CREATE_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "pending": "PENDING_COUNT"
        }
      }
    }
    

When the LRO finishes, the server returns a response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.fhir.FhirService.configureSearch",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty",
      }
    }
    

If the LRO succeeds, the response contains the number of FHIR resources successfully reindexed and a `google.protobuf.Empty` response type.

### Search for resources with a custom search

You can search using a custom SearchParameter the same way as any other search. Use the `code` value from the search parameter resource as the `key` for the search query. For more information, see [Searching for FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search).

## SearchParameter resource fields

The following section describes the fields of the [SearchParameter](http://hl7.org/fhir/searchparameter.html) resource that are relevant to custom searches. These fields are available in both the STU3 and R4 versions of FHIR.

### `uri` and `version`

The `uri` field, which is required, and the `version` fields, which are optional, define the [canonical url](http://hl7.org/fhir/references.html#canonical) for the SearchParameter resource. The combination of `uri` and `version` must be unique within the FHIR store.

The canonical URL is the URL used in the `configureSearch` call.

### `name`, `description`, and `status`

The `name`, `description`, and `status` fields are required but have no functional effect.

### `base`

The `base` field lists the FHIR resource types to which this search applies.

If there is more than one type, the `expression` field must have a clause for each type. There is no difference between defining one parameter on two types or defining one parameter for each type. Defining one parameter for multiple resource types makes the definitions more compact.

### `code`

The `code` field defines the key to use in a FHIR search query. For example, if `code` is defined as `payment-type` and `base` is defined as `Claim`, a search query using this parameter would be `Claim?payment-type=ABC`.

The `code` field can't have the same value as any other standard or custom search parameter on the same resource type. The standard search parameters can't be redefined or modified using custom search parameters. The `configureSearch` method rejects duplicate search parameters.

The value of the `code` field must meet the following requirements:

  * Must start with a letter
  * Can't be longer than 64 characters
  * Must contain only the following: 
    * Alphanumeric characters
    * Hyphen character `-`
    * Underscore character `_`



The FHIR standard convention for the `code` field is lowercase with dashes.

### `type`

The `type` field defines the search parameter type. The search parameter type determines the semantics of the search conditions as defined in the [FHIR search specification](http://hl7.org/fhir/search.html#ptypes). This value of `type` must be compatible with the data type of the field specified by the `expression` field. If it is not, `configureSearch` rejects the custom search parameter.

The `type` field must be defined as one of the following:

  * `number`
  * `date`
  * `string`
  * `token`
  * `reference`
  * `quantity`
  * `uri`



The `composite` and `special` types are not supported.

### `expression`

The `expression` field defines which fields or extensions the search parameter queries. This field uses a limited set of the syntax and functions of [FHIRPath](https://hl7.org/fhirpath/).

**Note:** Specifying search parameters using XPath in the `xpath` field is not supported and will be ignored.

#### Field syntax

The `expression` field is defined as a path starting with the resource type and followed by one or more fields separated by `.`, for example, `Patient.contact.name.given`. The field structure of FHIR data can be found in the [FHIR resources](http://hl7.org/fhir/resourcelist.html) and [FHIR datatypes](http://hl7.org/fhir/datatypes.html).

#### Multiple clauses

The `expression` field can contain multiple clauses separated by `|`. In this case, the search parameter matches if any of the clauses match the resource. For example, a search parameter with the expression `Patient.name.given | Patient.name.family` matches either of those two fields. Use multiple clauses when more than one resource type is specified in `base`. For example `Patient.name.given | Practitioner.name.given` for a search parameter that applies to both `Patient` and `Practitioner`.

#### `.as([data type])`

Use the function `.as([data type])` when a field has more than one potential data type. For example, the `Observation.value` field can contain many different types, such as `Quantity` and `String`, which work with different search types. You can select these search types with `Observation.value.as(Quantity)`or `Observation.value.as(String)`.

#### Selecting extensions

You can select extensions with the `.extension([canonical url])` function. Because extensions contain a `value` field that can contain any data type, the full path is defined as `.extension([canonical url]).value.as([data type])`. Complex extensions can use multiple `.extension()` components, for example `Patient.extension('http://hl7.org/fhir/StructureDefinition/patient-citizenship').extension('code').value.as(CodeableConcept)`.

You can also use the `.extension.where(url='[canonical url]')` function to select extensions. This is the only context where the `where()` function is allowed.

No other FHIRPath functions are supported.

### `target`

If the `type` field is defined as `reference`, the `target` field must contain one or more FHIR resource types that define which resource types can be the target of this reference search.

For example, if the `Patient.generalPractitioner` field allows references to `Practitioner`, `PractitionerRole`, and `Organization`, a search parameter can specifically match references to `Practitioner`, `PractitionerRole`, or `Organization`. To match all target types of references, include all types in the `target` field.

### `modifier`, `comparator`, `multipleOr`, `multipleAnd`, and `chain`

The `modifier`, `comparator`, `multipleOr`, `multipleAnd`, and `chain` fields are ignored. The options and functionality available with a custom search parameter are the same as those supported by the FHIR store on a standard search parameter of the same type.

## Use search parameters from an implementation guide

If you are implementing search parameters obtained from a FHIR implementation guide, import the `SearchParameter` resources from your implementation guide's JSON file into the FHIR store using either of the following methods:

  * [`projects.locations.datasets.fhirStores.fhir.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/create)
  * [`projects.locations.datasets.fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import)



In some instances, you must convert a published search parameter for the Cloud Healthcare API to support it. If the search parameters are not converted, the `configureSearch` method rejects them. The following constraints apply to search parameters from implementation guides:

  * If the search parameter is identical to parameters in the base FHIR specification, the `configureSearch` method rejects the duplicate search parameters. Omit such duplicates when calling `configureSearch`. For more information, see `code`.

  * If the search parameter only contains an `xpath` expression, convert the expression to an equivalent FHIRPath expression and use it in the `expression` field. For more information, see `expression`.

  * The `composite` and `special` search parameter types are not supported.

  * The alternate type-casting syntax `([field] as [data type])` is not supported. Convert to the supported equivalent `[field].as([data type])`. For more information, see `.as([data type])`.

  * The `[reference field].where(resolve() is [resource type])` convention for constraining the type of a referenced resource is not supported. Remove the `where()` clause and store the referenced resource type in the `SearchParameter.target` field instead. For more information, see `target`.

  * Some implementation guides use expressions for extensions that omit some of the path components required by the Cloud Healthcare API FHIR store. For example, `Patient.extension('url')` must be modified to `Patient.extension('url').value.as([data type])`, and `Patient.extension('url').extension.value` must be modified to `Patient.extension('url').extension('url2').value.as([data type])`.




## Examples

### Use a custom search to search on an extension field

The following steps show an example of searching for text within the `mothersMaidenName` extension in Patient resources.

  1. Create a sample Patient resource:

### curl

The following sample shows how to create a Patient resource by making a `POST` request using `curl`. This Patient resource has the `mothersMaidenName` extension set to `Marca`.
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             --data "{
               \"name\": [
                   {
                       \"use\": \"official\",
                       \"family\": \"Smith\",
                       \"given\": [
                           \"Darcy\"
                       ]
                   }
               ],
               \"gender\": \"female\",
               \"birthDate\": \"1970-01-01\",
               \"resourceType\": \"Patient\",
               \"extension\": [
                   {
                       \"url\": \"http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName\",
                       \"valueString\": \"Marca\"
                   }
               ]
             }" \
             "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient"

If the request is successful, the server returns a response similar to the following sample in JSON format:
         
         {
           "birthDate": "1970-01-01",
           "gender": "female",
           "id": "PATIENT_ID",
           "meta": {
             "lastUpdated": "2020-01-01T00:00:00+00:00",
             "versionId": "VERSION_ID"
           },
           "name": [
             {
               "family": "Smith",
               "given": [
                 "Darcy"
               ],
               "use": "official"
             }
           ],
           "resourceType": "Patient"
           "extension": [
             {
                 "url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
                 "valueString": "Marca"
             }
           ]
         }
         

### PowerShell

The following sample shows how to create a Patient resource by making a `POST` request using Windows PowerShell. This Patient resource has the `mothersMaidenName` extension set to `Marca`.
         
         $cred = gcloud auth application-default print-access-token
         $headers = @{ Authorization = "Bearer $cred" }
         
         $Patient = '{
             "name": [
                 {
                     "use": "official",
                     "family": "Smith",
                     "given": [
                         "Darcy"
                     ]
                 }
             ],
             "gender": "female",
             "birthDate": "1970-01-01",
             "resourceType": "Patient",
             "extension": [
                 {
                     "url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
                     "valueString": "Marca"
                 }
             ]
         }'
         
         Invoke-RestMethod `
           -Method Post `
           -Headers $headers `
           -ContentType: "application/fhir+json; charset=utf-8" `
           -Body $Patient `
           -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient" | ConvertTo-Json

If the request is successful, the server returns a response similar to the following sample in JSON format:
         
         {
           "birthDate": "1970-01-01",
           "gender": "female",
           "id": "PATIENT_ID",
           "meta": {
             "lastUpdated": "2020-01-01T00:00:00+00:00",
             "versionId": "VERSION_ID"
           },
           "name": [
             {
               "family": "Smith",
               "given": [
                 "Darcy"
               ],
               "use": "official"
             }
           ],
           "resourceType": "Patient"
           "extension": [
             {
                 "url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
                 "valueString": "Marca"
             }
           ]
         }
         

  2. Create a custom search parameter resource:

### curl

The following sample shows how to create the custom search parameter resource for the `mothersMaidenName` extension by making a `POST` request using `curl`.
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             --data "{
                 \"resourceType\": \"SearchParameter\",
                 \"url\": \"http://example.com/SearchParameter/patient-mothersMaidenName\",
                 \"base\": [\"Patient\"],
                 \"code\": \"mothers-maiden-name\",
                 \"name\": \"mothers-maiden-name\",
                 \"type\": \"string\",
                 \"expression\": \"Patient.extension('http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName').value.as(String)\",
                 \"status\": \"active\",
                 \"description\": \"search on mother's maiden name\"
           }" \
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/SearchParameter"

If the request is successful, the server returns the response in JSON format:
         
         {   
         
            "resourceType": "SearchParameter",   
         
            "url": "http://example.com/SearchParameter/patient-mothersMaidenName",   
         
            "base": ["Patient"],   
         
            "code": "mothers-maiden-name",   
         
            "name": "mothers-maiden-name",   
         
            "type": "string",   
         
            "expression": "Patient.extension('http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName').value.as(String)",   
         
            "status": "active",   
         
            "description": "search on mother's maiden name",   
         
            "meta": {   
         
             "lastUpdated": "2020-01-01T00:00:00+00:00",   
         
             "versionId": "VERSION_ID"   
         
            },   
         
         }
         
         

### PowerShell

The following shows how to create the custom search parameter resource for the `mothersMaidenName` extension by making a `POST` request using Windows PowerShell. 
         
         $cred = gcloud auth application-default print-access-token
         $headers = @{ Authorization = "Bearer $cred" }
         
         $SearchParameter = '{
             "resourceType": "SearchParameter",
             "url": "http://example.com/SearchParameter/patient-mothersMaidenName",
             "base": ["Patient"],
             "code": "mothers-maiden-name",
             "name": "mothers-maiden-name",
             "type": "string",
             "expression": "Patient.extension(''http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName'').value.as(String)",
             "status": "active",
             "description": "search on mother''s maiden name"
         }'
         
         Invoke-WebRequest `
           -Method Post `
           -Headers $headers `
           -ContentType: "application/json; charset=utf-8" `
           -Body $SearchParameter `
           -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/SearchParameter"

If the request is successful, the server returns the response in JSON format:
         
         {   
         
            "resourceType": "SearchParameter",   
         
            "url": "http://example.com/SearchParameter/patient-mothersMaidenName",   
         
            "base": ["Patient"],   
         
            "code": "mothers-maiden-name",   
         
            "name": "mothers-maiden-name",   
         
            "type": "string",   
         
            "expression": "Patient.extension('http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName').value.as(String)",   
         
            "status": "active",   
         
            "description": "search on mother's maiden name",   
         
            "meta": {   
         
               "lastUpdated": "2020-01-01T00:00:00+00:00",   
         
               "versionId": "VERSION_ID"   
         
            },   
         
         }
         
         

To target a different data type in the `expression` field, use the function `.as([data type])`. For example, to specify the search expression for a boolean value, use `.value.as(Boolean)`. For more information, see `.as([data type])`.
  3. Enable the search parameter:

### curl

To enable the custom search parameter, make a `POST` request and specify the canonical URL for each search parameter that you are enabling.

The following sample shows a `POST` request using `curl`.
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             --data "{
                 \"canonicalUrls\": [\"http://example.com/SearchParameter/patient-mothersMaidenName\"],
             }" \
             "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:configureSearch"

If the request is successful, the server returns the response in JSON format:
         
         {
           "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
         }
         

### PowerShell

To enable the custom search parameter, make a `POST` request and specify the canonical URL for each search parameter that you are enabling.

The following sample shows a `POST` request using Windows PowerShell.
         
         $cred = gcloud auth application-default print-access-token
         $headers = @{ Authorization = "Bearer $cred" }
         
         $configureSearch = '{
           "canonicalUrls": "http://example.com/SearchParameter/patient-mothersMaidenName"
         }' `
         
         Invoke-WebRequest `
           -Method Post `
           -Headers $headers `
           -ContentType: "application/json; charset=utf-8" `
           -Body $configureSearch `
           -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:configureSearch"

If the request is successful, the server returns the response in JSON format:
         
         {
           "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
         }
         

  4. Search using the custom search parameter:

### curl

The following sample shows how to search Patient resources for the string `Marca` in the `mothersMaidenName` extension by making a `GET` request using `curl`.
         
         curl -X GET \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?mothers-maiden-name:exact=Marca"

If the request is successful, the server returns the response as a FHIR `Bundle` in JSON format. The `Bundle.type` is `searchset` and the search results are entries in the `Bundle.entry` array. In this example, the request returns a single Patient resource including the data inside that resource:
         
         {
           "entry": [
             {
               "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID",
               "resource": {
                 "birthDate": "1970-01-01",
                 "gender": "female",
                 "id": "PATIENT_ID",
                 "meta": {
                   "lastUpdated": "LAST_UPDATED",
                   "versionId": "VERSION_ID"
                 },
                 "name": [
                   {
                     "family": "Smith",
                     "given": [
                       "Darcy"
                     ],
                     "use": "official"
                   }
                 ],
                 "resourceType": "Patient"
                 "extension": [
                   {
                       "url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
                       "valueString": "Marca"
                   }
                 ]
               },
               "search": {
                 "mode": "match"
               }
             }
           ],
           "link": [
             {
               "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?family%3Aexact=Smith"
             }
           ],
           "resourceType": "Bundle",
           "total": 1,
           "type": "searchset"
         }
         

### PowerShell

The following sample shows how to search Patient resources for the string `Marca` in the `mothersMaidenName` extension by making a `GET` request using Windows PowerShell. 
         
         $cred = gcloud auth application-default print-access-token
         $headers = @{ Authorization = "Bearer $cred" }
         
         Invoke-RestMethod `
           -Method Get `
           -Headers $headers `
           -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?mothers-maiden-name:exact=Marca" | ConvertTo-Json

If the request is successful, the server returns the response as a FHIR `Bundle` in JSON format. The `Bundle.type` is `searchset` and the search results are entries in the `Bundle.entry` array. In this example, the request returns a single Patient resource including the data inside that resource:
         
         {
           "entry": [
             {
               "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID",
               "resource": {
                 "birthDate": "1970-01-01",
                 "gender": "female",
                 "id": "PATIENT_ID",
                 "meta": {
                   "lastUpdated": "LAST_UPDATED",
                   "versionId": "VERSION_ID"
                 },
                 "name": [
                   {
                     "family": "Smith",
                     "given": [
                       "Darcy"
                     ],
                     "use": "official"
                   }
                 ],
                 "resourceType": "Patient"
                 "extension": [
                   {
                       "url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
                       "valueString": "Marca"
                   }
                 ]
               },
               "search": {
                 "mode": "match"
               }
             }
           ],
           "link": [
             {
               "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?family%3Aexact=Smith"
             }
           ],
           "resourceType": "Bundle",
           "total": 1,
           "type": "searchset"
         }
         




### Use a custom search to search on a 2-level extension field

The following steps show how to search for the code within the `us-core-ethnicity` extension in a Patient resource.

  1. Create a sample Patient resource:

### curl

The following sample shows how to create a Patient resource by making a `POST` request using `curl`. This Patient resource has the `us-core-ethnicity` extension set.
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             --data "{
               \"name\": [
                   {
                       \"use\": \"official\",
                       \"family\": \"Smith\",
                       \"given\": [
                           \"Darcy\"
                       ]
                   }
               ],
               \"gender\": \"female\",
               \"birthDate\": \"1970-01-01\",
               \"resourceType\": \"Patient\",
               \"extension\": [
                   {
                     \"url\": \"http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity\",
                     \"extension\": [
                       {
                         \"url\" : \"ombCategory\",
                         \"valueCoding\" : {
                           \"system\" : \"urn:oid:2.16.840.1.113883.6.238\",
                           \"code\" : \"2028-9\",
                           \"display\" : \"Asian\"
                         }
                       }
                     ]
                   }
               ]
             }" \
             "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient"

If the request is successful, the server returns a response similar to the following sample in JSON format:
         
         {
           "birthDate": "1970-01-01",
           "gender": "female",
           "id": "PATIENT_ID",
           "meta": {
             "lastUpdated": "2020-01-01T00:00:00+00:00",
             "versionId": "VERSION_ID"
           },
           "name": [
             {
               "family": "Smith",
               "given": [
                 "Darcy"
               ],
               "use": "official"
             }
           ],
           "resourceType": "Patient"
           "extension": [
             {
               "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
               "extension": [
                 {
                   "url" : "ombCategory",
                   "valueCoding" : {
                     "system" : "urn:oid:2.16.840.1.113883.6.238",
                     "code" : "2028-9",
                     "display" : "Asian"
                   }
                 }
               ]
             }
           ]
         }
         

### PowerShell

The following sample shows how to create a Patient resource by making a `POST` request using Windows PowerShell. This Patient resource has the `us-core-ethnicity` extension set.
         
         $cred = gcloud auth application-default print-access-token
         $headers = @{ Authorization = "Bearer $cred" }
         
         $Patient = '{
             "name": [
                 {
                     "use": "official",
                     "family": "Smith",
                     "given": [
                         "Darcy"
                     ]
                 }
             ],
             "gender": "female",
             "birthDate": "1970-01-01",
             "resourceType": "Patient",
             "extension": [
               {
                 "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
                 "extension": [
                   {
                     "url" : "ombCategory",
                     "valueCoding" : {
                       "system" : "urn:oid:2.16.840.1.113883.6.238",
                       "code" : "2028-9",
                       "display" : "Asian"
                     }
                   }
                 ]
               }
             ]
         }'
         
         Invoke-RestMethod `
           -Method Post `
           -Headers $headers `
           -ContentType: "application/fhir+json; charset=utf-8" `
           -Body $Patient `
           -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient" | ConvertTo-Json

If the request is successful, the server returns a response similar to the following sample in JSON format:
         
         {
           "birthDate": "1970-01-01",
           "gender": "female",
           "id": "PATIENT_ID",
           "meta": {
             "lastUpdated": "2020-01-01T00:00:00+00:00",
             "versionId": "VERSION_ID"
           },
           "name": [
             {
               "family": "Smith",
               "given": [
                 "Darcy"
               ],
               "use": "official"
             }
           ],
           "resourceType": "Patient"
           "extension": [
             {
               "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
               "extension": [
                 {
                   "url" : "ombCategory",
                   "valueCoding" : {
                     "system" : "urn:oid:2.16.840.1.113883.6.238",
                     "code" : "2028-9",
                     "display" : "Asian"
                   }
                 }
               ]
             }
           ]
         }
         

  2. Create a custom search parameter resource:

### curl

The following sample shows how to create the custom search parameter resource for the `us-core-ethnicity` extension by making a `POST` request using `curl`. 
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             --data "{
                 \"resourceType\": \"SearchParameter\",
                 \"url\": \"http://example.com/SearchParameter/patient-us-core-ethnicity\",
                 \"base\": [\"Patient\"],
                 \"code\": \"ethnicity\",
                 \"name\": \"ethnicity\",
                 \"type\": \"token\",
                 \"expression\": \"Patient.extension('http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity').extension('ombCategory').value.as(Coding)\",
                 \"status\": \"active\",
                 \"description\": \"search on the ombCategory of a patient.\"
           }" \
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/SearchParameter"

If the request is successful, the server returns the response in JSON format:
         
         {
           "resourceType": "SearchParameter",
           "url": "http://example.com/SearchParameter/patient-us-core-ethnicity",
           "base": ["Patient"],
           "code": "ethnicity",
           "name": "ethnicity",
           "type": "token",
           "expression": "Patient.extension('http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity').extension('ombCategory').value.as(Coding)",
           "status": "active",
           "description": "search on the ombCategory of a patient.",
           "meta": {
             "lastUpdated": "2020-01-01T00:00:00+00:00",
             "versionId": "VERSION_ID"
           },
         }
         
         

### PowerShell

The following sample shows how to create the custom search parameter resource for the `mothersMaidenName` extension by making a `POST` request using Windows PowerShell. 
         
         $cred = gcloud auth application-default print-access-token
         $headers = @{ Authorization = "Bearer $cred" }
         
         $SearchParameter = '{
             "resourceType": "SearchParameter",
             "url": "http://example.com/SearchParameter/patient-us-core-ethnicity",
             "base": ["Patient"],
             "code": "ethnicity",
             "name": "ethnicity",
             "type": "token",
             "expression": "Patient.extension(''http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity'').extension(''ombCategory'').value.as(Coding)",
             "status": "active",
             "description": "search on the ombCategory of a patient."
         }'
         
         Invoke-WebRequest `
           -Method Post `
           -Headers $headers `
           -ContentType: "application/json; charset=utf-8" `
           -Body $SearchParameter `
           -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/SearchParameter"

If the request is successful, the server returns the response in JSON format:
         
         {
           "resourceType": "SearchParameter",
           "url": "http://example.com/SearchParameter/patient-us-core-ethnicity",
           "base": ["Patient"],
           "code": "ethnicity",
           "name": "ethnicity",
           "type": "token",
           "expression": "Patient.extension('http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity').extension('ombCategory').value.as(Coding)",
           "status": "active",
           "description": "search on the ombCategory of a patient.",
           "meta": {
             "lastUpdated": "2020-01-01T00:00:00+00:00",
             "versionId": "VERSION_ID"
           },
         }
         
         

  3. Enable the search parameter: 

### curl

To enable the custom search parameter, make a `POST` request and specify the canonical URL for each search parameter that you are enabling.

The following sample shows a `POST` request using `curl`.
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             --data "{
                 \"canonicalUrls\": [\"http://example.com/SearchParameter/patient-us-core-ethnicity\"],
             }" \
             "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:configureSearch"

If the request is successful, the server returns the response in JSON format:
         
         {
           "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
         }
         

### PowerShell

To enable the custom search parameter, make a `POST` request and specify the canonical URL for each search parameter that you are enabling.

The following sample shows a `POST` request using Windows PowerShell.
         
         $cred = gcloud auth application-default print-access-token
         $headers = @{ Authorization = "Bearer $cred" }
         
         $configureSearch = '{
           "canonicalUrls": "http://example.com/SearchParameter/patient-us-core-ethnicity"
         }' `
         
         Invoke-WebRequest `
           -Method Post `
           -Headers $headers `
           -ContentType: "application/json; charset=utf-8" `
           -Body $configureSearch `
           -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:configureSearch"

If the request is successful, the server returns the response in JSON format:
         
         {
           "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
         }
         

  4. Search using the custom search parameter:

### curl

The following sample shows how to search Patient resources for the code `urn:oid:2.16.840.1.113883.6.238|2028-9` in the `us-core-ethnicity` extension by making a `GET` request using `curl`.
         
         curl -X GET \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?ethnicity=urn:oid:2.16.840.1.113883.6.238|2028-9"

If the request is successful, the server returns the response as a FHIR `Bundle` in JSON format. The `Bundle.type` is `searchset` and the search results are entries in the `Bundle.entry` array. In this example, the request returns a single Patient resource including the data inside that resource:
         
         {
           "entry": [
             {
               "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID",
               "resource": {
                 "birthDate": "1970-01-01",
                 "gender": "female",
                 "id": "PATIENT_ID",
                 "meta": {
                   "lastUpdated": "LAST_UPDATED",
                   "versionId": "VERSION_ID"
                 },
                 "name": [
                   {
                     "family": "Smith",
                     "given": [
                       "Darcy"
                     ],
                     "use": "official"
                   }
                 ],
                 "resourceType": "Patient"
                 "extension": [
                   {
                     "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
                     "extension": [
                       {
                         "url" : "ombCategory",
                         "valueCoding" : {
                           "system" : "urn:oid:2.16.840.1.113883.6.238",
                           "code" : "2028-9",
                           "display" : "Asian"
                         }
                       }
                     ]
                   }
                 ]
               },
               "search": {
                 "mode": "match"
               }
             }
           ],
           "link": [
             {
               "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?ethnicity=urn:oid:2.16.840.1.113883.6.238|2028-9"
             }
           ],
           "resourceType": "Bundle",
           "total": 1,
           "type": "searchset"
         }
         

### PowerShell

The following sample shows how to search Patient resources for the code `urn:oid:2.16.840.1.113883.6.238|2028-9` in the `us-core-ethnicity` extension by making a `GET` request using Windows PowerShell. 
         
         $cred = gcloud auth application-default print-access-token
         $headers = @{ Authorization = "Bearer $cred" }
         
         Invoke-RestMethod `
           -Method Get `
           -Headers $headers `
           -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?ethnicity=urn:oid:2.16.840.1.113883.6.238|2028-9 | ConvertTo-Json

If the request is successful, the server returns the response as a FHIR `Bundle` in JSON format. The `Bundle.type` is `searchset` and the search results are entries in the `Bundle.entry` array. In this example, the request returns a single Patient resource including the data inside that resource:
         
         {
           "entry": [
             {
               "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID",
               "resource": {
                 "birthDate": "1970-01-01",
                 "gender": "female",
                 "id": "PATIENT_ID",
                 "meta": {
                   "lastUpdated": "LAST_UPDATED",
                   "versionId": "VERSION_ID"
                 },
                 "name": [
                   {
                     "family": "Smith",
                     "given": [
                       "Darcy"
                     ],
                     "use": "official"
                   }
                 ],
                 "resourceType": "Patient"
                 "extension": [
                   {
                     "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
                     "extension": [
                       {
                         "url" : "ombCategory",
                         "valueCoding" : {
                           "system" : "urn:oid:2.16.840.1.113883.6.238",
                           "code" : "2028-9",
                           "display" : "Asian"
                         }
                       }
                     ]
                   }
                 ]
               },
               "search": {
                 "mode": "match"
               }
             }
           ],
           "link": [
             {
               "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?ethnicity=urn:oid:2.16.840.1.113883.6.238|2028-9"
             }
           ],
           "resourceType": "Bundle",
           "total": 1,
           "type": "searchset"
         }
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
