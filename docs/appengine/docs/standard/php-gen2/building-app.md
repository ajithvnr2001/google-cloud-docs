---
url: https://docs.cloud.google.com/appengine/docs/standard/php-gen2/building-app/
title: Building an app with PHP \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:50.392941+00:00
---

# Building an app with PHP  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/php-gen2/building-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Building an app with PHP Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

**Note:** If you are deploying a new PHP web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-php-service).

Learn how to build an app in App Engine using either PHP version 7.4 or 8.1. The sample app allows users to post the titles, authors, descriptions, publication date, and images of their favorite books to a webpage. The app stores the textual data in a Cloud SQL database and the images in a Cloud Storage bucket.

## Guide structure

  1. Create a Google Cloud project using the Google Cloud CLI

  2. Download the sample app

  3. Specify dependencies with composer.json

  4. Initialize the app and defining front controllers

  5. Integrate with Google Cloud services

  6. Configure the app for App Engine

  7. Deploy the app




## Before you begin

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

  14. Install [Composer](https://getcomposer.org/doc/00-intro.md), the PHP dependency management tool. You must [install Composer globally](https://getcomposer.org/doc/00-intro.md#globally) on Linux and Mac OS X systems.
  15. Due to [changes in the default behavior for how Cloud Build uses service accounts](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates) in new projects, and [secure-by-default organization policy changes](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations), you might need to grant additional roles to your deploying service account. For more information on granting specific roles, see the [troubleshooting guide](https://docs.cloud.google.com/appengine/docs/standard/troubleshooter/deployment#default-sa-permissions).



## Download the sample app

  1. Explore the code on [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/appengine/standard/getting-started)

  2. Download or clone the app.
         
         git clone https://github.com/GoogleCloudPlatform/php-docs-samples.git

Or [download the sample](https://github.com/GoogleCloudPlatform/php-docs-samples/archive/master.zip) as a zip file and extract it.

  3. Navigate to the `getting-started` directory.
         
         cd php-docs-samples/appengine/standard/getting-started




## Specify dependencies with composer.json

The app uses a front controller to route requests. The sample code in this guide uses the [Slim Framework](https://www.slimframework.com/), but you are free to use a web framework of your choice.

  1. Open the `composer.json` file to review all direct dependencies:
         
         {
           "require": {
             "google/cloud-storage": "^1.6",
             "slim/slim": "^4.0",
             "slim/psr7": "^1.0",
             "slim/twig-view": "^3.0",
             "php-di/slim-bridge": "^3.1",
             "symfony/yaml": "^5.2"
           },
           "autoload": {
              "psr-4": {
                "Google\\Cloud\\Samples\\AppEngine\\GettingStarted\\": "src"
              }
           }
         }
         

  2. To install your dependencies and produce a `composer.lock` file, run the following command:
         
         composer install
         

The `composer.lock` file helps your app to retrieve the same versions of the packages you use across multiple builds and environments.

**Note:** Because Cloud Build operates in a limited memory environment, you are recommended to produce the `composer.lock` file locally. For more information, see [Specifying Dependencies](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/specifying-dependencies).



## Initialize the app and defining front controllers

The `index.php` file initializes the app and forwards all requests to controllers defined in the `./src/controllers.php` file.
    
    
    // Use the composer autoloader to load dependencies.
    require_once __DIR__ . '/vendor/autoload.php';
    
    //  Load the application code.
    /** @var Slim\App $app */
    $app = require __DIR__ . '/src/app.php';
    require __DIR__ . '/src/controllers.php';
    
    // Bootstrap the slim framework to handle the request.
    $app->run();
    

For more on request handling, read about [application startup](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime#application_startup) and [handling requests](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled).

## Integrating with Google Cloud services

App Engine requires apps to integrate with external systems for data storage. The sample app stores textual data on [Cloud SQL](https://docs.cloud.google.com/sql) and images on [Cloud Storage](https://docs.cloud.google.com/storage).

See the [Choosing a Storage Option page](https://docs.cloud.google.com/storage-options) for all Google Cloud storage options.

### Using Cloud SQL

In the sample app, users post books to a webpage. The app uses a Cloud SQL database to store the titles, authors, publication date, and descriptions of the books.

You will need to create a Cloud SQL instance before adding content to the app's database.

#### Creating a Cloud SQL instance

Use the gcloud CLI to create a Cloud SQL instance:
    
    
    gcloud sql instances create INSTANCE_NAME --tier=MACHINE_TYPE --region=REGION

For example, if you want to name your instance `bookshelf` and use the machine type of `db-n1-standard-2` in the United States central region:
    
    
    gcloud sql instances create bookshelf --tier=db-n1-standard-2 --region=us-central1

**Learn More** : 

  * For more information about creating a Cloud SQL instance,read the [Cloud SQL creating instances guide](https://docs.cloud.google.com/sql/docs/mysql/create-instance).
  * For information about instance locations, machine types, and their effects on pricing, see the [Cloud SQL pricing page](https://docs.cloud.google.com/sql/pricing#2nd-gen-pricing).



#### Setting up the MySQL root user

You can use the gcloud CLI to set the root user's password of your Cloud SQL instance:
    
    
    gcloud sql users set-password USER --host=HOST --instance=INSTANCE_NAME --password=PASSWORD

For example, if you want to set the root user's password for the Cloud SQL instance `bookshelf` to `passw0rd!`:
    
    
    gcloud sql users set-password root --host=% --instance=bookshelf --password=passw0rd!

**Learn more** : For more information, read the [Cloud SQL creating and managing MySQL users guide](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users). 

#### Setting up a database on the Cloud SQL instance

To store the authors, titles, publication date, and descriptions of the books, create a MySQL database:
    
    
    gcloud sql databases create DATABASE_NAME --instance=INSTANCE_NAME

For example, if you want to create a database called `book-data` on the Cloud SQL instance `bookshelf`:
    
    
    gcloud sql databases create book-data --instance=bookshelf

**Learn more** : For more information, read the [Cloud SQL creating and managing MySQL databases guide](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases). 

#### Connecting to Cloud SQL database

The sample app uses PHP's [PDO](http://php.net/manual/en/intro.pdo.php) to interact with the MySQL database.
    
    
    // Fill the variables below to match your Cloud SQL configuration.
    // $dbConn = 'YOUR_CLOUDSQL_CONNECTION_NAME';
    // $dbName = 'YOUR_CLOUDSQL_DATABASE_NAME';
    // $dbUser = 'YOUR_CLOUDSQL_USER';
    // $dbPass = 'YOUR_CLOUDSQL_PASSWORD';
    $dsn = "mysql:unix_socket=/cloudsql/{$dbConn};dbname={$dbName}";
    $pdo = new PDO($dsn, $dbUser, $dbPass);

For this tutorial, these parameters are specified as environment variables below in Configuring the app.

#### Querying a single row

When the user clicks on a book, the app queries the database and returns a single row that includes the title, author, publication date, and description of the book.
    
    
    $statement = $pdo->prepare('SELECT * FROM books WHERE id = :id');
    $statement->bindValue('id', $id, PDO::PARAM_INT);
    $statement->execute();
    $result = $statement->fetch(PDO::FETCH_ASSOC);

**Learn more** : For more information about how to use Cloud SQL from the PHP runtimes, read the [Using Cloud SQL for MySQL guide](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine). 

### Using Cloud Storage

The sample app uses Cloud Storage to store the images, which are binary files, uploaded by users.

#### Creating a Cloud Storage bucket

Cloud Storage uses buckets to organize and control access to your data.

Use gcloud CLI to create a Cloud Storage bucket:
    
    
    gcloud storage buckets create gs://BUCKET_NAME/ --location=BUCKET_REGION

For example, if you want to create a bucket called `picture-storage` in the `us-central1` region:
    
    
    gcloud storage buckets create gs://picture-storage/ --location=us-central1

**Note:** `picture-storage` will be unavailable as a bucket name since it has already been used. [See bucket naming requirements _help_outline_](https://docs.cloud.google.com/storage/docs/buckets#naming)

  * If successful, you see the following output:
        
        Creating gs://BUCKET_NAME/

  * If not successful, you might see the following output:
        
        ServiceException: 409 Bucket BUCKET_NAME already exists

Try again with a different bucket name.

**Learn more** : For more information, read [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-console).



#### Connecting a project to a Cloud Storage bucket

To use Cloud Storage, you need to specify the [Cloud Storage library](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/readme).
    
    
    use Google\Cloud\Storage\StorageClient;
    

#### Storing images

Now that you have created a Cloud Storage bucket and set up a connection, you can store images. Images can be uploaded with [predefined access controls lists (ACL)](https://docs.cloud.google.com/storage/docs/access-control/lists#predefined-acl) to control access to the images.

In this sample app, uploaded images will have the predefined ACL `public-read`. The public URL can be accessed via the `mediaLink` property of your Cloud Storage object. You can use this URL in an HTML image tag.
    
    
    // Set your own image file path and content type below to upload an
    // image to Cloud Storage.
    // $imageStream = fopen('/path/to/your_image.jpg', 'r');
    // $imageContentType = 'image/jpg';
    $object = $bucket->upload($imageStream, [
        'metadata' => ['contentType' => $imageContentType],
        'predefinedAcl' => 'publicRead',
    ]);
    $imageUrl = $object->info()['mediaLink'];

For instructions on how to read a private Cloud Storage object, see [Downloading Objects page](https://docs.cloud.google.com/storage/docs/downloading-objects).

#### Deleting images

When a user deletes a book from the app, this code removes the image from the Cloud Storage bucket.
    
    
    $object = $bucket->object($objectName);
    $object->delete();

## Configuring the app

You configure applications to run on App Engine using an [app.yaml file](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/configuring-your-app-with-app-yaml), which specifies the application's runtime, environment variables, and other settings.

For an app with minimal configuration requirements, the `app.yaml` file can be a single line:

### PHP 8.1
    
    
    runtime: php81
    

### PHP 7.4
    
    
    runtime: php74
    

You can add further configuration options and application-specific environment variables into the `app.yaml` configuration file.

### Adding environment variables

The `app.yaml` file is where environment configuration is provided to the app. The bookshelf example used in this guide needs configuration provided as environment variables to know how to connect to the correct Cloud SQL instance and Cloud Storage bucket.

To deploy your app, you need to edit the `app.yaml` configuration file:
    
    
    # See https://cloud.google.com/appengine/docs/standard/php/config/appref for a
    # complete list of `app.yaml` directives.
    
    runtime: php84
    
    env_variables:
        GOOGLE_STORAGE_BUCKET: ""
        # populate these to use the "mysql" or "postres" backends
        CLOUDSQL_CONNECTION_NAME: ""
        CLOUDSQL_USER: ""
        CLOUDSQL_PASSWORD: ""
        ## Uncomment to give your database a name other than "bookshelf"
        # CLOUDSQL_DATABASE_NAME: ""
    

  1. Set the `GOOGLE_STORAGE_BUCKET` variable to the name of your Cloud Storage bucket.

  2. Set the `CLOUDSQL_CONNECTION_NAME` variable to app-name:region:instance-name You can retrieve the necessary details by using the following `gcloud` command:
         
         gcloud sql instances describe INSTANCE

For a Cloud SQL Second Generation instance, the `CLOUDSQL_CONNECTION_NAME` will be in the following format: `your_project_name:your_region:your_instance`

  3. Uncomment and set the `CLOUD_SQL_DATABASE_NAME` variable if the database you have created has a name other than `bookshelf`. In this example, te database was created with the name `book-data`.

  4. Review your `app.yaml` file, which should look something like:




### PHP 8.1
    
    
    runtime: php81
    
    env_variables:
      GOOGLE_STORAGE_BUCKET: picture-storage
      CLOUDSQL_CONNECTION_NAME: sample-application:us-central1:bookshelf
      CLOUDSQL_USER: root
      CLOUDSQL_PASSWORD: passw0rd!
      CLOUDSQL_DATABASE_NAME: book-data
    

### PHP 7.4
    
    
    runtime: php74
    
    env_variables:
      GOOGLE_STORAGE_BUCKET: picture-storage
      CLOUDSQL_CONNECTION_NAME: sample-application:us-central1:bookshelf
      CLOUDSQL_USER: root
      CLOUDSQL_PASSWORD: passw0rd!
      CLOUDSQL_DATABASE_NAME: book-data
    

**Note:** You should encrypt sensitive data such as passwords and not put them in the `app.yaml` as plaintext. For production apps, use [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs) to store credentials.

## Deploying the application

  1. To deploy the application, navigate to the `getting-started` directory and run the following command:
         
         gcloud app deploy

  2. When the location prompt appears, choose a location near your app users. App Engine is regional, which means the infrastructure that runs your app is located in a specific geographic area. For example, this tutorial has used the `us-central1` region to deploy its storage resources. Deploy the app in the same region to decrease latency and improve performance.

In general, choosing a location near your users is a good idea, but there are cases when deploying your application near where its resources are located is recommended. Read about the available [App Engine locations](https://docs.cloud.google.com/appengine/docs/standard/locations) and [resource locations](https://cloud.google.com/about/locations/#locations).

  3. View the application:
         
         gcloud app browse




## Cleaning up

Delete your Google Cloud project to stop the billing for the resources used within the project.

**Note:** You can't delete the default app.**Warning:** Deleting a project has the following consequences: 

  * If you used an existing project, you'll also delete any other work you've done in the project.
  * You can't reuse the project ID of a deleted project. If you created a custom project ID that you plan to use in the future, delete the resources inside the project instead. This ensures that URLs with the project ID such as `https://PROJECT_ID.REGION_ID.r.appspot.com` remain available.



To deleted your project using the following command:
    
    
    gcloud projects delete PROJECT_ID

To verify the project was deleted, list your projects:
    
    
    gcloud projects list

## What's next

  * Learn how to [authenticate users](https://docs.cloud.google.com/appengine/docs/standard/authenticating-users).
  * Learn more about writing application logs and interpreting system logs in [Reading and writing application logs](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs).
  * Learn how to do work in the background asynchronously after your request using [Cloud Tasks](https://docs.cloud.google.com/tasks/docs).
  * Read about [request handling](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled) and [request routing](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed).
  * For a deeper dive into how App Engine works, see the [PHP runtime environment](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
