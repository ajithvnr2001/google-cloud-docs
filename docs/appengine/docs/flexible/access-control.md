---
url: https://docs.cloud.google.com/appengine/docs/flexible/access-control/
title: Setting up access control \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:58.638197+00:00
---

# Setting up access control  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Setting up access control Stay organized with collections  Save and categorize content based on your preferences. 

**Access control** determines who has permission to access services and resources in a Google Cloud project. In App Engine, there are a few separate use cases for setting up access control:

  * Granting team members access to your Google Cloud project so they can set up services and deploy apps.

  * Granting your app access to Google Cloud services, such as Cloud Storage. All Cloud services require authentication and authorization for every API call, including calls from your App Engine app.

  * Granting your users access to resources in a Google Cloud project. While this use case isn't common, there may be cases in which your app needs to request access to a Cloud resource on behalf of a user. For example, your app may need to access data that belongs to your users.




This page provides an overview of setting up access control in each use case.

For background information on how Google Cloud Platform handles access control, see the [overview of Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview).

**Note:** App Engine is not a supported service for [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), and can only be accessed using [Cloud Identity or Google Workspace accounts](https://docs.cloud.google.com/iam/docs/user-identities#google-accounts).

## Granting access to team members

To give a developer access to your Google Cloud project, create one or both of the following:

  * A user account, which is associated with a Google account and is intended to represent a specific individual on your project.

A user account can be used to authenticate from the following tools:

    * Google Cloud console
    * [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate#user-accounts)
    * IDEs and build tools that use the gcloud CLI to test and deploy App Engine apps
  * A service account, which is intended to represent an application or a process instead of a person. Use service accounts in your automated build, test, and deployment processes, especially if multiple developers can run these processes.

A service account can be used to authenticate from the following tools:

    * [gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate#service-accounts)
    * IDEs and build tools that use gcloud CLI tools to test and deploy App Engine apps



### Creating a user account

  1. Open the IAM page in the Google Cloud console. 

[Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Select a project** , choose a project, and click **Open**.

  3. Click **Add**.

  4. Enter an email address.

  5. Select roles that [grant access to App Engine features](https://docs.cloud.google.com/appengine/docs/flexible/roles).

If the user also needs access to other Cloud services, select [roles that grant access to other Cloud services](https://docs.cloud.google.com/iam/docs/understanding-roles).

  6. Click **Save**.




The user can now sign into Google Cloud console as well as [authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate#user-accounts).

You can also create user accounts [from gcloud, the REST API, or client libraries](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#updating-gcloud).

### Creating a service account

  1. Open the **Service Accounts** page in the Google Cloud console. 

[Open the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select your project and click **Open**.

  3. Click **Create Service Account**.

  4. Enter a service account name. This should be a user-friendly name for display.

  5. Click **Create**.

  6. Select roles that [grant access to App Engine features](https://docs.cloud.google.com/appengine/docs/flexible/roles).

If the service account also needs access to other Cloud services, select [roles that grant access to other Cloud services](https://docs.cloud.google.com/iam/docs/understanding-roles).

  7. Click **Continue**.

  8. Optionally, specify user accounts who can manage the service account. You can also specify user accounts who can use the service account to [indirectly access all the resources](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) to which the service account has access.

  9. Click **Save**.

A list of existing service accounts appears.

  10. Optionally, if you need to use your service account outside of Google Cloud, follow the instructions to [create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys).




#### Next steps

  * If you're using the service account in your automated build and deployment processes, [authenticate for the gcloud CLI with a service account](https://docs.cloud.google.com/sdk/docs/authenticate#service-accounts).
  * If you're using the service account with an IDE, follow the instructions provided by the IDE.
  * If you need to use a unique identity for a version of your App Engine app when accessing other Google Cloud services or executing tasks, you can specify a [user-managed service account](https://docs.cloud.google.com/appengine/docs/flexible/user-managed-service-accounts) in App Engine.



## Granting your app access to Cloud services

Every call to a Cloud service needs to be authenticated and authorized, including calls from an App Engine app to other Cloud services such as Cloud Storage.

By default, calls from your App Engine app to services in the same project are authorized. Here's how the default flow works:

  1. To initiate calls to a Cloud service, your app creates a client object, which contains the credentials and other data your app needs to interact with the service. If you don't specify credentials in the client's constructor, the client looks for credentials in the app's environment.

Here's an example of creating a client for Cloud Storage:

### Go
         
         // implicit uses Application Default Credentials to authenticate.
         func implicit() {
         	ctx := context.Background()
         
         	// For API packages whose import path is starting with "cloud.google.com/go",
         	// such as cloud.google.com/go/storage in this case, if there are no credentials
         	// provided, the client library will look for credentials in the environment.
         	storageClient, err := storage.NewClient(ctx)
         	if err != nil {
         		log.Fatal(err)
         	}
         	defer storageClient.Close()
         
         	it := storageClient.Buckets(ctx, "project-id")
         	for {
         		bucketAttrs, err := it.Next()
         		if err == iterator.Done {
         			break
         		}
         		if err != nil {
         			log.Fatal(err)
         		}
         		fmt.Println(bucketAttrs.Name)
         	}
         
         	// For packages whose import path is starting with "google.golang.org/api",
         	// such as google.golang.org/api/cloudkms/v1, use NewService to create the client.
         	kmsService, err := cloudkms.NewService(ctx)
         	if err != nil {
         		log.Fatal(err)
         	}
         
         	_ = kmsService
         }
         

### Java
         
         static void authImplicit() {
           // If you don't specify credentials when constructing the client, the client library will
           // look for credentials via the environment variable GOOGLE_APPLICATION_CREDENTIALS.
           Storage storage = StorageOptions.getDefaultInstance().getService();
         
           System.out.println("Buckets:");
           Page<Bucket> buckets = storage.list();
           for (Bucket bucket : buckets.iterateAll()) {
             System.out.println(bucket.toString());
           }
         }

### Node.js
         
         // Imports the Google Cloud client library.
         const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
         
         // Instantiates a client. If you don't specify credentials when constructing
         // the client, the client library will look for credentials in the
         // environment.
         const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
         // Makes an authenticated API request.
         async function listBuckets() {
           try {
             const results = await storage.[getBuckets](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html)();
         
             const [buckets] = results;
         
             console.log('Buckets:');
             buckets.forEach(bucket => {
               console.log(bucket.name);
             });
           } catch (err) {
             console.error('ERROR:', err);
           }
         }
         listBuckets();

### PHP
         
         // Imports the Cloud Storage client library.
         use Google\Cloud\Storage\StorageClient;
         
         /**
          * Authenticate to a cloud client library using a service account implicitly.
          *
          * @param string $projectId The Google project ID.
          */
         function auth_cloud_implicit($projectId)
         {
             $config = [
                 'projectId' => $projectId,
             ];
         
             # If you don't specify credentials when constructing the client, the
             # client library will look for credentials in the environment.
             $storage = new StorageClient($config);
         
             # Make an authenticated API request (listing storage buckets)
             foreach ($storage->buckets() as $bucket) {
                 printf('Bucket: %s' . PHP_EOL, $bucket->name());
             }
         }

### Python
         
         def implicit():
             from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         
             # If you don't specify credentials when constructing the client, the
             # client library will look for credentials in the environment.
             storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
         
             # Make an authenticated API request
             buckets = list(storage_client.[list_buckets](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_list_buckets)())
             print(buckets)
         
         

### Ruby
         
         # project_id = "Your Google Cloud project ID"
         
         require "google/cloud/storage"
         
         # If you don't specify credentials when constructing the client, the client
         # library will look for credentials in the environment.
         storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html) project: project_id
         
         # Make an authenticated API request
         storage.buckets.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |bucket|
           puts bucket.name
         end

### C#
         
         public object AuthImplicit(string projectId)
         {
             // If you don't specify credentials when constructing the client, the
             // client library will look for credentials in the environment.
             var credential = GoogleCredential.GetApplicationDefault();
             var storage = StorageClient.Create(credential);
             // Make an authenticated API request.
             var buckets = storage.ListBuckets(projectId);
             foreach (var bucket in buckets)
             {
                 Console.WriteLine(bucket.Name);
             }
             return null;
         }
         

  2. By default, the app's environment contains credentials from the [default App Engine service account](https://docs.cloud.google.com/appengine/docs/flexible/default-service-account). 

This service account is created by Google when you create an App Engine app and is given full permissions to manage and use all Cloud services in a Google Cloud project.




You can override this default flow by doing any of the following:

  * Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable. If this variable is set, Cloud services use the credentials specified by the variable instead of the default service account.

  * Specify credentials when you instantiate the `Client` object for a Cloud service. For example, if your app is calling a Cloud service in a different project, you may need to [pass credentials manually](https://docs.cloud.google.com/docs/authentication/production#passing_the_path_to_the_service_account_key_in_code).




If you set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable or pass credentials in your code, we recommend that you store your credentials in one of the following ways:

  * Store your credentials in a secure location such as Firestore in Datastore mode (Datastore) and retrieve them at runtime.
  * Keep the credentials in your code but encrypt them with a keystore, such as Cloud KMS.



To learn about the advantages of each approach, see [Choosing a secret management solution](https://docs.cloud.google.com/kms/docs/secret-management#choosing_a_secret_management_solution).

## Granting users access to Cloud resources

If you want your app to read user data from another Google service, you'll need to set up [OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/OAuth2WebServer). For example, if you want to pull a user's data from Google Drive and bring it into your app, use OAuth 2.0 for Web Server Applications to share specific data while keeping other data, such as usernames and passwords, private.

### Google Workspace domain-wide delegation of authority

If you have a Google Workspace (formerly G Suite) domain, an administrator of the domain can authorize an application to access user data on behalf of users in the Google Workspace domain. For example, an application that uses the Google Calendar API to add events to the calendars of all users in a Google Workspace domain would use a service account to access the Google Calendar API on behalf of users.

Authorizing a service account to access data on behalf of users in a domain is sometimes referred to as "delegating domain-wide authority" to a service account. This still uses OAuth 2.0, and requires a Google Workspace domain administrator to [authorize domain-wide authority to the service account](https://developers.google.com/identity/protocols/OAuth2ServiceAccount#delegatingauthority).

## Specifying a service account

App Engine lets you use two types of service accounts:

  * **Per-version service account** : A service account configured as the identity for a specific version of your deployed service. When deploying an existing version or a new version, you can specify a service account to act as that version's identity. For example, if a version requires permissions that differ from the app-level default service account, you can assign a service account that is specific to that version. For more information, see [Configure App Engine service accounts](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts).

**Note:** Instances in flexible environment require Logs Writer, Monitoring Metric Writer, and Storage Object Viewer roles. If you remove Editor role from the App Engine default service account, or if you are using a per-version service account, make sure to grant the service account these roles. In the Google Cloud console, you can find these roles under **Logging > Logs Writer**, **Monitoring > Monitoring Metric Writer**, and **Monitoring > Storage Object Viewer** respectively.

  * **App-level default service account** : If you don't configure a per-version service account, Google Cloud uses the app-level default service account for all of your deployed services. You assign the app-level default service account when you create the app. For more information, see [Assign an app-level default service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-accounts#assign_an_app-level_default_service_account).

If you don't assign an app-level default service account, Google Cloud uses the auto-created [App Engine default service account](https://docs.cloud.google.com/appengine/docs/flexible/default-service-account) (`PROJECT_ID@appspot.gserviceaccount.com`).

Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
