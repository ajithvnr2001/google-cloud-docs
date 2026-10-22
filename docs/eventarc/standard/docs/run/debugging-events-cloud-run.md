---
url: https://docs.cloud.google.com/eventarc/standard/docs/run/debugging-events-cloud-run/
title: Tutorial: Debug routing events to Cloud Run \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:48.253220+00:00
---

# Tutorial: Debug routing events to Cloud Run  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/run/debugging-events-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Tutorial: Debug routing events to Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This tutorial teaches you how to troubleshoot runtime errors encountered when you use Eventarc to route events from Cloud Storage to an _unauthenticated_ Cloud Run service using Cloud Audit Logs.

**Note:** All Cloud Run services are deployed privately by default, which means that they can't be accessed without providing authentication credentials in the request. For projects with [ domain restricted sharing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), use an authenticated Cloud Run target service rather than one that allows [public access](https://docs.cloud.google.com/run/docs/authenticating/public). 

## Objectives

This tutorial shows you how to complete the following tasks:

  1. Create an Artifact Registry standard repository to store your container image.
  2. Create a Cloud Storage bucket to be the event source.
  3. Build, upload, and deploy a container image to Cloud Run.
  4. Create Eventarc triggers.
  5. Upload a file to the Cloud Storage bucket.
  6. Troubleshoot and fix the runtime errors.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Build](https://docs.cloud.google.com/build)
  * [Cloud Logging](https://docs.cloud.google.com/logging)
  * [Cloud Run](https://docs.cloud.google.com/run)
  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Pub/Sub](https://docs.cloud.google.com/pubsub)
  * [Eventarc](https://docs.cloud.google.com/eventarc)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Artifact Registry, Cloud Build, Cloud Logging, Cloud Run, Cloud Storage, Eventarc, and Pub/Sub APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com eventarc.googleapis.com logging.googleapis.com pubsub.googleapis.com run.googleapis.com storage.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Artifact Registry, Cloud Build, Cloud Logging, Cloud Run, Cloud Storage, Eventarc, and Pub/Sub APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com eventarc.googleapis.com logging.googleapis.com pubsub.googleapis.com run.googleapis.com storage.googleapis.com

  14. If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this Identity and Access Management (IAM) role includes the permissions necessary for full access to most Google Cloud resources and you can skip this step.

If you are not the project creator, required permissions must be granted on the project to the appropriate _principal_. For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads). For more information, see the [Roles and permissions](https://docs.cloud.google.com/eventarc/docs/all-roles-permissions) page for your event destination.

Note that by default, [Cloud Build permissions include permissions to upload and download Artifact Registry artifacts](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp).

#### Required permissions

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

     * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
     * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
     * [Eventarc Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
     * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  15. For Cloud Storage, enable audit logging for the `ADMIN_READ`, `DATA_WRITE`, and `DATA_READ` data access types. 

     1. Read the Identity and Access Management (IAM) policy associated with your Google Cloud project, folder, or organization and store it in a temporary file: 
            
            gcloud projects get-iam-policy PROJECT_ID > /tmp/policy.yaml

     2. In a text editor, open `/tmp/policy.yaml`, and add or change _only_ the audit log configuration in the `auditConfigs` section: **Caution:** You must preserve the `bindings:` and `etag:` sections without changes. Changing parts of your policy not related to audit logging might make your Google Cloud project inaccessible.
            
            **auditConfigs :
            - auditLogConfigs:
              - logType: ADMIN_READ
              - logType: DATA_WRITE
              - logType: DATA_READ
              service: storage.googleapis.com**
            bindings:
            - members:
            [...]
            etag: BwW_bHKTV5U=
            version: 1

     3. Write your new IAM policy: 
            
            gcloud projects set-iam-policy PROJECT_ID /tmp/policy.yaml

If the preceding command reports a conflict with another change, then repeat these steps, starting with reading the IAM policy. For more information, see [Configure Data Access audit logs with the API](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-api). 

  16. Grant the `eventarc.eventReceiver` role to the Compute Engine service account: 
         
         export PROJECT_NUMBER="$(gcloud projects describe $(gcloud config get-value project) --format='value(projectNumber)')"
         
         gcloud projects add-iam-policy-binding $(gcloud config get-value project) \
             --member=serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com \
             --role='roles/eventarc.eventReceiver'

  17. If you enabled the Pub/Sub service account on or before April 8, 2021, grant the `iam.serviceAccountTokenCreator` role to the Pub/Sub service account: 
         
         gcloud projects add-iam-policy-binding $(gcloud config get-value project) \
             --member="serviceAccount:service-${PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com"\
             --role='roles/iam.serviceAccountTokenCreator'

  18. Set the defaults used in this tutorial: 
         
         export REGION=us-central1
         gcloud config set run/region ${REGION}
         gcloud config set run/platform managed
         gcloud config set eventarc/location ${REGION}




## Create an Artifact Registry standard repository

Create an Artifact Registry standard repository to store your container image:
    
    
    gcloud artifacts repositories create REPOSITORY \
        --repository-format=docker \
        --location=$REGION

Replace `REPOSITORY` with a unique name for the repository.

## Create a Cloud Storage bucket

Create a Cloud Storage bucket in each of two regions as the event source for the Cloud Run service:

  1. Create a bucket in `us-east1`:
         
         export BUCKET1="troubleshoot-bucket1-PROJECT_ID"
         gcloud storage buckets create gs://${BUCKET1} --location=us-east1

  2. Create a bucket in `us-west1`:
         
         export BUCKET2="troubleshoot-bucket2-PROJECT_ID"
         gcloud storage buckets create gs://${BUCKET2} --location=us-west1




After the event source is created, deploy the event receiver service on Cloud Run.

## Deploy the event receiver

Deploy a Cloud Run service that receives and logs events.

  1. Retrieve the code sample by cloning the GitHub repository:

### Go
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples.git
         cd golang-samples/eventarc/audit_storage
         

### Java
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git
         cd java-docs-samples/eventarc/audit-storage
         

### .NET
         
         git clone https://github.com/GoogleCloudPlatform/dotnet-docs-samples.git
         cd dotnet-docs-samples/eventarc/audit-storage
         

### Node.js
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git
         cd nodejs-docs-samples/eventarc/audit-storage
         

### Python
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
         cd python-docs-samples/eventarc/audit-storage
         

  2. Review the code for this tutorial which consists of the following:

     * An event handler that receives the incoming event as a CloudEvent within the HTTP `POST` request:

### Go
           
           // Processes CloudEvents containing Cloud Audit Logs for Cloud Storage
           package main
           
           import (
           	"fmt"
           	"log"
           	"net/http"
           	"os"
           
           	cloudevent "github.com/cloudevents/sdk-go/v2"
           )
           
           // HelloEventsStorage receives and processes a Cloud Audit Log event with Cloud Storage data.
           func HelloEventsStorage(w http.ResponseWriter, r *http.Request) {
           	if r.Method != http.MethodPost {
           		http.Error(w, "Expected HTTP POST request with CloudEvent payload", http.StatusMethodNotAllowed)
           		return
           	}
           
           	event, err := cloudevent.NewEventFromHTTPRequest(r)
           	if err != nil {
           		log.Printf("cloudevent.NewEventFromHTTPRequest: %v", err)
           		http.Error(w, "Failed to create CloudEvent from request.", http.StatusBadRequest)
           		return
           	}
           	s := fmt.Sprintf("Detected change in Cloud Storage bucket: %s", event.Subject())
           	fmt.Fprintln(w, s)
           }
           

### Java
           
           import io.cloudevents.CloudEvent;
           import io.cloudevents.rw.CloudEventRWException;
           import io.cloudevents.spring.http.CloudEventHttpUtils;
           import org.springframework.http.HttpHeaders;
           import org.springframework.http.HttpStatus;
           import org.springframework.http.ResponseEntity;
           import org.springframework.web.bind.annotation.RequestBody;
           import org.springframework.web.bind.annotation.RequestHeader;
           import org.springframework.web.bind.annotation.RequestMapping;
           import org.springframework.web.bind.annotation.RequestMethod;
           import org.springframework.web.bind.annotation.RestController;
           
           @RestController
           public class EventController {
           
             @RequestMapping(value = "/", method = RequestMethod.POST, consumes = "application/json")
             public ResponseEntity<String> receiveMessage(
                 @RequestBody String body, @RequestHeader HttpHeaders headers) {
               CloudEvent event;
               try {
                 event =
                     CloudEventHttpUtils.fromHttp(headers)
                         .withData(headers.getContentType().toString(), body.getBytes())
                         .build();
               } catch (CloudEventRWException e) {
                 return new ResponseEntity<>(e.getMessage(), HttpStatus.BAD_REQUEST);
               }
           
               String ceSubject = event.getSubject();
               String msg = "Detected change in Cloud Storage bucket: " + ceSubject;
               System.out.println(msg);
               return new ResponseEntity<>(msg, HttpStatus.OK);
             }
           }

### .NET
           
           using Microsoft.AspNetCore.Builder;
           using Microsoft.AspNetCore.Hosting;
           using Microsoft.AspNetCore.Http;
           using Microsoft.Extensions.DependencyInjection;
           using Microsoft.Extensions.Hosting;
           using Microsoft.Extensions.Logging;
           
           public class Startup
           {
               public void ConfigureServices(IServiceCollection services)
               {
               }
           
               public void Configure(IApplicationBuilder app, IWebHostEnvironment env, ILogger<Startup> logger)
               {
                   if (env.IsDevelopment())
                   {
                       app.UseDeveloperExceptionPage();
                   }
           
                   logger.LogInformation("Service is starting...");
           
                   app.UseRouting();
           
                   app.UseEndpoints(endpoints =>
                   {
                       endpoints.MapPost("/", async context =>
                       {
                           logger.LogInformation("Handling HTTP POST");
           
                           var ceSubject = context.Request.Headers["ce-subject"];
                           logger.LogInformation($"ce-subject: {ceSubject}");
           
                           if (string.IsNullOrEmpty(ceSubject))
                           {
                               context.Response.StatusCode = 400;
                               await context.Response.WriteAsync("Bad Request: expected header Ce-Subject");
                               return;
                           }
           
                           await context.Response.WriteAsync($"GCS CloudEvent type: {ceSubject}");
                       });
                   });
               }
           }
           

### Node.js
           
           const express = require('express');
           const app = express();
           
           app.use(express.json());
           app.post('/', (req, res) => {
             if (!req.header('ce-subject')) {
               return res
                 .status(400)
                 .send('Bad Request: missing required header: ce-subject');
             }
           
             console.log(
               `Detected change in Cloud Storage bucket: ${req.header('ce-subject')}`
             );
             return res
               .status(200)
               .send(
                 `Detected change in Cloud Storage bucket: ${req.header('ce-subject')}`
               );
           });
           
           module.exports = app;

### Python
           
           @app.route("/", methods=["POST"])
           def index():
               # Create a CloudEvent object from the incoming request
               event = from_http(request.headers, request.data)
               # Gets the GCS bucket name from the CloudEvent
               # Example: "storage.googleapis.com/projects/_/buckets/my-bucket"
               bucket = event.get("subject")
           
               print(f"Detected change in Cloud Storage bucket: {bucket}")
               return (f"Detected change in Cloud Storage bucket: {bucket}", 200)
           
           

     * A server that uses the event handler:

### Go
           
           func main() {
           	http.HandleFunc("/", HelloEventsStorage)
           	// Determine port for HTTP service.
           	port := os.Getenv("PORT")
           	if port == "" {
           		port = "8080"
           	}
           	// Start HTTP server.
           	log.Printf("Listening on port %s", port)
           	if err := http.ListenAndServe(":"+port, nil); err != nil {
           		log.Fatal(err)
           	}
           }
           

### Java
           
           import org.springframework.boot.SpringApplication;
           import org.springframework.boot.autoconfigure.SpringBootApplication;
           
           @SpringBootApplication
           public class Application {
             public static void main(String[] args) {
               SpringApplication.run(Application.class, args);
             }
           }

### .NET
           
           public static void Main(string[] args)
           {
               CreateHostBuilder(args).Build().Run();
           }
           public static IHostBuilder CreateHostBuilder(string[] args)
           {
               var port = Environment.GetEnvironmentVariable("PORT") ?? "8080";
               var url = $"http://0.0.0.0:{port}";
           
               return Host.CreateDefaultBuilder(args)
                   .ConfigureWebHostDefaults(webBuilder =>
                   {
                       webBuilder.UseStartup<Startup>().UseUrls(url);
                   });
           }
           

### Node.js
           
           const app = require('./app.js');
           const PORT = parseInt(process.env.PORT) || 8080;
           
           app.listen(PORT, () =>
             console.log(`nodejs-events-storage listening on port ${PORT}`)
           );

### Python
           
           import os
           
           from cloudevents.http import from_http
           
           from flask import Flask, request
           
           app = Flask(__name__)
           if __name__ == "__main__":
               app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

     * A Dockerfile that defines the operating environment for the service. The contents of the Dockerfile vary by language:

### Go
           
           # Use the official Go image to create a binary.
           # This is based on Debian and sets the GOPATH to /go.
           # https://hub.docker.com/_/golang
           FROM golang:1.25-bookworm as builder
           
           # Create and change to the app directory.
           WORKDIR /app
           
           # Retrieve application dependencies.
           # This allows the container build to reuse cached dependencies.
           # Expecting to copy go.mod and if present go.sum.
           COPY go.* ./
           RUN go mod download
           
           # Copy local code to the container image.
           COPY . ./
           
           # Build the binary.
           RUN go build -v -o server
           
           # Use the official Debian slim image for a lean production container.
           # https://hub.docker.com/_/debian
           # https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
           FROM debian:bookworm-slim
           RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
               ca-certificates && \
               rm -rf /var/lib/apt/lists/*
           
           # Copy the binary to the production image from the builder stage.
           COPY --from=builder /app/server /server
           
           # Run the web service on container startup.
           CMD ["/server"]
           

### Java
           
           # Use the official maven image to create a build artifact.
           # https://hub.docker.com/_/maven
           FROM maven:3-eclipse-temurin-17-alpine as builder
           
           # Copy local code to the container image.
           WORKDIR /app
           COPY pom.xml .
           COPY src ./src
           
           # Build a release artifact.
           RUN mvn package -DskipTests
           
           # Use Eclipse Temurin for base image.
           # https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
           FROM eclipse-temurin:17.0.18_8-jre-alpine
           
           # Copy the jar to the production image from the builder stage.
           COPY --from=builder /app/target/audit-storage-*.jar /audit-storage.jar
           
           # Run the web service on container startup.
           CMD ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/audit-storage.jar"]
           

### .NET
           
           # Use Microsoft's official build .NET image.
           # https://hub.docker.com/_/microsoft-dotnet-core-sdk/
           FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS build
           WORKDIR /app
           
           # Install production dependencies.
           # Copy csproj and restore as distinct layers.
           COPY *.csproj ./
           RUN dotnet restore
           
           # Copy local code to the container image.
           COPY . ./
           WORKDIR /app
           
           # Build a release artifact.
           RUN dotnet publish -c Release -o out
           
           
           # Use Microsoft's official runtime .NET image.
           # https://hub.docker.com/_/microsoft-dotnet-core-aspnet/
           FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine AS runtime
           WORKDIR /app
           COPY --from=build /app/out ./
           
           # Run the web service on container startup.
           ENTRYPOINT ["dotnet", "AuditStorage.dll"]

### Node.js
           
           # Use the official lightweight Node.js image.
           # https://hub.docker.com/_/node
           FROM node:20-slim
           # Create and change to the app directory.
           WORKDIR /usr/src/app
           
           # Copy application dependency manifests to the container image.
           # A wildcard is used to ensure both package.json AND package-lock.json are copied.
           # Copying this separately prevents re-running npm install on every code change.
           COPY package*.json ./
           
           # Install dependencies.
           # if you need a deterministic and repeatable build create a 
           # package-lock.json file and use npm ci:
           # RUN npm ci --omit=dev
           # if you need to include development dependencies during development
           # of your application, use:
           # RUN npm install --dev
           
           RUN npm install --omit=dev
           
           # Copy local code to the container image.
           COPY . .
           
           # Run the web service on container startup.
           CMD [ "npm", "start" ]
           

### Python
           
           # Use the official Python image.
           # https://hub.docker.com/_/python
           FROM python:3.14-slim
           
           # Allow statements and log messages to immediately appear in the Cloud Run logs
           ENV PYTHONUNBUFFERED True
           
           # Copy application dependency manifests to the container image.
           # Copying this separately prevents re-running pip install on every code change.
           COPY requirements.txt ./
           
           # Install production dependencies.
           RUN pip install -r requirements.txt
           
           # Copy local code to the container image.
           ENV APP_HOME /app
           WORKDIR $APP_HOME
           COPY . ./
           
           # Run the web service on container startup. 
           # Use gunicorn webserver with one worker process and 8 threads.
           # For environments with multiple CPU cores, increase the number of workers
           # to be equal to the cores available.
           CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

  3. Build your container image with Cloud Build and upload the image to Artifact Registry:
         
         export PROJECT_ID=$(gcloud config get-value project)
         export SERVICE_NAME=troubleshoot-service
         gcloud builds submit --tag $REGION-docker.pkg.dev/${PROJECT_ID}/REPOSITORY/${SERVICE_NAME}:v1

  4. Deploy the container image to Cloud Run:
         
         gcloud run deploy ${SERVICE_NAME} \
             --image $REGION-docker.pkg.dev/${PROJECT_ID}/REPOSITORY/${SERVICE_NAME}:v1 \
             --allow-unauthenticated

When the deployment succeeds, the command line displays the service URL.




## Create a trigger

After deploying a Cloud Run service, set up a trigger to listen for events from Cloud Storage through audit logs.

  1. Create an Eventarc trigger to listen for Cloud Storage events that are routed using Cloud Audit Logs:
         
         gcloud eventarc triggers create troubleshoot-trigger \
             --destination-run-service=troubleshoot-service \
             --event-filters="type=google.cloud.audit.log.v1.written" \
             --event-filters="serviceName=storage.googleapis.com" \
             --event-filters="methodName=storage.objects.create" \
             --service-account=${PROJECT_NUMBER}-compute@developer.gserviceaccount.com
         

This creates a trigger called `troubleshoot-trigger`.

  2. To confirm `troubleshoot-trigger` has been created, run:
         
         gcloud eventarc triggers list
         

The output should be similar to the following:
         
         NAME: troubleshoot-trigger
         TYPE: google.cloud.audit.log.v1.written
         DESTINATION: Cloud Run service: troubleshoot-service
         ACTIVE: By 20:03:37
         LOCATION: us-central1
         




## Generate and view an event

Confirm that you have successfully deployed the service and can receive events from Cloud Storage.

  1. Create and upload a file to the `BUCKET1` storage bucket:
         
         echo "Hello World" > random.txt
          gcloud storage cp random.txt gs://${BUCKET1}/random.txt
         

  2. [Monitor the logs](https://docs.cloud.google.com/run/docs/logging) to check if the service received an event. To view the log entry, complete the following steps:

     1. Filter the log entries and return the output in JSON format:
            
            gcloud logging read "resource.labels.service_name=troubleshoot-service \
                AND textPayload:random.txt" \
                --format=json

     2. Look for a log entry similar to:
            
            "textPayload": "Detected change in Cloud Storage bucket: ..."
            

**Note:** If you don't see a log entry, wait a few minutes and retry the `gcloud logging read` command. The trigger can take up to two minutes after being created to start filtering events.



Note that, initially, no log entry is returned. This indicates that there is a problem in the setup that you must investigate.

## Investigate the problem

Go through the process of investigating why the service is not receiving events.

### Initialization time

Although your trigger is created immediately, it can take up to two minutes for a trigger to propagate and filter events. Run the following command to confirm that a trigger is active:
    
    
    gcloud eventarc triggers list
    

The output indicates the status of the trigger. In the following example, `troubleshoot-trigger` will be active by 14:16:56:
    
    
    NAME                  TYPE                               DESTINATION_RUN_SERVICE  ACTIVE
    troubleshoot-trigger  google.cloud.audit.log.v1.written  troubleshoot-service     By 14:16:56
    

Once the trigger is active, upload a file again to the storage bucket. Events are written in the Cloud Run service logs. If the service does not receive events, it could be related to the size of events.

### Audit logs

In this tutorial, Cloud Storage events are routed using Cloud Audit Logs and sent to Cloud Run. Confirm that the audit logs are enabled for Cloud Storage.

  1. In the Google Cloud console, go to the **Audit logs** page.

[Go to Audit logs](https://console.cloud.google.com/iam-admin/audit)

  2. Select the **Google Cloud Storage** checkbox.
  3. Ensure that the **Admin Read** , **Data Read** , and **Data Write** log types are selected.



Once you have enabled Cloud Audit Logs, upload the file again to the storage bucket and check the logs. If the service still does not receive events, this could be related to the trigger location.

### Trigger location

There could be multiple resources in different locations and you must filter for events from sources that are in the same region as the Cloud Run target. For more information, see the [locations supported by Eventarc](https://docs.cloud.google.com/eventarc/docs/locations) and [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations).

In this tutorial, you deployed the Cloud Run service to `us-central1`. Because you set `eventarc/location` to `us-central1`, you also created a trigger in the same location.

However, you created two Cloud Storage buckets in `us-east1` and `us-west1` locations. To receive events from those locations, you must create Eventarc triggers in those locations.

Create an Eventarc trigger located in `us-east1`:

  1. Confirm the location of the existing trigger:
         
         gcloud eventarc triggers describe troubleshoot-trigger
         

  2. Set the location and region to `us-east1`:
         
         gcloud config set eventarc/location us-east1
         gcloud config set run/region us-east1
         

  3. Deploy the event receiver again by building and deploying the container image to Cloud Run.

  4. Create a new trigger located in `us-east1`:
         
         gcloud eventarc triggers create troubleshoot-trigger-new \
           --destination-run-service=troubleshoot-service \
           --event-filters="type=google.cloud.audit.log.v1.written" \
           --event-filters="serviceName=storage.googleapis.com" \
           --event-filters="methodName=storage.objects.create" \
           --service-account=${PROJECT_NUMBER}-compute@developer.gserviceaccount.com
         

  5. Check that the trigger is created:
         
         gcloud eventarc triggers list
         

A trigger can take up to two minutes to initialize before it starts to route events.

  6. To confirm that the trigger is now deployed correctly, generate and view an event.




## Other issues you might encounter

You might encounter other issues when using Eventarc.

### Event size

The events you send must not exceed the limits on [event size](https://docs.cloud.google.com/eventarc/docs/quotas).

### A trigger that previously delivered events has stopped working

  1. Verify that the source is generating events. Check the [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit#viewing_audit_logs) and make sure the monitored service is emitting logs. If logs are recorded but events are not delivered, [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support).

  2. Verify that a Pub/Sub topic with the same trigger name exists. Eventarc uses Pub/Sub as its transport layer and will either use an existing Pub/Sub topic or will automatically create a topic and manage it for you.

     1. To list triggers, see [`gcloud eventarc triggers list`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/list).
     2. To list the Pub/Sub topics, run:
            
            gcloud pubsub topics list
            

     3. Verify that the Pub/Sub topic name includes the name of the created trigger. For example:

`name: projects/PROJECT_ID/topics/eventarc-us-east1-**troubleshoot-trigger-new** -123`

If the Pub/Sub topic is missing, [create the trigger again for a specific provider, event type, and Cloud Run destination](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers).

  3. Verify that the trigger has been configured for the service.

     1. In the Google Cloud console, go to the **Services** page.

[Go to Services](https://console.cloud.google.com/run)

     2. Click the name of the service to open its **Service details** page.

     3. Click the **Triggers** tab.

The Eventarc trigger associated with the service should be listed.

  4. Verify the health of the Pub/Sub topic and subscription using Pub/Sub [metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsub).

     * You can [monitor forwarded undeliverable messages](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_forwarded_undeliverable_messages) using the `subscription/dead_letter_message_count` metric. This metric shows the number of undeliverable messages that Pub/Sub forwards from a subscription.

If messages are not published to the topic, check [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit#viewing_audit_logs) and make sure the monitored service is emitting logs. If logs are recorded but events are not delivered, [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support).

     * You can [monitor push subscriptions](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_push_subscriptions) using the `subscription/push_request_count` metric and grouping the metric by `response_code` and `subcription_id`.

If push errors are reported, check the Cloud Run service logs. If the receiving endpoint returns a non-OK status code, it indicates that the Cloud Run code is not working as expected and you must [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support).

For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).




## Clean up

If you created a new project for this tutorial, delete the project. If you used an existing project and want to keep it without the changes added in this tutorial, delete the resources created for the tutorial.

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete tutorial resources

  1. Delete the Cloud Run service you deployed in this tutorial:
         
         gcloud run services delete SERVICE_NAME

Where `SERVICE_NAME` is your chosen service name.

You can also delete Cloud Run services from the [Google Cloud console](https://console.cloud.google.com/run).

  2. Remove any gcloud CLI default configurations you added during the tutorial setup.

For example:

`gcloud config unset run/region`

or

`gcloud config unset project`

  3. Delete other Google Cloud resources created in this tutorial:

     * Delete the Eventarc trigger: 
           
           gcloud eventarc triggers delete TRIGGER_NAME
           

Replace `TRIGGER_NAME` with the name of your trigger.

     * [Delete the container image](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images)



## What's next

  * [Troubleshoot issues](https://docs.cloud.google.com/eventarc/docs/troubleshooting)
  * [Known issues for Eventarc](https://docs.cloud.google.com/eventarc/docs/issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
