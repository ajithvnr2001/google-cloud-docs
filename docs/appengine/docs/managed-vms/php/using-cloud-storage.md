---
url: https://docs.cloud.google.com/appengine/docs/managed-vms/php/using-cloud-storage/
title: Use Cloud Storage \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:26.533629+00:00
---

# Use Cloud Storage  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/managed-vms/php/using-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Use Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Cloud Storage](https://docs.cloud.google.com/storage/docs) to store and serve files, such as movies or images or other static content.

This document describes how to use the [Cloud Client Libraries for Cloud Storage](https://docs.cloud.google.com/storage/docs/reference/libraries) in your app to store data and retrieve data from Cloud Storage. You can use the sample application in this guide for any [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#python) version of Python by specifying the runtime version and operating system in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime#newversions) file. 

## Before you begin

  * Follow the instructions in [Setting up your development environment](https://docs.cloud.google.com/appengine/docs/flexible/setting-up-environment) to set up your environment and project, and to understand how apps are structured in App Engine. Write down and save your project ID, because you will need it to run the sample application described in this document.
  * Make sure you create a Cloud Storage bucket for your application by invoking the following command:
        
        gcloud storage buckets create gs://YOUR_BUCKET_NAME
        

  * Make the bucket [publicly readable](https://docs.cloud.google.com/storage/docs/access-control#using_permissions_with_acls) so it can serve files:
        
        gcloud storage buckets add-iam-policy-binding gs://<var>YOUR_BUCKET_NAME</var> --member=allUsers --role=roles/storage.objectViewer
        




## Download the sample

### Go

To clone the repository:
    
    
    git clone https://github.com/GoogleCloudPlatform/golang-samples.git
    cd golang-samples/appengine_flexible/storage
    

### Java

To clone the repository:
    
    
    git clone https://github.com/GoogleCloudPlatform/java-docs-samples
    cd java-docs-samples/flexible/java-17/cloudstorage
    

### Node.js

To clone the repository:
    
    
    git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples/
    cd nodejs-docs-samples/appengine/storage/flexible
    

### PHP

To clone the repository:
    
    
    git clone https://github.com/GoogleCloudPlatform/php-docs-samples
    cd php-docs-samples/appengine/flexible/storage
    

### Python

To clone the repository:
    
    
    git clone https://github.com/GoogleCloudPlatform/python-docs-samples
    cd python-docs-samples/appengine/flexible/storage
    

### Ruby

To clone the repository:
    
    
    git clone https://github.com/GoogleCloudPlatform/ruby-docs-samples
    cd ruby-docs-samples/appengine/flexible/storage/
    

### .NET

  1. [Download the sample app](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/archive/master.zip) and extract it.

  2. If you're using the command line, navigate into the following app directory:
         
         dotnet-docs-samples\appengine\flexible\CloudStorage\CloudStorage.Sample
         




To run your application locally, set up a [service account](https://docs.cloud.google.com/iam/docs/service-accounts) and download credentials:

  1. Open the list of credentials in the Google Cloud console.

[Open the list of credentials](https://console.cloud.google.com/project/_/apiui/credential)

  2. Click **Create credentials**.

  3. Select **Service account key**.

A _Create service account key_ window opens.

  4. Click the _Service account_ list, and select **Compute Engine default service account**.

  5. Select **JSON** for the **Key type**.

  6. Click **Create**.

A **New private key** window is displayed and the private key for the is downloaded automatically.

  7. Click **Close**.

**Note:** When you create the service account, choose **Compute Engine default service account** and leave **JSON** selected under **Key Type**.



## Edit project configuration and install dependencies

### Go

In `app.yaml`, set `GCLOUD_STORAGE_BUCKET`. This value is the name of the Cloud Storage bucket you created previously.
    
    
    # Copyright 2019 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    runtime: go
    env: flex
    
    runtime_config:
      operating_system: ubuntu22
      runtime_version: 1.21
    
    automatic_scaling:
      min_num_instances: 1
    
    env_variables:
      GCLOUD_STORAGE_BUCKET: your-bucket-name
    

### Java

In `app.yaml`, set the `BUCKET_NAME` to the Cloud Storage you previously created for your project.
    
    
    runtime: java
    env: flex
    runtime_config:
      operating_system: ubuntu22
      runtime_version: 17
    handlers:
    - url: /.*
      script: this field is required, but ignored
    
    env_variables:
      BUCKET_NAME: YOUR-BUCKET-NAME

In `pom.xml`, set `com.google.cloud` as a dependency, and specify `google-cloud-storage` as the artifactID for that dependency; this provides the functions to use Cloud Storage.
    
    
    <!--  Using libraries-bom to manage versions.
    See https://github.com/GoogleCloudPlatform/cloud-opensource-java/wiki/The-Google-Cloud-Platform-Libraries-BOM -->
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.45.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
        <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-dependencies</artifactId>
          <version>${spring.boot.version}</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
      </dependency>
      <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
      </dependency>
      <dependency>
        <groupId>javax.servlet</groupId>
        <artifactId>javax.servlet-api</artifactId>
        <type>jar</type>
        <scope>provided</scope>
      </dependency>
      <dependency>
        <groupId>org.junit.vintage</groupId>
        <artifactId>junit-vintage-engine</artifactId>
        <scope>test</scope>
      </dependency>
      <dependency>
        <groupId>org.junit-pioneer</groupId>
        <artifactId>junit-pioneer</artifactId>
        <version>2.2.0</version>
        <scope>test</scope>
      </dependency>
      <dependency>
          <groupId>org.mockito</groupId>
          <artifactId>mockito-junit-jupiter</artifactId>
          <scope>test</scope>
      </dependency>
      <dependency>
          <groupId>org.mockito</groupId>
          <artifactId>mockito-inline</artifactId>
          <scope>test</scope>
      </dependency>   
      <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
      </dependency>
      <dependency>
          <groupId>net.bytebuddy</groupId>
          <artifactId>byte-buddy</artifactId>
          <version>1.14.17</version>
      </dependency>
    </dependencies>

### Node.js

In `app.yaml`, add your project ID to the `GOOGLE_CLOUD_PROJECT` environment value. Then set the `GCLOUD_STORAGE_BUCKET` environment value to the name of the Cloud Storage bucket you created previously.
    
    
    runtime: nodejs
    env: flex
    runtime_config:
      operating_system: ubuntu22
    
    env_variables:
      GCLOUD_STORAGE_BUCKET: YOUR_BUCKET_NAME

In `package.json`, add `@google-cloud/storage` as a dependency, which provides the functions to use Cloud Storage.
    
    
    {
      "name": "appengine-storage",
      "description": "Node.js Google Cloud Storage sample for Google App Engine",
      "scripts": {
        "start": "node app.js",
        "test": "c8 mocha -p -j 2 system-test/*.test.js --exit --timeout=30000"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "dependencies": {
        "@google-cloud/storage": "^8.0.0",
        "express": "^5.0.0",
        "multer": "^2.1.1",
        "pug": "^3.0.2"
      },
      "devDependencies": {
        "@types/express": "^5.0.0",
        "@types/multer": "^2.0.0",
        "@types/proxyquire": "^1.3.28",
        "@types/supertest": "^7.0.0",
        "@types/uuid": "^11.0.0",
        "c8": "^12.0.0",
        "mocha": "^10.2.0",
        "proxyquire": "^2.1.3",
        "supertest": "^7.0.0",
        "uuid": "^11.1.1"
      }
    }
    

See the [`README.md` file](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/master/appengine/storage/flexible/README.md) for instructions on running and testing locally.

### PHP

In `app.yaml`, set `CLOUD_STORAGE_BUCKET`; this value is the name of the Cloud Storage bucket you created previously.
    
    
    env_variables:
      GOOGLE_STORAGE_BUCKET: "your-bucket-name"

In `composer.json`, notice that you must include the Cloud Client library, because this provides Cloud Storage functions.
    
    
    {
        "require": {
            "slim/slim": "^4.0",
            "slim/psr7": "^1.3",
            "google/cloud-storage": "^1.0",
            "php-di/slim-bridge": "^3.1"
        }
    }
    

### Python

In `app.yaml`, set `GOOGLE_STORAGE_BUCKET`; this value is the name of the Cloud Storage bucket you created previously.
    
    
    env_variables:
      CLOUD_STORAGE_BUCKET: [your-bucket-name]

In `requirements.txt`, notice that you must include the `google-cloud-storage` library, because this provides Cloud Storage functions.
    
    
    Flask==3.1.3; python_version >= '3.9'
    google-cloud-storage==2.9.0
    gunicorn==23.0.0
    

### Ruby

In `app.yaml`, set the `GCLOUD_STORAGE_BUCKET` to the Cloud Storage you previously created for your project.
    
    
    runtime: ruby
    env: flex
    entrypoint: bundle exec ruby app.rb
    
    runtime_config:
      operating_system: ubuntu22
    
    env_variables:
      GOOGLE_CLOUD_STORAGE_BUCKET: <your-bucket-name>

Note that you must include the `gcloud` library in `Gemfile` to use Cloud Storage functions.
    
    
    source "https://rubygems.org"
    
    gem "google-cloud-storage"
    gem "sinatra"

### .NET

In `app.yaml` file , set the `TEST_GOOGLE_BUCKET_NAME` to the Cloud Storage you previously created for your project.
    
    
    env_variables:
      TEST_GOOGLE_BUCKET_NAME: [your-bucket-name]
    

## Application code

### Go

The sample application presents a web page prompting the user to supply a file to be stored in Cloud Storage. When the user selects a file and clicks submit, the upload handler writes the file to the Cloud Storage bucket using Cloud Storage [NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest#cloud_google_com_go_storage_ObjectHandle_NewWriter) function.

Notice that to retrieve this file from Cloud Storage, you will need to specify the bucket name and the filename. You should store these values in your app for future use.
    
    
    // Copyright 2019 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    
    // Sample storage demonstrates use of the cloud.google.com/go/storage package from App Engine flexible environment.
    package main
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"[log](https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/log.html)"
    	"net/http"
    	"net/url"
    	"os"
    
    	"cloud.google.com/go/storage"
    	"google.golang.org/appengine"
    )
    
    var (
    	storageClient *storage.Client
    
    	// Set this in app.yaml when running in production.
    	bucket = os.Getenv("GCLOUD_STORAGE_BUCKET")
    )
    
    func main() {
    	ctx := context.Background()
    
    	var err error
    	storageClient, err = storage.NewClient(ctx)
    	if err != nil {
    		log.Fatal(err)
    	}
    
    	http.HandleFunc("/", formHandler)
    	http.HandleFunc("/upload", uploadHandler)
    
    	appengine.[Main](https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/index.html#google_golang_org_appengine_v2_Main)()
    }
    
    func uploadHandler(w http.ResponseWriter, r *http.Request) {
    	if r.Method != "POST" {
    		http.Error(w, "", http.StatusMethodNotAllowed)
    		return
    	}
    
    	ctx := appengine.NewContext(r)
    
    	f, fh, err := r.FormFile("file")
    	if err != nil {
    		msg := fmt.Sprintf("Could not get file: %v", err)
    		http.Error(w, msg, http.StatusBadRequest)
    		return
    	}
    	defer f.Close()
    
    	sw := storageClient.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(fh.Filename).[NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter)(ctx)
    	if _, err := io.Copy(sw, f); err != nil {
    		msg := fmt.Sprintf("Could not write file: %v", err)
    		http.Error(w, msg, http.StatusInternalServerError)
    		return
    	}
    
    	if err := sw.Close(); err != nil {
    		msg := fmt.Sprintf("Could not put file: %v", err)
    		http.Error(w, msg, http.StatusInternalServerError)
    		return
    	}
    
    	u, _ := url.Parse("/" + bucket + "/" + sw.Attrs().Name)
    
    	fmt.Fprintf(w, "Successful! URL: https://storage.googleapis.com%s", u.EscapedPath())
    }
    
    func formHandler(w http.ResponseWriter, r *http.Request) {
    	fmt.Fprint(w, formHTML)
    }
    
    const formHTML = `<!DOCTYPE html>
    <html>
      <head>
        <title>Storage</title>
        <meta charset="utf-8">
      </head>
      <body>
        <form method="POST" action="/upload" enctype="multipart/form-data">
          <input type="file" name="file">
          <input type="submit">
        </form>
      </body>
    </html>`
    
    

### Java

The sample application presents a web page prompting the user to supply a file to be stored in Cloud Storage. When the user selects a file and clicks submit, the `doPost` request handler writes the file to the Cloud Storage bucket using [Storage.create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage)

Notice that to retrieve this file from Cloud Storage, you will need to specify the bucket name and the filename. You should store these values in your app for future use.
    
    
    @SuppressWarnings("serial")
    @WebServlet(name = "upload", value = "/upload")
    @MultipartConfig()
    public class UploadServlet extends HttpServlet {
    
      private static final String BUCKET_NAME =
          System.getenv().getOrDefault("BUCKET_NAME", "my-test-bucket");
      private static Storage storage = null;
    
      public UploadServlet() {
        storage = StorageOptions.getDefaultInstance().getService();
      }
    
      @Override
      public void doPost(HttpServletRequest req, HttpServletResponse resp)
          throws IOException, ServletException {
        final Part filePart = req.getPart("file");
        final String fileName = filePart.getSubmittedFileName();
        // Modify access list to allow all users with link to read file
        List<Acl> acls = new ArrayList<>();
        acls.add(Acl.of(Acl.User.ofAllUsers(), Acl.Role.READER));
        // the inputstream is closed by default, so we don't need to close it here
        Blob blob =
            storage.create(
                BlobInfo.newBuilder(BUCKET_NAME, fileName).setAcl(acls).build(),
                filePart.getInputStream());
    
        // return the public download link
        resp.getWriter().print(blob.getMediaLink());
      }
    }

### Node.js

The sample application presents a web page prompting the user to supply a file to be stored in Cloud Storage. When the user selects a file and clicks submit, the upload handler loads the file content into a blob and writes it to Cloud Storage.

Notice that after the file is uploaded to Cloud Storage, the public URL to this file is returned, which you can use to serve the file directly from Cloud Storage. You should store this value in your app for future use.
    
    
    const {format} = require('util');
    const express = require('express');
    const Multer = require('multer');
    
    // By default, the client will authenticate using the service account file
    // specified by the GOOGLE_APPLICATION_CREDENTIALS environment variable and use
    // the project specified by the GOOGLE_CLOUD_PROJECT environment variable. See
    // https://github.com/GoogleCloudPlatform/google-cloud-node/blob/master/docs/authentication.md
    // These environment variables are set automatically on Google App Engine
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Instantiate a storage client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    const app = express();
    app.set('view engine', 'pug');
    
    // This middleware is available in Express v4.16.0 onwards
    app.use(express.json());
    
    // Multer is required to process file uploads and make them available via
    // req.files.
    const multer = Multer({
      storage: Multer.memoryStorage(),
      limits: {
        fileSize: 5 * 1024 * 1024, // no larger than 5mb, you can change as needed.
      },
    });
    
    // A bucket is a container for objects (files).
    const bucket = storage.bucket(process.env.GCLOUD_STORAGE_BUCKET);
    
    // Display a form for uploading files.
    app.get('/', (req, res) => {
      res.render('form.pug');
    });
    
    // Process the file upload and upload to Google Cloud Storage.
    app.post('/upload', multer.single('file'), (req, res, next) => {
      if (!req.file) {
        res.status(400).send('No file uploaded.');
        return;
      }
    
      // Create a new blob in the bucket and upload the file data.
      const blob = bucket.file(req.file.originalname);
      const blobStream = blob.createWriteStream();
    
      blobStream.on('error', err => {
        next(err);
      });
    
      blobStream.on('finish', () => {
        // The public URL can be used to directly access the file via HTTP.
        const publicUrl = format(
          `https://storage.googleapis.com/${bucket.name}/${blob.name}`
        );
        res.status(200).send(publicUrl);
      });
    
      blobStream.end(req.file.buffer);
    });
    
    const PORT = parseInt(process.env.PORT) || 8080;
    app.listen(PORT, () => {
      console.log(`App listening on port ${PORT}`);
      console.log('Press Ctrl+C to quit.');
    });

### PHP

The sample application presents a web page prompting the user to supply a file to be stored in Cloud Storage. When the user selects a file and clicks submit, the upload handler loads the file content into a blob and writes it to Cloud Storage.

Notice that after the file is uploaded to Cloud Storage, the public URL to this file is returned, which you can use to serve the file directly from Cloud Storage. You should store this value in your app for future use.
    
    
    use DI\Container;
    use Google\Cloud\Storage\StorageClient;
    use Psr\Http\Message\ServerRequestInterface as Request;
    use Psr\Http\Message\ResponseInterface as Response;
    use Slim\Factory\AppFactory;
    
    // Create App
    AppFactory::setContainer($container = new Container());
    $app = AppFactory::create();
    
    // Display errors
    $app->addErrorMiddleware(true, true, true);
    
    $container = $app->getContainer();
    
    $app->get('/', function (Request $request, Response $response) use ($container) {
        /** @var Google\Cloud\StorageClient */
        $storage = $container->get('storage');
        $bucketName = $container->get('bucket_name');
        $objectName = $container->get('object_name');
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $content = $object->exists() ? $object->downloadAsString() : '';
        $escapedContent = htmlspecialchars($content);
        $response->getBody()->write(<<<EOF
        <h1>Storage Example</h1>
        <h3>Write [<a href="https://cloud.google.com/appengine/docs/flexible/php/using-cloud-storage">docs</a>]:</h3>
        <form action="/write" method="post">
            Some file content:<br />
            <textarea name="content"></textarea><br />
            <input type="submit" />
        </form>
    EOF
        );
        if ($content) {
            $response->getBody()->write(
                "<p><strong>Your content:</strong><p><p>$escapedContent</p>"
            );
        }
        return $response;
    });
    
    /**
     * Write to a Storage bucket.
     * @see https://cloud.google.com/appengine/docs/flexible/php/using-cloud-storage
     */
    $app->post('/write', function (Request $request, Response $response) use ($container) {
        /** @var Google\Cloud\StorageClient */
        $storage = $container->get('storage');
        $bucketName = $container->get('bucket_name');
        $objectName = $container->get('object_name');
        parse_str((string) $request->getBody(), $postData);
        $metadata = ['contentType' => 'text/plain'];
        $storage->bucket($bucketName)->upload($postData['content'] ?? '', [
            'name' => $objectName,
            'metadata' => $metadata,
        ]);
        return $response
            ->withStatus(302)
            ->withHeader('Location', '/');
    });
    
    $container->set('storage', function () use ($container) {
        $projectId = $container->get('project_id');
        $storage = new StorageClient([
            'projectId' => $projectId
        ]);
        return $storage;
    });

### Python

The sample application presents a web page prompting the user to supply a file to be stored in Cloud Storage. When the user selects a file and clicks submit, the upload handler loads the file content into a Cloud Storage [blob](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob) and writes it to the Cloud Storage [bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket).

Notice that after the file is uploaded to Cloud Storage, the public URL to this file is returned, which you can use to serve the file directly from Cloud Storage. You should store this value in your app for future use.
    
    
    from __future__ import annotations
    
    import logging
    import os
    
    from flask import Flask, request
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    app = Flask(__name__)
    
    # Configure this environment variable via app.yaml
    CLOUD_STORAGE_BUCKET = os.environ["CLOUD_STORAGE_BUCKET"]
    
    
    @app.route("/")
    def index() -> str:
        return """
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit">
    </form>
    """
    
    
    @app.route("/upload", methods=["POST"])
    def upload() -> str:
        """Process the uploaded file and upload it to Google Cloud Storage."""
        uploaded_file = request.files.get("file")
    
        if not uploaded_file:
            return "No file uploaded.", 400
    
        # Create a Cloud Storage client.
        gcs = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        # Get the bucket that the file will be uploaded to.
        bucket = gcs.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(CLOUD_STORAGE_BUCKET)
    
        # Create a new blob and upload the file's content.
        blob = bucket.blob(uploaded_file.filename)
    
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
            uploaded_file.read(), content_type=uploaded_file.[content_type](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_content_type)
        )
    
        # Make the blob public. This is not necessary if the
        # entire bucket is public.
        # See https://cloud.google.com/storage/docs/access-control/making-data-public.
        blob.make_public()
    
        # The public URL can be used to directly access the uploaded file via HTTP.
        return blob.[public_url](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_public_url)
    
    
    @app.errorhandler(500)
    def server_error(e: Exception | int) -> str:
        logging.exception("An error occurred during a request.")
        return (
            """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(
                e
            ),
            500,
        )
    
    
    if __name__ == "__main__":
        # This is used when running locally. Gunicorn is used to run the
        # application on Google App Engine. See entrypoint in app.yaml.
        app.run(host="127.0.0.1", port=8080, debug=True)

### Ruby

The sample application presents a web page prompting the user to supply a file to be stored in Cloud Storage. When the user selects a file and clicks submit, the upload handler loads the file content into a blob and writes it to Cloud Storage.

Notice that after the file is uploaded to Cloud Storage, the public URL to this file is returned, which you can use to serve the file directly from Cloud Storage. You should store this value in your app for future use.
    
    
    require "sinatra"
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    bucket  = storage.bucket ENV["GOOGLE_CLOUD_STORAGE_BUCKET"]
    
    get "/" do
      # Present the user with an upload form
      '
        <form method="POST" action="/upload" enctype="multipart/form-data">
          <input type="file" name="file">
          <input type="submit" value="Upload">
        </form>
      '
    end
    
    post "/upload" do
      file_path = params[:file][:tempfile].path
      file_name = params[:file][:filename]
    
      # Upload file to Google Cloud Storage bucket
      file = bucket.create_file file_path, file_name, acl: "public"
    
      # The public URL can be used to directly access the uploaded file via HTTP
      file.public_url
    end

### .NET

The sample application presents a web page prompting the user to supply a file to be stored in Cloud Storage. When the user selects a file and clicks submit, the upload handler loads the file content into a blob and writes it to Cloud Storage.

Notice that after the file is uploaded to Cloud Storage, the public URL to this file is returned, which you can use to serve the file directly from Cloud Storage. You should store this value in your app for future use.
    
    
    public class HomeController : Controller
    {
        // Contains the bucket name and object name
        readonly CloudStorageOptions _options;
        // The Google Cloud Storage client.
        readonly StorageClient _storage;
    
        public HomeController(CloudStorageOptions options)
        {
            _options = options;
            _storage = StorageClient.Create();
        }
    
        [HttpGet]
        public async Task<IActionResult> Index()
        {
            var model = new HomeIndex();
            if (new string[] { null, "", "your-google-bucket-name" }
                .Contains(_options.BucketName))
            {
                model.MissingBucketName = true;
                return View(model);
            }
            try
            {
                // Get the storage object.
                var storageObject =
                    await _storage.GetObjectAsync(_options.BucketName, _options.ObjectName);
                // Get a direct link to the storage object.
                model.MediaLink = storageObject.MediaLink;
                // Download the storage object.
                MemoryStream m = new MemoryStream();
                await _storage.DownloadObjectAsync(
                    _options.BucketName, _options.ObjectName, m);
                m.Seek(0, SeekOrigin.Begin);
                byte[] content = new byte[m.Length];
                m.Read(content, 0, content.Length);
                model.Content = Encoding.UTF8.GetString(content);
            }
            catch (GoogleApiException e)
            when (e.HttpStatusCode == System.Net.HttpStatusCode.NotFound)
            {
                // Does not exist yet.  No problem.
            }
            return View(model);
        }
    
        [HttpPost]
        public async Task<IActionResult> Index(Form sendForm)
        {
            var model = new HomeIndex();
            // Take the content uploaded in the form and upload it to
            // Google Cloud Storage.
            await _storage.UploadObjectAsync(
                _options.BucketName, _options.ObjectName, "text/plain",
                new MemoryStream(Encoding.UTF8.GetBytes(sendForm.Content)));
            model.Content = sendForm.Content;
            model.SavedNewContent = true;
            var storageObject =
                await _storage.GetObjectAsync(_options.BucketName, _options.ObjectName);
            model.MediaLink = storageObject.MediaLink;
            return View(model);
        }
    

## For more information

For complete information on Cloud Storage, see the [Cloud Storage documentation](https://docs.cloud.google.com/storage/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
