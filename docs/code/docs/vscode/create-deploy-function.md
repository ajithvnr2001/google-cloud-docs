---
url: https://docs.cloud.google.com/code/docs/vscode/create-deploy-function/
title: Quickstart: Deploy a Cloud Run function using the gcloud CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:16.780242+00:00
---

# Quickstart: Deploy a Cloud Run function using the gcloud CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/create-deploy-function/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Deploy a Cloud Run function using the gcloud CLI

Cloud Run functions lets you run lightweight code in response to HTTP requests without managing infrastructure. In this quickstart, you deploy an HTTP function by using gcloud CLI.

## Before you begin

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

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Artifact Registry, Cloud Build, Cloud Run Admin API, and Cloud Logging APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com run.googleapis.com logging.googleapis.com

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  13. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Artifact Registry, Cloud Build, Cloud Run Admin API, and Cloud Logging APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable artifactregistry.googleapis.com cloudbuild.googleapis.com run.googleapis.com logging.googleapis.com

  16. To set the default project for your Cloud Run service: 
         
         gcloud config set project PROJECT_ID

Replace PROJECT_ID with the name of the project you created for this quickstart. 
  17. If you are under a domain restriction organization policy [restricting](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) unauthenticated invocations for your project, you will need to access your deployed service as described under [Testing private services](https://docs.cloud.google.com/run/docs/triggering/https-request#testing-private).

  18. Review [Cloud Run pricing](https://docs.cloud.google.com/run/pricing) or estimate costs with the [pricing calculator](https://cloud.google.com/products/calculator).



### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) on the project
  * [Cloud Run Source Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity
  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant the Cloud Build service account access to your project

Cloud Build automatically uses the [Compute Engine default service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) as the default Cloud Build service account to build your source code and Cloud Run resource, unless you override this behavior.

For Cloud Build to build your sources, grant the Cloud Build service account the [Cloud Run Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`) role on your project:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:SERVICE_ACCOUNT_EMAIL_ADDRESS \
        --role=roles/run.builder

Replace `PROJECT_ID` with your Google Cloud project ID and `SERVICE_ACCOUNT_EMAIL_ADDRESS` with the email address of the Cloud Build service account. If you're using the Compute Engine default service account as the Cloud Build service account, then use the following format for the service account email address:
    
    
    PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number.

For detailed instructions on how to find your project ID, and project number, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

Granting the Cloud Run builder role takes a couple of minutes to [propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Write the sample function

To write an application, follow these steps:

###  Node.js 

  1. Create a new directory named `helloworld` and change directory into it:
         
         mkdir helloworld
            cd helloworld
         

  2. Create a `package.json` file in the `helloworld` directory to specify Node.js dependencies:
         
         {
           "name": "nodejs-docs-samples-functions-hello-world-get",
           "version": "0.0.1",
           "private": true,
           "license": "Apache-2.0",
           "author": "Google Inc.",
           "repository": {
             "type": "git",
             "url": "https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git"
           },
           "engines": {
             "node": ">=16.0.0"
           },
           "scripts": {
             "test": "c8 mocha -p -j 2 test/*.test.js --timeout=6000 --exit"
           },
           "dependencies": {
             "@google-cloud/functions-framework": "^3.1.0"
           },
           "devDependencies": {
             "c8": "^10.0.0",
             "gaxios": "^6.0.0",
             "mocha": "^10.0.0",
             "wait-port": "^1.0.4"
           }
         }

  3. Create an `index.js` file in the `helloworld` directory with the following Node.js sample:
         
         import { http } from '@google-cloud/functions-framework';
         // Register an HTTP function with the Functions Framework that executes
         // when you make an HTTP request to the deployed function's endpoint.
         http('helloGET', (req, res) => {
           res.send('Hello World!');
         });




###  Python 

  1. Create a new directory named `helloworld` and change directory into it:
         
         mkdir helloworld
            cd helloworld
         

  2. Create a `requirements.txt` file in the `helloworld` directory, to specify Python dependencies:
         
         functions-framework==3.9.2
         Flask==3.1.3; python_version >= '3.9'
         google-cloud-error-reporting==1.11.1
         MarkupSafe==2.1.3
         

This adds packages needed by the sample.

  3. Create a `main.py` file in the `helloworld` directory with the following Python sample:
         
         import functions_framework
         
         @functions_framework.http
         def hello_get(request):
             """HTTP Cloud Function.
             Args:
                 request (flask.Request): The request object.
                 <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
             Returns:
                 The response text, or any set of values that can be turned into a
                 Response object using `make_response`
                 <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
             Note:
                 For more information on how Flask integrates with Cloud
                 Functions, see the `Writing HTTP functions` page.
                 <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
             """
             return "Hello World!"
         
         




###  Go 

  1. Create a new directory named `helloworld` and change directory into it:
         
         mkdir helloworld
            cd helloworld
         

  2. Create a `go.mod` file to declare the [go module](https://blog.golang.org/using-go-modules):
         
         module github.com/GoogleCloudPlatform/golang-samples/functions/functionsv2/helloworld
         
         go 1.25.0
         
         require github.com/GoogleCloudPlatform/functions-framework-go v1.8.1
         
         require (
         	github.com/cloudevents/sdk-go/v2 v2.15.2 // indirect
         	github.com/google/go-cmp v0.6.0 // indirect
         	github.com/google/uuid v1.6.0 // indirect
         	github.com/json-iterator/go v1.1.12 // indirect
         	github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
         	github.com/modern-go/reflect2 v1.0.2 // indirect
         	github.com/stretchr/testify v1.10.0 // indirect
         	go.uber.org/multierr v1.11.0 // indirect
         	go.uber.org/zap v1.27.0 // indirect
         	golang.org/x/time v0.15.0 // indirect
         )
         

  3. Create an `hello_http.go` file in the `helloworld` directory with the following Go code sample:
         
         // Package helloworld provides a set of Cloud Functions samples.
         package helloworld
         
         import (
         	"fmt"
         	"net/http"
         
         	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
         )
         
         func init() {
         	functions.HTTP("HelloGet", helloGet)
         }
         
         // helloGet is an HTTP Cloud Function.
         func helloGet(w http.ResponseWriter, r *http.Request) {
         	fmt.Fprint(w, "Hello, World!")
         }
         




###  Java 

  1. Create a new directory named `helloworld` and change directory into it:
         
         mkdir helloworld
            cd helloworld
         

  2. Create the following project structure to contain the source directory and source file:
         
         mkdir -p ~/helloworld/src/main/java/functions
         touch ~/helloworld/src/main/java/functions/HelloWorld.java
         

  3. Update the `HelloWorld.java` file with the following Java code sample:
         
         package functions;
         
         import com.google.cloud.functions.HttpFunction;
         import com.google.cloud.functions.HttpRequest;
         import com.google.cloud.functions.HttpResponse;
         import java.io.BufferedWriter;
         import java.io.IOException;
         
         public class HelloWorld implements HttpFunction {
           // Simple function to return "Hello World"
           @Override
           public void service(HttpRequest request, HttpResponse response)
               throws IOException {
             BufferedWriter writer = response.getWriter();
             writer.write("Hello World!");
           }
         }

  4. Create a `pom.xml` file in the `helloworld` directory, and add the following Java dependencies:
         
         <?xml version="1.0" encoding="UTF-8"?>
         
         <!--
           Copyright 2020 Google LLC
         
           Licensed under the Apache License, Version 2.0 (the "License");
           you may not use this file except in compliance with the License.
           You may obtain a copy of the License at
         
           http://www.apache.org/licenses/LICENSE-2.0
         
           Unless required by applicable law or agreed to in writing, software
           distributed under the License is distributed on an "AS IS" BASIS,
           WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
           See the License for the specific language governing permissions and
           limitations under the License.
         -->
         
         <project xmlns="http://maven.apache.org/POM/4.0.0"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
           <modelVersion>4.0.0</modelVersion>
         
           <groupId>com.example.functions</groupId>
           <artifactId>functions-hello-world</artifactId>
           <version>1.0.0-SNAPSHOT</version>
         
           <parent>
             <groupId>com.google.cloud.samples</groupId>
             <artifactId>shared-configuration</artifactId>
             <version>1.2.0</version>
           </parent>
         
           <dependencyManagement>
             <dependencies>
               <dependency>
                 <artifactId>libraries-bom</artifactId>
                 <groupId>com.google.cloud</groupId>
                 <scope>import</scope>
                 <type>pom</type>
                 <version>26.32.0</version>
               </dependency>
             </dependencies>
           </dependencyManagement>
         
           <properties>
             <maven.compiler.target>11</maven.compiler.target>
             <maven.compiler.source>11</maven.compiler.source>
           </properties>
         
           <dependencies>
             <!-- Required for Function primitives -->
             <dependency>
               <groupId>com.google.cloud.functions</groupId>
               <artifactId>functions-framework-api</artifactId>
               <version>1.1.0</version>
               <scope>provided</scope>
             </dependency>
         
             <!-- The following dependencies are only required for testing -->
             <dependency>
               <groupId>com.google.truth</groupId>
               <artifactId>truth</artifactId>
               <version>1.4.0</version>
               <scope>test</scope>
             </dependency>
             <dependency>
               <groupId>com.google.guava</groupId>
               <artifactId>guava-testlib</artifactId>
               <scope>test</scope>
             </dependency>
             <dependency>
               <groupId>org.mockito</groupId>
               <artifactId>mockito-core</artifactId>
               <version>5.10.0</version>
               <scope>test</scope>
             </dependency>
           </dependencies>
         
           <build>
             <plugins>
               <plugin>
                 <!--
                   Google Cloud Functions Framework Maven plugin
         
                   This plugin allows you to run Cloud Functions Java code
                   locally. Use the following terminal command to run a
                   given function locally:
         
                   mvn function:run -Drun.functionTarget=your.package.yourFunction
                 -->
                 <groupId>com.google.cloud.functions</groupId>
                 <artifactId>function-maven-plugin</artifactId>
                 <version>0.11.0</version>
                 <configuration>
                   <functionTarget>functions.HelloWorld</functionTarget>
                 </configuration>
               </plugin>
               <plugin>
                 <groupId>org.apache.maven.plugins</groupId>
                 <artifactId>maven-surefire-plugin</artifactId>
                 <!-- version 3.0.0-M4 does not load JUnit5 correctly -->
                 <!-- see https://issues.apache.org/jira/browse/SUREFIRE-1750 -->
                 <version>3.2.5</version>
                 <configuration>
                   <includes>
                     <include>**/*Test.java</include>
                   </includes>
                   <skipTests>${skipTests}</skipTests>
                   <reportNameSuffix>sponge_log</reportNameSuffix>
                   <trimStackTrace>false</trimStackTrace>
                 </configuration>
               </plugin>
             </plugins>
           </build>
         </project>
         




###  Ruby 

  1. Create a new directory named `helloworld` and change directory into it:
         
         mkdir helloworld
            cd helloworld
         

  2. Create a file named `app.rb` and paste the following code into it:
         
         require "functions_framework"
         
         FunctionsFramework.http "hello_get" do |_request|
           # The request parameter is a Rack::Request object.
           # See https://www.rubydoc.info/gems/rack/Rack/Request
         
           # Return the response body as a string.
           # You can also return a Rack::Response object, a Rack response array, or
           # a hash which will be JSON-encoded into a response.
           "Hello World!"
         end

  3. Create a file named `Gemfile` and copy the following into it:
         
         source "https://rubygems.org"
         
         gem "base64", "~> 0.2"
         gem "functions_framework", "~> 1.4"

  4. If you don't have Bundler 2.0 or greater installed, install [Bundler](https://bundler.io/).

  5. Generate a `Gemfile.lock` file by running:
         
         bundle install
         




###  PHP 

  1. Create a new directory named `helloworld` and change directory into it:
         
         mkdir helloworld
            cd helloworld
         

  2. Create a file named `index.php` and paste the following code into it:
         
         use Psr\Http\Message\ServerRequestInterface;
         
         function helloGet(ServerRequestInterface $request): string
         {
             return 'Hello, World!' . PHP_EOL;
         }
         

  3. If you aren't using Cloud Shell, create a `composer.json` file and paste the following code into it:
         
         {
             "require": {
                 "google/cloud-functions-framework": "^1.0"
             },
             "scripts": {
                 "start": [
                    "Composer\\Config::disableProcessTimeout",
                    "FUNCTION_TARGET=helloGet php -S localhost:${PORT:-8080} vendor/google/cloud-functions-framework/router.php"
                 ]
             }
         }
         




###  .NET 

  1. Install [.NET SDK](https://www.microsoft.com/net/core).

  2. From the console, create a new empty web project using the dotnet command.
         
         dotnet new web -o helloworld-csharp
         

  3. Change directory to `helloworld-csharp`:

  4. Replace the sample code in the project file `helloworld-csharp.csproj` with the following:
         
         <Project Sdk="Microsoft.NET.Sdk">
           <PropertyGroup>
             <OutputType>Exe</OutputType>
             <TargetFramework>net8.0</TargetFramework>
           </PropertyGroup>
         
           <ItemGroup>
             <PackageReference Include="Google.Cloud.Functions.Hosting" Version="3.0.1" />
           </ItemGroup>
         </Project>

  5. Replace the sample code in `Program.cs` file with the following:
         
         using Google.Cloud.Functions.Framework;
         using Microsoft.AspNetCore.Http;
         using System.Threading.Tasks;
         
         namespace HelloWorld;
         
         public class Function : IHttpFunction
         {
             public async Task HandleAsync(HttpContext context)
             {
                 await context.Response.WriteAsync("Hello World!", context.RequestAborted);
             }
         }




## Deploy the function

To deploy your Cloud Run function, follow these steps:

  1. Deploy the function by running the following command in the directory that contains the sample code:

###  Node.js 
         
         gcloud run deploy nodejs-http-function \
               --source . \
               --function helloGET \
               --base-image nodejs24 \
               --region REGION \
               --allow-unauthenticated
         

Replace REGION with the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) of the service where you want to deploy your function. For example, `europe-west1`. 

###  Python 
         
         gcloud run deploy python-http-function \
               --source . \
               --function hello_get \
               --base-image python314 \
               --region REGION \
               --allow-unauthenticated
         

Replace REGION with the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) of the service where you want to deploy your function. For example, `europe-west1`. 

###  Go 
         
         gcloud run deploy go-http-function \
                --source . \
                --function HelloGet \
                --base-image go127 \
                --region REGION \
                --allow-unauthenticated
         

Replace REGION with the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) of the service where you want to deploy your function. For example, `europe-west1`. 

###  Java 

Run the following command in the directory that contains the `pom.xml` file:
         
         gcloud run deploy java-http-function \
                --source . \
                --function functions.HelloWorld \
                --base-image java25 \
                --region REGION \
                --allow-unauthenticated
         

Replace REGION with the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) of the service where you want to deploy your function. For example, `europe-west1`. 

###  Ruby 
         
         gcloud run deploy ruby-http-function \
                --source . \
                --function hello_get \
                --base-image ruby40 \
                --region REGION \
                --allow-unauthenticated
         

Replace REGION with the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) of the service where you want to deploy your function. For example, `europe-west1`. 

###  PHP 
         
         gcloud run deploy php-http-function \
                --source . \
                --function helloGet \
                --base-image php85 \
                --region REGION \
                --allow-unauthenticated
         

Replace REGION with the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) of the service where you want to deploy your function. For example, `europe-west1`. 

###  .NET 
         
         gcloud run deploy csharp-http-function \
               --source . \
               --function HelloWorld.Function \
               --base-image dotnet10 \
               --region REGION \
               --allow-unauthenticated
         

Replace REGION with the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) of the service where you want to deploy your function. For example, `europe-west1`. 

  2. When the deployment is complete, the Google Cloud CLI displays a URL where the service is running. Open the URL in your browser to see the output of your function.

**Success:** You deployed an HTTP Cloud Run function using the gcloud CLI.



## Clean up

To avoid additional charges to your Google Cloud account, delete all the resources you deployed with this quickstart.

### Delete your repository

Cloud Run doesn't charge you when your deployed service isn't in use. However, you might still be [charged for storing the container image in Artifact Registry](https://cloud.google.com/artifact-registry/pricing). To delete Artifact Registry repositories, follow the steps in [Delete repositories](https://docs.cloud.google.com/artifact-registry/docs/manage-repos#delete) in the Artifact Registry documentation.

### Delete your service

Cloud Run services don't incur costs until they receive requests. To delete your Cloud Run service, follow one of these steps:

### Console

To delete a service:

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Locate the service you want to delete in the services list, and click its checkbox to select it.

  3. Click **Delete**. This deletes all revisions of the service.




###  gcloud 

To delete a service, run the following command:
    
    
    gcloud run services delete SERVICE --region REGION

Replace the following:

  * SERVICE: name of your service.
  * REGION: Google Cloud region of the service.



### Delete your test project

Deleting your Google Cloud project stops billing for all resources in that project. To release all Google Cloud resources in your project, follow these steps:

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * To deploy a sample function to Cloud Run using the Google Cloud console, see [Quickstart: Deploy a function to Cloud Run using the Google Cloud console](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console).

  * To deploy functions and create triggers using the Google Cloud console and the Google Cloud CLI, see [Deploy functions](https://docs.cloud.google.com/run/docs/deploy-functions).

  * To view and delete existing functions, see [Manage service revisions](https://docs.cloud.google.com/run/docs/managing/revisions).

  * To build function containers in your own toolchain and deploy it to Cloud Run, see [Build functions](https://docs.cloud.google.com/run/docs/building/functions).

  * To create triggers with Eventarc, see [Create triggers with Eventarc](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
