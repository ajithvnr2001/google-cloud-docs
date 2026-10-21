---
url: https://docs.cloud.google.com/ruby/rails/appengine/
title: Run Rails 7 on App Engine flexible environment \u00a0|\u00a0 Ruby \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:46.405758+00:00
---

# Run Rails 7 on App Engine flexible environment  |  Ruby  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/rails/appengine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Guides ](https://docs.cloud.google.com/ruby/docs/setup)



Send feedback 

#  Run Rails 7 on App Engine flexible environment Stay organized with collections  Save and categorize content based on your preferences. 

Get started developing Ruby on Rails apps that run on [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible). The apps you create run on the same infrastructure that powers all of Google's products, so you can be confident that they can scale to serve all of your users, whether there are a few or millions of them.

This tutorial assumes you are familiar with Rails web development. It walks you through deploying a new Rails app.

This tutorial supports and requires [Ruby 3.0](https://www.ruby-lang.org/) or later.

### Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Set up your local environment for Rails

To set up your local environment for Rails development, you'll need to:

  1. Install [Ruby](https://www.ruby-lang.org/) version 3.0 or later.

  2. Install the [Rails 7](http://guides.rubyonrails.org/) gem.

  3. Install the [Bundler](https://bundler.io/) gem.




Alternatively, you can use [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), which comes with Ruby, Rails, and the Google Cloud CLI already installed.

For additional information on installing Rails and its dependencies, see the official [Getting started with Rails](http://guides.rubyonrails.org/getting_started.html) guide.

After you complete the prerequisites, you can create and deploy a Rails app. The following sections guide you through configuring, running, and deploying an app.

### Create a new app

  1. Create a new Rails sample app.
         
         rails new appengine_example
         

  2. Go to the directory that contains the sample code.
         
         cd appengine_example
         




### Run the app locally

To run the new Rails app on your local computer:

  1. Start a local web server.
         
         bundle exec rails server
         

  2. In your browser, go to [http://localhost:3000/](http://localhost:3000).

The sample app displays the Rails logo with the Rails and Ruby versions.


**Note:** In your terminal window, press `Ctrl+C` to exit the web server.

### Add a simple page

Now add a Welcome page to the generated Rails app.

  1. To generate the scaffolding for a new page, create a new Rails controller named `WelcomeController` with an `index` action.
         
         bundle exec rails generate controller Welcome index
         

  2. Open the file `app/views/welcome/index.html.erb` to see the following boilerplate HTML.
         
         <h1>Welcome#index</h1>
         <p>Find me in app/views/welcome/index.html.erb</p>

  3. Modify the file however you like. For example, you can use the following content:
         
         <h1>Welcome</h1>
         <p>This is a home page for a new Rails App on Google Cloud Platform!</p>

  4. Set the `index` controller action as the root action for Rails. Then, whenever a user visits the Rails app, they see your welcome page.

  5. Open the file `config/routes.rb` to see the following generated content.
         
         Rails.application.routes.draw do
           get 'welcome/index'
         
           # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
         end

  6. To modify this file, add `root 'welcome#index'`.
         
         Rails.application.routes.draw do
           get 'welcome/index'
         
           # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
           root 'welcome#index'
         end

  7. Save the file and close it. Test the Rails app as you did before.




## Deploy the app to App Engine flexible environment

App Engine flexible environment uses a file called [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/ruby/configuring-your-app-with-app-yaml). to describe an app's deployment configuration. If this file isn't present, the gcloud CLI tries to guess the deployment configuration. However, it is a good idea to provide this file because Rails requires a secret key in a production environment.

To configure the sample app for deployment to App Engine, create a new file named `app.yaml` at the root of your sample app directory and add the following:
    
    
    entrypoint: bundle exec rackup --port $PORT
    env: flex
    runtime: ruby

### Configure the Rails secret key

When you deploy a Rails app in the production environment, set the environment variable `SECRET_KEY_BASE` to a secret key that is used to protect user session data. This environment variable is read in the `config/secrets.yml` file.

  1. Generate a new secret key.
         
         bundle exec rails secret
         

  2. Copy the generated secret key. You use the secret key in the next step.

  3. Open the file `app.yaml` that you created earlier, and add an `env_variables` section. The `env_variables` sets environment variables in the `production` environment in App Engine flexible environment. Your `app.yaml` should look like the example below, with `[SECRET_KEY]` replaced with your copied secret key.
         
         entrypoint: bundle exec rackup --port $PORT
         env: flex
         runtime: ruby
         
         env_variables:
           SECRET_KEY_BASE: [SECRET_KEY]




### Set up an App Engine flexible environment app

If this is the first time you are deploying an app, you need to create an App Engine flexible environment app to help you select the region in which to run the Rails app. You can read more about [regions and zones](https://docs.cloud.google.com/docs/geography-and-regions).

  1. Create an App Engine app. By default, the following command creates two instances:
         
         gcloud app create
         

  2. Select a region that supports the App Engine flexible environment for Ruby apps.




### Deploy to App Engine flexible environment

Deploy the sample app by running the following command:
    
    
    gcloud app deploy
    

Wait for the message that notifies you that the update has completed. This can take several minutes.

## Access the deployed Rails app

  1. To retrieve your project ID, run `gcloud info`.

  2. In your browser, enter the following URL:

`https://PROJECT_ID.REGION_ID.r.appspot.com`

Replace the following:

     * `PROJECT_ID`: Your Google Cloud project ID
     * `REGION_ID`: A [code that App Engine assigns to your app](https://docs.cloud.google.com/appengine/docs/flexible/ruby/how-requests-are-routed#region-id)



The following content is displayed.

![Screenshot of new Rails app running](https://docs.cloud.google.com/static/ruby/images/new-rails-app-getting-started.png)

This time, your request is served by the Rails app running in App Engine flexible environment.

This command deploys the app as described in `app.yaml` and sets the newly deployed version as the default version, causing it to serve all new traffic. As the app deploys, you might see several repeated messages while the platform checks whether the app is serving. This is normal. Wait for the message that notifies you that the update of the app is complete.

If you update your app, you can deploy the updated version by entering the same command you used to deploy the app the first time. The new deployment creates a [new version](https://console.cloud.google.com/appengine/versions) of your app and promotes it to the default version. The older versions of your app remain, as do their associated VM instances. Be aware that all of these app versions and VM instances are billable resources.

## Read App Engine logs

Now that you have deployed your Rails app, you may want to read the logs. You can read the app logs by using the [Logs Explorer](https://console.cloud.google.com/logs/query) located in the Google Cloud console, or by using `gcloud app logs read`. You can learn more about [reading logs by using the gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/app/logs/read).

## Clean up resources

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

### Delete project

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



### Delete an App Engine version

To delete an app version: 

  1. In the Google Cloud console, go to the **Versions** page for App Engine. 

[Go to Versions](https://console.cloud.google.com/appengine/versions)

  2. Select the checkbox for the non-default app version that you want to delete. **Note:** The only way you can delete the default version of your App Engine app is by deleting your project. However, you can [stop the default version in the Google Cloud console](https://console.cloud.google.com/appengine/versions). This action shuts down all instances associated with the version. You can restart these instances later if needed. 

In the App Engine standard environment, you can stop the default version only if your app has manual or basic scaling. 

  3. To delete the app version, click delete **Delete**. 



## What's next

  * Learn how to [use Cloud SQL for MySQL with Rails](https://docs.cloud.google.com/ruby/rails/using-cloudsql-mysql).

  * Learn how to [use Cloud SQL for PostgreSQL with Rails](https://docs.cloud.google.com/ruby/rails/using-cloudsql-postgres).

  * Learn how to [run the Ruby Bookshelf sample in App Engine flexible environment](https://docs.cloud.google.com/ruby/getting-started/tutorial-app).

  * Learn how to [run the Ruby Bookshelf sample on Compute Engine](https://docs.cloud.google.com/ruby/tutorials/bookshelf-on-compute-engine).

  * Learn how to [run the Ruby Bookshelf sample on GKE](https://docs.cloud.google.com/ruby/tutorials/bookshelf-on-kubernetes-engine).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
