---
url: https://docs.cloud.google.com/appengine/docs/standard/go/building-app/
title: Build a Go app on App Engine \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:43.053298+00:00
---

# Build a Go app on App Engine  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/building-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Build a Go app on App Engine Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are deploying a new Go web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-go-service).

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/go/how-requests-are-routed#region-id). 

OK

This guide helps you get started with App Engine and become familiar with developing, deploying, and managing a Go app.

After you build your app, you can read other [tutorials](https://docs.cloud.google.com/docs/tutorials) to learn how to integrate with other Google Cloud services and add more features to your app.

## Costs

There are no costs associated with running this guide. Running this sample app alone does not exceed your [free quota](https://docs.cloud.google.com/appengine/docs/standard/quotas).

**Note:** You can't delete the default app.

## Set up your development environment

You can either use your local machine, and use tools you're already familiar with, or [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell). Cloud Shell has the Google Cloud CLI already installed, your environment already set up, and many other [features](https://docs.cloud.google.com/shell/docs/features).

### Local Machine

Install Go and set up the gcloud CLI as described in [Setting up your development environment](https://docs.cloud.google.com/appengine/docs/standard/setting-up-environment).

### Cloud Shell

Launch Cloud Shell, which has all the tools you'll need pre-installed: 

[Open Cloud Shell](https://console.cloud.google.com/appengine?cloudshell=true)

## Create a Google Cloud project

A project is required to use Google Cloud, and forms the basis for using all Google Cloud services.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Create your App Engine app and its associated resources. You must choose a location, which cannot be changed later. 
         
         gcloud app create

**Learn more** : Generally, select the region nearest to your app's users, but also consider the location of the [other Google Cloud products and services](https://cloud.google.com/about/locations/#locations) that your app uses. Read about the available [App Engine locations](https://docs.cloud.google.com/appengine/docs/standard/locations) and [resource locations](https://cloud.google.com/about/locations/#locations).
  15. Due to [changes in the default behavior for how Cloud Build uses service accounts](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates) in new projects, and [secure-by-default organization policy changes](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations), you might need to grant additional roles to your deploying service account. For more information on granting specific roles, see the [troubleshooting guide](https://docs.cloud.google.com/appengine/docs/standard/troubleshooter/deployment#default-sa-permissions).



## Write a basic web service for App Engine

Learn how to write a web service and declare runtime settings.

### Structure your files

Your service will have the following file structure:

  * `go-app/`: directory for your Go service. 
    * `app.yaml`: Your service's configuration settings.
    * `main.go`: Your application code.



### Create the `app.yaml` file

Every App Engine project has an `app.yaml` configuration file which specifies your service's runtime environment settings. Your service will not deploy without this file.

  1. Create a new folder called `go-app` for your Go service: 
         
         mkdir go-app

  2. In your `go-app/` folder, create a file called `app.yaml`, and add the following contents:
         
         runtime: go127  # or another supported version
         

This is the simplest configuration for an App Engine app. It indicates to App Engine that you're using Go. The `app.yaml` file can specify other Go versions, network settings, scaling settings, and more. For more information, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml).




### Create the `main.go` file

This sample uses the [`net/http`](https://golang.org/pkg/net/http/) package to create an HTTP server that prints "Hello, World!".

To set up your `main.go` file:

  1. In your `go-app/` folder, create a `main.go` file.

  2. Add the `package main` statement to treat your code as an executable program:
         
         package main
         

To successfully deploy a service, a `package main` statement must be defined at the beginning of at least one of your Go source files.

**Learn more** : You do not have to put the `app.yaml` file and the `main.go` file in the same directory. You can specify the directory containing your main package by using `main:` in your project's `app.yaml` file. For more information, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/go/configuring-your-app-with-app-yaml).

  3. Import the following packages:
         
         import (
         	"fmt"
         	"log"
         	"net/http"
         	"os"
         )
         

  4. Define your HTTP handler:
         
         // indexHandler responds to requests with our greeting.
         func indexHandler(w http.ResponseWriter, r *http.Request) {
         	if r.URL.Path != "/" {
         		http.NotFound(w, r)
         		return
         	}
         	fmt.Fprint(w, "Hello, World!")
         }
         

The `http.ResponseWriter` object assembles the HTTP server response; by writing to it, you send data to the browser. The `http.Request` object is a data structure that represents the incoming HTTP request.

  5. Register your HTTP handler:
         
         func main() {
         	http.HandleFunc("/", indexHandler)
         
         	port := os.Getenv("PORT")
         	if port == "" {
         		port = "8080"
         		log.Printf("Defaulting to port %s", port)
         	}
         
         	log.Printf("Listening on port %s", port)
         	if err := http.ListenAndServe(":"+port, nil); err != nil {
         		log.Fatal(err)
         	}
         }
         

The `main` function is the entry point of your executable program, so it starts the application. It begins with a call to the `http.HandleFunc` function which tells the `http` package to handle all requests to the web root (`"/"`) with the `indexHandler` function.

If the `PORT` environment variable is not set, port `8080` is used as a default. When your app is running on App Engine, the `PORT` environment variable is set for you, but when testing your app locally, you can set `PORT` to any preferred value.




## Deploy your web service on App Engine

  1. In your `go-app` directory where your `app.yaml` file is located, deploy your web service to App Engine using the following command: 
         
         gcloud app deploy

  2. To launch your browser and view your web service at `https://PROJECT_ID.REGION_ID.r.appspot.com`, run the following command: 
         
         gcloud app browse




Congratulations! You've just created and deployed a service on App Engine.

### Services and versions

The first service you deploy for your application will be the default service. You can specify the name of your service in the `app.yaml` file, but if the name is omitted, it is treated as `default`. You can deploy [multiple services](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine) other than the default service.

You can update your service at any time by running the `gcloud app deploy` command. Each time you deploy, a new version is created and traffic is automatically routed to the latest version.

To confirm service creation and version deployment:

  1. View your App Engine services in the Google Cloud console:

[View services](https://console.cloud.google.com/appengine/services)

You should see one service listed, named `default`. The default service is publicly accessible at the following URL:

`https://PROJECT_ID.REGION_ID.r.appspot.com`

  2. View your versions:

[View versions](https://console.cloud.google.com/appengine/versions)

You should see one timestamped version listed, corresponding to your deployment.




To learn how to send requests to specific services and versions, see [How Requests are Routed](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed).

## Next steps

Congratulations! You just set up and deployed your web application to App Engine.

Learn how to add other features to your application by exploring the following pages:

  * Learn more about writing application logs and interpreting system logs in [Reading and Writing Application Logs](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs).
  * For a deeper dive into how App Engine works, see the [Go Runtime Environment](https://docs.cloud.google.com/appengine/docs/standard/go/runtime).
  * Read about [request handling](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled) and [request routing](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
