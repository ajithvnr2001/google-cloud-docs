---
url: https://docs.cloud.google.com/appengine/docs/flexible/serving-static-files/
title: Serving static files \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:12.049545+00:00
---

# Serving static files  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/serving-static-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Serving static files Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby .NET Custom

Applications often need to serve static files such as JavaScript, images, and CSS in addition to handling dynamic requests. Apps in the flexible environment can serve static files from a Google Cloud option like Cloud Storage, serve them directly, or use a third-party content delivery network (CDN).

## Serving files from Cloud Storage

[Cloud Storage](https://docs.cloud.google.com/storage) can host static assets for dynamic web apps. The benefits of using Cloud Storage instead of serving directly from your app include:

  * Cloud Storage essentially works as a [content delivery network](https://wikipedia.org/wiki/Content_delivery_network). This does not require any special configuration because by default any publicly readable object is cached in the global Cloud Storage network.
  * Your app's load will be reduced by offloading serving static assets to Cloud Storage. Depending on how many static assets you have and the frequency of access, this can reduce the cost of running your app by a significant amount.
  * Bandwidth charges for accessing content can often be less with Cloud Storage.



You can upload your assets to Cloud Storage by using the [Google Cloud CLI](https://docs.cloud.google.com/storage/docs/uploading-objects) or the [Cloud Storage API](https://docs.cloud.google.com/storage/docs).

The Google Cloud Client Library provides an idiomatic [client to Cloud Storage](https://docs.cloud.google.com/storage/docs/reference/libraries), for storing and retrieving data with Cloud Storage in an App Engine app.

### Example of serving from a Cloud Storage bucket

This example creates a Cloud Storage bucket and uploads static assets using the gcloud CLI:

  1. Create a bucket. It's common, but not required, to name your bucket after your project ID. The bucket name must be globally unique.
         
         gcloud storage buckets create gs://<var>your-bucket-name</var>
         

  2. Set the IAM policy to grant public read access to items in the bucket.
         
         gcloud storage buckets add-iam-policy-binding gs://<var>your-bucket-name</var> --member=allUsers --role=roles/storage.objectViewer
         

  3. Upload items to the bucket. The `rsync` command is typically the fastest and easiest way to upload and update assets. You could also use `cp`.
         
         gcloud storage rsync ./static gs://<var>your-bucket-name</var>/static --recursive
         




You can now access your static assets via `https://storage.googleapis.com/<var>your-bucket-name</var>/static/...`.

For more details on how to use Cloud Storage to serve static assets, including how to serve from a custom domain name, refer to [How to Host a Static Website](https://docs.cloud.google.com/storage/docs/website-configuration).

### Serving files from other Google Cloud services

You also have the option of using [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) or other Google Cloud storage services.

## Serving files directly from your app

Serving files from your app is typically straightforward, however, there are a couple drawbacks that you should consider:

  * Requests for static files can use resources that otherwise would be used for dynamic requests.
  * Depending on your configuration, serving files from your app can result in response latency, which can also affect when new instances are created for handling the load.

**Note:** In production environments, it's generally best practice to serve your static content separately from your app, either in Google Cloud or externally using a third-party CDN. 

### Example of serving static files with your app

### Go

The following sample demonstrates how to serve static files with your app. You can use the sample application in this guide for any [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#go) version of Go by specifying the runtime version and operating system in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime#newversions) file.

You can use the standard [`http.FileServer`](https://golang.org/pkg/net/http/#example_FileServer) or [`http.ServeFile`](https://golang.org/pkg/net/http/#ServeFile) to serve files directly from your app.
    
    
    // Package static demonstrates a static file handler for App Engine flexible environment.
    package main
    
    import (
    	"fmt"
    	"net/http"
    
    	"google.golang.org/appengine"
    )
    
    func main() {
    	// Serve static files from "static" directory.
    	http.Handle("/static/", http.FileServer(http.Dir(".")))
    
    	http.HandleFunc("/", homepageHandler)
    	appengine.[Main](https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/index.html#google_golang_org_appengine_v2_Main)()
    }
    
    const homepage = `<!doctype html>
    <html>
    <head>
      <title>Static Files</title>
      <link rel="stylesheet" type="text/css" href="/static/main.css">
    </head>
    <body>
      <p>This is a static file serving example.</p>
    </body>
    </html>`
    
    func homepageHandler(w http.ResponseWriter, r *http.Request) {
    	fmt.Fprint(w, homepage)
    }
    

### Java

The following sample demonstrates how to serve static files with your app. You can use the sample application in this guide for any [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#java) version of Java by specifying the runtime version and operating system in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/java/runtime#newversions) file.

The Java runtime's servlet container will use your app's [deployment descriptor](https://docs.cloud.google.com/appengine/docs/flexible/java/configuring-the-web-xml-deployment-descriptor), `web.xml` file, to map URLs to servlets, including static assets. If you don't specify a `web.xml`, a default is used that maps everything to the default servlet.

In this example, `./src/main/webapp/index.html` refers to a style sheet served from `/stylesheets/styles.css`.
    
    
    <!doctype html>
    <html>
    <head>
    <title>Static Files</title>
    <link rel="stylesheet" type="text/css" href="/stylesheets/styles.css">
    </head>
    <body>
      <p>This is a static file serving example.</p>
    </body>
    </html>

The `styles.css` file is located at `./src/main/webapp/stylesheets/styles.css`.
    
    
    body {
      font-family: Verdana, Helvetica, sans-serif;
      background-color: #CCCCFF;
    }
    

You can explicitly configure how static files are handled in the `web.xml` file. For example, if you wanted to map requests for all files that have the `.jpg` extension:
    
    
    <servlet-mapping>
        <servlet-name>default</servlet-name>
        <url-pattern>*.jpg</url-pattern>
    </servlet-mapping>
    

If you are using a web framework, such as [Play](https://www.playframework.com/documentation/2.0/Assets), you will need to refer to the framework's documentation on static assets.

### Node.js

The following sample demonstrates how to serve static files with your app. You can use the sample application in this guide for any [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#nodejs) version of Node.js by specifying the runtime version and operating system in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/runtime#newversions) file.

Most web frameworks include support for serving static files. In this sample, the application uses the [`express.static`](http://expressjs.com/starter/static-files.html) middleware to serve files from the `./public` directory to the `/static` URL.
    
    
    'use strict';
    
    const express = require('express');
    const app = express();
    
    app.set('view engine', 'pug');
    
    // Use the built-in express middleware for serving static files from './public'
    app.use('/static', express.static('public'));
    
    app.get('/', (req, res) => {
      res.render('index');
    });
    
    // Start the server
    const PORT = parseInt(process.env.PORT) || 8080;
    app.listen(PORT, () => {
      console.log(`App listening on port ${PORT}`);
      console.log('Press Ctrl+C to quit.');
    });
    

The view refers to `/static/main.css`.
    
    
    doctype html
    html(lang="en")
      head
        title Static Files
        meta(charset='utf-8')
        link(rel="stylesheet", href="/static/main.css")
      body
        p This is a static file serving example.
    

The style sheet itself is located at `./public/css`, which is served from `/static/main.css`.
    
    
    body {
      font-family: Verdana, Helvetica, sans-serif;
      background-color: #CCCCFF;
    }

Other Node.js frameworks, such as [Hapi](http://hapijs.com/tutorials/serving-files), [Koa](https://github.com/koajs/static), and [Sails](http://sailsjs.org/documentation/concepts/assets) typically support serving static files directly from the application. Refer to their documentation for details on how to configure and use static content.

### PHP

The PHP runtime runs [nginx](http://nginx.org/) to serve your app, which is configured to serve static files in your project directory. You must declare the document root by specifying `document_root` in your `app.yaml` file. You can use the sample application in this guide for any [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#php) version of PHP by specifying the runtime version and operating system in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/php/runtime#newversions) file.
    
    
    runtime: php
    env: flex
    
    runtime_config:
      document_root: web
      operating_system: ubuntu22
      runtime_version: 8.3
    
    build_env_variables:
      NGINX_SERVES_STATIC_FILES: true
    

### Python

The following sample demonstrates how to serve static files with your app. You can use the sample application in this guide for any [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#python) version of Python by specifying the runtime version and operating system in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime#newversions) file.

Most web frameworks include support for serving static files. In this sample, the app uses [Flask's built-in ability](http://flask.pocoo.org/docs/quickstart/#static-files) to serve files in `./static` directory from the `/static` URL.

The app includes a view that renders the template. Flask automatically serves everything in the `./static` directory without additional configuration.
    
    
    import logging
    
    from flask import Flask, render_template
    
    
    app = Flask(__name__)
    
    
    @app.route("/")
    def hello():
        """Renders and serves a static HTML template page.
    
        Returns:
            A string containing the rendered HTML page.
        """
        return render_template("index.html")
    
    
    @app.errorhandler(500)
    def server_error(e):
        """Serves a formatted message on-error.
    
        Returns:
            The error message and a code 500 status.
        """
        logging.exception("An error occurred during a request.")
        return (
            f"An internal error occurred: <pre>{e}</pre><br>See logs for full stacktrace.",
            500,
        )
    
    
    if __name__ == "__main__":
        # This is used when running locally. Gunicorn is used to run the
        # application on Google App Engine. See entrypoint in app.yaml.
        app.run(host="127.0.0.1", port=8080, debug=True)

The template rendered by the view includes a style sheet located at `/static/main.css`.
    
    
    <!doctype html>
    <html>
    <head>
      <title>Static Files</title>
      <!--
      Flask automatically makes files in the 'static' directory available via
      '/static'.
      -->
      <link rel="stylesheet" type="text/css" href="/static/main.css">
    </head>
    <body>
      <p>This is a static file serving example.</p>
    </body>
    </html>
    

The style sheet is located at `./static/main.css`.
    
    
    body {
      font-family: Verdana, Helvetica, sans-serif;
      background-color: #CCCCFF;
    }

Other Python frameworks, such as [Django](https://docs.djangoproject.com/en/4.1/howto/static-files/deployment/), [Pyramid](http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/assets.html), and [Bottle](http://bottlepy.org/docs/dev/tutorial.html#routing-static-files) typically support serving static files directly from the app. Refer to their documentation for details on how to configure and use static content.

### Ruby

Most web frameworks include support for serving static files. The following sample demonstrates how to serve static files with your app. You can use the sample application in this guide for any [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#ruby) version of Ruby by specifying the runtime version and operating system in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/ruby/runtime#newversions) file.

### Sinatra

The [Sinatra](http://www.sinatrarb.com/) web framework serves files from the `./public` directory by default. This app includes a view that refers to `/application.css`.
    
    
    body {
      font-family: Verdana, Helvetica, sans-serif;
      background-color: #CCCCFF;
    }

The style sheet is located at `./public/application.css` which is served from `/application.css`.

### Ruby on Rails

The [Ruby on Rails](http://rubyonrails.org/) web framework serves files from the `./public` directory by default. Static JavaScript and CSS files can also be generated by the Rails [asset pipeline](http://guides.rubyonrails.org/asset_pipeline.html).

These example apps contain a layout view that include all the application style sheets.
    
    
    doctype html
    html
      head
        title Serving Static Files
        link rel="stylesheet" href="/application.css"
        script src="/application.js"
      body
        p This is a static file serving example.

The style sheet itself is a `.css` file located at `./public/application.css`.
    
    
    body {
      font-family: Verdana, Helvetica, sans-serif;
      background-color: #CCCCFF;
    }

By default, Rails apps don't generate or serve static assets when running in production.

The [Ruby runtime](https://docs.cloud.google.com/appengine/docs/flexible/ruby/runtime) executes `rake assets:precompile` during deployment to generate static assets and sets the `RAILS_SERVE_STATIC_FILES` environment variable to enable static file serving in production.

### .NET

The following sample demonstrates how to serve static files with your app. You can use the sample application in this guide for any [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#net) version of .NET by specifying the runtime version and operating system in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/runtime#newversions) file.
    
    
    <html>
    <head>
        <meta charset="utf-8" />
        <title>Hello Static World</title>
    </head>
    <body>
        <p>This is a static html document.</p>
        <p><img src="trees.jpg" /></p>
    </body>
    </html>
    

To enable static file serving, add:
    
    
    app.UseDefaultFiles();
    app.UseStaticFiles();
    

## Serving from a third-party content delivery network

You can use any external third-party CDN to serve your static files and cache dynamic requests but your app might experience increased latency and cost.

For improved performance, you should use a third-party CDN that supports [CDN Interconnect](https://docs.cloud.google.com/network-connectivity/docs/cdn-interconnect).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
