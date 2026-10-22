---
url: https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy/host/
title: Host your agent \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:18.751406+00:00
---

# Host your agent  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy/host/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Host your agent Stay organized with collections  Save and categorize content based on your preferences. 

The final step of this tutorial is to host your Dialogflow agent. [App Engine](https://docs.cloud.google.com/appengine/docs) is used for hosting, because it is simple to set up and scales well. The [Dialogflow Messenger](https://docs.cloud.google.com/dialogflow/es/docs/integrations/dialogflow-messenger) integration is used for an agent user interface.

## Project configuration

Ideally, your Dialogflow agent and the App Engine instance are both in the same project. Also, you must enable the Cloud Build API.

  1. Before creating the instance, select your project from the Google Cloud console.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the Cloud Build API for the project.

[Enable the Cloud Build API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)




## Environment setup

You need to install and configure some things in order to develop a Go application for App Engine. Follow any steps you haven't already completed at [Setting up your development environment](https://docs.cloud.google.com/appengine/docs/standard/go/setting-up-environment).

## Create the web service code

The example code for this tutorial is written in Go, but you can use any language supported by App Engine. Create the following file structure anywhere on your local machine:

  * `go-app/`: directory for your Go service. 
    * `templates/`: directory for your Go HTML templates. 
      * `index.html`: Go HTML template.
    * `app.yaml`: Your service's configuration settings.
    * `main.go`: Your application code.



The next three sections provide content for the three files.

### Contents of the `index.html` file

This Go HTML template file contains the HTML for the homepage. Populate this file with the following contents:
    
    
    <!DOCTYPE html>
    <html lang="en-US">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width">
        <title>Tutorial agent</title>
      </head>
      <body>
        <p>Open the chat window in the bottom right corner.</p>
      </body>
    </html>

### Contents of the `app.yaml` file

This is a configuration file which specifies your service's runtime environment settings. You can reference the [Go 1.12+ Runtime Environment document](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) to see the list of supported Go versions. Populate this file with the following contents:
    
    
    runtime: go116  # or another supported version

### Contents of the `main.go` file

This file contains your application code. Populate this file with the following contents:
    
    
    // Package main is the main package
    package main
    
    import (
    	"log"
    	"net/http"
    	"os"
    	"text/template"
    )
    
    var templates *template.Template
    
    func init() {
    	templates = template.Must(template.New("").ParseGlob("templates/*"))
    }
    
    // indexHandler handles the homepage.
    func indexHandler(w http.ResponseWriter, r *http.Request) {
    	if r.URL.Path != "/" {
    		http.NotFound(w, r)
    		return
    	}
    	if err := templates.ExecuteTemplate(w, "index.html", nil); err != nil {
    		log.Fatal(err)
    	}
    }
    
    func main() {
    	// Register the handlers
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

## Deploy your web service

Your code is now ready to deploy. These steps use the [gcloud tool](https://docs.cloud.google.com/sdk/gcloud) for deployment:

  1. Ensure that gcloud is configured with the same project as your Dialogflow agent. To check the project:
         
         gcloud config get-value project

To change the project:
         
         gcloud config set project YOUR_PROJECT

  2. In your `go-app` directory where your `app.yaml` file is located, deploy your web service to App Engine using the following command:
         
         gcloud app deploy

The command will prompt you for a region. Be sure to select the same region as your Dialogflow agent. The command will output the `target url` value, which is the URL for your web service.

  3. To launch your browser and view your web service, you can open the target URL from the previous step, or run the following command:
         
         gcloud app browse




## Setup Dialogflow Messenger

To set up and enable Dialogflow Messenger:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Click **Integrations** in the left sidebar menu.
  3. Click **Dialogflow Messenger**.
  4. A configuration dialog opens.
  5. Choose an [environment](https://docs.cloud.google.com/dialogflow/docs/agents-versions).
  6. Click **Enable**.
  7. Copy the embed code for pasting in your website.
  8. Click **Close**.



## Embed the agent in your web service

Paste the embed code you copied above in your `index.html` file. The `<script>` and `<df-messenger>` HTML elements should be in the `<body>` element of your page.

Deploy your web service app again with gcloud. Once deployed, you can interact with your agent through the webpage by clicking the chat icon in the lower right corner.

![Screenshot of Dialogflow agent embedded on webpage](https://docs.cloud.google.com/static/dialogflow/es/docs/tutorials/deploy/images/messenger.png)

You now have a fully deployed Dialogflow agent! Try having a conversation with the agent.

## Cleanup

While going through the steps of this tutorial, [you created billable resources](https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy#cost). To avoid incurring additional charges to your Google Cloud account:

  1. [Delete your database instance](https://docs.cloud.google.com/spanner/docs/create-manage-instances#delete-instance).
  2. Delete your function:
         
         gcloud functions delete tutorial-telecommunications-webhook

  3. [Disable your app](https://docs.cloud.google.com/appengine/docs/standard/go/console#disabling_an_application).

  4. [Delete your agent](https://docs.cloud.google.com/dialogflow/es/docs/agents-manage#delete)




## More information

For more information about the steps above, see:

  * [Building a Go App on App Engine](https://docs.cloud.google.com/appengine/docs/standard/go/building-app)
  * [Dialogflow Messenger](https://docs.cloud.google.com/dialogflow/es/docs/integrations/dialogflow-messenger)



[ Previous arrow_back  Query a database  ](https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy/database)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
