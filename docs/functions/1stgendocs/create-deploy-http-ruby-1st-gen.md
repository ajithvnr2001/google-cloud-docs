---
url: https://docs.cloud.google.com/functions/1stgendocs/create-deploy-http-ruby-1st-gen/
title: Quickstart: Create and deploy an HTTP Cloud Run function by using Ruby \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:30.969309+00:00
---

# Quickstart: Create and deploy an HTTP Cloud Run function by using Ruby  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/create-deploy-http-ruby-1st-gen/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and deploy an HTTP Cloud Run function by using Ruby (1st gen)

This guide takes you through the process of writing a Cloud Run function using the Ruby runtime. There are two types of Cloud Run functions:

  * An HTTP function, which you invoke from standard HTTP requests.
  * An event-driven function, which you use to handle events from your Cloud infrastructure, such as messages on a Pub/Sub topic, or changes in a Cloud Storage bucket.



The sample shows how to create a simple HTTP function.

**Learn more** : For more details, read about [HTTP functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions) and [event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions). 

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

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Functions and Cloud Build APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudfunctions cloudbuild.googleapis.com

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

  13. Enable the Cloud Functions and Cloud Build APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudfunctions cloudbuild.googleapis.com

  14. Prepare your development environment. 

[ Go to the Ruby setup guide ](https://docs.cloud.google.com/ruby/docs/setup)




## Create a function

  1. Create a directory on your local system for the function code:

### Linux or Mac OS X
         
         mkdir ~/helloworld
         cd ~/helloworld
         

### Windows
         
         mkdir %HOMEPATH%\helloworld
         cd %HOMEPATH%\helloworld
         

  2. Create an `app.rb` file in the `helloworld` directory with the following contents:
         
         require "functions_framework"
         require "cgi/escape"
         require "json"
         
         FunctionsFramework.http "hello_http" do |request|
           # The request parameter is a Rack::Request object.
           # See https://www.rubydoc.info/gems/rack/Rack/Request
           name = request.params["name"] ||
                  begin
                    request.body.rewind
                    JSON.parse(request.body.read)["name"]
                  rescue StandardError
                    nil
                  end ||
                  "World"
           # Return the response body as a string.
           # You can also return a Rack::Response object, a Rack response array, or
           # a hash which will be JSON-encoded into a response.
           "Hello #{CGI.escape_html name}!"
         end

This example function takes a name supplied in the HTTP request and returns a greeting, or "Hello World!" when no name is supplied.

**Note:** Cloud Run functions looks for deployable functions in `app.rb` by default. Use the [`--source`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--source) flag when deploying your function using `gcloud` to specify a different directory containing an `app.rb` file.



## Specify dependencies

Dependencies in Ruby are managed with [bundler](https://bundler.io) and expressed in a file called `Gemfile`.

When you deploy your function, Cloud Run functions downloads and installs the dependencies declared in the `Gemfile` and `Gemfile.lock` using `bundler`.

The `Gemfile` lists the packages required by your function, along with any optional version constraints. For a Cloud Run function, one of these packages must be the `functions_framework` gem.

For this exercise, create a file named `Gemfile` in the same directory as the `app.rb` file that contains your function code, with the following contents:
    
    
    source "https://rubygems.org"
    
    gem "functions_framework", "~> 0.7"
    

Run the following command to install the `functions_framework` gem and other dependencies:
    
    
    bundle install
    

**Learn more** : For more details, read about [specifying dependencies](https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-ruby). 

## Build and test locally

Before deploying the function, you can build and test it locally. Run the following command to use the `functions-framework-ruby` executable to start a local web server running your `hello_http` function:
    
    
    bundle exec functions-framework-ruby --target hello_http
    # ...starts the web server in the foreground
    

If the function builds successfully, it displays the URL you can visit in your web browser to see the function in action: `http://localhost:8080/`. You should see a `Hello World!` message.

Alternatively, you can send requests to this function using `curl` from another terminal window:
    
    
    curl localhost:8080
    # Output: Hello World!
    

See [Testing Functions](https://github.com/GoogleCloudPlatform/functions-framework-ruby#documentation) in the Ruby Functions Framework documentation.

## Deploy the function

To deploy the function with an HTTP trigger, run the following command in the `helloworld` directory:
    
    
    gcloud functions deploy hello_http --no-gen2 --runtime ruby40 --trigger-http --allow-unauthenticated
    

The `--allow-unauthenticated` flag lets you reach the function [without authentication](https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam#allowing_unauthenticated_http_function_invocation). To require [authentication](https://docs.cloud.google.com/functions/1stgendocs/securing/authenticating#developers), omit the flag.

**Learn more** : For more details, read about [deploying Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/deploy#basics). 

## Test the deployed function

  1. When the function finishes deploying, take note of the `httpsTrigger.url` property or find it using the following command:
         
         gcloud functions describe hello_http
         

It should look like this:
         
         https://GCP_REGION-PROJECT_ID.cloudfunctions.net/hello_http

  2. Visit this URL in your browser. You should see a "Hello World!" message.

Try passing a name in the HTTP request, for example by using the following URL:
         
         https://GCP_REGION-PROJECT_ID.cloudfunctions.net/hello_http?name=NAME

You should see the message "Hello `NAME`!"




## View logs

You can view Cloud Run functions logs in the Cloud Logging UI or through the Google Cloud CLI.

### View logs with the command-line tool

To view logs for your function with the gcloud CLI, use the [`logs read`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/logs/read) command, followed by the name of the function:
    
    
    gcloud functions logs read hello_http

The output should resemble the following:
    
    
    LEVEL  NAME       EXECUTION_ID  TIME_UTC                 LOG
    D      helloHttp  rvb9j0axfclb  2019-09-18 22:06:25.983  Function execution started
    D      helloHttp  rvb9j0axfclb  2019-09-18 22:06:26.001  Function execution took 19 ms, finished with status code: 200

**Note:** There is typically a slight delay between when log entries are created and when they show up in Cloud Logging.

### View logs in the Logging dashboard

You can also view logs for Cloud Run functions from the [Google Cloud console](https://console.cloud.google.com/project/_/logs?service=cloudfunctions.googleapis.com).

**Learn more** : For more details, read about [writing, viewing, and responding to logs](https://docs.cloud.google.com/functions/1stgendocs/monitoring/logging). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
