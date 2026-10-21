---
url: https://docs.cloud.google.com/php/tutorials/wordpress-app-engine-flexible/
title: Hosting WordPress in the App Engine flexible environment \u00a0|\u00a0 PHP \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:34:49.350756+00:00
---

# Hosting WordPress in the App Engine flexible environment  |  PHP  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/tutorials/wordpress-app-engine-flexible/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Guides ](https://docs.cloud.google.com/php/getting-started)



Send feedback 

#  Hosting WordPress in the App Engine flexible environment Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to deploy a small WordPress site to the App Engine flexible environment.

## Objectives

  * Create a Cloud SQL Second Generation instance.
  * Configure a sample WordPress site.
  * Deploy the sample WordPress site to the App Engine flexible environment.



## Costs

**Important:** In this document, you use the following billable components of Google Cloud: 

  * [App Engine](https://docs.cloud.google.com/appengine/pricing)
  * [Cloud SQL](https://docs.cloud.google.com/sql/pricing)

To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the required APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin,compute_component)

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

  10. Enable the required APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin,compute_component)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Create credentials by following these steps: 
     * In the Google Cloud console, go to the **Credentials** page.

[Open the API Credentials Page](https://console.cloud.google.com/apis/credentials/)

     * Click **Create credentials** and select **Service account key**.
     * Select **Service account > App Engine default service account**.
     * Click **Create**.
     * Save the downloaded key in a secure place.
  15. Install [PHP](http://php.net/manual/en/install.php) and [Composer](https://getcomposer.org). 
  16. [Download the Cloud SQL Proxy](https://docs.cloud.google.com/sql/docs/mysql-connect-proxy#install) and make it executable. Also add the location of the Cloud SQL Proxy executable file to your `PATH` environment variable. 
  17. Install a [MySQL client](https://www.mysql.com) and verify that the location of the `mysql` executable file is in your `PATH` environment variable. 



## Creating and configuring a Cloud SQL Second Generation instance

  1. Create a Cloud SQL Second Generation instance:
         
         gcloud sql instances create tutorial-sql-instance \
             --activation-policy=ALWAYS \
             --tier=db-n1-standard-1 \
             --region=us-central1
         

  2. Set the root password for your instance:
         
         gcloud sql users set-password root --instance tutorial-sql-instance \
             --password [YOUR_SQL_ROOT_PASSWORD] \
             --host %
         

where `[YOUR_SQL_ROOT_PASSWORD]` is a secure password of your choice.

  3. Download and run the [Cloud SQL Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy#install):
         
         ./cloud-sql-proxy \
             -dir /tmp/cloudsql \
             -instances=[YOUR_PROJECT_ID]:us-central1:tutorial-sql-instance \
             -credential_file=[PATH_TO_YOUR_SERVICE_ACCOUNT_JSON]

where

     * `[YOUR_PROJECT_ID]` is your Google Cloud project ID.

     * `[PATH_TO_YOUR_SERVICE_ACCOUNT_JSON]` is the path to the service account JSON file that you downloaded previously.

The following output indicates that the proxy is ready for new connections:
    
    Listening on 127.0.0.1:3306 for [YOUR_PROJECT_ID]:us-central1:tutorial-sql-instance
    Ready for new connections
    

  4. In another terminal window, create a new database and a user:
         
         mysql -h 127.0.0.1 -u root --password=[YOUR_SQL_ROOT_PASSWORD]
         mysql> create database tutorialdb;
         mysql> create user 'tutorial-user'@'%' identified by '[YOUR_DATABASE_PASSWORD]';
         mysql> grant all on tutorialdb.* to 'tutorial-user'@'%';
         mysql> exit

where:

     * `[YOUR_SQL_ROOT_PASSWORD]` is the root password for your Cloud SQL instance.
     * `[YOUR_DATABASE_PASSWORD]` is a secure password of your choice.



## Setting up the WordPress project

  1. Clone the sample repository:
         
         git clone https://github.com/GoogleCloudPlatform/php-docs-samples.git
         

  2. Go to the directory that contains the sample code:
         
         cd php-docs-samples/appengine/flexible/wordpress
         

  3. Install dependencies:
         
         composer install
         

  4. Run the helper script:
         
         php wordpress.php setup -n \
             --dir=./wordpress-project \
             --db_instance=tutorial-sql-instance \
             --db_name=tutorialdb \
             --db_user=tutorial-user \
             --project_id=[YOUR_PROJECT_ID] \
             --db_password=[YOUR_DATABASE_PASSWORD]

where:

     * `[YOUR_PROJECT_ID]` is your project ID.
     * `[YOUR_DATABASE_PASSWORD]` is your database password.

The `-dir` parameter specifies the location of your WordPress project.

  5. The helper script writes information to `wordpress-project/wordpress/wp-config.php`. Inspect the content of `wp-config.php` to verify that your names, project ID, and database password are correct.
         
         if ($onGae) {
             /** Production environment */
             define('DB_HOST', ':/cloudsql/[YOUR_PROJECT_ID]:us-central1:tutorial-sql-instance');
             /** The name of the database for WordPress */
             define('DB_NAME', 'tutorialdb');
             /** MySQL database username */
             define('DB_USER', 'tutorial-user');
             /** MySQL database password */
             define('DB_PASSWORD', '[YOUR_DATABASE_PASSWORD]');
         } else {
             /** Local environment */
             define('DB_HOST', '127.0.0.1');
             /** The name of the database for WordPress */
             define('DB_NAME', 'tutorialdb');
             /** MySQL database username */
             define('DB_USER', 'tutorial-user');
             /** MySQL database password */
             define('DB_PASSWORD', '[YOUR_DATABASE_PASSWORD]');
         }




## Deploying the WordPress project to the App Engine flexible environment

  1. Go to your WordPress project directory:
         
         cd wordpress-project
         

  2. Deploy the WordPress project:
         
         gcloud app deploy \
             --promote --stop-previous-version app.yaml cron.yaml
         

  3. In your browser, enter the following URL:

`https://PROJECT_ID.REGION_ID.r.appspot.com`

Replace the following:

     * `PROJECT_ID`: Your Google Cloud project ID
     * `REGION_ID`: A [code that App Engine assigns to your app](https://docs.cloud.google.com/appengine/docs/flexible/php/how-requests-are-routed#region-id)



## Updating WordPress, plugins, and themes

It's important to keep WordPress, plugins, and themes up to date. You can keep these items updated by using the `wp` tool. After an update, you need to re- deploy the WordPress project.

  1. Update WordPress itself:
         
         vendor/bin/wp core update --path=wordpress
         

  2. Update plugins:
         
         vendor/bin/wp plugin update --all --path=wordpress
         # Just in case it updates any of the dropins, copy the files:
         cp wordpress/wp-content/plugins/batcache/advanced-cache.php \
             wordpress/wp-content/plugins/memcached/object-cache.php \
             wordpress/wp-content
         

  3. Update themes:
         
         vendor/bin/wp theme update --all --path=wordpress
         

  4. Deploy the project again:
         
         gcloud app deploy \
             --promote --stop-previous-version app.yaml cron.yaml
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

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



### Delete non-default versions of your app

If you don't want to delete your project, you can reduce costs by deleting the non-default versions of your app.

To delete an app version: 

  1. In the Google Cloud console, go to the **Versions** page for App Engine. 

[Go to Versions](https://console.cloud.google.com/appengine/versions)

  2. Select the checkbox for the non-default app version that you want to delete. **Note:** The only way you can delete the default version of your App Engine app is by deleting your project. However, you can [stop the default version in the Google Cloud console](https://console.cloud.google.com/appengine/versions). This action shuts down all instances associated with the version. You can restart these instances later if needed. 

In the App Engine standard environment, you can stop the default version only if your app has manual or basic scaling. 

  3. To delete the app version, click delete **Delete**. 



### Delete your Cloud SQL instance

To delete a Cloud SQL instance: 

  1. In the Google Cloud console, go to the **Instances** page. 

[Go to Instances](https://console.cloud.google.com/sql/instances)

  2. Click the name of the SQL instance you that want to delete. 
  3. To delete the instance, click delete **Delete** , and then follow the instructions. 



## What's next

  * Learn how to [run the PHP Bookshelf sample app in the App Engine flexible environment](https://docs.cloud.google.com/php/getting-started/tutorial-app).

  * Learn how to [run the PHP Bookshelf sample app on Google Kubernetes Engine](https://docs.cloud.google.com/php/tutorials/bookshelf-on-kubernetes-engine).

  * Learn how to [run the PHP Bookshelf sample app on Compute Engine](https://docs.cloud.google.com/php/tutorials/bookshelf-on-compute-engine).

  * Learn about [WordPress](https://wordpress.org/).

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
