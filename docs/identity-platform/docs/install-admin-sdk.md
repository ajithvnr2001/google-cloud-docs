---
url: https://docs.cloud.google.com/identity-platform/docs/install-admin-sdk/
title: Installing the Admin SDK \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:06.053651+00:00
---

# Installing the Admin SDK  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/install-admin-sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Installing the Admin SDK

This document shows you how to install the Identity Platform Admin SDK. The Admin SDK lets you manage Identity Platform from a server environment, and perform administrator actions such as migrating users, setting custom claims, and configuring identity providers.

## Before you begin

To use the Admin SDK, you need a server app running one of the following:

Language | Minimum framework version  
---|---  
Node.js | Node.js 8.13.0+  
Java | Java 7+ (Java 8+ recommended)  
Python | Python 2.7+ or 3.4+ (3.4+ recommended)  
Go | Go 1.9+  
C# | .NET Framework 4.5+ or .NET Core 1.5+  
  
The following table lists the features supported by each SDK language:

Feature | Node.js | Java | Python | Go | C#  
---|---|---|---|---|---  
[Custom token minting](https://firebase.google.com/docs/auth/admin/create-custom-tokens) |  |  |  |  |   
[ID token verification](https://firebase.google.com/docs/auth/admin/verify-id-tokens) |  |  |  |  |   
[User management](https://firebase.google.com/docs/auth/admin/manage-users) |  |  |  |  |   
[Control access with custom claims](https://firebase.google.com/docs/auth/admin/custom-claims) |  |  |  |  |   
[Refresh token revocation](https://firebase.google.com/docs/auth/admin/manage-sessions) |  |  |  |  |   
[Import users](https://firebase.google.com/docs/auth/admin/import-users) |  |  |  |  |   
[Session cookie management](https://firebase.google.com/docs/auth/admin/manage-cookies) |  |  |  |  |   
[Generating email action links](https://firebase.google.com/docs/auth/admin/email-action-links) |  |  |  |  |   
[ Managing SAML/OIDC provider configurations](https://cloud.google.com/identity-cp/docs/managing-providers-programmatically) |  |  |  |  |   
[ Multi-tenancy support](https://cloud.google.com/identity-platform/docs/multi-tenancy) |  |  |  |  |   
[Realtime Database](https://firebase.google.com/docs/database/admin/start) |  |  |  | * |   
[Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/server#firebase-admin-sdk-for-fcm) |  |  |  |  |   
[FCM Multicast](https://firebase.google.com/docs/cloud-messaging/send-message#send-messages-to-multiple-devices) |  |  |  |  |   
[Manage FCM topic subscriptions](https://firebase.google.com/docs/cloud-messaging/manage-topics) |  |  |  |  |   
[Cloud Storage](https://firebase.google.com/docs/storage/admin/start) |  |  |  |  |   
[Firestore](https://firebase.google.com/docs/firestore) |  |  |  |  |   
Project Management |  |  |  |  |   
[Security rules](https://firebase.google.com/docs/rules/manage-deploy) |  |  |  |  |   
[ML model management](https://firebase.google.com/docs/ml/manage-hosted-models) |  |  |  |  |   
[Firebase Remote Config](https://firebase.google.com/docs/remote-config/automate-rc) |  |  |  |  |   
[Firebase App Check](https://firebase.google.com/docs/app-check/custom-provider) |  |  |  |  |   
[Firebase Extensions](https://firebase.google.com/docs/extensions/publishers/lifecycle-events) |  |  |  |   
  
### Console

  1. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Other > Identity Toolkit Admin** role to the service account. 

To grant the role, find the **Select a role** list, then select **Other > Identity Toolkit Admin**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 

  2. Create a service account key: 

     1. In the Google Cloud console, click the email address for the service account that you created. 
     2. Click **Keys**. 
     3. Click **Add key** , and then click **Create new key**. 
     4. Click **Create**. A JSON key file is downloaded to your computer. 
     5. Click **Close**. 



### gcloud

  1. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant the `roles/identitytoolkit.admin` IAM role to the service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=roles/identitytoolkit.admin

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     4. Generate the key file: 
            
            gcloud iam service-accounts keys create FILE_NAME.json --iam-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace the following: 

        * `FILE_NAME`: a name for the key file
        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account



## Installing the SDK

### Node.js

The Node.js Admin SDK is available on npm. If you don't already have a `package.json` file, create one using `npm init`. Next, install the npm package and save it to your `package.json`:
    
    
    npm install firebase-admin --save
    

To use the module in your app, `require` it from any JavaScript file:
    
    
    var admin = require('firebase-admin');
    

If you are using ES2015, you can `import` the module instead:
    
    
    import * as admin from 'firebase-admin';
    

### Java

The Java Admin SDK is published to the Maven central repository. To install the library, declare it as a dependency in your `build.gradle` file:
    
    
    dependencies {
      implementation 'com.google.firebase:firebase-admin:6.11.0'
    }
    

If you use Maven to build your app, you can add the following dependency to your `pom.xml`:
    
    
    <dependency>
      <groupId>com.google.firebase</groupId>
      <artifactId>firebase-admin</artifactId>
      <version>6.11.0</version>
    </dependency>
    

### Python

The Python Admin SDK is available using [pip](https://pypi.python.org/pypi/pip).
    
    
    pip install --user firebase-admin
    

### Go

Use the `go get` utility to install the Go Admin SDK:
    
    
    go get firebase.google.com/go
    

### C#

Install the .NET Admin SDK using the .NET package manager:
    
    
    Install-Package FirebaseAdmin -Version 1.9.1
    

Alternatively, install it using the `dotnet` command-line utility:
    
    
    dotnet add package FirebaseAdmin --version 1.9.1
    

Or, you can install it by adding the following package reference entry to your `.csproj` file:
    
    
    <ItemGroup>
      <PackageReference Include="FirebaseAdmin" Version="1.9.1" />
    </ItemGroup>
    

## Initializing the SDK using default credentials

Add the following code to your server app to initialize the Admin SDK using the default credentials:

### Node.js
    
    
    // Initialize the default app
    var admin = require('firebase-admin');
    var app = admin.initializeApp({
      credential: admin.credential.applicationDefault()
    });
    

### Java
    
    
    FirebaseApp.initializeApp();
    
    [FirebaseAppSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAppSnippets.java#L71-L71)

### Python
    
    
    default_app = firebase_admin.initialize_app()
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L45-L45)

### Go
    
    
    app, err := firebase.NewApp(context.Background(), nil)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }
    
    [init.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/init.go#L60-L63)

### C#
    
    
    FirebaseApp.Create();
    
    
    [FirebaseAppSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/c08a6533b109f960bfec5eaa93a55126dd62fe9e/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAppSnippets.cs#L69-L69)

## Initializing the SDK with a service account key file

You can also manually specify a service account key file:

### Node.js
    
    
    // Initialize the default app
    var admin = require('firebase-admin');
    var app = admin.initializeApp({
      credential: admin.credential.cert('/path/to/serviceAccountKey.json')
    });
    

### Java
    
    
    FileInputStream serviceAccount = new FileInputStream("path/to/serviceAccountKey.json");
    
    FirebaseOptions options = FirebaseOptions.builder()
        .setCredentials(GoogleCredentials.fromStream(serviceAccount))
        .setDatabaseUrl("https://<DATABASE_NAME>.firebaseio.com/")
        .build();
    
    FirebaseApp.initializeApp(options);
    
    [FirebaseAppSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAppSnippets.java#L34-L41)

### Python
    
    
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import exceptions
    
    cred = credentials.Certificate('path/to/serviceAccountKey.json')
    default_app = firebase_admin.initialize_app(cred)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L34-L39)

### Go
    
    
    opt := option.WithCredentialsFile("path/to/serviceAccountKey.json")
    app, err := firebase.NewApp(context.Background(), nil, opt)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }
    
    [init.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/init.go#L35-L39)

### C#
    
    
    FirebaseApp.Create(new AppOptions()
    {
        Credential = CredentialFactory.FromFile<ServiceAccountCredential>("path/to/serviceAccountKey.json").ToGoogleCredential(),
    });
    
    
    [FirebaseAppSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/c08a6533b109f960bfec5eaa93a55126dd62fe9e/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAppSnippets.cs#L28-L31)

## Initializing multiple apps

Typically, you'll only want to initialize a single, default app. However, you can also create multiple app instances, each with its own configuration options and authentication state.

### Node.js
    
    
    // Initialize the default app
    admin.initializeApp(defaultAppConfig);
    
    // Initialize another app with a different config
    var otherApp = admin.initializeApp(otherAppConfig, 'other');
    
    console.log(admin.app().name);  // '[DEFAULT]'
    console.log(otherApp.name);     // 'other'
    
    // Use the shorthand notation to retrieve the default app's services
    var defaultAuth = admin.auth();
    

### Java
    
    
    // Initialize the default app
    FirebaseApp defaultApp = FirebaseApp.initializeApp(defaultOptions);
    
    // Initialize another app with a different config
    FirebaseApp otherApp = FirebaseApp.initializeApp(otherAppConfig, "other");
    
    System.out.println(defaultApp.getName());  // "[DEFAULT]"
    System.out.println(otherApp.getName());    // "other"
    
    // Use the shorthand notation to retrieve the default app's services
    FirebaseAuth defaultAuth = FirebaseAuth.getInstance();
    FirebaseDatabase defaultDatabase = FirebaseDatabase.getInstance();
    
    // Use the otherApp variable to retrieve the other app's services
    FirebaseAuth otherAuth = FirebaseAuth.getInstance(otherApp);
    FirebaseDatabase otherDatabase = FirebaseDatabase.getInstance(otherApp);
    
    [FirebaseAppSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAppSnippets.java#L105-L120)

### Python
    
    
    # Initialize the default app
    default_app = firebase_admin.initialize_app(cred)
    
    #  Initialize another app with a different config
    other_app = firebase_admin.initialize_app(cred, name='other')
    
    print(default_app.name)    # "[DEFAULT]"
    print(other_app.name)      # "other"
    
    # Retrieve default services via the auth package...
    # auth.create_custom_token(...)
    
    # Use the `app` argument to retrieve the other app's services
    # auth.create_custom_token(..., app=other_app)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L85-L98)

### Go
    
    
    // Initialize the default app
    defaultApp, err := firebase.NewApp(context.Background(), nil)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }
    
    // Initialize another app with a different config
    opt := option.WithCredentialsFile("service-account-other.json")
    otherApp, err := firebase.NewApp(context.Background(), nil, opt)
    if err != nil {
    	log.Fatalf("error initializing app: %v\n", err)
    }
    
    // Access Auth service from default app
    defaultClient, err := defaultApp.Auth(context.Background())
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }
    
    // Access auth service from other app
    otherClient, err := otherApp.Auth(context.Background())
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }
    
    [init.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/init.go#L102-L125)

### C#
    
    
    // Initialize the default app
    var defaultApp = FirebaseApp.Create(defaultOptions);
    
    // Initialize another app with a different config
    var otherApp = FirebaseApp.Create(otherAppConfig, "other");
    
    Console.WriteLine(defaultApp.Name); // "[DEFAULT]"
    Console.WriteLine(otherApp.Name); // "other"
    
    // Use the shorthand notation to retrieve the default app's services
    var defaultAuth = FirebaseAuth.DefaultInstance;
    
    // Use the otherApp variable to retrieve the other app's services
    var otherAuth = FirebaseAuth.GetAuth(otherApp);
    
    
    [FirebaseAppSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/c08a6533b109f960bfec5eaa93a55126dd62fe9e/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAppSnippets.cs#L103-L116)

## Setting scopes

If you're using a Compute Engine VM with Google Application Default Credentials for authentication, you''ll need to set the right [access scopes](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes). Identity Platform requires the `userinfo.email` and `cloud-platform` access scopes.

To check your existing access scopes, run the following:
    
    
    gcloud compute instances describe [INSTANCE-NAME] --format json
    

The command will return information about the service account. For example:
    
    
    "serviceAccounts": [
     {
      "email": "example.gserviceaccount.com",
      "scopes": [
       "https://www.googleapis.com/auth/cloud-platform",
       "https://www.googleapis.com/auth/userinfo.email"
       ]
      }
    ]
    

To update access scopes, stop the VM, then run the following:
    
    
    gcloud compute instances set-service-account [INSTANCE-NAME] \
      --service-account "your.gserviceaccount.com" \
      --scopes ""https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/userinfo.email"
    

## What's next

  * View the source code and additional documentation for the Admin SDK on GitHub: 
    * [Node.js](https://github.com/firebase/firebase-admin-node)
    * [Java](https://github.com/firebase/firebase-admin-java)
    * [Python](https://github.com/firebase/firebase-admin-python)
    * [Go](https://github.com/firebase/firebase-admin-go)
    * [C#](https://github.com/firebase/firebase-admin-dotnet)
  * [Migrate existing users to Identity Platform](https://docs.cloud.google.com/identity-platform/docs/migrating-users)
  * [Manage SAML and OIDC providers programmatically](https://docs.cloud.google.com/identity-platform/docs/managing-providers-programmatically)
  * [Manage Identity Platform tenants](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-managing-tenants)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
