---
url: https://docs.cloud.google.com/iam/docs/migrating-to-credentials-api/
title: Migrating to the Service Account Credentials API \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:14.195260+00:00
---

# Migrating to the Service Account Credentials API  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/migrating-to-credentials-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Migrating to the Service Account Credentials API Stay organized with collections  Save and categorize content based on your preferences. 

The [Service Account Credentials API](https://docs.cloud.google.com/iam/docs/reference/credentials/rest) creates short-lived credentials for Identity and Access Management (IAM) service accounts. You can also use this API to sign JSON Web Tokens (JWTs), as well as blobs of binary data that contain other types of tokens.

The [IAM API](https://docs.cloud.google.com/iam/docs/reference/rest) also contains methods for signing JWTs and binary blobs. As of July 1, 2020, these methods are deprecated in the REST API and in all [client libraries](https://docs.cloud.google.com/iam/docs/write-policy-client-libraries) for the IAM API. Also, if you use the Google Cloud CLI to sign JWTs, you might need to add a new claim to the JWT Claims Set. You can still use the deprecated methods, but they don't support advanced features like [HTTP request batching](https://developers.google.com/people/v1/batch). We encourage you to migrate to the Service Account Credentials API instead.

Compared to the IAM API, the Service Account Credentials API provides more flexibility for the expiration time of signed JWTs. In addition, the Service Account Credentials API adds multiple new API methods to generate impersonation tokens.

This page explains how to update your existing code to use the Service Account Credentials API. If you have feedback on this change, you can [complete the feedback form](https://docs.google.com/forms/d/e/1FAIpQLScbtyMsPmVVHZjM2QH0jQLy3bteyd306EjJyW7OtU4Zeg-9yw/viewform). You can also use the email address [iam-sign-deprecation-public@google.com](mailto:iam-sign-deprecation-public@google.com) to request support and provide detailed feedback.

## Before you begin

  * Enable the Service Account Credentials API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)




## Enabling audit logs

If you want to receive [audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) for requests to sign JWTs and blobs, you must [enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) for the IAM API. Enabling Data Access audit logs for the IAM API also enables these audit logs for the Service Account Credentials API.

There are a few notable differences between the log entries that each API generates:

Differences for audit log entries  
---  
Method name |  **IAM API** The method name (`protoPayload.methodName`) is one of the following: 

  * `google.iam.admin.v1.SignBlob`
  * `google.iam.admin.v1.SignJwt`

**Service Account Credentials API** The method name is one of the following: 

  * `SignBlob`
  * `SignJwt`

  
Request type |  **IAM API** The request type (`protoPayload.request.@type`) is one of the following: 

  * `type.googleapis.com/google.iam.admin.v1.SignBlobRequest`
  * `type.googleapis.com/google.iam.admin.v1.SignJwtRequest`

**Service Account Credentials API** The request type is one of the following: 

  * `type.googleapis.com/google.iam.credentials.v1.SignBlobRequest`
  * `type.googleapis.com/google.iam.credentials.v1.SignJwtRequest`

  
Service name |  **IAM API** The service name (`protoPayload.serviceName`) is `iam.googleapis.com`.  **Service Account Credentials API** The service name is `iamcredentials.googleapis.com`.   
  
Data Access audit logs count toward your free monthly allotment of logging data ingestion. If you exceed this allotment, you will be charged for log ingestion. For details, see [Pricing for Google Cloud Observability](https://docs.cloud.google.com/stackdriver/pricing).

## Migrating code for signing JWTs

This section describes how to migrate code that signs JWTs to the Service Account Credentials API.

### Signing JWTs with the REST API

The following table shows the differences between [signing a JWT with the IAM REST API](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/signJwt) and [signing a JWT with the Service Account Credentials API](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signJwt). Update your code to reflect these differences:

Differences for signing a JWT  
---  
HTTP endpoints |  **IAM API** The IAM API uses the following HTTP methods and endpoints: 

  * `POST https://iam.googleapis.com/v1/projects/project-id/serviceAccounts/sa-email:signJwt` In this URL, `project-id` is the project ID, and `sa-email` is the email address for the service account. 
  * `POST https://iam.googleapis.com/v1/projects/-/serviceAccounts/sa-email:signJwt` In this URL, the wildcard character `-` takes the place of the project ID, and `sa-email` is the email address for the service account. 

**Service Account Credentials API** Use the following HTTP method and endpoint. _Do not_ replace the wildcard character with the project ID:  `POST https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/sa-email:signJwt` In this URL, `sa-email` is the email address for the service account.   
Request body |  **IAM API** The request body includes a `payload` field. Its value is the JWT payload to sign. The payload must be a JSON object, serialized as a string, that contains a JWT Claims Set. If you provide an expiration time (`exp`) claim, it must be no more than _12 hours_ in the future. If you omit the `exp` claim, it _is added automatically_ and is set to _1 hour_ in the future. **Service Account Credentials API** The request body includes a `payload` field that is identical to the IAM API, except for the behavior of the expiration time (`exp`) claim:

  * If you provide the `exp` claim, it must be no more than _12 hours_ in the future.
  * If you omit the `exp` claim, it _is not added automatically_. **You must provide this claim if you use the signed JWT to authenticate with Google APIs, or with another API that requires the`exp` claim.**

  
Response body |  Both APIs use the same fields in the response body.  
  
### Signing JWTs with a client library

The client libraries for the Service Account Credentials API are separate from the client libraries for the IAM API.

To use the Service Account Credentials API, add its client library to your application, and update your code to use the new client library:

### C#

Add the [Service Account Credentials client library for C#](https://googleapis.dev/dotnet/Google.Apis.IAMCredentials.v1/latest/api/Google.Apis.IAMCredentials.v1.html) to your application. Use the [`SignJwt()` method](https://googleapis.dev/dotnet/Google.Apis.IAMCredentials.v1/latest/api/Google.Apis.IAMCredentials.v1.ProjectsResource.ServiceAccountsResource.html) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [IAM client library for C#](https://developers.google.com/api-client-library/dotnet/apis/iam/v1/), you can remove it from your application. 

### Go

Add the [Service Account Credentials client library for Go](https://pkg.go.dev/cloud.google.com/go/iam/credentials/apiv1?tab=doc) to your application. Use the [`IamCredentialsClient.SignJwt() function`](https://pkg.go.dev/cloud.google.com/go/iam/credentials/apiv1?tab=doc#IamCredentialsClient.SignJwt) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [IAM client library for Go](https://pkg.go.dev/google.golang.org/api/iam/v1?tab=doc), you can remove it from your application. 

### Java

Add the [Service Account Credentials client library for Java](https://github.com/googleapis/java-iamcredentials) to your application. Use the [`IamCredentialsClient#signJwt()` method](https://cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient#com_google_cloud_iam_credentials_v1_IamCredentialsClient_signJwt_com_google_cloud_iam_credentials_v1_ServiceAccountName_java_util_List_java_lang_String__java_lang_String_) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [IAM client library for Java](https://github.com/googleapis/google-api-java-client-services/tree/master/clients/google-api-services-iam/v1), you can remove it from your application. 

### Node.js

Add the [Service Account Credentials client library for Node.js](https://github.com/googleapis/google-api-nodejs-client/tree/master/src/apis/iamcredentials) to your application. Use the [`signJwt()` method](https://googleapis.dev/nodejs/googleapis/latest/iamcredentials/classes/Resource$Projects$Serviceaccounts.html#signJwt) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [IAM client library for Node.js](https://github.com/googleapis/google-api-nodejs-client/tree/master/src/apis/iam), you can remove it from your application. 

### PHP

Add the [Service Account Credentials client library for PHP](https://github.com/googleapis/google-api-php-client-services/tree/master/src/IAMCredentials) to your application. Use the [`signJwt()` method](https://github.com/googleapis/google-api-php-client-services/blob/master/src/IAMCredentials/Resource/ProjectsServiceAccounts.php) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [IAM client library for PHP](https://github.com/googleapis/google-api-php-client-services/tree/master/src/Iam), you can remove it from your application. 

### Python

Add the [Service Account Credentials client library for Python](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials) to your application. Use the [`sign_jwt()` method](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_sign_jwt) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [`iam_credentials` client library](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials), you can remove it from your application. 

### Ruby

Add the [Service Account Credentials client library for Ruby](https://github.com/googleapis/google-api-ruby-client/tree/master/generated/google-apis-iamcredentials_v1) to your application. Use the [`sign_service_account_jwt()` method](https://github.com/googleapis/google-api-ruby-client/blob/master/generated/google-apis-iamcredentials_v1/lib/google/apis/iamcredentials_v1/service.rb) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [IAM client library for Ruby](https://github.com/googleapis/google-api-ruby-client/tree/master/generated/google-apis-iam_v1), you can remove it from your application. 

## Migrating code for signing binary blobs

This section describes how to migrate code that signs binary blobs to the Service Account Credentials API.

### Signing binary blobs with the REST API

The following table shows the differences between [signing a binary blob with the IAM REST API](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/signBlob) and [signing a binary blob with the Service Account Credentials API](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signBlob). Update your code to reflect these differences:

Differences for signing a binary blob  
---  
HTTP endpoints |  **IAM API** The IAM API uses the following HTTP methods and endpoints: 

  * `POST https://iam.googleapis.com/v1/projects/project-id/serviceAccounts/sa-email:signBlob` In this URL, `project-id` is the project ID, and `sa-email` is the email address for the service account. 
  * `POST https://iam.googleapis.com/v1/projects/-/serviceAccounts/sa-email:signBlob` In this URL, the wildcard character `-` takes the place of the project ID, and `sa-email` is the email address for the service account. 

**Service Account Credentials API** Use the following HTTP method and endpoint. _Do not_ replace the wildcard character with the project ID:  `POST https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/sa-email:signBlob` In this URL, `sa-email` is the email address for the service account.   
Request body |  **IAM API** The request body includes a `bytesToSign` field. Its value is a base64-encoded string that represents the binary blob to sign. **Service Account Credentials API** The request body includes a `payload` field that has the same value as the `bytesToSign` field in the IAM API.  
Response body |  **IAM API** The response body contains a `keyId` field, which identifies the key that was used to sign the blob, and a `signature` field, which contains a base64-encoded string that represents the signature. **Service Account Credentials API** The response body contains a `keyId` field that is identical to the `keyId` field in the IAM API, as well as a `signedBlob` field that is identical to the `signature` field in the IAM API. **Note:** The `signedBlob` field contains only the signature, not the original blob.  
  
### Signing binary blobs with a client library

The client libraries for the Service Account Credentials API are separate from the client libraries for the IAM API.

To use the Service Account Credentials API, add its client library to your application, and update your code to use the new client library:

### C++

**If you use the Cloud Storage C++ client library to sign blobs,** either directly or as a dependency of another client library: 

Upgrade to version 0.9.0 or later of [`google-cloud-cpp`](https://github.com/googleapis/google-cloud-cpp/tree/master/google/cloud/storage). 

**If you use another client library to sign blobs:**

Contact [`iam-sign-deprecation-public@google.com`](mailto:iam-sign-deprecation-public@google.com) for support. 

### C#

**If you use the[IAM client library for C#](https://developers.google.com/api-client-library/dotnet/apis/iam/v1/),** either directly or as a dependency of another client library: 

Add the [Service Account Credentials client library for C#](https://googleapis.dev/dotnet/Google.Apis.IAMCredentials.v1/latest/api/Google.Apis.IAMCredentials.v1.html) to your application. Use the [`SignBlob()` method](https://googleapis.dev/dotnet/Google.Apis.IAMCredentials.v1/latest/api/Google.Apis.IAMCredentials.v1.ProjectsResource.ServiceAccountsResource.html) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [IAM client library for C#](https://developers.google.com/api-client-library/dotnet/apis/iam/v1/), you can remove it from your application. 

**If you use the Firebase Admin DotNet SDK,** either directly or as a dependency of another client library: 

Upgrade to version 1.17.1 or later of [`firebase-admin-dotnet`](https://github.com/firebase/firebase-admin-dotnet). 

**If you use another client library to sign blobs:**

Contact [`iam-sign-deprecation-public@google.com`](mailto:iam-sign-deprecation-public@google.com) for support. 

### Go

**If you use the[IAM client library for Go](https://pkg.go.dev/google.golang.org/api/iam/v1?tab=doc),** either directly or as a dependency of another client library: 

Add the [Service Account Credentials client library for Go](https://pkg.go.dev/cloud.google.com/go/iam/credentials/apiv1?tab=doc) to your application. Use the [`IamCredentialsClient.SignBlob() function`](https://pkg.go.dev/cloud.google.com/go/iam/credentials/apiv1?tab=doc#IamCredentialsClient.SignBlob) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [IAM client library for Go](https://pkg.go.dev/google.golang.org/api/iam/v1?tab=doc), you can remove it from your application. 

**If you use the Firebase Admin Go SDK,** either directly or as a dependency of another client library: 

Upgrade to version 4.1.0 or later of [`firebase-admin-go`](https://github.com/firebase/firebase-admin-go). 

**If you use another client library to sign blobs:**

Contact [`iam-sign-deprecation-public@google.com`](mailto:iam-sign-deprecation-public@google.com) for support. 

### Java

**If you use the[IAM client library for Java](https://github.com/googleapis/google-api-java-client-services/tree/master/clients/google-api-services-iam/v1),** either directly or as a dependency of another client library: 

Add the [Service Account Credentials client library for Java](https://github.com/googleapis/java-iamcredentials) to your application. Use the [`IamCredentialsClient#signBlob()` method](https://cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient#com_google_cloud_iam_credentials_v1_IamCredentialsClient_signBlob_java_lang_String_java_util_List_java_lang_String__com_google_protobuf_ByteString_) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [IAM client library for Java](https://github.com/googleapis/google-api-java-client-services/tree/master/clients/google-api-services-iam/v1), you can remove it from your application. 

**If you use the Google Auth Library for Java,** either directly or as a dependency of another client library: 

Upgrade to version 0.14.0 or later of [`google-auth-library-java`](https://github.com/googleapis/google-auth-library-java). 

**If you use the Firebase Admin Java SDK,** either directly or as a dependency of another client library: 

Upgrade to version 7.0.1 or later of [`firebase-admin-java`](https://github.com/firebase/firebase-admin-java). 

**If you use another client library to sign blobs:**

Contact [`iam-sign-deprecation-public@google.com`](mailto:iam-sign-deprecation-public@google.com) for support. 

### Node.js

**If you use the[IAM client library for Node.js](https://github.com/googleapis/google-api-nodejs-client/tree/master/src/apis/iam),** either directly or as a dependency of another client library: 

Add the [Service Account Credentials client library for Node.js](https://github.com/googleapis/google-api-nodejs-client/tree/master/src/apis/iamcredentials) to your application. Use the [`signBlob()` method](https://googleapis.dev/nodejs/googleapis/latest/iamcredentials/classes/Resource$Projects$Serviceaccounts.html#signBlob) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [IAM client library for Node.js](https://github.com/googleapis/google-api-nodejs-client/tree/master/src/apis/iam), you can remove it from your application. 

**If you use the Google Auth Library for Node.js,** either directly or as a dependency of another client library: 

Upgrade to version 6.0.0 or later of [`google-auth-library-nodejs`](https://github.com/googleapis/google-auth-library-nodejs). 

**If you use the Firebase Admin Node.js SDK,** either directly or as a dependency of another client library: 

Upgrade to version 8.13.0 or later of [`firebase-admin-node`](https://github.com/firebase/firebase-admin-node). 

**If you use another client library to sign blobs:**

Contact [`iam-sign-deprecation-public@google.com`](mailto:iam-sign-deprecation-public@google.com) for support. 

### PHP

**If you use the[IAM client library for PHP](https://github.com/googleapis/google-api-php-client-services/tree/master/src/Iam),** either directly or as a dependency of another client library: 

Add the [Service Account Credentials client library for PHP](https://github.com/googleapis/google-api-php-client-services/tree/master/src/IAMCredentials) to your application. Use the [`signBlob()` method](https://github.com/googleapis/google-api-php-client-services/blob/master/src/IAMCredentials/Resource/ProjectsServiceAccounts.php) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [IAM client library for PHP](https://github.com/googleapis/google-api-php-client-services/tree/master/src/Iam), you can remove it from your application. 

**If you use the Google Auth Library for PHP,** either directly or as a dependency of another client library: 

Upgrade to version 1.5.0 or later of [`google-auth-library-php`](https://github.com/googleapis/google-auth-library-php). 

**If you use another client library to sign blobs:**

Contact [`iam-sign-deprecation-public@google.com`](mailto:iam-sign-deprecation-public@google.com) for support. 

### Python

**If you use the[IAM client library for Python](https://github.com/googleapis/python-iam),** either directly or as a dependency of another client library: 

Add the [Service Account Credentials client library for Python](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials) to your application. Use the [`sign_blob()` method](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_sign_blob) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [`iam_credentials` client library](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials), you can remove it from your application. 

**If you use the Google Auth Library for Python,** either directly or as a dependency of another client library: 

Upgrade to version 1.21.2 or later of [`google-auth`](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth). 

**If you use the Python client for Cloud Storage,** either directly or as a dependency of another client library: 

Upgrade to version 1.30.0 or later of [`python-storage`](https://github.com/googleapis/python-storage). 

**If you use another client library to sign blobs:**

Contact [`iam-sign-deprecation-public@google.com`](mailto:iam-sign-deprecation-public@google.com) for support. 

### Ruby

**If you use the[IAM client library for Ruby](https://github.com/googleapis/google-api-ruby-client/tree/master/generated/google-apis-iam_v1),** either directly or as a dependency of another client library: 

Add the [Service Account Credentials client library for Ruby](https://github.com/googleapis/google-api-ruby-client/tree/master/generated/google-apis-iamcredentials_v1) to your application. Use the [`sign_service_account_blob()` method](https://github.com/googleapis/google-api-ruby-client/blob/master/generated/google-apis-iamcredentials_v1/lib/google/apis/iamcredentials_v1/service.rb) to generate a signature. 

The name of the service account must use the wildcard character `-` to represent the project ID: 

Valid: Name with wildcard character 
    
    
    projects/**-** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

Invalid: Name with project ID 
    
    
    projects/**my-project** /serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    

If you no longer use the [IAM client library for Ruby](https://github.com/googleapis/google-api-ruby-client/tree/master/generated/google-apis-iam_v1), you can remove it from your application. 

**If you use another client library to sign blobs:**

Contact [`iam-sign-deprecation-public@google.com`](mailto:iam-sign-deprecation-public@google.com) for support. 

## Migrating code that uses the gcloud CLI

The Google Cloud CLI provides commands that use the IAM API to sign JWTs and binary blobs, including the following:

  * [`gcloud beta iam service-accounts sign-jwt`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/sign-jwt)
  * [`gcloud iam service-accounts sign-blob`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/sign-blob)



On or after July 1, 2021, we will update these commands to use the Service Account Credentials API. This change will not affect commands to sign blobs.

**If you use the gcloud CLI to sign JWTs, you must follow these steps before July 1, 2021:**

  1. Check whether you include the expiration time (`exp`) claim in the JWT Claims Set.

If you already include this claim, you do not need to make any changes. You can skip the remaining steps.

If you do not include this claim, continue to the next step.

  2. Check whether you use the signed JWT to authenticate with Google APIs, or with another API that requires the `exp` claim.

If you omit this claim, the IAM API automatically sets it to 1 hour in the future. In contrast, the Service Account Credentials API does not set this field automatically.

If you are sure that you do not need the `exp` claim, you do not need to make any changes. You can skip the remaining steps.

If you know that you need the `exp` claim, or if you aren't sure, continue to the next step.

  3. Update your code for creating JWTs so that it adds the `exp` claim to the JWT Claims Set.

You can set the `exp` claim up to 1 hour in the future.




## Checking quotas

Quota for the Service Account Credentials API is separate from quota for the IAM API. If you have received a quota increase to sign JWTs and blobs with the IAM API, you might also need to request an increase for the Service Account Credentials API.

**Note:** Most Google Cloud customers use the default quota for signing JWTs and blobs. If you use the default quota, you do not need to read this section.

To view your quota and actual usage for both APIs, and to request a quota increase if necessary, do the following:

  1. In the Google Cloud console, go to the **Quotas** page.

[Go to the Quotas page](https://console.cloud.google.com/projectselector/iam-admin/quotas)

  2. Select a project. You can click a recent project, or you can click **Select project** to search all of your projects.

  3. In the **Filter table** text box above the table, enter `Sign requests per minute`, then select the value that appears.

  4. In the **Filter table** text box, select **OR** from the drop-down list.

  5. In the **Filter table** text box, enter `Generate credentials`, then select the value that appears.

The Google Cloud console shows your current usage for signing JWTs and blobs over the past minute; your peak usage per minute over the past 7 days; and your current quota, which appears in the **Limit** column.

  6. Compare the quotas for each row in the table, and ensure that your quota for the Service Account Credentials API is higher than your 7-day peak usage of the IAM API.

  7. Optional: If your quota for the Service Account Credentials API is too low, select the checkbox for the Service Account Credentials API, then click **Edit quotas**. Complete the form to request a quota increase.

  8. Repeat these steps for each project where you use the IAM API to sign JWTs and blobs.




## What's next

  * Find out how to [create a signed JWT](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-jwt) or [create a signed binary blob](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-blob) with the Service Account Credentials REST API.
  * Get details about the [REST API for the Service Account Credentials API](https://docs.cloud.google.com/iam/docs/reference/credentials/rest).
  * Understand [quotas and limits for IAM](https://docs.cloud.google.com/iam/quotas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
