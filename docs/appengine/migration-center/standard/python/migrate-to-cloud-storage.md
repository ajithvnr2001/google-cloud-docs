---
url: https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-storage/
title: Migrate App Engine Blobstore to Cloud Storage \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:45.067812+00:00
---

# Migrate App Engine Blobstore to Cloud Storage  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate App Engine Blobstore to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This guide covers how to migrate from App Engine Blobstore to [Cloud Storage](https://docs.cloud.google.com/storage/docs).

Cloud Storage is similar to App Engine Blobstore in that you can use Cloud Storage to serve large data objects (blobs), such as video or image files, and enable your users to upload large data files. While App Engine Blobstore is accessible only through the App Engine legacy bundled services, Cloud Storage is a standalone Google Cloud product that is accessed through the Cloud Client Libraries. Cloud Storage offers your app a more modern object storage solution and gives you the flexibility of migrating to Cloud Run or another Google Cloud app hosting platform later on.

For Google Cloud projects created after November 2016, Blobstore uses Cloud Storage buckets behind the scenes. This means that when you migrate your app to Cloud Storage, all of your existing objects and permissions in those existing Cloud Storage buckets remain unchanged. You can also start accessing those existing buckets using the [Cloud Client Libraries for Cloud Storage](https://docs.cloud.google.com/storage/docs/reference/libraries).

## Key differences and similarities

Cloud Storage excludes the following Blobstore dependencies and limitations:

  * The Blobstore API for Python 2 has a dependency on webapp.
  * The Blobstore API for Python 3 uses utility classes to use [Blobstore handlers](https://docs.cloud.google.com/appengine/docs/standard/python3/services/blobstore).
  * For Blobstore, the maximum number of files that can be uploaded to Blobstore is 500. There is no limit on the number of objects you can create in a Cloud Storage bucket.



Cloud Storage does not support:

  * Blobstore handler classes
  * Blobstore objects



Cloud Storage and App Engine Blobstore similarities:

  * Able to read and write large data objects in a runtime environment, as well as store and serve static large data objects, such as movies, images, or other static content. The object size limit for Cloud Storage is 5 TiB.
  * Lets you store objects in a Cloud Storage bucket.
  * Have a free tier.



## Before you begin

  * You should review and understand Cloud Storage pricing and quotas: 
    * Cloud Storage is a pay-to-use service and has its own [pricing](https://cloud.google.com/storage/pricing) for data storage based on the storage class of your data and the location of your buckets.
    * The [Cloud Storage quotas](https://docs.cloud.google.com/storage/quotas) have some differences from [App Engine Blobstore quotas and limits](https://docs.cloud.google.com/appengine/docs/standard/services/blobstore#Quotas_and_limits), which might impact your App Engine request quotas.
  * Have an existing Python 2 or Python 3 App Engine app that is using Blobstore.
  * The examples in this guide show an app that migrates to Cloud Storage using the Flask framework. Note that you can use any web framework, including staying on `webapp2`, when migrating to Cloud Storage.



## Overview

At a high level, the process to migrate to Cloud Storage from App Engine Blobstore consists of the following steps:

  1. Update configuration files
  2. Update your Python app: 
     * Update your web framework
     * Import and initialize Cloud Storage
     * Update Blobstore handlers
     * Optional: Update your data model if using Cloud NDB or App Engine NDB
  3. Test and deploy your app



## Update configuration files

Before modifying your application code to move from Blobstore to Cloud Storage, update your configuration files to use the Cloud Storage library.

  1. Update the `app.yaml` file. Follow the instructions for your version of Python:

###  Python 2 

For Python 2 apps:

     1. Remove the `handlers` section and any unnecessary webapp-dependencies in the `libraries` section.
     2. If you use Cloud Client Libraries, add the latest versions of `grpcio` and `setuptools` libraries.
     3. Add the `ssl` library since this is required by Cloud Storage.

The following is an example `app.yaml` file with the changes made:
    
    runtime: python27
    threadsafe: yes
    api_version: 1
    
    handlers:
    - url: /.*
      script: main.app
    
    libraries:
    - name: grpcio
      version: latest
    - name: setuptools
      version: latest
    - name: ssl
      version: latest
    

###  Python 3 

For Python 3 apps, delete all lines except for the `runtime` element. For example:
    
    runtime: python310 # or another support version
    

The Python 3 runtime installs libraries automatically, so you do not need to specify built-in libraries from the previous Python 2 runtime. If your Python 3 app is using other legacy bundled services when migrating to Cloud Storage, leave the `app.yaml` file as is.

  2. Update the `requirements.txt` file. Follow the instructions for your version of Python:

###  Python 2 

Add the Cloud Client Libraries for Cloud Storage to your list of dependencies in the `requirements.txt` file.
         
         google-cloud-storage
         

Then run `pip install -t lib -r requirements.txt` to update the list of available libraries for your app.

###  Python 3 

Add the Cloud Client Libraries for Cloud Storage to your list of dependencies in the `requirements.txt` file.
         
         google-cloud-storage
         

App Engine automatically installs these dependencies during app deployment in the Python 3 runtime, so delete the `lib` folder if one exists.

  3. For Python 2 apps, if your app is using built-in or copied libraries, you must specify those paths in the `appengine_config.py` file:
         
         import pkg_resources
         from google.appengine.ext import vendor
         
         # Set PATH to your libraries folder.
         PATH = 'lib'
         # Add libraries installed in the PATH folder.
         vendor.add(PATH)
         # Add libraries to pkg_resources working set to find the distribution.
         pkg_resources.working_set.add_entry(PATH)
         




## Update your Python app

After modifying your configuration files, update your Python app.

### Update your Python 2 web framework

For Python 2 apps that use the `webapp2` framework, it is recommended to migrate off the outdated `webapp2` framework. See the [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#python) for the Python 2 end of support date.

You can migrate to another web framework such as [Flask](https://codelabs.developers.google.com/codelabs/cloud-gae-python-migrate-1-flask), Django, or WSGI. Since Cloud Storage excludes dependencies on `webapp2` and Blobstore handlers are unsupported, you can delete or replace other webapp-related libraries.

If you choose to continue using `webapp2`, note that the examples throughout this guide use Cloud Storage with Flask.

If you plan to use the Google Cloud services in addition to Cloud Storage, or to gain access to the latest runtime versions, you should consider upgrading your app to the Python 3 runtime. For more information, see [Python 2 to Python 3 migration overview](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/python-differences).

### Import and initialize Cloud Storage

Modify your application files by updating the import and initialization lines:

  1. Remove Blobstore import statements, like the following:
         
         import webapp2
         from google.appengine.ext import blobstore
         from google.appengine.ext.webapp import blobstore_handlers
         

  2. Add the import statements for Cloud Storage and the Google Authentication libraries, like the following:
         
         import io
         from flask import (Flask, abort, redirect, render_template,
         request, send_file, url_for)
         from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         import google.auth
         

The Google Authentication library is needed to get the same project ID that was used in Blobstore for Cloud Storage. Import other libraries like Cloud NBD if applicable to your app.

  3. Create a new client for Cloud Storage and specify the bucket that is used in Blobstore. For example:
         
         gcs_client = storage.Client()
         _, PROJECT_ID = google.auth.default()
         BUCKET = '%s.appspot.com' % PROJECT_ID
         

For Google Cloud projects after November 2016, Blobstore writes to a Cloud Storage bucket named after your app's URL and follows the format of `PROJECT_ID.appspot.com`. You use Google authentication to get the project ID to specify the Cloud Storage bucket that is used for storing blobs in Blobstore.




### Update Blobstore handlers

Since Cloud Storage does not support the Blobstore upload and download handlers, you need to use a combination of Cloud Storage functionality, `io` standard library module, your web framework, and Python utilities to upload and download objects (blobs) in Cloud Storage.

The following demonstrates how to update the Blobstore handlers using Flask as the example web framework:

  1. Replace your Blobstore upload handler classes with an upload function in Flask. Follow the instructions for your version of Python:

###  Python 2 

Blobstore handlers in Python 2 are `webapp2` classes as shown in the following Blobstore example:
         
         class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
             'Upload blob (POST) handler'
             def post(self):
                 uploads = self.get_uploads()
                 blob_id = uploads[0].key() if uploads else None
                 store_visit(self.request.remote_addr, self.request.user_agent, blob_id)
                 self.redirect('/', code=307)
         ...
         app = webapp2.WSGIApplication([
             ('/', MainHandler),
             ('/upload', UploadHandler),
             ('/view/([^/]+)?', ViewBlobHandler),
         ], debug=True)
         

To use Cloud Storage:

     1. Replace the Webapp upload class with a Flask upload function.
     2. Replace the upload handler and routing with a Flask `POST` method decorated with routing.

**Updated code sample** :
    
    @app.route('/upload', methods=['POST'])
    def upload():
        'Upload blob (POST) handler'
        fname = None
        upload = request.files.get('file', None)
        if upload:
            fname = secure_filename(upload.filename)
            blob = gcs_client.bucket(BUCKET).blob(fname)
            blob.upload_from_file(upload, content_type=upload.content_type)
        store_visit(request.remote_addr, request.user_agent, fname)
        return redirect(url_for('root'), code=307)
    

In the updated Cloud Storage code sample, the app now identifies object artifacts by its object name (`fname`) instead of `blob_id`. Routing also occurs at the bottom of the application file.

To get the uploaded object, Blobstore's `get_uploads()` method is replaced with Flask's `request.files.get()` method. In Flask, you can use the `secure_filename()` method to get a name without path characters, such as `/`, for the file, and identify the object by using [`gcs_client.bucket(BUCKET).blob(fname)`](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket#google_cloud_storage_bucket_Bucket_blob) to specify the bucket name and object name.

The Cloud Storage [`upload_from_file()`](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_upload_from_file) call performs the upload as shown in the updated example.

###  Python 3 

The upload handler class in Blobstore for Python 3 is a utility class and requires using the [WSGI `environ` dictionary](https://www.python.org/dev/peps/pep-0333/#environ-variables) as an input parameter, as shown in the following Blobstore example:
    
    class UploadHandler(blobstore.BlobstoreUploadHandler):
        'Upload blob (POST) handler'
        def post(self):
            uploads = self.get_uploads(request.environ)
            if uploads:
                blob_id = uploads[0].key()
                store_visit(request.remote_addr, request.user_agent, blob_id)
            return redirect('/', code=307)
    ...
    @app.route('/upload', methods=['POST'])
    def upload():
        """Upload handler called by blobstore when a blob is uploaded in the test."""
        return UploadHandler().post()
    

To use Cloud Storage, replace Blobstore's `get_uploads(request.environ)` method with Flask's `request.files.get()` method.

**Updated code sample** :
    
    @app.route('/upload', methods=['POST'])
    def upload():
        'Upload blob (POST) handler'
        fname = None
        upload = request.files.get('file', None)
        if upload:
            fname = secure_filename(upload.filename)
            blob = gcs_client.bucket(BUCKET).blob(fname)
            blob.upload_from_file(upload, content_type=upload.content_type)
        store_visit(request.remote_addr, request.user_agent, fname)
        return redirect(url_for('root'), code=307)
    

In the updated Cloud Storage code sample, the app now identifies object artifacts by its object name (`fname`) instead of `blob_id`. Routing also occurs at the bottom of the application file.

To get the uploaded object, Blobstore's `get_uploads()` method is replaced with Flask's `request.files.get()` method. In Flask, you can use the `secure_filename()` method to get a name without path characters, such as `/`, for the file, and identify the object by using [`gcs_client.bucket(BUCKET).blob(fname)`](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket#google_cloud_storage_bucket_Bucket_blob) to specify the bucket name and object name.

The Cloud Storage [`upload_from_file()`](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_upload_from_file) method performs the upload as shown in the updated example.

  2. Replace your Blobstore Download handler classes with a download function in Flask. Follow the instructions for your version of Python:

###  Python 2 

The following download handler example shows the use of `BlobstoreDownloadHandler` class, which uses webapp2:
         
         class ViewBlobHandler(blobstore_handlers.BlobstoreDownloadHandler):
             'view uploaded blob (GET) handler'
             def get(self, blob_key):
                 self.send_blob(blob_key) if blobstore.get(blob_key) else self.error(404)
         ...
         app = webapp2.WSGIApplication([
             ('/', MainHandler),
             ('/upload', UploadHandler),
             ('/view/([^/]+)?', ViewBlobHandler),
         ], debug=True)
         

To use Cloud Storage:

     1. Update Blobstore's `send_blob()` method to use Cloud Storage's [`download_as_bytes()`](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_download_as_bytes) method.
     2. Change routing from webapp2 to Flask.

**Updated code sample** :
    
    @app.route('/view/<path:fname>')
    def view(fname):
        'view uploaded blob (GET) handler'
        blob = gcs_client.bucket(BUCKET).blob(fname)
        try:
            media = blob.download_as_bytes()
        except exceptions.NotFound:
            abort(404)
        return send_file(io.BytesIO(media), mimetype=blob.content_type)
    

In the updated Cloud Storage code sample, Flask decorates the route in the Flask function and identifies the object using `'/view/<path:fname>'`. Cloud Storage identifies the `blob` object by the object name and bucket name, and uses the `download_as_bytes()` method to download the object as bytes, instead of using the `send_blob` method from Blobstore. If the artifact isn't found, the app returns an HTTP `404` error.

###  Python 3 

Like the upload handler, the download handler class in Blobstore for Python 3 is a utility class and requires using the [WSGI `environ` dictionary](https://www.python.org/dev/peps/pep-0333/#environ-variables) as an input parameter, as shown in the following Blobstore example:
    
    class ViewBlobHandler(blobstore.BlobstoreDownloadHandler):
        'view uploaded blob (GET) handler'
        def get(self, blob_key):
            if not blobstore.get(blob_key):
                return "Photo key not found", 404
            else:
                headers = self.send_blob(request.environ, blob_key)
    
            # Prevent Flask from setting a default content-type.
            # GAE sets it to a guessed type if the header is not set.
            headers['Content-Type'] = None
            return '', headers
    ...
    @app.route('/view/<blob_key>')
    def view_photo(blob_key):
        """View photo given a key."""
        return ViewBlobHandler().get(blob_key)
    

To use Cloud Storage, replace Blobstore's `send_blob(request.environ, blob_key)` with Cloud Storage's [`blob.download_as_bytes()`](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_download_as_bytes) method.

**Updated code sample** :
    
    @app.route('/view/<path:fname>')
    def view(fname):
        'view uploaded blob (GET) handler'
        blob = gcs_client.bucket(BUCKET).blob(fname)
        try:
            media = blob.download_as_bytes()
        except exceptions.NotFound:
            abort(404)
        return send_file(io.BytesIO(media), mimetype=blob.content_type)
    

In the updated Cloud Storage code sample,`blob_key` is replaced with `fname`, and Flask identifies the object using the `'/view/<path:fname>'` URL. The `gcs_client.bucket(BUCKET).blob(fname)` method is used to locate the file name and the bucket name. Cloud Storage's `download_as_bytes()` method downloads the object as bytes, instead of using the `send_blob()` method from Blobstore.

  3. If your app uses a main handler, replace the `MainHandler` class with the `root()` function in Flask. Follow the instructions for your version of Python:

###  Python 2 

The following is an example of using Blobstore's `MainHandler` class:
         
         class MainHandler(BaseHandler):
             'main application (GET/POST) handler'
             def get(self):
                 self.render_response('index.html',
                         upload_url=blobstore.create_upload_url('/upload'))
         
             def post(self):
                 visits = fetch_visits(10)
                 self.render_response('index.html', visits=visits)
         
         app = webapp2.WSGIApplication([
             ('/', MainHandler),
             ('/upload', UploadHandler),
             ('/view/([^/]+)?', ViewBlobHandler),
         ], debug=True)
         

To use Cloud Storage:

     1. Remove the `MainHandler(BaseHandler)` class, since Flask handles routing for you.
     2. Simplify the Blobstore code with Flask.
     3. Remove the webapp routing at the end.

**Updated code sample** :
    
    @app.route('/', methods=['GET', 'POST'])
    def root():
        'main application (GET/POST) handler'
        context = {}
        if request.method == 'GET':
            context['upload_url'] = url_for('upload')
        else:
            context['visits'] = fetch_visits(10)
        return render_template('index.html', **context)
    

###  Python 3 

If you used Flask, you won't have a `MainHandler` class, but your Flask root function needs to be updated if blobstore is used. The following example uses the [`blobstore.create_upload_url('/upload')`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/blobstore/create_upload_url) function:
    
    @app.route('/', methods=['GET', 'POST'])
    def root():
        'main application (GET/POST) handler'
        context = {}
        if request.method == 'GET':
            context['upload_url'] = blobstore.create_upload_url('/upload')
        else:
            context['visits'] = fetch_visits(10)
        return render_template('index.html', **context)
    

To use Cloud Storage, replace the `blobstore.create_upload_url('/upload')` function with Flask's `url_for()` method to get the URL for the `upload()` function.

**Updated code sample** :
    
    @app.route('/', methods=['GET', 'POST'])
    def root():
        'main application (GET/POST) handler'
        context = {}
        if request.method == 'GET':
            context['upload_url'] = url_for('upload') # Updated to use url_for
        else:
            context['visits'] = fetch_visits(10)
        return render_template('index.html', **context)
    




## Test and deploy your app

The local development server lets you test that your app runs, but won't be able to test Cloud Storage until you deploy a new version because all Cloud Storage requests need to be sent over the Internet to an actual Cloud Storage bucket. See [Testing and deploying your application](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app) for how to run your application locally. Then deploy a new version to confirm the app appears the same as before.

## Apps using App Engine NDB or Cloud NDB

You must update your Datastore data model if your app uses App Engine NDB or Cloud NDB to include Blobstore-related properties.

### Update your data model

Since the `BlobKey` properties from NDB are not supported by Cloud Storage, you need to modify the Blobstore-related lines to use built-in equivalents from NDB, web frameworks, or elsewhere.

**Important:** If you replace `ndb.BlobKeyProperty` with `ndb.StringProperty`, your app won't be able to process older entries created by Blobstore. To retain your old data, you must follow the steps in the following backwards compatibility for Datastore section.

To update your data model:

  1. Find the lines that use `BlobKey` in the data model, like the following:
         
         class Visit(ndb.Model):
             'Visit entity registers visitor IP address & timestamp'
             visitor   = ndb.StringProperty()
             timestamp = ndb.DateTimeProperty(auto_now_add=True)
             file_blob = ndb.BlobKeyProperty()
         

  2. Replace [`ndb.BlobKeyProperty()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/BlobKeyProperty) with [`ndb.StringProperty()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/StringProperty):
         
         class Visit(ndb.Model):
             'Visit entity registers visitor IP address & timestamp'
             visitor   = ndb.StringProperty()
             timestamp = ndb.DateTimeProperty(auto_now_add=True)
             file_blob = ndb.StringProperty() # Modified from ndb.BlobKeyProperty()
         

  3. If you are also upgrading from App Engine NDB to Cloud NDB during the migration, see the [Cloud NDB migration guide](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-ndb#using_the_clients_runtime_context) for guidance on how to refactor the NDB code to use Python context managers.




### Backwards compatibility for Datastore data model

In the previous section, replacing `ndb.BlobKeyProperty` with `ndb.StringProperty` made the app backwards incompatible, meaning that the app won't be able to process older entries created by Blobstore. If you need to retain old data, create an additional field for new Cloud Storage entries instead of updating the `ndb.BlobKeyProperty` field, and create a function to normalize the data.

From the examples in previous sections, make the following changes:

  1. Create two separate property fields when defining your data model. Use the `file_blob` property to identify Blobstore-created objects and the `file_gcs` property to identify Cloud Storage-created objects:
         
         class Visit(ndb.Model):
             'Visit entity registers visitor IP address & timestamp'
             visitor   = ndb.StringProperty()
             timestamp = ndb.DateTimeProperty(auto_now_add=True)
             file_blob = ndb.BlobKeyProperty()  # backwards-compatibility
             file_gcs  = ndb.StringProperty()
         

  2. Find the lines that reference new visits, like the following:
         
         def store_visit(remote_addr, user_agent, upload_key):
             'create new Visit entity in Datastore'
             with ds_client.context():
                 Visit(visitor='{}: {}'.format(remote_addr, user_agent),
                         file_blob=upload_key).put()
         

  3. Change your code so that `file_gcs` is used for recent entries. For example:
         
         def store_visit(remote_addr, user_agent, upload_key):
             'create new Visit entity in Datastore'
             with ds_client.context():
                 Visit(visitor='{}: {}'.format(remote_addr, user_agent),
                         file_gcs=upload_key).put() # change file_blob to file_gcs for new requests
         

  4. Create a new function to normalize the data. The following example shows the use of extract, transform, and low (ETL) to loop through all visits, and takes the visitor and timestamp data to check if `file_gcs` or `file_gcs` exists:
         
         def etl_visits(visits):
             return [{
                     'visitor': v.visitor,
                     'timestamp': v.timestamp,
                     'file_blob': v.file_gcs if hasattr(v, 'file_gcs') \
                             and v.file_gcs else v.file_blob
                     } for v in visits]
         

  5. Find the line that references the `fetch_visits()` function:
         
         @app.route('/', methods=['GET', 'POST'])
         def root():
             'main application (GET/POST) handler'
             context = {}
             if request.method == 'GET':
                 context['upload_url'] = url_for('upload')
             else:
                 context['visits'] = fetch_visits(10)
             return render_template('index.html', **context)
         

  6. Wrap the `fetch_visits()` inside the `etl_visits()` function, for example:
         
         @app.route('/', methods=['GET', 'POST'])
         def root():
             'main application (GET/POST) handler'
             context = {}
             if request.method == 'GET':
                 context['upload_url'] = url_for('upload')
             else:
                 context['visits'] = etl_visits(fetch_visits(10)) # etl_visits wraps around fetch_visits
             return render_template('index.html', **context)
         




## Examples

  * To see an example of how to migrate a Python 2 app to Cloud Storage, compare the [Blobstore for Python 2 code sample](https://github.com/googlecodelabs/migrate-python2-appengine/tree/master/mod15-blobstore) and the [Cloud Storage code sample](https://github.com/googlecodelabs/migrate-python2-appengine/tree/master/mod16-cloudstorage) in GitHub.
  * To see an example of how to migrate a Python 3 app to Cloud Storage, compare the [Blobstore for Python 3 code sample](https://github.com/googlecodelabs/migrate-python2-appengine/tree/master/mod15b-blobstore) and the [Cloud Storage code sample](https://github.com/googlecodelabs/migrate-python2-appengine/tree/master/mod16-cloudstorage) in GitHub.



## What's next

  * For a hands-on tutorial, see the [Migrate from App Engine Blobstore to Cloud Storage codelab for Python](https://codelabs.developers.google.com/codelabs/cloud-gae-python-migrate-16-cloudstorage).
  * Learn how to [store and service static files from Cloud Storage](https://docs.cloud.google.com/appengine/docs/standard/serving-static-files).
  * See [Cloud Storage documentation](https://docs.cloud.google.com/storage/docs) for more details.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
