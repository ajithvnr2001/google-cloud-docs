---
url: https://docs.cloud.google.com/ruby/rails/using-cloudsql-mysql/
title: Use Cloud SQL for MySQL with Rails 7 on App Engine \u00a0|\u00a0 Ruby \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:12.928576+00:00
---

# Use Cloud SQL for MySQL with Rails 7 on App Engine  |  Ruby  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/rails/using-cloudsql-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Guides ](https://docs.cloud.google.com/ruby/docs/setup)



Send feedback 

#  Use Cloud SQL for MySQL with Rails 7 on App Engine Stay organized with collections  Save and categorize content based on your preferences. 

Get started developing Ruby on Rails apps that run on the [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible). The apps you create run on the same infrastructure that powers all of Google's products, so you can be confident that they can scale to serve all of your users, whether there are a few or millions of them.

This tutorial assumes you are familiar with Rails web development. It walks you through setting up [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql) with a new Rails app. You can also use this tutorial as a reference for configuring existing Rails apps to use Cloud SQL for MySQL.

This tutorial supports and requires [Ruby 3.0](https://www.ruby-lang.org/) or later.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin.googleapis.com)

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

  10. Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Preparing Cloud SQL for a MySQL instance

To set up Cloud SQL for a MySQL instance for this tutorial:

  1. Create a [Second Generation instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance). In this tutorial the name for the instance is `rails-cloudsql-instance`.

  2. Create a [database in the instance](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases). In this tutorial the name for the production database is `cat_list_production`.

  3. Set a [root user password for the instance](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#user-root).




## Setting up your local environment for Rails

To set up your local environment for this tutorial:

  1. Install [Ruby](https://www.ruby-lang.org/) version 3.0 or later.

  2. Install the [Rails 7](http://guides.rubyonrails.org/) gem.

  3. Install the [Bundler](https://bundler.io/) gem.


**Note:** Alternatively, you can use [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), which comes with Ruby, Rails, Bundler, and the Google Cloud CLI already installed.

For additional information on installing Rails and its dependencies, see the official [Getting started with Rails](http://guides.rubyonrails.org/getting_started.html) guide.

After you complete the prerequisites, you can create and deploy a Rails app using Cloud SQL for MySQL. The following sections guide you through configuring, connecting to Cloud SQL for MySQL, and deploying an app.

### Create a new app to list cats

  1. Run the `rails new` command to create a new Rails app. This app stores a list of cats in Cloud SQL for MySQL.
         
         rails new cat_sample_app
         

You might also need to install mysql libraries for mysql gems using a command like the following example:
         
         sudo apt-get install libmysqlclient-dev
         

  2. Go to the directory that contains the generated Rails app.
         
         cd cat_sample_app
         




### Run the application locally

To run the new Rails application on your local computer:

  1. Start a local web server:
         
         bundle exec bin/rails server
         

  2. In a web browser, go to <http://localhost:3000/>

The sample app displays the Rails logo with the Rails and Ruby versions.


**Note:** In your terminal window, press `Ctrl+C` to exit the web server.

### Generate scaffolding for a list of cats

Generate scaffolding for a resource named `Cat` that is used to form a list of cats with their name and age.

  1. Generate the scaffolding.
         
         bundle exec rails generate scaffold Cat name:string age:integer
         

The command generates a model, controller, and views for the `Cat` resource.
         
         invoke  active_record
         create    db/migrate/20230922063608_create_cats.rb
         create    app/models/cat.rb
         invoke    test_unit
         create      test/models/cat_test.rb
         create      test/fixtures/cats.yml
         invoke  resource_route
         route    resources :cats
         invoke  scaffold_controller
         create    app/controllers/cats_controller.rb
         invoke    erb
         create      app/views/cats
         create      app/views/cats/index.html.erb
         create      app/views/cats/edit.html.erb
         create      app/views/cats/show.html.erb
         create      app/views/cats/new.html.erb
         create      app/views/cats/_form.html.erb
         create      app/views/cats/_cat.html.erb
         invoke    resource_route
         invoke    test_unit
         create      test/controllers/cats_controller_test.rb
         create      test/system/cats_test.rb
         invoke    helper
         create      app/helpers/cats_helper.rb
         invoke      test_unit
         invoke    jbuilder
         create      app/views/cats/index.json.jbuilder
         create      app/views/cats/show.json.jbuilder
         create      app/views/cats/_cat.json.jbuilder
         

  2. Open the `config/routes.rb` file to see the following generated content.
         
         Rails.application.routes.draw do
           resources :cats
           get 'cats/index'
           # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
         
         end

  3. Add `root 'cats#index'` to the file.
         
         Rails.application.routes.draw do
           resources :cats
           get 'cats/index'
         
           # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
           root 'cats#index'
         end

  4. Save the file and close it.

  5. Test the Rails app as instructed before.




## Using Cloud SQL for MySQL with App Engine

Cloud SQL for MySQL is a fully managed database service to set up, maintain, manage, and administer your relational MySQL databases in Google Cloud. You can use Cloud SQL in a Rails app like any other relational database.

### Set up Cloud SQL for MySQL

To begin using Cloud SQL with your Rails app in production:

  1. Add the `mysql2` and `appengine` gems to the `Gemfile` file.
         
         bundle add mysql2
         bundle add appengine
         

The Rails `Gemfile` contains the following additional `gem` entries:
         
         # Added at 2017-08-07 11:54:06 -0700 by USER:
         gem "mysql2", "~> 0.4.8"
         
         # Added at 2017-08-07 11:54:12 -0700 by USER:
         gem "appengine", "~> 0.4.1"

**Note:** The `appengine` gem provides a Rake task to run database migrations in production.
  2. To configure the Rails app to connect to Cloud SQL, open the `config/database.yml` file. The following boilerplate database settings for SQLite are displayed:
         
         # SQLite version 3.x
         #   gem install sqlite3
         #
         #   Ensure the SQLite 3 gem is defined in your Gemfile
         #   gem 'sqlite3'
         #
         default: &default
           adapter: sqlite3
           pool: 5
           timeout: 5000
         
         development:
           <<: *default
           database: db/development.sqlite3
         
         # Warning: The database defined as "test" will be erased and
         # re-generated from your development database when you run "rake".
         # Do not set this db to the same as development or production.
         test:
           <<: *default
           database: db/test.sqlite3
         
         production:
           <<: *default
           database: db/production.sqlite3

  3. Configure the Cloud SQL instance connection name for the App Engine production environment.

     1. Retrieve the instance connection name.
            
            gcloud sql instances describe rails-cloudsql-instance
            

     2. Copy the value next to `connectionName`.

  4. Modify the `database.yml` production database configuration to the following:
         
         production:
           adapter: mysql2
           pool: 5
           timeout: 5000
           username: "[YOUR_MYSQL_USERNAME]"
           password: "[YOUR_MYSQL_PASSWORD]"
           database: "cat_list_production"
           socket:   "/cloudsql/[YOUR_INSTANCE_CONNECTION_NAME]"

Where:

     * `[YOUR_MYSQL_USERNAME]` represents your MySQL username.
     * `[YOUR_MYSQL_PASSWORD]` represents your MySQL password.
     * `[YOUR_INSTANCE_CONNECTION_NAME]` represents the instance connection name that you copied in the previous step.



The Rails app is now set up to use Cloud SQL when deploying to the App Engine flexible environment.

## Deploying the app to the App Engine flexible environment

The App Engine flexible environment uses a file called [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/ruby/configuring-your-app-with-app-yaml) to describe an app's deployment configuration. If this file isn't present, the gcloud CLI tries to guess the deployment configuration. However, you should define the file to provide required configuration settings for the Rails secret key and Cloud SQL.

To configure the sample app for deployment to App Engine, create a new file named `app.yaml` at the root of the Rails application directory and add the following:
    
    
    entrypoint: bundle exec rackup --port $PORT
    env: flex
    runtime: ruby

### Configure the Rails secret key in the `app.yaml` file

When a Rails app is deployed to the `production` environment, set the environment variable `SECRET_KEY_BASE` with a secret key to protect user session data. This environment variable is read from the `config/secrets.yml` file in your Rails app.

  1. Generate a new secret key.
         
         bundle exec bin/rails secret
         

  2. Copy the generated secret key.

  3. Open the `app.yaml` file that you created earlier, and add an `env_variables` section. The `env_variables` defines environment variables in the App Engine flexible environment. The `app.yaml` file should look similar to the following example with `[SECRET_KEY]` replaced with your secret key.
         
         entrypoint: bundle exec rackup --port $PORT
         env: flex
         runtime: ruby
         
         env_variables:
           SECRET_KEY_BASE: [SECRET_KEY]




### Configure the Cloud SQL instance in the `app.yaml` file

Next, configure the App Engine flexible environment to use a specified Cloud SQL instance by providing the Cloud SQL instance connection name in the `app.yaml` configuration file.

  1. Open the `app.yaml` file, and add a new section named `beta_settings`.

  2. Define a nested parameter `cloud_sql_instances` with the instance connection name as the value.

**Note:** You can retrieve the Cloud SQL instance connection name by running `gcloud sql instances describe rails-cloudsql-instance`.

The `app.yaml` should look similar to the following:
         
         entrypoint: bundle exec rackup --port $PORT
         env: flex
         runtime: ruby
         
         env_variables:
           SECRET_KEY_BASE: [SECRET_KEY]
         
         beta_settings:
           cloud_sql_instances: [YOUR_INSTANCE_CONNECTION_NAME]




### Create an App Engine flexible environment app

If this is the first time you are deploying an app, you need to create an App Engine flexible environment app and select the region where you want to run the Rails app.

  1. Create an App Engine app.
         
         gcloud app create
         

  2. Select a region that supports App Engine flexible environment for Ruby apps. Read more about [Regions and zones](https://docs.cloud.google.com/docs/geography-and-regions).




### Deploy a new version

Next, deploy a new version of the Rails app described in the `app.yaml` file without redirecting traffic from the current default serving version.

  1. Precompile the Rails assets.
         
         bundle exec bin/rails assets:precompile
         

  2. After the assets finish compiling, deploy a new version of the app.
         
         gcloud app deploy --no-promote
         

It can take several minutes to finish the deployment. Wait for a success message. You can view deployed versions in the App Engine [version list](https://console.cloud.google.com/appengine/versions).


**Warning:** The older versions of your app remain, as do their associated VM instances. Be aware that all of these app versions and VM instances are billable resources.

After you deploy the new version, if you attempt to access this new version, it shows the following error message because you haven't migrated the database.

![Screenshot of new Rails app error message](https://docs.cloud.google.com/static/ruby/images/rails-error-message.png)

### Grant required permission for the `appengine` gem

Next, grant access to the cloudbuild service account to run production database migrations with the `appengine` gem.

  1. List available projects.
         
         gcloud projects list
         

  2. In the output, find the project you want to use to deploy your app, and copy the project number.

  3. Add a new member to your project IAM policy for the role `roles/editor` to run database migrations. Replace `PROJECT_ID` with your Google Cloud project ID and replace `PROJECT_NUMBER` with the project number you copied in the previous step.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=serviceAccount:PROJECT_NUMBER@cloudbuild.gserviceaccount.com \
           --role=roles/editor
         




### Migrate your Rails database

Rails database migrations are used to update the schema of your database without using SQL syntax directly. Next you migrate your `cat_list_production` database.

The `appengine` gem provides the Rake task `appengine:exec` to run a command against the most recent deployed version of your app in the production App Engine flexible environment.

  1. Migrate the Cloud SQL for MySQL `cat_list_production` database in production.
         
         bundle exec rake appengine:exec -- bundle exec rake db:migrate
         

You should see output similar to:
         
         ---------- EXECUTE COMMAND ----------
         bundle exec rake db:migrate
         Debuggee gcp:787021104993:8dae9032f8b02004 successfully registered
         == 20230922063608 CreateCats: migrating =======================================
         -- create_table(:cats)
            -> 0.0219s
         == 20230922063608 CreateCats: migrated (0.0220s) ==============================
         
         ---------- CLEANUP ----------
         

**Note:** If a permission error occurs when attempting to run database migrations, verify that `PROJECT_NUMBER@cloudbuild.gserviceaccount.com` has the `roles/editor` role.
  2. To verify the database migration, go to:

VERSION-dot-PROJECT_ID.appspot.com

**Note:** To get a list of versions, use `gcloud app versions list`. The last **default** service version item is the latest deployment.



The following is displayed for a successful deployment:

![Screenshot of new Rails app running](https://docs.cloud.google.com/static/ruby/images/new-rails-app-cloudsql.png)

### Migrate traffic to new version

Finally, direct traffic to your newly deployed version by using the following command:
    
    
    gcloud app services set-traffic default --splits VERSION=1
    

The new version of the app is now accessible from:
    
    
    https://PROJECT_ID.appspot.com
    

## Reading App Engine logs

Now that you have deployed your Rails app, you might want to read the logs. You can read the app logs by using the [Logs Explorer](https://console.cloud.google.com/logs/query) located in the Google Cloud console.

You can learn more about [reading logs using the gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/app/logs/read).

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



### Delete a Cloud SQL instance

To delete a Cloud SQL instance: 

  1. In the Google Cloud console, go to the **Instances** page. 

[Go to Instances](https://console.cloud.google.com/sql/instances)

  2. Click the name of the SQL instance you that want to delete. 
  3. To delete the instance, click delete **Delete** , and then follow the instructions. 



## What's next

  * Learn how to [run the Ruby Bookshelf sample app in the App Engine flexible environment](https://docs.cloud.google.com/ruby/getting-started/tutorial-app).

  * Learn how to [run the Ruby Bookshelf sample app on Compute Engine](https://docs.cloud.google.com/ruby/tutorials/bookshelf-on-compute-engine).

  * Learn how to [run the Ruby Bookshelf sample app on Google Kubernetes Engine](https://docs.cloud.google.com/ruby/tutorials/bookshelf-on-kubernetes-engine).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
