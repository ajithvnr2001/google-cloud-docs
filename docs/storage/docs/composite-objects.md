---
url: https://docs.cloud.google.com/storage/docs/composite-objects/
title: Composite objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:20.959667+00:00
---

# Composite objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/composite-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Composite objects Stay organized with collections  Save and categorize content based on your preferences. 

[Create](https://docs.cloud.google.com/storage/docs/composing-objects)

This page describes composite objects, which you create from existing objects without transferring additional object data. Composite objects are useful for making appends to an existing object, as well as for recreating objects that you [uploaded as multiple components in parallel](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads).

## Compose operation

The compose operation concatenates the data in a given sequence of source objects to create a new object called a _composite object_. The source objects must meet these requirements:

  * All of the source objects must have the same [storage class](https://docs.cloud.google.com/storage/docs/storage-classes).
  * All of the source objects must be stored in the same Cloud Storage bucket.



When you perform a composition, note the following:

  * You can optionally hard delete the source objects as part of the composition process. Use this option to minimize billing for temporary objects that don't need to be protected by soft delete or Object Versioning. 
  * You can compose between 1 and 32 source objects.
  * Source objects can themselves be composite objects.



The composite object that results from a composition has these characteristics:

  * The composite object has the same storage class as the source objects.
  * The composite object doesn't change if the source objects are subsequently replaced or deleted.



When using [`gcloud storage`](https://docs.cloud.google.com/sdk/gcloud/reference/storage) to perform object composition, the object that results has a [`Content-Type`](https://docs.cloud.google.com/storage/docs/metadata#content-type) set to match the `Content-Type` of the first source object.

## Composite object metadata

There are several differences between the metadata of a composite object and the metadata of other objects:

  * Composite objects _do not_ have an MD5 hash metadata field.

    * Any MD5 value you provide as part of a compose request is ignored.
  * The ETag value of a composite object is not based on an MD5 hash, and client code should make no assumptions about composite object ETags except that they change whenever the underlying object changes per the [IETF specification for HTTP/1.1](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3).

**Caution:** Exercise caution when first using composite objects, since any clients expecting to find an MD5 digest within the ETag header may conclude that object data has been corrupted, which could trigger endless data retransmission attempts.
  * Each composite object has a _component count_ metadata field, which counts the number of non-composite objects contained within the composite object.

    * If you rewrite a composite object to a different location or storage class, the result is a composite object with a component count of 1.



## Integrity Checking Composite Objects

Cloud Storage uses [CRC32C](https://datatracker.ietf.org/doc/html/rfc4960#appendix-B) for integrity checking each source object at upload time and for allowing the caller to perform an integrity check of the resulting composite object when it is downloaded. CRC32C is an error detecting code that can be efficiently calculated from the CRC32C values of its components. Your application should use CRC32C as follows:

  * When uploading source objects, you should calculate the CRC32C for each object using a CRC32C library, such as one of those listed in the [Object metadata page](https://docs.cloud.google.com/storage/docs/metadata#crc32c), and include that value in your request. Based on the values you provide, Cloud Storage [validates each upload](https://docs.cloud.google.com/storage/docs/data-validation).
  * The compose operation automatically checks that the source objects are correctly assembled, and it ignores any CRC32C value you provide as part of the compose request. A CRC32C of the resulting composite object is returned in the response.
  * If your application could change source objects between the time of uploading and composing those objects, you should specify generation-specific names for the source objects to avoid race conditions. Alternatively, you can build a CRC32C value from the CRC32C values of the intended source objects and compare it to the CRC32C value returned by the compose operation.
  * At download time, you should calculate the CRC32C of the downloaded object and compare that with the value included in the response.

**Note:** CRC32C is not intended to protect against ["man-in-the-middle"](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) attacks, where someone modifies the content in a way that still matches the provided checksum. Protection against such attacks is provided by using SSL connections when uploading and downloading objects, which is the default for many tools and libraries, such as the Google Cloud CLI.

## Append and edit

You can use the compose operation to perform object appends and edits.

To append data to an existing object, first you create a temporary object that contains the data that you want to append. Then, you compose the existing object with the temporary object. As part of the composition process, you can delete the temporary object and the previous version of the original object. You can also name the resulting object the same as the original object.

For example, in the gcloud CLI, the following commands append the string `new data` to an existing object:
    
    
    $ echo 'new data' | gcloud storage cp - gs://bucket/temporary_object
    $ gcloud storage objects compose gs://bucket/existing_object gs://bucket/temporary_object \
        gs://bucket/existing_object --delete-source-objects

**Caution:** Compose operations create a new version of an object. When performing appends in a bucket with [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) or [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) enabled, be sure to use the `--delete-source-objects` option to avoid creating additional versions that incur extra storage charges. 

You can also use composition to support a basic flavor of object editing. For example, you could compose an object _X_ from the sequence _{Y1, Y2, Y3}_ , replace the contents of _Y2_ , and recompose _X_ from those same components. Note that this requires that _Y1_ , _Y2_ , and _Y3_ be left undeleted, so you will be billed for those components as well as for the composite.

## Composite object contexts

When you use the [compose operation](https://docs.cloud.google.com/storage/docs/composing-objects), Cloud Storage merges all [contexts](https://docs.cloud.google.com/storage/docs/object-contexts) from the source objects and attaches them to the destination object. This process handles both unique and duplicate context keys as described in the following sections.

This merging behavior is the default. It occurs when you don't specify contexts for the destination object in the compose request. You can override this default behavior by clearing contexts or specifying new contexts for the destination object during the [compose operation](https://docs.cloud.google.com/storage/docs/use-object-contexts#compose-objects).

### Unique context keys

If source objects have unique context keys, Cloud Storage directly attaches these keys and their corresponding values to the destination object.

Consider the following example:

Source object A contexts: `Department: Engineering, Status: Active`

Source object B contexts: `Owner: m_jones, Version: 1.1`

After the compose operation, the destination object has the following combined contexts:
    
    
      {
        "contexts": {
          "custom": {
            "Department": {
              "value": "Engineering",
              "createTime": "2023-10-26T10:00:00.000Z",
              "updateTime": "2023-10-26T10:00:00.000Z"
            },
            "Status": {
              "value": "Active",
              "createTime": "2023-10-26T10:00:00.000Z",
              "updateTime": "2023-10-26T10:00:00.000Z"
            },
            "Owner": {
              "value": "m_jones",
              "createTime": "2023-10-26T10:00:00.000Z",
              "updateTime": "2023-10-26T10:00:00.000Z"
            },
            "Version": {
              "value": "1.1",
              "createTime": "2023-10-26T10:00:00.000Z",
              "updateTime": "2023-10-26T10:00:00.000Z"
            }
          }
        }
      }
      

### Duplicate context keys

When multiple source objects have the same context key, the value from the last source object in the compose list that contains that key is used for the composed object.

For example, consider source objects processed in the following order:

  1. Source object A

  2. Source object B




Source object A contexts: `Version: 1.0, ReleaseDate: 2024-01-15`

Source object B contexts: `Version: 1.1, Owner: m_jones`

Both source objects have a `Version` key, but object A has `Version: 1.0` and object B has `Version: 1.1`. Because Cloud Storage processes source object B after source object A, the `Version` value from source object B takes precedence and the final value is `1.1`.

The destination object combines these contexts as follows:
    
    
      {
        "contexts": {
          "custom": {
            "Version": {
              "value": "1.1",
              "createTime": "2025-01-01T00:00:00.000Z",
              "updateTime": "2025-01-01T00:00:00.000Z"
            },
            "ReleaseDate": {
              "value": "2024-01-15",
              "createTime": "2025-01-01T00:00:00.000Z",
              "updateTime": "2025-01-01T00:00:00.000Z"
            },
            "Owner": {
              "value": "m_jones",
              "createTime": "2025-01-01T00:00:00.000Z",
              "updateTime": "2025-01-01T00:00:00.000Z"
            }
          }
        }
      }
      

## What's next

  * [Compose an object](https://docs.cloud.google.com/storage/docs/composing-objects).
  * Learn about [parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads).
  * Learn about [Multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads), an alternative way to upload objects in multiple chunks for XML API users.
  * Learn about [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
