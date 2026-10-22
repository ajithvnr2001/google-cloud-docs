---
url: https://docs.cloud.google.com/appengine/docs/standard/services/blobstore/
title: Overview of Blobstore API for legacy bundled services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:21.201058+00:00
---

# Overview of Blobstore API for legacy bundled services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/blobstore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Overview of Blobstore API for legacy bundled services Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

**Note:** You should consider using [Cloud Storage](https://docs.cloud.google.com/appengine/docs/standard/using-cloud-storage) rather than Blobstore for storing blob data.

The Blobstore API allows your application to serve data objects, called _blobs,_ that are much larger than the size allowed for objects in the Datastore service. Blobs are useful for serving large files, such as video or image files, and for allowing users to upload large data files. Blobs are created by uploading a file through an HTTP request. Typically, your applications will do this by presenting a form with a file upload field to the user. When the form is submitted, the Blobstore creates a blob from the file's contents and returns an opaque reference to the blob, called a _blob key,_ which you can later use to serve the blob. The application can serve the complete blob value in response to a user request, or it can read the value directly using a streaming file-like interface.

## Introducing the Blobstore

App Engine includes the Blobstore service, which allows applications to serve data objects limited only by the amount of data that can be uploaded or downloaded over a single HTTP connection. These objects are called _Blobstore values,_ or _blobs._ Blobstore values are served as responses from request handlers and are created as uploads via web forms. Applications do not create blob data directly; instead, blobs are created indirectly, by a submitted web form or other HTTP `POST` request. Blobstore values can be served to the user, or accessed by the application in a file-like stream, using the Blobstore API.

**Note:** Blobs as defined by the Blobstore service are not related to blob property values used by the datastore.

To prompt a user to upload a Blobstore value, your application presents a web form with a file upload field. The application generates the form's action URL by calling the Blobstore API. The user's browser uploads the file directly to the Blobstore via the generated URL. Blobstore then stores the blob, rewrites the request to contain the blob key, and passes it to a path in your application. A request handler at that path in your application can perform additional form processing.

To serve a blob, your application sets a header on the outgoing response, and App Engine replaces the response with the blob value.

Blobs can't be modified after they're created, though they can be deleted. Each blob has a corresponding _blob info record_ , stored in the datastore, that provides details about the blob, such as its creation time and content type. You can use the blob key to fetch blob info records and query their properties.

An application can read a Blobstore value a portion at a time using an API call. The size of the portion can be up to the maximum size of an API return value. This size is a little less than 32 megabytes, represented in Python by the constant [`google.appengine.ext.blobstore.MAX_BLOB_FETCH_SIZE`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore#functions) . An application cannot create or modify Blobstore values except through files uploaded by the user. 

## Using the Blobstore

Applications can use the Blobstore to accept large files as uploads from users and to serve those files. Files are called blobs once they're uploaded. Applications don't access blobs directly, instead, applications work with blobs through _blob info entities_ (represented by the [`BlobInfo`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobReferenceProperty/data_type) class) in the Datastore.

The user creates a blob by submitting an HTML form that includes one or more file input fields. Your application calls [`blobstore.create_upload_url()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_upload_url) to get the destination (action) of this form, passing the function a URL path of a handler in your application. When the user submits the form, the user's browser uploads the specified files directly to the Blobstore. The Blobstore rewrites the user's request and stores the uploaded file data, replacing the uploaded file data with one or more corresponding blob keys, then passes the rewritten request to the handler at the URL path you provided to [`blobstore.create_upload_url()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_upload_url) .

This handler can do additional processing based on the blob key. 

The application can read portions of a Blobstore value using a file-like streaming interface. See the [`BlobReader`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobReader) class. 

## Uploading a blob

To create and upload a blob, follow this procedure:

#### 1\. Create an upload URL

Call [`blobstore.create_upload_url()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_upload_url) to create an upload URL for the form that the user will fill out, passing the application path to load when the `POST` of the form is completed.
    
    
    upload_url = blobstore.create_upload_url("/upload_photo")

There is an asynchronous version, [`create_upload_url_async()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_upload_url_async). It allows your application code to continue running while Blobstore generates the upload URL.

#### 2\. Create an upload form

The form must include a file upload field, and the form's `enctype` must be set to `multipart/form-data`. When the user submits the form, the `POST` is handled by the Blobstore API, which creates the blob. The API also creates an info record for the blob and stores the record in the Datastore, and passes the rewritten request to your application on the given path as a blob key.

You must serve the form's page with a `Content-Type` of `text/html; charset=utf-8`, or any filenames with non-ASCII characters will be misinterpreted.  
Since Blobstore for Python 3 doesn't use webapp, you must set your own `Content-Type` to prevent your web framework from setting a default content-type and App Engine from setting this to a guessed type. 

You can't use a [global external Application Load Balancer with a Serverless NEG](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) to handle upload requests sent to the `/_ah/upload/` URL returned from the `blobstore.create_upload_url` call. Instead, you must route those upload requests directly to the App Engine service. You can do this by using either the `appspot.com` domain or a custom domain that is mapped directly to the App Engine service.

#### 3\. Implement upload handler

In this handler, you can store the blob key with the rest of your application's data model. The blob key itself remains accessible from the blob info entity in the Datastore. Note that after the user submits the form and your handler is called, the blob has already been saved and the blob info added to the Datastore. If your application doesn't want to keep the blob, you should delete the blob immediately to prevent it from becoming orphaned.

For all Flask apps, all calls made to methods in the [`BlobstoreUploadHandler`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobstoreUploadHandler) class require the `request.environ dictionary` (request being imported from the flask module). If your app is a WSGI app without a web framework, you use the `environ` parameter in the `get_uploads()` method. When rewriting the user's request, the Blobstore empties the MIME parts of the uploaded files and adds the blob key as a MIME part header. The Blobstore preserves all other form fields and parts, passing them to the upload handler. If you don't specify a content type, the Blobstore will try to infer it from the file extension. If it can't determine a content type, it assigns the content type `application/octet-stream` to the newly created blob. 

## Serving a blob

**Note:** If you are serving images, a more efficient and potentially less-expensive method is to use [`get_serving_url`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/get_serving_url) using the App Engine Images API rather than `send_blob` . The `get_serving_url` function lets you serve the image directly, without having to go through your App Engine instances.

To serve blobs, you must include a blob download handler as a path in your application. The application serves a blob by setting a header on the outgoing response. If using Flask, the [`BlobstoreDownloadHandler`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobstoreDownloadHandler) class requires the `request.environ` dictionary (request being imported from the flask module). If your app is a WSGI app without a web framework, you use the `environ` parameter in the `send_blob()` methods . 

Blobs can be served from any application URL. To serve a blob in your application, you put a special header in the response containing the blob key. App Engine replaces the body of the response with the content of the blob.

### Blob byte ranges

The Blobstore supports serving part of a large value instead of the full value in response to a request. To serve a partial value, include the `X-AppEngine-BlobRange` header in the outgoing response. Its value is a standard [HTTP byte range](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html). The byte numbering is zero-based. A blank `X-AppEngine-BlobRange` instructs the API to ignore the range header and serve the full blob. Example ranges include:

  * `0-499` serves the first 500 bytes of the value (bytes 0 through 499, inclusive).
  * `500-999` serves 500 bytes starting with the 501st byte.
  * `500-` serves all bytes starting with the 501st byte to the end of the value.
  * `-500` serves the last 500 bytes of the value.



If the byte range is valid for the Blobstore value, the Blobstore sends a `206` `Partial` `Content` status code and the requested byte range to the client. If the range is not valid for the value, the Blobstore sends `416` `Requested` `Range` `Not` `Satisfiable`.

The Blobstore does not support multiple byte ranges in a single request (for example, `100-199,200-299`), whether or not they overlap.

## Complete sample application

See the Flask app example in the [Blobstore API for Python 3](https://docs.cloud.google.com/appengine/docs/standard/python3/services/blobstore#example_flask_app) guide.

## Using the Images service with the Blobstore

The Images service can use a Blobstore value as the source of a transformation. The source image can be as large as the maximum size for a Blobstore value. The Images service still returns the transformed image to the application, so the transformed image must be smaller than 32 megabytes. This is useful for making thumbnail images of large photographs uploaded by users. For information on using the Images service with Blobstore values, see the [Images Service documentation](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images). 

## Using the Blobstore API with Cloud Storage

You can use the Blobstore API to store blobs in Cloud Storage instead of storing them in Blobstore. You need to set up a bucket as described in the [Cloud Storage](https://docs.cloud.google.com/appengine/docs/standard/using-cloud-storage) documentation and specify the bucket and filename in the [`blobstore.create_upload_url`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_upload_url) `gs_bucket_name` parameter. 

In your upload handler, you need to process the returned [FileInfo](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/FileInfo) metadata and explicitly store the Cloud Storage filename needed to retrieve the blob later.

You can also serve Cloud Storage objects using the Blobstore API.

**Note:** Once you obtain a `blobKey` for the Cloud Storage object, you can pass it around, serialize it, and otherwise use it interchangeably anywhere you can use a `blobKey` for objects stored in Blobstore. This allows for usage where an app stores some data in blobstore and some in Cloud Storage, but treats the data otherwise identically by the rest of the app. (However, `BlobInfo` objects are not available for Cloud Storage objects.)

If you want a more modern object storage solution, consider [migrating from App Engine Blobstore to Cloud Storage](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-storage).

## Using BlobReader

An application can read data from Blobstore values using an interface similar to a Python [`file`](http://docs.python.org/library/stdtypes.html#file-objects) object. This interface can start reading a value at any byte position, and uses multiple service calls and buffering, so an application can access the full size of the value despite the limit on the size of a single service call response.

The [`BlobReader`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobReader) class can take one of three values as an argument to its constructor:

  * A [`BlobKey`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/BlobKey)
  * The string form of a BlobKey
  * A [`BlobInfo`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobReferenceProperty/data_type) object



The object implements the familiar file methods for reading the value. The application cannot modify the Blobstore value; file methods for writing are not implemented.
    
    
    # Instantiate a BlobReader for a given Blobstore blob_key.
    blob_reader = blobstore.BlobReader(blob_key)
    
    # Instantiate a BlobReader for a given Blobstore blob_key, setting the
    # buffer size to 1 MB.
    blob_reader = blobstore.BlobReader(blob_key, buffer_size=1048576)
    
    # Instantiate a BlobReader for a given Blobstore blob_key, setting the
    # initial read position.
    blob_reader = blobstore.BlobReader(blob_key, position=0)
    
    # Read the entire value into memory. This may take a while depending
    # on the size of the value and the size of the read buffer, and is not
    # recommended for large values.
    blob_reader_data = blob_reader.read()
    
    # Write the contents to the response.
    self.response.headers["Content-Type"] = "text/plain"
    self.response.write(blob_reader_data)
    
    # Set the read position back to 0, then read and write 3 bytes.
    blob_reader.seek(0)
    blob_reader_data = blob_reader.read(3)
    self.response.write(blob_reader_data)
    self.response.write("\n")
    
    # Set the read position back to 0, then read and write one line (up to
    # and including a '\n' character) at a time.
    blob_reader.seek(0)
    for line in blob_reader:
        self.response.write(line)

## Making asynchronous requests

An application can call some Blobstore functions that work in the background. Blobstore carries out the request while the application does other things. To make the request, the application calls an asynchronous function. The function immediately returns an RPC object; this object represents the request. When the application needs the result of the request, it calls the RPC object's `get_result()` method.

If the service has not completed the request when the application calls `get_result()`, the method waits until the request is complete (or has reached the deadline, or an error occurs). The method returns the result object, or raises an exception if an error occurred while carrying out the request. For example, this code snippet
    
    
    upload_url = blobstore.create_upload_url('/upload')
    slow_operation()
    self.response.out.write("""<form action="%s" method="POST"
                               enctype="multipart/form-data">""" % upload_url)
    

becomes
    
    
    upload_url_rpc = blobstore.create_upload_url_async('/upload')
    slow_operation()
    upload_url = upload_url_rpc.get_result()
    self.response.out.write("""<form action="%s" method="POST"
                               enctype="multipart/form-data">""" % upload_url)
    

In this example, the application carries out the `slow_operation()` code at the same time that Blobstore generates the upload URL.

## Quotas and limits

Space used for Blobstore values contributes to the **Stored Data (billable)** quota. Blob info entities in the Datastore count towards Datastore-related limits. Notice that Cloud Storage is a pay-to-use service; you will be charged according to the Cloud Storage [price sheet](https://cloud.google.com/storage/pricing).

For more information on system-wide safety quotas, see [Quotas](https://docs.cloud.google.com/appengine/docs/quotas).

In addition to system-wide safety quotas, the following limits apply specifically to the use of the Blobstore:

  * The maximum size of Blobstore data that can be read by the application with one API call is 32 megabytes.
  * The maximum number of files that can be uploaded in a single form POST is 500.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
