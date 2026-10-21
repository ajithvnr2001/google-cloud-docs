---
url: https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create/
title: Create a bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:06.249532+00:00
---

# Create a bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Create a bucket Stay organized with collections  Save and categorize content based on your preferences. 

To create a bucket, you make a `PUT` request that includes an `x-goog-project-id` header, and you include bucket settings such as the bucket's location and default storage class in the request body. Note that certain settings, such as a bucket's location, can only be set at creation time. Additionally, the XML API does not support all settings at bucket creation time, such as a bucket's Object Lifecycle Management configuration. Such settings can only be specified in a [metadata update request](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata) after bucket creation.

Your bucket name must be unique across the global Cloud Storage namespace. If your bucket name is in use, you get a [409 Conflict](https://docs.cloud.google.com/storage/docs/xml-api/reference-status#409%E2%80%94conflict) error, and the bucket creation request fails. Similarly, requests that attempt to create a bucket with an invalid name fail. For more information, see [bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming).

You can only create a bucket in projects for which you have [permission](https://docs.cloud.google.com/storage/docs/iam) to do so. For example, if you have the **Storage Admin** role on a project, you have the required permission (`storage.buckets.create`) to create buckets.

## Query string parameters

This request does not typically include query string parameters.

See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

In addition to [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket#request-headers), the following can be used.

Header | Description | Required  
---|---|---  
`[x-goog-acl](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogacl)` | The predefined access control list (ACL) that you want to apply to the bucket. Do not use if you are using the `acl` query string parameter to apply ACLs. | No  
`[x-goog-bucket-object-lock-enabled](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogbucketobjectlockenabled)` | The boolean determining if [object retention](https://docs.cloud.google.com/storage/docs/object-lock) is enabled for the bucket. | No  
`[x-goog-bucket-retention-period](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogbucketretentionperiod)` | The time, in seconds, that objects in the bucket must be retained before they can be replaced or deleted. | No  
`[x-goog-project-id](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogprojectid)` | The project ID of a project. Required unless you have set the default project for interoperable access. | No  
  
## Request body elements

The following request body elements are applicable when creating a bucket. If you don't specify a request body, Cloud Storage creates a bucket in the `US` location with a default storage class of `STANDARD`.

Element | Description  
---|---  
`CreateBucketConfiguration` | Container for create body request.  
`LocationConstraint` | A [location](https://docs.cloud.google.com/storage/docs/locations) for the bucket. Can be the name of a single region, predefined dual-region, or multi-region.  
`CustomPlacementConfig` | Container for the `dataLocations` element. If present in the request, the `LocationConstraint` element must use a [valid location code](https://docs.cloud.google.com/storage/docs/locations#location-dr).  
`DataLocations` | Container for specifying the locations to use if the request creates a bucket in a [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr).  
`DataLocation` | One of the [regions](https://docs.cloud.google.com/storage/docs/locations#location-dr) to use for the configurable dual-region. If used, exactly two `dataLocation` elements are required in the request.  
`StorageClass` | The default [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for objects added to the bucket, such as `STANDARD`, `NEARLINE`, `COLDLINE`, or `ARCHIVE`.  
`EncryptionConfiguration` |  Container that defines the following encryption settings for the bucket:

  * The [default customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys), represented by the `DefaultKmsKeyName` element.
  * [Which encryption methods are allowed or restricted](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in the bucket, represented by the elements `CustomerManagedEncryptionEnforcement`, `CustomerSuppliedEncryptionEnforcement`, and `GoogleManagedEncryptionEnforcement`.

If this element is empty, then all encryption methods are allowed, and no default Cloud Key Management Service key is set for the bucket.  
`DefaultKmsKeyName` | The name of the [Cloud KMS key resource](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) to use by default for new objects added to the bucket.  
`CustomerManagedEncryptionEnforcement` |  Controls the use of [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) to encrypt objects in this bucket. If omitted, then creating new objects with CMEKs is allowed. If set, then new objects must comply with the encryption enforcement configuration. This property applies when new objects are created, including when soft-deleted objects are restored. Changing this property has no effect on existing objects. This element is a container for a `RestrictionMode` element.  
`CustomerSuppliedEncryptionEnforcement` |  Controls the use of [customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) to encrypt objects in this bucket. If omitted, then creating new objects with customer-supplied encryption keys is allowed. If set, then new objects must comply with the encryption enforcement configuration. This property applies when new objects are created, including when soft-deleted objects are restored. Changing this property has no effect on existing objects. This element is a container for a `RestrictionMode` element.  
`GoogleManagedEncryptionEnforcement` |  Controls the use of [standard encryption (Google default encryption)](https://docs.cloud.google.com/storage/docs/encryption) to encrypt objects in this bucket. If omitted, then creating new objects with standard encryption is allowed. If set, then new objects must comply with the encryption enforcement configuration. This property applies when new objects are created, including when soft-deleted objects are restored. Changing this property has no effect on existing objects. This element is a container for a `RestrictionMode` element.  
`RestrictionMode` |  The enforcement configuration for an encryption method. The following values are supported:

  * `NotRestricted`: new objects can use the encryption type.
  * `FullyRestricted`: new objects can't use the encryption type.

  
  
## Request syntax
    
    
    PUT / HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: REQUEST_BODY_LENGTH
    Authorization: AUTHENTICATION_STRING
    x-goog-project-id: PROJECT_ID
    x-goog-acl: PREDEFINED_ACL
    x-goog-bucket-object-lock-enabled: BOOLEAN
    x-goog-bucket-retention-period: TIME_IN_SECONDS
    
    <CreateBucketConfiguration>
      <LocationConstraint>LOCATION</LocationConstraint>
      <CustomPlacementConfig>
        <DataLocations>
          <DataLocation>REGION_1</DataLocation>
          <DataLocation>REGION_2</DataLocation>
        </DataLocations>
      </CustomPlacementConfig>
      <StorageClass>STORAGE_CLASS</StorageClass>
      <EncryptionConfiguration>
        <DefaultKmsKeyName>KEY_RESOURCE</DefaultKmsKeyName>
        <GoogleManagedEncryptionEnforcement>
          <RestrictionMode>STANDARD_ENCRYPTION_RESTRICTION_MODE</RestrictionMode>
        </GoogleManagedEncryptionEnforcement>
        <CustomerManagedEncryptionEnforcement>
          <RestrictionMode>CMEK_RESTRICTION_MODE</RestrictionMode>
        </CustomerManagedEncryptionEnforcement>
        <CustomerSuppliedEncryptionEnforcement>
          <RestrictionMode>CSEK_RESTRICTION_MODE</RestrictionMode>
        </CustomerSuppliedEncryptionEnforcement>
      <EncryptionConfiguration>
    </CreateBucketConfiguration>
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The response does not include an XML document in the response body.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
