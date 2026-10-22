---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/services/blobstore/
title: Blobstore API for Python 3 \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:20:02.593508+00:00
---

# Blobstore API for Python 3  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/services/blobstore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Blobstore API for Python 3 Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the Blobstore API, one of the legacy bundled services, with the [Python 3 runtime](https://docs.cloud.google.com/appengine/docs/standard/python3) for the standard environment. Your app can access the bundled services through the [**App Engine services SDK for Python 3**](https://github.com/GoogleCloudPlatform/appengine-python-standard).

## Overview

Since webapp is not supported in Python 3, you need to make some minimal changes when migrating Blobstore handler code from Python 2 to Python 3. To use the Blobstore API for Python 3, keep in mind the following:

  * Blobstore handler classes are utility classes. This means that the handler classes are no longer webapp-based, and you cannot use the `blobstore_handlers` module provided by the webapp package (`google.appengine.ext.webapp`) or the `webapp2.RequestHandler` parameters in subclasses of these handlers.

  * All of the methods in Blobstore handler classes require the [WSGI `environ` dictionary](https://www.python.org/dev/peps/pep-0333/#environ-variables) as an input parameter.




The following sections show how to use `BlobstoreUploadHandler` and `BlobstoreDownloadHandler` classes for Python 3 in a Flask app and a WSGI app that does not use a Python framework.

## Example: Flask app

In Python 3, the Blobstore handler classes are part of module [`google.appengine.ext.blobstore`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore). For a Flask app, all calls made to methods in `BlobstoreUploadHandler` and `BlobstoreDownloadHandler` classes require the `request.environ` dictionary (`request` being imported from the `flask` module).

Compare the code changes made from Python 2 (webapp2) to Python 3 (Flask). Notice how the Flask app uses the `request.environ` parameter in the methods `get_uploads()` and `send_blob()`:

### Python 2 (webapp2)
    
    
    class PhotoUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
        def post(self):
            upload = self.get_uploads()[0]
            user_photo = UserPhoto(
                user=users.get_current_user().user_id(),
                blob_key=upload.key())
            user_photo.put()
    
            self.redirect('/view_photo/%s' % upload.key())
    
    class ViewPhotoHandler(blobstore_handlers.BlobstoreDownloadHandler):
        def get(self, photo_key):
            if not blobstore.get(photo_key):
                self.error(404)
            else:
                self.send_blob(photo_key)
    
    app = webapp2.WSGIApplication([
        ('/', PhotoUploadFormHandler),
        ('/upload_photo', PhotoUploadHandler),
        ('/view_photo/([^/]+)?', ViewPhotoHandler),
    ], debug=True)
    

### Python 3 (Flask)
    
    
    class PhotoUploadHandler(blobstore.BlobstoreUploadHandler):
        def post(self):
            upload = self.get_uploads(request.environ)[0]
            photo = PhotoUpload(blob_key=upload.key())
            photo.put()
    
            return redirect("/view_photo/%s" % upload.key())
    
    
    class ViewPhotoHandler(blobstore.BlobstoreDownloadHandler):
        def get(self, photo_key):
            if not blobstore.get(photo_key):
                return "Photo key not found", 404
            else:
                headers = self.send_blob(request.environ, photo_key)
    
                # Prevent Flask from setting a default content-type.
                # GAE sets it to a guessed type if the header is not set.
                headers["Content-Type"] = None
                return "", headers
    
    
    @app.route("/view_photo/<photo_key>")
    def view_photo(photo_key):
        """View photo given a key."""
        return ViewPhotoHandler().get(photo_key)
    
    
    @app.route("/upload_photo", methods=["POST"])
    def upload_photo():
        """Upload handler called by blobstore when a blob is uploaded in the test."""
        return PhotoUploadHandler().post()
    
    

To view the complete code sample for Python 3 (Flask), see [GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/appengine/standard_python3/bundled-services).

## Example: WSGI app without a web framework

The following Python 3 (WSGI app) code shows how to add the `environ` parameter when using Blobstore handler classes for a WSGI app without a web framework. Notice how the `environ` parameter is used in the `get_uploads()` and `send_blob()` methods, and compare it with the Python 2 version:

### Python 2
    
    
    class PhotoUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
        def post(self):
            upload = self.get_uploads()[0]
            user_photo = UserPhoto(
                user=users.get_current_user().user_id(),
                blob_key=upload.key())
            user_photo.put()
    
            self.redirect('/view_photo/%s' % upload.key())
    
    class ViewPhotoHandler(blobstore_handlers.BlobstoreDownloadHandler):
        def get(self, photo_key):
            if not blobstore.get(photo_key):
                self.error(404)
            else:
                self.send_blob(photo_key)
    
    app = webapp2.WSGIApplication([
        ('/', PhotoUploadFormHandler),
        ('/upload_photo', PhotoUploadHandler),
        ('/view_photo/([^/]+)?', ViewPhotoHandler),
    ], debug=True)
    

### Python 3
    
    
    class UploadPhotoHandler(blobstore.BlobstoreUploadHandler):
        """Upload handler called by blobstore when a blob is uploaded in the test."""
    
        def post(self, environ):
            upload = self.get_uploads(environ)[0]
            user_photo = UserPhoto(blob_key=upload.key())
            user_photo.put()
    
            # Redirect to the '/view_photo/<Photo Key>' URL
            return (
                "",
                http.HTTPStatus.FOUND,
                [("Location", "/view_photo/%s" % upload.key())],
            )
    
    
    class ViewPhotoHandler(blobstore.BlobstoreDownloadHandler):
        def get_photo(self, environ, photo_key):
            if not blobstore.get(photo_key):
                return "Photo key not found", http.HTTPStatus.NOT_FOUND, []
            else:
                return (
                    "",
                    http.HTTPStatus.OK,
                    list(self.send_blob(environ, photo_key).items()),
                )
    
        def get(self, environ):
            photo_key = (environ["app.url_args"])[0]
            return self.get_photo(environ, photo_key)
    
    
    # map urls to functions
    urls = [
        (r"^$", UploadFormHandler),
        (r"upload_photo/?$", UploadPhotoHandler),
        (r"view_photo/(.+)$", ViewPhotoHandler),
    ]

To view the complete code sample for Python 3, see [GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/appengine/standard_python3/bundled-services).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
