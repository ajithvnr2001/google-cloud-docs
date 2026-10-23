---
url: https://docs.cloud.google.com/sql/docs/mysql/phpmyadmin-on-app-engine/
title: Use phpMyAdmin with Cloud SQL on App Engine standard environment \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:40.963954+00:00
---

# Use phpMyAdmin with Cloud SQL on App Engine standard environment  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/phpmyadmin-on-app-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use phpMyAdmin with Cloud SQL on App Engine standard environment Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to install phpMyAdmin on App Engine standard environment. You can use phpMyAdmin to administer Cloud SQL over the web. 

You will find this tutorial helpful if you:

  * Run applications on App Engine.
  * Use [Cloud SQL](https://docs.cloud.google.com/sql/docs) as your database.
  * Use phpMyAdmin as an interface for MySQL or you prefer a web interface for database administration.

**Note:** This tutorial only applies to MySQL version 5.7 or lower.

If you use Compute Engine, consider using one of the development stacks or products available through Click to Deploy. Deployments of stacks that include MySQL, such as [LAMP](https://docs.cloud.google.com/marketplace/solution/click-to-deploy-images/lamp) and [LEMP](https://docs.cloud.google.com/marketplace/solution/click-to-deploy-images/lemp), or products such as [Drupal](https://docs.cloud.google.com/marketplace/solution/click-to-deploy-images/drupal), provide an option to install phpMyAdmin as part of the deployment.

## Objectives

  * Deploy phpMyAdmin on App Engine standard environment.



## Costs

This tutorial uses billable components of Cloud Platform, including:

  * App Engine
  * Cloud SQL



Use the [Pricing Calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage. 

New Cloud Platform users might be eligible for a [free trial](https://cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Create a [Cloud SQL Second Generation instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen).
  13. (Optional) Deploy an App Engine application that uses your Cloud SQL instance or select an existing application. 

For example, [create and deploy the guestbook sample](https://docs.cloud.google.com/appengine/docs/php/cloud-sql). Although you can deploy phpMyAdmin on its own, you'll probably want to use it with an App Engine application in your real-world scenario. 




## Download the phpMyAdmin source code

You'll deploy phpMyAdmin as a service of your App Engine application, so you must download the source code for phpMyAdmin. Follow these steps:

  1. In a Cloud Shell terminal, enter the following command to download the source code for phpMyAdmin version 4.9.5:
         
         wget https://files.phpmyadmin.net/phpMyAdmin/4.9.5/phpMyAdmin-4.9.5-all-languages.tar.gz
         

To use a different version of phpMyAdmin, use the links to available versions on the [phpMyAdmin Downloads page](http://www.phpmyadmin.net/home_page/downloads.php).

  2. Make a new directory. You will extract the files into this directory.
         
         mkdir phpMyAdmin
         

  3. Extract the files from the archive into the new directory.
         
         tar -xzvf phpMyAdmin-4.9.5-all-languages.tar.gz -C phpMyAdmin --strip-components=1
         




## Prepare the files for deployment

Deploying phpMyAdmin requires that you create three files: `app.yaml`, which contains the configuration information for App Engine; `config.inc.php`, which contains the configuration information for phpMyAdmin; and `php.ini`, which contains application-specific configuration for PHP.

### Create `app.yaml`

The [App Engine configuration file](https://docs.cloud.google.com/appengine/docs/php/config/appconfig) specifies how URL paths correspond to request handlers and static files. It also contains information about the application code, such as the application ID and the latest version identifier. Follow these steps to create the file:

  1. In the directory that you created, named `phpMyAdmin`, create a new file named `app.yaml`.
         
         cd phpMyAdmin
         touch app.yaml
         

  2. Using your favorite editor, paste the following text into `app.yaml`.
         
         service: phpmyadmin
         runtime: php55
         api_version: 1
         
         handlers:
         
         - url: /(.+\.(ico|jpg|png|gif))$
           static_files: \1
           upload: (.+\.(ico|jpg|png|gif))$
           application_readable: true
         
         - url: /(.+\.(htm|html|css|js))$
           static_files: \1
           upload: (.+\.(htm|html|css|js))$
           application_readable: true
         
         - url: /(.+\.php)$
           script: \1
           login: admin
         
         - url: /.*
           script: index.php
           login: admin
         

  3. If you are deploying phpMyAdmin as the first and only application in App Engine, change the value for `service` from `phpmyadmin` to `default`.

Normally, you would deploy phpMyAdmin as a service of an existing application and provide a name for the service. However, if you haven't yet deployed an application, then you are required to use the service name "default". That's fine for the purposes of this tutorial if you're trying out phpMyAdmin on App Engine.

This tutorial works only for App Engine standard environment.

  4. Save the file.




### Create `config.inc.php`

Follow these steps to create the phpMyAdmin configuration file.

  1. Create a new file named `config.inc.php`.
         
         touch config.inc.php
         

  2. Using your favorite editor, paste the following text into `config.inc.php`.
         
         <?php
         /**
          * Copyright 2016 Google Inc.
          *
          * Licensed under the Apache License, Version 2.0 (the "License");
          * you may not use this file except in compliance with the License.
          * You may obtain a copy of the License at
          *
          *     http://www.apache.org/licenses/LICENSE-2.0
          *
          * Unless required by applicable law or agreed to in writing, software
          * distributed under the License is distributed on an "AS IS" BASIS,
          * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
          * See the License for the specific language governing permissions and
          * limitations under the License.
          */
         /*
          * This is needed for cookie based authentication to encrypt password in
          * cookie
          * http://www.question-defense.com/tools/phpmyadmin-blowfish-secret-generator
          */
         $cfg['blowfish_secret'] = '{{your_secret}}'; /* YOU MUST FILL IN THIS FOR COOKIE AUTH! */
         
         /*
          * Servers configuration
          */
         $i = 0;
         
         // Change this to use the project and instance that you've created.
         $host = '/cloudsql/{{your_connection_string}}';
         $type = 'socket';
         
         /*
         * First server
         */
         $i++;
         /* Authentication type */
         $cfg['Servers'][$i]['auth_type'] = 'cookie';
         /* Server parameters */
         $cfg['Servers'][$i]['socket'] = $host;
         $cfg['Servers'][$i]['connect_type'] = $type;
         $cfg['Servers'][$i]['compress'] = false;
         /* Select mysql if your server does not have mysqli */
         $cfg['Servers'][$i]['extension'] = 'mysqli';
         $cfg['Servers'][$i]['AllowNoPassword'] = true;
         /*
          * End of servers configuration
          */
         
         /*
          * Directories for saving/loading files from server
          */
         $cfg['UploadDir'] = '';
         $cfg['SaveDir'] = '';
         
         /*
         * Other settings
         */
         $cfg['PmaNoRelation_DisableWarning'] = true;
         $cfg['ExecTimeLimit'] = 60;
         $cfg['CheckConfigurationPermissions'] = false;
         

  3. Open Google Cloud Shell and execute the following to get a random string for your blowfish:
         
         php -r "echo password_hash(uniqid(), PASSWORD_BCRYPT).PHP_EOL;"
         

  4. Paste the new secret in place of `{{your_secret}}` in `config.inc.php`.

  5. Go to the [Cloud SQL instances page](https://console.cloud.google.com/sql/instances) in the Google Cloud console.

  6. Click the Cloud SQL instance to display its Instance details page.

  7. Replace the value of `{{your_connection_string}}` (within the `$host` variable) with the **Instance connection name** property.

  8. Save the file.




### Create `php.ini`

In its code, phpMyAdmin uses functions that are disabled by default in App Engine. Follow these steps to add a `php.ini` file so that App Engine enables the functions again:

  1. In the `phpMyAdmin` directory, create the file.
         
         touch php.ini
         

  2. Edit the file and add the following line:
         
         google_app_engine.enable_functions = "php_uname, getmypid"
         

  3. Save the file.




## Deploy the application

Use the following commands to deploy your application to App Engine.

  1. Check for updates for your `gcloud` components.
         
         gcloud components update
         

  2. Deploy the application by running the following command from within the `phpMyAdmin` directory where your `app.yaml` file is located:
         
         gcloud app deploy
         

This command deploys the app to the `phpMyAdmin` service, as specified your `app.yaml` file. Deploying to a separate service helps to ensure that phpMyAdmin runs in the same data center as your main application, which improves performance. To learn more about deploying your app from the command line, see [Deploying a PHP App](https://docs.cloud.google.com/appengine/docs/php/tools/uploadinganapp).




## Log in to phpMyAdmin

You can now log in to phpMyAdmin.

  1. In your web browser, enter the URL for phpMyAdmin to open the welcome page, changing the URL to use your app ID.
         
         https://phpmyadmin-dot-[YOUR_APP_ID].appspot.com
         

  2. For **Username** , enter **root**.

  3. Enter the root password you provided when you configured the root account.

  4. Click **Go**.




As you develop your App Engine app, remember to password protect any user accounts that you create to access databases in Cloud SQL.

## Troubleshoot

App Engine uses the Cloud SQL Auth Proxy to connect to Cloud SQL Second Generation instances. For more information about how the Cloud SQL Auth Proxy works, see [About the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy).

The [App Engine logs](https://console.cloud.google.com/logs) in the [Google Cloud console](https://console.cloud.google.com/) can provide information about App Engine errors.

## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

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



### Delete instances

To delete a Cloud SQL instance: 

  1. In the Google Cloud console, go to the **Instances** page. 

[Go to Instances](https://console.cloud.google.com/sql/instances)

  2. Click the name of the SQL instance you that want to delete. 
  3. To delete the instance, click delete **Delete** , and then follow the instructions. 



## What's next

  * [Learn more about phpMyAdmin](http://www.phpmyadmin.net/home_page/docs.php).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
